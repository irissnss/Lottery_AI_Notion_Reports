> **Public-safe report.** No private code, no DB rows, no provider keys, no raw VPS detail. Numbers shown are summary-only aggregates from V106.36 read-only audit. No official mutation occurred.



# V10636 REGION ISOLATION PROOF

- ts_vn: `2026-05-27T23:03:25`

## Per-region rule pool size (TIER_A only)

| Region | TIER_A rules |
|---|---|
| MN | 26 |
| MT | 18 |
| MB | 4 |

## DB writes during lane execution

- official table writes (`predictions`, `final_bundles`, `lottery_results`, `mined_rules`): **0**
- lane-test table writes (`du_doan_test_bundles`, `du_doan_test_results`, `experimental_preview_shadow`): **0** (dry-run only)
- cross-region table touched: **No**
- shared state writes: **0**

## Proof method

- All lane computations are in-memory only.
- Only SELECT statements were issued against `lottery_results`, `final_bundles`, `mined_rules`.
- No `INSERT/UPDATE/DELETE` to any DB table.
- Phase 9 will re-hash DB and prove integrity.
