# V105.15-18 Lane-Test Audit + Doctrine Pack

**Date:** 2026-05-10  
**Private source commit:** `c97e4d021b40c040634e7f7004210efb8a6a9c14` (`irissnss/Lottery_AI_Test`, private)  
**Runtime target:** VPS `/root/Lottery_AI_Test`, `lottery.service` active after restart at 21:11 VN  
**Scope:** lane-test / shadow measurement only unless explicitly stated.

## Public Summary

V105.15 through V105.18 closed four owner-facing issues:

1. AI model calls now use `90s` soft-continue and `300s` hard timeout. Late results between those limits are still accepted, so one slow model does not block the lane.
2. Official `/du-doan` remains fixed at exactly `15/15` output-eligible contributors. It is never topped up by shadow models.
3. `/du-doan-test` now publishes only from a full `20/20` lane-test method. Under-budget rows remain preview-only.
4. Shadow auto-eval AI models now receive the lane-test doctrine pack: PB-18 shadow context, phase-first contract, D-1 final-bundle carry/lag context, prior-region same-day tails, MN D-2 union pool, and gated lag-1 signals.
5. Lane-test aggregation now uses per-region lo2 position weights: MB heavy, MN/MT light.

## Repository Separation

- **Private repo (`Lottery_AI_Test`)**: source code, scheduler/runtime changes, private changelog, SSOT, FU tracker, smoke scripts.
- **Public repo (`Lottery_AI_Notion_Reports`)**: this report only. It contains no database, no JSONL trace, no API keys, no VPS secrets, and no runtime artifacts.

## Private Code Changes

Private commit `c97e4d0` includes:

- `web/backend/scheduler.py`
- `web/backend/gpt_analyzer.py`
- `web/backend/main.py`
- `web/backend/_materialize_du_doan_test_model_budget.py`
- `web/backend/_materialize_adaptive_exploit_v1.py`
- `web/frontend/du-doan-test.html`
- `CHANGELOG.md`
- `docs/CURRENT_TRUTH_SSOT.md`
- `docs/FOLLOW_UP_TRACKER.md`
- smoke/audit artifacts for V105.16 and V105.18

Runtime hygiene was corrected in the same commit:

- `web/backend/prediction_trace.jsonl` is no longer tracked.
- `.gitignore` excludes `*.jsonl` and `artifacts/live_sync/`.

## V105.17 Shadow Doctrine Pack

`scheduler._run_shadow_auto_eval()` now calls:

```text
analyze_and_predict(..., lane_test_shadow_pack=True)
```

That flag is not used by official `/du-doan`.

When enabled:

- `build_context_pack(..., shadow_mode=True)` is forced for all shadow-auto-eval models, not just the old `SHADOW_GATE_MODELS` cohort.
- `PHASE_FIRST_JSON_CONTRACT` is enabled for the lane-test cohort.
- `_build_lane_test_shadow_doctrine_addon()` appends:
  - D-1 final-bundle BT + status.
  - Prior same-day region tails (`MN -> MT -> MB` sequence).
  - MN D-2 union pool from MN+MT+MB.
  - Gated lag-1 adaptive signals from `lag1_adaptive_exploit_signal_shadow`, if present.

Live journal evidence after deploy:

```text
[CONTEXT_PACK] [LANE-TEST-SHADOW-CTX] Injected 14574 chars + REASONING_RULEBOOK (model=qwen3.6-plus)
[CONTEXT_PACK] [LANE-TEST-SHADOW-CTX] Injected 14574 chars + REASONING_RULEBOOK (model=qwen3-coder)
[CONTEXT_PACK] [LANE-TEST-SHADOW-CTX] Injected 14574 chars + REASONING_RULEBOOK (model=qwen3-max-thinking)
```

MB shadow summary after deploy:

```text
success=12 error=1 persisted=12 missing_rows=['gemma-4-31b'] empty_rows=[]
```

The one error was Google Gemini quota `429 RESOURCE_EXHAUSTED`, not a code regression.

## V105.18 Lane-Test lo2 Weight

Lane-test materializers now share:

```text
LANE_TEST_LO2_POS_WEIGHT_BY_REGION = {
  "MB": 0.95,
  "MN": 0.55,
  "MT": 0.55,
}
```

Top1 position weight remains `1.0`.

Applied only in:

- `_materialize_du_doan_test_model_budget.py` for `*_ADAPTIVE_BUDGET_SELECTOR_V1`.
- `_materialize_adaptive_exploit_v1.py` step 5, `same_region_lo2_lag1_final_bundle`, for `*_ADAPTIVE_EXPLOIT_V1`.

Not applied to:

- `combo_super`
- `generate_final_bundle`
- official `/du-doan`
- `final_bundles`

## Audit Endpoint

`/api/admin/lo1-lo2-audit/{region}?days=30` is now schema `lo1_lo2_audit_v2`.

It compares:

- `official`
- `top1_only`
- `mixed_weighted` (`top1=2`, `top2=1`)
- `lane_test_region_weighted` (`top1=1`, `top2=MB 0.95 / MN-MT 0.55`)

The endpoint is read-only and does not change scoring.

## VPS Smoke Results

Smoke script:

```text
/root/Lottery_AI_Test/venv/bin/python3 /root/Lottery_AI_Test/web/backend/_v105_18_vps_smoke.py
```

30-day audit summary:

| Region | lo2 weight | official BT | official lo2 | top1 BT | top1 lo2 | mixed BT | mixed lo2 | lane-test BT | lane-test lo2 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| MN | 0.55 | 50.00 | 26.67 | 50.00 | 23.33 | 53.33 | 30.00 | 53.33 | 30.00 |
| MT | 0.55 | 46.67 | 13.33 | 43.33 | 16.67 | 46.67 | 13.33 | 46.67 | 16.67 |
| MB | 0.95 | 20.00 | 6.67 | 10.00 | 0.00 | 16.67 | 0.00 | 16.67 | 3.33 |

Interpretation:

- MB lo2 improved from `0.00%` under fixed mixed weighting to `3.33%` under lane-test regional weighting.
- MT lo2 also improved from `13.33%` to `16.67%`.
- MN stayed stable at `53.33% / 30.00%`.

## Verification

- Local `py_compile`: passed for modified backend files.
- Local smoke `artifacts/v105_18_local_smoke.py`: 8/8 passed.
- VPS `py_compile`: passed.
- VPS service restart: active.
- `/api/health`: HTTP 200.
- Journal check: no new closed-file crash or traceback caused by this change.

## Follow-up

Track for 7 live days:

- MB `lane_test_region_weighted.lo2_pct` vs `mixed_weighted.lo2_pct`.
- MN/MT BT stability under reduced lo2 position weight.
- Shadow eval success ratio after the full lane-test doctrine pack.

