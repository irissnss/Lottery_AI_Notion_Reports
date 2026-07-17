# V10816 — RULE "GĐB MB ĐẢO 2 SỐ ĐẦU → LÔ NGÀY MAI" CÓ MẠNH KHÔNG? (17/07/2026)

**Owner (19:52):** "anh thấy có một sự trùng hợp MB là giải đặc biệt hàng chục ngàn và hàng ngàn hay đổi vị trí và xổ ở ngày hôm sau ví dụ: ngày 16/06 [16/07] giải đặc biệt 96763 ==> hôm nay xổ có 69 đó em. xem kỹ dùm anh rules này có mạnh không em? Có cái nào rõ ràng và fix sớm hơn không em? thua quá em ơi"

---

## 1. VÍ DỤ CỦA ANH — VERIFY ĐÚNG

- GĐB MB **16/07 = 96763** → hàng chục ngàn (9) đổi chỗ hàng ngàn (6) = **69** → 69 CÓ trong 22 lô MB hôm nay 17/07 ✓
- Trùng kép thú vị: 69 cũng chính là BT official MB của 16/07 (trượt hôm đó, về hôm sau).

## 2. BACKTEST TOÀN LỊCH SỬ — RULE KHÔNG MẠNH NHƯ QUY LUẬT

Dữ liệu: 2331 cặp ngày liên tiếp (01/2020 → 07/2026), GĐB 5 chữ số parse từ `lottery_results`.

| Cửa sổ | Hit | Tỷ lệ | Nền kỳ vọng | z |
|---|---|---|---|---|
| **Toàn kỳ 6.5 năm** | 563/2331 | **24.2%** | 23.8% | **+0.42 (null)** |
| Nửa đầu | 294/1165 | 25.2% | 23.8% | +1.18 |
| Nửa sau | 269/1166 | 23.1% | 23.8% | −0.59 |
| 120 ngày cuối | 37/120 | 30.8% | 23.8% | +1.82 |
| 60 ngày cuối | 22/60 | 36.7% | 23.8% | +2.35 |
| **30 ngày cuối** | **12/30** | **40.0%** | 23.7% | **+2.10** |

- Nền 23.8% = xác suất 1 số bất kỳ nằm trong ~22-26 lô MB mỗi ngày — tức rule toàn kỳ KHÔNG hơn việc chọn số ngẫu nhiên.
- Quét CẢ HỌ 20 biến thể vị trí (mọi cặp chữ số GĐB, xuôi + đảo): **không biến thể nào qua FDR** — biến thể tốt nhất (trăm+ngàn, 25.7%, z=2.22 thô) đúng mức "thử 20 phép thì 1 phép z≈2 do may".
- Đảo 2 số đầu ăn thẳng ĐB hôm sau (trúng BT): 0.9% = nền 1% — không có gì.
- Weekday phẳng (21.6%-26.9%) — không có ngày ăn riêng.

## 3. NHƯNG VỆT NÓNG HIỆN TẠI LÀ THẬT — VÀ LỊCH SỬ NÓI NÓ SẼ XẸP

- 30 ngày cuối 12 hit (23/06→16/07), trong đó **chuỗi 12→16/07 = 5 ngày hit liên tiếp = ĐÚNG BẰNG kỷ lục 6.5 năm** (lần trước 09/2025):
  - 12/07 GĐB 10494→01 ✓ · 13/07 74299→47 ✓ · 14/07 59147→95 ✓ · 15/07 36119→63 ✓ · 16/07 96763→69 ✓
- Soi toàn lịch sử: cụm nóng ≥12/30 từng xuất hiện **8 lần** (~1.2 lần/năm — 2020, 2021, 2022, 2023, 2024, 2025×2, 2026-nay). Mức 40%/30d chính là TRẦN — chưa bao giờ cao hơn.
- **7 cụm trước: 30 ngày SAU trung bình ~24%** (37% / 13% / 37% / 20% / 17% / 27% / 17%) — tức đều xẹp về nền, không cụm nào duy trì.
- Null-sim 2000 lần (không quy luật, chỉ nền 23.8%): xác suất xuất hiện ≥1 cụm 12/30 đâu đó trong 6.5 năm = **100%** — cụm nóng kiểu này là điều CHẮC CHẮN xảy ra do ngẫu nhiên; chuỗi ≥4 ngày trong 30 ngày bất kỳ = 7.2% (hiếm vừa, 1/14).

**Kết luận trung thực:** ví dụ anh thấy là thật và vệt nóng là thật, nhưng đây là trạng thái hiếm của một rule mà toàn kỳ = null; 7 lần trước nó đều tự tắt trong ~30 ngày. KHÔNG nên đưa vào official/prompt. Em đã treo nó lên bảng đo forward — nếu lần này KHÁC 7 lần trước (vẫn ≥40% sau 30 ngày) thì mình nói chuyện tiếp bằng số liệu.

## 4. ĐÃ LÀM GÌ (§52 CHAIN, DEPLOY 20:1x)

- Khối **🔄 GĐB MB ĐẢO 2 SỐ ĐẦU** trong panel 🏃 CHASE-BIAS tại `/monitoring`: full/nửa/120-60-30d/**FORWARD từ 17/07**, chuỗi hiện tại, 8 cụm nóng + follow-through, 10 ngày gần, **số theo dõi ngày mai**.
- Backend `_gdb_swap_stats()` (read-only từ `lottery_results`) trong view chase-bias; gate `node --check` PASS; health 200; admin 401; **hash 4 bảng official PRE=POST IDENTICAL**; ZERO đụng `/du-doan`, prompt, miner.
- **Ngưỡng hành động ghi sẵn:** ~16/08 (30d forward): ≥12/30 (≥40%) → trình anh cân nhắc side-bet lô /choi; ≤~28% → đóng (mean-revert như 7 cụm trước). Checkpoint giữa ~31/07: ≥7/14 → báo sớm.
- **Số theo dõi ngày mai 18/07: GĐB hôm nay 45739 → đảo 2 số đầu = 54.**
- Ghi chú: rule engine (miner) hiện chỉ làm họ tail-giải, chưa phủ họ đảo-vị-trí-chữ-số — nếu forward giữ ≥40% sẽ bàn mở rộng họ rule tại checkpoint.

## 5. "CÓ CÁI NÀO RÕ RÀNG VÀ FIX SỚM HƠN KHÔNG?" — CÓ, XẾP THEO ĐỘ CHẮC

| # | Việc | Bằng chứng | Trạng thái |
|---|---|---|---|
| 1 | **K11a MB flip về champion** | Champion đúng bị thay **4 lần** (11+15+16+17/07: 98✓→64✗, 57✓→64✗, 16✓→69✗, 02✓→34✗); 9 ngày challenger 1/9 vs champion 4/9 = net **−3 ngày** | **Chờ chữ ký anh — OK là em flip NGAY tối nay** (1 dòng kill-switch, đảo ngược được) |
| 2 | B1: hạ reasoning gpt-5.5 HIGH→default | Đốt ~$1.3/ngày, BT 37%→27% sau khi bật HIGH | Chờ chữ ký (1 dòng) |
| 3 | CP-L6 19/07 (2 ngày nữa) | gemini-3.5-flash 43% vs 2.5-flash 29% (7d) → swap; retire glm-5.1; align tier best-spots; retire gpt-5.5→grok-4.3 | Đúng lịch |
| 4 | Rule GĐB-đảo này | Toàn kỳ null | Không fix được gì ngay — chỉ forward |

**Artifacts:** `_v10816_gdb_swap_probe.py` · `_v10816_streak_probe.py` · `_v10816_deploy.py` · backup `backups/v10816_pre/` + VPS `backups/v10816_vps/`.
