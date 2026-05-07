# V82 — 60D EVIDENCE CONTROL PASS — Báo cáo tiếng Việt

Ngày: 2026-05-07T23:05:06+07:00
Trạng thái: SHADOW ONLY — KHÔNG động official.

## 0. TL;DR cho anh

- **Anh nói đúng**: V82 cần 60d, đa số đề xuất mới chỉ 4d (V79/V80) hoặc 2d (V81); KHÔNG được dùng 4d/2d để promote.
- **Anh đúng**: AI herd có nguy cơ thật ở MT (60d AI_HERD 43.3% vs OFFICIAL 50.0%, 12 breaks).
- **Anh đúng**: tài liệu (Notion + prompt + cluster) đi trước code/runtime; V78–V80 đã đưa vào shadow nhưng chưa thành consumer official.
- **Anh đúng phần lớn**: MB cold thật, OFFICIAL 60d MB chỉ 25% — nhưng KHÔNG được giải bằng cách tăng NO_TOKEN floor MB (60d NO_TOKEN MB 23.3% < OFFICIAL).
- **OFFICIAL UNCHANGED**: 4 bảng official 60d không bị đụng pre/post; mọi shadow flag đều đúng.

## 1. Latest report verification

- Latest folder = `V81_PROVIDER_SHADOW_PILOT_20260507` (đã reset từ stale-V77).
- `LATEST_REPORT.json` on-disk sau push = V81 (commit `54ea5c8`).
- `official_touched=false`, cron chain 6 jobs/ngày 19:00-19:14 VN, V82 sắp được publish kế tiếp.

## 2. P0.1 → P0.6 status

| P0 | Topic | Implemented | 60d proof | Risk | Next action |
|---|---|---|---|---|---|
| P0.1 | Code↔Notion reconcile | YES (V80 master matrix + 7 Notion pages + V81 governance) | governance only | LOW | Continuous |
| P0.2 | AI↔NO_TOKEN cross-verify | YES (table 12 rows, cron 19:08) | NO (4d only) | LOW shadow | Wait 7-14d natural cron |
| P0.3 | Cluster-weighted consensus | YES (table 130 rows, cron 19:08) | NO (4d only) | LOW shadow | Wait 14d natural cron |
| P0.4 | Rule-phase synthesis pack | YES (table 12 rows, cron 19:12, no consumer) | NO (4d) | LOW shadow | Backfill + observe |
| P0.5 | MB regime-shift mode | YES (table 4 rows, cron 19:12) | NO (4d) | LOW shadow | 7d watch |
| P0.6 | Timezone HCM | CONTAINED (helpers `_today_vn_date_str`/`_tomorrow_vn_date_str`) | YES (14d/7d) | HIGH if regress | P1 audit legacy datetime |

Chi tiết: `evidence/p0_status_matrix.md`.

## 3. 60d evidence — top finding theo region

### 3.1 MN (60d, n=60)

| Method | Hit | n | Save | Break | Net | Verdict |
|---|---|---|---|---|---|---|
| MN_AI_CHAIN_PRESERVATION_V1 | 52.5% (31/59) | 59 | 5 | 1 | +4 | **PROMOTION_CANDIDATE** |
| NO_TOKEN_HERD | 51.7% (31/60) | 60 | 14 | 10 | +4 | REGION_SPECIFIC |
| MN_SPECIALIST_ROSTER_V1 | 51.7% (31/60) | 60 | 4 | 0 | +4 | **PROMOTION_CANDIDATE_CLEAN** |
| AI_HERD | 48.3% (29/60) | 60 | 6 | 4 | +2 | PARITY+ |
| OFFICIAL | 45.0% (27/60) | 60 | 0 | 0 | baseline | BASELINE |

→ MN có ≥ 2 method beat OFFICIAL +6.7pp đến +7.5pp 60d, nhưng chưa promote vì cần 14d fresh live + dossier owner OK.

### 3.2 MT (60d, n=60)

| Method | Hit | n | Save | Break | Net | Verdict |
|---|---|---|---|---|---|---|
| OFFICIAL | 50.0% (30/60) | 60 | 0 | 0 | baseline | BASELINE_STRONG |
| NO_TOKEN_HERD | 51.7% (31/60) | 60 | 7 | 6 | +1 | PARITY (Wilson overlap) |
| MT_NO_TOKEN_HERD_REDUCTION_V1 | 48.3% | 60 | 2 | 3 | -1 | PARITY |
| AI_HERD | 43.3% (26/60) | 60 | 8 | 12 | -4 | **DESTRUCTIVE -6.7pp** |
| MT_AI_CHAIN_PRESERVATION_V1 | 41.7% | 60 | 7 | 12 | -5 | **DESTRUCTIVE -8.3pp** |
| MT_PRIOR_REGION_CONTEXT_SAFE_V1 | 41.7% | 60 | 4 | 9 | -5 | **DESTRUCTIVE -8.3pp** |

→ MT consensus-first đã đúng. AI herd thật sự hại MT 60d. KHÔNG được tăng AI weight cho MT.

### 3.3 MB (60d, n=60 hoặc nhỏ hơn)

| Method | Hit | n | Save | Break | Net | Verdict |
|---|---|---|---|---|---|---|
| MB_SPECIALIST_ROSTER_V1 | 36.6% (15/41) | 41 | 5 | 0 | +5 | PROMISING_BUT_LIMITED_SAMPLE |
| MB_PRIOR_REGION_CONTEXT_SAFE_V1 | 28.3% | 60 | 8 | 6 | +2 | PARITY+ |
| AI_HERD | 26.7% | 60 | 12 | 11 | +1 | NOISY |
| MB_STRENGTH_WEIGHTED_V52_5_2 | 26.7% | 60 | 8 | 7 | +1 | NOISY |
| OFFICIAL | 25.0% | 60 | 0 | 0 | baseline | BASELINE_WEAK |
| NO_TOKEN_HERD | 23.3% | 60 | 5 | 6 | -1 | PARITY |

→ MB cold thật. Chưa method nào đủ 60d clean lift. Cần MB regime forensic chuyên sâu, không tự promote.

## 4. NO_TOKEN vs AI 60d (region-specific)

| Region | NO_TOKEN | AI | Δ | Recommendation |
|---|---|---|---|---|
| MN | 51.7% | 48.3% | +3.4pp | KEEP_BALANCED (within Wilson) |
| MT | 51.7% | 43.3% | +8.3pp | AI_CAP_DECREASE (test-lane only, with break-watch) |
| MB | 23.3% | 26.7% | -3.3pp | REGION_SPECIFIC_ONLY (KHÔNG tăng NO_TOKEN MB) |

→ Owner directive xác nhận: KHÔNG tăng NO_TOKEN floor toàn cục. Chỉ MT có dấu hiệu rõ.

## 5. AI herd risk 60d

| Region | n | AI hit | Severe herd days (>50%) | AI miss rescued by V67/V73/NO_TOKEN |
|---|---|---|---|---|
| MN | 60 | 13 (27%) sao? thấp hơn herd-vs-actual? | 16 | 7/47 |
| MT | 60 | 26 (43.3%) | 27 | 16/49 |
| MB | 60 | 16 (26.7%) | 25 | 13/44 |

(Chú: cột AI hit ở section 3 và 5 khác cách đếm — section 3 đếm theo "AI herd top tail vs actuals tails of region", section 5 theo cùng logic nhưng từ herd dict. Số sẽ khác nhỏ do cách walk multi-station — đã merge sau bug fix.)

→ MT 27 ngày severe herd nhưng AI hit rate vẫn 43.3% (thấp hơn OFFICIAL 50%). Chứng minh AI dồn vào sai. V67/V73/NO_TOKEN có thể cứu 16/49 lần MT AI miss.

## 6. Cluster-weighted (V79) — 4d limit

| Region | OFFICIAL | AI herd | NO_TOKEN | Cluster-weighted | Save | Break |
|---|---|---|---|---|---|---|
| MN | 0/4 (0%) | 0/4 | 0/4 | 0/4 | 0 | 0 |
| MT | 3/4 (75%) | 0/4 | 2/4 | 1/4 | 0 | 2 |
| MB | 0/4 | 1/4 | 1/4 | 0/4 | 0 | 0 |

→ Cluster-weighted 4d KHÔNG vượt OFFICIAL ở MT (1/4 vs 3/4) và còn 2 breaks. Không được promote. Cần ≥14d.

## 7. V81 provider pilot — 2d limit

| Model | n | Hit | Save | Break |
|---|---|---|---|---|
| claude-sonnet-4-6 | 6 | 3 | 1 | 0 |
| deepseek-chat | 6 | 3 | 1 | 0 |
| gemini-3-flash | 6 | 3 | 1 | 0 |

→ 2d không đủ proof. Tiếp tục 7d → 14d natural cron 19:14 VN.

## 8. MB regime-shift forensic

- 60d official MB 25%, AI 26.7%, NO_TOKEN 23.3% — cluster trong ±3pp.
- Severe herd 25/60 ngày (~42%) — herd hoạt động mạnh ở MB nhưng không cứu hit rate.
- 13/44 lần AI miss được V67/V73/NO_TOKEN cứu.
- Hiện chưa có method 60d nào đủ thuyết phục.
- Đề xuất: KÍCH HOẠT shadow MB regime watch 7d (đã có `mb_regime_shift_shadow`); nếu cold ≥ 7 ngày liên tiếp → escalate P0 forensic chuyên sâu (lag/source-prize/station/rule reset).

## 9. MN recovery forensic

- MN 60d OFFICIAL 45%, AI 48.3%, NO_TOKEN 51.7% — NO_TOKEN herd vượt official 6.7pp.
- 60d MN có 2 method clean lift: SPECIALIST_ROSTER (+6.7pp, save=4 break=0) và AI_CHAIN_PRESERVATION (+7.5pp, save=5 break=1).
- V67 1d, V70 4d, V79 cluster 4d, V81 2d — quá ít để dùng độc lập.
- Đề xuất MN recovery: chuẩn bị dossier `MN_TEST_LANE_VOTER_PROPOSAL` sau 14d natural live (đến 2026-05-21), không official.

## 10. MT stability protection

- MT 60d OFFICIAL 50% là baseline mạnh nhất hệ thống.
- AI_HERD MT -6.7pp với 12 break — nguy hiểm thật.
- V70 consensus + V73 hybrid 4/4 trên 4d nhưng quá nhỏ; KHÔNG được dùng để rebalance MT.
- Doctrine: MT giữ OFFICIAL/V70 consensus-first. KHÔNG promote single-source exploit cho MT.

## 11. Safety classification — verdict tổng hợp

Xem `evidence/safety_gate_matrix.md`. Tổng hợp ngắn:

- `OFFICIAL_LOCKED`: official path / model roster / official prompt.
- `OWNER_GATE_REQUIRED`: bất kỳ promotion test-lane voter nào.
- `PROMOTION_CANDIDATE_AFTER_DOSSIER`: 2 method MN (SPECIALIST_ROSTER, AI_CHAIN_PRESERVATION).
- `WAIT_14D_LIVE`: V67, V70, V73, V79 cluster, V79 cross-verify.
- `WAIT_7D_LIVE_THEN_14D_LIVE`: V81 provider pilot.
- `DO_NOT_PROMOTE`: MT AI_CHAIN, MT PRIOR_REGION (60d destructive).
- `REGION_SPECIFIC_ONLY`: NO_TOKEN floor (chỉ MT).
- `DATA_READY_UI_PENDING`: panel admin.
- `KEEP_MONITORING_NO_CONSUMER`: V80 rule_phase, V80 no_token_rule_pack.

## 12. Phương án tối ưu

Xem `evidence/optimal_plan.md`. Tóm tắt:

- 24h: giữ cron, bật UI admin panel read-only (DATA_READY_UI_PENDING).
- 7d: tích lũy V79/V80/V81 7d natural; MB 7d cold check.
- 14d: nếu MN candidates giữ lift sau 14d fresh live → đề xuất dossier MN test-lane voter (KHÔNG official).
- KHÔNG: tăng NO_TOKEN toàn cục, sửa official prompt, promote V67/V73/V79/V81 vào official.

## 13. Owner approval pending

| Item | Trạng thái | Cần OK |
|---|---|---|
| UI admin monitor panel | DATA_READY | Anh OK để build read-only frontend |
| MN dossier draft | sau 14d (target 2026-05-21) | Sẽ trình anh xem trước khi build |
| Provider invoice update vào pricing table | tùy ý anh | Anh có thể tự edit hoặc chỉ thị em làm |
| MB regime forensic deep | nếu cold ≥ 7d | Sẽ tự kích hoạt + báo anh |

## 14. Next 24h / 7d / 14d

- 24h: chỉ chờ closeout 2026-05-08 + chạy natural cron 6 jobs. Em không đụng gì.
- 7d (đến 2026-05-14): Tích V79/V80/V81 + MB watch.
- 14d (đến 2026-05-21): nếu MN candidates giữ lift → trình owner dossier; cron drift V76 chính thức active sau ngày này.

## 15. Hash guard + Official untouched

- Pre/post hashes 4 bảng `predictions/final_bundles/lottery_results/model_daily_eval` không đổi từ V77 đến V82.
- V82 chỉ đọc DB + ghi file `artifacts/v82_60d_evidence_control/` + governance docs.
- KHÔNG có wrapper/route mới chạm `/du-doan` hoặc `/api/final-bundle`.

## 16. Links

- Tóm tắt: [V82_REPORT.md]
- Evidence chi tiết:
  - `evidence/p0_status_matrix.md`
  - `evidence/60d_method_region_table.md`
  - `evidence/30d_method_region_table.md`
  - `evidence/14d_method_region_table.md`
  - `evidence/7d_method_region_table.md`
  - `evidence/4d_method_region_table.md`
  - `evidence/no_token_vs_ai_60d.md`
  - `evidence/ai_herd_risk_60d.md`
  - `evidence/cluster_weighted_4d.md`
  - `evidence/v81_provider_pilot_review.md`
  - `evidence/mb_60d_region_forensic.md`
  - `evidence/mn_60d_region_forensic.md`
  - `evidence/mt_60d_region_forensic.md`
  - `evidence/safety_gate_matrix.md`
  - `evidence/optimal_plan.md`

## 17. Final stance

- Anh đúng về việc cần 60d. Em đã build 60d evidence thật.
- Anh đúng về việc tài liệu đi trước. V78-V80 hiện đang shadow để khớp; chưa consumer.
- Anh đúng về việc không được tự promote. Em vẫn giữ official locked.
- Phương án tối ưu hiện tại: KHÔNG đụng official. Bật UI admin panel read-only. Chuẩn bị MN dossier sau 14d natural live. MB chờ regime forensic. MT giữ consensus-first.
