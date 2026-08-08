# CONVERSATION CONTEXT — V11043 · 2026-08-09 00:38 → 02:00

## Owner nói gì (NGUYÊN VĂN)

> **PROMPT TỔNG LỰC LẦN 5 — PHIÊN 09/08: THI HÀNH KÝ GỘP 00:33 + DỌN SỔ FOLLOW_UP + HÀNG ĐỢI CỔNG**
>
> (1) BẢNG 57 MỤC (V11041): KÝ A=43 ĐÓNG + C=5 giữ luật đứng (liên tục, không đặt hạn) · nhóm
> B=9: agent tự mở từng trang/endpoint VERIFY còn sống rồi TRÌNH LẠI (cấm tự đặt hạn — RM-06).
> Quyết định này MỞ KHOÁ GĐ-3 dọn sổ FOLLOW_UP;
> (2) FU-381 (B1): phương án A — GIỮ cơ chế cổng CHẶN số, sửa câu mô tả sai trong tài liệu;
> (3) FU-382: CHỈ BỎ viewer.html;
> (4) FU-383: GIỮ trạng thái hiện tại theo V10750;
> (5) FU-379: theo khuyến nghị agent;
> (6) FU-380: CHỜ 21/08.

Trước đó owner chỉ hỏi: *"có báo cáo đầy đủ không em?"*

## Việc đầu tiên là nhìn đồng hồ

Owner viết *«bộ tự kiểm 18:05 hôm nay»* và *«cron lane 19:35 hôm nay»*. Đồng hồ: **00:38**.
Hai mốc đó còn **17,4 giờ** và **19 giờ** nữa — **không quan sát được**.

Nói thẳng chuyện đó, rồi làm thứ **kiểm được ngay**: chứng minh dây nối. Bản trên VPS **có**
C23/C24; **21** lần `add("C…")` + **3** phép trong vòng lặp = **24**; và log 08/08 ghi **22**
đúng bằng **24 − 2** vì lượt đó chạy lúc 18:05, **trước** khi C23/C24 deploy lúc 20:09.
Con số 22 hôm qua vì thế **được giải thích trọn vẹn**, không còn là dấu hỏi.

## Bốn chỗ agent nói thẳng với owner

**1. `STANDING_RULE` suýt làm 5 mục biến mất.** Owner ra lệnh *«đánh dấu STANDING_RULE»* — nhưng
nhãn đó **không nằm trong** `TREO_STATUSES` lẫn `DONG_STATUSES`, nên `trang_thai_mo_coi()` sẽ bêu
cả 5 là **mồ côi**, rơi khỏi mọi bộ đếm. Đúng lỗi V10980 từng làm 14 mục biến mất. Phải **dạy bộ
đọc trước** bằng một loại thứ ba, rồi mới đặt nhãn.

**2. Gỡ `viewer.html` không phải gỡ một tệp.** Năm chỗ còn trỏ vào nó, **một trong đó đang serve
thật**: `_v87_master_board.py:378` — bảng tra cứu hiển thị trên `/monitoring`, sẽ tiếp tục quảng
cáo một tệp đã xoá. Gỡ mỗi tệp là để lại đúng thứ §60.2 cấm.

**3. Không sửa lời owner.** Câu *«hệ luôn xuất số»* trong `FU-381` là **trích nguyên văn owner**.
Agent sửa **mọi chỗ khác** nhưng giữ nguyên câu trích, chỉ sửa số dòng kèm theo và thêm dòng kết
luận. Sửa lời owner cho khớp code là **ghi đè lịch sử**.

**4. Không dọn sổ trong phiên này.** Owner mở khoá GĐ-3, nhưng đào ra thì việc thật lớn hơn hẳn
đề bài (xem dưới), và sửa regex là **đổi thứ mọi bộ đếm dựa vào** — trong một phiên đã sửa sổ 5
lần và đã băm tiêu đề một lần. Ghi `FU-384`, hạn 10/08.

## Phát hiện lớn hơn hẳn đề bài

Owner nghĩ GĐ-3 là *«sổ 749 mục, dọn cho gọn»*. Đo thật thì:

**Bộ đọc chỉ khớp `### FU-<số>`. Tệp có 768 tiêu đề `###`. Nghĩa là 384 khối — 640 KB, 47,7%
dung lượng, 5.669 dòng — CHƯA BAO GIỜ được đếm.**

- 357 khối là `### FU-V<version>-…` (định dạng di sản)
- **`FU-330` mất tích thật**: dòng 941 ghi `### A1 / FU-330 · ĐÃ LÀM …` — tiền tố `A1 / ` làm
  trượt regex. **Lần thứ tư** của họ lỗi V10980 / FU-353 / FU-370.
- **`FU-185` nuốt 573 KB** thân bài (dòng 5912→11104) vì thân khối chạy tới `### FU-<số>` kế tiếp
- 86 mã bị trùng, hai mã lặp **5 lần**

⇒ **Mọi con số về sổ theo dõi từ trước tới nay đều tính trên một nửa tệp.**

## Vấp ở đâu — ghi hết

**1. Agent tự dính RM-09 lần nữa.** `grep -c` trên crontab trả **3** và agent suýt kết luận *«ba
cron đang gọi các script trỏ tới viewer.html»*. Đọc lại từng dòng: **cả ba đều bắt đầu bằng `#`**
(đã tắt) và trỏ tới một **tệp khác hẳn**. Nếu tin con số đó thì đã không dám gỡ.

**2. Lặp đúng lỗi «quên ô `status`» sau hai giờ.** `FU-385` viết thiếu ô đó ⇒ bộ đọc trả rỗng.
Lần đầu là `FU-381/382/383` lúc 00:50, lần hai là `FU-385` lúc 01:45. Một lỗi lặp hai lần thì
theo §61 **phải thành cổng máy**, không được chỉ hứa.

**3. `assert` chặn đúng lúc.** Lượt gỡ `viewer.html` đầu tiên dùng `\n` trên tệp CRLF ⇒ assert
fail ⇒ **script dừng trước khi xoá tệp**. Nếu viết `if count==1: replace` mà không assert thì đã
lặng lẽ bỏ qua bốn chỗ tham chiếu **và vẫn xoá tệp**.

**4. Thêm mục mới làm vỡ trần giãn.** Ghi `FU-384`/`FU-385` vào 10/08 làm ngày đó lên **8**.
Chạy lại phép giãn ⇒ về 6. **Thêm mục cũng là đổi tải.**

**5. Một agent điều tra tưởng có phiên song song** — thực ra là **chính phiên này** đang ghi sổ
trong lúc nó đọc. Nó xử lý đúng (chụp bản, chốt số trên bản chụp, đối chiếu lại với live), nhưng
câu chữ dễ làm người đọc tưởng vi phạm luật PARALLELISM. **Không phải.**

## Ba câu chờ owner

1. **Nghiệm thu 9 mục nhóm B** — cả ba trang trả **401**, tức **còn sống và đòi admin**, không
   phải chết. Agent không có tài khoản admin nên không mở được thay owner.
2. **`v81_provider_pilot_recent = 0`** trên `/v82-monitor` — một bảng rỗng giữa 18 khoá có dữ
   liệu. Cố ý hay hỏng?
3. **Dây chuyền mồ côi** — owner chỉ ký bỏ `viewer.html`, nên `viewer.js` (`/viewer.js` vẫn trả
   **200**), `/api/viewer/predictions`, `/api/viewer/today` nay **100% vô chủ**. Gỡ luôn hay giữ?
