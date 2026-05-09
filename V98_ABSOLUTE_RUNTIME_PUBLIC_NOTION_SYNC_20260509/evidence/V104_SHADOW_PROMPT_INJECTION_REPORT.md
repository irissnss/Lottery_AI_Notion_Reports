# V104 Shadow Prompt Injection — Phase A Report (2026-05-09 23:50 VN)

> **Status:** SHADOW ONLY. Phase A delivered. Phase B (provider pilot) gated by owner OK.
> **Hard contract:** `shadow_only=1`, `diagnostic_only=1`, `output_eligible=0`, `owner_approved=0`. NO `/du-doan` / `final_bundles` / production selector / SP-4.1 mutation. NO provider call this phase.
> **§52 + §52F compliance:** measurement table + admin API + `/monitoring` UI panel + 3 region prompts + Notion MCP auto-sync + dual GitHub push + pre/post hash 4 official tables IDENTICAL.

## 1. Executive summary

V104 closes the gap between V103 (which only flagged candidates as REQUIRED/REVIEW/BLOCKED) and the AI shadow chain (which previously did not see those flags). For every owner-flagged candidate today, V104 builds a region-specific prompt addendum + accept/reject schema that the AI shadow chain reads, **shadow only, no production weight**. All measurement is surfaced at `https://xs.io.vn/monitoring` panel `sectionV104ShadowPromptInjection` and `/api/admin/v104-shadow-prompt-injection`.

## 2. Tables created

| Table | Rows (today / total) | Purpose |
|---|---:|---|
| `v104_shadow_prompt_candidate_injection` | 81 (2026-05-09) / **1823** (30d backfill) | Per-(date, region, tail) injection class + prompt text |
| `v104_shadow_prompt_model_decision` | 0 (Phase A) | Phase B placeholder for ACCEPT / REJECT / HOLD per model |

Both tables have: `output_eligible=0`, `diagnostic_only=1`, `shadow_only=1`, `owner_approved=0`.

## 3. Today's distribution (2026-05-09)

| Region | REQUIRED_IN_PROMPT | OPTIONAL_REVIEW | BLOCKED | Total |
|--------|-------------------:|----------------:|--------:|------:|
| MN | 0 | 39 | 0 | 39 |
| MT | 0 | 24 | 0 | 24 |
| MB | 0 | 18 | 0 | 18 |
| **Total** | **0** | **81** | **0** | **81** |

**Why 0 REQUIRED today?** V103 gate has 0 REQUIRED for 2026-05-09 (tightened logic: requires recurrence STRONG + non-gan core + 2+ layers). V102 candidate context only identified 61 STRONG/MEDIUM tails today, but none satisfied V103's full chain after gate. V104 correctly does NOT inflate by promoting REVIEW → REQUIRED unless the upgrade rule (recurrence STRONG/MEDIUM + lift_pp ≥ 5 + non-gan core + ≥2 layers) is met. Honest result.

## 4. 13 / 61 / 64 / 89 case audit (today)

| Region | Tail | V103 gate | V104 injection | Reason summary |
|---|---|---|---|---|
| MN | 13 | REVIEW | OPTIONAL_REVIEW | non_gan_core=True (test_bt, test_lo2, V67/V70/V73, V101) total=7 layers, but recurrence_class=None & lift_pp=0 → upgrade rule not met |
| MT | 61 | REVIEW | OPTIONAL_REVIEW | non_gan_core=True (ai_model, V67), recurrence_class=None & lift_pp=0 |
| MB | 64 | REVIEW | OPTIONAL_REVIEW | non_gan_core=True (ai_model, V67), recurrence_class=None & lift_pp=0 |
| MN | 89 | REVIEW | OPTIONAL_REVIEW | non_gan_core=True (V101), recurrence_class=None & lift_pp=0 |

**All 4 candidates surface to AI shadow chain** as OPTIONAL_REVIEW with full source-layer breakdown + V101/V102/gan context. AI must respond ACCEPT / REJECT / HOLD with reason. The fact that V102 doesn't classify them STRONG/MEDIUM for 2026-05-09 is itself useful diagnostic — owner can compare AI decision vs V102 silence after closeout.

## 5. Endpoints (admin-only)

| Endpoint | VPS status | Local payload OK |
|---|---|---|
| `/api/admin/v104-shadow-prompt-injection` | 401 (unauth — admin-locked correct) | YES |
| `/api/admin/v103-cross-region-tracker` | 401 | (unchanged) |
| `/api/health` | 200 | (unchanged) |
| `/du-doan` | 200 (production unchanged) | (unchanged) |

## 6. UI panel `sectionV104ShadowPromptInjection`

- Registered in `loadAllSections()` AND `setInterval(60s)`.
- 4 sub-panels rendered:
  1. Owner intent banner.
  2. Per-region summary cards (REQUIRED / OPTIONAL / BLOCKED counts).
  3. STRICT vs DIAGNOSTIC warning banner (yellow alert).
  4. Per-region collapsible candidate table (Tail × V103 gate × Injection class × Source layers × Recurrence × Gan × Reasons).
- Phase B notice at bottom: provider pilot not activated, owner gate.
- Admin-only. NO promote / rollback / trigger button. Read-only.

## 7. Region prompts (independent)

| File | Path |
|---|---|
| MN | `web/backend/prompts/shadow/MN_AI_REGION_SPECIALIST_PROMPT_SHADOW_V104.md` |
| MT | `web/backend/prompts/shadow/MT_AI_REGION_SPECIALIST_PROMPT_SHADOW_V104.md` |
| MB | `web/backend/prompts/shadow/MB_AI_REGION_SPECIALIST_PROMPT_SHADOW_V104.md` |

Each declares region independence, region-specific gan thresholds, anti-noise rules, max 2-number output, strict vs diagnostic semantic.

## 8. Gating logic — anti-noise validation

`_classify_injection()` enforces:

| Path | Result |
|---|---|
| V103 = REQUIRED | REQUIRED_IN_PROMPT (direct) |
| V103 = REVIEW + recurrence STRONG/MEDIUM + lift ≥ 5 + non-gan core + ≥2 layers | REQUIRED_IN_PROMPT (upgrade) |
| V103 = REVIEW (otherwise) | OPTIONAL_REVIEW |
| V103 = REVIEW + only gan, no non-gan core | OPTIONAL_REVIEW with reason `ANTI_NOISE_GAN_ONLY` |
| V103 = BLOCKED | filtered upstream (not inserted) |

**Gan alone NEVER promotes to REQUIRED_IN_PROMPT.** Verified: 30d backfill produced 0 REQUIRED rows because no tail simultaneously satisfied recurrence STRONG/MEDIUM + lift ≥ 5 + non-gan core + ≥2 layers. This matches expectation given V102 stat distribution.

## 9. Hash guard — ZERO official mutation

| Table | Rows pre | SHA256 pre | Rows post | SHA256 post | Δ |
|---|---:|---|---:|---|---|
| `predictions` | 4625 | `28f207...db4933` | 4625 | `28f207...db4933` | IDENTICAL |
| `final_bundles` | 213 | `e3da0e...910005` | 213 | `e3da0e...910005` | IDENTICAL |
| `lottery_results` | 14642 | `6972fd...80fb32` | 14642 | `6972fd...80fb32` | IDENTICAL |
| `model_daily_eval` | 4493 | `a865b9...46cc` | 4493 | `a865b9...46cc` | IDENTICAL |

VPS post-hash matches local pre-hash exactly. ZERO official mutation. ZERO rows added to production tables.

## 10. Phase B gate (owner action)

Phase B (provider pilot) will populate `v104_shadow_prompt_model_decision` by calling a limited model roster per region (MN 3-5, MT 3, MB 3-5) with the V104 injection prompt and recording each model's ACCEPT / REJECT / HOLD decision. **Phase B is OWNER_GATE_REQUIRED.** Reasons:

- Provider cost: even limited 3-5 models × 3 regions × daily = ~10-15 calls/day. Owner should approve cost.
- Provider trust: real model decisions become evidence — owner should pre-approve which models are in the trust circle for V104 (suggested: claude-opus, gpt-5-pro, gemini-2.5-pro for MN; consensus subset for MT; cold-aware subset for MB).
- Latency: cron timing must not collide with production 19:35-19:55 VN closeout.

Until owner OK, V104 stays **Phase A: prompt produced, no provider called, decision table empty**.

## 11. Cron / scheduler

V104 is **not yet wired into `web/backend/scheduler.py`**. Phase A backfill ran via direct CLI (`python -m web.backend._v104_shadow_prompt_injection --mode backfill`). Adding a daily cron at 19:25 VN (after V103 cron at 19:24, before V96 master tracker at 19:22) is part of the Phase B owner-gate decision package. Don't auto-add cron until Phase B approved.

## 12. Cross-ref

- §52 hardlock: shadow table + admin API + `/monitoring` UI + CHANGELOG + SSOT + FU + AUTOMATION + Notion + private push + public push + hash guard → all delivered same session.
- §52F hardlock: Notion MCP automation attempted before defaulting to FU-170. Result: V104 sub-page created on canonical `Lottery_AI_Test`.
- V103 gate decisions feed V104 directly. V104 is the prompt-side counterpart of V103.
- V101 / V102 / V100 / V67 / V70 / V73 / V94 still feeding signals through V103 → V104.

## 13. Limitations / honesty

1. V103 gate has 0 REQUIRED today, so V104 has 0 REQUIRED_IN_PROMPT today. This is faithful to V103 logic; we do NOT pre-inflate.
2. V102 recurrence STRONG/MEDIUM list (61 rows for 2026-05-10 in `v102_candidate_recurrence_context_shadow`) does not currently include 13/61/64/89 — these come through OPTIONAL_REVIEW only. AI shadow chain still sees them.
3. Drive ingest for Báo Cáo 16 + Phân Tích Đánh Giá 1 = LISTED_NOT_READ (no Drive API in workspace). See `DRIVE_REPORT_INGEST_INDEX.md`.
4. Phase B provider call is not yet runnable; the column `provider_called` exists for forward compatibility.

## 14. Pending owner actions

- **FU-V104-PHASE-B-PROVIDER-PILOT (P1 OWNER_GATE_REQUIRED)**: approve provider roster + cost budget + cron slot for Phase B model decision pilot.
- **FU-V104-DRIVE-INGEST-PARTIAL (P2 OWNER_LOCK)**: provide Drive content access (paste, public link, or Drive MCP) so Báo Cáo 16 / Phân Tích Đánh Giá 1 can be ingested.
- **FU-V99-GITHUB-TOKEN-LEAK (P0 CRITICAL)**: still pending revoke of `ghp_cvoSP***`.

## 15. Final control matrix

| Control | Value | Proof |
|---|---|---|
| OFFICIAL_TOUCHED | **false** | 4 SHA256 IDENTICAL pre vs post |
| PRODUCTION_PROMPT_CHANGED | **false** | SP-4.1 not modified |
| PRODUCTION_SCORING_CHANGED | **false** | no selector / scoring touch |
| FINAL_BUNDLE_MUTATED | **false** | rows=213 unchanged |
| PREDICTIONS_MUTATED_BY_V104 | **false** | rows=4625 unchanged |
| SHADOW_ONLY | **true** | tables flagged |
| PROVIDER_CALLED | **false** | Phase A; v104_shadow_prompt_model_decision rows=0 |
| SECRET_PRINTED | **false** | Grep ghp_/sk-/AIza scan clean |
| NOTION_SYNC | (pending) | will create V104 sub-page next |
| PUBLIC_SYNC | (pending) | will commit + push |
| PRIVATE_SYNC | (pending) | will commit + push |
| MONITORING_PANEL | LIVE on VPS | `sectionV104ShadowPromptInjection` registered + auto-refresh 60s |
| V104_READY_FOR_7D_OBSERVE | **true** | 30d backfill = 1823 rows; daily 81 rows expected |

Status: Phase A DELIVERED. Phase B gated by owner.
