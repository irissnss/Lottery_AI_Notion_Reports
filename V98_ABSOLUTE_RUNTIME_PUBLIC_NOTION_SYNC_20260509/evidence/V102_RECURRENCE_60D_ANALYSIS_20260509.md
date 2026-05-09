# V102 Recurrence 60D Analysis — D-1 Lost Signal Persistence

**DB source:** live sync manifest `artifacts\live_sync\20260509_212533\manifest.json`
**Window:** 2026-03-10 → 2026-05-08 with D+1 through 2026-05-09

## 1. Same-Region D Lost → D+1 Hit (ANY-PRIZE diagnostic)

| Region | Source | n lost_any | hit D+1 any | rate | baseline | lift |
|---|---|---:|---:|---:|---:|---:|
| MB | V73 | 5 | 2 | 40.0% | 23.8% | +16.2pp |
| MB | V67 | 8 | 3 | 37.5% | 24.5% | +13.0pp |
| MB | V70 | 11 | 4 | 36.4% | 23.9% | +12.5pp |
| MB | OFFICIAL_LO2 | 91 | 28 | 30.8% | 23.8% | +6.9pp |
| MB | TEST_BT | 53 | 16 | 30.2% | 23.6% | +6.6pp |
| MB | TEST_LO2 | 67 | 20 | 29.9% | 23.6% | +6.3pp |
| MB | OFFICIAL_BT | 45 | 13 | 28.9% | 23.8% | +5.1pp |
| MB | MODEL_MAIN | 663 | 173 | 26.1% | 23.8% | +2.3pp |
| MN | V70 | 6 | 5 | 83.3% | 44.0% | +39.3pp |
| MN | TEST_LO2 | 36 | 25 | 69.4% | 43.5% | +25.9pp |
| MN | TEST_BT | 21 | 14 | 66.7% | 44.0% | +22.7pp |
| MN | V101_MN_D1_D2 | 66 | 39 | 59.1% | 42.9% | +16.2pp |
| MN | OFFICIAL_LO2 | 64 | 37 | 57.8% | 43.5% | +14.4pp |
| MN | OFFICIAL_BT | 33 | 15 | 45.5% | 43.8% | +1.7pp |
| MN | MODEL_MAIN | 455 | 205 | 45.1% | 43.5% | +1.6pp |
| MT | OFFICIAL_BT | 30 | 15 | 50.0% | 37.0% | +13.0pp |
| MT | OFFICIAL_LO2 | 65 | 30 | 46.2% | 36.7% | +9.5pp |
| MT | TEST_BT | 52 | 23 | 44.2% | 36.4% | +7.9pp |
| MT | TEST_LO2 | 67 | 29 | 43.3% | 36.2% | +7.1pp |
| MT | MODEL_MAIN | 543 | 203 | 37.4% | 35.5% | +1.9pp |

## 2. Same-Region D Lost → D+1 Strict ĐB Hit

| Region | Source | n lost_strict | hit D+1 strict | rate | baseline | lift |
|---|---|---:|---:|---:|---:|---:|
| MB | V73 | 5 | 1 | 20.0% | 1.0% | +19.0pp |
| MB | V70 | 13 | 1 | 7.7% | 1.0% | +6.7pp |
| MB | OFFICIAL_BT | 59 | 2 | 3.4% | 1.0% | +2.4pp |
| MB | OFFICIAL_LO2 | 118 | 4 | 3.4% | 1.0% | +2.4pp |
| MB | TEST_BT | 69 | 2 | 2.9% | 1.0% | +1.9pp |
| MB | TEST_LO2 | 87 | 2 | 2.3% | 1.0% | +1.3pp |
| MB | MODEL_MAIN | 890 | 13 | 1.5% | 1.0% | +0.5pp |
| MB | V67 | 10 | 0 | 0.0% | 1.0% | -1.0pp |
| MN | V101_MN_D1_D2 | 125 | 5 | 4.0% | 3.2% | +0.8pp |
| MN | MODEL_MAIN | 800 | 22 | 2.8% | 3.2% | -0.4pp |
| MN | OFFICIAL_LO2 | 117 | 1 | 0.9% | 3.1% | -2.3pp |
| MN | TEST_BT | 45 | 0 | 0.0% | 3.1% | -3.1pp |
| MN | OFFICIAL_BT | 58 | 0 | 0.0% | 3.1% | -3.1pp |
| MN | TEST_LO2 | 75 | 0 | 0.0% | 3.2% | -3.2pp |
| MN | V73 | 5 | 0 | 0.0% | 3.2% | -3.2pp |
| MN | V70 | 9 | 0 | 0.0% | 3.2% | -3.2pp |
| MN | V67 | 6 | 0 | 0.0% | 3.5% | -3.5pp |
| MT | TEST_LO2 | 112 | 2 | 1.8% | 2.4% | -0.6pp |
| MT | OFFICIAL_LO2 | 118 | 2 | 1.7% | 2.4% | -0.7pp |
| MT | OFFICIAL_BT | 59 | 1 | 1.7% | 2.4% | -0.7pp |
| MT | MODEL_MAIN | 846 | 12 | 1.4% | 2.4% | -1.0pp |
| MT | TEST_BT | 82 | 1 | 1.2% | 2.4% | -1.2pp |
| MT | V67 | 6 | 0 | 0.0% | 2.3% | -2.3pp |
| MT | V70 | 14 | 0 | 0.0% | 2.4% | -2.4pp |
| MT | V73 | 5 | 0 | 0.0% | 2.4% | -2.4pp |

## 3. Cross-Region Same-Day Downstream Lost → Hit (ANY-PRIZE)

| Pair | Source | n lost_any | hit downstream same-day | rate | baseline | lift |
|---|---|---:|---:|---:|---:|---:|
| MN->MB | V70 | 6 | 4 | 66.7% | 23.7% | +43.0pp |
| MN->MB | V101_MN_D1_D2 | 66 | 26 | 39.4% | 23.8% | +15.6pp |
| MN->MB | OFFICIAL_BT | 33 | 11 | 33.3% | 24.0% | +9.3pp |
| MN->MB | TEST_BT | 21 | 7 | 33.3% | 24.1% | +9.2pp |
| MN->MB | OFFICIAL_LO2 | 64 | 18 | 28.1% | 23.9% | +4.2pp |
| MN->MB | TEST_LO2 | 36 | 10 | 27.8% | 23.9% | +3.8pp |
| MN->MB | MODEL_MAIN | 455 | 113 | 24.8% | 23.8% | +1.0pp |
| MN->MT | OFFICIAL_BT | 33 | 13 | 39.4% | 34.0% | +5.4pp |
| MN->MT | OFFICIAL_LO2 | 64 | 24 | 37.5% | 33.8% | +3.7pp |
| MN->MT | TEST_LO2 | 36 | 13 | 36.1% | 34.0% | +2.1pp |
| MN->MT | V70 | 6 | 2 | 33.3% | 31.8% | +1.5pp |
| MN->MT | TEST_BT | 21 | 7 | 33.3% | 34.1% | -0.8pp |
| MN->MT | MODEL_MAIN | 455 | 144 | 31.6% | 34.5% | -2.8pp |
| MN->MT | V101_MN_D1_D2 | 66 | 19 | 28.8% | 33.7% | -4.9pp |
| MT->MB | OFFICIAL_BT | 30 | 8 | 26.7% | 23.9% | +2.8pp |
| MT->MB | MODEL_MAIN | 543 | 128 | 23.6% | 23.7% | -0.2pp |
| MT->MB | OFFICIAL_LO2 | 65 | 15 | 23.1% | 23.8% | -0.8pp |
| MT->MB | TEST_LO2 | 67 | 15 | 22.4% | 23.8% | -1.4pp |
| MT->MB | TEST_BT | 52 | 11 | 21.2% | 23.8% | -2.6pp |

## 4. Cross-Region Next-Day Lost → Hit (ANY-PRIZE)

| Pair | Source | n lost_any | hit dst D+1 | rate | baseline | lift |
|---|---|---:|---:|---:|---:|---:|
| MB->MN | OFFICIAL_LO2 | 91 | 46 | 50.5% | 43.6% | +6.9pp |
| MB->MN | V67 | 8 | 4 | 50.0% | 44.0% | +6.0pp |
| MB->MN | MODEL_MAIN | 663 | 318 | 48.0% | 43.2% | +4.8pp |
| MB->MN | V70 | 11 | 5 | 45.5% | 42.6% | +2.8pp |
| MB->MN | TEST_LO2 | 67 | 29 | 43.3% | 43.6% | -0.3pp |
| MB->MN | OFFICIAL_BT | 45 | 19 | 42.2% | 43.6% | -1.3pp |
| MB->MN | V73 | 5 | 2 | 40.0% | 42.2% | -2.2pp |
| MB->MN | TEST_BT | 53 | 21 | 39.6% | 43.8% | -4.2pp |
| MB->MT | OFFICIAL_BT | 45 | 22 | 48.9% | 35.7% | +13.2pp |
| MB->MT | OFFICIAL_LO2 | 91 | 37 | 40.7% | 35.7% | +5.0pp |
| MB->MT | V73 | 5 | 2 | 40.0% | 35.2% | +4.8pp |
| MB->MT | TEST_BT | 53 | 20 | 37.7% | 35.8% | +2.0pp |
| MB->MT | TEST_LO2 | 67 | 25 | 37.3% | 35.6% | +1.7pp |
| MB->MT | MODEL_MAIN | 663 | 234 | 35.3% | 35.2% | +0.1pp |
| MB->MT | V70 | 11 | 3 | 27.3% | 35.8% | -8.5pp |
| MB->MT | V67 | 8 | 2 | 25.0% | 37.0% | -12.0pp |
| MN->MB | V70 | 6 | 3 | 50.0% | 23.8% | +26.2pp |
| MN->MB | OFFICIAL_BT | 33 | 12 | 36.4% | 23.9% | +12.5pp |
| MN->MB | OFFICIAL_LO2 | 64 | 18 | 28.1% | 23.9% | +4.2pp |
| MN->MB | TEST_LO2 | 36 | 10 | 27.8% | 23.7% | +4.1pp |
| MN->MB | MODEL_MAIN | 455 | 120 | 26.4% | 23.8% | +2.5pp |
| MN->MB | TEST_BT | 21 | 5 | 23.8% | 23.9% | -0.0pp |
| MN->MB | V101_MN_D1_D2 | 66 | 12 | 18.2% | 23.7% | -5.5pp |
| MN->MT | OFFICIAL_BT | 33 | 18 | 54.5% | 37.9% | +16.6pp |
| MN->MT | TEST_BT | 21 | 10 | 47.6% | 38.7% | +8.9pp |
| MN->MT | OFFICIAL_LO2 | 64 | 29 | 45.3% | 36.6% | +8.7pp |
| MN->MT | MODEL_MAIN | 455 | 178 | 39.1% | 35.6% | +3.5pp |
| MN->MT | V101_MN_D1_D2 | 66 | 24 | 36.4% | 34.4% | +1.9pp |
| MN->MT | TEST_LO2 | 36 | 14 | 38.9% | 37.3% | +1.6pp |
| MN->MT | V70 | 6 | 1 | 16.7% | 36.5% | -19.8pp |
| MT->MB | TEST_LO2 | 67 | 20 | 29.9% | 23.7% | +6.1pp |
| MT->MB | TEST_BT | 52 | 14 | 26.9% | 23.7% | +3.2pp |
| MT->MB | OFFICIAL_LO2 | 65 | 16 | 24.6% | 24.0% | +0.6pp |
| MT->MB | MODEL_MAIN | 543 | 128 | 23.6% | 23.8% | -0.3pp |
| MT->MB | OFFICIAL_BT | 30 | 6 | 20.0% | 23.8% | -3.8pp |
| MT->MN | MODEL_MAIN | 543 | 243 | 44.8% | 43.4% | +1.4pp |
| MT->MN | TEST_LO2 | 67 | 29 | 43.3% | 43.4% | -0.1pp |
| MT->MN | OFFICIAL_BT | 30 | 13 | 43.3% | 44.4% | -1.1pp |
| MT->MN | TEST_BT | 52 | 21 | 40.4% | 43.8% | -3.4pp |
| MT->MN | OFFICIAL_LO2 | 65 | 26 | 40.0% | 43.8% | -3.8pp |

## 5. AI Model Same-Region Recurrence Watchlist (ANY-PRIZE, n>=20)

| Region | Model | n lost_any | hit D+1 any | rate | baseline | lift |
|---|---|---:|---:|---:|---:|---:|
| MN | grok-4.20-multi-agent | 29 | 20 | 69.0% | 43.5% | +25.5pp |
| MT | smart-ensemble | 61 | 32 | 52.5% | 35.5% | +16.9pp |
| MN | gpt-oss-120b | 20 | 12 | 60.0% | 44.0% | +16.0pp |
| MT | gpt-oss-120b | 22 | 11 | 50.0% | 34.2% | +15.8pp |
| MN | gpt-5.4 | 46 | 27 | 58.7% | 44.1% | +14.6pp |
| MB | kimi-k2.5 | 34 | 13 | 38.2% | 23.9% | +14.4pp |
| MN | glm-5.1 | 28 | 16 | 57.1% | 42.9% | +14.3pp |
| MN | qwen3-max-thinking | 28 | 16 | 57.1% | 43.3% | +13.8pp |
| MT | qwen3.6-plus | 23 | 11 | 47.8% | 34.7% | +13.1pp |
| MN | claude-opus-4-20250514 | 53 | 30 | 56.6% | 43.7% | +12.9pp |
| MN | deepseek-reasoner | 57 | 32 | 56.1% | 43.4% | +12.7pp |
| MB | gemini-2.5-flash | 95 | 32 | 33.7% | 23.9% | +9.8pp |
| MN | claude-sonnet-4-6 | 58 | 31 | 53.4% | 44.0% | +9.5pp |
| MN | gemini-2.5-flash | 62 | 33 | 53.2% | 43.8% | +9.5pp |
| MT | combo-no-token | 71 | 32 | 45.1% | 35.8% | +9.3pp |
| MT | qwen3-max-thinking | 29 | 13 | 44.8% | 36.0% | +8.8pp |
| MB | gpt-oss-120b | 28 | 9 | 32.1% | 23.6% | +8.6pp |
| MN | smart-ml | 70 | 36 | 51.4% | 43.1% | +8.3pp |
| MT | qwen3-coder | 35 | 15 | 42.9% | 34.7% | +8.1pp |
| MT | glm-5.1 | 32 | 14 | 43.8% | 35.8% | +7.9pp |
| MT | gpt-5-mini | 73 | 32 | 43.8% | 36.0% | +7.8pp |
| MN | xgboost | 63 | 32 | 50.8% | 43.4% | +7.4pp |
| MT | deepseek-reasoner | 69 | 30 | 43.5% | 36.2% | +7.2pp |
| MB | claude-sonnet-4-6 | 68 | 21 | 30.9% | 23.8% | +7.1pp |
| MT | meta-learning | 58 | 25 | 43.1% | 36.2% | +6.9pp |
| MT | smart-ml | 67 | 29 | 43.3% | 36.6% | +6.7pp |
| MN | gemini-2.5-pro | 58 | 29 | 50.0% | 43.5% | +6.5pp |
| MN | qwen3-coder | 30 | 15 | 50.0% | 43.6% | +6.4pp |
| MB | gemini-2.5-pro | 93 | 28 | 30.1% | 23.9% | +6.2pp |
| MT | random-forest | 69 | 29 | 42.0% | 35.9% | +6.1pp |
| MB | qwen3-coder | 37 | 11 | 29.7% | 23.8% | +6.0pp |
| MN | combo-super | 71 | 35 | 49.3% | 43.8% | +5.5pp |
| MB | gpt-5-mini | 89 | 26 | 29.2% | 23.8% | +5.4pp |
| MB | combo-super | 104 | 30 | 28.8% | 23.8% | +5.0pp |
| MT | claude-opus-4-20250514 | 60 | 24 | 40.0% | 35.3% | +4.7pp |
| MB | claude-opus-4-20250514 | 75 | 21 | 28.0% | 23.9% | +4.1pp |
| MN | lstm | 66 | 31 | 47.0% | 42.9% | +4.1pp |
| MT | lstm | 75 | 29 | 38.7% | 34.8% | +3.9pp |
| MB | deepseek-reasoner | 76 | 21 | 27.6% | 23.9% | +3.7pp |
| MT | claude-sonnet-4-6 | 72 | 28 | 38.9% | 35.3% | +3.6pp |
| MB | smart-ensemble | 91 | 25 | 27.5% | 23.9% | +3.5pp |
| MB | qwen3.6-plus | 22 | 6 | 27.3% | 23.8% | +3.5pp |
| MT | kimi-k2.5 | 31 | 12 | 38.7% | 35.4% | +3.3pp |
| MT | gemini-2.5-pro | 83 | 32 | 38.6% | 35.9% | +2.7pp |
| MB | grok-4.20-multi-agent | 38 | 10 | 26.3% | 23.9% | +2.4pp |
| MB | meta-learning | 93 | 24 | 25.8% | 23.9% | +1.9pp |
| MB | combo-no-token | 94 | 24 | 25.5% | 23.8% | +1.7pp |
| MB | xgboost | 94 | 24 | 25.5% | 23.9% | +1.6pp |
| MN | gpt-5-mini | 62 | 28 | 45.2% | 43.7% | +1.5pp |
| MB | smart-ml | 83 | 21 | 25.3% | 23.9% | +1.4pp |
| MB | gpt-5.4 | 68 | 17 | 25.0% | 23.6% | +1.4pp |
| MT | xgboost | 73 | 27 | 37.0% | 35.8% | +1.2pp |
| MT | gpt-5.4 | 63 | 24 | 38.1% | 37.1% | +1.0pp |
| MB | random-forest | 90 | 22 | 24.4% | 23.9% | +0.6pp |
| MB | glm-5.1 | 43 | 10 | 23.3% | 23.6% | -0.4pp |
| MN | smart-ensemble | 65 | 28 | 43.1% | 43.5% | -0.4pp |
| MN | meta-learning | 66 | 28 | 42.4% | 43.3% | -0.9pp |
| MN | combo-no-token | 70 | 29 | 41.4% | 43.4% | -2.0pp |
| MN | random-forest | 73 | 30 | 41.1% | 43.2% | -2.1pp |
| MT | grok-4.20-multi-agent | 29 | 10 | 34.5% | 36.7% | -2.2pp |
| MB | qwen3-max-thinking | 34 | 7 | 20.6% | 23.7% | -3.1pp |
| MT | gemini-2.5-flash | 75 | 24 | 32.0% | 36.1% | -4.1pp |
| MB | lstm | 88 | 17 | 19.3% | 23.9% | -4.6pp |
| MT | combo-super | 87 | 27 | 31.0% | 35.9% | -4.9pp |
| MN | kimi-k2.5 | 27 | 9 | 33.3% | 43.6% | -10.3pp |

## 6. Examples

### MB / MODEL::arcee-trinity / same_any
- 2026-04-17 tail `54` labels=['1'] → hit on 2026-04-18
- 2026-04-21 tail `91` labels=['0'] → hit on 2026-04-22

### MB / MODEL::claude-opus-4-20250514 / same_any
- 2026-03-11 tail `59` labels=['0'] → hit on 2026-03-12
- 2026-03-12 tail `68` labels=['1'] → hit on 2026-03-13
- 2026-03-13 tail `41` labels=['0'] → hit on 2026-03-14
- 2026-03-19 tail `57` labels=['0'] → hit on 2026-03-20
- 2026-03-19 tail `32` labels=['1'] → hit on 2026-03-20

### MB / MODEL::claude-opus-4-20250514 / same_strict
- 2026-05-05 tail `41` labels=['0'] → hit on 2026-05-06

### MB / MODEL::claude-sonnet-4-6 / same_any
- 2026-03-13 tail `41` labels=['0'] → hit on 2026-03-14
- 2026-03-17 tail `81` labels=['0'] → hit on 2026-03-18
- 2026-03-19 tail `32` labels=['0'] → hit on 2026-03-20
- 2026-03-20 tail `92` labels=['0'] → hit on 2026-03-21
- 2026-03-21 tail `91` labels=['0'] → hit on 2026-03-22

### MB / MODEL::claude-sonnet-4-6 / same_strict
- 2026-03-30 tail `91` labels=['0'] → hit on 2026-03-31
- 2026-05-05 tail `41` labels=['0'] → hit on 2026-05-06

### MB / MODEL::combo-no-token / same_any
- 2026-03-10 tail `68` labels=['0'] → hit on 2026-03-11
- 2026-03-11 tail `04` labels=['1'] → hit on 2026-03-12
- 2026-03-13 tail `23` labels=['0'] → hit on 2026-03-14
- 2026-03-13 tail `14` labels=['1'] → hit on 2026-03-14
- 2026-03-14 tail `76` labels=['0'] → hit on 2026-03-15

### MB / MODEL::combo-no-token / same_strict
- 2026-03-10 tail `68` labels=['0'] → hit on 2026-03-11
- 2026-04-01 tail `67` labels=['0'] → hit on 2026-04-02
- 2026-04-17 tail `43` labels=['0'] → hit on 2026-04-18

### MB / MODEL::combo-super / same_any
- 2026-03-10 tail `68` labels=['0'] → hit on 2026-03-11
- 2026-03-11 tail `04` labels=['2'] → hit on 2026-03-12
- 2026-03-14 tail `80` labels=['0'] → hit on 2026-03-15
- 2026-03-15 tail `46` labels=['2'] → hit on 2026-03-16
- 2026-03-19 tail `32` labels=['2'] → hit on 2026-03-20

### MB / MODEL::combo-super / same_strict
- 2026-03-10 tail `68` labels=['0'] → hit on 2026-03-11
- 2026-04-03 tail `37` labels=['1'] → hit on 2026-04-04
- 2026-04-11 tail `00` labels=['0'] → hit on 2026-04-12
- 2026-05-05 tail `41` labels=['0'] → hit on 2026-05-06

### MB / MODEL::deepseek-chat / same_any
- 2026-03-10 tail `96` labels=['1'] → hit on 2026-03-11
- 2026-03-13 tail `41` labels=['1'] → hit on 2026-03-14
- 2026-03-17 tail `64` labels=['1'] → hit on 2026-03-18
- 2026-03-19 tail `57` labels=['0'] → hit on 2026-03-20
- 2026-03-21 tail `91` labels=['0'] → hit on 2026-03-22

### MB / MODEL::deepseek-reasoner / same_any
- 2026-03-13 tail `41` labels=['1'] → hit on 2026-03-14
- 2026-03-17 tail `64` labels=['1'] → hit on 2026-03-18
- 2026-03-19 tail `57` labels=['0'] → hit on 2026-03-20
- 2026-03-23 tail `64` labels=['0'] → hit on 2026-03-24
- 2026-03-25 tail `49` labels=['0'] → hit on 2026-03-26

### MB / MODEL::deepseek-reasoner / same_strict
- 2026-03-30 tail `91` labels=['1'] → hit on 2026-03-31

### MB / MODEL::deepseek-v4-flash / same_any
- 2026-04-29 tail `79` labels=['1'] → hit on 2026-04-30
- 2026-04-30 tail `46` labels=['0'] → hit on 2026-05-01
- 2026-04-30 tail `91` labels=['1'] → hit on 2026-05-01
- 2026-05-03 tail `14` labels=['1'] → hit on 2026-05-04
- 2026-05-05 tail `09` labels=['0'] → hit on 2026-05-06

### MB / MODEL::deepseek-v4-pro / same_any
- 2026-04-29 tail `79` labels=['0'] → hit on 2026-04-30
- 2026-05-01 tail `57` labels=['1'] → hit on 2026-05-02
- 2026-05-03 tail `30` labels=['1'] → hit on 2026-05-04
- 2026-05-05 tail `09` labels=['0'] → hit on 2026-05-06
- 2026-05-06 tail `49` labels=['0'] → hit on 2026-05-07

### MB / MODEL::gemini-2.5-flash / same_any
- 2026-03-13 tail `41` labels=['1'] → hit on 2026-03-14
- 2026-03-17 tail `64` labels=['1'] → hit on 2026-03-18
- 2026-03-18 tail `50` labels=['0'] → hit on 2026-03-19
- 2026-03-19 tail `57` labels=['0'] → hit on 2026-03-20
- 2026-03-20 tail `26` labels=['0'] → hit on 2026-03-21

### MB / MODEL::gemini-2.5-flash / same_strict
- 2026-03-30 tail `91` labels=['1'] → hit on 2026-03-31
- 2026-05-05 tail `41` labels=['0'] → hit on 2026-05-06

### MB / MODEL::gemini-2.5-pro / same_any
- 2026-03-13 tail `41` labels=['0'] → hit on 2026-03-14
- 2026-03-19 tail `57` labels=['1'] → hit on 2026-03-20
- 2026-03-21 tail `91` labels=['0'] → hit on 2026-03-22
- 2026-03-21 tail `46` labels=['1'] → hit on 2026-03-22
- 2026-03-22 tail `92` labels=['1'] → hit on 2026-03-23

### MB / MODEL::gemini-2.5-pro / same_strict
- 2026-03-21 tail `46` labels=['1'] → hit on 2026-03-22
- 2026-05-05 tail `41` labels=['0'] → hit on 2026-05-06

### MB / MODEL::gemini-3-flash / same_any
- 2026-05-06 tail `49` labels=['1'] → hit on 2026-05-07
- 2026-05-07 tail `87` labels=['0'] → hit on 2026-05-08
- 2026-05-08 tail `37` labels=['0'] → hit on 2026-05-09

### MB / MODEL::gemini-3.1-pro / same_any
- 2026-05-05 tail `90` labels=['0'] → hit on 2026-05-06
- 2026-05-06 tail `49` labels=['0'] → hit on 2026-05-07

### MB / MODEL::gemma-4-31b / same_any
- 2026-05-05 tail `09` labels=['1'] → hit on 2026-05-06
- 2026-05-06 tail `49` labels=['0'] → hit on 2026-05-07

### MB / MODEL::glm-5.1 / same_any
- 2026-04-17 tail `54` labels=['0'] → hit on 2026-04-18
- 2026-04-21 tail `91` labels=['1'] → hit on 2026-04-22
- 2026-04-22 tail `22` labels=['0'] → hit on 2026-04-23
- 2026-04-22 tail `84` labels=['1'] → hit on 2026-04-23
- 2026-05-01 tail `73` labels=['1'] → hit on 2026-05-02

### MB / MODEL::glm-5.1 / same_strict
- 2026-05-05 tail `41` labels=['0'] → hit on 2026-05-06

### MB / MODEL::gpt-5-mini / same_any
- 2026-03-17 tail `64` labels=['0'] → hit on 2026-03-18
- 2026-03-19 tail `57` labels=['0'] → hit on 2026-03-20
- 2026-03-20 tail `92` labels=['1'] → hit on 2026-03-21
- 2026-03-22 tail `69` labels=['1'] → hit on 2026-03-23
- 2026-03-28 tail `31` labels=['1'] → hit on 2026-03-29

### MB / MODEL::gpt-5-mini / same_strict
- 2026-03-30 tail `91` labels=['1'] → hit on 2026-03-31
- 2026-04-11 tail `00` labels=['0'] → hit on 2026-04-12

### MB / MODEL::gpt-5.4 / same_any
- 2026-03-24 tail `66` labels=['1'] → hit on 2026-03-25
- 2026-03-25 tail `49` labels=['0'] → hit on 2026-03-26
- 2026-03-29 tail `38` labels=['0'] → hit on 2026-03-30
- 2026-04-01 tail `39` labels=['0'] → hit on 2026-04-02
- 2026-04-07 tail `41` labels=['1'] → hit on 2026-04-08

### MB / MODEL::gpt-5.4 / same_strict
- 2026-05-05 tail `41` labels=['1'] → hit on 2026-05-06

### MB / MODEL::gpt-5.5 / same_any
- 2026-04-29 tail `79` labels=['1'] → hit on 2026-04-30
- 2026-04-30 tail `46` labels=['0'] → hit on 2026-05-01
- 2026-04-30 tail `32` labels=['1'] → hit on 2026-05-01
- 2026-05-01 tail `38` labels=['1'] → hit on 2026-05-02
- 2026-05-02 tail `68` labels=['1'] → hit on 2026-05-03

### MB / MODEL::gpt-oss-120b / same_any
- 2026-04-21 tail `91` labels=['1'] → hit on 2026-04-22
- 2026-04-22 tail `22` labels=['0'] → hit on 2026-04-23
- 2026-04-22 tail `84` labels=['1'] → hit on 2026-04-23
- 2026-04-24 tail `48` labels=['1'] → hit on 2026-04-25
- 2026-04-25 tail `05` labels=['0'] → hit on 2026-04-26

### MB / MODEL::grok-4.20-multi-agent / same_any
- 2026-04-17 tail `73` labels=['1'] → hit on 2026-04-18
- 2026-04-22 tail `22` labels=['0'] → hit on 2026-04-23
- 2026-04-23 tail `28` labels=['0'] → hit on 2026-04-24
- 2026-04-24 tail `48` labels=['1'] → hit on 2026-04-25
- 2026-04-30 tail `46` labels=['0'] → hit on 2026-05-01

### MB / MODEL::grok-4.20-multi-agent / same_strict
- 2026-05-05 tail `41` labels=['0'] → hit on 2026-05-06

### MB / MODEL::kimi-k2.5 / same_any
- 2026-04-17 tail `73` labels=['0'] → hit on 2026-04-18
- 2026-04-18 tail `94` labels=['0'] → hit on 2026-04-19
- 2026-04-22 tail `22` labels=['0'] → hit on 2026-04-23
- 2026-04-23 tail `28` labels=['1'] → hit on 2026-04-24
- 2026-04-30 tail `46` labels=['0'] → hit on 2026-05-01

### MB / MODEL::kimi-k2.5 / same_strict
- 2026-05-05 tail `41` labels=['0'] → hit on 2026-05-06

### MB / MODEL::kimi-k2.6 / same_any
- 2026-04-23 tail `28` labels=['1'] → hit on 2026-04-24

### MB / MODEL::lstm / same_any
- 2026-03-12 tail `00` labels=['1'] → hit on 2026-03-13
- 2026-03-20 tail `34` labels=['0'] → hit on 2026-03-21
- 2026-03-22 tail `81` labels=['0'] → hit on 2026-03-23
- 2026-03-23 tail `07` labels=['1'] → hit on 2026-03-24
- 2026-03-24 tail `61` labels=['1'] → hit on 2026-03-25

### MB / MODEL::lstm / same_strict
- 2026-04-11 tail `00` labels=['1'] → hit on 2026-04-12

### MB / MODEL::meta-learning / same_any
- 2026-03-10 tail `68` labels=['1'] → hit on 2026-03-11
- 2026-03-13 tail `23` labels=['1'] → hit on 2026-03-14
- 2026-03-14 tail `76` labels=['0'] → hit on 2026-03-15
- 2026-03-15 tail `88` labels=['3'] → hit on 2026-03-16
- 2026-03-16 tail `66` labels=['0'] → hit on 2026-03-17

### MB / MODEL::meta-learning / same_strict
- 2026-03-10 tail `68` labels=['1'] → hit on 2026-03-11
- 2026-04-05 tail `06` labels=['0'] → hit on 2026-04-06

### MB / MODEL::minimax-m2.7 / same_any
- 2026-04-22 tail `22` labels=['0'] → hit on 2026-04-23
- 2026-04-22 tail `84` labels=['1'] → hit on 2026-04-23
- 2026-04-23 tail `28` labels=['1'] → hit on 2026-04-24

### MB / MODEL::mistral-large-3 / same_any
- 2026-04-21 tail `39` labels=['1'] → hit on 2026-04-22
- 2026-04-22 tail `02` labels=['1'] → hit on 2026-04-23

### MB / MODEL::mistral-nemo / same_any
- 2026-04-20 tail `64` labels=['0'] → hit on 2026-04-21
- 2026-04-21 tail `73` labels=['1'] → hit on 2026-04-22

### MB / MODEL::qwen3-coder / same_any
- 2026-04-15 tail `76` labels=['1'] → hit on 2026-04-16
- 2026-04-24 tail `48` labels=['1'] → hit on 2026-04-25
- 2026-04-29 tail `06` labels=['0'] → hit on 2026-04-30
- 2026-04-30 tail `46` labels=['0'] → hit on 2026-05-01
- 2026-04-30 tail `91` labels=['1'] → hit on 2026-05-01

### MB / MODEL::qwen3-coder / same_strict
- 2026-05-05 tail `41` labels=['0'] → hit on 2026-05-06

### MB / MODEL::qwen3-max-thinking / same_any
- 2026-04-17 tail `54` labels=['1'] → hit on 2026-04-18
- 2026-04-22 tail `22` labels=['0'] → hit on 2026-04-23
- 2026-04-23 tail `28` labels=['0'] → hit on 2026-04-24
- 2026-04-30 tail `46` labels=['0'] → hit on 2026-05-01
- 2026-05-03 tail `85` labels=['1'] → hit on 2026-05-04

### MB / MODEL::qwen3-max-thinking / same_strict
- 2026-05-05 tail `41` labels=['0'] → hit on 2026-05-06

### MB / MODEL::qwen3.6-plus / same_any
- 2026-04-28 tail `46` labels=['1'] → hit on 2026-04-29
- 2026-04-29 tail `79` labels=['0'] → hit on 2026-04-30
- 2026-04-30 tail `32` labels=['0'] → hit on 2026-05-01
- 2026-05-03 tail `14` labels=['1'] → hit on 2026-05-04
- 2026-05-06 tail `49` labels=['0'] → hit on 2026-05-07

### MB / MODEL::random-forest / same_any
- 2026-03-10 tail `68` labels=['1'] → hit on 2026-03-11
- 2026-03-13 tail `14` labels=['0'] → hit on 2026-03-14
- 2026-03-14 tail `76` labels=['0'] → hit on 2026-03-15
- 2026-03-14 tail `80` labels=['1'] → hit on 2026-03-15
- 2026-03-16 tail `22` labels=['1'] → hit on 2026-03-17

### MB / MODEL::random-forest / same_strict
- 2026-03-10 tail `68` labels=['1'] → hit on 2026-03-11
- 2026-04-07 tail `50` labels=['0'] → hit on 2026-04-08

### MB / MODEL::smart-ensemble / same_any
- 2026-03-13 tail `23` labels=['0'] → hit on 2026-03-14
- 2026-03-14 tail `80` labels=['0'] → hit on 2026-03-15
- 2026-03-14 tail `76` labels=['1'] → hit on 2026-03-15
- 2026-03-18 tail `22` labels=['0'] → hit on 2026-03-19
- 2026-03-21 tail `49` labels=['0'] → hit on 2026-03-22

### MB / MODEL::smart-ensemble / same_strict
- 2026-04-01 tail `67` labels=['0'] → hit on 2026-04-02
- 2026-04-03 tail `37` labels=['1'] → hit on 2026-04-04
- 2026-04-04 tail `55` labels=['1'] → hit on 2026-04-05
- 2026-04-10 tail `04` labels=['1'] → hit on 2026-04-11

### MB / MODEL::smart-ml / same_any
- 2026-03-10 tail `68` labels=['0'] → hit on 2026-03-11
- 2026-03-11 tail `04` labels=['1'] → hit on 2026-03-12
- 2026-03-13 tail `23` labels=['0'] → hit on 2026-03-14
- 2026-03-14 tail `80` labels=['0'] → hit on 2026-03-15
- 2026-03-14 tail `76` labels=['1'] → hit on 2026-03-15

### MB / MODEL::smart-ml / same_strict
- 2026-03-10 tail `68` labels=['0'] → hit on 2026-03-11
- 2026-04-17 tail `43` labels=['0'] → hit on 2026-04-18

### MB / MODEL::xgboost / same_any
- 2026-03-10 tail `68` labels=['0'] → hit on 2026-03-11
- 2026-03-10 tail `36` labels=['3'] → hit on 2026-03-11
- 2026-03-11 tail `04` labels=['0'] → hit on 2026-03-12
- 2026-03-11 tail `06` labels=['1'] → hit on 2026-03-12
- 2026-03-13 tail `14` labels=['0'] → hit on 2026-03-14

### MB / MODEL::xgboost / same_strict
- 2026-03-10 tail `68` labels=['0'] → hit on 2026-03-11
- 2026-03-23 tail `29` labels=['0'] → hit on 2026-03-24
- 2026-04-03 tail `37` labels=['0'] → hit on 2026-04-04
- 2026-04-04 tail `55` labels=['1'] → hit on 2026-04-05
- 2026-04-07 tail `50` labels=['0'] → hit on 2026-04-08

### MB / MODEL_MAIN / same_any
- 2026-03-10 tail `68` labels=['combo-no-token[0]', 'combo-super[0]', 'meta-learning[1]', 'random-forest[1]', 'smart-ml[0]'] → hit on 2026-03-11
- 2026-03-10 tail `36` labels=['xgboost[3]'] → hit on 2026-03-11
- 2026-03-10 tail `96` labels=['deepseek-chat[1]'] → hit on 2026-03-11
- 2026-03-11 tail `04` labels=['combo-no-token[1]', 'combo-super[2]', 'smart-ml[1]', 'xgboost[0]'] → hit on 2026-03-12
- 2026-03-11 tail `06` labels=['xgboost[1]'] → hit on 2026-03-12

### MB / MODEL_MAIN / same_strict
- 2026-03-10 tail `68` labels=['combo-no-token[0]', 'combo-super[0]', 'meta-learning[1]', 'random-forest[1]', 'smart-ml[0]'] → hit on 2026-03-11
- 2026-03-21 tail `46` labels=['gemini-2.5-pro[1]'] → hit on 2026-03-22
- 2026-03-23 tail `29` labels=['xgboost[0]'] → hit on 2026-03-24
- 2026-03-30 tail `91` labels=['claude-sonnet-4-6[0]', 'deepseek-reasoner[1]', 'gemini-2.5-flash[1]', 'gpt-5-mini[1]'] → hit on 2026-03-31
- 2026-04-01 tail `67` labels=['combo-no-token[0]', 'smart-ensemble[0]'] → hit on 2026-04-02

### MB / OFFICIAL_BT / same_any
- 2026-03-10 tail `68` labels=['final_bundles.bach_thu'] → hit on 2026-03-11
- 2026-03-13 tail `23` labels=['final_bundles.bach_thu'] → hit on 2026-03-14
- 2026-03-14 tail `76` labels=['final_bundles.bach_thu'] → hit on 2026-03-15
- 2026-03-19 tail `57` labels=['final_bundles.bach_thu'] → hit on 2026-03-20
- 2026-03-21 tail `49` labels=['final_bundles.bach_thu'] → hit on 2026-03-22

### MB / OFFICIAL_BT / same_strict
- 2026-03-10 tail `68` labels=['final_bundles.bach_thu'] → hit on 2026-03-11
- 2026-04-17 tail `43` labels=['final_bundles.bach_thu'] → hit on 2026-04-18

### MB / OFFICIAL_LO2 / same_any
- 2026-03-10 tail `68` labels=['final_bundles.lo2'] → hit on 2026-03-11
- 2026-03-11 tail `04` labels=['final_bundles.lo2'] → hit on 2026-03-12
- 2026-03-13 tail `23` labels=['final_bundles.lo2'] → hit on 2026-03-14
- 2026-03-13 tail `14` labels=['final_bundles.lo2'] → hit on 2026-03-14
- 2026-03-14 tail `76` labels=['final_bundles.lo2'] → hit on 2026-03-15

### MB / OFFICIAL_LO2 / same_strict
- 2026-03-10 tail `68` labels=['final_bundles.lo2'] → hit on 2026-03-11
- 2026-04-01 tail `67` labels=['final_bundles.lo2'] → hit on 2026-04-02
- 2026-04-17 tail `43` labels=['final_bundles.lo2'] → hit on 2026-04-18
- 2026-05-05 tail `41` labels=['final_bundles.lo2'] → hit on 2026-05-06

### MB / TEST_BT / same_any
- 2026-04-08 tail `37` labels=['MB_AI_CHAIN_PRESERVATION_V1', 'MB_NO_TOKEN_HERD_REDUCTION_V1', 'MB_OFFICIAL_BASELINE_CONTROL', 'MB_PRIOR_REGION_CONTEXT_SAFE_V1', 'MB_SPECIALIST_ROSTER_V1'] → hit on 2026-04-09
- 2026-04-10 tail `16` labels=['MB_PRIOR_REGION_CONTEXT_SAFE_V1'] → hit on 2026-04-11
- 2026-04-13 tail `03` labels=['MB_AI_CHAIN_PRESERVATION_V1', 'MB_PRIOR_REGION_CONTEXT_SAFE_V1'] → hit on 2026-04-14
- 2026-04-17 tail `43` labels=['MB_OFFICIAL_BASELINE_CONTROL'] → hit on 2026-04-18
- 2026-04-17 tail `73` labels=['MB_AI_CHAIN_PRESERVATION_V1', 'MB_NO_TOKEN_HERD_REDUCTION_V1', 'MB_PRIOR_REGION_CONTEXT_SAFE_V1', 'MB_STRENGTH_WEIGHTED_V52_5_2'] → hit on 2026-04-18

### MB / TEST_BT / same_strict
- 2026-04-17 tail `43` labels=['MB_OFFICIAL_BASELINE_CONTROL'] → hit on 2026-04-18
- 2026-05-05 tail `41` labels=['MB_ADAPTIVE_BUDGET_SELECTOR_V1', 'MB_AI_CHAIN_PRESERVATION_V1', 'MB_COMPOSITE_CHALLENGER_V2', 'MB_NO_TOKEN_HERD_REDUCTION_V1', 'MB_STRENGTH_WEIGHTED_V52_5_2'] → hit on 2026-05-06

### MB / TEST_LO2 / same_any
- 2026-04-07 tail `26` labels=['MB_OFFICIAL_BASELINE_CONTROL'] → hit on 2026-04-08
- 2026-04-08 tail `37` labels=['MB_AI_CHAIN_PRESERVATION_V1', 'MB_NO_TOKEN_HERD_REDUCTION_V1', 'MB_OFFICIAL_BASELINE_CONTROL', 'MB_PRIOR_REGION_CONTEXT_SAFE_V1', 'MB_SPECIALIST_ROSTER_V1'] → hit on 2026-04-09
- 2026-04-10 tail `16` labels=['MB_AI_CHAIN_PRESERVATION_V1', 'MB_NO_TOKEN_HERD_REDUCTION_V1', 'MB_OFFICIAL_BASELINE_CONTROL', 'MB_PRIOR_REGION_CONTEXT_SAFE_V1', 'MB_SPECIALIST_ROSTER_V1'] → hit on 2026-04-11
- 2026-04-12 tail `45` labels=['MB_AI_CHAIN_PRESERVATION_V1', 'MB_NO_TOKEN_HERD_REDUCTION_V1', 'MB_OFFICIAL_BASELINE_CONTROL', 'MB_PRIOR_REGION_CONTEXT_SAFE_V1', 'MB_SPECIALIST_ROSTER_V1'] → hit on 2026-04-13
- 2026-04-13 tail `03` labels=['MB_AI_CHAIN_PRESERVATION_V1', 'MB_PRIOR_REGION_CONTEXT_SAFE_V1'] → hit on 2026-04-14

### MB / TEST_LO2 / same_strict
- 2026-04-17 tail `43` labels=['MB_AI_CHAIN_PRESERVATION_V1', 'MB_NO_TOKEN_HERD_REDUCTION_V1', 'MB_OFFICIAL_BASELINE_CONTROL', 'MB_PRIOR_REGION_CONTEXT_SAFE_V1', 'MB_SPECIALIST_ROSTER_V1'] → hit on 2026-04-18
- 2026-05-05 tail `41` labels=['MB_ADAPTIVE_BUDGET_SELECTOR_V1', 'MB_AI_CHAIN_PRESERVATION_V1', 'MB_COMPOSITE_CHALLENGER_V2', 'MB_NO_TOKEN_HERD_REDUCTION_V1', 'MB_OFFICIAL_BASELINE_CONTROL'] → hit on 2026-05-06

### MB / V67 / same_any
- 2026-05-07 tail `79` labels=['adaptive_exploit_v67_candidate_trace:score=4.4076'] → hit on 2026-05-08
- 2026-05-07 tail `87` labels=['adaptive_exploit_v67_candidate_trace:score=1.0668'] → hit on 2026-05-08
- 2026-05-08 tail `37` labels=['adaptive_exploit_v67_candidate_trace:score=2.1661'] → hit on 2026-05-09

### MB / V70 / same_any
- 2026-05-05 tail `41` labels=['consensus_v1_trace:agreement_count=5'] → hit on 2026-05-06
- 2026-05-07 tail `79` labels=['consensus_v1_trace:agreement_count=2'] → hit on 2026-05-08
- 2026-05-08 tail `37` labels=['consensus_v1_trace:agreement_count=3'] → hit on 2026-05-09
- 2026-05-08 tail `64` labels=['consensus_v1_trace:agreement_count=1'] → hit on 2026-05-09

### MB / V70 / same_strict
- 2026-05-05 tail `41` labels=['consensus_v1_trace:agreement_count=5'] → hit on 2026-05-06

### MB / V73 / same_any
- 2026-05-05 tail `41` labels=['hybrid_v1_trace:confidence_tier=HIGH'] → hit on 2026-05-06
- 2026-05-07 tail `79` labels=['hybrid_v1_trace:confidence_tier=AURA'] → hit on 2026-05-08

### MB / V73 / same_strict
- 2026-05-05 tail `41` labels=['hybrid_v1_trace:confidence_tier=HIGH'] → hit on 2026-05-06

### MB->MN / MODEL::arcee-trinity / cross_next
- 2026-04-16 tail `08` labels=['1'] → hit on 2026-04-17
- 2026-04-17 tail `07` labels=['0'] → hit on 2026-04-18
- 2026-04-20 tail `46` labels=['0'] → hit on 2026-04-21
- 2026-04-22 tail `66` labels=['1'] → hit on 2026-04-23

### MB->MN / MODEL::claude-opus-4-20250514 / cross_next
- 2026-03-16 tail `32` labels=['1'] → hit on 2026-03-17
- 2026-03-17 tail `47` labels=['1'] → hit on 2026-03-18
- 2026-03-19 tail `57` labels=['0'] → hit on 2026-03-20
- 2026-03-19 tail `32` labels=['1'] → hit on 2026-03-20
- 2026-03-22 tail `63` labels=['0'] → hit on 2026-03-23

### MB->MN / MODEL::claude-sonnet-4-6 / cross_next
- 2026-03-10 tail `59` labels=['1'] → hit on 2026-03-11
- 2026-03-17 tail `81` labels=['0'] → hit on 2026-03-18
- 2026-03-19 tail `32` labels=['0'] → hit on 2026-03-20
- 2026-03-22 tail `63` labels=['0'] → hit on 2026-03-23
- 2026-03-22 tail `69` labels=['1'] → hit on 2026-03-23

### MB->MN / MODEL::combo-no-token / cross_next
- 2026-03-10 tail `68` labels=['0'] → hit on 2026-03-11
- 2026-03-11 tail `04` labels=['1'] → hit on 2026-03-12
- 2026-03-12 tail `74` labels=['0'] → hit on 2026-03-13
- 2026-03-13 tail `23` labels=['0'] → hit on 2026-03-14
- 2026-03-13 tail `14` labels=['1'] → hit on 2026-03-14

### MB->MN / MODEL::combo-super / cross_next
- 2026-03-10 tail `68` labels=['0'] → hit on 2026-03-11
- 2026-03-10 tail `59` labels=['2'] → hit on 2026-03-11
- 2026-03-11 tail `04` labels=['2'] → hit on 2026-03-12
- 2026-03-12 tail `23` labels=['2'] → hit on 2026-03-13
- 2026-03-14 tail `80` labels=['0'] → hit on 2026-03-15

### MB->MN / MODEL::deepseek-chat / cross_next
- 2026-03-10 tail `74` labels=['0'] → hit on 2026-03-11
- 2026-03-11 tail `02` labels=['0'] → hit on 2026-03-12
- 2026-03-15 tail `45` labels=['1'] → hit on 2026-03-16
- 2026-03-16 tail `67` labels=['0'] → hit on 2026-03-17
- 2026-03-19 tail `57` labels=['0'] → hit on 2026-03-20

### MB->MN / MODEL::deepseek-reasoner / cross_next
- 2026-03-10 tail `66` labels=['0'] → hit on 2026-03-11
- 2026-03-10 tail `59` labels=['1'] → hit on 2026-03-11
- 2026-03-11 tail `25` labels=['0'] → hit on 2026-03-12
- 2026-03-15 tail `45` labels=['1'] → hit on 2026-03-16
- 2026-03-19 tail `57` labels=['0'] → hit on 2026-03-20

### MB->MN / MODEL::deepseek-v4-flash / cross_next
- 2026-04-28 tail `31` labels=['1'] → hit on 2026-04-29
- 2026-04-29 tail `64` labels=['0'] → hit on 2026-04-30
- 2026-04-30 tail `91` labels=['1'] → hit on 2026-05-01
- 2026-05-01 tail `74` labels=['0'] → hit on 2026-05-02
- 2026-05-01 tail `18` labels=['1'] → hit on 2026-05-02

### MB->MN / MODEL::deepseek-v4-pro / cross_next
- 2026-04-28 tail `31` labels=['1'] → hit on 2026-04-29
- 2026-05-01 tail `74` labels=['0'] → hit on 2026-05-02
- 2026-05-03 tail `30` labels=['1'] → hit on 2026-05-04
- 2026-05-05 tail `09` labels=['0'] → hit on 2026-05-06
- 2026-05-07 tail `39` labels=['0'] → hit on 2026-05-08

### MB->MN / MODEL::gemini-2.5-flash / cross_next
- 2026-03-10 tail `59` labels=['0'] → hit on 2026-03-11
- 2026-03-10 tail `74` labels=['1'] → hit on 2026-03-11
- 2026-03-11 tail `02` labels=['0'] → hit on 2026-03-12
- 2026-03-11 tail `25` labels=['1'] → hit on 2026-03-12
- 2026-03-18 tail `50` labels=['0'] → hit on 2026-03-19

### MB->MN / MODEL::gemini-2.5-pro / cross_next
- 2026-03-11 tail `25` labels=['0'] → hit on 2026-03-12
- 2026-03-16 tail `67` labels=['0'] → hit on 2026-03-17
- 2026-03-17 tail `67` labels=['1'] → hit on 2026-03-18
- 2026-03-18 tail `17` labels=['0'] → hit on 2026-03-19
- 2026-03-19 tail `57` labels=['1'] → hit on 2026-03-20

### MB->MN / MODEL::gemini-3-flash / cross_next
- 2026-05-07 tail `87` labels=['0'] → hit on 2026-05-08
- 2026-05-07 tail `32` labels=['1'] → hit on 2026-05-08

### MB->MN / MODEL::gemini-3.1-pro / cross_next
- 2026-05-05 tail `90` labels=['0'] → hit on 2026-05-06

### MB->MN / MODEL::gemma-4-31b / cross_next
- 2026-05-05 tail `09` labels=['1'] → hit on 2026-05-06
- 2026-05-07 tail `32` labels=['0'] → hit on 2026-05-08

### MB->MN / MODEL::glm-5.1 / cross_next
- 2026-04-12 tail `73` labels=['1'] → hit on 2026-04-13
- 2026-04-13 tail `31` labels=['0'] → hit on 2026-04-14
- 2026-04-15 tail `42` labels=['0'] → hit on 2026-04-16
- 2026-04-15 tail `01` labels=['1'] → hit on 2026-04-16
- 2026-04-16 tail `02` labels=['0'] → hit on 2026-04-17

### MB->MN / MODEL::gpt-5-mini / cross_next
- 2026-03-18 tail `31` labels=['0'] → hit on 2026-03-19
- 2026-03-19 tail `57` labels=['0'] → hit on 2026-03-20
- 2026-03-22 tail `63` labels=['0'] → hit on 2026-03-23
- 2026-03-22 tail `69` labels=['1'] → hit on 2026-03-23
- 2026-03-24 tail `71` labels=['0'] → hit on 2026-03-25

### MB->MN / MODEL::gpt-5.4 / cross_next
- 2026-03-25 tail `49` labels=['0'] → hit on 2026-03-26
- 2026-03-25 tail `25` labels=['1'] → hit on 2026-03-26
- 2026-03-26 tail `19` labels=['0'] → hit on 2026-03-27
- 2026-03-26 tail `31` labels=['1'] → hit on 2026-03-27
- 2026-03-27 tail `07` labels=['1'] → hit on 2026-03-28

### MB->MN / MODEL::gpt-5.5 / cross_next
- 2026-04-27 tail `61` labels=['1'] → hit on 2026-04-28
- 2026-04-29 tail `49` labels=['0'] → hit on 2026-04-30
- 2026-04-30 tail `32` labels=['1'] → hit on 2026-05-01
- 2026-05-01 tail `74` labels=['0'] → hit on 2026-05-02
- 2026-05-03 tail `14` labels=['0'] → hit on 2026-05-04

### MB->MN / MODEL::gpt-oss-120b / cross_next
- 2026-04-20 tail `45` labels=['1'] → hit on 2026-04-21
- 2026-04-21 tail `50` labels=['0'] → hit on 2026-04-22
- 2026-04-22 tail `22` labels=['0'] → hit on 2026-04-23
- 2026-04-23 tail `48` labels=['1'] → hit on 2026-04-24
- 2026-04-24 tail `48` labels=['1'] → hit on 2026-04-25

### MB->MN / MODEL::grok-4.20-multi-agent / cross_next
- 2026-04-13 tail `31` labels=['0'] → hit on 2026-04-14
- 2026-04-15 tail `42` labels=['0'] → hit on 2026-04-16
- 2026-04-17 tail `73` labels=['1'] → hit on 2026-04-18
- 2026-04-20 tail `45` labels=['1'] → hit on 2026-04-21
- 2026-04-21 tail `50` labels=['1'] → hit on 2026-04-22

### MB->MN / MODEL::kimi-k2.5 / cross_next
- 2026-04-17 tail `73` labels=['0'] → hit on 2026-04-18
- 2026-04-17 tail `07` labels=['1'] → hit on 2026-04-18
- 2026-04-18 tail `11` labels=['1'] → hit on 2026-04-19
- 2026-04-20 tail `46` labels=['1'] → hit on 2026-04-21
- 2026-04-21 tail `12` labels=['0'] → hit on 2026-04-22

### MB->MN / MODEL::kimi-k2.6 / cross_next
- 2026-04-23 tail `28` labels=['1'] → hit on 2026-04-24
- 2026-04-25 tail `32` labels=['0'] → hit on 2026-04-26

### MB->MN / MODEL::llama-4-maverick / cross_next
- 2026-04-20 tail `45` labels=['1'] → hit on 2026-04-21
- 2026-04-22 tail `76` labels=['1'] → hit on 2026-04-23

### MB->MN / MODEL::lstm / cross_next
- 2026-03-11 tail `00` labels=['0'] → hit on 2026-03-12
- 2026-03-12 tail `00` labels=['1'] → hit on 2026-03-13
- 2026-03-13 tail `67` labels=['0'] → hit on 2026-03-14
- 2026-03-14 tail `67` labels=['1'] → hit on 2026-03-15
- 2026-03-16 tail `40` labels=['1'] → hit on 2026-03-17

### MB->MN / MODEL::meta-learning / cross_next
- 2026-03-10 tail `68` labels=['1'] → hit on 2026-03-11
- 2026-03-12 tail `74` labels=['0'] → hit on 2026-03-13
- 2026-03-12 tail `14` labels=['1'] → hit on 2026-03-13
- 2026-03-13 tail `06` labels=['0'] → hit on 2026-03-14
- 2026-03-13 tail `23` labels=['1'] → hit on 2026-03-14

### MB->MN / MODEL::minimax-m2.7 / cross_next
- 2026-04-17 tail `18` labels=['0'] → hit on 2026-04-18
- 2026-04-19 tail `95` labels=['1'] → hit on 2026-04-20
- 2026-04-20 tail `45` labels=['1'] → hit on 2026-04-21
- 2026-04-21 tail `12` labels=['0'] → hit on 2026-04-22
- 2026-04-21 tail `80` labels=['1'] → hit on 2026-04-22

### MB->MN / MODEL::mistral-large-3 / cross_next
- 2026-04-20 tail `45` labels=['1'] → hit on 2026-04-21
- 2026-04-22 tail `02` labels=['1'] → hit on 2026-04-23

### MB->MN / MODEL::mistral-nemo / cross_next
- 2026-04-19 tail `91` labels=['0'] → hit on 2026-04-20
- 2026-04-20 tail `46` labels=['1'] → hit on 2026-04-21
- 2026-04-21 tail `46` labels=['0'] → hit on 2026-04-22

### MB->MN / MODEL::nemotron-3-super / cross_next
- 2026-04-16 tail `08` labels=['0'] → hit on 2026-04-17
- 2026-04-16 tail `02` labels=['1'] → hit on 2026-04-17
- 2026-04-17 tail `07` labels=['0'] → hit on 2026-04-18

### MB->MN / MODEL::qwen3-coder / cross_next
- 2026-04-14 tail `45` labels=['1'] → hit on 2026-04-15
- 2026-04-20 tail `45` labels=['1'] → hit on 2026-04-21
- 2026-04-21 tail `50` labels=['0'] → hit on 2026-04-22
- 2026-04-24 tail `48` labels=['1'] → hit on 2026-04-25
- 2026-04-25 tail `32` labels=['0'] → hit on 2026-04-26

### MB->MN / MODEL::qwen3-max-thinking / cross_next
- 2026-04-16 tail `02` labels=['0'] → hit on 2026-04-17
- 2026-04-19 tail `30` labels=['1'] → hit on 2026-04-20
- 2026-04-21 tail `12` labels=['0'] → hit on 2026-04-22
- 2026-04-21 tail `80` labels=['1'] → hit on 2026-04-22
- 2026-04-22 tail `22` labels=['0'] → hit on 2026-04-23

### MB->MN / MODEL::qwen3.6-plus / cross_next
- 2026-04-13 tail `31` labels=['1'] → hit on 2026-04-14
- 2026-04-15 tail `01` labels=['0'] → hit on 2026-04-16
- 2026-04-15 tail `42` labels=['1'] → hit on 2026-04-16
- 2026-04-27 tail `61` labels=['0'] → hit on 2026-04-28
- 2026-04-28 tail `46` labels=['1'] → hit on 2026-04-29

### MB->MN / MODEL::random-forest / cross_next
- 2026-03-10 tail `68` labels=['1'] → hit on 2026-03-11
- 2026-03-12 tail `74` labels=['0'] → hit on 2026-03-13
- 2026-03-13 tail `14` labels=['0'] → hit on 2026-03-14
- 2026-03-14 tail `76` labels=['0'] → hit on 2026-03-15
- 2026-03-14 tail `80` labels=['1'] → hit on 2026-03-15

### MB->MN / MODEL::smart-ensemble / cross_next
- 2026-03-11 tail `00` labels=['1'] → hit on 2026-03-12
- 2026-03-12 tail `74` labels=['0'] → hit on 2026-03-13
- 2026-03-13 tail `23` labels=['0'] → hit on 2026-03-14
- 2026-03-13 tail `06` labels=['1'] → hit on 2026-03-14
- 2026-03-14 tail `80` labels=['0'] → hit on 2026-03-15

### MB->MN / MODEL::smart-ml / cross_next
- 2026-03-10 tail `68` labels=['0'] → hit on 2026-03-11
- 2026-03-11 tail `04` labels=['1'] → hit on 2026-03-12
- 2026-03-12 tail `74` labels=['0'] → hit on 2026-03-13
- 2026-03-13 tail `23` labels=['0'] → hit on 2026-03-14
- 2026-03-14 tail `80` labels=['0'] → hit on 2026-03-15

### MB->MN / MODEL::xgboost / cross_next
- 2026-03-10 tail `68` labels=['0'] → hit on 2026-03-11
- 2026-03-11 tail `04` labels=['0'] → hit on 2026-03-12
- 2026-03-12 tail `63` labels=['0'] → hit on 2026-03-13
- 2026-03-13 tail `14` labels=['0'] → hit on 2026-03-14
- 2026-03-13 tail `23` labels=['1'] → hit on 2026-03-14

### MB->MN / MODEL_MAIN / cross_next
- 2026-03-10 tail `68` labels=['combo-no-token[0]', 'combo-super[0]', 'meta-learning[1]', 'random-forest[1]', 'smart-ml[0]'] → hit on 2026-03-11
- 2026-03-10 tail `59` labels=['claude-sonnet-4-6[1]', 'combo-super[2]', 'deepseek-reasoner[1]', 'gemini-2.5-flash[0]'] → hit on 2026-03-11
- 2026-03-10 tail `74` labels=['deepseek-chat[0]', 'gemini-2.5-flash[1]'] → hit on 2026-03-11
- 2026-03-10 tail `66` labels=['deepseek-reasoner[0]'] → hit on 2026-03-11
- 2026-03-11 tail `00` labels=['lstm[0]', 'smart-ensemble[1]'] → hit on 2026-03-12

### MB->MN / OFFICIAL_BT / cross_next
- 2026-03-10 tail `68` labels=['final_bundles.bach_thu'] → hit on 2026-03-11
- 2026-03-12 tail `74` labels=['final_bundles.bach_thu'] → hit on 2026-03-13
- 2026-03-13 tail `23` labels=['final_bundles.bach_thu'] → hit on 2026-03-14
- 2026-03-14 tail `76` labels=['final_bundles.bach_thu'] → hit on 2026-03-15
- 2026-03-19 tail `57` labels=['final_bundles.bach_thu'] → hit on 2026-03-20

### MB->MN / OFFICIAL_LO2 / cross_next
- 2026-03-10 tail `68` labels=['final_bundles.lo2'] → hit on 2026-03-11
- 2026-03-11 tail `04` labels=['final_bundles.lo2'] → hit on 2026-03-12
- 2026-03-12 tail `74` labels=['final_bundles.lo2'] → hit on 2026-03-13
- 2026-03-13 tail `23` labels=['final_bundles.lo2'] → hit on 2026-03-14
- 2026-03-13 tail `14` labels=['final_bundles.lo2'] → hit on 2026-03-14

### MB->MN / TEST_BT / cross_next
- 2026-04-09 tail `34` labels=['MB_AI_CHAIN_PRESERVATION_V1', 'MB_NO_TOKEN_HERD_REDUCTION_V1', 'MB_PRIOR_REGION_CONTEXT_SAFE_V1', 'MB_SPECIALIST_ROSTER_V1', 'MB_STRENGTH_WEIGHTED_V52_5_2'] → hit on 2026-04-10
- 2026-04-10 tail `24` labels=['MB_AI_CHAIN_PRESERVATION_V1', 'MB_NO_TOKEN_HERD_REDUCTION_V1', 'MB_OFFICIAL_BASELINE_CONTROL', 'MB_SPECIALIST_ROSTER_V1', 'MB_STRENGTH_WEIGHTED_V52_5_2'] → hit on 2026-04-11
- 2026-04-13 tail `31` labels=['MB_NO_TOKEN_HERD_REDUCTION_V1', 'MB_OFFICIAL_BASELINE_CONTROL', 'MB_SPECIALIST_ROSTER_V1', 'MB_STRENGTH_WEIGHTED_V52_5_2'] → hit on 2026-04-14
- 2026-04-15 tail `42` labels=['MB_AI_CHAIN_PRESERVATION_V1', 'MB_NO_TOKEN_HERD_REDUCTION_V1', 'MB_OFFICIAL_BASELINE_CONTROL', 'MB_SPECIALIST_ROSTER_V1', 'MB_STRENGTH_WEIGHTED_V52_5_2'] → hit on 2026-04-16
- 2026-04-15 tail `74` labels=['MB_PRIOR_REGION_CONTEXT_SAFE_V1'] → hit on 2026-04-16

### MB->MN / TEST_LO2 / cross_next
- 2026-04-06 tail `37` labels=['MB_AI_CHAIN_PRESERVATION_V1', 'MB_NO_TOKEN_HERD_REDUCTION_V1', 'MB_OFFICIAL_BASELINE_CONTROL', 'MB_PRIOR_REGION_CONTEXT_SAFE_V1', 'MB_SPECIALIST_ROSTER_V1'] → hit on 2026-04-07
- 2026-04-07 tail `26` labels=['MB_OFFICIAL_BASELINE_CONTROL'] → hit on 2026-04-08
- 2026-04-09 tail `34` labels=['MB_AI_CHAIN_PRESERVATION_V1', 'MB_NO_TOKEN_HERD_REDUCTION_V1', 'MB_OFFICIAL_BASELINE_CONTROL', 'MB_PRIOR_REGION_CONTEXT_SAFE_V1', 'MB_SPECIALIST_ROSTER_V1'] → hit on 2026-04-10
- 2026-04-10 tail `24` labels=['MB_AI_CHAIN_PRESERVATION_V1', 'MB_NO_TOKEN_HERD_REDUCTION_V1', 'MB_OFFICIAL_BASELINE_CONTROL', 'MB_PRIOR_REGION_CONTEXT_SAFE_V1', 'MB_SPECIALIST_ROSTER_V1'] → hit on 2026-04-11
- 2026-04-13 tail `31` labels=['MB_AI_CHAIN_PRESERVATION_V1', 'MB_NO_TOKEN_HERD_REDUCTION_V1', 'MB_OFFICIAL_BASELINE_CONTROL', 'MB_PRIOR_REGION_CONTEXT_SAFE_V1', 'MB_SPECIALIST_ROSTER_V1'] → hit on 2026-04-14

### MB->MN / V67 / cross_next
- 2026-05-07 tail `32` labels=['adaptive_exploit_v67_candidate_trace:score=2.87178'] → hit on 2026-05-08
- 2026-05-07 tail `87` labels=['adaptive_exploit_v67_candidate_trace:score=1.0668'] → hit on 2026-05-08
- 2026-05-08 tail `04` labels=['adaptive_exploit_v67_candidate_trace:score=1.0891'] → hit on 2026-05-09
- 2026-05-08 tail `88` labels=['adaptive_exploit_v67_candidate_trace:score=1.0602'] → hit on 2026-05-09

### MB->MN / V70 / cross_next
- 2026-05-04 tail `09` labels=['consensus_v1_trace:agreement_count=3'] → hit on 2026-05-05
- 2026-05-04 tail `19` labels=['consensus_v1_trace:agreement_count=1'] → hit on 2026-05-05
- 2026-05-05 tail `41` labels=['consensus_v1_trace:agreement_count=5'] → hit on 2026-05-06
- 2026-05-06 tail `79` labels=['consensus_v1_trace:agreement_count=2'] → hit on 2026-05-07
- 2026-05-08 tail `64` labels=['consensus_v1_trace:agreement_count=1'] → hit on 2026-05-09

### MB->MN / V73 / cross_next
- 2026-05-04 tail `09` labels=['hybrid_v1_trace:confidence_tier=HIGH'] → hit on 2026-05-05
- 2026-05-05 tail `41` labels=['hybrid_v1_trace:confidence_tier=HIGH'] → hit on 2026-05-06

### MB->MT / MODEL::arcee-trinity / cross_next
- 2026-04-17 tail `54` labels=['1'] → hit on 2026-04-18
- 2026-04-22 tail `83` labels=['0'] → hit on 2026-04-23
- 2026-04-22 tail `66` labels=['1'] → hit on 2026-04-23

### MB->MT / MODEL::claude-opus-4-20250514 / cross_next
- 2026-03-10 tail `81` labels=['1'] → hit on 2026-03-11
- 2026-03-13 tail `41` labels=['0'] → hit on 2026-03-14
- 2026-03-16 tail `68` labels=['0'] → hit on 2026-03-17
- 2026-03-18 tail `79` labels=['0'] → hit on 2026-03-19
- 2026-03-21 tail `24` labels=['1'] → hit on 2026-03-22

### MB->MT / MODEL::claude-sonnet-4-6 / cross_next
- 2026-03-10 tail `59` labels=['1'] → hit on 2026-03-11
- 2026-03-12 tail `02` labels=['1'] → hit on 2026-03-13
- 2026-03-13 tail `41` labels=['0'] → hit on 2026-03-14
- 2026-03-15 tail `29` labels=['1'] → hit on 2026-03-16
- 2026-03-16 tail `91` labels=['0'] → hit on 2026-03-17

### MB->MT / MODEL::combo-no-token / cross_next
- 2026-03-10 tail `68` labels=['0'] → hit on 2026-03-11
- 2026-03-11 tail `04` labels=['1'] → hit on 2026-03-12
- 2026-03-14 tail `76` labels=['0'] → hit on 2026-03-15
- 2026-03-14 tail `29` labels=['1'] → hit on 2026-03-15
- 2026-03-15 tail `55` labels=['1'] → hit on 2026-03-16

### MB->MT / MODEL::combo-super / cross_next
- 2026-03-10 tail `68` labels=['0'] → hit on 2026-03-11
- 2026-03-10 tail `59` labels=['2'] → hit on 2026-03-11
- 2026-03-11 tail `04` labels=['2'] → hit on 2026-03-12
- 2026-03-12 tail `02` labels=['1'] → hit on 2026-03-13
- 2026-03-14 tail `29` labels=['1'] → hit on 2026-03-15

### MB->MT / MODEL::deepseek-chat / cross_next
- 2026-03-10 tail `74` labels=['0'] → hit on 2026-03-11
- 2026-03-12 tail `02` labels=['1'] → hit on 2026-03-13
- 2026-03-13 tail `41` labels=['1'] → hit on 2026-03-14
- 2026-03-16 tail `91` labels=['1'] → hit on 2026-03-17
- 2026-03-18 tail `79` labels=['0'] → hit on 2026-03-19

### MB->MT / MODEL::deepseek-reasoner / cross_next
- 2026-03-10 tail `66` labels=['0'] → hit on 2026-03-11
- 2026-03-10 tail `59` labels=['1'] → hit on 2026-03-11
- 2026-03-13 tail `41` labels=['1'] → hit on 2026-03-14
- 2026-03-15 tail `48` labels=['0'] → hit on 2026-03-16
- 2026-03-19 tail `30` labels=['1'] → hit on 2026-03-20

### MB->MT / MODEL::deepseek-v4-flash / cross_next
- 2026-04-29 tail `79` labels=['1'] → hit on 2026-04-30
- 2026-04-30 tail `91` labels=['1'] → hit on 2026-05-01
- 2026-05-01 tail `74` labels=['0'] → hit on 2026-05-02
- 2026-05-06 tail `79` labels=['0'] → hit on 2026-05-07

### MB->MT / MODEL::deepseek-v4-pro / cross_next
- 2026-04-29 tail `79` labels=['0'] → hit on 2026-04-30
- 2026-04-30 tail `20` labels=['0'] → hit on 2026-05-01
- 2026-04-30 tail `93` labels=['1'] → hit on 2026-05-01
- 2026-05-01 tail `74` labels=['0'] → hit on 2026-05-02
- 2026-05-01 tail `57` labels=['1'] → hit on 2026-05-02

### MB->MT / MODEL::gemini-2.5-flash / cross_next
- 2026-03-10 tail `59` labels=['0'] → hit on 2026-03-11
- 2026-03-10 tail `74` labels=['1'] → hit on 2026-03-11
- 2026-03-13 tail `41` labels=['1'] → hit on 2026-03-14
- 2026-03-16 tail `68` labels=['0'] → hit on 2026-03-17
- 2026-03-16 tail `91` labels=['1'] → hit on 2026-03-17

### MB->MT / MODEL::gemini-2.5-pro / cross_next
- 2026-03-11 tail `65` labels=['1'] → hit on 2026-03-12
- 2026-03-12 tail `82` labels=['1'] → hit on 2026-03-13
- 2026-03-13 tail `41` labels=['0'] → hit on 2026-03-14
- 2026-03-16 tail `68` labels=['1'] → hit on 2026-03-17
- 2026-03-18 tail `17` labels=['0'] → hit on 2026-03-19

### MB->MT / MODEL::gemini-3-flash / cross_next
- 2026-05-06 tail `64` labels=['0'] → hit on 2026-05-07

### MB->MT / MODEL::gemini-3.1-pro / cross_next
- 2026-05-06 tail `64` labels=['1'] → hit on 2026-05-07

### MB->MT / MODEL::gemma-4-31b / cross_next
- 2026-05-06 tail `64` labels=['1'] → hit on 2026-05-07

### MB->MT / MODEL::glm-5.1 / cross_next
- 2026-04-14 tail `47` labels=['0'] → hit on 2026-04-15
- 2026-04-15 tail `01` labels=['1'] → hit on 2026-04-16
- 2026-04-16 tail `02` labels=['0'] → hit on 2026-04-17
- 2026-04-17 tail `54` labels=['0'] → hit on 2026-04-18
- 2026-04-19 tail `88` labels=['1'] → hit on 2026-04-20

### MB->MT / MODEL::gpt-5-mini / cross_next
- 2026-03-16 tail `91` labels=['1'] → hit on 2026-03-17
- 2026-03-18 tail `31` labels=['0'] → hit on 2026-03-19
- 2026-03-20 tail `92` labels=['1'] → hit on 2026-03-21
- 2026-03-22 tail `69` labels=['1'] → hit on 2026-03-23
- 2026-03-23 tail `74` labels=['1'] → hit on 2026-03-24

### MB->MT / MODEL::gpt-5.4 / cross_next
- 2026-03-24 tail `66` labels=['1'] → hit on 2026-03-25
- 2026-03-25 tail `25` labels=['1'] → hit on 2026-03-26
- 2026-03-26 tail `19` labels=['0'] → hit on 2026-03-27
- 2026-03-26 tail `31` labels=['1'] → hit on 2026-03-27
- 2026-03-27 tail `07` labels=['1'] → hit on 2026-03-28

### MB->MT / MODEL::gpt-5.5 / cross_next
- 2026-04-28 tail `85` labels=['1'] → hit on 2026-04-29
- 2026-04-29 tail `49` labels=['0'] → hit on 2026-04-30
- 2026-04-29 tail `79` labels=['1'] → hit on 2026-04-30
- 2026-05-01 tail `74` labels=['0'] → hit on 2026-05-02
- 2026-05-06 tail `64` labels=['1'] → hit on 2026-05-07

### MB->MT / MODEL::gpt-oss-120b / cross_next
- 2026-04-20 tail `45` labels=['1'] → hit on 2026-04-21
- 2026-04-22 tail `22` labels=['0'] → hit on 2026-04-23
- 2026-04-25 tail `32` labels=['1'] → hit on 2026-04-26
- 2026-04-29 tail `91` labels=['0'] → hit on 2026-04-30
- 2026-05-01 tail `30` labels=['0'] → hit on 2026-05-02

### MB->MT / MODEL::grok-4.20-multi-agent / cross_next
- 2026-04-13 tail `52` labels=['1'] → hit on 2026-04-14
- 2026-04-14 tail `47` labels=['1'] → hit on 2026-04-15
- 2026-04-16 tail `65` labels=['1'] → hit on 2026-04-17
- 2026-04-17 tail `82` labels=['0'] → hit on 2026-04-18
- 2026-04-18 tail `07` labels=['1'] → hit on 2026-04-19

### MB->MT / MODEL::kimi-k2.5 / cross_next
- 2026-04-18 tail `11` labels=['1'] → hit on 2026-04-19
- 2026-04-19 tail `88` labels=['1'] → hit on 2026-04-20
- 2026-04-22 tail `22` labels=['0'] → hit on 2026-04-23
- 2026-04-23 tail `38` labels=['0'] → hit on 2026-04-24
- 2026-05-01 tail `74` labels=['1'] → hit on 2026-05-02

### MB->MT / MODEL::kimi-k2.6 / cross_next
- 2026-04-23 tail `38` labels=['0'] → hit on 2026-04-24
- 2026-04-25 tail `32` labels=['0'] → hit on 2026-04-26

### MB->MT / MODEL::llama-4-maverick / cross_next
- 2026-04-20 tail `45` labels=['1'] → hit on 2026-04-21
- 2026-04-21 tail `54` labels=['1'] → hit on 2026-04-22
- 2026-04-22 tail `76` labels=['1'] → hit on 2026-04-23

### MB->MT / MODEL::lstm / cross_next
- 2026-03-10 tail `67` labels=['0'] → hit on 2026-03-11
- 2026-03-13 tail `67` labels=['0'] → hit on 2026-03-14
- 2026-03-14 tail `67` labels=['1'] → hit on 2026-03-15
- 2026-03-15 tail `48` labels=['0'] → hit on 2026-03-16
- 2026-03-16 tail `48` labels=['0'] → hit on 2026-03-17

### MB->MT / MODEL::meta-learning / cross_next
- 2026-03-10 tail `68` labels=['1'] → hit on 2026-03-11
- 2026-03-11 tail `23` labels=['1'] → hit on 2026-03-12
- 2026-03-14 tail `76` labels=['0'] → hit on 2026-03-15
- 2026-03-14 tail `29` labels=['1'] → hit on 2026-03-15
- 2026-03-15 tail `55` labels=['2'] → hit on 2026-03-16

### MB->MT / MODEL::minimax-m2.7 / cross_next
- 2026-04-19 tail `95` labels=['1'] → hit on 2026-04-20
- 2026-04-20 tail `45` labels=['1'] → hit on 2026-04-21
- 2026-04-22 tail `22` labels=['0'] → hit on 2026-04-23
- 2026-04-25 tail `32` labels=['0'] → hit on 2026-04-26
- 2026-04-27 tail `02` labels=['0'] → hit on 2026-04-28

### MB->MT / MODEL::mistral-large-3 / cross_next
- 2026-04-20 tail `45` labels=['1'] → hit on 2026-04-21
- 2026-04-22 tail `02` labels=['1'] → hit on 2026-04-23

### MB->MT / MODEL::mistral-nemo / cross_next
- 2026-04-21 tail `46` labels=['0'] → hit on 2026-04-22
- 2026-04-21 tail `73` labels=['1'] → hit on 2026-04-22

### MB->MT / MODEL::nemotron-3-super / cross_next
- 2026-04-16 tail `02` labels=['1'] → hit on 2026-04-17

### MB->MT / MODEL::qwen3-coder / cross_next
- 2026-04-16 tail `65` labels=['0'] → hit on 2026-04-17
- 2026-04-17 tail `97` labels=['0'] → hit on 2026-04-18
- 2026-04-18 tail `07` labels=['1'] → hit on 2026-04-19
- 2026-04-20 tail `45` labels=['1'] → hit on 2026-04-21
- 2026-04-23 tail `38` labels=['0'] → hit on 2026-04-24

### MB->MT / MODEL::qwen3-max-thinking / cross_next
- 2026-04-16 tail `02` labels=['0'] → hit on 2026-04-17
- 2026-04-16 tail `65` labels=['1'] → hit on 2026-04-17
- 2026-04-17 tail `54` labels=['1'] → hit on 2026-04-18
- 2026-04-18 tail `07` labels=['0'] → hit on 2026-04-19
- 2026-04-22 tail `22` labels=['0'] → hit on 2026-04-23

### MB->MT / MODEL::qwen3.6-plus / cross_next
- 2026-04-14 tail `47` labels=['1'] → hit on 2026-04-15
- 2026-04-15 tail `01` labels=['0'] → hit on 2026-04-16
- 2026-04-28 tail `46` labels=['1'] → hit on 2026-04-29
- 2026-04-29 tail `79` labels=['0'] → hit on 2026-04-30
- 2026-05-01 tail `74` labels=['0'] → hit on 2026-05-02

### MB->MT / MODEL::random-forest / cross_next
- 2026-03-10 tail `11` labels=['0'] → hit on 2026-03-11
- 2026-03-10 tail `68` labels=['1'] → hit on 2026-03-11
- 2026-03-11 tail `15` labels=['0'] → hit on 2026-03-12
- 2026-03-11 tail `23` labels=['1'] → hit on 2026-03-12
- 2026-03-14 tail `76` labels=['0'] → hit on 2026-03-15

### MB->MT / MODEL::smart-ensemble / cross_next
- 2026-03-10 tail `67` labels=['1'] → hit on 2026-03-11
- 2026-03-14 tail `76` labels=['1'] → hit on 2026-03-15
- 2026-03-15 tail `55` labels=['1'] → hit on 2026-03-16
- 2026-03-18 tail `44` labels=['1'] → hit on 2026-03-19
- 2026-03-19 tail `26` labels=['0'] → hit on 2026-03-20

### MB->MT / MODEL::smart-ml / cross_next
- 2026-03-10 tail `68` labels=['0'] → hit on 2026-03-11
- 2026-03-11 tail `04` labels=['1'] → hit on 2026-03-12
- 2026-03-14 tail `76` labels=['1'] → hit on 2026-03-15
- 2026-03-15 tail `55` labels=['1'] → hit on 2026-03-16
- 2026-03-18 tail `44` labels=['0'] → hit on 2026-03-19

### MB->MT / MODEL::xgboost / cross_next
- 2026-03-10 tail `68` labels=['0'] → hit on 2026-03-11
- 2026-03-11 tail `04` labels=['0'] → hit on 2026-03-12
- 2026-03-15 tail `55` labels=['1'] → hit on 2026-03-16
- 2026-03-17 tail `61` labels=['3'] → hit on 2026-03-18
- 2026-03-18 tail `44` labels=['0'] → hit on 2026-03-19

### MB->MT / MODEL_MAIN / cross_next
- 2026-03-10 tail `67` labels=['lstm[0]', 'smart-ensemble[1]'] → hit on 2026-03-11
- 2026-03-10 tail `68` labels=['combo-no-token[0]', 'combo-super[0]', 'meta-learning[1]', 'random-forest[1]', 'smart-ml[0]'] → hit on 2026-03-11
- 2026-03-10 tail `11` labels=['random-forest[0]'] → hit on 2026-03-11
- 2026-03-10 tail `59` labels=['claude-sonnet-4-6[1]', 'combo-super[2]', 'deepseek-reasoner[1]', 'gemini-2.5-flash[0]'] → hit on 2026-03-11
- 2026-03-10 tail `74` labels=['deepseek-chat[0]', 'gemini-2.5-flash[1]'] → hit on 2026-03-11

### MB->MT / OFFICIAL_BT / cross_next
- 2026-03-10 tail `68` labels=['final_bundles.bach_thu'] → hit on 2026-03-11
- 2026-03-14 tail `76` labels=['final_bundles.bach_thu'] → hit on 2026-03-15
- 2026-03-18 tail `44` labels=['final_bundles.bach_thu'] → hit on 2026-03-19
- 2026-03-21 tail `49` labels=['final_bundles.bach_thu'] → hit on 2026-03-22
- 2026-03-25 tail `23` labels=['final_bundles.bach_thu'] → hit on 2026-03-26

### MB->MT / OFFICIAL_LO2 / cross_next
- 2026-03-10 tail `68` labels=['final_bundles.lo2'] → hit on 2026-03-11
- 2026-03-11 tail `04` labels=['final_bundles.lo2'] → hit on 2026-03-12
- 2026-03-14 tail `76` labels=['final_bundles.lo2'] → hit on 2026-03-15
- 2026-03-16 tail `91` labels=['final_bundles.lo2'] → hit on 2026-03-17
- 2026-03-18 tail `44` labels=['final_bundles.lo2'] → hit on 2026-03-19

### MB->MT / TEST_BT / cross_next
- 2026-04-04 tail `67` labels=['MB_NO_TOKEN_HERD_REDUCTION_V1', 'MB_OFFICIAL_BASELINE_CONTROL', 'MB_PRIOR_REGION_CONTEXT_SAFE_V1', 'MB_STRENGTH_WEIGHTED_V52_5_2'] → hit on 2026-04-05
- 2026-04-07 tail `23` labels=['MB_OFFICIAL_BASELINE_CONTROL'] → hit on 2026-04-08
- 2026-04-08 tail `37` labels=['MB_AI_CHAIN_PRESERVATION_V1', 'MB_NO_TOKEN_HERD_REDUCTION_V1', 'MB_OFFICIAL_BASELINE_CONTROL', 'MB_PRIOR_REGION_CONTEXT_SAFE_V1', 'MB_SPECIALIST_ROSTER_V1'] → hit on 2026-04-09
- 2026-04-14 tail `47` labels=['MB_AI_CHAIN_PRESERVATION_V1', 'MB_NO_TOKEN_HERD_REDUCTION_V1', 'MB_OFFICIAL_BASELINE_CONTROL', 'MB_STRENGTH_WEIGHTED_V52_5_2'] → hit on 2026-04-15
- 2026-04-15 tail `74` labels=['MB_PRIOR_REGION_CONTEXT_SAFE_V1'] → hit on 2026-04-16

### MB->MT / TEST_LO2 / cross_next
- 2026-04-04 tail `67` labels=['MB_AI_CHAIN_PRESERVATION_V1', 'MB_NO_TOKEN_HERD_REDUCTION_V1', 'MB_OFFICIAL_BASELINE_CONTROL', 'MB_PRIOR_REGION_CONTEXT_SAFE_V1', 'MB_SPECIALIST_ROSTER_V1'] → hit on 2026-04-05
- 2026-04-06 tail `37` labels=['MB_AI_CHAIN_PRESERVATION_V1', 'MB_NO_TOKEN_HERD_REDUCTION_V1', 'MB_OFFICIAL_BASELINE_CONTROL', 'MB_PRIOR_REGION_CONTEXT_SAFE_V1', 'MB_SPECIALIST_ROSTER_V1'] → hit on 2026-04-07
- 2026-04-07 tail `23` labels=['MB_AI_CHAIN_PRESERVATION_V1', 'MB_NO_TOKEN_HERD_REDUCTION_V1', 'MB_OFFICIAL_BASELINE_CONTROL', 'MB_PRIOR_REGION_CONTEXT_SAFE_V1', 'MB_SPECIALIST_ROSTER_V1'] → hit on 2026-04-08
- 2026-04-08 tail `37` labels=['MB_AI_CHAIN_PRESERVATION_V1', 'MB_NO_TOKEN_HERD_REDUCTION_V1', 'MB_OFFICIAL_BASELINE_CONTROL', 'MB_PRIOR_REGION_CONTEXT_SAFE_V1', 'MB_SPECIALIST_ROSTER_V1'] → hit on 2026-04-09
- 2026-04-08 tail `40` labels=['MB_AI_CHAIN_PRESERVATION_V1', 'MB_NO_TOKEN_HERD_REDUCTION_V1', 'MB_OFFICIAL_BASELINE_CONTROL', 'MB_PRIOR_REGION_CONTEXT_SAFE_V1', 'MB_SPECIALIST_ROSTER_V1'] → hit on 2026-04-09

### MB->MT / V67 / cross_next
- 2026-05-08 tail `20` labels=['adaptive_exploit_v67_candidate_trace:score=3.2129'] → hit on 2026-05-09
- 2026-05-08 tail `88` labels=['adaptive_exploit_v67_candidate_trace:score=1.0602'] → hit on 2026-05-09

### MB->MT / V70 / cross_next
- 2026-05-05 tail `41` labels=['consensus_v1_trace:agreement_count=5'] → hit on 2026-05-06
- 2026-05-06 tail `79` labels=['consensus_v1_trace:agreement_count=2'] → hit on 2026-05-07
- 2026-05-08 tail `20` labels=['consensus_v1_trace:agreement_count=2'] → hit on 2026-05-09

### MB->MT / V73 / cross_next
- 2026-05-05 tail `41` labels=['hybrid_v1_trace:confidence_tier=HIGH'] → hit on 2026-05-06
- 2026-05-08 tail `20` labels=['hybrid_v1_trace:confidence_tier=AURA'] → hit on 2026-05-09

### MN / MODEL::arcee-trinity / same_any
- 2026-04-19 tail `46` labels=['1'] → hit on 2026-04-20
- 2026-04-20 tail `45` labels=['1'] → hit on 2026-04-21

### MN / MODEL::claude-opus-4-20250514 / same_any
- 2026-03-12 tail `73` labels=['0'] → hit on 2026-03-13
- 2026-03-13 tail `45` labels=['0'] → hit on 2026-03-14
- 2026-03-17 tail `52` labels=['0'] → hit on 2026-03-18
- 2026-03-17 tail `74` labels=['1'] → hit on 2026-03-18
- 2026-03-19 tail `85` labels=['1'] → hit on 2026-03-20

### MN / MODEL::claude-sonnet-4-6 / same_any
- 2026-03-10 tail `35` labels=['0'] → hit on 2026-03-11
- 2026-03-12 tail `23` labels=['0'] → hit on 2026-03-13
- 2026-03-12 tail `73` labels=['1'] → hit on 2026-03-13
- 2026-03-13 tail `45` labels=['0'] → hit on 2026-03-14
- 2026-03-14 tail `43` labels=['1'] → hit on 2026-03-15

### MN / MODEL::claude-sonnet-4-6 / same_strict
- 2026-03-29 tail `92` labels=['1'] → hit on 2026-03-30
- 2026-04-10 tail `28` labels=['1'] → hit on 2026-04-11

### MN / MODEL::combo-no-token / same_any
- 2026-03-13 tail `44` labels=['1'] → hit on 2026-03-14
- 2026-03-15 tail `90` labels=['0'] → hit on 2026-03-16
- 2026-03-18 tail `92` labels=['0'] → hit on 2026-03-19
- 2026-03-19 tail `75` labels=['1'] → hit on 2026-03-20
- 2026-03-21 tail `38` labels=['0'] → hit on 2026-03-22

### MN / MODEL::combo-no-token / same_strict
- 2026-03-27 tail `46` labels=['1'] → hit on 2026-03-28
- 2026-03-30 tail `78` labels=['0'] → hit on 2026-03-31
- 2026-04-04 tail `13` labels=['1'] → hit on 2026-04-05

### MN / MODEL::combo-super / same_any
- 2026-03-10 tail `35` labels=['0'] → hit on 2026-03-11
- 2026-03-12 tail `23` labels=['0'] → hit on 2026-03-13
- 2026-03-12 tail `14` labels=['1'] → hit on 2026-03-13
- 2026-03-13 tail `45` labels=['1'] → hit on 2026-03-14
- 2026-03-14 tail `04` labels=['0'] → hit on 2026-03-15

### MN / MODEL::deepseek-chat / same_any
- 2026-03-13 tail `46` labels=['1'] → hit on 2026-03-14
- 2026-03-17 tail `52` labels=['0'] → hit on 2026-03-18
- 2026-03-17 tail `74` labels=['1'] → hit on 2026-03-18
- 2026-03-19 tail `85` labels=['1'] → hit on 2026-03-20
- 2026-03-20 tail `64` labels=['0'] → hit on 2026-03-21

### MN / MODEL::deepseek-reasoner / same_any
- 2026-03-13 tail `45` labels=['1'] → hit on 2026-03-14
- 2026-03-17 tail `74` labels=['0'] → hit on 2026-03-18
- 2026-03-20 tail `41` labels=['0'] → hit on 2026-03-21
- 2026-03-22 tail `71` labels=['1'] → hit on 2026-03-23
- 2026-03-25 tail `07` labels=['0'] → hit on 2026-03-26

### MN / MODEL::deepseek-reasoner / same_strict
- 2026-03-22 tail `71` labels=['1'] → hit on 2026-03-23
- 2026-04-12 tail `31` labels=['1'] → hit on 2026-04-13
- 2026-05-06 tail `93` labels=['1'] → hit on 2026-05-07

### MN / MODEL::deepseek-v4-flash / same_any
- 2026-04-27 tail `81` labels=['1'] → hit on 2026-04-28
- 2026-04-28 tail `64` labels=['0'] → hit on 2026-04-29
- 2026-04-28 tail `86` labels=['1'] → hit on 2026-04-29
- 2026-04-29 tail `82` labels=['0'] → hit on 2026-04-30
- 2026-04-29 tail `85` labels=['1'] → hit on 2026-04-30

### MN / MODEL::deepseek-v4-pro / same_any
- 2026-04-28 tail `64` labels=['0'] → hit on 2026-04-29
- 2026-04-29 tail `85` labels=['0'] → hit on 2026-04-30
- 2026-04-29 tail `82` labels=['1'] → hit on 2026-04-30
- 2026-05-02 tail `64` labels=['1'] → hit on 2026-05-03
- 2026-05-05 tail `56` labels=['1'] → hit on 2026-05-06

### MN / MODEL::gemini-2.5-flash / same_any
- 2026-03-10 tail `35` labels=['1'] → hit on 2026-03-11
- 2026-03-11 tail `61` labels=['1'] → hit on 2026-03-12
- 2026-03-13 tail `45` labels=['0'] → hit on 2026-03-14
- 2026-03-17 tail `74` labels=['1'] → hit on 2026-03-18
- 2026-03-20 tail `41` labels=['1'] → hit on 2026-03-21

### MN / MODEL::gemini-2.5-flash / same_strict
- 2026-03-15 tail `15` labels=['1'] → hit on 2026-03-16
- 2026-04-01 tail `76` labels=['1'] → hit on 2026-04-02

### MN / MODEL::gemini-2.5-pro / same_any
- 2026-03-10 tail `35` labels=['1'] → hit on 2026-03-11
- 2026-03-11 tail `61` labels=['1'] → hit on 2026-03-12
- 2026-03-14 tail `43` labels=['1'] → hit on 2026-03-15
- 2026-03-15 tail `87` labels=['1'] → hit on 2026-03-16
- 2026-03-17 tail `74` labels=['0'] → hit on 2026-03-18

### MN / MODEL::gemini-2.5-pro / same_strict
- 2026-03-22 tail `71` labels=['0'] → hit on 2026-03-23

### MN / MODEL::gemini-3-flash / same_any
- 2026-05-05 tail `13` labels=['0'] → hit on 2026-05-06
- 2026-05-06 tail `95` labels=['1'] → hit on 2026-05-07
- 2026-05-07 tail `32` labels=['0'] → hit on 2026-05-08
- 2026-05-08 tail `94` labels=['0'] → hit on 2026-05-09

### MN / MODEL::gemini-3-flash / same_strict
- 2026-05-06 tail `93` labels=['0'] → hit on 2026-05-07

### MN / MODEL::gemini-3.1-pro / same_any
- 2026-05-05 tail `56` labels=['0'] → hit on 2026-05-06
- 2026-05-05 tail `13` labels=['1'] → hit on 2026-05-06
- 2026-05-06 tail `95` labels=['0'] → hit on 2026-05-07
- 2026-05-08 tail `94` labels=['0'] → hit on 2026-05-09
- 2026-05-08 tail `51` labels=['1'] → hit on 2026-05-09

### MN / MODEL::gemma-4-31b / same_any
- 2026-05-05 tail `13` labels=['0'] → hit on 2026-05-06
- 2026-05-05 tail `05` labels=['1'] → hit on 2026-05-06
- 2026-05-06 tail `95` labels=['0'] → hit on 2026-05-07
- 2026-05-06 tail `27` labels=['1'] → hit on 2026-05-07
- 2026-05-07 tail `32` labels=['1'] → hit on 2026-05-08

### MN / MODEL::gemma-4-31b / same_strict
- 2026-05-05 tail `05` labels=['1'] → hit on 2026-05-06

### MN / MODEL::glm-5.1 / same_any
- 2026-04-14 tail `04` labels=['0'] → hit on 2026-04-15
- 2026-04-15 tail `42` labels=['0'] → hit on 2026-04-16
- 2026-04-18 tail `62` labels=['1'] → hit on 2026-04-19
- 2026-04-20 tail `57` labels=['0'] → hit on 2026-04-21
- 2026-04-25 tail `32` labels=['0'] → hit on 2026-04-26

### MN / MODEL::glm-5.1 / same_strict
- 2026-04-24 tail `57` labels=['1'] → hit on 2026-04-25

### MN / MODEL::gpt-5-mini / same_any
- 2026-03-17 tail `52` labels=['0'] → hit on 2026-03-18
- 2026-03-17 tail `74` labels=['1'] → hit on 2026-03-18
- 2026-03-19 tail `85` labels=['0'] → hit on 2026-03-20
- 2026-03-20 tail `52` labels=['1'] → hit on 2026-03-21
- 2026-03-24 tail `89` labels=['1'] → hit on 2026-03-25

### MN / MODEL::gpt-5-mini / same_strict
- 2026-04-12 tail `31` labels=['1'] → hit on 2026-04-13
- 2026-05-06 tail `93` labels=['0'] → hit on 2026-05-07

### MN / MODEL::gpt-5.4 / same_any
- 2026-03-24 tail `95` labels=['0'] → hit on 2026-03-25
- 2026-03-27 tail `82` labels=['0'] → hit on 2026-03-28
- 2026-03-27 tail `93` labels=['1'] → hit on 2026-03-28
- 2026-03-30 tail `27` labels=['1'] → hit on 2026-03-31
- 2026-04-01 tail `67` labels=['1'] → hit on 2026-04-02

### MN / MODEL::gpt-5.4 / same_strict
- 2026-04-14 tail `03` labels=['1'] → hit on 2026-04-15
- 2026-04-28 tail `46` labels=['1'] → hit on 2026-04-29

### MN / MODEL::gpt-5.5 / same_any
- 2026-04-27 tail `28` labels=['1'] → hit on 2026-04-28
- 2026-04-28 tail `64` labels=['0'] → hit on 2026-04-29
- 2026-04-29 tail `85` labels=['0'] → hit on 2026-04-30
- 2026-05-01 tail `74` labels=['0'] → hit on 2026-05-02
- 2026-05-01 tail `51` labels=['1'] → hit on 2026-05-02

### MN / MODEL::gpt-5.5 / same_strict
- 2026-05-06 tail `93` labels=['1'] → hit on 2026-05-07

### MN / MODEL::gpt-oss-120b / same_any
- 2026-04-20 tail `45` labels=['0'] → hit on 2026-04-21
- 2026-04-21 tail `12` labels=['1'] → hit on 2026-04-22
- 2026-04-24 tail `02` labels=['1'] → hit on 2026-04-25
- 2026-04-25 tail `05` labels=['0'] → hit on 2026-04-26
- 2026-04-25 tail `32` labels=['1'] → hit on 2026-04-26

### MN / MODEL::gpt-oss-120b / same_strict
- 2026-04-22 tail `53` labels=['0'] → hit on 2026-04-23

### MN / MODEL::grok-4.20-multi-agent / same_any
- 2026-04-15 tail `42` labels=['0'] → hit on 2026-04-16
- 2026-04-15 tail `33` labels=['1'] → hit on 2026-04-16
- 2026-04-17 tail `47` labels=['1'] → hit on 2026-04-18
- 2026-04-20 tail `57` labels=['1'] → hit on 2026-04-21
- 2026-04-21 tail `19` labels=['1'] → hit on 2026-04-22

### MN / MODEL::grok-4.20-multi-agent / same_strict
- 2026-04-22 tail `53` labels=['1'] → hit on 2026-04-23
- 2026-05-06 tail `93` labels=['0'] → hit on 2026-05-07

### MN / MODEL::kimi-k2.5 / same_any
- 2026-04-17 tail `47` labels=['1'] → hit on 2026-04-18
- 2026-04-18 tail `62` labels=['1'] → hit on 2026-04-19
- 2026-04-24 tail `52` labels=['1'] → hit on 2026-04-25
- 2026-04-26 tail `71` labels=['0'] → hit on 2026-04-27
- 2026-04-29 tail `82` labels=['0'] → hit on 2026-04-30

### MN / MODEL::kimi-k2.6 / same_any
- 2026-04-25 tail `32` labels=['1'] → hit on 2026-04-26
- 2026-04-26 tail `71` labels=['0'] → hit on 2026-04-27
- 2026-04-26 tail `69` labels=['1'] → hit on 2026-04-27

### MN / MODEL::llama-4-maverick / same_any
- 2026-04-20 tail `45` labels=['1'] → hit on 2026-04-21
- 2026-04-22 tail `22` labels=['0'] → hit on 2026-04-23

### MN / MODEL::lstm / same_any
- 2026-03-10 tail `56` labels=['1'] → hit on 2026-03-11
- 2026-03-14 tail `56` labels=['1'] → hit on 2026-03-15
- 2026-03-15 tail `90` labels=['0'] → hit on 2026-03-16
- 2026-03-17 tail `81` labels=['1'] → hit on 2026-03-18
- 2026-03-18 tail `92` labels=['1'] → hit on 2026-03-19

### MN / MODEL::lstm / same_strict
- 2026-04-02 tail `33` labels=['0'] → hit on 2026-04-03
- 2026-05-07 tail `34` labels=['0'] → hit on 2026-05-08

### MN / MODEL::meta-learning / same_any
- 2026-03-13 tail `44` labels=['1'] → hit on 2026-03-14
- 2026-03-14 tail `09` labels=['1'] → hit on 2026-03-15
- 2026-03-15 tail `01` labels=['0'] → hit on 2026-03-16
- 2026-03-16 tail `88` labels=['0'] → hit on 2026-03-17
- 2026-03-21 tail `38` labels=['1'] → hit on 2026-03-22

### MN / MODEL::meta-learning / same_strict
- 2026-03-20 tail `61` labels=['1'] → hit on 2026-03-21

### MN / MODEL::minimax-m2.7 / same_any
- 2026-04-16 tail `26` labels=['1'] → hit on 2026-04-17
- 2026-04-17 tail `47` labels=['1'] → hit on 2026-04-18
- 2026-04-19 tail `46` labels=['0'] → hit on 2026-04-20
- 2026-04-20 tail `57` labels=['0'] → hit on 2026-04-21
- 2026-04-21 tail `19` labels=['1'] → hit on 2026-04-22

### MN / MODEL::mistral-large-3 / same_any
- 2026-04-20 tail `45` labels=['0'] → hit on 2026-04-21
- 2026-04-21 tail `19` labels=['1'] → hit on 2026-04-22
- 2026-04-22 tail `22` labels=['0'] → hit on 2026-04-23

### MN / MODEL::mistral-nemo / same_any
- 2026-04-19 tail `64` labels=['0'] → hit on 2026-04-20
- 2026-04-19 tail `46` labels=['1'] → hit on 2026-04-20

### MN / MODEL::nemotron-3-super / same_any
- 2026-04-16 tail `76` labels=['0'] → hit on 2026-04-17

### MN / MODEL::qwen3-coder / same_any
- 2026-04-20 tail `45` labels=['1'] → hit on 2026-04-21
- 2026-04-22 tail `22` labels=['0'] → hit on 2026-04-23
- 2026-04-24 tail `02` labels=['0'] → hit on 2026-04-25
- 2026-04-25 tail `32` labels=['0'] → hit on 2026-04-26
- 2026-04-25 tail `05` labels=['1'] → hit on 2026-04-26

### MN / MODEL::qwen3-coder / same_strict
- 2026-05-06 tail `93` labels=['0'] → hit on 2026-05-07

### MN / MODEL::qwen3-max-thinking / same_any
- 2026-04-17 tail `30` labels=['1'] → hit on 2026-04-18
- 2026-04-21 tail `19` labels=['1'] → hit on 2026-04-22
- 2026-04-24 tail `02` labels=['1'] → hit on 2026-04-25
- 2026-04-25 tail `32` labels=['0'] → hit on 2026-04-26
- 2026-04-26 tail `71` labels=['0'] → hit on 2026-04-27

### MN / MODEL::qwen3-max-thinking / same_strict
- 2026-04-22 tail `53` labels=['0'] → hit on 2026-04-23

### MN / MODEL::qwen3.6-plus / same_any
- 2026-04-14 tail `64` labels=['1'] → hit on 2026-04-15
- 2026-04-15 tail `42` labels=['0'] → hit on 2026-04-16
- 2026-04-27 tail `74` labels=['1'] → hit on 2026-04-28
- 2026-04-28 tail `64` labels=['0'] → hit on 2026-04-29
- 2026-04-29 tail `28` labels=['0'] → hit on 2026-04-30

### MN / MODEL::qwen3.6-plus / same_strict
- 2026-05-06 tail `93` labels=['0'] → hit on 2026-05-07

### MN / MODEL::random-forest / same_any
- 2026-03-11 tail `85` labels=['1'] → hit on 2026-03-12
- 2026-03-12 tail `19` labels=['1'] → hit on 2026-03-13
- 2026-03-13 tail `51` labels=['0'] → hit on 2026-03-14
- 2026-03-13 tail `44` labels=['1'] → hit on 2026-03-14
- 2026-03-14 tail `09` labels=['1'] → hit on 2026-03-15

### MN / MODEL::random-forest / same_strict
- 2026-03-12 tail `19` labels=['1'] → hit on 2026-03-13
- 2026-03-20 tail `61` labels=['1'] → hit on 2026-03-21
- 2026-03-30 tail `78` labels=['0'] → hit on 2026-03-31
- 2026-04-04 tail `13` labels=['0'] → hit on 2026-04-05
- 2026-04-10 tail `49` labels=['0'] → hit on 2026-04-11

### MN / MODEL::smart-ensemble / same_any
- 2026-03-15 tail `90` labels=['0'] → hit on 2026-03-16
- 2026-03-16 tail `88` labels=['1'] → hit on 2026-03-17
- 2026-03-18 tail `92` labels=['0'] → hit on 2026-03-19
- 2026-03-19 tail `90` labels=['0'] → hit on 2026-03-20
- 2026-03-19 tail `16` labels=['1'] → hit on 2026-03-20

### MN / MODEL::smart-ensemble / same_strict
- 2026-03-27 tail `46` labels=['1'] → hit on 2026-03-28
- 2026-03-30 tail `78` labels=['0'] → hit on 2026-03-31
- 2026-04-04 tail `13` labels=['1'] → hit on 2026-04-05

### MN / MODEL::smart-ml / same_any
- 2026-03-11 tail `85` labels=['0'] → hit on 2026-03-12
- 2026-03-12 tail `19` labels=['0'] → hit on 2026-03-13
- 2026-03-13 tail `51` labels=['0'] → hit on 2026-03-14
- 2026-03-13 tail `97` labels=['1'] → hit on 2026-03-14
- 2026-03-14 tail `09` labels=['1'] → hit on 2026-03-15

### MN / MODEL::smart-ml / same_strict
- 2026-03-12 tail `19` labels=['0'] → hit on 2026-03-13
- 2026-03-30 tail `78` labels=['0'] → hit on 2026-03-31
- 2026-04-04 tail `13` labels=['0'] → hit on 2026-04-05
- 2026-04-10 tail `49` labels=['0'] → hit on 2026-04-11

### MN / MODEL::xgboost / same_any
- 2026-03-12 tail `19` labels=['0'] → hit on 2026-03-13
- 2026-03-13 tail `97` labels=['0'] → hit on 2026-03-14
- 2026-03-14 tail `09` labels=['1'] → hit on 2026-03-15
- 2026-03-15 tail `26` labels=['0'] → hit on 2026-03-16
- 2026-03-19 tail `16` labels=['0'] → hit on 2026-03-20

### MN / MODEL::xgboost / same_strict
- 2026-03-12 tail `19` labels=['0'] → hit on 2026-03-13
- 2026-03-27 tail `58` labels=['1'] → hit on 2026-03-28
- 2026-03-30 tail `78` labels=['0'] → hit on 2026-03-31
- 2026-04-04 tail `13` labels=['0'] → hit on 2026-04-05

### MN / MODEL_MAIN / same_any
- 2026-03-10 tail `56` labels=['lstm[1]'] → hit on 2026-03-11
- 2026-03-10 tail `35` labels=['claude-sonnet-4-6[0]', 'combo-super[0]', 'gemini-2.5-flash[1]', 'gemini-2.5-pro[1]'] → hit on 2026-03-11
- 2026-03-11 tail `85` labels=['random-forest[1]', 'smart-ml[0]'] → hit on 2026-03-12
- 2026-03-11 tail `61` labels=['gemini-2.5-flash[1]', 'gemini-2.5-pro[1]'] → hit on 2026-03-12
- 2026-03-12 tail `19` labels=['random-forest[1]', 'smart-ml[0]', 'xgboost[0]'] → hit on 2026-03-13

### MN / MODEL_MAIN / same_strict
- 2026-03-12 tail `19` labels=['random-forest[1]', 'smart-ml[0]', 'xgboost[0]'] → hit on 2026-03-13
- 2026-03-15 tail `15` labels=['gemini-2.5-flash[1]'] → hit on 2026-03-16
- 2026-03-20 tail `61` labels=['meta-learning[1]', 'random-forest[1]'] → hit on 2026-03-21
- 2026-03-22 tail `71` labels=['deepseek-reasoner[1]', 'gemini-2.5-pro[0]'] → hit on 2026-03-23
- 2026-03-27 tail `58` labels=['xgboost[1]'] → hit on 2026-03-28

### MN / OFFICIAL_BT / same_any
- 2026-03-17 tail `74` labels=['final_bundles.bach_thu'] → hit on 2026-03-18
- 2026-03-20 tail `52` labels=['final_bundles.bach_thu'] → hit on 2026-03-21
- 2026-03-30 tail `27` labels=['final_bundles.bach_thu'] → hit on 2026-03-31
- 2026-04-02 tail `61` labels=['final_bundles.bach_thu'] → hit on 2026-04-03
- 2026-04-04 tail `53` labels=['final_bundles.bach_thu'] → hit on 2026-04-05

### MN / OFFICIAL_LO2 / same_any
- 2026-03-12 tail `19` labels=['final_bundles.lo2'] → hit on 2026-03-13
- 2026-03-13 tail `45` labels=['final_bundles.lo2'] → hit on 2026-03-14
- 2026-03-14 tail `09` labels=['final_bundles.lo2'] → hit on 2026-03-15
- 2026-03-17 tail `74` labels=['final_bundles.lo2'] → hit on 2026-03-18
- 2026-03-17 tail `52` labels=['final_bundles.lo2'] → hit on 2026-03-18

### MN / OFFICIAL_LO2 / same_strict
- 2026-03-12 tail `19` labels=['final_bundles.lo2'] → hit on 2026-03-13

### MN / TEST_BT / same_any
- 2026-04-04 tail `53` labels=['MN_AI_CHAIN_PRESERVATION_V1', 'MN_NO_TOKEN_HERD_REDUCTION_V1', 'MN_OFFICIAL_BASELINE_CONTROL', 'MN_STRENGTH_WEIGHTED_V52_5_2'] → hit on 2026-04-05
- 2026-04-04 tail `83` labels=['MN_SPECIALIST_ROSTER_V1'] → hit on 2026-04-05
- 2026-04-09 tail `32` labels=['MN_NO_TOKEN_HERD_REDUCTION_V1', 'MN_OFFICIAL_BASELINE_CONTROL', 'MN_SPECIALIST_ROSTER_V1', 'MN_STRENGTH_WEIGHTED_V52_5_2'] → hit on 2026-04-10
- 2026-04-15 tail `98` labels=['MN_NO_TOKEN_HERD_REDUCTION_V1', 'MN_OFFICIAL_BASELINE_CONTROL', 'MN_SPECIALIST_ROSTER_V1', 'MN_STRENGTH_WEIGHTED_V52_5_2'] → hit on 2026-04-16
- 2026-04-15 tail `42` labels=['MN_AI_CHAIN_PRESERVATION_V1'] → hit on 2026-04-16

### MN / TEST_LO2 / same_any
- 2026-04-04 tail `53` labels=['MN_AI_CHAIN_PRESERVATION_V1', 'MN_NO_TOKEN_HERD_REDUCTION_V1', 'MN_OFFICIAL_BASELINE_CONTROL', 'MN_PRIOR_REGION_CONTEXT_SAFE_V1', 'MN_SPECIALIST_ROSTER_V1'] → hit on 2026-04-05
- 2026-04-04 tail `83` labels=['MN_AI_CHAIN_PRESERVATION_V1', 'MN_NO_TOKEN_HERD_REDUCTION_V1', 'MN_OFFICIAL_BASELINE_CONTROL', 'MN_PRIOR_REGION_CONTEXT_SAFE_V1', 'MN_SPECIALIST_ROSTER_V1'] → hit on 2026-04-05
- 2026-04-09 tail `32` labels=['MN_AI_CHAIN_PRESERVATION_V1', 'MN_NO_TOKEN_HERD_REDUCTION_V1', 'MN_OFFICIAL_BASELINE_CONTROL', 'MN_PRIOR_REGION_CONTEXT_SAFE_V1', 'MN_SPECIALIST_ROSTER_V1'] → hit on 2026-04-10
- 2026-04-13 tail `24` labels=['MN_AI_CHAIN_PRESERVATION_V1', 'MN_NO_TOKEN_HERD_REDUCTION_V1', 'MN_OFFICIAL_BASELINE_CONTROL', 'MN_PRIOR_REGION_CONTEXT_SAFE_V1', 'MN_SPECIALIST_ROSTER_V1'] → hit on 2026-04-14
- 2026-04-14 tail `04` labels=['MN_AI_CHAIN_PRESERVATION_V1', 'MN_NO_TOKEN_HERD_REDUCTION_V1', 'MN_OFFICIAL_BASELINE_CONTROL', 'MN_PRIOR_REGION_CONTEXT_SAFE_V1', 'MN_SPECIALIST_ROSTER_V1'] → hit on 2026-04-15

### MN / V101_MN_D1_D2 / same_any
- 2026-04-26 tail `57` labels=['rank=1,score=9.06'] → hit on 2026-04-27
- 2026-04-26 tail `71` labels=['rank=3,score=8.36'] → hit on 2026-04-27
- 2026-04-26 tail `91` labels=['rank=9,score=6.24'] → hit on 2026-04-27
- 2026-04-27 tail `81` labels=['rank=2,score=8.36'] → hit on 2026-04-28
- 2026-04-27 tail `62` labels=['rank=3,score=8.0'] → hit on 2026-04-28

### MN / V101_MN_D1_D2 / same_strict
- 2026-04-28 tail `91` labels=['rank=9,score=6.59'] → hit on 2026-04-29
- 2026-04-30 tail `30` labels=['rank=2,score=7.3'] → hit on 2026-05-01
- 2026-05-03 tail `25` labels=['rank=6,score=7.56'] → hit on 2026-05-04
- 2026-05-06 tail `93` labels=['rank=10,score=6.45'] → hit on 2026-05-07
- 2026-05-08 tail `89` labels=['rank=5,score=6.85'] → hit on 2026-05-09

### MN / V67 / same_any
- 2026-05-08 tail `94` labels=['adaptive_exploit_v67_candidate_trace:score=3.6098'] → hit on 2026-05-09

### MN / V70 / same_any
- 2026-05-04 tail `65` labels=['consensus_v1_trace:agreement_count=3'] → hit on 2026-05-05
- 2026-05-05 tail `15` labels=['consensus_v1_trace:agreement_count=3'] → hit on 2026-05-06
- 2026-05-06 tail `95` labels=['consensus_v1_trace:agreement_count=6'] → hit on 2026-05-07
- 2026-05-08 tail `13` labels=['consensus_v1_trace:agreement_count=5'] → hit on 2026-05-09
- 2026-05-08 tail `94` labels=['consensus_v1_trace:agreement_count=2'] → hit on 2026-05-09

### MN / V73 / same_any
- 2026-05-04 tail `65` labels=['hybrid_v1_trace:confidence_tier=HIGH'] → hit on 2026-05-05
- 2026-05-05 tail `15` labels=['hybrid_v1_trace:confidence_tier=HIGH'] → hit on 2026-05-06
- 2026-05-06 tail `95` labels=['hybrid_v1_trace:confidence_tier=HIGH'] → hit on 2026-05-07
- 2026-05-08 tail `94` labels=['hybrid_v1_trace:confidence_tier=AURA'] → hit on 2026-05-09

### MN->MB / MODEL::claude-opus-4-20250514 / cross_next
- 2026-03-13 tail `05` labels=['1'] → hit on 2026-03-14
- 2026-03-17 tail `74` labels=['1'] → hit on 2026-03-18
- 2026-03-18 tail `93` labels=['0'] → hit on 2026-03-19
- 2026-03-18 tail `73` labels=['1'] → hit on 2026-03-19
- 2026-03-28 tail `67` labels=['1'] → hit on 2026-03-29

### MN->MB / MODEL::claude-opus-4-20250514 / cross_same
- 2026-03-11 tail `28` labels=['1'] → hit on 2026-03-11
- 2026-03-17 tail `52` labels=['0'] → hit on 2026-03-17
- 2026-03-22 tail `61` labels=['1'] → hit on 2026-03-22
- 2026-03-30 tail `27` labels=['0'] → hit on 2026-03-30
- 2026-04-01 tail `21` labels=['0'] → hit on 2026-04-01

### MN->MB / MODEL::claude-sonnet-4-6 / cross_next
- 2026-03-11 tail `93` labels=['0'] → hit on 2026-03-12
- 2026-03-13 tail `05` labels=['1'] → hit on 2026-03-14
- 2026-03-17 tail `74` labels=['0'] → hit on 2026-03-18
- 2026-03-19 tail `14` labels=['1'] → hit on 2026-03-20
- 2026-03-20 tail `52` labels=['0'] → hit on 2026-03-21

### MN->MB / MODEL::claude-sonnet-4-6 / cross_same
- 2026-03-19 tail `73` labels=['0'] → hit on 2026-03-19
- 2026-03-22 tail `61` labels=['1'] → hit on 2026-03-22
- 2026-03-27 tail `65` labels=['1'] → hit on 2026-03-27
- 2026-03-30 tail `27` labels=['0'] → hit on 2026-03-30
- 2026-04-01 tail `21` labels=['1'] → hit on 2026-04-01

### MN->MB / MODEL::combo-no-token / cross_next
- 2026-03-13 tail `44` labels=['1'] → hit on 2026-03-14
- 2026-03-21 tail `38` labels=['0'] → hit on 2026-03-22
- 2026-03-23 tail `90` labels=['0'] → hit on 2026-03-24
- 2026-03-23 tail `31` labels=['1'] → hit on 2026-03-24
- 2026-03-25 tail `93` labels=['0'] → hit on 2026-03-26

### MN->MB / MODEL::combo-no-token / cross_same
- 2026-03-10 tail `95` labels=['1'] → hit on 2026-03-10
- 2026-03-17 tail `90` labels=['1'] → hit on 2026-03-17
- 2026-03-23 tail `90` labels=['0'] → hit on 2026-03-23
- 2026-03-23 tail `31` labels=['1'] → hit on 2026-03-23
- 2026-03-26 tail `94` labels=['1'] → hit on 2026-03-26

### MN->MB / MODEL::combo-super / cross_next
- 2026-03-13 tail `05` labels=['0'] → hit on 2026-03-14
- 2026-03-15 tail `87` labels=['2'] → hit on 2026-03-16
- 2026-03-17 tail `74` labels=['1'] → hit on 2026-03-18
- 2026-03-18 tail `93` labels=['0'] → hit on 2026-03-19
- 2026-03-19 tail `14` labels=['1'] → hit on 2026-03-20

### MN->MB / MODEL::combo-super / cross_same
- 2026-03-10 tail `95` labels=['2'] → hit on 2026-03-10
- 2026-03-11 tail `28` labels=['0'] → hit on 2026-03-11
- 2026-03-13 tail `64` labels=['2'] → hit on 2026-03-13
- 2026-03-20 tail `93` labels=['1'] → hit on 2026-03-20
- 2026-03-22 tail `46` labels=['0'] → hit on 2026-03-22

### MN->MB / MODEL::deepseek-chat / cross_next
- 2026-03-12 tail `15` labels=['1'] → hit on 2026-03-13
- 2026-03-17 tail `74` labels=['1'] → hit on 2026-03-18
- 2026-03-18 tail `93` labels=['1'] → hit on 2026-03-19
- 2026-03-20 tail `52` labels=['1'] → hit on 2026-03-21

### MN->MB / MODEL::deepseek-chat / cross_same
- 2026-03-11 tail `28` labels=['1'] → hit on 2026-03-11
- 2026-03-17 tail `52` labels=['0'] → hit on 2026-03-17
- 2026-03-20 tail `64` labels=['0'] → hit on 2026-03-20
- 2026-03-22 tail `61` labels=['0'] → hit on 2026-03-22

### MN->MB / MODEL::deepseek-reasoner / cross_next
- 2026-03-13 tail `05` labels=['0'] → hit on 2026-03-14
- 2026-03-17 tail `74` labels=['0'] → hit on 2026-03-18
- 2026-03-17 tail `64` labels=['1'] → hit on 2026-03-18
- 2026-03-21 tail `13` labels=['0'] → hit on 2026-03-22
- 2026-03-22 tail `92` labels=['0'] → hit on 2026-03-23

### MN->MB / MODEL::deepseek-reasoner / cross_same
- 2026-03-11 tail `28` labels=['0'] → hit on 2026-03-11
- 2026-03-25 tail `07` labels=['0'] → hit on 2026-03-25
- 2026-03-25 tail `51` labels=['1'] → hit on 2026-03-25
- 2026-03-30 tail `28` labels=['1'] → hit on 2026-03-30
- 2026-04-03 tail `09` labels=['1'] → hit on 2026-04-03

### MN->MB / MODEL::deepseek-v4-flash / cross_next
- 2026-05-02 tail `37` labels=['0'] → hit on 2026-05-03
- 2026-05-03 tail `14` labels=['0'] → hit on 2026-05-04
- 2026-05-05 tail `41` labels=['1'] → hit on 2026-05-06
- 2026-05-07 tail `05` labels=['0'] → hit on 2026-05-08

### MN->MB / MODEL::deepseek-v4-flash / cross_same
- 2026-04-27 tail `81` labels=['1'] → hit on 2026-04-27
- 2026-05-02 tail `37` labels=['0'] → hit on 2026-05-02
- 2026-05-06 tail `95` labels=['0'] → hit on 2026-05-06
- 2026-05-07 tail `40` labels=['1'] → hit on 2026-05-07
- 2026-05-08 tail `93` labels=['1'] → hit on 2026-05-08

### MN->MB / MODEL::deepseek-v4-pro / cross_next
- 2026-05-02 tail `64` labels=['1'] → hit on 2026-05-03
- 2026-05-07 tail `05` labels=['0'] → hit on 2026-05-08

### MN->MB / MODEL::deepseek-v4-pro / cross_same
- 2026-04-27 tail `64` labels=['1'] → hit on 2026-04-27
- 2026-05-01 tail `19` labels=['1'] → hit on 2026-05-01
- 2026-05-04 tail `42` labels=['1'] → hit on 2026-05-04
- 2026-05-06 tail `95` labels=['0'] → hit on 2026-05-06
- 2026-05-07 tail `50` labels=['1'] → hit on 2026-05-07

### MN->MB / MODEL::gemini-2.5-flash / cross_next
- 2026-03-17 tail `74` labels=['1'] → hit on 2026-03-18
- 2026-03-18 tail `93` labels=['0'] → hit on 2026-03-19
- 2026-03-29 tail `46` labels=['0'] → hit on 2026-03-30
- 2026-03-29 tail `38` labels=['1'] → hit on 2026-03-30
- 2026-03-31 tail `09` labels=['0'] → hit on 2026-04-01

### MN->MB / MODEL::gemini-2.5-flash / cross_same
- 2026-03-20 tail `93` labels=['0'] → hit on 2026-03-20
- 2026-03-22 tail `61` labels=['0'] → hit on 2026-03-22
- 2026-03-27 tail `32` labels=['1'] → hit on 2026-03-27
- 2026-03-30 tail `28` labels=['1'] → hit on 2026-03-30
- 2026-04-03 tail `09` labels=['0'] → hit on 2026-04-03

### MN->MB / MODEL::gemini-2.5-pro / cross_next
- 2026-03-15 tail `87` labels=['1'] → hit on 2026-03-16
- 2026-03-17 tail `74` labels=['0'] → hit on 2026-03-18
- 2026-03-20 tail `52` labels=['1'] → hit on 2026-03-21
- 2026-03-23 tail `24` labels=['0'] → hit on 2026-03-24
- 2026-03-24 tail `95` labels=['1'] → hit on 2026-03-25

### MN->MB / MODEL::gemini-2.5-pro / cross_same
- 2026-03-20 tail `93` labels=['0'] → hit on 2026-03-20
- 2026-03-22 tail `73` labels=['1'] → hit on 2026-03-22
- 2026-03-25 tail `07` labels=['0'] → hit on 2026-03-25
- 2026-03-30 tail `27` labels=['1'] → hit on 2026-03-30
- 2026-04-01 tail `21` labels=['0'] → hit on 2026-04-01

### MN->MB / MODEL::gemini-3-flash / cross_next
- 2026-05-05 tail `13` labels=['0'] → hit on 2026-05-06

### MN->MB / MODEL::gemini-3-flash / cross_same
- 2026-05-06 tail `95` labels=['1'] → hit on 2026-05-06
- 2026-05-08 tail `94` labels=['0'] → hit on 2026-05-08

### MN->MB / MODEL::gemini-3.1-pro / cross_next
- 2026-05-05 tail `13` labels=['1'] → hit on 2026-05-06

### MN->MB / MODEL::gemini-3.1-pro / cross_same
- 2026-05-06 tail `95` labels=['0'] → hit on 2026-05-06
- 2026-05-08 tail `94` labels=['0'] → hit on 2026-05-08

### MN->MB / MODEL::gemma-4-31b / cross_next
- 2026-05-05 tail `13` labels=['0'] → hit on 2026-05-06
- 2026-05-08 tail `13` labels=['1'] → hit on 2026-05-09

### MN->MB / MODEL::gemma-4-31b / cross_same
- 2026-05-05 tail `05` labels=['1'] → hit on 2026-05-05
- 2026-05-06 tail `95` labels=['0'] → hit on 2026-05-06
- 2026-05-08 tail `13` labels=['1'] → hit on 2026-05-08

### MN->MB / MODEL::glm-5.1 / cross_next
- 2026-04-18 tail `29` labels=['0'] → hit on 2026-04-19
- 2026-04-18 tail `62` labels=['1'] → hit on 2026-04-19
- 2026-04-21 tail `73` labels=['1'] → hit on 2026-04-22
- 2026-04-26 tail `71` labels=['0'] → hit on 2026-04-27
- 2026-05-05 tail `13` labels=['1'] → hit on 2026-05-06

### MN->MB / MODEL::glm-5.1 / cross_same
- 2026-04-13 tail `00` labels=['0'] → hit on 2026-04-13
- 2026-04-15 tail `14` labels=['1'] → hit on 2026-04-15
- 2026-04-20 tail `57` labels=['0'] → hit on 2026-04-20
- 2026-04-26 tail `71` labels=['0'] → hit on 2026-04-26
- 2026-05-04 tail `42` labels=['1'] → hit on 2026-05-04

### MN->MB / MODEL::gpt-5-mini / cross_next
- 2026-03-17 tail `74` labels=['1'] → hit on 2026-03-18
- 2026-03-18 tail `93` labels=['1'] → hit on 2026-03-19
- 2026-03-20 tail `52` labels=['1'] → hit on 2026-03-21
- 2026-03-25 tail `51` labels=['0'] → hit on 2026-03-26
- 2026-03-28 tail `31` labels=['0'] → hit on 2026-03-29

### MN->MB / MODEL::gpt-5-mini / cross_same
- 2026-03-17 tail `52` labels=['0'] → hit on 2026-03-17
- 2026-03-22 tail `61` labels=['0'] → hit on 2026-03-22
- 2026-03-25 tail `51` labels=['0'] → hit on 2026-03-25
- 2026-03-27 tail `32` labels=['1'] → hit on 2026-03-27
- 2026-03-30 tail `28` labels=['0'] → hit on 2026-03-30

### MN->MB / MODEL::gpt-5.4 / cross_next
- 2026-03-24 tail `95` labels=['0'] → hit on 2026-03-25
- 2026-03-25 tail `51` labels=['0'] → hit on 2026-03-26
- 2026-03-28 tail `67` labels=['1'] → hit on 2026-03-29
- 2026-04-01 tail `21` labels=['0'] → hit on 2026-04-02
- 2026-04-01 tail `67` labels=['1'] → hit on 2026-04-02

### MN->MB / MODEL::gpt-5.4 / cross_same
- 2026-03-25 tail `51` labels=['0'] → hit on 2026-03-25
- 2026-03-30 tail `27` labels=['1'] → hit on 2026-03-30
- 2026-04-01 tail `21` labels=['0'] → hit on 2026-04-01
- 2026-04-03 tail `09` labels=['0'] → hit on 2026-04-03
- 2026-04-11 tail `16` labels=['0'] → hit on 2026-04-11

### MN->MB / MODEL::gpt-5.5 / cross_next
- 2026-05-07 tail `05` labels=['1'] → hit on 2026-05-08

### MN->MB / MODEL::gpt-5.5 / cross_same
- 2026-04-27 tail `28` labels=['1'] → hit on 2026-04-27
- 2026-05-01 tail `51` labels=['1'] → hit on 2026-05-01
- 2026-05-04 tail `42` labels=['0'] → hit on 2026-05-04
- 2026-05-06 tail `95` labels=['0'] → hit on 2026-05-06
- 2026-05-08 tail `93` labels=['0'] → hit on 2026-05-08

### MN->MB / MODEL::gpt-oss-120b / cross_next
- 2026-04-25 tail `05` labels=['0'] → hit on 2026-04-26
- 2026-04-30 tail `81` labels=['1'] → hit on 2026-05-01
- 2026-05-05 tail `41` labels=['1'] → hit on 2026-05-06
- 2026-05-06 tail `21` labels=['0'] → hit on 2026-05-07
- 2026-05-08 tail `79` labels=['1'] → hit on 2026-05-09

### MN->MB / MODEL::gpt-oss-120b / cross_same
- 2026-04-26 tail `17` labels=['0'] → hit on 2026-04-26
- 2026-05-01 tail `51` labels=['1'] → hit on 2026-05-01
- 2026-05-04 tail `63` labels=['0'] → hit on 2026-05-04
- 2026-05-04 tail `42` labels=['1'] → hit on 2026-05-04
- 2026-05-08 tail `93` labels=['0'] → hit on 2026-05-08

### MN->MB / MODEL::grok-4.20-multi-agent / cross_next
- 2026-04-13 tail `91` labels=['1'] → hit on 2026-04-14
- 2026-04-15 tail `33` labels=['1'] → hit on 2026-04-16
- 2026-04-22 tail `22` labels=['0'] → hit on 2026-04-23
- 2026-04-25 tail `05` labels=['1'] → hit on 2026-04-26
- 2026-05-05 tail `41` labels=['1'] → hit on 2026-05-06

### MN->MB / MODEL::grok-4.20-multi-agent / cross_same
- 2026-04-13 tail `00` labels=['0'] → hit on 2026-04-13
- 2026-04-20 tail `73` labels=['0'] → hit on 2026-04-20
- 2026-04-20 tail `57` labels=['1'] → hit on 2026-04-20
- 2026-04-26 tail `17` labels=['1'] → hit on 2026-04-26
- 2026-04-27 tail `28` labels=['0'] → hit on 2026-04-27

### MN->MB / MODEL::kimi-k2.5 / cross_next
- 2026-04-16 tail `30` labels=['0'] → hit on 2026-04-17
- 2026-04-18 tail `29` labels=['0'] → hit on 2026-04-19
- 2026-04-18 tail `62` labels=['1'] → hit on 2026-04-19
- 2026-04-26 tail `71` labels=['0'] → hit on 2026-04-27
- 2026-04-30 tail `14` labels=['1'] → hit on 2026-05-01

### MN->MB / MODEL::kimi-k2.5 / cross_same
- 2026-04-20 tail `73` labels=['1'] → hit on 2026-04-20
- 2026-04-26 tail `71` labels=['0'] → hit on 2026-04-26
- 2026-04-26 tail `17` labels=['1'] → hit on 2026-04-26
- 2026-05-04 tail `42` labels=['1'] → hit on 2026-05-04
- 2026-05-07 tail `94` labels=['0'] → hit on 2026-05-07

### MN->MB / MODEL::kimi-k2.6 / cross_next
- 2026-04-26 tail `71` labels=['0'] → hit on 2026-04-27

### MN->MB / MODEL::kimi-k2.6 / cross_same
- 2026-04-26 tail `71` labels=['0'] → hit on 2026-04-26

### MN->MB / MODEL::llama-4-maverick / cross_next
- 2026-04-22 tail `22` labels=['0'] → hit on 2026-04-23

### MN->MB / MODEL::llama-4-maverick / cross_same
- 2026-04-19 tail `59` labels=['1'] → hit on 2026-04-19

### MN->MB / MODEL::lstm / cross_next
- 2026-03-10 tail `56` labels=['1'] → hit on 2026-03-11
- 2026-03-17 tail `81` labels=['1'] → hit on 2026-03-18
- 2026-03-19 tail `90` labels=['0'] → hit on 2026-03-20
- 2026-03-19 tail `81` labels=['1'] → hit on 2026-03-20
- 2026-03-21 tail `90` labels=['0'] → hit on 2026-03-22

### MN->MB / MODEL::lstm / cross_same
- 2026-03-10 tail `56` labels=['1'] → hit on 2026-03-10
- 2026-03-11 tail `28` labels=['0'] → hit on 2026-03-11
- 2026-03-13 tail `56` labels=['1'] → hit on 2026-03-13
- 2026-03-17 tail `90` labels=['0'] → hit on 2026-03-17
- 2026-03-19 tail `81` labels=['1'] → hit on 2026-03-19

### MN->MB / MODEL::meta-learning / cross_next
- 2026-03-12 tail `77` labels=['0'] → hit on 2026-03-13
- 2026-03-13 tail `44` labels=['1'] → hit on 2026-03-14
- 2026-03-21 tail `38` labels=['1'] → hit on 2026-03-22
- 2026-03-23 tail `31` labels=['0'] → hit on 2026-03-24
- 2026-03-25 tail `93` labels=['0'] → hit on 2026-03-26

### MN->MB / MODEL::meta-learning / cross_same
- 2026-03-10 tail `95` labels=['1'] → hit on 2026-03-10
- 2026-03-15 tail `01` labels=['0'] → hit on 2026-03-15
- 2026-03-16 tail `88` labels=['0'] → hit on 2026-03-16
- 2026-03-18 tail `75` labels=['1'] → hit on 2026-03-18
- 2026-03-23 tail `31` labels=['0'] → hit on 2026-03-23

### MN->MB / MODEL::minimax-m2.7 / cross_next
- 2026-04-18 tail `29` labels=['1'] → hit on 2026-04-19

### MN->MB / MODEL::minimax-m2.7 / cross_same
- 2026-04-20 tail `57` labels=['0'] → hit on 2026-04-20
- 2026-04-20 tail `47` labels=['1'] → hit on 2026-04-20
- 2026-04-26 tail `17` labels=['0'] → hit on 2026-04-26
- 2026-04-27 tail `28` labels=['1'] → hit on 2026-04-27

### MN->MB / MODEL::mistral-large-3 / cross_next
- 2026-04-22 tail `22` labels=['0'] → hit on 2026-04-23

### MN->MB / MODEL::mistral-nemo / cross_next
- 2026-04-21 tail `64` labels=['0'] → hit on 2026-04-22

### MN->MB / MODEL::mistral-nemo / cross_same
- 2026-04-19 tail `64` labels=['0'] → hit on 2026-04-19
- 2026-04-21 tail `64` labels=['0'] → hit on 2026-04-21

### MN->MB / MODEL::nemotron-3-super / cross_next
- 2026-04-16 tail `76` labels=['0'] → hit on 2026-04-17
- 2026-04-16 tail `30` labels=['1'] → hit on 2026-04-17

### MN->MB / MODEL::nemotron-3-super / cross_same
- 2026-04-16 tail `76` labels=['0'] → hit on 2026-04-16

### MN->MB / MODEL::qwen3-coder / cross_next
- 2026-04-13 tail `91` labels=['1'] → hit on 2026-04-14
- 2026-04-22 tail `22` labels=['0'] → hit on 2026-04-23
- 2026-04-25 tail `05` labels=['1'] → hit on 2026-04-26
- 2026-05-03 tail `14` labels=['0'] → hit on 2026-05-04
- 2026-05-05 tail `41` labels=['1'] → hit on 2026-05-06

### MN->MB / MODEL::qwen3-coder / cross_same
- 2026-04-13 tail `00` labels=['0'] → hit on 2026-04-13
- 2026-04-26 tail `17` labels=['0'] → hit on 2026-04-26
- 2026-04-27 tail `28` labels=['0'] → hit on 2026-04-27
- 2026-04-30 tail `75` labels=['1'] → hit on 2026-04-30
- 2026-05-01 tail `51` labels=['0'] → hit on 2026-05-01

### MN->MB / MODEL::qwen3-max-thinking / cross_next
- 2026-04-26 tail `71` labels=['0'] → hit on 2026-04-27
- 2026-05-05 tail `13` labels=['0'] → hit on 2026-05-06
- 2026-05-07 tail `94` labels=['0'] → hit on 2026-05-08
- 2026-05-07 tail `05` labels=['1'] → hit on 2026-05-08

### MN->MB / MODEL::qwen3-max-thinking / cross_same
- 2026-04-17 tail `30` labels=['1'] → hit on 2026-04-17
- 2026-04-20 tail `73` labels=['1'] → hit on 2026-04-20
- 2026-04-26 tail `71` labels=['0'] → hit on 2026-04-26
- 2026-04-26 tail `17` labels=['1'] → hit on 2026-04-26
- 2026-04-29 tail `28` labels=['0'] → hit on 2026-04-29

### MN->MB / MODEL::qwen3.6-plus / cross_next
- 2026-04-14 tail `02` labels=['0'] → hit on 2026-04-15
- 2026-05-05 tail `13` labels=['1'] → hit on 2026-05-06
- 2026-05-06 tail `25` labels=['1'] → hit on 2026-05-07
- 2026-05-08 tail `79` labels=['1'] → hit on 2026-05-09

### MN->MB / MODEL::qwen3.6-plus / cross_same
- 2026-04-13 tail `00` labels=['0'] → hit on 2026-04-13
- 2026-04-15 tail `30` labels=['1'] → hit on 2026-04-15
- 2026-04-29 tail `28` labels=['0'] → hit on 2026-04-29
- 2026-04-30 tail `75` labels=['1'] → hit on 2026-04-30
- 2026-05-01 tail `81` labels=['1'] → hit on 2026-05-01

### MN->MB / MODEL::random-forest / cross_next
- 2026-03-13 tail `44` labels=['1'] → hit on 2026-03-14
- 2026-03-21 tail `38` labels=['0'] → hit on 2026-03-22
- 2026-03-23 tail `90` labels=['0'] → hit on 2026-03-24
- 2026-03-23 tail `31` labels=['1'] → hit on 2026-03-24
- 2026-03-25 tail `51` labels=['1'] → hit on 2026-03-26

### MN->MB / MODEL::random-forest / cross_same
- 2026-03-10 tail `95` labels=['1'] → hit on 2026-03-10
- 2026-03-14 tail `31` labels=['0'] → hit on 2026-03-14
- 2026-03-15 tail `44` labels=['0'] → hit on 2026-03-15
- 2026-03-22 tail `39` labels=['1'] → hit on 2026-03-22
- 2026-03-23 tail `90` labels=['0'] → hit on 2026-03-23

### MN->MB / MODEL::smart-ensemble / cross_next
- 2026-03-13 tail `31` labels=['0'] → hit on 2026-03-14
- 2026-03-19 tail `90` labels=['0'] → hit on 2026-03-20
- 2026-03-19 tail `16` labels=['1'] → hit on 2026-03-20
- 2026-03-23 tail `90` labels=['0'] → hit on 2026-03-24
- 2026-03-24 tail `51` labels=['0'] → hit on 2026-03-25

### MN->MB / MODEL::smart-ensemble / cross_same
- 2026-03-11 tail `28` labels=['1'] → hit on 2026-03-11
- 2026-03-16 tail `88` labels=['1'] → hit on 2026-03-16
- 2026-03-17 tail `90` labels=['1'] → hit on 2026-03-17
- 2026-03-21 tail `92` labels=['1'] → hit on 2026-03-21
- 2026-03-22 tail `33` labels=['0'] → hit on 2026-03-22

### MN->MB / MODEL::smart-ml / cross_next
- 2026-03-21 tail `38` labels=['0'] → hit on 2026-03-22
- 2026-03-23 tail `31` labels=['1'] → hit on 2026-03-24
- 2026-03-24 tail `51` labels=['1'] → hit on 2026-03-25
- 2026-03-25 tail `93` labels=['0'] → hit on 2026-03-26
- 2026-03-26 tail `21` labels=['1'] → hit on 2026-03-27

### MN->MB / MODEL::smart-ml / cross_same
- 2026-03-10 tail `95` labels=['1'] → hit on 2026-03-10
- 2026-03-17 tail `62` labels=['0'] → hit on 2026-03-17
- 2026-03-18 tail `75` labels=['0'] → hit on 2026-03-18
- 2026-03-22 tail `39` labels=['0'] → hit on 2026-03-22
- 2026-03-23 tail `31` labels=['1'] → hit on 2026-03-23

### MN->MB / MODEL::xgboost / cross_next
- 2026-03-15 tail `26` labels=['0'] → hit on 2026-03-16
- 2026-03-19 tail `16` labels=['0'] → hit on 2026-03-20
- 2026-03-21 tail `38` labels=['0'] → hit on 2026-03-22
- 2026-03-23 tail `90` labels=['0'] → hit on 2026-03-24
- 2026-03-25 tail `93` labels=['0'] → hit on 2026-03-26

### MN->MB / MODEL::xgboost / cross_same
- 2026-03-15 tail `44` labels=['1'] → hit on 2026-03-15
- 2026-03-18 tail `75` labels=['0'] → hit on 2026-03-18
- 2026-03-22 tail `39` labels=['1'] → hit on 2026-03-22
- 2026-03-23 tail `90` labels=['0'] → hit on 2026-03-23
- 2026-03-26 tail `94` labels=['0'] → hit on 2026-03-26

### MN->MB / MODEL_MAIN / cross_next
- 2026-03-10 tail `56` labels=['lstm[1]'] → hit on 2026-03-11
- 2026-03-11 tail `93` labels=['claude-sonnet-4-6[0]'] → hit on 2026-03-12
- 2026-03-12 tail `77` labels=['meta-learning[0]'] → hit on 2026-03-13
- 2026-03-12 tail `15` labels=['deepseek-chat[1]'] → hit on 2026-03-13
- 2026-03-13 tail `31` labels=['smart-ensemble[0]'] → hit on 2026-03-14

### MN->MB / MODEL_MAIN / cross_same
- 2026-03-10 tail `95` labels=['combo-no-token[1]', 'combo-super[2]', 'meta-learning[1]', 'random-forest[1]', 'smart-ml[1]'] → hit on 2026-03-10
- 2026-03-10 tail `56` labels=['lstm[1]'] → hit on 2026-03-10
- 2026-03-11 tail `28` labels=['claude-opus-4-20250514[1]', 'combo-super[0]', 'deepseek-chat[1]', 'deepseek-reasoner[0]', 'lstm[0]'] → hit on 2026-03-11
- 2026-03-13 tail `56` labels=['lstm[1]'] → hit on 2026-03-13
- 2026-03-13 tail `64` labels=['combo-super[2]'] → hit on 2026-03-13

### MN->MB / OFFICIAL_BT / cross_next
- 2026-03-17 tail `74` labels=['final_bundles.bach_thu'] → hit on 2026-03-18
- 2026-03-18 tail `93` labels=['final_bundles.bach_thu'] → hit on 2026-03-19
- 2026-03-20 tail `52` labels=['final_bundles.bach_thu'] → hit on 2026-03-21
- 2026-03-25 tail `51` labels=['final_bundles.bach_thu'] → hit on 2026-03-26
- 2026-03-28 tail `67` labels=['final_bundles.bach_thu'] → hit on 2026-03-29

### MN->MB / OFFICIAL_BT / cross_same
- 2026-03-10 tail `95` labels=['final_bundles.bach_thu'] → hit on 2026-03-10
- 2026-03-22 tail `61` labels=['final_bundles.bach_thu'] → hit on 2026-03-22
- 2026-03-25 tail `51` labels=['final_bundles.bach_thu'] → hit on 2026-03-25
- 2026-03-30 tail `27` labels=['final_bundles.bach_thu'] → hit on 2026-03-30
- 2026-04-01 tail `21` labels=['final_bundles.bach_thu'] → hit on 2026-04-01

### MN->MB / OFFICIAL_LO2 / cross_next
- 2026-03-17 tail `74` labels=['final_bundles.lo2'] → hit on 2026-03-18
- 2026-03-18 tail `93` labels=['final_bundles.lo2'] → hit on 2026-03-19
- 2026-03-20 tail `52` labels=['final_bundles.lo2'] → hit on 2026-03-21
- 2026-03-25 tail `51` labels=['final_bundles.lo2'] → hit on 2026-03-26
- 2026-03-28 tail `67` labels=['final_bundles.lo2'] → hit on 2026-03-29

### MN->MB / OFFICIAL_LO2 / cross_same
- 2026-03-10 tail `95` labels=['final_bundles.lo2'] → hit on 2026-03-10
- 2026-03-11 tail `28` labels=['final_bundles.lo2'] → hit on 2026-03-11
- 2026-03-17 tail `52` labels=['final_bundles.lo2'] → hit on 2026-03-17
- 2026-03-20 tail `93` labels=['final_bundles.lo2'] → hit on 2026-03-20
- 2026-03-22 tail `61` labels=['final_bundles.lo2'] → hit on 2026-03-22

### MN->MB / TEST_BT / cross_next
- 2026-04-08 tail `37` labels=['MN_AI_CHAIN_PRESERVATION_V1', 'MN_NO_TOKEN_HERD_REDUCTION_V1', 'MN_OFFICIAL_BASELINE_CONTROL', 'MN_SPECIALIST_ROSTER_V1', 'MN_STRENGTH_WEIGHTED_V52_5_2'] → hit on 2026-04-09
- 2026-04-18 tail `59` labels=['MN_SPECIALIST_ROSTER_V1'] → hit on 2026-04-19
- 2026-05-05 tail `15` labels=['MN_NO_TOKEN_HERD_REDUCTION_V1', 'MN_OFFICIAL_BASELINE_CONTROL', 'MN_SPECIALIST_ROSTER_V1', 'MN_STRENGTH_WEIGHTED_V52_5_2'] → hit on 2026-05-06
- 2026-05-07 tail `94` labels=['MN_ADAPTIVE_BUDGET_SELECTOR_V1', 'MN_AI_CHAIN_PRESERVATION_V1', 'MN_NO_TOKEN_HERD_REDUCTION_V1', 'MN_OFFICIAL_BASELINE_CONTROL', 'MN_SPECIALIST_ROSTER_V1'] → hit on 2026-05-08
- 2026-05-08 tail `13` labels=['MN_ADAPTIVE_BUDGET_SELECTOR_V1', 'MN_AI_CHAIN_PRESERVATION_V1', 'MN_NO_TOKEN_HERD_REDUCTION_V1', 'MN_OFFICIAL_BASELINE_CONTROL', 'MN_SPECIALIST_ROSTER_V1'] → hit on 2026-05-09

### MN->MB / TEST_BT / cross_same
- 2026-04-04 tail `83` labels=['MN_SPECIALIST_ROSTER_V1'] → hit on 2026-04-04
- 2026-04-09 tail `32` labels=['MN_NO_TOKEN_HERD_REDUCTION_V1', 'MN_OFFICIAL_BASELINE_CONTROL', 'MN_SPECIALIST_ROSTER_V1', 'MN_STRENGTH_WEIGHTED_V52_5_2'] → hit on 2026-04-09
- 2026-04-18 tail `59` labels=['MN_SPECIALIST_ROSTER_V1'] → hit on 2026-04-18
- 2026-05-01 tail `51` labels=['MN_NO_TOKEN_HERD_REDUCTION_V1', 'MN_OFFICIAL_BASELINE_CONTROL', 'MN_SPECIALIST_ROSTER_V1', 'MN_STRENGTH_WEIGHTED_V52_5_2'] → hit on 2026-05-01
- 2026-05-06 tail `95` labels=['MN_ADAPTIVE_BUDGET_SELECTOR_V1', 'MN_AI_CHAIN_PRESERVATION_V1', 'MN_NO_TOKEN_HERD_REDUCTION_V1', 'MN_OFFICIAL_BASELINE_CONTROL', 'MN_SPECIALIST_ROSTER_V1'] → hit on 2026-05-06

### MN->MB / TEST_LO2 / cross_next
- 2026-04-07 tail `65` labels=['MN_AI_CHAIN_PRESERVATION_V1', 'MN_NO_TOKEN_HERD_REDUCTION_V1', 'MN_OFFICIAL_BASELINE_CONTROL', 'MN_PRIOR_REGION_CONTEXT_SAFE_V1', 'MN_SPECIALIST_ROSTER_V1'] → hit on 2026-04-08
- 2026-04-08 tail `37` labels=['MN_AI_CHAIN_PRESERVATION_V1', 'MN_NO_TOKEN_HERD_REDUCTION_V1', 'MN_OFFICIAL_BASELINE_CONTROL', 'MN_PRIOR_REGION_CONTEXT_SAFE_V1', 'MN_SPECIALIST_ROSTER_V1'] → hit on 2026-04-09
- 2026-04-11 tail `42` labels=['MN_AI_CHAIN_PRESERVATION_V1', 'MN_NO_TOKEN_HERD_REDUCTION_V1', 'MN_OFFICIAL_BASELINE_CONTROL', 'MN_PRIOR_REGION_CONTEXT_SAFE_V1', 'MN_SPECIALIST_ROSTER_V1'] → hit on 2026-04-12
- 2026-04-18 tail `59` labels=['MN_SPECIALIST_ROSTER_V1'] → hit on 2026-04-19
- 2026-04-22 tail `22` labels=['MN_AI_CHAIN_PRESERVATION_V1', 'MN_NO_TOKEN_HERD_REDUCTION_V1', 'MN_OFFICIAL_BASELINE_CONTROL', 'MN_PRIOR_REGION_CONTEXT_SAFE_V1', 'MN_SPECIALIST_ROSTER_V1'] → hit on 2026-04-23

### MN->MB / TEST_LO2 / cross_same
- 2026-04-04 tail `83` labels=['MN_AI_CHAIN_PRESERVATION_V1', 'MN_NO_TOKEN_HERD_REDUCTION_V1', 'MN_OFFICIAL_BASELINE_CONTROL', 'MN_PRIOR_REGION_CONTEXT_SAFE_V1', 'MN_SPECIALIST_ROSTER_V1'] → hit on 2026-04-04
- 2026-04-09 tail `32` labels=['MN_AI_CHAIN_PRESERVATION_V1', 'MN_NO_TOKEN_HERD_REDUCTION_V1', 'MN_OFFICIAL_BASELINE_CONTROL', 'MN_PRIOR_REGION_CONTEXT_SAFE_V1', 'MN_SPECIALIST_ROSTER_V1'] → hit on 2026-04-09
- 2026-04-18 tail `59` labels=['MN_SPECIALIST_ROSTER_V1'] → hit on 2026-04-18
- 2026-04-26 tail `91` labels=['MN_AI_CHAIN_PRESERVATION_V1', 'MN_NO_TOKEN_HERD_REDUCTION_V1', 'MN_OFFICIAL_BASELINE_CONTROL', 'MN_PRIOR_REGION_CONTEXT_SAFE_V1', 'MN_SPECIALIST_ROSTER_V1'] → hit on 2026-04-26
- 2026-05-01 tail `51` labels=['MN_AI_CHAIN_PRESERVATION_V1', 'MN_NO_TOKEN_HERD_REDUCTION_V1', 'MN_OFFICIAL_BASELINE_CONTROL', 'MN_PRIOR_REGION_CONTEXT_SAFE_V1', 'MN_SPECIALIST_ROSTER_V1'] → hit on 2026-05-01

### MN->MB / V101_MN_D1_D2 / cross_next
- 2026-04-26 tail `71` labels=['rank=3,score=8.36'] → hit on 2026-04-27
- 2026-04-28 tail `84` labels=['rank=1,score=8.01'] → hit on 2026-04-29
- 2026-04-30 tail `48` labels=['rank=5,score=6.71'] → hit on 2026-05-01
- 2026-05-01 tail `97` labels=['rank=4,score=7.15'] → hit on 2026-05-02
- 2026-05-01 tail `46` labels=['rank=5,score=6.95'] → hit on 2026-05-02

### MN->MB / V101_MN_D1_D2 / cross_same
- 2026-04-26 tail `71` labels=['rank=3,score=8.36'] → hit on 2026-04-26
- 2026-04-26 tail `91` labels=['rank=9,score=6.24'] → hit on 2026-04-26
- 2026-04-27 tail `81` labels=['rank=2,score=8.36'] → hit on 2026-04-27
- 2026-04-28 tail `84` labels=['rank=1,score=8.01'] → hit on 2026-04-28
- 2026-04-28 tail `30` labels=['rank=2,score=8.01'] → hit on 2026-04-28

### MN->MB / V67 / cross_same
- 2026-05-08 tail `94` labels=['adaptive_exploit_v67_candidate_trace:score=3.6098'] → hit on 2026-05-08

### MN->MB / V70 / cross_next
- 2026-05-05 tail `15` labels=['consensus_v1_trace:agreement_count=3'] → hit on 2026-05-06
- 2026-05-07 tail `94` labels=['consensus_v1_trace:agreement_count=5'] → hit on 2026-05-08
- 2026-05-08 tail `13` labels=['consensus_v1_trace:agreement_count=5'] → hit on 2026-05-09

### MN->MB / V70 / cross_same
- 2026-05-06 tail `95` labels=['consensus_v1_trace:agreement_count=6'] → hit on 2026-05-06
- 2026-05-07 tail `94` labels=['consensus_v1_trace:agreement_count=5'] → hit on 2026-05-07
- 2026-05-08 tail `13` labels=['consensus_v1_trace:agreement_count=5'] → hit on 2026-05-08
- 2026-05-08 tail `94` labels=['consensus_v1_trace:agreement_count=2'] → hit on 2026-05-08

### MN->MB / V73 / cross_next
- 2026-05-05 tail `15` labels=['hybrid_v1_trace:confidence_tier=HIGH'] → hit on 2026-05-06

### MN->MB / V73 / cross_same
- 2026-05-06 tail `95` labels=['hybrid_v1_trace:confidence_tier=HIGH'] → hit on 2026-05-06
- 2026-05-08 tail `94` labels=['hybrid_v1_trace:confidence_tier=AURA'] → hit on 2026-05-08

### MN->MT / MODEL::arcee-trinity / cross_next
- 2026-04-17 tail `09` labels=['1'] → hit on 2026-04-18
- 2026-04-19 tail `46` labels=['1'] → hit on 2026-04-20
- 2026-04-20 tail `45` labels=['1'] → hit on 2026-04-21

### MN->MT / MODEL::arcee-trinity / cross_same
- 2026-04-17 tail `09` labels=['1'] → hit on 2026-04-17
- 2026-04-20 tail `45` labels=['1'] → hit on 2026-04-20

### MN->MT / MODEL::claude-opus-4-20250514 / cross_next
- 2026-03-10 tail `67` labels=['0'] → hit on 2026-03-11
- 2026-03-11 tail `28` labels=['1'] → hit on 2026-03-12
- 2026-03-13 tail `45` labels=['0'] → hit on 2026-03-14
- 2026-03-13 tail `05` labels=['1'] → hit on 2026-03-14
- 2026-03-14 tail `95` labels=['1'] → hit on 2026-03-15

### MN->MT / MODEL::claude-opus-4-20250514 / cross_same
- 2026-03-11 tail `28` labels=['1'] → hit on 2026-03-11
- 2026-03-13 tail `05` labels=['1'] → hit on 2026-03-13
- 2026-03-15 tail `71` labels=['0'] → hit on 2026-03-15
- 2026-03-18 tail `93` labels=['0'] → hit on 2026-03-18
- 2026-03-20 tail `22` labels=['0'] → hit on 2026-03-20

### MN->MT / MODEL::claude-sonnet-4-6 / cross_next
- 2026-03-10 tail `67` labels=['1'] → hit on 2026-03-11
- 2026-03-13 tail `45` labels=['0'] → hit on 2026-03-14
- 2026-03-13 tail `05` labels=['1'] → hit on 2026-03-14
- 2026-03-14 tail `95` labels=['0'] → hit on 2026-03-15
- 2026-03-15 tail `48` labels=['1'] → hit on 2026-03-16

### MN->MT / MODEL::claude-sonnet-4-6 / cross_same
- 2026-03-10 tail `35` labels=['0'] → hit on 2026-03-10
- 2026-03-12 tail `23` labels=['0'] → hit on 2026-03-12
- 2026-03-13 tail `05` labels=['1'] → hit on 2026-03-13
- 2026-03-15 tail `71` labels=['0'] → hit on 2026-03-15
- 2026-03-20 tail `22` labels=['1'] → hit on 2026-03-20

### MN->MT / MODEL::combo-no-token / cross_next
- 2026-03-11 tail `78` labels=['0'] → hit on 2026-03-12
- 2026-03-12 tail `94` labels=['1'] → hit on 2026-03-13
- 2026-03-13 tail `44` labels=['1'] → hit on 2026-03-14
- 2026-03-14 tail `95` labels=['0'] → hit on 2026-03-15
- 2026-03-15 tail `48` labels=['1'] → hit on 2026-03-16

### MN->MT / MODEL::combo-no-token / cross_same
- 2026-03-13 tail `44` labels=['1'] → hit on 2026-03-13
- 2026-03-18 tail `90` labels=['1'] → hit on 2026-03-18
- 2026-03-19 tail `75` labels=['1'] → hit on 2026-03-19
- 2026-03-26 tail `94` labels=['1'] → hit on 2026-03-26
- 2026-03-31 tail `01` labels=['0'] → hit on 2026-03-31

### MN->MT / MODEL::combo-super / cross_next
- 2026-03-10 tail `67` labels=['1'] → hit on 2026-03-11
- 2026-03-11 tail `28` labels=['0'] → hit on 2026-03-12
- 2026-03-13 tail `05` labels=['0'] → hit on 2026-03-14
- 2026-03-13 tail `45` labels=['1'] → hit on 2026-03-14
- 2026-03-13 tail `64` labels=['2'] → hit on 2026-03-14

### MN->MT / MODEL::combo-super / cross_same
- 2026-03-10 tail `35` labels=['0'] → hit on 2026-03-10
- 2026-03-11 tail `28` labels=['0'] → hit on 2026-03-11
- 2026-03-12 tail `23` labels=['0'] → hit on 2026-03-12
- 2026-03-13 tail `05` labels=['0'] → hit on 2026-03-13
- 2026-03-14 tail `04` labels=['0'] → hit on 2026-03-14

### MN->MT / MODEL::deepseek-chat / cross_next
- 2026-03-11 tail `28` labels=['1'] → hit on 2026-03-12
- 2026-03-13 tail `04` labels=['0'] → hit on 2026-03-14
- 2026-03-13 tail `46` labels=['1'] → hit on 2026-03-14
- 2026-03-15 tail `48` labels=['1'] → hit on 2026-03-16
- 2026-03-17 tail `74` labels=['1'] → hit on 2026-03-18

### MN->MT / MODEL::deepseek-chat / cross_same
- 2026-03-11 tail `28` labels=['1'] → hit on 2026-03-11
- 2026-03-12 tail `15` labels=['1'] → hit on 2026-03-12
- 2026-03-13 tail `04` labels=['0'] → hit on 2026-03-13
- 2026-03-15 tail `71` labels=['0'] → hit on 2026-03-15
- 2026-03-18 tail `93` labels=['1'] → hit on 2026-03-18

### MN->MT / MODEL::deepseek-reasoner / cross_next
- 2026-03-10 tail `67` labels=['1'] → hit on 2026-03-11
- 2026-03-11 tail `28` labels=['0'] → hit on 2026-03-12
- 2026-03-13 tail `05` labels=['0'] → hit on 2026-03-14
- 2026-03-13 tail `45` labels=['1'] → hit on 2026-03-14
- 2026-03-15 tail `48` labels=['1'] → hit on 2026-03-16

### MN->MT / MODEL::deepseek-reasoner / cross_same
- 2026-03-11 tail `28` labels=['0'] → hit on 2026-03-11
- 2026-03-13 tail `05` labels=['0'] → hit on 2026-03-13
- 2026-03-20 tail `41` labels=['0'] → hit on 2026-03-20
- 2026-03-21 tail `35` labels=['1'] → hit on 2026-03-21
- 2026-03-28 tail `87` labels=['1'] → hit on 2026-03-28

### MN->MT / MODEL::deepseek-v4-flash / cross_next
- 2026-04-28 tail `64` labels=['0'] → hit on 2026-04-29
- 2026-04-28 tail `86` labels=['1'] → hit on 2026-04-29
- 2026-05-01 tail `74` labels=['0'] → hit on 2026-05-02
- 2026-05-02 tail `37` labels=['0'] → hit on 2026-05-03
- 2026-05-05 tail `41` labels=['1'] → hit on 2026-05-06

### MN->MT / MODEL::deepseek-v4-flash / cross_same
- 2026-04-29 tail `85` labels=['1'] → hit on 2026-04-29
- 2026-05-03 tail `14` labels=['0'] → hit on 2026-05-03

### MN->MT / MODEL::deepseek-v4-pro / cross_next
- 2026-04-28 tail `64` labels=['0'] → hit on 2026-04-29
- 2026-05-04 tail `48` labels=['0'] → hit on 2026-05-05
- 2026-05-06 tail `27` labels=['1'] → hit on 2026-05-07
- 2026-05-08 tail `94` labels=['0'] → hit on 2026-05-09
- 2026-05-08 tail `40` labels=['1'] → hit on 2026-05-09

### MN->MT / MODEL::deepseek-v4-pro / cross_same
- 2026-04-27 tail `64` labels=['1'] → hit on 2026-04-27
- 2026-04-29 tail `85` labels=['0'] → hit on 2026-04-29

### MN->MT / MODEL::gemini-2.5-flash / cross_next
- 2026-03-10 tail `67` labels=['0'] → hit on 2026-03-11
- 2026-03-11 tail `61` labels=['1'] → hit on 2026-03-12
- 2026-03-13 tail `45` labels=['0'] → hit on 2026-03-14
- 2026-03-14 tail `95` labels=['1'] → hit on 2026-03-15
- 2026-03-17 tail `05` labels=['0'] → hit on 2026-03-18

### MN->MT / MODEL::gemini-2.5-flash / cross_same
- 2026-03-10 tail `35` labels=['1'] → hit on 2026-03-10
- 2026-03-15 tail `71` labels=['0'] → hit on 2026-03-15
- 2026-03-18 tail `93` labels=['0'] → hit on 2026-03-18
- 2026-03-20 tail `93` labels=['0'] → hit on 2026-03-20
- 2026-03-20 tail `41` labels=['1'] → hit on 2026-03-20

### MN->MT / MODEL::gemini-2.5-pro / cross_next
- 2026-03-10 tail `67` labels=['0'] → hit on 2026-03-11
- 2026-03-11 tail `61` labels=['1'] → hit on 2026-03-12
- 2026-03-15 tail `48` labels=['0'] → hit on 2026-03-16
- 2026-03-17 tail `74` labels=['0'] → hit on 2026-03-18
- 2026-03-20 tail `93` labels=['0'] → hit on 2026-03-21

### MN->MT / MODEL::gemini-2.5-pro / cross_same
- 2026-03-10 tail `35` labels=['1'] → hit on 2026-03-10
- 2026-03-15 tail `87` labels=['1'] → hit on 2026-03-15
- 2026-03-18 tail `96` labels=['0'] → hit on 2026-03-18
- 2026-03-19 tail `75` labels=['0'] → hit on 2026-03-19
- 2026-03-20 tail `93` labels=['0'] → hit on 2026-03-20

### MN->MT / MODEL::gemini-3-flash / cross_next
- 2026-05-08 tail `94` labels=['0'] → hit on 2026-05-09
- 2026-05-08 tail `02` labels=['1'] → hit on 2026-05-09

### MN->MT / MODEL::gemini-3.1-pro / cross_next
- 2026-05-07 tail `90` labels=['1'] → hit on 2026-05-08
- 2026-05-08 tail `94` labels=['0'] → hit on 2026-05-09

### MN->MT / MODEL::gemini-3.1-pro / cross_same
- 2026-05-07 tail `69` labels=['0'] → hit on 2026-05-07
- 2026-05-07 tail `90` labels=['1'] → hit on 2026-05-07

### MN->MT / MODEL::gemma-4-31b / cross_next
- 2026-05-06 tail `27` labels=['1'] → hit on 2026-05-07

### MN->MT / MODEL::glm-5.1 / cross_next
- 2026-04-12 tail `85` labels=['0'] → hit on 2026-04-13
- 2026-04-19 tail `86` labels=['1'] → hit on 2026-04-20
- 2026-04-21 tail `73` labels=['1'] → hit on 2026-04-22
- 2026-04-25 tail `32` labels=['0'] → hit on 2026-04-26
- 2026-04-26 tail `71` labels=['0'] → hit on 2026-04-27

### MN->MT / MODEL::glm-5.1 / cross_same
- 2026-04-13 tail `00` labels=['0'] → hit on 2026-04-13
- 2026-04-14 tail `04` labels=['0'] → hit on 2026-04-14
- 2026-04-15 tail `14` labels=['1'] → hit on 2026-04-15
- 2026-04-16 tail `03` labels=['1'] → hit on 2026-04-16
- 2026-04-21 tail `73` labels=['1'] → hit on 2026-04-21

### MN->MT / MODEL::gpt-5-mini / cross_next
- 2026-03-15 tail `48` labels=['0'] → hit on 2026-03-16
- 2026-03-17 tail `74` labels=['1'] → hit on 2026-03-18
- 2026-03-22 tail `61` labels=['0'] → hit on 2026-03-23
- 2026-03-22 tail `32` labels=['1'] → hit on 2026-03-23
- 2026-03-25 tail `51` labels=['0'] → hit on 2026-03-26

### MN->MT / MODEL::gpt-5-mini / cross_same
- 2026-03-15 tail `71` labels=['1'] → hit on 2026-03-15
- 2026-03-18 tail `93` labels=['1'] → hit on 2026-03-18
- 2026-03-20 tail `56` labels=['0'] → hit on 2026-03-20
- 2026-03-22 tail `61` labels=['0'] → hit on 2026-03-22
- 2026-03-28 tail `87` labels=['1'] → hit on 2026-03-28

### MN->MT / MODEL::gpt-5.4 / cross_next
- 2026-03-25 tail `51` labels=['0'] → hit on 2026-03-26
- 2026-03-27 tail `82` labels=['0'] → hit on 2026-03-28
- 2026-03-28 tail `67` labels=['1'] → hit on 2026-03-29
- 2026-04-01 tail `21` labels=['0'] → hit on 2026-04-02
- 2026-04-02 tail `61` labels=['0'] → hit on 2026-04-03

### MN->MT / MODEL::gpt-5.4 / cross_same
- 2026-03-27 tail `93` labels=['1'] → hit on 2026-03-27
- 2026-03-30 tail `27` labels=['1'] → hit on 2026-03-30
- 2026-04-01 tail `21` labels=['0'] → hit on 2026-04-01
- 2026-04-01 tail `67` labels=['1'] → hit on 2026-04-01
- 2026-04-02 tail `61` labels=['0'] → hit on 2026-04-02

### MN->MT / MODEL::gpt-5.5 / cross_next
- 2026-04-28 tail `64` labels=['0'] → hit on 2026-04-29
- 2026-05-01 tail `74` labels=['0'] → hit on 2026-05-02
- 2026-05-01 tail `51` labels=['1'] → hit on 2026-05-02
- 2026-05-07 tail `90` labels=['0'] → hit on 2026-05-08
- 2026-05-08 tail `19` labels=['1'] → hit on 2026-05-09

### MN->MT / MODEL::gpt-5.5 / cross_same
- 2026-04-27 tail `28` labels=['1'] → hit on 2026-04-27
- 2026-04-29 tail `85` labels=['0'] → hit on 2026-04-29
- 2026-05-07 tail `90` labels=['0'] → hit on 2026-05-07
- 2026-05-08 tail `19` labels=['1'] → hit on 2026-05-08

### MN->MT / MODEL::gpt-oss-120b / cross_next
- 2026-04-20 tail `45` labels=['0'] → hit on 2026-04-21
- 2026-04-25 tail `32` labels=['1'] → hit on 2026-04-26
- 2026-04-28 tail `64` labels=['0'] → hit on 2026-04-29
- 2026-05-01 tail `51` labels=['1'] → hit on 2026-05-02
- 2026-05-05 tail `41` labels=['1'] → hit on 2026-05-06

### MN->MT / MODEL::gpt-oss-120b / cross_same
- 2026-04-19 tail `40` labels=['1'] → hit on 2026-04-19
- 2026-04-20 tail `45` labels=['0'] → hit on 2026-04-20
- 2026-04-24 tail `25` labels=['0'] → hit on 2026-04-24
- 2026-05-06 tail `21` labels=['0'] → hit on 2026-05-06
- 2026-05-07 tail `90` labels=['0'] → hit on 2026-05-07

### MN->MT / MODEL::grok-4.20-multi-agent / cross_next
- 2026-04-13 tail `91` labels=['1'] → hit on 2026-04-14
- 2026-04-15 tail `33` labels=['1'] → hit on 2026-04-16
- 2026-04-17 tail `47` labels=['1'] → hit on 2026-04-18
- 2026-04-18 tail `06` labels=['0'] → hit on 2026-04-19
- 2026-04-20 tail `73` labels=['0'] → hit on 2026-04-21

### MN->MT / MODEL::grok-4.20-multi-agent / cross_same
- 2026-04-13 tail `00` labels=['0'] → hit on 2026-04-13
- 2026-04-18 tail `06` labels=['0'] → hit on 2026-04-18
- 2026-04-20 tail `73` labels=['0'] → hit on 2026-04-20
- 2026-04-24 tail `25` labels=['1'] → hit on 2026-04-24
- 2026-04-26 tail `57` labels=['0'] → hit on 2026-04-26

### MN->MT / MODEL::kimi-k2.5 / cross_next
- 2026-04-17 tail `47` labels=['1'] → hit on 2026-04-18
- 2026-04-19 tail `86` labels=['1'] → hit on 2026-04-20
- 2026-04-20 tail `73` labels=['1'] → hit on 2026-04-21
- 2026-04-23 tail `38` labels=['1'] → hit on 2026-04-24
- 2026-04-26 tail `71` labels=['0'] → hit on 2026-04-27

### MN->MT / MODEL::kimi-k2.5 / cross_same
- 2026-04-16 tail `30` labels=['0'] → hit on 2026-04-16
- 2026-04-16 tail `56` labels=['1'] → hit on 2026-04-16
- 2026-04-20 tail `73` labels=['1'] → hit on 2026-04-20
- 2026-04-24 tail `25` labels=['0'] → hit on 2026-04-24
- 2026-04-24 tail `52` labels=['1'] → hit on 2026-04-24

### MN->MT / MODEL::kimi-k2.6 / cross_next
- 2026-04-23 tail `46` labels=['1'] → hit on 2026-04-24
- 2026-04-25 tail `32` labels=['1'] → hit on 2026-04-26
- 2026-04-26 tail `71` labels=['0'] → hit on 2026-04-27

### MN->MT / MODEL::kimi-k2.6 / cross_same
- 2026-04-26 tail `71` labels=['0'] → hit on 2026-04-26

### MN->MT / MODEL::llama-4-maverick / cross_next
- 2026-04-19 tail `59` labels=['1'] → hit on 2026-04-20
- 2026-04-20 tail `45` labels=['1'] → hit on 2026-04-21
- 2026-04-21 tail `54` labels=['1'] → hit on 2026-04-22
- 2026-04-22 tail `22` labels=['0'] → hit on 2026-04-23

### MN->MT / MODEL::llama-4-maverick / cross_same
- 2026-04-19 tail `59` labels=['1'] → hit on 2026-04-19
- 2026-04-20 tail `45` labels=['1'] → hit on 2026-04-20

### MN->MT / MODEL::lstm / cross_next
- 2026-03-11 tail `28` labels=['0'] → hit on 2026-03-12
- 2026-03-12 tail `28` labels=['1'] → hit on 2026-03-13
- 2026-03-14 tail `56` labels=['1'] → hit on 2026-03-15
- 2026-03-17 tail `90` labels=['0'] → hit on 2026-03-18
- 2026-03-21 tail `81` labels=['1'] → hit on 2026-03-22

### MN->MT / MODEL::lstm / cross_same
- 2026-03-11 tail `28` labels=['0'] → hit on 2026-03-11
- 2026-03-12 tail `28` labels=['1'] → hit on 2026-03-12
- 2026-03-18 tail `90` labels=['0'] → hit on 2026-03-18
- 2026-03-22 tail `33` labels=['0'] → hit on 2026-03-22
- 2026-03-22 tail `80` labels=['1'] → hit on 2026-03-22

### MN->MT / MODEL::meta-learning / cross_next
- 2026-03-11 tail `78` labels=['1'] → hit on 2026-03-12
- 2026-03-12 tail `77` labels=['0'] → hit on 2026-03-13
- 2026-03-13 tail `44` labels=['1'] → hit on 2026-03-14
- 2026-03-14 tail `95` labels=['0'] → hit on 2026-03-15
- 2026-03-14 tail `09` labels=['1'] → hit on 2026-03-15

### MN->MT / MODEL::meta-learning / cross_same
- 2026-03-13 tail `44` labels=['1'] → hit on 2026-03-13
- 2026-03-15 tail `01` labels=['0'] → hit on 2026-03-15
- 2026-03-16 tail `88` labels=['0'] → hit on 2026-03-16
- 2026-03-26 tail `94` labels=['0'] → hit on 2026-03-26
- 2026-03-27 tail `16` labels=['1'] → hit on 2026-03-27

### MN->MT / MODEL::minimax-m2.7 / cross_next
- 2026-04-17 tail `47` labels=['1'] → hit on 2026-04-18
- 2026-04-18 tail `06` labels=['0'] → hit on 2026-04-19
- 2026-04-19 tail `46` labels=['0'] → hit on 2026-04-20
- 2026-04-19 tail `86` labels=['1'] → hit on 2026-04-20
- 2026-04-25 tail `32` labels=['0'] → hit on 2026-04-26

### MN->MT / MODEL::minimax-m2.7 / cross_same
- 2026-04-16 tail `26` labels=['1'] → hit on 2026-04-16
- 2026-04-18 tail `06` labels=['0'] → hit on 2026-04-18
- 2026-04-24 tail `25` labels=['1'] → hit on 2026-04-24
- 2026-04-27 tail `28` labels=['1'] → hit on 2026-04-27

### MN->MT / MODEL::mistral-large-3 / cross_next
- 2026-04-20 tail `45` labels=['0'] → hit on 2026-04-21
- 2026-04-21 tail `54` labels=['0'] → hit on 2026-04-22
- 2026-04-22 tail `22` labels=['0'] → hit on 2026-04-23

### MN->MT / MODEL::mistral-large-3 / cross_same
- 2026-04-20 tail `45` labels=['0'] → hit on 2026-04-20

### MN->MT / MODEL::mistral-nemo / cross_next
- 2026-04-19 tail `46` labels=['1'] → hit on 2026-04-20
- 2026-04-22 tail `34` labels=['0'] → hit on 2026-04-23
- 2026-04-22 tail `17` labels=['1'] → hit on 2026-04-23

### MN->MT / MODEL::mistral-nemo / cross_same
- 2026-04-22 tail `34` labels=['0'] → hit on 2026-04-22

### MN->MT / MODEL::nemotron-3-super / cross_same
- 2026-04-16 tail `30` labels=['1'] → hit on 2026-04-16

### MN->MT / MODEL::qwen3-coder / cross_next
- 2026-04-13 tail `91` labels=['1'] → hit on 2026-04-14
- 2026-04-17 tail `09` labels=['0'] → hit on 2026-04-18
- 2026-04-18 tail `06` labels=['0'] → hit on 2026-04-19
- 2026-04-19 tail `92` labels=['1'] → hit on 2026-04-20
- 2026-04-20 tail `45` labels=['1'] → hit on 2026-04-21

### MN->MT / MODEL::qwen3-coder / cross_same
- 2026-04-13 tail `00` labels=['0'] → hit on 2026-04-13
- 2026-04-16 tail `56` labels=['1'] → hit on 2026-04-16
- 2026-04-17 tail `09` labels=['0'] → hit on 2026-04-17
- 2026-04-18 tail `06` labels=['0'] → hit on 2026-04-18
- 2026-04-19 tail `92` labels=['1'] → hit on 2026-04-19

### MN->MT / MODEL::qwen3-max-thinking / cross_next
- 2026-04-18 tail `06` labels=['0'] → hit on 2026-04-19
- 2026-04-20 tail `73` labels=['1'] → hit on 2026-04-21
- 2026-04-23 tail `46` labels=['1'] → hit on 2026-04-24
- 2026-04-25 tail `32` labels=['0'] → hit on 2026-04-26
- 2026-04-26 tail `71` labels=['0'] → hit on 2026-04-27

### MN->MT / MODEL::qwen3-max-thinking / cross_same
- 2026-04-18 tail `06` labels=['0'] → hit on 2026-04-18
- 2026-04-20 tail `73` labels=['1'] → hit on 2026-04-20
- 2026-04-24 tail `25` labels=['0'] → hit on 2026-04-24
- 2026-04-26 tail `71` labels=['0'] → hit on 2026-04-26
- 2026-05-01 tail `29` labels=['0'] → hit on 2026-05-01

### MN->MT / MODEL::qwen3.6-plus / cross_next
- 2026-04-14 tail `02` labels=['0'] → hit on 2026-04-15
- 2026-04-15 tail `30` labels=['1'] → hit on 2026-04-16
- 2026-04-28 tail `64` labels=['0'] → hit on 2026-04-29
- 2026-04-30 tail `75` labels=['1'] → hit on 2026-05-01
- 2026-05-04 tail `48` labels=['0'] → hit on 2026-05-05

### MN->MT / MODEL::qwen3.6-plus / cross_same
- 2026-04-13 tail `00` labels=['0'] → hit on 2026-04-13
- 2026-04-14 tail `64` labels=['1'] → hit on 2026-04-14
- 2026-04-30 tail `75` labels=['1'] → hit on 2026-04-30

### MN->MT / MODEL::random-forest / cross_next
- 2026-03-12 tail `94` labels=['0'] → hit on 2026-03-13
- 2026-03-13 tail `44` labels=['1'] → hit on 2026-03-14
- 2026-03-14 tail `09` labels=['1'] → hit on 2026-03-15
- 2026-03-15 tail `48` labels=['1'] → hit on 2026-03-16
- 2026-03-18 tail `54` labels=['0'] → hit on 2026-03-19

### MN->MT / MODEL::random-forest / cross_same
- 2026-03-11 tail `85` labels=['1'] → hit on 2026-03-11
- 2026-03-13 tail `44` labels=['1'] → hit on 2026-03-13
- 2026-03-18 tail `54` labels=['0'] → hit on 2026-03-18
- 2026-03-19 tail `20` labels=['0'] → hit on 2026-03-19
- 2026-03-27 tail `33` labels=['0'] → hit on 2026-03-27

### MN->MT / MODEL::smart-ensemble / cross_next
- 2026-03-11 tail `28` labels=['1'] → hit on 2026-03-12
- 2026-03-14 tail `95` labels=['1'] → hit on 2026-03-15
- 2026-03-15 tail `48` labels=['1'] → hit on 2026-03-16
- 2026-03-16 tail `88` labels=['1'] → hit on 2026-03-17
- 2026-03-17 tail `46` labels=['0'] → hit on 2026-03-18

### MN->MT / MODEL::smart-ensemble / cross_same
- 2026-03-11 tail `28` labels=['1'] → hit on 2026-03-11
- 2026-03-16 tail `88` labels=['1'] → hit on 2026-03-16
- 2026-03-18 tail `90` labels=['1'] → hit on 2026-03-18
- 2026-03-20 tail `22` labels=['1'] → hit on 2026-03-20
- 2026-03-21 tail `55` labels=['0'] → hit on 2026-03-21

### MN->MT / MODEL::smart-ml / cross_next
- 2026-03-10 tail `85` labels=['0'] → hit on 2026-03-11
- 2026-03-11 tail `78` labels=['1'] → hit on 2026-03-12
- 2026-03-12 tail `94` labels=['1'] → hit on 2026-03-13
- 2026-03-14 tail `09` labels=['1'] → hit on 2026-03-15
- 2026-03-15 tail `48` labels=['0'] → hit on 2026-03-16

### MN->MT / MODEL::smart-ml / cross_same
- 2026-03-11 tail `85` labels=['0'] → hit on 2026-03-11
- 2026-03-13 tail `97` labels=['1'] → hit on 2026-03-13
- 2026-03-19 tail `75` labels=['1'] → hit on 2026-03-19
- 2026-03-27 tail `33` labels=['0'] → hit on 2026-03-27
- 2026-03-31 tail `01` labels=['1'] → hit on 2026-03-31

### MN->MT / MODEL::xgboost / cross_next
- 2026-03-10 tail `85` labels=['1'] → hit on 2026-03-11
- 2026-03-11 tail `78` labels=['0'] → hit on 2026-03-12
- 2026-03-14 tail `95` labels=['0'] → hit on 2026-03-15
- 2026-03-14 tail `09` labels=['1'] → hit on 2026-03-15
- 2026-03-18 tail `75` labels=['0'] → hit on 2026-03-19

### MN->MT / MODEL::xgboost / cross_same
- 2026-03-12 tail `55` labels=['1'] → hit on 2026-03-12
- 2026-03-13 tail `97` labels=['0'] → hit on 2026-03-13
- 2026-03-15 tail `26` labels=['0'] → hit on 2026-03-15
- 2026-03-26 tail `94` labels=['0'] → hit on 2026-03-26
- 2026-03-27 tail `33` labels=['0'] → hit on 2026-03-27

### MN->MT / MODEL_MAIN / cross_next
- 2026-03-10 tail `85` labels=['smart-ml[0]', 'xgboost[1]'] → hit on 2026-03-11
- 2026-03-10 tail `67` labels=['claude-opus-4-20250514[0]', 'claude-sonnet-4-6[1]', 'combo-super[1]', 'deepseek-reasoner[1]', 'gemini-2.5-flash[0]'] → hit on 2026-03-11
- 2026-03-11 tail `28` labels=['claude-opus-4-20250514[1]', 'combo-super[0]', 'deepseek-chat[1]', 'deepseek-reasoner[0]', 'lstm[0]'] → hit on 2026-03-12
- 2026-03-11 tail `78` labels=['combo-no-token[0]', 'meta-learning[1]', 'smart-ml[1]', 'xgboost[0]'] → hit on 2026-03-12
- 2026-03-11 tail `61` labels=['gemini-2.5-flash[1]', 'gemini-2.5-pro[1]'] → hit on 2026-03-12

### MN->MT / MODEL_MAIN / cross_same
- 2026-03-10 tail `35` labels=['claude-sonnet-4-6[0]', 'combo-super[0]', 'gemini-2.5-flash[1]', 'gemini-2.5-pro[1]'] → hit on 2026-03-10
- 2026-03-11 tail `28` labels=['claude-opus-4-20250514[1]', 'combo-super[0]', 'deepseek-chat[1]', 'deepseek-reasoner[0]', 'lstm[0]'] → hit on 2026-03-11
- 2026-03-11 tail `85` labels=['random-forest[1]', 'smart-ml[0]'] → hit on 2026-03-11
- 2026-03-12 tail `55` labels=['xgboost[1]'] → hit on 2026-03-12
- 2026-03-12 tail `28` labels=['lstm[1]'] → hit on 2026-03-12

### MN->MT / OFFICIAL_BT / cross_next
- 2026-03-11 tail `78` labels=['final_bundles.bach_thu'] → hit on 2026-03-12
- 2026-03-14 tail `95` labels=['final_bundles.bach_thu'] → hit on 2026-03-15
- 2026-03-15 tail `48` labels=['final_bundles.bach_thu'] → hit on 2026-03-16
- 2026-03-17 tail `74` labels=['final_bundles.bach_thu'] → hit on 2026-03-18
- 2026-03-22 tail `61` labels=['final_bundles.bach_thu'] → hit on 2026-03-23

### MN->MT / OFFICIAL_BT / cross_same
- 2026-03-18 tail `93` labels=['final_bundles.bach_thu'] → hit on 2026-03-18
- 2026-03-22 tail `61` labels=['final_bundles.bach_thu'] → hit on 2026-03-22
- 2026-03-30 tail `27` labels=['final_bundles.bach_thu'] → hit on 2026-03-30
- 2026-04-01 tail `21` labels=['final_bundles.bach_thu'] → hit on 2026-04-01
- 2026-04-02 tail `61` labels=['final_bundles.bach_thu'] → hit on 2026-04-02

### MN->MT / OFFICIAL_LO2 / cross_next
- 2026-03-10 tail `67` labels=['final_bundles.lo2'] → hit on 2026-03-11
- 2026-03-11 tail `78` labels=['final_bundles.lo2'] → hit on 2026-03-12
- 2026-03-11 tail `28` labels=['final_bundles.lo2'] → hit on 2026-03-12
- 2026-03-13 tail `45` labels=['final_bundles.lo2'] → hit on 2026-03-14
- 2026-03-14 tail `95` labels=['final_bundles.lo2'] → hit on 2026-03-15

### MN->MT / OFFICIAL_LO2 / cross_same
- 2026-03-11 tail `28` labels=['final_bundles.lo2'] → hit on 2026-03-11
- 2026-03-15 tail `71` labels=['final_bundles.lo2'] → hit on 2026-03-15
- 2026-03-18 tail `93` labels=['final_bundles.lo2'] → hit on 2026-03-18
- 2026-03-20 tail `93` labels=['final_bundles.lo2'] → hit on 2026-03-20
- 2026-03-22 tail `61` labels=['final_bundles.lo2'] → hit on 2026-03-22

### MN->MT / TEST_BT / cross_next
- 2026-04-04 tail `53` labels=['MN_AI_CHAIN_PRESERVATION_V1', 'MN_NO_TOKEN_HERD_REDUCTION_V1', 'MN_OFFICIAL_BASELINE_CONTROL', 'MN_STRENGTH_WEIGHTED_V52_5_2'] → hit on 2026-04-05
- 2026-04-08 tail `37` labels=['MN_AI_CHAIN_PRESERVATION_V1', 'MN_NO_TOKEN_HERD_REDUCTION_V1', 'MN_OFFICIAL_BASELINE_CONTROL', 'MN_SPECIALIST_ROSTER_V1', 'MN_STRENGTH_WEIGHTED_V52_5_2'] → hit on 2026-04-09
- 2026-04-10 tail `91` labels=['MN_AI_CHAIN_PRESERVATION_V1', 'MN_NO_TOKEN_HERD_REDUCTION_V1', 'MN_OFFICIAL_BASELINE_CONTROL', 'MN_SPECIALIST_ROSTER_V1', 'MN_STRENGTH_WEIGHTED_V52_5_2'] → hit on 2026-04-11
- 2026-04-12 tail `85` labels=['MN_AI_CHAIN_PRESERVATION_V1', 'MN_NO_TOKEN_HERD_REDUCTION_V1', 'MN_OFFICIAL_BASELINE_CONTROL', 'MN_SPECIALIST_ROSTER_V1', 'MN_STRENGTH_WEIGHTED_V52_5_2'] → hit on 2026-04-13
- 2026-04-15 tail `98` labels=['MN_NO_TOKEN_HERD_REDUCTION_V1', 'MN_OFFICIAL_BASELINE_CONTROL', 'MN_SPECIALIST_ROSTER_V1', 'MN_STRENGTH_WEIGHTED_V52_5_2'] → hit on 2026-04-16

### MN->MT / TEST_BT / cross_same
- 2026-04-08 tail `37` labels=['MN_AI_CHAIN_PRESERVATION_V1', 'MN_NO_TOKEN_HERD_REDUCTION_V1', 'MN_OFFICIAL_BASELINE_CONTROL', 'MN_SPECIALIST_ROSTER_V1', 'MN_STRENGTH_WEIGHTED_V52_5_2'] → hit on 2026-04-08
- 2026-04-09 tail `32` labels=['MN_NO_TOKEN_HERD_REDUCTION_V1', 'MN_OFFICIAL_BASELINE_CONTROL', 'MN_SPECIALIST_ROSTER_V1', 'MN_STRENGTH_WEIGHTED_V52_5_2'] → hit on 2026-04-09
- 2026-04-18 tail `06` labels=['MN_NO_TOKEN_HERD_REDUCTION_V1', 'MN_OFFICIAL_BASELINE_CONTROL', 'MN_STRENGTH_WEIGHTED_V52_5_2'] → hit on 2026-04-18
- 2026-04-24 tail `25` labels=['MN_AI_CHAIN_PRESERVATION_V1', 'MN_NO_TOKEN_HERD_REDUCTION_V1', 'MN_OFFICIAL_BASELINE_CONTROL', 'MN_SPECIALIST_ROSTER_V1', 'MN_STRENGTH_WEIGHTED_V52_5_2'] → hit on 2026-04-24
- 2026-04-29 tail `85` labels=['MN_AI_CHAIN_PRESERVATION_V1', 'MN_NO_TOKEN_HERD_REDUCTION_V1', 'MN_OFFICIAL_BASELINE_CONTROL', 'MN_SPECIALIST_ROSTER_V1', 'MN_STRENGTH_WEIGHTED_V52_5_2'] → hit on 2026-04-29

### MN->MT / TEST_LO2 / cross_next
- 2026-04-04 tail `53` labels=['MN_AI_CHAIN_PRESERVATION_V1', 'MN_NO_TOKEN_HERD_REDUCTION_V1', 'MN_OFFICIAL_BASELINE_CONTROL', 'MN_PRIOR_REGION_CONTEXT_SAFE_V1', 'MN_SPECIALIST_ROSTER_V1'] → hit on 2026-04-05
- 2026-04-07 tail `65` labels=['MN_AI_CHAIN_PRESERVATION_V1', 'MN_NO_TOKEN_HERD_REDUCTION_V1', 'MN_OFFICIAL_BASELINE_CONTROL', 'MN_PRIOR_REGION_CONTEXT_SAFE_V1', 'MN_SPECIALIST_ROSTER_V1'] → hit on 2026-04-08
- 2026-04-08 tail `37` labels=['MN_AI_CHAIN_PRESERVATION_V1', 'MN_NO_TOKEN_HERD_REDUCTION_V1', 'MN_OFFICIAL_BASELINE_CONTROL', 'MN_PRIOR_REGION_CONTEXT_SAFE_V1', 'MN_SPECIALIST_ROSTER_V1'] → hit on 2026-04-09
- 2026-04-10 tail `91` labels=['MN_AI_CHAIN_PRESERVATION_V1', 'MN_NO_TOKEN_HERD_REDUCTION_V1', 'MN_OFFICIAL_BASELINE_CONTROL', 'MN_PRIOR_REGION_CONTEXT_SAFE_V1', 'MN_SPECIALIST_ROSTER_V1'] → hit on 2026-04-11
- 2026-04-11 tail `42` labels=['MN_AI_CHAIN_PRESERVATION_V1', 'MN_NO_TOKEN_HERD_REDUCTION_V1', 'MN_OFFICIAL_BASELINE_CONTROL', 'MN_PRIOR_REGION_CONTEXT_SAFE_V1', 'MN_SPECIALIST_ROSTER_V1'] → hit on 2026-04-12

### MN->MT / TEST_LO2 / cross_same
- 2026-04-07 tail `65` labels=['MN_AI_CHAIN_PRESERVATION_V1', 'MN_NO_TOKEN_HERD_REDUCTION_V1', 'MN_OFFICIAL_BASELINE_CONTROL', 'MN_PRIOR_REGION_CONTEXT_SAFE_V1', 'MN_SPECIALIST_ROSTER_V1'] → hit on 2026-04-07
- 2026-04-08 tail `37` labels=['MN_AI_CHAIN_PRESERVATION_V1', 'MN_NO_TOKEN_HERD_REDUCTION_V1', 'MN_OFFICIAL_BASELINE_CONTROL', 'MN_PRIOR_REGION_CONTEXT_SAFE_V1', 'MN_SPECIALIST_ROSTER_V1'] → hit on 2026-04-08
- 2026-04-09 tail `32` labels=['MN_AI_CHAIN_PRESERVATION_V1', 'MN_NO_TOKEN_HERD_REDUCTION_V1', 'MN_OFFICIAL_BASELINE_CONTROL', 'MN_PRIOR_REGION_CONTEXT_SAFE_V1', 'MN_SPECIALIST_ROSTER_V1'] → hit on 2026-04-09
- 2026-04-14 tail `04` labels=['MN_AI_CHAIN_PRESERVATION_V1', 'MN_NO_TOKEN_HERD_REDUCTION_V1', 'MN_OFFICIAL_BASELINE_CONTROL', 'MN_PRIOR_REGION_CONTEXT_SAFE_V1', 'MN_SPECIALIST_ROSTER_V1'] → hit on 2026-04-14
- 2026-04-18 tail `06` labels=['MN_AI_CHAIN_PRESERVATION_V1', 'MN_NO_TOKEN_HERD_REDUCTION_V1', 'MN_OFFICIAL_BASELINE_CONTROL', 'MN_PRIOR_REGION_CONTEXT_SAFE_V1', 'MN_SPECIALIST_ROSTER_V1'] → hit on 2026-04-18

### MN->MT / V101_MN_D1_D2 / cross_next
- 2026-04-26 tail `71` labels=['rank=3,score=8.36'] → hit on 2026-04-27
- 2026-04-26 tail `91` labels=['rank=9,score=6.24'] → hit on 2026-04-27
- 2026-04-28 tail `30` labels=['rank=2,score=8.01'] → hit on 2026-04-29
- 2026-04-28 tail `86` labels=['rank=4,score=7.65'] → hit on 2026-04-29
- 2026-04-29 tail `60` labels=['rank=5,score=6.85'] → hit on 2026-04-30

### MN->MT / V101_MN_D1_D2 / cross_same
- 2026-04-26 tail `57` labels=['rank=1,score=9.06'] → hit on 2026-04-26
- 2026-04-26 tail `71` labels=['rank=3,score=8.36'] → hit on 2026-04-26
- 2026-04-26 tail `39` labels=['rank=7,score=6.85'] → hit on 2026-04-26
- 2026-04-26 tail `91` labels=['rank=9,score=6.24'] → hit on 2026-04-26
- 2026-04-27 tail `62` labels=['rank=3,score=8.0'] → hit on 2026-04-27

### MN->MT / V67 / cross_next
- 2026-05-08 tail `94` labels=['adaptive_exploit_v67_candidate_trace:score=3.6098'] → hit on 2026-05-09

### MN->MT / V70 / cross_next
- 2026-05-08 tail `94` labels=['consensus_v1_trace:agreement_count=2'] → hit on 2026-05-09

### MN->MT / V70 / cross_same
- 2026-05-04 tail `65` labels=['consensus_v1_trace:agreement_count=3'] → hit on 2026-05-04
- 2026-05-07 tail `94` labels=['consensus_v1_trace:agreement_count=5'] → hit on 2026-05-07

### MN->MT / V73 / cross_next
- 2026-05-08 tail `94` labels=['hybrid_v1_trace:confidence_tier=AURA'] → hit on 2026-05-09

### MN->MT / V73 / cross_same
- 2026-05-04 tail `65` labels=['hybrid_v1_trace:confidence_tier=HIGH'] → hit on 2026-05-04

### MT / MODEL::claude-opus-4-20250514 / same_any
- 2026-03-13 tail `58` labels=['1'] → hit on 2026-03-14
- 2026-03-14 tail `06` labels=['1'] → hit on 2026-03-15
- 2026-03-15 tail `32` labels=['0'] → hit on 2026-03-16
- 2026-03-16 tail `65` labels=['1'] → hit on 2026-03-17
- 2026-03-17 tail `90` labels=['1'] → hit on 2026-03-18

### MT / MODEL::claude-sonnet-4-6 / same_any
- 2026-03-11 tail `76` labels=['1'] → hit on 2026-03-12
- 2026-03-14 tail `06` labels=['1'] → hit on 2026-03-15
- 2026-03-17 tail `74` labels=['1'] → hit on 2026-03-18
- 2026-03-18 tail `97` labels=['0'] → hit on 2026-03-19
- 2026-03-18 tail `27` labels=['1'] → hit on 2026-03-19

### MT / MODEL::claude-sonnet-4-6 / same_strict
- 2026-04-04 tail `34` labels=['1'] → hit on 2026-04-05
- 2026-04-11 tail `39` labels=['1'] → hit on 2026-04-12
- 2026-04-27 tail `97` labels=['0'] → hit on 2026-04-28

### MT / MODEL::combo-no-token / same_any
- 2026-03-10 tail `28` labels=['0'] → hit on 2026-03-11
- 2026-03-11 tail `78` labels=['1'] → hit on 2026-03-12
- 2026-03-12 tail `35` labels=['1'] → hit on 2026-03-13
- 2026-03-13 tail `55` labels=['1'] → hit on 2026-03-14
- 2026-03-17 tail `96` labels=['0'] → hit on 2026-03-18

### MT / MODEL::combo-no-token / same_strict
- 2026-04-07 tail `01` labels=['1'] → hit on 2026-04-08

### MT / MODEL::combo-super / same_any
- 2026-03-11 tail `78` labels=['0'] → hit on 2026-03-12
- 2026-03-11 tail `55` labels=['1'] → hit on 2026-03-12
- 2026-03-20 tail `58` labels=['0'] → hit on 2026-03-21
- 2026-03-20 tail `27` labels=['1'] → hit on 2026-03-21
- 2026-03-21 tail `44` labels=['1'] → hit on 2026-03-22

### MT / MODEL::combo-super / same_strict
- 2026-05-02 tail `55` labels=['1'] → hit on 2026-05-03

### MT / MODEL::deepseek-chat / same_any
- 2026-03-11 tail `23` labels=['1'] → hit on 2026-03-12
- 2026-03-12 tail `02` labels=['0'] → hit on 2026-03-13
- 2026-03-14 tail `06` labels=['1'] → hit on 2026-03-15
- 2026-03-15 tail `32` labels=['0'] → hit on 2026-03-16
- 2026-03-18 tail `27` labels=['0'] → hit on 2026-03-19

### MT / MODEL::deepseek-reasoner / same_any
- 2026-03-12 tail `02` labels=['0'] → hit on 2026-03-13
- 2026-03-15 tail `32` labels=['1'] → hit on 2026-03-16
- 2026-03-18 tail `27` labels=['0'] → hit on 2026-03-19
- 2026-03-18 tail `39` labels=['1'] → hit on 2026-03-19
- 2026-03-24 tail `91` labels=['1'] → hit on 2026-03-25

### MT / MODEL::deepseek-reasoner / same_strict
- 2026-03-25 tail `71` labels=['0'] → hit on 2026-03-26
- 2026-04-11 tail `39` labels=['1'] → hit on 2026-04-12
- 2026-05-02 tail `55` labels=['0'] → hit on 2026-05-03

### MT / MODEL::deepseek-v4-flash / same_any
- 2026-04-27 tail `65` labels=['0'] → hit on 2026-04-28
- 2026-04-27 tail `47` labels=['1'] → hit on 2026-04-28
- 2026-04-28 tail `86` labels=['0'] → hit on 2026-04-29
- 2026-04-28 tail `42` labels=['1'] → hit on 2026-04-29
- 2026-04-29 tail `94` labels=['0'] → hit on 2026-04-30

### MT / MODEL::deepseek-v4-pro / same_any
- 2026-04-27 tail `47` labels=['0'] → hit on 2026-04-28
- 2026-04-27 tail `30` labels=['1'] → hit on 2026-04-28
- 2026-04-29 tail `94` labels=['0'] → hit on 2026-04-30
- 2026-04-29 tail `43` labels=['1'] → hit on 2026-04-30
- 2026-04-30 tail `20` labels=['0'] → hit on 2026-05-01

### MT / MODEL::gemini-2.5-flash / same_any
- 2026-03-11 tail `69` labels=['1'] → hit on 2026-03-12
- 2026-03-18 tail `39` labels=['0'] → hit on 2026-03-19
- 2026-03-20 tail `64` labels=['0'] → hit on 2026-03-21
- 2026-03-20 tail `58` labels=['1'] → hit on 2026-03-21
- 2026-03-22 tail `32` labels=['0'] → hit on 2026-03-23

### MT / MODEL::gemini-2.5-flash / same_strict
- 2026-03-25 tail `71` labels=['0'] → hit on 2026-03-26
- 2026-04-07 tail `01` labels=['0'] → hit on 2026-04-08
- 2026-04-27 tail `97` labels=['1'] → hit on 2026-04-28

### MT / MODEL::gemini-2.5-pro / same_any
- 2026-03-12 tail `02` labels=['0'] → hit on 2026-03-13
- 2026-03-15 tail `32` labels=['1'] → hit on 2026-03-16
- 2026-03-20 tail `58` labels=['0'] → hit on 2026-03-21
- 2026-03-20 tail `64` labels=['1'] → hit on 2026-03-21
- 2026-03-22 tail `32` labels=['1'] → hit on 2026-03-23

### MT / MODEL::gemini-2.5-pro / same_strict
- 2026-04-07 tail `01` labels=['1'] → hit on 2026-04-08
- 2026-04-28 tail `64` labels=['0'] → hit on 2026-04-29

### MT / MODEL::gemini-3-flash / same_any
- 2026-05-05 tail `37` labels=['1'] → hit on 2026-05-06
- 2026-05-08 tail `79` labels=['0'] → hit on 2026-05-09

### MT / MODEL::gemini-3.1-pro / same_any
- 2026-05-06 tail `67` labels=['1'] → hit on 2026-05-07
- 2026-05-08 tail `79` labels=['0'] → hit on 2026-05-09

### MT / MODEL::gemma-4-31b / same_any
- 2026-05-05 tail `37` labels=['0'] → hit on 2026-05-06
- 2026-05-06 tail `67` labels=['1'] → hit on 2026-05-07
- 2026-05-08 tail `79` labels=['0'] → hit on 2026-05-09

### MT / MODEL::glm-5.1 / same_any
- 2026-04-16 tail `29` labels=['1'] → hit on 2026-04-17
- 2026-04-17 tail `36` labels=['1'] → hit on 2026-04-18
- 2026-04-18 tail `49` labels=['0'] → hit on 2026-04-19
- 2026-04-18 tail `92` labels=['1'] → hit on 2026-04-19
- 2026-04-21 tail `54` labels=['0'] → hit on 2026-04-22

### MT / MODEL::glm-5.1 / same_strict
- 2026-05-02 tail `55` labels=['0'] → hit on 2026-05-03

### MT / MODEL::gpt-5-mini / same_any
- 2026-03-15 tail `32` labels=['0'] → hit on 2026-03-16
- 2026-03-18 tail `27` labels=['0'] → hit on 2026-03-19
- 2026-03-20 tail `49` labels=['0'] → hit on 2026-03-21
- 2026-03-20 tail `64` labels=['1'] → hit on 2026-03-21
- 2026-03-22 tail `32` labels=['0'] → hit on 2026-03-23

### MT / MODEL::gpt-5-mini / same_strict
- 2026-03-15 tail `73` labels=['2'] → hit on 2026-03-16
- 2026-03-25 tail `71` labels=['0'] → hit on 2026-03-26
- 2026-04-07 tail `01` labels=['1'] → hit on 2026-04-08

### MT / MODEL::gpt-5.4 / same_any
- 2026-03-24 tail `91` labels=['0'] → hit on 2026-03-25
- 2026-03-25 tail `27` labels=['0'] → hit on 2026-03-26
- 2026-03-27 tail `91` labels=['0'] → hit on 2026-03-28
- 2026-04-03 tail `47` labels=['0'] → hit on 2026-04-04
- 2026-04-03 tail `18` labels=['1'] → hit on 2026-04-04

### MT / MODEL::gpt-5.5 / same_any
- 2026-04-27 tail `65` labels=['0'] → hit on 2026-04-28
- 2026-04-27 tail `47` labels=['1'] → hit on 2026-04-28
- 2026-04-28 tail `86` labels=['0'] → hit on 2026-04-29
- 2026-04-29 tail `94` labels=['0'] → hit on 2026-04-30
- 2026-04-29 tail `43` labels=['1'] → hit on 2026-04-30

### MT / MODEL::gpt-oss-120b / same_any
- 2026-04-21 tail `54` labels=['0'] → hit on 2026-04-22
- 2026-04-25 tail `32` labels=['0'] → hit on 2026-04-26
- 2026-04-27 tail `47` labels=['0'] → hit on 2026-04-28
- 2026-04-27 tail `02` labels=['1'] → hit on 2026-04-28
- 2026-04-28 tail `86` labels=['0'] → hit on 2026-04-29

### MT / MODEL::grok-4.20-multi-agent / same_any
- 2026-04-17 tail `36` labels=['1'] → hit on 2026-04-18
- 2026-04-18 tail `49` labels=['1'] → hit on 2026-04-19
- 2026-04-21 tail `54` labels=['1'] → hit on 2026-04-22
- 2026-04-25 tail `32` labels=['0'] → hit on 2026-04-26
- 2026-04-27 tail `47` labels=['0'] → hit on 2026-04-28

### MT / MODEL::kimi-k2.5 / same_any
- 2026-04-16 tail `42` labels=['1'] → hit on 2026-04-17
- 2026-04-17 tail `58` labels=['0'] → hit on 2026-04-18
- 2026-04-18 tail `34` labels=['1'] → hit on 2026-04-19
- 2026-04-21 tail `54` labels=['0'] → hit on 2026-04-22
- 2026-04-25 tail `32` labels=['0'] → hit on 2026-04-26

### MT / MODEL::kimi-k2.5 / same_strict
- 2026-04-17 tail `58` labels=['0'] → hit on 2026-04-18
- 2026-04-22 tail `20` labels=['1'] → hit on 2026-04-23
- 2026-05-02 tail `55` labels=['0'] → hit on 2026-05-03

### MT / MODEL::kimi-k2.6 / same_any
- 2026-04-23 tail `38` labels=['0'] → hit on 2026-04-24

### MT / MODEL::llama-4-maverick / same_any
- 2026-04-21 tail `54` labels=['1'] → hit on 2026-04-22
- 2026-04-22 tail `75` labels=['0'] → hit on 2026-04-23

### MT / MODEL::lstm / same_any
- 2026-03-11 tail `34` labels=['1'] → hit on 2026-03-12
- 2026-03-13 tail `55` labels=['1'] → hit on 2026-03-14
- 2026-03-15 tail `78` labels=['1'] → hit on 2026-03-16
- 2026-03-17 tail `96` labels=['0'] → hit on 2026-03-18
- 2026-03-19 tail `07` labels=['1'] → hit on 2026-03-20

### MT / MODEL::lstm / same_strict
- 2026-04-04 tail `34` labels=['1'] → hit on 2026-04-05
- 2026-04-07 tail `01` labels=['0'] → hit on 2026-04-08

### MT / MODEL::meta-learning / same_any
- 2026-03-11 tail `63` labels=['0'] → hit on 2026-03-12
- 2026-03-12 tail `35` labels=['1'] → hit on 2026-03-13
- 2026-03-15 tail `28` labels=['0'] → hit on 2026-03-16
- 2026-03-20 tail `27` labels=['0'] → hit on 2026-03-21
- 2026-03-23 tail `67` labels=['0'] → hit on 2026-03-24

### MT / MODEL::meta-learning / same_strict
- 2026-05-06 tail `87` labels=['1'] → hit on 2026-05-07

### MT / MODEL::minimax-m2.7 / same_any
- 2026-04-17 tail `97` labels=['0'] → hit on 2026-04-18
- 2026-04-17 tail `36` labels=['1'] → hit on 2026-04-18
- 2026-04-18 tail `92` labels=['0'] → hit on 2026-04-19
- 2026-04-18 tail `34` labels=['1'] → hit on 2026-04-19
- 2026-04-21 tail `54` labels=['0'] → hit on 2026-04-22

### MT / MODEL::mistral-large-3 / same_any
- 2026-04-22 tail `02` labels=['1'] → hit on 2026-04-23

### MT / MODEL::mistral-nemo / same_any
- 2026-04-19 tail `46` labels=['1'] → hit on 2026-04-20
- 2026-04-21 tail `46` labels=['1'] → hit on 2026-04-22

### MT / MODEL::nemotron-3-super / same_any
- 2026-04-18 tail `92` labels=['1'] → hit on 2026-04-19

### MT / MODEL::qwen3-coder / same_any
- 2026-04-13 tail `73` labels=['1'] → hit on 2026-04-14
- 2026-04-15 tail `57` labels=['1'] → hit on 2026-04-16
- 2026-04-16 tail `49` labels=['1'] → hit on 2026-04-17
- 2026-04-17 tail `36` labels=['1'] → hit on 2026-04-18
- 2026-04-21 tail `54` labels=['0'] → hit on 2026-04-22

### MT / MODEL::qwen3-max-thinking / same_any
- 2026-04-17 tail `26` labels=['0'] → hit on 2026-04-18
- 2026-04-21 tail `54` labels=['0'] → hit on 2026-04-22
- 2026-04-22 tail `02` labels=['1'] → hit on 2026-04-23
- 2026-04-25 tail `32` labels=['0'] → hit on 2026-04-26
- 2026-04-27 tail `47` labels=['0'] → hit on 2026-04-28

### MT / MODEL::qwen3.6-plus / same_any
- 2026-04-27 tail `47` labels=['0'] → hit on 2026-04-28
- 2026-04-27 tail `30` labels=['1'] → hit on 2026-04-28
- 2026-04-28 tail `86` labels=['0'] → hit on 2026-04-29
- 2026-04-29 tail `94` labels=['0'] → hit on 2026-04-30
- 2026-04-29 tail `43` labels=['1'] → hit on 2026-04-30

### MT / MODEL::random-forest / same_any
- 2026-03-10 tail `28` labels=['1'] → hit on 2026-03-11
- 2026-03-11 tail `04` labels=['1'] → hit on 2026-03-12
- 2026-03-13 tail `73` labels=['0'] → hit on 2026-03-14
- 2026-03-16 tail `12` labels=['0'] → hit on 2026-03-17
- 2026-03-17 tail `63` labels=['1'] → hit on 2026-03-18

### MT / MODEL::random-forest / same_strict
- 2026-03-19 tail `34` labels=['1'] → hit on 2026-03-20

### MT / MODEL::smart-ensemble / same_any
- 2026-03-11 tail `34` labels=['1'] → hit on 2026-03-12
- 2026-03-12 tail `35` labels=['0'] → hit on 2026-03-13
- 2026-03-13 tail `55` labels=['1'] → hit on 2026-03-14
- 2026-03-15 tail `28` labels=['1'] → hit on 2026-03-16
- 2026-03-17 tail `26` labels=['1'] → hit on 2026-03-18

### MT / MODEL::smart-ensemble / same_strict
- 2026-05-06 tail `87` labels=['1'] → hit on 2026-05-07

### MT / MODEL::smart-ml / same_any
- 2026-03-11 tail `76` labels=['0'] → hit on 2026-03-12
- 2026-03-12 tail `35` labels=['0'] → hit on 2026-03-13
- 2026-03-13 tail `73` labels=['1'] → hit on 2026-03-14
- 2026-03-16 tail `12` labels=['1'] → hit on 2026-03-17
- 2026-03-17 tail `26` labels=['1'] → hit on 2026-03-18

### MT / MODEL::smart-ml / same_strict
- 2026-03-19 tail `34` labels=['0'] → hit on 2026-03-20

### MT / MODEL::xgboost / same_any
- 2026-03-10 tail `15` labels=['1'] → hit on 2026-03-11
- 2026-03-11 tail `76` labels=['1'] → hit on 2026-03-12
- 2026-03-12 tail `35` labels=['1'] → hit on 2026-03-13
- 2026-03-18 tail `20` labels=['1'] → hit on 2026-03-19
- 2026-03-20 tail `27` labels=['0'] → hit on 2026-03-21

### MT / MODEL::xgboost / same_strict
- 2026-04-07 tail `01` labels=['0'] → hit on 2026-04-08
- 2026-05-06 tail `87` labels=['0'] → hit on 2026-05-07

### MT / MODEL_MAIN / same_any
- 2026-03-10 tail `28` labels=['combo-no-token[0]', 'random-forest[1]'] → hit on 2026-03-11
- 2026-03-10 tail `15` labels=['xgboost[1]'] → hit on 2026-03-11
- 2026-03-11 tail `34` labels=['lstm[1]', 'smart-ensemble[1]'] → hit on 2026-03-12
- 2026-03-11 tail `76` labels=['claude-sonnet-4-6[1]', 'smart-ml[0]', 'xgboost[1]'] → hit on 2026-03-12
- 2026-03-11 tail `78` labels=['combo-no-token[1]', 'combo-super[0]'] → hit on 2026-03-12

### MT / MODEL_MAIN / same_strict
- 2026-03-15 tail `73` labels=['gpt-5-mini[2]'] → hit on 2026-03-16
- 2026-03-19 tail `34` labels=['random-forest[1]', 'smart-ml[0]'] → hit on 2026-03-20
- 2026-03-25 tail `71` labels=['deepseek-reasoner[0]', 'gemini-2.5-flash[0]', 'gpt-5-mini[0]'] → hit on 2026-03-26
- 2026-04-04 tail `34` labels=['claude-sonnet-4-6[1]', 'lstm[1]'] → hit on 2026-04-05
- 2026-04-07 tail `01` labels=['combo-no-token[1]', 'gemini-2.5-flash[0]', 'gemini-2.5-pro[1]', 'gpt-5-mini[1]', 'lstm[0]'] → hit on 2026-04-08

### MT / OFFICIAL_BT / same_any
- 2026-03-15 tail `32` labels=['final_bundles.bach_thu'] → hit on 2026-03-16
- 2026-03-20 tail `27` labels=['final_bundles.bach_thu'] → hit on 2026-03-21
- 2026-03-24 tail `91` labels=['final_bundles.bach_thu'] → hit on 2026-03-25
- 2026-03-25 tail `90` labels=['final_bundles.bach_thu'] → hit on 2026-03-26
- 2026-03-27 tail `71` labels=['final_bundles.bach_thu'] → hit on 2026-03-28

### MT / OFFICIAL_BT / same_strict
- 2026-04-07 tail `01` labels=['final_bundles.bach_thu'] → hit on 2026-04-08

### MT / OFFICIAL_LO2 / same_any
- 2026-03-11 tail `76` labels=['final_bundles.lo2'] → hit on 2026-03-12
- 2026-03-12 tail `35` labels=['final_bundles.lo2'] → hit on 2026-03-13
- 2026-03-15 tail `32` labels=['final_bundles.lo2'] → hit on 2026-03-16
- 2026-03-18 tail `27` labels=['final_bundles.lo2'] → hit on 2026-03-19
- 2026-03-20 tail `27` labels=['final_bundles.lo2'] → hit on 2026-03-21

### MT / OFFICIAL_LO2 / same_strict
- 2026-03-25 tail `71` labels=['final_bundles.lo2'] → hit on 2026-03-26
- 2026-04-07 tail `01` labels=['final_bundles.lo2'] → hit on 2026-04-08

### MT / TEST_BT / same_any
- 2026-04-06 tail `68` labels=['MT_OFFICIAL_BASELINE_CONTROL', 'MT_SPECIALIST_ROSTER_V1'] → hit on 2026-04-07
- 2026-04-07 tail `01` labels=['MT_OFFICIAL_BASELINE_CONTROL', 'MT_PRIOR_REGION_CONTEXT_SAFE_V1', 'MT_SPECIALIST_ROSTER_V1'] → hit on 2026-04-08
- 2026-04-09 tail `10` labels=['MT_PRIOR_REGION_CONTEXT_SAFE_V1'] → hit on 2026-04-10
- 2026-04-10 tail `23` labels=['MT_SPECIALIST_ROSTER_V1'] → hit on 2026-04-11
- 2026-04-15 tail `03` labels=['MT_OFFICIAL_BASELINE_CONTROL', 'MT_SPECIALIST_ROSTER_V1'] → hit on 2026-04-16

### MT / TEST_BT / same_strict
- 2026-04-07 tail `01` labels=['MT_OFFICIAL_BASELINE_CONTROL', 'MT_PRIOR_REGION_CONTEXT_SAFE_V1', 'MT_SPECIALIST_ROSTER_V1'] → hit on 2026-04-08

### MT / TEST_LO2 / same_any
- 2026-04-06 tail `68` labels=['MT_AI_CHAIN_PRESERVATION_V1', 'MT_NO_TOKEN_HERD_REDUCTION_V1', 'MT_OFFICIAL_BASELINE_CONTROL', 'MT_PRIOR_REGION_CONTEXT_SAFE_V1', 'MT_SPECIALIST_ROSTER_V1'] → hit on 2026-04-07
- 2026-04-07 tail `01` labels=['MT_AI_CHAIN_PRESERVATION_V1', 'MT_NO_TOKEN_HERD_REDUCTION_V1', 'MT_OFFICIAL_BASELINE_CONTROL', 'MT_PRIOR_REGION_CONTEXT_SAFE_V1', 'MT_SPECIALIST_ROSTER_V1'] → hit on 2026-04-08
- 2026-04-09 tail `10` labels=['MT_PRIOR_REGION_CONTEXT_SAFE_V1'] → hit on 2026-04-10
- 2026-04-10 tail `23` labels=['MT_AI_CHAIN_PRESERVATION_V1', 'MT_NO_TOKEN_HERD_REDUCTION_V1', 'MT_OFFICIAL_BASELINE_CONTROL', 'MT_PRIOR_REGION_CONTEXT_SAFE_V1', 'MT_SPECIALIST_ROSTER_V1'] → hit on 2026-04-11
- 2026-04-15 tail `03` labels=['MT_AI_CHAIN_PRESERVATION_V1', 'MT_NO_TOKEN_HERD_REDUCTION_V1', 'MT_OFFICIAL_BASELINE_CONTROL', 'MT_PRIOR_REGION_CONTEXT_SAFE_V1', 'MT_SPECIALIST_ROSTER_V1'] → hit on 2026-04-16

### MT / TEST_LO2 / same_strict
- 2026-04-07 tail `01` labels=['MT_AI_CHAIN_PRESERVATION_V1', 'MT_NO_TOKEN_HERD_REDUCTION_V1', 'MT_OFFICIAL_BASELINE_CONTROL', 'MT_PRIOR_REGION_CONTEXT_SAFE_V1', 'MT_SPECIALIST_ROSTER_V1'] → hit on 2026-04-08
- 2026-05-06 tail `87` labels=['MT_ADAPTIVE_BUDGET_SELECTOR_V1'] → hit on 2026-05-07

### MT / V67 / same_any
- 2026-05-08 tail `94` labels=['adaptive_exploit_v67_candidate_trace:score=1.2161'] → hit on 2026-05-09
- 2026-05-08 tail `40` labels=['adaptive_exploit_v67_candidate_trace:score=1.0658'] → hit on 2026-05-09

### MT / V70 / same_any
- 2026-05-08 tail `61` labels=['consensus_v1_trace:agreement_count=5'] → hit on 2026-05-09
- 2026-05-08 tail `87` labels=['consensus_v1_trace:agreement_count=1'] → hit on 2026-05-09
- 2026-05-08 tail `94` labels=['consensus_v1_trace:agreement_count=1'] → hit on 2026-05-09

### MT / V73 / same_any
- 2026-05-08 tail `61` labels=['hybrid_v1_trace:confidence_tier=HIGH'] → hit on 2026-05-09

### MT->MB / MODEL::claude-opus-4-20250514 / cross_next
- 2026-03-18 tail `73` labels=['0'] → hit on 2026-03-19
- 2026-03-19 tail `16` labels=['1'] → hit on 2026-03-20
- 2026-03-23 tail `80` labels=['1'] → hit on 2026-03-24
- 2026-03-30 tail `30` labels=['0'] → hit on 2026-03-31
- 2026-04-08 tail `18` labels=['0'] → hit on 2026-04-09

### MT->MB / MODEL::claude-opus-4-20250514 / cross_same
- 2026-03-10 tail `37` labels=['0'] → hit on 2026-03-10
- 2026-03-12 tail `96` labels=['0'] → hit on 2026-03-12
- 2026-03-17 tail `90` labels=['1'] → hit on 2026-03-17
- 2026-04-11 tail `16` labels=['0'] → hit on 2026-04-11
- 2026-04-15 tail `75` labels=['1'] → hit on 2026-04-15

### MT->MB / MODEL::claude-sonnet-4-6 / cross_next
- 2026-03-15 tail `74` labels=['1'] → hit on 2026-03-16
- 2026-03-17 tail `74` labels=['1'] → hit on 2026-03-18
- 2026-03-18 tail `97` labels=['0'] → hit on 2026-03-19
- 2026-03-19 tail `16` labels=['1'] → hit on 2026-03-20
- 2026-03-21 tail `54` labels=['0'] → hit on 2026-03-22

### MT->MB / MODEL::claude-sonnet-4-6 / cross_same
- 2026-03-10 tail `37` labels=['1'] → hit on 2026-03-10
- 2026-03-20 tail `64` labels=['0'] → hit on 2026-03-20
- 2026-03-20 tail `46` labels=['1'] → hit on 2026-03-20
- 2026-03-22 tail `38` labels=['1'] → hit on 2026-03-22
- 2026-04-04 tail `56` labels=['0'] → hit on 2026-04-04

### MT->MB / MODEL::combo-no-token / cross_next
- 2026-03-10 tail `28` labels=['0'] → hit on 2026-03-11
- 2026-03-13 tail `55` labels=['1'] → hit on 2026-03-14
- 2026-03-18 tail `91` labels=['0'] → hit on 2026-03-19
- 2026-03-19 tail `91` labels=['1'] → hit on 2026-03-20
- 2026-03-21 tail `18` labels=['1'] → hit on 2026-03-22

### MT->MB / MODEL::combo-no-token / cross_same
- 2026-03-10 tail `28` labels=['0'] → hit on 2026-03-10
- 2026-03-14 tail `28` labels=['0'] → hit on 2026-03-14
- 2026-03-15 tail `44` labels=['0'] → hit on 2026-03-15
- 2026-03-15 tail `68` labels=['1'] → hit on 2026-03-15
- 2026-03-18 tail `91` labels=['0'] → hit on 2026-03-18

### MT->MB / MODEL::combo-super / cross_next
- 2026-03-15 tail `74` labels=['1'] → hit on 2026-03-16
- 2026-03-17 tail `64` labels=['0'] → hit on 2026-03-18
- 2026-03-18 tail `91` labels=['0'] → hit on 2026-03-19
- 2026-03-30 tail `42` labels=['0'] → hit on 2026-03-31
- 2026-04-03 tail `23` labels=['1'] → hit on 2026-04-04

### MT->MB / MODEL::combo-super / cross_same
- 2026-03-10 tail `78` labels=['1'] → hit on 2026-03-10
- 2026-03-18 tail `91` labels=['0'] → hit on 2026-03-18
- 2026-03-19 tail `94` labels=['2'] → hit on 2026-03-19
- 2026-03-20 tail `27` labels=['1'] → hit on 2026-03-20
- 2026-03-22 tail `43` labels=['1'] → hit on 2026-03-22

### MT->MB / MODEL::deepseek-chat / cross_next
- 2026-03-13 tail `48` labels=['0'] → hit on 2026-03-14
- 2026-03-16 tail `69` labels=['0'] → hit on 2026-03-17
- 2026-03-17 tail `64` labels=['1'] → hit on 2026-03-18
- 2026-03-18 tail `39` labels=['1'] → hit on 2026-03-19
- 2026-03-19 tail `16` labels=['1'] → hit on 2026-03-20

### MT->MB / MODEL::deepseek-chat / cross_same
- 2026-03-12 tail `96` labels=['1'] → hit on 2026-03-12
- 2026-03-20 tail `64` labels=['1'] → hit on 2026-03-20
- 2026-03-22 tail `39` labels=['0'] → hit on 2026-03-22

### MT->MB / MODEL::deepseek-reasoner / cross_next
- 2026-03-18 tail `39` labels=['1'] → hit on 2026-03-19
- 2026-03-30 tail `13` labels=['0'] → hit on 2026-03-31
- 2026-04-08 tail `18` labels=['0'] → hit on 2026-04-09
- 2026-04-09 tail `10` labels=['1'] → hit on 2026-04-10
- 2026-04-12 tail `20` labels=['1'] → hit on 2026-04-13

### MT->MB / MODEL::deepseek-reasoner / cross_same
- 2026-03-10 tail `37` labels=['1'] → hit on 2026-03-10
- 2026-03-24 tail `91` labels=['1'] → hit on 2026-03-24
- 2026-03-28 tail `61` labels=['1'] → hit on 2026-03-28
- 2026-03-30 tail `13` labels=['0'] → hit on 2026-03-30
- 2026-04-01 tail `16` labels=['1'] → hit on 2026-04-01

### MT->MB / MODEL::deepseek-v4-flash / cross_next
- 2026-04-28 tail `42` labels=['1'] → hit on 2026-04-29
- 2026-05-03 tail `17` labels=['1'] → hit on 2026-05-04
- 2026-05-07 tail `93` labels=['0'] → hit on 2026-05-08
- 2026-05-08 tail `79` labels=['0'] → hit on 2026-05-09

### MT->MB / MODEL::deepseek-v4-flash / cross_same
- 2026-04-27 tail `47` labels=['1'] → hit on 2026-04-27
- 2026-05-04 tail `42` labels=['0'] → hit on 2026-05-04
- 2026-05-07 tail `40` labels=['1'] → hit on 2026-05-07
- 2026-05-08 tail `79` labels=['0'] → hit on 2026-05-08
- 2026-05-08 tail `87` labels=['1'] → hit on 2026-05-08

### MT->MB / MODEL::deepseek-v4-pro / cross_next
- 2026-04-27 tail `30` labels=['1'] → hit on 2026-04-28
- 2026-05-01 tail `73` labels=['0'] → hit on 2026-05-02
- 2026-05-03 tail `67` labels=['0'] → hit on 2026-05-04
- 2026-05-03 tail `30` labels=['1'] → hit on 2026-05-04
- 2026-05-08 tail `79` labels=['0'] → hit on 2026-05-09

### MT->MB / MODEL::deepseek-v4-pro / cross_same
- 2026-04-27 tail `47` labels=['0'] → hit on 2026-04-27
- 2026-05-05 tail `37` labels=['0'] → hit on 2026-05-05
- 2026-05-07 tail `40` labels=['0'] → hit on 2026-05-07
- 2026-05-08 tail `79` labels=['0'] → hit on 2026-05-08
- 2026-05-08 tail `87` labels=['1'] → hit on 2026-05-08

### MT->MB / MODEL::gemini-2.5-flash / cross_next
- 2026-03-13 tail `48` labels=['1'] → hit on 2026-03-14
- 2026-03-17 tail `64` labels=['0'] → hit on 2026-03-18
- 2026-03-18 tail `39` labels=['0'] → hit on 2026-03-19
- 2026-03-22 tail `28` labels=['1'] → hit on 2026-03-23
- 2026-03-30 tail `16` labels=['1'] → hit on 2026-03-31

### MT->MB / MODEL::gemini-2.5-flash / cross_same
- 2026-03-10 tail `37` labels=['1'] → hit on 2026-03-10
- 2026-03-11 tail `69` labels=['1'] → hit on 2026-03-11
- 2026-03-12 tail `96` labels=['1'] → hit on 2026-03-12
- 2026-03-14 tail `83` labels=['0'] → hit on 2026-03-14
- 2026-03-20 tail `64` labels=['0'] → hit on 2026-03-20

### MT->MB / MODEL::gemini-2.5-pro / cross_next
- 2026-03-16 tail `69` labels=['1'] → hit on 2026-03-17
- 2026-03-17 tail `64` labels=['0'] → hit on 2026-03-18
- 2026-03-21 tail `54` labels=['1'] → hit on 2026-03-22
- 2026-03-25 tail `99` labels=['0'] → hit on 2026-03-26
- 2026-03-25 tail `27` labels=['1'] → hit on 2026-03-26

### MT->MB / MODEL::gemini-2.5-pro / cross_same
- 2026-03-10 tail `37` labels=['1'] → hit on 2026-03-10
- 2026-03-12 tail `96` labels=['1'] → hit on 2026-03-12
- 2026-03-19 tail `94` labels=['1'] → hit on 2026-03-19
- 2026-03-20 tail `64` labels=['1'] → hit on 2026-03-20
- 2026-03-22 tail `39` labels=['0'] → hit on 2026-03-22

### MT->MB / MODEL::gemini-3-flash / cross_next
- 2026-05-05 tail `13` labels=['0'] → hit on 2026-05-06
- 2026-05-08 tail `79` labels=['0'] → hit on 2026-05-09

### MT->MB / MODEL::gemini-3-flash / cross_same
- 2026-05-05 tail `37` labels=['1'] → hit on 2026-05-05
- 2026-05-07 tail `40` labels=['0'] → hit on 2026-05-07
- 2026-05-08 tail `79` labels=['0'] → hit on 2026-05-08

### MT->MB / MODEL::gemini-3.1-pro / cross_next
- 2026-05-08 tail `79` labels=['0'] → hit on 2026-05-09

### MT->MB / MODEL::gemini-3.1-pro / cross_same
- 2026-05-05 tail `14` labels=['1'] → hit on 2026-05-05
- 2026-05-07 tail `40` labels=['0'] → hit on 2026-05-07
- 2026-05-08 tail `79` labels=['0'] → hit on 2026-05-08

### MT->MB / MODEL::gemma-4-31b / cross_next
- 2026-05-08 tail `79` labels=['0'] → hit on 2026-05-09

### MT->MB / MODEL::gemma-4-31b / cross_same
- 2026-05-05 tail `37` labels=['0'] → hit on 2026-05-05
- 2026-05-07 tail `40` labels=['0'] → hit on 2026-05-07
- 2026-05-08 tail `79` labels=['0'] → hit on 2026-05-08

### MT->MB / MODEL::glm-5.1 / cross_next
- 2026-04-17 tail `36` labels=['1'] → hit on 2026-04-18
- 2026-04-20 tail `64` labels=['0'] → hit on 2026-04-21
- 2026-04-27 tail `82` labels=['1'] → hit on 2026-04-28
- 2026-05-04 tail `88` labels=['0'] → hit on 2026-05-05

### MT->MB / MODEL::glm-5.1 / cross_same
- 2026-04-18 tail `49` labels=['0'] → hit on 2026-04-18
- 2026-04-18 tail `92` labels=['1'] → hit on 2026-04-18
- 2026-04-22 tail `52` labels=['0'] → hit on 2026-04-22
- 2026-04-30 tail `99` labels=['0'] → hit on 2026-04-30
- 2026-05-05 tail `14` labels=['0'] → hit on 2026-05-05

### MT->MB / MODEL::gpt-5-mini / cross_next
- 2026-03-16 tail `69` labels=['0'] → hit on 2026-03-17
- 2026-03-17 tail `64` labels=['1'] → hit on 2026-03-18
- 2026-03-23 tail `64` labels=['1'] → hit on 2026-03-24
- 2026-03-25 tail `27` labels=['1'] → hit on 2026-03-26
- 2026-03-30 tail `30` labels=['1'] → hit on 2026-03-31

### MT->MB / MODEL::gpt-5-mini / cross_same
- 2026-03-18 tail `29` labels=['1'] → hit on 2026-03-18
- 2026-03-20 tail `64` labels=['1'] → hit on 2026-03-20
- 2026-03-22 tail `39` labels=['1'] → hit on 2026-03-22
- 2026-03-28 tail `61` labels=['1'] → hit on 2026-03-28
- 2026-04-09 tail `49` labels=['0'] → hit on 2026-04-09

### MT->MB / MODEL::gpt-5.4 / cross_next
- 2026-03-25 tail `27` labels=['0'] → hit on 2026-03-26
- 2026-03-27 tail `91` labels=['0'] → hit on 2026-03-28
- 2026-03-27 tail `43` labels=['1'] → hit on 2026-03-28
- 2026-03-30 tail `13` labels=['0'] → hit on 2026-03-31
- 2026-04-04 tail `56` labels=['1'] → hit on 2026-04-05

### MT->MB / MODEL::gpt-5.4 / cross_same
- 2026-03-24 tail `91` labels=['0'] → hit on 2026-03-24
- 2026-03-27 tail `91` labels=['0'] → hit on 2026-03-27
- 2026-03-30 tail `13` labels=['0'] → hit on 2026-03-30
- 2026-04-01 tail `16` labels=['1'] → hit on 2026-04-01
- 2026-04-04 tail `56` labels=['1'] → hit on 2026-04-04

### MT->MB / MODEL::gpt-5.5 / cross_next
- 2026-04-30 tail `46` labels=['0'] → hit on 2026-05-01
- 2026-05-03 tail `67` labels=['1'] → hit on 2026-05-04
- 2026-05-08 tail `79` labels=['0'] → hit on 2026-05-09

### MT->MB / MODEL::gpt-5.5 / cross_same
- 2026-04-27 tail `47` labels=['1'] → hit on 2026-04-27
- 2026-05-04 tail `42` labels=['1'] → hit on 2026-05-04
- 2026-05-07 tail `40` labels=['0'] → hit on 2026-05-07
- 2026-05-08 tail `79` labels=['0'] → hit on 2026-05-08

### MT->MB / MODEL::gpt-oss-120b / cross_next
- 2026-04-21 tail `31` labels=['1'] → hit on 2026-04-22
- 2026-04-23 tail `28` labels=['0'] → hit on 2026-04-24
- 2026-04-28 tail `42` labels=['1'] → hit on 2026-04-29
- 2026-04-30 tail `64` labels=['0'] → hit on 2026-05-01
- 2026-04-30 tail `46` labels=['1'] → hit on 2026-05-01

### MT->MB / MODEL::gpt-oss-120b / cross_same
- 2026-04-21 tail `31` labels=['1'] → hit on 2026-04-21
- 2026-04-27 tail `47` labels=['0'] → hit on 2026-04-27
- 2026-05-03 tail `24` labels=['1'] → hit on 2026-05-03
- 2026-05-08 tail `79` labels=['0'] → hit on 2026-05-08

### MT->MB / MODEL::grok-4.20-multi-agent / cross_next
- 2026-04-17 tail `36` labels=['1'] → hit on 2026-04-18
- 2026-04-24 tail `48` labels=['1'] → hit on 2026-04-25
- 2026-04-25 tail `05` labels=['1'] → hit on 2026-04-26
- 2026-04-30 tail `46` labels=['0'] → hit on 2026-05-01
- 2026-05-01 tail `57` labels=['0'] → hit on 2026-05-02

### MT->MB / MODEL::grok-4.20-multi-agent / cross_same
- 2026-04-18 tail `49` labels=['1'] → hit on 2026-04-18
- 2026-04-22 tail `52` labels=['0'] → hit on 2026-04-22
- 2026-04-27 tail `47` labels=['0'] → hit on 2026-04-27
- 2026-05-08 tail `79` labels=['1'] → hit on 2026-05-08

### MT->MB / MODEL::kimi-k2.5 / cross_next
- 2026-04-17 tail `58` labels=['0'] → hit on 2026-04-18
- 2026-04-17 tail `74` labels=['1'] → hit on 2026-04-18
- 2026-04-20 tail `65` labels=['1'] → hit on 2026-04-21
- 2026-04-23 tail `84` labels=['1'] → hit on 2026-04-24
- 2026-04-26 tail `46` labels=['1'] → hit on 2026-04-27

### MT->MB / MODEL::kimi-k2.5 / cross_same
- 2026-04-22 tail `52` labels=['0'] → hit on 2026-04-22
- 2026-04-23 tail `84` labels=['1'] → hit on 2026-04-23
- 2026-04-26 tail `46` labels=['1'] → hit on 2026-04-26
- 2026-04-27 tail `81` labels=['1'] → hit on 2026-04-27
- 2026-05-03 tail `40` labels=['0'] → hit on 2026-05-03

### MT->MB / MODEL::kimi-k2.6 / cross_next
- 2026-04-25 tail `48` labels=['1'] → hit on 2026-04-26

### MT->MB / MODEL::kimi-k2.6 / cross_same
- 2026-04-25 tail `48` labels=['1'] → hit on 2026-04-25

### MT->MB / MODEL::lstm / cross_next
- 2026-03-13 tail `55` labels=['1'] → hit on 2026-03-14
- 2026-03-19 tail `32` labels=['0'] → hit on 2026-03-20
- 2026-03-26 tail `49` labels=['0'] → hit on 2026-03-27
- 2026-03-29 tail `34` labels=['1'] → hit on 2026-03-30
- 2026-03-30 tail `74` labels=['1'] → hit on 2026-03-31

### MT->MB / MODEL::lstm / cross_same
- 2026-03-15 tail `44` labels=['0'] → hit on 2026-03-15
- 2026-03-20 tail `27` labels=['0'] → hit on 2026-03-20
- 2026-03-25 tail `00` labels=['1'] → hit on 2026-03-25
- 2026-03-26 tail `49` labels=['0'] → hit on 2026-03-26
- 2026-03-27 tail `32` labels=['0'] → hit on 2026-03-27

### MT->MB / MODEL::meta-learning / cross_next
- 2026-03-15 tail `28` labels=['0'] → hit on 2026-03-16
- 2026-03-16 tail `54` labels=['1'] → hit on 2026-03-17
- 2026-03-18 tail `91` labels=['0'] → hit on 2026-03-19
- 2026-03-19 tail `91` labels=['1'] → hit on 2026-03-20
- 2026-03-25 tail `51` labels=['1'] → hit on 2026-03-26

### MT->MB / MODEL::meta-learning / cross_same
- 2026-03-14 tail `28` labels=['0'] → hit on 2026-03-14
- 2026-03-18 tail `91` labels=['0'] → hit on 2026-03-18
- 2026-03-19 tail `91` labels=['1'] → hit on 2026-03-19
- 2026-03-20 tail `27` labels=['0'] → hit on 2026-03-20
- 2026-03-24 tail `91` labels=['1'] → hit on 2026-03-24

### MT->MB / MODEL::minimax-m2.7 / cross_next
- 2026-04-17 tail `36` labels=['1'] → hit on 2026-04-18
- 2026-04-24 tail `11` labels=['1'] → hit on 2026-04-25
- 2026-04-26 tail `46` labels=['0'] → hit on 2026-04-27

### MT->MB / MODEL::minimax-m2.7 / cross_same
- 2026-04-18 tail `92` labels=['0'] → hit on 2026-04-18
- 2026-04-22 tail `52` labels=['1'] → hit on 2026-04-22
- 2026-04-24 tail `11` labels=['1'] → hit on 2026-04-24
- 2026-04-26 tail `46` labels=['0'] → hit on 2026-04-26
- 2026-04-27 tail `47` labels=['0'] → hit on 2026-04-27

### MT->MB / MODEL::mistral-large-3 / cross_next
- 2026-04-22 tail `02` labels=['1'] → hit on 2026-04-23

### MT->MB / MODEL::mistral-large-3 / cross_same
- 2026-04-19 tail `64` labels=['1'] → hit on 2026-04-19

### MT->MB / MODEL::mistral-nemo / cross_next
- 2026-04-20 tail `64` labels=['0'] → hit on 2026-04-21
- 2026-04-21 tail `64` labels=['0'] → hit on 2026-04-22

### MT->MB / MODEL::mistral-nemo / cross_same
- 2026-04-19 tail `64` labels=['0'] → hit on 2026-04-19
- 2026-04-21 tail `64` labels=['0'] → hit on 2026-04-21
- 2026-04-22 tail `64` labels=['0'] → hit on 2026-04-22

### MT->MB / MODEL::nemotron-3-super / cross_same
- 2026-04-18 tail `92` labels=['1'] → hit on 2026-04-18

### MT->MB / MODEL::qwen3-coder / cross_next
- 2026-04-13 tail `73` labels=['1'] → hit on 2026-04-14
- 2026-04-17 tail `36` labels=['1'] → hit on 2026-04-18
- 2026-04-22 tail `02` labels=['1'] → hit on 2026-04-23
- 2026-04-23 tail `28` labels=['1'] → hit on 2026-04-24
- 2026-04-28 tail `42` labels=['0'] → hit on 2026-04-29

### MT->MB / MODEL::qwen3-coder / cross_same
- 2026-04-14 tail `50` labels=['0'] → hit on 2026-04-14
- 2026-04-15 tail `75` labels=['0'] → hit on 2026-04-15
- 2026-04-27 tail `47` labels=['0'] → hit on 2026-04-27
- 2026-05-07 tail `40` labels=['0'] → hit on 2026-05-07
- 2026-05-07 tail `15` labels=['1'] → hit on 2026-05-07

### MT->MB / MODEL::qwen3-max-thinking / cross_next
- 2026-04-20 tail `65` labels=['0'] → hit on 2026-04-21
- 2026-04-22 tail `02` labels=['1'] → hit on 2026-04-23
- 2026-04-24 tail `11` labels=['1'] → hit on 2026-04-25
- 2026-05-03 tail `17` labels=['0'] → hit on 2026-05-04
- 2026-05-05 tail `13` labels=['1'] → hit on 2026-05-06

### MT->MB / MODEL::qwen3-max-thinking / cross_same
- 2026-04-22 tail `52` labels=['0'] → hit on 2026-04-22
- 2026-04-24 tail `11` labels=['1'] → hit on 2026-04-24
- 2026-04-27 tail `47` labels=['0'] → hit on 2026-04-27
- 2026-05-04 tail `42` labels=['0'] → hit on 2026-05-04
- 2026-05-05 tail `37` labels=['0'] → hit on 2026-05-05

### MT->MB / MODEL::qwen3.6-plus / cross_next
- 2026-04-27 tail `30` labels=['1'] → hit on 2026-04-28
- 2026-04-30 tail `46` labels=['0'] → hit on 2026-05-01
- 2026-04-30 tail `64` labels=['1'] → hit on 2026-05-01
- 2026-05-03 tail `17` labels=['1'] → hit on 2026-05-04
- 2026-05-08 tail `79` labels=['0'] → hit on 2026-05-09

### MT->MB / MODEL::qwen3.6-plus / cross_same
- 2026-04-27 tail `47` labels=['0'] → hit on 2026-04-27
- 2026-05-04 tail `42` labels=['1'] → hit on 2026-05-04
- 2026-05-05 tail `14` labels=['0'] → hit on 2026-05-05
- 2026-05-05 tail `37` labels=['1'] → hit on 2026-05-05
- 2026-05-07 tail `40` labels=['0'] → hit on 2026-05-07

### MT->MB / MODEL::random-forest / cross_next
- 2026-03-10 tail `28` labels=['1'] → hit on 2026-03-11
- 2026-03-11 tail `04` labels=['1'] → hit on 2026-03-12
- 2026-03-14 tail `35` labels=['0'] → hit on 2026-03-15
- 2026-03-17 tail `63` labels=['1'] → hit on 2026-03-18
- 2026-03-18 tail `91` labels=['0'] → hit on 2026-03-19

### MT->MB / MODEL::random-forest / cross_same
- 2026-03-10 tail `28` labels=['1'] → hit on 2026-03-10
- 2026-03-14 tail `23` labels=['1'] → hit on 2026-03-14
- 2026-03-17 tail `63` labels=['1'] → hit on 2026-03-17
- 2026-03-18 tail `91` labels=['0'] → hit on 2026-03-18
- 2026-03-20 tail `27` labels=['0'] → hit on 2026-03-20

### MT->MB / MODEL::smart-ensemble / cross_next
- 2026-03-13 tail `55` labels=['1'] → hit on 2026-03-14
- 2026-03-15 tail `28` labels=['1'] → hit on 2026-03-16
- 2026-03-18 tail `91` labels=['0'] → hit on 2026-03-19
- 2026-03-26 tail `20` labels=['0'] → hit on 2026-03-27
- 2026-04-11 tail `60` labels=['0'] → hit on 2026-04-12

### MT->MB / MODEL::smart-ensemble / cross_same
- 2026-03-14 tail `28` labels=['1'] → hit on 2026-03-14
- 2026-03-18 tail `91` labels=['0'] → hit on 2026-03-18
- 2026-03-20 tail `27` labels=['0'] → hit on 2026-03-20
- 2026-03-24 tail `63` labels=['0'] → hit on 2026-03-24
- 2026-03-27 tail `32` labels=['0'] → hit on 2026-03-27

### MT->MB / MODEL::smart-ml / cross_next
- 2026-03-10 tail `69` labels=['1'] → hit on 2026-03-11
- 2026-03-18 tail `91` labels=['0'] → hit on 2026-03-19
- 2026-03-21 tail `18` labels=['0'] → hit on 2026-03-22
- 2026-03-23 tail `09` labels=['1'] → hit on 2026-03-24
- 2026-04-04 tail `89` labels=['0'] → hit on 2026-04-05

### MT->MB / MODEL::smart-ml / cross_same
- 2026-03-14 tail `23` labels=['1'] → hit on 2026-03-14
- 2026-03-18 tail `91` labels=['0'] → hit on 2026-03-18
- 2026-03-20 tail `90` labels=['1'] → hit on 2026-03-20
- 2026-03-23 tail `09` labels=['1'] → hit on 2026-03-23
- 2026-03-24 tail `91` labels=['0'] → hit on 2026-03-24

### MT->MB / MODEL::xgboost / cross_next
- 2026-03-10 tail `69` labels=['0'] → hit on 2026-03-11
- 2026-03-16 tail `90` labels=['1'] → hit on 2026-03-17
- 2026-03-17 tail `87` labels=['1'] → hit on 2026-03-18
- 2026-03-18 tail `91` labels=['0'] → hit on 2026-03-19
- 2026-03-19 tail `91` labels=['0'] → hit on 2026-03-20

### MT->MB / MODEL::xgboost / cross_same
- 2026-03-15 tail `42` labels=['1'] → hit on 2026-03-15
- 2026-03-18 tail `91` labels=['0'] → hit on 2026-03-18
- 2026-03-19 tail `91` labels=['0'] → hit on 2026-03-19
- 2026-03-20 tail `27` labels=['0'] → hit on 2026-03-20
- 2026-03-23 tail `09` labels=['1'] → hit on 2026-03-23

### MT->MB / MODEL_MAIN / cross_next
- 2026-03-10 tail `69` labels=['smart-ml[1]', 'xgboost[0]'] → hit on 2026-03-11
- 2026-03-10 tail `28` labels=['combo-no-token[0]', 'random-forest[1]'] → hit on 2026-03-11
- 2026-03-11 tail `04` labels=['random-forest[1]'] → hit on 2026-03-12
- 2026-03-13 tail `55` labels=['combo-no-token[1]', 'lstm[1]', 'smart-ensemble[1]'] → hit on 2026-03-14
- 2026-03-13 tail `48` labels=['deepseek-chat[0]', 'gemini-2.5-flash[1]'] → hit on 2026-03-14

### MT->MB / MODEL_MAIN / cross_same
- 2026-03-10 tail `28` labels=['combo-no-token[0]', 'random-forest[1]'] → hit on 2026-03-10
- 2026-03-10 tail `37` labels=['claude-opus-4-20250514[0]', 'claude-sonnet-4-6[1]', 'deepseek-reasoner[1]', 'gemini-2.5-flash[1]', 'gemini-2.5-pro[1]'] → hit on 2026-03-10
- 2026-03-10 tail `78` labels=['combo-super[1]'] → hit on 2026-03-10
- 2026-03-11 tail `69` labels=['gemini-2.5-flash[1]'] → hit on 2026-03-11
- 2026-03-12 tail `96` labels=['claude-opus-4-20250514[0]', 'deepseek-chat[1]', 'gemini-2.5-flash[1]', 'gemini-2.5-pro[1]'] → hit on 2026-03-12

### MT->MB / OFFICIAL_BT / cross_next
- 2026-03-18 tail `91` labels=['final_bundles.bach_thu'] → hit on 2026-03-19
- 2026-04-07 tail `01` labels=['final_bundles.bach_thu'] → hit on 2026-04-08
- 2026-04-08 tail `18` labels=['final_bundles.bach_thu'] → hit on 2026-04-09
- 2026-04-17 tail `60` labels=['final_bundles.bach_thu'] → hit on 2026-04-18
- 2026-04-21 tail `48` labels=['final_bundles.bach_thu'] → hit on 2026-04-22

### MT->MB / OFFICIAL_BT / cross_same
- 2026-03-18 tail `91` labels=['final_bundles.bach_thu'] → hit on 2026-03-18
- 2026-03-20 tail `27` labels=['final_bundles.bach_thu'] → hit on 2026-03-20
- 2026-03-24 tail `91` labels=['final_bundles.bach_thu'] → hit on 2026-03-24
- 2026-03-25 tail `90` labels=['final_bundles.bach_thu'] → hit on 2026-03-25
- 2026-04-11 tail `16` labels=['final_bundles.bach_thu'] → hit on 2026-04-11

### MT->MB / OFFICIAL_LO2 / cross_next
- 2026-03-17 tail `64` labels=['final_bundles.lo2'] → hit on 2026-03-18
- 2026-03-18 tail `91` labels=['final_bundles.lo2'] → hit on 2026-03-19
- 2026-03-26 tail `20` labels=['final_bundles.lo2'] → hit on 2026-03-27
- 2026-04-07 tail `01` labels=['final_bundles.lo2'] → hit on 2026-04-08
- 2026-04-08 tail `18` labels=['final_bundles.lo2'] → hit on 2026-04-09

### MT->MB / OFFICIAL_LO2 / cross_same
- 2026-03-14 tail `28` labels=['final_bundles.lo2'] → hit on 2026-03-14
- 2026-03-18 tail `91` labels=['final_bundles.lo2'] → hit on 2026-03-18
- 2026-03-20 tail `27` labels=['final_bundles.lo2'] → hit on 2026-03-20
- 2026-03-20 tail `64` labels=['final_bundles.lo2'] → hit on 2026-03-20
- 2026-03-24 tail `91` labels=['final_bundles.lo2'] → hit on 2026-03-24

### MT->MB / TEST_BT / cross_next
- 2026-04-07 tail `01` labels=['MT_OFFICIAL_BASELINE_CONTROL', 'MT_PRIOR_REGION_CONTEXT_SAFE_V1', 'MT_SPECIALIST_ROSTER_V1'] → hit on 2026-04-08
- 2026-04-08 tail `18` labels=['MT_AI_CHAIN_PRESERVATION_V1', 'MT_NO_TOKEN_HERD_REDUCTION_V1', 'MT_OFFICIAL_BASELINE_CONTROL', 'MT_PRIOR_REGION_CONTEXT_SAFE_V1', 'MT_SPECIALIST_ROSTER_V1'] → hit on 2026-04-09
- 2026-04-09 tail `10` labels=['MT_PRIOR_REGION_CONTEXT_SAFE_V1'] → hit on 2026-04-10
- 2026-04-11 tail `95` labels=['MT_PRIOR_REGION_CONTEXT_SAFE_V1'] → hit on 2026-04-12
- 2026-04-13 tail `03` labels=['MT_PRIOR_REGION_CONTEXT_SAFE_V1', 'MT_SPECIALIST_ROSTER_V1'] → hit on 2026-04-14

### MT->MB / TEST_BT / cross_same
- 2026-04-10 tail `23` labels=['MT_SPECIALIST_ROSTER_V1'] → hit on 2026-04-10
- 2026-04-11 tail `16` labels=['MT_AI_CHAIN_PRESERVATION_V1', 'MT_NO_TOKEN_HERD_REDUCTION_V1', 'MT_OFFICIAL_BASELINE_CONTROL', 'MT_SPECIALIST_ROSTER_V1', 'MT_STRENGTH_WEIGHTED_V52_5_2'] → hit on 2026-04-11
- 2026-04-17 tail `60` labels=['MT_NO_TOKEN_HERD_REDUCTION_V1', 'MT_OFFICIAL_BASELINE_CONTROL', 'MT_SPECIALIST_ROSTER_V1', 'MT_STRENGTH_WEIGHTED_V52_5_2'] → hit on 2026-04-17
- 2026-04-18 tail `92` labels=['MT_AI_CHAIN_PRESERVATION_V1', 'MT_PRIOR_REGION_CONTEXT_SAFE_V1', 'MT_STRENGTH_WEIGHTED_V52_5_2'] → hit on 2026-04-18
- 2026-04-20 tail `66` labels=['MT_NO_TOKEN_HERD_REDUCTION_V1', 'MT_OFFICIAL_BASELINE_CONTROL', 'MT_SPECIALIST_ROSTER_V1'] → hit on 2026-04-20

### MT->MB / TEST_LO2 / cross_next
- 2026-04-07 tail `01` labels=['MT_AI_CHAIN_PRESERVATION_V1', 'MT_NO_TOKEN_HERD_REDUCTION_V1', 'MT_OFFICIAL_BASELINE_CONTROL', 'MT_PRIOR_REGION_CONTEXT_SAFE_V1', 'MT_SPECIALIST_ROSTER_V1'] → hit on 2026-04-08
- 2026-04-08 tail `18` labels=['MT_AI_CHAIN_PRESERVATION_V1', 'MT_NO_TOKEN_HERD_REDUCTION_V1', 'MT_OFFICIAL_BASELINE_CONTROL', 'MT_PRIOR_REGION_CONTEXT_SAFE_V1', 'MT_SPECIALIST_ROSTER_V1'] → hit on 2026-04-09
- 2026-04-09 tail `10` labels=['MT_PRIOR_REGION_CONTEXT_SAFE_V1'] → hit on 2026-04-10
- 2026-04-11 tail `95` labels=['MT_AI_CHAIN_PRESERVATION_V1', 'MT_NO_TOKEN_HERD_REDUCTION_V1', 'MT_OFFICIAL_BASELINE_CONTROL', 'MT_PRIOR_REGION_CONTEXT_SAFE_V1', 'MT_SPECIALIST_ROSTER_V1'] → hit on 2026-04-12
- 2026-04-13 tail `03` labels=['MT_PRIOR_REGION_CONTEXT_SAFE_V1', 'MT_SPECIALIST_ROSTER_V1'] → hit on 2026-04-14

### MT->MB / TEST_LO2 / cross_same
- 2026-04-10 tail `23` labels=['MT_AI_CHAIN_PRESERVATION_V1', 'MT_NO_TOKEN_HERD_REDUCTION_V1', 'MT_OFFICIAL_BASELINE_CONTROL', 'MT_PRIOR_REGION_CONTEXT_SAFE_V1', 'MT_SPECIALIST_ROSTER_V1'] → hit on 2026-04-10
- 2026-04-11 tail `16` labels=['MT_AI_CHAIN_PRESERVATION_V1', 'MT_NO_TOKEN_HERD_REDUCTION_V1', 'MT_OFFICIAL_BASELINE_CONTROL', 'MT_PRIOR_REGION_CONTEXT_SAFE_V1', 'MT_SPECIALIST_ROSTER_V1'] → hit on 2026-04-11
- 2026-04-17 tail `60` labels=['MT_AI_CHAIN_PRESERVATION_V1', 'MT_NO_TOKEN_HERD_REDUCTION_V1', 'MT_OFFICIAL_BASELINE_CONTROL', 'MT_PRIOR_REGION_CONTEXT_SAFE_V1', 'MT_SPECIALIST_ROSTER_V1'] → hit on 2026-04-17
- 2026-04-18 tail `92` labels=['MT_AI_CHAIN_PRESERVATION_V1', 'MT_PRIOR_REGION_CONTEXT_SAFE_V1', 'MT_STRENGTH_WEIGHTED_V52_5_2'] → hit on 2026-04-18
- 2026-04-20 tail `66` labels=['MT_AI_CHAIN_PRESERVATION_V1', 'MT_NO_TOKEN_HERD_REDUCTION_V1', 'MT_OFFICIAL_BASELINE_CONTROL', 'MT_PRIOR_REGION_CONTEXT_SAFE_V1', 'MT_SPECIALIST_ROSTER_V1'] → hit on 2026-04-20

### MT->MB / V67 / cross_same
- 2026-05-08 tail `94` labels=['adaptive_exploit_v67_candidate_trace:score=1.2161'] → hit on 2026-05-08

### MT->MB / V70 / cross_same
- 2026-05-08 tail `61` labels=['consensus_v1_trace:agreement_count=5'] → hit on 2026-05-08
- 2026-05-08 tail `87` labels=['consensus_v1_trace:agreement_count=1'] → hit on 2026-05-08
- 2026-05-08 tail `94` labels=['consensus_v1_trace:agreement_count=1'] → hit on 2026-05-08

### MT->MB / V73 / cross_same
- 2026-05-08 tail `61` labels=['hybrid_v1_trace:confidence_tier=HIGH'] → hit on 2026-05-08

### MT->MN / MODEL::claude-opus-4-20250514 / cross_next
- 2026-03-10 tail `37` labels=['0'] → hit on 2026-03-11
- 2026-03-12 tail `96` labels=['0'] → hit on 2026-03-13
- 2026-03-13 tail `19` labels=['0'] → hit on 2026-03-14
- 2026-03-14 tail `06` labels=['1'] → hit on 2026-03-15
- 2026-03-15 tail `32` labels=['0'] → hit on 2026-03-16

### MT->MN / MODEL::claude-sonnet-4-6 / cross_next
- 2026-03-10 tail `37` labels=['1'] → hit on 2026-03-11
- 2026-03-13 tail `19` labels=['0'] → hit on 2026-03-14
- 2026-03-14 tail `06` labels=['1'] → hit on 2026-03-15
- 2026-03-15 tail `21` labels=['0'] → hit on 2026-03-16
- 2026-03-17 tail `74` labels=['1'] → hit on 2026-03-18

### MT->MN / MODEL::combo-no-token / cross_next
- 2026-03-11 tail `35` labels=['0'] → hit on 2026-03-12
- 2026-03-15 tail `68` labels=['1'] → hit on 2026-03-16
- 2026-03-16 tail `36` labels=['1'] → hit on 2026-03-17
- 2026-03-20 tail `61` labels=['1'] → hit on 2026-03-21
- 2026-03-21 tail `18` labels=['1'] → hit on 2026-03-22

### MT->MN / MODEL::combo-super / cross_next
- 2026-03-12 tail `19` labels=['2'] → hit on 2026-03-13
- 2026-03-13 tail `19` labels=['2'] → hit on 2026-03-14
- 2026-03-14 tail `15` labels=['0'] → hit on 2026-03-15
- 2026-03-14 tail `08` labels=['1'] → hit on 2026-03-15
- 2026-03-20 tail `69` labels=['2'] → hit on 2026-03-21

### MT->MN / MODEL::deepseek-chat / cross_next
- 2026-03-12 tail `96` labels=['1'] → hit on 2026-03-13
- 2026-03-13 tail `48` labels=['0'] → hit on 2026-03-14
- 2026-03-13 tail `19` labels=['1'] → hit on 2026-03-14
- 2026-03-14 tail `06` labels=['1'] → hit on 2026-03-15
- 2026-03-15 tail `32` labels=['0'] → hit on 2026-03-16

### MT->MN / MODEL::deepseek-reasoner / cross_next
- 2026-03-10 tail `37` labels=['1'] → hit on 2026-03-11
- 2026-03-14 tail `74` labels=['1'] → hit on 2026-03-15
- 2026-03-15 tail `15` labels=['0'] → hit on 2026-03-16
- 2026-03-15 tail `32` labels=['1'] → hit on 2026-03-16
- 2026-03-18 tail `27` labels=['0'] → hit on 2026-03-19

### MT->MN / MODEL::deepseek-v4-flash / cross_next
- 2026-04-27 tail `47` labels=['1'] → hit on 2026-04-28
- 2026-04-28 tail `86` labels=['0'] → hit on 2026-04-29
- 2026-04-28 tail `42` labels=['1'] → hit on 2026-04-29
- 2026-05-01 tail `74` labels=['0'] → hit on 2026-05-02
- 2026-05-02 tail `15` labels=['1'] → hit on 2026-05-03

### MT->MN / MODEL::deepseek-v4-pro / cross_next
- 2026-04-27 tail `47` labels=['0'] → hit on 2026-04-28
- 2026-05-01 tail `73` labels=['0'] → hit on 2026-05-02
- 2026-05-02 tail `71` labels=['0'] → hit on 2026-05-03
- 2026-05-03 tail `30` labels=['1'] → hit on 2026-05-04
- 2026-05-05 tail `37` labels=['0'] → hit on 2026-05-06

### MT->MN / MODEL::gemini-2.5-flash / cross_next
- 2026-03-10 tail `37` labels=['1'] → hit on 2026-03-11
- 2026-03-11 tail `69` labels=['1'] → hit on 2026-03-12
- 2026-03-12 tail `96` labels=['1'] → hit on 2026-03-13
- 2026-03-13 tail `19` labels=['0'] → hit on 2026-03-14
- 2026-03-13 tail `48` labels=['1'] → hit on 2026-03-14

### MT->MN / MODEL::gemini-2.5-pro / cross_next
- 2026-03-10 tail `37` labels=['1'] → hit on 2026-03-11
- 2026-03-11 tail `54` labels=['1'] → hit on 2026-03-12
- 2026-03-12 tail `96` labels=['1'] → hit on 2026-03-13
- 2026-03-13 tail `19` labels=['1'] → hit on 2026-03-14
- 2026-03-14 tail `49` labels=['1'] → hit on 2026-03-15

### MT->MN / MODEL::gemini-3-flash / cross_next
- 2026-05-05 tail `13` labels=['0'] → hit on 2026-05-06
- 2026-05-05 tail `37` labels=['1'] → hit on 2026-05-06
- 2026-05-08 tail `79` labels=['0'] → hit on 2026-05-09
- 2026-05-08 tail `89` labels=['1'] → hit on 2026-05-09

### MT->MN / MODEL::gemini-3.1-pro / cross_next
- 2026-05-08 tail `79` labels=['0'] → hit on 2026-05-09
- 2026-05-08 tail `89` labels=['1'] → hit on 2026-05-09

### MT->MN / MODEL::gemma-4-31b / cross_next
- 2026-05-05 tail `37` labels=['0'] → hit on 2026-05-06
- 2026-05-05 tail `03` labels=['1'] → hit on 2026-05-06
- 2026-05-08 tail `79` labels=['0'] → hit on 2026-05-09
- 2026-05-08 tail `89` labels=['1'] → hit on 2026-05-09

### MT->MN / MODEL::glm-5.1 / cross_next
- 2026-04-13 tail `54` labels=['1'] → hit on 2026-04-14
- 2026-04-16 tail `29` labels=['1'] → hit on 2026-04-17
- 2026-04-17 tail `87` labels=['0'] → hit on 2026-04-18
- 2026-04-17 tail `36` labels=['1'] → hit on 2026-04-18
- 2026-04-22 tail `52` labels=['0'] → hit on 2026-04-23

### MT->MN / MODEL::gpt-5-mini / cross_next
- 2026-03-15 tail `32` labels=['0'] → hit on 2026-03-16
- 2026-03-16 tail `69` labels=['0'] → hit on 2026-03-17
- 2026-03-18 tail `27` labels=['0'] → hit on 2026-03-19
- 2026-03-20 tail `64` labels=['1'] → hit on 2026-03-21
- 2026-03-22 tail `39` labels=['1'] → hit on 2026-03-23

### MT->MN / MODEL::gpt-5.4 / cross_next
- 2026-03-24 tail `91` labels=['0'] → hit on 2026-03-25
- 2026-03-28 tail `74` labels=['0'] → hit on 2026-03-29
- 2026-03-28 tail `10` labels=['1'] → hit on 2026-03-29
- 2026-04-01 tail `16` labels=['1'] → hit on 2026-04-02
- 2026-04-03 tail `18` labels=['1'] → hit on 2026-04-04

### MT->MN / MODEL::gpt-5.5 / cross_next
- 2026-04-27 tail `47` labels=['1'] → hit on 2026-04-28
- 2026-04-28 tail `86` labels=['0'] → hit on 2026-04-29
- 2026-05-01 tail `44` labels=['1'] → hit on 2026-05-02
- 2026-05-02 tail `71` labels=['1'] → hit on 2026-05-03
- 2026-05-08 tail `79` labels=['0'] → hit on 2026-05-09

### MT->MN / MODEL::gpt-oss-120b / cross_next
- 2026-04-20 tail `03` labels=['0'] → hit on 2026-04-21
- 2026-04-21 tail `31` labels=['1'] → hit on 2026-04-22
- 2026-04-23 tail `28` labels=['0'] → hit on 2026-04-24
- 2026-04-23 tail `73` labels=['1'] → hit on 2026-04-24
- 2026-04-25 tail `32` labels=['0'] → hit on 2026-04-26

### MT->MN / MODEL::grok-4.20-multi-agent / cross_next
- 2026-04-13 tail `24` labels=['0'] → hit on 2026-04-14
- 2026-04-14 tail `31` labels=['0'] → hit on 2026-04-15
- 2026-04-17 tail `36` labels=['1'] → hit on 2026-04-18
- 2026-04-20 tail `03` labels=['0'] → hit on 2026-04-21
- 2026-04-21 tail `50` labels=['0'] → hit on 2026-04-22

### MT->MN / MODEL::kimi-k2.5 / cross_next
- 2026-04-17 tail `58` labels=['0'] → hit on 2026-04-18
- 2026-04-17 tail `74` labels=['1'] → hit on 2026-04-18
- 2026-04-21 tail `50` labels=['1'] → hit on 2026-04-22
- 2026-04-22 tail `52` labels=['0'] → hit on 2026-04-23
- 2026-04-25 tail `32` labels=['0'] → hit on 2026-04-26

### MT->MN / MODEL::kimi-k2.6 / cross_next
- 2026-04-25 tail `16` labels=['0'] → hit on 2026-04-26
- 2026-04-25 tail `48` labels=['1'] → hit on 2026-04-26

### MT->MN / MODEL::llama-4-maverick / cross_next
- 2026-04-20 tail `03` labels=['0'] → hit on 2026-04-21
- 2026-04-21 tail `50` labels=['0'] → hit on 2026-04-22
- 2026-04-22 tail `75` labels=['0'] → hit on 2026-04-23

### MT->MN / MODEL::lstm / cross_next
- 2026-03-11 tail `35` labels=['0'] → hit on 2026-03-12
- 2026-03-11 tail `34` labels=['1'] → hit on 2026-03-12
- 2026-03-12 tail `19` labels=['1'] → hit on 2026-03-13
- 2026-03-19 tail `32` labels=['0'] → hit on 2026-03-20
- 2026-03-23 tail `48` labels=['0'] → hit on 2026-03-24

### MT->MN / MODEL::meta-learning / cross_next
- 2026-03-10 tail `04` labels=['1'] → hit on 2026-03-11
- 2026-03-14 tail `08` labels=['1'] → hit on 2026-03-15
- 2026-03-15 tail `28` labels=['0'] → hit on 2026-03-16
- 2026-03-20 tail `61` labels=['1'] → hit on 2026-03-21
- 2026-03-23 tail `67` labels=['0'] → hit on 2026-03-24

### MT->MN / MODEL::minimax-m2.7 / cross_next
- 2026-04-17 tail `36` labels=['1'] → hit on 2026-04-18
- 2026-04-20 tail `03` labels=['0'] → hit on 2026-04-21
- 2026-04-22 tail `52` labels=['1'] → hit on 2026-04-23
- 2026-04-24 tail `11` labels=['1'] → hit on 2026-04-25
- 2026-04-25 tail `32` labels=['0'] → hit on 2026-04-26

### MT->MN / MODEL::mistral-large-3 / cross_next
- 2026-04-19 tail `64` labels=['1'] → hit on 2026-04-20
- 2026-04-20 tail `03` labels=['0'] → hit on 2026-04-21
- 2026-04-22 tail `02` labels=['1'] → hit on 2026-04-23

### MT->MN / MODEL::mistral-nemo / cross_next
- 2026-04-19 tail `64` labels=['0'] → hit on 2026-04-20
- 2026-04-19 tail `46` labels=['1'] → hit on 2026-04-20
- 2026-04-21 tail `46` labels=['1'] → hit on 2026-04-22

### MT->MN / MODEL::qwen3-coder / cross_next
- 2026-04-13 tail `54` labels=['0'] → hit on 2026-04-14
- 2026-04-13 tail `73` labels=['1'] → hit on 2026-04-14
- 2026-04-14 tail `50` labels=['0'] → hit on 2026-04-15
- 2026-04-14 tail `45` labels=['1'] → hit on 2026-04-15
- 2026-04-17 tail `36` labels=['1'] → hit on 2026-04-18

### MT->MN / MODEL::qwen3-max-thinking / cross_next
- 2026-04-17 tail `87` labels=['1'] → hit on 2026-04-18
- 2026-04-22 tail `52` labels=['0'] → hit on 2026-04-23
- 2026-04-22 tail `02` labels=['1'] → hit on 2026-04-23
- 2026-04-24 tail `11` labels=['1'] → hit on 2026-04-25
- 2026-04-25 tail `32` labels=['0'] → hit on 2026-04-26

### MT->MN / MODEL::qwen3.6-plus / cross_next
- 2026-04-13 tail `24` labels=['0'] → hit on 2026-04-14
- 2026-04-14 tail `31` labels=['0'] → hit on 2026-04-15
- 2026-04-27 tail `47` labels=['0'] → hit on 2026-04-28
- 2026-04-28 tail `86` labels=['0'] → hit on 2026-04-29
- 2026-05-01 tail `44` labels=['0'] → hit on 2026-05-02

### MT->MN / MODEL::random-forest / cross_next
- 2026-03-10 tail `04` labels=['0'] → hit on 2026-03-11
- 2026-03-11 tail `04` labels=['1'] → hit on 2026-03-12
- 2026-03-13 tail `73` labels=['0'] → hit on 2026-03-14
- 2026-03-14 tail `35` labels=['0'] → hit on 2026-03-15
- 2026-03-17 tail `04` labels=['0'] → hit on 2026-03-18

### MT->MN / MODEL::smart-ensemble / cross_next
- 2026-03-11 tail `35` labels=['0'] → hit on 2026-03-12
- 2026-03-11 tail `34` labels=['1'] → hit on 2026-03-12
- 2026-03-15 tail `28` labels=['1'] → hit on 2026-03-16
- 2026-03-17 tail `26` labels=['1'] → hit on 2026-03-18
- 2026-03-23 tail `67` labels=['0'] → hit on 2026-03-24

### MT->MN / MODEL::smart-ml / cross_next
- 2026-03-10 tail `04` labels=['0'] → hit on 2026-03-11
- 2026-03-10 tail `69` labels=['1'] → hit on 2026-03-11
- 2026-03-13 tail `73` labels=['1'] → hit on 2026-03-14
- 2026-03-14 tail `15` labels=['0'] → hit on 2026-03-15
- 2026-03-17 tail `26` labels=['1'] → hit on 2026-03-18

### MT->MN / MODEL::xgboost / cross_next
- 2026-03-10 tail `69` labels=['0'] → hit on 2026-03-11
- 2026-03-10 tail `15` labels=['1'] → hit on 2026-03-11
- 2026-03-14 tail `15` labels=['1'] → hit on 2026-03-15
- 2026-03-15 tail `42` labels=['1'] → hit on 2026-03-16
- 2026-03-17 tail `87` labels=['1'] → hit on 2026-03-18

### MT->MN / MODEL_MAIN / cross_next
- 2026-03-10 tail `04` labels=['meta-learning[1]', 'random-forest[0]', 'smart-ml[0]'] → hit on 2026-03-11
- 2026-03-10 tail `69` labels=['smart-ml[1]', 'xgboost[0]'] → hit on 2026-03-11
- 2026-03-10 tail `15` labels=['xgboost[1]'] → hit on 2026-03-11
- 2026-03-10 tail `37` labels=['claude-opus-4-20250514[0]', 'claude-sonnet-4-6[1]', 'deepseek-reasoner[1]', 'gemini-2.5-flash[1]', 'gemini-2.5-pro[1]'] → hit on 2026-03-11
- 2026-03-11 tail `35` labels=['combo-no-token[0]', 'lstm[0]', 'smart-ensemble[0]'] → hit on 2026-03-12

### MT->MN / OFFICIAL_BT / cross_next
- 2026-03-11 tail `35` labels=['final_bundles.bach_thu'] → hit on 2026-03-12
- 2026-03-15 tail `32` labels=['final_bundles.bach_thu'] → hit on 2026-03-16
- 2026-03-24 tail `91` labels=['final_bundles.bach_thu'] → hit on 2026-03-25
- 2026-03-25 tail `90` labels=['final_bundles.bach_thu'] → hit on 2026-03-26
- 2026-03-28 tail `74` labels=['final_bundles.bach_thu'] → hit on 2026-03-29

### MT->MN / OFFICIAL_LO2 / cross_next
- 2026-03-10 tail `04` labels=['final_bundles.lo2'] → hit on 2026-03-11
- 2026-03-11 tail `35` labels=['final_bundles.lo2'] → hit on 2026-03-12
- 2026-03-15 tail `32` labels=['final_bundles.lo2'] → hit on 2026-03-16
- 2026-03-18 tail `27` labels=['final_bundles.lo2'] → hit on 2026-03-19
- 2026-03-20 tail `64` labels=['final_bundles.lo2'] → hit on 2026-03-21

### MT->MN / TEST_BT / cross_next
- 2026-04-07 tail `01` labels=['MT_OFFICIAL_BASELINE_CONTROL', 'MT_PRIOR_REGION_CONTEXT_SAFE_V1', 'MT_SPECIALIST_ROSTER_V1'] → hit on 2026-04-08
- 2026-04-08 tail `18` labels=['MT_AI_CHAIN_PRESERVATION_V1', 'MT_NO_TOKEN_HERD_REDUCTION_V1', 'MT_OFFICIAL_BASELINE_CONTROL', 'MT_PRIOR_REGION_CONTEXT_SAFE_V1', 'MT_SPECIALIST_ROSTER_V1'] → hit on 2026-04-09
- 2026-04-09 tail `10` labels=['MT_PRIOR_REGION_CONTEXT_SAFE_V1'] → hit on 2026-04-10
- 2026-04-10 tail `34` labels=['MT_AI_CHAIN_PRESERVATION_V1', 'MT_NO_TOKEN_HERD_REDUCTION_V1', 'MT_OFFICIAL_BASELINE_CONTROL', 'MT_PRIOR_REGION_CONTEXT_SAFE_V1', 'MT_STRENGTH_WEIGHTED_V52_5_2'] → hit on 2026-04-11
- 2026-04-11 tail `95` labels=['MT_PRIOR_REGION_CONTEXT_SAFE_V1'] → hit on 2026-04-12

### MT->MN / TEST_LO2 / cross_next
- 2026-04-07 tail `01` labels=['MT_AI_CHAIN_PRESERVATION_V1', 'MT_NO_TOKEN_HERD_REDUCTION_V1', 'MT_OFFICIAL_BASELINE_CONTROL', 'MT_PRIOR_REGION_CONTEXT_SAFE_V1', 'MT_SPECIALIST_ROSTER_V1'] → hit on 2026-04-08
- 2026-04-08 tail `18` labels=['MT_AI_CHAIN_PRESERVATION_V1', 'MT_NO_TOKEN_HERD_REDUCTION_V1', 'MT_OFFICIAL_BASELINE_CONTROL', 'MT_PRIOR_REGION_CONTEXT_SAFE_V1', 'MT_SPECIALIST_ROSTER_V1'] → hit on 2026-04-09
- 2026-04-09 tail `10` labels=['MT_PRIOR_REGION_CONTEXT_SAFE_V1'] → hit on 2026-04-10
- 2026-04-10 tail `34` labels=['MT_AI_CHAIN_PRESERVATION_V1', 'MT_NO_TOKEN_HERD_REDUCTION_V1', 'MT_OFFICIAL_BASELINE_CONTROL', 'MT_PRIOR_REGION_CONTEXT_SAFE_V1', 'MT_SPECIALIST_ROSTER_V1'] → hit on 2026-04-11
- 2026-04-11 tail `95` labels=['MT_AI_CHAIN_PRESERVATION_V1', 'MT_NO_TOKEN_HERD_REDUCTION_V1', 'MT_OFFICIAL_BASELINE_CONTROL', 'MT_PRIOR_REGION_CONTEXT_SAFE_V1', 'MT_SPECIALIST_ROSTER_V1'] → hit on 2026-04-12

### MT->MN / V67 / cross_next
- 2026-05-08 tail `94` labels=['adaptive_exploit_v67_candidate_trace:score=1.2161'] → hit on 2026-05-09

### MT->MN / V70 / cross_next
- 2026-05-08 tail `87` labels=['consensus_v1_trace:agreement_count=1'] → hit on 2026-05-09
- 2026-05-08 tail `94` labels=['consensus_v1_trace:agreement_count=1'] → hit on 2026-05-09

## 7. Interpretation

- Positive lift above baseline means the recurrence is not simply caused by large any-prize tail-set size.
- Any-prize recurrence is diagnostic and must not be called production BT win.
- If a source shows stable +pp over 60d, it should feed V101/V102 shadow ranking, not production.