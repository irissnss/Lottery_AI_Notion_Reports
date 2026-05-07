# 7/8 — ALL MECHANISMS

## 7a. Production cascade

| Step | Trigger | Action |
|---|---|---|
| MN AI predict | 04:30 VN | Generate MN prediction with full AI cascade |
| MN closeout | After MN result | Verify MN, write final_bundles status |
| NO-TOKEN ML predict (all regions) | 04:00 VN | LSTM + Meta + Smart-ML + Smart-Ensemble |
| MT AI predict | 16:45 VN | Generate MT prediction |
| MT scrape | ~17:30 VN | Scrape MT result + verify MT |
| MB AI predict | 17:45 VN | Generate MB prediction |
| MB watchdog | 17:55 VN | Re-trigger MB if missing |
| MB scrape | ~18:30 VN | Scrape MB result + verify MB |
| Cascade rerun post_verify | After each region verify | Re-evaluate downstream models |

## 7b. Bundle gate / publish audit

| Mechanism | Table | Doctrine |
|---|---|---|
| ai_primary_gate | ai_primary_gate_daily | AI BLOCKED / OK gate per day |
| bundle_readiness_gate | bundle_readiness_gate_daily | READY / PARTIAL_READY / BLOCKED |
| public_bundle_publish_audit | public_bundle_publish_audit_daily | PUBLISHED_BEFORE_READY warning |
| output_eligible_completion | output_eligible_completion_daily | Output completeness per cycle |
| reasoning_layer_penetration | reasoning_layer_penetration_daily | How deep reasoning layers reached |
| ai_reasoning_contract | ai_reasoning_contract_daily | PHASE-FIRST contract compliance |
| degraded_live_day flag | live_watch markers | DEGRADED_LIVE_DAY annotation |
| readiness_state | bundle_readiness_gate | READY / PARTIAL_READY / BLOCKED |
| bundle_quality | various | INCOMPLETE / OK |
| publication_status | final_bundles | OFFICIAL / SUPPRESSED |
| escape_state | strongest_candidate_escape_daily | STRONGEST_OVERRIDDEN / STRONGEST_PRESERVED |

## 7c. Strongest-to-final preservation (P0 portfolio)

| Item | Where | Status |
|---|---|---|
| strongest_to_final_preservation_v1 | shadow_results | LIVE 11d, **POTENTIAL_LIFT 11/11 hits all regions** |
| strongest_vs_final_conversion_daily | C-01 | LIVE |
| strongest_candidate_escape_daily | Wave 1 | LIVE |
| candidate_drop_stage_daily | Wave 1 | LIVE |
| BUNDLE_SKEW detection | candidate_drop_stage = BUNDLE_SKEW | LIVE |

## 7d. Output verification (V59 strict)

| Output type | Verification rule | Status |
|---|---|---|
| BT (bach_thu) | Last 2 digits of MTĐB only | LIVE |
| LO2 | Last 2 digits any prize | LIVE |
| LO3 | **Strict 3-digit suffix from actual prize** (NOT 2-digit tail) | FIXED V59 |
| Xien 2 | Same-station hit when station data exists | FIXED V59 |
| Xien 3 | Same-station hit when station data exists | FIXED V59 |

## 7e. Post-cascade rerun (V77)

| Action | Trigger | Purpose |
|---|---|---|
| V70/V73 rerun with full pool | 19:00 VN | Re-run V70 + V73 AFTER all 3 region test runners completed (was firing at 23:45 BEFORE pool ready) |
| Fast incident monitor | 19:05 VN | 5 alert classes RED_FAST/ORANGE_FAST/YELLOW_FAST/EXPLOIT_FAIL_FAST/BUDGET_FAIL_FAST |

## 7f. Anti-herding

| Method | Where | Status |
|---|---|---|
| anti_herding_shadow_v1 | shadow_results | LIVE 9d, PARITY 14d |
| verdict_distribution_daily | Wave 2 | LIVE |
| convergence_cluster_pattern_daily | shadow | LIVE |
| AI cluster cap (V79) | cluster_weighted_consensus_shadow | LIVE shadow |
| NO_TOKEN floor (V79) | cluster_weighted_consensus_shadow | LIVE shadow |
| AI vs NO_TOKEN cross-verify (V79) | ai_no_token_cross_verification_shadow | LIVE 4d |

## 7g. Cohere rerank

| Item | Where | Status |
|---|---|---|
| cohere-rerank-4-pro | model_registry | REGISTERED non-output, RERANKER role |
| cohere_rerank_log | DB | LIVE |
| cohere_effectiveness_daily | DB | LIVE |
| cohere_rerank_effectiveness_v1 | shadow_results | LIVE 8d, INSUFFICIENT_SAMPLE n=23 |

## 7h. Provider key isolation

| Key env | Used by | Notes |
|---|---|---|
| OPENAI_API_KEY | gpt-5.4, gpt-5-mini | 401 on gpt-5-mini endpoint (V81 swap) |
| ANTHROPIC_API_KEY | claude-opus-4, claude-sonnet-4-6 | OK |
| DEEPSEEK_API_KEY | deepseek-reasoner, deepseek-v4-pro/flash, deepseek-chat | OK |
| GEMINI_API_KEY | gemini-2.5-flash, gemini-2.5-pro | OK |
| GEMINI_KEY_SHADOW_NEW | gemini-3.1-pro, gemini-3-flash, gemma-4-31b | Owner-isolated for V20.3.37.55 cohort |
| OPENROUTER_API_KEY | gpt-oss-120b, gpt-5.5, qwen3-coder, qwen3-max-thinking, qwen3.6-plus, kimi-k2.5, glm-5.1, grok-4.20-multi-agent | OK |

## 7i. Timezone HCM

| Item | Where | Status |
|---|---|---|
| VN_TZ string for APScheduler | scheduler.py L6899 | DESIGN (string is required by APScheduler) |
| `_today_vn_date_str()` helper | scheduler.py L7081 | FIXED V78 |
| `_tomorrow_vn_date_str()` helper | scheduler.py L7090 | FIXED V78 |
| `vn_now()` proper tzinfo | vn_timezone.py | LIVE |
| Cron chain 19:00-19:14 | 6 jobs | LIVE Asia/Ho_Chi_Minh |

## 7j. Hash guard (4 official tables)

| Table | sha256 short | rows |
|---|---|---|
| predictions | 25d1a3db67d6e406 | 4461 |
| final_bundles | 999d42cbaabea95a | 207 |
| lottery_results | 937407feeb8d8f90 | 14628 |
| model_daily_eval | 07a53a97d1521933 | 4412 |

PRE = POST verified V77 → V85.
