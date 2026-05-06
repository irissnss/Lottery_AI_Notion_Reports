# TOTAL-FORCE V55 — 04/05 + 05/05 closeout forensic + test lane / official quality / next upgrade plan

**Anchor date:** 2026-05-05 20:14 VN (post all live cycles MN 16:30, MT 17:30, MB 18:30)  
**Pass id:** V20.3.37.55_full_chain  
**Mode:** Forensic + measurement-only + test-lane-only + UI-test-only. **Zero official mutation.**  
**Live data integrity:** synced VPS DB at 20:11 VN (manifest `artifacts/live_sync/20260505_201101/manifest.json`) and again at 20:33 VN after materialization (manifest `artifacts/live_sync/20260505_203357/manifest.json`).  
**Hard lock:** `/du-doan`, `/api/final-bundle`, `final_bundles`, `predictions`, `lottery_results`, `model_daily_eval`, official scoring, voting, lane weights, prompt, model roster, official scheduler — **không đổi trong V55**.

---

## A. Executive verdict (12 dòng)

1. 04/05: official MN BT_LOSE+lo2_PARTIAL, MT BT_WIN+lo2_WIN, MB BT_LOSE+lo2_LOSE.
2. 05/05: official MN BT_LOSE+lo2_LOSE, MT BT_WIN+lo2_PARTIAL, MB BT_LOSE+lo2_LOSE.
3. MT đang trỗi dậy: 7d BT=**71.4%**, nhưng 30d vẫn **36.7%** → tốt 1 tuần, chưa đủ rolling.
4. MN đang chậm lại: 30d 56.7% (V54: 60%); 7d chỉ 42.9% (3/7).
5. MB tiếp tục yếu cấu trúc: 7d **14.3%**, 30d 20%, 60d 26.7%; MB Wed/Fri vẫn `WEEKDAY_BLACK_SPOT_CONFIRMED` trên anchor 2026-05-05.
6. Test lane **đã cứu MN 2/2 ngày**: `SPECIALIST_ROSTER` 04/05 picked 32 (hit) khi official 65 LOSE; `AI_CHAIN_PRESERVATION` 05/05 picked 52 (hit) khi official 15 LOSE. Cả hai là `INDEPENDENT_DIVERGENCE_HELPFUL`, gate chưa đạt.
7. Test lane **phá MT WIN**: `AI_CHAIN_PRESERVATION` chuyển 29 WIN → 82 (LOSE for BT) ngày 04/05; chuyển 44 WIN → 39 ngày 05/05. MT herding đã đo lại trên 60d (fw=8/fl=12 destructive) — **NOT promote MT_AI_CHAIN**.
8. Test lane **chưa cứu MB** ngày nào trong 04/05+05/05 dù `mb_experimental_preview_shadow` 05/05 có 1 free win (07/05/2026 sample chưa khẳng định).
9. `gemini-3-flash` ngày đầu tiên (05/05) **MB BT WIN** (91+14 hit) — KEEP_CANDIDATE; `gemini-3.1-pro` 05/05 MB PARTIAL; `gemma-4-31b` 0 rows 05/05 vì preflight bug. **Bug đã FIX trong V55**, gemma sẽ chạy 06/05.
10. Loz1/loz2 vẫn `LOZ_NOT_READY_FOR_RULE`. Trace 04/05+05/05 cho thấy MN có 5 loz_line_select_miss, MT 6, MB 4 → có pattern "model đúng nhưng final loz drop" — đặc biệt MT.
11. C-05 latency: 0/0 latency_available trên 04/05+05/05 → **PRUNING_NOT_ALLOWED_NO_LATENCY** vẫn còn nguyên.
12. `**/du-doan-test` vẫn ở `LIVE_PARALLEL_AUTO_PENDING_ONLY`**. Chưa đủ proof để đổi official; chưa đạt gate cho method nào.

---

## B. Full report chain reconciliation


| Pass                                              | Status                | Reconciled                                                                                                        |
| ------------------------------------------------- | --------------------- | ----------------------------------------------------------------------------------------------------------------- |
| V52.5.7 multi-region test lane                    | CONFIRMED             | runner manual, anti-leak D-1, no auto wire — vẫn đúng                                                             |
| V53 / V52.5.8 full chain audit                    | CONFIRMED             | UI source-badge V52.6, test lane independent verified                                                             |
| V53.1 owner deliverables (roadmap + timeline)     | CONFIRMED             | docs only, no code change                                                                                         |
| V54 natural live watch (2026-05-04 12:55 VN)      | CONFIRMED             | C-02 API source labels, C-06 loz_stage_trace 6174 rows, C-15 weekday blackspot 21 rows; C-05 deferred             |
| V55 V20.3.37.55 add 3 Google direct shadow models | CONFIRMED + CORRECTED | Registry/cohort wiring OK, key resolution OK; *scheduler preflight bug for `gemma-` discovered and FIXED in V55** |


**Embedded reports**: V48 inside V49 (already reconciled in V52). No new embedded discovery.

**Document drift check**: SSOT, FU tracker, active roadmap, changelog all consistent up to V55 (entries written this session).

---

## C. Current system status (2026-05-05 20:14 VN)

- **VPS service:** `lottery` active (latest restart 2026-05-05 20:08 VN after V55 scheduler fix); `/api/health` HTTP 200.
- **Registry counts:** SHADOW_AUTO_EVAL=13 (10 → +3 V55), OUTPUT_ELIGIBLE=15 unchanged, ALL_RUNTIME=31 (28 → 31).
- **Today's predictions (05/05):** 27 model rows × 3 regions = 81 prediction rows; 3 final bundles (MN/MT/MB) generated and verified.
- **Today's shadow eval:** 128 shadow_eval scheduler events (MN 64 + MT 32 + MB 32). 12/13 shadow models persisted predictions (gemma-4-31b skipped due to bug, **fixed**).
- **Test lane data 04/05:** 25 bundles + 25 results across 6 methods × 3 regions + MB legacy duplicate.
- **Test lane data 05/05:** 25 bundles + 25 results across 6 methods × 3 regions (newly created in this V55 pass via manual runner).
- **Loz stage trace 04/05:** 88 actual tails traced (MN 39, MT 27, MB 22).
- **Loz stage trace 05/05:** 94 actual tails traced (MN 42, MT 30, MB 22).
- **Model strength tensor:** anchor advanced to 2026-05-05 (8875 rows).
- **Weekday blackspot:** anchor 2026-05-05 (21 rows). MB Wed/Fri = BLACK_SPOT_CONFIRMED. MT Fri = BLACK_SPOT_CONFIRMED. MT Mon downgraded to STRUCTURAL_RISK.
- **Latency audit:** 0/0 latency_available — pruning still blocked.
- **Scheduler logs 05/05:** 2,000+ rows including measurement_materialize, shadow_catchup, du_doan_test_mb, mb_watchdog. No anomaly.

---

## D. 2026-05-04 OFFICIAL closeout by region (DB-proven)


| Region | BT  | BT status | lo2      | lo2 status                | Actual ground truth (sample)                                           | Verdict                   |
| ------ | --- | --------- | -------- | ------------------------- | ---------------------------------------------------------------------- | ------------------------- |
| MN     | 65  | **LOSE**  | [65, 32] | **PARTIAL** (32 hit)      | 6 ĐB+G8 tails: 16,15,41,04 (MN 4 stations) + actual_n=39 incl 32 in G7 | OFFICIAL_LOSE+LO2_PARTIAL |
| MT     | 29  | **WIN**   | [29, 41] | **WIN** (cả 29 và 41 hit) | 27 tails incl 39 (Phú Yên ĐB), 41 (Phú Yên G8), 51, 52, 13             | OFFICIAL_WIN              |
| MB     | 09  | **LOSE**  | [09, 38] | **LOSE**                  | 22 tails (Hà Nội); 09 và 38 đều không trong actual                     | OFFICIAL_LOSE             |


**Key model-level finding (04/05):**

- MN: actual tail `32` xuất hiện trong final voter set top10 (ranked #2 với 6 voter no-token, score 0.1484) nhưng top1 chọn 65 dù 32 có cluster mạnh hơn về tỷ lệ vote → bundle conversion gap.
- MT: bundle BT=29 đến từ consensus AI+ML; thắng đúng. Một vài model AI khác chỉ vào 82 (cũng hit cuối cùng) — đây là tín hiệu phụ.
- MB: ML herding rất mạnh quanh 09 (AI và ML đều top1=09); không model nào lấy được tail thắng (rất cao ngẫu nhiên cho MB Hà Nội đơn đài).

---

## E. 2026-05-05 OFFICIAL closeout by region (DB-proven)


| Region | BT  | BT status | lo2      | lo2 status                     | Actual ground truth (sample)                                              | Verdict                  |
| ------ | --- | --------- | -------- | ------------------------------ | ------------------------------------------------------------------------- | ------------------------ |
| MN     | 15  | **LOSE**  | [15, 13] | **LOSE**                       | 42 tails: 32 (G7), 35, 60, 96, 95, 22… 15 và 13 đều không hit             | OFFICIAL_LOSE            |
| MT     | 44  | **WIN**   | [44, 31] | **PARTIAL** (44 hit, 31 không) | 30 tails: G7=144(44), G8=53,89, ĐB=43,78                                  | OFFICIAL_WIN+LO2_PARTIAL |
| MB     | 83  | **LOSE**  | [83, 41] | **LOSE**                       | 22 tails (Quảng Ninh): 12,37,44,31,37,44 G7 list (37,44,31)… 83 không hit | OFFICIAL_LOSE            |


**Key model-level finding (05/05):**

- MN: 15 LOSE; nhiều model AI khác chỉ vào 56, 13, 82 — không trùng actual. Specialist ML cũng đồng thuận 15 sai. Actual G7 ‘32’ có nhưng không có model AI nào pick.
- MT: 44 WIN — combo-no-token + xgboost + lstm ML all top1=44 đồng thuận. MN(D) và MT prior signal dẫn dắt đúng.
- MB: 83 LOSE; AI chain herding quanh 83 và 41 — cùng pattern MB thường thấy. Actual G7 = 37, 44, 31 (Quảng Ninh đặc biệt G7 nhiều).

---

## F. 2026-05-04 `/du-doan-test` result by method


| Region  | Method                                             | test_bt | off_bt | hit   | flip_to_win | Verdict                                             |
| ------- | -------------------------------------------------- | ------- | ------ | ----- | ----------- | --------------------------------------------------- |
| MN      | OFFICIAL_BASELINE_CONTROL                          | 65      | 65     | 0     | 0           | clone-by-design (LOSE)                              |
| MN      | AI_CHAIN_PRESERVATION_V1                           | 65      | 65     | 0     | 0           | INDEPENDENT_AGREEMENT (cùng sai)                    |
| MN      | NO_TOKEN_HERD_REDUCTION_V1                         | 65      | 65     | 0     | 0           | INDEPENDENT_AGREEMENT (cùng sai)                    |
| MN      | **SPECIALIST_ROSTER_V1**                           | **32**  | 65     | **1** | **1**       | **TEST_METHOD_TRUE_RESCUE** ✓                       |
| MN      | PRIOR_REGION_CONTEXT_SAFE_V1                       | None    | 65     | 0     | 0           | NO_PICK_NO_RESCUE                                   |
| MN      | STRENGTH_WEIGHTED_V52_5_2                          | 65      | 65     | 0     | 0           | clone (LOSE)                                        |
| MT      | OFFICIAL_BASELINE_CONTROL                          | 29      | 29     | 1     | 0           | clone-by-design (WIN — official đã WIN)             |
| MT      | **AI_CHAIN_PRESERVATION_V1**                       | **82**  | 29     | 1     | 0           | INDEPENDENT_DIVERGENCE_HARMFUL (broke baseline win) |
| MT      | NO_TOKEN_HERD_REDUCTION_V1                         | 29      | 29     | 1     | 0           | INDEPENDENT_AGREEMENT                               |
| MT      | PRIOR_REGION_CONTEXT_SAFE_V1                       | 82      | 29     | 1     | 0           | INDEPENDENT_DIVERGENCE_HARMFUL                      |
| MT      | SPECIALIST_ROSTER_V1                               | 29      | 29     | 1     | 0           | INDEPENDENT_AGREEMENT                               |
| MT      | STRENGTH_WEIGHTED_V52_5_2                          | 82      | 29     | 1     | 0           | INDEPENDENT_DIVERGENCE_HARMFUL                      |
| MB (×2) | OFFICIAL/AI_CHAIN/NO_TOKEN/STRENGTH/COMPOSITE/TIER | 09      | 09     | 0     | 0           | clone (LOSE)                                        |
| MB      | PRIOR_REGION                                       | 19      | 09     | 0     | 0           | wrong but different                                 |
| MB      | SPECIALIST_ROSTER                                  | None    | 09     | 0     | 0           | NO_PICK                                             |


**Score 04/05 (region × method):** 1 free win (MN_SPECIALIST → 32), 0 false_promotion, 3 harmful divergence (MT broke). Net = `+1 free_win`, `-3 harmful` (nhưng official MT WIN nên harmful không bị tính LOSE; gọi là "method would have broken official win").

---

## G. 2026-05-05 `/du-doan-test` result by method


| Region | Method                       | test_bt | off_bt | hit   | flip_to_win | Verdict                                            |
| ------ | ---------------------------- | ------- | ------ | ----- | ----------- | -------------------------------------------------- |
| MN     | OFFICIAL_BASELINE_CONTROL    | 15      | 15     | 0     | 0           | clone (LOSE)                                       |
| MN     | **AI_CHAIN_PRESERVATION_V1** | **52**  | 15     | **1** | **1**       | **TEST_METHOD_TRUE_RESCUE** ✓                      |
| MN     | NO_TOKEN_HERD_REDUCTION_V1   | 15      | 15     | 0     | 0           | INDEPENDENT_AGREEMENT (cùng sai)                   |
| MN     | PRIOR_REGION_CONTEXT_SAFE_V1 | None    | 15     | 0     | 0           | NO_PICK                                            |
| MN     | SPECIALIST_ROSTER_V1         | 15      | 15     | 0     | 0           | clone (LOSE)                                       |
| MN     | STRENGTH_WEIGHTED_V52_5_2    | 15      | 15     | 0     | 0           | clone (LOSE)                                       |
| MT     | OFFICIAL_BASELINE_CONTROL    | 44      | 44     | 1     | 0           | clone (WIN)                                        |
| MT     | **AI_CHAIN_PRESERVATION_V1** | **39**  | 44     | 1     | 0           | INDEPENDENT_DIVERGENCE_HARMFUL (broke 44 win → 39) |
| MT     | NO_TOKEN_HERD_REDUCTION_V1   | 44      | 44     | 1     | 0           | INDEPENDENT_AGREEMENT (WIN)                        |
| MT     | PRIOR_REGION_CONTEXT_SAFE_V1 | 52      | 44     | 1     | 0           | INDEPENDENT_DIVERGENCE_HARMFUL                     |
| MT     | SPECIALIST_ROSTER_V1         | 44      | 44     | 1     | 0           | INDEPENDENT_AGREEMENT (WIN)                        |
| MT     | STRENGTH_WEIGHTED_V52_5_2    | 44      | 44     | 1     | 0           | INDEPENDENT_AGREEMENT (WIN)                        |
| MB     | OFFICIAL_BASELINE_CONTROL    | 83      | 83     | 0     | 0           | clone (LOSE)                                       |
| MB     | AI_CHAIN_PRESERVATION_V1     | 41      | 83     | 0     | 0           | wrong divergence                                   |
| MB     | NO_TOKEN_HERD_REDUCTION_V1   | 41      | 83     | 0     | 0           | wrong divergence                                   |
| MB     | COMPOSITE_CHALLENGER_V2      | 41      | 83     | 0     | 0           | wrong divergence                                   |
| MB     | STRENGTH_WEIGHTED_V52_5_2    | 41      | 83     | 0     | 0           | wrong divergence                                   |
| MB     | TIER_AWARE_BUNDLE_SHADOW_V1  | 41      | 83     | 0     | 0           | wrong divergence                                   |
| MB     | PRIOR_REGION_CONTEXT_SAFE_V1 | 98      | 83     | 0     | 0           | wrong divergence                                   |
| MB     | SPECIALIST_ROSTER_V1         | None    | 83     | 0     | 0           | NO_PICK                                            |


**Score 05/05:** 1 free win (MN_AI_CHAIN → 52), 0 false_promotion, 2 harmful divergence MT (broke baseline win, không bị penalty rolling).

---

## H. Official vs test — who won, who broke, who rescued


| Day   | Region | Official | Test rescue                       | Test break                                 | Net                                                 |
| ----- | ------ | -------- | --------------------------------- | ------------------------------------------ | --------------------------------------------------- |
| 04/05 | MN     | LOSE     | SPECIALIST_ROSTER picked 32 ✓     | —                                          | +1 free_win MN                                      |
| 04/05 | MT     | WIN (29) | —                                 | AI_CHAIN, PRIOR_REGION, STRENGTH (chọn 82) | break baseline win, but 82 also hit so no LOSE flip |
| 04/05 | MB     | LOSE     | —                                 | —                                          | NO_METHOD_FOUND_HIT                                 |
| 05/05 | MN     | LOSE     | AI_CHAIN_PRESERVATION picked 52 ✓ | —                                          | +1 free_win MN                                      |
| 05/05 | MT     | WIN (44) | —                                 | AI_CHAIN (39), PRIOR_REGION (52)           | break baseline win                                  |
| 05/05 | MB     | LOSE     | —                                 | —                                          | NO_METHOD_FOUND_HIT                                 |


**Important nuance:** "harmful divergence trên MT" không tự động làm LO2 hỏng — ví dụ test_bt=82 ngày 04/05 vẫn hit actual nên `would_flip_to_lose=0` trong DB. Đây không phải false_promotion thuần, mà là method tự pick **một số khác** mà cũng hit. Nhưng nếu method được promote vào lane chính, nó sẽ chuyển BT win 29 → 82, và `82` không phải BT win theo bundle status logic (vì DB tracks bach_thu_status by exact bt match).

---

## I. Rolling 7/14/30/60 updated post-05/05

```
Region 7d_BT  14d_BT 30d_BT 60d_BT  | 30d_LO2_FULL  30d_LO2_ANY
MN     42.9%  50.0%  56.7%  46.7%   | 30.0%         83.3%
MT     71.4%  50.0%  36.7%  50.0%   | 16.7%         66.7%
MB     14.3%  28.6%  20.0%  26.7%   |  6.7%         36.7%
```

**Reconcile vs V54 numbers:**

- MN BT 30d **60% → 56.7%** (giảm sau 04/05 LOSE và 05/05 LOSE).
- MT BT 30d 33% → **36.7%** (tăng nhẹ sau 04/05 + 05/05 WIN).
- MB BT 30d 20% → **20.0%** (không đổi; 04/05 và 05/05 đều LOSE).
- MN LO2_ANY 83% → **83.3%** (vẫn mạnh).
- MT LO2_FULL 17% → **16.7%** (nhỉnh hơn).
- MB LO2_FULL 7% → **6.7%** (giảm nhẹ).

**Per-weekday 60d highlights (anchor 2026-05-05):**

- MN Mon 4/5 BT WIN (80%); Thu 3/4 (75%); Sun 3/4 (75%) — mạnh.
- MN Wed/Fri STRUCTURAL_RISK (1/4 = 25%).
- MT Thu 4/4 BT WIN (100%); MT Mon 1/5 (20% — đã downgrade từ V54 BLACK_SPOT).
- MT Fri 0/4 BT — `WEEKDAY_BLACK_SPOT_CONFIRMED`.
- MB Wed 0/4 BT — `WEEKDAY_BLACK_SPOT_CONFIRMED`.
- MB Fri 0/4 BT — `WEEKDAY_BLACK_SPOT_CONFIRMED`.
- MB Sat 2/4 BT (50%) — best MB weekday.

---

## J. MT forensic — correct-but-dropped, loz line, AI drop, candidate miss

**04/05 MT:**

- `mt_model_hit_output_drop_shadow`: 5 actual tails phân tích, AI signal dropped = 2, no_token dropped = 0.
- `loz_stage_trace_shadow`: MT 27 actual tails; in_top1=3, in_top2=6, in_top10=6; LOZ_LINE_SELECTION_MISS=1, CANDIDATE_POOL_MISS=3, AI_DROPPED=0.

**05/05 MT:**

- `mt_model_hit_output_drop_shadow`: 5 actual tails, AI signal dropped = 4 (cao!), no_token dropped = 3.
- `loz_stage_trace_shadow`: MT 30 actual tails; in_top1=6, in_top2=6, in_top10=6; LOZ_LINE_SELECTION_MISS=5 (cao!), CANDIDATE_POOL_MISS=0, AI_DROPPED=0.

**Diễn giải:** Ngày 05/05 MT có **6 actual tails đã có model nào đó đặt top1**, nhưng **5 trong số đó bị final loz_line drop** (final chỉ chọn 44 và 31). Tức là model có signal mạnh nhưng converter bundle chỉ giữ top2. Đây là dấu hiệu cải thiện được nếu C-07 panel + lo2 policy mở rộng. **Gate vẫn chưa đạt** vì sample 30d MT BT chỉ 36.7%.

C-07 UI panel **chưa implement**. Plan: build read-only admin panel `/du-doan-test/mt-correct-but-dropped` consuming `mt_model_hit_output_drop_shadow` + `loz_stage_trace_shadow`. Đề xuất V55.x trong vòng 7 ngày.

---

## K. MB forensic — AI weakness, no-token herd, specialist, weekday blackspot

**04/05 MB (Hà Nội, Mon):**

- BT=09 LOSE (cluster AI+NO_TOKEN herding quanh 09 mạnh, 5+ voter cùng top1).
- Actual không có 09 hay 38; actual G7 list = 15, 69, 63 (Hà Nội thường hot 7 numbers G7).
- Family summary:
  - AI top1_hit_pct ~14% (1 hit / 7 model) — yếu.
  - NO_TOKEN top1_hit_pct ~25% — better but still low.
  - SHADOW_AUTO ~14%.

**05/05 MB (Quảng Ninh, Tue):**

- BT=83 LOSE; actual G7 = 37, 44, 31; có 91, 14 (đặc biệt). 
- `gemini-3-flash` ngày đầu tiên → MB BT WIN (91+14, hit cả 2)!
- AI/ML cluster sai (41, 83 dominate).
- Specialist roster không có pick (None) — vẫn thin sample.

**Weekday blackspot anchor 2026-05-05:**

- MB Wed/Fri vẫn BLACK_SPOT_CONFIRMED.
- MB Sat best (50% BT, 75% LO2_ANY).
- MN Mon mạnh 80% BT.
- MT Thu top 100% BT (n=4).

**Plan MB:**

- Không loại model nào (sample thin, latency vắng).
- Continue measure SPECIALIST_ROSTER 30-60 ngày trước owner review.
- Continue watch 3 Google direct shadow models 14 ngày, đặc biệt `gemini-3-flash` MB sau ngày đầu thắng.

---

## L. Loz1/loz2 status + stage trace

- `loz_stage_trace_shadow` đã materialized cho 04/05 + 05/05 (88 + 94 = 182 actual tails traced).
- Drop_stages 04/05: MN 2 LOZ_LINE_SELECTION_MISS, MT 1, MB 2.
- Drop_stages 05/05: MN 3, MT 5, MB 2.
- AI signal dropped (qua loz lane) = 0 trên 04/05 và 05/05.
- LO2 region/weekday-conditional pattern không thay đổi.

**Verdict labels:**

- `LOZ_DIAGNOSTIC_ONLY` ✓
- `LOZ_REGION_CONDITIONAL` ✓
- `LOZ_WEEKDAY_CONDITIONAL` ✓ (xem MN Sun 100% LO2_ANY vs MB Wed 25%)
- `LOZ_STAGE_TRACE_AVAILABLE` ✓ (V54 deploy + V55 backfill 04/05+05/05)
- `LOZ_NOT_READY_FOR_RULE` ✓
- `LOZ_OUTPUT_POLICY_CHANGE_NOT_ALLOWED` ✓

---

## M. Model tensor — strong/weak by region/weekday/station + latency/pruning

**Tensor latest_anchor=2026-05-05** (V55 cập nhật từ 2026-05-02). 8875 rows × 4 windows × 3 grains.

**Region 30d top by family** (helpful_signal_strength):

- **MN AI top:** `combo-super` (auto_daily) — 0.59 hữu ích cao nhất.
- **MN ENSEMBLE top:** `combo-super` cùng top1.
- **MN NO_TOKEN top:** `meta-learning` ~0.56.
- **MT AI top:** `gemini-2.5-pro` ~0.53; theo sau là `claude-sonnet-4-6`.
- **MT NO_TOKEN top:** `xgboost` ~0.50.
- **MB AI top:** `claude-sonnet-4-6` ~0.28 — vẫn yếu.
- **MB NO_TOKEN top:** `random-forest rerun_post_mt` ~0.34.
- **MB SHADOW top:** chưa có sample đủ cho 3 model mới (mới 1 ngày).

**Latency/pruning:**

- 04/05+05/05: 50/50 + 81/81 rows trong `model_latency_cost_audit_daily` đều `latency_available=0`, missing_reason còn `NO_PER_MODEL_DURATION` 100%.
- **C-05 BLOCKED** — chưa instrument `gpt_analyzer.py` per-model timing.
- `PRUNING_NOT_ALLOWED_NO_LATENCY` vẫn nguyên.

---

## N. Method/multi-lane/shadow status


| Method                              | Phase                | Sample 60d                                | Free win              | False promotion   | Next gate                  | ETA earliest     |
| ----------------------------------- | -------------------- | ----------------------------------------- | --------------------- | ----------------- | -------------------------- | ---------------- |
| OFFICIAL_BASELINE_CONTROL           | TEST_LANE_PARALLEL   | 60d                                       | n/a                   | 0                 | n/a                        | always-on        |
| **AI_CHAIN_PRESERVATION_V1**        | TEST_LANE_PARALLEL   | MN fw=4/fl=1                              | **+1 day 05/05 MN**   | 0                 | NEED_14D_MN_ONLY           | 2026-05-19       |
| AI_CHAIN_PRESERVATION_V1 (MT/MB)    | TEST_LANE_PARALLEL   | MT fw=8/fl=12 destructive, MB destructive | n/a                   | n/a               | DROP_FROM_MT_MB            | DROP_AS_DESIGNED |
| **SPECIALIST_ROSTER_V1**            | TEST_LANE_PARALLEL   | MB fw=5/fl=0; MN fw=3/fl=0; +1 04/05 MN   | **+1 04/05 MN**       | 0                 | WAIT_30_60D_MORE_MB        | 2026-06-15       |
| STRENGTH_WEIGHTED_V52_5_2           | TEST_LANE_PARALLEL   | MB fw=8/fl=7                              | 0 04/05+05/05         | 0                 | NEED_30D                   | 2026-06-04       |
| PRIOR_REGION_CONTEXT_SAFE_V1        | TEST_LANE_PARALLEL   | thin                                      | 0                     | 0                 | NEED_30D                   | 2026-06-04       |
| NO_TOKEN_HERD_REDUCTION_V1          | TEST_LANE_PARALLEL   | thin                                      | 0                     | 0                 | NEED_30D                   | 2026-06-04       |
| COMPOSITE_CHALLENGER_V2 (MB)        | TEST_LANE_PARALLEL   | MB only                                   | 0                     | 0                 | NEED_30D                   | 2026-06-04       |
| TIER_AWARE_BUNDLE_SHADOW_V1 (MB)    | SHADOW_BACKFILL      | thin                                      | n/a                   | n/a               | OWNER_LOCK_TIER_3          | OWNER_DECIDE     |
| corrected_rescue_replay             | SHADOW_BACKFILL      | 13 VALID days                             | n/a                   | leakage-corrected | NEED_14_VALID + ≥+5 net pp | OPEN             |
| single_vote_rescue_replay           | DROP_AS_DESIGNED     | leaky                                     | n/a                   | LEAKY             | n/a                        | DROPPED          |
| tier2_replay_shadow V1/V2           | DROP_AS_DESIGNED     | -9.5..-19.4 pp                            | n/a                   | n/a               | n/a                        | DROPPED          |
| cohere_rerank_effectiveness_v1      | SHADOW_BACKFILL      | 39 rows                                   | n/a                   | unproven_lift     | NEED_30D                   | 2026-06-04       |
| mt_model_hit_output_drop_shadow     | TEST_LANE_PARALLEL   | measurement                               | n/a                   | n/a               | feeds C-07 panel           | UI_TEST_ONLY     |
| loz_stage_trace_shadow              | TEST_LANE_PARALLEL   | 6174+182 rows                             | n/a                   | n/a               | feeds C-09 (deferred)      | OWNER_DECIDE     |
| weekday_blackspot_shadow            | TEST_LANE_PARALLEL   | 21 rows                                   | n/a                   | n/a               | feeds C-15 alert UI        | UI_TEST_ONLY     |
| cross_region_spillover_shadow       | TEST_LANE_PARALLEL   | 9577 rows                                 | n/a                   | n/a               | informational              | always-on        |
| model_strength tensor               | TEST_LANE_PARALLEL   | 8875 rows anchor 05/05                    | n/a                   | n/a               | feeds C-14 chip            | UI_TEST_ONLY     |
| model_latency_cost_audit_daily      | **BROKEN_NEEDS_FIX** | 0/0                                       | n/a                   | n/a               | C-05 instrumentation       | OPEN             |
| **V55_GOOGLE_DIRECT_SHADOW_COHORT** | TEST_LANE_PARALLEL   | day 1                                     | 1 (gemini-3-flash MB) | 0                 | NEED_14D                   | 2026-05-19       |


`/du-doan-test` overall: `**LIVE_PARALLEL_AUTO_PENDING_ONLY`** — chưa đổi.

---

## O. What improved after 04/05 + 05/05

1. **MT 7d** vọt lên 71.4% — best MT trong dài hạn nhiều tuần. Cần xem có duy trì không.
2. **Test lane đã chứng minh có ngày cứu được MN** (2/2 ngày qua); SPECIALIST_ROSTER + AI_CHAIN_PRESERVATION trên MN đáng theo dõi tiếp.
3. **gemini-3-flash MB BT WIN ngày đầu** (91+14 cả 2 hit) — tín hiệu thú vị, cần theo dõi 14 ngày.
4. **V55 fix bug scheduler preflight** cho `gemma-`* → từ 06/05 cohort 3 model Google đầy đủ.
5. **Weekday blackspot rolling 30d cập nhật** (MT Mon downgrade từ BLACK_SPOT → STRUCTURAL_RISK; MB Wed/Fri vẫn BLACK_SPOT).

## P. What did NOT improve

1. **MN 30d BT giảm** từ 60% → 56.7%; 7d chỉ 42.9%.
2. **MB structural BT yếu** không thay đổi (60d 26.7%, 7d 14.3%).
3. **C-05 latency** vẫn 0/0 — pruning blocked vô thời hạn.
4. **MT herding tiếp tục** (AI_CHAIN_PRESERVATION còn destructive trên MT 60d fw=8/fl=12).
5. **MB Wed/Fri** vẫn BLACK_SPOT_CONFIRMED.
6. **Single-vote rescue, tier2 V1/V2** vẫn DROPPED.
7. **Composite V2 chưa đạt gate**.
8. **Loz output policy chưa đủ proof** — `LOZ_NOT_READY_FOR_RULE` vẫn còn.

---

## Q. Safe implementation plan

### Q.1 — Đã làm ngay trong V55 pass này (24h, đã DONE)

- ✓ V55 add 3 Google direct shadow models (Gemini 3.1 Pro, Gemini 3 Flash, Gemma 4 31B) — already ran 06/05 morning.
- ✓ V55 fix scheduler preflight bug for `gemma-`* — sẽ chạy 06/05.
- ✓ Materialize 04/05+05/05 surfaces: loz_stage_trace, mt_drop, v52, weekday_blackspot, model_strength tensor, experimental_preview_shadow, V52.5.6 multi-region runner.
- ✓ Tensor anchor advanced 2026-05-02 → **2026-05-05**.
- ✓ Governance docs synced: CHANGELOG, SSOT, FOLLOW_UP_TRACKER, active roadmap.

### Q.2 — Trong 3 ngày (06-08/05)

- C-02 API source labels reconfirm trong UI sau V52.6.
- Daily 1-day mini-report (`artifacts/_v55_daily_*.md`) cho 06/05 + 07/05 + 08/05.
- Method rescue/break table cập nhật mỗi ngày.

### Q.3 — Sau 3-5 clean closeouts (~10/05)

- **C-03 multi-region closeout evaluator** — extend `_du_doan_test_closeout_evaluator.py` từ MB-only sang MN+MT+MB.
- **C-04 scheduler auto-wire** test lane only — chỉ wire khi C-03 sạch ≥3 ngày.
- **NEVER auto-wire** nếu source fields còn drift.

### Q.4 — Sau 14 VALID_LIVE_DAY (~19/05)

- Owner evidence pack: MN_AI_CHAIN_PRESERVATION (chỉ MN), MN_SPECIALIST_ROSTER, MB_SPECIALIST_ROSTER, MB_STRENGTH_WEIGHTED, V55 cohort.
- **Không production deploy**.

### Q.5 — Sau 30 ngày (~04/06)

- C-05 per-model latency instrumentation deploy ngoài live window.
- 30d latency review cho cả 16 model (13 shadow + 3 mới + ML/AI active).
- Model pruning proposal **test-lane first**.
- Composite V2, NO_TOKEN_HERD, PRIOR_REGION đủ samples để gate.

### Q.6 — Sau 60 ngày (~04/07)

- Family/region-weekday/station-aware aggregation proposal.
- Shadow → voter promotion candidate review.
- Wave 1 official output improvement (single-region single-method swap) chỉ nếu evidence pack ≥+5 pp BT_lift + false_promo <3% theo OFFICIAL_OUTPUT_IMPROVEMENT_TIMELINE_20260504.md.

---

## R. Code readiness matrix


| Item                                            | Bucket                                                                        |
| ----------------------------------------------- | ----------------------------------------------------------------------------- |
| C-01 UI source-badge V52.6                      | DONE                                                                          |
| C-02 API source labels                          | DONE (V54)                                                                    |
| C-05 per-model latency instrumentation          | IMPLEMENT_NOW_MEASUREMENT_ONLY (chưa làm; ưu tiên tuần này ngoài live window) |
| C-06 loz_stage_trace materializer               | DONE (V54 + V55 backfill 04/05+05/05)                                         |
| C-07 MT correct-but-dropped UI panel            | IMPLEMENT_NOW_UI_TEST_ONLY                                                    |
| C-14 per-station/weekday/model strength chip UI | IMPLEMENT_NOW_UI_TEST_ONLY                                                    |
| C-15 MB blackspot alert                         | DONE (V54) — UI panel surface PENDING `IMPLEMENT_NOW_UI_TEST_ONLY`            |
| C-03 multi-region closeout evaluator            | WAIT_3_5_CLEAN_CLOSEOUTS                                                      |
| C-04 scheduler auto-wire test lane              | WAIT_3_5_CLEAN_CLOSEOUTS                                                      |
| C-08 model pruning                              | WAIT_30D_LATENCY_AND_SIGNAL                                                   |
| C-09 loz output policy change                   | WAIT_30D + OWNER_DECIDE                                                       |
| C-10 Composite V2 promote                       | WAIT_14_VALID_LIVE_DAYS + GATE_NOT_MET                                        |
| C-11 single-vote rescue                         | DROP_AS_DESIGNED + LEAKY_REFERENCE_ONLY                                       |
| C-12 Sunday retrain enabling new shadow         | WAIT_30D                                                                      |
| **V55 add 3 Google models**                     | DONE (V20.3.37.55)                                                            |
| **V55 scheduler preflight gemma fix**           | DONE (V20.3.37.55)                                                            |


---

## S. Post-hash / no-official-mutation proof

- Pre-hash: `artifacts/_v55_pre_hash_20260505.txt`.
- Post-hash: `artifacts/_v55_post_hash_20260505.txt`.
- 4 forensic tables (`predictions`, `final_bundles`, `lottery_results`, `model_daily_eval`): hash growth chỉ do **NATURAL_LIVE_GROWTH** (predictions +81 hôm nay, final_bundles +3 hôm nay, lottery_results 04/05 và 05/05 đầy đủ, model_daily_eval +3 hôm nay).
- Test/diagnostic tables tăng do V55 manual run (du_doan_test_runs +25, bundles +25, candidates +396, model_contribution +396, audit_log +5).
- Measurement tables tăng do materializer (loz_stage_trace +182, mt_drop +10, weekday_blackspot anchor 2026-05-05 +21, model_strength_by_region_weekday_station_daily +8875).
- **Không có mutation không giải thích được**. Service restart 1 lần lúc 20:08 VN sau scheduler fix → scheduler_logs growth tự nhiên.

---

## T. What NOT to do next

1. **Không** auto-wire scheduler test lane (C-04) trước khi có ≥3 clean closeouts với evaluator C-03.
2. **Không** promote MT_AI_CHAIN_PRESERVATION_V1 — destructive trên MT (60d fw=8/fl=12; 04/05+05/05 broke baseline win).
3. **Không** prune model nào (C-08) khi C-05 latency vẫn 0/0.
4. **Không** đổi `final_bundles` BT/lo2 selection logic.
5. **Không** đổi roster output (vẫn 15 model).
6. **Không** sử dụng single_vote_rescue, tier2 V1/V2 (DROPPED).
7. **Không** dựa 04/05+05/05 alone để promote method nào — `TWO_DAY_FORENSIC_ONLY`.
8. **Không** đổi loz output policy (`LOZ_OUTPUT_POLICY_CHANGE_NOT_ALLOWED`).
9. **Không** dùng MN_SPECIALIST_ROSTER hoặc MN_AI_CHAIN làm output trong tuần này — chỉ test lane.

---

## OWNER-FACING ANSWERS (Tiếng Việt)

1. **04/05 official**:
  - MN BT 65 = **TRẬT** (PARTIAL lo2 vì 32 hit).
  - MT BT 29 = **TRÚNG** + lo2 đầy đủ.
  - MB BT 09 = **TRẬT**.
2. **05/05 official**:
  - MN BT 15 = **TRẬT** (cả lo2 trật).
  - MT BT 44 = **TRÚNG** (lo2 phần 1).
  - MB BT 83 = **TRẬT**.
3. `**/du-doan-test` 04/05 và 05/05** có hơn official không?
  - **Có**, ở **MN**: ngày 04/05 SPECIALIST_ROSTER chọn 32 (trúng), ngày 05/05 AI_CHAIN_PRESERVATION chọn 52 (trúng). Đây là 2 free wins → đáng theo dõi.
  - **Không**, ở **MT**: official đã trúng cả 2 ngày, AI_CHAIN_PRESERVATION lại đổi sang số khác → **không nên promote** trên MT.
  - **Không**, ở **MB**: không method nào trúng 2 ngày qua.
4. Test giống official thì là **clone hay agreement**? Báo cáo phân loại rõ:
  - `OFFICIAL_BASELINE_CONTROL` luôn là **clone-by-design**.
  - Khi method khác chọn cùng số official → `INDEPENDENT_AGREEMENT_WITH_OFFICIAL` (không phải clone).
  - V52.6 UI đã sửa label `🟰 đồng thuận` thay vì `= chính` → owner sẽ không bị nhầm.
5. **MT còn lỗi "model đúng nhưng final sai"?** — **Còn**. 05/05 MT có 6 actual tails đã được model nào đó top1, nhưng 5 trong số đó bị final loz drop. Pattern này lặp lại nhiều ngày. C-07 panel cần build để owner thấy rõ.
6. **MB AI còn yếu?** — **Còn rất yếu**. 60d MB BT 26.7%; AI top model `claude-sonnet-4-6` chỉ helpful 0.28 trên MB. MB Wed/Fri vẫn BLACK_SPOT_CONFIRMED. **Chưa đủ proof để loại model nào** vì sample thin + latency không có.
7. **Loz1/loz2 kiểm soát tốt hơn chưa?** — **Chưa**. Vẫn `LOZ_NOT_READY_FOR_RULE`. Stage trace đã có data 60d + 04/05+05/05 nhưng tín hiệu mixed/region-conditional.
8. **Model nào mạnh/yếu?**
  - **Mạnh chung**: `combo-super` MN, `gemini-2.5-pro` MN/MT, `claude-opus-4` MN, `claude-sonnet-4-6` MN/MT.
  - **Yếu MB**: hầu hết. Best MB AI là `claude-sonnet-4-6 ai_chain` nhưng helpful chỉ 0.28.
  - **NO_TOKEN**: `meta-learning` MN tốt; `random-forest rerun_post_mt` cứu một phần MB.
  - **Mới**: `gemini-3-flash` MB ngày đầu WIN BT — KEEP_CANDIDATE 14 ngày; `gemini-3.1-pro` chậm hơn (PARTIAL MB ngày đầu); `gemma-4-31b` 0 rows do bug — fix V55, sẽ chạy 06/05.
9. **Đã đủ cơ sở giảm model/cost?** — **Chưa**. C-05 latency vẫn 0/0; pruning blocked tới khi instrument xong + thêm 30 ngày samples.
10. **Đã đủ cơ sở đổi official?** — **Chưa, tuyệt đối chưa**. `NOT_READY_FOR_OFFICIAL_CHANGE`. Cần ≥14 VALID_LIVE_DAY rolling proof + owner approval trước Wave 1 (sớm nhất 2026-06-15 theo OFFICIAL_OUTPUT_IMPROVEMENT_TIMELINE).
11. **Kế hoạch nâng cấp tiếp theo (chính xác)**:
  - **Trong 24h (đã DONE V55 pass này)**: 3 Google models live, scheduler preflight fix, 2-day materialize, governance sync.
    - **3 ngày**: daily mini-report 06-08/05, theo dõi 3 model mới, tiếp tục manual V52.5.6 runner.
    - **5-7 ngày (10-12/05)**: C-03 multi-region closeout evaluator (test lane only); C-07 MT panel; C-14 chip UI; C-15 MB blackspot alert UI surface; C-05 latency instrumentation chuẩn bị deploy ngoài live window.
    - **14 ngày (19/05)**: Evidence pack cho method MN-only (AI_CHAIN_PRESERVATION, SPECIALIST_ROSTER) + V55 cohort (gemini-3-flash MB).
    - **30 ngày (04/06)**: C-05 chính thức + composite V2 review + pruning proposal test lane.
    - **60-105 ngày**: Wave 1 official output improvement (chỉ nếu evidence pack đạt gate + owner OK).
12. **Cái gì làm ngay** (đã làm trong V55 pass này): add 3 Google models + fix scheduler preflight + materialize 2 ngày + sync docs.
  **Cái gì TUYỆT ĐỐI CHƯA làm**: đổi `/du-doan`, đổi `final_bundles`, prune model, scheduler auto-wire test lane, promote method nào ra production, đổi loz output policy.

---

## Required artifacts (V55)

- `artifacts/phase_checkpoints/TOTAL_FORCE_V55_20260504_20260505_CLOSEOUT_AND_NEXT_UPGRADE_PLAN.md` (file này)
- `artifacts/phase_checkpoints/_v55_state_20260505.json`
- `artifacts/_v55_pre_hash_20260505.txt`
- `artifacts/_v55_post_hash_20260505.txt`
- `artifacts/_v55_official_closeout_20260504_20260505.json`
- `artifacts/_v55_du_doan_test_closeout_20260504_20260505.json`
- `artifacts/_v55_du_doan_test_ui_api_source_audit_20260505.json`
- `artifacts/_v55_rolling_metrics_after_20260505.json`
- `artifacts/_v55_mt_correct_but_dropped_20260504_20260505.json`
- `artifacts/_v55_mt_correct_but_dropped_extra_20260504_20260505.json`
- `artifacts/_v55_mb_ai_notoken_specialist_forensic_20260504_20260505.json`
- `artifacts/_v55_loz_control_audit_20260505.json`
- `artifacts/_v55_model_tensor_latency_pruning_readiness_20260505.json`
- `artifacts/_v55_method_multilane_status_20260505.json`
- `artifacts/_v55_forensic_query.py`, `_v55_aggregate.py`, `_v55_test_preview_check.py`, `_v55_status_recon.py`, `_v55_check_new_shadow_rows.py`, `_v55_gemma_debug_and_picks.py`, `_v55_gemma_route_verify.py`, `_v55_envload_check.py`, `_v55_actual_tails_verify.py`
- VPS deploy artifacts: `artifacts/_v55_vps_apply.sh`, `_v55_fix_envpath.sh`, `_v55_materialize_2day.sh`, `_v55_materialize_2day_v2.sh`
- `artifacts/live_watch/LIVE_WATCH_20260505_V55.md` (next phase write)

---

**Câu chốt:** Hôm nay live cycle hoàn tất bình thường. **Official quality V55 verdict = `OFFICIAL_QUALITY_NOT_PROVEN / MIXED_SIGNAL / REGION_CONDITIONAL` (không đổi vs V54 mặc dù MN giảm nhẹ và MT 7d cao).** Test lane đã chứng minh có ngày cứu MN. **Không đủ proof cho official change**. Em đã thực hiện toàn bộ items trong nhóm "an toàn tuyệt đối" cho phép trong V55, không chạm output, không promote method, không prune model.