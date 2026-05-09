# Open issues — as of V98 (2026-05-09)

## Resolved this session (V98 + V98.1)

V98 (đêm 2026-05-09 00:50 VN):
- ✅ **FU-169** Public reports stale V92/V74 — published V98 wrapper, LATEST_REPORT.json + README + REPORT_INDEX updated to V98.
- ✅ **FU-176** /monitoring V98 Command Center — deployed 10 panels admin-locked auto-refresh 60s.
- ✅ V93→V97 documented and traced (private commit `1cd2833` synced to public V98 wrapper).

V98.1 (sáng 2026-05-09 09:30 VN):
- ✅ **FU-172** Cron 23:45+ misfire post service restart — 6/6 cron đêm qua fired naturally (V93.2 stdout fix VERIFIED).
- ✅ **FU-V97.1-CRON-MISFIRE** — root cause: APScheduler misfire grace time after fresh restart only.
- ✅ **FU-V97.1-LOG-PERSIST** — FALSE_NEGATIVE_RESOLVED (em đã misread SQLite UTC CURRENT_TIMESTAMP as VN local).
- ✅ V97 SP-4.1 LIVE FIRST CYCLE confirmed: MN cascade 04:24 VN produced final_bundle MN BT=05 target_date=2026-05-09.

## Active items (post V98.1)

| FU | Severity | Title | Earliest decision |
|---|---|---|---|
| **FU-170** | P1 | Notion `Lottery_AI_Test` V93-V97 sync UNVERIFIED (no MCP in Cursor scope) | Owner provide MCP/screenshot |
| **FU-171** | P1 | 4 file local↔VPS md5 drift (V93.1/V94.1/V95 materializers; runtime is OK) | 2026-05-14 |
| **FU-173** | P1 | Bundle conversion replay 30d evidence — defer | 2026-05-21 14d gate |
| **FU-174** | P1 | Combo-super BT-first replay (combo_super.py uses WR not BT) | 2026-05-21 14d gate |
| **FU-175** | P1 | Prompt context injection dossier per region | 2026-05-21 14d gate |
| FU-V96-AUDIT-3 | P1 | combo_super uses WR not BT (BT-first North Star violation) | tied to FU-174 |
| FU-V96-AUDIT-4 | P1 | combo_super hardcode 6 AI (model_registry SSOT violation) | tied to FU-174 |
| ~~FU-172~~ | — | ~~Cron 23:45+ misfire~~ | ✅ DONE V98.1 |
| ~~FU-V97.1-CRON-MISFIRE~~ | — | ~~APScheduler 23:45+ post-restart~~ | ✅ DONE V98.1 |
| ~~FU-V97.1-LOG-PERSIST~~ | — | ~~scheduler_logs stops persisting~~ | ✅ FALSE_NEGATIVE_RESOLVED V98.1 |

## Calendar gates

- ✅ 2026-05-09 04:24 VN: MN cascade với SP-4.1 prompt FIRED — final_bundle MN BT=05 generated (first V97 prediction live)
- 2026-05-09 16:30-18:30 VN: MT + MB cascade with SP-4.1
- 2026-05-09 19:14-19:22 VN: 5 cron shadow chain (V81/V93.1/V94.1/V95/V96)
- 2026-05-09 23:35-23:55 VN: V93.2 fix cron continuing clean fire
- 2026-05-12: 4 P0 methods reach 14d sample
- 2026-05-14: V79/V80/V81 7d rolling + MB cold gate
- 2026-05-21: 14d full + MN dossier + V94.1+V95 14d evidence + FU-165/174/175
- 2026-06-06: 30d sweep
- 2026-06-08: FU-162/164/166/167 30d evidence proposals
- 2026-07-06: 60d full review
