# V10871 — Cutting weak models on quality, not on price

Owner instruction that reset this session:

> model chất lượng giữ lại cắt giảm model yếu kém việc cắt giảm đã tiết kiệm rồi đừng nói chi phí
> cao thấp trên 1 model... ít nhưng mà chất là được

> quá trình shadow khá dài nhưng đôi lúc bị lỗi gián đoạn nên em cần tư duy đánh giá tổng thể,
> thời gian live, shadow dài là lợi thế để đo lường

Both constraints are now encoded in code, not just in a report.

Source: paired live sync `artifacts/live_sync/20260729_110343/manifest.json`.

## 1. Start of day 29 July — no re-run was needed

Miền Nam had already produced a complete official field: 15 rows, `scoreable_model_count` 15,
`incomplete_bundle` false, bundle `BT 96 ["96","32"]` written at 04:18:51 Vietnam time, plus 21
lane rows. Miền Trung and Miền Bắc only had their seven 04:00 machine-learning rows, which is
correct because their AI passes run at 16:42 and 17:42.

Only `gemma-4-31b` failed, with a Gemini 429 quota error, and it is a shadow lane.

Re-running the models would have rewritten a frozen output after the fact, which the V10861 owner
lock forbids, so nothing was re-triggered.

## 2. Closeout 28 July

Results: Miền Bắc special 00; Miền Nam 00 / 71 / 31; Miền Trung 82 / 50.

All three official picks missed the special prize (55, 95, 39). Miền Trung's `lo2` was partial
because 87 landed on the board. On `/choi`, Miền Trung hit and the other two missed.

All three bundles were marked incomplete, but only one was a real defect:

| Region | Missing | Why |
|---|---|---|
| Miền Bắc | `gpt-5-mini` | `bt_gate bt<12` — a deliberate quality gate |
| Miền Trung | `lstm`, `meta-learning` | `max_voters_cap MT_top13_only_V10752` — deliberate design |
| Miền Nam | `deepseek-reasoner` | genuinely empty, now fixed |

### The Miền Trung aggregation problem

Sixteen of twenty-seven models had their primary number hit as a lô. Eight models put **87** in
first position: deepseek-reasoner, gemini-3.5-flash, gemma-4-31b, glm-5.1, gpt-5.5, gpt-oss-120b,
grok-4.3, kimi-k2.5.

The official pick was 39, which came from random-forest, smart-ensemble, smart-ml, xgboost and
combo-no-token — five machine-learning models that share features and therefore vote as a
correlated block. A five-vote block outweighed a broader agreement across independent AI models.

That is a failure of the aggregation weighting, not of the models. It is filed as
`FU-V10871-MT-AGGREGATION` with a shadow measurement to come; production selection was not
touched.

## 3. Ranking models by quality

New module `_v10871_model_quality_ledger.py`. Instead of comparing raw hit rates, every model is
scored against the **same-day, same-region pool average**. This matters for two reasons the owner
raised directly:

- Lanes start and stop on different dates. A 23-day lane is now comparable with a 180-day lane.
- Shadow lanes get interrupted by provider errors. Days a model missed simply drop out of its
  own pairing instead of distorting a raw average.

Window 1 April to 28 July: 180 days, 35 models, 11,034 evaluation rows, one-sided bootstrap with
4,000 resamples. **Price is recorded as context and never enters the ranking.**

### The method validates itself

The three models the owner retired in earlier sessions all score weak on this metric:
`qwen3-coder` −6.0pp (p=0.011), `gemini-3-flash` −4.1pp, `deepseek-v4-pro` −1.6pp BT and −4.6pp
ANY. The measure reproduces his past decisions before being used to propose new ones.

### Retired on 29 July

| Model | BT lift | p | ANY lift | p | n | Periods positive | Error rate |
|---|---|---|---|---|---|---|---|
| `gemma-4-31b` | −6.7pp | 0.004 | −8.9pp | 0.000 | 243 | 0 of 4 | 21.3% |
| `kimi-k2.5` | −5.0pp | 0.009 | −5.2pp | 0.023 | 274 | 1 of 5 | 2.9% |

Both are shadow lanes, so the official field did not change. Shadow roster 12 → 10, official stays
at 15. After the cut, no active model is flagged as a retire candidate.

### Strongest models in the pool are still shadow

| Model | Roster | Signal |
|---|---|---|
| `gemini-3.5-flash` | SHADOW | BT **+8.2pp** (p=0.034), positive in both periods it ran |
| `qwen3.7-max` | SHADOW | ANY **+8.1pp** (p=0.029), 0% error rate |
| `gemini-2.5-pro` | OFFICIAL | +3.4pp, positive in **5 of 5** periods — the stable anchor |

Promoting the first two would change the official field and therefore open a new M2/Total cohort,
so it waits for an explicit owner decision.

### Regime warning

`claude-opus-4-6` scored +15.3pp under prompt PB-18.0 and **−16.6pp** under PB-18.1. Any judgement
on it must be made inside a single prompt regime.

## 4. Two deferred defects from 28 July, now closed

**`deepseek-reasoner` truncation.** The model runs with `thinking=True`, and DeepSeek counts
reasoning tokens against `max_tokens`. It had no entry in `_DIRECT_DEEPSEEK_SHADOW_MAX_TOKENS`, so
it fell back to the 16,384 default — while its own shadow twin `deepseek-v4-pro-real` was granted
393,216. Measuring 160 calls since 1 July gives a reasoning peak of 13,198 tokens, which leaves
almost no room for the JSON body. Raised to 32,768, roughly 2.5× the observed peak while still
bounding latency.

**PHASE-FIRST contract.** V10750, owner-approved on 25 June, dropped the contract after a 70-day
measurement showed no improvement. The implementation only went half way: the model set was
emptied but the `lane_test_shadow_pack` branch still forced the contract, which is what voided
grok-4.3's valid answer on 28 July after two paid calls. The gate now reads
`gate_contract_mode = selected_model in PHASE_FIRST_CONTRACT_MODELS`, matching the decision the
owner actually signed.

## 5. Measurement surfaces

Table `v10871_model_quality_ledger` (`shadow_only=1`, `diagnostic_only=1`, `output_eligible=0`),
admin API `/api/admin/model-quality-ledger`, a **BẢNG CHẤT LƯỢNG MODEL** panel on `/monitoring`
registered for the 60-second refresh, and a daily cron at 21:25 after the CP-L6 audit at 21:20.

## 6. Two stale surfaces found

`model_latency_cost_audit_daily` stopped on 6 May and `pnl_daily_summary` stopped on 20 May;
`du_doan_test_latency_daily` is empty. Cost and latency for this session had to be rebuilt by hand
from `prediction_trace.jsonl`. The new ledger now records average latency and tokens per call for
the last 30 days so the gap is partially covered. Filed as `FU-V10871-STALE-COST-PNL`.

## 7. Verification

Hashes of `predictions`, `final_bundles`, `lottery_results` and `model_daily_eval` are identical
before and after deployment. Cross-module contract check passes, the timetable self-check is
11/11, `/api/health` returns 200, `/du-doan` returns 200, and the new admin endpoint returns 401
without a session.
