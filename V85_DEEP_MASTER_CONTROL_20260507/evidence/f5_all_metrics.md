# 5/8 — ALL METRICS / CONTRACTS / SCORES

## 5a. C-XX measurement contracts (8 known active)

| ID | Purpose | Table | Status |
| --- | --- | --- | --- |
| C-01 | Strongest-vs-final conversion daily (per region/method) | strongest_vs_final_conversion_daily | LIVE |
| C-02 | API source labels (response-only metadata) | — | DEPLOYED V54 |
| C-03 | Closeout evaluator PENDING tracking + would_save tally | shadow_results | LIVE — PENDING reduced 37→9 (V74) |
| C-05 | Per-model latency / cost audit (token tracking) | model_latency_cost_audit_daily | RESOLVED V74.1 (was data lag); 20/42 latency rows captured 2026-05-07 |
| C-06 | LOZ stage trace shadow (LOZ_LINE_SELECTION_MISS / CANDIDATE_POOL_MISS) | loz_stage_trace_shadow (6356 rows over 60d) | LIVE V54 |
| C-15 | Weekday blackspot shadow (MB Wed/Fri, MT Mon/Fri) | weekday_blackspot_shadow (42 rows) | LIVE V54 |
| C-16 | Adaptive Model Budget Selector (15-20 voters per region/weekday/station) | du_doan_test_model_budget_daily + du_doan_test_selected_voters | LIVE V57; 20 voters all 3 regions after V71/V74 fix |
| C-17 | test lane bundle output_lock_status / readiness_status columns | du_doan_test_bundles | LIVE V74; 685 rows backfilled |

## 5b. PB-XX phase breakdown / PP layers

| ID | Purpose | Where | Status |
| --- | --- | --- | --- |
| PB-18.0 | PHASE-FIRST GATE 8-step (classify_rule_state) | gpt_analyzer.py PB-18 block | LIVE; cohort PFG-20260505-E active |
| PB-18.1..18.x | PB-18 trace fields (current_week_context, phase_alignment_summary, primary/secondary/stale rules, top_source_prizes_by_region, etc.) | gpt_analyzer JSON schema | LIVE for cohort-gated models |
| PP-1 | Pre-Push live watch surface (V20.3.22) | Wave 2 surfaces | LIVE |

## 5c. Flip / risk / health / cost metrics (16)

| Metric | Purpose | Where | Status |
| --- | --- | --- | --- |
| would_flip_baseline_to_win (would_save) | Method picks WIN where OFFICIAL LOSE | shadow_results | LIVE |
| would_flip_baseline_to_lose (would_break) | Method picks LOSE where OFFICIAL WIN | shadow_results | LIVE |
| false_promotion | Method picks LOSE while at higher rank than OFFICIAL | shadow_results | LIVE |
| strongest_vs_final_conversion | Strongest candidate retained in final bundle | shadow_results + strongest_vs_final_conversion_daily | LIVE |
| wilson_95_ci | Wilson 95% CI for hit_rate | evidence pack + V82 audit | LIVE |
| freshness_ready | Freshness chain readiness flag | shadow_results.freshness_ready + freshness_chain_daily | LIVE |
| candidate_drop_stage | Where candidate dropped in pipeline (LINE/POOL/BUNDLE_SKEW) | candidate_drop_stage_daily | LIVE |
| herd_pct | Herd percentage per pick | shadow_results.herd_pct + verdict_distribution_daily | LIVE |
| reliability_score | Per-model rolling reliability | runtime_reliability_model_daily | LIVE |
| stability_score | Per-method stability across days | shadow_method_scoreboard.stability_score | LIVE |
| promotion_bucket | Per-method maturity bucket label | shadow_method_scoreboard.promotion_bucket | LIVE |
| drift_alert_class | RED/YELLOW/ORANGE/GREEN/GRAY drift classes (V76) | test_lane_signal_drift_monitor | LIVE alert-only |
| fast_incident_alert_class | RED_FAST/ORANGE_FAST/YELLOW_FAST/EXPLOIT_FAIL_FAST/BUDGET_FAIL_FAST (V77) | test_lane_fast_incident_monitor | LIVE alert-only |
| cluster_weighted_score (V79) | Cluster-weighted final score with AI cap + NO_TOKEN floor | cluster_weighted_consensus_shadow.final_cluster_score | LIVE shadow |
| regime_shift_warning (V78/V80) | Region regime shift warning labels | ai_no_token_cross_verification_shadow.herd_risk_flag + mb_regime_shift_shadow.regime_state | LIVE shadow |
| cost_estimate_usd | Cost estimate per call (V76 P0-3 provider table) | model_latency_cost_audit_daily.cost_estimate_usd + _provider_pricing_table.py | LIVE tracking-only |
