# V52.4.1 `/du-doan-test` UI Loading Fix

> Date: 2026-05-03  
> Mode: test-lane UI only / no official mutation

## Symptom

Owner reported `/du-doan-test` stuck at "Đang tải dự đoán test..." after V52.4 deploy.

## Root Cause

V52.4 introduced `renderRegionControls(data)` which generated window-filter buttons with inline `onclick="setWindowDays(\\'7\\')"`. After string concatenation, the resulting HTML attribute contained literal backslashes, which would throw `SyntaxError` when clicked. More critically, the V52.4 `render(data)` function had no try/catch, so any single panel exception left the whole page stuck on the loading state because `app.innerHTML` was never reassigned.

## Fix

- Replaced inline `onclick` strings with `data-window` attributes plus `addEventListener` after `innerHTML` write.
- Wrapped each render section with a `safeRender(fn, label, data)` helper so a single broken panel renders an in-place error chip instead of breaking the page.
- Added a fatal try/catch around the whole `render(data)` body that surfaces JS errors to the user.
- Bumped cache buster on `/du-doan` admin link to `?v=20260503-v52-4-multi`.
- Added live region title that updates per tab (`MN`, `MT`, `MB`).

## Smoke

After deploy:

- `/du-doan` HTTP `200`
- `/du-doan-test` HTTP `401` unauth
- `/api/du-doan-test/mn` HTTP `401` unauth
- `/api/du-doan-test/mt` HTTP `401` unauth
- `/api/du-doan-test/mb` HTTP `401` unauth

Direct admin API payloads match the expected shape:

- MN/MT: `success=true`, `mode=MN_MT_TEST_LANE_DESIGN_ONLY`, `test_bundle=null`, no scoreboards/leakage rows.
- MB: `success=true`, `mode=POST_CLOSEOUT_DIAGNOSTIC_FULL_25`, `test_bundle=true`, 7 experiments, 7 leakage rows, 7/14/30 scoreboards, V52 measurements.

## Owner Action

Hard refresh the page (Ctrl+Shift+R or open in private window) so the new HTML/JS replaces the cached `?v=20260503-v48-1-row` version.

## Hash Guard

V52.4.1 only edits `web/frontend/du-doan-test.html` and `web/frontend/du-doan.html`. No DB writes. Source tables `predictions`, `final_bundles`, `lottery_results`, and `model_daily_eval` remain untouched.
