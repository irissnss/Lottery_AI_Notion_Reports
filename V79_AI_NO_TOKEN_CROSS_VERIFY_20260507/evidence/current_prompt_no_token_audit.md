# Current Prompt / NO_TOKEN Audit

Kết luận: AI production hiện có self-history + model ranking, nhưng **không có daily no-token herd candidate trước khi gọi model**, không có V67/V70/V73/C16 candidates, không có independent cluster count.

| field | production_prompt | production_context | shadow_context | risk |
| --- | --- | --- | --- | --- |
| no_token_herd_candidate | MISSING | MISSING | PRESENT_V79 | HIGH |
| no_token_top_votes | MISSING | MISSING | PRESENT_V79 | HIGH |
| no_token_cluster_score | MISSING | MISSING | PRESENT_V79 | HIGH |
| no_token_recent_hit_rate | PARTIAL_MODEL_RANKING_ONLY | PARTIAL | PRESENT_V79_4_7_14D | MEDIUM |
| ai_herd_candidate | MISSING_PRE_PROMPT | POST_PREDICTION_ONLY | PRESENT_V79 | HIGH |
| V67/V70/V73/C16 | MISSING | MISSING | PRESENT_V79 | HIGH |
| independent_cluster_count | MISSING | MISSING | PRESENT_V79 | HIGH |
| created_before_result_guard | N/A | PARTIAL | PRESENT_V79 | HIGH |
