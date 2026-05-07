# 6/8 — ALL RULES & RULESETS

## 6a. Rule mining / weekly miner

| Item | Where | Schedule | Status |
|---|---|---|---|
| Weekly Rule Mining | `web/backend/weekly_rule_miner.py` | Mon 00:30 VN | LIVE |
| Mined rules table | `mined_rules` | continuous | LIVE |
| Mined rule effectiveness | `mined_rule_effectiveness` | nightly ~20:10 VN (auto_mined_rule_eval) | LIVE |
| Verified bucket rules | `verified_bucket_rules` (105 rows) | manual | LIVE |
| Rule windows | 12W / 16W rolling | rule_engine.py | LIVE (RULE_WINDOW_TOP5_12W16W reconciled) |

## 6b. Phase-first / rule-state classification

| Item | Where | Status |
|---|---|---|
| classify_rule_state (PB-18 step) | `gpt_analyzer.py PB-18` | LIVE for cohort-gated models |
| primary_rule_group | PB-18 JSON schema | LIVE |
| secondary_rule_group | PB-18 JSON schema | LIVE |
| stale_rules | PB-18 JSON schema | LIVE |
| rules_to_downweight | PB-18 JSON schema | LIVE |
| top_source_prizes_by_region | PB-18 JSON schema | LIVE |
| strongest_source_prizes_used | PB-18 JSON schema | LIVE |
| strongest_rules_used | PB-18 JSON schema | LIVE |

## 6c. Rule-phase / rule-injection shadow methods

| Method | Table | Status | 14d verdict |
|---|---|---|---|
| rule_phase_evidence_v1 | shadow_results | LIVE 11d | DESTRUCTIVE_BIAS (MT 103 lf 139 fp) |
| rule_injection_contract_shadow_v1 | shadow_results | LIVE 10d | DESTRUCTIVE_BIAS (MT 16 lf 21 fp) |
| rule_phase_synthesis_shadow (V80) | rule_phase_synthesis_shadow | LIVE 4d | KEEP_MONITORING (no consumer) |
| no_token_rule_aware_pack_shadow (V80) | no_token_rule_aware_pack_shadow | LIVE 4d | KEEP_MONITORING (no consumer) |
| weekday_rule_strength_daily | weekday_rule_strength_daily | LIVE Wave 1 | active |

## 6d. PHASE-FIRST policy

- Cohort gate: PFG-20260505-E (8 models active).
- Contract required: True.
- Switch history: PFG-A → B → C → D → E (5 cohorts since 2026-04-17).

## 6e. Custom prompt rules (containment)

- `rule_custom_prompt` mode = `ARCHIVE_ONLY` (V20.3.x).
- Max 500 chars (containment).
- Runtime injection: NO.
