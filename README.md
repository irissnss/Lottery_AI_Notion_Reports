# Lottery AI Notion Reports

**Latest version: V10690 PHASE 3 (T6/T7/CN forward-audit CONFIRM-only — GATE 3 GREEN 16/16)**

## Latest report for AI tools

- [**V10690_PHASE3_T6T7CN_FORWARD_AUDIT_REPORT_VN.md**](./V10667_RULES_PER_REGION_DETAILED_PUBLIC_SAFE/V10690_PHASE3_T6T7CN_FORWARD_AUDIT_REPORT_VN.md) — **NEW (Phase 3/5)**
  - 9 T6/T7/CN STRONG candidates loaded as CONFIRM-only forward-audit (drive_weight=0, never drive). Triple safety: drive_weight=0 + confirm_only filter + weekday gate.
  - GATE 3 = 16/16 PASS. Phases 1+2+3 all GREEN. Ready for Phase 4 VPS deploy (awaits owner).
  - harness 108/108, full 55/55, isolation 18/18, official zero-drift.
- [V10690_PHASE2_EXPERIMENTS_REPORT_VN.md](./V10667_RULES_PER_REGION_DETAILED_PUBLIC_SAFE/V10690_PHASE2_EXPERIMENTS_REPORT_VN.md) — Phase 2/5 (4 branches, GATE 2 GREEN)
- [V10689_PHASE1_ROLLING_REMEASURE_REPORT_VN.md](./V10667_RULES_PER_REGION_DETAILED_PUBLIC_SAFE/V10689_PHASE1_ROLLING_REMEASURE_REPORT_VN.md) — Phase 1/5 (rolling re-measure, GATE 1 GREEN)
  - 3 experiments registered + materializer for 4 branches (A full-swap, B BH-pass, C blend, CTRL). Cron 23:50 gated OFF.
  - Weekday gate verified: T6/T7/CN block MANUAL-alone-lead (A→blend, B→control).
  - GATE 2 GREEN: official 4-table zero-drift after lane write, harness 108/108, full 55/55, isolation 18/18.
- [V10689_PHASE1_ROLLING_REMEASURE_REPORT_VN.md](./V10667_RULES_PER_REGION_DETAILED_PUBLIC_SAFE/V10689_PHASE1_ROLLING_REMEASURE_REPORT_VN.md) — Phase 1/5 (rolling re-measure, GATE 1 GREEN)
  - Coded V10689 rolling re-measure of 77 MANUAL rules → drive_weight (excludes mining gap W20/W21). Cron 20:25 written but gated OFF.
  - GATE 1 GREEN: official 4-table zero-drift, MN/MT mined_rules identical, harness 108/108, full 55/55, isolation 18/18.
  - drive_weight: 55/77 rules > 0 (TANG_TRUONG 23, MANH 4); static-gold MN:DB#1:D now shows rolling decay → drive_weight 0.
  - No VPS deploy; official untouched. Next: Phase 2 experiments.
- [V10688_MASTER_CONSOLIDATION_NAMING_SWAP_LEDGER_VN.md](./V10667_RULES_PER_REGION_DETAILED_PUBLIC_SAFE/V10688_MASTER_CONSOLIDATION_NAMING_SWAP_LEDGER_VN.md) — single source of truth (naming/swap/ledger)
  - NAMING final: PRODUCTION (35, drives) / MANUAL (77, confirm) / PREREG (cancelled). Names follow source, not role.
  - SWAP clarity: "đảo T2↔T1" = a ROLE swap (who drives the score), tested in `/du-doan-test` via 3 experiments — NOT a rename, never on official.
  - VERSION-FIX: V10684 collision resolved — rolling re-measure = V10689, experiments = V10690.
  - Full decisions ledger (V10679→V10688), pending-items list, verification status, and a hard GATE: no further code/dig until owner confirms T6/T7/CN (A/B/C) + naming/swap + version-fix.
- [V10687_DIG_T6T7CN_STRONG_CANDIDATES_VN.md](./V10667_RULES_PER_REGION_DETAILED_PUBLIC_SAFE/V10687_DIG_T6T7CN_STRONG_CANDIDATES_VN.md)
  - Owner asked to dig gold (BH-pass) rules for MB weekdays T6/T7/CN (had 0 BH-pass).
  - Honest result: NO gold exists even after expanded dig (~322 samples/cell over ~6 years). Modest effect size (+5 to +11pp) vs strict FDR; strongest T6 MN:G1#1:FIRST2:D-4 (+10.9pp, p=4.9e-5) just barely fails focused-BH.
  - STRONG (p<.01) candidates listed for 90d forward-audit (NOT gold, selection-bias flagged). Owner to choose A=forward-audit / B=MANUAL CONFIRM-only / C=skip.
  - Also confirmed PRE-REGISTER (old T3) fully purged.
- [V10686_TECHNICAL_DESIGN_V10684_V10683_VN.md](./V10667_RULES_PER_REGION_DETAILED_PUBLIC_SAFE/V10686_TECHNICAL_DESIGN_V10684_V10683_VN.md)
  - Owner confirmed 3 decisions: D (all 3 shadow experiments), V10684 rolling re-measure pre-req 1 week before, 30d PASS/FAIL thresholds OK.
  - Technical design: `mb_manual_rolling_eval` schema, function signatures for V10684 + V10683 (3 chooser), cron 20:25 + 23:50, hard contract, verify checklist, risk matrix, rollback paths.
  - Code NOT written yet. Awaiting owner explicit "code đi" to begin V10684 local build.
- [V10685_NAMING_CONSISTENCY_PROD_MANUAL_VN.md](./V10667_RULES_PER_REGION_DETAILED_PUBLIC_SAFE/V10685_NAMING_CONSISTENCY_PROD_MANUAL_VN.md)
  - Owner caught: if MANUAL drives in shadow lane but is still called "T2", code/docs conflate ID with role.
  - Rename T1/T2/T3 → PRODUCTION/MANUAL/PREREG before any V10683 code is written. IDs now follow source; drive/confirm role lives in description/log.
  - 55/55 full verify PASS, 18/18 isolation matrix PASS, MN/MT 108/108 IDENTICAL.
- [V10684_ISOLATION_MATRIX_AND_FULL_BACKUP_VN.md](./V10667_RULES_PER_REGION_DETAILED_PUBLIC_SAFE/V10684_ISOLATION_MATRIX_AND_FULL_BACKUP_VN.md)
  - Owner-asked: ensure MN/MT isolation in BOTH official and `/du-doan-test`, plus full backup before any code work begins.
  - Result: 18/18 PASS isolation matrix (static + runtime + DB hash). Multi-region lane-test engines have ZERO MB-only symbol leaks. 4 official tables hash zero-drift. Frozen-DB harness 108/108 IDENTICAL.
  - Backup: 5 MB-edited code files .v10684.pre + 11 official-critical references + 22 in-DB snapshot tables _bak_v10684_* + 4 baseline hashes + MANIFEST.json with restore instructions.
- [V10683_MB_T2_DRIVE_SHADOW_LANE_PLAN_VN.md](./V10667_RULES_PER_REGION_DETAILED_PUBLIC_SAFE/V10683_MB_T2_DRIVE_SHADOW_LANE_PLAN_VN.md)
  - Owner correction: production already drives T1; owner asked to swap T1↔T2 INSIDE `/du-doan-test`, not on official.
  - Lane test currently has 10 MB experiments registered + 7 active, all picking from T1-scored pool — none recompute via T2.
  - Plan: add `MB_T2_MANUAL_DRIVE_SHADOW_V1` (+ optionally BH-pass-only and blend variants), pre-requisite V10684 rolling re-measure for the 73 manual T2 rules.
  - Hard contract preserved (no mined_rules / final_bundles / predictions touched). PLAN-ONLY, awaiting owner choice.
- [V10682_T1_VS_T2_SWAP_ANALYSIS_VN.md](./V10667_RULES_PER_REGION_DETAILED_PUBLIC_SAFE/V10682_T1_VS_T2_SWAP_ANALYSIS_VN.md)
  - Empirical analysis: T1∩T2 = 0 axes overlap; T2 measured once; T6/T7/CN have zero BH-pass.
  - Verdict for OFFICIAL: do not fully swap. Confirms why test-lane swap (V10683) is the right place to try.
- [V10681_DROP_TIER3_T1_T2_CROSS_VERIFY_VN.md](./V10667_RULES_PER_REGION_DETAILED_PUBLIC_SAFE/V10681_DROP_TIER3_T1_T2_CROSS_VERIFY_VN.md)
  - Owner-decision: drop Tier-3 (V10626 pre-register, 19 MB rules) — they all fail BH_FDR, lack `target_weekday`, contain duplicates, and have no rolling re-measure.
  - 2-tier weekday-bound cross-verify = T1 (35 production, drives score) + T2 (77 manual MB-target, CONFIRM-only).
  - Verify 54/54 PASS, MN/MT invariance 108/108 IDENTICAL, no VPS deploy.
- [V10680_MB_RULE_STACK_CLARIFICATION_AND_NEXT_STEPS_VN.md](./V10667_RULES_PER_REGION_DETAILED_PUBLIC_SAFE/V10680_MB_RULE_STACK_CLARIFICATION_AND_NEXT_STEPS_VN.md) — preceding clarification (T3 sections superseded by V10681; T1/T2/gates/test-lane sections still valid).

## ⚠️ Read first (4 critical notes)

1. [**🎯 V10670_SOURCE_SEMANTICS_LEGEND.md**](./V10667_RULES_PER_REGION_DETAILED_PUBLIC_SAFE/V10670_SOURCE_SEMANTICS_LEGEND.md) — **NEW**: how source notation works. `#Bộ` = position-in-prize NOT station. Multi-station source = UNION of all stations that weekday. Full station-by-weekday map (MB is per-province: T2=Hà Nội, T3=Quảng Ninh, T4=Bắc Ninh, T5=Hà Nội, T6=Hải Phòng, T7=Nam Định, CN=Thái Bình).
2. [**✅ V10669_TEMPORAL_VERIFICATION_REPORT_VN.md**](./V10667_RULES_PER_REGION_DETAILED_PUBLIC_SAFE/V10669_TEMPORAL_VERIFICATION_REPORT_VN.md) — comprehensive verification: OVERALL CLEAN=True. 232 BH-pass valid + 28 forward audit rules.
3. [**🕐 V10668_TEMPORAL_CAUSALITY_PATCH_NOTICE.md**](./V10667_RULES_PER_REGION_DETAILED_PUBLIC_SAFE/V10668_TEMPORAL_CAUSALITY_PATCH_NOTICE.md) — draw order MN(16:10)→MT(17:10)→MB(18:15); same-day source-after-target removed.
4. [**📖 V10667_BO_NUMBERING_LEGEND.md**](./V10667_RULES_PER_REGION_DETAILED_PUBLIC_SAFE/V10667_BO_NUMBERING_LEGEND.md) — `Giải X bộ Y` notation. G.4 MB (4 bộ): `Bộ 1=top-left, Bộ 2=top-right, Bộ 3=bottom-left, Bộ 4=bottom-right`.

## Quick navigation — per region rule docs

| Target | Detailed rules document |
|---|---|
| **Miền Bắc (MB)** | [V10667_RULES_MB_TARGET.md](./V10667_RULES_PER_REGION_DETAILED_PUBLIC_SAFE/V10667_RULES_MB_TARGET.md) |
| **Miền Nam (MN)** | [V10667_RULES_MN_TARGET.md](./V10667_RULES_PER_REGION_DETAILED_PUBLIC_SAFE/V10667_RULES_MN_TARGET.md) |
| **Miền Trung (MT)** | [V10667_RULES_MT_TARGET.md](./V10667_RULES_PER_REGION_DETAILED_PUBLIC_SAFE/V10667_RULES_MT_TARGET.md) |
| **Index hub** | [V10667_RULES_INDEX.md](./V10667_RULES_PER_REGION_DETAILED_PUBLIC_SAFE/V10667_RULES_INDEX.md) |

## Tài liệu chứa gì

Mỗi tài liệu MB/MN/MT có:
- 7 sections (T2 → CN)
- Mỗi section: top 8-12 rule mạnh nhất
- Mỗi rule có:
  - Mô tả tiếng Việt cách áp dụng
  - Bảng per-station (đài nào hit nhiều nhất)
  - 3 ngày gần nhất rule trúng (worked examples)
  - p-value, BH-pass, strength classification

## Methodology

- V10636 series audit: 3,696 unique rule combinations tested
- **268 BH-pass cells** (gold standard, FDR α=0.05)
- 357 cells với lift ≥ +5pp
- 35 best rules registered into 90-day forward audit (anchor 2026-06-02 → closeout 2026-08-31)

## Owner constraints applied

- MN/MT G3 = source only (không làm target)
- MB source whitelist: DB, G1, G2, G4, G6, G7

## Status

All rules: `PRE_REGISTER_FORWARD_AUDIT`, `live_eligible=False`.
No official mutation. Read-only research.

For previous versions, see `REPORT_INDEX.md`.
