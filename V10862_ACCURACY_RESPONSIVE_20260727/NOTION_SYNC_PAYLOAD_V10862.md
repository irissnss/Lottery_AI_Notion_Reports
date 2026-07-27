# V10862 — Morning check + `/accuracy` responsive

- Owner báo `/accuracy` méo cả mobile/desktop, chữ bị đẩy khỏi vùng đọc.
- Root 1: mobile `input width:100%` áp nhầm checkbox.
- Root 2: model chart giữ inline min-width 160px, bóp bar/text.
- Root 3: desktop lặp sidebar + top navigation, 1024px xuống hai hàng.
- Root 4: tên model dùng font KPI 2rem nên gãy méo.
- Fix checkbox 16px + label canh trái.
- ≤360px KPI chuyển một cột; model-name có clamp/ellipsis guard.
- Model chart mobile chuyển grid, label tách hàng.
- Ẩn duplicate top navigation khi sidebar đã inject.
- Chromium+WebKit, 320/390/1024/1366: 8/8 PASS.
- Body overflow false; checkbox 16px; pageerror 0.
- MD5 local=VPS=served: `289559e41891a1af632091c1e4e0c3bd`.
- Frontend-only, không restart; health/accuracy 200; journal 0.
- Hash 4 bảng official pre/post IDENTICAL.
- Morning: self-check 11/11, contract PASS, MN 15+12 row không rỗng.
- Bundle MN BT 42 `[42,32]`; trace PB-18.1 27/27, fallback 0.
- Status: DEPLOYED_PENDING_OWNER_EYE.
- Báo cáo gốc: https://github.com/irissnss/Lottery_AI_Notion_Reports/tree/main/V10862_ACCURACY_RESPONSIVE_20260727
- Commits gốc: private `2f4dbcb`; public `9c0e7fe`.

