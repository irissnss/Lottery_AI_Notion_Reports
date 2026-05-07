# TEST LANE METHOD REGISTRY

> Active test-lane methods (V20.3.37.74). Test-lane only. ZERO touch official.

| ID | Name | Source | Selector logic | Region scope | Output table | Trace table | Cron VN | Status |
|---|---|---|---|---|---|---|---|---|
| M01 | OFFICIAL_BASELINE_CONTROL | `final_bundles` | clone-of-official baseline | MN/MT/MB | `experimental_preview_shadow` | — | (mirror) | ACTIVE_TEST |
| M02 | C16_BUDGET_SELECTOR_V1 | C-16 budget materializer | weighted vote of 20 strongest measured models per region/weekday/station | MN/MT/MB | `experimental_preview_shadow` + `du_doan_test_model_budget_daily` + `du_doan_test_selected_voters` | `du_doan_test_model_skip_reason` | (with closeout) | ACTIVE_TEST |
| M03 | V67_ADAPTIVE_EXPLOIT_V1 | V66.1 BOOST signals | per-model lag-1 + cross-region next-day + same-region lag-1 + LO2 lag-1 weighted by `1+Δpp/100` cap 1.5 | MN/MT/MB | `experimental_preview_shadow` | `adaptive_exploit_v67_candidate_trace` | 23:40 | ACTIVE_TEST (eager) |
| M04 | V70_CONSENSUS_V1 | other test-method picks | gate `agreement_count >= 3`; excludes OFFICIAL_BASELINE_CONTROL | MN/MT/MB | `experimental_preview_shadow` | `consensus_v1_trace` | 23:45 | ACTIVE_TEST |
| M05 | V73_HYBRID_V1 | combines M02/M03/M04 | region-adaptive priority: MN/MB exploit-first; MT consensus-first; CROWN if M03==M04 | MN/MT/MB | `experimental_preview_shadow` | `hybrid_v1_trace` | 23:48 | ACTIVE_TEST |
| M06 | AI_CHAIN_PRESERVATION_V1 | shared candidate set | preserves high AI-chain consensus | MN/MT/MB | `experimental_preview_shadow` | — | (with closeout) | ACTIVE_TEST |
| M07 | NO_TOKEN_HERD_REDUCTION_V1 | shared candidate set | down-weight no-token herd | MN/MT/MB | `experimental_preview_shadow` | — | (with closeout) | DIAGNOSTIC_ONLY |
| M08 | SPECIALIST_ROSTER_V1 | shared candidate set | placeholder | MN/MT/MB | `experimental_preview_shadow` | — | (with closeout) | PLACEHOLDER_ONLY |
| M09 | PRIOR_REGION_CONTEXT_SAFE_V1 | prior-region same-day actuals | uses MN(D) for MT, MN(D)+MT(D) for MB | MN/MT/MB | `experimental_preview_shadow` | — | (with closeout) | ACTIVE_TEST |
| M10 | STRENGTH_WEIGHTED_V52_5_2 | strength tensor | weighted aggregation by region/weekday/station strength | MN/MT/MB | `experimental_preview_shadow` | — | (with closeout) | ACTIVE_TEST |

## Signal layer

| Layer | Source | Refresh | Purpose |
|---|---|---|---|
| Strength tensor | `model_strength_by_region_weekday_station_daily` | daily, 4 windows × 3 grains | per-region/weekday/station strength |
| V66.1 lag-1 signals | `lag1_adaptive_exploit_signal_shadow` | 23:35 daily | 11 flow_types: same-region lag-1/2/3, cross-region same/next, predictions class & per-model, LO2, repeat-tail, per-weekday |
| C-16 budget | `du_doan_test_model_budget_daily` + `du_doan_test_selected_voters` | per closeout cycle | top-20 strongest voters per region |
| V67 exploit signal | `adaptive_exploit_v67_candidate_trace` | 23:40 daily | yesterday LOSE picks weighted by V66.1 BOOST |
| V70 consensus signal | `consensus_v1_trace` | 23:45 daily | agreement_count tally |
| V73 hybrid trace | `hybrid_v1_trace` | 23:48 daily | tier breakdown CROWN/AURA/HIGH/MEDIUM/LOW/SKIP |

## Hard contract for every entry

- `output_eligible = 0` for all test-lane rows
- `diagnostic_only = 1` unless explicitly labeled active test
- `owner_approved = 0` until owner OK in `DECISION_LOG.md`
- ZERO write to `predictions`, `final_bundles`, `model_daily_eval`, `lottery_results`, scoring, prompts, model_registry
- pre/post hash guard for 4 official tables

STATUS: **REGISTERED V20.3.37.74**.
