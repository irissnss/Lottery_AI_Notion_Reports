# Lottery AI Notion Reports

**Latest version: V10681 (Drop Tier-3, T1+T2 cross-verify per weekday — report-only, no code deploy)**

## Latest report for AI tools

- [**V10681_DROP_TIER3_T1_T2_CROSS_VERIFY_VN.md**](./V10667_RULES_PER_REGION_DETAILED_PUBLIC_SAFE/V10681_DROP_TIER3_T1_T2_CROSS_VERIFY_VN.md) — **NEW**
  - Owner-decision: drop Tier-3 (V10626 pre-register, 19 MB rules) — they all fail BH_FDR, lack `target_weekday`, contain duplicates, and have no rolling re-measure.
  - New design: **2-tier weekday-bound cross-verify** = T1 (35 production, drives score) + T2 (77 manual MB-target, CONFIRM-only).
  - Verify 54/54 PASS, MN/MT invariance 108/108 IDENTICAL, no VPS deploy.
- [V10680_MB_RULE_STACK_CLARIFICATION_AND_NEXT_STEPS_VN.md](./V10667_RULES_PER_REGION_DETAILED_PUBLIC_SAFE/V10680_MB_RULE_STACK_CLARIFICATION_AND_NEXT_STEPS_VN.md) — preceding clarification (T3 sections superseded by V10681; T1/T2/gates/test-lane sections still valid).

## ⚠️ Read first (4 critical notes)

1. [**🎯 V10670_SOURCE_SEMANTICS_LEGEND.md**](./V10667_RULES_PER_REGION_DETAILED_PUBLIC_SAFE/V10670_SOURCE_SEMANTICS_LEGEND.md) — **NEW**: how source notation works. `#Bộ` = position-in-prize NOT station. Multi-station source = UNION of all stations that weekday. Full station-by-weekday map (MB is per-province: T2=Hà Nội, T3=Quảng Ninh, T4=Bắc Ninh, T5=Hà Nội, T6=Hải Phòng, T7=Nam Định, CN=Thái Bình).
2. [**✅ V10669_TEMPORAL_VERIFICATION_REPORT_VN.md**](./V10667_RULES_PER_REGION_DETAILED_PUBLIC_SAFE/V10669_TEMPORAL_VERIFICATION_REPORT_VN.md) — comprehensive verification: OVERALL CLEAN=True. 232 BH-pass valid + 28 forward audit rules.
3. [**🕐 V10668_TEMPORAL_CAUSALITY_PATCH_NOTICE.md**](./V10667_RULES_PER_REGION_DETAILED_PUBLIC_SAFE/V10668_TEMPORAL_CAUSALITY_PATCH_NOTICE.md) — draw order MN(16:10)→MT(17:10)→MB(18:15); same-day source-after-target removed.
4. [**📖 V10667_BO_NUMBERING_LEGEND.md**](./V10667_RULES_PER_REGION_DETAILED_PUBLIC_SAFE/V10667_BO_NUMBERING_LEGEND.md) — `Giải X bộ Y` notation. G.4 MB (4 bộ): `Bộ 1=top-left, Bộ 2=top-right, Bộ 3=bottom-left, Bộ 4=bottom-right`.

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
