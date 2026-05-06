# Master Logical Synthesis — V52 to V61

**Purpose:** one coherent, chronological synthesis for Notion AI and owner review.  
**Scope:** V52 family → V61 current.  
**Raw evidence:** [raw export direct links](../V52_TO_CURRENT_FULL_CHAIN_20260506/11_DIRECT_LINKS/READ_THIS_FIRST_LINKS.md).  
**Important:** This file is a logical synthesis. When exact source wording matters, read the linked raw reports.

---

## 1. Core thesis across the chain

The project evolved from “measure-only diagnostics” into a guarded experimental lane that can display a daily test output while keeping official `/du-doan` locked. The chain has two distinct tracks:

1. **Official track**: `/du-doan`, `final_bundles`, production `predictions`, scoring, voting, model roster, prompt, and official scheduler. This remains locked until rolling proof and owner approval exist.
2. **Experimental track**: `/du-doan-test`, `experimental_preview_shadow`, `du_doan_test_*`, C-16 model budget, experience UI, and measurement surfaces. This is allowed to move faster as long as it is admin-only, test-only, output_eligible=0, and never writes official output.

The owner’s recurring correction is also now canonical: testing must be useful and visible before official proof is mature. Strict gates apply to **official promotion**, not to **experience/test visibility**.

---

## 2. Chronological logic

### V52 — Measurement and reality check foundation

V52 established that official quality must not be improved by guesswork. It implemented measurement-only surfaces and forced report-chain honesty:

- MT correct-but-dropped / model-hit-output-drop diagnosis.
- Loz selector measurement.
- Latency/cost audit table, which revealed no true per-model timing.
- `/du-doan-test` reality checks to ensure test lane is not confused with official.
- Explicit source-hash guarding.

Key result: official output was not mutated, but the system gained enough diagnostics to identify where official lost correct model signals.

Raw links:

- [V52 links](../V52_TO_CURRENT_FULL_CHAIN_20260506/11_DIRECT_LINKS/BY_VERSION/V52.md)
- [DB table counts](../V52_TO_CURRENT_FULL_CHAIN_20260506/04_DB_PROOF/table_counts_by_version.md)

### V52.5 — Multi-region parallel test lane

V52.5 generalized the test lane to MN/MT/MB:

- `model_strength_by_region_weekday_station_daily` tensor.
- `experimental_preview_shadow`.
- `_du_doan_test_engine.py`.
- `_du_doan_test_daily_runner.py`.
- multi-region API/UI.

Key truth: `/du-doan-test` became real enough to compare methods across regions, but it was still manual and not full live-auto.

### V53 / V53.1 — UI clarity and roadmap

V53 reconciled the owner’s concern that test numbers looked like official numbers. V52.6 added UI source-badge and labels:

- official baseline is read-only from `final_bundles`;
- test picks come from test tables;
- same number means independent agreement unless it is the baseline control.

V53.1 converted the test-lane and official-improvement strategy into roadmap/timeline docs. Official improvement was explicitly gated by future evidence.

Raw links:

- [V53 links](../V52_TO_CURRENT_FULL_CHAIN_20260506/11_DIRECT_LINKS/BY_VERSION/V53.md)

### V54 — Natural live watch and safe measurement add-ons

V54 ran during the 2026-05-04 live day and added safe surfaces:

- C-02 API source labels.
- C-06 `loz_stage_trace_shadow`.
- C-15 `weekday_blackspot_shadow`.

C-05 latency instrumentation was deferred because it touches the live model-call path.

Key truth: loz and weekday blackspots became measurable, but official remained not proven.

### V55 — 04/05 + 05/05 closeout forensic and new Google shadow cohort

V55 had two important parts:

1. **New Google direct shadow cohort**:
   - `gemini-3.1-pro`
   - `gemini-3-flash`
   - `gemma-4-31b`

2. **Full 04/05 + 05/05 forensic**:
   - 04/05: MN lose/partial, MT win, MB lose.
   - 05/05: MN lose, MT win/partial, MB lose.
   - MN test methods rescued two misses.
   - MT test methods could break official wins.
   - MB stayed structurally weak.

V55 also found a scheduler bug: `gemma-*` was routed as OpenRouter and skipped. This was fixed.

Raw links:

- [V55 links](../V52_TO_CURRENT_FULL_CHAIN_20260506/11_DIRECT_LINKS/BY_VERSION/V55.md)
- [test rows DB proof](../V52_TO_CURRENT_FULL_CHAIN_20260506/04_DB_PROOF/pre_result_lock_rows.md)

### V56 — Experience lane

V56 answered the owner’s concern that waiting 14/30/60 days made the experiment lane feel dead. It added an `EXPERIENCE_MODE` panel that surfaces:

- method rescues;
- harmful/false-promotion cases;
- V55 Google shadow picks;
- explicit “not official” labels.

Key truth: experience is allowed before official promotion.

### V57 — C-16 adaptive model budget selector

V57 implemented C-16:

- full pool: 29 measured components;
- selected voters per bucket;
- watch-only;
- skip-today;
- C-16 output method: `{REGION}_ADAPTIVE_BUDGET_SELECTOR_V1`.

Key truth: `/du-doan-test` now has a model-budget layer, but C-05 latency is still missing so it is not yet a true cost optimizer.

Raw links:

- [V57/C-16 links](../V52_TO_CURRENT_FULL_CHAIN_20260506/11_DIRECT_LINKS/BY_VERSION/V57_C16.md)

### V58 — Visual parallel output

V58 added the visible test-output card:

- BT
- 3-càng
- xiên 2
- xiên 3

It also introduced visible lock labels:

- `PRE_RESULT_LOCKED`
- `POST_CLOSEOUT_DIAGNOSTIC`

Key truth: 05/05 rows were post-closeout diagnostic, not natural realtime proof.

### V59 — Strict 3-càng / xiên verification

The owner caught a critical error: test LO3 could be labeled WIN by 2-digit tail match. V59 fixed:

- LO3 must match full 3-digit suffix.
- Xiên 2/3 must hit same station when station rows exist.

Key truth: earlier LO3 wins based only on 2D tail are invalid and must be treated as UI/API verification bugs.

### V60 — Mobile UI and model execution priority

V60 fixed mobile two-column viewing and changed shadow evaluation order:

- no-token already runs first;
- shadow token models are ordered by C-16 when available;
- otherwise fallback to tensor strength;
- otherwise registry order.

Key truth: execution order became bucket-aware but still lacks hard deadline/cutoff.

### V61 — Dynamic pre-result trigger

V61 found that 06/05 MN was ready but test lane had not run. It added a readiness-gated 5-minute trigger:

Run test lane only if:

- final bundle exists;
- predictions exist;
- actual result does not exist yet;
- no test bundle exists yet.

MN 06/05 was then run pre-result in `REALTIME_AVAILABLE_ONLY` mode.

Key truth: this is the first step toward natural parallel test operation.

---

## 3. Current status as of V61

Official output:

- Still locked.
- Official quality is mixed and region-conditional.
- No official promotion/change is justified yet.

Test lane:

- Admin-only.
- Now has visual output, experience mode, C-16 model budget, strict LO3/Xien verification, mobile two-column UI, and dynamic pre-result trigger.
- Still not fully mature because C-03 evaluator and C-04 auto-wire governance gates remain.

Measurement:

- Much broader, but latency/cost remains the biggest unresolved blocker.
- C-05 is mandatory before pruning or cost optimization.

---

## 4. Main unresolved issues

1. C-05 per-model latency instrumentation is still missing.
2. C-03 multi-region closeout evaluator is not complete.
3. C-04 scheduler auto-wire for test lane needs 3-5 clean closeouts.
4. C-16 uses neutral latency until C-05 exists.
5. V55 Google shadow cohort needs 14+ valid days.
6. MB remains structurally weak.
7. MT AI-chain methods are harmful in current evidence and must not be promoted.
8. Loz policy remains diagnostic-only.
9. No official output change is allowed yet.

---

## 5. Official promotion rule

A test method may be discussed for official only after:

- clean rolling evidence;
- false-promotion risk bounded;
- no leakage;
- owner review;
- explicit owner approval.

Until then: test visibility is allowed; official mutation is not.

---

## 6. Read raw evidence next

Start with:

- [Direct link index](../V52_TO_CURRENT_FULL_CHAIN_20260506/11_DIRECT_LINKS/READ_THIS_FIRST_LINKS.md)
- [Full chain manifest](../V52_TO_CURRENT_FULL_CHAIN_20260506/00_MANIFEST/FULL_CHAIN_MANIFEST.md)
- [DB proof overview](../V52_TO_CURRENT_FULL_CHAIN_20260506/04_DB_PROOF/table_counts_by_version.md)
- [Function change index](../V52_TO_CURRENT_FULL_CHAIN_20260506/03_CODE_DIFFS/function_change_index.md)
