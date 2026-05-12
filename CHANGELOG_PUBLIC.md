## V105.31 — CURRENT TRUTH CLEAN WRAPPER + SHADOW NO-MISSING PUBLIC SSOT (2026-05-12 11:35 VN)

- Created `V105_31_CURRENT_TRUTH_CLEAN_WRAPPER_20260512/` and `evidence/V105_31_CURRENT_TRUTH_CLEAN_WRAPPER.md` as the clean public current truth after V105.30d/e.
- Public SSOT now explicitly states: MN 2026-05-12 official `auto_daily=15/15`; shadow `shadow_auto_eval=13/13`; `missing_shadow=[]`; `glm-5.1` is a persisted diagnostic empty row due `finish_reason=length`, with no fabricated numbers.
- Shadow no-missing contract wording added: only `HARD_TIMEOUT` / `WAITING_TIMEOUT` may remain truly missing; non-timeout system/provider/parser/empty-output failures must persist diagnostic rows.
- GLM policy added as owner-gated proposal: `glm-5.1_compact_json_profile`, JSON-only, no explanation/CoT, max 2 tails, reduced context; no provider/manual re-call without owner OK.
- Rule105 terminology normalized: prize-source lock applies by `source_region`; `true_violation_count=0`; 30 prior flags are false positives / examination trace only; production `mined_rules` untouched; quarantine withdrawn.
- Natural verify remains `NATURAL_VERIFY_PENDING` until MT/MB complete naturally. Experiments remain HOLD / DO_NOT_PROMOTE; AI strongest-first remains HOLD.

---

## V105.30c — PUBLIC REPORT REFRESH / STALE WORDING CLEANUP (2026-05-12 10:08 VN)

- Rà lại `README.md` + `V105_30_FINALIZATION_REPORT.md`: thêm **READ THIS FIRST** để override các dòng cũ về `SSH_DEPLOY_KEY_PENDING`, `HTTPS_REMOTE_STILL_ACTIVE`, `QUARANTINE_INVALID_RECOMMENDED`.
- Chốt public truth hiện tại: GitHub account-level SSH OK; public mirror push SSH; Notion V105.30 deferred; GitHub raw là SSOT public.
- Rule105: `source_region` lock → **0 true violations**; 30 prior flags are false positives, historical examination trace only.
- Còn mở thật sự: natural MN cascade verify, AI strongest-first runtime reorder, strength tensor/runtime manifest cron decisions; all prediction experiments remain HOLD / DO_NOT_PROMOTE.

---

## V105.30b — RULE105 PRIZE-SOURCE RECHECK + PUBLIC MIRROR ONLY (2026-05-12)

- **Owner correction (prize-source lock):** áp dụng theo **source_region** (đài nguồn rule), không phải `target_region`. Audit lại: **0** vi phạm thật trên 105 rules đang active; 30 cờ cũ trong shadow audit là **false positive** (ví dụ MN khai thác từ nguồn MB vẫn được phép dùng prize kiểu MB). Không cách ly `mined_rules` production.
- **GitHub SSH:** xác thực account-level OK (`Hi irissnss! You've successfully authenticated`). Mirror public chỉ cần **`irissnss/Lottery_AI_Notion_Reports`** raw; push qua SSH.
- **Notion V105.30:** owner yêu cầu **tạm bỏ qua / không ưu tiên** — tra cứu dùng GitHub raw (index + `LATEST_REPORT.json`).

---

## V105.30 — TOTAL FORCE FINALIZATION: SAFE_STDIO VPS DEPLOY + RULE105 STRICT SHADOW + SSOT V105.29 PUBLIC LIVE (2026-05-12 01:48 VN)

- Owner approval string `A,A,A,A,A,A,A,A,A,A,A,B,A,A,A` executed.
- **LANE 1 (P0)**: `_safe_stdio_ctx` wide DEPLOYED LIVE to VPS. `scheduler.py` md5 `9c17595d3dd5c0fa323bbaf4bf221f34` (= local). Service active. 6/6 endpoints 200. Journal 5-min: closed_file_count=0, provider_call_count=0. Backup `/root/Lottery_AI_Test/backups/v105_30_safe_stdio_20260512_012511/scheduler.py.bak`.
- **LANE 2**: SSH ed25519 ready; VPS SSH OK. **Update V105.30b:** GitHub **account-level** SSH xác thực OK (`Hi irissnss!`); push mirror `Lottery_AI_Notion_Reports` qua `git@github.com` (không cần HTTPS/GCM cho luồng này khi đã add Personal SSH key).
- **LANE 3**: Public raw `LATEST_REPORT.json` advanced **V105.27 → V105.29** in commit `18ddf38`. 27 files / 9933 insertions / 119 deletions. desktop.ini + transcripts + commit helpers now gitignored.
- **LANE 4 (#12 B)**: Rule105 strict shadow re-mine built (tables + so sánh coverage). **Bổ sung V105.30b:** audit sai lệch do nhầm **target_region**; sau khi owner chốt lock theo **source_region**, `v10530_rule105_recheck` = **0** violation thật — các cờ “30 vi phạm” chỉ còn giá trị lịch sử shadow, không áp cho production.
- **LANE 5**: `docs/SIGNAL_LAYER_REGISTRY.md` created with 13 canonical signal layers.
- **LANE 6**: Region/Weekday/Station_set independence matrix verified. MT D-2 leak 7d = 0; MB D-2 leak 7d = 0.
- **LANE 7-11**: All experiment lanes HOLD: lose-carryover (DO_NOT_PROMOTE), Top2/Bundler (shadow), MB_D_v2 (Option A REJECTED), V102 relaxed (HOLD), AI strongest-first (shadow 7d).
- **LANE 12**: Official 4-table row counts identical pre/post (4791/219/14655/4655). sha256 drift only from VPS-side natural cascade between live syncs (hash double-check on static DB = identical 4/4). Provider call count = 0. MT protect preserved.
- **LANE 13**: Governance local đã sync trong session V105.30. **Public SSOT:** tra cứu ưu tiên GitHub raw (`REPORT_INDEX.md`, `LATEST_REPORT.json`). Trang Notion V105.30 **tạm hoãn** theo owner — không chặn release public.
- Final verdict: `V105_30_STABILITY_PASS_FOR_SAFE_STDIO` + `DEPLOYED_PENDING_NATURAL_VERIFY` (chờ MN cascade ~16:30 VN). Toàn cục `PARTIAL_NOT_PASS` cho prediction quality lanes (vẫn `DO_NOT_PROMOTE`).

---

## V105.29 — TOTAL FORCE NO-MISS CONTROL + LOSE-CARRYOVER SIGNAL LAYER + RUNTIME STABILITY (2026-05-12 00:55 VN)

- 20 LANE audit V105.23→V105.29; 14 lanes PASS, 2 lanes open (`_safe_stdio_ctx` VPS deploy + AI priority reorder), 1 governance gate (PRIZE_SOURCE_VIOLATION).
- V105.29 Lose-Carryover Signal Layer materialized (shadow-only): 4 tables, 30d backtest for 6 paths. All paths break_ratio 0.93-0.99 → `LOSE_CARRYOVER_DO_NOT_PROMOTE`. Useful only as supporting prompt-context when Rule105/source-pool/model-strength also confirm.
- Rule105 vs V101 separation audit (21 buckets): confirmed separate in code (mined_rules vs v101_region_source_pool_top5_shadow); flagged 30 mined_rules using prize_keys outside owner V105.29 prize-source lock (MB:13, MN:6, MT:11) → `PRIZE_SOURCE_VIOLATION_DETECTED`.
- `scheduler.py` refactor: module-level `_safe_stdio_ctx` context manager wrapping all no-token entry points (`_run_free_model_prediction`, `_run_smart_ensemble`, `_run_smart_ml_ensemble`, `_run_combo_no_token`, `_rerun_free_models_after_scrape`). Smoke 3/3 PASS. VPS deploy script `_v10529_DEPLOY_SAFE_STDIO_VPS.md` ready; owner OK pending.
- Official 4-table hash guard pre/post IDENTICAL (predictions=4791, final_bundles=219, lottery_results=14655, model_daily_eval=4655). No provider/manual AI call. MT_PROTECT_PRESERVED (D-2 leak MT/MB 7d = 0).
- Status PARTIAL — not PASS.

---

## V105.28 — TOTAL FORCE RUNTIME CONTRACT VERIFY (2026-05-11 23:38 VN)

- Latest public pointer advanced to `V105_28_RUNTIME_CONTRACT_VERIFY_20260511`.
- Verified owner runtime contract end-to-end: DD Trước/DD Sau routing, no-token retrain-before-rerun cascade, 90s soft / 300s hard timeout, official 15 / lane-test 20 gate, region-only freeze, manual provider block, MT protect, and OWNER_CONFIRMED_PAT_REVOKED.
- PASS gates: `DD_TRUOC_DD_SAU_MATCH`, `RETRAIN_BEFORE_RERUN_CONFIRMED`, `SOFT_90S_CONFIRMED`, `OFFICIAL_15_GATE_CONFIRMED`, `LANE_TEST_20_GATE_CONFIRMED`, `REGION_FREEZE_OK`, `TOKEN_GATE_CORRECT`, `MANUAL_PROVIDER_BLOCKED`, `MT_PROTECT_PRESERVED`, `OWNER_CONFIRMED_PAT_REVOKED`, `SECRET_SCAN_CLEAN` (public/docs).
- Open gaps: `CLOSED_FILE_DEPLOY_PENDING` (86 closed_file errors on 2026-05-11 + 25 on 2026-05-10 in MB no-token rerun — `_safe_stdio_ctx` wraps only AI token path; no-token path still raw print) and `AI_PRIORITY_ORDER_GAP` (scheduler iterates `AUTO_AI_MODELS` static; no region+weekday strongest-first reorder yet).
- Official 4-table hash guard unchanged: predictions=4791, final_bundles=219, lottery_results=14655, model_daily_eval=4655. No provider/manual AI call.
- 10 shadow audit tables `v10528_*` materialized; all `shadow_only=1`, `output_eligible=0`, `diagnostic_only=1`.
- Final acceptance: **PARTIAL** — not PASS.

---

## V105.27 — TOTAL FORCE SSOT + MN D-2 RANKED TOP5 SHADOW WIRE (2026-05-11 22:27 VN)

- Latest public pointer advanced to `V105_27_TOTAL_FORCE_CONTROL_20260511`.
- MN D-2 ranked top5 prompt visibility is closed in shadow only: `mn_d2_rows=137`, `mn_d2_prompt_seen_count=137`, `real_prompt_not_injected_count=0`, `mt_mb_d2_prompt_leak_count=0`, `v10527_prompt_flow_trace=450`.
- Top2/Bundler A/B and MB_D_v2 remain blocked from promotion. MB_D_v2 result: `would_save=115`, `would_break=171`, `break_ratio=0.3379`, `auto_disable=true`.
- Official hash guard unchanged for `predictions`, `final_bundles`, `lottery_results`, and `model_daily_eval`; no manual/provider AI call was issued.
- Notion bridge pages created/recorded for V105.25 and V105.26; V105.27 page ID retained in `LATEST_REPORT.json`.
- Final acceptance remains **PARTIAL**, not PASS, due promotion gates and owner security/deploy decisions.

---

## V105.25 — STATION ALIAS FIXUP + SOURCE-POOL REASON RANKING + V103 SUPPLY CLASS FIX (2026-05-11 15:30 VN)

- Published public V105.25 evidence folder: `V105_25_STATION_ALIAS_FIXUP_20260511`.
- LANE 1 STATION ALIAS FIXUP: code/runtime/prompt/UI labels canonicalized via `station_identity.py` SSOT. Audit `_v10524_station_code_audit.py` upgraded to v10525 with embedded-canonical detection + strict weekday-as-station rule + expanded forensic exception list. Post-audit `alias_unexpected_count = 0` and `weekday_as_station_unexpected_strict = 0`. Raw `lottery_results.station` NOT mutated.
- LANE 2 SOURCE-POOL REASON RANKING: `_v10525_source_pool_reason_ranking.py` aggregates `v10524_source_pool_gap_drilldown` by region × weekday × station × miss_reason × source_prize. Top REAL root cause across MN/MT/MB = `SOURCE_FORMULA_EXCLUSION` (MN 187, MT 405, MB 1021). `PROMPT_NOT_INJECTED=4349` is a measurement artifact pending V104 wiring.
- LANE 3 CANDIDATE FLOW FUNNEL: `_v10525_candidate_flow_funnel.py` computes conversions across source_pool → prompt → rank → top5 → top2 → bundled → ui. Biggest drop is `top5→top2` for MN/MB and `top2→bundled` for MT. First-miss stage by region matches the rank table.
- LANE 4 V103 SUPPLY CLASS FIX: `_v10525_v103_supply_class_backfill.py` propagates V102 recurrence (`v102_recurrence_score`, `v102_recurrence_class`, `v102_recommendation`, `v102_evidence_json`) into `v103_candidate_supply_shadow` where the join `(target_date, region, candidate_tail)` matches. `_v10524_v102_relaxed_selector_shadow.py` got an evidence_json-aware fallback so `non_gan_core_present` derives correctly when V103 row is absent — RELAXED_L2 activated 0 → 11 rows (RELAXED_L1 = 13). No V102 promotion to official.
- LANE 5 V102 RELAXED WATCH: `_v10525_v102_relaxed_watch.py` tracks 7d/14d observations + entered_top2 + would_save + would_break + net_save + save_ratio + break_ratio. Promotion gate hard-coded: window_days >= 14 + save_ratio >= 0.30 + break_ratio <= 0.10 + net_save > 0 + owner explicit OK.
- LANE 6 RUNTIME MANIFEST DAILY: `_v10525_runtime_manifest_daily.py` snapshots runtime manifest to `artifacts/runtime_manifest/<date>/manifest.json` and writes `drift_alert.json` when critical file hashes change without a corresponding `commit/ref` change. Scheduler wiring 00:05 VN is pending owner OK.
- End-to-end audit `artifacts/v10525/v10525_local_audit_latest.json` confirms `official_unchanged = true` for predictions / final_bundles / lottery_results / model_daily_eval (SHA256 pre = post). No manual/provider AI call was issued at any step.
- Updated `LATEST_REPORT.json`, `REPORT_INDEX.md`, `NEXT_ACTION.md`, `OPEN_ISSUES.md` to point to V105.25.

---

## V105.24 — SOURCE_POOL_GAP_DRILLDOWN + V102_RELAXED_SHADOW + TOKEN_LOCK + RUNTIME_MANIFEST (2026-05-11 13:50 VN)

- Published public V105.24 evidence folder: `V105_24_SOURCE_POOL_GAP_DRILLDOWN_20260511`.
- Persistent shadow drilldown surfaces created: `v10524_source_pool_gap_drilldown`, `v10524_candidate_flow_trace`, `v10524_v102_relaxed_selector_shadow`.
- Token-cost contract guard hardened: owner-lock flags, `_owner_ai_token_attempt_exists`, manual API endpoints + startup catch-up blocked, duplicate-save prevention.
- `DEPLOYED_RUNTIME_MANIFEST.json` (file hash + commit ref + DB hash) generated as forensic identity.
- Final acceptance **OFFICIAL LOCKED**: official tables unchanged; only shadow + admin-readout work. Outstanding from V105.24 audit: 62 alias residue (resolved in V105.25), `RELAXED_L2 = 0` (resolved in V105.25), V103 supply class NULL (mitigated in V105.25).

---

## V105.23 — TOTAL FORCE CODE-TRUTH AUDIT + PUBLIC NOTION EVIDENCE (2026-05-11 11:40 VN)

- Published public V105.23 evidence folder: `V105_23_TOTAL_FORCE_CODE_TRUTH_AUDIT_20260511`.
- Final acceptance is **PARTIAL**, not PASS: official locked and token guard verified, but SOURCE_POOL_MISS, V102 0-row strict shadow, MT/MB below-budget lane rows, and missing persistent V105.23 drilldown surfaces remain open.
- Added public machine-readable matrix: `V105_23_EVIDENCE_MATRIX.json` for Notion/control review.
- Updated `LATEST_REPORT.json`, `REPORT_INDEX.md`, `NEXT_ACTION.md`, and `OPEN_ISSUES.md` to point to V105.23.
- No official/runtime source changes; no manual/provider AI verification call.

---

## V105.22 — Total Force Live Prep (2026-05-11T08:59:39+07:00)

- Added region-independent lane profile and live-prep evidence package.
- Official hashes unchanged; V105.22 changes are lane-test/shadow/admin-readout only.
- Morning lane status is explicit: MN ready 20/20, MT/MB preview below budget.

---

## V105.20 — DUAL-LANE STABILIZATION + REAL TEST-LANE MEASUREMENT (2026-05-10 22:55 VN)

- Official `/du-doan` verified exact 15/15 with official hashes unchanged.
- Lane `/du-doan-test` verified exact 20/20 with `MAIN_TEST_EQUALS_OFFICIAL` marker and challenger preview.
- V102 STRONG/PROMPT_REVIEW_STRONG admitted to test-only adaptive selector under non-gan-core + >=2-layer gate.
- Public evidence folder: `V105_20_DUAL_LANE_STABILIZATION_20260510`.
- Notion page: `35c1d385-9bf8-81e7-b20a-df49057d3da4`.

---

## V105.19 — Hard Stabilization Night Pass (2026-05-10 22:15 VN)

- Public latest advanced to V105.19.
- Added wrapper report and evidence files for runtime control, lane-test contract, identity duplicate audit, and owner context.
- Official hashes unchanged; Notion pages created under canonical `Lottery_AI_Test`.

---

## V105.6 — SSOT CLEAN + LIVE CRON VERIFY + REGIONAL SOURCE-POOL DATA HEALTH (2026-05-10 12:40 VN)

- Fixed public SSOT drift wrapper: latest pointer now V105.6 with V105.5 evidence and conversation context.
- Added dedicated `/monitoring` source-pool data-health panel and admin API.
- Added `v101_region_source_pool_evidence_shadow` and `v105_no_token_independent_scoreboard`.
- Deployed source-gated V104 Phase B guard: if source-pool is incomplete, Phase B logs `PHASE_B_BLOCKED_BY_SOURCE` and does not force provider calls.
- Official hashes unchanged 4/4; no production mutation.

---

## V105.5 — REGIONAL SOURCE-POOL LANE TEST MEASUREMENT (2026-05-10 11:50 VN)

- Added owner-approved V101 regional source pools:
  - `MN_D = (MN+MT+MB) D-1 + (MN+MT+MB) D-2`
  - `MT_D = (MN+MT+MB) D-1 + MN D`
  - `MB_D = (MN+MT+MB) D-1 + MN D + MT D`
- Backfilled 113 days on VPS: regional source-pool 10170 rows, top5 1695 rows, flag violations 0.
- `/monitoring` V105 panel now shows V101 top5 + source completeness; pre-draw state honestly reports `SOURCE_PARTIAL`.
- Official hashes unchanged 4/4; no production mutation.

---

## V105.2 — MONITORING LEGACY CONTRAST + NOTION/PUBLIC SYNC (2026-05-10 01:45 VN)

- Hardened legacy `/monitoring` pastel inline cards after owner screenshots showed low-contrast text in older V95/V103/V104 panels.
- Deployed frontend-only contrast fix; `/monitoring` remains admin-locked (`401` unauth).
- Created 4 Notion V105 pages under canonical `Lottery_AI_Test`.
- Redacted secret scans found no full `ghp_`, `sk-`, or Google `AIza` token patterns in private/public report trees.

---

## V105.1 — TRUE LANE TEST INDEPENDENCE + PROVIDER ROUTING FIX (2026-05-10 01:30 VN)

- Fixed GPT lane-test routing: `gpt-5.5` uses OpenRouter key source; GPT 5 mini/GPT 5.4 remain OpenAI-platform routed.
- Added independent AI shadow, no-token shadow, and context completeness audit surfaces. All V105 outputs remain `shadow_only=1`, `diagnostic_only=1`, `output_eligible=0`, `owner_approved=0`.
- Added `/monitoring` V105 Lane Test Control with provider health, why-empty/data health, status badges, and 60s refresh.
- Added prediction-quality data-health metadata so `/app` can show source/date/row counts without mixing shadow and official metrics.
- Verified VPS real run for target_date `2026-05-09`: 9 provider calls, 93 AI rows, 7422 no-token rows, 7515 context rows. Official table hashes unchanged 4/4.

---

## V104.1 — PHASE B ACTIVATED + GITHUB PAT ROTATED (2026-05-10 00:15 VN)

- Owner directive (verbatim, condensed): "Cập nhật API Token Githup Mới đi em "ghp_N9GS***" anh đã gennere rồi đó. Anh muốn Lane Test chạy thực sự với các thay đổi. Mắc gì sau 7 ngày mới nâng cấp khi mọi bằng chứng đề cho thấy các điều chỉnh phù hợp khi verify 60 ngày rồi mà em."
- **GitHub PAT rotation**: VPS git remote `origin` URL on `vietnix:/root/Lottery_AI_Test` updated to new owner-generated PAT. Verified via `git ls-remote origin HEAD` returns `494071b3d6046ec1fb9bd0cb51656878ac909596` (V104 commit head, auth working). New token NEVER written to any tracked file in private/public repo. Local Windows uses Credential Manager (clean). FU-V99-GITHUB-TOKEN-LEAK status `OPEN` → `ROTATED`. Owner manual action remaining: revoke old `ghp_cvoSP***` explicitly on GitHub UI.
- **V104 Phase B activated**: NEW backend `web/backend/_v104_phase_b_runner.py` (~370 lines) với limited roster 3 models × 3 regions = 9 calls/day max + 3 buffer (`MAX_TOTAL_CALLS_PER_DAY=12`). Roster: Claude Opus 4 + GPT-5-pro + Gemini 2.5 Pro per MN/MT/MB. Cost guard: 90s timeout, 1500 output tokens, 20 candidates per prompt max. 3 thin provider wrappers (Anthropic / OpenAI gpt-5/o-series-aware / Gemini google-genai+legacy fallback).
- V104 review prompt embeds full region prompt family + forces strict JSON `{decisions[], shadow_bt, shadow_lo2, max_two_numbers=true, production_weight=false}`. Decisions written to `v104_shadow_prompt_model_decision` với `provider_called=1, output_eligible=0, diagnostic_only=1, shadow_only=1`.
- **Scheduler crons added** in `web/backend/scheduler.py`: 19:24 VN daily V104 materializer + 19:30 VN daily V104 Phase B runner (BEFORE production cron 19:35-19:55 VN). Both registered in journalctl.
- **First real Phase B fire 2026-05-10 00:08 VN target_date=2026-05-09**: 9 calls fired total, 5 succeeded (3 Anthropic Opus + 2 Gemini empty/parse_fail), 4 failed (3 OpenAI 401 + 1 Gemini 503). 45 decision rows stored in `v104_shadow_prompt_model_decision`. Elapsed 216.66s.
  - **MN**: Claude Opus ACCEPT 2 / HOLD 2 / REJECT 16, shadow_bt='05' shadow_lo2=['13']. MN 13 = ACCEPT HIGH ("V67+V70+V73+V101 convergence, test_bt×2, strong pattern match") ✅ catches exact owner-flagged case.
  - **MT**: Claude Opus PARSE_FAIL (max_tokens=1500 hit), GPT-5-pro 401, Gemini PARSE_FAIL.
  - **MB**: Claude Opus ACCEPT 2 / HOLD 2 / REJECT 14 shadow_bt='37' shadow_lo2=['02']. MB 64 = REJECT MEDIUM ("AI-herd + V67 but no cross-region, MB herd suspicious").
  - **MN 89**: not in candidate set for 2026-05-09 (was earlier-day candidate).
- **Hash guard 4 official tables SHA256 IDENTICAL pre vs post** (predictions=4625 / final_bundles=213 / lottery_results=14642 / model_daily_eval=4493). ZERO production mutation. ✅
- **NEW FUs**: `FU-V104-1-OPENAI-KEY-INVALID` P0 (owner regen at platform.openai.com), `FU-V104-1-GEMINI-EMPTY-RESPONSE` P1 (SDK fallback), `FU-V104-1-MT-CLAUDE-TRUNCATED` P1 (bump max_tokens), `FU-V104-PHASE-B-7D-ADJUSTMENT` P2 (review 2026-05-17 19:30 VN).
- AUTOMATION_STATE seq 53 → 54 với phase_b_first_fire + hash_guard + github_pat_rotation arrays.
- NO production prompt change, NO selector touch, NO `/du-doan` mutation.

---

## V104 — SHADOW PROMPT INJECTION PER REGION (Phase A) (2026-05-09 23:55 VN)

- Owner directive (verbatim, condensed): "[V104 TOTAL FORCE] Mục tiêu chính là triển khai V104 shadow-only để candidate từ V103 thật sự đi vào prompt AI shadow theo từng miền MN/MT/MB, để model phải accept/reject với lý do rõ ràng."
- NEW backend `web/backend/_v104_shadow_prompt_injection.py` (~660 lines).
- 2 NEW shadow tables: `v104_shadow_prompt_candidate_injection` (1823 rows 30d backfill 2026-04-10 → 2026-05-10, 81 rows for 2026-05-09 — MN OPTIONAL=39 / MT OPTIONAL=24 / MB OPTIONAL=18, REQUIRED=0 honest) + `v104_shadow_prompt_model_decision` (0 rows Phase A; columns ready for Phase B ACCEPT/REJECT/HOLD per model).
- NEW admin route `/api/admin/v104-shadow-prompt-injection` (401 admin-locked).
- NEW UI section `sectionV104ShadowPromptInjection` registered in `loadAllSections()` AND `setInterval(60000)` of `web/frontend/monitoring.html` — 4 sub-panels (owner intent, per-region summary, strict vs diagnostic warning, per-region candidate tables), NO promote/rollback/trigger button.
- NEW 3 region prompts (independent): `web/backend/prompts/shadow/MN/MT/MB_AI_REGION_SPECIALIST_PROMPT_SHADOW_V104.md`. MN: MN_D = (MN+MT+MB) D-1+D-2 pool + gan 15d/7d. MT: anti-import + consensus-first + no-break guard. MB: cold-aware + gan 30d/15d + cross-region downstream priority.
- Gating logic: REQUIRED_IN_PROMPT = V103=REQUIRED OR (V103=REVIEW + recurrence STRONG/MEDIUM + lift_pp ≥ 5 + non-gan core + ≥2 layers). Gan alone NEVER promotes (anti-noise rule `ANTI_NOISE_GAN_ONLY`).
- 13/61/64/89 case audit: all 4 surface as OPTIONAL_REVIEW today (V103 gate=REVIEW, non_gan_core=true, V102 recurrence_class=None today → upgrade rule honestly miss).
- Notion MCP §52F: 2 V104 sub-pages auto-created on canonical `Lottery_AI_Test`: (1) `🧪 V104 — Shadow Prompt Injection per Region (Phase A, 2026-05-09)` id `35b1d385-9bf8-81bb-b5a8-ecffb0c817e6`, (2) `📝 V104 — Owner Conversation Context (Phiên 2026-05-09 22:00 → 23:50 VN)` id `35b1d385-9bf8-8150-88cf-e36abe524520`.
- VPS deploy: scp 6 files + restart lottery + 30d backfill on VPS = same 1823 rows. Endpoints: health=200, v104=401 admin-locked, v103=401, monitoring=401, du-doan=200.
- Hash guard 4 official tables IDENTICAL pre vs post: predictions=4625, final_bundles=213, lottery_results=14642, model_daily_eval=4493 — VPS post-hash matches local pre-hash exactly. ZERO official mutation.
- Phase B (provider pilot) = OWNER_GATE_REQUIRED (FU-V104-PHASE-B-PROVIDER-PILOT). Drive ingest LISTED PARTIAL (FU-V104-DRIVE-INGEST-PARTIAL).
- AUTOMATION_STATE seq 52 → 53 with `notion_pages[]` array + hash_guard array.
- NO runtime production change, NO official table touch, NO production prompt change.

---

## V103.2 — NOTION MCP AUTO-SYNC + §52F NOTION AUTOMATION HARDLOCK (2026-05-09 22:55 VN)

- Owner directive (verbatim): "tại sao không cập nhật Notion MCP được em? em tiến hành 1 cách tự động đi chứ, lớn quá thì chia nhỏ từng trang ra chứ em. Tổng hợp các yêu cầu mà anh anh trao đổi trong trò chuyện này đẩy lên github Pulic luôn nha em."
- Discovered `user-notion` MCP server in workspace (`mcps/user-notion/tools/`). Previous default to `FU-170 OWNER_LOCK` without first attempting MCP = `§52F_VIOLATION_NOTION_NOT_ATTEMPTED` (and `§52_OWNER_REREMINDER` because owner had flagged this ≥2 sessions).
- Authenticated as bot `Antigravity` workspace `TanPhat ERP`. Located canonical page `Lottery_AI_Test` (id `067b40e9-0096-47e7-952c-504503559a29`). Created 2 sub-pages:
  - `V103.1 — Cross-Region & D-1 Recurrence Tracker UI + §52 Hardlock` (id `35b1d385-9bf8-8156-94fc-d86cfa331153`, 45 blocks).
  - `Phiên 2026-05-09 — Tổng hợp yêu cầu owner + V99.1 → V103.1` (id `35b1d385-9bf8-8140-b9fc-d0583c5e02ff`, 38 blocks; verbatim owner messages 09:05 → 22:42 VN).
- NEW public file `evidence/CONVERSATION_CONTEXT_V99_1_TO_V103_2_20260509.md` — verbatim conversation context for the same content as Notion (so public GitHub holds the authoritative ngữ cảnh).
- NEW governance section `§52F NOTION MCP AUTOMATION OBLIGATION` (10 hard rules) in `.Antigravityrules.md` + mirrored `§9D-1` in `.AGENT.md` + Notion MCP Automation Rule section in `.cursorrules`. Mandates: discover MCP tools first, attempt MCP calls, only escalate to FU-170 with concrete error.
- FU-170 status flipped from `OWNER_LOCK` to `RESOLVED`. New FU `FU-V103-2-NOTION-MCP-AUTOSYNC` opened (`DEPLOYED_PENDING_LIVE_VERIFY`).
- AUTOMATION_STATE seq 51 → 52 with `notion_pages[]` array (page IDs + URLs) so future agents verify continuity without re-searching.
- NO runtime change, NO official table touch, NO production prompt change.

---

## V103.1 — CROSS-REGION & D-1 RECURRENCE TRACKER UI + §52 MEASUREMENT-UI-DEPLOY-SYNC HARDLOCK (2026-05-09 22:35 VN)

- Owner re-emphasized (2nd time): "lose hôm nay xổ ngày mai" + "lose miền trước xổ miền sau" must have measurement table AND visual UI at `https://xs.io.vn/monitoring`; codify rule into `.Antigravityrules.md` / `.AGENT.md` / `.cursorrules`.
- NEW `web/backend/_v103_cross_region_tracker.py` (290 lines) — admin-only aggregator combining V101 + V102 + V103 + V94 leakage shadow tables.
- NEW admin route `/api/admin/v103-cross-region-tracker` (401 unauth, 200 admin, no-store cache).
- NEW UI panel `sectionV103CrossRegionTracker` in `monitoring.html` with 4 panels:
  - P1 V101 MN D-1/D-2 cross-region top 15 today.
  - P2 V102 60d/90d recurrence stats with `eligible_for_shadow_boost` flag + STRONG/MEDIUM today.
  - P3 V103 prompt gate REQUIRED/REVIEW/BLOCKED counts + top + supply layer heatmap.
  - P4 V94 cross-region leakage continuous monitor.
- UI panel registered in `loadAllSections()` AND `setInterval(60s)` — auto-refresh, admin-locked, no promote/rollback button.
- NEW governance section `§52 MEASUREMENT-UI-DEPLOY-SYNC HARDLOCK` in `.Antigravityrules.md`: 13-deliverable contract + self-check matrix + violation taxonomy (`§52_VIOLATION_UI_MISSING`, `§52_VIOLATION_DOC_MISSING`, `§52D_DRIFT_VIOLATION`, `§52B_VIOLATION_REFRESH_MISSING`, `§52_OWNER_REREMINDER`).
- Mirrored §52 contract in `.AGENT.md §9D` + `.cursorrules`.
- VPS deploy + restart + smoke OK (`/api/health=200`, admin endpoint `=401`).
- Hash 4 official tables IDENTICAL pre/post.
- Notion sync payload: `evidence/NOTION_SYNC_PAYLOAD_V103_1.md`.
- FU-V103-1-MONITORING-UI = DEPLOYED_PENDING_LIVE_VERIFY (pass condition: 2026-05-10 19:00 VN cycle populate panels).
- Shadow only, output_eligible=0, diagnostic_only=1, owner_approved=0. Official UNCHANGED.

---

## V103 — CANDIDATE SUPPLY AUDIT + TIGHTENED PROMPT GATE (2026-05-09 21:55 VN)

- New shadow tables: `v103_candidate_supply_shadow` (8743 rows 30d) + `v103_prompt_candidate_gate_shadow` (8743 rows 30d).
- Supply audit tracks 11 source layers per candidate tail: AI / no-token / official / test / V67 / V70 / V73 / V101 / V102 / gan / rule.
- Prompt gate tightened: `REQUIRED` needs recurrence STRONG + ≥1 non-gan core layer + ≥2 total source layers. Gan support is secondary only — never alone promotes to REQUIRED.
- Smoke 2026-05-10 pre-cycle: REQUIRED=0, REVIEW=49, BLOCKED=251 (expected — D+1 core sources not yet run).
- Private commit `2dac1ea` + governance sweep `582edab`.
- V104 prompt injection = OWNER_LOCK pending (proposed [A]: shadow inject REQUIRED/REVIEW with accept/reject capture per region).
- Shadow only, output_eligible=0, diagnostic_only=1, owner_approved=0. Official UNCHANGED.

## V102 — D-1 LOST SIGNAL RECURRENCE TRACKER (2026-05-09 21:10 VN)

- New shadow tables: `v102_recurrence_stats_shadow` + `v102_candidate_recurrence_context_shadow`.
- Quantifies 4 recurrence patterns over 60d/90d:
  1. Same-region D-1 lost → D hit (e.g. MN yesterday losing prediction reappearing today).
  2. Cross-region same-day (MT D → MB D, MN D → MT D, etc.).
  3. Cross-region next-day (MN D-1 → MT D, MT D-1 → MB D).
  4. Combined STRONG/MEDIUM/WEAK class per candidate.
- Sources tracked: official, test_lane, V67/V70/V73 traces, V101 candidates, individual AI models.
- `recurrence_class`: STRONG → recommended for `PROMPT_REVIEW_STRONG`; MEDIUM → review only; WEAK/BLOCKED → not surfaced.
- Private commit `7dc3536`.
- Shadow only, no production runtime change.

## V101 — MN CROSS-REGION D-1/D-2 RULE + REGION-SPECIFIC V2 PROMPTS (2026-05-09 20:35 VN)

- New shadow tables: `v101_mn_cross_region_rule_shadow` (ranked MN candidates from previous-day MT/MB tails) + `v101_region_prompt_context_shadow` (per-region addendum text + context JSON).
- Three new region-specific shadow prompts (V2):
  - `MN_AI_REGION_SPECIALIST_PROMPT_SHADOW_V2.md`: V101 cross-region context + V100 gan + V99 evaluator semantic guards.
  - `MT_AI_REGION_SPECIALIST_PROMPT_SHADOW_V2.md`: consensus-first + gan diagnostic + semantic guards.
  - `MB_AI_REGION_SPECIALIST_PROMPT_SHADOW_V2.md`: MB gan thresholds + cold flag doctrine + semantic guards.
- New admin API: `/api/admin/v101-shadow-pilot` (admin-locked readout).
- 14d backfill done locally + VPS.
- Per-region independent — owner can tune one region without affecting others.
- Private commit `522969c`. Shadow only, NOT injected into production prompt SP-4.1 yet.

## V100 — `du-doan-test` UI FIX + GAN CALCULATOR FOUNDATION (2026-05-09 16:30 VN)

- `/du-doan-test` UI: default tab MN (was MB), mobile responsive @media 480/768, two new panels (Lịch sử dự đoán + Bảng chỉ số kỹ thuật).
- Two new admin APIs: `/api/admin/test-lane-history`, `/api/admin/test-lane-metrics`.
- New shadow table: `gan_signal_shadow_v100` (252K rows 30d) computing `gan_normal` (any prize) + `gan_special` (ĐB/G8) per region/station/tail.
- Owner-specified thresholds: MB normal=30 special=15; MN+MT normal=15 special=7.
- Private commit `5624570`.
- Shadow only, no production runtime change.

## V99.2 — TOTAL FORCE SECURITY + BT DOCTRINE LOCK + SCOREBOARD (2026-05-09 13:15 VN)

- Security scan PARTIAL: 0 PAT in working tree, .env protected by .gitignore, AI provider keys env-only. Owner must revoke `ghp_cvoSP***` PAT (FU-V99-GITHUB-TOKEN-LEAK P0).
- BT doctrine LOCKED: `STRICT_DAC_BIET` = production KPI (UNCHANGED). `TAIL_ANY_PRIZE_DIAGNOSTIC` = shadow signal only. FU-V99-BT-SCORING-DEBATE → DEFAULT KEEP STRICT (revisit 2026-06-08 30d gate).
- V99 evaluator sanity PASS: 10 tests OK, 747 rows shadow integrity 100%, STRICT_ZERO_VALIDATED 14d (Wilson 95% upper 0.7%).
- 14d/30d scoreboard: OFFICIAL strict 0% (n=42), TEST_LANE strict 0% (n=371). Lenient: OFFICIAL 38.1%, TEST_LANE 35.3%. NO method qualifies for production promotion.
- Bundle replay 10 hypotheses preliminary, ALL defer FU-173 14d gate.
- Private commit `d134838`, public `b0a4e7a`.

## V99.1 — TRUTH VERIFY + V99 EXACT EVALUATOR + 3 P0 FINDINGS (2026-05-09 11:35 VN)

- V99 exact station-aware evaluator built (`v99_exact_evaluator_results` shadow table). Supports `BT_STRICT_DAC_BIET` (production) and `TAIL_ANY_PRIZE_DIAGNOSTIC` (shadow).
- V98.1 metadata cleanup in `LATEST_REPORT.json`.
- 3 P0 findings:
  - **MB 2026-05-08 "56" report conflict** = EVALUATOR_SEMANTIC_DIFFERENCE (V93 multi-prize lenient vs production strict-ĐB; both correct under their semantic).
  - **GitHub PAT leak** in VPS git remote URL + private commit `fb2ae98` history (REDACTED in working tree, owner must revoke).
  - **VPS git drift expected** — VPS at `ceb36c2` V17.19.4 2026-04-19; all V77→V103 work via scp deploy mode.
- FU-171 false_negative resolved (CRLF/LF only, not content drift).
- Private commit `bfea15d` (token-redacted), public `74cab5b`.

## V98 — ABSOLUTE RUNTIME ↔ PUBLIC ↔ NOTION SSOT + MONITORING COMMAND CENTER (2026-05-09 00:50 VN)

- Public root pointer V92 → V98. README no longer claims V74 latest.
- V93-V97 batch (private commit `1cd2833`, 28 files +4759 -39) documented in V98 wrapper.
- /monitoring V98 Command Center 10 panels admin-locked auto-refresh 60s deployed:
  1. SSOT Status (public/private/runtime/Notion mismatch class)
  2. Runtime Parity (md5 + endpoint status)
  3. Natural-Fire Cron Tracker (11 crons row count)
  4. Accuracy Root Cause (10 items severity + FU)
  5. Owner Gate Queue (12 items)
  6. Prompt/Context Completeness (SP-4.1 + 21 fields)
  7. Bundle Conversion (V94.1 + V93 MN save 5d)
  8. Cross-Region Leakage (6 pairs × 3 windows)
  9. Data Freshness 30d (provisional vs clean)
  10. Public/Notion Sync Checklist
- 7 new FU items (FU-169 RESOLVED, FU-170-175 owner-gated, FU-176 RESOLVED).
- Hash guard 4 official tables IDENTICAL across V92.1 → V98 (predictions=4542, final_bundles=210, lottery_results=14634, model_daily_eval=4493).
- Notion `Lottery_AI_Test` sync UNVERIFIED (no MCP in Cursor scope) — FU-170 owner-locked.
- V97 SP-4.1 prompt fix (max 2 numbers) is verified live (predictions 30d 0/2102 rows ≥3).
- Cron natural-fire status PARTIAL (V66.1+V67 OK; V70/V73/V76/C16 0 rows post-restart) — FU-172 escalated.
- 4 file local↔VPS md5 drift documented (FU-171, runtime OK).
- NO official scoring/selector/prompt production change beyond V97 SP-4.1.

## V92 — ABSOLUTE SSOT RECONCILIATION (2026-05-08 01:30 VN)

- Public root pointer fixed to V92.
- V90 and V91 claims verified.
- V92 one-source truth wrapper published.
- No runtime change, no DB write, official unchanged.

## V91 — Total Reconciliation + Stale-FU Closure + Actionable Evidence Pass (2026-05-08 01:15 VN)

- NEWER_THAN_V89_FOUND verified: latest = V90.
- 74 stale FU re-audited: 54 SUPERSEDED + 13 RESOLVED + 7 NEEDS_RUNTIME (67/74 = 90% docs-only).
- 11 evidence matrices generated for Notion AI lookup (FU reconciliation, actionable evidence, method accuracy, region strategy, prompt status, routes audit, decision calendar hardened, per-decision tracking, stale-FU auto-update spec, 29 tabs audit, V91_ONE_SOURCE_INDEX).
- Decision calendar hardened with pass/fail/owner_action/auto_report.
- NO VPS deploy. NO UI change. NO DB write.
- 4 official tables hash byte-identical.

## V90 — Final cleanup (2026-05-08 01:05 VN)

- 5 final tabs in /monitoring (29 tabs total): 🐍 Backend Modules (293) / 📜 Scripts (19) / 🛠️ Web Helpers (42) / 🗺️ Active Roadmaps (2) / ⚖️ Cursor Rules (3).
- Schema v89_master_board_v3 → v90_master_board_v4 (36 keys).
- Total V85+V86+V87+V88+V89+V90 = ~1378 items reconciled.
- ĐẾN ĐÂY THẬT SỰ HẾT — không còn category nào sót.
- 4 official tables hash byte-identical.

## V89 — 5-extension pack (2026-05-08 00:55 VN)

- 6 new tabs in /monitoring (24 tabs total): Migrations / Live Cron (realtime next_run) / FU Audit (72/152 stale flagged) / Phase Findings (116 first paragraph) / Decision Log (22 DEC) / Governance Ledger (96 entries).
- Schema v88_master_board_v2 → v89_master_board_v3 (31 keys).
- monitoring.html 201KB → 209KB.
- ~1019 items reconciled across V85+V86+V87+V88+V89.
- 4 official tables hash byte-identical.

## V88 — TOTAL_ENCYCLOPEDIA + 6 new tabs in /monitoring (2026-05-08 00:40 VN)

- 6 new tabs: ⚙️ Settings (252) / 📜 Automation History (28) / 📋 FU History (151) / 🗓️ Phase Checkpoints (116) / 💾 VPS Backups (31) / 📓 Notion Docs (15).
- /monitoring now has **18 tabs** total.
- TOTAL_ENCYCLOPEDIA.md (36 KB) single searchable file.
- Backend extended `_v87_master_board.py` with 6 new READ-ONLY blocks.
- Schema bump `v87_master_board_v1 → v88_master_board_v2` (25 keys).
- monitoring.html 196KB → 201KB.
- ~991 items reconciled across V85+V86+V87+V88.
- 4 official tables hash byte-identical.

## V87 — Master Index 12 tabs in /monitoring (2026-05-08 00:25 VN)

- New backend module `_v87_master_board.py` READ-ONLY 370 lines.
- New admin endpoint `/api/admin/master-board` for Agent IDE single-call lookup.
- New `sectionV87MasterIndex` in /monitoring with 12 tabs: Models / Prompts / Rules / Mechanisms / Metrics / Shadow Methods / DB Tables / Cron / Frontend / API / Decision Calendar / Owner Gate.
- Cached payload, switch tab no re-fetch. Auto-refresh 60s.
- monitoring.html 162KB → 196KB (+34KB).
- 4 official tables hash UNCHANGED.

## V86 — TOTAL FORENSIC REGISTRY + V82 merged into /monitoring (2026-05-08 00:10 VN)

- TOTAL_PUBLIC_REGISTRY.md (26 KB) for Notion AI single-table lookup.
- V82 Master Control Board merged into /monitoring as sectionV82MasterControl.
- /v82-monitor standalone kept.
- 132 API endpoints + 12 frontend pages + 142 FU + 224 CHANGELOG + 116 phase_checkpoints.
- monitoring.html 142KB → 162KB (+20KB).
- 4 official tables hash UNCHANGED.

## V85 — DEEP MASTER CONTROL (2026-05-07 23:55 VN)

- 8 super-family full inventory: 41 AI models + 129 DB tables + 26 cron jobs + 8 prompts + 5 PFG cohorts + 3 V81 pilot models + 27 metrics + 59 shadow methods.
- ~298 distinct items reconciled.
- 4 official tables hash UNCHANGED.

## V84 — MASTER CONTROL BOARD (2026-05-07 23:30 VN)

- 24-row master control board covering ALL families V63 → V83.
- 18-method P0 portfolio maturity matrix: 14 READY_TO_EVALUATE, 4 WAIT 5 days (until 2026-05-12).
- 14d region split: 2 POTENTIAL_LIFT (strongest_to_final_preservation, counterfactual_decision_audit), 3 DESTRUCTIVE_BIAS.
- 60d evidence availability map per family.
- Decision calendar 11 specific VN dates 2026-05-08 → 2026-07-06.
- Owner-gate queue 9 items with trigger dates.
- D-1/D-2 subsumed; D-7 ambiguous resolved as 7d gate concept.
- UI master board spec proposed (owner OK pending).
- 4 official tables hash UNCHANGED.

## V83 — V82 MONITOR UI PANEL (admin-only, read-only) (2026-05-07 23:20 VN)

- New backend module `web/backend/_v82_monitor.py` (read-only payload, 18 keys).
- 2 new admin-required routes: `GET /v82-monitor` (HTML) + `GET /api/admin/v82-monitor` (JSON).
- New frontend `web/frontend/v82-monitor.html` — 7-section dashboard, auto-refresh 5min.
- Hard contract honored: NO promote/rollback/edit/trigger button, NO DB write, NO scoring/selector change.
- Pre/post hashes 4 official tables UNCHANGED.

## V82 — 60D EVIDENCE CONTROL PASS (2026-05-07 23:05 VN)

- 307 audit cells (method × region × window {60, 30, 14, 7, 4}).
- 60D real evidence: OFFICIAL/AI_HERD/NO_TOKEN_HERD + 6 V52.5 methods.
- MN: 2 promotion candidates clean lift — SPECIALIST_ROSTER +6.7pp (save=4 break=0); AI_CHAIN_PRESERVATION +7.5pp (save=5 break=1).
- MT: consensus-first doctrine confirmed (AI_HERD -6.7pp with 12 breaks).
- MB: cold confirmed; all methods within ±5pp.
- V67/V70/V73/V79 max 4-15d; V81 2d → RETRO_LIMITED, no promotion.
- NO_TOKEN vs AI: region-specific (MN +3.4pp, MT +8.3pp, MB -3.3pp); no global floor change.
- Hash guard: 4 official tables UNCHANGED.

## V81 — PROVIDER SHADOW PILOT (owner-approved) (2026-05-07 22:18 VN)

- 3 models × 3 regions × 2 days = 18 provider calls. 18/18 parse_status=OK. 0 contract violations.
- Each model: hits=3/6, would_save=1, would_break=0 (n=6).
- MN 2026-05-07: all 3 models converge on V67/V73 tail 95 vs OFFICIAL 94 (would_save).
- MT: stable consensus. MB: honest LOW conf + herd warnings.
- New cron 19:14 VN. Cron now 6 jobs daily.
- Hard contract: shadow_only=1, output_eligible=0, output_impact='false'. Official tables UNCHANGED.

## V80 — ABSOLUTE CLOSURE PASS (2026-05-07 21:55 VN)

- Notion MCP doctrine pages reconciled with code (7 key pages patched).
- New shadow tables: rule_phase_synthesis_shadow / no_token_rule_aware_pack_shadow / mb_regime_shift_shadow / mn_ai_herd_vs_v67_save_daily.
- New cron 19:12 VN. Official tables UNCHANGED.

## V79 — AI↔NO_TOKEN CROSS-VERIFICATION + CLUSTER-WEIGHTED CONSENSUS (2026-05-07 19:08 VN)

- Cluster-weighted consensus shadow + AI/NO_TOKEN cross-verification.
- Region policies: MN V67/V73 boost, MB cold treatment, MT consensus-first.
- New cron 19:08 VN. Official tables UNCHANGED.

## V78 — AI PROMPT/CONTEXT FORENSIC + REGION-SPECIALIST SHADOW PROMPTS (2026-05-07 19:10 VN)

- Region-specialist shadow prompts MN/MT/MB authored and audited (no provider call yet at V78).
- Scheduler tzinfo bug fixed (V77 selector chain).
- New cron 19:10 VN. Official tables UNCHANGED.

# CHANGELOG_PUBLIC

## V80
- Notion/code/runtime sync closure.
- Shadow completion surfaces.
- Official unchanged.

## V79
- AI↔NO_TOKEN cross verification.
