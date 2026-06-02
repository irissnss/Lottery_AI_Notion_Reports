# V10667 — Detailed Rule Reference Per Region (PUBLIC-SAFE)

Tài liệu chi tiết cho 3 miền target (MN, MT, MB) với:
- Per-weekday breakdown (T2-CN)
- Per-station hit rate (đài nào contribute nhiều nhất)
- Worked examples (3 ngày gần nhất rule trúng)
- Strength classification (BH-pass, STRONG, MODERATE, MARGINAL, WEAK)

## 🕐 Read first #1 — TEMPORAL CAUSALITY (CRITICAL)

**[V10668_TEMPORAL_CAUSALITY_PATCH_NOTICE.md](./V10668_TEMPORAL_CAUSALITY_PATCH_NOTICE.md)**

Vietnam draws sequentially: **MN (~16:10) → MT (~17:10) → MB (~18:15)**.

A same-day cross-region rule where the source draws AFTER the target (MT(D)→MN(D), MB(D)→MN(D), MB(D)→MT(D)) is a TEMPORAL CAUSALITY VIOLATION — you'd be using data from the future. These 266 invalid cells (36 BH-pass) have been **removed**. Per region:
- **MN target** (draws first): only lag≥1 sources or MN self-lag
- **MT target** (draws 2nd): MN(D) same-day OK, MB(D) removed
- **MB target** (draws last): no same-day temporal limit

## ⚠️ Read first #2 — Bộ Numbering Convention

**[📖 V10667_BO_NUMBERING_LEGEND.md](./V10667_BO_NUMBERING_LEGEND.md)** — quy ước đánh số bộ cho mỗi giải (G2/G4/G6/G7 MB, G3 MN/MT).

Owner 02/06/2026 đã bổ sung G.4 MB làm nguồn rules. Mỗi bộ được đánh số rõ ràng theo position:

**G.4 MB (4 bộ):**
```
Bộ 1 [top-left]    Bộ 2 [top-right]
Bộ 3 [bottom-left] Bộ 4 [bottom-right]
```

Ví dụ verify MB 31/05/2026: G.4 bộ 1=7717, bộ 2=7829, bộ 3=5183, bộ 4=4559.

## Read next

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
