# V10865 — 4 card sức khỏe theo đài

- Owner xác định đúng nhóm: TP.HCM, Cà Mau, Đồng Tháp, Gộp miền.
- V10864 đã sửa nhầm nhóm Governance.
- Root: audit mock slice-health unavailable nên bỏ sót card live.
- Root: card là inline spans nằm trong header, dùng `<br>` thủ công.
- Fix: chuyển thành panel riêng dưới tabs.
- Mobile: grid 2×2; desktop: 4 cột.
- Equal auto rows; mỗi card height 100%, min-width 0.
- Payload giữ nguyên: TP.HCM TB17%, Cà Mau YẾU0%, Đồng Tháp YẾU0%, Gộp miền YẾU17%.
- Chromium 320: 4 card 143×76.
- WebKit 320: 4 card 140×76.
- Chromium 390: 4 card 178×76.
- WebKit 390: 4 card 175×76.
- Chromium+WebKit 320–1366: 12/12 PASS.
- Equal width/height, zero overflow/pageerror, panel ngoài header.
- Deploy MD5 `93cf13e8e4a14d6333e847c29133d8f6`.
- Health/slice-health 200; journal 0; hash-4 identical.
- Không đổi data/API/prompt/writer/selector/scheduler/lane 20/20.
- Status: DEPLOYED_PENDING_LIVE_VERIFY.
- Báo cáo gốc: https://github.com/irissnss/Lottery_AI_Notion_Reports/tree/main/V10865_STATION_HEALTH_CARDS_20260727
- Commits gốc: private `331de77`; public `20350a4`.

