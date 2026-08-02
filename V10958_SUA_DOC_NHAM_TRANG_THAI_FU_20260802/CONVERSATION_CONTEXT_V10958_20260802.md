# CONVERSATION_CONTEXT_V10958_20260802

## Owner (nguyên văn — nhiệm vụ phiên)

Sửa một lỗi công cụ đang gây báo động giả lặp lại. Dự án dự đoán xổ số Việt Nam tại `E:\Lottery_AI_Test` (Windows, PowerShell). VPS `14.225.224.89`, user `root`, khoá `C:\Users\Admin\.ssh\id_ed25519`, mã nguồn `/root/Lottery_AI_Test/web/backend`. Repo công khai `E:\Lottery_AI_Notion_Reports`.

### Vấn đề

`docs/FOLLOW_UP_TRACKER.md` được ghi theo kiểu **chèn khối mới lên đầu file** (hàm `prepend()` trong `web/backend/_doc_prepend.py`). Nên một mã FU có thể xuất hiện **nhiều lần** trong file: bản mới nhất nằm gần đầu, các bản cũ vẫn nằm nguyên phía dưới làm lịch sử.

Hậu quả: ai đọc file mà không cẩn thận sẽ vớ trúng bản cũ và báo nhầm trạng thái.

**Đã xảy ra thật hai lần trong một ngày.** Cả hai lần đều báo `FU-194` đang quá hạn chờ live tối 01/08, trong khi thực tế nó đã đóng `CLOSED_PASS` lúc 17:45 ngày 01/08. Bản đóng nằm ở vị trí khoảng ký tự 8.238 trong file, bản cũ `WAIT_LIVE` nằm ở khoảng 17.666.

### Việc cần làm

1. Tìm chỗ đọc sai (`_v10920_session_start.py` quan trọng nhất, hook briefing, report_gate, grep thêm) — chứng minh bằng chạy thật.
2. Sửa: mỗi mã FU chỉ lấy bản gần đầu file nhất; module chung ví dụ `_v10958_fu_reader.py`.
3. Kiểm chứng: FU-194 không còn quá hạn; FU-208/209/215/216 vẫn hiện; đếm trùng và đếm đọc sai.
4. Cân nhắc ghi chú đầu FOLLOW_UP — không xoá lịch sử.
5. Ràng buộc QD-014 đóng băng đường ra số tới 08/08 — việc này được phép vì không chạm.
6. Version V10958; prepend docs; AUTOMATION_STATE; báo cáo công khai; đẩy hai repo; không Notion; commit tiếng Việt không dấu qua file `.cmd`.

## Agent đã làm

1. Chạy `_v10920_session_start.py` — xác nhận báo giả FU-194 WAIT_LIVE quá hạn.
2. Grep mọi chỗ đọc FOLLOW_UP; đọc code session_start / briefing / report_gate / master_board.
3. Đo vị trí FU-194/199; `duplicate_stats`: 2 mã trùng, 1 false-treo.
4. Viết `_v10958_fu_reader.py`; sửa session_start + master_board.
5. Chạy lại session start: 0 quá hạn FU; FU-208/209/215/216 vẫn treo; FU-194 CLOSED_PASS.
6. Ghi CHANGELOG/SSOT/FOLLOW_UP bằng `prepend`; seq 376; báo cáo công khai; commit/push hai repo.

## Vấp trong phiên

- Copy backup sau khi đã sửa → bổ sung `*.pre` từ git HEAD.
- PowerShell không dùng `&&` / nuốt chuỗi Python dài → dùng file script / tách lệnh.
- Số treo 67 vs 42 cũ: đo đúng hơn (status field + dedupe), không phải tăng báo động giả.
