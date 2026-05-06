# V52.2 Measurement Backfill Rollup

- Tables: {"mt_model_hit_output_drop_shadow": 301, "loz_selector_shadow": 3273, "model_latency_cost_audit_daily": 3273}

## Window 7 days

### MT Drop By Stage

| Stage | Rows | Model hits | Token | No-token | Shadow |
|---|---:|---:|---:|---:|---:|
| LOZ_LINE_SELECTION_MISS | 17 | 25 | 0 | 23 | 2 |
| AI_SIGNAL_DROPPED | 13 | 52 | 21 | 2 | 29 |
| NOT_IN_CANDIDATE_UNIVERSE | 6 | 6 | 0 | 1 | 5 |
| OFFICIAL_LO2_INCLUDED | 2 | 6 | 0 | 6 | 0 |

### Loz model-top2 vs official

| Region | Model better | Official better | Rows |
|---|---:|---:|---:|
| MB | 26 | 63 | 202 |
| MN | 41 | 58 | 201 |
| MT | 45 | 70 | 201 |

### Latency/cost availability

| Missing reason | Rows |
|---|---:|
| NO_PER_MODEL_DURATION,NO_COST_ESTIMATE,NO_TOKEN_COUNT | 604 |

## Window 14 days

### MT Drop By Stage

| Stage | Rows | Model hits | Token | No-token | Shadow |
|---|---:|---:|---:|---:|---:|
| LOZ_LINE_SELECTION_MISS | 35 | 49 | 0 | 45 | 4 |
| AI_SIGNAL_DROPPED | 26 | 98 | 48 | 3 | 47 |
| NOT_IN_CANDIDATE_UNIVERSE | 22 | 28 | 0 | 3 | 25 |
| OFFICIAL_LO2_INCLUDED | 3 | 9 | 0 | 9 | 0 |

### Loz model-top2 vs official

| Region | Model better | Official better | Rows |
|---|---:|---:|---:|
| MB | 43 | 127 | 371 |
| MN | 65 | 128 | 368 |
| MT | 107 | 81 | 366 |

### Latency/cost availability

| Missing reason | Rows |
|---|---:|
| NO_PER_MODEL_DURATION,NO_COST_ESTIMATE,NO_TOKEN_COUNT | 1105 |

## Window 30 days

### MT Drop By Stage

| Stage | Rows | Model hits | Token | No-token | Shadow |
|---|---:|---:|---:|---:|---:|
| LOZ_LINE_SELECTION_MISS | 61 | 88 | 0 | 83 | 5 |
| AI_SIGNAL_DROPPED | 55 | 176 | 104 | 5 | 67 |
| NOT_IN_CANDIDATE_UNIVERSE | 35 | 43 | 0 | 7 | 36 |
| OFFICIAL_LO2_INCLUDED | 15 | 58 | 14 | 42 | 2 |

### Loz model-top2 vs official

| Region | Model better | Official better | Rows |
|---|---:|---:|---:|
| MB | 122 | 156 | 652 |
| MN | 113 | 211 | 650 |
| MT | 140 | 198 | 646 |

### Latency/cost availability

| Missing reason | Rows |
|---|---:|
| NO_PER_MODEL_DURATION,NO_COST_ESTIMATE,NO_TOKEN_COUNT | 1948 |

## Window 60 days

### MT Drop By Stage

| Stage | Rows | Model hits | Token | No-token | Shadow |
|---|---:|---:|---:|---:|---:|
| LOZ_LINE_SELECTION_MISS | 115 | 184 | 0 | 177 | 7 |
| AI_SIGNAL_DROPPED | 112 | 282 | 195 | 14 | 73 |
| NOT_IN_CANDIDATE_UNIVERSE | 50 | 60 | 0 | 21 | 39 |
| OFFICIAL_LO2_INCLUDED | 24 | 91 | 35 | 53 | 3 |

### Loz model-top2 vs official

| Region | Model better | Official better | Rows |
|---|---:|---:|---:|
| MB | 195 | 256 | 1093 |
| MN | 231 | 321 | 1091 |
| MT | 229 | 332 | 1089 |

### Latency/cost availability

| Missing reason | Rows |
|---|---:|
| NO_PER_MODEL_DURATION,NO_COST_ESTIMATE,NO_TOKEN_COUNT | 3273 |
