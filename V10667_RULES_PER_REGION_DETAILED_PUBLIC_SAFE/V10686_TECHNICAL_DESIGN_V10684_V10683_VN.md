# V10686 — Technical design V10684 (rolling re-measure) + V10683 (3 shadow experiments)

> **Generated**: 2026-06-03 02:10 VN
> **Trigger**: Owner đã chốt 3 quyết định: D (cả 3 experiment) + V10684 trước 1 tuần OK + ngưỡng PASS/FAIL OK.
> **Trạng thái**: REPORT-ONLY. Design xong, **CHƯA code**, **CHƯA deploy**. Owner OK "code đi" thì em mới viết file.
> **Naming**: V10685 đã rename — chỉ dùng PROD/MANUAL/PREREG, không còn T1/T2/T3.

---

## 0. Owner decisions — chốt

| # | Quyết định |
|---|---|
| 1 | Phương án **D**: code cả 3 experiment trong `/du-doan-test` |
| 2 | Pre-requisite V10684 rolling re-measure 77 MANUAL trước experiment 1 tuần — **OK** |
| 3 | Ngưỡng 30d: would_flip_to_win ≥ 8/30, false_promotion ≤ 5/30, ΔBT ≥ +5pp, n_lose ≥ 30 — **OK** |

---

## 1. Lịch trình

```
NGAY (V10686)        report-only design + push GitHub (file này)
            ↓ owner OK "code đi"
V10684 build         _v10684_mb_manual_rolling_remeasure.py + schema + backfill 90d
            ↓ verify local 55/55 + isolation 18/18 + 108/108
+1 tuần              data rolling đủ tươi (snapshot daily)
            ↓
V10683 build         _v10683_mb_manual_drive_shadow.py + 3 chooser + register 3 experiments
            ↓ verify local
            ↓ owner OK deploy VPS
DEPLOY               cron V10684 20:25 + cron V10683 23:50
            ↓ 30 ngày
EVIDENCE PACK        đo 4 ngưỡng → owner promote vào official hoặc drop
```

---

## 2. V10684 — Rolling re-measure 77 MANUAL rules

### 2.1 Mục tiêu

77 rule MANUAL hiện đo MỘT lần khi V10667 đào — sau đó không cập nhật. V10684 đo lại mỗi ngày trên `lottery_results` mới nhất → có lift_pp / hit_rate / half_stable / lifecycle ĐỘNG đúng theo thời gian.

### 2.2 Schema mới

```sql
CREATE TABLE IF NOT EXISTS mb_manual_rolling_eval (
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    eval_date       TEXT NOT NULL,
    rule_lineage    TEXT NOT NULL,           -- "MN:DB#1:D"
    transform       TEXT NOT NULL,           -- LAST2 / FIRST2 / HEAD_TAIL / P3P2 / P4P1 / TAIL_HEAD / LAST2_REV
    target_weekday  TEXT NOT NULL,           -- T2/T3/T4/T5/T6/T7/CN
    source_artifact TEXT,                    -- V10667 / V10636-DIG / V10636-LAGS

    -- Rolling stats
    n_eval_30d      INTEGER, hit_rate_30d  REAL, lift_pp_30d  REAL,
    n_eval_60d      INTEGER, hit_rate_60d  REAL, lift_pp_60d  REAL,
    n_eval_90d      INTEGER, hit_rate_90d  REAL, lift_pp_90d  REAL,

    -- Stability
    half_stable      INTEGER,                -- 0/1/2 (split-half lift ≥ 3pp count)
    first_half_lift  REAL,
    second_half_lift REAL,

    -- Lifecycle (V10685 naming)
    lifecycle        TEXT,                   -- MANH / TANG_TRUONG / ON_DINH / XUONG_CAP / YEU
    handling         TEXT,                   -- weight_mult description

    -- Quality flags
    n_eval_total     INTEGER,
    significant      INTEGER,                -- 1 if BH-pass or p<.01 historical
    notes            TEXT,
    created_at       TEXT DEFAULT CURRENT_TIMESTAMP,

    UNIQUE(eval_date, rule_lineage, transform, target_weekday)
);

CREATE INDEX IF NOT EXISTS idx_mb_manual_rolling_lookup
    ON mb_manual_rolling_eval (eval_date, target_weekday, rule_lineage);
```

### 2.3 Function signatures

```python
def run_rolling_remeasure(eval_date: str, force: bool = False) -> dict:
    """Re-measure 77 MANUAL rules on lottery_results up to eval_date.

    Steps:
      1. Load 77 manual rules from V10667 + V10636-DIG/LAGS (same as mb_rule_ranker._rerank_tier2)
      2. For each rule:
         a. Resolve source draws over the past 90 days where target weekday matches
         b. Apply transform (LAST2/FIRST2/HEAD_TAIL/P3P2/P4P1/TAIL_HEAD/LAST2_REV) to source
         c. Compare against MB target draws same target_weekday
         d. Compute hit_rate / lift_pp at 30d / 60d / 90d windows
         e. Compute half_stable (split sample halves; lift ≥3pp in BOTH → 1)
         f. Determine lifecycle (V10685 5 nhãn) using DYNAMIC stats
      3. INSERT OR REPLACE into mb_manual_rolling_eval
      4. Update mb_t2_manual_daily.lifecycle (only) for backwards compat
    Returns: {'status', 'eval_date', 'n_rules', 'lifecycle_dist', ...}
    """
```

```python
def backfill_rolling_remeasure(start_date: str, end_date: str) -> dict:
    """Backfill rolling re-measure across a date range. Used for one-shot 30d/60d/90d catch-up."""
```

### 2.4 Cron đề xuất

| Giờ VN | Job | Lý do |
|---|---|---|
| 20:25 | `_run_v10684_manual_rolling_remeasure` | Sau MRE 20:15 (data tươi nhất), trước MB ranker 20:30 (để PROD ranker đọc lifecycle MANUAL mới) |

### 2.5 Hard contract

- Đọc: `lottery_results`, `mb_t2_manual_daily`, V10667/V10636 artifact JSON.
- Ghi: `mb_manual_rolling_eval` (mới) + UPDATE `mb_t2_manual_daily.lifecycle` (cột đã tồn tại).
- KHÔNG đụng: `mined_rules`, `predictions`, `final_bundles`, `lottery_results`, `model_daily_eval`.

---

## 3. V10683 — 3 shadow experiments

### 3.1 Three chooser functions

```python
def _choose_manual_drive(candidates, manual_rules_for_wd) -> tuple:
    """Top1 by manual_score (sum of boosts from 77 MANUAL rules matching tail).

    For each candidate tail c.tail:
      manual_score(c) = sum_over_rules(
        (c.tail in apply_transform(rule.transform, source_draws_at_lag(rule.lag)))
          * rule.composite * LIFECYCLE_WEIGHT[rule.lifecycle]
      )
    Tie-break: candidate's existing model-vote score, then rank.
    """
```

```python
def _choose_manual_bhpass_drive(candidates, manual_bhpass_only) -> tuple:
    """Top1 by manual_score using ONLY 5 BH-pass MANUAL rules (gold standard subset)."""
```

```python
def _choose_blend_prod_manual(candidates, prod_score_map, manual_score_map) -> tuple:
    """Top1 by 0.7 * normalised_prod_score + 0.3 * normalised_manual_score."""
```

### 3.2 Experiment registry (3 row mới vào `du_doan_test_experiments`)

```python
NEW_EXPERIMENTS = [
    {
        'experiment_name': 'MB_MANUAL_DRIVE_SHADOW_V1',
        'region': 'MB',
        'status': 'SHADOW',
        'method_family': 'manual_rule_drive',
        'description': 'V10683: 77 MANUAL rules (V10667 + V10636-DIG/LAGS) drive replacement '
                       'for PRODUCTION in /du-doan-test only. live_eligible=False, diagnostic_only=True.',
        ...
    },
    {
        'experiment_name': 'MB_MANUAL_BHPASS_DRIVE_SHADOW_V1',
        'region': 'MB',
        ...
        'description': 'V10683: 5 BH-pass MANUAL rules (gold standard) drive only.',
    },
    {
        'experiment_name': 'MB_BLEND_PROD_MANUAL_SHADOW_V1',
        'region': 'MB',
        ...
        'description': 'V10683: Blend 0.7×PROD + 0.3×MANUAL score.',
    },
]
```

### 3.3 Cron đề xuất

| Giờ VN | Job | Lý do |
|---|---|---|
| 23:50 | `_run_v10683_manual_drive_shadow` | Sau V66 23:35, V67 23:40, V70 23:45, V71 23:48; trước V76 23:50 drift monitor (cron mới đẩy thành 23:51 nếu va chạm) |

### 3.4 Hard contract

- Đọc: `mb_experimental_preview_shadow` (candidates pool có sẵn, đã được PROD chấm), `mb_manual_rolling_eval` (MANUAL rolling), `lottery_results` (read-only cho transform).
- Ghi: 3 row mới `mb_experimental_preview_shadow` với 3 experiment_name; `du_doan_test_*` tự động qua engine downstream.
- KHÔNG đụng: `mined_rules`, `final_bundles`, `predictions`, `lottery_results`, `model_daily_eval`, MN/MT.

### 3.5 4 ngưỡng PASS/FAIL 30d (đã owner OK)

| Metric | PASS | FAIL |
|---|---|---|
| `would_flip_baseline_to_win` | ≥ 8/30 ngày | ≤ 3/30 |
| `would_flip_baseline_to_lose` (false_promotion) | ≤ 5/30 | > 8/30 |
| Δ BT hit-rate vs `MB_OFFICIAL_BASELINE_CONTROL` | ≥ +5 pp | < +2 pp hoặc âm |
| Sample `n_lose` (ngày baseline LOSE) | ≥ 30 | < 30 |

Quyết định promote chính thức chỉ sau closeout forward audit (31/08/2026).

---

## 4. Verify checklist (sau khi code)

| Check | Tool | Kết quả mong đợi |
|---|---|---|
| py_compile các file mới | `python -m py_compile` | PASS |
| ReadLints | tool | 0 errors |
| Unit test `apply_transform` 7 transforms | manual | đúng output mỗi transform |
| Backfill 90d V10684 trên DB local | CLI | populate `mb_manual_rolling_eval` ~7000 row |
| Smoke test V10683 trên 1 ngày | CLI | 3 row mới trong `mb_experimental_preview_shadow` |
| Harness MN/MT 108 chữ ký | `_mn_mt_invariance_harness.py` | 108/108 IDENTICAL |
| Full verify suite | `_vf_full_verify.py` | 55/55 PASS (sẽ có check mới cho V10684/V10683) |
| Isolation matrix | `_v10684_isolation_matrix.py` | 18/18 PASS |
| 4 official tables hash | inline | zero-drift |

---

## 5. Risk matrix + rollback

| Rủi ro | Mức | Mitigation |
|---|---|---|
| Schema migration `mb_manual_rolling_eval` lỗi | Thấp | `CREATE TABLE IF NOT EXISTS`, có script rollback DROP TABLE |
| Transform `apply_transform` sai logic | Trung bình | Unit test 7 transforms với fixture cố định trước backfill |
| Cron 23:50 va với V76 drift monitor | Thấp | Đẩy V10683 23:51 nếu phát hiện collision khi đăng ký |
| MANUAL rule reference V10636 artifact bị thay đổi | Trung bình | Hash check artifact ở mỗi run; fallback dùng snapshot V10685 backup |
| Lane test multi-region engine thay đổi | Trung bình | Isolation matrix re-run sau mỗi sửa file mới |
| 4 official tables drift | Cao | Pre/post hash check + abort nếu khác |

**Rollback nhanh** (nếu code có vấn đề):
- Tắt cron mới (chưa đăng ký nên dễ).
- DROP `mb_manual_rolling_eval` (nếu cần).
- DELETE FROM `mb_experimental_preview_shadow` WHERE experiment_name LIKE 'MB_MANUAL_%' OR 'MB_BLEND_%'.
- DELETE FROM `du_doan_test_experiments` WHERE experiment_name LIKE 'MB_MANUAL_%' OR 'MB_BLEND_%'.
- Code rollback: copy `*.v10685.pre` về.

---

## 6. Trạng thái + cần owner OK

| Hạng mục | Status |
|---|---|
| Owner chốt 3 quyết định | DONE |
| V10685 rename | DONE (push GitHub `1b61d22`) |
| V10686 design (file này) | sắp push GitHub |
| Backup full | có (`v10684_full_isolation_backup_*` + `v10685_naming_consistency_*`) |
| MN/MT bất biến | PROVEN 108/108 |
| Isolation matrix | 18/18 PASS |
| **V10684 code local** | **CHƯA — chờ owner OK "code đi"** |
| V10683 code local | sau V10684 + 1 tuần |
| VPS deploy | sau verify đầy đủ + owner OK |

---

**Bottom line**: Plan kỹ thuật đã đủ chi tiết. Em chờ anh nói "code đi V10684" thì bắt đầu viết file local + backup + verify. Tới đó vẫn không deploy VPS — anh review code rồi mới OK deploy.
