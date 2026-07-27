# V10866 — Hoàn tất UI toàn trang và kiểm soát hệ dự đoán

## Owner yêu cầu

- Ghim header trên cùng.
- Kiểm tra và xử lý mọi trang còn lại.
- Không để thay áo/UI gây lỗi hoạt động dự đoán.

## Hệ thống dự đoán tại 14:02

Nguồn paired live:
`artifacts/live_sync/20260727_140204/manifest.json`.

- Timetable self-check: 11/11 PASS.
- V10841 cross-module contract: PASS; canon/pool 15 model mỗi miền.
- Service active, PID 210217; health 200.
- Journal error-level = 0; scheduler ERROR/CRITICAL = 0.
- SQLite quick_check = OK.
- Timing chain 7 ngày: 0 causal violation.
- Known thin margins: MT bundle→lock +1 phút, lock→cutoff +3 phút; MB bundle→lock +2 phút.
- MN: 15 official + 12 shadow, 0 empty.
- Bundle MN: BT42, lo2 `[42,32]`, model_count=15.
- Trace: PB-18.1 27/27, rules 27/27, fallback 0.
- MT/MB có 7 ML rows lúc 14:02 là đúng phase trước AI rolling wave.
- Read-only monitor chạy qua 15:55/16:55/17:55; alert nếu health/error hoặc bundle không exact15.

## UI impact map

14 production pages được phân loại:

- V2 shell sticky đã đúng: index, `/du-doan`, `/choi`, P&L.
- Settings sticky đã đúng.
- Login exempt.
- Cần sửa: lane-test, accuracy, review, monitoring, search, V82,
  user-view và viewer.

## Fix header/navigation

- Lane-test: header sticky; ancestor `overflow-x:hidden` đổi thành `clip`.
- Accuracy: top bar sticky.
- Review: header sticky; sticky-summary dùng ResizeObserver tính đúng offset, không overlap.
- Monitoring: sửa sticky giả do `.app overflow-x:hidden`; mobile header một hàng chừa ☰.
- Search/V82: header sticky, mobile chừa gutter ☰.
- User-view/viewer: own header sticky; không thêm sidebar vào pre-existing self-contained shell.
- Review/P&L/V82: bỏ route buttons trùng sidebar; giữ `/filter`, Reload và controls nghiệp vụ.

## Fix card/clip còn sót

- `/choi`: grid card dùng `minmax(min(310px,100%),1fr)`, hết cắt verdict ở 320px.
- Monitoring dynamic money/play/EV/3-layer grids dùng shrinkable tracks; bỏ hard min-width 285–330px.
- Settings ensemble/retrain buttons và learning tabs wrap trong viewport 320px.
- Viewer bổ sung accessible names cho filter miền/model.
- Wide tables có local scroll wrapper được giữ nguyên, không nhầm thành body overflow.

## Audit mới chống PASS giả

`_v10866_ui_contract_audit.js` kiểm:

- sticky header sau scroll;
- drawer đóng/mở và width ≤260px;
- duplicate navigation;
- body overflow;
- từng element vượt viewport kể cả khi ancestor dùng `overflow:clip`;
- representative `/choi` dynamic cards;
- source gates cho monitoring dynamic min-width.

Kết quả cuối:

- Chromium + WebKit;
- 14 pages × 6 viewports (320/390/430/768/1024/1366);
- 168/168 PASS;
- clipped elements = 0;
- sticky/drawer/nav/body-overflow failures = 0;
- source gates = PASS.

## Deploy

11 HTML files local=VPS MD5 match:

- lane `8cf1b6e4098c2ead6e955bbdddb3ab92`;
- accuracy `359c641065b02cfe5e84942b7b9e3479`;
- review `e6be17fdaee64112c7555f5a1a22682d`;
- monitoring `8dde54571ae6733fd9d077a2fd364ceb`;
- search `96b7509118b7e6ff46b527d5ac9b6736`;
- V82 `014de2502e126eafffd5f16df6b1eb57`;
- user-view `fd7e144a3605e98a5ecc1c631d69dc75`;
- viewer `2db1022452ffb7efd3096175fff4eea6`;
- choi `42230e8da9a7581ac000f8bd9fe2ff88`;
- P&L `84f88f1c423d1248792cb1da8f225b6e`;
- settings `c4435657e5be6f0fc8ea7fcb01f4394b`.

Frontend-only, không restart. Health 200; route matrix đúng; journal 0;
hash bốn bảng official trước/sau IDENTICAL. Rollback:
`/root/backups_v10866/` hoặc `backups/v10866_pre/`.

## Safety

Không thay prompt, scheduler, provider calls, prediction writer, model selector,
`/du-doan`, `final_bundles`, official 15/15 hoặc lane 20/20. Prediction monitor
chỉ SELECT và health-check.

## Trạng thái

UI: `DEPLOYED_PENDING_LIVE_VERIFY` — tự động pass, chờ owner eye-check.

Prediction: sạch tại thời điểm deploy; monitor tiếp tục tới 18:05.

Notion short page: `3aa1d385-9bf8-81a8-919f-e8890ff57e2d`.

Commits gốc: private `e6c9035`; public `7a8edbd`.

