# CONVERSATION CONTEXT — V11006 · 2026-08-06

## Owner nói gì (NGUYÊN VĂN)

> Anh chưa thấy được các trạng thái được hiển thị , cái nào đã xử lý cử lý như thế nào trong V4
> ah em, còn gì cần gì , tất cả phải nên được tổng hợp dùm anh lại nha em chú thích màu sách dùm
> anh rõ ràng nha em. Vì trang là là cốt lõi để đơn model hoạt động chuẩn chỉnh ra số tốt thì
> total output tốt được em. Càng chi tiết càng rõ ràng càng tốt, chứ trong các đoạn prompt vẫn
> còn tham chiếu đến 1 số cơ chế anh không nắm được hết ah em. Đẩy toàn bộ thông tin báo cáo chi
> tiết lên github report. Và tất cả xử lý xong cần deploy đầy đủ đừng để hỏng hệ thống nha em.
> Ah còn 1 việc là hiện các tỉnh thành đã gộp nên 1 số đài tên đài lịch sổ đều bị thay đổi em xem
> kỹ dùm anh nha em. Mỗi nơi đặt mỗi tên gọi khách nhau như khánh hòa có chỗ là KH hay TP HCM ,
> chỗ thì tp hồ chí minh.

## Agent làm gì, theo thứ tự

1. **Đo trước, sửa sau.** Việc gộp tỉnh nghe có vẻ nguy hiểm nên đo bốn mặt: tên đài trong DB ·
   lịch xổ khai trong code vs thực tế · đài nào xổ thứ nào · luật có trỏ trúng không.
   Kết quả: **chưa đụng gì tới dữ liệu**.
2. **Nhưng vẫn đào tiếp** vì owner nêu đúng chuyện tên gọi khác nhau. Thử 116 cách viết →
   nhận đúng 66, không nhận ra 50.
3. Tìm ra `station_identity.py` **đã có sẵn** đúng hai ví dụ owner nêu (`KH`, `TP HCM`).
   Nhưng nó thiếu **chính tên đài**, nên bản bỏ dấu vẫn trượt.
4. Vá vòng một → 66→92. Vẫn trượt `Da Lat`, `Dak Lak`. **Đào tiếp** ra nguyên nhân gốc:
   chữ `Đ` không tách dấu được theo NFKD.
5. Vá gốc → 66→**111/116**, 0 nhận nhầm.
6. Kiểm an toàn: 0/39 bí danh cũ đổi nghĩa, 0 va chạm khoá, 0 tên đang có bị đổi cách gom.
7. Ghi CHANGELOG · SSOT · FOLLOW_UP (FU-292, FU-293), cập nhật bảng mốc tải cho J5.
8. Deploy có **cổng thử trên VPS trước khi restart**. PID 930315→936322, 4 bảng khoá y hệt.
9. Nâng trang phân tích lên **V5**: chú giải 5 màu + bảng trạng thái 20 việc + từ điển 12 cơ chế.

## Vấp ở đâu

### Vấp 1 — suýt dừng ở kết luận "không sao"

Bốn phép đo đầu đều sạch (21/21 lịch khớp, 17/17 ngày, 0 luật hỏng). Rất dễ báo cáo *"việc gộp
tỉnh không ảnh hưởng gì"* rồi dừng. Nhưng owner nêu cụ thể `KH` vs `Khánh Hòa` — nên phải thử
tiếp các **cách viết**, và chỗ đó mới lòi ra 50/116 trượt.

### Vấp 2 — vá vòng một chưa tới gốc

Thêm 41 tên chuẩn + tên tỉnh mới + mã ngắn → 92/116. Còn `Da Lat`, `Dak Lak`, `Da Nang` trượt.
Nếu dừng ở đây thì đã bỏ sót **cả họ chữ Đ** (6 đài). Đào tiếp mới ra: `Đ` (U+0110) là chữ có
gạch ngang, NFKD không tách được — đó cũng là lý do bảng cũ phải liệt kê tay `Da Nang`,
`Dak Lak`, `Dak Nong`.

### Vấp 3 — smoke test gõ nhầm endpoint

Kiểm `/api/admin/rule-drift` mong 401 nhưng ra 404 — endpoint không tồn tại. Lỗi ở câu kiểm của
agent, không phải ở hệ. `/api/health` = 200 đúng.

## Quyết định thiết kế đáng ghi

**TỪ CHỐI đoán thay vì đoán bừa.** `Lâm Đồng` sau gộp có thể là Đà Lạt hay Bình Thuận hay Đắk
Nông. Mã `BD` `ĐN` `QN` cũng mơ hồ. Hệ **cố ý trả về nguyên văn** để cảnh gác bắt được, thay vì
đoán một đài.

Lý do: trả rỗng thì **mất số** và có cảnh báo; đoán sai thì **lấy số từ đài khác** mà không ai
biết. Cái thứ hai tệ hơn hẳn.

**Cổng thử trên VPS trước khi restart.** Script deploy chạy bản mới trên VPS rồi so cách gom tên
đài trước/sau. Chỉ chấp nhận đúng một thay đổi đã biết; khác đi là DỪNG, không restart.

## Điều agent NÓI THẲNG với owner

**Tin tốt là thật:** việc gộp tỉnh chưa đụng gì tới dữ liệu. Các công ty xổ số giữ nguyên tên
thương hiệu, 41 đài vẫn xổ đều tới 04/08.

**Nhưng lỗ hổng là thật và đã sập một lần:** 03–07/07/2026 nguồn đổi sang mã ngắn
`GL`/`NT`/`DLK`/`QNA`, hệ im lặng không ra gì. Không nổ, không log. V10810 vá bằng cách thêm
từng mã — tức là vá triệu chứng.

**Sáu trong 12 cơ chế trong prompt cùng một gốc bệnh:** `MINED RULES` · `RULES-FIRST` ·
`WEEKLY LIVINGNESS` · `EVIDENCE TABLE` · `BT MODEL RANKING` · `Model Performance 14d` — tất cả
chấm điểm bằng cách nhìn ngược vào quá khứ. M4 vừa chứng minh cách chấm đó cho `+9,77σ` khi nhìn
ngược và `−1,34σ` khi đo tiến.
