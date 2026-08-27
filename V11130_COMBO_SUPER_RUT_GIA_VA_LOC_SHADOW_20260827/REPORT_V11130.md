# REPORT V11130 — «RÚT GIẢ» ĐÃ ĐƯỢC CHỨNG MINH VÀ BỊT: SHADOW ĐI VÒNG VÀO FINAL QUA COMBO-SUPER

```
REPORT_VERSION        : V11130
REPORT_TITLE          : Reconcile roster · dependency graph · Combo-Super AS-IS ·
                        chứng minh shadow lọt FINAL gián tiếp · deploy bộ lọc run_source
WORK_DATE_ICT         : 2026-08-27
PUBLISHED_AT_ICT      : xem mục bàn giao
TIMEZONE              : Asia/Ho_Chi_Minh / UTC+07:00
OWNER_DECISION        : prompt 43 · D-25 WINDOWED_AUTODEPLOY (CLASS B)
ACTOR_RUNTIME         : CLAUDE_CODE
PREVIOUS_PUBLIC_HEAD  : 93bc1fde0f19ead54cbb53d92c91356a9d042aed
LABELS                : CLASS_B_DEPLOYED · RUNTIME_LOADED · SHADOW_LEAK_FIXED ·
                        NOT_VERIFIED_PRESENT · OWNER_DECISION_PENDING
```

---

## 1 · TÓM TẮT BẰNG LỜI THƯỜNG

Owner cảnh báo một khả năng: *«nếu rút AI trực tiếp nhưng Combo-Super vẫn dùng AI đó thì việc rút
là giả»*.

**Phiên này chứng minh điều đó ĐÃ XẢY RA THẬT, và đã bịt.**

| bằng chứng | |
|---|---|
| Bảng quyết định *model nào được bỏ phiếu* (`_ti_le_bach_thu`) đọc `model_daily_eval` **KHÔNG lọc `run_source`** | `combo_super.py:351` |
| ⇒ dòng `shadow_auto_eval` được đếm làm **lượt dự tuyển** | — |
| `gemini-3.5-flash` và `gemini-3.6-flash` — **cả hai là SHADOW** — có **8 lượt/7 ngày** ở **cả ba miền**, vượt sàn `MIN_MAU_DU_TUYEN = 5` | đo từ DB |
| 🔴 Đọc **manifest thật**: `gemini-3.5-flash` **ĐÃ CÓ MẶT** trong một lượt Combo-Super | `predictions.reasoning_json` |

⇒ **Một model đang bị giữ ở shadow đã thực sự đi vòng vào đường tới FINAL.**

**Đã vá và deploy** — thêm bộ lọc `run_source` vào đúng truy vấn đó. Mô phỏng trước khi vá:
dự tuyển **15 → 12** model, **cả ba miền vẫn còn 4 ML + 8 AI** nên Combo không cạn nguồn.
Sau deploy, gọi thẳng hàm trên VPS xác nhận **shadow đã biến mất khỏi bảng dự tuyển**.

**Và một phát hiện thứ hai, không kém quan trọng:** Combo-Super — vốn được mô tả là tầng hợp
nhất ML + LLM — **thực tế chỉ chạy với 2–3 model** (trung bình **2,9**; min 2; max 3), với cảnh
báo *«Coverage thấp: chỉ 2/8 models hoạt động»* lặp lại liên tục.

---

## 2 · GĐ-0 · RECONCILE «17 vs 16» — mâu thuẫn **KHÔNG TỒN TẠI**

| phép đếm | kết quả |
|---|---|
| `predictions` · 30 ngày · `run_source IN (auto_daily, ai_chain)` | **17** |
| `model_daily_eval` · 30 ngày · `run_source NOT LIKE '%shadow%'` | **17** |
| tập chênh hai chiều | **rỗng cả hai** |

**Cả hai bảng đều cho 17.** Con số `16` trong `V11128` là **lỗi nhãn của chính tôi**: script gán
`SHADOW_MEASURE` cho model có **mẫu < 30**, và `gpt-5-mini` chỉ có 13 mẫu nên bị xếp nhầm dù nó
là `OFFICIAL_PRIMARY`. **16 + `gpt-5-mini` = 17.**

### Roster sống — 30 model

| trạng thái | loại | số |
|---|---|---|
| `OFFICIAL_PRIMARY` | `LLM_BASE` | **9** |
| `OFFICIAL_PRIMARY` | `ML_BASE` | **4** — `lstm` `random-forest` `smart-ml` `xgboost` |
| `OFFICIAL_PRIMARY` | `ENSEMBLE` | **2** — `meta-learning` `smart-ensemble` |
| `OFFICIAL_PRIMARY` | `HYBRID_COMBO` | **2** — `combo-super` `combo-no-token` |
| `SHADOW` | `LLM_BASE` | **13** |

---

## 3 · DEPENDENCY GRAPH — BASE → COMBO → TOTAL → FINAL

### 3.1 · 🔴 12 model được đếm **HAI LẦN** vào FINAL

`claude-opus-4-6` · `claude-sonnet-4-6` · `deepseek-reasoner` · `gemini-2.5-flash` ·
`gemini-2.5-pro` · `glm-5.1` · `gpt-5-mini` · `gpt-5.4` · `gpt-oss-120b` · `lstm` ·
`random-forest` · `xgboost`

Mỗi model vừa bỏ phiếu **trực tiếp** vào TOTAL, vừa bỏ phiếu **lần nữa** qua Combo-Super.

### 3.2 · 🔴 `meta-learning` — một **ENSEMBLE** — nằm trong `ML_MODELS` của Combo

```
combo_super.py:64   ML_MODELS = ['meta-learning', 'lstm', 'xgboost', 'random-forest']
```

`meta-learning` **không phải base ML**; nó là ensemble tổng hợp từ chính các base ML khác. Đặt nó
vào `ML_MODELS` là để một tổng hợp **bỏ phiếu như thể nó là nguồn độc lập**.

### 3.3 · 🔴 `AI_MODELS` khai **17** mục — chỉ **9** là thật

```
combo_super.py:74   AI_MODELS = [17 mục]
```

| nhóm | số | model |
|---|---|---|
| 🟢 `OFFICIAL_PRIMARY` | **9** | `claude-sonnet-4-6` `gemini-2.5-flash` `claude-opus-4-6` `gemini-2.5-pro` `deepseek-reasoner` `glm-5.1` `gpt-oss-120b` `gpt-5-mini` `gpt-5.4` |
| 🔴 **SHADOW** | **3** | `gemini-3.5-flash` `gemini-3.6-flash` `grok-4.20-multi-agent` |
| 🔴 **INACTIVE** | **4** | `qwen3-coder` (249 bản ghi, không có 30 ngày qua) · `qwen3.6-plus` (216) · `o4-mini` (47) · `gpt-5.1` (20) |
| 🔴 **KHÔNG TỒN TẠI** | **1** | `o3-deep-research` — **0 bản ghi, chưa bao giờ** |

---

## 4 · 🔴 «RÚT GIẢ» — CHỨNG MINH ĐẦY ĐỦ

### 4.1 · Cơ chế, đọc từ code

`combo_super.py:351`, trong `_ti_le_bach_thu()` — **bảng quyết định model nào được bỏ phiếu**:

```sql
FROM model_daily_eval
WHERE region = ? AND date >= date('now','localtime', ?)
GROUP BY ai_model
```

**Không có lọc `run_source`.** Dòng `shadow_auto_eval` được tính là lượt dự tuyển hợp lệ.

### 4.2 · Hậu quả, đo từ DB

| model | trạng thái | lượt/7 ngày mỗi miền | sàn | kết quả |
|---|---|---|---|---|
| `gemini-3.5-flash` | 🔴 **SHADOW** | **8** | 5 | ✅ **QUA CỔNG** |
| `gemini-3.6-flash` | 🔴 **SHADOW** | **8** | 5 | ✅ **QUA CỔNG** |
| `grok-4.20-multi-agent` | SHADOW | 0 | 5 | ❌ không qua |

### 4.3 · 🔴 Bằng chứng cuối — nó **đã thực sự xảy ra**

Đọc **manifest thật** (`predictions.reasoning_json` của `combo-super`), 24 lượt gần nhất:

| model trong manifest | số lần |
|---|---|
| `random-forest` | 10/24 |
| `gemini-2.5-pro` | 8/24 |
| `xgboost` | 6/24 |
| `claude-o…` | 6/24 |
| `meta-learning` | 5/24 |
| `deepseek-r…` | 3/24 |
| `lstm` | 2/24 |
| 🔴 **`gemini-3.5-flash`** | **1/24** ← **SHADOW đã vào Combo** |

**Không phải rủi ro lý thuyết. Nó đã xảy ra.**

### 4.4 · Phát hiện đi kèm — Combo chạy với **2–3 model**, không phải 8

| | |
|---|---|
| tổng model vào Combo | **trung bình 2,9** · min **2** · max **3** |
| cảnh báo lặp lại trong manifest | *«Coverage thấp: chỉ 2/8 models hoạt động»* · *«chỉ 3/8»* |
| ví dụ 27/08 MB | `total_models: 3` · `ml_success: 2` · `ai_success: 1` |

⇒ Cái tên *«Combo-Super»* **không** phản ánh kiến trúc thật. Nó đang là một tổng hợp **2–3
nguồn**, phần lớn là `random-forest` + một LLM.

---

## 5 · BẢN VÁ ĐÃ DEPLOY (CLASS B)

### 5.1 · Mô phỏng **trước** khi vá — điều kiện bắt buộc

| miền | dự tuyển hiện tại | sau khi lọc | mất | còn lại |
|---|---|---|---|---|
| MN | 15 | **12** | `gemini-3.5-flash` `gemini-3.6-flash` `gpt-5-mini` | 🟢 **4 ML + 8 AI** |
| MT | 15 | **12** | như trên | 🟢 **4 ML + 8 AI** |
| MB | 15 | **12** | như trên | 🟢 **4 ML + 8 AI** |

**Cả ba miền vẫn thừa sàn «≥1 ML và ≥1 AI»** ⇒ vá được, không cần replacement.

> ⚠️ **`gpt-5-mini` mất tư cách dự tuyển** — nó là `OFFICIAL_PRIMARY` nhưng có **0 lượt eval sạch**
> trong 7 ngày. Tức nó **vốn đã chỉ đủ tư cách nhờ chính dòng shadow**. Đây cũng là model gây ra
> nhầm lẫn «16 vs 17» ở mục 2. Không phải bị cắt — nó **chưa bao giờ đủ tư cách hợp lệ**.

Kiểm thêm trước khi vá: `model_daily_eval` có **0 dòng `run_source` NULL** trong 7 ngày, và hai
biến thể truy vấn (có/không vế `IS NULL`) cho **kết quả y hệt** ⇒ bản vá khớp đúng mô phỏng.

### 5.2 · Deploy và bằng chứng

| bậc | bằng chứng |
|---|---|
| cửa | CLASS B · **22:5x — sau FINAL cả ba miền, ngoài block 15:30–18:15** |
| backup | hash **khớp gốc** `ed503dfe1a40…` |
| `py_compile` | OK cả local lẫn VPS |
| **kiểm logic trên VPS** | gọi thẳng `combo_super._ti_le_bach_thu('MN', 7)` → **`SHADOW_CON_LAI []`** ✅ |
| `RUNTIME_LOADED` | PID **2671007 → 2694667** · hash runtime **khớp** tệp gửi |
| `FU-438` không regression | `/api/final-bundle` `/api/predictions` `/api/slice-recommendation` → **401** cả ba |
| log lỗi | **0** |
| **không drift** | `predictions` · `final_bundles` · **FINAL 27/08** · `model_daily_eval` — **cả bốn KHÔNG ĐỔI** |

### 5.3 · Nhãn runtime — đúng bậc

**`RUNTIME_LOADED`.** ⛔ **Chưa** `RUNTIME_PROVEN`: bản vá đổi **cách chọn model cho lượt sinh
kế tiếp**, mà lượt đó là **05:00 ngày 28/08**. Bằng chứng hành vi có từ lúc đó.

**`effective_from` = lượt kế tiếp. FINAL ngày 27/08 KHÔNG ĐỔI** — đã chứng minh ở mục 5.2.

---

## 6 · VERDICT TỪNG MODEL

| model | loại | verdict | căn cứ |
|---|---|---|---|
| `gemini-3.5-flash` | LLM SHADOW | **`ALREADY_SHADOW_NO_ACTION`** + đã bịt đường vòng | vốn là shadow; nay không còn dự tuyển được |
| `gemini-3.6-flash` | LLM SHADOW | **`ALREADY_SHADOW_NO_ACTION`** + đã bịt | như trên |
| `grok-4.20-multi-agent` | LLM SHADOW | `ALREADY_SHADOW_NO_ACTION` | 6 bản ghi/30 ngày, chưa từng qua cổng |
| **`gpt-5.5`** | LLM SHADOW | 🟢 **`ALREADY_SHADOW_NO_ACTION`** | **runtime xác nhận**: `run_source = shadow_auto_eval`, **không** trong `AI_MODELS` của Combo ⇒ **không ở FINAL, không có gì để rút** |
| **`qwen3-max-thinking`** | LLM SHADOW | 🟢 **`ALREADY_SHADOW_NO_ACTION`** | như trên — **xác nhận đúng như báo cáo trước** |
| `qwen3-coder` `qwen3.6-plus` `o4-mini` `gpt-5.1` | INACTIVE | **`REPLACE_REQUIRED`** (dọn khai báo) | còn trong `AI_MODELS` nhưng **không hoạt động 30 ngày** |
| `o3-deep-research` | KHÔNG TỒN TẠI | **`REPLACE_REQUIRED`** (dọn khai báo) | **0 bản ghi, chưa bao giờ** |
| `meta-learning` | ENSEMBLE | **`NOT_VERIFIED`** | đang nằm trong `ML_MODELS` — cần quyết định kiến trúc, xem mục 8 |
| `gpt-5-mini` | LLM OFFICIAL | **`NOT_VERIFIED`** | official nhưng **0 lượt eval sạch**/7 ngày — cần truy nguyên nhân |
| 9 LLM official còn lại | LLM_BASE | **`KEEP_FINAL`** | có lượt sạch, qua cổng |
| 4 ML base + `lstm` | ML_BASE | **`KEEP_FINAL`** · `lstm` **giữ riêng** | không hard-collapse |

⛔ **Không model nào bị cắt trong phiên này.** Bản vá **không xoá model** — nó chỉ **bịt đường
vòng** mà shadow đang dùng.

---

## 7 · BẢNG `NOT_VERIFIED`

| # | chưa rõ điều gì | thiếu bằng chứng nào | cần kiểm ở đâu | ai lấy | nếu chưa có thì sao | vẫn tiếp tục được gì |
|---|---|---|---|---|---|---|
| 1 | `meta-learning` (ENSEMBLE) trong `ML_MODELS` có làm phiếu bị nhân đôi thật không | contribution trace theo từng số | `combo_super.py` hàm `_chon_top` + `run_combo_super` | Agent IDE | không định lượng được mức nhân đôi | vẫn dựng được lean TOTAL shadow |
| 2 | `gpt-5-mini` vì sao **0 lượt eval sạch** dù `OFFICIAL_PRIMARY` | đường ghi `model_daily_eval` cho model này | writer `scheduler._run_model_daily_eval` + `run_source` gốc | Agent IDE | không biết nó có thật sự đang phục vụ FINAL không | không chặn việc gì |
| 3 | **12 model đếm hai lần** ảnh hưởng FINAL bao nhiêu | phép đo paired có/không Combo | `TOTAL_LEAN_SHADOW` chưa dựng | Agent IDE | chưa biết bỏ Combo có tốt hơn không | vẫn giữ M0 official |
| 4 | prompt phát ra dài bao nhiêu | emit prompt thật cần ngữ cảnh DB đầy đủ | `gpt_analyzer.create_analysis_prompt` + fixture | Agent IDE | chưa quét ngược được sau khi sửa | bản đồ 46 dấu vết đã có |
| 5 | 3-càng | writer/scorer/cột | 253 bảng — đã tra, **không có** | Agent IDE | `MISSING_PIPELINE` | không chế số, trả `NO_VALID_3CANG` |

---

## 8 · CHƯA LÀM — VÀ VÌ SAO

| việc | trạng thái | lý do |
|---|---|---|
| dọn 8 mục chết trong `AI_MODELS` | **CHUẨN BỊ XONG**, chưa deploy | giữ diff CLASS B **nhỏ nhất có thể** trong một lần. Bộ lọc `run_source` đã đạt trọn mục tiêu an ninh; 5 mục không tồn tại vốn **không thể qua cổng mẫu** nên hiệu ứng bằng 0. Danh sách chính xác ở mục 3.3 |
| gỡ `meta-learning` khỏi `ML_MODELS` | **CHƯA** | đây là **quyết định kiến trúc**, không phải sửa lỗi — cần đo mức nhân đôi trước (`NOT_VERIFIED` #1) |
| LLM context-only atomic | **CHƯA** | 46 dấu vết đã lập bản đồ ở `V11129`; chưa emit được prompt thật nên **không quét ngược được** — `§60.1` cấm nửa vời |
| persist `ML_PURE_MATH` / `LLM_CONTEXT_ONLY` shadow | **CHƯA** | phụ thuộc việc trên |
| `TOTAL_LEAN_SHADOW` · `COMBO_SUPER_VNEXT_SHADOW` | **CHƯA** | — |
| 3-càng | **CHƯA** | `MISSING_PIPELINE` |
| backlog (SC-05/08 · 34 script · FU-440/441/443/444 · 23 report · QD-041) | **CHƯA** | — |

---

## 9 · BA LỚP NGUỒN (§62)

### `OWNER_SAID`

> *« Combo-Super là tầng HYBRID kết hợp ML + LLM, không phải model ML độc lập. »*
>
> *« Nếu rút AI trực tiếp nhưng Combo-Super, smart-ensemble, meta-learning hoặc TOTAL vẫn dùng AI
> đó: việc rút là giả. »*
>
> *« Điều gì chưa rõ phải ghi `NOT_VERIFIED` và lấy bằng chứng từ code/DB/runtime. Cấm suy diễn,
> phán đại. »*
>
> *« Cấm báo DONE khi mới audit hoặc viết report. »*
>
> *« gpt-5.5 và qwen3-max-thinking: phải verify runtime. Cấm báo "đã rút" một model vốn không ở
> FINAL. »*

### `CODE_DID`

| việc | evidence |
|---|---|
| `17 = 17`, chênh rỗng | hai truy vấn `COUNT(DISTINCT ai_model)` |
| thiếu lọc `run_source` | `combo_super.py:351` |
| shadow qua cổng | `gemini-3.5/3.6-flash` **8 lượt/7 ngày** × 3 miền, sàn 5 |
| **shadow ĐÃ vào Combo** | `predictions.reasoning_json` — `gemini-3.5-flash` **1/24** manifest |
| Combo chạy 2–3 model | `meta.total_models` trung bình **2,9** |
| `AI_MODELS` 17 mục | `combo_super.py:74` — 9 official · 3 shadow · 5 inactive/không tồn tại |
| mô phỏng | 15 → **12** dự tuyển, 3 miền đều còn **4 ML + 8 AI** |
| deploy | PID `2671007 → 2694667` · `SHADOW_CON_LAI []` gọi thẳng hàm trên VPS |
| không drift | 4 bảng khoá **không đổi** |

### `DOC_SAID`

| nguồn | ghi gì |
|---|---|
| `CLAUDE.md §59` | pool combo thật là `ML_MODELS` + `AI_MODELS`, **không** phải danh sách 15 model official |
| `RM-10` | cấm kết luận theo tên đoán — đã tra `pragma`/`grep` thay vì đoán |
| `RM-13` | nguồn sai thì kết luận sai |
| `§60.1` | bỏ nửa chừng còn tệ hơn không làm |

### 🔴 BA LỚP LỆCH NHAU

| lệch | chi tiết |
|---|---|
| `DOC_SAID` ≠ `CODE_DID` | tên *«Combo-Super»* gợi ý hợp nhất nhiều nguồn; thực tế **2–3 model** |
| `DOC_SAID` ≠ `CODE_DID` | `AI_MODELS` khai **17**; thật chỉ **9** dùng được |
| nội bộ phiên | `V11128` báo **16** official — sai vì nhãn của chính tôi; đúng là **17** |
| nội bộ phiên | tôi báo `reasoning_json` **rỗng** ⇒ *«không có manifest»*; **sai** — truy vấn của tôi vỡ định dạng, manifest **có** và dài 769–1651 ký tự |

---

## 10 · MUTATION / ROLLBACK LOG

| # | thay đổi | gỡ về |
|---|---|---|
| 1 | `combo_super.py`: `ed503dfe…` → `47047b1d…` (**+1 dòng lọc** + khối chú thích) | bản sao lưu trên VPS, hash **khớp gốc**; tự động gỡ về đã cài, không phải dùng |
| 2 | restart dịch vụ ×1 | như trên |

**KHÔNG thay đổi:** ghi DB · prediction/FINAL/M0 · roster (không model nào bị xoá) · prompt ·
`main.py` · `scheduler.py` · credential · SSH · hook · Notion · Git history · push code kho riêng.

---

## 11 · MỘT CÂU OWNER CẦN XÁC NHẬN

**Vấn đề:** `combo_super.ML_MODELS` chứa `meta-learning`, vốn là **ENSEMBLE** chứ không phải base
ML. Nó khiến một tổng hợp bỏ phiếu **như thể là nguồn độc lập**, bên cạnh chính các base ML mà
nó đã tổng hợp.

**Bằng chứng:** `combo_super.py:64` · `meta-learning` xuất hiện **5/24** manifest Combo.

**Được gì nếu gỡ:** phiếu trong Combo trở về đúng nghĩa độc lập; giảm nhân đôi ảnh hưởng.
**Mất gì:** Combo hiện chỉ chạy **2–3 nguồn**; gỡ một nguồn có thể đẩy xuống **1–2** ở vài
ngày–miền, và `random-forest` (10/24) sẽ càng chi phối.
**Khuyến nghị:** **chưa gỡ ngay.** Đo mức nhân đôi trước (`NOT_VERIFIED` #1), rồi gỡ kèm bù
nguồn — nếu không sẽ đổi *«phiếu không độc lập»* thành *«quá ít phiếu»*.
**Rollback:** khôi phục dòng 64 từ bản sao lưu.

> ### ❓ Owner có đồng ý để `meta-learning` **tạm ở lại** `ML_MODELS` cho tới khi đo xong mức nhân đôi và chuẩn bị được nguồn bù, thay vì gỡ ngay lượt này không?

---

TanPhatAI cần làm: ghi vào `docs/FOLLOW_UP_TRACKER.md` phát hiện **«rút giả» đã được chứng minh**: truy vấn quyết định phiếu bầu (`combo_super.py:351`) **không lọc `run_source`**, khiến `gemini-3.5-flash` và `gemini-3.6-flash` — **cả hai SHADOW** — đủ tư cách dự tuyển (**8 lượt/7 ngày**, sàn 5), và **`gemini-3.5-flash` ĐÃ THỰC SỰ có mặt trong manifest Combo (1/24)**. Ghi rằng bản vá **đã deploy**, trạng thái **`RUNTIME_LOADED`**, `effective_from` = **lượt 05:00 ngày 28/08** — **đừng** ghi `RUNTIME_PROVEN` trước lúc đó. Ghi hai đính chính của chính Agent: **`17 = 17`, không có mâu thuẫn** (con số 16 ở `V11128` là lỗi nhãn do `gpt-5-mini` chỉ có 13 mẫu), và **manifest Combo KHÔNG rỗng** (truy vấn trước của Agent vỡ định dạng). Ghi phát hiện kiến trúc: **Combo-Super thực tế chỉ chạy 2–3 model** (trung bình 2,9/8), và **`AI_MODELS` khai 17 mục nhưng chỉ 9 dùng được** — 3 shadow, 4 inactive, 1 (`o3-deep-research`) **chưa bao giờ có bản ghi nào**. **`gpt-5.5` và `qwen3-max-thinking` đã xác minh runtime: cả hai vốn ở shadow, KHÔNG trong `AI_MODELS` của Combo ⇒ không có gì để rút.** Bảng **`NOT_VERIFIED` 5 mục** ở mục 7 cần người lấy bằng chứng. **Không model nào bị cắt trong phiên này.**
