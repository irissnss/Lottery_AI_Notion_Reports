# Prompt coverage matrix

| field | present_in_prompt | present_in_context | present_in_code | logged_to_trace | used_by_model | fix_status | note |
| --- | --- | --- | --- | --- | --- | --- | --- |
| previous_official_miss | True | True | True | False | True | PARTIAL | self-history exists but not official final_bundle miss context |
| previous_lo2_miss | True | True | True | False | True | PARTIAL | not explicitly injected as prior LO2 miss candidate |
| same_region_lag1 | False | False | False | False | False | MISSING | not in official prompt; V66/V67 exists in test-lane only |
| same_region_lag2 | False | False | False | False | False | MISSING | not in official prompt; V66.1 measures it only |
| cross_region_sameday | True | True | True | False | True | PARTIAL | inter-region source data present for MT/MB |
| cross_region_nextday | False | False | False | False | False | MISSING | not in official prompt |
| V67_candidate | False | False | False | False | False | SHADOW_PROMPT_REQUIRED | not in official prompt |
| V70_consensus_candidate | False | True | True | False | True | SHADOW_PROMPT_REQUIRED | not in official prompt |
| V73_candidate/tier | False | True | True | False | True | SHADOW_PROMPT_REQUIRED | not in official prompt |
| agreement_count | False | False | False | False | False | SHADOW_PROMPT_REQUIRED | not in official prompt |
| no_token_herd_candidate | False | False | False | False | False | MISSING | only model ranking, no daily no-token herd candidate |
| ai_herd_candidate | False | False | False | False | False | MISSING | post-prediction diversity pass exists, not pre-prompt context |
| official_tail | False | False | False | False | False | MISSING | not injected into prompt for same target day |
| recent_model_failure_streak | True | True | True | True | True | PARTIAL | self WR exists; model-specific failure streak partial |
| region-specific doctrine | True | True | True | False | True | PARTIAL | generic region caution exists; not V78 specialist split |
| anti-herding instruction | True | True | True | False | True | PARTIAL | generic anti-herding exists |
| MB volatility warning | True | True | True | False | True | PARTIAL | present generic; lacks current cold-streak input |
| MN lag1 exploit instruction | True | True | True | False | True | SHADOW_PROMPT_REQUIRED | opposite instruction: avoid yesterday loses |
| MT consensus-first instruction | True | True | True | False | True | SHADOW_PROMPT_REQUIRED | not explicit by region |
