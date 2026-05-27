# V106.36 FULL DEBT CLOSEOUT + REGION-INDEPENDENT LANE EXECUTION

- Phiên bản: V106.36
- Thời gian: 2026-05-27 (Thứ Tư) — báo cáo report-only
- Phạm vi: kiểm 3 miền 1 ngày, đóng sổ tồn đọng V1.0 → V106.35, dựng tier-gate Rule105, dry-run lane-test 3 miền, audit UI/API, drift-proof, public-safe report.

> Public-safe. Không có code private, không có DB rows, không có provider key, không có chi tiết VPS. Tất cả số liệu là tổng hợp sau audit read-only.

## 1. Tình hình hôm nay 2026-05-27 (Wed weekday=2)

| Miền | BT chính thức | Trạng thái | Strongest candidate | Drop stage |
|---|---|---|---|---|
| MN | 58 | **WIN** | 58 (support=14) | NO_GAP |
| MT | 77 | LOSE | 56 (support=29, hit thực tế) | BUNDLE_SKEW |
| MB | 08 | LOSE | 13 (support=14, hit thực tế) | BUNDLE_SKEW |

- MN thắng "đúng người, đúng cuộc": strongest candidate = official BT = 58.
- MT/MB strongest candidate đã chạm tail thực, nhưng bundle chọn BT khác → **selector_gap / bundle_skew xác nhận lại**.

## 2. Đơn model 30 ngày

| Miền | Nhánh | BT hit rate | Đóng góp ngày thắng | Nhận xét |
|---|---|---|---|---|
| MN | AI-token | 46% | 27% | Đáng giá nhất, giữ nguyên |
| MN | No-token | 33% | 12% | Hỗ trợ baseline |
| MT | AI-token | 32% | 1.4% | Hit cao nhưng selector gap |
| MT | No-token | 45% | 41% | Baseline thực sự đáng tin |
| MT | Combo | 47% | 64% | **Phương thức số 1** của MT |
| MB | AI-token | 20% | 4.4% | **Cost-waste candidate** |
| MB | No-token | 26% | 33% | **Tốt hơn AI-token** ở MB |
| MB | Combo | 16% | 25% | Yếu hơn cả no-token |

## 3. Cohere

- 30 ngày qua: MN/MT/MB đều `helped=0, hurt=0, no_effect>=29/30 rows`.
- `bt_changed_rate` 3-10% nhưng mọi thay đổi đều trung tính.
- Verdict: **COHERE_NO_EFFECT_DOMINANT_30d** ở cả 3 miền.
- Khuyến nghị: chuyển sang `diagnostic_only` trong lane-test (V10637). Không gỡ khỏi production khi chưa có owner approve.

## 4. 105 Rules - phân tier mới (V10636)

| Miền | TIER_A (lane-test) | TIER_B (shadow only) | TIER_C (reject) |
|---|---|---|---|
| MN | **26** | 9 | 0 |
| MT | **18** | 14 | 3 |
| MB | **4** | 26 | 5 |

- 4w là window đỉnh cho 67-71% rule nhưng cũng nhiễu nhất → dampener yêu cầu 12w/16w stable confirmation.
- MN có TIER_A bao phủ 6/7 ngày trong tuần (thiếu Sun).
- MT có TIER_A bao phủ 6/7 ngày trong tuần (thiếu Wed).
- MB chỉ có TIER_A bao phủ 3/7 ngày trong tuần (thiếu Tue/Wed/Thu/Sat).

## 5. Lane-test dry-run hôm nay

| Miền | Rules eligible | Lane BT | Lane vs Official BT | Lane hit DB |
|---|---|---|---|---|
| MN | 5 | 39 | khác (Official=58 WIN) | 0 |
| MT | 0 | - | - | - |
| MB | 0 | - | - | - |

- MN lane chọn 39 (false consensus từ 4 rule cùng Quảng Ninh G7-family → cùng 4 tail). Lane TỆ HƠN official today.
- MT/MB chưa có TIER_A rule trên Wed → lane không có signal → cần re-mine.

## 6. MB AI-token cost-value (P0)

- 30d: bt_hit_rate 20.4% (ngang baseline ~21%); contribution_to_winning **4.4%** (2/45 ngày thắng).
- Latency trung bình 107 giây/call × 16 models = ~28 phút/ngày tính-toán AI-token.
- **LANE_FREEZE_CANDIDATE** — cần owner OK để limit/freeze trong shadow/lane (KHÔNG đụng production trong V106.36).

## 7. UI/API/Board

- `/monitoring` 401 đúng thiết kế (admin auth).
- `/app`, `/du-doan` 200 OK với placeholder loading qua JS.
- `/accuracy`, `/du-doan-test`, `/api/prediction-quality`, `/api/final-bundle?region=MN` timeout qua HTTP probe (không có JS).
- Probe tĩnh không kết luận STALE; cần owner mở browser sáng mai để smoke.
- Board deploy: **OWNER_GATE_REQUIRED**; KHÔNG deploy trong V106.36.

## 8. Tồn đọng V1.0 → V106.35

| Severity | Số issue |
|---|---|
| P0 | 3 |
| P_LOCK / P_GUARD | 3 |
| P1 | 10 |
| P2 | 1 |
| CLOSED | 2 |

P0 issues:
- `MT-CONVERSION-GATE` — wire vào MT_CONVERSION_GATE_LANE_V1 trong V10637.
- `MB-COST-WASTE-AI-TOKEN` — owner OK để limit/freeze trong shadow.
- `MB-WEEKDAY-COVERAGE-GAP` — re-mine để có TIER_A trên Tue/Wed/Thu/Sat.

## 9. Action tối nay

- Đã build artifact đầy đủ (35+ files).
- Đã verify SSOT pointer alignment (public=private=V106.35).
- Đã fresh sync DB (sync_completed 22:46 VN).
- Đã drift-proof: DB sha256 không đổi, prediction trace sha256 không đổi, không có row count thay đổi.

## 10. Action ngày mai (2026-05-28)

| Ưu tiên | Việc |
|---|---|
| P0 | Owner smoke `/du-doan`, `/accuracy`, `/api/*` qua browser. |
| P0 | Owner quyết định MB AI-token freeze/limit gate. |
| P1 | Implement `web/backend/lane/_v10636_rule105_query.py` (chỉ lane-test). |
| P1 | Implement MN false_consensus dampener (unique_source_evidence). |
| P1 | Implement MT conversion-gate dampener (boost_dominance_cap). |
| P1 | Re-mine MB rules để mở rộng TIER_A weekday coverage. |
| P2 | Forward audit 71 pre-register rules (weekly snapshot bắt đầu 2026-06-01). |

## 11. Safety proof

- `official_mutation`: **false**
- `provider_call_count`: **0**
- `wallet`: **0**
- `lane_promotion`: **false**
- `mined_rules_official_import`: **false**
- `production_prompt_switch`: **false**
- `production_selector/scoring/voting/roster_switch`: **false**
- `v10628r1_run`: **false**
- `cron_install`: **false**
- `deploy` (any kind): **false**
- `public_code_deploy`: **false**
- `cross_region_contamination`: **0**
- `drift_detected`: **false** (DB + trace sha256 unchanged pre/post)

## 12. Owner decisions còn lại

| Quyết định | Tác động nếu OK | Default nếu không quyết |
|---|---|---|
| Limit/freeze MB AI-token trong shadow | Tiết kiệm ~28 phút compute/day; preserve no-token baseline | Tiếp tục không thay đổi |
| Deploy admin-only read-only board | Có dashboard real-time cho 3 miền | Tiếp tục artifact-only |
| Implement V10637 lane helpers (no official touch) | Có lane V1 cho 3 miền cho V10638+ | Tiếp tục report-only |
| Accept V10635 MB GĐB D-2 NOT_VALIDATED | Đóng debt path đó | Đóng mặc định |

---

V106.36 không claim ACCURACY_READY / OFFICIAL_IMPROVED / SELECTOR_FIXED / MN_FIXED / MT_FIXED / MB_FIXED / LANE_TEST_PROMOTED. Đây là pass forensic + decision-board + ledger, KHÔNG phải pass cải tiến production.
