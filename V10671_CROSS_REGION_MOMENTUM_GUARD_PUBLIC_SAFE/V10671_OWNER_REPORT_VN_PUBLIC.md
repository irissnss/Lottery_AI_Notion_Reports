# V10671 — DRAW-ORDER Causality Guard for Cross-Region Momentum (construction-safe)

Public-safe report. No private endpoints, no IP, no internal paths.

## 1. Context

Draw order is a hard fact: MN draws first (~16:30) → MT second (~17:30) → MB last (~18:30). A same-day (D) cross-region signal is only valid if the source region draws BEFORE the target. The reverse (e.g. using MT's same-day result to predict MN) is impossible because the data does not exist yet when the earlier region is predicted.

A parallel work stream already fixed the RULE REGISTRY side of this (removed 266 source-draws-after-target rule cells; verified the registry causally clean). This report covers a DIFFERENT, additive mechanism: the no-token machine-learning "cross-region momentum" feature.

## 2. Audit result — system causally clean

Six live mechanisms were verified for same-day direction correctness:

| Mechanism | Verdict |
|---|---|
| Rule registry (mined rules) | 0 same-day violations; the earliest-drawing region has 0 same-day sources |
| AI prompt cascade | earliest region uses previous-day only; later regions may use earlier same-day |
| AI chain source labels | explicit previous-day vs same-day markers, correct |
| Lag-1 adaptive exploit signals | only valid same-day directions present, 0 wrong-direction |
| Adaptive exploit selector | gated on "source actuals known" + earliest region restricted to previous-day |
| No-token ML momentum | uses previous-day by default in training |

Re-prediction cascade verified timing-safe across 7 consecutive days. Test-lane / shadow rows are all marked non-output (never feed the official result). Some shadow rows are correctly flagged as measurement-timing by the no-lookahead harness.

## 3. The one hardening point fixed in V10671

The no-token ML momentum feature used an adjacency map where the middle-drawing region listed the last-drawing region as a neighbour. With the same-day flag enabled (re-prediction path), the query could in principle pull the later region's same-day data. In practice this was safe ONLY because of timing (the later region had not drawn yet at re-prediction time) — not guaranteed by code.

Fix: a draw-order guard now splits neighbours into "earlier" (may contribute same-day) and "later" (forced to previous-day only, never same-day) — enforced by code, not timing. A single query with a single result limit preserves the exact original row-selection, so when the same-day flag is off the output is byte-identical to before.

## 4. Verification (production database never mutated; tests on disposable copies)

1. Behavior-neutral: all six (region × same-day-flag) momentum outputs are IDENTICAL before and after the fix on live data.
2. Wrong-direction BLOCKED: injecting a fake later-region same-day row left the middle-region momentum completely unchanged — the later region cannot leak in.
3. Valid-direction PRESERVED: injecting a fake earlier-region same-day row DID change the later-region momentum — same-day signals still flow in the correct direction.

Four official tables hash unchanged; service healthy; compiles on both local and server.

## 5. Net effect

Same-day cross-region rules are KEPT and fully functional in the correct direction (earlier region → later region). The only thing removed is the theoretical ability for a later-drawing region to leak its same-day result into an earlier-drawing region — which has no real data anyway. The system is now safe by construction, not by timing luck — closing exactly the kind of silent-fragility gap that caused a past multi-day issue.

## 6. STATUS

PUBLIC_SAFE — no IP / no internal paths / no provider keys / no DB DDL exposure / no private repo references.
