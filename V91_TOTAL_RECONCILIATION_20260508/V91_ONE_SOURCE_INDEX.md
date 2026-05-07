# V91_ONE_SOURCE_INDEX — Lottery AI Test (single Notion lookup)

Generated 2026-05-08T01:19:20+07:00

> **One file** Notion AI có thể paste link để query toàn bộ.

## 0. Latest pointer (verified V90)

- latest_version: V90
- latest_folder: V90_FINAL_CLEANUP_20260508
- 29 tabs total trong /monitoring V87 Master Index
- ~1378 distinct items reconciled
- 4 official tables hash byte-identical V77 → V90

## 1. /monitoring 29 tabs

Tab list trong [`monitoring_24_tabs_audit.md`](monitoring_24_tabs_audit.md).

## 2. V91 reconciliation summary

| Class | Count |
|---|---|
| Total FU parsed | 154 |
| Stale flagged | 74 |
| **STALE_FU_SUPERSEDED** (older, subsumed by V74+) | 54 |
| **STALE_FU_RESOLVED** (recent FU with hist/gov proof) | 13 |
| **STALE_FU_NEEDS_RUNTIME** (live verify needed) | 7 |

→ 67/74 = **90% docs-only resolvable** trong V91 batch update.

## 3. Decision calendar (hardened with pass/fail + auto-report)

11 mốc cụ thể trong [`decision_calendar_hardened.md`](decision_calendar_hardened.md).

## 4. Owner-gate queue (9 items)

From V84 + V90:
- Selector promotion (any) — OWNER_LOCKED
- Official prompt change — OWNER_LOCKED
- Production model swap — OWNER_LOCKED
- Global NO_TOKEN floor change — OWNER_LOCKED
- MN_TEST_LANE_VOTER_PROPOSAL dossier (2026-05-21)
- MB regime forensic (auto-trigger 2026-05-14 if cold ≥ 7d)
- Provider invoice update _provider_pricing_table.py
- GPT-5-mini API key validation
- UI Master Board build extension (proposal only)

## 5. Route map

5 main routes user/agent will visit:
- `/du-doan` — production (DO_NOT_TOUCH)
- `/monitoring` — single-source dashboard (29 tabs)
- `/v82-monitor` — V83 standalone (also embedded /monitoring)
- `/du-doan-test` — admin experimental lane
- `/api/admin/master-board` — Agent IDE single endpoint (schema v90_master_board_v4, 36 keys)

## 6. Model/Method/Action summary

See [`actionable_evidence_matrix.md`](actionable_evidence_matrix.md) + [`method_accuracy_action_map.md`](method_accuracy_action_map.md).

Highlights:
- **DOSSIER_PREP for 2026-05-21**: MN_SPECIALIST_ROSTER_V1 + MN_AI_CHAIN_PRESERVATION_V1
- **DROP_FROM_PROMOTION**: MT_AI_CHAIN_PRESERVATION_V1, MT_PRIOR_REGION_CONTEXT_SAFE_V1, rule_phase_evidence_v1, rule_injection_contract_shadow_v1, no_token_drift_guard_v1
- **CLOSED — continuous**: Wave 1, Wave 2, D-1, D-2, D-7, V82-V90 inventory chain
- **WAIT_60D (2026-07-06)**: MB_SPECIALIST_ROSTER_V1
- **WAIT_14D (2026-05-21)**: V79 cluster, V81 pilot

## 7. Region strategy

[`region_strategy_matrix.md`](region_strategy_matrix.md):
- **MN**: 2 promotion candidates clean lift 60d → DOSSIER_PREP 2026-05-21
- **MT**: PROTECT consensus-first; 4 method DESTRUCTIVE_PROVEN_60D → DROP
- **MB**: cold confirmed; SPECIALIST_ROSTER promising n=41 → WAIT_60D

## 8. Prompt / Rule / No-token

[`prompt_rule_no_token_status.md`](prompt_rule_no_token_status.md):
- Production prompt OFFICIAL_LOCKED.
- Shadow prompts (V78 region-specialist + V81 pilot) advanced context.
- 4 rule-shadow methods classified.
- No global NO_TOKEN floor change (region delta differ).

## 9. Hard locks (do-not-touch)

1. 4 official tables hash byte-identical (predictions / final_bundles / lottery_results / model_daily_eval).
2. NO selector promotion without dossier + owner OK.
3. NO global NO_TOKEN floor change.
4. NO official prompt change.
5. NO production model swap.
6. NO promote/rollback/edit/trigger button anywhere in UI.

## 10. Where to look for X (index)

| Looking for... | Go to |
|---|---|
| Latest report pointer | LATEST_REPORT.json |
| 29 tabs | /monitoring V87 Master Index |
| Full inventory | /api/admin/master-board (schema v90_v4) |
| 60d evidence | V82_60D_EVIDENCE_CONTROL_PASS_20260507/ |
| FU reconciliation | V91 FU_STALE_RECONCILIATION_MATRIX.md |
| Decision calendar | V91 decision_calendar_hardened.md |
| Region strategy | V91 region_strategy_matrix.md |
| Method accuracy | V91 method_accuracy_action_map.md |
| Owner gate queue | V84 open_owner_gate_queue.md |
| 1019/1378 items | V88 TOTAL_ENCYCLOPEDIA.md + V90 evidence |
| Notion docs (15) | V87 Master Index → 📓 Notion Docs tab |
| Backend modules (293) | V90 Backend Modules tab |
| All API endpoints (132) | V86 TOTAL_PUBLIC_REGISTRY.md + V87 API tab |

## 11. Cross-link

- V82 60d audit: V82_60D_EVIDENCE_CONTROL_PASS_20260507/
- V83 UI panel: V83_V82_MONITOR_UI_PANEL_20260507/
- V84 master board: V84_MASTER_CONTROL_BOARD_20260507/
- V85 deep: V85_DEEP_MASTER_CONTROL_20260507/
- V86 forensic: V86_TOTAL_FORENSIC_REGISTRY_20260508/
- V87 UI 12 tabs: V87_MASTER_INDEX_20260508/
- V88 encyclopedia: V88_TOTAL_ENCYCLOPEDIA_20260508/
- V89 5-extension: V89_5_EXTENSION_PACK_20260508/
- V90 final cleanup: V90_FINAL_CLEANUP_20260508/
- **V91 reconciliation**: V91_TOTAL_RECONCILIATION_20260508/

## 12. V91 deliverables (this report)

- FU_STALE_RECONCILIATION_MATRIX.md
- monitoring_24_tabs_audit.md
- actionable_evidence_matrix.md
- method_accuracy_action_map.md
- region_strategy_matrix.md
- prompt_rule_no_token_status.md
- routes_ui_coverage.md
- decision_calendar_hardened.md
- per_decision_tracking.md
- stale_fu_auto_update_spec.md
- V91_ONE_SOURCE_INDEX.md (this file)
