# REPORT V11164 — EOD LIVE CLOSURE SAU V11163 · NGÀY LIVE 04/09/2026

> **Ngày:** 04/09/2026 20:53 → 23:xx (VN) · `CURRENT_ACTOR = CLAUDE_CODE`
> **Phạm vi:** forensic đầy đủ sau chuỗi fix V11158→V11163, cho ngày live đã hoàn tất cả ba miền.
> **8 cổng · 40 agent · 32 phản biện độc lập · 84 phát hiện · 196 artifact · 821,8 MB.**
>
> `MATERIALIZATION_DECISION = DEFERRED_PENDING_OWNER_REVIEW` · `OUTPUT_COUNTERFACTUAL_RANK_PRODUCTION_WRITE = FORBIDDEN`
> `MT_PREREGISTRATION = PROVISIONAL_AGENT_PROPOSED` · `POOL_VERDICT = HOLD` · `MODEL_ACTION = BLOCKED`
> `PROMPT_43_R1 = PARTIAL` · `GRAND_OVERHAUL_CHAIN = PARTIAL`
>
> **Bản này RÚT LẠI năm kết luận đã công bố** (mục 4.3) — trong đó **hai** là của chính V11163 vừa xuất hôm nay.

---

## 1 · Tóm tắt — EXECUTIVE VERDICT

**Ngày 04/09 là ngày vận hành sạch nhất trong 12 ngày, và đồng thời là ngày phơi ra rằng lớp ĐO
của hệ đang hỏng ở nhiều chỗ hơn ta tưởng.** Hai câu đó không mâu thuẫn: máy chạy tốt, còn cái
thước đo máy thì lệch.

| | |
|---|---|
| **Chạy đúng mã sau fix?** | ✅ **CÓ** — 10/10 tệp trọng yếu sửa **trước** `01:08:40`, service khởi động `01:08:40`, `NRestarts 0`, PID `3370750` không đổi suốt ngày |
| **Vận hành** | 🟢 81/81 lượt có output · **0 rỗng ở cả ba miền — ngày DUY NHẤT đạt 0/0/0 trong 12 ngày** · 0 timeout · 0 parse lỗi · 0 late · 0 ERROR |
| **TOTAL/FINAL tái lập** | 🟢 **30/30 hàng top-10 khớp tuyệt đối** cả số, điểm 4 chữ số thập phân và thứ tự voter; 81/81 hàng trọng số BT khớp; 3-càng 853/228/586 đúng |
| **Năm tầng raw → UI** | 🟢 tầng 1 = 2 = 3 = 4, **không có điểm lệch** |
| **Prompt regime** | 🟡 `PROMPT_LANE_REGIME_FIXED` **nhưng** `PROMPT_CLEAN_NOT_PROVEN` |
| **Dự đoán** | ⚪ BT 1/3 (MT trúng 28) · 60 ngày đo lại: **không model nào vượt nền có ý nghĩa** |
| **Nợ** | 🔴 nợ báo cáo **tăng** 38/232 → **40/240** · 152/194 mục quá hạn · ba tệp điều hướng lệch 14 ngày |
| **production** | 🟢 `neo558` khớp từng ký tự với lúc chụp GATE 0 · 6 bảng khoá y hệt · `output_counterfactual_rank` vẫn `0/17.121` |

### Ba điều đáng đọc nhất

**① Bộ chọn TOTAL trung thực tuyệt đối.** Tái lập từ **raw model output** (không lấy published
FINAL làm đầu vào) cho cả ba bundle: khớp 30/30 hàng. Số công bố cho owner hôm nay **đúng là số
máy tính ra** — không drift, không writer thay thế, không lookahead. Đây là lần đầu mệnh đề đó
được chứng minh chứ không phải được tin.

**② Vá V11160 đúng nhưng chưa kín, và chính agent đã nói quá.** Định tuyến **regime** đã theo
LƯỢT: 60/60 lượt đúng, `gpt-oss-120b` ngày 03/09 ăn `CONTEXT_ONLY_V2` ở hai lượt official thì
ngày 04/09 về `LEGACY_PROMPT` cả ba miền. **Nhưng** còn **một chỗ thứ hai** vẫn định tuyến theo
MODEL (`gpt_analyzer.py:6738`), nên `gpt-oss-120b` chạy official vẫn nhận **gói ngữ cảnh của lane
thí nghiệm** — và nó bỏ phiếu **top-1** vào bạch thủ công bố của MN (`53`) lẫn MB (`86`). Cộng
thêm: **vân tay prompt chỉ băm 48,2% chuỗi thật**, nên `contam_hits = 0` **không chứng minh được
prompt cuối sạch**.

**③ MT bị loại khỏi đo lường chính 71 ngày liên tiếp vì một lỗi KẾ TOÁN, không phải lỗi chạy.**
Trần voter MT-13 (V10752, owner duyệt 25/06 — **cố ý** bỏ hai model yếu nhất) bị kế toán **chung
một tập** với model trượt gate, nên `day_governance` ghi nguyên văn *«Thiếu 2 model (13/15)»*,
gắn `DEGRADED_LIVE_DAY` + `EXCLUDE_PRIMARY`. Hệ quả 90 ngày: **MT bị loại 72/90 lượt (80,0%)** so
với MN 10/91 (11,0%). Hai model đó **chạy xong và đều PASS gate** — `gate_diagnostics` ghi
`pass=true` cho cả hai, trong khi `wr_gate_filtered` lại liệt kê chúng.

---

## 2 · Owner yêu cầu gì — NGUYÊN VĂN (`PRJ-INTERACTION-LEDGER-001`)

| giờ (VN) | NGUYÊN VĂN | loại | agent đã làm gì | trạng thái |
|---|---|---|---|---|
| 03/09 ~08:xx | *«⚠️ 🔬 DeepSeek Reasoner 43% 30d ⚠️ 🤖 GLM 5.2 45% 30dEVAL — 2 model này không ra output sẵn kiểm tra dùm anh luôn em»* | `YÊU_CẦU` | truy nguyên nhân gốc hai model | `ĐÃ_LÀM` (V11158) |
| 03/09 ~09:xx | *«fix cho chạy ra output luôn chứ em. Chưa tới giờ block mà em.»* | `YÊU_CẦU` | trần token 49152/49152 · hard-timeout · lớp bóc JSON | `ĐÃ_LÀM` (V11158) |
| 03/09 ~10:xx | *«Anh chưa thấy 2 model rỗng tiến hành chạy dự đoán và áp dụng vào total nếu có vậy em? nguyên nhân là gì em?»* | `HỎI` | giải thích đường vào TOTAL | `ĐÃ_LÀM` |
| 03/09 ~11:xx | *«Tiếp theo là gì em? … Hôm nay vẫn tệ như mọi ngày»* | `HỎI` | đánh giá dự đoán · prompt thuần ngữ cảnh · đơn model vs TOTAL | `ĐÃ_LÀM` |
| 03/09 chiều | **PROMPT 43 R1 · COUNTERFACTUAL RANK REPAIR OFFLINE-FIRST** (I–XIX) | `YÊU_CẦU` | V11159, production READ-ONLY | `ĐÃ_LÀM` |
| 03/09 tối | *«làm xong chả báo cáo gì là sao em?»* | `BÁC_BỎ` | thôi báo miệng — xuất bốn mặt + báo cáo công khai | `ĐÃ_LÀM` |
| 03/09 tối | *«ok vậy đợi soi xong tổng hợp đề xuất báo cáo tổng hợp 1 lần luôn em»* | `ĐỔI_ƯU_TIÊN` | gộp báo cáo một lần | `ĐÃ_LÀM` |
| 04/09 ~00:2x | *«ok em thực hiện tuần tự lần lượt xử lý dứt điểm các vấn đề em đã đào ra dùm anh»* | `YÊU_CẦU` | mở khoá mục ① (chạm đường official); xử tuần tự 5 vấn đề | `ĐÃ_LÀM` (V11160–V11163) |
| 04/09 ~01:0x | *«Tiếp đi em»* | `YÊU_CẦU` | V11162 tầng ghi vết 3-càng | `ĐÃ_LÀM` |
| 04/09 ~01:3x | *«Tiếp tục đi e»* | `YÊU_CẦU` | V11163 diễn tập migration | `ĐÃ_LÀM` |
| 04/09 ~20:5x | **PROMPT 43 R1 · EOD LIVE CLOSURE AFTER V11163** — 8 gate · 19 output · 10 câu | `YÊU_CẦU` | bản V11164 này | `ĐÃ_LÀM` |
| 04/09 ~21:5x | *«8 gate xong chưa em?»* | `HỎI` | báo tiến độ thật: 6/8 xong, 2 đang chạy — không tô hồng | `ĐÃ_LÀM` |
| 04/09 ~21:1x | *«Xong chưa còn gì nữa không em?»* | `HỎI` | báo thẳng **chưa xong**: workflow lần 1 chết sau 4 phút, phải chạy lại | `ĐÃ_LÀM` |

**Ràng buộc owner khoá, giữ nguyên suốt phiên:** *«Không mở: Prompt 44; FU mới; Plan mới; work
package materialization mới; model promotion/retirement/cutover.»* · *«Không được diễn giải
"Agent nghiêng về B" thành OWNER_LOCKED.»* · *«Không dùng câu "production 0 mutation" nếu thực tế
đã có code deploy/restart. Phải dùng nhãn chính xác cho từng loại.»*

---

## 3 · Đào bới / phát hiện

### 3.1 · Immutable evidence manifest *(output 2)*

Đóng băng **trước** mọi phân tích, không sửa về sau.

```
MANIFEST_SHA256 = ad25492b889f570314eb935ae8b08103a3cb171ced72ddbbabe41f985c34e78f
artifact        = /root/Lottery_AI_Test/artifacts/v11164_gate0_manifest.json
INDEX_SHA256    = b9e232738d9bf85e1f965b363b0b202e4bd5fa4c9622f44c85ccf3c0d7a011fc
artifact index  = /root/Lottery_AI_Test/artifacts/v11164_index.json  (196 tệp · 821,8 MB)
```

| | |
|---|---|
| runtime | PID `3370750` · active · `NRestarts 0` · health `200` · start `Fri 2026-09-04 01:08:40 +07` |
| env service | `{PYTHONUNBUFFERED:1, LLM_CONTEXT_ONLY_V2_LANE:shadow}` |
| **10/10 tệp trọng yếu sửa TRƯỚC service start** | `gpt_analyzer.py 758c29c1…` (00:43:26) · `main.py 4ed5fd7e…` (01:08:38) · `scheduler.py 2961987d…` · `database.py fd3d2349…` · `model_registry.py 4c84ae9a…` · `combo_super.py 47047b1d…` · `_v10785_late_fill.py 23cf4c10…` · `_v11160_test_lane.py dc32f708…` · `_v11162_lo3_lineage.py e67fcac4…` · `_materialize_shadow_promotion_scorecard.py 291e4520…` |
| DB | 254 bảng · `predictions 14.201` · `final_bundles 567` · `lottery_results 15.416` · `model_daily_eval 14.065` · scorecard `17.121` · reliability `5.276` |
| neo558 | `a82c508d3569abda47041ad625cca93fdec2227fbe389c395dc7f139893a0e5f` |
| journal 04/09 | 10.854 dòng · sha `160a6bb53325c109` |
| bản sao audit | `v11164_audit.db` 813 MB · `integrity_check = ok` · khớp gốc |

**Xác nhận cuối phiên (23:xx) — cả 5 phép khớp GATE 0:** `neo558` KHỚP · đếm dòng KHỚP ·
`output_counterfactual_rank = 0/17.121` KHỚP · PID KHỚP · `NRestarts 0` KHỚP.

### 3.2 · Mutation ledger — năm loại tách riêng *(output 3)*

> Owner cấm dùng câu *«production 0 mutation»* nếu thực tế đã có deploy/restart. Dưới đây là nhãn
> chính xác cho từng loại, **không gộp**.

| # | loại | ngày 04/09 | bằng chứng |
|---|---|---|---|
| ① | **production DB row mutation do agent** | **0** | mọi kết nối mở `mode=ro`; ghi production cuối cùng là V11158 lúc **03/09 13:59** |
| ② | **production code deploy** | **CÓ — 3 commit, TẤT CẢ trước 01:08:40** | `5e8217a` 00:56 · `741bcfb` 01:13 · `6243211` 01:41 · mtime tệp: `gpt_analyzer.py` 00:43:26, `main.py` 01:08:38 |
| ③ | **service restart** | **CÓ — 1 lần, 01:08:40 +07** | `ActiveEnterTimestamp`; `NRestarts 0` kể từ đó; PID `3370750` không đổi suốt ngày |
| ④ | **local clone write** | **CÓ** | `artifacts/v11164_audit.db` (813 MB) — bản sao; **0 ghi** vào clone (mở `mode=ro` khi phân tích) |
| ⑤ | **report / Git write** | **CÓ** | commit riêng ×3 · commit công khai `a430a72` · 196 artifact JSON |

**Câu ĐÚNG phải nói:** *«Toàn bộ deploy và restart của ngày 04/09 xảy ra TRƯỚC 01:08:40. Mọi lượt
dự đoán live — MN 05:00, MT 05:00–17:00, MB 17:30 — chạy trên MỘT bản mã duy nhất, không đổi giữa
chừng. Agent không ghi một dòng nào vào production DB trong ngày 04/09.»*

**Câu SAI, cấm dùng:** *«production 0 mutation ngày 04/09»*.

### 3.3 · `LIVE_EOD_REGION_LEDGER` *(output 4)*

Artifact: `artifacts/v11164_g1_region_ledger.json`

| cột | MN | MT | MB |
|---|---|---|---|
| bundle ID | **825** | **827** | **829** |
| mốc đóng băng | 15:45 | 16:58 | 17:58 |
| `ai_chain` start → end | 05:15:00 → 05:21:04 (363,7s) | 16:40:11 → 16:46:00 (349,0s) | 17:30:33 → 17:33:41 (188,0s) |
| bundle created_at | 05:21:04 (**sớm 10h24**) | 16:46:00 (**sớm 12′**) | 17:33:41 (**sớm 24′**) |
| invoked / returned | 8/8 (+combo = 9/9) | 8/8 (9/9) | 8/8 (9/9) |
| parse_ok / err | 16 / **0** | 16 / **0** | 16 / **0** |
| **empty** (JSON→list rỗng, RM-09) | **0** | **0** | **0** |
| timeout cứng / soft-continue 90s | **0** / 5 | **0** / 2 | **0** / 2 |
| late | **0** | **0** | **0** |
| output-eligible voter | 15 | 15 | 15 |
| **actual voter** (`model_count`) | 15 | **13** | 15 |
| cap applied · displaced | không | **CÓ · meta-learning, random-forest** | không |
| TOTAL top-1 (điểm) | `53` (0,1088) | `28` (0,0977) | `86` (0,0887) — top-2 `78` cách **0,0011** |
| FINAL BT · lô2 · 3-càng | `53` · `["53","73"]` · `853` | `28` · `["28","86"]` · `228` | `86` · `["86","78"]` · `586` |
| anti-trap | `NOT_APPLICABLE` | **`FULL_SPENT`** — vẫn công bố | **`FULL_SPENT`** — vẫn công bố |
| PP-1 dampener | 1 sự kiện (`53`: 0,128→0,1088) | **TẮT** theo thiết kế | bật, 0 sự kiện |
| kết quả về | 16:39:39 | 17:30:01 | 18:31:32 |
| **hit/miss** | BT **LOSE** · lô2 PARTIAL | **BT WIN · lô2 WIN · xiên2 WIN** | BT **LOSE** · lô2 LOSE |
| `day_governance` | INCLUDE · VALID | **EXCLUDE_PRIMARY · DEGRADED** *«Thiếu 2 model (13/15)»* | INCLUDE · VALID |

> ⚠️ **Bảng trên là SỔ GHI KẾT QUẢ MỘT NGÀY, không phải tuyên bố hiệu quả** — hai dòng `FINAL BT ·
> lô2 · 3-càng` và `hit/miss` chỉ ghi *chuyện gì đã xảy ra ngày 04/09*, **không** so với nền nào.
> Phiên này **cố ý không đo** hiệu quả bộ k số vì phạm vi là **một ngày live**, không phải đo dài hạn
> (`PRJ-SELECTION-WINDOW-001` · RM-18). Bộ cửa sổ **đầy đủ** cho thước bộ k số nằm ở **V11086**, đo
> trên nền đúng `1 − (1−b)^k` (**không** phải nền 1 số): **30 ngày −3,96pp · 90 ngày −5,15pp ·
> 180 ngày −0,35pp** — cả ba đều **âm**.

**Phân loại `prediction_trace` (60 dòng, KHÔNG 1:1 với 81 dòng `predictions`):**
scheduled production invocation **24** · post-bundle replay **0** · emission-only **0** ·
diagnostic (`shadow_auto_eval`) **33** · duplicate **3**. Cộng: 24+33+3 = **60** ✓.
24 cặp có `predictions` mà không có trace = **8 model no-token × 3 miền** (không gọi provider nên
không sinh trace); 57 + 24 = **81** ✓.

### 3.4 · Prompt routing / fingerprint matrix *(output 5)*

Kiểm **toàn bộ 84 lượt**, không lấy mẫu (60 lượt LLM có trace + 24 lượt ML/ensemble không có
prompt LLM). Artifact: `artifacts/v11164_g2_prompt_matrix.json`

| phép | kết quả |
|---|---|
| `SCHEDULED_LANE_ROUTING_PROVEN` | ✅ **PROVEN** — 27/27 official → `LEGACY_PROMPT` · 33/33 shadow → `CONTEXT_ONLY_V2` · 0 FAIL |
| `SCHEDULED_SHADOW_PROMPT_CLEAN_PROVEN` | 🟡 **PROVEN NHƯNG PHẠM VI HẸP HƠN CÂU CHỮ** — 33/33 có `contam=0`, nhưng vân tay chỉ phủ 40,1–48,2% chuỗi thật |
| `OFFICIAL_CONTROL_COHORT_CLEAN_ON_04_09` | 🟡 **sạch về REGIME, KHÔNG đồng nhất về NỘI DUNG** |
| Model nhận SAI regime mà vẫn bỏ phiếu? | ✅ **KHÔNG** — 0/3 bundle có voter `CONTEXT_ONLY_V2` |
| Vân tay thiếu / stale? | ✅ **KHÔNG** — 60/60 có đủ ba trường, 60 sha256 khác nhau, 0 trùng |

**Năm kiểm bắt buộc cho `gpt-oss-120b`** (model duy nhất ở giao `SHADOW_GATE_MODELS × output_eligible`):

| # | nội dung | kết quả |
|---|---|---|
| 1 | Official dùng legacy prompt | ✅ **PASS** — 3/3 lượt `LEGACY_PROMPT`, journal 2 dòng `[CONTEXT_ONLY_V2][V11160] … lượt NÀY là OFFICIAL → GIỮ prompt cũ` |
| 2 | Shadow dùng `CONTEXT_ONLY_V2` | ⚪ **INDETERMINATE_NOT_EXERCISED** — 0 lượt shadow ngày 04/09; lượt cuối `2026-08-01T05:20:52`. **Không tự nâng thành PASS** |
| 3 | Không còn routing theo model membership | 🔴 **FAIL** — `gpt_analyzer.py:6738` còn `or (selected_model in SHADOW_GATE_MODELS)` |
| 4 | Mọi lượt `CONTEXT_ONLY_V2` có `contam = 0` | ✅ **PASS** — 33/33 |
| 5 | Vân tay đến từ prompt runtime THẬT | 🟡 **PARTIAL** — băm chuỗi thật, nhưng ở `:6723` **trước** khi nối `ctx_pack`/RULEBOOK ở `:6755-6762` |

**Hệ quả đo được của kiểm #3:** `gpt-oss-120b` chạy official nhận gói ngữ cảnh **14.142 / 14.536 /
18.427** ký tự — **đúng bằng gói của lane thí nghiệm** — trong khi 7 model official cùng miền nhận
**10.977 / 11.557 / 15.448**, chênh **+2.979 … +3.165** ký tự. Quét 30 ngày (06/08→04/09), lọc bỏ
dòng shadow-lane: **86/86 cặp (ngày, miền) đo được đều lệch**; 3 cặp không đủ dữ liệu đối chiếu;
mở sang 31 ngày: **89/89**. Bảy model official khác **không lệch ở bất kỳ cặp nào (0/86)**.

**Vân tay thiếu bao nhiêu:** chuỗi thật = `24.435 − 12 + 10.977 + 2 + 15.256` = **50.658** ký tự;
`runtime_prompt_chars` báo **24.435** ⇒ **thiếu 26.223 ký tự = 51,8%**. Chú thích trong chính mã
(`:6716-6718`) ghi *«Ba trường dưới đây băm CHÍNH chuỗi sắp gửi đi»* — mâu thuẫn trực tiếp giữa ý
định thành văn và hành vi.

**Điểm mù của bộ 5 dấu ô nhiễm:** khối Phase 11 in ra `Win Rate` (viết hoa, có dấu cách) trong khi
bộ dấu tìm `win_rate` ⇒ khối đó **lọt vào cũng đếm ra 0**. Chốt chặn Phase 11 ở lane shadow vẫn
đứng, nhưng đứng bằng **đọc mã + 19 dòng journal `[Phase 11][CONTEXT_ONLY_V2] BỎ QUA`**, không
phải bằng con số `contam=0`.

### 3.5 · `MODEL_UNIVERSE_LEDGER` *(output 6)*

Artifact: `artifacts/v11164_g3_model_universe.json` — 63/63 danh tính đủ 20 trường.

| tập | số | ghi chú |
|---|---|---|
| **vũ trụ model thật** | **63** | 57 trong `predictions` ∪ 6 chỉ có trong registry |
| «57 nguồn lịch sử» | 57 | ✅ ĐÚNG cho `predictions.ai_model` — nhưng **KHÔNG PHẢI vũ trụ model**; và `<NULL>` / `NO_TOKEN_DIAGNOSTIC` / `all` **không phải model** |
| roster mong đợi 04/09 | 27 | = **27 thực tế** · hiệu hai chiều **rỗng** |
| output-eligible | 15 | = **15 voter-at-time** · **0 rò shadow** |
| shadow | 11 | đúng 11 model chạy `shadow_auto_eval` regime `CONTEXT_ONLY_V2` |

**Phát hiện cấu trúc nặng nhất — số voter công bố LỚN HƠN số nguồn độc lập.** 7/15 voter là dẫn
xuất hoặc cha mẹ của nhau: `smart-ensemble` ⊂ 4 ML · `smart-ml` = xgboost + random-forest ·
`combo-super` = top-3 của chính pool đó. Ngày 04/09: số `73` ở MN có **3 phiếu nhưng chỉ 2 nguồn**;
bạch thủ MT `28` có **4 voter nhưng chỉ 3 danh tính model**.

**Chất lượng 60 ngày, nền ĐÚNG cho từng miền** (phủ sóng đuôi 2 số / 100, bootstrap cụm theo ngày):
**KHÔNG model nào vượt nền có ý nghĩa.** Ba dòng dưới nền: `gemma-4-31b` [−21,9; −6,1] (đã nghỉ) ·
`glm-5.2` [−13,1; −0,5] · `smart-ml` [−13,2; −1,0]. Hai dòng sau **sát biên và chưa hiệu chỉnh đa
biến** (34 phép so ⇒ kỳ vọng ~1,7 dương tính giả ở 95%) — **không đề xuất hành động nào** từ số này.

`combo-super` — model cờ đầu — chỉ đổi top-1 **6/158 bundle**, đóng **6,0%** điểm top-1, **0 cứu /
0 phá**.

### 3.6 · Tái lập TOTAL / FINAL / override *(output 7)*

Artifact: `artifacts/v11164_g4_total_final.json` · công cụ `_v11161_rank_gen.py` (`CanhGac` chặn
oracle **bằng cấu trúc**, không bằng lời hứa).

| thành phần | kết quả |
|---|---|
| `effective_weight` · `strength/10` · `verdict_weight` · `lane_weight` · `position_weight` | ✅ khớp từng thành phần |
| PP-1 dampener ×0,85 | ✅ MN kích hoạt **đúng 1 lần** trên `53` (0,1280 → 0,1088, 3 voter mang dấu CONV-DOWNGRADE/DIVERSITY) · MT factor = 1,0 (**TẮT** đúng `_PP1_DAMPENER_DISABLED_REGIONS={"MT"}`) · MB bật, 0 sự kiện |
| PP-5 family bonus | ✅ `ENABLE_FAMILY_BONUS=False` → không áp |
| **trần voter MT-13** | ✅ tái lập **đúng hai model bị đẩy ra** (meta-learning, random-forest) và **đúng thứ tự** `(bt_rate, win_rate)` giảm dần — hai model đó hạng 14 và 15/15 |
| production rounding | ✅ `round(bt_rate,1)` rồi `round(bt_weight,3)` (`database.py:3420-3429`) — **điều kiện cần**, bỏ là lệch thứ tự |
| tie-break tất định | ✅ MB có **hoà điểm THẬT**: `96` và `82` cùng `0,050800000000` (hiệu = 0,0). Tái lập ra đúng thứ tự vì `sorted` ổn định + `ORDER BY created_at DESC` |
| `ranked[:10]` · lô2 · xiên2 · xiên3 · lô3 | ✅ khớp |
| **tổng** | **30/30 hàng top-10 · 81/81 hàng trọng số BT** |

**So năm tầng — ĐIỂM LỆCH ĐẦU TIÊN: KHÔNG CÓ.** Tầng 1 (raw tái lập) = 2 (persisted TOTAL) =
3 (published FINAL) = 4 (override-adjusted). `bach_thu` luôn là `ranked[0]` ở cả ba miền.
Không có writer thay thế, không backfill (81/81 dòng `late=0`), không bundle fallback.

**Tầng 5 KHÔNG ĐO ĐƯỢC** cho 04/09 — bề mặt công khai bị **viewer-freeze kẹp ở 2026-06-07**, và
`/api/final-bundle` sau FU-438 là admin-only fail-closed. Đây là **thiết kế owner đã khoá**, không
phải drift; nhưng phải ghi là *không đo được*, không được ghi là *không lệch*.

**Hai cơ chế nhân đôi ảnh hưởng — phải gọi tên tách bạch:**

| cơ chế | bản chất | bằng chứng |
|---|---|---|
| `smart-ensemble` / `smart-ml` | **CHẠY LẠI model cha trong bộ nhớ** rồi bỏ phiếu như model riêng | mảng `lstm_numbers` của smart-ensemble MN là `["73","10","92","05","17"]` — **trùng từng phần tử** với `xgboost_numbers` của smart-ml MN |
| `combo-super` | **GỌI LẠI bằng lượt API MỚI** chính model đã có phiếu | trace: MN `gemini-2.5-pro` 05:15:42 → `['28','75']` **và** 05:21:04 → `['28','53']`; MN `claude-opus-4-6` 05:16:01 và 05:20:24; MT `gemini-2.5-flash` 16:40:49 và 16:46:00 — dòng thứ hai **trùng đúng giây tạo bundle** |

Cơ chế `combo-super` gọi lại **là thiết kế đã thành văn** (`combo_super.py:1374 → :1134`, docstring
`:1238`, `CLAUDE.md §59`) ⇒ nhãn đúng là `EXPECTED_BEHAVIOR`, không phải lỗi. **Lỗi thật** nằm ở
chỗ khác: số đếm voter **thô** (không de-dup huyết thống) đi thẳng vào `consensus_level`
(`main.py:10339-10345`, ≥4 → `strong`) ⇒ nhãn đồng thuận **bị thổi từ `moderate` lên `strong`**.
Ngày 04/09 việc này **KHÔNG đổi bạch thủ**.

**Trần MT-13 cắt lá phiếu nhưng KHÔNG cắt ảnh hưởng:** meta-learning và random-forest bị đẩy ra,
nhưng tín hiệu của chúng **quay lại nguyên vẹn** qua `smart-ensemble` / `smart-ml`.

### 3.7 · Tái lập 3-càng *(output 8)*

`_v11162_lo3_lineage.tinh_lo3_co_ghi_vet` tái lập **đúng 853 / 228 / 586**. Hai chữ số cuối của
lô-3 **bằng `bach_thu` của ĐÚNG lane official** ở cả ba miền (53/28/86). Cutoff `2026-03-08`, câu
lệnh dùng `date >= cutoff AND date < date_str` — **chặn trên NGHIÊM NGẶT**, nên 6 dòng
`lottery_results` của chính ngày 04/09 **không lọt vào**: không lookahead, bảo đảm **bằng cấu
trúc**. Ngày 04/09 nằm sau `MOC_THUAT_TOAN = 2026-06-27` ⇒ đúng thời kỳ thuật toán hiện hành (RM-21).
Mở rộng: **93/93 lô-3 tái lập đúng** trên 15 ngày × 3 miền.

⚠️ Cảnh báo kèm: prefix MB gần như **hoà bốn phía** — `5`(14) · `1`(12) · `6`(12) · `2`(12) —
thắng bằng **2 phiếu**.

### 3.8 · Operational before/after *(output 9)*

| thước | 04/09 | nền |
|---|---|---|
| output rỗng (cả ba miền) | **0 / 0 / 0** | **ngày DUY NHẤT đạt 0/0/0 trong 12 ngày** (03/09 MN=2; 02/09 và 01/09 mỗi miền 1) |
| coverage | 81/81 | — |
| parse | 60/60 | — |
| latency | med **55,0s** · p90 223,3s · **max 300,1s** | max **THẤP NHẤT trong 10 ngày** (nền 275–1084s) |
| scheduler | 1.250 dòng · 18 WARNING · **0 ERROR** | nền 7 ngày: 1.151–1.666 dòng · 13–40 non-INFO |
| tái lập tất định | **45/45 bundle** (15 ngày × 3 miền) · **93/93 lô-3** | — |
| roster drift | **không** | — |

**Không so trực tiếp được:** hai trường vân tay `runtime_prompt_*` chỉ tồn tại từ 03/09 (và 03/09
còn 20/62 dòng rỗng) ⇒ nền cho ba trường đó chỉ có **1 ngày**. Ghi rõ thay vì so bừa.

### 3.9 · Kết quả dự đoán — chỉ mô tả đúng mức bằng chứng *(output 10)*

| | 04/09 | nền 30 ngày | nền 7 ngày |
|---|---|---|---|
| BT | **1/3 = 33,3%** (MT `28` WIN) | 26/90 = 28,9% | 3/21 = 14,3% |
| top-10 trúng lô | MN 4/10 · MT 7/10 · MB 3/10 | med 4 · med 4 (tb 3,73; max 8) · med 2 | — |
| `model_daily_eval.bt_hit` | MN 63,0% · MT 59,3% · MB 14,8% | 39,5% · 39,2% · 19,6% | — |

**Với n = 3 bundle trong MỘT ngày, mọi con số trên là `EXPLORATORY`** — không đăng ký trước, không
hiệu chỉnh đa biến, không dùng z/Fisher/McNemar. **RM-04: chưa được phép kết luận.**
**CẤM dùng 04/09 để sửa ngưỡng MT sau khi đã nhìn kết quả.**

> ⚠️ **Cố ý trích MỘT cửa sổ — và phải nói rõ** (`PRJ-SELECTION-WINDOW-001` · RM-18).
> Bảng trên chỉ nêu nền **30 ngày** (và 7 ngày). Phiên này **không đo** cửa sổ 90 và 180 ngày cho
> bộ k số (lô2 / lô3 / xiên) — vì phạm vi work package là **một ngày live đã hoàn tất**, không phải
> đo hiệu quả dài hạn. **Không được đọc bảng trên như một tuyên bố hiệu quả.**
> Bộ cửa sổ đầy đủ nằm ở **V11086**, đo trên đúng thước bộ k số với nền `1 − (1−b)^k`
> (**không** phải nền 1 số — RM-18 cấm đúng chỗ này): **30 ngày −3,96pp · 90 ngày −5,15pp ·
> 180 ngày −0,35pp**. Cả ba cửa sổ đều **âm**, nên kết luận *«chưa có gì để mừng»* ở mục 10 câu **không
> phụ thuộc vào việc chọn cửa sổ nào**.

Trên cửa sổ 60 ngày với nền đúng từng miền: **không model nào vượt nền có ý nghĩa.** Đây là
**tái xác nhận** V11116 (25/08), không phải phát hiện mới.

### 3.10 · Anomaly register *(output 11)* — 20/20 phép đã chạy

**16 phép không thấy bất thường**, trong đó đáng kể: bundle tái lập 45/45 · lô-3 93/93 · 0 output
rỗng · 0 timeout · 0 ERROR · **không có lookahead** · **không có model xuất output sau giờ kết quả**
· roster không trôi.

**Bốn phép có kết quả:**

| # | phép | kết quả |
|---|---|---|
| 2 | nhiều model ra số giống nhau do route/alias/prompt duplication | 🟡 MN: **9 model ra cùng bộ `{28,53}`** — vượt p90 nhưng **chưa vượt max lịch sử** (max 11, ngày 30/08). Bảy trong chín thuộc lane shadow nên không bỏ phiếu — **nhưng cụm này ĐÃ chạm output**: bạch thủ MN công bố là `53` |
| 9/10 | vân tay trùng/khác sai regime | ⚪ **mất nghĩa** cho tới khi sửa lỗi vân tay thiếu 51,8% |
| 13 | replay bị tính như scheduled output | 🟡 **3 dòng trace lặp** (2 trùng đúng giây tạo bundle) — `prediction_trace` **không có trường tự khai loại lượt** |
| 18/19 | writer có chạm cột / có reader mới | 🔴 writer **CHẠM** cột ở cả hai câu INSERT, bind `None` vô điều kiện · **0 reader mới** |

### 3.11 · Debt register *(output 12)* — 32 dòng, map hết vào FU-449 / FU-450

**Không mở FU mới. Không có dòng `NEEDS_OWNER_MAPPING`.**

| món nợ | trạng thái đo hôm nay |
|---|---|
| 3 tệp điều hướng (`LATEST_REPORT.json` · `NEXT_ACTION.md` · `REPORT_INDEX.md`) | 🔴 **lệch 14 ngày** — khai V11098 / 376 thư mục; thật **V11163 / 440**. Cùng một lần sinh `2026-08-21 20:57:22`, commit `a8fca05`. Gốc: bộ sinh `_v11083` **không nối vào hook nào** |
| «94 mục quá hạn» | 🟡 tái lập **đúng bằng 94** tại commit `709efaf` (21/08) trên thước cửa sổ `[−14,+21]`. Đo lại hôm nay bằng chính bộ đọc canonical: **194 treo · 152 quá hạn**. **KHÁC THƯỚC — cấm trừ hai số** (RM-21) |
| sổ rút lại `docs/SO_RUT_LAI.json` | 🔴 đứng ở **7 mục từ 18/08**. Cổng `_v11085` **VẪN chạy mỗi git commit** — nhưng **danh sách chặn cũ 17 ngày**, nên mù đúng 4 kết luận vừa bị bác |
| **nợ báo cáo §57** | 🔴 **TĂNG**: 38/232 (02/09) → **40/240** (hôm nay) = **21 bản thiếu hẳn + 2 dương tính giả của cổng + 17 bản trượt khung**. **`V11156` (03/09) không có thư mục báo cáo nào** |
| 111 ô lưới role-at-time thiếu lớp L3 | 🟡 xác nhận 111, tái lập độc lập bằng số học lưới (37 ngày × 3 miền). Đóng được bằng **ghi hạn chế phạm vi**, **tuyệt đối không bù dữ liệu** (RM-17) |
| 357 bundle trước boundary 3-càng | ✅ xác nhận 357/567. **Cảnh báo:** V11159 cũng có một con số **357** nghĩa **hoàn toàn khác** (ô lưới trước 05/07) — cả hai đều tái lập đúng ⇒ dòng nợ `D-NUM-01`: mọi lần trích sau **bắt buộc kèm danh từ** |
| bất đối xứng telemetry | 🔴 11 model shadow **n = 92** đều nhau; ba model official **n = 6/3/2** vì lane official chỉ ghi khi hỏng ⇒ **vế official KHÔNG CÓ MẪU SỐ**, mọi so sánh độ tin cậy hai lane hiện vô nghĩa |
| writer `None` | 🔴 phạm vi bị khai **thiếu**: không phải 1 vị trí mà **3** ở câu INSERT thứ nhất và **6** ở câu thứ hai; caller thật là **`scheduler.py:665`**, không phải crontab |
| briefing đầu phiên | 🔴 **đứng im 19 ngày** — nguồn gốc của thói quen trích số cũ |
| `promotion_bucket` không có reader | ✅ **MỆNH ĐỀ NÀY SAI** — có `SELECT` sống ở `_v11155:135`, thêm `_materialize_multi_lane_shadow_p0:3038` và index `idx_smps_bucket` |
| true missing output 04/09 | ✅ **0/81** (đo theo RM-09) |
| stale reader | 🟡 **76 bảng im ≥7 ngày, 31 trong đó có điểm ĐỌC sống** (8 trên `/monitoring`, 11 trên `/du-doan-test`, 6 chỉ qua API, 6 chỉ mã nội bộ) |

⚠️ Số dòng RM-20 ghi trong `CLAUDE.md` đã **trôi ~360 dòng** (nay là `:12244 :12281 :15390 :15402`)
— mọi báo cáo sau phải **dẫn số dòng đo lại**, không chép lại.

### 3.12 · `_safe_stdio_ctx` fault injection *(output 13)*

Harness **cô lập**, trích đúng dòng 209–305 của `scheduler.py` (sha `2961987d8c3a6e27`) rồi `exec`
trong **tiến trình riêng** — **không** import module production, **không** chạm tiến trình service.
Chạy **4 lần**, `on_dinh = true`, `lech = []`.

**PHÂN LOẠI (đúng một nhãn): `LATENT_CODE_BUG_NOT_RUNTIME_INCIDENT`.**

| # | khiếm khuyết | nhãn | ghi chú |
|---|---|---|---|
| G7-F1 | probe `write("")+flush()` **mù với PIPE mất đầu đọc** (kernel thoát sớm *«Null write succeeds»* trước cả khi kiểm `pipe->readers`) | `PROVEN_DEFECT` | **Phạm vi đã thu hẹp sau phản biện:** **KHÔNG mù** với socket journald của production |
| G7-F2 | `sys.stdout` là **toàn cục** nhưng ctx chạy trong **luồng worker** ⇒ lượt A thoát trả stream hỏng về khi lượt B còn trong vùng ctx của chính nó | `PROVEN_DEFECT` (tầng MÃ) + **`PRODUCTION_MANIFESTATION = NOT PROVEN`** | tái lập bằng chính `_start_timed_model_call`: `A='A_OK'`, `B="B_NO:ValueError('I/O operation on closed file.')"`. Chạy chồng lượt là THẬT (soft-continue 90s, `scheduler_logs` id=280173 lúc 16:55:13) |
| G7-F3 | `_ensure_safe_stdio` **chỉ lưu stream HỎNG** (đúng thiết kế); nhánh `None` để lại `_SafeNullWriter` **vĩnh viễn** | `OPERATIONAL_IMPROVEMENT` *(hạ từ PROVEN_DEFECT sau phản biện)* | nhánh `None` **hiện không khả đạt** trong production |
| G7-F4 | hai docstring (`:254`, `:272`) mô tả **ngược** với mã | `OPERATIONAL_IMPROVEMENT` | lệch `DOC_SAID` ≠ `CODE_DID` (§62), không có hậu quả hành vi |
| G7-F6 | **stdout của service bị đệm khối dù `PYTHONUNBUFFERED=1`** — log console tới journal trễ trung vị **+19.200s**, tối đa **+84.900s** | `PROVEN_DEFECT` | kênh DB **đầy đủ và đúng giờ**; đây là mù **chẩn đoán**, không chạm dự đoán/bundle/DB |

**Ngày 04/09: 0 sự cố** trên cả ba nguồn — journal 04/09 (10.854 dòng) 0 hit · journalctl toàn bộ
còn lưu (39.101 dòng từ 29/08) 0 hit cho cả `closed file`, `Broken pipe`, `Bad file descriptor` ·
`prediction_trace` 04/09 (60 dòng) 0 hit.

---

## 4 · Hướng xử lý và vì sao chọn

### 4.1 · A/B/C materialization decision packet *(output 14)*

> **Kết quả cổng: `READY_FOR_OWNER_DECISION`.** Không ghi `OWNER_LOCKED`. Không chọn thay owner.

**Sáu câu bắt buộc, trả lời sau khi ĐO LẠI trên dữ liệu hôm nay:**

| # | câu | trả lời |
|---|---|---|
| 1 | Sau V11163 có reader THẬT nào xuất hiện? | **KHÔNG.** Quét lại toàn cây **5.056 tệp** → 253 dòng khớp; mã sống chỉ 7 dòng ở 3 tệp, **tất cả là DDL hoặc danh sách cột**. `main.py` **0 dòng**. 0 view · 0 trigger · 0 index |
| 2 | Có consumer/panel bị chặn vì cột rỗng? | **KHÔNG.** Sáu tệp đọc BẢNG không tệp nào chứa tên cột. Đây là **cột duy nhất trong họ không có giá trị** — bốn cột láng giềng đều `17.121/17.121` |
| 3 | Writer vẫn unconditional `None`? | **VẪN NGUYÊN** (sha `291e45203ddfb501`, khớp GATE 0). Writer **KHÔNG PHẢI «không chạm cột»** — nó **CHẠM** trong mọi INSERT và ghi đè `NULL` |
| 4 | Có cách biểu diễn `NOT_COMPUTED` khác `COMPUTED_OUTSIDE_TOP10`? | **CÓ, nhưng KHÔNG bằng một cột INTEGER đơn.** ⚠️ **Chặn cứng chưa ai nêu:** artifact PHA 1 chỉ lưu `top10` ⇒ **94/99 ô có hơn 10 ứng viên, tổng 420 hạng bị cắt cụt** — với dữ liệu đang có, *«hạng 11»* và *«không có trong danh sách»* **không phân biệt được** |
| 5 | Live 04/09 tạo yêu cầu mới đủ biện minh cho C? | **CÓ một yêu cầu mới thật, nhưng KHÔNG đủ.** Cửa sổ đo tiến cứu MT mở **đúng hôm nay**, nhưng artifact PHA 1 **dừng ở 03/09** và **không có job sinh hằng ngày**. Yêu cầu đó nói về **SINH KỊP THỜI**, không nói nơi lưu là SQL hay JSON |
| 6 | B còn là lựa chọn rủi ro thấp nhất? | **CÒN** — 0 đổi schema · 0 đụng writer · 0 dòng production bị ghi. **Nhưng phải sửa cách mô tả B: nó KHÔNG phải «không cần làm gì»** |

**Ba lỗ hổng của B, đo được hôm nay** *(đây là điều V11163 chưa nói)*:
① artifact dừng ở 03/09, **không tự kéo dài**; ② chỉ lưu top-10 ⇒ **420 hạng cắt cụt**;
③ trường mang **đúng cái tên** `hang_cua_no_trong_A` trong chính artifact là `NULL` **973/973 =
100%** — ai đọc artifact mà tưởng đó là rank **sẽ kết luận sai**; nguyên liệu thật là `A.top10`.

**Rủi ro của A nay có tiền lệ THẬT, không còn là giả định:** `17.001/17.121` dòng mang
`created_at = 03/09` — tức V11158 đã **viết lại gần trọn 6 tháng lịch sử trong một đợt**, và với
`UNIQUE(date,region,ai_model)` + `INSERT OR REPLACE` thì mọi giá trị đổ vào trước đó **đã bị xoá
sạch**. Trong đời bảng: **31.934 dòng đã bị ghi đè**.

**Bốn lớp `NULL` đo được** (không phải hai như đã công bố): `COMPUTED_IN_TOP10` **2.094** ·
`COMPUTED_OUTSIDE_TOP10` **444** · `NOT_COMPUTABLE_NO_NUMBER` **135** ·
`NOT_COMPUTED_OUT_OF_WINDOW` **14.448**.

**Agent vẫn nghiêng về B** — và đây **KHÔNG phải quyết định**, chỉ là khuyến nghị kèm giá.
Câu chặn quyết định không phải *«đổ hay không đổ»* mà là ***«câu hỏi nào cần trả lời bằng SQL trên
dữ liệu này»*** — **chỉ owner trả lời được**.

### 4.2 · MT preregistration readiness *(output 15)*

> ## **`NOT_READY_FOR_OWNER_LOCK`**

Ba lý do, cả ba đo được hôm nay:

1. **Thước đo bị hỏng ngay tại miền cần đo.** Phép đo tiến cứu MT dựa vào rolling WR/TOP1 của MT —
   nhưng MT bị `EXCLUDE_PRIMARY` **72/90 lượt (80,0%)**, trong đó **46/72 giải thích hoàn toàn bởi
   trần V10752** (một quyết định **cố ý** của owner bị kế toán nhầm thành hỏng hóc). Khoá ngưỡng
   trên một thước đang loại 80% mẫu của chính miền đó là khoá vào chỗ trống.
2. **Thước thứ cấp chưa có nguyên liệu.** Nó cần *«hạng của ứng viên trúng đầu tiên»* — tức bảng
   xếp hạng sinh **TRƯỚC** kết quả, **mỗi ngày**. Artifact PHA 1 **dừng ở 03/09**, **không có ô nào
   cho 04/09**, **không cron/job nào sinh hằng ngày**.
3. **Ngày mở cửa sổ trùng đúng ngày phát hiện lỗi routing.** `gpt-oss-120b` nhận gói ngữ cảnh khác
   phần còn lại của cohort official ở **86/86 cặp đo được trong 30 ngày** — chưa đo được ảnh hưởng
   định lượng lên số. Khoá ngưỡng trước khi biết điều đó là khoá lên nền chưa sạch.

### 4.3 · 🔴 RÚT LẠI — `PRJ-RETRACTION-001`

> Bốn phần bắt buộc cho mỗi ca: **chỗ gốc · nguyên văn câu sai · điều đúng kèm phép đo · quyết định
> nào đã dựa trên số sai.** Hai trong năm ca là của chính **V11163 xuất ra hôm nay**.

#### R1 — «Writer hằng giờ chạy `16:00 · 17:00 · 18:00 · 20:00`»

- **Chỗ gốc:** `CHANGELOG.md` mục V11163 · `docs/DE_XUAT_MATERIALIZATION_V11163.md:86` ·
  `docs/FOLLOW_UP_TRACKER.md` mục V11163 · `REPORT_V11163.md §3.3`
- **Nguyên văn câu sai:** *«job `measurement_materialize` chạy `16:00 · 17:00 · 18:00 · 20:00`»*
- **Điều đúng:** writer chạy **3 lần ngày 04/09**, theo **kết quả từng miền**:
  `scheduler_logs` id=280006 → VN **16:39:55** MN · id=280228 → VN **17:30:18** MT · id=280473 →
  VN **18:31:48** MB, mỗi lần `inserted=27`. Neo độc lập: chỉ có **đúng 3** giá trị `created_at`
  phân biệt trong ngày. Caller thật là **`scheduler.py:665`**, `crontab -l` **không có dòng nào**.
  Tần suất chính xác: **INDETERMINATE**.
- **Quyết định đã dựa trên:** lý do ② của khuyến nghị *«ĐỪNG ĐỔ»*. **Kết luận KHÔNG đổi** — writer
  vẫn ghi đè cột — nhưng lý do phải phát biểu đúng.

#### R2 — «`NULL` mang HAI nghĩa»

- **Chỗ gốc:** `REPORT_V11163.md §3.2` · `CHANGELOG.md` V11163 · `FOLLOW_UP_TRACKER` FU-450
- **Nguyên văn câu sai:** *«`NULL` đó gộp hai thứ khác hẳn nhau về ý nghĩa»*
- **Điều đúng:** **ÍT NHẤT BỐN lớp**, đo lại trên production (chỉ đọc): `COMPUTED_IN_TOP10` 2.094 ·
  `COMPUTED_OUTSIDE_TOP10` 444 · `NOT_COMPUTABLE_NO_NUMBER` **135** (lớp bị bỏ sót) ·
  `NOT_COMPUTED_OUT_OF_WINDOW` 14.448.
- **Quyết định đã dựa trên:** cùng khuyến nghị *«ĐỪNG ĐỔ»* — **củng cố thêm**, không đổi hướng.

#### R3 — «Nhánh `_safe_stdio_ctx` CHƯA TỪNG CHẠY» 🔴 *(nặng nhất)*

- **Chỗ gốc:** `REPORT_V11163.md §4` và `§9` · `CONVERSATION_CONTEXT_V11163 §4` ·
  `CHANGELOG.md` V11163 · `FOLLOW_UP_TRACKER`
- **Nguyên văn câu sai:** *«đo được **0 dòng lỗi I/O** trong journal ⇒ nhánh đó **chưa từng chạy**»*
- **Điều đúng:** nhánh **ĐÃ chạy thật**. `scheduler_logs` có **270 dòng** mang
  `ValueError: I/O operation on closed file.` từ **2026-05-10 12:01:21** đến **2026-07-19 17:30:00**
  (log_time naive = UTC), traceback chỉ thẳng `scheduler.py:1851 print(...)`. Ba họ lớn:
  `shadow_eval` per-model (90) · retrain ML ba miền (84) · Weekly Mining / weight optimizer / Excel.
  Nó im **từ 2026-08-01** nhờ **V10800 (15/07) và V10826 tách job sang subprocess có stdout riêng**
  — tức được vá bằng **CÁCH LY TIẾN TRÌNH**, hoàn toàn không nhờ `_safe_stdio_ctx`.
  Lỗi đo lường của tôi: tôi quét **journal** (chỉ còn lưu từ 29/08) chứ **không quét `scheduler_logs`**
  (có từ 2026-03-27) — **cửa sổ bằng chứng hẹp hơn cửa sổ kết luận**.
- **Quyết định đã dựa trên:** quyết định *«chủ động KHÔNG sửa»*. **Quyết định đó GIỮ NGUYÊN** —
  ngày 04/09 vẫn 0 sự cố trên cả ba nguồn — **nhưng lý do phải đổi hẳn**: không phải *«chưa từng
  chạy»* mà *«đã chạy 270 lần, đã được vá bằng đường khác, và hôm nay bằng 0»*.

#### R4 — «Bỏ mệnh đề theo-model mất 0 lượt đo» (V11160)

- **Chỗ gốc:** chú thích V11160 trong `gpt_analyzer.py` · `REPORT_V11160.md`
- **Nguyên văn câu sai:** *«bỏ mệnh đề theo-model mất 0 lượt đo»*
- **Điều đúng:** **mất đúng 1 model.** `gpt-oss-120b` **không có lượt `shadow_auto_eval` nào** ngày
  04/09 (lượt cuối `2026-08-01T05:20:52`) ⇒ cohort prompt ngữ cảnh thuần **tụt 12 → 11 model**. Và
  nó **không có đường quay lại** vì không nằm trong `SHADOW_AUTO_EVAL_MODELS` — sự kiện cần kiểm
  **sẽ không tự xảy ra** ở các ngày sau.
- **Quyết định đã dựa trên:** biện minh cho cách vá V11160. Bản vá **vẫn đúng**, nhưng cái giá của
  nó **đã bị khai bằng 0 trong khi thực tế là 1 model**.

#### R5 — «`promotion_bucket` không có reader»

- **Chỗ gốc:** báo cáo nợ V11163 · `FOLLOW_UP_TRACKER`
- **Nguyên văn câu sai:** *«promotion bucket không có reader»*
- **Điều đúng:** **SAI.** Có `SELECT` sống ở `_v11155_vai_tro_theo_thoi_diem.py:135`, thêm
  `_materialize_multi_lane_shadow_p0.py:3038` và index `idx_smps_bucket`. Mệnh đề «không reader»
  **chỉ đúng cho `output_counterfactual_rank`** (7 dòng mã sống, 0 `SELECT`).
- **Quyết định đã dựa trên:** không có quyết định nào — nhưng đây đúng họ lỗi **RM-20** (*«0 dòng
  mới» ≠ «không ai đọc»*), tức một RM **đã tái phạm**.

#### R6 — Câu tôi nói với owner trong chính phiên này (~21:5x, trong IDE)

- **Nguyên văn câu sai:** *«probe không phát hiện được hỏng ở tầng fd — đúng hình dạng
  `fd1=fd2=socket` của production»*
- **Điều đúng:** phản biện độc lập đã **thu hẹp phạm vi**: probe mù với **PIPE mất đầu đọc**,
  **KHÔNG mù** với **socket journald** của production. Mức nghiêm trọng thấp hơn tôi đã nói.
- **Quyết định đã dựa trên:** không có — nhưng owner đã đọc câu sai, nên phải rút lại **đúng chỗ
  đã nói**.

---

## 5 · Đã làm gì

| việc | TRƯỚC | SAU |
|---|---|---|
| bằng chứng ngày live | chưa đóng băng | **GATE 0 manifest** `ad25492b…`, 196 artifact, index `b9e23273…` |
| tái lập TOTAL từ raw | chưa từng làm cho ngày live | **30/30 hàng · 81/81 trọng số · 3-càng 3/3** |
| ma trận prompt | mẫu 1 model | **toàn bộ 84 lượt**, 5 kiểm bắt buộc cho `gpt-oss-120b` |
| vũ trụ model | «57 nguồn» | **63 danh tính**, 20 trường mỗi danh tính |
| `_safe_stdio_ctx` | «chưa từng chạy» *(sai)* | **270 dòng lịch sử** + 14 phép fault injection, 4/4 ổn định |
| sổ nợ | rải rác | **32 dòng**, map hết vào FU-449/FU-450, **0 FU mới** |
| gói A/B/C | V11163, hai lớp NULL | **bốn lớp NULL**, tiền lệ ghi đè 31.934 dòng, ba lỗ hổng của B |
| rút lại | 0 | **6 ca**, đủ bốn phần |
| production | `0/17.121` | **`0/17.121` — không đụng** |

**Cách chạy:** 8 cổng song song, mỗi phát hiện đi qua **một agent phản biện độc lập** được lệnh
mặc định hoài nghi và tự kiểm bằng đường khác. **32 phản biện: 7 `DUNG` · 25 `DUNG_MOT_PHAN` ·
0 `SAI`.** Mọi hiệu chỉnh của phản biện **đã áp vào bản này** — ví dụ `88/88` → **`86/86` đo được**,
`50.670` → **`50.658`** ký tự, G7-F3 hạ từ `PROVEN_DEFECT` → `OPERATIONAL_IMPROVEMENT`, phạm vi
G7-F1 thu hẹp khỏi socket journald.

---

## 6 · Cổng kiểm — xác minh

| cổng | kết quả |
|---|---|
| production DB row mutation | **0** — mọi kết nối `mode=ro` |
| `neo558` trước/sau | **KHỚP TỪNG KÝ TỰ** `a82c508d3569abda…` |
| 6 bảng khoá trước/sau | **y hệt** |
| `output_counterfactual_rank` | **`0/17.121`** trước và sau |
| PID · NRestarts · start | `3370750` · `0` · `01:08:40` — **không đổi** |
| health endpoint | **200** |
| tệp code sửa trong phiên | **0** |
| deploy / restart trong phiên audit | **0** |
| git commit / push của agent trong lúc soi | **0** |
| Notion | **0 ghi** (§57.1) |
| FU / Plan / Prompt mới | **0** |
| bản sao audit | `integrity_check = ok`, khớp gốc |
| phản biện độc lập | 32/32 chạy · **0 phát hiện bị bác hoàn toàn** |

---

## 7 · Vướng vấp — lỗi tự gây, bài học

| # | vấp | gỡ thế nào |
|---|---|---|
| 1 | **Workflow lần 1 chết sau 4 phút**, 6 agent mất trắng công | thêm luật *«ghi artifact sớm và nhiều lần»* vào nền chung; chạy lại → 40/40 agent xong |
| 2 | **Backtick trong template literal** JS làm hỏng cú pháp workflow | thay bằng nháy đơn |
| 3 | **Ghi lại file bằng Python trên Windows đẻ ra 446 ký tự `\r`** ⇒ tool từ chối | ghi với `newline=""`; đây đúng họ lỗi đã có trong bộ nhớ *(no-python-escapes-in-heredoc)* mà vẫn vấp |
| 4 | **Đọc `journal.jsonl` bằng đường dẫn `/c/...` trong Python** → `FileNotFoundError`, suýt kết luận «không có journal» | dùng đường dẫn Windows |
| 5 | 🔴 **Cửa sổ bằng chứng hẹp hơn cửa sổ kết luận** (R3) — quét journal (từ 29/08) rồi kết luận cho **cả đời** nhánh mã | phải quét `scheduler_logs` (từ 27/03). **Bài học chung: trước khi nói «chưa từng xảy ra», phải nói rõ NGUỒN đó phủ tới đâu** |
| 6 | Tôi báo owner *«đang chạy»* trong khi tiến trình đã chết | kiểm journal thật trước khi báo tiến độ |

---

## 8 · Gỡ về — rollback

**Không áp dụng** cho phần audit: **0 ghi production · 0 deploy · 0 restart** trong phiên soi.

Phần deploy của ngày (V11160–V11163, trước 01:08:40) đã có đường gỡ riêng trong báo cáo của chính
các bản đó. Bản V11164 này **không thêm bất kỳ thay đổi runtime nào** cần gỡ.

Artifact và bản sao audit nằm ngoài đường phục vụ, xoá lúc nào cũng được:
`artifacts/v11164_*` (196 tệp) và `artifacts/v11164_audit.db`.

---

## 9 · Theo dõi tiếp

| # | việc | ai chặn / chặn ở đâu | trạng thái |
|---|---|---|---|
| 1 | **Owner chọn A / B / C** | **OWNER** — cổng đã `READY_FOR_OWNER_DECISION` | `CHỜ_OWNER` |
| 2 | **Khoá ngưỡng đăng ký trước MT** | **OWNER** — nhưng agent báo `NOT_READY_FOR_OWNER_LOCK`, nên **đề nghị chưa khoá** | `CHỜ_OWNER` |
| 3 | 🔴 **Kế toán trần MT-13 tách khỏi «trượt gate»** — đang loại MT khỏi đo lường chính 71 ngày liên tiếp | chạm `day_governance` ⇒ cần owner duyệt | `CHỜ_OWNER` · FU-449 |
| 4 | 🔴 **`gpt_analyzer.py:6738` còn định tuyến gói ngữ cảnh theo MODEL** | chạm đường official ⇒ cần owner duyệt | `CHỜ_OWNER` · FU-450 |
| 5 | 🔴 **Vân tay prompt băm thiếu 51,8% chuỗi** — chuyển băm xuống sau khi nối `ctx_pack`/RULEBOOK | chạm `gpt_analyzer.py` | `CHỜ_OWNER` · FU-450 |
| 6 | **Bộ 5 dấu ô nhiễm có điểm mù `Win Rate`** | cùng chỗ mục 5 | `CHỜ_OWNER` · FU-450 |
| 7 | **`consensus_level` đếm voter thô, không de-dup huyết thống** | chạm `main.py:10339` | `CHỜ_OWNER` · FU-449 |
| 8 | **stdout service bị đệm khối** — journal trễ tới 23 giờ, mù kênh chẩn đoán | không chạm dự đoán; cần restart để sửa ⇒ ngoài phạm vi | `CHỜ_OWNER` · FU-450 |
| 9 | **Ba tệp điều hướng lệch 14 ngày** + bộ sinh `_v11083` chưa nối hook | có thể đóng ở phiên sau bằng canonical generator (snapshot → dry-run → diff → validate) | `ĐANG_LÀM` · FU-449 |
| 10 | **Sổ rút lại cũ 17 ngày** — bản này thêm **6 ca** | đóng ngay trong phiên này | `ĐÃ_LÀM` |
| 11 | **Nợ báo cáo 40/240**, `V11156` thiếu hẳn | đóng dần, không bịa nội dung (RM-17) | `ĐANG_LÀM` · FU-449 |
| 12 | **111 ô role-at-time thiếu L3** | đóng bằng **ghi hạn chế phạm vi**, cấm bù dữ liệu | `ĐANG_LÀM` · FU-450 |
| 13 | **`prediction_trace` không tự khai loại lượt** | cần thêm trường ⇒ chạm writer | `CHỜ_OWNER` · FU-450 |
| 14 | **Bất đối xứng telemetry** — vế official không có mẫu số | cần đổi cách ghi lane official | `CHỜ_OWNER` · FU-450 |
| 15 | **Nội dung `ctx_pack` chưa đo** — phần lớn nhất ngoài vùng băm | phải chứng minh `build_context_pack()` không ghi DB trước khi gọi | `CHỜ_OWNER` |

---

## 10 · TRẢ LỜI THẲNG 10 CÂU

**1 · Cả ba lượt MN/MT/MB 04/09 có thực sự chạy trên code sau fix không?**
**CÓ — chứng minh được, không phải tin.** 10/10 tệp trọng yếu có `mtime` **trước** `01:08:40`;
service khởi động `01:08:40`; `NRestarts 0`; PID `3370750` không đổi suốt ngày. Lượt sớm nhất là
MN `05:00:07`. Không có deploy hay restart nào sau đó.

**2 · Official và shadow có nhận đúng prompt regime không?**
**CÓ, 60/60 lượt.** 27/27 official → `LEGACY_PROMPT`; 33/33 shadow → `CONTEXT_ONLY_V2`; 0 FAIL.
`gpt-oss-120b` — model từng rò ngày 03/09 — nay `LEGACY_PROMPT` cả ba miền, có 2 dòng journal xác
nhận. **0/3 bundle có voter thuộc nhóm `CONTEXT_ONLY_V2`.**

**3 · Có prompt contamination nào còn tồn tại không?**
**KHÔNG chứng minh được là hết — và đây là câu phải trả lời thẳng: `PROMPT_CLEAN_NOT_PROVEN`.**
Ba lý do: ① vân tay chỉ băm **48,2%** chuỗi thật, phần `ctx_pack` + RULEBOOK + contract
(**26.223 ký tự**) nằm **ngoài** phép đếm; ② `gpt_analyzer.py:6738` **vẫn định tuyến gói ngữ cảnh
theo MODEL**, nên `gpt-oss-120b` chạy official vẫn ăn gói của lane thí nghiệm — lệch **86/86** cặp
đo được trong 30 ngày; ③ bộ 5 dấu có **điểm mù** `Win Rate`. Nói *«đã sạch»* lúc này là **tự nâng
tầng**.

**4 · Có model nào empty, timeout, parse lỗi, late hoặc bỏ phiếu sai không?**
**KHÔNG, ở cả năm loại.** empty **0/81** (đo theo RM-09, đọc JSON ra list rỗng) · timeout cứng
**0/60** · parse lỗi **0/48** · late **0/81** · bỏ phiếu sai regime **0/3 bundle**.
⚠️ Một cảnh báo về **dụng cụ đo**, không phải về model: `bundle.hard_timeout_models` là **hằng số
`[]` viết cứng** (`main.py:10504`) ⇒ **không dùng được** làm bằng chứng «không timeout»; kết luận
trên dựa vào `finish_reason` và `timeout_or_fallback`.

**5 · TOTAL và FINAL của cả ba miền có tái lập chính xác không?**
**CÓ — 30/30 hàng top-10 khớp tuyệt đối**, cả số, điểm 4 chữ số thập phân **và** thứ tự voter;
81/81 hàng trọng số BT khớp; 3-càng `853/228/586` đúng. Năm tầng raw → override **không có điểm
lệch**. Tầng 5 (UI công khai) **không đo được** vì viewer-freeze — ghi là *không đo được*, không
ghi là *không lệch*.

**6 · Hôm nay có bất thường kỹ thuật đáng ngờ nào không?**
**Có ba, đều đã chứng minh, và không cái nào đổi số công bố hôm nay:**
① `gpt-oss-120b` nhận gói ngữ cảnh khác 7 model official còn lại và **bỏ phiếu top-1 vào bạch thủ
MN `53` và MB `86``;
② **journald mất toàn bộ dòng `print()` từ 16:53:48** ⇒ **cả cohort MB không có đối chứng journal**
— đây là lỗ thủng của chính kênh bằng chứng GATE 0 đã dùng;
③ **3 dòng trace lặp**, hai trong đó trùng **đúng giây** tạo bundle.
Cộng một quan sát chưa kết luận được: **MN có 9 model ra cùng bộ `{28,53}`** — vượt p90, chưa vượt
max lịch sử (n = 1 ngày, RM-04).

**7 · Có cải thiện vận hành thật nào sau fix không?**
**CÓ, và đo được trên nền chứ không phải cảm giác.** **0 output rỗng ở cả ba miền — ngày duy nhất
đạt 0/0/0 trong 12 ngày** (03/09 MN=2; 02/09 và 01/09 mỗi miền 1). Latency **max 300,1s — thấp
nhất trong 10 ngày** (nền 275–1084s). Scheduler **0 ERROR**. Hai model owner bắt hôm qua
(`deepseek-reasoner`, `glm-5.2`) **hết rỗng**. Định tuyến regime đã có **bằng chứng nội dung** thay
vì cờ tự khai.

**8 · Có tín hiệu dự đoán khả quan nào vượt quá dao động một ngày không?**
**KHÔNG.** BT 1/3 với n = 3 là `EXPLORATORY` thuần. Trên cửa sổ 60 ngày với nền đúng từng miền,
**không model nào vượt nền có ý nghĩa** — tái xác nhận V11116 (25/08). Ba dòng **dưới** nền thì
hai dòng sát biên và chưa hiệu chỉnh đa biến ⇒ **không đề xuất hành động nào**.
Nói ngắn: **hôm nay máy chạy tốt hơn hẳn, còn chất lượng dự đoán thì chưa có gì để mừng.**

**9 · Những debt nào đã đóng, còn mở hoặc bị báo cáo sai trước đây?**
- **Đã đóng:** role-at-time vào production (`PARTIALLY_CLOSED`, còn 11 ô lệch = 2,04%) · lineage
  3-càng 8/8 trường · định tuyến regime prompt (`RUNTIME_PROVEN`) · hai model rỗng.
- **Báo cáo SAI trước đây — 5 ca rút lại ở mục 4.3**, nặng nhất là *«nhánh `_safe_stdio_ctx` chưa
  từng chạy»* (thật: **270 dòng**, 05–07/2026) và *«`promotion_bucket` không có reader»* (thật:
  **có `SELECT` sống** — RM-20 tái phạm).
- **Còn mở, và một món đang xấu đi:** nợ báo cáo **tăng** 38/232 → **40/240**; ba tệp điều hướng
  lệch **14 ngày**; sổ rút lại cũ **17 ngày**; briefing đầu phiên **đứng im 19 ngày**;
  **152/194** mục quá hạn.

**10 · Facts hiện tại có thay đổi đánh giá A/B/C hay chưa?**
**Có thay đổi FACTS, không thay đổi KHUYẾN NGHỊ.** Ba dữ kiện mới: ① rủi ro của **A** nay có
**tiền lệ thật** (17.001 dòng bị viết lại trong một đợt, 31.934 dòng bị ghi đè trong đời bảng);
② `NULL` mang **bốn** lớp, không phải hai; ③ **B không phải «không làm gì»** — artifact dừng ở
03/09, chỉ lưu top-10 nên **420 hạng bị cắt cụt**, và trường tên `hang_cua_no_trong_A` là `NULL`
**973/973**. Vẫn **0 reader**, writer **vẫn** bind `None` vô điều kiện.
⇒ **`READY_FOR_OWNER_DECISION`**. Agent **nghiêng về B** — và câu này **KHÔNG được đọc thành
`OWNER_LOCKED`**.

---

## 11 · Grand Overhaul chain status *(output 16)*

> ## **`PARTIAL`**

| cổng | tầng |
|---|---|
| GATE 1 region ledger · GATE 3 model universe · GATE 4 TOTAL/FINAL · GATE 5 anomaly · GATE 7 stdio · GATE 8 A/B/C | `EVIDENCE_COMPLETE` (6) |
| GATE 2 prompt routing · GATE 6 debt | `PARTIAL` (2) |

**Vì sao không phải `EVIDENCE_COMPLETE`:** GATE 2 còn hai mệnh đề chưa đóng được bằng bằng chứng
(`gpt-oss-120b` shadow `INDETERMINATE_NOT_EXERCISED`; nội dung `ctx_pack` chưa đo); GATE 6 không
được phép **đóng** dòng nợ nào bằng hành động vì luật cứng của phiên cấm ghi tài liệu trong lúc soi.

---

## 12 · Câu hỏi chưa giải *(output 17)*

1. **Nội dung `ctx_pack` có chứa dấu ô nhiễm không** — `INDETERMINATE`. Phải gọi
   `build_context_pack()` trên hàm đang serve, mà chưa chứng minh được nó **không ghi DB**.
   **Đây là việc phải làm trước khi bất kỳ ai nâng `PROMPT_43_R1` khỏi `PARTIAL`.**
2. **Ảnh hưởng định lượng của gói ngữ cảnh lệch lên số của `gpt-oss-120b`** — `NOT PROVEN`. Đo được
   prompt khác và nó bỏ phiếu top-1; **không** chứng minh được lá phiếu **khác đi vì** prompt khác.
   Đối chứng nào cũng phải gọi lại model **sau khi đã biết kết quả** ⇒ vi phạm cấm ORACLE.
3. **Vì sao `print()` ngừng vào journal từ 16:53:48** — `INDETERMINATE`. Đã loại trừ rate-limit
   tường minh. Giả thuyết có sức nặng: 9 module `_materialize_*` gán lại `sys.stdout` ở **mức
   module**, lần gán thứ hai đóng `BufferedWriter` dùng chung (tái lập 4/4). **Chưa** chứng minh
   được hai trong 9 module cùng được nạp trong tiến trình `3370750` — cần một endpoint chẩn đoán
   chỉ đọc.
4. **Tần suất thật của job `measurement_materialize`** — `INDETERMINATE` (xem R1).
5. **Combo-super MB gồm những model nào** — `INDETERMINATE`. Journal in dòng `UNIFIED` cho MN và
   MT nhưng **không** cho MB.
6. **11 ô lệch (2,04%) của đối chiếu L1∩L3 vs L2** — chưa có nguyên nhân.
7. **Sự kiện 13/04/2026**: ba model shadow/retired bỏ phiếu vào bundle official qua
   `run_source='manual'` — **sự thật đo được**, nhưng chưa dựng lại được **chính sách đương thời**
   nên **không gọi là vi phạm** (RM-13).
8. **Ai là người đọc thật của `output_counterfactual_rank`** — chỉ owner trả lời được.
9. **Ngữ nghĩa đích ở mức grain nào** — bốn khoá owner đã chốt loại trừ đúng, nhưng chưa nói một
   dòng lưu hạng của cái gì khi một model ra tới 2 số. Diễn tập V11163 **tự chọn `main_number`** —
   đó là lựa chọn của agent, **chưa được owner xác nhận**.
10. **Tần suất thực tế của ca đua luồng G7-F2** — chứng minh được nó **xảy ra được**, chưa đếm được
    bao nhiêu lần/ngày; đếm được thì phải sửa mã.

---

## 13 · Commit *(output 18)*

| | |
|---|---|
| private HEAD **trước** | `6243211b0d8615eca7d77f2785304ec41fa3c190` (branch `fu438/admin-only-p0a`) |
| public HEAD **trước** | `a430a720796bde27bd2a7900ebda38f335980545` |
| private commit V11164 | *(ghi ở `CONVERSATION_CONTEXT`, cập nhật ngay sau khi push)* |
| public commit V11164 | *(nt)* |
| `governance_seq` | 479 → **480** |

---

## Nguồn ba lớp (§62)

### `OWNER_SAID`
- 04/09 ~20:5x — **PROMPT 43 R1 · EOD LIVE CLOSURE AFTER V11163**, nguyên văn ràng buộc:
  *«Không dùng câu "production 0 mutation" nếu thực tế đã có code deploy/restart. Phải dùng nhãn
  chính xác cho từng loại.»* · *«Không được diễn giải "Agent nghiêng về B" thành OWNER_LOCKED.»* ·
  *«Nếu một claim không có raw evidence: ghi NOT PROVEN hoặc INDETERMINATE; không suy luận lấp chỗ
  trống.»*
- 04/09 ~21:1x — *«Xong chưa còn gì nữa không em?»*
- 04/09 ~21:5x — *«8 gate xong chưa em?»*
- 03/09 tối — *«làm xong chả báo cáo gì là sao em?»* (còn hiệu lực: cấm báo miệng không artifact)

### `CODE_DID`
- GATE 0 manifest `ad25492b889f570314eb935ae8b08103a3cb171ced72ddbbabe41f985c34e78f`;
  index 196 artifact `b9e232738d9bf85e1f965b363b0b202e4bd5fa4c9622f44c85ccf3c0d7a011fc`
- 10/10 tệp trọng yếu `mtime` < `2026-09-04 01:08:40`; PID `3370750`, `NRestarts 0`, health `200`
- `neo558 = a82c508d3569abda47041ad625cca93fdec2227fbe389c395dc7f139893a0e5f` **trước và sau**
- tái lập TOTAL 30/30 hàng · 81/81 trọng số BT · lô-3 93/93 · bundle 45/45
- `predictions` 04/09: 81 dòng · `prediction_trace` 60 dòng · 57 cặp ghép · 24 no-token × 3 miền
- prompt: 27/27 `LEGACY_PROMPT` (contam=4) · 33/33 `CONTEXT_ONLY_V2` (contam=0) · 60 sha256 khác nhau
- `gpt_analyzer.py:6738` `_shadow_mode = lane_test_shadow_pack or (selected_model in SHADOW_GATE_MODELS)`
- `scheduler_logs`: 270 dòng `I/O operation on closed file` từ `2026-05-10 12:01:21` đến
  `2026-07-19 17:30:00`; **0 dòng** từ `2026-08-01`
- writer scorecard chạy **3 lần** 04/09: VN `16:39:55` · `17:30:18` · `18:31:48`, mỗi lần
  `inserted=27`; cột vẫn `0/17.121`
- 32 phản biện độc lập: 7 `DUNG` · 25 `DUNG_MOT_PHAN` · **0 `SAI`**

### `DOC_SAID`
- `docs/DE_XUAT_MATERIALIZATION_V11163.md:86` ghi *«writer chạy 16:00·17:00·18:00·20:00»* —
  **`DOC_SAID` ≠ `CODE_DID`**, rút lại ở **R1**
- `REPORT_V11163.md §4` ghi *«nhánh đó chưa từng chạy»* — **`DOC_SAID` ≠ `CODE_DID`**, rút lại ở **R3**
- `scheduler.py:254` docstring *«if originals were valid»* nói **ngược** với mã (`saved` chỉ giữ
  bản **không** hợp lệ) — **`DOC_SAID` ≠ `CODE_DID`**, không có hậu quả hành vi
- `main.py:12306` chú thích *«For lo3 we clone official»* — đã ghi nhận sai từ commit `d411670`
  (07/05/2026) ở V11162, **giữ làm bằng chứng**
- `CLAUDE.md §52` mục 13 *«không đụng writer của `final_bundles`»* — là **một cánh cửa duy nhất**
  đang chặn **ba** món nợ khác nhau
- `CLAUDE.md` RM-20 dẫn `main.py:11881 :11918 :14923 :14935` — số dòng đã **trôi ~360**, nay là
  `:12244 :12281 :15390 :15402`

---

TanPhatAI cần làm: ghi **`V11164`** — `governance_seq 480`, công khai bản này. Ghi **8 cổng · 40 agent · 32 phản biện · 84 phát hiện (42 `PROVEN_DEFECT`) · 196 artifact · `INDEX_SHA256 = b9e232738d9bf85e1f965b363b0b202e4bd5fa4c9622f44c85ccf3c0d7a011fc`**. Ghi **MUTATION LEDGER đúng nhãn: ngày 04/09 CÓ 3 code deploy và CÓ 1 service restart, tất cả TRƯỚC 01:08:40 — cấm dùng câu «production 0 mutation» cho cả ngày; câu đúng là agent 0 ghi production DB và mọi lượt live chạy trên MỘT bản mã**. Ghi **SÁU CA RÚT LẠI (`PRJ-RETRACTION-001`, đủ bốn phần)**, nặng nhất là **R3 «nhánh `_safe_stdio_ctx` chưa từng chạy» — SAI, có 270 dòng lỗi thật từ 10/05 đến 19/07/2026; nhánh im từ 01/08 là nhờ V10800/V10826 tách job sang subprocess, KHÔNG nhờ `_safe_stdio_ctx`; quyết định «không sửa» GIỮ NGUYÊN nhưng lý do đổi hẳn**, và **R5 «`promotion_bucket` không có reader» — SAI, có `SELECT` sống ở `_v11155:135` ⇒ RM-20 TÁI PHẠM, cần cổng máy**. Ghi **TOTAL tái lập 30/30 hàng khớp tuyệt đối từ raw model output — số công bố đúng là số máy tính ra**. Ghi **`PROMPT_LANE_REGIME_FIXED` nhưng `PROMPT_CLEAN_NOT_PROVEN`**: vân tay chỉ băm **48,2%** chuỗi thật (thiếu 26.223 ký tự) và `gpt_analyzer.py:6738` **vẫn định tuyến gói ngữ cảnh theo MODEL** — lệch **86/86** cặp đo được trong 30 ngày, `gpt-oss-120b` bỏ phiếu top-1 vào bạch thủ công bố của MN và MB. Ghi **MT bị `EXCLUDE_PRIMARY` 72/90 lượt (80,0%) vì trần V10752 CỐ Ý bị kế toán chung với «trượt gate»** ⇒ **`MT_PREREGISTRATION` = `NOT_READY_FOR_OWNER_LOCK`, đề nghị CHƯA khoá ngưỡng**. Ghi **A/B/C = `READY_FOR_OWNER_DECISION`**, facts mới: **`NULL` bốn lớp (không phải hai)**, **tiền lệ ghi đè 31.934 dòng**, và **B KHÔNG phải «không làm gì» (artifact dừng 03/09 · 420 hạng cắt cụt · trường `hang_cua_no_trong_A` NULL 973/973)** — **agent nghiêng về B, CẤM đọc thành `OWNER_LOCKED`**. Ghi **nợ báo cáo §57 TĂNG 38/232 → 40/240, `V11156` thiếu hẳn thư mục**; **ba tệp điều hướng lệch 14 ngày**; **sổ rút lại cũ 17 ngày**; **briefing đầu phiên đứng im 19 ngày**; **152/194 mục quá hạn** — và **cấm trừ «94» với «152» vì hai thước khác nhau (RM-21)**. Ghi **`GRAND_OVERHAUL_CHAIN = PARTIAL`** (6 cổng `EVIDENCE_COMPLETE`, 2 `PARTIAL`). **Code KHÔNG đi trước tài liệu trong bản này** — 0 ghi production, 0 deploy, 0 restart trong phiên soi; bốn mặt ghi cùng phiên. **Không mở Prompt 44. Không mở FU mới. Không mở Plan mới.** `POOL_VERDICT` giữ **`HOLD`** · `MODEL_ACTION` giữ **`BLOCKED`** · `PROMPT_43_R1` giữ **`PARTIAL`**.
