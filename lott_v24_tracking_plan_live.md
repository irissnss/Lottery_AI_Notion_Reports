# LOTT v2.4 — TRACKING PLAN LIVE
**Created:** 2026-06-05 13:50 VN | **Type:** Live monitoring (T5 + T6 items)

---

## I. DATA COVERAGE FINAL (sau T2.cont)

| Region | Total dates | Full stations | First date | Last date |
|---|---|---|---|---|
| MN | 24 | **18 ngày ≥2 đài** ⬆ from 11 | 2026-05-12 | 2026-06-04 |
| MT | 24 | **18 ngày ≥2 đài** ⬆ from 11 | 2026-05-12 | 2026-06-04 |
| MB | 31 | 31 (1 đài/ngày) | 2026-04-28 | 2026-06-04 |
| **DB total** | — | **315 records** ⬆ from 192 | — | — |

Improvement: +123 records trong session, MN/MT full-station coverage tăng 64%.

---

## II. T5 — VERIFY T6 HÔM NAY (Live trong vài giờ tới)

### Timeline

| Time VN | Event | Auto-action |
|---|---|---|
| **16:15** | MN xổ (Vĩnh Long, Bình Dương, Trà Vinh) | scraper trigger |
| **16:35** | post_mn phase | `restore → preflight → cào MN → verify MN → re-predict MT/MB (cascade) → save → audit → backup` |
| **17:15** | MT xổ (Gia Lai, Ninh Thuận) | scraper trigger |
| **17:35** | post_mt phase | `cào MT → verify MT → re-predict MB SP only → save → audit → backup` |
| **18:15** | MB xổ (Hải Phòng) | scraper trigger |
| **18:35** | post_mb phase | `cào MB → verify MB → tổng kết → save → backup → update knowledge_accumulator` |
| **19:00+** | end-of-day | `verify all + predict D+1 (06/06 T7) + knowledge update` |

### Predictions cần verify (v2.4 final)

| Miền | BT | SP1 | SP2 | Xiên | Score | Expected outcome |
|---|---|---|---|---|---|---|
| **MN** | 80 | 16 | 67 | X2 80-16, X3 80-16-67 | 7.2/10 | Mirror #1 + cross-3 — high confidence |
| **MT** | 52 | 16 | 22 | X2 52-16, X3 52-16-22 | 7.5/10 | DDXS-aligned 6 signals — strongest pick |
| **MB** | 16 | 52 | 80 | X2 16-52, X3 16-52-80 | 6.5/10 | Overheating WARN but 6 signals — risky bet |

### Success criteria T5 (đánh giá lúc 19:00)

| KPI | Target | Threshold |
|---|---|---|
| BT hit rate 3 miền | ≥ 1/3 hit | Baseline 33%, target ≥33% |
| Any hit rate | ≥ 2/3 (≥66%) | Baseline 89%, target ≥66% |
| SP hit rate | ≥ 3/6 (≥50%) | Baseline 33-67% |
| Xiên 2 hit | ≥ 1 (out of 3) | Baseline 50% |
| Audit consistency | Match prediction post-verify | 100% |

### Cascade tracking (CRITICAL — v2.4 sẽ tự re-predict)

| Phase | What changes | Watch for |
|---|---|---|
| 16:35 post_mn | MT BT có thể đổi (cascade primary), MB BT giữ (cascade SP only) | Markov MN→MT transition |
| 17:35 post_mt | MB SP có thể đổi (G4 CASCADE_MT_ONLY) | KHÔNG đổi MB BT |
| 18:35 post_mb | Final verify all + lock | Compare 3 versions trong DB |

---

## III. T6 — A/B TEST 7 NGÀY v2.3 vs v2.4

### Design

**Hypothesis:** v2.4 (audit + mirror + multi-signal) > v2.3 baseline về BT hit rate hoặc severity reduction.

**Setup:**
- v2.3 baseline: existing predictions trong DB (date 02-04/06 = 9 data points)
- v2.4 starting: hôm nay (05/06) trở đi
- Test window: **05/06 → 11/06 (7 ngày)** = 21 predictions

### Metrics tracked daily

| Metric | v2.3 baseline (3 ngày) | v2.4 target |
|---|---|---|
| BT hit rate | 44.4% (4/9) | ≥ 50% |
| Any hit rate | 89% (8/9) | ≥ 85% |
| SP1 hit rate | 22% (2/9) | ≥ 30% |
| SP2 hit rate | 67% (6/9) | ≥ 60% |
| Audit BLOCK incidents | 1 (morning_v23) | 0 |
| Independence violations | Multiple | 0 |
| Overheating accepted | N/A | Track outcomes |

### Daily logging template (em sẽ tự update mỗi ngày sau 19:00)

```
[YYYY-MM-DD] LOTT v2.4 Daily Log
  MN: BT=XX [HIT/MISS]  SP1=XX [H/M]  SP2=XX [H/M]  X2=XX-YY [H/M]
  MT: BT=XX [HIT/MISS]  SP1=XX [H/M]  SP2=XX [H/M]  X2=XX-YY [H/M]
  MB: BT=XX [HIT/MISS]  SP1=XX [H/M]  SP2=XX [H/M]  X2=XX-YY [H/M]
  Audit: severity=PASS/WARN/BLOCK, violations=N
  Insights: [pattern phát hiện được]
  Knowledge update: layer_X bumped, auto_rule_Y added
```

### Decision point 12/06 (sau 7 ngày)

| Outcome | Action |
|---|---|
| v2.4 BT > 50% & 0 BLOCK | **PROMOTE** v2.4 → default. Deprecate v2.3 logic. |
| v2.4 BT 40-50% & WARN < 3 | **CONTINUE** monitoring 7 ngày nữa |
| v2.4 BT < 40% OR BLOCK > 0 | **ROLLBACK** + root cause analysis |
| Mixed results | **HYBRID** — pick best per region |

---

## IV. AUTO-MONITORING SCRIPTS (đã có sẵn)

| Script | Purpose | Trigger |
|---|---|---|
| `run_lott.py preflight` | Check phase, data_ok, need_scrape | Mỗi phase boundary |
| `run_lott.py verify` | Verify predictions vs actual | Sau mỗi miền xổ |
| `run_lott.py backup` | Backup DB to JSON | Sau mỗi save/verify |
| `lott_audit.py audit_predictions()` | 3 checks pre-save | Auto-fire trong save_prediction |
| `lott_mirror.py analyze_mirror_full()` | Tầng 6 signal | Auto-inject vào context |
| `backtest_mirror.py` | Compare 4 methods | Manual khi cần re-validate |

---

## V. CHECKLIST EM SẼ TỰ THỰC THI

### Mỗi phase (16:35, 17:35, 18:35):
- [ ] Run `preflight` để check data status
- [ ] Run `verify` để chấm BT/SP/Xiên
- [ ] Run `save` với version mới (post_mn/post_mt/post_mb)
- [ ] Verify audit output không BLOCK (chỉ WARN acceptable)
- [ ] Update knowledge_accumulator nếu có insight mới
- [ ] Run `backup` cuối phase

### Cuối ngày (19:00):
- [ ] Tổng kết hit rate 3 miền
- [ ] Update `cumulative_stats` trong knowledge_accumulator
- [ ] Update `learning_matrix[region][T6]` với notes
- [ ] Predict D+1 (06/06 T7) với v2.4 methodology
- [ ] Append entry vào `weight_adjustments.log`
- [ ] Write daily report `lott_pred_20260605_summary.md`

### Hàng ngày 06/06 → 11/06:
- [ ] Repeat full phase cycle
- [ ] Daily log entry vào tracking file
- [ ] Mid-week check 09/06: KPI status

### 12/06 (decision day):
- [ ] A/B compare 7-day v2.3 vs v2.4
- [ ] Decision: PROMOTE / CONTINUE / ROLLBACK / HYBRID
- [ ] Update `LOTT_SUPER_SKILL.md` với findings

---

## VI. RISK & MITIGATION

| Risk | Likelihood | Mitigation |
|---|---|---|
| MB 16 overheating MISS | HIGH (đã WARN) | Có SP=52, SP=80 backup. Any hit vẫn có khả năng. |
| MN 80 mirror burnout | MEDIUM | Mirror balance 1.0 nên ít risk overheating |
| MT 52 cascade re-predict đổi BT | HIGH | post_mn sẽ re-evaluate, accept new BT nếu tốt hơn |
| File truncation lại xảy ra | MEDIUM | Use Python script write atomically, không dùng Edit cho file > 500 lines |
| 7-day backtest sample vẫn nhỏ | HIGH | Continue monitoring sau 12/06, không close A/B sớm |

---

## VII. TÓM TẮT — Còn lại gì?

### Đã xử lý DONE:
- T1 wire audit ✅
- T2.cont MN+MT extension ✅ (+39 records, 64% improvement coverage)
- T3 knowledge v3.4 ✅
- T4 wire MIRROR ✅
- T7 dedupe ✅
- T11 recover v3.3 detail ✅
- Dashboard chuẩn chỉnh ✅ + LOCKED rules trong SKILL.md

### Chờ live (em sẽ tự xử lý theo schedule):
- **T5** verify T6 hôm nay 16:35/17:35/18:35 — auto trigger
- **T6** A/B test 7 ngày — daily logging từ hôm nay

### Không cần action thêm:
- Tất cả modules wired và tested
- Layout dashboard locked
- Process discipline checklist documented
- Knowledge base full recovery

---

## KẾT LUẬN

Em đã xử lý hết các tồn đọng có thể xử lý NGAY (T2.cont + dashboard). 2 items còn lại (T5, T6) là live monitoring — em đã chuẩn bị plan chi tiết + KPIs + checklists.

Anh không cần làm gì thêm. Lúc 16:35 hệ thống sẽ tự verify MN + re-predict cascade. Em sẽ update report sau mỗi phase.

**Next milestone:** 12/06/2026 — A/B test decision point.
