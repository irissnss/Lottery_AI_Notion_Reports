# V54 C-15 — Weekday Black-Spot Alert Result

> Status: `WEEKDAY_BLACKSPOT_ALERT_DEPLOYED_MEASUREMENT_ONLY`  
> File: `web/backend/_materialize_weekday_blackspot_shadow.py`  
> Table: `weekday_blackspot_shadow`  
> Anchor: 2026-05-03, window 30d

## Confirmed Black Spots

| Region | Weekday | BT | LO2_FULL | Label |
|---|---|---:|---:|---|
| MB | Wed | 0/4 | 0/4 | `WEEKDAY_BLACK_SPOT_CONFIRMED` |
| MB | Fri | 0/4 | 0/4 | `WEEKDAY_BLACK_SPOT_CONFIRMED` |
| MT | Mon | 0/4 | 0/4 | `WEEKDAY_BLACK_SPOT_CONFIRMED` |
| MT | Fri | 0/4 | 0/4 | `WEEKDAY_BLACK_SPOT_CONFIRMED` |

Other risk labels:

- MB Mon/Tue/Thu/Sun: `WEEKDAY_STRUCTURAL_RISK`
- MN Wed/Fri: `WEEKDAY_STRUCTURAL_RISK`
- MT Tue/Wed: `WEEKDAY_STRUCTURAL_RISK`

## Safety

- Reads only `final_bundles`.
- Writes only `weekday_blackspot_shadow`.
- Does not alter `/du-doan`.

## Next UI Step

Show this as a `/du-doan-test` admin panel with warning chips, not as a production rule.
