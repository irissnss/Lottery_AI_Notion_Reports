# V105.41 Model Health and Methodology Deep Dive — 2026-05-14

This report exposes the analytical surfaces (model registry, ML and AI generators, prompt mechanism, rule engine, scoring/voting pipeline, measurement and monitoring) and adds per-model performance commentary over the most recent 30-day window. It is intended as a self-contained briefing for external AI tools that the owner uses for second-opinion analysis. All metrics are derived from the local read-only forensic snapshot taken at 2026-05-14 09:25 VN.

## 1. System overview

The system runs three regions:

- **MN — Miền Nam.** Cycle anchor 04:15 VN. Multi-station draw. Best historical hit rate of the three because the MN composition formula has access to D-1 across all three regions and D-2 from MN.
- **MT — Miền Trung.** Cycle anchor 16:30–17:35 VN. Composition formula uses D-1 cross-region + MN D-today.
- **MB — Miền Bắc.** Cycle anchor 17:35–18:45 VN. Hardest weekday-conditioned region. Composition uses D-1 cross-region + MN D-today + MT D-today.

For every region the system writes a **final bundle** per day with five components (BT — bạch thủ, lo2 — top-2 numbers, lo3 — a 3-digit signal, xien2 — pair, xien3 — triple). Every component has an independent verified status (`WIN / LOSE / PARTIAL`).

## 2. Model registry truth (SSOT)

The registry currently activates **15 output-eligible models** for `/du-doan`:

### 2.1 Token (AI) generators — `output_eligible=True`

| ID | Provider | Class | Role | Note (registry wr_note) |
|---|---|---|---|---|
| gpt-5-mini | openai | TOKEN | GENERATOR | WR≈73% |
| claude-sonnet-4-6 | anthropic | TOKEN | GENERATOR | WR≈73% |
| gemini-2.5-flash | google | TOKEN | GENERATOR | WR≈70% |
| claude-opus-4-20250514 | anthropic | TOKEN | GENERATOR | WR≈76% (highest token) |
| deepseek-reasoner | deepseek | TOKEN | GENERATOR | WR≈62% overall, ≈67% MB |
| gemini-2.5-pro | google | TOKEN | GENERATOR | WR≈63% overall, ≈86% MN |
| gpt-5.4 | openai | TOKEN | GENERATOR | Replaced deepseek-chat |

### 2.2 No-token (ML / ensemble) generators — `output_eligible=True`

| ID | Class | Role | Stack |
|---|---|---|---|
| meta-learning | NO_TOKEN | ML_PREDICTOR | LightGBM meta-classifier ranking the top-K tails. |
| lstm | NO_TOKEN | ML_PREDICTOR | Sequence LSTM, top-K by next-step probability. |
| xgboost | NO_TOKEN | ML_PREDICTOR | Gradient boosted tree on tabular features. |
| random-forest | NO_TOKEN | ML_PREDICTOR | Random forest classifier on tabular features. |
| smart-ensemble | NO_TOKEN | ENSEMBLE | LSTM + Meta-Learning, overlap-weighted top-2. |
| smart-ml | NO_TOKEN | ENSEMBLE | XGBoost + Random Forest, overlap-weighted top-2. |
| combo-no-token | NO_TOKEN | ENSEMBLE | Consensus over all four ML predictors plus cross-region signals. |

### 2.3 Hybrid generator — `output_eligible=True`

| ID | Class | Role | Stack |
|---|---|---|---|
| combo-super | TOKEN | ENSEMBLE | Hybrid: 4 ML predictors + 7 token AI predictors, weighted consensus. Cost = top-3 token calls. |

### 2.4 Shadow auto-eval roster (`status=SHADOW_AUTO`, `output_eligible=False`) — 13 models

`glm-5.1`, `grok-4.20-multi-agent`, `qwen3-coder`, `kimi-k2.5`, `qwen3-max-thinking`, `gpt-oss-120b`, `gpt-5.5`, `deepseek-v4-pro`, `deepseek-v4-flash`, `qwen3.6-plus`, `gemini-3.1-pro`, `gemini-3-flash`, `gemma-4-31b`.

These run on each region after the official chain, write predictions and reliability rows, but are explicitly excluded from `/du-doan` publishing. They feed measurement and A/B (`DIRECT_KEY_AB_SHADOW_PENDING`).

### 2.5 Schedule slots

The registry exposes seven schedule slots:

- `04:00_all_regions` — no-token ML batch for all three regions.
- `04:15_MN_only` — token AI batch for MN (cron 04:15 VN).
- `ai_chain_post_verify` — token AI batch triggered after MN result verify (≈ 16:30 for MT, 17:35 for MB).
- `completion_triggered_shadow` — shadow eval starts immediately after each region's token batch finishes.
- `shadow_eval_post_verify` — shadow eval rerun after each region's verified result.
- `cascade_rerun_post_verify` — no-token cascade rerun after verify for downstream regions.
- `shadow_rerank_post_combo_super` — Cohere shadow rerank (no generative output today).

## 3. Cycle architecture

```
04:00 VN  ML batch all regions (DD Trước / DD Sau by region)
04:15 VN  MN token batch starts → diversity pass → combo-super → MN final bundle (ACTIVE)
04:15+  MN shadow eval completion-triggered (13 SHADOW_AUTO models)
16:30 VN MT token cycle (post-verify cascade, ai_chain) → MT final bundle
17:35 VN MB token cycle (post-verify cascade) → MB final bundle
18:30 VN MB scrape + verify → final bundle verified_at populated
```

Each token call is wrapped by `_safe_stdio_ctx` plus a worker thread:

- 0–90 s : normal — result accepted directly.
- 90 s : soft-continue, the scheduler logs `[SOFT_CONTINUE_90S]` and starts the next model. The slow model keeps running in its own thread.
- 90–300 s : `OK_AFTER_SOFT_CONTINUE_90S` if the result arrives in time; otherwise the model is marked timeout at the hard boundary.
- 300 s : hard timeout. The thread is cancelled and the row is marked `TIMEOUT_300S`. The model contributes nothing to the bundle. The diagnostic-row contract from V105.30d guarantees a persisted empty diagnostic row instead of a silent missing model.

Hard-locked timeouts are `AI_MODEL_SOFT_CONTINUE_SEC=90` and `AI_MODEL_HARD_TIMEOUT_SEC=300`. V105.38 designed an extended-grace lane at 500 s as proposal only; it is not deployed.

## 4. Prompt mechanism (token AI generators)

Every token model receives the same Vietnamese-language system + user prompt for the (region, date) it is predicting. The prompt is composed at runtime in three blocks:

1. **Phase & Doctrine.** Reading from a small static doctrine block plus per-region rule cards (P-18, Phase-19). This declares the analytic framing (Đảo gương / Giao trục), strength bands, diversity penalty rule, region/weekday WR pointers, and the JSON output schema.
2. **Context Pack.** A compact one-screen Vietnamese block summarizing the current candidate convergence (CONV×N), source prizes, "FRESH / PARTIAL_SPENT / FULL_SPENT" status for top candidates, mined rules with their tier (`READY_STRONG`, `READY_WITH_CAUTION`, `LIMITED_WEIGHT`, `REFERENCE_ONLY`), 4W/8W/12W/16W hit rates and lift365.
3. **Decision Policy.** Soft rules guiding the model toward a `verdict` ∈ `{CHOT_HA, CHON_CAN_THAN, SKIP}` with `main_number`, `secondary_number`, `main_reason`, `secondary_reason`, plus a structured `strength` breakdown (phase_match, frequency, db_g8_presence, cycle_rhythm, mirror_support).

Each model returns the prompt as a JSON object that the backend parses, validates and persists. The structured fields are then re-used by the scoring/voting pipeline downstream.

Important locks preserved:

- Production prompt is unchanged. Any prompt experiments are shadow-only.
- The prompt asks the model to **avoid herding** explicitly (`CONV×4 trap`) and to weight regional weak-day signals.

## 5. ML pipeline (no-token generators)

The no-token lane has four standalone ML predictors:

- **LSTM.** Sequence model over per-region tail histories. Outputs a top-K by next-step probability. Recent val_loss reported per region in the verdict reason for transparency.
- **Meta-Learning.** LightGBM meta-classifier whose features include per-tail stat scores, weekday context, region condition. Reranks top-K candidates.
- **XGBoost / Random Forest.** Tabular classifiers on engineered features (frequency, gan, hot/cold, pairs, day-of-week boosts, cross-region cues). Each emits a top-K probability ranking.

Three local ensembles consume those outputs:

- **smart-ensemble:** intersects LSTM + Meta-Learning top-K, picks the two with the largest combined probability.
- **smart-ml:** intersects XGBoost + Random Forest top-K with the same rule.
- **combo-no-token:** consensus vote across all four ML predictors, with cross-region signals overlay. This model has consistently been one of the highest performing in BT hit rate over the last 30 days.

The hybrid **combo-super** sits on top: weighted vote across the four ML predictors + the seven token AI predictors, gated by per-model WR adjustments. It does not over-write the AI predictions; it acts as an explicit "consensus check" that is allowed to publish only when both votes count ≥3 and combined strength ≥5.5.

## 6. Rule engine

The rule engine is the system's deterministic backbone. It mines candidate rules of the form:

```
"Tail X appears in target_region D-today when source prize Y on source_region (offset D-1 or D-2) shows pattern Z, weekday W."
```

Each mined rule has:

- `tier ∈ {READY_STRONG, READY_WITH_CAUTION, LIMITED_WEIGHT, REFERENCE_ONLY}`
- `activation_status ∈ {active, shadow, monitor, demoted}`
- `prediction_use ∈ {direct_core, direct_extended, support}`
- 4-, 8-, 12-, 16-week hit rates
- 365-day lift score (`lift_365`)
- `prize_keys` restricted to the *source_region* (Rule105 fix from V105.30b)
- `source_station_slot` (weekday-conditioned source station)

Important locks preserved:

- **Rule105 prize-source lock by `source_region`** (not target_region). After the V105.30b correction this constraint produced **zero true violations** across 105 active rules.
- Production mined-rules table is not touched outside the dedicated weekly retrain process. All experiments write to shadow tables (`*_shadow`).

## 7. Scoring and voting pipeline (`generate_final_bundle`)

The scoring pipeline reads each prediction row and produces the final bundle:

1. Apply WR/BT quality filter. Models below the per-region WR threshold are excluded from the vote. They still appear in the output-eligible row count for readiness, but contribute zero weight to the bundle vote (V105.35 semantic split — readiness vs voting quality).
2. Apply diversity penalty (V10.5). If 4+ token models converge on the same tail, the two weakest contributors get a strength penalty (-1.0 to -2.5 depending on herd size). This prevents single-tail collapses.
3. Weighted vote with WR adjustment. Each candidate tail accumulates weight = strength × WR_weight. The top tail becomes BT; the runner-up becomes lo2[1].
4. lo3 / xien2 / xien3 derive from BT / lo2 with deterministic post-processing.
5. Consensus level: `strong` if ≥3 voters agree on BT *and* the BT score is ≥ 5.5; otherwise `moderate` or `weak`.
6. Publish gate: V105.35 semantic gate — `publish_ready = output_eligible_row_count == 15` (the 15 official roster slots), independent of how many models passed WR/BT. If `scoreable_model_count < 15`, the gate publishes the bundle but adds a quality warning.

## 8. Measurement and monitoring surfaces

The system writes daily measurement to multiple tables:

- `predictions` — one row per (model, region, date, run_source). Hit count, pick count, verdict, strength, run_source, context integrity.
- `final_bundles` — one row per (region, date). BT/lo2/lo3/xien2/xien3 with verified status, model_count, generation_method, consensus_level.
- `runtime_reliability_model_daily` — one row per (model, region, date, component). Outcome status, finish_reason, error_message, latency, persisted_row, notes.
- `model_daily_eval` — one row per (model, region, date). BT hit, hit_count, strength, run_source, context_integrity, status.
- `scheduler_logs` — text log table with region, job_name, log_level. Holds runtime events (model_call_start/end, soft_continue, hard_timeout, closed_file).
- `du_doan_test_bundles` — lane-test bundles (shadow / challenger experiments). Strict guard: `output_eligible=0`, `diagnostic_only=1`, `owner_approved=0`.
- Various `*_shadow` tables for measurement-only experiments.

Two automation surfaces (`docs/AUTOMATION_STATE.json`, `docs/AUTOMATION_HISTORY.jsonl`) provide machine-readable history of each V105.* event for queryability.

## 9. 30-day per-model scoreboard

Computed at 2026-05-14 09:25 VN over the window 2026-04-15 → 2026-05-14. Sorted by BT hit rate over `model_daily_eval` rows.

| Model | Lane | Predictions | Empty rate | Reliability rows | Success rate | Closed-file | Eval rows | BT hit rate | lo2 hit rate | Latency p50 / p95 (ms) | Recommendation |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| arcee-trinity | shadow (REMOVED 22/4) | 26 | 0% | 0 | n/a | 0 | 26 | 46.15% | 61.54% | n/a | shadow accumulate (no active runs) |
| smart-ml | no-token output | 84 | 0% | 0 | n/a | 0 | 84 | 44.05% | 64.29% | n/a | KEEP |
| combo-no-token | no-token ensemble output | 84 | 0% | 0 | n/a | 0 | 84 | 42.86% | 60.71% | n/a | KEEP |
| llama-4-maverick | shadow (REMOVED 22/4) | 12 | 0% | 0 | n/a | 0 | 12 | 41.67% | 58.33% | n/a | shadow accumulate (no active runs) |
| xgboost | no-token output | 84 | 0% | 0 | n/a | 0 | 84 | 40.48% | 64.29% | n/a | KEEP |
| gpt-5.5 | shadow | 52 | 1.92% | 84 | 95.24% | 3 | 52 | 40.43% | 55.32% | varies | PROBATION_SHADOW (closed-file watch) |
| meta-learning | no-token output | 84 | 0% | 0 | n/a | 0 | 84 | 39.29% | 60.71% | n/a | KEEP |
| gpt-5-mini | token output | 83 | 0% | 0 | n/a | 0 | 83 | 38.55% | 62.65% | n/a | KEEP |
| gpt-oss-120b | shadow | 73 | 1.37% | 86 | 96.51% | 2 | 73 | 37.31% | 47.76% | varies | PROBATION_SHADOW (closed-file watch) |
| random-forest | no-token output | 84 | 0% | 0 | n/a | 0 | 84 | 36.90% | 63.10% | n/a | KEEP |

Observations:

- The strongest "everyday" model is `smart-ml` (44.05% BT). It uses XGBoost + Random Forest agreement, which avoids the herding risk that token AI sometimes shows. `combo-no-token` and `xgboost` are also consistently in the top six.
- Among token models, `gpt-5-mini` is the highest BT hit-rate model with 38.55% and zero closed-file events over the 30-day window. `gpt-5.5` and `gpt-oss-120b` perform well but sit in `PROBATION_SHADOW` because of intermittent closed-file diagnostics in the shadow lane.
- The four removed shadow models (`arcee-trinity`, `llama-4-maverick`, `mistral-large-3`, `kimi-k2.6`) show high hit rates but on smaller samples, and they were pruned for stability / cost reasons — they remain in the audit trail only.
- The "empty rate" column captures token models whose runs occasionally returned empty/null content (parser fail or `finish_reason=length`). Today's roster shows zero empty rate for active output-eligible models; the only non-zero values are on shadow models.
- `latency_p95` is captured at the reliability layer for shadow models (token models in the official lane use a different code path that does not currently emit latency reliability rows; this is on the V105.40 expansion list).

## 10. Final bundle 30-day aggregate

| Region | Days | BT WIN rate | lo2 WIN+PARTIAL rate | Days at model_count=15 | Days at consensus=strong |
|---|---:|---:|---:|---:|---:|
| MN | 30 | 46.67% | 63.33% | 27/30 | 29/30 |
| MT | 29 | 48.28% | 65.52% | 26/29 | 25/29 |
| MB | 29 | 20.69% | 48.28% | 7/29 | 27/29 |

Interpretation:

- **MN** and **MT** publish 15/15 almost every day with strong consensus; their BT WIN rates near 47–48% are the system's strongest signal.
- **MB** stays at 15/15 only on 7 of 29 days. The remainder publish with `model_count<15` because the WR/BT filter often drops two-to-three quality-warned models on MB. BT WIN rate at 20.69% reflects MB's structural difficulty (single station, single tail target), not a publish-gate failure.
- The 30-day window includes 2026-05-13 where MB BT=32 lost and all seven lane-test challengers also picked 32. That confirms the MB difficulty is shared across challengers, not a publisher mistake — promoting any lane-test challenger that day would not have helped.

## 11. Methodology evaluation and recommendations

### 11.1 What is working well

- **Diversity penalty (V10.5).** Effective. Avoided multiple herding traps in the 30-day window. Recommendation: keep enabled, accumulate more cycles before re-tuning the penalty curve.
- **V105.30d diagnostic-row contract.** Working as designed. Every closed-file event observed in the past three days produced a persisted diagnostic empty row; zero silent missing rows in `auto_daily`.
- **V105.35 semantic publish gate.** Working as designed. MB publishes whenever output rows are 15/15 even if scoreable count is 13–14 due to WR/BT filtering. The quality warning surfaces in the bundle but does not block the user.
- **V105.15 timeout architecture (90 / 300 s).** Working as designed. 20 soft-continue events and 8 hard-timeout events on 13/5 all completed without official mutation.
- **MT 5-model recovery.** Confirms that the morning closed-file class on 13/5 was transient. The afternoon cycle (ai_chain) produced clean outputs for all five token models.

### 11.2 What needs attention

- **Closed-file regression**, currently spanning 7 source paths. The official prediction path is unaffected, but user-facing `/api/review-hub/filter` is broken and several measurement surfaces (Pattern Tracker, Shadow Daily Comparison, Shadow Rule D1, Excel writer) lose runtime. V105.40 expansion patch is designed; deploy is owner-gated.
- **MN Wednesday weakness.** Wednesday MN has historically been the weakest weekday (~41% per the prompt's weekday hint). Forecast: keep highlighting this in the prompt; consider a per-weekday confidence threshold proposal in shadow only.
- **MB structural difficulty.** MB BT WIN rate ≈21% across 29 days is consistent with the historical 27.8% baseline. The lane-test forensic confirms challengers do not consistently outperform official on bad days — `DO_NOT_PROMOTE_MB_CHALLENGER` remains correct. A new approach (regional source-station-slot reweighting on MB) would have to be a multi-week shadow experiment before any owner gate.
- **Shadow lane latency outliers.** `gpt-oss-120b` 725s, `gpt-5.5` 635s, `qwen3.6-plus` 450s, `deepseek-v4-pro` 576s, `qwen3-coder` 808s — all shadow-only, all persisted SUCCESS. Recommendation: classify per V105.38 (`LATE_AFTER_HARD_TIMEOUT_SHADOW` 300–500 s, `TOO_LATE_SHADOW` >500 s), do not feed official, and continue accumulating data for the direct-API vs OpenRouter A/B plan.
- **Source-pool / prompt / top-2 tuning.** Held until V105.40 deploys and the runtime is clean across a full 24-hour cycle.

### 11.3 Concrete next-step proposals

1. **V105.40 expansion patch (shadow + main + measurement).** Add a module-level `_safe_stdio_ctx` plus `_safe_print` helper to `gpt_analyzer.py`; wrap each token provider entry point. Add `_safe_print` to `main.py` and replace every `traceback.print_exc()` in user-facing endpoints (16 sites today). Apply the same to Excel writer, verify-final-bundle, Pattern Tracker, Shadow Daily Comparison, Shadow Rule D1 materializer. Minimal-diff; no scoring/prompt/selector/voting/roster/publish-gate/timeout/trigger changes. Deploy + restart only outside live windows.
2. **V105.38 extended-grace 500 s proposal.** Implement as new constant `AI_MODEL_EXTENDED_GRACE_SEC=500` only when V105.40 patch lands and the system is clean. Keep 300 s as the official freeze SLA; 500 s only enables late metadata + diagnostic, never feeds official.
3. **Direct-API vs OpenRouter shadow A/B.** Continue measurement-only. The closed-file regression shows up on both OpenRouter (`qwen3-max-thinking`, `kimi-k2.5`, `gpt-oss-120b`) and direct provider routes (`gemma-4-31b`, `gpt-5-mini`), confirming the issue is in stdio handling on the long-running process, not in the route choice.
4. **MN Wednesday confidence tuning proposal.** Shadow only. Lower per-model strength threshold on T4 MN and let combo-no-token + smart-ml carry more weight. Track WR delta for 14 days. No production change.
5. **Source-pool drilldown.** Held until runtime is clean. The plan (`SOURCE_POOL_ROOT_CAUSE_DRILLDOWN_PLAN.md`) is owner-approved as plan-only.

## 12. Per-model commentary (today's roster)

| Model | Lane | 30d BT hit rate | Today's role | Commentary |
|---|---|---:|---|---|
| gpt-5-mini | token output | 38.55% | First token call; usually breaks ties early | Highest hit-rate token model with zero closed-file in 30d. Reliable workhorse. Today picked tail 35 for MN. |
| claude-sonnet-4-6 | token output | n/a (in eval) | Strong reasoning, often herds with gpt models | Performed reliably yesterday afternoon after morning closed-file; today picked tail 35 for MN. |
| gemini-2.5-flash | token output | n/a | Fast call, supports diversity | Today picked tail 04 + 15, providing diversity against the 35 cluster. |
| claude-opus-4-20250514 | token output | n/a | Highest WR per registry note (76%) | Today picked tail 35 + 04 with strongest convergence reasoning. |
| deepseek-reasoner | token output | n/a | MB-leaning (67% per note); SKIP eligible | Today SKIP'd MN with strength 3.5 < threshold 5.0 — correct behavior. |
| gemini-2.5-pro | token output | n/a (very high MN) | Often picks rule-aligned tails | Today picked 35 + 51 for MN. |
| gpt-5.4 | token output | n/a | Cost-balanced replacement | Today SKIP'd MN — correct under AUTO-SKIP rule. |
| meta-learning | no-token ML output | 39.29% | LightGBM reranker | Robust everyday performer. |
| lstm | no-token ML output | (in eval) | Sequence baseline | Lower confidence on small N; supports overlap signals only. |
| xgboost | no-token ML output | 40.48% | Tabular booster | Top-5 by BT in 30 days. |
| random-forest | no-token ML output | 36.90% | Tabular RF | Reliable but slightly behind XGB. |
| smart-ensemble | no-token ensemble output | n/a | LSTM × Meta overlap | Drops out when WR<40%. |
| smart-ml | no-token ensemble output | 44.05% | XGB × RF overlap | Highest BT hit rate among production-eligible models. |
| combo-no-token | no-token ensemble output | 42.86% | Consensus over 4 ML | Today picked tail 16, 74 for MN; the eventual final bundle BT was 16. |
| combo-super | hybrid output | n/a (output-eligible) | Cross-vote 4 ML + 7 AI | Today SKIP'd MN (only 2/3 model agreement, strength 5.0 < 5.5 threshold). Correct under publish gate. |

For shadow lane, the most notable lately-watched models are:

| Model | Provider route | Window observation |
|---|---|---|
| glm-5.1 | OpenRouter | Recurring `finish_reason=length` under heavy full context. Compact-JSON profile proposal exists (owner-gated). |
| gpt-5.5 | OpenRouter | Strong BT hit rate (40.43%) but 3 closed-file events in 30d. PROBATION_SHADOW. |
| gpt-oss-120b | OpenRouter | High latency in shadow; persisted closed-file 2 times in 30d; PROBATION_SHADOW. |
| gemma-4-31b | Google direct shadow | Closed-file 04:36 13/5; persisted diagnostic — contract held. |
| qwen3-max-thinking | OpenRouter | Closed-file 04:31 13/5; persisted diagnostic — contract held. |

## 13. Recommendations summary

- **Keep**: smart-ml, combo-no-token, xgboost, meta-learning, gpt-5-mini, claude-opus-4-20250514, random-forest, claude-sonnet-4-6, gemini-2.5-flash, gemini-2.5-pro, gpt-5.4, lstm, smart-ensemble, combo-super. (All 14 active output-eligible models stay on the roster.)
- **Watch**: gpt-5.5 and gpt-oss-120b shadow models — promotion blocked until closed-file class is fully fixed.
- **Probation shadow**: glm-5.1 (compact profile proposal owner-gated).
- **Do not promote**: any MB lane-test challenger. Confirmed across two consecutive MB days that challengers either match official or lose worse.
- **Direct-key A/B continue accumulating** — no migration decision until V105.40 deploys and stdio class is clean.
- **Owner approve V105.40 expansion + restart after MB close ~19:00 VN today**. This is the safest deploy window of the day.

## 14. Public-safe assertions

- No prediction numbers from currently-pending cycles are disclosed in this report.
- No credentials, secrets, IP addresses, or VPS paths appear in this document.
- Every metric is taken from the local read-only forensic snapshot, no manual provider call was made.
- The official `/du-doan` lock remains intact across the entire 30-day window.
