# V10800 — Audit toàn hệ 3 miền × 3 luồng + mốc học tập → fix retrain/optimizer CN chết ngầm (15/07, DEPLOYED)

**Owner 12:54:** "MN anh chả thấy em đề cập gì… toàn bộ 3 miền, 3 luồng… mốc giờ retrain, học tập phân tích, xếp hạng rules, pattern… cơ chế tổng hợp số ngày số tuần còn đúng không… phải kiểm tra định kỳ. Xem lại toàn diện 1 lần nữa."

**Phát hiện lớn (từ bảng giờ toàn hệ 43 job + 40 cron đối chiếu DB thật):**
- Auto Retrain CN 02:00 **FAILED 4/6 tuần** (14/06→12/07, lỗi `I/O operation on closed file` cả 12 model×miền — stdout service bị đóng). Model 6 tuần nay sống nhờ guard 06:30 → chu kỳ học THẬT ~8-10 ngày, không phải hằng tuần.
- Weight optimizer CN 03:00 **chết cùng lỗi** (lần thật gần nhất 10/07 do weekly_guard fallback).
- Chứng cứ chéo: cùng pipeline chạy qua subprocess thành công 100% → lỗi môi trường process.

**Fix (một đường chạy duy nhất):** retrain CN 02:00 = subprocess `retrain_guard --force`; optimizer CN 03:00 = subprocess `_run_optimizer_once.py` (bỏ hardcode /root + đọc metric setting); guard 06:30 + weekly_guard 07:00 giữ nguyên backstop kép; `training_history` ghi OK/FAILED thật.

**Self-check định kỳ MỚI:** `_v10800_timetable_selfcheck.py` cron T2 08:10 — 10 bất biến (tuổi model, marker, retrain, rules/cau/pattern fresh, MDE, T-chốt, lane, bundle, weekly lock). Chạy ngay: **9/10 PASS** — FAIL duy nhất `retrain_OK_in_8d` = đúng bệnh vừa fix.

**MN verify đủ 8 ngày:** shadow MN về 04:19-04:45 sáng (pool đủ 26 từ ~04:45); chốt 15:45 regen pool ĐỦ (vote đổi 4/8 ngày — mốc có giá trị); BT1 /choi lock-vs-final khớp 8/8; bundle updated 16:3x = ghi kết quả, không đổi picks; lane MN 04:30 partial-pool vĩnh viễn = caveat đo lường (không promote, không /choi) — không sửa, giữ baseline K16.

**Mốc học tập verify đúng hết:** v10708 04:40+20:35 · MB rules 04:45/17:00/20:30 · mining T2 00:30 · cau T2 04:50 (320d) · pattern V10763 post-closeout · MDE 20:20 (26 model) · selector 15:56/16:56/17:56 + settle 21:30 · champion 06:00 · scrape khớp 16:34/17:30/18:32. Cửa sổ: strength 30d · money board 60/30d + weekly lock T2 (13/07 đủ 3 miền; MB 14/07 lock 17:58 đủ 2 leg = bằng chứng sống fix V10794) · retrain 300/500d. `pattern_rules` legacy 0 active — không phải bug.

**Deploy:** 3 file + cron; restart active; health 200; hash 4 bảng pre=post IDENTICAL; rollback sẵn `/root/backups/v10800_pre/`.

**Verify sống:** CN 19/07 (retrain 02:00 + optimizer 03:00 chạy thật) · T2 21/07 (self-check ALL PASS) · tối 15/07 chuỗi V10798/V10799.

**GitHub:** `Lottery_AI_Notion_Reports/V10800_FULL_SYSTEM_TIMETABLE_AUDIT_20260715_PUBLIC_SAFE/` (báo cáo đầy đủ + conversation context).
