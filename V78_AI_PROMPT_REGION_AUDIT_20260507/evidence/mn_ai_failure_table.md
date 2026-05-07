# MN AI failure table

| date | region | model | class | bt | actual_hit | official_bt | c16_bt | v67_bt | v70_bt | v73_bt | herd_tail | herd_count | previous_official_miss | labels |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-05-04 | MN | claude-opus-4-20250514 | TOKEN | 42 | False | 65 | None | None | 65 | 65 | 65 | 7 | None |  |
| 2026-05-04 | MN | claude-sonnet-4-6 | TOKEN | 65 | False | 65 | None | None | 65 | 65 | 65 | 7 | None | AI_HERD_WRONG,OFFICIAL_TAIL_OVERWEIGHTED |
| 2026-05-04 | MN | combo-super | TOKEN | 65 | False | 65 | None | None | 65 | 65 | 65 | 7 | None | AI_HERD_WRONG,OFFICIAL_TAIL_OVERWEIGHTED,PROMPT_CONTEXT_MISSING_TRACE |
| 2026-05-04 | MN | deepseek-reasoner | TOKEN | 65 | False | 65 | None | None | 65 | 65 | 65 | 7 | None | AI_HERD_WRONG,OFFICIAL_TAIL_OVERWEIGHTED |
| 2026-05-04 | MN | deepseek-v4-flash | TOKEN | 54 | False | 65 | None | None | 65 | 65 | 65 | 7 | None |  |
| 2026-05-04 | MN | deepseek-v4-pro | TOKEN | 48 | False | 65 | None | None | 65 | 65 | 65 | 7 | None |  |
| 2026-05-04 | MN | gemini-2.5-flash | TOKEN | 30 | True | 65 | None | None | 65 | 65 | 65 | 7 | None |  |
| 2026-05-04 | MN | gemini-2.5-pro | TOKEN | 65 | False | 65 | None | None | 65 | 65 | 65 | 7 | None | AI_HERD_WRONG,OFFICIAL_TAIL_OVERWEIGHTED |
| 2026-05-04 | MN | glm-5.1 | TOKEN | 65 | False | 65 | None | None | 65 | 65 | 65 | 7 | None | AI_HERD_WRONG,OFFICIAL_TAIL_OVERWEIGHTED |
| 2026-05-04 | MN | gpt-5-mini | TOKEN | 48 | False | 65 | None | None | 65 | 65 | 65 | 7 | None |  |
| 2026-05-04 | MN | gpt-5.4 | TOKEN | 65 | False | 65 | None | None | 65 | 65 | 65 | 7 | None | AI_HERD_WRONG,OFFICIAL_TAIL_OVERWEIGHTED |
| 2026-05-04 | MN | gpt-5.5 | TOKEN | 42 | False | 65 | None | None | 65 | 65 | 65 | 7 | None |  |
| 2026-05-04 | MN | gpt-oss-120b | TOKEN | 63 | False | 65 | None | None | 65 | 65 | 65 | 7 | None |  |
| 2026-05-04 | MN | grok-4.20-multi-agent | TOKEN | 48 | False | 65 | None | None | 65 | 65 | 65 | 7 | None |  |
| 2026-05-04 | MN | kimi-k2.5 | TOKEN | 48 | False | 65 | None | None | 65 | 65 | 65 | 7 | None |  |
| 2026-05-04 | MN | qwen3-coder | TOKEN | 56 | False | 65 | None | None | 65 | 65 | 65 | 7 | None |  |
| 2026-05-04 | MN | qwen3-max-thinking | TOKEN | 65 | False | 65 | None | None | 65 | 65 | 65 | 7 | None | AI_HERD_WRONG,OFFICIAL_TAIL_OVERWEIGHTED |
| 2026-05-04 | MN | qwen3.6-plus | TOKEN | 48 | False | 65 | None | None | 65 | 65 | 65 | 7 | None |  |
| 2026-05-05 | MN | claude-opus-4-20250514 | TOKEN | 52 | True | 15 | 52 | None | 15 | 15 | 52 | 9 | 65 | AI_HERD_RIGHT |
| 2026-05-05 | MN | claude-sonnet-4-6 | TOKEN | 24 | True | 15 | 52 | None | 15 | 15 | 52 | 9 | 65 |  |
| 2026-05-05 | MN | combo-super | TOKEN | 52 | True | 15 | 52 | None | 15 | 15 | 52 | 9 | 65 | AI_HERD_RIGHT,PROMPT_CONTEXT_MISSING_TRACE |
| 2026-05-05 | MN | deepseek-reasoner | TOKEN | 13 | False | 15 | 52 | None | 15 | 15 | 52 | 9 | 65 |  |
| 2026-05-05 | MN | deepseek-v4-flash | TOKEN | 52 | True | 15 | 52 | None | 15 | 15 | 52 | 9 | 65 | AI_HERD_RIGHT |
| 2026-05-05 | MN | deepseek-v4-pro | TOKEN | 52 | True | 15 | 52 | None | 15 | 15 | 52 | 9 | 65 | AI_HERD_RIGHT |
| 2026-05-05 | MN | gemini-2.5-flash | TOKEN | 13 | False | 15 | 52 | None | 15 | 15 | 52 | 9 | 65 |  |
| 2026-05-05 | MN | gemini-2.5-pro | TOKEN | 24 | True | 15 | 52 | None | 15 | 15 | 52 | 9 | 65 |  |
| 2026-05-05 | MN | gemini-3-flash | TOKEN | 13 | False | 15 | 52 | None | 15 | 15 | 52 | 9 | 65 |  |
| 2026-05-05 | MN | gemini-3.1-pro | TOKEN | 56 | False | 15 | 52 | None | 15 | 15 | 52 | 9 | 65 |  |
| 2026-05-05 | MN | gemma-4-31b | TOKEN | 13 | False | 15 | 52 | None | 15 | 15 | 52 | 9 | 65 |  |
| 2026-05-05 | MN | glm-5.1 | TOKEN | 56 | False | 15 | 52 | None | 15 | 15 | 52 | 9 | 65 |  |
| 2026-05-05 | MN | gpt-5-mini | TOKEN | 41 | False | 15 | 52 | None | 15 | 15 | 52 | 9 | 65 |  |
| 2026-05-05 | MN | gpt-5.4 | TOKEN | 52 | True | 15 | 52 | None | 15 | 15 | 52 | 9 | 65 | AI_HERD_RIGHT |
| 2026-05-05 | MN | gpt-5.5 | TOKEN | 63 | True | 15 | 52 | None | 15 | 15 | 52 | 9 | 65 |  |
| 2026-05-05 | MN | gpt-oss-120b | TOKEN | 52 | True | 15 | 52 | None | 15 | 15 | 52 | 9 | 65 | AI_HERD_RIGHT |
| 2026-05-05 | MN | grok-4.20-multi-agent | TOKEN | 52 | True | 15 | 52 | None | 15 | 15 | 52 | 9 | 65 | AI_HERD_RIGHT |
| 2026-05-05 | MN | kimi-k2.5 | TOKEN | 56 | False | 15 | 52 | None | 15 | 15 | 52 | 9 | 65 |  |
| 2026-05-05 | MN | qwen3-coder | TOKEN | 52 | True | 15 | 52 | None | 15 | 15 | 52 | 9 | 65 | AI_HERD_RIGHT |
| 2026-05-05 | MN | qwen3-max-thinking | TOKEN | 13 | False | 15 | 52 | None | 15 | 15 | 52 | 9 | 65 |  |
| 2026-05-05 | MN | qwen3.6-plus | TOKEN | 52 | True | 15 | 52 | None | 15 | 15 | 52 | 9 | 65 | AI_HERD_RIGHT |
| 2026-05-06 | MN | claude-opus-4-20250514 | TOKEN | 95 | False | 95 | 95 | None | 95 | 95 | 95 | 11 | 15 | AI_HERD_WRONG,OFFICIAL_TAIL_OVERWEIGHTED |
| 2026-05-06 | MN | claude-sonnet-4-6 | TOKEN | 95 | False | 95 | 95 | None | 95 | 95 | 95 | 11 | 15 | AI_HERD_WRONG,OFFICIAL_TAIL_OVERWEIGHTED |
| 2026-05-06 | MN | combo-super | TOKEN | 95 | False | 95 | 95 | None | 95 | 95 | 95 | 11 | 15 | AI_HERD_WRONG,OFFICIAL_TAIL_OVERWEIGHTED,PROMPT_CONTEXT_MISSING_TRACE |
| 2026-05-06 | MN | deepseek-reasoner | TOKEN | 27 | False | 95 | 95 | None | 95 | 95 | 95 | 11 | 15 |  |
| 2026-05-06 | MN | deepseek-v4-flash | TOKEN | 95 | False | 95 | 95 | None | 95 | 95 | 95 | 11 | 15 | AI_HERD_WRONG,OFFICIAL_TAIL_OVERWEIGHTED |
| 2026-05-06 | MN | deepseek-v4-pro | TOKEN | 95 | False | 95 | 95 | None | 95 | 95 | 95 | 11 | 15 | AI_HERD_WRONG,OFFICIAL_TAIL_OVERWEIGHTED |
| 2026-05-06 | MN | gemini-2.5-flash | TOKEN | 27 | False | 95 | 95 | None | 95 | 95 | 95 | 11 | 15 |  |
| 2026-05-06 | MN | gemini-2.5-pro | TOKEN | 67 | False | 95 | 95 | None | 95 | 95 | 95 | 11 | 15 |  |
| 2026-05-06 | MN | gemini-3-flash | TOKEN | 93 | True | 95 | 95 | None | 95 | 95 | 95 | 11 | 15 |  |
| 2026-05-06 | MN | gemini-3.1-pro | TOKEN | 95 | False | 95 | 95 | None | 95 | 95 | 95 | 11 | 15 | AI_HERD_WRONG,OFFICIAL_TAIL_OVERWEIGHTED |
| 2026-05-06 | MN | gemma-4-31b | TOKEN | 95 | False | 95 | 95 | None | 95 | 95 | 95 | 11 | 15 | AI_HERD_WRONG,OFFICIAL_TAIL_OVERWEIGHTED |
| 2026-05-06 | MN | glm-5.1 | TOKEN | 95 | False | 95 | 95 | None | 95 | 95 | 95 | 11 | 15 | AI_HERD_WRONG,OFFICIAL_TAIL_OVERWEIGHTED |
| 2026-05-06 | MN | gpt-5-mini | TOKEN | 93 | True | 95 | 95 | None | 95 | 95 | 95 | 11 | 15 |  |
| 2026-05-06 | MN | gpt-5.4 | TOKEN | 95 | False | 95 | 95 | None | 95 | 95 | 95 | 11 | 15 | AI_HERD_WRONG,OFFICIAL_TAIL_OVERWEIGHTED |
| 2026-05-06 | MN | gpt-5.5 | TOKEN | 95 | False | 95 | 95 | None | 95 | 95 | 95 | 11 | 15 | AI_HERD_WRONG,OFFICIAL_TAIL_OVERWEIGHTED |
| 2026-05-06 | MN | gpt-oss-120b | TOKEN | 21 | False | 95 | 95 | None | 95 | 95 | 95 | 11 | 15 |  |
| 2026-05-06 | MN | grok-4.20-multi-agent | TOKEN | 93 | True | 95 | 95 | None | 95 | 95 | 95 | 11 | 15 |  |
| 2026-05-06 | MN | kimi-k2.5 | TOKEN | 56 | True | 95 | 95 | None | 95 | 95 | 95 | 11 | 15 |  |
| 2026-05-06 | MN | qwen3-coder | TOKEN | 93 | True | 95 | 95 | None | 95 | 95 | 95 | 11 | 15 |  |
| 2026-05-06 | MN | qwen3-max-thinking | TOKEN | 95 | False | 95 | 95 | None | 95 | 95 | 95 | 11 | 15 | AI_HERD_WRONG,OFFICIAL_TAIL_OVERWEIGHTED |
| 2026-05-06 | MN | qwen3.6-plus | TOKEN | 93 | True | 95 | 95 | None | 95 | 95 | 95 | 11 | 15 |  |
| 2026-05-07 | MN | claude-opus-4-20250514 | TOKEN | 94 | False | 94 | 94 | 95 | 94 | 95 | 94 | 9 | 95 | AI_HERD_WRONG,IGNORED_V67_SAVE_CANDIDATE,IGNORED_LAG1_EDGE,OFFICIAL_TAIL_OVERWEIGHTED |
| 2026-05-07 | MN | claude-sonnet-4-6 | TOKEN | 94 | False | 94 | 94 | 95 | 94 | 95 | 94 | 9 | 95 | AI_HERD_WRONG,IGNORED_V67_SAVE_CANDIDATE,IGNORED_LAG1_EDGE,OFFICIAL_TAIL_OVERWEIGHTED |
| 2026-05-07 | MN | combo-super | TOKEN | 05 | False | 94 | 94 | 95 | 94 | 95 | 94 | 9 | 95 | IGNORED_V67_SAVE_CANDIDATE,IGNORED_LAG1_EDGE,PROMPT_CONTEXT_MISSING_TRACE |
| 2026-05-07 | MN | deepseek-reasoner | TOKEN | 94 | False | 94 | 94 | 95 | 94 | 95 | 94 | 9 | 95 | AI_HERD_WRONG,IGNORED_V67_SAVE_CANDIDATE,IGNORED_LAG1_EDGE,OFFICIAL_TAIL_OVERWEIGHTED |
| 2026-05-07 | MN | deepseek-v4-flash | TOKEN | 05 | False | 94 | 94 | 95 | 94 | 95 | 94 | 9 | 95 | IGNORED_V67_SAVE_CANDIDATE,IGNORED_LAG1_EDGE |
| 2026-05-07 | MN | deepseek-v4-pro | TOKEN | 05 | False | 94 | 94 | 95 | 94 | 95 | 94 | 9 | 95 | IGNORED_V67_SAVE_CANDIDATE,IGNORED_LAG1_EDGE |
| 2026-05-07 | MN | gemini-2.5-flash | TOKEN | 94 | False | 94 | 94 | 95 | 94 | 95 | 94 | 9 | 95 | AI_HERD_WRONG,IGNORED_V67_SAVE_CANDIDATE,IGNORED_LAG1_EDGE,OFFICIAL_TAIL_OVERWEIGHTED |
| 2026-05-07 | MN | gemini-2.5-pro | TOKEN | 94 | False | 94 | 94 | 95 | 94 | 95 | 94 | 9 | 95 | AI_HERD_WRONG,IGNORED_V67_SAVE_CANDIDATE,IGNORED_LAG1_EDGE,OFFICIAL_TAIL_OVERWEIGHTED |
| 2026-05-07 | MN | gemini-3-flash | TOKEN | 32 | False | 94 | 94 | 95 | 94 | 95 | 94 | 9 | 95 | IGNORED_V67_SAVE_CANDIDATE,IGNORED_LAG1_EDGE |
| 2026-05-07 | MN | gemini-3.1-pro | TOKEN | 69 | False | 94 | 94 | 95 | 94 | 95 | 94 | 9 | 95 | IGNORED_V67_SAVE_CANDIDATE,IGNORED_LAG1_EDGE |
| 2026-05-07 | MN | gemma-4-31b | TOKEN | 02 | True | 94 | 94 | 95 | 94 | 95 | 94 | 9 | 95 | IGNORED_V67_SAVE_CANDIDATE,IGNORED_LAG1_EDGE |
| 2026-05-07 | MN | glm-5.1 | TOKEN | 05 | False | 94 | 94 | 95 | 94 | 95 | 94 | 9 | 95 | IGNORED_V67_SAVE_CANDIDATE,IGNORED_LAG1_EDGE |
| 2026-05-07 | MN | gpt-5-mini | TOKEN | 05 | False | 94 | 94 | 95 | 94 | 95 | 94 | 9 | 95 | IGNORED_V67_SAVE_CANDIDATE,IGNORED_LAG1_EDGE |
| 2026-05-07 | MN | gpt-5.4 | TOKEN | 05 | False | 94 | 94 | 95 | 94 | 95 | 94 | 9 | 95 | IGNORED_V67_SAVE_CANDIDATE,IGNORED_LAG1_EDGE |
| 2026-05-07 | MN | gpt-5.5 | TOKEN | 90 | False | 94 | 94 | 95 | 94 | 95 | 94 | 9 | 95 | IGNORED_V67_SAVE_CANDIDATE,IGNORED_LAG1_EDGE |
| 2026-05-07 | MN | gpt-oss-120b | TOKEN | 90 | False | 94 | 94 | 95 | 94 | 95 | 94 | 9 | 95 | IGNORED_V67_SAVE_CANDIDATE,IGNORED_LAG1_EDGE |
| 2026-05-07 | MN | grok-4.20-multi-agent | TOKEN | 94 | False | 94 | 94 | 95 | 94 | 95 | 94 | 9 | 95 | AI_HERD_WRONG,IGNORED_V67_SAVE_CANDIDATE,IGNORED_LAG1_EDGE,OFFICIAL_TAIL_OVERWEIGHTED |
| 2026-05-07 | MN | kimi-k2.5 | TOKEN | 94 | False | 94 | 94 | 95 | 94 | 95 | 94 | 9 | 95 | AI_HERD_WRONG,IGNORED_V67_SAVE_CANDIDATE,IGNORED_LAG1_EDGE,OFFICIAL_TAIL_OVERWEIGHTED |
| 2026-05-07 | MN | qwen3-coder | TOKEN | 94 | False | 94 | 94 | 95 | 94 | 95 | 94 | 9 | 95 | AI_HERD_WRONG,IGNORED_V67_SAVE_CANDIDATE,IGNORED_LAG1_EDGE,OFFICIAL_TAIL_OVERWEIGHTED |
| 2026-05-07 | MN | qwen3-max-thinking | TOKEN | 94 | False | 94 | 94 | 95 | 94 | 95 | 94 | 9 | 95 | AI_HERD_WRONG,IGNORED_V67_SAVE_CANDIDATE,IGNORED_LAG1_EDGE,OFFICIAL_TAIL_OVERWEIGHTED |
| 2026-05-07 | MN | qwen3.6-plus | TOKEN | 32 | False | 94 | 94 | 95 | 94 | 95 | 94 | 9 | 95 | IGNORED_V67_SAVE_CANDIDATE,IGNORED_LAG1_EDGE |
