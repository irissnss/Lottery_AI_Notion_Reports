# V81 — OWNER-APPROVED PROVIDER SHADOW PILOT (2026-05-07)

Status: **SHADOW ONLY**. Owner OK 2026-05-07 22:02 VN cho phép gọi provider thật, KHÔNG động official.

## Goal

Đo xem 3 model AI đại diện (FAST_CHEAP, REASONING, NEW_CHEAP) khi được prompt theo doctrine vùng V78 + context V79 (AI herd, NO_TOKEN herd, V67/V70/V73, cluster-weighted) thì pick BT có khá hơn OFFICIAL không, và có giảm risk không. Mọi output ghi vào shadow table riêng.

## Models

| Slot | Model | Provider |
| --- | --- | --- |
| FAST_CHEAP | deepseek-chat | DeepSeek |
| REASONING | claude-sonnet-4-6 | Anthropic |
| NEW_CHEAP | gemini-3-flash | Google (GEMINI_KEY_SHADOW_NEW) |

`gpt-5-mini` slot ban đầu được chọn nhưng VPS OPENAI key trả 401 trên endpoint đó (vấn đề ops, không phải lỗi pilot logic). Em swap sang `deepseek-chat` để giữ slot honest. GPT-5-mini key validation track riêng.

## Pilot run

- Run for 2026-05-07 (target day), backfill 2026-05-06.
- 3 models × 3 regions × 2 days = **18 provider calls**.
- 18/18 parse_status=OK after swap.
- Hard contract honored on all rows: `output_eligible=0`, `diagnostic_only=1`, `owner_approved=1`, `shadow_only=1`, `output_impact='false'`.

## Result summary

### Per model (2-day, parse OK only)

| model_id | n | hits | saves | breaks | hi | lo |
| --- | --- | --- | --- | --- | --- | --- |
| claude-sonnet-4-6 | 6 | 3 | 1 | 0 | 2 | 2 |
| deepseek-chat | 6 | 3 | 1 | 0 | 3 | 2 |
| gemini-3-flash | 6 | 3 | 1 | 0 | 3 | 2 |

### Per region (across 3 models)

| region | n | hits | saves | breaks |
| --- | --- | --- | --- | --- |
| MB | 6 | 0 | 0 | 0 |
| MN | 6 | 3 | 3 | 0 |
| MT | 6 | 6 | 0 | 0 |


## Findings

1. **MN 2026-05-07 — All 3 models converge on V67/V73 tail 95** (would_save=1 each). Official chose 94, lost. AI herd in production also chose 94 (not 95). The V78 region-specialist shadow prompts steer providers toward V67/V73 evidence properly.
2. **MT — consensus stable**. All 3 models pick OFFICIAL=88 on 2026-05-07 (matching V73). 6/6 hits across both days. No false override risk.
3. **MB — honest cold acknowledgement**. All 3 models pick OFFICIAL=20 on 2026-05-07 with `confidence=LOW` and `herd_warning=AI_HERD_WRONG_RISK / NO_TOKEN_HERD_RISK / ALL_METHODS_COLD`. The shadow prompt successfully forces AI to admit uncertainty when all methods are cold instead of overconfidence.
4. **No false promotions**: across 18 calls, zero `would_break` events.

## Hash guard

Pre and post hashes for `predictions / final_bundles / lottery_results / model_daily_eval` are byte-identical across all 18 provider calls AND scheduler restart.

## Cron registration

- **NEW** `v81_provider_shadow_pilot` at **19:14 VN** daily (after V80 19:12). Will execute 9 calls/day. Shadow only.

## Remaining

- Natural cron proof at 19:14 VN on next live day.
- Accumulate 7-14 day rolling `would_save vs would_break` per model + region before any selector promotion proposal.
- Owner-lock holds for any official prompt/output/selector change.

