# V10683 — Plan: đảo T2 ↔ T1 trong lane test (`/du-doan-test`) MB-only

> **Generated**: 2026-06-03 01:50 VN
> **Trigger**: Owner: "hệ thống đang chạy T1 trước giờ rồi mà, anh nghĩ nên đảo ở lane test luôn đi".
> **Trạng thái**: PLAN-ONLY. Chưa code, chưa deploy. Owner OK rồi mới làm.
> **Scope**: CHỈ `/du-doan-test`. Official path KHÔNG đụng.

---

## 0. Owner correction & cấu trúc đúng

| Quan niệm cũ (em hiểu nhầm) | Thực tế owner xác nhận |
|---|---|
| Coi như T1 chưa drive, đề xuất "giữ nguyên" | Sai — production đang drive T1 (35 MB rules trong `mined_rules`) từ trước qua `extract_rule_candidates_v2` + `final_bundle.number_scores` |
| Đảo hoàn toàn = rủi ro | Đúng cho official, NHƯNG `/du-doan-test` chính là nơi để thử nghiệm safe |

→ Đảo T2 ↔ T1 trên **lane test** đúng là cách dùng đúng của lane test.

---

## 1. Lane test MB hiện tại đang làm gì?

### 1.1 Schema registry: 10 experiment MB đã đăng ký

Trong `web/backend/_du_doan_test_schema.py`:

```
MB_OFFICIAL_BASELINE_CONTROL    — clone official (control)
MB_COMPOSITE_CHALLENGER_V2
MB_ADAPTIVE_BUDGET_SELECTOR_V1
MB_CONSENSUS_V1
MB_ADAPTIVE_EXPLOIT_V1          — V67 lag-1 exploit
MB_TIER_AWARE_BUNDLE_SHADOW_V1
MB_AI_CHAIN_PRESERVATION_V1
MB_SPECIALIST_ROSTER_V1
MB_PRIOR_REGION_CONTEXT_SAFE_V1
MB_NO_TOKEN_HERD_REDUCTION_V1
```

### 1.2 Cách 7 experiment hiện chạy chọn BT

Materializer `_materialize_mb_experimental_preview_shadow.py` đọc:
- `candidates` pool: list các tail (`number_scores`) đã được production T1 chấm
- Mỗi experiment chọn TOP 1 từ pool theo logic riêng (composite, tier-aware, AI-chain, specialist, prior-region, no-token-herd…)

→ **TẤT CẢ 7 experiment dùng cùng 1 score base do T1 sinh.** Không có experiment nào tính lại score bằng T2.

### 1.3 Hard contract đã có

Materializer ghi rõ:

```
- Does NOT call generate_final_bundle().
- Does NOT write final_bundles.
- Does NOT write production predictions.
- Uses only live-available selection inputs.
- Writes diagnostic-only rows to mb_experimental_preview_shadow.
```

Engine `_du_doan_test_mb_engine.py` cũng có hard contract tương đương cho `du_doan_test_*`.

---

## 2. Đề xuất: thêm experiment `MB_T2_MANUAL_DRIVE_SHADOW_V1`

### 2.1 Mục tiêu

Tính lại score từng candidate trên cùng list models nhưng **dùng T2 axes** (77 manual MB-target rules) thay vì T1 axes → chọn TOP 1 → so với `MB_OFFICIAL_BASELINE_CONTROL` 30 ngày.

### 2.2 Thuật toán

Cho ngày `D` weekday `wd`:

1. Lấy `candidates` pool như các experiment khác (live-available, không đụng official).
2. Lấy 8-12 T2 manual rule MB-target cho `wd` từ `mb_t2_manual_daily` (snapshot mới nhất).
3. Với mỗi candidate `c` (tail 2 chữ số):
   - `t2_score = 0`
   - Với mỗi T2 rule `r`:
     - Lấy source data MB ngày `D + lag(r)` từ `lottery_results` (giữ guard temporal).
     - Áp transform `r.transform` (LAST2 / FIRST2 / HEAD_TAIL / P3P2 / P4P1 / TAIL_HEAD / LAST2_REV / ...) → tail set.
     - Nếu `c.tail` ∈ tail set → cộng boost = `r.composite × multiplier_table[r.lifecycle]`.
4. Chọn `c*` có `t2_score` cao nhất; tie-break theo `c.score` (model votes) rồi rank.
5. Ghi `(MB_T2_MANUAL_DRIVE_SHADOW_V1, c*.tail)` vào `mb_experimental_preview_shadow`.

### 2.3 Multiplier table theo lifecycle T2

```
MANH:        1.00
TANG_TRUONG: 1.05
ON_DINH:     1.00
XUONG_CAP:   0.85
YEU:         0.70
```

(Đồng nhất với T1 weight-mult đã định trong `mb_rule_ranker.LIFECYCLE_WEIGHT`.)

### 2.4 Temporal guard

T2 rules có `source_lag` (D, D-1, D-2 …). Áp đúng quy tắc thứ tự xổ:
- MN(D) hợp lệ nguồn vào MB
- MT(D) hợp lệ nguồn vào MB
- MB(D) KHÔNG (MB tự xổ cuối)

Đã được verify ở V10681 — temporal causality 0 vi phạm trong T2 store.

---

## 3. Mở rộng: 2 experiment phụ tùy ý

| Experiment | Mục tiêu |
|---|---|
| `MB_T2_BHPASS_ONLY_DRIVE_SHADOW_V1` | Chỉ 5 BH-pass T2 drive (gold standard, conservative) |
| `MB_T2_MANUAL_BLEND_T1_T2_SHADOW_V1` | Blend `0.7 × T1_score + 0.3 × T2_score` (giữ T1 chính, T2 phụ) |

Owner chốt: chỉ thử 1 hay cả 3?

---

## 4. Code changes cần thiết (chưa làm)

### 4.1 File mới (không đụng materializer cũ)

```
web/backend/_v10683_mb_t2_drive_shadow.py
```

- Tự đọc `lottery_results`, `mb_t2_manual_daily`.
- Tính `t2_score` per candidate.
- Ghi `mb_experimental_preview_shadow` row mới (đúng schema, hard contract).
- CLI: `python _v10683_mb_t2_drive_shadow.py --date YYYY-MM-DD --backfill-days 30`.

### 4.2 Đăng ký experiment

Sửa `_du_doan_test_schema.py` block REGISTRY:

```python
{
    "experiment_name": "MB_T2_MANUAL_DRIVE_SHADOW_V1",
    "region": "MB",
    "status": "SHADOW",
    "method_family": "manual_rule_drive",
    "description": "T2 manual MB-target rules (77) drive replacement for T1 production.",
    "input_sources": "lottery_results, mb_t2_manual_daily, mb_experimental_preview_shadow",
    "allowed_live_sources": "MN(D), MT(D), MB(D-N)",
    "forbidden_sources": "official mined_rules, final_bundles",
    "uses_ai_prompt": False,
    "uses_no_token": False,
    "uses_prior_region": True,
    "uses_shadow": True,
    "uses_replay": False,
    "uses_tensor": False,
    "realtime_eligible": False,
    "diagnostic_only": True,
    "notes": "V10683 owner-asked T1↔T2 swap test.",
}
```

### 4.3 Cron đăng ký

Thêm 1 job vào `scheduler.py`:

```python
# 23:50 — sau 23:35 V66 + 23:40 V67 + 23:45 V70 + 23:48 V71
_scheduler.add_job(
    _run_v10683_mb_t2_drive_shadow,
    CronTrigger(hour=23, minute=50, timezone=VN_TZ),
    id="mb_t2_drive_shadow_materializer",
    name="MB T2 Manual Drive Shadow (23:50)",
    replace_existing=True,
)
```

### 4.4 Engine downstream

`_du_doan_test_mb_engine.py` ĐÃ tự động đọc tất cả experiments trong `mb_experimental_preview_shadow` qua `_preview_rows()` — chỉ cần thêm experiment vào `ORDER BY` mapping (rank 7) hoặc để fallback `ELSE 99`.

---

## 5. Hard contract preserved

| Thứ | Chạm? |
|---|---|
| `mined_rules` (production T1) | NO |
| `final_bundles` | NO |
| `predictions` (production) | NO |
| `extract_rule_candidates_v2` runtime path | NO |
| `lottery_results` | READ-ONLY |
| MN/MT path | NO |
| `mb_experimental_preview_shadow` | WRITE (thêm row experiment mới) |
| `du_doan_test_*` | tự động qua engine |

---

## 6. Acceptance criteria 30 ngày

So sánh `MB_T2_MANUAL_DRIVE_SHADOW_V1` vs `MB_OFFICIAL_BASELINE_CONTROL`:

| Metric | Ngưỡng PASS | Ngưỡng FAIL |
|---|---|---|
| `would_flip_baseline_to_win` | ≥ 8/30 ngày | ≤ 3/30 |
| `would_flip_baseline_to_lose` (false promotion) | ≤ 5/30 | > 8/30 |
| Δ BT hit-rate vs control | +5 pp trở lên | < +2 pp hoặc âm |
| sample n_lose ≥ 30 | đủ | thiếu |

Nếu PASS → owner cân nhắc PHƯƠNG ÁN 2 chính thức (curated subset T2 vào dual-drive với multiplier nhỏ trong official, sau forward audit closeout 31/08).

Nếu FAIL → drop experiment, giữ T1 drive như hiện tại.

---

## 7. Verify checklist trước khi deploy

| Check | Tool |
|---|---|
| py_compile file mới | `python -m py_compile` |
| ReadLints 0 errors | `ReadLints` |
| MN/MT invariance 108/108 | `_mn_mt_invariance_harness.py check` |
| Full verify suite 54/54 | `_vf_full_verify.py` |
| Temporal causality T2 store | `_audit_tier3_origin.py` (đã verify) |
| Backfill 30d dry-run | `--backfill-days 30 --dry-run` |
| 4 official tables hash IDENTICAL | pre/post hash check |
| `mined_rules` row count IDENTICAL | pre/post |
| Service health post-deploy | `/login`, `/api/health` 200 |

---

## 8. Pha tiếp + dependencies

| Pre-requisite | Trạng thái |
|---|---|
| T2 rolling re-measure (V10684 sắp viết) | CHƯA. T2 đo 1 lần. Pre-condition QUAN TRỌNG vì shadow 30d cần dữ liệu T2 luôn cập nhật. |
| `mb_t2_manual_daily` đã chạy | OK (V10681 verify) |
| `mb_experimental_preview_shadow` schema | OK |
| Owner OK plan này | AWAITING |

---

## 9. Câu hỏi cần owner chốt

1. **Phương án experiment**: chỉ `MB_T2_MANUAL_DRIVE_SHADOW_V1` (tất cả 77 T2 drive), hay thêm `MB_T2_BHPASS_ONLY_DRIVE_SHADOW_V1` (5 BH-pass), hay thêm `MB_T2_MANUAL_BLEND_T1_T2_SHADOW_V1` (blend 0.7/0.3)?

2. **Pre-requisite**: có cần em viết V10684 = job rolling re-measure 73 T2 trước, để dữ liệu T2 luôn fresh trong 30d shadow? (Đề xuất: CÓ, làm trước experiment 1 tuần.)

3. **Ngưỡng PASS/FAIL**: anh đồng ý ngưỡng đề xuất ở §6 hay muốn chỉnh?

---

## 10. Trạng thái

| Hạng mục | Status |
|---|---|
| Code mới | CHƯA viết |
| Code deploy | NO |
| Official mutation | NO |
| Public report (file này) | sẽ push GitHub |
| Local files đã sửa V10681/82 | giữ nguyên, KHÔNG đụng thêm |
| MN/MT bất biến | PROVEN 108/108 |
| Owner OK plan V10683 | AWAITING |

**Bottom line**: lane test là chỗ đúng để thử đảo T2 ↔ T1. Em đã xác nhận lane test MB hiện CHƯA có experiment nào dùng T2 drive. Cần thêm experiment mới + pre-requisite rolling re-measure. KHÔNG deploy gì cho tới khi anh chốt phương án.
