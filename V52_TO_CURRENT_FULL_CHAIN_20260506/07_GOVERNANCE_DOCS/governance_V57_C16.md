

===== CHANGELOG.md hits for V57_C16 =====
12|
13|- MN had 15 `auto_daily` + 13 `shadow_auto_eval` prediction rows and official final bundle BT=95, lo2=[95,46].
14|- MN had no lottery result rows yet (pre-result).
15|- MN had 0 C-16 budget rows, 0 experimental_preview rows, 0 du_doan_test rows.
16|- MT/MB had only no-token rows and no final bundle yet.
17|
18|### Immediate action
19|
20|Manually ran MN pre-result:
21|
22|- C-16 budget: pool 29, measured 28, selected 10, watch 18, skipped 1.
19|
20|Manually ran MN pre-result:
21|
22|- C-16 budget: pool 29, measured 28, selected 10, watch 18, skipped 1.
23|- V52.5.6 test runner `REALTIME_AVAILABLE_ONLY`: created 7 runs / 7 bundles / 7 results / 164 candidates / 164 contributions.
24|- MN adaptive output currently agrees with official: test_bt=95, official_bt=95, status=PENDING.
25|
26|### Implemented automation
27|
28|`web/backend/scheduler.py`:
29|
34|  - predictions exist (`preds >= 7`)
35|  - actual result not present yet
36|  - no test bundle exists yet
37|- If ready: materialize C-16 budget and run V52.5.6 runner in `REALTIME_AVAILABLE_ONLY`.
38|
39|### Dynamic ordering
40|
41|No-token models already run first via 04:00 batch. Shadow/token model order uses C-16 selected-voter rows if available, otherwise latest tensor strength fallback. This makes region/weekday/station-set differences automatic.
42|
43|### Verification
44|
38|
39|### Dynamic ordering
40|
41|No-token models already run first via 04:00 batch. Shadow/token model order uses C-16 selected-voter rows if available, otherwise latest tensor strength fallback. This makes region/weekday/station-set differences automatic.
42|
43|### Verification
44|
45|- VPS service active.
46|- `/api/health=200`.
47|- Scheduler log shows `/du-doan-test pre-result trigger: every 5 minutes, readiness-gated`.
48|- Live sync `artifacts/live_sync/20260506_075455/manifest.json`.
57|
58|---
59|
60|## V20.3.37.60 — Mobile two-column UI + C-16-prioritized shadow model order (2026-05-05 23:42 VN)
61|
62|### Scope
63|
64|Owner reported mobile `/du-doan-test` still hard to read and clarified model execution must prioritize fast lanes and strong bucket models to reduce risk of missing prediction windows. This pass keeps official untouched.
65|
66|### Changes
67|
68|- `web/frontend/du-doan-test.html`: mobile compare grid now remains 2 columns (official/test) with smaller cards, text, icons, badges, and spacing.
69|- `web/backend/scheduler.py`: added `_order_shadow_models_for_region()`.
70|- `_run_shadow_auto_eval()` now orders `SHADOW_AUTO_EVAL_MODELS` by:
71|  1. C-16 `du_doan_test_selected_voters` roles/scores for that date+region when available.
72|  2. latest tensor helpful/BT strength fallback.
73|  3. registry order fallback on error.
74|
75|### Verification
76|
77|- VPS service active; `/api/health=200`.
78|- Verified C-16 order for MN/MT/MB 2026-05-05. MB starts with `qwen3.6-plus`, `qwen3-coder`, `glm-5.1`, `qwen3-max-thinking`; Google V55 models remain watch/order by C-16 score until more tensor history.
75|### Verification
76|
77|- VPS service active; `/api/health=200`.
78|- Verified C-16 order for MN/MT/MB 2026-05-05. MB starts with `qwen3.6-plus`, `qwen3-coder`, `glm-5.1`, `qwen3-max-thinking`; Google V55 models remain watch/order by C-16 score until more tensor history.
79|
80|### Governance
81|
82|No-token models already run first via 04:00 batch. This change affects only shadow_auto_eval sequence. No official scoring, final bundle, production prediction semantics, or roster change.
83|
84|### Cross-links
85|
153|
154|---
155|
156|## V20.3.37.57 — C-16 Adaptive Model Budget Selector for `/du-doan-test` (2026-05-05 23:00 VN)
157|
158|### Scope
159|
160|Implemented the test-lane model budget selector requested by owner: use the full measured pool (29 components) but select only the strongest daily voter subset by `region + weekday + station-set + output_type=BT`. This is the foundation for reducing future AI runtime/token cost without affecting official `/du-doan`.
161|
162|### Implemented
163|
166|  - `du_doan_test_model_budget_daily`
167|  - `du_doan_test_selected_voters`
168|  - `du_doan_test_model_skip_reason`
169|- `web/backend/_du_doan_test_schema.py`: added new C-16 tables to `TEST_TABLES`.
170|- `web/backend/main.py`: added `_build_du_doan_test_model_budget_summary()` and returned `model_budget` in `/api/du-doan-test/mb` + `/api/du-doan-test/{region}`.
171|- `web/frontend/du-doan-test.html`: added **“🧠 Model mạnh hôm nay / C-16 Adaptive Budget”** section.
172|
173|### Selection result for 2026-05-05
174|
175|- MN: pool 29, measured 28, selected 10, watch 16, skip 3.
176|- MT: pool 29, measured 28, selected 8, watch 14, skip 7.
168|  - `du_doan_test_model_skip_reason`
169|- `web/backend/_du_doan_test_schema.py`: added new C-16 tables to `TEST_TABLES`.
170|- `web/backend/main.py`: added `_build_du_doan_test_model_budget_summary()` and returned `model_budget` in `/api/du-doan-test/mb` + `/api/du-doan-test/{region}`.
171|- `web/frontend/du-doan-test.html`: added **“🧠 Model mạnh hôm nay / C-16 Adaptive Budget”** section.
172|
173|### Selection result for 2026-05-05
174|
175|- MN: pool 29, measured 28, selected 10, watch 16, skip 3.
176|- MT: pool 29, measured 28, selected 8, watch 14, skip 7.
177|- MB: pool 29, measured 28, selected 8, watch 10, skip 11.
178|
178|
179|### Adaptive test output
180|
181|After budget surface verification, C-16 was also materialized as a real test-lane experiment method:
182|
183|- `MN_ADAPTIVE_BUDGET_SELECTOR_V1`: test_bt `52` vs official `15`, status WIN, would_save=1.
184|- `MT_ADAPTIVE_BUDGET_SELECTOR_V1`: test_bt `52` vs official `44`, status WIN, would_save=0 / would_break=0 (divergent hit, not official replacement proof).
185|- `MB_ADAPTIVE_BUDGET_SELECTOR_V1`: test_bt `41` vs official `83`, status LOSE.
186|
187|These rows were written only through `experimental_preview_shadow` → `du_doan_test_*`; official output remains unchanged.
188|
188|
189|### Governance
190|
191|All C-16 writes are to `du_doan_test_*` + `experimental_preview_shadow` only. No `final_bundles`, production `predictions`, official scoring/voting/prompt/roster/scheduler mutation. C-16 now produces a test-lane challenger output, but remains `output_eligible=0`.
192|
193|### Verification
194|
195|- VPS materializer 2026-05-05 ALL succeeded.
196|- Service active after restart; `/api/health=200`; `/du-doan-test=401` unauth; `/api/final-bundle?region=MN=200`.
197|- VPS backup `/root/Lottery_AI_Test/backups/c16_model_budget_20260505_2248/`.
198|- Live sync `artifacts/live_sync/20260505_230032/manifest.json`.
199|
200|### Cross-links
201|
202|- Phase checkpoint `artifacts/phase_checkpoints/V57_C16_ADAPTIVE_MODEL_BUDGET_SELECTOR_20260505.md`
203|- FU-132
204|
205|---
206|
207|## V20.3.37.56 — `/du-doan-test` Experience Lane (2026-05-05 21:41 VN)
208|
209|### Scope


===== docs/CURRENT_TRUTH_SSOT.md hits for V57_C16 =====
14|| Area | Current Truth | Status | Evidence | Source | Last Updated | Supersedes |
15||------|--------------|--------|----------|--------|:------------:|------------|
16|| V59 strict LO3/Xien verification for `/du-doan-test` | Owner caught a real verification bug: `/du-doan-test` could mark LO3/3-càng WIN by matching only the last 2 digits. Fixed API semantics in `web/backend/main.py` so LO3 requires full 3-digit suffix match from actual prize values, and xiên 2/3 require same-station hit when station data exists, matching official verifier. 2026-05-05 honest test status after fix: MN_ADAPTIVE BT 52 WIN but lo3 452 LOSE / xien2 [52,13] LOSE / xien3 [52,13,56] LOSE; MT_ADAPTIVE BT 52 WIN but lo3 752 LOSE / xien2 [52,46] LOSE / xien3 [52,46,44] LOSE; MB_ADAPTIVE BT 41 LOSE / lo3 341 LOSE / xien2 [41,98] LOSE / xien3 [41,98,19] LOSE. Any earlier LO3 WIN based only on 2D tail is invalid and classified as UI/API verification bug, not true win. | `STRICT_LO3_3DIGIT_ONLY + Xien_SAME_STATION + TEST_API_VERIFICATION_FIXED + OFFICIAL_UNCHANGED` | `web/backend/main.py`; `artifacts/phase_checkpoints/V59_LO3_XIEN_STRICT_VERIFICATION_FIX_20260505.md`; CHANGELOG V20.3.37.59 | VPS deploy + internal API bundle verification + route health 200 | 2026-05-05 | corrects V58/V57 test-axis display semantics |
17|| V57 C-16 Adaptive Model Budget Selector | `/du-doan-test` now has C-16 model budget intelligence and a real adaptive test-lane output method. New materializer `web/backend/_materialize_du_doan_test_model_budget.py` ranks the full measured pool (`total_pool_count=29`) by `region + weekday + station-set + output_type=BT`, using tensor strength, recent signal, unique/herd contribution, region penalties, and neutral latency placeholder (C-05 missing). New test-only tables: `du_doan_test_model_budget_daily`, `du_doan_test_selected_voters`, `du_doan_test_model_skip_reason`. API `/api/du-doan-test/mb` and `/api/du-doan-test/{region}` returns `model_budget`; UI shows “Model mạnh hôm nay / C-16 Adaptive Budget”. 2026-05-05 budget result: MN measured 28 selected 10; MT measured 28 selected 8; MB measured 28 selected 8. C-16 also writes `{REGION}_ADAPTIVE_BUDGET_SELECTOR_V1` through `experimental_preview_shadow` → `du_doan_test_*`: MN test_bt `52` vs official `15` WIN (would_save=1), MT test_bt `52` vs official `44` WIN (divergent hit, not replacement proof), MB test_bt `41` vs official `83` LOSE. Official untouched. | `C16_ADAPTIVE_BUDGET_TEST_OUTPUT_READY + TEST_ONLY + OUTPUT_IMPACT_FALSE + POOL_29_SELECTED_8_TO_10 + OFFICIAL_UNCHANGED` | `web/backend/_materialize_du_doan_test_model_budget.py`; `web/backend/main.py`; `web/frontend/du-doan-test.html`; `artifacts/phase_checkpoints/V57_C16_ADAPTIVE_MODEL_BUDGET_SELECTOR_20260505.md`; live sync `artifacts/live_sync/20260505_230032/manifest.json` + `20260505_231309/manifest.json`; CHANGELOG V20.3.37.57; FU-132 | VPS materializer + adaptive test bundle rows + API/UI deploy + route smoke + DB sync | 2026-05-05 | extends V56 experience lane |
18|| V56 `/du-doan-test` Experience Lane | Owner clarified experiment lane must allow daily experience/trial without waiting for official-promotion proof. V56 adds admin-only `EXPERIENCE_MODE` to `/du-doan-test`: read-only backend helper `_build_du_doan_test_experience_summary(region,date_str)` and frontend section “🚀 Trải nghiệm hôm nay”. It surfaces method rescues/breaks, `OFFICIAL_BASELINE_CLONE_BY_DESIGN`, `INDEPENDENT_AGREEMENT_WITH_OFFICIAL`, `TEST_METHOD_TRUE_RESCUE`, and V55 Google shadow picks. Verified for 2026-05-05: MN `MN_AI_CHAIN_PRESERVATION_V1` picked 52 WIN; MB `MB_PRIOR_REGION_CONTEXT_SAFE_V1` picked 98 WIN; `gemini-3-flash` MB WIN `[91,14]`; `gemini-3.1-pro` MB PARTIAL. MT official already WIN and shadow models watch only. Routes smoke OK (`/api/health=200`, `/du-doan=200`, `/du-doan-test=401`, `/api/du-doan-test/mn` unauth=401, `/api/final-bundle?region=MB=200`). Official path untouched. | `EXPERIENCE_MODE_READY + ADMIN_ONLY + TEST_ONLY + OUTPUT_IMPACT_FALSE + PROMOTION_ALLOWED_FALSE + OFFICIAL_UNCHANGED` | `web/backend/main.py`; `web/frontend/du-doan-test.html`; `artifacts/phase_checkpoints/V56_DU_DOAN_TEST_EXPERIENCE_LANE_20260505.md`; VPS backup `/root/Lottery_AI_Test/backups/v56_experience_lane_20260505_2133/`; live sync `artifacts/live_sync/20260505_214133/manifest.json`; CHANGELOG V20.3.37.56; FU-131 | VPS deploy + route smoke + direct helper verify | 2026-05-05 | extends V55 full-chain |
19|| V55 full-chain closeout 04/05 + 05/05 + scheduler preflight fix + 2-day materialization | TOTAL-FORCE V55 reconciled V52.5.7→V53→V53.1→V54 chain. 2026-05-04 closeout: MN BT 65 LOSE + lo2 PARTIAL (32 hit), MT BT 29 WIN + lo2 WIN, MB BT 09 LOSE + lo2 LOSE. 2026-05-05 closeout: MN BT 15 LOSE + lo2 LOSE, MT BT 44 WIN + lo2 PARTIAL, MB BT 83 LOSE + lo2 LOSE. Test lane on MN: SPECIALIST_ROSTER picked 32 on 04/05 (free win), AI_CHAIN_PRESERVATION picked 52 on 05/05 (free win). MT methods broke baseline win on both days (AI_CHAIN/PRIOR_REGION/STRENGTH chose 82 then 39 — `MT_AI_CHAIN_DESTRUCTIVE` pattern continues). MB no rescue on 04/05+05/05; `gemini-3-flash` shadow ngày đầu MB BT WIN ([91,14] both hit) — KEEP_CANDIDATE 14d. Rolling anchor 2026-05-05: MN BT 30d 56.7% (V54: 60%), MT 36.7% (V54: 33%), MB 20% unchanged; MN 7d 42.9% / MT 7d 71.4% / MB 7d 14.3%. Discovered + FIXED V55 scheduler preflight bug routing `gemma-*` to OpenRouter (key_missing) — gemma-4-31b had 0 rows on 05/05; bug fix in `scheduler.py` `_get_api_key_for_model` + `_preflight_check_provider_runtime` so gemma-* → Google lane via `GEMINI_KEY_SHADOW_NEW`. VPS deploy 20:08 VN after MB cycle. Materialized 04/05+05/05: loz_stage_trace 88+94=182 actual tails traced; mt_drop 10 rows; model_strength tensor anchor advanced 2026-05-02 → 2026-05-05 (8875 rows); weekday_blackspot anchor 2026-05-05 (21 rows: MB Wed/Fri + MT Fri = BLACK_SPOT_CONFIRMED, MT Mon downgraded to STRUCTURAL_RISK). V52.5.6 multi-region runner ALL ran on 05/05 (25 new bundles). `model_latency_cost_audit_daily` still NO_PER_MODEL_DURATION 100% → PRUNING_NOT_ALLOWED_NO_LATENCY. /du-doan-test remains `LIVE_PARALLEL_AUTO_PENDING_ONLY`. ZERO official mutation: predictions/final_bundles/lottery_results/model_daily_eval grew only via NATURAL_LIVE_GROWTH; `final_bundles` content unchanged for 04/05 closed rows. | `TWO_DAY_FORENSIC_ONLY + READY_FOR_TEST_LANE_ENHANCEMENT + READY_FOR_MEASUREMENT_ONLY_IMPLEMENTATION + NOT_READY_FOR_OFFICIAL_CHANGE + V55_PREFLIGHT_BUG_FIXED + LIVE_PARALLEL_AUTO_PENDING_ONLY + OFFICIAL_QUALITY_NOT_PROVEN_MIXED_SIGNAL_REGION_CONDITIONAL` | `artifacts/phase_checkpoints/TOTAL_FORCE_V55_20260504_20260505_CLOSEOUT_AND_NEXT_UPGRADE_PLAN.md`; `artifacts/_v55_state_20260505.json`; `artifacts/_v55_pre_hash_20260505.txt`; `artifacts/_v55_post_hash_20260505.txt`; `artifacts/_v55_official_closeout_20260504_20260505.json`; `artifacts/_v55_du_doan_test_closeout_20260504_20260505.json`; `artifacts/_v55_du_doan_test_ui_api_source_audit_20260505.json`; `artifacts/_v55_rolling_metrics_after_20260505.json`; `artifacts/_v55_mt_correct_but_dropped_20260504_20260505.json`; `artifacts/_v55_mt_correct_but_dropped_extra_20260504_20260505.json`; `artifacts/_v55_mb_ai_notoken_specialist_forensic_20260504_20260505.json`; `artifacts/_v55_loz_control_audit_20260505.json`; `artifacts/_v55_model_tensor_latency_pruning_readiness_20260505.json`; `artifacts/_v55_method_multilane_status_20260505.json`; `artifacts/live_watch/LIVE_WATCH_20260505_V55.md`; live sync `artifacts/live_sync/20260505_201101/manifest.json` + `20260505_203357/manifest.json`; CHANGELOG V20.3.37.55_full_chain | VPS DB sync + DB-proven closeout + materializer outputs + scheduler bug fix verify + source-hash guard | 2026-05-05 | extends V20.3.37.55 (does not supersede earlier morning add; this entry adds the closeout+fix+materialize result on top) |
20|| V55 add 3 Google direct shadow models | Owner-requested addition of `gemini-3.1-pro`, `gemini-3-flash`, `gemma-4-31b` to the SHADOW lane only (`output_eligible=False`, `provider='google'`, `status='SHADOW_AUTO'`, slots `completion_triggered_shadow` + `shadow_eval_post_verify`). Routed through `google.genai` SDK (`is_gemini` extended to also match `gemma*`). Per-model API id map: `gemini-3.1-pro→gemini-3.1-pro-preview`, `gemini-3-flash→gemini-3-flash-preview`, `gemma-4-31b→gemma-4-31b-it` (current Google ListModels). New PHASE-FIRST cohort `PFG-20260505-E` opened 2026-05-05 07:45 VN containing prior 5 + 3 new (8 total), `contract_required=True`. Per-model key isolation `GOOGLE_MODEL_KEYS` reads new env var `GEMINI_KEY_SHADOW_NEW` (Google AI Studio project `sxkt`, Tier 2); legacy `GEMINI_API_KEY` for `gemini-2.5-flash`/`gemini-2.5-pro` (output models) UNCHANGED. VPS post-restart counts: SHADOW_AUTO 13 (10→13), OUTPUT_ELIGIBLE 15 unchanged, ALL_RUNTIME 31 (28→31), `/api/health` registry_visible_model_count=31. Real Google API smoke 3/3 PASSED: gemini-3.1-pro 2.54s 151 tokens (thinking), gemini-3-flash 1.40s 57 tokens, gemma-4-31b 2.56s 65 tokens. Source hash for `predictions`/`final_bundles`/`lottery_results`/`model_daily_eval` unchanged because no scoring/voting/output path was touched. | `SHADOW_LANE_ONLY + OUTPUT_HASH_UNCHANGED + 3_MODELS_API_PROVEN + PHASE_FIRST_COHORT_PFG_20260505_E_LIVE + KEY_ISOLATION_VS_LEGACY + READY_FOR_NEXT_LIVE_CYCLE_2026_05_05` | `web/backend/model_registry.py` (3 entries, V20.3.37.55 block); `web/backend/gpt_analyzer.py` (`SHADOW_GATE_MODELS`, `PHASE_FIRST_GATE_HISTORY`, `GOOGLE_MODEL_KEYS`, `GOOGLE_MODEL_API_MAP`, `GOOGLE_DIRECT_SHADOW_MODELS`, dispatch); `/root/Lottery_AI_Test/.env` (key appended, idempotent); VPS backups `/root/Lottery_AI_Test/backups/v55_shadow_add_20260505_0750/`; `artifacts/_v55_vps_verify.py`, `artifacts/_v55_envload_check.py`, `artifacts/_v55_post_restart_check.py`, `artifacts/_v55_api_smoke.py`, `artifacts/_v55_list_models.py`; CHANGELOG V20.3.37.55; FU-125 | VPS scp + restart + `/api/health` 200 + venv python self-tests + real Google API smoke 3/3 + source-hash guard | 2026-05-05 | extends V20.3.37.54 |
21|| V54 natural live watch + measurement-only instrumentation | V54 ran during 2026-05-04 live day at 12:55 VN: MN official bundle exists (BT `65`, lo2 `[65,32]`, PENDING); MT/MB only auto_daily predictions, no final bundle/result yet; `/du-doan-test` has no 2026-05-04 test rows yet, so current day verdict is `WAIT_CLOSEOUT`. C-02 API source labels deployed (response-only metadata; no selection change). C-06 loz stage trace deployed measurement-only: new `loz_stage_trace_shadow` with 6174 rows over 60 closed days, showing `LOZ_LINE_SELECTION_MISS` MN 221 / MT 182 / MB 121 and `CANDIDATE_POOL_MISS` MN 105 / MT 90 / MB 73. C-15 weekday blackspot deployed measurement-only: `weekday_blackspot_shadow` 21 rows, confirming MB Wed/Fri and MT Mon/Fri as 30d blackspots. C-05 latency instrumentation not deployed because `gpt_analyzer.py` touches live model-call path before MT/MB cascade. Post-hash official behavior unchanged, but `final_bundles` hash changed because startup catch-up refreshed `updated_at/verified_at` timestamps for 2026-05-03 rows; BT/lo2/status content unchanged. | `V54_LIVE_WATCH_PRE_CLOSEOUT + C02_API_LABELS_DEPLOYED + C06_LOZ_TRACE_DEPLOYED + C15_BLACKSPOT_DEPLOYED + OFFICIAL_BEHAVIOR_UNCHANGED + FINAL_BUNDLES_TIMESTAMP_REFRESH_NOT_OUTPUT_CHANGE + WAIT_CLOSEOUT_20260504` | `artifacts/phase_checkpoints/TOTAL_FORCE_V54_NATURAL_LIVE_CLOSEOUT_MEASUREMENT_AND_TEST_LANE_CONTROL_20260504.md`; `artifacts/phase_checkpoints/_v54_state_20260504.json`; `artifacts/live_watch/LIVE_WATCH_20260504_V54.md`; `artifacts/_v54_api_source_labels_audit_20260504.json`; `artifacts/_v54_loz_stage_trace_plan_or_result_20260504.md`; `artifacts/_v54_mb_blackspot_alert_plan_or_result_20260504.md`; `artifacts/_v54_pre_hash_20260504.txt`; `artifacts/_v54_post_hash_20260504.txt`; CHANGELOG V20.3.37.54 | VPS live watch + response-only API enrich + measurement-only materializers + source-hash guard | 2026-05-04 | extends V20.3.37.53.1 |
22|| V53.1 owner deliverables: experimental-lane roadmap + official output timeline | Two owner-facing markdown deliverables landed (docs only, no code/DB change). `docs/EXPERIMENTAL_LANE_ROADMAP_20260504.md` documents how `/du-doan-test` runs today (LIVE_PARALLEL_AUTO_PENDING_ONLY), 6 phase ladder per method (Proposed → Design → Shadow_Backfill → Test_Lane_Parallel → Owner_Review → Production_Deploy), per-method status with sample sizes and gate criteria, model lifecycle (individual model gomming, shadow→voter promotion, AI weak pruning), UI roadmap V52.7+ (per-station strength chip, MT correct-but-dropped, station-aware loz). `docs/OFFICIAL_OUTPUT_IMPROVEMENT_TIMELINE_20260504.md` documents 4 production-improvement waves with explicit gate criteria and ETA: Wave 1 single-region single-method swap earliest 2026-06-15 (Composite V2 / AI_CHAIN MB / SPECIALIST MB), Wave 2 region-conditional pruning 2026-07-15 (after C-05 latency 30d), Wave 3 shadow→voter promotion 2026-08-04, Wave 4 family/region-weekday/station-aware aggregation 2026-08-15. Every owner-review milestone explicitly requires DECISION_LOG owner OK; no auto-deploy. ZERO code change this pass. | `OWNER_DELIVERABLES_DOCS_LANDED + EXPERIMENTAL_LANE_PHASES_DOCUMENTED + 4_WAVE_PRODUCTION_TIMELINE + GATE_CRITERIA_EXPLICIT + AGENT_NO_AUTO_DEPLOY + OFFICIAL_HASH_UNCHANGED + ZERO_CODE_CHANGE` | `docs/EXPERIMENTAL_LANE_ROADMAP_20260504.md`; `docs/OFFICIAL_OUTPUT_IMPROVEMENT_TIMELINE_20260504.md`; CHANGELOG V20.3.37.53.1; cross-link to V53 main report `artifacts/phase_checkpoints/TOTAL_FORCE_V53_FULL_REPORT_CHAIN_DU_DOAN_TEST_REALITY_AND_SAFE_NEXT_ACTION_20260503.md`; FU-115 | Owner deliverable docs only | 2026-05-04 | extends V20.3.37.53 (does not supersede; owner-facing roadmap/timeline only) |
23|| V53 / V52.5.8 full-chain audit + UI source-badge fix | TOTAL-FORCE V53 reconciled V39→V52.5.7 chain (all CONFIRMED, no overclaim). `/du-doan-test` audited 5 layers (UI/API/DB/code/log). DB confirms test methods are INDEPENDENT (2026-05-02 MB: 4 of 6 methods picked 91 WIN vs official 43 LOSE; 2026-05-03 MB AI_CHAIN_PRESERVATION test_bt=85 LOSE ≠ official 48 WIN, false_promotion=1). Owner concern "test shows official numbers" classified as `UI_LABEL_CONFUSION_INDEPENDENT_AGREEMENT_LOOKS_LIKE_CLONE` — when test method picks SAME as official it is consensus, not cloning. V52.6 UI fix: explicit source banner, picks-per-experiment table, `🟰 đồng thuận` / `🆚 khác chính` labels. `/du-doan-test` status remains `LIVE_PARALLEL_AUTO_PENDING_ONLY` (no scheduler auto-wire, V50 MB-only closeout evaluator). Official quality `OFFICIAL_QUALITY_NOT_PROVEN_MIXED_SIGNAL_REGION_CONDITIONAL`: 30d BT MN 60% / MT 33% / MB 20%; MB Wed/Fri 0/4 BT structural. Tensor `PRUNING_NOT_ALLOWED_NO_LATENCY`. Loz `LOZ_NOT_READY_FOR_RULE`. Source hashes for predictions/final_bundles/lottery_results/model_daily_eval IDENTICAL pre/post; scheduler_logs +12 from V52.6 service restart only. ZERO mutation to official. | `FULL_CHAIN_RECONCILED + UI_SOURCE_BADGE_FIX_SHIPPED + DB_PROVES_TEST_INDEPENDENT + LIVE_PARALLEL_AUTO_PENDING_ONLY + OFFICIAL_QUALITY_NOT_PROVEN + OFFICIAL_HASH_UNCHANGED + V52_5_NO_OVERCLAIM_DETECTED` | `artifacts/phase_checkpoints/TOTAL_FORCE_V53_FULL_REPORT_CHAIN_DU_DOAN_TEST_REALITY_AND_SAFE_NEXT_ACTION_20260503.md`; `_v53_full_report_chain_state_20260503.json`; `_v53_du_doan_test_reality_ui_api_db_audit_20260503.json`; `_v53_official_post_live_20260503_forensic.json`; `_v53_code_readiness_matrix_20260503.md`; `_v53_pre_hash_20260503.txt`; `_v53_post_hash_20260503.txt`; live sync `artifacts/live_sync/20260504_000308/manifest.json`; CHANGELOG V20.3.37.53; FU-114 update | VPS-synced DB + 5-layer audit + source-hash guard + V52.6 UI source badge fix | 2026-05-04 | extends V20.3.37.52.5 (does not supersede; UI clarity fix on top of V52.5.x test lane) |
24|| V52.5 multi-region parallel test lane | `/du-doan-test` is now a real parallel experimental lane for MN/MT/MB. New runtime tensor `model_strength_by_region_weekday_station_daily` (9052 rows), new multi-region preview `experimental_preview_shadow` (1098 rows after 60d backfill), new multi-region engine `_du_doan_test_engine.py` (579 runs/bundles/results, 13405 candidates/contributions across 30d), extended registry to 20 experiments across MN/MT/MB, multi-region API `/api/du-doan-test/{MN,MT,MB}` returning real `test_bundle` with full axes (BT/lo2/lo3/xien2/xien3), and multi-region daily runner `--region ALL`. Anti-leak: strength anchor strict D-1, MN uses D-1 only, MT uses D-1+MN(D), MB uses D-1+MN(D)+MT(D); never target-region same-day actuals. 60d measurement evidence: MB SPECIALIST_ROSTER fw=5/fl=0 (5 free wins); MN AI_CHAIN_PRESERVATION fw=4/fl=1 hits 32 vs 29; MT AI_CHAIN_PRESERVATION fw=8/fl=12 destructive (confirms owner's MT herding). Source hashes for `predictions`, `final_bundles`, `lottery_results`, `model_daily_eval` identical pre/post; `scheduler_logs +46` from service restart + test markers only. | `MULTI_REGION_TEST_LANE_LIVE_PARALLEL_V52_5 + OFFICIAL_HASH_UNCHANGED + ANTI_LEAK_ANCHORED + ADMIN_ONLY + STRENGTH_TENSOR_INTEGRATED` | `artifacts/phase_checkpoints/V52_5_MULTI_REGION_PARALLEL_TEST_LANE_20260503.md`; `artifacts/phase_checkpoints/V52_5_1_MODEL_STRENGTH_TENSOR_20260503.md`; `artifacts/_v52_5_1_pre_hash_20260503.txt`; `artifacts/_v52_5_7_post_hash_20260503.txt`; `artifacts/_v52_5_2_inspect_vps.py`; `artifacts/_v52_5_3_inspect_engine.py`; live sync `artifacts/live_sync/20260503_225849/manifest.json`; CHANGELOG V20.3.37.52.5; FU-114 | VPS multi-region materializer + engine + runner + admin-only API/UI + source-hash guard | 2026-05-03 | extends V20.3.37.52.5.1 (does not supersede MB-specific V50 lane; multi-region path coexists) |


===== docs/FOLLOW_UP_TRACKER.md hits for V57_C16 =====
28|
29|    ## Active Issues
30|
31|### FU-132 — C-16 adaptive model budget selector
32|
33|| Field | Value |
34||-------|-------|
35|| **issue_id** | FU-132 |
36|| **first_observed_in** | V20.3.37.57 |
37|| **status** | DEPLOYED_PENDING_LIVE_VERIFY |
38|| **next_action** | Run C-16 daily after closeout for 2-3 days. Then add an `ADAPTIVE_BUDGET_SELECTOR_V1` test method that builds a challenger candidate set only from `SELECTED_VOTER` rows. |
35|| **issue_id** | FU-132 |
36|| **first_observed_in** | V20.3.37.57 |
37|| **status** | DEPLOYED_PENDING_LIVE_VERIFY |
38|| **next_action** | Run C-16 daily after closeout for 2-3 days. Then add an `ADAPTIVE_BUDGET_SELECTOR_V1` test method that builds a challenger candidate set only from `SELECTED_VOTER` rows. |
39|| **owner_lock** | None for test-lane selector surface; YES for any official use |
40|| **last_evidence** | V57 materialized 2026-05-05: MN pool=29 measured=28 selected=10; MT pool=29 measured=28 selected=8; MB pool=29 measured=28 selected=8. UI/API surface deployed. Adaptive test output rows created: MN_ADAPTIVE test_bt=52 WIN would_save=1; MT_ADAPTIVE test_bt=52 WIN divergent hit; MB_ADAPTIVE test_bt=41 LOSE. |
41|| **regression_check** | Writes only `du_doan_test_model_budget_daily`, `du_doan_test_selected_voters`, `du_doan_test_model_skip_reason`; no official writes. |
42|| **notes** | C-16 now surfaces the selected-voter budget and writes `{REGION}_ADAPTIVE_BUDGET_SELECTOR_V1` to `experimental_preview_shadow`/`du_doan_test_*`. C-05 latency remains neutral placeholder until instrumentation exists. |
43|
44|---
45|
39|| **owner_lock** | None for test-lane selector surface; YES for any official use |
40|| **last_evidence** | V57 materialized 2026-05-05: MN pool=29 measured=28 selected=10; MT pool=29 measured=28 selected=8; MB pool=29 measured=28 selected=8. UI/API surface deployed. Adaptive test output rows created: MN_ADAPTIVE test_bt=52 WIN would_save=1; MT_ADAPTIVE test_bt=52 WIN divergent hit; MB_ADAPTIVE test_bt=41 LOSE. |
41|| **regression_check** | Writes only `du_doan_test_model_budget_daily`, `du_doan_test_selected_voters`, `du_doan_test_model_skip_reason`; no official writes. |
42|| **notes** | C-16 now surfaces the selected-voter budget and writes `{REGION}_ADAPTIVE_BUDGET_SELECTOR_V1` to `experimental_preview_shadow`/`du_doan_test_*`. C-05 latency remains neutral placeholder until instrumentation exists. |
43|
44|---
45|
46|### FU-131 — V56 `/du-doan-test` Experience Lane
47|
48|| Field | Value |
49||-------|-------|


===== docs/ACTIVE_ROADMAP_CROSS_REGION_LEAKAGE.md hits for V57_C16 =====
164|| 2026-05-04 | V54 live-window-aware pass at 12:55 VN. 2026-05-04 MN bundle exists (BT=65 lo2=[65,32]) pending result; MT/MB predictions only. Implemented C-02 API source labels (response-only), C-06 loz stage trace measurement table (`loz_stage_trace_shadow` 6174 rows), and C-15 weekday blackspot table (`weekday_blackspot_shadow` 21 rows). Confirmed MB Wed/Fri and MT Mon/Fri 30d blackspots. C-05 latency instrumentation deferred because it touches `gpt_analyzer.py` before live cascade. Post-hash: predictions/lottery_results/model_daily_eval/V52/V52.5 tables unchanged; `final_bundles` hash changed only because startup catch-up refreshed 2026-05-03 `updated_at/verified_at` timestamps (BT/lo2/status unchanged). | `artifacts/phase_checkpoints/TOTAL_FORCE_V54_NATURAL_LIVE_CLOSEOUT_MEASUREMENT_AND_TEST_LANE_CONTROL_20260504.md`, `_v54_state_20260504.json`, CHANGELOG V20.3.37.54, FU-117..FU-124 |
165|| 2026-05-05 (20:14 VN) | V55 full-chain pass after 04/05 + 05/05 closeouts. **Closeout truth:** 04/05 MN BT 65 LOSE + lo2 PARTIAL (32 hit), MT BT 29 WIN + lo2 WIN, MB BT 09 LOSE + lo2 LOSE; 05/05 MN BT 15 LOSE + lo2 LOSE, MT BT 44 WIN + lo2 PARTIAL, MB BT 83 LOSE + lo2 LOSE. **Test-lane wins on MN both days** (SPECIALIST_ROSTER 32 / AI_CHAIN_PRESERVATION 52 — free wins, gate not met). **MT herding pattern remains destructive** (AI_CHAIN broke baseline WIN on both days). **MB structural weak unchanged** (60d 26.7%, 7d 14.3%, Wed/Fri BLACK_SPOT_CONFIRMED). **Discovered + fixed scheduler preflight bug** introduced by V55: `gemma-*` was mis-routed to OpenRouter prefix list → key_missing → gemma-4-31b had 0 rows on 05/05. Fixed in `scheduler.py` (`_get_api_key_for_model` + `_preflight_check_provider_runtime`), deploy 20:08 VN after MB cycle. **Materialized 04/05+05/05** measurement surfaces: loz_stage_trace 182 rows, mt_drop 10 rows, weekday_blackspot anchor 2026-05-05 (21 rows), model_strength tensor anchor advanced 2026-05-02 → 2026-05-05 (8875 rows), experimental_preview_shadow 72 rows, V52.5.6 multi-region runner 25 new bundles for 05/05. **C-05 latency still 0/0 → PRUNING_NOT_ALLOWED_NO_LATENCY.** /du-doan-test still `LIVE_PARALLEL_AUTO_PENDING_ONLY`. ZERO official mutation; predictions/final_bundles/lottery_results/model_daily_eval grew only via natural live cycle. | `artifacts/phase_checkpoints/TOTAL_FORCE_V55_20260504_20260505_CLOSEOUT_AND_NEXT_UPGRADE_PLAN.md`, `_v55_state_20260505.json`, `_v55_pre_hash_20260505.txt`, `_v55_post_hash_20260505.txt`, `live_watch/LIVE_WATCH_20260505_V55.md`, CHANGELOG `V20.3.37.55_full_chain`, FU-126..FU-130, live sync `artifacts/live_sync/20260505_201101/manifest.json` + `20260505_203357/manifest.json` |
166|| 2026-05-05 (21:41 VN) | V56 `/du-doan-test` Experience Lane. Owner clarified that experiment/test lane should not wait 14/30/60 days just to let owner *experience* new methods; strict gates apply only to official promotion. Added read-only `experience` object to `/api/du-doan-test/mb` and `/api/du-doan-test/{region}`, plus frontend section “Trải nghiệm hôm nay (EXPERIENCE MODE)”. It surfaces method rescues/breaks, baseline clone vs independent agreement, and V55 Google shadow picks. Verified 2026-05-05: MN AI_CHAIN 52 WIN, MB PRIOR_REGION 98 WIN, `gemini-3-flash` MB WIN [91,14], `gemini-3.1-pro` MB PARTIAL. Routes smoke OK. ZERO official mutation; page remains admin-only/test-only/output_eligible=0/promotion_allowed=false. | `artifacts/phase_checkpoints/V56_DU_DOAN_TEST_EXPERIENCE_LANE_20260505.md`, CHANGELOG V20.3.37.56, FU-131, live sync `artifacts/live_sync/20260505_214133/manifest.json`, VPS backup `/root/Lottery_AI_Test/backups/v56_experience_lane_20260505_2133/` |
167|| 2026-05-05 (23:00 VN) | V57 C-16 adaptive model budget selector for `/du-doan-test`. Implemented model budget surface using full measured pool (29 components) and selecting daily voters by region+weekday+station-set+BT. New test-only tables `du_doan_test_model_budget_daily`, `du_doan_test_selected_voters`, `du_doan_test_model_skip_reason`. 2026-05-05 materialization: MN pool 29 / measured 28 / selected 10; MT pool 29 / measured 28 / selected 8; MB pool 29 / measured 28 / selected 8. API returns `model_budget`; UI shows “Model mạnh hôm nay / C-16 Adaptive Budget”. C-16 also now writes real test method `{REGION}_ADAPTIVE_BUDGET_SELECTOR_V1` via `experimental_preview_shadow` → `du_doan_test_*`: MN test_bt=52 WIN (would_save=1), MT test_bt=52 WIN divergent hit, MB test_bt=41 LOSE. ZERO official mutation. | `artifacts/phase_checkpoints/V57_C16_ADAPTIVE_MODEL_BUDGET_SELECTOR_20260505.md`, CHANGELOG V20.3.37.57, FU-132, live sync `artifacts/live_sync/20260505_230032/manifest.json` + `20260505_231309/manifest.json`, VPS backup `/root/Lottery_AI_Test/backups/c16_model_budget_20260505_2248/` |
168|| 2026-05-05 (07:56 VN) | V55 add 3 Google direct shadow models (`gemini-3.1-pro`, `gemini-3-flash`, `gemma-4-31b`) into SHADOW lane only. Owner-supplied Google AI Studio key (project sxkt, Tier 2) appended to `/root/Lottery_AI_Test/.env` as `GEMINI_KEY_SHADOW_NEW`; legacy `GEMINI_API_KEY` for `gemini-2.5-flash` / `gemini-2.5-pro` (output models) UNCHANGED. PHASE-FIRST cohort `PFG-20260505-E` opened at 07:45 VN with 8 models (5 prior + 3 new), `contract_required=True`. `is_gemini` predicate extended to also match `gemma*`. `GOOGLE_MODEL_API_MAP` routes registry id → current Google API name (`*-preview` for Gemini 3 family). Real Google API smoke 3/3 PASSED (PONG): gemini-3.1-pro 2.54s, gemini-3-flash 1.40s, gemma-4-31b 2.56s. VPS `/api/health` 200; SHADOW_AUTO 10→13; OUTPUT_ELIGIBLE 15 unchanged; ALL_RUNTIME 28→31. Source hash for predictions/final_bundles/lottery_results/model_daily_eval UNCHANGED. Deployed at 07:55 VN, well outside live windows (16:30/16:42/17:42). | CHANGELOG V20.3.37.55, FU-125, `artifacts/_v55_*` smoke + verify scripts, VPS backups `/root/Lottery_AI_Test/backups/v55_shadow_add_20260505_0750/` |
169|| 2026-05-03 | `/du-doan-test` full MB test lane V20.3.37.46: deployed separate `du_doan_test_*` schema + MB test engine; 7 test runs/bundles/results and 147 candidates/contributions for 2026-05-02. Official `/du-doan` unchanged. | `artifacts/phase_checkpoints/DU_DOAN_TEST_FULL_MODEL_TENSOR_MB_RECOVERY_20260503.md`, `_du_doan_test_full_engine_vps_run_20260503.txt`, CHANGELOG V20.3.37.46 |
170|| 2026-05-03 | MB `/du-doan-test` Phase 2 V20.3.37.45.2: added `MB_COMPOSITE_CHALLENGER_V2`, 30d backtest, and UI best-shadow/backtest snapshot. Composite 8/30 vs official 5/30, FW=5 FL=2 FP=2; gate not met, remains shadow-only. | `artifacts/_mb_test_phase2_summary_20260503.md`, `_mb_experimental_backtest_20260503_002427.md`, CHANGELOG V20.3.37.45.2 |
171|| 2026-05-03 | MB `/du-doan-test` experimental preview V20.3.37.45 deployed: admin-only route/API + `mb_experimental_preview_shadow` materializer/table. Official `/du-doan` unchanged. First shadow rows show 4 MB experiments selecting 91 over official 43 on 2026-05-02, would_flip_to_win=1. Source hash protected. | `artifacts/_du_doan_test_deploy_log_20260502.txt`, `_du_doan_test_vps_materialize_20260502.txt`, CHANGELOG V20.3.37.45 |
172|| 2026-05-02 | GLOBAL MODEL ? REGION ? WEEKDAY ? MB RECOVERY CONTROL PASS V20.3.37.44: built global model capability tensor (3,216 observations), model role matrix (198 aggregates), latency/value matrix (per-model latency gap identified), MB recovery experiment matrix, MB preview UI feasibility, region UI separation plan, prior-region signal matrix, rule/prompt conversion matrix, shadow control matrix, and master outstanding matrix. No production mutation. | `artifacts/phase_checkpoints/GLOBAL_MODEL_REGION_WEEKDAY_MB_RECOVERY_AUDIT_20260502.md`, `_model_capability_tensor_20260502.csv`, `_mb_recovery_experiment_matrix_20260502.json`, FU-087..FU-095 |
173|| 2026-05-02 | POST-LIVE TOTAL-FORCE CLOSEOUT + SYSTEM IMPACT AUDIT V20.3.37.42: live closeout complete. MN BT=73 WIN + lo2 WIN; MT BT=88 WIN + lo2 PARTIAL; MB BT=43 LOSE + lo2 PARTIAL via 91. PP1-WATCH-POST-MDE natural fire observed (1 MN event). P0/FU-065 coverage 18/18 clean. 8 safe post-closeout materializers ran on VPS; corrected replay rows refreshed to closeout KNOWN; VALID days now 13; today FW=0/FL=1; TIER 3 gate NOT met. Loz remains mixed/not output-ready. ZERO output mutation. | `artifacts/phase_checkpoints/POST_LIVE_TOTAL_FORCE_CLOSEOUT_AND_SYSTEM_IMPACT_20260502.md`, `_post_closeout_materialization_20260502.json`, `_corrected_replay_delta_after_live_20260502.txt`, CHANGELOG V20.3.37.42 |
174|| 2026-05-02 | TOTAL-FORCE LIVE STABILITY + MEASUREMENT CONTROL + CORRECTED REPLAY CONTINUATION V20.3.37.41 (read-only audit pass): live watch documented (MN ready BT=73 lo2=[73,54], PP-1 dampener fired on 54, MT/MB pre-cascade, rule quality alert flagged); 9 measurement tables persistence + semantic audit (1 LEAKY_REFERENCE_ONLY = single_vote_rescue_replay_shadow, 1 ACTIVE_ACCUMULATION = corrected_rescue_replay_shadow, 4 DIAGNOSTIC, 2 DROP_AS_DESIGNED, 1 RESEARCH); corrected replay 12 VALID_LIVE_DAY evaluation TIER 3 gate NOT MET on 4 of 8 criteria; Option A stop-guard PASSED (main.py grep clean); PP1-WATCH-POST-MDE V36 hook awaits first natural fire today ~13:20 VN; FU-065 verifier alias NOT REPRODUCING (18/18 methods in shadow_results 2026-05-01); rollover UX banner plan documented frontend-only awaiting owner OK; automation 4-stage plan; CP-1.3/1.4/X.1/X.4/X.6/2.2 reconciled. 5/5 source-table hashes IDENTICAL. 22/22 technical + 15/15 governance no-overclaim self-audit PASS. ZERO mutation to /du-doan, scoring, bundle, lane, prompt, model roster, scheduler. | `artifacts/phase_checkpoints/LIVE_STABILITY_MEASUREMENT_AND_ROLLOVER_AUDIT_20260502.md`, `_live_stability_state_20260502.json`, `LIVE_WATCH_20260502.md`, `_measurement_table_semantic_audit_20260502.json`, CHANGELOG V20.3.37.41, FU-082+FU-065+FU-085 status updates |
