# MN master recovery queue

## 18-method P0 portfolio 14d (shadow_results region split)

| Method | n | Hit | Rate | Win flip | Lose flip | FP | Net | Verdict |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| model_wisdom_scorecard_shadow_v1 | 233 | 108 | 0.464 | 47 | 14 | 85 | 33 | BENEFICIAL_REGION |
| rule_phase_evidence_v1 | 219 | 93 | 0.425 | 60 | 43 | 115 | 17 | PARITY |
| counterfactual_decision_audit_v1 | 79 | 44 | 0.557 | 16 | 2 | 12 | 14 | BENEFICIAL_REGION |
| strongest_to_final_preservation_v1 | 11 | 11 | 1.0 | 7 | 0 | 0 | 7 | INSUFFICIENT |
| phase_first_decision_shadow_v1 | 27 | 14 | 0.519 | 6 | 1 | 7 | 5 | BENEFICIAL_REGION |
| anti_herding_shadow_v1 | 27 | 14 | 0.519 | 6 | 1 | 7 | 5 | BENEFICIAL_REGION |
| meta_ranker_ltr_dataset_shadow_v1 | 27 | 14 | 0.519 | 6 | 1 | 7 | 5 | BENEFICIAL_REGION |
| context_specialist_policy_shadow_v1 | 27 | 14 | 0.519 | 6 | 1 | 7 | 5 | BENEFICIAL_REGION |
| phase_aware_rerank_shadow_v1 | 27 | 14 | 0.519 | 6 | 1 | 7 | 5 | BENEFICIAL_REGION |
| meta_ranker_v1 | 33 | 16 | 0.485 | 6 | 2 | 10 | 4 | BENEFICIAL_REGION |
| rule_aware_adaptive_notoken_shadow_v1 | 27 | 13 | 0.481 | 7 | 3 | 11 | 4 | BENEFICIAL_REGION |
| output_policy_replay_governance_v1 | 77 | 31 | 0.403 | 3 | 0 | 6 | 3 | BENEFICIAL_REGION |
| online_bayesian_weighting_shadow_v1 | 27 | 12 | 0.444 | 5 | 2 | 9 | 3 | BENEFICIAL_REGION |
| rule_injection_contract_shadow_v1 | 30 | 11 | 0.367 | 4 | 2 | 13 | 2 | PARITY |
| cohere_rerank_effectiveness_v1 | 7 | 4 | 0.571 | 2 | 1 | 2 | 1 | INSUFFICIENT |
| freshness_readiness_guard_v1 | 8 | 3 | 0.375 | 0 | 0 | 0 | 0 | INSUFFICIENT |
| no_token_drift_guard_v1 | 8 | 3 | 0.375 | 0 | 0 | 0 | 0 | INSUFFICIENT |
| runtime_final_baseline_control_v1 | 9 | 3 | 0.333 | 0 | 0 | 0 | 0 | INSUFFICIENT |

## V82 60d evidence (cached)

- OFFICIAL 45.0% (n=60).
- MN_AI_CHAIN_PRESERVATION_V1 52.5% (n=59) save=5 break=1 → PROMOTION_CANDIDATE_AFTER_DOSSIER (test-lane voter only).
- MN_SPECIALIST_ROSTER_V1 51.7% (n=60) save=4 break=0 → PROMOTION_CANDIDATE_CLEAN (test-lane voter only).
- NO_TOKEN_HERD 51.7% save=14 break=10 → REGION_SPECIFIC.
- AI_HERD 48.3% save=6 break=4 → PARITY+.
- V67/V73 trùng 95 vs OFFICIAL 94 trên 2026-05-07 — first save signal under stress.

## V79 cluster + V81 pilot

- V79 cluster_weighted_tail MN 2/4 hits + 2 saves + 0 breaks (n=4 only, INSUFFICIENT).
- V81 provider pilot MN 3/6 across 3 models, each model 1 save, 0 breaks, all converged on V67/V73 tail 95 — prompt-first signal valid for MN.

## Pass conditions for MN test-lane voter promotion proposal

1. After 14d (2026-05-21): MN_SPECIALIST_ROSTER + MN_AI_CHAIN_PRESERVATION sustain hit ≥ OFFICIAL + win_flip > lose_flip.
2. After 14d: V81 provider pilot MN 14d would_save > would_break per model.
3. After 14d: MT no_break test passes (MT consensus untouched).
4. Owner OK required.

## Fail conditions

- MN candidates lose lift (<OFFICIAL hit).
- Any candidate breaks MT.
- False_promotion > would_save x 1.5.

## Hard locks for MN

- KHÔNG promote candidate vào official trước 30d.
- Test-lane voter level cũng cần dossier + owner OK.
