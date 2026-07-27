# V10862 — Kiểm tra đầu ngày và sửa `/accuracy` mobile/desktop

## Kết luận

Owner phản ánh đúng: trang không tạo horizontal scroll nên audit hình học cũ báo PASS,
nhưng bố cục vẫn méo và chữ bị đẩy/bóp trên thiết bị thật. V10862 đã xác định bốn
nguyên nhân, sửa và deploy trực tiếp lên VPS.

## Kiểm tra hệ thống đầu ngày 27/07

Nguồn paired live: `artifacts/live_sync/20260727_084030/manifest.json`.

- Timetable self-check: 11/11 PASS.
- Cross-module contract V10841: PASS; pool/canon 15 model mỗi miền.
- Service active; `/api/health=200`; `/accuracy=200`; journal error-level = 0.
- SQLite `quick_check=ok`.
- MN: 15 official + 12 shadow, không row rỗng.
- Bundle MN: BT 42, lo2 `[42,32]`, 15 model.
- Trace: 27/27 PB-18.1, rules injected 27/27, fallback 0.
- Weekly money-board lock: đủ MN/MT/MB.
- V10861 sáng: MN display/capital `[42]`; MT/MB pending đúng deadline.
- `PATTERN-REASONING_ERR=0`.

## Root cause `/accuracy`

1. CSS mobile dùng `.filter-bar input { width:100% }`, vô tình áp cho checkbox.
   Checkbox chiếm nguyên hàng và đẩy nhãn “Chỉ CHOT_HA / Chỉ Win” sang phải.
2. Model chart có inline `min-width:160px`; trên màn hình hẹp, bar và số liệu bị bóp.
3. Desktop vừa có sidebar mới vừa còn top navigation cũ; ở 1024px header xuống hai hàng.
4. Card “model tốt nhất” dùng font KPI số 2rem nên tên model dài bị gãy méo.

Đây là lỗi visual-readability; kiểm tra chỉ dựa vào `body.scrollWidth` không phát hiện được.

## Fix

- Checkbox có width cố định 16px; label full-row và canh trái.
- Ở ≤360px, KPI chuyển một cột.
- Tên model dùng font clamp, nowrap và ellipsis guard.
- Mobile model chart chuyển grid: label một hàng; bar + thông tin ở hàng dưới.
- `min-width:0` và `break-word` cho các phần tử động.
- Khi sidebar đã inject, ẩn top navigation legacy trên desktop và mobile.
- Bổ sung accessible labels cho toàn bộ filter/backtest controls.

## Xác minh trước và sau deploy

| Engine | Viewport | Body overflow | Checkbox | KPI | Duplicate nav | Page error |
|---|---:|---|---:|---|---|---:|
| Chromium | 320 | false | 16px | 1 cột | hidden | 0 |
| Chromium | 390 | false | 16px | 2 cột | hidden | 0 |
| Chromium | 1024 | false | 16px | 4 cột | hidden | 0 |
| Chromium | 1366 | false | 16px | 4 cột | hidden | 0 |
| WebKit | 320 | false | 16px | 1 cột | hidden | 0 |
| WebKit | 390 | false | 16px | 2 cột | hidden | 0 |
| WebKit | 1024 | false | 16px | 4 cột | hidden | 0 |
| WebKit | 1366 | false | 16px | 4 cột | hidden | 0 |

Tất cả test dùng trang VPS và production API thật, không dùng dữ liệu tĩnh.

## Deploy safety

- Frontend-only; không restart service.
- `accuracy.html` local = VPS = served:
  `289559e41891a1af632091c1e4e0c3bd`.
- Health/accuracy 200; journal error-level 0.
- SHA256 bốn bảng official trước/sau deploy IDENTICAL:
  `predictions`, `final_bundles`, `lottery_results`, `model_daily_eval`.
- Backup VPS: `/root/backups_v10862/accuracy.html`.
- Backup local: `backups/v10862_pre/accuracy.html`.

## Trạng thái

`DEPLOYED_PENDING_OWNER_EYE`: bằng chứng tự động đã PASS; owner cần hard-refresh
`/accuracy` trên điện thoại và desktop để xác nhận bằng mắt.

Notion short page: `3aa1d385-9bf8-81f7-baf7-e9e93118cb7b`.

