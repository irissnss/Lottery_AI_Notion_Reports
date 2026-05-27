> **Public-safe report.** No private code, no DB rows, no provider keys, no raw VPS detail. Numbers shown are summary-only aggregates from V106.36 read-only audit. No official mutation occurred.



# V10636 TRI-REGION CLOSEOUT SUMMARY — 2026-05-27

- ts_vn: `2026-05-27T22:53:15`

## Quick official outcome

| Region | BT | BT status | actual tail_db | actual full_tail (count) |
|---|---|---|---|---|
| MN | `58` | `WIN` | ['09', '38', '40'] | 39 |
| MT | `77` | `LOSE` | ['12', '99'] | 33 |
| MB | `08` | `LOSE` | ['13'] | 24 |

## Per-region model group counts & BT hits & votes-for-official-BT

- MN: counts={'ai_token': 16, 'no_token': 3, 'combo': 4, 'cohere': 0, 'other': 4} bt_hits={'ai_token': 6, 'no_token': 0, 'combo': 1, 'cohere': 0, 'other': 0} votes_for_official={'ai_token': 5, 'no_token': 0, 'combo': 0, 'cohere': 0, 'other': 0} avg_strength={'ai_token': '6.369', 'no_token': '5.567', 'combo': '5.025', 'cohere': '0.000', 'other': '5.125'}
- MT: counts={'ai_token': 16, 'no_token': 3, 'combo': 4, 'cohere': 0, 'other': 5} bt_hits={'ai_token': 11, 'no_token': 2, 'combo': 1, 'cohere': 0, 'other': 3} votes_for_official={'ai_token': 0, 'no_token': 0, 'combo': 1, 'cohere': 0, 'other': 0} avg_strength={'ai_token': '4.675', 'no_token': '6.067', 'combo': '5.975', 'cohere': '0.000', 'other': '7.000'}
- MB: counts={'ai_token': 16, 'no_token': 3, 'combo': 4, 'cohere': 0, 'other': 5} bt_hits={'ai_token': 5, 'no_token': 0, 'combo': 0, 'cohere': 0, 'other': 2} votes_for_official={'ai_token': 0, 'no_token': 0, 'combo': 3, 'cohere': 0, 'other': 0} avg_strength={'ai_token': '5.344', 'no_token': '5.467', 'combo': '5.425', 'cohere': '0.000', 'other': '5.640'}

## Clone / no-commit rates

- MN: same_as_official_bt_rate=0.192 no_commit_rate=0.000 (n_models=27, has_bt=26, same=5, no_commit=0)
- MT: same_as_official_bt_rate=0.036 no_commit_rate=0.000 (n_models=28, has_bt=28, same=1, no_commit=0)
- MB: same_as_official_bt_rate=0.107 no_commit_rate=0.000 (n_models=28, has_bt=28, same=3, no_commit=0)

## Lane-test summary (sum of all experiments)

- MN: would_save=0 would_break=2 false_promo=2 net=-2 correct_but_dropped=4 wrong_boosted=0 lo2_to_bt_promo=2
- MT: would_save=0 would_break=0 false_promo=0 net=0 correct_but_dropped=2 wrong_boosted=6 lo2_to_bt_promo=2
- MB: would_save=0 would_break=0 false_promo=0 net=0 correct_but_dropped=0 wrong_boosted=1 lo2_to_bt_promo=0

## Shadow summary

- MN: bt_hits=2 flip_to_win=0 flip_to_lose=0 false_promo=0 diagnostic_only=10 shadow_only=10 output_eligible=0
- MT: bt_hits=0 flip_to_win=0 flip_to_lose=0 false_promo=0 diagnostic_only=9 shadow_only=9 output_eligible=0
- MB: bt_hits=0 flip_to_win=0 flip_to_lose=0 false_promo=0 diagnostic_only=10 shadow_only=10 output_eligible=0

## Cohere rows today

- MN: cohere_rows=1
- MT: cohere_rows=1
- MB: cohere_rows=1

## Rule105 active rules supporting today

- MN: rule105_active_today_count=5
- MT: rule105_active_today_count=5
- MB: rule105_active_today_count=5

## Runtime reliability today

- MN: runtime_success=11 / total=13
- MT: runtime_success=13 / total=13
- MB: runtime_success=13 / total=13
