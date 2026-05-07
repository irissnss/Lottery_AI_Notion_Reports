# Shadow Prompt Specs — V78

## Files Created

| Region | File | Purpose |
| --- | --- | --- |
| MN | `web/backend/prompts/shadow/MN_AI_REGION_SPECIALIST_PROMPT_SHADOW_V1.md` | Lag-1/lag-2 + V67/V73 exploit-aware specialist |
| MB | `web/backend/prompts/shadow/MB_AI_REGION_SPECIALIST_PROMPT_SHADOW_V1.md` | Cold-streak/regime-shift + volatility + uncertainty specialist |
| MT | `web/backend/prompts/shadow/MT_AI_REGION_SPECIALIST_PROMPT_SHADOW_V1.md` | Consensus-first specialist, protects MT stability |

## Contract

- Shadow only, not production prompt.
- No provider calls in V78.
- Output rows default `output_eligible=0`, `diagnostic_only=1`, `owner_approved=0`.
- Strict JSON output schema requested from future provider calls:
  `bt`, `lo2`, `lo3`, `xien2`, `xien3`, `confidence`, `selected_reason`,
  `signals_used`, `signals_rejected`, `herd_warning`, `regime_shift_warning`,
  `would_override_official`, `explanation_short`.

## Why Shadow Prompts

Production prompt currently includes broad source-prize, rule, statistics, and generic anti-herding guidance, but it does not explicitly include V67/V70/V73 candidates, agreement_count, current fast incident state, or region-specific doctrine from V77/V78. V78 therefore adds versioned shadow prompts and a dry-run context/audit materializer instead of touching official prompt.
