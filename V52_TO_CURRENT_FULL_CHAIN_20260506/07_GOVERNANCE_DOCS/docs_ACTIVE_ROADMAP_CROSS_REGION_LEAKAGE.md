# ACTIVE ROADMAP — Cross-Region Leakage & Structural Herding Initiative

> **Owner:** anh
> **Created:** 2026-05-01 19:50 UTC+7 (V20.3.37.31)
> **Source:** FU-073 + V20.3.37.30 audit `artifacts/phase_checkpoints/TOTAL_FORCE_CROSS_REGION_LEAKAGE_AUDIT_20260501.md`
> **Status:** ACTIVE — chưa hoàn thành
>
> ⚠ **MANDATORY READ AT SESSION START** ⚠
> Bất kỳ session nào (em hoặc AI khác) mở lên trong dự án Lottery_AI_Test mà:
> - FU-073 còn status `MEASURED_BUT_NOT_FIXED` HOẶC
> - File này chưa có dòng `STATUS: COMPLETED` ở cuối
>
> → BẮT BUỘC đọc file này TRƯỚC khi reply câu hỏi của owner.
> → BẮT BUỘC check ngày hiện tại với cột `Deadline` trong checkpoint table bên dưới.
> → BẮT BUỘC surface item OVERDUE lên đầu reply, không được lờ đi.
>
> Tham chiếu enforcement: `.cursor/rules/active-roadmap-precedence.mdc`

---

## 0. PURPOSE (vì sao file này tồn tại)

Owner đã nhiều lần frustrated vì hệ thống "block không có điểm dừng" — vấn đề `WAIT_LIVE` mãi không có ai tự nhắc, không có deadline cứng. File này khắc phục bằng cách:

1. **Liệt kê tất cả checkpoint** của initiative cross-region leakage với deadline cứng
2. **Auto-action khi quá hạn** — agent tiếp theo PHẢI surface, không được im lặng
3. **Owner-decision-required-by** rõ ràng — nếu owner chưa OK trong N ngày, agent escalate

→ File này là "lương tâm" của initiative: nó không cho ai quên, kể cả khi switch agent / pause project nhiều ngày.

---

## 1. ROOT-CAUSE TÓM TẮT (anh đọc lại sau N ngày để recall)

Hiện tượng: predictions trật ở MN/MT thường ra ở MT/MB cùng ngày (ví dụ MN `17` → MT, MT `46` → MB).

Forensic 30 ngày + 14 ngày confirm:
- Bundle leak `MN→MT BT = 53.3%` vs random baseline `35.3%` (+18 pp)
- Same-model cross-region duplication `17-20%` vs random `~4%` (4-5x baseline)
- AI / NO_TOKEN / SHADOW family **đều** leak 36-47% → **không phải bug 1 lane**
- Universe coverage `14-20%` per region per day → **no lift over random**
- Tất cả 7 output policy đều output `bt=16` cho MT today → output layer không cứu được

Root-cause: **shared-context cross-region herding** + **bundle aggregation amplifies herd over dispersed correct signal**.

---

## 2. CHECKPOINT TABLE (đây là phần quan trọng nhất)

### Cách đọc cột `Auto-action`:
- 🟢 OK = đúng tiến độ, không cần làm gì
- 🟡 NEAR = trong vòng 1 ngày tới deadline → agent NHẮC nhẹ ở cuối reply
- 🔴 OVERDUE = quá hạn → agent BẮT BUỘC đưa lên ĐẦU reply, không bỏ qua
- ⚫ ESCALATE = quá hạn 7+ ngày → status FU-073 nâng lên `BLOCKED`, owner được nhắc 1-page reminder

| ID | Item | Earliest start | Hard Deadline | Owner OK by | Status | Actor | Auto-action threshold |
|---|---|---|---|---|---|---|---|
| **CP-1.1** | TIER 1 measurement surfaces local complete (V20.3.37.33) | 2026-05-02 | 2026-05-04 | 2026-05-04 | 🟢 LOCAL_COMPLETE → SUPERSEDED_BY_CP-1.2 | agent | done |
| **CP-1.2** | **DEPLOYED 2026-05-02 V20.3.37.36 Phase A**: 5 measurement-only materializer files pushed to VPS; 5 NEW tables persistent (cross_region_spillover_shadow 9577 rows, model_cross_region_dup_shadow 640, bundle_universe_coverage_shadow 93, mb_structural_drilldown_shadow 61, tier2_replay_shadow 180); service active V20.3.36; source hash 4/5 IDENTICAL | After CP-1.1 | 2026-05-04 | 2026-05-02 | 🟢 **VPS_DEPLOYED_PERSISTENT** | agent | done |
| **CP-1.3** | Backfill 30d historical for 3 new tables (V20.3.37.41 reconciliation): all 5 tables now backfilled on VPS to 30-60d (cross_region_spillover 60d, model_cross_region_dup 29d, bundle_universe_coverage 30d, mb_structural_drilldown 60d, tier2_replay 14d). Plus V37 added 3 more tables backfilled 30d (tier2_v2, single_vote_rescue LEAKY, strength_calibration). Plus V39 added corrected_rescue_replay 30d. Total = 9 tables on VPS. | After CP-1.2 | 2026-05-04 | — | 🟢 **VPS_BACKFILL_DONE** | agent | done |
| **CP-1.4** | Verify auto-materialize on first natural closeout (V20.3.37.41 reconciliation): manual materialization is current ground truth; auto-wire is Stage 1 in V41 §18 automation plan (after 2-3 days manual proof). DEFERRED is correct status — not "overdue", as the need for auto-wire is bounded by Stage 0/1 readiness gates. | After natural closeout | per-stage gate | — | ⏳ **DEFERRED_TO_NATURAL_CLOSEOUT_AUTO_WIRE_STAGE_2** | agent | bounded by §18 plan |
| **CP-2.1** | TIER 2 replay 14d run COMPLETE (V20.3.37.33). HONEST FINDING: ALL 4 policies UNDERPERFORM baseline by -9.5 to -14.3 pp BT_WIN. Recommendation: DROP all 4 as designed. New table `tier2_replay_shadow` 168 rows. | 2026-05-02 | 2026-05-04 | 2026-05-04 | 🟢 REPLAY_RAN_NEGATIVE_DROP_AS_DESIGNED | agent | already done; refinement needed |
| **CP-2.2** | Refine policy logic with smaller multipliers (V20.3.37.41 reconciliation): V37 V2 6 policies STILL underperform -19.4 pp clean-day → DROP_AS_DESIGNED. V39 corrected non-leakage rescue framework deployed `corrected_rescue_replay_shadow` 900 rows / 30 dates VPS. V42 post-live evaluation: 2026-05-02 became VALID_LIVE_DAY and corrected replay closeout rows are KNOWN; VALID count now 13. Today added FW=0/FL=1 because production MN BT=73 won and AI_ONLY rescue would have changed away to 30. TIER 3 gate still NOT MET; ACCUMULATE_MORE_DATA. | After owner OK refinement | n/a | n/a | 🟡 **REFINED_V2_DROPPED_AS_DESIGNED + CORRECTED_FRAMEWORK_DEPLOYED_GATE_NOT_MET + ACCUMULATE_MORE_DATA** | agent | gate met when ≥14 VALID days + ≥+5 net pp |
| **CP-2.3** | Run refined replay over fresh 14d window | After CP-2.2 | +14 days after CP-2.2 | — | LOCKED_ON_CP-2.2 | agent | — |
| **CP-2.4** | Refined replay window 14d kết thúc | After CP-2.3 | +14 days after CP-2.3 | — | SCHEDULED | system | — |
| **CP-2.5** | Sinh REFINED REPLAY EVIDENCE PACK với delta BT, false_promotion, flips_to_win/lose per refined policy | Ngay sau CP-2.4 | +1 day after CP-2.4 | — | SCHEDULED | agent | OVERDUE if not generated within 2 days of CP-2.4 |
| **CP-3.0** | Owner reviews evidence pack + decide unlock T3 items nào | After CP-2.5 | +7 days after CP-2.5 | +7 days after CP-2.5 | OWNER_DECISION_GATE | owner | RE-SURFACE if no reply 7 days; ESCALATE 14 days |
| **CP-3.1** | Deploy T3 item #1 (chỉ item nào evidence pack chứng minh + ≥5 pp BT_lift + false_promo < 3%) | After CP-3.0 unlock | +7 days after CP-3.0 unlock | per-item OK | LOCKED_ON_CP-3.0 | agent | per-item OVERDUE +3 days |
| **CP-3.2** | Live verify T3 item #1 (7d closeout sạch) | After CP-3.1 deploy | +7 days after deploy | — | LOCKED_ON_CP-3.1 | agent + owner | — |
| **CP-3.3** | Repeat CP-3.1+3.2 cho item #2, #3, #4 nếu owner unlock | sequential, 1 item/tuần | per-item | per-item OK | LOCKED | — | — |
| **CP-4.0** | Sample maturity check cho TIER 4 (shadow promote / model prune / Cohere on-off) | 2026-06-01 | 2026-06-15 | TBD | SCHEDULED | agent | — |

### Status legend
- `AWAITING_OWNER_OK` — chờ anh trả lời ✅/❌
- `LOCKED_ON_CP-X.Y` — bị block bởi checkpoint khác chưa xong
- `SCHEDULED` — đã có ngày, agent tự làm khi đến hẹn
- `OWNER_DECISION_GATE` — bắt buộc owner quyết định, agent không được tự deploy
- `IN_PROGRESS` — đang làm
- `DONE` — xong, ghi version + evidence
- `BLOCKED` — escalation, cần owner can thiệp
- `CANCELLED` — owner hủy bỏ

### EXTENDED OUTSTANDING — V35 controller pass added these to scope

| ID | Item | Owner OK by | Status | Cross-link |
|---|---|---|---|---|
| **CP-X.1** | pp1_live_watch_daily post-MDE rerun hook (FU-082) — **DEPLOYED V36 Phase A**; V41 reconciliation: code verified at scheduler.py:521+7066. [PP1-WATCH-POST-MDE] marker NEVER observed because V36 deploy 2026-05-02 12:24 happened AFTER yesterday's MDE 13:20. First natural fire window today ~13:20 VN. Companion [P0-RULE-PHASE-POST-MDE] hook fired successfully 2026-05-01 13:20. | per-deploy | ⏳ **WAIT_NATURAL_FIRE_TODAY_~13_20_VN** | FU-082 |
| **CP-X.2** | Degraded-day hygiene canonical criteria (FU-083) — **DOC DEPLOYED V36 Phase A** `docs/DAY_GOVERNANCE_CRITERIA.md`; runtime adoption in CP-2.2 V2 materializer | docs OK done | 🟢 **DOCS_DEPLOYED_RUNTIME_PENDING_V2** | FU-083 |
| **CP-X.3** | Strength gate region-conditional review TIER 3 (FU-084) | TIER 3 unlock | TIER_3_OWNER_LOCK | FU-084 |
| **CP-X.4** | Single-vote rescue regional gate TIER 3 (FU-085) | TIER 3 unlock | TIER_3_OWNER_LOCK | FU-085 |
| **CP-X.5** | MB structural drilldown shadow table (FU-086) — **DEPLOYED V36 Phase A** 61 rows / 60d on VPS | per-deploy | 🟢 **VPS_DEPLOYED_PERSISTENT** | FU-086 |
| **CP-X.6** | FU-065 verifier-level alias fix (verifier should look in dedicated tables for some methods). V41 reconciliation: NOT REPRODUCING today — `rule_phase_evidence_v1` has 56 rows in BOTH `rule_phase_evidence_shadow` AND `shadow_results` for 2026-05-01. All 18 P0 methods present in `shadow_results`. Verifier reports correctly. | per-deploy | LOW_PRIORITY_NOT_REPRODUCING_TODAY | FU-065 |
| **CP-X.7** | Bundle tier-blindness verified -> TIER 3 candidate (tier-aware bundle voting) | TIER 3 unlock | TIER_3_OWNER_LOCK | FU-079 |
| **CP-2.2 (Phase B)** | Refined replay V2 policy materializer (`_materialize_tier2_replay_shadow_v2.py`) + S_SINGLE_VOTE_RESCUE_REGIONAL_V1 + T_STRENGTH_REGION_GATE_V1 + day_tag column. Build estimated ~3 hours work. AWAITING owner OK. | per-deploy | 🟡 **READY_TO_BUILD** | FU-081 |

### V20.3.37.38 correction

| ID | Correction | Status | Cross-link |
|---|---|---|---|
| **CP-X.4** | Option A single-vote rescue STOPPED. V37 positive rescue replay was leaky (target-day actual support + hit-known selection). Corrected non-leaky replay is negative overall: clean-day ALL -8.3 pp, MT -16.7 pp, MB -16.7 pp. | 🔴 **REPLAY_CORRECTION_FAILED** | FU-085, `OPTION_A_STOP_LEAKAGE_CORRECTION_20260502.md` |
| **CP-2.2** | Future rescue work must use corrected non-leaky replay materializer before any owner-unlock package. | 🟡 **NEEDS_CORRECTED_REPLAY_DESIGN** | FU-085 |

---

## 3. SESSION-START PROTOCOL (agent đọc đoạn này mỗi lần mở session)

```
IF FU-073 status != DONE AND ngày hôm nay <= CP-4.0 deadline:
    1. Đọc file này TRƯỚC khi reply câu hỏi đầu tiên của owner
    2. Run `python web/_sync_live_forensic_inputs.py` để có DB live
    3. Loop qua bảng checkpoint, so sánh ngày hôm nay với cột Deadline:
       a. Nếu có CP nào OVERDUE (🔴) → đưa lên ĐẦU reply như sau:
          "⚠ CP-X.Y đang OVERDUE từ ngày YYYY-MM-DD. Action cần: ..."
       b. Nếu có CP nào NEAR deadline (≤1 day, 🟡) → ghi cuối reply:
          "[REMINDER] CP-X.Y đến hạn ngày mai..."
       c. Nếu có CP nào ở status `AWAITING_OWNER_OK` đã quá ngày OK by →
          re-surface với "Anh chưa OK CP-X.Y, em đợi anh quyết..."
    4. Sau khi handle overdue/near, mới reply câu hỏi gốc của owner
    5. Sau khi owner OK / item hoàn thành → cập nhật Status TRONG FILE NÀY +
       sync CHANGELOG + FU-073 trong cùng session (governance rule)
```

→ Nếu agent không tuân theo protocol này, có thể trace bằng grep `CP-` trong agent transcript.

---

## 4. ESCALATION LOGIC

| Trigger | Action |
|---|---|
| 1 CP overdue 3 ngày | Agent đưa lên đầu reply MỖI session đến khi resolve |
| 1 CP overdue 7 ngày | Agent gen 1-page reminder ở đầu reply, link về file này |
| 1 CP overdue 14 ngày | FU-073 status đổi sang `BLOCKED`, ghi DECISION_LOG entry yêu cầu owner can thiệp |
| 2 CP liên tiếp bị skip | Toàn bộ initiative status `BLOCKED`, owner phải re-prioritize |
| Owner explicitly bỏ initiative | Status `CANCELLED`, ghi DEC-XXX, file này archive sang `docs/archive/` |

---

## 5. WHAT ALREADY DONE (lịch sử để recall)

| Date | Event | Reference |
|---|---|---|
| 2026-05-01 | Owner observed MN `17` → MT, MT `46` → MB | session prompt |
| 2026-05-01 | First-pass audit V20.3.37.29 | FU-073 |
| 2026-05-01 | Deeper forensic V20.3.37.30 — confirmed root-cause | `artifacts/phase_checkpoints/TOTAL_FORCE_CROSS_REGION_LEAKAGE_AUDIT_20260501.md` |
| 2026-05-01 | This roadmap file created (V20.3.37.31) | this file |
| 2026-05-01 | FU-073 + SSOT + CHANGELOG synced cross-link | governance |
| 2026-05-01 | Cursor rule `active-roadmap-precedence.mdc` deployed | `.cursor/rules/` |
| 2026-05-01 | TOTAL-FORCE post-live pass V20.3.37.32: `cross_region_spillover_shadow_v1` measurement-only deployed LOCAL with 60d backfill (9428 rows); P0 verifier `NATURAL_CLOSEOUT_PROVEN` 18/18 methods; source-table hashes UNCHANGED; FU-076..FU-080 created. CP-1.1 partial (1/5 surfaces). 15-section closeout report. | `artifacts/phase_checkpoints/POST_LIVE_TOTAL_FORCE_CROSS_REGION_SPILLOVER_CLOSEOUT_20260501.md`, CHANGELOG V20.3.37.32, FU-076..FU-080 |
| 2026-05-01 | TOTAL-FORCE EXTREME continuation V20.3.37.33: CP-1.1 LOCAL complete (5/5: spillover re-backfilled after VPS sync wipe + 2 NEW tables `model_cross_region_dup_shadow` 590 rows + `bundle_universe_coverage_shadow` 90 rows); CP-2.1 TIER 2 replay launched 14d on NEW table `tier2_replay_shadow` 168 rows; HONEST FINDING: all 4 policies UNDERPERFORM baseline -9.5 to -14.3 pp BT_WIN -> recommend DROP as designed; P0 verifier post-MDE 18/18 result rows; FU-081 created; source-table hashes 5/5 UNCHANGED; output unaffected. | `artifacts/phase_checkpoints/TOTAL_FORCE_CP11_CP12_CP21_CONTINUATION_CLOSEOUT_20260501.md`, CHANGELOG V20.3.37.33, FU-081 |
| 2026-05-01 | TOTAL-FORCE ABSOLUTE CONTROL PASS V20.3.37.34: 9 self-discovered audits (strength gate inversion, W+P inflation, degraded-day hygiene, runtime clean, Cohere healthy, REMOVED model residue RECONCILED false alarm, MB Friday 0/5 = 0% WIN, MB BUNDLE_SKEW 53%, source-data G5 healthy); 4 reconciliations; 25-section report; source-table hashes 5/5 UNCHANGED. | `artifacts/phase_checkpoints/TOTAL_FORCE_ABSOLUTE_CONTROL_PASS_20260501.md`, CHANGELOG V20.3.37.34 |
| 2026-05-03 | `/du-doan-test` V47 live-parallel verification: confirmed admin-only/test tables and corrected status to LIVE_PARALLEL_MANUAL; full 25 realtime and AI test prompt are not yet active; manual runner deployed/dry-run verified. | `artifacts/phase_checkpoints/DU_DOAN_TEST_V47_LIVE_PARALLEL_VERIFICATION_20260503.md`, CHANGELOG V20.3.37.47 |
| 2026-05-03 | `/du-doan-test` V49 controller re-read: embedded `TOTAL-FORCE V48 — KẾT QUẢ ĐẦY ĐỦ` found and audited (`V48_EMBEDDED_REPORT_PRESENT`). Current status locked as `MANUAL_STAGE_0_CONFIRMED`, not auto. 2026-05-03 has 0 test rows, 0 scheduler markers, 0 scheduler.py wiring; 25-model realtime remains 14/25 voter coverage; AI test prompt not executing; tensor diagnostic only. | `artifacts/phase_checkpoints/DU_DOAN_TEST_V49_FULL_REPORT_REREAD_AND_LIVE_PARALLEL_CONTROL_20260503.md`, CHANGELOG V20.3.37.49 |
| 2026-05-03 | `/du-doan-test` V50 MB experiment lab deployed on VPS: registry, mode-aware manual runner, evaluator, scoreboards, leakage/conversion audit, API/UI surfacing, and 2026-05-03 MB test rows. Official source hashes unchanged. Status remains `MANUAL_STAGE_0_CONFIRMED` because scheduler auto-wire is still owner-locked / not naturally proven. | `artifacts/phase_checkpoints/DU_DOAN_TEST_V50_PARALLEL_EXPERIMENT_LANE_COMPLETION_20260503.md`, `artifacts/daily_evidence/du_doan_test_mb/2026-05-03.md`, CHANGELOG V20.3.37.50 |
| 2026-05-03 | V51 post-live audit: official closeout 03/05 fully audited without mutation. MT one-day issue measured (no-token/rerun dominance and dropped actual tails), `/du-doan-test` remains `MANUAL_STAGE_0_CONFIRMED`, tensor not pruning-ready, loz mixed. Source hashes unchanged. | `artifacts/phase_checkpoints/TOTAL_FORCE_V51_POST_LIVE_20260503_MEASUREMENT_TEST_LANE_OUTPUT_QUALITY_AUDIT.md`, CHANGELOG V20.3.37.51 |
| 2026-05-03 | V52 full-chain report forensic: reconciled V39/V41/V46/V48/V49/V50/V51 and embedded V48. Confirmed no official mutation, `/du-doan-test` still `MANUAL_STAGE_0_CONFIRMED`, MT 03/05 requires measurement-only drop tracing, loz mixed, tensor not prune-ready, corrected replay still gate-locked. | `artifacts/phase_checkpoints/TOTAL_FORCE_V52_FULL_CHAIN_REPORT_FORENSIC_AND_SAFE_NEXT_STEP_20260503.md`, CHANGELOG V20.3.37.52 |
| 2026-05-03 | V52.1 executed clear non-official-impact work: deployed measurement-only MT drop matrix, loz selector shadow, and latency/cost audit. Official/source hashes unchanged; no `/du-doan` mutation. | `artifacts/phase_checkpoints/V52_MEASUREMENT_ONLY_IMPLEMENTATION_20260503.md`, CHANGELOG V20.3.37.52.1 |
| 2026-05-03 | V52.2 backfilled new measurement-only surfaces over 60 closed days: MT drop matrix 301 rows, loz selector shadow 3273 rows, latency/cost audit 3273 rows. Official/source hashes unchanged. | `artifacts/phase_checkpoints/V52_2_MEASUREMENT_BACKFILL_ROLLUP_20260503.md`, CHANGELOG V20.3.37.52.2 |
| 2026-05-03 | V52.3 surfaced V52.2 measurement rollups in `/du-doan-test` admin UI/API. Official hashes unchanged (except scheduler log restart growth); no official mutation. | `artifacts/phase_checkpoints/V52_3_DU_DOAN_TEST_UI_MEASUREMENT_SURFACING_20260503.md`, CHANGELOG V20.3.37.52.3 |
| 2026-05-03 | V52.4 added MN/MT/MB region tabs and 7/14/30/60 filters to `/du-doan-test`, plus read-only `/api/du-doan-test/{region}`. MN/MT are design-only readiness views with anti-leak cutoff spec, not fake test outputs. | `artifacts/phase_checkpoints/V52_4_MULTI_REGION_DU_DOAN_TEST_UI_READINESS_20260503.md`, CHANGELOG V20.3.37.52.4 |
| 2026-05-03 | V52.5.1 created `model_strength_by_region_weekday_station_daily` materializer + table; populated 9052 rows for anchor `2026-05-02` (D-1 of 2026-05-03 test cycle) across 4 windows × 3 grains. Quantitative proof that model strength is region/run_source/weekday-conditional. Source/official hashes unchanged; tensor flagged `test_only=1`, `output_eligible=0`, `diagnostic_only=1`. Backup `/root/Lottery_AI_Test/backups/v52_5_1_20260503_2300/`. | `artifacts/phase_checkpoints/V52_5_1_MODEL_STRENGTH_TENSOR_20260503.md`, CHANGELOG V20.3.37.52.5.1, FU-114 |
| 2026-05-03 | V52.5 multi-region parallel test lane finished end-to-end (V52.5.2 multi-region preview + V52.5.3 multi-region engine + V52.5.4 registry extension + V52.5.5 multi-region API/UI returning `test_bundle` for MN/MT/MB + V52.5.6 multi-region daily runner). 60d flip evidence: MB SPECIALIST_ROSTER fw=5/fl=0, MN AI_CHAIN_PRESERVATION fw=4/fl=1 hits 32 vs 29, MT AI_CHAIN_PRESERVATION fw=8/fl=12 destructive (confirms owner's MT herding). Hashes for predictions/final_bundles/lottery_results/model_daily_eval identical pre/post; scheduler_logs +46 from service restart + `[DU-DOAN-TEST-*]` test markers only; V52 measurement tables identical. ZERO mutation to `/du-doan` / `final_bundles` / scoring / prompt / model roster / scheduler. | `artifacts/phase_checkpoints/V52_5_MULTI_REGION_PARALLEL_TEST_LANE_20260503.md`, CHANGELOG V20.3.37.52.5, FU-114 |
| 2026-05-04 | V53 / V52.5.8 full-chain controller audit. Reconciled V39 → V52.5.7 (all CONFIRMED, zero overclaim). 5-layer audit (UI/API/DB/code/log) of `/du-doan-test`. DB confirms test methods independent (2026-05-02 MB official=43 LOSE, 4/6 V52.5.2 methods picked 91 WIN; 2026-05-03 MB AI_CHAIN test_bt=85 ≠ official 48). Owner concern classified `UI_LABEL_CONFUSION_INDEPENDENT_AGREEMENT_LOOKS_LIKE_CLONE`. Shipped V52.6 UI source banner + picks-per-experiment table + `🟰 đồng thuận`/`🆚 khác chính` labels. Status remains `LIVE_PARALLEL_AUTO_PENDING_ONLY`. Official quality `OFFICIAL_QUALITY_NOT_PROVEN_MIXED_SIGNAL`. ZERO mutation; only +12 scheduler_logs from V52.6 service restart. | `artifacts/phase_checkpoints/TOTAL_FORCE_V53_FULL_REPORT_CHAIN_DU_DOAN_TEST_REALITY_AND_SAFE_NEXT_ACTION_20260503.md`, `_v53_full_report_chain_state_20260503.json`, CHANGELOG V20.3.37.53, FU-115 |
| 2026-05-04 | V54 live-window-aware pass at 12:55 VN. 2026-05-04 MN bundle exists (BT=65 lo2=[65,32]) pending result; MT/MB predictions only. Implemented C-02 API source labels (response-only), C-06 loz stage trace measurement table (`loz_stage_trace_shadow` 6174 rows), and C-15 weekday blackspot table (`weekday_blackspot_shadow` 21 rows). Confirmed MB Wed/Fri and MT Mon/Fri 30d blackspots. C-05 latency instrumentation deferred because it touches `gpt_analyzer.py` before live cascade. Post-hash: predictions/lottery_results/model_daily_eval/V52/V52.5 tables unchanged; `final_bundles` hash changed only because startup catch-up refreshed 2026-05-03 `updated_at/verified_at` timestamps (BT/lo2/status unchanged). | `artifacts/phase_checkpoints/TOTAL_FORCE_V54_NATURAL_LIVE_CLOSEOUT_MEASUREMENT_AND_TEST_LANE_CONTROL_20260504.md`, `_v54_state_20260504.json`, CHANGELOG V20.3.37.54, FU-117..FU-124 |
| 2026-05-05 (20:14 VN) | V55 full-chain pass after 04/05 + 05/05 closeouts. **Closeout truth:** 04/05 MN BT 65 LOSE + lo2 PARTIAL (32 hit), MT BT 29 WIN + lo2 WIN, MB BT 09 LOSE + lo2 LOSE; 05/05 MN BT 15 LOSE + lo2 LOSE, MT BT 44 WIN + lo2 PARTIAL, MB BT 83 LOSE + lo2 LOSE. **Test-lane wins on MN both days** (SPECIALIST_ROSTER 32 / AI_CHAIN_PRESERVATION 52 — free wins, gate not met). **MT herding pattern remains destructive** (AI_CHAIN broke baseline WIN on both days). **MB structural weak unchanged** (60d 26.7%, 7d 14.3%, Wed/Fri BLACK_SPOT_CONFIRMED). **Discovered + fixed scheduler preflight bug** introduced by V55: `gemma-*` was mis-routed to OpenRouter prefix list → key_missing → gemma-4-31b had 0 rows on 05/05. Fixed in `scheduler.py` (`_get_api_key_for_model` + `_preflight_check_provider_runtime`), deploy 20:08 VN after MB cycle. **Materialized 04/05+05/05** measurement surfaces: loz_stage_trace 182 rows, mt_drop 10 rows, weekday_blackspot anchor 2026-05-05 (21 rows), model_strength tensor anchor advanced 2026-05-02 → 2026-05-05 (8875 rows), experimental_preview_shadow 72 rows, V52.5.6 multi-region runner 25 new bundles for 05/05. **C-05 latency still 0/0 → PRUNING_NOT_ALLOWED_NO_LATENCY.** /du-doan-test still `LIVE_PARALLEL_AUTO_PENDING_ONLY`. ZERO official mutation; predictions/final_bundles/lottery_results/model_daily_eval grew only via natural live cycle. | `artifacts/phase_checkpoints/TOTAL_FORCE_V55_20260504_20260505_CLOSEOUT_AND_NEXT_UPGRADE_PLAN.md`, `_v55_state_20260505.json`, `_v55_pre_hash_20260505.txt`, `_v55_post_hash_20260505.txt`, `live_watch/LIVE_WATCH_20260505_V55.md`, CHANGELOG `V20.3.37.55_full_chain`, FU-126..FU-130, live sync `artifacts/live_sync/20260505_201101/manifest.json` + `20260505_203357/manifest.json` |
| 2026-05-05 (21:41 VN) | V56 `/du-doan-test` Experience Lane. Owner clarified that experiment/test lane should not wait 14/30/60 days just to let owner *experience* new methods; strict gates apply only to official promotion. Added read-only `experience` object to `/api/du-doan-test/mb` and `/api/du-doan-test/{region}`, plus frontend section “Trải nghiệm hôm nay (EXPERIENCE MODE)”. It surfaces method rescues/breaks, baseline clone vs independent agreement, and V55 Google shadow picks. Verified 2026-05-05: MN AI_CHAIN 52 WIN, MB PRIOR_REGION 98 WIN, `gemini-3-flash` MB WIN [91,14], `gemini-3.1-pro` MB PARTIAL. Routes smoke OK. ZERO official mutation; page remains admin-only/test-only/output_eligible=0/promotion_allowed=false. | `artifacts/phase_checkpoints/V56_DU_DOAN_TEST_EXPERIENCE_LANE_20260505.md`, CHANGELOG V20.3.37.56, FU-131, live sync `artifacts/live_sync/20260505_214133/manifest.json`, VPS backup `/root/Lottery_AI_Test/backups/v56_experience_lane_20260505_2133/` |
| 2026-05-05 (23:00 VN) | V57 C-16 adaptive model budget selector for `/du-doan-test`. Implemented model budget surface using full measured pool (29 components) and selecting daily voters by region+weekday+station-set+BT. New test-only tables `du_doan_test_model_budget_daily`, `du_doan_test_selected_voters`, `du_doan_test_model_skip_reason`. 2026-05-05 materialization: MN pool 29 / measured 28 / selected 10; MT pool 29 / measured 28 / selected 8; MB pool 29 / measured 28 / selected 8. API returns `model_budget`; UI shows “Model mạnh hôm nay / C-16 Adaptive Budget”. C-16 also now writes real test method `{REGION}_ADAPTIVE_BUDGET_SELECTOR_V1` via `experimental_preview_shadow` → `du_doan_test_*`: MN test_bt=52 WIN (would_save=1), MT test_bt=52 WIN divergent hit, MB test_bt=41 LOSE. ZERO official mutation. | `artifacts/phase_checkpoints/V57_C16_ADAPTIVE_MODEL_BUDGET_SELECTOR_20260505.md`, CHANGELOG V20.3.37.57, FU-132, live sync `artifacts/live_sync/20260505_230032/manifest.json` + `20260505_231309/manifest.json`, VPS backup `/root/Lottery_AI_Test/backups/c16_model_budget_20260505_2248/` |
| 2026-05-05 (07:56 VN) | V55 add 3 Google direct shadow models (`gemini-3.1-pro`, `gemini-3-flash`, `gemma-4-31b`) into SHADOW lane only. Owner-supplied Google AI Studio key (project sxkt, Tier 2) appended to `/root/Lottery_AI_Test/.env` as `GEMINI_KEY_SHADOW_NEW`; legacy `GEMINI_API_KEY` for `gemini-2.5-flash` / `gemini-2.5-pro` (output models) UNCHANGED. PHASE-FIRST cohort `PFG-20260505-E` opened at 07:45 VN with 8 models (5 prior + 3 new), `contract_required=True`. `is_gemini` predicate extended to also match `gemma*`. `GOOGLE_MODEL_API_MAP` routes registry id → current Google API name (`*-preview` for Gemini 3 family). Real Google API smoke 3/3 PASSED (PONG): gemini-3.1-pro 2.54s, gemini-3-flash 1.40s, gemma-4-31b 2.56s. VPS `/api/health` 200; SHADOW_AUTO 10→13; OUTPUT_ELIGIBLE 15 unchanged; ALL_RUNTIME 28→31. Source hash for predictions/final_bundles/lottery_results/model_daily_eval UNCHANGED. Deployed at 07:55 VN, well outside live windows (16:30/16:42/17:42). | CHANGELOG V20.3.37.55, FU-125, `artifacts/_v55_*` smoke + verify scripts, VPS backups `/root/Lottery_AI_Test/backups/v55_shadow_add_20260505_0750/` |
| 2026-05-03 | `/du-doan-test` full MB test lane V20.3.37.46: deployed separate `du_doan_test_*` schema + MB test engine; 7 test runs/bundles/results and 147 candidates/contributions for 2026-05-02. Official `/du-doan` unchanged. | `artifacts/phase_checkpoints/DU_DOAN_TEST_FULL_MODEL_TENSOR_MB_RECOVERY_20260503.md`, `_du_doan_test_full_engine_vps_run_20260503.txt`, CHANGELOG V20.3.37.46 |
| 2026-05-03 | MB `/du-doan-test` Phase 2 V20.3.37.45.2: added `MB_COMPOSITE_CHALLENGER_V2`, 30d backtest, and UI best-shadow/backtest snapshot. Composite 8/30 vs official 5/30, FW=5 FL=2 FP=2; gate not met, remains shadow-only. | `artifacts/_mb_test_phase2_summary_20260503.md`, `_mb_experimental_backtest_20260503_002427.md`, CHANGELOG V20.3.37.45.2 |
| 2026-05-03 | MB `/du-doan-test` experimental preview V20.3.37.45 deployed: admin-only route/API + `mb_experimental_preview_shadow` materializer/table. Official `/du-doan` unchanged. First shadow rows show 4 MB experiments selecting 91 over official 43 on 2026-05-02, would_flip_to_win=1. Source hash protected. | `artifacts/_du_doan_test_deploy_log_20260502.txt`, `_du_doan_test_vps_materialize_20260502.txt`, CHANGELOG V20.3.37.45 |
| 2026-05-02 | GLOBAL MODEL ? REGION ? WEEKDAY ? MB RECOVERY CONTROL PASS V20.3.37.44: built global model capability tensor (3,216 observations), model role matrix (198 aggregates), latency/value matrix (per-model latency gap identified), MB recovery experiment matrix, MB preview UI feasibility, region UI separation plan, prior-region signal matrix, rule/prompt conversion matrix, shadow control matrix, and master outstanding matrix. No production mutation. | `artifacts/phase_checkpoints/GLOBAL_MODEL_REGION_WEEKDAY_MB_RECOVERY_AUDIT_20260502.md`, `_model_capability_tensor_20260502.csv`, `_mb_recovery_experiment_matrix_20260502.json`, FU-087..FU-095 |
| 2026-05-02 | POST-LIVE TOTAL-FORCE CLOSEOUT + SYSTEM IMPACT AUDIT V20.3.37.42: live closeout complete. MN BT=73 WIN + lo2 WIN; MT BT=88 WIN + lo2 PARTIAL; MB BT=43 LOSE + lo2 PARTIAL via 91. PP1-WATCH-POST-MDE natural fire observed (1 MN event). P0/FU-065 coverage 18/18 clean. 8 safe post-closeout materializers ran on VPS; corrected replay rows refreshed to closeout KNOWN; VALID days now 13; today FW=0/FL=1; TIER 3 gate NOT met. Loz remains mixed/not output-ready. ZERO output mutation. | `artifacts/phase_checkpoints/POST_LIVE_TOTAL_FORCE_CLOSEOUT_AND_SYSTEM_IMPACT_20260502.md`, `_post_closeout_materialization_20260502.json`, `_corrected_replay_delta_after_live_20260502.txt`, CHANGELOG V20.3.37.42 |
| 2026-05-02 | TOTAL-FORCE LIVE STABILITY + MEASUREMENT CONTROL + CORRECTED REPLAY CONTINUATION V20.3.37.41 (read-only audit pass): live watch documented (MN ready BT=73 lo2=[73,54], PP-1 dampener fired on 54, MT/MB pre-cascade, rule quality alert flagged); 9 measurement tables persistence + semantic audit (1 LEAKY_REFERENCE_ONLY = single_vote_rescue_replay_shadow, 1 ACTIVE_ACCUMULATION = corrected_rescue_replay_shadow, 4 DIAGNOSTIC, 2 DROP_AS_DESIGNED, 1 RESEARCH); corrected replay 12 VALID_LIVE_DAY evaluation TIER 3 gate NOT MET on 4 of 8 criteria; Option A stop-guard PASSED (main.py grep clean); PP1-WATCH-POST-MDE V36 hook awaits first natural fire today ~13:20 VN; FU-065 verifier alias NOT REPRODUCING (18/18 methods in shadow_results 2026-05-01); rollover UX banner plan documented frontend-only awaiting owner OK; automation 4-stage plan; CP-1.3/1.4/X.1/X.4/X.6/2.2 reconciled. 5/5 source-table hashes IDENTICAL. 22/22 technical + 15/15 governance no-overclaim self-audit PASS. ZERO mutation to /du-doan, scoring, bundle, lane, prompt, model roster, scheduler. | `artifacts/phase_checkpoints/LIVE_STABILITY_MEASUREMENT_AND_ROLLOVER_AUDIT_20260502.md`, `_live_stability_state_20260502.json`, `LIVE_WATCH_20260502.md`, `_measurement_table_semantic_audit_20260502.json`, CHANGELOG V20.3.37.41, FU-082+FU-065+FU-085 status updates |
| 2026-05-02 | TOTAL-FORCE MONOLITHIC CONTROL PASS V20.3.37.35: full controller pass with 7 deep-dive audits (FU-065 alias verifier-level confirmed, MB structural drilldown by Friday + drop_stage + station, strength gate refined per family x region x bin, single-vote rescue spec MN +10.8 pp / MT -3.8 pp / MB +9.6 pp, 60d degraded-day tag distribution 12 VALID / 18 DEGRADED / 21 INCOMPLETE / 9 EXCLUDE_PRIMARY, bundle tier-blindness CONFIRMED in source_predictions_json, pp1 timing race scheduler trail). FU-082..FU-086 created. Active roadmap expanded with CP-X.1..X.7 tracks. 28-section report. Source-table hashes 5/5 UNCHANGED. | `artifacts/phase_checkpoints/TOTAL_FORCE_MONOLITHIC_CONTROL_20260502.md`, CHANGELOG V20.3.37.35, FU-082..FU-086 |

---

## 6. WHAT'S NEXT (TLDR cho owner sau khi pause project) — V35 UPDATE

> Anh quay lại sau X ngày? Đọc đoạn này:
>
> **CONTROLLER STATE (V35 2026-05-02 00:30)**:
> - CP-1.1 LOCAL_COMPLETE_BUT_NOT_PERSISTENT (VPS sync wipes; need CP-1.2)
> - CP-2.1 DROP_AS_DESIGNED (4 policies all underperformed -9.5 to -14.3 pp)
>
> **Em đang chờ anh quyết các thứ sau (theo độ ưu tiên / risk)**:
>
> ### Owner OK NGAY (zero risk, measurement-only)
> 1. **CP-1.2** VPS push 4 measurement-only files (cross_region_spillover, model_cross_region_dup, bundle_universe_coverage, tier2_replay materializers)
> 2. **CP-X.1** pp1_live_watch post-result-scrape rerun hook deploy (FU-082)
> 3. **CP-X.5** MB structural drilldown shadow table deploy (FU-086)
> 4. **CP-X.2** Add `day_tag` column to next replay design (FU-083)
>
> ### Owner OK CP-2.2 design (refined replay)
> 5. **CP-2.2** Refined replay 4 V2 policies + new S/T policies with smaller multipliers + degraded-day filter
>    - L_LANE_REWEIGHT_CONFLICT_V2 (1.05-1.15x not 1.5x)
>    - R_REGION_DEDUP_PENALTY_V2 (0.95 not 0.85, source-prize-protected)
>    - M_MIRROR_DECAY_MN_V2 (0.9 not 0.7)
>    - U_UNIVERSE_FLOOR_V2 (15-18 not 25, weight 0.15-0.30 not 0.5)
>    - **NEW** S_SINGLE_VOTE_RESCUE_REGIONAL_V1 (FU-085, MN/MB only)
>    - **NEW** T_STRENGTH_REGION_GATE_V1 (FU-084, AI MN 3-4 lower threshold)
>
> ### TIER 3 owner-lock (do NOT touch until CP-2.2 evidence pack 2026-05-19)
> 6. CP-X.3 strength gate region-conditional (FU-084)
> 7. CP-X.4 single-vote rescue regional (FU-085)
> 8. CP-X.7 bundle tier-aware voting (FU-079)
> 9. region-isolated prompt context
> 10. lane_diverse_voting aggregation upgrade
>
> ### WAIT_LIVE / WAIT_DATA (no action)
> 11. TIER 4 model promotion / Cohere on-off (need ≥30 closeouts)
> 12. MB Friday black spot live verification (need more Fridays)
>
> ### DROP_AS_DESIGNED (no action)
> 13. CP-2.1 V1 policies (all 4 underperformed)
>
> Trong giai đoạn em làm tự động, anh KHÔNG CẦN LÀM GÌ. Hệ thống live không thay đổi.

---

## 7. AUTOMATIC PROGRESS TRACKING

Mỗi lần CP đổi status, agent BẮT BUỘC update file này TRONG CÙNG SESSION:
- Update cột `Status`
- Append dòng vào table `WHAT ALREADY DONE` (mục 5)
- Cross-link CHANGELOG version mới
- Cập nhật FU-073 `last_checked` timestamp + `current_truth` nếu thay đổi đáng kể

---

## 8. CROSS-REFERENCES

- Initiative tracker: `docs/FOLLOW_UP_TRACKER.md` → FU-073
- SSOT row: `docs/CURRENT_TRUTH_SSOT.md` → row `Closed-day production truth (2026-05-01) + cross-region leakage forensic`
- Forensic report: `artifacts/phase_checkpoints/TOTAL_FORCE_CROSS_REGION_LEAKAGE_AUDIT_20260501.md`
- Raw audit outputs: `artifacts/_cross_region_leakage_out.txt`, `_source_prize_strong_out.txt`, `_bundle_anti_trap_out.txt`, `_cross_region_dup_out.txt`, `_winrate_summary_out.txt`
- CHANGELOG entries: V20.3.37.29, V20.3.37.30, V20.3.37.31
- Live sync manifest: `artifacts/live_sync/20260501_190852/manifest.json`
- Enforcement rule: `.cursor/rules/active-roadmap-precedence.mdc`

---

## 9. STATUS

**STATUS: ACTIVE**

Khi initiative hoàn tất (CP-3.3 done hoặc owner cancel), thay dòng trên thành:
- `STATUS: COMPLETED on YYYY-MM-DD` HOẶC
- `STATUS: CANCELLED on YYYY-MM-DD by DEC-XXX`

Sau đó move file này sang `docs/archive/ACTIVE_ROADMAP_CROSS_REGION_LEAKAGE_<date>.md`.

---

*Maintained by agent. Owner has read access. Session-start enforcement via Cursor rule.*
