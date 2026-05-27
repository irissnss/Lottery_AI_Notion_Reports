> **Public-safe report.** No private code, no DB rows, no provider keys, no raw VPS detail. Numbers shown are summary-only aggregates from V106.36 read-only audit. No official mutation occurred.



# V10636 PHASE 6 — Lane Execution Interpretation

- ts_vn: 2026-05-27T23:04:00+07:00
- date: 2026-05-27 Wed (weekday=2)

## Weekday gap finding (TIER_A only)

| Region | total TIER_A | weekday=2 (Wed) | weekdays present |
|---|---|---|---|
| MN | 26 | 5 | {0:2, 1:5, 2:5, 3:4, 4:5, 5:5} |
| MT | 18 | 0 | {0:5, 1:2, 3:3, 4:1, 5:4, 6:3} |
| MB | 4 | 0 | {0:2, 4:1, 6:1} |

Interpretation:
- MN has TIER_A coverage on 6/7 weekdays; missing only weekday=6 (Sun).
- MT has TIER_A coverage on 6/7 weekdays; missing weekday=2 (Wed).
- MB has TIER_A coverage on only 3/7 weekdays; missing Tue/Wed/Thu/Sat = 4 days/week.

Today (Wed 2026-05-27) → MT and MB lane executions necessarily return empty pools. This is NOT a script bug; it is a real distribution gap in the current 105 mined_rules. PHASE 8 ledger tracks this as an action item.

## MN lane execution finding

- lane_bt = **39** (false consensus from 4 same-station-different-prize-key rules of `MB:Quảng Ninh@D-1`).
- official_bt = **58** WIN.
- lane lost vs official today: lane_bt_hit_db = 0, lane_bt_hit_full = 1.
- This confirms the **selector_gap / false_consensus** pattern: rules pile up on the same station and prize key family, producing the same tails, which inflates the lane score without true independent evidence.

Recommended dampener upgrade for V10637:
- count `unique(source_region, source_station, source_offset)` rather than `n_rules`.
- if `unique_source_evidence < 2`, scale lane score to 30%.

## MT/MB lane execution finding

- lane_bt = None (no rule eligible today).
- Recommendation: in V10637+, mining must close the weekday coverage gap so each region has TIER_A coverage on every weekday OR the lane must fall back to TIER_B SHADOW_ONLY when no TIER_A rule is available.

## Region isolation proof

- DB writes during lane execution: **0**
- Cross-region table touched: **No**
- Only SELECT against `lottery_results`, `final_bundles`, `mined_rules`.
- PHASE 9 re-hash will prove official tables unchanged.

## Action items into V10636 ledger (Phase 8)

| Item | Region | Severity | Action tonight | Action tomorrow |
|---|---|---|---|---|
| Close weekday=2 TIER_A gap | MT | P1 | document gap | re-mine + observe |
| Close weekday gap (4 days) | MB | P0 | document gap | re-mine + observe |
| Upgrade dampener: unique_source_evidence | MN | P1 | spec'd here | implement in V10637 shadow |
