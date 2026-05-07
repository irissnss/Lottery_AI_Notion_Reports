# V74 — delta from V73

| Item | V73 | V74 |
|---|---|---|
| C-16 budget for 2026-05-07 | 15 voters MT/MB | 20 voters all regions |
| CONSENSUS_V1 14d rows | empty (regression) | re-backfilled 15 anchors |
| C-03 PENDING | 37 rows | 9 rows (non-closed only) |
| C-17B output_lock_status column | missing | added + 669 rows backfilled |
| Continuous measurement doctrine | implicit | explicit doc + windows + cadence |
| GitHub LATEST_REPORT.json | missing | created |
| GitHub REPORT_INDEX.md | missing | created |
| GitHub CHANGELOG_PUBLIC.md | missing | created |
| GitHub README | stale at V62 | rewritten |
| Daily evidence pack | not bootstrapped | bootstrapped with rolling 7/14/30/60/90/180d Wilson CI |
| C-05 latency live | broken | still broken (P0 next) |
