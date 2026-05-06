# Official Output Improvement Timeline — `/du-doan`

> Owner deliverable | Created 2026-05-04 00:50 VN
> Scope: trả lời "Các phương pháp / đo lường / cơ chế hiện tại đang ở giai đoạn nào? Khi nào có kết quả? Khi nào luồng output official `/du-doan` được cải tiến?"
> Hard lock: file này không tự promote production. Mọi production change phải owner-OK.

---

## 1. Tóm tắt 6 dòng cho anh

1. Hiện tại `/du-doan` chưa có thay đổi nào lên kế hoạch trong 14 ngày tới — đang **observe + accumulate evidence**.
2. Wave 1 production change earliest: **2026-06-03** (30 ngày), nếu Composite V2 / AI_CHAIN_PRESERVATION / SPECIALIST_ROSTER MB đạt gate +5 net.
3. Wave 2: **2026-06-15** (45 ngày), region-conditional pruning sau khi per-model latency C-05 có data 30d.
4. Wave 3: **2026-07-04** (60 ngày), shadow→production voter promotion.
5. Wave 4: **2026-08-15** (105 ngày), family-aware / region-weekday-aware aggregation production.
6. Mỗi wave KHÔNG auto deploy; agent chỉ trình evidence pack, owner ký OK.

---

## 2. Phương pháp / đo lường / cơ chế — bảng full status

### 2.1 Phương pháp test-lane (đã có evidence rolling)

| ID | Method / Mechanism | Region | Pha hiện tại | Sample 60d | Gate criteria | Earliest Owner Review | Production ETA |
|---|---|---|---|---|---|---|---|
| P-01 | `MB_COMPOSITE_CHALLENGER_V2` | MB | 4 pending | 30d backtest +3/30 vs gate +4 | thêm 30d → +4/30 hoặc +5 net trên 30d sạch | 2026-06-03 | Wave 1, earliest 2026-06-15 |
| P-02 | `MB_AI_CHAIN_PRESERVATION_V1` | MB | 3 | 10/10/18 (60d) | net +5 trên 30d active picks | 2026-06-03 | Wave 1, earliest 2026-06-15 |
| P-03 | `MB_STRENGTH_WEIGHTED_V52_5_2` | MB | 3 | 8/7/19 | net +5 trên 30d | 2026-06-03 | Wave 1, 2026-06-15 |
| P-04 | `MB_SPECIALIST_ROSTER_V1` | MB | 3 | 5/0/18 (zero downside) | sample ≥30 active picks | 2026-07-15 | Wave 2-3, 2026-07-30 |
| P-05 | `MB_PRIOR_REGION_CONTEXT_SAFE_V1` | MB | 3 | 7/6/19 | net +5 | 2026-06-03 | Wave 1 |
| P-06 | `MN_AI_CHAIN_PRESERVATION_V1` | MN | 3 | 4/1/32 | sample ≥30 active picks (hiện 5/60) | 2026-07-01 | Wave 2 |
| P-07 | `MN_SPECIALIST_ROSTER_V1` | MN | 3 | 3/0/32 | sample ≥30 active picks (hiện 3/60) | 2026-07-15 | Wave 3 |
| P-08 | `MN_STRENGTH_WEIGHTED_V52_5_2` | MN | 3 | 1/1/29 | sample mỏng | 2026-08-01 | Wave 4 |
| P-09 | `MT_STRENGTH_WEIGHTED_V52_5_2` | MT | 3 | 5/6/27 | net +5 chưa met | 2026-07-01 | Wave 2 |
| P-10 | `MT_AI_CHAIN_PRESERVATION_V1` | MT | DROP candidate | **8/12/24 destructive** | KHÔNG met | DROP_AS_DESIGNED 2026-06-03 |
| P-11 | `MT_PRIOR_REGION_CONTEXT_SAFE_V1` | MT | DROP candidate | **4/10/22 destructive** | KHÔNG met | DROP_AS_DESIGNED 2026-06-03 |
| P-12 | `MT_SPECIALIST_ROSTER_V1` | MT | 3 | 1/3/26 | sample mỏng | 2026-07-15 | Wave 3 |
| P-13 | `MT_NO_TOKEN_HERD_REDUCTION_V1` | MT | 3 | 2/3/27 | inconclusive | 2026-07-01 review |
| P-14 | `corrected_rescue_replay` regional | all | 3 | 12 VALID_LIVE_DAY | ≥14 VALID + net +5 | 2026-06-15 | Wave 2 |
| P-15 | `single_vote_rescue` regional | n/a | DROP forever | leaky | KHÔNG unlock | drop |
| P-16 | `tier2_replay V1/V2` | n/a | DROP forever | -19.4 pp | KHÔNG unlock | drop |

### 2.2 Đo lường mới (đang có / sắp có)

| ID | Đo lường | Bảng | Status | Có data từ | Bắt đầu chạy thật | Output cụ thể |
|---|---|---|---|---|---|---|
| M-01 | Per-model latency / cost / token | `model_latency_cost_audit_daily` (NULL hôm nay) + `gpt_analyzer.py` instrument | C-05 (`IMPLEMENT_NOW_MEASUREMENT_ONLY`) | 2026-05-07 (3 ngày) | 2026-05-07 | unblock pruning gate |
| M-02 | Loz stage trace ("tail bị drop ở stage nào") | new `_materialize_loz_stage_trace_shadow.py` | C-06 | 2026-05-11 (7 ngày) | 2026-05-11 | unblock loz output policy review |
| M-03 | Per-station strength UI surface (MN/MT) | tensor đã có grain region_station | C-14 (UI only) | 2026-05-07 | 2026-05-07 | UI per-station chip |
| M-04 | Family contribution daily | derive từ `du_doan_test_candidates` | C-04 (test-lane only) | 2026-05-11 | 2026-05-11 | family-aware aggregation prereq |
| M-05 | Loz selector station-level | extend `loz_selector_shadow` | sau M-01 | 2026-05-18 (14 ngày) | 2026-05-18 | unblock station loz proof |
| M-06 | Output convergence trace | new materializer | sau M-04 | 2026-05-18 | 2026-05-18 | transparency for owner |
| M-07 | Cost/token/timeout per model per day | extend `model_latency_cost_audit_daily` | sau M-01 | 2026-05-11 | 2026-05-11 | cost reduction proof |
| M-08 | Black-spot alert (MB Wed/Fri, MT Mon/Fri) | new shadow alert table | C-15 | 2026-05-11 | 2026-05-11 | weekday-aware adjustment proof |
| M-09 | Family-aware aggregation (test) | new `_FAMILY_AWARE_AGGREGATION_V1` method | sau M-04 | 2026-05-21 | 2026-05-28 | new test method |
| M-10 | Region-weekday-aware aggregation (test) | new method consume tensor grain region_weekday | sau M-04 | 2026-05-28 | 2026-06-04 | new test method |
| M-11 | Station-aware aggregation (test) | new method MN/MT consume tensor grain region_station | sau M-05 | 2026-06-04 | 2026-06-11 | new test method |
| M-12 | Multi-region closeout evaluator | C-03 | sau ≥3 manual closeout sạch | 2026-05-07 | 2026-05-11 | unblock scoreboard daily |
| M-13 | Scheduler auto-wire V52.5.6 runner | C-04 | sau M-12 + ≥5 closeout sạch | 2026-05-14 (10 ngày) | 2026-05-15 | runner tự chạy sau closeout |

### 2.3 Cơ chế (mechanism)

| ID | Cơ chế | Status | Trigger | ETA |
|---|---|---|---|---|
| MX-01 | Multi-region experimental preview shadow | Live (V52.5.2) | done | 2026-05-04 ✅ |
| MX-02 | Multi-region test engine | Live (V52.5.3) | done | 2026-05-04 ✅ |
| MX-03 | Multi-region API/UI test_bundle | Live (V52.5.5 + V52.6 source badges) | done | 2026-05-04 ✅ |
| MX-04 | Multi-region daily runner | Live (V52.5.6 manual) | done | 2026-05-04 ✅ |
| MX-05 | Multi-region closeout evaluator | C-03 | sau ≥3 manual closeout | 2026-05-11 |
| MX-06 | Scheduler auto-wire | C-04 | sau MX-05 + ≥5 sạch | 2026-05-15 |
| MX-07 | Strength tensor anchor strict D-1 | Live | done | 2026-05-04 ✅ |
| MX-08 | Anti-leakage cutoff spec MN/MT/MB | Live | done | 2026-05-04 ✅ |
| MX-09 | Source-hash guard mỗi runner | Live | done | 2026-05-04 ✅ |
| MX-10 | Per-method experiment registry | Live (20 entries) | done | 2026-05-04 ✅ |
| MX-11 | Pruning candidate framework | NOT_READY | C-05 latency | 2026-06-15 |
| MX-12 | Production rollback plan template | DESIGN_ONLY | trước Wave 1 | 2026-05-28 |

---

## 3. 4 wave production cải tiến — gate criteria + ETA cụ thể

### 3.1 Wave 1: Single-region single-method swap (earliest 2026-06-15)

Áp dụng nếu 1 method đạt gate trên 1 region.

Gate criteria:
- Method ở pha 4 (`OWNER_REVIEW`).
- `flips_to_win - flips_to_lose ≥ +5` trên ≥30 active picks rolling 30d.
- `false_promotion_rate ≤ 10%`.
- ≥30 ngày VALID_LIVE_DAY (clean degraded-day filter).
- Region-conditional check: nếu method âm ở region khác → swap chỉ áp dụng region thắng.
- Hash guard pre/post identical.
- Rollback plan ký.
- Owner DECISION_LOG entry.

Method có khả năng đạt sớm:
- **MB Composite Challenger V2**: 30d backtest +3, cần thêm sample 30d → +4-5; nếu pattern giữ, ETA 2026-06-03 review.
- **MB AI_CHAIN_PRESERVATION**: 60d 10/10/18, neutral; cần 30d sạch chuyển sang positive.
- **MB STRENGTH_WEIGHTED V52.5.2**: 60d 8/7/19, slight positive; cần 30d sạch hơn.

Chỉ 1 method được apply, KHÔNG combine 2 method khác nhau ở Wave 1.

### 3.2 Wave 2: Region-conditional roster reduction (earliest 2026-06-15 → 2026-07-15)

Cần M-01 (latency) + M-07 (cost) + 30d active per-model BT measurement.

Gate criteria pruning:
- Model BT_rate ≤ 25% trên ≥45 ngày active per region+run_source.
- `unique_useful_signal` ≤ 1 trên 45 ngày.
- `helped_test - hurt_test` âm trên 45 ngày.
- Latency ≥ 60s OR cost ≥ ngân sách approve.
- Test lane chạy ≥7d không có model bị remove, hit-rate không tệ hơn.
- Owner DECISION_LOG.

Cần xác nhận **không loại model toàn cục** vì cùng model có thể strong region khác (ví dụ `claude-sonnet-4-6` weak MB ai_chain helpful 0.28 nhưng MN auto_daily helpful 0.563).

ETA pruning earliest: **2026-06-15** (Wave 2 review), production deploy earliest **2026-06-30**.

### 3.3 Wave 3: Shadow → production voter promotion (earliest 2026-07-04)

Cần shadow_auto_eval → vote candidate test 30d trước khi production.

Gate criteria:
- Shadow model BT_rate ≥ 40% trên ≥30 ngày active.
- `unique_useful_signal` ≥ 5 (5 ngày shadow đúng mà 14 voter chính sai).
- Latency ≤ 60s.
- Cost/day ≤ ngân sách.
- Test lane chạy ≥7d với shadow → voter, không destructive.
- Owner DECISION_LOG.

Candidate hiện tại theo tensor V52.5.1 (sample mỏng):
- MN `glm-5.1` shadow_auto_eval 18 days BT 11/18 helpful 0.589 — strongest MN shadow.
- MN `arcee-trinity` shadow_auto_eval 2 days BT 2/2 — sample quá mỏng.
- MB `llama-4-maverick` shadow_auto_eval 4 days BT 3/4 — sample quá mỏng.
- MB `mistral-large-3` shadow_auto_eval 4 days BT 3/4 — sample quá mỏng.

ETA earliest sample đủ + active in test lane: **2026-07-04**, production: **2026-08-04**.

### 3.4 Wave 4: Family-aware / region-weekday-aware aggregation (earliest 2026-08-15)

Cần M-09 + M-10 + M-11 (3 method mới) chạy ≥30d test-lane-only sạch.

Gate criteria:
- Method aggregation đạt net +5 trên 30d active rolling vs 6 method hiện có.
- Per-region/per-weekday/per-station không destructive ở bất kỳ axis nào.
- Latency tổng cascade không tăng (vì aggregation chỉ thay đổi voting weight).
- Owner DECISION_LOG.

ETA test lane evidence sạch: **2026-07-15**, owner review: **2026-08-01**, production: **2026-08-15**.

### 3.5 Loz output policy change (earliest 2026-07-01, có thể trễ hơn)

Chờ M-02 loz stage trace + 30d rolling proof region-conditional.

Hiện tại loz `MIXED + REGION_CONDITIONAL`:
- 30d official thắng model-top2 mọi miền.
- 14d MT model-top2 thắng official.

Cần gate criteria:
- Method loz mới đạt LO2_FULL ≥ +5 pp net trên ≥30d 1 region.
- Không destructive region khác.
- M-02 trace cho thấy stage drop cụ thể có thể fix.

ETA: **2026-07-15** earliest.

---

## 4. Lịch trình rõ ràng

| Mốc | Date | Việc | Trạng thái |
|---|---|---|---|
| Now | 2026-05-04 | V52.6 UI source-badge fix shipped | DONE |
| +24h | 2026-05-05 | Quan sát natural live closeout 04/05 với V52.6 UI | observe |
| +3 ngày | 2026-05-07 | Ship C-02 (API source labels) + C-05 (latency instrument) + C-07 (MT correct-but-dropped panel) + C-14 (per-station/weekday strength chip) | next |
| +5 ngày | 2026-05-09 | Đủ 3 manual closeout sạch | gate |
| +7 ngày | 2026-05-11 | Ship C-03 multi-region closeout evaluator + M-02 loz stage trace + M-04 family contribution + M-08 black-spot alert | next |
| +10 ngày | 2026-05-14 | Đủ 5 manual closeout sạch → review C-04 scheduler auto-wire | gate |
| +14 ngày | 2026-05-18 | Ship M-05 station-level loz selector + M-06 output convergence trace; re-evaluate sample của 6 method | review |
| +21 ngày | 2026-05-25 | Ship M-09 family-aware test method | next |
| +25 ngày | 2026-05-29 | Owner review pack draft cho Wave 1 candidates | gate |
| +30 ngày | 2026-06-03 | **Wave 1 owner review window**: Composite V2 / AI_CHAIN MB / SPECIALIST MB / STRENGTH_WEIGHTED MB / PRIOR_REGION MB | OWNER |
| +35 ngày | 2026-06-08 | Ship M-10 region-weekday-aware test method | next |
| +42 ngày | 2026-06-15 | **Wave 2 owner review window**: pruning candidates per region+run_source | OWNER |
| +49 ngày | 2026-06-22 | Ship M-11 station-aware test method | next |
| +60 ngày | 2026-07-04 | **Wave 3 owner review window**: shadow → voter promotion | OWNER |
| +75 ngày | 2026-07-15 | Wave 1/2 production verify after 7d live | review |
| +90 ngày | 2026-07-30 | Wave 3 production verify | review |
| +105 ngày | 2026-08-15 | **Wave 4 owner review window**: family-aware / region-weekday-aware aggregation | OWNER |

Mọi mốc OWNER ở trên là **agent trình evidence pack, không phải auto deploy**. Owner đọc, hỏi, ký OK trong DECISION_LOG.

---

## 5. Agent KHÔNG được làm

- Tự deploy production mà không có DECISION_LOG owner OK.
- Push production change sau 1 ngày live result tốt.
- Promote method khi sample < 14 VALID_LIVE_DAY.
- Drop model production khi `NO_PER_MODEL_DURATION` còn 3273/3273.
- Reuse single_vote_rescue (V37 leaky) hay tier2 V1/V2 (drop_as_designed).
- Auto-wire scheduler V52.5.6 runner trước khi ≥5 closeout thủ công sạch + owner OK.
- Đổi prompt / model roster / scoring / lane weights / verdict weights / output policy / D-2 mà không có evidence pack + owner OK.
- Chỉ dùng MB measurement để justify thay đổi global (cùng model có thể strong MN, weak MB).

---

## 6. Cross-link

- Roadmap luồng thực nghiệm: `docs/EXPERIMENTAL_LANE_ROADMAP_20260504.md`
- V53 controller audit: `artifacts/phase_checkpoints/TOTAL_FORCE_V53_FULL_REPORT_CHAIN_DU_DOAN_TEST_REALITY_AND_SAFE_NEXT_ACTION_20260503.md`
- V52.5 multi-region buildout: `artifacts/phase_checkpoints/V52_5_MULTI_REGION_PARALLEL_TEST_LANE_20260503.md`
- Cutoff spec: `artifacts/phase_checkpoints/V52_4_MN_MT_TEST_LANE_CUTOFF_SPEC_20260503.md`
- Code readiness matrix: `artifacts/_v53_code_readiness_matrix_20260503.md`
- Cross-region leakage initiative: `docs/ACTIVE_ROADMAP_CROSS_REGION_LEAKAGE.md`
- FU items: `docs/FOLLOW_UP_TRACKER.md` FU-073 / FU-114 / FU-115
