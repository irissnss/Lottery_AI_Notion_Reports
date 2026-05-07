# V83 — read this first

Owner OK 2026-05-07 23:14 VN: build UI admin read-only panel cho V82.

## What's new

- Route `GET /v82-monitor` — admin-only HTML dashboard.
- Route `GET /api/admin/v82-monitor` — admin-only JSON, 18-key payload.
- Backend module `_v82_monitor.py` — read-only payload builder.

## Hard locks

- READ-ONLY backend.
- Admin-only auth.
- NO promote/rollback/edit/trigger button.
- NO scoring change. NO selector change. NO official mutation.
- Pre/post hashes 4 official tables UNCHANGED.

## How to use (anh)

1. Login `/login` với admin account.
2. Truy cập `/v82-monitor`.
3. Auto-refresh 5 phút.

Main: [V83_REPORT.md](V83_REPORT.md)
Source of truth: [LATEST_REPORT.json](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/LATEST_REPORT.json)

Cron daily VN unchanged: 19:00-19:14 (6 jobs).
