# LANE 4 — MB 2026-05-08 '56' Truth Table

**Generated**: 2026-05-09 11:30 VN  
**Question**: V93 claim '14/19 AI picked 56' vs Báo Cáo 15 'act=47' — DB truth?

## A. lottery_results raw rows for MB 2026-05-08

Total rows: 1

### Row id=14738 | station=Hải Phòng | tail_db=47 | tail_g8=62
- created_at: 2026-05-08T18:32:03.654960+07:00
  - Giải Đặc Biệt: `29147`
  - Giải nhất: `10644`
  - Giải nhì: `['52246', '38093']`
  - Giải ba: `['50305', '32171', '15677', '32860', '08316', '19956']`
  - Giải tư: `['7479', '5784', '9374', '6562']`
  - Giải năm: `['3272', '1087', '3487', '3352', '7313', '4385']`
  - Giải sáu: `['661', '311', '582']`
  - Giải bảy: `['62', '25', '42', '94']`

## B. Aggregated tail sets for MB 2026-05-08
- **Special 2D tail (Đặc Biệt)**: `47`
- **All 2D tails (every prize)**: ['05', '11', '13', '16', '25', '42', '44', '46', '47', '52', '56', '60', '61', '62', '71', '72', '74', '77', '79', '82', '84', '85', '87', '93', '94']
- **Total unique 2D tails**: 25
- **All 3D tails**: ['087', '093', '147', '171', '246', '272', '305', '311', '313', '316', '352', '374', '385', '479', '487', '562', '582', '644', '661', '677', '784', '860', '956']
- **Is '56' in 2D set?**: YES ✅
- **Is '47' in 2D set?**: YES ✅
- **Is '37' in 2D set?**: NO ❌
- **Is special '56'?**: NO (special=47)

## C. Production predictions for MB target_date=2026-05-08
Total predictions: 27
- Models picking 56: **14/27**
  - claude-opus-4-20250514(['56', '02'])
  - claude-sonnet-4-6(['56'])
  - deepseek-v4-flash(['56', '39'])
  - gemini-2.5-pro(['56', '86'])
  - gemini-3-flash(['37', '56'])
  - gemini-3.1-pro(['56', '39'])
  - glm-5.1(['37', '56'])
  - gpt-5-mini(['37', '56'])
  - gpt-5.5(['56', '37'])
  - gpt-oss-120b(['56', '25'])
  - grok-4.20-multi-agent(['86', '56'])
  - kimi-k2.5(['37', '56'])
  - qwen3-max-thinking(['86', '56'])
  - qwen3.6-plus(['56', '37'])
- Models picking 47: **0/27**
- Models picking 37: **10/27**
  - deepseek-reasoner(['37', '86'])
  - deepseek-v4-pro(['37', '86'])
  - gemini-2.5-flash(['37', '26'])
  - gemini-3-flash(['37', '56'])
  - glm-5.1(['37', '56'])
  - gpt-5-mini(['37', '56'])
  - gpt-5.4(['26', '37'])
  - gpt-5.5(['56', '37'])
  - kimi-k2.5(['37', '56'])
  - qwen3.6-plus(['56', '37'])

## D. Production final_bundles for MB 2026-05-08
- bundle_id=284 BT=**37** lo2=["37", "64"] lo3=537 top_score=0.0873 method=weighted_voting_wr
  - bach_thu_status=LOSE lo2_status=LOSE model_count=15

## E. V93 shadow tables for MB 2026-05-08
- v93_wr_gate_filter_audit_shadow: 27 rows for MB 2026-05-08
- v93_verdict_weight_recalibration_shadow: 11 rows for MB 2026-05-08
- v93_mn_save_signal_per_method_shadow: 9 rows for MB 2026-05-08

### V93 WR gate audit detail for MB tails picked
- ⚠ no such column: candidate_tail

## G. Final verdict
- Official BT=37 vs special_2d=47: bundle status from DB row=LOSE
- Bundle BT=37 → status='LOSE'

## H. CONFLICT RESOLUTION — V93 vs Báo Cáo 15

| Claim | Source | Verdict | Evidence |
|---|---|---|---|
| V93 "14/19 AI picked 56" | V93 forensic | ✅ **CONFIRMED** | 14/27 production predictions có '56' trong main_numbers (claude-opus, claude-sonnet, deepseek-v4-flash, gemini-2.5-pro, gemini-3-flash, gemini-3.1-pro, glm-5.1, gpt-5-mini, gpt-5.5, gpt-oss-120b, grok-4.20, kimi-k2.5, qwen3-max, qwen3.6-plus) |
| V93 "56 in actual MB 2026-05-08" | V93 forensic | ✅ **CONFIRMED (multi-prize semantic)** | Giải ba 19956 → 2D tail '56' ∈ all-prize tail set. 56 KHÔNG phải special tail. |
| Báo Cáo 15 "actual=47" | morning audit (sáng nay) | ✅ **CONFIRMED (special-prize semantic)** | Giải Đặc Biệt 29147 → 2D tail = 47. Production scoring dùng tail_db=47. |
| Production bundle BT=37 LOSE | DB final_bundles row 284 | ✅ **CONFIRMED** | bach_thu_status='LOSE' (37 ≠ 47 special, 37 ∉ all-prize set) |

### → KẾT LUẬN: KHÔNG CÓ CONFLICT, là **EVALUATOR_SEMANTIC_DIFFERENCE**

Hai semantic đều **valid** và đều **được dùng trong thực tế**:

**Semantic 1 — `BT_DAC_BIET_STRICT`** (production hiện tại):
- BT chỉ trúng nếu khớp 2D tail của Giải Đặc Biệt (1 số duy nhất per region per day)
- Production `final_bundles.bach_thu_status` dùng cái này
- → MB 2026-05-08: BT=37 LOSE vì ĐB=47

**Semantic 2 — `BT_BAT_KY_GIAI`** (V93 forensic + lottery thực tế):
- BT trúng nếu xuất hiện trong **bất kỳ giải nào** (27 prize tails per MB)
- V93 forensic dùng cái này → MB 56 "smoking gun"
- → MB 2026-05-08: nếu BT=56 thì WIN (vì giải ba có 19956)

### Implication

→ **V93 "bundle conversion lost 56" claim** vẫn VALID NẾU owner score theo semantic 2.

→ Nhưng production scoring vẫn theo semantic 1, nên:
   - V93 "smoking gun" applies trong bối cảnh **alternative scoring rule**
   - Production scoring CHƯA "miss" gì theo current rule (BT=37 LOSE đúng theo strict ĐB)
   - Bundle conversion failure analysis chỉ valid nếu owner muốn shift scoring semantic

### → NEW FU-V99-BT-SCORING-DEBATE (P0 OWNER_GATE_REQUIRED)

Owner cần quyết định: BT scoring nên là `STRICT_DAC_BIET` (current) hay `ANY_PRIZE_LENIENT` (V93/lottery thực tế)?

- **Hậu quả nếu shift sang ANY_PRIZE**:
  - Hit rate tăng vọt (mỗi MB ~25 unique tails dễ khớp)
  - Bundle scoring phải thay đổi phương pháp
  - Đây là **production scoring change** → 14d/30d backfill replay required
  - User experience thay đổi (BT WIN nghĩa là khác)

- **Hậu quả giữ STRICT_DAC_BIET**:
  - V93 forensic "bundle lost 56" KHÔNG phải bug — chỉ là near-miss alternative
  - FU-173 bundle conversion replay metric cần **2 lanes** (strict + lenient) để compare

→ Em đề xuất giữ STRICT_DAC_BIET cho production. Build LENIENT semantic chỉ trong shadow evaluator (LANE 5).