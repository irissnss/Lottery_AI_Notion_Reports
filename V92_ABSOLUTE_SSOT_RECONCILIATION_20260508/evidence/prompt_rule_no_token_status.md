# V91 — Prompt / Rule / No-token status

Generated 2026-05-08T01:19:20+07:00

## Layer audit

| Layer | Production | Shadow | Evidence | Accuracy signal | Risk | Next action |
|---|---|---|---|---|---|---|
| SP-4.0 SYSTEM_PROMPT | YES (active) | — | gpt_analyzer.py L157 | OFFICIAL baseline | LOW (locked) | DO_NOT_TOUCH |
| CP-7.9 CORE_POLICY | NO (ARCHIVE_ONLY) | — | gpt_analyzer.py L256-305 | declared but not injected | LOW | KEEP_ARCHIVE |
| RR-16.4 REASONING_RULEBOOK | YES | — | gpt_analyzer.py L308-520 | active for all AI calls | LOW (locked) | DO_NOT_TOUCH |
| CTX-16.4 CONTEXT_PACK | YES | — | build_context_pack() | active | LOW | DO_NOT_TOUCH |
| PB-18.0 PHASE-FIRST GATE | YES (cohort-gated) | — | PFG-20260505-E (8 models) | trace fields available | MED | KEEP active for cohort |
| MN_V78_SHADOW prompt | — | YES | web/backend/prompts/shadow/MN_*.md | V81 pilot 3 models converge V67/V73 | LOW shadow | WAIT 14d natural live |
| MT_V78_SHADOW prompt | — | YES | MT_*.md | V81 MT consensus stable | LOW shadow | WAIT 14d natural live |
| MB_V78_SHADOW prompt | — | YES | MB_*.md | V81 MB honest cold acknowledge | LOW shadow | WAIT 14d natural live |
| V81 provider pilot | — | OWNER_APPROVED | 3 models × 3 regions × 2d | 18/18 OK 0 break 3 saves | LOW shadow | WAIT 7d→14d |

## Production prompt content NOT yet updated with

- V67 candidate field
- V70 agreement_count
- V73 hybrid tier
- no_token_herd_candidate
- MB cold flag
- MT consensus-first flag
- cluster_weighted_tail

→ All these are in **shadow** lane only (V78/V79/V80/V81). Production prompt remains OFFICIAL_LOCKED.

## Rule status

- mined_rules: weekly Mon 00:30 VN
- mined_rule_effectiveness: nightly 20:10 VN
- 12W/16W rolling windows: ACTIVE
- PB-18 classify_rule_state: ACTIVE for cohort-gated models
- 4 rule-shadow methods:
  - rule_phase_evidence_v1: DESTRUCTIVE_BIAS_MT (drop from promotion)
  - rule_injection_contract_shadow_v1: DESTRUCTIVE_BIAS_MT (drop from promotion)
  - rule_phase_synthesis_shadow (V80): NO CONSUMER (intentional)
  - no_token_rule_aware_pack_shadow (V80): NO CONSUMER (intentional)

## No-token status

- 7 NO_TOKEN models active output-eligible (LSTM/XGB/RF/SmartML/SmartEnsemble/Combo-NoToken/Meta-Learning)
- 60d region delta: MN +3.4pp / MT +8.3pp / MB -3.3pp → REGION_SPECIFIC only
- Global floor change: BLOCKED
- V79 NO_TOKEN floor + cluster cap: shadow only 4d
- V80 no_token_rule_aware_pack: shadow only no consumer

## Next action

- KHÔNG modify production prompt.
- 14d (2026-05-21): nếu V81 shadow prompt + V79 cluster sustain lift → trình owner dossier (test-lane voter only, NOT official).
- 30d (2026-06-06): full 30d Wilson CI verify cho MN.
- 60d (2026-07-06): full 60d Wilson CI verify cho MB SPECIALIST_ROSTER.
