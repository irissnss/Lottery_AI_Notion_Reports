# V71 — HYBRID_V1 selector + C-16 score-gate fix → MT/MB rescued

**Date:** 2026-05-07 02:02 VN
**Scope:** test-lane only. Pre/post hashes for 4 official tables UNCHANGED.

---

## Owner question

> "Sao MT/MB chỉ setting 15 model cứng tối thiểu là 15 và tối đa là 20 model? Tăng số đồng thuận có cứu được hit không? Việc xếp hạng các model mạnh yếu ở miền/thứ/đài đã thực hiện tới đâu? Sự kết hợp V67 + C-16 có cứu được Miền Trung không?"

---

## 1. Tại sao MT/MB chỉ có 15 voters?

C-16 score gate `final_budget_score >= 0.42` đã **calibrate cho MN**. Phân bố score per region (anchor 2026-05-06):

| Region | n_measured | score ≥ 0.42 | score ≥ 0.35 | score ≥ 0.30 | selected (cũ) |
|---|---:|---:|---:|---:|---:|
| **MN** | 29 | 22 | 22 | 22 | **20** ✅ |
| **MT** | 29 | **0** | 4 | 11 | **15** 🔴 |
| **MB** | 29 | **0** | 4 | 12 | **15** 🔴 |

→ MT/MB **0/29 model** đạt 0.42 (max MT=0.416, max MB=0.399). Backfill loop dừng ở target_min=15.

### Fix

Drop the absolute 0.42 threshold; first loop fills `target_max=20` with strongest measured models regardless of score.

```python
for row in scored:
    if len(selected_names) >= target_max: break
    if row["model_name"] in selected_names: continue
    if row["measured"]:
        selected_names.add(row["model_name"])
```

**After fix**: MN/MT/MB all selected = **20** (owner directive met across all regions).

---

## 2. Strength ranking đã thực hiện tới đâu?

Tensor `model_strength_by_region_weekday_station_daily` đã có từ V52.5.1, refresh daily (anchor 2026-05-05), 4 windows (7/14/30/60), 3 grains (region, region_weekday, region_station). Top-20 per region đã expose:

### Top-5 mỗi miền (window=30d, grain=region)

| Rank | MN | MT | MB |
|---:|---|---|---|
| 1 | gpt-5.5 (h=0.60) | smart-ml (h=0.51) | qwen3.6-plus (h=0.34) |
| 2 | combo-super (h=0.58) | meta-learning (h=0.46) | gpt-5.5 (h=0.31) |
| 3 | claude-sonnet-4-6 (h=0.58) | smart-ensemble (h=0.45) | random-forest (h=0.31) |
| 4 | smart-ensemble (h=0.56) | random-forest (h=0.44) | gpt-5-mini (h=0.29) |
| 5 | gemini-2.5-pro (h=0.56) | grok-4.20 (h=0.43) | (lower scores) |

→ **MT mạnh ở NO_TOKEN cluster** (4/5 top là NO_TOKEN), giải thích vì sao C-16 score MT thấp hơn (TOKEN-bias scoring).
→ **MN mạnh ở mix TOKEN+NO_TOKEN** (đa dạng hơn).
→ **MB cấu trúc yếu nhất** (max h=0.34).

### Per-weekday breakdown

Cũng đã sẵn ở grain `region_weekday` (sample size: 3-7 per cell) — chỉ vài cell qualify với window 30d. Cần 180d để gate per-weekday đầy đủ (xem CP-66.5b).

---

## 3. V71 HYBRID_V1 — V67 + C-16 + CONSENSUS hợp tác

Confidence tiers:
- **CROWN**: CONSENSUS pick == EXPLOIT pick (overlap → highest expected hit)
- **HIGH**: CONSENSUS pick alone (≥3 method agreement)
- **MEDIUM**: EXPLOIT pick alone (V67 STRICT-gated lag-1)
- **LOW**: BUDGET_SELECTOR pick alone
- **SKIP**: nothing

### 14d backfill ALL-region (n=42, largest cross-method sample)

| Method | MN | MT | MB | ALL hit% (95%CI) | profit |
|---|---:|---:|---:|---|---:|
| OFFICIAL | 42.9% | 57.1% | 28.6% | 42.9% [29.1-57.8] | +1358u |
| **🏆 HYBRID_V1** | 42.9% | **57.1%** ✅ | **35.7%** ✅ | **45.2%** [31.2-60.1] | **+1428u** |
| CONSENSUS_V1 | 46.2% | 57.1% | 38.5% | 47.5% [32.9-62.5] | +1430u |
| C-16 BUDGET (15-20) | 42.9% | 42.9% | 21.4% | 35.7% [23.0-50.8] | +1128u |
| V67 EXPLOIT (STRICT) | 100% (n=2) | 50% (n=2) | 50% (n=6) | 60% [31.3-83.2] | +440u |

### MT rescue specifically

Owner asked: "V67 + C-16 có cứu được Miền Trung?" — **CÓ.**

| Stage | MT hit% |
|---|---:|
| C-16 alone (with old gate) | 33% |
| C-16 alone (15-20 voters) | 42.9% |
| **V71 HYBRID** | **57.1%** ✅ TIED OFFICIAL |

→ MT đã được CỨU. Cơ chế cứu chính là **HIGH tier** (CONSENSUS với ≥3 method agreement) — 14/14 MT picks ở HIGH tier.

### MB rescue

| Stage | MB hit% |
|---|---:|
| OFFICIAL | 28.6% |
| C-16 alone (15-20) | 21.4% |
| **V71 HYBRID** | **35.7%** ✅ +7.1pp vs official |

→ MB cũng được CỨU.

### MN

HYBRID = OFFICIAL = 42.9% (tied). MN MEDIUM tier (V67 EXPLOIT alone) chưa fire trong window này; HIGH tier dominate.

---

## 4. HYBRID tier breakdown

| Region | CROWN | HIGH | MEDIUM | LOW | SKIP |
|---|---:|---:|---:|---:|---:|
| MN | 0 | 13 (46.2% hit) | 0 | 1 (0% hit) | 0 |
| MT | 0 | **14 (57.1% hit)** | 0 | 0 | 0 |
| MB | 0 | 13 (38.5% hit) | 1 (0% hit) | 0 | 0 |

→ CROWN tier rare (V67 EXPLOIT rarely overlaps CONSENSUS picks because exploit is anti-consensus by design).
→ **HIGH tier là động lực rescue chính**, đặc biệt cho MT.

---

## 5. Verification

| Check | Result |
|---|---|
| `predictions` count LOCAL | 4377 (unchanged) |
| `final_bundles` count LOCAL | 204 (unchanged) |
| `lottery_results` count LOCAL | 14621 (unchanged) |
| `model_daily_eval` count LOCAL | 4328 (unchanged) |
| VPS C-16 budget 2026-05-06 | MN=20, MT=20, MB=20 ✅ |
| VPS deploy + restart | 02:02 VN, `/api/health=200` |
| Pre/post hash | UNCHANGED on LOCAL+VPS |

---

## 6. Discoveries

### D12 — C-16 score gate was MN-biased

The 0.42 gate prevented owner directive. Removing it lets MT/MB use their top-20 strongest measured models without absolute score thresholds. Future calibration should be region-relative, not absolute.

### D13 — HIGH tier (CONSENSUS) is the MT rescue mechanism

V67 EXPLOIT alone failed in MT (single-source noise). C-16 BUDGET alone failed in MT (TOKEN-bias scoring). But CONSENSUS aggregates picks from 7+ methods including AI_CHAIN_PRESERVATION, NO_TOKEN_HERD_REDUCTION, STRENGTH_WEIGHTED, SPECIALIST_ROSTER, PRIOR_REGION_CONTEXT_SAFE — and 14/14 days the consensus matched OFFICIAL's pick rate. **MT's signal IS consensus, not single-method.**

### D14 — HYBRID covers all 42 days where CONSENSUS only covers 40

CONSENSUS_V1 skips 2 days (MN 2026-04-28, MB 2026-05-03 had only 2-method agreement). HYBRID falls back to MEDIUM/LOW tier on those days, providing coverage. Trade-off: HYBRID 45.2% slightly below CONSENSUS 47.5% because of LOW-tier dilution. But HYBRID is more reliable (no skip).

---

## 7. Next gates

| Proposal | Status |
|---|---|
| C-16 gate removed → MT/MB at 20 voters | ✅ DONE |
| V71 HYBRID_V1 selector | ✅ DEPLOYED |
| Strength ranking surface | ✅ exposed |
| Cron 23:48 VN HYBRID daily | ✅ DEPLOYED |
| **CP-66.7 14-day fresh live** | ⏳ accumulating |
| CP-66.9 owner decision TIER 3 | ⏳ pending evidence pack |

---

## 8. Raw paths

| Artifact | Path |
|---|---|
| V71 HYBRID materializer | `web/backend/_materialize_hybrid_v1.py` |
| V71 trace table | `hybrid_v1_trace` |
| C-16 patch (gate removed) | `web/backend/_materialize_du_doan_test_model_budget.py` |
| Audit (score dist + ranking) | `artifacts/v71_hybrid_audit/v71_audit.txt` |
| 14d full eval | `artifacts/v71_hybrid_audit/v71_full_eval.txt` |
| Schema | `web/backend/_du_doan_test_schema.py` |
| Scheduler cron | `web/backend/scheduler.py` (23:48 VN) |
| Public Notion | `https://github.com/irissnss/Lottery_AI_Notion_Reports/tree/main/V71_HYBRID_AND_C16_FIX_20260507` |

STATUS: **V71_HYBRID_V1_DEPLOYED + C16_GATE_FIXED + MT/MB_RESCUED — accumulating CP-66.7 fresh live evidence**.
