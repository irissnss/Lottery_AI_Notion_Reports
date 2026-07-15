# Conversation Context — V10797 (2026-07-15 sáng)

## Owner message (08:54, verbatim)

> 17h là khóa xổ MT rồi em dời sang 17h05 sao kịp bó tay bậy ah
> MB khóa xổ 18h - nên 17h56 cũng tương đối tàm tạm
> CP l6 là gì anh ko nhớ nổi sao mà duyệt em. Cái nào từ DB từ live em đề xuất hướng cải tiến , nâng cao dự đoán nha em

## Bối cảnh

- V10796 (14/07 tối) mổ ngày lạnh 3 miền trượt, đề xuất P1 "dời bundle MT→17:05, MB→17:56". Owner chỉnh: MT khóa xổ 17:00 nên 17:05 là sau giờ khóa — vô dụng (agent nhận lỗi); MB khóa 18:00 nên ~17:56 chấp nhận được ("tàm tạm").
- Owner quên CP-L6 (checkpoint lean roster từ roadmap Lean Harvest 19/06) → agent giải trình lại + đo counterfactual mới.
- Owner yêu cầu các đề xuất cải tiến phải xuất phát từ DB/live.

## Phản hồi của agent (V10797, read-only)

1. Sửa P1: MT không dời (đo lệch pool 14d đến 24/07 trước); MB đề xuất 17:50-17:52 thay vì 17:56.
2. CP-L6: giải trình + counterfactual 90d (cắt opus/gpt-5.4 khỏi vote vô hại ±1 ngày nhưng tiết kiệm nhỏ, opus carry 46% cao nhất) → 3 lựa chọn a/b/c cho owner.
3. GLM 5.1-vs-5.2 checkpoint (hạn 14/07): hoà accuracy, 5.2 ổn định hơn → retire 5.1 tại 19/07.
4. Gói cải tiến xếp hạng: selector-trio MB (23/07 → K16), MB pool-full, K11a/K15 chốt 16-17/07, MT 24/07, MN giữ, housekeeping 19/07.
