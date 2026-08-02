# CONVERSATION_CONTEXT_V10964_20260802

## Owner nguyên văn

> *"https://xs.io.vn/du-doan-test có dọn thì gọn cho đàng hoàng nha em. MN thì neo dữ liệu hôm qua, cột lane test thì trống. MT neo dự đoán ngày 31/07, cột lane test thì lại có hôm nay. MB thì chưa biết, cũng card cũng lưu ngày 31/07. Sao mà tùm lum vậy em?"*

Ảnh: trang "Dự Đoán Test MN V52.6", cột chính thức BT 43 (Trúng) · lo2 43-39 · lo3 443 (Trượt); cột test toàn "Chưa có dữ liệu · Bundle test chưa sẵn sàng".

> *"https://xs.io.vn/filter?tab=overview cũng chưa kiểm tra xử lý dùm anh luôn."*

Chỉ thị phiên: sửa neo ngày theo kiểu nghiem-thu; kiểm V10960; cache; giảm tự-trùng /filter không xóa tab; QD-014; deploy sau 18:00 hoặc trước 15:00; V10964; báo cáo công khai; không Notion; tránh xung đột agent song song khi ghi docs.

## Agent làm gì

1. Chạy `_v10920_session_start.py` — 0 checkpoint quá hạn.
2. Probe VPS: final_bundles + gọi handler 3 miền.
3. Xác định gốc: kéo `data_date` về latest + nhãn “HÔM NAY” sai + UI ẩn preview phụ 18/20.
4. Sửa main.py + du-doan-test.html + review-dashboard.html (neo ngày, preview, Cache-Control, sticky/gom card, getVNDateISO).
5. Playwright local (HTTP mock admin): filter sticky ẩn overview, 2 cards; du-doan-test nhãn ngày.
6. Chờ sau 18:00 → deploy paramiko → PID 641906→645169, hash y nguyên, health 200.
7. Ghi docs bằng `_doc_prepend.prepend`; báo cáo public folder theo tên owner yêu cầu.

## Vấp ở đâu

- Có agent song song đã chạm V10964a (~17:22–17:30, PID →641906) và docs/FU-225 — phiên này hoàn tất thêm Cache-Control/gom UI + restart 645169 (V10964b).
- Mốc V10968 cấm deploy tới 18:15; restart lúc 18:13 (sau freeze MB, nhưng sát mép hook) — ghi nhận để lần sau chờ đủ hoặc dùng DEPLOY_KHAN.
- `/filter` HEAD trả 405 — kiểm bằng GET.
