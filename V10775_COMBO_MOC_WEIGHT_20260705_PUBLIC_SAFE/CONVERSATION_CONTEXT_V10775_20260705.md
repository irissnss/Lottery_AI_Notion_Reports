# CONVERSATION CONTEXT — V10775 — 2026-07-05

Nguyên văn tin nhắn owner trong phiên (giữ đúng chính tả gốc):

## Tin nhắn 1 (05/07 00:10) — đã xử lý ở V10774

> "Tiếp đi em gián đoạn nữa rồi em.
>
> Đồng thời xem thêm dùm anh vấn đề này
> ML vừa rồi xác định mốc cho từng miền rồi, giờ có cần kiểm chứng lại không? có cần xác định, phân tích lại không? với ML model RF của MB vừa fix thì dangđo lường, xác định là ở mốc nào ? đã kiểm chứng , phân tích cho từng mốc chưa hiện đang báo cáo chung chung lắm chưa rõ ràng ah em . Root cũng quá hỗn loạn cũng cần dọn dẹp sạch sẻ tinh gọn bớt đi em"

## Tin nhắn 2 (05/07 00:58) — xử lý ở V10775 này

> "Nếu như ML các mốc chưa chính xác thì muilt model như combo hoặc super chắc phải kiểm tra lại rồi đó em. nhồi vào đó mốc không tương thích thì thôi bó tay em luôn đó. Total Output offical có cần thay đổi gì không sau khi đào sâu, có cần + thêm trọng số cho model nào trong quá trình total output không em? Ghi chép đầu đủ chi tiết , từ yêu cầu đến xử lý lên githubs report và notion nha em không bỏ sót , rơi rớt gì nha em."

## Bối cảnh chuỗi phiên 04–05/07

- V10771: /choi rõ ràng (khóa method tuần + khóa số ngày + forward W/L).
- V10772: audit mốc + backtest MB 96d → shadow giả thuyết random-forest + deploy-guard + nhãn combo.
- V10773: tinh gọn hệ (gỡ 6 panel zombie, giảm auto-refresh 39→17) + SO GĂNG 3 TẦNG từ 10/5.
- V10774: bản đồ mốc thật (MB 2 mốc 04:00/17:30 + D-1), RF-MB đo riêng TỪNG MỐC (12 variant), vá log-mốc bị restart ghi đè, dọn root ~110 file.
- **V10775 (phiên này): combo lệch mốc (đo forward combo@đúng-mốc) + audit trọng số total output 3 miền (MT RF×2 ứng viên mạnh nhất; MN trọng số vô dụng — cấu trúc; MB trùng checkpoint RF) — KHÔNG đổi official, 4 variant forward mới, checkpoint 14/07.**

Chi tiết đầy đủ từ yêu cầu → phương pháp → số liệu → thay đổi → bằng chứng: xem `NOTION_SYNC_PAYLOAD_V10775.md` cùng thư mục.
