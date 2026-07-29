# V10871b — The owner approved the swap; the swap failed his own condition

Owner instruction:

> Đổi luôn đi em nhưng cần làm rõ phương pháp dùm anh để đảm bảo phải chỉ có nâng cao độ chính xác
> hơn và đồng thời vẫn đo song song làm sao phải kiểm soát tốt nhất cho anh. Áp vào luồn nào mình
> có 4 luồng lận mà em nên luồn nào đổi , luồng nào áp dụng , luồn nào đo lường , luồng nào khuyên
> chơi v.v.. 4 luồng phải có tác dụng của nó chứ để đó cho vui sao em?

The approval carried a condition: the swap must strictly raise accuracy. That condition was tested
before touching anything, and the swap did not pass it. Nothing was swapped.

## The test

Backfill counterfactual across 5 to 28 July, 61 region-days. Each arm is scored with the **same
selection function the M2 lane already uses** (`_coverage_pick`), fed the **same pre-draw
prediction rows**, so the only variable is the roster.

| Arm | BT hits | BT % | ANY % |
|---|---|---|---|
| A — current 15 | 28 / 61 | **45.9** | **70.5** |
| B — `gemini-3.5-flash` replaces `gpt-5-mini` | 27 / 61 | 44.3 | 68.9 |
| C — `qwen3.7-max` replaces `gpt-5-mini` | 27 / 61 | 44.3 | 68.9 |
| D — both in, drop `gpt-5-mini` and `claude-sonnet-4-6` | 28 / 61 | 45.9 | 67.2 |

A roster change altered the output on only **3 of 61 days**. On the single day where the arms
diverged into a win and a loss, the current roster won: 18 July Miền Trung, A picked 46 and hit
while B picked 26 and missed.

The lesson is that a model's solo quality does not carry into the aggregate. `gemini-3.5-flash`
genuinely is the strongest single model in the pool at +8.2pp, and putting it into the official
field still changed almost nothing, because the aggregation rarely lets one voter decide.

## The herding worry was backwards

The concern before testing was that official already has two Gemini models, so adding a third
would deepen the correlated-block problem that cost Miền Trung on 28 July. Measured first-pick
agreement says the opposite.

| Model | Average first-pick agreement with official |
|---|---|
| `gpt-oss-120b` | 9.6% |
| `gemini-3.5-flash` | 12.5% |
| `qwen3.7-max` | 12.7% |
| Baseline between official pairs | **13.7%** |
| `gpt-5.5` | 17.0% |

The candidates are *more* independent than the average official pair. The real correlated blocks
are already inside the official field:

| Pair | Agreement |
|---|---|
| `claude-opus-4-6` + `claude-sonnet-4-6` | 54.8% |
| `combo-no-token` + `meta-learning` | 49.3% |
| `smart-ensemble` + `smart-ml` | 45.3% |
| `combo-no-token` + `random-forest` | 45.3% |
| `gpt-5-mini` + `gpt-5.4` | 44.4% |

## The actual bottleneck

Same 61 region-days, comparing how different selection rules convert the same pool into a pick:

| Selection rule | BT hits | % |
|---|---|---|
| Official `weighted_voting_wr` | 16 / 61 | **26.2** |
| Plain majority of first picks, all 15 | 18 / 61 | 29.5 |
| Majority of the ML block only, 7 models | 19 / 61 | 31.1 |
| Majority excluding the ML block, 8 LLMs | 16 / 61 | 26.2 |

The production weighted selector is **no better than a plain majority vote** on identical inputs.
A gap of 16 versus 18 versus 19 at n=61 sits inside noise, so the safe statement is "no better",
not "worse" — but there is certainly no evidence the weighting is earning its complexity.

More striking: on **40 of 61 days, 65.6%**, the official pick missed while the winning number was
already sitting in the pool as some model's first choice. The Miền Trung case on 28 July, where
eight models led with 87 and the official chose 39, is not an unlucky day. It is the normal
failure mode.

## What this means for the roadmap

Cutting and adding models remains useful hygiene: it keeps the roster controllable and removes
lanes that drag the average. But it is close to irrelevant for official accuracy, because the
selection layer discards most of the signal the pool already contains.

The next accuracy work should target the selector, measured in shadow with a written action
threshold and at least 21 forward days before any production change is proposed. Filed as
`FU-V10871B-SELECTOR-IS-BOTTLENECK`.

Evidence: `artifacts/v10871b_swap_test/V10871b_SWAP_BACKFILL.json`. No runtime change was made in
this step.
