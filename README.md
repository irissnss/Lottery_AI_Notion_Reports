# Lottery AI Notion Reports

- Latest package: **V10643** — `V10643_SHADOW_PROMPT_FORENSIC_AND_REDESIGN` (Forensic: "Prompt shadow-first" = V81 provider pilot showing MN shadow +23pp over official — but PROVEN to be LOOKAHEAD illusion [runs 19:14 after all draws, context leaks actual_known/official_status/winner-tail, 3 models converge]. Not usable as live edge; burns ~20K tokens/day. Redesign roadmap: no-lookahead by construction; owner decision RETIRE vs re-architect EX-ANTE.) Prev: `V10642_PER_SLICE_HEALTH_AND_POLICY` (Per-slice architecture. P1+P2+P4 + V10642B: realtime health labels now per region×weekday×STATION(đài) LIVE shadow [reveals đài truth hidden by region label, e.g. MN CN ALL=STRONG but Kiên Giang=WEAK 0% / Đà Lạt=STRONG 50%]; model_progress tracker [per-model rec30 vs prev30 trend, RECOVERING detection — some reduced models already recovering] answering "measure if reduced models improve"; slice_policy mode=REDUCE [giảm≠tắt, keep measuring]; UI per-đài badges + model panel via /api/slice-health + /api/model-progress. P3 token-saving = careful next [reduce-cadence not hard-skip]. Backup taken. Official numbers unchanged.)
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
