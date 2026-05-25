# V106.29 Schema Extractor Audit Public-Safe

## Scope

This public file records the owner-image canonical prize contract and a safe metadata-only schema check. It does not publish lottery result rows, prediction rows, runtime trace rows, or private raw artifacts.

## Canonical owner-image contract

### MN/MT

| Prize | Count | Digits |
|---|---:|---:|
| DB | 1 | 6 |
| G1 | 1 | 5 |
| G2 | 1 | 5 |
| G3 | 2 | 5 |
| G4 | 7 | 5 |
| G5 | 1 | 4 |
| G6 | 3 | 4 |
| G7 | 1 | 3 |
| G8 | 1 | 2 |

### MB

| Prize | Count | Digits |
|---|---:|---:|
| DB | 1 | 5 |
| G1 | 1 | 5 |
| G2 | 2 | 5 |
| G3 | 6 | 5 |
| G4 | 4 | 4 |
| G5 | 6 | 4 |
| G6 | 3 | 3 |
| G7 | 4 | 2 |

## Safe DB schema metadata checked

- `lottery_results` columns checked: id, date, region, station, prizes_json, tail_db, tail_g8, created_at
- `predictions` columns checked: id, date, target_region, source_regions, ai_model, main_numbers, analysis_text, phase_type, cluster, pivot, strength, verdict, verdict_reason, status, hit_numbers, hit_level, hit_details, created_at, verified_at, pick_count, hit_count, reasoning_json, pre_result_numbers, pre_result_strength, pre_result_status, pre_result_hit_count, repredict_verdict, run_source, convergence_flag, prediction_before, verified_station_count, policy_version_ref, week_slot, context_integrity, run_id
- `final_bundles` columns checked: id, date, region, bach_thu, lo2, lo3, xien2, xien3, policy_version_ref, source_predictions_json, generation_method, consensus_level, model_count, top_score, is_fallback, status, notes, created_at, updated_at, bach_thu_status, lo2_status, lo3_status, xien2_status, xien3_status, verified_at, bundle_version

## Public conclusion

V106.28R1 remains blocked until private V106.28R0 schema/extractor integrity audit passes. No rule import, selector switch, prompt switch, or official mutation is authorized by this public package.
