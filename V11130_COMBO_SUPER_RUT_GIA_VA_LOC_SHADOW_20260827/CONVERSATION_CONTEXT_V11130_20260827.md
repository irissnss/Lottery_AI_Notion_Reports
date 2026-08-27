# CONVERSATION CONTEXT — V11130 · 27/08/2026

> Nguyên văn lời owner · agent làm gì · vấp ở đâu (§57.2). Giờ **Việt Nam (UTC+07:00)**.
> `ACTOR_RUNTIME = CLAUDE_CODE`.

---

## 1 · Owner nói gì — nguyên văn

Prompt tổng lực lần 43, hiệu lực **27/08/2026 22:34 ICT**:

> *« ML là thuần số học. LLM là thuần ngữ cảnh. Combo-Super là tầng HYBRID kết hợp ML + LLM,
> không phải model ML độc lập. »*
>
> *« Nếu rút AI trực tiếp nhưng Combo-Super, smart-ensemble, meta-learning hoặc TOTAL vẫn dùng
> AI đó: việc rút là giả. Phải xóa toàn bộ ảnh hưởng gián tiếp cùng effective cycle. »*
>
> *« Điều gì chưa rõ phải ghi `NOT_VERIFIED` và lấy bằng chứng từ code/DB/runtime. Cấm suy diễn,
> phán đại hoặc lấy lời TanPhatAI làm bằng chứng kỹ thuật. »*
>
> *« Bắt buộc giải thích chính xác 17 MAIN so với 16 KEEP_OFFICIAL. Nếu chưa giải thích được:
> ghi `NOT_VERIFIED`. Cấm đổi roster dựa trên con số đó. »*
>
> *« gpt-5.5 và qwen3-max-thinking: phải verify runtime. Nếu đúng, ghi
> `ALREADY_SHADOW_NO_ACTION`. Cấm báo "đã rút" một model vốn không ở FINAL. »*
>
> *« Không chỉ đọc config tĩnh. Ghi đúng model thực sự đi vào Combo mỗi ngày × miền. »*
>
> *« Cấm báo DONE khi mới audit hoặc viết report. »*
>
> *« Mọi đề xuất trước đây của TanPhatAI về smart-ml, xgboost hoặc model khác: chỉ là giả thuyết.
> Không phải lệnh. »*

---

## 2 · Agent làm gì

| GĐ | việc | kết quả |
|---|---|---|
| 0 | reconcile 17 vs 16 | 🟢 **mâu thuẫn KHÔNG tồn tại** — cả hai đều 17 |
| 0b | dependency graph | **12 model đếm hai lần** · `meta-learning` (ENSEMBLE) trong `ML_MODELS` |
| 3 | đọc `AI_MODELS` từ code | 17 khai · **9 official · 3 shadow · 5 inactive/không tồn tại** |
| 3 | 🔴 tìm cơ chế «rút giả» | `combo_super.py:351` **không lọc `run_source`** |
| 3 | xác minh bằng DB | shadow có **8 lượt/7 ngày**, sàn 5 ⇒ **qua cổng** |
| 3 | đọc manifest thật | 🔴 **`gemini-3.5-flash` ĐÃ có mặt trong Combo (1/24)** |
| 3 | đo coverage Combo | **2,9/8** trung bình — *«Coverage thấp»* lặp lại |
| 2 | mô phỏng trước khi vá | 15 → **12** dự tuyển · 3 miền đều còn **4 ML + 8 AI** |
| 7 | **deploy CLASS B** | PID `2671007 → 2694667` · `SHADOW_CON_LAI []` |
| — | phát hành | báo cáo này |

---

## 3 · Vấp ở đâu — kể cả vấp do chính agent gây ra

### V1 · 🔴 «Mâu thuẫn 17 vs 16» hoá ra là **lỗi nhãn của chính tôi**

Đề bài yêu cầu giải thích chênh lệch. Đo lại: **cả hai bảng đều cho 17**, tập chênh **rỗng cả hai
chiều**.

Con số `16` trong `V11128` do script của tôi gán `SHADOW_MEASURE` cho model có **mẫu < 30** —
`gpt-5-mini` chỉ có 13 mẫu nên bị xếp nhầm dù là `OFFICIAL_PRIMARY`.

**Nếu không tự truy**, tôi sẽ đi tìm một mâu thuẫn không tồn tại, hoặc tệ hơn — đổi roster dựa
trên một con số sai.

### V2 · 🔴 Tôi báo *«manifest Combo RỖNG»* — và điều đó **SAI**

Truy vấn đầu dùng dấu phân cách tab, vỡ trên JSON nhiều dòng, trả **0 bản ghi**. Tôi suýt kết luận
*«không có `combo_input_manifest` trong DB»* và ghi `NOT_VERIFIED`.

Đọc lại **từng dòng một** thì manifest **có**, dài **769–1651 ký tự**, cấu trúc đầy đủ:
`numbers` · `source_weights` · `active_rules_applied` · `warnings` · `meta` · `knowledge_weights`.

**Chính manifest đó mới là thứ chứng minh được `gemini-3.5-flash` đã vào Combo.** Nếu tin con số
`0`, tôi đã bỏ lỡ bằng chứng quan trọng nhất của phiên.

### V3 · 🔴 Suýt vá mà **không mô phỏng trước**

Phản xạ đầu là thêm bộ lọc `run_source` ngay. Nhưng Combo đang chạy ở **2–3/8 nguồn** — lọc thêm
có thể đẩy xuống dưới sàn và **làm hỏng Combo**.

Mô phỏng trước cho thấy còn **12 model, 4 ML + 8 AI ở cả ba miền** ⇒ an toàn. **Không mô phỏng
thì đây là một thay đổi mù trên đường sinh dự đoán.**

### V4 · 🔴 Bản vá của tôi ban đầu **khác thứ tôi đã mô phỏng**

Tôi viết `(run_source IS NULL OR run_source NOT LIKE '%shadow%')` trong khi mô phỏng chỉ dùng
`run_source NOT LIKE '%shadow%'`.

Kiểm: `model_daily_eval` có **0 dòng NULL** trong 7 ngày, và hai biến thể cho **kết quả y hệt
(16 model)**. Nên vế `IS NULL` là phòng thủ vô hại. **Nhưng nếu có dòng NULL thì bản deploy đã
khác bản đã kiểm** — đúng loại chênh âm thầm giữa «thứ đã thử» và «thứ đã đẩy».

### V5 · `gpt-5-mini` mất tư cách dự tuyển — và đó **không phải cắt model**

Nó là `OFFICIAL_PRIMARY` nhưng có **0 lượt eval sạch** trong 7 ngày. Tức nó **vốn chỉ đủ tư cách
nhờ chính dòng shadow**. Sau khi lọc, nó không còn qua cổng.

Ghi đúng bản chất: **không phải bị cắt — nó chưa bao giờ đủ tư cách hợp lệ.** Nguyên nhân gốc vẫn
`NOT_VERIFIED` (mục 7 báo cáo).

---

## 4 · Điều agent **không** làm, và vì sao

| không làm | vì sao |
|---|---|
| dọn 8 mục chết trong `AI_MODELS` | giữ diff CLASS B **nhỏ nhất**; bộ lọc `run_source` đã đạt trọn mục tiêu an ninh, còn 5 mục không tồn tại vốn **không thể qua cổng mẫu** ⇒ hiệu ứng bằng 0 |
| gỡ `meta-learning` khỏi `ML_MODELS` | **quyết định kiến trúc**, không phải sửa lỗi. Combo đang chỉ có 2–3 nguồn; gỡ ngay có thể đổi *«phiếu không độc lập»* thành *«quá ít phiếu»* ⇒ trình thành câu hỏi duy nhất |
| cắt bất kỳ model nào | bản vá **không xoá model**, chỉ bịt đường vòng |
| báo *«đã rút gpt-5.5 / qwen3-max-thinking»* | runtime xác nhận **cả hai vốn ở shadow và KHÔNG trong `AI_MODELS`** ⇒ `ALREADY_SHADOW_NO_ACTION`. Owner cấm báo «đã rút» model vốn không ở FINAL |
| LLM context-only atomic | 46 dấu vết đã có bản đồ; **chưa emit được prompt thật** nên không quét ngược được — `§60.1` |
| nâng `RUNTIME_PROVEN` | bản vá đổi cách chọn cho **lượt sinh kế tiếp** (05:00 ngày 28/08) |
| thi hành đề xuất cũ của TanPhatAI | Owner ghi rõ đó **chỉ là giả thuyết, không phải lệnh** |
| ghi vào production DB | mọi truy vấn `-readonly` + chặn từ khoá ghi phía client |

---

## 5 · Trạng thái cuối

| | |
|---|---|
| `combo_super.py` | `ed503dfe…` → `47047b1d…` · **RUNTIME_LOADED** |
| MainPID | **2694667** · health **200** · log lỗi **0** |
| `FU-438` | **không regression** — 401 cả ba endpoint kiểm |
| 4 bảng khoá | **KHÔNG ĐỔI** |
| FINAL 27/08 | **KHÔNG ĐỔI** — `MB:61:WIN · MN:61:LOSE · MT:68:WIN` |
| roster | **không model nào bị xoá** |
| `effective_from` | **lượt kế tiếp — 05:00 ngày 28/08** |
| `NOT_VERIFIED` | **5 mục**, có người chịu trách nhiệm |

---

TanPhatAI cần làm: ghi **«rút giả» đã chứng minh** — `combo_super.py:351` không lọc `run_source`, hai model SHADOW đủ tư cách dự tuyển (**8 lượt/7 ngày**, sàn 5), và **`gemini-3.5-flash` ĐÃ có mặt trong manifest Combo 1/24**. Bản vá **đã deploy**, **`RUNTIME_LOADED`**, `effective_from` **05:00 ngày 28/08** — **đừng** nâng `RUNTIME_PROVEN` sớm. Ghi hai đính chính của Agent: **17 = 17, không có mâu thuẫn** (16 là lỗi nhãn do `gpt-5-mini` 13 mẫu); **manifest Combo KHÔNG rỗng** (truy vấn trước vỡ định dạng). Ghi **Combo thực chạy 2–3/8 model** và **`AI_MODELS` khai 17 nhưng chỉ 9 dùng được** (`o3-deep-research` chưa bao giờ có bản ghi). **`gpt-5.5` và `qwen3-max-thinking`: `ALREADY_SHADOW_NO_ACTION`** — đã verify runtime, không có gì để rút. Bảng **`NOT_VERIFIED` 5 mục** cần người lấy bằng chứng. **Không model nào bị cắt.**
