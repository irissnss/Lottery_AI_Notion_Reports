# METRIC DICTIONARY (test-lane scoreboard)

> Defines every metric the daily evidence pack and method scoreboards must compute.

## Per (date, region, method)

| Metric | Definition |
|---|---|
| `n` | closed days where method emitted a candidate AND actuals exist |
| `hit_count` | days where `candidate_bt` ∈ actuals_tails(date, region) |
| `hit_rate` | `hit_count / n` |
| `wilson_ci_95_lo` / `_hi` | Wilson score interval at 95% |
| `profit_proxy` | `+payout_per_unit − 1` per hit, `−1` per miss; payout MN/MT=80x, MB=70x |
| `roi_pct` | `profit_proxy / n * 100` |
| `delta_vs_official_pp` | `hit_rate − OFFICIAL.hit_rate` |
| `delta_vs_random_pp` | `hit_rate − random_baseline_for_region` |
| `would_save` | OFFICIAL miss AND method hit AND method ≠ OFFICIAL |
| `would_break` | OFFICIAL hit AND method miss AND method ≠ OFFICIAL |
| `net_save_break` | `would_save − would_break` |
| `false_promotion` | method changes BT to a tail that did NOT win, while OFFICIAL did win |
| `lo2_hit` | any tail in `candidate_lo2_json` ∈ actuals_tails |
| `lo3_strict_hit` | candidate 3-càng matches full 3-digit suffix in actuals (NOT 2-digit shortcut) |
| `xien2_strict_hit` | both xien-2 picks hit at SAME station |
| `xien3_strict_hit` | all 3 xien-3 picks hit at SAME station |
| `agreement_count` | for CONSENSUS / HYBRID: number of methods that voted for `candidate_bt` |
| `tier` | for HYBRID: `CROWN`, `AURA`, `HIGH`, `MEDIUM`, `LOW`, or `SKIP` |
| `confidence_class` | `HIGH` if ≥2 contributing sources, `MEDIUM` if score ≥1.10, else `LOW` |
| `voter_count` | for C-16: number of selected voters |
| `model_class_mix` | `{TOKEN: n, NO_TOKEN: n, SHADOW: n}` |
| `flow_type` | for V66.1: which flow contributed |
| `duplicate_count` | rows with same logical key (date+region+experiment+run_label) |
| `pending_count` | `du_doan_test_results` rows with `official_bt_status` IS NULL or 'PENDING' |
| `output_lock_status` | `READY_PRE_RESULT_LOCKED` / `PARTIAL_BUDGET_LOCKED` / `NOT_READY_NO_PICK` / `POST_CLOSEOUT_DIAGNOSTIC_ONLY` / `DUPLICATE_BLOCKED` / `EVALUATOR_PENDING` / `EVALUATOR_FAILED` / `EVALUATED_AFTER_CLOSEOUT` |
| `latency_available` | 1 if C-05 captured wall-time + tokens for at least one model call |
| `scheduler_status` | `OK`, `MISSED`, `PARTIAL`, `ERROR` |
| `official_mutation` | always `false` for test-lane methods |

## Rolling windows

`1d`, `3d`, `7d`, `14d`, `30d`, `60d`, `90d`, `180d`, `lifetime`

## Aggregations

- per region (MN, MT, MB)
- per region+weekday
- per region+weekday+station_set
- per model_class (TOKEN, NO_TOKEN, SHADOW)
- per flow_type (for V66.1 signals)
- per tier (for HYBRID)
- ALL regions combined

## Random baselines (per region)

- MN: avg_distinct_tails ≈ 43 → P(hit) k=1 ≈ 43.0%
- MT: ≈ 35 → 35.0%
- MB: ≈ 24 → 24.0%

(Refresh weekly via materializer; current values in `lag1_adaptive_exploit_signal_shadow.random_baseline_rate`.)

STATUS: **DICTIONARY V20.3.37.74 LOCKED**.
