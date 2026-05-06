# V54 Code Readiness Matrix

| ID | Item | V54 status | Bucket | Notes |
|---|---|---|---|---|
| C-02 | API source labels | DONE | `IMPLEMENT_NOW_UI_TEST_ONLY` | Added response metadata to `/api/du-doan-test/{region}` and MB legacy endpoint. |
| C-03 | Multi-region closeout evaluator | NOT DONE | `WAIT_3_5_CLEAN_CLOSEOUTS` | V50 evaluator MB-only; wait after V54 live watch + 3 manual closeouts. |
| C-04 | Scheduler auto-wire | NOT DONE | `WAIT_3_5_CLEAN_CLOSEOUTS` | No scheduler official job touched. |
| C-05 | Per-model latency instrumentation | PLAN ONLY | `IMPLEMENT_NOW_MEASUREMENT_ONLY` | Not deployed before live cascade because `gpt_analyzer.py` is live model-call path. |
| C-06 | Loz stage trace | DONE | `IMPLEMENT_NOW_MEASUREMENT_ONLY` | New `loz_stage_trace_shadow`, 6174 rows over 60 closed days. |
| C-07 | MT correct-but-dropped UI panel | PLAN ONLY | `IMPLEMENT_NOW_UI_TEST_ONLY` | Backend data ready: `mt_model_hit_output_drop_shadow` + new `loz_stage_trace_shadow`. |
| C-08 | Model roster pruning | NOT DONE | `WAIT_30D_LATENCY_AND_SIGNAL` | Blocked by `NO_PER_MODEL_DURATION`. |
| C-09 | Loz output policy change | NOT DONE | `WAIT_14_VALID_LIVE_DAYS` | New trace shows many misses are NOT_IN_MODEL_OUTPUT, so no simplistic loz rule. |
| C-10 | Composite V2 promote | NOT DONE | `WAIT_30D_LATENCY_AND_SIGNAL` | Gate not met; still test-only. |
| C-11 | Single-vote rescue | NOT DONE | `LEAKY_REFERENCE_ONLY` | V37 remains dropped. |
| C-12 | Sunday retrain promotion | NOT DONE | `OWNER_DECIDE` | Needs shadow proof + owner OK. |
| C-13 | Strength-aware roster test lane | NOT DONE | `WAIT_3_5_CLEAN_CLOSEOUTS` | After C-05 latency and evaluator. |
| C-14 | Strength chips UI | PLAN ONLY | `IMPLEMENT_NOW_UI_TEST_ONLY` | Tensor data ready; UI next. |
| C-15 | Weekday blackspot alert | DONE | `IMPLEMENT_NOW_MEASUREMENT_ONLY` | New `weekday_blackspot_shadow`, MB Wed/Fri + MT Mon/Fri confirmed. |

Official output mutation: NONE by V54 code. Official table timestamp refresh occurred due service restart startup catch-up and is tracked separately.
