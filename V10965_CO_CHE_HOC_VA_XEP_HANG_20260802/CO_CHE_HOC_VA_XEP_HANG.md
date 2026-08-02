# Cơ chế học và xếp hạng — tài liệu kiểm soát (V10965)

> Viết **02/08/2026** (giờ Việt Nam). **Chỉ đọc** code + crontab + DB VPS. Không sửa đường ra số (QD-014 đóng băng tới hết 08/08).  
> VPS `14.225.224.89` · DB `/root/Lottery_AI_Test/data/lottery_ai.db` · bằng chứng `artifacts/v10965_co_che_hoc/`.  
> Bản rút gọn song song (agent khác): `docs/CAC_CO_CHE_HOC_CUA_HE.md`. Tài liệu này là bản **đầy đủ sáu câu hỏi bằng chứng**.

Owner nguyên văn:

> *"Rồi các cơ chế như học tập tích luỹ, xếp hạng, retrain của các model LLM và ML thì sao, em đã đào sâu hết cỡ chưa? Viết chi tiết cụ thể tất cả mọi thứ hiện đang code để kiểm soát, tổng hợp thật đầy đủ."*

---

## 1. Bảng tổng một trang

Cột **Ảnh hưởng số?** trả lời câu quan trọng nhất: kết quả có quay lại đổi số công bố `/du-doan` không.

| # | Cơ chế | Chạy lúc nào | Sống? | Ảnh hưởng số? | Ghi chú ngắn |
|---|---|---|---|---|---|
| 1 | Retrain ML (meta/xgb/rf/lstm) | CN **02:00** APScheduler + cron **06:30** backstop | **Sống** | **Có** — file model → dự đoán ML → vote | AUC MN/MB ≈ 0,50; MT nhỉnh |
| 2 | Weight optimizer | CN **03:00** + cron **07:00** | **Sống** | **Có (mềm)** — `app_settings.learned_weights` → `statistical_analyzer` | Lift tốt nhất **âm** cả 3 miền |
| 3 | Đào luật tuần | T2 **00:30** + cron **07:00** | **Sống** | **Có (qua prompt)** — nuôi RULES-FIRST | 105 luật `v2026W31` |
| 4 | Chấm luật ngày (MRE) | **20:15** | **Sống** | Gián tiếp — promote/demote luật | 01/08 còn ghi |
| 5 | RULES-FIRST (ép list ~11 số) | Mỗi lần gọi LLM | **Sống** | **Có và đang hại** | List 12,4% ≈ random; pick 35,8% |
| 6 | Prompt nhồi stats / Phase-15 / context | Mỗi lần gọi LLM | **Sống** | Có (in-context) | LLM không train lại |
| 7 | `model_daily_eval` | **20:20** (+ inline sau verify) | **Sống** | **Có** — nguồn lọc combo-super | Nền đo |
| 8 | Lọc combo-super (bạch thủ) | Trong luồng dự đoán | **Sống** | **Có** | V10938; nửa UNIFIED vẫn WR+50% |
| 9 | Vote official `/du-doan` | T-chốt bundle | **Sống** | **Có — quyết định cuối** | Trọng số theo win_rate (+PARTIAL) |
| 10 | `money_board` | Snapshot/score ngày | **Sống** | **Vốn `/choi` thôi** | Không đổi số |
| 11 | `model_progress` | cron ~**09:05** | **Sống** | **Không** | Chỉ xem + nuôi weakest |
| 12 | `weakest_model_watch` | cron ~**09:15** | **Sống** | **Không** | Nhãn SHADOW_PROMPT / RETRAIN — không tự cắt |
| 13 | `shadow_scoreboard` | cron **09:10** | **Sống** | **Không** | 0 promote official nhiều tháng |
| 14 | `_v10871` quality ledger | cron **21:25** | **Sống** | **Không** (CP-L6 tạm dừng) | as_of 01/08 |
| 15 | `_v10945` edge_gate | (ghi sổ đo) | **Sống đo** | **Không** — cổng đóng cả 3 miền | MN −0,36 · MT −2,92 · MB −7,19 pp |
| 16 | Three-layer scoreboard | On-demand API | **Sống đọc** | **Không** | Không ghi bảng |
| 17 | Champion selector | cron **06:25** | **Chạy cron nhưng bảng đứng** | **Không** | Log 02/08; bảng max **15/06** |
| 18 | MB/MN-MT rule re-rank | 04:40 / 20:30 / 20:35 | **Sống** | Mềm (prompt MB) | |
| 19 | pattern_tracker → learned factor | Sau verify MB | **Sống ghi** | Có đường code | `pattern_rules` **160/160 inactive** |
| 20 | Optuna tune | Không lịch | **Chết** | Không | Không có `optuna_params/` trên VPS |
| 21 | Shadow V81/V101/V104/V105 | Job còn đăng ký | **Chết cứng 31/05** | Không | Early-return DISABLED |
| 22 | `model_latency_cost_audit_daily` | — | **Chết** (max 06/05) | Không | Không ai đọc |
| 23 | `pnl_daily_summary` | — | **Chết** (max 20/05) | Không | Không ai đọc |
| 24 | Legacy `pattern_rules` boost | — | **Tắt V6.4** | Không | Boost disabled |
| 25 | Nhiều lane shadow V66–V96 / V107xx | Crontab chiều–tối | **Sống ghi shadow** | **Không** (trừ khi owner promote) | Chạy cho đo |

**Đếm nhanh (02/08):**

| Nhóm | Số |
|---|---:|
| Cơ chế học/xếp hạng **đang chạy và còn sống** | ~18 |
| Trong đó **ảnh hưởng số công bố** | **7** (retrain ML, optimizer, luật→RULES-FIRST, MDE→combo, vote, soft mined boost, MB re-rank prompt) |
| **Chạy mà kết quả gần như không ai đọc / không đổi số** | ~8 (progress, weakest, shadow_scoreboard, quality ledger, edge_gate, three_layer, champion bảng đứng, nhiều shadow lane) |
| **Đã chết / tắt cứng** | ~6+ (Optuna, V81/V101/V104/V105, cost/pnl stale, pattern boost) |
| **Đang hại có bằng chứng** | **1** (RULES-FIRST) |

---

## 2A. Phía model ML

### A1. Huấn luyện lại meta / xgboost / random-forest

| Câu hỏi | Bằng chứng |
|---|---|
| **File / hàm / dòng** | Điều phối `_retrain_all.py::main` (~37–128); thu mẫu `meta_data_collector.collect_training_data`; train `meta_learner.MetaLearner.train`, `ml_models.MLModel.train`; sổ `_v10952_training_journal.ghi` |
| **Chạy lúc nào** | APScheduler CN **02:00** → `scheduler._run_auto_retrain` → subprocess `_v10646_retrain_guard.py --force`. **Không** chỉ tin comment: crontab thật có `30 6 * * * …_v10646_retrain_guard.py` (backstop) |
| **Đọc / ghi** | Đọc `lottery_results` (+ analyzer). Ghi CSV `data/meta_training_*.csv`, file `data/models/*.{pkl,joblib}`, `*_metrics.json`, bảng `training_history` |
| **Lần gần nhất** | **02/08 ~02:00–02:02** — `training_history` 12/12 OK; `ml_retrain_guard_log` id69 `RETRAINED forced … 0/12 lỗi`. 06:30 cùng ngày `FRESH_SKIP` tuổi 0,19 ngày |
| **Ảnh hưởng số?** | **Có.** Registry: meta/xgb/rf `output_eligible=True` → dự đoán 04:00 → vào vote `/du-doan` và combo-super |
| **Còn sống?** | **Sống.** Trước đó 05–07 từng chết in-process (`I/O closed file`); V10800 subprocess đã cứu. 12/07 từng 0 OK trong sổ cũ |

**Cửa sổ / đặc trưng / mẫu (code + DB 02/08):**

- Cửa sổ train: **300 ngày** (`_retrain_all.DAYS_BACK`).
- Đặc trưng: **28 cột** tabular.
- Mẫu: ~**2400**/miền (cột `samples` trong `training_history`).
- LSTM riêng: 500 ngày, seq (30×100)+meta — chỉ train trong `_v10646_retrain_guard._retrain`.

**AUC 02/08 (DB thật):**

| Miền | lstm | meta | rf | xgb |
|---|---:|---:|---:|---:|
| MT | 0,5554 | 0,5394 | 0,5299 | 0,5236 |
| MN | 0,5137 | 0,4892 | 0,5039 | 0,4993 |
| MB | 0,5106 | 0,4768 | 0,5017 | 0,4839 |

MN meta AUC tụt 0,5115→0,4892 (−0,0223) — **cảnh báo ghi sổ, model vẫn giữ** (không có cổng tự rollback; FU-209 / FU-213).

### A2. Bộ tự chữa 06:30

| Câu hỏi | Bằng chứng |
|---|---|
| **File** | `_v10646_retrain_guard.py::main` (~141–169), ngưỡng `THRESHOLD_DAYS=8` |
| **Lịch** | Crontab VPS: `30 6 * * * …_v10646_retrain_guard.py` |
| **Ghi** | `ml_retrain_guard_log` (+ LSTM → `training_history`) |
| **Lần gần nhất** | 02/08 06:30 `FRESH_SKIP`; lần train gần nhất cùng ngày 02:02 |
| **Ảnh hưởng số?** | Chỉ khi kích hoạt retrain — lúc đó giống A1 |
| **Sống?** | **Sống** — đúng vai trò backstop sau sự cố 10/05 (model đóng băng 21 ngày) |

### A3. `training_history` và cổng chặn model xấu

| Câu hỏi | Bằng chứng |
|---|---|
| **Writer duy nhất** | `_v10952_training_journal.ghi` |
| **Đọc bởi** | Script audit (`_v10951_…`, `_v10952_…`, …). **Không** có consumer trên đường dự đoán |
| **Cổng?** | `canh_bao_tut` chỉ in cảnh báo nếu AUC tụt >0,02. **Không rollback.** `model_manager.compare_models` tồn tại nhưng **chỉ CLI tay** |
| **Kết luận** | Sổ chất lượng **chạy**; cổng chặn **không tồn tại** (cố ý) |

### A4. Weight optimizer CN 03:00

| Câu hỏi | Bằng chứng |
|---|---|
| **File** | `scheduler._run_weight_optimizer` → `_run_optimizer_once.py` → `weight_optimizer.optimize_and_save` |
| **Lịch** | APScheduler CN 03:00; crontab `0 7 * * * …_v10648_weekly_guard.py` (ngưỡng 9 ngày) |
| **Ghi** | `app_settings` category=`learned_weights` keys `weights_MN/MT/MB`; marker `data/models/.last_optimizer_run` |
| **Lần gần nhất** | Marker **02/08 03:15:15**; weights updated_at khớp; guard 07:00 `FRESH` tuổi 0,16 ngày |
| **Ảnh hưởng số?** | **Có:** `statistical_analyzer.load_learned_weights` → `calculate_stat_score`. Cũng vào `knowledge_weights.get_optimizer_weights` |
| **Sống nhưng vô ích?** | Job sống. Metadata lift: MN **−4,75** · MT **−10,95** · MB **−8,47**. Đang chọn tổ hợp **ít tệ nhất trong tập âm** — chưa chứng minh giúp số công bố |

---

## 2B. Phía model LLM

### B1. LLM không huấn luyện lại

Không có fine-tune / adapter / job cập nhật trọng số Claude/GPT/Gemini/DeepSeek. “Học” = **nhồi prompt** từ DB.

### B2. Prompt được dựng thế nào

Đường: `gpt_analyzer.analyze_and_predict` (~6025):

1. `create_analysis_prompt` — đài hôm nay, nguồn, stats rút gọn, metrics.
2. `build_system_prompt` — system + ngưỡng.
3. `build_context_pack` (~4466) — WR/BT (thường bị `_deherd_strip_ranking` cắt), luật đào, **RULES-FIRST cuối pack**.
4. `REASONING_RULEBOOK` + (shadow) phase-first JSON contract.

**Cái gì đổi theo thời gian:** list số RULES-FIRST · thống kê mined · WR 14 ngày · luật promote/demote · Phase-15 vài dự đoán gần nhất của chính model.

### B3. Đào luật tuần → RULES-FIRST

| Câu hỏi | Bằng chứng |
|---|---|
| **File** | `weekly_rule_miner.run_weekly_mining` → `_seed_rules.main` (xoá+ghi `mined_rules`); chấm `mined_rule_eval.evaluate_mined_rules` |
| **Lịch** | T2 00:30 APScheduler; MRE 20:15; guard 07:00 |
| **Bảng** | Ghi `mined_rules` (105 active, 35/miền), `mining_log`, `mined_rule_effectiveness`. Đọc bởi `_rules_first_live_block` (`gpt_analyzer` ~4393) + soft boost `rule_engine` |
| **Lần gần nhất** | Mining `v2026W31` **27/07** SUCCESS 105 rules / 9 STRONG; MRE ngày mới **01/08** (15 dòng/ngày); tuần sau là **03/08** |
| **Ảnh hưởng số?** | **Có và mạnh qua prompt.** MB/MN: dòng lệnh **BẮT BUỘC chọn từ DANH SÁCH**. MT: ưu tiên mạnh. Thêm soft boost số vào điểm vote |
| **Hiệu quả?** | V10959: số thật trong list **12,4%** ≈ random 11%; model prompt pick **35,8%**. → ép hội tụ vào túi vô giá trị |

**Nguồn list ~11 số (đường đầy đủ):**

```
lottery_results
  → T2 00:30 _seed_rules (top-5 × 21 bucket miền×thứ)
  → mined_rules (is_active=1)
  → mỗi ngày _rules_first_live_block: lấy top luật bucket hôm nay,
    đọc đuôi đài nguồn từ lottery_results, hợp thành DANH SÁCH
  → nhồi cuối context pack → LLM buộc/ưu tiên chọn
```

### B4. `pattern_rules` / `rule_effectiveness` (cũ)

- `pattern_rules`: **160 dòng, `is_active=0` hết** (VPS 02/08).
- `rule_effectiveness`: **0 dòng**.
- Boost legacy **DISABLED V6.4** trong `scheduler.py`.
- `pattern_effectiveness`: còn **92** dòng, max **01/08** — có đường `get_learned_weights` trong code; mức ảnh hưởng thực tế cần A/B (chưa đo trong phiên này).

---

## 2C. Xếp hạng model

### C0. Ai thật sự quyết định model nào được dùng?

| Quyết định | Module | Thước |
|---|---|---|
| Roster 15 model official | `model_registry.OUTPUT_ELIGIBLE_MODELS` | Cờ tay / owner |
| Chọn model trong combo-super | `combo_super` filter + UNIFIED TOP-3 | **Hai thước lệch** (xem C2) |
| Số bạch thủ `/du-doan` | `generate_final_bundle` / vote trong `scheduler`+`main` | **win_rate có PARTIAL** |
| Vốn `/choi` | `money_board` | P&L — **không đổi số** |

Mọi bảng tên “progress / weakest / quality / shadow / edge_gate / three_layer” = **đo / xem**, không tự đổi roster.

### C1. Các bộ xếp hạng

#### `model_progress` (`_v10642_model_progress.py`)

- Thước: top1 ∈ union đuôi miền; `edge_pp` vs base 30d.
- Cron ~09:05 (APScheduler / playbook). Cập nhật **02/08**.
- Ảnh hưởng số: **Không** (API public + nuôi weakest).

**Mâu thuẫn vùng (cùng model, khác miền) — DB 02/08:**

| Model | MN | MT |
|---|---|---|
| `deepseek-v4-pro` | edge **−43,1** REDUCED_WATCHING | edge **+64,9** KEEP |
| `gemini-3.1-pro` | edge **−43,1** REDUCED_WATCHING | edge **+64,9** KEEP |

#### `weakest_model_watch` (`_v10645_weakest_watch.py`)

- Đọc `model_progress.edge_pp`; gắn nhãn SHADOW_PROMPT / RETRAIN_NUMERICAL.
- Cập nhật 02/08 09:15. **Không tự cắt / không tự retrain.**

#### `_v10871_model_quality_ledger`

- Paired lift vs pool từ **01/04**; cron 21:25; as_of **01/08**.
- `lstm` OFFICIAL bt_lift **−2,33** (MEASURE_MORE) trong khi vẫn nằm roster và được retrain hàng tuần.
- `gemini-3.5-flash` lift **+6,55** (mạnh nhất sổ) nhưng roster_kind **SHADOW** (đã rút official).
- Ảnh hưởng số: **Không** (CP-L6 tạm dừng tới 08/08).

#### `shadow_scoreboard` / three_layer / edge_gate

- Shadow scoreboard: cron 09:10, 81 lane — vệ sinh lane, không promote.
- Three-layer: chỉ API đọc, không ghi.
- Edge_gate 01/08 (90 ngày): cổng **đóng** cả 3 miền — MN −0,36 · MT −2,92 · MB −7,19 pp so “đánh bừa 00–99”.

### C2. Mâu thuẫn thước đo — ví dụ số thật (30 ngày, VPS 02/08)

**Win rate (có PARTIAL) vs bạch thủ `bt_hit` — 81 cặp model×miền giao nhau:**

| Model | Miền | WR% | BT% | Lệch |
|---|---|---:|---:|---:|
| claude-sonnet-4-6 | MN | 83,87 | 36,67 | **+47,2** |
| deepseek-reasoner | MN | 67,74 | 23,33 | **+44,4** |
| glm-5.2 | MN | 82,76 | 39,29 | **+43,5** |
| meta-learning | MN | 77,42 | 36,67 | **+40,8** |
| smart-ml | MN | 54,84 | 16,67 | **+38,2** |

Ý nghĩa: bộ vote official (thích WR) và bộ lọc combo theo bạch thủ (V10938) **có thể xếp cùng model ở hai thái cực**. Code đã ghi nhận khoảng lệch này tại `combo_super.py` ~298–312.

**Mâu thuẫn bên trong combo-super:**

- `_cham_diem_du_tuyen` / `get_dynamic_*_filter`: bạch thủ, bỏ mặc định 50%, cần ≥5 mẫu (V10936).
- `run_combo_super` UNIFIED TOP-3 (~1216–1224): vẫn `compute_adaptive_top_n` + fallback **`50.0`**.

**Mâu thuẫn “mạnh nhất đàn” vs “thắng ngẫu nhiên”:** combo/vote luôn chọn top tương đối; `edge_gate` nói cả 3 miền **dưới** đánh bừa — cổng đóng.

---

## 2D. Tích luỹ và học từ kết quả

### D1. Sau khi có kết quả xổ số, hệ làm gì?

```
Cào + verify (MN~16:30 / MT~17:30 / MB~18:30)
  ├─ cập nhật predictions.status / hit
  ├─ pattern_tracker (inline sau MB) → pattern_effectiveness
  ├─ 20:15 mined_rule_eval → mined_rule_effectiveness
  ├─ 20:20 model_daily_eval → bt_hit (nguồn combo)
  ├─ money_board score (vốn)
  └─ nhiều materializer shadow (chiều–tối)
```

### D2. Vòng phản hồi đóng kín thật sự?

| Vòng | Đóng kín? | Đường |
|---|---|---|
| Kết quả → train ML tuần → file model → số ML | **Có** | Chậm 1 tuần; chất lượng gần random ở MN/MB |
| Kết quả → MDE → lọc combo / trọng số vote | **Có** | Ngày T+1 |
| Kết quả → luật → RULES-FIRST / soft boost | **Có** | Nhưng tín hiệu list ≈ random → **đóng kín theo hướng hại** |
| Kết quả → optimizer → learned_weights → stats score | **Có** | Lift âm → đóng kín nhưng **không có lợi thế** |
| Kết quả → progress / weakest / quality / edge | **Không** (chỉ sổ) | Người đọc; không auto |
| Kết quả → champion_selector_shadow | **Gãy** | Cron còn chạy log 02/08; bảng dừng **15/06** |

**Kết luận thẳng:** có vài vòng đóng kín, nhưng vòng “học → ra số đúng hơn” **chưa chứng minh được**. Vòng RULES-FIRST đóng kín theo hướng **kéo phiếu về túi số vô giá trị**.

### D3. Bảng chính — ai ghi / ai đọc

| Bảng | Ghi | Đọc production? |
|---|---|---|
| `model_daily_eval` | scheduler 20:20 | **Có** — combo-super |
| `mined_rules` | weekly miner | **Có** — RULES-FIRST + soft boost |
| `mined_rule_effectiveness` | MRE 20:15 | Promote/demote + monitoring |
| `training_history` | journal | **Không** (audit) |
| `pattern_effectiveness` | pattern_tracker | Đường `get_learned_weights` — mức sống cần A/B |
| `pattern_rules` | legacy | **Không** (0 active) |
| `rule_effectiveness` | — | **Trống** |
| `daily_stats` | verify flags | Khoá trạng thái, không học |
| `app_settings learned_weights` | optimizer | **Có** — statistical_analyzer |

---

## 2E. Cơ chế chết / chạy vô ích

### E1. Chết cứng (đã tắt trong code)

| Cơ chế | Bằng chứng | Từ khi |
|---|---|---|
| V81 provider shadow pilot | `scheduler` early-return `DISABLED_V10644` | 31/05 |
| V101 shadow pilot | `DISABLED_V10659` | 31/05 |
| V104 materializer / phase B | DISABLED | 31/05 |
| V105 lane test control | DISABLED (zombie writer) | 31/05 |
| Optuna | Không lịch, không thư mục params VPS | — |
| Legacy pattern_rules boost | Comment DISABLED V6.4 | — |

Đây là chuỗi sự cố **10/05** (retrain + shadow V102–V105 rụng im lặng) rồi khoá cứng 31/05 — khớp tiền lệ owner nhắc.

### E2. Chạy (cron còn) nhưng kết quả không nuôi số / bảng đứng

| Cơ chế | Hiện tượng 02/08 |
|---|---|
| `champion_selector_shadow` | Crontab 06:25 + log mtime 02/08; **bảng max_date 15/06** |
| `model_progress` / `weakest` / `shadow_scoreboard` / quality ledger | Cập nhật đều; **0 ảnh hưởng roster/số** trong cửa sổ đóng băng |
| `model_latency_cost_audit_daily` | 4033 dòng, max **06/05** — chết ghi |
| `pnl_daily_summary` | 14 dòng, max **20/05** |
| Nhiều cron shadow V10733/737/789/801/803/821/829… | Ghi bảng shadow / log — không vào `/du-doan` trừ khi owner promote |

### E3. Sống nhưng kết quả “học” đang vô ích hoặc hại

1. **RULES-FIRST** — hại có số (V10959).
2. **Weight optimizer** — sống, lift âm.
3. **Retrain ML MN/MB** — sống, AUC ≈ 0,50; vẫn `output_eligible`.
4. **Đào luật** — sống; nuôi cơ chế hại ở trên; chưa đo lợi trên số công bố.

---

## 3. Chỗ đang hỏng hoặc vô ích (xếp mức nghiêm trọng)

| Mức | Vấn đề | Bằng chứng | Hệ quả nếu bỏ qua |
|---|---|---|---|
| **P0 — hại đang chạy** | RULES-FIRST ép list ~11 số | Hit thật 12,4% · pick 35,8% · hội tụ prompt | Nuốt phiếu, làm model LLM giống nhau trên túi rác |
| **P1 — học chạy ngược** | Optimizer chọn lift âm | MN −4,75 / MT −10,95 / MB −8,47 | Tinh chỉnh tầng thua nền vẫn nhồi vào scorer |
| **P1 — thước mâu thuẫn** | Vote theo WR, combo filter theo BT; UNIFIED còn 50% | Lệch tới +47 pp (sonnet MN); code ~1216–1224 | Chọn model “trúng lai rai”, không phải bạch thủ |
| **P2 — xếp hạng ảo** | progress/weakest/quality/edge không quyết định | Cron xanh, 0 promote | Owner tưởng hệ “tự tỉa” — thật ra không |
| **P2 — champion gãy nửa** | Cron sống, bảng đứng 15/06 | Log vs DB | Báo cáo “đang chọn champion” dễ tô hồng |
| **P2 — ML yếu vẫn official** | AUC ~0,50; không cổng AUC | training_history + registry | Tiếp tục bỏ slot vote cho tín hiệu gần random |
| **P3 — rác bảng chết** | cost audit / pnl summary / V81–V105 jobs đăng ký nhưng return | max_date 05/xx | Làm nhiễu kiểm soát lịch |
| **P3 — pattern_rules chết** | 160 inactive, rule_effectiveness=0 | DB | Tài liệu cũ vẫn gọi là “học luật thủ công” |

**Không tự sửa** trong phiên này (QD-014). Việc sau 08/08 đã có hướng: QD-016 bỏ bắt buộc RULES-FIRST (shadow), QD-017 A/B prompt, FU-228 đo từng cơ chế.

---

## 4. Sơ đồ đường đi dữ liệu (chữ)

```
lottery_results (KQ thật)
        │
        ├──► [CN 02:00] retrain ML ──► data/models/* ──► predictions (ML)
        │                                              │
        ├──► [CN 03:00] weight optimizer ──► app_settings.learned_weights
        │         └──► statistical_analyzer (điểm đuôi) ──► (nhồi prompt / scorer)
        │
        ├──► [T2 00:30] đào luật ──► mined_rules ──┬──► RULES-FIRST trong prompt ──► predictions (LLM)
        │         │                                └──► soft boost rule_engine ──► điểm vote
        │         └──► [20:15] mined_rule_effectiveness ──► promote/demote (tuần sau)
        │
        ├──► [verify + 20:20] model_daily_eval ──► combo-super chọn model ──► predictions (combo)
        │
        ├──► pattern_tracker ──► pattern_effectiveness ──► (?) get_learned_weights
        │
        └──► (sổ xem) model_progress / weakest / quality / edge_gate / shadow_* 
                 ✗ không nối vào final_bundles

predictions (15 output_eligible)
        │
        ├── vote có trọng số WR (+PARTIAL) + boost luật
        │         │
        ▼         ▼
   final_bundles  = số công bố /du-doan
        │
        └── money_board chỉ quyết VỐN /choi (số vẫn hiện)

CHỖ ĐỨT / HỎNG:
  (1) RULES-FIRST ← tín hiệu ≈ random nhưng ép LLM
  (2) Optimizer ← lift âm vẫn ghi đè weights
  (3) training_history / progress / quality / edge ← không có đường sửa roster tự động
  (4) champion_selector_shadow bảng đứng từ 15/06 dù cron còn
  (5) WR vs BT ← hai bộ quyết định production không cùng thước
```

---

## 5. Phụ lục — lệnh đối chiếu (chỉ đọc)

```bash
crontab -l | grep -E '10646|10648|10644|10871|10708|10725|retrain|optim|miner'
sqlite3 /root/Lottery_AI_Test/data/lottery_ai.db "
  SELECT date,region,model_type,round(auc,4),status FROM training_history
  WHERE date=(SELECT MAX(date) FROM training_history) ORDER BY region,auc DESC;"
sqlite3 ... "SELECT run_at,action,detail FROM ml_retrain_guard_log ORDER BY id DESC LIMIT 5;"
sqlite3 ... "SELECT setting_key,substr(setting_value,1,120),updated_at FROM app_settings WHERE category='learned_weights';"
ls -la /root/Lottery_AI_Test/data/models/.last_optimizer_run
```

Probe đã lưu: `artifacts/v10965_co_che_hoc/probe_live.json`, `probe5_lech.json`.

---

## 6. Kết luận một đoạn cho owner

Hệ đang **chạy khoảng 18 cơ chế** mang tên học / xếp hạng / tối ưu. Trong đó khoảng **7 cái thật sự đụng tới số công bố**; khoảng **8 cái chạy đều nhưng chỉ ghi sổ**; khoảng **6+ cái đã chết** hoặc bảng đứng. Vòng phản hồi **có đóng kín vài nhánh**, nhưng nhánh mạnh nhất lên LLM (RULES-FIRST) đang **đóng kín theo hướng hại**, nhánh optimizer **đóng kín với lift âm**, và nhánh ML official ở MN/MB **gần mức đoán bừa** vẫn được vote. Các bảng xếp hạng đẹp trên `/monitoring` **không quyết định** model nào được dùng — hai thứ quyết định là **roster tay** và **vote/combo với thước đo đang lệch nhau** (WR vs bạch thủ, lệch tới hơn 40 điểm phần trăm trên dữ liệu 30 ngày).
