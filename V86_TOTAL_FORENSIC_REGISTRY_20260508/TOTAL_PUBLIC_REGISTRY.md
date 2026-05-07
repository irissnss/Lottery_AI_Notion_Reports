# TOTAL PUBLIC REGISTRY — Lottery AI Test (V86 deep)

Generated: 2026-05-08T00:08:04+07:00

This is the **single canonical reference** for Notion AI / agent / owner to look up any model, table, endpoint, frontend page, FU item, CHANGELOG version, phase checkpoint, prompt, cron job, metric, rule, or mechanism. Built from V85 deep inventory + V86 forensic extension.

## 0. STATISTICS

| Family | Count |
|---|---|
| AI Models | 41 (ACTIVE=15 / SHADOW=13 / TOKEN=32 / NO_TOKEN=7) |
| DB Tables | 129 ({'OFFICIAL': 4, 'TEST_LANE': 21, 'WAVE_1_2': 13, 'SHADOW': 43, 'INFRA': 1, 'SUPPORT': 47}) |
| Cron Jobs | 26 |
| Prompt Layers | 8 |
| PHASE-FIRST GATE Cohorts | 5 |
| Metrics (C-XX + PB-XX + flip) | 27 |
| Shadow Methods | 59 |
| API Endpoints (main.py) | 132 ({'PAGE': 22, 'PUBLIC_API': 86, 'ADMIN_API': 24}) |
| Admin-only Endpoints | 90 |
| Frontend Pages | 12 |
| FU Items | 142 |
| CHANGELOG Versions (V6.8 → V20.3.37.85) | 224 |
| Phase Checkpoint Files | 116 |
| AUTOMATION_HISTORY Entries | 26 |

---

## 1. FRONTEND PAGES (12)

| File | URL | Size (KB) |
| --- | --- | --- |
| accuracy.html | /accuracy | 19 |
| du-doan-test.html | /du-doan-test | 63 |
| du-doan.html | /du-doan | 44 |
| index.html | / | 21 |
| login.html | /login | 8 |
| monitoring.html | /monitoring | 162 |
| review-dashboard.html | /review-dashboard | 86 |
| search.html | /search | 34 |
| settings.html | /settings | 93 |
| user-view.html | /user-view | 19 |
| v82-monitor.html | /v82-monitor | 18 |
| viewer.html | /viewer | 21 |

**URL summary** (production: https://xs.io.vn):

- `/` (or `/login`) — index page
- `/login` — login page
- `/du-doan` — production prediction page (15 model output-eligible)
- `/du-doan-test` — admin-only experimental lane (V52.5+ test methods, includes V57 budget)
- `/du-doan-test?v=...-source-badges` — same page; query param refresh badges
- `/monitoring` — admin runtime monitoring center (Parallel Shadow Proof + V82 master control after V86 merge)
- `/v82-monitor` — admin V82 read-only panel (V83 standalone; V86 also embeds inside `/monitoring`)
- `/accuracy` — accuracy review board
- `/review-dashboard` — review dashboard
- `/search` — search interface
- `/settings` — admin settings
- `/user-view` — compact user view
- `/viewer` — generic viewer

---

## 2. ADMIN API ENDPOINTS (24)

| Method | Path | Function | Line |
| --- | --- | --- | --- |
| GET | /api/admin/bt-trail | get_bt_trail | 11565 |
| GET | /api/admin/candidate-drop-stage | get_candidate_drop_stage | 13399 |
| GET | /api/admin/cohere-effectiveness | get_cohere_effectiveness | 12609 |
| GET | /api/admin/combo-vs-single | get_combo_vs_single | 12529 |
| GET | /api/admin/eq-experiment-tracker | get_eq_experiment_tracker | 12841 |
| GET | /api/admin/experiments | get_experiments | 11968 |
| GET | /api/admin/mb-d1-shadow | get_mb_d1_shadow | 13677 |
| GET | /api/admin/ml-freshness-chain | get_ml_freshness_chain | 13085 |
| GET | /api/admin/model-bt-by-region | get_model_bt_by_region | 12742 |
| GET | /api/admin/model-daily-accuracy | get_model_daily_accuracy | 12327 |
| GET | /api/admin/model-family-bt | get_model_family_bt | 13004 |
| GET | /api/admin/parallel-shadow-proof | get_parallel_shadow_proof | 11412 |
| GET | /api/admin/prompt-gate-cohort | get_prompt_gate_cohort | 12083 |
| GET | /api/admin/region-streaks | get_region_streaks | 12911 |
| GET | /api/admin/rerun-drift | get_rerun_drift | 7536 |
| GET | /api/admin/rule-offset-performance | get_rule_offset_performance | 13613 |
| GET | /api/admin/rule-summary | get_rule_summary | 11850 |
| GET | /api/admin/runtime-monitoring-center | get_runtime_monitoring_center | 10958 |
| GET | /api/admin/runtime-reliability | get_runtime_reliability | 13099 |
| GET | /api/admin/selection-gap | get_selection_gap | 11651 |
| GET | /api/admin/shadow-comparison | get_shadow_comparison | 13506 |
| GET | /api/admin/shadow-rules-emit | get_shadow_rules_emit | 12458 |
| GET | /api/admin/strongest-vs-final | get_strongest_vs_final | 13300 |
| GET | /api/admin/v82-monitor | api_admin_v82_monitor | 10866 |

---

## 3. PUBLIC API ENDPOINTS (86)

| Method | Path | Function | Line |
| --- | --- | --- | --- |
| GET | /api/accuracy/chot_ha | accuracy_chot_ha_report_api | 4893 |
| GET | /api/accuracy/dashboard | accuracy_dashboard_api | 3456 |
| GET | /api/accuracy/today-warnings | accuracy_today_warnings | 4746 |
| GET | /api/analysis-rules | get_analysis_rules | 5091 |
| POST | /api/analysis-rules | save_analysis_rules | 5100 |
| GET | /api/auth/check | check_auth | 2302 |
| POST | /api/backfill | api_backfill | 2400 |
| POST | /api/backtest | run_backtest | 7870 |
| GET | /api/backtest-metrics | get_backtest_metrics | 5369 |
| POST | /api/backtest/ai-models | backtest_ai_models_api | 4944 |
| POST | /api/backtest/run | run_backtest_api | 4912 |
| GET | /api/data-coverage | api_data_coverage | 2387 |
| GET | /api/db-stats | get_database_stats | 2379 |
| GET | /api/du-doan-test/mb | api_du_doan_test_mb | 9662 |
| GET | /api/du-doan-test/{region} | api_du_doan_test_region | 10290 |
| GET | /api/effectiveness | api_get_effectiveness | 3151 |
| GET | /api/elimination/{date_str}/{region} | get_elimination_report | 7486 |
| GET | /api/filter-2-so-cuoi | api_filter_2_so_cuoi | 2929 |
| GET | /api/final-bundle | api_get_final_bundle | 9008 |
| GET | /api/final-bundle/history | api_get_bundle_history | 9093 |
| GET | /api/final-bundle/selection-delta | api_selection_delta | 9119 |
| POST | /api/generate-bundle | api_generate_bundle | 10745 |
| GET | /api/health | health_check | 3321 |
| GET | /api/learned-weights | api_get_learned_weights | 3176 |
| POST | /api/login | login | 2278 |
| POST | /api/logout | logout | 2296 |
| GET | /api/mined-rules/bucket/{bucket_code} | api_mined_rules_bucket | 2608 |
| GET | /api/mined-rules/effectiveness/{rule_id} | api_mined_rule_effectiveness | 2784 |
| GET | /api/mined-rules/flow/{target_date} | api_mined_rules_flow | 2742 |
| GET | /api/mined-rules/overview | api_mined_rules_overview | 2544 |
| GET | /api/mined-rules/preview-state | api_mined_rules_preview_state | 2837 |
| GET | /api/mined-rules/split-audit | api_mined_rules_split_audit | 2701 |
| POST | /api/ml-models/train | train_ml_models | 5013 |
| GET | /api/model-ranking | model_ranking_api | 4617 |
| GET | /api/model-selection | get_model_selection | 4363 |
| GET | /api/model-warnings | model_warnings_api | 4596 |
| GET | /api/notifications-config | get_notifications_config | 5112 |
| POST | /api/optimize-weights | optimize_weights_api | 7922 |
| POST | /api/predict/MB | predict_mb | 5830 |
| POST | /api/predict/MN | predict_mn | 5677 |
| POST | /api/predict/MT | predict_mt | 5755 |
| POST | /api/predict/ml-model | predict_with_ml_model | 4968 |
| GET | /api/prediction-advisory | get_prediction_advisory | 4405 |
| GET | /api/prediction-quality | get_prediction_quality | 3474 |
| GET | /api/prediction-trace | get_prediction_trace | 3279 |
| GET | /api/predictions | get_predictions | 7705 |
| POST | /api/predictions/delete-batch | delete_batch_predictions | 8026 |
| DELETE | /api/predictions/{date_str}/{target_region} | delete_single_prediction | 7998 |
| GET | /api/preflight-status | get_preflight_status | 8136 |
| GET | /api/reasoning | api_get_reasoning | 3136 |
| GET | /api/repredict-quality | api_repredict_quality | 7513 |
| GET | /api/results/{region} | get_results | 7807 |
| GET | /api/review-hub/filter | api_review_hub_filter | 2948 |
| GET | /api/rules | api_get_rules | 2443 |
| POST | /api/rules | api_create_rule | 2458 |
| PUT | /api/rules/{rule_id} | api_update_rule | 2477 |
| DELETE | /api/rules/{rule_id} | api_delete_rule | 2501 |
| POST | /api/rules/{rule_id}/toggle | api_toggle_rule | 2516 |
| POST | /api/run-optimizer-now | run_optimizer_now_api | 7984 |
| POST | /api/scheduler/reload | scheduler_reload | 3359 |
| POST | /api/scheduler/run-free-predict | scheduler_run_free_predict | 3383 |
| POST | /api/scheduler/run-now/{region} | scheduler_run_now | 3367 |
| POST | /api/scheduler/run-retrain | scheduler_run_retrain | 3393 |
| POST | /api/scheduler/shadow-eval-now | shadow_eval_now_api | 3427 |
| GET | /api/scheduler/status | scheduler_status | 3352 |
| GET | /api/search-results | search_results | 7829 |
| POST | /api/settings | update_settings | 2353 |
| POST | /api/settings/bulk | update_settings_bulk | 2361 |
| GET | /api/settings/{category} | get_settings | 2333 |
| GET | /api/so-gan | api_so_gan | 2974 |
| GET | /api/status | get_status | 5191 |
| POST | /api/sync/push | push_results | 5381 |
| GET | /api/system-alerts | get_system_alerts | 8055 |
| POST | /api/system-alerts/{alert_id}/resolve | resolve_system_alert | 8113 |
| GET | /api/system-prompt-raw | get_system_prompt_raw | 8044 |
| GET | /api/time | get_server_time | 5120 |
| GET | /api/top-models | api_top_models | 3083 |
| GET | /api/training-status | get_training_status_api | 3416 |
| POST | /api/update/{region} | update_results | 5413 |
| GET | /api/users | list_users | 3188 |
| POST | /api/users | create_new_user | 3195 |
| PUT | /api/users/{user_id} | update_existing_user | 3208 |
| DELETE | /api/users/{user_id} | delete_existing_user | 3224 |
| GET | /api/viewer/predictions | viewer_predictions | 3237 |
| GET | /api/viewer/today | viewer_today | 3256 |
| GET | /api/win-rates | get_all_win_rates | 7859 |

---

## 4. PAGE ROUTES (22)

| Method | Path | Function | Admin? |
| --- | --- | --- | --- |
| GET | / | root |  |
| GET | /accuracy | accuracy_page | True |
| GET | /accuracy.js | serve_accuracy_js | True |
| GET | /app | serve_frontend |  |
| GET | /app.js | serve_js | True |
| GET | /du-doan | serve_dudoan_page | True |
| GET | /du-doan-test | serve_dudoan_test_page | True |
| GET | /filter | filter_page |  |
| GET | /login | login_page |  |
| GET | /login.html | serve_login_page | True |
| GET | /monitoring | serve_monitoring | True |
| GET | /review-dashboard | review_dashboard_page | True |
| GET | /rules-dashboard | rules_dashboard_page | True |
| GET | /search | serve_search_page | True |
| GET | /settings | serve_settings_page |  |
| GET | /settings.js | serve_settings_js |  |
| GET | /styles.css | serve_css | True |
| GET | /user-view | serve_user_view_page |  |
| GET | /user-view.js | serve_user_view_js | True |
| GET | /v82-monitor | serve_v82_monitor_page | True |
| GET | /viewer | serve_viewer_page |  |
| GET | /viewer.js | serve_viewer_js |  |

---

## 5. FU ITEMS — latest 30 of 142

| FU ID | Status | Title |
| --- | --- | --- |
| FU-151 | DELIVERED_INVENTORY_DOCS_ONLY | V85 DEEP MASTER CONTROL: 8 super-families full inventory |
| FU-150 | DELIVERED_AUDIT_DOCS_ONLY | V84 Master Control Board + 60D method maturity + all-open-threads reconciliation |
| FU-149 | DEPLOYED_PENDING_OWNER_VERIFY | V83 admin-only V82 monitor UI panel (read-only shadow surfaces) |
| FU-148 | DEPLOYED_PENDING_LIVE_VERIFY | V82 60D evidence control pass (P0.1→P0.6 verification + accuracy dossier) |
| FU-147 | DEPLOYED_PENDING_LIVE_VERIFY | V81 owner-approved provider shadow pilot (3 models × 3 regions) |
| FU-146 | DEPLOYED_PENDING_LIVE_VERIFY | V80 absolute closure: Notion/code/runtime sync + shadow completion |
| FU-145 | DEPLOYED_PENDING_LIVE_VERIFY | V79 AI↔NO_TOKEN cross-verification + cluster-weighted consensus |
| FU-144 | DEPLOYED_PENDING_LIVE_VERIFY | V78 AI prompt/context forensic + region-specialist shadow prompts |
| FU-143 | DEPLOYED_PENDING_LIVE_VERIFY | V77 post-closeout incident audit + V70/V73 timing fix + fast incident monitor |
| FU-142 | DEPLOYED_PENDING_LIVE_VERIFY | V76 P0 batch: drift monitor + C-16 latency live + cost tracking |
| FU-141 | DEPLOYED_PENDING_LIVE_VERIFY | V74 follow-up: C-05 RESOLVED + V75 next-action proposal |
| FU-140 | DEPLOYED_PENDING_LIVE_VERIFY | V74 TOTAL FORCE AUDIT (governance + runtime verify + GitHub metadata) |
| FU-139 | DEPLOYED_PENDING_LIVE_VERIFY | V73 region-adaptive HYBRID (owner-final balanced state) |
| FU-138 | DEPLOYED_PENDING_LIVE_VERIFY | V72 V67 STRICT gate REVERTED → eager (per owner) |
| FU-137 | DEPLOYED_PENDING_LIVE_VERIFY | V71 HYBRID_V1 + C-16 score-gate fix (rescued MT/MB) |
| FU-136 | DEPLOYED_PENDING_LIVE_VERIFY | V69 metrics + V70 CONSENSUS_V1 selector (test-lane only) |
| FU-135 | DEPLOYED_PENDING_LIVE_VERIFY | V68 MT diagnostic + C-16 budget expansion 15-20 voters |
| FU-134 | DEPLOYED_PENDING_LIVE_VERIFY | V67 ADAPTIVE_EXPLOIT_V1 selector (test-lane only) |
| FU-133 | DEPLOYED_PENDING_LIVE_VERIFY | V66/V66.1 Lag-1 + cross-region adaptive exploit signal (measurement-only) |
| FU-132 | DEPLOYED_PENDING_LIVE_VERIFY | C-16 adaptive model budget selector |
| FU-131 | DEPLOYED_PENDING_LIVE_VERIFY | V56 `/du-doan-test` Experience Lane |
| FU-130 | DEPLOYED_PENDING_LIVE_VERIFY | V55 test-lane auto-wire readiness |
| FU-129 | READY_TO_BUILD_UI_TEST_ONLY | V55 model strong/weak tensor advanced + UI surfacing pending |
| FU-128 | DEPLOYED_PENDING_LIVE_VERIFY | V55 latency/cost still blocked |
| FU-127 | DEPLOYED_PENDING_LIVE_VERIFY | V55 loz stage trace 04/05+05/05 backfilled |
| FU-126 | DEPLOYED_PENDING_LIVE_VERIFY | V55 2-day official-vs-test scorecard |
| FU-125 | DEPLOYED_PENDING_LIVE_VERIFY | V55 add 3 Google direct shadow models (Gemini 3.1 Pro / Gemini 3 Flash / Gemma 4 31B) |
| FU-124 | DEPLOYED_PENDING_LIVE_VERIFY | V54 multi-region evaluator / auto readiness |
| FU-123 | DEPLOYED_PENDING_LIVE_VERIFY | V54 MB Wed/Fri blackspot alert |
| FU-122 | READY_TO_BUILD_UI_TEST_ONLY | V54 region/weekday/station strength chips |

**Status distribution**: {'DELIVERED_INVENTORY_DOCS_ONLY': 1, 'DELIVERED_AUDIT_DOCS_ONLY': 1, 'DEPLOYED_PENDING_OWNER_VERIFY': 1, 'DEPLOYED_PENDING_LIVE_VERIFY': 29, 'READY_TO_BUILD_UI_TEST_ONLY': 3, 'READY_TO_BUILD_MEASUREMENT_ONLY': 1, 'WAIT_CLOSEOUT': 1, 'DONE_DOCS_DELIVERED': 1, 'NOT_YET_PROVEN': 8, 'DESIGN_ONLY': 1, 'DONE': 3, 'PARTIAL': 2, 'OWNER_LOCK': 1, '—': 88, '[One': 1}

---

## 6. CHANGELOG VERSIONS — latest 30 of 224

| Version | Title |
| --- | --- |
| V20.3.37.85 | V85 DEEP MASTER CONTROL: 8 super-families full inventory (audit only, no official touch) (2026-05-07 23:55 VN) |
| V20.3.37.84 | V84 Master Control Board + 60D method maturity + all-open-threads reconciliation (audit only, no official touch) (2026-05-07 23:30 VN) |
| V20.3.37.83 | V83 admin-only V82 monitor UI panel (read-only, shadow surfaces only) (2026-05-07 23:20 VN) |
| V20.3.37.82 | V82 60D evidence control pass + P0.1→P0.6 verification + accuracy optimization dossier (shadow only, no official touch) (2026-05-07 23:05 VN) |
| V20.3.37.81 | V81 owner-approved provider shadow pilot: 3 models × 3 regions × 2 days (test-lane only) (2026-05-07 22:18 VN) |
| V20.3.37.80 | V80 absolute closure: Notion/code/runtime sync + shadow completion + HCM hardening (test-lane only) (2026-05-07 21:55 VN) |
| V20.3.37.79 | V79 AI↔NO_TOKEN cross-verification + cluster-weighted consensus + HCM timezone audit (test-lane only) (2026-05-07 21:25 VN) |
| V20.3.37.78 | V78 AI prompt/context forensic + region-specialist shadow prompts + V77 timezone hardening (test-lane only) (2026-05-07 20:05 VN) |
| V20.3.37.77 | V77 Post-closeout incident audit: V70/V73 timing fix + fast incident monitor + 4-day regression diagnostic (2026-05-07 18:55 VN) |
| V20.3.37.76 | V76 P0 batch: drift monitor + C-16 latency_score live + cost provider (test-lane only) (2026-05-07 15:16 VN) |
| V20.3.37.74.1 | V74 follow-up: C-05 RESOLVED (was data lag, not broken) + V75 next-action proposal (2026-05-07 11:55 VN) |
| V20.3.37.74 | V74 TOTAL FORCE AUDIT: runtime verify + continuous measurement doctrine + GitHub report governance (2026-05-07 11:15 VN) |
| V20.3.37.73 | V73 region-adaptive HYBRID — owner-final balanced state (2026-05-07 02:22 VN) |
| V20.3.37.72 | V67 STRICT-gate REVERTED to eager (per owner directive) (2026-05-07 02:13 VN) |
| V20.3.37.71 | V71 HYBRID_V1 selector + C-16 score-gate fix → MT/MB rescued (2026-05-07 02:00 VN) |
| V20.3.37.69 | V69 metrics expansion + V70 CONSENSUS_V1 selector (test-lane only) (2026-05-07 01:50 VN) |
| V20.3.37.68 | V68 MT diagnostic fix + C-16 budget expansion 8-10 → 15-20 (2026-05-07 01:40 VN) |
| V20.3.37.67 | V67 ADAPTIVE_EXPLOIT_V1 selector + Discovery 8 (model anti-recommit) (2026-05-07 01:25 VN) |
| V20.3.37.66.1 | V66.1 expand coverage: per-model + lag-2/3 + LO2 + per-weekday cross + repeat-tail (2026-05-07 01:10 VN) |
| V20.3.37.66 | V66 Lag-1 + Cross-region Adaptive Exploit Signal (measurement-only) (2026-05-07 00:55 VN) |
| V20.3.37.65 | V65 lag-1 leakage + strength priority + test-lane weighting audit (2026-05-06 23:50 VN) |
| V20.3.37.63 | C-05 latency instrumentation + C-03 multi-region evaluator (2026-05-06 23:20 VN) |
| V20.3.37.62 | Notion AI logical synthesis + report export rule sync (2026-05-06) |
| V20.3.37.61 | Dynamic `/du-doan-test` pre-result trigger (2026-05-06 07:55 VN) |
| V20.3.37.60 | Mobile two-column UI + C-16-prioritized shadow model order (2026-05-05 23:42 VN) |
| V20.3.37.59 | Strict LO3 / Xien verification fix for `/du-doan-test` (2026-05-05 23:25 VN) |
| V20.3.37.58 | `/du-doan-test` visual parallel output cards (2026-05-05 23:20 VN) |
| V20.3.37.57 | C-16 Adaptive Model Budget Selector for `/du-doan-test` (2026-05-05 23:00 VN) |
| V20.3.37.56 | `/du-doan-test` Experience Lane (2026-05-05 21:41 VN) |
| V20.3.37.55_full_chain | TOTAL-FORCE V55 closeout 04/05 + 05/05 + scheduler preflight fix + 2-day materialization (2026-05-05 20:14 VN) |

Oldest: V6.8 — Newest: V20.3.37.85. Full registry covers ~9 months of evolution.

---

## 7. PHASE CHECKPOINT FILES — by date (116 files / 14 distinct dates)

| Date | Files | Filenames (first 300 chars) |
| --- | --- | --- |
| 2026-05-06 | 1 | V61_DYNAMIC_DU_DOAN_TEST_TRIGGER_20260506.md |
| 2026-05-05 | 6 | SHADOW_ADD_GOOGLE_DIRECT_COHORT_20260505.md, V56_DU_DOAN_TEST_EXPERIENCE_LANE_20260505.md, V57_C16_ADAPTIVE_MODEL_BUDGET_SELECTOR_20260505.md, V58_DU_DOAN_TEST_VISUAL_PARALLEL_OUTPUT_20260505.md, V59_LO3_XIEN_STRICT_VERIFICATION_FIX_20260505.md, V60_MOBILE_AND_MODEL_PRIORITY_ORDER_20260505.md |
| 2026-05-04 | 2 | TOTAL_FORCE_V54_NATURAL_LIVE_CLOSEOUT_MEASUREMENT_AND_TEST_LANE_CONTROL_20260504.md, TOTAL_FORCE_V55_20260504_20260505_CLOSEOUT_AND_NEXT_UPGRADE_PLAN.md |
| 2026-05-03 | 16 | DU_DOAN_TEST_FULL_MODEL_TENSOR_MB_RECOVERY_20260503.md, DU_DOAN_TEST_V47_LIVE_PARALLEL_VERIFICATION_20260503.md, DU_DOAN_TEST_V48_START_LIVE_PARALLEL_COMPLETION_20260503.md, DU_DOAN_TEST_V49_FULL_REPORT_REREAD_AND_LIVE_PARALLEL_CONTROL_20260503.md, DU_DOAN_TEST_V50_PARALLEL_EXPERIMENT_LANE_COMPLETIO |
| 2026-05-02 | 13 | FULL_QUALITY_COVERAGE_AND_IMPROVEMENT_GAP_AUDIT_20260502.md, GLOBAL_MODEL_REGION_WEEKDAY_MB_RECOVERY_AUDIT_20260502.md, LIVE_STABILITY_MEASUREMENT_AND_ROLLOVER_AUDIT_20260502.md, LOTTERY_PROFIT_REPORT_20260502.md, LOZ1_LOZ2_MONTHLY_BREAKDOWN_20260502.md, LOZ_SYSTEM_STABILITY_SUMMARY_20260502.md, MOD |
| 2026-05-01 | 19 | CURRENT_RUNTIME_TRUTH_D2_PRECHECK_20260501.md, D1_RULE_MECHANISM_FULL_AUDIT_20260501.md, D2_BASIC_REGION_VERDICT_20260501.md, D2_EXPANDED_RULESET_SHADOW_SPEC_20260501.md, D2_FOUNDATION_HOLD_DECISION_20260501.md, D2_LOCAL_REPLAY_REGION_DECISION_PACK_20260501.md, D2_MINIMUM_ARTIFACT_REPLAY_REPORT_2026 |
| 2026-04-30 | 13 | AXES_ML_RULES_PRIZE_READINESS_AUDIT_20260430.md, BACKTEST_60_VS_90_EXPERIMENT_20260430.md, COHERE_RERANK_P0_BRIDGE_CLOSEOUT_20260430.md, FULL_PARALLEL_MEASUREMENT_CONSOLIDATED_STATUS_20260430.md, FULL_PARALLEL_MEASUREMENT_CONSOLIDATED_STATUS_FINAL_20260430.md, ML_LEARNING_MECHANISMS_AND_60_90_BACKTE |
| 2026-04-29 | 2 | POST_LIVE_FULL_CYCLE_AUDIT_REPORT_20260429.md, POST_LIVE_TOTAL_FORCE_CLOSEOUT_20260429.md |
| 2026-04-28 | 12 | EXECUTION_CLOSEOUT_REPORT_MONITORING_CLEANUP_MULTI_LANE_SHADOW_P0_PROGRESSION_20260428.md, MINIMAX_M27_SHADOW_PRUNE_CLOSEOUT_20260428.md, NEXT_LIVE_WATCH_CHECKLIST_AFTER_MINIMAX_PRUNE_20260428.md, OUTPUT_REPLAY_EXECUTION_DECISION_PACK_20260428.md, OUTSTANDING_ISSUES_ACTION_PLAN_20260428.md, P05_MULT |
| 2026-04-27 | 16 | FINAL_OUTPUT_REPLAY_MEASUREMENT_DECISION_PACK_20260427.md, MASTER_RECONCILIATION_REPORT_MONITORING_MULTI_LANE_SHADOW_CURRENT_SYSTEM_STATE_20260427.md, MONITORING_AND_MULTI_LANE_SHADOW_MASTER_RECONCILIATION_REPORT_20260427.md, MONITORING_TOTAL_FORCE_AUDIT_REPORT_20260427.md, MT_BUNDLE_SKEW_REPLAY_PAC |
| 2026-04-26 | 8 | BLOCK_ACTIVATION_MATRIX_20260426.md, DEEP_OUTPUT_REPLAY_AFTER_PP5_ROLLBACK_20260426.md, MASTER_STATUS_DASHBOARD_20260426.md, OUTPUT_POLICY_DECISION_REPORT_20260426.md, OUTPUT_REPLAY_WRITER_DECISION_PACK_20260426.md, OUTPUT_SECONDARY_AUDIT_REPORT_20260426.md, PP5_EFFECT_VERDICT_REPORT_20260426.md, PP |
| 2026-04-25 | 1 | BLOCK_ACTIVATION_MATRIX_20260425.md |
| 2026-04-24 | 1 | PHASE_G_IMPLEMENTATION_PLAN_20260424.md |
| 2026-04-23 | 6 | PHASE_A_TRUTH_LOCK_20260423.md, PHASE_B_PROMPT_INTEGRITY_20260423.md, PHASE_C_RERUN_DRIFT_20260423.md, PHASE_D_RULES_CHAIN_20260423.md, PHASE_E_PROMPT_PRESSURE_GAN_KB_20260423.md, PHASE_F_SHADOW_ML_UI_20260423.md |

---

## 8. CROSS-REFERENCE — V63 → V85 SHADOW SURFACES

| Version | Surface | URL/Path | Cron | Status |
|---|---|---|---|---|
| V57 | C-16 ADAPTIVE_BUDGET_SELECTOR_V1 | experimental_preview_shadow + du_doan_test_model_budget_daily | 23:50 VN (drift) | LIVE |
| V63 | governance lock + GitHub metadata | docs/ + LATEST_REPORT.json | — | LIVE |
| V66.1 | lag1_adaptive_exploit_signal_shadow | lag1_adaptive_exploit_signal_shadow | 23:35 VN | LIVE |
| V67 | ADAPTIVE_EXPLOIT_V1 | adaptive_exploit_v67_candidate_trace | 23:40 VN | LIVE |
| V70 | CONSENSUS_V1 | consensus_v1_trace | 23:45 + 19:00 (V77) | LIVE |
| V73 | HYBRID_V1 region-adaptive | hybrid_v1_trace | 23:48 + 19:00 | LIVE |
| V74 | governance lock + 4 docs | docs/CONTINUOUS_MEASUREMENT_DOCTRINE.md etc. | — | LIVE |
| V76 | drift monitor + latency live + cost provider | test_lane_signal_drift_monitor + model_latency_cost_audit_daily | 23:50 VN | LIVE alert-only |
| V77 | post-cascade rerun + fast incident monitor | test_lane_fast_incident_monitor | 19:00 + 19:05 VN | LIVE |
| V78 | region-specialist shadow prompts (3) + audit | ai_region_specialist_prompt_shadow_results + 3 .md | 19:10 VN | LIVE (no provider) |
| V79 | AI↔NO_TOKEN cross-verify + cluster-weighted | ai_no_token_cross_verification_shadow + cluster_weighted_consensus_shadow | 19:08 VN | LIVE |
| V80 | rule_phase_synthesis + no_token_rule_pack + mb_regime + mn_v67_save | 4 shadow tables | 19:12 VN | LIVE |
| V81 | provider shadow pilot 3 models | ai_region_specialist_provider_shadow_results | 19:14 VN | LIVE owner-approved |
| V82 | 60D evidence audit | artifacts/v82_60d_evidence_control/ | — | DELIVERED |
| V83 | V82 monitor UI panel `/v82-monitor` | web/frontend/v82-monitor.html + /api/admin/v82-monitor | — | DEPLOYED |
| V84 | Master Control Board summary | artifacts/v84_master_control_board/ | — | DELIVERED |
| V85 | DEEP MASTER CONTROL 8 super-families | artifacts/v85_deep_master_control/ | — | DELIVERED |
| V86 | TOTAL_PUBLIC_REGISTRY + monitoring merge | artifacts/v86_total_forensic_registry/ + monitoring.html sectionV82MasterControl | — | THIS REPORT |

---

## 9. INDEX — Where to find what

| Looking for... | Go to |
|---|---|
| Total models list | [V85 f1_all_models.md](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/V85_DEEP_MASTER_CONTROL_20260507/evidence/f1_all_models.md) |
| Total DB tables | [V85 f2_all_db_tables.md](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/V85_DEEP_MASTER_CONTROL_20260507/evidence/f2_all_db_tables.md) |
| Cron jobs | [V85 f3_all_cron_jobs.md](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/V85_DEEP_MASTER_CONTROL_20260507/evidence/f3_all_cron_jobs.md) |
| Prompts/cohorts | [V85 f4_all_prompts.md](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/V85_DEEP_MASTER_CONTROL_20260507/evidence/f4_all_prompts.md) |
| Metrics | [V85 f5_all_metrics.md](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/V85_DEEP_MASTER_CONTROL_20260507/evidence/f5_all_metrics.md) |
| Rules | [V85 f6_all_rules.md](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/V85_DEEP_MASTER_CONTROL_20260507/evidence/f6_all_rules.md) |
| Mechanisms | [V85 f7_all_mechanisms.md](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/V85_DEEP_MASTER_CONTROL_20260507/evidence/f7_all_mechanisms.md) |
| Shadow methods | [V85 f8_all_shadow_methods.md](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/V85_DEEP_MASTER_CONTROL_20260507/evidence/f8_all_shadow_methods.md) |
| Decision calendar | [V84 decision_calendar.md](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/V84_MASTER_CONTROL_BOARD_20260507/evidence/decision_calendar.md) |
| Owner gate queue | [V84 open_owner_gate_queue.md](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/V84_MASTER_CONTROL_BOARD_20260507/evidence/open_owner_gate_queue.md) |
| 60D evidence | [V82 60d_method_region_table.md](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/V82_60D_EVIDENCE_CONTROL_PASS_20260507/evidence/60d_method_region_table.md) |
| MN/MT/MB region forensic | V82 mn/mt/mb_60d_region_forensic.md |
| Master control board (V84) | [V84 master_control_board.md](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/V84_MASTER_CONTROL_BOARD_20260507/evidence/master_control_board.md) |
| Method maturity matrix | [V84 method_maturity_matrix.md](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/V84_MASTER_CONTROL_BOARD_20260507/evidence/method_maturity_matrix.md) |
| Latest report pointer | [LATEST_REPORT.json](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/LATEST_REPORT.json) |
| Open issues | [OPEN_ISSUES.md](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/OPEN_ISSUES.md) |
| Next action | [NEXT_ACTION.md](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/NEXT_ACTION.md) |
| Public CHANGELOG | [CHANGELOG_PUBLIC.md](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/CHANGELOG_PUBLIC.md) |
| Delta versions | [DELTA_INDEX.md](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/DELTA_INDEX.md) |

---

## 10. HARD LOCKS (do-not-touch)

1. 4 official tables hash UNCHANGED (predictions / final_bundles / lottery_results / model_daily_eval).
2. No selector promotion without dossier + owner OK.
3. No global NO_TOKEN floor change.
4. No official prompt change.
5. No production model swap.
6. UI Master Board build only after owner OK.
7. Provider invoice update needs owner instruction.
