# GÓI DEPLOY & ROLLBACK — `V11165` GATE 14

> **Lập:** 05/09/2026 · **Trạng thái:** `CODED_AND_TESTED_NOT_RUNTIME_PROVEN`
> **Đây KHÔNG phải lệnh deploy.** Không một dòng nào trong gói này đã chạy trên production.
> Owner ký thì mới thi hành.
>
> **Mutation ledger phiên này:** `0` ghi DB production · `0` deploy · `0` restart ·
> `0` sửa tệp đang serve. Mọi tệp ứng viên nằm trong `/root/Lottery_AI_Test/artifacts/`.

---

## NEO NGUỒN — mọi con số dưới đây đo tại chỗ, không chép báo cáo cũ (`RM-11` · `RM-13`)

| | |
|---|---|
| service | `lottery` (**không phải** `lottery-ai`) · `active` · PID **3370750** · NRestarts **0** |
| `gpt_analyzer.py` | sha256 `758c29c13185763f…` · **416.285** byte |
| `main.py` | sha256 `4ed5fd7ebaee8d23…` |
| clone bất biến | `artifacts/v11165_immutable.db` · **813.821.952** byte · `mode=ro` |
| artifact gói | `artifacts/v11165_k14_deploy_packet.json` (**26.870** byte) |

---

## VIỆC 1 — SÁU VÁ + HAI HẠNG MỤC **KHÔNG** ĐỀ NGHỊ DEPLOY

### Thứ tự đề nghị

```
0.   CỔNG-V2        cổng vào TRƯỚC — để có đối chứng "trước khi vá"
1.   VA-A           bịt rò gói ngữ cảnh          ← một biến một lần, đo 3 ngày
1.5  MOD-VANTAY     module vân tay (phụ thuộc của VA-B)
2.   VA-B           vân tay phủ 100%             ← đo 3 ngày
3.   VA-h12         kế toán MT (độc lập)
4.   VA-C           herd keys                    ← ĐỔI PROMPT, không cùng ngày với VA-A
KHÔNG đợt này:      CONTAM-V2 · RENDERER
```

**`QD-018` một biến một lần:** `VA-A` và `VA-C` **đều** đổi nội dung prompt. Deploy cùng ngày thì
không quy được hiệu ứng về từng vá.

---

### `VA-A` — bịt rò **gói ngữ cảnh shadow** vào lượt OFFICIAL

Nửa còn lại của `V11160`. **Độc lập**, thứ tự **1**.

| | |
|---|---|
| tệp · dòng | `web/backend/gpt_analyzer.py:6738` (sửa 1 dòng) + chèn hàm mới sau `:950` |
| **TRƯỚC** | `_shadow_mode = lane_test_shadow_pack or (selected_model in SHADOW_GATE_MODELS)` |
| **SAU** | `_shadow_mode = regime_ctx_cho_luot(lane_test_shadow_pack, selected_model)` + thêm `def regime_ctx_cho_luot(...) -> bool: return bool(lane_test_shadow_pack)` |

**Vì sao.** `V11160` đã bỏ mệnh đề theo-MODEL khỏi `regime_prompt_cho_luot` (quyết định **prompt
nền**) nhưng **không đụng** `:6738` — dòng quyết định **nội dung gói ngữ cảnh**.
`output_eligible ∩ SHADOW_GATE_MODELS = ['gpt-oss-120b']`, một model **OFFICIAL**. Lượt official
của nó nhận thêm **MN +3.208 · MT +3.075 · MB +3.097** ký tự so với 7 official khác, lớn nhất là
khối *"PHASE-FIRST REASONING GATE"* **2.979** ký tự mà 7 model kia **không hề nhận**.
⇒ nhánh official **không còn là đối chứng sạch**. `A58_VIOLATION_HALF_DONE`.

**Vì sao tách thành HÀM có tên:** cổng chỉ soi được thứ **có tên**. Dòng inline chính là lý do cổng
`_v11160_test_lane.py` mù suốt — đo được: nó nhắc `build_context_pack`/`shadow_mode`/`ctx_pack`
**0/3** lần.

**Test đã chạy**

| phép | kết quả |
|---|---|
| dump ctx TRƯỚC/SAU, 3 miền × 8 model official | trước: **2** bản ctx cho official ở **cả ba miền** (do `gpt-oss-120b`) → sau: **1** bản |
| cổng V2 phép (1)(3)(4) | bản đang serve **HỎNG** · bản vá **ĐẠT** |
| `--thu-chan` hai chiều (`RM-15`) | serve **DENY** (thoát 1) · bản vá **ALLOW 7/7** (thoát 0) |
| `py_compile` bản vá | thoát **0** |

**Rủi ro**
- `gpt-oss-120b` (OFFICIAL) sẽ nhận prompt **ngắn hơn ~3.000 ký tự** ⇒ hành vi của **nó** sẽ đổi.
  Đó là **mục đích** của vá, nhưng phải coi là **ĐỔI OUTPUT**, không phải dọn dẹp.
- Lane shadow của `gpt-oss-120b` là `NOT_EXERCISED` từ **01/08** (168 lượt shadow thật 06/06→01/08
  rồi dừng hẳn) ⇒ sau vá, model này không còn đường nào nhận gói shadow.

**Kiểm sau deploy** — `python3 artifacts/v11165_k14_test_lane_v2.py` phải **7/7** (hiện **2/7**) ·
so PID trước/sau · dump lại ctx 8 model × 3 miền, sha **phải giống nhau hết** · hash 4 bảng khoá.

**Gỡ về** — đổi lại một dòng, xoá hàm. **Không** migration, **không** đụng DB, **không** backfill.
Restart `lottery`, so PID.

**Điều kiện dừng** — `gpt-oss-120b` trả JSON hỏng/rỗng ở lượt official (theo dõi 3 ngày) · số
output rỗng của bất kỳ miền nào tăng so với nền 12 ngày.

---

### `VA-B` — vân tay phủ **43,59% → 100%**

**Phụ thuộc `MOD-VANTAY`.** Thứ tự **2**.

| | |
|---|---|
| tệp · dòng | `gpt_analyzer.py:6722-6726` (bỏ băm sớm) + chèn trước `:6904 api_response = _invoke_model_api(prompt)` |
| **TRƯỚC** | `_prompt_sha = sha256(system_prompt + "\n<<<USER>>>\n" + prompt)` — băm **trước** khi nối `_ctx_pack` (`:6755`) và `REASONING_RULEBOOK` (`:6760`) |
| **SAU** | băm sớm ⇒ `None`; tính lại ngay trước `_invoke_model_api` bằng `_v11165_van_tay_payload.van_tay(...)` |

**Vì sao.** Đo trên **57** tổ hợp: vân tay hiện tại phủ **39,81–48,07%** (tb **43,59%**), thiếu
**26.478–35.315** ký tự mỗi lượt; bắt **2/11** phép đột biến (module ứng viên bắt **11/11**).
⇒ `runtime_prompt_sha256` **hiện tại không dùng được** làm bằng chứng "prompt sạch": đổi một chữ
trong `ctx_pack`/rulebook **không** làm nó đổi.

#### 🔴 SỬA SO VỚI BẢN NHÁP LÀN SÓNG 1 — bản nháp **KHÔNG deploy được**

Bản nháp `artifacts/v11165_patch_B_van_tay.diff` gọi `_route_cua_luot` và `_dem_o_nhiem`.
Đo lại trên mã **đang serve**: **cả hai xuất hiện 0 lần**. Tên thật là `_dau_o_nhiem`
(dấu `_dau_`, không phải `_dem_`).

> **Hậu quả nếu deploy bản nháp:** `NameError` bị `except Exception` nuốt ⇒ `_prompt_sha` giữ
> `None`. Vì `VA-B` **đã bỏ băm sớm**, kết quả là **KHÔNG CÒN VÂN TAY NÀO** — **tệ hơn hiện
> trạng**. Đây đúng là `RM-10`: kết luận theo tên đoán.

**Bản sửa** suy route từ **năm cờ boolean CÓ THẬT** đặt ở `:6573` (`is_claude` · `is_deepseek` ·
`is_openrouter` · `is_openai` · `is_gemini`), theo đúng thứ tự `if/elif` của `_invoke_model_api`
(`:6793-6809`). Đã kiểm: cả năm cờ **đều được gán TRƯỚC điểm chèn, trong cùng hàm**
`analyze_and_predict` (`:6553`).

**Rủi ro**
- `runtime_prompt_sha256` **đổi giá trị cho mọi lượt** kể từ khi deploy ⇒ mọi phép so vân tay
  bắc qua mốc deploy là **không so sánh được**. **Phải ghi mốc vào SSOT.**
- `runtime_prompt_chars` **nhảy vọt** (+26k…35k) ⇒ panel/cảnh báo dựa trên ngưỡng ký tự cũ sẽ
  **báo động giả**.
- `_v11165_van_tay_payload.py` đang ở `artifacts/` ⇒ **phải chép sang `web/backend/` trước**,
  nếu không `import` thất bại **im lặng** trong `try/except`.

**Kiểm sau deploy** — một lượt thật: `runtime_prompt_chars` ≈ `prompt_total_chars`, không còn lệch
26k+ · hai lượt cùng miền/model khác regime phải cho vân tay **khác nhau** · cổng V2 phép (5)(6) ĐẠT.

**Gỡ về** — khôi phục khối băm cũ `:6722-6726`, xoá khối chèn. **Không** đụng DB. Vân tay cũ quay
lại — nhưng các dòng đã ghi bằng vân tay mới **vẫn giữ**, nên **phải ghi mốc đổi trong SSOT** để
người đọc sau không so nhầm hai hệ.

**Điều kiện dừng** — log `[PROMPT_FINGERPRINT][V11165] không băm được` xuất hiện > 0 lần/ngày ·
latency tăng có ý nghĩa so với nền 10 ngày (275–1084s).

---

### `VA-h12` — tách kế toán **«CẤP CÓ Ý»** khỏi **«TRƯỢT GATE»**

**Độc lập** (khác tệp với VA-A/VA-B). Thứ tự **3**. Ba khối vá.

| khối | tệp · dòng |
|---|---|
| VA-1 | `main.py:9823-9847` — thêm tập song song `_capped_models`, **giữ nguyên** `filtered_models.add(_dm)` |
| VA-2 | `main.py:10506` + `:10511` — `incomplete_bundle` và `wr_gate_filtered` trừ đi phần bị cấp; **+5 trường kế toán mới** |
| VA-3 | `database.py:5028-5047` + `5074-5091` — `classify_day_status` đọc số model bị cấp từ bundle |

**Vì sao.** `main.py:9840` dùng **một** tập `filtered_models` cho **hai** việc khác hẳn: (a) model
trượt gate chất lượng, (b) model bị **cấp có ý** theo trần MT-13 (`V10752`, owner duyệt 25/06).
Dây chuyền hậu quả: `incomplete_bundle=True` → `INCOMPLETE` → `DEGRADED_LIVE_DAY` +
`EXCLUDE_PRIMARY` → `daily_evaluation` loại ngày khỏi rolling metrics.

**Hậu quả nặng nhất:** rolling WR/TOP1 của MT đang **trễ 71 ngày** — *"7 lượt gần nhất"* tính trên
các lượt **19/06–25/06** tại thời điểm **04/09**.

**Test đã chạy** — **30/30** test đơn vị ĐẠT · replay 90 ngày × 3 miền: **đổi 45** dòng, **giữ 521**
dòng · **MB 0 đổi · MN 0 đổi · MT 45 đổi** (đúng kỳ vọng — chỉ MT có trần voter).

> #### 🔴 Cảnh báo số liệu — phải báo owner TRƯỚC
> Sửa kế toán xong thì số của MT **XẤU ĐI** (vì các ngày bị loại quay lại tập tính):
> `wr7` 14,3% → **0,0%** · `wr14` 14,3% → **0,0%** · `wrALL` 15,1% → **10,9%** ·
> `top1_7` 57,1% → **28,6%** · `top1_14` 57,1% → **21,4%**.
> Đây là **sửa đúng**, không phải hồi quy — nhưng nếu không báo trước thì sẽ bị đọc thành
> *"vá làm hỏng MT"*.

> #### 🔴 Phải rút lại (`PRJ-RETRACTION-001`)
> - *«ít nhất 46/72 quy cho cấp»* — **KHÔNG tái lập được**. Số đúng: **45** ngày cấp giải thích
>   trọn vẹn (hoặc **70** ngày có cấp tham gia).
> - *«MT `EXCLUDE_PRIMARY` 71 ngày liên tiếp»* — chỉ đúng với định nghĩa
>   `evaluation_policy != INCLUDE`. Chuỗi `EXCLUDE_PRIMARY` **liên tiếp thật** chỉ **7 ngày**.

**Rủi ro** — **không** đổi hành vi bỏ phiếu: `filtered_models.add(_dm)` **giữ nguyên**, bundle phải
giống hệt từng byte. `database.py` thêm 1 `SELECT` trong hàm đã mở connection; bundle thiếu/JSON lỗi
⇒ `_capped=[]` ⇒ hành vi **về đúng như trước vá** (fail-safe về phía cũ).

**Kiểm sau deploy** — một ngày MT có cấp: `day_governance` phải ghi `VALID_LIVE_DAY` + `INCLUDE` ·
`wr_gate_filtered` không còn chứa model bị cấp (kiểm **cả ba** điểm đọc: `main.py:489` ·
`main.py:11346` · `web/frontend/du-doan.html:1354`) · bundle `bach_thu`/`lo2`/`lo3` của ngày đó
**KHÔNG ĐỔI** · hash 4 bảng khoá không đổi.

**Gỡ về — ba bước, không cần backfill**
1. `main.py`: xoá `_capped_models = set()` và `_capped_models.add(_dm)`; trả `incomplete_bundle`
   về `model_count < EXPECTED_MODEL_COUNT`; trả `wr_gate_filtered` về `sorted(filtered_models)`;
   xoá 6 khoá mới.
2. `database.py`: xoá khối đọc `source_predictions_json` trong `classify_day_status`; trả
   `quality = classify_bundle_quality(model_count, expected)`.
3. Chạy lại `classify_day_status(date, region)` cho các ngày bị ảnh hưởng — **hoặc không làm gì**:
   các dòng cũ vẫn còn nguyên vị và **chỉ** ghi khi cron verify chạy lại.

**Không** cần dừng service · **không** sửa DB bằng tay · **không** có migration schema.
Hash 4 bảng khoá **không đổi** bởi vá này.

---

### `VA-C` — bộ khoá de-herding **bỏ sót 3 header CÓ THẬT**

| | |
|---|---|
| tệp · dòng | `gpt_analyzer.py:4598` |
| **TRƯỚC** | `("Model Performance", "BT MODEL RANKING", "Width Warning", "Riêng")` |
| **SAU** | thêm `"MB HARD MODE"`, `"MODEL-ONLY CANDIDATE VETO"`, `"Đa dạng model"` |

Quét **6 dump payload THẬT**: 3 header mang meta-model **không** bị strip vì bộ khoá khớp chuỗi con
không phủ. **Lần THỨ HAI cùng họ lỗi** — `V11106` đã phải vá thêm `MB MODEL RANKING`.

**Rủi ro** — strip **thêm** nội dung khỏi `ctx_pack` cho **mọi** model ⇒ **ĐỔI OUTPUT**, không phải
"dọn dẹp". `"Đa dạng model"` là chuỗi **tiếng Việt có dấu** — phải kiểm mã hoá tệp khi vá.
**Không** deploy cùng ngày với `VA-A` (`QD-018`).

**Gỡ về** — trả tuple về 4 phần tử cũ. Không DB, không migration.

---

### `CỔNG-V2` — cổng bất biến lane V2

`artifacts/v11165_k14_test_lane_v2.py` · **11.337** byte · sha256 `ab84c1b8b863b224…`

Cổng `V11160` nhắc **0/3** chuỗi `build_context_pack`/`shadow_mode`/`ctx_pack` ⇒ **mù với nửa
ctx_pack**. Cổng V2 nhắc **3/3** và soi **cả hai** quyết định regime.

**Bảy phép** ① regime ngữ cảnh × lượt official · ② không mất phạm vi đo · ③ không phụ thuộc tên
model · ④ `RM-15` bắt được logic `:6738` · ⑤ vị trí vân tay · ⑥ ô nhiễm quét trên chuỗi cuối ·
⑦ herd keys phủ hết header có thật.

**Kết quả hiện tại trên mã đang serve: `2/7 ĐẠT`** — hỏng (1)(3)(5)(6)(7).
Đó là **đúng**: năm phép hỏng chính là bốn vá chưa vào.

**Thử chặn `RM-15` hai chiều**

| chiều | kết quả |
|---|---|
| bản **đang serve** (có vi phạm) | **DENY** — thoát **1** |
| bản **đã vá** (sạch) | **ALLOW** — **7/7**, thoát **0** |

Deploy **trước** mọi vá để có đối chứng "trước khi vá". Gỡ về: xoá tệp (không tệp nào import nó).

---

### `MOD-VANTAY` — `_v11165_van_tay_payload.py`

Module thuần hàm, không I/O · không DB · không mạng. **Là phụ thuộc của `VA-B`** — phải chép sang
`web/backend/` **trước** `VA-B`. Gỡ về: xoá tệp.

---

### 🔴 HAI HẠNG MỤC **KHÔNG ĐỀ NGHỊ** DEPLOY ĐỢT NÀY

**`CONTAM-V2`** (`artifacts/v11165_k9_contam_v2.py`) — bộ 5 dấu hiện tại báo `0/5` *"sạch"* trong khi
payload thật còn `weight=` **33/33** lượt · `Best MB model` **11/33** · `AI token models 14d WR`
**11/33**; dấu meta thật đếm được **12 (MN) / 11 (MT) / 14 (MB)**. Bộ V2 sửa đúng chỗ đó — **nhưng**
nó đổi `_prompt_contam` từ *"đếm 5 chuỗi"* sang *"bộ phân loại ngữ cảnh"*, tức **đổi nghĩa một cột
đang được ghi vào trace hằng ngày**. Đổi nghĩa một cột mà **không đổi tên cột** là đúng họ lỗi
`V11158` (`MISSING_SHADOW_ROW` gộp 4 lớp ⇒ 1.058 lượt thua ảo).
⇒ nếu dùng, **phải ghi ra cột MỚI** (`runtime_prompt_contam_v2`), giữ cột cũ để so.

**`RENDERER`** (`artifacts/v11165_k9_renderer.py` + `v11165_k9_tests.py`) — bộ thử hiện **68/68 ĐẠT**,
2 mục `KHÔNG_CHẠY_ĐƯỢC`. Đây là ứng viên cho **phép đo shadow**, mà phép đo đó **chưa được
owner-lock preregistration** ⇒ chưa deploy. Xem phần VIỆC 3.

---

## VIỆC 2 — ARTIFACT ĐO LƯỜNG MT theo **PHƯƠNG ÁN B**

> `MATERIALIZATION_OPTION = B` · `OUTPUT_COUNTERFACTUAL_RANK_PRODUCTION_WRITE = FORBIDDEN`

### Phương án B **không phải** "không làm gì" — bản B đang có hỏng bốn chỗ

| # | khiếm khuyết của `v11159_pha1_rank_dong_bang.json` |
|---|---|
| ① | **dừng sinh từ 03/09**, không ai sinh tiếp |
| ② | **chỉ lưu top-10** — bảng xếp hạng đầy đủ bị vứt ngay trong tiến trình sinh |
| ③ | `hang_cua_no_trong_A` = `NULL` **973/973 = 100%** |
| ④ | `meta.bam_artifact` = `9474b7bc…` **≠** sha256 của tệp = `fe9a2741…`, tệp không nói băm nào băm cái gì |

**③ không phải thiếu dữ liệu — nó BẤT KHẢ THI VỀ CẤU TRÚC.** Truy được đến đúng dòng:

```
_run__v11159_pha1.py:158   hang = next(k+1 for k,y in enumerate(rA["ranked"]) if m in y["voters"])
_run__v11159_rank_gen.py:208   gom_shadow = (che_do != "OFFICIAL_ONLY")  → False
_run__v11159_rank_gen.py:212-215   cho_phep = du_dieu_kien   (KHÔNG cộng them_nguon)
                                    raw = [p for p in raw if ai_model in cho_phep]
```

`m` **luôn** là model **shadow**; `rA` sinh ở chế độ `OFFICIAL_ONLY` nên shadow **bị lọc khỏi
`raw`** ⇒ **không bao giờ** có trong `voters` ⇒ `next(...)` **luôn** rơi về `None`.
Đổ dữ liệu vào trường này bao nhiêu lần cũng vẫn `NULL`.

### Bản thay thế — `artifacts/v11165_k14_mt_artifact.py`

sha256 `c63419f5b7555809…` · **31.350** byte

**Đã chạy thật trên dữ liệu lịch sử** — MT, `2026-06-07 … 2026-09-04`:

| | |
|---|---|
| tệp ra | `artifacts/v11165_k14_mt_rank_2026-06-07_2026-09-04_MT_r2.jsonl` |
| số dòng | **2.635** (1 HEADER · 90 ô · **2.544** ứng viên) |
| kích thước | **2.568.125** byte (**2,45 MB**) |
| sha256 tệp | `8bd4ab818deda57a0c37700a3d0307efdc22c3692ab73e6784d6a65dcdc02c3b` |
| sha256 nội dung | `c5e0b58831e03fcdad02e199fb8126e114c7a02ae15623c3cd65477679f23b58` |
| quyền tệp | `0444` (bất biến) |

### `NULL` hai nghĩa — chỗ `V11163` khuyến nghị **đừng đổ** cột `INTEGER`

Artifact này **không bao giờ** ghi `NULL` cho hạng. Mọi dòng có `trang_thai` thuộc **bảy** nhãn
loại trừ nhau, và `hang` có giá trị **khi và chỉ khi** `trang_thai == "CO_HANG"`:

| trạng thái | số dòng |
|---|---|
| `CO_HANG` | **2.247** |
| `MODEL_KHONG_CO_DONG` | 132 |
| `MODEL_BI_CAP_CO_Y` | **122** |
| `MODEL_BI_LOAI_CONG` | **38** |
| `SO_KHONG_HOP_LE` | 5 |
| `NGOAI_HAI_VI_TRI_DAU` · `O_KHONG_SINH_DUOC_BANG` | 0 (định nghĩa sẵn) |

**`MODEL_BI_CAP_CO_Y` 122 vs `MODEL_BI_LOAI_CONG` 38** — chính là hai thứ mà production đang gộp
làm một (xem `VA-h12`). Artifact tách được **mà không cần đụng production**.

### Bảng xếp hạng **ĐẦY ĐỦ**, không cắt cụt

**71/90 ô có hơn 10 ứng viên**, ô lớn nhất **19** ứng viên, tổng **1.127** ứng viên.
⇒ cách lưu top-10 cũ **mất dữ liệu ở 78,9% số ô MT**. Mỗi ô kiểm `len(bảng) == so_ung_vien`.

### Tự bắt chính mình rơi vào bẫy vừa vá

Bản `r1` ghi `prompt_version = None` cho **50,4%** dòng — **đúng cái bẫy `NULL` hai nghĩa** mà
artifact này tuyên bố sửa (*"model ML không đi qua đường prompt"* lẫn với *"không tìm thấy dòng
trace"*). Bản `r2` thêm `prompt_version_trang_thai`, phân biệt **bằng phép đo** (model có xuất hiện
trong `prediction_trace.jsonl` ở bất kỳ ô nào không), **không** bằng danh sách tên đoán (`RM-10`):

| trạng thái | số dòng |
|---|---|
| `CO` | 1.261 |
| `KHONG_AP_DUNG_MODEL_KHONG_QUA_DUONG_PROMPT` | 1.258 |
| `KHONG_TIM_THAY_DONG_TRACE_CHO_O_NAY` | 25 |

### Trung thực về `payload_sha256`

Mỗi dòng mang `payload_sha256_do_phu = "PHAN_PHAN_43.59pct_BAM_TRUOC_CTX_PACK"`. Vân tay lấy từ
trace là vân tay **của mã đang serve**, tức chỉ phủ **43,59%**. Ghi rõ để không ai đọc thành
"băm đầy đủ". Sau khi `VA-B` vào runtime, độ phủ mới thành 100% và phải ghi mốc.

### Chống oracle · bất biến · cấm cron

- Mọi truy vấn qua `CanhGac`: **ném** `LoiOracle` khi chạm `lottery_results` hoặc đọc cột kết quả
  của ngày đích (T05/T06 ĐẠT). **0** trường outcome trong toàn tệp.
- **Append-only**: chạy lại ⇒ **TỪ CHỐI GHI ĐÈ** (thoát 1), sha256 tệp **không đổi**. Tên tệp
  **kèm phiên bản** để hai lần chạy không trộn vào một tệp.
- **Manifest ghi rõ băm nào băm cái gì** — `sha256_tep_jsonl` (toàn bộ byte) và `sha256_noi_dung`
  (JSON canonical đã sắp xếp, độc lập thứ tự dòng). Đây là chỗ bản `v11159` làm người đọc không
  kiểm được.
- **Cấm cron**: giả lập môi trường cron ⇒ **từ chối chạy** (T07 ĐẠT). **Không** đăng ký crontab nào.
  Lý do ghi thẳng trong log: `MT_PREREGISTRATION = NOT_READY_FOR_OWNER_LOCK`.

**Kiểm chứng: `13/13` phép độc lập ĐẠT · `15/15` phép tự kiểm ĐẠT**
(`artifacts/v11165_k14_mt_artifact_kiem.json`).

---

## VIỆC 3 — `PURE_CONTEXT_CANDIDATE` = **`BLOCKED_WITH_EXACT_REASONS`**

**6 blocker · 1 indeterminate · 6 không chặn.**

| mã | điều kiện dừng | trạng thái |
|---|---|---|
| SC-01 | không dùng được full final payload | 🟢 không chặn |
| **SC-02** | **hash coverage < 100%** | 🔴 **CHẶN** |
| SC-03 | `build_context_pack` còn side effect | 🟢 không chặn |
| **SC-04** | **candidate vẫn có preselected basket** | 🔴 **CHẶN** |
| **SC-05** | **condition không truy được về raw source/cutoff** | 🔴 **CHẶN** |
| SC-06 | same-day outcome lọt vào | 🟢 không chặn |
| **SC-07** | **routing vẫn phụ thuộc `selected_model`** | 🔴 **CHẶN** |
| **SC-08** | **model bị yêu cầu làm việc không có phương tiện để làm** | 🔴 **CHẶN** |
| SC-09 | provider bị truncation | 🟡 không chặn **nhưng phải canh** |
| SC-10 | output schema không tương thích **UCC** | ⚪ **INDETERMINATE** |
| SC-11 | negative test không bắt được lỗi | 🟢 không chặn |
| **SC-12** | **MT cấp vẫn bị tính là gate failure** | 🔴 **CHẶN** |
| SC-13 | cần production mutation | 🟢 không chặn |

### Ba blocker **đã có vá**, chỉ chờ owner ký

`SC-02` → `VA-B` · `SC-07` → `VA-A` · `SC-12` → `VA-h12`. Cả ba đã code, đã test, đã có gỡ về.

### Ba blocker là **BẢN CHẤT của prompt production** — không vá nào trong gói này gỡ được

**`SC-04` — rổ số chọn sẵn.** Đo lại trên dump thật: official **6** dấu rổ-chọn-sẵn mỗi miền;
lane `CONTEXT_ONLY_V2` **vẫn còn 5**. Model-meta: official **30–32**, context-only **0–2**.
⇒ thứ đang được gọi là *"thuần ngữ cảnh"* **không thoả** định nghĩa owner.

**`SC-05` — điều kiện không truy được về nguồn.** 35 producer: **27** bơm
`AGGREGATED_NUMBER_SET` · **2** `RAW_NUMBER_FACT` · **chỉ 1/35** có nền tường minh.
`CONDITION_CONTRACT v1.0` đã định nghĩa đủ 24 trường bắt buộc, nhưng **production chưa áp**.

**`SC-08` — mệnh lệnh trỏ vào dữ liệu không có.** Khối §19 *"Bạn PHẢI quét 8 cửa sổ thời gian"*
(`MB:962-977`) bắt model chấm `1W…8W`, và quy tắc chọn **khoá thẳng vào 8W**:
*"Tất cả 1W→8W mạnh → SỐ ĐÁNG TIN NHẤT → chọn ngay"*.
Đo số liệu thực tế trong payload: **`7W` và `8W` có 0 dòng số liệu ở CẢ 6 DUMP**. Sáu cửa sổ còn
lại chỉ có **đúng một dòng TỔNG HỢP** (`Windows: 1W(7d):24/42=57% | … | 6W(42d):250/384=65%`) —
tỉ lệ chung của miền × thứ, **không** phải số liệu theo **từng ứng viên**, trong khi quy tắc lại
viết theo từng ứng viên. Không có tool-calling ở bất kỳ model nào (**0** dòng trên toàn
`web/backend`) ⇒ model **không có cách nào** lấy phần thiếu ⇒ **buộc phải tự bịa**.
`PRJ_PROMPT_DANGLING`. Có mặt ở **cả official lẫn context-only**.

> #### 🔴 Tự rút lại trong chính phiên này (`PRJ-RETRACTION-001` · `RM-09`)
> Phép đo **đầu tiên** của tôi kết luận *"7/8 cửa sổ không có dữ liệu"* — **SAI**. Mẫu
> `\b14\s*ngày\b` bỏ sót cách viết thật là `2W(14d)`. Kiểm lại bằng **8 cách viết khác nhau** mới
> ra kết quả đúng ở trên. Kết luận **CHẶN vẫn đứng**, nhưng **lý do đúng** là `7W`/`8W` trống +
> thiếu độ phân giải theo ứng viên — **không phải** *"7/8 cửa sổ trống rỗng"*.

### `SC-10` — không đánh giá được

Quét toàn bộ `web/backend` + `artifacts`: **"UCC" không có định nghĩa nào**. 12 tệp khớp chỉ vì
`UCC` là chuỗi con của `SUCCESS`. `RM-10` cấm kết luận theo tên đoán ⇒ **không thể** đánh giá một
hợp đồng chưa được định nghĩa. **Cần owner chỉ rõ `UCC` là gì**, hoặc tên thật của hợp đồng đầu ra.

### `SC-09` — không chặn nhưng phải canh

`prediction_trace.jsonl` 6.533 dòng: `finish_reason = 'length'` **2** + `FinishReason.MAX_TOKENS`
**1** = **3/6533 = 0,046%** · `timeout_or_fallback` False **6533/6533**.
**Cảnh báo:** prompt thuần-ngữ-cảnh **dài hơn** official (MN 53.877 vs 50.464 · MT 54.571 vs 51.487
· MB 58.124 vs 55.178) ⇒ rủi ro truncation **tăng**, và **chưa có phép đo nào** trên prompt mới ở
quy mô ⇒ `INDETERMINATE` cho bản mới.

### Câu chốt

Kể cả khi gỡ hết **6 blocker kỹ thuật**, phép đo **vẫn chưa được phép kết luận**:
`MT_PREREGISTRATION = NOT_READY_FOR_OWNER_LOCK` và `POOL_VERDICT = HOLD`.
Và chưa **ai từng đo** một prompt thoả đủ **chín điều kiện** owner đặt ra — phép đo lane ba tầng
T-B (`101/96` cặp bất đồng · McNemar `z = -0,0995` **không** hiệu chỉnh liên tục · `p = 1,00` **có**
hiệu chỉnh — **hai phép khác nhau, cấm ghép một dòng**) so *"prompt production"* với *"prompt
production đã xếp lại ba tầng"*, **không** phải so với **pure context**.

---

## BA LỚP NGUỒN (`§62` / `A60`)

**`OWNER_SAID`** — `MATERIALIZATION_OPTION = B · OWNER_LOCKED` · `OPTION_A = REJECTED` ·
`OUTPUT_COUNTERFACTUAL_RANK_PRODUCTION_WRITE = FORBIDDEN` ·
`CURRENT_FROZEN_ARTIFACT_ROLE = AUDIT_EVIDENCE_ONLY` ·
`MT_PREREGISTRATION = NOT_READY_FOR_OWNER_LOCK` · `POOL_VERDICT = HOLD` ·
`MODEL_ACTION = BLOCKED` (khoá 23:14 04/09, đã ghi `QD-073`).

**`CODE_DID`** — `gpt_analyzer.py:6738` vẫn còn mệnh đề theo-MODEL (cổng V2 phép (1) HỎNG) ·
`gpt_analyzer.py:6723` băm trước khi nối (phép (5) HỎNG) · `gpt_analyzer.py:4598` bỏ sót 3 header
(phép (7) HỎNG) · `main.py:9840` gộp cấp có ý với trượt gate (artifact MT đo: 122 vs 38 dòng) ·
`_v11159_pha1.py:158` cấu trúc bất khả thi ⇒ `NULL` 973/973.

**`DOC_SAID`** — `docs/DE_XUAT_MATERIALIZATION_V11163.md` §10 (ba lựa chọn A/B/C, agent nghiêng B) ·
`docs/FOLLOW_UP_TRACKER.md:51` (`NULL` 973/973 · 420 hạng cắt cụt) · `CHANGELOG.md` V11163/V11164.

**Lệch giữa ba lớp** — `DOC_SAID` nói phương án B *"không làm gì thêm — artifact đã có đủ"*, nhưng
`CODE_DID` cho thấy bản B **dừng sinh 03/09**, **cắt cụt top-10 ở 71/90 ô MT**, và có một trường
`NULL` **100%** vì lý do cấu trúc. ⇒ **Phương án B đúng như owner khoá, nhưng bản B đang có thì
chưa dùng được** — đó là lý do có VIỆC 2.

---

## GHI CHÚ TÁI LẬP

| artifact | nội dung |
|---|---|
| `artifacts/v11165_k14_deploy_packet.json` | gói đầy đủ 8 hạng mục, mọi hash đo tại chỗ |
| `artifacts/v11165_k14_verdict.json` | 13 stop condition + phép đo trên 6 dump |
| `artifacts/v11165_k14_mt_artifact.py` | mã sinh artifact MT (phương án B) |
| `artifacts/v11165_k14_mt_rank_*_r2.jsonl` + `.manifest.json` | artifact MT + manifest |
| `artifacts/v11165_k14_mt_artifact_kiem.json` | 13/13 phép kiểm độc lập |
| `artifacts/v11165_k14_test_lane_v2.py` | cổng V2 |
| `artifacts/v11165_k14_test_lane_v2_thuchan.json` | thử chặn `RM-15` hai chiều |
| `artifacts/v11165_k14_gpt_analyzer_VA_A_B.py` | bản vá sandbox (A+B+C) — **chưa deploy** |
| `artifacts/v11165_k14_sc08_chot.json` | phép đo 7W/8W trên 6 dump |

**Trần verdict phiên này: `CODED_AND_TESTED_NOT_RUNTIME_PROVEN`.**
Không hạng mục nào được ghi `DEPLOYED` / `RUNTIME_PROVEN` / `OFFICIAL_CLEAN` /
`PREDICTIVE_IMPROVEMENT_PROVEN`.

---

TanPhatAI cần làm: cập nhật `docs/FOLLOW_UP_TRACKER.md` mục `NULL 973/973` — nguyên nhân đã truy
được là **bất khả thi về cấu trúc** (`_run__v11159_pha1.py:158` × `rank_gen.py:212-215`), không
phải thiếu dữ liệu, nên **đổ bao nhiêu lần cũng vẫn `NULL`**; ghi nhận bản thay thế
`v11165_k14_mt_rank_*_r2.jsonl` (2.635 dòng · 7 trạng thái · bảng xếp hạng đầy đủ · `0444`) là
hiện thân mới của **phương án B** mà owner đã khoá; theo dõi **6 blocker** của
`PURE_CONTEXT_CANDIDATE` (3 đã có vá chờ ký: `VA-A`/`VA-B`/`VA-h12`; 3 cần renderer +
preregistration: `SC-04`/`SC-05`/`SC-08`); và **hỏi owner định nghĩa `UCC`** vì `SC-10` hiện
`INDETERMINATE` — chuỗi này không tồn tại trong kho. Phiên này **code đi trước tài liệu**: mọi tệp
ứng viên nằm trong `artifacts/`, **chưa deploy**, xem mục VIỆC 1 để biết chỗ nào đi trước.
