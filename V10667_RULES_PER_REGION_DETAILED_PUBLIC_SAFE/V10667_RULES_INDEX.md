# V10668 — Rules per Region — Index Hub (TEMPORAL-FIXED)

> **Generated**: 2026-06-02T10:32:49+07:00
> **Patch**: V10668 TEMPORAL CAUSALITY FIX — đã loại 266 cells vi phạm thứ tự xổ
> **BH-pass valid (sau fix)**: 232 cells (đã loại 36 BH-pass temporal-invalid)
> **Forward audit window**: 90 ngày, anchor 2026-06-02 → closeout 2026-08-31 (28 rule valid)

## ⚠️ Temporal Causality (đọc trước)

Thứ tự xổ: **MN (~16:10) → MT (~17:10) → MB (~18:15)**. Rule "nguồn xổ SAU đích cùng ngày" đã bị loại (MT(D)→MN(D), MB(D)→MN(D), MB(D)→MT(D)). Chi tiết: [V10668_TEMPORAL_CAUSALITY_PATCH_NOTICE.md](./V10668_TEMPORAL_CAUSALITY_PATCH_NOTICE.md).

## ⚠️ Bộ Numbering (đọc trước)

Ký hiệu `Giải X bộ Y`: xem [V10667_BO_NUMBERING_LEGEND.md](./V10667_BO_NUMBERING_LEGEND.md).

## Tài liệu rule theo từng miền target

| Target | Tài liệu | Note |
|---|---|---|
| **MB** | [V10667_RULES_MB_TARGET.md](./V10667_RULES_MB_TARGET.md) | 1 đài, xổ cuối → KHÔNG bị giới hạn temporal same-day |
| **MN** | [V10667_RULES_MN_TARGET.md](./V10667_RULES_MN_TARGET.md) | xổ đầu → CHỈ dùng lag≥1 hoặc MN self-lag |
| **MT** | [V10667_RULES_MT_TARGET.md](./V10667_RULES_MT_TARGET.md) | xổ giữa → dùng MN(D) same-day OK, MB(D) bị loại |

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