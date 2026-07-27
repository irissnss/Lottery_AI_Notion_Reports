# V10868 — Edge Tools diagnostics + Bugbot review

## Screenshot diagnosis

The Problems badge showed 129 warnings for `web/frontend/monitoring.html`; it did not show
129 application/runtime failures.

- 125 warnings: Microsoft Edge Tools/webhint `no-inline-styles`.
- 4 warnings: `compat-api/css` for intentional `color-mix()` use with Chrome versions below 111.

This static dashboard intentionally uses inline/dynamic presentation, and production targets
modern browsers. Mechanically moving 125 declarations would create UI regression risk without
fixing runtime behavior.

## Fix

Added project `.hintrc` with targeted overrides:

- `no-inline-styles: off`;
- `compat-api/css: off`.

Post-fix IDE diagnostics: 0.

## Bugbot findings

| Severity | Location | Finding | Resolution |
|---|---|---|---|
| High | `backups/_commit_v10785.cmd:7` + 7 peers | Private helpers pushed `origin main` while canonical private branch is `master` | Changed to `origin master` |
| Medium | `backups/_commit_v10809*.cmd` | Bare commit commands depended on caller CWD/staging | Added `@echo off`, exact repo CWD and intended `git add` |
| Medium | `backups/_phasea_db_check.py:6` | Relative DB path could open/fail against wrong DB | Repo-root absolute SQLite URI with `mode=ro` |

The repaired Phase-A probe then exposed another stale query: `experimental_preview_shadow`
uses `date`, not `run_date`. This was corrected and verified from a non-root working directory.

## Verification

- Active private helper scripts still pushing `origin main`: 0.
- Phase-A probe from `E:\Lottery_AI_Test\web`: exit 0.
- Phase-A `err:` markers: 0.
- IDE diagnostics for monitoring/config: 0.
- Runtime/VPS/DB/prediction/prompt/selector changes: none.

Bugbot review ID: `10d3dc55-7abe-402c-b429-f756a2a55d29`.

