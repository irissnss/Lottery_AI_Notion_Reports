# V10823 — Verify 93 lose TRUNG THỰC + quét 7 biến thể (giữ M2s) + panel "TOTAL 10 NGÀY THAY ĐỔI LỚN"

**Owner 22:00 18/07:** "Đã backtest verify kỹ chưa? Sao 93 là lose — trung thực đó hả? Làm nổi bật dễ nhìn hơn? Đã thử hết các phương pháp chưa? Đặt tên chỗ này là TOTAL 10 NGÀY THAY ĐỔI LỚN — nằm lọt giữa khó xem."

**1. Verify — 93 lose là THẬT:**
- MB tails 18/07 (24 số) KHÔNG có 93 → BT trượt thật; CÓ 86 → phụ VỀ lô. Panel chấm khớp 100% DB, không tô hồng.
- Kỳ vọng đúng: M2s BT 30-48%/miền — đa số ngày vẫn trượt BT; giá trị = chênh +9→+11.5pp vs bundle cũ cộng dồn.

**2. "Thử hết chưa?" — quét thêm 7 biến thể (khung leak-safe 165d):**
- VA main-weight · VC WR-rules · VD multi-rule · VE dual-gate · VF main-gate · VH hedge · W3 bộ-3.
- BT-gộp FULL/60d: M2s 40.0/38.9 — VC 41.0/40.6, VE 41.0/39.4 (nhỉnh ≤1.7pp = trong nhiễu), VH làm sập any MB, W3 tăng any nhưng 1.5× vốn.
- KẾT LUẬN: không ai thắng M2s bền → GIỮ M2s cho 10 ngày đo; VC re-check sau 28/07 bằng forward.

**3. Panel theo lệnh owner:**
- Đổi tên "🧮 TOTAL 10 NGÀY THAY ĐỔI LỚN", dời từ giữa trang lên vị trí #2 (sau 🎯 BẢNG NÊN CHƠI), viền vàng + glow.
- Khối SỐ CHƠI HÔM NAY: chip số TO nhãn BT/phụ, màu trung thực (xanh=VỀ, đỏ=TRƯỢT, xám=chờ); lịch sử ✓/✗ từng số (field `marks` mới).

**Verify deploy:** sha khớp, restart ngoài giờ job học, health 200/admin 401, journal sạch, hash 4 bảng IDENTICAL. UI-only — phương pháp lane/shadow KHÔNG đổi.

**Mốc:** 19/07 xem panel mới + 3 rows lane forward đầu · 28/07 chốt M2s vs M0 + re-check VC.

**Chi tiết:** GitHub `Lottery_AI_Notion_Reports/V10823_TOTAL10_PANEL_VARIANTS_20260718/`
