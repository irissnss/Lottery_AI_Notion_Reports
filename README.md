# Lottery AI Notion Reports

**Latest version: V10669 (Per-Region Rules — TEMPORAL CAUSALITY FULLY VERIFIED)**

## ⚠️ Read first (3 critical notes)

1. [**✅ V10669_TEMPORAL_VERIFICATION_REPORT_VN.md**](./V10667_RULES_PER_REGION_DETAILED_PUBLIC_SAFE/V10669_TEMPORAL_VERIFICATION_REPORT_VN.md) — comprehensive verification: ALL artifacts scanned, OVERALL CLEAN=True. 232 BH-pass valid cells + 28 forward audit rules remain.
2. [**🕐 V10668_TEMPORAL_CAUSALITY_PATCH_NOTICE.md**](./V10667_RULES_PER_REGION_DETAILED_PUBLIC_SAFE/V10668_TEMPORAL_CAUSALITY_PATCH_NOTICE.md) — **CRITICAL**: Vietnam draws sequentially MN(16:10) → MT(17:10) → MB(18:15). Same-day rule where source draws AFTER target (e.g. MT(D)→MN(D)) is TEMPORAL VIOLATION and removed. 266 invalid cells filtered.
3. [**📖 V10667_BO_NUMBERING_LEGEND.md**](./V10667_RULES_PER_REGION_DETAILED_PUBLIC_SAFE/V10667_BO_NUMBERING_LEGEND.md) — `Giải X bộ Y` notation. G.4 MB (4 bộ): `Bộ 1=top-left, Bộ 2=top-right, Bộ 3=bottom-left, Bộ 4=bottom-right`.

## Quick navigation — per region rule docs

| Target | Detailed rules document |
|---|---|
| **Miền Bắc (MB)** | [V10667_RULES_MB_TARGET.md](./V10667_RULES_PER_REGION_DETAILED_PUBLIC_SAFE/V10667_RULES_MB_TARGET.md) |
| **Miền Nam (MN)** | [V10667_RULES_MN_TARGET.md](./V10667_RULES_PER_REGION_DETAILED_PUBLIC_SAFE/V10667_RULES_MN_TARGET.md) |
| **Miền Trung (MT)** | [V10667_RULES_MT_TARGET.md](./V10667_RULES_PER_REGION_DETAILED_PUBLIC_SAFE/V10667_RULES_MT_TARGET.md) |
| **Index hub** | [V10667_RULES_INDEX.md](./V10667_RULES_PER_REGION_DETAILED_PUBLIC_SAFE/V10667_RULES_INDEX.md) |

## Tài liệu chứa gì

Mỗi tài liệu MB/MN/MT có:
- 7 sections (T2 → CN)
- Mỗi section: top 8-12 rule mạnh nhất
- Mỗi rule có:
  - Mô tả tiếng Việt cách áp dụng
  - Bảng per-station (đài nào hit nhiều nhất)
  - 3 ngày gần nhất rule trúng (worked examples)
  - p-value, BH-pass, strength classification

## Methodology

- V10636 series audit: 3,696 unique rule combinations tested
- **268 BH-pass cells** (gold standard, FDR α=0.05)
- 357 cells với lift ≥ +5pp
- 35 best rules registered into 90-day forward audit (anchor 2026-06-02 → closeout 2026-08-31)

## Owner constraints applied

- MN/MT G3 = source only (không làm target)
- MB source whitelist: DB, G1, G2, G4, G6, G7

## Status

All rules: `PRE_REGISTER_FORWARD_AUDIT`, `live_eligible=False`.
No official mutation. Read-only research.

For previous versions, see `REPORT_INDEX.md`.
