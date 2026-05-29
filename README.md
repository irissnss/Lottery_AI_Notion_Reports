# Lottery AI Notion Reports

- Latest package: **V106.38-R8D** — `V106_38R8D_PHASE1_CANONICAL_VIEWS_PUBLIC_SAFE` (Phase 1: 5 canonical VIEWs tested PASS, Data Dictionary v1.0 SSOT, Phase B drop/merge SQL prepared)
- Owner report: `V106_38R8D_PHASE1_CANONICAL_VIEWS_PUBLIC_SAFE/V10638R8D_PHASE1_OWNER_REPORT_VN_PUBLIC.md`
- Chain: R8 (truth) -> R8B (dependency) -> R8C (verify) -> R8D (Phase 1)
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
