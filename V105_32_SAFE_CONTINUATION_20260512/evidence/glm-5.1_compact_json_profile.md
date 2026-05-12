# Proposal — `glm-5.1_compact_json_profile`

Generated: 2026-05-12 12:18 VN  
Status: `OPEN P1 / OWNER_GATE`  
Runtime action: proposal only. No provider/manual AI call was made.

## Reason

`glm-5.1` is not globally dead: earlier rows have valid numbers. The current MN 2026-05-12 shadow profile failed because the model received a heavy full-context prompt and returned empty content with `finish_reason=length`.

Current evidence from V105.31:

| Evidence | Value |
|---|---|
| Provider route | OpenRouter `z-ai/glm-5.1` |
| Runtime profile | `FULL_CONTEXT` |
| Context injected | `LANE-TEST-SHADOW-CTX` 11358 chars + reasoning rulebook |
| Token setting | `max_tokens=24576` |
| Response | 0 chars |
| Finish reason | `length` |
| DB policy | persisted diagnostic empty row, no fabricated numbers |

## Proposed Profile

| Field | Policy |
|---|---|
| Profile name | `glm-5.1_compact_json_profile` |
| Scope | shadow-only |
| Prompt | short JSON-only instruction |
| Context | reduced source facts only; no long reasoning rulebook |
| Output | max 2 tails |
| Explanation | forbidden |
| Chain-of-thought | forbidden |
| Reasoning text | short `reason_code` only |
| Promotion | never official until stable 7/14 natural days and owner OK |

Strict schema:

```json
{
  "main_numbers": ["NN", "NN"],
  "confidence": 0.0,
  "reason_code": "short"
}
```

## Failure Policy

| Consecutive result | Handling |
|---|---|
| 1 `finish_reason=length` | Persist `PERSISTED_DIAGNOSTIC_EMPTY`; no missing row; no fake numbers |
| 2 consecutive length failures | Mark `SHADOW_PROBATION` |
| 3 consecutive length failures | Compact-profile-only or disable from `shadow_auto_eval` |

Owner gate: runtime profile change and any new provider test both require explicit owner approval.
