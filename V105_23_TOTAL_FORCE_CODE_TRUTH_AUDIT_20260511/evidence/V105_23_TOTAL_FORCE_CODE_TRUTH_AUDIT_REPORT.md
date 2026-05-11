# V105.23 TOTAL FORCE SOURCE-POOL GAP + TOKEN-COST SAFE LIVE AUDIT

Generated: 2026-05-11 11:20 VN  
Final acceptance: **PARTIAL, không PASS**.

## Executive

Official `/du-doan` vẫn an toàn: 4 bảng official giữ nguyên hash trước/sau khi refresh shadow live-prep trên VPS. Token-cost guard đang có trong code và runtime hiện tại không có process manual/provider bất thường; current PID journal không có traceback/provider trigger mới.

Không được claim hoàn hảo: `SOURCE_POOL_MISS` vẫn là blind spot chính; V102 strict shadow vẫn `0 rows`; MT/MB lane-test hiện dưới 20/20 ở các row chính; V105.23 drilldown chi tiết theo station/prize/formula-stage mới dừng ở JSON artifact, chưa thành bảng/admin API riêng.

## Sources Read

- Governance/private repo: `.Antigravityrules.md`, `.antigravityrules`, `.AGENT.md`, `.cursorrules`, `CHANGELOG.md`, `docs/CURRENT_TRUTH_SSOT.md`, `docs/FOLLOW_UP_TRACKER.md`, `docs/AUTOMATION_STATE.json`, `docs/AUTOMATION_HISTORY.jsonl`.
- Active roadmaps: `docs/ACTIVE_ROADMAP_LAG1_ADAPTIVE_EXPLOIT.md`, `docs/ACTIVE_ROADMAP_CROSS_REGION_LEAKAGE.md`; no overdue checkpoint in this pass.
- Public GitHub: V105.22 public live-prep evidence was the previous latest.
- Notion MCP: root `Lottery_AI_Test` and V105.19/V105.20/V105.21/V105.22/MASTER/FULL SPECTRUM pages were checked before code-truth audit.
- Drive/local attachments: `Báo Cáo 20 Update Liên Tục`, `Báo Cáo 19 Update Liên Tục`, `Phân Tích Đánh Giá 4`, `Phân Tích Đánh Giá 5` were available locally; Drive Folder 2 remains `DRIVE_FOLDER_2_EMPTY_OR_NO_ACCESS`.
- Live sync: `artifacts/live_sync/latest_manifest.json` at `2026-05-11T11:16:24+07:00` proves local DB and prediction trace were synced from VPS after shadow refresh.

## Version Matrix

- Private head: `e626ba74d968b38479e1d261c9ea56029704c361 V20.3.37.105.22: prepare region-independent live prep`.
- VPS runtime head: `ceb36c2daaff3b4a265a9e2b7a047abd7bfa8aad V17.19.4 production snapshot (2026-04-19)`. This is git metadata drift risk; deployed files can be ahead of git head.
- Public latest before this push: V105.22.
- Notion latest relevant pages before this push: V105.22 live prep / region strategy / live checklist.

## Official Safety Proof

VPS command run: `python3 web/backend/_v10522_live_prep.py --date 2026-05-11 --days 30 --json`.

Official hash pre/post from V105.23 remote refresh:

- `predictions`: 4750 rows, `4e7ec39408cfd5ace2f49abfa51a0acd9d11b4701e8716b1faccf829ba5f7293` pre = post.
- `final_bundles`: 217 rows, `a3b12676ec1be9386e66c9fff640c70d651614fd5ae8c6aabad3974b30a14c91` pre = post.
- `lottery_results`: 14649 rows, `1dfdcb41cfd9f7cea2863bb70d0d3e1ca04270eb62fb547533dd4ac4948df9ad` pre = post.
- `model_daily_eval`: 4572 rows, `bd716238c1e56bf1551f494049a3622acf7faddf2747d47ec9f6a48b6877a952` pre = post.

Endpoint smoke:

- `/api/health=200`, `/api/status=200`, `/du-doan=200`.
- `/api/final-bundle?region=MN/MT/MB=200`.
- `/du-doan-test=401` unauth and `/api/admin/v10522-live-prep=401` unauth; access control expected.

## Token-Cost Proof

- `OWNER_MANUAL_PROVIDER_CALLS_ENABLED=false` by default.
- `OWNER_STARTUP_SHADOW_CATCHUP_PROVIDER_ENABLED=false` by default.
- `OWNER_AI_TOKEN_ONCE_DAILY_ONLY=true` by default.
- Admin manual `/api/scheduler/run-now/{region}` and `/api/scheduler/shadow-eval-now` are HTTP 423 when owner manual gate is off.
- `_run_ai_predict_job()` writes `[AI_ONCE_DAILY_ATTEMPT]` and checks `_owner_ai_token_attempt_exists()` before provider execution.
- `database.save_prediction()` blocks duplicate TOKEN-class model rows and forces token models to DD Sau.
- Current VPS process scan matched no manual/provider worker.
- Current VPS PID journal scan had `hit_count=0` for `Traceback`, `I/O operation on closed file`, `AI Predict Job triggered`, `SHADOW_COMPLETION_TRIGGER`, `[API] Attempt`, `KEY_MODE`, `MANUAL_PROVIDER`.

Important nuance: DB `scheduler_logs` still contains older 2026-05-11 MN shadow tracebacks from before `_safe_print`; current PID journal is clean, so those are historical rows, not current process evidence.

## Region Profiles

`lane_test_region_profiles=3`, all `official_impact_allowed=0`, `exact_model_count=20`.

- MN: `MN_LANE_TEST_PROFILE`; formula `(MN+MT+MB) D-1 + (MN+MT+MB) D-2`; `lo2_weight=0.55`; V102 shadow enabled; no official promotion.
- MT: `MT_LANE_TEST_PROFILE`; formula `(MN+MT+MB) D-1 + MN D`; `protect_mode=1`; `lo2_weight=0.55`; primary V102 injection disabled.
- MB: `MB_LANE_TEST_PROFILE`; formula `(MN+MT+MB) D-1 + MN D + MT D`; `lo2_weight=0.95`; forensic only.

Formula isolation check: `MT d2_rows=0`, `MB d2_rows=0`, `MN d2_rows=3080`; D-2 is not leaking into MT/MB.

## Source-Pool Miss

Current V105.22 surfaces exist:

- `bundle_universe_coverage_daily=3076`.
- `source_prize_strong_coverage=3076`.
- `rule_injection_contract=3076`.
- `candidate_drop_stage_daily=102`.

Dominant drop reasons:

- MN: `SOURCE_POOL_MISS` invisible `28/28`, `PROMPT_NOT_INJECTED=1212`.
- MT: `SOURCE_POOL_MISS` invisible `24/29`, `PROMPT_NOT_INJECTED=994`.
- MB: `SOURCE_POOL_MISS` invisible `14/18`, `PROMPT_NOT_INJECTED=671`.

This proves the main blind spot remains before prompt/rank/bundle, not only selector ranking. Current table still lacks full V105.23 fields: `source_formula_stage`, `source_available`, `source_result_complete`, `station_alias_block`, `prize_lock`, `ranked_not_top2`, `top2_not_bundle`, `bundle_not_ui` at per-station/prize granularity.

## V102 STRONG

`v10522_v102_strong_selector_shadow=0`.

Reason from DB/code:

- `_v10522_live_prep._materialize_v102_shadow()` only inserts candidates from `v103_candidate_supply_shadow` where `v102_recurrence_class='STRONG'` or `v102_recommendation='PROMPT_REVIEW_STRONG'`.
- Latest `v103_candidate_supply_shadow` max date is `2026-05-09`.
- Per region latest supply rows: 100 each for MN/MT/MB.
- `v102_strong_or_prompt=0` for MN/MT/MB.
- Strict/relaxed counts in audit probe are all `0` because no row satisfies the upstream V102 STRONG/PROMPT_REVIEW_STRONG seed condition.
- Owner tails `68/78/02/82` appear in candidate supply history, but sampled rows have `v102_recurrence_score=0` or null class/recommendation.

Therefore `0 rows` is explained as upstream recurrence-context absence, not selector pass.

## Lose-Only Proof

30d after refresh:

- MB: `recycled_from_win_count=0`, `source_actual_unknown_used=0`, `pass_gate=1`.
- MN: `recycled_from_win_count=0`, `source_actual_unknown_used=0`, `pass_gate=1`.
- MT: `recycled_from_win_count=0`, `source_actual_unknown_used=0`, `pass_gate=1`.

`_materialize_adaptive_exploit_v1.py` admits D-1 and same-day cross-region candidates only when source BT/lo2 was LOSE; source WIN and unknown same-day actuals are skipped.

## Model Count / Timeout

- Official latest final bundle for 2026-05-11: MN `model_count=15`; MT/MB not yet final at audit time.
- Lane-test latest rows: MN `MN_ADAPTIVE_BUDGET_SELECTOR_V1 model_count=20`; MT `MT_ADAPTIVE_EXPLOIT_V1 model_count=4`; MB `MB_ADAPTIVE_EXPLOIT_V1 model_count=5`.
- UI/API gates lane primary with `TEST_LANE_FULL_BUDGET_TARGET=20`; sub-budget row is `PREVIEW_PHU_BELOW_BUDGET`, not READY.
- Timeout code truth: `AI_MODEL_SOFT_CONTINUE_SEC=90`, `AI_MODEL_HARD_TIMEOUT_SEC=300`.

## LO1/LO2

- `LANE_TEST_LO2_POS_WEIGHT_BY_REGION`: MB `0.95`, MN/MT `0.55`.
- `main.py` read-only audit uses the same weights for `/api/admin/lo1-lo2-audit/{region}`.
- No official production selector reference was found to these lane-test weights.
- MB remains forensic because lo2/weighted remains weaker despite BT signal.

## UI / History / Monitoring

- `/monitoring` includes V105.22 Live Prep panel with region profile, V102 shadow, coverage, lose-only, MB forensic, station audit.
- `/du-doan-test` displays under-budget warning and challenger rows separately.
- `MAIN_TEST_EQUALS_OFFICIAL` marker exists in admin readiness/diff API path; `/du-doan-test` uses a different meta/copy path and should be wired to exact marker in V105.23 follow-up.
- `du_doan_test_*` engine/evaluator writes would-save/would-break/false-promotion/history only; official tables are not written.

## Station Identity

`station_identity.py` is SSOT:

- `Huế` -> `Thừa Thiên Huế`.
- `HCM`, `TPHCM`, `TP HCM`, `TP.HCM` -> `TP. HCM`.
- `Đắc Lắc` -> `Đắk Lắk`.
- `Đắc Nông` -> `Đắk Nông`.

Runtime station audit after refresh: `unexpected_count=0` for `lottery_results.station` and `pnl_daily_settlements.station`. Raw `lottery_results.station` remains forensic, not mutated.

## Security

Secret scan pattern results:

- Exact PAT-like/token-like pattern matched files: `docs/AUTOMATION_STATE.json`, `artifacts/1.Báo Cáo Cursor/Báo Cáo 17 Update Liên Tục.txt`.
- Provider env-name references appear in code/docs/backups; this is not equivalent to exposed values.
- No full token is printed in this report.

Security remains owner-pending: revoke exposed/old PATs in GitHub UI and migrate VPS deploy to SSH key.

## Remaining Contradictions

- VPS git head is stale (`V17.19.4`) while private repo head is V105.22-era. Runtime files may be ahead of git, but traceability drift remains.
- V105.22 materializer can refresh 30d window, but because 2026-05-11 actuals are not available yet, coverage/drop-stage max date remains `2026-05-10`.
- V105.23-required drilldown and relaxed V102 diagnostics are not persisted as first-class DB tables/API.

## Next Plan

Immediate 24h:

- Create V105.23 shadow-only materializer/table for `v10523_source_pool_gap_drilldown` and `v10523_v102_relaxed_selector_shadow`.
- Add admin read-only endpoint/panel for source_pool -> prompt -> rank -> top2 -> bundle -> UI.
- Keep provider/manual calls closed; verify only by DB/log/API/materializers.

7 days:

- Track MN save/break with exact 20/20 only; no promotion until owner gate.
- Keep MT protect mode and measure would-save/would-break separately.
- Run MB forensic dashboard for AI-chain suppression, LO2 weakness, and source_pool_miss.

14 days:

- Reassess source-pool formula performance by region+weekday+station-set.
- If V102 relaxed finds consistent save without break, propose lane-test-only selector experiment, not official promotion.
- Complete SSH deploy key migration and PAT revocation confirmation.

## Final Acceptance

**PARTIAL**.

Reasons not PASS:

- SOURCE_POOL_MISS remains unresolved and lacks full V105.23 drilldown table/API.
- V102 strict remains 0 rows; relaxed diagnostic exists only in JSON audit, not persistent shadow table/API.
- MT/MB current lane rows are under 20/20 and must remain preview/diagnostic.
- Security PAT revocation remains owner-pending.
