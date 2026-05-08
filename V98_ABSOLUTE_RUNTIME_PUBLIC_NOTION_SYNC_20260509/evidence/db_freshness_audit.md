# V98 DB Freshness Audit

## Sync info (Pre-V98 audit)

- DB Source: VPS `/root/Lottery_AI_Test/data/lottery_ai.db`
- Sync timestamp: 2026-05-09 00:30 VN (post Phase 0 sync)
- Sync manifest: `artifacts/live_sync/latest_manifest.json`
- DB access: **FRESH_SYNC**
- Freshness status: ✅ Fresh — copy-of-VPS within last 20 minutes

## Today (2026-05-09) row counts at audit time

| Table | Today rows |
|---|---|
| `predictions` | 81 (3 region × 27 models avg) |
| `final_bundles` | 3 (one per region tomorrow MN/MT/MB) |
| `model_daily_eval` | 0 (eval rebuilds nightly post-cascade) |
| `du_doan_test_*` | varies |

## V93/V94/V95/V96 shadow tables today

- `v93_wr_gate_filter_audit_shadow`: 2055 rows total, 50/today
- `v93_verdict_weight_recalibration_shadow`: 910 rows total, 25/today
- `v93_mn_save_signal_per_method_shadow`: 204 rows total, 5/today
- `v94_cross_region_spillover_aware_shadow`: 3211 rows total, 95/today
- `v94_cross_region_leakage_continuous_monitor`: 540 rows total, 18/today
- `v94_no_token_first_simulation_shadow`: 5 rows
- `v95_data_freshness_audit_shadow`: 1502 rows
- `v95_ai_context_completeness_shadow`: 1337 rows
- `v96_master_tracker_daily_snapshot`: 1 row (today)

## V95 data integrity shadow snapshot (30d)

| Region | Integrity | n | main_hits | main_hit_pct |
|---|---|---|---|---|
| MN | clean | TBD via V98 panel 9 | TBD | TBD |
| MN | provisional | TBD | TBD | TBD |
| MT | clean | TBD | TBD | TBD |
| MT | provisional | TBD | TBD | TBD |
| MB | clean | TBD | TBD | TBD |
| MB | provisional | TBD | TBD | TBD |

→ Live values populated via V98 Command Center Panel 9 (Data Freshness 30d).

## Cross-region leakage 30d (V94.1 monitor)

| Pair | 7d Δpp | 14d Δpp | 30d Δpp | Alert |
|---|---|---|---|---|
| MN→MT | TBD | TBD | +13.70 | ALERT_HIGH |
| MN→MB | TBD | TBD | +12.78 | ALERT_HIGH |
| MT→MB | TBD | TBD | +6.32 | ALERT_MEDIUM |
| MT→MN | TBD | TBD | TBD | TBD |
| MB→MN | TBD | TBD | TBD | TBD |
| MB→MT | TBD | TBD | TBD | TBD |

→ Live values populated via V98 Command Center Panel 8.

## No-write doctrine

V98 audit phase: NO writes to DB. Evidence read from existing shadow tables built by V93/V94/V95/V96 cron. V98 Command Center backend `_v98_command_center.py` is read-only aggregator.
