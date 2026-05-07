# V84 — 18-method P0 portfolio status (14d evidence + 60d coverage)

Generated: 2026-05-07T23:33:33+07:00

Note: portfolio originally 17 methods, expanded to 18 with `cohere_rerank_effectiveness_v1` (V20.3.37.24).

| ID | Method | Group | Min days | Min N | Days observed | Rows 60d | First | Last | Maturity | n 14d | Win flip | Lose flip | FP | Net | Verdict |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | freshness_readiness_guard_v1 | cross_system | 0 | 0 | 8 | 24 | 2026-04-30 | 2026-05-07 | 7D_SAMPLE | 24 | 0 | 0 | 0 | 0 | INSUFFICIENT_SAMPLE |
| 2 | strongest_to_final_preservation_v1 | cross_system | 3 | 3 | 11 | 33 | 2026-04-27 | 2026-05-07 | 7D_SAMPLE | 33 | 19 | 0 | 0 | 19 | POTENTIAL_LIFT |
| 3 | no_token_drift_guard_v1 | no_token | 3 | 3 | 11 | 162 | 2026-04-27 | 2026-05-07 | 7D_SAMPLE | 162 | 16 | 33 | 71 | -17 | DESTRUCTIVE_BIAS |
| 4 | rule_phase_evidence_v1 | cross_system | 3 | 3 | 11 | 590 | 2026-04-27 | 2026-05-07 | 7D_SAMPLE | 590 | 91 | 176 | 387 | -85 | DESTRUCTIVE_BIAS |
| 5 | meta_ranker_v1 | cross_system | 5 | 9 | 11 | 99 | 2026-04-27 | 2026-05-07 | 7D_SAMPLE | 99 | 15 | 16 | 41 | -1 | PARITY |
| 6 | output_policy_replay_governance_v1 | cross_system | 3 | 3 | 11 | 231 | 2026-04-27 | 2026-05-07 | 7D_SAMPLE | 231 | 7 | 1 | 25 | 6 | PARITY |
| 7 | counterfactual_decision_audit_v1 | cross_system | 3 | 3 | 8 | 239 | 2026-04-30 | 2026-05-07 | 7D_SAMPLE | 239 | 47 | 27 | 89 | 20 | POTENTIAL_LIFT |
| 44 | runtime_final_baseline_control_v1 | baseline | 0 | 0 | 9 | 27 | 2026-04-29 | 2026-05-07 | 7D_SAMPLE | 27 | 0 | 0 | 0 | 0 | INSUFFICIENT_SAMPLE |
| 51 | phase_first_decision_shadow_v1 | phase_first | 3 | 9 | 9 | 81 | 2026-04-29 | 2026-05-07 | 7D_SAMPLE | 81 | 14 | 11 | 30 | 3 | PARITY |
| 52 | anti_herding_shadow_v1 | cross_system | 3 | 9 | 9 | 81 | 2026-04-29 | 2026-05-07 | 7D_SAMPLE | 81 | 13 | 11 | 31 | 2 | PARITY |
| 53 | rule_injection_contract_shadow_v1 | rules | 3 | 9 | 10 | 90 | 2026-04-28 | 2026-05-07 | 7D_SAMPLE | 90 | 11 | 21 | 56 | -10 | DESTRUCTIVE_BIAS |
| 54 | model_wisdom_scorecard_shadow_v1 | model_wisdom | 3 | 9 | 9 | 694 | 2026-04-29 | 2026-05-07 | 7D_SAMPLE | 694 | 97 | 124 | 360 | -27 | PARITY |
| 55 | meta_ranker_ltr_dataset_shadow_v1 | meta_ranker_dataset | 14 | 42 | 9 | 81 | 2026-04-29 | 2026-05-07 | 7D_SAMPLE | 81 | 14 | 11 | 30 | 3 | PARITY |
| 56 | rule_aware_adaptive_notoken_shadow_v1 | no_token | 5 | 15 | 9 | 81 | 2026-04-29 | 2026-05-07 | 7D_SAMPLE | 81 | 10 | 10 | 33 | 0 | PARITY |
| 57 | context_specialist_policy_shadow_v1 | context_policy | 14 | 30 | 9 | 81 | 2026-04-29 | 2026-05-07 | 7D_SAMPLE | 81 | 14 | 11 | 30 | 3 | PARITY |
| 58 | online_bayesian_weighting_shadow_v1 | adaptive_weighting | 14 | 30 | 9 | 81 | 2026-04-29 | 2026-05-07 | 7D_SAMPLE | 81 | 10 | 14 | 36 | -4 | DESTRUCTIVE_BIAS |
| 59 | phase_aware_rerank_shadow_v1 | phase_first | 5 | 15 | 9 | 81 | 2026-04-29 | 2026-05-07 | 7D_SAMPLE | 81 | 14 | 11 | 30 | 3 | PARITY |
| 203 | cohere_rerank_effectiveness_v1 | rerank | 3 | 3 | 8 | 23 | 2026-04-30 | 2026-05-07 | 7D_SAMPLE | 23 | 3 | 3 | 11 | 0 | INSUFFICIENT_SAMPLE |
