# Lottery AI Notion Reports

- Latest package: **V106.38-R8G** — `V106_38R8G_VPS_VIEWS_DEPLOYED_PUBLIC_SAFE` (DEPLOYED 5 canonical VIEWs to VPS, official unchanged, smoke 200; local<->VPS divergence + PAT-exposure findings)
- Owner report: `V106_38R8G_VPS_VIEWS_DEPLOYED_PUBLIC_SAFE/V10638R8G_OWNER_REPORT_VN_PUBLIC.md`
- Chain: R8 -> R8B -> R8C -> R8D -> R8E -> R8F -> R8G
- Public push status: **PUSHED (owner requested for AI analysis)**

## Policies
- Public reports do NOT contain private code, DB rows, provider API keys, or raw VPS internals.
- No claim of ACCURACY_READY / OFFICIAL_IMPROVED / SELECTOR_FIXED / MN_FIXED / MT_FIXED / MB_FIXED / LANE_TEST_PROMOTED.
- Read-only forensic + backtest. 0 production change.

## V106.38-R8 highlights (91-day audit)
- "win ~44%" metric = lo-toan-mien, near-random for MN/MB.
- Only statistically significant edge: MB frequency (hot numbers), +~0.4 hits/day, p~0.004 (borderline, needs forward proof).
- AI token models: no significant edge anywhere.
- Single models are weekday/station specialists; current weighting is region-global (root of "chaos").
- Standardization: 163 tables, station-name + column-name inconsistencies, 6 duplicate table pairs, 9 dead tables, ~100 backend scripts.
- 3 flows (official/lane-test/shadow) separated by name but per-slice axis mostly missing.
- Proposal: canonical Data Dictionary -> views -> name-only normalization -> per-slice weighting + shrinkage.
