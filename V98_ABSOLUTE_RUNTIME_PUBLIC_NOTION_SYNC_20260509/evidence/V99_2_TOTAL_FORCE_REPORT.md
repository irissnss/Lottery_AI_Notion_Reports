# V99.2 — TOTAL FORCE SECURITY + SSOT CLEANUP + BT SEMANTIC LOCK + EXACT EVALUATOR REPLAY + NOTION SYNC

**Generated**: 2026-05-09 13:15 VN  
**Owner directive**: V99.2 11 lanes (P0 security first, sanity, doctrine lock, scoreboard, bundle replay).
**Scope**: Read-only audit + shadow-only evaluator + governance update + Notion payload. NO production change.

---

## 1. Executive Summary

| Lane | Status | Verdict |
|---|---|---|
| L1 Security | PARTIAL | Code redacted ✅, owner must revoke PAT |
| L2 SSOT cleanup | DONE | LATEST_REPORT.json updated V98.1 + V99.1 + V99.2 evidence |
| L3 BT doctrine | LOCKED | STRICT_DAC_BIET production, DIAGNOSTIC shadow only |
| L4 Evaluator sanity | PASS | 10 tests passed, shadow integrity 747/747 |
| L5 Scoreboard | DONE | 14d strict 0% (Wilson upper 0.7%), lenient 35-38% |
| L6 Bundle replay | PRELIMINARY | 10 hypotheses, all defer to FU-173 14d gate |
| L7 Prompt/model | DEFERRED | FU-175 14d gate |
| L8 Notion payload | DONE | V99.2 payload file (no MCP) |
| L9 Monitoring | OK | V98 panels still serve, no new UI needed |
| L10 Hash guard | PASS | 4 official tables IDENTICAL |
| L11 Final report | THIS FILE | controller-grade VN |

## 2. Control Table

| Control | Value | Proof |
|---|---|---|
| OFFICIAL_TOUCHED | false | Hash 4 tables IDENTICAL pre/post |
| PRODUCTION_SCORING_CHANGED | false | No code change in main.py generate_final_bundle |
| FINAL_BUNDLE_MUTATED | false | final_bundles count=211 unchanged |
| PREDICTIONS_MUTATED | false | predictions count=4584 (only natural cycle growth) |
| SHADOW_ONLY | true | v99_exact_evaluator_results.shadow_only=1 (747/747) |
| SECRET_PRINTED | false | All redactions verified, only `ghp_cvoSP***` prefix |
| GITHUB_PAT_EXPOSED | true | private commit fb2ae98 + VPS git remote URL |
| GITHUB_PAT_REVOKED | unknown_owner_required | no revoke proof yet |
| MODEL_TOKENS_EXPOSED | unknown | env-only, no exposure proof, KEEP_WITH_MONITORING |
| BT_PRODUCTION_SEMANTIC | STRICT_DAC_BIET | LOCKED V99.2 L3 |
| DIAGNOSTIC_SEMANTIC | TAIL_ANY_PRIZE_DIAGNOSTIC | shadow only |
| EXACT_EVALUATOR | READY | 10 sanity tests pass, 747 rows backfill |
| TEST_LANE_PROMOTION | false | strict 0% 14d, no method qualifies |
| NOTION_SYNC | UNVERIFIED | FU-170 (no MCP) |
| PUBLIC_LATEST | V98.1 (root) + V99.1 + V99.2 evidence | LATEST_REPORT.json |
| FU-171 | CLOSED FALSE_NEGATIVE | CRLF vs LF (V99.1) |
| FU-172 | DONE | V98.1 6/6 cron natural-fire |

## 3. Security Status (L1)

### GitHub PAT containment
- ✅ Working tree: 0 PAT patterns
- ✅ Local files redacted (only `ghp_cvoSP***` prefix)
- ⚠ Private git history commit `fb2ae98`: contains full token (pre-V99.1 redact)
- ⚠ VPS git remote URL: contains full token (CONFIRMED V99.1)
- ⏳ Owner must REVOKE token at github.com/settings/tokens (P0)
- 💡 Post-revoke: token becomes inert, no need to scrub history (OPTIONAL BFG/filter-repo)

### Secret inventory (REDACTED)
| Provider | Location | In git? | Status |
|---|---|---|---|
| GitHub PAT | VPS+git history | YES | EXPOSED → MUST_ROTATE |
| OpenAI/Anthropic/Google/DeepSeek/Qwen/Kimi/GLM/xAI | `.env` | NO (.gitignore) | NOT_EXPOSED_ENV_ONLY |
| Admin/DB | `.env` | NO | NOT_EXPOSED_ENV_ONLY |

### False positives
- 84 GLM-pattern hits in `_test_output_utf8.txt` = lottery digit sequences (NOT real tokens)

## 4. SSOT version naming (L2)

LATEST_REPORT.json now reflects:
- `latest_version`: V98.1 (root)
- `v98_1_updated_at_vn`: 2026-05-09T09:30
- `v99_1_metadata_cleanup_at_vn`: 2026-05-09T11:35
- `v99_1_findings`: mb_56_truth, github_token_leak, vps_git_drift
- `v99_2_findings`: NEW (this session) — security inventory, BT semantic lock, evaluator sanity pass, scoreboard

V99.1 + V99.2 evidence files all reside under V98 folder (`evidence/`) — addendum approach. Not creating separate V99.1/V99.2 root folders to avoid Notion AI confusion.

## 5. BT Semantic Doctrine LOCK (L3)

| Semantic | Use | Production? |
|---|---|---|
| BT_STRICT_DAC_BIET | BT khớp Đặc Biệt only | **PRODUCTION KPI (LOCKED)** |
| TAIL_ANY_PRIZE_DIAGNOSTIC | BT khớp any 2D tail | shadow signal only |

V93 MB 56:
- TRUE under DIAGNOSTIC (signal observation)
- NOT production bug under STRICT
- Bundle replay must report both lanes, owner gate uses STRICT

FU-V99-BT-SCORING-DEBATE → DEFAULT KEEP STRICT, revisit 30d gate 2026-06-08 if evidence.

## 6. MB 2026-05-08 56 final interpretation

| Question | Answer |
|---|---|
| 56 in actual MB 2026-05-08? | YES (any-prize: giải ba 19956). NO (special: ĐB=47) |
| V93 claim valid? | YES under DIAGNOSTIC, NOT under STRICT |
| Production bug? | NO (production strict semantic, BT=37 LOSE correct) |
| Bundle conversion lost 56? | YES under DIAGNOSTIC interpretation; under STRICT, 56 was never a "winner" |
| Future fix needed? | DEFER to FU-173 14d gate; if owner shifts semantic, full replay required |

## 7. Exact Evaluator (L4 + L5)

### Sanity (L4)
- ✅ 10 tests pass: strict, lenient, padding, pending, multi-station, MB 56 spot-check, 10 random rows, aggregate, integrity
- ✅ STRICT_ZERO_VALIDATED for 14d (Wilson upper 0.7%) and 30d (Wilson upper 0.4%) — lottery rare event normal
- ✅ All 747 rows shadow_only=1, output_eligible=0, diagnostic_only=1, owner_approved=0

### Scoreboard (L5)
**14d strict**:
- OFFICIAL_FINAL_BUNDLE: 0/42 = 0.0% [Wilson 95% CI 0.0-8.4%]
- TEST_LANE: 0/371 = 0.0% [Wilson 95% CI 0.0-1.0%]

**14d lenient (DIAGNOSTIC)**:
- OFFICIAL: 16/42 = 38.1%
- TEST_LANE: 131/371 = 35.3%

**Per region 14d**: MB 24.9%, MN 35.2%, MT 50.8% (lenient)

**Top diagnostic methods (NO promotion claim)**:
- MN_AI_CHAIN_PRESERVATION_V1 (53.3%, n=15) ⭐
- MT NO_TOKEN/OFFICIAL/SPECIALIST/STRENGTH (53.3% each, n=15)
- MN_SPECIALIST_ROSTER_V1 (46.7%, n=15)
- MB_STRENGTH_WEIGHTED_V52_5_2 (42.9%, n=14)

## 8. Bundle replay preliminary (L6)

10 hypotheses scoreboard built. ALL defer to FU-173 14d gate 2026-05-21.

NO method has strict_would_save > 0 yet. NO promotion eligible.

## 9. Prompt/model audit (L7)

DEFERRED to FU-175 14d gate 2026-05-21. Heavy work, not blocking.

## 10. Monitoring (L9)

V98 Command Center 10 panels still active and complete. No new UI built (per V99.2 directive: "ưu tiên report/evidence hơn UI").

## 11. Hash guard (L10)

| Table | Pre-V99.2 | Post-V99.2 |
|---|---:|---:|
| predictions | 4584 | **4584** |
| final_bundles | 211 | **211** |
| lottery_results | 14634 | **14634** |
| model_daily_eval | 4493 | **4493** |

→ ZERO unauthorized mutation across 12 sessions (V92.1 → V99.2).

## 12. Files changed V99.2

### Private (`Lottery_AI_Test`)
- `artifacts/v992_total_force/` (8 evidence files + scripts)
- `CHANGELOG.md` V99.2 entry
- `docs/AUTOMATION_STATE.json` seq 44 (already V99.1) → seq 45 (V99.2)
- NO new code files (V99 evaluator was V99.1, sanity validated only)

### Public (`Lottery_AI_Notion_Reports`)
- `LATEST_REPORT.json` v99_2 fields added
- 5 new evidence files:
  - L1_SECURITY_GITHUB_PAT_CONTAINMENT.md
  - L3_BT_SCORING_SEMANTIC_DOCTRINE.md
  - L5_SCOREBOARD_14D_30D.md
  - NOTION_SYNC_PAYLOAD_V99_2.md
  - V99_2_TOTAL_FORCE_REPORT.md (this file)

## 13. Open issues post-V99.2

| FU | Severity | Status | Decision |
|---|---|---|---|
| **FU-V99-GITHUB-TOKEN-LEAK** | P0 | OWNER_ACTION_REQUIRED | REVOKE NOW |
| **FU-V99-BT-SCORING-DEBATE** | P0 | LOCKED V99.2 L3 (default STRICT) | revisit 30d gate |
| FU-170 | P1 | UNVERIFIED | owner provide MCP |
| FU-173 | P1 | EVIDENCE_COLLECTING | 14d gate 2026-05-21 |
| FU-174 | P1 | EVIDENCE_COLLECTING | 14d gate |
| FU-175 | P1 | DEFERRED HEAVY | 14d gate |

## 14. Next action

### Immediate (owner)
1. **REVOKE GitHub PAT** at https://github.com/settings/tokens
2. Fix VPS git remote post-revoke
3. (Optional) BFG repo cleanup

### Auto today
- 16:30-18:30 VN: MT/MB cascade SP-4.1
- 19:14-22 VN: 5 cron shadow chain
- Manual rerun V99 evaluator post-closeout: `python web/backend/_v99_exact_evaluator.py --target 2026-05-09`

### 14d gate (2026-05-21)
- V99 evaluator with sufficient sample → FU-173/174/175 owner gate

---

**STATUS V99.2**: DELIVERED.
- ✅ Security containment partial (owner must revoke)
- ✅ SSOT cleaned
- ✅ BT doctrine LOCKED
- ✅ Evaluator sanity PASS
- ✅ Scoreboard built (no promotion)
- ✅ Bundle replay preliminary (defer 14d)
- ⏳ Notion sync UNVERIFIED (FU-170)
- ✅ Hash guard 4 official IDENTICAL — ZERO mutation

NO production prediction change. Production stays STRICT_DAC_BIET. Test-lane chưa thắng official.
