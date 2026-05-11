# V105.28 — TOTAL FORCE RUNTIME CONTRACT VERIFY (2026-05-11, 23:35 VN)

> Báo cáo Owner. Tiếng Việt. Read-only/shadow-only. Không gọi provider. Không động official. MT_PROTECT_MODE giữ tuyệt đối. Công thức MN/MT/MB lock.

## 0. EXECUTIVE SUMMARY

V105.28 audit kết quả là **PARTIAL_NOT_PASS**. Hệ thống hiện đáp ứng phần lớn contract owner mới (DD Trước/DD Sau, retrain-before-rerun, 90s soft timeout, official 15 / lane-test 20, region-only freeze, manual provider block, MT protect, PAT revoke confirmation). Tuy nhiên còn 2 gap thật chưa thể gọi PASS:

1. **CLOSED_FILE_DEPLOY_PENDING** — `_safe_stdio_ctx` đã có trong code local cho path AI token (`_start_timed_model_call`) nhưng KHÔNG được áp cho path no-token rerun (`_rerun_free_models_after_scrape` → `_run_smart_ensemble` / `_run_smart_ml_ensemble` / `_run_combo_no_token` / `_run_free_model_prediction`). Live VPS có **86 closed_file errors** ngày 2026-05-11 + **25 errors** ngày 2026-05-10 trong MB no-token rerun. Owner đã approve deploy ở V105.27 Decision #10 nhưng chưa deploy.
2. **AI_PRIORITY_ORDER_GAP** — scheduler `_run_ai_models_predict` lặp `AUTO_AI_MODELS` theo thứ tự static từ registry. Không có reorder theo `region + weekday + station_set` từ `model_strength_by_region_weekday_station_daily`. Strength tensor đã có (anchor mới nhất 2026-05-05) nhưng chưa được tiêu thụ. Đã materialize đề xuất `v10528_ai_priority_order_proposal` (24 buckets) — shadow-only, owner cần OK trước khi áp vào scheduler.

Mọi nhánh khác PASS hoặc PARTIAL theo hướng có lợi. Official 4-bảng tuyệt đối không đổi trong session này (pre/post SHA256 4/4 IDENTICAL).

## 1. KHÔNG GỌI PROVIDER / KHÔNG ĐỘNG OFFICIAL — BẰNG CHỨNG

- Live sync manifest: `artifacts/live_sync/20260511_231809/manifest.json` (DB pulled từ VPS, sha256 = `7000bdc7396838910520ebbb22bf11a28fd40787532ab2e1d4823510e4d39c51`).
- Pre-hash (artifacts/v10528/v10528_preflight.json):
  - predictions=4791 sha256=`a50f257db00acb36e4aef91d62955cdce2a8a6ed9845d7fe23dcb8d0a600e6ea`
  - final_bundles=219 sha256=`e6da525afc4c291c7cb1d105620c44ee10db300d5d183d54c419dbfef592d130`
  - lottery_results=14655 sha256=`564377b65ae7677e25d0fbc2e15dfe73ba0076aeaaa523273f81926d69a1dbb6`
  - model_daily_eval=4655 sha256=`a5c2f35c7d06a2097f28746118a25d51f918736225ea198ad6cc7d7304024c79`
- Post-hash (artifacts/v10528/v10528_post_hash.json) khớp pre-hash 4/4 → `ALL_OFFICIAL_TABLES_UNCHANGED = true`.
- Provider/manual AI call count session này: **0**.
- Scripts đụng vào: `_v10528_preflight.py`, `_v10528_runtime_contract_audit.py`, `_v10528_deep_probes.py`, `_v10528_security_and_rules.py`, `_v10528_post_hash.py`, materializer `web/backend/_v10528_runtime_contract_materializer.py` — tất cả read-only đối với 4 official tables; materializer chỉ ghi vào `v10528_*` shadow tables.

## 2. NO-TOKEN DD TRƯỚC / DD SAU CÓ HOẠT ĐỘNG ĐÚNG KHÔNG?

**Câu trả lời: ĐÚNG.** `DD_COLUMN_POLICY` trong `web/backend/model_registry.py` mã hóa contract owner mới:

| Slot | MN | MT | MB |
|---|---|---|---|
| 04:00_all_regions | DD_SAU | DD_TRUOC | DD_TRUOC |
| 04:15_MN_only | DD_SAU | — | — |
| completion_triggered_shadow | DD_SAU | DD_TRUOC | DD_TRUOC |
| ai_chain_post_verify | DD_SAU | DD_SAU | DD_SAU |
| shadow_eval_post_verify | DD_SAU | DD_SAU | DD_SAU |
| cascade_rerun_post_verify | DD_ROTATION | DD_ROTATION | DD_ROTATION |

`database.save_prediction` thực thi:
- LOCK guard per-row: nếu `existing.status` ∈ {WIN, LOSE, PARTIAL} → return không ghi đè (region-only freeze).
- `AI_ONCE_DAILY_SAVE_BLOCK`: token model không cuốn chiếu dù được gọi lần 2.
- Cutoff per region: MN luôn `is_after_scrape=True`; MT cutoff = `schedule_mn` (16:30); MB cutoff = `schedule_mt` (17:30).
- Cuốn chiếu chuẩn: post-cutoff + existing không có real pre → `pre_result_numbers = old main`, `main_numbers = new`.

Audit shadow table `v10528_dd_truoc_dd_sau_audit` (64 buckets 7d): MN auto_daily=15 rows/day → DD_SAU_OK, MT/MB rerun_post_X xuất hiện theo đúng chuỗi → DD_ROTATION_OBSERVED, MT/MB auto_daily 04:00 ghi pre=null (CASE 1) → DD_TRUOC_OK.

→ **DD_TRUOC_DD_SAU_MATCH**.

## 3. NO-TOKEN RETRAIN/RELOAD TRƯỚC RERUN — CÓ ĐÚNG THỨ TỰ KHÔNG?

**Câu trả lời: ĐÚNG (theo nghĩa feature/eval refresh; không phải full ML weight retrain).**

Thứ tự trong `_run_auto_update(region)`:
1. Scrape lottery_results (đã có trong DB trước khi nhánh verify chạy).
2. `verify_prediction(today, region, all_tails, ...)` → predictions.status đổi sang WIN/LOSE/PARTIAL.
3. `verify_final_bundle(today, region, ...)` → final_bundles.verified_at được set.
4. `classify_day_status(today, region, source='auto_verify')` → day governance.
5. `_materialize_closeout_measurements(today, region)` → OUTPUT_FORENSICS / FRESHNESS_CHAIN / EXT_MEASUREMENTS / WAVE1_CONTROL / CCPD / PP1_WATCH / VERDICT_DIST / PROMPT_SECTION / OUTPUT_POLICY_REPLAY (chỉ ghi shadow tables).
6. `update_daily_stat(today, '<region>_verified', 1)` → daily_stats cập nhật.
7. `REGION_FROZEN_H2_ONLY` log (chỉ block H2 rescrape cho region đã verify, **không global freeze**).
8. `_rerun_free_models_after_scrape(today, trigger_region=region)` → re-predict no-token cho miền hạ lưu với fresh same-day cross-region tails từ lottery_results (V6.8 path).
9. `_run_ai_predict_job(next_region, run_source='ai_chain')` → AI token chain.

Quan trọng:
- "Retraining" theo nghĩa cập nhật model weights (LSTM/XGB/RF) chỉ chạy 1 lần/tuần (CN 02:00 AM `Retrain LSTM+Meta`).
- Per-verify path KHÔNG retrain weights mà refresh **fresh_cross_tails** từ `lottery_results` + `model_daily_eval` + `training_history` → no-token rerun ăn input mới ngay lập tức.
- Đây vẫn đáp ứng owner contract: "nạp dữ liệu vừa cào → cập nhật no-token state → mới rerun no-token miền sau".

Audit shadow table `v10528_retrain_order_lineage` (24 region-day events 7d) đa số markers seen theo đúng thứ tự `VERIFY_FINAL_BUNDLE → FRESHNESS_CHAIN → REGION_FROZEN_H2_ONLY → RERUN_NO_TOKEN → AI_PREDICT_CHAIN`.

→ **RETRAIN_BEFORE_RERUN_CONFIRMED** (feature refresh + eval update, weekly weight retrain riêng).

## 4. AI MODEL MẠNH THEO MIỀN/THỨ — CÓ ƯU TIÊN CHẠY TRƯỚC KHÔNG?

**Câu trả lời: KHÔNG (đây là gap).**

`scheduler._run_ai_models_predict` ở `web/backend/scheduler.py:3993` chạy:
```python
for ai_model in AUTO_AI_MODELS:  # static order from model_registry.TOKEN_MODELS
    ...
```

`AUTO_AI_MODELS` = `['gpt-5-mini', 'claude-sonnet-4-6', 'gemini-2.5-flash', 'claude-opus-4-20250514', 'deepseek-reasoner', 'gemini-2.5-pro', 'gpt-5.4']` — thứ tự cố định, không phụ thuộc `target_region` hay `weekday`.

`model_strength_by_region_weekday_station_daily` tồn tại nhưng KHÔNG được scheduler tiêu thụ trước khi lặp models. Anchor mới nhất của tensor là `2026-05-05` (6 ngày cũ) → tensor cũng đang stale, cần refresh trước khi enforce strongest-first.

Em đã materialize **đề xuất shadow-only** `v10528_ai_priority_order_proposal` (24 buckets region×weekday) thay cho gap, ví dụ:
- MN weekday 0: proposed order = top-7 token models theo `bt_rate` tại anchor 2026-05-05.
- MT/MB tương tự, nhưng nguồn dữ liệu chỉ là measurement, chưa áp vào scheduler.

→ **AI_PRIORITY_ORDER_GAP**. Cần owner OK 2 việc: (a) refresh strength tensor mỗi ngày (cron job), (b) cho phép scheduler reorder TOKEN_MODELS theo top-7 per region+weekday. Tuyệt đối không bỏ model nào — chỉ đổi thứ tự.

## 5. 90S SOFT / 300S HARD TIMEOUT — TRIỂN KHAI THẾ NÀO?

**Câu trả lời: CHUẨN TRONG CODE; LIVE ĐÃ THẤY SOFT 90S; CHƯA THẤY HARD 300S.**

`scheduler.py`:
- `AI_MODEL_SOFT_CONTINUE_SEC = int(os.getenv("AI_MODEL_SOFT_CONTINUE_SEC", "90"))`
- `AI_MODEL_HARD_TIMEOUT_SEC = int(os.getenv("AI_MODEL_HARD_TIMEOUT_SEC", "300"))`
- `_start_timed_model_call(...)` → `concurrent.futures.ThreadPoolExecutor` 1 worker với `_ensure_safe_stdio` wrapper.
- `_await_timed_model_call(call, 90)` → nếu timeout: log `[SOFT_CONTINUE_90S]`, append vào `_pending_ai_calls`, scheduler tiếp tục model kế tiếp.
- Sau khi loop chính kết thúc: với mỗi `_pending`, `_await_model_call_to_hard_timeout(call)` đợi tới `300s - elapsed`. Nếu vẫn timeout: `{"error": "TIMEOUT_AFTER_300s", "_timeout": True, ...}` → status `TIMEOUT_300S`.

Live log audit (`v10528_timeout_event_log_audit`):
- SOFT_CONTINUE_90S last 14d: **66 events** (qwen3.6-plus, kimi-k2.5 thường được continue trước 90s).
- OK_AFTER_SOFT_CONTINUE_90S last 14d: tồn tại (model trả về kết quả < 300s, vẫn được persist nếu không bị duplicate-block).
- HARD_TIMEOUT_300S last 14d: **0** events → models hiện tất cả đều hoàn tất < 300s.

→ **SOFT_90S_CONFIRMED**, **HARD_300S_NOT_OBSERVED_IN_LOOKBACK** (không phải lỗi; nghĩa là chưa có model thật sự treo quá 300s trong 14 ngày qua).

## 6. OFFICIAL 15 / LANE-TEST 20 GATE

**Câu trả lời: ENFORCED.**

- `database.EXPECTED_MODEL_COUNT = len(_goe())` (= 15 từ `OUTPUT_ELIGIBLE_MODELS`); fallback 15.
- `main.py _build_model_count_publish_gate(surface, observed, min, max)` chỉ trả `ready=True` khi `min ≤ observed ≤ max`.
- Official surfaces:
  - `/api/final-bundle/{region}`: gate `min=max=15` → READY chỉ khi đúng 15/15. Audit 7d: 6/6 final bundle MN/MT/MB hôm nay+hôm qua đều `model_count=15`.
  - Final bundle lịch sử trước 2026-05-01 có `model_count=14` (do roster chưa được lock vào registry); recent rows toàn 15.
- Lane-test surfaces:
  - `main.py TEST_LANE_FULL_BUDGET_TARGET = 20`.
  - `_select_test_lane_primary_with_full_budget(...)` chỉ promote method là `FULL_BUDGET_PRIMARY` nếu `effective_count ≥ 20`; dưới 20 trả `PREVIEW_PHU_BELOW_BUDGET`, không publish primary.
  - V105.16.1 anti-clone: trong nhóm full-budget rows, ưu tiên candidate_bt khác baseline để tránh "clone official".

Shadow audit `v10528_model_count_gate_audit` (288 rows = 6 final_bundles + 282 experimental_preview_shadow methods cho 7d) ghi cụ thể từng dòng pass/fail.

→ **OFFICIAL_15_GATE_CONFIRMED + LANE_TEST_20_GATE_CONFIRMED + BELOW_BUDGET_LABEL_OK**.

## 7. CASCADE FREEZE — REGION ONLY, KHÔNG GLOBAL

**Câu trả lời: ĐÚNG, FREEZE CHỈ MIỀN ĐÃ VERIFY.**

- `database.save_prediction` LOCK guard kiểm `existing['status'] in ('WIN','LOSE','PARTIAL')` theo `(date, target_region, ai_model)` → từng row riêng biệt.
- `_rerun_free_models_after_scrape` LOCK guard riêng theo `(date, target_region, run_source='rerun_post_<X>')` → chỉ skip nếu cùng phase này đã ghi rows.
- `_run_ai_predict_job` LOCK guard chỉ check `run_source='ai_chain'` (không block ML rerun).
- `daily_stats` flags `mn_verified` / `mt_verified` / `mb_verified` là per-region.
- `REGION_FROZEN_H2_ONLY` log chỉ block H2 rescrape path, không chặn `_rerun_free_models_after_scrape` hay `_run_ai_predict_job` của miền hạ lưu.

Audit `v10528_freeze_scope_audit` (24 region-day): trên các ngày miền A đã verify, miền B/C vẫn có `rerun_post_A` + `ai_chain` rows được ghi vào predictions (xem evidence `v10528_deep_probes.json` mục `dd_column_distribution`).

→ **REGION_FREEZE_OK / GLOBAL_FREEZE_BUG=false**.

## 8. _safe_stdio_ctx DEPLOY & CLOSED-FILE STATUS

**Câu trả lời: CHƯA HOÀN CHỈNH — `CLOSED_FILE_DEPLOY_PENDING`.**

Code state local:
- `_SafeNullWriter` class — PRESENT.
- `_ensure_safe_stdio()` helper trong `_start_timed_model_call` — PRESENT.
- `_safe_stdio_ctx` context manager (hoặc decorator) áp rộng — **NOT PRESENT.**
- No-token rerun chain (`_run_smart_ensemble`, `_run_smart_ml_ensemble`, `_run_combo_no_token`, `_run_free_model_prediction`) gọi vào `ml_predict.py` mà KHÔNG dùng `_start_timed_model_call`, do đó không được bảo vệ.

Live log (`v10528_safe_stdio_event_audit`):
- 2026-05-11: **86** dòng "I/O operation on closed file" (MB rerun: xgboost, random-forest, lstm, meta-learning, smart_ml, smart_ensemble, combo_no_token, tại 09:38:54 VN).
- 2026-05-10: **25** dòng tương tự.
- Region distribution: MN 44, MB 24, không-region (no date_str=null) 43.
- job_name: `shadow_eval` 68 dòng + null 43 dòng.

Hậu quả: MB no-token rerun đã FAIL với "Both ML models failed" / "All 4 ML models failed" / "Both models failed" cho `Re-predict MB random-forest/xgboost/lstm/meta-learning` và các ensemble bọc ngoài (`Smart Ensemble`, `Smart ML`, `COMBO No Token`).

Proposed fix (KHÔNG deploy nếu owner chưa OK):
- Tạo `scheduler._safe_stdio_ctx()` context manager export hàm `_ensure_safe_stdio` + restore.
- Wrap `_run_free_model_prediction(...)`, `_run_smart_ensemble(...)`, `_run_smart_ml_ensemble(...)`, `_run_combo_no_token(...)` bằng `with _safe_stdio_ctx(): ...` ở phần gọi vào ml_predict.
- Hoặc patch tại `ml_predict.py` để mỗi predict function tự bảo vệ raw print/traceback.
- `python -m py_compile` local PASS, lints clean trước khi scp.
- VPS backup `backups/v105_28_safe_stdio_full_path_<timestamp>/`.
- scp file + `systemctl restart lottery.service` + `/api/health=200` + chờ 1 chu kỳ verify để confirm rerun success 14/14 (hoặc 7/7).

→ Đề xuất gửi owner: **deploy ngay (Decision #10 V105.27 vẫn còn open + nay V105.28 chứng minh đã hit thật).**

## 9. TOKEN / MANUAL PROVIDER GUARD

**Câu trả lời: ENFORCED.**

- `OWNER_MANUAL_PROVIDER_CALLS_ENABLED` default `0` (block).
- `OWNER_STARTUP_SHADOW_CATCHUP_PROVIDER_ENABLED` default `0` (block).
- `OWNER_AI_TOKEN_ONCE_DAILY_ONLY` default `1` (enforced).
- `main._v10524_enforce_manual_provider_gate(...)` raise HTTP 423 cho mọi token/provider model trên `/api/predict/{region}`.
- `/api/scheduler/run-now/{region}` và `/api/scheduler/shadow-eval-now` cũng 423.
- `scheduler._owner_ai_token_attempt_exists(...)` quét `[AI_ONCE_DAILY_ATTEMPT]` log + token prediction row để chặn re-run.
- `database.save_prediction` AI_ONCE_DAILY_SAVE_BLOCK chặn ghi đè duplicate cho token model.

Live log (`v10528_token_manual_guard_audit`, 7 checks):
- `[AI_ONCE_DAILY_ATTEMPT]` 14d: 2 rows (1 MN morning + 1 MT post-verify hoặc tương tự).
- `[AI_ONCE_DAILY_BLOCK]` 14d: 2 rows.
- `[AI_ONCE_DAILY_SAVE_BLOCK]` 14d: kiểm DB show 0 (token AI chưa retry trong window này).
- `[MANUAL_PREDICT_PROVIDER_BLOCKED]` 14d: 0.

→ **TOKEN_GATE_CORRECT + MANUAL_PROVIDER_BLOCKED**.

## 10. GITHUB PAT REVOKE / SSH KEY

- Owner xác nhận: "Key GitHub đã revoke rồi, không còn tồn key nào." → **OWNER_CONFIRMED_PAT_REVOKED = true** (đã ghi vào `v10528_security_and_rules.json:owner_confirmation`).
- Secret scan `v10528_security_and_rules.json`: 1712 files scanned (40.5 MB), pattern hits:
  - `openai_sk` 3, `anthropic_sk_ant` 1, `google_aiza` 2.
  - **All hits trong `web/backend/.env` duy nhất.** `.env` được `.gitignore` line 28 match `.env` → `git ls-files web/backend/.env` trả empty → **không tracked vào git, không lên public**.
- Public mirror + docs + artifacts: **0 hits** → **SECRET_SCAN_CLEAN cho mặt public**.
- Git remote: `origin = https://github.com/irissnss/Lottery_AI_Test.git`. SSH remote chưa cấu hình → nếu owner thực sự revoke mọi PAT thì push hiện tại sẽ fail.

→ Khuyến nghị: **SSH_DEPLOY_KEY_PENDING** — owner setup SSH deploy key trước khi push V105.28 public mirror.

## 11. 105 RULES / NO-TOKEN / PROMPT 12–16W

- `_v101_shadow_pilot.py`: mentions 12W/16W + top5 + (ĐB/G1/G2/G5/G6/G7/G8) + MN D-2; KHÔNG có MT D-2 wide. ✅
- `rule_engine.py`: mentions 12W/16W + ĐB/G1-G8; không có MN D-2 hoặc MT D-2 wide. ✅
- `weekly_rule_miner.py`: không mention 12W/16W keyword chính xác (rule miner dùng cửa sổ khác — cần audit sâu hơn nếu owner muốn).
- `_v10527_ranked_prompt_wire_shadow.py`: full mentions 12W/16W + top5 + DB/G1-G7 + MN D-2; không MT D-2 wide. ✅
- `gpt_analyzer.py`: full mentions 12W/16W + top5 + DB/G1-G7 + MN D-2; không MT D-2 wide. ✅

Prize set lock:
- MN/MT prize sources cho rule-mining: ĐB, G1, G2, G5, G7, G8 (per V101 / weekly_rule_miner code paths).
- MB prize sources: ĐB, G1, G2, G6, G7.

→ **RULE_105_SHADOW_ONLY** — 105 rules + ranked top5 + MN D-2 chỉ ở shadow/lane-test/prompt-injection-shadow. Official prompt content chưa đổi.

## 12. LOZ1 / LOZ2 MIXING SCOPE

- `LANE_TEST_LO2_POS_WEIGHT_BY_REGION = {"MB": 0.95, "MN": 0.55, "MT": 0.55}` xuất hiện trong:
  - `_materialize_du_doan_test_model_budget.py:_write_adaptive_preview_row`
  - `_materialize_adaptive_exploit_v1.py` step 5 `same_region_lo2_lag1_final_bundle`
  - `main.py LANE_TEST_AUDIT_LO2_WEIGHT_BY_REGION` cho `/api/admin/lo1-lo2-audit/{region}` replay.
- Official `/du-doan`, `generate_final_bundle`, `combo_super`: **không tiêu thụ map này**.

→ **LOZ_MIXING_LANE_ONLY**. MT giữ 0.55 (nhẹ) như spec V105.18; MB 0.95 (nặng) chỉ trong lane test.

## 13. MT PROTECT REGRESSION

Audit `v10528_mt_protect_regression_audit` (12 changes):

| Change area | Touches MT | Risk | Verdict |
|---|---:|---|---|
| MN_D2 ranked top5 shadow prompt wire | 0 | low | MT_PROTECT_PRESERVED |
| Top2/Bundler A/B shadow | 0 | low | MT_PROTECT_PRESERVED |
| V102 relaxed watch | 0 | low | MT_PROTECT_PRESERVED |
| MB_D_v2 shadow | 0 | low | MT_PROTECT_PRESERVED |
| Lane-test LO2 weight | 0 | low | MT_PROTECT_PRESERVED |
| station_identity runtime | 0 | low | MT_PROTECT_PRESERVED |
| DD Trước/DD Sau mapping | 1 (read) | low | MT_PROTECT_PRESERVED |
| AI priority proposal (shadow) | 0 | low | MT_PROTECT_PRESERVED |
| Timeout 90s/300s | 1 | low | MT_PROTECT_PRESERVED |
| Closed stdio (no-token path) | 1 | medium | MT_PROTECT_PRESERVED_BUT_NO_TOKEN_STDIO_GAP |
| MT D-2 leak audit 7d | 1 | low | MT_D2_LEAK_BLOCKED (0 rows) |
| MB D-2 leak audit 7d | 1 | low | MB_D2_LEAK_BLOCKED (0 rows) |

→ **MT_PROTECT_PRESERVED** tuyệt đối. MT chỉ "touches" ở dạng đọc/đo, không thay đổi source formula, selector, scoring, prompt official, model roster, lo2 weight chính thức.

## 14. OPEN ISSUES

| ID | Issue | Severity | Action |
|---|---|---|---|
| P0-28-A | `_safe_stdio_ctx` chưa wrap no-token rerun path → 111 closed_file errors 2 ngày qua | P0 stability | Owner OK → deploy patch + restart `lottery.service` |
| P0-28-B | AI_PRIORITY_ORDER_GAP (scheduler không strongest-first per region+weekday) | P1 quality | Owner OK → daily refresh strength tensor + scheduler reorder |
| P1-28-A | Strength tensor anchor stale (2026-05-05) | P1 measurement | Cron daily 19:30 VN materialize tensor; auto |
| P1-28-B | SSH deploy key chưa setup; HTTPS origin sẽ fail sau PAT revoke | P1 infra | Owner setup SSH + chuyển `git remote set-url origin git@github.com:...` |
| P1-28-C | weekly_rule_miner.py không thấy 12W/16W keyword trực tiếp | P2 audit | Inspect rule miner source-window logic nếu owner cần evidence sâu |
| P2-28 | V105.21/23/24/26 chưa có CHANGELOG entry chính thức trong repo local | P2 governance | Backfill rows theo Notion/Drive (đã ghi nhận trong V105.27) |

## 15. OWNER DECISIONS PENDING

1. **Deploy `_safe_stdio_ctx` full no-token path** lên VPS (đã Owner OK từ V105.27 Decision #10, V105.28 chứng minh đã hit thật → priority P0).
2. **Cho phép scheduler strongest-first reorder** TOKEN_MODELS theo region+weekday từ tensor (shadow proposal đã có). Không bỏ model nào, chỉ đổi thứ tự.
3. **Setup SSH deploy key** thay HTTPS+PAT (PAT đã revoke).
4. **Daily 00:05 VN snapshot** (carry từ V105.27).
5. **Hue canonical** (`Thừa Thiên Huế` vs `Huế`, carry từ V105.27).
6. **MB_D_v2 scope final** (carry từ V105.27).
7. **V102 relaxed promotion gate** vẫn HOLD đến >= 14 ngày + net_save>0 + break_ratio≤0.05.
8. **Top2/Bundler A/B** giữ shadow 14 ngày.
9. **Migrate strength tensor refresh cron 19:30 VN** (đã có code trong _v52_5_1, cần wire vào APScheduler).

## 16. 24H / 7D / 14D PLAN

- 24h:
  - Theo dõi tự nhiên MN scrape 16:30 + verify + MT/MB rerun → kiểm log có còn `I/O operation on closed file` không (nếu owner OK deploy patch).
  - Watch `[AI_ONCE_DAILY_ATTEMPT]` / `[AI_ONCE_DAILY_BLOCK]` count = 3 (1/region/day) — 4 rows nếu MN có 2 nhánh.
- 7d:
  - 7 chu kỳ MN→MT→MB cascade, mỗi chu kỳ kỳ vọng MT rerun_post_mn 7 success + MB rerun_post_mn 7 success + MB rerun_post_mt 7 success.
  - Final bundles MN/MT/MB đều `model_count=15`, không drift xuống 14.
  - Strength tensor anchor advance từng ngày nếu owner OK cron.
- 14d:
  - Owner đánh giá V102 relaxed + Top2 A/B + MB_D_v2 — chỉ promote nếu net_save>0, break_ratio≤0.05.
  - Nếu strongest-first reorder áp được (sau owner OK), so sánh hit rate vs static order.

## 17. CLASSIFICATION LABELS TÓM TẮT

`OWNER_CONTRACT_CONFIRMED`, `DD_TRUOC_DD_SAU_MATCH`, `RETRAIN_BEFORE_RERUN_CONFIRMED`, `NO_TOKEN_CASCADE_OK` (path-success khi stdio ok), `CLOSED_FILE_DEPLOY_PENDING`, `AI_PRIORITY_ORDER_GAP`, `SOFT_90S_CONFIRMED`, `HARD_300S_NOT_OBSERVED_IN_LOOKBACK`, `OFFICIAL_15_GATE_CONFIRMED`, `LANE_TEST_20_GATE_CONFIRMED`, `BELOW_BUDGET_LABEL_OK`, `REGION_FREEZE_OK`, `MT_PROTECT_PRESERVED`, `TOKEN_GATE_CORRECT`, `MANUAL_PROVIDER_BLOCKED`, `OWNER_CONFIRMED_PAT_REVOKED`, `SECRET_SCAN_CLEAN` (public/docs), `SSH_DEPLOY_KEY_PENDING`, `RULE_105_SHADOW_ONLY`, `LOZ_MIXING_LANE_ONLY`, `DO_NOT_PROMOTE`, **`PARTIAL_NOT_PASS`**.

---

**Status:** PARTIAL — không PASS. Official 4 bảng pre/post sha256 IDENTICAL. No provider/manual AI call. MT protect tuyệt đối. Đề xuất P0 deploy `_safe_stdio_ctx` rộng + P1 strongest-first reorder shadow, chờ owner OK.
