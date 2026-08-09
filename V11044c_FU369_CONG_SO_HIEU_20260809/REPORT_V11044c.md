# REPORT V11044c — FU-369: CỔNG CẤP SỐ HIỆU QUÉT SÁU NƠI

**Ngày:** 2026-08-09 11:20–11:45 · **Tầng verdict:** `REPORT_PROVEN` (tooling, không runtime)

## 1. Tóm tắt
Số hiệu va chạm **5 lần trong 2 ngày** (`QD-028`·`QD-043`·`QD-046`·mã đọc `SC0908-4`·`V11043`).
Dựng cổng quét **SÁU nơi** trả số trống tiếp theo, phân biệt KHAI BÁO với NHẮC TỚI.

## 2. Owner yêu cầu (nguyên văn)
> FU-369 — LÀM TRƯỚC TIÊN TRONG GĐ-4: cổng cấp số hiệu quét BỐN nơi (V·FU·QD·mã đọc §58) +
> thử allow/deny thật (RM-15).

## 3. Đào bới
Đề bài ghi «4 nơi» nhưng khảo sát cho **SÁU**: CHANGELOG · FOLLOW_UP · thư mục reports · **tên
tệp `_v*.py`** (đang giữ số CAO HƠN CHANGELOG — đây là chỗ cách cũ mù) · **`OWNER_DECISION_LEDGER.json`**
(nơi duy nhất khai QD) · **git log** (FU-372: hai commit cùng V11037). CLAUDE.md gần vô dụng.

Bẫy dương-tính-giả thật: `V99999`/`V99998` (sổ giả thử cổng), câu «QD-054 TRỐNG — dùng được»
(văn xuôi), `FU-901`/`FU-902` (dữ liệu thử), `LX` là hai chữ cái không phải `L+số`.

## 4. Hướng xử lý
Chỉ đếm **KHAI BÁO** (neo tiêu đề `## V`/`### FU-` · tên tệp · tên thư mục · `"id": "QD-"`),
bỏ văn xuôi. Trần loại dữ liệu thử: V≤19999 · FU≤899 · QD≤899.

## 5. Đã làm
`web/backend/_v11044_cong_so_hieu.py`: in số trống mỗi loại, hoặc kiểm một mã TRỐNG/ĐÃ DÙNG.
Kết quả: V trống tiếp **V11045** · FU **FU-386** · QD **QD-055** · 222 mã đọc đã khai báo.

## 6. Cổng kiểm (ngưỡng owner + RM-15)
- Chạy 2 lần liên tiếp ra **CÙNG** số (ổn định) ✓
- Tạo `_v11045_gia.py` ⇒ số trống nhảy **V11045 → V11046** ✓ (bắt được tên tệp)
- Gỡ tệp giả ⇒ về **V11045** ✓
- Trần loại `V99999`/`FU-901` khỏi kết quả ✓

## 7. Vướng vấp
Khảo sát ban đầu (workflow) tự bắt lỗi RM-10: viết `L[0-9]+` cho LX ⇒ sót 67 mã; sửa thành
`([0-9]{4}|LX)`. Cổng thừa hưởng bản đã sửa.

## 8. Gỡ về
`rm web/backend/_v11044_cong_so_hieu.py` — cổng độc lập, không ai phụ thuộc.

## 9. Theo dõi tiếp
FU-350 · FU-377 · FU-360 · FU-375 (GĐ-4). Tối nay 18:05/19:35 đóng FU-373/FU-366.

## LOCK-IN / OPEN / NEXT
**LOCK-IN:** cổng cấp số 6 nơi, ổn định + nhảy-qua đã chứng minh, bắt được tên tệp CHANGELOG bỏ sót.
**OPEN:** ba câu owner (nhóm B · v81 · viewer.js).
**NEXT:** FU-350 → FU-377 → FU-360 → FU-375; verify tối nay.

*Đẩy cùng commit (A55).*
