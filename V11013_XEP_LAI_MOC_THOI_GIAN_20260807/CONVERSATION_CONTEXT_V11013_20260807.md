# CONVERSATION CONTEXT — V11013 · 2026-08-07

## Owner nói gì (NGUYÊN VĂN)

> "cái gì mà đợi tới 24/12 hết năm kiểu này thôi chứ làm gì với dự án bé tẹo này, làm tiếp đi
> nhưng cân đối thời gian hạn mốc tương đối ổn hơn đẹp hơn đi"

## Agent làm gì

1. **Không bào chữa cho mốc 24/12** mà đi tìm vì sao nó dài thế. Hoá ra cổng M4 đặt
   `MAU_TOI_THIEU_DO_TIEN = 20` **cho mỗi luật**, mà mỗi luật chỉ chấm vào đúng THỨ của nó
   ⇒ 1 lượt/tuần ⇒ 140 ngày.
2. **Hỏi lại câu hỏi**: cái đang chặn quyết định FU-291 là *"cơ chế mined_rules có lợi thế
   không"* — câu **LỚP**, gộp được 105 luật, nhịp **15 dòng/ngày**.
3. **Tính lại mẫu cần** bằng công thức McNemar theo cặp, có sức mạnh 80% và α=0,05 —
   ra bảng bốn mức chênh với ngày đạt tương ứng.
4. **Quét phân bố hạn toàn sổ** — phát hiện ngày 13/08 dồn 16 mục, và **hai định dạng ngày**
   làm cổng trần tải đếm sai.
5. **Rải lại theo mức ưu tiên thật**, không rải đều.
6. Khi xếp vào 10/08 thì **cổng QD-022 chặn** (owner đã ký trần 3 mục cho ngày chốt) ⇒ dời 11/08.

## Kết quả

| | trước | sau |
|---|---|---|
| FU-286 | 24/12/2026 | **27/08/2026** |
| FU-285 | 06/11 một phát | **07/09 · 07/10 · 07/11** |
| ngày 13/08 | **16 mục** | **1 mục** |
| ngày xa nhất | 24/12 (139 ngày) | **19/09 (43 ngày)** |

## Vấp ở đâu

### Mốc dài không đến từ việc khó mà từ CÂU HỎI SAI

Agent đặt cổng "n≥20 cho mỗi luật" rồi tính ra 140 ngày, và **báo cáo con số đó như một sự
thật khách quan**. Không hỏi lại: *câu hỏi nào đang thật sự chặn quyết định?*

Câu chặn là câu **lớp** — gộp được, nhanh hơn **15 lần**. Cùng họ với lỗi §60 đã ký: **làm đúng
kỹ thuật nhưng sai phạm vi**.

### Thói quen đặt hạn cho có

**15 trong 16 mục** dồn ngày 13/08 là do agent tự đặt. Nghĩa là khi mở việc mới, agent chọn
"một ngày trông xa xa cho đủ trường" chứ **không cân nhắc mức ưu tiên**.

### Phát hiện phụ — sổ dùng hai định dạng ngày

`2026-08-13` (51 mục) và `13/08` (32 mục) cùng tồn tại. Cổng trần tải J5 đếm theo **chuỗi**, nên
coi đó là **hai ngày khác nhau** ⇒ **ngày nặng thật sự bị giấu đi**. Đã mở FU-314.

### Cổng QD-022 làm đúng việc

Khi agent xếp 3 mục vào 10/08, cổng chặn ngay: owner đã ký 04/08 rằng **10/08 là ngày chốt, trần
3 mục**. Agent dời sang 11/08. Đây là ví dụ cổng ngăn agent phá quyết định cũ của owner.

## Điều agent NÓI THẲNG với owner

**Owner đúng cả hai chỗ.** Mốc 24/12 là lỗi thiết kế phép đo, không phải giới hạn tự nhiên. Và
lịch dồn cục là do agent lười đặt hạn.

**Nhưng ba ngày còn nặng agent KHÔNG tự dời:** 08/08 (10 mục) · 09/08 (9) · 15/08 (12) — đó là
mục của phiên khác. Trình owner xem có giãn không (FU-315).

**Và cách sửa FU-285 đáng nhân rộng:** thay một mốc dài bằng nhiều mốc ngắn có **điều kiện dừng
sớm**. Cùng công sức, thông tin về sớm hơn hai tháng, và nếu kết quả rõ từ mốc đầu thì khỏi chờ
hết chu kỳ.
