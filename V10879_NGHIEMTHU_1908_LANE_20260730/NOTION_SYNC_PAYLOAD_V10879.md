# V10879 — Luồng Nghiệm Thu 19/08 chạy live song song

**30/07/2026 · đã deploy, đang chạy thật · chốt 19/08**

Owner: *"thay vì đợi 19/08 sao em không làm 1 luồng mới với tên Nghiệm Thu 19/08... live song song... Ok thì mình áp vào offical cũng nhanh chóng hơn."*

**Vấn đề cách cũ:** 10 hạng mục đo xong nằm chờ 19/08. Tới ngày đó vẫn 0 ngày forward → 19/08 không phải ngày quyết mà là ngày bắt đầu đo lại, trễ thêm 3 tuần.

**Cấu hình đóng băng 30/07:** de-herd family-√ · 1 số mỗi miền · đài đặt MN 2 / MT 1 / MB 1 theo phong độ cửa sổ mở rộng ≤120 ngày · 50 điểm · chấm 1/1 là thước quyết định.

**Đối chứng 15/06–29/07** (135 miền-ngày, 182,2tr, chuẩn 1/1):

| Phạm vi | NGHIỆM THU | official | /choi |
|---|---|---|---|
| TỔNG | **+4,9%** | −34,6% | −8,0% |
| MN | +2,8% | −18,9% | −31,4% |
| MT | **+33,1%** | −44,5% | +23,1% |
| MB | −11,3% | −51,6% | −27,4% |

**Ngày đầu chạy thật 30/07:** MN `86` (Cần Thơ, Đồng Nai) · MT `20` (Đà Nẵng) · MB `43` (Bắc Ninh).

**Đã sửa trong lúc dựng:** bản đầu dùng cửa sổ 21 ngày, không khớp với cách đo ra +36,1% ở V10876 (cửa sổ mở rộng). 21 ngày chỉ cho ~3 mẫu mỗi đài MN. Đã đổi.

**Rủi ro mở:** MB âm −11,3%; giữ trong luồng để forward phán quyết, không cắt theo backfill.

**An toàn:** không ghi `final_bundles`, không đụng `/choi`. Hash 4 bảng official pre/post IDENTICAL. V10841 PASS. Admin endpoint 401.

**Lên official:** cần forward 1/1 dương và vượt official, có chữ ký owner ở 19/08.

Báo cáo đầy đủ: `V10879_NGHIEMTHU_1908_LANE_20260730/REPORT_V10879_NGHIEMTHU_1908.md`
