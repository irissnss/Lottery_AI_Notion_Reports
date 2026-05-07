# MB AI failure table

| date | region | model | class | bt | actual_hit | official_bt | c16_bt | v67_bt | v70_bt | v73_bt | herd_tail | herd_count | previous_official_miss | labels |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-05-04 | MB | claude-opus-4-20250514 | TOKEN | 24 | False | 09 | None | None | 09 | 09 | 46 | 6 | None |  |
| 2026-05-04 | MB | claude-sonnet-4-6 | TOKEN | 09 | False | 09 | None | None | 09 | 09 | 46 | 6 | None | OFFICIAL_TAIL_OVERWEIGHTED |
| 2026-05-04 | MB | combo-super | TOKEN | 19 | False | 09 | None | None | 09 | 09 | 46 | 6 | None | PROMPT_CONTEXT_MISSING_TRACE |
| 2026-05-04 | MB | deepseek-reasoner | TOKEN | 56 | True | 09 | None | None | 09 | 09 | 46 | 6 | None |  |
| 2026-05-04 | MB | deepseek-v4-flash | TOKEN | 24 | False | 09 | None | None | 09 | 09 | 46 | 6 | None |  |
| 2026-05-04 | MB | deepseek-v4-pro | TOKEN | 59 | False | 09 | None | None | 09 | 09 | 46 | 6 | None |  |
| 2026-05-04 | MB | gemini-2.5-flash | TOKEN | 46 | True | 09 | None | None | 09 | 09 | 46 | 6 | None | AI_HERD_RIGHT |
| 2026-05-04 | MB | gemini-2.5-pro | TOKEN | 09 | False | 09 | None | None | 09 | 09 | 46 | 6 | None | OFFICIAL_TAIL_OVERWEIGHTED |
| 2026-05-04 | MB | glm-5.1 | TOKEN | 59 | False | 09 | None | None | 09 | 09 | 46 | 6 | None |  |
| 2026-05-04 | MB | gpt-5-mini | TOKEN | 46 | True | 09 | None | None | 09 | 09 | 46 | 6 | None | AI_HERD_RIGHT |
| 2026-05-04 | MB | gpt-5.4 | TOKEN | 19 | False | 09 | None | None | 09 | 09 | 46 | 6 | None |  |
| 2026-05-04 | MB | gpt-5.5 | TOKEN | 09 | False | 09 | None | None | 09 | 09 | 46 | 6 | None | OFFICIAL_TAIL_OVERWEIGHTED |
| 2026-05-04 | MB | gpt-oss-120b | TOKEN | 09 | False | 09 | None | None | 09 | 09 | 46 | 6 | None | OFFICIAL_TAIL_OVERWEIGHTED |
| 2026-05-04 | MB | grok-4.20-multi-agent | TOKEN | 46 | True | 09 | None | None | 09 | 09 | 46 | 6 | None | AI_HERD_RIGHT |
| 2026-05-04 | MB | kimi-k2.5 | TOKEN | 46 | True | 09 | None | None | 09 | 09 | 46 | 6 | None | AI_HERD_RIGHT |
| 2026-05-04 | MB | qwen3-coder | TOKEN | 24 | False | 09 | None | None | 09 | 09 | 46 | 6 | None |  |
| 2026-05-04 | MB | qwen3-max-thinking | TOKEN | 46 | True | 09 | None | None | 09 | 09 | 46 | 6 | None | AI_HERD_RIGHT |
| 2026-05-04 | MB | qwen3.6-plus | TOKEN | 46 | True | 09 | None | None | 09 | 09 | 46 | 6 | None | AI_HERD_RIGHT |
| 2026-05-05 | MB | claude-opus-4-20250514 | TOKEN | 41 | False | 83 | 41 | None | 41 | 41 | 41 | 10 | 09 | AI_HERD_WRONG |
| 2026-05-05 | MB | claude-sonnet-4-6 | TOKEN | 41 | False | 83 | 41 | None | 41 | 41 | 41 | 10 | 09 | AI_HERD_WRONG |
| 2026-05-05 | MB | combo-super | TOKEN | 41 | False | 83 | 41 | None | 41 | 41 | 41 | 10 | 09 | AI_HERD_WRONG,PROMPT_CONTEXT_MISSING_TRACE |
| 2026-05-05 | MB | deepseek-reasoner | TOKEN | 98 | True | 83 | 41 | None | 41 | 41 | 41 | 10 | 09 |  |
| 2026-05-05 | MB | deepseek-v4-flash | TOKEN | 09 | False | 83 | 41 | None | 41 | 41 | 41 | 10 | 09 | PICKED_PREVIOUS_OFFICIAL_MISS |
| 2026-05-05 | MB | deepseek-v4-pro | TOKEN | 09 | False | 83 | 41 | None | 41 | 41 | 41 | 10 | 09 | PICKED_PREVIOUS_OFFICIAL_MISS |
| 2026-05-05 | MB | gemini-2.5-flash | TOKEN | 41 | False | 83 | 41 | None | 41 | 41 | 41 | 10 | 09 | AI_HERD_WRONG |
| 2026-05-05 | MB | gemini-2.5-pro | TOKEN | 41 | False | 83 | 41 | None | 41 | 41 | 41 | 10 | 09 | AI_HERD_WRONG |
| 2026-05-05 | MB | gemini-3-flash | TOKEN | 91 | True | 83 | 41 | None | 41 | 41 | 41 | 10 | 09 |  |
| 2026-05-05 | MB | gemini-3.1-pro | TOKEN | 90 | False | 83 | 41 | None | 41 | 41 | 41 | 10 | 09 |  |
| 2026-05-05 | MB | gemma-4-31b | TOKEN | 14 | True | 83 | 41 | None | 41 | 41 | 41 | 10 | 09 |  |
| 2026-05-05 | MB | glm-5.1 | TOKEN | 41 | False | 83 | 41 | None | 41 | 41 | 41 | 10 | 09 | AI_HERD_WRONG |
| 2026-05-05 | MB | gpt-5-mini | TOKEN | 71 | True | 83 | 41 | None | 41 | 41 | 41 | 10 | 09 |  |
| 2026-05-05 | MB | gpt-5.4 | TOKEN | 09 | False | 83 | 41 | None | 41 | 41 | 41 | 10 | 09 | PICKED_PREVIOUS_OFFICIAL_MISS |
| 2026-05-05 | MB | gpt-5.5 | TOKEN | 66 | True | 83 | 41 | None | 41 | 41 | 41 | 10 | 09 |  |
| 2026-05-05 | MB | gpt-oss-120b | TOKEN | 14 | True | 83 | 41 | None | 41 | 41 | 41 | 10 | 09 |  |
| 2026-05-05 | MB | grok-4.20-multi-agent | TOKEN | 41 | False | 83 | 41 | None | 41 | 41 | 41 | 10 | 09 | AI_HERD_WRONG |
| 2026-05-05 | MB | kimi-k2.5 | TOKEN | 41 | False | 83 | 41 | None | 41 | 41 | 41 | 10 | 09 | AI_HERD_WRONG |
| 2026-05-05 | MB | qwen3-coder | TOKEN | 41 | False | 83 | 41 | None | 41 | 41 | 41 | 10 | 09 | AI_HERD_WRONG |
| 2026-05-05 | MB | qwen3-max-thinking | TOKEN | 41 | False | 83 | 41 | None | 41 | 41 | 41 | 10 | 09 | AI_HERD_WRONG |
| 2026-05-05 | MB | qwen3.6-plus | TOKEN | 91 | True | 83 | 41 | None | 41 | 41 | 41 | 10 | 09 |  |
| 2026-05-06 | MB | claude-opus-4-20250514 | TOKEN | 32 | False | 79 | 79 | None | 32 | 32 | 49 | 7 | 83 |  |
| 2026-05-06 | MB | claude-sonnet-4-6 | TOKEN | 71 | False | 79 | 79 | None | 32 | 32 | 49 | 7 | 83 |  |
| 2026-05-06 | MB | combo-super | TOKEN | 32 | False | 79 | 79 | None | 32 | 32 | 49 | 7 | 83 | PROMPT_CONTEXT_MISSING_TRACE |
| 2026-05-06 | MB | deepseek-reasoner | TOKEN | 79 | False | 79 | 79 | None | 32 | 32 | 49 | 7 | 83 | OFFICIAL_TAIL_OVERWEIGHTED |
| 2026-05-06 | MB | deepseek-v4-flash | TOKEN | 79 | False | 79 | 79 | None | 32 | 32 | 49 | 7 | 83 | OFFICIAL_TAIL_OVERWEIGHTED |
| 2026-05-06 | MB | deepseek-v4-pro | TOKEN | 49 | False | 79 | 79 | None | 32 | 32 | 49 | 7 | 83 | AI_HERD_WRONG |
| 2026-05-06 | MB | gemini-2.5-flash | TOKEN | 79 | False | 79 | 79 | None | 32 | 32 | 49 | 7 | 83 | OFFICIAL_TAIL_OVERWEIGHTED |
| 2026-05-06 | MB | gemini-2.5-pro | TOKEN | 32 | False | 79 | 79 | None | 32 | 32 | 49 | 7 | 83 |  |
| 2026-05-06 | MB | gemini-3-flash | TOKEN | 64 | False | 79 | 79 | None | 32 | 32 | 49 | 7 | 83 |  |
| 2026-05-06 | MB | gemini-3.1-pro | TOKEN | 49 | False | 79 | 79 | None | 32 | 32 | 49 | 7 | 83 | AI_HERD_WRONG |
| 2026-05-06 | MB | gemma-4-31b | TOKEN | 49 | False | 79 | 79 | None | 32 | 32 | 49 | 7 | 83 | AI_HERD_WRONG |
| 2026-05-06 | MB | glm-5.1 | TOKEN | 49 | False | 79 | 79 | None | 32 | 32 | 49 | 7 | 83 | AI_HERD_WRONG |
| 2026-05-06 | MB | gpt-5-mini | TOKEN | 79 | False | 79 | 79 | None | 32 | 32 | 49 | 7 | 83 | OFFICIAL_TAIL_OVERWEIGHTED |
| 2026-05-06 | MB | gpt-5.4 | TOKEN | 32 | False | 79 | 79 | None | 32 | 32 | 49 | 7 | 83 |  |
| 2026-05-06 | MB | gpt-5.5 | TOKEN | 49 | False | 79 | 79 | None | 32 | 32 | 49 | 7 | 83 | AI_HERD_WRONG |
| 2026-05-06 | MB | gpt-oss-120b | TOKEN | 78 | False | 79 | 79 | None | 32 | 32 | 49 | 7 | 83 |  |
| 2026-05-06 | MB | grok-4.20-multi-agent | TOKEN | 78 | False | 79 | 79 | None | 32 | 32 | 49 | 7 | 83 |  |
| 2026-05-06 | MB | kimi-k2.5 | TOKEN | 49 | False | 79 | 79 | None | 32 | 32 | 49 | 7 | 83 | AI_HERD_WRONG |
| 2026-05-06 | MB | qwen3-coder | TOKEN | 78 | False | 79 | 79 | None | 32 | 32 | 49 | 7 | 83 |  |
| 2026-05-06 | MB | qwen3-max-thinking | TOKEN | 62 | False | 79 | 79 | None | 32 | 32 | 49 | 7 | 83 |  |
| 2026-05-06 | MB | qwen3.6-plus | TOKEN | 49 | False | 79 | 79 | None | 32 | 32 | 49 | 7 | 83 | AI_HERD_WRONG |
| 2026-05-07 | MB | claude-opus-4-20250514 | TOKEN | 37 | False | 20 | 20 | 79 | 20 | 79 | 37 | 5 | 79 | AI_HERD_WRONG,IGNORED_LAG1_EDGE |
| 2026-05-07 | MB | claude-sonnet-4-6 | TOKEN | 37 | False | 20 | 20 | 79 | 20 | 79 | 37 | 5 | 79 | AI_HERD_WRONG,IGNORED_LAG1_EDGE |
| 2026-05-07 | MB | combo-super | TOKEN | 64 | False | 20 | 20 | 79 | 20 | 79 | 37 | 5 | 79 | IGNORED_LAG1_EDGE,PROMPT_CONTEXT_MISSING_TRACE |
| 2026-05-07 | MB | deepseek-reasoner | TOKEN | 20 | False | 20 | 20 | 79 | 20 | 79 | 37 | 5 | 79 | IGNORED_LAG1_EDGE,OFFICIAL_TAIL_OVERWEIGHTED |
| 2026-05-07 | MB | deepseek-v4-flash | TOKEN | 79 | False | 20 | 20 | 79 | 20 | 79 | 37 | 5 | 79 | PICKED_PREVIOUS_OFFICIAL_MISS |
| 2026-05-07 | MB | deepseek-v4-pro | TOKEN | 39 | False | 20 | 20 | 79 | 20 | 79 | 37 | 5 | 79 | IGNORED_LAG1_EDGE |
| 2026-05-07 | MB | gemini-2.5-flash | TOKEN | 20 | False | 20 | 20 | 79 | 20 | 79 | 37 | 5 | 79 | IGNORED_LAG1_EDGE,OFFICIAL_TAIL_OVERWEIGHTED |
| 2026-05-07 | MB | gemini-2.5-pro | TOKEN | 20 | False | 20 | 20 | 79 | 20 | 79 | 37 | 5 | 79 | IGNORED_LAG1_EDGE,OFFICIAL_TAIL_OVERWEIGHTED |
| 2026-05-07 | MB | gemini-3-flash | TOKEN | 87 | False | 20 | 20 | 79 | 20 | 79 | 37 | 5 | 79 | IGNORED_LAG1_EDGE |
| 2026-05-07 | MB | gemini-3.1-pro | TOKEN | 40 | True | 20 | 20 | 79 | 20 | 79 | 37 | 5 | 79 | IGNORED_LAG1_EDGE |
| 2026-05-07 | MB | gemma-4-31b | TOKEN | 32 | False | 20 | 20 | 79 | 20 | 79 | 37 | 5 | 79 | IGNORED_LAG1_EDGE |
| 2026-05-07 | MB | glm-5.1 | TOKEN | 37 | False | 20 | 20 | 79 | 20 | 79 | 37 | 5 | 79 | AI_HERD_WRONG,IGNORED_LAG1_EDGE |
| 2026-05-07 | MB | gpt-5-mini | TOKEN | 04 | False | 20 | 20 | 79 | 20 | 79 | 37 | 5 | 79 | IGNORED_LAG1_EDGE |
| 2026-05-07 | MB | gpt-5.4 | TOKEN | 20 | False | 20 | 20 | 79 | 20 | 79 | 37 | 5 | 79 | IGNORED_LAG1_EDGE,OFFICIAL_TAIL_OVERWEIGHTED |
| 2026-05-07 | MB | gpt-5.5 | TOKEN | 32 | False | 20 | 20 | 79 | 20 | 79 | 37 | 5 | 79 | IGNORED_LAG1_EDGE |
| 2026-05-07 | MB | gpt-oss-120b | TOKEN | 56 | True | 20 | 20 | 79 | 20 | 79 | 37 | 5 | 79 | IGNORED_LAG1_EDGE |
| 2026-05-07 | MB | grok-4.20-multi-agent | TOKEN | 37 | False | 20 | 20 | 79 | 20 | 79 | 37 | 5 | 79 | AI_HERD_WRONG,IGNORED_LAG1_EDGE |
| 2026-05-07 | MB | kimi-k2.5 | TOKEN | 37 | False | 20 | 20 | 79 | 20 | 79 | 37 | 5 | 79 | AI_HERD_WRONG,IGNORED_LAG1_EDGE |
| 2026-05-07 | MB | qwen3-coder | TOKEN | 79 | False | 20 | 20 | 79 | 20 | 79 | 37 | 5 | 79 | PICKED_PREVIOUS_OFFICIAL_MISS |
| 2026-05-07 | MB | qwen3-max-thinking | TOKEN | 32 | False | 20 | 20 | 79 | 20 | 79 | 37 | 5 | 79 | IGNORED_LAG1_EDGE |
| 2026-05-07 | MB | qwen3.6-plus | TOKEN | 75 | False | 20 | 20 | 79 | 20 | 79 | 37 | 5 | 79 | IGNORED_LAG1_EDGE |
