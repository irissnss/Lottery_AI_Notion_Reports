## V80 → V81

- Owner-approved provider shadow pilot deployed.
- New shadow table `ai_region_specialist_provider_shadow_results`.
- New cron 19:14 VN. Cron now 6 jobs daily.
- 3 models × 3 regions × 2 days backfill: 18/18 parse_ok, 0 breaks.
- Public root metadata reset to V81 (was stale at V77).

## V79 → V80

- Notion/code/runtime sync; 4 new shadow tables; cron 19:12 VN.

## V78 → V79

- AI ↔ NO_TOKEN cross-verification + cluster-weighted consensus shadow.

## V77 → V78

- Region-specialist shadow prompts + scheduler tzinfo fix.

# DELTA_INDEX

## V80 vs V79
V80 adds Notion sync and remaining shadow completion surfaces: rule-phase synthesis, no-token rule-aware pack, MB regime, MN V67-save monitor.
