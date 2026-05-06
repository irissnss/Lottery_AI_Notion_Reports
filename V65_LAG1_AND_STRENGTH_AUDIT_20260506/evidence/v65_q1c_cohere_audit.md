# V65 Q1c — Cohere effectiveness vs lag-1 leakage

Window: 2026-04-07 .. 2026-05-06

## Per region — old (combo_super top-1) vs new (Cohere top-1)

| region | n | bt_changed | old_hit_N | new_hit_N | old_lose_N→old_hit_N1 | new_lose_N→new_hit_N1 |
|---|---:|---:|---:|---:|---:|---:|
| MN | 20 | 5.0% | 50.0% | 50.0% | 80.0% | 70.0% |
| MT | 20 | 5.0% | 30.0% | 30.0% | 35.7% | 42.9% |
| MB | 20 | 5.0% | 25.0% | 25.0% | 26.7% | 20.0% |

## Examples

- MN 2026-04-19 old=18 new=18 (old_bt_lose_N_then_hit_N1)
- MT 2026-04-19 old=27 new=27 (old_bt_lose_N_then_hit_N1)
- MN 2026-04-22 old=22 new=22 (old_bt_lose_N_then_hit_N1)
- MT 2026-04-22 old=85 new=85 (old_bt_lose_N_then_hit_N1)
- MN 2026-04-25 old=32 new=32 (old_bt_lose_N_then_hit_N1)
- MN 2026-04-26 old=57 new=57 (old_bt_lose_N_then_hit_N1)
- MB 2026-04-28 old=41 new=41 (old_bt_lose_N_then_hit_N1)
- MN 2026-04-28 old=79 new=79 (old_bt_lose_N_then_hit_N1)
- MT 2026-04-28 old=23 new=23 (old_bt_lose_N_then_hit_N1)
- MN 2026-04-29 old=67 new=67 (old_bt_lose_N_then_hit_N1)

## Verdict

- If `new_lose_N→new_hit_N1` is meaningfully LOWER than `old_lose_N→old_hit_N1`, Cohere is effective.
- If unchanged or higher, Cohere does NOT mitigate lag-1 leakage.