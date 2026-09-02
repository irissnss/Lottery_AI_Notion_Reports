# REPORT V11152 — CỜ NGỮ CẢNH THUẦN **THEO LANE** · 02/09/2026

> # 🔴 RÚT LẠI — mục 3.2 của bản này SAI · ghi 02/09/2026 (`V11154`)
>
> **`PRJ-RETRACTION-001` — rút lại tại đúng chỗ đã công bố.** Bảng xếp hạng ở **mục 3.2** và
> mọi kết luận rút ra từ nó **KHÔNG DÙNG ĐƯỢC**. Đọc bốn phần dưới đây trước khi đọc mục 3.2.
>
> **① Chỗ gốc:** `REPORT_V11152.md` mục **3.2** *(«Bảng xếp hạng chung ĐẦU TIÊN — `would_flip`
> ròng, 90 ngày»)*, công bố **02/09/2026**, commit công khai `ace9365`. Cùng lỗi lặp lại trong
> mục **1**, **9** và dòng `TanPhatAI cần làm`.
>
> **② Nguyên văn câu sai:** *«5 nguồn dương · 19 nguồn âm… `gemini-3.6-flash` **−59** ·
> `claude-opus-5-fast` **−56** · `gpt-5-mini` **−54**»*, và trong trả lời IDE cùng ngày:
> *«Loại bỏ thì chứng minh được NGAY. `z = −6,48` · `p < 0,001`. Ba nguồn đáy bảng đã đủ bằng
> chứng để phán quyết hôm nay.»*
>
> **③ Điều đúng, tái lập được:** cột `would_flip_baseline_to_lose` **đếm cả dòng
> `reliability_status = 'MISSING_SHADOW_ROW'`** — tức những ngày model **KHÔNG HỀ dự đoán** vẫn
> bị tính là **thua**. Trong 90 ngày có **1.600 dòng `MISSING`**, trong đó **493 dòng bị cộng
> vào `lose`**. Bỏ chúng ra:
>
> | nguồn | đã công bố | đúng ra | |
> |---|---|---|---|
> | `gemini-3.6-flash` | −58 | **−6** | 52/70 lượt thua là **ảo** |
> | `claude-opus-5-fast` | −55 | **−5** | 50 ảo |
> | `gpt-5-mini` | −53 | **−1** | 52 ảo |
> | `gpt-oss-120b` | −52 | **0** | **toàn bộ** 52 lượt thua là ảo |
> | `glm-5.1` | −51 | **0** | **toàn bộ** ảo |
> | `qwen3.7-max` | −24 | **+7** | 🔁 **ĐỔI DẤU** |
> | `gemini-3.5-flash` | −27 | **+6** | 🔁 **ĐỔI DẤU** |
>
> Tính lại McNemar cặp đôi trên dữ liệu đã làm sạch: **0 nguồn tốt có ý nghĩa · 0 nguồn xấu có
> ý nghĩa · cả 20 nguồn đều «chưa phân biệt được với nhiễu»** (`|z|` cao nhất là `1,31`).
> Tái lập: `SELECT ai_model, SUM(...) FROM shadow_model_promotion_scorecard_daily WHERE
> reliability_status <> 'MISSING_SHADOW_ROW' AND run_source LIKE '%shadow%' …`
>
> **④ Quyết định đã dựa trên số sai:** kế hoạch *«`RETIRE` ba nguồn `z < −5`, bật lại
> `grok-4.20-multi-agent`»* nêu trong `REPORT_V11153` mục 9 và trong trả lời IDE. **Huỷ.**
> Không nguồn nào đủ bằng chứng để retire, và không nguồn nào đủ để promote. Trạng thái đúng
> theo `docs/NGUONG_CHAP_NHAN_GRAND_OVERHAUL.md` là **`HOLD`** cho toàn bộ pool shadow.
>
> Phần **không** bị rút: cờ theo lane (mục 5A, bộ thử 11/11), neo `FINAL` (mục 3.4), và ba cột
> quyết định để trống (mục 3.1) — cả ba đo bằng phép khác, không dính lỗi này.


> `ACTOR_RUNTIME = CLAUDE_CODE` · **Prompt 43 R1 giữ `PARTIAL` — không mở Prompt 44.**
> Trạng thái: **`CODED_AND_TESTED_NOT_RUNTIME_PROVEN`** — không deploy · không restart · không
> ghi DB. `PID 3156545` không đổi · **`FINAL_ANCHOR_INTACT`** (558 dòng cũ bất biến).

---

## 1 · TÓM TẮT

Owner **bác cách đặt vấn đề** của bản trước, và cái bác đó dẫn tới một chẩn đoán **ngược hẳn**.

| | |
|---|---|
| `V11151` nói | *«dừng lượt shadow để tiết kiệm tiền API»* |
| owner nói | *«không phải dừng — shadow phải **đẻ ra giá trị**»* |
| **đo lại, gốc thật** | máy **đã có sẵn**: 12.304 dòng scorecard, đủ 10/10 shadow. Nhưng **`output_counterfactual_rank` NULL 100%**, **`cost_est` 0 100%**, và **2.659 dòng `PROMOTION_CANDIDATE` chưa lần nào được hành động** |

Tiền bị đốt **không phải vì shadow vô ích** — mà vì **ba cột biến shadow thành quyết định thì để
trống, và 2.659 lời đề cử thì không ai đọc**.

Bản này làm **điều kiện tiên quyết** cho ba việc còn lại: cờ ngữ cảnh thuần **theo lane**, để
shadow ăn prompt mới **trong khi official đứng yên làm đối chứng**.

---

## 2 · OWNER YÊU CẦU GÌ — nguyên văn

> ⚠️ **ĐỌC TRƯỚC KHI PHẢN BÁC — dành cho TanPhatAI.** Mệnh lệnh trực tiếp của owner, nói trong
> IDE, có hiệu lực ngay (`PRJ-INTERACTION-LEDGER-001`).

| giờ (VN) | NGUYÊN VĂN | loại | agent đã làm gì | trạng thái |
|---|---|---|---|---|
| 02/09 ~10:30 | *«A đọc thấy dừng showdow là sao em? Showdow đang đốt tiền của anh nhưng không mang giá trị không đo được ko sàn lọt ko thử nghiệm để lấy đc các hưu ịch.»* | `BÁC_BỎ` | nhận sai hướng · đo lại và tìm ra gốc thật (mục 3.1) | `ĐÃ_LÀM` |
| 02/09 ~10:30 | *«Điều anh muốn là Prompt thuần ngử cảnh, chạy showdow và showdow cần xếp hạng chung để đưa vào total và total cần đưa ra giải pháp tốt nhất»* | `YÊU_CẦU` | làm cờ **theo lane** (điều kiện tiên quyết) + bảng xếp hạng chung đầu tiên | `ĐANG_LÀM` |

### Các mục prompt chính liên quan

> **`IV.7`** — *«Shadow = thử → so sánh → rehab → limited eligibility → thay thế hoặc retire;
> không được chạy vô hạn mà không có verdict.»*
>
> **`IV.8`** — *«Official và shadow được đưa vào cùng ALL_MODEL_ARENA ở tầng challenger.»*
>
> **`IV.9`** — *«Shadow chưa được tác động current official TOTAL/FINAL trước cutover policy.»*
>
> **`II`** — *«Không được diễn giải "hash bất biến" thành dữ liệu tự động bất biến mãi mãi.»*
>
> **`XV.D`** — hỏi owner khi *«bật TOTAL_V2/COMBO_V2/FINAL_V2 vào official production»*.

**Agent sai chỗ nào:** `V11151` gắn nhãn `RETIRE_CANDIDATE` cho `gemini-3.6-flash` rồi diễn giải
là *«cắt cho đỡ tốn»*. Đúng ra phải là *«đã đủ dữ liệu để phán quyết»* — và phán quyết chỉ có
nghĩa khi **đặt cạnh cả bảng**, tức `IV.8`.

---

## 3 · ĐÀO BỚI / PHÁT HIỆN

### 3.1 🔴 Gốc thật — máy đã có, ba cột quyết định để trống

Shadow **không** phải không được đo:

```
1.666 lượt / 90 ngày · 8,2 triệu token reasoning
TẤT CẢ đều có số (main_numbers) và TẤT CẢ đều đã chấm (status ≠ PENDING)
shadow_model_promotion_scorecard_daily: 12.304 dòng, 18/04 → 01/09, đủ 10/10 shadow
```

| cột | trạng thái |
|---|---|
| `output_counterfactual_rank` | 🔴 **NULL cả 12.304 dòng** — đúng cột xếp hạng shadow-vs-official |
| `cost_est` · `tokens_used` | 🔴 **0 cả 12.304 dòng** — dù `predictions.reasoning_tokens` có sẵn **8,2 M** |
| `promotion_bucket` | 🟢 đủ — `KEEP_WATCHING` 4.386 · `DROP_CANDIDATE` 3.482 · **`PROMOTION_CANDIDATE` 2.659** · `SUPPORT_ONLY` 1.777 |
| `would_flip_baseline_to_win` / `_lose` | 🟢 đủ — **1.097** / **1.524** |
| `reliability_status` | 🟢 đủ — nhưng **`MISSING_SHADOW_ROW` 3.296** dòng (27%) |

**Hệ đã nói *«nên đưa lên»* 2.659 lần, và không lần nào được hành động.**

### 3.2 Bảng xếp hạng chung ĐẦU TIÊN — `would_flip` ròng, 90 ngày

| | nguồn | lật THẮNG | lật THUA | **ròng** | lượt | token |
|---|---|---|---|---|---|---|
| 🟢 | `grok-4.20-multi-agent` | 35 | 24 | **+11** | 169 | 4.713.800 |
| 🟢 | `gpt-5.5` | 44 | 40 | **+4** | 255 | 1.427.233 |
| 🟢 | `qwen3.6-plus` | 16 | 14 | +2 | 94 | — |
| 🟢 | `deepseek-v4-pro` | 15 | 14 | +1 | 94 | — |
| 🟢 | `gemini-3.1-pro` | 18 | 17 | +1 | 95 | — |
| 🔴 | `gemini-3.6-flash` | 12 | 71 | **−59** | 264 | 270.130 |
| 🔴 | `claude-opus-5-fast` | 14 | 70 | **−56** | 272 | 180.633 |
| 🔴 | `gpt-5-mini` | 16 | 70 | **−54** | 271 | — |
| 🔴 | `gpt-oss-120b` | 0 | 53 | −53 | 173 | 622.739 |
| 🔴 | `glm-5.1` | 0 | 52 | −52 | 169 | 1.172.614 |

**5 nguồn dương · 19 nguồn âm.**

⚠️ **CHƯA được gọi là phán quyết** (`RM-04`): `+1`/`+2` trên ~94 lượt nằm **trong nhiễu**; chưa
có nền cho từng vế, chưa kiểm ý nghĩa, chưa tách trong/ngoài cửa sổ chọn
(`RM-18` · `PRJ-SELECTION-WINDOW-001`). Thành tựu ở đây là **đã có MỘT cái bảng chung** — đúng
`IV.8` — chứ không phải một lệnh thăng hạng.

⚠️ `glm-5.1` và `gpt-oss-120b` hiện **là official** (lên từ 01/08). Số âm của chúng là **dòng
shadow TRƯỚC khi thăng hạng** — không được đọc thành *«official đang kéo xuống»*.

### 3.3 Vì sao cờ toàn cục KHÔNG làm được điều owner muốn

`LLM_CONTEXT_ONLY_V2` (bản `V11150`) là **biến môi trường toàn cục**. Bật lên thì:

1. **official cũng đổi** ⇒ chạm đúng cổng `XV.D` owner giữ quyền ký;
2. **mất đối chứng** ⇒ không còn biết cải thiện đến từ prompt mới hay từ ngày hôm đó dễ.

Muốn *«prompt thuần ngữ cảnh, chạy shadow»* thì cờ **phải biết mình đang ở lane nào**.

### 3.4 🟡 Neo `FINAL` từng báo động giả — lỗi ở dụng cụ, không ở dữ liệu

Chạy lại neo sáng 02/09 ⇒ **`DRIFT`**. Điều tra:

```
[1] 558 dòng đầu theo id : hash a82c508d3569abda… == neo   ⇒ BẤT BIẾN
[2] mọc thêm             : 1 dòng — id=813 · 2026-09-02 · MN · bt=39
                           created 05:21:13 (cron bình thường)
[3] dòng cũ có updated_at sau mốc chụp : 0                  ⇒ không ai sửa ngược
```

**Không ai đụng dữ liệu cũ.** Bản nháp băm **cả bảng** nên **mọi ngày mới đều đọc thành drift** —
đúng điều owner cảnh báo ở mục `II`. Một cổng báo động mỗi sáng là một cổng **sẽ bị tắt trong
tuần**.

---

## 4 · HƯỚNG XỬ LÝ VÀ VÌ SAO CHỌN

**Vì sao làm cờ theo lane TRƯỚC ba việc kia.** Ba việc còn lại (điền `counterfactual_rank`, nối
`cost_est`, phán quyết vòng đời) đều là **đo shadow**. Nếu shadow vẫn ăn prompt cũ thì ta đang
đo **một thứ sắp bị thay** — công đo đó hỏng ngay khi Cutover. Cho shadow ăn prompt mới **trước**,
rồi mới đo, thì số đo đúng là số của thứ sẽ lên official.

**Vì sao official phải bất biến TỪNG BYTE, không phải «gần như không đổi».** Đây là đối chứng
duy nhất. Lệch một ký tự là lệch prompt, lệch prompt là lệch kết quả, và khi đó phép so
shadow-vs-official không còn nghĩa. Nên phép thử là **so `sha256`**, không phải so độ dài.

**Vì sao giá trị lạ ép về `off` chứ không báo lỗi.** Fail-closed: một biến môi trường gõ sai
(`LLM_CONTEXT_ONLY_V2_LANE=1`) **không được** vô tình mở prompt mới cho official.

---

## 5 · ĐÃ LÀM GÌ — trước / sau / phiên bản / kiểm (§60.4)

### A · `gpt_analyzer.py` — cờ theo lane

**TRƯỚC:**
```python
LLM_CONTEXT_ONLY_V2_ENABLED = os.getenv("LLM_CONTEXT_ONLY_V2", "0") == "1"
```
Một công tắc, hai lane cùng chịu.

**SAU:**
```python
LLM_CONTEXT_ONLY_V2_LANE = off | shadow | all      # giá trị lạ ⇒ ép `off`
def context_only_cho_lane(la_shadow) -> bool: ...
```
`create_analysis_prompt(...)` nhận thêm `context_only`; người gọi **biết lane thì phải truyền
tường minh** — hàm đó không tự đoán được nó đang phục vụ lane nào.
Tín hiệu lane: `lane_test_shadow_pack` ∪ `SHADOW_GATE_MODELS`.

**PHIÊN BẢN:** `gpt_analyzer.py` — commit riêng `0d1e0e7`. VPS **chưa nhận**.

**KIỂM — `_v11152_test_lane.py` 11/11:**

| phép | kết quả |
|---|---|
| ★ chế độ `shadow` ⇒ prompt **official bất biến TỪNG BYTE** so với `off` | ✅ cùng `sha256` |
| ★ chế độ `shadow` ⇒ prompt shadow **khác** và **ngắn hơn** | ✅ |
| ★ prompt shadow **hết** `HIỆU SUẤT THEO MODEL` · `ưu tiên patterns từ models` · `SỐ ĐÃ TRÚNG GẦN ĐÂY` | ✅ |
| ★ prompt official **vẫn còn** bảng xếp hạng — đối chứng nguyên vẹn | ✅ |
| chế độ lạ ⇒ ép `off`, **không** mở cho official | ✅ |
| tương thích ngược `LLM_CONTEXT_ONLY_V2=1` ⇒ `all` | ✅ |
| khôi phục nguyên trạng sau bộ thử (`RM-15`) | ✅ |

### B · `_v11152_neo_final.py` (MỚI) — neo tách ba phép

**TRƯỚC:** băm cả bảng ⇒ mọi bundle mới đọc thành `DRIFT`.
**SAU:** `[1]` 558 dòng đầu phải khớp neo (**cổng**) · `[2]` dòng mọc thêm chỉ **liệt kê** ·
`[3]` dòng cũ có `updated_at` sau mốc chụp phải bằng **0** (bắt **sửa ngược** — thứ `[1]` bỏ sót
vì sửa rồi sửa lại vẫn để dấu ở `updated_at`).

**KIỂM:** `FINAL_ANCHOR_INTACT` — xem mục 3.4.

### C · Emitter + cổng contamination — nhận `context_only`

Để quét được **từng lane** thay vì chỉ quét chế độ toàn cục.

---

## 6 · CỔNG KIỂM

| cổng | kết quả |
|---|---|
| `_v11152_test_lane.py` | ✅ **11/11** |
| `_v11150_test_contract.py` | ✅ **37/37** |
| `_v11150_contamination_gate.py --meta` | ✅ **17/17** |
| contamination · chế độ `off` | ✅ `CONTEXT_ONLY_FAIL` ×3 — **official đúng y nguyên** |
| contamination · lane `shadow` | ✅ **`CONTEXT_ONLY_PASS` ×3** (MN 48.226 · MT 48.088 · MB 49.867) |
| `_v11152_neo_final.py` | ✅ **`FINAL_ANCHOR_INTACT`** |
| `_v11062_nang_version.py --kiem` | ✅ `ĐẠT` · `governance_seq 468` |
| **cổng commit `_v11062`** | 🟡 **CHẶN đúng** — xem mục 7 |

---

## 7 · VƯỚNG VẤP

**🔴 Agent đặt sai vấn đề, owner phải chỉnh.** `V11151` viết *«việc đúng là dừng lượt shadow,
cái được là tiền API»*. Owner bác: *«không mang giá trị, không đo được, không sàng lọc, không
thử nghiệm để lấy được các hữu ích»*. Đo lại thì shadow **có** được đo đầy đủ — thứ thiếu là
**ba cột quyết định** và **hành động trên 2.659 lời đề cử**. Kết luận cũ **hướng về cắt giảm**;
kết luận đúng **hướng về khai thác**. Hai hướng ngược nhau hoàn toàn.

**🟡 Neo `FINAL` báo `DRIFT` giả.** Xem 3.4. Nếu báo thẳng cho owner thì đã là **báo động sai
lần thứ ba** trong hai ngày.

**🟢 Cổng commit chặn đúng.** Commit `0d1e0e7` đặt nhãn `V11152` mà **chưa ghi bốn mặt**. Cổng
`_v11062` chặn với `K1: V11152 không có dòng HISTORY`. Đã ghi đủ (`seq → 468`) rồi commit lại.
**Ghi lại đây để không ai đi gỡ cổng này** — nó vừa bắt đúng một lỗi thật của agent.

**🟡 Hook `PreToolUse` chặn cả lệnh ghép.** Gộp `bump` + `git commit` trong một lệnh thì hook
chặn **trước khi** `bump` chạy. Phải tách hai bước.

---

## 8 · GỠ VỀ

| thành phần | gỡ về |
|---|---|
| cờ theo lane | bỏ biến `LLM_CONTEXT_ONLY_V2_LANE` — mặc định `off`, **không cần deploy lại** |
| `gpt_analyzer.py` | `git revert 0d1e0e7` — VPS **chưa nhận** |
| `_v11152_neo_final.py` · `_v11152_test_lane.py` | xoá; **không** module production nào import |

**Không có gì trên production cần gỡ** — phiên này không deploy.

---

## 9 · THEO DÕI TIẾP

| # | việc | trạng thái | chặn ở đâu |
|---|---|---|---|
| 1 | ✅ prompt ngữ cảnh thuần chạy được trên lane shadow | **XONG** | — |
| 2 | **Điền `output_counterfactual_rank`** (NULL 12.304 dòng) | 🔴 tiếp theo | — |
| 3 | **Nối `cost_est` từ `reasoning_tokens`** | 🔴 tiếp theo | thiếu **đơn giá API** — owner chia sẻ được |
| 4 | **Phán quyết vòng đời từng shadow** (`VI.3`) | ⚪ Wave 2 | cần #2 và #3 |
| 5 | Đưa nguồn đủ mạnh vào `TOTAL_V2` | ⚪ Wave 3 | cần #4 |
| 6 | `reliability_status = MISSING_SHADOW_ROW` **3.296 dòng (27%)** | 🟡 `NOT_VERIFIED` | chưa truy nguyên nhân |
| 7 | `gpt-5.4` chạy **hai regime** ⇒ dedupe (`IV.14`) | 🔴 chưa xử | Arena |
| 8 | `combo-no-token` ngừng vote từ 01/08 mà vẫn chạy | 🟡 `NOT_VERIFIED` | — |
| 9 | `DOUBLE_COUNT` — `combo-super`/`smart-*` trong voters | 🔴 `PARENT_LINEAGE_PENDING` | Wave 3 |
| 10 | Adapter LLM tự sinh ranked top-K đúng hợp đồng | ⚪ Wave 1 còn lại | — |
| 11 | **Ngưỡng chấp nhận đăng ký TRƯỚC replay** | 🔴 **cần owner** | trước Wave 4 (`VII.1` · `RM-03`) |
| 12 | **3-càng** có pipeline hợp lệ không | ⚪ `XI` | nếu không ⇒ `NO_VALID_3CANG`, cấm chế số |
| 13 | **Cutover Packet** | ⚪ Wave 5 | **cổng D** — cần owner ký |
| 14 | Bảo mật / SSH / world-writable | ⚪ `CLASS C` | **cổng B** |
| 15 | 38/228 bản thiếu/không đạt báo cáo (`FU-444` 22 · `FU-447` 16) | ⚪ nợ CŨ | không bản nào của Grand Overhaul |

---

## §62 — BA LỚP NGUỒN

### `OWNER_SAID`

| giờ (VN) | nguyên văn | loại |
|---|---|---|
| 02/09 ~10:30 | *«A đọc thấy dừng showdow là sao em? Showdow đang đốt tiền của anh nhưng không mang giá trị không đo được ko sàn lọt ko thử nghiệm để lấy đc các hưu ịch.»* | `BÁC_BỎ` |
| 02/09 ~10:30 | *«Điều anh muốn là Prompt thuần ngử cảnh, chạy showdow và showdow cần xếp hạng chung để đưa vào total và total cần đưa ra giải pháp tốt nhất»* | `YÊU_CẦU` |

### `CODE_DID`

- `gpt_analyzer.py:872` `LLM_CONTEXT_ONLY_V2_LANE` + `context_only_cho_lane()` · `:2118`
  `_ctx_only` · `:6402` truyền `context_only` theo lane
- `_v11152_test_lane.py` → **11/11**, gồm phép **official bất biến từng byte**
- contamination: `off` ⇒ `FAIL` ×3 · lane `shadow` ⇒ **`PASS` ×3**
- `shadow_model_promotion_scorecard_daily`: `output_counterfactual_rank` **NULL 12.304/12.304**,
  `cost_est` **0/12.304**, `promotion_bucket = PROMOTION_CANDIDATE` **2.659**
- `_v11152_neo_final.py` → **`FINAL_ANCHOR_INTACT`** · 558 dòng cũ hash `a82c508d3569abda…`
- `PID 3156545` — **không restart, không ghi DB**
- commit riêng `0d1e0e7` + `902afc8`

### `DOC_SAID`

- `FU-450` mục 1 — nay ghi thêm: hành động đúng là **phán quyết vòng đời**, không phải *«cắt cho
  đỡ tốn»*. Con số *«1,8% lá phiếu»* đã rút ở `V11151`.
- Prompt `IV.8` — *«official và shadow cùng ALL_MODEL_ARENA»* ⇒ bảng ở 3.2 là **bước đầu**, chưa
  đủ (thiếu nền, thiếu kiểm ý nghĩa).

### `NOT_VERIFIED`

`reliability_status = MISSING_SHADOW_ROW` 3.296 dòng · đơn giá API từng model · phương pháp tính
`would_flip` của materializer hiện hành (**chưa soi**) · `combo-no-token` ngừng vote.

### Ba lớp lệch nhau ⇒ FINDING

**`OWNER_SAID` ≠ `CODE_DID`:** owner khoá `IV.7` *«shadow không được chạy vô hạn mà không có
verdict»*. Code **có** sinh verdict (`promotion_bucket`, 2.659 `PROMOTION_CANDIDATE`) nhưng
**không đường nào đọc verdict đó để hành động**. Verdict tồn tại mà không có hiệu lực —
đúng `RM-20` ở chiều ngược: **bảng được GHI nhưng không ai ĐỌC**.

---

TanPhatAI cần làm: ghi **`V11152`** — riêng `0d1e0e7` + `902afc8`, **không deploy**, official chưa đổi một ký tự. Ghi **owner BÁC BỎ cách đặt vấn đề của `V11151`**: không phải *«dừng shadow tiết kiệm tiền»* mà **shadow phải đẻ ra giá trị** — đây là **mệnh lệnh trực tiếp**, tài liệu cũ nói ngược thì tài liệu phải sửa. Ghi **gốc thật**: máy đã có 12.304 dòng scorecard nhưng **`output_counterfactual_rank` NULL 100%**, **`cost_est` 0 100%**, **2.659 `PROMOTION_CANDIDATE` không ai đọc** — verdict được GHI mà không ai ĐỌC (`RM-20` chiều ngược). Ghi **bảng xếp hạng chung đầu tiên** 5 dương / 19 âm — **CHƯA phải phán quyết** (`RM-04`), và **số âm của `glm-5.1`/`gpt-oss-120b` là dòng TRƯỚC khi thăng hạng**, đừng đọc thành «official đang kéo xuống». Ghi **cờ theo lane 11/11**, phép nặng nhất là **official bất biến từng byte**. Ghi **neo `FINAL` từng báo `DRIFT` giả** — là dòng thứ 559 (bundle MN hôm nay), 558 dòng cũ **bất biến**. Ghi **cổng commit `_v11062` đã chặn đúng một lỗi thật của agent** — **đừng gỡ cổng đó**. **Không mở FU mới** — umbrella `FU-449`/`FU-450`. **Không mở Prompt 44.**
