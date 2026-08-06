# CONVERSATION CONTEXT — V11003–V11005 · 2026-08-06

## Owner nói gì (NGUYÊN VĂN, không diễn giải)

> FU 283 có nên làm không khi vừa rút ngắn prompt lọi bỏ gan, hot, clod rồi em tiền bạc trong
> việc sử dụng token không quan trọng lắm em, nếu mọi thứ rõ ràng thì có thể chỉ sử dụng 1 số
> model đẳng cấp thôi là đủ không cần thiết phải nhiều model vào đó chỉ tốn tiền và tăng thời
> gian dự đoán làm hệ thống quá tải thêm thôi.
> - Miner Rules là cơ chế tổng hợp cơ học , số học để nhồi vào cho model ML thêm lớp tổng hợp
> sàn lọc , Còn riêng LLM thì là một ngữ cảnh bài bảng hơn để agent LLM tự truy vấn bóc tách và
> chọn số mới đúng , nhưng anh không hiểu sao agent IDE kia lại nhét bộ số được Miner Rules tổng
> hợp lại cho prompt dùng anh chưa hiểu.
> M4 nên làm thực sự nên làm
> - Cần 1 cơ chế chống quên lãng , rơi rớt các vấn đề anh phân tích đề xuất cũng như căn dặn nha
> em. Như việc code , fix cho các cơ chế như retrain tháng , học máy tháng hay tổng hợp theo
> tháng mà để cả tháng mới biết code lỗi hoặc sai hướng thì bó tay nha em.
> - BUNDLE_SKEW là gì anh chưa hiểu luôn

## Agent làm gì, theo thứ tự

1. **Đọc code trước khi trả lời** — `BUNDLE_SKEW` gắn ở `main.py:1086-1114`, ngữ nghĩa ở
   `main.py:20866`. Không đoán.
2. **Tìm đúng M4 nào.** Có **hai** M4 khác nhau trong kho: M4 trong `DECISION_LOG.md:417`
   (rules MB vào prompt AI — đã BẬT từ 05/06/2026) và M4 trong bài phân tích PL17 (nối đối
   chứng giả vào bộ đào luật). Owner đang nói M4 thứ hai — xác nhận bằng cách đọc lại mục 05
   của trang phân tích.
3. **Đối chứng `BUNDLE_SKEW`** bằng số bốc bừa → phát hiện nhãn gần như vô nghĩa.
4. **Đo bầy đàn** → 21 model chỉ bầu ra 9,2 số khác nhau.
5. **Đo danh sách ép trong prompt** bằng chính hàm production.
6. **Dựng M4** — hai lần sai trước khi đúng (xem dưới).
7. **Dựng cơ chế chống quên** — bốn lần sai trước khi đúng.
8. **Bảng quyết định cắt model** từ `prediction_trace.jsonl`.
9. Cập nhật CHANGELOG · SSOT · FOLLOW_UP · sổ quyết định (QD-039, QD-040), commit `2977213`.

## Vấp ở đâu — ghi đủ, không giấu

### Vấp 1 — M4 vòng đầu bỏ mất 96% dòng

Luật giả chọn đài nguồn từ **toàn bộ** danh sách đài của miền. Nhưng MN/MT **xoay đài theo thứ**,
nên đài bốc ra thường không xổ hôm đó ⇒ 3.089/3.203 dòng bị bỏ. MB thì chỉ có **1 đài/ngày** nên
không đổi đài được.

**Sửa:** chỉ bốc trong số đài **thực sự có kết quả** ngày đó, và thêm kiểu đối chứng thứ hai
(**dịch nguồn 28 ngày**, giữ nguyên thứ) — kiểu này luôn dùng được kể cả MB.

### Vấp 2 — phép so không công bằng

Vòng hai chạy được, cho z=+19,10. Con số quá đẹp nên đi kiểm — và **hỏng**: so gộp thì luật giả
chỉ sinh **2,0 đuôi** còn luật thật **3,8 đuôi**. Ít đuôi thì khó trúng hơn ⇒ luật thật được lợi
một cách giả tạo.

**Sửa:** so **theo cặp** (cùng luật, cùng ngày) bằng **McNemar**. Khoá theo cặp thì cả hai đều
2,0 đuôi. z thật là **+9,77**, không phải +19,10.

Đây là **lần thứ tư trong tuần** một con số đẹp hoá ra là lỗi phép đo.

### Vấp 3 — cổng diễn tập tự nó hỏng

Viết `ok = rc==0 and "DIEN_TAP_OK" in out or rc==0`. Python rút gọn thành `(A and B) or A` = `A`.
Nên **chỉ kiểm mã thoát**, câu dấu hiệu sống là **câu chết** — diễn tập sẽ gật hết kể cả khi hàm
không hề chạy. Phát hiện vì 5/5 đạt trong 0,1–0,3 giây, quá nhanh cho việc quét 2.908 tổ hợp.

### Vấp 4 — sổ ghi ra che mất bản trong code

`nap_so()` đọc tệp JSON trước, lấy tệp làm chuẩn. Hậu quả: sửa lệnh diễn tập trong code **không
ăn gì**, tệp cũ vẫn thắng.

**Sửa:** code là nguồn thật; tệp chỉ là bản ghi + bộ dò trôi.

### Vấp 5 — đoán sai tên trường

Đoán hạn nằm ở `han`. Thật ra là `due` / `due_date`. Kết quả: báo **119/119** mục thiếu hạn.
Phát hiện vì **briefing đầu phiên nói 56** — hai con số không khớp thì phải có một cái sai.

### Vấp 6 — diễn tập suýt báo nhầm production hỏng

`prize_keys` lưu dạng `GĐB+G6` — ngăn bằng **dấu cộng**, không phải dấu phẩy. Và `_seed_rules`
dùng khoá **nội bộ chữ thường** (`db`, `g1`, `g6`) trong lúc đào, chỉ đổi sang dạng hiển thị khi
lưu. Ném chuỗi đã lưu ngược vào `ext_tails()` thì **luôn** trả rỗng.

Diễn tập in *"DIEN_TAP_HONG — đường chấm luật đã gãy"* trong khi **production chạy bình thường**.
Nếu không đào tới nơi thì đã báo động giả cho owner.

### Vấp 7 — cổng J5 trượt sau khi thêm việc mới

Thêm FU-290 và FU-291 hạn 08/08 làm bảng mốc tải trong `_v10982_lich9.py` lệch với sổ thật. Đã
cập nhật bảng kèm lý do. Đây là **lần thứ ba** cùng một cổng bắt được việc mới chưa khai — cổng
làm đúng việc của nó.

## Điều agent NÓI THẲNG với owner

**Một con số hôm qua phải đọc lại.** REPORT_V11002 ghi *"65% rớt ở BUNDLE_SKEW"* như bằng chứng
bộ tổng hợp chọn sai. **Không phải.** Với ~21 model/ngày, gần như luôn có ít nhất một model trúng
ngẫu nhiên, nên nhãn đó xuất hiện gần như mỗi khi bundle trượt.

**Owner nêu đúng một vấn đề kiến trúc thật.** Việc nhét danh sách số từ Miner Rules vào prompt LLM
kéo model ~4 lần về một cơ chế **đo tiến −0,81**, đồng thời làm mất phần đóng góp độc lập của LLM.
Nhưng lệnh "BẮT BUỘC" bị bỏ qua ~59% — vừa lái mạnh vừa không nhất quán.

**Không làm hai việc đụng số trong phiên này.** V11001 deploy 19:50 hôm qua, chưa sinh số nào để
so. Đổi tiếp bây giờ là hai biến chồng nhau, trái QD-018.

**Cắt model không chọn được bằng độ trúng.** 0/34 hơn nền sau Bonferroni. Chọn "model đẳng cấp"
theo bảng xếp hạng độ trúng là **chọn nhiễu**. Cắt theo **tốc độ** thì có cơ sở: 36 phút nếu nối
tiếp, giữ 5 model nhanh nhất giảm 94%.
