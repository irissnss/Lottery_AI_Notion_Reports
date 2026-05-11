# V105.23 UI / Model Count / LO1-LO2 Audit

Status: **read-only audit, no official mutation**.

## Official 15/15

Backend truth:

- Official expected count comes from registry/DB via `get_expected_output_model_count`.
- Publish gate uses `_build_model_count_publish_gate(..., EXPECTED_MODEL_COUNT, EXPECTED_MODEL_COUNT)`.
- Current latest official final bundle at audit time: MN `model_count=15`.

UI truth:

- `/monitoring` region cards render runtime model count vs expected count from backend runtime-monitoring-center.
- Fallback UI value is `15` only when backend omits expected count.

## Lane Test 20/20

Backend truth:

- `TEST_LANE_FULL_BUDGET_TARGET=20`.
- `_select_test_lane_primary_with_full_budget()` requires contributor count >= 20 for primary.
- `/api/du-doan-test/{region}` builds test publish gate with min/max 20.

Current latest rows:

- MN: `MN_ADAPTIVE_BUDGET_SELECTOR_V1 model_count=20`.
- MT: `MT_ADAPTIVE_EXPLOIT_V1 model_count=4`.
- MB: `MB_ADAPTIVE_EXPLOIT_V1 model_count=5`.

Conclusion:

- MN can be exact 20/20 lane primary.
- MT/MB must remain `PREVIEW_BELOW_BUDGET` or diagnostic, not READY.

## MAIN_TEST_EQUALS_OFFICIAL

Backend truth:

- `main.py` `_v10519_lane_contract_for_region` sets `clone_warning="MAIN_TEST_EQUALS_OFFICIAL"` when normalized test BT equals official BT.
- It is surfaced through admin test-lane readiness/diff APIs.

UI gap:

- `du-doan-test.html` uses `primary_differs_from_baseline_bt`, challenger strip, and copy warning, but does not directly render the exact `MAIN_TEST_EQUALS_OFFICIAL` marker string.
- V105.23 UI follow-up should wire the exact marker into `/du-doan-test` for SSOT clarity.

## Region Badges

`monitoring.html` V105.22 panel renders:

- `MN_PRIORITY`.
- `MT_PROTECT`.
- `MB_FORENSIC`.
- exact model count `/20`.
- source-pool formula.
- V102 status and LO2 weight.

Gap:

- Smaller hero chips named `laneMN/laneMT/laneMB` refer to configured lane weights, not exact 20/20 lane readiness. Naming can confuse owner review.

## History / Metrics

Backend:

- `api_admin_test_lane_history`.
- `api_admin_test_lane_metrics`.
- `_du_doan_test_engine.py` writes only `du_doan_test_*` tables.
- `_du_doan_test_closeout_evaluator.py` computes `would_save`, `would_break`, `false_promotion`, `delta_bt`, `delta_lo2`.

Frontend:

- `du-doan-test.html` fetches admin test-lane history and metrics.
- `settings.js` does not call test-lane/readiness/lo1-lo2 surfaces; this is acceptable because it is settings/auth/scheduler/rules focused.

## LO1/LO2 Lane-Only Weights

Backend truth:

- `_materialize_du_doan_test_model_budget.py`: `LANE_TEST_LO2_POS_WEIGHT_BY_REGION`.
- `_materialize_adaptive_exploit_v1.py`: same map.
- `main.py`: `LANE_TEST_AUDIT_LO2_WEIGHT_BY_REGION` for read-only audit.

Weights:

- MB: `0.95`.
- MN: `0.55`.
- MT: `0.55`.

Gap:

- `/api/admin/lo1-lo2-audit/{region}` exists, but `du-doan-test.html` does not have a dedicated LO1/LO2 panel.

## P&L Tracker

`pnl-tracker.html` is admin P&L only. It has station identity note and station canonicalization support, but it is intentionally not a lane-test/model-count/lo1-lo2 dashboard.

## Actionable UI Follow-Up

- Render exact `MAIN_TEST_EQUALS_OFFICIAL` marker on `/du-doan-test`.
- Rename or clarify `/monitoring` hero `laneMN/laneMT/laneMB` chips so they are not mistaken for 20/20 lane readiness.
- Add a read-only LO1/LO2 audit panel on `/du-doan-test` or `/monitoring`.
- Add V105.23 source-pool gap panel: source_pool -> prompt -> rank -> top2 -> bundle -> UI.
