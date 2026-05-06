# C16 audit

## Daily
| run_date | region | total_pool_count | measured_pool_count | selected_count | watch_count | skipped_count | created_at |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-05-05 | MB | 29 | 28 | 8 | 10 | 11 | 2026-05-05T23:10:52+07:00 |
| 2026-05-05 | MN | 29 | 28 | 10 | 16 | 3 | 2026-05-05T23:10:51+07:00 |
| 2026-05-05 | MT | 29 | 28 | 8 | 14 | 7 | 2026-05-05T23:10:52+07:00 |
| 2026-05-06 | MB | 29 | 23 | 8 | 10 | 11 | 2026-05-06T17:40:00+07:00 |
| 2026-05-06 | MN | 29 | 28 | 10 | 18 | 1 | 2026-05-06T07:50:52+07:00 |
| 2026-05-06 | MT | 29 | 22 | 8 | 10 | 11 | 2026-05-06T16:45:00+07:00 |

## Empty selected picks
| run_date | region | model_name | selector_role | final_budget_score | pick_for_date_json |
| --- | --- | --- | --- | --- | --- |
| 2026-05-06 | MB | qwen3-max-thinking | SELECTED_VOTER | 0.3125 | {} |
| 2026-05-06 | MB | qwen3.6-plus | CONTROL | 0.3824 | {} |
| 2026-05-06 | MT | qwen3-coder | SELECTED_VOTER | 0.3431 | {} |

## Role summary
| run_date | region | selector_role | n | avg_score |
| --- | --- | --- | --- | --- |
| 2026-05-05 | MB | CONTROL | 4 | 0.428 |
| 2026-05-05 | MB | SELECTED_VOTER | 4 | 0.3494 |
| 2026-05-05 | MB | SKIP_TODAY | 11 | 0.2478 |
| 2026-05-05 | MB | WATCH_ONLY | 10 | 0.2281 |
| 2026-05-05 | MN | CONTROL | 4 | 0.4747 |
| 2026-05-05 | MN | SELECTED_VOTER | 6 | 0.5241 |
| 2026-05-05 | MN | SKIP_TODAY | 3 | 0.2223 |
| 2026-05-05 | MN | WATCH_ONLY | 16 | 0.3198 |
| 2026-05-05 | MT | CONTROL | 4 | 0.4371 |
| 2026-05-05 | MT | SELECTED_VOTER | 4 | 0.4305 |
| 2026-05-05 | MT | SKIP_TODAY | 7 | 0.2303 |
| 2026-05-05 | MT | WATCH_ONLY | 14 | 0.2811 |
| 2026-05-06 | MB | CONTROL | 4 | 0.3653 |
| 2026-05-06 | MB | SELECTED_VOTER | 4 | 0.328 |
| 2026-05-06 | MB | SKIP_TODAY | 11 | 0.2568 |
| 2026-05-06 | MB | WATCH_ONLY | 10 | 0.1853 |
| 2026-05-06 | MN | CONTROL | 4 | 0.5532 |
| 2026-05-06 | MN | SELECTED_VOTER | 6 | 0.54 |
| 2026-05-06 | MN | SKIP_TODAY | 1 | 0.0935 |
| 2026-05-06 | MN | WATCH_ONLY | 18 | 0.3958 |
| 2026-05-06 | MT | CONTROL | 4 | 0.3892 |
| 2026-05-06 | MT | SELECTED_VOTER | 4 | 0.3345 |
| 2026-05-06 | MT | SKIP_TODAY | 11 | 0.247 |
| 2026-05-06 | MT | WATCH_ONLY | 10 | 0.1781 |
