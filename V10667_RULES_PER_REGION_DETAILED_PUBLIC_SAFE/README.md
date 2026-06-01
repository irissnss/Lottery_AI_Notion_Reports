# V10667 — Detailed Rule Reference Per Region (PUBLIC-SAFE)

Tài liệu chi tiết cho 3 miền target (MN, MT, MB) với:
- Per-weekday breakdown (T2-CN)
- Per-station hit rate (đài nào contribute nhiều nhất)
- Worked examples (3 ngày gần nhất rule trúng)
- Strength classification (BH-pass, STRONG, MODERATE, MARGINAL, WEAK)

## Read first

[`V10667_RULES_INDEX.md`](./V10667_RULES_INDEX.md) — hub navigation.

## 3 per-region documents

| Target | Document | Lines |
|---|---|---|
| **MB** | [V10667_RULES_MB_TARGET.md](./V10667_RULES_MB_TARGET.md) | 1,711 |
| **MN** | [V10667_RULES_MN_TARGET.md](./V10667_RULES_MN_TARGET.md) | 2,061 |
| **MT** | [V10667_RULES_MT_TARGET.md](./V10667_RULES_MT_TARGET.md) | 2,150 |

## Supplementary

- [V10667_RULES_FLAT_RANKING.md](./V10667_RULES_FLAT_RANKING.md) — flat ranking (all 3 regions in one MD)
- [machine_readable/V10667_RULES_PER_REGION_RAW.json](./machine_readable/V10667_RULES_PER_REGION_RAW.json) — structured per-station data
- [machine_readable/V10667_FORWARD_AUDIT_REGISTRY.json](./machine_readable/V10667_FORWARD_AUDIT_REGISTRY.json) — 35 BH-pass rules in forward audit

## Methodology summary

- **Data source**: V10636 series audit (CROSS + DIG + LAGS + MBSELF)
- **Total unique cells**: 3,696
- **p<0.05 raw**: 431
- **BH-pass FDR α=0.05**: 268 ⭐ (gold standard, survives multiple-testing correction)
- **Lift ≥ +5pp**: 357

## Owner constraints (applied)

- MN/MT G3 = source only (NO MB G3 source)
- MB source whitelist: DB, G1, G2, G4, G6, G7
- MN/MT source whitelist: DB, G1, G2, G3 (both bộ), G5, G7, G8

## Status

- All rules at `PRE_REGISTER_FORWARD_AUDIT`
- `live_eligible = False` for all
- Forward audit anchor: 2026-06-02
- Earliest closeout: 2026-08-31

Public push approved by owner for external AI tool consumption.

## Safety

- Read-only audit
- No DB/JSONL/log files
- No VPS IP, no API keys
- No official mutation
