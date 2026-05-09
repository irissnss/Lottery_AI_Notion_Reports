# NOTION SYNC PAYLOAD V99.2 — Copy vào page `Lottery_AI_Test`

**Generated**: 2026-05-09 13:10 VN  
**Purpose**: FU-170 still UNVERIFIED. Owner copy nội dung này vào Notion `Lottery_AI_Test` HOME nếu MCP chưa khả dụng.

---

## 1. Current truth (V99.2)

| Surface | Identifier | Status |
|---|---|---|
| Public latest | `LATEST_REPORT.json.latest_version=V98.1` + V99.1 + V99.2 evidence | ACTIVE |
| Public commit | `74cab5b` then `+V99.2 commit (this session)` | UPDATED |
| Private commit | `bfea15d` (V99.1 redact) → `+V99.2 commit (this session)` | UPDATED |
| VPS runtime | `ceb36c2` git + scp deploy mode + V99 evaluator deployed | ACTIVE |
| Notion `Lottery_AI_Test` | UNVERIFIED — no MCP in Cursor scope | FU-170 |
| Hash 4 official tables | predictions=4584 / final_bundles=211 / lottery_results=14634 / model_daily_eval=4493 | IDENTICAL |

## 2. V99.2 deliverables

### Security (LANE 1)
- ✅ Working tree scan: 0 GitHub PAT classic, 0 OpenAI/xAI/OpenRouter
- ✅ False positives identified (lottery digit sequences in `_test_output_utf8.txt`)
- ✅ Real secrets in `.env` files protected by `.gitignore` (NOT tracked)
- ⚠ GitHub PAT in private git history commit `fb2ae98` + VPS git remote URL → **OWNER MUST REVOKE**
- ⚠ AI provider keys env-only, no exposure proof, KEEP_WITH_MONITORING

### BT scoring doctrine LOCK (LANE 3)
- **STRICT_DAC_BIET** = production KPI (UNCHANGED)
- **TAIL_ANY_PRIZE_DIAGNOSTIC** = shadow signal quality only
- V93 MB 56 = valid under DIAGNOSTIC, NOT production bug under STRICT
- FU-V99-BT-SCORING-DEBATE → DEFAULT KEEP STRICT (revisit at 30d gate 2026-06-08 if evidence)

### Evaluator sanity (LANE 4)
- ✅ 10 sanity tests PASS (synthetic + spot-check + multi-station + padding)
- ✅ STRICT_ZERO_VALIDATED 14d/30d (Wilson 95% upper bound 0.4-0.7% — lottery rare event normal)
- ✅ Shadow integrity 747/747 rows: shadow_only=1, output_eligible=0, diagnostic_only=1, owner_approved=0

### Scoreboard 14d/30d (LANE 5)
- 14d strict: OFFICIAL 0.0% (n=42), TEST_LANE 0.0% (n=371)
- 14d lenient: OFFICIAL 38.1%, TEST_LANE 35.3%
- Per region: MB 24.9%, MN 35.2%, MT 50.8% (all lenient)
- **NO promotion** — strict 0% across all methods

### Bundle replay preliminary (LANE 6)
- 10 hypotheses scoreboard built (preliminary)
- All defer to FU-173/174 14d gate 2026-05-21
- Watchlist 8 methods (DIAGNOSTIC only, no promotion)

## 3. Open FUs (V99.2)

| FU | Severity | Title | Decision date |
|---|---|---|---|
| FU-V99-GITHUB-TOKEN-LEAK | **P0** | GitHub PAT exposed VPS+git history | OWNER REVOKE NOW |
| FU-V99-BT-SCORING-DEBATE | P0 | STRICT vs LENIENT doctrine | LOCKED to STRICT (V99.2 L3) |
| FU-170 | P1 | Notion sync UNVERIFIED | owner provide MCP/screenshot |
| FU-173 | P1 | Bundle conversion replay 30d | 2026-05-21 14d gate |
| FU-174 | P1 | Combo-super BT-first / WR | 2026-05-21 14d gate |
| FU-175 | P1 | Prompt context dossier | 2026-05-21 14d gate |
| FU-V96-AUDIT-3/4 | P1 | combo_super uses WR + hardcode 6 AI | tied to FU-174 |

## 4. Resolved FUs (V98 + V98.1 + V99.1 + V99.2)

| FU | Resolution date |
|---|---|
| FU-169 public stale | V98 |
| FU-176 monitoring command center | V98 |
| FU-172 cron misfire | V98.1 (6/6 cron natural-fire verified) |
| FU-V97.1-CRON-MISFIRE | V98.1 |
| FU-V97.1-LOG-PERSIST | V98.1 (FALSE_NEGATIVE — UTC vs VN tz) |
| FU-171 md5 drift | V99.1 (FALSE_NEGATIVE — CRLF vs LF only) |

## 5. Decision calendar

- 2026-05-09 16:30-18:30 VN: MT/MB cascade với SP-4.1 (V99 evaluator auto-evaluate post-closeout)
- 2026-05-09 19:14-22 VN: 5 cron shadow chain
- 2026-05-09 23:35-55 VN: V93.2 cron round 2
- 2026-05-12: 4 P0 methods 14d sample
- 2026-05-14: V79/V80/V81 7d + MB cold gate
- **2026-05-21**: 14d full gate FU-173/174/175 (V99 evaluator backed)
- 2026-06-08: 30d sweep + FU-V99-BT-SCORING-DEBATE re-evaluation
- 2026-07-06: 60d MB SPECIALIST_ROSTER

## 6. Hard locks honored (V99.2)

- ✅ ZERO official mutation across 12 sessions (V92.1 → V99.2)
- ✅ NO production scoring change beyond V97 SP-4.1
- ✅ NO promote/rollback button
- ✅ NO BT semantic shift (production stays STRICT)
- ✅ V99 evaluator + 30d backfill = shadow_only=1
- ✅ Admin routes 401-locked
- ✅ All secrets redacted in commits

## 7. Public links

- Public LATEST: https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/LATEST_REPORT.json
- V98 base: V98_ABSOLUTE_RUNTIME_PUBLIC_NOTION_SYNC_20260509/V98_REPORT.md
- V98.1 morning: evidence/v98_1_morning_sanity_check.md
- V99.1 truth verify: evidence/V99_1_TRUTH_VERIFY_REPORT.md
- V99.2 L1 security: evidence/L1_SECURITY_GITHUB_PAT_CONTAINMENT.md (this session)
- V99.2 L3 doctrine: evidence/L3_BT_SCORING_SEMANTIC_DOCTRINE.md
- V99.2 L5 scoreboard: evidence/L5_SCOREBOARD_14D_30D.md
- V99.2 final: evidence/V99_2_TOTAL_FORCE_REPORT.md (TBD this session)

## 8. Owner immediate action (P0)

1. **REVOKE GitHub PAT** at https://github.com/settings/tokens — IMMEDIATE
2. After revoke, set VPS git remote without inline PAT (SSH key OR `gh auth login`)
3. (OPTIONAL) BFG repo-cleaner for git history hygiene
4. Provide Notion MCP access trong session sau để FU-170 đóng

---

End of payload. Owner copy nội dung này vào Notion `Lottery_AI_Test` HOME page.
