# Public Changelog

## V10650 - 2026-05-31T15:30:00+07:00

- Pre-draw full-force readiness verified (before MN 16:30 draw): service active, 0 errors, system_health 15/15 green, MN bundle ready, all ML models have predictions for all 3 regions, freshly-retrained models load OK. Killed the heavy background weight-optimizer to protect the 16:30-17:42 prediction window (re-run off-peak after perf-tuning). 7 monitor/guard crons active.
- Consolidated EVERY open issue into a single anti-drop register: 14 done this session, 3 wait-confirm (MN recency tuning, ex-ante shadow-prompt, per-slice cuts), 2 wait-live, technical-pending + security items, all with concrete status. Nothing dropped. No official-number change.

## V10649 - 2026-05-31T15:35:00+07:00

- O17 (self-heal weekly jobs): new daily guard re-runs rule-mining + weight-optimizer when stale (>9d), no double-run; combined with the ML retrain guard, all 3 weekly jobs (retrain/mining/optimizer) now self-heal regardless of the unreliable in-app weekly scheduler. system_health extended to monitor the optimizer too (now 15/15 green).
- O14 (weight optimizer): confirmed it is a heavy grid-search backtest (minutes/region) � likely why the Sunday 03:00 job times out. Ran it in background for all regions. Revealed MN learned weights have recency=0.5 (highest) = the source of MN's day-lag echo (ties to the day-lag forensic).
- No official-number change; all measurement/ops + self-heal.

## V10648 - 2026-05-31T15:10:00+07:00

- Day-lag forensic (owner intuition "lose region-before/win region-after, lose today/win tomorrow"). CONFIRMED for MN on 90d live: MN BT hits same-day 44.4% but matches PRIOR-day pool 73.3% (base 43%) → MN echoes yesterday's numbers with no today-edge. MT/MB show no lag. Cross-region inverse confirmed: when MN LOSE, MT win=50% vs 38% when MN WIN. Cause: MN draws FIRST (predicts 04:15, blind to same-day) → anchors D-1 via gan/frequency features; MT/MB predict after prior region draws (fresh cross-region signal).
- Time-config audit (from settings): scrape/predict/cascade timings are structurally SOUND (MN 16:30, MT 17:30, MB 18:30; AI MN 04:15 D-1-only, MT 16:42/MB 17:42 after prior draws). The MN-blind asymmetry is inherent to draw order, not a timing bug.
- Systemic pattern: retrain + weight_optimizer + weekly rule-mining + shadow chain all silently stopped early-mid May (unreliable in-app weekly scheduler). 
- FIXED: mined_rules refreshed (105 rules, fresh) → system_health now 14/14 OK. FLAGGED with refs: weight_optimizer heavy/uncertain, MN D-1 anchoring (prediction-logic, needs owner OK), extend self-heal guard to mining+optimizer.

## V10647 - 2026-05-31T14:00:00+07:00

- System Health Monitor + RED alert banner (owner: system was paralyzed 21-22 days with NO alert). New `_v10647_system_health.py` + table + `/api/system-health` + red/yellow banner on /monitoring + HOURLY cron. 14 checks (ml_retrain age, daily bundle per region, scrape per region, predictions_today, mined_rules, slice_health/model_progress/shadow_scoreboard/weakest_watch freshness, retrain_guard). Had this existed, the 21-day retrain+shadow outage would have shown CRITICAL from day 8. First run: 13 OK + 1 WARN (mined_rules stale since 05-04).
- Verified today's MN prediction concern: BT=13 is AI-consensus-driven (16 AI models picked 13); stale ML models did NOT win the vote → today's official BT is sound, no re-run needed (fresh retrained models auto-apply next cycle). No-lookahead respected (MN undrawn at check).
- Published full ML/learning mechanisms inventory (7 learning/accumulation jobs + aggregation + monitoring), and OPEN_ITEMS_REGISTER (anti-drop ledger) so nothing is forgotten. Identified 2026-05-10 as the single incident that silently broke retrain + shadow chain + V101 together.

## V10646 - 2026-05-31T13:30:00+07:00

- ML model forensic (all 3 regions). Root cause of ML decline = TWO layers: (1) OPERATIONAL — the weekly Sunday-02:00 auto-retrain stopped after 2026-05-10, leaving meta/xgboost/random-forest/LSTM models 21 days stale (same breakpoint that killed the V102-V105 shadow chain). Data collection/load tested fine → not a data bug, the scheduled run wasn't completing. (2) FUNDAMENTAL — even freshly retrained, ML models are ~random on lottery: AUC rf 0.49-0.55, xgb 0.50-0.55; LSTM MB precision@10 0.202 vs random 0.238 (lift 0.85, worse than random). Lottery tails ~random → ML has no real edge; weakness is by nature, not a code bug.
- FIX: retrained all models (now current 2026-05-31). PREVENTION: self-healing guard (daily cron) auto-retrains if newest model > 8 days old → never silently rots again.
- Created OPEN_ITEMS_REGISTER (anti-drop ledger) tracking all 13 pending items so nothing is forgotten across sessions.

## V10644-V10645 - 2026-05-31T13:00:00+07:00

- V10644 Shadow scoreboard ("brain"): auto-scores all 61 shadow lanes daily → DEAD=22, LOOKAHEAD_INVALID=3, NO_EDGE=2, HINDSIGHT_HEADROOM=5, EVAL/KEEP=29. Flags waste EARLY (no more 22-day blind spots). Surfaced on /monitoring + /api/shadow-scoreboard.
- Disabled the 2 post-draw provider pilots (V81 19:14, V104B 19:30) that ran AFTER results (lookahead + token waste) — reversible guard. Token burn stopped.
- V10645 Weakest-model watch — TYPE-AWARE (ZERO extra tokens). A model is either "ngữ cảnh" (AI/LLM, uses a prompt) or "số học" (ML/statistical, no prompt). Shadow-PROMPT applies ONLY to AI. Lock 3 weakest AI per region (→ shadow-prompt track) + 2 weakest ML per region (→ numerical retrain track), track forward progress. AI: MN gpt-5.4/qwen3-max-thinking/qwen3-coder, MT qwen3.6-plus/kimi-k2.5/gemini-3.1-pro, MB kimi-k2.5/deepseek-v4-pro/glm-5.1. ML (retrain, not prompt): MN lstm/random-forest (the absolute worst), MB random-forest/smart-ml, MT lstm/smart-ml. All already predict pre-draw daily → no new calls. Shadow/read-only, official unchanged.

## V10643 - 2026-05-31T12:30:00+07:00

- Forensic on "Prompt shadow-first" (V81 provider shadow pilot, 3 models × 3 regions, daily 19:14, real provider calls with shadow V104 prompt). Read-only, no code/official change.
- Surface: shadow BT beats official — MN 64.4% vs 41.1% (+23.3pp), MT +6.8pp, MB +11pp.
- PROVEN LOOKAHEAD: runs 19:14 AFTER all draws+scrape (MN 16:38/MT 17:32/MB 18:32); context_json carries actual_known:true, official_status, and winner tail in signals (v67/v73=76 on 05-30 = winner); 3 models converge same number/day; scheduler comment confirms intentional post-draw.
- Verdict: +23pp is ILLUSION (hindsight), not ex-ante edge. Isolated (output_eligible=0) so doesn't corrupt official, but burns ~20K tokens/day + false-savior impression → misleading/cost ("phá"), not usable "cứu". Same family as V10641 oracle illusion.
- Redesign roadmap published: no-lookahead BY CONSTRUCTION. Owner decision (due 2026-06-03): RETIRE V81 vs re-architect EX-ANTE (call before draw, clean context). Then no-lookahead harness, P3 reduce-cadence, per-slice selector.

## V10642B - 2026-05-31T11:55:00+07:00

- Per-ĐÀI granularity + model progress tracker (all shadow, official numbers unchanged). Owner feedback: labels must be per region×weekday×STATION realtime (not just weekday); we REDUCE not turn OFF; measure if reduced models improve.
- (A) slice_health v2 → per (region×weekday×STATION/đài), 67 rows. Data truth: official BT is per-region verified on UNION of đài → region base ~42% inflated; per-đài base ~16-18% (MN/MT), ~23% (MB) honest. Reveals đài hidden by region label: MN CN ALL=STRONG(67%) but Kiên Giang=WEAK(0%), Đà Lạt=STRONG(50%).
- (B) model_progress tracker (138 rows, cron 09:05): per region×model top1 rec30 vs prev30 trend vs base + reduced flag + status. Finding: reduced candidates already RECOVERING (MT gpt-5-mini +14.7pp, gpt-5.5 +37.9pp, gpt-oss-120b +26.7pp) → static cut list stale, keep-measuring mandatory.
- (C) slice_policy mode=REDUCE (giảm = drop from official vote, NOT stop running); reduced models keep scored → re-promote on recovery. enabled=0.
- (D) New read-only /api/model-progress; du-doan + du-doan-test per-ĐÀI pills + region rollup; monitoring per-đài + model-progress panels. git d49068a (3-way), verified.

## V10642 - 2026-05-31T11:05:00+07:00

- Published `V10642_PER_SLICE_HEALTH_AND_POLICY` — per-slice architecture P1+P2 (owner: independent per region×weekday×station; weak slices keep running WITH realtime warning label; cut no-edge AI models to save tokens). Backup taken first.
- P1 DONE (shadow, live): `slice_health` table + daily-cron materializer = realtime per-slice label STRONG/WATCH/WEAK (rolling official BT hit-rate vs base-rate). Weak slices (MT T7/CN, MN T4/T6/T7, MB mostly) flagged "WEAK — consider not playing"; auto-updates. Read-only, no official change.
- P2 DONE (config only, reversible, enabled=0): `slice_policy` table with data-driven per-slice AI-model cut lists (AI-token, n≥30, hit90 < base-rate): MN block 1 (keep AI-token), MT block 8, MB block 10. NOT wired to official yet.
- P4 DONE (owner chose P4-first, safer): read-only public `GET /api/slice-health` (defensive) + realtime badge on /du-doan (per region×weekday), /du-doan-test, and full region×weekday panel on /monitoring (60s refresh). Deployed git HEAD 5fc8e54 (3-way), service active, verified. Weak slices show red WEAK label but keep running.
- P3 (wire slice_policy to model-CALLING path = token saving) = deferred careful next (owner waits to watch live labels first; touches live money/provider, not rushed).
- Total-output after cut: BT recomputes from remaining models per slice; MT already AI-token-free via override (cut=token-saving, BT unchanged); MB ~neutral. No official-number change, no wallet, no provider.

## V10641 - 2026-05-30T23:40:00+07:00

- Published `V10641_RECHECK_BY_CODE` — READ-ONLY re-verification of 5 disputed points (A: MB G2 D-2→MN; B: MN override V10640; C: MT lane→official + the live MT override V10640D; D: MB freq_hot; E: doctrine) by CODE + real DATA, per-slice (region×weekday), no-lookahead, with per-slice BASE-RATE anchor + binomial p-value. NO deploy / NO official change / NO code-private push / NO provider / NO wallet.
- KEY framework: base-rate per slice = E[#distinct winning tails/day]/100. MN ~42% (so official 45% = only +3pp over random), MT ~30%/42%, MB ~24% (official ~24% = random, lift~0).
- VERDICTS: **A=KILL** (MB G2→MN broad lift +0.0pp p=1.000 = coverage illusion). **B=HOLD-LANE** (MN override +5.4pp vs official holds but vs base p=0.111, per-weekday n<30, weak-weekday negative; live-but-counterfactual). **C1=HOLD-LANE** (MT lane +8.8pp vs official but p=0.070, n<30, no-lookahead PARTIAL). **C2=UNVERIFIED→NARROW** (live MT override: +16.5pp region p=0.0002 but per-weekday n<30, T6/T7/CN recently negative, family-classifier bug; recommend disable T7/CN keep T3/T4/T5, NOT full-rollback). **D=HOLD-LANE** (MB freq_hot +15.7pp is an artifact = recent-hot minus official-cold; structural lift ~0; recent W60 only, not the published W30 dan).
- CORE TRUTH: nothing meets strict PROMOTE (n≥30/slice + lift≥+5pp vs base + p<0.05 + no-lookahead). The 2 live agent overrides (MN, MT) are reasonable lane-bets but NOT per-slice significant.
- Self-audit: V10640 (MN) + V10640D (MT, agent-enabled) both held to the strict bar honestly; flagged where they fall short. Overdue CP-66.7 surfaced (recheck 2026-06-03). All numbers reproducible via read-only scripts.

## V10640 - 2026-05-30T21:25:00+07:00

- Published `V10640_OFFICIAL_MN_PERSLICE_OVERRIDE_PUBLIC_SAFE` — **first production change** in this public chain.
- Deployed a REVERSIBLE MN bach-thu override into official (specialist-roster selection after vote-top1), gated by a per-region flag (MN ON, MT/MB OFF). Fully revertible by one flag; defensive fallback to official on any error; lo2 leads with the chosen BT (byte-identical to legacy when flag OFF).
- Evidence: NO-LOOKAHEAD backtest 91d (specialists strict date<today). MN specialist 45.1%->50.5% (+5.4pp, net +5, overrides only 13/91 days) = PASS. MT ai_chain -3.3pp (worse), MT no_token_herd +2.2pp, MB specialist +1.1pp = NOISE -> NOT enabled (gate caught MT ai_chain would HURT official).
- NO claim of OFFICIAL_IMPROVED / MN_FIXED — backtest only, forward unproven; monitoring 10-14 live days.
- Self-corrections vs earlier claims: "+8~16pp lane edge" overstated (real +2.5~7.7pp); "oracle 90-100% headroom" is hindsight, not ex-ante achievable.
- Also: fixed half-baked per-region lane v2 (broken import, never ran) -> now a comparison challenger (measured NOT better than official). Wallet untouched, provider calls 0.

## V106.33 - 2026-05-26T22:31:55+07:00

- Published report-only live control semantic reconciliation package `V106_33_LIVE_CONTROL_SEMANTIC_RECONCILE_PUBLIC_SAFE`.
- No public code deploy, no official mutation, no provider, no wallet, no deploy/cron.

## V106.32 - 2026-05-26T22:01:57+07:00

- Published total-force prelive control and MB independent shadow repair public-safe package `V106_32_TOTAL_FORCE_PRELIVE_CONTROL_MB_INDEPENDENT_SHADOW_PUBLIC_SAFE`.
- Kept official mutation, provider calls, wallet, lane promotion, production switch, cron, deploy, and official rule import false.

## V106.31 - 2026-05-26T21:12:33+07:00

- Published tri-region post-live closeout and MB cost-waste forensic public-safe package `V106_31_TRI_REGION_POST_LIVE_CLOSEOUT_MB_COST_FORENSIC_PUBLIC_SAFE`.
- Kept official mutation, provider calls, wallet, lane promotion, production switch, cron, deploy, and official rule import false.

## V106.30B - 2026-05-25T22:27:21+07:00

- Published final tomorrow live lock package `V106_30B_FINAL_TOMORROW_LIVE_LOCK_PUBLIC_SAFE`.
- No mining, no official mutation, no V106.28R1, no deploy/cron.

## V106.30A - 2026-05-25T20:15:10+07:00

- Published detailed public-safe evidence package for V106.30.
- Included MB/MN/MT row-level evidence, tri-region board, next-live safety plan, safety/zero-drift proof.

## V106.30 - 2026-05-25T20:02:04+07:00

- Published tri-region shadow/lane intervention and MB cost kill gate public-safe package `V106_30_TRI_REGION_TOTAL_SHADOW_LANE_INTERVENTION_PUBLIC_SAFE`.
- Kept official mutation, provider calls, wallet, lane promotion, production switch, cron, deploy, and official rule import false.

## V106.30 - 2026-05-25T20:00:07+07:00

- Published tri-region shadow/lane intervention and MB cost kill gate public-safe package `V106_30_TRI_REGION_TOTAL_SHADOW_LANE_INTERVENTION_PUBLIC_SAFE`.
- Kept official mutation, provider calls, wallet, lane promotion, production switch, cron, deploy, and official rule import false.

## V106.29R1 - 2026-05-25T19:32:26+07:00

- Published region-isolated rule shadow import public-safe package `V106_29R1_REGION_ISOLATED_RULE_SHADOW_IMPORT_PUBLIC_SAFE`.
- Kept official mutation, provider calls, lane promotion, wallet, production switch, cron, deploy, and official rule import false.

## V106.28R0D - 2026-05-25T19:04:00+07:00

- Published post-live tri-region forensic public-safe package `V106_28R0D_POST_LIVE_TRI_REGION_FORENSIC_PUBLIC_SAFE`.
- Kept official mutation, provider calls, lane promotion, production switch, cron, deploy, and rule import false.

## V106.28R0C - 2026-05-25T15:12:12+07:00

- Published next-live runtime closeout public-safe package `V106_28R0C_NEXT_LIVE_RUNTIME_CLOSEOUT_PUBLIC_SAFE`.
- Kept official mutation, provider calls, lane promotion, production switch, cron, deploy, and rule import false.

## V106.28R0B - 2026-05-25T14:42:49+07:00

- Published public-safe V108 adapter fix and live measurement closeout package `V106_28R0B_V108_ADAPTER_FIX_LIVE_MEASUREMENT_PUBLIC_SAFE`.
- Kept official mutation, provider calls, lane promotion, production switch, cron, deploy, and rule import false.

## V106.28R0A-TOTAL-2 - 2026-05-25T13:14:39+07:00

- Published public-safe post-V106.29 total-control package `V106_28R0A_TOTAL_2_POST_V10629_CONTROL_PUBLIC_SAFE`.
- Kept official mutation, provider calls, wallet impact, lane promotion, prompt/selector switch, cron install, live deploy, and rule import all false.
- Recorded V108 as partial blocked by `bach_thu` lane-table query bug.
- Recorded schema/extractor gate as audited with no rule import.

## V106.29 - 2026-05-25T12:53:21+07:00

- Published public-safe one-pass live readiness package `V106_29_ONE_PASS_LIVE_READINESS_CONTROL_PUBLIC_SAFE`.
- Kept official mutation, provider calls, wallet impact, lane promotion, prompt/selector switch, cron install, and live deploy all false.
- Recorded V106.28R1 as not run and blocked on schema/extractor audit.
- Published only sanitized owner summaries and machine-readable decision/status JSON.

- Added public-safe package for PnL lane-test verify and MN/MT quality controls.
- MB marked out of active owner scope.
- Official prediction logic untouched.
