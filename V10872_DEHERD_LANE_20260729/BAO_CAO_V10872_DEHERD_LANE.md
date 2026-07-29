# V10872 — A de-herding selector, running for real in a lane

Owner instruction:

> Live lâu lắm rồi, đo nhiều rồi mà em vẫn không moi ra được vấn đề để xử lý cứ lẩn quẩn mãi kiểu
> này. Phải là C và hơn thế nữa chạy thật với các phương pháp cơ chế đo lường ở 1 luồng nào đó đi
> chứ còn chờ gì nữa

Fair criticism. The evidence had already identified the disease; the response had been another
measurement table. This step builds the competing method and puts it in a live lane.

## The disease

V10871b established that on 65.6% of days the official pick misses while the winning tail is
already some model's first choice, and that the weighted selector performs no better than a plain
majority vote.

The cause is correlated voting blocks. The seven machine-learning lanes share engineered features
and agree with each other 38–49% of the time, so they behave like one very loud voter. Miền Trung
on 28 July is the template: eight models led with 87, five ML lanes led with 39, 39 won the vote
and lost the draw.

## The rule

    score(number) = Σ over families of √(weight that family gave the number)
    weight = 1.0 for a first pick, 0.5 for a second pick

Families group models by signal source: ML (the seven feature-sharing lanes), Anthropic, OpenAI,
Google, DeepSeek, Hybrid. A family of seven agreeing counts √7 ≈ 2.6 instead of 7, while five
distinct families agreeing counts 5. Broad cross-family agreement now outranks one loud block.

## Validation before going live

Five variants were tried and the best selected, which risks fitting noise, so two periods were
held out of that search entirely.

| Window | n | Official | De-herd lane | Wins / losses |
|---|---|---|---|---|
| 1 May – 15 Jun (**held out**) | 112 | 32.1% | **36.6%** | 15 / 10 |
| 16 Jun – 4 Jul (**held out**) | 38 | 31.6% | **42.1%** | 6 / 2 |
| 5 Jul – 28 Jul (used for tuning) | 61 | 26.2% | **34.4%** | 6 / 1 |

Full backfill along the production path, 267 region-days: official **29.2%** (78/267) against the
lane's **37.1%** (99/267), a gain of **7.9 percentage points**. Wins 38, losses 17 across 55
decisive days, McNemar one-sided p ≈ 0.0035.

Positive in all three regions:

| Region | Official | De-herd | Wins / losses |
|---|---|---|---|
| Miền Nam | 35 / 89 | **43 / 89** | 10 / 2 |
| Miền Trung | 30 / 89 | **37 / 89** | 16 / 9 |
| Miền Bắc | 13 / 89 | **19 / 89** | 12 / 6 |

Miền Bắc, the weakest region and the owner's biggest complaint, improves from 14.6% to 21.3%.

## Which lane it runs in

The owner asked what each of the four lanes is actually for. The assignment used here:

| Lane | Role |
|---|---|
| Official `/du-doan` | **Apply** — the published number, locked at 15 models |
| K-lane `/du-doan-test` | **Change and test** — the only place a new variable is introduced |
| Total V2 / V3 | **Measure** |
| `/choi` | **Recommend play** |

So the de-herd selector goes into the K-lane, as `{REGION}_DEHERD_V1` in `du_doan_test_bundles`,
pre-draw, `test_only=1`, `output_eligible=0`. It never writes `final_bundles` and never touches
`/choi`. Cron at 15:51 for Miền Nam, 17:00 for Miền Trung, 18:00 for Miền Bắc — all before their
draws — plus a settle pass at 21:15 once results are in.

First live row, 29 July Miền Nam: `BT 96`, `lo2 ["96","00"]`, 15 models across 6 families. Same as
official today, so no divergence yet.

## Promotion threshold, written in advance

At least 21 forward days with the lane ahead of official on the special-prize tail and not behind
in any single region, then an owner signature. If the lane loses over those 21 days, it closes and
the reason a 267-day backfill did not carry into forward results gets written down.

## Two premium shadow lanes

The owner also approved adding two stronger, more expensive shadow models. OpenRouter was probed
on 29 July: 367 models, filtered to those with reasoning support, context of at least 200k, and
never previously run here, giving 18 candidates. The owner chose `claude-opus-5-fast` (1M context,
$10 per million in, $50 out) and `gpt-5.6-sol-pro` (1.05M context, $5 in, $30 out) — deliberately
two different families so they do not add correlation.

Both carry `first_run_date` 2026-07-30 with no backfill. Shadow goes from 10 to 12; official stays
at 15. They will be judged by `v10871_model_quality_ledger` after at least 30 rows.

Worth stating plainly: given the V10871b finding, adding models is not expected to raise official
accuracy on its own, because the selection layer is what discards the signal. Their value is in
feeding the K-lane and supplying future promotion candidates.

## Verification

Hashes of `predictions`, `final_bundles`, `lottery_results` and `model_daily_eval` are identical
before and after deployment. Cross-module contract passes, `/api/health` returns 200, `/du-doan`
returns 200, the new admin endpoint returns 401 unauthenticated, and all four cron lines are
installed.
