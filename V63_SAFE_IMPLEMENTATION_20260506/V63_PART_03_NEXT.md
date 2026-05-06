# V63 Safe Implementation — Part 3 Next

## Next required checks

1. On 07/05, verify `prediction_trace.jsonl` rows include `latency_seconds` and `token_count`.
2. Re-run `model_latency_cost_audit_daily` materializer after new model calls.
3. Confirm `latency_available > 0`.
4. Only then start cost/time pruning analysis.

## Still not allowed

- No official model pruning.
- No official `/du-doan` change.
- No bundle voting/scoring change.
- No promotion of test methods.
