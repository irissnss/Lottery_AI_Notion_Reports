# Lottery AI Notion Reports

**Latest version: V10667.1 (Detailed Per-Region Rules + Bộ Numbering Legend)**

## ⚠️ Read first

[**📖 V10667_BO_NUMBERING_LEGEND.md**](./V10667_RULES_PER_REGION_DETAILED_PUBLIC_SAFE/V10667_BO_NUMBERING_LEGEND.md) — explains how `Giải X bộ Y` notation maps to positions on lottery result board. Owner explicitly marked G.4 MB (4 bộ) — `Bộ 1=top-left, Bộ 2=top-right, Bộ 3=bottom-left, Bộ 4=bottom-right`.

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
