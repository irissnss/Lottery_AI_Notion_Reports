# MASTER SSOT RECONCILIATION MATRIX — V105.27 (2026-05-11)

> Read-only audit. No official mutation. No provider call.

## 1. Latest claim per source

| Source | Latest version claimed | Evidence path | Is stale? | Missing reports | Action |
|---|---|---|---|---|---|
| Local `CHANGELOG.md` | V20.3.37.105.25b (2026-05-11T17:35:00+07:00) | `CHANGELOG.md:1` | Yes — missing V105.21 / V105.23 / V105.24 / V105.26 entries | V105.21, V105.23, V105.24, V105.26 | `CHANGELOG_STALE` — backfill or mark as Drive/Notion-only |
| Local `docs/CURRENT_TRUTH_SSOT.md` | V105.25b → V105.22 chain | `docs/CURRENT_TRUTH_SSOT.md:1-9` | Same gap as CHANGELOG | V105.21, V105.23, V105.24, V105.26 | `SSOT_SYNC_REQUIRED` |
| Local `docs/FOLLOW_UP_TRACKER.md` | FU-V105-25B current; FU-V105-25 superseded | `docs/FOLLOW_UP_TRACKER.md:31-58` | Stale for V105.21/23/24/26 | FU items for V105.21, V105.23, V105.24, V105.26 | Cross-link to V105.27 + add FU-V105-27-TOTAL-FORCE-CONTROL |
| Local `docs/AUTOMATION_STATE.json` | `governance_seq=65`, last detail at seq 62 (V105.11) | `docs/AUTOMATION_STATE.json:1-21` | Yes — 14 versions behind | V105.12..V105.27 | `LATEST_REPORT_STALE` — append V105.25b + V105.27 events |
| Local root `OPEN_ISSUES.md` | NOT PRESENT | `glob: OPEN_ISSUES.md=0 files (root)` | N/A | All | `OPEN_ISSUES_MISSING` — owner decide rebuild from FU tracker |
| Local root `NEXT_ACTION.md` | NOT PRESENT | `glob` returns 0 | N/A | All | `NEXT_ACTION_MISSING` |
| Local root `LATEST_REPORT.json` | NOT PRESENT | `glob` returns 0 | N/A | All | `LATEST_REPORT_MISSING` |
| Local root `REPORT_INDEX.md` | NOT PRESENT | `glob` returns 0 | N/A | All | `REPORT_INDEX_MISSING` |
| Local root `CHANGELOG_PUBLIC.md` | NOT PRESENT | `glob` returns 0 | N/A | All | `PUBLIC_CHANGELOG_MISSING` |
| Local root `DELTA_INDEX.md` | NOT PRESENT | `glob` returns 0 | N/A | All | `DELTA_INDEX_MISSING` |
| Local root `00_PUBLIC_RAW_LINKS.md` | NOT PRESENT | `glob` returns 0 | N/A | All | `PUBLIC_RAW_LINKS_MISSING` |
| Local `Lottery_AI_Notion_Reports/*` | NOT PRESENT in workspace | `glob` returns 0 | N/A | All | This repo is private side only; public mirror lives elsewhere (Drive / GitHub public mirror) — `PUBLIC_STALE` until owner re-pulls |
| Live VPS DB (live-sync 20260511_180555) | `predictions=4791`, `final_bundles=219`, `lottery_results=14654`, `model_daily_eval=4572` | `artifacts/v10527/preflight.json` | Runtime ahead of docs (V105.25b stdio fix is local-only, not yet deployed) | none | `RUNTIME_AHEAD` |
| Notion MCP | Owner mission expects V105.19..V105.26 pages exist | Not re-checked in this session (no MCP read in window) | Unknown | None confirmed | `NOTION_RECHECK_REQUIRED` |

## 2. Classification

- `PUBLIC_STALE` — all public-facing SSOT files (`LATEST_REPORT.json`, `REPORT_INDEX.md`, `CHANGELOG_PUBLIC.md`, `DELTA_INDEX.md`, `00_PUBLIC_RAW_LINKS.md`, `OPEN_ISSUES.md`, `NEXT_ACTION.md`) are missing from local workspace.
- `CHANGELOG_STALE` — local `CHANGELOG.md` jumps V105.20 → V105.22 → V105.25b; missing V105.21, V105.23, V105.24, V105.26 rows.
- `SSOT_SYNC_REQUIRED` — same gap in `docs/CURRENT_TRUTH_SSOT.md`.
- `LATEST_REPORT_STALE` — `docs/AUTOMATION_STATE.json` last full event is V105.11 era (seq 62). V105.12..V105.26 events are not captured.
- `RUNTIME_AHEAD` — DB on VPS (and now live-synced locally) contains V105.22+ shadow tables (`bundle_universe_coverage_daily=3076`, `rule_injection_contract=3076`, `source_prize_strong_coverage=3076`, `lane_test_lose_only_audit_daily=90`) that are documented but not surfaced in latest CHANGELOG entries.
- `NOTION_STALE` — pending MCP re-check this session; flag `NOTION_RECHECK_REQUIRED` for the next agent pass with MCP browser.

## 3. Versions confirmed in code

| Version | Code evidence | Status |
|---|---|---|
| V105.5 | `_v101_shadow_pilot.py` (region source-pool shadow); CURRENT_TRUTH_SSOT row | Live |
| V105.10..V105.18 | `_materialize_adaptive_exploit_v1.py`, lane-test gates, lo1/lo2 audit, du-doan-test API | Live |
| V105.19 | `station_identity.py`, hard-stabilization control endpoints | Live |
| V105.20 | dual-lane probe artifacts | Live |
| V105.22 | `_v10522_live_prep.py`, `lane_test_region_profiles=3`, `mb_ai_chain_preservation_v1=30`, `station_identity_runtime_audit=69` | Live |
| V105.22b | `database.save_prediction` duplicate token guard; `_run_ai_predict_job` once-daily | Live |
| V105.24 source-pool gap drilldown | `_v10524_source_pool_gap_drilldown.py` (code present) | **Table `v10524_source_pool_gap_drilldown` NOT in DB** — never materialized locally |
| V105.24 V102 relaxed selector shadow | `_v10524_v102_relaxed_selector_shadow.py` (code present); `v10522_v102_strong_selector_shadow=0` (empty); no `v10524_*` selector table | **Empty** — `V103_SUPPLY_BOTTLENECK` likely |
| V105.25 candidate flow funnel | `_v10525_candidate_flow_funnel.py` (code present) | **Table `v10524_candidate_flow_trace` NOT in DB** — never materialized locally |
| V105.25 V103 supply class backfill | `_v10525_v103_supply_class_backfill.py` (code present) | Backfill may be VPS-only |
| V105.25b cascade contract + stdio harden | `web/backend/scheduler.py:_safe_stdio_ctx`, `web/backend/main.py:/api/admin/cascade-contract-audit`, CHANGELOG, SSOT, FU updated | LOCAL FIX, OWNER_GATE_REQUIRED for VPS deploy |
| V105.26 final report | No reference found in local CHANGELOG/SSOT/FU | `MISSING_ON_LOCAL` — referenced by owner only |

## 4. SSOT conflicts requiring owner

- Owner mission requires canonical Huế = `Huế`, but `web/backend/station_identity.py:24-27` canonicalizes to `Thừa Thiên Huế` (per V105.9 deploy + V105.19 lock). **OWNER_GATE_REQUIRED** — flipping breaks current monitoring/rule/pnl groupings that read `Thừa Thiên Huế`.
- Owner mission claims V105.24 source-pool gap tables exist (with `miss_reason`, `station_canonical`, etc.) but local DB has the materializer code only, no rows. Either VPS has the table but live-sync did not pull (DB only pulls full file, so this means VPS does not have these tables either) OR the table name is different (e.g. `candidate_drop_stage_daily=103` may be the actual SSOT table). Recommend treat `candidate_drop_stage_daily` + `bundle_universe_coverage_daily` + `source_prize_strong_coverage` + `rule_injection_contract` as canonical proxies until owner confirms.

## 5. Recommended next actions (no official touch)

1. Owner gates a single backfill commit appending V105.21/23/24/26 + V105.27 rows to `CHANGELOG.md`, `docs/CURRENT_TRUTH_SSOT.md`, `docs/FOLLOW_UP_TRACKER.md`, `docs/AUTOMATION_STATE.json` from Drive/Notion sources.
2. Recreate root files (`LATEST_REPORT.json`, `REPORT_INDEX.md`, `OPEN_ISSUES.md`, `NEXT_ACTION.md`, `CHANGELOG_PUBLIC.md`, `DELTA_INDEX.md`, `00_PUBLIC_RAW_LINKS.md`) from latest agreed truth.
3. Pull `Lottery_AI_Notion_Reports/` mirror so public SSOT can be verified inside this workspace.
4. Materialize V105.24 source-pool gap tables locally (or document the rename to `candidate_drop_stage_daily`).
