# REPORT V11134 — A3 HOÀN TẤT · BA CỔNG · A4/A5/A6 · VÀ MỘT CÂU CỦA V11133 PHẢI RÚT LẠI

```
REPORT_VERSION        : V11134
REPORT_TITLE          : A3 score-level + paired McNemar · tách ba cổng (12/12 thử) ·
                        A4 hai lane shadow · A5 prompt context-only · A6 ML pure-math ·
                        RÚT LẠI verdict shadow của V11133 · đối chứng HẰNG SỐ
WORK_DATE_ICT         : 2026-08-28
TIMEZONE              : Asia/Ho_Chi_Minh / UTC+07:00
OWNER_DECISION        : prompt 43 R1 — "AFTER V11132 · CLOSE PHA B · COMPLETE A3 · A4→A6"
ACTOR_RUNTIME         : CLAUDE_CODE
PREVIOUS_PUBLIC_HEAD  : 48a4aa264d06fd8fc46edacf152442bcef240bcf
LABELS                : A3_DONE · GATES_DONE · A4_DONE · A5_DONE · A6_DONE ·
                        RETRACTION · NO_MUTATION
```

---

## 1 · TÓM TẮT

Ba việc lớn xong, và **một câu tôi phát hành sáng nay phải rút lại**.

🔴 **Rút lại:** `V11133` viết *«`SHADOW_CHANGED_FINAL = FALSE_IN_OBSERVED_14D_WINDOW`»*. **Quá mạnh.**
Tôi chỉ soi **một** kênh (`components[].model`) và kết luận cho **mọi** kênh. Có **kênh thứ hai**:
`gemini-3.5-flash` — model shadow — **đã vào chấm điểm của Combo** qua nhân tố `ai_confirm`
**3 lần** (12/08 · 13/08 · 23/08, đều MN), mỗi lần **rơi đúng vào số được chọn**, trọng số tới **2.000**.

🔴 **Đối chứng hằng số — kết quả nặng nhất phiên này.** Một **con số cố định** đạt trung bình
**33,87%**. FINAL hiện hành đạt **30,77%** — **thấp hơn**. Mọi biến thể đo được đều nằm trong dải mà
một hằng số cũng với tới.

**A3 xong đúng cách:** paired McNemar + permutation trên 10 cặp ⇒ **0 cặp có ý nghĩa**, kể cả
**trước** hiệu chỉnh đa so sánh. **8/13** model chứng minh được double-count điểm thật, chiếm
**12,1%** tổng điểm.

**Ba cổng tách xong** (12/12 thử), **A4 hai lane persist**, **A5 dump prompt thật** (MN 50.594 ký tự),
**A6 audit pure-math** — tất cả `LOCAL_ONLY`, **không mutation official path**.

---

## 2 · OWNER YÊU CẦU GÌ — NGUYÊN VĂN

Prompt 43 R1 tiếp nối, **28/08 khoảng 09:30 ICT**:

> *« Không mở Prompt 44. Không plan-only. Không dừng sau khi phát hành report. Không chuyển việc
> kỹ thuật Agent tự xử được sang Owner. »*
>
> *« Không ghi "13/18 model thực sự được đếm hai lần vào FINAL". Tạm ghi 13/18
> DUPLICATE_LINEAGE_PATHS. Chỉ nhóm ACTUAL_DOUBLE_COUNT_NONZERO mới được gọi "đếm hai lần thật". »*
>
> *« Không chỉ so CI riêng lẻ. Vì cùng 273 lượt, phải xuất McNemar hoặc paired
> bootstrap/permutation phù hợp. »*
>
> *« 72/273 = 26,4% đổi top-1 chỉ chứng minh architecture sensitivity. »*
>
> *« source_weights={} và meta={} không chứng minh production dùng 0 model. »*
>
> *« Cổng phải đọc structured object/JSON, cấm regex stdout làm verdict. »*
>
> *« N≥1 official hợp lệ: vẫn output DEGRADED. N=0: mới không output. Cấm lấy SHADOW bù. »*
>
> *« Điều gì chưa rõ phải ghi NOT_VERIFIED. »*
>
> *« Báo tiến độ: ĐANG LÀM → ĐÃ XONG → EVIDENCE → VIỆC KẾ. »*

---

## 3 · 🔴 RÚT LẠI — `PRJ-RETRACTION-001`, ĐỦ BỐN PHẦN

### 3.1 · Rút lại #1 — verdict shadow của `V11133` (phát hành **sáng nay**)

**① Chỗ gốc.** `V11133_PHA_B_LIVE_PROOF_RAW_EVIDENCE_20260828/REPORT_V11133.md`, commit
`48a4aa2`, phát hành **28/08 lúc ~10:20 ICT**. Nằm ở **mục 1**, **dòng `TanPhatAI cần làm:`**, và
**CONVERSATION_CONTEXT mục 5**.

**② Nguyên văn câu sai.**

> *« Nhãn đúng là `NO_OBSERVED_SHADOW_SCORE_CONTRIBUTION_14D` và
> `SHADOW_CHANGED_FINAL = FALSE_IN_OBSERVED_14D_WINDOW` »*

**③ Điều đúng, kèm phép đo tái lập được.**

Câu trên **chỉ đúng cho một kênh**: `final_bundles.score_breakdown[].components[].model`.
Ở kênh đó, 0/871 vẫn **đúng**. Nhưng có **hai kênh nữa** tôi chưa soi:

| kênh | nguồn | shadow xuất hiện |
|---|---|---|
| `components[].model` | `final_bundles.source_predictions_json` | 🟢 **0/871** — câu cũ đúng ở đây |
| **`factors[].detail` kiểu `ai_confirm`** | `predictions.reasoning_json` của `combo-super` | 🔴 **3 ca sau 01/08** |
| **`number_voters`** | **`predictions.analysis_text`** của `combo-super` | 🔴 `gemini-3.5-flash` ×4 · `gemini-3.6-flash` ×2 |

Ba ca rò rỉ, tái lập được từng ca:

```
2026-08-12 MN  số=82  gemini-3.5-flash  là số được chọn: CÓ  weight=2.000
2026-08-13 MN  số=73  gemini-3.5-flash  là số được chọn: CÓ  weight=0.524
2026-08-23 MN  số=73  gemini-3.5-flash  là số được chọn: CÓ  weight=2.000
```

Nguyên văn trong manifest 23/08 MN:

```json
{"type": "ai_confirm", "weight": 2.0, "detail": "1 AI model xác nhận (gemini-3.5-flash)"}
"dynamic_wr": {"xgboost": 38.8, "random-forest": 44.2, "gemini-3.5-flash": 51.3}
```

**Nhãn đúng thay thế:**

- `SHADOW_ENTERED_COMBO_SCORING_VIA_AI_CONFIRM = TRUE` — **3 ca xác nhận**, 12/08–23/08, đều MN.
- `SHADOW_CHANGED_FINAL` = 🟡 **`NOT_EXCLUDED`** trong cửa sổ đó — **không phải `FALSE`**.
- `NO_OBSERVED_SHADOW_SCORE_CONTRIBUTION_14D` — **giữ**, nhưng phải ghi kèm **«ở kênh
  `components[].model`»**, không được để trần.

**Có lật top-1 không?** 🟡 **`NOT_VERIFIED`.** Ca 23/08 MN có biên độ `top1 − top2 = 3.0380`,
trọng số `ai_confirm` là `2.000` — nhưng `weight` và `final_score` là **hai thang đo khác nhau**,
cấm suy trực tiếp. Muốn biết phải chạy lại hàm chấm điểm với factor đó bị gỡ.

**④ Quyết định nào đã dựa trên số sai.** 🟢 **Chưa có quyết định nào.** Câu đó mới phát hành sáng
nay, chưa dùng làm căn cứ cắt/promote/đổi FINAL. **Nhưng** nếu để nguyên, nó sẽ là căn cứ để đóng
`FU` theo dõi rò rỉ shadow — nên phải sửa ngay.

### 3.2 · Rút lại #2 — hai con số của `V11132`

**① Chỗ gốc.** `V11132_A3_DOUBLE_COUNT_VA_CONG_CHONG_VACUOUS_20260828/REPORT_V11132.md`,
commit `afa35cc`, mục **4.1** và **4.2**.

**② Nguyên văn.**

> *« 125/273 manifest có `numbers` không phải `dict` nên rơi ra »*
> *« Kiểm chứng trên 62 manifest: `max(final_score)` KHÁC `main_numbers[0]` ở `0` ca (0%) »*

**③ Điều đúng.** Đo lại trên **toàn bộ** bản ghi `combo-super` official, cửa sổ 29/05–27/08:

| | con số cũ | đo lại đầy đủ |
|---|---|---|
| `numbers` **không phải dict** | *«125»* | 🔴 **0** — không có bản ghi nào |
| `numbers` là dict nhưng **RỖNG** | không nêu | 🟢 **125** — đây mới là điều đã xảy ra |
| mẫu kiểm chứng | 62 | **148** |
| `max(final_score)` **khớp** `main_numbers[0]` | 62/62 = 100% | **145/148 = 98,0%** |
| **lệch** | 0 | **3 = 2,0%** |

⇒ Kết luận *«phương pháp tái lập được lựa chọn của Combo»* **vẫn đúng** (98%), nhưng chữ
**«không phải dict»** là **sai** — đúng phải là **«rỗng»**. Hai chuyện khác nhau: một cái là sai
kiểu dữ liệu, một cái là không có dữ liệu.

**④ Quyết định dựa vào.** Con số 62/62 từng là căn cứ để tôi ghi *«lỗi là căn dữ liệu, phương pháp
đúng»*. Kết luận đó **vẫn đứng** với con số đúng 145/148.

### 3.3 · Sửa nhãn — `13/18` theo lệnh owner

Owner bắt tạm ghi `DUPLICATE_LINEAGE_PATHS`. Đo xong, con số **tách ra được**:

| nhãn | số model | căn cứ |
|---|---|---|
| **`DUPLICATE_LINEAGE` cấu hình** | **13** | đúng bằng pool `combo_super.ML_MODELS` (4) + `AI_MODELS` (9) |
| 🔴 **`ACTUAL_DOUBLE_COUNT_NONZERO`** | **8** | direct ≠ 0 **VÀ** indirect ≠ 0 trên **cùng một candidate**, truy lineage thật |
| `DUPLICATE_LINEAGE_ONLY` | 3 | `gemini-2.5-flash` · `glm-5.1` · `gpt-oss-120b` |
| `CONFIGURED_BUT_NO_CONTRIBUTION` | 1 | `combo-no-token` (`output_eligible=False`) |
| `SHADOW_NO_OFFICIAL_CONTRIBUTION` | 1 | `gpt-5-mini` — **cảnh báo trước đây là ĐÚNG** |

⇒ **`13/18` là SAI ở cả hai đầu.** Đúng là: **13 duplicate lineage · 8 double-count điểm thật**.

Tôi tự đo bằng một tiêu chí **lỏng hơn** (đồng-xuất-hiện base + aggregator trên cùng số) và ra
**12**. Tiêu chí đó **kém hơn**: đồng xuất hiện **không** chứng minh tín hiệu của model đó chảy qua
aggregator. Con số dùng được là **8**, vì nó truy lineage thật qua
`predictions.analysis_text['rf_numbers' | 'xgboost_numbers' | 'lstm_numbers']`.

**Sửa thêm một phân loại của chính tôi:** `meta-learning` tôi xếp là *aggregator*. **Sai** —
`analysis_text` cho thấy nó là **model nền thật** (lgbm, `model_auc`, `top_features`).

---

## 4 · ĐÀO BỚI / PHÁT HIỆN — LIỆT KÊ ĐỦ

### 4.1 · 🔴 ĐỐI CHỨNG HẰNG SỐ — phát hiện nặng nhất phiên này

Câu hỏi: *một con số cố định, chọn trước, không nhìn dữ liệu — đạt bao nhiêu?*

| | hit rate trên **cùng 273 lượt** |
|---|---|
| **trung bình 100 hằng số** | **33,87%** ← đây mới là **nền đúng** |
| `M0_CURRENT_OFFICIAL` (FINAL đang chạy) | 🔴 **30,77%** |
| `TOTAL_LEAN_SHADOW` (A4) | 35,16% |
| `COMBO_CURRENT` | 35,53% |
| hằng số `'00'` | 35,16% |
| hằng số **tệ nhất** `'15'` | 27,11% |
| hằng số **tốt nhất** `'54'` | 43,96% ⚠️ *chọn sau khi biết kết quả = thiên vị, không dùng được* |

**FINAL hiện hành thấp hơn trung bình một hằng số.** Và biến thể tốt nhất tôi dựng được
(35,53%) **không vượt** hằng số `'00'` (35,16%) một cách có ý nghĩa.

⚠️ **Đọc cho đúng:** phép này **không** nói hệ thống vô dụng. Nó nói **thước đo hiện tại
(bạch thủ hit) không phân biệt được kỹ năng với may rủi ở cỡ mẫu này** — nền 33,87% quá cao và
phương sai quá lớn. Muốn đo được kỹ năng phải đổi thước hoặc tăng mẫu, chứ không phải tinh chỉnh
ranking.

### 4.2 · A3 · Paired test — làm đúng phương pháp

Cách cũ so **CI riêng lẻ** giữa các biến thể đo trên **cùng** 273 lượt — sai phương pháp.
Nay: **McNemar exact + permutation (seed `20260828`, 20.000 lần, ghi TRƯỚC khi đọc)**, 10 cặp,
Bonferroni `α = 0,001`.

| cặp | A đúng/B sai | A sai/B đúng | Δ điểm | McNemar | permutation |
|---|---|---|---|---|---|
| `COMBO_CURRENT` vs `M0` | 51 | 38 | **+4,76** | 0,2031 | 0,2077 |
| `M0` vs `TOTAL_LEAN_SHADOW` | 23 | 35 | −4,40 | 0,1480 | 0,1523 |
| `COMBO_VNEXT` vs `TOTAL_LEAN` | 23 | 34 | −4,03 | 0,1849 | 0,1831 |
| **`COMBO_CURRENT` vs `TOTAL_LEAN_SHADOW`** | 46 | 45 | **+0,37** | **1,0000** | **1,0000** |
| *(6 cặp còn lại)* | | | | 0,2713 – 1,0000 | |

🔴 **0/10 cặp có ý nghĩa** — và **cả trước hiệu chỉnh** đa so sánh (p thô nhỏ nhất 0,2031).

🟡 **Điều đáng chú ý nhất:** `COMBO_CURRENT` vs `TOTAL_LEAN_SHADOW` cho `p = 1,0000` với **46 vs 45**
ca bất đồng. Nghĩa là: **bỏ sạch double-count thì hệ đổi lựa chọn ở 91/273 lượt, mà kết quả
không nhúc nhích**. Bất đồng nhiều, hiệu số bằng không.

### 4.3 · A3 · Double-count điểm thật

| | |
|---|---|
| cửa sổ | 15/08 – 28/08 · 40 bundle · 399 candidate · **871 component** |
| bundle lỗi parse / rỗng component | **0 / 0** *(đối chứng dương đạt)* |
| tỉ trọng điểm của 4 aggregator | **18,8%** (4,0841 / 21,6824) |
| 🔴 **tỉ trọng điểm bị đếm hai lần** | **12,1%** (2,6314 / 21,6824) |
| 🔴 **bạch thủ có ít nhất 1 model đếm hai lần** | **20/40 = 50%** |

Bốn model nặng nhất — đường thứ hai là `smart-ml`/`smart-ensemble`, **không** phải `combo-super`:

| model | direct | cùng-candidate hai đường | điểm gián tiếp |
|---|---|---|---|
| `random-forest` | 64 | **43 candidate / 33 ngày-miền** | 1,2953 |
| `xgboost` | 70 | 40 / 32 | 1,1849 |
| `lstm` | 39 | 24 / 17 | 0,3496 |
| `meta-learning` | 54 | 23 / 18 | 0,4502 |

Bốn LLM (`deepseek-reasoner` 6 · `claude-opus-4-6` 4 · `claude-sonnet-4-6` 3 · `gemini-2.5-pro` 1)
đi qua `combo-super` với **n rất nhỏ**. Riêng `gemini-2.5-pro` **n=1** ⇒ `RM-04`: **chưa được phép
kết luận** về độ lớn; chỉ kết luận được **hiện tượng có tồn tại**.

### 4.4 · A3 · Family dedupe — tách kết cục

Tái lập **chính xác** 72/273 = 26,4%. Tách bốn ô:

```
đúng->đúng 75 | đúng->sai 14 | sai->đúng 20 | sai->sai 164
NET = +6 ca = +2,20 điểm · CI95 [-1,98 .. +6,38] · McNemar p = 0,3915
```

Ba điều làm yếu con số 26,4%:

1. **38/72 = 52,8%** số ca «đổi lựa chọn» **không đổi kết cục** — đổi số nhưng cả hai đều trượt.
2. **Net effect đổi dấu** (`+6 → −5`) chỉ vì đổi quy ước phá hoà. Con số «72» cũng trôi **72–81**
   tuỳ thứ tự đọc. Luật *«giữ model đầu tiên của mỗi family»* là **tuỳ tiện**.
3. Bản đồ family gốc **bỏ sót** `gpt-5-mini` (có mặt 192/273 lượt) và `claude-opus-4-20250514`
   (54/273) — chúng bị coi là SOLO nên không bao giờ bị gộp.

⇒ **26,4% chứng minh hệ NHẠY VỚI KIẾN TRÚC**, **không** phải lợi ích độ chính xác.

### 4.5 · A3 · Ablation `meta-learning` — làm lại được

Nguồn cũ **sai hẳn**: `predictions.reasoning_json` của `combo-super` có `factors[]` **chỉ có
trường `type`** với 6 giá trị (`cross_region` 485 · `ml_consensus` 471 · `ai_confirm` 395 ·
`hot_cold` 39 · `manual_rule` 17 · `hot_streak` 7) — **không có tên model nào**. Ablation trên
object đó là **bất khả thi về cấu trúc**, không phải lỗi truy vấn.

Làm lại trên `final_bundles.score_breakdown[].components[].model`, **n = 427** bundle
(MN 144 · MT 141 · MB 142, 06/04 → 27/08), **reproduction check 427/427 = 100%**:

| | |
|---|---|
| bỏ `meta-learning` đổi top-1 | **47/427 = 11,0%** |
| hit trước → sau | 33,26% → 32,32% |
| paired delta | **−0,94pp** · CI95 `[−2,81 ; +0,94]` **bao trùm 0** |
| McNemar | b=11 · c=7 · **p = 0,4807** |
| biến thể B (thuần tổng component) | **+0,00pp** · p = 1,0000 |
| **verdict** | 🟡 **`INSUFFICIENT_POWER`** |

⛔ **Cấm đọc −0,94pp là «meta-learning có hại».** Đối chứng: gỡ **bất kỳ** model nào cũng tạo delta
trong dải `−0,94pp .. +1,87pp`. Và đối chứng âm — gỡ một model **không tồn tại** — cho đúng
`0/427` đổi, `+0,00pp`.

⇒ Con số cũ *«147/273 = 53,8%»* và *«41,22%»*: 🔴 **BÁC BỎ** hoàn toàn.

🔴 **Phát hiện phụ, đổi cách đọc mọi số liệu Combo:** **77/427 = 18,0%** ca có `bach_thu` **công bố
khác** số thắng cuộc bỏ phiếu — bị **bốn module ghi đè** sau bỏ phiếu (V10640/V10767/V10789/V10790),
và bốn module đó **không đọc** `score_breakdown`.

### 4.6 · A5 · LLM context-only — dump prompt THẬT

Hàm đang serve: `analyze_and_predict` (`gpt_analyzer.py:6272`, sha256 `0d2be324…`). Dump bằng venv
production, dữ liệu thật:

```
MN 50.594 ký tự · MT 49.662 · MB 53.834      (system + user)
hash 4 bảng khoá PRE = POST qua 2 lần chạy  => chứng minh phép đo CHỈ ĐỌC
```

**Quét ngược ô nhiễm trên prompt PHÁT RA** (không phải trên tài liệu):

| nhóm | khối | dòng |
|---|---|---|
| A — top-list / con số cứng | 20 | 124 |
| B — win-rate / độ tin cậy | 11 | 120 |
| D — xếp hạng model | 4 | 95 |
| **C — TOTAL/FINAL** | 🟢 **0** | **0** |
| **tổng** | **35** | **339** |

Phân loại mã nguồn (`RM-09`, 74 điểm chạm): `TRONG_PROMPT` **6** · `GHI_VÀO_PROMPT` **42** ·
`CODE` **16** · `CHÚ_THÍCH` **10**.

🔴 **Ba phát hiện nặng:**

1. **De-herding `V10768` làm NỬA VỜI** — nó cắt khối `### BT MODEL RANKING` khỏi context pack
   (mất 1.091–1.204 ký tự) **nhưng không đụng** bảng xếp hạng 28–30 model + win-rate mà chính
   `create_analysis_prompt` bơm vào **thân prompt** (`gpt_analyzer.py:2830-2833`, 1.263–1.340 ký tự).
   ⇒ **De-herd gỡ ÍT HƠN lượng nó để lại.**
2. **`PRJ_PROMPT_CONTRADICTS` xác nhận** — cùng một prompt vừa ra lệnh
   *«AI nên ưu tiên patterns từ models có win_rate cao hơn»* (dòng 2833) vừa có
   **ANTI-HERDING DIRECTIVE** và mục 22/23 ANTI-HERDING của RULEBOOK.
3. **Prompt tự mâu thuẫn về cùng một con số** — cả ba miền: số **`03`** đồng thời là
   *«ĐỀ XUẤT PYTHON»* hạng 1 (score=16), nằm trong *«SỐ NÊN TRÁNH»* kèm *«AI KHÔNG NÊN chọn»*,
   và ở MN/MT còn là *«CONV x4 TRAP RISK»*. **Ba mệnh lệnh loại trừ nhau về cùng một số.**

**Ba mệnh lệnh mồ côi, BA nguyên nhân khác nhau** (đo 5 ngày × 3 miền = 15 lượt — một phép quét
**một ngày** sẽ báo cả ba như nhau, đúng lỗi `RM-09` cấm):

| mệnh lệnh | mồ côi | nguyên nhân |
|---|---|---|
| `BT MODEL RANKING` | **15/15** | cơ cấu — khối bị de-herd cắt |
| `WEEKLY LIVINGNESS` | **0/15** | `V11014` ép cứng `_live_rows=[]` mà **không gỡ mệnh lệnh** — treo **21 ngày** |
| `RULE TAILS` | 10/15 | **có điều kiện** — vắng 10, có thật 5 |

🟢 **Bác bỏ con số cũ:** *«5 chỗ bơm TOTAL/FINAL»* **không tái lập được** — đếm trên cả 3 prompt +
`SYSTEM_PROMPT` + `REASONING_RULEBOOK`: `TOTAL`=0 · `FINAL`=0 · `bundle`=0.

### 4.7 · A6 · ML pure-math

🟢 **Cả 6 model ĐẠT hợp đồng «không đọc output LLM».** Quét toàn bộ import closure trên VPS: không
điểm nào đọc `predictions` của LLM, `reasoning_json`, `final_bundles`, `gpt_analyzer` hay
`combo_super`. Nguồn feature duy nhất là `lottery_results` với ràng buộc `date < target_date`.
Không rò rỉ dữ liệu tương lai — ba chặn độc lập.

🔴 **Con số «8,2 candidate» KHÔNG tái lập được.** Đo lại 30 ngày (90 ô miền-ngày):

| pool | ứng viên phân biệt |
|---|---|
| 6 model ML (12 suất) | **6,92** |
| 4 ML base (8 suất) | 5,98 |
| 3 base độc lập (6 suất) | 5,39 |
| ML6 **+ `combo-super`** | 8,59 ← **8,x chỉ xuất hiện khi gộp `combo-super`** |

Mà `combo-super` **không phải pure-ML** (nó chứa 5 model LLM) ⇒ gộp nó vào «pool ML» là **lỗi
phân loại**. Ổn định qua mọi cửa sổ 7/14/30/45/69 ngày (6,64–6,95).

🔴 **Nút thắt lớn nhất là MỘT DÒNG CODE:** `database.py:2463-2464` cắt cứng `main_numbers[:2]`.
Bốn model base thực sự sinh **13,77** ứng viên phân biệt ở top-5; sau khi cắt còn **6,34** —
**mất 54%**.

🔴 **Nút thắt thứ hai:** `xgboost` / `random-forest` / `meta-learning` dùng **chung một tập 30 ứng
viên** (`meta_predict.py:129 all_scores[:30]`), **chung 28 feature**, **chung một file CSV huấn
luyện**. Trùng top-1 **23–33%**. **Chỉ `lstm` là trực giao thật** (trùng top-1 **0–1,1%**).

🔴 **AUC cả ba model MB đều DƯỚI 0,5**: `meta-learning` 0,4845 · `xgboost` 0,4765 ·
`random-forest` 0,4736 — **kém hơn tung đồng xu** trên chính tập holdout của chúng.

🔴 **Chỉ số LSTM bị thổi phồng**: checkpoint được **chọn theo loss trên chính tập test** dùng để
chấm nó (`lstm_model.py:210-217`).

### 4.8 · Ba cổng tách lớp — 12/12 thử ĐẠT

| cổng | nguồn | rỗng nghĩa là gì | được chặn output không |
|---|---|---|---|
| `ELIGIBILITY_GATE` | giá trị trả về hàm eligibility | thật sự không có nguồn | **CÓ** — qua `N` |
| `MANIFEST_OBSERVABILITY_GATE` | manifest đã lưu | **chỉ** telemetry thiếu | 🔴 **KHÔNG BAO GIỜ** |
| `CONTRIBUTION_GATE` | `score_breakdown[].components[]` | không truy được đóng góp | **KHÔNG** — chỉ cảnh báo |

Mười phép owner bắt buộc + hai phép META, **12/12 ĐẠT**:

| # | phép | kết quả |
|---|---|---|
| ① | eligibility RỖNG ⇒ gate FAIL + `NO_OUTPUT` | 🟢 |
| ② | **manifest rỗng ⇒ KHÔNG chặn output, observability đỏ RIÊNG** | 🟢 `DEGRADED` + `OBSERVABILITY_MISSING` |
| ③ | `N=1` official ⇒ **DEGRADED** (vẫn output) | 🟢 |
| ④ | chỉ có shadow ⇒ `N=0` ⇒ `NO_OUTPUT` (**cấm bù bằng shadow**) | 🟢 |
| ⑤ | official + còn shadow ⇒ FAIL, shadow **không vào `N`** | 🟢 N=16 |
| ⑥ | chỉ ML / chỉ LLM ⇒ FAIL hybrid, `DEGRADED` chứ không chặn | 🟢 |
| ⑦ | model inactive hoặc ID lạ ⇒ FAIL | 🟢 |
| ⑧ | contribution trace rỗng ⇒ gate FAIL, **không** chặn output | 🟢 |
| ⑨ | **ALIAS shadow** (`openai/GPT-5-Mini:free`) ⇒ canonical join bắt được | 🟢 |
| ⑩ | fixture đầy đủ ⇒ ba cổng PASS + `NORMAL` | 🟢 |
| **META-A** | cổng gộp cũ suy nhầm «chặn»; ba cổng tách ⇒ vẫn output | 🟢 |
| **META-B** | bundle rỗng **không lọt** kể cả khi nới một vế dương | 🟢 |

**Chạy trên dữ liệu production thật** — cả ba miền: `ELIGIBILITY` **PASS** (16 · 0 shadow · 4 ML ·
8 LLM), `CONTRIBUTION` **PASS**, `MANIFEST` **`OBSERVABILITY_MISSING`**, quyết định **`DEGRADED`**
với lý do ghi rõ *«manifest thiếu telemetry — KHÔNG chặn output»*.

### 4.9 · A4 · Hai lane shadow đã persist

Lọc cửa sổ chọn: 7.373 dòng thô → bỏ **3.203** shadow/eval → bỏ **0** sau giờ khoá → **4.158** dòng,
**273 lượt**.

| lane | n | hit rate | CI99 |
|---|---|---|---|
| `TOTAL_LEAN_SHADOW` | 273 | **35,16%** | `[28,15 – 42,88]` |
| `COMBO_SUPER_VNEXT_SHADOW` | 273 | 31,14% | `[24,44 – 38,73]` |
| `COMBO_VNEXT` *(comparator bỏ meta-learning)* | 273 | 32,60% | `[25,78 – 40,25]` |

Persist đủ trường owner yêu cầu: `lane_version` · `roster_version` · `input_manifest` ·
`candidate_provenance` · `generated_at` · `cutoff` · `score_breakdown` · `contribution_trace` ·
`degraded_reason` · `stop_rule` · `rollback_version` · `evidence_class=RETROSPECTIVE_SHADOW`.
Ba tệp, 273 bản ghi mỗi tệp, **không** vào Git (đúng luật cấm runtime artifact).

### 4.10 · Đối chứng cho phép lọc «tạo sau giờ khoá» — và một phát hiện ngoài dự kiến

Phép lọc đó loại **0 dòng**. Đúng bẫy `RM-15`: bộ lọc không loại gì **có thể** là bộ lọc vô hiệu.
Đối chứng: hạ ngưỡng xuống `06:00` thì nó bắt **991 dòng MT** và **1.391 dòng MB** ⇒ **cơ chế chạy
thật**, và 0 là **số đúng**.

🟡 **Nhưng đối chứng lộ ra một thứ khác:**

| miền | khoá | biên §55 (2 phút) | ngày vượt **biên** | ngày vượt **khoá** | muộn nhất |
|---|---|---|---|---|---|
| MN | 15:45 | 15:43 | 0/91 | **0/91** | 15:15 |
| **MT** | 16:58 | 16:56 | 🟡 **1/91** | **0/91** | **16:57** |
| MB | 17:58 | 17:56 | 0/91 | **0/91** | 17:45 |

Ngày **13/08/2026**, `combo-super` MT ghi lúc **16:57** — cách khoá **1 phút**, trong khi §55 quy
định biên an toàn **2 phút**. **Chưa từng trễ hạn**, nhưng đệm mỏng hơn quy định 1 lần.

### 4.11 · Nguyên nhân gốc của rò rỉ shadow — định vị chính xác

```
combo_super.py:115    {'id': 'gemini-3.5-flash', ...}   <-- SHADOW, KHÔNG bị comment
combo_super.py:116    {'id': 'gemini-3.6-flash', ...}   <-- SHADOW, KHÔNG bị comment
combo_super.py:118  # {'id': 'gpt-5-mini', ...}         <-- đã comment 01/08 (V10931)
```

Chuỗi ảnh hưởng, đọc từ code thật:

```
_ti_le_bach_thu (:318)  ->  _chon_top (:395,:465)  ->  allowed_models (:1291)
     ->  allowed_ai_ids (:1302)  ->  filtered_ai (:1364)  ->  ai_results
     ->  ai_details  ->  factor "ai_confirm" (:2432)  ->  điểm của số
```

Bản vá `V11130` nằm **đúng đầu chuỗi** (`_ti_le_bach_thu`), nên nó **bịt cả kênh này**. Khớp với
dữ liệu: **3 ca rò rỉ 12/08–23/08 · 0 ca từ 28/08**.

⚠️ Nhưng đó là **phòng thủ một lớp**. Hai tên vẫn nằm trong danh sách nguồn. **Việc phải làm:**
comment `dòng 115–116` y như dòng 118. Đây là **CLASS B** ⇒ deploy **sau 18:15** hôm nay,
`effective_from` = **29/08**, **không** áp giữa ngày khi MN đã chốt còn MT/MB chưa.

---

## 5 · HƯỚNG XỬ LÝ VÀ VÌ SAO CHỌN

**Vì sao rút lại ngay thay vì chờ.** `V11133` mới phát hành sáng nay. Càng để lâu càng có khả năng
ai đó dùng nó để đóng một mục theo dõi rò rỉ shadow. `PRJ-RETRACTION-001` bắt rút **đúng chỗ đã
công bố**, đủ bốn phần.

**Vì sao không deploy sửa `AI_MODELS` hôm nay.** MN đã chốt FINAL lúc 05:20, MT/MB **chưa chạy**.
Deploy bây giờ làm một ngày có **hai pool khác nhau** giữa ba miền — phá tính so sánh được của
chính ngày đó. Đợi sau 18:15, `effective_from` 29/08.

**Vì sao dùng đối chứng hằng số.** Mọi biến thể đều quanh 30–36%. Câu hỏi đúng không phải *«biến
thể nào cao hơn»* mà *«có cái nào hơn thứ không cần suy nghĩ gì không»*. Câu trả lời: **không**.

---

## 6 · ĐÃ LÀM GÌ

| # | việc | kết quả |
|---|---|---|
| 1 | Rút lại verdict shadow `V11133` | 3 ca rò rỉ, tái lập từng ca |
| 2 | Rút lại 2 con số `V11132` | 0 (không phải 125) · 145/148 = 98,0% |
| 3 | A3 double-count điểm thật | **8/13**, 12,1% tổng điểm, 50% bạch thủ |
| 4 | A3 paired McNemar + permutation | **0/10 cặp có ý nghĩa** |
| 5 | A3 family dedupe tách kết cục | net +6 ca, p=0,3915, con số **không ổn định** |
| 6 | A3 ablation `meta-learning` | n=427, repro 100%, −0,94pp, p=0,4807 |
| 7 | **Đối chứng hằng số** | nền thật 33,87% · **M0 = 30,77% thấp hơn** |
| 8 | Tách **ba cổng** + 12 phép thử | 12/12 ĐẠT, chạy trên dữ liệu thật |
| 9 | A4 hai lane shadow | persist 3 tệp × 273 bản ghi, đủ 11 trường |
| 10 | A5 dump prompt production | 35 khối / 339 dòng ô nhiễm, phân loại RM-09 |
| 11 | A6 ML pure-math | 6/6 ĐẠT hợp đồng · 6,92 (không phải 8,2) |
| 12 | Định vị nguyên nhân gốc | `combo_super.py:115-116` |

**Không** deploy · **không** restart · **không** ghi DB · **không** đổi
prediction/FINAL/roster/prompt.

---

## 7 · CỔNG KIỂM

| cổng | kết quả |
|---|---|
| `_v11133_thu_chan_ba_cong.py` | **12/12 ĐẠT** |
| ba cổng trên production thật (3 miền) | ELIG **PASS** · CONTRIB **PASS** · MANIFEST `OBSERVABILITY_MISSING` |
| đối chứng dương contribution | **ĐẠT** — 40/40 bundle · 871/871 khác 0 |
| đối chứng dương phép lọc cửa sổ | **ĐẠT** — hạ ngưỡng bắt 991 + 1.391 dòng |
| đối chứng âm ablation (gỡ model không tồn tại) | **ĐẠT** — 0/427 đổi · +0,00pp |
| reproduction check ablation | **ĐẠT** — 427/427 = 100% |
| A5 hash 4 bảng khoá PRE=POST | **ĐẠT** — 2 lần chạy |
| không mutation official path | **ĐẠT** — PID 2694667, 4 hash khớp |

---

## 8 · VƯỚNG VẤP

### 🔴 V1 · Tôi công bố một verdict quá mạnh, và phải rút sau 2 giờ

Xem mục 3.1. Nguyên nhân: soi **một** kênh rồi kết luận cho **mọi** kênh. Bài học cụ thể — trước
khi viết `X = FALSE`, phải liệt kê **có bao nhiêu đường X có thể xảy ra** và nói rõ đã soi đường nào.

### 🟡 V2 · Tiêu chí double-count của tôi lỏng hơn cần thiết

Tôi đo «đồng xuất hiện base + aggregator trên cùng số» ⇒ **12**. Tiêu chí chặt (truy lineage thật
qua `analysis_text`) ⇒ **8**. Tôi lấy **8**.

### 🟡 V3 · Suýt bác nhầm một kết quả đúng

Luồng đo báo *«shadow rót điểm official gián tiếp»* kèm đường dẫn `number_voters` trong
`reasoning_json`. Tôi kiểm: **0 dòng** ở cả `predictions.reasoning_json` lẫn
`final_bundles.source_predictions_json` ⇒ suýt kết luận *«không tái lập được»*.
**Trường đó nằm ở cột thứ ba: `predictions.analysis_text`** — cột tôi chưa soi.
**Đường dẫn họ ghi sai, nhưng kết luận của họ ĐÚNG.** Bác một kết quả vì đường dẫn sai là một
kiểu sai khác.

### 🟡 V4 · Bốn lỗi kỹ thuật nhỏ

`tr '\0'` sinh ký tự null thật · `stat -c %%Y` in ra chữ `%Y` · `datetime()` trả `NULL` nuốt cả
dòng · heredoc bash vấp ký tự đặc biệt khi ghi báo cáo lớn.

### 🟡 V5 · Lỗi các luồng đo tự bắt được (ghi lại vì có ích)

- A6: audit xong Phần 1 trên kho **local** rồi mới đối chiếu hash — phát hiện **7/10 tệp ML khác
  giữa local và VPS**, phải chạy lại toàn bộ trên VPS (`RM-13`).
- A3.2: lần dựng đầu dùng `ORDER BY id` và **không** tái lập được biến thể BASE.
- A3.3: đối chứng âm **thất bại** — biến thể «lấy số ít phiếu nhất» không ra âm (p=0,92). Chính
  việc điều tra thất bại đó dẫn tới **phát hiện hằng số**.

---

## 9 · GỠ VỀ (ROLLBACK)

Phiên này **không mutation** nên **không có gì để gỡ**.

| hạng mục | trạng thái | cách gỡ |
|---|---|---|
| `_v11133_ba_cong.py` + bộ thử | `LOCAL_ONLY` | xoá tệp local |
| `_v11133_lane_shadow.py` | `LOCAL_ONLY` | xoá tệp local |
| artifact hai lane (3 tệp JSONL) | local, **không** vào Git | xoá thư mục `artifacts/lane_shadow` |
| sửa `combo_super.py:115-116` | **CHƯA LÀM** | khi làm: bỏ dấu `#`, restart `lottery`, so PID |

---

## 10 · THEO DÕI TIẾP — LIỆT KÊ ĐỦ

| mã | việc | trạng thái | chặn ở đâu |
|---|---|---|---|
| **SC-shadow** | comment `combo_super.py:115-116` | 🔴 **CHỜ SAU 18:15** hôm nay, `effective_from` 29/08 | tránh 2 pool trong 1 ngày |
| **DO-flip** | 3 ca rò rỉ có lật top-1 không | 🔴 `NOT_VERIFIED` | phải chạy lại hàm chấm điểm |
| **SC-deherd** | de-herd `V10768` làm nửa vời | 🔴 OPEN | phải gỡ cả `gpt_analyzer.py:2830-2833` |
| **SC-contra** | prompt tự mâu thuẫn về số `03` | 🔴 OPEN | `metrics_calculator.py` tính 2 danh sách độc lập |
| **SC-orphan** | `WEEKLY LIVINGNESS` treo **21 ngày** | 🔴 OPEN | `V11014` ép `_live_rows=[]` mà không gỡ mệnh lệnh |
| **SC-cap2** | `database.py:2463-2464` cắt cứng 2 số, mất **54%** đa dạng | 🔴 OPEN | nới cắt phải rất thận trọng |
| **DO-auc** | AUC 3 model MB **dưới 0,5** | 🔴 OPEN | và `_v10952_ket_qua_huan_luyen.json` vẫn ghi trạng thái tốt |
| **DO-lstm** | chỉ số LSTM thổi phồng (chọn checkpoint trên chính tập test) | 🔴 OPEN | `lstm_model.py:210-217` |
| **DO-override** | **18%** bạch thủ công bố đến từ 4 module ghi đè | 🔴 OPEN | 4 module không đọc `score_breakdown` |
| **KS-bien** | biên an toàn MT còn 1 phút (13/08) | 🟡 theo dõi | 0/91 ngày vượt khoá |
| **scorer** | mốc 16:50 / 17:45 / 18:45 / 20:20 | ⏳ **WAIT_LIVE** | chiều nay |
| **1.2** | timeline MT/MB ngày 28/08 | ⏳ **WAIT_LIVE** | chưa chạy lúc đo |
| **3-càng** | Algorithm Card + generator + writer | 🔴 `MISSING_PIPELINE` | không có writer/cột |

---

## 11 · BA LỚP NGUỒN (§62)

### `OWNER_SAID` — xem mục 2, nguyên văn kèm giờ.

### `CODE_DID`

| việc | evidence |
|---|---|
| rò rỉ shadow qua `ai_confirm` | `predictions.reasoning_json` combo-super 12/08 · 13/08 · 23/08 MN |
| shadow trong `number_voters` | `predictions.analysis_text` — `gemini-3.5-flash` ×4 · `gemini-3.6-flash` ×2 |
| nguyên nhân gốc | `combo_super.py:115-116` không bị comment, `:118` thì có |
| chuỗi ảnh hưởng | `:318 → :395/:465 → :1291 → :1302 → :1364 → :2432` |
| double-count | 8/13 · 12,1% điểm · 20/40 bạch thủ |
| paired test | 0/10 cặp có ý nghĩa · p thô nhỏ nhất 0,2031 · seed 20260828 |
| đối chứng hằng số | trung bình 100 hằng số 33,87% · M0 30,77% |
| ablation meta | n=427 · repro 427/427 · −0,94pp · p=0,4807 |
| prompt thật | MN 50.594 · MT 49.662 · MB 53.834 ký tự |
| đa dạng ML | 6,92 (không phải 8,2) · cắt 2 số mất 54% |
| ba cổng | 12/12 thử · PASS trên production thật |
| không mutation | PID 2694667 · 4 hash khớp PRE |

### `DOC_SAID`

- `CLAUDE.md §55` biên an toàn **2 phút** — MT vượt biên **1/91 ngày** ⇒ `DOC_SAID ≠ CODE_DID`, ghi
  theo dõi `KS-bien`.
- `_v10952_ket_qua_huan_luyen.json` ghi trạng thái huấn luyện **tốt**, trong khi AUC ba model MB
  **dưới 0,5** ⇒ `DOC_SAID ≠ CODE_DID`, ghi theo dõi `DO-auc`.
- `docs/CURRENT_TRUTH_SSOT.md` chưa cập nhật — `DOC_SAID` chậm hơn `CODE_DID`, đúng khung
  `PRJ-INTERACTION-LEDGER-001`.

---

## 12 · RUNTIME_LADDER

| hạng mục | bậc |
|---|---|
| bộ lọc shadow `V11130` | 🟢 `RUNTIME_PROVEN` (V11133, kèm giới hạn đã ghi) |
| FU-438 auth gate | 🟢 `RUNTIME_PROVEN` |
| ba cổng `_v11133` | ⚪ `LOCAL_ONLY` — 12/12 thử |
| hai lane shadow A4 | ⚪ `LOCAL_ONLY` — persist artifact |
| sửa `AI_MODELS:115-116` | ⚪ `NOT_STARTED` — chờ sau 18:15 |
| scorer cuốn chiếu | 🟡 `RUNTIME_LOADED` — chưa tới mốc |

---

## 13 · NOT_VERIFIED

| # | chưa rõ | thiếu gì | kiểm ở đâu | ảnh hưởng |
|---|---|---|---|---|
| 1 | 3 ca rò rỉ **có lật top-1 không** | phải chạy lại hàm chấm điểm không có factor đó | `combo_super.py:2432` | quyết định mức nghiêm trọng |
| 2 | bộ lọc `V11130` có bịt **hoàn toàn** kênh `ai_confirm` không | mới có **1 ngày** dữ liệu sau vá | quan sát tiếp 29–31/08 | lập luận cơ chế mạnh, dữ liệu còn mỏng |
| 3 | tập eligibility **đầy đủ** trong lượt scheduled | manifest không lưu | cần `MANIFEST_OBSERVABILITY` deploy | giới hạn của `RUNTIME_PROVEN` |
| 4 | **18%** bạch thủ bị 4 module ghi đè — ảnh hưởng gì | 4 module không đọc `score_breakdown` | V10640/V10767/V10789/V10790 | mọi số liệu Combo phải đọc lại theo tầng |
| 5 | định nghĩa gốc của con số «8,2 candidate» | không tìm được script sinh ra nó | — | trước khi dùng 6,92 làm căn cứ |
| 6 | `db_env_drift:google:selected_db` | chưa điều tra | log 05:15 + preflight | chưa rõ ảnh hưởng |
| 7 | timeline MT/MB 28/08 | chưa chạy lúc đo | sau 16:58 / 17:58 | không suy từ MN |
| 8 | `rule-engine` xuất hiện 27 lần trong `number_voters` | không phải model nào trong roster | — | chưa rõ là gì |
| 9 | nới `main_numbers[:2]` có tốt lên không | chưa đo | `database.py:2463` | **cấm** sửa vội |

---

## 14 · MUTATION_LOG

| | |
|---|---|
| deploy / restart | ❌ **KHÔNG** — PID 2694667 = PRE · `NRestarts=0` |
| ghi production DB | ❌ **KHÔNG** — `-readonly`, hash 4 bảng PRE=POST |
| prediction · FINAL · roster · prompt | ❌ **KHÔNG ĐỔI** |
| tệp trong `Lottery_AI_Test` | 🟡 **3 tệp MỚI**, `LOCAL_ONLY`, chưa deploy: `_v11133_ba_cong.py` · `_v11133_thu_chan_ba_cong.py` · `_v11133_lane_shadow.py` |
| artifact | 3 tệp JSONL trong `artifacts/lane_shadow/` — **không** vào Git |
| credential · SSH · Notion · ERP | ❌ **KHÔNG CHẠM** |
| CLASS C | ❌ **KHÔNG** |

---

## 15 · NEXT_ACTION

1. **Sau 18:15 hôm nay:** comment `combo_super.py:115-116`, `effective_from` 29/08, so PID trước/sau.
2. **Chiều nay:** scorer **16:50 → 17:45 → 18:45 → 20:20**; timeline MT/MB.
3. Chạy lại hàm chấm điểm cho 3 ca rò rỉ ⇒ trả lời `NOT_VERIFIED #1`.
4. Deploy ba cổng khi đã khớp schema thật (`BLOCKED_TECHNICAL_SCHEMA_ALIGNMENT`, **không phải**
   «chờ Owner duyệt»).
5. Gỡ nốt de-herd nửa vời + mệnh lệnh mồ côi `WEEKLY LIVINGNESS`.

---

TanPhatAI cần làm: ghi **RÚT LẠI** — câu *«`SHADOW_CHANGED_FINAL = FALSE_IN_OBSERVED_14D_WINDOW`»* trong **`REPORT_V11133` (commit `48a4aa2`, phát hành sáng 28/08)** là **QUÁ MẠNH**; nhãn đúng là **`SHADOW_ENTERED_COMBO_SCORING_VIA_AI_CONFIRM = TRUE`** với **3 ca xác nhận** (12/08 · 13/08 · 23/08, đều MN, `gemini-3.5-flash`, mỗi ca **rơi đúng số được chọn**, weight tới **2.000**), và **`SHADOW_CHANGED_FINAL = NOT_EXCLUDED`** — **không phải `FALSE`**. Câu **`NO_OBSERVED_SHADOW_SCORE_CONTRIBUTION_14D` vẫn đúng nhưng phải ghi kèm «ở kênh `components[].model`»**, cấm để trần. Nguyên nhân gốc: **`combo_super.py:115-116`** — `gemini-3.5-flash` và `gemini-3.6-flash` vẫn nằm trong `AI_MODELS` **không bị comment**, trong khi `gpt-5-mini` ở dòng 118 **đã** comment từ 01/08. Ghi **đối chứng hằng số**: trung bình 100 hằng số đạt **33,87%**, còn FINAL hiện hành **30,77% — THẤP HƠN**; đây là lý do kỹ thuật để **không** tối ưu ranking. Ghi **`13/18` là SAI**: đúng là **13 `DUPLICATE_LINEAGE`** và **8 `ACTUAL_DOUBLE_COUNT_NONZERO`**, chiếm **12,1% tổng điểm** và có mặt ở **20/40 = 50%** bạch thủ. Ghi **paired McNemar + permutation: 0/10 cặp có ý nghĩa, kể cả TRƯỚC hiệu chỉnh** — `INSUFFICIENT_POWER`. Ghi **bác bỏ** con số cũ *«bỏ meta-learning đổi 147/273 = 53,8%»* — đúng là **47/427 = 11,0%**, delta **−0,94pp, p=0,4807**, `INSUFFICIENT_POWER`. Ghi **đính chính `V11132`**: *«125 manifest `numbers` không phải dict»* là **SAI**, đúng là **0 không-phải-dict / 125 RỖNG**; và *«0/62 lệch»* đúng phải là **145/148 = 98,0% khớp**. Ghi **A5**: prompt thật **MN 50.594 ký tự**, **35 khối / 339 dòng ô nhiễm**, **nhóm TOTAL/FINAL = 0** (bác con số «5 chỗ» cũ), **de-herding `V10768` làm nửa vời** và **`WEEKLY LIVINGNESS` treo mồ côi 21 ngày**. Ghi **A6**: **6/6 model ĐẠT** hợp đồng pure-math, đa dạng thật là **6,92 chứ không phải 8,2**, nút thắt là **`database.py:2463-2464` cắt cứng 2 số làm mất 54%**, và **AUC ba model MB đều dưới 0,5**. Ghi **ba cổng 12/12 thử**, `LOCAL_ONLY`. **Phiên này không mutation official path.**
