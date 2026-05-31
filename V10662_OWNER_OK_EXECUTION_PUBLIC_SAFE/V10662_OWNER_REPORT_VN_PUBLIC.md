# V10662 — Owner OK Execution After V10661 Control Audit

Public-safe report for owner and external AI review tools.

## 1. Context

After the V10661 read-only control audit, the owner approved six items in one window. All six were executed in sequence, each with backup, verify, and reversibility. The session followed `.Antigravityrules.md` and `.AGENT.md` strictly: no provider call, no wallet impact, no DB table drop, no official prediction logic change.

## 2. Six Items Executed

### Item 1. P0 source mismatch — VPS git HEAD reset

Audit V10661 found VPS `git rev-parse HEAD` was stale at an old commit while local + private GitHub were on the latest. File-level raw hash showed the working tree on VPS already matched (files were correctly deployed), but the git pointer was stale, which breaks `git log` traceability and risks future drift.

Action:

- Backed up VPS `.git/HEAD`, `config`, `refs`, `packed-refs`, current `git status`, and `git log -5` into a timestamped backup folder.
- `git fetch origin --prune` then `git reset --hard origin/master`.
- Verified four official DB tables (`predictions`, `final_bundles`, `lottery_results`, `model_daily_eval`) have **identical sha256 pre/post** = zero official drift.
- Verified service active, scoped files compile.

Result: VPS git HEAD now equals private GitHub. Reversible via the saved backup.

### Item 2. P0 public LATEST_REPORT.json was stale

Audit V10661 found the public `LATEST_REPORT.json` pointer still showed an old version while the public repository already contained a newer report folder.

Action:

- Updated `LATEST_REPORT.json` to point to the current latest public package.
- Committed and pushed `Lottery_AI_Notion_Reports` main.

Result: external AI tools that follow `LATEST_REPORT.json` now see the current state.

### Item 3. CP-R1 shadow-prompt retired

Owner approved RETIRE rather than re-architecting an ex-ante version yet.

Action:

- Verified scheduler had five `DISABLED` markers from prior versions (post-draw shadow-prompt writers all off): V81 provider pilot, V104 Phase B, V101 19:23 writer, V104 materializer 19:24, V105 lane-test control 19:34.
- Verified shadow-prompt history tables stopped receiving new rows after their respective disable dates. Historical rows kept for UI history per `KEEP_UI_HISTORY` policy.
- No new disable needed; documented retirement in roadmap, SSOT, follow-up tracker, and open items register.

Result: post-draw lookahead writers stay off. Any future ex-ante pilot must pass a no-lookahead harness before tokens are spent.

### Item 4. O10 — 12 local-only V105.2x files purged

Owner approved deletion. These files exist only in local working tree, were superseded by later versions, and are not present on VPS (confirmed by file listing).

Action:

- Backed up all 12 files (~225 KB total) into a timestamped backup folder under `artifacts/v10662_o10_purge/`.
- Deleted from local `web/backend/`.
- `_v10522_live_prep.py` was kept because VPS still runs it.
- Verified `main.py` two endpoints that reference one of the purged files use lazy import with try/except, so the API endpoints stay defined and return graceful errors instead of crashing.

Result: less local sprawl, no VPS impact.

### Item 5. O19 — MB AI LIMIT plan surface (not freeze, keeps measurement)

Owner directive: LIMIT, not freeze; keep weak models measured so RECOVERING can be detected.

Action:

- Added `web/backend/_v10662_mb_ai_limit.py` and table `mb_ai_limit_plan`.
- Built data-driven LIMIT classification from `model_progress`:
  - LIMIT: edge_pp at most −3.0 with n at least 20. Suggested vote weight multiplier 0.5.
  - RELEASE: model is RECOVERING or edge_pp at least 0.
  - KEEP: healthy.
  - THIN: not enough data.
- Auto-refreshes `slice_policy` MB `blocked_models_json` daily.
- `slice_policy.enabled` is kept at 0 — this is **surface only, NOT wired into official voting**.
- Cron at 09:30 daily.

Initial classification:

| Decision | Count |
| --- | ---: |
| LIMIT | 12 |
| RELEASE | 5 |
| KEEP | 2 |
| THIN | 16 |
| Total | 35 |

Plan: review the plan stability for about seven days. If the LIMIT list and RECOVERING releases are correct, owner can later approve wiring into vote (separate change, will need owner OK again).

### Item 6. D2 — Cohere KEEP_MEASURE

Verified Cohere is currently classified as `rerank_measurement_count=1`, not output-eligible. No `predictions` rows written for Cohere in the last seven days. The current state is consistent with shadow-only measurement.

Action:

- No change to runtime. Document the rationale and review again in about 14 days.

## 3. Safety

- Official prediction logic: unchanged.
- DB tables: zero dropped, zero altered for official tables, only the new `mb_ai_limit_plan` added.
- Provider calls: none.
- Wallet impact: none.
- Backups taken: VPS git state, VPS pre-deploy folder for V10662, local 12 V105.2x files.
- Service active after every change.

## 4. Three-Way Consistency Post-V10662

- Private local: latest V10662 commit.
- Private GitHub `Lottery_AI_Test` main branch: same.
- VPS working tree + git HEAD: same.

This is the first time in this chain that all three sources are at identical commits with identical file hashes.

## 5. Live Verification

- `/api/health` returns 200 with `runtime_model_count=28`, `expected_output_model_count=15` unchanged.
- `/login` returns 200.
- `/du-doan-test` and `/monitoring` return 401 for unauthenticated requests (correct admin protection).
- 15 of 15 system health checks OK.

## 6. Next Watch Points

- The next natural fire for `slice_health`, `model_progress`, `mb_ai_limit_plan`, and the disabled writer markers happens on the next daily cron cycle.
- The MT and MB BT override evaluation continues for about 10 to 14 live days.
- CP-66.7 data-blocked checkpoint reviews on 2026-06-03.
- MB AI LIMIT plan stability review in about seven days before any wiring discussion.
