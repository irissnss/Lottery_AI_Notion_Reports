# Open issues for 2026-05-07 as of V76

## ✅ Resolved during V74-V76 sessions

1. **README stale** → fixed (V74)
2. **Missing GitHub discovery metadata** → fixed (V74)
3. **C-16 budget at 15** → fixed to 20 (V74 + V71 patch)
4. **CONSENSUS_V1 14d empty** → re-backfilled (V74)
5. **C-03 PENDING 37 rows** → reduced to 9 (V74)
6. **C-17B output_lock_status missing** → column added 669 rows backfilled (V74)
7. **C-05 latency live broken** → was data lag, RESOLVED 2026-05-07 20/42 captured (V74.1)
8. **Continuous measurement doctrine** → 4 governance docs locked (V74)
9. **GitHub README + discovery files** → 8 files created (V74)
10. **Daily evidence pack** → bootstrapped (V74)
11. **V76 P0-1 Drift detector** → deployed alert-only (this session)
12. **V76 P0-2 C-16 latency_score live** → deployed no-prune (this session)
13. **V76 P0-3 Cost provider table** → deployed tracking-only (this session)

## 🟢 No open P0 items

All P0 items closed in V76. Cron daily 23:35-23:50 VN will continuously measure and alert.

## 🟡 P1 watch (next session)

1. Drift alerts will activate after 14 fresh days (target 2026-05-21).
2. C-16 latency_score has rolling 7d avg active from 2026-05-13 onwards (need ≥2 valid days).
3. Cost provider table prices are estimates; owner can edit `_provider_pricing_table.py` to update with real provider invoices.

## ⏳ Always-on (continuous measurement)

- 5 cron jobs daily VN: 23:35 V66, 23:40 V67, 23:45 V70, 23:48 V73, 23:50 V76 drift.
- Daily evidence pack auto-generation.
- Drift alerts will surface RED/YELLOW/ORANGE when methods drift, degrade, or consensus weakens.
- Window gates 7/14/30/60/90/180 days are CHECKPOINTS, not stop points.

## P1 / P2 next steps

- P1: method interaction trace, C-16 top-20 audit surface, UI dashboard, per-station consensus.
- P2: OFFICIAL_PROMOTION_DOSSIER draft, region-specific candidates, Lo3/Xien consensus.
- P3: NO_TOKEN local timing, Cohere wide-pool, production cascade strength-ordering (owner gate).
