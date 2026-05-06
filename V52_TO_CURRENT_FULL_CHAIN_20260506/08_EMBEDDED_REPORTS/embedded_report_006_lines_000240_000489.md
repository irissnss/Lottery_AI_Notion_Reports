## V20.3.37.55_full_chain — TOTAL-FORCE V55 closeout 04/05 + 05/05 + scheduler preflight fix + 2-day materialization (2026-05-05 20:14 VN)

### Scope

Full-chain V55 forensic pass after MN/MT/MB closeouts on 2026-05-05. Reads V52.5.7 → V53/V53.1 → V54 chain, classifies 04/05 + 05/05 official + test lane outcomes by region/method, refreshes rolling metrics, audits MT correct-but-dropped + MB AI weakness + loz stage trace + weekday blackspot. Discovered and fixed a scheduler preflight bug introduced by V55 (gemma-* was mis-routed to OpenRouter lane). Materialized 04/05 + 05/05 measurement surfaces (loz_stage_trace, mt_drop, v52, weekday_blackspot anchor 2026-05-05, model_strength tensor anchor 2026-05-05, experimental_preview_shadow MN/MT/MB, V52.5.6 multi-region runner ALL). ZERO official mutation.

### Closeout result (DB-proven)

- 2026-05-04: MN BT=65 LOSE + lo2 PARTIAL (32 hit). MT BT=29 WIN + lo2 WIN. MB BT=09 LOSE + lo2 LOSE.
- 2026-05-05: MN BT=15 LOSE + lo2 LOSE. MT BT=44 WIN + lo2 PARTIAL (44 hit). MB BT=83 LOSE + lo2 LOSE.
- Test lane rescues: MN_SPECIALIST_ROSTER picked 32 on 04/05 (free win); MN_AI_CHAIN_PRESERVATION picked 52 on 05/05 (free win). MT methods broke baseline win (AI_CHAIN, PRIOR_REGION, STRENGTH on 04/05). MB no method rescued.
- 3 V55 Google direct shadow models day 1: `gemini-3-flash` MB BT WIN ([91,14] both hit); `gemini-3.1-pro` MB PARTIAL; `gemma-4-31b` 0 rows due to scheduler preflight bug.

### Rolling metrics post-05/05 (anchor 2026-05-05, 30d)

- MN BT 56.7% (V54: 60%); LO2_FULL 30%; LO2_ANY 83.3%.
- MT BT 36.7% (V54: 33%); LO2_FULL 16.7%; LO2_ANY 66.7%. 7d MT BT 71.4% rising.
- MB BT 20% (V54: 20%); LO2_FULL 6.7%; LO2_ANY 36.7%. 7d MB BT only 14.3%.
- Weekday blackspot anchor 2026-05-05: MB Wed/Fri = WEEKDAY_BLACK_SPOT_CONFIRMED. MT Fri = BLACK_SPOT_CONFIRMED. MT Mon downgraded BLACK_SPOT → STRUCTURAL_RISK.

### Bug fixed (V55 scheduler preflight)

- `web/backend/scheduler.py` `_get_api_key_for_model`: branch `model.startswith("gemini") or model.startswith("gemma")` so Gemma routes to Google lane; per-model env `GEMINI_KEY_SHADOW_NEW` (or DB `gemini_key_shadow_new`) for shadow cohort, fallback `GEMINI_API_KEY` for legacy.
- `_preflight_check_provider_runtime`: also matches `model.startswith("gemma")` as `provider="google"`, before OpenRouter prefix list. Removed `'gemma'` from OpenRouter prefix list.
- VPS deploy lúc 20:08 VN (sau MB live window). Verify 13/13 shadow preflight ok=True; 3 Google direct shadow models all resolve `DEDICATED_GOOGLE_SHADOW (env GEMINI_KEY_SHADOW_NEW)`.
- VPS backup at `/root/Lottery_AI_Test/backups/v55_shadow_add_20260505_0750/scheduler.py.post_v55_fix`.

### V55 measurement materialization (04/05 + 05/05)

- `loz_stage_trace_shadow` 04/05: MN 39 + MT 27 + MB 22 = 88 actual tails traced.
- `loz_stage_trace_shadow` 05/05: MN 42 + MT 30 + MB 22 = 94 actual tails traced.
- `mt_model_hit_output_drop_shadow` 04/05: 5 rows (ai_drop=2). 05/05: 5 rows (ai_drop=4).
- `model_strength_by_region_weekday_station_daily` anchor advanced 2026-05-02 → 2026-05-05 (8875 rows).
- `weekday_blackspot_shadow` anchor 2026-05-05 (21 rows).
- `experimental_preview_shadow` 04/05+05/05 MN/MT/MB: 36 + 36 = 72 rows.
- `du_doan_test_*` 04/05 already had 25 bundles; 05/05 NEW 25 bundles + 25 results + 396 candidates + 396 model_contribution rows.
- `mb_experimental_preview_shadow` 05/05: 7 rows including `flip_win=1` (1 free win in shadow run).
- `model_latency_cost_audit_daily` 04/05+05/05: 50+81 rows but `latency_available=0/0` and `NO_PER_MODEL_DURATION` 100% — C-05 still BROKEN_NEEDS_FIX.

### Test-lane status (unchanged)

`/du-doan-test` remains `LIVE_PARALLEL_AUTO_PENDING_ONLY`. V52.5.6 multi-region runner is still manual; C-03 multi-region closeout evaluator (next gate after 3-5 clean closeouts) and C-04 scheduler auto-wire (after evaluator stable) remain on the WAIT list.

### Next-action plan (no production deploy in this pass)

- 24h: V55 fixes are live (above).
- 3d: daily forensic 06-08/05 + watch first run with `gemma-4-31b` 06/05.
- 5-7d: build C-07 MT panel + C-14 chip UI + C-15 alert UI (UI-test-only); start C-05 latency instrumentation outside live windows.
- 14d (~19/05): owner evidence pack for MN-only AI_CHAIN/SPECIALIST + V55 cohort; no production deploy.
- 30d (~04/06): C-05 deployed + Composite V2 review; pruning proposal test-lane only.
- 60-105d: Wave 1 official output improvement gating (per OFFICIAL_OUTPUT_IMPROVEMENT_TIMELINE_20260504.md).

### Hash / mutation guard

`predictions`, `final_bundles`, `lottery_results`, `model_daily_eval` grew only via NATURAL_LIVE_GROWTH (today's predictions + bundles + scrape + eval). All measurement/test/diagnostic table changes carry `official_output=false`, `output_impact=false`, `output_eligible=0`. No scoring/voting/output policy was changed. `scheduler_logs` grew naturally + 1 service restart for V55 preflight fix.

### Cross-links

- FU-126 V55 2-day forensic
- FU-127 V55 loz stage trace 04/05+05/05
- FU-128 V55 latency/cost still blocked
- FU-129 V55 model strong/weak tensor advanced
- FU-130 V55 test-lane auto-wire readiness still pending
- Phase checkpoint: `artifacts/phase_checkpoints/TOTAL_FORCE_V55_20260504_20260505_CLOSEOUT_AND_NEXT_UPGRADE_PLAN.md`
- Live watch: `artifacts/live_watch/LIVE_WATCH_20260505_V55.md`
- State: `artifacts/_v55_state_20260505.json`

---

## V20.3.37.55 — Add 3 Google direct shadow models (Gemini 3.1 Pro / Gemini 3 Flash / Gemma 4 31B) (2026-05-05 07:56 VN)

### Scope

Owner-requested addition of three new Google AI Studio (project `sxkt`, Tier-2) models into the SHADOW lane only. Zero impact on `/du-doan` output, scoring, bundle voting, output roster, or live cascade. Deployed in the morning (07:55 VN), well outside the 16:30/16:42/17:42 live windows.

### Implemented

- **Registry add** (`web/backend/model_registry.py`): three new entries with `status='SHADOW_AUTO'`, `provider='google'`, `output_eligible=False`, `allowed_regions=['MN','MT','MB']`, `schedule_slots=['completion_triggered_shadow','shadow_eval_post_verify']`:
  - `gemini-3.1-pro` (Gemini 3.1 Pro)
  - `gemini-3-flash` (Gemini 3 Flash)
  - `gemma-4-31b` (Gemma 4 31B IT)
- **Distribution policy** (`gpt_analyzer.MODEL_DISTRIBUTION_POLICY`): all three set to `FULL_CONTEXT` so they receive system prompt + dynamic prompt + context pack + reasoning rulebook + PHASE-FIRST GATE.
- **Routing** (`gpt_analyzer.analyze_and_predict`): `is_gemini` predicate extended to also match models starting with `gemma`, so Gemma 4 31B routes through `_call_gemini` (google.genai SDK).
- **API model name map** (`gpt_analyzer.GOOGLE_MODEL_API_MAP`): keeps stable registry id but routes to the actual API name returned by Google `ListModels` on 2026-05-05:
  - `gemini-3.1-pro` → `gemini-3.1-pro-preview`
  - `gemini-3-flash` → `gemini-3-flash-preview`
  - `gemma-4-31b` → `gemma-4-31b-it`
- **Per-model key isolation** (`gpt_analyzer.GOOGLE_MODEL_KEYS`): the new shadow cohort reads `GEMINI_KEY_SHADOW_NEW` (project sxkt, Tier-2). Output models `gemini-2.5-flash` / `gemini-2.5-pro` keep using the legacy `GEMINI_API_KEY` unchanged.
- **PHASE-FIRST cohort** (`gpt_analyzer.SHADOW_GATE_MODELS` + `PHASE_FIRST_GATE_HISTORY`): closed cohort `PFG-20260428-D` at `2026-05-05 07:44:59`, opened new cohort `PFG-20260505-E` at `2026-05-05 07:45:00` containing the prior 5 + the 3 new Google direct shadow models (8 total). All gated models keep `contract_required=True`.
- **VPS env**: `GEMINI_KEY_SHADOW_NEW` appended to `/root/Lottery_AI_Test/.env` (the actual file `env_loader.PROJECT_ENV_PATH` reads — confirmed via load_project_env then os.getenv). Backend-local `.env` left untouched after a temporary stray entry was removed.

### Live API smoke test (real Google AI Studio call, project sxkt key)

- `gemini-3.1-pro` → `gemini-3.1-pro-preview`: `PONG` in 2.54s, 151 tokens (input 9, output 2, ~140 thinking).
- `gemini-3-flash` → `gemini-3-flash-preview`: `PONG` in 1.40s, 57 tokens.
- `gemma-4-31b` → `gemma-4-31b-it`: `PONG` in 2.56s, 65 tokens.

### Verification

- VPS `/api/health` 200 OK; service active V20.3.36 PID 712542 since 07:55:55.
- Registry counts: `SHADOW_AUTO=13` (10 → 13), `OUTPUT_ELIGIBLE=15` unchanged, `ALL_RUNTIME=31` (28 → 31), `registry_visible_model_count=31` from API.
- All three models present in shadow batch for MN/MT/MB (`completion_triggered_shadow`).
- All three models report `cohort=PFG-20260505-E gate_applied=True contract_required=True status=CURRENT`.
- Two Google keys present and distinct (legacy `GEMINI_API_KEY` length 39 prefix `<REDACTED_GOOGLE_API_KEY>` ; shadow `GEMINI_KEY_SHADOW_NEW` length 39 prefix `<REDACTED_GOOGLE_API_KEY>`).

### Hash guard

Source hash unchanged for the 4 forensic tables `predictions`, `final_bundles`, `lottery_results`, `model_daily_eval` because no scoring/voting/output code path was touched. `scheduler_logs` grew naturally from one service restart at 07:55:55. Backups retained at `/root/Lottery_AI_Test/backups/v55_shadow_add_20260505_0750/{model_registry.py.bak,gpt_analyzer.py.bak,env.bak,project_root_env.bak}`.

### Risk notes

- Gemini 3.1 Pro is a thinking model; runtime call uses `max_output_tokens=65536` so Pro will not hit `MAX_TOKENS` like the 64-token smoke probe did.
- All three remain `output_eligible=False`; `/du-doan` cannot be affected by them. Scheduler picks them up via registry-derived `SHADOW_AUTO_EVAL_MODELS` (no hardcoding).
- The Google `*-preview` suffix is current as of 2026-05-05 ListModels. If Google drops the suffix later, only the `GOOGLE_MODEL_API_MAP` entry needs updating; registry id stays stable for measurement continuity.

### Cross-links

- FU-125
- Active roadmap row 2026-05-05
- Phase checkpoint `artifacts/phase_checkpoints/SHADOW_ADD_GOOGLE_DIRECT_COHORT_20260505.md`

---

## V20.3.37.54 — Natural live watch + API source labels + loz trace + blackspot measurement (2026-05-04 13:20 VN)

### Scope

V54 live-window-aware pass. Started at 12:55 VN after MN bundle and before MN scrape / MT-MB cascade. No official selection logic, scoring, prompt, model roster, or output policy changed.

### Implemented

- **C-02 API source labels** in `web/backend/main.py`: `/api/du-doan-test/{region}` and MB legacy endpoint now return `source_proof` plus per-test fields such as `official_baseline_source_table`, `test_output_source_table`, `candidate_pool_source`, `is_clone_of_official`, `is_independent_agreement_with_official`, `selection_time`, `result_known_at_selection`, `is_realtime_prediction`, and `is_post_closeout_diagnostic`.
- **C-06 loz stage trace**: new `web/backend/_materialize_loz_stage_trace_shadow.py` + new table `loz_stage_trace_shadow` (6174 rows, 60 closed days through 2026-05-03).
- **C-15 weekday blackspot alert**: new `web/backend/_materialize_weekday_blackspot_shadow.py` + new table `weekday_blackspot_shadow` (21 rows, anchor 2026-05-03, 30d window).

### Live watch

- 2026-05-04 MN official bundle exists: BT `65`, lo2 `[65,32]`, PENDING result.
- MT/MB have auto_daily predictions only; no final bundle or result yet at 12:55 VN.
- No 2026-05-04 test rows yet. Verdict: `WAIT_CLOSEOUT`.

### Measurement findings

- Loz trace 60d: `LOZ_LINE_SELECTION_MISS` = MN 221, MT 182, MB 121; `CANDIDATE_POOL_MISS` = MN 105, MT 90, MB 73.
- Weekday blackspots 30d: MB Wed/Fri = `WEEKDAY_BLACK_SPOT_CONFIRMED`; MT Mon/Fri = `WEEKDAY_BLACK_SPOT_CONFIRMED`.

### Guardrail finding

Post-hash detected `final_bundles` hash changed with count unchanged. Forensic shows only `updated_at/verified_at` for 2026-05-03 rows refreshed from `12:50:01` to `13:05:07` after service restart/startup catch-up; BT/lo2/status content did not change. Label: `OFFICIAL_TABLE_TIMESTAMP_REFRESH_BY_STARTUP_CATCHUP`. No output behavior mutation.

### Hash guard

`predictions`, `lottery_results`, `model_daily_eval`, V52 measurement tables, and V52.5 test-lane tables unchanged. `scheduler_logs` +19 from service restart + route smoke. New diagnostic tables only: `loz_stage_trace_shadow`, `weekday_blackspot_shadow`.

Evidence: `artifacts/phase_checkpoints/TOTAL_FORCE_V54_NATURAL_LIVE_CLOSEOUT_MEASUREMENT_AND_TEST_LANE_CONTROL_20260504.md`.

## V20.3.37.53.1 — Owner deliverables: experimental-lane roadmap + official output timeline (docs only, 2026-05-04 00:55 VN)

### Pass type

Two owner-facing markdown deliverables. ZERO code change. ZERO DB write. ZERO official mutation.

### Files added

- `docs/EXPERIMENTAL_LANE_ROADMAP_20260504.md` — luồng thực nghiệm hiện chạy thế nào, 6 phase ladder mỗi method đi qua, lifecycle model individual/shadow/AI weak, UI nâng cấp roadmap V52.7+, đo lường mới khi nào ra.
- `docs/OFFICIAL_OUTPUT_IMPROVEMENT_TIMELINE_20260504.md` — per-method/measurement/mechanism status, gate criteria cụ thể, 4 wave production cải tiến với ETA earliest 2026-06-03 / 2026-06-15 / 2026-07-04 / 2026-08-15.

### Key timeline anchors

- **2026-05-07 (+3 ngày)**: ship C-02 API source labels + C-05 per-model latency instrument + C-07 MT correct-but-dropped panel + C-14 per-station/weekday strength chip.
- **2026-05-11 (+7 ngày)**: ship C-03 multi-region closeout evaluator + M-02 loz stage trace + M-04 family contribution + M-08 black-spot alert.
- **2026-05-15 (+11 ngày)**: review C-04 scheduler auto-wire after ≥5 manual closeout sạch.
- **2026-06-03 (+30 ngày)**: Wave 1 owner review window — Composite V2 / AI_CHAIN MB / SPECIALIST MB candidates.
- **2026-06-15 (+42 ngày)**: Wave 2 owner review — region-conditional pruning.
- **2026-07-04 (+60 ngày)**: Wave 3 owner review — shadow→voter promotion.
- **2026-08-15 (+105 ngày)**: Wave 4 owner review — family-aware / region-weekday-aware aggregation production.

Every owner-review milestone is "agent trình evidence pack", NOT auto-deploy.

## V20.3.37.53 / V52.5.8 — Full-chain controller audit + UI source-badge fix (VPS deployed, 2026-05-04 00:30 VN)

### Pass type

Full-chain forensic audit (V39 → V52.5.7) + `/du-doan-test` reality audit (UI/API/DB/code/log) + official 2026-05-03 post-live forensic + safe next-action plan. Single safe code change shipped (V52.6 UI labels). ZERO mutation to `/du-doan`, `final_bundles`, production `predictions`, scoring, prompt, model roster, scheduler.

### Owner concern resolved

Concern: "luồng thực nghiệm vẫn hiển thị các số dự đoán do luồng official". Verdict: `UI_LABEL_CONFUSION_INDEPENDENT_AGREEMENT_LOOKS_LIKE_CLONE` — DB confirms test methods pick INDEPENDENTLY (e.g., 2026-05-02 MB official=43 LOSE while 4 of 6 V52.5.2 methods independently picked 91 WIN; 2026-05-03 MB AI_CHAIN_PRESERVATION test_bt=85 LOSE ≠ official 48 WIN with false_promotion=1). When test method picks the SAME number as official it is independent agreement (consensus around top1 strong), not cloning.

### V52.6 UI source-badge fix shipped

- `renderSourceBanner` explains exactly which source table feeds each column.
- `renderExperimentSummary` table at top shows ALL 6 method picks with their BT and `🟰 đồng thuận` / `🆚 khác chính` chips.
- `diffChip` text changed from `= chính` / `≠ chính` to `🟰 đồng thuận` / `🆚 khác chính` with hover tooltip clarifying agreement vs clone.
- Footer-note expanded to mention `experimental_preview_shadow` and explicit "đọc `final_bundles` chỉ để hiển thị baseline".
- Cache buster on `/du-doan` admin link bumped to `?v=20260504-v52-6-source-badges`.

### Findings (rolling, anchor 2026-05-03)

- Official 30d BT: MN 60% / MT 33% / MB 20%. LO2_FULL: MN 33% / MT 17% / MB 7%. LO2_ANY: MN 83% / MT 67% / MB 43%.
- Verdict: `OFFICIAL_QUALITY_NOT_PROVEN_MIXED_SIGNAL_REGION_CONDITIONAL`. MB Wed/Fri 0/4 BT (structural). MT Mon/Fri 0/4 BT.
- `/du-doan-test` status remains `LIVE_PARALLEL_AUTO_PENDING_ONLY`: schema/engine/multi-region API/UI/runner exist; scheduler auto-wire NOT enabled; closeout evaluator V50 MB-only.

### Hard locks reaffirmed

- ZERO write to `final_bundles`, `predictions`, `generate_final_bundle()`, scoring, bundle voting, lane weights, verdict weights, output policy, model roster, production prompt.
- `model_latency_cost_audit_daily` 3273/3273 still NO_PER_MODEL_DURATION → `PRUNING_NOT_ALLOWED_NO_LATENCY`.
- Loz `LOZ_SIGNAL_MIXED + LOZ_REGION_CONDITIONAL + LOZ_NOT_READY_FOR_RULE`.

### Hash guard

Pre `artifacts/_v53_pre_hash_20260503.txt` vs post `artifacts/_v53_post_hash_20260503.txt`. Source hashes for `predictions`, `final_bundles`, `lottery_results`, `model_daily_eval` IDENTICAL. V52 measurement tables and V52.5 test-lane tables IDENTICAL. Only `scheduler_logs` +12 from `lottery` service restart on V52.6 deploy (no production scheduler run).

### Next-action plan

24h: observe natural live closeout 2026-05-04. NO code change.  
3d: implement C-02 API source labels, C-05 per-model latency instrumentation, C-07 MT correct-but-dropped panel.  
7d: implement C-03 multi-region closeout evaluator + C-13 strength-aware roster (test lane only) after manual closeout proofs.  
14d: re-evaluate MB SPECIALIST_ROSTER fw=5/fl=0; if pattern holds, propose owner unlock package.

Evidence: `artifacts/phase_checkpoints/TOTAL_FORCE_V53_FULL_REPORT_CHAIN_DU_DOAN_TEST_REALITY_AND_SAFE_NEXT_ACTION_20260503.md`.

## V20.3.37.52.5 — Multi-region parallel experimental test lane (VPS deployed, 2026-05-03 23:55 VN)

### Scope

Real parallel experimental lane mirroring `/du-doan` for MN/MT/MB, strictly admin-only `/du-doan-test`. All test-lane rows are flagged `official_output=false`, `output_impact=false`, `test_only=1`. ZERO mutation to `/du-doan`, `final_bundles`, production `predictions`, scoring, prompt, model roster, or scheduler.

### What landed (V52.5.1 → V52.5.7)

- `web/backend/_compute_model_strength_tensor.py` + new table `model_strength_by_region_weekday_station_daily` (V52.5.1, 9052 rows).
- `web/backend/_materialize_experimental_preview_shadow.py` + new table `experimental_preview_shadow` (V52.5.2, 1080 rows / 60d for MN/MT/MB × 6 experiments).
- `web/backend/_du_doan_test_engine.py` multi-region engine (V52.5.3, 540 runs/bundles/results across 3 regions × 30 days).
- `web/backend/_du_doan_test_schema.py` registry extended to 20 experiments across MN/MT/MB (V52.5.4).
- `web/backend/main.py` `api_du_doan_test_region` extended for MN/MT to return real `test_bundle` (V52.5.5); UI label bumped to v52.5; `/du-doan` admin link cache buster `?v=20260503-v52-5-live-parallel`.
- `web/backend/_du_doan_test_daily_runner.py` multi-region with `--region MN/MT/MB/ALL` and `--mode REALTIME_AVAILABLE_ONLY/POST_CLOSEOUT_DIAGNOSTIC_FULL_25` (V52.5.6).

### Selected 60d evidence (measurement-only, no official change)

- MB SPECIALIST_ROSTER: fw=5, fl=0 (5 free wins).
- MB STRENGTH_WEIGHTED V52.5.2: fw=8, fl=7, hits 19 vs official 18.
- MN AI_CHAIN_PRESERVATION: fw=4, fl=1, hits 32 vs official 29.
- MN SPECIALIST_ROSTER: fw=3, fl=0.
- MT AI_CHAIN_PRESERVATION: fw=8, fl=12 (destructive — confirms owner's MT herding observation).
- MT STRENGTH_WEIGHTED V52.5.2: fw=5, fl=6 (still negative net).

### Anti-leakage

Strength tensor anchored strictly D-1. MN selection uses D-1 only. MT selection uses D-1 + MN(D) actuals. MB selection uses D-1 + MN(D) + MT(D) actuals. Target-region same-day actuals are NEVER used for selection.

