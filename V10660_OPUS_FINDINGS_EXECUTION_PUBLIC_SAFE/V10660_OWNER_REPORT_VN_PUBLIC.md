# V10660 — Opus Findings Execution: No-Lookahead + Monitoring Surfaces

Public-safe report for owner and external AI review tools.

## 1. Context

Owner requested a careful continuation after reviewing issues found by the previous Opus agent chain. The accepted plan required:

- Read-only live verification first.
- No-lookahead protection before new shadow/lane experiments.
- Monitoring deployed BT overrides and confidence recommendations.
- Preparing reduce-cadence without hard-freezing models.
- Preparing the CP-66.7/P1 evidence path.
- Correct private/public deployment split.

## 2. Live Verification

Live forensic inputs were synced before using local evidence.

Read-only verification:

- System health: 15/15 OK.
- `/login`: 200.
- `/du-doan-test`: 401 when unauthenticated, expected admin protection.
- `/monitoring`: 401 when unauthenticated, expected admin protection.
- Slice health, model progress, shadow scoreboard, weakest watch, and slice recommendation were fresh on 2026-05-31.

## 3. No-Lookahead Harness

Private runtime added a no-lookahead audit harness:

- Writes only `no_lookahead_audit`.
- Uses regional draw cutoffs:
  - MN: 16:30.
  - MT: 17:30.
  - MB: 18:30.
- Classifies rows as `EX_ANTE`, `HINDSIGHT`, or `UNKNOWN`.
- Lane V2 future rows are now wired to record no-lookahead proof.

Initial VPS run:

- Audit rows: 143.
- EX_ANTE: 90.
- HINDSIGHT: 53.

Interpretation: historical/backtest rows can be hindsight; future shadow/lane rows must prove ex-ante timing before being treated as usable edge.

## 4. Live Edge Monitor

Private runtime added a live edge monitor:

- Tracks official BT by region using the correct lô metric: any prize, occurrence count.
- Tracks the deployed override family:
  - MN specialist.
  - MT no-token consensus.
  - MB hot-number strategy.
- Links recommendation tier mix and model-progress status mix.

Initial VPS run:

- Rows: 42.
- Settled rows: 42.
- Wins: 10.

This does not change predictions. It only creates a monitor surface for the next 10-14 live days.

## 5. Reduce-Cadence Plan Surface

Private runtime added a reduce-cadence planning table:

- Source: `model_progress`.
- Output: review recommendations such as daily, every 2 days, every 3 days.
- RECOVERING models stay daily/review-promote.
- Thin-sample models keep accumulating data.
- No scheduler or provider calling was changed.

Initial VPS run:

- Rows: 138.
- Daily: 30.
- Accumulate daily: 54.
- Review daily/promote: 14 combined.
- Every 2 days keep measuring: 15.
- Every 3 days keep measuring: 25.

This is a planning surface only, not a freeze.

## 6. CP-66.7 / P1 Evidence Scaffold

Private runtime added an evidence-pack scaffold for the 2026-06-03 checkpoint.

Current read for 2026-05-21 to 2026-05-31:

- Adaptive exploit rows: 32.
- Adaptive exploit closed dates: 0.
- Lane V2 forward rows: 6.
- No-lookahead audit rows: 393.
- No-lookahead hindsight rows: 156.

Conclusion: CP-66.7 remains data-blocked until closeout rows exist. CP-66.8 remains locked.

## 7. Safety

No official prediction logic changed.

No provider calls were made.

No DB table was dropped.

No root cleanup was performed.

Private commit: `baecf6a`.

