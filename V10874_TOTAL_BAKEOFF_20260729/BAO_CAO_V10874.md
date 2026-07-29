# V10874 — Fifteen Total methods tried, and the measurement bug that made Total promise more than it delivered

Owner, 29 July 22:56:

> vấn đề total trước giờ anh đã nhắc rất nhiều lần rồi mà em sao anh nhắc lại cứ mơ hồ không biết gì
> ah em? Các phương pháp cơ chế total cần làm rõ đã nhắc nhiều lần và cần tư duy thử các phương
> pháp khác nhau để đạt hiệu quả nhất rồi mà em

The owner had already asked the direct version on 18 July 22:00 — *"thử hết phương pháp chưa"* —
and it had never been answered with a table. This session answers it, and finds something bigger
along the way.

## The bake-off

Fifteen aggregation rules scored on identical data with a train and a hold-out window: coverage
(M1), coverage plus rules screen (M2s), Borda over top-3, Borda damped by family, a contrarian
rule, family-damping at exponents 0.25 / 0.33 / 0.50 / 0.75 / 1.0, secondary-pick weights 0.3 /
0.5 / 0.7, family plus rules, family minus herd, and family plus rules minus herd.

Train 1 May to 30 June, n = 183. Hold-out 1 July to 29 July, n = 87.

## The bigger finding: the rules-union backtest leaks

The first run put the rules-screened methods far ahead. That result is not usable.

`v10821_total_v2_daily.rules_union_json` is materialised at **20:50, after the draw**, while the
live lane computes its union **before** the draw. Rebuilding M2s from the post-draw union
reproduces the real lane's pick only **69.4%** of the time.

The decisive test, on the **same 33 days**, same formula, only the union source differing:

| Source of the rules union | Hits | Rate |
|---|---|---|
| Reconstruction using the **post-draw** union | 16 / 33 | **48.5%** |
| The **real pre-draw lane** as persisted | 12 / 33 | 36.4% |
| Official M0 | 11 / 33 | 33.3% |

The post-draw union inflates the result by roughly **12 percentage points**.

This explains a puzzle the owner has been circling since 18 July: the M2s backtest promised +15pp
and the forward record delivers about +3pp. The gap was never the method degrading — it was the
backtest being scored with information the lane could not have had.

Every Total backtest figure built on that union has to be treated as **not reproducible pre-draw**
until rebuilt from a time-stamped union: the M2s 165-day claim (+10 / +8.3 / +15pp) and the Total
V3 180-day claim (+15.2pp).

**The M2s promotion gate is holding correctly.** On pre-draw truth, n = 33, M2s 36.4% against M0
33.3%, a lift of **+3.1pp**, below the +5pp threshold. Continuing to wait is the right call.

## Leak-free leaderboard

Removing every method that touches the union. The `− herd` screen stays in, because
`herd_chase_d1` uses only the previous day's results, which are available before the draw.

| Method | Train 183d | Hold-out 87d |
|---|---|---|
| M1 coverage | **70** | 28 |
| family exponent 0.75 | 68 | 31 |
| Borda top-3 · family exponent 1.0 | 67 | 28 |
| **family exponent 0.50 — DEHERD_V1, currently live** | 66 | **33** |
| family exponent 0.5 minus herd | 63 | **34** |
| M0 official | 57 | 22 |

`M1 coverage` wins the training window and then collapses out of sample, 70 down to 28. That is a
textbook overfit and a warning about trusting any single-window ranking.

`DEHERD_V1`, the method already running in the lane, is stable across both windows. The `− herd`
variant leads the hold-out by exactly one event over 87 days, which is noise and **not enough to
justify opening a second lane**.

## The de-herd lane itself is clean

Since the union leak was real, the same class of error had to be ruled out for `DEHERD_V1`. Its
backfill reads `main_numbers`, which can be rewritten by the cascade re-runs. Audit result:

- The cascade only flows in the legal direction. Miền Trung consumes the Miền Nam result, Miền Bắc
  consumes Miền Nam and Miền Trung. There are no Miền Nam rows sourced from `post_mt` or `post_mb`,
  and no Miền Trung rows sourced from `post_mb`.
- Every July write lands before its own region's draw: Miền Nam latest 04:34 against a 16:15 draw,
  Miền Trung 17:00 against 17:15, Miền Bắc 17:48 against 18:15.

So the +7.9pp over 267 days stands.

## Decision

Fifteen methods tried; none that is leak-free beats the one already running. Keep a single
variable and let `DEHERD_V1` complete its 21 forward days to 19 August. If it clears the gate, the
`− herd` variant becomes the natural second step.

No runtime change was made. Evidence:
`artifacts/v10874_total_bakeoff/V10874_TOTAL_BAKEOFF.json`.
