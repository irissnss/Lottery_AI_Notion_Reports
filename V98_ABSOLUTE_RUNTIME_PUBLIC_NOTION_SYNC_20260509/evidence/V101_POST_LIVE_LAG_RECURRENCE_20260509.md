# V101 Post-Live Lag Recurrence Forensic — 2026-05-09

**Question:** Did losing numbers from 2026-05-08 appear again on 2026-05-09 in MN/MT/MB?

**DB source:** live-synced from VPS via `artifacts\live_sync\20260509_211836\manifest.json`

## 1. Actual Result Sets

| Date | Region | Strict ĐB tails | G8 tails | Any-prize 2D count | Any-prize 2D tails |
|---|---|---|---|---:|---|
| 2026-05-08 | MN | ['21', '34', '52'] | ['39', '61', '68'] | 35 | ['05', '07', '10', '11', '15', '17', '21', '22', '23', '26', '27', '30', '32', '33', '34', '35', '38', '39', '44', '47', '52', '59', '61', '68', '72', '74', '75', '77', '83', '86', '87', '89', '91', '98', '99'] |
| 2026-05-08 | MT | ['25', '82'] | ['10', '70'] | 31 | ['01', '10', '12', '18', '19', '24', '25', '27', '29', '35', '36', '41', '44', '46', '53', '55', '56', '66', '67', '70', '71', '72', '74', '78', '82', '83', '85', '86', '90', '97', '98'] |
| 2026-05-08 | MB | ['47'] | ['62'] | 25 | ['05', '11', '13', '16', '25', '42', '44', '46', '47', '52', '56', '60', '61', '62', '71', '72', '74', '77', '79', '82', '84', '85', '87', '93', '94'] |
| 2026-05-09 | MN | ['69', '78', '89', '96'] | ['13', '15', '47', '64'] | 53 | ['00', '01', '03', '04', '08', '10', '13', '15', '16', '17', '26', '27', '29', '31', '32', '33', '34', '35', '36', '42', '43', '47', '48', '49', '51', '55', '57', '59', '64', '65', '66', '67', '69', '70', '71', '72', '73', '74', '75', '78', '79', '81', '83', '84', '86', '87', '88', '89', '90', '92', '93', '94', '96'] |
| 2026-05-09 | MT | ['27', '75', '99'] | ['09', '54'] | 43 | ['00', '01', '02', '03', '05', '09', '10', '11', '14', '16', '19', '20', '22', '24', '25', '27', '31', '34', '35', '38', '40', '41', '43', '49', '54', '55', '57', '58', '59', '61', '69', '72', '75', '78', '79', '84', '85', '87', '88', '90', '94', '95', '99'] |
| 2026-05-09 | MB | ['92'] | ['05'] | 24 | ['05', '10', '13', '17', '23', '37', '42', '45', '47', '50', '52', '53', '63', '64', '65', '66', '67', '79', '81', '83', '86', '92', '95', '96'] |

## 2. D-1 Lost → D Hit, Same Region

Definitions:
- `lost_strict_y`: tail was not in 2026-05-08 strict ĐB tail.
- `lost_any_y`: tail was not in 2026-05-08 any-prize set.
- `hit_strict_t`: tail is in 2026-05-09 strict ĐB tail.
- `hit_any_t`: tail is in 2026-05-09 any-prize set.

| Region | Tail | Lost strict yesterday | Lost any yesterday | Hit strict today | Hit any today | Yesterday sources | Today sources | Verdict |
|---|---|---:|---:|---:|---:|---|---|---|
| MN | **13** | 1 | 1 | 0 | 1 | MODEL_MAIN=10, OFFICIAL_BT=1, OFFICIAL_LO2=1, TEST_BT=6, TEST_LO2=7, V70=1 | ex: OFFICIAL_BT:final_bundles.bach_thu; OFFICIAL_LO2:final_bundles.lo2; TEST_BT:MN_ADAPTIVE_BUDGET_SELECTOR_V1; TEST_LO2:MN_ADAPTIVE_BUDGET_SELECTOR_V1; TEST_BT:MN_OFFICIAL_BASELINE_CONTROL; TEST_LO2:MN_OFFICIAL_BASELINE_CONTROL; TEST_BT:MN_STRENGTH_WEIGHTED_V52_5_2; TEST_LO2:MN_STRENGTH_WEIGHTED_V52_5_2 | TEST_BT=2, TEST_LO2=2, V101_MN_D1_D2=1, V67=1, V70=1, V73=1 | ex: TEST_BT:MN_ADAPTIVE_EXPLOIT_V1; TEST_LO2:MN_ADAPTIVE_EXPLOIT_V1; TEST_BT:MN_HYBRID_V1; TEST_LO2:MN_HYBRID_V1; V67:adaptive_exploit_v67_candidate_trace:score=2.2763; V70:consensus_v1_trace:agreement_count=2; V73:hybrid_v1_trace:confidence_tier=AURA; V101_MN_D1_D2:rank=1,score=8.74 | CLEAN_ANY_PRIZE_RECURRENCE |
| MN | **32** | 1 | 0 | 0 | 1 | MODEL_MAIN=1 | ex: MODEL_MAIN:lstm[1] | MODEL_MAIN=1 | ex: MODEL_MAIN:lstm[1] | STRICT_LOSS_TO_DIAGNOSTIC_HIT |
| MN | **35** | 1 | 0 | 0 | 1 | MODEL_MAIN=1 | ex: MODEL_MAIN:qwen3-max-thinking[1] |  | STRICT_LOSS_TO_DIAGNOSTIC_HIT |
| MN | **43** | 1 | 1 | 0 | 1 | MODEL_MAIN=3 | ex: MODEL_MAIN:smart-ensemble[0]; MODEL_MAIN:smart-ml[0]; MODEL_MAIN:meta-learning[1] | V67=1 | ex: V67:adaptive_exploit_v67_candidate_trace:score=1.1256 | CLEAN_ANY_PRIZE_RECURRENCE |
| MN | **51** | 1 | 1 | 0 | 1 | MODEL_MAIN=3 | ex: MODEL_MAIN:glm-5.1[0]; MODEL_MAIN:gemini-3.1-pro[1]; MODEL_MAIN:gemma-4-31b[0] |  | CLEAN_ANY_PRIZE_RECURRENCE |
| MN | **70** | 1 | 1 | 0 | 1 | MODEL_MAIN=4, OFFICIAL_LO2=1, TEST_LO2=6 | ex: OFFICIAL_LO2:final_bundles.lo2; TEST_LO2:MN_OFFICIAL_BASELINE_CONTROL; TEST_LO2:MN_STRENGTH_WEIGHTED_V52_5_2; TEST_LO2:MN_AI_CHAIN_PRESERVATION_V1; TEST_LO2:MN_SPECIALIST_ROSTER_V1; TEST_LO2:MN_PRIOR_REGION_CONTEXT_SAFE_V1; TEST_LO2:MN_NO_TOKEN_HERD_REDUCTION_V1; MODEL_MAIN:smart-ensemble[1] |  | CLEAN_ANY_PRIZE_RECURRENCE |
| MN | **79** | 1 | 1 | 0 | 1 | MODEL_MAIN=4 | ex: MODEL_MAIN:gpt-5-mini[1]; MODEL_MAIN:combo-super[0]; MODEL_MAIN:gpt-oss-120b[1]; MODEL_MAIN:qwen3.6-plus[1] | MODEL_MAIN=1, V101_MN_D1_D2=1, V67=1 | ex: V67:adaptive_exploit_v67_candidate_trace:score=1.0679; MODEL_MAIN:deepseek-v4-pro[1]; V101_MN_D1_D2:rank=2,score=7.76 | CLEAN_ANY_PRIZE_RECURRENCE |
| MN | **81** | 1 | 1 | 0 | 1 | MODEL_MAIN=1 | ex: MODEL_MAIN:random-forest[0] |  | CLEAN_ANY_PRIZE_RECURRENCE |
| MN | **93** | 1 | 1 | 0 | 1 | MODEL_MAIN=8, TEST_LO2=1 | ex: TEST_LO2:MN_ADAPTIVE_BUDGET_SELECTOR_V1; MODEL_MAIN:gpt-5-mini[0]; MODEL_MAIN:claude-opus-4-20250514[0]; MODEL_MAIN:grok-4.20-multi-agent[0]; MODEL_MAIN:qwen3-coder[0]; MODEL_MAIN:gpt-oss-120b[0]; MODEL_MAIN:gpt-5.5[0]; MODEL_MAIN:deepseek-v4-flash[1] | MODEL_MAIN=1, V101_MN_D1_D2=1, V67=1 | ex: V67:adaptive_exploit_v67_candidate_trace:score=1.1739; MODEL_MAIN:gemini-2.5-flash[1]; V101_MN_D1_D2:rank=5,score=6.79 | CLEAN_ANY_PRIZE_RECURRENCE |
| MN | **94** | 1 | 1 | 0 | 1 | MODEL_MAIN=4, V67=1, V70=1, V73=1 | ex: V67:adaptive_exploit_v67_candidate_trace:score=3.6098; V70:consensus_v1_trace:agreement_count=2; V73:hybrid_v1_trace:confidence_tier=AURA; MODEL_MAIN:deepseek-v4-pro[0]; MODEL_MAIN:kimi-k2.5[0]; MODEL_MAIN:gemini-3-flash[0]; MODEL_MAIN:gemini-3.1-pro[0] |  | CLEAN_ANY_PRIZE_RECURRENCE |
| MT | **34** | 1 | 1 | 0 | 1 | MODEL_MAIN=1 | ex: MODEL_MAIN:lstm[0] | MODEL_MAIN=2 | ex: MODEL_MAIN:gpt-oss-120b[1]; MODEL_MAIN:deepseek-v4-pro[1] | CLEAN_ANY_PRIZE_RECURRENCE |
| MT | **40** | 1 | 1 | 0 | 1 | V67=1 | ex: V67:adaptive_exploit_v67_candidate_trace:score=1.0658 |  | CLEAN_ANY_PRIZE_RECURRENCE |
| MT | **58** | 1 | 1 | 0 | 1 | MODEL_MAIN=2 | ex: MODEL_MAIN:glm-5.1[1]; MODEL_MAIN:gpt-5.5[1] |  | CLEAN_ANY_PRIZE_RECURRENCE |
| MT | **61** | 1 | 1 | 0 | 1 | MODEL_MAIN=6, OFFICIAL_BT=1, OFFICIAL_LO2=1, TEST_BT=5, TEST_LO2=7, V70=1, V73=1 | ex: OFFICIAL_BT:final_bundles.bach_thu; OFFICIAL_LO2:final_bundles.lo2; TEST_BT:MT_ADAPTIVE_BUDGET_SELECTOR_V1; TEST_LO2:MT_ADAPTIVE_BUDGET_SELECTOR_V1; TEST_BT:MT_OFFICIAL_BASELINE_CONTROL; TEST_LO2:MT_OFFICIAL_BASELINE_CONTROL; TEST_BT:MT_STRENGTH_WEIGHTED_V52_5_2; TEST_LO2:MT_STRENGTH_WEIGHTED_V52_5_2 | MODEL_MAIN=1, V67=1 | ex: V67:adaptive_exploit_v67_candidate_trace:score=1.107; MODEL_MAIN:claude-opus-4-20250514[1] | CLEAN_ANY_PRIZE_RECURRENCE |
| MT | **69** | 1 | 1 | 0 | 1 | MODEL_MAIN=1 | ex: MODEL_MAIN:combo-super[0] |  | CLEAN_ANY_PRIZE_RECURRENCE |
| MT | **79** | 1 | 1 | 0 | 1 | MODEL_MAIN=17 | ex: MODEL_MAIN:gpt-5-mini[0]; MODEL_MAIN:gemini-2.5-flash[0]; MODEL_MAIN:gemini-2.5-pro[0]; MODEL_MAIN:gpt-5.4[0]; MODEL_MAIN:combo-super[1]; MODEL_MAIN:grok-4.20-multi-agent[1]; MODEL_MAIN:qwen3-coder[0]; MODEL_MAIN:gpt-oss-120b[0] | MODEL_MAIN=1, TEST_BT=2, TEST_LO2=2, V67=1, V70=1 | ex: TEST_BT:MT_ADAPTIVE_EXPLOIT_V1; TEST_LO2:MT_ADAPTIVE_EXPLOIT_V1; TEST_BT:MT_HYBRID_V1; TEST_LO2:MT_HYBRID_V1; V67:adaptive_exploit_v67_candidate_trace:score=3.224; V70:consensus_v1_trace:agreement_count=2; MODEL_MAIN:qwen3.6-plus[1] | CLEAN_ANY_PRIZE_RECURRENCE |
| MT | **87** | 1 | 1 | 0 | 1 | MODEL_MAIN=7, TEST_BT=1, TEST_LO2=1, V70=1 | ex: TEST_BT:MT_PRIOR_REGION_CONTEXT_SAFE_V1; TEST_LO2:MT_PRIOR_REGION_CONTEXT_SAFE_V1; V70:consensus_v1_trace:agreement_count=1; MODEL_MAIN:gpt-5-mini[1]; MODEL_MAIN:gemini-2.5-flash[1]; MODEL_MAIN:deepseek-reasoner[0]; MODEL_MAIN:gpt-5.4[1]; MODEL_MAIN:qwen3-coder[1] | V67=1 | ex: V67:adaptive_exploit_v67_candidate_trace:score=1.0601 | CLEAN_ANY_PRIZE_RECURRENCE |
| MT | **94** | 1 | 1 | 0 | 1 | V67=1, V70=1 | ex: V67:adaptive_exploit_v67_candidate_trace:score=1.2161; V70:consensus_v1_trace:agreement_count=1 |  | CLEAN_ANY_PRIZE_RECURRENCE |
| MB | **37** | 1 | 1 | 0 | 1 | MODEL_MAIN=10, OFFICIAL_BT=1, OFFICIAL_LO2=1, TEST_BT=9, TEST_LO2=14, V67=1, V70=1 | ex: OFFICIAL_BT:final_bundles.bach_thu; OFFICIAL_LO2:final_bundles.lo2; TEST_BT:MB_OFFICIAL_BASELINE_CONTROL; TEST_LO2:MB_OFFICIAL_BASELINE_CONTROL; TEST_BT:MB_COMPOSITE_CHALLENGER_V2; TEST_LO2:MB_COMPOSITE_CHALLENGER_V2; TEST_BT:MB_TIER_AWARE_BUNDLE_SHADOW_V1; TEST_LO2:MB_TIER_AWARE_BUNDLE_SHADOW_V1 | V67=1, V70=1, V73=1 | ex: V67:adaptive_exploit_v67_candidate_trace:score=3.3152; V70:consensus_v1_trace:agreement_count=2; V73:hybrid_v1_trace:confidence_tier=AURA | CLEAN_ANY_PRIZE_RECURRENCE |
| MB | **64** | 1 | 1 | 0 | 1 | MODEL_MAIN=5, OFFICIAL_LO2=1, TEST_BT=1, TEST_LO2=12, V70=1 | ex: OFFICIAL_LO2:final_bundles.lo2; TEST_LO2:MB_OFFICIAL_BASELINE_CONTROL; TEST_LO2:MB_COMPOSITE_CHALLENGER_V2; TEST_LO2:MB_TIER_AWARE_BUNDLE_SHADOW_V1; TEST_LO2:MB_AI_CHAIN_PRESERVATION_V1; TEST_LO2:MB_SPECIALIST_ROSTER_V1; TEST_LO2:MB_NO_TOKEN_HERD_REDUCTION_V1; TEST_BT:MB_ADAPTIVE_BUDGET_SELECTOR_V1 | MODEL_MAIN=2, V67=1 | ex: V67:adaptive_exploit_v67_candidate_trace:score=0.735345; MODEL_MAIN:gemini-2.5-flash[0]; MODEL_MAIN:grok-4.20-multi-agent[0] | CLEAN_ANY_PRIZE_RECURRENCE |
| MB | **79** | 1 | 0 | 0 | 1 | MODEL_MAIN=2 | ex: MODEL_MAIN:meta-learning[1]; MODEL_MAIN:xgboost[1] |  | STRICT_LOSS_TO_DIAGNOSTIC_HIT |
| MB | **86** | 1 | 1 | 0 | 1 | MODEL_MAIN=6 | ex: MODEL_MAIN:deepseek-reasoner[1]; MODEL_MAIN:gemini-2.5-pro[1]; MODEL_MAIN:grok-4.20-multi-agent[0]; MODEL_MAIN:qwen3-coder[0]; MODEL_MAIN:deepseek-v4-pro[1]; MODEL_MAIN:qwen3-max-thinking[0] |  | CLEAN_ANY_PRIZE_RECURRENCE |

## 3. Key Owner-Observed Cases

### MN tail 13 — CLEAN_ANY_PRIZE_RECURRENCE

- Yesterday sources: MODEL_MAIN=10, OFFICIAL_BT=1, OFFICIAL_LO2=1, TEST_BT=6, TEST_LO2=7, V70=1 | ex: OFFICIAL_BT:final_bundles.bach_thu; OFFICIAL_LO2:final_bundles.lo2; TEST_BT:MN_ADAPTIVE_BUDGET_SELECTOR_V1; TEST_LO2:MN_ADAPTIVE_BUDGET_SELECTOR_V1; TEST_BT:MN_OFFICIAL_BASELINE_CONTROL; TEST_LO2:MN_OFFICIAL_BASELINE_CONTROL; TEST_BT:MN_STRENGTH_WEIGHTED_V52_5_2; TEST_LO2:MN_STRENGTH_WEIGHTED_V52_5_2; TEST_BT:MN_AI_CHAIN_PRESERVATION_V1; TEST_LO2:MN_AI_CHAIN_PRESERVATION_V1; TEST_BT:MN_SPECIALIST_ROSTER_V1; TEST_LO2:MN_SPECIALIST_ROSTER_V1
- Today sources: TEST_BT=2, TEST_LO2=2, V101_MN_D1_D2=1, V67=1, V70=1, V73=1 | ex: TEST_BT:MN_ADAPTIVE_EXPLOIT_V1; TEST_LO2:MN_ADAPTIVE_EXPLOIT_V1; TEST_BT:MN_HYBRID_V1; TEST_LO2:MN_HYBRID_V1; V67:adaptive_exploit_v67_candidate_trace:score=2.2763; V70:consensus_v1_trace:agreement_count=2; V73:hybrid_v1_trace:confidence_tier=AURA; V101_MN_D1_D2:rank=1,score=8.74
- 2026-05-08 actual: strict=['21', '34', '52'], any_contains=False
- 2026-05-09 actual: strict=['69', '78', '89', '96'], any_contains=True

### MN tail 79 — CLEAN_ANY_PRIZE_RECURRENCE

- Yesterday sources: MODEL_MAIN=4 | ex: MODEL_MAIN:gpt-5-mini[1]; MODEL_MAIN:combo-super[0]; MODEL_MAIN:gpt-oss-120b[1]; MODEL_MAIN:qwen3.6-plus[1]
- Today sources: MODEL_MAIN=1, V101_MN_D1_D2=1, V67=1 | ex: V67:adaptive_exploit_v67_candidate_trace:score=1.0679; MODEL_MAIN:deepseek-v4-pro[1]; V101_MN_D1_D2:rank=2,score=7.76
- 2026-05-08 actual: strict=['21', '34', '52'], any_contains=False
- 2026-05-09 actual: strict=['69', '78', '89', '96'], any_contains=True

### MT tail 61 — CLEAN_ANY_PRIZE_RECURRENCE

- Yesterday sources: MODEL_MAIN=6, OFFICIAL_BT=1, OFFICIAL_LO2=1, TEST_BT=5, TEST_LO2=7, V70=1, V73=1 | ex: OFFICIAL_BT:final_bundles.bach_thu; OFFICIAL_LO2:final_bundles.lo2; TEST_BT:MT_ADAPTIVE_BUDGET_SELECTOR_V1; TEST_LO2:MT_ADAPTIVE_BUDGET_SELECTOR_V1; TEST_BT:MT_OFFICIAL_BASELINE_CONTROL; TEST_LO2:MT_OFFICIAL_BASELINE_CONTROL; TEST_BT:MT_STRENGTH_WEIGHTED_V52_5_2; TEST_LO2:MT_STRENGTH_WEIGHTED_V52_5_2; TEST_LO2:MT_AI_CHAIN_PRESERVATION_V1; TEST_BT:MT_SPECIALIST_ROSTER_V1; TEST_LO2:MT_SPECIALIST_ROSTER_V1; TEST_LO2:MT_PRIOR_REGION_CONTEXT_SAFE_V1
- Today sources: MODEL_MAIN=1, V67=1 | ex: V67:adaptive_exploit_v67_candidate_trace:score=1.107; MODEL_MAIN:claude-opus-4-20250514[1]
- 2026-05-08 actual: strict=['25', '82'], any_contains=False
- 2026-05-09 actual: strict=['27', '75', '99'], any_contains=True

### MT tail 79 — CLEAN_ANY_PRIZE_RECURRENCE

- Yesterday sources: MODEL_MAIN=17 | ex: MODEL_MAIN:gpt-5-mini[0]; MODEL_MAIN:gemini-2.5-flash[0]; MODEL_MAIN:gemini-2.5-pro[0]; MODEL_MAIN:gpt-5.4[0]; MODEL_MAIN:combo-super[1]; MODEL_MAIN:grok-4.20-multi-agent[1]; MODEL_MAIN:qwen3-coder[0]; MODEL_MAIN:gpt-oss-120b[0]; MODEL_MAIN:kimi-k2.5[0]; MODEL_MAIN:qwen3-max-thinking[0]; MODEL_MAIN:qwen3.6-plus[0]; MODEL_MAIN:gpt-5.5[0]
- Today sources: MODEL_MAIN=1, TEST_BT=2, TEST_LO2=2, V67=1, V70=1 | ex: TEST_BT:MT_ADAPTIVE_EXPLOIT_V1; TEST_LO2:MT_ADAPTIVE_EXPLOIT_V1; TEST_BT:MT_HYBRID_V1; TEST_LO2:MT_HYBRID_V1; V67:adaptive_exploit_v67_candidate_trace:score=3.224; V70:consensus_v1_trace:agreement_count=2; MODEL_MAIN:qwen3.6-plus[1]
- 2026-05-08 actual: strict=['25', '82'], any_contains=False
- 2026-05-09 actual: strict=['27', '75', '99'], any_contains=True

### MB tail 37 — CLEAN_ANY_PRIZE_RECURRENCE

- Yesterday sources: MODEL_MAIN=10, OFFICIAL_BT=1, OFFICIAL_LO2=1, TEST_BT=9, TEST_LO2=14, V67=1, V70=1 | ex: OFFICIAL_BT:final_bundles.bach_thu; OFFICIAL_LO2:final_bundles.lo2; TEST_BT:MB_OFFICIAL_BASELINE_CONTROL; TEST_LO2:MB_OFFICIAL_BASELINE_CONTROL; TEST_BT:MB_COMPOSITE_CHALLENGER_V2; TEST_LO2:MB_COMPOSITE_CHALLENGER_V2; TEST_BT:MB_TIER_AWARE_BUNDLE_SHADOW_V1; TEST_LO2:MB_TIER_AWARE_BUNDLE_SHADOW_V1; TEST_BT:MB_AI_CHAIN_PRESERVATION_V1; TEST_LO2:MB_AI_CHAIN_PRESERVATION_V1; TEST_LO2:MB_SPECIALIST_ROSTER_V1; TEST_LO2:MB_PRIOR_REGION_CONTEXT_SAFE_V1
- Today sources: V67=1, V70=1, V73=1 | ex: V67:adaptive_exploit_v67_candidate_trace:score=3.3152; V70:consensus_v1_trace:agreement_count=2; V73:hybrid_v1_trace:confidence_tier=AURA
- 2026-05-08 actual: strict=['47'], any_contains=False
- 2026-05-09 actual: strict=['92'], any_contains=True

### MB tail 79 — STRICT_LOSS_TO_DIAGNOSTIC_HIT

- Yesterday sources: MODEL_MAIN=2 | ex: MODEL_MAIN:meta-learning[1]; MODEL_MAIN:xgboost[1]
- Today sources: not picked today by tracked sources
- 2026-05-08 actual: strict=['47'], any_contains=True
- 2026-05-09 actual: strict=['92'], any_contains=True


## 4. D-1 Lost → D Hit, Cross-Region

| Source region | Tail | Lost any in source yesterday | Hit today regions (any-prize) | Yesterday source count |
|---|---|---:|---|---:|
| MN | **02** | 1 | ['MT'] | 1 |
| MN | **13** | 1 | ['MN', 'MB'] | 26 |
| MN | **19** | 1 | ['MT'] | 4 |
| MN | **20** | 1 | ['MT'] | 2 |
| MN | **37** | 1 | ['MB'] | 1 |
| MN | **40** | 1 | ['MT'] | 4 |
| MN | **43** | 1 | ['MN', 'MT'] | 3 |
| MN | **51** | 1 | ['MN'] | 3 |
| MN | **53** | 1 | ['MB'] | 1 |
| MN | **70** | 1 | ['MN'] | 11 |
| MN | **79** | 1 | ['MN', 'MT', 'MB'] | 4 |
| MN | **81** | 1 | ['MN', 'MB'] | 1 |
| MN | **93** | 1 | ['MN'] | 9 |
| MN | **94** | 1 | ['MN', 'MT'] | 7 |
| MT | **08** | 1 | ['MN'] | 1 |
| MT | **34** | 1 | ['MN', 'MT'] | 1 |
| MT | **40** | 1 | ['MT'] | 1 |
| MT | **52** | 1 | ['MB'] | 1 |
| MT | **58** | 1 | ['MT'] | 2 |
| MT | **61** | 1 | ['MT'] | 22 |
| MT | **69** | 1 | ['MN', 'MT'] | 1 |
| MT | **73** | 1 | ['MN'] | 1 |
| MT | **79** | 1 | ['MN', 'MT', 'MB'] | 17 |
| MT | **87** | 1 | ['MN', 'MT'] | 10 |
| MT | **89** | 1 | ['MN'] | 6 |
| MT | **94** | 1 | ['MN', 'MT'] | 2 |
| MB | **02** | 1 | ['MT'] | 1 |
| MB | **04** | 1 | ['MN'] | 1 |
| MB | **20** | 1 | ['MT'] | 3 |
| MB | **26** | 1 | ['MN'] | 2 |
| MB | **34** | 1 | ['MN', 'MT'] | 2 |
| MB | **37** | 1 | ['MB'] | 37 |
| MB | **54** | 1 | ['MT'] | 3 |
| MB | **64** | 1 | ['MN', 'MB'] | 20 |
| MB | **78** | 1 | ['MN', 'MT'] | 1 |
| MB | **86** | 1 | ['MN', 'MB'] | 6 |
| MB | **88** | 1 | ['MN', 'MT'] | 1 |

## 5. V101 Context for 2026-05-09 MN

| Rank | Tail | Score | D1 | D2 | Regions | Gan normal | Gan special | V67 | V70 | V73 | Today hit any | Today hit strict |
|---:|---|---:|---:|---:|---|---:|---:|---:|---:|---:|---:|---:|
| 1 | **13** | 8.74 | 1 | 3 | ['MB', 'MN', 'MT'] | 0.8 | 1.2 | 1 | 1 | 1 | 1 | 0 |
| 2 | **79** | 7.76 | 1 | 5 | ['MB', 'MN', 'MT'] | 0.0 | 1.2 | 1 | 0 | 0 | 1 | 0 |
| 3 | **83** | 6.85 | 3 | 2 | ['MB', 'MN', 'MT'] | 0.0 | 1.2 | 0 | 0 | 0 | 1 | 0 |
| 4 | **61** | 6.85 | 3 | 2 | ['MB', 'MN', 'MT'] | 0.0 | 1.2 | 0 | 0 | 0 | 0 | 0 |
| 5 | **93** | 6.79 | 1 | 3 | ['MB', 'MN'] | 0.8 | 1.2 | 1 | 0 | 0 | 1 | 0 |
| 6 | **52** | 6.59 | 2 | 2 | ['MB', 'MN', 'MT'] | 0.8 | 1.2 | 0 | 0 | 0 | 0 | 0 |
| 7 | **44** | 6.45 | 3 | 2 | ['MB', 'MN', 'MT'] | 0.8 | 0.0 | 0 | 0 | 0 | 0 | 0 |
| 8 | **74** | 6.23 | 3 | 0 | ['MB', 'MN', 'MT'] | 0.8 | 1.2 | 0 | 0 | 0 | 1 | 0 |
| 9 | **89** | 6.15 | 2 | 3 | ['MN', 'MT'] | 0.0 | 1.2 | 0 | 0 | 0 | 1 | 1 |
| 10 | **27** | 6.15 | 2 | 3 | ['MN', 'MT'] | 0.0 | 1.2 | 0 | 0 | 0 | 1 | 0 |

## 6. Preliminary Interpretation

1. If a tail is `lost_any_y=1` and `hit_any_t=1`, this is a clean same-region lag recurrence under diagnostic any-prize semantics.
2. If a tail is only `lost_strict_y=1` but was already in yesterday any-prize set, it is not a clean recurrence; it is strict-vs-diagnostic semantic drift.
3. A repeated pattern across MN/MT/MB does not yet prove a data bug. It can be an exploitable delayed-signal mechanism, especially if the same tails also appear in V67/V70/V73/V101.
4. Next safe step: materialize a V102 recurrence tracker that quantifies `lost_any_y -> hit_any_t` and `lost_strict_y -> hit_strict_t` per region/source/method for 30/60/90 days, then feed it into V101 only if above baseline.

**No production change is recommended from this single-day observation.**