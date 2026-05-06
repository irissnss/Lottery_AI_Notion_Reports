# V52.4 MN/MT `/du-doan-test` Cutoff Spec

> Scope: test-lane only / no official output mutation / anti-leakage.

## Status

This spec enables `/du-doan-test` UI/API readiness for MN/MT without pretending that MN/MT already have independent test outputs.

Current implementation target:

- MN/MT show official baseline and measurement/readiness panels.
- MB remains the only region with persisted `du_doan_test_bundles` experiment outputs.
- MN/MT test output generation stays `DESIGN_ONLY` until runner/engine is generalized with the cutoff rules below.

## Allowed Sources

### MN

- Allowed before MN draw: D-1 all regions, historical `predictions`, historical `final_bundles`, historical `model_daily_eval`, historical shadow tables.
- Forbidden: MN(D) actual, MT(D), MB(D), hit-known selection, baseline-miss-known selection.

### MT

- Allowed after MN result is available and before MT draw: D-1 all regions, MN(D) actual/results, historical prediction/eval/shadow surfaces.
- Forbidden: MT(D) actual, MB(D), hit-known selection, baseline-miss-known selection.

### MB

- Allowed after MN+MT results are available and before MB draw: D-1 all regions, MN(D), MT(D), historical prediction/eval/shadow surfaces.
- Forbidden: MB(D) actual, hit-known selection, baseline-miss-known selection.

## Required Row Flags

Every future MN/MT test row must carry:

- `official_output=false`
- `output_impact=false`
- `test_only=1`
- `admin_only=1`
- `owner_approved=0`
- `output_eligible=0`
- `diagnostic_only=0` for realtime rows, `diagnostic_only=1` for post-closeout rows
- explicit `mode`: `REALTIME_AVAILABLE_ONLY` or `POST_CLOSEOUT_DIAGNOSTIC_FULL_25`

## Required Proof Before Calling Live-Parallel Full

- Runner timestamp before target actual.
- Source timestamp snapshot.
- Leakage audit row.
- Official hash unchanged.
- Post-closeout evaluator row.
- UI/API smoke.
- At least 3 clean manual closeouts before scheduler proposal.

## Current V52.4 Verdict

`MN_MT_TEST_LANE_DESIGN_ONLY`: UI/API can display readiness/measurement now, but MN/MT are not yet experiment-output lanes.
