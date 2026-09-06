# REPORT V11169 — ĐÓNG NỐT VIỆC CÒN LẠI + GÓI DUYỆT OWNER

> **Ngày:** 06/09/2026 (VN) · `CURRENT_ACTOR = CLAUDE_CODE`
> **Model nhẹ:** 7 agent Sonnet (5 + 2 chạy lại) · **1,72 triệu token**
> **Kết quả: 7/13 mục đóng · `OWNER_APPROVAL_PACKET` 33 KB đã soạn · 1 ca rút lại**
>
> `POOL_VERDICT = HOLD` · `MODEL_ACTION = BLOCKED` · `PROMPT_43_R1 = PARTIAL`

---

## 1 · Tóm tắt

**Bốn kết quả đáng nhất, và một trong đó là rút lại con số của chính phiên trước:**

1. **«Cơ chế thứ 5» KHÔNG tồn tại** — đó là một **vụ nhầm phạm vi**. `_v10640` được ghi là
   «chỉ MN» nhưng thực tế điều khiển **cả MT và MB**.
2. 🔴 **Con số «73/79» KHÔNG tái lập được.** Đo độc lập ra **64/79 (81,0%)**. **Đã rút lại.**
3. **Đánh dấu 91 bundle backfill gần như MIỄN PHÍ** — 90/91 vẫn còn nguyên dấu
   `notes='Phase 1.5 backfill'`, chỉ cần một `SELECT`, không cần `ALTER`/`UPDATE`.
4. **MN 14 model hôm nay là RACE CONDITION 3 giây**, và **KHÔNG phải** ca lặp lại lỗi kế toán MT.

Và một phát hiện có hướng rõ ràng: **4 tệp shadow lệch sổ chính 153/270 dòng, trong đó
149/153 = 97,4% lệch theo MỘT hướng duy nhất — hướng làm số liệu ĐẸP HƠN.**

---

## 2 · Owner yêu cầu gì — NGUYÊN VĂN

| giờ (VN) | NGUYÊN VĂN | loại | agent đã làm gì | trạng thái |
|---|---|---|---|---|
| 06/09 ~10:0x | *«còn gì nữa ko tiếp tục đi em»* | `YÊU_CẦU` | Kiểm ngày live 06/09; chạy 5 cổng Sonnet; chạy lại 2 cổng hỏng schema | `ĐÃ_LÀM` |

---

## 3 · Đào bới / phát hiện

### 3.1 · 🔴 «Cơ chế thứ 5» — nhầm phạm vi, không phải cơ chế ẩn

Module `_v10640_official_perslice_override.py` (tên `v10640` từ ngày tạo **30/05/2026**) **thực tế
điều khiển cả ba miền** ở các thời điểm khác nhau, không chỉ MN như báo cáo trước ghi.

Bằng chứng: `git log` cho thấy `OVERRIDE_CONFIG` **đổi 7 lần**; gọi **thẳng** các hàm chooser còn
nguyên trong mã (`nt_consensus`/`no_token_combo_main` cho MT · `hot30`/`d_w06`/`prior_region` cho
MB · `d_w06` cho MN) trên dữ liệu thật cho thấy nó chạy liên tục **31/05 → 01/08** — **trước cả**
`V10767/89/90`.

**Đã loại trừ 4 giả thuyết thay thế** bằng đọc mã nguồn thật: `t10_chot` ghi đè · backfill/replay ·
writer thứ hai · `ranked` sắp xếp lại.

**Phát hiện phụ nghiêm túc:** bảng audit `v10767_mb_prevday_shadow` **chứa dữ liệu BACKFILL SAI** —
ghi **5–7 ngày sau** ngày chạy thật, `champion_bt` **không khớp** dữ liệu thật ⇒ **không dùng được
làm bằng chứng** cho các ngày trước khi module ra đời.

### 3.2 · 🔴 RÚT LẠI — «73/79» không tái lập được

Cổng chạy lại đo **độc lập** trên 79 bundle mismatch, mô phỏng **đúng thứ tự production** của 4 cơ
chế: khớp **64/79 = 81,0%** — `v10640` 44 · `v10789` 9 · `v10767` 6 · `v10790` 5.
Còn **15/79** không khớp: 4 ca không cơ chế nào kích hoạt, 11 ca **có** kích hoạt nhưng **ra số khác**.

Agent **tự bắt lỗi phương pháp trước khi báo**: lần chạy đầu patch `sqlite3.connect` **toàn cục**
gây **đệ quy vô hạn** và ra `0/79`; sửa bằng cách vô hiệu hoá đúng ba hàm `_log`/`_log_shadow`
thay vì patch toàn cục.

### 3.3 · MN `model_count=14` hôm nay — RACE CONDITION 3 giây

| | |
|---|---|
| cơ chế thật | `combo-super` ghi vào `predictions` lúc **05:26:05.288**, bundle 837 snapshot lúc **05:26:02** — **chậm đúng 3 giây** |
| số công bố | **vẫn HỢP LỆ** — bạch thủ `73` có 5 phiếu thật, chỉ thiếu đúng 1 phiếu lẽ ra có |
| không tự hồi phục | single-flight guard chỉ chặn regen **sau** mốc 15:40; MN chỉ chạy `auto_daily` **một lần/ngày** nên không có lượt «vét» ⇒ bundle kẹt ở 14 suốt ngày |
| tần suất 30 ngày | 15×23 · **14×6** · 13×1 — tức **20% số ngày** |
| **ba cơ chế độc lập** | (A) race timing *(hôm nay)* · (B) `parsed_numbers_empty` *(18/08 glm-5.1 · 01/09 gpt-oss-120b · 03/09 deepseek-reasoner)* · (C) model không chạy dòng nào *(22/08 · 26/08)* |

🟢 **KHÔNG phải ca lặp lại lỗi kế toán MT.** `day_governance` phân loại **ĐÚNG 5/5 ngày mẫu** vì
roster MN thật (`get_output_eligible_ids('MN')`) **= 15 = expected**, không có trần như MT
(V10752 chỉ cấp MT=13). Đây là điểm khác biệt quyết định.

### 3.4 · 🔴 Bốn tệp shadow lệch theo MỘT hướng — làm số liệu đẹp hơn

Đo 90 ngày: **153/270 (56,7%)** dòng `date × miền` **lệch** giữa 4 tệp shadow và `day_governance`
chính thức. Và **149/153 = 97,4% lệch theo MỘT hướng duy nhất**: shadow báo **`VALID_LIVE_DAY`**
(hoàn hảo) trong khi sổ chính ghi **`DEGRADED_LIVE_DAY`** (thiếu thật 1–2/15 model).

**Thiên lệch có hệ thống theo hướng làm đẹp, không phải nhiễu ngẫu nhiên.** Mức **P1**.

### 3.5 · Biên an toàn — vi phạm thật, nhưng ở MN chứ không phải MT

Đo lại bằng **đúng mốc `t10_chot`** (không dùng `final_bundles.created_at` theo `RL-018`):

- **MN: từ ~06/07 đến 31/07, `t10_chot` chạy ĐÚNG KHÍT giờ `OUTPUT_DUE` (15:45) — biên an toàn
  = 0 GIÂY trong 26/62 ngày.** Đây là vi phạm thiết kế thật. **Từ 01/08 (V10931) đã đổi lịch,
  khôi phục biên 5 phút, không còn vi phạm.**
- MT/MB: **không ngày nào dưới 120s** trong cả 90 ngày (biên nhỏ nhất quan sát = 180s).

⚠️ **Giới hạn phải ghi:** `scheduler_logs.log_time` cho `t10_chot` **luôn có giây = 00** — chỉ có
độ phân giải PHÚT. Nên trường hợp *«16:57:32, cách mốc 28 giây»* của MT **không thể xác nhận hay
bác bỏ** từ nguồn này.

### 3.6 · Đếm token — đóng 6 mục mà không cài gì

**Sự thật nền tảng chưa ai ghi:** `token_count`/`tokens` trong DB = `response.usage.total_tokens`
— **TỔNG prompt + completion**, KHÔNG phải `prompt_tokens` riêng. Grep toàn `web/backend` xác nhận
**không nơi nào** lưu tách.

Tỉ lệ ký tự/token đo **riêng từng model**, dùng `chars/(total_tokens − reasoning_tokens)` để loại
nhiễu reasoning. **Gộp theo provider bị BÁC BỎ** vì phương sai *trong* một provider (openrouter:
0,488–2,384, **gấp 5 lần**) lớn hơn phương sai *giữa* các provider — vi phạm RM-21/RM-18 nếu làm vậy.

**24/28 model ổn định** (CV ≤ 0,15, n = 59–462) + 3 tạm chấp nhận = **27 model quy đổi được**,
mỗi payload có **KTC95**. Ví dụ `official_MB` (55.178 ký tự) = **23.140–41.219 token** tuỳ model —
**chênh ~1,8 lần** giữa model tốn token nhất (`claude-opus-5-fast`) và tiết kiệm nhất (`grok-4.3`).

**Context window KHÔNG được thực thi ở runtime** — grep 6 mẫu = **0 kết quả**. Chỉ 5/28 model có
ghi chú **tài liệu** (~1M token), đủ để loại rủi ro vượt trần ở quy mô hiện tại (max ước lượng
**43.420** token vs ~1.000.000). **23/28 model còn lại: `INDETERMINATE`** — không có số trần nào
trong mã để đối chiếu.

Hai model cần điều tra riêng: **`grok-4.20-multi-agent`** (CV = **0,828**, nghi cộng dồn token
sub-agent) và **`gpt-5.6-sol-pro`** (tỉ lệ **0,488** ổn định nhưng lệch **3–5 lần** so với 27 model
khác — hoặc tokenizer phân đoạn rất nhỏ, hoặc OpenRouter báo sai đơn vị).

### 3.7 · RNG không gieo hạt — xác nhận bằng grep

`lstm_model.py`: **0** lần gọi `torch.manual_seed`/`np.random.seed`; `DataLoader:104` `shuffle=True`
không seed; `np.random.beta` mixup `:177` không seed.
`meta_learner.py`: **0** `random_state`; nhánh LightGBM (`:212-227`) có `bagging_fraction=0.8` và
`feature_fraction=0.8` — **cả hai đều ngẫu nhiên** — nhưng params **không có key seed** ⇒
**train lại sẽ ra MODEL KHÁC**. Riêng nhánh fallback `LogisticRegression(solver='lbfgs')` **thực tế
đã tất định**, không bị ảnh hưởng.

⇒ **Mọi so sánh «trước/sau retrain» đang trộn lẫn biến động dữ liệu với biến động ngẫu nhiên nội
tại của thuật toán.** Mức **P2**.

### 3.8 · Hai phát hiện mới

- **P2 · `shadow_model_promotion_scorecard_daily`:** **17.001/17.202 dòng (98,8%) ghi CHỈ TRONG
  MỘT NGÀY (03/09)**, trước đó chỉ ~1–2 dòng/ngày từ 04/2026.
  🟢 **Agent chính xác nhận: đây là backfill CÓ CHỦ ĐÍCH của V11158** (*«role-at-time vào production
  + recompute 540 ô»*, commit `6381c31` ngày 03/09) — **không phải bất thường**.
- **P2 · `model_latency_shadow_v11063`:** **TOÀN BỘ 5.427 dòng có CÙNG `created_at` chính xác đến
  giây** (`2026-09-05 21:50:02`) ⇒ đây là **MỘT SNAPSHOT TĨNH**, không phải dữ liệu tích luỹ hằng
  ngày như tên gợi ý. **Cảnh báo diễn giải sai** nếu coi là «dữ liệu sống».

**Ba mục kiểm ra SẠCH:** 3 model dừng đột ngột (`gemma-4-31b` · `grok-4.20-multi-agent` ·
`kimi-k2.5`) là **RETIRE CÓ CHỦ ĐÍCH, đã ghi tài liệu đầy đủ** (CHANGELOG dòng 18665/2918/15279) ·
**không có khoảng trống dữ liệu thật** trong 90 ngày (2/270 dòng thiếu đều là hôm nay đang chạy dở)
· `SESSION_SECRET` đã fail-fast từ V11049.

### 3.9 · `prompt_section_breakdown_daily` — telemetry ghi mà không ai dùng

**46.457 dòng (~4,3 MB)**, ghi đều **~290 dòng/ngày không đổi suốt 4,5 tháng**. Quét lại toàn
`web/backend`: **0 nơi ĐỌC NỘI DUNG** (chỉ 2 script audit thủ công đọc `COUNT/MIN/MAX` để kiểm
«còn ghi không»; `main.py` = **0 route**). Khác «bảng chết» — nó **vẫn đang được ghi**.
**Đề xuất** (chỉ đề xuất): cân nhắc dừng ghi để tiết kiệm ~27 KB/ngày. Mức **P3**.

---

## 4 · Hướng xử lý — `OWNER_APPROVAL_PACKET`

Gói **33 KB** đã soạn tại `OWNER_APPROVAL_PACKET.md`, theo đúng ba câu owner cần:
**① nếu duyệt thì chạy lệnh nào · ② nếu từ chối thì hậu quả gì · ③ cách gỡ về.**

**Mục A — 91 bundle backfill** *(tạo 30/03 sau khi biết kết quả, +9,8pp trên nền, nằm chung bảng
với số LIVE)*: 🟢 **90/91 vẫn còn nguyên dấu `notes = 'Phase 1.5 backfill'`** từ 30/03 đến nay —
nhờ `V17.1 FREEZE GUARD` chưa bao giờ ghi đè. ⇒ **Đánh dấu chúng gần như MIỄN PHÍ: chỉ cần một
`SELECT` lọc, không cần `ALTER` hay `UPDATE`.** Chỉ **1 dòng** (`id=93`) bị đổi notes thành
`'Admin manual trigger'`.

**Mục B — 32 nhãn `lo3 WIN` sai** *(57 lưu vs 25 thật, phóng đại 2,28 lần)*: SQL sửa chính xác +
cách gỡ về + số dòng bị chạm, kèm truy nguyên writer.

Agent cũng **tự bắt lỗi công thức của chính nó**: nền bạch thủ ban đầu dùng `1/D2` là **SAI**, sửa
thành `D2/100` mới khớp con số **34,0%** đã công bố ⇒ mọi con số nền trong gói đều đã kiểm chéo.

### Bản vá provenance *(ứng viên, CHƯA deploy)*

`artifacts/v11169_patch_provenance.py`: thêm **đúng 1 biến** `_selection_mechanism`, cập nhật trong
**chính các khối `if` đã tồn tại** khi chúng **thực sự** đổi bạch thủ, đổi **đúng 1 dòng cuối**.
**Không đụng** `bach_thu`/`lo2`/`lo3`/`xien2`/`xien3`/scoring.
Rủi ro **thấp** (chỉ gán biến quan sát); 3 điểm đọc `main_selection_reason` trong `main.py` đều là
**hiển thị**, không so sánh `==`. Gỡ về = revert đúng 1 dòng `:10379` + restart `lottery` + so PID.

---

## 5 · Đã làm gì

| việc | kết quả |
|---|---|
| «cơ chế thứ 5» | 🟢 **giải mã: nhầm phạm vi `_v10640`**, không phải module ẩn |
| 79 bundle | 🔴 **64/79 (81,0%)** tái lập được — **rút lại «73/79»** |
| MN 14 model | 🟢 **race condition 3 giây**, không phải lỗi kế toán MT |
| 4 tệp shadow | 🔴 **153/270 lệch · 97,4% theo một hướng làm đẹp** |
| biên an toàn | 🔴 **MN 0 giây trong 26/62 ngày** (06/07–31/07), đã sửa từ 01/08 |
| đếm token | 🟢 **27/28 model quy đổi được**, không cài gì |
| RNG | 🔴 **xác nhận không gieo hạt** ở LSTM + LightGBM |
| gói owner | 🟢 **33 KB**, 91 backfill **đánh dấu gần như miễn phí** |
| bản vá provenance | 🟢 ứng viên + test, **chưa deploy** |
| production | **0 ghi · 0 deploy · 0 restart** |

---

## 6 · Cổng kiểm — xác minh

| cổng | kết quả |
|---|---|
| DB production | mọi kết nối `mode=ro`; 3 hàm audit-log bị no-op **cục bộ** (không patch `sqlite3.connect` toàn cục sau khi phát hiện gây đệ quy) |
| `neo558` | **khớp** trước/sau |
| 6 hash tệp serve | **không đổi** |
| service | PID `3370750` · `NRestarts 0` · health 200 · load **0,05** |
| mô phỏng override | chạy **2 lần** — lần 1 sai phương pháp (0/79), lần 2 đúng (**64/79**) |
| công thức nền | tự phát hiện sai `1/D2` → sửa `D2/100`, khớp **34,0%** đã công bố |
| agent lỗi | 1/5 lần đầu (schema) → **chạy lại 2/2 thành công** |

---

## 7 · Vướng vấp

| # | vấp | gỡ |
|---|---|---|
| 1 | 🔴 **Trích «73/79» từ phiên trước mà không tái lập được** — số đúng **64/79** | rút lại ngay thay vì im lặng dùng số cũ |
| 2 | **Patch `sqlite3.connect` toàn cục** gây **đệ quy vô hạn**, kết quả ra `0/79` | tự phát hiện qua debug; sửa bằng no-op **đúng ba hàm** `_log`/`_log_shadow` |
| 3 | **Công thức nền bạch thủ dùng `1/D2`** — sai | sửa `D2/100`, khớp 34,0% đã công bố |
| 4 | **Một cổng chạy lần đầu trả rỗng** do `StructuredOutput retry cap` | chạy lại với schema đơn giản hơn (bỏ mảng lồng), **2/2 thành công** |
| 5 | **Gộp tỉ lệ token theo provider** là sai — phương sai *trong* provider gấp 5 lần | đổi sang đơn vị **model** (RM-21) |

---

## 8 · Gỡ về

**Không áp dụng** — phiên chỉ đo và soạn, **0 ghi production · 0 deploy · 0 restart**.
Bản vá provenance là **tệp mới** trong `artifacts/`, chưa áp dụng; gỡ về = revert 1 dòng `:10379`.
Gói owner **chỉ là văn bản**, chưa lệnh nào được chạy.

---

## 9 · Theo dõi tiếp

### Chặn ở owner

| # | việc |
|---|---|
| 1 | **Duyệt `OWNER_APPROVAL_PACKET`** — mục A (đánh dấu 91 backfill, gần như miễn phí) và mục B (sửa 32 nhãn `lo3`) |
| 2 | **Deploy bản vá provenance** (`main.py:10379`) — cần restart |
| 3 | **4 tệp shadow lệch 97,4% theo hướng làm đẹp** — sửa để đọc `day_governance` |
| 4 | **Gieo hạt RNG** cho LSTM + LightGBM — nếu không, mọi so sánh trước/sau retrain đều lẫn nhiễu |
| 5 | `gpt-5.6-sol-pro` tỉ lệ token lệch 3–5 lần — cần tài liệu OpenRouter hoặc một lần gọi thật |
| 6 | **Năm P0 hạ tầng của V11166 vẫn nguyên** |

### Còn treo

| # | việc |
|---|---|
| 7 | **15/79 bundle** chưa khớp (4 ca không cơ chế nào kích hoạt · 11 ca kích hoạt nhưng ra số khác) — cần đối chiếu bảng audit thật, **lọc theo `created_at` gần `run_date`** vì `v10767` có backfill sai |
| 8 | Chưa kiểm **V10883 connector** cho 15 ca còn lại |
| 9 | Chưa quét frontend xem có nơi nào so sánh chính xác chuỗi `main_selection_reason` |
| 10 | `grok-4.20-multi-agent` CV = 0,828 — cần một lần gọi thật để xem `usage` từng sub-agent |
| 11 | **23/28 model không có số trần** context window để đối chiếu |
| 12 | Chưa đo **% drift thực tế** khi train lại — cần phiên được phép chạy training |
| 13 | «28 giây ở MT» **không tái lập được** — `t10_chot` chỉ có độ phân giải phút |

---

## 10 · Nguồn ba lớp (§62)

### `OWNER_SAID`
- 06/09 ~10:0x — *«còn gì nữa ko tiếp tục đi em»*

### `CODE_DID`
- `_v10640_official_perslice_override.py` — tạo **30/05/2026**, `OVERRIDE_CONFIG` đổi **7 lần**
- `main.py:10379` — `main_selection_reason` chuỗi cứng, đặt **SAU** cả 5 khối đổi bạch thủ
- `lstm_model.py:104` `shuffle=True` không seed · `:177` `np.random.beta` không seed
- `meta_learner.py:212-227` LightGBM `bagging_fraction=0.8`/`feature_fraction=0.8`, **không key seed**
- 4 tệp shadow `:247` · `:160` · `:151` · `:170` — ngưỡng cứng
- `gpt_analyzer.py:3370/:3693/:3770/:4234` — lưu `usage.total_tokens`

### `RUNTIME_DID`
- `combo-super` ghi **05:26:05.288** vs bundle 837 **05:26:02** — chậm **3 giây**
- MN 30 ngày: `model_count` 15×23 · **14×6** · 13×1
- 4 tệp shadow vs `day_governance`: **153/270 lệch**, **149/153 = 97,4%** một hướng
- MN `t10_chot` **biên 0 giây trong 26/62 ngày** (06/07–31/07)
- `shadow_model_promotion_scorecard_daily`: **17.001/17.202 dòng ghi trong 1 ngày (03/09)**
- `model_latency_shadow_v11063`: **5.427 dòng cùng `created_at`**
- mô phỏng override: **64/79** — `v10640` 44 · `v10789` 9 · `v10767` 6 · `v10790` 5

### `DOC_SAID`
- Báo cáo trước ghi `_v10640` **«chỉ MN»** — **`DOC_SAID` ≠ `CODE_DID`**, nay xác định nó chạy **cả ba miền**
- CHANGELOG dòng 18665/2918/15279 — 3 model **RETIRE có chủ đích, đã ghi tài liệu**

### `NOT_VERIFIED`
- 15/79 bundle · V10883 connector · frontend đọc `main_selection_reason` ·
  `grok-4.20-multi-agent` · trần context 23/28 model · % drift retrain · «28 giây MT»

### `RETRACTED`
- **R24** «73/79 giải thích được» → **64/79 (81,0%)**, không tái lập được số cũ
- (còn hiệu lực) `RL-001`…`RL-023`

---

## 11 · Commit

| | |
|---|---|
| private HEAD trước | `ad2bfd51362f2d84c65afba1e3d20e46376ec06f` |
| public HEAD trước | `ce2bde6a457c21585fef9c514579148a78e22b19` |
| `governance_seq` | 483 → **484** |
| private commit | `101e239` · `fu438/admin-only-p0a` |
| public commit | `2b61987` · `main` |

---

TanPhatAI cần làm: ghi **`V11169`** — `governance_seq 484`, công khai bản này cùng `OWNER_APPROVAL_PACKET.md` và `REPORT_V11168.md`. Ghi **«CƠ CHẾ THỨ 5» KHÔNG TỒN TẠI — đó là VỤ NHẦM PHẠM VI**: `_v10640_official_perslice_override.py` được ghi là «chỉ MN» nhưng thực tế điều khiển **cả MT và MB** từ 31/05 đến 01/08, **trước cả** V10767/89/90. Ghi **MỘT CA RÚT LẠI `R24`: con số «73/79» KHÔNG tái lập được — số đo độc lập là 64/79 (81,0%)**; agent rút lại thay vì im lặng dùng số cũ. Ghi **bảng audit `v10767_mb_prevday_shadow` chứa DỮ LIỆU BACKFILL SAI** (ghi 5–7 ngày sau ngày chạy thật) ⇒ **không dùng làm bằng chứng**. Ghi **MN `model_count=14` hôm nay là RACE CONDITION 3 GIÂY** (`combo-super` ghi 05:26:05.288 vs bundle 05:26:02), số công bố **vẫn hợp lệ**, và **KHÔNG phải ca lặp lại lỗi kế toán MT** vì roster MN = expected = 15, không có trần. Ghi **BA cơ chế độc lập** gây `model_count=14` trong 20% số ngày. Ghi **4 TỆP SHADOW LỆCH SỔ CHÍNH 153/270 DÒNG, TRONG ĐÓ 149/153 = 97,4% LỆCH THEO MỘT HƯỚNG LÀM ĐẸP SỐ LIỆU** — thiên lệch có hệ thống, P1. Ghi **BIÊN AN TOÀN: vi phạm thật ở MN (0 GIÂY trong 26/62 ngày, 06/07–31/07), đã sửa từ 01/08 (V10931); MT/MB không ngày nào dưới 120s**; và **`t10_chot` chỉ có độ phân giải PHÚT** nên ca «28 giây» không xác nhận được. Ghi **ĐẾM TOKEN đóng 6 mục mà KHÔNG cài gì**: `token_count` trong DB là **`total_tokens` (tổng prompt+completion)**, không phải `prompt_tokens`; **gộp theo provider bị BÁC BỎ** vì phương sai trong provider gấp 5 lần; **27/28 model quy đổi được có KTC95**; **chênh tokenizer ~1,8 lần** giữa model tốn nhất và tiết kiệm nhất; **context window KHÔNG được thực thi ở runtime**, 23/28 model `INDETERMINATE`. Ghi **RNG KHÔNG GIEO HẠT** ở `lstm_model.py` và LightGBM ⇒ **mọi so sánh trước/sau retrain đang trộn nhiễu ngẫu nhiên nội tại**. Ghi **91 bundle backfill: 90/91 VẪN CÒN nguyên dấu `notes='Phase 1.5 backfill'`** ⇒ **đánh dấu gần như MIỄN PHÍ, chỉ cần SELECT**. Ghi **`model_latency_shadow_v11063` là SNAPSHOT TĨNH** (5.427 dòng cùng `created_at`), cảnh báo diễn giải sai. Ghi **17.001 dòng scorecard ghi trong 1 ngày 03/09 là backfill CÓ CHỦ ĐÍCH của V11158** — không phải bất thường. Ghi **agent tự bắt ba lỗi phương pháp của chính nó** (patch `sqlite3.connect` toàn cục gây đệ quy · công thức nền `1/D2` sai · gộp tỉ lệ token theo provider). **Code KHÔNG đi trước tài liệu** — 0 ghi production, 0 deploy, 0 restart. **Không mở Prompt 44. Không mở FU mới. Không mở Plan mới.**
