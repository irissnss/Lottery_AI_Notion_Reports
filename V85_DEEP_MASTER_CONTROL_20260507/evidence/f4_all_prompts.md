# 4/8 — ALL PROMPTS + COHORTS + PROVIDER ASSIGNMENTS

## 4a. Prompt layers (8 total: 5 production-stack + 3 shadow region-specialist)

| Version | Name | Location | Scope | Purpose | Runtime active? |
| --- | --- | --- | --- | --- | --- |
| SP-4.0 | SYSTEM_PROMPT | gpt_analyzer.py L157 | Production AI calls | TOP1-FIRST discipline V8.0 (max 2 numbers, tertiary removed) | YES |
| CP-7.9 | CORE_POLICY | gpt_analyzer.py L256-305 | Confidence/anti-overclaim/MB ceiling/width | Declared but not injected | NO (ARCHIVE_ONLY) |
| RR-16.4 | REASONING_RULEBOOK | gpt_analyzer.py L308-520 | 24 rules + §24 BT North Star V16.4 | Rule injection layer | YES |
| CTX-16.4 | CONTEXT_PACK | build_context_pack() | BT model ranking + weekly livingness tiers | Context injected into AI | YES |
| PB-18.0 | PROMPT_BUNDLE / PHASE-FIRST GATE | gpt_analyzer.py PB-18 block | classify_rule_state + 8-step PHASE-FIRST GATE | Phase-first decision gate for cohort-gated models | YES (gated cohort) |
| MN_V78_SHADOW | MN_AI_REGION_SPECIALIST_PROMPT_SHADOW_V1 | web/backend/prompts/shadow/MN_AI_REGION_SPECIALIST_PROMPT_SHADOW_V1.md | MN region, V67/V73/cluster context | Shadow-only region prompt; MN doctrine (V67 eager + lag1 exploit) | SHADOW only (V81 pilot) |
| MT_V78_SHADOW | MT_AI_REGION_SPECIALIST_PROMPT_SHADOW_V1 | web/backend/prompts/shadow/MT_AI_REGION_SPECIALIST_PROMPT_SHADOW_V1.md | MT region | Shadow-only MT consensus-first doctrine | SHADOW only (V81 pilot) |
| MB_V78_SHADOW | MB_AI_REGION_SPECIALIST_PROMPT_SHADOW_V1 | web/backend/prompts/shadow/MB_AI_REGION_SPECIALIST_PROMPT_SHADOW_V1.md | MB region | Shadow-only MB cold acknowledge + diversification doctrine | SHADOW only (V81 pilot) |

## 4b. PHASE-FIRST GATE cohorts (5 total)

| Cohort ID | Models | Active period (VN) | Contract required? | Status |
| --- | --- | --- | --- | --- |
| PFG-20260417-A | gemini-2.5-flash + gpt-5.4 | 2026-04-17 → 2026-04-26 01:20 | False | RETIRED |
| PFG-20260426-B | minimax-m2.7 + gpt-oss-120b | 2026-04-26 01:21 → 2026-04-27 00:26 | True | RETIRED |
| PFG-20260427-C | minimax-m2.7 + gpt-oss-120b + gpt-5.5 + deepseek-v4-pro + deepseek-v4-flash + qwen3.6-plus | 2026-04-27 00:27 → 2026-04-28 21:04 | True | RETIRED |
| PFG-20260428-D | gpt-oss-120b + gpt-5.5 + deepseek-v4-pro + deepseek-v4-flash + qwen3.6-plus | 2026-04-28 21:05 → 2026-05-05 07:44 | True | RETIRED |
| PFG-20260505-E | gpt-oss-120b + gpt-5.5 + deepseek-v4-pro + deepseek-v4-flash + qwen3.6-plus + gemini-3.1-pro + gemini-3-flash + gemma-4-31b | 2026-05-05 07:45 → present | True | ACTIVE |

## 4c. V81 provider pilot model assignments

| Slot | Model | Provider | Purpose |
| --- | --- | --- | --- |
| FAST_CHEAP | deepseek-chat | deepseek | Fast cheap shadow pilot (swapped from gpt-5-mini after VPS OPENAI 401) |
| REASONING | claude-sonnet-4-6 | anthropic | Reasoning shadow pilot |
| NEW_CHEAP | gemini-3-flash | google | New cheap shadow pilot (GEMINI_KEY_SHADOW_NEW) |
