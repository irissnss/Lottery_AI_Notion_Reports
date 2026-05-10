# Open issues — as of V105.6 (2026-05-10 12:40 VN)

## V105.6 status

V105.6 fixed public SSOT stale pointers and added dedicated source-pool data-health + no-token scoreboard. Current pre-MN-draw source status is `WAITING_MN` for MT/MB; this is expected until same-day results are scraped.

Active owner actions:

- `FU-V105-5-LIVE-CRON-VERIFY`: verify after natural 19:23 → 19:34 chain tonight.
- `FU-V105-5-SOURCE-PARTIAL-UI`: owner verify `/monitoring` sectionV105RegionalSourcePool after admin login.
- `FU-V105-SSH-DEPLOY-KEY`: revoke old/new PATs, approve SSH deploy key migration.
- `FU-V105-PREDICTION-QUALITY-REALTIME-AUDIT`: continue watching official/shadow separation.

---

## V104 Phase A delivered — `FU-V104-SHADOW-PROMPT-INJECTION` RESOLVED, 2 NEW FUs OPENED

V104 Phase A shipped (no provider call): 2 shadow tables + 3 region prompts MN/MT/MB independent + admin route 401 + UI panel registered loadAll/60s + Notion 2 sub-pages auto-created. Gating logic: gan alone NEVER promotes; REQUIRED_IN_PROMPT requires V103=REQUIRED OR (V103=REVIEW + recurrence STRONG/MEDIUM + lift_pp ≥ 5 + non-gan core + ≥2 layers). 13/61/64/89 audit: all 4 surface OPTIONAL_REVIEW today honestly. Hash 4 official tables IDENTICAL pre vs post.

**New FUs:**

- `FU-V104-PHASE-B-PROVIDER-PILOT` (P1 OWNER_GATE_REQUIRED): approve provider roster (suggested MN claude-opus + gpt-5-pro + gemini-2.5-pro; MT consensus subset; MB cold-aware subset) + cost budget + cron slot không đụng 19:35-19:55 VN production closeout.
- `FU-V104-DRIVE-INGEST-PARTIAL` (P2 OWNER_LOCK): WebFetch không đọc được Drive `.txt` content. Owner action: (1) paste Báo Cáo 16 + Phân Tích Đánh Giá 1 trong chat, OR (2) provide direct-download `?export=download&id=` URLs, OR (3) install Drive MCP server.

`FU-V104-SHADOW-PROMPT-INJECTION` Phase A → RESOLVED, superseded by `FU-V104-PHASE-B-PROVIDER-PILOT`.

## V103.2 Notion MCP self-sync — `FU-V103-2-NOTION-MCP-AUTOSYNC` DEPLOYED, `FU-170` RESOLVED

Owner explicitly demanded automatic Notion sync (22:42 VN). Agent discovered `user-notion` MCP in workspace (folder `mcps/user-notion/tools/` with full tool set), authenticated, created 2 sub-pages on canonical `Lottery_AI_Test` page (45 + 38 blocks). Codified `§52F NOTION MCP AUTOMATION OBLIGATION` in `.Antigravityrules.md` + `.AGENT.md` + `.cursorrules`. NEW public file `CONVERSATION_CONTEXT_V99_1_TO_V103_2_20260509.md` (verbatim owner messages 09:05 → 22:42 VN). FU-170 status flipped from `OWNER_LOCK` to `RESOLVED`. New FU `FU-V103-2-NOTION-MCP-AUTOSYNC` = `DEPLOYED_PENDING_LIVE_VERIFY`. Pass condition: owner opens Notion canonical page and sees the 2 new sub-pages.

## V103.1 owner re-emphasis — `FU-V103-1-MONITORING-UI` DEPLOYED

Owner re-emphasized at 22:12 VN: cross-region & D-1 recurrence patterns must have measurement table AND visual UI at `/monitoring`; codify rule into 3 governance files. V103.1 ships:

- Aggregator `_v103_cross_region_tracker.py` + admin route + UI panel `sectionV103CrossRegionTracker` registered in `loadAllSections()` + `setInterval(60s)`.
- Governance §52 MEASUREMENT-UI-DEPLOY-SYNC HARDLOCK in `.Antigravityrules.md` + mirrored in `.AGENT.md §9D` + `.cursorrules`.
- Status: `DEPLOYED_PENDING_LIVE_VERIFY`. Pass condition: live cycle 2026-05-10 19:00 VN populate panels with current-day candidates.

## Resolved this evening (V99.1 → V103)

| FU | Resolution | Version |
|---|---|---|
| FU-169 | Public reports stale V92 → V98 wrapper published | V98 |
| FU-176 | /monitoring V98 Command Center 10 panels deployed | V98 |
| FU-172 | Cron 23:45+ misfire — 6/6 cron fired naturally next day (APScheduler grace time, not bug) | V98.1 |
| FU-V97.1-CRON-MISFIRE | Same root cause as FU-172 | V98.1 |
| FU-V97.1-LOG-PERSIST | FALSE_NEGATIVE — em misread SQLite UTC `CURRENT_TIMESTAMP` as VN local | V98.1 |
| FU-171 | 4 file md5 drift = CRLF/LF only, not content drift | V99.1 (FALSE_NEGATIVE) |
| FU-V100-UI-GAN | du-doan-test UI fix + Gan calculator 252K rows | V100 |
| FU-V101-SHADOW-RULE-PROMPT | MN cross-region rule + V2 region prompts deployed shadow-only | V101 |
| FU-V102-RECURRENCE-TRACKER | 60d recurrence stats + candidate context shadow tables | V102 |
| FU-V103-CANDIDATE-SUPPLY-GATE | Supply audit + tightened prompt gate REQUIRED/REVIEW/BLOCKED | V103 (DEPLOYED_PENDING_LIVE_VERIFY) |

## Active items (post V103)

| FU | Severity | Title | Earliest decision |
|---|---|---|---|
| **FU-V99-GITHUB-TOKEN-LEAK** | P0 | **ROTATED 2026-05-10 00:15 VN** — VPS git remote `origin` updated to new owner-generated PAT, `git ls-remote` returns 494071b... (V104 commit head, auth working). New token NEVER written to any tracked file. Old `ghp_cvoSP***` still on owner's GitHub UI — **owner action: revoke explicitly**. | Owner revoke old PAT on GitHub Settings |
| **FU-V99-BT-SCORING-DEBATE** | P0 | LOCKED to `STRICT_DAC_BIET` production. `TAIL_ANY_PRIZE_DIAGNOSTIC` shadow only. | Revisit 2026-06-08 30d gate |
| **FU-V104-SHADOW-PROMPT-INJECTION** | P1 | OWNER_LOCK — actually inject V103 REQUIRED+REVIEW candidates into shadow AI prompts (per region MN/MT/MB independent), capture accept/reject for analysis | Awaiting owner OK (proposed [A]) |
| **FU-170** | P1 | Notion `Lottery_AI_Test` V93-V103 sync UNVERIFIED (no MCP in Cursor scope) | Owner provide MCP/manual copy |
| **FU-173** | P1 | Bundle conversion replay 30d evidence — preliminary scoreboard built, no promotion | 2026-05-21 14d gate |
| **FU-174** | P1 | Combo-super BT-first replay (combo_super uses WR not BT) | 2026-05-21 14d gate |
| **FU-175** | P1 | Prompt context injection dossier per region | 2026-05-21 14d gate |
| FU-V96-AUDIT-3 | P1 | combo_super uses WR not BT (BT-first North Star violation) | tied to FU-174 |
| FU-V96-AUDIT-4 | P1 | combo_super hardcode 6 AI (model_registry SSOT violation) | tied to FU-174 |

## V100→V103 hard contracts (shadow only)

- **NO official scoring touch** — production KPI = `STRICT_DAC_BIET` BT (UNCHANGED since V99.2 lock).
- **NO production prompt change** post V97 SP-4.1.
- **NO selector change** — V67/V70/V71/V73/HYBRID_V1 untouched.
- Gan / V101 rule / V102 recurrence / V103 supply gate are all `output_eligible=0`, `diagnostic_only=1`, `owner_approved=0`.
- Shadow tables created tonight (V100→V103):
  - `gan_signal_shadow_v100` (252K rows)
  - `v101_mn_cross_region_rule_shadow`
  - `v101_region_prompt_context_shadow`
  - `v102_recurrence_stats_shadow`
  - `v102_candidate_recurrence_context_shadow`
  - `v103_candidate_supply_shadow` (8743 rows 30d)
  - `v103_prompt_candidate_gate_shadow` (8743 rows 30d)

## Calendar gates

- ✅ 2026-05-09 22:00 VN: V99.1 → V103 chain delivered, governance synced (private commits 522969c / 7dc3536 / 2dac1ea / 582edab).
- 2026-05-10 04:24 VN: MN cascade SP-4.1 + V103 supply layers fill (post AI/test run).
- 2026-05-10 19:00 VN: live closeout, V99 evaluator scores D+1.
- 2026-05-12: 4 P0 methods reach 14d sample.
- 2026-05-14: V79/V80/V81 7d rolling + MB cold gate.
- 2026-05-21: 14d full + FU-173/174/175 gates + V101/V102/V103 first 7d evidence.
- 2026-06-08: 30d sweep + FU-V99-BT-SCORING-DEBATE revisit.
- 2026-07-06: 60d full review.
