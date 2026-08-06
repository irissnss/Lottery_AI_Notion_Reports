## §60 (A58) — SOI TRƯỚC SAU: CẤM VÁ LẺ, CẤM BỎ NỬA CHỪNG
*(owner ký 06/08/2026, V11007 — khoá cứng)*

> Owner nguyên văn: *"anh biết em có tư duy suy nghĩ, phải đảm bảo logic tương quan, tương thích,
> phù hợp nha em, nghĩa là đụng tới chỗ nào các vấn đề nào liên quan là cần phải soi xét mới xử
> lý chứ đừng để xử lý chỗ này làm lỗi chỗ khác điều này cần ghi vào quy tắc làm việc claude.md
> đó nha cấm cẩu thả thiếu suy xét trước sau nha em"*

### §60.1 — Vi phạm thật đã xảy ra (đọc trước khi làm)

**V11001 ngày 05/08 gỡ gan/nóng/lạnh khỏi prompt.** Gỡ xong **8 khối dữ liệu**, báo cáo "xong",
đẩy lên máy chủ. Ngày 06/08 quét lại thì **còn 10 chỗ** vẫn dạy model dùng gan/nóng/lạnh:

| chỗ sót | vì sao nguy hiểm |
|---|---|
| `2. KẾT HỢP … (Top 10 Score, **Gan, Hot/Cold**, Trends)` | ra lệnh dùng nguồn đã bị gỡ |
| `6. Sử dụng dữ liệu Deep Focus (…, **Gan đài**)` | **trỏ vào khối dữ liệu KHÔNG CÒN TỒN TẠI** |
| `8. ưu tiên số … (thống kê + ĐÀI + THỨ **+ Gan**)` | đúng chữ mà đề xuất G4 bảo bỏ |
| few-shot `Gan=02(freq=71)` · `02 → 3 nguồn (…+Gan)` | **dạy bằng ví dụ** — mạnh hơn cả mệnh lệnh |
| `🔥 Số HOT (xuất hiện nhiều trong WIN)` | gỡ mệnh lệnh nhưng **giữ nhãn dữ liệu** |

**Bỏ nửa chừng còn tệ hơn không làm.** Gỡ dữ liệu mà để lại câu lệnh trỏ vào nó thì model
được bảo dùng một thứ không tồn tại — nó sẽ **tự bịa ra** hoặc **tự suy lại mệnh lệnh cũ**.
Và phép đo 14 ngày (FU-284) sẽ đang đo một thay đổi **làm nửa vời**, kết luận rút ra vô giá trị.

### §60.2 — Ba câu phải trả lời TRƯỚC khi sửa bất cứ thứ gì

1. **Ai còn trỏ tới thứ này?** Không chỉ `import` — phải soi **cả ai đọc BẢNG** mà nó ghi,
 **cả câu chữ trong prompt** nhắc tên nó, **cả ví dụ few-shot** dùng nó, **cả nhãn hiển thị**.
2. **Gỡ/đổi xong thì chỗ nào thành vô nghĩa?** Câu lệnh trỏ vào dữ liệu đã gỡ · nhãn mô tả thứ
 không còn · cổng kiểm dò chuỗi đã đổi tên · tài liệu mô tả hành vi cũ.
3. **Có phép nào máy chạy được để chứng minh đã sạch không?** Không có thì **chưa được nói xong**.

### §60.3 — Sau khi sửa: bắt buộc QUÉT NGƯỢC

Chạy một phép quét **toàn tệp / toàn kho** tìm mọi dấu vết của thứ vừa đổi, rồi **phân loại
từng chỗ** — không được chỉ đếm số lần xuất hiện:

| loại | xử lý |
|---|---|
| `TRONG_PROMPT` — nằm trong chuỗi bơm cho model | **phải xử**, đây là chỗ nguy hiểm nhất |
| `GHI_VAO_PROMPT` — `prompt +=` · `sections.append` · `kb_text +=` | **phải xử** |
| `CODE` — tên biến, logic nội bộ | xét từng cái; tên biến không vào prompt thì để được |
| `CHU_THICH` — dòng `#` ghi lại lịch sử | **giữ**, đó là bằng chứng đã làm |

Đếm chuỗi thô là **sai** — dòng chú thích ghi *"(V11001 — GỠ) khối GAN ĐÀI"* sẽ làm phép đếm
báo động giả. Ngày 06/08 agent suýt báo nhầm "G2/G5 chưa làm" chỉ vì đếm chuỗi mà không đọc
ngữ cảnh.

### §60.4 — Mọi việc phải ghi TRẠNG THÁI TRƯỚC / SAU / PHIÊN BẢN

Cấm viết ở **thì đề xuất** cho việc **đã làm**. Bảng đề xuất mà không có cột trạng thái thì
người đọc tưởng chưa động gì — owner đã bắt đúng lỗi này trên trang phân tích V4 ngày 06/08.

Mọi mục trong báo cáo / trang / tài liệu phải có đủ bốn thứ:

```
TRƯỚC:      câu/khối cũ, nguyên văn
SAU:        câu/khối mới, nguyên văn (hoặc "đã xoá hẳn")
PHIÊN BẢN:  V-nào làm, ngày nào, phiên bản prompt trước→sau
KIỂM:       lệnh máy chạy được + kết quả phải thấy
```

### §60.5 — Vi phạm

`A58_VIOLATION_HALF_DONE` — gỡ/đổi một thứ mà còn chỗ khác trỏ vào nó ·
`A58_VIOLATION_NO_REVERSE_SCAN` — báo xong mà không có phép quét ngược phân loại ·
`A58_VIOLATION_NO_BEFORE_AFTER` — trình bày việc đã làm mà thiếu trạng thái trước/sau/phiên bản ·
`A58_VIOLATION_RAW_COUNT` — kết luận bằng cách đếm chuỗi thô, không đọc ngữ cảnh.

---
