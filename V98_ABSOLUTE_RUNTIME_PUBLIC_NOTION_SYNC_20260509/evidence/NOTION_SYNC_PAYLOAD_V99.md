# NOTION SYNC PAYLOAD V99 — Copy vào page `Lottery_AI_Test`

**Generated**: 2026-05-09 12:00 VN  
**Purpose**: FU-170 Notion sync UNVERIFIED — owner copy nội dung này vào Notion `Lottery_AI_Test` HOME nếu MCP chưa khả dụng.

---

## 1. Current truth — Latest version

- **V98.1** (2026-05-09 09:30 VN morning sanity)
- Public commit: `0f29545` (`Lottery_AI_Notion_Reports/main`)
- Private commit: `9326e94` (`Lottery_AI_Test/master`)
- VPS runtime: `ceb36c2` git + scp deploy mode (all V77→V98 deployed via scp; runtime is truth)
- Hash 4 official tables IDENTICAL pre/post all sessions: `predictions=4584 / final_bundles=211 / lottery_results=14634 / model_daily_eval=4493`

## 2. V93 → V98 → V98.1 timeline

| Version | Date VN | Scope | Status |
|---|---|---|---|
| V93 | 2026-05-08 20:30 | MB 56 forensic + 3-càng audit | DELIVERED |
| V93.1 | 2026-05-08 21:00 | P0 shadow audits 3 tables cron 19:16 | DEPLOYED |
| V93.2 | 2026-05-08 21:30 | Sibling stdout fix 6 materializers | DEPLOYED + VERIFIED V98.1 |
| V94 | 2026-05-08 21:45 | Cross-region leakage forensic + D-2 region-gated | DELIVERED |
| V94.1 | 2026-05-08 22:30 | Spillover-aware safe batch 3 shadow surfaces cron 19:18 | DEPLOYED |
| V95 | 2026-05-08 23:15 | Data integrity + AI context audit + UI dashboard cron 19:20 | DEPLOYED |
| V96 | 2026-05-08 23:35 | Master Tracker SSOT + 9-panel dashboard cron 19:22 | DEPLOYED |
| V97 | 2026-05-08 22:50 | SP-4.0 → SP-4.1 prompt fix L159+L161 max 2 numbers | DEPLOYED |
| V97.1 | 2026-05-08 23:58 | Governance commit V93-V97 batch + cron natural-fire validate | DEPLOYED |
| V98 | 2026-05-09 00:50 | Absolute SSOT + monitoring command center 10 panels | DEPLOYED |
| **V98.1** | **2026-05-09 09:30** | **Morning sanity 6/6 cron fired + V97 first live MN BT=05** | **DELIVERED** |
| **V99.1** | **2026-05-09 12:00** | **Truth verify + V98.1 metadata cleanup + exact evaluator** | **THIS PAYLOAD** |

## 3. Resolved FUs (V98 + V98.1 + V99.1)

| FU | Resolution | Verified by |
|---|---|---|
| FU-169 | Public reports stale V92/V74 → fixed V98 | LATEST_REPORT.json now V98.1 |
| FU-176 | /monitoring V98 Command Center | 10 panels live, /api/admin/v98-command-center=401 |
| **FU-172** | **Cron 23:45+ misfire** | **6/6 cron natural-fire 2026-05-08 verified V98.1** |
| **FU-V97.1-CRON-MISFIRE** | **Root cause: APScheduler misfire grace time after fresh restart only** | V98.1 |
| **FU-V97.1-LOG-PERSIST** | **FALSE_NEGATIVE — em misread SQLite UTC CURRENT_TIMESTAMP as VN** | V98.1 probe insert success |
| **FU-171 (V99.1)** | **md5 drift = CRLF (VPS) vs LF (local) line endings ONLY, content byte-identical** | `_quick_diff.py` normalize confirmed |

## 4. Active FUs

| FU | Severity | Title | Decision date |
|---|---|---|---|
| FU-170 | P1 | Notion `Lottery_AI_Test` V93-V97 sync UNVERIFIED | Owner provide MCP/screenshot anytime |
| FU-173 | P1 | Bundle conversion replay 30d evidence | 2026-05-21 14d gate (V99 evaluator ready) |
| FU-174 | P1 | Combo-super BT-first replay | 2026-05-21 14d gate |
| FU-175 | P1 | Prompt context injection dossier per region | 2026-05-21 14d gate |
| FU-V96-AUDIT-3 | P1 | combo_super uses WR not BT | tied to FU-174 |
| FU-V96-AUDIT-4 | P1 | combo_super hardcode 6 AI | tied to FU-174 |

## 5. NEW V99.1 items

### FU-V99-BT-SCORING-DEBATE (P0 OWNER_GATE_REQUIRED)

**Discovery**: V93 forensic + Báo Cáo 15 dùng 2 evaluator semantic khác:
- **Production scoring** = `STRICT_DAC_BIET` (BT khớp ĐB tail only) → MB 2026-05-08 BT=37 vs ĐB=47 → LOSE
- **V93 forensic** = `ANY_PRIZE_LENIENT` (BT khớp bất kỳ giải nào trong 25 unique 2D tails) → 56 ∈ all-prize set (giải ba 19956) → near-WIN

**Proof**: Database query MB 2026-05-08 confirmed:
- Special tail = 47 (Giải Đặc Biệt 29147)
- All 25 unique 2D tails: 05, 11, 13, 16, 25, 42, 44, 46, 47, 52, 56, 60, 61, 62, 71, 72, 74, 77, 79, 82, 84, 85, 87, 93, 94
- 14/27 production AI picked 56 (V93 claim CONFIRMED)

**Decision needed**: Owner muốn giữ STRICT (current) hay shift sang LENIENT (lottery thực tế)?

### FU-V99-GITHUB-TOKEN-LEAK (P0 CRITICAL SECURITY)

**Discovery**: VPS git remote URL chứa GitHub Personal Access Token leaked:
```
origin https://irissnss:ghp_***REDACTED***@github.com/irissnss/Lottery_AI_Test.git
```

**Token prefix observed (private record only)**: `ghp_cvoSP***` (full value not committed publicly)

**Action required**: Owner phải REVOKE token này tại `https://github.com/settings/tokens` ngay.
**Cause**: Token leak in git config — visible to anyone with SSH access to VPS.
**Mitigation post-revoke**: Set VPS remote dùng SSH key hoặc gh auth thay vì PAT inline URL.

### V99 Exact Station-Aware Evaluator (READY)

- Backend `web/backend/_v99_exact_evaluator.py` (~280 lines)
- Shadow table `v99_exact_evaluator_results` (NEW)
- 30d backfill DONE (88 OFFICIAL + 614 test-lane + 9 V67 + 18 V70 + 18 V73 = 747 evaluator rows)
- Supports both STRICT_DAC_BIET + ANY_PRIZE_LENIENT semantic
- Foundation cho FU-173 14d gate 2026-05-21

## 6. 14d evaluator hit rate (V99.1 verified)

| Category | n | strict% | lenient% |
|---|---:|---:|---:|
| OFFICIAL | 42 | 0.0% | 38.1% |
| TEST_LANE | 371 | 0.0% | 35.3% |

**Per region 14d aggregated**:
| Region | n | strict% | lenient% |
|---|---:|---:|---:|
| MB | 169 | 0.0% | 24.9% |
| MN | 122 | 0.0% | 35.2% |
| MT | 122 | 0.0% | 50.8% |

**Top 14d test-lane methods (n≥10)**:
| Method | Region | n | lenient% |
|---|---|---:|---:|
| MN_AI_CHAIN_PRESERVATION_V1 | MN | 15 | 53.3% |
| MT_NO_TOKEN_HERD_REDUCTION_V1 | MT | 15 | 53.3% |
| MT_OFFICIAL_BASELINE_CONTROL | MT | 15 | 53.3% |
| MT_SPECIALIST_ROSTER_V1 | MT | 15 | 53.3% |
| MT_STRENGTH_WEIGHTED_V52_5_2 | MT | 15 | 53.3% |

→ **0% strict (BT đặc biệt) cho ALL methods 14d** = lottery rare event, Wilson CI normal (1/100 chance × 14 days × 3 region = 0.42 expected, 0 observed).
→ **TEST_LANE và OFFICIAL gần bằng nhau** (35.3% vs 38.1% lenient) = test-lane chưa thắng official đáng kể.

## 7. 2026-05-09 cluster (await closeout 19:00 VN)

MN test-lane chia 3 cluster:
- **Cluster 82**: ADAPTIVE_BUDGET / AI_CHAIN / STRENGTH (3 methods)
- **Cluster 05**: NO_TOKEN_HERD / OFFICIAL_BASELINE / SPECIALIST + OFFICIAL = 05
- **Cluster 13**: ADAPTIVE_EXPLOIT / HYBRID + V67/V70/V73

V67/V70/V73 đêm qua đồng thuận **MN=13, MB=37, MT=79**.

## 8. Decision calendar

- 2026-05-09 16:30-18:30 VN: MT/MB cascade lần 1 với SP-4.1 prompt
- 2026-05-09 19:14-22 VN: 5 cron shadow chain (V81/V93.1/V94.1/V95/V96)
- 2026-05-09 23:35-55 VN: V93.2 round 2 cron clean
- 2026-05-12: 4 P0 methods reach 14d sample
- 2026-05-14: V79/V80/V81 7d + MB cold gate + FU-171 review
- **2026-05-21**: 14d full + MN dossier + V99 evaluator metrics + FU-173/174/175 owner gate
- 2026-06-08: 30d sweep FU-162/164/166/167
- 2026-07-06: 60d MB SPECIALIST_ROSTER + V97 prompt eval

## 9. Hard locks honored (V98 + V98.1 + V99.1)

- ✅ ZERO official mutation across 11 sessions
- ✅ NO production scoring/selector/prompt change beyond V97 SP-4.1 (text only)
- ✅ NO promote/rollback button
- ✅ NO MB 56 production "fix" until owner gate FU-V99-BT-SCORING-DEBATE
- ✅ V99 evaluator shadow_only=1, output_eligible=0
- ✅ All admin routes 401-locked verified (health=200, du-doan=200, monitoring=401, v98=401)

## 10. Public links

- **Public LATEST**: https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/LATEST_REPORT.json
- **V98 REPORT**: https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/V98_ABSOLUTE_RUNTIME_PUBLIC_NOTION_SYNC_20260509/V98_REPORT.md
- **V98.1 morning sanity**: https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/V98_ABSOLUTE_RUNTIME_PUBLIC_NOTION_SYNC_20260509/evidence/v98_1_morning_sanity_check.md
- **V99 hit rate**: https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/V98_ABSOLUTE_RUNTIME_PUBLIC_NOTION_SYNC_20260509/evidence/L5_hit_rate_report.md
- **MB 56 truth**: https://raw.githubusercontent.com/irissnss/Lottery_AI_Notion_Reports/main/V98_ABSOLUTE_RUNTIME_PUBLIC_NOTION_SYNC_20260509/evidence/L4_mb_56_truth_table.md

## 11. Owner immediate action items

1. **CRITICAL**: REVOKE GitHub PAT `ghp_cvoSPkk5...PAnY` tại github.com/settings/tokens
2. **OWNER GATE**: Decide FU-V99-BT-SCORING-DEBATE (STRICT vs LENIENT)
3. **OPTIONAL**: Provide Notion MCP access trong session sau để FU-170 đóng

---

End of payload. Owner copy nội dung này vào Notion `Lottery_AI_Test` HOME page nếu cần.
