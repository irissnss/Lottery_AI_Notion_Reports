# DU-DOAN-TEST V50 — Parallel Experiment Lane Completion

> Date: 2026-05-03  
> Mode: VPS-first / admin-only test lane / no official mutation  
> Final label: **`MANUAL_STAGE_0_CONFIRMED`**

## 1. Controller Scope

V50 completed the MB-only `/du-doan-test` lab lane without changing official `/du-doan`.

Hard locks held:
- No change to `generate_final_bundle()`.
- No writes to `final_bundles`.
- No writes to production `predictions`.
- No scoring, bundle voting, lane weight, model roster, production prompt, production AI chain, Option A, or TIER 3 unlock.
- Writes were limited to `du_doan_test_*`, `mb_experimental_preview_shadow`, and scheduler test markers.

## 2. Sync / Hash Evidence

- Pre-work live sync: `artifacts/live_sync/20260503_193743/manifest.json`.
- Post-VPS-run live sync: `artifacts/live_sync/20260503_201947/manifest.json`.
- Local pre-hash artifact: `artifacts/_du_doan_test_v50_pre_hash_20260503.txt`.
- VPS pre-hash artifact: `artifacts/_du_doan_test_v50_vps_pre_hash_20260503.txt`.
- VPS post-hash artifact: `artifacts/_du_doan_test_v50_post_hash_20260503.txt`.

Official hash result:
- `predictions`: unchanged (`4134 -> 4134`, same hash).
- `final_bundles`: unchanged (`195 -> 195`, same hash).
- `lottery_results`: unchanged (`14603 -> 14603`, same hash).
- `model_daily_eval`: unchanged (`4014 -> 4014`, same hash).
- `scheduler_logs`: changed (`113095 -> 113117`) from restart/test markers.

## 3. Current Status Classification

Current status is **`MANUAL_STAGE_0_CONFIRMED`**.

Reasons:
- Test lane has real schema, registry, runner, evaluator, scoreboard, leakage audit, API, UI.
- Today has VPS test rows for `2026-05-03`.
- Evaluator wrote closeout metrics and scoreboard.
- Official hashes are unchanged.
- Scheduler auto-wire is not enabled; no natural scheduler proof exists.

Not allowed to call `LIVE_PARALLEL_AUTO_FULL_CONFIRMED` yet because scheduler auto-wire proof is missing.

## 4. Official vs Test Separation

| Surface | Official lane | Test lane | Can write official? | Evidence | Verdict |
|---|---|---|---|---|---|
| UI | `/du-doan` / `web/frontend/du-doan.html` | `/du-doan-test` / `web/frontend/du-doan-test.html` | No | unauth `/du-doan=200`, `/du-doan-test=401` | separated |
| API | `/api/final-bundle` | `/api/du-doan-test/mb` | No | test API calls `require_admin()` and reads test tables | separated |
| Output | `final_bundles` | `du_doan_test_bundles` | No | official hash unchanged | safe |
| Runner | production scheduler/final bundle | `_du_doan_test_daily_runner.py` | No | writes test tables + test marker only | safe |
| Evaluator | production closeout semantics | `_du_doan_test_closeout_evaluator.py` | No | reads official/results, writes test scoreboards | safe |

## 5. V50 Components Created / Verified

- `web/backend/_du_doan_test_schema.py`: shared V50 schema, registry seed, source-hash helpers, leakage/conversion audit.
- `web/backend/_du_doan_test_daily_runner.py`: mode-aware manual runner with `--region`, `--mode`, `--dry-run`, source hashes, audit log, test scheduler markers.
- `web/backend/_du_doan_test_closeout_evaluator.py`: closeout evaluator for results, daily summary, experiment/model/method scoreboards.
- `web/backend/_du_doan_test_mb_engine.py`: registry enforcement, V50 metadata, mode labels, signal audit write.
- `web/backend/main.py`: `/api/du-doan-test/mb` now returns `mode`, `official`, `best_test`, `scoreboard_7d`, `scoreboard_14d`, `scoreboard_30d`, `model_contribution`, `method_contribution`, `leakage_audit`, `conversion_trace`, `experiment_registry`, and governance booleans.
- `web/frontend/du-doan-test.html`: UI now renders governance/mode, 7/14/30 scoreboards, model contribution, method contribution, and signal trace/leakage audit under the official-vs-test cards.

## 6. VPS Run Result

VPS runner:
- `created_runs=7`
- `created_bundles=7`
- `created_candidates=161`
- `created_model_contributions=161`
- `skipped_existing=0`
- `official_tables_touched=false`

VPS evaluator:
- `evaluated_runs=7`
- `actual_tail_count=24`
- `would_save_count=0`
- `would_break_count=2`
- `false_promotion_count=2`
- `lo2_to_bt_promotion_count=0`
- `official_tables_touched=false`

## 7. 2026-05-03 MB Result

Official MB:
- BT `48` = WIN.
- lo2 `["48", "89"]` = PARTIAL.

V50 test:
- Composite/tier/no-token matched official `48`, no lift today.
- AI-chain and prior-region selected `85`, both would break official today.
- Specialist has no BT candidate and is not counted as a break.

## 8. Method Truth

- AI test prompt: `AI_TEST_PROMPT_DESIGNED_NOT_EXECUTING`; table exists, rows = 0.
- No-token herd reduction: `LOGICAL_CLONE_ONLY`, not a real no-token rerun yet.
- Prior-region safe: no MB(D) actual used for selection; current verdict `PARTIALLY_SHARED_SIGNAL` / no leakage proof issue today.
- Tier-aware bundle: `PLACEHOLDER_ONLY`; no real `rule_tier/source_prize_tier/candidate_tier` fields yet.
- Tensor: still `TENSOR_NOT_OK_FOR_PRUNING` and `TENSOR_NOT_OK_FOR_REALTIME_SELECTION` due missing per-model duration/cost.

## 9. UI/API Smoke

- `GET /du-doan`: `200`.
- `GET /du-doan-test`: `401` unauth.
- `GET /api/du-doan-test/mb`: `401` unauth.
- `GET /api/health`: `200`.
- Admin API direct smoke returned success with:
  - date `2026-05-03`
  - mode `POST_CLOSEOUT_DIAGNOSTIC_FULL_25`
  - `count=7`
  - `score7=7`, `score14=7`, `score30=7`
  - `models=20`, `methods=7`, `leakage=7`
  - governance: `official_output=false`, `output_impact=false`, `test_only=true`, `admin_only=true`.

## 10. What Is Still Missing

- Scheduler auto-wire is not enabled.
- Realtime natural proof is missing.
- AI test prompt execution is still not active.
- Raw 25-model direct ingestion is not complete.
- No-token herd method is not a true independent rerun.
- Tier-aware method is still placeholder.
- Per-model latency/cost remains incomplete.

## 11. Final Verdict

**`MANUAL_STAGE_0_CONFIRMED`**.

V50 made `/du-doan-test` a real separate MB experiment lab with registry, runner, evaluator, scoreboards, leakage audit, API/UI surfacing, and source-hash proof. It is not yet `LIVE_PARALLEL_AUTO_FULL_CONFIRMED` because scheduler auto-wire and natural proof remain absent.
