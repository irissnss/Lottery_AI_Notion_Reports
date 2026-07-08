# BÁO CÁO TỔNG V10787 — AUDIT LIVE 07-08/07 + ĐỐI CHỨNG 3 MẶT (OFFICIAL / LANE / CHOI)

Ngày: 2026-07-08 (chiều) · Phiên: V10787 · FU: `FU-V10787-THREE-SURFACE` · governance seq: 242

Câu hỏi owner (08/07, nguyên văn): *"Điều lại lùng là office 1 đường , lane test 1 nẻo , và /choi 1 kiểu . Mỗi cái trúng mỗi kiểu. Em không tìm ra được điểm mạnh để có output hoàn hảo nhất ah em"*

---

## PHẦN 1 — TRẢ LỜI THẲNG CÂU HỎI

### 1.1 Vì sao 3 mặt "mỗi cái một kiểu" — đó là THIẾT KẾ, không phải lỗi

| Mặt | Số lấy từ đâu | Vai trò |
|---|---|---|
| **OFFICIAL /du-doan** | Weighted voting 26 model (+ MB doctrine đầu tháng) | Số publish chính thức |
| **LANE test** | 20+ method thử nghiệm chạy shadow mỗi ngày | Phòng thí nghiệm — CHƯA vào official |
| **/choi** | Method ĐÃ KHÓA theo tuần (owner ký): MN=BT1-official · MT=AE · MB=AE | Tiền thật — chơi 1 method, bám cả tuần |

Số đo (từ 10/05, cùng thước /choi: song thủ × 50 điểm × tất cả đài, 1 ăn 98k, cost 18k/27k):
**3 mặt gần như KHÔNG BAO GIỜ chọn trùng số** — same-pick: MN **0/57 ngày** · MT **3/58** · MB **0/34**.
Selector khác nhau → số khác nhau → "mỗi cái trúng mỗi kiểu" là hệ quả toán học, không phải hệ thống loạn.

### 1.2 Bù trừ có thật — nhưng "trộn thành 1 output hoàn hảo" thì THUA TIỀN

Đối chứng BT official vs BT lane-AE (method /choi đang chơi), từ 10/05:

| Miền | n ngày | Official hit | Lane hit | Cả 2 trúng | Chỉ OFF | Chỉ LANE | Cùng trượt | Trần chọn-đúng-mặt |
|---|---|---|---|---|---|---|---|---|
| MN | 57 | 45.6% | 50.9% | 12 | 14 | 17 | 14 | **75.4%** |
| MT | 58 | 31.0% | 39.7% | 8 | 10 | 15 | 25 | **56.9%** |
| MB | 34 | 20.6% | 32.4% | 2 | 5 | 9 | 18 | **47.1%** |

Trần 75/57/47% nghe hấp dẫn — nhưng đó là **hindsight** (biết trước mặt nào trúng mới chọn được). Cách khả thi duy nhất để "ăn cả 2 mặt" là đánh CẢ 2 số mỗi ngày — và em đo luôn P&L cặp gộp [off-BT, lane-BT]:

| Miền | Cặp OFFICIAL | Cặp LANE | Cặp GỘP off+lane | Verdict |
|---|---|---|---|---|
| MN | -14.5M | **+47.2M** | +30.6M | Gộp THUA lane đơn |
| MT | **+31.7M** | +20.6M | +8.2M | Gộp THUA official đơn |
| MB | -2.5M | **+25.8M** | +1.3M | Gộp THUA lane đơn |

**Cả 3 miền: gộp đều thua mặt tốt nhất** — vì tiền cược x2 (2 số × tất cả đài) nuốt sạch lợi ích bù trừ. Cửa sổ gần (17/06→nay) cũng cùng kết luận (MN -5.1 · MT +8.9 · MB -12.6 khi gộp).

### 1.3 Vậy "điểm mạnh" thật nằm ở đâu?

**Không có output hoàn hảo bằng cách trộn. Điểm mạnh = CHỌN ĐÚNG MẶT THEO MIỀN, rồi bám — chính là cơ chế weekly-lock /choi đang làm.** Và lock tuần 06/07 anh đã ký KHỚP với data 21 ngày gần:

| Miền | Lock tuần 06/07 (anh ký) | Data 21d gần nói gì | Khớp? |
|---|---|---|---|
| MN | `MN_BT1_OFFICIAL_V1` | Official +8.6M/21d · lane AE **-6.1M/21d** (nguội rõ sau khi +35.9M nửa đầu) | ✅ ĐÚNG mặt |
| MT | `MT_ADAPTIVE_EXPLOIT_V1` | Official +30.7 vs lane +30.7 — HOÀ 21d | ✅ chấp nhận |
| MB | `MB_ADAPTIVE_EXPLOIT_V1` | Lane **+36.4M/21d** vs official **-7.7M/21d** — lệch nặng | ✅ ĐÚNG mặt |

Ý nghĩa thực dụng: mặt YẾU nhất hiện nay là **MB official** (doctrine đầu tháng đang 1W-1L, scorecard theo dõi riêng) — nhưng /choi KHÔNG chơi MB official nên tiền thật không dính. MN lane AE nguội là lý do data ủng hộ việc anh chuyển MN sang BT1-official tuần này.

### 1.4 Công cụ mới để anh nhìn thấy điều này mỗi tuần (deploy live 14:01 hôm nay)

Panel **SO GĂNG 3 TẦNG** tại `/monitoring` giờ có thêm khối **⚔ ĐỐI CHỨNG official vs lane-AE** cho từng miền: hit % 2 mặt · bù trừ (cả2/chỉOFF/chỉLANE/cùng trượt) · trần chọn-đúng-mặt · P&L 3 cặp (off/lane/gộp) · verdict `GỘP THẮNG / gộp KHÔNG hơn — đừng trộn`. Quy trình đề xuất: **mỗi thứ 2 trước khi khóa tuần, nhìn khối này + hàng BỀN để chọn mặt cho từng miền.** Nếu tương lai `merge_wins=True` xuất hiện 2 tuần liên tiếp ở miền nào, em sẽ trình phương án cặp gộp cho miền đó — hiện tại cả 3 = False.

---

## PHẦN 1B — "3 LUỒNG CŨNG ĐOÁN MÒ À?" (owner hỏi tiếp 14:59 — đo vs random baseline)

Phương pháp: (a) z-test Poisson-binomial — kỳ vọng trúng ngày d = số-đuôi-distinct/100 của chính ngày đó; (b) Monte Carlo 5000 người bốc số ngẫu nhiên 00-99 qua CÙNG kinh tế /choi. Probe: `_v10787_random_baseline.py` (READ-ONLY). 59 ngày từ 10/05.

**Kết quả BT 1 số vs đoán mò:**

| Mặt | MN | MT | MB | Combined 3 miền |
|---|---|---|---|---|
| Đoán mò (baseline) | 42.8% | 35.0% | 23.7% | — |
| OFFICIAL | 44.1% (z=+0.2) | 30.5% (z=-0.73) | **15.3% (z=-1.53)** | **z=-1.12 ≈ MÒ** |
| LANE AE | 50.9% (z=+1.24) | 39.7% (z=+0.74) | 32.4% (z=+1.18) | **z=+1.78, p≈0.038 — EDGE THẬT** |
| Top model | 44.8% (z=+0.31) | 44.1% (z=+1.47) | 27.1% (z=+0.61) | z=+1.38 |

**Monte Carlo P&L (dân đoán mò median ÂM vì house edge ~2%):** lane pair thật +47.2/+20.6/+25.8M = percentile **91.2/75.0/89.0** so với 5000 người mò (median mò -8.6/-8.8/-3.6M). Official pair MN percentile 40.8 (thua cả median mò), MB 47.2.

**Kết luận trung thực:** (1) Trực giác anh ĐÚNG cho mặt official-BT — nó không phân biệt được với đoán mò, MB còn TỆ hơn mò (z=-1.53, thêm bằng chứng cho scorecard doctrine). (2) Nhưng KHÔNG phải cả hệ là mò: lane AE có edge thật cùng chiều cả 3 miền (p≈3.8%), P&L top ~10% so với dân mò trong khi dân mò lỗ. (3) Edge là KHIÊM TỐN (+5-9 điểm hit, ~+40-90k/điểm-ngày kỳ vọng) — không phải máy in tiền, phải chơi bằng kỷ luật lock + size. (4) MN BT1-official 1-số: +0.1M/59 ngày = percentile 52 ≈ hoà vốn lịch sử — lock hiện tại sống nhờ form 21d (+8.6M) + chữ ký E5; em gắn trigger: 21d chuyển âm → trình đổi mặt. Badge z + mốc "đoán mò %" đã thêm vào khối ⚔ /monitoring (deploy 15:06, hash IDENTICAL, backup `v10787c_pre_20260708_150608`).

## PHẦN 1C — MT DEEP-DIVE (owner 17:54: "ML MT thảm hại khi thay đổi, xem kỹ output MT cả 3 luồng")

**MT hôm nay 08/07 (Đà Nẵng + Khánh Hòa, 29 đuôi):**

| Luồng | Số | Kết quả |
|---|---|---|
| OFFICIAL | BT=59, lo2=[59,41] | ✗✗ — chuỗi thua BT 4 ngày |
| LANE AE (/choi chơi) | BT=63, lo2=[63,37] | **63 TRÚNG** |
| /CHOI daily lock | [63,37] khóa 16:40 | **+1.3M** — tuần: +6.2 / -3.6 / +1.3 = **+3.9M** |

→ Mặt tiền thật /choi MT KHÔNG thảm (2/3 ngày ăn từ đổi lock). Thảm là **official** (21d chỉ 4/19 = 21%, DƯỚI mức đoán mò 35%) và **ML**.

**ML MT — kiểm chứng "thảm khi thay đổi":** combo-super 0/3 (nền 49%/35 ngày) · random-forest 1/3 · meta-learning 0/3 · smart-ml 1/3 · ngoại lệ lstm 2/3. Nhưng (a) KHÔNG có thay đổi nào trong ML vào 06/07 — ML chạy nguyên code/data cũ; (b) mẫu 3 ngày quá nhỏ; (c) cả miền lạnh (07/07: 0/26 model trúng). → ML lạnh là triệu chứng, không phải bệnh do "thay đổi".

**Thay đổi THẬT từ 06/07 và phát hiện chính — BẦY ĐÀN:** 3 model mới (gemini-3.5-flash, qwen3.7-max, glm-5.2) vào voting từ 06/07 và bám herd nặng (trùng herd top1 5-6/9 lượt). Concentration top1 MT nổ: 06/07 = 12 model chụm 76✗ (46%) · 07/07 = 11 chụm 37✗ (42%) · 08/07 = **15/26 chụm 86✗ (58%)** — nền cũ ≤31%. Đo 30 ngày: **bầy ≥10 model tại MT chỉ trúng 12% (1/8) = ANTI-SIGNAL** (bầy ≤5 trúng 50-67%; MN 40%, MB 25%). 86 hôm nay thậm chí không phải lô gan (mới về hôm qua) — herd đoán theo nhau, không theo data.

**Lane AE MT bản chất:** lag-1 echo có chủ đích (V66) — 13/23 ngày BT AE = official hôm trước, 5 phiên gần đều echo. Hôm nay ăn 63 = đúng kiểu "số official hôm qua về trễ 1 ngày". Edge này là lý do AE MT z=+0.74 trên mò.

**Deploy 18:05 (guard MB chain xong mới restart):** khối `herd` trong module + panel **🐑 BẦY top-1** mỗi miền tại /monitoring (số bầy hôm nay + hit 30d theo cỡ bầy, cảnh đỏ khi ≥10). Sandbox PASS · health 200 · admin 401 · hash 4 bảng IDENTICAL · backup `v10787d_pre_20260708_180510`.

**Đề xuất K9 (CHỜ KÝ):** lane shadow `HERD_FADE_V1` — khi bầy top1 ≥10 model thì né số đó, thay bằng ứng viên hạng 2 ngoài bầy; đo shadow 14 ngày rồi mới bàn. KHÔNG đụng official voting khi anh chưa ký.

## PHẦN 1E — ĐÍNH CHÍNH + XÁC NHẬN "OUTPUT ĐANG BÁM THEO ML" (owner 18:31)

Anh hỏi "Em có xem kỹ không mà nói thế — output hiện tại đang bám theo ML thì phải, và ML MT đang không ổn". Em tái dựng phiếu bầu official MT từng ngày theo đúng logic production (gate BT≥14%/WR≥28% + cap top-13 theo BT-rate 30 ngày + trọng số BT × strength × verdict):

**ANH ĐÚNG — và em đính chính phần 1D:**

| Ngày | Official BT | Ai bầu số đó |
|---|---|---|
| 04/07 | 98 ✓ | 5 ML — 0 AI |
| 05/07 | 49 ✗ | 6 ML — 0 AI |
| 06/07 | 76 ✗ | 3 ML + 2 AI |
| 07/07 | 63 ✗ | 6 ML — 0 AI |
| 08/07 | 59 ✗ | **6 ML — 0 AI** (điểm vote: 59=0.337 thắng 41=0.283 của claude-opus+gemini-pro) |

- **13/14 ngày gần nhất, số official MT = đúng số khối ML bầu chụm** (match 30 ngày = 82%).
- Cơ chế: 7/13 ghế voters là ML và khối này **chụm 5-6/7 model vào 1 số** (chung pipeline anh em: random-forest / smart-ml / smart-ensemble / combo-no-token / meta-learning) trong khi 6 model AI tán loạn mỗi con một số → vote trọng số LUÔN nghiêng khối ML. Official MT thực chất là "máy đồng thuận ML".
- **ĐÍNH CHÍNH:** hôm qua em nói official bị bầy-86 kéo là SAI. Bầy 86 gồm 15/26 model nhưng 3 model mới chỉ chạy shadow (không có quyền vote); official không chọn 86 — nó chọn 59 của khối ML. Em xin lỗi vì kết luận vội.
- **ML MT không ổn — đúng:** form 7 ngày: meta-learning **0/7** (vẫn giữ ghế vote vì gate dùng BT-rate 30 ngày = trọng số nguội 26.7%) · combo-super, combo-no-token, smart-ensemble 2/7 · random-forest, smart-ml, xgboost 3/7. Ngược đời: lstm 3/7 (nóng nhất khối) bị gate loại (13.3% < 14) và claude-sonnet-4-6 (4/7 = 57% tuần này) bị cap top-13 loại; claude-opus-4-6 đang 6/7 = 86% tuần này có vote nhưng bị khối ML đè.

**Phản chứng (mô phỏng vote, 14 ngày / 35 ngày):** ACTUAL 29%/29% · bỏ-ML 36%/31% · chỉ-ML 36%/37% · trọng-số-recency(7d×60%+30d×40%) 43%/34%. Chênh 1-3 hit = trong nhiễu thống kê → em KHÔNG đề xuất đổi selector từ data này. Chẩn đoán đúng: vấn đề không phải "có ML trong vote" — mà là **khối ML tương quan cao hoạt động như 1 phiếu khổng lồ, và khi khối lạnh thì official chết chùm nguyên chuỗi** (4 ngày).

**Deploy 18:53 (guard: 3 bundle hôm nay xong + qua 18:10):** khối `ml_bloc` trong module + panel **🤝 OFFICIAL bám khối ML** mỗi miền tại /monitoring: % ngày official = phiếu khối (30d), hit khối vs hit official, số khối hôm nay + form 7d từng model ML. Sandbox PASS (MT match 82% · MN match 27% — official MN KHÔNG bám ML và đang khoẻ 45% · MB match 58%) · health 200 · admin 401 · hash 4 bảng IDENTICAL (`8d0ddc04/5243ade7/76af5ec6/59b55081`) · backup `.bak_20260708_185351`.

**Đề xuất K10 (CHỜ KÝ):** lane shadow `ML_BLOC_DEDUP_V1` — de-correlation: khối ML sibling đếm như 1.5 phiếu thay vì 5-6 phiếu, đo shadow 14 ngày song song K9 (K9 đo mặt bầy-26-model, K10 đo mặt khối-ML-trong-13-voter — bổ sung nhau). KHÔNG đụng official khi anh chưa ký.

## PHẦN 2 — AUDIT LIVE 07-08/07 (cùng phiên, hỏi trước đó)

- **Kết quả 07/07:** BT 3 miền đều LOSE (MN 30 · MT 63 · MB 87). MT lạnh sâu: 0/26 model WIN. MB: doctrine ML-plurality chọn 87 trong khi plain-vote top1=62 TRÚNG (12 model WIN với 62) → **scorecard doctrine 06-07/07: 1W-1L**, backtest owner-ký +30.8M, 1 ngày thua chưa đủ revert — theo dõi hết dom≤10.
- **Coverage 07/07:** 78/78 rows (26 model × 3 miền) · 1 empty duy nhất = gemma MB 429 (K8 CHỜ KÝ) · **late-fill cứu ca thứ 2**: gemma MT timeout 439s → kết quả về ghi late=1 lúc 10:00 (model khác qwen — cơ chế generalize đúng).
- **Vật theo dõi cũ:** kimi rt=1 KHÔNG tái diễn · glm-5.1 sạch 2 ngày · gpt-5.5 sạch tiếp.
- **Hạ tầng:** T-10 đúng giây 2 ngày · watchdog 96+ tick 0 alert · MDE 78 rows · verify 0 pending · cron gate 07:30 log ra file từ 08/07 (`all_pass=true`) · 0 restart · 0 ERROR.
- **/choi tuần 06/07 sau 3 ngày:** MN BT1 +1.7M · MT AE -2.8M · MB AE -3.2M (đều 1W-2L — mẫu nhỏ, đầu tuần).

---

## PHẦN 3 — THAY ĐỔI KỸ THUẬT + AN TOÀN

| Mục | Chi tiết |
|---|---|
| Code | `_v10773_three_layer_scoreboard.py`: thêm `_vs_lane()` + khối `vs_lane_ae` per region (READ-ONLY SELECT, không bảng mới) · `monitoring.html`: render khối đối chứng trong panel sẵn (auto-refresh 60s sẵn, API `require_admin` + `no-store` sẵn) |
| Sandbox-first | Test module mới trên DB thật READ-ONLY tại `/root/sandbox_v10785/v10787_mod/` PASS (3 miền đủ keys, số khớp probe) TRƯỚC khi deploy |
| Deploy | 14:01 08/07 — ngoài cửa sổ live (MN sáng xong 04:xx; T-10 MN 15:45 chưa tới) · restart `lottery.service` · smoke health=200 · admin unauth=401 · monitoring=401 |
| Hash 4 bảng | pre = post IDENTICAL: predictions 9538 `0e39714e` · final_bundles 391 `cde8625c` · lottery_results 15029 `d0564050` · model_daily_eval 9362 `59b55081` |
| Rollback | `/root/backups/v10787_pre_20260708_140006/` (2 file) |
| Nguyên tắc | DIAGNOSTIC-ONLY — /du-doan, bundle writer, selector official KHÔNG đổi; đề xuất đổi method lock luôn qua chữ ký anh |
| Probes (local, READ-ONLY) | `_v10787_2day_audit.py` · `_v10787_three_surface_gap.py` · `_v10787_cross_pair_pnl.py` · `_v10787_lock_probe.py` · `_v10787_selector_probe.py` · `_v10787_mb_selector.py` |

## PHẦN 4 — CHỜ KÝ (không mới trong phiên này)

- **K8 gemma MB 429** (từ V10785): K8a slim-context riêng gemma MB (đề xuất) / K8b nâng tier Google / K8c chấp nhận không phủ.
- K1–K7: bảng trong `BAO_CAO_TONG_V10785.md`.
- Nhắc lịch: **CP-L5 (LEAN_HARVEST) hard deadline 2026-07-09 — ngày mai.**
