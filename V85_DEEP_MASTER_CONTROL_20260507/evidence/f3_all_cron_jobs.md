# 3/8 — ALL CRON JOBS (26 total)

| Job ID | Trigger (VN) | Purpose | Lane |
| --- | --- | --- | --- |
| auto_mn | config (default 16:30 VN) | Scrape MN + closeout chain | OFFICIAL_INFRA |
| auto_mt | config (default 17:30 VN) | Scrape MT + predict MB | OFFICIAL_INFRA |
| auto_mb | config (default 18:30 VN) | Scrape MB + verify MN/MT | OFFICIAL_INFRA |
| auto_weight_optimizer | config (weekly day+time) | Auto weights optimizer | MEASUREMENT |
| auto_weekly_mining | Mon 00:30 VN | Weekly rule mining | RULE_MINING |
| auto_free_predict | config (default 04:00 VN) | LSTM + Meta no-token predict all regions | OFFICIAL_NO_TOKEN |
| auto_ai_mt | config (default 16:45 VN) | AI predict MT | OFFICIAL_AI |
| auto_ai_mb | config (default 17:45 VN) | AI predict MB | OFFICIAL_AI |
| mb_prediction_watchdog | 17:55 VN | Re-trigger MB if missing | OFFICIAL_INFRA |
| auto_ai_mn | config (default 04:30 VN) | AI predict MN | OFFICIAL_AI |
| du_doan_test_pre_result_trigger | every 5 min | /du-doan-test pre-result readiness | TEST_LANE |
| lag1_adaptive_exploit_signal_materializer | 23:35 VN | V66.1 lag1 adaptive exploit signal materializer | MEASUREMENT_V66 |
| adaptive_exploit_v67_materializer | 23:40 VN | V67 ADAPTIVE_EXPLOIT_V1 selector | TEST_LANE_V67 |
| consensus_v1_materializer | 23:45 VN | V70 CONSENSUS_V1 selector | TEST_LANE_V70 |
| hybrid_v1_materializer | 23:48 VN | V73 HYBRID_V1 region-adaptive selector | TEST_LANE_V73 |
| drift_monitor_materializer | 23:50 VN | V76 drift detector (alert-only) | MEASUREMENT_V76 |
| v77_post_cascade_rerun | 19:00 VN | V77 V70/V73 post-cascade rerun with full pool | TEST_LANE_V77 |
| v77_fast_incident_monitor | 19:05 VN | V77 fast incident monitor (5 alert classes) | MEASUREMENT_V77 |
| v79_ai_no_token_cross_verify | 19:08 VN | V79 AI ↔ NO_TOKEN cross-verify + cluster-weighted | SHADOW_V79 |
| v78_prompt_shadow_audit | 19:10 VN | V78 region-specialist prompt audit (no provider call) | SHADOW_V78 |
| v80_shadow_completion | 19:12 VN | V80 rule_phase_synthesis + no_token_rule_pack + mb_regime + mn_v67_save | SHADOW_V80 |
| v81_provider_shadow_pilot | 19:14 VN | V81 owner-approved 3-model provider pilot | SHADOW_V81 |
| auto_retrain | Sun 02:00 VN (weekly) | Auto retrain ML models (LSTM/XGB/RF/Meta) | ML_TRAINING |
| auto_daily_eval | config (default ~20:00 VN) | Daily evaluation per model | MEASUREMENT |
| auto_mined_rule_eval | config (default ~20:10 VN) | Mined rule effectiveness eval | RULE_EVAL |
| auto_model_daily_eval | config (default ~20:20 VN) | Per-model daily eval (model_daily_eval table) | MEASUREMENT |
