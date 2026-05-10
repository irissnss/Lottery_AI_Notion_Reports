# V105.5 — Regional Source-Pool Lane Test Measurement

Time: 2026-05-10 11:50 VN

## Owner Formulas

- `MN_D = (MN + MT + MB) D-1 + (MN + MT + MB) D-2`
- `MT_D = (MN + MT + MB) D-1 + MN D`
- `MB_D = (MN + MT + MB) D-1 + MN D + MT D`

## What Changed

- Added `v101_region_source_pool_shadow` for MN/MT/MB regional source pools.
- Added `v101_region_source_pool_top5_shadow` for current top 5 per region with 12-week and 16-week same-weekday measurement.
- Kept the legacy MN table for compatibility.
- Wired V103/V104 shadow candidate supply to region-specific V101 context.
- Added scheduler cron at 19:23 VN before V104 materializer and Phase B.
- Extended `/monitoring` V105 panel with V101 top5 and source completeness.

## VPS Evidence

- Backfill window: `2026-01-18` to `2026-05-10` (113 days).
- `v101_mn_cross_region_rule_shadow`: 3390 rows.
- `v101_region_source_pool_shadow`: 10170 rows.
- `v101_region_source_pool_top5_shadow`: 1695 rows.
- `v101_region_prompt_context_shadow`: 339 rows.
- New V101 flag violations: 0.

Current `2026-05-10` pre-draw status is `SOURCE_PARTIAL` / `WAITING_MN`: there are no same-day `lottery_results` rows yet, so MT waits for `MN D` and MB waits for `MN D + MT D`. The 19:23 VN cron refreshes the lane after same-day source data exists.

## Safety

Official tables unchanged after deploy/backfill:

- `predictions`: 4667 rows, sha256 `032a268e6b255f3e06c5abb3a525a508581c25dd361b21852cc8a5a317251602`
- `final_bundles`: 214 rows, sha256 `702fc30bc1dd6e9199cfd57b40025151355d4cd5fa508d0f498bb03f341ff15e`
- `lottery_results`: 14642 rows, sha256 `6972fddfeb574e4b436993a7f73989162d7e95ef3986f283b3151d193380fb32`
- `model_daily_eval`: 4493 rows, sha256 `a865b9e3ea3523b85412be455469ef37417fb84ad27305b437408ddc7f1e46cc`

Live sync manifest: `artifacts/live_sync/20260510_121518/manifest.json`.

No `/du-doan`, final bundle, production prompt, production scoring, selector, bundle voting, combo-super, or official table mutation. New outputs remain shadow-only, diagnostic-only, not output eligible, and not owner-approved for production.
