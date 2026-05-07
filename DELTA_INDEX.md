# DELTA INDEX (between consecutive versions)

## V75 → V76
- 3 P0 items deployed: drift detector + C-16 latency_score live + cost provider table.
- New shadow table: `test_lane_signal_drift_monitor`.
- New file: `_provider_pricing_table.py` (configurable USD/1k tokens).
- Patched: `_latency_score()` rolling 7d avg gentle curve no-prune.
- Patched: V52 measurement materializer to derive cost_estimate from provider table.
- New cron 23:50 VN (drift monitor alert-only).
- Cron schedule expanded to 5 jobs.

## V74 → V75
- C-05 status corrected: NOT BROKEN, was data lag. 20/42 rows captured 2026-05-07.
- V75 NEXT_ACTION_PROPOSAL published with P0-P3 tiers.
- OPEN_ISSUES.md updated: C-05 marked RESOLVED.
- No code change in V75 (proposal only).

## V73 → V74
- Runtime verification PASS/FAIL table
- C-16 budget 2026-05-07 fixed to 20 voters
- CONSENSUS_V1 re-backfilled
- C-03 evaluator PENDING reduced 37→9
- C-17B output_lock_status column added
- 4 governance docs created
- Daily evidence pack bootstrapped (rolling 1/3/7/14/30/60/90/180d Wilson CI)
- GitHub README rewritten
- LATEST_REPORT.json / REPORT_INDEX.md / CHANGELOG_PUBLIC.md / OPEN_ISSUES.md / NEXT_ACTION.md / DELTA_INDEX.md created

## V72 → V73
- Region-adaptive HYBRID priority (MN/MB exploit-first; MT consensus-first)
- New AURA tier
- ALL-region 14d HYBRID 45.2% → 57.1%

## V71 → V72
- V67 STRICT gate disabled
- V67 sample restored MN 5/5

## V70 → V71
- C-16 score gate (0.42) removed
- HYBRID_V1 5-tier selector

## V69 → V70
- CONSENSUS_V1 selector with agreement_count≥3 gate

## V68 → V69
- Metrics expansion: Wilson CI, profit, agreement bucket, daily scoreboard

## V67 → V68
- C-16 target_min/max 8/10 → 15/20

## V66.1 → V67
- ADAPTIVE_EXPLOIT_V1 selector built from V66.1 BOOST signals

## V66 → V66.1
- Materializer expanded from 5 to 11 flow_types
