# V10817 — Phối điều kiện rule GĐB đảo (miền trước / giải chú ý / nóng lạnh rơi gan) — 17/07/2026

- Owner 20:30: "phối ghép điều kiện để nâng tỷ lệ trên nền — số đảo xổ ở miền trước (MN/MT), đặc biệt giải đáng chú ý dùng soi cầu, hoặc nằm top nóng/lạnh/rơi/gan".
- Backtest 31 điều kiện + combo trên 2331 cặp (2020→2026), FDR toàn battery.
- TOP: E2 = (số đảo ∈ lô MT ngày D) ∧ (gan MB 3-9 ngày) = 88/287 = 30.7% vs nền 23.9% (+6.5pp, z=+2.69 raw) — rớt FDR.
- A6 = số đảo ∈ ĐB/G1/G7/G8 của MT ngày D = 28.4%, ổn 2 nửa (26.5/30.3) — "giải đáng chú ý" đúng ý owner, ứng viên bền nhất.
- MN ngày D = 22.8% hơi ÂM → "miền trước" chỉ có tín hiệu ở MT, không phải MN.
- Nền soi cầu tổng quát: MỌI số xổ MN∪MT chiều D+1 → về lô MB tối D+1 = 23.8% = đúng nền (z=+0.06) → "về miền trước dễ về MB" không tồn tại như quy luật chung.
- Placebo 2 lớp: mỗi biến thể trong 20 biến thể đảo-vị-trí tự chọn điều-kiện-tốt-nhất → median best-z = +2.23, biến thể owner hạng 3/20, 5/20 đạt z≥2.5 → mức 30.7% NẰM TRONG NHIỄU CHỌN-LỌC, chưa phải edge thật.
- Kết luận: hướng phối điều kiện ĐÚNG phương pháp; E2/A6 đáng theo nhưng chưa đủ chứng cứ → KHÔNG vào official/prompt; đo forward có kỷ luật.
- Deploy: bảng 🧩 PHỐI ĐIỀU KIỆN (5 điều kiện × full/2-nửa/120-gần/forward riêng) + dòng tín-hiệu-tối-mai vào khối 🔄 GĐB panel CHASE-BIAS /monitoring; cache view 4.2s→0.54s; health 200, admin 401, hash 4 bảng IDENTICAL.
- Tín hiệu 18/07: cand = 54 (GĐB 45739); MT(D)=✗ gan=7d hot7=0 → KHÔNG có tín hiệu E2 tối mai.
- Ngưỡng: rule gốc giữ mốc ~31/07 + ~16/08; lớp điều kiện đánh giá cùng mốc; nếu rule gốc đóng mà A6 forward ≥30% (n≥15) → mở case riêng A6; E2 cần ~6 tháng (3.7 tín hiệu/tháng).
- Chi tiết đầy đủ: GitHub public repo `V10817_PHOI_DIEU_KIEN_GDB_DAO_20260717/`.
