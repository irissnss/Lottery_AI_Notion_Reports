# V52 Measurement Completeness Matrix

| Measurement area | Existing table/file | Auto/manual | Latest date | Region coverage | Rolling window | Data quality | Missing fields | Owner usefulness | Ready for code/fix? | Verdict |
|---|---|---|---|---|---|---|---|---|---|---|
| official output quality | final_bundles + model_daily_eval | AUTO | 2026-05-03 | MN/MT/MB | 3/7/14/30/60 | good for diagnostic | degraded-day formal split | high | diagnostic only | MEASUREMENT_SUFFICIENT_FOR_DIAGNOSTIC |
| model-level quality | model_daily_eval + tensor CSV | AUTO/artifact | 2026-05-03 | MN/MT/MB | 7/14/30/60 | partial | latency/cost/unique risk | high | no pruning | MISSING_LATENCY |
| model contribution | final_bundles.source_predictions_json + du_doan_test_model_scoreboard | MANUAL/test for MB | 2026-05-03 | official all, test MB only | limited | partial | station-level + loz line contribution | high | measurement/test only | MEASUREMENT_NOT_SUFFICIENT_FOR_OFFICIAL_CHANGE |
| correct_but_dropped | V51 forensic JSON | MANUAL audit | 2026-05-03 | MN/MT/MB | one-day + rolling needed | thin | canonical table | high | measurement now | MISSING_TRACE |
| wrong_boosted | du_doan_test_results/model_scoreboard | MANUAL test | 2026-05-03 | MB only | 2 dates | thin | MN/MT, realtime proof | medium | test only | MISSING_AUTO_EVALUATOR |
| source-prize conversion | source_predictions_json / shadow tables | partial | 2026-05-03 | MN/MT/MB | limited | partial | daily conversion table | high | measurement only | MISSING_TRACE |
| rule injection conversion | rule_phase_evidence_shadow | AUTO/post-MDE | 2026-05-01/varies | MN/MT/MB | limited | partial | latest freshness reconciliation | medium | measurement only | MISSING_TRACE |
| no-token drift | no_token_drift_shadow + V51 MT forensic | AUTO/shadow | varies | MN/MT/MB | rolling | partial | official drop-stage table | high | measurement only | MEASUREMENT_SUFFICIENT_FOR_DIAGNOSTIC |
| AI vs no-token split | predictions/final bundle score_breakdown | AUTO | 2026-05-03 | MN/MT/MB | rolling possible | partial | canonical family-score daily table | high | measurement only | MISSING_TRACE |
| shadow vs official | shadow_results + scoreboards | AUTO | varies | MN/MT/MB | rolling | good diagnostic | UI consolidation | medium | measurement/UI | MEASUREMENT_SUFFICIENT_FOR_DIAGNOSTIC |
| loz1/loz2 | final_bundles + predictions | AUTO/manual audit | 2026-05-03 | MN/MT/MB | 3/7/14/30/60 | mixed | loz selector shadow | high | measurement/test only | LOZ_SIGNAL_MIXED |
| cost/latency | tensor/trace | artifact | 2026-05-03 | all | diagnostic | insufficient | duration/cost/token | very high | no prune | MISSING_LATENCY + MISSING_COST |
| runtime reliability | scheduler_logs/health | AUTO | 2026-05-03 | system | daily | good | none critical | medium | watch | MEASUREMENT_SUFFICIENT_FOR_DIAGNOSTIC |
| test lane comparison | du_doan_test_* | MANUAL | 2026-05-03 | MB only | 2 dates | manual only | MN/MT + realtime natural proof | high | test only | MISSING_AUTO_EVALUATOR |
| leakage audit | du_doan_test_leakage_audit + corrected replay audit | MANUAL/test | 2026-05-03 | MB test + replay | limited | partial | source timestamp rows for all regions | high | test/measurement | MEASUREMENT_SUFFICIENT_FOR_TEST_LANE |
| UI visibility | du-doan-test.html | MANUAL UI | 2026-05-03 | MB | current | partial | explicit loz1/loz2/region filters | medium | UI-test only | MISSING_UI_COMPARISON |
