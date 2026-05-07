# V84 method maturity matrix (P0 portfolio)

| Method | Min days | Min N | Days obs | N obs | Min days met? | Min N met? | Maturity | 14d verdict | Next gate |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| freshness_readiness_guard_v1 | 0 | 0 | 8 | 24 | YES | YES | 7D_SAMPLE | INSUFFICIENT_SAMPLE | READY_TO_EVALUATE |
| strongest_to_final_preservation_v1 | 3 | 3 | 11 | 33 | YES | YES | 7D_SAMPLE | POTENTIAL_LIFT | READY_TO_EVALUATE |
| no_token_drift_guard_v1 | 3 | 3 | 11 | 162 | YES | YES | 7D_SAMPLE | DESTRUCTIVE_BIAS | READY_TO_EVALUATE |
| rule_phase_evidence_v1 | 3 | 3 | 11 | 590 | YES | YES | 7D_SAMPLE | DESTRUCTIVE_BIAS | READY_TO_EVALUATE |
| meta_ranker_v1 | 5 | 9 | 11 | 99 | YES | YES | 7D_SAMPLE | PARITY | READY_TO_EVALUATE |
| output_policy_replay_governance_v1 | 3 | 3 | 11 | 231 | YES | YES | 7D_SAMPLE | PARITY | READY_TO_EVALUATE |
| counterfactual_decision_audit_v1 | 3 | 3 | 8 | 239 | YES | YES | 7D_SAMPLE | POTENTIAL_LIFT | READY_TO_EVALUATE |
| runtime_final_baseline_control_v1 | 0 | 0 | 9 | 27 | YES | YES | 7D_SAMPLE | INSUFFICIENT_SAMPLE | READY_TO_EVALUATE |
| phase_first_decision_shadow_v1 | 3 | 9 | 9 | 81 | YES | YES | 7D_SAMPLE | PARITY | READY_TO_EVALUATE |
| anti_herding_shadow_v1 | 3 | 9 | 9 | 81 | YES | YES | 7D_SAMPLE | PARITY | READY_TO_EVALUATE |
| rule_injection_contract_shadow_v1 | 3 | 9 | 10 | 90 | YES | YES | 7D_SAMPLE | DESTRUCTIVE_BIAS | READY_TO_EVALUATE |
| model_wisdom_scorecard_shadow_v1 | 3 | 9 | 9 | 694 | YES | YES | 7D_SAMPLE | PARITY | READY_TO_EVALUATE |
| meta_ranker_ltr_dataset_shadow_v1 | 14 | 42 | 9 | 81 | NO | YES | 7D_SAMPLE | PARITY | WAIT (need 5d more days, 0 more samples) |
| rule_aware_adaptive_notoken_shadow_v1 | 5 | 15 | 9 | 81 | YES | YES | 7D_SAMPLE | PARITY | READY_TO_EVALUATE |
| context_specialist_policy_shadow_v1 | 14 | 30 | 9 | 81 | NO | YES | 7D_SAMPLE | PARITY | WAIT (need 5d more days, 0 more samples) |
| online_bayesian_weighting_shadow_v1 | 14 | 30 | 9 | 81 | NO | YES | 7D_SAMPLE | DESTRUCTIVE_BIAS | WAIT (need 5d more days, 0 more samples) |
| phase_aware_rerank_shadow_v1 | 5 | 15 | 9 | 81 | YES | YES | 7D_SAMPLE | PARITY | READY_TO_EVALUATE |
| cohere_rerank_effectiveness_v1 | 3 | 3 | 8 | 23 | YES | YES | 7D_SAMPLE | INSUFFICIENT_SAMPLE | READY_TO_EVALUATE |
