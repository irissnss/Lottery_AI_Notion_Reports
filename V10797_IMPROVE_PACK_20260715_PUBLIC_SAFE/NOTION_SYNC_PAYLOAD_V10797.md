# V10797 — Sửa P1 theo khóa xổ + CP-L6 giải trình + GLM checkpoint + gói cải tiến (15/07 sáng, read-only)

**Trigger:** owner sửa ràng buộc — MT khóa xổ 17:00 (dời 17:05 vô dụng), MB khóa 18:00 (17:56 tàm tạm), hỏi CP-L6 là gì, yêu cầu đề xuất cải tiến từ DB/live.

**Kết quả chính:**
- P1 sửa: **MT KHÔNG dời bundle** (16:38 giữ, đo lệch pool đủ 14d đến 24/07); **MB đề xuất 17:50-17:52** (sau shadow 17:47-48, user còn 8-10' trước khóa 18:00) — chờ owner gật.
- CP-L6 = checkpoint tùy chọn Lean Harvest 19/06: cắt model đắt (opus $15/M + gpt-5.4 $5/M) khỏi bộ gọi ngày. Counterfactual 90d: cắt khỏi vote gần như vô hại (±1 ngày/91/miền) NHƯNG tiết kiệm nhỏ ~$10/th, cả hai đang trong roster lane đo (budget MT 14/14 · MN 15/15), opus carry-quality cao nhất bể (46%). Khuyến nghị: dời 19/07 quyết cùng CP-R4, hoặc huỷ.
- GLM checkpoint (9 ngày): 5.1 top1 38%/1 EMPTY vs 5.2 top1 37%/0 EMPTY/ít token hơn → HOÀ, 5.2 ổn định hơn → đề xuất retire glm-5.1 tại 19/07.
- Gói cải tiến từ DB: #1 MB selector-trio forward BT 3/6=50% +3.4M → 23/07 trình K16 promote MB; #2 MB pool-full 17:50; #3 K11a 16/07 + K15 17/07; #4 MT 24/07; #5 MN giữ nguyên; #6 housekeeping roster 1 lần 19/07.

**Chờ owner ký:** (a) P1B MB 17:50? (b) CP-L6: dời/làm/huỷ? (c) retire glm-5.1 tại 19/07?

**An toàn:** read-only 100%, không deploy; hash 4 bảng tăng trưởng tự nhiên.

**Chi tiết:** GitHub public `V10797_IMPROVE_PACK_20260715_PUBLIC_SAFE/BAO_CAO_V10797_FULL.md`
