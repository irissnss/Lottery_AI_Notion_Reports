# V10864 — 4 Governance cards bằng tuyệt đối

- Owner reject V10863: nhóm 4 card vẫn nhìn lệch.
- Root: columns bằng nhau nhưng Mode token dài tràn sang card kế bên.
- Token: `MN_MT_TEST_LANE_LIVE_PARALLEL_V52_5`.
- Fix grid equal rows; mỗi card min-width 0, height 100%, overflow hidden.
- Mode pill block width 100%.
- Chỉ cho xuống dòng sau dấu `_`, không bẻ chữ tùy tiện.
- Chromium 320: 4 card 141×85.
- WebKit 320: 4 card 138×85.
- Chromium 390: 4 card 176×72.
- WebKit 390: 4 card 173×72.
- Chromium+WebKit 320–1366: 12/12 PASS.
- Equal width/height true; card/mode/body overflow false; pageerror 0.
- Deploy MD5 `c3fed0037e8de1f34e4111912606d05d`.
- Frontend-only, không restart; health 200; journal 0.
- Hash-4 official pre/post IDENTICAL.
- Không đổi API/prompt/writer/selector/scheduler/lane 20/20.
- Status: DEPLOYED_PENDING_LIVE_VERIFY — chờ owner xác nhận mắt.
- Báo cáo gốc: https://github.com/irissnss/Lottery_AI_Notion_Reports/tree/main/V10864_EQUAL_CARDS_20260727
- Commits gốc: private `dc43a8b`; public `929a75f`.

