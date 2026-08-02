# CONVERSATION_CONTEXT V10964b — 02/08/2026

## Owner (nguyên văn, chuỗi phiên V10964 → V10964b)

> https://xs.io.vn/du-doan-test có dọn thì gọn cho đàng hoàng nha em. MN thì neo dữ liệu hôm qua, cột lane test thì trống. MT neo dự đoán ngày 31/07, cột lane test thì lại có hôm nay. MB thì chưa biết, cũng card cũng lưu ngày 31/07. Sao mà tùm lum vậy em?

> https://xs.io.vn/filter?tab=overview cũng chưa kiểm tra xử lý dùm anh luôn.

## Agent đã làm (V10964b)

- Hoàn tất neo ngày / preview phụ / nhãn fallback trên `/du-doan-test`.
- `/filter`: Cache-Control no-store, gom overview, sửa getVNDateISO.
- Deploy ~18:13 VN, PID 641906→645169, hash 4 bảng y nguyên.
- Ghi CHANGELOG + SSOT V10964b.

## Lỗ hổng A55

Thư mục báo cáo công khai `V10964b_*` **chưa tạo** khi kết phiên code — chỉ có CHANGELOG/SSOT. Phiên V10969 (02/08 tối) bù REPORT + CONTEXT này từ hồ sơ đã có, không bịa số.

## Không làm

- Không đổi cách tính số / roster / combo (QD-014).
- Không ghi Notion.
