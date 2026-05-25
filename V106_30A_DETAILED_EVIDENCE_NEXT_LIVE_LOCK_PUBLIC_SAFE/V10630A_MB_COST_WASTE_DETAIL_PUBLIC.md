# V10630A MB Cost Waste Detail Public

Status: `COST_WASTE_CANDIDATE`.

- false_promotion rows: 12
- high_support_miss rows: 12
- model diagnostic net: -9
- hybrid net: -9
- rule strategic net: 0

Owner-gated recommendation:
- MB_AI_MODEL_FREEZE_RECOMMENDED=True
- MB_PROVIDER_CALL_BLOCK_RECOMMENDED=True
- MB_RULE_ONLY_READ_ONLY_MODE_RECOMMENDED=True
- MB_WALLET_REMAIN_ZERO=true

## False promotion row sample
| date | candidate_tail | votes | hit | high_support_miss | false_promotion | net_effect | why_failed |
|---|---|---|---|---|---|---|---|
| 2026-05-11 | 39 | 9 | False | True | True | -1 | candidate_tail did not hit actual results |
| 2026-05-12 | 36 | 11 | False | True | True | -1 | candidate_tail did not hit actual results |
| 2026-05-13 | 32 | 8 | False | True | True | -1 | candidate_tail did not hit actual results |
| 2026-05-15 | 72 | 12 | False | True | True | -1 | candidate_tail did not hit actual results |
| 2026-05-16 | 16 | 14 | False | True | True | -1 | candidate_tail did not hit actual results |
| 2026-05-17 | 81 | 11 | False | True | True | -1 | candidate_tail did not hit actual results |
| 2026-05-19 | 36 | 8 | False | True | True | -1 | candidate_tail did not hit actual results |
| 2026-05-20 | 79 | 12 | False | True | True | -1 | candidate_tail did not hit actual results |
| 2026-05-21 | 10 | 6 | False | True | True | -1 | candidate_tail did not hit actual results |
| 2026-05-22 | 38 | 8 | False | True | True | -1 | candidate_tail did not hit actual results |
| 2026-05-24 | 16 | 17 | False | True | True | -1 | candidate_tail did not hit actual results |
| 2026-05-25 | 38 | 18 | False | True | True | -1 | candidate_tail did not hit actual results |
