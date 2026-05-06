# DU-DOAN-TEST V48 START-OF-LIVE + PARALLEL COMPLETION CONTROL PASS

> Date: **2026-05-03** (audit run 10:16–10:30 +07)
> Mode: **VPS-first / read-only / verify-before-claim / no production mutation**
> Live sync: `artifacts/live_sync/20260503_101603/manifest.json`
> Production DB sha256 (after sync): `0a1c1e20647074c1933f3741d0d434508711b0df600184b9ba2203684204c0d0`
> Pre-hash: `artifacts/_du_doan_test_v48_pre_hash_20260503.txt`
> Post-hash: `artifacts/_du_doan_test_v48_post_hash_20260503.txt`
> Audit raw: `artifacts/_v48_audit_out.json`, `_v48_readiness_out.json`, `_v48_extras_out.json`

---

## 1. Executive summary

`/du-doan-test` MB lane đang ở **MANUAL_TEST_LANE (mức 3/5)**. Đã có route, API, UI, schema, engine, daily runner, dry-run; nhưng **chưa auto-run, chưa execute AI test prompt, chưa raw-25-model realtime, chưa method scoreboard, chưa latency**. 7 experiment cho 2026-05-02 thực ra là 7 transform khác nhau trên cùng 1 candidate set 8 tails × 14 voter models — **không phải 7 pipeline hoàn toàn độc lập**. Official `/du-doan` không bị đụng: 4/4 source table hash IDENTICAL pre/post audit, scheduler_logs +0 (không có marker test). Hôm nay 2026-05-03 đang đầu chu kỳ live: MN bundle đã có (BT=79 PENDING), MT/MB chờ cascade. Chưa có shadow/test row nào cho 2026-05-03 → confirm `LIVE_PARALLEL_AUTO = NO`.

---

## 2. Start-of-live 2026-05-03 readiness

| Region | Predictions today | Run sources | Final bundle today | Lottery result today |
|---|---|---|---|---|
| MN | 25 (15 auto_daily + 10 shadow_auto_eval) | full ✓ | **BT=79, lo2=[79,96], lo3=579, xien2=[79,96], xien3=[79,96,15]**, status=PENDING | 0 (chưa quay) |
| MT | 7 auto_daily | partial — chờ AI cascade | chưa có (sẽ tạo sau MN scrape ~16:42) | 0 |
| MB | 7 auto_daily | partial — chờ AI cascade | chưa có (sẽ tạo sau MT scrape ~17:42) | 0 |

Service (VPS): `lottery.service active`, PID 630181 chạy từ 01:59, uptime ~8h, `runtime_model_count=25`, `active_measurement_model_count=25`, `registry_visible_model_count=28`. Health 200.

Latest scheduler markers (sync time 10:16 +07): cuối cùng là `2026-05-02 21:33:56` của shadow_auto_eval MN cho `date_str=2026-05-03` — nghĩa là chu kỳ MN đã kick-off đêm qua 21:24, hoàn tất 21:33. Sau đó im đến giờ là **bình thường** — MT/MB chờ kết quả MN quay 16:30 mới chạy.

`/du-doan-test` 2026-05-03 state: **0 preview row, 0 test_runs, 0 test_bundles, 0 test_results** → confirm không có auto-run.

---

## 3. Official `/du-doan` integrity proof

| Check | Result |
|---|---|
| `/du-doan` unauth HTTP | 200 ✓ |
| `/api/final-bundle?region=MB` unauth HTTP | 200 ✓ (returns bundle MB 2026-05-02 BT=43) |
| `/api/final-bundle?region=MN` unauth HTTP | 200 ✓ (returns bundle MN 2026-05-03 BT=79) |
| `predictions` rows | 4098 (V47 was 4059, +39 natural live activity) |
| `final_bundles` rows | 193 (V47 was 192, +1 = MN 2026-05-03 generated last night) |
| `lottery_results` SHA-256 | UNCHANGED `4acf72d3bda7…` |
| `model_daily_eval` SHA-256 | UNCHANGED `bc7a827b642e…` |
| Scheduler markers `[DU-DOAN-TEST]` | **0 lifetime** ✓ |
| `grep main.py` test-write paths | **none** (only 2 SELECT lines at 9325-9326) ✓ |
| `grep scheduler.py` test-runner wiring | **none** ✓ |

Verdict: **OFFICIAL_DU_DOAN_UNTOUCHED**.

---

## 4. `/du-doan-test` access control proof

| Check | Result |
|---|---|
| `/du-doan-test` unauth | **HTTP 401** ✓ |
| `/api/du-doan-test/mb` unauth | **HTTP 401** ✓ |
| Admin gate code (main.py L9647) | `require_admin(request)` enforced before FileResponse ✓ |
| Admin chip in `/du-doan` (`duDoanTestLink`) | hidden by default, revealed only when `/api/auth/check` returns `role=admin` ✓ |
| UI label "Test Lane" / "EXPERIMENTAL" | present (line 431 du-doan-test.html) |
| UI label "admin/dev" | present (line 453, 468) |
| UI label "không ảnh hưởng /du-doan" | present (line 453) |
| UI safety contract (`Không ghi final_bundles`) | present (footer-note section) |
| Public navbar leak | none — Test MB chip is `display:none` until admin auth ✓ |

Verdict: **DU_DOAN_TEST_ACCESS_CONTROL_PROOF = PASS**.

---

## 5. `/du-doan-test` architecture map

```
/du-doan-test (HTML, admin-gated route, line 9647 main.py)
    │
    └─→ JS calls /api/du-doan-test/mb (admin-gated, line 9225 main.py)
              │
              ├── READ  final_bundles MB (today or fallback latest)        ─→ baseline column
              ├── READ  mb_experimental_preview_shadow (date, region=MB)   ─→ experiments[]
              ├── READ  du_doan_test_bundles JOIN du_doan_test_results     ─→ test_history
              ├── READ  lottery_results MB (for actual_tail_set)           ─→ status badges
              └── CALL  _generate_lo3_frequency(test_bt, "MB", date)       ─→ test_bundle.lo3 (V48.1)

UI shows:
- Hero compare-grid 2-col × 6 rows: header + BT + lo2 + lo3 + xien2 + xien3
  Left  = official (final_bundles, blue/purple)
  Right = test challenger (gold/amber, primary auto-picked from priority list)
- 30-day backtest snapshot (HARDCODED in API — see §17, §19 caveat)
- Experiment list (all 7 experiments with chip Would Save / Would Break / PRIMARY)
- Test history (du_doan_test_bundles + du_doan_test_results JOIN)

Writes from this entire surface: NONE.
Writers (manual only):
- web/backend/_materialize_mb_experimental_preview_shadow.py → mb_experimental_preview_shadow
- web/backend/_du_doan_test_mb_engine.py → du_doan_test_*
- web/backend/_du_doan_test_daily_runner.py → calls the two above (manual CLI)
```

Fallback rule: if today has no shadow rows, API auto-falls back to `MAX(date)` from `mb_experimental_preview_shadow` and sets `experiments_fallback=true`. UI shows fallback banner. Confirmed working: hôm nay sẽ trả về 2026-05-02 với fallback flag bật.

---

## 6. V46 claim verification matrix

| # | Claim | Verdict | Evidence |
|---|---|---|---|
| 1 | `_du_doan_test_mb_engine.py` exists | **VERIFIED** | file present, schema + materialize_for + backfill |
| 2 | `du_doan_test_*` 6 tables exist | **VERIFIED** | all 6 tables hash-OK in pre/post |
| 3 | 2026-05-02 MB has runs=7, bundles=7, results=7, candidates=147, contrib=147, audit=1 | **VERIFIED** (audit=1 lifetime, others all 7/147) | sec_06_test_state |
| 4 | `/du-doan-test` admin-only | **VERIFIED** | unauth 401 |
| 5 | `/du-doan` HTML/JS/route unchanged | **VERIFIED** | 200 OK + final-bundle MB 2026-05-02 BT=43 unchanged |
| 6 | `predictions` unchanged | **PARTIAL** | hash changed (+39 rows from natural live activity for 2026-05-03 cycle, NOT mutation by test code). No du_doan_test write paths in main.py. |
| 7 | `final_bundles` unchanged | **PARTIAL** | hash changed (+1 row = MN 2026-05-03 generated by official scheduler last night, NOT by test). |
| 8 | `lottery_results` unchanged | **VERIFIED** (rows=14596, sha=`4acf72d3bda7…` IDENTICAL pre/post) | |
| 9 | `model_daily_eval` unchanged | **VERIFIED** (rows=4014, sha=`bc7a827b642e…` IDENTICAL pre/post) | |
| 10 | scheduler_logs only natural growth | **VERIFIED** | +469 rows from natural shadow/AI scheduler markers, **0 markers** containing `DU-DOAN-TEST` or `du_doan_test` |

Note on #6/#7: They are "PARTIAL" only because rows grew from **legitimate live cycle activity** (MN 2026-05-03 cycle ran last night). The test-lane code did NOT cause those changes. Acceptable per hard-lock rule (no test code touches official tables).

---

## 7. 2026-05-02 MB test output / eval matrix

Actual MB tails 2026-05-02: `["00","04","07","14","21","24","25","32","37","38","41","46","54","57","58","60","62","73","82","83","84","87","91","97"]`. Official MB BT=43 LOSE; lo2=[43,91] PARTIAL (43 missed, 91 hit).

| Experiment | test_bt | official_bt | test_status | official_status | save | break | fp | net | model_count claim | aggregation method | risk_flags |
|---|---|---|---|---|---|---|---|---|---|---|---|
| MB_OFFICIAL_BASELINE_CONTROL | 43 | 43 | LOSE | LOSE | 0 | 0 | 0 | 0 | 25 | clone | [] |
| MB_COMPOSITE_CHALLENGER_V2 | 91 | 43 | WIN | LOSE | 1 | 0 | 0 | +1 | 25 | composite_v2=0.2695;rank=2 | [] |
| MB_TIER_AWARE_BUNDLE_SHADOW_V1 | 91 | 43 | WIN | LOSE | 1 | 0 | 0 | +1 | 25 | tier_aware_adjusted=0.2120;rank=2 | [] |
| MB_AI_CHAIN_PRESERVATION_V1 | 91 | 43 | WIN | LOSE | 1 | 0 | 0 | +1 | 25 | ai_chain_preserve;rank=2;ai_chain=5 | [] |
| MB_PRIOR_REGION_CONTEXT_SAFE_V1 | 91 | 43 | WIN | LOSE | 1 | 0 | 0 | +1 | 25 | prior_region_safe_support;rank=2;tail=91 | [] |
| MB_NO_TOKEN_HERD_REDUCTION_V1 | 91 | 43 | WIN | LOSE | 1 | 0 | 0 | +1 | 25 | no_token_herd_reduction_adjusted=0.1350;rank=2 | [] |
| MB_SPECIALIST_ROSTER_V1 | **null** | 43 | LOSE | LOSE | 0 | 0 | 0 | 0 | 25 | **no_specialist_vote** | [] |

`du_doan_test_bundles.model_count = 25` là số MB predictions hôm đó, **KHÔNG PHẢI** số voter trong candidate ranking (xem §10). Chỉ 14 model voter thực sự góp vào candidate_ranked.

Lo2 status: tất cả PARTIAL vì 91 hit và 43 miss → cả official lo2 [43,91] và test lo2 [91,43] đều có 1 hit.

---

## 8. Why 91 appeared across many experiments — independence audit

Tất cả 7 experiment dùng CHUNG candidate set:

| Experiment | Candidate tails (sorted) | Distinct count | Voter models | Selection basis |
|---|---|---|---|---|
| MB_OFFICIAL_BASELINE_CONTROL | [12, 28, 30, 43, 63, 79, 80, 91] | **8** | 14 | `official_baseline_control` |
| MB_COMPOSITE_CHALLENGER_V2 | [12, 28, 30, 43, 63, 79, 80, 91] | 8 | 14 | `composite_v2=0.2695;rank=2;score=0.075;ai_chain=5;rerun=0;voters=5;prior=True;source_resolved=True` |
| MB_TIER_AWARE_BUNDLE_SHADOW_V1 | [12, 28, 30, 43, 63, 79, 80, 91] | 8 | 14 | `tier_aware_adjusted=0.2120;rank=2;ai_chain=5;rerun=0;voters=5` |
| MB_AI_CHAIN_PRESERVATION_V1 | [12, 28, 30, 43, 63, 79, 80, 91] | 8 | 14 | `ai_chain_preserve;rank=2;ai_chain=5;ai_models=5;score=0.075` |
| MB_SPECIALIST_ROSTER_V1 | [12, 28, 30, 43, 63, 79, 80, 91] | 8 | 14 | `no_specialist_vote` |
| MB_PRIOR_REGION_CONTEXT_SAFE_V1 | [12, 28, 30, 43, 63, 79, 80, 91] | 8 | 14 | `prior_region_safe_support;rank=2;tail=91;ai_chain=5` |
| MB_NO_TOKEN_HERD_REDUCTION_V1 | [12, 28, 30, 43, 63, 79, 80, 91] | 8 | 14 | `no_token_herd_reduction_adjusted=0.1350;rank=2;rerun=0;ai_chain=5` |

**Verdict per method:**

| Experiment | Classification | Why |
|---|---|---|
| MB_OFFICIAL_BASELINE_CONTROL | **VALID_TEST (control)** | Trả lại đúng BT của official, dùng làm baseline |
| MB_COMPOSITE_CHALLENGER_V2 | **SHARED_SOURCE_VARIANT** | Scoring transform riêng nhưng đọc CÙNG candidate_ranked_json |
| MB_TIER_AWARE_BUNDLE_SHADOW_V1 | **SHARED_SOURCE_VARIANT** | KHÔNG thực sự tính source_prize_tier riêng — chỉ adjust score theo prior_tails + ai_chain_votes |
| MB_AI_CHAIN_PRESERVATION_V1 | **SHARED_SOURCE_VARIANT** | Pick top theo ai_chain_votes>=3 từ chung candidate set; method độc lập về **rule chọn**, không độc lập về **input** |
| MB_SPECIALIST_ROSTER_V1 | **PLACEHOLDER (BUG_OR_INCOMPLETE)** | `no_specialist_vote` → `test_bt=null`, vì specialist filter (rate>=0.35 over 60d) loại hết model — method không output gì cho ngày này |
| MB_PRIOR_REGION_CONTEXT_SAFE_V1 | **SHARED_SOURCE_VARIANT** | Đúng là dùng MN(D)+MT(D) prior tails, nhưng filter trên cùng candidate set chứ không re-aggregate raw 25 |
| MB_NO_TOKEN_HERD_REDUCTION_V1 | **SHARED_SOURCE_VARIANT (NOT a true rerun)** | Chỉ adjust score: `+0.012*ai_chain - 0.010*max(0, rerun-ai_chain) - 0.004*max(0, no_token-ai)`. Không thực sự rerun no-token model với herd reduction logic |

Lý do 91 thắng nhiều: candidate `91` là rank #2 với **5 AI-chain voters** (cao thứ 2), score 0.075 (rất gần top1 0.085). Bất kỳ scoring nào cộng AI-chain vote bonus đều đẩy 91 lên top1. Đây là **một tín hiệu thật** (91 thực sự trúng) nhưng các method **không độc lập về input**, nên nếu coi như 5 vote = 5 method → bị nhầm "consensus".

---

## 9. Live parallel status

Classification: **`MANUAL_TEST_LANE` (mức 3/5)**.

| Indicator | Value |
|---|---|
| Engine code exists | YES (`_du_doan_test_mb_engine.py`) |
| Daily runner exists | YES (`_du_doan_test_daily_runner.py`) |
| Daily runner imported by scheduler.py | **NO** (grep empty) |
| Scheduler marker `[DU-DOAN-TEST-MB-REALTIME]` | **0 lifetime** |
| Scheduler marker `[DU-DOAN-TEST-MB-EVAL]` | **0 lifetime** |
| `mb_experimental_preview_shadow` rows for 2026-05-03 | **0** |
| `du_doan_test_runs` for 2026-05-03 | **0** |
| `du_doan_test_runs` for 2026-05-02 | 7 (manual run V46 evening 2026-05-02 22:30) |
| `du_doan_test_runs` lifetime distinct dates | **1** |
| Idempotency UNIQUE constraint | YES — `UNIQUE(run_date, region, experiment_name, run_label)` in CREATE TABLE; manual re-run is safe |
| Audit log lifetime | 1 row only |

Reading: chỉ chạy 1 lần thủ công cho 2026-05-02. Hôm nay 2026-05-03 cần chạy thủ công sau 18:30 (sau MB scrape).

---

## 10. Schema + column gap audit

7-category coverage of the 6 test tables:

| Category | Required columns | Present | Missing |
|---|---|---|---|
| A. Identity (run_id/run_date/region/experiment_name/run_label/code_version/config_hash) | 14 in runs | 14 | 0 |
| B. Safety (test_only/admin_only/official_output/output_impact/owner_approved/does_not_write_final_bundles) | 5 in runs+bundles | 5 each | `does_not_write_final_bundles` (column not declared as separate; logically enforced by code; not strict per-row) |
| C. Mode (mode/realtime_available/diagnostic_only/source_table/source_date) | mode + flags partial | mode ✓; `realtime_available`/`diagnostic_only` columns không tồn tại — chỉ có `is_realtime_available` ở candidates table | 2 columns missing |
| D. Candidate (model_name/family/run_source/tail/rank/output_task/strength/strength_bin/verdict/rule_tier/source_prize_tier/prompt_variant/selection_basis) | 12 declared | 12 | 0 (basic set complete; `strength`/`strength_bin`/`verdict`/`rule_tier` exist but **always NULL** in current rows because engine doesn't populate; `source_prize_tier` exists but is `","-joined` raw prize ID list, not tier classification) |
| E. Evaluation (actual/official_*_status/test_*_status/would_save/would_break/false_promotion/net_effect) | 9 | 9 | 0 |
| F. Model contribution (helped/hurt/unique_signal/duplicate/herd/dropped_hit/wrong_boost/latency_sec/value_score) | 13 | 13 | 0 (column exists; `latency_sec` always NULL because no per-model timing instrumented) |
| G. Audit (timestamp/action/source_hash_before/source_hash_after/changed_tables/official_tables_touched/output_impact/rollback_ref) | 7 | 7 | 0 (only 1 row lifetime — V46 manual run; daily runner does NOT write audit log entries currently) |

Column DDL: 100% complete per schema spec. **Population gaps** (NULL or stub data):
- `du_doan_test_candidates.strength` — always NULL (engine doesn't compute per-candidate strength bin)
- `du_doan_test_candidates.strength_bin` — always NULL
- `du_doan_test_candidates.verdict` — always NULL
- `du_doan_test_candidates.is_test_prompt` — always 0 (no test prompt)
- `du_doan_test_candidates.is_realtime_available` — always 1 (assumed, never measured)
- `du_doan_test_candidates.latency_sec` — always NULL
- `du_doan_test_candidates.cost_estimate` — always NULL
- `du_doan_test_model_contribution.latency_sec` — always NULL
- `du_doan_test_audit_log` — only 1 row (manual V46 run); daily runner doesn't append

---

## 11. Lane separation matrix

| Lane | Input source | Output table | Timing | Official impact | Status |
|---|---|---|---|---|---|
| Official AI output (8 model) | `predictions.run_source IN (auto_daily, ai_chain, rerun_post_*)` | `final_bundles` (output_eligible) | Theo cron 04:15/16:42/17:42 | YES | LIVE production |
| Official no-token output (7 model) | `predictions.run_source = auto_daily` | `final_bundles` (output_eligible) | 04:00 cùng AI | YES | LIVE production |
| Shadow auto-eval (10 model) | `predictions.run_source = shadow_auto_eval` | `shadow_results` + `shadow_candidates` | Sau token batch xong | NO | LIVE shadow, output_eligible=0 |
| Cohere rerank measurement | `cohere_rerank_log` | `cohere_effectiveness_daily` + `cohere_rerank_effectiveness_v1` shadow method | Per closeout | NO | LIVE shadow, output_eligible=0 |
| P0/P0.5/P0.7/P0.8 portfolio (18 method) | `predictions` + `final_bundles` | `shadow_results` + `shadow_method_scoreboard` | Per closeout | NO | LIVE shadow, all output_eligible=0 |
| **MB experimental preview shadow** (1 mat) | `final_bundles.MB.source_predictions_json` + `model_daily_eval` + prior MN/MT | `mb_experimental_preview_shadow` | **MANUAL only** | NO | 1 day persisted |
| **MB test engine (`du_doan_test_*`)** | `mb_experimental_preview_shadow` rows | `du_doan_test_runs/bundles/results/candidates/contribution/audit` | **MANUAL only** | NO | 1 day persisted (2026-05-02) |
| Tier-2 replay shadow | `final_bundles` + `predictions` | `tier2_replay_shadow` 180r, `tier2_replay_v2_shadow` 540r | manual backfill | NO | LIVE (V37) but DROP_AS_DESIGNED |
| Single-vote rescue replay (LEAKY) | various | `single_vote_rescue_replay_shadow` 540r | manual backfill | NO | **LEAKY_REFERENCE_ONLY** — không dùng |
| Corrected rescue replay | `final_bundles` + `predictions` D-1 + prior regions | `corrected_rescue_replay_shadow` 900r | manual backfill | NO | LIVE; TIER 3 gate not met |
| Strength calibration replay | strength bin × family × region | `strength_skip_calibration_replay_shadow` 865r | manual backfill | NO | RESEARCH_DIAGNOSTIC |
| MB structural drilldown | per friday/weekday | `mb_structural_drilldown_shadow` 62r | manual backfill | NO | LIVE shadow |
| Full model capability tensor | `predictions` × `model_daily_eval` × prediction_trace | `artifacts/_full_model_capability_tensor_*.csv` | manual snapshot | NO | DIAGNOSTIC artifact only |

→ **Kết luận**: 13 lane phân biệt rõ. Test lane chỉ ghi `du_doan_test_*` + `mb_experimental_preview_shadow`. Không lane nào ghi `final_bundles` ngoài official.

---

## 12. 25-model usage audit

Production MB 2026-05-02 = **25 distinct models** predicted MB:

| Model | run_source | Used in test contribution? |
|---|---|---|
| claude-opus-4-20250514 | ai_chain | YES |
| claude-sonnet-4-6 | ai_chain | YES |
| combo-no-token | rerun_post_mt | YES |
| combo-super | ai_chain | YES |
| deepseek-reasoner | ai_chain | YES |
| **deepseek-v4-flash** | shadow_auto_eval | **NO** |
| **deepseek-v4-pro** | shadow_auto_eval | **NO** |
| **gemini-2.5-flash** | ai_chain | **NO** |
| gemini-2.5-pro | ai_chain | YES |
| **glm-5.1** | shadow_auto_eval | **NO** |
| gpt-5-mini | ai_chain | YES |
| gpt-5.4 | ai_chain | YES |
| **gpt-5.5** | shadow_auto_eval | **NO** |
| **gpt-oss-120b** | shadow_auto_eval | **NO** |
| **grok-4.20-multi-agent** | shadow_auto_eval | **NO** |
| **kimi-k2.5** | shadow_auto_eval | **NO** |
| lstm | rerun_post_mt | YES |
| meta-learning | rerun_post_mt | YES |
| **qwen3-coder** | shadow_auto_eval | **NO** |
| **qwen3-max-thinking** | shadow_auto_eval | **NO** |
| **qwen3.6-plus** | shadow_auto_eval | **NO** |
| random-forest | rerun_post_mt | YES |
| smart-ensemble | rerun_post_mt | YES |
| smart-ml | rerun_post_mt | YES |
| xgboost | rerun_post_mt | YES |

| Status | Count |
|---|---|
| `USED_IN_TEST_REALTIME` (output-eligible 14) | 14 |
| `MISSING_FROM_TEST` (shadow_auto_eval 11) | 11 |
| `TENSOR_ONLY` | 25 (all models có trong `_full_model_capability_tensor_20260503.csv`) |
| `NO_LATENCY` | 25 (no per-model duration in test layer) |

**Verdict**: ✗ Không phải "25 model thực sự đã chạy realtime test". Đúng là "25 model đã chạy MB predictions hôm đó, 14 model là voter của final_bundles candidate ranking, 11 shadow model chỉ có trong shadow_results không vào candidate set của final bundle nên test engine không thấy".

---

## 13. AI test prompt execution status

| Check | Value |
|---|---|
| `du_doan_test_ai_predictions` table | **DOES NOT EXIST** |
| `du_doan_test_candidates.is_test_prompt=1` rows | **0 lifetime** |
| `prompt_variant` distribution | 100% = `production_prompt_clone_or_none` (147/147 rows) |
| Test prompt config file | **does not exist** |

**Status**: `DESIGNED_ONLY`. AI test prompt **CHƯA EXECUTE**.

Đề xuất Phase AI-1 (chỉ là design, chờ owner OK):
- Tạo `du_doan_test_ai_predictions` schema (admin_only, official_output=false).
- Clone production prompt → `web/backend/prompts/du_doan_test_mb_prompt_v1.txt` với marker test only.
- CLI runner `--mode test_ai_prompt` chạy MB-only sau khi MT closeout, gọi 1-2 AI model với prompt clone, ghi vào `du_doan_test_ai_predictions` + `du_doan_test_candidates.is_test_prompt=1`.
- Compare với production AI rows side-by-side.
- Hard lock: không ghi production `predictions`, không ghi `final_bundles`.

---

## 14. No-token clone + herd-reduction audit

`MB_NO_TOKEN_HERD_REDUCTION_V1` thực tế:

```python
# from _materialize_mb_experimental_preview_shadow.py
def _choose_no_token_herd_reduction(candidates):
    for c in candidates:
        adjusted = c["score"]
        adjusted += 0.012 * c["ai_chain_votes"]
        adjusted -= 0.010 * max(0, c["rerun_post_mt_votes"] - c["ai_chain_votes"])
        adjusted -= 0.004 * max(0, c["no_token_votes"] - c["ai_model_votes"])
        ...
```

**Không thực sự rerun no-token model với cơ chế herd reduction.** Chỉ adjust score trên cùng `candidate_ranked_json`. Penalty cho candidate có nhiều no-token vote hơn AI vote (`-0.004*max(0, no_token-ai)`) → đây là transform, không phải rerun.

`du_doan_test_candidates` 2026-05-02 MB:
- 7 NO_TOKEN model × 11 rows = 77 rows (combo-no-token + lstm + meta-learning + random-forest + smart-ensemble + smart-ml + xgboost)
- 7 AI model × 10 rows = 70 rows
- `is_cloned_from_production=1` cho 100% rows (cloned from preview ranked)
- Không có herd-metric column populated

**Verdict**: clone từ production preview, transform score, không re-run no-token.

---

## 15. Prior-region safe audit

`MB_PRIOR_REGION_CONTEXT_SAFE_V1` code:

```python
def _choose_prior_region(candidates, prior):
    prior_tails = set(prior["MN"]["tails"]) | set(prior["MT"]["tails"])
    hits = [c for c in candidates if c["number"] in prior_tails]
    if not hits:
        return None, "no_prior_region_tail_support"
    ...
```

Prior context build:

```python
def _prior_context(cur, date):
    ctx = {}
    for region in ("MN", "MT"):
        tails = sorted(_actual_tails(cur, date, region))  # actual MN(D) + MT(D)
        ctx[region] = {"tail_count": len(tails), "tails": tails}
    return ctx
```

**Leakage check**:
- ✅ Dùng MN(D) và MT(D) actual tails — đây là **live-available** sau MN/MT scrape (16:30/17:30 VN), trước MB scrape (18:30 VN). KHÔNG leak từ MB(D) actual.
- ✅ KHÔNG dùng `lottery_results` của MB target date.
- ⚠ Caveat: nếu chạy `materialize_for(date)` SAU 18:30 (sau MB closeout), prior tails KHÔNG đổi (chỉ MN+MT) → không leak. Nhưng `_actual_tails` cũng dùng cho MB target để tính `actual_tail_set` cho status — đó là dùng cho **scoring/eval**, không phải selection. ✓ Selection vs eval phân tách đúng.

`source_basis` cho 2026-05-02 chứng minh: `prior_region_safe_support;rank=2;tail=91;ai_chain=5` — chọn 91 vì 91 nằm trong prior tails (`MN={28,71,73,86,...}` hoặc `MT={43,02,88,...}` trong day predecessor logic). Cần kiểm 91 có thực sự xuất hiện trong MN(D) + MT(D) không. Để xác nhận ở next manual run.

**Verdict**: NO_LEAKAGE_DETECTED. Method dùng input live-available đúng nguyên tắc.

---

## 16. Tier-aware + AI-chain preservation audit

`MB_TIER_AWARE_BUNDLE_SHADOW_V1`:

```python
def _choose_tier_aware(candidates, prior):
    for c in candidates:
        adjusted = c["score"]
        adjusted += 0.015 * c["ai_chain_votes"]
        adjusted += 0.008 * c["ai_model_votes"]
        adjusted += 0.010 if c["voter_count"] >= 5 else 0
        adjusted += 0.012 if c["number"] in prior_tails else 0
        adjusted -= 0.006 * max(0, c["rerun_post_mt_votes"] - c["ai_chain_votes"])
```

**Không thực sự tính source_prize_tier.** Tên method "tier_aware" gây hiểu nhầm: code chỉ adjust score theo `ai_chain_votes`, `ai_model_votes`, `voter_count`, `prior_tails`, không có G1/G2/...G7/GDB tier weighting. `source_prize_tier` field trong candidates đang lưu chuỗi `","-joined raw prize ID` (vd `"DB,1,5,7"` từ `source_prizes_json`) chứ không phải tier classification.

`MB_AI_CHAIN_PRESERVATION_V1`:

```python
def _choose_ai_chain(candidates):
    qualified = [c for c in candidates if c["ai_chain_votes"] >= 3]
    if not qualified:
        qualified = [c for c in candidates if c["ai_model_votes"] >= 3]
    qualified.sort(key=lambda c: (-c["ai_chain_votes"], -c["ai_model_votes"], -c["score"], c["rank"]))
    return c["number"], ...
```

**Genuine preservation logic**: chọn candidate có >=3 AI chain voter, sort theo ai_chain_votes desc. Đây là method preserve AI signal hợp lý. Trong 2026-05-02 candidate `91` có 5 AI chain voters → top1 → method chọn 91. ✓

`correct_but_dropped` / `helped_test`: nhìn `du_doan_test_model_contribution`:
- 5 voter của `91` đều có `helped_test=1` (vì 91 = test_bt và 91 trúng).
- 5 voter của `43` đều có `hurt_test=1` (vì 43 = baseline và 43 không trúng).
- `helped_vs_official=1` cho voter của 91 vì test BT khác official BT.
- `dropped_hit=1` cho voter của candidate trúng nhưng KHÁC official (chứng tỏ có evidence là model mạnh bị bỏ).

**Verdict**: AI-chain preservation = genuine. Tier-aware = misnamed transform.

---

## 17. Model capability tensor quality

`artifacts/_full_model_capability_tensor_20260503.csv`: **3217 rows** (3216 data + 1 header).

Cột chính: model, region, weekday, station, run_source, output_type, prompt fields, rule fields, source_prize fields, latency, provider/status.

Quality:
- Date coverage: dài 30+ ngày
- Region coverage: MN/MT/MB
- Weekday: 7/7
- Model: 25+
- **Latency**: phần lớn rows = `NO_PER_MODEL_DURATION` (chỉ có cascade-stage duration tổng, không phải per-model duration). Bị block ở step instrumentation.
- Cost: NULL
- Provider: phần lớn = unknown trừ AI model

**Đủ cho diagnostics?** YES (model strength × region × weekday × run_source).
**Đủ cho pruning?** **NO** — thiếu per-model latency và cost.

---

## 18. MB recovery 6→12 scoreboard

| Scope | Source | Days |
|---|---|---|
| Persisted rows in `mb_experimental_preview_shadow` | 1 (2026-05-02 only) |
| Persisted rows in `du_doan_test_bundles` | 1 (2026-05-02 only) |
| 30-day backtest in API response | **HARDCODED** (from `artifacts/_mb_experimental_backtest_20260503_002427.md`) |

Lifetime persisted scoreboard:

| Experiment | Days | Test wins | Save | Break | FP | Net |
|---|---|---|---|---|---|---|
| MB_AI_CHAIN_PRESERVATION_V1 | 1 | 1 | 1 | 0 | 0 | +1 |
| MB_COMPOSITE_CHALLENGER_V2 | 1 | 1 | 1 | 0 | 0 | +1 |
| MB_NO_TOKEN_HERD_REDUCTION_V1 | 1 | 1 | 1 | 0 | 0 | +1 |
| MB_PRIOR_REGION_CONTEXT_SAFE_V1 | 1 | 1 | 1 | 0 | 0 | +1 |
| MB_TIER_AWARE_BUNDLE_SHADOW_V1 | 1 | 1 | 1 | 0 | 0 | +1 |
| MB_OFFICIAL_BASELINE_CONTROL | 1 | 0 | 0 | 0 | 0 | 0 |
| MB_SPECIALIST_ROSTER_V1 | 1 | 0 (null) | 0 | 0 | 0 | 0 |

Hardcoded API 30-day backtest (cited):
- official baseline: 5/30 BT win
- composite challenger: 8/30 BT win, +5 save / -2 break, false_promotion=2
- AI chain preservation: 9/30 BT win
- target gate: ≥+4 net BT lift / 30 days
- composite is +3 (close but below)
- AI chain is +4 (gate met) but has false-promotion risk

**Verdict**: `BELOW_GATE` for persisted live-parallel evidence (1 day not enough). `APPROACHING_GATE` based on artifact backtest (but artifact ≠ live-parallel writes — separate evidence stream). Need 14+ live manual closeouts before owner-review-ready.

---

## 19. UI completeness matrix

| Item | Status | Note |
|---|---|---|
| Official MB current output | **PRESENT** | left column hero card |
| Test MB current output | **PRESENT** | right column gold/amber |
| Per-axis BT/lo2/lo3/xien2/xien3 | **PRESENT** (V48.1) | row-aligned grid |
| Status badge per axis (Trúng/Trượt/Phụ/Chờ) | **PRESENT** | verify-badge component |
| Diff chip GIỐNG / KHÁC vs official | **PRESENT** | axis-diff-chip per test card |
| Experiment list with chip | **PRESENT** | 7 cards Would Save/Break/PRIMARY |
| Current status: pending/evaluated | **PARTIAL** | hiển thị qua status badge, nhưng không có top-level "PENDING"/"EVALUATED" row label |
| 30-day backtest | **PRESENT but HARDCODED** | from artifact, not from persisted rows |
| Best Shadow Today | **PRESENT** (auto-pick logic by priority) | |
| Test history | **PRESENT** | du_doan_test_bundles JOIN results |
| Mode label realtime vs diagnostic | **PARTIAL** | mode field stored as `REALTIME_AVAILABLE_ONLY` but UI doesn't surface |
| Admin-only warning | **PRESENT** | "Test Lane" badge + footer "không ảnh hưởng /du-doan" |
| official_output=false warning | **PRESENT** | footer-note section |
| No-leakage badge per experiment | **MISSING** | không hiển thị từng method có leakage_audit hay không |
| Fallback date explanation | **PRESENT** | banner "Đang hiển thị ngày test mới nhất ..." |
| 91 independence explanation | **MISSING** | UI không note "7 methods share candidate set" |
| Model contribution detail | **PARTIAL** | candidate ranked table có voters list nhưng không có helped/hurt counters trên UI |
| Would_save/break/false_promotion per experiment | **PARTIAL** | chỉ có chip "Would Save"/"Would Break", không có số FP |
| AI prompt status (designed vs running) | **MISSING** | |
| Loz diagnostics | **MISSING** | |
| MB recovery scoreboard panel | **PARTIAL** | có 30-day snapshot nhưng không có rolling 7/14 từ persisted rows |

→ **Verdict**: 11/20 PRESENT, 6/20 PARTIAL, 3/20 MISSING.

---

## 20. Daily runner status

File `web/backend/_du_doan_test_daily_runner.py`:

✅ Implemented:
- `--date YYYY-MM-DD`
- `--dry-run`
- `--json`
- Idempotent (skip via UNIQUE constraint in test tables)
- Writes only `mb_experimental_preview_shadow` + `du_doan_test_*`

❌ Missing:
- `--region MB` (hardcoded to MB only — fine for now)
- `--mode realtime` / `--mode evaluate` separation (chỉ có 1 mode = REALTIME_AVAILABLE_ONLY)
- Source-hash guard before/after (không có pre/post hash logging)
- `[DU-DOAN-TEST-MB-REALTIME]` / `[DU-DOAN-TEST-MB-EVAL]` markers
- Audit log entry (chỉ engine ghi 1 row lifetime, runner KHÔNG ghi)
- Auto-wire scheduler.py integration

**Hôm nay manual command** (sau MB closeout ~18:30 VN):
```bash
ssh root@14.225.224.89 "cd /root/Lottery_AI_Test && /root/Lottery_AI_Test/venv/bin/python3 web/backend/_du_doan_test_daily_runner.py --date 2026-05-03 --dry-run --json"
ssh root@14.225.224.89 "cd /root/Lottery_AI_Test && /root/Lottery_AI_Test/venv/bin/python3 web/backend/_du_doan_test_daily_runner.py --date 2026-05-03 --json"
```

---

## 21. Today 2026-05-03 live + test timeline

| Time (VN) | Stage | Action | Test lane action |
|---|---|---|---|
| ~21:24 (yesterday) | MN AI cascade for today | DONE last night ✓ | none |
| ~21:33 (yesterday) | MN shadow_auto_eval done | DONE ✓ | none |
| Now (10:14) | MN bundle ready, waiting for MN draw | observed ✓ | none — không thể chạy MB test khi chưa có MB bundle |
| 16:30 | MN scrape (lottery_results MN 2026-05-03) | watch | none |
| ~16:42 | MT AI cascade fires | watch | none |
| 17:30 | MT scrape | watch | none |
| ~17:42 | MB AI cascade fires | watch | none |
| ~18:00 | MB final_bundle generated | watch | **after this** test runner can fire (MB official input ready) |
| 18:30 | MB scrape (lottery_results MB) | watch | **realtime mode** test runner fires ngay sau khi có MB final_bundle, **trước** khi có actual_known |
| 19:00–22:00 | post-closeout materializers | watch | **eval mode** runner re-runs sau khi có lottery_results MB → cập nhật test_bt_status, would_save/break |

Hôm nay vì là Stage 0 manual: **owner approve em chạy thủ công 1-2 lần** (không auto-wire). Em báo trước khi chạy.

---

## 22. Source hash proof

| Table | Pre (10:20) | Post (10:30) | Drift |
|---|---|---|---|
| predictions | 4098 / `130e5e5de858…` | 4098 / `130e5e5de858…` | **IDENTICAL** ✓ |
| final_bundles | 193 / `443251d22f73…` | 193 / `443251d22f73…` | **IDENTICAL** ✓ |
| lottery_results | 14596 / `4acf72d3bda7…` | 14596 / `4acf72d3bda7…` | **IDENTICAL** ✓ |
| model_daily_eval | 4014 / `bc7a827b642e…` | 4014 / `bc7a827b642e…` | **IDENTICAL** ✓ |
| scheduler_logs | 112612 / `ee4b0a6bcede…` | 112612 / `ee4b0a6bcede…` | **IDENTICAL** ✓ |
| du_doan_test_runs | 7 / `e9ca079d832a…` | identical | ✓ |
| du_doan_test_candidates | 147 / `15da774080ca…` | identical | ✓ |
| du_doan_test_bundles | 7 / `45d2dbf9e810…` | identical | ✓ |
| du_doan_test_results | 7 / `cd813f60efaf…` | identical | ✓ |
| du_doan_test_model_contribution | 147 / `66ea29f64e86…` | identical | ✓ |
| du_doan_test_audit_log | 1 / `13c6de2a3612…` | identical | ✓ |
| mb_experimental_preview_shadow | 7 / `4d597130d8b5…` | identical | ✓ |

**12/12 IDENTICAL pre/post audit. ZERO write impact from this control pass.**

---

## 23. What is fully done

- Route + API + UI + admin gate
- 6 `du_doan_test_*` tables with declared schema
- Manual engine + manual runner
- 1 manual run (2026-05-02 MB)
- V48 + V48.1 UI: 5-axis side-by-side comparison + independent test lo3 (frequency_co_occurrence_with_test_bt)
- Hard locks: 7/7 runs and 7/7 bundles có test_only=1, admin_only=1, official_output='false', output_impact='false', owner_approved=0
- Source hash guard
- Idempotency UNIQUE constraints in 6 test tables

---

## 24. What is partial

- 25-model usage: 14/25 voter coverage (11 shadow_auto_eval missing in test contribution — **structural** vì final_bundles không lấy shadow voter)
- Method independence: 5 method là scoring transform trên cùng candidate set, không phải pipeline độc lập
- 30-day backtest: số đẹp nhưng artifact-based, không phải persisted shadow rows
- UI: 11/20 PRESENT, 6/20 PARTIAL
- Daily runner: thiếu mode separation, marker logging, audit log append, hash guard

---

## 25. What is missing

- AI test prompt execution (`du_doan_test_ai_predictions` table không tồn tại; 0 row `is_test_prompt=1`)
- Direct raw-25 candidate ingestion (test engine chỉ đọc preview ranked, không re-aggregate raw 25 predictions)
- Method scoreboard table (cho từng method × ngày × region)
- Latency daily table (per-model latency)
- Leakage audit table (per-experiment leakage flags)
- Loz diagnostic panel
- Realtime vs Diagnostic mode separation
- Scheduler auto-wire markers
- Specialist roster method bị placeholder (test_bt=null)
- Tier-aware method misnamed (không thực sự tính tier)
- Cost / latency / value-score columns đều NULL trong contribution

---

## 26. What to do next 24h (manual, owner-approve trước)

1. Sau MB scrape (~18:30 VN hôm nay), em chạy thủ công:
   - `_du_doan_test_daily_runner.py --date 2026-05-03 --dry-run --json` (preview)
   - `_du_doan_test_daily_runner.py --date 2026-05-03 --json` (live write to test tables)
2. Verify pre/post hash identical for OFFICIAL tables.
3. Update `du_doan_test_audit_log` with manual run entry (em add code support trong runner).
4. Re-fetch `/du-doan-test` UI verify hôm nay 2026-05-03 hiển thị 7 experiment cho MB.

---

## 27. What to wait 7-14 days

- Cần ≥7 ngày persisted shadow rows trước khi tin số rolling-7 trong UI scoreboard.
- Cần ≥14 ngày trước khi đề xuất scheduler auto-wire (CP-1.4 active roadmap).
- Cần ≥30 ngày persisted trước khi đề xuất bất kỳ thay đổi nào lên `/du-doan` official.

---

## 28. What remains owner-lock

- Scheduler auto-wire: vẫn chờ ≥3-5 manual run sạch.
- Production prompt thay đổi: hard-locked.
- Production model roster (8 AI + 7 NO_TOKEN): hard-locked.
- Bundle voting: hard-locked.
- Lane weights: hard-locked.
- Output policy: hard-locked.
- AI test prompt deploy: chờ owner OK trước khi tạo `du_doan_test_ai_predictions`.

---

## 29. Risk register

| Risk | Severity | Mitigation |
|---|---|---|
| Test mistaken as official | HIGH | unauth 401, "Test Lane" badge, footer note, nav chip hidden cho non-admin |
| 25-model overclaim | MEDIUM | this report explicitly clarifies 14 voter / 25 prediction |
| 91 false-consensus across methods | MEDIUM | this report classifies SHARED_SOURCE_VARIANT, không tính 5 method = 5 confirm |
| Tier-aware misnamed | LOW | dùng tên cẩn thận khi báo cáo; refactor future |
| Specialist roster placeholder | LOW | chấp nhận null cho ngày không đủ specialist; UI hiển thị "no_specialist_vote" |
| Daily runner thiếu hash guard | MEDIUM | trước khi auto-wire phải bổ sung |
| AI prompt designed-only | LOW | rõ ràng documented, không claim đang chạy |
| Persisted scoreboard chỉ 1 ngày | HIGH | không base decision trên 1 ngày; gate yêu cầu 14+ ngày |

---

## 30. Rollback plan

Nếu có sự cố:
1. Xóa các route `/du-doan-test`, `/api/du-doan-test/mb` trong main.py.
2. `DROP TABLE du_doan_test_*` (tất cả 6 bảng).
3. Xóa `mb_experimental_preview_shadow` (1 bảng).
4. Xóa file engine/runner/materializer trong `web/backend/`.
5. Frontend: xóa `du-doan-test.html` và link `duDoanTestLink` trong `du-doan.html`.
6. Restart `lottery.service`.
7. Verify `/du-doan` 200, source hashes identical.

`final_bundles`, `predictions`, `lottery_results`, `model_daily_eval`, scoring, voting, lane weights, prompt, model roster đều **không bị tác động** → rollback chỉ cần 5 phút.

---

## 31. Docs / tracker / changelog sync

Sẽ cập nhật ngay phần tiếp theo của session:
- `CHANGELOG.md` → V20.3.37.48.2 (TOTAL-FORCE START-OF-LIVE pass)
- `docs/CURRENT_TRUTH_SSOT.md` → row mới
- `docs/FOLLOW_UP_TRACKER.md` → 9 FU mới
- `docs/CHANGELOG_GOVERNANCE_LEDGER.md` → governance entry
- `docs/ACTIVE_ROADMAP_CROSS_REGION_LEAKAGE.md` → reference link

---

## 32. Technical no-drop audit

| Item | Drop? |
|---|---|
| VPS sync done | ✓ NO |
| Pre-hash captured (5+6+6 tables) | ✓ NO |
| Post-hash captured | ✓ NO |
| 12/12 hash IDENTICAL verified | ✓ NO |
| 7 experiment evaluated | ✓ NO |
| 91 independence explained | ✓ NO |
| 25-model corrected (14 voter) | ✓ NO |
| AI prompt status corrected (DESIGNED_ONLY) | ✓ NO |
| Live parallel classified MANUAL | ✓ NO |
| Schema gap audit | ✓ NO |
| Lane separation 13-row matrix | ✓ NO |
| UI matrix 20-item | ✓ NO |
| Today timeline | ✓ NO |
| Risk register | ✓ NO |
| Rollback plan | ✓ NO |

---

## 33. Governance no-overclaim audit

| Statement | OK? |
|---|---|
| "Đã có route + UI + schema" | ✓ |
| "Đã chạy auto live song song" | **❌** không claim — pass classified MANUAL |
| "Đã 25 model thực sự realtime test" | **❌** không claim — corrected 14/25 |
| "Đã chạy AI test prompt" | **❌** không claim — DESIGNED_ONLY |
| "Composite challenger 8/30 BT wins là live evidence" | **❌** không claim — clarified hardcoded backtest |
| "7 experiment fully independent pipelines" | **❌** không claim — SHARED_SOURCE_VARIANT |
| "Tier-aware tính tier thật" | **❌** không claim — misnamed transform |
| "Source hash 4/4 unchanged" | ✓ verified for 4 tables that should not change; predictions/final_bundles changed naturally and correctly attributed to live activity not test code |
| "Output mutation = false" | ✓ verified |
| "/du-doan unaffected" | ✓ verified |

→ Pass đạt yêu cầu **VERIFY-BEFORE-CLAIM** + **NO PASS-WASH**.
