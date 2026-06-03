# V10694 — Sửa thẻ UI lane test (mất số sáng sớm + thiếu ngày giờ + win/lose)

Public-safe. Đầu ngày T5 04/06/2026.

## 1. Owner báo 3 vấn đề (sáng sớm)
1. Thẻ lane test MN mất Bạch Thủ + số phụ 1/2.
2. UI không rõ ngày giờ của dự đoán.
3. Không hiển thị kết quả win/lose.

## 2. Căn nguyên (đã xác định, KHÔNG phải mất dữ liệu)
- **Lane test chạy buổi chiều (17:00–17:10)** sau khi model AI dự đoán đủ. Buổi sáng, dự đoán chính thức MN đã có (04:21) nên thẻ đọc ngày hôm nay (04/06) — nhưng số lane hôm nay chưa sinh → thẻ rỗng → biến mất.
- Thêm yếu tố lệch múi giờ: hàm ngày mặc định của CSDL trả giờ UTC, lệch 1 ngày vào sáng sớm giờ VN.

## 3. Đã sửa (chỉ đọc, không đụng luồng chính thức)
- **Tự lùi ngày (fallback)**: nếu hôm nay chưa có số lane → tự lấy ngày lane gần nhất + ghi rõ "ngày gần nhất, lane hôm nay chạy lúc 17:10". Thẻ KHÔNG còn biến mất.
- **Ngày giờ rõ ràng**: hiển thị "Dự đoán cho ngày DD/MM/YYYY · tạo lúc HH:MM".
- **Win/Lose**: đọc bảng kết quả đã chấm sau xổ → hiện ✓TRÚNG / ✗Trượt cho từng số (Bạch Thủ, số phụ 1, số phụ 2) + tổng Bạch Thủ / Lô.
- Khi chưa tới giờ lane: thẻ hiện thông báo "lane chạy 17:00–17:10", không để trống gây hiểu nhầm lỗi.

## 4. Kiểm chứng
- Sáng 04/06: thẻ MN tự lùi về 03/06 → BT=47 (Bạch Thủ Trượt, số phụ 2=52 Trúng, Lô trúng 1 phần). MT về 03/06 → BT=38 (Trúng cả 3 số).
- 4 bảng chính thức hash GIỐNG HỆT trước/sau khởi động lại.
- Dịch vụ chạy, không lỗi log.

## 5. Kiểm tra toàn diện đầu ngày (3 miền, 2 luồng, shadow)
- Chính thức: MN 04/06 đã dự đoán đủ (BT + lô 2 + lô 3 càng + xiên 2 + xiên 3). MT/MB chờ chiều (đúng lịch).
- Lane test: experiment chạy sáng đã có cho MN; nhóm thử nghiệm mới (full-pool/top-K/đa hướng) chạy 17:xx chiều.
- Shadow: đang tích lũy + chấm điểm sau xổ bình thường.
- Học máy: model mới 3.7 ngày tuổi (OK, không còn cảnh "dữ liệu cũ 22 ngày"); cơ chế tự sửa retrain chạy sáng nay 06:30; mining luật 4 ngày (theo tuần — bình thường).
- Theo dõi sức khoẻ: 16/16 OK.

## 6. Ghi chú
- Lane hiện xuất Bạch Thủ + số phụ 1 + số phụ 2 (theo chốt trước). "Xiên 2/3/4" thuộc bảng chính thức; nếu muốn lane có xiên cần thuật toán riêng (sẽ kiểm thử trước, không vội).
- Việc lệch múi giờ ở phạm vi rộng hơn: thẻ đã an toàn nhờ cơ chế tự lùi ngày; sửa rộng cần chủ sở hữu duyệt riêng.

STATUS: `PUBLIC_SAFE` — chỉ luồng lane-test; chính thức và MB không bị đụng.
