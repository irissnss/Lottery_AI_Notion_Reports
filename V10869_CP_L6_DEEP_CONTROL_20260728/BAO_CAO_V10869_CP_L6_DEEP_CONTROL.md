# V10869 — CP-L6 deep control: model, Total/M2, cost, timing and same-day

## Owner requirement

- Keep only genuinely strong models.
- Do not treat “shadow” as harmless without tracing indirect output influence.
- Total must always show numbers; warnings are realtime and the user decides whether to play.
- Segment historical evidence around bugs and major updates.
- Verify every model, mechanism, Total method, ML/LLM learning/ranking path, same-day option,
  execution order and timezone before CP-L6 changes.
- Business time must be Vietnam time, `Asia/Ho_Chi_Minh`.

## Evidence source

- Paired VPS database + trace sync:
  `artifacts/live_sync/20260728_001925/manifest.json`.
- Closed evidence through 27/07.
- VPS timetable self-check: 11/11 PASS.
- Cross-module contract: PASS.
- Seven-day causal timing audit: PASS.
- No production model-policy change in this version.

## Direct versus indirect model influence

Current active population:

- 15 official models;
- 12 shadow models.

M2 and V3 consume only the 15 canonical official models. Shadow models do not directly enter
their votes.

K-lane is different: it ranks every model with a current prediction. Latest 27/07 composition:

| Lane | Official voters | Shadow voters |
|---|---:|---:|
| MN K25 | 13 | 12 |
| MT K10 | 7 | 3 |
| MB K8 | 6 | 2 |

MT/MB K outputs are currently promoted. Therefore a shadow model can affect official output
indirectly even though `output_eligible=false`.

Conclusion: no coarse global shadow cut.

## Cost and latency

Ten-day estimate, 18–27/07:

| Roster | Calls | Trace tokens | Estimated USD |
|---|---:|---:|---:|
| Official | 387 | 11,051,998 | 43.47 |
| Shadow | 345 | 53,965,381 | 104.52 |

The estimate uses trace token counts multiplied by the project pricing table. It is not a
provider invoice.

`grok-4.20-multi-agent` alone accounts for an estimated $89.50. Its provider reports
multi-agent reasoning token counts differently; billing must be reconciled before treating
that figure as an actual charge.

## Model evidence

The audit materializes 81 rows: 27 active models × 3 regions.

Each row contains:

- pre-trial and PB-18.1 trial BT/any rates;
- unique winning tails;
- current K rank;
- K leave-one-out save/break days;
- M2 leave-one-out save/break days;
- trace calls, tokens, estimated cost, mean and p95 latency;
- first-run/config regime markers;
- measurement-only recommendation.

## Current lean candidates

### Global candidate

`gemma-4-31b`:

- zero unique winning tails in the trial;
- zero K/M2 would-break;
- no API charge but slow and weak;
- eligible for reduced-cadence parallel proof, not immediate removal.

### Region-specific candidates

| Model | Region | Reason |
|---|---|---|
| grok-4.20-multi-agent | MB | high estimated tokens, weak MB evidence, no latest MB K role |
| gpt-5.5 | MT, MB | no unique contribution in those regions; slow; no latest K role |
| kimi-k2.5 | MB | 10% BT, 20% any, very high latency |
| gpt-oss-120b | MB | weak MB but strong/unique MN–MT value |
| qwen3.7-max | MT | removal saved one K replay day; valuable in MN/MB |

No official model is approved for immediate removal. Several models that look weak globally
still save or break a region-specific K/M2 day. The safe target is per-region cadence, not one
global roster.

## M2 coupling

Current pre-draw truth:

- M2 BT 11/27;
- M0 BT 10/27;
- lift +3.7pp;
- M2 any 18/27 vs M0 13/27;
- `WAIT_N_LT_30`.

M2 reads the official 15-model roster. Any CP-L6 roster/cadence change creates a new regime.
Pre-change and post-change rows must not be pooled. A roster signature is now exposed by the
CP-L6 API.

## Same-day evidence

V10801 forward evidence through 27/07:

| Region/cohort | D-1 top2 | Same-day top2 | Delta |
|---|---:|---:|---:|
| MT meta+xgboost | 61.5% | 46.2% | −15.3pp |
| MB meta+xgboost | 26.9% | 23.1% | −3.8pp |

No same-day promotion. The original gate remains: at least 28 forward days, same-day minus D-1
at least +8pp and positive in both halves.

## ML versus LLM execution order

Current order remains the safest:

- MN: ML 04:00, LLM 04:15;
- MT: ML D-1 at 04:00, LLM 16:42 with legal MN(D) context;
- MB: ML reruns through 17:30, LLM 17:42.

LLMs do not consume today’s ML picks directly; they consume historical ML recent WR.
`combo-super` consumes both ML and AI outputs and runs afterward. Running LLM first has no
accuracy evidence and complicates thin cutoff margins.

## Timezone and `run_date`

- VPS OS timezone: `Asia/Ho_Chi_Minh`.
- BackgroundScheduler and every CronTrigger use `Asia/Ho_Chi_Minh`.
- Business dates are Vietnam dates.
- `scheduler_logs.log_time` and `mined_rule_effectiveness.created_at` are raw UTC surfaces;
  they must be converted before UI/comparison.
- `run_date` is the business-date column name used by `du_doan_test_*`.
- `date` is used by predictions, results and evaluation tables.
- The naming difference is not missing data.

Seven-day timing passed. Thin margins remain:

- MT bundle→lock→cutoff: 1–3 minutes;
- MB bundle→lock→cutoff: 2–4 minutes.

No execution-order change should be made inside those margins without a shadow timing test.

## Total always-display contract

The existing `/choi` contract already:

- always preserves display numbers;
- separates display numbers from capital numbers;
- refreshes every 60 seconds;
- shows form/weekday/week warnings;
- keeps the play/no-play decision with the user.

V10869 adds the realtime official pool warning `input→scoreable`. It never hides numbers and
never changes capital.

## Future Total candidates

1. Region-specific lean coverage-rules M2.
2. Diversity/family-balanced voting to limit correlated AI or ML herds.
3. Cost-aware tie-break only after quality is equal.
4. Selective same-day ML by model×region after forward proof.
5. Conditional Total fallback: V3 may abstain, but display falls back to M2 then M0 with an
   explicit warning.

These are experiment definitions, not production changes.

## Implemented control surface

- Table: `v10869_model_lean_audit`.
- Rows: 81 for 27/07.
- Admin API: `/api/admin/cp-l6-lean`, no-store.
- UI: `/monitoring`, auto-refresh 60 seconds.
- Cron: 21:20 Vietnam time after nightly evaluations.
- Browser verification: Chromium + WebKit at 320, 390 and 1366 pixels, 6/6 PASS.
- `/choi`: model pool warning added; numbers remain visible.

## Deployment safety

- 4/4 deployed MD5 matched.
- Materializer wrote 81 rows.
- Service restart and health passed.
- Admin API and monitoring guest access correctly returned 401.
- Journal errors: zero.
- Official hashes for predictions, final_bundles, lottery_results and model_daily_eval:
  identical pre/post.
- Production model policy changed: false.

## Decision

No model is cut in V10869.

The next action is a reversible 7–14 day parallel lean roster by region. Only after that
forward proof can CP-L6 alter cadence or roster. The natural 28/07 closeout remains the final
input for the first owner decision.

## V10869c enhanced evidence

- Added 600 scorecard rows on the canonical `region + weekday + station-set` axis.
- Added 81 exact model→flow participation rows and surfaced five shadow models that can affect
  official MT/MB indirectly through K-lanes.
- Added 81 M2 roster A/B rows. Arm A is bound to persisted pre-draw truth: 11/27 versus
  official 10/27. Arms B/C only score the 16 days whose reconstructed context exactly matches
  the persisted lane; they are not promotion evidence.
- Added 42 ML–LLM execution-order rows and 240 timezone inventory rows.
- Contract check now fails if M2 Arm A drifts from the persisted lane.
- Enhanced materialization, restart, health, admin auth, journal and hash-4 checks passed.
- Runtime SQL timezone migration remains deferred until after 28/07 closeout so the final
  PB-18.1 trial day is not contaminated by a new ranking/prompt regime.

## Readiness check at 01:26 on 28/07

Live verification passed: health 200, admin lean endpoint 401, service active, cron 21:20 points
at the consolidated materializer, and all six evidence tables are populated
(81 / 600 / 81 / 81 / 42 / 240 rows). The cross-module contract passed both locally and on the
server.

The 28/07 business day itself still has zero results, zero predictions and zero bundles, because
the daily cycle only begins at 04:00 and the closeout materialization runs at 21:20. The CP-L6
decision therefore cannot be made before tonight.

One hygiene defect was found and fixed during this check. Three never-deployed local modules
duplicated the consolidated materializer and wrote a conflicting arm-C name
(`C_TOP10_TRAILING_BT` instead of `C_TOP10_PRETRIAL_BT`) into the same
`v10869_m2_roster_ab_daily` table. They were backed up and removed, leaving exactly one
measurement writer. No production file, table value or hash changed.

## Publication references

- Private code/governance: `92cdc9f`.
- Private report/Notion lineage: `4c54969`.
- Public report: `b7b9171`.
- Notion page: `3aa1d385-9bf8-81f1-b83f-fa2d970f8529`.
- Enhanced private controls: `914106a`.
- Enhanced private lineage: `caa72ce`.
- Enhanced public evidence: `5e376bb`.

