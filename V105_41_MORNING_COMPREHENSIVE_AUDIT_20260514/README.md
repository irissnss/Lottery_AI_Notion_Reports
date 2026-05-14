# V105.41 — Morning Comprehensive Audit (2026-05-14)

This wrapper packages the comprehensive morning audit produced at the start of the 2026-05-14 live cycle, together with deep-dive analytical reports owners asked for so external AI tools can analyze the system end-to-end.

## Status

- Wrapper version: `V105.41`
- Owner directive: comprehensive end-of-cycle audit + deep dive into measurement, methodology, ML, rules, prompt, per-model behavior.
- Mode: read-only, no runtime change, no provider/manual AI call, no trigger change, no restart.
- Day-control hard lock still active (`V105.40 day-control`). V105.40 expansion patch remains owner-gated.
- `NATURAL_VERIFY_PARTIAL_PASS_NOT_FULL_PASS` because shadow lane still emits 1 closed-file diagnostic this morning, plus 14 closed-file events recorded yesterday across multiple paths.

## Contents

| File | Purpose |
|---|---|
| `evidence/V105_41_MORNING_COMPREHENSIVE_REPORT.md` | Day-control morning audit — live sync, smoke endpoints, yesterday closeout, today MN cycle, MT/MB pending, regression scope. |
| `evidence/V105_41_MODEL_HEALTH_AND_METHODOLOGY_DEEP_DIVE.md` | 30-day model performance scoreboard, per-model hit rate / latency / failure class / recommendation, ML pipeline overview, prompt structure, rule engine, scoring/voting pipeline, owner-locked invariants. |
| `evidence/V105_41_RUNTIME_STABILITY_AND_GOVERNANCE.md` | Runtime stability story (V105.30d → V105.40), closed-file regression map, V105.40 expansion patch plan, governance lock list, follow-up tracker excerpt. |

## How to read

1. Start with `V105_41_MORNING_COMPREHENSIVE_REPORT.md` for the current truth and live state.
2. Read `V105_41_MODEL_HEALTH_AND_METHODOLOGY_DEEP_DIVE.md` for analytical commentary on each model, prompt mechanism, rules engine, and recommendations.
3. Use `V105_41_RUNTIME_STABILITY_AND_GOVERNANCE.md` for the runtime regression history, P0 watch list, and pending owner decisions.

## Hard locks preserved

- Official `/du-doan` publishes only the fixed `15/15` output-eligible roster.
- Official scoring / prompt / selector / bundle voting / WR/BT filter / model roster / trigger timing — **unchanged**.
- Lane-test reserve-fill remains test-only.
- Official reserve-fill remains HOLD.
- Timeout values remain `AI_MODEL_SOFT_CONTINUE_SEC=90`, `AI_MODEL_HARD_TIMEOUT_SEC=300`. V105.38 500s extended-grace is proposal only.
- No provider / manual AI call.

## Key labels

`V105_41_MORNING_COMPREHENSIVE_AUDIT` · `NATURAL_VERIFY_PARTIAL_PASS_NOT_FULL_PASS` · `V105_40_PATCH_NOT_DEPLOYED` · `MT_2026_05_13_BT_92_WIN` · `MB_2026_05_13_BT_32_LOSE_NO_DIVERGENCE` · `MN_2026_05_14_BT_16_ACTIVE_STRONG` · `OFFICIAL_PUBLISH_PATH_UNAFFECTED` · `WR_BT_FILTER_PRESERVED` · `TIMEOUT_90_300_PRESERVED` · `V105_38_TIMEOUT_500_PROPOSAL_ONLY` · `V105_40_SAFE_STDIO_SHADOW_PROPOSAL_ONLY` · `V105_40_SCOPE_FURTHER_EXTENDED` · `PROVIDER_MANUAL_CALL_0` · `TRIGGERS_UNCHANGED` · `OFFICIAL_RESERVE_HOLD` · `LANE_TEST_RESERVE_ONLY`.
