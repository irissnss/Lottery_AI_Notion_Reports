# CONVERSATION_CONTEXT V10957 — 02/08/2026

## Owner nguyên văn (phiên này)

> Hai việc gộp trong một phiên (gộp lại vì cùng ghi vào một bộ file tài liệu, tách ra sẽ xung đột khi ghi).

Về QD-015 / shadow RF:

> *"Có. Duyệt trước để 08/08 tự chạy, kèm chốt tự cắt nếu tỉ lệ khớp dưới 95% trong 7 ngày đầu."*

Về LSTM:

> Owner chốt: *"Đào ngay để hiểu nguyên nhân (chỉ đọc), nhưng chỉ sửa sau 08/08."*

Ràng buộc đóng băng QD-014: không đổi 15 model official, không đổi combo-super, không bật/tắt lớp ghi đè. Được điều tra chỉ-đọc và sửa lỗi kỹ thuật rõ — nhưng owner phiên này chốt **chỉ sửa sau 08/08**.

## Agent đã làm

1. Chạy `_v10920_session_start.py` — FU-194 quá hạn; không có checkpoint roadmap ACTIVE quá hạn mới.
2. Ghi QD-015 + FU-216 (+ FU-217 cho LSTM) + CHANGELOG/SSOT/AUTOMATION_STATE qua `prepend()`.
3. Đào LSTM trên VPS bằng paramiko (4 script `_v10957_lstm_*.py`): chuỗi kẹt, live vs re, vote bỏ LSTM, xác minh key xác suất + model cũ.
4. Viết REPORT_V10957 + evidence; push hai repo (phạm vi hẹp).
5. Không sửa code model, không deploy.

## Vấp

- Script đào sâu lần 1: `TypeError` vì iterate nhầm list ngày — sửa và chạy lại.
- File `.pt` lúc kẹt 96 đã bị đè — không tái tạo chuỗi bằng backup; bằng chứng dựa vào DB + analysis_text.
- `OD-20260731-A` (mốc FINAL) vẫn TRÔI trên kiểm local — có từ trước, ngoài phạm vi phiên này.
- Proxy phiếu đơn giản ≠ toàn bộ logic điểm combo_super — đã ghi rõ trong báo cáo.

## Kết luận đưa owner

LSTM live đang tệ (−5,58pp), kẹt 96 có thật, lệch re chủ yếu do đè model; lỗi key xác suất rõ nhưng chưa sửa; bỏ LSTM khỏi phiếu proxy không đổi số thắng cuộc; ưu tiên sau 08/08 là shadow RF (QD-015) chứ không kỳ vọng LSTM cứu công bố ngắn hạn.
