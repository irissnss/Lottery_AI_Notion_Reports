# MB FORENSIC / MB_D_v2 OWNER-GATE — V105.27

## 1. Current formula (locked)

```
MB_D = (MN + MT + MB) D-1 + MN D + MT D
```

Evidence:
- Owner mission V105.27 explicit doctrine.
- `_attach_owner_priority_meta` MB spec: `MN_D1, MT_D1, MB_D1, MN, MT`.
- `predictions.source_regions` 2026-05-09/10 MB rows contain exactly these keys.

## 2. MB_D_v2 option matrix (NOT ACTIVE — owner gate required)

| Option | Scope | Risk | Expected benefit | Required evidence | Recommendation |
|---|---|---|---|---|---|
| A. Add `MB D-2 / MN D-2 / MT D-2` to MB priority | Wide D-2 for MB | HIGH — would leak D-2 to a non-MN region, violating current doctrine | unclear; MB lo2 may rise but anti-herding risk | 14d shadow, per-weekday separated, no MT contamination | **HOLD — do not pursue unless owner explicitly requests** |
| B. Relax TOP30 cap (e.g. 50 or remove) | Source-pool cap relax for MB | MEDIUM — more noise, slower prompt | Catch missing tails outside top30 | source-pool gap drilldown table populated → run 14d shadow | Shadow-only after source-pool gap materialized |
| C. Add `source_prize_strong_coverage`-derived strong class | Promote `source_prize_effectiveness_daily` rows into MB candidate class | LOW (already diagnostic) | Strong-tier candidates lifted to V103 supply | 7d shadow + per-weekday break_ratio check | Shadow-only candidate; owner OK after 14d |
| D. Same-day MN/MT stronger weighting | Boost weight of same-day MN+MT verdicts in MB priority | LOW–MEDIUM | Lift MB BT hit-rate on lag1 carry days | per-weekday measurement, MT_PROTECT_PRESERVED check | Shadow-only |

## 3. Source-pool gap first

Before any MB_D_v2 shadow:

1. Materialize `_v10524_source_pool_gap_drilldown.py` or equivalent on VPS so per-region miss reasons are quantified.
2. Confirm MB miss reasons split between `FORMULA_EXCLUSION`, `TOP30_CAP`, `PROMPT_NOT_INJECTED`, `SELECTOR_RANK_DROP`, `BUNDLE_DROP`.
3. Pick the MB_D_v2 option(s) targeting the largest miss bucket, not a generic relax.

## 4. Default recommendation

`MB_D_v2 shadow only 14 days after owner defines scope.` No primary/lane-primary/official change. MB_FORENSIC_MODE remains active.

## 5. Verdicts

- `MB_FORENSIC_ONLY` for current path.
- `MB_D_V2_OWNER_GATE` — register owner decision before any work.
- `DO_NOT_PROMOTE` MB_D_v2 to official under any circumstance until 14d shadow + per-weekday clean evidence.
