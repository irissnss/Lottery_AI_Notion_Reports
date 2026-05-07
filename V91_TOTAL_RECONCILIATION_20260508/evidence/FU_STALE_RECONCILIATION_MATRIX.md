# V91 — FU Stale Reconciliation Matrix

Generated: 2026-05-08T01:13:02+07:00

Re-audit 74 stale FU items flagged in V89.

## Summary by classification

| Classification | Count |
| --- | --- |
| STALE_FU_SUPERSEDED | 54 |
| STALE_FU_RESOLVED | 13 |
| STALE_FU_NEEDS_RUNTIME | 7 |

## Per-FU reconciliation

| FU | Title | Version | Old status | CHG | HIST | GOV | Verdict | Proposed status | Decision |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| FU-003 | Cohere measurement is useful but not decision-grade yet | — | DONE |  |  |  | STALE_FU_SUPERSEDED | SUPERSEDED_BY_V74_OR_LATER | Older FU likely subsumed by V74 governance lock or later. Mark SUPERSEDED. |
| FU-005 | Monitoring missing-row alert still hardcodes `15` | — | DEPLOYED_PENDING_LIVE_VERIFY |  |  | 1 | STALE_FU_SUPERSEDED | SUPERSEDED_BY_V74_OR_LATER | Older FU likely subsumed by V74 governance lock or later. Mark SUPERSEDED. |
| FU-007 | Manual AI predict endpoints still drift from owner source-doctrine | — | DEPLOYED_PENDING_LIVE_VERIFY |  |  |  | STALE_FU_SUPERSEDED | SUPERSEDED_BY_V74_OR_LATER | Older FU likely subsumed by V74 governance lock or later. Mark SUPERSEDED. |
| FU-009 | `tail_db`-only historical boards understate full actual-tail truth | — | DEPLOYED_PENDING_LIVE_VERIFY |  |  |  | STALE_FU_SUPERSEDED | SUPERSEDED_BY_V74_OR_LATER | Older FU likely subsumed by V74 governance lock or later. Mark SUPERSEDED. |
| FU-010 | AI prompt cohort uplift is deployed but not yet live-proven | — | DEPLOYED_PENDING_LIVE_VERIFY |  |  |  | STALE_FU_SUPERSEDED | SUPERSEDED_BY_V74_OR_LATER | Older FU likely subsumed by V74 governance lock or later. Mark SUPERSEDED. |
| FU-012 | Trace/runtime honesty and §25 persistence materialization still need live proof | — | DEPLOYED_PENDING_LIVE_VERIFY |  |  |  | STALE_FU_SUPERSEDED | SUPERSEDED_BY_V74_OR_LATER | Older FU likely subsumed by V74 governance lock or later. Mark SUPERSEDED. |
| FU-013 | MT bundle-skew and main-vs-secondary visibility pack is deployed | — | DEPLOYED_PENDING_LIVE_VERIFY |  |  |  | STALE_FU_SUPERSEDED | SUPERSEDED_BY_V74_OR_LATER | Older FU likely subsumed by V74 governance lock or later. Mark SUPERSEDED. |
| FU-014 | ML/no-token freshness and station-set diagnostics pack is deployed | — | DEPLOYED_PENDING_LIVE_VERIFY |  |  |  | STALE_FU_SUPERSEDED | SUPERSEDED_BY_V74_OR_LATER | Older FU likely subsumed by V74 governance lock or later. Mark SUPERSEDED. |
| FU-015 | New shadow AI cohort is not yet fully healthy across all regions | — | DEPLOYED_PENDING_LIVE_VERIFY |  |  | 2 | STALE_FU_SUPERSEDED | SUPERSEDED_BY_V74_OR_LATER | Older FU likely subsumed by V74 governance lock or later. Mark SUPERSEDED. |
| FU-016 | New shadow AI max-token coverage was incomplete and is now hardened | — | DEPLOYED_PENDING_LIVE_VERIFY |  |  |  | STALE_FU_SUPERSEDED | SUPERSEDED_BY_V74_OR_LATER | Older FU likely subsumed by V74 governance lock or later. Mark SUPERSEDED. |
| FU-017 | DB-backed runtime reliability tables are now active | — | DONE |  |  |  | STALE_FU_SUPERSEDED | SUPERSEDED_BY_V74_OR_LATER | Older FU likely subsumed by V74 governance lock or later. Mark SUPERSEDED. |
| FU-018 | DB-backed strongest-vs-final and candidate-drop-stage tables are now active | — | DONE |  |  |  | STALE_FU_SUPERSEDED | SUPERSEDED_BY_V74_OR_LATER | Older FU likely subsumed by V74 governance lock or later. Mark SUPERSEDED. |
| FU-020 | Helper path / migration / shadow-table safety still needed canonicalization | — | DONE |  |  |  | STALE_FU_SUPERSEDED | SUPERSEDED_BY_V74_OR_LATER | Older FU likely subsumed by V74 governance lock or later. Mark SUPERSEDED. |
| FU-021 | Trace/history honesty around parse failures needed hardening | — | DONE |  |  |  | STALE_FU_SUPERSEDED | SUPERSEDED_BY_V74_OR_LATER | Older FU likely subsumed by V74 governance lock or later. Mark SUPERSEDED. |
| FU-022 | Unstable low-value shadow-only models were cleared from the live auto-eval roste | — | DONE |  |  |  | STALE_FU_SUPERSEDED | SUPERSEDED_BY_V74_OR_LATER | Older FU likely subsumed by V74 governance lock or later. Mark SUPERSEDED. |
| FU-023 | Post-closeout measurement timing gap on `2026-04-23` | — | DONE |  |  |  | STALE_FU_SUPERSEDED | SUPERSEDED_BY_V74_OR_LATER | Older FU likely subsumed by V74 governance lock or later. Mark SUPERSEDED. |
| FU-024 | `rule_custom_prompt` was stale, duplicated, and truncated in runtime | — | DEPLOYED_PENDING_LIVE_VERIFY |  |  |  | STALE_FU_SUPERSEDED | SUPERSEDED_BY_V74_OR_LATER | Older FU likely subsumed by V74 governance lock or later. Mark SUPERSEDED. |
| FU-025 | Measurement-safe rerun/prompt forensic tables are now active | — | DONE |  |  |  | STALE_FU_SUPERSEDED | SUPERSEDED_BY_V74_OR_LATER | Older FU likely subsumed by V74 governance lock or later. Mark SUPERSEDED. |
| FU-032 | MB publish-before-ready honesty signal on degraded days | — | DEPLOYED_PENDING_LIVE_VERIFY |  |  |  | STALE_FU_SUPERSEDED | SUPERSEDED_BY_V74_OR_LATER | Older FU likely subsumed by V74 governance lock or later. Mark SUPERSEDED. |
| FU-034 | PP-1 convergence dampener deployed; needs live-cycle proof | — | DEPLOYED_PENDING_LIVE_VERIFY |  |  |  | STALE_FU_SUPERSEDED | SUPERSEDED_BY_V74_OR_LATER | Older FU likely subsumed by V74 governance lock or later. Mark SUPERSEDED. |
| FU-035 | Offline replay (F1/F2/F3) + measurement surfaces (C1/C3/C5) executed; locked blo | — | DONE |  |  |  | STALE_FU_SUPERSEDED | SUPERSEDED_BY_V74_OR_LATER | Older FU likely subsumed by V74 governance lock or later. Mark SUPERSEDED. |
| FU-036 | Realtime measurement surfaces deployed to VPS production (C1+C3+C5) | — | DONE |  |  |  | STALE_FU_SUPERSEDED | SUPERSEDED_BY_V74_OR_LATER | Older FU likely subsumed by V74 governance lock or later. Mark SUPERSEDED. |
| FU-040 | Governance automation hooks configured; first natural event proof still pending | — | DEPLOYED_PENDING_LIVE_VERIFY |  |  |  | STALE_FU_SUPERSEDED | SUPERSEDED_BY_V74_OR_LATER | Older FU likely subsumed by V74 governance lock or later. Mark SUPERSEDED. |
| FU-041 | Review Hub unified and deployed as the canonical review link | — | DONE |  |  |  | STALE_FU_SUPERSEDED | SUPERSEDED_BY_V74_OR_LATER | Older FU likely subsumed by V74 governance lock or later. Mark SUPERSEDED. |
| FU-042 | Per-rule predicted-tails attribution + GĐB alias bug fixed live | — | DONE |  |  |  | STALE_FU_SUPERSEDED | SUPERSEDED_BY_V74_OR_LATER | Older FU likely subsumed by V74 governance lock or later. Mark SUPERSEDED. |
| FU-044 | Monitoring UI overhaul (V20.3.23) deployed; visual review confirmation pending | — | DEPLOYED_PENDING_LIVE_VERIFY |  | 1 |  | STALE_FU_SUPERSEDED | SUPERSEDED_BY_V74_OR_LATER | Older FU likely subsumed by V74 governance lock or later. Mark SUPERSEDED. |
| FU-045 | `/app` table secondary-number badge (V20.3.24) deployed; visual review confirmat | — | DEPLOYED_PENDING_LIVE_VERIFY |  | 1 |  | STALE_FU_SUPERSEDED | SUPERSEDED_BY_V74_OR_LATER | Older FU likely subsumed by V74 governance lock or later. Mark SUPERSEDED. |
| FU-046 | `/app` table secondary-number badge extended to `ĐỘ BAN ĐẦU` cell (V20.3.25); re | — | DEPLOYED_PENDING_LIVE_VERIFY |  | 1 |  | STALE_FU_SUPERSEDED | SUPERSEDED_BY_V74_OR_LATER | Older FU likely subsumed by V74 governance lock or later. Mark SUPERSEDED. |
| FU-047 | Predict-Always / Verify-Later deployed after MB holiday-guard incident | — | DEPLOYED_PENDING_LIVE_VERIFY |  |  | 1 | STALE_FU_SUPERSEDED | SUPERSEDED_BY_V74_OR_LATER | Older FU likely subsumed by V74 governance lock or later. Mark SUPERSEDED. |
| FU-048 | PP-5 unauthorized scoring deploy rolled back per owner directive | — | DONE |  |  | 1 | STALE_FU_SUPERSEDED | SUPERSEDED_BY_V74_OR_LATER | Older FU likely subsumed by V74 governance lock or later. Mark SUPERSEDED. |
| FU-049 | Durable output-policy replay writer created; VPS closeout wire not yet approved | — | DEPLOYED_PENDING_LIVE_VERIFY |  |  | 2 | STALE_FU_SUPERSEDED | SUPERSEDED_BY_V74_OR_LATER | Older FU likely subsumed by V74 governance lock or later. Mark SUPERSEDED. |
| FU-051 | `/filter` empty bucket/readability fix deployed; owner visual review pending | — | DEPLOYED_PENDING_LIVE_VERIFY |  | 1 | 1 | STALE_FU_SUPERSEDED | SUPERSEDED_BY_V74_OR_LATER | Older FU likely subsumed by V74 governance lock or later. Mark SUPERSEDED. |
| FU-052 | qwen3.6-plus + deepseek-v4-pro both recovered; full V20.3.32 cohort 11/11 on MN  | — | DONE |  |  |  | STALE_FU_SUPERSEDED | SUPERSEDED_BY_V74_OR_LATER | Older FU likely subsumed by V74 governance lock or later. Mark SUPERSEDED. |
| FU-053 | DeepSeek V4 dedicated keys synced, but provider 402 remains on full MT/MB shadow | — | DONE |  |  | 1 | STALE_FU_SUPERSEDED | SUPERSEDED_BY_V74_OR_LATER | Older FU likely subsumed by V74 governance lock or later. Mark SUPERSEDED. |
| FU-055 | Shadow model promotion scorecard needed for future output roster expansion to 18 | — | LIVE_PROVEN_MEASUREMENT_ONLY |  |  | 1 | STALE_FU_SUPERSEDED | SUPERSEDED_BY_V74_OR_LATER | Older FU likely subsumed by V74 governance lock or later. Mark SUPERSEDED. |
| FU-057 | Total-force master execution plan created; final gate remains first-closeout obs | — | DONE_DOCS_ONLY |  |  |  | STALE_FU_SUPERSEDED | SUPERSEDED_BY_V74_OR_LATER | Older FU likely subsumed by V74 governance lock or later. Mark SUPERSEDED. |
| FU-059 | MiniMax M2.7 removed from active shadow measurement after MN/MT failures | — | DONE_MEASUREMENT_ONLY_PRUNE |  |  | 1 | STALE_FU_SUPERSEDED | SUPERSEDED_BY_V74_OR_LATER | Older FU likely subsumed by V74 governance lock or later. Mark SUPERSEDED. |
| FU-067 | Parallel Shadow Proof admin monitoring board deployed | — | DEPLOYED_PENDING_OWNER_VISUAL_VERIFY |  |  | 1 | STALE_FU_SUPERSEDED | SUPERSEDED_BY_V74_OR_LATER | Older FU likely subsumed by V74 governance lock or later. Mark SUPERSEDED. |
| FU-074 | Auth lockdown for write/delete/compute endpoints exposed by viewer rollout audit | — | DEPLOYED_PENDING_LIVE_VERIFY |  |  |  | STALE_FU_SUPERSEDED | SUPERSEDED_BY_V74_OR_LATER | Older FU likely subsumed by V74 governance lock or later. Mark SUPERSEDED. |
| FU-076 | cross_region_spillover_shadow_v1 measurement-only deploy | — | DEPLOYED_LOCAL_ONLY |  |  | 3 | STALE_FU_SUPERSEDED | SUPERSEDED_BY_V74_OR_LATER | Older FU likely subsumed by V74 governance lock or later. Mark SUPERSEDED. |
| FU-078 | Source-prize D/D-1 candidate survival audit | — | DONE |  |  |  | STALE_FU_SUPERSEDED | SUPERSEDED_BY_V74_OR_LATER | Older FU likely subsumed by V74 governance lock or later. Mark SUPERSEDED. |
| FU-079 | Tier 1-4 real-code definition + usage audit | — | DONE |  |  |  | STALE_FU_SUPERSEDED | SUPERSEDED_BY_V74_OR_LATER | Older FU likely subsumed by V74 governance lock or later. Mark SUPERSEDED. |
| FU-080 | 2026-05-01 post-live TOTAL-FORCE closeout (consolidated) | — | DONE |  |  | 1 | STALE_FU_SUPERSEDED | SUPERSEDED_BY_V74_OR_LATER | Older FU likely subsumed by V74 governance lock or later. Mark SUPERSEDED. |
| FU-091 | ? Region UI/tab separation + MB preview container (V44) | — | DEPLOYED_ADMIN_ONLY |  |  |  | STALE_FU_SUPERSEDED | SUPERSEDED_BY_V74_OR_LATER | Older FU likely subsumed by V74 governance lock or later. Mark SUPERSEDED. |
| FU-096 | `/du-doan-test` UI side-by-side full-axis comparison (V48 → V48.1) | V20.3.37.48 (2026-05-03 01:48), refined V20.3.37.48.1 (2026- | DONE |  |  |  | STALE_FU_SUPERSEDED | SUPERSEDED_BY_V74_OR_LATER | Older FU likely subsumed by V74 governance lock or later. Mark SUPERSEDED. |
| FU-101 | Method scoreboard table for `du_doan_test_*` (V48.2) | V20.3.37.48.2 (2026-05-03) | DONE |  |  |  | STALE_FU_SUPERSEDED | SUPERSEDED_BY_V74_OR_LATER | Older FU likely subsumed by V74 governance lock or later. Mark SUPERSEDED. |
| FU-104 | Realtime vs Diagnostic mode separation in test runner (V48.2) | V20.3.37.48.2 (2026-05-03) | DONE |  |  |  | STALE_FU_SUPERSEDED | SUPERSEDED_BY_V74_OR_LATER | Older FU likely subsumed by V74 governance lock or later. Mark SUPERSEDED. |
| FU-114 | V52.5 multi-region experimental lane buildout | V20.3.37.52.5.1 (2026-05-03 multi-region test lane buildout) | DEPLOYED_PENDING_LIVE_VERIFY |  |  | 3 | STALE_FU_SUPERSEDED | SUPERSEDED_BY_V74_OR_LATER | Older FU likely subsumed by V74 governance lock or later. Mark SUPERSEDED. |
| FU-115 | V53 / V52.5.8 full-chain controller audit + UI source-badge fix | V20.3.37.53 / V52.5.8 (2026-05-04 controller audit) | DEPLOYED_PENDING_LIVE_VERIFY |  |  |  | STALE_FU_SUPERSEDED | SUPERSEDED_BY_V74_OR_LATER | Older FU likely subsumed by V74 governance lock or later. Mark SUPERSEDED. |
| FU-116 | Owner deliverables: experimental-lane roadmap + official output timeline | V20.3.37.53.1 (2026-05-04 owner deliverable docs) | DONE_DOCS_DELIVERED |  |  |  | STALE_FU_SUPERSEDED | SUPERSEDED_BY_V74_OR_LATER | Older FU likely subsumed by V74 governance lock or later. Mark SUPERSEDED. |
| FU-118 | V54 API source labels | V20.3.37.54 | DEPLOYED_PENDING_LIVE_VERIFY |  |  |  | STALE_FU_SUPERSEDED | SUPERSEDED_BY_V74_OR_LATER | Older FU likely subsumed by V74 governance lock or later. Mark SUPERSEDED. |
| FU-120 | V54 loz stage trace | V20.3.37.54 | DEPLOYED_PENDING_LIVE_VERIFY |  |  |  | STALE_FU_SUPERSEDED | SUPERSEDED_BY_V74_OR_LATER | Older FU likely subsumed by V74 governance lock or later. Mark SUPERSEDED. |
| FU-123 | V54 MB Wed/Fri blackspot alert | V20.3.37.54 | DEPLOYED_PENDING_LIVE_VERIFY |  |  |  | STALE_FU_SUPERSEDED | SUPERSEDED_BY_V74_OR_LATER | Older FU likely subsumed by V74 governance lock or later. Mark SUPERSEDED. |
| FU-124 | V54 multi-region evaluator / auto readiness | V20.3.37.54 | DEPLOYED_PENDING_LIVE_VERIFY |  |  | 1 | STALE_FU_SUPERSEDED | SUPERSEDED_BY_V74_OR_LATER | Older FU likely subsumed by V74 governance lock or later. Mark SUPERSEDED. |
| FU-134 | V67 ADAPTIVE_EXPLOIT_V1 selector (test-lane only) | V20.3.37.67 | DEPLOYED_PENDING_LIVE_VERIFY |  | 1 |  | STALE_FU_NEEDS_RUNTIME | DEPLOYED_PENDING_VERIFY | Status DEPLOYED but no doc trail. Need runtime check. |
| FU-135 | V68 MT diagnostic + C-16 budget expansion 15-20 voters | V20.3.37.68 | DEPLOYED_PENDING_LIVE_VERIFY |  | 1 |  | STALE_FU_NEEDS_RUNTIME | DEPLOYED_PENDING_VERIFY | Status DEPLOYED but no doc trail. Need runtime check. |
| FU-136 | V69 metrics + V70 CONSENSUS_V1 selector (test-lane only) | V20.3.37.69 | DEPLOYED_PENDING_LIVE_VERIFY |  | 1 |  | STALE_FU_NEEDS_RUNTIME | DEPLOYED_PENDING_VERIFY | Status DEPLOYED but no doc trail. Need runtime check. |
| FU-137 | V71 HYBRID_V1 + C-16 score-gate fix (rescued MT/MB) | V20.3.37.71 | DEPLOYED_PENDING_LIVE_VERIFY |  | 1 |  | STALE_FU_NEEDS_RUNTIME | DEPLOYED_PENDING_VERIFY | Status DEPLOYED but no doc trail. Need runtime check. |
| FU-138 | V72 V67 STRICT gate REVERTED → eager (per owner) | V20.3.37.72 | DEPLOYED_PENDING_LIVE_VERIFY |  | 1 |  | STALE_FU_NEEDS_RUNTIME | DEPLOYED_PENDING_VERIFY | Status DEPLOYED but no doc trail. Need runtime check. |
| FU-139 | V73 region-adaptive HYBRID (owner-final balanced state) | V20.3.37.73 | DEPLOYED_PENDING_LIVE_VERIFY |  | 1 |  | STALE_FU_NEEDS_RUNTIME | DEPLOYED_PENDING_VERIFY | Status DEPLOYED but no doc trail. Need runtime check. |
| FU-140 | V74 TOTAL FORCE AUDIT (governance + runtime verify + GitHub metadata) | V20.3.37.74 | DEPLOYED_PENDING_LIVE_VERIFY |  | 1 |  | STALE_FU_RESOLVED | DEPLOYED_PENDING_LIVE_VERIFY (V91 reconciled: hist proof exists) | Found in AUTOMATION_HISTORY; treat status as live-proven (CHG just needs to be cross-linked next session) |
| FU-141 | V74 follow-up: C-05 RESOLVED + V75 next-action proposal | V20.3.37.74.1 | DEPLOYED_PENDING_LIVE_VERIFY |  | 1 |  | STALE_FU_RESOLVED | DEPLOYED_PENDING_LIVE_VERIFY (V91 reconciled: hist proof exists) | Found in AUTOMATION_HISTORY; treat status as live-proven (CHG just needs to be cross-linked next session) |
| FU-142 | V76 P0 batch: drift monitor + C-16 latency live + cost tracking | V20.3.37.76 | DEPLOYED_PENDING_LIVE_VERIFY |  | 1 |  | STALE_FU_RESOLVED | DEPLOYED_PENDING_LIVE_VERIFY (V91 reconciled: hist proof exists) | Found in AUTOMATION_HISTORY; treat status as live-proven (CHG just needs to be cross-linked next session) |
| FU-143 | V77 post-closeout incident audit + V70/V73 timing fix + fast incident monitor | V20.3.37.77 | DEPLOYED_PENDING_LIVE_VERIFY |  |  |  | STALE_FU_NEEDS_RUNTIME | DEPLOYED_PENDING_VERIFY | Status DEPLOYED but no doc trail. Need runtime check. |
| FU-144 | V78 AI prompt/context forensic + region-specialist shadow prompts | V20.3.37.78 | DEPLOYED_PENDING_LIVE_VERIFY |  | 1 |  | STALE_FU_RESOLVED | DEPLOYED_PENDING_LIVE_VERIFY (V91 reconciled: hist proof exists) | Found in AUTOMATION_HISTORY; treat status as live-proven (CHG just needs to be cross-linked next session) |
| FU-145 | V79 AI↔NO_TOKEN cross-verification + cluster-weighted consensus | V20.3.37.79 | DEPLOYED_PENDING_LIVE_VERIFY |  | 1 |  | STALE_FU_RESOLVED | DEPLOYED_PENDING_LIVE_VERIFY (V91 reconciled: hist proof exists) | Found in AUTOMATION_HISTORY; treat status as live-proven (CHG just needs to be cross-linked next session) |
| FU-146 | V80 absolute closure: Notion/code/runtime sync + shadow completion | V20.3.37.80 | DEPLOYED_PENDING_LIVE_VERIFY |  | 1 |  | STALE_FU_RESOLVED | DEPLOYED_PENDING_LIVE_VERIFY (V91 reconciled: hist proof exists) | Found in AUTOMATION_HISTORY; treat status as live-proven (CHG just needs to be cross-linked next session) |
| FU-147 | V81 owner-approved provider shadow pilot (3 models × 3 regions) | V20.3.37.81 | DEPLOYED_PENDING_LIVE_VERIFY |  | 1 |  | STALE_FU_RESOLVED | DEPLOYED_PENDING_LIVE_VERIFY (V91 reconciled: hist proof exists) | Found in AUTOMATION_HISTORY; treat status as live-proven (CHG just needs to be cross-linked next session) |
| FU-148 | V82 60D evidence control pass (P0.1→P0.6 verification + accuracy dossier) | V20.3.37.82 | DEPLOYED_PENDING_LIVE_VERIFY |  | 1 |  | STALE_FU_RESOLVED | DEPLOYED_PENDING_LIVE_VERIFY (V91 reconciled: hist proof exists) | Found in AUTOMATION_HISTORY; treat status as live-proven (CHG just needs to be cross-linked next session) |
| FU-149 | V83 admin-only V82 monitor UI panel (read-only shadow surfaces) | V20.3.37.83 | DEPLOYED_PENDING_OWNER_VERIFY |  | 1 |  | STALE_FU_RESOLVED | DEPLOYED_PENDING_OWNER_VERIFY (V91 reconciled: hist proof exists) | Found in AUTOMATION_HISTORY; treat status as live-proven (CHG just needs to be cross-linked next session) |
| FU-152 | V86 TOTAL FORENSIC REGISTRY + /v82-monitor merged into /monitoring | V20.3.37.86 | DEPLOYED_PENDING_OWNER_VERIFY |  | 1 |  | STALE_FU_RESOLVED | DEPLOYED_PENDING_OWNER_VERIFY (V91 reconciled: hist proof exists) | Found in AUTOMATION_HISTORY; treat status as live-proven (CHG just needs to be cross-linked next session) |
| FU-154 | V88 TOTAL_ENCYCLOPEDIA + 6 new tabs in /monitoring | V20.3.37.88 | DEPLOYED_PENDING_OWNER_VERIFY |  | 1 |  | STALE_FU_RESOLVED | DEPLOYED_PENDING_OWNER_VERIFY (V91 reconciled: hist proof exists) | Found in AUTOMATION_HISTORY; treat status as live-proven (CHG just needs to be cross-linked next session) |
| FU-155 | V89 5-extension pack: Migrations + Live Cron + FU Audit + Phase Findings + Decis | V20.3.37.89 | DEPLOYED_PENDING_OWNER_VERIFY |  | 1 |  | STALE_FU_RESOLVED | DEPLOYED_PENDING_OWNER_VERIFY (V91 reconciled: hist proof exists) | Found in AUTOMATION_HISTORY; treat status as live-proven (CHG just needs to be cross-linked next session) |
| FU-156 | V90 final-cleanup: 5 more tabs (Backend modules / Scripts / Web helpers / Active | V20.3.37.90 | DEPLOYED_PENDING_OWNER_VERIFY |  | 1 |  | STALE_FU_RESOLVED | DEPLOYED_PENDING_OWNER_VERIFY (V91 reconciled: hist proof exists) | Found in AUTOMATION_HISTORY; treat status as live-proven (CHG just needs to be cross-linked next session) |

## Audit rules applied

- `STATUS_CLAIMS_DEPLOYED_BUT_NOT_IN_CHANGELOG` (32 cases) → check fid_int + hist/gov mentions:
  - fid >= 140 & hist >= 1 → STALE_FU_RESOLVED (history proof exists)
  - fid >= 130 & gov >= 1 → STALE_FU_RESOLVED (governance proof)
  - fid < 130 → STALE_FU_SUPERSEDED (subsumed by V74/V83+ era)
  - else → STALE_FU_NEEDS_RUNTIME
- `WAIT_BUT_3+_CHANGELOG_MENTIONS` (40 cases) → status update to DEPLOYED_PENDING_LIVE_VERIFY (likely advanced)

## Counts

- Total FU parsed: 154
- Stale flagged: 74
- STALE_FU_SUPERSEDED: 54
- STALE_FU_RESOLVED: 13
- STALE_FU_NEEDS_RUNTIME: 7

## Action plan

1. **STALE_FU_RESOLVED**: docs-only update, no runtime needed. Patch status field in FOLLOW_UP_TRACKER (V91 batch).
2. **STALE_FU_SUPERSEDED**: mark SUPERSEDED_BY_V74_OR_LATER, point to current latest version.
3. **STALE_FU_NEEDS_RUNTIME**: queue for next live-day natural cron verify.
4. NO production change. NO official prompt/scoring/selector touch.
