# V84 — MASTER CONTROL BOARD — Báo cáo cho anh

Ngày: 2026-05-07T23:36:12+07:00
Trạng thái: SHADOW ONLY — Audit + governance, không động official.

## 0. TL;DR cho anh

Anh đang lo "không biết cái nào xong, cái nào còn chờ". V84 trả lời bằng 1 bảng duy nhất + 1 lịch quyết định cụ thể.

**Latest = V83** (V82 monitor UI panel). Em đang chuẩn bị publish V84 này thành report kế tiếp.

**Tổng kết V63 → V83**:
- 5 phase governance docs (CONTINUOUS_MEASUREMENT_DOCTRINE, METRIC_DICTIONARY, OFFICIAL_PROMOTION_GATE, TEST_LANE_METHOD_REGISTRY, SSOT)
- 18-method P0 portfolio đã chạy 8-11 ngày, 14 method `READY_TO_EVALUATE`, 4 method còn chờ 5 ngày (đến 2026-05-12).
- 10 method V52.5 era (60d sample): MN có 2 candidate clean lift (SPECIALIST_ROSTER + AI_CHAIN_PRESERVATION).
- V66/V67/V70/V73/V79/V80/V81 selectors: chỉ 1-15 ngày data, chưa promote được.
- V77/V78/V79/V80/V81 cron 6 jobs/ngày 19:00-19:14 VN active.
- V82 60d evidence pass + V83 admin UI panel deployed.
- 4 official tables hash UNCHANGED suốt V77→V84.

**Cái gì còn chờ** (xem decision_calendar.md cho ngày cụ thể):
- 2026-05-08: 6-cron natural proof
- 2026-05-12: 4 method 14-day-min activate (rule_aware_adaptive_notoken / phase_aware_rerank / etc.)
- 2026-05-14: 7d gate cho V79/V80/V81 + MB cold-streak escalation check
- 2026-05-21: 14d gate, dossier MN test-lane voter (nếu lift giữ)
- 2026-06-06: 30d gate
- 2026-07-06: 60d gate cho V79/V80/V81

## 1. Latest report state

- `LATEST_REPORT.json` on-disk: V83 (commit `d411670 master` / `4511e29 main`)
- Cron chain 6 jobs/ngày 19:00-19:14 VN active
- Open issues count: 0 P0
- Official touched: false
- V83 panel `/v82-monitor` admin-only deployed, route 401 unauth verified

## 2. Em đã xử lý gì từ V77 → V83 (1 tháng việc)

| Version | Deliverable | Trạng thái |
|---|---|---|
| V77 | post-cascade rerun cron 19:00 + fast incident monitor 19:05 + 4d regression diagnostic + V70/V73 timing fix + VPS schema fix | DEPLOYED |
| V78 | AI prompt forensic + 3 region-specialist shadow prompts + ai_prompt_context_audit_shadow + scheduler tzinfo helper fix | DEPLOYED |
| V79 | AI↔NO_TOKEN cross-verification + cluster-weighted consensus + cron 19:08 + region policies | DEPLOYED |
| V80 | rule_phase_synthesis + no_token_rule_pack + mb_regime_shift + mn_v67_save + cron 19:12 + Notion/code/runtime sync (7 pages patched) | DEPLOYED |
| V81 | 3-model owner-approved provider shadow pilot + cron 19:14 (deepseek-chat / claude-sonnet-4-6 / gemini-3-flash) | DEPLOYED + 2D LIVE |
| V82 | 60D evidence control pass — 307 audit cells × 5 windows × 3 regions | DELIVERED |
| V83 | V82 monitor UI admin read-only panel `/v82-monitor` | DEPLOYED |

## 3. Master Control Board (1 bảng duy nhất)

Xem `evidence/master_control_board.md` để full bảng. Tổng cộng 24 dòng covering:

- OFFICIAL baseline
- 4 V52.5 promotion candidates / destructive
- V66/V67/V70/V73 selectors
- V76 drift/latency/cost
- V77 fast incident
- V78 prompt shadow audit
- V79 cluster + cross-verify
- V80 4 surfaces
- V81 provider pilot
- V82 audit + V83 UI
- 18-method P0 portfolio
- Wave 1 + Wave 2
- D-1/D-2 (subsumed) + D-7 (ambiguous resolved)
- Timezone + hash guard

Mỗi dòng có: family / id / current_state / evidence / 60d? / live_proof / next_trigger / decision_date / pass / fail / owner_gate / official_impact / next_action.

## 4. Cái gì THẬT SỰ phải chờ + ngày cụ thể

| Item | Phải chờ đến | Vì sao |
|---|---|---|
| 4 P0 methods (meta_ranker_ltr_dataset, context_specialist_policy, online_bayesian_weighting, …) | 2026-05-12 | Min 14 ngày, hiện 9 ngày |
| V79/V80/V81 7d rolling | 2026-05-14 | Mới 4d/2d, cần 7d |
| MB cold-streak escalation gate | 2026-05-14 | Nếu OFFICIAL MB 0/7 → P0 forensic |
| MN dossier test-lane voter | 2026-05-21 | Cần 14d natural live sustain lift |
| Drift monitor V76 active alerts | 2026-05-21 | Cần 14d fresh-data |
| 30d full sweep | 2026-06-06 | 30 ngày từ 2026-05-07 |
| 60d full V79/V80/V81 | 2026-07-06 | 60 ngày từ 2026-05-07 |

→ KHÔNG còn ngày "chờ thêm" mơ hồ. Mỗi cái có ngày cụ thể.

## 5. Cái gì KHÔNG cần chờ live, có thể làm ngay (an toàn)

1. Owner đăng nhập admin và xem `/v82-monitor` (V83 đã sẵn).
2. Em update `_provider_pricing_table.py` với invoice thật khi anh đưa.
3. Em build Master Experiment Control Board UI mở rộng (xem `evidence/ui_master_board_spec.md`) — chỉ build sau khi anh OK.
4. Em sửa layout V83 nếu anh thấy chưa hợp.
5. Em viết MN dossier draft (sẵn sàng cho 2026-05-21) — có thể bắt đầu chuẩn bị từ giờ.
6. Em xác minh GPT-5-mini key trên VPS (ops issue, không phải pilot bug).

## 6. D-7 / Wave / 17 methods đang ở đâu

Xem `evidence/d7_wave_items.md`.

- **D-1 RULE_MECHANISM_FULL_AUDIT**: doc complete, subsumed bởi P0 portfolio `rule_phase_evidence_v1` + `rule_injection_contract_v1`.
- **D-2 OVERREACH_ROLLBACK_AUDIT**: doc complete, governance principle vẫn áp dụng.
- **D-7**: AMBIGUOUS_LABEL — không có deliverable đứng riêng. Em đã resolve thành "concept 7-day rolling proof gate", áp dụng per-method trong decision_calendar.
- **Wave 1 (V20.3.18-20)**: DEPLOYED + LIVE_PROVEN từ 2026-04-25, 9 control surfaces.
- **Wave 2 (V20.3.22)**: DEPLOYED + LIVE_PROVEN.
- **17 methods** (sau lên 18 với cohere): DEPLOYED + 8-11 ngày data, xem maturity matrix dưới.

## 7. 18-method P0 portfolio status

Xem `evidence/17_methods_status.md` + `evidence/method_maturity_matrix.md`.

| Method | Maturity | 14d verdict | Next gate |
|---|---|---|---|
| freshness_readiness_guard_v1 | 7D | INSUFFICIENT_SAMPLE | READY_TO_EVALUATE (informational only) |
| strongest_to_final_preservation_v1 | 7D | **POTENTIAL_LIFT** | READY (33 rows, 0 fp) |
| no_token_drift_guard_v1 | 7D | DESTRUCTIVE_BIAS (MB lf=14) | READY (drift signal only) |
| rule_phase_evidence_v1 | 7D | DESTRUCTIVE_BIAS (MT 103 lf, 139 fp) | KEEP_DIAGNOSTIC |
| meta_ranker_v1 | 7D | PARITY | READY |
| output_policy_replay_governance_v1 | 7D | PARITY (MT 56/77 win, 0 lf!) | READY (MT-favorable) |
| counterfactual_decision_audit_v1 | 7D | **POTENTIAL_LIFT** (MN 44/79=56%) | READY |
| runtime_final_baseline_control_v1 | 7D | INSUFFICIENT (this IS baseline) | READY (control) |
| phase_first_decision_shadow_v1 | 7D | PARITY | READY |
| anti_herding_shadow_v1 | 7D | PARITY | READY |
| rule_injection_contract_shadow_v1 | 7D | DESTRUCTIVE_BIAS (MT 16 lf, 21 fp) | KEEP_DIAGNOSTIC |
| model_wisdom_scorecard_shadow_v1 | 7D | PARITY (MT 90 lf!) | READY (MT destructive watch) |
| meta_ranker_ltr_dataset_shadow_v1 | 7D | PARITY | **WAIT 5d more** (min 14d) |
| rule_aware_adaptive_notoken_shadow_v1 | 7D | PARITY | READY |
| context_specialist_policy_shadow_v1 | 7D | PARITY | **WAIT 5d more** (min 14d) |
| online_bayesian_weighting_shadow_v1 | 7D | DESTRUCTIVE_BIAS | **WAIT 5d more** (min 14d) |
| phase_aware_rerank_shadow_v1 | 7D | PARITY | READY |
| cohere_rerank_effectiveness_v1 | 7D | INSUFFICIENT (n=23) | READY (low sample) |

→ **14/18 READY_TO_EVALUATE; 4/18 WAIT 5 ngày** (đến 2026-05-12).
→ **2 method có POTENTIAL_LIFT**: `strongest_to_final_preservation_v1` (MN/MT/MB 11/11 win), `counterfactual_decision_audit_v1` (MN 56% lift).
→ **3 method DESTRUCTIVE_BIAS** cần KEEP_DIAGNOSTIC, KHÔNG promote: `rule_phase_evidence_v1`, `rule_injection_contract_shadow_v1`, `no_token_drift_guard_v1`.

## 8. Prompt-first / rule-phase / no-token DB cross-check

Xem `evidence/prompt_first_status.md` + `evidence/ai_no_token_status.md`.

- **Production prompt** (`gpt_analyzer.py SYSTEM_PROMPT`): KHÔNG inject V67/V70/V73, no_token_herd_candidate, agreement_count, MB cold flag. Vẫn dùng prompt cũ.
- **Shadow lane**: V78 region-specialist prompts + V79 context (AI/NO_TOKEN cluster) + V80 rule_phase pack + V81 provider pilot DÙNG đầy đủ context.
- **Status**: PROMPT_AHEAD trong shadow, production OFFICIAL_LOCKED.

## 9. V81 provider pilot status

Xem `evidence/v81_provider_pilot_status.md`.

- 18 calls / 18 OK / 0 break / 1 save mỗi model trên MN
- Cron 19:14 VN active
- 2D → cần 7D (2026-05-14) → 14D (2026-05-21) → 30D → 60D
- GPT-5-mini key issue đang track riêng (ops)

## 10. MN/MT/MB status

### MN — Recovery candidate
- 60d: 2 candidate clean lift, 1 V67 save signal hôm 2026-05-07.
- Decision date: 2026-05-21 cho test-lane voter dossier.
- KHÔNG promote vào official trước 30d.

### MT — Protect at all cost
- 60d: OFFICIAL 50% baseline mạnh nhất hệ thống.
- 6 method DESTRUCTIVE_PROVEN cho MT (xem mt_protection_queue.md).
- Bất kỳ method nào muốn live cho MT phải có lose_flip < win_flip / 2 trên 14d.

### MB — Forensic queue
- 60d: cold thật, mọi method ±5pp.
- MB_SPECIALIST_ROSTER 36.6% hấp dẫn nhưng chỉ n=41.
- Decision date: 2026-05-14 7d cold-streak gate, 2026-05-21 14d, 2026-06-06 30d.

## 11. Decision calendar

Xem `evidence/decision_calendar.md`. 11 mốc cụ thể từ 2026-05-08 → 2026-07-06 + always-on rules.

## 12. Owner-gate queue

Xem `evidence/open_owner_gate_queue.md`. 9 items, mỗi item có trigger_date + blocker + owner_action + official_impact rõ.

## 13. Phương án tối ưu nhất hiện tại

1. **Giữ official locked** (đã làm).
2. **Bật V83 monitor** (đã deploy). Anh xem khi rảnh.
3. **Continuous cron 6 jobs** 19:00-19:14 VN (đã chạy).
4. **Daily auto-update SSOT/FU/AUTOMATION** sau mỗi cycle (đã wired).
5. **2026-05-12** kích hoạt 4 method còn lại tự động (cron đã chạy, chỉ cần đủ 14 ngày).
6. **2026-05-14** auto-check MB cold-streak; nếu cold ≥ 7d → tự generate P0 MB forensic dossier (em sẽ làm).
7. **2026-05-21** MN dossier draft (em sẽ chuẩn bị trước, trình anh xem).
8. **KHÔNG promote** bất kỳ thứ gì vào official trước 30-60d + dossier + owner OK.

## 14. Official UNTOUCHED ✅

- 4 official tables `predictions/final_bundles/lottery_results/model_daily_eval` không bị đụng V77→V84.
- V84 audit READ-ONLY, không ghi DB nào.
- Hash guard PRE = POST mỗi session.

## 15. Next 24h / 7d / 14d

| Khung | Action |
|---|---|
| 24h | Chờ closeout 2026-05-08 + 6-cron natural proof. Em không đụng gì. |
| 7d (đến 2026-05-14) | Tích V79/V80/V81 + MB 7d cold check + 4 method 14d gate (5 ngày nữa) |
| 14d (đến 2026-05-21) | MN dossier draft + drift V76 active + V79/V80/V81 14d rolling review |

## 16. Links + commits (sẽ update sau publish)

- Public V84: `V84_MASTER_CONTROL_BOARD_20260507/`
- Em sẽ commit + push private + public sau khi finalize.

## 17. Final stance

Anh không phải nhớ gì nữa. Bảng `master_control_board.md` + `decision_calendar.md` là 2 file duy nhất anh cần xem.
- Cái gì xong → đã ghi DEPLOYED.
- Cái gì đang chạy → đã ghi NATURAL_CRON_PROVEN.
- Cái gì chờ → đã ghi WAIT XXd với ngày cụ thể.
- Cái gì cần OK → đã ghi OWNER_GATE với decision_date.
- Cái gì không được đụng → đã ghi OFFICIAL_LOCKED.

System sẽ tự nhắc anh tại các mốc. Em sẽ tự generate dossier sẵn cho từng decision_date.
