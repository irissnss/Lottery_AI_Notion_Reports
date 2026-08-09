# CONVERSATION CONTEXT — V11044c (FU-369) · 2026-08-09

## Owner nói gì
> FU-369 — LÀM TRƯỚC TIÊN TRONG GĐ-4: cổng cấp số hiệu quét BỐN nơi + thử allow/deny (RM-15).

## Agent làm gì & nói thẳng
Đề bài ghi «4 nơi» — nhưng agent **không làm đúng 4 mù quáng**. Khảo sát cho thấy số hiệu nằm ở
**SÁU** nơi, và hai nơi thiếu chính là chỗ đã gây va chạm: **tên tệp `_v*.py`** (giữ số cao hơn
CHANGELOG) và **sổ quyết định JSON** (nơi duy nhất khai QD). Cách cũ chỉ nhìn CHANGELOG nên mù
hai chỗ đó — đó là lý do va chạm 5 lần.

Điều tinh tế nhất: phân biệt **KHAI BÁO** với **NHẮC TỚI**. Câu «QD-054 TRỐNG — dùng được» trong
báo cáo hôm qua, nếu grep thô, bị đọc thành "QD-054 đã dùng". Và sổ giả `V99999` trong tệp thử
cổng khác, nếu không có trần, sẽ được cấp tiếp thành V100000. Cả hai bẫy đều có thật trong kho.

## Vấp
Khảo sát ban đầu tự dính RM-10: viết `L[0-9]+` cho `LX` theo cách đọc §58, sót 67 mã. `LX` là
hai chữ cái nguyên văn. Sửa rồi cổng mới thừa hưởng.
