# Open Issues — V105.41 morning comprehensive audit (2026-05-14 09:25 VN)

Latest public truth: V105.41 covers the start of the 2026-05-14 live cycle. Yesterday 2026-05-13 cycles closed naturally for all three regions (MN id=301 BT=23 LOSE / lo2 PARTIAL — Wednesday MN weakest; MT id=302 BT=92 **WIN** BT/lo2/xien2 — Đà Nẵng tail=92; MB id=303 BT=32 LOSE all lanes — no challenger divergence). Today MN 04:15 cycle is clean: 15/15 auto_daily valid, final bundle id=304 ACTIVE BT=16 strong consensus. MT/MB cycles pending cron 16:30 / 17:35. Closed-file regression scope confirmed wider — 14 events across 7 source paths in 24 hours. Official prediction path unaffected; user-facing `/api/review-hub/filter` still returns HTTP 500 closed-file. V105.40 expansion patch is owner-gated for deploy after MB cycle close (~19:00 VN). `NATURAL_VERIFY_PARTIAL_PASS_NOT_FULL_PASS` preserved.

## V105.41 / V105.40 active issues

- `FU-V105-41-CLOSED-FILE-REGRESSION-MULTI-SITE`: **OPEN P0 / OWNER_LOCK** — 14 closed-file events on 2026-05-13 across 7 source paths (Excel writer, verify final bundle MN/MT/MB, Pattern Tracker, Shadow Daily Comparison, Shadow Rule D1 measurement, token AI provider wrapper, shadow eval provider wrapper). Service uptime 26d 8h; no restart since V105.35. V105.40 patch must extend further to wrap each path.
- `FU-V105-40-SAFE-STDIO-EXPANSION`: **OPEN P0 / OWNER_LOCK** — Patch design for shadow + main user-facing endpoints. Deploy gate: after MB 17:35 cycle close today (~19:00 VN). Backup + py_compile + smoke + journal scan + rollback path documented.
- `FU-V105-39-SHADOW-CLOSED-FILE-REGRESSION-P0`: **DEPLOYED_PENDING_LIVE_VERIFY** — Recurred today 2026-05-14 04:25 VN: `gpt-oss-120b` shadow ERROR closed-file diagnostic row. Contract V105.30d still held; no silent missing.
- `FU-V105-40b-REVIEW-HUB-FILTER-500`: **OPEN / WORKAROUND** — `/api/review-hub/filter?target_region=MN/MT/MB` returns HTTP 500 `{"detail":"I/O operation on closed file."}`. Page `/filter` overview tab stuck for users. Workaround: use `/du-doan`, `/api/mined-rules/overview`, `/api/so-gan` directly until V105.40 patch ships.
- `FU-V105-38-TIMEOUT-EXTENDED-GRACE-PROPOSAL`: **OPEN / OWNER_LOCK** — 500 s extended-grace lane proposal only; design proves not a single-constant flip.
- `FU-V105-35-SEMANTIC-PUBLISH-GATE-LATE-LANE-FORENSIC`: **DEPLOYED_PENDING_LIVE_VERIFY** — Confirmed by today's MN cycle (15/15 output rows, 15/15 scoreable, publish_ready=true).
- `FU-V105-34-OFFICIAL-DIAGNOSTIC-GATE-CLARITY`: **DEPLOYED_PENDING_LIVE_VERIFY** — Confirmed by yesterday's closed-file events all persisting diagnostic rows (no silent missing).
- `FU-V105-32-SOURCE-POOL-ROOT-CAUSE`: **OPEN / ACCURACY_LANE** — Plan-only; held until V105.40 patch deploys and 24h cycle is clean.
- `FU-V105-31-GLM51-COMPACT-PROFILE`: **OPEN / OWNER_GATE** — Compact JSON profile design exists for `glm-5.1` `finish_reason=length` case. No provider re-call without owner OK.

## V105.41 hard-lock invariants honored

- Official `/du-doan` publishes only the fixed 15/15 output-eligible roster.
- Production prompt / scoring / selector / bundle voting / WR-BT filter / model roster / cron timings — unchanged.
- Timeout 90 / 300 s unchanged. V105.38 500 s remains proposal only.
- No silent missing — V105.30d diagnostic-row contract held across 14 closed-file events.
- No shadow / lane-test backfill into official.
- No manual provider / AI call.
- No public root push when mirror is dirty (this release pushed only after working tree was cleaned).

## V105.33 / V105.32 / V105.31 carry-over

- `FU-V105-28-CLOSED-FILE-NO-TOKEN`: **CLOSED (V105.30)** — `_safe_stdio_ctx` bọc toàn bộ path no-token trên VPS; theo audit finalization + journal post-deploy.
- `FU-V105-28-AI-PRIORITY-ORDER`: **OPEN P1** — scheduler vẫn static `AUTO_AI_MODELS`; reorder strongest-first + tensor daily refresh chờ owner OK.
- `FU-V105-28-SSH-DEPLOY-KEY`: **CLOSED (account SSH)** — GitHub: `Hi irissnss! You've successfully authenticated`; mirror public push SSH.
- `FU-V105-28-TENSOR-REFRESH-CRON`: **OPEN P1** — materialize `model_strength_by_region_weekday_station_daily` định kỳ (đề xuất 19:30 VN).
- `FU-V105-30-NOTION-PAGE`: **DEFERRED** — owner ưu tiên GitHub raw thay vì Notion (page ID có thể bổ sung sau).
- `FU-V105-30B-RULE105-PRIZE-SOURCE`: **CLOSED / CORRECTED** — source lock theo `source_region`; 0 true violation; 30 prior flags are false positives.
- `FU-V105-30D-SHADOW-NO-MISSING-CONTRACT`: **DEPLOYED_PENDING_FULL_NATURAL_VERIFY** — V105.30d scheduler/database hardening deployed. MN 2026-05-12 proves shadow `13/13`, `missing_shadow=[]`; `glm-5.1` diagnostic empty row is valid non-timeout diagnostic, not missing. MT/MB natural-cycle verification remains pending at the 16:00 VN snapshot.
- `FU-V105-33-NATURAL-VERIFY-FULL-CYCLE`: **OPEN P1 / NATURAL_VERIFY_PENDING** — V105.33 sync `artifacts/live_sync/20260512_160034/manifest.json` shows no P0 regression, but MT/MB are not complete: both only `official=7/15`, no same-day final bundle, no natural shadow run. Do not call `V105_33_NATURAL_VERIFY_PASS` until MT/MB complete naturally and cleanly.
- `FU-V105-31-GLM51-COMPACT-PROFILE`: **OPEN P1 / OWNER_GATE** — `glm-5.1` full-context shadow run returned empty content with `finish_reason=length`; proposal file created in V105.32 as `glm-5.1_compact_json_profile`. No provider/manual re-call without owner OK.
- `FU-V105-32-SOURCE-POOL-ROOT-CAUSE`: **OPEN P1 / ACCURACY_LANE** — after runtime stability is clean, drill down where actual tails drop across `source_pool -> prompt -> rank -> top5 -> top2 -> bundle -> UI`, using `region + weekday + station_set` and Rule105 `source_region` wording. Plan created in V105.32; no official change.

## V105.27 carry-over

- `FU-V105-27-MN-D2-RANKED-PROMPT-WIRE`: PARTIAL/CLOSED-FOR-SHADOW. 137/137 injected; official prompt untouched.
- `FU-V105-27-TOP2-BUNDLER-AB`: OPEN. Shadow only; promotion math not met.
- `FU-V105-27-MB-D-V2-SHADOW`: OPEN/HOLD. `auto_disable=true`. Do not promote.
- `FU-V105-27-SECURITY-PAT-SSH`: CLOSED PAT side; SSH account live.

## Earlier carry-over

- `FU-V105-25-STATION-ALIAS-FIXUP`: CLOSED under canonical target `Thừa Thiên Huế`.
- `FU-V105-24-SOURCE-POOL-FORMULA`: OPEN / SUPERSEDED-BY-V105.32-PLAN for next execution wording. Miss matrix evolves; use V105.32 source-pool root-cause plan as current readout.
- `FU-V105-24-RELAXED-PROMOTION-RULE`: OPEN. Promotion gate >= 14d, save_ratio >= 0.30, break_ratio <= 0.10, net_save > 0, owner OK.

## Measurement risk

Không promote official từ các lane thí nghiệm; MT source formula và 4 bảng chính chỉ đọc/hash trong audit.
