# 8/8 — ALL SHADOW METHODS / SELECTORS

## 8a. P0 portfolio (18 methods)

| # | Method key | Group | State | Min days | Min N |
| --- | --- | --- | --- | --- | --- |
| 1 | freshness_readiness_guard_v1 | cross_system | SHADOW_AUTO |  |  |
| 2 | strongest_to_final_preservation_v1 | cross_system | SHADOW_AUTO | 3 | 3 |
| 3 | no_token_drift_guard_v1 | no_token | SHADOW_AUTO | 3 | 3 |
| 4 | rule_phase_evidence_v1 | cross_system | SHADOW_AUTO | 3 | 3 |
| 5 | meta_ranker_v1 | cross_system | SHADOW_AUTO | 5 | 9 |
| 6 | output_policy_replay_governance_v1 | cross_system | SHADOW_AUTO | 3 | 3 |
| 7 | counterfactual_decision_audit_v1 | cross_system | SHADOW_AUTO | 3 | 3 |
| 8 | runtime_final_baseline_control_v1 | baseline | SHADOW_AUTO |  |  |
| 9 | phase_first_decision_shadow_v1 | phase_first | SHADOW_AUTO | 3 | 9 |
| 10 | anti_herding_shadow_v1 | cross_system | SHADOW_AUTO | 3 | 9 |
| 11 | rule_injection_contract_shadow_v1 | rules | SHADOW_AUTO | 3 | 9 |
| 12 | model_wisdom_scorecard_shadow_v1 | model_wisdom | SHADOW_AUTO | 3 | 9 |
| 13 | meta_ranker_ltr_dataset_shadow_v1 | meta_ranker_dataset | SHADOW_AUTO | 14 | 42 |
| 14 | rule_aware_adaptive_notoken_shadow_v1 | no_token | SHADOW_AUTO | 5 | 15 |
| 15 | context_specialist_policy_shadow_v1 | context_policy | SHADOW_AUTO | 14 | 30 |
| 16 | online_bayesian_weighting_shadow_v1 | adaptive_weighting | SHADOW_AUTO | 14 | 30 |
| 17 | phase_aware_rerank_shadow_v1 | phase_first | SHADOW_AUTO | 5 | 15 |
| 18 | cohere_rerank_effectiveness_v1 | rerank | SHADOW_AUTO | 3 | 3 |

## 8b. V52.5 era methods (30 entries; 10 per region × 3 regions)

| # | Experiment name | Table |
| --- | --- | --- |
| 1 | MB_ADAPTIVE_BUDGET_SELECTOR_V1 | experimental_preview_shadow |
| 2 | MB_ADAPTIVE_EXPLOIT_V1 | experimental_preview_shadow |
| 3 | MB_AI_CHAIN_PRESERVATION_V1 | experimental_preview_shadow |
| 4 | MB_CONSENSUS_V1 | experimental_preview_shadow |
| 5 | MB_HYBRID_V1 | experimental_preview_shadow |
| 6 | MB_NO_TOKEN_HERD_REDUCTION_V1 | experimental_preview_shadow |
| 7 | MB_OFFICIAL_BASELINE_CONTROL | experimental_preview_shadow |
| 8 | MB_PRIOR_REGION_CONTEXT_SAFE_V1 | experimental_preview_shadow |
| 9 | MB_SPECIALIST_ROSTER_V1 | experimental_preview_shadow |
| 10 | MB_STRENGTH_WEIGHTED_V52_5_2 | experimental_preview_shadow |
| 11 | MN_ADAPTIVE_BUDGET_SELECTOR_V1 | experimental_preview_shadow |
| 12 | MN_ADAPTIVE_EXPLOIT_V1 | experimental_preview_shadow |
| 13 | MN_AI_CHAIN_PRESERVATION_V1 | experimental_preview_shadow |
| 14 | MN_CONSENSUS_V1 | experimental_preview_shadow |
| 15 | MN_HYBRID_V1 | experimental_preview_shadow |
| 16 | MN_NO_TOKEN_HERD_REDUCTION_V1 | experimental_preview_shadow |
| 17 | MN_OFFICIAL_BASELINE_CONTROL | experimental_preview_shadow |
| 18 | MN_PRIOR_REGION_CONTEXT_SAFE_V1 | experimental_preview_shadow |
| 19 | MN_SPECIALIST_ROSTER_V1 | experimental_preview_shadow |
| 20 | MN_STRENGTH_WEIGHTED_V52_5_2 | experimental_preview_shadow |
| 21 | MT_ADAPTIVE_BUDGET_SELECTOR_V1 | experimental_preview_shadow |
| 22 | MT_ADAPTIVE_EXPLOIT_V1 | experimental_preview_shadow |
| 23 | MT_AI_CHAIN_PRESERVATION_V1 | experimental_preview_shadow |
| 24 | MT_CONSENSUS_V1 | experimental_preview_shadow |
| 25 | MT_HYBRID_V1 | experimental_preview_shadow |
| 26 | MT_NO_TOKEN_HERD_REDUCTION_V1 | experimental_preview_shadow |
| 27 | MT_OFFICIAL_BASELINE_CONTROL | experimental_preview_shadow |
| 28 | MT_PRIOR_REGION_CONTEXT_SAFE_V1 | experimental_preview_shadow |
| 29 | MT_SPECIALIST_ROSTER_V1 | experimental_preview_shadow |
| 30 | MT_STRENGTH_WEIGHTED_V52_5_2 | experimental_preview_shadow |

## 8c. Selector / generator surfaces (V67/V70/V73/V79/V80/V81; 11 entries)

| Selector | Purpose | Table | Status |
| --- | --- | --- | --- |
| MN/MT/MB_ADAPTIVE_BUDGET_SELECTOR_V1 | C-16 V57 budget selector | experimental_preview_shadow + du_doan_test_model_budget_daily | LIVE 3d emit |
| MN/MT/MB_ADAPTIVE_EXPLOIT_V1 (V67) | Lag1 exploit single-source | adaptive_exploit_v67_candidate_trace | LIVE 1d emit eager |
| MN/MT/MB_CONSENSUS_V1 (V70) | >=3 method consensus | consensus_v1_trace | LIVE 4d emit (post V77 fix) |
| MN/MT/MB_HYBRID_V1 (V73) | Region-adaptive HYBRID 5-tier | hybrid_v1_trace | LIVE 15d trace / 4d emit |
| V79 cluster_weighted | Cluster-weighted consensus with AI cap + NO_TOKEN floor | cluster_weighted_consensus_shadow | LIVE 4d (cron 19:08) |
| V79 cross_verify | AI ↔ NO_TOKEN cross-verification | ai_no_token_cross_verification_shadow | LIVE 4d (cron 19:08) |
| V80 rule_phase_synthesis | Rule phase pack for AI/no-token consumers | rule_phase_synthesis_shadow | LIVE 4d (cron 19:12) NO CONSUMER |
| V80 no_token_rule_pack | No-token rule-aware feature pack | no_token_rule_aware_pack_shadow | LIVE 4d (cron 19:12) NO CONSUMER |
| V80 mb_regime_shift | MB all-method cold flag + regime severity | mb_regime_shift_shadow | LIVE 4d (cron 19:12) |
| V80 mn_v67_save | MN AI herd vs V67 save signal monitor | mn_ai_herd_vs_v67_save_daily | LIVE 4d (cron 19:12) |
| V81 provider pilot | Owner-approved 3-model provider shadow pilot | ai_region_specialist_provider_shadow_results | LIVE 2d (cron 19:14) |
