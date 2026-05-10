# NOTION_SYNC_PAYLOAD_V105_20

Notion page: https://www.notion.so/V105-20-Dual-Lane-Stabilization-Test-Lane-Measurement-35c1d3859bf881e7b20adf49057d3da4

Synced bullets match V105.20 dual-lane stabilization evidence.

# V105.20 Dual-Lane Stabilization + Real Test-Lane Improvement Pass

DB Source: VPS_LIVE_DB (`artifacts/v105_20_dual_lane_measurement/v105_20_dual_lane_probe.json`)

## 1. SSOT matrix

- Private latest before V105.20: V105.19 commit `c63e3e1`; V105.20 local changes pending commit at report generation.
- Public latest before V105.20: V105.19 raw pointer returns 200; V105.20 folder created here.
- Notion latest: V105.20 page `35c1d385-9bf8-81e7-b20a-df49057d3da4` under canonical `Lottery_AI_Test`.
- VPS latest: service active, runtime `V20.3.36`, V105.20 files deployed.

## 2. Official stability proof

- `/api/health=200`, `/api/status=200`, `/du-doan=200`, `/api/final-bundle` MN/MT/MB=200.
- Official model counts MN/MT/MB are exact `15/15`.
- `generate_final_bundle()`, production scoring, official selector, and official writer tables were not changed.

## 3. Lane test 20/20 proof

- MN: READY `20/20`, primary `MN_ADAPTIVE_BUDGET_SELECTOR_V1`, challenger `82`.
- MT: READY `20/20`, primary `MT_ADAPTIVE_BUDGET_SELECTOR_V1`, challenger `39`.
- MB: READY `20/20`, primary `MB_ADAPTIVE_BUDGET_SELECTOR_V1`, challenger `78`.

## 4. Challenger / anti-clone proof

- When primary equals official, API marker is now exact `MAIN_TEST_EQUALS_OFFICIAL`.
- Challenger panel remains separate and is not official output.

## 5. Improvement pack applied

- V101 source-pool formulas are present: MN D-1+D-2 all regions; MT all D-1 + MN D; MB all D-1 + MN D + MT D.
- Lose-only rescue is active in V67 for D-1 and same-day upstream sources.
- V102 `STRONG` / `PROMPT_REVIEW_STRONG` now enters `ADAPTIVE_EXPLOIT_V1` only if non-gan core + `source_layer_count >= 2`.
- Gan thresholds match owner spec: MB normal 30 / special 15; MN/MT normal 15 / special 7.

## 6. Measurement tables

# V105.20 Dual-Lane Probe

- Generated: `2026-05-10T22:51:27+07:00`
- DB source: `VPS_LIVE_DB`
- Target date: `2026-05-10`
- Sample warning: `NONE`

## Endpoint Smoke
- `health`: `200` ok=`True`
- `status`: `200` ok=`True`
- `du_doan`: `200` ok=`True`
- `final_bundle_MN`: `200` ok=`True`
- `final_bundle_MT`: `200` ok=`True`
- `final_bundle_MB`: `200` ok=`True`

## Official Hashes
- `predictions` rows=`4708` sha256=`3cb0a5634fbd2e0d21f6d2503f8081f6edb336b1fd8f52d93575f8c4d209746f`
- `final_bundles` rows=`216` sha256=`8317fce623595bc753acdf827f6035827829c062df623a5dcb02f00c0916297a`
- `lottery_results` rows=`14649` sha256=`379b7b51587bf5c8e2d5fac206099bc2b7ee3fd4feb2fbd68f57a1e230911e87`
- `model_daily_eval` rows=`4572` sha256=`3f71c595ee87b620182e0f2f28949f33de9916c489dc635167ff066a3e0e6517`

## Lane Contract
- `MN` state=`READY` count=`20/20` method=`MN_ADAPTIVE_BUDGET_SELECTOR_V1` clone=`MAIN_TEST_EQUALS_OFFICIAL` challenger=`82`
- `MT` state=`READY` count=`20/20` method=`MT_ADAPTIVE_BUDGET_SELECTOR_V1` clone=`MAIN_TEST_EQUALS_OFFICIAL` challenger=`39`
- `MB` state=`READY` count=`20/20` method=`MB_ADAPTIVE_BUDGET_SELECTOR_V1` clone=`MAIN_TEST_EQUALS_OFFICIAL` challenger=`78`

## Adaptive Exploit Sources
- rows=`17` by_source=`{'lo2_lag1_final_bundle': 2, 'same_region_lag1_final_bundle': 1, 'per_model_lag1': 12, 'cross_region_nextday': 2, 'cross_region_sameday': 2}`

## Measurement Summary
- `official/MN` n=`30` BT=`50.0%` lo2=`66.67%` weighted=`1.0133` save=`0` break=`0` false_promo=`0`
- `official/MT` n=`30` BT=`46.67%` lo2=`70.0%` weighted=`0.925` save=`0` break=`0` false_promo=`0`
- `official/MB` n=`30` BT=`20.0%` lo2=`43.33%` weighted=`0.675` save=`0` break=`0` false_promo=`0`
- `lane_test/MN` n=`30` BT=`60.0%` lo2=`70.0%` weighted=`1.1317` save=`3` break=`0` false_promo=`0`
- `lane_test/MT` n=`30` BT=`36.67%` lo2=`66.67%` weighted=`0.825` save=`3` break=`6` false_promo=`6`
- `lane_test/MB` n=`30` BT=`23.33%` lo2=`36.67%` weighted=`0.645` save=`5` break=`4` false_promo=`4`
- `challenger/MN` n=`30` BT=`20.0%` lo2=`26.67%` weighted=`0.365` save=`3` break=`12` false_promo=`12`
- `challenger/MT` n=`30` BT=`23.33%` lo2=`33.33%` weighted=`0.4533` save=`1` break=`8` false_promo=`8`
- `challenger/MB` n=`30` BT=`6.67%` lo2=`10.0%` weighted=`0.225` save=`1` break=`5` false_promo=`5`


## 7. Runtime logs

Post-deploy journal scan since 22:50 VN returned no `closed file`, `traceback`, `exception`, or `error`.

## 8. Official hash proof

```json
{
  "predictions": {
    "rows": 4708,
    "sha256": "3cb0a5634fbd2e0d21f6d2503f8081f6edb336b1fd8f52d93575f8c4d209746f"
  },
  "final_bundles": {
    "rows": 216,
    "sha256": "8317fce623595bc753acdf827f6035827829c062df623a5dcb02f00c0916297a"
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

## 9. Public/private commits

Pending at report-generation time; final session report records pushed commit IDs.

## 10. Notion page IDs

- `V105.20 Dual-Lane Stabilization + Test-Lane Measurement`: `35c1d385-9bf8-81e7-b20a-df49057d3da4`

## 11. 24h / 7d / 14d plan

- 24h: watch natural scheduler, exact 15/15 official, exact 20/20 lane, and clone marker.
- 7d: compare lane weighted lo1+lo2 by region/weekday/method/model/rule; block MT/MB if would-break grows.
- 14d: consider MN-only test-lane promotion step only if sample stays positive and false-promotion remains low.

## Blockers

Drive reports Báo Cáo 18, Báo Cáo 19, Phân Tích Đánh Giá 4 were requested but are not present in local workspace and no Drive MCP/direct files are available in this session. Notion V105.19 OWNER REQUIREMENTS SSOT was read successfully.
