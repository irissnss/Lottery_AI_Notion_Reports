# OFFICIAL PROMOTION GATE

> Test-lane → official lift requires ALL gates passed AND owner explicit OK.

## Gate set

| Gate | Threshold |
|---|---|
| **G1 Fresh-live days** | ≥ 14 closed days at the candidate configuration with NO config drift |
| **G2 Stability 30d** | rolling 30d hit rate stable; std/mean ≤ 0.20 |
| **G3 Robustness 60d** | rolling 60d hit rate ≥ rolling 30d hit rate − 5 pp |
| **G4 Lift vs OFFICIAL** | Wilson 95% CI lower bound > OFFICIAL Wilson 95% CI lower bound |
| **G5 Per-region no degrade** | no region drops below OFFICIAL by more than 3 pp |
| **G6 Profit/ROI** | rolling 30d profit > OFFICIAL rolling 30d profit |
| **G7 would_save ≥ would_break** | over the same 30d window |
| **G8 false_promotion** | < 10% on the same 30d window |
| **G9 Single-source resilience** | not dependent on a single volatile signal source (e.g. single cross-region pair) |
| **G10 Continuous measurement** | `CONTINUOUS_MEASUREMENT_DOCTRINE.md` compliance verified |
| **G11 Hash guard** | pre/post hash on 4 official tables UNCHANGED across the candidate evaluation window |
| **G12 Rollback plan** | documented in `OFFICIAL_PROMOTION_DOSSIER.md`; owner reviewed |
| **G13 Owner OK** | explicit entry in `DECISION_LOG.md` referencing the candidate dossier |

## Hard NEVERs

- NEVER promote based only on backfill (no fresh data).
- NEVER promote when any of G1–G12 fails.
- NEVER promote with PENDING > 5 in the candidate region.
- NEVER promote when duplicate_count > 0 in candidate config.
- NEVER promote without `OFFICIAL_PROMOTION_DOSSIER` complete.

## Promotion checklist (template)

```
[ ] G1 Fresh-live days ≥ 14 (date range: ____)
[ ] G2 Stability 30d (std/mean: ____)
[ ] G3 Robustness 60d (Δ60-30: ____)
[ ] G4 Lift vs OFFICIAL (CI lo: candidate=____, OFFICIAL=____)
[ ] G5 Per-region no degrade (MN: ___, MT: ___, MB: ___)
[ ] G6 Profit (candidate=____, OFFICIAL=____)
[ ] G7 would_save (___) ≥ would_break (___)
[ ] G8 false_promotion (___% < 10%)
[ ] G9 Single-source resilience (multi-source pp%: ____)
[ ] G10 Continuous measurement compliance: ___
[ ] G11 Hash guard: PASS
[ ] G12 Rollback plan documented in OFFICIAL_PROMOTION_DOSSIER.md
[ ] G13 Owner OK in DECISION_LOG.md (entry id: DEC-____)
```

STATUS: **ACTIVE — gate definition locked**.
