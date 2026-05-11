# V105.29 — TOTAL FORCE NO-MISS CONTROL + LOSE-CARRYOVER SIGNAL LAYER + RUNTIME STABILITY (2026-05-12, 00:55 VN)

> Báo cáo Owner. Tiếng Việt. Stability-first. Evidence-first. Không gọi provider. Không động official. MT_PROTECT_MODE tuyệt đối. Công thức MN/MT/MB lock. Rule105 ≠ V101 source-pool top5.

## 1. EXECUTIVE SUMMARY

V105.29 verdict cuối: **`PARTIAL_NOT_PASS` + `SHADOW_ONLY` cho V105.29 layer + `DO_NOT_PROMOTE` cho Top2/Bundler/MB_D_v2/V102/Lose-Carryover.**

Phân loại gọn:
- ✅ V105.29 Lose-Carryover Signal Layer: SHADOW_ONLY, materialize OK, backtest DECISIVE → `DO_NOT_PROMOTE` (break_ratio 93-99% ở 6 signal paths).
- ✅ V105.29 Rule105 vs V101 separation audit: SHADOW_ONLY, materialize OK, phát hiện `PRIZE_SOURCE_VIOLATION_DETECTED` (30 rules trong mined_rules dùng prize_keys ngoài owner-lock).
- ✅ `_safe_stdio_ctx` wide patch: code đã LOCAL, smoke 3/3 PASS, deploy VPS pending owner OK (script `_v10529_DEPLOY_SAFE_STDIO_VPS.md` sẵn sàng).
- ✅ Official 4 bảng: pre/post sha256 IDENTICAL.
- ✅ MT_PROTECT_PRESERVED: D-2 leak MT/MB 7d = 0.
- ❌ Public GitHub raw still V105.27; local mirror đã V105.28 (chưa push) + V105.29 folder vừa stage local.
- ❌ SSH deploy key chưa migrate (origin còn HTTPS) — sau khi PAT revoke push sẽ fail.

## 2. NGUỒN ĐÃ ĐỌC (READ MATRIX)

Tóm tắt — đầy đủ trong `v10529_master_audit.json`:

| Nhóm | Path / Source | Trạng thái |
|---|---|---|
| Governance | `.Antigravityrules.md`, `.AGENT.md`, `.cursorrules`, `CHANGELOG.md`, `docs/CURRENT_TRUTH_SSOT.md`, `docs/FOLLOW_UP_TRACKER.md`, `docs/AUTOMATION_STATE.json`, `docs/AUTOMATION_HISTORY.jsonl` | READ |
| Active roadmaps | `docs/ACTIVE_ROADMAP_LAG1_ADAPTIVE_EXPLOIT.md`, `docs/ACTIVE_ROADMAP_CROSS_REGION_LEAKAGE.md` | READ |
| Public mirror local | `E:/Lottery_AI_Notion_Reports/LATEST_REPORT.json` (V105.28 local), `REPORT_INDEX.md`, `OPEN_ISSUES.md`, `NEXT_ACTION.md`, `CHANGELOG_PUBLIC.md` | READ |
| Public mirror remote raw | `raw.githubusercontent.com/.../LATEST_REPORT.json` = **V105.27** | READ (PUBLIC_RAW_STALE) |
| Notion pages | V105.25 / V105.26 / V105.27 / V105.28 đã có (4 page IDs ghi trong LATEST_REPORT.json) | RECORDED |
| Code | scheduler.py, main.py, database.py, model_registry.py, gpt_analyzer.py, station_identity.py, scraper.py, ml_predict.py, meta_predict.py, rule_engine.py, _v101_shadow_pilot.py, _v10522_live_prep.py, _v10527_ranked_prompt_wire_shadow.py, _v10528_runtime_contract_materializer.py, _materialize_du_doan_test_model_budget.py, _materialize_adaptive_exploit_v1.py, weekly_rule_miner.py, _seed_rules.py | READ |
| Frontend | app.js, index.html, monitoring.html, du-doan-test.html, pnl-tracker.html, settings.js | READ (lane mapping) |
| Artifacts | artifacts/v10523_*, v10524/*, v10525/*, v10526/*, v10527/*, v10528/* | READ |
| Live sync | `artifacts/live_sync/20260512_003215/manifest.json` | READ |
| Past transcript | `artifacts/cursor_no_token_model_verification_and.md` (thread ac1b4495) | READ |

## 3. SSOT DRIVE / GITHUB / NOTION VERDICT

| Source | Latest version | Evidence | Status |
|---|---|---|---|
| GitHub Public raw `LATEST_REPORT.json` | **V105.27** (commit `e4b8711`) | WebFetch 2026-05-12 00:32 VN | `PUBLIC_RAW_STALE_AT_V105_27` |
| Local public mirror `E:/Lottery_AI_Notion_Reports` | **V105.28** ghi sẵn (dirty, chưa commit/push) | git status: 21 file modified | `LOCAL_AHEAD_REMOTE` |
| Local public mirror V105.29 folder | Vừa stage (6 file evidence + report) | này | Ready to commit (chờ owner OK) |
| Notion MCP | V105.25/26/27/28 đã có (4 pages) | `LATEST_REPORT.json:notion_pages` | OK — V105.29 sẽ tạo sau khi report final |
| Drive folder 1/2 | Em không có Drive API tool | — | Owner tự upload sau khi GitHub push |
| Runtime VPS | sha256 = `7000bdc7…e4d39c51`, predictions=4791, final_bundles=219, lottery_results=14655, model_daily_eval=4655 | `artifacts/live_sync/20260512_003215/manifest.json` | `RUNTIME_AHEAD` |
| Repo private `Lottery_AI_Test` | master `e626ba74…` + 811 dirty (audit churn) | git probe | OK |

Verdict: `SSOT_PARTIAL` + `PUBLIC_RAW_STALE_AT_V105_27` + `LOCAL_AHEAD_REMOTE` + `NOTION_RECHECK_REQUIRED_FOR_V105_29`.

## 4. P0 STABILITY VERDICT — `_safe_stdio_ctx`

| Item | Status |
|---|---|
| Local code: `_SafeNullWriter`, `_ensure_safe_stdio`, `_safe_stdio_ctx` module-level | ✅ DONE (V105.29 refactor) |
| Wrap `_run_free_model_prediction` | ✅ DONE (inner exposed) |
| Wrap `_run_smart_ensemble` | ✅ DONE |
| Wrap `_run_smart_ml_ensemble` | ✅ DONE |
| Wrap `_run_combo_no_token` | ✅ DONE |
| Wrap `_rerun_free_models_after_scrape` | ✅ DONE (defense-in-depth) |
| `_start_timed_model_call` reuse module-level ctx | ✅ DONE (refactor) |
| `python -m py_compile` local | ✅ PASS |
| Smoke `_v10529_safe_stdio_smoke.py` | ✅ 3/3 PASS (case_A absorbed, case_B re-raised, case_C wrapped) |
| VPS deploy | ❌ `OWNER_GATE_PENDING` — script `_v10529_DEPLOY_SAFE_STDIO_VPS.md` sẵn sàng |

Verdict: `CLOSED_FILE_FIXED_LOCAL_ONLY` + `OWNER_GATE_PENDING (P0)`.

Live evidence: 111 closed_file errors trong 14d gần nhất, đa số tại MB rerun_post_mn 2026-05-11 (86) + MT rerun ngày 2026-05-10 (25). Sau deploy: kỳ vọng count plateau, MN cascade trả `7/7+7/7 success`.

## 5. DD TRƯỚC / DD SAU VERDICT

Đã verify đầy đủ trong V105.27/V105.28 và re-verify trong V105.29 master audit:

- MN no-token 04:00 → **DD Sau** ✅
- MN AI 04:15 → **DD Sau** ✅
- MN sau verify → freeze MN only, không rerun MN ✅
- MT no-token 04:00 → **DD Trước** ✅
- MT sau MN verify → `rerun_post_mn` → DD Sau (cuốn chiếu) ✅
- MT AI sau MN verify → `ai_chain` → DD Sau ✅
- MB no-token 04:00 → **DD Trước** ✅
- MB sau MN verify → `rerun_post_mn` intermediate diagnostic ✅
- MB sau MT verify → `rerun_post_mt` → DD Sau ✅
- MB AI sau MN+MT verify → `ai_chain` → DD Sau ✅
- MB sau MB verify → close day, không downstream ✅

Verdict: `DD_TRUOC_DD_SAU_MATCH`.

## 6. NO-TOKEN RETRAIN CASCADE VERDICT

`_run_auto_update(region)` flow xác nhận:
1. Scrape `lottery_results`.
2. `verify_prediction` → predictions.status WIN/LOSE/PARTIAL.
3. `verify_final_bundle` → final_bundles.verified_at.
4. `_materialize_closeout_measurements` → 9 shadow surfaces.
5. `update_daily_stat(<region>_verified=1)`.
6. `_rerun_free_models_after_scrape(trigger_region)` — refresh `fresh_cross_tails` từ `lottery_results` cùng ngày → re-predict no-token cho miền hạ lưu.
7. `_run_ai_predict_job(next_region, run_source='ai_chain')`.

Weekly full ML retrain CN 02:00 (LSTM + Meta). Per-verify path refresh feature state + cross-tail + model_daily_eval + training_history.

Verdict: `RETRAIN_BEFORE_RERUN_CONFIRMED` + `FEATURE_REFRESH_CONFIRMED` + `FULL_RETRAIN_WEEKLY_ONLY_OK`.

## 7. TOKEN / MANUAL GUARD VERDICT

- `OWNER_MANUAL_PROVIDER_CALLS_ENABLED=False` (default block).
- `OWNER_STARTUP_SHADOW_CATCHUP_PROVIDER_ENABLED=False`.
- `OWNER_AI_TOKEN_ONCE_DAILY_ONLY=True` (enforce).
- `AI_MODEL_SOFT_CONTINUE_SEC=90`, `AI_MODEL_HARD_TIMEOUT_SEC=300`.
- `main._v10524_enforce_manual_provider_gate` raise 423 cho token model.
- `database.save_prediction` `AI_ONCE_DAILY_SAVE_BLOCK` chặn duplicate.
- Live 14d: 2 attempts + 2 blocks logged.

Verdict: `TOKEN_GATE_CORRECT` + `MANUAL_PROVIDER_BLOCKED`.

## 8. OFFICIAL 15 / LANE-TEST 20 VERDICT

Recent final_bundles 7d (`v10529_drilldown.json:lane6_final_bundles_7d`):

| Date | MN | MT | MB |
|---|---:|---:|---:|
| 2026-05-11 | 15 | 15 | 15 |
| 2026-05-10 | 15 | 15 | 15 |
| 2026-05-09 | 15 | 15 | 15 |
| 2026-05-08 | 15 | **13** | 15 |
| 2026-05-07 | 15 | 15 | 15 |
| 2026-05-06 | 15 | 15 | 15 |
| 2026-05-05 | 15 | 15 | 15 |

20/21 bundles = 15. Edge case: MT 2026-05-08 model_count=13 — đây là sự cố MT ngày đó (không phải pattern). Lane-test 20/20 gate enforced via `_select_test_lane_primary_with_full_budget` + `TEST_LANE_FULL_BUDGET_TARGET=20`.

Verdict: `OFFICIAL_15_GATE_CONFIRMED` (20/21 ngày recent) + `LANE_TEST_20_GATE_CONFIRMED` + `BELOW_BUDGET_LABEL_OK`. MT 2026-05-08 13/15 đã ghi nhận historical event 1 lần.

## 9. AI PRIORITY VERDICT

`scheduler._run_ai_models_predict` lặp `AUTO_AI_MODELS` static order: `['gpt-5-mini', 'claude-sonnet-4-6', 'gemini-2.5-flash', 'claude-opus-4-20250514', 'deepseek-reasoner', 'gemini-2.5-pro', 'gpt-5.4']`.

Strength tensor `model_strength_by_region_weekday_station_daily` anchor mới nhất **2026-05-05** (7 ngày cũ) — stale. Scheduler chưa consume tensor.

Đề xuất V105.28 shadow proposal `v10528_ai_priority_order_proposal` (24 buckets) đã có sẵn (re-materialize từ V105.28 materializer ngày hôm nay).

Verdict: `AI_PRIORITY_ORDER_GAP` + `STRENGTH_TENSOR_STALE` + `SHADOW_PROPOSAL_ONLY` + `OWNER_GATE_PENDING (P1)` để bật reorder thực sự.

## 10. SOURCE FORMULA PROOF

- `MN_D = (MN+MT+MB) D-1 + (MN+MT+MB) D-2` ✅ (code + V101 + runtime).
- `MT_D = (MN+MT+MB) D-1 + MN D` ✅.
- `MB_D = (MN+MT+MB) D-1 + MN D + MT D` ✅.
- MT D-2 leak 7d = **0 rows** (predictions.source_regions không chứa D-2/D2 cho MT).
- MB D-2 leak 7d = **0 rows**.
- MB_D_v2 (Option A = MB_D + MB D-2) shadow đã test V105.27: `auto_disable=true`, `break_ratio=0.3379`.

Verdict: `FORMULA_LOCK_CONFIRMED` + `MN_D2_CONFIRMED` + `MT_D2_LEAK_ZERO` + `MB_D2_LEAK_ZERO` + `FORMULA_EXCLUSION_ROOT_CAUSE` (MB SOURCE_FORMULA_EXCLUSION=1052 là root cause thật).

## 11. RULE105 12W/16W PROOF / GAP

- **Rule105 lives in `mined_rules`** table với fields: target_region, target_weekday, source_station, source_region, source_offset, prize_keys, hr_4w, hr_8w, **hr_12w**, **hr_16w**, composite_score, production_tier.
- 105 = 21 buckets/region (3 region × 7 weekday) × 5 rule_family avg.
- Prize set MN/MT (code `_seed_rules.py`): ĐB, G1, G2, G3, G4, G5, G7, G8 — generated, **NHƯNG** combo seeds chỉ pick `('db','g1','g7','g8','g2','g5')` + combos.
- Prize set MB (code): ĐB, G1, G2, G3, G4, G5, G6, G7 — generated, combo seeds pick `('db','g1','g2','g6','g7')` + combos.
- gpt_analyzer line 3907-3915: query mined_rules ORDER BY `hr_12w DESC, hr_16w DESC, score DESC LIMIT 5` → Rule105 top5 vào prompt official.
- V101 source-pool top5 = `v101_region_source_pool_top5_shadow` với `hr_12w`/`hr_16w` — riêng biệt với Rule105.
- gpt_analyzer line 5223+ (lane-test shadow doctrine addon): inject `v101_region_source_pool_top5_shadow` chỉ trong shadow mode.

**Gap phát hiện (`v10529_rule105_vs_v101_audit` + drilldown)**:

| Region | Allowed prize lock | Rule105 vi phạm count | Examples |
|---|---|---:|---|
| MB | ĐB, G1, G2, G6, G7 | **13** | G5+G7 (6), G1+G8 (3), G7+G8 (2), G5+GĐB (1), G2+G5 (1) |
| MN | ĐB, G1, G2, G5, G7, G8 | **6** | G6+G7 (5), GĐB+G6 (1) |
| MT | ĐB, G1, G2, G5, G7, G8 | **11** | G6+G7 (7), GĐB+G6 (3), G6 (1) |
| **Tổng** | | **30** | |

→ **`PRIZE_SOURCE_VIOLATION_DETECTED`**. 30 rules trong mined_rules dùng prize_keys ngoài owner-lock V105.29. Đây không phải bug em tạo — đây là rule mining historical với prize set rộng hơn lock. Cần owner quyết:
- A. Owner OK keep current — V105.29 prize-source lock chỉ là guideline, mined_rules có tự do mining rộng hơn.
- B. Re-mine rules với strict lock — em chuẩn bị `weekly_rule_miner.py` patch + re-run.

Verdict: `RULE105_TOP5_CONFIRMED` + `RULE105_VS_V101_SEPARATED` (không lẫn) + `PRIZE_SOURCE_VIOLATION_DETECTED (OWNER_GATE_REQUIRED)`.

## 12. MN D-2 RANKED TOP5 PROMPT WIRE PROOF / GAP

V105.27 materializer re-ran:
- `v10527_mn_d2_prompt_injection_trace = 137 rows`
- `v10527_prompt_flow_trace = 450`
- `mn_d2_prompt_seen = 137 / 137`
- `real_prompt_not_injected = 0`
- `mt_mb_d2_prompt_leak = 0`
- `coverage = 1.0`
- `model_decision_seen = 1`
- Official hash UNCHANGED.
- gpt_analyzer `_build_lane_test_shadow_doctrine_addon` (line 5137-5255) inject ranked top5 trong **MN_D2_RANKED_TOP5_SHADOW_V10527** profile — shadow-only.

Verdict: `MN_D2_TOP5_EXISTS` + `MN_D2_PROMPT_WIRED_SHADOW` + `MN_D2_PROMPT_OFFICIAL_UNTOUCHED` + `REAL_PROMPT_NOT_INJECTED_ZERO` + `MT_MB_D2_PROMPT_LEAK_ZERO` + `NEED_NATURAL_RUN_7D_14D`.

## 13. V105.29 LOSE-CARRYOVER SIGNAL LAYER — PROOF + BACKTEST

Em build mới trong V105.29:

`web/backend/_v10529_lose_carryover_materializer.py` tạo 4 shadow tables:

| Table | Rows | Notes |
|---|---:|---|
| `v10529_lose_carryover_signal_shadow` | 3785 | Per (target_date, target_region, signal_path, source_tail) signal candidates |
| `v10529_lose_carryover_backtest` | 6 | Aggregated 30d backtest per (target_region, signal_path) |
| `v10529_ai_prompt_lose_context_trace` | 40 | Prompt context trace last 7d (shadow profile `LOSE_CARRYOVER_CONTEXT_SHADOW_V10529`) |
| `v10529_rule105_vs_v101_audit` | 21 | Per (region, weekday) Rule105/V101 separation |

**Backtest 30d cho 6 signal paths**:

| target_region | signal_path | sample_n | save | break | net | break_ratio |
|---|---|---:|---:|---:|---:|---:|
| MB | cross_region_same_day_mt_to_mb | 232 | 2 | 230 | -228 | **0.9914** |
| MB | same_region_d1_to_d | 308 | 2 | 293 | -291 | **0.9932** |
| MN | cross_region_nextday_mb_to_mn | 308 | 11 | 283 | -272 | **0.9593** |
| MN | same_region_d1_to_d | 187 | 3 | 172 | -169 | **0.9663** |
| MT | cross_region_same_day_mn_to_mt | 184 | 5 | 174 | -169 | **0.9457** |
| MT | same_region_d1_to_d | 232 | 4 | 207 | -203 | **0.9367** |

**Kết luận DECISIVE**: tất cả 6 signal paths có `break_ratio` 0.93-0.99 + `net_save_break` âm sâu. LOSE-carryover **KHÔNG thể auto-promote** thành selector. Đây chính xác là evidence chứng minh owner intuition: dùng LOSE-carryover chỉ làm prompt-context supporting layer + cần xác nhận đa tầng (Rule105 + source-pool + model-strength) trước khi propose tail.

**Prompt policy** đã implement:
- Chỉ inject khi `source_status = LOSE` AND `source_actual_known = true`.
- Skip WIN sources.
- Skip UNKNOWN sources.
- `shadow_only=1`, `diagnostic_only=1`, `output_eligible=0`, `official_impact=false`.
- Không tự promote — chỉ supporting context.

Verdict: `LOSE_CARRYOVER_PARTIAL_EXISTING_V10511` (V67/V102 đã có lose-only gate trước đó) + `LOSE_CARRYOVER_PROMPT_LAYER_CREATED` (V105.29 shadow) + `LOSE_CARRYOVER_BACKTEST_CREATED` (30d) + **`LOSE_CARRYOVER_DO_NOT_PROMOTE`** + `WIN_SKIP_CONFIRMED` + `UNKNOWN_SKIP_CONFIRMED` + `MB_TO_MN_NEXTDAY_PATH_PRESENT (308 samples)`.

## 14. SOURCE-POOL MISS ROOT CAUSES

`v10524_source_pool_gap_drilldown` chưa có local (đã ghi V105.27 P1-A). Từ V105.27 report stack: MB SOURCE_FORMULA_EXCLUSION=1052, MT=1013, MN=898. PROMPT_NOT_INJECTED là measurement artifact V104 tracker.

Verdict: `SOURCE_POOL_MISS_ROOT_CAUSE` + `FORMULA_EXCLUSION_REAL` + `PROMPT_TRACKER_ARTIFACT` + `STATION_ALIAS_RAW_FORENSIC_ONLY`.

## 15. TOP2 / BUNDLER VERDICT

V105.27 materializer re-ran:
- `v10527_top2_policy_ab_shadow = 3150 rows`.
- `v10527_bundler_drop_audit_shadow = 196 rows`.
- Không policy nào pass gate `net_save>0 AND break_ratio<=0.05 AND >=14d`.

Verdict: `TOP2_AB_SHADOW_ONLY` + `TOP2_POLICY_FAIL_GATE` + `BUNDLER_DROP_CONFIRMED` + `MT_MEASUREMENT_ONLY` + `DO_NOT_PROMOTE`.

## 16. MB_D_v2 VERDICT

V105.27 materializer re-ran: `v10527_mb_d_v2_shadow = 506 rows`, `would_save=115`, `would_break=171`, `break_ratio=0.3379`, `auto_disable=true`. Option A (D-2) đã REJECTED.

Verdict: `MB_D_V2_OPTION_A_REJECTED` + `MB_D_V2_AUTO_DISABLE` + `MB_D_PRIMARY_UNCHANGED` + `DO_NOT_PROMOTE`. Option C+D chờ owner Decision #5.

## 17. V102 RELAXED VERDICT

`v10524_v102_relaxed_selector_shadow` không tồn tại local (đã ghi V105.27 P1-A). V102 promotion gate chưa met (>=14d, break_ratio<=0.05, net_save>0, owner OK).

Verdict: `V102_RELAXED_HOLD` + `V102_RELAXED_PROMOTION_BLOCKED` + `V103_SUPPLY_CLASS_GAP` + `NEED_14D_WATCH`.

## 18. STATION CANONICAL VERDICT

`station_identity.py` chứa: `Thừa Thiên Huế` ✅, `TP. HCM` ✅, `Đắk Lắk` ✅, `Đắk Nông` ✅, `Bà Rịa` / `Vũng Tàu` reference (cần audit thêm cho Bà Rịa - Vũng Tàu canonical). Runtime unexpected_count=0.

Verdict: `STATION_ALIAS_ZERO` + `WEEKDAY_AS_STATION_ZERO_STRICT` + `RAW_FORENSIC_PRESERVED` + `HUE_CANONICAL_OWNER_DECISION` (owner chưa chốt Huế vs Thừa Thiên Huế).

## 19. LO1/LO2 SCOPE VERDICT

- `LANE_TEST_LO2_POS_WEIGHT_BY_REGION = {MB: 0.95, MN: 0.55, MT: 0.55}` chỉ ở `_materialize_du_doan_test_model_budget.py` + `_materialize_adaptive_exploit_v1.py` + `main.py` audit-replay.
- Official `/du-doan`, `combo_super`, `generate_final_bundle` KHÔNG consume.

Verdict: `LOZ_MIXING_LANE_ONLY` + `OFFICIAL_NOT_AFFECTED` + `LO2_WEIGHT_DIAGNOSTIC_ONLY`.

## 20. MT PROTECT REGRESSION VERDICT

MT D-2 leak 7d = 0. MT source formula, selector, scoring, prompt, roster, lo2 weight KHÔNG đổi. Mọi shadow layer (V105.29 lose-carryover, MN D-2 prompt wire, Top2 A/B, MB_D_v2) không touch MT production.

Verdict: `MT_PROTECT_PRESERVED` + `MT_TOUCH_SAFE_STABILITY_ONLY` + `MT_D2_LEAK_ZERO` + `MT_RISK_BLOCKED`.

## 21. SECURITY / PAT / SSH VERDICT

- Owner đã confirm PAT revoked (V105.28 mission + V105.29 mission).
- Secret scan public/docs/artifacts: 0 hit thật (chỉ `.env` local có 6 secret values, đã gitignore line 28, `git ls-files` empty).
- Git remote `Lottery_AI_Test`: `https://github.com/irissnss/Lottery_AI_Test.git` (still HTTPS).
- Git remote `Lottery_AI_Notion_Reports`: `https://github.com/irissnss/Lottery_AI_Notion_Reports.git` (still HTTPS).
- Sau PAT revoke → push HTTPS sẽ fail.

Verdict: `OWNER_CONFIRMED_PAT_REVOKED` + `SECRET_SCAN_CLEAN_PUBLIC` + `ENV_LOCAL_NOT_TRACKED` + `SSH_DEPLOY_KEY_PENDING` + `HTTPS_REMOTE_RISK_AFTER_PAT_REVOKE` (P1 blocker).

## 22. OFFICIAL HASH PRE/POST

`artifacts/v10529/v10529_post_hash.json` + `v10529_preflight.json`:

| Table | Pre rows / sha256 (first16) | Post rows / sha256 | Unchanged |
|---|---|---|---|
| predictions | 4791 / `a50f257db00acb36…` | 4791 / `a50f257db00acb36…` | ✅ true |
| final_bundles | 219 / `e6da525afc4c291c…` | 219 / `e6da525afc4c291c…` | ✅ true |
| lottery_results | 14655 / `564377b65ae7677e…` | 14655 / `564377b65ae7677e…` | ✅ true |
| model_daily_eval | 4655 / `a5c2f35c7d06a209…` | 4655 / `a5c2f35c7d06a209…` | ✅ true |

→ `ALL_OFFICIAL_TABLES_UNCHANGED = true`.

## 23. PROVIDER / MANUAL AI CALL COUNT

**0**. Không có tool nào trong session gọi OpenAI / Claude / Gemini / DeepSeek / Grok / Qwen / OpenRouter / Cohere / GLM. Mọi script V105.29 đều read-only SQL hoặc shadow-write.

Verdict: `NO_PROVIDER_CALL_CONFIRMED`.

## 24. OPEN ISSUES P0/P1/P2

| Rank | ID | Issue | Severity | Action |
|---|---|---|---|---|
| P0 | V10529-A | `_safe_stdio_ctx` VPS deploy pending → MN cascade tiếp tục fail no-token rerun | P0 stability | Owner OK → chạy `_v10529_DEPLOY_SAFE_STDIO_VPS.md` |
| P1 | V10529-B | AI_PRIORITY_ORDER_GAP (scheduler static, không strongest-first) | P1 quality | Owner OK → reorder per region+weekday |
| P1 | V10529-C | Strength tensor anchor stale 2026-05-05 | P1 measurement | Cron daily 19:30 VN |
| P1 | V10529-D | SSH deploy key chưa migrate; HTTPS push sẽ fail | P1 infra | Owner setup SSH |
| P1 | V10529-E | PRIZE_SOURCE_VIOLATION_DETECTED — 30 mined_rules dùng prize_keys ngoài owner-lock | P1 governance | Owner quyết keep / re-mine |
| P1 | V10529-F | Public GitHub raw still V105.27 — local đã V105.28+V105.29 | P1 SSOT | Owner OK push sau khi SSH migrate |
| P2 | V10529-G | V102 relaxed table + v10524_source_pool_gap_drilldown chưa persist trong VPS DB | P2 measurement | Deploy materializer cron VPS |
| P2 | V10529-H | Notion V105.29 page chưa tạo | P2 SSOT | Sẽ tạo khi report final approve |

## 25. OWNER DECISIONS NEEDED

Em chuẩn bị format trả lời (anh chỉ cần ghi `A,B,C` hoặc số):

| # | Decision | Recommendation |
|---|---|---|
| #1 | Publish V105.24/25/25b/26/27/28/29 lên Drive + Notion + public GitHub sau khi SSH+SSOT verify | A. YES (recommend) |
| #2 | Canonical kỹ thuật `Thừa Thiên Huế`; UI có thể hiển thị `Huế`; không split station | A. YES |
| #3 | MN D-2 shadow 7/14d, MN-only, no MT/MB leak | A. YES |
| #4 | Top2/Bundler A/B shadow 14d MN+MB; MT measurement-only | A. YES |
| #5 | MB_D_v2 scope = C + D; HOLD A; no MB D-2 primary | A. YES (C+D) |
| #6 | V102 relaxed HOLD đến gate met | A. YES |
| #7 | Manual AI/provider blocked | A. YES |
| #8 | MB rerun_post_mn intermediate hiển thị với label `(stage=rerun_post_mn)` | A. YES |
| #9 | Hoàn tất SSH deploy key migration (PAT đã revoke owner-confirmed) | A. CONFIRM |
| #10 | Deploy `_safe_stdio_ctx` wide patch lên VPS (script sẵn) | A. CONFIRM |
| #11 | V105.29 lose-carryover signal layer shadow-only + prompt-context-only sau khi P0 ổn | A. YES |
| #12 | Rule105 12W/16W vs V101 separation audit — tiếp tục audit; nếu PRIZE_SOURCE_VIOLATION cần fix: re-mine với strict lock | B. Re-mine với strict lock (recommend) hoặc A. Keep current |
| #13 | Daily station regression cron + daily 00:05 VN runtime snapshot | A. YES |
| #14 | AI strongest-first runtime reorder | A. HOLD (chờ shadow proposal verify thêm 7d) |
| #15 | KHÔNG promote Top2/Bundler, MB_D_v2, V102 relaxed, V105.29 cho tới khi gate pass | A. HOLD (cứng) |

## 26. EXACT NEXT ACTIONS FOR TOMORROW

1. **(Sau owner OK #10)** Chạy `_v10529_DEPLOY_SAFE_STDIO_VPS.md` deploy script. Verify post-deploy: `journalctl -u lottery.service | grep -c 'closed file'` plateau, MN cascade trả 7/7+7/7.
2. **(Sau owner OK #9)** Setup SSH key cho `Lottery_AI_Test` + `Lottery_AI_Notion_Reports`; `git remote set-url origin git@github.com:...`.
3. **(Sau owner OK #1)** Push public mirror: `git -C E:/Lottery_AI_Notion_Reports add -A && git commit -m "V105.29 + V105.28 + V105.27 backfill" && git push`.
4. **(Sau owner OK #12B)** Re-mine `mined_rules` với strict prize-source lock.
5. **(Sau owner OK #14)** Wire scheduler reorder + daily 19:30 VN tensor refresh cron.
6. Notion V105.29 page (em sẽ tạo sau owner approve report).

## 27. DO_NOT_PROMOTE LIST

- V105.29 Lose-Carryover Signal Layer (break_ratio 0.93-0.99).
- Top2/Bundler A/B (no policy passed gate).
- MB_D_v2 Option A (auto_disable=true, break_ratio=0.3379).
- V102 relaxed (gate not met; needs >=14d).
- AI strongest-first runtime reorder (shadow only until owner approve).
- MN D-2 ranked prompt wire (shadow only; need natural-run 7/14d).

## 28. PASS / PARTIAL FINAL VERDICT

**`PARTIAL_NOT_PASS`.**

- ✅ 14 lanes PASS (DD, retrain, token guard, gates, formula, station, lo2, MT protect, MN D-2 shadow, lose-carryover shadow, rule105 separation evidence, official hash unchanged, no provider call, MT D-2 zero leak).
- ❌ 2 lanes vẫn open: `_safe_stdio_ctx` VPS deploy pending + AI priority reorder gap.
- ❌ 1 governance: PRIZE_SOURCE_VIOLATION_DETECTED cần owner quyết.
- ❌ SSOT: public raw still V105.27 + SSH not migrated.

PASS_FULL chỉ đạt khi: (1) `_safe_stdio_ctx` deployed live + 1 natural cascade chứng minh closed_file=0; (2) SSH migrated + public raw push V105.28/V105.29; (3) Rule105 prize-source violation resolved (re-mine hoặc owner confirm keep); (4) AI priority reorder enable.

---

## Phụ lục

- `artifacts/v10529/v10529_preflight.json` — pre-hash + env state.
- `artifacts/v10529/v10529_safe_stdio_smoke.json` — 3/3 PASS proof.
- `artifacts/v10529/v10529_master_audit.json` — 20-lane audit.
- `artifacts/v10529/v10529_drilldown.json` — LANE 6/9/14 drill.
- `artifacts/v10529/v10529_post_hash.json` — pre/post identical 4/4.
- `artifacts/v10529/_v10529_DEPLOY_SAFE_STDIO_VPS.md` — deploy script + rollback.
- `web/backend/_v10529_lose_carryover_materializer.py` — V105.29 shadow tables.
- DB shadow tables: `v10529_lose_carryover_signal_shadow` (3785), `v10529_lose_carryover_backtest` (6), `v10529_ai_prompt_lose_context_trace` (40), `v10529_rule105_vs_v101_audit` (21), `v10529_runtime_summary` (4).

Stability first. Evidence first. No official touch. No provider calls. MT protect preserved. D-2 only MN. Rule105 separate from V101 source-pool. LOSE-carryover prompt layer only when source LOSE + actual known. No PASS-wash.
