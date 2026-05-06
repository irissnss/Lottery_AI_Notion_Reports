# DU-DOAN-TEST V49 FULL REPORT RE-READ + LIVE-PARALLEL CONTROL

> Date: 2026-05-03, audit time 12:41–12:55 +07  
> Mode: VPS-first / controller-grade audit / no pass-wash / no official output mutation  
> Sync manifest: `artifacts/live_sync/20260503_124229/manifest.json`  
> Raw DB audit: `artifacts/_v49_audit_out.json`  
> Route smoke: `artifacts/_v49_route_smoke_out.txt`  
> Pre-hash: `artifacts/_du_doan_test_v49_pre_hash_20260503.txt`  
> Post-hash: `artifacts/_du_doan_test_v49_post_hash_20260503.txt`

---

## 1. Executive summary

Final status label: **`MANUAL_STAGE_0_CONFIRMED`**.

`/du-doan-test` is a real admin-only MB test lane with route/API/UI/schema/engine/manual runner and persisted 2026-05-02 rows, but it is **not** live-parallel auto. It has **0 scheduler markers**, **0 scheduler.py references**, and **0 rows for 2026-05-03**. It also is not a true 25-model realtime lane yet: 25 production models predicted MB 2026-05-02, but only 14 voter models enter `du_doan_test_candidates`. AI test prompt execution is not active (`du_doan_test_ai_predictions` does not exist; 0 `is_test_prompt=1`). V48 claims are present and audited; V48 is **not missing**.

Official `/du-doan` is untouched: `/du-doan` HTTP 200, `/api/final-bundle` HTTP 200, `/du-doan-test` unauth 401, `/api/du-doan-test/mb` unauth 401. Test code has no scheduler auto-wire. This V49 pass is read-only and made no production DB writes.

---

## 2. Full attached report re-read confirmation

Read fully:

- `artifacts/phase_checkpoints/DU_DOAN_TEST_V48_START_LIVE_PARALLEL_COMPLETION_20260503.md` — all 707 lines.
- Governance: `docs/ACTIVE_ROADMAP_CROSS_REGION_LEAKAGE.md`, `docs/CURRENT_TRUTH_SSOT.md`, `docs/FOLLOW_UP_TRACKER.md`, `docs/CHANGELOG_GOVERNANCE_LEDGER.md`, `CHANGELOG.md`.
- V46/V48 artifacts: `DU_DOAN_TEST_FULL_MODEL_TENSOR_MB_RECOVERY_20260503.md`, `_du_doan_test_full_tensor_state_20260503.json`, `_official_baseline_closeout_20260502.json`, `_du_doan_test_full_engine_vps_run_20260503.txt`, full tensor CSV, V46 pre/post hashes.
- Code: `main.py`, `scheduler.py`, `_du_doan_test_mb_engine.py`, `_du_doan_test_daily_runner.py`, `_materialize_mb_experimental_preview_shadow.py`, `model_registry.py`, `gpt_analyzer.py`, `du-doan-test.html`.

---

## 3. Embedded V48 extraction summary

Transcript grep found the embedded marker:

`TOTAL-FORCE V48 — KẾT QUẢ ĐẦY ĐỦ`

Therefore label is **`V48_EMBEDDED_REPORT_PRESENT`**. The forbidden label `V48_REPORT_NOT_FOUND` is not used.

Core embedded V48 claims extracted:

- `/du-doan-test` not auto live, status `MANUAL_TEST_LANE`.
- Official `/du-doan` untouched.
- Admin-only access 401 unauth.
- 2026-05-03 start-live: MN has BT=79 PENDING; MT/MB no today final bundle; test today 0 rows.
- 7 experiments are not independent pipelines.
- 25-model realtime not proven (14 voter models only).
- AI test prompt not executing.
- MB recovery not owner-review-ready.

---

## 4. V48 claim verification table

| Claim | V48 text basis | Verification | Verdict |
|---|---|---|---|
| V48 exists / embedded present | Transcript has `TOTAL-FORCE V48 — KẾT QUẢ ĐẦY ĐỦ` | `rg` over agent transcript found marker | **VERIFIED** |
| `/du-doan-test` admin-only | V48 §4 | route smoke: `/du-doan-test=401`, `/api/du-doan-test/mb=401` unauth | **VERIFIED** |
| `/du-doan` unaffected | V48 §3 | `/du-doan=200`, `/api/final-bundle MB=200`, no test write path in main.py | **VERIFIED** |
| Current status not auto | V48 §9 | scheduler marker count 0; scheduler.py references none; 2026-05-03 test rows 0 | **VERIFIED** |
| 2026-05-02 test rows exist | V48 §7 | DB: runs=7 bundles=7 results=7 candidates=147 contribution=147 | **VERIFIED** |
| 7 methods not independent | V48 §8 | all share same candidate set `[12,28,30,43,63,79,80,91]` and 14 voter models | **VERIFIED** |
| 25-model realtime not proven | V48 §12 | production model count=25, test contribution model count=14 | **VERIFIED** |
| AI test prompt not executing | V48 §13 | no table `du_doan_test_ai_predictions`; 0 `is_test_prompt=1`; prompt variant clone only | **VERIFIED** |
| Prior-region no leakage | V48 §15 | code uses MN(D)+MT(D), not MB(D), for selection | **VERIFIED** |
| 30-day backtest not persisted live | V48 §18 | preview rows only 7 rows / one date; API backtest is hardcoded artifact summary | **VERIFIED** |

---

## 5. Files/docs/code/artifacts read

See §2. No required file critical to V49 was missing. Some earlier optional V39/V41 artifact filenames are absent under exact names, but their evidence is covered by CHANGELOG, SSOT, and existing V41/V47/V48 summaries. Impact: none for current `/du-doan-test` classification.

---

## 6. VPS sync manifest

Latest sync:

- `artifacts/live_sync/20260503_124229/manifest.json`
- DB remote/local after sha: `0a1c1e20647074c1933f3741d0d434508711b0df600184b9ba2203684204c0d0`
- prediction_trace sha: `bfe6c34df852c032817e515c56d8074f765d51b3a0fd9378be6c286ac8199c82`

---

## 7. Pre-hash source guard

Captured in `artifacts/_du_doan_test_v49_pre_hash_20260503.txt`.

Important rows:

- `predictions`: 4098, max_date 2026-05-03
- `final_bundles`: 193, max_date 2026-05-03
- `lottery_results`: 14596, max_date 2026-05-02
- `model_daily_eval`: 4014, max_date 2026-05-02
- `scheduler_logs`: 112612, max_date 2026-05-03
- `du_doan_test_runs`: 7, min=max 2026-05-02
- `mb_experimental_preview_shadow`: 7, min=max 2026-05-02
- replay/shadow tables current through 2026-05-02 except leaky `single_vote_rescue_replay_shadow` max 2026-05-01.

---

## 8. Start-live 2026-05-03 readiness

| Region | Predictions | Run sources | Final bundle | Results |
|---|---:|---|---|---:|
| MN | 25 | 15 auto_daily + 10 shadow_auto_eval | BT=79, lo2=[79,96], status PENDING | 0 |
| MT | 7 | auto_daily only | none today, API falls back 2026-05-02 BT=88 | 0 |
| MB | 7 | auto_daily only | none today, API falls back 2026-05-02 BT=43 | 0 |

Scheduler latest live markers are MN 2026-05-03 AI/shadow markers at `2026-05-02 21:24–21:33`. This is expected for early/live-day state. MT/MB are waiting for cascade after MN/MT results.

---

## 9. Official `/du-doan` integrity proof

Official path:

`/du-doan` → `web/frontend/du-doan.html` → `GET /api/final-bundle` → `final_bundles`.

Verified:

- `/du-doan=200`
- `/api/final-bundle?region=MB=200`
- `generate_final_bundle()` remains separate under `POST /api/generate-bundle`.
- `_du_doan_test_mb_engine.py` does not call `generate_final_bundle()`.
- `_du_doan_test_mb_engine.py` does not write `final_bundles` or production `predictions`.
- scheduler.py has no `du_doan_test` references.

Unsafe mutation: **NO**.

---

## 10. `/du-doan-test` architecture map

`/du-doan-test` → `web/frontend/du-doan-test.html` → `/api/du-doan-test/mb`.

API reads:

- `mb_experimental_preview_shadow`
- `du_doan_test_bundles` + `du_doan_test_results`
- `final_bundles` MB baseline read-only
- `lottery_results` MB for status

Writers are not in the API. Writers are manual:

- `_materialize_mb_experimental_preview_shadow.py`
- `_du_doan_test_mb_engine.py`
- `_du_doan_test_daily_runner.py` wrapper

UI markers present: Test Lane, admin/dev, final_bundles no-write warning, compare-grid, renderAxisCard, v48.1.

---

## 11. `du_doan_test_*` schema audit

All current required columns used by the existing implementation are present.

Blocking gaps for future live-parallel auto:

- `du_doan_test_bundles` lacks `test_lo3`, `test_xien2`, `test_xien3` persisted columns. UI derives those through API only.
- No `du_doan_test_method_scoreboard`.
- No `du_doan_test_ai_predictions`.
- No explicit `source_date`, `source_tables`, `does_not_write_final_bundles`, `leakage_audit`, `source_available_at`, `target_cutoff_time`.

Population gaps:

- `strength`, `strength_bin`, `verdict`, `candidate_latency_sec`, `cost_estimate` are 147/147 NULL in candidates.
- `du_doan_test_model_contribution.latency_sec` is 147/147 NULL.

Classification: **SCHEMA_GAP_NON_BLOCKING for manual lane**, **SCHEMA_GAP_BLOCKING for owner-review-ready / auto-live evidence**.

---

## 12. V46 claim verification

V46 counts verified:

- runs=7
- bundles=7
- results=7
- candidates=147
- model_contribution=147
- audit_log=1

V46 bundle outputs verified:

- baseline=43
- composite=91
- tier-aware=91
- AI-chain=91
- specialist=null
- prior-region=91
- no-token-herd=91

V46 foundation is **VERIFIED** at schema/engine/manual-run level, but **not** auto-live.

---

## 13. V48 claim verification

V48 claims remain current after V49 sync. No new test rows were generated between 10:16 and 12:42. The status remains manual.

---

## 14. MB 2026-05-02 output analysis

Official:

- MN BT=73 WIN, lo2 WIN
- MT BT=88 WIN, lo2 PARTIAL
- MB BT=43 LOSE, lo2 `[43,91]` PARTIAL

MB test:

- Five challengers promote 91 to BT and would save BT.
- This is a real BT save vs official BT=43.
- But official lo2 already contained 91, so it is also a **lo2-to-BT promotion**, not discovery of a number absent from official output.
- Not enough to call production improvement; 1 day persisted only.

Gate: not met for persisted live-parallel. Artifact backtest composite +3/30 is below +4/30 gate.

---

## 15. Why many experiments output 91

All experiments use same candidate set and same candidate source payload. `91` had rank=2, score close to top1, and 5 AI-chain votes. Different transforms picked the same strong runner-up. This is **partially shared signal**, not independent multi-method proof.

Verdict: `NOT_INDEPENDENT_YET` for 5 challengers as independent pipelines; `PARTIALLY_SHARED_SIGNAL` as transforms.

---

## 16. AI test prompt status

Status: **`AI_TEST_PROMPT_DESIGNED_NOT_EXECUTING`**.

Evidence:

- `du_doan_test_ai_predictions_exists=false`
- `is_test_prompt_rows=0`
- all 147 candidates have `prompt_variant='production_prompt_clone_or_none'`
- production prompt in `gpt_analyzer.py` unchanged.

---

## 17. 25-model realtime vs diagnostic status

Status: **`NOT_25_MODEL` / `TENSOR_ONLY for 11 shadow models`**.

Evidence:

- 25 MB prediction models exist for 2026-05-02.
- 14 distinct models appear in test contribution.
- 11 missing are shadow_auto_eval or non-final-voter rows.

Do not call it 25-model realtime test until raw-25 ingestion exists and timestamps prove realtime cutoff.

---

## 18. No-token clone/herd audit

`MB_NO_TOKEN_HERD_REDUCTION_V1` is **LOGICAL_CLONE_ONLY / shared-source transform**. It applies a score penalty/bonus over candidate payload; it does not rerun no-token models or create a separate no-token candidate universe.

---

## 19. Prior-region safe no-leakage audit

Verdict: **`PARTIAL_LEAKAGE_PROOF` leaning `NO_LEAKAGE_VERIFIED` for code path**.

Code uses MN(D)+MT(D), not MB(D), for selection. However schema does not persist `source_available_at`, `target_cutoff_time`, or `leakage_audit`, so row-level future forensic proof is partial.

---

## 20. Model capability tensor quality audit

Tensor exists:

- rows=3216
- date_count=61
- region_count=3
- model_count=37
- provider_unknown=103
- status_unknown=103
- station_set_blank=2867
- prompt_version_blank=2562
- latency_no_per_model_duration=3216
- latency_seconds_blank=3216

Verdict: enough for diagnostics, **not enough for pruning/right-sizing**. `NO_MODEL_PRUNING_DECISION_ALLOWED`.

---

## 21. MB recovery scoreboard

Persisted live-test evidence:

- preview_rows=7 total, only 1 date (2026-05-02).
- Five challengers each 1/1 test win, but one day only.

Backtest claim:

- composite 8/30 vs official 5/30 = +3/30, below +4/30 gate.

Verdict: **TEST_ONLY_GATE_NOT_MET**.

---

## 22. Shadow/replay/test/tensor separation

| Surface | Purpose | Output impact | Unlock eligible |
|---|---|---|---|
| `du_doan_test_*` | admin MB test output/history/eval | false | not yet |
| full tensor CSV | diagnostic model matrix | false | no, due latency gaps |
| `single_vote_rescue_replay_shadow` | leaky reference | false | **never** |
| `tier2_replay*` | policy replay | false | no, dropped |
| `corrected_rescue_replay_shadow` | non-leaky replay accumulation | false | not yet |
| P0 shadow tables | measurement | false | not output |

---

## 23. True live-parallel status classification

Final label: **`MANUAL_STAGE_0_CONFIRMED`**.

Not auto because:

- no scheduler marker
- no scheduler.py reference
- no 2026-05-03 rows
- no automatic pending/eval split
- no post-closeout automatic evaluation for today

---

## 24. Completion plan manual Stage 0 → auto

Stage A: run 2–3 manual daily cycles after MB closeout.  
Stage B: upgrade runner with `--region`, `--mode realtime_available_only/evaluate`, pre/post hash, audit log append, markers.  
Stage C: owner-approved scheduler auto-wire only after clean manual cycles.  
Stage D: daily evidence pack with official/test/delta/hash/UI/API proof.

---

## 25. Live watch 2026-05-03

Created: `artifacts/live_watch/LIVE_WATCH_20260503.md`.

Current watched state:

- MN AI + shadow done.
- MT/MB pending cascade.
- No `/du-doan-test` action until MB final bundle exists.

---

## 26. Post-closeout materializer plan

After MB closeout, run safe measurement materializers for 2026-05-03:

- cross-region spillover
- model cross-region dup
- bundle universe coverage
- mb structural drilldown
- strength calibration
- corrected rescue replay

Skip leaky single-vote rescue for unlock.

Then run test lane manually if owner approves:

```bash
python web/backend/_du_doan_test_daily_runner.py --date 2026-05-03 --dry-run --json
python web/backend/_du_doan_test_daily_runner.py --date 2026-05-03 --json
```

---

## 27. Risk register

| Risk | Severity | Status |
|---|---|---|
| route mistaken as completion | high | controlled by final label |
| many 91 mistaken independent | high | audited shared-source |
| 25-model overclaim | high | corrected 14/25 |
| AI prompt overclaim | high | designed-not-executing |
| test mistaken official | high | admin 401 + labels |
| latency missing | medium | blocks pruning |

---

## 28. Wait-data / owner-lock / drop list

Wait data:

- 3–5 manual closeouts before scheduler proposal.
- 14+ persisted test days before owner review.
- 30 days before production discussion.

Owner-lock:

- scheduler auto-wire
- AI test prompt execution
- production scoring/model/prompt/roster changes
- any `/du-doan` promotion

Drop / do not use:

- leaky single-vote rescue replay for unlock
- V2 tier2 policies as designed
- one-day persisted result as promotion proof

---

## 29. Docs/tracker/changelog sync

Updated in V49 session:

- `CHANGELOG.md` V20.3.37.49
- `docs/CURRENT_TRUTH_SSOT.md` V49 row
- `docs/CHANGELOG_GOVERNANCE_LEDGER.md` V49 row
- `docs/FOLLOW_UP_TRACKER.md` FU-097/FU-100/FU-102 notes refined
- `docs/ACTIVE_ROADMAP_CROSS_REGION_LEAKAGE.md` note added for V49 status

---

## 30. Technical no-drop self-audit

All checked: full report re-read, embedded V48 extracted, VPS sync first, pre-hash, official/test map, schema, counts, 91 audit, AI prompt, 25-model, no-token, prior-region, tensor, live readiness, live watch, post-hash, route smoke, docs sync.

---

## 31. Governance no-overclaim self-audit

No claim that:

- route = complete
- rows = value proof
- many 91 = independent proof
- 25-model realtime is active
- AI test prompt executed
- test is production-ready
- auto live parallel is active

No official mutation performed.

---

## 32. Final owner-facing answer

See chat final for direct 22 answers. Final status label: **`MANUAL_STAGE_0_CONFIRMED`**, not auto.
