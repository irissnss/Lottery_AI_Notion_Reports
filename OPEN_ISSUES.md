# Open issues — as of V88 (2026-05-08)

## Resolved this session (V88)

1. /monitoring extended from 12 → 18 tabs.
2. Backend module extended with 6 new blocks (settings, automation_history, fu_items_full, phase_checkpoints, vps_backups, notion_docs).
3. TOTAL_ENCYCLOPEDIA.md (36 KB) single searchable file.
4. ~991 items reconciled across V85+V86+V87+V88.

## Active automated triggers (unchanged)

- 2026-05-08 6-cron natural proof.
- 2026-05-12 4 P0 methods 14d gate.
- 2026-05-14 V79/V80/V81 7d + MB cold gate.
- 2026-05-21 14d full + MN dossier + drift V76 active.
- 2026-06-06 30d sweep.
- 2026-07-06 60d V79/V80/V81.

## Owner-locked

- Selector promotion (any).
- Official prompt change.
- Production model swap.
- Global NO_TOKEN floor change.

## V89+ candidates (owner OK pending)

1. Migrations history parser (no formal schema_migrations table; parse `web/backend/migration_*.py` if needed).
2. Live cron last_run timestamps via APScheduler runtime.
3. Per-FU full audit (FU-001 → FU-100 status verify).
4. Per-phase_checkpoint findings extraction (~200 chars summary).
5. CHANGELOG_GOVERNANCE_LEDGER + DECISION_LOG entries inventory.
