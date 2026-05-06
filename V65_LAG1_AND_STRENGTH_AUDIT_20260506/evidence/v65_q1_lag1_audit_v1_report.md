# V65 Q1 — Lag-1 leakage audit (window: 2026-04-07 .. 2026-05-06)

## A. Per region × model_class summary

| region | class | n_pred | n_N | n_N1 | hit_N_any | hit_N1_any | hit_N2 | hit_N3 | lose_N | lose_N→hit_N1 | lose_N→hit_N2 | lose_N→hit_N3 |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| MB | NO_TOKEN | 210 | 210 | 203 | 108 (51.4%) | 81 (39.9%) | 90 (45.9%) | 93 (49.2%) | 102 | 39 (38.2%) | 42 (41.2%) | 52 (51.0%) |
| MB | TOKEN | 453 | 453 | 432 | 179 (39.5%) | 200 (46.3%) | 178 (43.3%) | 185 (47.1%) | 274 | 116 (42.3%) | 103 (37.6%) | 113 (41.2%) |
| MN | NO_TOKEN | 210 | 210 | 203 | 155 (73.8%) | 150 (73.9%) | 130 (66.3%) | 116 (61.4%) | 55 | 37 (67.3%) | 34 (61.8%) | 32 (58.2%) |
| MN | TOKEN | 451 | 451 | 430 | 329 (72.9%) | 335 (77.9%) | 257 (62.8%) | 263 (67.3%) | 122 | 88 (72.1%) | 75 (61.5%) | 64 (52.5%) |
| MT | NO_TOKEN | 210 | 210 | 203 | 139 (66.2%) | 126 (62.1%) | 123 (62.8%) | 115 (60.8%) | 71 | 43 (60.6%) | 38 (53.5%) | 50 (70.4%) |
| MT | TOKEN | 446 | 446 | 425 | 242 (54.3%) | 246 (57.9%) | 220 (54.5%) | 215 (55.7%) | 204 | 123 (60.3%) | 103 (50.5%) | 102 (50.0%) |

## B. BT (bach-thu) lag-1 specific

| region | class | n_pred | bt_hit_N | bt_hit_N1 | bt_lose_N→bt_hit_N1 |
|---|---|---:|---:|---:|---:|
| MB | NO_TOKEN | 210 | 53 (25.2%) | 48 (23.6%) | 39 (38.2%) |
| MB | TOKEN | 453 | 100 (22.1%) | 117 (27.1%) | 97 (35.4%) |
| MN | NO_TOKEN | 210 | 105 (50.0%) | 98 (48.3%) | 47 (85.5%) |
| MN | TOKEN | 451 | 226 (50.1%) | 251 (58.4%) | 129 (105.7%) |
| MT | NO_TOKEN | 210 | 94 (44.8%) | 78 (38.4%) | 48 (67.6%) |
| MT | TOKEN | 446 | 139 (31.2%) | 162 (38.1%) | 123 (60.3%) |

## C. Per individual model (region × model)

| region | model | class | n_pred | lose_N | lose_N→hit_N1 | hit_N | hit_N1 | bt_lose_N→bt_hit_N1 | bt_hit_N1 |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|
| MN | combo-no-token | NO_TOKEN | 30 | 7 | 5 (71.4%) | 23 | 19 | 7 (100.0%) | 16 |
| MN | combo-super | TOKEN | 30 | 7 | 5 (71.4%) | 23 | 22 | 9 (128.6%) | 18 |
| MN | gemini-2.5-flash | TOKEN | 30 | 8 | 6 (75.0%) | 22 | 24 | 8 (100.0%) | 17 |
| MN | gemini-2.5-pro | TOKEN | 30 | 5 | 3 (60.0%) | 25 | 21 | 6 (120.0%) | 16 |
| MN | gpt-5-mini | TOKEN | 30 | 6 | 3 (50.0%) | 24 | 21 | 7 (116.7%) | 16 |
| MN | gpt-5.4 | TOKEN | 30 | 5 | 3 (60.0%) | 25 | 22 | 9 (180.0%) | 14 |
| MN | lstm | NO_TOKEN | 30 | 8 | 4 (50.0%) | 22 | 19 | 6 (75.0%) | 11 |
| MN | meta-learning | NO_TOKEN | 30 | 8 | 5 (62.5%) | 22 | 23 | 5 (62.5%) | 12 |
| MN | random-forest | NO_TOKEN | 30 | 13 | 9 (69.2%) | 17 | 21 | 5 (38.5%) | 9 |
| MN | smart-ensemble | NO_TOKEN | 30 | 5 | 5 (100.0%) | 25 | 24 | 6 (120.0%) | 15 |
| MN | smart-ml | NO_TOKEN | 30 | 7 | 4 (57.1%) | 23 | 22 | 10 (142.9%) | 20 |
| MN | xgboost | NO_TOKEN | 30 | 7 | 5 (71.4%) | 23 | 22 | 8 (114.3%) | 15 |
| MN | claude-opus-4-20250514 | TOKEN | 29 | 5 | 3 (60.0%) | 24 | 19 | 9 (180.0%) | 15 |
| MN | claude-sonnet-4-6 | TOKEN | 29 | 7 | 6 (85.7%) | 22 | 25 | 7 (100.0%) | 18 |
| MN | deepseek-reasoner | TOKEN | 28 | 9 | 7 (77.8%) | 19 | 20 | 10 (111.1%) | 19 |
| MN | glm-5.1 | TOKEN | 25 | 7 | 6 (85.7%) | 18 | 22 | 8 (114.3%) | 14 |
| MN | grok-4.20-multi-agent | TOKEN | 24 | 8 | 7 (87.5%) | 16 | 17 | 8 (100.0%) | 12 |
| MN | qwen3-coder | TOKEN | 24 | 7 | 4 (57.1%) | 17 | 15 | 7 (100.0%) | 11 |
| MN | kimi-k2.5 | TOKEN | 21 | 7 | 5 (71.4%) | 14 | 15 | 3 (42.9%) | 10 |
| MN | qwen3-max-thinking | TOKEN | 21 | 10 | 8 (80.0%) | 11 | 18 | 7 (70.0%) | 15 |
| MN | gpt-oss-120b | TOKEN | 18 | 5 | 4 (80.0%) | 13 | 11 | 4 (80.0%) | 7 |
| MN | qwen3.6-plus | TOKEN | 13 | 4 | 3 (75.0%) | 9 | 8 | 3 (75.0%) | 6 |
| MN | minimax-m2.7 | TOKEN | 12 | 5 | 4 (80.0%) | 7 | 9 | 4 (80.0%) | 8 |
| MN | deepseek-v4-flash | TOKEN | 10 | 3 | 2 (66.7%) | 7 | 9 | 6 (200.0%) | 8 |
| MN | deepseek-v4-pro | TOKEN | 10 | 3 | 1 (33.3%) | 7 | 7 | 2 (66.7%) | 5 |
| MN | gpt-5.5 | TOKEN | 10 | 1 | 1 (100.0%) | 9 | 8 | 3 (300.0%) | 6 |
| MN | arcee-trinity | TOKEN | 4 | 0 | 0 (—) | 4 | 4 | 0 (—) | 3 |
| MN | llama-4-maverick | TOKEN | 4 | 1 | 0 (0.0%) | 3 | 3 | 1 (100.0%) | 3 |
| MN | mistral-large-3 | TOKEN | 4 | 1 | 1 (100.0%) | 3 | 4 | 2 (200.0%) | 2 |
| MN | mistral-nemo | TOKEN | 4 | 2 | 1 (50.0%) | 2 | 3 | 1 (50.0%) | 1 |
| MN | kimi-k2.6 | TOKEN | 3 | 2 | 2 (100.0%) | 1 | 3 | 1 (50.0%) | 2 |
| MN | nemotron-3-super | TOKEN | 2 | 1 | 1 (100.0%) | 1 | 2 | 1 (100.0%) | 2 |
| MN | gemini-3-flash | TOKEN | 2 | 0 | 0 (—) | 2 | 1 | 1 (—) | 1 |
| MN | gemini-3.1-pro | TOKEN | 2 | 1 | 1 (100.0%) | 1 | 1 | 1 (100.0%) | 1 |
| MN | gemma-4-31b | TOKEN | 2 | 2 | 1 (50.0%) | 0 | 1 | 1 (50.0%) | 1 |
| MT | combo-no-token | NO_TOKEN | 30 | 11 | 7 (63.6%) | 19 | 20 | 5 (45.5%) | 10 |
| MT | combo-super | TOKEN | 30 | 17 | 8 (47.1%) | 13 | 15 | 6 (35.3%) | 11 |
| MT | deepseek-reasoner | TOKEN | 30 | 14 | 9 (64.3%) | 16 | 18 | 10 (71.4%) | 13 |
| MT | gemini-2.5-flash | TOKEN | 30 | 10 | 5 (50.0%) | 20 | 14 | 6 (60.0%) | 9 |
| MT | gemini-2.5-pro | TOKEN | 30 | 15 | 8 (53.3%) | 15 | 15 | 9 (60.0%) | 12 |
| MT | gpt-5-mini | TOKEN | 30 | 14 | 8 (57.1%) | 16 | 14 | 7 (50.0%) | 9 |
| MT | gpt-5.4 | TOKEN | 30 | 16 | 11 (68.8%) | 14 | 17 | 10 (62.5%) | 12 |
| MT | lstm | NO_TOKEN | 30 | 11 | 8 (72.7%) | 19 | 20 | 7 (63.6%) | 13 |
| MT | meta-learning | NO_TOKEN | 30 | 9 | 5 (55.6%) | 21 | 17 | 7 (77.8%) | 11 |
| MT | random-forest | NO_TOKEN | 30 | 10 | 6 (60.0%) | 20 | 18 | 11 (110.0%) | 16 |
| MT | smart-ensemble | NO_TOKEN | 30 | 10 | 7 (70.0%) | 20 | 17 | 7 (70.0%) | 9 |
| MT | smart-ml | NO_TOKEN | 30 | 9 | 6 (66.7%) | 21 | 18 | 7 (77.8%) | 11 |
| MT | xgboost | NO_TOKEN | 30 | 11 | 4 (36.4%) | 19 | 16 | 4 (36.4%) | 8 |
| MT | claude-opus-4-20250514 | TOKEN | 29 | 14 | 4 (28.6%) | 15 | 13 | 6 (42.9%) | 9 |
| MT | claude-sonnet-4-6 | TOKEN | 29 | 16 | 8 (50.0%) | 13 | 15 | 7 (43.8%) | 11 |
| MT | grok-4.20-multi-agent | TOKEN | 24 | 8 | 5 (62.5%) | 16 | 13 | 4 (50.0%) | 7 |
| MT | qwen3-coder | TOKEN | 24 | 10 | 6 (60.0%) | 14 | 15 | 6 (60.0%) | 9 |
| MT | glm-5.1 | TOKEN | 23 | 7 | 6 (85.7%) | 16 | 14 | 6 (85.7%) | 8 |
| MT | kimi-k2.5 | TOKEN | 21 | 9 | 6 (66.7%) | 12 | 12 | 6 (66.7%) | 6 |
| MT | qwen3-max-thinking | TOKEN | 21 | 9 | 7 (77.8%) | 12 | 12 | 8 (88.9%) | 8 |
| MT | gpt-oss-120b | TOKEN | 16 | 7 | 5 (71.4%) | 9 | 10 | 5 (71.4%) | 6 |
| MT | qwen3.6-plus | TOKEN | 13 | 6 | 4 (66.7%) | 7 | 10 | 5 (83.3%) | 6 |
| MT | minimax-m2.7 | TOKEN | 12 | 5 | 4 (80.0%) | 7 | 9 | 5 (100.0%) | 6 |
| MT | deepseek-v4-flash | TOKEN | 10 | 5 | 5 (100.0%) | 5 | 6 | 5 (100.0%) | 5 |
| MT | deepseek-v4-pro | TOKEN | 10 | 7 | 4 (57.1%) | 3 | 6 | 6 (85.7%) | 6 |
| MT | gpt-5.5 | TOKEN | 10 | 5 | 5 (100.0%) | 5 | 7 | 3 (60.0%) | 4 |
| MT | llama-4-maverick | TOKEN | 4 | 3 | 1 (33.3%) | 1 | 2 | 1 (33.3%) | 1 |
| MT | mistral-nemo | TOKEN | 4 | 2 | 2 (100.0%) | 2 | 2 | 0 (0.0%) | 0 |
| MT | arcee-trinity | TOKEN | 3 | 0 | 0 (—) | 3 | 1 | 0 (—) | 0 |
| MT | mistral-large-3 | TOKEN | 3 | 1 | 0 (0.0%) | 2 | 1 | 0 (0.0%) | 1 |
| MT | kimi-k2.6 | TOKEN | 3 | 1 | 0 (0.0%) | 2 | 2 | 1 (100.0%) | 1 |
| MT | gemini-3-flash | TOKEN | 2 | 1 | 1 (100.0%) | 1 | 1 | 0 (0.0%) | 0 |
| MT | gemini-3.1-pro | TOKEN | 2 | 1 | 0 (0.0%) | 1 | 0 | 0 (0.0%) | 0 |
| MT | gemma-4-31b | TOKEN | 2 | 1 | 1 (100.0%) | 1 | 1 | 1 (100.0%) | 1 |
| MT | nemotron-3-super | TOKEN | 1 | 0 | 0 (—) | 1 | 1 | 0 (—) | 1 |
| MB | combo-no-token | NO_TOKEN | 30 | 16 | 6 (37.5%) | 14 | 13 | 4 (25.0%) | 5 |
| MB | combo-super | TOKEN | 30 | 19 | 10 (52.6%) | 11 | 16 | 8 (42.1%) | 9 |
| MB | deepseek-reasoner | TOKEN | 30 | 16 | 6 (37.5%) | 14 | 12 | 6 (37.5%) | 10 |
| MB | gemini-2.5-flash | TOKEN | 30 | 19 | 8 (42.1%) | 11 | 15 | 9 (47.4%) | 10 |
| MB | gemini-2.5-pro | TOKEN | 30 | 21 | 12 (57.1%) | 9 | 15 | 8 (38.1%) | 9 |
| MB | gpt-5-mini | TOKEN | 30 | 15 | 7 (46.7%) | 15 | 15 | 8 (53.3%) | 8 |
| MB | gpt-5.4 | TOKEN | 30 | 18 | 8 (44.4%) | 12 | 12 | 6 (33.3%) | 7 |
| MB | lstm | NO_TOKEN | 30 | 15 | 5 (33.3%) | 15 | 9 | 3 (20.0%) | 5 |
| MB | meta-learning | NO_TOKEN | 30 | 17 | 6 (35.3%) | 13 | 11 | 8 (47.1%) | 8 |
| MB | random-forest | NO_TOKEN | 30 | 11 | 5 (45.5%) | 19 | 11 | 6 (54.5%) | 7 |
| MB | smart-ensemble | NO_TOKEN | 30 | 13 | 6 (46.2%) | 17 | 14 | 6 (46.2%) | 7 |
| MB | smart-ml | NO_TOKEN | 30 | 16 | 5 (31.2%) | 14 | 11 | 7 (43.8%) | 9 |
| MB | xgboost | NO_TOKEN | 30 | 14 | 6 (42.9%) | 16 | 12 | 5 (35.7%) | 7 |
| MB | claude-opus-4-20250514 | TOKEN | 29 | 19 | 7 (36.8%) | 10 | 12 | 6 (31.6%) | 8 |
| MB | claude-sonnet-4-6 | TOKEN | 29 | 18 | 9 (50.0%) | 11 | 15 | 7 (38.9%) | 11 |
| MB | glm-5.1 | TOKEN | 25 | 17 | 5 (29.4%) | 8 | 8 | 4 (23.5%) | 4 |
| MB | grok-4.20-multi-agent | TOKEN | 24 | 13 | 4 (30.8%) | 11 | 9 | 5 (38.5%) | 5 |
| MB | qwen3-coder | TOKEN | 24 | 11 | 4 (36.4%) | 13 | 10 | 4 (36.4%) | 4 |
| MB | qwen3-max-thinking | TOKEN | 21 | 12 | 3 (25.0%) | 9 | 9 | 4 (33.3%) | 4 |
| MB | kimi-k2.5 | TOKEN | 20 | 13 | 8 (61.5%) | 7 | 11 | 7 (53.8%) | 7 |
| MB | gpt-oss-120b | TOKEN | 17 | 13 | 6 (46.2%) | 4 | 7 | 3 (23.1%) | 3 |
| MB | qwen3.6-plus | TOKEN | 13 | 7 | 3 (42.9%) | 6 | 6 | 2 (28.6%) | 3 |
| MB | minimax-m2.7 | TOKEN | 11 | 9 | 2 (22.2%) | 2 | 2 | 1 (11.1%) | 1 |
| MB | deepseek-v4-flash | TOKEN | 10 | 7 | 3 (42.9%) | 3 | 6 | 2 (28.6%) | 4 |
| MB | deepseek-v4-pro | TOKEN | 10 | 5 | 2 (40.0%) | 5 | 4 | 2 (40.0%) | 2 |
| MB | gpt-5.5 | TOKEN | 10 | 5 | 4 (80.0%) | 5 | 7 | 2 (40.0%) | 4 |
| MB | arcee-trinity | TOKEN | 6 | 5 | 2 (40.0%) | 1 | 2 | 1 (20.0%) | 1 |
| MB | llama-4-maverick | TOKEN | 4 | 1 | 0 (0.0%) | 3 | 0 | 0 (0.0%) | 0 |
| MB | mistral-large-3 | TOKEN | 4 | 1 | 0 (0.0%) | 3 | 2 | 0 (0.0%) | 1 |
| MB | mistral-nemo | TOKEN | 4 | 3 | 2 (66.7%) | 1 | 2 | 1 (33.3%) | 1 |
| MB | kimi-k2.6 | TOKEN | 4 | 2 | 1 (50.0%) | 2 | 1 | 0 (0.0%) | 0 |
| MB | nemotron-3-super | TOKEN | 2 | 2 | 0 (0.0%) | 0 | 0 | 0 (0.0%) | 0 |
| MB | gemini-3-flash | TOKEN | 2 | 1 | 0 (0.0%) | 1 | 0 | 0 (0.0%) | 0 |
| MB | gemini-3.1-pro | TOKEN | 2 | 1 | 0 (0.0%) | 1 | 1 | 1 (100.0%) | 1 |
| MB | gemma-4-31b | TOKEN | 2 | 1 | 0 (0.0%) | 1 | 1 | 0 (0.0%) | 0 |

## D. Examples (lose_N then hit_N1)

### MB / NO_TOKEN
- 2026-04-07 model=combo-no-token picks=['23', '26'] → on 2026-04-08 matched ['26']
- 2026-04-07 model=meta-learning picks=['26', '23'] → on 2026-04-08 matched ['26']
- 2026-04-07 model=random-forest picks=['50', '23'] → on 2026-04-08 matched ['50']
- 2026-04-07 model=smart-ensemble picks=['23', '26'] → on 2026-04-08 matched ['26']
- 2026-04-07 model=smart-ml picks=['78', '23'] → on 2026-04-08 matched ['78']
- 2026-04-07 model=xgboost picks=['50', '23'] → on 2026-04-08 matched ['50']

### MN / TOKEN
- 2026-04-07 model=deepseek-reasoner picks=['64', '65'] → on 2026-04-08 matched ['64']
- 2026-04-09 model=gemini-2.5-flash picks=['97', '32'] → on 2026-04-10 matched ['32']
- 2026-04-13 model=gpt-5-mini picks=['24', '39'] → on 2026-04-14 matched ['24']
- 2026-04-14 model=qwen3.6-plus picks=['02', '64'] → on 2026-04-15 matched ['64']
- 2026-04-15 model=claude-sonnet-4-6 picks=['42', '10'] → on 2026-04-16 matched ['42']
- 2026-04-15 model=deepseek-reasoner picks=['42', '33'] → on 2026-04-16 matched ['33', '42']

### MT / NO_TOKEN
- 2026-04-07 model=combo-no-token picks=['28', '01'] → on 2026-04-08 matched ['01']
- 2026-04-07 model=lstm picks=['01', '80'] → on 2026-04-08 matched ['01']
- 2026-04-07 model=xgboost picks=['01', '25'] → on 2026-04-08 matched ['01']
- 2026-04-08 model=lstm picks=['95', '49'] → on 2026-04-09 matched ['95']
- 2026-04-10 model=random-forest picks=['23', '72'] → on 2026-04-11 matched ['23']
- 2026-04-10 model=smart-ml picks=['23', '50'] → on 2026-04-11 matched ['23']

### MB / TOKEN
- 2026-04-08 model=claude-opus-4-20250514 picks=['37'] → on 2026-04-09 matched ['37']
- 2026-04-08 model=claude-sonnet-4-6 picks=['37'] → on 2026-04-09 matched ['37']
- 2026-04-08 model=combo-super picks=['37', '08'] → on 2026-04-09 matched ['08', '37']
- 2026-04-08 model=deepseek-reasoner picks=['37', '79'] → on 2026-04-09 matched ['37', '79']
- 2026-04-08 model=gemini-2.5-flash picks=['37', '13'] → on 2026-04-09 matched ['37']
- 2026-04-08 model=gemini-2.5-pro picks=['37', '73'] → on 2026-04-09 matched ['37', '73']

### MT / TOKEN
- 2026-04-08 model=combo-super picks=['18', '39'] → on 2026-04-09 matched ['39']
- 2026-04-08 model=gpt-5.4 picks=['24', '18'] → on 2026-04-09 matched ['24']
- 2026-04-09 model=gemini-2.5-pro picks=['10', '01'] → on 2026-04-10 matched ['01', '10']
- 2026-04-09 model=gpt-5.4 picks=['78', '10'] → on 2026-04-10 matched ['10']
- 2026-04-10 model=gpt-5-mini picks=['34', '68'] → on 2026-04-11 matched ['68']
- 2026-04-11 model=claude-sonnet-4-6 picks=['16', '39'] → on 2026-04-12 matched ['39']

### MN / NO_TOKEN
- 2026-04-09 model=random-forest picks=['32', '44'] → on 2026-04-10 matched ['32']
- 2026-04-11 model=random-forest picks=['42', '10'] → on 2026-04-12 matched ['10']
- 2026-04-12 model=lstm picks=['45', '14'] → on 2026-04-13 matched ['14']
- 2026-04-12 model=smart-ensemble picks=['45', '14'] → on 2026-04-13 matched ['14']
- 2026-04-14 model=combo-no-token picks=['63', '46'] → on 2026-04-15 matched ['63']
- 2026-04-15 model=combo-no-token picks=['98', '24'] → on 2026-04-16 matched ['98']
