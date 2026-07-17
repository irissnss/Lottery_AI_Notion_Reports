# V10817 — PHỐI ĐIỀU KIỆN CHO RULE "GĐB MB ĐẢO 2 SỐ ĐẦU → LÔ D+1" (2026-07-17 20:30 → 21:0x)

## 0. Câu hỏi của owner (20:30)

> "để nâng tỷ lệ trên nền em phải phối ghép điều kiện nữa mới được anh nghĩ vậy? ví dụ như số đảo đó có xổ ở miền trước như miền nam hoặc miền trung đặc biệt là rơi vào các giải đáng chú ý dùng để soi cầu đó em, hoặc số đảo đó nó nằm trong tóp số nóng lạnh rơi hoặc gan gì đó phối các điều kiện vào nữa để có thể nâng tỷ lệ cao lên và loại bỏ thêm các % ngoài nền ah em. Xem kỹ dùm anh. Rules và pattern chắc chắn có lý của nó nhưng thiếu điều kiện em thử bổ sung thêm các điều kiện vào xem có tăng tỷ lệ cao hơn không nào em?"

## 1. Thiết kế test — đúng từng lớp anh nói (2331 cặp ngày 2020→2026)

Rule nền: cand = GĐB MB(D) đảo 2 số đầu → có trong lô MB(D+1)? Nền = 24.2% (563/2331).

- **Lớp A — "xổ ở miền trước" ngày D**: cand có trong lô MN(D) / MT(D) / cả hai; riêng biến thể "giải đáng chú ý" = ĐB, G1, G7, G8 (các giải dân soi cầu hay dùng đầu/đuôi).
- **Lớp B — soi-cùng-ngày D+1**: MN xổ 16:40, MT 17:40, MB 18:15 → chiều D+1 biết kết quả MN/MT TRƯỚC khi MB quay, vẫn kịp đặt. Test cand có về MN/MT chiều D+1 không.
- **Lớp C — nóng/lạnh/rơi/gan của MB** tính đến hết ngày D: rơi (về hôm D), hot7 (số lần về trong 7 kỳ), gan (số ngày chưa về: ≥5, ≥10, 3-9…).
- **Lớp D/E — combo** các điều kiện trên (11 combo).

Tổng 31 điều kiện, FDR toàn battery. Mọi số liệu so với kỳ vọng nền THEO NGÀY (|lô D+1|/100, ~23.8%).

## 2. Kết quả — bảng xếp hạng chính

| Điều kiện | n | hit | rate | nền | z | ghi chú |
|---|---|---|---|---|---|---|
| **E2 = lô MT(D) ∧ gan MB 3-9 ngày** | 287 | 88 | **30.7%** | 23.9% | **+2.69** | TOP — nhưng rớt FDR (cần p≤0.0016) |
| A2 = cand ∈ lô MT(D) | 781 | 208 | 26.6% | 23.8% | +1.84 | nửa đầu 29.2% / nửa sau 24.0% = phai dần |
| **A6 = cand ∈ ĐB/G1/G7/G8 MT(D)** | 197 | 56 | **28.4%** | 23.8% | +1.52 | **ổn 2 nửa (26.5/30.3), 120 tín hiệu gần 42.9% — "giải đáng chú ý" đúng ý anh, ứng viên bền nhất** |
| C3 hot7≥3 | 499 | 130 | 26.1% | 23.8% | +1.17 | nóng nhẹ, không đủ |
| B3 = MN∪MT(D+1) soi-cùng-ngày | 1427 | 347 | 24.3% | 23.8% | +0.44 | ~nền |
| C1 rơi (về MB hôm D) | 559 | 137 | 24.5% | 23.8% | +0.37 | ~nền |
| C4 gan≥5 | 642 | 153 | 23.8% | 23.8% | −0.01 | =nền |
| A1 = cand ∈ lô MN(D) | 1020 | 233 | 22.8% | 23.8% | −0.71 | **hơi ÂM — "miền trước" chỉ có tín hiệu ở MT, KHÔNG phải MN** |

Nền soi cầu tổng quát (đo cho chắc): MỌI SỐ xổ MN∪MT chiều D+1 → về lô MB tối D+1 = 33774/141953 = **23.8% = đúng nền (z=+0.06)**. "Số về miền trước dễ về MB" KHÔNG tồn tại như quy luật chung; giải-đáng-chú-ý cũng 23.8%; "rơi" MB D→D+1 cũng 23.9%.

## 3. Placebo 2 lớp — vì sao 30.7% CHƯA phải edge thật

- **Lớp 1**: áp CÙNG điều kiện E2 lên cả 20 biến thể đảo-vị-trí GĐB → biến thể của anh (hàng chục ngàn ↔ hàng ngàn) đứng NHẤT (+6.5pp), nhưng 2/20 biến thể cũng đạt z≥2.0 (null kỳ vọng ~0.5); E2 theo năm dao động 21-41% (2021: 23.7%, 2024: 21.4%) — không bền.
- **Lớp 2 (selection-aware)**: cho MỖI biến thể tự chọn điều-kiện-tốt-nhất trong cùng 31 điều kiện → **median best-z toàn họ = +2.23; biến thể của anh xếp hạng 3/20; 5/20 biến thể đạt best-z ≥ 2.5** (cao nhất (3,4)+hot7≥3 z=+2.96 — còn cao hơn của anh). Nghĩa là: cứ đào 31 điều kiện trên 1 biến thể bất kỳ thì THƯỜNG moi được ~z2.3 chỉ do may.

**Kết luận trung thực**: hướng phối điều kiện của anh là ĐÚNG PHƯƠNG PHÁP (và trên lịch sử nó có nâng 24.2% → 30.7%, lọc bỏ ~88% ngày nhiễu), nhưng sau khi trừ nhiễu chọn-lọc thì mức tăng chưa chứng minh được là thật. E2 và A6 là 2 ứng viên đáng theo — em đưa lên panel đo forward, KHÔNG đưa vào official.

## 4. Đã deploy (§52 chain đủ)

- `_gdb_swap_stats()` mở rộng: parse 3 miền + giải-chú-ý (fix dấu tiếng Việt — key DB là "Giải Đặc Biệt" có dấu) + gan/hot7; khối `conditions` 5 điều kiện (E2/A2/A6/B3/C2) mỗi cái có full/2-nửa/120-tín-hiệu-gần/**forward riêng**; `watch.e2_ok` = tối mai có tín hiệu E2 không; cache → view nhanh 8x (4.2s → 0.54s).
- UI: bảng **🧩 PHỐI ĐIỀU KIỆN** trong khối 🔄 GĐB panel CHASE-BIAS `/monitoring` + dòng **tín hiệu tối mai** (18/07: cand=54 từ GĐB 45739; MT(D)=✗, gan=7d, hot7=0 → KHÔNG có tín hiệu E2).
- Verify: health 200 · admin 401 · 5 conditions khớp probe · hash 4 bảng PRE=POST IDENTICAL · journal sạch. Backup 2 đầu (local git HEAD + VPS).

## 5. Ngưỡng hành động (ghi sẵn)

- Rule gốc: giữ mốc V10816 — 14d (~31/07) ≥7/14 báo sớm; 30d (~16/08) ≥40% trình side-bet / ≤28% đóng.
- Lớp điều kiện: đánh giá CÙNG các mốc trên. E2 tần suất ~3.7 tín hiệu/tháng → cần ~6 tháng đủ n≈22. Nếu rule gốc đóng vì mean-revert mà A6 forward vẫn ≥30% (n≥15) → mở case riêng cho A6.

## 6. Artifacts

`web/backend/_v10817_cond_probe.py` · `_v10817_cond_probe2.py` · `_v10817_placebo_probe.py` · `_v10817_bestof_probe.py` · `_v10817_deploy.py` · backup `backups/v10817_pre/` + VPS `backups/v10817_vps/` · CHANGELOG V10817 · SSOT V10817 · FU-V10816-GDB-SWAP (mở rộng) · AUTOMATION_STATE seq 278.
