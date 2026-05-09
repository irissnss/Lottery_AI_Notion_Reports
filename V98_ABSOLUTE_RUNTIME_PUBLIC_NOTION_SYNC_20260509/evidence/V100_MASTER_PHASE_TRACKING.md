# V100 MASTER PHASE TRACKING — PUBLIC MIRROR

**Created:** 2026-05-09 15:35 VN  
**Source:** private `docs/V100_MASTER_PHASE_TRACKING.md`  
**Purpose:** public, redacted, read-first tracker for V93 → V100, active FUs, decision gates, and V101 proposal.

---

## Current Executive Truth

| Layer | Current truth | Status |
|---|---|---|
| Production output | Still uses `BT_STRICT_DAC_BIET` scoring and official selector | LOCKED / unchanged |
| Test lane | Active, admin-only, defaults to MN, has history + tech metrics panels | LIVE |
| Exact evaluator | `v99_exact_evaluator_results` ready, 747 rows, strict + diagnostic split | READY |
| Gan signals | `gan_signal_shadow_v100` ready, 252,000 rows 30d local + VPS | READY FOR V101 |
| Public reports | V98 root with V98.1/V99.1/V99.2/V100 evidence addenda | UPDATED |
| Notion | Not verified via MCP | FU-170 OWNER_LOCK |
| Security | GitHub PAT was exposed in VPS git remote and private history | OWNER_ACTION_REQUIRED |

---

## Version / Session Ledger

| Version | Requirement | Result | Status | Remaining |
|---|---|---|---|---|
| V93 | Live failure forensic, MB signal, 3-càng audit | MB 56 signal found; 3-càng display-only documented | DELIVERED | V99 clarified semantics |
| V93.1 | P0 shadow audits | WR gate / verdict / MN save-signal tables | DEPLOYED | Needs gate evidence |
| V93.2 | Fix cron stdout bug | 6 materializers patched; V98.1 verified 6/6 cron | DONE | None |
| V94 | Cross-region / D-2 forensic | Spillover and D-2 region-gated confirmed | DELIVERED | Owner-gated doctrine |
| V94.1 | Spillover safe batch | 3 shadow surfaces, cron 19:18 | DEPLOYED | Continue measurement |
| V95 | Data freshness + AI context | Context only 47.6%-52.4%; dashboard added | DEPLOYED | FU-175 |
| V96 | Master tracker | SSOT doc, backend, UI, cron 19:22 | DEPLOYED | Continue daily snapshot |
| V97 | Prompt max-2 fix | SP-4.1, 0 rows >=3 numbers | VERIFIED | Monitor |
| V98 | Public/runtime sync + command center | Public root fixed, V98 UI live | DELIVERED | Notion unverified |
| V98.1 | Morning sanity | 6/6 cron, V97 first live cycle | DONE | None |
| V99.1 | Truth verify + exact evaluator | MB 56 semantics resolved; evaluator 747 rows | DELIVERED | Security owner action |
| V99.2 | Security + doctrine + sanity + scoreboard | PAT redacted, doctrine locked, scoreboard, no promotion | DELIVERED | Revoke PAT |
| V100 | `/du-doan-test` UI + gan foundation | Default MN, mobile fix, history, metrics, gan 252K rows | DELIVERED | V101 prompts/rules |

---

## Active Issues and Owner Gates

| ID | Severity | Requirement | Current handling | Next action |
|---|---|---|---|---|
| FU-V99-GITHUB-TOKEN-LEAK | P0 | Revoke exposed GitHub PAT | Current files redacted; history/VPS remote may contain old token | Owner revoke immediately |
| FU-V99-BT-SCORING-DEBATE | P0 | Strict vs diagnostic BT semantics | Production locked to `BT_STRICT_DAC_BIET` | Revisit only with 30d evidence |
| FU-170 | P1 | Notion sync | No MCP proof | Owner provide MCP/screenshot |
| FU-173 | P1 | Bundle replay | V99 evaluator ready | 2026-05-21 |
| FU-174 | P1 | Combo-super BT-first / registry pool | Replay only | 2026-05-21 |
| FU-175 | P1 | Prompt context dossier | V100 gan ready | V101 / 2026-05-21 |

Resolved:
- FU-169 public stale fixed.
- FU-176 command center deployed.
- FU-172 cron misfire closed.
- FU-V97.1-LOG-PERSIST false negative.
- FU-171 CRLF/LF false negative.

---

## Test-Lane Reality Check

V99.2 scoreboard:

| Category | n | Strict production hit | Diagnostic any-prize hit |
|---|---:|---:|---:|
| Official | 42 | 0.0% | 38.1% |
| Test lane | 371 | 0.0% | 35.3% |

Conclusion:
- Test lane has not beaten official.
- No method is promotion-eligible.
- Any-prize is diagnostic only, not production win.

---

## V101 Recommended Next Step

**V101 Shadow Rule + Region Prompt Pilot**

| Phase | Requirement | Implementation | Safety |
|---|---|---|---|
| V101-A | MN-only cross-region source rule | `MN_D = (MN+MT+MB) D-1 + (MN+MT+MB) D-2` | shadow_only |
| V101-B | Region-specific shadow prompts | MN/MT/MB prompt variants with gan and V99 context | no production prompt change |
| V101-C | Gan injection | Use `gan_signal_shadow_v100` top normal/special signals | diagnostic only |
| V101-D | Monitoring panel | Admin read-only V100/V101 panel | admin-only |
| V101-E | Replay/live watch | 14d/30d measurement via V99 evaluator | no promotion |

Region notes:
- MN: use D-1/D-2 cross-region source union + gan normal >=15d + gan special G8/DB >=7d.
- MT: keep consensus-first, no noisy cross-region expansion.
- MB: use cold flag, gan normal >=30d, gan special DB >=15d, AI/no-token conflict, secondary survival.

---

## Decision Calendar

| Date | Gate |
|---|---|
| 2026-05-09 19:00 VN | Rerun evaluator after closeout; assess MN clusters |
| 2026-05-10 morning | Confirm V100 UI/mobile/gan |
| 2026-05-14 | 7d live review and MB cold check |
| 2026-05-21 | 14d FU-173/174/175 gate |
| 2026-06-08 | 30d strict/diagnostic replay and BT semantic revisit |
| 2026-07-06 | 60d MB specialist review |

---

## Hard Locks

- No `/du-doan` production change.
- No `/api/final-bundle` change.
- No `generate_final_bundle()` scoring change.
- No mutation of official production tables.
- No BT semantic shift to any-prize.
- No test-lane promotion.
- No full secrets in reports.

**STATUS:** ACTIVE PUBLIC MIRROR. Use this with private master for continuity.
