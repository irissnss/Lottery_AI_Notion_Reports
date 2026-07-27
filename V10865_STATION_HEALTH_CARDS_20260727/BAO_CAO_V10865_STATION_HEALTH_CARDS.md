# V10865 — Bốn card sức khỏe theo đài trên cùng

## Correct owner target

Owner xác định nhóm cần sửa tại `/du-doan-test`:

- TP. HCM — TB 17%;
- Cà Mau — YẾU 0%;
- Đồng Tháp — YẾU 0%;
- Gộp miền — YẾU 17%.

V10864 đã sửa nhầm nhóm Governance.

## Root cause

Audit trước mock `/api/slice-health` thành unavailable nên bốn card live không xuất
hiện trong bằng chứng tự động.

Runtime cũ:

- đặt `#sliceHealthBadgeTest` bên trong header;
- render mỗi card thành `inline-block`;
- chèn `<br>` thủ công trước card Gộp miền;
- không có grid hoặc equal-height contract.

Khi station/status có độ dài khác nhau, card tự co và làm cả header lệch.

## Fix

- Di chuyển panel sức khỏe ra khỏi header, đặt riêng dưới tabs MN/MT/MB.
- Desktop: grid 4 cột.
- Mobile ≤760px: grid 2×2.
- `grid-auto-rows:1fr`; mỗi card `height:100%`, `min-width:0`.
- Tách station, trạng thái/tỷ lệ và n/base thành ba dòng rõ ràng.
- Giữ nguyên payload, status, màu và tooltip.

## Real-data verification

Payload thật `/api/slice-health?region=MN`, weekday T2.

| Engine / viewport | Geometry |
|---|---|
| Chromium 320 | 4 × 143×76, 2×2 |
| WebKit 320 | 4 × 140×76, 2×2 |
| Chromium 390 | 4 × 178×76, 2×2 |
| WebKit 390 | 4 × 175×76, 2×2 |
| Chromium 430 | 4 × 198×76, 2×2 |
| WebKit 430 | 4 × 195×76, 2×2 |
| Chromium 768/1024 | 4 × 175×76, 4×1 |
| WebKit 768/1024 | 4 × 174×76, 4×1 |
| Chromium 1366 | 4 × 261×76, 4×1 |
| WebKit 1366 | 4 × 259×76, 4×1 |

Tất cả 12 case: equal width/height, zero card/body overflow, panel ngoài header,
pageerror 0.

## Deploy

- MD5 local=VPS `93cf13e8e4a14d6333e847c29133d8f6`.
- Frontend-only, không restart.
- Health 200; slice-health 200; lane guest 401; journal 0.
- Bốn bảng official SHA256 trước/sau IDENTICAL.
- Backup VPS `/root/backups_v10865/du-doan-test.html`.
- Backup local `backups/v10865_pre/du-doan-test.html`.

## Safety

Không đổi slice-health data/API, prediction, prompt, writer, selector, scheduler,
official output hoặc lane primary 20/20.

## Status

`DEPLOYED_PENDING_LIVE_VERIFY`: chờ owner hard-refresh và xác nhận đúng nhóm card
TP.HCM/Cà Mau/Đồng Tháp/Gộp miền.

Notion short page: `3aa1d385-9bf8-811a-9a9e-f00fc172b6fb`.

Commits gốc: private `331de77`; public `20350a4`.

