# V105.31 — CURRENT TRUTH CLEAN WRAPPER

Generated: 2026-05-12 11:22-11:35 VN  
Scope: public SSOT cleanup after V105.30c plus V105.30d/e runtime/UI findings.  
Hard lock: no official mutation, no provider/manual AI call, no fabricated numbers.

## 1. Executive Verdict

| Label | Verdict | Evidence |
|---|---|---|
| `V105_31_PUBLIC_SSOT_PASS` | PASS after this wrapper is raw-verified | This folder, `LATEST_REPORT.json`, `REPORT_INDEX.md`, `OPEN_ISSUES.md`, `NEXT_ACTION.md`, `CHANGELOG_PUBLIC.md` now point to V105.31 current truth. |
| `V105_30D_SHADOW_NO_MISSING_DEPLOYED` | PASS for MN 2026-05-12 | Live-synced DB `artifacts/live_sync/20260512_112202/manifest.json`: MN shadow `13/13`, `missing_shadow=[]`, diagnostic empty `glm-5.1`. |
| `PARTIAL_DIAGNOSTIC_EMPTY_OK` | PASS/PARTIAL | `glm-5.1` has no fabricated numbers; persisted as empty diagnostic row with `finish_reason=length`. |
| `NATURAL_VERIFY_PENDING` | PENDING | At 11:22 VN, MN completed; MT/MB full post-result cycles not yet complete. Do not call `NATURAL_VERIFY_PASS` yet. |
| `OFFICIAL_LOCK_PRESERVED` | PASS | Official final bundle present for MN with `model_count=15`; no code changed in official selector/scoring/bundle semantics. |
| `AI_PRIORITY_HOLD` | HOLD | Strongest-first remains proposal/shadow only. |
| `DO_NOT_PROMOTE` | ACTIVE | Lose-carryover, Top2/Bundler, MB_D_v2, V102 relaxed remain shadow/HOLD. |

## 2. READ Matrix

| Source | Read status | Current truth found | Conflict/stale wording? | Required action |
|---|---|---|---|---|
| Public `LATEST_REPORT.json` | READ | Latest was V105.30, refreshed 10:08. | Missing V105.30d/e no-missing + GLM diagnostic truth. | Update pointer to V105.31 wrapper. |
| Public `REPORT_INDEX.md` | READ | Latest said V105.30c. | Stale after V105.30d/e. | Make V105.31 wrapper latest. |
| Public `OPEN_ISSUES.md` | READ | No shadow no-missing/GLM policy item. | Incomplete current truth. | Add V105.30d/e and GLM compact profile issue. |
| Public `NEXT_ACTION.md` | READ | Natural verify + AI priority only. | Missing GLM compact profile and no-missing contract. | Update priority order. |
| Public V105.30 evidence | READ | Safe-stdio deployed; Rule105 V105.30b corrected. | `v10530_master_audit.json` still contains old quarantine language in audit body. | Wrapper overrides stale language. |
| Local governance | READ | `.Antigravityrules.md`, `.AGENT.md`, `.cursorrules` enforce live sync + governance update. | None for this task. | Followed. |
| Local live manifest | READ | `artifacts/live_sync/20260512_112202/manifest.json` synced DB + trace from VPS. | None. | Cite as live evidence. |
| Code paths | READ | `scheduler.py`, `database.py`, `gpt_analyzer.py`, `model_registry.py`, frontend `app.js`. | GLM uses full shadow context; UI label needed compact display. | Propose GLM compact profile; frontend display-only label compacted. |

## 3. PREFLIGHT Matrix

| Check | Expected | Actual | Status |
|---|---|---|---|
| VN timestamp | Recorded | 2026-05-12 11:20-11:35 VN | PASS |
| Main repo branch/commit | Recorded | `Lottery_AI_Test` branch `master`, commit `e626ba7`, dirty working tree present before this task | PASS_WITH_DIRTY_TREE |
| Public repo branch/commit | Recorded | `Lottery_AI_Notion_Reports` branch `main`, pre-update commit `b3ecaff` | PASS |
| Git remotes | SSH | Both repos use `git@github.com:irissnss/...` | PASS |
| GitHub SSH | Account auth OK | `Hi irissnss! You've successfully authenticated` | PASS |
| Provider/manual AI call | Must be 0 in this task | 0; only DB/log/code audit and UI/static public docs | PASS |
| Live forensic sync | Required before DB claims | `artifacts/live_sync/20260512_112202/manifest.json` | PASS |
| Official mutation | Forbidden | No selector/scoring/bundle/prompt official edits | PASS |

## 4. Current Truth Matrix

| Topic | Old/stale wording | Correct current truth | Evidence | Action |
|---|---|---|---|---|
| GitHub SSH | Deploy key pending / HTTPS risk. | Account-level SSH OK; public mirror pushes via SSH. | `ssh -T git@github.com` auth message. | Mark stale as superseded. |
| Rule105 | 30 prize-source violations / quarantine. | `source_region` lock; true violation count `0`; 30 are false positives. | `v10530_rule105_recheck.json`. | Use `prize_source_lock_by_source_region` wording. |
| `_safe_stdio_ctx` | Pending deploy. | Deployed live; V105.30d widened shadow/save handling; natural full-cycle verify still pending. | V105.30 report + scheduler/database deploy evidence. | Keep `DEPLOYED_PENDING_NATURAL_VERIFY`. |
| Shadow missing | MN shadow 6/13 or 12/13. | MN 2026-05-12 shadow persisted `13/13`, `missing_shadow=[]`; `glm-5.1` is diagnostic empty. | Live DB query after sync 11:22 VN. | Public SSOT updated. |
| Notion | V105.30 Notion page required. | Owner deferred Notion; GitHub raw is current public SSOT. | Owner lock + public raw status. | Not blocking. |
| Experiments | Candidate promotion possible. | Lose-carryover, Top2/Bundler, MB_D_v2, V102 relaxed stay HOLD/DO_NOT_PROMOTE. | `SIGNAL_LAYER_REGISTRY.md`, V105.30 report. | Keep gates. |
| Official | Could be backfilled from shadow. | Forbidden; official remains exact 15/15 gate. | Final bundle MN `model_count=15`. | Preserve hard-lock. |

## 5. Natural Verify Matrix

| Region | Stage | Official expected | Official actual | Shadow expected | Shadow persisted | Missing | Diagnostic empty | Timeout missing | System missing | Verdict |
|---|---|---:|---:|---:|---:|---|---|---|---|---|
| MN | Post MN cycle observed | 15 | 15 | 13 | 13 | `[]` | `["glm-5.1"]` | `[]` | `[]` | `PARTIAL_DIAGNOSTIC_EMPTY_OK` |
| MT | Pre full post-result cycle | 15 | 7 pre/post-current rows before closeout | 13 | 0 | Not evaluated yet | `[]` | Not evaluated yet | Not evaluated yet | `NATURAL_VERIFY_PENDING` |
| MB | Pre full post-result cycle | 15 | 7 pre/post-current rows before closeout | 13 | 0 | Not evaluated yet | `[]` | Not evaluated yet | Not evaluated yet | `NATURAL_VERIFY_PENDING` |

Do not call `NATURAL_VERIFY_PASS` until MT and MB complete naturally with `closed_file=0`, official `15/15`, and no `SYSTEM_MISSING`.

## 6. Shadow No-Missing Contract Proof

| Date | Region | Model | Expected class | Row exists | Numbers | Reliability | Error reason | Valid? |
|---|---|---|---|---|---|---|---|---|
| 2026-05-12 | MN | 12 shadow models excluding GLM | `PERSISTED_VALID_NUMBERS` | YES | Non-empty | `persisted_row=1` for successful rows | None | YES |
| 2026-05-12 | MN | `glm-5.1` | `PERSISTED_DIAGNOSTIC_EMPTY` | YES | `[]` | `persisted_row=1`, `finish_reason=length` diagnostic fill row | Provider/model returned empty content after length finish | YES |
| 2026-05-12 | MN | All expected shadow models | No true missing allowed except timeout | YES 13/13 | Mixed valid + diagnostic | Daily summary was corrected by contract fill | `missing_rows=[]`, `empty_rows=["glm-5.1"]` | YES |

Invalid classes not observed after V105.30d fill: `SYSTEM_MISSING`, `SAVE_PATH_FAILED_MISSING`, `CLOSED_STDIO_MISSING`, `PARSER_ERROR_MISSING_WITHOUT_DIAG_ROW`, `PROVIDER_EMPTY_MISSING_WITHOUT_DIAG_ROW`, `FABRICATED_NUMBERS`.

## 7. GLM-5.1 Evidence and Policy

| Model | Current issue | Evidence | Proposed profile | Promotion impact | Owner gate |
|---|---|---|---|---|---|
| `glm-5.1` | Current MN run returned empty content with `finish_reason=length`; row persisted as diagnostic empty. | Rerun log: `CONTEXT_PACK` injected `11358` chars + `REASONING_RULEBOOK`; OpenRouter actual model `z-ai/glm-5.1`; `max_tokens=24576`; response `0 chars`, `tokens=46881`, `finish=length`; DB diagnostic row created. | `glm-5.1_compact_json_profile`: tiny prompt, JSON-only, no explanation, no chain-of-thought, max 2 tails, strict schema `{"main_numbers":["NN","NN"],"confidence":0.xx,"reason_code":"short"}`; reduced context; keep 90s soft / 300s hard. | Never official; shadow only. One failure = diagnostic empty. Two consecutive length failures = `SHADOW_PROBATION`. Three consecutive failures = disable from full shadow auto or compact-profile-only. | Owner approval required before changing runtime profile or making a new provider call. |

Interpretation: `glm-5.1` is not globally broken. It produced valid numbers on prior days, including 2026-05-11 for MN/MT/MB. The failure is a profile/context compatibility failure under the current heavy shadow profile, not a hidden UI number and not a reason to fabricate numbers.

## 8. Rule105 Source-Region Doctrine

Required terminology:

- `prize_source_lock_by_source_region`
- `source_region_prize_keys`
- `target_region_formula`
- `prior_flagged_rows_false_positive`
- `true_violation_count=0`
- `production_mined_rules_untouched`
- `quarantine_withdrawn`

Allowed source prizes:

- MN/MT source: ĐB, G1, G2, G5, G7, G8.
- MB source: ĐB, G1, G2, G6, G7.

Doctrine:

- `target_region` = region being predicted.
- `source_region` = region/station source used for mining.
- `prize_keys` belongs to `source_region`.
- MN_D = (MN+MT+MB) D-1 + (MN+MT+MB) D-2.
- MT_D = (MN+MT+MB) D-1 + MN D.
- MB_D = (MN+MT+MB) D-1 + MN D + MT D.

## 9. Experiments HOLD Matrix

| Experiment | Status | Current rule |
|---|---|---|
| Lose-carryover | `DO_NOT_PROMOTE` | Prompt-support only, requires LOSE + actual-known + Rule105/source-pool/model-strength confirmation. |
| Top2/Bundler | `SHADOW_ONLY` | Needs 14d+, `net_save>0`, low break ratio; no official. |
| MB_D_v2 | `DO_NOT_PROMOTE` | Option A rejected; no MB D-2 primary; only owner-gated C+D shadow if any. |
| V102 relaxed | `HOLD` | Needs >=14d, `net_save>0`, break-ratio threshold, owner OK. |
| AI strongest-first | `AI_PRIORITY_HOLD` | Shadow 7d and tensor refresh proposal only; no live reorder. |

## 10. Open Issues

| Severity | Issue | Status | Next action |
|---|---|---|---|
| P0 | Closed stdout/system missing recurrence | No recurrence observed in current post-deploy journal check; keep natural verify pending | Verify after MT/MB natural cycles. |
| P1 | GLM full-context `finish_reason=length` | Diagnostic empty persisted; compact profile proposal only | Owner approve compact profile before runtime change/call. |
| P1 | AI strongest-first | HOLD | Owner-gated shadow 7d/tensor refresh. |
| P1 | Tensor refresh cron | OPEN | Owner-gated cron proposal, not live. |
| P2 | Notion V105.30 | DEFERRED | Optional short pointer page later. |

## 11. Final Verdict

Current status: `V105_31_PUBLIC_SSOT_PASS` once raw links verify, `V105_30D_SHADOW_NO_MISSING_DEPLOYED`, `PARTIAL_DIAGNOSTIC_EMPTY_OK`, `NATURAL_VERIFY_PENDING`, `OFFICIAL_LOCK_PRESERVED`, `AI_PRIORITY_HOLD`, experiments `DO_NOT_PROMOTE`.

Not a full runtime PASS yet because MT/MB natural cycles are not complete.
