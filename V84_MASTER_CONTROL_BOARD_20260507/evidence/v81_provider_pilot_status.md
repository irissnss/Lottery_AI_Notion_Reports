# V81 provider shadow pilot status

## Implementation

- Materializer: `web/backend/_materialize_ai_region_specialist_provider_shadow_pilot.py`
- Table: `ai_region_specialist_provider_shadow_results` (21 rows = 18 OK + 3 gpt-5-mini errors)
- Cron: 19:14 VN daily
- Models active: deepseek-chat (FAST_CHEAP), claude-sonnet-4-6 (REASONING), gemini-3-flash (NEW_CHEAP)
- Models swapped: gpt-5-mini → deepseek-chat (VPS OPENAI 401 issue, ops-only)

## 2-day pilot (2026-05-06 + 2026-05-07)

- 18 calls / 18 parse_status=OK (after swap) / 0 contract violations.
- Per-model: each scored hits=3/6, would_save=1, would_break=0, hi_conf=2-3, lo_conf=2.
- MN 2026-05-07: all 3 models converge V67/V73 tail 95 (vs OFFICIAL 94 LOSE) — would_save=1 each.
- MT 2026-05-07: all 3 models pick OFFICIAL=88 (consensus-first stable).
- MB 2026-05-07: all 3 models pick OFFICIAL=20 with LOW confidence + herd warnings (honest cold).

## Maturity gate

- 2d → LIVE_LIMITED_2D.
- 7d gate: 2026-05-14.
- 14d gate: 2026-05-21.
- 30d gate: 2026-06-06.
- 60d gate: 2026-07-06.

## Pass condition for V81 promotion candidate

- 14d natural live: would_save > would_break per model + per region.
- MT no_break > 90%.
- MB confidence calibration matches outcome.
- Owner OK + dossier required.

## Status

- DEPLOYED + 2d live.
- Waiting natural cron 19:14 VN proof.
- Owner-locked for promotion.
