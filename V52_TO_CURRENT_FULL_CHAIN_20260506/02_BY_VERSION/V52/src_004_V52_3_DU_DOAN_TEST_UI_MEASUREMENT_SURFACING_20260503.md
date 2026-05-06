# V52.3 `/du-doan-test` Measurement Surfacing

> Date: 2026-05-03  
> Mode: test-lane UI/API only / no official output mutation  
> Live sync after deploy: `artifacts/live_sync/20260503_221017/manifest.json`

## What Changed

Surfaced the V52.2 measurement tables in the admin-only `/du-doan-test` API/UI.

API `/api/du-doan-test/mb` now includes:

- `v52_measurements.mt_drop_rollup`
- `v52_measurements.mt_drop_recent`
- `v52_measurements.loz_selector_rollup`
- `v52_measurements.latency_cost_rollup`

UI `web/frontend/du-doan-test.html` now renders:

- MT dropped actual tails for the selected date.
- MT drop rollups for 7d / 30d / 60d.
- Loz selector rollups for 14d / 30d / 60d.
- Latency/cost availability rollup for 60d.

## Smoke

- `/du-doan`: `200`
- `/du-doan-test` unauth: `401`
- `/api/du-doan-test/mb` unauth: `401`
- `/api/health`: `200`
- Admin API direct smoke: `has_v52=true`, `mt_drop_60=4`, `loz_60=3`, `latency_60=1`.

## Hash Guard

Pre: `artifacts/_v52_3_pre_hash_20260503.txt`  
Post: `artifacts/_v52_3_post_hash_20260503.txt`

Official/source:

- `predictions`: unchanged
- `final_bundles`: unchanged
- `lottery_results`: unchanged
- `model_daily_eval`: unchanged
- `scheduler_logs`: changed only from service restart (`113122 -> 113134`)

Measurement tables:

- `mt_model_hit_output_drop_shadow`: unchanged (`301`)
- `loz_selector_shadow`: unchanged (`3273`)
- `model_latency_cost_audit_daily`: unchanged (`3273`)

## Verdict

This is UI/API surfacing only. It makes the rolling measurement evidence visible on the test lane without changing official output.
