# CONVERSATION CONTEXT — V11040 · 2026-08-08 khuya *(owner gọi «phiên 09/08»)*

## Owner nói gì (NGUYÊN VĂN — trích từ PROMPT TỔNG LỰC LẦN 3)

> **GĐ-1** — vá cổng chống cắt cụt (FU-378).

> **KÈM NHANH (15 phút, cùng GĐ-1):** FU-347 — sửa "39 đặc trưng" → 28 ở CHANGELOG.md:1179 +
> FOLLOW_UP_TRACKER.md:533 (đây là ngưỡng hành động của FU-320 — sai thì bản A/B đăng ký sai từ
> đầu). §60 đầy đủ.

> **Báo cáo công khai ĐẨY NGAY cùng commit** (A55 — hôm qua owner phải hỏi mới lộ thiếu; không
> để lặp).

> **NUMBERING:** TRƯỚC khi dùng bất kỳ mã mới nào (V · FU · QD · mã đọc §58), phải quét thủ công
> BỐN nơi… và in bằng chứng quét vào report. Cấm "đoán số tiếp theo".

> **KHÔNG LÀM:** đổi prompt/chọn số/roster (QD-041 tới 21/08) · FU-290 · chấm sớm lane G2-MB ·
> kết luận FU-284 · B1/B2 trước khi sổ FOLLOW_UP sạch · §24 · mở rộng phạm vi ngoài danh sách trên.

## Agent làm gì

**Trước khi chạm gì:** kiểm phiên song song (không có — hai nhật ký cũ **+0 dòng, +0 byte**, chỉ
mtime bị chạm bởi chính agent đọc) · cổng tuổi dữ liệu `cu=4.06 giờ / ngưỡng 6` **ĐẠT** · quét số
hiệu bốn nơi.

**Vá ba lỗ hổng** của cổng chống cắt cụt, không phải một (RM-07): CRLF vs LF · `BIEN_NGHI` thiếu
768 KiB · `_doc_prepend` chỉ so với bản trên đĩa.

**Thử chứng minh chặn được** (RM-15) trên **vật thật** `main.py` 976.303 byte / 21.204 CRLF —
khôi phục byte-khớp trong `finally` sau mỗi phép, có `assert`. Hook `truncation_guard` kế thừa
bản vá: vi phạm ⇒ `deny`, sạch ⇒ `allow`.

**Sửa số đặc trưng** theo AST trên code thật (28, không phải 39; bỏ 6 còn 22, không phải 33) và
dựng cổng riêng cho nó.

## Vấp ở đâu — ba chỗ, ghi hết

**1. Agent tự dính RM-09 ngay trong lượt quét ngược của chính mình.**
Regex lỏng `vs\s*33` bắt nhầm `48.17% vs 33.75%` — ba dòng backtest V10636 chẳng liên quan gì —
rồi báo *«còn 5 chỗ sai»*. Đúng bẫy §60.3 cấm: đếm chuỗi thô, không đọc ngữ cảnh. Buồn cười ở
chỗ đây là quy tắc em **vừa trích ra để tự dặn mình** ở đầu việc.

**2. Rồi dính tiếp lần hai, ngược chiều.**
Ghi xong khối tài liệu V11040 thì cổng đỏ **3 chỗ** — chính khối báo cáo của em **trích lại số
cũ** để kể sự cố. Cám dỗ rất mạnh: nới danh sách từ khoá cho cổng xanh. Làm thế là **làm yếu
cổng** — một dòng khẳng định thật cũng sẽ lọt theo. Chọn ngược lại: đặt **dấu quy ước bắt buộc
`(SỐ CŨ)`**, ai trích số sai phải ghi kèm. Hồi quy thật không bao giờ tự viết «SỐ CŨ».

**3. Ngày trong brief lệch ngày thật.**
Brief gọi «phiên 09/08», đồng hồ là **08/08 23:00**. Em lỡ ghi `2026-08-09` vào ba mặt tài liệu
rồi sửa lại theo đồng hồ. Sổ ghi giờ thật; nhãn phiên của owner để trong ngoặc.

## Và một thứ không định tìm mà bật ra

Chạy loạt cổng chuẩn thì `_v10920_decision_ledger` báo **`QD-022` TRÔI**. Phản xạ đầu tiên là
nghĩ *«mình vừa làm gãy cái gì»*. Đào tới gốc thì **ngược lại**:

Mục thứ tư đáo hạn 10/08 là **`FU-325`**, và nó **luôn** đáo hạn 10/08. Tiêu đề gốc viết
`cần 10/08` — **thiếu chữ «hạn»** — nên bộ đọc trả `due=None`. Nó **vô hình với mọi bộ đếm** kể
từ ngày được viết. Hai bản vá hôm qua (`FU-353` sửa tiêu đề, `FU-370` cho kế thừa hạn) **không
tạo** tải mới — chúng **làm hiện** tải vốn có.

⇒ Bảng tải trong `QD-022` (*«10/08 = 3 mục»*) **sai ngay tại thời điểm owner ký 04/08**. Owner
đã ký một con số tính trên cuốn sổ có hạn vô hình. **RM-17** đúng dạng.

**Agent KHÔNG tự xử.** Ba cách làm-cho-xanh đều bị loại: dời hạn `FU-325` (nó neo vào cửa sổ đo,
và RM-06 cấm agent đặt/dời hạn) · sửa trần 3→4 trong cổng (đổi cam kết owner đã ký) · nới cổng
(**ép số cho đẹp**, đúng thứ chính `QD-022` tự dặn *«nói thẳng thay vì ép số»*). Ghi thành
`FU-379`, hai phương án A/B, khuyến nghị **A**, **chờ owner ký**.

## Điều agent nói thẳng với owner

**1. Lỗi lặp lại sau đúng một ngày.** Docstring của chính cổng chống cắt cụt đã ghi về sự cố
07/08: *«`_doc_prepend` chỉ so với bản TRÊN ĐĨA (đã cụt sẵn)»*. Ghi rồi, đọc rồi, **không vá** —
và 08/08 mất thêm 4.056 dòng của một tệp production. Ghi ra không bằng dựng cổng (RM-01 nói đúng
chuyện này: nhắc suông đã thất bại 17 lần).

**2. Số dòng owner trích trong brief đã hết hạn.** `FOLLOW_UP_TRACKER.md:533` → thật là **1055**.
Hai sổ này ghi kiểu prepend nên **mọi số dòng đều hết hạn ngay lượt ghi sau**. Trích theo nội
dung, đừng trích theo số dòng — em cũng vậy.

**3. Va chạm mã đọc lần thứ năm trong hai ngày.** `SC0908-3` đã có chủ. `FU-369` (cổng cấp số
hiệu) không còn là việc «nên làm» nữa.

**4. Con số 39 mâu thuẫn với bảng nằm cùng dòng với nó** — `5+6+3+1+5+2+5+1 = 28` in ngay bên
phải chữ «39». Không ai đọc ra suốt thời gian đó, kể cả em, cho tới khi owner chỉ vào.

**5. Báo cáo này đẩy cùng commit.** Hôm qua owner phải hỏi *«đẩy báo cáo đầy đủ chi tiết chưa
em?»* mới lộ ra `A55_VIOLATION_REPORT_MISSING`. **Owner không nên phải là cổng kiểm.**
