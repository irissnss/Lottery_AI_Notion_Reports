# V10822 — Rules chấm/xếp hạng NGÀY+TUẦN (câu 1) + LANE TOTAL_V2_RULES_V1 để anh CHƠI từ 19/07 (câu 2)

**Owner 21:00 18/07:** "1/ Rules có được tổng hợp phân tích xếp hạng hàng ngày hàng tuần không? 2/ Lane test có xử lý được không — anh muốn 1 luồng output mới để chơi 10 ngày tới."

**Câu 1 — CÓ, đủ 2 nhịp:**
- Hàng ngày 20:15: MRE chấm từng rule (2.978 rows / 205 ngày liên tục).
- Hàng ngày 20:30 (MB, cửa sổ 8W) + 04:40 & 20:35 (MN/MT, 12W/16W + vòng đời MẠNH→YẾU): re-rank 1..35, snapshot riêng từng miền.
- Hàng tuần T2 00:30: đào lại toàn bộ (hiện v2026W29, 105 rules, 21 đợt).

**Câu 2 — ĐƯỢC, lane đã live:**
- Lane `TOTAL_V2_RULES_V1` 3 miền chạy phương pháp M2s coverage-rules (backtest 165d thắng bundle +5.7→+11.6pp BT), ghi số TRƯỚC giờ xổ: MN 15:47 · MT 16:56 · MB 17:56.
- Danh sách rules tính LIVE (rules active + KQ đài nguồn đã quay) — không nhìn trộm tương lai; hệ lane tự chấm điểm mỗi tối.
- /choi + official MIỄN NHIỄM: method mới cần ≥24-30 ngày mới được vào khóa tuần → 10 ngày tới thuần song song.
- **Anh lấy số chơi:** /monitoring panel 🧮 → khối 🚏 (vàng): "hôm nay BT=xx bộ2=[..] lúc HH:MM" + lịch sử ✓/✗.

**Bonus vá bug V10821:** cron shadow 19:14 chạy TRƯỚC giờ chấm rules 20:15 → cột rules ngày mới luôn trống (M2s âm thầm = M1). Dời 20:50 + chấm lại 18/07: MT [41,46] 46✓, MB [93,86] 86✓ → M2s any ngày-1 2/3.

**Verify:** dry-run khớp shadow; hash 4 bảng official IDENTICAL; health 200/admin 401; journal sạch; backup 2 đầu.

**Mốc:** 19/07 rows lane đầu · 28/07 đọc cùng V10820/V10821 · ~12-17/08 lane đủ điều kiện ứng viên khóa tuần /choi.

**Chi tiết:** GitHub `Lottery_AI_Notion_Reports/V10822_TOTAL_V2_LANE_20260718/`
