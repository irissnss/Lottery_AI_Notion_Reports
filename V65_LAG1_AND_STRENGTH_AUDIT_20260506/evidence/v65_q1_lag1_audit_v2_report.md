# V65 Q1 v2 — Lag-1 leakage audit (window 2026-04-07 .. 2026-05-06, 30 days)

## A. Empirical baselines (random hit rate)

| region | avg distinct tails / day | P(hit) k=1 | P(hit) k=2 |
|---|---:|---:|---:|
| MN | 43.1 | 43.0% | 67.8% |
| MT | 35.0 | 35.0% | 58.0% |
| MB | 23.6 | 24.0% | 42.4% |

## B. Per-region × class — any-pick hit rates (control vs lag)

| region | class | n_pred | hit_N | hit_N1 | hit_N2 | hit_N3 | Δ N1−N | random k=2 baseline |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| MB | NO_TOKEN | 210 | 51.4% | 39.9% | 44.3% | 45.8% | -11.5 pp | 42.4% |
| MB | TOKEN | 453 | 39.5% | 46.3% | 41.2% | 42.8% | +6.8 pp | 42.4% |
| MN | NO_TOKEN | 210 | 73.8% | 73.9% | 64.0% | 57.1% | +0.1 pp | 67.8% |
| MN | TOKEN | 451 | 72.9% | 77.9% | 59.8% | 61.2% | +5.0 pp | 67.8% |
| MT | NO_TOKEN | 210 | 66.2% | 62.1% | 60.6% | 56.7% | -4.1 pp | 58.0% |
| MT | TOKEN | 446 | 54.3% | 57.9% | 51.8% | 50.6% | +3.6 pp | 58.0% |

## C. BT (bach-thu) — proper denominators

| region | class | n_pred | bt_hit_N | bt_lose_N | bt_lose_N→bt_hit_N1 | random k=1 baseline | leakage signal |
|---|---|---:|---:|---:|---:|---:|---:|
| MB | NO_TOKEN | 210 | 25.2% | 157 | 24.8% | 24.0% | ≈ baseline (+0.8 pp) |
| MB | TOKEN | 453 | 22.1% | 353 | 27.5% | 24.0% | ≈ baseline (+3.5 pp) |
| MN | NO_TOKEN | 210 | 50.0% | 105 | 44.8% | 43.0% | ≈ baseline (+1.8 pp) |
| MN | TOKEN | 451 | 50.1% | 225 | 57.3% | 43.0% | ⚠ above (+14.3 pp) |
| MT | NO_TOKEN | 210 | 44.8% | 116 | 41.4% | 35.0% | ⚠ above (+6.4 pp) |
| MT | TOKEN | 446 | 31.2% | 307 | 40.1% | 35.0% | ⚠ above (+5.1 pp) |

## D. Status-based (using predictions.status='LOSE' as truth)

| region | class | status_LOSE | →any_hit_N1 | →bt_hit_N1 |
|---|---|---:|---:|---:|
| MB | NO_TOKEN | 102 | 38.2% | 22.5% |
| MB | TOKEN | 274 | 42.3% | 25.5% |
| MN | NO_TOKEN | 55 | 67.3% | 45.5% |
| MN | TOKEN | 122 | 72.1% | 59.0% |
| MT | NO_TOKEN | 71 | 60.6% | 40.8% |
| MT | TOKEN | 204 | 60.3% | 43.6% |

## E. Per-model BT lag-1 (proper denominator)

| region | model | class | n_pred | bt_lose_N | bt_lose_N→bt_hit_N1 | vs baseline |
|---|---|---|---:|---:|---:|---:|
| MN | combo-no-token | NO_TOKEN | 30 | 12 | 58.3% | 🚨 +15.3 pp |
| MN | combo-super | TOKEN | 30 | 14 | 64.3% | 🚨 +21.3 pp |
| MN | gemini-2.5-flash | TOKEN | 30 | 16 | 50.0% | ⚠ +7.0 pp |
| MN | gemini-2.5-pro | TOKEN | 30 | 13 | 46.2% |  +3.2 pp |
| MN | gpt-5-mini | TOKEN | 30 | 16 | 43.8% |  +0.7 pp |
| MN | gpt-5.4 | TOKEN | 30 | 16 | 56.2% | ⚠ +13.2 pp |
| MN | lstm | NO_TOKEN | 30 | 18 | 33.3% |  -9.7 pp |
| MN | meta-learning | NO_TOKEN | 30 | 14 | 35.7% |  -7.3 pp |
| MN | random-forest | NO_TOKEN | 30 | 18 | 27.8% |  -15.2 pp |
| MN | smart-ensemble | NO_TOKEN | 30 | 13 | 46.2% |  +3.2 pp |
| MN | smart-ml | NO_TOKEN | 30 | 14 | 71.4% | 🚨 +28.4 pp |
| MN | xgboost | NO_TOKEN | 30 | 16 | 50.0% | ⚠ +7.0 pp |
| MN | claude-opus-4-20250514 | TOKEN | 29 | 13 | 69.2% | 🚨 +26.2 pp |
| MN | claude-sonnet-4-6 | TOKEN | 29 | 12 | 58.3% | 🚨 +15.3 pp |
| MN | deepseek-reasoner | TOKEN | 28 | 13 | 76.9% | 🚨 +33.9 pp |
| MN | glm-5.1 | TOKEN | 25 | 13 | 61.5% | 🚨 +18.5 pp |
| MN | grok-4.20-multi-agent | TOKEN | 24 | 13 | 61.5% | 🚨 +18.5 pp |
| MN | qwen3-coder | TOKEN | 24 | 13 | 53.8% | ⚠ +10.8 pp |
| MN | kimi-k2.5 | TOKEN | 21 | 10 | 30.0% |  -13.0 pp |
| MN | qwen3-max-thinking | TOKEN | 21 | 11 | 63.6% | 🚨 +20.6 pp |
| MN | gpt-oss-120b | TOKEN | 18 | 7 | 57.1% | ⚠ +14.1 pp |
| MN | qwen3.6-plus | TOKEN | 13 | 6 | 50.0% | ⚠ +7.0 pp |
| MN | minimax-m2.7 | TOKEN | 12 | 6 | 66.7% | 🚨 +23.7 pp |
| MN | deepseek-v4-flash | TOKEN | 10 | 7 | 85.7% | 🚨 +42.7 pp |
| MN | deepseek-v4-pro | TOKEN | 10 | 4 | 50.0% | ⚠ +7.0 pp |
| MN | gpt-5.5 | TOKEN | 10 | 5 | 60.0% | 🚨 +17.0 pp |
| MN | arcee-trinity | TOKEN | 4 | 0 | — |  -43.0 pp |
| MN | llama-4-maverick | TOKEN | 4 | 2 | 50.0% | ⚠ +7.0 pp |
| MN | mistral-large-3 | TOKEN | 4 | 4 | 50.0% | ⚠ +7.0 pp |
| MN | mistral-nemo | TOKEN | 4 | 3 | 33.3% |  -9.7 pp |
| MN | kimi-k2.6 | TOKEN | 3 | 2 | 50.0% | ⚠ +7.0 pp |
| MN | nemotron-3-super | TOKEN | 2 | 1 | 100.0% | 🚨 +57.0 pp |
| MN | gemini-3-flash | TOKEN | 2 | 1 | 100.0% | 🚨 +57.0 pp |
| MN | gemini-3.1-pro | TOKEN | 2 | 2 | 50.0% | ⚠ +7.0 pp |
| MN | gemma-4-31b | TOKEN | 2 | 2 | 50.0% | ⚠ +7.0 pp |
| MT | combo-no-token | NO_TOKEN | 30 | 15 | 33.3% |  -1.7 pp |
| MT | combo-super | TOKEN | 30 | 21 | 28.6% |  -6.4 pp |
| MT | deepseek-reasoner | TOKEN | 30 | 22 | 45.5% | ⚠ +10.5 pp |
| MT | gemini-2.5-flash | TOKEN | 30 | 21 | 28.6% |  -6.4 pp |
| MT | gemini-2.5-pro | TOKEN | 30 | 22 | 40.9% | ⚠ +5.9 pp |
| MT | gpt-5-mini | TOKEN | 30 | 19 | 36.8% |  +1.8 pp |
| MT | gpt-5.4 | TOKEN | 30 | 22 | 45.5% | ⚠ +10.5 pp |
| MT | lstm | NO_TOKEN | 30 | 20 | 35.0% |  +0.0 pp |
| MT | meta-learning | NO_TOKEN | 30 | 15 | 46.7% | ⚠ +11.7 pp |
| MT | random-forest | NO_TOKEN | 30 | 18 | 61.1% | 🚨 +26.1 pp |
| MT | smart-ensemble | NO_TOKEN | 30 | 15 | 46.7% | ⚠ +11.7 pp |
| MT | smart-ml | NO_TOKEN | 30 | 15 | 46.7% | ⚠ +11.7 pp |
| MT | xgboost | NO_TOKEN | 30 | 18 | 22.2% |  -12.8 pp |
| MT | claude-opus-4-20250514 | TOKEN | 29 | 17 | 35.3% |  +0.3 pp |
| MT | claude-sonnet-4-6 | TOKEN | 29 | 21 | 33.3% |  -1.7 pp |
| MT | grok-4.20-multi-agent | TOKEN | 24 | 14 | 28.6% |  -6.4 pp |
| MT | qwen3-coder | TOKEN | 24 | 15 | 40.0% |  +5.0 pp |
| MT | glm-5.1 | TOKEN | 23 | 15 | 40.0% |  +5.0 pp |
| MT | kimi-k2.5 | TOKEN | 21 | 15 | 40.0% |  +5.0 pp |
| MT | qwen3-max-thinking | TOKEN | 21 | 16 | 50.0% | ⚠ +15.0 pp |
| MT | gpt-oss-120b | TOKEN | 16 | 10 | 50.0% | ⚠ +15.0 pp |
| MT | qwen3.6-plus | TOKEN | 13 | 12 | 41.7% | ⚠ +6.7 pp |
| MT | minimax-m2.7 | TOKEN | 12 | 8 | 62.5% | 🚨 +27.5 pp |
| MT | deepseek-v4-flash | TOKEN | 10 | 6 | 83.3% | 🚨 +48.3 pp |
| MT | deepseek-v4-pro | TOKEN | 10 | 9 | 66.7% | 🚨 +31.7 pp |
| MT | gpt-5.5 | TOKEN | 10 | 5 | 60.0% | 🚨 +25.0 pp |
| MT | llama-4-maverick | TOKEN | 4 | 4 | 25.0% |  -10.0 pp |
| MT | mistral-nemo | TOKEN | 4 | 4 | 0.0% |  -35.0 pp |
| MT | arcee-trinity | TOKEN | 3 | 2 | 0.0% |  -35.0 pp |
| MT | mistral-large-3 | TOKEN | 3 | 2 | 0.0% |  -35.0 pp |
| MT | kimi-k2.6 | TOKEN | 3 | 2 | 50.0% | ⚠ +15.0 pp |
| MT | gemini-3-flash | TOKEN | 2 | 1 | 0.0% |  -35.0 pp |
| MT | gemini-3.1-pro | TOKEN | 2 | 1 | 0.0% |  -35.0 pp |
| MT | gemma-4-31b | TOKEN | 2 | 1 | 100.0% | 🚨 +65.0 pp |
| MT | nemotron-3-super | TOKEN | 1 | 0 | — |  -35.0 pp |
| MB | combo-no-token | NO_TOKEN | 30 | 23 | 17.4% |  -6.6 pp |
| MB | combo-super | TOKEN | 30 | 23 | 34.8% | ⚠ +10.8 pp |
| MB | deepseek-reasoner | TOKEN | 30 | 22 | 27.3% |  +3.3 pp |
| MB | gemini-2.5-flash | TOKEN | 30 | 26 | 34.6% | ⚠ +10.6 pp |
| MB | gemini-2.5-pro | TOKEN | 30 | 25 | 32.0% | ⚠ +8.0 pp |
| MB | gpt-5-mini | TOKEN | 30 | 19 | 42.1% | 🚨 +18.1 pp |
| MB | gpt-5.4 | TOKEN | 30 | 23 | 26.1% |  +2.1 pp |
| MB | lstm | NO_TOKEN | 30 | 19 | 15.8% |  -8.2 pp |
| MB | meta-learning | NO_TOKEN | 30 | 24 | 33.3% | ⚠ +9.3 pp |
| MB | random-forest | NO_TOKEN | 30 | 22 | 27.3% |  +3.3 pp |
| MB | smart-ensemble | NO_TOKEN | 30 | 25 | 24.0% |  +0.0 pp |
| MB | smart-ml | NO_TOKEN | 30 | 20 | 35.0% | ⚠ +11.0 pp |
| MB | xgboost | NO_TOKEN | 30 | 24 | 20.8% |  -3.2 pp |
| MB | claude-opus-4-20250514 | TOKEN | 29 | 24 | 25.0% |  +1.0 pp |
| MB | claude-sonnet-4-6 | TOKEN | 29 | 22 | 31.8% | ⚠ +7.8 pp |
| MB | glm-5.1 | TOKEN | 25 | 20 | 20.0% |  -4.0 pp |
| MB | grok-4.20-multi-agent | TOKEN | 24 | 19 | 26.3% |  +2.3 pp |
| MB | qwen3-coder | TOKEN | 24 | 19 | 21.1% |  -2.9 pp |
| MB | qwen3-max-thinking | TOKEN | 21 | 19 | 21.1% |  -2.9 pp |
| MB | kimi-k2.5 | TOKEN | 20 | 17 | 41.2% | 🚨 +17.2 pp |
| MB | gpt-oss-120b | TOKEN | 17 | 13 | 23.1% |  -0.9 pp |
| MB | qwen3.6-plus | TOKEN | 13 | 10 | 20.0% |  -4.0 pp |
| MB | minimax-m2.7 | TOKEN | 11 | 9 | 11.1% |  -12.9 pp |
| MB | deepseek-v4-flash | TOKEN | 10 | 8 | 25.0% |  +1.0 pp |
| MB | deepseek-v4-pro | TOKEN | 10 | 9 | 22.2% |  -1.8 pp |
| MB | gpt-5.5 | TOKEN | 10 | 6 | 33.3% | ⚠ +9.3 pp |
| MB | arcee-trinity | TOKEN | 6 | 5 | 20.0% |  -4.0 pp |
| MB | llama-4-maverick | TOKEN | 4 | 1 | 0.0% |  -24.0 pp |
| MB | mistral-large-3 | TOKEN | 4 | 1 | 0.0% |  -24.0 pp |
| MB | mistral-nemo | TOKEN | 4 | 3 | 33.3% | ⚠ +9.3 pp |
| MB | kimi-k2.6 | TOKEN | 4 | 4 | 0.0% |  -24.0 pp |
| MB | nemotron-3-super | TOKEN | 2 | 2 | 0.0% |  -24.0 pp |
| MB | gemini-3-flash | TOKEN | 2 | 1 | 0.0% |  -24.0 pp |
| MB | gemini-3.1-pro | TOKEN | 2 | 2 | 50.0% | 🚨 +26.0 pp |
| MB | gemma-4-31b | TOKEN | 2 | 1 | 0.0% |  -24.0 pp |

## F. final_bundles (the actual /du-doan output) — lag-1 BT

| region | n | bt_hit_N | bt_lose_N | bt_lose_N→bt_hit_N1 | baseline | leakage signal |
|---|---:|---:|---:|---:|---:|---:|
| MN | 29 | 55.2% | 13 | 61.5% | 43.0% | 🚨 HIGH (+18.5 pp) |
| MT | 29 | 37.9% | 18 | 44.4% | 35.0% | ⚠ above (+9.4 pp) |
| MB | 29 | 20.7% | 23 | 26.1% | 24.0% | ≈ baseline (+2.1 pp) |

## G. final_bundles BT lose→hit examples

- MT 2026-04-07 BT=01 → on 2026-04-08 actually appeared
- MB 2026-04-08 BT=37 → on 2026-04-09 actually appeared
- MN 2026-04-09 BT=32 → on 2026-04-10 actually appeared
- MN 2026-04-15 BT=98 → on 2026-04-16 actually appeared
- MT 2026-04-15 BT=03 → on 2026-04-16 actually appeared
- MB 2026-04-17 BT=43 → on 2026-04-18 actually appeared
- MT 2026-04-18 BT=80 → on 2026-04-19 actually appeared
- MT 2026-04-21 BT=48 → on 2026-04-22 actually appeared
- MB 2026-04-22 BT=22 → on 2026-04-23 actually appeared
- MT 2026-04-22 BT=85 → on 2026-04-23 actually appeared
- MT 2026-04-24 BT=59 → on 2026-04-25 actually appeared
- MN 2026-04-25 BT=32 → on 2026-04-26 actually appeared
- MB 2026-04-26 BT=93 → on 2026-04-27 actually appeared
- MT 2026-04-27 BT=21 → on 2026-04-28 actually appeared
- MB 2026-04-28 BT=41 → on 2026-04-29 actually appeared
- MN 2026-04-28 BT=19 → on 2026-04-29 actually appeared
- MN 2026-04-29 BT=85 → on 2026-04-30 actually appeared
- MB 2026-04-30 BT=62 → on 2026-05-01 actually appeared
- MN 2026-05-01 BT=51 → on 2026-05-02 actually appeared
- MT 2026-05-03 BT=29 → on 2026-05-04 actually appeared
- MN 2026-05-04 BT=65 → on 2026-05-05 actually appeared
- MN 2026-05-05 BT=15 → on 2026-05-06 actually appeared

## H. Verdict / interpretation

Compare the **leakage signal** column (BT lose_N→hit_N1 vs random baseline):

- 🚨 HIGH (> +15 pp above baseline): genuine timing-shift leakage suspected.
- ⚠ above (> +5 pp): mild signal, watch.
- ≈ baseline (±5 pp): consistent with random chance — no specific leakage.
- below (< −5 pp): models are LESS likely to lag-1 hit than random.

If most rows are `≈ baseline`, the user's intuitive impression is explained by **prize density**, not by a learning bug.
