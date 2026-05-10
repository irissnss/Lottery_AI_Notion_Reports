# V105.6 — SSOT Clean + Live Cron Verify + Regional Source-Pool Data Health

DB Source: VPS_SYNCED
Sync Timestamp: 2026-05-10T12:15:33+07:00
Freshness Check: PASS
Sync Manifest: `artifacts/live_sync/20260510_121518/manifest.json`
Hard Lock: NO `/du-doan`, NO `/api/final-bundle`, NO `generate_final_bundle()`, NO official table mutation, NO production scoring/prompt/selector change.


## Summary

V105.6 fixes the public SSOT stale gap and adds runtime data-health surfaces around the V105.5 regional source-pool lane. It keeps all changes shadow-only/admin-only and verifies no official table mutation.

## Preflight

| Source | Status | Latest version | Issue |
|---|---|---:|---|
| Notion | read/done | V105.6 | V105.5 page exists; 3 V105.6 pages created under canonical `Lottery_AI_Test` |
| GitHub public LATEST | read/verified | V105.6 | Raw public now points to V105.6 after public commit |
| GitHub public evidence V105.5 | 200 after push | V105.5 | `V105_5_REGIONAL_SOURCE_POOL_LANE_TEST_REPORT.md` raw URL verified 200 after push |
| Private repo docs | read | V105.5 plus P&L V105.6/V105.7 | Label collision: P&L hotfix used V105.6/V105.7; this total-force wrapper recorded as V20.3.37.105.8 privately |
| VPS runtime | checked | V105.6 deployed | health public 200 via WebFetch; localhost admin endpoints 401; source-pool/status tables populated shadow-only |

## Runtime Evidence

- `v101_region_source_pool_shadow=10170`, flag violations 0.
- `v101_region_source_pool_top5_shadow=1695`, flag violations 0.
- `v101_region_source_pool_evidence_shadow=263`, flag violations 0.
- `v105_no_token_independent_scoreboard=7422`, flag violations 0.
- 2026-05-10 top5 rows: MN=5, MT=5, MB=5.
- Status before MN draw: `WAITING_MN` overall; MN formula is source-ready from D-1/D-2, MT/MB wait for same-day MN/MT as designed.

## Official Untouched Proof

Pre/post VPS hash guard stayed identical:

- `predictions`: `032a268e6b255f3e06c5abb3a525a508581c25dd361b21852cc8a5a317251602`
- `final_bundles`: `702fc30bc1dd6e9199cfd57b40025151355d4cd5fa508d0f498bb03f341ff15e`
- `lottery_results`: `6972fddfeb574e4b436993a7f73989162d7e95ef3986f283b3151d193380fb32`
- `model_daily_eval`: `a865b9e3ea3523b85412be455469ef37417fb84ad27305b437408ddc7f1e46cc`

## Public Fix

This report, V105.5 evidence, and V105.5 conversation context are now the public read path. Raw URL verification passed after push.

## Notion MCP Sync

- `V105.6 — SSOT Clean + Source-Pool Live Verify`: `35c1d385-9bf8-81cb-ac79-c7f9b8d693d9`
- `V105.6 — Monitoring Data Health + Prediction Quality Audit`: `35c1d385-9bf8-819e-b5ca-db7f9b57d6d4`
- `V105.6 — Owner Conversation Context`: `35c1d385-9bf8-8136-b6f6-ef7663b1a35d`
