# PHÂN TÍCH SO SÁNH DDXS_Full vs LOTT — Ngày 03/06/2026 (T4)

**Mục đích:** Tổng hợp đầy đủ điểm mạnh/yếu cả 2 hệ thống. Đề xuất fix cho DDXS_Full thử nghiệm trước.

---

## 1. BẢNG TỔNG HỢP KẾT QUẢ 03/06/2026

### 1.1 Kết quả thực tế

| Miền | Đài | DB tail | G8 tail | Tổng tails |
|------|-----|---------|---------|------------|
| MN | Đồng Nai | 86 | 40 | 18 |
| MN | Cần Thơ | 81 | 48 | 18 |
| MN | Sóc Trăng | 57 | 57 | 18 |
| MT | Đà Nẵng | 75 | 95 | 18 |
| MT | Khánh Hòa | 14 | 71 | 18 |
| MB | Bắc Ninh | 36 | (ko G8) | 27 |

### 1.2 So sánh dự đoán

| | DDXS_Full | | | LOTT | | |
|---|---|---|---|---|---|---|
| **Miền** | **BT** | **P1** | **P2** | **BT** | **SP1** | **SP2** |
| MN | 19 MISS | 08 HIT(2x) | 48 HIT(2x) | 99 MISS | 94 MISS | 25 HIT(4x!) |
| MT | 19 MISS | 58 HIT(1x) | 28 MISS | 59 HIT(1x) | 95 HIT(1x) | 75 HIT(3x) |
| MB | 52 HIT(1x) | 66 HIT(1x) | 35 HIT(1x) | 87 MISS | 54 MISS | 52 HIT(1x) |

### 1.3 Tóm tắt score

| Metric | DDXS_Full | LOTT |
|--------|-----------|------|
| BT hit | 1/3 (MB) | 1/3 (MT) |
| Tổng số hit | 5/9 | 4/9 |
| Số lần xuất hiện | 7x | 9x |
| Perfect miền | MB (3/3) | MT (3/3 + Xiên2+3 WIN) |
| Worst miền | MT (0/3 BT, 1/3 tổng) | MB (0/3 BT, 1/3 tổng) |

**Nhận xét:** Cả 2 hệ thống đều 1/3 BT. DDXS mạnh MB, LOTT mạnh MT. Mỗi bên có 1 điểm mù rõ ràng.

---

## 2. PHÂN TÍCH DDXS_Full — TẠI SAO THUA MN VÀ MT

### 2.1 MT: 0/3 BT, chỉ P1=58 hit — TỆ NHẤT

**Dự đoán:** BT=19, P1=58, P2=28
**Thực tế Đà Nẵng:** 95 87 35 18 17 22 23 46 11 58 35 81 75 68 59 50 46 75
**Thực tế Khánh Hòa:** 71 87 11 57 49 94 54 68 38 93 06 14 06 52 60 89 60 14

**Root cause 1 — Không có real-time Markov cascade:**
- MN Sóc Trăng xổ DB=57 lúc 16:15. Markov chain 57→59 (xuất hiện 3x trong 30d) là signal cực mạnh cho MT.
- LOTT dùng Markov cascade: 57→59 HIT (Đà Nẵng G3_2=85559), 57→75 HIT (Đà Nẵng DB=725175).
- DDXS_Full: 8 ML models train trên historical data (30-60 ngày). Khi MN xổ xong, cascade re-predict chỉ gọi lại AI models với source_data mới — nhưng AI models không có Markov transition table built-in. Cross-region module (cross_region.py) chỉ check momentum/frequency, KHÔNG trace Markov chain cụ thể "57 → ?" .

**Root cause 2 — Cross-region chỉ là boost, không đủ mạnh:**
- Rule MT-01 (MB G7#2 → MT D+1): MB G7#2 hôm qua = 59. Rule cho ra candidate 59.
- Ở DDXS_Full: cross-region boost tối đa +0.35 (active mode, READY_STRONG). Nếu 59 không nằm trong top candidates từ ML/Stat, boost +0.35 không đủ đẩy lên top.
- Ở LOTT: 59 từ MT-01 rule được weight 3-4 + Markov confirm = BT candidate trực tiếp.

**Root cause 3 — T4 là non-hot day cho MT:**
- V10667 data: MT T4 có 0 BH-pass rules, 0 MODERATE+ rules.
- Khi V10667 trống, DDXS phải dựa hoàn toàn vào ML ensemble → ML chọn 19 (có thể dựa trên freq pattern) → sai.

### 2.2 MN: BT=19 MISS, P1=08 HIT, P2=48 HIT

**Dự đoán DDXS:** BT=19, P1=08, P2=48
**Dự đoán LOTT:** BT=99, SP1=94, SP2=25

**DDXS weakness:**
- BT=19 MISS hoàn toàn (không có trong bất kỳ đài nào).
- Tuy nhiên P1=08 HIT(2x: Đồng Nai + Sóc Trăng) và P2=48 HIT(2x: Cần Thơ) — ML ensemble chọn SP tốt hơn LOTT.
- DDXS không dùng V10667 rules database → bỏ lỡ signal 25 (V10667 MB:G6#2:D-1 MODERATE).

**LOTT weakness (cũng thua MN):**
- BT=99 MISS: Nguồn từ mined rule (Ben Tre db→g8 pattern) + freq 8x/22d. T4 không phải hot day MN → mined+freq không đủ tin cậy.
- SP1=94 MISS: Không có trong tails nào.
- SP2=25 HIT(4x cả 3 đài) nhưng chỉ là SP2, không phải BT.
- Nếu ranking đúng, 25 nên là BT (V10667 MODERATE, cross-region confirmed).

### 2.3 MB: DDXS 3/3 WIN — Tại sao?

**DDXS dự đoán:** BT=52, P1=66, P2=35
**Thực tế Bắc Ninh:** 36 66 30 79 70 58 13 38 35 69 23 22 51 98 76 95 71 98 48 18 74 13 55 52 90 77 34

- BT=52: G7#1 = 52. 8 models consensus → ML (freq + trend) + AI đều chỉ vào 52.
- P1=66: G1 tail = 66. Freq strong signal.
- P2=35: G3#5 = 08835, tail = 35. Nằm trong top freq candidates.
- Cross: 52, 66, 35, 23 — tất cả đều HIT. Cross-region boost confirm.

**Bí quyết DDXS ở MB:** Multi-model consensus trên frequency-based candidates. MB có 27 tails → baseline 23.8% cho mỗi số → freq-based approach có xác suất hit cao hơn. DDXS tận dụng điều này bằng ensemble của 8 models.

---

## 3. PHÂN TÍCH LOTT — TẠI SAO THUA MN VÀ MB

### 3.1 MN: BT=99 MISS, SP1=94 MISS — CHỈ SP2=25 CỨU

**Root cause 1 — Mined rules dominance on non-hot day:**
- BT=99 từ Tầng 2 mined rule (Ben Tre db=66 → g8=99, tier READY_WITH_CAUTION) + Tầng 3 freq 8x.
- T4 MN có 0 BH-pass rules (hot day = T7 với 86 BH-pass). Non-hot day → tín hiệu cross-region yếu.
- Mined rule READY_WITH_CAUTION + freq ĐƠN THUẦN → không đủ tin cậy.
- V10667 MODERATE rule cho ra 25 (MB:G6#2:D-1), nhưng MODERATE weight=3 < mined+freq weight=5 → 25 bị đẩy xuống SP2.

**Root cause 2 — Ranking sai ưu tiên:**
- 25 có V10667 MODERATE (confirmed cross-region, weight 3) + thực tế HIT 4 lần ở CẢ 3 đài.
- 99 chỉ có mined (CAUTION tier) + freq — KHÔNG có cross-region confirmation.
- Hệ thống đánh giá mined+freq (weight 5) > V10667 MODERATE (weight 3) → sai. Vì ngày non-hot, V10667 dù chỉ MODERATE vẫn đáng tin hơn mined alone.

**Root cause 3 — Không có Hot/Cold filter:**
- 99 freq 8x/22d nghe "hot" nhưng thiếu trend analysis sâu (MA7 vs MA14, day-of-week pattern).
- DDXS có hot/cold post-filter loại bỏ số không phù hợp → LOTT không có.

### 3.2 MT: 3/3 PERFECT tại Đà Nẵng — Nhưng Khánh Hòa 0/3

**Đây là điểm mù ẩn:**
- 59, 95, 75 ALL HIT tại Đà Nẵng. PERFECT.
- Khánh Hòa: 59 MISS, 95 MISS, 75 MISS → 0/3.
- Tổng MT: vẫn tính WIN vì BT/SP chỉ cần trúng bất kỳ đài. Nhưng dự đoán hoàn toàn station-agnostic.

**Điều đáng chú ý tại Khánh Hòa:**
- Khánh Hòa có: 87 (LOTT MB BT!), 94 (LOTT MN SP1!), 54 (LOTT MB SP1!), 52 (DDXS MB BT!), 14
- Cross-region leakage rõ ràng: các số được predict cho miền khác lại xuất hiện tại Khánh Hòa.

**Bài học:** Dự đoán station-agnostic may mắn trúng ở 1 đài, nhưng miss hoàn toàn đài còn lại. Cần cân nhắc station-specific prediction cho MT/MN (nhiều đài).

### 3.3 MB: BT=87 MISS, SP1=54 MISS — Single-rule bias

**Đã phân tích ở phần trước. Tóm tắt:**
- BT=87 từ V10667 BH-pass rule (MB:G7#4:D-1, weight 5) NHƯNG freq chỉ 4x/22d (< avg 5.9).
- 52 (SP2, HIT G7#1) có V10667 STRONG + mined confirm + freq 6x — đáng lẽ phải là BT.
- Single BH-pass rule without freq confirmation → over-confidence → miss.

---

## 4. CROSS-REGION LEAKAGE — HIỆN TƯỢNG ĐÁNG CHÚ Ý

| Số | Predict cho | Xuất hiện thực tế ở |
|----|-------------|---------------------|
| 87 | LOTT MB BT | MT Đà Nẵng (1x), MT Khánh Hòa (1x) — KHÔNG có ở MB! |
| 52 | LOTT MB SP2 / DDXS MB BT | MN Cần Thơ (1x), MT Khánh Hòa (1x), MB Bắc Ninh (1x) |
| 94 | LOTT MN SP1 | MT Khánh Hòa (1x) — MISS ở MN! |
| 54 | LOTT MB SP1 | MN Cần Thơ (1x), MN Sóc Trăng (1x), MT Khánh Hòa (1x) — MISS ở MB! |
| 25 | LOTT MN SP2 | MN cả 3 đài (4x) — chỉ hit MN |

**Insight:** Các số 87, 52, 54 được predict cho 1 miền nhưng xuất hiện chủ yếu ở miền khác. Chỉ 25 xuất hiện đúng miền target. Điều này cho thấy cross-region signal thật nhưng attribution miền có thể sai.

---

## 5. ĐIỂM MẠNH VÀ ĐIỂM YẾU MỖI HỆ THỐNG

### 5.1 DDXS_Full

| Điểm mạnh | Chi tiết |
|------------|----------|
| Multi-model consensus | 8 models vote → giảm single-rule bias, chọn số có agreement cao |
| Dynamic weight learning | knowledge_weights.py tự điều chỉnh theo tuần, weight_optimizer.py tối ưu |
| Hot/Cold post-filter | Loại bỏ số COLD extreme sau scoring |
| MB prediction mạnh | 27 tails + freq-based ensemble → hit rate cao |
| Auto-calibrate | Threshold tự điều chỉnh theo performance gần nhất |

| Điểm yếu | Chi tiết | Severity |
|-----------|----------|----------|
| Không có Markov cascade real-time | ML models không trace "57→?" khi MN xổ xong. AI models nhận source_data nhưng không có Markov table | **CRITICAL** |
| Cross-region boost quá nhỏ | Max +0.35 không đủ override ML consensus sai | **HIGH** |
| V10667 rules database không có | Bỏ lỡ BH-pass signals (87 cho MB, 25 cho MN) | **MEDIUM** |
| MT non-hot day blind | T4 MT không có signal → ML chọn sai | **HIGH** |
| Station-agnostic prediction | Không phân biệt đài nào khả năng hit cao hơn | **LOW** |

### 5.2 LOTT

| Điểm mạnh | Chi tiết |
|------------|----------|
| Real-time Markov cascade | MN xổ → trace Markov → predict MT/MB. Cực mạnh cho MT | 
| Cross-region MT-01 rule | 3 ngày WIN liên tiếp, signal thật | 
| V10667 rules database | 268 rules, BH-pass, forward audit 90 ngày |
| Cascade re-predict | 16:35, 17:35, 18:35 re-predict với data mới |

| Điểm yếu | Chi tiết | Severity |
|-----------|----------|----------|
| Single-rule BT dominance | BH-pass weight 5 override mọi thứ dù freq thấp | **CRITICAL** |
| Không multi-model | 1 Claude manual → susceptible to cognitive bias | **HIGH** |
| Mined rules over-confidence non-hot | T4 MN mined+freq → BT=99 MISS | **HIGH** |
| Không có Hot/Cold filter | Số COLD (gap cao) vẫn có thể thành BT | **MEDIUM** |
| Station-agnostic | MT win Đà Nẵng nhưng miss Khánh Hòa hoàn toàn | **LOW** |

---

## 6. ĐỀ XUẤT CỤ THỂ CHO DDXS_Full

### Fix 1 — CRITICAL: Thêm Markov Cascade Module

**Vấn đề:** Khi MN xổ lúc 16:15, DDXS re-predict MT+MB nhưng chỉ gọi lại AI models với source_data mới. AI không biết trace "57 → ?" systematically.

**Giải pháp:**
```
1. Build Markov transition table từ 30-60 ngày data:
   - Cho mỗi số X xuất hiện hôm nay (DB tail, G8 tail)
   - Đếm: ngày mai số nào xuất hiện? (top-5 transitions)
   - Lưu: markov[region_source][X] = {Y: count, Z: count, ...}

2. Khi MN xổ xong → extract DB tail, G8 tail
   → Tra markov[MN][57] = {59: 3x, 75: 2x, 14: 3x, ...}
   → Boost candidates MT: 59 += 2.0, 75 += 1.5 (scale theo count)

3. Integrate vào cascade re-predict:
   - 16:35: MN data → Markov boost cho MT+MB candidates
   - 17:35: MN+MT data → Markov boost cho MB candidates
```

**Impact estimate:** MT hit rate +15-20% dựa trên LOTT data (Markov 57→59 + 57→75 đều HIT).

### Fix 2 — HIGH: Tăng Cross-Region Boost Power

**Vấn đề:** Cross-region boost tối đa +0.35 quá nhỏ so với ML score range (0.5-5.0).

**Giải pháp:**
```
Thêm "Override mode" cho cross-region khi:
  - Rule có streak >= 3 ngày WIN liên tiếp (MT-01 đang 3 streak)
  - Rule + Markov confirm cùng 1 số
  → Boost = max(0.50, score_of_top1 × 0.3) — đủ đẩy vào top-3

Hoặc đơn giản hơn:
  - BOOST_TABLE active READY_STRONG DIRECT_TOP2_CORE: 0.35 → 0.60
  - Thêm Markov convergence bonus: +0.25 khi rule + Markov cùng chỉ 1 số
```

### Fix 3 — HIGH: Thêm Real-Time V10667 Rules Lookup

**Vấn đề:** DDXS dùng mined_rules (rule_engine.py) nhưng không có V10667 BH-pass rules database.

**Giải pháp:**
```
1. Import V10667_RULES_PER_REGION_RAW.json (268 BH-pass rules)
2. Mỗi ngày: tra rules cho target_region × target_weekday
3. Extract candidate numbers từ source data (LAST2 transform)
4. Boost vào scoring pipeline:
   - BH-pass: +0.40 (highest tier)
   - STRONG (p<0.01): +0.25
   - MODERATE (p<0.05): +0.15
5. Đặc biệt: Hot days (MN T7=86 rules, MT T5=85, MT T7=90) → boost ×1.5
```

**Note:** V10667 rules đã có sẵn tại `D:\Lottery_AI_Test\web\backend\data\lott\V10667_RULES_PER_REGION_RAW.json`. Có thể copy và integrate.

### Fix 4 — MEDIUM: Non-Hot Day Fallback Strategy

**Vấn đề:** T4 MT có 0 BH-pass rules → ML ensemble không có guidance → chọn sai.

**Giải pháp:**
```
Khi V10667 BH-pass = 0 cho target:
  1. Tăng weight cho Markov cascade (nếu có fresh data): ×1.5
  2. Tăng weight cho mined_rules READY_STRONG: ×1.25
  3. Giảm confidence output: max 60% (thay vì 80%)
  4. Nếu không có signal mạnh nào → output SKIP thay vì guess
```

### Fix 5 — MEDIUM: Frequency Threshold cho BT

**Vấn đề:** DDXS chọn BT=19 (MN) — 19 có thể từ ML nhưng không verify frequency.

**Giải pháp:**
```
BT candidate PHẢI có freq >= avg_region:
  - MN avg ~5x/30d mỗi số (với 54 tails/ngày × 3 đài)
  - MT avg ~3x/30d
  - MB avg ~8x/30d (27 tails)

Nếu BT candidate freq < avg → downgrade xuống SP, chọn candidate tiếp theo.
```

---

## 7. NGÀY 03/06 NẾU CẢ HAI HỆ THỐNG ÁP DỤNG HYBRID

| Miền | Hybrid approach | BT dự kiến | Kết quả |
|------|----------------|------------|---------|
| MN | Stat top (freq+trend) → V10667 25 confirm → BT=25 | 25 | HIT (4x cả 3 đài) |
| MT | Markov 57→59 + MT-01 rule confirm → BT=59 | 59 | HIT (Đà Nẵng) |
| MB | Freq+trend → 52 top. BH-pass 87 chỉ boost (freq<avg) → BT=52 | 52 | HIT (G7#1) |

**BT 3/3 WIN** thay vì cả 2 hệ thống chỉ 1/3.

---

## 8. TÓM TẮT BÀI HỌC

1. **Multi-model consensus tốt cho base candidates** (DDXS mạnh) nhưng **thiếu real-time signals** → miss MT.
2. **Markov cascade cực mạnh cho cascade prediction** (LOTT mạnh) nhưng **single-rule BT bias** → miss MB.
3. **V10667 rules có edge thật** nhưng phải dùng như **boost/confirm, không phải primary** khi freq thấp.
4. **Non-hot days nguy hiểm**: T4 MN/MT đều non-hot → cả 2 hệ thống thua BT ở miền mình yếu.
5. **Cross-region leakage**: Số predict cho miền A thường xuất hiện ở miền B → cần rethink attribution.
6. **Giải pháp tối ưu = Hybrid**: freq-based base + Markov cascade boost + V10667 confirm + multi-source BT requirement.

---

*Report generated: 03/06/2026 19:30 VN | Data source: minhngoc.net.vn + xskt.com.vn*
