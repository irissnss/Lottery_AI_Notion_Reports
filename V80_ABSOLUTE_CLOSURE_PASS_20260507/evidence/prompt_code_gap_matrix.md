# Prompt Code Gap Matrix

| Field | In docs | In code | In prompt | In trace | Gap | Severity |
| --- | --- | --- | --- | --- | --- | --- |
| same_region_lag1 | Yes/desired | V66/V67 shadow | No official | V67 trace | Official prompt missing | HIGH |
| V67_candidate | Desired | V67/V79/V80 shadow | Shadow only | Yes | Official locked | HIGH |
| no_token_herd_candidate | Desired | V79/V80 shadow | Shadow context only | Yes shadow | Production missing | HIGH |
| agreement_count | Desired | V70/V79 | Shadow context only | Yes | Production missing | HIGH |
| MB cold flag | Partial | V77/V80 | Shadow only | Yes | Official locked | HIGH |
| MT consensus-first | Partial | V73/V79 | Shadow only | Yes | Production prompt generic | MEDIUM |
