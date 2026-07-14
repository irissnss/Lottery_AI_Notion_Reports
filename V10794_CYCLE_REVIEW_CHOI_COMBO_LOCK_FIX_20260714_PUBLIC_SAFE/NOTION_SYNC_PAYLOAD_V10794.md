# V10794 — Tổng kết chu kỳ live 09-13/07 + fix race khóa combo /choi MB (14/07)

**Kết quả chính:**
- K11a MB 5 ngày: challenger +1.2M (BT 1/5, ăn 3/5) vs champion +6.1M (BT 1/5, ăn 3/5) — champion dẫn CHỈ nhờ 1 ngày đúp 11/07; 13/07 challenger BT WIN đầu tiên (89✓). Chưa chạm kill. Checkpoint 16/07.
- K15 MT 4 ngày: challenger +1.6M ≥ champion (−3.3M) cả 4/4 ngày, BT 2/4 vs 1/4. Checkpoint 17/07.
- Selector forward 5 ngày: MN cả 3 bộ ÂM SÂU (−9.2 → −23.9M) NGƯỢC backfill → forward-test cứu khỏi quyết định sai, KHÔNG đổi MN. MB trio +6.1M (BT 3/5) đáng theo dõi. Tổng kết 14d: 23/07.
- /choi tuần 06-13/07: +23.4M stake-adjusted (MT +16.4 · MB +7.9 · MN −1.2). Khóa tuần mới 13-19/07 tự chọn đúng hạn (MB lần đầu gộp `MB_OUTPUT_V1+AE`).
- 🐛 FIX: race khóa số /choi MB — lock 17:36 thiếu leg `MB_OUTPUT_V1` (17:55) → 13/07 lock 41,31 thay vì 89,41 (89 WIN, P&L may mắn hoà). Fix: chỉ freeze khi đủ 2 leg hoặc qua cutoff. Test 5 case PASS, deploy 09:11, hash 4 bảng IDENTICAL.

**Quyết định cần owner:**
- CP-L6 (lean roster, hạn 14/07): đề xuất DỜI 19/07 gộp CP-R4 — không cắt model giữa cửa sổ đo K11a/K15. Chờ anh: (a) dời · (b) làm ngay · (c) huỷ.
- 41 bảng chết CP-L3 chờ OK drop.

**Đề xuất:** K11a giữ đến 16/07, K15 giữ đến 17/07, MN không đổi, 23/07 xét selector MB.

**Chi tiết đầy đủ:** GitHub `Lottery_AI_Notion_Reports/V10794_CYCLE_REVIEW_CHOI_COMBO_LOCK_FIX_20260714_PUBLIC_SAFE/BAO_CAO_V10794.md`
