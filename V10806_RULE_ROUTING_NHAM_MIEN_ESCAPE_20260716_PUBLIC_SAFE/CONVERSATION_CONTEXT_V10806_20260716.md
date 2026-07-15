# CONVERSATION CONTEXT — V10806 (2026-07-15 23:35 → 16/07 ~00h)

## Tin nhắn owner (nguyên văn, trigger V10806)

> "anh hiểu rồi vậy em có đặt câu hỏi lại tại sao ? với prompt đó mà 19 lại trung Miền Bắc và 51 lại trúng miền MT và MN mà lại output ngược ngạo vậy làm cho trật chồng chéo vậy không? rõ ràng còn số 12W=92% nó cũng có lý được rules phân tích học tập và xếp hạng nhưng có lẻ có nhầm lẫn miền thì sao em? rồi tại sao cũng prompt đó mà model Ai khác lại output ra số ổn hơn vượt qua được hoặc hiểu được con số đó nó không nằm trong đề xuất hôm nay ? em phải giải thích được các vấn đề đó đã rồi hãy đề xuất sửa nhãn, có khi giữ nguyên chỉ thêm điều kiện nào khác để nó trỏ đúng miền thì sao? Xem lại dùm anh 1 lần nữa nhé"

## Bối cảnh phiên trước (V10805, cùng tối)

Owner 21:53 yêu cầu tra ngược 51/19 theo model + điều kiện thời điểm. V10805 kết luận: rule engine emit đuôi giải D-1 miền khác (Đồng Tháp G5+G7→[32,51] nhãn "12W=92%"; Vũng Tàu GĐB+G1→[19,61] nhãn "75%"); replay thật 5/6 model RA LẠI đúng số; nhãn % là hit_ANY bao-lô (không phải per-số); đề xuất sửa nhãn per-tail. Owner chưa thoả mãn → 3 câu hỏi trên → V10806.

## V10806 trả lời

1. "Ngược ngạo" = 2 chiều: chiều MN/MT→MB cùng tối là THẬT (+5.5/+11.8pp, z≥3; vụ 19); chiều D+1 là ẢO (z<1.6; vụ 51 = base-rate 63%).
2. "Nhầm miền": phép tính nhãn KHÔNG nhầm; re-route VT→MN là mirage vòng tròn (VT là đài MN); ô sai chỗ THẬT là nguồn-MB→MT (âm −2pp nhưng 23 rule active đang bơm vào prompt MT — nguồn herd 39/61).
3. "Model vượt qua": không ai vượt — AI 0/18, 17/17 in-block cả 2 ngày; ML thoát vì mù prompt; guard CONV×4 cứu MN khỏi 39 nhưng 51 (×2)/19 (×1) dưới ngưỡng alert ≥3.
4. Deploy panel 🧭 RULE ROUTING (đo forward); đề xuất CP-L6 cập nhật theo đúng hướng owner: GIỮ NHÃN + THÊM ĐIỀU KIỆN trỏ miền (routing gate ô-âm + trap alert theo miền), thay vì chỉ sửa nhãn.
