# Open issues — as of V98 (2026-05-09)

## Resolved this session (V98)

- ✅ **FU-169** Public reports stale V92/V74 — published V98 wrapper, LATEST_REPORT.json + README + REPORT_INDEX updated to V98.
- ✅ **FU-176** /monitoring V98 Command Center — deployed 10 panels admin-locked auto-refresh 60s.
- ✅ V93→V97 documented and traced (private commit `1cd2833` synced to public V98 wrapper).

## Active items (V98 owner-gated)

| FU | Severity | Title | Earliest decision |
|---|---|---|---|
| **FU-170** | P1 | Notion `Lottery_AI_Test` V93-V97 sync UNVERIFIED (no MCP in Cursor scope) | Owner provide MCP/screenshot |
| **FU-171** | P1 | 4 file local↔VPS md5 drift (V93.1/V94.1/V95 materializers; runtime is OK) | 2026-05-14 |
| **FU-172** | P1 | Cron 23:45+ misfire post service restart (V70/V73/V76/C16) | 2026-05-09 (clean test) |
| **FU-173** | P1 | Bundle conversion replay 30d evidence — defer | 2026-05-21 14d gate |
| **FU-174** | P1 | Combo-super BT-first replay (combo_super.py uses WR not BT) | 2026-05-21 14d gate |
| **FU-175** | P1 | Prompt context injection dossier per region | 2026-05-21 14d gate |
| FU-V96-AUDIT-3 | P1 | combo_super uses WR not BT (BT-first North Star violation) | tied to FU-174 |
| FU-V96-AUDIT-4 | P1 | combo_super hardcode 6 AI (model_registry SSOT violation) | tied to FU-174 |
| FU-V97.1-CRON-MISFIRE | P1 | APScheduler 23:45+ post-restart misfire | tied to FU-172 |
| FU-V97.1-LOG-PERSIST | P1 | scheduler_logs DB stops persisting after 16:35 VN | 2026-05-14 |

## Calendar gates

- 2026-05-09 16:30 VN: MN/MT/MB cascade — first natural fire AI với SP-4.1 prompt
- 2026-05-09 19:14-19:22 VN: 5 cron shadow chain (V81/V93.1/V94.1/V95/V96)
- 2026-05-09 23:35-23:55 VN: V93.2 fix cron clean test
- 2026-05-12: 4 P0 methods reach 14d sample
- 2026-05-14: V79/V80/V81 7d rolling + MB cold gate
- 2026-05-21: 14d full + MN dossier + V94.1+V95 14d evidence + FU-165/174/175
- 2026-06-06: 30d sweep
- 2026-06-08: FU-162/164/166/167 30d evidence proposals
- 2026-07-06: 60d full review
