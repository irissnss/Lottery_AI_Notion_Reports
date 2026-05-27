> **Public-safe report.** No private code, no DB rows, no provider keys, no raw VPS detail. Numbers shown are summary-only aggregates from V106.36 read-only audit. No official mutation occurred.



# V10636 MASTER DEBT LEDGER — V1.0 → V106.35

- ts_vn: `2026-05-27T23:08:36`
- total_issues: 20

## Severity distribution

| Severity | Count |
|---|---|
| P0 | 3 |
| P_LOCK | 2 |
| P_GUARD | 1 |
| P1 | 10 |
| P2 | 1 |
| P0_THIS_PASS_NOW_RESOLVED_BY_V10636 | 1 |
| CLOSED | 1 |
| CLOSED_NOT_VALIDATED | 1 |

## Master ledger (sorted by severity)

### `MT-CONVERSION-GATE` (P0)

- version_introduced: `V106.23`
- status: `SHADOW_ONLY_NEGATIVE_BACKTEST`
- evidence: V10623 MT gate backtest negative for 3/7/14d; V10636 MT BT 77 LOSE while strongest=56 (support=29) hit.
- impact: MT bundle picks wrong BT despite strongest candidate hitting.
- owner_gate: `True`
- action_tonight: Documented in PHASE 2 closeout: drop_stage=BUNDLE_SKEW.
- action_tomorrow: MT_CONVERSION_GATE_LANE_V1 wires conversion-gate rules in lane-test only (V10637).
- deadline: `V10637 lane-test`
- blocker: Backtest still negative; need lane-test to prove signal.
- close_condition: Lane net-effect >= 0 over 7 days with conversion gate active.

### `MB-COST-WASTE-AI-TOKEN` (P0)

- version_introduced: `V106.30 / V106.32`
- status: `COST_WASTE_CANDIDATE_OWNER_GATE`
- evidence: V10636_AI_TOKEN_BRANCH_AUDIT.md: MB AI-token 30d bt_hit_rate=0.204 contribution_to_winning=0.044; avg_latency=107s; n_models=16.
- impact: MB AI-token branch costs ~16 model calls × 107s latency per day but contributes to only ~4% of winning days.
- owner_gate: `True`
- action_tonight: V10636 marks LANE_FREEZE_CANDIDATE; no production change.
- action_tomorrow: Owner decides whether to flip MB AI-token to LANE_LIMIT or LANE_FREEZE in V10637 shadow.
- deadline: `Owner-decided (next pass)`
- blocker: Owner gate.
- close_condition: Owner OK to limit MB AI-token in lane/shadow; no production change.

### `MB-WEEKDAY-COVERAGE-GAP` (P0)

- version_introduced: `V106.36 (newly identified)`
- status: `FOUND_AND_DOCUMENTED`
- evidence: V10636_PHASE6_INTERPRETATION.md: MB TIER_A coverage only 3/7 weekdays.
- impact: MB lane-test has no signal on Tue/Wed/Thu/Sat.
- owner_gate: `False`
- action_tonight: Documented in PHASE 6.
- action_tomorrow: Re-mine MB rules on missing weekdays in V10637.
- deadline: `V10637`
- blocker: Needs MB-specific re-mining pass.
- close_condition: MB TIER_A coverage >= 1 rule per weekday.

### `GOV-V1-HARD-LOCKS` (P_LOCK)

- version_introduced: `V1.0`
- status: `ACTIVE_GOVERNANCE`
- evidence: .cursorrules; .cursor/hooks/governance_guard.py; .cursor/rules/*.mdc
- impact: Production safety — no official mutation/provider/wallet/promotion/cron/deploy without owner gate.
- owner_gate: `False`
- action_tonight: Continue to respect locks in V10636. Re-hashed pre/post in PHASE 9.
- action_tomorrow: Same locks active in V10637 mission.
- deadline: `continuous`
- blocker: None
- close_condition: Never closed; permanent guardrail.

### `FU-LIVE-ELIGIBLE-COUNT-ZERO` (P_LOCK)

- version_introduced: `V106.28 onwards`
- status: `BY_DESIGN_PRE_REGISTER_ONLY`
- evidence: V10628/V10628R0D/V10629R1/V10630 artifacts all have live_eligible_count=0.
- impact: None to official; this is the lock that protects production.
- owner_gate: `False`
- action_tonight: Verified zero in PHASE 1.
- action_tomorrow: Continue zero; owner-gated to flip.
- deadline: `permanent until owner approves promotion path`
- blocker: None.
- close_condition: When forward audit (CP-66.7) closes AND owner approves promotion gate.

### `PUBLIC-PRIVATE-DRIVE-NOTION-MISMATCH` (P_GUARD)

- version_introduced: `V106.30/V106.36 (ongoing concern)`
- status: `NO_MISMATCH_THIS_PASS`
- evidence: V10636_SSOT_POINTER_AUDIT.md: public V106.35, private V106.35, all aligned. Drive/Notion owner-managed.
- impact: None now.
- owner_gate: `False`
- action_tonight: Confirmed alignment.
- action_tomorrow: Re-check at V10637 start.
- deadline: `every pass start`
- blocker: None.
- close_condition: Per-pass SSOT pointer audit always run.

### `CP-66.7-ADAPTIVE-EXPLOIT-LIVE-VERIFY-14D` (P1)

- version_introduced: `V106.6 roadmap`
- status: `OVERDUE_AWAITING_LIVE_ROWS`
- evidence: docs/ACTIVE_ROADMAP_*.md; FU tracker; lag1_adaptive_exploit_signal_shadow table
- impact: Cannot promote adaptive-exploit lane to lane-test eligibility without 14d live verification.
- owner_gate: `False`
- action_tonight: Verify N closed live days against 14d need.
- action_tomorrow: Daily increment; recheck at 2026-06-03.
- deadline: `2026-06-03`
- blocker: Need 14 consecutive closed live days from anchor; current accumulation insufficient.
- close_condition: When 14d window closes with hits >= 25% AND false_promo <= 10%, owner-gate promotion to lane-test.

### `CP-66.8-EVIDENCE-PACK-FOR-CP66.7` (P1)

- version_introduced: `V106.6 roadmap`
- status: `LOCKED_ON_CP-66.7`
- evidence: docs/FOLLOW_UP_TRACKER.md FU-V106-22-R1 entries
- impact: Cannot deliver evidence pack until CP-66.7 closes.
- owner_gate: `False`
- action_tonight: Pre-build evidence template under `artifacts/v107_cp_66_8_evidence_pack/` (no data yet).
- action_tomorrow: Idle until CP-66.7 closes.
- deadline: `2026-06-03 (gated by CP-66.7)`
- blocker: CP-66.7 not closed.
- close_condition: Delivered when CP-66.7 verifies.

### `FU-V10622-PARALLEL-LIVE-BOARD` (P1)

- version_introduced: `V106.22`
- status: `DEPLOY_GATE_REQUIRED`
- evidence: V10622 artifacts + V10625 board deploy gate.
- impact: Board API/UI only available locally; not on VPS.
- owner_gate: `True`
- action_tonight: Reconfirmed BOARD_DEPLOY_OWNER_GATE_REQUIRED in V10636 PHASE 7.
- action_tomorrow: Continue artifact-only.
- deadline: `Owner-decided`
- blocker: OWNER_OK_DEPLOY_BOARD=false in current session.
- close_condition: Owner explicitly approves admin-only read-only deploy.

### `FU-V10628R1-NOT-RUN` (P1)

- version_introduced: `V106.28R1`
- status: `NOT_RUN_BY_DESIGN`
- evidence: All V10628R1 artifacts have v10628r1_ran=false flag.
- impact: No live rule import attempted; safety preserved.
- owner_gate: `True`
- action_tonight: Confirmed v10628r1_ran=false in PHASE 1 freeze.
- action_tomorrow: Keep not-run unless owner explicitly approves.
- deadline: `Owner-decided`
- blocker: Owner gate.
- close_condition: Owner explicit approve OR design abandons V10628R1 path.

### `MN-SELECTOR-GAP` (P1)

- version_introduced: `V106.22/V106.30`
- status: `OBSERVED_SHADOW_ONLY`
- evidence: V10636_TODAY_CLOSEOUT_MN (5/27 model same_as_official=19.2%); shadow MN_CONSENSUS_V1 BT hit
- impact: Even when MN wins, some models predict correctly but get dropped from BT pick.
- owner_gate: `False`
- action_tonight: Documented in V10636 PHASE 2.
- action_tomorrow: Add MN selector_gap_rescue path in V10637 shadow lane (no official mutation).
- deadline: `V10637 lane-test`
- blocker: None.
- close_condition: When lane shadow shows selector_gap_rescue gives positive net 7d.

### `MN-FALSE-CONSENSUS` (P1)

- version_introduced: `V106.36 (formal naming)`
- status: `OBSERVED_DAMPENER_DESIGNED`
- evidence: V10636 MN lane execution: 4 different prize_keys from same Quảng Ninh G7 family produce same 4 tails -> false consensus.
- impact: Inflates lane score without true independent evidence.
- owner_gate: `False`
- action_tonight: Designed `unique_source_evidence < 2` dampener in V10636 PHASE 6.
- action_tomorrow: Implement in V10637 lane helper.
- deadline: `V10637`
- blocker: None.
- close_condition: Dampener live in lane; 7d net-effect not worsened.

### `MT-FULL-SPENT-BOOST` (P1)

- version_introduced: `V106.23`
- status: `DOMINANCE_OBSERVED`
- evidence: V10623/V10628R0D; V10636 MT lane wrong_boosted_sum=6 today.
- impact: Boost dominance pushes wrong candidates above strongest correct candidate.
- owner_gate: `True`
- action_tonight: Captured as MT_CONVERSION_GATE dampener boost_dominance_cap in V10636 PHASE 4.
- action_tomorrow: Apply cap in V10637 lane.
- deadline: `V10637`
- blocker: None.
- close_condition: Cap reduces wrong_boosted to <= 3 per region per day in 7d window.

### `MB-NO-TOKEN-BASELINE-NOT-USABLE` (P1)

- version_introduced: `V106.30`
- status: `USABLE_PER_V10636_AUDIT`
- evidence: V10636 30d no-token MB: bt_hit_rate=0.264, contribution=0.333. BETTER than AI-token.
- impact: Should be used FIRST for MB lane-test; AI-token only as second-pass.
- owner_gate: `False`
- action_tonight: Reclassified as USABLE in V10636.
- action_tomorrow: Wire no-token baseline first in MB lane via V10637.
- deadline: `V10637`
- blocker: None.
- close_condition: MB lane no-token-first delivers >= AI-token in 7d shadow.

### `COHERE-VALUE-UNKNOWN-NOW-PROVEN-ZERO` (P1)

- version_introduced: `V106.36`
- status: `ZERO_VALUE_PROOF_30D_ALL_REGIONS`
- evidence: V10636_COHERE_VALUE_AUDIT.md: 30d MN/MT/MB all helped=0 hurt=0 no_effect dominant; bt_changed_rate 3-10%; latency 1.5-2.6s; cost_usd=0.
- impact: Cohere insertion is dead weight in current placement; no improvement.
- owner_gate: `True`
- action_tonight: Verdict COHERE_NO_EFFECT_DOMINANT_30d; no production removal without owner gate.
- action_tomorrow: Set Cohere to diagnostic_only in lane-test in V10637; no production removal.
- deadline: `V10637`
- blocker: Owner gate required for production removal.
- close_condition: Owner decision: diagnostic_only OK in lane; production removal requires explicit OK.

### `UI-API-STATIC-PROBE-INCONCLUSIVE` (P1)

- version_introduced: `V106.36 (probe-only)`
- status: `PENDING_OWNER_BROWSER_CONFIRM`
- evidence: V10636_UI_API_BOARD_AUDIT.md: /accuracy, /du-doan-test, /api/* timed out via HTTP-only probe.
- impact: Cannot conclude STALE from static probe (no JS). Owner browser smoke needed.
- owner_gate: `False`
- action_tonight: Noted owner-confirm items.
- action_tomorrow: Owner-side smoke tomorrow morning before live.
- deadline: `2026-05-28 morning`
- blocker: Owner browser session.
- close_condition: Owner confirms /du-doan, /accuracy, /api/* respond < 3s.

### `FU-71-PRE-REGISTER-RULES` (P2)

- version_introduced: `V106.26 / V106.26-2 (FU4)`
- status: `PRE_REGISTER_ONLY_PENDING_90D_FORWARD`
- evidence: 58 V10626 baseline + 13 FU4 addendum = 71.
- impact: Forward audit harness watches them; no live impact.
- owner_gate: `True`
- action_tonight: Reconfirmed in V10636 master ledger.
- action_tomorrow: Weekly forward audit snapshot starting 2026-06-01.
- deadline: `2026-08-23 (90d from 2026-05-25 anchor)`
- blocker: 90d forward audit window open.
- close_condition: Filter survivors with H2-lift >= +3pp after 2026-08-23; only then owner-gated COMMIT_ELIGIBLE_SHADOW.

### `FU-105-RULES-INDEPENDENT-QUERY` (P0_THIS_PASS_NOW_RESOLVED_BY_V10636)

- version_introduced: `V106.36`
- status: `QUERY_V2_DESIGNED_LANE_HELPERS_PLANNED`
- evidence: V10636_RULE105_INDEPENDENT_QUERY_V2.csv/json/md; V10636_RULE105_DAMPENER_PLAN; V10636_RULE105_CODE_CHANGE_PLAN.md
- impact: Region+weekday+window-aware query replaces global selector noise in lane-test only.
- owner_gate: `True`
- action_tonight: Implemented V2 query as artifact; classified all 105 rules.
- action_tomorrow: Build lane helpers `web/backend/lane/_v10636_rule105_query.py` in V10637 (lane-test only).
- deadline: `V10637 implementation`
- blocker: Owner OK to add lane helper files (no official touch).
- close_condition: Lane helpers + safety tests pass; 7-day lane-test net-effect > 0 → owner-gated next-step.

### `FU-V10614-INCOMPLETE` (CLOSED)

- version_introduced: `V106.14`
- status: `TASK_COMPLETE_OBSOLETE_BY_LATER_PASSES`
- evidence: CHANGELOG V106.15 onwards superseded V10614 partial work.
- impact: None now. V10614 partial issues subsumed by later mining/lane passes.
- owner_gate: `False`
- action_tonight: Document closure as superseded.
- action_tomorrow: No action.
- deadline: `2026-05-27 (this pass)`
- blocker: None
- close_condition: Marked superseded.

### `V10635-MB-GDB-D2-NOT-VALIDATED` (CLOSED_NOT_VALIDATED)

- version_introduced: `V106.35`
- status: `HYPOTHESIS_NOT_VALIDATED_OWNER_INFORMED`
- evidence: V10635_MB_DB_D2_DEEP_DIVE_REPORT_VN.md; V10636 TIER_GATE rejects MB self GĐB D-2.
- impact: Owner observation not actionable. V10636 respects in tier classification.
- owner_gate: `False`
- action_tonight: Reconfirmed in V10636 PHASE 5.
- action_tomorrow: Test alternative lags D-1/D-3/D-5/W-1/W-2 only if owner asks.
- deadline: `Owner-decided`
- blocker: Owner direction.
- close_condition: Owner accepts NOT_VALIDATED verdict or requests alternative lag test.
