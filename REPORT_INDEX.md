# REPORT INDEX (auto-discovery)

Latest: **V10673** - `V10667_RULES_PER_REGION_DETAILED_PUBLIC_SAFE/V10673_SESSION_RULE_DIGGING_JOURNEY_VN.md` (SESSION JOURNEY: gom 38 đợt đào rules 21/05→02/06 / 10 packages vào 1 index, mỗi đợt có verdict validated/pre-register/weak/rejected + link. Chỉ V10636-CROSS cho rule đáng tin = 28 forward-audit; còn lại yếu/bác bỏ/pre-register. Plus V10672 system-wide verify + all prior).

## Quick links - V10673 (SESSION JOURNEY + SYSTEM-WIDE-VERIFIED)

1. [LATEST_REPORT.json](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/LATEST_REPORT.json)
2. 🗺️ **[SESSION RULE-DIGGING JOURNEY](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/V10667_RULES_PER_REGION_DETAILED_PUBLIC_SAFE/V10673_SESSION_RULE_DIGGING_JOURNEY_VN.md)** — NEW: all 38 digging episodes + verdicts in one index
3. ✅ **[MASTER VERIFICATION REPORT](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/V10667_RULES_PER_REGION_DETAILED_PUBLIC_SAFE/V10672_MASTER_VERIFICATION_REPORT_VN.md)** — production LIVE + all reports temporal-clean (286k rules verified)
3. 🎯 **[SOURCE SEMANTICS LEGEND](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/V10667_RULES_PER_REGION_DETAILED_PUBLIC_SAFE/V10670_SOURCE_SEMANTICS_LEGEND.md)** — #Bộ vs đài, multi-station union, station-by-weekday map
3. ✅ **[TEMPORAL VERIFICATION REPORT](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/V10667_RULES_PER_REGION_DETAILED_PUBLIC_SAFE/V10669_TEMPORAL_VERIFICATION_REPORT_VN.md)** — OVERALL CLEAN=True
4. 🕐 **[TEMPORAL CAUSALITY PATCH NOTICE](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/V10667_RULES_PER_REGION_DETAILED_PUBLIC_SAFE/V10668_TEMPORAL_CAUSALITY_PATCH_NOTICE.md)** — draw order MN→MT→MB
3. ⭐ **[BỘ NUMBERING LEGEND](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/V10667_RULES_PER_REGION_DETAILED_PUBLIC_SAFE/V10667_BO_NUMBERING_LEGEND.md)** — `Giải X bộ Y` notation
4. **[Index Hub](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/V10667_RULES_PER_REGION_DETAILED_PUBLIC_SAFE/V10667_RULES_INDEX.md)**
5. **[MB Target Rules](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/V10667_RULES_PER_REGION_DETAILED_PUBLIC_SAFE/V10667_RULES_MB_TARGET.md)** — Miền Bắc (xổ cuối, no temporal limit)
6. **[MN Target Rules](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/V10667_RULES_PER_REGION_DETAILED_PUBLIC_SAFE/V10667_RULES_MN_TARGET.md)** — Miền Nam (xổ đầu, chỉ lag≥1)
7. **[MT Target Rules](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/V10667_RULES_PER_REGION_DETAILED_PUBLIC_SAFE/V10667_RULES_MT_TARGET.md)** — Miền Trung (MN(D) OK, MB(D) loại)
8. [Forward Audit Registry FIXED (28 valid rules)](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/V10667_RULES_PER_REGION_DETAILED_PUBLIC_SAFE/machine_readable/V10668_FORWARD_AUDIT_REGISTRY_FIXED.json)
9. [Temporal Violation Audit (full map)](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/V10667_RULES_PER_REGION_DETAILED_PUBLIC_SAFE/machine_readable/V10668_TEMPORAL_VIOLATION_AUDIT.json)

---

# REPORT INDEX (legacy auto-discovery)

Latest: **V106.38-R8G** - `V106_38R8G_VPS_VIEWS_DEPLOYED_PUBLIC_SAFE/V10638R8G_OWNER_REPORT_VN_PUBLIC.md` (DEPLOYED 5 canonical VIEWs to VPS production: backup taken, official table counts unchanged before==after, 13 views total, smoke /api/health 200 V20.3.36 — standardization now LIVE, reversible. Findings: local<->VPS divergent (VPS master/164 tables vs local main/163, VPS uncommitted) -> no blind code deploy; GitHub PAT exposed in VPS git remote -> rotate. NOT deployed (owner-gated, divergent code/behavior): Phase B drop/merge, MB freq lane runtime+cron, per-slice weighting, MB cap, token LIMIT. Official numbers unchanged; wallet untouched. Chain R8->R8G).

## Quick links - V106.38-R8G
1. [V10638R8G Owner Report VN](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/V106_38R8G_VPS_VIEWS_DEPLOYED_PUBLIC_SAFE/V10638R8G_OWNER_REPORT_VN_PUBLIC.md)
2. [V10638R8G Summary (JSON)](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/V106_38R8G_VPS_VIEWS_DEPLOYED_PUBLIC_SAFE/machine_readable/V10638R8G_SUMMARY.json)

---

# REPORT INDEX (auto-discovery)

Latest: **V106.38-R8F** - `V106_38R8F_UNIFIED_SHADOW_PREDICTOR_PUBLIC_SAFE/V10638R8F_OWNER_REPORT_VN_PUBLIC.md` (Ranking audit: current model weight is region-30d near-uniform NOISE (not per-slice) + includes stale models; A2 shadow fix = flexible-by-weekday active-only ranking. B1 unified per-slice shadow predictor backtest 70d BT lo-hit: MB freq_hot 34.3% vs official 18.6% (+15.7pp, token-FREE, strongest); MT ml-free +2.9pp; MN per-slice ranking -2.9pp (MN AI already good). Forward-log seeded 3 regions (only MB freq forward-able from IDE). Honest: n=70 low ceiling, NOT improved-claim, needs forward proof + lane/shadow live before deploy. Official 0 writes. 14 owner-gated remain; milestone 2026-06-03. Chain R8->R8F).

## Quick links - V106.38-R8F
1. [V10638R8F Owner Report VN](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/V106_38R8F_UNIFIED_SHADOW_PREDICTOR_PUBLIC_SAFE/V10638R8F_OWNER_REPORT_VN_PUBLIC.md)
2. [V10638R8F Summary (JSON)](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/V106_38R8F_UNIFIED_SHADOW_PREDICTOR_PUBLIC_SAFE/machine_readable/V10638R8F_SUMMARY.json)

---

# REPORT INDEX (auto-discovery)

Latest: **V106.38-R8E** - `V106_38R8E_NIGHT_RUN_AND_DOT1_PUBLIC_SAFE/V10638R8E_OWNER_REPORT_VN_PUBLIC.md` (Night run 6/6 PASS P0-P5 + Dot1 shadow lanes. KPI per-slice: MT.T5 official BT 76.9% p=0.013 sig; MN.T7 23% vs random 52% = SELECTION bug (gemini-2.5-pro hits 82% on T7 but bundle ignores it, not signal scarcity); MB freq_hot lane backtest +0.37 hits/day p=0.0089 token-FREE, next-draw dan seeded + forward-log; MT.T5 strength from FREE ML (combo-no-token/random-forest 84.6%); 12 MB token-AI no-lift LIMIT candidates. Master sequential roadmap (4 dot). Official 0 writes mode=ro. Production drop/merge/deploy/token = owner-gated. AI running to 2026-06-03. Chain R8->R8E).

## Quick links - V106.38-R8E
1. [V10638R8E Owner Report VN](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/V106_38R8E_NIGHT_RUN_AND_DOT1_PUBLIC_SAFE/V10638R8E_OWNER_REPORT_VN_PUBLIC.md)
2. [V10638R8E Summary (JSON)](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/V106_38R8E_NIGHT_RUN_AND_DOT1_PUBLIC_SAFE/machine_readable/V10638R8E_SUMMARY.json)

---

# REPORT INDEX (auto-discovery)

Latest: **V106.38-R8D** - `V106_38R8D_PHASE1_CANONICAL_VIEWS_PUBLIC_SAFE/V10638R8D_PHASE1_OWNER_REPORT_VN_PUBLIC.md` (Phase 1 executed safely after owner approval of gói A+B. 5 canonical VIEWs (v_predictions/v_model_daily_eval/v_mined_rules/v_final_bundles/v_lottery_results) generated + tested PASS via read-only ATTACH — 0 write to real DB, 0 numbers changed; code reads 1 canonical name without breaking 153 files. Data Dictionary v1.0 promoted to docs/ as SSOT (canonical cols, flow labels, per-slice key, station aliases, model=no-merge). Phase B drop/merge SQL prepared (drop rule_features + merge true-dup pair #4 after materializer consolidation) but NOT executed - awaiting backup + button + deploy gate. AI still running to 2026-06-03. Chain R8->R8B->R8C->R8D).

## Quick links - V106.38-R8D Phase 1
1. [V10638R8D Phase 1 Owner Report VN](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/V106_38R8D_PHASE1_CANONICAL_VIEWS_PUBLIC_SAFE/V10638R8D_PHASE1_OWNER_REPORT_VN_PUBLIC.md)
2. [Data Dictionary v1.0 (SSOT)](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/V106_38R8D_PHASE1_CANONICAL_VIEWS_PUBLIC_SAFE/DATA_DICTIONARY_v1.0.md)
3. [Phase 1 canonical views SQL](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/V106_38R8D_PHASE1_CANONICAL_VIEWS_PUBLIC_SAFE/phase1_canonical_views.sql)
4. [Phase B drop/merge SQL (prepared)](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/V106_38R8D_PHASE1_CANONICAL_VIEWS_PUBLIC_SAFE/phase_b_drop_merge.sql)
5. [V10638R8D Summary (JSON)](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/V106_38R8D_PHASE1_CANONICAL_VIEWS_PUBLIC_SAFE/machine_readable/V10638R8D_SUMMARY.json)

---

# REPORT INDEX (auto-discovery)

Latest: **V106.38-R8C** - `V106_38R8C_PHASE0_VERIFICATION_PUBLIC_SAFE/V10638R8C_PHASE0_VERIFICATION_OWNER_REPORT_VN_PUBLIC.md` (Phase 0 verification gate. Models clarified: 28 active / 13 removed-idle / 13 historical-orphans, NOT merged, registry is SSOT, keys shared by provider. Full station x weekday matrix verified: HCM_MN runs T2+T7 (Saturday) NOT Sunday; Ha Noi_MB T2+T5; Thua Thien Hue_MT T2+CN; Da Nang/Khanh Hoa multi-weekday. Merge verify of 6 schema-duplicate pairs: only 1 true duplicate, 2 region-subset, 1 version -> row-level check before any merge. rule_features SAFE to drop (0 rows/0 refs). Awaiting owner approval of canonical column names before Phase 1 views. Read-only; 0 production change; AI running. Parents: R8 truth + R8B dependency).

## Quick links - V106.38-R8C Phase 0 verification
1. [V10638R8C Verification Owner Report VN](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/V106_38R8C_PHASE0_VERIFICATION_PUBLIC_SAFE/V10638R8C_PHASE0_VERIFICATION_OWNER_REPORT_VN_PUBLIC.md)
2. [V10638R8C Summary (JSON)](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/V106_38R8C_PHASE0_VERIFICATION_PUBLIC_SAFE/machine_readable/V10638R8C_SUMMARY.json)

---

# REPORT INDEX (auto-discovery)

Latest: **V106.38-R8B** - `V106_38R8B_PHASE0_STANDARDIZATION_DEPENDENCY_PUBLIC_SAFE/V10638R8B_PHASE0_OWNER_REPORT_VN_PUBLIC.md` (Phase 0 of 6-phase standardization. Inventory 163 tables (100 with non-canonical columns, 126 lint findings); dependency scan of 351 source files: only rule_features safe to drop (8 empty tables still code-referenced -> keep), 4 of 6 duplicate pairs are true merge candidates (2 same-schema-different-semantics -> keep both), column rename too risky (target_region in 153 files) -> canonical VIEW layer. Data Dictionary proposed v0.1; awaiting owner approval. Read-only; 0 production change; AI still running. Parent: V106.38-R8 total-truth report).

## Quick links - V106.38-R8B Phase 0
1. [V10638R8B Phase 0 Owner Report VN](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/V106_38R8B_PHASE0_STANDARDIZATION_DEPENDENCY_PUBLIC_SAFE/V10638R8B_PHASE0_OWNER_REPORT_VN_PUBLIC.md)
2. [Data Dictionary proposed v0.1](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/V106_38R8B_PHASE0_STANDARDIZATION_DEPENDENCY_PUBLIC_SAFE/DATA_DICTIONARY_PROPOSED_v0.1.md)
3. [Table inventory map](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/V106_38R8B_PHASE0_STANDARDIZATION_DEPENDENCY_PUBLIC_SAFE/P0_TABLE_INVENTORY_MAP.md)
4. [Dependency-aware action plan](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/V106_38R8B_PHASE0_STANDARDIZATION_DEPENDENCY_PUBLIC_SAFE/P0_DEPENDENCY_AWARE_ACTION_PLAN.md)
5. [Phase 0 Summary (JSON)](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/V106_38R8B_PHASE0_STANDARDIZATION_DEPENDENCY_PUBLIC_SAFE/machine_readable/V10638R8B_PHASE0_SUMMARY.json)

---

# REPORT INDEX (auto-discovery)

Latest: **V106.38-R8** - `V106_38R8_TOTAL_TRUTH_STANDARDIZATION_FLOW_PUBLIC_SAFE/V10638R8_OWNER_REPORT_VN_PUBLIC.md` (Total-truth + standardization + flow-separation audit, 91-day. Only statistically significant edge = MB frequency hot-numbers +~0.4 hits/day p~0.004 borderline; AI token models show no significant edge; "win 44%" metric is near-random lo-toan-mien; single models are weekday/station specialists but weighting is region-global; schema chaos 163 tables + station/column-name inconsistencies + 6 duplicate table pairs + 9 dead tables + ~100 scripts; 3 flows separated by name but per-slice axis missing. Standardization master plan: canonical Data Dictionary -> views -> name-only normalization -> per-slice weighting + shrinkage. Read-only; 0 production change; AI still running).

## Quick links - V106.38-R8
1. [V10638R8 Owner Report VN](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/V106_38R8_TOTAL_TRUTH_STANDARDIZATION_FLOW_PUBLIC_SAFE/V10638R8_OWNER_REPORT_VN_PUBLIC.md)
2. [V10638R8 Execution Summary (JSON)](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/V106_38R8_TOTAL_TRUTH_STANDARDIZATION_FLOW_PUBLIC_SAFE/machine_readable/V10638R8_EXECUTION_SUMMARY.json)

---

# REPORT INDEX (auto-discovery)

Latest: **V106.36** - `V106_36_FULL_DEBT_CLOSEOUT_REGION_INDEPENDENT_LANE_PUBLIC_SAFE/V10636_OWNER_REPORT_VN_PUBLIC.md` (Full debt closeout pass + region-independent lane execution dry-run. Tri-region closeout 2026-05-27 with selector_gap / bundle_skew root-cause for MT/MB. Model/method 30d audit shows MB AI-token cost-waste (contribution 4.4% on 45 winning days), MT combo dominates contribution 64%, MN AI-token healthy. Cohere ZERO_VALUE_PROOF 30d all regions. Rule105 V2 tier gate: MN 26/35 TIER_A, MT 18/35 TIER_A, MB 4/35 TIER_A with weekday coverage gap. Lane dry-run today: MN 5 rules→lane=39 vs official=58 WIN (false_consensus), MT/MB 0 rules eligible Wed. Master debt ledger V1.0→V106.35: 3 P0 + 10 P1; CP-66.7 still overdue. Safety: official_mutation=0, drift_detected=False).

## Quick links - V106.36 Full Debt Closeout + Region-Independent Lane Execution

1. [LATEST_REPORT.json](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/LATEST_REPORT.json)
2. [V10636 Owner Report VN (NEWEST MAIN)](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/V106_36_FULL_DEBT_CLOSEOUT_REGION_INDEPENDENT_LANE_PUBLIC_SAFE/V10636_OWNER_REPORT_VN_PUBLIC.md)
3. [V10636 Tri-Region Closeout 2026-05-27](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/V106_36_FULL_DEBT_CLOSEOUT_REGION_INDEPENDENT_LANE_PUBLIC_SAFE/V10636_TRI_REGION_CLOSEOUT_PUBLIC.md)
4. [V10636 Model × Method Scorecard](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/V106_36_FULL_DEBT_CLOSEOUT_REGION_INDEPENDENT_LANE_PUBLIC_SAFE/V10636_MODEL_METHOD_SCORECARD_PUBLIC.md)
5. [V10636 AI-Token Branch Audit (region-specific verdict)](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/V106_36_FULL_DEBT_CLOSEOUT_REGION_INDEPENDENT_LANE_PUBLIC_SAFE/V10636_AI_TOKEN_BRANCH_AUDIT_PUBLIC.md)
6. [V10636 No-Token Baseline Audit](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/V106_36_FULL_DEBT_CLOSEOUT_REGION_INDEPENDENT_LANE_PUBLIC_SAFE/V10636_NO_TOKEN_BASELINE_AUDIT_PUBLIC.md)
7. [V10636 Cohere Value Audit](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/V106_36_FULL_DEBT_CLOSEOUT_REGION_INDEPENDENT_LANE_PUBLIC_SAFE/V10636_COHERE_VALUE_AUDIT_PUBLIC.md)
8. [V10636 Rule105 Independent Query V2](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/V106_36_FULL_DEBT_CLOSEOUT_REGION_INDEPENDENT_LANE_PUBLIC_SAFE/V10636_RULE105_INDEPENDENT_QUERY_PUBLIC.md)
9. [V10636 Rule105 Window Sensitivity](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/V106_36_FULL_DEBT_CLOSEOUT_REGION_INDEPENDENT_LANE_PUBLIC_SAFE/V10636_RULE105_WINDOW_SENSITIVITY_PUBLIC.md)
10. [V10636 Rule105 Dampener Plan](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/V106_36_FULL_DEBT_CLOSEOUT_REGION_INDEPENDENT_LANE_PUBLIC_SAFE/V10636_RULE105_DAMPENER_PLAN_PUBLIC.md)
11. [V10636 Top Rules Tier Gate](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/V106_36_FULL_DEBT_CLOSEOUT_REGION_INDEPENDENT_LANE_PUBLIC_SAFE/V10636_TOP_RULES_TIER_GATE_PUBLIC.md)
12. [V10636 MN Lane Execution (dry-run)](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/V106_36_FULL_DEBT_CLOSEOUT_REGION_INDEPENDENT_LANE_PUBLIC_SAFE/V10636_MN_LANE_EXECUTION_PUBLIC.md)
13. [V10636 MT Lane Execution (dry-run)](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/V106_36_FULL_DEBT_CLOSEOUT_REGION_INDEPENDENT_LANE_PUBLIC_SAFE/V10636_MT_LANE_EXECUTION_PUBLIC.md)
14. [V10636 MB Lane Execution (dry-run)](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/V106_36_FULL_DEBT_CLOSEOUT_REGION_INDEPENDENT_LANE_PUBLIC_SAFE/V10636_MB_LANE_EXECUTION_PUBLIC.md)
15. [V10636 Master Debt Ledger V1.0→V106.35](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/V106_36_FULL_DEBT_CLOSEOUT_REGION_INDEPENDENT_LANE_PUBLIC_SAFE/V10636_MASTER_DEBT_LEDGER_PUBLIC.md)
16. [V10636 P0/P1 Action Board](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/V106_36_FULL_DEBT_CLOSEOUT_REGION_INDEPENDENT_LANE_PUBLIC_SAFE/V10636_P0_P1_ACTION_BOARD_PUBLIC.md)
17. [V10636 Owner Decision Table](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/V106_36_FULL_DEBT_CLOSEOUT_REGION_INDEPENDENT_LANE_PUBLIC_SAFE/V10636_OWNER_DECISION_TABLE_PUBLIC.md)
18. [V10636 Safety Gate](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/V106_36_FULL_DEBT_CLOSEOUT_REGION_INDEPENDENT_LANE_PUBLIC_SAFE/V10636_SAFETY_GATE_PUBLIC.md)
19. [V10636 Zero Official Drift Proof](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/V106_36_FULL_DEBT_CLOSEOUT_REGION_INDEPENDENT_LANE_PUBLIC_SAFE/V10636_ZERO_OFFICIAL_DRIFT_PROOF_PUBLIC.md)
20. [V10636 Execution Summary](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/V106_36_FULL_DEBT_CLOSEOUT_REGION_INDEPENDENT_LANE_PUBLIC_SAFE/machine_readable/V10636_EXECUTION_SUMMARY.json)

Latest: **V106.35** - `V106_35_MB_DB_D2_DEEP_DIVE_PUBLIC_SAFE/V10635_MB_DB_D2_DEEP_DIVE_REPORT_VN_PUBLIC.md` (Deep-dive audit of owner hypothesis "MB target D = MB GĐB at D-2 often repeats". Tested 2,338 MB days × 28 transforms × 6 windows × 7 weekdays. **HYPOTHESIS NOT VALIDATED**: H1 loose 22-25% (baseline ~24%, lift −3.78 to +1.65pp), H2 strict 0-1.12% (baseline 1%, lift −1 to +1pp). Recent 60-90d shows NEGATIVE lift. Recommends do NOT add to any pipeline tier. Owner observation likely selection bias.).

## Quick links - V106.35 MB DB D-2 Deep-Dive

1. [LATEST_REPORT.json](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/LATEST_REPORT.json)
2. [V10635 MB DB D-2 Deep-Dive Report VN (NEWEST MAIN)](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/V106_35_MB_DB_D2_DEEP_DIVE_PUBLIC_SAFE/V10635_MB_DB_D2_DEEP_DIVE_REPORT_VN_PUBLIC.md)
3. [V10635 Hypothesis Results Grid (168 rows: 28 transforms × 6 windows)](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/V106_35_MB_DB_D2_DEEP_DIVE_PUBLIC_SAFE/machine_readable/V10635_HYPOTHESIS_RESULTS.json)
4. [V10635 Top Transforms (28 ranked by composite score)](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/V106_35_MB_DB_D2_DEEP_DIVE_PUBLIC_SAFE/machine_readable/V10635_TOP_TRANSFORMS.json)
5. [V10635 Weekday Breakdown (LAST2 transform, 365d, 7 weekdays)](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/V106_35_MB_DB_D2_DEEP_DIVE_PUBLIC_SAFE/machine_readable/V10635_WEEKDAY_BREAKDOWN.json)
6. [V10635 Recent 180d Timeline (hit/miss + streak/gap)](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/V106_35_MB_DB_D2_DEEP_DIVE_PUBLIC_SAFE/machine_readable/V10635_RECENT_TIMELINE.json)
7. [V10635 Execution Summary](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/V106_35_MB_DB_D2_DEEP_DIVE_PUBLIC_SAFE/machine_readable/V10635_EXECUTION_SUMMARY.json)


Latest: **V106.34** - `V106_34_RULE_PIPELINE_MECHANISM_AUDIT_PUBLIC_SAFE/V10634_RULE_PIPELINE_MECHANISM_REPORT_VN_PUBLIC.md` (Read-only investigation of the production rule pipeline behind xs.io.vn/app UI. Answers three owner questions: rules are statistical lift mining (NOT ML); axis is region+weekday with 21 buckets; weekly mining + daily eval + real-time UI render. Confirms owner correction: MN/MT/MB independent across 8 dimensions vs 7 items fixed. Live DB audit covers 105 active rules. Includes source-file line references for every claim.).

## Quick links - V106.34 Rule Pipeline Mechanism

1. [LATEST_REPORT.json](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/LATEST_REPORT.json)
2. [V10634 Rule Pipeline Mechanism Report VN (NEWEST MAIN)](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/V106_34_RULE_PIPELINE_MECHANISM_AUDIT_PUBLIC_SAFE/V10634_RULE_PIPELINE_MECHANISM_REPORT_VN_PUBLIC.md)
3. [V10634 Per-Region Independence Matrix (7 fixed + 8 independent)](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/V106_34_RULE_PIPELINE_MECHANISM_AUDIT_PUBLIC_SAFE/machine_readable/V10634_PER_REGION_INDEPENDENCE_MATRIX.json)
4. [V10634 Bucket Quality Table Audit (21 entries + per-region suppression)](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/V106_34_RULE_PIPELINE_MECHANISM_AUDIT_PUBLIC_SAFE/machine_readable/V10634_BUCKET_QUALITY_TABLE_AUDIT.json)
5. [V10634 Rule Pipeline Flow (12-stage DAG with source-file refs)](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/V106_34_RULE_PIPELINE_MECHANISM_AUDIT_PUBLIC_SAFE/machine_readable/V10634_RULE_PIPELINE_FLOW.json)
6. [V10634 DB Audit Live Data (105 rules across 21 buckets)](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/V106_34_RULE_PIPELINE_MECHANISM_AUDIT_PUBLIC_SAFE/machine_readable/V10634_DB_AUDIT_LIVE_DATA.json)
7. [V10634 Execution Summary](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/V106_34_RULE_PIPELINE_MECHANISM_AUDIT_PUBLIC_SAFE/machine_readable/V10634_EXECUTION_SUMMARY.json)


Latest: **V106.33** - `V106_33_LIVE_CONTROL_SEMANTIC_RECONCILE_PUBLIC_SAFE/V10633_OWNER_REPORT_VN_PUBLIC.md` (live control semantic reconciliation; report-only; no public code deploy).

## Quick links - V106.33

1. [LATEST_REPORT.json](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/LATEST_REPORT.json)
2. [Owner Report](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/V106_33_LIVE_CONTROL_SEMANTIC_RECONCILE_PUBLIC_SAFE/V10633_OWNER_REPORT_VN_PUBLIC.md)
3. [Semantic Reconciliation](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/V106_33_LIVE_CONTROL_SEMANTIC_RECONCILE_PUBLIC_SAFE/V10633_SEMANTIC_RECONCILIATION_PUBLIC.md)
4. [Risk Deep Dive](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/V106_33_LIVE_CONTROL_SEMANTIC_RECONCILE_PUBLIC_SAFE/V10633_RISK_DEEP_DIVE_PUBLIC.md)
5. [Runbook](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/V106_33_LIVE_CONTROL_SEMANTIC_RECONCILE_PUBLIC_SAFE/V10633_LIVE_20260527_RUNBOOK_PUBLIC.md)

Latest: **V106.32** - `V106_32_TOTAL_FORCE_PRELIVE_CONTROL_MB_INDEPENDENT_SHADOW_PUBLIC_SAFE/V10632_OWNER_REPORT_VN_PUBLIC.md` (total-force prelive control + MB independent shadow repair; official protected).

## Quick links - V106.32

1. [LATEST_REPORT.json](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/LATEST_REPORT.json)
2. [Owner Report](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/V106_32_TOTAL_FORCE_PRELIVE_CONTROL_MB_INDEPENDENT_SHADOW_PUBLIC_SAFE/V10632_OWNER_REPORT_VN_PUBLIC.md)
3. [Safety Gate](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/V106_32_TOTAL_FORCE_PRELIVE_CONTROL_MB_INDEPENDENT_SHADOW_PUBLIC_SAFE/V10632_SAFETY_GATE_PUBLIC.md)
4. [MB Cost Kill](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/V106_32_TOTAL_FORCE_PRELIVE_CONTROL_MB_INDEPENDENT_SHADOW_PUBLIC_SAFE/V10632_MB_COST_KILL_PUBLIC.md)
5. [Next Live Runbook](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/V106_32_TOTAL_FORCE_PRELIVE_CONTROL_MB_INDEPENDENT_SHADOW_PUBLIC_SAFE/V10632_NEXT_LIVE_RUNBOOK_PUBLIC.md)

Latest: **V106.31** - `V106_31_TRI_REGION_POST_LIVE_CLOSEOUT_MB_COST_FORENSIC_PUBLIC_SAFE/V10631_OWNER_REPORT_VN_PUBLIC.md` (tri-region post-live closeout + MB cost forensic; official protected).

## Quick links - V106.31

1. [LATEST_REPORT.json](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/LATEST_REPORT.json)
2. [Owner Report](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/V106_31_TRI_REGION_POST_LIVE_CLOSEOUT_MB_COST_FORENSIC_PUBLIC_SAFE/V10631_OWNER_REPORT_VN_PUBLIC.md)
3. [Closeout Summary](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/V106_31_TRI_REGION_POST_LIVE_CLOSEOUT_MB_COST_FORENSIC_PUBLIC_SAFE/V10631_TRI_REGION_CLOSEOUT_SUMMARY_PUBLIC.md)
4. [MB Cost Waste](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/V106_31_TRI_REGION_POST_LIVE_CLOSEOUT_MB_COST_FORENSIC_PUBLIC_SAFE/V10631_MB_COST_WASTE_PUBLIC.md)
5. [Next Live Plan](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/V106_31_TRI_REGION_POST_LIVE_CLOSEOUT_MB_COST_FORENSIC_PUBLIC_SAFE/V10631_NEXT_LIVE_PLAN_PUBLIC.md)

Latest: **V106.30B** - `V106_30B_FINAL_TOMORROW_LIVE_LOCK_PUBLIC_SAFE/V10630B_OWNER_REPORT_VN_PUBLIC.md` (final tomorrow live lock; owner can rest; no mining/no official mutation).

## Quick links - V106.30B

1. [LATEST_REPORT.json](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/LATEST_REPORT.json)
2. [Owner Report](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/V106_30B_FINAL_TOMORROW_LIVE_LOCK_PUBLIC_SAFE/V10630B_OWNER_REPORT_VN_PUBLIC.md)
3. [Sleep Summary](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/V106_30B_FINAL_TOMORROW_LIVE_LOCK_PUBLIC_SAFE/V10630B_OWNER_SLEEP_SUMMARY_VN_PUBLIC.md)
4. [Checkpoint Lock](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/V106_30B_FINAL_TOMORROW_LIVE_LOCK_PUBLIC_SAFE/V10630B_TOMORROW_LIVE_CHECKPOINT_LOCK_PUBLIC.md)

Latest: **V106.30A** - `V106_30A_DETAILED_EVIDENCE_NEXT_LIVE_LOCK_PUBLIC_SAFE/V10630A_OWNER_REPORT_VN_PUBLIC.md` (detailed evidence package for V106.30; public-safe; official protected).

## Quick links - V106.30A

1. [LATEST_REPORT.json](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/LATEST_REPORT.json)
2. [Owner Report](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/V106_30A_DETAILED_EVIDENCE_NEXT_LIVE_LOCK_PUBLIC_SAFE/V10630A_OWNER_REPORT_VN_PUBLIC.md)
3. [Tri-region Board](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/V106_30A_DETAILED_EVIDENCE_NEXT_LIVE_LOCK_PUBLIC_SAFE/V10630A_TRI_REGION_MASTER_BOARD_PUBLIC.md)
4. [MB Cost Detail](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/V106_30A_DETAILED_EVIDENCE_NEXT_LIVE_LOCK_PUBLIC_SAFE/V10630A_MB_COST_WASTE_DETAIL_PUBLIC.md)
5. [Next Live Plan](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/V106_30A_DETAILED_EVIDENCE_NEXT_LIVE_LOCK_PUBLIC_SAFE/V10630A_NEXT_LIVE_SAFE_PLAN_VN.md)

Latest: **V106.30** - `V106_30_TRI_REGION_TOTAL_SHADOW_LANE_INTERVENTION_PUBLIC_SAFE/V10630_OWNER_REPORT_VN_PUBLIC.md` (tri-region shadow/lane intervention + MB cost kill gate; official protected).

## Quick links - V106.30

1. [LATEST_REPORT.json](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/LATEST_REPORT.json)
2. [Owner Report](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/V106_30_TRI_REGION_TOTAL_SHADOW_LANE_INTERVENTION_PUBLIC_SAFE/V10630_OWNER_REPORT_VN_PUBLIC.md)
3. [Execution Summary JSON](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/V106_30_TRI_REGION_TOTAL_SHADOW_LANE_INTERVENTION_PUBLIC_SAFE/machine_readable/V10630_EXECUTION_SUMMARY.json)
4. [Tri-region Board](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/V106_30_TRI_REGION_TOTAL_SHADOW_LANE_INTERVENTION_PUBLIC_SAFE/V10630_TRI_REGION_BOARD_PUBLIC.md)
5. [AI Cost Value](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/V106_30_TRI_REGION_TOTAL_SHADOW_LANE_INTERVENTION_PUBLIC_SAFE/V10630_AI_COST_VALUE_PUBLIC.md)

Latest: **V106.29R1** - `V106_29R1_REGION_ISOLATED_RULE_SHADOW_IMPORT_PUBLIC_SAFE/V10629R1_OWNER_REPORT_VN_PUBLIC.md` (region-isolated rule shadow import; official protected; no deploy/cron/provider/rule import official).

## Quick links - V106.29R1

1. [LATEST_REPORT.json](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/LATEST_REPORT.json)
2. [Owner Report](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/V106_29R1_REGION_ISOLATED_RULE_SHADOW_IMPORT_PUBLIC_SAFE/V10629R1_OWNER_REPORT_VN_PUBLIC.md)
3. [Execution Summary JSON](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/V106_29R1_REGION_ISOLATED_RULE_SHADOW_IMPORT_PUBLIC_SAFE/machine_readable/V10629R1_EXECUTION_SUMMARY.json)
4. [Region Isolation](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/V106_29R1_REGION_ISOLATED_RULE_SHADOW_IMPORT_PUBLIC_SAFE/V10629R1_REGION_ISOLATION_PUBLIC.md)
5. [Safety Gate](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/V106_29R1_REGION_ISOLATED_RULE_SHADOW_IMPORT_PUBLIC_SAFE/V10629R1_SAFETY_GATE_PUBLIC.md)

Latest: **V106.28R0D** - `V106_28R0D_POST_LIVE_TRI_REGION_FORENSIC_PUBLIC_SAFE/V10628R0D_OWNER_REPORT_VN_PUBLIC.md` (post-live tri-region forensic + rule overlay; no official/provider/cron/deploy/lane promotion/rule import).

## Quick links - V106.28R0D

1. [LATEST_REPORT.json](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/LATEST_REPORT.json)
2. [Owner Report](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/V106_28R0D_POST_LIVE_TRI_REGION_FORENSIC_PUBLIC_SAFE/V10628R0D_OWNER_REPORT_VN_PUBLIC.md)
3. [Execution Summary JSON](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/V106_28R0D_POST_LIVE_TRI_REGION_FORENSIC_PUBLIC_SAFE/machine_readable/V10628R0D_EXECUTION_SUMMARY.json)
4. [Closeout](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/V106_28R0D_POST_LIVE_TRI_REGION_FORENSIC_PUBLIC_SAFE/V10628R0D_CLOSEOUT_PUBLIC.md)
5. [Rule Overlay](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/V106_28R0D_POST_LIVE_TRI_REGION_FORENSIC_PUBLIC_SAFE/V10628R0D_RULE_OVERLAY_PUBLIC.md)
6. [Root Cause](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/V106_28R0D_POST_LIVE_TRI_REGION_FORENSIC_PUBLIC_SAFE/V10628R0D_ROOT_CAUSE_PUBLIC.md)
7. [Safety Gate](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/V106_28R0D_POST_LIVE_TRI_REGION_FORENSIC_PUBLIC_SAFE/V10628R0D_SAFETY_GATE_PUBLIC.md)

Latest: **V106.28R0C** - `V106_28R0C_NEXT_LIVE_RUNTIME_CLOSEOUT_PUBLIC_SAFE/V10628R0C_OWNER_REPORT_VN_PUBLIC.md` (next-live runtime closeout + MT conversion gate + UI semantics lock; no official/provider/cron/deploy/lane promotion/rule import).

## Quick links - V106.28R0C

1. [LATEST_REPORT.json](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/LATEST_REPORT.json)
2. [Owner Report](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/V106_28R0C_NEXT_LIVE_RUNTIME_CLOSEOUT_PUBLIC_SAFE/V10628R0C_OWNER_REPORT_VN_PUBLIC.md)
3. [Execution Summary JSON](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/V106_28R0C_NEXT_LIVE_RUNTIME_CLOSEOUT_PUBLIC_SAFE/machine_readable/V10628R0C_EXECUTION_SUMMARY.json)
4. [Runtime Closeout](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/V106_28R0C_NEXT_LIVE_RUNTIME_CLOSEOUT_PUBLIC_SAFE/V10628R0C_RUNTIME_CLOSEOUT_PUBLIC.md)
5. [MT Conversion Gate](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/V106_28R0C_NEXT_LIVE_RUNTIME_CLOSEOUT_PUBLIC_SAFE/V10628R0C_MT_CONVERSION_GATE_PUBLIC.md)
6. [UI Semantics](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/V106_28R0C_NEXT_LIVE_RUNTIME_CLOSEOUT_PUBLIC_SAFE/V10628R0C_UI_SEMANTICS_PUBLIC.md)

Latest: **V106.28R0B** - `V106_28R0B_V108_ADAPTER_FIX_LIVE_MEASUREMENT_PUBLIC_SAFE/V10628R0B_OWNER_REPORT_VN_PUBLIC.md` (V108 adapter fix + live measurement closeout; no official/provider/cron/deploy/lane promotion/rule import).

## Quick links - V106.28R0B

1. [LATEST_REPORT.json](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/LATEST_REPORT.json)
2. [Owner Report](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/V106_28R0B_V108_ADAPTER_FIX_LIVE_MEASUREMENT_PUBLIC_SAFE/V10628R0B_OWNER_REPORT_VN_PUBLIC.md)
3. [Execution Summary JSON](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/V106_28R0B_V108_ADAPTER_FIX_LIVE_MEASUREMENT_PUBLIC_SAFE/machine_readable/V10628R0B_EXECUTION_SUMMARY.json)
4. [V108 Adapter Fix](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/V106_28R0B_V108_ADAPTER_FIX_LIVE_MEASUREMENT_PUBLIC_SAFE/V10628R0B_V108_ADAPTER_FIX_PUBLIC.md)
5. [Live Measurement Closeout](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/V106_28R0B_V108_ADAPTER_FIX_LIVE_MEASUREMENT_PUBLIC_SAFE/V10628R0B_LIVE_MEASUREMENT_CLOSEOUT_PUBLIC.md)
6. [MT Conversion Closeout](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/V106_28R0B_V108_ADAPTER_FIX_LIVE_MEASUREMENT_PUBLIC_SAFE/V10628R0B_MT_CONVERSION_CLOSEOUT_PUBLIC.md)
7. [Safety Gate](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/V106_28R0B_V108_ADAPTER_FIX_LIVE_MEASUREMENT_PUBLIC_SAFE/V10628R0B_SAFETY_GATE_PUBLIC.md)

Latest: **V106.28R0A-TOTAL-2** - `V106_28R0A_TOTAL_2_POST_V10629_CONTROL_PUBLIC_SAFE/V10628R0A_OWNER_REPORT_VN_PUBLIC.md` (post-V106.29 total-control public-safe package; V106.28R1 not run; V108 partial blocked; no official/provider/cron/deploy/lane promotion/rule import).

## Quick links - V106.28R0A-TOTAL-2

1. [LATEST_REPORT.json](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/LATEST_REPORT.json)
2. [Owner Report](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/V106_28R0A_TOTAL_2_POST_V10629_CONTROL_PUBLIC_SAFE/V10628R0A_OWNER_REPORT_VN_PUBLIC.md)
3. [Execution Summary JSON](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/V106_28R0A_TOTAL_2_POST_V10629_CONTROL_PUBLIC_SAFE/machine_readable/V10628R0A_EXECUTION_SUMMARY.json)
4. [Master Issue Matrix](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/V106_28R0A_TOTAL_2_POST_V10629_CONTROL_PUBLIC_SAFE/V10628R0A_MASTER_ISSUE_MATRIX_PUBLIC.md)
5. [Schema Extractor Audit](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/V106_28R0A_TOTAL_2_POST_V10629_CONTROL_PUBLIC_SAFE/V10628R0A_SCHEMA_EXTRACTOR_AUDIT_PUBLIC.md)
6. [V108 Blocker](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/V106_28R0A_TOTAL_2_POST_V10629_CONTROL_PUBLIC_SAFE/V10628R0A_V108_BLOCKER_PUBLIC.md)
7. [Next Live Runbook](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/V106_28R0A_TOTAL_2_POST_V10629_CONTROL_PUBLIC_SAFE/V10628R0A_NEXT_LIVE_RUNBOOK_PUBLIC.md)
8. [Safety Gate](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/V106_28R0A_TOTAL_2_POST_V10629_CONTROL_PUBLIC_SAFE/V10628R0A_SAFETY_GATE_PUBLIC.md)

Latest: **V106.29** - `V106_29_ONE_PASS_LIVE_READINESS_CONTROL_PUBLIC_SAFE/V10629_OWNER_REPORT_VN_PUBLIC.md` (one-pass live readiness public-safe package; diagnostic-only; V106.28R1 not run; schema/extractor gate blocks rule import; official/provider/wallet/cron/deploy all false).

## Quick links - V106.29

1. [LATEST_REPORT.json](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/LATEST_REPORT.json)
2. [V106.29 Owner Report VN Public](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/V106_29_ONE_PASS_LIVE_READINESS_CONTROL_PUBLIC_SAFE/V10629_OWNER_REPORT_VN_PUBLIC.md)
3. [V106.29 Execution Summary JSON](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/V106_29_ONE_PASS_LIVE_READINESS_CONTROL_PUBLIC_SAFE/machine_readable/V10629_EXECUTION_SUMMARY.json)
4. [V106.29 Master Issue Matrix](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/V106_29_ONE_PASS_LIVE_READINESS_CONTROL_PUBLIC_SAFE/V10629_MASTER_ISSUE_MATRIX_PUBLIC.md)
5. [V106.29 Next Live Runbook](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/V106_29_ONE_PASS_LIVE_READINESS_CONTROL_PUBLIC_SAFE/V10629_NEXT_LIVE_RUNBOOK_PUBLIC.md)
6. [V106.29 Safety Gate](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/V106_29_ONE_PASS_LIVE_READINESS_CONTROL_PUBLIC_SAFE/V10629_SAFETY_GATE_PUBLIC.md)
7. [V106.29 Zero Official Drift](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/V106_29_ONE_PASS_LIVE_READINESS_CONTROL_PUBLIC_SAFE/V10629_ZERO_OFFICIAL_DRIFT_PUBLIC.md)
8. [V106.29 Schema Extractor Audit](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/V106_29_ONE_PASS_LIVE_READINESS_CONTROL_PUBLIC_SAFE/V10629_SCHEMA_EXTRACTOR_AUDIT_PUBLIC.md)

Latest: **V106.26.2** - `V106_26_TOTAL_SOURCE_VERIFY_AND_FU_PUBLIC_SAFE/V10626_FU4_OWNER_SCHEMA_REPORT_VN_PUBLIC.md` (FU4 OWNER_SCHEMA_FIX: 2026-05-25 owner image confirmed MB low-prize source set includes G.4/G.6/G.7 — missed by FU3. Full rescan: 20,843 positive rules (+3,220 NEW from MB G4/G6/G7). Stability w60/w90/w180 audit -> 13 STABLE_ALL added to pre-register panel. Combined panel: 58 baseline + 13 addendum = 71 PRE_REGISTER_ONLY total. live_eligible=0.).

## Quick links - V106.26.2 FU4

1. [LATEST_REPORT.json](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/LATEST_REPORT.json)
2. [V10626 FU4 Owner-Schema Report VN (NEWEST MAIN)](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/V106_26_TOTAL_SOURCE_VERIFY_AND_FU_PUBLIC_SAFE/V10626_FU4_OWNER_SCHEMA_REPORT_VN_PUBLIC.md)
3. [V10626 FU4 Pre-Register Addendum Summary JSON (13 NEW STABLE_ALL)](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/V106_26_TOTAL_SOURCE_VERIFY_AND_FU_PUBLIC_SAFE/machine_readable/V10626_FU4_PRE_REGISTER_ADDENDUM_SUMMARY.json)
4. [V10626 FU4 Pre-Register Addendum MB CSV (4 self-lag NEW)](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/V106_26_TOTAL_SOURCE_VERIFY_AND_FU_PUBLIC_SAFE/machine_readable/V10626_FU4_PRE_REGISTER_ADDENDUM_MB.csv)
5. [V10626 FU4 Pre-Register Addendum MN CSV (3 cross MB->MN NEW)](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/V106_26_TOTAL_SOURCE_VERIFY_AND_FU_PUBLIC_SAFE/machine_readable/V10626_FU4_PRE_REGISTER_ADDENDUM_MN.csv)
6. [V10626 FU4 Pre-Register Addendum MT CSV (6 cross MB->MT NEW)](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/V106_26_TOTAL_SOURCE_VERIFY_AND_FU_PUBLIC_SAFE/machine_readable/V10626_FU4_PRE_REGISTER_ADDENDUM_MT.csv)
7. [V10626 FU4 Stability Audit w60/w90/w180 JSON (24 candidates classified)](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/V106_26_TOTAL_SOURCE_VERIFY_AND_FU_PUBLIC_SAFE/machine_readable/V10626_FU4_NEW_MB_CANDIDATES_STABILITY.json)
8. [V10626 FU4 Owner-Schema Scan Summary JSON (full 20,843 rules)](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/V106_26_TOTAL_SOURCE_VERIFY_AND_FU_PUBLIC_SAFE/machine_readable/V10626_FU4_OWNER_SCHEMA_SUMMARY.json)


Latest: **V106.26** - `V106_26_TOTAL_SOURCE_VERIFY_AND_FU_PUBLIC_SAFE/V10626_FU_FULL_REPORT_VN_PUBLIC.md` (total source rule verify + FU1/FU2/FU3 comprehensive cross-source for MN/MT/MB; 55,546 main inventory rules + 12,966 new low-prize positive rules; 19 PRE_REGISTER_ONLY candidates).

## Quick links - V106.26

1. [LATEST_REPORT.json](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/LATEST_REPORT.json)
2. [V10626 FU Full Report VN (MAIN)](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/V106_26_TOTAL_SOURCE_VERIFY_AND_FU_PUBLIC_SAFE/V10626_FU_FULL_REPORT_VN_PUBLIC.md)
3. [V10626 Owner Report VN](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/V106_26_TOTAL_SOURCE_VERIFY_AND_FU_PUBLIC_SAFE/V10626_OWNER_REPORT_VN_PUBLIC.md)
4. [V10626 FU MB DB D-2 Verify](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/V106_26_TOTAL_SOURCE_VERIFY_AND_FU_PUBLIC_SAFE/V10626_FU_OWNER_REPORT_VN_PUBLIC.md)
5. [V10626 FU Comprehensive (pre-schema-fix)](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/V106_26_TOTAL_SOURCE_VERIFY_AND_FU_PUBLIC_SAFE/V10626_FU_COMPREHENSIVE_REPORT_VN_PUBLIC.md)
6. [V10626 Methodology](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/V106_26_TOTAL_SOURCE_VERIFY_AND_FU_PUBLIC_SAFE/V10626_METHODOLOGY_PUBLIC.md)
7. [V10626 Target-Source Coverage Matrix](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/V106_26_TOTAL_SOURCE_VERIFY_AND_FU_PUBLIC_SAFE/V10626_TARGET_SOURCE_COVERAGE_MATRIX_PUBLIC.md)
8. [V10626 Pre-Register Panel Summary](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/V106_26_TOTAL_SOURCE_VERIFY_AND_FU_PUBLIC_SAFE/V10626_PRE_REGISTER_PANEL_SUMMARY_PUBLIC.md)
9. [V10626 V107 Overfit Warning](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/V106_26_TOTAL_SOURCE_VERIFY_AND_FU_PUBLIC_SAFE/V10626_OVERFIT_WARNING_PUBLIC.md)
10. [V10626 FU3 Low Prize Summary JSON](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/V106_26_TOTAL_SOURCE_VERIFY_AND_FU_PUBLIC_SAFE/machine_readable/V10626_FU3_KEYNAME_LOW_PRIZE_SUMMARY.json)
11. [V10626 FU3 Top-600 Rules CSV](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/V106_26_TOTAL_SOURCE_VERIFY_AND_FU_PUBLIC_SAFE/machine_readable/V10626_FU3_TOP_600_RULES.csv)
12. [V10626 19 New Candidate Rules JSON](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/V106_26_TOTAL_SOURCE_VERIFY_AND_FU_PUBLIC_SAFE/machine_readable/V10626_19_NEW_CANDIDATE_RULES.json)
13. [V10626 Execution Summary JSON](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/V106_26_TOTAL_SOURCE_VERIFY_AND_FU_PUBLIC_SAFE/machine_readable/V10626_EXECUTION_SUMMARY.json)


Latest: **V107** - `V107_NULL_AND_SIGNAL_TEST_PUBLIC_SAFE/V107_OWNER_REPORT_VN_PUBLIC.md` (null-hypothesis stress test on V106.x framework; 5 null tests + 2 integrity families; 0/153228 rules survive multiple-testing correction; recommends pre-register <50 rules and wait actual 90d).

## Quick links - V107

1. [LATEST_REPORT.json](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/LATEST_REPORT.json)
2. [V107 Owner Report VN](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/V107_NULL_AND_SIGNAL_TEST_PUBLIC_SAFE/V107_OWNER_REPORT_VN_PUBLIC.md)
3. [V107 Methodology](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/V107_NULL_AND_SIGNAL_TEST_PUBLIC_SAFE/V107_METHODOLOGY_PUBLIC.md)
4. [V107 Null Test 1 Permutation](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/V107_NULL_AND_SIGNAL_TEST_PUBLIC_SAFE/machine_readable/V107_NULL1_PERMUTATION.json)
5. [V107 Null Test 2 Negative Control](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/V107_NULL_AND_SIGNAL_TEST_PUBLIC_SAFE/machine_readable/V107_NULL2_NEGATIVE_CONTROL.json)
6. [V107 Null Test 3 Multiple Testing Correction](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/V107_NULL_AND_SIGNAL_TEST_PUBLIC_SAFE/machine_readable/V107_NULL3_CORRECTION.json)
7. [V107 Null Test 4 Sub-sample Replication](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/V107_NULL_AND_SIGNAL_TEST_PUBLIC_SAFE/machine_readable/V107_NULL4_SUBSAMPLE.json)
8. [V107 Null Test 5 Forward Audit](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/V107_NULL_AND_SIGNAL_TEST_PUBLIC_SAFE/machine_readable/V107_NULL5_FORWARD_AUDIT.json)
9. [V107 Family A Autocorrelation](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/V107_NULL_AND_SIGNAL_TEST_PUBLIC_SAFE/machine_readable/V107_FAMILY_A_AUTOCORR.json)
10. [V107 Family D Reverse Causality](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/V107_NULL_AND_SIGNAL_TEST_PUBLIC_SAFE/machine_readable/V107_FAMILY_D_REVERSE_CAUSALITY.json)


Latest: **V106.06** - `V106_06_DEEP_SOURCE_RULE_DISCOVERY_PUBLIC_SAFE/V10606_OWNER_REPORT_VN_PUBLIC.md` (deep source-rule discovery for MN/MT/MB; 153,228 rules tested, full Vietnamese owner report; recommends shadow modules; no official change).

## Quick links - V106.06

1. [LATEST_REPORT.json](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/LATEST_REPORT.json)
2. [V106.06 Owner Report VN](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/V106_06_DEEP_SOURCE_RULE_DISCOVERY_PUBLIC_SAFE/V10606_OWNER_REPORT_VN_PUBLIC.md)
3. [V106.06 Methodology](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/V106_06_DEEP_SOURCE_RULE_DISCOVERY_PUBLIC_SAFE/V10606_METHODOLOGY_PUBLIC.md)
4. [V106.06 Manifest](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/V106_06_DEEP_SOURCE_RULE_DISCOVERY_PUBLIC_SAFE/V10606_MANIFEST.md)
5. [V106.06 Overfit Warning Report](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/V106_06_DEEP_SOURCE_RULE_DISCOVERY_PUBLIC_SAFE/V10606_OVERFIT_WARNING_REPORT.md)
6. [V106.06 Summary JSON](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/V106_06_DEEP_SOURCE_RULE_DISCOVERY_PUBLIC_SAFE/machine_readable/V10606_SUMMARY.json)
7. [V106.06 Top Rules By Target Region](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/V106_06_DEEP_SOURCE_RULE_DISCOVERY_PUBLIC_SAFE/machine_readable/V10606_TOP_RULES_BY_TARGET_REGION.json)
8. [V106.06 Top 600 Rules CSV](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/V106_06_DEEP_SOURCE_RULE_DISCOVERY_PUBLIC_SAFE/machine_readable/V10606_TOP_600_RULES.csv)
9. [V106.06 Agreement Rules JSON](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/V106_06_DEEP_SOURCE_RULE_DISCOVERY_PUBLIC_SAFE/machine_readable/V10606_AGREEMENT_RULES.json)


Latest: **V106.05** ? `V106_05_MT_FROM_MB_D1D3_PUBLIC_SAFE/V10605_OWNER_REPORT_VN_PUBLIC.md` (MT target from MB D-1/D-2/D-3 low-prize digit-transform analysis; recommends measurement-only shadow module).

## Quick links ? V106.05

1. [LATEST_REPORT.json](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/LATEST_REPORT.json)
2. [V106.05 Owner Report](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/V106_05_MT_FROM_MB_D1D3_PUBLIC_SAFE/V10605_OWNER_REPORT_VN_PUBLIC.md)
3. [V106.05 Methodology](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/V106_05_MT_FROM_MB_D1D3_PUBLIC_SAFE/V10605_METHODOLOGY_PUBLIC.md)
4. [V106.05 Summary JSON](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/V106_05_MT_FROM_MB_D1D3_PUBLIC_SAFE/machine_readable/V10605_SUMMARY.json)


Latest: **V106.03** ? `V106_03_MB_G2_PAIR_LAG_RECURRENCE_PUBLIC_SAFE/V10603_OWNER_REPORT_VN_PUBLIC.md` (public-safe analysis of MB Gi?i nh? both-number D-1/D-2/D-3 recurrence into MN D; D-2 recommended as primary no-token source-pool feature; official unchanged).

## Quick links ? V106.03 (read first)

1. [LATEST_REPORT.json](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/LATEST_REPORT.json) ? machine pointer + latest status.
2. [V106.03 Owner Report VN](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/V106_03_MB_G2_PAIR_LAG_RECURRENCE_PUBLIC_SAFE/V10603_OWNER_REPORT_VN_PUBLIC.md) ? detailed Vietnamese report.
3. [V106.03 Methodology](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/V106_03_MB_G2_PAIR_LAG_RECURRENCE_PUBLIC_SAFE/V10603_METHODOLOGY_PUBLIC.md) ? extraction and baseline notes.
4. [V106.03 Summary JSON](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/V106_03_MB_G2_PAIR_LAG_RECURRENCE_PUBLIC_SAFE/machine_readable/V10603_SUMMARY.json) ? machine-readable summary.


Latest: **V105.41** — `V105_41_MORNING_COMPREHENSIVE_AUDIT_20260514/evidence/` (comprehensive morning audit at the start of 2026-05-14 live cycle; yesterday MN/MT/MB closed naturally with MT BT=92 WIN; today MN BT=16 ACTIVE strong; closed-file regression scope confirmed wider — 14 events across 7 source paths; V105.40 expansion patch owner-gated; official prediction path unaffected; NATURAL_VERIFY_PARTIAL_PASS_NOT_FULL_PASS preserved).

## Quick links — V105.41 (read first)

1. [LATEST_REPORT.json](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/LATEST_REPORT.json) — machine pointer + latest status.
2. [V105.41 README](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/V105_41_MORNING_COMPREHENSIVE_AUDIT_20260514/README.md) — overview of the V105.41 wrapper.
3. [V105.41 Morning Comprehensive Report](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/V105_41_MORNING_COMPREHENSIVE_AUDIT_20260514/evidence/V105_41_MORNING_COMPREHENSIVE_REPORT.md) — day-control audit, yesterday closeout, today MN cycle, regression scope.
4. [V105.41 Model Health and Methodology Deep Dive](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/V105_41_MORNING_COMPREHENSIVE_AUDIT_20260514/evidence/V105_41_MODEL_HEALTH_AND_METHODOLOGY_DEEP_DIVE.md) — 30-day per-model scoreboard, prompt mechanism, ML pipeline, rule engine, scoring/voting, recommendations.
5. [V105.41 Runtime Stability and Governance](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/V105_41_MORNING_COMPREHENSIVE_AUDIT_20260514/evidence/V105_41_RUNTIME_STABILITY_AND_GOVERNANCE.md) — runtime timeline V105.30d → V105.41, closed-file regression map, governance locks, owner decisions queue.
6. [V105.36 Closeout Audit Only](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/V105_36_CLOSEOUT_AUDIT_ONLY_20260512/evidence/V105_36_CLOSEOUT_AUDIT_ONLY_REPORT.md) — closeout audit baseline (no natural verify pass).
7. [V105.36 Final Safe Closeout Combined Report](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/V105_36_CLOSEOUT_AUDIT_ONLY_20260512/evidence/V105_36_V105_37_FINAL_SAFE_CLOSEOUT_REPORT.md) — combined V105.36 + V105.37 closeout with timeline.
8. [V105.38 Timeout Extended Grace Proposal Only](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/V105_36_CLOSEOUT_AUDIT_ONLY_20260512/evidence/V105_38_TIMEOUT_EXTENDED_GRACE_PROPOSAL_ONLY.md) — 500s proposal design (not deployed).
9. [OPEN_ISSUES.md](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/OPEN_ISSUES.md) — active open items after V105.41.
10. [NEXT_ACTION.md](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/NEXT_ACTION.md) — next owner / runtime actions.

Current override: V105.41 supersedes the public-side narrative for V105.36..V105.40 by publishing the closeout wrapper and deep-dive analytical reports alongside today's morning audit. Official `/du-doan` lock remains intact.

## Quick links — V105.33 (read first)

1. [LATEST_REPORT.json](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/LATEST_REPORT.json) — machine pointer + latest status.
2. [V105_33_NATURAL_VERIFY_SNAPSHOT_REPORT.md](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/V105_33_NATURAL_VERIFY_SNAPSHOT_20260512/evidence/V105_33_NATURAL_VERIFY_SNAPSHOT_REPORT.md) — 16:00 VN natural verify snapshot.
3. [OPEN_ISSUES.md](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/OPEN_ISSUES.md) — active open items after V105.33.
4. [NEXT_ACTION.md](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/NEXT_ACTION.md) — next owner/runtime actions.

Current override: V105.33 does not supersede V105.32 truth; it extends it with a newer read-only snapshot. `V105_33_NATURAL_VERIFY_PASS` is still not allowed until MN/MT/MB all complete natural cycles cleanly.

## Quick links — V105.32 (read first)

1. [LATEST_REPORT.json](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/LATEST_REPORT.json) — machine pointer + latest status.
2. [V105_32_SAFE_CONTINUATION_REPORT.md](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/V105_32_SAFE_CONTINUATION_20260512/evidence/V105_32_SAFE_CONTINUATION_REPORT.md) — natural verify snapshot, open gates, public cleanup.
3. [glm-5.1_compact_json_profile.md](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/V105_32_SAFE_CONTINUATION_20260512/evidence/glm-5.1_compact_json_profile.md) — owner-gated GLM compact profile proposal.
4. [SOURCE_POOL_ROOT_CAUSE_DRILLDOWN_PLAN.md](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/V105_32_SAFE_CONTINUATION_20260512/evidence/SOURCE_POOL_ROOT_CAUSE_DRILLDOWN_PLAN.md) — accuracy root-cause plan.
5. [OPEN_ISSUES.md](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/OPEN_ISSUES.md) — active open items after V105.32.
6. [NEXT_ACTION.md](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/NEXT_ACTION.md) — next owner/runtime actions.

Current override: V105.32 does not supersede V105.31 truth; it extends it with a newer read-only snapshot and proposals. `NATURAL_VERIFY_PASS` is still not allowed until MN/MT/MB all complete natural cycles cleanly.

## Quick links — V105.31 (read first)

1. [LATEST_REPORT.json](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/LATEST_REPORT.json) — machine pointer + latest status.
2. [V105_31_CURRENT_TRUTH_CLEAN_WRAPPER.md](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/V105_31_CURRENT_TRUTH_CLEAN_WRAPPER_20260512/evidence/V105_31_CURRENT_TRUTH_CLEAN_WRAPPER.md) — current truth wrapper, including GLM policy and natural verify status.
3. [OPEN_ISSUES.md](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/OPEN_ISSUES.md) — active open items after V105.31.
4. [NEXT_ACTION.md](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/NEXT_ACTION.md) — next owner/runtime actions.

Current override: V105.31 supersedes V105.30/V105.30b/V105.30c stale wording where it conflicts. In particular: only timeout/waiting-timeout may remain truly missing; non-timeout shadow failures must persist diagnostic rows; Rule105 prize lock is by `source_region`.

## Quick links — V105.30 (read in order)

1. [LATEST_REPORT.json](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/LATEST_REPORT.json) — machine pointer + status one-liner.
2. [V105_30_FINALIZATION_REPORT.md](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/V105_30_FINALIZATION_SAFE_STDIO_DEPLOY_20260512/evidence/V105_30_FINALIZATION_REPORT.md) — báo cáo đầy đủ (tiếng Việt).
3. [v10530_rule105_recheck.json](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/V105_30_FINALIZATION_SAFE_STDIO_DEPLOY_20260512/evidence/v10530_rule105_recheck.json) — **0** true violations after source_region correction.

Current override: read the top **READ THIS FIRST** block in `V105_30_FINALIZATION_REPORT.md`; it supersedes older lines inside the original audit body about SSH pending and Rule105 quarantine.

## Latest evidence (V105.30)

- [V105_30_FINALIZATION_REPORT.md](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/V105_30_FINALIZATION_SAFE_STDIO_DEPLOY_20260512/evidence/V105_30_FINALIZATION_REPORT.md) — full Vietnamese report; stability PASS for safe-stdio deploy; experiments HOLD.
- [v10530_master_audit.json](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/V105_30_FINALIZATION_SAFE_STDIO_DEPLOY_20260512/evidence/v10530_master_audit.json) — lane summary.
- [v10530_rule105_recheck.json](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/V105_30_FINALIZATION_SAFE_STDIO_DEPLOY_20260512/evidence/v10530_rule105_recheck.json) — Rule105 V105.30b recheck.
- [v10530_hash_double_check.json](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/V105_30_FINALIZATION_SAFE_STDIO_DEPLOY_20260512/evidence/v10530_hash_double_check.json) — official 4-table integrity proof.

## Previous evidence (V105.29)

- [V105_29_LOSE_CARRYOVER_RUNTIME_STABILITY_REPORT.md](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/V105_29_LOSE_CARRYOVER_RUNTIME_STABILITY_20260512/evidence/V105_29_LOSE_CARRYOVER_RUNTIME_STABILITY_REPORT.md) — lose-carryover signal layer + runtime stability.

## Previous evidence (V105.28)

- [V105_28_RUNTIME_CONTRACT_REPORT.md](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/V105_28_RUNTIME_CONTRACT_VERIFY_20260511/evidence/V105_28_RUNTIME_CONTRACT_REPORT.md) — full Vietnamese report (17 sections); status PARTIAL_NOT_PASS.
- [v10528_preflight.json](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/V105_28_RUNTIME_CONTRACT_VERIFY_20260511/evidence/v10528_preflight.json) — pre-hash + env flags + git state + live sync manifest.
- [v10528_runtime_contract_audit.json](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/V105_28_RUNTIME_CONTRACT_VERIFY_20260511/evidence/v10528_runtime_contract_audit.json) — 11 lanes audit.
- [v10528_deep_probes.json](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/V105_28_RUNTIME_CONTRACT_VERIFY_20260511/evidence/v10528_deep_probes.json) — closed_file detail + DD distribution + tensor ranking.
- [v10528_security_and_rules.json](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/V105_28_RUNTIME_CONTRACT_VERIFY_20260511/evidence/v10528_security_and_rules.json) — secret scan + git remote + station identity + 105 rules window consistency.
- [v10528_post_hash.json](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/V105_28_RUNTIME_CONTRACT_VERIFY_20260511/evidence/v10528_post_hash.json) — post-hash proof identical to pre-hash for 4 official tables.

---

## Previous evidence (V105.27)

- [V105_27_TOTAL_FORCE_CONTROL_REPORT.md](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/V105_27_TOTAL_FORCE_CONTROL_20260511/evidence/V105_27_TOTAL_FORCE_CONTROL_REPORT.md) — final Vietnamese report; status PARTIAL, not PASS.
- [OWNER_DECISION_REGISTER.md](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/V105_27_TOTAL_FORCE_CONTROL_20260511/evidence/OWNER_DECISION_REGISTER.md) — owner decisions pending.
- [MASTER_SSOT_RECONCILIATION_MATRIX.md](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/V105_27_TOTAL_FORCE_CONTROL_20260511/evidence/MASTER_SSOT_RECONCILIATION_MATRIX.md) — public/local/private/Notion matrix.
- [PROMPT_INJECTION_GAP.md](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/V105_27_TOTAL_FORCE_CONTROL_20260511/evidence/PROMPT_INJECTION_GAP.md) — prompt injection gap lineage.
- [TOP2_AB_RISK.md](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/V105_27_TOTAL_FORCE_CONTROL_20260511/evidence/TOP2_AB_RISK.md) — Top2/Bundler shadow risk.
- [MB_FORENSIC_OPTIONS.md](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/V105_27_TOTAL_FORCE_CONTROL_20260511/evidence/MB_FORENSIC_OPTIONS.md) — MB_D_v2 owner-gated options.
- [v10527_ranked_prompt_wire_audit_latest.json](../Lottery_AI_Test/artifacts/v10527/v10527_ranked_prompt_wire_audit_latest.json) — local DB-backed shadow materializer output.

---

## Previous evidence (V105.25)

- [V105_25_FINAL_REPORT.md](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/V105_25_STATION_ALIAS_FIXUP_20260511/evidence/V105_25_FINAL_REPORT.md) — full Vietnamese final report.

---

## Previous evidence (V105.24)

- [V105_24_FINAL_REPORT.md](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/V105_24_SOURCE_POOL_GAP_DRILLDOWN_20260511/evidence/V105_24_FINAL_REPORT.md) — V105.24 SOURCE_POOL_GAP_DRILLDOWN + V102_RELAXED_SHADOW + TOKEN_LOCK + RUNTIME_MANIFEST audit.
- [v10524_local_audit_latest.json](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/V105_24_SOURCE_POOL_GAP_DRILLDOWN_20260511/evidence/v10524_local_audit_latest.json)
- [v10524_station_code_audit.json](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/V105_24_SOURCE_POOL_GAP_DRILLDOWN_20260511/evidence/v10524_station_code_audit.json) — 62 alias residue (resolved in V105.25).
- [DEPLOYED_RUNTIME_MANIFEST.json](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/V105_24_SOURCE_POOL_GAP_DRILLDOWN_20260511/evidence/DEPLOYED_RUNTIME_MANIFEST.json)

---

## Previous evidence (V105.23)

- [V105_23_TOTAL_FORCE_CODE_TRUTH_AUDIT_REPORT.md](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/V105_23_TOTAL_FORCE_CODE_TRUTH_AUDIT_20260511/evidence/V105_23_TOTAL_FORCE_CODE_TRUTH_AUDIT_REPORT.md) — full Vietnamese audit report; final acceptance PARTIAL.
- [V105_23_SOURCE_POOL_AND_V102_AUDIT.md](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/V105_23_TOTAL_FORCE_CODE_TRUTH_AUDIT_20260511/evidence/V105_23_SOURCE_POOL_AND_V102_AUDIT.md)
- [V105_23_TOKEN_COST_GUARD_AUDIT.md](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/V105_23_TOTAL_FORCE_CODE_TRUTH_AUDIT_20260511/evidence/V105_23_TOKEN_COST_GUARD_AUDIT.md)
- [V105_23_UI_MODEL_COUNT_AUDIT.md](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/V105_23_TOTAL_FORCE_CODE_TRUTH_AUDIT_20260511/evidence/V105_23_UI_MODEL_COUNT_AUDIT.md)
- [V105_23_EVIDENCE_MATRIX.json](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/V105_23_TOTAL_FORCE_CODE_TRUTH_AUDIT_20260511/evidence/V105_23_EVIDENCE_MATRIX.json)

---

## Previous evidence (V105.22)

- [V105.22 Total Force Live Prep](V105_22_TOTAL_FORCE_LIVE_PREP_20260511/evidence/V105_22_TOTAL_FORCE_LIVE_PREP_REPORT.md)
- [V105.22 Region Profiles](V105_22_TOTAL_FORCE_LIVE_PREP_20260511/evidence/V105_22_REGION_INDEPENDENT_LANE_PROFILES.md)
- [V105.22 V102 STRONG Selector Shadow](V105_22_TOTAL_FORCE_LIVE_PREP_20260511/evidence/V105_22_V102_STRONG_SELECTOR_SHADOW.md)
- [V105.22 Candidate Universe Coverage](V105_22_TOTAL_FORCE_LIVE_PREP_20260511/evidence/V105_22_CANDIDATE_UNIVERSE_COVERAGE.md)
- [V105.22 Tomorrow Live Ready Checklist](V105_22_TOTAL_FORCE_LIVE_PREP_20260511/evidence/V105_22_TOMORROW_LIVE_READY_CHECKLIST.md)

---

## Previous evidence (V105.19)

- [V105.19 Hard Stabilization](V105_19_HARD_STABILIZATION_20260510/evidence/V105_19_HARD_STABILIZATION_REPORT.md)
- [V105.19 Runtime Control Matrix](V105_19_HARD_STABILIZATION_20260510/evidence/V105_19_RUNTIME_CONTROL_MATRIX.md)
- [V105.19 Lane Test Contract](V105_19_HARD_STABILIZATION_20260510/evidence/V105_19_LANE_TEST_CONTRACT.md)
- [V105.19 Identity Duplicate Audit](V105_19_HARD_STABILIZATION_20260510/evidence/V105_19_IDENTITY_DUPLICATE_AUDIT.md)
