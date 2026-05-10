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
