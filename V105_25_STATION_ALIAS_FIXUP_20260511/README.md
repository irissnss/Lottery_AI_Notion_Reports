# V105.25 — STATION ALIAS FIXUP + SOURCE-POOL REASON RANKING + V103 SUPPLY CLASS FIX

Published: 2026-05-11 VN.
Status: **OFFICIAL LOCKED** — `predictions / final_bundles / lottery_results / model_daily_eval` proven unchanged; LANE 1–6 completed under shadow-only contracts; Notion sync pending owner OK.

## What this folder contains

| File | Purpose |
|---|---|
| `evidence/V105_25_FINAL_REPORT.md` | Vietnamese final report (11 sections). |
| `evidence/V105_25_SOURCE_POOL_GAP_ANALYSIS_VI.md` | LANE 2 deliverable — reason-ranking + funnel analysis. |
| `evidence/v10525_local_audit_latest.json` | End-to-end V105.25 audit run with official-table hash guard. |
| `evidence/v10525_source_pool_reason_ranking.json` | Aggregated reason ranking by region × weekday × station × miss_reason × source_prize. |
| `evidence/v10525_candidate_flow_funnel.json` | Conversion through source_pool → prompt → ranked → top5 → top2 → bundle → UI. |
| `evidence/v10525_v102_relaxed_watch.json` | 7d/14d would_save / would_break tracker for V102 RELAXED L1/L2 (shadow-only). |
| `evidence/v10524_station_code_audit_post_v10525.json` | Code-axis audit after LANE 1 fixup (`alias_unexpected_count = 0`). |
| `evidence/drift_alert.json` | LANE 6 daily runtime manifest drift alert (first run; alert = false). |

## Hard contracts

- No mutation of `predictions / final_bundles / lottery_results / model_daily_eval`.
- No mutation of raw `lottery_results.station` values (DB still legitimately stores `Huế`, `HCM`, `Đắc Lắc`, `Đắc Nông`; canonicalization is read-time only).
- No provider/manual AI calls were issued.
- V102 RELAXED rows are `output_eligible=0`, `shadow_only=1`, `owner_approved=0`; no promotion to production.

## Acceptance gates (LANE 1 target)

- `alias_unexpected_count = 0` ✅
- `weekday_as_station_unexpected_strict = 0` ✅
- All 4 official tables: pre/post row_count + sha256 identical ✅

## Read order

1. `evidence/V105_25_FINAL_REPORT.md`
2. `evidence/v10525_local_audit_latest.json` (`official_unchanged: true`)
3. `evidence/V105_25_SOURCE_POOL_GAP_ANALYSIS_VI.md`
4. `evidence/v10525_source_pool_reason_ranking.json`
5. `evidence/v10525_candidate_flow_funnel.json`
6. `evidence/v10525_v102_relaxed_watch.json`
7. `evidence/v10524_station_code_audit_post_v10525.json`

V105.24 evidence pack: `../V105_24_SOURCE_POOL_GAP_DRILLDOWN_20260511/`.
