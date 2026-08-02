# CONVERSATION_CONTEXT_V10971_20260802

**Phiên:** bàn giao máy mới + tổng hợp ~20 ngày + live 02/08 may vs edge  
**Transcript:** `eeb49d3c-16d5-440b-9e2e-df1485c7bdf9`  
**Giờ VN:** 02/08/2026 ~21:26+

---

## 1. Owner — nguyên văn / ý nguyên văn kích hoạt V10971

Owner cần GÓI BÀN GIAO sang máy local khác để code/fix liền mạch — không rơi sót thông tin.

1) Tổng hợp đầy đủ hơn nữa mọi vấn đề đã đề cập/đào bới/xử lý/chờ hạn trong trò chuyện này + KHÔNG BỎ SÓT.  
2) Đồng thời: trong ~20 ngày gần đây có nhiều yêu cầu, đào bới, code fix, điều chỉnh — tổng hợp thật kỹ.  
3) Đẩy báo cáo thật đầy đủ lên GitHub công khai.  
4) Trả lời: live 02/08 thành công nhờ đâu / có thay đổi gì làm tốt lên?  
5) Mục đích: chuyển máy local khác — đảm bảo không thiếu soát, không rơi thông tin, tiếp tục code/fix liền mạch.

Version: **V10971** · folder `V10971_BAN_GIAO_MAY_MOI_20_NGAY_20260802/`  
Nền V10970: đọc làm nền, không copy nguyên; phải RỘNG HƠN (~20 ngày) + HANDOFF.

---

## 2. Owner — câu gốc V10970 vẫn gắn phiên (02/08 ~21:14)

> *"Quá nhiều vấn đề anh và em đã đề cập đến và đào bới trong suốt trò chuyện này em có thể tổng hợp lại đầy đủ , chiêt hơn nữa được không em? Đẩy thêm 1 báo cáo thật đầy đủ hơn nữa bao gồm tất cả các vấn đề anh đã đề cập, em đã xử lý , em đã tổng hợp, em đã đào bới, em đã ghi nhận chờ tới hạn , tất cả mọi thứ không bỏ sót bất kỳ nội dung nào trong trò chuyện này ? Đồng thời em đánh live hôm nay thành công nhờ đâu? Có thay đổi gì khiến 'tốt lên' hay chỉ may?"*

---

## 3. Owner — hết live (02/08 ~18:44) — đã giao V10969

> *"Hết live rồi đó em kiểm tra tổng lực toàn diện dùm anh? đẩy toàn bộ các báo cáo chi tiets đầy đủ lên github report dùm anh nha em"*

---

## 4. Agent làm gì trong V10971

1. Chạy `_v10920_session_start.py` — 0 CP quá hạn; FU treo liệt kê.  
2. Đọc V10970 / V10969 / TONG_HOP_TINH_HINH / ledger / FOLLOW_UP / CHANGELOG / public folders.  
3. Index **116** folder public 13/07–02/08 → `evidence/public_report_index_20d.json`.  
4. Viết REPORT (9 phần A55) + HANDOFF_CHECKLIST + INDEX_QD_FU + CONTEXT.  
5. Mirror `docs/BAN_GIAO_MAY_MOI_V10971.md` · prepend CHANGELOG/SSOT/FOLLOW_UP.  
6. Commit + push private + public · chạy report gate V10971.  
7. **Không** sửa production path chọn số · **không** ghi Notion · **không** claim edge từ 3/3.

---

## 5. Kết luận đưa owner (may vs thật)

Giữ V10970: 3/3 = nhiễu ngày; edge ĐÓNG; QD-014 freeze; model mới vote thắng = anecdote 1 ngày.

---

## 6. Vấp trong phiên V10971

- Cửa sổ 20 ngày quá rộng → dùng timeline theo ngày + bảng version trọng yếu + JSON index 116 folder (không nhét full prose từng V).  
- Briefing txt trên đĩa có thể lệch ngày so stdout script — tin lệnh vừa chạy.  
- Không đo lại VPS trong subagent này — kế thừa số đã khóa trong V10969/70 evidence (trung thực ghi nguồn).

---

## 7. Việc máy mới phải nhớ ngay

Freeze tới 08/08 · FU-225 hạn 03/08 · không mở tiền · session_start mỗi phiên · Notion chỉ đọc · service tên `lottery`.
