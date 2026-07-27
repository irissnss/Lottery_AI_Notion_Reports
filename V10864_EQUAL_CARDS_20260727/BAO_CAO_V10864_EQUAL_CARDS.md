# V10864 — Cân bằng tuyệt đối 4 Governance cards

## Owner rejection

Owner không chấp nhận nhóm bốn card còn nhìn lệch sau V10863.

## Root cause

Bốn column thực tế đã cùng chiều rộng, nhưng giá trị Mode
`MN_MT_TEST_LANE_LIVE_PARALLEL_V52_5` là một token không có điểm xuống dòng.
Pill tràn qua biên card đầu sang card `official_output`, làm toàn nhóm nhìn như
chia không đều.

## Fix

- Grid dùng `grid-auto-rows: 1fr`.
- Từng card có `min-width:0`, `height:100%`, `overflow:hidden`.
- Mode pill là block width 100%.
- Chỉ chèn cơ hội xuống dòng sau dấu `_` bằng `<wbr>`.
- Không dùng break tùy tiện giữa chữ.

## Geometry proof

| Engine / viewport | Bốn card |
|---|---|
| Chromium 320 | 141×85 mỗi card |
| WebKit 320 | 138×85 mỗi card |
| Chromium 390 | 176×72 mỗi card |
| WebKit 390 | 173×72 mỗi card |
| Chromium 430 | 196×72 mỗi card |
| WebKit 430 | 193×72 mỗi card |
| Chromium 768/1024 | 175×72 mỗi card |
| WebKit 768/1024 | 173×72 mỗi card |
| Chromium 1366 | 260×58 mỗi card |
| WebKit 1366 | 259×58 mỗi card |

Tất cả 12 case:

- equal width = true;
- equal height = true;
- card overflow = false;
- Mode overflow = false;
- body overflow = false;
- pageerror = 0.

## Deploy

- `du-doan-test.html` local=VPS MD5:
  `c3fed0037e8de1f34e4111912606d05d`.
- Frontend-only; không restart.
- Health 200; lane guest 401; journal error-level 0.
- SHA256 bốn bảng official trước/sau IDENTICAL.
- Backup VPS `/root/backups_v10864/du-doan-test.html`.
- Backup local `backups/v10864_pre/du-doan-test.html`.

## Safety

Không thay đổi API, dữ liệu, prompt, scheduler, writer, selector, `/du-doan`,
official output hoặc contract lane primary 20/20.

## Trạng thái

`DEPLOYED_PENDING_LIVE_VERIFY`: chờ owner hard-refresh và xác nhận bằng mắt đúng
nhóm bốn Governance cards.

Notion short page: `3aa1d385-9bf8-8184-9148-db15b32d4a8f`.

