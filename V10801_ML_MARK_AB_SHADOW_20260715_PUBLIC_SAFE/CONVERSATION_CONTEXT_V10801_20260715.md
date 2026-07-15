# Conversation context V10801 — 15/07/2026 (verbatim owner)

## Owner 14:23 (trigger V10801)

> "Model ML của MN và MT , MB khác nhau về mốc  dự đoán ah em xem kỹ nha em MN thì đang lấy D-1 của 3 miền , còn miền trung và miền Bắc thì sao? Có cần kiểm tra tới thời điểm này việc setting mốc như thế còn phù hợp không có ổn định không ? MB nữa trước nữa sau gì đó anh không nhớ nổi, kiểm tra backtess lại xem có mốc nào tốt hơn nữa không em? v.v... ví dụ mốc giờ  fix retrain cho MT và hiện tại MT không cần same day thì cũng nên tư duy mà xử lý nha. xem lại vẫn chưa yên tâm luôn em"

## Owner 16:03

> "tiếp đi em gián đoạn rồi em"

## Bối cảnh phiên

Câu hỏi này nối tiếp chuỗi audit V10798 (re-time T-chốt MT 16:54 / MB 17:54), V10799 (ma trận nhất quán 9 luồng), V10800 (audit toàn hệ mốc giờ + fix retrain/optimizer CN chết ngầm). Owner đi sâu thêm một tầng: mốc DỰ ĐOÁN của riêng nhóm model ML per miền — MN lấy D-1, MT/MB thế nào, có mốc tốt hơn không, và yêu cầu chủ động xử lý ("tư duy mà xử lý") thay vì chỉ báo cáo.

## Kết quả phiên (tóm tắt 1 dòng)

Xác nhận MN 04:00 D-1 (ép buộc) / MT 04:00 D-1 (V10766) / MB re-predict 17:30 same-day; backtest A/B 42d cho thấy MB giữ nguyên đúng, MT có ứng viên meta+xgb same-day (+14.3/+11.9pp, p~0.027) mâu thuẫn V10766 → dựng shadow forward-proof (bảng + cron 19:05 + API admin + panel /monitoring) với ngưỡng hành động ghi sẵn, KHÔNG đổi production, hash 4 bảng IDENTICAL.
