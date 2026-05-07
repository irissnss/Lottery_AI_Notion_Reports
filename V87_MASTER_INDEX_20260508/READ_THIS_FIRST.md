# V87 — read this first

Owner: /monitoring là nơi tổng hợp toàn bộ — phải triger, realtime, trực quan, hỗ trợ Agent IDE.

## What's new

- **`/api/admin/master-board`** (admin-only READ-ONLY) — 1 endpoint trả 12 categories đầy đủ.
- **`sectionV87MasterIndex`** trong `/monitoring` với 12 tabs:
  Models / Prompts / Rules / Mechanisms / Metrics / Shadow Methods / DB Tables / Cron / Frontend / API / Decision Calendar / Owner Gate.
- **Tab pattern**: dùng existing `region-tabs` UI; cached payload, switch tab không re-fetch.
- **Auto-refresh 60s** cùng các section khác.

## Hard locks

- READ-ONLY backend (zero write SQL).
- NO promote / rollback / edit / trigger button.
- NO scoring / selector / output mutation.
- 4 official tables hash UNCHANGED.

## Owner action

1. Login admin → truy cập `/monitoring`.
2. Cuộn xuống section "📚 V87 Master Index".
3. Click 12 tabs để xem từng category.

## Agent IDE action

- Gọi `GET /api/admin/master-board` (admin auth) để có 1 payload tổng.
- Schema: `v87_master_board_v1`.

Main: [V87_REPORT.md](V87_REPORT.md)
Source of truth: [LATEST_REPORT.json](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/LATEST_REPORT.json)
