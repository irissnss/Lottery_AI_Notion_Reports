# Cluster Weighted Consensus

Raw AI vote count is capped by cluster. Official is diagnostic/control only and does not add score. NO_TOKEN has a protected floor when valid. V67/V70/V73/C16 are independent test-lane clusters.

| target_date | region | rank | tail | raw_vote_count | cluster_vote_count | cluster_list_json | ai_vote_count | no_token_vote_count | testlane_vote_count | official_vote_present | final_cluster_score | selected_tail | herd_risk_flag | independent_cluster_count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-05-04 | MB | 1 | 09 | 6 | 4 | ["AI_FAST_GENERAL", "AI_REASONING_HEAVY", "TEST_CONSENSUS", "TEST_HYBRID"] | 4 | 0 | 2 | 1 | 0.805 | 09 | AI_HERD_RISK | 4 |
| 2026-05-04 | MB | 2 | 19 | 2 | 2 | ["AI_REASONING_HEAVY", "NO_TOKEN_ENSEMBLE"] | 1 | 1 | 0 | 0 | 0.425 | 09 | AI_HERD_RISK | 2 |
| 2026-05-04 | MB | 3 | 24 | 3 | 2 | ["AI_FAST_GENERAL", "AI_REASONING_HEAVY"] | 3 | 0 | 0 | 0 | 0.35 | 09 | AI_HERD_RISK | 2 |
| 2026-05-04 | MB | 4 | 46 | 6 | 2 | ["AI_FAST_GENERAL", "AI_REASONING_HEAVY"] | 6 | 0 | 0 | 0 | 0.35 | 09 | AI_HERD_RISK | 2 |
| 2026-05-04 | MB | 5 | 60 | 2 | 2 | ["NO_TOKEN_ENSEMBLE", "NO_TOKEN_TREE"] | 0 | 2 | 0 | 0 | 0.25 | 09 | AI_HERD_RISK | 2 |
| 2026-05-04 | MN | 1 | 65 | 9 | 5 | ["AI_FAST_GENERAL", "AI_REASONING_HEAVY", "NO_TOKEN_ENSEMBLE", "TEST_CONSENSUS", "TEST_HYBRID"] | 6 | 1 | 2 | 1 | 1.055 | 65 | NONE | 5 |
| 2026-05-04 | MN | 2 | 48 | 5 | 2 | ["AI_FAST_GENERAL", "AI_REASONING_HEAVY"] | 5 | 0 | 0 | 0 | 0.35 | 65 | NONE | 2 |
| 2026-05-04 | MN | 3 | 15 | 1 | 1 | ["NO_TOKEN_TREE"] | 0 | 1 | 0 | 0 | 0.25 | 65 | NONE | 1 |
| 2026-05-04 | MN | 4 | 18 | 1 | 1 | ["NO_TOKEN_SEQUENCE"] | 0 | 1 | 0 | 0 | 0.25 | 65 | NONE | 1 |
| 2026-05-04 | MN | 5 | 32 | 4 | 2 | ["NO_TOKEN_ENSEMBLE", "NO_TOKEN_TREE"] | 0 | 4 | 0 | 0 | 0.25 | 65 | NONE | 2 |
| 2026-05-04 | MT | 1 | 82 | 8 | 4 | ["AI_FAST_GENERAL", "AI_REASONING_HEAVY", "TEST_CONSENSUS", "TEST_HYBRID"] | 6 | 0 | 2 | 0 | 0.855 | 82 | NONE | 4 |
| 2026-05-04 | MT | 2 | 28 | 2 | 2 | ["AI_FAST_GENERAL", "AI_REASONING_HEAVY"] | 2 | 0 | 0 | 0 | 0.35 | 82 | NONE | 2 |
| 2026-05-04 | MT | 3 | 42 | 3 | 2 | ["AI_FAST_GENERAL", "AI_REASONING_HEAVY"] | 3 | 0 | 0 | 0 | 0.35 | 82 | NONE | 2 |
| 2026-05-04 | MT | 4 | 97 | 2 | 2 | ["AI_FAST_GENERAL", "AI_REASONING_HEAVY"] | 2 | 0 | 0 | 0 | 0.35 | 82 | NONE | 2 |
| 2026-05-04 | MT | 5 | 25 | 1 | 1 | ["NO_TOKEN_SEQUENCE"] | 0 | 1 | 0 | 0 | 0.25 | 82 | NONE | 1 |
| 2026-05-05 | MB | 1 | 41 | 13 | 6 | ["AI_FAST_GENERAL", "AI_REASONING_HEAVY", "BUDGET_STRENGTH", "NO_TOKEN_ENSEMBLE", "TEST_CONSENSUS", "TEST_HYBRID"] | 9 | 1 | 3 | 0 | 1.23 | 41 | NONE | 6 |
| 2026-05-05 | MB | 2 | 09 | 3 | 2 | ["AI_FAST_GENERAL", "AI_REASONING_HEAVY"] | 3 | 0 | 0 | 0 | 0.35 | 41 | NONE | 2 |
| 2026-05-05 | MB | 3 | 14 | 2 | 2 | ["AI_FAST_GENERAL", "AI_REASONING_HEAVY"] | 2 | 0 | 0 | 0 | 0.35 | 41 | NONE | 2 |
| 2026-05-05 | MB | 4 | 91 | 2 | 2 | ["AI_FAST_GENERAL", "AI_REASONING_HEAVY"] | 2 | 0 | 0 | 0 | 0.35 | 41 | NONE | 2 |
| 2026-05-05 | MB | 5 | 19 | 2 | 2 | ["NO_TOKEN_ENSEMBLE", "NO_TOKEN_TREE"] | 0 | 2 | 0 | 0 | 0.25 | 41 | NONE | 2 |
| 2026-05-05 | MN | 1 | 52 | 10 | 4 | ["AI_FAST_GENERAL", "AI_REASONING_HEAVY", "BUDGET_STRENGTH", "NO_TOKEN_ENSEMBLE"] | 8 | 1 | 1 | 0 | 0.775 | 52 | NONE | 4 |
| 2026-05-05 | MN | 2 | 15 | 6 | 4 | ["NO_TOKEN_ENSEMBLE", "NO_TOKEN_TREE", "TEST_CONSENSUS", "TEST_HYBRID"] | 0 | 4 | 2 | 1 | 0.705 | 52 | NONE | 4 |
| 2026-05-05 | MN | 3 | 13 | 5 | 2 | ["AI_FAST_GENERAL", "AI_REASONING_HEAVY"] | 5 | 0 | 0 | 0 | 0.35 | 52 | NONE | 2 |
| 2026-05-05 | MN | 4 | 24 | 2 | 2 | ["AI_FAST_GENERAL", "AI_REASONING_HEAVY"] | 2 | 0 | 0 | 0 | 0.35 | 52 | NONE | 2 |
| 2026-05-05 | MN | 5 | 56 | 3 | 2 | ["AI_FAST_GENERAL", "AI_REASONING_HEAVY"] | 3 | 0 | 0 | 0 | 0.35 | 52 | NONE | 2 |
| 2026-05-05 | MT | 1 | 44 | 5 | 4 | ["NO_TOKEN_ENSEMBLE", "NO_TOKEN_TREE", "TEST_CONSENSUS", "TEST_HYBRID"] | 0 | 3 | 2 | 1 | 0.755 | 44 | AI_HERD_RISK | 4 |
| 2026-05-05 | MT | 2 | 52 | 8 | 3 | ["AI_FAST_GENERAL", "AI_REASONING_HEAVY", "BUDGET_STRENGTH"] | 7 | 0 | 1 | 0 | 0.525 | 44 | AI_HERD_RISK | 3 |
| 2026-05-05 | MT | 3 | 14 | 2 | 2 | ["AI_FAST_GENERAL", "AI_REASONING_HEAVY"] | 2 | 0 | 0 | 0 | 0.35 | 44 | AI_HERD_RISK | 2 |
| 2026-05-05 | MT | 4 | 37 | 6 | 2 | ["AI_FAST_GENERAL", "AI_REASONING_HEAVY"] | 6 | 0 | 0 | 0 | 0.35 | 44 | AI_HERD_RISK | 2 |
| 2026-05-05 | MT | 5 | 08 | 1 | 1 | ["NO_TOKEN_ENSEMBLE"] | 0 | 1 | 0 | 0 | 0.25 | 44 | AI_HERD_RISK | 1 |
| 2026-05-06 | MB | 1 | 32 | 6 | 5 | ["AI_FAST_GENERAL", "AI_REASONING_HEAVY", "NO_TOKEN_ENSEMBLE", "TEST_CONSENSUS", "TEST_HYBRID"] | 3 | 1 | 2 | 0 | 1.055 | 32 | AI_HERD_RISK | 5 |
| 2026-05-06 | MB | 2 | 78 | 4 | 3 | ["AI_FAST_GENERAL", "AI_REASONING_HEAVY", "NO_TOKEN_ENSEMBLE"] | 3 | 1 | 0 | 0 | 0.6 | 32 | AI_HERD_RISK | 3 |
| 2026-05-06 | MB | 3 | 79 | 5 | 3 | ["AI_FAST_GENERAL", "AI_REASONING_HEAVY", "BUDGET_STRENGTH"] | 4 | 0 | 1 | 1 | 0.525 | 32 | AI_HERD_RISK | 3 |
| 2026-05-06 | MB | 4 | 49 | 7 | 2 | ["AI_FAST_GENERAL", "AI_REASONING_HEAVY"] | 7 | 0 | 0 | 0 | 0.35 | 32 | AI_HERD_RISK | 2 |
| 2026-05-06 | MB | 5 | 92 | 3 | 2 | ["NO_TOKEN_ENSEMBLE", "NO_TOKEN_TREE"] | 0 | 3 | 0 | 0 | 0.25 | 32 | AI_HERD_RISK | 2 |
| 2026-05-06 | MN | 1 | 95 | 14 | 6 | ["AI_FAST_GENERAL", "AI_REASONING_HEAVY", "BUDGET_STRENGTH", "NO_TOKEN_ENSEMBLE", "TEST_CONSENSUS", "TEST_HYBRID"] | 10 | 1 | 3 | 1 | 1.23 | 95 | NONE | 6 |
| 2026-05-06 | MN | 2 | 27 | 2 | 2 | ["AI_FAST_GENERAL", "AI_REASONING_HEAVY"] | 2 | 0 | 0 | 0 | 0.35 | 95 | NONE | 2 |
| 2026-05-06 | MN | 3 | 93 | 5 | 2 | ["AI_FAST_GENERAL", "AI_REASONING_HEAVY"] | 5 | 0 | 0 | 0 | 0.35 | 95 | NONE | 2 |
| 2026-05-06 | MN | 4 | 15 | 1 | 1 | ["NO_TOKEN_ENSEMBLE"] | 0 | 1 | 0 | 0 | 0.25 | 95 | NONE | 1 |
| 2026-05-06 | MN | 5 | 18 | 1 | 1 | ["NO_TOKEN_SEQUENCE"] | 0 | 1 | 0 | 0 | 0.25 | 95 | NONE | 1 |
| 2026-05-06 | MT | 1 | 71 | 18 | 5 | ["AI_FAST_GENERAL", "AI_REASONING_HEAVY", "BUDGET_STRENGTH", "TEST_CONSENSUS", "TEST_HYBRID"] | 15 | 0 | 3 | 0 | 1.03 | 71 | NONE | 5 |
| 2026-05-06 | MT | 2 | 67 | 3 | 2 | ["AI_FAST_GENERAL", "AI_REASONING_HEAVY"] | 3 | 0 | 0 | 0 | 0.35 | 71 | NONE | 2 |
| 2026-05-06 | MT | 3 | 05 | 1 | 1 | ["NO_TOKEN_SEQUENCE"] | 0 | 1 | 0 | 0 | 0.25 | 71 | NONE | 1 |
| 2026-05-06 | MT | 4 | 11 | 2 | 1 | ["NO_TOKEN_ENSEMBLE"] | 0 | 2 | 0 | 1 | 0.25 | 71 | NONE | 1 |
| 2026-05-06 | MT | 5 | 26 | 1 | 1 | ["NO_TOKEN_ENSEMBLE"] | 0 | 1 | 0 | 0 | 0.25 | 71 | NONE | 1 |
| 2026-05-07 | MB | 1 | 20 | 6 | 4 | ["AI_FAST_GENERAL", "AI_REASONING_HEAVY", "BUDGET_STRENGTH", "TEST_CONSENSUS"] | 4 | 0 | 2 | 1 | 0.75 | 20 | AI_HERD_RISK | 4 |
| 2026-05-07 | MB | 2 | 79 | 4 | 3 | ["AI_FAST_GENERAL", "TEST_EXPLOIT", "TEST_HYBRID"] | 2 | 0 | 2 | 0 | 0.655 | 20 | AI_HERD_RISK | 3 |
| 2026-05-07 | MB | 3 | 32 | 3 | 2 | ["AI_FAST_GENERAL", "AI_REASONING_HEAVY"] | 3 | 0 | 0 | 0 | 0.35 | 20 | AI_HERD_RISK | 2 |
| 2026-05-07 | MB | 4 | 37 | 5 | 2 | ["AI_FAST_GENERAL", "AI_REASONING_HEAVY"] | 5 | 0 | 0 | 0 | 0.35 | 20 | AI_HERD_RISK | 2 |
| 2026-05-07 | MB | 5 | 64 | 3 | 2 | ["NO_TOKEN_ENSEMBLE", "NO_TOKEN_TREE"] | 0 | 3 | 0 | 0 | 0.25 | 20 | AI_HERD_RISK | 2 |
| 2026-05-07 | MN | 1 | 95 | 2 | 2 | ["TEST_EXPLOIT", "TEST_HYBRID"] | 0 | 0 | 2 | 0 | 0.83 | 95 | AI_HERD_RISK | 2 |
| 2026-05-07 | MN | 2 | 94 | 11 | 4 | ["AI_FAST_GENERAL", "AI_REASONING_HEAVY", "BUDGET_STRENGTH", "TEST_CONSENSUS"] | 9 | 0 | 2 | 1 | 0.75 | 95 | AI_HERD_RISK | 4 |
| 2026-05-07 | MN | 3 | 05 | 6 | 3 | ["AI_FAST_GENERAL", "AI_REASONING_HEAVY", "NO_TOKEN_ENSEMBLE"] | 5 | 1 | 0 | 0 | 0.6 | 95 | AI_HERD_RISK | 3 |
| 2026-05-07 | MN | 4 | 32 | 2 | 2 | ["AI_FAST_GENERAL", "AI_REASONING_HEAVY"] | 2 | 0 | 0 | 0 | 0.35 | 95 | AI_HERD_RISK | 2 |
| 2026-05-07 | MN | 5 | 20 | 1 | 1 | ["NO_TOKEN_TREE"] | 0 | 1 | 0 | 0 | 0.25 | 95 | AI_HERD_RISK | 1 |
| 2026-05-07 | MT | 1 | 88 | 10 | 5 | ["BUDGET_STRENGTH", "NO_TOKEN_ENSEMBLE", "NO_TOKEN_TREE", "TEST_CONSENSUS", "TEST_HYBRID"] | 0 | 7 | 3 | 1 | 0.93 | 88 | AI_HERD_RISK | 5 |
| 2026-05-07 | MT | 2 | 40 | 9 | 2 | ["AI_FAST_GENERAL", "AI_REASONING_HEAVY"] | 9 | 0 | 0 | 0 | 0.35 | 88 | AI_HERD_RISK | 2 |
| 2026-05-07 | MT | 3 | 69 | 6 | 2 | ["AI_FAST_GENERAL", "AI_REASONING_HEAVY"] | 6 | 0 | 0 | 0 | 0.35 | 88 | AI_HERD_RISK | 2 |
| 2026-05-07 | MT | 4 | 93 | 3 | 2 | ["AI_FAST_GENERAL", "AI_REASONING_HEAVY"] | 3 | 0 | 0 | 0 | 0.35 | 88 | AI_HERD_RISK | 2 |
| 2026-05-07 | MT | 5 | 12 | 1 | 1 | ["NO_TOKEN_SEQUENCE"] | 0 | 1 | 0 | 0 | 0.25 | 88 | AI_HERD_RISK | 1 |
