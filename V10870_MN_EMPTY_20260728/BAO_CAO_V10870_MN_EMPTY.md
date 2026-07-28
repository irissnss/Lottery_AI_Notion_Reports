# V10870 — Three empty MN models on 28 July: three different causes

## Short answer

The owner saw three empty models in the Miền Nam morning run. They are not one incident.
Each has a separate cause, and only one of them touched the official output.

| Model | Roster | Cause | Touches official |
|---|---|---|---|
| `deepseek-reasoner` | OFFICIAL | Provider truncation, `finish_reason=length` | Yes |
| `grok-4.3` | SHADOW | Voided by the PHASE-FIRST contract gate | Indirect, via MT K-lane |
| `gemini-3.5-flash` | SHADOW | Gemini API `503 UNAVAILABLE` | No |

Source: paired live sync `artifacts/live_sync/20260728_131405/manifest.json`.
This session made no runtime change.

## 1. deepseek-reasoner — the only official impact

The provider returned an empty response after 97.8 seconds with `finish_reason=length`.
The model spent its whole completion budget on internal reasoning and never emitted the final
JSON. This is truncation, not a network or key failure.

Consequence for the official bundle:

- Miền Nam published `bach_thu 95`, `lo2 ["95","54"]` at 04:19.
- `output_eligible_row_count` 15, `scoreable_model_count` **14**.
- `incomplete_bundle` true, exclusion reason `empty_or_invalid / parsed_numbers_empty`.
- This is the first time Miền Nam broke its 15/15 streak inside the PB-18.1 trial window.

Frequency over 21 days: 1 of 61 rows, about 1.6 percent. Sporadic, not systemic.

## 2. grok-4.3 — the model answered, the gate discarded it

The trace shows a valid answer: prediction `['05','81']`, `finish_reason=stop`, 20,836 tokens
of which 2,934 were reasoning tokens, prompt version PB-18.1.

It was still rejected because six required `analysis.*` fields were missing, and it failed the
same check again after an automatic repair retry. Two paid calls were made and both results
were thrown away.

Mechanism:

```
gate_contract_mode = (selected_model in PHASE_FIRST_CONTRACT_MODELS) or lane_test_shadow_pack
```

`PHASE_FIRST_CONTRACT_MODELS` has been empty since V10750, so only the lane-test shadow path
(`scheduler.py:7450`) still enforces the contract.

Over 21 days grok-4.3 is the only model that has failed this contract, twice. It also belongs to
the five shadow models that can influence official Miền Trung indirectly through the K-lane, so
this is relevant to the CP-L6 roster decision.

## 3. gemini-3.5-flash — provider outage

`Gemini API error: 503 UNAVAILABLE. This model is currently experiencing high demand. Spikes in
demand are usually temporary.` Nothing on our side failed. Frequency 2 of 61 rows, 3.3 percent.

## Full system check

- Timetable self-check: 11/11 PASS.
- Cross-module contract check: PASS.
- Health 200, service active.
- Scheduler ERROR/CRITICAL rows for 28 July: 0.
- Journal errors for 28 July: none.

Baseline context: one to three empty models per day is the normal range across the last 14 days;
25 July had three empties in Miền Trung. Today sits at the high end of that range rather than
outside it.

Day status at 13:38: Miền Nam complete, lane 95 at 05:01 and `/choi` locked `["95"]` at 13:09.
Miền Trung and Miền Bắc had only the seven 04:00 machine-learning rows, which is correct because
their AI passes run at 16:42 and 17:42.

## Additional quality finding

`gemini-2.5-flash` returned `["96","96"]`, the same number as both main and secondary pick, so its
effective coverage was one number instead of two. The bundle flagged
`duplicate_numbers_detected` as diagnostic only. Miền Nam also showed heavy herding around 95 and
96 this morning.

## Decision

The owner approved deferring both fixes. 28 July is the closing day for the PB-18.1 trial and the
CP-L6 decision, so changing a token budget or a contract gate today would introduce a new variable
on the exact day the results are read.

Two items go to tonight's CP-L6 session after closeout:

1. `deepseek-reasoner`: verify or raise the output budget so reasoning cannot consume the whole
   completion, and add an alert on `finish_reason=length`.
2. `grok-4.3`: decide whether the lane-test shadow path should keep enforcing the PHASE-FIRST
   contract for a model that already returned valid numbers, instead of paying for two discarded
   calls.

Evidence file: `artifacts/v10870_mn_empty/V10870_MN_EMPTY_2026-07-28.json`.
