> **Public-safe report.** No private code, no DB rows, no provider keys, no raw VPS detail. Numbers shown are summary-only aggregates from V106.36 read-only audit. No official mutation occurred.



# V10636 MN MN_INDEPENDENT_LANE_V1 EXECUTION (dry-run, artifact-only)

- ts_vn: `2026-05-27T23:03:25`
- date: `2026-05-27` (today_weekday=2)
- rules_eligible_today: 5
- tail_pool_size: 11 (cap max_pool=8)
- dampeners_applied: []

## Lane decisions

- lane_bt: `39`
- lane_lo2: `['39', '74']`
- official_bt: `58` status `WIN`
- lane_bt_same_as_official: 0 | hit_db: 0 | hit_full: 1
- actual_tails_db: ['09', '38', '40', '64', '94']

## Top pool

| Rank | Tail | Score | N rules | Contributors |
|---|---|---|---|---|
| 1 | `39` | 0.84 | 4 | MB:Quảng Ninh@D-1(G7, w=0.21), MB:Quảng Ninh@D-1(GĐB+G7, w=0.21), MB:Quảng Ninh@D-1(G1+G7, w=0.21), MB:Quảng Ninh@D-1(G6+G7, w=0.21) |
| 2 | `74` | 0.84 | 4 | MB:Quảng Ninh@D-1(G7, w=0.21), MB:Quảng Ninh@D-1(GĐB+G7, w=0.21), MB:Quảng Ninh@D-1(G1+G7, w=0.21), MB:Quảng Ninh@D-1(G6+G7, w=0.21) |
| 3 | `28` | 0.84 | 4 | MB:Quảng Ninh@D-1(G7, w=0.21), MB:Quảng Ninh@D-1(GĐB+G7, w=0.21), MB:Quảng Ninh@D-1(G1+G7, w=0.21), MB:Quảng Ninh@D-1(G6+G7, w=0.21) |
| 4 | `81` | 0.84 | 4 | MB:Quảng Ninh@D-1(G7, w=0.21), MB:Quảng Ninh@D-1(GĐB+G7, w=0.21), MB:Quảng Ninh@D-1(G1+G7, w=0.21), MB:Quảng Ninh@D-1(G6+G7, w=0.21) |
| 5 | `11` | 0.21 | 1 | MB:Quảng Ninh@D-1(GĐB+G7, w=0.21) |
| 6 | `77` | 0.21 | 1 | MB:Quảng Ninh@D-1(G1+G7, w=0.21) |
| 7 | `51` | 0.21 | 1 | MB:Quảng Ninh@D-1(G6+G7, w=0.21) |
| 8 | `23` | 0.21 | 1 | MB:Quảng Ninh@D-1(G6+G7, w=0.21) |

## Rules used

| src_station | src_region | offset | prize_keys | composite | v10636_tier | weight | n_signals |
|---|---|---|---|---|---|---|---|
| Quảng Ninh | MB | D-1 | G7 | 100.0 | RERANK_ONLY | 0.3 | 4 |
| Quảng Ninh | MB | D-1 | GĐB+G7 | 100.0 | RERANK_ONLY | 0.3 | 5 |
| Quảng Ninh | MB | D-1 | G1+G7 | 100.0 | RERANK_ONLY | 0.3 | 5 |
| Quảng Ninh | MB | D-1 | G6+G7 | 100.0 | RERANK_ONLY | 0.3 | 7 |
| Bến Tre | MN | D-1 | G7+G8 | 91.1 | CONFIRM_ONLY | 0.3 | 2 |

## Safety

- official_mutation: false
- lane_promotion: false
- du_doan_test_bundles write: false (dry-run only)
- final_bundles write: false
- mined_rules write: false
- region_isolation: only this region's rules used
