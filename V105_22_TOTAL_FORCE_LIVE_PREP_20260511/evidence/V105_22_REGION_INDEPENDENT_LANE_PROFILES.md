# V105.22 Region-Independent Lane Profiles

Generated: 2026-05-11T08:59:39+07:00

Safety scope: lane-test / shadow / diagnostic only. No production scoring, selector, bundle voting, official prompt, official roster, `generate_final_bundle()`, `/du-doan`, or `/api/final-bundle` mutation.

Hash guard pre/post for the V105.22 live-prep deploy and access-log stability fix is identical for the four official evidence tables:

```json
{
  "predictions": {
    "rows": 4739,
    "sha256": "a3a6022eda6fadcf244f7b429091d5d6d0a1946d8816ce1266e6fc14584a1b2c"
  },
  "final_bundles": {
    "rows": 217,
    "sha256": "105ed85c01defb3c6407dff87f7ede426afd3f54f137981aeeb6d80ece2aadcf"
  },
  "lottery_results": {
    "rows": 14649,
    "sha256": "379b7b51587bf5c8e2d5fac206099bc2b7ee3fd4feb2fbd68f57a1e230911e87"
  },
  "model_daily_eval": {
    "rows": 4572,
    "sha256": "3f71c595ee87b620182e0f2f28949f33de9916c489dc635167ff066a3e0e6517"
  }
}
```


## Profiles

- `MN_LANE_TEST_PROFILE`: `MN_LANE_TEST_PRIORITY`, V102 STRONG selector shadow, D-1/D-2 source pool, lose-only rescue, candidate universe coverage. Source formula: `MN_D = (MN+MT+MB) D-1 + (MN+MT+MB) D-2`. Exact model target: 20. Official impact: false.
- `MT_LANE_TEST_PROFILE`: `MT_PROTECT_MODE`, measurement only, false consensus audit, selector preservation audit. Source formula: `MT_D = (MN+MT+MB) D-1 + MN D`. D-2 wide pool disabled; V102 primary injection disabled. Exact model target: 20. Official impact: false.
- `MB_LANE_TEST_PROFILE`: `MB_SHADOW_FORENSIC_MODE`, `MB_AI_CHAIN_PRESERVATION_V1`, forensic V102 branch, same-day cross-region lose-only, LO1/LO2 diagnostic only, anti-herding audit. Source formula: `MB_D = (MN+MT+MB) D-1 + MN D + MT D`. Exact model target: 20. Official impact: false.

## Table Counts

```json
{
  "lane_test_region_profiles": 3,
  "bundle_universe_coverage_daily": 3076,
  "source_prize_strong_coverage": 3076,
  "rule_injection_contract": 3076,
  "candidate_drop_stage_daily": 102,
  "lane_test_lose_only_audit_daily": 90,
  "mb_ai_chain_preservation_v1": 30,
  "station_identity_runtime_audit": 69,
  "v10522_v102_strong_selector_shadow": 0
}
```
