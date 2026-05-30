# V10640 — FULL EVIDENCE DETAIL (for cross-AI analysis)

All numbers below are aggregate statistics from read-only backtests/queries on the
production DB (no raw rows, no keys, no internals). Region codes: MN=South, MT=Central,
MB=North. Weekdays: CN=Sun, T2=Mon … T7=Sat. BT = "bach thu" = the single money number.

---

## 1. Official absolute trend by month (final_bundles, BT win-rate %)
| Region | Mar (T3) | Apr (T4) | May (T5) | n/month |
|---|---|---|---|---|
| MB | 38.7 | 23.3 | **10.0** | ~30 |
| MN | 41.9 | 53.3 | **40.0** | ~30 |
| MT | 54.8 | 40.0 | **40.0** | ~30 |

→ Owner observation confirmed: **both official AND lane got worse in May** (absolute). MB collapse 38.7→10.

## 2. du_doan_test lane vs official — FORWARD-logged, deduped 1 row/day (honest)
(Earlier "all-rows" version was inflated by 7-10 rows/day; deduped = honest.)
| Region | Apr off→lane | May off→lane |
|---|---|---|
| MN | 59.3 → 59.3 | 41.7 → **54.2** |
| MT | 33.3 → 37.0 | 33.3 → **50.0** |
| MB | 18.5 → 22.2 | 8.0 → **16.0** |
Caveat: lane's own official_bt_status matches final_bundles ~90% (settlement-timing); BT number matches 100%.

## 3. Oracle ceiling (did ANY model hit BT) by month — WITH hindsight caveat
| Region | Mar | Apr | May | avg models/day |
|---|---|---|---|---|
| MB | 83.9 | 86.7 | 89.7 | 8→27 |
| MN | 100 | 100 | 96.6 | 8→27 |
| MT | 93.5 | 96.7 | 100 | 8→27 |
⚠ **Correction:** this is HINDSIGHT — with ~27 models scattering guesses, "some model hits"
is near-certain by luck; ex-ante you CANNOT reliably pick which. The 90-100% is NOT achievable.
More models (8→27) raised this number mechanically but did NOT help ex-ante selection.

## 4. Herd-follow loses (May): when official BT = most-voted-by-models tail
| Region | days official followed herd | herd win-rate |
|---|---|---|
| MB | 5/34 | 0.0% |
| MN | 12/33 | 12.1% |
| MT | 5/31 | 3.2% |
→ Following the model "consensus" tail LOSES. Anti-herd / selective is the direction.

## 5. Per-weekday official BT win-rate (90d) — the "bleed map"
| Region | by weekday (%) |
|---|---|
| MN | T4 **23**, T6 **31**, T7 **31**, T5 46, CN 62, T2 62, T3 62 |
| MT | T6 **23**, T2 **31**, CN 46, T3 46, T4 46, T7 46, T5 **77** |
| MB | T4 15, T2 23, T5 23, T6 23, T7 23, CN 31, T3 31 |
→ MN/MT are bimodal (strong some days, bleed others). MB weak everywhere.

## 6. Per-chooser experimental_preview (60d) — NOTE: materializer specialists use date<=today (mild lookahead)
| Region | best chooser | cand% | baseline% |
|---|---|---|---|
| MN | AI_CHAIN 61.5 / SPECIALIST 56.4 / HYBRID 55.6 | — | 51.3 |
| MT | CONSENSUS 52.0 / STRENGTH 48.7 | — | 46.2 |
| MB | PRIOR_REGION 30.8 / STRENGTH 30.8 | — | 23.1 |

## 7. ★ DECISION GATE: NO-LOOKAHEAD backtest (91d, specialists STRICT date<today)
| Region | chooser | official% | override% | Δpp | net | override days | verdict |
|---|---|---|---|---|---|---|---|
| **MN** | specialist | 45.1 | **50.5** | **+5.4** | +5 | 13/91 | **PASS → enabled** |
| MT | ai_chain | 45.1 | 41.8 | −3.3 | −3 | 64/91 | REJECT (worse) |
| MT | no_token_herd | 45.1 | 47.3 | +2.2 | +2 | 18 | noise → off |
| MT | strength | 45.1 | 46.2 | +1.1 | +1 | 39 | noise → off |
| MB | specialist | 24.2 | 25.3 | +1.1 | +1 | 19 | noise → off |
| MB | strength | 24.2 | 24.2 | 0 | 0 | 47 | flat → off |
→ Only MN specialist is a reliable edge. The gate CAUGHT that MT ai_chain (looked good with
lookahead/weak-weekday slicing) would actually HURT official (−3.3pp).

## 8. Lane v2 (per-region modules) — half-baked, fixed, measured
- Were committed to git but NEVER deployed + import broken (`web.backend.lane` unresolvable) → never ran.
- Fixed imports → runnable; added daily runner + comparison table + isolated cron.
- In-sample backtest: MN 45.9 vs official 47.5 (−1.6), MT 40.4 vs 41.0 (−0.6) → NOT better → kept as comparison challenger only, NOT promoted.

## 9. V10640 deploy mechanism + safety
- Reversible per-region flag (MN ON, MT/MB OFF). Reuses lane choosers (single source of truth).
- Specialists computed STRICT date<today (no lookahead). Defensive: any error/empty → keep official top1.
- Deploy: backup → py_compile → dry-run verify (pre-restart) → restart → health /api/health+/api/status=200 → rollback-ready.
- Verify: 6 most-recent MN days override = top1 (agreed, not broken); MT/MB = disabled. lo2 leads with chosen BT (byte-identical to legacy when flag OFF).

## 10. Self-corrections (transparency)
- "lane +8~16pp" → mixed experiments + dedup artifact; honest clean edge +2.5~7.7pp.
- "oracle 90-100% = huge selection headroom" → hindsight, not ex-ante achievable.

## 11. Open questions for cross-AI analysis
1. Better-than-"specialist-roster" ex-ante BT selector per (region×weekday), validated out-of-sample? Ensemble + shrinkage vs single-best?
2. MB official ~10-19% with hindsight-oracle ~90%: is there ANY ex-ante selector that exploits this BURDEN-of-proof bend, out-of-sample, robustly? Or is MB simply near-random?
3. Statistically sound stop/rollback threshold for MN override given small daily samples (e.g., sequential test, min live days)?
4. Is the per-slice (region×weekday×station) axis worth the complexity vs region-global, given edges are small?

---
*Public-safe. Aggregate stats only. No private code / DB rows / API keys / VPS internals.*
