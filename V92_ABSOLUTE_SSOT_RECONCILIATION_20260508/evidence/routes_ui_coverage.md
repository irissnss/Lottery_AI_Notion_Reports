# V91 — Routes / UI coverage audit

Generated 2026-05-08T01:19:20+07:00

## Frontend page routes (12)

| Route | Auth | Role | Latest truth? | Owner-useful | Action |
|---|---|---|---|---|---|
| `/` | public | home | OK | LOW | OK |
| `/login` | public | auth | OK | LOW | OK |
| `/du-doan` | public | **production prediction** | YES (15 model output) | HIGH user-facing | DO_NOT_TOUCH |
| `/du-doan-test` | admin-only | experimental lane | YES (V52.5+, V57 budget) | HIGH admin | OK |
| `/du-doan-test?v=20260504-v52-6-source-badges` | admin-only | same page query refresh | YES | LOW (V52.6 fixed) | OK; query param chỉ là cache buster |
| `/monitoring` | admin-only | **single-source dashboard** | YES (29 tabs V90) | HIGHEST | OK; primary dashboard |
| `/v82-monitor` | admin-only | V83 standalone V82 monitor | YES | MEDIUM (also embedded /monitoring) | OK; kept for direct link |
| `/accuracy` | admin-only | accuracy review | OK | MEDIUM | OK |
| `/review-dashboard` | admin-only | review | OK | LOW | OK |
| `/search` | admin-only | search | OK | LOW | OK |
| `/settings` | admin-only | settings | OK | MEDIUM | OK |
| `/user-view` | public | compact user | OK | LOW | OK |
| `/viewer` | admin/public | generic viewer | OK | LOW | OK |

## Admin API endpoints (24)

Verified from main.py grep:
- `/api/admin/master-board` — V87+V88+V89+V90 master board (READ-ONLY 36 keys)
- `/api/admin/v82-monitor` — V83 V82 monitor (READ-ONLY)
- `/api/admin/parallel-shadow-proof` — V20.3.37.19 portfolio board
- `/api/admin/runtime-monitoring-center` — main monitoring data
- ~20 more admin endpoints (rules CRUD, predictions backfill, etc.)

All admin endpoints unauth = 401 verified.

## Coverage status

- ✅ `/monitoring` is single-source dashboard (29 tabs)
- ✅ `/v82-monitor` linked from /monitoring (V86 sectionV82MasterControl)
- ✅ `/du-doan-test` clearly test-lane (not official)
- ✅ `/du-doan` clearly production (DO_NOT_TOUCH)
- ✅ Agent IDE has `/api/admin/master-board` single endpoint

## No duplicate / no stale

After V90 audit: no stale route detected. /v82-monitor is intentional duplicate (both standalone + embedded).
