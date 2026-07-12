# V10792 — Giả thuyết đuôi-1 MB + quy luật hàng chục ngày mai: MEASURED_NULL (12/07 tối muộn, READ-ONLY)

**Owner 20:59:** "MB hầu như ngày nào hàng đơn vị các giải đều có số 1 đuôi (10/07: 31/61/81 · 11/07: 01/61/31 · 12/07: 11/71). Với khối lượng DB khổng lồ, tìm quy luật xác định số HÀNG CHỤC ngày tiếp theo (vd 81 → mai 01; 31 → mai 71). Số đuôi-1 ở giải 7 khả năng xổ lại hôm sau? Hay yếu tố nào khác?"

**Kết quả chính (2.334 ngày MB 2020→12/07/2026, BH FDR + walk-forward 3 cửa sổ OOS):**
- Quan sát ĐÚNG dữ kiện nhưng là **hệ quả toán học**: 27 lô/ngày → P(≥1 số đuôi-1) = 94.2% lý thuyết, đo 95.3%; **mọi đuôi 0-9 đều 93.4-95.3%** — đuôi 1 không đặc biệt.
- **Ma trận chuyển hàng chục 10×10: 0/100 ô qua BH**; hai cặp owner nêu đúng bằng nền (81→01 = 23.7% vs nền 23.5% · 31→71 = 24.5% vs nền 24.6%) — chuỗi 10-12/07 là pattern hồi tố 3 ngày.
- **G7 xổ lại hôm sau: 25.8% vs nền 23.8% (p=0.16, KHÔNG đạt)**; echo MB mức-số vốn ÂM −6pp (V10788) — echo thật ở MT +6pp/MN +12pp, /choi AE đang khai thác đúng chỗ.
- 17 họ yếu tố khác (gan, thứ, đuôi ĐB, streak, bóng, số kề, tổng, cặp bậc-2, lag-2/3, đếm digit) — **toàn bộ NULL** sau hiệu chỉnh.
- Walk-forward: chiến lược tốt nhất (ma trận chuyển trailing 730d) chỉ lift ở 1/3 cửa sổ OOS (z≤1.72, p≥0.09), 2 cửa sổ kia = mù → nhiễu regime, không phải quy luật.

**Kết luận/khuyến nghị:** KHÔNG tồn tại quy luật dùng được — không đặt tiền theo pattern đuôi-1; thích chơi echo thì miền đúng là MT/MN (qua /choi AE có sẵn), không phải MB. §52 panel forward KHÔNG dựng có chủ đích (tín hiệu đã bác ở n=2334, tránh zombie panel — ngược lean CP-L3); owner vẫn muốn thì ký 1 lệnh, dựng 1 phiên.

**READ-ONLY:** không deploy, không restart, hash 4 bảng không đổi. **FU:** FU-V10792-MB-TAIL1.

**Báo cáo đầy đủ:** GitHub `Lottery_AI_Notion_Reports/V10792_MB_TAIL1_TENS_PATTERN_20260712_PUBLIC_SAFE/BAO_CAO_V10792.md`
