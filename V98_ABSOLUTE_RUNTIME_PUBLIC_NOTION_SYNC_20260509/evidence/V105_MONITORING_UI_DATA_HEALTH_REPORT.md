# V105 — Monitoring UI + Data Health Report

## What Changed

- Added high-contrast V105 CSS classes to `/monitoring`.
- Added legacy contrast hardening after owner screenshots showed older V95/V103/V104 pastel inline cards with low-contrast text.
- Added `sectionV105LaneTestControl`.
- Registered `loadV105LaneTestControl()` in initial load and 60s refresh.
- Added explicit status badges: `OK`, `NO_DATA_YET`, `PROVIDER_FAIL`, `API_KEY_ROUTING_MISMATCH`, `PARSE_FAIL`, `CONTEXT_INCOMPLETE`, `DB_EMPTY`, `STALE_DATA`.
- Every V105 panel shows target date, last updated, row count, source table, status, reason if empty, and next expected cron.

## Current Runtime Data

| Panel | Status | Rows |
|---|---|---:|
| V104 Phase B Provider Health | PROVIDER_FAIL | 93 |
| AI Shadow Independence | OK | 93 |
| No-token Independent Shadow | OK | 7422 |
| Context Completeness | OK | 7515 |
| Data Empty Reason | OK | 0 |
| Prediction Quality Realtime | OK | 83 |

Provider status is `PROVIDER_FAIL` only because Gemini still has empty/parse rows. GPT routing and Claude truncation are fixed.

## Follow-up Contrast Patch

At 2026-05-10 01:45 VN, `web/frontend/monitoring.html` was deployed again to override legacy pastel inline card backgrounds to dark high-contrast surfaces. This is frontend-only and does not touch `/du-doan`, scoring, prompts, selectors, or official tables.

## Prediction Quality Panel

`/api/prediction-quality` now returns `data_health` with source, query date, row count, missing reason, V104/V105 shadow row counts, and `official_and_shadow_mixed=false`.
