# V101 SHADOW RULE + REGION PROMPT CONTEXT REPORT

**Date:** 2026-05-09 16:05 VN  
**Scope:** shadow-only/admin-only accuracy pilot after V100 gan foundation.  
**Hard lock:** no production scoring, prompt, selector, model roster, `/du-doan`, or official table mutation.

---

## 1. What Was Built

| Component | File / table | Purpose | Status |
|---|---|---|---|
| MN cross-region D-1/D-2 rule | `web/backend/_v101_shadow_pilot.py` | Build MN-only candidate pool from `(MN+MT+MB) D-1 + (MN+MT+MB) D-2`, plus gan and V67/V70/V73 bonuses | DEPLOYED |
| Prompt context table | `v101_region_prompt_context_shadow` | Stores per-region shadow prompt addendum/context JSON | DEPLOYED |
| MN candidate table | `v101_mn_cross_region_rule_shadow` | Stores ranked MN candidates, top 30 per day | DEPLOYED |
| Admin readout API | `/api/admin/v101-shadow-pilot` | Read-only top MN candidates + prompt context | DEPLOYED, 401 unauth |
| MN prompt V2 | `MN_AI_REGION_SPECIALIST_PROMPT_SHADOW_V2.md` | Adds MN D-1/D-2 rule + gan + V99 semantic guard | DEPLOYED |
| MT prompt V2 | `MT_AI_REGION_SPECIALIST_PROMPT_SHADOW_V2.md` | Keeps MT consensus-first/no-break; gan diagnostic only | DEPLOYED |
| MB prompt V2 | `MB_AI_REGION_SPECIALIST_PROMPT_SHADOW_V2.md` | Adds MB gan normal/special, cold flag doctrine, semantic guard | DEPLOYED |

---

## 2. Safety Contract

- `shadow_only=1`
- `output_eligible=0`
- `diagnostic_only=1`
- `owner_approved=0`
- No provider calls were made.
- No production prompt was changed.
- No production selector/scoring/model roster was changed.
- No official table was mutated.

Post-deploy hash/count:

| Table | Count |
|---|---:|
| `predictions` | 4584 |
| `final_bundles` | 211 |
| `lottery_results` | 14634 |
| `model_daily_eval` | 4493 |

---

## 3. Backfill Result

VPS command:

```bash
python web/backend/_v101_shadow_pilot.py --backfill-days 14 --json
```

Result:

| Surface | Rows |
|---|---:|
| `v101_mn_cross_region_rule_shadow` | 420 |
| `v101_region_prompt_context_shadow` | 42 |

Daily pattern:

| Date | MN candidates | Prompt contexts |
|---|---:|---:|
| 2026-05-09 | 30 | 3 |
| 2026-05-08 | 30 | 3 |
| 2026-05-07 | 30 | 3 |
| 2026-05-06 | 30 | 3 |
| 2026-05-05 | 30 | 3 |

---

## 4. 2026-05-09 MN Candidate Readout

Top signal for 2026-05-09:

| Rank | Tail | Score | D-1 | D-2 | Source regions | Gan | V67 | V70 | V73 |
|---:|---|---:|---:|---:|---|---|---:|---:|---:|
| 1 | 13 | 8.74 | 1 | 3 | MB/MN/MT | normal + special | 1 | 1 | 1 |
| 2 | 79 | 7.76 | 1 | 5 | MB/MN/MT | special | 1 | 0 | 0 |
| 3 | 83 | 6.85 | 3 | 2 | MB/MN/MT | special | 0 | 0 | 0 |
| 4 | 61 | 6.85 | 3 | 2 | MB/MN/MT | special | 0 | 0 | 0 |
| 5 | 93 | 6.79 | 1 | 3 | MB/MN | normal + special | 1 | 0 | 0 |

Interpretation:
- `13` is the strongest V101 MN challenger because it combines D-1/D-2 cross-region support, gan normal/special support, and V67/V70/V73 agreement.
- This does **not** mean production should pick 13. It is a shadow candidate to evaluate after result-known closeout.

---

## 5. Region Prompt V2 Policy

| Region | V101 policy | What remains locked |
|---|---|---|
| MN | Use MN-only cross-region D-1/D-2 pool, gan normal >=15d, gan special G8/DB >=7d, V67/V70/V73 agreement | No production prompt injection |
| MT | Consensus-first/no-break guard, gan diagnostic only, no cross-region expansion | No noisy expansion |
| MB | Cold flag + gan normal >=30d + gan DB >=15d + AI/no-token conflict + semantic warning | No strict scoring shift |

---

## 6. Deployment Proof

Smoke:

| Endpoint / check | Result |
|---|---|
| `/api/health` | 200 |
| `/api/admin/v101-shadow-pilot` | 401 unauth (admin-locked) |
| `v101_mn_cross_region_rule_shadow` | 420 rows |
| `v101_region_prompt_context_shadow` | 42 rows |
| Official hash/count | unchanged |

---

## 7. Next Required Step

After 2026-05-09 closeout:

1. Rerun V99 evaluator:
   `python web/backend/_v99_exact_evaluator.py --target 2026-05-09`
2. Rerun V101:
   `python web/backend/_v101_shadow_pilot.py --date 2026-05-09 --json`
3. Compare MN clusters:
   - Official: `05`
   - V100 test lane clusters: `82`, `05`, `13`
   - V101 cross-region shadow: top `13`
4. Record strict vs diagnostic result.

**Status:** V101 delivered as shadow pilot. Await result-known evaluation.
