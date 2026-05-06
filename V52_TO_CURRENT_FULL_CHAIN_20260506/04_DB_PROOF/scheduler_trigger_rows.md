# Scheduler trigger rows

| log_time | log_level | region | job_name | date_str | message |
| --- | --- | --- | --- | --- | --- |
| 2026-05-05 00:56:30 | INFO | MN | shadow_catchup | 2026-05-05 | 🔄 [SHADOW_CATCH_UP] [MN] Incomplete shadow eval detected: 10/13 models. Recovering 3 missing models... |
| 2026-05-05 00:56:30 | WARNING | MN | shadow_eval | 2026-05-05 | [SHADOW_PREFLIGHT] ⚠️ checked=13 failures=['gemma-4-31b:key_missing:openrouter'] warnings=['gemini-3.1-pro:db_env_drift:google:selected_db', 'gemini-3-flash:db_env_drift:google:selected_db'] |
| 2026-05-05 00:56:30 | INFO | MN | shadow_eval | 2026-05-05 | 🔍 === Shadow Auto-Eval Start (2026-05-05) === models=['glm-5.1', 'grok-4.20-multi-agent', 'qwen3-coder', 'kimi-k2.5', 'qwen3-max-thinking', 'gpt-oss-120b', 'gpt-5.5', 'deepseek-v4-pro', 'deepseek-v4-flash', 'qwen3.6-plus', 'gemini-3.1-pro', 'gemini-3-flash', 'gemma-4-31b'] regions=['MN'] trigger_source=startup_shadow_catchup |
| 2026-05-05 00:56:30 | INFO | MN | shadow_eval | 2026-05-05 |   📦 [SHADOW_CONTEXT] [MN] source_data keys=['MB', 'MT', 'MN'] total_stations=6 |
| 2026-05-05 00:56:30 | INFO | MN | shadow_eval | 2026-05-05 |   🔄 [SHADOW_EVAL_SEQUENTIAL] [MN] model 1/13: glm-5.1 — starting... |
| 2026-05-05 01:00:58 | INFO | MN | shadow_catchup | 2026-05-05 | 🔄 [SHADOW_CATCH_UP] [MN] Incomplete shadow eval detected: 10/13 models. Recovering 3 missing models... |
| 2026-05-05 01:00:59 | WARNING | MN | shadow_eval | 2026-05-05 | [SHADOW_PREFLIGHT] ⚠️ checked=13 failures=['gemma-4-31b:key_missing:openrouter'] warnings=['gemini-3.1-pro:db_env_drift:google:selected_db', 'gemini-3-flash:db_env_drift:google:selected_db'] |
| 2026-05-05 01:00:59 | INFO | MN | shadow_eval | 2026-05-05 | 🔍 === Shadow Auto-Eval Start (2026-05-05) === models=['glm-5.1', 'grok-4.20-multi-agent', 'qwen3-coder', 'kimi-k2.5', 'qwen3-max-thinking', 'gpt-oss-120b', 'gpt-5.5', 'deepseek-v4-pro', 'deepseek-v4-flash', 'qwen3.6-plus', 'gemini-3.1-pro', 'gemini-3-flash', 'gemma-4-31b'] regions=['MN'] trigger_source=startup_shadow_catchup |
| 2026-05-05 01:00:59 | INFO | MN | shadow_eval | 2026-05-05 |   📦 [SHADOW_CONTEXT] [MN] source_data keys=['MB', 'MT', 'MN'] total_stations=6 |
| 2026-05-05 01:00:59 | INFO | MN | shadow_eval | 2026-05-05 |   🔄 [SHADOW_EVAL_SEQUENTIAL] [MN] model 1/13: glm-5.1 — starting... |
| 2026-05-05 01:07:24 | INFO | MN | shadow_eval | 2026-05-05 |   ✅ [MN] glm-5.1: ['56', '13'] (str=5.0, 385.6s) [shadow_auto_eval] |
| 2026-05-05 01:07:24 | INFO | MN | shadow_eval | 2026-05-05 |   🔄 [SHADOW_EVAL_SEQUENTIAL] [MN] model 2/13: grok-4.20-multi-agent — starting... |
| 2026-05-05 01:07:35 | INFO | MN | shadow_eval | 2026-05-05 |   ✅ [MN] grok-4.20-multi-agent: ['52', '41'] (str=8.0, 10.5s) [shadow_auto_eval] |
| 2026-05-05 01:07:35 | INFO | MN | shadow_eval | 2026-05-05 |   🔄 [SHADOW_EVAL_SEQUENTIAL] [MN] model 3/13: qwen3-coder — starting... |
| 2026-05-05 01:07:45 | INFO | MN | shadow_eval | 2026-05-05 |   ✅ [MN] qwen3-coder: ['52', '41'] (str=8.5, 10.7s) [shadow_auto_eval] |
| 2026-05-05 01:07:45 | INFO | MN | shadow_eval | 2026-05-05 |   🔄 [SHADOW_EVAL_SEQUENTIAL] [MN] model 4/13: kimi-k2.5 — starting... |
| 2026-05-05 01:08:56 | INFO | MN | shadow_eval | 2026-05-05 |   ✅ [MN] kimi-k2.5: ['56', '26'] (str=7.5, 70.5s) [shadow_auto_eval] |
| 2026-05-05 01:08:56 | INFO | MN | shadow_eval | 2026-05-05 |   🔄 [SHADOW_EVAL_SEQUENTIAL] [MN] model 5/13: qwen3-max-thinking — starting... |
| 2026-05-05 01:09:21 | INFO | MN | shadow_eval | 2026-05-05 |   ✅ [MN] qwen3-max-thinking: ['13', '24'] (str=6.5, 25.2s) [shadow_auto_eval] |
| 2026-05-05 01:09:21 | INFO | MN | shadow_eval | 2026-05-05 |   🔄 [SHADOW_EVAL_SEQUENTIAL] [MN] model 6/13: gpt-oss-120b — starting... |
| 2026-05-05 01:09:38 | INFO | MN | shadow_eval | 2026-05-05 |   ✅ [MN] gpt-oss-120b: ['52', '41'] (str=0.0, 16.2s) [shadow_auto_eval] |
| 2026-05-05 01:09:38 | INFO | MN | shadow_eval | 2026-05-05 |   🔄 [SHADOW_EVAL_SEQUENTIAL] [MN] model 7/13: gpt-5.5 — starting... |
| 2026-05-05 01:11:04 | INFO | MN | shadow_eval | 2026-05-05 |   ✅ [MN] gpt-5.5: ['63', '52'] (str=7.5, 86.5s) [shadow_auto_eval] |
| 2026-05-05 01:11:04 | INFO | MN | shadow_eval | 2026-05-05 |   🔄 [SHADOW_EVAL_SEQUENTIAL] [MN] model 8/13: deepseek-v4-pro — starting... |
| 2026-05-05 01:12:08 | INFO | MN | shadow_eval | 2026-05-05 |   ✅ [MN] deepseek-v4-pro: ['52', '56'] (str=8.0, 63.9s) [shadow_auto_eval] |
| 2026-05-05 01:12:08 | INFO | MN | shadow_eval | 2026-05-05 |   🔄 [SHADOW_EVAL_SEQUENTIAL] [MN] model 9/13: deepseek-v4-flash — starting... |
| 2026-05-05 01:12:30 | INFO | MN | shadow_eval | 2026-05-05 |   ✅ [MN] deepseek-v4-flash: ['52', '41'] (str=7.5, 22.0s) [shadow_auto_eval] |
| 2026-05-05 01:12:30 | INFO | MN | shadow_eval | 2026-05-05 |   🔄 [SHADOW_EVAL_SEQUENTIAL] [MN] model 10/13: qwen3.6-plus — starting... |
| 2026-05-05 01:14:34 | INFO | MN | shadow_eval | 2026-05-05 |   ✅ [MN] qwen3.6-plus: ['52', '13'] (str=6.5, 123.5s) [shadow_auto_eval] |
| 2026-05-05 01:14:34 | INFO | MN | shadow_eval | 2026-05-05 |   🔄 [SHADOW_EVAL_SEQUENTIAL] [MN] model 11/13: gemini-3.1-pro — starting... |
| 2026-05-05 01:15:25 | INFO | MN | shadow_eval | 2026-05-05 |   ✅ [MN] gemini-3.1-pro: ['56', '13'] (str=7.5, 51.6s) [shadow_auto_eval] |
| 2026-05-05 01:15:25 | INFO | MN | shadow_eval | 2026-05-05 |   🔄 [SHADOW_EVAL_SEQUENTIAL] [MN] model 12/13: gemini-3-flash — starting... |
| 2026-05-05 01:15:46 | INFO | MN | shadow_eval | 2026-05-05 |   ✅ [MN] gemini-3-flash: ['13', '52'] (str=7.0, 20.6s) [shadow_auto_eval] |
| 2026-05-05 01:15:46 | INFO | MN | shadow_eval | 2026-05-05 |   🔄 [SHADOW_EVAL_SEQUENTIAL] [MN] model 13/13: gemma-4-31b — starting... |
| 2026-05-05 01:15:46 | WARNING | MN | shadow_eval | 2026-05-05 |   ⚠️ [MN] gemma-4-31b: no API key — skip |
| 2026-05-05 01:15:46 | INFO | MN | shadow_eval | 2026-05-05 | [SHADOW_SUMMARY] MN 2026-05-05: success=12 error=1 persisted=12 missing_rows=['gemma-4-31b'] empty_rows=[] |
| 2026-05-05 01:15:46 | INFO | MN | shadow_eval | 2026-05-05 | 🔍 Shadow Auto-Eval Done (startup_shadow_catchup): regions=['MN'] |
| 2026-05-05 09:42:00 | INFO | MT | shadow_eval | 2026-05-05 | ⏭️ [SHADOW_SKIP_FALLBACK] MT: fallback path skipped main predict (ai_chain already has 5 rows). Shadow trigger deferred to ai_chain path. |
| 2026-05-05 09:43:28 | INFO | MT | shadow_rerank | 2026-05-05 | 🔀 [SHADOW_RERANK] MT: original=['30', '44'] → reranked=['30', '44'] (scores=[0.9709, 0.9686], bt_changed=False, latency=1232ms) |
| 2026-05-05 09:43:28 | WARNING | MT | shadow_eval | 2026-05-05 | [SHADOW_PREFLIGHT] ⚠️ checked=13 failures=['gemma-4-31b:key_missing:openrouter'] warnings=['gemini-3.1-pro:db_env_drift:google:selected_db', 'gemini-3-flash:db_env_drift:google:selected_db'] |
| 2026-05-05 09:43:28 | INFO | MT | shadow_eval | 2026-05-05 | 🔍 === Shadow Auto-Eval Start (2026-05-05) === models=['glm-5.1', 'grok-4.20-multi-agent', 'qwen3-coder', 'kimi-k2.5', 'qwen3-max-thinking', 'gpt-oss-120b', 'gpt-5.5', 'deepseek-v4-pro', 'deepseek-v4-flash', 'qwen3.6-plus', 'gemini-3.1-pro', 'gemini-3-flash', 'gemma-4-31b'] regions=['MT'] trigger_source=ai_chain |
| 2026-05-05 09:43:28 | INFO | MT | shadow_eval | 2026-05-05 |   📦 [SHADOW_CONTEXT] [MT] source_data keys=['MT_D1', 'MB_D1', 'MN_D1', 'MN'] total_stations=9 |
| 2026-05-05 09:43:28 | INFO | MT | shadow_eval | 2026-05-05 |   🔄 [SHADOW_EVAL_SEQUENTIAL] [MT] model 1/13: glm-5.1 — starting... |
| 2026-05-05 09:50:57 | INFO | MT | shadow_eval | 2026-05-05 |   ✅ [MT] glm-5.1: ['14', '37'] (str=6.0, 449.0s) [shadow_auto_eval] |
| 2026-05-05 09:50:57 | INFO | MT | shadow_eval | 2026-05-05 |   🔄 [SHADOW_EVAL_SEQUENTIAL] [MT] model 2/13: grok-4.20-multi-agent — starting... |
| 2026-05-05 09:51:09 | INFO | MT | shadow_eval | 2026-05-05 |   ✅ [MT] grok-4.20-multi-agent: ['52', '46'] (str=7.2, 11.7s) [shadow_auto_eval] |
| 2026-05-05 09:51:09 | INFO | MT | shadow_eval | 2026-05-05 |   🔄 [SHADOW_EVAL_SEQUENTIAL] [MT] model 3/13: qwen3-coder — starting... |
| 2026-05-05 09:51:19 | INFO | MT | shadow_eval | 2026-05-05 |   ✅ [MT] qwen3-coder: ['52', '46'] (str=7.1, 9.9s) [shadow_auto_eval] |
| 2026-05-05 09:51:19 | INFO | MT | shadow_eval | 2026-05-05 |   🔄 [SHADOW_EVAL_SEQUENTIAL] [MT] model 4/13: kimi-k2.5 — starting... |
| 2026-05-05 09:51:55 | INFO | MT | shadow_eval | 2026-05-05 |   ✅ [MT] kimi-k2.5: ['52'] (str=6.8, 36.0s) [shadow_auto_eval] |
| 2026-05-05 09:51:55 | INFO | MT | shadow_eval | 2026-05-05 |   🔄 [SHADOW_EVAL_SEQUENTIAL] [MT] model 5/13: qwen3-max-thinking — starting... |
| 2026-05-05 09:52:22 | INFO | MT | shadow_eval | 2026-05-05 |   ✅ [MT] qwen3-max-thinking: ['37', '13'] (str=7.2, 27.7s) [shadow_auto_eval] |
| 2026-05-05 09:52:22 | INFO | MT | shadow_eval | 2026-05-05 |   🔄 [SHADOW_EVAL_SEQUENTIAL] [MT] model 6/13: gpt-oss-120b — starting... |
| 2026-05-05 09:52:40 | INFO | MT | shadow_eval | 2026-05-05 |   ✅ [MT] gpt-oss-120b: ['52', '46'] (str=0.0, 18.0s) [shadow_auto_eval] |
| 2026-05-05 09:52:41 | INFO | MT | shadow_eval | 2026-05-05 |   🔄 [SHADOW_EVAL_SEQUENTIAL] [MT] model 7/13: gpt-5.5 — starting... |
| 2026-05-05 09:53:42 | INFO | MT | shadow_eval | 2026-05-05 |   ✅ [MT] gpt-5.5: ['52', '79'] (str=7.1, 61.3s) [shadow_auto_eval] |
| 2026-05-05 09:53:42 | INFO | MT | shadow_eval | 2026-05-05 |   🔄 [SHADOW_EVAL_SEQUENTIAL] [MT] model 8/13: deepseek-v4-pro — starting... |
| 2026-05-05 09:55:57 | INFO | MT | shadow_eval | 2026-05-05 |   ✅ [MT] deepseek-v4-pro: ['37', '03'] (str=7.0, 134.8s) [shadow_auto_eval] |
| 2026-05-05 09:55:57 | INFO | MT | shadow_eval | 2026-05-05 |   🔄 [SHADOW_EVAL_SEQUENTIAL] [MT] model 9/13: deepseek-v4-flash — starting... |
| 2026-05-05 09:56:31 | INFO | MT | shadow_eval | 2026-05-05 |   ✅ [MT] deepseek-v4-flash: ['79'] (str=6.5, 34.8s) [shadow_auto_eval] |
| 2026-05-05 09:56:32 | INFO | MT | shadow_eval | 2026-05-05 |   🔄 [SHADOW_EVAL_SEQUENTIAL] [MT] model 10/13: qwen3.6-plus — starting... |
| 2026-05-05 09:58:38 | INFO | MT | shadow_eval | 2026-05-05 |   ✅ [MT] qwen3.6-plus: ['14', '37'] (str=7.0, 126.5s) [shadow_auto_eval] |
| 2026-05-05 09:58:38 | INFO | MT | shadow_eval | 2026-05-05 |   🔄 [SHADOW_EVAL_SEQUENTIAL] [MT] model 11/13: gemini-3.1-pro — starting... |
| 2026-05-05 09:59:31 | INFO | MT | shadow_eval | 2026-05-05 |   ✅ [MT] gemini-3.1-pro: ['67', '14'] (str=7.5, 53.2s) [shadow_auto_eval] |
| 2026-05-05 09:59:31 | INFO | MT | shadow_eval | 2026-05-05 |   🔄 [SHADOW_EVAL_SEQUENTIAL] [MT] model 12/13: gemini-3-flash — starting... |
| 2026-05-05 09:59:55 | INFO | MT | shadow_eval | 2026-05-05 |   ✅ [MT] gemini-3-flash: ['13', '37'] (str=7.5, 23.9s) [shadow_auto_eval] |
| 2026-05-05 09:59:55 | INFO | MT | shadow_eval | 2026-05-05 |   🔄 [SHADOW_EVAL_SEQUENTIAL] [MT] model 13/13: gemma-4-31b — starting... |
| 2026-05-05 09:59:55 | WARNING | MT | shadow_eval | 2026-05-05 |   ⚠️ [MT] gemma-4-31b: no API key — skip |
| 2026-05-05 09:59:55 | INFO | MT | shadow_eval | 2026-05-05 | [SHADOW_SUMMARY] MT 2026-05-05: success=12 error=1 persisted=12 missing_rows=['gemma-4-31b'] empty_rows=[] |
| 2026-05-05 09:59:55 | INFO | MT | shadow_eval | 2026-05-05 | 🔍 Shadow Auto-Eval Done (ai_chain): regions=['MT'] |
| 2026-05-05 10:39:20 | INFO | MB | shadow_rerank | 2026-05-05 | 🔀 [SHADOW_RERANK] MB: original=['41', '36'] → reranked=['41', '36'] (scores=[0.9702, 0.9658], bt_changed=False, latency=2677ms) |
| 2026-05-05 10:39:20 | WARNING | MB | shadow_eval | 2026-05-05 | [SHADOW_PREFLIGHT] ⚠️ checked=13 failures=['gemma-4-31b:key_missing:openrouter'] warnings=['gemini-3.1-pro:db_env_drift:google:selected_db', 'gemini-3-flash:db_env_drift:google:selected_db'] |
| 2026-05-05 10:39:20 | INFO | MB | shadow_eval | 2026-05-05 | 🔍 === Shadow Auto-Eval Start (2026-05-05) === models=['glm-5.1', 'grok-4.20-multi-agent', 'qwen3-coder', 'kimi-k2.5', 'qwen3-max-thinking', 'gpt-oss-120b', 'gpt-5.5', 'deepseek-v4-pro', 'deepseek-v4-flash', 'qwen3.6-plus', 'gemini-3.1-pro', 'gemini-3-flash', 'gemma-4-31b'] regions=['MB'] trigger_source=ai_chain |
| 2026-05-05 10:39:20 | INFO | MB | shadow_eval | 2026-05-05 |   📦 [SHADOW_CONTEXT] [MB] source_data keys=['MT_D1', 'MB_D1', 'MN_D1', 'MN', 'MT'] total_stations=11 |
| 2026-05-05 10:39:20 | INFO | MB | shadow_eval | 2026-05-05 |   🔄 [SHADOW_EVAL_SEQUENTIAL] [MB] model 1/13: glm-5.1 — starting... |
| 2026-05-05 10:42:00 | INFO | MB | shadow_eval | 2026-05-05 | ⏭️ [SHADOW_SKIP_FALLBACK] MB: fallback path skipped main predict (ai_chain already has 8 rows). Shadow trigger deferred to ai_chain path. |
| 2026-05-05 10:43:48 | INFO | MB | shadow_eval | 2026-05-05 |   ✅ [MB] glm-5.1: ['41', '14'] (str=5.0, 267.6s) [shadow_auto_eval] |
| 2026-05-05 10:43:48 | INFO | MB | shadow_eval | 2026-05-05 |   🔄 [SHADOW_EVAL_SEQUENTIAL] [MB] model 2/13: grok-4.20-multi-agent — starting... |
| 2026-05-05 10:43:59 | INFO | MB | shadow_eval | 2026-05-05 |   ✅ [MB] grok-4.20-multi-agent: ['41', '14'] (str=6.0, 11.1s) [shadow_auto_eval] |
| 2026-05-05 10:43:59 | INFO | MB | shadow_eval | 2026-05-05 |   🔄 [SHADOW_EVAL_SEQUENTIAL] [MB] model 3/13: qwen3-coder — starting... |
| 2026-05-05 10:44:25 | INFO | MB | shadow_eval | 2026-05-05 |   ✅ [MB] qwen3-coder: ['41', '98'] (str=6.0, 25.9s) [shadow_auto_eval] |
| 2026-05-05 10:44:25 | INFO | MB | shadow_eval | 2026-05-05 |   🔄 [SHADOW_EVAL_SEQUENTIAL] [MB] model 4/13: kimi-k2.5 — starting... |
| 2026-05-05 10:46:57 | INFO | MB | shadow_eval | 2026-05-05 |   ✅ [MB] kimi-k2.5: ['41', '91'] (str=6.0, 152.1s) [shadow_auto_eval] |
| 2026-05-05 10:46:57 | INFO | MB | shadow_eval | 2026-05-05 |   🔄 [SHADOW_EVAL_SEQUENTIAL] [MB] model 5/13: qwen3-max-thinking — starting... |
| 2026-05-05 10:47:26 | INFO | MB | shadow_eval | 2026-05-05 |   ✅ [MB] qwen3-max-thinking: ['41', '98'] (str=6.0, 28.9s) [shadow_auto_eval] |
| 2026-05-05 10:47:26 | INFO | MB | shadow_eval | 2026-05-05 |   🔄 [SHADOW_EVAL_SEQUENTIAL] [MB] model 6/13: gpt-oss-120b — starting... |
| 2026-05-05 10:49:16 | INFO | MB | shadow_eval | 2026-05-05 |   ✅ [MB] gpt-oss-120b: ['14'] (str=0.0, 109.2s) [shadow_auto_eval] |
| 2026-05-05 10:49:16 | INFO | MB | shadow_eval | 2026-05-05 |   🔄 [SHADOW_EVAL_SEQUENTIAL] [MB] model 7/13: gpt-5.5 — starting... |
| 2026-05-05 10:50:25 | INFO | MB | shadow_eval | 2026-05-05 |   ✅ [MB] gpt-5.5: ['66', '09'] (str=6.0, 69.1s) [shadow_auto_eval] |
| 2026-05-05 10:50:25 | INFO | MB | shadow_eval | 2026-05-05 |   🔄 [SHADOW_EVAL_SEQUENTIAL] [MB] model 8/13: deepseek-v4-pro — starting... |
| 2026-05-05 10:53:06 | INFO | MB | shadow_eval | 2026-05-05 |   ✅ [MB] deepseek-v4-pro: ['09', '14'] (str=6.0, 161.2s) [shadow_auto_eval] |
| 2026-05-05 10:53:06 | INFO | MB | shadow_eval | 2026-05-05 |   🔄 [SHADOW_EVAL_SEQUENTIAL] [MB] model 9/13: deepseek-v4-flash — starting... |
| 2026-05-05 10:53:33 | INFO | MB | shadow_eval | 2026-05-05 |   ✅ [MB] deepseek-v4-flash: ['09', '91'] (str=6.0, 27.4s) [shadow_auto_eval] |
| 2026-05-05 10:53:33 | INFO | MB | shadow_eval | 2026-05-05 |   🔄 [SHADOW_EVAL_SEQUENTIAL] [MB] model 10/13: qwen3.6-plus — starting... |
| 2026-05-05 10:55:33 | INFO | MB | shadow_eval | 2026-05-05 |   ✅ [MB] qwen3.6-plus: ['91', '14'] (str=6.0, 119.7s) [shadow_auto_eval] |
| 2026-05-05 10:55:33 | INFO | MB | shadow_eval | 2026-05-05 |   🔄 [SHADOW_EVAL_SEQUENTIAL] [MB] model 11/13: gemini-3.1-pro — starting... |
| 2026-05-05 10:56:21 | INFO | MB | shadow_eval | 2026-05-05 |   ✅ [MB] gemini-3.1-pro: ['90', '14'] (str=6.0, 47.5s) [shadow_auto_eval] |
| 2026-05-05 10:56:21 | INFO | MB | shadow_eval | 2026-05-05 |   🔄 [SHADOW_EVAL_SEQUENTIAL] [MB] model 12/13: gemini-3-flash — starting... |
| 2026-05-05 10:56:51 | INFO | MB | shadow_eval | 2026-05-05 |   ✅ [MB] gemini-3-flash: ['91', '14'] (str=6.0, 30.1s) [shadow_auto_eval] |
| 2026-05-05 10:56:51 | INFO | MB | shadow_eval | 2026-05-05 |   🔄 [SHADOW_EVAL_SEQUENTIAL] [MB] model 13/13: gemma-4-31b — starting... |
| 2026-05-05 10:56:51 | WARNING | MB | shadow_eval | 2026-05-05 |   ⚠️ [MB] gemma-4-31b: no API key — skip |
| 2026-05-05 10:56:51 | INFO | MB | shadow_eval | 2026-05-05 | [SHADOW_SUMMARY] MB 2026-05-05: success=12 error=1 persisted=12 missing_rows=['gemma-4-31b'] empty_rows=[] |
| 2026-05-05 10:56:51 | INFO | MB | shadow_eval | 2026-05-05 | 🔍 Shadow Auto-Eval Done (ai_chain): regions=['MB'] |
| 2026-05-05 13:30:37 | INFO | MN | shadow_catchup | 2026-05-05 | 🔄 [SHADOW_CATCH_UP] [MN] Incomplete shadow eval detected: 12/13 models. Recovering 1 missing models... |
| 2026-05-05 13:30:37 | INFO | MN | shadow_eval | 2026-05-05 | [SHADOW_PREFLIGHT] ✅ checked=13 warnings=['gemini-3.1-pro:db_env_drift:google:selected_db', 'gemini-3-flash:db_env_drift:google:selected_db', 'gemma-4-31b:db_env_drift:google:selected_db'] |
| 2026-05-05 13:30:37 | INFO | MN | shadow_eval | 2026-05-05 | 🔍 === Shadow Auto-Eval Start (2026-05-05) === models=['glm-5.1', 'grok-4.20-multi-agent', 'qwen3-coder', 'kimi-k2.5', 'qwen3-max-thinking', 'gpt-oss-120b', 'gpt-5.5', 'deepseek-v4-pro', 'deepseek-v4-flash', 'qwen3.6-plus', 'gemini-3.1-pro', 'gemini-3-flash', 'gemma-4-31b'] regions=['MN'] trigger_source=startup_shadow_catchup |
| 2026-05-05 13:30:37 | INFO | MN | shadow_eval | 2026-05-05 |   📦 [SHADOW_CONTEXT] [MN] source_data keys=['MB', 'MT', 'MN'] total_stations=6 |
| 2026-05-05 13:30:37 | INFO | MN | shadow_eval | 2026-05-05 |   🔄 [SHADOW_EVAL_SEQUENTIAL] [MN] model 1/13: glm-5.1 — starting... |
| 2026-05-05 13:32:20 | INFO | MN | du_doan_test_mb | 2026-05-04 | [DU-DOAN-TEST-MB] runner_start mode=POST_CLOSEOUT_DIAGNOSTIC_FULL_25 run_label=du_doan_test_v52_5_6_MN_post_closeout_diagnostic_full_25_2026-05-04 |
| 2026-05-05 13:32:22 | INFO | MN | du_doan_test_mb | 2026-05-04 | [DU-DOAN-TEST-MB] runner_finish mode=POST_CLOSEOUT_DIAGNOSTIC_FULL_25 run_label=du_doan_test_v52_5_6_MN_post_closeout_diagnostic_full_25_2026-05-04 official_tables_touched=false |
| 2026-05-05 13:32:23 | INFO | MT | du_doan_test_mb | 2026-05-04 | [DU-DOAN-TEST-MB] runner_start mode=POST_CLOSEOUT_DIAGNOSTIC_FULL_25 run_label=du_doan_test_v52_5_6_MT_post_closeout_diagnostic_full_25_2026-05-04 |
| 2026-05-05 13:32:25 | INFO | MT | du_doan_test_mb | 2026-05-04 | [DU-DOAN-TEST-MB] runner_finish mode=POST_CLOSEOUT_DIAGNOSTIC_FULL_25 run_label=du_doan_test_v52_5_6_MT_post_closeout_diagnostic_full_25_2026-05-04 official_tables_touched=false |
| 2026-05-05 13:32:25 | INFO | MB | du_doan_test_mb | 2026-05-04 | [DU-DOAN-TEST-MB] runner_start mode=POST_CLOSEOUT_DIAGNOSTIC_FULL_25 run_label=du_doan_test_v52_5_6_MB_post_closeout_diagnostic_full_25_2026-05-04 |
| 2026-05-05 13:32:28 | INFO | MB | du_doan_test_mb | 2026-05-04 | [DU-DOAN-TEST-MB] runner_finish mode=POST_CLOSEOUT_DIAGNOSTIC_FULL_25 run_label=du_doan_test_v52_5_6_MB_post_closeout_diagnostic_full_25_2026-05-04 official_tables_touched=false |
| 2026-05-05 13:32:29 | INFO | MN | du_doan_test_mb | 2026-05-05 | [DU-DOAN-TEST-MB] runner_start mode=POST_CLOSEOUT_DIAGNOSTIC_FULL_25 run_label=du_doan_test_v52_5_6_MN_post_closeout_diagnostic_full_25_2026-05-05 |
| 2026-05-05 13:32:31 | INFO | MN | du_doan_test_mb | 2026-05-05 | [DU-DOAN-TEST-MB] runner_finish mode=POST_CLOSEOUT_DIAGNOSTIC_FULL_25 run_label=du_doan_test_v52_5_6_MN_post_closeout_diagnostic_full_25_2026-05-05 official_tables_touched=false |
| 2026-05-05 13:32:31 | INFO | MT | du_doan_test_mb | 2026-05-05 | [DU-DOAN-TEST-MB] runner_start mode=POST_CLOSEOUT_DIAGNOSTIC_FULL_25 run_label=du_doan_test_v52_5_6_MT_post_closeout_diagnostic_full_25_2026-05-05 |
| 2026-05-05 13:32:33 | INFO | MT | du_doan_test_mb | 2026-05-05 | [DU-DOAN-TEST-MB] runner_finish mode=POST_CLOSEOUT_DIAGNOSTIC_FULL_25 run_label=du_doan_test_v52_5_6_MT_post_closeout_diagnostic_full_25_2026-05-05 official_tables_touched=false |
| 2026-05-05 13:32:34 | INFO | MB | du_doan_test_mb | 2026-05-05 | [DU-DOAN-TEST-MB] runner_start mode=POST_CLOSEOUT_DIAGNOSTIC_FULL_25 run_label=du_doan_test_v52_5_6_MB_post_closeout_diagnostic_full_25_2026-05-05 |
| 2026-05-05 13:32:37 | INFO | MB | du_doan_test_mb | 2026-05-05 | [DU-DOAN-TEST-MB] runner_finish mode=POST_CLOSEOUT_DIAGNOSTIC_FULL_25 run_label=du_doan_test_v52_5_6_MB_post_closeout_diagnostic_full_25_2026-05-05 official_tables_touched=false |
| 2026-05-05 13:36:43 | INFO | MN | shadow_eval | 2026-05-05 |   ✅ [MN] glm-5.1: ['56', '05'] (str=7.5, 365.9s) [shadow_auto_eval] |
| 2026-05-05 13:36:43 | INFO | MN | shadow_eval | 2026-05-05 |   🔄 [SHADOW_EVAL_SEQUENTIAL] [MN] model 2/13: grok-4.20-multi-agent — starting... |
| 2026-05-05 13:36:56 | INFO | MN | shadow_eval | 2026-05-05 |   ✅ [MN] grok-4.20-multi-agent: ['52', '41'] (str=7.5, 13.3s) [shadow_auto_eval] |
| 2026-05-05 13:36:56 | INFO | MN | shadow_eval | 2026-05-05 |   🔄 [SHADOW_EVAL_SEQUENTIAL] [MN] model 3/13: qwen3-coder — starting... |
| 2026-05-05 13:37:08 | INFO | MN | shadow_eval | 2026-05-05 |   ✅ [MN] qwen3-coder: ['52', '41'] (str=8.5, 11.8s) [shadow_auto_eval] |
| 2026-05-05 13:37:08 | INFO | MN | shadow_eval | 2026-05-05 |   🔄 [SHADOW_EVAL_SEQUENTIAL] [MN] model 4/13: kimi-k2.5 — starting... |
| 2026-05-05 13:37:46 | INFO | MN | shadow_eval | 2026-05-05 |   ✅ [MN] kimi-k2.5: ['52', '24'] (str=7.5, 37.6s) [shadow_auto_eval] |
| 2026-05-05 13:37:46 | INFO | MN | shadow_eval | 2026-05-05 |   🔄 [SHADOW_EVAL_SEQUENTIAL] [MN] model 5/13: qwen3-max-thinking — starting... |
| 2026-05-05 13:38:10 | INFO | MN | shadow_eval | 2026-05-05 |   ✅ [MN] qwen3-max-thinking: ['24', '13'] (str=7.0, 24.5s) [shadow_auto_eval] |
| 2026-05-05 13:38:10 | INFO | MN | shadow_eval | 2026-05-05 |   🔄 [SHADOW_EVAL_SEQUENTIAL] [MN] model 6/13: gpt-oss-120b — starting... |
| 2026-05-05 13:38:34 | INFO | MN | shadow_eval | 2026-05-05 |   ✅ [MN] gpt-oss-120b: ['41', '52'] (str=0.0, 23.5s) [shadow_auto_eval] |
| 2026-05-05 13:38:34 | INFO | MN | shadow_eval | 2026-05-05 |   🔄 [SHADOW_EVAL_SEQUENTIAL] [MN] model 7/13: gpt-5.5 — starting... |
| 2026-05-05 13:39:53 | INFO | MN | shadow_eval | 2026-05-05 |   ✅ [MN] gpt-5.5: ['52', '63'] (str=8.0, 79.5s) [shadow_auto_eval] |
| 2026-05-05 13:39:53 | INFO | MN | shadow_eval | 2026-05-05 |   🔄 [SHADOW_EVAL_SEQUENTIAL] [MN] model 8/13: deepseek-v4-pro — starting... |
| 2026-05-05 13:41:07 | INFO | MN | shadow_eval | 2026-05-05 |   ✅ [MN] deepseek-v4-pro: ['63', '56'] (str=7.0, 73.9s) [shadow_auto_eval] |
| 2026-05-05 13:41:07 | INFO | MN | shadow_eval | 2026-05-05 |   🔄 [SHADOW_EVAL_SEQUENTIAL] [MN] model 9/13: deepseek-v4-flash — starting... |
| 2026-05-05 13:41:39 | INFO | MN | shadow_eval | 2026-05-05 |   ✅ [MN] deepseek-v4-flash: ['63', '52'] (str=7.5, 31.7s) [shadow_auto_eval] |
| 2026-05-05 13:41:39 | INFO | MN | shadow_eval | 2026-05-05 |   🔄 [SHADOW_EVAL_SEQUENTIAL] [MN] model 10/13: qwen3.6-plus — starting... |
| 2026-05-05 13:43:46 | INFO | MN | shadow_eval | 2026-05-05 |   ✅ [MN] qwen3.6-plus: ['24', '41'] (str=7.5, 127.2s) [shadow_auto_eval] |
| 2026-05-05 13:43:46 | INFO | MN | shadow_eval | 2026-05-05 |   🔄 [SHADOW_EVAL_SEQUENTIAL] [MN] model 11/13: gemini-3.1-pro — starting... |
| 2026-05-05 13:44:37 | INFO | MN | shadow_eval | 2026-05-05 |   ✅ [MN] gemini-3.1-pro: ['13', '52'] (str=8.0, 50.5s) [shadow_auto_eval] |
| 2026-05-05 13:44:37 | INFO | MN | shadow_eval | 2026-05-05 |   🔄 [SHADOW_EVAL_SEQUENTIAL] [MN] model 12/13: gemini-3-flash — starting... |
| 2026-05-05 13:45:02 | INFO | MN | shadow_eval | 2026-05-05 |   ✅ [MN] gemini-3-flash: ['13', '63'] (str=8.0, 25.5s) [shadow_auto_eval] |
| 2026-05-05 13:45:02 | INFO | MN | shadow_eval | 2026-05-05 |   🔄 [SHADOW_EVAL_SEQUENTIAL] [MN] model 13/13: gemma-4-31b — starting... |
| 2026-05-05 13:47:30 | INFO | MN | shadow_eval | 2026-05-05 |   ✅ [MN] gemma-4-31b: ['13', '05'] (str=7.2, 148.3s) [shadow_auto_eval] |
| 2026-05-05 13:47:30 | INFO | MN | shadow_eval | 2026-05-05 | [SHADOW_SUMMARY] MN 2026-05-05: success=13 error=0 persisted=13 missing_rows=[] empty_rows=[] |
| 2026-05-05 13:47:30 | INFO | MN | shadow_eval | 2026-05-05 | 🔍 Shadow Auto-Eval Done (startup_shadow_catchup): regions=['MN'] |
| 2026-05-05 13:47:30 | INFO | MT | shadow_catchup | 2026-05-05 | 🔄 [SHADOW_CATCH_UP] [MT] Incomplete shadow eval detected: 12/13 models. Recovering 1 missing models... |
| 2026-05-05 13:47:31 | INFO | MT | shadow_eval | 2026-05-05 | [SHADOW_PREFLIGHT] ✅ checked=13 warnings=['gemini-3.1-pro:db_env_drift:google:selected_db', 'gemini-3-flash:db_env_drift:google:selected_db', 'gemma-4-31b:db_env_drift:google:selected_db'] |
| 2026-05-05 13:47:31 | INFO | MT | shadow_eval | 2026-05-05 | 🔍 === Shadow Auto-Eval Start (2026-05-05) === models=['glm-5.1', 'grok-4.20-multi-agent', 'qwen3-coder', 'kimi-k2.5', 'qwen3-max-thinking', 'gpt-oss-120b', 'gpt-5.5', 'deepseek-v4-pro', 'deepseek-v4-flash', 'qwen3.6-plus', 'gemini-3.1-pro', 'gemini-3-flash', 'gemma-4-31b'] regions=['MT'] trigger_source=startup_shadow_catchup |
| 2026-05-05 13:47:31 | INFO | MT | shadow_eval | 2026-05-05 |   📦 [SHADOW_CONTEXT] [MT] source_data keys=['MT_D1', 'MB_D1', 'MN_D1', 'MN'] total_stations=9 |
| 2026-05-05 13:47:31 | INFO | MT | shadow_eval | 2026-05-05 |   🔄 [SHADOW_EVAL_SEQUENTIAL] [MT] model 1/13: glm-5.1 — starting... |
| 2026-05-05 13:48:08 | WARNING | MT | shadow_eval | 2026-05-05 |   ❌ [MT] glm-5.1: Lỗi phân tích response JSON từ AI: Unterminated string starting at: line 10 column 30 (char 447) (37.9s) |
| 2026-05-05 13:48:08 | INFO | MT | shadow_eval | 2026-05-05 |   🔄 [SHADOW_EVAL_SEQUENTIAL] [MT] model 2/13: grok-4.20-multi-agent — starting... |
| 2026-05-05 13:48:21 | INFO | MT | shadow_eval | 2026-05-05 |   ✅ [MT] grok-4.20-multi-agent: ['52', '46'] (str=7.1, 12.9s) [shadow_auto_eval] |
| 2026-05-05 13:48:21 | INFO | MT | shadow_eval | 2026-05-05 |   🔄 [SHADOW_EVAL_SEQUENTIAL] [MT] model 3/13: qwen3-coder — starting... |
| 2026-05-05 13:48:33 | INFO | MT | shadow_eval | 2026-05-05 |   ✅ [MT] qwen3-coder: ['52', '46'] (str=8.2, 11.5s) [shadow_auto_eval] |
| 2026-05-05 13:48:33 | INFO | MT | shadow_eval | 2026-05-05 |   🔄 [SHADOW_EVAL_SEQUENTIAL] [MT] model 4/13: kimi-k2.5 — starting... |
| 2026-05-05 13:51:18 | WARNING | MT | shadow_eval | 2026-05-05 |   ❌ [MT] kimi-k2.5: ⚠️ Model kimi-k2.5: Trả về rỗng (finish_reason: None). Model có thể không hỗ trợ loại prompt này. (165.6s) |
| 2026-05-05 13:51:19 | INFO | MT | shadow_eval | 2026-05-05 |   🔄 [SHADOW_EVAL_SEQUENTIAL] [MT] model 5/13: qwen3-max-thinking — starting... |
| 2026-05-05 13:51:47 | INFO | MT | shadow_eval | 2026-05-05 |   ✅ [MT] qwen3-max-thinking: ['37', '13'] (str=7.2, 28.1s) [shadow_auto_eval] |
| 2026-05-05 13:51:47 | INFO | MT | shadow_eval | 2026-05-05 |   🔄 [SHADOW_EVAL_SEQUENTIAL] [MT] model 6/13: gpt-oss-120b — starting... |
| 2026-05-05 13:53:05 | INFO | MT | shadow_eval | 2026-05-05 |   ✅ [MT] gpt-oss-120b: ['46', '52'] (str=0.0, 78.3s) [shadow_auto_eval] |
| 2026-05-05 13:53:05 | INFO | MT | shadow_eval | 2026-05-05 |   🔄 [SHADOW_EVAL_SEQUENTIAL] [MT] model 7/13: gpt-5.5 — starting... |
| 2026-05-05 13:54:17 | INFO | MT | shadow_eval | 2026-05-05 |   ✅ [MT] gpt-5.5: ['67', '37'] (str=7.0, 71.7s) [shadow_auto_eval] |
| 2026-05-05 13:54:17 | INFO | MT | shadow_eval | 2026-05-05 |   🔄 [SHADOW_EVAL_SEQUENTIAL] [MT] model 8/13: deepseek-v4-pro — starting... |
| 2026-05-05 13:56:30 | INFO | MT | shadow_eval | 2026-05-05 |   ✅ [MT] deepseek-v4-pro: ['67', '14'] (str=5.5, 133.1s) [shadow_auto_eval] |
| 2026-05-05 13:56:30 | INFO | MT | shadow_eval | 2026-05-05 |   🔄 [SHADOW_EVAL_SEQUENTIAL] [MT] model 9/13: deepseek-v4-flash — starting... |
| 2026-05-05 13:56:53 | INFO | MT | shadow_eval | 2026-05-05 |   ✅ [MT] deepseek-v4-flash: ['67', '75'] (str=8.0, 23.5s) [shadow_auto_eval] |
| 2026-05-05 13:56:53 | INFO | MT | shadow_eval | 2026-05-05 |   🔄 [SHADOW_EVAL_SEQUENTIAL] [MT] model 10/13: qwen3.6-plus — starting... |
| 2026-05-05 13:59:27 | INFO | MT | shadow_eval | 2026-05-05 |   ✅ [MT] qwen3.6-plus: ['67', '37'] (str=6.5, 153.2s) [shadow_auto_eval] |
| 2026-05-05 13:59:27 | INFO | MT | shadow_eval | 2026-05-05 |   🔄 [SHADOW_EVAL_SEQUENTIAL] [MT] model 11/13: gemini-3.1-pro — starting... |
| 2026-05-05 14:00:17 | INFO | MT | shadow_eval | 2026-05-05 |   ✅ [MT] gemini-3.1-pro: ['67', '15'] (str=6.5, 50.2s) [shadow_auto_eval] |
| 2026-05-05 14:00:17 | INFO | MT | shadow_eval | 2026-05-05 |   🔄 [SHADOW_EVAL_SEQUENTIAL] [MT] model 12/13: gemini-3-flash — starting... |
| 2026-05-05 14:00:36 | INFO | MT | shadow_eval | 2026-05-05 |   ✅ [MT] gemini-3-flash: ['67', '13'] (str=8.0, 18.5s) [shadow_auto_eval] |
| 2026-05-05 14:00:36 | INFO | MT | shadow_eval | 2026-05-05 |   🔄 [SHADOW_EVAL_SEQUENTIAL] [MT] model 13/13: gemma-4-31b — starting... |
| 2026-05-05 14:02:45 | INFO | MT | shadow_eval | 2026-05-05 |   ✅ [MT] gemma-4-31b: ['37', '03'] (str=8.0, 129.1s) [shadow_auto_eval] |
| 2026-05-05 14:02:45 | INFO | MT | shadow_eval | 2026-05-05 | [SHADOW_SUMMARY] MT 2026-05-05: success=11 error=2 persisted=13 missing_rows=[] empty_rows=[] |
| 2026-05-05 14:02:45 | INFO | MT | shadow_eval | 2026-05-05 | 🔍 Shadow Auto-Eval Done (startup_shadow_catchup): regions=['MT'] |
| 2026-05-05 14:02:45 | INFO | MB | shadow_catchup | 2026-05-05 | 🔄 [SHADOW_CATCH_UP] [MB] Incomplete shadow eval detected: 12/13 models. Recovering 1 missing models... |
| 2026-05-05 14:02:45 | INFO | MB | shadow_eval | 2026-05-05 | [SHADOW_PREFLIGHT] ✅ checked=13 warnings=['gemini-3.1-pro:db_env_drift:google:selected_db', 'gemini-3-flash:db_env_drift:google:selected_db', 'gemma-4-31b:db_env_drift:google:selected_db'] |
| 2026-05-05 14:02:45 | INFO | MB | shadow_eval | 2026-05-05 | 🔍 === Shadow Auto-Eval Start (2026-05-05) === models=['glm-5.1', 'grok-4.20-multi-agent', 'qwen3-coder', 'kimi-k2.5', 'qwen3-max-thinking', 'gpt-oss-120b', 'gpt-5.5', 'deepseek-v4-pro', 'deepseek-v4-flash', 'qwen3.6-plus', 'gemini-3.1-pro', 'gemini-3-flash', 'gemma-4-31b'] regions=['MB'] trigger_source=startup_shadow_catchup |
| 2026-05-05 14:02:45 | INFO | MB | shadow_eval | 2026-05-05 |   📦 [SHADOW_CONTEXT] [MB] source_data keys=['MT_D1', 'MB_D1', 'MN_D1', 'MN', 'MT'] total_stations=11 |
| 2026-05-05 14:02:45 | INFO | MB | shadow_eval | 2026-05-05 |   🔄 [SHADOW_EVAL_SEQUENTIAL] [MB] model 1/13: glm-5.1 — starting... |
| 2026-05-05 14:04:38 | INFO | MB | shadow_eval | 2026-05-05 |   ✅ [MB] glm-5.1: ['41', '09'] (str=5.5, 113.4s) [shadow_auto_eval] |
| 2026-05-05 14:04:38 | INFO | MB | shadow_eval | 2026-05-05 |   🔄 [SHADOW_EVAL_SEQUENTIAL] [MB] model 2/13: grok-4.20-multi-agent — starting... |
| 2026-05-05 14:04:53 | INFO | MB | shadow_eval | 2026-05-05 |   ✅ [MB] grok-4.20-multi-agent: ['41', '14'] (str=6.0, 14.9s) [shadow_auto_eval] |
| 2026-05-05 14:04:53 | INFO | MB | shadow_eval | 2026-05-05 |   🔄 [SHADOW_EVAL_SEQUENTIAL] [MB] model 3/13: qwen3-coder — starting... |
| 2026-05-05 14:05:31 | INFO | MB | shadow_eval | 2026-05-05 |   ✅ [MB] qwen3-coder: ['91', '14'] (str=6.0, 37.9s) [shadow_auto_eval] |
| 2026-05-05 14:05:31 | INFO | MB | shadow_eval | 2026-05-05 |   🔄 [SHADOW_EVAL_SEQUENTIAL] [MB] model 4/13: kimi-k2.5 — starting... |
| 2026-05-05 14:06:12 | INFO | MB | shadow_eval | 2026-05-05 |   ✅ [MB] kimi-k2.5: ['41', '93'] (str=5.5, 40.5s) [shadow_auto_eval] |
| 2026-05-05 14:06:12 | INFO | MB | shadow_eval | 2026-05-05 |   🔄 [SHADOW_EVAL_SEQUENTIAL] [MB] model 5/13: qwen3-max-thinking — starting... |
| 2026-05-05 14:06:37 | INFO | MB | shadow_eval | 2026-05-05 |   ✅ [MB] qwen3-max-thinking: ['41', '14'] (str=6.0, 25.4s) [shadow_auto_eval] |
| 2026-05-05 14:06:37 | INFO | MB | shadow_eval | 2026-05-05 |   🔄 [SHADOW_EVAL_SEQUENTIAL] [MB] model 6/13: gpt-oss-120b — starting... |
| 2026-05-05 14:07:00 | INFO | MB | shadow_eval | 2026-05-05 |   ✅ [MB] gpt-oss-120b: ['09', '14'] (str=0.0, 23.1s) [shadow_auto_eval] |
| 2026-05-05 14:07:00 | INFO | MB | shadow_eval | 2026-05-05 |   🔄 [SHADOW_EVAL_SEQUENTIAL] [MB] model 7/13: gpt-5.5 — starting... |
| 2026-05-05 14:08:32 | INFO | MB | shadow_eval | 2026-05-05 |   ✅ [MB] gpt-5.5: ['66', '09'] (str=6.0, 92.1s) [shadow_auto_eval] |
| 2026-05-05 14:08:32 | INFO | MB | shadow_eval | 2026-05-05 |   🔄 [SHADOW_EVAL_SEQUENTIAL] [MB] model 8/13: deepseek-v4-pro — starting... |
| 2026-05-05 14:12:55 | INFO | MB | shadow_eval | 2026-05-05 |   ✅ [MB] deepseek-v4-pro: ['09', '14'] (str=6.0, 262.5s) [shadow_auto_eval] |
| 2026-05-05 14:12:55 | INFO | MB | shadow_eval | 2026-05-05 |   🔄 [SHADOW_EVAL_SEQUENTIAL] [MB] model 9/13: deepseek-v4-flash — starting... |
| 2026-05-05 14:13:23 | INFO | MB | shadow_eval | 2026-05-05 |   ✅ [MB] deepseek-v4-flash: ['09', '91'] (str=6.0, 27.7s) [shadow_auto_eval] |
| 2026-05-05 14:13:23 | INFO | MB | shadow_eval | 2026-05-05 |   🔄 [SHADOW_EVAL_SEQUENTIAL] [MB] model 10/13: qwen3.6-plus — starting... |
| 2026-05-05 14:15:15 | INFO | MB | shadow_eval | 2026-05-05 |   ✅ [MB] qwen3.6-plus: ['14', '09'] (str=6.0, 112.4s) [shadow_auto_eval] |
| 2026-05-05 14:15:15 | INFO | MB | shadow_eval | 2026-05-05 |   🔄 [SHADOW_EVAL_SEQUENTIAL] [MB] model 11/13: gemini-3.1-pro — starting... |
| 2026-05-05 14:15:58 | INFO | MB | shadow_eval | 2026-05-05 |   ✅ [MB] gemini-3.1-pro: ['14', '91'] (str=6.0, 42.5s) [shadow_auto_eval] |
| 2026-05-05 14:15:58 | INFO | MB | shadow_eval | 2026-05-05 |   🔄 [SHADOW_EVAL_SEQUENTIAL] [MB] model 12/13: gemini-3-flash — starting... |
| 2026-05-05 14:16:23 | INFO | MB | shadow_eval | 2026-05-05 |   ✅ [MB] gemini-3-flash: ['91', '09'] (str=6.0, 25.6s) [shadow_auto_eval] |
| 2026-05-05 14:16:23 | INFO | MB | shadow_eval | 2026-05-05 |   🔄 [SHADOW_EVAL_SEQUENTIAL] [MB] model 13/13: gemma-4-31b — starting... |
| 2026-05-05 14:18:03 | INFO | MB | shadow_eval | 2026-05-05 |   ✅ [MB] gemma-4-31b: ['14', '09'] (str=6.0, 99.3s) [shadow_auto_eval] |
| 2026-05-05 14:18:03 | INFO | MB | shadow_eval | 2026-05-05 | [SHADOW_SUMMARY] MB 2026-05-05: success=13 error=0 persisted=13 missing_rows=[] empty_rows=[] |
| 2026-05-05 14:18:03 | INFO | MB | shadow_eval | 2026-05-05 | 🔍 Shadow Auto-Eval Done (startup_shadow_catchup): regions=['MB'] |
| 2026-05-05 16:10:53 | INFO | MN | du_doan_test_mb | 2026-05-05 | [DU-DOAN-TEST-MB] runner_start mode=POST_CLOSEOUT_DIAGNOSTIC_FULL_25 run_label=du_doan_test_v52_5_6_MN_post_closeout_diagnostic_full_25_2026-05-05 |
| 2026-05-05 16:10:54 | INFO | MN | du_doan_test_mb | 2026-05-05 | [DU-DOAN-TEST-MB] runner_finish mode=POST_CLOSEOUT_DIAGNOSTIC_FULL_25 run_label=du_doan_test_v52_5_6_MN_post_closeout_diagnostic_full_25_2026-05-05 official_tables_touched=false |
| 2026-05-05 16:10:55 | INFO | MT | du_doan_test_mb | 2026-05-05 | [DU-DOAN-TEST-MB] runner_start mode=POST_CLOSEOUT_DIAGNOSTIC_FULL_25 run_label=du_doan_test_v52_5_6_MT_post_closeout_diagnostic_full_25_2026-05-05 |
| 2026-05-05 16:10:57 | INFO | MT | du_doan_test_mb | 2026-05-05 | [DU-DOAN-TEST-MB] runner_finish mode=POST_CLOSEOUT_DIAGNOSTIC_FULL_25 run_label=du_doan_test_v52_5_6_MT_post_closeout_diagnostic_full_25_2026-05-05 official_tables_touched=false |
| 2026-05-05 16:10:58 | INFO | MB | du_doan_test_mb | 2026-05-05 | [DU-DOAN-TEST-MB] runner_start mode=POST_CLOSEOUT_DIAGNOSTIC_FULL_25 run_label=du_doan_test_v52_5_6_MB_post_closeout_diagnostic_full_25_2026-05-05 |
| 2026-05-05 16:10:59 | INFO | MB | du_doan_test_mb | 2026-05-05 | [DU-DOAN-TEST-MB] runner_finish mode=POST_CLOSEOUT_DIAGNOSTIC_FULL_25 run_label=du_doan_test_v52_5_6_MB_post_closeout_diagnostic_full_25_2026-05-05 official_tables_touched=false |
| 2026-05-05 16:11:56 | INFO | MB | du_doan_test_mb | 2026-05-05 | [DU-DOAN-TEST-MB] runner_start mode=POST_CLOSEOUT_DIAGNOSTIC_FULL_25 run_label=du_doan_test_v52_5_6_MB_post_closeout_diagnostic_full_25_2026-05-05 |
| 2026-05-05 16:11:59 | INFO | MB | du_doan_test_mb | 2026-05-05 | [DU-DOAN-TEST-MB] runner_finish mode=POST_CLOSEOUT_DIAGNOSTIC_FULL_25 run_label=du_doan_test_v52_5_6_MB_post_closeout_diagnostic_full_25_2026-05-05 official_tables_touched=false |
| 2026-05-05 21:24:20 | INFO | MN | shadow_rerank | 2026-05-06 | 🔀 [SHADOW_RERANK] MN: original=['95', '27'] → reranked=['95', '27'] (scores=[0.9768, 0.9697], bt_changed=False, latency=2224ms) |
| 2026-05-05 21:24:20 | INFO | MN | shadow_eval | 2026-05-06 | [SHADOW_PREFLIGHT] ✅ checked=13 warnings=['gemini-3.1-pro:db_env_drift:google:selected_db', 'gemini-3-flash:db_env_drift:google:selected_db', 'gemma-4-31b:db_env_drift:google:selected_db'] |
| 2026-05-05 21:24:20 | INFO | MN | shadow_eval | 2026-05-06 | 🔍 === Shadow Auto-Eval Start (2026-05-06) === models=['glm-5.1', 'grok-4.20-multi-agent', 'qwen3-coder', 'kimi-k2.5', 'qwen3-max-thinking', 'gpt-oss-120b', 'gpt-5.5', 'deepseek-v4-pro', 'deepseek-v4-flash', 'qwen3.6-plus', 'gemini-3.1-pro', 'gemini-3-flash', 'gemma-4-31b'] regions=['MN'] trigger_source=auto_daily |
| 2026-05-05 21:24:20 | INFO | MN | shadow_eval | 2026-05-06 |   📦 [SHADOW_CONTEXT] [MN] source_data keys=['MB', 'MT', 'MN'] total_stations=6 |
| 2026-05-05 21:24:20 | INFO | MN | shadow_eval | 2026-05-06 |   🧠 [SHADOW_ORDER_C16] [MN] ordered_by_budget_or_tensor=['grok-4.20-multi-agent', 'qwen3-coder', 'gpt-oss-120b', 'gpt-5.5', 'deepseek-v4-pro', 'deepseek-v4-flash', 'qwen3.6-plus', 'glm-5.1', 'qwen3-max-thinking', 'kimi-k2.5', 'gemini-3-flash', 'gemini-3.1-pro', 'gemma-4-31b'] |
| 2026-05-05 21:24:20 | INFO | MN | shadow_eval | 2026-05-06 |   🔄 [SHADOW_EVAL_SEQUENTIAL] [MN] model 1/13: grok-4.20-multi-agent — starting... |
| 2026-05-05 21:24:30 | INFO | MN | shadow_eval | 2026-05-06 |   ✅ [MN] grok-4.20-multi-agent: ['93', '46'] (str=7.5, 10.3s) [shadow_auto_eval] |
| 2026-05-05 21:24:31 | INFO | MN | shadow_eval | 2026-05-06 |   🔄 [SHADOW_EVAL_SEQUENTIAL] [MN] model 2/13: qwen3-coder — starting... |
| 2026-05-05 21:25:32 | INFO | MN | shadow_eval | 2026-05-06 |   ✅ [MN] qwen3-coder: ['93', '78'] (str=8.0, 61.2s) [shadow_auto_eval] |
| 2026-05-05 21:25:32 | INFO | MN | shadow_eval | 2026-05-06 |   🔄 [SHADOW_EVAL_SEQUENTIAL] [MN] model 3/13: gpt-oss-120b — starting... |
| 2026-05-05 21:27:45 | INFO | MN | shadow_eval | 2026-05-06 |   ✅ [MN] gpt-oss-120b: ['21', '24'] (str=0.0, 133.2s) [shadow_auto_eval] |
| 2026-05-05 21:27:45 | INFO | MN | shadow_eval | 2026-05-06 |   🔄 [SHADOW_EVAL_SEQUENTIAL] [MN] model 4/13: gpt-5.5 — starting... |
| 2026-05-05 21:28:56 | INFO | MN | shadow_eval | 2026-05-06 |   ✅ [MN] gpt-5.5: ['95', '93'] (str=8.0, 71.0s) [shadow_auto_eval] |
| 2026-05-05 21:28:56 | INFO | MN | shadow_eval | 2026-05-06 |   🔄 [SHADOW_EVAL_SEQUENTIAL] [MN] model 5/13: deepseek-v4-pro — starting... |
| 2026-05-05 21:30:59 | INFO | MN | shadow_eval | 2026-05-06 |   ✅ [MN] deepseek-v4-pro: ['95', '27'] (str=6.0, 123.4s) [shadow_auto_eval] |
| 2026-05-05 21:31:00 | INFO | MN | shadow_eval | 2026-05-06 |   🔄 [SHADOW_EVAL_SEQUENTIAL] [MN] model 6/13: deepseek-v4-flash — starting... |
| 2026-05-05 21:31:17 | INFO | MN | shadow_eval | 2026-05-06 |   ✅ [MN] deepseek-v4-flash: ['95', '27'] (str=7.5, 17.0s) [shadow_auto_eval] |
| 2026-05-05 21:31:17 | INFO | MN | shadow_eval | 2026-05-06 |   🔄 [SHADOW_EVAL_SEQUENTIAL] [MN] model 7/13: qwen3.6-plus — starting... |
| 2026-05-05 21:34:02 | INFO | MN | shadow_eval | 2026-05-06 |   ✅ [MN] qwen3.6-plus: ['93', '25'] (str=8.0, 165.6s) [shadow_auto_eval] |
| 2026-05-05 21:34:02 | INFO | MN | shadow_eval | 2026-05-06 |   🔄 [SHADOW_EVAL_SEQUENTIAL] [MN] model 8/13: glm-5.1 — starting... |
| 2026-05-05 21:36:04 | INFO | MN | shadow_eval | 2026-05-06 |   ✅ [MN] glm-5.1: ['95', '67'] (str=8.0, 122.1s) [shadow_auto_eval] |
| 2026-05-05 21:36:04 | INFO | MN | shadow_eval | 2026-05-06 |   🔄 [SHADOW_EVAL_SEQUENTIAL] [MN] model 9/13: qwen3-max-thinking — starting... |
| 2026-05-05 21:36:31 | INFO | MN | shadow_eval | 2026-05-06 |   ✅ [MN] qwen3-max-thinking: ['95', '27'] (str=7.5, 26.2s) [shadow_auto_eval] |
| 2026-05-05 21:36:31 | INFO | MN | shadow_eval | 2026-05-06 |   🔄 [SHADOW_EVAL_SEQUENTIAL] [MN] model 10/13: kimi-k2.5 — starting... |
| 2026-05-05 21:40:39 | INFO | MN | shadow_eval | 2026-05-06 |   ✅ [MN] kimi-k2.5: ['56', '67'] (str=7.5, 248.1s) [shadow_auto_eval] |
| 2026-05-05 21:40:39 | INFO | MN | shadow_eval | 2026-05-06 |   🔄 [SHADOW_EVAL_SEQUENTIAL] [MN] model 11/13: gemini-3-flash — starting... |
| 2026-05-05 21:40:59 | INFO | MN | shadow_eval | 2026-05-06 |   ✅ [MN] gemini-3-flash: ['93', '95'] (str=8.5, 20.5s) [shadow_auto_eval] |
| 2026-05-05 21:40:59 | INFO | MN | shadow_eval | 2026-05-06 |   🔄 [SHADOW_EVAL_SEQUENTIAL] [MN] model 12/13: gemini-3.1-pro — starting... |
| 2026-05-05 21:41:47 | INFO | MN | shadow_eval | 2026-05-06 |   ✅ [MN] gemini-3.1-pro: ['95', '56'] (str=6.5, 47.7s) [shadow_auto_eval] |
| 2026-05-05 21:41:47 | INFO | MN | shadow_eval | 2026-05-06 |   🔄 [SHADOW_EVAL_SEQUENTIAL] [MN] model 13/13: gemma-4-31b — starting... |
| 2026-05-05 21:43:57 | INFO | MN | shadow_eval | 2026-05-06 |   ✅ [MN] gemma-4-31b: ['95', '27'] (str=7.0, 130.0s) [shadow_auto_eval] |
| 2026-05-05 21:43:57 | INFO | MN | shadow_eval | 2026-05-06 | [SHADOW_SUMMARY] MN 2026-05-06: success=13 error=0 persisted=13 missing_rows=[] empty_rows=[] |
| 2026-05-05 21:43:57 | INFO | MN | shadow_eval | 2026-05-06 | 🔍 Shadow Auto-Eval Done (auto_daily): regions=['MN'] |
| 2026-05-06 00:50:53 | INFO | MN | du_doan_test_mb | 2026-05-06 | [DU-DOAN-TEST-MB] runner_start mode=REALTIME_AVAILABLE_ONLY run_label=du_doan_test_v52_5_6_MN_realtime_available_only_2026-05-06 |
| 2026-05-06 00:50:55 | INFO | MN | du_doan_test_mb | 2026-05-06 | [DU-DOAN-TEST-MB] runner_finish mode=REALTIME_AVAILABLE_ONLY run_label=du_doan_test_v52_5_6_MN_realtime_available_only_2026-05-06 official_tables_touched=false |
| 2026-05-06 00:54:32 | INFO | None | None | None | 🧪 /du-doan-test pre-result trigger: every 5 minutes, readiness-gated |
