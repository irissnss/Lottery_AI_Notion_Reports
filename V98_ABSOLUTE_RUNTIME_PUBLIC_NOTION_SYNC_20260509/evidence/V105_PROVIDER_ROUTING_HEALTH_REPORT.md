# V105 — Provider Routing Health Report

## Fixed

- Replaced invalid V104.1 route `gpt-5-pro/openai`.
- V105 route is `gpt-5.5/openrouter`, using `OPENROUTER_KEY_GPT55` / DB `openrouter_key_gpt55`.
- GPT 5 mini and GPT 5.4 remain OpenAI platform-key slots.
- Claude MT no longer truncates after prompt trim + `MAX_OUTPUT_TOKENS=3000`.

## Real Run

| Region | Claude Opus | GPT 5.5 OpenRouter | Gemini 2.5 Pro |
|---|---|---|---|
| MN | OK 15 decisions | OK 15 decisions | PARSE_FAIL row |
| MT | OK 15 decisions | OK 15 decisions | `PROVIDER_EMPTY_RESPONSE` |
| MB | OK 15 decisions | OK 15 decisions | `PROVIDER_EMPTY_RESPONSE` |

Total calls: `9`; failed calls: `2`; rows stored: `93`.

## Current Health

`GPT_KEY_ROUTING_MISMATCH`: fixed.
`MT_CLAUDE_TRUNCATED`: fixed.
`GEMINI_EMPTY_RESPONSE`: partial, still open as provider-specific issue but no longer silent.
