## V105.6 — SSOT CLEAN + LIVE CRON VERIFY + REGIONAL SOURCE-POOL DATA HEALTH (2026-05-10 12:40 VN)

- Fixed public SSOT drift wrapper: latest pointer now V105.6 with V105.5 evidence and conversation context.
- Added dedicated `/monitoring` source-pool data-health panel and admin API.
- Added `v101_region_source_pool_evidence_shadow` and `v105_no_token_independent_scoreboard`.
- Deployed source-gated V104 Phase B guard: if source-pool is incomplete, Phase B logs `PHASE_B_BLOCKED_BY_SOURCE` and does not force provider calls.
- Official hashes unchanged 4/4; no production mutation.

---

## V105.5 — REGIONAL SOURCE-POOL LANE TEST MEASUREMENT (2026-05-10 11:50 VN)

- Added owner-approved V101 regional source pools:
  - `MN_D = (MN+MT+MB) D-1 + (MN+MT+MB) D-2`
  - `MT_D = (MN+MT+MB) D-1 + MN D`
  - `MB_D = (MN+MT+MB) D-1 + MN D + MT D`
- Backfilled 113 days on VPS: regional source-pool 10170 rows, top5 1695 rows, flag violations 0.
- `/monitoring` V105 panel now shows V101 top5 + source completeness; pre-draw state honestly reports `SOURCE_PARTIAL`.
- Official hashes unchanged 4/4; no production mutation.

---

## V105.2 — MONITORING LEGACY CONTRAST + NOTION/PUBLIC SYNC (2026-05-10 01:45 VN)

- Hardened legacy `/monitoring` pastel inline cards after owner screenshots showed low-contrast text in older V95/V103/V104 panels.
- Deployed frontend-only contrast fix; `/monitoring` remains admin-locked (`401` unauth).
- Created 4 Notion V105 pages under canonical `Lottery_AI_Test`.
- Redacted secret scans found no full `ghp_`, `sk-`, or Google `AIza` token patterns in private/public report trees.

---

## V105.1 — TRUE LANE TEST INDEPENDENCE + PROVIDER ROUTING FIX (2026-05-10 01:30 VN)

- Fixed GPT lane-test routing: `gpt-5.5` uses OpenRouter key source; GPT 5 mini/GPT 5.4 remain OpenAI-platform routed.
- Added independent AI shadow, no-token shadow, and context completeness audit surfaces. All V105 outputs remain `shadow_only=1`, `diagnostic_only=1`, `output_eligible=0`, `owner_approved=0`.
- Added `/monitoring` V105 Lane Test Control with provider health, why-empty/data health, status badges, and 60s refresh.
- Added prediction-quality data-health metadata so `/app` can show source/date/row counts without mixing shadow and official metrics.
- Verified VPS real run for target_date `2026-05-09`: 9 provider calls, 93 AI rows, 7422 no-token rows, 7515 context rows. Official table hashes unchanged 4/4.

---

## V104.1 — PHASE B ACTIVATED + GITHUB PAT ROTATED (2026-05-10 00:15 VN)

- Owner directive (verbatim, condensed): "Cập nhật API Token Githup Mới đi em "ghp_N9GS***" anh đã gennere rồi đó. Anh muốn Lane Test chạy thực sự với các thay đổi. Mắc gì sau 7 ngày mới nâng cấp khi mọi bằng chứng đề cho thấy các điều chỉnh phù hợp khi verify 60 ngày rồi mà em."
- **GitHub PAT rotation**: VPS git remote `origin` URL on `vietnix:/root/Lottery_AI_Test` updated to new owner-generated PAT. Verified via `git ls-remote origin HEAD` returns `494071b3d6046ec1fb9bd0cb51656878ac909596` (V104 commit head, auth working). New token NEVER written to any tracked file in private/public repo. Local Windows uses Credential Manager (clean). FU-V99-GITHUB-TOKEN-LEAK status `OPEN` → `ROTATED`. Owner manual action remaining: revoke old `ghp_cvoSP***` explicitly on GitHub UI.
- **V104 Phase B activated**: NEW backend `web/backend/_v104_phase_b_runner.py` (~370 lines) với limited roster 3 models × 3 regions = 9 calls/day max + 3 buffer (`MAX_TOTAL_CALLS_PER_DAY=12`). Roster: Claude Opus 4 + GPT-5-pro + Gemini 2.5 Pro per MN/MT/MB. Cost guard: 90s timeout, 1500 output tokens, 20 candidates per prompt max. 3 thin provider wrappers (Anthropic / OpenAI gpt-5/o-series-aware / Gemini google-genai+legacy fallback).
- V104 review prompt embeds full region prompt family + forces strict JSON `{decisions[], shadow_bt, shadow_lo2, max_two_numbers=true, production_weight=false}`. Decisions written to `v104_shadow_prompt_model_decision` với `provider_called=1, output_eligible=0, diagnostic_only=1, shadow_only=1`.
- **Scheduler crons added** in `web/backend/scheduler.py`: 19:24 VN daily V104 materializer + 19:30 VN daily V104 Phase B runner (BEFORE production cron 19:35-19:55 VN). Both registered in journalctl.
- **First real Phase B fire 2026-05-10 00:08 VN target_date=2026-05-09**: 9 calls fired total, 5 succeeded (3 Anthropic Opus + 2 Gemini empty/parse_fail), 4 failed (3 OpenAI 401 + 1 Gemini 503). 45 decision rows stored in `v104_shadow_prompt_model_decision`. Elapsed 216.66s.
  - **MN**: Claude Opus ACCEPT 2 / HOLD 2 / REJECT 16, shadow_bt='05' shadow_lo2=['13']. MN 13 = ACCEPT HIGH ("V67+V70+V73+V101 convergence, test_bt×2, strong pattern match") ✅ catches exact owner-flagged case.
  - **MT**: Claude Opus PARSE_FAIL (max_tokens=1500 hit), GPT-5-pro 401, Gemini PARSE_FAIL.
  - **MB**: Claude Opus ACCEPT 2 / HOLD 2 / REJECT 14 shadow_bt='37' shadow_lo2=['02']. MB 64 = REJECT MEDIUM ("AI-herd + V67 but no cross-region, MB herd suspicious").
  - **MN 89**: not in candidate set for 2026-05-09 (was earlier-day candidate).
- **Hash guard 4 official tables SHA256 IDENTICAL pre vs post** (predictions=4625 / final_bundles=213 / lottery_results=14642 / model_daily_eval=4493). ZERO production mutation. ✅
- **NEW FUs**: `FU-V104-1-OPENAI-KEY-INVALID` P0 (owner regen at platform.openai.com), `FU-V104-1-GEMINI-EMPTY-RESPONSE` P1 (SDK fallback), `FU-V104-1-MT-CLAUDE-TRUNCATED` P1 (bump max_tokens), `FU-V104-PHASE-B-7D-ADJUSTMENT` P2 (review 2026-05-17 19:30 VN).
- AUTOMATION_STATE seq 53 → 54 với phase_b_first_fire + hash_guard + github_pat_rotation arrays.
- NO production prompt change, NO selector touch, NO `/du-doan` mutation.

---

## V104 — SHADOW PROMPT INJECTION PER REGION (Phase A) (2026-05-09 23:55 VN)

- Owner directive (verbatim, condensed): "[V104 TOTAL FORCE] Mục tiêu chính là triển khai V104 shadow-only để candidate từ V103 thật sự đi vào prompt AI shadow theo từng miền MN/MT/MB, để model phải accept/reject với lý do rõ ràng."
- NEW backend `web/backend/_v104_shadow_prompt_injection.py` (~660 lines).
- 2 NEW shadow tables: `v104_shadow_prompt_candidate_injection` (1823 rows 30d backfill 2026-04-10 → 2026-05-10, 81 rows for 2026-05-09 — MN OPTIONAL=39 / MT OPTIONAL=24 / MB OPTIONAL=18, REQUIRED=0 honest) + `v104_shadow_prompt_model_decision` (0 rows Phase A; columns ready for Phase B ACCEPT/REJECT/HOLD per model).
- NEW admin route `/api/admin/v104-shadow-prompt-injection` (401 admin-locked).
- NEW UI section `sectionV104ShadowPromptInjection` registered in `loadAllSections()` AND `setInterval(60000)` of `web/frontend/monitoring.html` — 4 sub-panels (owner intent, per-region summary, strict vs diagnostic warning, per-region candidate tables), NO promote/rollback/trigger button.
- NEW 3 region prompts (independent): `web/backend/prompts/shadow/MN/MT/MB_AI_REGION_SPECIALIST_PROMPT_SHADOW_V104.md`. MN: MN_D = (MN+MT+MB) D-1+D-2 pool + gan 15d/7d. MT: anti-import + consensus-first + no-break guard. MB: cold-aware + gan 30d/15d + cross-region downstream priority.
- Gating logic: REQUIRED_IN_PROMPT = V103=REQUIRED OR (V103=REVIEW + recurrence STRONG/MEDIUM + lift_pp ≥ 5 + non-gan core + ≥2 layers). Gan alone NEVER promotes (anti-noise rule `ANTI_NOISE_GAN_ONLY`).
- 13/61/64/89 case audit: all 4 surface as OPTIONAL_REVIEW today (V103 gate=REVIEW, non_gan_core=true, V102 recurrence_class=None today → upgrade rule honestly miss).
- Notion MCP §52F: 2 V104 sub-pages auto-created on canonical `Lottery_AI_Test`: (1) `🧪 V104 — Shadow Prompt Injection per Region (Phase A, 2026-05-09)` id `35b1d385-9bf8-81bb-b5a8-ecffb0c817e6`, (2) `📝 V104 — Owner Conversation Context (Phiên 2026-05-09 22:00 → 23:50 VN)` id `35b1d385-9bf8-8150-88cf-e36abe524520`.
- VPS deploy: scp 6 files + restart lottery + 30d backfill on VPS = same 1823 rows. Endpoints: health=200, v104=401 admin-locked, v103=401, monitoring=401, du-doan=200.
- Hash guard 4 official tables IDENTICAL pre vs post: predictions=4625, final_bundles=213, lottery_results=14642, model_daily_eval=4493 — VPS post-hash matches local pre-hash exactly. ZERO official mutation.
- Phase B (provider pilot) = OWNER_GATE_REQUIRED (FU-V104-PHASE-B-PROVIDER-PILOT). Drive ingest LISTED PARTIAL (FU-V104-DRIVE-INGEST-PARTIAL).
- AUTOMATION_STATE seq 52 → 53 with `notion_pages[]` array + hash_guard array.
- NO runtime production change, NO official table touch, NO production prompt change.

---

## V103.2 — NOTION MCP AUTO-SYNC + §52F NOTION AUTOMATION HARDLOCK (2026-05-09 22:55 VN)

- Owner directive (verbatim): "tại sao không cập nhật Notion MCP được em? em tiến hành 1 cách tự động đi chứ, lớn quá thì chia nhỏ từng trang ra chứ em. Tổng hợp các yêu cầu mà anh anh trao đổi trong trò chuyện này đẩy lên github Pulic luôn nha em."
- Discovered `user-notion` MCP server in workspace (`mcps/user-notion/tools/`). Previous default to `FU-170 OWNER_LOCK` without first attempting MCP = `§52F_VIOLATION_NOTION_NOT_ATTEMPTED` (and `§52_OWNER_REREMINDER` because owner had flagged this ≥2 sessions).
- Authenticated as bot `Antigravity` workspace `TanPhat ERP`. Located canonical page `Lottery_AI_Test` (id `067b40e9-0096-47e7-952c-504503559a29`). Created 2 sub-pages:
  - `V103.1 — Cross-Region & D-1 Recurrence Tracker UI + §52 Hardlock` (id `35b1d385-9bf8-8156-94fc-d86cfa331153`, 45 blocks).
  - `Phiên 2026-05-09 — Tổng hợp yêu cầu owner + V99.1 → V103.1` (id `35b1d385-9bf8-8140-b9fc-d0583c5e02ff`, 38 blocks; verbatim owner messages 09:05 → 22:42 VN).
- NEW public file `evidence/CONVERSATION_CONTEXT_V99_1_TO_V103_2_20260509.md` — verbatim conversation context for the same content as Notion (so public GitHub holds the authoritative ngữ cảnh).
- NEW governance section `§52F NOTION MCP AUTOMATION OBLIGATION` (10 hard rules) in `.Antigravityrules.md` + mirrored `§9D-1` in `.AGENT.md` + Notion MCP Automation Rule section in `.cursorrules`. Mandates: discover MCP tools first, attempt MCP calls, only escalate to FU-170 with concrete error.
- FU-170 status flipped from `OWNER_LOCK` to `RESOLVED`. New FU `FU-V103-2-NOTION-MCP-AUTOSYNC` opened (`DEPLOYED_PENDING_LIVE_VERIFY`).
- AUTOMATION_STATE seq 51 → 52 with `notion_pages[]` array (page IDs + URLs) so future agents verify continuity without re-searching.
- NO runtime change, NO official table touch, NO production prompt change.

---

## V103.1 — CROSS-REGION & D-1 RECURRENCE TRACKER UI + §52 MEASUREMENT-UI-DEPLOY-SYNC HARDLOCK (2026-05-09 22:35 VN)

- Owner re-emphasized (2nd time): "lose hôm nay xổ ngày mai" + "lose miền trước xổ miền sau" must have measurement table AND visual UI at `https://xs.io.vn/monitoring`; codify rule into `.Antigravityrules.md` / `.AGENT.md` / `.cursorrules`.
- NEW `web/backend/_v103_cross_region_tracker.py` (290 lines) — admin-only aggregator combining V101 + V102 + V103 + V94 leakage shadow tables.
- NEW admin route `/api/admin/v103-cross-region-tracker` (401 unauth, 200 admin, no-store cache).
- NEW UI panel `sectionV103CrossRegionTracker` in `monitoring.html` with 4 panels:
  - P1 V101 MN D-1/D-2 cross-region top 15 today.
  - P2 V102 60d/90d recurrence stats with `eligible_for_shadow_boost` flag + STRONG/MEDIUM today.
  - P3 V103 prompt gate REQUIRED/REVIEW/BLOCKED counts + top + supply layer heatmap.
  - P4 V94 cross-region leakage continuous monitor.
- UI panel registered in `loadAllSections()` AND `setInterval(60s)` — auto-refresh, admin-locked, no promote/rollback button.
- NEW governance section `§52 MEASUREMENT-UI-DEPLOY-SYNC HARDLOCK` in `.Antigravityrules.md`: 13-deliverable contract + self-check matrix + violation taxonomy (`§52_VIOLATION_UI_MISSING`, `§52_VIOLATION_DOC_MISSING`, `§52D_DRIFT_VIOLATION`, `§52B_VIOLATION_REFRESH_MISSING`, `§52_OWNER_REREMINDER`).
- Mirrored §52 contract in `.AGENT.md §9D` + `.cursorrules`.
- VPS deploy + restart + smoke OK (`/api/health=200`, admin endpoint `=401`).
- Hash 4 official tables IDENTICAL pre/post.
- Notion sync payload: `evidence/NOTION_SYNC_PAYLOAD_V103_1.md`.
- FU-V103-1-MONITORING-UI = DEPLOYED_PENDING_LIVE_VERIFY (pass condition: 2026-05-10 19:00 VN cycle populate panels).
- Shadow only, output_eligible=0, diagnostic_only=1, owner_approved=0. Official UNCHANGED.

---

## V103 — CANDIDATE SUPPLY AUDIT + TIGHTENED PROMPT GATE (2026-05-09 21:55 VN)

- New shadow tables: `v103_candidate_supply_shadow` (8743 rows 30d) + `v103_prompt_candidate_gate_shadow` (8743 rows 30d).
- Supply audit tracks 11 source layers per candidate tail: AI / no-token / official / test / V67 / V70 / V73 / V101 / V102 / gan / rule.
- Prompt gate tightened: `REQUIRED` needs recurrence STRONG + ≥1 non-gan core layer + ≥2 total source layers. Gan support is secondary only — never alone promotes to REQUIRED.
- Smoke 2026-05-10 pre-cycle: REQUIRED=0, REVIEW=49, BLOCKED=251 (expected — D+1 core sources not yet run).
- Private commit `2dac1ea` + governance sweep `582edab`.
- V104 prompt injection = OWNER_LOCK pending (proposed [A]: shadow inject REQUIRED/REVIEW with accept/reject capture per region).
- Shadow only, output_eligible=0, diagnostic_only=1, owner_approved=0. Official UNCHANGED.

## V102 — D-1 LOST SIGNAL RECURRENCE TRACKER (2026-05-09 21:10 VN)

- New shadow tables: `v102_recurrence_stats_shadow` + `v102_candidate_recurrence_context_shadow`.
- Quantifies 4 recurrence patterns over 60d/90d:
  1. Same-region D-1 lost → D hit (e.g. MN yesterday losing prediction reappearing today).
  2. Cross-region same-day (MT D → MB D, MN D → MT D, etc.).
  3. Cross-region next-day (MN D-1 → MT D, MT D-1 → MB D).
  4. Combined STRONG/MEDIUM/WEAK class per candidate.
- Sources tracked: official, test_lane, V67/V70/V73 traces, V101 candidates, individual AI models.
- `recurrence_class`: STRONG → recommended for `PROMPT_REVIEW_STRONG`; MEDIUM → review only; WEAK/BLOCKED → not surfaced.
- Private commit `7dc3536`.
- Shadow only, no production runtime change.

## V101 — MN CROSS-REGION D-1/D-2 RULE + REGION-SPECIFIC V2 PROMPTS (2026-05-09 20:35 VN)

- New shadow tables: `v101_mn_cross_region_rule_shadow` (ranked MN candidates from previous-day MT/MB tails) + `v101_region_prompt_context_shadow` (per-region addendum text + context JSON).
- Three new region-specific shadow prompts (V2):
  - `MN_AI_REGION_SPECIALIST_PROMPT_SHADOW_V2.md`: V101 cross-region context + V100 gan + V99 evaluator semantic guards.
  - `MT_AI_REGION_SPECIALIST_PROMPT_SHADOW_V2.md`: consensus-first + gan diagnostic + semantic guards.
  - `MB_AI_REGION_SPECIALIST_PROMPT_SHADOW_V2.md`: MB gan thresholds + cold flag doctrine + semantic guards.
- New admin API: `/api/admin/v101-shadow-pilot` (admin-locked readout).
- 14d backfill done locally + VPS.
- Per-region independent — owner can tune one region without affecting others.
- Private commit `522969c`. Shadow only, NOT injected into production prompt SP-4.1 yet.

## V100 — `du-doan-test` UI FIX + GAN CALCULATOR FOUNDATION (2026-05-09 16:30 VN)

- `/du-doan-test` UI: default tab MN (was MB), mobile responsive @media 480/768, two new panels (Lịch sử dự đoán + Bảng chỉ số kỹ thuật).
- Two new admin APIs: `/api/admin/test-lane-history`, `/api/admin/test-lane-metrics`.
- New shadow table: `gan_signal_shadow_v100` (252K rows 30d) computing `gan_normal` (any prize) + `gan_special` (ĐB/G8) per region/station/tail.
- Owner-specified thresholds: MB normal=30 special=15; MN+MT normal=15 special=7.
- Private commit `5624570`.
- Shadow only, no production runtime change.

## V99.2 — TOTAL FORCE SECURITY + BT DOCTRINE LOCK + SCOREBOARD (2026-05-09 13:15 VN)

- Security scan PARTIAL: 0 PAT in working tree, .env protected by .gitignore, AI provider keys env-only. Owner must revoke `ghp_cvoSP***` PAT (FU-V99-GITHUB-TOKEN-LEAK P0).
- BT doctrine LOCKED: `STRICT_DAC_BIET` = production KPI (UNCHANGED). `TAIL_ANY_PRIZE_DIAGNOSTIC` = shadow signal only. FU-V99-BT-SCORING-DEBATE → DEFAULT KEEP STRICT (revisit 2026-06-08 30d gate).
- V99 evaluator sanity PASS: 10 tests OK, 747 rows shadow integrity 100%, STRICT_ZERO_VALIDATED 14d (Wilson 95% upper 0.7%).
- 14d/30d scoreboard: OFFICIAL strict 0% (n=42), TEST_LANE strict 0% (n=371). Lenient: OFFICIAL 38.1%, TEST_LANE 35.3%. NO method qualifies for production promotion.
- Bundle replay 10 hypotheses preliminary, ALL defer FU-173 14d gate.
- Private commit `d134838`, public `b0a4e7a`.

## V99.1 — TRUTH VERIFY + V99 EXACT EVALUATOR + 3 P0 FINDINGS (2026-05-09 11:35 VN)

- V99 exact station-aware evaluator built (`v99_exact_evaluator_results` shadow table). Supports `BT_STRICT_DAC_BIET` (production) and `TAIL_ANY_PRIZE_DIAGNOSTIC` (shadow).
- V98.1 metadata cleanup in `LATEST_REPORT.json`.
- 3 P0 findings:
  - **MB 2026-05-08 "56" report conflict** = EVALUATOR_SEMANTIC_DIFFERENCE (V93 multi-prize lenient vs production strict-ĐB; both correct under their semantic).
  - **GitHub PAT leak** in VPS git remote URL + private commit `fb2ae98` history (REDACTED in working tree, owner must revoke).
  - **VPS git drift expected** — VPS at `ceb36c2` V17.19.4 2026-04-19; all V77→V103 work via scp deploy mode.
- FU-171 false_negative resolved (CRLF/LF only, not content drift).
- Private commit `bfea15d` (token-redacted), public `74cab5b`.

## V98 — ABSOLUTE RUNTIME ↔ PUBLIC ↔ NOTION SSOT + MONITORING COMMAND CENTER (2026-05-09 00:50 VN)

- Public root pointer V92 → V98. README no longer claims V74 latest.
- V93-V97 batch (private commit `1cd2833`, 28 files +4759 -39) documented in V98 wrapper.
- /monitoring V98 Command Center 10 panels admin-locked auto-refresh 60s deployed:
  1. SSOT Status (public/private/runtime/Notion mismatch class)
  2. Runtime Parity (md5 + endpoint status)
  3. Natural-Fire Cron Tracker (11 crons row count)
  4. Accuracy Root Cause (10 items severity + FU)
  5. Owner Gate Queue (12 items)
  6. Prompt/Context Completeness (SP-4.1 + 21 fields)
  7. Bundle Conversion (V94.1 + V93 MN save 5d)
  8. Cross-Region Leakage (6 pairs × 3 windows)
  9. Data Freshness 30d (provisional vs clean)
  10. Public/Notion Sync Checklist
- 7 new FU items (FU-169 RESOLVED, FU-170-175 owner-gated, FU-176 RESOLVED).
- Hash guard 4 official tables IDENTICAL across V92.1 → V98 (predictions=4542, final_bundles=210, lottery_results=14634, model_daily_eval=4493).
- Notion `Lottery_AI_Test` sync UNVERIFIED (no MCP in Cursor scope) — FU-170 owner-locked.
- V97 SP-4.1 prompt fix (max 2 numbers) is verified live (predictions 30d 0/2102 rows ≥3).
- Cron natural-fire status PARTIAL (V66.1+V67 OK; V70/V73/V76/C16 0 rows post-restart) — FU-172 escalated.
- 4 file local↔VPS md5 drift documented (FU-171, runtime OK).
- NO official scoring/selector/prompt production change beyond V97 SP-4.1.

## V92 — ABSOLUTE SSOT RECONCILIATION (2026-05-08 01:30 VN)

- Public root pointer fixed to V92.
- V90 and V91 claims verified.
- V92 one-source truth wrapper published.
- No runtime change, no DB write, official unchanged.

## V91 — Total Reconciliation + Stale-FU Closure + Actionable Evidence Pass (2026-05-08 01:15 VN)

- NEWER_THAN_V89_FOUND verified: latest = V90.
- 74 stale FU re-audited: 54 SUPERSEDED + 13 RESOLVED + 7 NEEDS_RUNTIME (67/74 = 90% docs-only).
- 11 evidence matrices generated for Notion AI lookup (FU reconciliation, actionable evidence, method accuracy, region strategy, prompt status, routes audit, decision calendar hardened, per-decision tracking, stale-FU auto-update spec, 29 tabs audit, V91_ONE_SOURCE_INDEX).
- Decision calendar hardened with pass/fail/owner_action/auto_report.
- NO VPS deploy. NO UI change. NO DB write.
- 4 official tables hash byte-identical.

## V90 — Final cleanup (2026-05-08 01:05 VN)

- 5 final tabs in /monitoring (29 tabs total): 🐍 Backend Modules (293) / 📜 Scripts (19) / 🛠️ Web Helpers (42) / 🗺️ Active Roadmaps (2) / ⚖️ Cursor Rules (3).
- Schema v89_master_board_v3 → v90_master_board_v4 (36 keys).
- Total V85+V86+V87+V88+V89+V90 = ~1378 items reconciled.
- ĐẾN ĐÂY THẬT SỰ HẾT — không còn category nào sót.
- 4 official tables hash byte-identical.

## V89 — 5-extension pack (2026-05-08 00:55 VN)

- 6 new tabs in /monitoring (24 tabs total): Migrations / Live Cron (realtime next_run) / FU Audit (72/152 stale flagged) / Phase Findings (116 first paragraph) / Decision Log (22 DEC) / Governance Ledger (96 entries).
- Schema v88_master_board_v2 → v89_master_board_v3 (31 keys).
- monitoring.html 201KB → 209KB.
- ~1019 items reconciled across V85+V86+V87+V88+V89.
- 4 official tables hash byte-identical.

## V88 — TOTAL_ENCYCLOPEDIA + 6 new tabs in /monitoring (2026-05-08 00:40 VN)

- 6 new tabs: ⚙️ Settings (252) / 📜 Automation History (28) / 📋 FU History (151) / 🗓️ Phase Checkpoints (116) / 💾 VPS Backups (31) / 📓 Notion Docs (15).
- /monitoring now has **18 tabs** total.
- TOTAL_ENCYCLOPEDIA.md (36 KB) single searchable file.
- Backend extended `_v87_master_board.py` with 6 new READ-ONLY blocks.
- Schema bump `v87_master_board_v1 → v88_master_board_v2` (25 keys).
- monitoring.html 196KB → 201KB.
- ~991 items reconciled across V85+V86+V87+V88.
- 4 official tables hash byte-identical.

## V87 — Master Index 12 tabs in /monitoring (2026-05-08 00:25 VN)

- New backend module `_v87_master_board.py` READ-ONLY 370 lines.
- New admin endpoint `/api/admin/master-board` for Agent IDE single-call lookup.
- New `sectionV87MasterIndex` in /monitoring with 12 tabs: Models / Prompts / Rules / Mechanisms / Metrics / Shadow Methods / DB Tables / Cron / Frontend / API / Decision Calendar / Owner Gate.
- Cached payload, switch tab no re-fetch. Auto-refresh 60s.
- monitoring.html 162KB → 196KB (+34KB).
- 4 official tables hash UNCHANGED.

## V86 — TOTAL FORENSIC REGISTRY + V82 merged into /monitoring (2026-05-08 00:10 VN)

- TOTAL_PUBLIC_REGISTRY.md (26 KB) for Notion AI single-table lookup.
- V82 Master Control Board merged into /monitoring as sectionV82MasterControl.
- /v82-monitor standalone kept.
- 132 API endpoints + 12 frontend pages + 142 FU + 224 CHANGELOG + 116 phase_checkpoints.
- monitoring.html 142KB → 162KB (+20KB).
- 4 official tables hash UNCHANGED.

## V85 — DEEP MASTER CONTROL (2026-05-07 23:55 VN)

- 8 super-family full inventory: 41 AI models + 129 DB tables + 26 cron jobs + 8 prompts + 5 PFG cohorts + 3 V81 pilot models + 27 metrics + 59 shadow methods.
- ~298 distinct items reconciled.
- 4 official tables hash UNCHANGED.

## V84 — MASTER CONTROL BOARD (2026-05-07 23:30 VN)

- 24-row master control board covering ALL families V63 → V83.
- 18-method P0 portfolio maturity matrix: 14 READY_TO_EVALUATE, 4 WAIT 5 days (until 2026-05-12).
- 14d region split: 2 POTENTIAL_LIFT (strongest_to_final_preservation, counterfactual_decision_audit), 3 DESTRUCTIVE_BIAS.
- 60d evidence availability map per family.
- Decision calendar 11 specific VN dates 2026-05-08 → 2026-07-06.
- Owner-gate queue 9 items with trigger dates.
- D-1/D-2 subsumed; D-7 ambiguous resolved as 7d gate concept.
- UI master board spec proposed (owner OK pending).
- 4 official tables hash UNCHANGED.

## V83 — V82 MONITOR UI PANEL (admin-only, read-only) (2026-05-07 23:20 VN)

- New backend module `web/backend/_v82_monitor.py` (read-only payload, 18 keys).
- 2 new admin-required routes: `GET /v82-monitor` (HTML) + `GET /api/admin/v82-monitor` (JSON).
- New frontend `web/frontend/v82-monitor.html` — 7-section dashboard, auto-refresh 5min.
- Hard contract honored: NO promote/rollback/edit/trigger button, NO DB write, NO scoring/selector change.
- Pre/post hashes 4 official tables UNCHANGED.

## V82 — 60D EVIDENCE CONTROL PASS (2026-05-07 23:05 VN)

- 307 audit cells (method × region × window {60, 30, 14, 7, 4}).
- 60D real evidence: OFFICIAL/AI_HERD/NO_TOKEN_HERD + 6 V52.5 methods.
- MN: 2 promotion candidates clean lift — SPECIALIST_ROSTER +6.7pp (save=4 break=0); AI_CHAIN_PRESERVATION +7.5pp (save=5 break=1).
- MT: consensus-first doctrine confirmed (AI_HERD -6.7pp with 12 breaks).
- MB: cold confirmed; all methods within ±5pp.
- V67/V70/V73/V79 max 4-15d; V81 2d → RETRO_LIMITED, no promotion.
- NO_TOKEN vs AI: region-specific (MN +3.4pp, MT +8.3pp, MB -3.3pp); no global floor change.
- Hash guard: 4 official tables UNCHANGED.

## V81 — PROVIDER SHADOW PILOT (owner-approved) (2026-05-07 22:18 VN)

- 3 models × 3 regions × 2 days = 18 provider calls. 18/18 parse_status=OK. 0 contract violations.
- Each model: hits=3/6, would_save=1, would_break=0 (n=6).
- MN 2026-05-07: all 3 models converge on V67/V73 tail 95 vs OFFICIAL 94 (would_save).
- MT: stable consensus. MB: honest LOW conf + herd warnings.
- New cron 19:14 VN. Cron now 6 jobs daily.
- Hard contract: shadow_only=1, output_eligible=0, output_impact='false'. Official tables UNCHANGED.

## V80 — ABSOLUTE CLOSURE PASS (2026-05-07 21:55 VN)

- Notion MCP doctrine pages reconciled with code (7 key pages patched).
- New shadow tables: rule_phase_synthesis_shadow / no_token_rule_aware_pack_shadow / mb_regime_shift_shadow / mn_ai_herd_vs_v67_save_daily.
- New cron 19:12 VN. Official tables UNCHANGED.

## V79 — AI↔NO_TOKEN CROSS-VERIFICATION + CLUSTER-WEIGHTED CONSENSUS (2026-05-07 19:08 VN)

- Cluster-weighted consensus shadow + AI/NO_TOKEN cross-verification.
- Region policies: MN V67/V73 boost, MB cold treatment, MT consensus-first.
- New cron 19:08 VN. Official tables UNCHANGED.

## V78 — AI PROMPT/CONTEXT FORENSIC + REGION-SPECIALIST SHADOW PROMPTS (2026-05-07 19:10 VN)

- Region-specialist shadow prompts MN/MT/MB authored and audited (no provider call yet at V78).
- Scheduler tzinfo bug fixed (V77 selector chain).
- New cron 19:10 VN. Official tables UNCHANGED.

# CHANGELOG_PUBLIC

## V80
- Notion/code/runtime sync closure.
- Shadow completion surfaces.
- Official unchanged.

## V79
- AI↔NO_TOKEN cross verification.
