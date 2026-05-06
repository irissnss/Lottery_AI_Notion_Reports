# V53 / V52.5.8 Code Readiness Matrix

> Date: 2026-05-04 00:30 VN  
> Pass: TOTAL-FORCE V53 / V52.5.8 controller audit  
> Hard lock: NO mutation of `final_bundles`, `predictions`, scoring, prompt, model roster, scheduler

| ID | Item | File(s) involved | Risk if code now | Mutate official? | Bucket | Why |
|---|---|---|---|---|---|---|
| C-01 | UI source banner + picks-per-experiment table + 🟰 đồng thuận / 🆚 khác chính labels | `web/frontend/du-doan-test.html`, `web/frontend/du-doan.html` | none | NO | `IMPLEMENT_NOW_UI_TEST_ONLY` ✅ DONE V52.6 | Owner concern UI-clarity blocker; no backend/DB risk |
| C-02 | API `source_table` + `is_clone_of_official` + `selection_time` + `result_known_at_selection` fields in `/api/du-doan-test/{region}` payload | `web/backend/main.py` | none | NO | `IMPLEMENT_NOW_UI_TEST_ONLY` | Adds telemetry fields only; no behavior change |
| C-03 | Multi-region closeout evaluator (current: V50 MB only) | `web/backend/_du_doan_test_closeout_evaluator.py` | none | NO | `IMPLEMENT_NOW_TEST_LANE_ONLY` | Writes only `du_doan_test_*` summaries |
| C-04 | Scheduler auto-wire for V52.5.6 runner (post-closeout for each region) | `web/backend/scheduler.py` | low | NO (writes only test tables) | `WAIT_DATA` | Need ≥3 manual clean closeouts before auto per FU-097 contract |
| C-05 | Per-model latency instrumentation in cascade timer | `web/backend/gpt_analyzer.py`, `web/backend/_materialize_v52_measurement_surfaces.py` | low | NO (writes only `model_latency_cost_audit_daily`) | `IMPLEMENT_NOW_MEASUREMENT_ONLY` | Unblocks pruning gate; required for cost reduction decision |
| C-06 | `loz_stage_trace` materializer (where exactly does the actual tail drop?) | new `_materialize_loz_stage_trace_shadow.py` | none | NO | `IMPLEMENT_NOW_MEASUREMENT_ONLY` | Owner asked for loz control; needs trace before any output policy change |
| C-07 | MT correct-but-dropped UI panel for `/du-doan-test` | `web/frontend/du-doan-test.html` | none | NO | `IMPLEMENT_NOW_UI_TEST_ONLY` | Surface `mt_model_hit_output_drop_shadow` rolling stats inside test UI |
| C-08 | Model roster pruning for production | `web/backend/model_registry.py`, `gpt_analyzer.py` | HIGH | YES | `OWNER_DECIDE` + `PRUNING_NOT_ALLOWED_NO_LATENCY` | Must complete C-05 first; sample needs ≥30 days latency before any propose |
| C-09 | Output policy change for loz line selection | `web/backend/main.py` `generate_final_bundle` | HIGH | YES | `WAIT_DATA` + `LOZ_NOT_READY_FOR_RULE` | Loz remains region/window-conditional; no rolling proof |
| C-10 | Composite Challenger V2 promote to official | `web/backend/main.py` | HIGH | YES | `WAIT_DATA` | 30d backtest +3 vs gate +4; sample insufficient |
| C-11 | Single-vote rescue regional unlock | `web/backend/main.py` | HIGH | YES | `DROP_AS_DESIGNED` + `LEAKY_REFERENCE_ONLY` | V37 path was leaky; V39 corrected replay still gate-locked |
| C-12 | Sunday retrain enabling new shadow models in production | `web/backend/scheduler.py`, `model_registry.py` | medium | YES | `OWNER_DECIDE` + `WAIT_DATA` | Need ≥30d shadow proof per model |
| C-13 | Strength-tensor-backed roster reduction in test lane only | `web/backend/_materialize_experimental_preview_shadow.py` | low | NO | `IMPLEMENT_NOW_TEST_LANE_ONLY` (after C-05) | Test lane variant; no official roster touch |
| C-14 | UI per-station/per-weekday strength chip on test_bundle | `web/frontend/du-doan-test.html` | none | NO | `IMPLEMENT_NOW_UI_TEST_ONLY` | Surface tensor data in test UI per owner ask |
| C-15 | Data-quality alert for MB Wed/Fri black spots | new shadow alert table | none | NO | `IMPLEMENT_NOW_MEASUREMENT_ONLY` | Make MB Wed/Fri 0/4 BT visible in admin UI |

This pass implements C-01 only. C-02/C-05/C-06/C-07/C-14/C-15 are next 3-day candidates. C-03/C-13 next 7-day after manual closeout proofs. Everything `WAIT_DATA` or `OWNER_DECIDE` is parked with explicit gate.
