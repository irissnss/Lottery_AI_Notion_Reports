# MT PROTECT REGRESSION AUDIT — V105.27

> For every change V105.22 → V105.26 (+ V105.25b stdio harden + V105.27 audit), evaluate MT impact.

| Change | Touches MT? | MT formula changed? | D-2 leak? | Selector/prompt changed? | would_break risk | Verdict |
|---|---|---|---|---|---|---|
| V105.22 region-independent lane test profiles (`lane_test_region_profiles=3`) | Yes — separates MT profile | No | No (MT spec: MN_D1, MT_D1, MB_D1, MN(D)) | No official selector change; MT profile = PROTECT | None | `MT_PROTECT_PRESERVED` |
| V105.22 source-pool / strong coverage / rule injection (3076 rows each) | Diagnostic on MT included | No | No | No | None | `MT_PROTECT_PRESERVED` |
| V105.22 MT preview below budget | Honest reporting only | No | No | No (gate, not selector) | None | `MT_PROTECT_PRESERVED` |
| V105.22a MN shadow recovery | MN-only | No | No | No | None | `MT_PROTECT_PRESERVED` |
| V105.22b token-cost guard | All regions | No | No | No (database-level once-daily lock) | None | `MT_PROTECT_PRESERVED` |
| V105.23 station identity lock | All regions | No | No | No (label canonicalization) | None | `MT_PROTECT_PRESERVED` |
| V105.24 source-pool gap drilldown (code present, table not materialized locally) | Diagnostic only on all regions | No | No | No | None | `MT_PROTECT_PRESERVED` |
| V105.25 candidate flow funnel / V103 supply backfill (code present) | Diagnostic only | No | No | No | None | `MT_PROTECT_PRESERVED` |
| V105.25b cascade contract verify | All regions | No | No | No (stdio harden + UI mapping only) | None | `MT_PROTECT_PRESERVED` |
| V105.25b `_safe_stdio_ctx` scheduler patch | All regions equally | No | No | No | None — stdio safety only | `MT_PROTECT_PRESERVED` |
| V105.25b admin `/api/admin/cascade-contract-audit` | Read-only diagnostic | No | No | No | None | `MT_PROTECT_PRESERVED` |
| V105.27 evidence harvesters / audit artifacts | Read-only | No | No | No | None | `MT_PROTECT_PRESERVED` |

## Hard rule reaffirmed

If a method improves MN and/or MB but degrades MT, do NOT apply to MT. Any MT change requires:

1. MT-specific positive evidence (`region=MT + weekday + station_set` clean).
2. 14d clean break_ratio.
3. Owner explicit OK.

## Verdict

`MT_PROTECT_PRESERVED` across the V105.22 → V105.27 window. No selector, scoring, source-pool formula, prompt, or roster mutation touched MT.
