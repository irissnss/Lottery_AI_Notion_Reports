# V10634 — Báo Cáo Cơ Chế Rule Pipeline (Owner Report VN)

> **Version:** V20.3.37.106.34 — RULE_PIPELINE_MECHANISM_AUDIT
> **Created:** 2026-05-27 21:48 UTC+7
> **Trigger:** Owner question từ xs.io.vn/app screenshot — "rules trong UI là tổng hợp tuần hay ngày, ML nào, có real-time không?"
> **Owner clarification:** "MN/MT/MB độc lập hết, không phải cố định 12-16 tuần cho cả 3 miền"
> **Scope:** Read-only audit. Không official mutation, không provider, không live mutation.

---

## 0. TL;DR — 3 câu trả lời cho 3 câu hỏi của anh

### Câu 1: Rules là tổng hợp tuần hay ngày?

**Theo trục `region + weekday` (21 bucket = 3 miền × 7 thứ).**

| Layer | Cadence | Job/File |
|---|---|---|
| Sinh rule mới (mining) | **Tuần** — Thứ Hai 00:30 VN | `weekly_rule_miner.py → _seed_rules.main()` |
| Đánh giá hit của rule | **Ngày** — 20:15 VN sau khi xổ xong | `mined_rule_eval.py` |
| Promote/Demote tier | Tuần + ad-hoc | `weekly_rule_miner.py::auto_promote_eligible_rules` |
| Hiển thị UI | **Real-time** | `/api/prediction-quality` (NO_STORE_REALTIME) |

`T(Thứ 3)` = **Thứ Ba**, không phải tuần thứ 3.

### Câu 2: Cơ chế ML nào?

**KHÔNG phải ML.** Là **statistical lift mining thuần** (audit-based).

Tách biệt 2 luồng trong UI:

| Luồng | Cơ chế | Vị trí UI |
|---|---|---|
| **Rules** (R1271, R1272…) | Statistical lift mining — đếm hit_rate theo weekday, không có gradient descent/training | Khung đỏ "Rules hôm nay" |
| **Models** (GLMS5.1, RF, COMBO, Meta-Learn…) | ML thực sự — RandomForest, XGB, GLM, Transformer ensemble, AI providers | "Khuyến nghị" với % confidence |

Gộp lại bằng công thức (`main.py:4580`):
```
rec_score = 0.60 × model_WR_14d + 0.25 × rule_strength_score + 0.15 × diversity_bonus
```

### Câu 3: Real-time?

**Có và không — tùy thành phần:**

| Thành phần UI | Real-time? |
|---|---|
| Mở panel "Khuyến nghị" | ✅ Tính lại từ đầu mỗi lần (NO_STORE cache header) |
| Bar chart WR 14 ngày | ✅ Live SQL `predictions` table |
| `predicted_tails` của mỗi rule | ✅ Live lookup `lottery_results` D-1 |
| Danh sách rules trong bucket | ⏸ Cached weekly từ `mined_rules` |
| `hit_rate_365`, `hr_12w`, `hr_16w` | ⏸ Tính lúc mining (Thứ Hai 00:30) |
| Tier promote/demote | ⏸ Daily MRE 20:15 cập nhật |

---

## 1. Owner-correction at turn N-1 — admission

Ở turn trước em đã trả lời simplistic rằng "12-16 tuần cố định cho 3 miền". Anh chỉ ra **đúng** rằng MN/MT/MB có hệ số tích lũy tổng hợp **độc lập** với nhau.

Em đã đào lại source code (`_seed_rules.py`, `weekly_rule_miner.py`, `rule_engine.py`, `gpt_analyzer.py`, `main.py`) và verify trên DB live. Pass V10634 này **chỉnh lại câu trả lời chính xác**.

**Phân tích lại cho rõ ràng:**

| Tham số | Cố định 3 miền? | Độc lập theo miền? |
|---|---|---|
| Kích thước window 4W/8W/12W/16W | ✅ Fixed | — |
| Trọng số composite (0.50/0.35/0.10/0.05) | ✅ Fixed | — |
| Verdict thresholds (50/45/40%) | ✅ Fixed | — |
| Lifecycle gate (55% / 8 samples) | ✅ Fixed | — |
| Boost table (tier × prediction_use) | ✅ Fixed | — |
| Convergence bonus + cap | ✅ Fixed | — |
| **Source pool (số cross-region direction)** | ❌ | ✅ MN=3, MT=4, MB=5 |
| **Prize key set** | ❌ | ✅ MN/MT có g8+g5, MB không |
| **Baseline xác suất p_region** | ❌ | ✅ Tính riêng |
| **BUCKET_QUALITY_TABLE** (21 entries) | ❌ | ✅ |
| **BUCKET_SUPPRESS_THRESHOLD** | ❌ | ✅ MN=50, **MT=60**, MB=50 |
| **MB CALIBRATION V10.3** | ❌ | ✅ MB ceiling 55%, MN/MT 70% |
| **Station/day count** | ❌ | ✅ MN 3-4, MT 2, MB 1 |
| **Effective sample size n_365** | ❌ | ✅ MN 28-53, MT 7-53, MB 6-53 |

→ **7 cố định + 8 độc lập**. Anh đúng — phần "tích lũy tổng hợp cuối cùng" KHÁC nhau hoàn toàn vì 8 tham số độc lập trên áp lên 7 tham số fixed.

---

## 2. Pipeline 12 bước chi tiết (DAG)

```
[1] Data load
    lottery_results → in-memory dict[date][region]
    file: _seed_rules.py::load

[2] Baseline computation (PER-REGION, ĐỘC LẬP)
    For each region in (MN, MT, MB):
        avg_tail_count_per_day_365d = ...
        baselines[region] = {avg, p = avg/100}
    file: _seed_rules.py::main line 359-368

[3] Rule enumeration (PER-REGION, ĐỘC LẬP)
    For each (target_region, target_weekday) in 21 buckets:
        src_cfgs = {
            MN: [MT D-1, MN D-1, MB D-1]                  ← 3 sources
            MT: [MN D=0, MT D-1, MN D-1, MB D-1]           ← 4 sources
            MB: [MT D=0, MN D=0, MT D-1, MN D-1, MB D-1]  ← 5 sources
        }
    file: _seed_rules.py::src_cfgs line 94-97

[4] Statistical metrics (FIXED windows, PER-REGION input)
    hit_rate_365, hr_4w/8w/12w/16w (windows cố định)
    lift_365 = hit_rate / (1 - (1-p_region)^avg_src_tails)
             ↑ baseline khác nhau theo miền → lift khác nhau
    streak, gap, stability
    file: _seed_rules.py::build_rule, _compute_window_hrs

[5] Scoring + tier classification (FIXED coefficients)
    score_rule() — threshold-based bumps
    composite_score = 0.50×hr_12w + 0.35×hr_16w + 0.10×hr_4w + 0.05×confidence
    cumulative_rank_score = composite + verdict_bonus + stability_bonus
                            + evidence_bonus + use_bonus + legacy_bonus
                            − living_penalty
    tier ∈ {READY_STRONG, READY_WITH_CAUTION, LIMITED_WEIGHT, REFERENCE_ONLY}
    file: _seed_rules.py::score_rule, _compute_composite_score

[6] Top-5 selection per bucket
    21 buckets × 5 = 105 rules persisted
    file: _seed_rules.py::main loop

[7] DB persist + version tag
    DELETE FROM mined_rules
    INSERT new top-5 per bucket
    rule_version = v{ISO_YEAR}W{ISO_WEEK}
    activation_status = 'shadow'
    file: weekly_rule_miner.py::run_weekly_mining

[8] Daily MRE evaluation (DAILY 20:15)
    For each active rule:
        Lookup source date, extract tails
        Check if appears in target region results
        INSERT mined_rule_effectiveness
    file: mined_rule_eval.py

[9] Lifecycle (promote/demote)
    Promote: hit_rate ≥ 55% AND samples ≥ 8 → shadow → active
    Demote:  hit_rate < 25% AND samples ≥ 8 AND active ≥ 14d → active → shadow
    file: weekly_rule_miner.py::auto_promote_eligible_rules / demote_stale_rules

[10] Runtime rule lookup (PER PREDICTION CYCLE, PER-REGION)
    get_active_rules(target_region, target_date) filter:
        region + weekday + tier + activation_status
    Apply BUCKET_QUALITY_TABLE[bucket_code] suppression:
        if score < BUCKET_SUPPRESS_THRESHOLD[region] → READY_STRONG only
                        ↑ MN=50, MT=60, MB=50
    file: rule_engine.py::get_active_rules, extract_rule_candidates_v2

[11] Boost computation (FIXED table, PER-REGION input)
    For each rule:
        Generate 2-digit tails from source date
        boost = BOOST_TABLE[(tier, prediction_use)]
        boost ×= DH_MULTIPLIER (hit_level history)
        boost ×= livingness_weight (last 84 days same weekday)
        boost ≤ CONVERGENCE_CAP if multiple rules converge
    file: rule_engine.py::extract_rule_candidates_v2

[12] Display in UI (REAL-TIME, PER-REGION ceiling)
    GET /api/prediction-quality
    Cache: NO_STORE_REALTIME (no cache header)
    MB CALIBRATION V10.3 applied at prompt level:
        MN/MT confidence ceiling = 70%
        MB confidence ceiling = 55%
        MB requires ≥2 independent evidence sources
    file: main.py::api_prediction_quality, gpt_analyzer.py line 4534-4547
```

---

## 3. DB audit live — 2026-05-27 21:48 VN

Em chạy `_audit_rule_pipeline.py` đọc DB live (không mutation). Kết quả ở `machine_readable/V10634_DB_AUDIT_LIVE_DATA.json`.

### 3.1. Total per region

| Miền | Rule active | Avg HR_365 | Avg HR_12W | Avg HR_16W | n_365 range | Avg cumulative_rank_score |
|---|---|---|---|---|---|---|
| **MN** | 35 | **88.6%** | **96.0%** | ~96% | 28–53 | **116.2** |
| **MT** | 35 | 82.3% | 89.6% | ~88% | **7–53** | 110.5 |
| **MB** | 35 | **63.6%** | **75.7%** | ~73% | **6–53** | **96.8** |

→ Chênh lệch `cumulative_rank_score` trung bình MN→MB = **20 điểm** (116 vs 97). Vì 8 tham số độc lập per-region áp lên 7 tham số fixed.

### 3.2. Source diversity per target

```
TARGET MN: 35 rules
    ├─ 24 từ MB D-1 (68.6%)
    ├─ 8 MN self D-1 (22.9%)
    └─ 3 MT D-1 (8.6%)

TARGET MT: 35 rules
    ├─ 23 từ MB D-1 (65.7%)
    ├─ 5 MN D-1 (14.3%)
    ├─ 4 MN D=0 same-day (11.4%)  ← chỉ MT có
    └─ 3 MT self D-1 (8.6%)

TARGET MB: 35 rules
    ├─ 12 MB self D-1 (34.3%)
    ├─ 8 MT D-1 (22.9%)
    ├─ 7 MN D-1 (20.0%)
    ├─ 5 MT D=0 same-day (14.3%)  ← chỉ MB có
    └─ 3 MN D=0 same-day (8.6%)   ← chỉ MB có
```

### 3.3. Tier distribution per region

| Miền | READY_STRONG | READY_WITH_CAUTION | LIMITED_WEIGHT |
|---|---|---|---|
| MN | 3 | 11 | 21 |
| MT | 4 | 11 | 20 |
| MB | 3 | 14 | 18 |

→ Phân bố tier khác nhau. MB có nhiều RWC hơn (14 vs 11) — kết hợp với MB calibration ceiling 55% là cơ chế phòng vệ "evidence mỏng".

### 3.4. Per-bucket detail (21 buckets, top metrics)

| rg | wd | n | HR365 | HR4W | HR12W | HR16W | comp | cum |
|---|---|---|---|---|---|---|---|---|
| MB | 0 (T2) | 5 | 76.3 | 95.0 | 78.3 | 77.9 | 80.4 | 100.9 |
| MB | 1 (T3) | 5 | 69.0 | 65.0 | 73.3 | 73.8 | 74.0 | 94.7 |
| MB | 2 (T4) | 5 | 64.5 | 80.0 | 71.7 | 71.3 | 73.8 | 95.2 |
| MB | 3 (T5) | 5 | 52.5 | 70.0 | 70.0 | 70.0 | 71.5 | 93.2 |
| MB | 4 (T6) | 5 | 55.9 | 75.0 | 66.7 | 68.8 | 69.9 | 89.9 |
| MB | 5 (T7) | 5 | 55.5 | 90.0 | 78.3 | 73.8 | 79.0 | 100.2 |
| MB | 6 (CN) | 5 | 71.7 | 85.0 | 91.7 | 83.8 | 88.7 | 108.2 |
| MN | 0 (T2) | 5 | 81.2 | 100.0 | 96.7 | 95.0 | 96.6 | 118.1 |
| MN | 1 (T3) | 5 | 91.9 | 100.0 | 95.0 | 96.3 | 96.2 | 116.2 |
| MN | 2 (T4) | 5 | 93.4 | 95.0 | 98.3 | 98.8 | 98.2 | 118.5 |
| MN | 3 (T5) | 5 | 85.3 | 95.0 | 91.7 | 91.3 | 92.3 | 113.2 |
| MN | 4 (T6) | 5 | 87.8 | 100.0 | 96.7 | 97.5 | 97.4 | 117.3 |
| MN | 5 (T7) | 5 | 93.2 | 100.0 | 100.0 | 100.0 | 100.0 | 121.3 |
| MN | 6 (CN) | 5 | 87.8 | 90.0 | 93.3 | 87.5 | 91.3 | 111.2 |
| MT | 0 (T2) | 5 | 82.5 | 100.0 | 92.1 | 89.6 | 92.1 | 111.7 |
| MT | 1 (T3) | 5 | 91.0 | 75.0 | 88.3 | 91.3 | 88.6 | 108.8 |
| MT | 2 (T4) | 5 | 72.4 | 70.0 | 78.3 | 78.8 | 78.7 | 99.0 |
| MT | 3 (T5) | 5 | 84.2 | 95.0 | 96.7 | 92.5 | 95.2 | 115.3 |
| MT | 4 (T6) | 5 | 79.7 | 90.0 | 88.3 | 83.8 | 87.5 | 107.1 |
| MT | 5 (T7) | 5 | 83.6 | 95.0 | 91.7 | 87.5 | 91.0 | 113.0 |
| MT | 6 (CN) | 5 | 82.8 | 90.0 | 91.7 | 91.3 | 91.8 | 113.9 |

---

## 4. BUCKET_QUALITY_TABLE — 21 hệ số độc lập

Từ `rule_engine.py:108-115` (snapshot **2026-03-22** từ `verified_bucket_rules` weekly mining run):

| Miền/Thứ | T2 | T3 | T4 | T5 | T6 | T7 | CN | Threshold |
|---|---|---|---|---|---|---|---|---|
| **MN** | 70 | 61 | 55 | 53 | 72 | 59 | 67 | **50** |
| **MT** | 58 | 51 | 73 | 51 | 76 | 74 | 49 | **60** ⬆ |
| **MB** | 63 | 59 | 64 | 51 | 64 | 63 | 65 | **50** |

**Hiệu lực thực sự** (số bucket bị suppress xuống chỉ READY_STRONG):

| Miền | Bucket dưới threshold | Tỷ lệ suppress |
|---|---|---|
| MN | 0 bucket (T5=53 > 50) | 0% |
| **MT** | **4 bucket** (T2=58, T3=51, T5=51, CN=49 < 60) | **57%** ⚠ |
| MB | 0 bucket (T5=51 vừa qua) | 0% |

→ **MT bị gating nặng nhất** — 4/7 weekday MT phải chỉ dùng READY_STRONG rules. Đây là một dấu hiệu MT noisier hơn MN/MB ở mức bucket-level.

---

## 5. MB CALIBRATION V10.3 — thiên vị phòng vệ cho MB

Từ `gpt_analyzer.py:4534-4547`:

```
📐 V10.3 MB CALIBRATION:
⚠️ MB = 1 đài/ngày → evidence mỏng hơn MN/MT 3-4x
📋 MB CONFIDENCE RULES:
   • Base confidence ceiling: 55% (MN/MT = 70%)
   • Rule match từ 1 đài = evidence yếu → giảm tin cậy 20%
   • CHỈ tăng confidence khi có ≥2 nguồn evidence ĐỘC LẬP:
     - cross-region (MN/MT đã ra → xác nhận MB)
     - frequency + gap agreement
     - weekday pattern consistent ≥3 tuần
   • Nếu chỉ có 1 rule match → giữ SKIP hoặc strength ≤5
   • KHÔNG overclaim 'strong evidence' từ 1-station data
```

| Tham số | MN | MT | MB |
|---|---|---|---|
| Base confidence ceiling | 70% | 70% | **55%** ⬇ |
| Rule evidence penalty | 0% | 0% | **−20%** |
| Independent evidence required | Không | Không | **≥2 nguồn** |
| Station/day | 3-4 | 2 | **1** |

→ MB có một tầng calibration ở prompt level mà MN/MT không có. Đây là phần "tích lũy tổng hợp khác" sâu sắc nhất của MB so với 2 miền kia.

---

## 6. Real-time architecture chi tiết

### 6.1. `/api/prediction-quality` (`main.py` ~4257-5210)

```
Mỗi lần FE call panel:
    1. Query rankings models (live SQL predictions WIN/LOSE/PARTIAL 14d)
    2. Query rule_support per region:
        SELECT từ mined_rules WHERE target_region = ? AND target_weekday = today_wd
        ORDER BY cumulative_rank_score DESC
        LIMIT 5
    3. Live lookup predicted_tails cho mỗi rule:
        Resolve source_date = today + offset (-1 hoặc 0)
        Lookup lottery_results @ source_date + source_station
        Extract tails from prize_keys
    4. Compute alignment + diversity
    5. recommend = 60% WR_14d + 25% rule_strength + 15% diversity_bonus
    6. Apply MB CALIBRATION nếu region == MB:
        ceiling = 55% (vs 70% MN/MT)
    7. Return JSON với cache_header: NO_STORE_REALTIME
```

### 6.2. UI display rule (`app.js`)

```
R{rule.id} · {prize_keys} · WR{hit_rate_365}% · S{streak}
{source_region}({source_offset}/{weekday}) · {station} → {target_region}
```

- `R1271` = SQLite AUTOINCREMENT id, **không stable** giữa các tuần
- `S22` = **streak** (chuỗi hit liên tiếp), **không phải sample size**
- `WR84.1%` = `hit_rate_365 × 100`, snapshot từ Thứ Hai 00:30

### 6.3. Khi nào panel data thay đổi?

| Sự kiện | Component thay đổi |
|---|---|
| Mỗi lần F5 panel | WR 14d models, predicted_tails (live) |
| Mỗi prediction cycle (~04:00 sáng) | Rankings models, recommended primary |
| Verify/closeout (sau khi xổ ~20:00) | model status WIN/LOSE/PARTIAL, WR 14d update |
| Daily MRE 20:15 | mined_rule_effectiveness, hit tracking |
| Weekly mining Thứ Hai 00:30 | Toàn bộ mined_rules (DELETE + INSERT) |

---

## 7. Models trong screenshot — danh sách thật

Từ `model_registry.py`:

| UI label | Registry ID | Status | Output-eligible |
|---|---|---|---|
| **GLMS5.1** | `glm-5.1` | **SHADOW_AUTO** | ❌ |
| **DeepSeek R1** | `deepseek-reasoner` | ACTIVE | ✅ |
| **Opus 4.6** | `claude-opus-4-20250514` | ACTIVE | ✅ |
| **RF** | `random-forest` | ACTIVE | ✅ |
| **XGB+RF** | `smart-ml` | ACTIVE | ✅ |
| **COMBO** | `combo-no-token` | ACTIVE | ✅ |
| **SUPER** | `combo-super` | ACTIVE | ✅ |
| **Meta-Learn** | `meta-learning` | ACTIVE | ✅ |
| **Gemini 2.5** | `gemini-2.5-flash/pro` | ACTIVE | ✅ |
| gemini-3-flash | `gemini-3-flash` | SHADOW_AUTO | ❌ |
| gemini-3-pro | `gemini-3.1-pro` | SHADOW_AUTO | ❌ |
| **gpt-5.5** | `gpt-5.5` (OpenRouter) | SHADOW_AUTO | ❌ |

⚠ **Lưu ý quan trọng**: GLMS5.1 lead với 90.9% trong screenshot, nhưng **status = SHADOW_AUTO → không output_eligible → KHÔNG đi vào `/du-doan` chính thức**. Khi UI hiện như primary recommendation, đó là **leaderboard tham khảo**, không phải dự đoán đang dùng để chốt bundle final.

---

## 8. Khác biệt giữa rules từ V10626 FU4 (pre-register) và mined_rules (UI)

Quan trọng để không nhầm — anh có hỏi về 13 rule FU4 em đẩy public hôm 25/05/2026:

| Đặc tính | mined_rules (UI hiển thị) | V10626 FU4 (pre-register addendum) |
|---|---|---|
| Trạng thái | `activation_status = active` | `PRE_REGISTER_ONLY` |
| Vị trí | DB table `mined_rules` | File CSV trong `artifacts/v106_26_followup_*/` |
| Boost prediction? | ✅ Có (qua `extract_rule_candidates_v2`) | ❌ Không |
| Public push | Không (tách private) | Đã push lên `Lottery_AI_Notion_Reports` 2026-05-25 |
| Window/coefficient | 4W/8W/12W/16W từ weekly mining | w60/w90/w180 forward-audit |
| Source pool | `src_cfgs()` của `_seed_rules.py` | MB G4/G6/G7 OWNER_SCHEMA |
| Khi nào lên UI? | Tự động Thứ Hai 00:30 | Chỉ khi sau **forward audit 90d** (≥ 2026-08-23) + owner OK promote |

→ 13 rule FU4 hôm 25/05 **chưa có ảnh hưởng tới UI hôm nay**. Cần đợi forward audit 90 ngày rồi mới được anh OK move sang `mined_rules`.

---

## 9. Source code references (mọi claim đều có evidence)

| Claim | File | Line |
|---|---|---|
| Window sizes 4/8/12/16W fixed | `_seed_rules.py::_compute_window_hrs` | 142-158 |
| Composite weights 0.50/0.35/0.10/0.05 | `_seed_rules.py::_compute_composite_score` | 179-188 |
| Verdict thresholds | `_seed_rules.py::_compute_window_verdict` | 161-176 |
| Cumulative rank score formula | `_seed_rules.py::_compute_cumulative_rank_score` | 191-238 |
| Per-region src_cfgs (3/4/5) | `_seed_rules.py::src_cfgs` | 94-97 |
| SRC_MNMT vs SRC_MB prize keys | `_seed_rules.py` constants | 26-27 |
| Per-region baselines | `_seed_rules.py::main` | 359-368 |
| Top-5 per bucket selection | `_seed_rules.py::main` | 500+ |
| Weekly schedule (Mon 00:30) | `weekly_rule_miner.py::run_weekly_mining` | 37 |
| Daily MRE (20:15) | `scheduler.py` job `auto_mined_rule_eval` | — |
| Promote gate 55%/8 samples | `weekly_rule_miner.py::auto_promote_eligible_rules` | 243 |
| Demote gate 25%/8/14d | `weekly_rule_miner.py::demote_stale_rules` | 328 |
| BUCKET_QUALITY_TABLE 21 entries | `rule_engine.py::BUCKET_QUALITY_TABLE` | 108-115 |
| BUCKET_SUPPRESS_THRESHOLD MN=50/MT=60/MB=50 | `rule_engine.py::BUCKET_SUPPRESS_THRESHOLD` | 116 |
| BOOST_TABLE | `rule_engine.py::BOOST_TABLE` | 49-72 |
| Convergence cap | `rule_engine.py::CONV_BOOST_CAP` | 80-84 |
| Runtime lookup with suppression | `rule_engine.py::extract_rule_candidates_v2` | 288-540 |
| MB CALIBRATION V10.3 | `gpt_analyzer.py` V10.3 block | 4534-4547 |
| /api/prediction-quality logic | `main.py::api_prediction_quality` | 4259-5210 |
| Rec score 60/25/15 formula | `main.py` | 4580 |

---

## 10. Files trong audit pass V10634

```
artifacts/v105_55_safe_quality/V10634_rule_pipeline_mechanism_audit/
├── V10634_RULE_PIPELINE_MECHANISM_AUDIT_VN.md    (file này)
├── machine_readable/
│   ├── V10634_DB_AUDIT_LIVE_DATA.json            (audit DB live)
│   ├── V10634_PER_REGION_INDEPENDENCE_MATRIX.json (7 fixed + 8 independent)
│   ├── V10634_BUCKET_QUALITY_TABLE_AUDIT.json    (21 entries + interpretation)
│   ├── V10634_RULE_PIPELINE_FLOW.json            (12-stage DAG)
│   └── V10634_EXECUTION_SUMMARY.json
└── scripts/
    └── _audit_rule_pipeline.py
```

---

## 11. Safety gate

| Check | Status |
|---|---|
| official_mutation | 0 |
| mined_rules mutation | 0 (read-only) |
| Production prompt/selector/scoring/voting switch | 0 |
| Provider call | 0 |
| Manual AI call | 0 |
| Wallet/MB expansion | 0 |
| Lane promotion | 0 |
| Cron install | 0 |
| Deploy | 0 |
| Live result change | 0 |
| Public push | YES (owner-explicit) |

---

## 12. Kết luận cho anh

**3 câu trả lời cuối cùng:**

1. **Tổng hợp tuần hay ngày?** Theo trục **region + weekday** (21 bucket). Mining tuần (Thứ Hai 00:30), eval ngày (20:15), display real-time.

2. **Cơ chế ML?** Rules **KHÔNG phải ML** — là statistical lift mining. Models (GLMS5.1, RF, COMBO, …) là ML/AI **TÁCH BIỆT**, gộp lại bằng công thức 60/25/15. **13 rule FU4 em đẩy 25/05 cũng KHÔNG phải ML** — đó là pre-register PRE_REGISTER_ONLY chờ forward audit 90d.

3. **Real-time?** UI panel hoàn toàn real-time (NO_STORE cache). Nội dung rules được snapshot từ Thứ Hai. Hit_rate từ daily MRE 20:15. Models WR từ live 14d SQL.

**Anh đúng về MN/MT/MB độc lập:** 8 tham số khác nhau hoàn toàn theo miền (source pool, prize set, baseline, bucket quality 21 entries, suppress threshold 50/60/50, MB calibration 55/70, station/day count, n_365 range). Em sửa lại câu trả lời simplistic ở turn trước.

---

**STATUS: V10634 READ-ONLY AUDIT DONE — DOCS READY FOR PUBLIC PUSH**
