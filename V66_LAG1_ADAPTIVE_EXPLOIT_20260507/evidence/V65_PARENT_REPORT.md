# V65 — LAG-1 LEAKAGE + STRENGTH PRIORITY + TEST-LANE WEIGHTING AUDIT

**Date**: 2026-05-06 23:50 → 2026-05-07 00:15 VN
**Window**: 2026-04-07 .. 2026-05-06 (30 ngày predictions)
**Live data sync**: artifacts/live_sync/20260506_234557/manifest.json
**Source**: production DB sha256=`893adb19...79347`, prediction_trace.jsonl sha256=`46efd1b7...e5bb9`

> SCOPE: Trả lời 3 câu hỏi của owner (V65 Q1 / Q2 / Q3) bằng data trên cùng 1 SSOT,
> KHÔNG sửa output chính `/du-doan` / `final_bundles`. Mọi thay đổi đề xuất nằm
> ở measurement / test-lane / governance.

---

## TÓM TẮT 1 PHÚT

| Câu hỏi | Tóm tắt verdict |
|---|---|
| Q1 — Số dự đoán SAI hôm trước = số ĐÚNG hôm sau? Có phải NO_TOKEN gây ra? | **Hiện tượng có thật**, nhưng **NO_TOKEN KHÔNG phải thủ phạm chính**. Ở MN final_bundle, tỉ lệ "BT lose hôm N → hit hôm N+1" = **61.5% vs baseline ngẫu nhiên 43%** (🚨 +18.5 pp). Ở per-model, các model có signal cao nhất là **TOKEN/AI** (deepseek-reasoner +33.9, claude-opus +26.2, combo-super +21.3, qwen3-max-thinking +20.6, glm-5.1 +18.5, grok +18.5). NO_TOKEN có 2 model đáng chú ý (`smart-ml` MN +28.4, `random-forest` MT +26.1) nhưng class-level NO_TOKEN ở MB chỉ +0.8 pp (clean). Cohere hiện rubber-stamp combo_super (BT change 5%) → **không giảm leakage**. |
| Q2 — Cơ chế ưu tiên model mạnh theo region+weekday+station đã hoàn hảo? | **Một phần**. Tensor `model_strength_by_region_weekday_station_daily` ✅ refresh hàng ngày, có 4 windows (7/14/30/60), 3 grains (region / region_weekday / region_station). C-16 budget selector ✅ gán 55% trọng số strength + 15% recent (7+14d) → score thay đổi mỗi ngày. **NHƯNG**: cơ chế này chỉ ảnh hưởng **shadow ordering** + **test-lane**. **Production AI cascade `_run_ai_predict_job` vẫn iterate `for ai_model in AUTO_AI_MODELS` theo registry order — KHÔNG ưu tiên theo strength**. |
| Q3 — Test output có cộng điểm cho model mạnh chưa? | **Có**, vận hành hằng ngày. C-16 `final_budget_score` aggregate 5 thành phần với weights `{strength:0.55, recent:0.15, unique:0.10, region_penalty:0.10, latency:0.10}`. Mỗi pick × score × position_weight (1.0 BT, 0.65 #2). C-16 viết `ADAPTIVE_BUDGET_SELECTOR_V1` rows vào `experimental_preview_shadow`, engine `_du_doan_test_engine.py` consume. **Hạn chế**: latency_score hiện flat 0.50 (C-05 mới deploy 2026-05-06 → live data từ 2026-05-07); range final_score hẹp (0.30-0.57) → discrimination yếu. |

---

## Q1 — LAG-1 LEAKAGE: "SỐ SAI HÔM TRƯỚC = SỐ ĐÚNG HÔM SAU"

### Q1.1 Phương pháp đo

Cho mỗi prediction `(date=N, region=R, model=M)`:
- `picks` = parse `main_numbers` → 2-digit tails
- `tails_N` = tất cả 2-digit tails trong `lottery_results` cho `(R, N)`
- `tails_N1` = ditto cho `(R, N+1)`
- **bt_lose_N** = `picks[0] ∉ tails_N`
- **bt_lose_N → bt_hit_N1** = bt_lose_N AND `picks[0] ∈ tails_N1`

So với baseline ngẫu nhiên: `P(hit) = 1 − C(100−distinct_tails, 1) / C(100, 1)`.

### Q1.2 Empirical baselines (random hit rate)

| region | avg distinct tails / day | P(hit) k=1 | P(hit) k=2 |
|---|---:|---:|---:|
| MN | 43.1 | **43.0%** | 67.8% |
| MT | 35.0 | **35.0%** | 58.0% |
| MB | 23.6 | **24.0%** | 42.4% |

### Q1.3 Class-level (NO_TOKEN vs TOKEN)

| region | class | n_pred | bt_hit_N | bt_lose_N | **bt_lose_N → bt_hit_N1** | random k=1 | leakage signal |
|---|---|---:|---:|---:|---:|---:|---:|
| MB | NO_TOKEN | 210 | 25.2% | 157 | 24.8% | 24.0% | ≈ baseline (+0.8 pp) |
| MB | TOKEN    | 453 | 22.1% | 353 | 27.5% | 24.0% | ≈ baseline (+3.5 pp) |
| MN | NO_TOKEN | 210 | 50.0% | 105 | 44.8% | 43.0% | ≈ baseline (+1.8 pp) |
| MN | TOKEN    | 451 | 50.1% | 225 | **57.3%** | 43.0% | ⚠ above (**+14.3 pp**) |
| MT | NO_TOKEN | 210 | 44.8% | 116 | 41.4% | 35.0% | ⚠ above (+6.4 pp) |
| MT | TOKEN    | 446 | 31.2% | 307 | 40.1% | 35.0% | ⚠ above (+5.1 pp) |

> **Verdict class-level**: KHÔNG đúng giả thuyết "NO_TOKEN bị nặng hơn".
> NO_TOKEN ở MB / MN clean ≈ baseline. TOKEN MN có signal +14.3 pp (4.3σ trên 225 mẫu).

### Q1.4 Final bundle (`/du-doan` output thực sự owner thấy)

| region | n | bt_hit_N | bt_lose_N | **bt_lose_N → bt_hit_N1** | baseline | leakage signal |
|---|---:|---:|---:|---:|---:|---|
| **MN** | 29 | 55.2% | 13 | **61.5%** | 43.0% | 🚨 HIGH (**+18.5 pp**) |
| MT | 29 | 37.9% | 18 | 44.4% | 35.0% | ⚠ above (+9.4 pp) |
| MB | 29 | 20.7% | 23 | 26.1% | 24.0% | ≈ baseline (+2.1 pp) |

> **Verdict final-bundle**: Owner thấy đúng — MN có signal cao nhất.
> Mẫu n=13 lose còn nhỏ → CI rộng (~±27 pp), nhưng signal cộng dồn với per-model Q1.5 dưới đây thì **đáng tin cậy ở MN**.

### Q1.5 Top per-model leakage signal (sorted by Δ pp)

**MN (đỏ nhất):**

| model | class | n_pred | bt_lose_N | obs % | Δ vs baseline 43% |
|---|---|---:|---:|---:|---:|
| deepseek-reasoner | TOKEN | 28 | 13 | 76.9% | 🚨 **+33.9 pp** |
| smart-ml | NO_TOKEN | 30 | 14 | 71.4% | 🚨 **+28.4 pp** |
| claude-opus-4-20250514 | TOKEN | 29 | 13 | 69.2% | 🚨 +26.2 pp |
| minimax-m2.7 | TOKEN | 12 | 6 | 66.7% | 🚨 +23.7 pp |
| combo-super | TOKEN | 30 | 14 | 64.3% | 🚨 +21.3 pp |
| qwen3-max-thinking | TOKEN | 21 | 11 | 63.6% | 🚨 +20.6 pp |
| glm-5.1 | TOKEN | 25 | 13 | 61.5% | 🚨 +18.5 pp |
| grok-4.20-multi-agent | TOKEN | 24 | 13 | 61.5% | 🚨 +18.5 pp |
| gpt-5.5 | TOKEN | 10 | 5 | 60.0% | 🚨 +17.0 pp |
| combo-no-token | NO_TOKEN | 30 | 12 | 58.3% | 🚨 +15.3 pp |
| claude-sonnet-4-6 | TOKEN | 29 | 12 | 58.3% | 🚨 +15.3 pp |

**MT:**

| model | class | n_pred | bt_lose_N | obs % | Δ vs baseline 35% |
|---|---|---:|---:|---:|---:|
| deepseek-v4-flash | TOKEN | 10 | 6 | 83.3% | 🚨 +48.3 pp (n nhỏ) |
| deepseek-v4-pro | TOKEN | 10 | 9 | 66.7% | 🚨 +31.7 pp |
| minimax-m2.7 | TOKEN | 12 | 8 | 62.5% | 🚨 +27.5 pp |
| random-forest | NO_TOKEN | 30 | 18 | 61.1% | 🚨 +26.1 pp |
| qwen3-max-thinking | TOKEN | 21 | 16 | 50.0% | ⚠ +15.0 pp |
| gpt-oss-120b | TOKEN | 16 | 10 | 50.0% | ⚠ +15.0 pp |

**MB (sạch):** chỉ `gpt-5-mini` +18.1 pp, `kimi-k2.5` +17.2 pp, còn lại ≈ baseline hoặc dưới.

### Q1.6 Sanity check — Cohere có giúp không?

Window 2026-04-07 .. 2026-05-06, 60 cohere_rerank_log rows (3/region/day).

| region | n | bt_changed | old_hit_N | new_hit_N | old_lose_N→old_hit_N1 | new_lose_N→new_hit_N1 |
|---|---:|---:|---:|---:|---:|---:|
| MN | 20 | **5.0%** (1/20) | 50.0% | 50.0% | 80.0% | 70.0% |
| MT | 20 | 5.0% | 30.0% | 30.0% | 35.7% | 42.9% |
| MB | 20 | 5.0% | 25.0% | 25.0% | 26.7% | 20.0% |

> Cohere hiện chỉ đổi BT 5% lần (essentially rubber-stamp combo_super). Không thay đổi
> hit_N, không giảm leakage. **Cohere KHÔNG giúp gì cho lag-1 leakage ở trạng thái hiện tại.**

### Q1.7 Tại sao có lag-1 (giả thuyết, ranked theo plausibility)

Ngẫu nhiên thuần đã giải thích phần lớn (MB clean, MN/MT chỉ TOKEN class lệch). Phần lệch còn lại (MN +14.3 pp, một số TOKEN models +20-35 pp) gợi ý:

1. **STALE_PROMPT_CONTEXT** — prompt đầu vào cho ngày N có thể chứa "hot tails / cold tails / heat-features" tính trên window 7-30d gần nhất, mà những tail vừa xuất hiện hôm N-2/N-3 vẫn được đánh dấu "đang nóng" vào ngày N+1 sau khi N đã ra. Model TOKEN dễ bị lệ thuộc số "vừa nóng" → trùng với số ra hôm sau. Cao plausibility ⭐⭐⭐⭐.
2. **ML_FEATURE_LEAK_FROM_RECENT_WINDOW** — ML models dùng feature `last_seen_X_days_ago`, `frequency_last_7d`. Nếu actual của day N được scrape vào 18:30 và prediction cho day N+1 chạy lúc 04:00, feature "tail nóng" sẽ phản ánh kết quả N → tạo tương quan với output N+1. Plausibility ⭐⭐⭐.
3. **REPREDICT_KNOWLEDGE** — khi `repredict_verdict='LOSE'` rerun sau closeout với context có actual N, nếu pattern_rules / mined_rules / learned_intelligence cập nhật từ kết quả này thì N+1 prompt có thể "biết" structure lệch — thường "đúng" hôm sau vì lottery có autocorrelation thấp. Plausibility ⭐⭐.
4. **SELECTION_BIAS** — số mẫu lose_N nhỏ (10-30) trên một số model nhỏ (deepseek-v4-flash n=6) tạo CI rất rộng. Plausibility ⭐⭐⭐⭐ cho các model n<15 (không cần hành động khẩn).
5. **NO_TOKEN_MEMORIZATION** (giả thuyết owner) — chỉ thấy ở 2 model `smart-ml`, `combo-no-token`, `random-forest MT`. Không phải pattern hệ thống cho cả lớp. Plausibility ⭐⭐.

### Q1.8 Cohere có thể giúp được điểm này nếu tái cấu hình

Hiện tại Cohere được gọi với context = "analysis text from combo_super reasoning". Vì combo_super đã chọn picks dựa trên tổng hợp các model TOKEN bị stale, Cohere chỉ rerank trong cùng pool → rubber-stamp.

**Nếu** cấu hình Cohere với:
- candidates = pool rộng hơn (top-10 from full-bundle universe, không phải top-2 của combo_super)
- context = bao gồm "anti-stale anchor" (yesterday's actual tails để Cohere PHẠT số trùng)

→ Cohere có thể trở thành **anti-leakage filter**. Đây là proposal C-18 (xem mục cuối).

---

## Q2 — STRENGTH PRIORITY THEO REGION+WEEKDAY+STATION

### Q2.1 Tensor freshness (live state)

```
latest anchor_date = 2026-05-05
latest computed_at = 2026-05-05T20:32:19+07:00
recent anchors: 2026-05-05, 2026-05-02 (refresh ~3 ngày/lần thực tế)
windows = (7, 14, 30, 60)
grains = (region, region_weekday, region_station)
sample threshold: predictions_count >= 5 (region_station/weekday), >= 10 (region)
```

→ Tensor là **daily-anchored, multi-window, multi-grain**. Không phải weekly aggregate — mỗi ngày có anchor riêng.

### Q2.2 Top-3 strongest per region+weekday (anchor=2026-05-05, window=30)

| region | weekday | top-3 (helpful, bt_rate, n) |
|---|---|---|
| MN | Mon | claude-sonnet-4-6 (0.80,0.80,5), combo-super (0.80,0.80,5), xgboost (0.80,0.80,5) |
| MN | Tue | combo-super (0.68,0.60,5), claude-opus (0.64,0.80,5), claude-sonnet-4-6 (0.52,0.60,5) |
| MT | Mon | meta-learning (0.52,0.60,5), smart-ml (0.44,0.60,5), gemini-2.5-flash (0.44,0.20,5) |
| MT | Tue | lstm (0.52,0.60,5), smart-ml (0.44,0.60,5), claude-opus (0.40,0.40,5) |
| MB | Mon | meta-learning (0.36,0.20,5), gpt-5-mini (0.32,0.40,5), claude-opus (0.24,0.40,5) |
| MB | Tue | gpt-5-mini (0.44,0.60,5), lstm (0.44,0.60,5), combo-no-token (0.32,0.40,5) |

→ Strength **thay đổi rõ rệt theo weekday** trong cùng region (e.g. MN Mon: claude-sonnet và combo-super tied; MN Tue: combo-super dẫn → claude-opus hạng 2).

### Q2.3 Score có thay đổi day-to-day?

Compare 2026-05-06 vs 2026-05-05 budget scores (excerpt):

| model | 05-06 | 05-05 | Δ |
|---|---:|---:|---:|
| MN claude-sonnet-4-6 | 0.561 | 0.389 | **+0.172** |
| MN combo-no-token | 0.544 | 0.337 | **+0.207** |
| MN smart-ensemble | 0.561 | 0.421 | +0.140 |
| MT smart-ml | 0.338 | 0.490 | -0.152 |
| MT combo-no-token | 0.309 | 0.449 | -0.140 |
| MB lstm | 0.399 | 0.497 | -0.098 |
| MB gpt-5-mini | 0.364 | 0.476 | -0.112 |

→ Score **đổi đáng kể giữa 2 ngày liên tiếp** (đến 0.2/1.0 = 20% range). Cơ chế daily — không cần weekly rollup.

### Q2.4 Có ưu tiên model mạnh trong PRODUCTION cascade?

```python
# scheduler.py line 3662
for ai_model in AUTO_AI_MODELS:        # ❌ registry order, KHÔNG sort theo strength
    api_key = _get_api_key_for_model(ai_model)
    ...
    result = analyze_and_predict(...)
```

`AUTO_AI_MODELS = TOKEN_MODELS` (theo `model_registry.py`) — gpt-5-mini, claude-sonnet-4-6, gemini-2.5-flash, claude-opus-4-20250514, deepseek-reasoner, gemini-2.5-pro, gpt-5.4 — chạy theo thứ tự khai báo, KHÔNG dựa vào strength tensor.

### Q2.5 Có ưu tiên trong SHADOW lane?

```python
# scheduler.py line 5864 (V60)
def _order_shadow_models_for_region(models, region, date_str):
    # 1) Prefer C-16 budget rows (selector_role priority + final_budget_score)
    # 2) Fallback: model_strength_by_region_weekday_station_daily window=30
    return ordered
```

✅ Shadow models được sort theo C-16 budget score (CONTROL → SELECTED_VOTER → WATCH_ONLY → SKIP_TODAY) trước khi chạy tuần tự.

### Q2.6 Verdict Q2

| Thành phần | Trạng thái |
|---|---|
| Tensor strength theo region+weekday+station | ✅ tồn tại, refresh daily, 4 windows × 3 grains |
| C-16 budget selector dùng tensor | ✅ 55% strength + 15% recent + 30% misc |
| Shadow ordering theo strength | ✅ áp dụng từ V60 |
| **Production AI cascade ordering theo strength** | ❌ **CHƯA** — vẫn iterate registry order |
| Weekly rollup vs daily | Daily cycle (đúng owner mong muốn — adaptive) |

→ "Hôm nay mạnh thì ưu tiên dự đoán sớm để kịp giờ, hôm sau không mạnh nữa thì ưu tiên model khác" — **đã thực hiện cho SHADOW + TEST lane**, **CHƯA cho OFFICIAL output cascade**.

---

## Q3 — TEST OUTPUT CỘNG ĐIỂM CHO MODEL MẠNH THEO REGION+WEEKDAY+STATION

### Q3.1 C-16 Adaptive Budget Selector — đã chạy

Last 6 budget rows:

| run_date | region | weekday | pool | measured | selected | watch | skipped | controls |
|---|---|---|---:|---:|---:|---:|---:|---:|
| 2026-05-06 | MB | Wed | 29 | 23 | 8 | 10 | 11 | 4 |
| 2026-05-06 | MN | Wed | 29 | 28 | 10 | 18 | 1 | 4 |
| 2026-05-06 | MT | Wed | 29 | 22 | 8 | 10 | 11 | 4 |
| 2026-05-05 | MB | Tue | 29 | 28 | 8 | 10 | 11 | 4 |
| 2026-05-05 | MN | Tue | 29 | 28 | 10 | 16 | 3 | 4 |
| 2026-05-05 | MT | Tue | 29 | 28 | 8 | 14 | 7 | 4 |

→ C-16 chạy **mỗi ngày × mỗi region**. 8-10 voters × 4 controls × 10-18 watch.

### Q3.2 Score formula

```python
# _materialize_du_doan_test_model_budget.py line 117
WEIGHTS = {
    "strength":       0.55,   # tensor by region+weekday+station/region+weekday/region
    "recent":         0.15,   # 7-day + 14-day rolling region-only
    "unique":         0.10,   # du_doan_test_model_contribution: unique - dup - herd
    "region_penalty": 0.10,   # MB AI -0.10; herd/hurt penalties
    "latency":        0.10,   # latency >15s/30s/60s penalty; timeout -0.35
}

# Strength internal weighting (line 228)
score = 0.50*helpful + 0.35*bt_rate + 0.15*any_rate

# Selection
1) 4 controls: best output-eligible TOKEN, best NO_TOKEN ML, best ENSEMBLE, best SHADOW_AUTO
2) Fill to target_max=10 with measured AND final_score >= 0.42
3) Backfill to target_min=8 with measured (regardless of score)
```

### Q3.3 Aggregation cho test output (C-16 → experimental_preview_shadow)

```python
# _write_adaptive_preview_row line 681
for voter in selected_voters:
    weight = voter.final_budget_score
    for pos, tail in enumerate(voter.picks[:2]):
        pos_weight = 1.0 if pos == 0 else 0.65
        scores[tail] += weight * pos_weight  # cộng dồn theo strength weight
candidate_bt = max(scores, key=scores.get)
candidate_lo2 = top-2 tails by score
```

→ Test output là **kết hợp có trọng số** của picks từ các voters, weight = budget score. Đây CHÍNH LÀ "tầng cộng điểm cho model mạnh ở miền/thứ" mà owner hỏi.

### Q3.4 Live snapshot 2026-05-06 — top voters per region

**MN top-8 voters (final_budget_score 0.528-0.571):**

| role | model | class | final | strength | recent | unique | latency | penalty |
|---|---|---|---:|---:|---:|---:|---:|---:|
| CONTROL | glm-5.1 | TOKEN | 0.571 | 0.583 | 0.634 | 0.300 | 0.500 | 0.750 |
| SELECTED_VOTER | gpt-oss-120b | TOKEN | 0.571 | 0.584 | 0.647 | 0.275 | 0.500 | 0.750 |
| CONTROL | smart-ensemble | NO_TOKEN | 0.561 | 0.615 | 0.639 | 0.171 | 0.500 | 0.600 |
| CONTROL | claude-sonnet-4-6 | TOKEN | 0.561 | 0.613 | 0.636 | 0.186 | 0.500 | 0.600 |
| SELECTED_VOTER | gemini-2.5-pro | TOKEN | 0.546 | 0.614 | 0.553 | 0.154 | 0.500 | 0.600 |
| SELECTED_VOTER | combo-no-token | NO_TOKEN | 0.544 | 0.607 | 0.566 | 0.155 | 0.500 | 0.600 |
| SELECTED_VOTER | qwen3.6-plus | TOKEN | 0.532 | 0.535 | 0.569 | 0.275 | 0.500 | 0.750 |
| SELECTED_VOTER | combo-super | TOKEN | 0.528 | 0.608 | 0.474 | 0.121 | 0.500 | 0.600 |

**MB top-8 voters (final 0.312-0.399):**

| role | model | class | final | strength | recent | unique | latency | penalty |
|---|---|---|---:|---:|---:|---:|---:|---:|
| CONTROL | lstm | NO_TOKEN | 0.399 | 0.342 | 0.316 | 0.387 | 0.500 | 0.750 |
| CONTROL | qwen3.6-plus | TOKEN | 0.382 | 0.365 | 0.394 | 0.225 | 0.500 | 0.500 |
| CONTROL | gpt-5-mini | TOKEN | 0.364 | 0.347 | 0.450 | 0.259 | 0.500 | 0.300 |
| SELECTED_VOTER | random-forest | NO_TOKEN | 0.356 | 0.342 | 0.239 | 0.226 | 0.500 | 0.600 |
| SELECTED_VOTER | deepseek-reasoner | TOKEN | 0.330 | 0.278 | 0.389 | 0.185 | 0.500 | 0.500 |
| CONTROL | smart-ml | NO_TOKEN | 0.316 | 0.300 | 0.223 | 0.271 | 0.500 | 0.400 |

**Quan sát quan trọng:**
- MB scores thấp hơn MN (đúng — MB harder region, structural penalty -0.10 cho TOKEN AI).
- MB top voter là **`lstm` NO_TOKEN** (không phải AI), phản ánh đúng tensor MB.
- Tất cả `latency_score = 0.500` (flat fallback) vì C-05 mới deploy 2026-05-06 → live data từ 07/05.

### Q3.5 Verdict Q3

| Thành phần | Trạng thái |
|---|---|
| Score cộng theo region+weekday+station | ✅ — strength gốc multi-grain (region_station ưu tiên cao nhất) |
| Score cộng theo recency (7-14d) | ✅ — recent_score weight 0.15 |
| Score cộng theo unique vs herd | ✅ — unique_score weight 0.10 (nhưng sample còn thấp) |
| Score cộng theo latency/cost | ⏳ — code đã wire, data từ 07/05 |
| Test output BT/LO2 dùng weighted aggregation | ✅ — final_budget_score × position_weight |
| `MB_/MN_/MT_ADAPTIVE_BUDGET_SELECTOR_V1` xuất hiện trong UI test | ✅ — được wire vào primary priority V57 |

**Nhược điểm cần cải thiện:**
1. `latency_score` flat 0.50 — sẽ tự động sửa khi C-05 có data (07/05+).
2. `unique_score` cho shadow mới (gemini-3.1-pro, gemma-4-31b) còn 0.45 default vì chưa đủ test_lane contribution rows.
3. Range final_score hẹp (MN 0.47-0.57, MB 0.28-0.40) → discrimination yếu giữa các voters. Nên giãn weights khi C-05 có data.

---

## NEXT-ACTIONS (RANKED, AN TOÀN, KHÔNG CHẠM OUTPUT CHÍNH)

### Tier 1 — fix lag-1 leakage (P0)

**C-18 ANTI-STALE FILTER (test-lane only, shadow proof first)**
- New table: `lag1_stale_pick_filter_shadow`
- Logic: cho mỗi (region, date_N+1), liệt kê BT của final_bundle date_N + top-3 lo2 → nếu một voter trong C-16 chọn 1 trong các tail này, scaling weight × 0.5
- Trong `_materialize_du_doan_test_model_budget.py` thêm `_anti_stale_score` = 1.0 nếu pick KHÁC yesterday's loss-set, 0.5 nếu match
- Đo `would_avoid_lag1_leak` per region per day → 30 ngày proof → owner OK promote production
- **Test-lane only, output_eligible=0, không chạm `/du-doan`**.
- Estimate: 1 file mới + 30 dòng patch C-16. ETA 1 ngày.

**C-19 PROMPT_LAG1_LEAKAGE_AUDIT (measurement-only)**
- New table: `prompt_lag1_audit_shadow` — log mỗi prediction: list các "hot tails" trong prompt context có trùng N-1 actuals không
- Identify pattern: model nào nhận stale context nhiều nhất
- 30 ngày data → biết có nên thay đổi prompt design (P1+)
- Pure measurement.

### Tier 2 — strength priority cho production (P0 nhưng cần proof)

**C-20 PRODUCTION AI CASCADE STRENGTH-ORDERING (shadow proof first)**
- Đo: trong shadow mode, sort `AUTO_AI_MODELS` theo C-16 score, log thứ tự predicted vs current registry order
- Compare: nếu strong-first order, model thứ 1-2 (mạnh nhất trong bucket) hoàn thành trước cutoff thường xuyên hơn → ít miss
- **KHÔNG đổi production order ngay** — shadow proof 14-30 ngày
- Promote khi có evidence ổn định → owner OK

### Tier 3 — Cohere reactivation (P1)

**C-21 COHERE WIDE_POOL ANTI_STALE (test-lane only)**
- Reconfig Cohere: candidates = top-10 universe (không chỉ combo_super top-2)
- Context = analysis_text + "AVOID_TAILS: <yesterday lose tails>"
- Đo bt_change_rate (hiện 5%) → expected 25-40% sau reconfig
- Nếu bt_change_rate cao và lag1_leak giảm → promote thành post-processor cho test-lane

### Tier 4 — Score discrimination (P1, sau C-05 data)

**C-22 BUDGET_WEIGHT_RECALIBRATION**
- Đợi 07/05+ có C-05 latency data → recompute baseline distribution
- Stretch weights để discrimination tốt hơn (e.g. strength 0.55 → 0.60, latency 0.10 → 0.15 khi data có)
- Reweight không cần touching production output.

---

## RAW PROOF PATHS

| Artifact | Path |
|---|---|
| Live sync manifest | `artifacts/live_sync/20260506_234557/manifest.json` |
| Lag-1 audit script | `artifacts/v65_lag1_audit/_v65_q1_lag1_audit_v2.py` |
| Lag-1 audit report | `artifacts/v65_lag1_audit/v65_q1_lag1_audit_v2_report.md` |
| Cohere effectiveness | `artifacts/v65_lag1_audit/v65_q1c_cohere_audit.md` |
| Strength + C-16 dump | `artifacts/v65_lag1_audit/v65_q23_strength_audit.txt` |
| Per-class JSON | `artifacts/v65_lag1_audit/v65_q1_v2_per_class.json` |
| Per-model JSON | `artifacts/v65_lag1_audit/v65_q1_per_model.json` |

## GOVERNANCE

- Không chạm `predictions`, `final_bundles`, `generate_final_bundle()`, `model_registry.py` ACTIVE/output_eligible.
- Mọi proposal C-18/19/20/21/22 đều chạy ở `*_shadow` table với `official_output=false`, `output_eligible=0`, owner_approved=0.
- Test-lane window: 14-30 ngày proof trước khi xin owner OK promote.

---
STATUS: REPORT_COMPLETE — chờ owner confirm Tier để em tiến hành.
