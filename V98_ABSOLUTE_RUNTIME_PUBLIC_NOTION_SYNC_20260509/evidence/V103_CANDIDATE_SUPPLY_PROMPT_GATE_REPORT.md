# V103 Candidate Supply + Prompt Gate Report

**Date:** 2026-05-09 22:00 VN  
**Scope:** shadow-only candidate supply and prompt compatibility gate.  
**Owner concern:** AI cannot output a number if the candidate is never supplied to the model/prompt.

---

## 1. What V103 Solves

V102 proved recurrence edges exist over 60 days. V103 answers the next root question:

> For each tail, did it enter the candidate supply before output?

V103 records each candidate tail per day/region and marks where it appears:

- AI model predictions
- no-token/local model predictions
- official BT/LO2
- `/du-doan-test` BT/LO2
- V67/V70/V73 traces
- V101 MN D-1/D-2 candidates
- V102 recurrence context
- V100 gan normal/special
- rule/soi-cầu source via `rule_phase_evidence_shadow`

---

## 2. New Shadow Tables

| Table | Purpose | Rows after 30d VPS backfill |
|---|---|---:|
| `v103_candidate_supply_shadow` | Candidate supply by tail × region × date | 8,743 |
| `v103_prompt_candidate_gate_shadow` | Prompt gate: REQUIRED / REVIEW / BLOCKED | 8,743 |

All rows are:

- `shadow_only=1`
- `output_eligible=0`
- `diagnostic_only=1`
- `owner_approved=0`

---

## 3. Prompt Gate Logic

### REQUIRED

Candidate becomes `REQUIRED` only if:

1. Recurrence is `STRONG` or `MEDIUM`, **and**
2. There is at least one non-gan core layer:
   - AI model
   - no-token model
   - official
   - test-lane
   - V67/V70/V73
   - V101
   - rule/soi-cầu support
3. At least 2 source layers support the candidate.

### REVIEW

Candidate becomes `REVIEW` if:

- recurrence + gan exists but no non-gan core layer yet; or
- recurrence is positive but evidence is incomplete; or
- multiple non-gan layers exist but recurrence gate is weak.

### BLOCKED

Candidate becomes `BLOCKED` when:

- only gan/noise exists; or
- recurrence is not eligible; or
- insufficient source support.

Important V103 fix:

> Gan alone can no longer make a candidate REQUIRED. It is only support/tie-breaker.

---

## 4. 2026-05-10 Current Gate Snapshot

Before 2026-05-10 predictions exist, V103 has:

| Gate | Count |
|---|---:|
| REQUIRED | 0 |
| REVIEW | 49 |
| BLOCKED | 251 |

This is correct because tomorrow’s AI/test predictions have not run yet. When AI/test/V67/V70/V73/rule sources appear, rerunning V103 can promote compatible candidates from REVIEW to REQUIRED.

Examples of current REVIEW candidates:

| Region | Tail | Reason |
|---|---|---|
| MN | 82 | strong recurrence + gan, AI missing supply |
| MN | 05 | strong recurrence + gan, AI missing supply |
| MN | 61 | strong recurrence + gan, AI missing supply |
| MN | 52 | strong recurrence + gan, AI missing supply |
| MT | 82 | strong recurrence + gan, AI missing supply |
| MB | 82 | strong recurrence + gan, AI missing supply |
| MB | 05 | strong recurrence + gan, AI missing supply |

---

## 5. Deployment Proof

VPS backfill:

```text
v103_supply=8743
v103_gate=8743
predictions=4625
final_bundles=213
lottery_results=14642
model_daily_eval=4493
```

The official table counts reflect natural live cycle after 19:00, not V103 writes. V103 writes only its two shadow tables.

Endpoint smoke after V102/V103:

```text
health=200
du-doan=200
monitoring=401
```

---

## 6. How V103 Feeds AI Prompt

Shadow AI prompt should receive only candidates with:

- `prompt_gate=REQUIRED`, or
- `prompt_gate=REVIEW` and region-specific prompt asks for diagnostic context.

Prompt phrasing:

```text
CANDIDATE_REVIEW_REQUIRED:
- tail
- why supplied
- recurrence lift
- model/source support
- rule/gan support
- strict vs diagnostic warning
```

This addresses the root issue:

> If AI did not call a tail but recurrence/rule/gan/V101 says it must be reviewed, V103 explicitly forces it into the shadow prompt review set.

---

## 7. Next Step

V104 should integrate V103 gate rows into the actual region-specialist shadow provider prompt call, still without production prompt change.

Recommended V104 flow:

1. Before AI shadow provider call, query V103 REQUIRED/REVIEW candidates.
2. Build a compact candidate review block per region.
3. Ask model to output max 2 numbers and explicitly accept/reject each supplied candidate.
4. Store `accepted/rejected` reasoning in a new shadow table.
5. Compare against V99 exact evaluator after closeout.

**Status:** V103 delivered. Await V104 shadow prompt injection.
