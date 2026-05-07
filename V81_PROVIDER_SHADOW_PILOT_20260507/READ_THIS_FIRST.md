# V81 — read this first

Owner OK 2026-05-07 22:02 VN — provider shadow pilot.

Hard contract:
- 3 representative models (FAST_CHEAP=deepseek-chat, REASONING=claude-sonnet-4-6, NEW_CHEAP=gemini-3-flash).
- V78 region-specialist shadow prompts + V79 cluster-weighted context.
- All rows shadow_only=1, output_eligible=0, output_impact='false'.
- Official tables UNCHANGED.

2-day pilot (2026-05-06 + 2026-05-07): 18 provider calls, 18 parse_status=OK, 0 contract violations.

Each model scored hits=3/6, would_save=1, would_break=0.
- MN 2026-05-07: all 3 models converge on V67/V73 tail 95 vs OFFICIAL 94 (would_save).
- MT: stable consensus, no false override.
- MB: honest cold acknowledgement (LOW conf + herd warnings) — no overclaim.

Main: [V81_REPORT.md](V81_REPORT.md)
Source of truth: [LATEST_REPORT.json](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/LATEST_REPORT.json)

Cron: now 6 jobs daily VN — 19:00, 19:05, 19:08, 19:10, 19:12, **19:14 (NEW V81)**.
