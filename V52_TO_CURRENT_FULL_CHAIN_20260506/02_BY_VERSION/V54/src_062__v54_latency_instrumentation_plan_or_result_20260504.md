# V54 C-05 — Per-Model Latency Instrumentation Plan

> Status: `READY_FOR_LATENCY_INSTRUMENTATION_NOT_DEPLOYED`  
> Reason: current time is before MN scrape / MT-MB cascade on 2026-05-04; `gpt_analyzer.py` touches live model-call path, so V54 did not deploy it during live-sensitive window.

## Current Proof

- `model_latency_cost_audit_daily` remains 3273 rows.
- V53 finding remains true: 3273/3273 rows have `NO_PER_MODEL_DURATION`.
- `latency_seconds`, `token_count`, `cost_estimate` are still not reliable enough for pruning.

## Safe Patch Plan

Target files:

- `web/backend/gpt_analyzer.py`
- `web/backend/_materialize_v52_measurement_surfaces.py`

Add a measurement-only trace event around every model call:

```python
start = time.perf_counter()
started_at = datetime.now(timezone.utc).isoformat()
status = "OK"
error_type = None
token_count = None
cost_estimate = None
try:
    result = call_model(...)
    token_count = extract_usage_tokens(result)
finally:
    ended_at = datetime.now(timezone.utc).isoformat()
    latency_seconds = round(time.perf_counter() - start, 4)
    append_prediction_trace_event({
        "event": "per_model_latency",
        "date": date_str,
        "region": target_region,
        "model_name": model,
        "run_source": run_source,
        "run_label": run_label,
        "started_at": started_at,
        "ended_at": ended_at,
        "latency_seconds": latency_seconds,
        "status": status,
        "error_type": error_type,
        "token_count": token_count,
        "cost_estimate": cost_estimate,
        "measurement_only": 1,
        "output_eligible": 0,
    })
```

Then `_materialize_v52_measurement_surfaces.py` can read the event keys already supported by its parser:

- `latency_seconds`
- `duration_seconds`
- `duration_sec`
- `elapsed_seconds`
- `cost_estimate`
- `token_count`
- `tokens`
- `timeout_or_fallback`

## Deploy Gate

Deploy only after:

- Not inside 04:00/04:15/16:30/16:42/17:30/17:42/18:30/20:00 windows.
- `python -m py_compile web/backend/gpt_analyzer.py web/backend/_materialize_v52_measurement_surfaces.py`
- pre/post hash guard.
- route smoke.

## Verdict

`PRUNING_NOT_ALLOWED_NO_LATENCY` remains. No model pruning allowed in V54.
