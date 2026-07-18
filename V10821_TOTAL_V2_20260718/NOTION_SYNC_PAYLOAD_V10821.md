# V10821 — Ngày-1 RULES-FIRST + TOTAL-V2 shadow (18/07/2026)

**Owner flag 19:39:** "Total và /choi cần có 1 phương pháp mới với tín hiệu dàn trải ở các model và ở bt và số phụ? cần kiểm tra và có kế hoạch cụ thể."

**Ngày-1 trial V10820 (PB-18.1):**
- Tuân thủ 21/21 main trong danh sách rules (100%, baseline 24-30%); biến-thể phụ 0/21.
- LLM official any 15/21 (MN 6/7 · MT 5/7 với 2 WIN · MB 4/7); bầy shadow bám 67 ngoài rules — 67 KHÔNG về.
- GĐB-đảo: ứng viên 54 VỀ lô MB ngay ngày-1 (mai theo dõi 62).
- Hệ thống sạch: 28 trace PB-18.1, 0 lỗi journal, scorer + eval đủ.
- **Điểm trừ: bundle BT 0/3** — MN số 13 VỀ nằm 2 main + 2 phụ mà bundle chốt 31 (7 phiếu main); MB 86 VỀ nằm 1 main + 3 phụ mà chốt 93. Tầng vote cũ chỉ đếm main, số phụ chìm, không neo rules.

**Backtest 165 ngày (leak-safe 0%):** M2s COVERAGE-RULES (1 model = 1 phiếu mỗi số chạm kể cả phụ + ưu tiên số trong rules) BT-lô **MN 48.6% / MT 44.3% / MB 32.9%** vs bundle hiện tại 42.9/39.3/21.4; 60 ngày gần +10/+8.3/+15pp. DÀN-4 any MN 88.6/MT 82.9/MB 68.6.

**Đã deploy (shadow, ZERO đụng /du-doan //choi/writer):** bảng `v10821_total_v2_daily` (backfill 471 rows) + cron 19:14 + API `/api/admin/total-v2` + panel 🧮 TOTAL-V2 /monitoring (60s). Restart gate chờ daily-eval xong; hash 3 bảng IDENTICAL + eval natural growth.

**Kế hoạch:** forward 19→28/07 đọc cùng cửa sổ trial V10820. 25/07 giữa kỳ (M2s−M0 giữ dấu +). **28/07 chốt: ≥ +5pp BT gộp 3 miền → trình owner ký promote scoring bundle = coverage-rules (/choi tự hưởng); ≤ +2pp → đóng giữ M0.** Play-style dàn-4 cho /choi = kèo vốn riêng owner quyết sau.

**Chi tiết đầy đủ:** GitHub `Lottery_AI_Notion_Reports/V10821_TOTAL_V2_20260718/`
