# PHASE 0 — TABLE INVENTORY MAP (read-only)

- Generated: 2026-05-29T21:25:42+07:00
- Total tables: 163
- Tables with non-canonical column names: 100
- Dead tables (0 rows): 9
- Duplicate pairs: 6

## By flow

| Flow | Tables | Full per-slice axis |
|---|---|---|
| OFFICIAL | 10 | 2 |
| LANE_TEST | 21 | 2 |
| SHADOW | 62 | 13 |
| MEASUREMENT_DAILY | 39 | 3 |
| OTHER_AMBIGUOUS | 31 | 4 |

## Dead tables (candidate drop after backup)

bundle_replay_compare_daily, data_preservation_manifest_daily, du_doan_test_ai_predictions, du_doan_test_latency_daily, rule_effectiveness, rule_features, sync_parity_audit_daily, training_records, v10522_v102_strong_selector_shadow

## Duplicate pairs (candidate merge)

- `ai_prompt_context_audit_shadow` <~> `ai_region_specialist_prompt_shadow_results`
- `digit_transform_source_rule_shadow_v10610` <~> `exact_position_source_rule_shadow_v10610`
- `experimental_preview_shadow` <~> `mb_experimental_preview_shadow`
- `pre_partial_post_lose_daily` <~> `pre_win_post_lose_daily`
- `tier2_replay_shadow` <~> `tier2_replay_v2_shadow`
- `v101_mn_cross_region_rule_shadow` <~> `v101_region_source_pool_shadow`