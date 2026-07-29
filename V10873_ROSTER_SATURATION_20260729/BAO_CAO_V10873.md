# V10873 — "Models that don't take part in Total are waste": measured, and the answer is not what it looked like

Owner:

> các model nhiều mà không tham gia total thì cũng lãng phí nha em nên kiểm soát tốt để thay thế
> loại bỏ bớt vừa cắt giảm chi phí vừa tinh gọn nhưng vẫn chính xác nâng cao hiệu quả hơn

Three separate measurements were run against that concern. Two of them contradicted the
expectation, and the third found a much bigger problem.

## 1. No model is idle

For every shadow model, how often does its first pick appear in *any* published output — official
bundle, K-lane, Total, or `/choi`? Window 1 to 29 July.

Every one of them lands between **64% and 92%**. With 25 models and only 30 to 40 plausible tails
on a board each day, agreement is the norm. Nothing is running without taking part.

## 2. The official roster is already minimal

**Leave-one-out over 214 region-days.** How often does removing a single model change the final
pick?

| Model | Days changed |
|---|---|
| `claude-sonnet-4-6` | 20.3% |
| `combo-super` | 17.5% |
| `deepseek-reasoner` | 14.3% |
| `gemini-2.5-flash` | 13.6% |
| `gpt-5.4` | 13.2% |
| `claude-opus-4-6` | 11.0% |
| `gpt-5-mini` | 10.8% |
| `gemini-2.5-pro` | 10.3% |
| the seven ML lanes | 1.9% – 3.7% |

At first reading that says the ML block is dead weight. It is not.

**Group cuts over 212 region-days**, scored with the de-herd selector:

| Roster | Models | Hits | vs current |
|---|---|---|---|
| Current 15 | 15 | 80 | — |
| Drop `lstm` | 14 | 80 | **0** |
| Drop `lstm` + `meta-learning` | 13 | 76 | −4 |
| ML reduced to 3 | 11 | 77 | −3 |
| ML reduced to 2 | 10 | 76 | −4 |
| ML reduced to 1 | 9 | 74 | −6 |
| Drop the whole ML block | 8 | 73 | **−7** |
| Drop `gpt-5-mini` | 14 | 73 | **−7** |

The seven ML lanes are individually redundant but collectively load-bearing. They also run locally
at **$0**, so cutting them would save nothing anyway.

**Replacement test.** `lstm` is the only model that can be removed for free, so can it be swapped
for something better?

| Change | Effect |
|---|---|
| `lstm` → `gemini-3.5-flash` (strongest model in the pool) | **0** |
| `lstm` → `gpt-oss-120b` | **0** |
| `lstm` → `qwen3.7-max` | −1 |
| `lstm` → `gpt-5.5` | −1 |
| Add a 16th model | **0** |

**The selector is saturated at 15 models.** Adding, dropping or swapping no longer moves the
output. This is the same conclusion V10871b reached from a different direction, now confirmed
three ways.

**One gate check.** `gpt-5-mini` is dropped by `bt_gate` on 13% of bundles, which looked like paid
work being thrown away. It is not: on those 34 days its own first pick hit only **17.6%** against
its normal ~32%. The gate is correctly identifying its bad days.

## 3. The real waste was cost concentration

Total shadow spend from 1 to 29 July: **$264.74**.

| Model | Cost | Self-hit | $ per participation |
|---|---|---|---|
| **`grok-4.20-multi-agent`** | **$225.14** | 34.9% | **$3.042** |
| `gpt-5.5` | $12.87 | 27.7% | $0.169 |
| `qwen3.7-max` | $5.73 | 35.1% | $0.094 |
| `gemini-3.5-flash` | $2.08 | **40.0%** | $0.035 |
| `glm-5.1` | $1.51 | **40.5%** | **$0.023** |

One model consumed **85% of the entire shadow budget** at roughly **130× the median unit cost**,
because it burns an average of 1.51 million tokens per call. In return its quality is squarely
mid-pack: 34.9% self-hit, BT lift +1.5pp at p=0.260 which is not significant, and 86%
participation which is average.

The owner approved retiring it. This is not the earlier rejected argument about one model's price
tag — it meets the owner's own three criteria: reduce **total** cost, make the roster easier to
control, lose no quality. Shadow goes from 12 to 11, official stays at 15, and monthly shadow spend
falls from roughly $274 to roughly $41.

The best value in the pool is `glm-5.1` at 40.5% self-hit for $0.023 per participation, followed by
`gemini-3.5-flash` at 40.0% for $0.035.

## What this changes for the roadmap

No further roster cuts or swaps will be proposed until the aggregation changes, because the optimal
roster depends on the selector. The remaining lever is the de-herd lane, under forward test until
19 August.

Verification: official table hashes identical before and after, cross-module contract passes,
health 200, `/du-doan` 200, official 15 and shadow 11.
