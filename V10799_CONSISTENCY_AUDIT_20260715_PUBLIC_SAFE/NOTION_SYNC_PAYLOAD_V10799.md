# V10799 — Audit ma trận nhất quán 9 luồng sau V10798 + vá 3 lệch sót (15/07, DEPLOYED)

**Owner 10:42:** "nhất quán các luồng lane, official, /choi, đơn model ML mới fix cho MT/MB… anh nhắc cái nào là lòi ra cái đó là sao em? Sau đó tổng hợp tổng lực toàn bộ."

**Cách làm:** rà NGUYÊN MA TRẬN 9 luồng × mốc giờ quanh V10798 (official, lane, promote K11a/K15, /choi + combo V10794, đơn-model ML, selector, AE, watchdog ×2, freeze + UI) thay vì rà theo điểm.

**3 lệch sót tự tìm thấy → vá cùng phiên:**
- Watchdog `T10_EXPECT` còn mốc :50 cũ → sẽ báo động giả "T-chốt chưa fire" mỗi ngày → vá :55 (test 8 case PASS).
- Copy /monitoring còn "T-10 16:45/17:45" + "shadow không phiếu" (sai từ V10798) → sửa nhịp mới.
- Copy /du-doan-test laneTime cũ → 16:53/17:52.

**Replay 7 ngày (bằng chứng):** pool MB 3-6 voter (mốc cũ) → 7-8 (mốc mới, gần gấp đôi); MT 6-8 → 7-9; any-hit ±0-1 → fix cấu trúc pool-đủ, không hứa tăng hit tức thì. Nhất quán by-construction: chốt :54 đọc lane bundle :53/:52 → official = lane từng số.

**Deploy:** 6 file, backup .bak_v10799, restart active, smoke OK, hash 4 bảng IDENTICAL. Rollback 1 lệnh.

**Regime-change 15/07:** mọi checkpoint forward (K11a 16/07, K15 17/07, trio 23/07, lệch 24/07) đọc số phải chú thích trước/sau 15/07.

**GitHub chi tiết:** `Lottery_AI_Notion_Reports/V10799_CONSISTENCY_AUDIT_20260715_PUBLIC_SAFE/`
