# CONVERSATION CONTEXT — V11076 · 16/08/2026

## Owner nói gì (NGUYÊN VĂN)

> *«anh phải nói rằng em làm việc vẫn chểnh mảng lắm rơi rớt tùm lum, anh phải nhắc đi nhắc lại,
> nhấn mạnh nhiều lần mệt mỏi quá em. Hãy đưa ra khối lượng agent lớn đi làm việc khắp nơi trong
> dự án để đào cho ra cho chỗ thiếu sót»*

> *«làm hết đi giao nhiệm vụ thì làm đi, làm sao phải tổng lực không rơi rớt, phải tìm cho ra chỗ
> cải tiến nâng cao dự đoán, cấm đoán bừa, suy diễn»*

---

## Owner đúng, và con số chứng minh owner đúng

Không phải cảm giác. **12 nhãn version trôi 4 ngày** mà không một mặt ghi nhận nào động đậy.
Trong đó có **hai thay đổi chạm production thật**: bật WAL cho DB sống, và vá lane giữ khoá DB.

Và đây là **tái phạm đúng ngày đến hạn xử lần trước** — , hạn 16/08, nội dung y hệt.
Lần trước 8 commit, lần này 12.

---

## Nhưng gốc bệnh không phải «agent lười»

Đợt đào 49 tác nhân tìm ra thứ khác hẳn:



**Toàn bộ hàng rào 8 cổng chưa bao giờ chạy** trong môi trường đang được dùng. Không có tiếng
động nào là vì **không có ai canh**, chứ không phải vì agent tắt nó đi.

Trớ trêu nhất:  đã tự ghi câu *«một cổng phải nhớ gọi là một cổng
không tồn tại»* — rồi chính nó nằm trong nhóm không được gọi.

---

## Phép đo cho kết quả NGƯỢC với điều agent tin

: dòng bơm vào prompt cắt bỏ **83%** pool, **30/30 ngày** không chứa đuôi nào > 21.
Cả agent lẫn bản đào đều nghiêng về **«có neo»**.

Đăng ký ngưỡng **trước khi chạy**: .

Kết quả: model chọn đuôi thấp **20,2%** vs nền **21,0%** ⇒ **−0,79pp, z = −1,01**. **Không neo.**

> Nếu không đăng ký ngưỡng trước, bản báo cáo này đã ghi *«tìm ra nguyên nhân»* cho một thứ
> không tồn tại. Đó là lý do luật đăng ký trước tồn tại.

Và phải nói giới hạn: đây là **một** ca. **Không được** suy rộng thành *«mọi nhồi nhét đều vô
hại»* —  (nhãn  nói quá) vẫn còn nguyên trong gói 21/08.

---

## Phản biện đã cứu owner khỏi 9 thứ

Bản đào đưa lên **40 phát hiện**, **9 bị bác**. Trong đó có bốn cái sẽ làm owner mất công kiểm hộ:
«ba lệnh §0 chưa bao giờ chạy» (sai — log có 9 lượt chạy thật), «FU-224 quá hạn 5 ngày» (owner đã
trả lời **trước hạn 2 ngày**), «FU-399 biến mất» (owner **chủ ý gác lại, có ký**), «model bịa
trích dẫn G3/G4 78,3%» (không model nào trích — Python tự tính ngược rồi ghi đè).

---

## Trạng thái cuối phiên

Production **không đổi**. Cổng đã cắm và **đã chặn thật** ngay lần thử đầu. 12 dòng  và
12 báo cáo công khai đã bù, mỗi bản mang **banner phân biệt ngày việc vs ngày viết**.

Dự đoán 16/08: **0/3**, nền 33,7%. MT lại là ca trọng số làm mất số trúng —  cập nhật
**−2,45pp** trên 449 miền-ngày, ổn định qua ba lần đo liên tiếp.

TanPhatAI cần làm: xem mục cuối  — năm việc, quan trọng nhất là ① gốc bệnh cổng
chưa bao giờ chạy, và ⑤ **31 phát hiện đứng vững chưa xử hết**.
