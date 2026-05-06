# V72 — V67 STRICT gate REVERTED → eager (per owner directive)

**Date:** 2026-05-07 02:13 VN
**Scope:** test-lane only. Pre/post hashes 4 official tables UNCHANGED.

---

## Owner directive

> "MN/MT/MB giờ đã ổn rồi đúng không? Chứ nãy anh thấy em gia giảm gì đó để cân bằng — MN lúc nãy giảm gì đó để cứu MT và MB nhưng ko mỹ mãn lắm. Đưa về V67 và C-16 với 20 model top miền/thứ/đài đi. Đang chạy official 15 model mà cắt thế số đồng thuận và dự đoán giảm làm lane test tụt — mất cân bằng, thiếu đồng thuận."

---

## Verdict before revert

C-16 budget đã đạt 20 voters cho cả MN/MT/MB sau V71. Owner xác nhận đây là trạng thái lý tưởng.

V68 trước đó đã thêm V67 STRICT gate (`min_contributions=2 AND score>=1.5`) để giảm noise MT. **Trade-off**: cắt 3 ngày MN single-source winning picks (V67 hits trên các pick độc lập). Owner chỉ ra: cắt picks → giảm input cho CONSENSUS → CONSENSUS agreement count thấp → HYBRID giảm cơ hội fire HIGH tier.

## Fix

Disable STRICT gate trong `_materialize_adaptive_exploit_v1.py`:
```python
STRICT_MIN_CONTRIBUTIONS = 0  # disabled
STRICT_SCORE_THRESHOLD   = 0.0  # disabled
```

V67 trở lại eager: emit candidate khi BẤT KỲ V66.1 BOOST signal nào fire. Trace tag confidence_class (HIGH/MEDIUM/LOW) cho transparency, không suppress row.

Downstream filters tự nhiên:
- CONSENSUS_V1: agreement_count ≥ 3 (no change)
- HYBRID_V1: tier dựa trên overlap (no change)

## After-revert 14d backfill (n=42 ALL-region)

| Method | n | hit% (95%CI) | profit | Δ vs STRICT |
|---|---:|---|---:|---:|
| OFFICIAL | 42 | 42.9% [29.1-57.8] | +1358u | — |
| HYBRID_V1 | 42 | 45.2% [31.2-60.1] | +1428u | unchanged |
| CONSENSUS_V1 | 40 | 47.5% [32.9-62.5] | +1430u | unchanged |
| C-16 (20 voters) | 42 | 35.7% [23.0-50.8] | +1128u | unchanged |
| **V67 EXPLOIT eager** | **17** | **58.8%** [36.0-78.4] | **+753u** | **n: +7, profit: +313u** |

## Per-region V67 sample restored

| Region | Eager (V72) | STRICT (V68) | Original V67 |
|---|---:|---:|---:|
| MN | 5/5 = 100% | 2/2 = 100% (cut 3 winners) | 5/5 = 100% |
| MT | 2/6 = 33% | 1/2 = 50% | 2/6 = 33% |
| MB | 3/6 = 50% | 3/6 = 50% | 3/6 = 50% |

→ MN single-source picks (5 days) restored. MT eager exposes original 4/6 misses but those were never propagated to HYBRID (HYBRID picks consensus). MB unchanged.

## Why downstream rates didn't change

CONSENSUS_V1 và HYBRID_V1 chưa bao giờ filter qua V67 STRICT — chúng dùng `agreement_count >= 3` riêng. Gate STRICT chỉ ảnh hưởng V67 standalone metric.

Nhưng owner đúng về một thứ: **agreement counts tăng** sau revert vì V67 đóng góp thêm input. Ví dụ:
- 2026-05-06 MN consensus: 5-method (STRICT) → **6-method (eager)**
- 2026-05-05 MB consensus: 4-method → **5-method**

Higher agreement = stronger downstream signal robustness, dù hit rate top-line stable.

## Current balanced state (per owner)

| Layer | Status |
|---|---|
| Strength tensor | ✅ daily refresh, 4 windows, 3 grains |
| C-16 budget | ✅ 20 voters all regions (MN=20, MT=20, MB=20) |
| V66.1 lag-1 signal | ✅ 11 flow_types daily |
| V67 ADAPTIVE_EXPLOIT_V1 | ✅ **eager** (revert STRICT) |
| V70 CONSENSUS_V1 | ✅ gate ≥3 method agreement |
| V71 HYBRID_V1 | ✅ CROWN/HIGH/MEDIUM/LOW/SKIP tier |
| Cron schedule | ✅ 23:35/40/45/48 VN daily |
| Pre/post hashes | ✅ UNCHANGED 4 official tables |

## Verification

- VPS deploy 02:13 VN, `/api/health=200`.
- Counts UNCHANGED on LOCAL+VPS.

## Raw paths

- `web/backend/_materialize_adaptive_exploit_v1.py` (STRICT constants 0/0.0)
- `artifacts/v71_hybrid_audit/v71_full_eval_after_revert.txt`
- CHANGELOG `V20.3.37.72`
- FU-138; SSOT V72 row; AUTOMATION_STATE seq=13
- Public Notion `V72_REVERT_STRICT_GATE_20260507`

STATUS: **V72_BALANCED_FINAL_STATE — V67 eager + 20 voters + CONSENSUS gate**.
