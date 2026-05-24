# V10626 Pre-Register Panel SUMMARY

| Panel | Size | Cap |
|---|---:|---:|
| MT | 20 | 20 |
| MN | 15 | 15 |
| MB | 15 | 15 |
| Controls | 3 | 10 |
| Negative controls | 5 | 5 |

All entries: status=`PRE_REGISTER_ONLY`, live_eligible=`False`.
No entries with COMMIT_ELIGIBLE_SHADOW / OUTPUT_ELIGIBLE / PROMOTION_READY.

## Controls list

| Type | Lineage | Target | Axis | Lift |
|---|---|---|---|---:|
| SELF_LAG_AUTOCORR | `MB:MB_BOARD:G1#1:LAST2` | MB | W-2 | +1.17 |
| SELF_LAG_AUTOCORR | `MB:MB_BOARD:G1#1:LAST2` | MB | W-2 | +1.17 |
| SELF_LAG_AUTOCORR | `MB:MB_BOARD:G2#1:LAST2` | MB | W-2 | -2.13 |

## Negative controls list

- `SYNTHETIC:RANDOM_00_99_SEED42` (NEGATIVE_RANDOM_00_99_SEED42, expected_lift_pp = 0)
- `SYNTHETIC:MOON_PHASE_28DAY` (NEGATIVE_MOON_PHASE_28D, expected_lift_pp = 0)
- `SYNTHETIC:LUNAR_DAY_30` (NEGATIVE_LUNAR_DAY_30, expected_lift_pp = 0)
- `SYNTHETIC:DAY_OF_YEAR_TAIL` (NEGATIVE_DAY_OF_YEAR_TAIL, expected_lift_pp = 0)
- `SYNTHETIC:SINE_PERIOD_27` (NEGATIVE_SINE_PERIOD_27, expected_lift_pp = 0)
