# Ngày 31/07 — V10885 → V10891 (tóm tắt)

**Sáu việc trong ngày, đều từ câu hỏi owner. Hash official IDENTICAL xuyên suốt.**

- **V10885** Gemini: khoá chính hãng, official 0 rớt/91×2 lane; chỉ shadow 3.5 rớt 5,3%. Tự sửa con số 27% em báo sai hôm trước (lát cắt 11 ngày).
- **V10886** Nâng lên `gemini-3.6-flash`: 3.5 nghỉ hưu giữ 76 dòng đối chứng, 3.6 là lane mới `first_run=01/08`, gọi thử thật trước khi khai.
- **V10887** "/nghiem-thu chưa khởi sắc" vì 49% ngày hai bên chọn cùng số. Tách riêng 69 ngày lệch: **bản mới 25 · official 10 · p=0,017** — thêm khối "Chỗ đáng nhìn nhất" lên đầu trang.
- **V10888** Thử tải dồn: Google 34/36 (rớt 5,6% ≈ 5,3% production) · OpenRouter 36/36. Vá: gặp 503 nhảy OpenRouter ngay, ~5% lưu lượng, dưới $1/tháng. Chứng minh bằng ép lỗi.
- **V10889** Official đúng hạn 0/9 ngày; same-day MT đã cắt đúng như owner nhớ (V10766, chỉ nhóm ML); chứng minh luồng không bốc số bằng bịt mắt + số học tay + thống kê; đính chính 2 trang Notion.
- **V10890+V10891** Owner bắt đúng: các luồng NGOÀI official trễ — khoá `/choi` trễ 4/8 ngày MT, 3/5 MB. Gốc: hệ dựng quanh cutoff 17:00/18:00, muộn hơn hạn thật 5 phút. **Dời 23 mốc cron** theo chuỗi owner ký: total xong 16:50/17:50 · khoá /choi 16:53/17:53 · hạn 16:55/17:55. Chốt chặn tự động 18:02/ngày trên `/monitoring` — hồi tố: 30/07 trễ 33 mục, 29/07 trễ 32 mục.

**Theo dõi:** guard chấm ngày đầu tối nay 18:02 · 3.6-flash chạy 01/08 · Nghiệm Thu chốt sớm nhất 06/08 · hạn chót 19/08.

Báo cáo đầy đủ: `V10885_V10891_DAY_20260731/REPORT_V10885_V10891.md`
