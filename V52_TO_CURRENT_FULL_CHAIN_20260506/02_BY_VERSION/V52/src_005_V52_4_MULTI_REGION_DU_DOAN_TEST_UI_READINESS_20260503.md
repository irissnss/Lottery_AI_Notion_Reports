# V52.4 Multi-Region `/du-doan-test` UI Readiness

> Date: 2026-05-03  
> Mode: test-lane UI/API only / MN-MT design-only / no official mutation  
> Live sync after deploy: `artifacts/live_sync/20260503_222141/manifest.json`

## What Changed

`/du-doan-test` now has region tabs and window filters:

- MN test/readiness
- MT test/readiness
- MB test
- Window filters: 7d / 14d / 30d / 60d

API:

- Existing MB endpoint remains: `/api/du-doan-test/mb`
- New read-only multi-region endpoint: `/api/du-doan-test/{region}`
  - `/api/du-doan-test/mn`
  - `/api/du-doan-test/mt`
  - `/api/du-doan-test/mb`

MN/MT are intentionally `DESIGN_ONLY` for test-output generation. They show official baseline + V52 measurement/readiness panels, not fake test predictions.

## Cutoff Spec

Spec artifact:

- `artifacts/phase_checkpoints/V52_4_MN_MT_TEST_LANE_CUTOFF_SPEC_20260503.md`

Rules:

- MN: D-1 only; no MN(D) actual.
- MT: D-1 + MN(D) after MN result; no MT(D) actual.
- MB: D-1 + MN(D)+MT(D); no MB(D) actual.

## Smoke

Unauth:

- `/du-doan`: 200
- `/du-doan-test`: 401
- `/api/du-doan-test/mn`: 401
- `/api/du-doan-test/mt`: 401
- `/api/du-doan-test/mb`: 401
- `/api/health`: 200

Admin direct API:

```json
{
  "mn": {"success": true, "mode": "MN_MT_TEST_LANE_DESIGN_ONLY", "has_v52": true, "test_bundle": false, "cutoff": "DESIGN_ONLY"},
  "mt": {"success": true, "mode": "MN_MT_TEST_LANE_DESIGN_ONLY", "has_v52": true, "test_bundle": false, "cutoff": "DESIGN_ONLY"},
  "mb": {"success": true, "mode": "POST_CLOSEOUT_DIAGNOSTIC_FULL_25", "has_v52": true, "test_bundle": true}
}
```

## Hash Guard

Pre: `artifacts/_v52_4_pre_hash_20260503.txt`  
Post: `artifacts/_v52_4_post_hash_20260503.txt`

Official/source:

- `predictions`: unchanged
- `final_bundles`: unchanged
- `lottery_results`: unchanged
- `model_daily_eval`: unchanged
- `scheduler_logs`: changed only from service restart

Measurement/test tables:

- `mt_model_hit_output_drop_shadow`: unchanged
- `loz_selector_shadow`: unchanged
- `model_latency_cost_audit_daily`: unchanged
- `du_doan_test_runs/bundles/results`: unchanged

## Verdict

V52.4 makes `/du-doan-test` multi-region visible without pretending MN/MT are live experiment-output lanes. This is the correct anti-leakage step before any MN/MT test runner.
