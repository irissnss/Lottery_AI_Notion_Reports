# CONVERSATION CONTEXT — V11018 · 2026-08-07

## Owner nói gì (NGUYÊN VĂN)

> khẩn trương đi em, sắp tới giờ block rồi rm

Cửa sổ deploy đóng **15:00–18:45**. Lúc owner nhắc là **~14:30**.

Trước đó owner duyệt hướng:

> ok tiếp đi em.

Việc gốc, owner nêu 07/08:

> *"Với ML ngoài xác xuất thống kê thuần, anh quan tâm đến **đối chứng với rules, bộ lọc** để so
> sánh đối chiếu để output **số chính và nhẹ hơn là số phụ**."*

## Agent làm gì dưới sức ép thời gian

Xếp lại thứ tự: **đẩy phần cần máy chủ lên trước 15:00, tài liệu và báo cáo làm sau** — vì tài
liệu không đụng VPS nên không bị cửa sổ chặn.

Deploy xong lúc **14:33**. Tài liệu và báo cáo viết sau đó.

## Kết quả — trả lời thẳng câu owner hỏi

| số nguồn cùng chỉ | n | trúng | tỉ lệ |
|---|---|---|---|
| 1 nguồn | 2.658 | 1.159 | **43,60%** |
| 2 nguồn | 516 | 245 | **47,48%** |
| **3 nguồn** | **24** | 8 | **33,33%** |

**z (3 vs 1) = −1,01** ⇒ **KHÔNG CÓ LỢI THẾ**.

Đuôi được cả ba nguồn cùng chỉ **trúng THẤP HƠN** đuôi chỉ một nguồn.

## Vấp ở đâu — một nguồn CHẾT mà bảng vẫn ra số

Bản đầu dò hàm bộ lọc bằng **tên đoán**: `run_filter` · `filter_2_so_cuoi` · `run` · `compute`.
**Không hàm nào tồn tại.** Nguồn `LOC` ra **0 dòng** — và bảng **vẫn chạy trơn tru**, vẫn ra
bảng tỉ lệ, vẫn có kết luận. Chỉ là kết luận của **hai nguồn đội lốt ba**.

Đúng lỗi V11015 đã mắc — lần đó đoán tên **tệp** (`ml_train.py` không tồn tại), lần này đoán
tên **hàm**. Sửa: đọc tên thật từ mã nguồn ⇒ `get_filter_data_with_cascade` ⇒ **743 → 3.250 dòng**.

**Kiểu hỏng này nguy hiểm nhất** vì không có gì báo lỗi — chỉ có một con số nhỏ hơn bình thường
mà không ai biết bình thường là bao nhiêu. Mở **FU-327**.

## Điều agent NÓI THẲNG với owner

**1. Số nói ĐỪNG LÀM cái owner đang muốn.** Owner muốn dùng đối chứng ba nguồn để tách số chính
/ số phụ. Số hiện tại: 3 nguồn **33,3%** vs 1 nguồn **43,6%**. Không có căn cứ.

**2. Đây là lần THỨ HAI cơ chế "nhiều nguồn cùng chỉ" đi ngược.** §5g từng đo `z = −2,54` — ô 3
nguồn là ô **tệ nhất** — và đã phải gỡ khỏi prompt ở V11014. Hai phép đo độc lập, hai bộ nguồn
khác nhau, **cùng một hướng**.

**3. Nhóm 3 nguồn chỉ có 24 lượt — mỏng, agent nói thẳng.** Nhưng nó mỏng **vì ba nguồn hiếm
khi cùng chỉ một đuôi**: 3.231 dòng mới có 24 lần. Bản thân điều đó đã là câu trả lời — cơ chế
đồng thuận ba nguồn **hầu như không kích hoạt**, nên kể cả nếu tốt cũng gần như không dùng được.

**4. Ngưỡng chốt TRƯỚC:** `z ≥ +1,96` ⇒ mới bàn đưa vào cách chọn số · `z ≤ −1,96` ⇒ ghi SSOT
**cấm dựng lại** cơ chế cộng điểm theo số nguồn dưới bất kỳ tên nào. Viết thẳng vào mã nguồn và
panel để sau này không ai bẻ ngưỡng cho vừa kết quả.

**5. Agent làm việc này ở dạng SHADOW, không gắn thẳng vào ML.** Owner hỏi *"có đối chứng
không"* — câu trả lời đúng không phải *"em gắn vào rồi"* mà *"em đo xem có ích không đã"*. §5g
là ví dụ của việc đi thẳng từ trực giác vào prompt production mà không đo.
