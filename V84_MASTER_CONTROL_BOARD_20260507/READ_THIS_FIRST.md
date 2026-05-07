# V84 — read this first

Owner directive: 1 bảng duy nhất gom toàn bộ tồn đọng V63→V83. Không "chờ thêm" mơ hồ.

## What's in V84

- **Master Control Board** (`evidence/master_control_board.md`) — 24 dòng covering OFFICIAL/V52.5/V67/V70/V73/V76/V77/V78/V79/V80/V81/V82/V83/P0_18_methods/Wave1/Wave2/D-items/Timezone/Hash. Mỗi dòng có ngày trigger, decision_date, pass/fail, owner_gate.
- **Method maturity matrix** (`evidence/method_maturity_matrix.md`) — 18 P0 methods. 14 READY_TO_EVALUATE, 4 WAIT 5 ngày (đến 2026-05-12).
- **Decision calendar** (`evidence/decision_calendar.md`) — 11 ngày VN cụ thể từ 2026-05-08 → 2026-07-06.
- **Region queues** — MN recovery, MT protection, MB forensic.
- **Owner-gate queue** — 9 items chờ owner action với trigger_date.

## Hard locks (do-not-touch)

- 4 official tables hash UNCHANGED (predictions / final_bundles / lottery_results / model_daily_eval).
- No selector promotion without dossier + owner OK.
- No global NO_TOKEN floor change (region-specific delta differ).
- No official prompt change.

Main: [V84_REPORT.md](V84_REPORT.md)
Source of truth: [LATEST_REPORT.json](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/LATEST_REPORT.json)
