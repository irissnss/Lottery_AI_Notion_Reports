> **Public-safe report.** No private code, no DB rows, no provider keys, no raw VPS detail. Numbers shown are summary-only aggregates from V106.36 read-only audit. No official mutation occurred.



# V10636 P0/P1 ACTION BOARD

- ts_vn: `2026-05-27T23:08:36`

| Severity | Issue | Action tonight | Action tomorrow | Deadline | Owner gate |
|---|---|---|---|---|---|
| P0 | `MT-CONVERSION-GATE` | Documented in PHASE 2 closeout: drop_stage=BUNDLE_SKEW. | MT_CONVERSION_GATE_LANE_V1 wires conversion-gate rules in lane-test only (V10637). | V10637 lane-test | True |
| P0 | `MB-COST-WASTE-AI-TOKEN` | V10636 marks LANE_FREEZE_CANDIDATE; no production change. | Owner decides whether to flip MB AI-token to LANE_LIMIT or LANE_FREEZE in V10637 shadow. | Owner-decided (next pass) | True |
| P0 | `MB-WEEKDAY-COVERAGE-GAP` | Documented in PHASE 6. | Re-mine MB rules on missing weekdays in V10637. | V10637 | False |
| P1 | `CP-66.7-ADAPTIVE-EXPLOIT-LIVE-VERIFY-14D` | Verify N closed live days against 14d need. | Daily increment; recheck at 2026-06-03. | 2026-06-03 | False |
| P1 | `CP-66.8-EVIDENCE-PACK-FOR-CP66.7` | Pre-build evidence template under `artifacts/v107_cp_66_8_evidence_pack/` (no data yet). | Idle until CP-66.7 closes. | 2026-06-03 (gated by CP-66.7) | False |
| P1 | `FU-V10622-PARALLEL-LIVE-BOARD` | Reconfirmed BOARD_DEPLOY_OWNER_GATE_REQUIRED in V10636 PHASE 7. | Continue artifact-only. | Owner-decided | True |
| P1 | `FU-V10628R1-NOT-RUN` | Confirmed v10628r1_ran=false in PHASE 1 freeze. | Keep not-run unless owner explicitly approves. | Owner-decided | True |
| P1 | `MN-SELECTOR-GAP` | Documented in V10636 PHASE 2. | Add MN selector_gap_rescue path in V10637 shadow lane (no official mutation). | V10637 lane-test | False |
| P1 | `MN-FALSE-CONSENSUS` | Designed `unique_source_evidence < 2` dampener in V10636 PHASE 6. | Implement in V10637 lane helper. | V10637 | False |
| P1 | `MT-FULL-SPENT-BOOST` | Captured as MT_CONVERSION_GATE dampener boost_dominance_cap in V10636 PHASE 4. | Apply cap in V10637 lane. | V10637 | True |
| P1 | `MB-NO-TOKEN-BASELINE-NOT-USABLE` | Reclassified as USABLE in V10636. | Wire no-token baseline first in MB lane via V10637. | V10637 | False |
| P1 | `COHERE-VALUE-UNKNOWN-NOW-PROVEN-ZERO` | Verdict COHERE_NO_EFFECT_DOMINANT_30d; no production removal without owner gate. | Set Cohere to diagnostic_only in lane-test in V10637; no production removal. | V10637 | True |
| P1 | `UI-API-STATIC-PROBE-INCONCLUSIVE` | Noted owner-confirm items. | Owner-side smoke tomorrow morning before live. | 2026-05-28 morning | False |
| P0_THIS_PASS_NOW_RESOLVED_BY_V10636 | `FU-105-RULES-INDEPENDENT-QUERY` | Implemented V2 query as artifact; classified all 105 rules. | Build lane helpers `web/backend/lane/_v10636_rule105_query.py` in V10637 (lane-test only). | V10637 implementation | True |