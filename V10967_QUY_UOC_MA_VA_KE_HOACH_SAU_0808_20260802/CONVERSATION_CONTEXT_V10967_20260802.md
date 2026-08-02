# CONVERSATION_CONTEXT V10967 — 2026-08-02

## Owner (nguyên văn / yêu cầu phiên)

1. Áp quy ước mã — chọn phương án B: giữ mã máy, bắt buộc kèm nhãn đọc + hạn.
   > *"Số hiệu phải viết tắt đầu mục công việc và hạn ngày, ví dụ Kiểm Soát 08/08 thì số hiệu viết tắt phải viết là TH0808 chẳng hạn, thế dễ đọc hơn."*

2. Ghi kế hoạch sau 08/08:
   > *"Tắt bộ tối ưu trọng số (đang làm tệ đi) · đo xem 105 luật có giúp gì không · gỡ lệnh bắt buộc chọn từ danh sách. Làm từng cái một để biết cái nào ăn thua."*

3. Ghi sót V10938: nửa trọng số số còn dùng win rate (`_get_dynamic_win_rates`) — chưa sửa, đóng băng.

4. Tách FU-225 dùng hai nghĩa; quét mã trùng nghĩa khác.

5. Ràng buộc: QD-014 đóng băng đường ra số tới hết 08/08; không deploy sát chuỗi dự đoán; Notion chỉ đọc; báo cáo công khai V10967; commit tiếng Việt không dấu.

## Agent đã làm

- Đọc `docs/DE_XUAT_QUY_UOC_MA_CONG_VIEC.md`; chạy session start.
- Sửa `_v10958_fu_reader.py` + `_v10920_session_start.py`.
- Script gắn nhãn + tách FU-225→FU-231, FU-222 frontend→FU-222b.
- QD-018 (3 bước) + QD-019 (quy ước B); FU-232..235.
- §58 vào năm mặt quy tắc; CHANGELOG/SSOT/AUTOMATION_STATE; báo cáo công khai.
- Không deploy VPS; không sửa combo_super / đường ra số.

## Vấp

- FU-225 kép khiến QD-016 bị che khỏi treo — đã tách FU-231.
- Format bullet `Trạng thái` không khớp parser cũ — đã bổ sung regex VN.
- Không còn agent song song nên gắn nhãn hàng loạt an toàn hơn.

## Mẫu briefing sau sửa

```
[3] MỤC THEO DÕI CÒN TREO: 81 · trong đó QUÁ HẠN 0
      FU-189 · KS0802-1 · Xác minh lane nghỉ vắng · hạn 02/08                  WAIT_LIVE
      FU-184 · KS0802-2 · MT/MB công bố đúng phiếu · hạn 02/08                 WAIT_LIVE
      FU-225 · UI0803 · Xác minh UI du-doan-test + filter · hạn 03/08          DEPLOYED_PENDING_LIVE_VERIFY
```
