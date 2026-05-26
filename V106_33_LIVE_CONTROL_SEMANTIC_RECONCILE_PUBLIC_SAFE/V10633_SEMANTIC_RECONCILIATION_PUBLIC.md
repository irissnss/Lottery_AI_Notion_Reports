# V10633 Semantic Reconciliation Public

| claim | SURFACE_CREATED | DATA_ROW_EXISTS | DATA_USABLE | SIGNAL_PRESENT | OUTPUT_IMPACTED | OFFICIAL_IMPACTED | semantic_status |
|---|---|---|---|---|---|---|---|
| MB_RULE_ONLY_AGGRESSIVE_SHADOW | True | True | True | NOT_FIRED | False | False | SURFACE_CREATED_SIGNAL_NOT_FIRED |
| MB_NO_TOKEN_BASELINE_SHADOW | True | False | False | NOT_PROVEN | False | False | SURFACE_CREATED_DATA_NOT_USABLE |
| MB_HIGH_SUPPORT_MISS_SUPPRESSOR_SHADOW | True | True | True | NOT_PROVEN | False | False | DATA_EXISTS_SIGNAL_NOT_PROVEN |
| MB_FALSE_PROMOTION_KILL_GATE_SHADOW | True | True | True | NOT_PROVEN | False | False | DATA_EXISTS_SIGNAL_NOT_PROVEN |
| MB_COST_VALUE_SCORECARD | True | True | True | NOT_PROVEN | False | False | DATA_EXISTS_SIGNAL_NOT_PROVEN |
| MB_NO_IMPACT_ON_MN_MT_PROOF | True | True | True | PROOF_ONLY | False | False | DATA_USABLE |
| MN trace | True | True | True | PRESENT | True | False | OUTPUT_HIT_SOURCE_NOT_PROVEN |
| MT trace | True | True | True | PRESENT | True | False | OUTPUT_HIT_SOURCE_NOT_PROVEN |
| next live runbook | True | True | True | NOT_PROVEN | False | False | DATA_EXISTS_SIGNAL_NOT_PROVEN |
