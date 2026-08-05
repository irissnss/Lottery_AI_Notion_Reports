# NGỮ CẢNH HỘI THOẠI — V10989b · 05/08/2026

## Owner nói gì ở vòng này

**Owner không nói thêm câu nào.** V10989b là hệ quả trực tiếp của một câu owner đã ra lệnh ở
vòng đầu cùng ngày (V10989):

> *"Tự gọi API đọc nội dung THẬT cho cả 3 miền sau khi sửa, dán số vào báo cáo. Đừng kết luận
> 'đã đạt' chỉ vì file giống nhau hay header đúng — đó đúng là cái sai hôm qua."*

Bối cảnh vòng đầu: owner chụp màn hình `/du-doan-test` tab MN lúc ~10:07 và nói cụt lủn:

> *"em tự nhìn đi"*

Owner bực vì hôm trước agent báo `FU-225` *"phần thuộc hệ đã đạt, chỉ chờ owner nhìn tận mắt"* —
owner nhìn, và **nó không đạt**.

Nguyên tắc §54 owner đã ký, áp thẳng vào việc này:

> *"output thô phải luôn nhìn thấy được; cổng chỉ khoá tiền; không hứa hẹn con số chưa đủ cỡ
> mẫu — phải ghi rõ cỡ mẫu + z hoặc bỏ nhãn"*

## Agent làm gì

1. Chạy hậu kiểm VPS chỉ-đọc: PID, health, admin, kích thước `monitoring.html`, bộ tự kiểm 22
   phép + `C22`.
2. Làm đúng lệnh *"tự gọi API đọc nội dung thật"* → thấy dòng MB: `khuyến cáo = LANE · nền 11%
   n=8`.
3. Soi nguyên khối `play_recommendation` cả ba miền, chấm đuôi nhị thức → MB **2/8, p=0,217**.
4. Đọc `_v10725_champion_selector.py` → phát hiện chân khối mô tả **sai cổng** (`n≥40` trong khi
   đường đang đi chỉ cần `n≥8`).
5. Kiểm lane được khuyến cáo có sống không → `MB_FULL_POOL_D_W06_V1` chạy cuối 04/08, **còn
   sống nhưng không có số hôm nay**, mà trang không có cách nào nói ra.
6. Sửa **tầng hiển thị** (không đụng gốc), backup trước, deploy 11:49:37, so PID, hash 4 bảng.
7. Nghiệm thu bằng cách **bốc đúng hàm dựng khối khỏi tệp đang phục vụ** rồi đọc chữ — 3/3 miền.
8. Ghi sổ `FU-272`, cập nhật bảng mốc tải, chạy đủ cổng kiểm tách riêng từng lệnh, đẩy hai kho.

## Agent vấp ở đâu — nói thẳng, không bào chữa

1. **Vòng đầu chữa chưa hết.** Chỉ soi nhánh *"đang THEO DÕI"* vì đó là chỗ owner chỉ mặt, mà
   không soi **nhánh khuyến cáo chính** — dù cùng một khối, cùng một hàm, cùng một bệnh. Nếu
   owner không ra lệnh "tự gọi API đọc chữ thật", lỗi này đã trôi và **owner lại là người phát
   hiện lần thứ hai**.
2. **Bộ hậu kiểm tự viết báo TRƯỢT vì chính nó gõ nhầm đường dẫn endpoint admin** (404 thay vì
   401). Mất một lượt chạy mới nhận ra lỗi nằm ở bộ đo chứ không ở hệ.
3. **Bộ deploy đếm chữ `"hứa hẹn"` ra 2 và gắn cờ** — hoá ra là 2 dòng **chú thích JS** vừa
   viết. Phép đếm chuỗi thô không phân biệt mã với chú thích.
4. **Suýt quên báo cáo riêng cho `V10989b`.** Cổng quét toàn bộ bắt ngay: `CHANGELOG` có mục
   `## V10989b` thì phải có thư mục `V10989B_*` với đủ 9 phần — đúng cái đã làm cổng TRƯỢT 13,5
   giờ hôm 04/08. Không né bằng cách đổi tên phiên bản.

## Cái được từ vòng này

Từ nay việc nghiệm thu trang **không còn dựa vào "API trả đúng trường"**.
`_v10989b_render_check.js` bốc đúng hàm dựng khối ra khỏi **tệp đang phục vụ**, đổ dữ liệu thật
vào, rồi đọc chữ sau khi bỏ thẻ HTML — **đúng thứ người đọc nhìn thấy**. Hai lần trong một ngày
phép đếm chuỗi thô tỏ ra không đủ; bộ dựng chữ thật này là câu trả lời.
