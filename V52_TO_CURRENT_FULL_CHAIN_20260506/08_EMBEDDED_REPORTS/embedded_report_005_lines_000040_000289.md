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

