# CONVERSATION CONTEXT — V11115 · bù ngày 26/08/2026

> ⚠️ **BẢN BÙ.** Việc làm ngày **25/08/2026**; tệp này viết ngày **26/08/2026**.

## 1 · Vì sao có tệp này

`V11115` **không có** thư mục báo cáo công khai — vi phạm `§57.2` tồn tại
**1 ngày** mà không cổng nào thấy, vì cổng A55 chỉ soi **8 bản gần nhất**
(lỗ hổng ②, vá ở `V11122`/`FU-442`).

## 2 · Nguồn dùng để dựng

| nguồn | quy mô | tính chất |
|---|---|---|
| khối `## V11115` trong `CHANGELOG.md` | 2,530 ký tự / 53 dòng | **đương thời** — viết lúc làm việc |
| commit git | 1 commit, ngày 2026-08-25 | **đương thời** |
| lượt owner trong vết phiên `.jsonl` | có | **đương thời** |

## 3 · Nguyên văn lời owner

> *«PROMPT TỔNG LỰC LẦN 35 KIỂM TOÁN VÀ THAY PHƯƠNG PHÁP TOTAL/OUTPUT THỰC THI TRONG NGÀY 25/08/2026 Dùng multi-agent song song nhưng chỉ MỘT Coordinator hợp nhất. Không mở Plan/sổ cạnh tranh. Không mặc định 15 model tốt hơn 8 model. Không mặc định nhiều model tốt hơn ít model. Số lượng model chỉ là tồn kho. Chất lượng TOTAL phải được chứng minh bằng: - khả năng sinh số; - độ phủ; - xếp hạng; - đóng góp biên; - tính độc …»*
> — owner, **25/08/2026 12:52** (giờ VN)

> *«đang đo lường ah em? đợi kết quả hay sao?»*
> — owner, **25/08/2026 13:03** (giờ VN)

> *«còn đang chạy không em ? xong chưa push báo cáo tổng lực chưa em?»*
> — owner, **25/08/2026 14:26** (giờ VN)

> *«Đã push báo cáo hết chưa em? - Kiểm tra lại toàn bộ 1 lần nữa xem còn gì không để push báo cáo 1 lần luôn - Các vấn đề anh tương tác trực tiếp đã push thành 1 bảng ghi nhận yêu cầu của owner chưa ? Có cần cập nhật quy tắc trong claude.md để chuẩn hóa không vì đôi lúc code đi trước tài liệu do tương tác trực tiếp với em liên tục cho liền mạch ah em. Nên em claude code có thể đi trước tài liệu và việc ghi nhận các yêu …»*
> — owner, **25/08/2026 18:29** (giờ VN)

> *«Em hãy tiến hành đọc toàn bộ các phiên làm việc của claude code và cursor kết hợp báo cáo tổng hợp đính kèm và các thông tin audit báo cáo tất cả mọi thể chạy tổng lực tổng hợp lại một phiên tổng lực với đầy đủ tất cả các vấn đề không làm rơi rụng bất kỳ vấn đề nào, các vấn đề đã xử lý , có thể xử lý , tự xử lý rõ ràng , các yêu cầu của anh v.... không bỏ sớt bất kỳ điểm nào nha em. Em tiến hành xem toàn bộ các phiên…»*
> — owner, **25/08/2026 18:56** (giờ VN)


## 4 · Điều KHÔNG khôi phục được — ghi thẳng, không suy

- **giờ chính xác** từng thao tác trong phiên gốc
- **vướng vấp giữa chừng** — không tài liệu nào ghi lúc đó
- **các phương án đã cân nhắc rồi loại**
- **hash 4 bảng khoá trước/sau** và **PID trước/sau** nếu phiên gốc có chạm DB hoặc restart
- **output cổng kiểm** của phiên gốc — cổng in `stdout`, không ghi tệp (khuyết tật `RM-15`, đã vá
  cho `cong_git_commit.py` ở `V11121` bằng sổ điểm danh)

## 5 · Điều bản bù này **không** làm

| không làm | vì sao |
|---|---|
| Chế lại lời owner | `§62` cấm — thà để trống còn hơn bịa |
| Điền số ước cho hash/PID | `RM-11` — số không tái lập được thì không dùng |
| Sửa khối `CHANGELOG` gốc | nó là bản ghi đương thời, **cấm viết lại lịch sử** |
| Gộp với bản khác | mỗi bản một thư mục riêng, đúng `§57.2` |

**TanPhatAI cần làm:** đọc mục 4 trước khi đối chiếu — bản bù **không** thay được báo cáo viết lúc
làm việc, và những chỗ trống là **cố ý trung thực**, không phải thiếu sót.
