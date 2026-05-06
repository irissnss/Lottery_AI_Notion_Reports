# V62 System Audit — Part 1 Current Day 2026-05-06

**Sync manifest:** `artifacts/live_sync/20260506_224044/manifest.json`

## Current status by region

### MN

- Official bundle exists: see `01_current_day_state.json`.
- `/du-doan-test` pre-result ran in `REALTIME_AVAILABLE_ONLY`.
- C-16 budget exists.
- Lottery actual may now be present depending on late sync; check DB proof JSON.

### MT / MB

- Readiness depends on final bundle + no actual results + no test bundle.
- Dynamic trigger runs every 5 minutes, readiness-gated.

## Important

This report does not mutate official output. It reads synced DB/log state and summarizes current issues.
