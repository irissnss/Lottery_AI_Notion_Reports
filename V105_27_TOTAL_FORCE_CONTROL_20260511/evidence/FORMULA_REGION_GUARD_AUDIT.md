# FORMULA / REGION PROFILE / D-2 GUARD AUDIT — V105.27

## 1. Canonical formulas under audit

```
MN_D = (MN + MT + MB) D-1 + (MN + MT + MB) D-2
MT_D = (MN + MT + MB) D-1 + MN D
MB_D = (MN + MT + MB) D-1 + MN D + MT D
```

## 2. Code source (priority meta attached to AI prompt context)

`web/backend/scheduler.py:_attach_owner_priority_meta` (lines 2406-2441):

```
MN spec: MN_D1, MT_D1, MB_D1
MT spec: MN_D1, MT_D1, MB_D1, MN(D)
MB spec: MN_D1, MT_D1, MB_D1, MN(D), MT(D)
```

| Formula | Docs source | Code source (priority meta) | Runtime evidence | Status |
|---|---|---|---|---|
| `MN_D = (MN+MT+MB) D-1 + (MN+MT+MB) D-2` | V105.5/V105.22/V105.25b doctrine rows | `MN` spec lists only `*_D1`; D-2 still consumed at statistical level (`statistical_depth=30`) via `meta_predict.run_full_analysis` | `predictions.source_regions` for MN today contains `MN_D1,MT_D1,MB_D1,MN` (no D-2 token) | `FORMULA_LOCK_CONFIRMED` for D-1; **MN D-2 PROMPT NOT INJECTED** (`PROMPT_INJECTION_GAP` per V105.26) |
| `MT_D = (MN+MT+MB) D-1 + MN D` | V105.5 | MT spec exactly matches | `predictions.source_regions` for MT after MN verify contains `MT_D1,MB_D1,MN_D1,MN` | `FORMULA_LOCK_CONFIRMED`; `D2_LEAK_BLOCKED` |
| `MB_D = (MN+MT+MB) D-1 + MN D + MT D` | V105.5 | MB spec exactly matches | `predictions.source_regions` for MB after MT verify contains `MT_D1,MB_D1,MN_D1,MN,MT` | `FORMULA_LOCK_CONFIRMED`; `D2_LEAK_BLOCKED` |

## 3. D-2 leak runtime probe (last 7 days)

Query:

```sql
SELECT target_region, source_regions, COUNT(*) cnt
FROM predictions
WHERE date >= '2026-05-05' AND target_region IN ('MT','MB')
  AND (source_regions LIKE '%D2%' OR source_regions LIKE '%D-2%'
       OR source_regions LIKE '%MN_D2%' OR source_regions LIKE '%MT_D2%' OR source_regions LIKE '%MB_D2%')
GROUP BY target_region, source_regions;
```

Result: **0 rows.**

Verdict: `D2_LEAK_BLOCKED` confirmed for MT and MB at the prediction `source_regions` layer.

## 4. Region mode evidence

- `MN_PRIORITY=true` — V105.22 row in SSOT, lane-test materializer prioritizes MN; same-day lose gate (V105.10/V105.11) is MN-first.
- `MT_PROTECT_MODE=true` — V105.22 row in SSOT; lane-test region profiles (`lane_test_region_profiles=3`) confirm 3 separate region profiles, no global override.
- `MB_FORENSIC_MODE=true` — V105.22 row in SSOT; MB AI chain preservation table `mb_ai_chain_preservation_v1=30`.

## 5. Outstanding gaps

| Item | Status | Severity | Notes |
|---|---|---|---|
| MN D-2 prompt injection wired | NOT WIRED | P1 (prediction-quality only, not stability) | V105.26 mention `mn_d2_rows`, `REAL_PROMPT_NOT_INJECTED` — needs natural-run tracking 7/14d, shadow-only, no provider call. |
| MT D-2 leak | 0 occurrences | None | Preserved. |
| MB D-2 leak | 0 occurrences | None | Preserved. |
| MT protect | active | None | No selector/scoring change in V105.22+ that touches MT formula. |
| MB forensic | active | None | No MB_D_v2 active path; owner-gate required. |

## 6. Hard locks for V105.27

- Do NOT change `_attach_owner_priority_meta` formulas.
- Do NOT add D-2 keys for MT or MB.
- Any MN D-2 prompt injection must go through a shadow profile keyed on `region=MN + weekday + station_set`, with no impact on MT/MB.
