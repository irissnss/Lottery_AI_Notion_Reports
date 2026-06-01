# V10667 — Rules per Region — Index Hub

> **Generated**: 2026-06-02T01:27:09+07:00
> **Total rules**: 3,696 unique cells aggregated từ V10636 series
> **BH-pass FDR α=0.05**: 268 cells (gold standard)
> **Forward audit window**: 90 ngày, anchor 2026-06-02 → closeout 2026-08-31

## Tài liệu rule theo từng miền target

| Target | Tài liệu | Số rule active | Note |
|---|---|---|---|
| **MB** | [V10667_RULES_MB_TARGET.md](./V10667_RULES_MB_TARGET.md) | 7 weekday cells | 1 đài MB_BOARD, evidence mỏng, V10.3 calibration ceiling 55% |
| **MN** | [V10667_RULES_MN_TARGET.md](./V10667_RULES_MN_TARGET.md) | 7 weekday cells | 3-4 đài/ngày, T7 Saturday = "hot day" 86 BH-pass |
| **MT** | [V10667_RULES_MT_TARGET.md](./V10667_RULES_MT_TARGET.md) | 7 weekday cells | 2-3 đài/ngày, T5 Thu + T7 Sat = "hot days" 175 BH-pass tổng |

## Owner constraints applied

- ✓ MN/MT G3 = source-only (không làm target)
- ✓ MB source whitelist: DB, G1, G2, G4, G6, G7 (NO G3)
- ✓ All rules at status `PRE_REGISTER_FORWARD_AUDIT`
- ✓ All rules `live_eligible = False`

## Aggregation sources

- V10636-CROSS: 2,387 cells cross-region (268 BH-pass)
- V10636-DIG: 784 MB self-lag cells
- V10636-LAGS: 1,260 MB D-1/D-2/D-3 cells
- Total dedup: 3,696 unique combinations

## Forward audit tracking

35 best BH-pass cells from V10636-CROSS được register vào 90-day forward audit (V10636_FORWARD_AUDIT_REGISTRY.json). Sau 90 ngày em sẽ classify:

- STRONG_SURVIVE (≥50% historical lift) → đáng promote COMMIT_ELIGIBLE_SHADOW (cần owner OK)
- MODERATE_SURVIVE (25-50%) → continue audit
- MARGINAL/NULL/NEGATIVE → DROP

## Strength scoring legend

| Tag | Condition | Recommendation |
|---|---|---|
| ⭐ STRONG (BH-pass) | Pass FDR α=0.05 | Most reliable, có thể trust |
| STRONG | p<0.01 lift ≥ +5pp | Đáng tham khảo |
| MODERATE | p<0.05 lift ≥ +3pp | Có ý nghĩa thống kê nhẹ |
| MARGINAL | p<0.05 lift < +3pp | Yếu, đợi audit |
| WEAK | p≥0.05 | KHÔNG nên dùng |

---

**STATUS**: Owner reference rules per region — read-only, no official mutation.