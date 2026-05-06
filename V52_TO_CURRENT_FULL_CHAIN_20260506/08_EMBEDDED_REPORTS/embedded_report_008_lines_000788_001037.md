    ### FU-080 — 2026-05-01 post-live TOTAL-FORCE closeout (consolidated)

    | Field | Value |
    |-------|-------|
    | **issue_id** | FU-080 |
    | **title** | Closeout artifact + tracker reconciliation for the 2026-05-01 TOTAL-FORCE pass |
    | **current_truth** | The 2026-05-01 TOTAL-FORCE closeout is consolidated in `artifacts/phase_checkpoints/POST_LIVE_TOTAL_FORCE_CROSS_REGION_SPILLOVER_CLOSEOUT_20260501.md` (15 sections). 3/3 regions LOSE today (MN BT=51 LOSE BUNDLE_SKEW; MT BT=16 LOSE BUNDLE_SKEW; MB BT=94 LOSE CANDIDATE_SPLIT). Owner examples 17/46/91/23 verified per-prize-key/station. Cross-region spillover at per-tail level over 60 days (9428 rows) is at-or-below random baseline; bundle-level elevation comes from narrow universe (14-20%) + extreme vote concentration (MB 14/25 herd 74). cross_region_spillover_shadow_v1 deployed locally with backfill 60d. P0 verifier `NATURAL_CLOSEOUT_PROVEN` for 2026-05-01. Source-table hashes UNCHANGED before/after action. |
    | **evidence** | `artifacts/phase_checkpoints/POST_LIVE_TOTAL_FORCE_CROSS_REGION_SPILLOVER_CLOSEOUT_20260501.md`; `artifacts/_spillover_data_out.txt`; `artifacts/_candidate_lifecycle_out.txt`; `artifacts/_p0_verifier_20260501.json`; `artifacts/_pre_action_hash_out.txt`+`_post_action_hash.txt`; `artifacts/live_sync/20260501_201308/manifest.json`; CHANGELOG V20.3.37.32; SSOT V20.3.37.32 row |
    | **impact** | Provides the single owner-readable post-live closeout for 2026-05-01 with Vietnamese 15-section report including current VPS truth, output truth, spillover findings, random baseline comparison, no-token/AI/rule/prompt audits, candidate lifecycle, bundle-skew root cause, P0/method portfolio status, safe fixes executed, wait-data/owner-decide/do-not-touch lists, and final verdict + next commands. |
    | **status** | DONE |
    | **next_action** | None for this FU. Owner pending decisions tracked in FU-076 (spillover VPS push), CP-1.1/CP-2.1 in active roadmap. |
    | **pass_condition** | The closeout artifact exists, references valid live truth, source-table hashes UNCHANGED, no `/du-doan` or scoring change. |
    | **fail_condition** | Closeout claims output-ready or owner-approved without explicit owner decision. |
    | **owner_decision_needed** | NO for the closeout itself; YES for VPS push of spillover materializer (see FU-076). |
    | **last_checked** | 2026-05-01T20:30:00+07:00 |
    | **notes** | This is the consolidated post-live deliverable for the 2026-05-01 cycle. Reconciles V20.3.37.30 bundle-level +18 pp finding with V20.3.37.32 per-tail -3.3 pp finding by explaining they measure different statistics. |

    ### FU-079 — Tier 1-4 real-code definition + usage audit

    | Field | Value |
    |-------|-------|
    | **issue_id** | FU-079 |
    | **title** | Document where production tiers are defined in code and how they flow into prompt / no-token / bundle |
    | **current_truth** | Production tiers are 4 labels in `web/backend/rule_engine.py` `BOOST_TABLE`: `READY_STRONG` (Tier 1), `READY_WITH_CAUTION` (Tier 2), `LIMITED_WEIGHT` (Tier 3), `REFERENCE_ONLY` (Tier 4). Tiers are computed from `cumulative_rank_score`, `composite_score`, `score`, `hr_12w`, `hr_16w`. Boost magnitudes per (tier, prediction_use): in `soft` mode 0.01-0.15; in `active` mode 0.03-0.35. `shadow` mode applies zero boost. Convergence boost: shadow=0, soft=0.10, active=0.20. Tier flows into prompt context via `analysis.top_source_prizes_by_region` and into no-token candidate scoring via `extract_rule_candidates_v2()`. Bundle layer is tier-blind (votes count, tier is evidence not weight). |
    | **evidence** | `web/backend/rule_engine.py` lines 49-71 (BOOST_TABLE); 73-75 (CONVERGENCE_BONUS, CONVERGENCE_MAX_TAILS); 220-282 (get_active_rules); 472-574 (extract_rule_candidates_v2 boost application) |
    | **impact** | Clarifies that "Tier 1/2/3/4" is shorthand. Bundle layer not using tier as weight is a known measurement-only observation; changing it is owner-locked under `generate_final_bundle()` lock. |
    | **status** | DONE |
    | **next_action** | None unless owner wants tier-aware bundle voting (would be a TIER 3 owner-unlock item). |
    | **pass_condition** | Documentation of real tier names and flow exists; matches code. |
    | **fail_condition** | Future doc drift uses "Tier 1/2/3/4" without naming the real constants. |
    | **owner_decision_needed** | NO |
    | **last_checked** | 2026-05-01T20:30:00+07:00 |
    | **notes** | Tier names anchored here for future agent re-use; closeout report §8.1 cross-references this entry. |

    ### FU-078 — Source-prize D/D-1 candidate survival audit

    | Field | Value |
    |-------|-------|
    | **issue_id** | FU-078 |
    | **title** | Verify owner-strong tails 17/46/91/23 are present in source-prize chain D/D-1 and trace to bundle |
    | **current_truth** | Source-prize chain (G1/G2/G5/G7/G8/DB) for 2026-04-30 (D-1) and 2026-05-01 (D) verified to contain owner-strong tails: 91 in MT D-1, MN D, MT D, MB D; 23 in MN D-1, MN D, MT D; 17 in MT D-1, MT D; 46 in MN D-1. Source-prize chain is clean. Chain is referenced by REASONING_RULEBOOK (RR-§10A), required by validation gate (`analysis.top_source_prizes_by_region` non-empty). Drop sites identified: 91 dropped at strength<5.0 SKIP gate; 23 dropped at 1-vote bundle gate; 17 included in MN bundle lo2 but MN itself missed; 46 included in MT bundle lo2 but MT itself missed. |
    | **evidence** | `artifacts/_source_prize_strong_out.txt`; `artifacts/_audit_source_prize_strong.py`; `artifacts/_audit_candidate_lifecycle.py` output; closeout report §4 + §8.3 + §10 |
    | **impact** | Documents that the data layer is healthy. The bottleneck is verdict gate + bundle vote concentration, not data ingestion. |
    | **status** | DONE |
    | **next_action** | If owner wants to fix at source: candidate would be TIER 3 unlock for "single-vote rescue gate" or "tier-aware bundle weight" (locked). |
    | **pass_condition** | Source-prize chain confirmed clean; downstream drop sites identified for owner's specific examples. |
    | **fail_condition** | Future agent claims data is missing without tracing through chain. |
    | **owner_decision_needed** | NO |
    | **last_checked** | 2026-05-01T20:30:00+07:00 |
    | **notes** | Cross-link FU-073 (cross_region_spillover_shadow_v1), FU-077 (no-token rerun cascade). |

    ### FU-077 — No-token rerun cascade + spillover hot-spot

    | Field | Value |
    |-------|-------|
    | **issue_id** | FU-077 |
    | **title** | Track no-token combo herd in rerun_post_mn / rerun_post_mt overriding AI lane + spillover MB->MN next-day |
    | **current_truth** | On 2026-05-01, `rerun_post_mn` lane (no-token) had 5 voters herd `16` for MT, overriding AI lane that proposed correct 91/30/75 (1 vote each, 2 main hits, 0 bundle votes). MB bundle picked `94` after 14 voters herded on `74` (also wrong). 60d per-family stat shows NO_TOKEN MB->MN spillover 49.0% vs random 43.5% (+5.5 pp; small but consistent), highest of all family/pair combinations. SHADOW MB->MN 50.6%, AI_ACTIVE 38.6%. `no_token_drift_guard_v1` shadow has 15 rows for 2026-05-01 (healthy). |
    | **evidence** | `artifacts/_spillover_data_out.txt` per-family table; `artifacts/_audit_candidate_lifecycle.py` output; closeout report §6 + §11 |
    | **impact** | Identifies a measurement-only signal that NO_TOKEN MB->MN next-day pair has slight elevation worth tracking. Does not change runtime. |
    | **status** | MEASURED_BUT_NOT_FIXED |
    | **next_action** | Continue logging via `cross_region_spillover_shadow_v1` table; owner may unlock TIER 3 `lane_diverse_voting` to reduce no-token combo herd dominance after evidence pack. |
    | **pass_condition** | Trend data continues to grow; reaches 30d sample for owner-grade evaluation. |
    | **fail_condition** | Pattern is just noise that disappears with more data. |
    | **owner_decision_needed** | YES eventually for any TIER 3 fix (post 2026-05-19 evidence pack). |
    | **last_checked** | 2026-05-01T20:30:00+07:00 |
    | **notes** | Cross-link FU-073, FU-076. |

    ### FU-076 — cross_region_spillover_shadow_v1 measurement-only deploy

    | Field | Value |
    |-------|-------|
    | **issue_id** | FU-076 |
    | **title** | Deploy `cross_region_spillover_shadow_v1` as standalone shadow-only measurement; backfill; eventually push to VPS |
    | **current_truth** | Standalone materializer `web/backend/_materialize_cross_region_spillover_shadow.py` implemented and compile-OK. Schema for new table `cross_region_spillover_shadow` ensured via `CREATE TABLE IF NOT EXISTS`. Backfilled 60 days into LOCAL synced DB only (9428 rows from 2026-03-03..2026-05-01) with run_label `backfill_cross_region_spillover_<date>`. All rows `output_eligible=0, diagnostic_only=1, shadow_only=1, owner_approved=0`. Source-table hashes (predictions, final_bundles, lottery_results, model_daily_eval, scheduler_logs) verified UNCHANGED before/after backfill. NOT YET wired into P0 portfolio loop on VPS — separate VPS deploy item awaiting owner OK. |
    | **evidence** | new file `web/backend/_materialize_cross_region_spillover_shadow.py`; backfill log `artifacts/_spillover_backfill_60d.json`; data audit `artifacts/_spillover_data_out.txt`; pre/post hash `artifacts/_pre_action_hash_out.txt` + `_post_action_hash.txt`; CHANGELOG V20.3.37.32; SSOT V20.3.37.32 row |
    | **impact** | Provides the durable measurement surface for the cross-region spillover question. Local-only deploy means VPS production behavior is completely unaffected. After VPS push (separate owner OK), each natural closeout will write fresh rows. |
    | **status** | DEPLOYED_LOCAL_ONLY |
    | **next_action** | Owner OK to push to VPS: backup, py_compile remote, register in P0 portfolio (add to `P0_METHODS` in `_materialize_multi_lane_shadow_p0.py` OR keep standalone), wire into scheduler closeout chain, smoke test, source-hash compare on VPS pre/post. Until owner OK, table exists locally only. |
    | **pass_condition** | After VPS push: table exists on VPS; first natural closeout writes rows; P0 verifier sees method registered; source-table hashes UNCHANGED on VPS. |
    | **fail_condition** | VPS deploy mutates source tables; or method goes output_eligible without owner approval; or rows are interpreted as "live signal" instead of measurement. |
    | **owner_decision_needed** | YES for VPS push. |
    | **last_checked** | 2026-05-01T20:30:00+07:00 |
    | **notes** | Cross-link FU-073 parent issue. Method registration pattern follows existing P0 methods (see `web/backend/_materialize_multi_lane_shadow_p0.py` line 315 P0_METHODS for reference). VPS deploy is a separate session per `.Antigravityrules.md` deploy chain. |

    ### FU-073 — Cross-region spillover shadow measurement (MN->MT/MB, MT->MB)

    | Field | Value |
    |-------|-------|
    | **issue_id** | FU-073 |
    | **title** | Track whether tails that miss in an earlier region but hit a later same-day region are systematic signal or natural overlap |
    | **current_truth** | UPDATED 2026-05-01T19:25 (V20.3.37.30): Owner identified concrete examples on 2026-05-01: MN prediction `17` missed MN but appeared in MT, and MT prediction `46` missed MT but appeared in MB. Two passes of read-only audit now exist. (a) V20.3.37.29 first pass: in the latest 30d window across `3553` predicted tail items, `935` had downstream same-day hits (`26.32%`), `502` were downstream-only (`14.13%`); by pair `MN->MT=399`, `MN->MB=256`, `MT->MB=280`. (b) V20.3.37.30 deeper pass against random baseline: bundle-level `MN->MT BT_leak=53.3%` vs random `35.3%` (+18.0 pp), `MT->MN BT_leak=57.9%` vs random `43.8%` (+14.1 pp), `MT->MB BT_leak=15.8%` (below baseline; lo2_leak 26.3% slight elevation), `MB->MN next-day lo2_leak=54.2%`. Same-model cross-region duplication 14d = `MN/MT 17.2%`, `MN/MB 17.8%`, `MT/MB 20.3%` vs random ~4% -> 4-5x baseline. AI / NO_TOKEN / SHADOW families all show 36-47% leak rate on missed picks -> NOT a single-lane bug. Root-cause hypothesis confirmed: H1 shared-context cross-region herding (primary), H2 `weighted_voting_wr` bundle aggregation amplifies herd over dispersed correct signal (secondary, drives `BUNDLE_SKEW`), H3 universe coverage too narrow at 14-20% per region per day (tertiary). All 7 output policies picked `bt=16` for MT today -> output policy layer cannot rescue when input universe is herded wrong; the upstream candidate generation is the bottleneck. |
    | **evidence** | V20.3.37.29 first pass: `artifacts/db_audit_20260501/_post_live_cross_region_total_audit.py`; output `artifacts/db_audit_20260501/post_live_cross_region_total_audit.json`; D/D-1 source-prize audit `artifacts/db_audit_20260501/_source_prize_d_d1_cross_region_audit.py`; output `artifacts/db_audit_20260501/source_prize_d_d1_cross_region_audit.json`; report `artifacts/phase_checkpoints/SOURCE_PRIZE_D_D1_CROSS_REGION_AUDIT_20260501.md`. V20.3.37.30 deeper pass: `artifacts/_audit_q1.py`, `artifacts/_audit_cross_region_leakage.py`, `artifacts/_audit_source_prize_strong.py`, `artifacts/_audit_bundle_anti_trap.py`, `artifacts/_audit_cross_region_dup_rules.py`, `artifacts/_audit_winrate_summary.py`; live sync `artifacts/live_sync/20260501_190852/manifest.json`; consolidated owner report `artifacts/phase_checkpoints/TOTAL_FORCE_CROSS_REGION_LEAKAGE_AUDIT_20260501.md`. No DB writes or runtime changes in either pass. |
    | **impact** | Confirmed structural root-cause of the perceived "wrong region / next-region hit" behavior. Affects all 3 model families (AI, no-token, shadow). Not currently an output signal and must not change `/du-doan` until replayed and proven. The fix path requires (TIER 1) measurement-safe diagnostic surfaces, (TIER 2) replay-only candidate policies, and only then (TIER 3) owner-unlocked region-isolation in prompt + lane-diverse bundle aggregation. |
    | **status** | MEASURED_BUT_NOT_FIXED |
    | **next_action** | **All work for this initiative is now scheduled in `docs/ACTIVE_ROADMAP_CROSS_REGION_LEAKAGE.md` with hard deadlines and auto-action thresholds (V20.3.37.31).** Immediate items awaiting owner OK: CP-1.1 (TIER 1 deploy 5 measurement surfaces) by 2026-05-04; CP-2.1 (TIER 2 replay launch 4 policies) by 2026-05-04. After owner OK, agent self-executes CP-1.2 .. CP-2.5 over 14d. Evidence pack at CP-2.5 target 2026-05-19. Owner decides T3 unlocks at CP-3.0 by 2026-05-26. TIER 4 sample maturity check at CP-4.0 by 2026-06-15. The Cursor rule `.cursor/rules/active-roadmap-precedence.mdc` enforces that any future session reads the roadmap file and surfaces overdue checkpoints at the top of the first reply. |
    | **pass_condition** | After at least 14 compatible closed days of TIER 1+2 measurement, evidence pack shows: (a) at least one TIER-2 policy delivers `+5 pp BT_WIN` lift over baseline AND `false_promotion < 3%` AND `flips_to_lose < flips_to_win`, OR (b) cross-region leakage trends down naturally as we close more closeouts. |
    | **fail_condition** | TIER 1 deploy breaks any existing measurement surface, TIER 2 replay shows all policies regress on backtest, or any TIER 3 idea is deployed without explicit owner unlock and 14d replay proof. |
    | **owner_decision_needed** | YES for TIER 1 deploy approval (this session). YES for TIER 2 replay launch (this session, low risk). YES for any TIER 3 unlock (after evidence pack 2026-05-06). |
    | **last_checked** | 2026-05-01T19:55:00+07:00 |
    | **notes** | This is the direct tracker item for the owner's MN->MT and MT->MB observation. V20.3.37.30 escalated from `NOT_YET_PROVEN` to `MEASURED_BUT_NOT_FIXED` because the leakage is now quantified above random baseline (18 pp / 14 pp on the MN<->MT axis). V20.3.37.31 added dedicated `docs/ACTIVE_ROADMAP_CROSS_REGION_LEAKAGE.md` with 12 checkpoints, hard deadlines, and auto-action thresholds, plus Cursor rule `.cursor/rules/active-roadmap-precedence.mdc` to enforce that any future session reads the roadmap and surfaces overdue items at the top of the first reply. Recommendation unchanged: measure deeply; do not use in `/du-doan` until replay shows positive lift without false-promotion risk. |

    ### FU-075 — D-2 expanded ruleset foundation HOLD / REFERENCE_ONLY / OWNER_LOCK / NOT_OUTPUT_READY

    | Field | Value |
    |-------|-------|
    | **issue_id** | FU-075 |
    | **title** | Park D-2 expanded-ruleset active engineering: HOLD / REFERENCE_ONLY / OWNER_LOCK / NOT_OUTPUT_READY |
    | **current_truth** | D-2 = HOLD / REFERENCE_ONLY / OWNER_LOCK / NOT_OUTPUT_READY. The bounded foundation replay (latest 14 closed days, `2026-04-17..2026-04-30`) did not pass the continuation gate: all MN/MT/MB regions hit `NOISE_RISK`, D-2 top1 declined versus D-1 (`52.38% -> 40.48%` overall; MN `78.57% -> 71.43%`; MT `42.86% -> 28.57%`; MB `35.71% -> 21.43%`), candidate pool inflated heavily (`10.29 -> 41.05`), and overall `would_save_simple=8` did not beat `would_break_simple=9`. Active D-2 engineering is stopped. No Phase B. No live shadow. No P0 registry addition. No prompt / no-token / model / output integration. No code, no deploy, no production DB write. Reopen requires explicit owner decision. |
    | **evidence** | `artifacts/phase_checkpoints/D2_FOUNDATION_HOLD_DECISION_20260501.md`; `artifacts/d2_foundation/d2_minimum_metrics_20260501.json`; `artifacts/d2_foundation/d2_foundation_self_audit_20260501.json`; `artifacts/replay/expanded_calendar_d2_ruleset_summary.json`; `artifacts/db_audit_20260501/d2_no_leak_proof.json`; `artifacts/phase_checkpoints/D2_MINIMUM_ARTIFACT_REPLAY_REPORT_20260501.md`; `artifacts/phase_checkpoints/D2_BASIC_REGION_VERDICT_20260501.md`; `artifacts/phase_checkpoints/D2_NEXT_PHASE_RECOMMENDATION_20260501.md`; `artifacts/phase_checkpoints/D2_OVERREACH_ROLLBACK_AUDIT_20260501.md`; `artifacts/phase_checkpoints/D1_RULE_MECHANISM_FULL_AUDIT_20260501.md`; `artifacts/phase_checkpoints/D2_EXPANDED_RULESET_SHADOW_SPEC_20260501.md`; `artifacts/phase_checkpoints/D2_LOCAL_REPLAY_REGION_DECISION_PACK_20260501.md`; `artifacts/phase_checkpoints/D2_ROLLBACK_REDESIGN_OWNER_REVIEW_SPEC_20260501.md`; one-off artifact runner removed after replay; `CHANGELOG.md` V20.3.37.27 / V20.3.37.28; SSOT V20.3.37.28. |
    | **impact** | Active D-2 implementation is stopped. No `/du-doan`, `final_bundles`, `predictions`, `lottery_results`, scoring, `BOOST_TABLE`, prompt runtime, no-token live, model roster, output eligibility, P0 registry, or scheduler production behavior change. Foundation evidence is preserved as guardrail-only artifacts. |
    | **status** | OWNER_LOCK |
    | **next_action** | No active D-2 implementation. No Phase B. No live shadow. No prompt/no-token/model/output integration. Revisit only if owner explicitly reopens with a new bounded hypothesis. |
    | **pass_condition** | If owner ever reopens D-2, the new effort must inherit the D-1 stack contract, run artifact-only first, and clear `NOISE_RISK` plus a `would_save > would_break` margin in a future bounded window before any shadow/live discussion. |
    | **fail_condition** | Any future work that adds D-2 to scheduler/P0 registry/prompt runtime/no-token live/output without a new owner decision. |
    | **owner_decision_needed** | YES to reopen any D-2 work; otherwise no owner action required. |
    | **last_checked** | 2026-05-01T11:13:00+07:00 |
    | **notes** | Governance final wording: D-2 = HOLD / REFERENCE_ONLY / OWNER_LOCK / NOT_OUTPUT_READY. Region verdicts: MN `MN_REFERENCE_ONLY`, MT `MT_REFERENCE_ONLY`, MB `MB_REFERENCE_ONLY` (close to `MB_DROP_FOR_NOW` due to highest noise). Cross-refs: DEC-021, DEC-022. |

    ### FU-074 — Auth lockdown for write/delete/compute endpoints exposed by viewer rollout audit

    | Field | Value |
    |-------|-------|
    | **issue_id** | FU-074 |
    | **title** | Lock down 15 write/delete/compute API endpoints to `require_admin` after the viewer-shell rollout audit |
    | **current_truth** | A safety audit of the viewer rollout found pre-existing auth gaps. Live probes confirmed `POST /api/rules/{id}/toggle` answered `200` without any cookie, and `POST /api/rules`, `PUT /api/rules/{id}`, `DELETE /api/rules/{id}` accepted unauthenticated requests at the route layer. Other endpoints only required login, not admin: `POST /api/predict/MN|MT|MB`, `POST /api/update/{region}`, `POST /api/sync/push`, `DELETE /api/predictions/{date}/{region}`, `POST /api/predictions/delete-batch`, `POST /api/generate-bundle`, `POST /api/backtest`, `POST /api/optimize-weights`, `POST /api/run-optimizer-now`, which let any logged-in viewer trigger writes or expensive compute. All 15 endpoints were upgraded to `require_admin` in `web/backend/main.py` and deployed; a live re-probe returned `401` on every endpoint without a session while `/user-view`, `/du-doan`, `/search`, and `/api/health` kept returning `200`. The single accidental toggle of `pattern_rules.id=1` during the probe was reverted in the same step. |
    | **evidence** | Updated handlers in `web/backend/main.py` for `api_create_rule`, `api_update_rule`, `api_delete_rule`, `api_toggle_rule`, `push_results`, `update_results`, `predict_mn`, `predict_mt`, `predict_mb`, `delete_single_prediction`, `delete_batch_predictions`, `run_backtest`, `optimize_weights_api`, `run_optimizer_now_api`, `api_generate_bundle`. Deploy log shows `lottery.service` `active (running)` after upload. Live re-probe results: 15/15 endpoints returned `401` with no cookie. Health, viewer pages, and admin pages still served `200`. `CHANGELOG.md` V20.3.37.25 records the lockdown. |
    | **impact** | Reduces blast radius from any viewer (or unauthenticated client for the rules endpoints) before this fix could be exploited via the new `/user-view` shell. No scoring, prediction execution, final bundle, model roster, output eligibility, scheduler, DB schema, `/du-doan`, `/search`, `/user-view`, or admin behavior change for legitimate admin sessions. |
    | **status** | DEPLOYED_PENDING_LIVE_VERIFY |
    | **next_action** | Owner uses an admin session to confirm `/api/predict/*`, `/api/update/{region}`, `/api/predictions/delete-batch`, `/api/predictions/{date}/{region}` (DELETE), `/api/generate-bundle`, and `/api/rules*` still work as expected for normal admin operation. Optional follow-up: cover read-only diagnostic endpoints (`/api/mined-rules/*`, `/api/prediction-trace`, `/api/prediction-advisory`, `/api/effectiveness`, `/api/reasoning`) with at least `get_current_user` if owner wants to gate strategy leakage. |
    | **pass_condition** | Live probes without a session keep returning `401` for the 15 endpoints, admin sessions can still operate normally, and viewer pages plus health remain `200`. |
    | **fail_condition** | Any of the 15 endpoints regress to allow viewer or unauthenticated writes; or admin operation breaks because of a wrong signature/dependency change. |
    | **owner_decision_needed** | NO for the deployed lockdown; YES before extending the same `require_admin` pattern to the read-only diagnostic GETs. |
    | **last_checked** | 2026-04-30T21:40:00+07:00 |
    | **notes** | Lockdown kept the existing `Depends(get_current_user)` parameter in place where present and added `require_admin(...)` so authentication still surfaces the same error envelope as the rest of the codebase. The `pattern_rules.id=1` accidental toggle during the audit was reverted by toggling once more before the lockdown deployed. |

    ### FU-073 — Compact `/user-view` preview for viewer users

    | Field | Value |
    |-------|-------|
    | **issue_id** | FU-073 |
    | **title** | Build a compact user-facing view derived from `/app` with a separate local preview link |
    | **current_truth** | A new `/user-view` route is deployed on VPS and the viewer shell is aligned around exactly three links: `/user-view` (`USER VIEW`), `/du-doan` (`Dự đoán`), and `/search` (`Tra cứu`). `/du-doan` and `/search` now render an explicit visible uppercase `USER VIEW` header button for returning to `/user-view`. `/user-view` is a compact read-only UI that keeps the `/app` structure users asked for: model/date controls, MN/MT/MB tabs, WR/backtest KPIs, current prediction, latest result tails, and filtered history. It intentionally removes admin/action controls: predict execution, update result, delete predictions, settings, monitoring, quality/admin panels, and refresh CTA. `Dashboard` remains hidden unless `/api/auth/check` returns admin. Viewer login is changed to land on `/user-view`; admin/non-viewer login lands on `/app`. The page also supports `user-view.html?mock=1` for static local layout preview when full FastAPI dependencies are unavailable on the workstation. |
    | **evidence** | `web/frontend/user-view.html`; `web/frontend/user-view.js`; `web/backend/main.py` route handlers for `/user-view` and `/user-view.js`; first deploy uploaded only those three web files; `lottery.service` active after restart; live checks `https://xs.io.vn/user-view=200`, `/user-view.js=200`, `/api/health=200`; second pass aligns `login.html`, `user-view.html`, `user-view.js`, `search.html`, and `du-doan.html`; safety grep found no delete/update/predict/admin controls in user-view and only logout POST; JS syntax OK; `CHANGELOG.md` V20.3.37.25; `docs/CURRENT_TRUTH_SSOT.md` viewer-shell row. |
    | **impact** | Viewer users get the requested three-link surface without admin/dev duplication. No scoring, prediction execution, final bundle, model roster, output eligibility, scheduler, DB schema, existing `/app`, or admin dashboard behavior changes. |
    | **status** | DEPLOYED_PENDING_LIVE_VERIFY |
    | **next_action** | Deploy visible uppercase `USER VIEW` return button pass and owner previews `https://xs.io.vn/user-view`, `https://xs.io.vn/du-doan`, and `https://xs.io.vn/search` as a viewer account. |
    | **pass_condition** | Owner preview confirms viewer login lands on `/user-view`; `/du-doan` and `/search` both show an obvious `USER VIEW` button back to `/user-view`; dashboard remains admin-only; `/user-view` history defaults to the active region instead of global all-region rows; no delete/update/predict execution actions appear in viewer surfaces beyond the existing read-only lookup/filter behavior. |
    | **fail_condition** | The preview exposes admin actions, delete history, refresh/update/predict execution actions, confuses `/du-doan` final-pick output with per-model `/app` data, or changes scoring/runtime behavior. |
    | **owner_decision_needed** | YES before live deploy or login redirect change. |
    | **last_checked** | 2026-04-30T20:55:00+07:00 |
    | **notes** | This is local preview work only until owner approval. It uses existing APIs and does not introduce a new data contract. |

    ### FU-072 — Native non-BT shadow_results writer for `lo2/lo3/xien2/xien3` axes (owner-gated)

    | Field | Value |
    |-------|-------|
    | **issue_id** | FU-072 |
    | **title** | Upgrade `shadow_method_scoreboard` non-BT axes from BT-derived projections to native `shadow_results` rows per output family |
    | **current_truth** | Since V20.3.37.22, `shadow_method_scoreboard` emits five output_type axes (`BT`, `lo2`, `lo3`, `xien2`, `xien3`). However the non-BT rows are computed by projecting BT-axis aggregates: `lo2/xien2` reuse BT's `top2_rate` and `lo3/xien3` reuse BT's `top3_rate`. The `notes` field of those rows already says `diagnostic_only; projected_output_family_axis_from_bt_ranked_shadow_results`. `shadow_results` rows themselves remain BT-centric — there is no per-output-family per-method per-region per-day fact row for `lo2/lo3/xien2/xien3` yet. To compute true (non-projected) per-family hit rates for Wave-2 maturity review, a new writer or schema field would be required. This is owner-gated because it touches measurement schema/writer scope and could grow shadow row counts ~5x. |
    | **evidence** | `web/backend/_materialize_multi_lane_shadow_p0.py` `_materialize_scoreboard()` axis loop with `axis_primary_rate` projection map and `projected_output_family_axis_from_bt_ranked_shadow_results` notes; `artifacts/db_audit_20260430/coverage_hardening_smoke.json` showing scoreboard_rows expanded 5x while `shadow_results` count stays the same; subagent audit `Audit P0 Shadow Coverage` 2026-04-30 confirming "shadow_results remain overwhelmingly BT-axis fact rows unless you execute the gap proposal". |
    | **impact** | Today: scoreboard non-BT rows are diagnostic projections; usable for trend signal but not for owner-grade Wave-2 promotion decisions on lo2/lo3/xien2/xien3 specifically. After upgrade: Wave-2/3/4 reviews would have true per-output-family fact rows matching `final_bundles.{family}_status`. No `/du-doan`, scoring, output-eligibility, or model-roster change is implied; only measurement scope grows. |
    | **status** | OPEN_OWNER_GATED |
    | **next_action** | Owner approves writer/scope; engineering then chooses one of: (a) extend `shadow_results` writers to emit per-family rows reading `final_bundles.{family}_status` truth; (b) keep `shadow_results` BT-only and add a new diagnostic table `shadow_method_family_rates_daily`; (c) keep projections and explicitly exclude lo2/lo3/xien2/xien3 from Wave-2 maturity criteria. |
    | **pass_condition** | After approved upgrade: every method × region × output_type pair has either native fact rows or an explicit ON_PROJECTION marker; scoreboard `notes` field no longer needs the projection disclaimer for chosen families. |
    | **fail_condition** | Upgrade silently doubles or breaks existing BT-axis aggregates, or any change writes to production output. |
    | **owner_decision_needed** | YES |
    | **last_checked** | 2026-04-30T13:50:00+07:00 |
    | **notes** | Without this upgrade, lo2/lo3/xien2/xien3 trend interpretation should always be qualified as "projected from BT-aligned hits". Cross-ref: V20.3.37.22 (FU-069), V20.3.37.24 (FU-071). |

    ### FU-071 — Cohere rerank measurement consolidated into P0 shadow

    | Field | Value |
    |-------|-------|
    | **issue_id** | FU-071 |
    | **title** | Treat Cohere as measured rerank component and bridge it into the unified P0 shadow scoreboard |
    | **current_truth** | Owner correctly flagged that Cohere is also a measured model/component. Semantics are now split: `runtime_model_count=25` for active prediction measurement (`15 output_eligible + 10 SHADOW_AUTO`), `active_rerank_measurement_model_count=1` for Cohere, and `active_measured_component_count=26` when Cohere rerank is included. `cohere_rerank_effectiveness_v1` is deployed and now live-proven on `2026-04-30`: it is registered in P0, remains `output_eligible=0`, `diagnostic_only=1`, `shadow_only=1`, `owner_approved=0`, wrote rows into `shadow_results`, and has scoreboard rows across all 5 output axes. |
    | **evidence** | Cohere audit `artifacts/db_audit_20260430/cohere_measurement_audit.json`; local copied-DB smoke `artifacts/db_audit_20260430/coverage_hardening_smoke.json` proved `cohere_rerank_effectiveness_v1` emits 1 row per region and scoreboard rows across 5 output axes; deploy artifact `artifacts/db_audit_20260430/cohere_p0_bridge_deploy.json`; VPS backup `/root/Lottery_AI_Test/backups/cohere_p0_bridge_20260430_032522/`; remote compile OK for `_materialize_multi_lane_shadow_p0.py`, `verify_p0_natural_closeout.py`, and `main.py`; remote import/bootstrap proved method count `18`, `has_cohere=True`, registry count `18`; health shows `active_measured_component_count=26`; sync `artifacts/live_sync/20260430_032553/manifest.json`; state verify `artifacts/db_audit_20260430/cohere_bridge_state_after_deploy.json`; source table hash compare unchanged for `predictions`, `final_bundles`, `lottery_results`. |
    | **impact** | Cohere is now part of the unified parallel measurement program, not a separate forgotten side surface. No `/du-doan`, final bundle, prediction, result, scoring, bundle voting, lane weight, output eligibility, public UI behavior, or DDL change. Historical Cohere P0 rows are not backfilled and remain owner-gated if desired. |
    | **status** | DONE |
    | **next_action** | Continue normal closeout watch for Cohere rows; optional owner-gated action: backfill 2026-04-17..2026-04-29 Cohere P0 rows under a distinct run-label. |
    | **pass_condition** | P0 verifier reports 18 registered methods, Cohere method rows appear after natural closeout, output_eligible remains 0, source table hashes unchanged. |
    | **fail_condition** | Cohere rows fail to bridge into P0, method is accidentally treated as generative/output-eligible, or health/model-count semantics collapse 25/26/28 again. |
    | **owner_decision_needed** | NO for deployed future-closeout bridge; YES before historical backfill or any Cohere output/promotion use. |
    | **last_checked** | 2026-04-30T20:35:00+07:00 |
    | **notes** | Transitioned from `DEPLOYED_PENDING_LIVE_VERIFY` to `DONE` after 2026-04-30 closeout proof. Correct vocabulary: 25 active prediction measurement models, 1 active rerank measurement component, 26 total measured components, 28 registry-visible inventory. |

    ### FU-070 — Model count semantics + policy replay consolidation clarified

    | Field | Value |
    |-------|-------|
    | **issue_id** | FU-070 |
    | **title** | Correct confusing `runtime_model_count` semantics and verify A/D/D2/S/F/F2 replay policies are consolidated into P0 shadow |
    | **current_truth** | Owner correctly flagged that active runtime/measurement model count should be `25`, not `28`. Audit proves the split is `15 output_eligible + 10 SHADOW_AUTO = 25 active measurement models`; the prior `28` was registry-visible inventory because it also included 3 `REGISTERED` non-active assets (`wan-2.7`, `pplx-embed-v1`, `cohere-rerank-4-pro`). `/api/health` is now patched to return `runtime_model_count=25`, `active_measurement_model_count=25`, `registry_visible_model_count=28`, `registered_non_active_model_count=3`, and explicit `model_count_semantics`. Separately, all owner-listed replay policies are present and bridged: `A_BASELINE`, `D_CONTEXT_ADAPTIVE`, `D2_CONTEXT_ADAPTIVE_SAFE_GATE`, `S_SECONDARY_STRICT_GATE`, `F_FAMILY_LANE_FUSION`, `F2_FAMILY_LANE_SAFE_GATE`; plus extra diagnostic `B_FLAT_TOTAL_MAIN_SECONDARY`. Each has rows for MN/MT/MB on 2026-04-29 in `output_policy_replay_daily` and bridged `shadow_results` under `output_policy_replay_governance_v1`. |
    | **evidence** | Registry self-test output; read-only audit `artifacts/db_audit_20260430/policy_and_registry_audit.json`; targeted remote patch artifact `artifacts/db_audit_20260430/health_model_count_patch_deploy.json`; VPS backup `/root/Lottery_AI_Test/backups/health_model_count_semantics_20260430_025854/`; remote `py_compile main.py` OK; public health after patch shows runtime `25`, registry-visible `28`; sync `artifacts/live_sync/20260430_025915/manifest.json`; source hash compare confirms `predictions`, `final_bundles`, `lottery_results`, existing shadow tables unchanged; only scheduler logs changed due restart/runtime logging. |
    | **impact** | Health/model-count semantics are now owner-readable and no longer confuse active measurement count with registry inventory. Policy replay A/D/D2/S/F/F2 is confirmed consolidated into the parallel P0 shadow program. No scoring, `/du-doan`, final bundle, prediction, lottery result, output eligibility, model roster, public UI behavior, or DDL change. |
    | **status** | DONE |
    | **next_action** | Keep using `runtime_model_count=25` for active measurement and `registry_visible_model_count=28` for inventory. On next closeout, verify `output_policy_replay_governance_v1` still bridges all 7 policies into shadow rows. |
    | **pass_condition** | Health endpoint exposes both `25` active measurement and `28` inventory semantics; replay policies A/D/D2/S/F/F2 present in both source replay table and P0 bridge rows. |
    | **fail_condition** | Any future UI/doc/API collapses `25` and `28` into one ambiguous count, or output replay policies stop bridging into P0 shadow rows. |
    | **owner_decision_needed** | NO for semantics clarification and read-only replay verification; YES before any replay policy affects `/du-doan`. |
    | **last_checked** | 2026-04-30T03:00:00+07:00 |
    | **notes** | This resolves the owner's `runtime 28 ==> có vẻ sai mà em 25 chứ em?` concern. 28 remains valid only as registry-visible inventory, not active runtime/measurement. |

    ### FU-069 — Measurement coverage hardening deployed (shadow-only)

    | Field | Value |
    |-------|-------|
    | **issue_id** | FU-069 |
    | **title** | Measurement coverage gap audit + first safe writer hardening for Wave/D7/P0 parallel evaluation |
    | **current_truth** | Read-only coverage audit identified 8 gaps. Owner then directed proceeding with the safest recommendation step-by-step, so M-NOW-1/2/3 were deployed in `web/backend/_materialize_multi_lane_shadow_p0.py`: scoreboard now emits projected `output_type` rows for `BT`, `lo2`, `lo3`, `xien2`, and `xien3`; `freshness_readiness_guard_v1` now writes a real `shadow_results` diagnostic row; `counterfactual_decision_audit_v1` now bridges source audit rows into per-row `shadow_results`; `no_token_drift_guard_v1` now emits an explicit diagnostic row when a region has no no-token evidence instead of silently producing 0 rows. M-NOW-4 (model alias audit) already completed read-only and found zero alias mismatch. No schema migration, DROP, ALTER, scoring change, output-policy change, model-roster change, or `/du-doan` mutation occurred. |
    | **evidence** | Coverage audit `artifacts/db_audit_20260430/coverage_audit.{json,md}`; alias audit `artifacts/db_audit_20260430/model_alias_audit.md`; proposal `artifacts/db_audit_20260430/COVERAGE_GAP_PROPOSAL_20260430.md`; local `py_compile` OK; local smoke on copied DB `artifacts/db_audit_20260430/coverage_hardening_smoke.json` proved all three regions emit 17 method rows and 5 output types; deployed file backup `/root/Lottery_AI_Test/backups/coverage_hardening_20260430_023613/`; remote `py_compile` OK; remote import check method count `17`, output types `BT,lo2,lo3,xien2,xien3`, helper functions present; service restarted active; public health `V20.3.36`, output `15`, runtime `28`; post-deploy sync `artifacts/live_sync/20260430_023704/manifest.json`; table hash compare `artifacts/db_audit_20260430/post_deploy_table_hash_compare.json` shows `predictions`, `final_bundles`, `lottery_results`, `shadow_candidates`, `shadow_results`, `shadow_method_scoreboard`, and `shadow_activation_registry` unchanged; only `scheduler_logs` changed due restart/runtime logging. |
    | **impact** | Safest writer hardening is deployed measurement-only. Future natural closeouts will collect output-family scoreboard rows and explicit per-row evidence for previously sparse methods without touching runtime final. Current historical DB rows are not backfilled yet; backfill is optional and should use a separate run-label if owner wants historical coverage immediately. |
    | **status** | DONE |
    | **next_action** | Continue normal closeout watch. Remaining adjacent gaps are tracked separately: FU-072 for native non-BT fact rows and the G7 runtime reliability writer gap in notes. Optional: owner may approve a measurement-only historical backfill on copied/run-label-separated shadow rows. |
    | **pass_condition** | After owner-authorized deploy: every method has both scoreboard and shadow_results rows; output_type axis covers BT + lo2 + lo3 + xien2 + xien3; runtime_reliability covers all 22 AI output-eligible/SHADOW_AUTO models (excl. ML/no-token by design); no scheduler errors; source-table hashes unchanged across deploy. |
    | **fail_condition** | Any change writes to production output, source-table hashes drift, or new measurement schema breaks existing readers. |
    | **owner_decision_needed** | NO for deployed M-NOW-1/2/3 measurement writers; YES before any historical backfill, DDL, output/scoring use, or Wave 2 enforcement. |
    | **last_checked** | 2026-04-30T20:35:00+07:00 |
    | **notes** | Transitioned from `DEPLOYED_PENDING_LIVE_VERIFY` to `DONE` after 2026-04-30 natural closeout and post-MDE verify proved: scoreboard 5 output axes, per-row `freshness_readiness_guard_v1`, `counterfactual_decision_audit_v1`, no-token diagnostic behavior, Cohere bridge, and rule-phase/rule-injection post-MDE rows all materialized. G7 runtime reliability coverage gap remains a separate follow-up because it touches a different materializer/scheduler path. Non-BT scoreboard rows remain projected aggregates from BT-axis `shadow_results`; native non-BT fact rows are tracked in FU-072. |

    ### FU-068 — DB table inventory + consolidation proposal (read-only)

    | Field | Value |
    |-------|-------|
    | **issue_id** | FU-068 |
    | **title** | First full DB table inventory and consolidation proposal (read-only audit, no DDL touched) |
    | **current_truth** | A read-only DB inventory has been produced from the locally-synced production DB (`data/lottery_ai.db`, hash `921690ac002ccb1860a73a7e0dea0d0a3bca7700385f1f7164caf705b6525901`, size 43,044,864 bytes). Total objects = `68 tables + 8 views = 76`. Class breakdown: `MEASUREMENT=30`, `LIVE_OR_OTHER=18`, `SHADOW=12`, `VIEW=8`, `EMPTY=6`, `REPLAY=1`, `SYSTEM=1`. Empty tables: `bundle_replay_compare_daily`, `data_preservation_manifest_daily`, `rule_effectiveness`, `rule_features`, `sync_parity_audit_daily`, `training_records`. Stale (>30d) tables: `pattern_rules` (admin-managed, low-churn) and `users` (auth, low-churn). A consolidation proposal classifies drop-candidates, dormant-but-wired entries, and dev-side-only writers, plus 5 possible merge groups (only 1 actionable, the others NOT recommended). All actions are gated on owner approval. No DDL, no DROP, no ALTER, no RENAME has been executed. |
    | **evidence** | Inventory script `artifacts/db_audit_20260430/_audit_db.py` (read-only, opens DB with `mode=ro`); inventory artifacts `artifacts/db_audit_20260430/inventory.json` and `inventory.md`; consolidation proposal `artifacts/db_audit_20260430/DB_TABLE_CONSOLIDATION_PROPOSAL_20260430.md`; live sync `artifacts/live_sync/20260430_015322/manifest.json`; per-table reference scan via `Grep web/backend/` confirms drop-candidate isolation. |
    | **impact** | Pure read-only inventory + proposal. No `/du-doan`, `final_bundles`, `predictions`, `lottery_results`, scoring, bundle voting, lane-weight, output eligibility, model roster, public UI, scheduler hook, or runtime final behavior change. Production DB schema is untouched. |
    | **status** | PROPOSAL_PENDING_OWNER_APPROVAL |
    | **next_action** | Owner reviews `DB_TABLE_CONSOLIDATION_PROPOSAL_20260430.md` and decides per-table action for Phase R1 (drop orphans), Phase R2 (re-wire-or-drop dormant writers), and Phase R3 (docs reconciliation). |
    | **pass_condition** | Inventory artifacts exist and match VPS DB hash; consolidation proposal lists each candidate with verdict and rollback path; no DB write occurred during the audit. |
    | **fail_condition** | Audit script writes to DB or to runtime files; or proposal recommends destructive action without owner approval; or proposal hides a table that is wired in active code. |
    | **owner_decision_needed** | YES for Phase R1 (drop) and Phase R2 (re-wire-or-drop); NO for Phase R3 (docs-only sync). |
    | **last_checked** | 2026-04-30T13:55:00+07:00 |
    | **notes** | Live wires confirmed: `pattern_rules` is admin-managed (live CRUD via `/api/rules` and `/rules-dashboard`, used by `filter_2_so_cuoi.py`, `knowledge_weights.py`); `rule_effectiveness` has a dormant V5.8 writer (`update_rule_outcome`); `data_preservation_manifest_daily` and `sync_parity_audit_daily` only fire from a dev-side admin endpoint that reads `artifacts/live_sync/latest_manifest.json`. **Cross-ref:** also tracking machine-surface drift in `docs/AUTOMATION_STATE.json` (`last_event` still reads seq=6 / 2026-04-27); not in scope for Phase R1/R2 but should be folded into the next governance automation pass. |

    ### FU-067 — Parallel Shadow Proof admin monitoring board deployed

    | Field | Value |
    |-------|-------|
    | **issue_id** | FU-067 |
    | **title** | Add owner-readable admin board comparing runtime final baseline with the 17-method parallel shadow portfolio |
    | **current_truth** | `/monitoring` now includes an admin-only `Parallel Shadow Proof — baseline vs methods` section backed by `/api/admin/parallel-shadow-proof`. The endpoint is read-only and uses existing `final_bundles`, `shadow_activation_registry`, `shadow_results`, `shadow_candidates`, and `shadow_method_scoreboard` tables. It returns baseline final, method coverage, would-save/risk summaries, and top1 candidate rows with `output_impact=false`. |
    | **evidence** | Deployed `web/backend/main.py` and `web/frontend/monitoring.html`; backup `/root/Lottery_AI_Test/backups/parallel_shadow_ui_<timestamp>/`; local `py_compile main.py` OK; remote venv `py_compile main.py` OK; remote marker grep found `/api/admin/parallel-shadow-proof` and UI title; direct function smoke with admin bypass for `2026-04-29` returned `success=True`, `method_count=17`, `output_impact=False`, baseline regions `MN/MT/MB`, and 17 methods; public health `V20.3.36`, output `15`, runtime `28`. |
    | **impact** | Gives owner/admin a visual proof board for the parallel measurement branch. No `/du-doan`, `final_bundles`, `predictions`, `lottery_results`, scoring, bundle voting, lane-weight, output eligibility, model roster, public UI, or runtime final behavior change. |
    | **status** | DEPLOYED_PENDING_OWNER_VISUAL_VERIFY |
    | **next_action** | Owner opens `/monitoring`, verifies the `Parallel Shadow Proof — baseline vs methods` section appears, and confirms wording clearly says `SHADOW_ONLY` / no `/du-doan` impact. |
    | **pass_condition** | Board loads for admin, shows 17 methods and baseline regions for latest shadow scoreboard date, and does not confuse method count with model count. |
