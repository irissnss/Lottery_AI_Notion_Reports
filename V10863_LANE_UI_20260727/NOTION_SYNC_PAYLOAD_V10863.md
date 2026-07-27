# V10863 — Lane-test UI + sidebar navigation

- Owner yêu cầu card lane-test ngay ngắn như `/choi`, bỏ nút điều hướng lặp.
- Root: `#app.loading` không được gỡ sau render → padding + căn giữa sai.
- Root: mobile giữ comparison 2 cột, card chỉ 121px ở 320px.
- Root: header links rộng 339px, bị cắt và ☰ đè title.
- Root: ba card số dùng flex min-width nên thành 2+1.
- Fix: gỡ loading class sau fetch.
- Fix: ba card số dùng grid đều; Xiên/method wrap an toàn.
- Fix: ≤640px Official/Test xếp dọc full-width có nhãn rõ.
- Fix: header chừa gutter ☰; chỉ giữ Refresh; tabs rút gọn MN/MT/MB.
- Source/Cách hiểu chuyển panel thu gọn như `/choi`.
- Ẩn nav lặp trên lane, `/choi`, monitoring, search, settings.
- Giữ Refresh/filters/regions/time/logout và `/filter` chưa có trong sidebar.
- Live payload MN 27/07: official + test bundle + 46 history rows.
- Chromium+WebKit 320–1366: lane 12/12 PASS.
- Navigation cleanup: 24/24 PASS.
- 320px: cards 93/93/93, compare 289px, overflow false, pageerror 0.
- Deploy 5/5 MD5, frontend-only, không restart.
- Health 200, journal 0, hash-4 official IDENTICAL.
- Không đổi `/du-doan`, prompt, writer, selector, scheduler hay lane 20/20.
- Status: DEPLOYED_PENDING_LIVE_VERIFY — chờ owner xác nhận mắt.
- Báo cáo gốc: https://github.com/irissnss/Lottery_AI_Notion_Reports/tree/main/V10863_LANE_UI_20260727

