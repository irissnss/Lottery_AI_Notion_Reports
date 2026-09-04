# PURE CONTEXT — ĐẶC TẢ BA TẦNG

**V11165 · Làn sóng 2 · Gate 6 · 2026-09-05 ICT**

| | |
|---|---|
| **Tầng verdict** | `CODED_AND_TESTED_NOT_RUNTIME_PROVEN` **CHƯA ĐẠT** — đây là **ĐẶC TẢ**, chưa có mã, chưa chạy lượt nào |
| **Nguồn đo** | `artifacts/v11165_h4_set_to_condition.json` (Gate 4, làn sóng 1 — 35 producer, dump từ hàm đang serve) · `artifacts/v11165_k6_bangchung.json` (số đo của chính gate này) |
| **Neo runtime** | `gpt_analyzer.py` sha16 `758c29c13185763f` · PID 3370750 · NRestarts 0 |
| **Clone đo** | `/root/Lottery_AI_Test/artifacts/v11165_immutable.db` mở `mode=ro` |
| **Artifact máy đọc** | `artifacts/v11165_k6_three_layer.json` (41.334 B · sha16 `1f3efe32a03ae1ad`) |
| **Cấm** | deploy · restart · sửa tệp đang serve · ghi DB · gọi provider LLM |

---

## 0. Vì sao cần đặc tả này — ba việc làn sóng 1 đã chứng minh

Không lặp lại phép đo. Ba kết quả dưới đây là **tiền đề**, đã đóng ở làn sóng 1:

1. **«Thuần ngữ cảnh» hiện tại chưa đạt.** Cờ `context_only` chỉ gác **6/171 = 3,51%** điểm bơm
   chuỗi; `build_context_pack` (141 điểm) gác **0**. Lane `CONTEXT_ONLY_V2` gỡ 3 khối trong ~30
   và **thêm 4 khối**. 33/33 lượt shadow vẫn nhận rổ số đã chọn sẵn.
2. **Không có tool calling ở bất kỳ model nào** (grep 5 mẫu trên toàn `web/backend` = 0 dòng).
   Mọi mệnh lệnh bảo model «tự truy vấn» là **không thi hành được**.
3. **35 producer**: 27 bơm `AGGREGATED_NUMBER_SET`, 2 `RAW_NUMBER_FACT`, **chỉ 1/35 có nền
   tường minh**. 83/100 đuôi được bơm vào MN official dưới 23 nhãn khác nhau — nghĩa là **bất kỳ
   số nào model chọn cũng biện minh được**.

Đặc tả này là câu trả lời cho **chín mục tiêu owner** về «thuần ngữ cảnh», không phải một bản
dọn dẹp prompt.

---

## 1. Định nghĩa đóng — dùng nguyên văn, không diễn giải lại

| thuật ngữ | nghĩa |
|---|---|
| **`RAW_NUMBER_FACT`** | số trong kết quả lịch sử / sự kiện nguồn thật, **kèm** ngày · miền · đài · giải · bộ · cutoff |
| **`AGGREGATED_NUMBER_SET`** | danh sách ứng viên đã union / lọc / xếp hạng / boost / chia `FRESH`–`FULL_SPENT` / cắt top-k |
| **`CONDITION`** | mệnh đề có phạm vi · đầu vào · phép biến đổi · cutoff · nền · cỡ mẫu · độ bất định · trạng thái bằng chứng. **`CONDITION` KHÔNG PHẢI `RECOMMENDATION`** |
| **`PURE CONTEXT`** | `raw facts` + `neutral conditions` + `reasoning/output contract` |

---

## 2. TẦNG 1 — FACTS

### Được chứa

- quan sát lịch sử **thô** (kết quả từng đài × từng giải × từng ngày);
- **lịch đài xổ hôm nay**;
- định danh **miền / thứ / bộ giải**;
- thông tin **cùng ngày hợp lệ tại cutoff** (miền xổ trước — MB được dùng MN(D)/MT(D));
- **bảng đếm TOÀN VŨ TRỤ** `00–99` render đối xứng.

### Cấm tuyệt đối

mệnh lệnh · xếp hạng · danh sách ứng viên rút gọn · điểm/boost · nhãn cảm tính
(`HOT` · `GAN` · `OVERDUE` · `sắp về`) · cắt top-k.

### Quy tắc render — chỗ dễ lách nhất

> Bảng đếm phải phủ **đủ** vũ trụ mục tiêu (`00–99`, hoặc toàn bộ đài/giải), và **sắp theo thứ tự
> tự nhiên của khoá**, không theo điểm.
> **Sắp theo điểm chính là xếp hạng** — đổi hình thức mà giữ bản chất, đúng lỗi `P25` đã mắc:
> tiêu đề tự khai *«KHÔNG có danh sách số chốt sẵn»* nhưng mọi câu vẫn liệt kê đuôi tường minh và
> thứ tự vẫn theo xếp hạng.

**6 producer thuộc tầng này:** `P01` `P09` `P14` `P16` `P17` `P29`.

`P29_D1_POOL_COUNT` là khuôn mẫu **đúng** đã có sẵn trong kho — `D-1 cross-region tail pool: 76
distinct tails`: ghi **số đếm**, không ghi danh sách thiên lệch. `P29` mang disposition
`EXPOSE_VIA_REAL_QUERY_TOOL`, nhưng vì tiền đề (2) đo được **0 tool**, nó vào Tầng 1 dưới dạng
**số đếm thuần**, và **cấm** mọi câu bảo model «tự truy vấn».

---

## 3. TẦNG 2 — CONDITIONS + EVIDENCE

### 🔴 Khuôn `CONDITION` KHÔNG định nghĩa ở đây — dùng bản của Gate 5

> **Đính chính trong cùng phiên.** Bản nháp đầu của mục này tự dựng một khuôn `CONDITION` **12
> trường**. Đó là **sai** — Gate 5 cùng làn sóng đã chốt `CONDITION_CONTRACT` với **24 trường bắt
> buộc** và **17 điều kiện cụ thể**, đo nền thật trên clone bất biến. Dựng khuôn thứ hai là **tạo
> chồng tầng mới**, đúng lỗi `§60` cấm. Khuôn 12 trường **đã rút**, không dùng.

**Nguồn duy nhất cho hình dạng bản ghi Tầng 2:** `CONDITION_CONTRACT.md` (V11165 · Gate 5) —
24 trường, `condition_family ∈ {RAW · UNIVERSE · STAT · RULE · SPEND · TOOL · SHADOW}`,
`candidate_binding_mode ∈ {FULL_UNIVERSE_SYMMETRIC · RAW_EVENT_NARRATIVE · RULE_PROPOSITION ·
REAL_QUERY_TOOL · CANDIDATE_NEGATIVE · SHADOW_ONLY}`.

Gate 6 **không thêm trường nào**. Nó chỉ thêm **hai** ràng buộc dùng lại từ vựng của Gate 5:

1. **`evidence_status` quyết định điều kiện đó được dùng để làm gì** (xem §4.1);
2. mỗi condition phải báo **cả TRONG và NGOÀI cửa sổ chọn** — Gate 5 đã đặt việc này ở trường
   `effect_size`. `RM-18` đo được luật hơn nền **+7,5 / +13,8 / +20,7 điểm** *trong* cửa sổ chọn
   và **đúng bằng 0** ngoài cửa sổ; báo một con số gộp là giấu mất nửa sự thật.

### Hệ quả nặng nhất của việc dùng từ vựng Gate 5

Kiểm kê Gate 5 trên 17 điều kiện: `RAW_FACT` **2** · `MECHANICALLY_DERIVED` **3** ·
`HYPOTHESIS_ONLY` **5** · `RETROSPECTIVE_ONLY` **6** · `UNAVAILABLE` **1** ·
**`PROSPECTIVE_SUPPORTED` = 0**.

> **Không một điều kiện nào đạt `PROSPECTIVE_SUPPORTED`.**
> Ghép với luật Tầng 3 (§4.1), điều đó có nghĩa: dưới hợp đồng đề xuất, model **chỉ được rút số**
> từ **5/17** điều kiện (`RAW_FACT` + `MECHANICALLY_DERIVED`). Mười hai điều kiện còn lại được
> phép **xuất hiện như dữ kiện**, nhưng **cấm dùng làm căn cứ ưu tiên số**.
> Đây là **kết quả**, không phải thiếu sót của bản kiểm kê.

### Cấm trong Tầng 2

| cấm | vì sao |
|---|---|
| động từ ra lệnh: `ưu tiên` `nên` `tránh` `loại` `boost` `prefer` `avoid` | `CONDITION` là **bằng chứng để model cân nhắc**, không phải khuyến nghị số (mục tiêu owner #8) |
| điểm tổng hợp: `score=` `weight=` `pt` `lift` dùng như điểm thưởng | đó là `AGGREGATED_NUMBER_SET` trá hình |
| cắt top-k trên không gian ứng viên | mục tiêu owner #3 |
| nhãn cảm tính `HOT` `GAN` `OVERDUE` `sắp về` | owner 06/08 nguyên văn: *«cái anh không thích nhất là gan, cold, hot nó chả tích sự gì»* |
| tên model · win rate · xếp hạng model | mục tiêu owner #1 và #5 |
| số liệu **không** kèm `n` và **nền** | Gate 4 đo: **33/35** producer không có nền trong prompt |

**10 producer thuộc tầng này:** `P04` `P15` `P21` `P23` `P24` `P25` `P26` `P28` `P30` `P34`.

> ⚠️ **Cố ý trích MỘT cửa sổ** (`PRJ-SELECTION-WINDOW-001` · RM-18). Phiên này **không** tuyên bố
> hiệu quả của luật khai mỏ, nên cả bốn vế — **trong cửa sổ chọn · ngoài cửa sổ chọn · trong mẫu ·
> ngoài mẫu** — đều để trống có chủ ý. Bộ đủ nằm ở **RM-18/V11030** (**+7,5 / +13,8 / +20,7 điểm
> TRONG cửa sổ chọn, ĐÚNG BẰNG 0 ngoài cửa sổ**) và **V11073** (**+9,9% trong mẫu → −1,6% ngoài
> mẫu**). Đo bổ sung của phiên này: **n = 20/miền trên 4 ngày** ⇒ **RM-04, chưa được phép kết
> luận**; KTC95 đều chứa 0. Báo một vế là giấu mất nửa sự thật.
`P21_MINED_RULES` là khuôn mẫu **đúng** duy nhất đang có: cột `lợi thế/nền` (V11094) hiện mức
**hơn nền** trên 365 ngày, kèm đoạn «cách đọc» **tự phủ định**. Đó là hình dạng mà 9 producer còn
lại phải được dịch sang.

---

## 4. TẦNG 3 — REASONING + OUTPUT CONTRACT

### 4.1 Luật lập luận

- tự đối chiếu **nhiều** condition; nêu rõ `condition_id` **đã dùng** *và* **đã bỏ**;
- phân biệt **FACT** (Tầng 1) với **HYPOTHESIS** (suy diễn của model);
- **không bịa** dữ liệu thiếu — thiếu thì ghi thiếu;
- **không** tham chiếu model khác, tên model, win rate, xếp hạng model;
- **luật `evidence_status`** — dùng từ vựng đóng của Gate 5, không đặt nhãn mới:

  | `evidence_status` | được dùng để |
  |---|---|
  | `RAW_FACT` · `MECHANICALLY_DERIVED` | **rút số** |
  | `HYPOTHESIS_ONLY` · `RETROSPECTIVE_ONLY` | chỉ **kể như dữ kiện**; **cấm** làm căn cứ ưu tiên số |
  | `UNAVAILABLE` | **cấm** vào prompt tĩnh (cần tool thật, mà làn sóng 1 đo được **0** model bật tool) |
  | `PROSPECTIVE_PENDING` · `PROSPECTIVE_SUPPORTED` · `REJECTED` | hiện **0** điều kiện mang các nhãn này |

- output đúng schema, không thêm chữ ngoài JSON.

### 4.2 OUTPUT CONTRACT — `PURE-CONTEXT-OUTPUT-1.0.0-DRAFT`

> **Trạng thái: ĐỀ XUẤT.** Chưa owner khoá · chưa deploy · chưa chạy lượt nào.
> Hợp đồng này **hoà giải** ba thứ đang mâu thuẫn nhau — lý do và cái giá của từng lựa chọn nằm
> ở `CONTRACT_CONFLICT_LEDGER.md`, **không** được đọc riêng tệp này rồi thi hành.

| trường | luật |
|---|---|
| `main_number` | **BẮT BUỘC**, string 2 chữ số, **cấm rỗng**. Giữ owner-lock V11016/V11022: *«luôn ra số, không bao giờ bỏ số, để owner tự quyết»* |
| `secondary_number` | khoá **bắt buộc có mặt**; giá trị `""` hợp lệ (kèm `secondary_reason="NO_SECONDARY"`). **MỘT** điều kiện duy nhất: chỉ được có khi `condition_refs` của nó **không giao** với `condition_refs` của main ở mức `nhóm_độc_lập`. **Cấm** là biến thể của main |
| `ranked_candidates` | `[{rank, candidate, condition_refs, reason_not_main}]` · rank 1 = main · rank 2 = secondary · **rank 3–5 = `near_miss_shortlist`** (đã tồn tại trong `reasoning_json`). `raw_score = None` khi nguồn không có điểm thật — **cấm bịa điểm**. **Chỉ rank 1–2 được công bố**: trần 2 số **giữ nguyên** |
| `condition_refs` | **bắt buộc** — không nêu `condition_id` đã dùng thì không truy ngược được lập luận |
| `evidence_summary` | **bắt buộc**; cấm tham chiếu model khác |
| `confidence_class` | từ vựng **ĐÓNG** `THIN · MODERATE · STRONG`. **KHÔNG phải xác suất** |
| `evidence_sufficiency` | từ vựng **ĐÓNG** `SUFFICIENT · THIN · INSUFFICIENT`. **KHÔNG chặn số** — đây là kênh kiêng nhượng thật, thay cho `SKIP` |
| `limitations` | **bắt buộc**, list |
| `output_status` | `OK · DEGRADED · NO_OUTPUT`. `NO_OUTPUT` **chỉ** cho lỗi truyền tải / lỗi parse / model không trả lời. **CẤM** dùng như một lựa chọn biên tập |

#### Vì sao `confidence_class` không được là xác suất — đo được, không phải ý kiến

`hit-any` (WIN|PARTIAL) theo dải `strength`, 90 ngày `2026-06-07 → 2026-09-04`, lane official:

| dải strength | n | hit-any | KTC95 |
|---|---|---|---|
| A `<3` | 130 | **54,6%** | ±8,6 pp |
| B `3–3,9` | 479 | 56,4% | ±4,4 pp |
| C `4–4,9` | 806 | 53,5% | ±3,4 pp |
| D `5–5,9` | 954 | **57,5%** | ±3,1 pp |
| E `6–6,9` | 1.036 | **47,9%** | ±3,0 pp |
| F `≥7` | 718 | 61,6% | ±3,6 pp |

Dải **E (6–6,9) = 47,9%** thấp hơn cả dải **A (<3) = 54,6%** và **D = 57,5%**, khoảng tin cậy
không chồng. **`strength` không đơn điệu theo kết quả** ⇒ cấm trình bày như xác suất.

> **Giới hạn của chính phép đo này — đọc trước khi trích lại bảng trên:**
> đây là `hit-any` trên bộ **k = 2** số theo cột `status`, **gộp cả ba miền**, và **KHÔNG kèm
> nền**. Nền đúng cho bộ k phải là `1−(1−b)^k` (`RM-18`), với `b` đo **riêng cho từng miền**.
> ⚠️ **Cố ý trích MỘT cửa sổ** (`PRJ-SELECTION-WINDOW-001` · RM-18 · RM-21). Phiên này đo **NỀN**
> cho thước bạch thủ, **không** tuyên bố hiệu quả, nên **14 / 30 / 90 / 180 ngày** đều để trống có
> chủ ý. Bộ đủ bốn cửa sổ nằm ở **V11084 + V11086**, và ở đó **dấu ĐỔI**: 30 ngày **+4,07pp** ·
> 90 ngày **−3,18pp** · 180 ngày **+0,91pp** (CI95 [−3,2 ; +5,0]). Trích riêng một cửa sổ để
> tuyên bố hiệu quả là chọn cửa sổ cho khớp kết quả — bản này **không** làm thế.
> Gate 5 đã đo `b` thật (`T1` bạch thủ, W180 kết thúc 04/09): **MN 0,4298 · MT 0,3509 ·
> MB 0,2374** — ba giá trị **rất khác nhau**, nên một con số gộp ba miền **không so được** với
> bất kỳ nền nào.
>
> ⇒ Bảng trên **chỉ** kết luận về **tính đơn điệu** của `strength`. Nó **không** nói `54,6%` là
> tốt hay xấu, và **cấm** dùng nó làm bằng chứng hiệu năng. Phép so với nền phải làm **tách
> miền** và **khớp định nghĩa** (`status=WIN|PARTIAL` chưa chắc đồng nghĩa `đuôi có mặt` của
> thước `T1`) — **chưa làm trong gate này**, đã ghi ở §9.

### 4.3 Bất biến đo lường — không được vi phạm khi so control ↔ candidate

- vai trò `system`/`user` **giữ nhất quán** giữa control và candidate;
- **không** đổi đồng thời model / provider / temperature / token cap / data cutoff / output schema;
- mọi thay đổi prompt phải **DUMP từ hàm đang serve** rồi quét đủ 4 mục
  `PRJ-PROMPT-COHERENCE-001` (`RM-14`).

---

## 5. Bảng gán tầng — cả 35 producer

Gán **suy từ `disposition` đã đo ở Gate 4**, không gán tay.

| tầng | số producer | producer |
|---|---|---|
| **TẦNG 1 — FACTS** | **6** | `P01` `P09` `P14` `P16` `P17` `P29` |
| **TẦNG 2 — CONDITIONS** | **10** | `P04` `P15` `P21` `P23` `P24` `P25` `P26` `P28` `P30` `P34` |
| **LOẠI** | **18** | `P02` `P03` `P05` `P06` `P07` `P08` `P10` `P11` `P12` `P13` `P18` `P19` `P20` `P22` `P27` `P31` `P32` `P35` |
| **NGOÀI HỢP ĐỒNG** | **1** | `P33` (giả thuyết, chỉ lane shadow) |

Lý do loại, theo nhóm:

| nhóm | producer | lý do |
|---|---|---|
| `DROP_UNSUPPORTED` (5) | `P02` `P03` `P08` `P11` `P12` | không nền, không n, không tái lập |
| `DROP_DUPLICATE` (4) | `P05` `P20` `P22` `P27` | trùng họ với khối khác — vi phạm độc lập nguồn |
| `DROP_MODEL_META` (6) | `P06` `P10` `P13` `P31` `P32` `P35` | meta của chính hệ (tên model · WR · trọng số) — mục tiêu owner #1 và #5 |
| `BLOCK_ORACLE` (1) | `P07` | đưa sẵn đáp án rồi ra lệnh ưu tiên đáp án đó — mục tiêu owner #3 |
| `BLOCK_AMBIGUOUS` (2) | `P18` `P19` | nguồn đông băng 131 ngày, nhãn nói sai về chính nó — phải sửa nguồn trước |

Bảng đầy đủ 35 dòng kèm `dòng_hiện_tại` · `điểm_bơm` · `mệnh_lệnh_mồ_côi` · `rủi_ro` nằm ở
`artifacts/v11165_k6_three_layer.json`, khoá `bang_gan_tang`.

---

## 6. Bốn điểm vào ĐỘC LẬP — sửa một chỗ KHÔNG sửa được ba chỗ kia

`§60.2` bắt buộc trả lời «ai còn trỏ tới thứ này» trước khi sửa. Với prompt, câu trả lời là **bốn
điểm, không phải một**:

| # | điểm | dòng | producer |
|---|---|---|---|
| 1 | `create_analysis_prompt` | `gpt_analyzer.py:2221-3212` | `P01..P20` `P31` `P32` |
| 2 | `build_context_pack` | `gpt_analyzer.py:4831-5937` | `P21..P30` `P34` `P35` |
| 3 | **BA MODULE NGOÀI** | `statistical_analyzer.py` · `metrics_calculator.py` · `feature_engineering.py` | — |
| 4 | `_build_lane_test_shadow_doctrine_addon` | `gpt_analyzer.py:6370-6533` | `P33` |

**Điểm 3 chính là chỗ V11001/V11007 bỏ sót** khi tuyên bố đã «gỡ gan/hot/cold»: `gan`/`hot` vẫn
được bơm mỗi lượt từ `statistical_analyzer.py:874-881` và `feature_engineering.py:301-314`.

---

## 7. Cảnh báo thi hành

1. **Cấm sửa lẻ.** Sửa một trong bốn điểm mà bỏ ba điểm kia = `A58_VIOLATION_HALF_DONE`, và phép
   đo tiếp theo sẽ chạy trên một thay đổi **làm nửa vời** ⇒ kết luận vô giá trị (`§60.1`).
2. **Phải vá THƯỚC trước.** Vân tay `runtime_prompt_sha256` chỉ phủ 39,81–48,07% (tb 43,59%); bộ
   5 dấu ô nhiễm `_dau_o_nhiem` (`gpt_analyzer.py:6712`) **mù cấu trúc** — báo 0/5 «sạch» trong
   khi payload thật còn `weight=` (33/33 lượt); cổng `_v11160_test_lane.py` **mù** với nửa
   `ctx_pack`. Đo bằng dụng cụ hỏng thì mọi kết luận vô hiệu.
3. **CẤM phục hồi T-B/V11059 một cách mù.** Bản T-B cũ **chưa sạch** — 5 chỗ vi phạm
   (`gpt_analyzer.py:2418-2424` · `:3191` · `RULEBOOK §8:565` · MB `:5591/:5689` ·
   Phase 15 `:2472-2526`) **vẫn có mặt trong CẢ HAI nhánh**. Dùng lại nguyên bản thì phép đo lại
   vô nghĩa. Phải đối chiếu candidate mới với `T1/T2/T3` cũ và **chỉ tái sử dụng phần còn đúng**.
4. **Rổ shadow vào official vẫn sống.** `gpt_analyzer.py:6738` còn
   `_shadow_mode = lane_test_shadow_pack or (selected_model in SHADOW_GATE_MODELS)` ⇒
   `gpt-oss-120b` (OFFICIAL) nhận gói ngữ cảnh SHADOW 88/88 lượt official trong 30 ngày. Phải vá
   trước khi lấy official làm control.

---

## 8. Thử chặn bắt buộc (`RM-15`) — cổng không qua thử coi như KHÔNG TỒN TẠI

| # | phép thử | kỳ vọng |
|---|---|---|
| T1 | dump prompt từ hàm đang serve, đếm chuỗi thuộc `AGGREGATED_NUMBER_SET` | **0** |
| T2 | dump prompt, đếm động từ ra lệnh trong danh sách cấm | **0** |
| T3 | một condition thiếu 1 trong 12 trường | **deny**, thoát ≠ 0 |
| T4 | trạng thái sạch | **allow**, thoát 0 |
| T5 | giả lập một producer `LOẠI` quay lại | **deny** |
| T6 | giả lập `secondary` là biến thể của `main` | **deny** |
| T7 | giả lập output thiếu `condition_refs` | **deny** |
| T8 | khôi phục nguyên trạng sau thử | bắt buộc |

Quét ngược sau khi sửa phải **PHÂN LOẠI** (`RM-09` · `§60.3`): `TRONG_PROMPT` và `GHI_VÀO_PROMPT`
**phải xử**; `CODE` xét từng cái; `CHÚ_THÍCH` **giữ**.

---

## 9. Đặc tả này CHƯA làm được gì

- **Chưa có mã.** Đây là đặc tả, không phải patch. Verdict trần
  `CODED_AND_TESTED_NOT_RUNTIME_PROVEN` **chưa đạt**.
- **Chưa đo được hiệu ứng dự đoán.** Mục tiêu owner #9: *output tốt hơn phải chứng minh bằng ĐO
  TIẾN*; cấm hứa hit rate từ thiết kế prompt.
- **Mục tiêu owner #6 chỉ thoả được bằng cách GỠ** mệnh lệnh «tự truy vấn» — thêm tool thật nằm
  ngoài phạm vi làn này.
- **Grain của `near_miss_shortlist` chưa định nghĩa** — xem `CONTRACT_CONFLICT_LEDGER.md` `XD-03`.
  Prompt (`gpt_analyzer.py:786`) định nghĩa nó là **tập bị loại**, *không* phải **hạng 3–5**.
- **Chưa so bảng hiệu chuẩn §4.2 với nền tách miền** của Gate 5 — cần khớp định nghĩa
  `status` ↔ `T1` trước; cấm đọc bảng đó như bằng chứng hiệu năng.
- Phép đo pure-context **chưa từng tồn tại**: lane T-B của V11059 so *«prompt production»* với
  *«prompt production đã xếp lại ba tầng»*, **không** so với `PURE CONTEXT` theo định nghĩa owner.

### Đã tự rút trong phiên

Bản nháp đầu của §3 dựng một khuôn `CONDITION` **12 trường** riêng. **Đã rút** — Gate 5 cùng làn
sóng đã có `CONDITION_CONTRACT` **24 trường**, và dựng khuôn thứ hai là tạo chồng tầng mới
(`§60`). Tệp này nay **trỏ** sang Gate 5, không định nghĩa lại.

---

## 10. Ba lớp nguồn (§62)

| lớp | nội dung |
|---|---|
| **`OWNER_SAID`** | Chín mục tiêu «thuần ngữ cảnh» và `OWNER LOCK` 23:14 04/09 (đã ghi `QD-073`): `MATERIALIZATION_OPTION = B` · `OUTPUT_COUNTERFACTUAL_RANK_PRODUCTION_WRITE = FORBIDDEN` · `MODEL_ACTION = BLOCKED`. Nguyên văn nằm trong prompt phiên và `docs/SO_TUONG_TAC_OWNER.md`. |
| **`CODE_DID`** | Mọi con số trong tệp này đến từ `artifacts/v11165_k6_bangchung.json`, đo trên clone bất biến `mode=ro`, cửa sổ cố định `2026-08-06..2026-09-04`. Mã đọc: `gpt_analyzer.py` sha16 `758c29c13185763f`. Lệnh tái lập: `python _chay.py _k6_bangchung.py`. |
| **`DOC_SAID`** | `_v11137_d30_lane.py:29` ghi *«14/16 model chưa persist top-5»* — **lệch với `CODE_DID`**: dữ liệu hạng 3–5 có thật trong `reasoning_json`, bộ đọc tra nhầm cột. Đã ghi thành `XD-03`. |

**Lệch phải báo, không được im lặng chọn một lớp.** Lệch đã báo: `DOC_SAID ≠ CODE_DID` ở `XD-03`.

---

TanPhatAI cần làm: cập nhật `docs/FOLLOW_UP_TRACKER.md` với **hai** mục treo mới — (a) grain của
`near_miss_shortlist` chưa định nghĩa (chặn `XD-03`), (b) giao diện có render `display_text` hay
không (chặn phạm vi `XD-04`); và theo dõi rằng đặc tả này **chưa có mã**, mọi tham chiếu tới nó
phải ghi tầng `SPEC_ONLY`, cấm nâng lên `CODED`.
