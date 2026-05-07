# NEXT ACTION (2026-05-08)

V87 Master Index đã ship. /monitoring giờ là single-source dashboard.

## Owner action right now

- Đăng nhập admin và truy cập **`/monitoring`** (https://xs.io.vn/monitoring).
- Cuộn xuống section "📚 V87 Master Index — toàn bộ hệ thống ở 1 chỗ (12 tab)".
- Click 12 tabs:
  - 🧬 Models (41)
  - 💬 Prompts (5+3+5+3)
  - 📐 Rules
  - ⚙️ Mechanisms
  - 📊 Metrics (8 C-XX + 3 PB + 16 flip)
  - 🌒 Shadow Methods (59)
  - 🗄️ DB Tables (129)
  - ⏰ Cron (26)
  - 🎨 Frontend (12)
  - 🔌 API (132)
  - 📅 Decision Calendar (11 với T+/T-)
  - 🔒 Owner Gate (9)

## Agent IDE action

Gọi `GET /api/admin/master-board` (admin auth) — 1 endpoint, 12 categories, đầy đủ.

## Until next session (automated)

- 26 cron jobs daily VN.
- /monitoring auto-refresh 60s.
- Decision calendar tự kích hoạt tại các mốc.

## Owner-gate (no auto-action)

1. Selector promotion (any).
2. Official prompt change.
3. Production model swap.
4. V88+ extension (live cron last_run, settings, migration, backup, full FU).
