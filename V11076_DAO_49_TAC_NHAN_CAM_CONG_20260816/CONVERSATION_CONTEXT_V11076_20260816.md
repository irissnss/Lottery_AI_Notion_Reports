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
Trong đó có **hai thay đổi chạm production thật**: bật WAL cho DB sống, và vá lane giữ khoá DB
làm mất 2 kết quả model.

Và đây là **tái phạm đúng ngày đến hạn xử lần trước** — `FU-375`, hạn 16/08, nội dung y hệt.
Lần trước 8 commit, lần này 12.

---

## Nhưng gốc bệnh không phải «agent lười»

Đợt đào 49 tác nhân tìm ra thứ khác hẳn:

```
~/.claude/settings.json       chỉ có effortLevel + model — KHÔNG có khoá hooks
<kho>/.claude/settings.json   KHÔNG TỒN TẠI
.git/hooks/                   trống, chỉ có .sample
.cursor/hooks.json            tên sự kiện của Cursor — Claude Code KHÔNG đọc
```

**Toàn bộ hàng rào 8 cổng chưa bao giờ chạy** trong môi trường đang được dùng. Không có tiếng
động nào là vì **không có ai canh**, chứ không phải vì agent tắt nó đi.

Trớ trêu nhất: `_v11028_cong_dong_bang.py` đã tự ghi câu *«một cổng phải nhớ gọi là một cổng
không tồn tại»* — rồi chính nó nằm trong nhóm không được gọi.

---

## Phép đo cho kết quả NGƯỢC với điều agent tin

`FU-316`: dòng bơm vào prompt cắt bỏ **83%** pool D-1, và **30/30 ngày** không chứa đuôi nào
lớn hơn 21. Cả agent lẫn bản đào đều nghiêng về **«có neo»**.

Đăng ký ngưỡng **trước khi chạy**: CÓ NEO khi chênh ≥ +2,5pp **và** |z| ≥ 2.

Kết quả: model chọn đuôi thấp **20,2%** so với nền **21,0%** ⇒ **−0,79pp, z = −1,01**.
**Không neo.**

> Nếu không đăng ký ngưỡng trước, bản báo cáo này đã ghi *«tìm ra nguyên nhân»* cho một thứ
> không tồn tại. Đó là lý do luật đăng ký trước tồn tại.

Và phải nói giới hạn: đây là **một** ca, đo **một** cơ chế. **Không được** suy rộng thành
*«mọi việc nhồi nhét đều vô hại»* — `FU-404` (nhãn `HR12W` nói quá giá trị thật) vẫn còn nguyên
trong gói 21/08.

---

## Phản biện đã cứu owner khỏi 9 thứ

Bản đào đưa lên **40 phát hiện**, **9 bị bác**. Bốn cái trong đó sẽ làm owner mất công kiểm hộ:

| bị bác | vì sao |
|---|---|
| «ba lệnh §0 chưa bao giờ chạy» | **sai** — log có **9 lượt** chạy thật, briefing mới in đúng bộ 16/08 |
| «FU-224 quá hạn trả lời 5 ngày» | owner đã trả lời **trước hạn 2 ngày** (QD-051/QD-054 ký 09/08) |
| «FU-399 biến mất từ 12/08» | owner **chủ ý gác lại, có ký** — QD-066 |
| «model bịa trích dẫn giải G3/G4 ở 78,3%» | **không model nào trích** — Python tự tính ngược rồi ghi đè |

Nếu bưng cả 40 lên thì owner lại phải đi kiểm hộ agent lần nữa.

---

## Một vấp ngay trong phiên này — và cách bắt được

Bản `CONVERSATION_CONTEXT` này lần đầu được ghi qua một lệnh shell có chứa dấu backtick. Bash
**ăn mất** mọi đoạn trong backtick trước khi Python nhìn thấy, nên tệp ghi ra **rỗng ở các khối
mã** — mà lệnh vẫn báo thành công và cổng báo cáo vẫn cho qua.

Bắt được vì **kiểm dấu vết** sau khi ghi (đếm số dòng còn giữ tên mã ⇒ **0**), không phải vì tin
dòng «✓ đã viết». Cùng họ với bài học đã ghi hôm 13/08: **«lệnh chạy xong» không bằng «việc đã
xảy ra»**.

---

## Trạng thái cuối phiên

Production **không đổi**. Cổng đã cắm và **đã chặn thật** ngay lần thử đầu — nó bắt đúng lỗi
agent đang mắc, và agent không commit được cho tới khi bù xong.

12 dòng `HISTORY` và 12 báo cáo công khai đã bù, mỗi bản mang **banner phân biệt ngày việc xảy ra
với ngày viết báo cáo**.

Dự đoán 16/08: **0/3**, nền 33,7%. MT lại là ca trọng số làm mất số trúng — `FU-400` cập nhật
**−2,45pp** trên 449 miền-ngày, ổn định qua ba lần đo liên tiếp.

TanPhatAI cần làm: xem mục cuối `REPORT_V11076.md` — năm việc, quan trọng nhất là ① gốc bệnh
cổng chưa bao giờ chạy, và ⑤ **31 phát hiện đứng vững chưa xử hết**.
