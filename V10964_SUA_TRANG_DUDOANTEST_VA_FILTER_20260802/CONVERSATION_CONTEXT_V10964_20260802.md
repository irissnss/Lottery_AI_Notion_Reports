# CONVERSATION_CONTEXT V10964 — 2026-08-02

## Owner (nguyên văn)

> *"https://xs.io.vn/du-doan-test có dọn thì gọn cho đàng hoàng nha em. MN thì neo dữ liệu hôm qua, cột lane test thì trống. MT neo dự đoán ngày 31/07 cột lane test thì lại có hôm nay. MB thì chưa biết, cũng card cũng lưu ngày 31/07. Sao mà tùm lum vậy em?"*

Ảnh MN: official BT 43 (Trúng), lo2 43-39 (Phụ), lo3 443 (Trượt), xiên2 43-39 (Trượt), xiên3 "Chưa đủ"; cột test 5 dòng "Chưa có dữ liệu — Bundle test chưa sẵn sàng."

> *"cũng chưa kiểm tra xử lý dùm a luôn"* — `/filter?tab=overview` vẫn đang tải / trống sau V10960.

Hướng dẫn phiên: tự kiểm trước khi sửa; nói thẳng nếu owner nhầm; QD-014 không đổi tính số; version V10964; deploy ngoài khung dự đoán; báo cáo công khai 9 phần.

## Agent làm gì

1. Session start: 0 checkpoint quá hạn.
2. Query VPS `final_bundles` + shadow tables + in-process API handlers.
3. Playwright `/filter` với timezone VN: bắt được `date=2026-08-03`.
4. Sửa `main.py` + `du-doan-test.html` + `review-dashboard.html`.
5. Deploy 17:28 (PID đổi, hash giữ). Hot-patch HTML banner.
6. Docs prepend + báo cáo công khai + push 2 repo.

## Vấp

- PowerShell nuốt SSH/heredoc — chuyển sang file script.
- Không login được admin cookie — probe bằng import handler + mock `require_admin`.
- Agent V10965 song song — chờ mtime docs.
- Gần khung MB — deploy trước 17:38.

## Kết luận trung thực gửi owner

- MN official ảnh anh gửi là **số hôm nay 02/08 (43)**, không phải hôm qua.
- Lane test MN trống vì **18/20 model**, không vì “hết dữ liệu”.
- `/filter` hỏng vì **lệch ngày mai** sau 17:00, không phải API chết.
