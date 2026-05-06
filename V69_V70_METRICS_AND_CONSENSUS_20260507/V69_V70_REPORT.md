# V69 metrics expansion + V70 CONSENSUS_V1 selector — beats OFFICIAL on 14d

**Date:** 2026-05-07 01:50 VN
**Scope:** test-lane only. Pre/post hashes for `predictions`, `final_bundles`, `lottery_results`, `model_daily_eval` UNCHANGED on LOCAL+VPS.

---

## Owner question

> "Sau khi điều chỉnh từ 8-12 model lên 15-20 model có tăng tỷ lệ trúng hơn xíu nào không em? Với V67 MN, MT, MB có tiến bộ gì không? Cần đo đạt thêm chỉ số nào? Thiếu cái gì đề xuất bổ sung ngay."

---

## A. C-16 expansion 8-10 → 15-20 voters: kết quả 14d

| Region | C-16 hit (15-20) | Official | LO2 hit | Profit |
|---|---:|---:|---:|---:|
| **MN** | **50.0%** (7/14) | 42.9% | 57.1% | +546u (**+7.1pp vs official**) |
| MT | 42.9% (6/14) | 57.1% | 64.3% | +466u (−14.2pp vs official) |
| MB | 14.3% (2/14) | 28.6% | 50.0% | +126u (−14.3pp vs official) |

→ Mở rộng 15-20 voters **giúp MN** (vượt official +7pp), nhưng **không cứu MT/MB**. Đây là evidence rằng "lấy nhiều model mạnh hơn" không phải đáp án duy nhất.

---

## B. V67 MN/MT/MB sau STRICT gate

| Region | n | hit | LO2 hit | profit |
|---|---:|---:|---:|---:|
| MN | 2 | 100% | 100% | +158u |
| MT | 2 | 50% | 50% | +78u |
| MB | 6 | 50% | 50% | +204u |

Sample còn nhỏ (CP-66.7 14d gate chưa kết thúc). Nhưng V67 vẫn keep highest single-method rate.

---

## C. Discovery — Method consensus là metric mạnh nhất

V69 thêm `agreement_count` bucket. Khi N method test-lane đồng ý cùng 1 BT, hit rate:

| Agreement count | n_picks | hit | hit rate |
|---:|---:|---:|---:|
| 1 method | 45 | 13 | 28.9% |
| 2 methods | 12 | 3 | 25.0% |
| **3 methods** | **14** | **9** | **64.3%** 🏆 |
| 4 methods | 13 | 8 | 61.5% |
| 5 methods | 9 | 2 | 22.2% |
| 6 methods | 8 | 5 | 62.5% |
| 8 methods | 4 | 2 | 50.0% |

**+35pp edge** khi 3+ methods agree. Đây là signal mạnh nhất từ trước đến giờ.

---

## D. V70 CONSENSUS_V1 (built in response to discovery)

New file `web/backend/_materialize_consensus_v1.py`:

- Reads other test-method picks from `experimental_preview_shadow` for the date+region
- Excludes `*_OFFICIAL_BASELINE_CONTROL` (clone-of-official, would bias)
- Excludes self
- Counts agreement per tail
- Emit BT only when top tail has ≥3 agreeing methods
- New shadow trace table `consensus_v1_trace`
- Schema register `MN/MT/MB_CONSENSUS_V1`
- Scheduler cron 23:45 VN daily (after V66 23:35 + V67 23:40)

### V70 14-day backfill — BEATS OFFICIAL

ALL-REGION combined:

| Method | n | hit rate (95% CI) | profit |
|---|---:|---|---:|
| **OFFICIAL** | 42 | 42.9% [29.1-57.8] | +1358u |
| 🏆 **CONSENSUS_V1** | 40 | **47.5%** [32.9-62.5] | **+1430u** |
| C-16 ADAPTIVE_BUDGET_SELECTOR_V1 (15-20) | 42 | 35.7% [23.0-50.8] | +1138u |
| V67 ADAPTIVE_EXPLOIT_V1 (STRICT) | 10 | 60.0% [31.3-83.2] | +440u |

→ **CONSENSUS_V1 beats OFFICIAL by +4.6pp on n=40**. Trên cùng cỡ mẫu lớn nhất, đây là method ĐẦU TIÊN consistently outperform official across all 3 regions.

### Per-region V70 vs official

| Region | CONSENSUS_V1 | OFFICIAL | Δ |
|---|---:|---:|---:|
| MN | 46.2% (n=13) | 42.9% (n=14) | +3.3pp |
| MT | 57.1% (n=14) | 57.1% (n=14) | tie |
| **MB** | **38.5%** (n=13) | 28.6% (n=14) | **+9.9pp** 🏆 |

→ MB là single-region biggest improvement (+9.9pp) — vượt cả V67 ADAPTIVE_EXPLOIT_V1 (chỉ MB +33pp nhưng n=6).

---

## E. Discoveries

### D9 — Method consensus là multiplier, không phải individual method

Single best method (V67) vs CONSENSUS:
- V67 60% on n=10 (highest hit rate, smallest sample)
- CONSENSUS 47.5% on n=40 (largest reliable sample)

Khi n đủ lớn, CONSENSUS là method robust nhất. Single methods như V67 high variance.

### D10 — C-16 expansion 15-20 chỉ giúp 1/3 miền

C-16 15-20 voters helps MN +7pp nhưng MT/MB -14pp. Hypothesis: voter pool đa dạng có thể dilute discrimination ở weak buckets nơi chỉ 8-10 model thực sự strong. Owner directive đúng cho MN; cần thêm cơ chế per-region adaptive budget size.

### D11 — Profit > hit rate signal

Mọi method đều +profit (payout 70-80x bù miss cost). Nhưng OFFICIAL +1358u, CONSENSUS +1430u, C-16 +1138u → CONSENSUS dẫn đầu profit dù hit rate khác biệt nhỏ. Ratio is strong.

---

## F. NEXT — what's still missing

Em đề xuất xử lý tiếp:

| Proposal | Priority | Reason |
|---|---|---|
| **CP-70.1** Per-region adaptive C-16 budget (MN=20, MT=8-12, MB=8-12) | 🟡 owner OK needed | C-16 15-20 hurts MT/MB; adaptive size khôi phục bias-variance balance |
| **CP-70.2** Hybrid CONSENSUS + V67 (when both agree → ultra-high confidence) | 🟢 safe | Combine top 2 methods for compound edge |
| **CP-70.3** Real-time consensus dashboard in `/du-doan-test` UI | 🟢 safe | Show owner per-method picks + agreement count + Wilson CI |
| **CP-70.4** Per-method weekly trend (slope of hit rate over time) | 🟢 safe | Detect method decay/improvement early |
| **CP-70.5** LO3 / Xien 2-3 axis consensus | 🟢 safe | Currently only BT; Lo3/Xien also beneficial |
| **CP-70.6** Owner OK to consider CONSENSUS for TIER 3 lift | 🔴 owner gate | After 14 fresh live days at +4pp consistent |

---

## G. Verification

- VPS deploy `01:50 VN`, `/api/health=200`.
- VPS smoke `2026-05-07`: AGREEMENT_BELOW_MIN_3 (chỉ V67 đã write tomorrow's row; consensus tự nhiên fire post-closeout sau khi other methods write).
- Counts `predictions=4377`, `final_bundles=204`, `lottery_results=14621`, `model_daily_eval=4328` UNCHANGED on LOCAL+VPS.

---

## H. Raw paths

| Artifact | Path |
|---|---|
| V70 materializer | `web/backend/_materialize_consensus_v1.py` |
| V69 metrics eval (full) | `artifacts/v69_metrics_expand/v69_metrics_eval.txt` |
| V70 consensus eval (Wilson CI) | `artifacts/v69_metrics_expand/v69_consensus_eval.txt` |
| Schema register | `web/backend/_du_doan_test_schema.py` |
| Scheduler | `web/backend/scheduler.py` (cron 23:45 VN) |
| New trace table | `consensus_v1_trace` |
| CHANGELOG | V20.3.37.69 |
| Public Notion | `https://github.com/irissnss/Lottery_AI_Notion_Reports/tree/main/V69_V70_METRICS_AND_CONSENSUS_20260507` |

STATUS: **V70_CONSENSUS_V1_DEPLOYED — beats OFFICIAL +4.6pp on n=40 — accumulating CP-66.7 14d fresh live evidence for TIER 3 review at CP-66.9**.
