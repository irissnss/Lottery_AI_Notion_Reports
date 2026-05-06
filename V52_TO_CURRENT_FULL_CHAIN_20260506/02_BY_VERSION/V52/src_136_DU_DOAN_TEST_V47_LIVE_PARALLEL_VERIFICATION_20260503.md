# DU-DOAN-TEST V47 LIVE PARALLEL VERIFICATION
# 2026-05-03 ? V20.3.37.47

> Mode: VPS-first / verify-before-claim / admin-only test lane / no production mutation.
> Sync: `artifacts/live_sync/20260503_010728/manifest.json`.

## 1. Executive summary

V46 claims are mostly verified, but with important corrections. `/du-doan-test` exists, is admin-gated, has separate `du_doan_test_*` tables, and has MB test rows/history/eval for 2026-05-02. However, it is **not yet auto-running daily**; it is **manual live parallel** via CLI runner. It also does **not yet truly store/use all 25 models in the test contribution layer**: official prediction source has 25 MB models, but current test contribution rows include 14 voter models from the ranked preview payload. AI test prompt duplication is **not implemented/executing**.

## 2. V46 claims verified / not verified

Verified: route/API exist, admin gate works, six `du_doan_test_*` tables exist, 7 runs/bundles/results exist, 147 candidates/contributions exist, official MB 43/lo2 43-91 remains unchanged, test rows have official_output=false/output_impact=false.

Corrected: live parallel is manual, not scheduler auto; 25-model claim is partial; AI test prompt is design-only; test engine reads preview rows rather than raw 25 predictions directly.

## 3. Official `/du-doan` integrity

Official `/du-doan` smoke returned 200. Official MB 2026-05-02 remains BT `43` LOSE and lo2 `[43,91]` PARTIAL. Source hashes for predictions/final_bundles/lottery_results/model_daily_eval are unchanged.

## 4. `/du-doan-test` access control

Unauth `/du-doan-test` returns 401. Unauth `/api/du-doan-test/mb` returns 401. This proves server-side admin/session protection, not only hidden UI.

## 5. End-to-end data flow

Official path: `/du-doan` ? `/api/final-bundle` ? `final_bundles`.

Test path: `/du-doan-test` ? `/api/du-doan-test/mb` ? `mb_experimental_preview_shadow` + `du_doan_test_*`.

The API reads test history from `du_doan_test_bundles/results`.

## 6. Schema audit

| table | rows | missing |
|---|---|---|
| du_doan_test_runs | 7 | none |
| du_doan_test_candidates | 147 | none |
| du_doan_test_bundles | 7 | none |
| du_doan_test_results | 7 | none |
| du_doan_test_model_contribution | 147 | none |
| du_doan_test_audit_log | 1 | none |

No required columns are missing.

## 7. V46 test rows/evaluation

| experiment | test_bt | official_bt | official | test | save | break | fp | net |
|---|---|---|---|---|---|---|---|---|
| MB_OFFICIAL_BASELINE_CONTROL | 43 | 43 | LOSE | LOSE | 0 | 0 | 0 | 0 |
| MB_COMPOSITE_CHALLENGER_V2 | 91 | 43 | LOSE | WIN | 1 | 0 | 0 | 1 |
| MB_TIER_AWARE_BUNDLE_SHADOW_V1 | 91 | 43 | LOSE | WIN | 1 | 0 | 0 | 1 |
| MB_AI_CHAIN_PRESERVATION_V1 | 91 | 43 | LOSE | WIN | 1 | 0 | 0 | 1 |
| MB_SPECIALIST_ROSTER_V1 | None | 43 | LOSE | LOSE | 0 | 0 | 0 | 0 |
| MB_PRIOR_REGION_CONTEXT_SAFE_V1 | 91 | 43 | LOSE | WIN | 1 | 0 | 0 | 1 |
| MB_NO_TOKEN_HERD_REDUCTION_V1 | 91 | 43 | LOSE | WIN | 1 | 0 | 0 | 1 |

## 8. Why 91 appeared across experiments

`91` was the strong runner-up in the same preview candidate set: ranked #2, 5 AI-chain voters, and actual hit. Multiple methods selected it because their scoring favors AI-chain/prior/tier/herd-reduction evidence. They are **not fully independent raw pipelines** yet; they are independent transforms over the same preview candidate payload.

## 9. Live parallel status

Classification: `LIVE_PARALLEL_MANUAL`.

`web/backend/_du_doan_test_daily_runner.py` exists and dry-run works, but it is intentionally not scheduler-wired yet. No daily auto marker exists.

## 10. MB test engine code audit

`web/backend/_du_doan_test_mb_engine.py` reads `mb_experimental_preview_shadow` and writes only `du_doan_test_*`. It does not call `generate_final_bundle()`, does not write `final_bundles`, and does not write production `predictions`. It has idempotency via existing run detection.

Limitations: it does not directly read all raw 25 prediction rows; it materializes from preview candidate rows. It does not execute AI test prompts.

## 11. Method coverage matrix

| experiment | tails | models | helped | hurt | status |
|---|---|---|---|---|---|
| MB_OFFICIAL_BASELINE_CONTROL | 8 | 14 | 0 | 5 | BASELINE |
| MB_COMPOSITE_CHALLENGER_V2 | 8 | 14 | 5 | 0 | ACTIVE_TEST_LANE_PREVIEW_DERIVED |
| MB_TIER_AWARE_BUNDLE_SHADOW_V1 | 8 | 14 | 5 | 0 | ACTIVE_TEST_LANE_PREVIEW_DERIVED |
| MB_AI_CHAIN_PRESERVATION_V1 | 8 | 14 | 5 | 0 | ACTIVE_TEST_LANE_PREVIEW_DERIVED |
| MB_SPECIALIST_ROSTER_V1 | 8 | 14 | 0 | 0 | PLACEHOLDER_NO_BT |
| MB_PRIOR_REGION_CONTEXT_SAFE_V1 | 8 | 14 | 5 | 0 | ACTIVE_TEST_LANE_PREVIEW_DERIVED |
| MB_NO_TOKEN_HERD_REDUCTION_V1 | 8 | 14 | 5 | 0 | ACTIVE_TEST_LANE_PREVIEW_DERIVED |

## 12. 25-model total output audit

Production MB predictions on 2026-05-02 include 25 models. Test contribution rows include 14 distinct voter models from the preview candidate payload. Missing from current test contribution layer: deepseek-v4-flash, deepseek-v4-pro, gemini-2.5-flash, glm-5.1, gpt-5.5, gpt-oss-120b, grok-4.20-multi-agent, kimi-k2.5, qwen3-coder, qwen3-max-thinking, qwen3.6-plus.

Verdict: `25_MODEL_TENSOR_AVAILABLE`, but not `25_MODEL_REALTIME_FULLY_USED` in the current test engine.

## 13. AI test prompt status

`du_doan_test_ai_predictions` table does not exist. `is_test_prompt=1` rows = 0. Prompt variant is `production_prompt_clone_or_none`. Status: `DESIGNED_ONLY`.

## 14. No-token clone/herd audit

No-token candidates are represented as cloned production-derived candidates in `du_doan_test_candidates`. Counts by family: [{"model_family": "AI", "rows": 70, "models": 7}, {"model_family": "NO_TOKEN", "rows": 77, "models": 7}]. Herd-reduction currently operates as transform over preview rows, not a separate no-token rerun.

## 15. Prior-region safe audit

Prior-region experiment is preview-derived. It is designed to use MN(D)+MT(D), not MB(D), but test engine stores the preview result rather than recomputing prior-region logic independently. Status: `ACTIVE_TEST_LANE_PREVIEW_DERIVED`.

## 16. Tier-aware + AI-chain preservation audit

Both are implemented in preview materializer and persisted through test engine. They selected `91` because AI-chain evidence was strong. They are transforms over the same ranked payload, not separate full pipelines.

## 17. Model tensor quality audit

Tensor exists and is useful for diagnostics. It is not enough for pruning because per-model duration/cost remains incomplete.

## 18. UI completeness matrix

Present: official baseline, shadow summary, best shadow, 30-day backtest snapshot, experiment cards, ranked preview table, test history, fallback latest date, safety banner.

Partial/missing: model contribution detail is not expanded in UI; realtime vs diagnostic label is not explicit per row; AI prompt status is not displayed; loz diagnostics are absent.

## 19. Data model gap analysis

Sufficient: multiple experiments per day, official vs test, post-closeout eval, model contribution rows, rollback via deleting test tables/rows.

Gaps: no method scoreboard table, no latency daily table, no leakage audit table, no AI test prediction table.

## 20. MB recovery scoreboard 6?12

Current backtest: official baseline 5/30, composite 8/30, AI-chain 9/30. Gate for official discussion is at least +4/30 stable; composite is +3, AI-chain is +4 but has false-promotion risk. Status: promising but still test-only.

## 21. Daily runner plan/deployment

`web/backend/_du_doan_test_daily_runner.py` deployed and dry-run verified. It remains manual-only. Recommended next: run manually for 3-5 closeouts before scheduler auto-wire.

## 22. Source hash proof

Pre-hash: `artifacts/_du_doan_test_v47_pre_hash_20260503.txt`. Post-hash saved after this report. Logical source tables unchanged except scheduler_logs natural deploy/smoke growth.

## 23. What is fully done

Admin route/API, preview materializer, test tables, test engine, manual runner dry-run, UI with history, route protection, 2026-05-02 test/eval rows.

## 24. What is partial

25-model full realtime usage, method independence, model contribution UI, latency/value instrumentation, daily automation.

## 25. What is missing

AI test prompts, direct raw-25 candidate ingestion into test engine, method scoreboard, latency daily table, leakage audit table, loz diagnostic panel.

## 26. What should be done next 24h

Run manual daily runner after MB closeout, add test method scoreboard, and expand UI to show contribution detail + realtime/diagnostic labels.

## 27. What should wait 7-14 days

Scheduler auto-wire, official-output decision, roster pruning, prompt production changes.

## 28. What remains owner-lock

Any migration into official `/du-doan`, production prompt, production model roster, scoring, bundle voting, or scheduler auto-wire.

## 29. Risk register

Main risks: test mistaken as official; multiple methods not independent enough; 25-model claim overread; AI prompt not executing; latency missing. Mitigations: admin-only, labels, this V47 correction, manual runner first.

## 30. Rollback plan

Remove routes/API if needed; delete `du_doan_test_*` tables/rows; leave official untouched.

## 31. Docs/tracker/changelog sync

Synced as V20.3.37.47.

## 32. Technical no-drop audit

VPS sync yes; source hash yes; route smoke yes; schema audit yes; test counts yes; 25-model status corrected yes; prompt status corrected yes.

## 33. Governance no-overclaim audit

No official mutation. No public exposure. No claim that 25 models are fully realtime in test. No claim that AI prompt test is running. No production migration.
