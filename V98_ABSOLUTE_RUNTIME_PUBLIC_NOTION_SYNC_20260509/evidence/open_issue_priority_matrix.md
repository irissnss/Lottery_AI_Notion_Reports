# V98 Open Issue Priority Matrix

| FU | Priority | Severity | Title | Status | Decision date |
|---|---|---|---|---|---|
| **FU-169** | P0 | CRITICAL | Public reports stale V92/V74 vs private V97 | ✅ RESOLVED V98 | DONE |
| **FU-176** | P0 | HIGH | /monitoring V98 Command Center | ✅ RESOLVED V98 | DONE |
| **FU-170** | P1 | MEDIUM | Notion `Lottery_AI_Test` V93-V97 sync UNVERIFIED | OWNER_LOCK | Owner provide MCP/screenshot |
| **FU-171** | P1 | MEDIUM | 4 file local↔VPS md5 drift | OWNER_LOCK | 2026-05-14 |
| **FU-172** | P1 | MEDIUM | Cron 23:45+ misfire post service restart | OWNER_LOCK | 2026-05-09 (clean test no restart) |
| **FU-173** | P1 | MEDIUM | Bundle conversion replay 30d evidence | DEFER | 2026-05-21 14d gate |
| **FU-174** | P1 | MEDIUM | Combo-super BT-first replay (combo_super uses WR) | DEFER | 2026-05-21 14d gate |
| **FU-175** | P1 | MEDIUM | Prompt context injection dossier per region | DEFER | 2026-05-21 14d gate |
| FU-V96-AUDIT-3 | P1 | MEDIUM | combo_super uses WR not BT | tied to FU-174 | 14d gate |
| FU-V96-AUDIT-4 | P1 | MEDIUM | combo_super hardcode 6 AI | tied to FU-174 | 14d gate |
| FU-V96-AUDIT-5 | P1 | MEDIUM | V93-V97 not in public reports | ✅ RESOLVED V98 | DONE |
| FU-V97.1-CRON-MISFIRE | P1 | MEDIUM | APScheduler 23:45+ post-restart | tied to FU-172 | 2026-05-09 |
| FU-V97.1-LOG-PERSIST | P1 | MEDIUM | scheduler_logs DB stops persisting | OWNER_LOCK | 2026-05-14 |
| FU-159 | P0 | CRITICAL | V81 cron stdout bug | DEPLOYED_PENDING_LIVE_VERIFY | 2026-05-09 |
| FU-160 | P0 | CRITICAL | V93 P0 audit shadow tables | DEPLOYED_PENDING_LIVE_VERIFY | 2026-05-09 |
| FU-162 | P0 | CRITICAL | verdict_weight recalibration shadow | 30D_EVIDENCE_COLLECTING | 2026-06-08 |
| FU-163 | P1 | MEDIUM | V93.2 sibling stdout fix | PARTIAL — superseded by FU-172 | tied to FU-172 |
| FU-164 | P0 | CRITICAL | Cross-region leakage recurrence | DEPLOYED_PENDING_LIVE_VERIFY | 2026-06-08 |
| FU-165 | P1 | MEDIUM | RR-16.4 §9 D-2 region-gated update | OWNER_LOCK | 2026-05-21 |
| FU-166 | P0 | CRITICAL | Secondary signal survival V93 | OWNER_LOCK | 2026-06-08 |
| FU-167 | P1 | MEDIUM | Spillover-aware selector promotion proposal | 30D_EVIDENCE_COLLECTING | 2026-06-08 |
| FU-168 | P1 | MEDIUM | V95 data integrity + AI context | DEPLOYED_PENDING_LIVE_VERIFY | 2026-05-21 |

## Summary by status

| Status | Count |
|---|---|
| RESOLVED V98 | 3 (FU-169, FU-176, FU-V96-AUDIT-5) |
| DEPLOYED_PENDING_LIVE_VERIFY | 4 |
| 30D_EVIDENCE_COLLECTING | 3 |
| OWNER_LOCK / DEFER | 8 |
| PARTIAL | 2 |
| **Total active** | **16** |
