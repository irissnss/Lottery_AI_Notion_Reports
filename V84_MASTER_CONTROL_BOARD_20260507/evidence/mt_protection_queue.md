# MT protection queue

## 18-method P0 portfolio 14d (shadow_results region split)

| Method | n | Hit | Rate | Win flip | Lose flip | FP | Net | Verdict |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| strongest_to_final_preservation_v1 | 11 | 11 | 1.0 | 3 | 0 | 0 | 3 | INSUFFICIENT |
| freshness_readiness_guard_v1 | 8 | 6 | 0.75 | 0 | 0 | 0 | 0 | INSUFFICIENT |
| output_policy_replay_governance_v1 | 77 | 56 | 0.727 | 0 | 0 | 3 | 0 | PARITY |
| runtime_final_baseline_control_v1 | 9 | 7 | 0.778 | 0 | 0 | 0 | 0 | INSUFFICIENT |
| cohere_rerank_effectiveness_v1 | 8 | 5 | 0.625 | 0 | 1 | 2 | -1 | INSUFFICIENT |
| rule_aware_adaptive_notoken_shadow_v1 | 27 | 16 | 0.593 | 0 | 5 | 6 | -5 | DESTRUCTIVE_REGION |
| phase_first_decision_shadow_v1 | 27 | 15 | 0.556 | 2 | 8 | 10 | -6 | DESTRUCTIVE_REGION |
| anti_herding_shadow_v1 | 27 | 15 | 0.556 | 2 | 8 | 10 | -6 | DESTRUCTIVE_REGION |
| meta_ranker_ltr_dataset_shadow_v1 | 27 | 15 | 0.556 | 2 | 8 | 10 | -6 | DESTRUCTIVE_REGION |
| context_specialist_policy_shadow_v1 | 27 | 15 | 0.556 | 2 | 8 | 10 | -6 | DESTRUCTIVE_REGION |
| phase_aware_rerank_shadow_v1 | 27 | 15 | 0.556 | 2 | 8 | 10 | -6 | DESTRUCTIVE_REGION |
| meta_ranker_v1 | 33 | 17 | 0.515 | 3 | 10 | 14 | -7 | DESTRUCTIVE_REGION |
| counterfactual_decision_audit_v1 | 80 | 52 | 0.65 | 8 | 16 | 23 | -8 | DESTRUCTIVE_REGION |
| online_bayesian_weighting_shadow_v1 | 27 | 13 | 0.481 | 2 | 10 | 12 | -8 | DESTRUCTIVE_REGION |
| no_token_drift_guard_v1 | 77 | 42 | 0.545 | 5 | 19 | 24 | -14 | DESTRUCTIVE_REGION |
| rule_injection_contract_shadow_v1 | 30 | 9 | 0.3 | 1 | 16 | 21 | -15 | DESTRUCTIVE_REGION |
| model_wisdom_scorecard_shadow_v1 | 228 | 99 | 0.434 | 11 | 90 | 118 | -79 | DESTRUCTIVE_REGION |
| rule_phase_evidence_v1 | 212 | 73 | 0.344 | 15 | 103 | 139 | -88 | DESTRUCTIVE_REGION |

## V82 60d evidence (cached)

- OFFICIAL 50.0% (n=60) — strongest baseline in entire system.
- AI_HERD 43.3% (n=60) save=8 break=12 — DESTRUCTIVE -6.7pp.
- MT_AI_CHAIN_PRESERVATION 41.7% break=12 — DO_NOT_PROMOTE.
- MT_PRIOR_REGION_CONTEXT_SAFE 41.7% break=9 — DO_NOT_PROMOTE.
- NO_TOKEN_HERD 51.7% (parity within Wilson).

## 18-method portfolio 14d MT destructive flags

- rule_phase_evidence_v1 MT: 73 hit / 212 = 34%, 103 lose_flip, 139 fp → DESTRUCTIVE bias.
- model_wisdom_scorecard_shadow_v1 MT: 99/228 = 43.4%, 90 lose_flip, 118 fp → DESTRUCTIVE bias.
- rule_injection_contract_shadow_v1 MT: 9/30 = 30%, 16 lose_flip, 21 fp → DESTRUCTIVE bias.
- counterfactual_decision_audit_v1 MT: 52/80 = 65%, 16 lose_flip, 23 fp → MARGINAL.
- output_policy_replay_governance_v1 MT: 56/77 = 72.7%, 0 lose_flip, 3 fp → BENEFICIAL_CLEAN.

## Pass conditions for MT (protection)

- Any new method going live for MT must have lose_flip < win_flip / 2 over 14d sample.
- Any consensus/cluster proposal must include explicit MT no-break test.

## Hard locks for MT

- KHÔNG remove OFFICIAL/V70 consensus-first.
- KHÔNG promote AI_HERD, AI_CHAIN_PRESERVATION, PRIOR_REGION_CONTEXT, rule_phase_evidence, model_wisdom_scorecard, rule_injection_contract for MT.
- output_policy_replay_governance_v1 may be re-evaluated at 30d gate (looks promising MT).
