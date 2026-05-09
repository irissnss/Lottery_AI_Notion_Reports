# NEXT ACTION (V104.1 — 2026-05-10 00:15 VN, Phase B Activated + GitHub PAT Rotated)

V99.1 → V104.1 chain delivered. **All shadow-only, official UNCHANGED. Phase B activated under owner explicit acceleration directive.**

## V104.1 owner directive (2026-05-09 23:57 VN)

> "Cập nhật API Token Githup Mới đi em "ghp_N9GS***" anh đã gennere rồi đó.
> Anh muốn Lane Test chạy thực sự với các thay đổi. Nếu quá sai thì kiểm soát điều
> chỉnh sau 7 ngày, mắc gì sau 7 ngày mới nâng cấp trong khi mọi bằng chứng đề
> cho thấy các điều chỉnh phù hợp khi verify 60 ngày rồi mà em."

**V104.1 = response chain:**

- **GitHub PAT rotated**: VPS git remote `origin` URL on vietnix updated với new owner-generated token. `git ls-remote origin HEAD` returns `494071b...` = V104 commit head, auth working. New token NEVER written to any tracked file. FU-V99-GITHUB-TOKEN-LEAK status `OPEN` → `ROTATED`. **Owner action remaining: revoke old `ghp_cvoSP***` PAT explicitly on GitHub Settings → Developer settings.**
- **V104 Phase B activated**: NEW `web/backend/_v104_phase_b_runner.py` (~370 lines) + 3 thin provider wrappers (Anthropic / OpenAI / Gemini) + scheduler crons 19:24 + 19:30 VN daily.
- **First real fire 2026-05-10 00:08 VN target_date=2026-05-09**: 9 calls fired, 5 ok, 4 failed, 45 decision rows stored. Elapsed 216.66s.
- **Owner-flagged case audit**: **MN 13 = ACCEPT HIGH** by Claude Opus với reason "V67+V70+V73+V101 convergence, test_bt×2, strong pattern match" — Phase B catches the exact case owner flagged at 21:25 VN ✅.
  - MB 64 = REJECT MEDIUM by Claude Opus ("AI-herd + V67 but no cross-region, MB herd suspicious").
  - MT 61 = PARSE_FAIL (Claude max_tokens=1500 truncated → FU-V104-1-MT-CLAUDE-TRUNCATED).
  - MN 89 = not in 2026-05-09 V104 candidate set (was earlier-day candidate).
- **Hash guard**: 4 official tables SHA256 IDENTICAL pre vs post (predictions=4625, final_bundles=213, lottery_results=14642, model_daily_eval=4493). ZERO production mutation.
- **7-day adjustment review gate**: 2026-05-17 19:30 VN per owner directive.

**Owner action**:

1. **Revoke old GitHub PAT explicitly** on GitHub Settings → Developer settings → Personal access tokens. New PAT đã active VPS-side; old PAT vẫn valid until owner revokes.
2. **Regenerate OPENAI_API_KEY** at https://platform.openai.com/api-keys (current `sk-proj-***` returns 401) → update VPS `/root/Lottery_AI_Test/.env` → `systemctl restart lottery`. Without this, 3 calls/day fail (Anthropic + Gemini still fire).
3. Watch https://xs.io.vn/monitoring V104 panel daily 19:30 VN cycle to see Phase B decisions populate.
4. 2026-05-17 19:30 VN: review 7-day Phase B evidence (FU-V104-PHASE-B-7D-ADJUSTMENT).

---

## V104 owner directive (2026-05-09 23:23 VN)

Owner: "[V104 TOTAL FORCE] Mục tiêu chính là triển khai V104 shadow-only để candidate từ V103 thật sự đi vào prompt AI shadow theo từng miền MN/MT/MB, để model phải accept/reject với lý do rõ ràng."

**V104 = response chain:**
- NEW backend `web/backend/_v104_shadow_prompt_injection.py` (~660 lines).
- 2 NEW shadow tables: `v104_shadow_prompt_candidate_injection` (1823 rows 30d backfill) + `v104_shadow_prompt_model_decision` (Phase B placeholder).
- 3 NEW independent region prompts: `MN/MT/MB_AI_REGION_SPECIALIST_PROMPT_SHADOW_V104.md`.
- NEW admin route `/api/admin/v104-shadow-prompt-injection` (401 admin-locked).
- NEW UI section `sectionV104ShadowPromptInjection` (loadAll + 60s refresh, 4 sub-panels).
- Notion MCP §52F: 2 V104 sub-pages auto-created (id `35b1d385-9bf8-81bb-b5a8-ecffb0c817e6` + `35b1d385-9bf8-8150-88cf-e36abe524520`).
- Hash 4 official tables IDENTICAL pre vs post (predictions=4625 / final_bundles=213 / lottery_results=14642 / model_daily_eval=4493).
- 13/61/64/89 case audit: all 4 surface OPTIONAL_REVIEW today (V103=REVIEW, non_gan_core=true, V102 recurrence_class=None today → upgrade rule honestly miss).

**Owner action**:
1. Open https://xs.io.vn/monitoring → see new `sectionV104ShadowPromptInjection` panel.
2. Open https://www.notion.so/Lottery_AI_Test-067b40e9009647e7952c504503559a29 → see new V104 sub-pages.
3. Decide on `FU-V104-PHASE-B-PROVIDER-PILOT`: approve provider roster + cost budget + cron timing.
4. Decide on `FU-V104-DRIVE-INGEST-PARTIAL`: paste Drive content OR install Drive MCP.

---

## V103.2 owner re-emphasis (2026-05-09 22:42 VN) — Notion MCP

Owner: "tại sao không cập nhật Notion MCP được em? em tiến hành 1 cách tự động đi chứ, lớn quá thì chia nhỏ từng trang ra chứ em. Tổng hợp các yêu cầu mà anh anh trao đổi trong trò chuyện này đẩy lên github Pulic luôn nha em."

**V103.2 = response chain:**
- Discovered `user-notion` MCP server in workspace (`mcps/user-notion/tools/` with 22 API tools). Previous default `FU-170 OWNER_LOCK` = `§52F_VIOLATION_NOTION_NOT_ATTEMPTED`.
- Authenticated as bot `Antigravity` workspace `TanPhat ERP`. Located canonical page `Lottery_AI_Test` (id `067b40e9-0096-47e7-952c-504503559a29`).
- Created 2 Notion sub-pages (auto, no manual copy-paste):
  - `V103.1 — Cross-Region & D-1 Recurrence Tracker UI + §52 Hardlock` (id `35b1d385-9bf8-8156-94fc-d86cfa331153`, 45 blocks).
  - `Phiên 2026-05-09 — Tổng hợp yêu cầu owner + V99.1 → V103.1` (id `35b1d385-9bf8-8140-b9fc-d0583c5e02ff`, 38 blocks; 10 timestamped owner messages 09:05 → 22:42 VN).
- NEW public file `evidence/CONVERSATION_CONTEXT_V99_1_TO_V103_2_20260509.md` — verbatim owner messages + agent confirmations.
- Codified `§52F NOTION MCP AUTOMATION OBLIGATION` in `.Antigravityrules.md` (10 hard rules) + mirrored `§9D-1` in `.AGENT.md` + Notion MCP Automation Rule section in `.cursorrules`.
- FU-170 status flipped from `OWNER_LOCK` → `RESOLVED`. New FU `FU-V103-2-NOTION-MCP-AUTOSYNC` = `DEPLOYED_PENDING_LIVE_VERIFY`.

**Owner action**: open https://www.notion.so/Lottery_AI_Test-067b40e9009647e7952c504503559a29 → see 2 new sub-pages V103.1 + Phiên 2026-05-09 (live-verify).

---



## V103.1 owner re-emphasis (2026-05-09 22:12 VN)

Owner đã nhắc lần thứ 2: "có bảng theo dõi đo lường không em ... có UI trực quan ở https://xs.io.vn/monitoring để theo dõi và không bị lãng quên ... cập nhật changlog Notion MCP, deploy code, githup pri/Public, ghi nhận vào .AGENT/.Antigravityrules/.cursorrules để luôn luôn tuân thủ".

**V103.1 = response chain:**
- NEW `web/backend/_v103_cross_region_tracker.py` — admin-only aggregator (V101 + V102 + V103 + V94 leakage trong 1 payload).
- NEW admin route `/api/admin/v103-cross-region-tracker` (401 unauth, 200 admin).
- NEW UI panel `sectionV103CrossRegionTracker` ở `https://xs.io.vn/monitoring` với 4 panels (V101 MN top 15, V102 60d recurrence, V103 prompt gate, V94 leakage). Auto-refresh 60s.
- NEW `.Antigravityrules.md §52` MEASUREMENT-UI-DEPLOY-SYNC HARDLOCK + mirror `.AGENT.md §9D` + `.cursorrules`. Codify 13-deliverable contract để không quên ở phiên sau.
- VPS deploy + restart + smoke OK. Hash 4 official tables IDENTICAL.
- Notion sync payload: `evidence/NOTION_SYNC_PAYLOAD_V103_1.md`.
- FU-V103-1-MONITORING-UI = DEPLOYED_PENDING_LIVE_VERIFY.



## Đã làm tối nay (2026-05-09)

| Version | Scope | Status |
|---|---|---|
| V99.1 | Truth verify + V99 exact evaluator (station-aware STRICT/DIAGNOSTIC) + 3 P0 findings | DELIVERED (private bfea15d, public 74cab5b) |
| V99.2 | Security scan + BT doctrine LOCK STRICT_DAC_BIET + 14d/30d scoreboard + bundle replay preliminary | DELIVERED (private d134838, public b0a4e7a) |
| V100 | `du-doan-test` UI fix (default MN, mobile responsive, history + tech metrics) + Gan calculator 252K rows | DELIVERED (private 5624570) |
| V101 | MN cross-region D-1/D-2 rule shadow + region-specific V2 prompts + admin readout API | DELIVERED (private 522969c) |
| V102 | 60d recurrence tracker (lost-D → hit-D+1 + cross-region) + candidate context STRONG/MEDIUM/WEAK class | DELIVERED (private 7dc3536) |
| V103 | Candidate supply audit + tightened prompt gate REQUIRED/REVIEW/BLOCKED | DELIVERED (private 2dac1ea + governance 582edab) |

## V103 prompt gate logic (hardened)

- `REQUIRED`: recurrence_class STRONG **AND** ≥1 non-gan core layer (AI / test / official / V67-V70-V73 / V101 / rules) **AND** ≥2 total source layers.
- `REVIEW`: recurrence MEDIUM/STRONG with ≥1 layer support, but doesn't meet REQUIRED bar.
- `BLOCKED`: recurrence WEAK or no corroboration — never injected.
- **Gan support is secondary** — alone never promotes to REQUIRED. This prevents "long-unseen flood" from drowning AI prompts.

## Smoke 2026-05-10 (pre-cycle, expected pattern)

- `REQUIRED=0` (D+1 official not yet drawn, AI/test for D+1 hasn't run yet) — natural empty state.
- `REVIEW=49`, `BLOCKED=251` — lower-layer signals already present.
- After 04:24 VN MN cascade + 16:30/18:30 VN MT/MB cascade + 19:14-19:22 shadow chain, supply layers fill → REQUIRED count will populate.

## V104 OWNER_LOCK (next decision)

Next logical step is V104 = **actually inject** V103 REQUIRED+selected REVIEW candidates into the SHADOW AI prompts (still shadow-only, max 2 numbers, no production runtime change), and capture per-region MN/MT/MB accept/reject decisions for analysis.

**Anh xác nhận điều gì để em tiếp tục:**

- [A] Tiếp tục V104: shadow prompt injection + accept/reject capture (per region MN/MT/MB independent, fully shadow), không touch production prompt SP-4.1.
- [B] Đợi 1-2 chu kỳ live (2026-05-10/11) để V103 supply fill rồi mới V104.
- [C] Khác — anh chỉ định.

Mặc định em **đề xuất [A]** vì owner đã phê duyệt độc lập per-region và lane test đã sẵn sàng.

## Owner pending (P0/P1)

- **P0 FU-V99-GITHUB-TOKEN-LEAK** — owner cần revoke PAT `ghp_cvoSP***` (VPS git remote + private commit fb2ae98 history).
- **P0 FU-V99-BT-SCORING-DEBATE** — locked to STRICT_DAC_BIET production, revisit 2026-06-08 30d gate.
- **P1 FU-170** Notion `Lottery_AI_Test` sync — em không có MCP access, owner cần copy payload manual hoặc cấp MCP.
- **P1 FU-173 / FU-174 / FU-175** — defer 2026-05-21 14d gate.

## Auto (no owner action)

- 2026-05-10 04:24 VN — MN cascade SP-4.1 (continuing daily).
- 2026-05-10 16:30/18:30 VN — MT + MB cascade.
- 2026-05-10 19:14-19:22 VN — 5-cron shadow chain (V81/V93.1/V94.1/V95/V96).
- 2026-05-10 23:35-23:55 VN — V93.2 stdout fix cron continuing.
- V100 Gan signal + V101/V102/V103 shadow tables refresh on schedule.

## Read first

- [V103_CANDIDATE_SUPPLY_PROMPT_GATE_REPORT.md](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/V98_ABSOLUTE_RUNTIME_PUBLIC_NOTION_SYNC_20260509/evidence/V103_CANDIDATE_SUPPLY_PROMPT_GATE_REPORT.md)
- [V102_RECURRENCE_60D_ANALYSIS_20260509.md](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/V98_ABSOLUTE_RUNTIME_PUBLIC_NOTION_SYNC_20260509/evidence/V102_RECURRENCE_60D_ANALYSIS_20260509.md)
- [V101_SHADOW_RULE_PROMPT_REPORT.md](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/V98_ABSOLUTE_RUNTIME_PUBLIC_NOTION_SYNC_20260509/evidence/V101_SHADOW_RULE_PROMPT_REPORT.md)
- [V100_MASTER_PHASE_TRACKING.md](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/V98_ABSOLUTE_RUNTIME_PUBLIC_NOTION_SYNC_20260509/evidence/V100_MASTER_PHASE_TRACKING.md)
- [LATEST_REPORT.json](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/LATEST_REPORT.json)
- [OPEN_ISSUES.md](https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/OPEN_ISSUES.md)
