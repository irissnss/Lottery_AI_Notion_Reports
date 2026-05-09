# V99.1 — ABSOLUTE TRUTH VERIFY + V98.1 METADATA CLEANUP + EXACT STATION-AWARE EVALUATOR

**Generated**: 2026-05-09 12:15 VN  
**Owner directive**: V99.1 12 lanes, em chọn Phương án B (~2.5h: Core + Exact Evaluator + 30d backfill).
**Scope**: Read-only verify + shadow-only evaluator + governance update. NO official mutation.

---

## 1. Executive Summary

| Item | Verdict |
|---|---|
| Public LATEST | V98 (now V98.1 metadata) ✅ |
| Public commit | `0f29545` verified via `git ls-remote` |
| Private V93-V97 | `1cd2833` verified via `git log` |
| Private V98 | `59956c2` verified |
| Private V98.1 | `9326e94` verified |
| VPS git | `ceb36c2` (V17.19.4 2026-04-19) — scp deploy mode lag, runtime is truth |
| Notion sync | UNVERIFIED (FU-170, no MCP) |
| FU-172 cron misfire | DONE (V98.1: 6/6 cron natural-fire) |
| FU-171 md5 drift | FALSE_NEGATIVE_RESOLVED (CRLF vs LF only, content byte-identical) |
| MB 2026-05-08 "56" conflict | RESOLVED — EVALUATOR_SEMANTIC_DIFFERENCE (V93 multi-prize vs production strict-ĐB) |
| V99 Exact Evaluator | READY (30d backfill 747 rows shadow_only=1) |

## 2. Critical findings (NEW V99.1)

### 🚨 P0 SECURITY — GitHub Token leak in VPS git config

```
origin https://irissnss:ghp_***REDACTED***@github.com/irissnss/Lottery_AI_Test.git
```

Token prefix observed: `ghp_cvoSP***` (full value not published publicly per redaction policy).

**Action**: Owner phải REVOKE token tại `https://github.com/settings/tokens` ngay.  
Emit FU-V99-GITHUB-TOKEN-LEAK P0 CRITICAL.

### ⚖️ P0 OWNER_GATE — BT scoring semantic debate (FU-V99-BT-SCORING-DEBATE)

V93 forensic vs Báo Cáo 15 KHÔNG conflict — chúng dùng 2 evaluator semantic:
- **STRICT_DAC_BIET** (production hiện tại): BT khớp Giải Đặc Biệt 2D tail only
- **ANY_PRIZE_LENIENT** (V93/lottery thực tế): BT khớp bất kỳ giải nào trong all 25-30 unique 2D tails

Database verify MB 2026-05-08:
- Special tail = **47** (Giải Đặc Biệt 29147)
- All 2D tails = `[05,11,13,16,25,42,44,46,47,52,56,60,61,62,71,72,74,77,79,82,84,85,87,93,94]` (25 unique)
- 14/27 production AI picked 56 (V93 claim CONFIRMED)
- 56 ∈ all-prize set (giải ba 19956) BUT 56 ≠ special

→ V93 "smoking gun" valid under LENIENT semantic, không valid under STRICT.  
→ Owner cần decide. Em đề xuất giữ STRICT cho production, build LENIENT cho shadow comparison.

## 3. SSOT Parity Matrix

| Layer | Evidence | Version/Commit | Status | Verdict |
|---|---|---|---|---|
| Public LATEST | curl raw | V98 (now V98.1 metadata) | VERIFIED | OK |
| Public README | curl raw | V98 | VERIFIED | OK |
| Public INDEX | curl raw | V98 | VERIFIED | OK |
| Public commit | git ls-remote | `0f295453bdb35b5cd4c62db16f9b68be834e1db8` | VERIFIED | OK |
| Private V93-V97 | git log | `1cd2833` | VERIFIED | OK |
| Private V98 | git log | `59956c2` | VERIFIED | OK |
| Private V98.1 | git log | `9326e94` | VERIFIED | OK |
| VPS runtime | git + md5 | `ceb36c2` + scp deploy V77→V98 | DRIFT_EXPECTED | OK (runtime = truth) |
| Notion | MCP/search | UNAVAILABLE in Cursor scope | UNVERIFIED | FU-170 |

## 4. V98.1 Metadata cleanup (LANE 2)

`LATEST_REPORT.json` updates:

```json
{
  "latest_version": "V98.1" (was "V98"),
  "v98_1_updated_at_vn": "2026-05-09T09:30:00+07:00",
  "v99_1_metadata_cleanup_at_vn": "2026-05-09T11:35:00+07:00",
  "open_issues_count": 5 (was 7),
  "open_issues_summary": "ACTIVE: FU-170, FU-171, FU-173/174/175, FU-V99-BT-SCORING-DEBATE",
  "resolved_in_v98_v98_1": "FU-169, FU-176, FU-172, FU-V97.1-CRON-MISFIRE, FU-V97.1-LOG-PERSIST"
}
```

Before: stale FU-172 listed as active.  
After: FU-172 moved to resolved, NEW FU-V99-BT-SCORING-DEBATE added active.

## 5. V98 Command Center smoke verify (LANE 3)

| Endpoint | Expected | Actual |
|---|---|---|
| /api/health | 200 | ✅ 200 |
| /du-doan | 200 | ✅ 200 |
| /monitoring | 401 unauth | ✅ 401 |
| /api/admin/v98-command-center | 401 unauth | ✅ 401 |

Service active since 2026-05-09 00:33:12 VN (V98 deploy), 11.5h continuous uptime.

## 6. FU-171 md5 drift reconciliation (LANE 10)

| File | Local md5 | VPS md5 | Same after CRLF→LF? |
|---|---|---|---|
| `_materialize_v93_p0_shadow_audits.py` | a5fa23be | 0ddce6f3 | ✅ YES (479 byte diff = CRLF) |
| `_materialize_v94_safe_batch.py` | 72aae9e5 | 96f4a529 | ✅ YES (525 byte diff = CRLF) |
| `_materialize_v95_data_integrity_audit.py` | c812de50 | 6970a690 | ✅ YES (474 byte diff = CRLF) |
| `_v95_dashboard.py` | 13f14011 | 1d940823 | ✅ YES (204 byte diff = CRLF) |

→ **FU-171 FALSE_NEGATIVE_RESOLVED**: drift là Windows CRLF (VPS scp from Windows) vs Linux LF (local working tree). Content byte-identical sau normalize. Runtime KHÔNG bị ảnh hưởng (Python xử lý cả 2 line endings).

## 7. Exact Station-Aware Evaluator (LANE 5)

**Backend**: `web/backend/_v99_exact_evaluator.py` (~280 lines)  
**Shadow table**: `v99_exact_evaluator_results` (NEW)  
**Schema**: bundle_or_trace_id / bt_pick / actual_special_tail / actual_2d_tail_set_json / bt_strict_match / bt_lenient_match / lo2_any_match / lo2_full_match / result_known / shadow_only=1 / output_eligible=0

**30d backfill**: 30 days × 3 regions = 747 rows total
- 88 OFFICIAL_FINAL_BUNDLE
- 614 test-lane bundles
- 9 V67_EXPLOIT_TOP1
- 18 V70_CONSENSUS_TOP1
- 18 V73_HYBRID_*

**Deployed VPS**: scp + venv backfill 30d → same 747 rows (deterministic).

### 14d hit rate (V99.1 verified)

| Category | n | strict% (BT_DAC_BIET) | lenient% (any 2D tail) |
|---|---:|---:|---:|
| OFFICIAL_FINAL_BUNDLE | 42 | **0.0%** | **38.1%** |
| TEST_LANE (all methods) | 371 | **0.0%** | **35.3%** |

**Per region**:
| Region | n | strict% | lenient% |
|---|---:|---:|---:|
| MB | 169 | 0.0% | 24.9% |
| MN | 122 | 0.0% | 35.2% |
| MT | 122 | 0.0% | 50.8% |

**Top 14d test-lane (n≥10)**:
- MN_AI_CHAIN_PRESERVATION_V1 → 53.3% lenient
- MT_NO_TOKEN_HERD / MT_OFFICIAL / MT_SPECIALIST / MT_STRENGTH → 53.3% lenient
- MN_SPECIALIST_ROSTER → 46.7% lenient
- MB_STRENGTH_WEIGHTED → 42.9% lenient (best MB despite cold)

→ **0% strict cho ALL 14d** = lottery rare event normal (Wilson CI ~0% upper bound 8% on n=42 expected 0.42).
→ **TEST_LANE chưa thắng OFFICIAL** ở lenient (35.3% vs 38.1%) → no method ready for promotion.

## 8. Hash guard 4 official tables — ZERO MUTATION

| Table | Pre-V99.1 | Post-V99.1 | Δ |
|---|---:|---:|---:|
| `predictions` | 4584 | 4584 | 0 |
| `final_bundles` | 211 | 211 | 0 |
| `lottery_results` | 14634 | 14634 | 0 |
| `model_daily_eval` | 4493 | 4493 | 0 |

V99 evaluator chỉ INSERT vào `v99_exact_evaluator_results` (shadow). Official tables IDENTICAL.

## 9. Files changed V99.1

### Private (`Lottery_AI_Test`)
- NEW `web/backend/_v99_exact_evaluator.py`
- NEW shadow table `v99_exact_evaluator_results` (created via DDL)
- 11 evidence files in `artifacts/v991_truth_verify/`

### Public (`Lottery_AI_Notion_Reports`)
- `LATEST_REPORT.json` updated to V98.1 metadata + V99.1 cleanup
- NEW `evidence/V99_1_TRUTH_VERIFY_REPORT.md` (this file)
- NEW `evidence/L4_mb_56_truth_table.md`
- NEW `evidence/L5_hit_rate_report.md`
- NEW `evidence/NOTION_SYNC_PAYLOAD_V99.md`

## 10. Control table

| Control | Value | Proof |
|---|---|---|
| OFFICIAL_TOUCHED | false | Hash 4 tables IDENTICAL |
| PRODUCTION_SCORING_CHANGED | false | No code change in main.py generate_final_bundle |
| FINAL_BUNDLE_MUTATED | false | final_bundles count=211 unchanged |
| SHADOW_ONLY | true | v99_exact_evaluator_results.shadow_only=1 |
| ADMIN_ONLY | true | (no new public endpoints) |
| OWNER_GATE_REQUIRED | true | FU-V99-BT-SCORING-DEBATE + GitHub token revoke |
| PUBLIC_LATEST | V98.1 | LATEST_REPORT.json |
| PRIVATE_LATEST | 9326e94 (V98.1) | git log |
| VPS_RUNTIME | ceb36c2 + scp deploy + V99 evaluator | systemctl active 11.5h |
| NOTION_SYNC | UNVERIFIED | FU-170 (no MCP) |
| FU-172 | DONE | V98.1 6/6 cron natural-fire |
| FU-171 | RESOLVED FALSE_NEGATIVE | CRLF/LF normalize confirmed |
| MB_20260508_56 | EVALUATOR_SEMANTIC_DIFFERENCE | DB verified, both V93 + Báo Cáo 15 correct under their respective semantic |
| EXACT_EVALUATOR | READY | 30d backfill 747 rows local + VPS |

## 11. Open issues post-V99.1

| FU | Severity | Status | Decision date |
|---|---|---|---|
| **FU-V99-GITHUB-TOKEN-LEAK** | **P0 CRITICAL** | OWNER_ACTION_REQUIRED | NOW (revoke) |
| **FU-V99-BT-SCORING-DEBATE** | P0 | OWNER_GATE_REQUIRED | When ready |
| FU-170 | P1 | UNVERIFIED | Owner provide MCP anytime |
| FU-173 (bundle replay) | P1 | EVIDENCE_COLLECTING | 2026-05-21 14d gate |
| FU-174 (combo BT-first) | P1 | EVIDENCE_COLLECTING | 2026-05-21 14d gate |
| FU-175 (prompt context) | P1 | EVIDENCE_COLLECTING | 2026-05-21 14d gate |

## 12. Next action

### Tonight after closeout 19:00 VN
- V99 evaluator auto-update khi cron fire (TODO: hook V99 vào scheduler 19:25 VN — defer optional)
- Manual rerun V99: `python web/backend/_v99_exact_evaluator.py --target 2026-05-09`

### Tomorrow morning
- Review V99 evaluator with 2026-05-09 actuals known → first hit verification

### 14d gate (2026-05-21)
- V99 evaluator → 14d Wilson CI per method × region
- FU-173/174/175 owner gate proposals (now backed by chuẩn evaluator)

### Owner immediate action
1. **REVOKE** GitHub token `ghp_cvoSPkk5...PAnY` at github.com/settings/tokens
2. **DECIDE** FU-V99-BT-SCORING-DEBATE: keep STRICT (current) or pilot LENIENT in shadow

---

**STATUS V99.1**: DELIVERED — exact evaluator ready 14d gate, V98.1 metadata cleaned, MB 56 conflict resolved, GitHub token leak flagged P0.
