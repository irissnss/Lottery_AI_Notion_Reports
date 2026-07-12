# V10792 — Kiểm định giả thuyết "đuôi 1 MB + quy luật hàng chục ngày mai" (2026-07-12 tối muộn, READ-ONLY)

## 1. Yêu cầu owner (20:59, nguyên văn ý)

> "Anh thấy một điểm rất đáng xem đối với MB là hầu như hàng đơn vị của các bộ số của các giải đều có số 1 đuôi. Giống 10/07 có 31/61/81, ngày 11/07 có 01/61/31 và ngày 12/07 có 11/71. Với một khối lượng DB khổng lồ em hãy kiểm tra phân tích tìm một quy luật xác định số hàng chục sẽ xảy ra ngày tiếp theo. Ví dụ số 81 ngày → ngày hôm sau sẽ ra 01, hoặc 31 ngày trước → ngày hôm sau khả năng sẽ là 71. Với các số đơn vị nằm ở giải 7 khả năng xổ lại ngày hôm sau chẳng hạn, hay có các yếu tố nào khác để xác định được số hàng chục ngày hôm sau."

## 2. Phạm vi & kỷ luật đo

- **Dữ liệu:** `lottery_results` MB local đã sync live 21:00 (manifest `artifacts/live_sync/20260712_210012/manifest.json`) — **2.335 ngày** (2020-01-01 → 2026-07-12), 2.334 ngày đủ 27 lô (loại 1 ngày 2026-01-01 thiếu 1 lô do scrape), **2.324 cặp ngày liên tiếp**.
- **Kỷ luật:** kiểm định nhị thức 2 phía vs nền + hiệu chỉnh đa-so-sánh Benjamini-Hochberg FDR 10% + walk-forward out-of-sample (OOS) causal 3 cửa sổ năm độc lập. Trục canonical region+weekday thoả mãn (MB 1 đài/ngày ⇒ đài ≡ thứ).
- **Scripts:** `web/backend/_v10792_mb_tail1_probe.py`, `_probe2.py`, `_analysis.py`, `_analysis2-6.py`, `_matrix_export.py` — READ-ONLY 100% (chỉ SELECT).
- Extract khớp 100% quan sát owner: 10/07 = {31,61,81} · 11/07 = {01,31,61} · 12/07 = {11,71}.

## 3. Kết quả 1 — "Hầu như ngày nào cũng có số đuôi 1" là TOÁN, không phải tín hiệu

27 lô/ngày ⇒ P(≥1 số đuôi-1 trong ngày) lý thuyết = 1 − 0.9²⁷ = **94.2%**. Đo thực: **95.3%**.

| Đuôi | P(≥1 số/ngày) | TB lô/ngày | | Đuôi | P(≥1 số/ngày) | TB lô/ngày |
|---|---|---|---|---|---|---|
| 0 | 93.4% | 2.71 | | 5 | 93.6% | 2.65 |
| **1** | **95.3%** | **2.73** | | 6 | 93.9% | 2.70 |
| 2 | 95.1% | 2.77 | | 7 | 93.5% | 2.64 |
| 3 | 93.4% | 2.68 | | 8 | 94.1% | 2.70 |
| 4 | 93.6% | 2.68 | | 9 | 93.5% | 2.73 |

**Mọi đuôi 0-9 đều "hầu như ngày nào cũng có"** (93.4-95.3%). Đuôi 1 không đặc biệt. 30 ngày gần đây x1 hơi nóng (100% ngày có, 3.03 lô/ngày vs 2.70 kỳ vọng = +1.2σ — trong nhiễu Poisson) → giải thích vì sao mắt chú ý đúng lúc này.

## 4. Kết quả 2 — Ma trận chuyển hàng chục D→D+1: KHÔNG có quy luật

Ma trận đầy đủ (% ngày mai có b1, biết hôm nay có a1; **đậm** = lệch ≥3pp vs nền):

| hôm nay \ mai | 01 | 11 | 21 | 31 | 41 | 51 | 61 | 71 | 81 | 91 | n |
|---|---|---|---|---|---|---|---|---|---|---|---|
| **01** | 22.9 | 23.4 | 22.1 | 21.6 | 23.9 | 20.8 | 22.3 | 23.6 | 24.7 | 25.4 | 547 |
| **11** | **20.0** | 26.3 | 22.6 | 23.8 | 22.8 | 22.8 | 22.6 | 26.1 | 22.9 | 25.6 | 571 |
| **21** | 23.0 | 25.5 | 24.6 | 22.3 | 25.7 | 23.4 | 24.6 | 23.6 | 25.0 | 25.7 | 556 |
| **31** | 25.6 | 22.2 | 22.9 | 24.0 | 25.6 | 24.7 | 24.9 | 24.5 | 23.1 | **28.2** | 554 |
| **41** | 24.2 | 24.6 | 24.4 | 22.8 | 25.8 | 25.3 | 26.3 | 25.1 | 23.0 | 24.9 | 570 |
| **51** | 25.8 | 22.6 | 21.8 | 23.9 | 23.4 | 22.2 | 24.1 | 25.0 | 24.3 | 25.8 | 531 |
| **61** | 24.8 | 25.4 | 22.3 | 25.0 | 24.8 | 25.7 | 25.5 | 23.9 | **27.1** | 23.6 | 564 |
| **71** | 26.1 | **20.4** | **28.2** | 22.6 | 24.0 | 23.2 | 23.9 | 23.2 | 22.1 | 23.7 | 570 |
| **81** | 23.7 | 27.4 | 23.3 | 23.1 | 25.3 | 21.7 | 23.1 | 22.2 | 24.9 | 26.7 | 558 |
| **91** | 24.5 | 25.9 | 23.8 | 23.0 | 23.5 | 23.3 | 22.8 | 26.1 | 26.1 | 25.7 | 583 |
| *nền* | 23.5 | 24.6 | 23.9 | 23.8 | 24.6 | 22.9 | 24.4 | 24.6 | 24.0 | 25.1 | 2334 |

- Ô mạnh nhất: 71→21 = 28.2% vs nền 23.9% (p thô 0.019). Kiểm 100 ô cùng lúc ⇒ kỳ vọng nhiễu thuần ~5 ô p<0.05; thực tế chỉ có 3 ô. **0/100 ô qua Benjamini-Hochberg FDR 10%.**
- **Hai cặp anh nêu ví dụ: 81→01 = 23.7% (nền 23.5%, p=0.97) · 31→71 = 24.5% (nền 24.6%, p=1.00)** — trùng khít nền, tức chuỗi 10-12/07 khớp "quy luật" chỉ là pattern hồi tố trên 3 ngày.
- Lặp chính nó (a1→a1): tổng 24.54% vs kỳ vọng độc lập 24.15% — không có lực lặp.
- Lag-2 (cách 1 ngày): 0/100 BH. Lag-3: 0/100 BH.

## 5. Kết quả 3 — "x1 ở Giải 7 xổ lại hôm sau": KHÔNG đạt ngưỡng

| Giả thuyết | Kết quả | Nền | p |
|---|---|---|---|
| x1 nằm ở G7 hôm nay → CHÍNH SỐ ĐÓ về lại mai | 246/955 = **25.8%** | ~23.8% | **0.16 (không đạt)** |
| x1 nằm ở giải KHÁC → về lại mai | 1129/4649 = 24.3% | ~23.8% | 0.42 |
| G7 nói chung (4 số/ngày) → về lại mai | 2234/9296 = 24.0% | ~23.8% | 0.55 |
| Theo 8 vị trí giải (ĐB→G7) | max = Giải nhất 28.4% | — | 0.13 (nhiễu đa-test) |

Đối chiếu hệ thống sẵn có (V10788 audit độc lập, mức số-chính-xác): **echo lag-1 MB = −6pp ÂM** — MB là miền duy nhất số hôm trước về lại KÉM hơn nền. Echo dương thật nằm ở **MN +12pp, MT +6pp, cross MT→MB +7pp** — và AE trên /choi đang khai thác đúng các kênh đó rồi.

## 6. Kết quả 4 — 17 họ yếu tố khác: đều NULL

| Yếu tố | Kết quả | p |
|---|---|---|
| Gan/vắng lâu (0→≥8 ngày) | phẳng 21.7-26.8%, không dốc | — |
| Thứ × digit (trục canonical) | max T3×71 29.4% (70 ô) | 0.048 thô = nhiễu |
| Đuôi ĐB hôm nay (chục/đơn vị) → x1 mai | 23.4% / 23.7% | 0.40 / 0.62 |
| Digit về 2 ngày liên tiếp → ngày 3 | 23.9% | 0.85 |
| Tương quan SỐ LƯỢNG digit hôm nay ↔ mai | r = +0.001 | — |
| Hôm nay đúng 1 digit → digit đó lặp | 26.4% | 0.27 |
| Bóng dương (d→d+5) | 24.11% | 0.98 |
| Số kề (d±1) | 24.05% / 23.79% | 0.91 / 0.56 |
| Tổng digit mod 10 | 24.39% | 0.79 |
| Cặp digit bậc-2 {a,b}→c (450 ô, n≥80) | 0/450 qua BH (nhiễu kỳ vọng ~22 ô p<0.05) | — |

## 7. Kết quả 5 — Walk-forward OOS: chiến lược tốt nhất cũng không sống qua 3 cửa sổ

6 chiến lược chọn K digit cho ngày mai, học trailing 730 ngày causal (không nhìn tương lai), so với **mù = 24.8%/pick**:

| Cửa sổ test | S3 ma-trận-chuyển K=2 | S0 tần suất K=2 | Mù |
|---|---|---|---|
| OOS-3 (07/2023→06/2024) | 22.3% | 22.3% | ~24.8% |
| OOS-2 (07/2024→06/2025) | 23.9% | 23.8% | ~24.8% |
| OOS-1 (07/2025→nay) | **26.9%** | 24.7% | ~24.8% |

- Lift của S3 **chỉ xuất hiện ở 1/3 cửa sổ**; ngay tại cửa sổ tốt nhất z=1.32 (K=2, p=0.20) / z=1.72 (K=3, p=0.09) — chưa đạt chuẩn; per-quý dao động 19.6%→33.3% (không ổn định). Hai cửa sổ trước đó bằng/thua mù ⇒ **nhiễu regime, không phải quy luật**.
- Các chiến lược "lặp digit hôm nay", "digit chưa ra hôm nay", "ưu tiên G7", "vắng lâu nhất" đều ≤ mù ở K=2 và K=3.

## 8. KẾT LUẬN + khuyến nghị

1. **KHÔNG tồn tại quy luật hàng-chục-đuôi-1 hôm nay → mai dùng được ở MB** (2.334 ngày, 19 họ giả thuyết, BH FDR + 3 cửa sổ OOS). Mỗi digit hàng chục ngày mai vẫn ~24% bất kể hôm nay ra gì.
2. Quan sát "ngày nào cũng có x1" đúng dữ kiện nhưng đúng với **mọi** đuôi — đó là tính chất của 27 lô/ngày, không khai thác được.
3. "G7 xổ lại hôm sau" = 25.8% vs 23.8%, chưa đạt (p=0.16); và echo MB mức-số là **âm** (−6pp) — nếu anh thích chơi echo/lặp, miền đúng là **MT/MN** (AE /choi đang làm đúng kênh này), **không phải MB**.
4. Khuyến nghị thực dụng: **không đặt tiền theo pattern đuôi-1**; giữ nguyên cấu hình hiện tại (official = vote K11a/K15, /choi = AE echo MT/MN) — nhất quán kết luận trần accuracy V10705 và lean CP-L4.
5. §52: shadow table + panel forward **không dựng** có chủ đích (tín hiệu đã bị bác ở n=2334 — panel sẽ thành zombie mới, ngược lean CP-L3 vừa gỡ 6 panel). Nếu anh vẫn muốn panel theo dõi sống, ký 1 lệnh — em dựng trong 1 phiên đúng chuẩn.

## 9. An toàn & vệt

- READ-ONLY 100%: không deploy, không restart, không đụng official/lane//choi; hash 4 bảng local sau phân tích `f8450ee1/178ebec1/fa680019/0b85e796` (baseline sync 21:00, phân tích chỉ SELECT).
- Governance: CHANGELOG V10792 · SSOT block V10792 · FU-V10792-MB-TAIL1 (MEASURED_NULL) · AUTOMATION_STATE seq 253 · AUTOMATION_HISTORY append.
- Cross-ref các phiên trước: V10705 (trần official), V10788 (echo per miền ±pp), V10790-B (seesaw 2 mặt), V10791 (tổng kết tuần).
