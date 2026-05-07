# V75 — NEXT-ACTION PROPOSAL (post-V74)

**Date:** 2026-05-07 11:55 VN
**Scope:** test-lane only / governance only / measurement only. ZERO official touch unless explicitly owner-approved.
**Audience:** owner — chọn ưu tiên để em triển khai.

---

## 0. Trạng thái hiện tại sau V74 + C-05 resolution

| Layer | Status |
|---|---|
| Strength tensor | ✅ daily refresh, 4 windows × 3 grains |
| C-16 budget | ✅ 20 voters all 3 regions |
| V66.1 lag-1 signals | ✅ 11 flow_types daily |
| V67 ADAPTIVE_EXPLOIT | ✅ eager (no STRICT) |
| V70 CONSENSUS_V1 | ✅ gate ≥3 method agreement |
| V73 HYBRID region-adaptive | ✅ MN/MB exploit-first; MT consensus-first |
| **C-05 latency live** | ✅ **20/42 rows captured 2026-05-07** (qwen3-coder 6.4s nhanh nhất / gpt-oss-120b 190.8s chậm nhất, 0 timeout) |
| C-17B output_lock_status | ✅ added + 669 rows backfilled |
| C-03 evaluator | ✅ PENDING 37→9 |
| 4 governance docs | ✅ CONTINUOUS_MEASUREMENT_DOCTRINE, METRIC_DICTIONARY, OFFICIAL_PROMOTION_GATE, TEST_LANE_METHOD_REGISTRY |
| Daily evidence pack | ✅ bootstrapped 2026-05-07 (Wilson CI rolling 1/3/7/14/30/60/90/180d) |
| GitHub metadata | ✅ LATEST_REPORT.json + REPORT_INDEX.md + 5 supporting files |
| Pre/post hash 4 official tables | ✅ UNCHANGED LOCAL+VPS |
| Cron daily VN | ✅ 23:35→23:40→23:45→23:48 |

→ Hệ thống test-lane đang ở **trạng thái cân bằng tối đa hiện tại**, đo lường liên tục, không chạm official.

---

## 1. P0 — Em đề xuất triển khai NGAY (low-risk, test-lane only)

### P0-1. Drift detector materializer

**Tên:** `_materialize_test_lane_signal_drift_monitor.py`
**Bảng mới:** `test_lane_signal_drift_monitor` (test-lane only)
**Job:** so sánh rolling 7d vs 30d hit rate per (method, region)
**Alerts:**
- 🔴 RED: `|hit_rate_7d − hit_rate_30d| > 15 pp` → method đang drift
- 🟡 YELLOW: 3 ngày liên tiếp dưới random baseline → method có thể bị degrade
- 🟠 ORANGE: 5 ngày liên tiếp consensus_agreement_count < 3 → consensus signal yếu

**Lợi ích:** không phải đợi weekly review để biết V67/V70/V73 bắt đầu kém. Auto-alert ngay khi drift.

**Risk:** ZERO. Materializer-only, test-lane table, no official write.

**ETA:** ~30 phút code + backfill 7 anchors + cron 23:50 VN.

---

### P0-2. C-16 latency_score live integration

**Hiện tại:** C-16 `latency_score = 0.50` flat cho mọi model (vì trước V74 không có latency data thật).
**Sau khi tích hợp:** `latency_score = 1 - (latency_seconds / max_acceptable)`, cap [0.0..1.0]. Áp dụng curve:
- < 30s → score 0.9-1.0
- 30-60s → score 0.7-0.9
- 60-120s → score 0.4-0.7
- 120-180s → score 0.2-0.4
- > 180s → score 0.0-0.2

**Lợi ích:**
- C-16 sẽ tự down-rank `gpt-oss-120b` (190s), `glm-5.1` (184s), `gemma-4-31b` (137s).
- Ưu tiên model nhanh + mạnh: `qwen3-coder` (6s), `kimi-k2.5` (11s), `grok-4.20` (11s).
- Fast model với strength score tốt = double advantage.

**Risk:** ZERO. Chỉ thay đổi logic tính trong `_materialize_du_doan_test_model_budget.py`. Đang dùng latency_seconds đã có (C-05 hoạt động). Không chạm official.

**ETA:** ~20 phút code + re-materialize 14 anchors + so sánh trước/sau.

**Caveat:** Cần ≥3 days latency history để tránh single-day noise. Em sẽ dùng rolling 7d avg latency thay vì 1-day.

---

### P0-3. C-05 cost_estimate provider table

**Hiện tại:** `cost_estimate = None` cho mọi row.
**Đề xuất:** Tạo `provider_pricing_table` (giá USD/1k tokens):
```
gpt-5-mini:    $0.001 / 1k token
gpt-5.4:       $0.005 / 1k token
gpt-5.5:       $0.005 / 1k token
gpt-oss-120b:  $0.001 / 1k token
claude-opus-4: $0.015 / 1k token
claude-sonnet: $0.003 / 1k token
gemini-2.5-pro:$0.00125 / 1k token
gemini-2.5-flash:$0.00075 / 1k token
gemini-3-flash:$0.00075 / 1k token
gemini-3.1-pro:$0.00125 / 1k token
gemma-4-31b:   $0.000 / 1k token (Google AI Studio free tier)
deepseek-reasoner: $0.0014 / 1k token
deepseek-v4-flash: $0.0007 / 1k token
deepseek-v4-pro:   $0.0014 / 1k token
glm-5.1:       $0.0006 / 1k token (OpenRouter)
qwen3-coder:   $0.0006 / 1k token
qwen3-max-thinking: $0.001 / 1k token
qwen3.6-plus:  $0.001 / 1k token
kimi-k2.5:     $0.0008 / 1k token
grok-4.20-multi-agent: $0.002 / 1k token
minimax-m2.7:  $0.0007 / 1k token
```

(Giá em ước lượng theo public listing cuối 2026; anh có thể chỉnh lại nếu có giá thực tế.)

**Cost compute:** `cost_estimate = (token_count / 1000) * price_per_1k`

**Lợi ích:**
- Daily $ tracking: tổng cost/ngày
- Cost-per-hit ratio: model "đắt" nhưng "yếu" → flag cho prune review
- Owner thấy chính xác mỗi ngày tốn bao nhiêu USD cho AI calls

**Risk:** ZERO. Pricing data only, test-lane materializer.

**ETA:** ~20 phút (tạo bảng + patch materializer + recompute).

---

## 2. P1 — Sau khi P0 chạy 7-14 ngày

### P1-1. Method interaction trace surface

Mỗi ngày log:
- Khi nào CROWN tier fire (V67 == CONSENSUS)
- Khi nào AURA tier fire (MN/MB V67 primary)
- Khi nào HIGH tier fire (CONSENSUS only)
- V67 và CONSENSUS DISAGREE bao nhiêu lần / region

Ghi vào bảng `method_interaction_trace_daily` (test-lane only).

### P1-2. C-16 top-20 audit per region/weekday surface

Hiện top-20 model strength rank đang lưu trong `model_strength_by_region_weekday_station_daily` nhưng UI chưa surface. Em build script `top20_per_region_weekday.md` daily.

### P1-3. UI dashboard `/du-doan-test`

Thêm section vào UI:
- Side-by-side OFFICIAL vs HYBRID vs CONSENSUS vs C-16 vs V67 (BT + LO2)
- Tier badge: 🌟 CROWN / 🟢 AURA / 🔵 HIGH / 🟡 MEDIUM / 🟠 LOW / ⚪ SKIP
- Wilson 95% CI hiển thị compact
- Top-20 voters per region với strength score
- Pending/duplicate/readiness warnings inline
- Latency band per model (xanh/vàng/đỏ)

**Risk:** Read-only UI. Frontend only. ZERO backend write.

### P1-4. Per-station + per-weekday consensus

Hiện CONSENSUS cộng dồn theo region. Mở rộng theo (region, weekday, station_set) khi có đủ 180d sample.

---

## 3. P2 — Owner gate, draft only, no implementation yet

### P2-1. OFFICIAL_PROMOTION_DOSSIER.md draft

Tạo file draft theo template `OFFICIAL_PROMOTION_GATE.md`:
- Fill checklist G1-G13 cho V73 HYBRID
- Document rollback plan
- Document risk register

**KHÔNG promote** — chỉ chuẩn bị dossier để owner review sau 14d fresh.

### P2-2. `official_promotion_readiness_shadow` materializer

Compute G1-G12 daily. Khi tất cả gates met liên tục 14 ngày → emit ready signal cho owner review.

**ZERO official write**. Pure shadow tracking.

### P2-3. Region-specific promotion candidates analysis

Phân tích từng region xem method nào ổn định nhất:
- MN: HYBRID AURA 64.3% (n=14) — small sample, cần 30d
- MT: HYBRID HIGH 57.1% (= official) — không cải thiện rõ
- MB: HYBRID 50% (vs official 28.6%) — biggest delta, cần 30d confirm

### P2-4. Lo3 / Xien 2-3 axis consensus

Hiện CONSENSUS chỉ cover BT. Mở rộng:
- LO3 strict 3-digit consensus
- Xien 2 same-station consensus
- Xien 3 same-station consensus

**Risk:** moderate complexity, test-lane only.

---

## 4. P3 — Long-term / owner-decision

### P3-1. NO_TOKEN local timing

Hiện 22 NO_TOKEN model rows missing latency vì chạy local Python. Wrap `time.time()` quanh predict call → có timing.

**Lợi ích:** thấy lstm/xgboost/random-forest chạy bao lâu. Thường <1s nhưng đo cho đầy đủ.

**Risk:** Touches `combo_super.py` và NO_TOKEN model wrappers. Có thể impact production timing nếu sai. Cần shadow trước.

### P3-2. Cohere wide-pool reactivation (CP-66.10)

Cohere hiện rubber-stamp combo_super (5% BT change). Nếu reconfig:
- Candidates = top-10 universe (not top-2)
- Context = analysis + "AVOID yesterday's lose tails"
→ Cohere thành anti-stale post-processor.

**Risk:** Touches Cohere call path. Test-lane only first.

### P3-3. Production AI cascade strength-ordering (CP-20)

Hiện `_run_ai_predict_job` chạy `for ai_model in AUTO_AI_MODELS:` theo registry order. Đề xuất sort theo C-16 score (chỉ shadow trước).

**Risk:** HIGH — touches official cascade. Cần owner OK + 14d shadow proof.

---

## 5. Đề xuất triển khai cụ thể

| Order | Item | Ngay session này? | Risk | ETA | Lợi ích |
|---|---|---|---|---|---|
| 1 | **P0-1 Drift detector** | ✅ YES | ZERO | 30 min | Auto-alert degrade |
| 2 | **P0-2 C-16 latency_score live** | ✅ YES | ZERO | 20 min | C-16 tự ưu tiên model nhanh + mạnh |
| 3 | **P0-3 Cost provider table** | ✅ YES | ZERO | 20 min | Daily $ tracking |
| 4 | P1-1 Method interaction trace | session sau | ZERO | 30 min | Transparency |
| 5 | P1-2 C-16 top-20 audit surface | session sau | ZERO | 20 min | Visibility |
| 6 | P1-3 UI dashboard | session sau | LOW | 1-2 hr | Owner UX |
| 7 | P1-4 Per-station consensus | sau 30d data | ZERO | 45 min | Granular signal |
| 8 | P2-1 OFFICIAL_PROMOTION_DOSSIER draft | session sau | ZERO | 1 hr | Pre-promote prep |
| 9 | P2-2 Promotion readiness shadow | session sau | ZERO | 45 min | Auto-gate tracking |
| 10 | P2-3 Region candidate analysis | continuous | ZERO | continuous | Per-region readiness |
| 11 | P2-4 Lo3/Xien consensus | session sau | LOW | 1 hr | Multi-axis gain |
| 12 | P3-1 NO_TOKEN local timing | session sau | MEDIUM (touches local ML) | 45 min | Complete picture |
| 13 | P3-2 Cohere wide-pool reactivate | sau owner OK | MEDIUM | 1 hr | Anti-stale post-process |
| 14 | P3-3 Production cascade strength-ordering | OWNER GATE | HIGH | 30 min code + 14d shadow | Faster cascade |

---

## 6. Đề xuất em triển khai trong session này (nếu anh OK)

**Top 3 P0 items**:
1. Drift detector materializer + cron 23:50 VN
2. C-16 latency_score live (recompute 14d)
3. Cost provider table + recompute

**Tổng ETA**: ~70 phút.
**Risk**: ZERO. Tất cả test-lane only. Không chạm official.

Sau khi xong, em update CHANGELOG/SSOT/FU/AUTOMATION + push public + private.

---

## 7. Items KHÔNG triển khai trong session này

- P1 dashboard UI (cần 1-2 hr code + verify, để session sau khi P0 ổn)
- P2 promotion dossier (cần 14d data trước)
- P3 (cần owner OK riêng)

---

## 8. Owner decision needed

Chọn 1 trong các option:

| Option | Ý nghĩa |
|---|---|
| **A** "OK em làm hết P0 trong session này" | Em triển khai P0-1, P0-2, P0-3 ngay |
| **B** "Chỉ làm drift detector trước" | Em chỉ làm P0-1, P0-2/3 chờ session sau |
| **C** "Để cron tự chạy 14d trước, đừng đụng" | Em không làm gì, chỉ monitoring qua cron |
| **D** "Làm UI dashboard P1-3 luôn" | Em skip P0 và làm UI ngay |
| **E** Custom | Anh chỉ định cụ thể |

---

STATUS: **PROPOSAL_READY — awaiting owner choice**.
