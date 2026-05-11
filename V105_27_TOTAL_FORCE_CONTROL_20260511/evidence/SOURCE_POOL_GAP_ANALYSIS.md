# SOURCE-POOL GAP ANALYSIS — V105.27

## 1. Local DB diagnostic table inventory

Mission expected:

- `v10524_source_pool_gap_drilldown` — **NOT PRESENT in local DB**
- `v10524_candidate_flow_trace` — **NOT PRESENT in local DB**
- `v10524_v102_strong_selector_shadow` — NOT PRESENT (only `v10522_v102_strong_selector_shadow` = 0 rows)

Materializer code DOES exist at `web/backend/_v10524_source_pool_gap_drilldown.py` and `web/backend/_v10525_candidate_flow_funnel.py`, but tables were never instantiated in this DB.

Likely-canonical alternative tables present:

| Table | Rows | Role |
|---|---:|---|
| `candidate_drop_stage_daily` | 103 | Per-day drop-stage diagnostics |
| `bundle_universe_coverage_daily` | 3076 | Bundle coverage per day |
| `source_prize_strong_coverage` | 3076 | Source-prize strong tier daily |
| `rule_injection_contract` | 3076 | Rule injection daily contract |
| `v101_region_source_pool_shadow` | 10170 | Region source-pool detail |
| `v101_region_source_pool_top5_shadow` | 1695 | Region top5 |
| `v103_candidate_supply_shadow` | 8743 | V103 supply |
| `v103_prompt_candidate_gate_shadow` | 8743 | V103 prompt gate |
| `v104_shadow_prompt_candidate_injection` | 1823 | V104 injection |
| `v104_shadow_prompt_model_decision` | 93 | V104 decision |
| `v105_no_token_independent_shadow` | 7126 | No-token shadow rows |

## 2. Cannot run mission SQL as-written

The four SQL queries in mission body require columns/tables not present locally:

- `miss_reason` not in any existing table directly.
- `actual_tail` not in any candidate table directly.

**Action**: This audit defers running those exact queries to a future session that either materializes the missing tables on VPS or accepts the alternative diagnostic tables above.

## 3. Indirect evidence — drop-stage funnel (from existing tables)

From V105.22 truth row + current rows:

| Region | Stage (V101→V103→V104) | Approx volume | Notes |
|---|---|---:|---|
| MN | Source pool | high (V101 top5 always populated) | MN priority active |
| MT | Source pool | high; V102 STRONG/PROMPT_REVIEW_STRONG context measured but **not yet selector-ranked into V67 top2** (FU-V105-11 still open per V105.10 row) | Selector gap, not source gap |
| MB | Source pool | high; MB AI chain preservation table populated (30 rows) | Forensic mode |

## 4. Suspected drop stages (subject to materializer run)

| Drop stage | Likely cause | How to confirm |
|---|---|---|
| `FORMULA_EXCLUSION` | Candidate not in `(MN+MT+MB) D-1` for MT/MB, or not in `(MN+MT+MB) D-1/D-2` for MN | Materialize gap drilldown |
| `TOP30_CAP` | Source-pool capped at 30, valid candidate ranked 31+ | Materialize `v10524_source_pool_gap_drilldown` |
| `PROMPT_NOT_INJECTED` | Candidate in pool but not in V104 prompt context | Cross `v101_region_source_pool_shadow` × `v104_shadow_prompt_candidate_injection` |
| `SELECTOR_RANK_DROP` | In prompt but not in top2 | Cross `v104_shadow_prompt_candidate_injection` × `final_bundles` |
| `BUNDLE_DROP` | In top2 but not in final bundle | Cross `top2` × `final_bundles` |

## 5. Verdicts

- `SOURCE_POOL_GAP_TABLE_NOT_MATERIALIZED` — owner gate to run `_v10524_source_pool_gap_drilldown.py` materializer locally or on VPS.
- `SOURCE_POOL_GAP_ACTIVE` — implicit (V105.24/V105.26 reports referenced miss reasons but local DB cannot verify without materializing).
- No write/promote actions taken. No provider call.
