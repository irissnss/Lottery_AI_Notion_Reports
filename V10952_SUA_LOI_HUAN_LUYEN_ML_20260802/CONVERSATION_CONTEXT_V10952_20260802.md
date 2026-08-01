# Bối cảnh hội thoại — V10952 (01–02/08/2026)

Ghi nguyên văn lời owner khi có, và ghi rõ agent làm gì / vấp ở đâu. Phiên kỹ thuật bị ngắt
giữa chừng; bước này chỉ hoàn tất báo cáo công khai và đẩy hai repo.

---

## Bối cảnh dẫn tới phiên

Owner đã dừng đặt tiền thật (V10945 / QD-013). V10947 phát hiện họ ML từng có lợi thế thật ở MT
rồi tắt từ tháng 6. Owner yêu cầu tiếp tục đào: bảng `training_history` cho thấy tỉ lệ hỏng tăng
vọt từ tháng 5, và mọi bản ghi gần đây đều không có chỉ số chất lượng.

CHANGELOG ghi: *"Owner 01/08 khuya: đào tận gốc tiếp — bảng `training_history` cho thấy tỉ lệ
hỏng tăng vọt từ tháng 5, và mọi bản ghi gần đây đều không có chỉ số chất lượng."*

---

## Agent kỹ thuật đã làm gì (trước khi bị ngắt)

1. Đào nhật ký — tìm nguyên văn `I/O operation on closed file.` giết cả 12 model trong 1 giây
   đúng 7 chủ nhật (17/05 → 12/07).
2. Kết luận lỗi 1 đã được sửa từ 15/07 (V10800) bằng tiến trình riêng.
3. Phát hiện lỗi 2 vẫn chảy: câu lệnh ghi bảng rút còn 4 cột; mã thoát luôn 0 dù mọi model lỗi.
4. Sửa: `_v10952_training_journal.py` + `_retrain_all.py` + `_v10646_retrain_guard.py` +
   `lstm_model.py` + `scheduler.py`. Không bật lại cổng tự gỡ model.
5. Đo lại AUC — MT còn tín hiệu (~0,55), MB bằng ngẫu nhiên. Tự thú đo sai meta-learning lần đầu
   (đưa đặc trưng thô vào model có StandardScaler).
6. Chạy thật V10952b lúc 00:02 ngày 02/08 — bảng ghi 12/12 dòng có AUC; 8/9 model giảm AUC nhưng
   phép so chưa công bằng (FU-213).
7. Ghi CHANGELOG / SSOT / FOLLOW_UP / AUTOMATION_STATE. Deploy VPS xong.
8. **Bị ngắt** (hết hạn dùng model) trước khi viết báo cáo công khai và đẩy hai repo.

---

## Nhiệm vụ bước hoàn tất (agent này)

Nhận từ agent cha — chỉ bốn phần:

1. Đọc CHANGELOG / SSOT / FU để nắm số chính xác.
2. Viết `REPORT_V10952.md` (+ conversation context) vào repo công khai.
3. Kiểm nhanh: git status, file có mặt, backup tồn tại, `py_compile` 12 file Python.
4. Đẩy đúng phạm vi V10952 hai repo — không sửa code, không deploy lại, không đo lại, không đụng
   Notion.

---

## Kiểm nhanh trước khi đẩy (kết quả)

- File đã sửa có mặt: `_retrain_all.py`, `_v10646_retrain_guard.py`, `lstm_model.py`,
  `scheduler.py`, `_v10952_training_journal.py` + các `_v10952_*.py`.
- Backup `backups/v10952_pre` tồn tại (4 file).
- `py_compile` 12/12 đạt — không thấy file bị cắt cụt hay lỗi cú pháp.
- Kho riêng tư có ~290 file chưa theo dõi (chủ yếu `backups/` cũ) — **không** đẩy hết; chỉ phạm
  vi V10952.

---

## Vấp trong toàn chuỗi V10952

| chỗ vấp | hậu quả nếu bỏ qua |
|---|---|
| Đo meta-learning bằng đặc trưng thô | Suýt kết luận ngược MT = ngẫu nhiên (0,4995) |
| Phép so AUC cũ↔mới hai cửa sổ khác nhau | Bật cổng tự gỡ sẽ gỡ oan / giữ oan |
| Phiên bị ngắt trước báo cáo công khai | Vi phạm A55 — code deploy mà không có báo cáo |
| FU-211 còn chờ đối chiếu sau job 02:00 | Không được tuyên bố "đã xác minh hết" sớm |

---

## Việc không làm trong bước này

- Không sửa thêm code
- Không deploy lại
- Không chạy lại phép đo AUC
- Không cập nhật Notion (cấm theo A55)
- Không commit hàng trăm file `backups/` cũ không liên quan
