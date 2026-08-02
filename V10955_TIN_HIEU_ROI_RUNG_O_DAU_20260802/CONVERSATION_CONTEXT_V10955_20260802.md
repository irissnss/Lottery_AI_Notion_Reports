# CONVERSATION_CONTEXT_V10955_20260802

## Owner (nguyên văn, nhiệm vụ phiên)

Nhiệm vụ điều tra quan trọng nhất của dự án lúc này. **CHỈ ĐỌC VÀ ĐO — TUYỆT ĐỐI KHÔNG SỬA CODE, KHÔNG DEPLOY.** Chủ dự án (owner) vừa ký lệnh **đóng băng đường ra số tới 08/08** để đo cho sạch.

Hai sự thật mâu thuẫn:
1. Model CÓ tín hiệu ở MT (AUC ~0,55 cả bốn họ; MB ~0,5).
2. Số công bố KHÔNG hơn ngẫu nhiên (MT official +0,21pp / 180 ngày; ML đơn nửa sau chỉ +0,58pp; nửa đầu từng +9,57pp z 3,74 rồi tắt).

Hỏi: tín hiệu rơi rớt ở đâu giữa "model xếp hạng được" và "số công bố trúng"?

Bắt buộc kiểm GT-1..GT-5. Nếu không cứu được thì nói thẳng. Sản phẩm: báo cáo 9 phần, CHANGELOG/SSOT/FU bằng prepend, đẩy hai repo, không Notion.

## Agent làm gì

1. Chạy `_v10920_session_start.py` — 4 checkpoint quá hạn; FU-194 quá hạn; FU-212 đúng việc này.
2. Đọc mẫu đo V10942/V10946/V10951/V10952 + `_v10918_override_watch.py` + `ml_predict.py` (argmax trong top-30).
3. Viết và chạy `_v10955_do_tin_hieu.py` trên VPS (GT-1..GT-5).
4. Bổ sung `_v10955_bo_sung.py` khi thấy LSTM holdout tốt nhưng live MDE kém — phát hiện khớp tái suy luận chỉ 13,3%, kẹt số 96.
5. Ghi tài liệu bằng `_doc_prepend.prepend()` + cập nhật FU-212 + AUTOMATION_STATE.
6. Viết REPORT + CONTEXT công khai; đẩy hai repo (phạm vi hẹp).

## Vấp

- AUC file sau 02:00 (RF 0,5299) khác số 0,5517 cửa sổ cũ — đã giải thích qua FU-213, không kết luận tín hiệu chết.
- Holdout top-1 RF ≠ live MDE RF — báo cả hai, không chọn số đẹp.
- LSTM live lệch tái suy luận — không đề xuất tin LSTM live cho tới khi sửa.

## Kết luận gửi owner

Tin hiệu rơi chủ yếu ở **gộp phiếu** rồi **ghi đè**. GT-2 bác bỏ. GT-5: AUC 0,55 đủ hòa vốn trên giấy và với LSTM holdout; RF/XGB không chuyển được. Đề xuất shadow BT=RF/XGB sau 08/08; QD-013 vẫn đóng.
