> **Public-safe report.** No private code, no DB rows, no provider keys, no raw VPS detail. Numbers shown are summary-only aggregates from V106.36 read-only audit. No official mutation occurred.



# V10636 RULE105 WINDOW SENSITIVITY

- ts_vn: `2026-05-27T22:58:52`

## Distribution of best_window per region

| Region | best_window | N |
|---|---|---|
| MB | 12w | 3 |
| MB | 16w | 5 |
| MB | 4w | 24 |
| MB | 8w | 3 |
| MN | 12w | 1 |
| MN | 16w | 3 |
| MN | 4w | 31 |
| MT | 12w | 5 |
| MT | 16w | 7 |
| MT | 4w | 21 |
| MT | 8w | 2 |

## Stable vs noisy

| Region | stable_window | N |
|---|---|---|
| MB | 12w_16w_stable | 20 |
| MB | noisy | 15 |
| MN | 12w_16w_stable | 31 |
| MN | noisy | 4 |
| MT | 12w_16w_stable | 30 |
| MT | noisy | 5 |

## Current window noise (4w vs 12-16w longer windows)

Negative pp = 4w is below longer windows (recent decay)

| Region | rules with 4w decay >5pp | rules with 4w boost >5pp |
|---|---|---|
| MN | 4 | 13 |
| MT | 12 | 16 |
| MB | 7 | 14 |