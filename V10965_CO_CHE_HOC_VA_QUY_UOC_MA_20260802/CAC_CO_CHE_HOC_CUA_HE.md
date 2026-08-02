# Các cơ chế học của hệ — tài liệu kiểm soát (V10965)

> Viết ngày **02/08/2026** (giờ Việt Nam). Chỉ đọc code + kiểm VPS, không sửa đường chạy số.  
> Nguồn sự thật lúc đo: VPS `14.225.224.89`, DB `/root/Lottery_AI_Test/data/lottery_ai.db`, crontab + journal service `lottery`.

Owner hỏi nguyên văn:

> *"Rồi các cơ chế như học tập tích luỹ, xếp hạng, retrain của các model LLM và ML thì sao, em đã đào sâu hết cỡ chưa? Viết chi tiết cụ thể tất cả mọi thứ hiện đang code để kiểm soát, tổng hợp thật đầy đủ."*

Tài liệu này trả lời đúng câu đó: hệ đang **tự học bằng những cách nào**, cái nào **đang chạy thật**, cái nào **có ích / vô dụng / đang hại**.

---

## 0. Bảng tổng hợp nhanh

| Nhóm | Cơ chế | File chính | Giờ chạy (VN) | Đang sống? | Có đo hiệu quả chưa? |
|---|---|---|---|---|---|
| A | Huấn luyện lại 4 model ML (meta / xgb / rf / lstm) | `_v10646_retrain_guard.py`, `_retrain_all.py`, `scheduler._run_auto_retrain` | CN **02:00** (ép); cron **06:30** (backstop nếu model >8 ngày) | **Sống** — CN 02/08 02:02 RETRAINED; 06:30 FRESH_SKIP | Có ghi AUC; **chưa có cổng tự gỡ** (FU-213: phép so lệch cửa sổ) |
| A | Optuna chỉnh siêu tham số | `optuna_tune.py` | Không có lịch — chỉ chạy tay | **Chết / không dùng** — thư mục `optuna_params/` không có trên VPS | Không |
| B | “Học” của model đọc prompt | `gpt_analyzer.py` (dựng prompt) | Mỗi lần gọi dự đoán | **Sống** (nhồi dữ liệu vào prompt, không train lại) | Có đo một phần (V10959) |
| B | RULES-FIRST (ép chọn từ list luật) | `gpt_analyzer._rules_first_live_block` | Mỗi lần gọi, MB/MN bắt buộc | **Sống và đang làm hại** (list vô giá trị nhưng nuốt ~1/3 phiếu) | **Đã đo** V10959: số thật trong list 12,4% · model pick 35,8% |
| C | Đào luật tuần | `weekly_rule_miner.py` → `_seed_rules.py` | T2 **00:30**; backstop cron **07:00** | **Sống** — 105 luật active, bản `v2026W31`; tuổi ~6 ngày | Có bảng chấm ngày; **chưa đo “luật có giúp ra số đúng hơn không” trên đường công bố** |
| C | Chấm luật ngày | `mined_rule_eval.py` | **20:15** | **Sống** — 3173 dòng, ngày mới nhất 01/08 | Đo hit từng luật; chưa đo tác động lên số công bố |
| C | `pattern_rules` / `rule_effectiveness` cũ | `database.py` | — | **Chết về mặt điểm số** (boost tắt từ V6.4); còn 160 dòng legacy | Không dùng cho production |
| D | Tối ưu trọng số thống kê | `weight_optimizer.py` qua `_run_optimizer_once.py` | CN **03:00**; backstop **07:00** | **Sống** — 02/08 03:15 xong; marker tươi | Có lift — nhưng **lift tốt nhất đang âm** cả 3 miền |
| E | `model_progress` | `_v10642_model_progress.py` | cron **09:05** | **Sống** — 164 dòng, cập nhật 02/08 09:05 | Có số; kết quả chủ yếu để xem / weakest_watch |
| E | `shadow_scoreboard` | `_v10644_shadow_scoreboard.py` | cron **09:10** | **Sống** — 81 lane | Có verdict; 0 lần promote thật sự nhiều tháng (FU-192) |
| E | `weakest_model_watch` | `_v10645_weakest_watch.py` | cron **09:15** | **Sống** — 57 dòng | Đọc lại edge của progress; ít hành động thật |
| E | Sổ chất lượng model | `_v10871_model_quality_ledger.py` | cron **21:25** | **Sống** — 175 dòng, as_of 01/08 | Có; CP-L6 tạm dừng tới 08/08 |
| E | Lọc model combo-super (bạch thủ) | `combo_super._cham_diem_du_tuyen` | Trong luồng dự đoán | **Sống** (V10938) | Có; **lệch thước** với bộ tính trọng số (vẫn win-rate) |
| F | Cào kết quả + verify | `scheduler._run_auto_update` | MN ~16:30 · MT ~17:30 · MB ~18:30 | **Sống** | Nền tảng — không phải “học”, là tích luỹ dữ liệu |
| F | Chấm `model_daily_eval` | `scheduler._run_model_daily_eval` | **20:20** | **Sống** — 11334 dòng, ngày mới 01/08 | Có |
| F | Độ tin cậy runtime | `_persist_runtime_reliability_model_daily` | Ngay lúc gọi model | **Sống** | Có (độ trễ / lỗi), không phải độ chính xác số |

---

## A. Model ML học thế nào

### A.1 Sự thật ngắn

Bốn họ model **có huấn luyện lại thật**: `meta-learning`, `xgboost`, `random-forest`, `lstm`. Chúng học từ kết quả xổ số đã lưu trong bảng `lottery_results`, không đọc prompt.

### A.2 Dữ liệu và đặc trưng

**meta / xgboost / random-forest** — cùng một đường:

| Hạng mục | Giá trị thật trong code |
|---|---|
| File thu mẫu | `web/backend/meta_data_collector.py` → `collect_training_data()` |
| File train | `meta_learner.py` · `ml_models.py` · điều phối `_retrain_all.py` |
| Cửa sổ | **300 ngày** (`DAYS_BACK = 300`) |
| Đặc trưng | **28 cột** (điểm hội tụ, gan, tần suất, thứ trong tuần, lag, rolling…) |
| Mẫu mỗi ngày | top-30 đuôi + tối đa 10 đuôi ngoài top (mẫu âm) |
| Số mẫu VPS 02/08 | **2400 mẫu/miền** (cột `samples` trong `training_history`) |
| Chia train/test | Theo thời gian 80/20, không xáo; mẫu mới nặng hơn mẫu cũ |

**lstm** — đường riêng:

| Hạng mục | Giá trị |
|---|---|
| File | `lstm_data_builder.py` + `lstm_model.py:train_lstm()` |
| Cửa sổ | **500 ngày** (`max_dates=500`), nhìn lại **30 ngày** mỗi mẫu |
| Đầu vào | Chuỗi tần suất 100 đuôi × 30 ngày + 27 đặc trưng meta |
| Nhãn | Vector 100 đuôi trúng/không |
| Số mẫu ghi sổ 02/08 | cột `samples=100` (theo cách journal LSTM ghi; khác đơn vị với 2400 của ba model kia) |

Không có thư mục Optuna trên VPS → cả bốn họ đang dùng **tham số mặc định**, không phải bản đã tune.

### A.3 Lịch huấn luyện lại — đã kiểm trên VPS

Hai lớp:

1. **Chủ Nhật 02:00** — APScheduler trong service `lottery` gọi `_run_auto_retrain()` → subprocess `_v10646_retrain_guard.py --force` → gọi `_retrain_all.py` (meta/xgb/rf) rồi tự train LSTM 3 miền.
2. **Hằng ngày 06:30** — crontab VPS chạy cùng guard **không** `--force`. Chỉ train nếu model già hơn **8 ngày**.

Bằng chứng sống 02/08:

```
02:02  RETRAINED  forced · 0/12 lỗi · lstm MN/MT/MB ok
06:30  FRESH_SKIP  tuổi model 0,19 ngày
```

File model trên đĩa đều mtime **02/08 ~02:00–02:02**.

Lịch sử quan trọng: trước 15/07 (V10800) job CN 02:00 chết vì lỗi I/O in-process; suốt nhiều tuần hệ sống nhờ guard 06:30. Nay đã chuyển sang subprocess — CN 02/08 chạy được.

### A.4 Cổng chất lượng AUC — ghi được, không tự gỡ

- AUC ghi vào bảng `training_history` (V10952) + file `*_metrics.json`.
- So cũ↔mới: nếu AUC tụt quá **0,02** thì **chỉ cảnh báo**, **không** trả model cũ.
- Lý do cố ý: FU-213 — phép so đang lệch hai cửa sổ thời gian (cửa sổ 300 ngày trượt theo ngày train). Bật cổng tự gỡ khi phép so còn lệch sẽ nguy hiểm hơn không có cổng.

### A.5 AUC thật 02/08 (đối chiếu lại trên VPS — khớp số owner đã nêu)

| Miền | lstm | meta | random-forest | xgboost |
|---|---:|---:|---:|---:|
| **MT** | **0,5554** | **0,5394** | **0,5299** | **0,5236** |
| **MN** | 0,5137 | 0,4892 | 0,5039 | 0,4993 |
| **MB** | 0,5106 | 0,4768 | 0,5017 | 0,4839 |

Đọc thẳng: chỉ **MT** có AUC rõ trên 0,52. **MN và MB** gần mức đoán bừa (0,50). Meta MB 0,4768 còn **dưới** mức ngẫu nhiên.

---

## B. Model LLM (đọc prompt) “học” thế nào

### B.1 Nói thẳng

**Model LLM không học gì cả theo nghĩa huấn luyện lại.** Không có job nào cập nhật trọng số Claude/GPT/Gemini/DeepSeek. Mỗi ngày chúng chỉ **đọc prompt rồi trả lời**.

Cái hệ gọi là “học” nằm ở chỗ **prompt được nhồi thêm dữ liệu mới** (thống kê, luật đào, lịch sử thắng/thua của chính model đó). Đó là học trong ngữ cảnh (in-context), không phải học trong model.

### B.2 Prompt được dựng thế nào

Đường chính: `gpt_analyzer.analyze_and_predict()` ráp 3 khối:

1. **User prompt** — `create_analysis_prompt()`: đài hôm nay, dữ liệu miền nguồn, thống kê/gan rút gọn, chỉ số định lượng, 7 dự đoán gần nhất của chính model (Phase 15 “tự học”), khối kiến thức 1001 ngày, chính sách 7 lớp.
2. **System prompt** — `build_system_prompt()`.
3. **Context pack** — `build_context_pack()`: xếp hạng (thường bị cắt bởi de-herd), luật đào, rồi **RULES-FIRST**.

Độ dài: baseline cũ ~35.000 ký tự; hiện tại chắc lớn hơn (chưa lấy số sống từng call trong phiên này). Trace có field `prompt_total_chars`.

### B.3 RULES-FIRST — cơ chế “học” đang làm hại

Code: `gpt_analyzer._rules_first_live_block()` đọc `mined_rules` active của (miền, thứ), hợp đuôi nguồn thành danh sách (~11 số), rồi **viết lệnh** vào prompt:

- MB / MN: **BẮT BUỘC** chọn số chính từ danh sách.
- MT: ưu tiên mạnh.

Đo V10959 (đã ký sổ quyết định):

| Chỉ số | Giá trị | Ý nghĩa |
|---|---:|---|
| Số thật nằm trong list | **12,4%** | ≈ ngẫu nhiên (11/100) → list **không có lợi thế** |
| Model prompt chọn trong list | **35,8%** | Gần gấp 3 lần nền → model **nghe lời ép** |
| Model ML chọn trong list | **12,9%** | ML không đọc prompt → đúng nền |

Hệ quả: các model đọc prompt **hội tụ** vào cùng một túi số vô giá trị (trùng bạch thủ prompt↔prompt ~24–27% so với nền ~1%). Owner đã duyệt QD-016: sau 08/08 thử shadow **bỏ lệnh bắt buộc** (vẫn đưa list như gợi ý). Trong cửa sổ đóng băng QD-014 thì chưa đụng.

---

## C. Đào luật tự động

### C.1 Luồng đang chạy

```
T2 00:30  weekly_rule_miner.run_weekly_mining()
            └─ _seed_rules.main()  → xoá + ghi lại mined_rules (top 5 × 21 bucket)
Hằng ngày 20:15  mined_rule_eval.evaluate_mined_rules() → mined_rule_effectiveness
Tuần sau         promote nếu hit≥55% & mẫu≥8; demote nếu hit<25%
Cron 07:00       _v10648_weekly_guard — nếu mined_rules già >9 ngày thì chạy lại
```

VPS 02/08:

- `mined_rules`: **105 luật, 105 đang active**, bản `v2026W31`
- `mined_rule_effectiveness`: **3173 dòng**, ngày mới nhất **01/08**
- weekly_guard 07:00: mining tuổi **6,27 ngày** → FRESH (chưa cần backstop)

### C.2 Ai ghi / ai đọc

| Bảng | Ai ghi | Ai đọc |
|---|---|---|
| `mined_rules` | `_seed_rules` (tuần) + promote/demote | RULES-FIRST, context pack, eval ngày, API monitoring |
| `mined_rule_effectiveness` | `mined_rule_eval` (ngày) + backfill tuần | Cổng promote/demote, monitoring |
| `pattern_rules` (160 dòng) | API cũ | UI; **boost điểm đã tắt** |
| `rule_effectiveness` | Legacy | Thực tế đã bị thay bằng bảng mined_* |

### C.3 Luật có cải thiện kết quả công bố không?

**Chưa ai đo được câu trả lời đó trên đường ra số chính.**  
Hệ có đo “luật có trúng đuôi nguồn→đích không” (bảng effectiveness), và có vòng đời promote/demote. Nhưng chưa có báo cáo kiểu: *bật RULES-FIRST / nhồi luật vào prompt thì bạch thủ công bố tăng bao nhiêu điểm so với tắt*. Ngược lại, V10959 đã đo được mặt hại của việc **ép chọn từ list**.

Kết luận thẳng: đào luật **đang chạy và đang nuôi** RULES-FIRST; hiệu quả lên số công bố **chưa chứng minh được là dương**, trong khi mặt ép list **đã chứng minh là hại**.

---

## D. Tối ưu trọng số

### D.1 Nó làm gì

- File: `weight_optimizer.py`, chạy qua `_run_optimizer_once.py`.
- Lịch: CN **03:00** (APScheduler) + backstop cron **07:00** (`_v10648_weekly_guard`, ngưỡng 9 ngày).
- Tối ưu **4 trọng số tầng thống kê** từng miền: hội tụ / xu hướng / gan / độ mới. Không chọn model AI.
- Kết quả ghi `app_settings` category `learned_weights`, rồi `statistical_analyzer` dùng khi chấm điểm đuôi.

### D.2 Đang sống — đã kiểm

02/08 03:05–03:15 chạy xong cả 3 miền. Marker `.last_optimizer_run` = 03:15. Guard 07:00 thấy tuổi 0,16 ngày → FRESH.

Trọng số đang dùng:

| Miền | hội tụ | xu hướng | gan | độ mới | Lift tốt nhất khi tối ưu |
|---|---:|---:|---:|---:|---:|
| MN | 0,3 | 0,1 | 0,1 | 0,5 | **−4,75%** |
| MT | 0,1 | 0,2 | 0,3 | 0,4 | **−10,95%** |
| MB | 0,1 | 0,2 | 0,4 | 0,3 | **−8,47%** |

### D.3 Đánh giá thẳng

Job **chạy được** (không còn chết như giai đoạn V10648). Nhưng kết quả tối ưu đang chọn tổ hợp **ít tệ nhất trong tập lift âm**. Nghĩa là: bộ này đang tinh chỉnh một tầng thống kê mà backtest cho thấy **không vượt nền**. Chưa có đo forward chứng minh trọng số học được giúp số công bố đúng hơn so với trọng số mặc định cố định.

---

## E. Xếp hạng model

Năm bề mặt, **năm thước đo** — đây là chỗ dễ ra kết luận trái nhau.

| Bề mặt | Thước đo | Cửa sổ | Dùng để |
|---|---|---|---|
| `model_progress` | Top-1 trúng trong union đuôi miền, so nền | 30 ngày gần vs 30 trước | Trạng thái KEEP / WATCH_CUT… |
| `weakest_model_watch` | Đọc lại `edge_pp` của progress | như trên | Khoá AI/ML yếu (ý định shadow/retrain) |
| `shadow_scoreboard` | Cứu − phá (không phải tỉ lệ trúng) | Toàn lịch sử lane | Verdict promote / chết / lookahead |
| `v10871_model_quality_ledger` | Paired-lift bạch thủ + trúng-bất-kỳ | Từ 01/04 → nay | Quyết giữ/cắt (CP-L6, đang tạm dừng) |
| combo-super chọn model | **Bạch thủ** `bt_hit` blend 7+30 ngày | 7d×2 + 30d×1 | Chọn top model vào tổ hợp |

### E.1 Lệch thước ngay trong combo-super

- **Chọn model** (V10938): bạch thủ thuần, không cộng PARTIAL.
- **Tính trọng số khi gộp số**: vẫn `win_rate` có PARTIAL×0,5 và mặc định 50% khi thiếu dữ liệu (`_get_dynamic_win_rates`).

Cùng một file, hai nửa đường dùng hai thước. Dễ chọn đúng model theo bạch thủ rồi lại nhân điểm theo win-rate lệch.

### E.2 Trạng thái sống VPS 02/08

- progress: 164 dòng, cập nhật 09:05 hôm nay (ví dụ `combo-super` MN đang `WATCH_CUT`, edge −9,7pp).
- shadow_scoreboard: 81 lane.
- weakest: 57 dòng.
- quality ledger: 175 dòng, as_of 01/08 (cron 21:25 chưa chạy phiên tối nay).

FU-192 ghi nhận: shadow chạy lâu, **0 lần promote** vào official trong cửa sổ đo — bảng xếp hạng shadow chủ yếu **chạy cho có quan sát**, chưa đổi đường ra số.

---

## F. Tích luỹ dữ liệu và đánh giá

### F.1 Chuỗi ngày thường

| Giờ (mặc định) | Việc | Bảng |
|---|---|---|
| 04:00 | Dự đoán ML miễn phí | `predictions` |
| ~16:30 / 17:30 / 18:30 | Cào MN / MT / MB + verify | `lottery_results`, cập nhật `predictions` |
| 16:42 / 17:42 | AI predict MT / MB | `predictions` |
| T-chốt → FINAL | Khoá bundle | `final_bundles` |
| 20:15 | Chấm luật | `mined_rule_effectiveness` |
| 20:20 | Chấm model ngày | `model_daily_eval` |
| Lúc gọi model | Ghi độ trễ / lỗi | `runtime_reliability_model_daily` |

### F.2 Same-day khác nhau theo miền (bắt buộc ghi rõ)

| Miền | Nguồn same-day được dùng khi dự đoán |
|---|---|
| **MN** | **Không có** — chỉ D-1 trở về trước (MN xổ đầu) |
| **MT** | Được dùng **MN cùng ngày** (đã cào trước) |
| **MB** | Được dùng **MN(D) + MT(D)** |

Có lớp “anti-trap” soft: đuôi đã ra hết ở miền prior cùng ngày bị gắn nhãn FULL_SPENT (không cấm cứng, chỉ cảnh báo trong prompt).

### F.3 Bảng đánh giá chính

| Bảng | Vai trò |
|---|---|
| `predictions` | Mọi dự đoán + WIN/PARTIAL/LOSE |
| `final_bundles` | Số công bố / khoá cuối |
| `lottery_results` | Kết quả thật |
| `model_daily_eval` | Bạch thủ + hit ngày — nguồn combo-super / quality ledger |
| `runtime_reliability_model_daily` | Chạy có ổn không (không phải đúng số) |
| `training_history` | AUC lần train |

---

## Phần quan trọng nhất — cái nào có ích, cái nào chạy cho có, cái nào đang hại

### Đang có ích (hoặc ít nhất là hạ tầng cần giữ)

1. **Tích luỹ kết quả + verify + `model_daily_eval`** — không phải “học thông minh”, nhưng là nền để đo bất kỳ thứ gì khác. Không có cái này thì mọi xếp hạng đều giả.
2. **Huấn luyện lại ML có lịch + guard** — máy chạy thật, có sổ AUC. Ở **MT** AUC còn nhỉnh hơn nền một chút; MN/MB gần nền.
3. **Lọc combo-super theo bạch thủ (V10938)** — hướng đúng với cách owner tính tiền; chưa hoàn tất vì nửa trọng số vẫn win-rate.
4. **Sổ chất lượng `_v10871`** — thước đo cẩn thận hơn (paired-lift). Đang tạm dừng hành động cắt/promote theo QD-014 / CP-L6.

### Đang chạy cho có (chưa chứng minh giúp ra số đúng hơn)

1. **Tối ưu trọng số CN 03:00** — chạy ổn, nhưng lift tốt nhất **âm** cả 3 miền. Tinh chỉnh tầng đang thua nền.
2. **Đào luật tuần + chấm luật ngày** — máy chạy, bảng đầy, promote/demote có quy tắc; **chưa đo** được là chúng làm số công bố tốt hơn. Hiện chúng đang nuôi RULES-FIRST.
3. **`model_progress` / `weakest_watch` / `shadow_scoreboard`** — cập nhật đều; hành động thật lên official gần như không (0 promote, cắt model bị đóng băng).
4. **Phase 15 “tự học” trong prompt** (7 dự đoán gần nhất) — có nhồi, **chưa đo A/B** xem có giúp không (QD-017 sẽ đo sau 08/08).
5. **Optuna** — code còn, lịch không có, thư mục tham số không tồn tại trên VPS → coi như **không hoạt động**.

### Đang làm hại

1. **RULES-FIRST ép list ~11 số** — bằng chứng số: list không tốt hơn ngẫu nhiên nhưng nuốt ~35,8% phiếu model prompt, làm các model hội tụ sai. Đây là “học” theo nghĩa cập nhật prompt, nhưng cập nhật theo tín hiệu rác.

### Tóm một câu

Hệ **có rất nhiều máy tự chạy mang tên học / xếp hạng / tối ưu**, nhưng phần lớn chỉ **ghi số và tự xoay vòng**. Phần học ML thật sự yếu ở MN/MB, chỉ khá hơn chút ở MT. Phần “học” của LLM chủ yếu là nhồi prompt — và cơ chế ép luật đang **kéo phiếu về túi số vô giá trị**. Muốn kiểm soát thật, sau cửa sổ 08/08 cần đo A/B từng cơ chế (đặc biệt RULES-FIRST và trọng số thống kê) thay vì tin vào việc “job còn xanh trên cron”.

---

## Phụ lục — lệnh đối chiếu nhanh (chỉ đọc)

```bash
# Crontab học
crontab -l | grep -E '10642|10644|10645|10646|10648|10871|10708'

# AUC mới nhất
sqlite3 data/lottery_ai.db "SELECT region, model_type, round(auc,4), date FROM training_history WHERE date=(SELECT MAX(date) FROM training_history) ORDER BY region, auc DESC;"

# Guard gần nhất
sqlite3 data/lottery_ai.db "SELECT run_at, action FROM ml_retrain_guard_log ORDER BY id DESC LIMIT 5;"

# Luật
sqlite3 data/lottery_ai.db "SELECT COUNT(*), SUM(is_active), MAX(rule_version) FROM mined_rules;"
```
