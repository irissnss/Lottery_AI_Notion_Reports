# Experimental Lane Roadmap — `/du-doan-test`

> Owner deliverable | Created 2026-05-04 00:40 VN
> Scope: trả lời "Luồng thực nghiệm hiện tại chạy thế nào? Khi nào áp dụng phương pháp mới / đo lường mới / shadow model mới / nâng cấp total output UI / loại bỏ model tệ?"
> Hard lock: file này KHÔNG đề xuất production change; chỉ mô tả luồng test lane và lộ trình tới đề xuất.

---

## 1. Tóm tắt 8 dòng

1. Luồng thực nghiệm chạy song song với `/du-doan` ở mức **`LIVE_PARALLEL_AUTO_PENDING_ONLY`** — đầy đủ schema/engine/runner/API/UI đa miền nhưng vẫn chạy thủ công, không có scheduler auto-wire.
2. Dữ liệu test KHÔNG ghi vào bảng official; mọi row mặc định `official_output=false`, `output_impact=false`, `test_only=1`, `output_eligible=0`.
3. Mỗi method mới đi qua **6 pha** (Proposed → Design → Shadow_Backfill → Test_Lane_Parallel → Owner_Review → Production). Hiện tại 6 method V52.5.x đang ở pha 4 (Test_Lane_Parallel) cho cả MN/MT/MB.
4. UI nâng cấp tiếp theo (V52.7+): per-station strength chip, MT correct-but-dropped panel, official-vs-test daily summary, model-strength sort. Đều test-only.
5. Model individual (no-token / AI / smart / super) hiện đã được gom thành **1 final bundle** ở luồng official, và **6 challenger bundle** ở luồng test (mỗi challenger là một cách aggregate khác nhau).
6. Promote model shadow → production, prune model AI tệ — đều **gated** sau khi V52.5.7 60d evidence + thêm 30-60d nữa + per-model latency có data.
7. Cost/latency reduction (mục tiêu giảm 25 model) chưa đủ điều kiện vì `NO_PER_MODEL_DURATION` 3273/3273 rows.
8. Dự kiến đề xuất official change **sớm nhất 14-30 ngày nữa** sau khi đủ rolling sample sạch + gate criteria thoả mãn + owner unlock — không phải tự động chạy production.

---

## 2. Hiện trạng kiến trúc luồng thực nghiệm

### 2.1 Luồng dữ liệu MN/MT/MB

```
Production cascade (hard-locked, không đụng):
  MN auto_daily 04:15 → predictions(MN) → final_bundles(MN) → /du-doan(MN)
        │
        ├─ rerun_post_mn lúc MT predict
        ▼
  MT 17:30 → predictions(MT) → final_bundles(MT) → /du-doan(MT)
        │
        ├─ rerun_post_mt lúc MB predict
        ▼
  MB 18:30 → predictions(MB) → final_bundles(MB) → /du-doan(MB)

Experimental lane (test-only, ghi bảng riêng):
  Production cascade hoàn tất
        │
        ▼
  V52.5.1 _compute_model_strength_tensor.py (anchor D-1)
    → model_strength_by_region_weekday_station_daily (9052 rows)
        │
        ▼
  V52.5.2 _materialize_experimental_preview_shadow.py
    READ: final_bundles.source_predictions_json (live-available trước actual)
    READ: model_daily_eval (past-only, < target date)
    READ: lottery_results (chỉ prior region, theo cutoff spec)
    APPLY: 6 method (BASELINE / STRENGTH_WEIGHTED / AI_CHAIN / SPECIALIST / PRIOR_REGION / NO_TOKEN_HERD)
    WRITE: experimental_preview_shadow (1098 rows × 60d × 3 region × 6 method)
        │
        ▼
  V52.5.3 _du_doan_test_engine.py
    READ: experimental_preview_shadow
    WRITE: du_doan_test_runs / bundles / results / candidates / model_contribution
        │
        ▼
  V52.5.6 _du_doan_test_daily_runner.py --region ALL
    Chạy thủ công sau closeout (chưa scheduler auto-wire)
        │
        ▼
  /api/du-doan-test/{MN/MT/MB} (V52.5.5)
    READ: experimental_preview_shadow + final_bundles (baseline only) + V52.2 measurement tables
    SHOW: /du-doan-test admin-only UI (V52.6 với source banner + picks-per-experiment)
```

### 2.2 Hard contract (đã kiểm hash V53)

- KHÔNG gọi `generate_final_bundle()`.
- KHÔNG ghi `final_bundles`, `predictions`, `model_daily_eval`, `lottery_results`, `scoring`, `bundle voting`, `lane weights`, `verdict weights`, `output policy`, `model roster`, `production prompt`.
- Mỗi V52.5.x runner viết source-hash before/after vào `du_doan_test_audit_log`.

### 2.3 Anti-leakage cutoff (đã codify ở `V52_4_MN_MT_TEST_LANE_CUTOFF_SPEC_20260503.md`)

| Region | Allowed selection inputs | Forbidden |
|---|---|---|
| MN | D-1 mọi region; tensor anchor strict D-1 | MN(D), MT(D), MB(D) actuals; hit-known selection |
| MT | D-1 + MN(D) actuals (MT chạy sau MN) | MT(D), MB(D) actuals |
| MB | D-1 + MN(D) + MT(D) actuals | MB(D) actuals |

### 2.4 6 method hiện đang chạy ở pha Test_Lane_Parallel

| Method | Mô tả | Thuộc tính nguồn |
|---|---|---|
| `*_OFFICIAL_BASELINE_CONTROL` | Mirror đọc-only của official BT/lo2 để so sánh apples-to-apples | logical clone |
| `*_STRENGTH_WEIGHTED_V52_5_2` | Score = base_score + ai_chain_votes·0.020 + ai_model_votes·0.012 + strong_voters·0.018 + prior_tail·0.014 + tensor_helpful·0.014 - rerun_overweight·0.008 - no_token_overweight·0.006 - gap_from_top·0.020 | tensor anchored D-1 + shared candidate set |
| `*_AI_CHAIN_PRESERVATION_V1` | Pick top1 candidate có ≥3 AI-chain voters (fallback: ≥3 AI model voters) | shared candidate set + lane_votes |
| `*_SPECIALIST_ROSTER_V1` | Pick candidate có nhiều specialist voters (specialist = model BT≥35% trên 60d trong cùng region) | model_daily_eval past-only + lane_votes |
| `*_PRIOR_REGION_CONTEXT_SAFE_V1` | Pick candidate có tail xuất hiện trong prior-region actuals D | prior region D actuals (live-available) |
| `*_NO_TOKEN_HERD_REDUCTION_V1` | Score điều chỉnh giảm rerun_post_X overweight và no_token_overweight | shared candidate set + lane composition |

Riêng MB còn 2 method legacy V46/V50: `MB_COMPOSITE_CHALLENGER_V2` và `MB_TIER_AWARE_BUNDLE_SHADOW_V1` (placeholder).

---

## 3. Phase ladder — khi nào method mới được áp dụng

### 3.1 6 pha

| Pha | Tên | Trigger vào pha | Trigger ra pha | Quyền |
|---|---|---|---|---|
| 0 | `PROPOSED` | Owner / agent ý tưởng | Code design + cutoff spec | agent draft |
| 1 | `DESIGN_ONLY` | Cutoff spec + leakage audit ký | Materializer compile-clean local | agent |
| 2 | `SHADOW_BACKFILL` | Materializer chạy 30-60d closed days | Pre/post hash sạch + ≥30 rows | agent |
| 3 | `TEST_LANE_PARALLEL` | Materializer + engine + UI surfacing | ≥14 VALID_LIVE_DAY natural closeout chứng minh | agent |
| 4 | `OWNER_REVIEW` | Evidence pack đạt gate | Owner ký unlock | owner |
| 5 | `PRODUCTION_DEPLOY` | Owner OK | Hash guard pass + 7d live verify | agent + owner |

### 3.2 Gate criteria mặc định (mỗi method tự chỉnh tăng nếu cần)

Để chuyển từ pha 3 → pha 4 (`OWNER_REVIEW`):
- `flips_to_win - flips_to_lose ≥ +5` trên ≥30 active picks (test_bt ≠ baseline_bt) trong rolling window 30d.
- `false_promotion_rate ≤ 10%`.
- Sample size ≥ 30 ngày VALID_LIVE_DAY.
- Region-conditional split: nếu method âm ở 1 region, chỉ unlock ở region khác.
- Leakage audit clean (anchor D-1 + cutoff spec compliant).
- 0 mutation pre/post hash với official tables.

Để chuyển từ pha 4 → pha 5 (`PRODUCTION_DEPLOY`):
- Owner trả lời `OK` trong DECISION_LOG.
- 7-day live verify dry-run trước final deploy.
- Rollback plan ghi sẵn (revert path + DROP TABLE script + commit revert SHA).

### 3.3 Hiện trạng từng method

| Method | Region áp dụng | Pha hiện tại | Sample 60d (fw / fl / hits) | Cần để vào pha 4 | ETA earliest |
|---|---|---|---|---|---|
| `MB_OFFICIAL_BASELINE_CONTROL` | MB | logical clone | 0/0/18 | n/a (control row) | n/a |
| `MB_COMPOSITE_CHALLENGER_V2` | MB | 4 pending | gate +4/30 vs achieved +3 | thêm 30d sạch | 2026-06-03 |
| `MB_AI_CHAIN_PRESERVATION_V1` | MB | 3 | 10/10/18 | net +5 trên 30d sạch | 2026-06-03 |
| `MB_STRENGTH_WEIGHTED_V52_5_2` | MB | 3 | 8/7/19 | net +5 trên 30d sạch | 2026-06-03 |
| `MB_SPECIALIST_ROSTER_V1` | MB | 3 (placeholder) | 5/0/18 | sample ≥30 active picks (hiện active ~5/60) | 2026-07-15 |
| `MB_PRIOR_REGION_CONTEXT_SAFE_V1` | MB | 3 | 7/6/19 | net +5 | 2026-06-03 |
| `MB_NO_TOKEN_HERD_REDUCTION_V1` | MB | logical clone | 4/4/18 | drop nếu giữ neutral | 2026-06-03 review |
| `MN_AI_CHAIN_PRESERVATION_V1` | MN | 3 | 4/1/32 | sample ≥30 active picks (hiện active 5/60) | 2026-07-01 |
| `MN_STRENGTH_WEIGHTED_V52_5_2` | MN | 3 | 1/1/29 | net +5, sample mỏng | 2026-07-15 |
| `MN_SPECIALIST_ROSTER_V1` | MN | 3 | 3/0/32 | sample mỏng | 2026-07-15 |
| `MN_NO_TOKEN_HERD_REDUCTION_V1` | MN | logical clone | 0/0/29 | drop candidate | 2026-06-03 review |
| `MN_PRIOR_REGION_CONTEXT_SAFE_V1` | MN | 3 (n/a) | 0/0/0 (MN không có prior region) | drop hoặc redesign | 2026-06-03 review |
| `MT_AI_CHAIN_PRESERVATION_V1` | MT | 3 | **8/12/24** destructive | DROP_AS_DESIGNED candidate | 2026-06-03 review |
| `MT_STRENGTH_WEIGHTED_V52_5_2` | MT | 3 | 5/6/27 | net +5 chưa met | 2026-07-01 |
| `MT_PRIOR_REGION_CONTEXT_SAFE_V1` | MT | 3 | **4/10/22** destructive | DROP_AS_DESIGNED candidate | 2026-06-03 review |
| `MT_SPECIALIST_ROSTER_V1` | MT | 3 | 1/3/26 | sample mỏng | 2026-07-15 |
| `MT_NO_TOKEN_HERD_REDUCTION_V1` | MT | 3 | 2/3/27 | inconclusive | 2026-07-01 |
| corrected_rescue_replay (V39) | all | 3 | 12 VALID_LIVE_DAY clean-day net mỏng | thêm sample → ≥30 VALID | 2026-06-15 |
| single_vote_rescue (V37) | n/a | DROP | leaky | KHÔNG unlock | drop forever |
| tier2_replay V1/V2 | n/a | DROP | -19.4 pp | KHÔNG unlock | drop forever |

---

## 4. Lifecycle model individual / shadow

### 4.1 Cách model individual đang được gom

Hiện tại trong production (`generate_final_bundle()`):
- 8 model TOKEN AI (`gpt-5-mini`, `claude-sonnet-4-6`, `gemini-2.5-flash`, `claude-opus-4-20250514`, `deepseek-reasoner`, `gemini-2.5-pro`, `gpt-5.4`, `combo-super`).
- 7 model NO_TOKEN (`meta-learning`, `lstm`, `xgboost`, `random-forest`, `smart-ensemble`, `smart-ml`, `combo-no-token`).
- 10-11 model SHADOW chạy trong `shadow_auto_eval` sau cascade (deepseek-v4-flash/pro, glm-5.1, gpt-5.5, gpt-oss-120b, grok-4.20-multi-agent, kimi-k2.5/k2.6, mistral-large-3, nemotron-3-super, qwen3-coder, qwen3-max-thinking, qwen3.6-plus, llama-4-maverick, arcee-trinity).
- Tổng ~25 model nhưng **shadow không vote vào candidate set** của `final_bundles.source_predictions_json` — chỉ 14 voter thực sự.

Aggregation production (read-only, không sửa):
- Mỗi candidate tail = sum(model.score · effective_weight(model, lane, run_source)).
- PP-1 herd dampener (giảm 0.85 nếu ≥3 voter trùng tail).
- PP-5 family bonus: `ENABLE_FAMILY_BONUS=False` từ V20.3.29.

### 4.2 Khi nào gom lại theo total cải tiến

Kế hoạch test-lane-only (chưa production):

| Phase | Action | Trigger | Output |
|---|---|---|---|
| Now | V52.5.2 6 method shared candidate set + 1 control + 5 challenger | đã chạy | `experimental_preview_shadow` |
| Phase A (3-7 ngày) | Thêm `*_FAMILY_AWARE_AGGREGATION_V1` (cộng tách AI vs NO_TOKEN trước, weight family theo strength tensor) | C-13 sau khi C-05 latency có data | `experimental_preview_shadow` thêm 3 row/region/day |
| Phase B (7-14 ngày) | Thêm `*_REGION_WEEKDAY_STRENGTH_AWARE_V1` (dùng tensor grain region+weekday để weight voter) | tensor đã có; chỉ cần materializer mới | dùng strength_tensor anchor D-1 |
| Phase C (14-30 ngày) | Thêm `*_STATION_AWARE_V1` cho MN/MT (mỗi đài có model strength khác) | tensor grain region+station đã có | bundle station-specific tail |
| Phase D (30+ ngày) | Hybrid composite: chọn voter theo region+weekday+station tensor, sau đó vote weighted | Phase A+B+C đã có evidence | full multi-grain composite |
| Phase E (60+ ngày) | Promote method strongest sang official (gate criteria thoả mãn) | owner unlock | production |

### 4.3 Khi nào shadow model promote vào production

Hiện shadow_auto_eval ghi rows nhưng KHÔNG vote vào final_bundles. Tensor V52.5.1 cho thấy MN shadow `arcee-trinity` BT 2/2 (sample 2 ngày), `glm-5.1` BT 11/18, `mistral-large-3` MB BT 3/4 — nhưng sample mỏng.

Promotion gate (test-lane-only deploy trước, production sau):
1. Shadow model đạt BT_rate ≥ 40% trên ≥30 ngày active prediction.
2. Shadow model có `unique_useful_signal` ≥ 5 (số ngày shadow đúng mà 14 voter chính sai).
3. Latency ≤ 60s (cần C-05 instrument trước).
4. Cost/day ≤ ngân sách owner approve.
5. Test lane chạy ≥7d với shadow model làm voter, không destructive.
6. Owner ký unlock.

ETA shadow → test-lane voter: **2026-06-04** (cần C-05 latency xong + 30d shadow data sạch).
ETA shadow → production voter: **2026-07-04** (sau 30d test-lane proof + owner OK).

### 4.4 Khi nào AI model tệ bị đào thải

Tensor V52.5.1 30d MB AI cao nhất `claude-sonnet-4-6 ai_chain` helpful 0.2815. Đây là yếu nhưng **chưa đủ proof để loại** vì:
- AI có thể có `unique_useful_signal` ở ngày herd đúng (cần đo `correct_but_dropped` rolling).
- Chưa có cost/latency data → không thể justify "loại để giảm cost".

Pruning gate (chỉ áp dụng test lane trước):
1. Model BT_rate ≤ 25% trên ≥45 ngày.
2. `unique_useful_signal` ≤ 1 trên 45 ngày (gần như không bao giờ là voter duy nhất đúng).
3. `helped_test - hurt_test` âm trên 45 ngày.
4. `correct_but_dropped` thấp (model không cứu được số dropped).
5. Latency ≥ 60s hoặc cost ≥ ngân sách (cần C-05).
6. Test lane chạy ≥7d với model bị remove, kiểm soát hit-rate không tệ hơn.
7. Owner ký drop.

ETA earliest model AI bị đào thải khỏi test lane: **2026-06-15** (cần C-05 + 30d active measurement).
ETA bị đào thải khỏi production: **2026-07-15** (sau 30d test-lane proof + owner OK).

Lưu ý: theo tensor 30d hiện tại, MB AI weak nhất là `claude-sonnet-4-6 ai_chain` (helpful 0.28) nhưng MN cùng model `claude-sonnet-4-6 auto_daily` BT 16/27 helpful 0.563 — **không loại được model toàn cục**, chỉ có thể loại theo region+run_source. Điều này phải reflect trong code trước khi prune.

---

## 5. UI nâng cấp `/du-doan-test`

### 5.1 Đã ship (V52.6 hôm nay)

- Source banner giải thích từng cột đọc bảng nào.
- Bảng "Picks per experiment" — anh thấy ngay 6 method chọn BT gì, đồng thuận hay khác chính.
- Chip `🟰 đồng thuận` / `🆚 khác chính` thay cho `= chính` / `≠ chính` với tooltip giải thích.
- Cache buster `?v=20260504-v52-6-source-badges`.

### 5.2 Kế hoạch UI 3-7 ngày (V52.7+)

| ID | UI item | Source | ETA | Status |
|---|---|---|---|---|
| U-01 | Per-station strength chip cho test_bundle (MN/MT) | `model_strength_by_region_weekday_station_daily` grain region_station | 3 ngày | C-14 ready |
| U-02 | Per-weekday tensor card | tensor grain region_weekday | 3 ngày | C-14 ready |
| U-03 | MT correct-but-dropped panel ("model nào đúng nhưng official drop") | `mt_model_hit_output_drop_shadow` | 3 ngày | C-07 ready |
| U-04 | "Method strongest by region/weekday/station" highlight box | tensor + scoreboards | 7 ngày | sau C-03 |
| U-05 | Real-time mode badge `REALTIME_AVAILABLE_ONLY` vs `POST_CLOSEOUT_DIAGNOSTIC` cho từng row | `du_doan_test_runs.mode` | 3 ngày | trivial |
| U-06 | Pruning candidate panel "Model AI weak by region (KHÔNG dùng cho production yet)" | strength tensor + cost/latency (sau C-05) | 14 ngày | sau C-05 |
| U-07 | Total comparison: "Test method này có cộng dồn đúng hơn official không trên rolling 14/30/60d" | `du_doan_test_results` rolling | 7 ngày | sau C-03 |
| U-08 | Banner cảnh báo MB Wed/Fri 0/4 BT structural | C-15 alert table | 7 ngày | C-15 |

### 5.3 Kế hoạch UI 14-30 ngày (V52.8+)

- Ranking total: hiển thị method-of-the-week / method-of-the-month theo region.
- Family-aware aggregation panel: AI vs NO_TOKEN vs SHADOW contribution daily.
- "Owner-unlock readiness" panel: hiển thị method nào đang gần đạt gate (fw/fl/sample/false_promotion).
- Cost/latency panel sau khi C-05 instrument xong.

---

## 6. Khi nào áp dụng đo lường mới

### 6.1 Đo lường đã có rolling 30-60d

| Đo lường | Bảng | Sample | Trạng thái |
|---|---|---|---|
| Cross-region spillover | `cross_region_spillover_shadow` | 9577 / 60d | đủ diagnostic |
| Same-model cross-region dup | `model_cross_region_dup_shadow` | 640 / 29d | đủ diagnostic |
| Bundle universe coverage | `bundle_universe_coverage_shadow` | 93 / 30d | đủ diagnostic |
| MB structural drilldown | `mb_structural_drilldown_shadow` | 61 / 60d | đủ diagnostic; chứng minh MB Friday 0/5 |
| Strength skip calibration | `strength_skip_calibration_replay_shadow` | 833 / 30d | đủ diagnostic |
| Corrected rescue replay | `corrected_rescue_replay_shadow` | 12 VALID / 30d window | THIẾU sample (cần ≥14) |
| MT model-hit drop matrix | `mt_model_hit_output_drop_shadow` | 301 / 60d | đủ diagnostic |
| Loz selector shadow | `loz_selector_shadow` | 3273 / 60d | đủ diagnostic |
| Latency/cost audit | `model_latency_cost_audit_daily` | 3273 / 60d nhưng **NULL latency_seconds** | KHÔNG đủ; cần C-05 |
| Strength tensor V52.5.1 | `model_strength_by_region_weekday_station_daily` | 9052 anchor D-1 | đủ test-lane consume |
| Multi-region preview V52.5.2 | `experimental_preview_shadow` | 1098 / 60d × 3 region | đủ test-lane scoring |
| Test runs V52.5.3 | `du_doan_test_*` | 579 runs/30d | đủ scoreboard |

### 6.2 Đo lường còn thiếu (sẽ làm 3-14 ngày tới)

| ID | Đo lường | Mục đích | ETA | Status |
|---|---|---|---|---|
| M-01 | Per-model latency instrumentation | Unblock pruning gate | 3 ngày | C-05 IMPLEMENT_NOW_MEASUREMENT_ONLY |
| M-02 | Loz stage trace | Tail bị drop ở stage nào | 7 ngày | C-06 |
| M-03 | Per-station MN/MT strength stratification UI surfacing | C-14 prerequisite | 3 ngày | tensor đã có |
| M-04 | Family contribution daily (AI vs NO_TOKEN vs SHADOW) | Hiểu model nào kéo final | 7 ngày | derive từ candidate row |
| M-05 | MN/MT/MB station-level loz_selector_shadow | Owner asked station split | 14 ngày | sau M-01 |
| M-06 | "Output convergence trace" — số nào leo top10 → top3 → top1 → official BT, qua những stage gì | Owner asked transparency | 14 ngày | new materializer |
| M-07 | Cost/token/timeout per model per day | Owner asked cost reduction | 7 ngày | M-01 prerequisite |
| M-08 | Black spot alert (MB Wed/Fri, MT Mon/Fri) | C-15 | 7 ngày | new shadow alert table |

### 6.3 Khi nào kết quả ra

- 24h (hôm nay → 04/05): Quan sát natural live closeout 04/05. V52.5.6 runner sẽ chạy lại, ghi thêm 1 ngày sample.
- 3 ngày: M-01 + M-03 + M-08 ship measurement-only. UI test bổ sung.
- 7 ngày: M-02 + M-04 + M-07 ship. Test lane có thêm 4 ngày sample sạch (~4 cycles). Begin C-03 multi-region closeout evaluator nếu 3 closeout sạch.
- 14 ngày: Re-evaluate sample. Một số method có thể chuyển từ pha 3 → pha 4 (`OWNER_REVIEW`).
- 30 ngày: First wave evidence pack → owner review → potential first production unlock (per-region per-method).

---

## 7. Khi nào output official được nâng cấp

Trả lời thẳng: **`/du-doan` official sẽ KHÔNG được nâng cấp tự động bởi agent.** Mỗi đề xuất nâng cấp phải:

1. Method đạt pha 4 (`OWNER_REVIEW`) → agent trình evidence pack.
2. Owner đọc, hỏi, cân nhắc, ký `OK` trong DECISION_LOG.
3. Agent triển khai pha 5 với rollback plan + 7-day live verify dry-run + post-deploy hash guard.

Earliest realistic timeline:
- **2026-06-03** (30 ngày): Composite V2 / AI_CHAIN_PRESERVATION MB / SPECIALIST_ROSTER MB có thể vào pha 4. Owner review week.
- **2026-06-15** (45 ngày): Per-region/run_source pruning candidate có thể vào pha 4 (sau khi C-05 latency xong).
- **2026-07-04** (60 ngày): Shadow → production voter promotion candidate.
- **2026-07-15** (75 ngày): AI weak model regional drop candidate.
- **2026-08-15** (105 ngày): Family-aware / region-weekday-aware aggregation production candidate.

Mỗi mốc đều **không phải auto deploy**; mỗi mốc là "agent trình owner review pack". Owner quyết.

---

## 8. Tuyệt đối KHÔNG làm

- Promote method nào sang official khi sample < 14 VALID_LIVE_DAY.
- Drop model nào khỏi production khi `NO_PER_MODEL_DURATION` còn 3273/3273.
- Single-vote rescue (V37) → leaky, drop forever.
- Tier2 V1/V2 → drop_as_designed.
- Force-fit test method ra đúng kết quả 1 ngày.
- Auto scheduler-wire V52.5.6 runner trước khi ≥3 closeout thủ công sạch.
- Đổi loz output policy khi loz `MIXED + REGION_CONDITIONAL`.
- Đổi prompt / model roster / scoring / lane weights khi không có evidence pack + owner OK.

---

## 9. Cross-link

- Lộ trình per-method timeline: `docs/OFFICIAL_OUTPUT_IMPROVEMENT_TIMELINE_20260504.md`
- Cutoff anti-leakage spec: `artifacts/phase_checkpoints/V52_4_MN_MT_TEST_LANE_CUTOFF_SPEC_20260503.md`
- V53 controller audit: `artifacts/phase_checkpoints/TOTAL_FORCE_V53_FULL_REPORT_CHAIN_DU_DOAN_TEST_REALITY_AND_SAFE_NEXT_ACTION_20260503.md`
- V52.5 multi-region buildout: `artifacts/phase_checkpoints/V52_5_MULTI_REGION_PARALLEL_TEST_LANE_20260503.md`
- Code readiness matrix: `artifacts/_v53_code_readiness_matrix_20260503.md`
- FU initiative: `docs/FOLLOW_UP_TRACKER.md` FU-073, FU-114, FU-115
