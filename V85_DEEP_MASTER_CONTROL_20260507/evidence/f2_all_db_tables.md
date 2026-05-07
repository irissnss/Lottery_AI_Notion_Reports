# 2/8 — ALL DATABASE TABLES (129 total)

**Family distribution**: OFFICIAL=4 | TEST_LANE=21 | WAVE_1_2=13 | SHADOW=43 | INFRA=1 | SUPPORT=47

| Family | Table | Type | Rows | Date col | Min date | Max date |
| --- | --- | --- | --- | --- | --- | --- |
| INFRA | scheduler_logs | table | 117480 | - | - | - |
| OFFICIAL | final_bundles | table | 207 | date | 2026-02-28 | 2026-05-07 |
| OFFICIAL | lottery_results | table | 14628 | date | 2020-01-01 | 2026-05-07 |
| OFFICIAL | model_daily_eval | table | 4412 | date | 2026-01-29 | 2026-05-07 |
| OFFICIAL | predictions | table | 4461 | date | 2026-01-29 | 2026-05-07 |
| SHADOW | adaptive_exploit_v67_candidate_trace | table | 12 | target_date | 2026-05-07 | 2026-05-07 |
| SHADOW | ai_no_token_cross_verification_shadow | table | 12 | target_date | 2026-05-04 | 2026-05-07 |
| SHADOW | ai_prompt_context_audit_shadow | table | 12 | target_date | 2026-05-04 | 2026-05-07 |
| SHADOW | ai_region_specialist_prompt_shadow_results | table | 12 | target_date | 2026-05-04 | 2026-05-07 |
| SHADOW | ai_region_specialist_provider_shadow_results | table | 21 | target_date | 2026-05-06 | 2026-05-07 |
| SHADOW | bundle_universe_coverage_shadow | table | 96 | date | 2026-04-02 | 2026-05-02 |
| SHADOW | cluster_weighted_consensus_shadow | table | 130 | target_date | 2026-05-04 | 2026-05-07 |
| SHADOW | consensus_v1_trace | table | 27 | target_date | 2026-05-04 | 2026-05-07 |
| SHADOW | corrected_rescue_replay_shadow | table | 900 | date | 2026-04-03 | 2026-05-02 |
| SHADOW | counterfactual_decision_audit_shadow | table | 308 | date | 2026-04-27 | 2026-05-07 |
| SHADOW | cross_region_spillover_shadow | table | 9724 | date | 2026-03-03 | 2026-05-02 |
| SHADOW | hybrid_v1_trace | table | 45 | target_date | 2026-04-23 | 2026-05-07 |
| SHADOW | lag1_adaptive_exploit_signal_shadow | table | 1239 | anchor_date | 2026-05-06 | 2026-05-07 |
| SHADOW | loz_selector_shadow | table | 3512 | date | 2026-03-05 | 2026-05-06 |
| SHADOW | loz_stage_trace_shadow | table | 6356 | date | 2026-03-05 | 2026-05-05 |
| SHADOW | mb_regime_shift_shadow | table | 4 | target_date | 2026-05-04 | 2026-05-07 |
| SHADOW | mb_structural_drilldown_shadow | table | 62 | date | 2026-03-03 | 2026-05-02 |
| SHADOW | mn_ai_herd_vs_v67_save_daily | table | 4 | target_date | 2026-05-04 | 2026-05-07 |
| SHADOW | model_cross_region_dup_shadow | table | 662 | date | 2026-04-02 | 2026-05-02 |
| SHADOW | model_latency_cost_audit_daily | table | 3512 | date | 2026-03-05 | 2026-05-06 |
| SHADOW | mt_model_hit_output_drop_shadow | table | 315 | date | 2026-03-05 | 2026-05-06 |
| SHADOW | no_token_drift_shadow | table | 162 | date | 2026-04-27 | 2026-05-07 |
| SHADOW | no_token_rule_aware_pack_shadow | table | 12 | target_date | 2026-05-04 | 2026-05-07 |
| SHADOW | rule_phase_evidence_shadow | table | 590 | date | 2026-04-27 | 2026-05-07 |
| SHADOW | rule_phase_synthesis_shadow | table | 12 | target_date | 2026-05-04 | 2026-05-07 |
| SHADOW | shadow_activation_registry | table | 18 | created_at | 2026-04-28T00:28:00.097597+07:00 | 2026-04-30T03:25:23.998221+07:00 |
| SHADOW | shadow_candidates | table | 2779 | date | 2026-04-27 | 2026-05-07 |
| SHADOW | shadow_daily_comparison | table | 171 | date | 2026-03-12 | 2026-05-07 |
| SHADOW | shadow_feature_snapshots | table | 525 | date | 2026-04-27 | 2026-05-07 |
| SHADOW | shadow_method_scoreboard | table | 9132 | as_of_date | 2026-04-27 | 2026-05-07 |
| SHADOW | shadow_model_promotion_scorecard_daily | table | 425 | date | 2026-04-24 | 2026-05-07 |
| SHADOW | shadow_results | table | 2779 | date | 2026-04-27 | 2026-05-07 |
| SHADOW | shadow_rule_d1_comparison | table | 104 | date | 2026-01-20 | 2026-05-07 |
| SHADOW | single_vote_rescue_replay_shadow | table | 540 | date | 2026-04-02 | 2026-05-01 |
| SHADOW | strength_skip_calibration_replay_shadow | table | 865 | date | 2026-04-02 | 2026-05-02 |
| SHADOW | strongest_vs_final_shadow | table | 33 | date | 2026-04-27 | 2026-05-07 |
| SHADOW | sync_parity_audit_daily | table |  | date | - | - |
| SHADOW | test_lane_fast_incident_monitor | table | 15 | target_date | 2026-05-07 | 2026-05-07 |
| SHADOW | test_lane_signal_drift_monitor | table | 12 | anchor_date | 2026-05-07 | 2026-05-07 |
| SHADOW | tier2_replay_shadow | table | 192 | date | 2026-04-18 | 2026-05-02 |
| SHADOW | tier2_replay_v2_shadow | table | 558 | date | 2026-04-02 | 2026-05-02 |
| SHADOW | trace_field_completeness_daily | table | 48 | date | 2026-04-22 | 2026-05-07 |
| SHADOW | weekday_blackspot_shadow | table | 42 | anchor_date | 2026-05-03 | 2026-05-05 |
| SUPPORT | ai_herding_failure_daily | table | 24 | target_date | 2026-05-04 | 2026-05-07 |
| SUPPORT | app_settings | table | 252 | - | - | - |
| SUPPORT | bundle_family_contribution_daily | table | 48 | date | 2026-04-22 | 2026-05-07 |
| SUPPORT | bundle_replay_compare_daily | table |  | date | - | - |
| SUPPORT | candidate_drop_stage_daily | table | 93 | date | 2026-04-07 | 2026-05-07 |
| SUPPORT | cohere_effectiveness_daily | table | 62 | date | 2026-04-17 | 2026-05-07 |
| SUPPORT | cohere_rerank_log | table | 62 | date | 2026-04-17 | 2026-05-07 |
| SUPPORT | daily_eval_log | table | 239 | date | 2026-02-04 | 2026-05-07 |
| SUPPORT | daily_stats | table | 102 | date | 2025-11-06 | 2026-05-07 |
| SUPPORT | data_preservation_manifest_daily | table |  | date | - | - |
| SUPPORT | day_governance | table | 207 | date | 2026-02-28 | 2026-05-07 |
| SUPPORT | draw_availability_daily | table | 34 | date | 2026-04-26 | 2026-05-07 |
| SUPPORT | freshness_chain_daily | table | 343 | date | 2026-04-21 | 2026-05-07 |
| SUPPORT | main_vs_secondary_quality_daily | table | 48 | date | 2026-04-22 | 2026-05-07 |
| SUPPORT | method_cluster_performance_daily | table | 24 | target_date | 2026-05-04 | 2026-05-07 |
| SUPPORT | mined_rule_effectiveness | table | 1875 | date | 2025-12-20 | 2026-05-07 |
| SUPPORT | mined_rules | table | 105 | - | - | - |
| SUPPORT | mining_log | table | 22 | run_date | 2026-03-15 | 2026-05-04 |
| SUPPORT | mn_mb_failure_streak_daily | table | 2 | target_date | 2026-05-07 | 2026-05-07 |
| SUPPORT | official_vs_testlane_rescue_daily | table | 12 | target_date | 2026-05-04 | 2026-05-07 |
| SUPPORT | output_policy_replay_daily | table | 315 | date | 2026-04-23 | 2026-05-07 |
| SUPPORT | pattern_effectiveness | table | 92 | - | - | - |
| SUPPORT | pattern_rules | table | 160 | created_at | 2026-02-14 19:34:17 | 2026-02-26 16:02:25 |
| SUPPORT | pre_partial_post_lose_daily | table | 336 | date | 2026-04-22 | 2026-05-07 |
| SUPPORT | pre_vs_post_rerun_effect_daily | table | 144 | date | 2026-04-22 | 2026-05-07 |
| SUPPORT | pre_win_post_lose_daily | table | 336 | date | 2026-04-22 | 2026-05-07 |
| SUPPORT | prediction_policies | table | 6 | created_at | 2026-03-30 01:49:23 | 2026-03-30 01:49:23 |
| SUPPORT | prompt_pressure_daily | table | 811 | date | 2026-04-22 | 2026-05-07 |
| SUPPORT | rule_conversion_loss_stage_daily | table | 48 | date | 2026-04-22 | 2026-05-07 |
| SUPPORT | rule_effectiveness | table |  | - | - | - |
| SUPPORT | rule_features | table |  | date | - | - |
| SUPPORT | runtime_reliability_daily | table | 133 | date | 2026-04-14 | 2026-05-07 |
| SUPPORT | runtime_reliability_model_daily | table | 866 | date | 2026-04-14 | 2026-05-07 |
| SUPPORT | strongest_vs_final_conversion_daily | table | 93 | date | 2026-04-07 | 2026-05-07 |
| SUPPORT | system_alerts | table | 7 | date | 2026-04-14 | 2026-04-27 |
| SUPPORT | training_history | table | 72 | date | 2026-03-29 | 2026-05-03 |
| SUPPORT | training_records | table |  | - | - | - |
| SUPPORT | users | table | 2 | created_at | 2026-02-09T21:00:47.248884 | 2026-02-09T21:05:50.899446 |
| SUPPORT | v_bt_rate | view | 138 | - | - | - |
| SUPPORT | v_family_contribution_rolling_14d | view | 42 | date | 2026-04-24 | 2026-05-07 |
| SUPPORT | v_model_bt_rate_30d | view | 105 | - | - | - |
| SUPPORT | v_wr_14d | view | 577 | - | - | - |
| SUPPORT | v_wr_30d | view | 637 | - | - | - |
| SUPPORT | v_wr_7d | view | 552 | - | - | - |
| SUPPORT | v_wr_station | view | 1129 | date | 2026-04-23 | 2026-05-07 |
| SUPPORT | v_wr_weekday | view | 783 | - | - | - |
| SUPPORT | verified_bucket_rules | table | 105 | - | - | - |
| TEST_LANE | du_doan_test_ai_predictions | table |  | run_date | - | - |
| TEST_LANE | du_doan_test_audit_log | table | 250 | - | - | - |
| TEST_LANE | du_doan_test_bundles | table | 685 | run_date | 2026-04-04 | 2026-05-07 |
| TEST_LANE | du_doan_test_candidates | table | 15830 | run_date | 2026-04-04 | 2026-05-07 |
| TEST_LANE | du_doan_test_conversion_trace | table | 685 | run_date | 2026-04-04 | 2026-05-07 |
| TEST_LANE | du_doan_test_daily_summary | table | 13 | run_date | 2026-05-03 | 2026-05-07 |
| TEST_LANE | du_doan_test_experiment_scoreboard | table | 81 | - | - | - |
| TEST_LANE | du_doan_test_experiments | table | 31 | created_at | 2026-05-03T20:16:40.270048+07:00 | 2026-05-07T04:30:00.110029+07:00 |
| TEST_LANE | du_doan_test_latency_daily | table |  | run_date | - | - |
| TEST_LANE | du_doan_test_leakage_audit | table | 685 | run_date | 2026-04-04 | 2026-05-07 |
| TEST_LANE | du_doan_test_method_scoreboard | table | 81 | - | - | - |
| TEST_LANE | du_doan_test_model_budget_daily | table | 9 | run_date | 2026-05-05 | 2026-05-07 |
| TEST_LANE | du_doan_test_model_contribution | table | 15830 | - | - | - |
| TEST_LANE | du_doan_test_model_scoreboard | table | 3632 | - | - | - |
| TEST_LANE | du_doan_test_model_skip_reason | table | 51 | run_date | 2026-05-05 | 2026-05-07 |
| TEST_LANE | du_doan_test_results | table | 685 | run_date | 2026-04-04 | 2026-05-07 |
| TEST_LANE | du_doan_test_runs | table | 685 | run_date | 2026-04-04 | 2026-05-07 |
| TEST_LANE | du_doan_test_selected_voters | table | 261 | run_date | 2026-05-05 | 2026-05-07 |
| TEST_LANE | experimental_preview_shadow | table | 1242 | date | 2026-03-05 | 2026-05-07 |
| TEST_LANE | mb_experimental_preview_shadow | table | 49 | date | 2026-05-02 | 2026-05-07 |
| TEST_LANE | model_strength_by_region_weekday_station_daily | table | 17927 | anchor_date | 2026-05-02 | 2026-05-05 |
| WAVE_1_2 | ai_primary_gate_daily | table | 45 | date | 2026-04-23 | 2026-05-07 |
| WAVE_1_2 | ai_reasoning_contract_daily | table | 45 | date | 2026-04-23 | 2026-05-07 |
| WAVE_1_2 | bundle_readiness_gate_daily | table | 45 | date | 2026-04-23 | 2026-05-07 |
| WAVE_1_2 | convergence_cluster_pattern_daily | table | 231 | date | 2026-04-05 | 2026-05-07 |
| WAVE_1_2 | output_eligible_completion_daily | table | 45 | date | 2026-04-23 | 2026-05-07 |
| WAVE_1_2 | pp1_live_watch_daily | table | 26 | date | 2026-04-26 | 2026-05-07 |
| WAVE_1_2 | prompt_section_breakdown_daily | table | 5081 | date | 2026-04-22 | 2026-05-07 |
| WAVE_1_2 | public_bundle_publish_audit_daily | table | 45 | date | 2026-04-23 | 2026-05-07 |
| WAVE_1_2 | reasoning_layer_penetration_daily | table | 45 | date | 2026-04-23 | 2026-05-07 |
| WAVE_1_2 | source_prize_effectiveness_daily | table | 985 | date | 2026-04-23 | 2026-05-07 |
| WAVE_1_2 | strongest_candidate_escape_daily | table | 45 | date | 2026-04-23 | 2026-05-07 |
| WAVE_1_2 | verdict_distribution_daily | table | 1346 | date | 2026-04-20 | 2026-05-07 |
| WAVE_1_2 | weekday_rule_strength_daily | table | 45 | date | 2026-04-23 | 2026-05-07 |
