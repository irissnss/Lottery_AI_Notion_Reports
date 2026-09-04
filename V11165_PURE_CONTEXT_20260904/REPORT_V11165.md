# REPORT V11165 — OWNER-LOCK B · PURE-CONTEXT END-TO-END RECONCILIATION

> **Ngày:** 04/09/2026 23:14 → 05/09/2026 (VN) · `CURRENT_ACTOR = CLAUDE_CODE`
> **Quy mô:** 2 làn sóng · 14 cổng · **70 agent** · **56 phản biện độc lập** · 0 lỗi ·
> **283 artifact · 837,5 MB** · 11,7 triệu token subagent.
>
> `MATERIALIZATION_OPTION = B` · `MATERIALIZATION_OWNER_DECISION = OWNER_LOCKED` (**`QD-073`**)
> `OPTION_A = REJECTED` · `OPTION_C = DEFERRED_UNTIL_SQL_CONSUMER_AND_GRAIN_DEFINED`
> `OUTPUT_COUNTERFACTUAL_RANK_PRODUCTION_WRITE = FORBIDDEN`
> `MT_PREREGISTRATION = NOT_READY_FOR_OWNER_LOCK` · `POOL_VERDICT = HOLD` · `MODEL_ACTION = BLOCKED`
> `PROMPT_43_R1 = PARTIAL` · `GRAND_OVERHAUL_CHAIN = PARTIAL`
>
> ## `PURE_CONTEXT_CANDIDATE = BLOCKED_WITH_EXACT_REASONS`
> **6 blocker · 1 indeterminate.** Ba blocker **đã có vá, chờ owner ký**; ba blocker còn lại là
> **bản chất của prompt production**, cần renderer + đăng ký trước.

---

## 1 · Tóm tắt — EXECUTIVE VERDICT

**Câu hỏi lớn nhất của owner — «prompt đã thuần ngữ cảnh chưa?» — nay có câu trả lời bằng số:
CHƯA, và cách xa hơn mọi báo cáo trước đây từng ghi.**

| đo được | con số |
|---|---|
| cờ `context_only` gác được bao nhiêu điểm bơm chuỗi | **6/171 = 3,51%** |
| `build_context_pack` (141 điểm) được gác | **0** |
| cổng `CONTEXT_ONLY_V2` gác được bao nhiêu nhóm khối | **1,5 / 14** |
| lượt shadow vẫn nhận rổ số đã chọn sẵn | **33/33** |
| payload thật trượt `CONTAMINATION_GATE_V2` | **57/57**, trung bình **220 điểm ô nhiễm** mỗi bản |
| producer bơm bộ số tổng hợp | **27/35** · raw fact **2/35** · **có nền tường minh 1/35** |
| đuôi được bơm vào prompt MN dưới 23 nhãn | **83/100** |

Sửa **đủ 14 nhóm** chỉ gỡ **~15%** độ dài payload — nên **«thuần ngữ cảnh» không phải chuyện cắt
ngắn prompt**, mà là chuyện **thay rổ số bằng điều kiện có nền**.

### Ba điều nặng nhất

**① Phép đo owner cần ĐÃ CHẠY XONG TỪ LÂU, đủ mẫu, và chưa ai đọc verdict.**
Lane prompt ba tầng `T-B` (V11059): n=346 · b=51 · c=50 · **101 cặp bất đồng** · z = **−0,0995** ·
CONTROL 33,53% vs T-B 33,24%. Theo đúng ngưỡng khoá 11/08: T1 ĐẠT · T3 ĐẠT · T2 **KHÔNG ĐẠT** ⇒
`NO_ANOMALY_FOUND`. **Nhưng bốn điều chưa ai đọc, cả bốn đổi cách hiểu:**

- **Ngưỡng `n=96` chỉ là 50% SỨC MẠNH** — công thức `(1,96/(2ψ−1))²` **thiếu số hạng `z_β`**.
  Đúng phải **194 cặp** cho power 80%. Sức mạnh thực tế đạt được tại m=101 chỉ **52%**.
- **Cả HAI nhánh đều không khác mức chọn ngẫu nhiên** ở cả ba miền (|z| max = 1,42). Con số gộp
  «33,24% vs 33,53%» là trung bình của **ba nền khác nhau** (MB 23,90% · MT 34,52% · MN 43,15%).
- **«Đổi 70,2% số chọn» phải đọc cạnh sàn nhiễu 61,3%** — gọi LẠI cùng một model AI đã cho top-1
  khác **61,3%** số lượt. Cùng bậc độ lớn ⇒ phần quy cho prompt là **nhỏ**.
- **Sáu ổ ô nhiễm còn nguyên trong mã ĐANG SERVE, ở CẢ HAI nhánh.**

⇒ Phép đo đó nói: *«xếp lại ba tầng mà vẫn giữ rổ số thì không khác»*. Nó **KHÔNG** nói *«pure
context vô dụng»*. **Chưa ai từng đo một prompt thoả đủ chín điều kiện owner đặt ra.**

**② Prompt đã phục vụ ngày 04/09 KHÔNG tái dựng được — hệ không lưu nó.**
Vân tay runtime khớp **0/60** lượt. Quét độ sâu thống kê 7…180 ngày, **không bản render nào** tái
lập được khối TOP-5 mà model trích dẫn. Bằng chứng quyết định: **ba model của ba nhà cung cấp khác
nhau** (`glm-5.2`, `gemini-3.5-flash`, `gemini-3.6-flash`) cùng ghi `39: 77.7pt, WARM, UP, #2` cho
MT — mà chuỗi `77.7` **không tồn tại trong bất kỳ bản render nào**. Ba model độc lập không thể bịa
ra cùng một bộ bốn (số + giá trị + hạng + zone) ⇒ **chuỗi đó CÓ THẬT trong prompt đã gửi, và hệ
thống không lưu bản prompt đó** (chỉ lưu sha256 phủ ~43,6%).

**③ Phép so official-vs-shadow đang đổi ít nhất BA biến cùng lúc.**
Official (`scheduler.py:4245-4255`) bị `find_optimal_window` ghi đè xuống **15/30/30 ngày**;
shadow (`scheduler.py:7356`) dùng thẳng **60 ngày**, không ghi đè. Cộng roster khác hẳn
(**8 token-model vs 11 shadow-model**) và regime prompt khác. Mọi kết luận so hai lane đều mang
confound này.

---

## 2 · Owner yêu cầu gì — NGUYÊN VĂN (`PRJ-INTERACTION-LEDGER-001`)

| giờ (VN) | NGUYÊN VĂN | loại | agent đã làm gì | trạng thái |
|---|---|---|---|---|
| 04/09 23:14 | *«Ok đồng ý khuyến nghị đề xuất, chứ ý ghi nhận đầy đủ thông tin kẻo quên.»* | `XÁC_NHẬN` | Cấp mã canonical `_v11044` → **`QD-073`**; ghi nguyên văn vào **sáu chỗ** | `ĐÃ_LÀM` |
| 04/09 23:1x | **PROMPT 43 R1 · CONTINUATION AFTER V11164 · OWNER-LOCK MATERIALIZATION B · PURE-CONTEXT END-TO-END RECONCILIATION** (I–XXI) | `YÊU_CẦU` | GATE 0 + 14 cổng, hai làn sóng | `ĐÃ_LÀM` |
| 05/09 ~00:0x | *«tới đâu rồi em»* | `HỎI` | Đọc journal thật, báo **0/7 cổng xong, 6 agent đang chạy**, kèm bằng chứng artifact trên VPS | `ĐÃ_LÀM` |

**Ràng buộc owner khoá, nguyên văn, giữ nguyên suốt phiên:**
*«Không mở: Prompt 44; FU mới; Plan mới; work package materialization mới.»* ·
*«Không tự đặt mã quyết định bằng phỏng đoán.»* ·
*«CONDITION ≠ RECOMMENDATION.»* ·
*«Không được tự nâng thành DEPLOYED / RUNTIME_PROVEN / OFFICIAL_CLEAN /
PREDICTIVE_IMPROVEMENT_PROVEN.»* ·
*«Nếu một claim không có raw evidence: ghi NOT PROVEN hoặc INDETERMINATE.»*

---

## 3 · Đào bới / phát hiện

### 3.1 · GATE 0 — và nó bắt được lỗi của chính agent

**Phép thử chặn hai chiều TRƯỢT 1/5 ở lần đầu.** `chmod 444` **không chặn được root** — `CREATE
TABLE` lọt qua và bản clone «bất biến» đã bị bẩn ngay bởi chính phép thử.

Dựng lại bằng `chattr +i`, thử lại **7/7 ĐẠT**:

| phép | mong | thực |
|---|---|---|
| SELECT hợp lệ | QUA | ✅ QUA (n=14.201) |
| INSERT qua `mode=ro` | CHẶN | ✅ `OperationalError` |
| CREATE dưới **root** | CHẶN | ✅ chặn |
| UPDATE dưới **root** | CHẶN | ✅ chặn |
| ghi byte thô dưới **root** | CHẶN | ✅ `PermissionError` |
| ghi ngoài `artifacts/` | CHẶN | ✅ bẫy chặn |
| ghi trong `artifacts/` | QUA | ✅ QUA |

```
GATE0_SHA256  = 8691651275c59b504300f165ba9cd3933be64f7a84ff31336529a4ca54a64924
GATE0B_SHA256 = 835bfd317b245c76087f5e661d724424fdd863d1d0d2ff43cd00ff6c9f73747a
INDEX_SHA256  = 12a115d9119938c22d35566e870506af87a629fe4c3eac47e3927d51df8d6f75
clone         = /root/.../v11165_immutable.db · sha c3c2f568…b6e2 · ----i---------e-------
```

### 3.2 · Mutation ledger — năm loại tách riêng

| # | loại | phiên này | bằng chứng |
|---|---|---|---|
| ① | production DB row mutation | **0** | mọi kết nối `mode=ro`; `neo558` trước = sau |
| ② | production code deploy | **0** | 6/6 hash tệp đang serve **không đổi** (`gpt_analyzer 758c29c1…`, `main 4ed5fd7e…`) |
| ③ | service restart | **0** | PID `3370750` · `NRestarts 0` · start `01:08:40` không đổi |
| ④ | local clone write | **0 ghi vào clone** | `chattr +i`; sha256 clone trước = sau |
| ⑤ | report / Git write | **CÓ** | docs quản trị + 283 artifact + repo công khai |

**Ở phiên này câu «production 0 mutation» là ĐÚNG** — không có deploy, không có restart. (Khác
V11164, nơi câu đó **sai** vì ngày đó có 3 deploy + 1 restart.)

### 3.3 · An toàn trước khi gọi hàm sinh prompt — CHỨNG MINH, không phải niềm tin

Đồ thị gọi AST từ ba điểm vào → **19 hàm** trong `gpt_analyzer.py` + **23 hàm** ngoài module.
Quét đủ bốn lớp (SQL ghi · `.commit()` · `open(w/a/x/+)` · mạng) đều **0**. **36 lệnh
`cursor.execute`**: 34 SELECT/PRAGMA, **0 ghi**, 2 «không rõ» mở ra đọc đều là SELECT.

⇒ **KHÔNG** phải ghi `BLOCKED_BY_SIDE_EFFECT_UNCERTAINTY`. Nhưng vẫn chạy trên clone bất biến với
**ba lớp chặn** (chuyển hướng `connect` · guard SQL · `mode=ro`), vì chứng minh tĩnh không thay
được bẫy mutation. Phép quan trọng nhất: **tắt guard rồi thử INSERT vẫn bị chặn** bởi `mode=ro` —
chứng minh có lớp thứ hai độc lập. **3.331 lần** module thật đòi mở `data/lottery_ai.db` đều bị
bẻ hướng sang clone.

### 3.4 · Prompt thật 100% — `CURRENT_FULL_PROMPT_MANIFEST`

**Bám được 222 payload:** 57 đường scheduler (**= 100% mẫu số thật** lấy từ `predictions` 30 ngày)
· **54 đường combo-super — chưa phép đo nào trước đây chạm tới** · 111 biến thể retry (105 tới được).

| | MN | MT | MB |
|---|---|---|---|
| official (`LEGACY_PROMPT`) | 50.464 | 51.487 | 55.178 |
| «ngữ cảnh thuần» (`CONTEXT_ONLY_V2`) | **53.877** | **54.571** | **58.124** |

⚠️ Lane «thuần ngữ cảnh» **DÀI HƠN** official ~3.400 ký tự — nó gỡ 3 khối và **thêm 4 khối**.

**Chưa phủ, nói thẳng:** số token **INDETERMINATE** (VPS không có tokenizer, cấm gọi provider;
**từ chối** ước lượng bằng hệ số mượn — RM-21) · ba đường `main.py:8769`, `ensemble_voting.py:192`,
`advanced_modes.py:286` **NOT DUMPED** (0 dòng trong 30 ngày) · 105 biến thể retry là
**`CODE_REPRODUCED`, không phải `RUNTIME_PROVEN`**.

### 3.5 · Thước đang dùng là thước hỏng — sửa thước trước khi đo lại bất cứ gì

| thước | tình trạng |
|---|---|
| vân tay `runtime_prompt_sha256` | phủ **39,81–48,07%** (tb 43,59%), thiếu **26.478–35.315** ký tự/lượt, bắt **2/11** phép đột biến. Vá ứng viên bắt **11/11** |
| bộ 5 dấu ô nhiễm (`:6712`) | **MÙ CẤU TRÚC** — báo «0/5 sạch» trong khi payload thật còn `weight=` (33/33), `Best MB model` (11/33), `AI token models 14d WR` (11/33). Dấu meta thật: **12 (MN) · 11 (MT) · 14 (MB)** |
| `_V10768_HERD_SECTION_KEYS` (`:4598`) | 4 chuỗi, khớp theo header `### ` — **bỏ sót `### 🔴 MB HARD MODE`**. Đây là lần **THỨ HAI** cùng họ lỗi (V11106 đã vá ca `MB MODEL RANKING`) ⇒ **RM tái phạm, phải dựng cổng máy** |
| `_v11160_test_lane.py` | **MÙ với nửa `ctx_pack`** — 0 lần nhắc `build_context_pack` / `shadow_mode` / `ctx_pack`, tức mù đúng chỗ nó nhận trách nhiệm canh |

### 3.6 · `SET_TO_CONDITION_LEDGER` — 35 producer

| disposition | n |
|---|---|
| `TRANSLATE_TO_NEUTRAL_CONDITION` | 10 |
| `DROP_MODEL_META` | 6 |
| `DROP_UNSUPPORTED` | 5 |
| `DROP_DUPLICATE` | 4 |
| `RENDER_FULL_UNIVERSE_SYMMETRICALLY` | 3 |
| `KEEP_RAW_FACT` | 2 |
| `BLOCK_AMBIGUOUS` | 2 |
| `BLOCK_ORACLE` | 1 |
| `EXPOSE_VIA_REAL_QUERY_TOOL` | 1 |
| `SHADOW_HYPOTHESIS_ONLY` | 1 |

⇒ **17 producer sinh 17 điều kiện · 18 bị DROP/BLOCK.**

**Bốn chỗ cấm tái sinh dưới bất kỳ dạng điều kiện nào:**

- **P07 `ĐỀ XUẤT PYTHON` — `BLOCK_ORACLE`, nặng nhất.** Prompt đưa thẳng **ĐÁP ÁN đúng dạng hợp
  đồng đầu ra** (`main + secondary` kèm score) rồi **hai mệnh lệnh** ép model ưu tiên nó
  (`SYSTEM_PROMPT §5b gpt_analyzer.py:337-341` và `metrics_calculator.py:635`). Đây là
  **RECOMMENDATION, không phải CONDITION** — vi phạm trực tiếp nhất mục tiêu owner **#3 và #8**.
  Có mặt **57/57 lượt**, kể cả làn «ngữ cảnh thuần».
- **RULEBOOK §11** (`gpt_analyzer.py:639`) *«KHÔNG tự tạo số mới nếu Rule Tails đã có gợi ý mạnh»*
  — **một câu này đóng cửa mục tiêu owner số 2**. Có mặt 57/57.
- **P18/P19 KNOWLEDGE BASE — `BLOCK_AMBIGUOUS`.** `_knowledge_base.json` đóng băng từ
  **2026-04-26**, **vẫn được ĐỌC mỗi lượt**, và **mâu thuẫn với khối sống trong CÙNG một prompt**.
  Đây là **RM-20 ngược lại**: không phải bảng chết, mà là **nguồn chết vẫn được đọc** — nguy hiểm hơn.
- **6 producer `DROP_MODEL_META`** — P10 và P35 hiện **CÓ MẶT ở cả lane «ngữ cảnh thuần»**.

### 3.7 · `CONDITION_CONTRACT` — 24 trường, 17 điều kiện, và nền đo lại

**Nền T1 (bạch thủ) W180:** MN **0,4298** · MT **0,3509** · MB **0,2374** — lệch **gần gấp đôi**
giữa MN và MB. Nền T2 (bộ k đuôi) đối chiếu cả nền đo thật lẫn `1−(1−b)^k` (|lệch| ≤ 0,9pp ⇒
RM-18 dùng công thức được, **miễn dùng `b` đúng miền**). k thật của luật: MN 3,96 · MT 3,70 · MB 2,52.

**Ba con số quyết định:**

| prompt in | nền đúng |
|---|---|
| MN `6W(42d): 265/288 = 92%` | **84,4%** |
| MB `65%` | **47,3%** |
| 12 dòng `6/6 = 100.0%` in như bằng chứng mạnh nhất | MN quan sát 32 ô đạt 100%, **kỳ vọng dưới nền 25,0** · MB quan sát 4, kỳ vọng 3,55 |

Câu *«12 tuần trúng 12/12»* lặp 4 lần trong một khối: **kỳ vọng 12,6/105 luật** đạt được **hoàn
toàn do may rủi** ở MN.

🔴 **`0/17` điều kiện đạt `PROSPECTIVE_SUPPORTED`.** Phân bố: `RAW_FACT` 2 · `MECHANICALLY_DERIVED`
3 · `RETROSPECTIVE_ONLY` 6 · `HYPOTHESIS_ONLY` 5 · `UNAVAILABLE` 1.
⇒ **Dưới hợp đồng đề xuất, model chỉ được rút số từ 5/17 điều kiện.**

### 3.8 · Mapping 14 nhóm khối lịch sử

| nhóm | kết quả |
|---|---|
| **P07 ĐỀ XUẤT PYTHON** | `BLOCK_ORACLE` — 57/57 lượt, cả làn thuần |
| **Phase 19 «TRÍ TUỆ TỰ HỌC»** | 🔴 **KHÔNG có cổng nào** — `weight=` sống sót **933 lần**, câu *«→ Ưu tiên yếu tố có WR cao nhất»* **57/57**. V11150 gỡ Phase 14A rồi **để mở cửa bên cạnh** = `A58_VIOLATION_HALF_DONE` |
| **EVIDENCE TABLE** | xếp hạng **988/988 dòng có n<10**; số dòng «100%» **không vượt kỳ vọng do nền** (nền 92,01/84,66/65,10%; kỳ vọng 31,0/19,9/5,6 bucket vs bảng in 10/10/4) ⇒ **xếp hạng không mang thông tin** |
| **CONVERGENCE** | **76/76 dòng khai «3 rules» thật ra là MỘT miền nguồn** và có **một giải chung** ở cả ba luật ⇒ hội tụ là **đếm một tiếng nói ba lần** |
| **GAN/HOT/COLD** | V11001/V11007 chỉ gỡ phía `gpt_analyzer`; **ba module ngoài vẫn bơm mọi lượt** |
| **Ký hiệu thủ công** `G4#3` `FIRST2` `HEAD_TAIL` `TAIL_HEAD` `LAST2` `D-3` | **0/19 lượt có định nghĩa** — model phải tự đoán |
| **Phase 15** (lịch sử của chính model) | **KHÔNG có mốc cutoff trong SQL** — 57/57 dump có dòng **đúng ngày dự đoán** |
| **OWNER ANTI-TRAP** | thang `FRESH > PARTIAL_SPENT > FULL_SPENT` là **KHUYẾN NGHỊ**, không phải điều kiện; nhãn `COLD/OVER_HOT` của P07 được **ngẫu nhiên thuần sinh ra** ở quy mô 22,4 và 18,8 đuôi/ngày |
| **Nhóm 1 (D-1 tail pool)** | ✅ **tiền đề đã CŨ** — `sorted(...)[:12]` **không còn** trong mã đang serve (V11105/V11106 đã vá) |
| **Nhóm 12 (lịch sử đài)** | ✅ khối **sạch nhất**, giữ, chỉ sửa hai chỗ nhỏ |

**Sửa đủ 14 nhóm gỡ 7.757–8.289 ký tự/lượt official (14,8–15,5%)** và 6.491–7.068 ký tự/lượt
shadow (11,8–12,3%).

### 3.9 · `PURE_CONTEXT_RENDERER` + `CONTAMINATION_GATE_V2` + test suite

**Renderer** (`artifacts/v11165_k9_renderer.py`) tách làm hai nửa: `thu_thap()` chạm DB (đọc-only,
mọi truy vấn có chặn as-of) và `render()` là **HÀM THUẦN** — không DB, không đồng hồ, không biến
môi trường.

| | candidate | official cùng ngày |
|---|---|---|
| payload MN | **18.682** ký tự | 50.464 |
| preselected basket | **không** | có |
| rank / boost / model-meta | **không** | có |
| bảng full-universe 00→99 | **có**, thứ tự cố định, chỉ có/không | — |
| nền cho mỗi CONDITION | `1−(1−b)^k` với **`b` đo lại cho chính miền × thứ** | 1/35 producer |

**`CONTAMINATION_GATE_V2`** đo trên **DUMP THẬT**, phân loại từng lần khớp
(`KHANG_DINH / PHU_DINH / DINH_NGHIA_HOP_DONG / SU_KIEN_GOC`) thay vì đếm chuỗi. Hiệu chuẩn hai chiều:

| | kết quả |
|---|---|
| candidate 3/3 miền | ✅ **ĐẠT**, ô nhiễm = **0** |
| **57/57 payload official + shadow THẬT** | 🔴 **TRƯỢT**, trung bình **220 điểm ô nhiễm** mỗi bản, dính đủ **9 nhóm** detector |

**Test suite A…I: 68 phép CHẠY · 68 ĐẠT · 0 TRƯỢT · 2 KHÔNG_CHẠY_ĐƯỢC** (ghi thẳng, không tính
là đạt). Nhóm E (negative tests) **làm cổng ĐỎ 6/6** lần cài vi phạm.

### 3.10 · Kế toán MT + lineage/consensus

**MT:** gốc lỗi `main.py:9840` đo **cap cố ý** và **trượt gate** vào **chung một tập**
`filtered_models` ⇒ `main.py:10511` xuất `wr_gate_filtered` chứa chính hai model mà
`gate_diagnostics` ghi `pass=true` — **tự mâu thuẫn trên 70/70 ngày có cap**.

🔴 **Hậu quả nặng nhất vừa đo được: rolling WR/TOP1 của MT đang TRỄ 71 NGÀY** — thước gọi là
«7 lượt gần nhất» tại 04/09 thực ra tính trên các lượt **19/06–25/06**.

Sửa kế toán xong thì **số của MT XẤU ĐI rõ ràng**: `wr7 14,3% → 0,0%` · `wr14 14,3% → 0,0%` ·
`wrALL 15,1% → 10,9%` · `top1_7 57,1% → 28,6%` · `top1_14 57,1% → 21,4%`.
Patch qua **30/30 test**, replay offline 566 dòng đổi **đúng 45 dòng**, cả 45 đều là MT, MN/MB **0 dòng**.

**Lineage:** `consensus_level` đếm voter **THÔ** ⇒ **268/567 bundle (47,3%)** mang nhãn **cao hơn
sự thật**, **200 bundle tụt thẳng `strong → weak`**; nguồn độc lập trung bình **3,07** chứ không
phải 5,32 voter. **Nhãn sai này ra tới người dùng**: `du-doan.html:1413` → *«Rất mạnh / Đồng thuận cao»*.

`combo-super` gọi lại model **KHÔNG phải defect** — đo thật: lần gọi lại cho kết quả **KHÁC 86,8%**
(AI) và **42,0%** (ML) ⇒ đúng là **lượt lấy mẫu mới**.

### 3.11 · Sổ xung đột hợp đồng — **năm** xung đột, không phải ba

| mã | xung đột |
|---|---|
| `XD-01` | **«Quyền SKIP» là mệnh lệnh trỏ vào một khả năng KHÔNG TỒN TẠI** — cùng họ với việc bảo model «tự truy vấn» khi không có tool |
| `XD-02` | Owner-lock V11150 «N≥1 không được thành `NO_OUTPUT`» và việc UCC **tự suy `NO_OUTPUT` ở tầng NGUỒN** là **hai tầng bị gọi cùng tên** |
| `XD-03` | 🔴 **`CAP5_INPUT_NOT_READY` là ÂM TÍNH GIẢ của bộ đọc** — `near_miss_shortlist` **có thật** trong `reasoning_json` (1.371 dòng, 3.774 phần tử); hợp nhất với `main_numbers` đạt **đúng 5 số ở 610 dòng**. Bộ đọc tra **nhầm cột** (`analysis_text`) và danh sách 9 tên khoá **không có** `near_miss_shortlist` |
| `XD-04` | `verdict.decision` là từ vựng **MỞ (37 giá trị)** nhưng bộ hiển thị coi mọi thứ ≠ `CHOT_HA` là SKIP |
| `XD-05` | `secondary_number` bị **BA luật và BA TÊN** khác nhau điều khiển trong cùng một prompt |

Đề xuất **một** contract duy nhất: `PURE-CONTEXT-OUTPUT-1.0.0-DRAFT`, phương án **PA-3** «tách
KIÊNG NHƯỜNG khỏi CHẶN SỐ».

⚠️ **`UCC` KHÔNG có định nghĩa nào trong kho** — 12 tệp khớp chỉ vì là chuỗi con của `SUCCESS`.
Ghi `INDETERMINATE`, cần owner chỉ rõ. *(RM-10: suýt kết luận theo tên đoán.)*

---

## 4 · Hướng xử lý và vì sao chọn

### 4.1 · `PURE_CONTEXT_CANDIDATE = BLOCKED_WITH_EXACT_REASONS`

**NHÓM A — ba blocker ĐÃ CÓ VÁ, chỉ chờ owner ký deploy:**

| mã | blocker | vá |
|---|---|---|
| `SC-02` | hash coverage 43,59% < 100% | **VA-B** — vân tay → 100%, bắt 11/11 đột biến |
| `SC-07` | routing vẫn phụ thuộc `selected_model` (`gpt_analyzer.py:6738`) | **VA-A** — bịt rò gói ngữ cảnh, thử chặn hai chiều |
| `SC-12` | MT cap vẫn bị tính là gate failure (`main.py:9840`) | **VA-h12** — 30/30 test, replay 45 dòng |

**NHÓM B — ba blocker là BẢN CHẤT của prompt production, không vá nào trong gói này gỡ được:**

| mã | blocker |
|---|---|
| `SC-04` | candidate vẫn có preselected basket — lane `CONTEXT_ONLY_V2` **đang chạy** còn 5 dấu rổ-chọn-sẵn mỗi miền (official 6) |
| `SC-05` | condition không truy được về raw source/cutoff — **1/35** producer có nền tường minh |
| `SC-08` | model bị yêu cầu làm việc **không có phương tiện để làm** — mệnh lệnh quét 8 cửa sổ, nhưng **7W/8W có 0 dòng số liệu ở cả 6 dump**, và **không model nào bật tool-calling** |

**Cộng 1 `INDETERMINATE`:** `SC-10` — `UCC` không có định nghĩa.

**Chặn nền tảng đứng trên tất cả:** `MT_PREREGISTRATION = NOT_READY_FOR_OWNER_LOCK` và
`POOL_VERDICT = HOLD`. **Kể cả gỡ hết 6 blocker kỹ thuật, phép đo vẫn chưa được phép kết luận** vì
chưa có ngưỡng nào được đăng ký trước.

### 4.2 · MT measurement artifact — đúng phương án B owner đã khoá

Không dùng cột · không `ALTER` schema · không materialize · không sửa writer · không mở C.

Artifact **ngoài DB, append-only**, đã **chạy thật trên 90 ngày MT**: **2.635 dòng · 2,45 MB ·
`chmod 0444` · 13/13 kiểm độc lập + 15/15 tự kiểm ĐẠT**. Full ranking, không cắt cụt top-10;
không dùng trường `hang_cua_no_trong_A`; sinh **trước** kết quả; **không tự chạy cron** trước khi
`MT_PREREGISTRATION` được owner khoá.

### 4.3 · 🔴 RÚT LẠI — `PRJ-RETRACTION-001`

#### R14 — «ít nhất 46/72 quy trực tiếp cho kế toán cap» (V11164)

- **Chỗ gốc:** `REPORT_V11164.md` §1 và §3.10 · `CONVERSATION_CONTEXT_V11164` · `CHANGELOG` V11164
  · `FOLLOW_UP_TRACKER` · commit công khai `af4597a`
- **Nguyên văn câu sai:** *«ít nhất 46/72 giải thích hoàn toàn bởi trần V10752»*
- **Điều đúng:** **KHÔNG TÁI LẬP ĐƯỢC.** Dẫn xuất không được ghi ở bất kỳ tệp evidence nào ⇒
  **RM-11**. Số đúng đo lại trên clone bất biến: **45 ngày** cap giải thích trọn vẹn (hoặc **70
  ngày** có cap tham gia). Phép đo: `artifacts/v11165_h12_mt_accounting.json`.
- **Quyết định đã dựa trên:** kết luận `MT_PREREGISTRATION = NOT_READY_FOR_OWNER_LOCK`.
  **Kết luận GIỮ NGUYÊN** — và nay còn mạnh hơn (rolling WR trễ 71 ngày) — nhưng con số phải đúng.

#### R15 — «71 ngày liên tiếp» thiếu định nghĩa (V11164)

- **Chỗ gốc:** như trên
- **Nguyên văn câu sai:** *«MT bị loại khỏi đo lường chính 71 ngày liên tiếp»*
- **Điều đúng:** **71 tái lập được, NHƯNG chỉ với định nghĩa `evaluation_policy != 'INCLUDE'`**
  (26/06 → 04/09, phá ở 25/06). Đọc theo đúng chữ `EXCLUDE_PRIMARY` thì chuỗi liên tiếp thật chỉ
  **7 NGÀY** (29/08 → 04/09). **CẤM viết «MT bị `EXCLUDE_PRIMARY` 71 ngày liên tiếp».**
  Thêm: trong 71 ngày đó **65 mang dấu hiệu cap** và **6 KHÔNG phải cap** — riêng **2026-08-28**
  là **hỏng CHẠY thật** (0 dòng `ai_chain`), nên câu *«vì một lỗi KẾ TOÁN»* **không đúng cho cả 71 ngày**.

#### R16 — «z = −0,10 · p = 1,00» trộn hai phép McNemar khác nhau (làn sóng 1 của chính phiên này)

- **Chỗ gốc:** báo cáo tiến độ giữa phiên gửi owner (05/09 ~00:xx, trong IDE)
- **Điều đúng:** con số tái lập được là **z = −0,0995** với b=51 · c=50 · m=101; giá trị `p` đi kèm
  phải nêu rõ là **hai phía trên phân phối chuẩn xấp xỉ**, không phải phép McNemar chính xác.
  Verdict `NO_ANOMALY_FOUND` **không đổi**, nhưng cách trình bày đã trộn hai phép.

---

## 5 · Đã làm gì

| việc | TRƯỚC | SAU |
|---|---|---|
| Owner-lock B | chưa ghi | **`QD-073`** vào **sáu chỗ** (sổ quyết định · SSOT · tracker · CHANGELOG · STATE/HISTORY · sổ tương tác) |
| lớp bằng chứng V11164 | 8 tệp raw không nhãn | **`EVIDENCE_STATUS_V11164`** — 8 tệp dán `RAW_PRE_REVIEW_ARTIFACT`, **13 mục claim correction**, nội dung **không sửa một byte** |
| di sản prompt | rải rác | **`PROMPT_KNOWLEDGE_COVERAGE_MATRIX`** 35 dòng × 10 cột · `AGENT_IDE_KNOWLEDGE_COVERAGE = PARTIAL` |
| payload cuối | chưa ai dựng đủ | **222 payload**, 100% đường scheduler, + 54 đường combo-super chưa ai chạm |
| bộ số tổng hợp | chưa kiểm kê | **35 producer × 32 trường**, 10 disposition |
| hợp đồng điều kiện | không có | **`CONDITION_CONTRACT`** 24 trường · 17 điều kiện · nền đo lại từng miền |
| spec ba tầng | không có | **`PURE_CONTEXT_THREE_LAYER_SPEC`** + **`CONTRACT_CONFLICT_LEDGER`** 5 xung đột |
| renderer | không có | **`v11165_k9_renderer.py`** — 18.682 ký tự, 0 basket, 0 rank, 0 model-meta |
| cổng ô nhiễm | 5 dấu, mù | **`CONTAMINATION_GATE_V2`** — candidate 3/3 ĐẠT, **57/57 payload thật TRƯỢT** |
| test suite | không có | **68 phép, 68 đạt**, negative test **6/6 làm cổng đỏ** |
| bộ đo lập luận | không có | 13 thước + **6 phép metamorphic**, tự kiểm **31/31** |
| đăng ký trước | ngưỡng cũ chưa hoà giải | **`PROSPECTIVE_MEASUREMENT_PREREG_DRAFT`** — hoà giải 5 bộ ngưỡng, `PROVISIONAL_AGENT_PROPOSED_DRAFT` |
| gói deploy | không có | **`DEPLOY_AND_ROLLBACK_PACKET`** — 8 hạng mục, mỗi cái có gỡ về chính xác |
| MT artifact (B) | không có | chạy thật 90 ngày: **2.635 dòng**, 13/13 + 15/15 kiểm ĐẠT |
| production | — | **0 ghi · 0 deploy · 0 restart** |

---

## 6 · Cổng kiểm — xác minh

| cổng | kết quả |
|---|---|
| thử chặn hai chiều GATE 0 | **7/7 ĐẠT** (sau khi bắt và sửa lỗi `chmod` không chặn root) |
| sandbox quanh hàm sinh prompt | **6/6 ĐẠT**, trong đó **tắt guard vẫn bị `mode=ro` chặn** |
| `neo558` trước/sau toàn phiên | **KHỚP TỪNG KÝ TỰ** |
| 6 hash tệp đang serve | **không đổi** |
| clone bất biến | `----i---------e-------`, sha256 trước = sau |
| PID · NRestarts · health | `3370750` · `0` · `200` — không đổi |
| `output_counterfactual_rank` | **`0/17.121`** — bằng chứng B đang được thi hành |
| test suite A…I | **68/68 đạt**, 2 không chạy được (ghi rõ) |
| negative test | **6/6 làm cổng đỏ** |
| hiệu chuẩn `CONTAMINATION_GATE_V2` | candidate 3/3 ĐẠT · **57/57 payload thật TRƯỢT** |
| tự kiểm bộ đo + metamorphic | **31/31 đạt** |
| MT patch | **30/30 test** · replay đổi đúng 45 dòng |
| MT artifact | **13/13 + 15/15 đạt** |
| phản biện độc lập | **56/56 chạy** · 10 `DUNG` · 46 `DUNG_MOT_PHAN` · **0 `SAI`** |

---

## 7 · Vướng vấp — lỗi tự gây, bài học

| # | vấp | gỡ |
|---|---|---|
| 1 | 🔴 **`chmod 444` không chặn root** — clone «bất biến» vẫn ghi được, và phép thử đã tạo bảng lạ trong đó | dựng lại sạch + `chattr +i`, thử lại 7/7. **Nếu không thử hai chiều thì cả phiên dựng trên một bản bất biến giả** |
| 2 | **Bản nháp patch B gọi hai ký hiệu KHÔNG TỒN TẠI** trong mã đang serve — deploy sẽ **mất sạch vân tay**, tệ hơn hiện trạng | sửa để suy route từ **năm cờ boolean có thật** |
| 3 | **Bản r1 của MT artifact lặp lại đúng bẫy NULL-hai-nghĩa mà nó tuyên bố sửa** (`prompt_version` rỗng 50,4% không kèm lý do) | bắt và vá ở r2 |
| 4 | **`CONTAMINATION_GATE_V2` bản đầu có ba lớp dương tính giả** — cùng họ lỗi với bộ 5 dấu mù, **chỉ ngược chiều** | phân loại từng lần khớp thay vì đếm chuỗi |
| 5 | **Bản ứng viên renderer lấy nhầm bucket luật** do kho có **hai quy ước thứ ngược nhau** ⇒ toàn bộ tầng điều kiện ra rỗng **mà không báo lỗi** | bộ thử bắt được; production **không** dính lỗi này (có bằng chứng mã nguồn) |
| 6 | **Gate 5 và Gate 6 suýt dựng HAI khuôn `CONDITION` khác nhau** (24 trường vs 12 trường) | Gate 6 tự rút khuôn 12 trường, trỏ sang Gate 5 — tránh `§60` chồng tầng |
| 7 | **Bộ đo lập luận bản V1 đếm chuỗi thô** → 59 mâu thuẫn giả + 15 lỗi số học giả | tự rút lại, viết lại theo phân loại |
| 8 | **Phép đo SC-08 đầu tiên kết luận sai** do regex bỏ sót cách viết `2W(14d)` | kiểm lại bằng 8 cách viết; kết luận CHẶN vẫn đứng nhưng **lý do khác hẳn** |
| 9 | **Hai con số tự suy ra SAI** ở Gate 5 (`P(≥6/8)=0,98` → đúng **0,8845**; nền k=4 trộn nhầm cột) | tính lại, buộc mọi giá trị lấy thẳng từ JSON đo được |
| 10 | Backtick trong template literal JS làm hỏng workflow (**lần thứ hai**) | thay bằng nháy đơn — cần nhớ dài hạn |

---

## 8 · Gỡ về — rollback

**Không áp dụng cho phiên này:** 0 ghi production · 0 deploy · 0 restart · 0 sửa tệp đang serve.

**`DEPLOY_AND_ROLLBACK_PACKET.md`** có gỡ về chính xác cho **8 hạng mục** khi owner duyệt, kèm thứ
tự deploy, cách kiểm sau deploy, điều kiện dừng, và **ghi rõ patch nào độc lập / patch nào phụ thuộc**.

Artifact và clone nằm ngoài đường phục vụ, xoá lúc nào cũng được (`chattr -i` trước khi xoá clone).

---

## 9 · Theo dõi tiếp

| # | việc | ai chặn | trạng thái |
|---|---|---|---|
| 1 | **Ký deploy 3 vá NHÓM A** (VA-A rò ctx · VA-B vân tay · VA-h12 kế toán MT) | **OWNER** | `CHỜ_OWNER` · FU-450 |
| 2 | **Chỉ rõ `UCC` là gì** — không có định nghĩa nào trong kho | **OWNER** | `CHỜ_OWNER` |
| 3 | **Khoá ngưỡng đo tiến** — bản nháp đã hoà giải 5 bộ ngưỡng cũ | **OWNER** | `CHỜ_OWNER` · FU-449 |
| 4 | **P07 `ĐỀ XUẤT PYTHON` + RULEBOOK §11** — hai chỗ đóng cửa mục tiêu owner #2, #3, #8 | chạm prompt official | `CHỜ_OWNER` · FU-450 |
| 5 | **Phase 19 «TRÍ TUỆ TỰ HỌC» chưa có cổng** — `weight=` sống sót 933 lần | chạm prompt | `CHỜ_OWNER` · FU-450 |
| 6 | **Ba module ngoài vẫn bơm gan/hot/cold** (`statistical_analyzer` · `metrics_calculator` · `feature_engineering`) | chạm mã | `CHỜ_OWNER` · FU-450 |
| 7 | **`consensus_level` nhãn sai ra tới người dùng** — 268/567 bundle | chạm `main.py` + UI | `CHỜ_OWNER` · FU-449 |
| 8 | **Phase 15 thiếu chặn as-of trong SQL** — 57/57 dump có dòng đúng ngày dự đoán | chạm mã | `CHỜ_OWNER` · FU-450 |
| 9 | **`XD-03` `CAP5_INPUT_NOT_READY` là âm tính giả** — dữ liệu hạng 3–5 đã tồn tại suốt | có thể đóng ở phiên sau | `ĐANG_LÀM` · FU-449 |
| 10 | **De-herding mù lần thứ HAI** ⇒ theo luật RM phải **dựng cổng máy** | có thể làm ở phiên sau | `ĐANG_LÀM` · FU-450 |
| 11 | **Hai lane dùng cửa sổ thống kê khác nhau** (15/30/30 vs 60) — confound của chính phép so | cần owner quyết chuẩn hoá | `CHỜ_OWNER` · FU-449 |
| 12 | **Hệ không lưu prompt đã gửi** — chỉ lưu sha256 phủ 43,6% | gắn với VA-B | `CHỜ_OWNER` · FU-450 |
| 13 | Nợ báo cáo §57 **40/241**, `V11156` thiếu hẳn | đóng dần, cấm bịa | `ĐANG_LÀM` · FU-449 |

---

## 10 · TRẢ LỜI THẲNG 12 CÂU

**1 · Agent IDE hiện đã đọc/nắm bao nhiêu phần lịch sử chuyển đổi prompt?**
**`AGENT_IDE_KNOWLEDGE_COVERAGE = PARTIAL`. Cấm ghi «đã nắm».** Đã đọc **toàn văn 18 thư mục báo
cáo** (V11014→V11164), kho tài liệu riêng, mã runtime đang serve (10/10 hash khớp GATE 0), 254 bảng
DB, crontab 93 dòng. **Năm nguồn chưa đóng được**, và cả năm đủ nặng để đổi kết luận: ① **Notion**
(§57.1 cấm ghi, đứng im từ 01/08 — mọi tri thức chỉ có trên đó là **chưa đối chiếu**); ② lớp
`create_analysis_prompt` — số ký tự **từng khối** vẫn là **suy ra**, không phải đo; ③ **9 cổng
Wave 1 KHÔNG có trên VPS** nên không chạy lại được; ④ **FU-419**; ⑤ **bản ghi đóng `A1` của V11024**.

**2 · Tài liệu nào còn hiệu lực, tài liệu nào đã bị supersede?**
Ma trận 35 dòng × 10 cột trong `PROMPT_KNOWLEDGE_COVERAGE_MATRIX.md`. Đáng chú ý:
**8 tệp `evidence/GATE_g*.md` của V11164 nay là `RAW_PRE_REVIEW_ARTIFACT · NOT_CANONICAL_IN_ISOLATION`**,
`SUPERSEDED_BY = REPORT_V11164 + PHAN_BIEN_32_SUA_LAI` — và **ba mâu thuẫn còn sống** ngay trong
lớp evidence đó (`g6:35` vs `g7:22`; `g5:5` giữ 88/88 · 50.670; `g4` tự khai «gate6 ·
EVIDENCE_COMPLETE» trong khi REPORT ghi «GATE 6 = PARTIAL»). Một đính chính **có lợi**: `A1` của
V11024 **đã được sửa** (dòng DELETE đã chú thích, bảng giữ 251 ngày) nhưng **không tìm được bản nào
ghi nhận** — tài liệu vẫn treo một blocker đã chết.

**3 · Prompt cuối hiện tại gồm chính xác những phần nào?**
Tám phần theo đúng thứ tự nối của mã đang serve, rồi wrapper của từng provider (**5 tuyến**):
system message · user message · context pack sau mọi filter · `REASONING_RULEBOOK` ·
JSON/output contract · provider wrapper · model-specific additions · retry/fallback additions.
Đo được: MN **50.464** / MT **51.487** / MB **55.178** (official); **53.877 / 54.571 / 58.124**
(context-only — **DÀI HƠN** official). Chi tiết từng section ở `CURRENT_FULL_PROMPT_MANIFEST` +
`PROMPT_SECTION_LEDGER` + `PROMPT_CALL_GRAPH`.

**4 · Bao nhiêu phần trăm final payload được fingerprint thật?**
**39,81–48,07%, trung bình 43,59%** — thiếu **26.478–35.315 ký tự mỗi lượt**. Bắt được **2/11**
phép đột biến. Vá ứng viên **VA-B** nâng lên **100% theo cấu trúc** và bắt **11/11** — đã code,
đã test, **chưa deploy**. Hệ quả nghiêm trọng hơn con số: **prompt đã gửi ngày 04/09 không tái dựng
được**, vân tay khớp **0/60** lượt.

**5 · Có bao nhiêu bộ số tổng hợp vẫn đang được bơm vào?**
**27/35 producer** bơm `AGGREGATED_NUMBER_SET`; chỉ **2** là `RAW_NUMBER_FACT`. Trong prompt MN
official: **27/30 khối mốc có mặt, 25 khối mang số, ~23 là bộ tổng hợp**. Tổng cộng **83/100 đuôi**
được trình như «tín hiệu» dưới **23 nhãn khác nhau** ⇒ **bất kỳ số nào model chọn cũng biện minh được**.

**6 · Mỗi bộ đó đến từ đâu, có baseline và cutoff không?**
Sáu nguồn: `lottery_results` (sự kiện thật) · `source_data` trong bộ nhớ (thật nhưng **bị chấm điểm
và chọn sẵn**) · `mined_rules` · **`predictions` — DỰ ĐOÁN CỦA CHÍNH HỆ** · **tệp tĩnh
`_knowledge_base.json` đóng băng từ 26/04** · **`final_bundles` — OUTPUT CÔNG BỐ của chính hệ**
(chỉ ở lane shadow!).

> ⚠️ **Về `mined_rules` — cố ý KHÔNG tuyên bố hiệu quả ở bản này** (`PRJ-SELECTION-WINDOW-001` ·
> RM-18). Phiên này đo **nền** cho họ điều kiện luật, **không** đo hiệu quả của luật. Vì vậy bản
> này **không** phát biểu con số nào cho **trong cửa sổ chọn**, **ngoài cửa sổ chọn**, **trong
> mẫu** hay **ngoài mẫu** — cả bốn vế đều để trống có chủ ý.
> Bộ đầy đủ bốn vế nằm ở **V11073** (**+9,9% trong mẫu → −1,6% ngoài mẫu**) và **RM-18/V11030**
> (**+7,5 / +13,8 / +20,7 điểm TRONG cửa sổ chọn, ĐÚNG BẰNG 0 ngoài cửa sổ**).
> Đo bổ sung của phiên này, ghi kèm để không ai đọc thiếu: **n = 20/miền trên 4 ngày** ⇒ **RM-04,
> chưa được phép kết luận**; điểm ước lượng âm ở cả ba miền nhưng **KTC95 đều chứa 0** — **cấm
> viết theo cả hai hướng**. Và **2.421/5.035** lượt đánh giá **không tách được** trong/ngoài cửa sổ
> vì `rule_id` không còn trong `mined_rules`, đã để riêng nhãn `KHONG_RO_mined_at`.
**Baseline: 1/35.** Chỉ P21 có cột «lợi thế/nền» và đoạn tự phủ định.
**Cutoff: đúng ở phần lớn; SAI hoặc THIẾU ở** P10 (không có `date < target_date`) · P22 (dùng
`date('now','-2 days')`) · P32/P35 (`date('now')`) · P21/P34 (không có điều kiện thời gian) ·
P18/P19 (tệp tĩnh, không neo ngày nào) · **Phase 15 (không có cutoff trong SQL — 57/57 dump có
dòng đúng ngày dự đoán)**.

**7 · Bộ nào phải giữ raw, bộ nào chuyển condition, bộ nào bỏ?**
**Giữ raw: 2** (`KEEP_RAW_FACT`). **Chuyển thành điều kiện: 10** + **3 render full-universe đối
xứng** + **1 qua tool thật** + **1 shadow-hypothesis** = **17 producer → 17 điều kiện**.
**Bỏ/chặn: 18** (6 `DROP_MODEL_META` · 5 `DROP_UNSUPPORTED` · 4 `DROP_DUPLICATE` ·
2 `BLOCK_AMBIGUOUS` · **1 `BLOCK_ORACLE`**). Bảng đối chiếu đủ 35 dòng ở `CONDITION_CONTRACT.md`.

**8 · Model có tool truy vấn thật hay chỉ được bảo «tự truy vấn» bằng lời?**
🔴 **CHỈ BẰNG LỜI.** Grep 5 mẫu trên toàn `web/backend` = **0 dòng** — **không model nào bật tool
calling**. Vậy mọi mệnh lệnh «hãy tự truy vấn» trong prompt là **không thi hành được**, đúng điều
owner cấm ở mục tiêu **#6**. Cùng họ: `XD-01` «Quyền SKIP» cũng trỏ vào một khả năng **không tồn tại**,
và `SC-08` bảo model quét **8 cửa sổ** trong khi **7W/8W có 0 dòng số liệu** ở cả 6 dump.

**9 · Candidate pure-context có còn top-k/rank/boost/model-meta ẩn không?**
**Bản candidate: KHÔNG** — `CONTAMINATION_GATE_V2` cho candidate **3/3 miền ĐẠT, ô nhiễm = 0**;
payload 18.682 ký tự, bảng full-universe 00→99 thứ tự cố định chỉ có/không, mỗi CONDITION có nền
`1−(1−b)^k` với `b` đo lại cho chính miền × thứ.
**Bản ĐANG CHẠY: CÒN RẤT NHIỀU** — **57/57 payload thật TRƯỢT**, trung bình **220 điểm ô nhiễm**,
dính đủ **9 nhóm** detector. Lane `CONTEXT_ONLY_V2` còn **5 dấu rổ-chọn-sẵn mỗi miền**.

**10 · Cùng facts, model có suy luận ổn định và dẫn đúng `condition_id` không?**
**KHÔNG ĐO ĐƯỢC — và lý do quan trọng hơn câu trả lời.** ① **Prompt hiện tại không đánh số điều
kiện nào**, nên đường suy luận của model **không kiểm được** (M02). ② **Prompt đã phục vụ 04/09
không tái dựng được** ⇒ mọi thước cần đối chiếu prompt có sẵn **một lỗi không khử được**.
③ **MR5: 117 tỉ lệ trong prompt chỉ có 14 (11,97%) kèm nền tường minh** ⇒ phép «đổi nền» **vô nghĩa**
với 88% còn lại. ④ **MR3: đổi TOÀN BỘ số nguồn bằng một song ánh, chỉ 3/27 khối mang số biến đổi
theo** ⇒ có **hidden anchor**. ⑤ **MR1: một đại lượng thống kê trong prompt là sản phẩm của THỨ TỰ
LIỆT KÊ đài**, không phải của dữ liệu. Renderer candidate **có** `condition_id` nên thước này sẽ
chạy được **sau khi** owner duyệt shadow deploy.

**11 · MT accounting và measurement artifact đã sẵn sàng để Owner-lock chưa?**
**Patch: SẴN SÀNG ĐỂ KÝ DEPLOY** — 30/30 test, replay đổi đúng 45 dòng, MN/MB 0 dòng, có gỡ về.
**Artifact: ĐÃ CHẠY THẬT** — 2.635 dòng / 90 ngày, 13/13 + 15/15 kiểm đạt, đúng phương án B.
**Preregistration: CHƯA — `NOT_READY_FOR_OWNER_LOCK`.** Ba lý do: ① ngưỡng `n=96` cũ chỉ **50% sức
mạnh** (thiếu `z_β`), đúng phải **194 cặp**; ② thước của chính miền MT đang **trễ 71 ngày**; ③ nhánh
CONTROL **chưa phải official thuần** vì `gpt_analyzer.py:6738` còn sống.

**12 · Candidate đã `READY_FOR_OWNER_SHADOW_DEPLOY` hay còn blocker gì?**
## `BLOCKED_WITH_EXACT_REASONS` — 6 blocker + 1 indeterminate.
Ba blocker **đã có vá chờ ký** (`SC-02` · `SC-07` · `SC-12`); ba blocker là **bản chất prompt
production**, cần renderer + đăng ký trước (`SC-04` · `SC-05` · `SC-08`); một `INDETERMINATE`
(`SC-10` — `UCC` không có định nghĩa). **Trên tất cả: `MT_PREREGISTRATION = NOT_READY_FOR_OWNER_LOCK`
và `POOL_VERDICT = HOLD`.**

---

## 11 · Deliverables *(24 mục owner yêu cầu)*

| # | mục | trạng thái |
|---|---|---|
| 1 | `OWNER_DECISION_B_RECORD` | ✅ **`QD-073`** trong `docs/OWNER_DECISION_LEDGER.json` |
| 2 | `EVIDENCE_STATUS_V11164` `.md`/`.json` | ✅ `V11164_.../EVIDENCE_STATUS_V11164.*` |
| 3 | `PROMPT_KNOWLEDGE_COVERAGE_MATRIX` | ✅ 30.235 B |
| 4 | `CURRENT_FULL_PROMPT_MANIFEST` | ✅ `artifacts/v11165_h3_manifest.json` |
| 5 | `PROMPT_CALL_GRAPH` | ✅ `artifacts/v11165_h3_callgraph.json` |
| 6 | `PROMPT_SECTION_LEDGER` | ✅ `artifacts/v11165_h3_section_ledger.json` |
| 7 | `SET_TO_CONDITION_LEDGER` | ✅ `artifacts/v11165_h4_set_to_condition.json` |
| 8 | `CONDITION_CONTRACT` | ✅ 51.197 B |
| 9 | `CONTRACT_CONFLICT_LEDGER` | ✅ 20.902 B — **5** xung đột |
| 10 | `PURE_CONTEXT_THREE_LAYER_SPEC` | ✅ 20.840 B |
| 11 | `CONTROL_VS_CANDIDATE_DIFF` | ✅ trong `v11165_k9_ketqua.json` |
| 12 | `MODEL_PROMPT_COMPATIBILITY_MATRIX` | ✅ 40.522 B — 19 LLM |
| 13 | `FULL_PAYLOAD_FINGERPRINT_SPEC` | ✅ trong `v11165_h3_full_prompt.json` + patch VA-B |
| 14 | `CONTAMINATION_GATE_V2` | ✅ `evidence/v11165_k9_contam_v2.py` |
| 15 | `PURE_CONTEXT_RENDERER` candidate | ✅ `evidence/v11165_k9_renderer.py` |
| 16 | UCC/output adapter candidate | 🟡 **`INDETERMINATE`** — `UCC` không có định nghĩa trong kho |
| 17 | Test suite + negative tests | ✅ `evidence/v11165_k9_tests.py` — 68/68, negative 6/6 |
| 18 | `MT_ACCOUNTING_LOCAL_PATCH` + offline impact | ✅ `evidence/v11165_h12_patch.py` |
| 19 | `LINEAGE_CONSENSUS_LOCAL_PATCH`/comparator | ✅ `artifacts/v11165_h13_*.json` |
| 20 | `PROSPECTIVE_MEASUREMENT_PREREG_DRAFT` | ✅ 37.235 B |
| 21 | `DEPLOY_AND_ROLLBACK_PACKET` | ✅ 29.048 B — 8 hạng mục |
| 22 | Integrated public-safe REPORT | ✅ **bản này** |
| 23 | `CONVERSATION_CONTEXT` | ✅ cùng thư mục |
| 24 | Exact private/public commits | ✅ mục 13 |

---

## 12 · Nguồn ba lớp mở rộng (§62)

### `OWNER_SAID`
- 04/09 23:14 — *«Ok đồng ý khuyến nghị đề xuất, chứ ý ghi nhận đầy đủ thông tin kẻo quên.»*
- 04/09 23:1x — *«Không tự đặt mã quyết định bằng phỏng đoán.»* · *«CONDITION ≠ RECOMMENDATION.»* ·
  *«Không được diễn giải "Agent nghiêng về B" thành OWNER_LOCKED.»*
- 05/09 ~00:0x — *«tới đâu rồi em»*

### `CODE_DID`
- `gpt_analyzer.py:6738` `_shadow_mode = lane_test_shadow_pack or (selected_model in SHADOW_GATE_MODELS)` — **còn sống**
- `main.py:9840` gộp cap cố ý + trượt gate vào một tập `filtered_models`
- `gpt_analyzer.py:639` RULEBOOK §11 · `:337-341` + `metrics_calculator.py:635` (P07)
- `scheduler.py:4245-4255` (official 15/30/30) vs `:7356` (shadow 60) — cửa sổ khác nhau
- `du-doan.html:1413` hiển thị `consensus_level` sai cho người dùng
- tool calling: grep 5 mẫu = **0 dòng**

### `RUNTIME_DID`
- 57/57 payload thật **TRƯỢT** `CONTAMINATION_GATE_V2`, trung bình 220 điểm
- 33/33 lượt shadow nhận `ĐỀ XUẤT PYTHON` + `SỐ NÊN TRÁNH`
- 88/88 lượt official của `gpt-oss-120b` nhận gói ngữ cảnh shadow
- vân tay khớp **0/60** lượt ngày 04/09
- ba model của ba provider cùng trích `39: 77.7pt, WARM, UP, #2` — chuỗi không có trong bản render nào

### `DOC_SAID`
- `REPORT_V11164.md` «ít nhất 46/72» — **`DOC_SAID` ≠ `CODE_DID`**, rút lại ở **R14**
- `REPORT_V11164.md` «71 ngày liên tiếp» — thiếu định nghĩa, rút lại ở **R15**
- V11059 ngưỡng `n=96` — công thức thiếu `z_β`, tài liệu ghi là đủ mẫu trong khi chỉ 50% sức mạnh
- V11001/V11007 «đã gỡ hết gan/nóng/lạnh» — **sai một phần sau 28 ngày**

### `NOT_VERIFIED`
- token count (không có tokenizer, cấm gọi provider) · 3 đường `analyze_and_predict` không dump ·
  105 biến thể retry là `CODE_REPRODUCED` · nội dung Notion · 9 cổng Wave 1 không có trên VPS

### `RETRACTED`
- **R14** «46/72» · **R15** «71 ngày liên tiếp» thiếu định nghĩa · **R16** «z=−0,10 p=1,00» trộn hai phép
- (từ V11164, vẫn đứng) RL-008…RL-013

### `PROPOSED`
- 17 điều kiện · `PURE-CONTEXT-OUTPUT-1.0.0-DRAFT` · renderer · `CONTAMINATION_GATE_V2` ·
  3 vá NHÓM A · MT artifact · bản nháp đăng ký trước
- **Tất cả đều là ĐỀ XUẤT. Không cái nào đã chạy trên production.**

---

## 13 · Commit

| | |
|---|---|
| private HEAD trước | `a68384fb235b548515e022131aa3e76932d0c3f9` |
| public HEAD trước | `53074cfe6704a4c6db37a849661a486557780013` (`V11164_FINAL_TIP`) |
| `V11164_BASE` | `af4597a38c5f3b80a76ae2b4a9fb8aa46de65a09` |
| `governance_seq` | 480 → **481** |
| `QD` mới | **`QD-073`** (bộ cấp canonical `_v11044`, QD-072 là cao nhất trước đó) |
| private commit V11165 | *(mục cuối, cập nhật sau push)* |
| public commit V11165 | *(nt)* |

---

TanPhatAI cần làm: ghi **`V11165`** — `governance_seq 481`, công khai bản này. Ghi **`QD-073` = Owner khoá PHƯƠNG ÁN B** (nguyên văn: *«Ok đồng ý khuyến nghị đề xuất, chứ ý ghi nhận đầy đủ thông tin kẻo quên.»*), `OPTION_A = REJECTED`, `OPTION_C = DEFERRED_UNTIL_SQL_CONSUMER_AND_GRAIN_DEFINED`, và quyết định đó đã được ghi vào **SÁU chỗ** theo đúng yêu cầu «kẻo quên». Ghi **`PURE_CONTEXT_CANDIDATE = BLOCKED_WITH_EXACT_REASONS` — 6 blocker + 1 indeterminate**, trong đó **ba blocker đã có vá chờ owner ký** (`SC-02` vân tay · `SC-07` rò ctx · `SC-12` kế toán MT) và **ba blocker là bản chất prompt production** (`SC-04` rổ chọn sẵn · `SC-05` 1/35 có nền · `SC-08` mệnh lệnh không có phương tiện). Ghi **CÂU TRẢ LỜI CHO «THUẦN NGỮ CẢNH»: CHƯA ĐẠT** — cờ `context_only` gác **6/171 = 3,51%**, cổng `CONTEXT_ONLY_V2` gác **1,5/14 nhóm**, **57/57 payload thật TRƯỢT** `CONTAMINATION_GATE_V2` với trung bình **220 điểm ô nhiễm**, và **sửa đủ 14 nhóm chỉ gỡ ~15% độ dài** ⇒ **đây không phải chuyện cắt ngắn prompt**. Ghi **phép đo T-B ĐÃ TỒN TẠI, đủ mẫu, chưa ai đọc verdict**: z = −0,0995, `NO_ANOMALY_FOUND` **nhưng chỉ trong phạm vi MDE ≈ 8,04 pp**, và **ngưỡng `n=96` chỉ là 50% sức mạnh vì công thức thiếu `z_β`** (đúng phải **194 cặp**); **cả hai nhánh đều không khác mức chọn ngẫu nhiên ở cả ba miền**; **«đổi 70,2% số chọn» phải đọc cạnh sàn nhiễu 61,3%**. Ghi **hệ KHÔNG lưu prompt đã gửi** — vân tay khớp **0/60** lượt, và **ba model của ba provider cùng trích một chuỗi không tồn tại trong bất kỳ bản render nào** ⇒ chuỗi đó có thật trong prompt đã gửi. Ghi **BA CA RÚT LẠI MỚI**: **R14 «46/72» KHÔNG tái lập được (RM-11) — số đúng là 45**; **R15 «71 ngày liên tiếp» phải kèm định nghĩa, chuỗi `EXCLUDE_PRIMARY` thật chỉ 7 ngày**; **R16 «z=−0,10 p=1,00» trộn hai phép McNemar**. Ghi **rolling WR/TOP1 của MT đang TRỄ 71 NGÀY**, và **sửa kế toán xong thì số MT XẤU ĐI** (`top1_7 57,1% → 28,6%`). Ghi **`consensus_level` gắn nhãn sai cho 268/567 bundle và nhãn đó ra tới người dùng**. Ghi **GATE 0 bắt được lỗi của chính agent**: `chmod 444` không chặn root nên bản clone «bất biến» đầu tiên là GIẢ — phải `chattr +i` mới thật. **Code KHÔNG đi trước tài liệu** — phiên này **0 ghi production · 0 deploy · 0 restart**, `neo558` khớp từng ký tự, 6 hash tệp đang serve không đổi. **Không mở Prompt 44. Không mở FU mới. Không mở Plan mới.** `POOL_VERDICT` giữ **`HOLD`** · `MODEL_ACTION` giữ **`BLOCKED`** · `PROMPT_43_R1` giữ **`PARTIAL`** · `GRAND_OVERHAUL_CHAIN` giữ **`PARTIAL`**.
