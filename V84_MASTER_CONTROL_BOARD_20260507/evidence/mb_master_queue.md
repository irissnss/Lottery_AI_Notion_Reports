# MB master forensic queue

## 18-method P0 portfolio 14d (shadow_results region split)

| Method | n | Hit | Rate | Win flip | Lose flip | FP | Net | Verdict |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| model_wisdom_scorecard_shadow_v1 | 233 | 44 | 0.189 | 39 | 20 | 157 | 19 | PARITY |
| counterfactual_decision_audit_v1 | 80 | 24 | 0.3 | 23 | 9 | 54 | 14 | BENEFICIAL_REGION |
| strongest_to_final_preservation_v1 | 11 | 11 | 1.0 | 9 | 0 | 0 | 9 | INSUFFICIENT |
| phase_first_decision_shadow_v1 | 27 | 7 | 0.259 | 6 | 2 | 13 | 4 | BENEFICIAL_REGION |
| meta_ranker_ltr_dataset_shadow_v1 | 27 | 7 | 0.259 | 6 | 2 | 13 | 4 | BENEFICIAL_REGION |
| context_specialist_policy_shadow_v1 | 27 | 7 | 0.259 | 6 | 2 | 13 | 4 | BENEFICIAL_REGION |
| phase_aware_rerank_shadow_v1 | 27 | 7 | 0.259 | 6 | 2 | 13 | 4 | BENEFICIAL_REGION |
| output_policy_replay_governance_v1 | 77 | 17 | 0.221 | 4 | 1 | 16 | 3 | BENEFICIAL_REGION |
| anti_herding_shadow_v1 | 27 | 6 | 0.222 | 5 | 2 | 14 | 3 | BENEFICIAL_REGION |
| rule_injection_contract_shadow_v1 | 30 | 6 | 0.2 | 6 | 3 | 22 | 3 | PARITY |
| meta_ranker_v1 | 33 | 8 | 0.242 | 6 | 4 | 17 | 2 | PARITY |
| rule_aware_adaptive_notoken_shadow_v1 | 27 | 4 | 0.148 | 3 | 2 | 16 | 1 | PARITY |
| online_bayesian_weighting_shadow_v1 | 27 | 4 | 0.148 | 3 | 2 | 15 | 1 | PARITY |
| freshness_readiness_guard_v1 | 8 | 1 | 0.125 | 0 | 0 | 0 | 0 | INSUFFICIENT |
| runtime_final_baseline_control_v1 | 9 | 1 | 0.111 | 0 | 0 | 0 | 0 | INSUFFICIENT |
| cohere_rerank_effectiveness_v1 | 8 | 1 | 0.125 | 1 | 1 | 7 | 0 | INSUFFICIENT |
| no_token_drift_guard_v1 | 77 | 11 | 0.143 | 11 | 14 | 47 | -3 | DESTRUCTIVE_REGION |
| rule_phase_evidence_v1 | 159 | 24 | 0.151 | 16 | 30 | 133 | -14 | DESTRUCTIVE_REGION |

## V82 60d evidence (cached)

- OFFICIAL 25.0% (n=60); MB_SPECIALIST_ROSTER 36.6% (n=41 only); other methods within ±5pp of OFFICIAL.
- AI severe herd 25/60 days; only 13/44 AI misses had a savior in V67/V73/NO_TOKEN.
- All test selectors V67/V70/V73/V79 0/4 on the 4d window.

## V79 cluster + V81 pilot 4d/2d MB

- V79 cluster_weighted_tail MB 0/4 hits; 0 saves.
- V81 provider pilot MB 0/6 (claude/gemini/deepseek), but each model gave LOW conf with herd warning — prompt working as designed (honest cold acknowledgement).

## Trigger calendar for MB

- 2026-05-14: 7d cold streak gate. If MB OFFICIAL still 0/7 → auto-escalate P0 MB regime forensic dossier.
- 2026-05-21: 14d gate. If still cold → kích hoạt detailed station/source-prize/lag deep dive.
- 2026-06-06: 30d gate. If MB_SPECIALIST_ROSTER hits ≥30 sample with positive lift → eligible test-lane voter proposal (MB only).

## What is NOT yet known

- MB station-level break analysis (need cross_region_spillover_shadow + mb_structural_drilldown_shadow rolling)
- MB rule-state alignment vs cold streak
- MB prize-band / source-prize concentration

## Hard locks for MB

- KHÔNG promote bất kỳ method nào cho MB trước 30d sample + owner OK.
- KHÔNG raise NO_TOKEN MB (60d delta -3.3pp).
