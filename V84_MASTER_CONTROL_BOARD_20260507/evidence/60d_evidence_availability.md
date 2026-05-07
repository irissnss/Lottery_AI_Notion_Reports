# 60d evidence availability map

| Family | Table | 60d? | Max window | Reason |
| --- | --- | --- | --- | --- |
| OFFICIAL final_bundles | final_bundles | YES | 60d (n=60) | Live since 2026-02-28. |
| AI_HERD via predictions | predictions | YES | 60d (n=60) | Live since 2026-01-29. |
| NO_TOKEN_HERD via predictions | predictions | YES | 60d (n=60) | Live since 2026-01-29. |
| V52.5 OFFICIAL/STRENGTH/SPECIALIST/PRIOR_REGION/AI_CHAIN/NO_TOKEN_REDUCTION | experimental_preview_shadow | YES | 60-67d (n=60-67) | Backfilled since 2026-03-05. |
| C-16 ADAPTIVE_BUDGET_SELECTOR_V1 (V57) | experimental_preview_shadow | NO | 3d | Method live since 2026-05-05. |
| V67 ADAPTIVE_EXPLOIT_V1 | experimental_preview_shadow + adaptive_exploit_v67_candidate_trace | NO | 1d emit / 12d trace (RETRO_LIMITED) | Cron 23:40 VN since 2026-05-07. |
| V70 CONSENSUS_V1 | experimental_preview_shadow + consensus_v1_trace | NO | 4d emit (RETRO_LIMITED) | Cron 23:45 + V77 19:00 rerun since 2026-05-07. |
| V73 HYBRID_V1 | experimental_preview_shadow + hybrid_v1_trace | NO | 15d trace / 4d emit (RETRO_LIMITED) | Region-adaptive HYBRID since 2026-05-07. |
| V76 drift monitor | test_lane_signal_drift_monitor | NO | 12 GRAY rows (n30<10) | Active alert after 14d fresh data (2026-05-21). |
| V77 fast incident monitor | test_lane_fast_incident_monitor | NO | 1d | Cron 19:05 VN since 2026-05-07. |
| V78 prompt shadow audit | ai_region_specialist_prompt_shadow_results | NO | 4d (no provider call) | Cron 19:10 VN since 2026-05-07. |
| V79 cluster_weighted + cross_verify | cluster_weighted_consensus_shadow + ai_no_token_cross_verification_shadow | NO | 4d | Cron 19:08 VN since 2026-05-07. |
| V80 rule_phase_synthesis + no_token_rule_pack + mb_regime + mn_v67_save | rule_phase_synthesis_shadow / no_token_rule_aware_pack_shadow / mb_regime_shift_shadow / mn_ai_herd_vs_v67_save_daily | NO | 4d | Cron 19:12 VN since 2026-05-07. |
| V81 provider shadow pilot | ai_region_specialist_provider_shadow_results | NO | 2d (LIVE_LIMITED_2D) | Cron 19:14 VN since 2026-05-07; 18 calls. |
| P0 portfolio 18 methods (shadow_results) | shadow_results | PARTIAL | 8-11d (started 2026-04-27 to 2026-04-30) | Newest scaffolds 2026-04-29/30; oldest 2026-04-27. Need 49 more days for true 60d. |
| Wave 1/2 control surfaces | ai_primary_gate_daily etc. | PARTIAL | ~12d (since 2026-04-25) | Live deploy 2026-04-25. |
