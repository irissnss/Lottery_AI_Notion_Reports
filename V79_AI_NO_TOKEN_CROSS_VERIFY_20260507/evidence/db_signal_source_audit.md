# DB Signal Source Audit

| signal | table | before_ai_call | before_test_lane | after_result | safe_to_use | leakage_risk |
| --- | --- | --- | --- | --- | --- | --- |
| AI predictions | predictions | NO_SELF_CURRENT_RUN | YES_AFTER_MODEL_RUN | YES | YES_IF_CREATED_BEFORE_RESULT | LOW_WITH_GUARD |
| NO_TOKEN predictions | predictions | YES_FOR_04:00_NO_TOKEN | YES | YES | YES_IF_CREATED_BEFORE_RESULT | LOW_WITH_GUARD |
| V67 | experimental_preview_shadow/adaptive_exploit_v67_candidate_trace | NO | YES | YES | YES_IF_CREATED_BEFORE_RESULT | LOW_WITH_GUARD |
| V70 | experimental_preview_shadow/consensus_v1_trace | NO | YES_AFTER_FULL_POOL | YES | YES_IF_CREATED_BEFORE_RESULT | MEDIUM_IF_BACKFILLED |
| V73 | experimental_preview_shadow/hybrid_v1_trace | NO | YES_AFTER_FULL_POOL | YES | YES_IF_CREATED_BEFORE_RESULT | MEDIUM_IF_BACKFILLED |
| C16 | du_doan_test_model_budget_daily / experimental_preview_shadow | NO | YES | YES | YES_IF_CREATED_BEFORE_RESULT | LOW_WITH_GUARD |
| Official | final_bundles | YES_BASELINE | YES | YES | DIAGNOSTIC_ONLY | LOW |
| Actuals | lottery_results | NO_FOR_TARGET | NO_FOR_TARGET | YES | EVALUATION_ONLY | HIGH_IF_PROMPT |
