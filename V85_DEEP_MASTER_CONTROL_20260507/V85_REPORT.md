# V85 — DEEP MASTER CONTROL — Báo cáo cho anh

Ngày: 2026-05-07T23:55:13+07:00
Trạng thái: SHADOW ONLY — Audit, không ghi DB, không touch official.

## 0. TL;DR cho anh

Anh đúng — V84 chỉ 24 dòng summary là quá thiếu. V85 đếm hết **298 items** vào 8 super-families. Đây là inventory thật, không phải bullet point cảm tính.

| Super-family | Số lượng | File |
|---|---|---|
| 1. AI Models | 41 (ACTIVE=15 / SHADOW=13 / TOKEN=32 / NO_TOKEN=7) | `evidence/f1_all_models.md` |
| 2. DB Tables | 129 (OFFICIAL=4 / TEST_LANE=21 / WAVE_1_2=13 / SHADOW=43 / INFRA=1 / SUPPORT=47) | `evidence/f2_all_db_tables.md` |
| 3. Cron Jobs | 26 (scrape + predict + materialize + V77/V78/V79/V80/V81 + retrain + eval) | `evidence/f3_all_cron_jobs.md` |
| 4. Prompts | 8 (5 production-stack SP/CP/RR/CTX/PB + 3 region-specialist shadow MN/MT/MB) + 5 PFG cohorts + 3 V81 pilot models | `evidence/f4_all_prompts.md` |
| 5. Metrics | 8 C-XX + 3 PB-XX + 16 flip/risk/health (Wilson/Brier/flip/freshness/herd/cluster/regime/cost/drift) | `evidence/f5_all_metrics.md` |
| 6. Rules | mined_rules + 12W/16W windows + PB-18 phase classification + 4 rule-shadow methods | `evidence/f6_all_rules.md` |
| 7. Mechanisms | cascade + bundle gate + strongest-to-final + LO3/Xien strict + post-cascade rerun + anti-herding + cohere + key isolation + timezone + hash guard | `evidence/f7_all_mechanisms.md` |
| 8. Shadow methods | 18 P0 + 30 V52.5 era + 11 V67/V70/V73/V79/V80/V81 selectors | `evidence/f8_all_shadow_methods.md` |

## 1. AI Models — 41 entries

- **15 ACTIVE output-eligible** (production cascade): claude-opus-4-20250514, claude-sonnet-4-6, combo-no-token, combo-super, deepseek-reasoner, gemini-2.5-flash, gemini-2.5-pro, gpt-5-mini, gpt-5.4, lstm, meta-learning, random-forest, smart-ensemble, smart-ml, xgboost.
- **13 SHADOW_AUTO** (measurement only): deepseek-v4-flash, deepseek-v4-pro, gemini-3-flash, gemini-3.1-pro, gemma-4-31b, glm-5.1, gpt-5.5, gpt-oss-120b, grok-4.20-multi-agent, kimi-k2.5, qwen3-coder, qwen3-max-thinking, qwen3.6-plus.
- **7 NO_TOKEN** (local ML, no API): combo-no-token, combo-super, lstm, meta-learning, random-forest, smart-ensemble, smart-ml, xgboost.
- **REMOVED 8 historical**: arcee-trinity, gemma-4-26b, kimi-k2.6, llama-4-maverick, minimax-m2.7, mistral-large-3, mistral-nemo, nemotron-3-super, o3-deep-research, yi-1.5-34b-chat (preserved for audit).
- **REGISTERED non-output**: cohere-rerank-4-pro, pplx-embed-v1, wan-2.7.

## 2. DB Tables — 129 entries

- 4 OFFICIAL (predictions, final_bundles, lottery_results, model_daily_eval) — HASH UNCHANGED.
- 21 TEST_LANE (du_doan_test_*, experimental_preview_shadow, model_strength_by_region_*).
- 13 WAVE_1_2 control surfaces (ai_primary_gate_daily, bundle_readiness_gate_daily, public_bundle_publish_audit_daily, source_prize_effectiveness_daily, weekday_rule_strength_daily, etc.).
- 43 SHADOW (cluster_weighted_consensus_shadow, ai_no_token_cross_verification_shadow, mb_regime_shift_shadow, ai_region_specialist_provider_shadow_results, hybrid_v1_trace, consensus_v1_trace, adaptive_exploit_v67_candidate_trace, etc.).
- 1 INFRA (scheduler_logs).
- 47 SUPPORT (settings, users, prompt_history, model_registry, mined_rules, etc.).

## 3. Cron Jobs — 26 entries

| Time VN | Job ID | Lane |
|---|---|---|
| 04:00 | auto_free_predict | NO_TOKEN ML predict (LSTM+Meta) |
| 04:30 | auto_ai_mn | AI predict MN |
| 16:30 | auto_mn | Scrape MN |
| 16:45 | auto_ai_mt | AI predict MT |
| 17:30 | auto_mt | Scrape MT |
| 17:45 | auto_ai_mb | AI predict MB |
| 17:55 | mb_prediction_watchdog | MB watchdog |
| 18:30 | auto_mb | Scrape MB |
| **19:00** | **v77_post_cascade_rerun** | **V70/V73 rerun** |
| **19:05** | **v77_fast_incident_monitor** | **5 alert classes** |
| **19:08** | **v79_ai_no_token_cross_verify** | **V79 cluster + cross-verify** |
| **19:10** | **v78_prompt_shadow_audit** | **Region prompt audit** |
| **19:12** | **v80_shadow_completion** | **rule_phase + no_token_pack + mb_regime + mn_v67_save** |
| **19:14** | **v81_provider_shadow_pilot** | **Owner-approved 3-model pilot** |
| ~20:00 | auto_daily_eval | Daily eval |
| ~20:10 | auto_mined_rule_eval | Rule eval |
| ~20:20 | auto_model_daily_eval | Per-model eval |
| 23:35 | lag1_adaptive_exploit_signal_materializer | V66.1 lag1 signal |
| 23:40 | adaptive_exploit_v67_materializer | V67 selector |
| 23:45 | consensus_v1_materializer | V70 selector |
| 23:48 | hybrid_v1_materializer | V73 selector |
| 23:50 | drift_monitor_materializer | V76 drift (alert-only) |
| Mon 00:30 | auto_weekly_mining | Rule mining |
| Sun 02:00 | auto_retrain | ML retrain |
| every 5min | du_doan_test_pre_result_trigger | /du-doan-test pre-result |
| weekly | auto_weight_optimizer | Weights optimizer |

## 4. Prompts — 5 production + 3 shadow + 5 PFG cohorts + 3 V81 models

### 4a. Production prompt stack (LIVE)
- **SP-4.0** SYSTEM_PROMPT (TOP1-FIRST V8.0).
- **CP-7.9** CORE_POLICY (declared, ARCHIVE_ONLY, không inject).
- **RR-16.4** REASONING_RULEBOOK (24 rules + §24 BT North Star V16.4).
- **CTX-16.4** CONTEXT_PACK (BT model ranking + weekly tiers).
- **PB-18.0** PROMPT_BUNDLE / PHASE-FIRST GATE 8-step (cohort-gated).

### 4b. PHASE-FIRST GATE cohorts (5)
- PFG-A → B → C → D → **E (active 2026-05-05+)** với 8 model gated.

### 4c. V78 region-specialist shadow prompts (3, SHADOW only)
- MN_AI_REGION_SPECIALIST_PROMPT_SHADOW_V1
- MT_AI_REGION_SPECIALIST_PROMPT_SHADOW_V1
- MB_AI_REGION_SPECIALIST_PROMPT_SHADOW_V1

### 4d. V81 pilot models (3, OWNER-APPROVED shadow)
- deepseek-chat (FAST_CHEAP)
- claude-sonnet-4-6 (REASONING)
- gemini-3-flash (NEW_CHEAP)

## 5. Metrics — 27 (8 C + 3 PB/PP + 16 flip/risk/health/cost)

### 5a. C-XX measurement contracts
C-01 strongest-vs-final | C-02 API source labels | C-03 closeout PENDING | C-05 latency/cost | C-06 LOZ stage | C-15 weekday blackspot | C-16 budget selector 20 voters | C-17 test-lane bundle output_lock_status.

### 5b. PB-XX phase / PP layers
PB-18.0 PHASE-FIRST GATE | PB-18.1+ trace fields | PP-1 Pre-Push live watch.

### 5c. Flip/risk/health/cost metrics (16)
would_save | would_break | false_promotion | strongest_vs_final_conversion | wilson_95_ci | freshness_ready | candidate_drop_stage | herd_pct | reliability_score | stability_score | promotion_bucket | drift_alert_class | fast_incident_alert_class | cluster_weighted_score | regime_shift_warning | cost_estimate_usd.

## 6. Rules

- **Weekly Rule Mining** Mon 00:30 VN → mined_rules + mined_rule_effectiveness.
- **12W / 16W rolling windows** trong rule_engine.py.
- **PB-18 classify_rule_state**: primary_rule_group / secondary_rule_group / stale_rules / rules_to_downweight / top_source_prizes / strongest_source_prizes / strongest_rules.
- **4 rule-shadow methods**: rule_phase_evidence_v1, rule_injection_contract_shadow_v1, rule_phase_synthesis_shadow (V80), no_token_rule_aware_pack_shadow (V80).
- **rule_custom_prompt** mode = ARCHIVE_ONLY (containment 500 chars, không inject runtime).

## 7. Mechanisms

7a. Production cascade (8 cron-driven steps daily)
7b. Bundle gate / publish audit (11 mechanisms: ai_primary_gate, bundle_readiness, publish_audit, output_eligible_completion, reasoning_layer, ai_reasoning_contract, degraded_live_day, readiness_state, bundle_quality, publication_status, escape_state)
7c. Strongest-to-final preservation — **POTENTIAL_LIFT 11/11 hits all regions** (top P0 candidate)
7d. Output verification V59 strict (BT/LO2/LO3 3-digit/Xien same-station)
7e. V77 post-cascade rerun (timing fix bug)
7f. Anti-herding (anti_herding_shadow_v1, verdict_distribution_daily, V79 AI cap + NO_TOKEN floor)
7g. Cohere rerank (LIVE shadow, INSUFFICIENT n=23)
7h. Provider key isolation (6 keys: OPENAI/ANTHROPIC/DEEPSEEK/GEMINI/GEMINI_KEY_SHADOW_NEW/OPENROUTER)
7i. Timezone HCM (helpers fix V78, cron 19:00-19:14 Asia/Ho_Chi_Minh)
7j. Hash guard 4 official tables PRE = POST V77→V85

## 8. Shadow methods — 59 total

- **18 P0 portfolio** (registry): freshness_readiness_guard / strongest_to_final_preservation / no_token_drift_guard / rule_phase_evidence / meta_ranker / output_policy_replay_governance / counterfactual_decision_audit / runtime_final_baseline_control / phase_first_decision / anti_herding / rule_injection_contract / model_wisdom_scorecard / meta_ranker_ltr_dataset / rule_aware_adaptive_notoken / context_specialist_policy / online_bayesian_weighting / phase_aware_rerank / cohere_rerank_effectiveness.
- **30 V52.5 era** (10 method × 3 regions): OFFICIAL_BASELINE_CONTROL, STRENGTH_WEIGHTED_V52_5_2, SPECIALIST_ROSTER_V1, PRIOR_REGION_CONTEXT_SAFE_V1, NO_TOKEN_HERD_REDUCTION_V1, AI_CHAIN_PRESERVATION_V1, ADAPTIVE_BUDGET_SELECTOR_V1 (V57), ADAPTIVE_EXPLOIT_V1 (V67), CONSENSUS_V1 (V70), HYBRID_V1 (V73).
- **11 selector / generator surfaces**: V57/V67/V70/V73/V79 cluster + cross-verify/V80 4 surfaces/V81 pilot.

## 9. Em chưa cover (anh đúng vẫn còn nữa)

V85 đã gom **8 super-families đầy đủ**. Những thứ chưa cover (planned cho V86 nếu anh OK):

1. **150 FU items** (FU-001 → FU-150) — cần dump full state với history.
2. **All phase_checkpoint files** (ước ~40 files) — cần index theo date + topic.
3. **Notion docs** — em chưa list 20+ pages doctrine.
4. **Settings DB** — config keys chưa kê.
5. **Migration history** — schema versions, alter tables.
6. **API routes** (~150 endpoints in main.py) — chưa list per-route.
7. **Frontend pages** — du-doan, monitoring, accuracy, settings, viewer, du-doan-test, v82-monitor, login, etc.
8. **Backup history** — VPS backups timeline.
9. **AUTOMATION_HISTORY full** — tất cả seq từ 0 → 24.
10. **CHANGELOG_GOVERNANCE_LEDGER** + DECISION_LOG entries.

## 10. Hash guard

4 official tables hash unchanged V77 → V85. Em sẽ verify lại sau khi push V85.

## 11. Phương án tiếp

- V85 đã publish 8 super-family files để anh tra cứu.
- Em đề xuất V86 = "Total Inventory Pass 2": full FU/phase/Notion/API routes/migrations/settings.
- Anh OK em làm V86 ngay sau V85 push xong.

## 12. Official UNTOUCHED ✅

Audit READ-ONLY, zero DB writes, zero VPS deploy this pass.
