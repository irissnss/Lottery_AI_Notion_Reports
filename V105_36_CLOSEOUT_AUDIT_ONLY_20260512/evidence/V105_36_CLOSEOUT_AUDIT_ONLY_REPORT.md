# V105.36 — Closeout Audit Only Report

Generated: 2026-05-12 22:15 VN

## Executive Verdict

V105.36 is **closeout audit only**, not natural-verify pass.

Labels:

- `V105_36_CLOSEOUT_AUDIT_ONLY`
- `NATURAL_VERIFY_PENDING`
- `MT_OUTPUT_ROWS_PENDING`
- `PROVIDER_MANUAL_CALL_0`
- `TRIGGERS_UNCHANGED`
- `OFFICIAL_SCORING_UNCHANGED`
- `WR_BT_FILTER_PRESERVED`
- `OFFICIAL_ROSTER_PRESERVED`
- `MB_OFFICIAL_WIN_LANE_TEST_LOSE_FORENSIC_OPEN`
- `MODEL_HEALTH_SCOREBOARD_DRAFTED`
- `DIRECT_KEY_AB_SHADOW_PENDING`

## Evidence

- Live sync: `artifacts/live_sync/20260512_220825/manifest.json`
- Endpoint captures: `artifacts/v105_37_final_MN.json`, `artifacts/v105_37_final_MT.json`, `artifacts/v105_37_final_MB.json`
- Closeout audit: `artifacts/v105_36_closeout_audit.json`
- DB summary: `artifacts/v105_36_db_summary.json`
- Model health + routing draft: `artifacts/v105_37_stability_quality/v10537_stability_quality_audit.json`
- Provider route scoreboard: `artifacts/v105_37_stability_quality/provider_route_scoreboard.json`
- Direct vs OpenRouter A/B plan: `artifacts/v105_37_stability_quality/DIRECT_VS_OPENROUTER_AB_SHADOW_PLAN.md`

## Public SSOT Status

GitHub raw public remains V105.35:

| Field | Value |
|---|---|
| latest_version | V105.35 |
| latest_folder | V105_35_OFFICIAL_PUBLISH_GATE_SEMANTIC_FIX_20260512 |
| latest_report | V105_35_OFFICIAL_PUBLISH_GATE_SEMANTIC_FIX_20260512/evidence/V105_35_OFFICIAL_PUBLISH_GATE_SEMANTIC_FIX_REPORT.md |
| last_public_refresh_at_vn | 2026-05-12T19:35:00+07:00 |
| provider_manual_ai_called | false |
| provider_call_count | 0 |
| official_touched | true, because V105.35 changed official API/UI readiness metadata semantics; prompt/scoring/selector/voting/roster were unchanged |

Status: `PUBLIC_SSOT_LAG_FOR_V10536_ARTIFACTS`.

## Natural Verify Matrix

| Region | Output Rows | Scoreable | Quality Filtered | Diagnostic Empty | Publish Ready | Gate Reason | Verdict |
|---|---:|---:|---|---|---|---|---|
| MN | 15/15 | 15/15 | none | none | true | OUTPUT_ELIGIBLE_ROWS_READY | clean snapshot, not full pass |
| MT | 10/15 | 9/15 | none | none | false | WAIT_OUTPUT_ELIGIBLE_ROW_COUNT | NATURAL_VERIFY_PENDING |
| MB | 15/15 | 13/15 | `claude-opus-4-20250514`, `smart-ensemble` | none | true | OUTPUT_ELIGIBLE_ROWS_READY_WITH_QUALITY_WARNING | clean snapshot, not full pass |

No closed-file markers appeared after the final V105.35 restart window. The live day still contains earlier closed-file evidence, so V105.36 cannot be natural verify pass.

## MT 5-Model Stability

| Model | Row | Failure Class | Evidence | Verdict |
|---|---|---|---|---|
| `gpt-5-mini` | none | CLOSED_FILE_REGRESSION_P0 | natural scheduled call ended with `I/O operation on closed file` | keep MT pending |
| `claude-sonnet-4-6` | none | CLOSED_FILE_REGRESSION_P0 | natural scheduled call ended with `I/O operation on closed file` | keep MT pending |
| `gemini-2.5-flash` | none | CLOSED_FILE_REGRESSION_P0 | natural scheduled call ended with `I/O operation on closed file` | keep MT pending |
| `claude-opus-4-20250514` | none | CLOSED_FILE_REGRESSION_P0 | natural scheduled call ended with `I/O operation on closed file` | keep MT pending |
| `deepseek-reasoner` | none | EXCEPTION_AFTER_SOFT_CONTINUE | soft continue then delayed exception | keep MT pending |

No manual refill was run. No fake row was inserted.

## MB Official Win / Lane-Test Lose

MB official BT `34` is a win. Actual MB tails include `34` and do not include `36`.

| Candidate | Lane | Voters | Rank | Actual Hit | Action |
|---|---|---|---:|---|---|
| `34` | official/baseline | `random-forest`, `xgboost`, `meta-learning`, `combo-no-token`, `smart-ml` | 1 | true | keep official |
| `36` | lane-test/challenger | `deepseek-reasoner`, `gemini-2.5-pro`, `gemini-2.5-flash`, `gpt-5-mini` | 2 | false | DO_NOT_PROMOTE_MB_CHALLENGER |

Experiment losing means fix experiment, not official.

## V105.37 Draft Outputs

Model health scoreboard and direct-vs-OpenRouter A/B plan were generated as read-only draft evidence. They are not runtime changes and do not call providers.

Promotion or routing changes require owner approval and at least 7 natural shadow days, preferably 14 days for official-impact decisions.
