# V91 — Actionable evidence matrix

Generated 2026-05-08T01:19:20+07:00

Items with enough evidence to act on (CLOSE / DOSSIER_PREP / DROP / WAIT).

| Item | Evidence | Verdict | Action |
| --- | --- | --- | --- |
| strongest_to_final_preservation_v1 | 11/11 hits MN/MT/MB; 9 win_flips MB; 0 lose_flips total; 0 false_promotion | POTENTIAL_LIFT | DOSSIER_PREP (test-lane voter); next_check 2026-05-21 |
| counterfactual_decision_audit_v1 | MN 56% lift; 80 total; 16 lose_flip MT (concerning) | POTENTIAL_LIFT_BUT_MT_RISK | KEEP_DIAGNOSTIC; MT-no-break test required at 14d |
| rule_phase_evidence_v1 | MT 73 hit / 212 = 34%; 103 lose_flips; 139 false_promotion | DESTRUCTIVE_BIAS | DROP_FROM_PROMOTION; KEEP_DIAGNOSTIC only |
| rule_injection_contract_shadow_v1 | MT 30 sample / 16 lose_flips / 21 fp | DESTRUCTIVE_BIAS | DROP_FROM_PROMOTION; KEEP_DIAGNOSTIC only |
| no_token_drift_guard_v1 | MB 77 sample / 14 lose_flips / 47 fp | DESTRUCTIVE_BIAS_MB | DROP_FROM_PROMOTION; signal-only |
| MN_SPECIALIST_ROSTER_V1 | 60d n=60 hit 51.7% save 4 break 0 (clean) | PROMOTION_CANDIDATE_TEST_LANE | DOSSIER_PREP for 2026-05-21 |
| MN_AI_CHAIN_PRESERVATION_V1 | 60d n=59 hit 52.5% save 5 break 1 | PROMOTION_CANDIDATE_TEST_LANE | DOSSIER_PREP for 2026-05-21 |
| MT_AI_CHAIN_PRESERVATION_V1 | 60d n=60 hit 41.7% break 12 | DESTRUCTIVE_BIAS_PROVEN_60D | DROP_FROM_PROMOTION_MT; CLOSE_DECISION |
| MT_PRIOR_REGION_CONTEXT_SAFE_V1 | 60d n=60 hit 41.7% break 9 | DESTRUCTIVE_BIAS_PROVEN_60D | DROP_FROM_PROMOTION_MT; CLOSE_DECISION |
| MB_SPECIALIST_ROSTER_V1 | n=41 hit 36.6% save 5 break 0 (limited sample) | PROMISING_LIMITED_SAMPLE | WAIT_60D (target 2026-07-06) |
| Wave 1 control surfaces (9 tables) | LIVE since 2026-04-25 (12+ days) | LIVE_PROVEN | CLOSED — continuous |
| Wave 2 (PP-1 + verdict_dist + prompt_section) | LIVE_PROVEN | LIVE_PROVEN | CLOSED — continuous |
| D-1 RULE_MECHANISM audit | Subsumed by P0 portfolio rule_phase_evidence_v1 | DOC_COMPLETE_SUBSUMED | CLOSED |
| D-2 OVERREACH_ROLLBACK audit | Doc complete; principle still active | DOC_COMPLETE | CLOSED — principle continuous |
| D-7 (ambiguous label) | Resolved as 7d gate concept in decision_calendar | AMBIGUOUS_RESOLVED | CLOSED — concept embedded in calendar |
| P0 portfolio 18 methods | 14/18 READY_TO_EVALUATE; 4 wait 5d to 2026-05-12 | PARTIAL_READY | WAIT_2026_05_12 then re-run maturity matrix |
| V79 cluster_weighted + cross_verify | 4d only; MT 1/4 vs OFF 3/4 + 2 breaks | INSUFFICIENT_SAMPLE | WAIT_14D (2026-05-21) |
| V81 provider shadow pilot | 2d / 18 calls / 0 break / 1 save MN per model | INSUFFICIENT_SAMPLE | WAIT_7D (2026-05-14) then 14D (2026-05-21) |
| V82 60D evidence audit | 307 audit cells delivered | DELIVERED | CLOSED |
| V83 V82 monitor UI | /v82-monitor + /api/admin/v82-monitor admin-only | DEPLOYED | CLOSED — also embedded in /monitoring (V86) |
| V84-V90 inventory chain | 1378 items reconciled; 29 tabs | DELIVERED | CLOSED |
