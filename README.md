# Lottery AI Notion Reports

- Latest package: **V10642** — `V10642_PER_SLICE_HEALTH_AND_POLICY` (Per-slice architecture: P1 realtime health labels per region×weekday LIVE shadow [STRONG/WATCH/WEAK, weak slices keep running WITH warning], P2 slice_policy config with data-driven per-slice AI-model cut lists [enabled=0, reversible], P4 UI labels LIVE on du-doan + du-doan-test + monitoring via read-only /api/slice-health. P3 token-call-saving = careful next (owner deferred). Backup taken. Official numbers unchanged.)
- Owner report: `V10642_PER_SLICE_HEALTH_AND_POLICY/V10642_OWNER_REPORT_VN_PUBLIC.md`
- Chain: … -> V10640 -> V10641 -> **V10642**
- Public push status: **PUSHED (owner requested for AI analysis)**

## Policies
- Public reports do NOT contain private code, DB rows, provider API keys, or raw VPS internals.
- No claim of ACCURACY_READY / OFFICIAL_IMPROVED / SELECTOR_FIXED / MN_FIXED / MT_FIXED / MB_FIXED / LANE_TEST_PROMOTED. (V10640 deployed a reversible MN override but makes NO improvement claim — backtest only, forward unproven.)
- Read-only forensic + backtest UNTIL V106.38-R8G. From **V10640**: first controlled, reversible, owner-approved production change (MN BT override); fully revertible by one flag; wallet untouched.

## V106.38-R8 highlights (91-day audit)
- "win ~44%" metric = lo-toan-mien, near-random for MN/MB.
- Only statistically significant edge: MB frequency (hot numbers), +~0.4 hits/day, p~0.004 (borderline, needs forward proof).
- AI token models: no significant edge anywhere.
- Single models are weekday/station specialists; current weighting is region-global (root of "chaos").
- Standardization: 163 tables, station-name + column-name inconsistencies, 6 duplicate table pairs, 9 dead tables, ~100 backend scripts.
- 3 flows (official/lane-test/shadow) separated by name but per-slice axis mostly missing.
- Proposal: canonical Data Dictionary -> views -> name-only normalization -> per-slice weighting + shrinkage.
