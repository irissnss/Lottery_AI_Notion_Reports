# 1/8 — ALL MODELS (41 total)

Generated 2026-05-07T23:53:02+07:00

**Statistics**: ACTIVE=15 | SHADOW_AUTO=13 | REMOVED=10 | REGISTERED_INACTIVE=3 | TOKEN=32 | NO_TOKEN=7 | RERANK=2 | OUTPUT_ELIGIBLE=15

| ID | Provider | Class | Role | Status | Output? | Regions | Schedule slots | WR / note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| claude-opus-4-20250514 | anthropic | TOKEN | GENERATOR | ACTIVE | True | MN+MT+MB | 04:15_MN_only+ai_chain_post_verify | WR=76% (best) |
| claude-sonnet-4-6 | anthropic | TOKEN | GENERATOR | ACTIVE | True | MN+MT+MB | 04:15_MN_only+ai_chain_post_verify | WR=73% |
| combo-no-token | local | NO_TOKEN | ENSEMBLE | ACTIVE | True | MN+MT+MB | 04:00_all_regions+cascade_rerun_post_verify | ALL 4 ML models + Cross-Region |
| combo-super | hybrid | TOKEN | ENSEMBLE | ACTIVE | True | MN+MT+MB | 04:15_MN_only+ai_chain_post_verify | 4ML + 7AI hybrid ensemble. Token cost = top-3 AI calls. |
| deepseek-reasoner | deepseek | TOKEN | GENERATOR | ACTIVE | True | MN+MT+MB | 04:15_MN_only+ai_chain_post_verify | WR=62%, MB=67% |
| gemini-2.5-flash | google | TOKEN | GENERATOR | ACTIVE | True | MN+MT+MB | 04:15_MN_only+ai_chain_post_verify | WR=70% |
| gemini-2.5-pro | google | TOKEN | GENERATOR | ACTIVE | True | MN+MT+MB | 04:15_MN_only+ai_chain_post_verify | WR=63%, MN=86% |
| gpt-5-mini | openai | TOKEN | GENERATOR | ACTIVE | True | MN+MT+MB | 04:15_MN_only+ai_chain_post_verify | WR=73% |
| gpt-5.4 | openai | TOKEN | GENERATOR | ACTIVE | True | MN+MT+MB | 04:15_MN_only+ai_chain_post_verify | Replaced deepseek-chat V7.9.12 |
| lstm | local | NO_TOKEN | ML_PREDICTOR | ACTIVE | True | MN+MT+MB | 04:00_all_regions+cascade_rerun_post_verify | Individual ML model |
| meta-learning | local | NO_TOKEN | ML_PREDICTOR | ACTIVE | True | MN+MT+MB | 04:00_all_regions+cascade_rerun_post_verify | Individual ML model |
| random-forest | local | NO_TOKEN | ML_PREDICTOR | ACTIVE | True | MN+MT+MB | 04:00_all_regions+cascade_rerun_post_verify | Individual ML model |
| smart-ensemble | local | NO_TOKEN | ENSEMBLE | ACTIVE | True | MN+MT+MB | 04:00_all_regions+cascade_rerun_post_verify | LSTM + Meta-Learning ensemble |
| smart-ml | local | NO_TOKEN | ENSEMBLE | ACTIVE | True | MN+MT+MB | 04:00_all_regions+cascade_rerun_post_verify | XGBoost + Random Forest ensemble |
| xgboost | local | NO_TOKEN | ML_PREDICTOR | ACTIVE | True | MN+MT+MB | 04:00_all_regions+cascade_rerun_post_verify | Individual ML model |
| cohere-rerank-4-pro | openrouter | RERANK | RERANKER | REGISTERED |  | MN+MT+MB | shadow_rerank_post_combo_super | RERANKER — uses /rerank endpoint. 0 generative tokens. Shadow-only. |
| pplx-embed-v1 | openrouter | RERANK | RERANKER | REGISTERED |  |  |  | REGISTERED V17.19.0 — EMBEDDING model, /embeddings endpoint. NOT chat/completions. |
| wan-2.7 | openrouter | TOKEN | GENERATOR | REGISTERED |  |  |  | REGISTERED V17.19.0 — VIDEO GENERATION model, NOT chat/completions. Cannot produce prediction JSON. |
| arcee-trinity | openrouter | TOKEN | GENERATOR | REMOVED |  |  |  | REMOVED 2026-04-22 — shadow-only model cleared after repeated EMPTY_RESPONSE runtime failures and weak keep value. |
| gemma-4-26b | openrouter | TOKEN | GENERATOR | REMOVED |  |  |  | REMOVED 2026-04-19 — free tier unreliable (429 rate limit upstream), owner decision to remove. |
| kimi-k2.6 | openrouter | TOKEN | GENERATOR | REMOVED |  |  |  | REMOVED 2026-04-27 — owner-directed prune after weak shadow quality and extreme latency; historical prediction/measureme |
| llama-4-maverick | openrouter | TOKEN | GENERATOR | REMOVED |  |  |  | REMOVED 2026-04-22 — shadow-only model cleared after low stability / low incremental value review. |
| minimax-m2.7 | openrouter | TOKEN | GENERATOR | REMOVED |  |  |  | REMOVED 2026-04-28 — shadow-only prune after repeated PHASE-FIRST contract/length failures on MN/MT, high latency, and w |
| mistral-large-3 | openrouter | TOKEN | GENERATOR | REMOVED |  |  |  | REMOVED 2026-04-22 — shadow-only model cleared after repeated instability and insufficient keep value. |
| mistral-nemo | openrouter | TOKEN | GENERATOR | REMOVED |  |  |  | REMOVED 2026-04-22 — shadow-only model cleared by owner direction after repeated instability / low-value review. |
| nemotron-3-super | openrouter | TOKEN | GENERATOR | REMOVED |  |  |  | REMOVED 2026-04-19 (V17.19.4) — paid slug 404 on OpenRouter. Replaced by mistral-nemo. |
| o3-deep-research | openrouter | TOKEN | GENERATOR | REMOVED |  |  |  | REMOVED 2026-04-13 (V17.15.3) — EMPTY_RESPONSE + high cost |
| yi-1.5-34b-chat | openrouter | TOKEN | GENERATOR | REMOVED |  |  |  | REMOVED 2026-04-16 (V17.19.1) — model discontinued on OpenRouter (404). Zero evals. |
| deepseek-v4-flash | deepseek | TOKEN | GENERATOR | SHADOW_AUTO |  | MN+MT+MB | completion_triggered_shadow+shadow_eval_post_verify | SHADOW_AUTO V20.3.35 — owner-routed through official DeepSeek key as direct shadow model, PHASE-FIRST contract cohort. |
| deepseek-v4-pro | deepseek | TOKEN | GENERATOR | SHADOW_AUTO |  | MN+MT+MB | completion_triggered_shadow+shadow_eval_post_verify | SHADOW_AUTO V20.3.35 — owner-routed through official DeepSeek key as direct shadow model, PHASE-FIRST contract cohort. |
| gemini-3-flash | google | TOKEN | GENERATOR | SHADOW_AUTO |  | MN+MT+MB | completion_triggered_shadow+shadow_eval_post_verify | SHADOW_AUTO V20.3.37.55 — owner-added Google direct, PHASE-FIRST contract cohort PFG-20260505-E. |
| gemini-3.1-pro | google | TOKEN | GENERATOR | SHADOW_AUTO |  | MN+MT+MB | completion_triggered_shadow+shadow_eval_post_verify | SHADOW_AUTO V20.3.37.55 — owner-added Google direct, PHASE-FIRST contract cohort PFG-20260505-E. |
| gemma-4-31b | google | TOKEN | GENERATOR | SHADOW_AUTO |  | MN+MT+MB | completion_triggered_shadow+shadow_eval_post_verify | SHADOW_AUTO V20.3.37.55 — owner-added Google direct (Gemma 4 31B-IT), PHASE-FIRST contract cohort PFG-20260505-E. Distin |
| glm-5.1 | openrouter | TOKEN | GENERATOR | SHADOW_AUTO |  | MN+MT+MB | completion_triggered_shadow+shadow_eval_post_verify | SHADOW_AUTO — auto-eval all regions, not output-eligible |
| gpt-5.5 | openrouter | TOKEN | GENERATOR | SHADOW_AUTO |  | MN+MT+MB | completion_triggered_shadow+shadow_eval_post_verify | SHADOW_AUTO V20.3.32 — owner-added OpenAI GPT-5.5 via OpenRouter, PHASE-FIRST contract cohort. |
| gpt-oss-120b | openrouter | TOKEN | GENERATOR | SHADOW_AUTO |  | MN+MT+MB | completion_triggered_shadow+shadow_eval_post_verify | SHADOW_AUTO V17.19.4 — OpenAI open-source 120B MoE, via OpenRouter |
| grok-4.20-multi-agent | openrouter | TOKEN | GENERATOR | SHADOW_AUTO |  | MN+MT+MB | completion_triggered_shadow+shadow_eval_post_verify | SHADOW_AUTO — auto-eval all regions, not output-eligible |
| kimi-k2.5 | openrouter | TOKEN | GENERATOR | SHADOW_AUTO |  | MN+MT+MB | completion_triggered_shadow+shadow_eval_post_verify | SHADOW_AUTO V17.19.0 — MoonshotAI multimodal |
| qwen3-coder | openrouter | TOKEN | GENERATOR | SHADOW_AUTO |  | MN+MT+MB | completion_triggered_shadow+shadow_eval_post_verify | SHADOW_AUTO — auto-eval all regions, not output-eligible |
| qwen3-max-thinking | openrouter | TOKEN | GENERATOR | SHADOW_AUTO |  | MN+MT+MB | completion_triggered_shadow+shadow_eval_post_verify | SHADOW_AUTO V17.19.0 — Alibaba flagship reasoning |
| qwen3.6-plus | openrouter | TOKEN | GENERATOR | SHADOW_AUTO |  | MN+MT+MB | completion_triggered_shadow+shadow_eval_post_verify | SHADOW_AUTO V20.3.32 — owner re-added Qwen3.6 Plus via OpenRouter with PHASE-FIRST contract cohort; old 2026-04-15 rows  |
