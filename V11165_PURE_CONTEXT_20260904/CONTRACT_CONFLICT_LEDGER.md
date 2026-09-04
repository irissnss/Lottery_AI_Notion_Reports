# SỔ XUNG ĐỘT HỢP ĐỒNG ĐẦU RA

**V11165 · Làn sóng 2 · Gate 6 · 2026-09-05 ICT**

> Gate 6 yêu cầu: *«Ba thứ này đang mâu thuẫn nhau. CẤM tự chọn cách hiểu. Lập sổ xung đột rồi
> ĐỀ XUẤT MỘT contract duy nhất, kèm lý do và cái giá của từng lựa chọn.»*
> Sổ này lập **năm** xung đột — ba xung đột gate nêu, cộng hai xung đột đo ra trong lúc lập sổ.

| | |
|---|---|
| **Artifact máy đọc** | `artifacts/v11165_k6_conflict.json` (20.322 B · sha16 `23a01a2460433d21`) |
| **Bằng chứng số** | `artifacts/v11165_k6_bangchung.json` — lệnh tái lập `python _chay.py _k6_bangchung.py` |
| **Cửa sổ đo** | `2026-08-06 → 2026-09-04` (30 ngày), **2.407** dòng `predictions` |
| **Nguồn đo** | clone bất biến `/root/Lottery_AI_Test/artifacts/v11165_immutable.db`, mở `mode=ro` |

### Mã đọc ở đâu — phải nói rõ, vì hai nơi khác nhau

| đọc trên **VPS** (production thật) | `gpt_analyzer.py` sha16 `758c29c13185763f` · `main.py` · `_v11137_d30_lane.py` · `_v11161_rank_gen.py` · `_backfill_bundles.py` · `database.py` · `daily_evaluation.py` |
|---|---|
| **CHỈ CÓ Ở REPO LOCAL** | `_v11150_unified_candidate_contract.py` · `_v11156_ranked_adapter.py` |

Đã kiểm trực tiếp: hai tệp trên **không tồn tại** trong `/root/Lottery_AI_Test/web/backend/`, và
`grep 'ranked_candidates'` trên toàn `web/backend` của VPS trả **0 dòng**. Mọi kết luận về `UCC`
và `ranked adapter` trong sổ này là **đọc bản local**, trạng thái `CODED`, **chưa** runtime.

---

## XD-01 — QUYỀN SKIP: mệnh lệnh trỏ vào một khả năng KHÔNG TỒN TẠI

**Phân loại: `PROVEN_DEFECT`**

### Các bên

| bên | mã thật |
|---|---|
| **A** · doctrine **cho phép** bỏ lượt | `gpt_analyzer.py:4342` *«thà 'SKIP' còn hơn chốt ép khi evidence yếu»* · `:5591` *«accept 'SKIP' nếu evidence yếu»* · `:5626` · `:5689` *«Nếu chỉ có 1 rule match → giữ SKIP hoặc strength ≤5»* |
| **B** · SYSTEM_PROMPT **ép** luôn ra số | `gpt_analyzer.py:409` *«Strength < 4: TÍN HIỆU YẾU — vẫn phải chốt 1 số»* |
| **C** · owner-lock | `gpt_analyzer.py:4784-4786` (V11022, owner chốt 07/08): *«luôn ra số, không bao giờ bỏ số, để owner tự quyết»* |
| **D** · schema + cổng kiểm **ép** có `main_number` | `:3267` `required=[main_number, secondary_number, main_reason, secondary_reason]` · `:1232-1233` `main_number` rỗng ⇒ ghi vào `missing`, tức **lỗi định dạng**, không phải một lựa chọn hợp lệ |
| **E** · hạ nguồn **không hề chặn số** | `_v11161_rank_gen.py:300-301` SKIP ⇒ hệ số **0,7** hoặc **0,4** · `_backfill_bundles.py:81-82` ⇒ `verdict_weight = 0,4` · `database.py:3173-3175` `get_win_rate` **bỏ** lọc verdict · `daily_evaluation.py:117-119` **bỏ** lọc `verdict='CHOT_HA'` |

### Đo được — và phải TÁCH HAI NGHĨA (`RM-09`)

`predictions.verdict` mang **hai nghĩa khác hẳn nhau**, cấm gộp:

- **`MODEL_TU_KHAI_LLM`** — verdict = `verdict.decision` do model trả về
  (`main.py:7540` · `scheduler.py:4548/5945/7544`);
- **`CODE_TU_NGUONG`** — verdict do **mã** sinh từ ngưỡng `strength`
  (`meta_predict.py:302` · `lstm_predict.py:376` · `scheduler.py:3043/3368/3722`),
  **không phải** model bỏ lượt.

| nhóm | tổng SKIP | vẫn ra số | 0 số | 1 số | 2 số |
|---|---|---|---|---|---|
| `MODEL_TU_KHAI_LLM` | **283** | **272 (96,1%)** | 11 | 21 | 251 |
| `CODE_TU_NGUONG` | **187** | **187 (100%)** | 0 | 0 | 187 |

Toàn cửa sổ: chỉ **34/2.407 (1,41%)** lượt ra 0 số — và **17** trong số đó mang verdict `ERROR`,
tức lỗi truyền tải, không phải kiêng nhượng.

### Kết

> **`SKIP` không phải một quyền — nó là một NHÃN.**
> Model được bảo có thể bỏ lượt, nhưng schema bắt nó phải ra số, cổng kiểm coi việc không ra số
> là **lỗi định dạng**, và hạ nguồn chỉ hạ trọng số 0,4–0,7 rồi hai bộ tính WR **bỏ qua hẳn**
> verdict. Đây **cùng họ với `L6`** (tool calling): prompt bảo model làm một việc mà đường chạy
> thực tế không có.

**Mã vi phạm:** `PRJ_PROMPT_DANGLING` · `PRJ_PROMPT_CONTRADICTS`

---

## XD-02 — OWNER-LOCK V11150 «N≥1 không được thành NO_OUTPUT» vs UCC TỰ SUY `NO_OUTPUT` ở tầng NGUỒN

**Phân loại: `PROVEN_DEFECT`** · **Trạng thái thi hành: TIỀM ẨN** (UCC chưa lên VPS)

### Các bên — cả ba đọc bản LOCAL

| bên | mã thật |
|---|---|
| **A** · luật owner ở tầng **NGÀY** | `_v11150_unified_candidate_contract.py:363-386` `validate_batch`: ≥1 VALID + có bộ hỏng ⇒ `DEGRADED`; **chỉ** 0 VALID mới ⇒ `NO_OUTPUT` |
| **B** · UCC **tự suy** ở tầng **NGUỒN** | `:165-167` `build()`: `ranked_candidates` rỗng ⇒ `output_status = "NO_OUTPUT"` |
| **C** · adapter **khẳng định hành vi đó là đúng** | `_v11156_ranked_adapter.py` tự kiểm: *«nguồn không trả số ⇒ NO_OUTPUT, vẫn hợp lệ»* |

### Xung đột

Hai **TẦNG** bị gọi cùng một tên. Luật owner nói về **NGÀY × MIỀN**; phép tự suy nói về **MỘT
NGUỒN**. Văn bản hợp đồng **không chỗ nào tách hai tầng này**.

Hậu quả cụ thể: nếu một ngày chỉ còn **một** nguồn và nguồn đó kiêng nhượng, `build()` cho nó
`NO_OUTPUT`, rồi `validate_batch` thấy **0 bộ VALID** và trả `NO_OUTPUT` cho **cả ngày** — đúng
điều owner cấm.

Với số liệu thật thì tình huống này **hiếm** (34/2.407 lượt ra 0 số trong 30 ngày), **nhưng nó
chưa bao giờ bị chặn bằng luật** — nó chỉ chưa xảy ra.

**Mã vi phạm:** `A60_VIOLATION_LAYER_CONFLATED`

---

## XD-03 — UCC RANKED TOP-K vs TRẦN 2 SỐ · và `CAP5_INPUT_NOT_READY` là ÂM TÍNH GIẢ của bộ đọc

**Phân loại: `PROVEN_DEFECT`**

### Các bên

| bên | mã thật |
|---|---|
| **A** · hợp đồng **đòi** danh sách xếp hạng | `_v11150_unified_candidate_contract.py` (đoạn đầu, mục 3): `ranked_candidates` có `rank` + `raw_score` để `CAP5` (top-K) *«không còn là một phép cắt ngoài hợp đồng»* (LOCAL) · `_v11156_ranked_adapter.py:123-140` ánh xạ thứ tự `main_numbers` → `rank`, `raw_score=None` (LOCAL) |
| **B** · sản xuất **chặn cứng ở 2** | `gpt_analyzer.py:6829` `return nums[:2]` · `:412` *«Tối đa 2 số (main + secondary). KHÔNG BAO GIỜ đưa 3 số.»* |
| **C** · lane CAP5 **tự khai thiếu input** | `_v11137_d30_lane.py:29` *«14/16 model chưa persist top-5»* · `:227-244` `_top5_tu_analysis` đọc **cột `analysis_text`** và 9 tên khoá: `rf_numbers` `xgboost_numbers` `lstm_numbers` `meta_numbers` `all_numbers` `top_numbers` `candidates` `ranked` `top5` |

### Đo được

- `predictions.main_numbers` độ dài trong **cả** cửa sổ: `{0: 34, 1: 77, 2: 2296}` —
  **chưa bao giờ vượt 2**. Trần top-K thực tế = **2**.
- `near_miss_shortlist` **có thật** trong `reasoning_json`: **1.371** dòng khác rỗng,
  **3.774** phần tử, dạng `dict{number, reason_not_main}`.
- Hợp nhất `main_numbers ∪ near_miss` đạt **đúng 5 số ở 610 dòng**, **4 số ở 645 dòng**,
  3 số ở 98 dòng.
- `analysis_text` là JSON dict ở **2.407/2.407** dòng — nhưng trong đó, 9 khoá CAP5 tìm chỉ thấy
  `lstm_numbers` `meta_numbers` `rf_numbers` `xgboost_numbers`, **mỗi khoá đúng 90 dòng**; còn
  `near_miss_shortlist` xuất hiện trong `analysis_text` đúng **3 lần**.

### Kết

> Dữ liệu hạng 3–5 **đã tồn tại suốt**. Bộ đọc CAP5 tra **nhầm cột** (`analysis_text` thay vì
> `reasoning_json`) và dùng một danh sách 9 tên khoá **không có** `near_miss_shortlist`.
> `CAP5_INPUT_NOT_READY` là **âm tính giả của bộ đọc**, không phải thiếu dữ liệu.
> Đây là `RM-10` (kết luận theo tên đoán) và `RM-20` (không quét **điểm đọc**) trong **cùng một
> lỗi** — cùng họ với việc gọi `mt_model_hit_output_drop_shadow` là bảng chết.

### Cảnh báo — chưa được dùng ngay

`near_miss_shortlist` **không phải** danh sách xếp hạng chặt. Chính prompt định nghĩa nó ở
`gpt_analyzer.py:786` là *«1–3 số khác có evidence mạnh nhưng KHÔNG được chọn làm main»* — tức là
**một tập bị loại**, **không** phải **hạng 3–5**. Đo khớp với định nghĩa đó: **33,8%** dòng có
phần tử **trùng với `main_numbers`** (thường là chính số phụ).

Phải định nghĩa **grain** và phép **dedupe + gán rank** trước khi dùng làm input CAP5 — nếu không
sẽ đếm một số hai lần, đúng lỗi `consensus_level` ở `L10` (268/567 bundle mang nhãn cao hơn sự
thật). **Đây là lý do `XD-03` được hoà giải nhưng CHƯA được thi hành.**

**Mã vi phạm:** `RM-10` · `RM-20`

---

## XD-04 — `verdict.decision` là TỪ VỰNG MỞ, nhưng bộ hiển thị coi MỌI giá trị ≠ `CHOT_HA` là SKIP

**Phân loại: `PROVEN_DEFECT`** *(phát hiện trong lúc lập sổ, không nằm trong ba xung đột gate nêu)*

### Các bên

| bên | mã thật |
|---|---|
| **A** · prompt chỉ bao giờ cho model thấy **MỘT** giá trị | `gpt_analyzer.py:475` ví dụ JSON: `"decision": "CHOT_HA"` — không liệt kê giá trị nào khác, không có enum |
| **B** · bộ hiển thị **nhị phân hoá** | `gpt_analyzer.py:7241-7251` `if decision == 'CHOT_HA': … else: "⏭️ SKIP - BỎ QUA HÔM NAY"` · `main.py:7529+7544` và `main.py:8881+8898` đưa `display_text` vào **thân trả lời API** |

### Đo được

- **37** giá trị `verdict` phân biệt trong 30 ngày;
- **862/2.407 = 35,81%** không phải `CHOT_HA`;
- trong đó **828 lượt VẪN CÓ SỐ**.

Ví dụ giá trị bị gộp: `CHON_CAN_THAN` (157) · `GOI_Y_THAM_KHAO` (45) · `CHOT` (42) ·
`DU_DOAN_THAM_KHAO` (34) · `CHOT_HA_THAM_KHAO` (21) · `DE_XUAT` (12).

### Kết

`CHON_CAN_THAN` — một kết luận **có số**, nghĩa là *«chọn cẩn thận»* — bị in ra y hệt
`SKIP – BỎ QUA HÔM NAY`. Trường tự do gặp một phép so bằng đúng một hằng ⇒ 35,81% lượt bị dán
nhãn ngược nghĩa.

**Giới hạn:** mục này chứng minh đến **tận thân trả lời API** (`display_text`). Việc giao diện có
render `display_text` hay không **chưa kiểm trong gate này** ⇒ chặng cuối ghi **`INDETERMINATE`**.

**Mã vi phạm:** `PRJ_PROMPT_CONTRADICTS`

---

## XD-05 — `secondary_number` bị BA luật khác nhau điều khiển trong CÙNG một prompt

**Phân loại: `PROVEN_DEFECT`** *(phát hiện trong lúc lập sổ)*

### Các bên

| bên | mã thật |
|---|---|
| **A** · §5d **ép** secondary theo một **BỘ SỐ đã xếp hạng** | `gpt_analyzer.py:349-350` *«Nếu có → secondary_number NÊN là số đi cùng»* — nguồn là khối `CẶP ĐÔI HAY ĐI CÙNG` (`P15`), đã xếp hạng, có `frequency:` |
| **B** · §6 và §24 **đòi** secondary **ĐỘC LẬP** | `:414` *«Số secondary chỉ được giữ khi có evidence ĐỘC LẬP (khác source, khác family)»* · `:776` *«Số phụ chỉ giữ khi evidence ĐỘC LẬP cực mạnh»* |
| **C** · PHASE-FIRST **cấm** secondary là biến thể của main | `:5916-5918` *«OUTPUT KHÔNG HỢP LỆ NẾU secondary_number là BIẾN THỂ của main_number»* · `:4798-4800` lặp lại lệnh cấm đó lần hai |

### Đo được

**123/2.296 = 5,36%** lượt hai số có **số phụ là biến thể của số chính** (đảo `XY→YX` hoặc ±1 một
chữ số) — **dù lệnh cấm được lặp hai chỗ trong cùng prompt**.

### Cùng một trường, BA TÊN khác nhau trong cùng một prompt

| chỗ | tên dùng |
|---|---|
| `OUTPUT FORMAT (JSON)` `:458-459` | `prediction.main_number` · `prediction.secondary_number` |
| §24 BẠCH THỦ NORTH STAR `:770` `:773` | `numbers[0]` · `numbers[1]` |
| §25 MAIN-NUMBER OUTPUT CONTRACT `:789` | `main_numbers[1]` |

Đây **không** chỉ là chuyện chữ nghĩa: bộ trích số `gpt_analyzer.py:7020` đọc **Priority 1** là
các khoá **danh sách** `so_du_doan` · `predictions` · `numbers` · `main_numbers` **trước**, chỉ khi
không có mới xuống `prediction.main_number` (Priority 2, `:7025-7036`). Một model làm đúng theo §24
sẽ trả `numbers: [...]` và đi **nhánh khác** với model làm đúng theo `OUTPUT FORMAT`.

### Kết

Một trường, ba chủ **và ba tên**: một luật **đẩy** nó theo bộ số tổng hợp, hai luật **đòi** nó độc
lập, một luật **cấm** nó là biến thể. Model chọn câu nào là ngẫu nhiên ⇒ phép đo trên trường này
mất nghĩa.

**Mã vi phạm:** `PRJ_PROMPT_CONTRADICTS` · `A58_VIOLATION_HALF_DONE`

---

## BA PHƯƠNG ÁN — và cái giá của từng cái

### PA-1 — Giữ `SKIP` như quyền THẬT, cho phép ra 0 số

| | |
|---|---|
| **được** | model kiêng nhượng được thật; dữ liệu đo sạch hơn (bỏ các lượt evidence rỗng) |
| **giá** | **trái thẳng** owner-lock V11016/V11022 (`gpt_analyzer.py:4784-4786`) · trái quy tắc sản phẩm *«luôn ra số, owner tự quyết»* · đo 07/08 (V11022): nhóm **BỎ** số phụ trúng **0/4** vs nhóm **GIỮ** **5/12** — đóng một cửa trúng **THẬT** · phải sửa UCC/adapter vì `NO_OUTPUT` tầng nguồn sẽ lan lên tầng ngày |
| **kết** | **TỪ CHỐI** — owner đã khoá, và đã từng thử rồi gỡ sau đúng một chu kỳ live |

### PA-2 — Gỡ hẳn mọi câu `SKIP` khỏi prompt, không thay bằng gì

| | |
|---|---|
| **được** | hết mâu thuẫn; prompt ngắn hơn |
| **giá** | mất kênh cho model **nói ra** rằng bằng chứng mỏng · MB (1 đài/ngày, bằng chứng mỏng hơn MN/MT 3–4×) mất cách hạ tin cậy có kỷ luật · **vẫn còn** `XD-04` và `XD-05` |
| **kết** | **KHÔNG ĐỦ** — chưa bàn đến trường nào thay thế |

### PA-3 — TÁCH **kiêng nhượng** khỏi **chặn số** ✅ **CHỌN**

| | |
|---|---|
| **được** | giữ owner-lock: `main_number` **vẫn bắt buộc**, không bao giờ rỗng · model có kênh **thật** để khai bằng chứng mỏng (`evidence_sufficiency`) · gỡ được mệnh lệnh trỏ vào khả năng không tồn tại (`XD-01`) · từ vựng **ĐÓNG** cho verdict ⇒ `XD-04` tự hết · hạ nguồn đọc **một trường có nghĩa** thay vì đoán từ 37 giá trị tự do |
| **giá** | phải sửa **4 điểm bơm độc lập trong CÙNG một phiên** (`§60.2`), cấm sửa lẻ · phải sửa bộ hiển thị `gpt_analyzer.py:7241-7251` **cùng lúc**, nếu không sẽ in sai nhãn mới · mọi số liệu WR/BT cũ tính theo `verdict` sẽ **đổi nghĩa** ⇒ phải **RÚT LẠI ở chỗ gốc** (`PRJ-RETRACTION-001`) nếu có báo cáo nào đã dùng `verdict` làm bộ lọc · **chưa đo được** hiệu ứng dự đoán — chỉ được nói là sửa **NGHĨA**, **cấm hứa hit rate** |

---

## CONTRACT ĐỀ XUẤT — `PURE-CONTEXT-OUTPUT-1.0.0-DRAFT`

> **Trạng thái: ĐỀ XUẤT.** Chưa owner khoá · chưa deploy · chưa chạy lượt nào.
> Đặc tả đầy đủ ở `PURE_CONTEXT_THREE_LAYER_SPEC.md` §4.2 và
> `artifacts/v11165_k6_three_layer.json` khoá `tang_3_REASONING_OUTPUT`.

| trường | luật | giải quyết xung đột nào |
|---|---|---|
| `main_number` | **bắt buộc**, cấm rỗng | `XD-01` (giữ owner-lock) |
| `secondary_number` | có mặt bắt buộc, `""` hợp lệ; **một** điều kiện: `condition_refs` không giao với main ở mức `nhóm_độc_lập`; cấm là biến thể của main | `XD-05` |
| `ranked_candidates` | rank 1 = main · rank 2 = secondary · **rank 3–5 = `near_miss_shortlist`**; công bố **chỉ** rank 1–2 | `XD-03` |
| `condition_refs` | bắt buộc | truy ngược lập luận |
| `evidence_summary` | bắt buộc; cấm nhắc model khác | mục tiêu owner #5 |
| `confidence_class` | ĐÓNG `THIN·MODERATE·STRONG`; **không phải xác suất** | `strength` đo được **không đơn điệu** |
| `evidence_sufficiency` | ĐÓNG `SUFFICIENT·THIN·INSUFFICIENT`; **không chặn số** | `XD-01` |
| `limitations` | bắt buộc | — |
| `output_status` | `OK·DEGRADED·NO_OUTPUT`; `NO_OUTPUT` **chỉ** cho lỗi truyền tải/parse | `XD-02` |

### Hoà giải từng điểm

| xung đột | cách hoà giải |
|---|---|
| **XD-01** | `main_number` **vẫn** bắt buộc. Thêm `evidence_sufficiency` làm kênh kiêng nhượng **không chặn số**. **GỠ** cả 4 câu SKIP ở `gpt_analyzer.py:4342` · `:5591` · `:5626` · `:5689` |
| **XD-02** | Viết **thẳng vào văn bản** UCC: `NO_OUTPUT` ở tầng **NGUỒN** chỉ được đặt khi lỗi truyền tải/parse; cấm đặt vì lựa chọn biên tập. Luật `N≥1` là luật tầng **NGÀY × MIỀN**, do `validate_batch` giữ. Vì UCC chưa lên VPS, sửa này ở trạng thái `CODED`, **chưa runtime** |
| **XD-03** | Công bố **giữ trần 2 số** (không đổi gì ở đầu ra người dùng). `ranked_candidates` rank 3–5 lấy từ `near_miss_shortlist`. Sửa bộ đọc CAP5: đọc **cột `reasoning_json`** và thêm khoá `near_miss_shortlist`, kèm phép dedupe với `main_numbers` rồi gán rank. **Trước khi dùng phải định nghĩa grain**: `near_miss` là *«số có evidence mạnh nhưng không được chọn làm main»*, **không phải** *«hạng 3»* |
| **XD-04** | **Đóng** từ vựng verdict. Bộ hiển thị **không được suy** `SKIP` từ phép phủ định; phải đọc `evidence_sufficiency`. Sửa `gpt_analyzer.py:7241-7251` **trong cùng phiên** với sửa prompt |
| **XD-05** | **MỘT** luật duy nhất cho secondary. **XOÁ §5d** (`gpt_analyzer.py:349-350`) vì đó là một **BỘ SỐ tổng hợp đẩy thẳng vào trường đầu ra** — đúng điều mục tiêu owner #3 cấm |

---

## CHƯA TRẢ LỜI ĐƯỢC

| câu hỏi | trạng thái | chặn ở đâu |
|---|---|---|
| Giao diện có render `display_text` không? | **`INDETERMINATE`** | ảnh hưởng phạm vi `XD-04`; chưa kiểm tầng frontend |
| `near_miss_shortlist` có phải hạng 3–5 **thật** không, hay chỉ là *«số bị loại»*? | **grain chưa định nghĩa** | chặn thi hành `XD-03` |
| Hiệu ứng dự đoán của contract đề xuất | **CHƯA ĐO** | mục tiêu owner #9 cấm hứa hit rate từ thiết kế prompt |

---

## Ba lớp nguồn (§62)

| lớp | nội dung |
|---|---|
| **`OWNER_SAID`** | `OWNER LOCK` 23:14 04/09 (`QD-073`): `OUTPUT_COUNTERFACTUAL_RANK_PRODUCTION_WRITE = FORBIDDEN` · `MODEL_ACTION = BLOCKED` · `CURRENT_FROZEN_ARTIFACT_ROLE = AUDIT_EVIDENCE_ONLY`. Chín mục tiêu «thuần ngữ cảnh», đặc biệt #3 (không đưa rổ số đã chọn sẵn), #5 (không dùng tên model/WR/trọng số), #6 (không bảo model tự truy vấn nếu không có tool), #8 (`CONDITION` là bằng chứng, không phải khuyến nghị), #9 (chỉ đo tiến mới tính). |
| **`CODE_DID`** | Mọi con số đo trên clone bất biến `mode=ro`, cửa sổ `2026-08-06..2026-09-04`, ghi ở `artifacts/v11165_k6_bangchung.json`. Mã production đọc: `gpt_analyzer.py` sha16 `758c29c13185763f`. Lệnh tái lập: `python _chay.py _k6_bangchung.py`. |
| **`DOC_SAID`** | `_v11137_d30_lane.py:29` ghi *«14/16 model chưa persist top-5»* — **lệch với `CODE_DID`** (`XD-03`). `gpt_analyzer.py:782` nói với model rằng các trường §25 *«được parser bỏ qua nếu thiếu, nhưng nên có»*, trong khi `:1225-1235` **thật sự kiểm** `main_number_justification` · `near_miss_shortlist` · `secondary_pick_rationale` và ghi vào `missing` — **lệch** giữa lời mô tả trong prompt và cổng kiểm thật. |

**Lệch đã báo, không im lặng chọn một lớp:** `DOC_SAID ≠ CODE_DID` ở **hai** chỗ trên.

---

TanPhatAI cần làm: mở **hai** mục treo trong `docs/FOLLOW_UP_TRACKER.md` — (a) `XD-03` chặn bởi
grain `near_miss_shortlist` chưa định nghĩa, (b) `XD-04` chặn bởi chưa kiểm frontend có render
`display_text`; và ghi nhận rằng năm xung đột trong sổ này **chưa có mã sửa nào** — mọi tham chiếu
phải giữ tầng `LEDGER_ONLY`, cấm nâng lên `CODED` hay `DEPLOYED`.
