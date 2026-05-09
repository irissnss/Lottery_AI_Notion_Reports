# V99.2 L5 — Exact Evaluator 14d/30d Scoreboard

**Generated**: 2026-05-09 13:00 VN  
**Source**: `v99_exact_evaluator_results` shadow table  
**Owner directive**: report STRICT separately from DIAGNOSTIC; no promotion claims

## ⚠ KEY INTERPRETATION RULES
- **STRICT** = production scoring (BT khớp Đặc Biệt only). 0% across 14d/30d is **statistical normal** for rare event.
- **DIAGNOSTIC** = signal quality only (BT khớp any 2D tail). Cannot be used as production WIN claim.
- **Method promotion** requires: net_strict ≥ +5pp + n≥30 + Wilson_lower > 0 + owner approval.
- **No method qualifies for production promotion in V99.2** based on 14d sample.

## 14D window — Per region aggregate (all methods)

| Region | n | strict_hits | strict% | strict 95% CI | lenient_hits | lenient% |
|---|---:|---:|---:|---|---:|---:|
| MB | 169 | 0 | **0.0%** | [0.00%, 2.22%] | 42 | **24.9%** |
| MN | 122 | 0 | **0.0%** | [0.00%, 3.05%] | 43 | **35.2%** |
| MT | 122 | 0 | **0.0%** | [0.00%, 3.05%] | 62 | **50.8%** |

## 30D window — Per region aggregate (all methods)

| Region | n | strict_hits | strict% | strict 95% CI | lenient_hits | lenient% |
|---|---:|---:|---:|---|---:|---:|
| MB | 274 | 0 | **0.0%** | [0.00%, 1.38%] | 62 | **22.6%** |
| MN | 227 | 0 | **0.0%** | [0.00%, 1.66%] | 103 | **45.4%** |
| MT | 227 | 0 | **0.0%** | [0.00%, 1.66%] | 88 | **38.8%** |

## 14d — OFFICIAL vs TEST_LANE comparison

| Category | n | strict% | strict 95% CI | lenient% |
|---|---:|---:|---|---:|
| OFFICIAL | 42 | 0.0% | [0.00%, 8.38%] | 38.1% |
| TEST_LANE | 371 | 0.0% | [0.00%, 1.02%] | 35.3% |

## 14d — Top methods by lenient% (sample n>=10) — DIAGNOSTIC ONLY

| Method | Region | n | strict% | strict 95% CI | lenient% |
|---|---|---:|---:|---|---:|
| OFFICIAL_FINAL_BUNDLE | MT | 14 | 0.0% | [0.00%, 21.53%] | **57.1%** |
| MN_AI_CHAIN_PRESERVATION_V1 | MN | 15 | 0.0% | [0.00%, 20.39%] | **53.3%** |
| MT_NO_TOKEN_HERD_REDUCTION_V1 | MT | 15 | 0.0% | [0.00%, 20.39%] | **53.3%** |
| MT_OFFICIAL_BASELINE_CONTROL | MT | 15 | 0.0% | [0.00%, 20.39%] | **53.3%** |
| MT_SPECIALIST_ROSTER_V1 | MT | 15 | 0.0% | [0.00%, 20.39%] | **53.3%** |
| MT_STRENGTH_WEIGHTED_V52_5_2 | MT | 15 | 0.0% | [0.00%, 20.39%] | **53.3%** |
| MN_SPECIALIST_ROSTER_V1 | MN | 15 | 0.0% | [0.00%, 20.39%] | **46.7%** |
| MB_STRENGTH_WEIGHTED_V52_5_2 | MB | 14 | 0.0% | [0.00%, 21.53%] | **42.9%** |
| MB_NO_TOKEN_HERD_REDUCTION_V1 | MB | 22 | 0.0% | [0.00%, 14.87%] | **40.9%** |
| MN_NO_TOKEN_HERD_REDUCTION_V1 | MN | 15 | 0.0% | [0.00%, 20.39%] | **40.0%** |
| MN_OFFICIAL_BASELINE_CONTROL | MN | 15 | 0.0% | [0.00%, 20.39%] | **40.0%** |
| MN_STRENGTH_WEIGHTED_V52_5_2 | MN | 15 | 0.0% | [0.00%, 20.39%] | **40.0%** |
| MT_PRIOR_REGION_CONTEXT_SAFE_V | MT | 15 | 0.0% | [0.00%, 20.39%] | **40.0%** |
| OFFICIAL_FINAL_BUNDLE | MN | 14 | 0.0% | [0.00%, 21.53%] | **35.7%** |
| MT_AI_CHAIN_PRESERVATION_V1 | MT | 15 | 0.0% | [0.00%, 20.39%] | **33.3%** |

## Watchlist methods (DIAGNOSTIC observation, NO promotion)

Top diagnostic methods 14d (n>=10):
- MN_AI_CHAIN_PRESERVATION_V1 (lenient 53.3%, n=15) ⭐
- MT_NO_TOKEN_HERD_REDUCTION_V1 / OFFICIAL / SPECIALIST / STRENGTH (lenient 53.3% each, n=15)
- MN_SPECIALIST_ROSTER_V1 (lenient 46.7%, n=15)
- MB_STRENGTH_WEIGHTED_V52_5_2 (lenient 42.9%, n=14) — best MB despite cold
- MB_NO_TOKEN_HERD_REDUCTION_V1 (lenient 40.9%, n=22)

**No promotion verdict**: All methods 0% strict 14d. Wilson CI strict cannot exclude 0%. Sample n=14-22 too small for production change. **Defer all promotion to FU-173 14d gate 2026-05-21**.

## 2026-05-09 status (await closeout 19:00 VN)

| Region | Method | BT pick | result_known |
|---|---|---|---:|
| MB | V67_EXPLOIT_TOP1 | 37 | 0 |
| MB | V70_CONSENSUS_TOP1 | 37 | 0 |
| MB | V73_HYBRID_AURA | 37 | 0 |
| MN | MN_ADAPTIVE_BUDGET_SELECTOR_V1 | 82 | 0 |
| MN | MN_ADAPTIVE_EXPLOIT_V1 | 13 | 0 |
| MN | MN_AI_CHAIN_PRESERVATION_V1 | 82 | 0 |
| MN | MN_HYBRID_V1 | 13 | 0 |
| MN | MN_NO_TOKEN_HERD_REDUCTION_V1 | 05 | 0 |
| MN | MN_OFFICIAL_BASELINE_CONTROL | 05 | 0 |
| MN | MN_PRIOR_REGION_CONTEXT_SAFE_V1 | None | 0 |
| MN | MN_SPECIALIST_ROSTER_V1 | 05 | 0 |
| MN | MN_STRENGTH_WEIGHTED_V52_5_2 | 82 | 0 |
| MN | OFFICIAL_FINAL_BUNDLE | 05 | 0 |
| MN | V67_EXPLOIT_TOP1 | 13 | 0 |
| MN | V70_CONSENSUS_TOP1 | 13 | 0 |
| MN | V73_HYBRID_AURA | 13 | 0 |
| MT | V67_EXPLOIT_TOP1 | 79 | 0 |
| MT | V70_CONSENSUS_TOP1 | 79 | 0 |
| MT | V73_HYBRID_MEDIUM | 79 | 0 |