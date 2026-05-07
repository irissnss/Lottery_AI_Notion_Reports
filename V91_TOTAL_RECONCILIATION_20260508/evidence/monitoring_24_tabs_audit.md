# V91 — /monitoring 29-tab audit

Generated 2026-05-08T01:19:20+07:00

Owner asks: 24 tabs có đủ không. Verified 29 tabs (V90 added 5 final tabs).

| Tab | Backend key | Count | Source | Owner usefulness | Action |
| --- | --- | --- | --- | --- | --- |
| 🧬 Models | models | 41 | MODEL_REGISTRY | HIGH (lookup model status/provider/region) | OK |
| 💬 Prompts | prompts | 8 layers + 5 PFG cohorts + 3 V81 pilot | gpt_analyzer.py + shadow MD | HIGH (lookup PB-18 cohort/active prompt) | OK |
| 📐 Rules (PB-18) | rules | weekly_mining + 4 rule_shadow methods | mined_rules + gpt_analyzer PB-18 | MEDIUM | OK |
| ⚙️ Mechanisms | mechanisms | 8 cascade steps + 9 bundle gate + V77 + anti-herding + 6 keys | scheduler + main.py + audit | HIGH | OK |
| 📊 Metrics | metrics | 8 C-XX + 3 PB/PP + 16 flip | shadow_method_scoreboard + V52 measurement | HIGH | OK |
| 🌒 Shadow Methods | shadow_methods | 59 | shadow_activation_registry + V52.5 + selectors | HIGH | OK |
| 🗄️ DB Tables | db_tables | 129 | sqlite_master live | MEDIUM | OK |
| ⏰ Cron | cron_jobs | 26 | scheduler.py registrations | HIGH | OK |
| 🎨 Frontend | frontend_pages | 12 | web/frontend/*.html | MEDIUM | OK |
| 🔌 API | api_endpoints | 132 (24 admin + 86 public + 22 page) | main.py @app.* parse | MEDIUM | OK |
| 📅 Decision Calendar | decision_calendar | 11 | static V84 calendar | HIGH | V91: hardened with pass/fail conditions |
| 🔒 Owner Gate | owner_gate_queue | 9 | static V84 queue | HIGH | OK |
| ⚙️ Settings | settings | 252 | app_settings DB (ai_keys redacted) | HIGH | OK |
| 📜 Automation History | automation_history | 28 | AUTOMATION_HISTORY.jsonl | HIGH | OK |
| 📋 FU History | fu_items_full | 154 | FOLLOW_UP_TRACKER parse | HIGH | V91: 74/154 stale resolved |
| 🗓️ Phase Checkpoints | phase_checkpoints | 116 | artifacts/phase_checkpoints/*.md | MEDIUM | OK |
| 💾 VPS Backups | vps_backups | 31 | manual catalog (last ssh ls) | LOW | OK; refresh manually if needed |
| 📓 Notion Docs | notion_docs | 15 | Notion MCP search | HIGH (Open ↗ link) | OK |
| 🛠️ Migrations | migrations | 3 | web/backend/migration_*.py | LOW | OK |
| 🔴 Live Cron | live_cron | 26 jobs realtime | APScheduler runtime + scheduler_logs | HIGH (next_run badge) | OK |
| 🔎 FU Audit | fu_audit | 152→154 items / 74 stale | FU vs CHANGELOG cross-check | HIGH | V91: reconciled 67/74 = 90% resolvable docs-only |
| 🔬 Phase Findings | phase_findings | 116 | first paragraph extract | MEDIUM | OK |
| ⚖️ Decision Log | decision_log | 22 | DECISION_LOG.md | HIGH | V91: per-decision tracking spec |
| 📓 Governance Ledger | governance_ledger | 96 | CHANGELOG_GOVERNANCE_LEDGER.md | MEDIUM | OK |
| 🐍 Backend Modules | backend_modules | 293 | web/backend/*.py | MEDIUM (legacy audit scripts visible) | OK; cleanup legacy is separate task |
| 📜 Scripts | scripts | 19 | scripts/*.py | LOW | OK |
| 🛠️ Web Helpers | web_helpers | 42 | web/*.py | LOW | OK |
| 🗺️ Active Roadmaps | active_roadmaps | 2 | docs/ACTIVE_ROADMAP_*.md | HIGH (workspace rule) | OK |
| ⚖️ Cursor Rules | cursor_rules | 3 | .cursor/rules/*.mdc | LOW | OK |
