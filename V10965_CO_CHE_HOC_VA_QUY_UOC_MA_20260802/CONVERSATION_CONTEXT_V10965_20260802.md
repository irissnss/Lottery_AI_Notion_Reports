# CONVERSATION_CONTEXT_V10965_20260802

## Owner — yêu cầu gốc (nguyên văn)

Hai việc gộp một phiên: viết tài liệu đầy đủ về các cơ chế học của hệ, và đề xuất cách đánh số hiệu công việc dễ đọc hơn.

> *"Rồi các cơ chế như học tập tích luỹ, xếp hạng, retrain của các model LLM và ML thì sao, em đã đào sâu hết cỡ chưa? Viết chi tiết cụ thể tất cả mọi thứ hiện đang code để kiểm soát, tổng hợp thật đầy đủ."*

> *"Số hiệu công việc cần quy chuẩn chứ kiểu như PL6 gì đó khó nhận biết quá. Số hiệu phải viết tắt đầu mục công việc và hạn ngày, ví dụ Kiểm Soát 08/08 thì số hiệu viết tắt phải viết là TH0808 chẳng hạn, thế dễ đọc hơn."*

Chỉ thị cứng của phiên:
- CHỈ ĐỌC VÀ VIẾT TÀI LIỆU. KHÔNG sửa code chạy, KHÔNG deploy.
- QD-014 đóng băng đường ra số tới hết 08/08.
- Version V10965.
- Đẩy hai repo; không đụng Notion.
- Tiếng Việt lời thường; trung thực tuyệt đối.

## Agent làm gì

1. Chạy `_v10920_session_start.py` — 0 checkpoint quá hạn.
2. Chia khám phá song song 6 nhóm cơ chế + kiểm kê hệ mã.
3. SSH/paramiko VPS: crontab, training_history, guard logs, mined_rules, optimizer marker/log, journal.
4. Viết `docs/CAC_CO_CHE_HOC_CUA_HE.md` và `docs/DE_XUAT_QUY_UOC_MA_CONG_VIEC.md`.
5. prepend CHANGELOG / SSOT / FOLLOW_UP; tăng governance_seq; chép sang repo công khai + REPORT + CONTEXT.
6. Commit/push hai repo (phạm vi đúng file).

## Vấp ở đâu

- PowerShell + SQL dấu phẩy → chuyển script file.
- Xung đột ghi với agent V10964 → chờ mtime ổn định.
- Schema cột DB lệch tên lần probe đầu.
- Phát hiện FU-225 dùng kép — đưa vào đề xuất quy ước mã.
