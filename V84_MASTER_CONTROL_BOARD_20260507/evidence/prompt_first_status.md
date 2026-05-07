# Prompt-first / rule-phase status

## Implementation

- V78 region-specialist shadow prompts: `web/backend/prompts/shadow/MN_AI_REGION_SPECIALIST_PROMPT_SHADOW_V1.md` + MT + MB
- V78 audit materializer: `web/backend/_materialize_ai_region_prompt_shadow_audit.py` (NO provider call)
- V79 context pack augmented: AI herd, NO_TOKEN herd, V67/V70/V73 candidates, agreement_count, independent_cluster_count, region_incident_flag (in shadow context only, NOT official prompt)
- V80 rule_phase_synthesis_shadow + no_token_rule_aware_pack_shadow (12 rows each, no consumer)
- V81 provider pilot uses V78 prompts + V79 context (3 models × 3 regions)

## What is in production prompt?

- Production `gpt_analyzer.py` SYSTEM_PROMPT does NOT include V67/V70/V73 candidates / agreement_count / no_token_herd_candidate.
- These are PROMPT_AHEAD (in shadow doctrine + V81 shadow prompts) but NOT injected to production AI calls.

## Status

| Field | In docs | In code | In production prompt | Severity |
|---|---|---|---|---|
| same_region_lag1 | YES | V66/V67 shadow | NO | HIGH |
| V67 candidate | YES | V67/V79/V80 shadow | NO | HIGH |
| no_token_herd_candidate | YES | V79/V80 shadow | NO | HIGH |
| agreement_count | YES | V70/V79 | NO | HIGH |
| MB cold flag | PARTIAL | V77/V80 | NO | HIGH |
| MT consensus-first | PARTIAL | V73/V79 | NO | MEDIUM |

## Next gate

- Production prompt change is OFFICIAL_LOCKED → cần owner OK + 60d shadow proof + dossier.
- V81 pilot continues to test region-specialist prompts in shadow only.

## Status

- Code-ahead in shadow lane.
- Production prompt unchanged.
- Owner-locked for promotion.
