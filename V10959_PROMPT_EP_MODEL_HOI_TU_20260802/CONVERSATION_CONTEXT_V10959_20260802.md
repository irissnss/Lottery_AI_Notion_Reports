# CONVERSATION_CONTEXT_V10959_20260802

## Owner (nguyên văn)

> Sao anh thấy các model eval có kết quả gần gần giống nhau, còn các model trong total ra kết quả gần gần giống nhau? Có khi nào do prompt không đúng không em? Giống như miền Trung hiện tại Opus 4.6 ra 69-86 còn GPT 5 mini ra 71-65, và nhóm eval thì giống giống nhau, còn nhóm total official thì giống giống nhau.

Kèm chỉ thị phiên: chỉ đọc và đo; không sửa code; không deploy (QD-014 đóng băng tới 08/08); đo trùng lặp; đọc prompt; tra A/B prompt; kết luận thẳng; đề xuất không tự làm; ghi V10959; đẩy hai repo; không đụng Notion.

## Agent làm gì

1. Chạy `_v10920_session_start.py` — 0 checkpoint quá hạn.
2. Thuê agent con đọc kiến trúc prompt + lịch sử A/B.
3. Viết và chạy trên VPS: `_v10959_do_trung_lap.py`, `_v10959b_kiem_cheo.py`, `_v10959c_ab_status.py`, `_v10959d_ab_counts.py`.
4. Đối chiếu với phát hiện V10955 (tín hiệu rơi ở gộp phiếu; RF không dùng prompt còn tín hiệu).
5. Ghi báo cáo công khai + CHANGELOG/SSOT/FOLLOW_UP qua `prepend()`; tăng governance_seq; đẩy hai repo.

## Vấp

- Schema MDE không có `lo2_numbers` → sửa sang `main_numbers`.
- Phân nhóm theo registry hiện tại làm lệch lịch sử gpt-5-mini → đo lại cửa sổ 01/05–31/07 với nhóm lịch sử.
- `build_context_pack` in ra stdout phá JSON → ghi file / redirect.
- Hai agent khác (V10960/V10961) cũng ghi docs cùng lúc → đọc lại trước khi prepend.

## Kết luận gửi owner

Owner đúng lõi (prompt ép hội tụ ~26% vs 1% ngẫu nhiên; ML gần như độc lập với prompt). Owner chưa đúng về hai cụm total/eval sạch (CROSS vẫn 22%). A/B cùng model chưa chạy đủ roster.
