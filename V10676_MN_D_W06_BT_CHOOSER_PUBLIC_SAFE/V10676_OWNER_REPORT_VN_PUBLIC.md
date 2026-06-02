# V10676 — MN BT Chooser switched: specialist → D_w06 (uses both number-1 and number-2)

Public-safe report. No private endpoints, no IP, no internal paths.

## 1. Why this change

After 3-out-of-3 regions missed today (2026-06-02), the owner asked to dig deeper for MN/MT and to specifically test whether the secondary number (`top2`) carries usable signal. A 92-day ex-ante walk-forward analysis on MN gave clear evidence:

- Per-model hit rate of the secondary number is 41–50%, comparable to the primary (44–56%).
- 100% of past 92 days had at least one model whose secondary number was inside the actual draw — the secondary signal is consistently present.
- The current single-number selector for MN ignores the secondary entirely.

Six aggregator candidates were backtested for MN:

| Selector | MN 90d | MN 30d |
|---|---|---|
| Live (specialist, current) | 45% | 42% |
| Consensus top1 | 50% | 55% |
| Top1+Top2 unweighted | 46% | 48% |
| **D_w06 (top1×1.0 + top2×0.6)** | **48%** | **52%** |
| Weighted by per-model WR | 46% | 45% |
| Top-K best models only | 41% | 42% |

D_w06 was chosen over plain consensus because it directly answers the owner's request to leverage the secondary number while still prioritizing the primary. It improves MN by +3 pp on the 90-day window and +10 pp on the recent 30-day window.

MT and MB selectors are NOT changed (the data does not support changing MT, and the owner asked to handle MB separately later).

## 2. Implementation

A new standalone read-only module computes the D_w06 pick for one region on one date by aggregating across all models that predicted that day:

- score(tail) = 1.0 × (count of models with tail as top1) + 0.6 × (count of models with tail as top2)
- pick = tail with highest score
- guarded: refuses to pick if fewer than 5 models contributed; on any error returns no-pick so the caller falls back to the official top1.

The existing per-region override config was edited to point MN at the new "d_w06" chooser. The previous "specialist" code path was kept untouched so rollback is a one-line config flip. MT and MB config unchanged.

## 3. Safety verification

- py_compile passed on local and on the production server.
- Service restart healthy: login + health endpoints return 200.
- Service log post-restart: no error / traceback / failure entries.
- Hash of all four official prediction tables IDENTICAL before vs after the deploy → zero data drift.
- Dry-run on production data (no DB write) verified:
  - MN under D_w06 would have picked tail 28 today (28 models contributed).
  - MT under nt_consensus picked 78 (no change in behavior).
  - MB under hot30 picked 14 (no change in behavior).

## 4. Rollback paths

Two independent ways to revert without redeploying anything new:

- Soft rollback: flip a module-level boolean inside the new file to False; the caller automatically falls back to the official top1.
- Hard rollback: change the override config to point MN back at "specialist" (the original code path is still present), or restore the saved `.pre` copy from the backup folder taken at 21:55.

## 5. Watch plan

Today's MN bundle had already been written this morning before the deploy, so the change does not affect today's outcome. The first live application is tomorrow's MN cycle (2026-06-03, 04:00 local). I will surface results each morning for 7 days. Auto-recommendation thresholds:

- < 35% hit-rate over the first 7 live days → recommend rollback.
- ≥ 50% → recommend keeping.
- 35–50% → recommend extending the watch by another 7 days.

## 6. Status

`PUBLIC_SAFE` — no IP, no internal paths, no provider keys, no DB DDL exposed, no private repo references. Numbering note: the new code file is named with version 10672 (pinned earlier). This CHANGELOG entry is V10676 because parallel work in another chat already used 10672–10675 for a separate rule-registry effort; the file name is kept as-is to avoid breaking references in code and docs.
