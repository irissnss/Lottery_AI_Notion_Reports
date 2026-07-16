# V10811 — BT vs SỐ PHỤ (bệnh của MT) + fix /monitoring chết JS 7 ngày + verify pending (16/07/2026)

**Câu owner:** "Tín hiệu trúng đa phần nằm ở số phụ không? Kiểm tra đơn model số phụ và bạch thủ. Shadow nay sao rồi? Kiểm tra toàn diện vấn đề đang treo."

**Kết quả chính:**
1. "Trúng nằm ở số phụ" = bệnh CỦA MT, không phải toàn hệ. 14d: MT phụ 38.0% > BT 29.2% (AI-SHD); MB NGƯỢC (BT 29.1% > phụ 21.3%); MN cân. Hôm 16/07: MN thắng thật (official WIN đôi, 14/26 model trúng BT); MT 3 BT / 12 chỉ-phụ; MB AI official trượt trắng.
2. MT không thiếu tín hiệu — tín hiệu xếp NHẦM VỊ TRÍ (72 từ MN nổ lại MT ở vị trí phụ; lane AE BT=19 trúng đôi trong khi official chọn 40). → MT hưởng lợi lớn nhất nếu ký CP-L6 (nhãn per-số + gate g′).
3. BUG THẬT: /monitoring chết TOÀN BỘ JS từ tối 09/07 — `const SS` khai báo trùng (khối V10790-B vs V10787-F) → SyntaxError giết nguyên script 4578 dòng → 7 ngày panel không render (owner chưa từng thấy BEST SPOTS, SHADOW A/B). Fix đổi SS→SW + gate mới `node --check` trước mọi deploy html.
4. Panel mới 🎯 TRÚNG NẰM Ở ĐÂU (BT vs SỐ PHỤ) live trong SO GĂNG /monitoring — metric chính phu_only (phụ trúng BT trượt).
5. Shadow A/B V10809 day-1 đủ 15/15 + scored: **B 8 vs A 7** (MT 4−2, MB 1−0, MN 3−5). SE3 mới: qwen arm B pick trùng [00,00] — theo dõi, không vá giữa kỳ.
6. Pending verify: C16 budget MB **CLOSED** (budget_catchup selected=20 sống); T-chốt V10798 ngày 2 đúng nhịp + watchdog 0 báo giả → FU-V10798/V10799 LIVE_VERIFIED; cron tối 19:05/19:10/19:15 đủ cả 3; self-check 10/11 PASS (FAIL = retrain bệnh cũ chờ CN 19/07); K11a MB d8: promote BT 1/8 < champion 3/8 (3 ngày champion đúng bị làm hỏng) — trio checkpoint 23/07 quyết.

**Deploy:** 2 file (`_v10773_three_layer_scoreboard.py` + `monitoring.html`), restart OK, health 200, hash 4 bảng PRE=POST IDENTICAL. Backup `v10811_pre/`. Không đụng /du-doan, lane, prompt production.

**Chờ owner:** (1) mở /monitoring xác nhận panel sống lại; (2) CP-L6 19/07; (3) API key mới dán vào /settings rồi gọi em (cửa sổ an toàn đến ~03:30 mỗi đêm).

**GitHub:** `Lottery_AI_Notion_Reports/V10811_BT_PHU_JS_FIX_20260716_PUBLIC_SAFE/` (báo cáo đầy đủ + evidence raw + context).
