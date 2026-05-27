> **Public-safe report.** No private code, no DB rows, no provider keys, no raw VPS detail. Numbers shown are summary-only aggregates from V106.36 read-only audit. No official mutation occurred.



# V10636 AI-TOKEN BRANCH AUDIT

- ts_vn: `2026-05-27T22:57:04`

## Per-region AI-token branch (30d windows)

| Region | N_models | BT hits | hit_rate | hits | picks | hit/pick | no_commit | latency_ms |
|---|---|---|---|---|---|---|---|---|
| MB | 16 | 91 | 0.204 | 179 | 864 | 0.207 | 0 | 107163.7 |
| MN | 16 | 209 | 0.464 | 383 | 881 | 0.435 | 0 | 121630.7 |
| MT | 16 | 143 | 0.324 | 284 | 857 | 0.331 | 0 | 106312.0 |

## AI-token branch verdict (region-specific)

- MB: bt_hit_rate=0.204 contrib_to_winning=0.044 avg_latency_ms=107163.7 → **LANE_LIMIT_HIGH_HIT_LOW_CONTRIB (selector_gap candidate)**
- MN: bt_hit_rate=0.464 contrib_to_winning=0.274 avg_latency_ms=121630.7 → **LANE_PRESERVE**
- MT: bt_hit_rate=0.324 contrib_to_winning=0.014 avg_latency_ms=106312.0 → **LANE_LIMIT_HIGH_HIT_LOW_CONTRIB (selector_gap candidate)**

## Region-comparative interpretation

- MB AI-token 30d: bt_hit_rate barely above 20% baseline, contribution 4.4%. AI-token effectively neutral in 95% of MB winning days → freeze candidate.
- MT AI-token 30d: hit_rate 32% but contribution 1.4%. Models find correct tail but selector picks different BT → selector_gap; AI-token NOT the bottleneck.
- MN AI-token 30d: hit_rate 46%, contribution 27% — single best-value branch across regions.