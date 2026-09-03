# REPORT V11160 — VÁ LỖ RÒ PROMPT THÍ NGHIỆM VÀO ĐƯỜNG OFFICIAL

> **Ngày:** 04/09/2026 00:20–00:55 (VN) · `CURRENT_ACTOR = CLAUDE_CODE`
> `POOL_VERDICT = HOLD` · `MODEL_ACTION = BLOCKED` · Prompt 43 R1 **PARTIAL**
> **Đây là bản SỬA cho lỗi do chính agent gây ra ở `V11157`**, đã rút lại ở `V11159`.

---

## 1 · Tóm tắt

`V11159` phát hiện `V11157` đã **rò prompt thí nghiệm vào đường official**. Bản này vá dứt điểm
ba việc, mỗi việc có phép kiểm riêng:

| # | việc | kiểm |
|---|---|---|
| ① | vá định tuyến lane | cổng mới **7/7** dưới env service |
| ④ | gỡ mệnh lệnh treo `PRJ_PROMPT_DANGLING` | dump từ hàm đang serve **6/6** |
| ③ | thêm vân tay prompt runtime vào trace | **6/6** · legacy **5** dấu ô nhiễm vs ngữ cảnh thuần **0** |

Deploy `PID 3299063 → 3366433 → 3367598` · neo FINAL 558 **nguyên** · 4 bảng khoá **không đổi**.

---

## 2 · Owner yêu cầu gì — NGUYÊN VĂN

| giờ (VN) | NGUYÊN VĂN | loại |
|---|---|---|
| 04/09 ~00:2x | *«ok em thực hiện tuần tự lần lượt xử lý dứt điểm các vấn đề em đã đào ra dùm anh»* | `YÊU_CẦU` |

Đây là **uỷ quyền thi hành** cho năm việc agent liệt kê cuối `V11159` — trong đó việc ① từng ghi
*«CHỜ OWNER — chạm đường official»*. Câu này mở khoá đúng việc đó.

---

## 3 · Đào bới / phát hiện

### 3.1 · Gốc lỗi — hợp tín hiệu PER-RUN với danh sách PER-MODEL

`gpt_analyzer.py` bản cũ:

```python
_la_shadow = bool(lane_test_shadow_pack) or (selected_model in SHADOW_GATE_MODELS)
```

`lane_test_shadow_pack` có tài liệu ngay trong mã: *«True chỉ từ `shadow_auto_eval`»* — tức tín
hiệu **THEO LƯỢT**. `SHADOW_GATE_MODELS` là danh sách **THEO MODEL**. Hợp bằng `or` biến cái thứ
nhất thành cái thứ hai.

Đo được:

```
SHADOW_GATE_MODELS ∩ get_output_eligible_ids(MN|MT|MB) = ['gpt-oss-120b']   ← DUY NHẤT
gpt-oss-120b (60 ngày): 82 lượt shadow  ·  100 lượt OFFICIAL   ← model HAI LANE
```

### 3.2 · Đo TRƯỚC khi sửa — để chắc không mất phạm vi đo

Nếu loại thẳng model output-eligible khỏi lane thí nghiệm thì **mất 82 lượt đo** của
`gpt-oss-120b`. Nên phải sửa theo **lượt**, không theo model. Kiểm giả thuyết đó:

| | |
|---|---|
| model nhận prompt ngữ cảnh thuần ngày 03/09 | **12** |
| trong đó **KHÔNG** nằm trong `SHADOW_GATE_MODELS` | **10/12** |
| ⇒ chúng đã đi bằng `lane_test_shadow_pack` sẵn | |
| hai model còn lại (`gpt-5.5`, `gpt-oss-120b`) | đều **có** lượt `shadow_auto_eval` thật |
| chỗ gọi `lane_test_shadow_pack=True` | `scheduler.py:7690` — **duy nhất**, đúng đường shadow-eval |

⇒ **Bỏ mệnh đề theo-model mất 0 lượt đo.**

### 3.3 · Mệnh lệnh treo — `PRJ_PROMPT_DANGLING`

Mục yêu cầu số 3 nguyên văn:

> `3. THAM KHẢO hiệu suất gần đây và số đã trúng để điều chỉnh confidence`

Nó trỏ thẳng vào khối `Phase 11` — mà `CONTEXT_ONLY_V2` **đã gỡ** (`:3000` in
`[Phase 11][CONTEXT_ONLY_V2] BỎ QUA win-rate miền + số đã trúng gần đây`). Có mặt trong **100%**
prompt ngữ cảnh thuần. Đúng ca `§60.1` đã cảnh báo từ `V11001`: *«gỡ dữ liệu mà để câu lệnh trỏ
vào nó thì model tự bịa ra hoặc tự suy lại mệnh lệnh cũ»*.

### 3.4 · Vì sao `SCHEDULED_SHADOW_PROMPT_CLEAN_PROVEN` không đóng được

Trace **không có vân tay prompt nào**: `custom_prompt.sha256` là khối `ARCHIVE_ONLY`
`runtime_active=false`, **giống hệt ở cả 62 dòng**; `prompt_version=PB-20.1` giống nhau ở **cả
hai** regime. Mọi bằng chứng về prompt sạch đều chỉ là **cờ tự khai**.

---

## 4 · Hướng xử lý và vì sao chọn

**Vì sao tách thành hàm CÓ TÊN.** Bản cũ tính thẳng trong thân `analyze_and_predict` nên **không
cổng nào soi được nó** — lỗi sống trọn một ngày trong khi hai bản báo cáo vẫn khẳng định
*«official không đổi một ký tự prompt»*. `regime_prompt_cho_luot()` tồn tại để cổng duyệt được
**MỌI** model, không phải một mẫu.

**Vì sao `selected_model` không ảnh hưởng kết quả của hàm đó.** Cố ý — để không ai lén đưa một
danh sách model nào khác vào quyết định này lần nữa.

**Vì sao đánh số lại danh sách yêu cầu thay vì để trống mục 3.** Giữ khoảng trống cũng là một dấu
hiệu để model đoán rằng có thứ gì đó bị lấy đi.

**Vì sao đếm dấu ô nhiễm ngay trên chuỗi thật.** `RM-14`: mọi con số về prompt phải đo trên **dump
production**, không phải bản đọc từ tài liệu. Đếm `> 0` ở lượt khai `CONTEXT_ONLY_V2` là **mâu
thuẫn tự lộ**, đọc thấy ngay trong trace.

---

## 5 · Đã làm gì — TRƯỚC / SAU / PHIÊN BẢN / KIỂM

| | TRƯỚC | SAU |
|---|---|---|
| quyết định regime | `lane_test_shadow_pack or model in SHADOW_GATE_MODELS`, tính inline | `regime_prompt_cho_luot()` — hàm có tên, **chỉ** theo lượt |
| nhãn trace `is_shadow_lane` | `_la_shadow` (per-model) | `_la_shadow_prompt` (per-run) |
| mục yêu cầu số 3 | luôn có | **gỡ** khi ngữ cảnh thuần, đánh số lại `1–7` |
| vân tay prompt | không có | `runtime_prompt_sha256` · `_chars` · `_contam_hits` |

**Kiểm — cổng `_v11160_test_lane.py`, chạy DƯỚI env service thật:**

| phép | kết quả |
|---|---|
| ① mọi model output-eligible × lượt OFFICIAL ⇒ KHÔNG prompt thí nghiệm | ĐẠT · duyệt **15** · vi phạm **0** |
| ② mọi model × lượt SHADOW THẬT ⇒ CÓ prompt thí nghiệm | ĐẠT · duyệt **22** · mất **0** |
| ③ kết quả KHÔNG phụ thuộc tên model | ĐẠT |
| ④ **`RM-15` — cổng BẮT ĐƯỢC logic cũ** | ĐẠT · tìm ra đúng **`['gpt-oss-120b']`** |
| ⑤ fail-closed `off/shadow/all` | ĐẠT |
| ⑥ `off` ⇒ không lượt nào ăn | ĐẠT |
| ⑦ `all` (owner ký Cutover) ⇒ mọi lượt ăn | ĐẠT |

**Kiểm mệnh lệnh treo — dump từ hàm đang serve (`RM-14`): 6/6 ĐẠT**

| miền | legacy | ngữ cảnh thuần |
|---|---|---|
| MN · MT · MB | mệnh lệnh **CÓ** · 8 mục `1–8` | mệnh lệnh **KHÔNG** · 7 mục `1–7` |

**Kiểm vân tay: 6/6 ĐẠT** — ba biến khởi tạo TRƯỚC `try` · ba tham số mặc định `None` (gọi kiểu
cũ vẫn chạy) · vân tay **khác nhau** giữa hai regime · đếm ô nhiễm **legacy 5 vs ngữ cảnh thuần 0**.

---

## 6 · Cổng kiểm

| cổng | kết quả |
|---|---|
| giờ ngoài block 15:30–18:15 | ✓ `00:38` và `00:52` |
| neo FINAL 558 | ✓ `a82c508d…` nguyên qua **2** lần restart |
| 4 bảng khoá | ✓ `14120 · 564 · 15410 · 13984` không đổi |
| health + PID đổi | ✓ |
| nhập thử TRƯỚC restart | ✓ `IMPORT_OK True False False` |
| **cổng lane dưới env service** | ✓ **7/7** |
| trace thật không bị nhiễm dòng thử | ✓ 6.473 dòng · **0** dòng thử nghiệm |

**Gỡ về:** `python _v11160_deploy.py --go-ve` — khôi phục `gpt_analyzer.py` từ `.V11160B.bak`,
xoá `_v11160_test_lane.py`, restart, kiểm neo.

---

## 7 · Vướng vấp

**🟡 ① `_chay.py --env` dính bẫy null-byte.** Chuỗi `tr '\0' '\n'` viết trong heredoc thành **ký
tự null thật**, Windows `CreateProcess` từ chối. Sửa bằng `xargs -0` — đọc thẳng null-separated,
không cần viết ký tự null trong mã nguồn. Đây là bẫy đã có trong sổ ghi nhớ và vẫn vấp lại.

**🟡 ② Raw-string kết thúc bằng dấu `\` trong lệnh một dòng** làm hỏng cú pháp. Chuyển sang dấu
gạch xuôi.

---

## 8 · Gỡ về

Đã thử **không** cần dùng — cả hai lần deploy đều qua cổng ngay lần đầu. Lệnh gỡ về có sẵn và đã
kiểm được đường dẫn `.bak`. Bảng `.bak` giữ: `gpt_analyzer.py.V11160.bak` (bản trước ①) và
`gpt_analyzer.py.V11160B.bak` (bản trước ③④).

---

## 9 · Theo dõi tiếp

| việc | trạng thái |
|---|---|
| xác nhận vân tay xuất hiện trong lượt scheduled thật | **chờ lượt MN ~05:15 ngày 04/09** |
| `SCHEDULED_SHADOW_PROMPT_CLEAN_PROVEN` | có thể đóng **sau** lượt scheduled đầu tiên có vân tay |
| chú thích ngược `main.py:12306-12307` | chưa xử |
| 7/8 trường lineage 3-càng | chưa tồn tại |
| 6/62 dòng trace không nối được sang `predictions` | chưa truy nguyên |
| journal giờ 17 có 0 dòng dù 12 model chạy | chưa giải thích được |

---

## Nguồn ba lớp (§62)

### `OWNER_SAID`
- 04/09 ~00:2x — *«ok em thực hiện tuần tự lần lượt xử lý dứt điểm các vấn đề em đã đào ra dùm anh»*

### `CODE_DID`
- `gpt_analyzer.py:935` `regime_prompt_cho_luot()` · `:6650` call site · `:1641-1643` + `:1743-1745` trace
- cổng `_v11160_test_lane.py` **7/7** dưới env service, phép ④ tìm ra `['gpt-oss-120b']`
- deploy `PID 3299063 → 3366433 → 3367598`, neo 558 nguyên
- dump prompt: legacy **5** dấu ô nhiễm · ngữ cảnh thuần **0**

### `DOC_SAID`
- `gpt_analyzer.py:6600` chú thích `V11152` *«Hợp hai cái lại là đúng tập lượt challenger»* —
  **`DOC_SAID` ≠ `CODE_DID` từ V11160**. Giữ nguyên câu cũ làm dấu vết, ghi thẳng bên dưới rằng
  nó SAI và sai ở đâu, thay vì xoá.
- `CLAUDE.md` `§60.1` ca `V11001` — phiên này là ca lặp lại **đúng** kịch bản đó, và lần này
  bắt được bằng quét ngược có phân loại.
- `docs/CURRENT_TRUTH_SSOT.md` §V11159 ghi *«nhánh đối chứng official KHÔNG sạch từ 03/09»* —
  nay ghi tiếp: **đã sạch từ 04/09 00:38**.

---

TanPhatAI cần làm: ghi **`V11160`** — `governance_seq 476`, công khai bản này. Ghi **đã VÁ lỗ rò prompt thí nghiệm vào đường official**: gốc lỗi là hợp tín hiệu **PER-RUN** (`lane_test_shadow_pack`) với danh sách **PER-MODEL** (`SHADOW_GATE_MODELS`); `gpt-oss-120b` là model duy nhất ở giao đó và chạy **cả hai lane** (82 shadow + 100 official/60 ngày). Ghi **bỏ mệnh đề theo-model mất 0 lượt đo** — đo được 10/12 model đã đi bằng `lane_test_shadow_pack` sẵn. Ghi **cổng mới `_v11160_test_lane.py` 7/7 dưới env service**, phép ④ (`RM-15`) chứng minh cổng **bắt được logic cũ**. Ghi **gỡ mệnh lệnh treo** *«THAM KHẢO hiệu suất gần đây»* — có trong 100% prompt ngữ cảnh thuần, kiểm dump từ hàm đang serve **6/6**. Ghi **ba trường vân tay prompt runtime** — legacy **5** dấu ô nhiễm vs ngữ cảnh thuần **0**. Ghi **nhánh đối chứng official ĐÃ SẠCH từ 04/09 00:38**. Ghi **neo 558 nguyên qua 2 lần restart · 4 bảng khoá không đổi**. **Không mở Prompt 44. Không mở FU mới.** `POOL_VERDICT` giữ **`HOLD`**.
