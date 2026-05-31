# V10659 — UI Dependency Guard + Zombie Post-Draw Writers Disabled

Public-safe report for owner and external AI review tools.

## 1. Why This Was Needed

Owner correctly warned that `/du-doan-test` and `/monitoring` are not disposable surfaces. They depend on historical measurement/shadow tables. A table may be stale or marked `DEAD`, but it can still be useful as measurement history for UI panels.

Therefore cleanup must be dependency-first:

- Do not drop DB tables by label alone.
- Protect anything used by `/du-doan-test` or `/monitoring`.
- Stop bad writers before deleting any historical data.
- Keep private runtime code in the private repository; keep analysis/reporting here.

## 2. What Was Corrected

An earlier cleanup attempt partially removed 9 historical shadow tables. A backup existed, and all 9 were restored immediately.

Restored row count: **15,158 rows**.

Restored table group:

- Cross-region / bundle coverage measurement tables.
- Corrected rescue / tier replay measurement tables.
- Structural/drilldown shadow history tables.

Public-safe principle: these tables are now treated as `KEEP_UI_HISTORY` until a compact replacement summary is built and verified.

## 3. New Guardrails

Added a dependency map in the private repo:

- `/du-doan-test` endpoint and panel dependencies.
- `/monitoring` endpoint and panel dependencies.
- Cleanup labels such as `ACTIVE_RUNTIME` and `KEEP_UI_HISTORY`.

Added a read-only UI smoke script in the private repo:

- Checks `/login`.
- Checks `/du-doan-test`.
- Checks `/monitoring`.
- Can optionally check authenticated JSON APIs when admin credentials are provided locally.

Live unauthenticated smoke result:

- `/login` → `200`
- `/du-doan-test` → `401` expected, admin-protected
- `/monitoring` → `401` expected, admin-protected

## 4. Zombie Writers Disabled

Disabled remaining post-draw zombie writers while preserving all historical tables for UI reading:

- V101 regional source-pool writer at 19:23.
- V104 prompt-injection materializer at 19:24.
- V105 lane-test control backup writer at 19:34.

V104 Phase B provider pilot had already been disabled earlier.

This means:

- No new post-result rows are added by the stale prompt/candidate chain.
- Historical tables remain available for `/du-doan-test` and `/monitoring`.
- No official prediction logic was changed.
- No DB table was dropped after the restore.

## 5. Private vs Public Separation

Private repository (`Lottery_AI_Test`):

- Runtime code and scheduler guard.
- UI dependency map.
- Read-only smoke script.
- SSOT/changelog/follow-up tracker updates.

Public repository (`Lottery_AI_Notion_Reports`):

- This report.
- Public-safe summary for external AI tools.

## 6. Current Status

Private code commit: `a3620b9`.

Status:

- Private pushed.
- VPS already updated and service verified active.
- Public report published in this folder.
- Root cleanup was intentionally skipped by owner; no file move/delete was done.

## 7. Next Safe Step

Do not drop any measurement table next. The next safe improvement is authenticated smoke coverage for the exact JSON panels behind `/du-doan-test` and `/monitoring`, using local admin credentials only.

