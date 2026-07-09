# CONVERSATION CONTEXT V10788 — 09/07/2026

## Nguyên văn owner (09/07 09:26)

> "Cái vấn đề mà số miền trước ra miền sau và số trật hày hôm qua hay ra lại ngày hôm sau là anh đang nói với ML có lẻ đang tổng hợp sớm hoặc muộn với các mốc không hợp thời điểm nên thấy có vẻ như thế ML MT dạo này tổng hợp tệ hăn kiểm tra toàn bộ các mốc xem mốc nào ổn định và có hoạt động đúng như thiết kế không?
> Từ các vấn đề anh đề cập em đào bới soi xét đúc kết và đề xuất giúp a hướng xử lý an toàn chính xác hơn đi em. dữ liệu có nhiều và trung thực mà không tìm ra thì quá dỡ"

## Bối cảnh chuỗi phiên trước (V10787 A-F, 08/07)

- Owner: "office 1 đường, lane test 1 nẻo, /choi 1 kiểu" → đo bù trừ: gộp cặp thua mặt tốt nhất cả 3 miền.
- Owner: "3 luồng cũng đoán mò à?" → official-BT ≈ random (MB dưới random z=−1.53); lane AE edge thật z=+1.78.
- Owner: "ML MT thảm hại khi thay đổi" + "output đang bám theo ML" → xác nhận: 13/14 ngày official MT = số khối ML chụm; meta-learning 0/7 vẫn giữ ghế.
- Owner: "MB tín hiệu đầy trời mà total như củ chuối" → 15 model + 14/22 lane cầm 77✓ mà official 44✗; doctrine 4-ML mù trước cụm AI.
- Owner: "không có 59 ở đơn model MB, MT 63/37 không thấy mà official lại đề xuất" → giải thích AE echo có chủ đích (số thua hôm trước / miền trước).

## Phiên này (V10788) — trả lời câu hỏi mốc

1. Audit 7 probe toàn bộ mốc: giờ chạy thật vs thiết kế (7 ngày), dedupe, cuốn chiếu 2 mốc, race T-10, retrain, echo base-rate 60d, chasing 30d, persistence.
2. Kết luận: mốc giờ sạch 100%; mốc hỏng = cấu trúc phiếu (khối ML 04:00 chụm chiếm official) + trọng số 30d nguội + MB động lực học ngược.
3. Deploy panel ⏱ MỐC & NHỊP `/monitoring` (hash 4 bảng IDENTICAL).
4. Đề xuất K13 RECENCY_WEIGHT_V1 shadow (mới) + nhắc K9/K10/K11a chờ ký.
