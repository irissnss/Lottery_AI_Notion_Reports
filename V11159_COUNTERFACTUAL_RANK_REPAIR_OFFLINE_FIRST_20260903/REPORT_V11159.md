# REPORT V11159 — COUNTERFACTUAL RANK REPAIR · OFFLINE-FIRST

> **Ngày:** 03/09/2026 22:20 → 04/09 00:4x (VN) · `CURRENT_ACTOR = CLAUDE_CODE`
> `PROMPT_STATE = PROMPT 43 R1 · PARTIAL` · `POOL_VERDICT = HOLD` · `MODEL_ACTION = BLOCKED`
> **`PRODUCTION_MUTATION_COUNT = 0`** — toàn bộ phép tính chạy trên bản sao.
> ⚠️ **Bản này chứa một RÚT LẠI lật ngược điều agent đã khẳng định hai lần trong ngày.**

---

## 1 · Tóm tắt

Work package yêu cầu dựng `output_counterfactual_rank` **từ dữ liệu trước kết quả**, không phải
xếp hạng theo kết quả đã biết. Bốn cổng nặng đã đóng được:

| cổng | kết quả |
|---|---|
| **B** nguồn dữ liệu | **ĐẠT** — clone 809 MB, `integrity_check=ok`, đếm dòng + neo khớp gốc |
| **D** tái lập selector | **ĐẠT 99/99 = 100,0%**, lệch điểm lớn nhất `0,000000` |
| **E** chống oracle | **ĐẠT 6/6 · `ANTI_ORACLE_PROVEN`** |
| **F** thống kê | **KHÔNG comparator nào qua cổng** — insufficient power ⇒ HOLD |
| **G** an toàn | **ĐẠT** — production 0 ghi, official không đụng |
| **A** context-only | **PARTIAL** — routing PASS, semantic clean **KHÔNG ĐẠT** |
| **C** eligibility | **ĐẠT có điều kiện** — 429/540 ô đủ ba lớp, 111 ô thiếu lớp L3 |

**Và một phát hiện nặng hơn mọi kết quả counterfactual**: bản deploy `V11157` của chính agent đã
**rò prompt thí nghiệm vào đường official** — mục 2 dưới đây.

---

## 2 · Owner yêu cầu gì — NGUYÊN VĂN

> `PRJ-INTERACTION-LEDGER-001`: **prompt chính VÀ mọi yêu cầu trực tiếp trong phiên**, nguyên văn + giờ.

| giờ (VN) | NGUYÊN VĂN | loại |
|---|---|---|
| 03/09 ~22:05 | *«Tiếp theo là gì em? phân tích đánh giá dự đoán hôm nay, việc xử lý prompt thuần ngữ cảnh và các vấn đề đơn model và total xử lý tới đâu rồi đo được gì rồi? Hôm nay vẫn tệ như mọi ngày»* | `HỎI` + `CHIA_SẺ` |
| 03/09 ~22:15 | `PROMPT 43 R1 · CONTINUATION AFTER V11158 · COUNTERFACTUAL RANK REPAIR OFFLINE-FIRST` — 19 mục `I`–`XIX` | `YÊU_CẦU` |
| 03/09 ~23:5x | *«làm xong chả báo cáo gì là sao em?»* | **`BÁC_BỎ`** |
| 04/09 ~00:0x | *«ok vậy đợi soi xong tổng hợp đề xuất báo cáo tổng hợp 1 lần luôn em»* | `ĐỔI_ƯU_TIÊN` |

**Owner sửa một đề xuất SAI của agent.** Bản cũ: *«đổ đầy `output_counterfactual_rank` cho 180
ngày, xếp hạng 27 model **theo kết quả thật**»* — đó là **oracle hindsight**. Owner tuyên phải
sửa thành: *«dựng từ **đúng selector/TOTAL và dữ liệu có trước region lock**; sau đó mới dùng kết
quả thật để chấm rank **đã đóng băng**»*. Toàn bộ mục `X` (hai pha + năm META test) sinh từ đây.

**Câu owner cho phép dùng, nguyên văn:** *«Chưa đo được lợi thế so với baseline ngẫu nhiên ở mẫu
hiện tại; cũng chưa đủ bằng chứng kết luận hệ thống thật sự kém hơn baseline.»*
**Owner CẤM ghi:** «hệ thống chắc chắn bằng bốc bừa» · «một ngày 0/3 chứng minh regression» ·
«có ít nhất một model trúng chứng minh pool tốt» · «một model hôm nay trúng chứng minh model đó
nên được chọn».

---

## 3 · 🔴 RÚT LẠI — `PRJ-RETRACTION-001`, đủ bốn phần

| phần | nội dung |
|---|---|
| **chỗ gốc** | `REPORT_V11157` mục 4 · `REPORT_V11158` mục 6 · `CHANGELOG`/`SSOT` V11157+V11158 — công bố **03/09/2026** |
| **nguyên văn câu sai** | *«official **KHÔNG đổi một ký tự prompt** — chứng minh bằng 6 băm»* · *«`SERVICE_ENV_RUNTIME_PROVEN` ĐẠT · official chưa đổi»* |
| **điều đúng, kèm phép đo tái lập được** | `LLM_CONTEXT_ONLY_V2_LANE=shadow` định tuyến theo `SHADOW_GATE_MODELS`. **`gpt-oss-120b` là model DUY NHẤT nằm trong CẢ `SHADOW_GATE_MODELS` LẪN `get_output_eligible_ids()`** — ở **cả ba miền**. Nên một model của **chuỗi official** nhận **prompt thí nghiệm**, và phiếu của nó **vào bundle official**. |
| **quyết định đã dựa trên số sai** | Nhãn `SERVICE_ENV_RUNTIME_PROVEN` và tiền đề *«official đứng yên làm đối chứng»* — **cả hai phải hạ**. Nhánh đối chứng official **KHÔNG sạch** kể từ 03/09. |

**Bằng chứng, tái lập được:**

```
SHADOW_GATE_MODELS ∩ get_output_eligible_ids(MN|MT|MB) = ['gpt-oss-120b']   ← duy nhất

bundle 823  MB  BT=32  · gpt-oss-120b bỏ phiếu ['32','49']  ← VOTER CỦA CHÍNH SỐ BẠCH THỦ
bundle 819  MN  BT=10  · gpt-oss-120b bỏ phiếu ['78','73']
bundle 821  MT  BT=32  · không bỏ phiếu (bị trần 13 loại)

predictions 03/09 · gpt-oss-120b:
   MN auto_daily 05:17:51  ["78","73"]  PARTIAL   (trước deploy 13:47 — regime = None)
   MT ai_chain   16:42:23  ["86","65"]  LOSE      trace 6437 · regime = CONTEXT_ONLY_V2
   MB ai_chain   17:34:37  ["32","49"]  LOSE      trace 6458 · regime = CONTEXT_ONLY_V2
```

**Vì sao cổng bất biến của agent KHÔNG bắt được.** Nó dựng prompt bằng `model="gemini-2.5-pro"`
— một model **không** nằm trong `SHADOW_GATE_MODELS`. Nó **về mặt cấu trúc không thể** phát hiện
một lỗi định tuyến **theo model**. Lấy một model làm mẫu rồi suy cho cả đường official là **lần
thứ năm trong ngày** mắc đúng họ *«dụng cụ đo đứng sai chỗ»*.

**Chưa đo được mức ảnh hưởng** (`RM-04`): `n = 1` ngày, và chưa tính lại bundle khi bỏ phiếu của
`gpt-oss-120b`. **Cấm** suy ra bất kỳ verdict model nào từ đây.

---

## 4 · Đào bới / phát hiện — liệt kê ĐỦ

### 3.1 · Pre-flight (mục IV)

`PID 3299063` · `NRestarts 0` · health `200` · env service `LLM_CONTEXT_ONLY_V2_LANE=shadow`.
Băm 9 tệp trọng yếu. 254 bảng. Đếm dòng: `predictions 14.120` · `final_bundles 564` ·
`lottery_results 15.410` · `model_daily_eval 13.984` · `scorecard 17.040` · `reliability 5.243`.
Neo 558 `a82c508d…` **KHỚP**. Clone `809 MB` bằng `sqlite3.backup()`, `integrity_check=ok`,
`foreign_key 0 lỗi`, đếm dòng + neo **khớp gốc**.

### 3.2 · 🟢 Gate D — tái lập selector **99/99 = 100,0%**

Cửa sổ sạch `02/08 → 03/09`. Khớp **cả dãy 10 số** 99/99 · khớp `model_count` 99/99 ·
**lệch điểm lớn nhất `0,000000`**.

**Hai lần agent sai, cả hai là THƯỚC sai chứ không phải VẬT ĐO sai:**

| lần | agent kết luận | sự thật |
|---|---|---|
| ① | *«15 ca lệch tập voter ⇒ selector sai»* | `main.py:10467` chỉ lưu **`ranked[:10]`** và `components[:8]`. Agent so bản ĐẦY ĐỦ với bản ĐÃ CẮT |
| ② | *«công thức đúng, còn lệch ~0,0005»* | `database.py:3422-3429` làm **`round(bt_rate,1)`** rồi **`round(bt_weight,3)`** TRƯỚC khi chấm. Thiếu hai phép đó đủ lật thứ tự cặp sát điểm |

**Khác biệt CÓ CHỦ Ý duy nhất so với production:** trọng số tính **as-of** `date < D`. Bản gốc
`get_model_bt_rates` dùng `vn_now()` **không có chặn trên** ⇒ tái lập lịch sử bằng nó là lookahead
nặng. Khác **đúng chiều an toàn**.

### 3.3 · Sổ ngoại lệ Gate D

| mã | ô | nội dung |
|---|---|---|
| `REGISTRY_TRANSITION_DAY` | **2** | `2026-08-01` MN + MT — đúng ngày registry đổi **4 commit** (`5e86072` · `cb6bc52` · `fa48c2f` · `24e9755`). Loại khỏi cửa sổ |

Không ca nào khác. Trong vòng chẩn đoán trước khi sửa thước: 19 ca lệch, mọi ca đều là **hoán đổi
hai hạng liền kề**, `lệch_voter = 0`, `lệch_điểm ≤ 0,001`.

### 3.4 · 🟢 Gate E — chống oracle **6/6 · `ANTI_ORACLE_PROVEN`**

Bảo đảm bằng **CẤU TRÚC**: lớp `CanhGac` bọc kết nối, **ném** nếu SQL chạm `lottery_results`,
hoặc đọc cột kết quả mà **không** có chặn trên nghiêm ngặt `date < ?` với chính ngày đích.

| phép | kết quả |
|---|---|
| ① xoá kết quả + status **của riêng ngày đích** ⇒ rank không đổi | **0/8 ô lệch** |
| ② thay kết quả ngày đích bằng dữ liệu giả (mọi `status→WIN`) | **0/8 ô lệch** |
| ③ băm artifact tất định | ĐẠT |
| ④ pha 1 chạm `lottery_results` lúc chạy | **0/8 ô** |
| ⑤ truyền `ket_qua_that=` ⇒ `TypeError` | ĐẠT |
| ⑥ cổng tự thử-chặn 3 mẫu vi phạm (`RM-15`) | 3/3 chặn |

**Vòng đầu ①② HỎNG 6/8** — vì phép thử xoá kết quả **cả ba ngày mẫu cùng lúc**, mà chúng nằm
trong cửa sổ 30 ngày của nhau ⇒ đổi TRỌNG SỐ chứ không phải lộ oracle. **Lỗi phép thử.**

Artifact pha 1 đóng băng: **`9474b7bcc50d1b13ae41b7d37c5619b86a52c6cdc5243ee16893c4b295e5faa6`**.
Pha 2 chạy **tiến trình RIÊNG**, kiểm băm khớp rồi mới nối kết quả.

### 3.5 · 🔴 Gate F — ba comparator, không cái nào qua cổng

McNemar **chính xác**, ghép theo `date × region`, Holm trên họ 3 miền:

| so sánh | miền | BT_A | BT_B | b (cứu) | c (phá) | `p_exact` | `p_Holm` | kết luận |
|---|---|---|---|---|---|---|---|---|
| **A vs B** thêm shadow thô | MN | 9 | 7 | 6 | 8 | 0,7905 | 1,000 | không khác |
| | **MT** | 11 | **15** | **4** | **0** | 0,1250 | **0,375** | không khác |
| | MB | 6 | 5 | 2 | 3 | 1,0000 | 1,000 | không khác |
| **A vs C** đã khử trùng | cả ba | — | — | **0** | **0** | 1,0000 | 1,000 | **không đổi một ô nào** |

**MT trần 13: lượt bị đẩy ra `59 → 228`.** Cái "tăng" ở MT phần lớn là **THAY THẾ official**,
không phải thêm nguồn — đúng thứ mục `IX` cấm gọi nhầm.

**C không đổi một ô nào** vì luật khử trùng agent viết (trùng nhà với official ⇒ bỏ) đã loại gần
hết shadow. Đó là **giới hạn của luật agent chọn**, KHÔNG được đọc thành «khử trùng vô hại».

**Add-one: 973 lượt · 125 đổi top-1 · 169 là THAY THẾ.**

| nguồn | có mặt | đổi top-1 | cứu | phá | thay thế | `p_exact` |
|---|---|---|---|---|---|---|
| `qwen3.7-max` | 86 | 16 | 7 | 2 | 8 | 0,180 |
| `gemini-3.5-flash` | 88 | 15 | 6 | 4 | 7 | 0,754 |
| `gpt-5.5` | 88 | 8 | 3 | 1 | 8 | 0,625 |
| `qwen3-max-thinking` | 98 | 15 | 5 | 3 | 31 | 0,727 |
| `glm-5.2` | 74 | 10 | 2 | 2 | 15 | 1,000 |
| `deepseek-v4-pro-real` | 74 | 11 | 0 | 2 | 4 | 0,500 |

**Không nguồn nào `p < 0,05`.**

### 3.6 · Đối chứng ngẫu nhiên khớp cỡ pool

Cùng `date × region`, cùng **số ứng viên duy nhất**, cùng trần, seed tất định, 2.000 lượt/ô:

| | BT thực | nền bốc bừa khớp pool |
|---|---|---|
| A · MN | 27,3% | **42,9%** |
| A · MT | 33,3% | 34,6% |
| A · MB | 18,2% | 24,0% |
| **B · MT** | **45,5%** | 34,5% |

Chỉ `B·MT` vượt nền. Mọi ô còn lại **ở hoặc dưới** nền — nhất quán `V11116` (25/08).

### 3.7 · Sức mạnh phép đo (mục XII)

| miền | b | c | tỉ lệ cứu | **n cần** |
|---|---|---|---|---|
| **MT** | 4 | 0 | 1,00 | **≈ 65 ngày (~2,1 tháng)** |
| MN | 6 | 8 | 0,43 | 907 ngày (~30 tháng) |
| MB | 2 | 3 | 0,40 | 1.295 ngày (~43 tháng) |

Bảng tra khi hiệu ứng thật nhỏ hơn: tỉ lệ cứu `0,80` với `15%` ô bất đồng ⇒ **145 ngày**;
`0,75` ⇒ **209 ngày**.

⚠️ `n cần` **suy từ chính tỉ lệ quan sát**, mà tỉ lệ đó dựa trên **4 ô bất đồng** (MT). Theo
`RM-04` con số này **cũng không ổn định** — nó nói bậc độ lớn, không phải lời hứa.

### 3.8 · 🟡 Gate A — context-only: tách HAI verdict, cấm gộp

| verdict | kết quả |
|---|---|
| `SCHEDULED_LANE_ROUTING_PROVEN` | **PASS** — scheduler thật đã chạy, ba nguồn độc lập |
| `SCHEDULED_SHADOW_PROMPT_CLEAN_PROVEN` | **KHÔNG ĐẠT** |

Vì sao verdict 2 không đạt: trace **không có vân tay prompt runtime nào**. `custom_prompt.sha256`
là khối `ARCHIVE_ONLY` `runtime_active=false` **giống hệt ở cả 62 dòng**; `prompt_version=PB-20.1`
**giống nhau ở cả hai regime**. Và quét ngược tìm được **mệnh lệnh treo `gpt_analyzer.py:3151`**
trỏ vào **đúng khối dữ liệu vừa bị gỡ**, xuất hiện trong **100%** prompt ngữ cảnh thuần ⇒
`PRJ_PROMPT_DANGLING`.

**Ma trận 62 lượt ngày 03/09:**

| regime | is_shadow | `run_source` thật | n |
|---|---|---|---|
| `CONTEXT_ONLY_V2` | True | **`ai_chain` (OFFICIAL)** | **2** ← rò |
| `CONTEXT_ONLY_V2` | True | `shadow_auto_eval` | 22 |
| `LEGACY_PROMPT` | False | `ai_chain` | 14 |
| `LEGACY_PROMPT` | False | (không nối được) | 4 |
| (None — trước instrument) | — | `auto_daily` / `shadow_auto_eval` | 20 |
| | | **TỔNG** | **62** |

`LEGACY_PROMPT × shadow_auto_eval = 0` — không lượt shadow nào ăn prompt cũ.

**Bằng chứng NỘI DUNG (không phải chỉ cờ tự khai):** journal của chính `PID 3299063` in
`[Phase 11][CONTEXT_ONLY_V2] BỎ QUA…` + `[Phase 14A][CONTEXT_ONLY_V2] BỎ QUA…` cho **8/24** lượt.
Sai phân độ dài diff-in-diff: **MT −1313 · MB −1070 · MN ≈−1264** so với khối đo trực tiếp
**−1281/−1327**.

⚠️ `context_pack_chars` **KHÔNG** phải thước của regime — nhóm shadow đã lớn hơn ~3.000 ký tự
**từ 26/08**, trước khi cờ bật.
⚠️ Journal chỉ chứng minh **SỰ CÓ MẶT**, tuyệt đối không dùng chứng minh sự vắng mặt: giờ 17 có
**0 dòng** dù 12 model shadow chạy thật — **chưa giải thích được**.

### 3.9 · 🟡 Gate C — roster theo thời điểm

540 ô (180 ngày × 3 miền), **ba lớp bằng chứng**: L1 sự kiện (`predictions.run_source`) · L2
runtime (`final_bundles.source_predictions_json`) · L3 registry-at-time dựng từ **22 commit git**.

| chỉ số | giá trị |
|---|---|
| roster official trung bình | **14,79** model/ô (min 6 · max 17) |
| roster shadow hợp lệ trung bình | **8,70** model/ô |
| ô đủ ba lớp | 429 |
| **ô thiếu lớp L3** (`RM-13`) | **111** (08/03 → 13/04, trước khi có registry) |
| ô không có mốc đóng băng (trước 05/07) | 357 |
| ca chuyển vai trò trong ledger | **72** |
| lệch đối chiếu L1∩L3 vs L2 | 11 ô (2,04%) |

**Hai phát hiện quan trọng:**
① `run_source` chỉ nói **LANE** nào chạy, **KHÔNG** nói model có được bỏ phiếu — `combo-no-token`
bị registry bỏ khỏi output-eligible lúc `2026-08-01 16:46` nhưng **vẫn chạy `auto_daily` mỗi
ngày** và bỏ phiếu vào **0/99** bundle. Lấy một mình L1 làm roster official là **sai**.
② Mốc đóng băng là **HẰNG SỐ CÓ THỜI HẠN** (`RM-21`): cơ chế freeze chỉ ra đời **05/07** và mốc
đã đổi **ba lần** (`05/07`: MN 15:55·MT 16:55·MB 17:55 → `31/07`: 15:45·16:53·17:53 → `01/08`:
15:45·16:58·17:58). Bản dựng đầu áp mốc hôm nay ngược 180 ngày đã **xoá oan trọn hai ô**.

### 3.10 · Hợp đồng ngữ nghĩa `output_counterfactual_rank` (mục VI)

| mục | nội dung | bằng chứng |
|---|---|---|
| **grain một dòng** | `date × region × ai_model` — **UNIQUE thật**, 0 trùng lặp | `UNIQUE(date,region,ai_model)`; 17.040 dòng = 17.040 bộ |
| **writer hiện tại** | `_materialize_shadow_promotion_scorecard.py`, **2 câu INSERT, cả hai truyền HẰNG CỨNG `None`** ở vị trí 17/34, **vô điều kiện** | AST `elts[16] == None`; 3/3 bản backup cũ cũng vậy |
| **reader của CỘT** | **KHÔNG CÓ** — quét 3.024 tệp, 34 dòng khớp toàn DDL/danh sách cột | |
| **NULL nghĩa là gì** | **«CHƯA TÍNH»**, tuyệt đối không phải «không đủ điều kiện» — chưa hề có phép xét điều kiện nào chạy | 17.040/17.040 `typeof='null'` |
| **một số nguyên có đủ không** | **KHÔNG** — mỗi model ra tới 2 số, bản công bố có 5 họ output. Kho đã có tiền lệ tách ba cột rank riêng ở `loz_stage_trace_shadow` | |
| **spec gốc** | **CÒN NGUYÊN** trong kho làm việc (`artifacts/phase_checkpoints/SHADOW_MODEL_PROMOTION_MEASUREMENT_ROADMAP_20260427.md:50`) nhưng **không deploy lên VPS** vì `artifacts/` bị gitignore | phản biện đã sửa lại kết luận đầu «spec đã mất» |

### 3.11 · 🟡 Nền theo dõi 14 ngày (mục XIII)

| model | lane | slot có SỐ W30 | empty W30 | **empty W14** | timeout | trước region-lock |
|---|---|---|---|---|---|---|
| `deepseek-reasoner` | official | 82/90 = 91,1% | 6,82% | 5,00% | không đo được¹ | 100% |
| **`glm-5.2`** | shadow | 71/90 = 78,9% | **20,22%** | **39,02%** | 1,12% | 92,13% |
| `glm-5.1` *(đối chứng)* | official | 84/90 = 93,3% | 3,45% | 2,50% | không đo được¹ | 100% |
| `deepseek-v4-pro-real` *(đối chứng)* | shadow | 89/90 = 98,9% | 0,00% | 0,00% | 13,48% | 78,65% |

¹ lane official **chỉ ghi dòng khi HỎNG** ⇒ **không có mẫu số** để tính tỉ lệ.

**Ba điều phải biết trước khi so 14 ngày tới:**
① **Nhóm đối chứng KHÔNG đối xứng** — `glm-5.1` đã có hard-timeout `840s` **từ 01/08**, còn
`glm-5.2` chỉ có `300s` suốt cửa sổ nền.
② Bảng độ tin cậy chỉ ghi đủ cho lane shadow.
③ **Empty-rate `glm-5.2` đang xấu dần**: W30 `20,22%` nhưng **14 ngày liền kề trước ngày vá là
`39,02%`** — lấy nền W30 làm mốc so sẽ **tự tạo ra một nửa "cải thiện" chỉ do chọn cửa sổ**.

Với `deepseek-reasoner`, 14 ngày (`n=42`) **KHÔNG đủ sức**: ở nền `5,00%` thì **ngay cả 0 lượt
rỗng cũng chỉ đạt `p = 0,116 > 0,05`** — cần tối thiểu **59 lượt (~20 ngày)**.

Nhãn giữ nguyên: `deepseek-reasoner` = **`FIRST_POST_FIX_RUNTIME_PASS`** ·
`glm-5.2` = **`FIRST_POST_FIX_RUNTIME_PASS`**. Bốn bản vá hạ tầng **KHÔNG tự chứng minh
predictive quality**.

### 3.12 · 🟢 Khoá 3-càng KHÔNG bị thay đổi (mục XIV)

Hàm sinh tên thật `_generate_lo3_frequency` (`main.py:10587-10685`). **8/10 mệnh đề owner ĐÚNG
trên code hôm nay.**

| # | mệnh đề | kết quả |
|---|---|---|
| 1 | đơn model không bắt buộc output 3-càng | **ĐÚNG** — dump prompt đang serve: 0 hit ở cả ba miền |
| 2 | `UCC` không thêm field 3-càng | **ĐÚNG về thực chất** — nhưng **tên «UCC» KHÔNG TỒN TẠI trong code** (`RM-10`): grep `unified_candidate\|UCC` = **0 hit/772 tệp** trên VPS |
| 3 | official dùng `bach_thu` thực sự công bố | **ĐÚNG** — lo3 tính tại `:10307`, **sau** cả 5 phép gán `bach_thu`; **564/564** bundle có `lo3[1:] == bach_thu` |
| 4 | shadow/challenger dùng BT riêng | **ĐÚNG** — `main.py:12425` · `:15568` |
| 5 | bộ chọn prefix chạy downstream | **ĐÚNG** |
| 6 | không clone 3-càng official sang challenger | **ĐÚNG trong CODE** — nhưng **chú thích `main.py:12306-12307` nói NGƯỢC** với code cách 110 dòng |
| 7 | derived per-model mang nhãn `DERIVED_FROM_MODEL_BT` | **CHƯA TỒN TẠI** — ý định thiết kế, chưa implement (`RM-12`). grep = 0 hit/772 tệp |
| 8 | derived không phải model vote, không vào TOTAL | **ĐÚNG** |
| 9 | `V11157 = SUBSTANTIALLY_VALID` | **ĐÚNG** (riêng về khoá 3-càng) |
| 10 | việc còn lại là lineage/trace | **ĐÚNG** — **7/8 trường lineage CHƯA TỒN TẠI**, chỉ `lo3_method` được lưu thật |

Không lookahead (`date < date_str`), giữ số 0 đầu (`BT='02' → '002'`, `BT='00' → '900'`).
Kết quả lô3 thua cả ba miền hôm nay **KHÔNG** tạo verdict và **KHÔNG** đổi kiến trúc.

---

## 5 · Hướng xử lý và vì sao chọn

**Vì sao dừng cửa sổ ở `02/08` chứ không lấy 180 ngày.** Registry đổi **22 lần/180 ngày**, lần
cuối `01/08`. Chỉ từ `02/08` trở đi mới chứng minh được eligibility-at-time **mà không cần** git
history. Lấy 180 ngày ngay từ đầu là mời `RM-13` vào.

**Vì sao chặn oracle bằng CẤU TRÚC chứ không bằng kỷ luật.** Lời hứa «tôi sẽ không đọc kết quả»
không kiểm được. Lớp `CanhGac` **ném** — và META test chứng minh nó ném thật.

**Vì sao khác production ở đúng một chỗ (trọng số as-of).** Bản gốc không có chặn trên; dùng
nguyên bản để tái lập lịch sử là lookahead. Khác **đúng chiều an toàn**, và ghi rõ để không ai
tưởng là lỗi.

**Vì sao KHÔNG deploy bản vá cho lỗ rò `gpt-oss-120b` trong work package này.** Mục `XVII` gate G
của chính đề bài đòi *«official untouched»*, mục `XVIII` cấm ghi production trong work package
offline. Bản vá này **chạm đường official** ⇒ phải là một packet riêng, owner duyệt.

---

## 6 · Đã làm gì — TRƯỚC / SAU / PHIÊN BẢN / KIỂM

| việc | TRƯỚC | SAU | KIỂM |
|---|---|---|---|
| tái lập selector | chưa từng tái lập | **99/99 = 100,0%** | lệch điểm `0,000000` |
| khoá chống oracle | không có | `CanhGac` + 6 META test | **6/6 ĐẠT** |
| artifact rank | không có | đóng băng + băm | `9474b7bc…`, pha 2 kiểm khớp |
| ba comparator | không có | A · B · C + add-one 973 lượt | McNemar chính xác + Holm |
| roster theo thời điểm | không có | 540 ô, ba lớp, ledger 72 ca | 429/540 đủ ba lớp |
| nền 14 ngày | không có | 4 model × 7 chỉ số | artifact JSON |
| `output_counterfactual_rank` | **NULL 17.040/17.040** | **VẪN NULL 17.040/17.040** | **chưa ghi production** |

---

## 7 · Cổng kiểm

| cổng | kết quả |
|---|---|
| A — scheduled context-only | 🟡 **PARTIAL**: routing PASS · semantic clean **KHÔNG ĐẠT** |
| B — nguồn dữ liệu | 🟢 ĐẠT |
| C — eligibility | 🟢 ĐẠT có điều kiện (111 ô thiếu L3, gắn `RM-13`) |
| D — tái lập baseline | 🟢 **ĐẠT 99/99** |
| E — counterfactual | 🟢 **ĐẠT** — rank sinh trước kết quả, nối sau, add/replacement tách bạch, displacement truy được, chạy lại tất định |
| F — thống kê | 🔴 **không comparator nào qua cổng** |
| G — an toàn | 🟢 ĐẠT — `PRODUCTION_MUTATION_COUNT = 0`, official không đụng, không model action, không materialize, không Prompt 44, không FU mới |

---

## 8 · Vướng vấp — năm lần, ghi đủ

**🔴 ① Cổng bất biến của agent KHÔNG THỂ bắt lỗi rò prompt** — vì nó lấy mẫu một model không nằm
trong `SHADOW_GATE_MODELS`. Lần **thứ năm** trong ngày mắc họ «dụng cụ đo đứng sai chỗ».

**🔴 ② So tập voter đầy đủ với bản bundle chỉ lưu top-10** — báo 15 ca lệch giả.

**🔴 ③ Thiếu hai phép `round()` của bản gốc** — báo tiếp 19 ca lệch giả.

**🔴 ④ META test đầu xoá kết quả CẢ BA ngày mẫu cùng lúc** — báo `ORACLE_CONTAMINATED` giả 6/8 ô.

**🟡 ⑤ Quét mốc cắt dựa trên giả thuyết sai** — mất một vòng chạy vì so bằng tập voter đã cắt.

---

## 9 · Gỡ về

**Không áp dụng** — work package này **không ghi production, không deploy, không đổi code
production**. Mọi phép tính trên `artifacts/v11159_phan_tich.db` (clone). Xoá clone là gỡ hết.

---

## 10 · Theo dõi tiếp — liệt kê ĐỦ

| việc | trạng thái | ai chặn |
|---|---|---|
| **vá lỗ rò `gpt-oss-120b`** | **CHỜ OWNER** | chạm đường official — cần packet riêng |
| `SCHEDULED_SHADOW_PROMPT_CLEAN_PROVEN` | KHÔNG ĐẠT | cần thêm `runtime_prompt_sha256` vào trace |
| mệnh lệnh treo `gpt_analyzer.py:3151` | chưa xử | `PRJ_PROMPT_DANGLING` |
| chú thích ngược `main.py:12306-12307` | chưa xử | |
| 7/8 trường lineage 3-càng | chưa tồn tại | |
| 6/62 dòng trace không nối được sang `predictions` | chưa truy nguyên | |
| journal giờ 17 có 0 dòng dù 12 model chạy | chưa giải thích được | |
| 111 ô thiếu lớp L3 | gắn `RM-13` | trước 14/04 chưa có registry |
| luật khử trùng quá gắt (C = A) | cần thiết kế lại | |
| materialize `output_counterfactual_rank` vào production | **CHỜ OWNER** | cần materialization proposal riêng |
| `23/09/2026` | **READOUT CHECKPOINT** | KHÔNG phải hạn buộc promote/cutover |

---

## 11 · Đối chiếu hoàn tất

| hạng mục | tầng |
|---|---|
| tái lập selector | `TESTED` |
| khoá chống oracle | `TESTED` |
| ba comparator + add-one | `MEASURED_ONLY` |
| roster theo thời điểm | `MEASURED_ONLY` |
| nền 14 ngày | `MEASURED_ONLY` |
| hợp đồng ngữ nghĩa cột | `AUDITED_ONLY` |
| khoá 3-càng | `MEASURED_ONLY` |
| context-only semantic clean | **`BLOCKED`** — thiếu vân tay prompt runtime |
| materialize vào production | `NOT_STARTED` |

---

## Nguồn ba lớp (§62)

### `OWNER_SAID`
- 03/09 ~22:05 — *«Tiếp theo là gì em? … Hôm nay vẫn tệ như mọi ngày»*
- 03/09 ~22:15 — `PROMPT 43 R1 · CONTINUATION … COUNTERFACTUAL RANK REPAIR OFFLINE-FIRST`
- 03/09 ~23:5x — *«làm xong chả báo cáo gì là sao em?»*
- 04/09 ~00:0x — *«ok vậy đợi soi xong tổng hợp đề xuất báo cáo tổng hợp 1 lần luôn em»*

### `CODE_DID`
- `SHADOW_GATE_MODELS ∩ get_output_eligible_ids() = ['gpt-oss-120b']` cả ba miền
- bundle `823` MB `BT=32`, voter gồm `gpt-oss-120b`; trace 6458 `regime=CONTEXT_ONLY_V2`
- Gate D 99/99, lệch `0,000000`; META 6/6; artifact `9474b7bc…`
- `PRODUCTION_MUTATION_COUNT = 0`; `output_counterfactual_rank` `0/17.040`

### `NOT_VERIFIED`
- nội dung prompt THẬT gửi lúc `16:41:49` MT và `17:32:44` MB — **không thể** chứng minh với dữ
  liệu hiện có (không có hash prompt runtime)
- mức ảnh hưởng định lượng của phiếu `gpt-oss-120b` — chưa tính lại bundle, `n=1` ngày
- vì sao journal giờ 17 có 0 dòng

### `DOC_SAID`

- `docs/CURRENT_TRUTH_SSOT.md` §V11157/§V11158 ghi *«official không đổi một ký tự prompt»* —
  **`DOC_SAID` ≠ `CODE_DID`**. Đã rút lại ở mục 3 và ghi bản sửa vào `SSOT` §V11159 cùng phiên.
- `docs/CURRENT_TRUTH_SSOT.md` §V11116 (25/08) ghi *«`M0` vs nền: KHÔNG KHÁC — ba làn độc lập»*
  và *«bước xếp hạng không mang thông tin»* — **`DOC_SAID` = `CODE_DID`**: phép đo 90 ngày × 3
  miền của phiên này ra cùng kết luận, nên đây là **tái xác nhận**, không phải phát hiện mới.
- `main.py:12306-12307` chú thích *«For lo3 we clone official»* — **`DOC_SAID` ≠ `CODE_DID`**:
  code cách đó 110 dòng (`:12438`) ghi `lo3_cloned_from_official: False`. Chú thích chết.
- `artifacts/phase_checkpoints/SHADOW_MODEL_PROMOTION_MEASUREMENT_ROADMAP_20260427.md:50` —
  spec gốc của `output_counterfactual_rank` **CÒN NGUYÊN trong kho làm việc** nhưng **không có
  trên VPS** vì `artifacts/` bị gitignore. Vòng đầu agent kết luận «spec đã mất» — **SAI**, phản
  biện độc lập đã sửa.
- `CLAUDE.md` `RM-21` *«hằng số đo được chỉ đúng cho thước đã đo nó»* — phiên này là ca áp dụng
  trực tiếp: **mốc đóng băng** là hằng số **có thời hạn**, đã đổi ba lần.

---

TanPhatAI cần làm: ghi **`V11159`** — `governance_seq 475`, công khai bản này. Ghi **RÚT LẠI `PRJ-RETRACTION-001`**: câu *«official không đổi một ký tự prompt»* của `V11157`/`V11158` **SAI** — `gpt-oss-120b` là model DUY NHẤT ở giao `SHADOW_GATE_MODELS` × `output_eligible`, đã nhận prompt thí nghiệm trên chuỗi `ai_chain` và **là voter của chính số bạch thủ MB=32** (bundle 823). Hạ nhãn `SERVICE_ENV_RUNTIME_PROVEN`; **nhánh đối chứng official KHÔNG sạch từ 03/09**. Ghi **Gate D tái lập selector 99/99 = 100,0%** (lệch điểm `0,000000`), ngoại lệ duy nhất `2026-08-01` mã `REGISTRY_TRANSITION_DAY`. Ghi **Gate E `ANTI_ORACLE_PROVEN` 6/6**, artifact đóng băng `9474b7bc…`. Ghi **Gate F: KHÔNG comparator nào qua cổng Holm** — MT `b=4 c=0 p_Holm=0,375`; `A vs C` `b=0 c=0` cả ba miền; add-one tốt nhất `p=0,180`; **MT trần 13 đẩy ra `59 → 228`** nên "tăng" là **THAY THẾ**. Ghi **n cần: MT ~65 ngày · MN 907 · MB 1.295**. Ghi **`SCHEDULED_LANE_ROUTING_PROVEN` PASS** nhưng **`SCHEDULED_SHADOW_PROMPT_CLEAN_PROVEN` KHÔNG ĐẠT** (không có vân tay prompt runtime; mệnh lệnh treo `gpt_analyzer.py:3151`). Ghi **khoá 3-càng KHÔNG đổi**, 8/10 mệnh đề đúng, mệnh đề 7 CHƯA IMPLEMENT, tên «UCC» không tồn tại trong code. Ghi **`PRODUCTION_MUTATION_COUNT = 0`** và **`output_counterfactual_rank` vẫn `0/17.040`**. Ghi **`23/09/2026` = READOUT CHECKPOINT**, không phải hạn buộc promote. **Không mở Prompt 44. Không mở FU mới.** `POOL_VERDICT` giữ **`HOLD`**.
