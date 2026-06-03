# V10693 — EVIDENCE (số liệu thô đo trên DB hiện tại)

- **DATA AS-OF:** `lottery_results` max date = **2026-06-03**
- **Live sync manifest:** `artifacts/live_sync/20260603_223215/manifest.json`
- **Định nghĩa HIT:** một số 2 chữ số "trúng" nếu nằm trong tập đuôi (2 số cuối) của **mọi giải** trong ngày của miền đó.
- **Cross-check:** định nghĩa HIT của report khớp **30/30** với `final_bundles.bach_thu_status` (WIN/LOSE) hệ thống tự verify cho MB 30 ngày → định nghĩa đúng.

---

## 0. OFFICIAL ZERO-DRIFT (trước & sau verify — chứng minh official KHÔNG đổi)

| Bảng | sha256 (20 ký tự đầu) | rows | Trạng thái |
|---|---|---|---|
| predictions | `6c8b7d1d636810d8aabd` | 6695 | IDENTICAL |
| final_bundles | `7c6b8d4303105da100b0` | 288 | IDENTICAL |
| lottery_results | `c477f9082ccf956ccb53` | 14805 | IDENTICAL |
| model_daily_eval | `569424e8be469e2ace42` | 6559 | IDENTICAL |

→ **OFFICIAL ZERO-DRIFT: PASS** (mọi script trong pha verify chỉ READ; không gọi `generate_final_bundle()`, không ghi `final_bundles`/`predictions`).

---

## 1. RANDOM BASELINE (đuôi unique/ngày → xác suất 1 số trúng ngẫu nhiên), 30 ngày

| Miền | Đuôi unique TB/ngày | Random 1-số HIT |
|---|---|---|
| MB | 23.7 / 100 | **~23.7%** |
| MN | 42.4 / 100 | ~42.4% |
| MT | 34.8 / 100 | ~34.8% |

(MB chỉ 1 đài/ngày → tập đuôi nhỏ nhất → baseline thấp nhất.)

---

## 2. V7 — PER-POSITION + XIÊN (OFFICIAL, đo trên DB hiện tại)

`top1=bạch thủ`, `top2=số phụ 1 (số thứ 2 của lô-2-số)`, `top3=số phụ 2 (số mới trong xiên3)`.

| Miền | Cửa sổ | n | top1 | top2 | top3 | xiên2 | xiên3 | cover top-N |
|---|---|---|---|---|---|---|---|---|
| **MB** | 7d | 7 | 0.0% | 0.0% | 14.3% | 0.0% | 0.0% | 14.3% |
| **MB** | 14d | 14 | 7.1% | 14.3% | 14.3% | 7.1% | 0.0% | 28.6% |
| **MB** | 30d | 30 | **6.7%** | 20.0% | 20.0% | 3.3% | 0.0% | 43.3% |
| **MB** | 60d | 60 | 13.3% | 23.3% | 22.8% | 5.0% | 1.7% | 45.0% |
| MN | 30d | 30 | 36.7% | 26.7% | 31.0% | 6.7% | 3.3% | 66.7% |
| MN | 60d | 60 | 48.3% | 43.3% | 41.1% | 20.0% | 11.7% | 78.3% |
| MT | 30d | 30 | 40.0% | 43.3% | 50.0% | 13.3% | 6.7% | 80.0% |
| MT | 60d | 60 | 36.7% | 46.7% | 42.9% | 15.0% | 6.7% | 76.7% |

**So với random baseline:** MB top1 30d = 6.7% so với random 23.7% → **dưới ngẫu nhiên ~3.5 lần**. MB 7 ngày gần nhất bạch thủ **trượt 0/7**. MT trên baseline ở mọi vị trí (thực sự tốt); MN quanh/dưới baseline; MB tệ nhất hệ thống.

`xiên4` official = **N/A** (official chỉ xuất tới top3/xiên3, không có top4).

---

## 3. V7 — LANE-TEST MB (mb_experimental_preview_shadow, 30d)

| Nhánh | n | top1 | top2 | top3 | x2 | x3 | x4 | covN |
|---|---|---|---|---|---|---|---|---|
| MB_OFFICIAL_BASELINE_CONTROL | 30 | 6.7% | 20.0% | 20.0% | 3.3% | 0.0% | 0.0% | 63.3% |
| MB_AI_CHAIN_PRESERVATION_V1 | 30 | 6.7% | 20.0% | 20.0% | 3.3% | 0.0% | 0.0% | 63.3% |
| MB_COMPOSITE_CHALLENGER_V2 | 30 | 6.7% | 20.0% | 20.0% | 3.3% | 0.0% | 0.0% | 63.3% |
| MB_NO_TOKEN_HERD_REDUCTION_V1 | 30 | 6.7% | 20.0% | 20.0% | 3.3% | 0.0% | 0.0% | 63.3% |
| MB_PRIOR_REGION_CONTEXT_SAFE_V1 | 30 | 6.7% | 20.0% | 20.0% | 3.3% | 0.0% | 0.0% | 63.3% |
| MB_SPECIALIST_ROSTER_V1 | 30 | 6.7% | 20.0% | 20.0% | 3.3% | 0.0% | 0.0% | 63.3% |
| MB_TIER_AWARE_BUNDLE_SHADOW_V1 | 30 | 6.7% | 20.0% | 20.0% | 3.3% | 0.0% | 0.0% | 63.3% |

→ **7/7 nhánh GIỐNG HỆT control** (cùng top1/2/3). Lane hiện **CHƯA phân hoá** — các "experiment" đang clone official, chưa test cải tiến MB thực sự.

---

## 4. V3 CEILING — tín hiệu tồn tại vs cái bundle chốt được (30d)

| Miền | Official BT (đang chạy) | Plurality model-top1 (đồng thuận đơn giản) | ANY model top1 hit (trần lỏng 27 pick) | Plurality top-3 set cover |
|---|---|---|---|---|
| **MB** | **6.7%** [2/30] | **10.0%** [3/30] | 90.0% [27/30] | 33.3% [10/30] |
| MN | 36.7% [11/30] | 50.0% [15/30] | 93.3% [28/30] | 80.0% [24/30] |
| MT | 40.0% [12/30] | 33.3% [10/30] | 100% [30/30] | 73.3% [22/30] |

**Phát hiện cốt lõi:** MB **plurality consensus 10.0% < random 23.7%** → đồng thuận model MB **phản tác dụng** (herd vào số SAI). Ngược lại MN plurality 50% > random 42% (đồng thuận giúp ích). Vì `d_w06` khuếch đại đồng thuận → MB BT 6.7% (tệ hơn cả plurality).

---

## 5. V1 — BUDGET MB LANE (du_doan_test_model_budget_daily, 7 ngày)

| date | region | total | measured | SELECTED | watch | skip | control | target_max |
|---|---|---|---|---|---|---|---|---|
| 2026-06-03 | MB | 29 | 24 | **20** | 6 | 3 | 4 | 20 |
| 2026-06-02 | MB | 29 | 23 | **20** | 6 | 3 | 4 | 20 |
| 2026-06-01 | MB | 29 | 23 | **20** | 6 | 3 | 4 | 20 |
| 2026-05-31 | MB | 29 | 23 | **20** | 6 | 3 | 4 | 20 |
| … | MB | 29 | 23-24 | **20** | 6 | 3 | 4 | 20 |

→ MB lane **đạt 20/20 SELECTED mọi ngày** (báo cũ "5/20 PREVIEW_BELOW_BUDGET" đã LỖI THỜI, đã được adaptive budget selector `c16_adaptive_model_budget_v1` khắc phục).

**Nhưng** 20 voter MB bị phạt cấu trúc (tần suất tag lý do, 7d):
- `MB_AI_STRUCTURAL_PENALTY` × 168
- `HERD_PENALTY` × 128
- `HURT_GT_HELP` × 112
- `NEUTRAL` × 64

MB skip_reason (14d): `LOW_BUCKET_SCORE` × 30, `NO_BUCKET_SAMPLE_OR_PREDICTION` × 15.

→ Budget đầy nhưng lấp bằng model **bị gắn cờ HURT_GT_HELP** (hại nhiều hơn lợi). Vấn đề là CHẤT LƯỢNG, không phải SỐ LƯỢNG.

---

## 6. V2 — SOURCE POOL / INJECTION (MB, 30d)

**Drop-stage (candidate_drop_stage_daily, MB 28 ngày):**

| drop_stage | số ngày |
|---|---|
| **BUNDLE_SKEW** | **17** |
| PROMPT_NOT_INJECTED | 6 |
| SOURCE_POOL_MISS | 1 |
| SECONDARY_ONLY_SIGNAL | 1 |
| UPSTREAM_MISS | 1 |
| CANDIDATE_SPLIT | 1 |
| NO_GAP | 1 |

`BUNDLE_SKEW` reason = `actual_main_candidate_existed_but_bundle...` (số trúng CÓ trong vote model nhưng bundle chốt số khác). Ví dụ:
- 2026-05-23: top1hitN=**18** (18 model trúng top1) nhưng bundle chốt 91 → LOSE.
- 2026-05-27: top1hitN=7, bundle chốt 08 → LOSE.
- 2026-05-30: top1hitN=6, bundle chốt 63 → LOSE.

**Injection class (v104_shadow_prompt_candidate_injection, MB 30d):**
- `injection_class`: `OPTIONAL_REVIEW` × 126 — **REQUIRED_IN_PROMPT = 0**
- `gate_class_from_v103`: `REVIEW` × 126

→ **0 candidate nào của MB được ép vào prompt (REQUIRED)**. Toàn bộ chỉ "review tuỳ chọn".

**Source pool (v101 evidence, MB 30d):** `SOURCE_READY` × 2572, `WAITING_MN` × 69. Số đuôi ứng viên riêng biệt theo nguồn: MT(D-1)=99, MN(D)=98, MN(D-1)=98, MT(D)=97, MB(D-1)=95.

→ Nguồn ĐÃ được gom đầy đủ (95-99 đuôi/nguồn) ở tầng shadow, nhưng `v104 REQUIRED_IN_PROMPT=0` nghĩa là **không có cơ chế ép tín hiệu nguồn mạnh (MN(D)/MT(D) same-day) vào prompt** → AI không "nhìn thấy" buộc phải dùng.

---

## 7. V6 — TRACEABILITY (VPS vs private git)

- **VPS git head:** `94242fb` (2026-06-03 13:44) "feat(V10680) Lane test TOP-K strength-filtered D_w06 per-region", branch `master`.
- **Local private head:** `c187370` (2026-06-03 21:40) "docs ROADMAP_POST_LIVE_T4 handoff".
- **VPS có thay đổi CHƯA commit (file đang chạy đi TRƯỚC git):**
  - `main.py` mtime 2026-06-03 15:49 > git commit 2026-05-31 20:20 → **ahead**
  - `web/frontend/du-doan-test.html` (M), `_v10679/_v10680/_v10692_*` lane (M/A), docs (M/A)
- **Service:** `lottery` active từ 2026-06-03 21:39.

→ Báo cũ "VPS=V17.19.4" đã lỗi thời; head VPS hiện `94242fb`. **Có drift runtime-ahead-of-git** (main.py + frontend + lane files sửa trên VPS chưa commit) — cần đồng bộ/commit để bảo toàn truy vết.

---

## 8. V5 — OBSERVABILITY / ISOLATION (kết quả đọc code)

- `MAIN_TEST_EQUALS_OFFICIAL` được tính trong `main.py` (`_v10519_lane_contract_for_region`, ~13481) và lộ qua **admin API** `/api/admin/test-lane-readiness`, `/api/admin/test-lane-diff-vs-official`.
- Trang `/du-doan-test` **đã có sẵn UI render marker** (du-doan-test.html ~1935) nhưng `loadPreview()` chỉ gọi `/api/du-doan-test/{region}` — endpoint này **KHÔNG set `clone_warning`** → marker đỏ thường không hiện (chỉ banner vàng `primary_differs_from_baseline_bt`).
- Isolation **được enforce trong code:** hard-contract trong `_du_doan_test_engine.py`, `_du_doan_test_mb_engine.py`, `_du_doan_test_daily_runner.py`; `source_hash_snapshot()` + `official_tables_changed()` (schema). Lane chỉ ghi `du_doan_test_*` + `*_experimental_preview_shadow`.

→ Cần wire `clone_warning` vào response `/api/du-doan-test/*` để marker hiển thị đúng trên UI lane test.
