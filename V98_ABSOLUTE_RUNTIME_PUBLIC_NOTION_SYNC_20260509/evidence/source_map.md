# V98 Source Map (verified 2026-05-09 00:50 VN)

| Source | URL / path | Latest identifier | Trust tier |
|---|---|---|---|
| Private git | github.com/irissnss/Lottery_AI_Test | commit `1cd2833` (V93-V97 batch) | T0 |
| Local CHANGELOG | E:/Lottery_AI_Test/CHANGELOG.md | V20.3.37.97.1 + V98 (this session) | T0 |
| Local SSOT | E:/Lottery_AI_Test/docs/CURRENT_TRUTH_SSOT.md | V97 row + V98 (this session) | T0 |
| Local FU tracker | E:/Lottery_AI_Test/docs/FOLLOW_UP_TRACKER.md | FU-159..168 + FU-V96-AUDIT-1..9 + FU-V96-MASTER + FU-169..176 (V98) | T0 |
| Local AUTOMATION | E:/Lottery_AI_Test/docs/AUTOMATION_STATE.json | seq 41 → 42 (V98) | T0 |
| Local DECISION | E:/Lottery_AI_Test/docs/DECISION_LOG.md | DEC-019-PROMPT-2NUM (FINAL) | T0 |
| Local V96 master index | E:/Lottery_AI_Test/docs/V96_MASTER_TRACKING_INDEX.md | V97 + V98 (this session) | T0 |
| VPS git | vietnix:/root/Lottery_AI_Test | `ceb36c2` V17.19.4 (2026-04-19) — modified-via-scp | T0 |
| VPS runtime | https://xs.io.vn | health=200, all admin endpoints 401-locked, /du-doan=200 | T0 |
| VPS DB | /root/Lottery_AI_Test/data/lottery_ai.db | predictions=4542 / final_bundles=210 / lottery_results=14634 / model_daily_eval=4493 | T0 |
| Local DB sync | manifest 2026-05-09 00:30 VN | identical to VPS | T0 |
| Public reports repo | github.com/irissnss/Lottery_AI_Notion_Reports | LATEST_REPORT.json was V92, now V98 | T1 |
| Notion `Lottery_AI_Test` | Notion workspace | UNVERIFIED (no MCP in Cursor scope) | T2 |

## File md5 parity (Pass-2 verified 2026-05-08 22:36 VN, restored 2026-05-09 00:30)

### MATCH (7 files)
- `web/backend/main.py` (latest after V98 add /api/admin/v98-command-center)
- `web/backend/gpt_analyzer.py` (V97 SP-4.1)
- `web/backend/scheduler.py`
- `web/backend/combo_super.py`
- `web/backend/model_registry.py`
- `web/backend/_v96_master_tracker.py`
- `web/frontend/monitoring.html` (latest after V98 sectionV98CommandCenter)

### DRIFT (4 files — FU-171)
- `web/backend/_materialize_v93_p0_shadow_audits.py`
- `web/backend/_materialize_v94_safe_batch.py`
- `web/backend/_materialize_v95_data_integrity_audit.py`
- `web/backend/_v95_dashboard.py`

→ **Severity P1**: Runtime OK because VPS = truth runtime. Local accidentally edited (likely formatting). FU-171 to reconcile.
