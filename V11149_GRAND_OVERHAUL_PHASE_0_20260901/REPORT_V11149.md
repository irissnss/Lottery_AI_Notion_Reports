# REPORT V11149 — **GRAND OVERHAUL · PHASE 0**: pool thật là **18 voter** không phải 27 · **KHÔNG có shadow leak** · trọng số **phẳng hơn** báo cáo trước

> **Ngày:** 01/09/2026 · `ACTOR_RUNTIME = CLAUDE_CODE` · **Phiên READ-ONLY với production**
> **Prompt 43 R1 giữ `PARTIAL` — không mở Prompt 44** · **Umbrella:** `FU-449` · `FU-450`

---

## 1 · Tóm tắt

Owner ra lệnh `GRAND OVERHAUL AFTER V11148`: **dừng chuỗi đo nhỏ giọt**, làm **một work package
tích hợp** thay kiến trúc dự đoán, **không hỏi giữa các Wave**, chỉ trình **một** Cutover Packet.

Bản này là **Phase 0 — nền đóng băng**, và nó đã **sửa hai con số của `V11148`**:

- pool bỏ phiếu thật là **18**, không phải 27
- tỉ số trọng số là **1,63× (MN)** / **2,08× (MB)**, không phải 3,87×

**Kết luận lõi vẫn đứng và còn nặng hơn**: weight đỉnh chỉ **0,0705–0,0726** trên cả ba miền.

Và một báo động P0 của chính agent đã **bị chính agent bác bỏ**: `SHADOW_LINEAGE_LEAK` là **dương
tính giả**.

---

## 2 · Owner yêu cầu gì — nguyên văn

> **01/09** — `PROMPT 43 R1 · GRAND OVERHAUL AFTER V11148`:
>
> *«Dừng chuỗi đo nhỏ giọt và report chủ yếu về D-30. Thực hiện một work package tích hợp để thay
> kiến trúc dự đoán hiện hành… Không cắt TOTAL. Phải làm lại TOTAL. Không hỏi Owner ký từng bước
> kỹ thuật. Chỉ trình đúng một Cutover Decision Packet sau khi package hoàn chỉnh.»*
>
> Mục `II` bắt buộc **sửa cách diễn giải `V11148`**: *«FINAL gần trung bình pool là diagnostic,
> chưa phải causal proof · Không dùng câu ±2 cả ba miền; MN tháng 08 lệch 4,69pp · Top-5 mean
> không phải kết quả gộp top-5 · Exact pool 27 phải được phân loại trước khi hành động.»*

⚠️ **TanPhatAI:** owner trao đổi liên tục trong IDE nên **code thường đi trước tài liệu** — điều
owner cho phép tường minh (`PRJ-INTERACTION-LEDGER-001`). Tài liệu cũ mâu thuẫn thực tế đang chạy
thì **thực tế + sổ tương tác thắng**.

---

## 3 · Đào bới / phát hiện

### 3.1 Bản chụp đóng băng (`III.1`–`III.3`)

```
chụp lúc      2026-09-01 22:04:16 +0700
PID           3156545 · health 200 · 93 cron bật
main.py       b618f0ed84ee152a   scheduler.py    2961987d8c3a6e27
combo_super   47047b1dc0b7e0b9   gpt_analyzer    4fc988bd2c23d22c
database.py   fd3d2349ab917c6f   strength_cal    44226fe9cc294163
mined_rule_eval 3216830f92b69705
DB            253 bảng · 761 MB
              predictions 13.958 · final_bundles 558 · model_daily_eval 13.822
              lottery_results 15.397 · mined_rules 105 · mined_rule_effectiveness 4.990
FINAL KHOÁ    558 bundle · 2026-02-28 → 2026-09-01
              hash bất biến a82c508d3569abda47041ad6…
```

`FINAL cũ` được **khoá bằng hash** — neo để mọi Wave sau chứng minh **không đụng** (`I.15`).

### 3.2 🔴 `III.4` — pool bỏ phiếu THẬT là **18**, không phải 27

Đo bằng **dấu vết thật, không tin registry**: quét danh sách `voters` trong `ranked_numbers` của
**270 bundle** (90 ngày × 3 miền).

- **57** nguồn từng chạy trong `predictions`
- **27** nguồn `RUNTIME_ACTIVE` (có output trong ≤ 2 ngày) ← con số `V11148` dùng
- **18** nguồn **thật sự xuất hiện trong `voters`** ← con số ĐÚNG

**18 voter thật:**
`claude-opus-4-20250514` · `claude-opus-4-6` · `claude-sonnet-4-6` · `combo-no-token` ·
`combo-super` · `deepseek-reasoner` · `gemini-2.5-flash` · `gemini-2.5-pro` · `glm-5.1` ·
`gpt-5-mini` · `gpt-5.4` · `gpt-oss-120b` · `lstm` · `meta-learning` · `random-forest` ·
`smart-ensemble` · `smart-ml` · `xgboost`

⚠️ Trong 18 voter này có **`combo-super`** và **`combo-no-token`** (HYBRID) cùng **`smart-ml`**,
**`smart-ensemble`** (ENSEMBLE) — tức **hybrid/ensemble đang được tính như voter độc lập cạnh
chính parents của nó**. Đây đúng là `DOUBLE_COUNT` mà owner nêu ở `I.11` và `IX.3`. **Đã ghi,
chưa xử** — thuộc Wave 3.

### 3.3 🟢 `III.5` — KHÔNG có `SHADOW_LINEAGE_LEAK`

**Phép đo thô đầu tiên của agent báo động sai.** Nó đếm tên model trong toàn bộ
`source_predictions_json` và cho ra **16 nguồn shadow "rò rỉ"** với `DIRECT_INFLUENCE = 270`.

**Kiểm lại:** blob là **dict 38 khoá**. Tên shadow nằm ở khoá **chẩn đoán** — `model_bt` ·
`model_wr` · `model_exclusion_reasons` · `diagnostic_empty_models` — tức **truy vết**, không phải
lá phiếu.

**Đo đúng chỗ (`voters`) trên 270 bundle: `0` model shadow.** Mọi shadow đều
`run_source = shadow_auto_eval`, đúng nhãn.

⇒ **KHÔNG có rò rỉ.** Đây là lần thứ tư trong ngày một phép **đếm chuỗi thô** suýt đẻ ra kết luận
sai (`RM-09`).

### 3.4 🟡 Sửa hai con số của `V11148` (owner mục `II` bắt buộc)

| `V11148` nói | đúng ra |
|---|---|
| «pool **27 model** cùng bỏ phiếu» | 27 `RUNTIME_ACTIVE`, **18 bỏ phiếu** |
| «tỉ số trọng số cao/thấp **3,87×**» | mẫu số sai. Trên 18 voter / 90 ngày: **MN 1,63×** · **MB 2,08×** · MT 5,70× |

**Kết luận lõi SỐNG SÓT và NẶNG HƠN:**

| miền | đỉnh | **w đỉnh** | đáy | w đáy | **tỉ số** | TB pool |
|---|---|---|---|---|---|---|
| MN | 50,00% | **0,0710** | 30,77% | 0,0437 | **1,63×** | 39,11% |
| MT | 43,82% | **0,0705** | 7,69% | 0,0124 | 5,70× | 34,54% |
| MB | 30,00% | **0,0726** | 14,44% | 0,0350 | **2,08×** | 22,96% |

Với **18** voter, chia đều là **0,0556**. Đỉnh được **0,0705–0,0726** ⇒ chỉ hơn mức đều **1,28×**.
Ở MN, model **50,00%** và model **30,77%** gần như **cùng tiếng nói**.

Theo owner mục `II.1`–`II.2`: câu *«FINAL ≈ trung bình pool ±2 cả ba miền»* là **diagnostic, chưa
phải causal proof**; và **MN tháng 08 lệch 4,69pp** nên **không được** dùng «±2 cả ba miền».

---

## 4 · Hướng xử lý

Phase 0 là **nền**, không phải thay đổi. Nó cung cấp ba thứ mọi Wave sau cần:

1. **Neo bất biến** cho `FINAL` cũ (`hash a82c508d3569abda…`) — chứng minh không đụng.
2. **Danh sách 18 voter chính xác** — `TOTAL_V2` phải chọn voter từ đây, không từ danh sách 27.
3. **Xác nhận không có shadow leak** — nên `ALL_MODEL_ARENA` (Wave 2) có thể nạp shadow vào
   challenger namespace mà **không** phải gỡ rối lineage trước.

---

## 5 · Đã làm gì

```
TRƯỚC:  V11148 nói "pool 27 model", "tỉ số 3,87×" — chưa ai kiểm ai THẬT SỰ bỏ phiếu
        chưa có neo bất biến cho FINAL cũ
SAU:    bản chụp đóng băng đủ 7 hash + DB counts + FINAL hash bất biến
        pool phân loại bằng DẤU VẾT: 57 từng chạy → 27 runtime-active → 18 bỏ phiếu
        SHADOW_LINEAGE_LEAK: báo động sai, đã tự bác bằng phép đo đúng chỗ
        hai con số V11148 đã sửa; kết luận lõi sống sót và nặng hơn
PHIÊN BẢN: KHÔNG deploy · KHÔNG restart · KHÔNG ghi DB · production không bị đụng
KIỂM:   mọi phép đo `sqlite3 -readonly` trên DB VPS (OWNER-02)
```

---

## 6 · Cổng kiểm

| cổng | kết quả |
|---|---|
| `NANG_VERSION_V11062` `K1..K4` | ✅ ĐẠT |
| nguồn đo | ✅ **DB VPS** `mode=ro` |
| production | ✅ **không đụng** — `PID 3156545` giữ nguyên |
| `FINAL` cũ | ✅ **khoá bằng hash** `a82c508d3569abda47041ad6…` |

---

## 7 · Vướng vấp

**🔴 Agent tự báo động P0 sai rồi tự bác trong cùng phiên.** Phép đếm tên trong blob cho 16 nguồn
"rò rỉ"; đo đúng chỗ (`voters`) cho **0**. Nếu công bố bản đầu thì đã báo owner một sự cố **không
có thật** — và tệ hơn, có thể kéo theo việc gỡ nhầm shadow khỏi hệ.

**🟡 Cổng chỉ-đọc của agent chặn nhầm vì chữ `update`** trong `khoa.update(...)` — mẫu cấm
`\\bUPDATE\\b` khớp không phân biệt hoa thường vào **mã Python**, không phải câu SQL ghi.

---

## 8 · Gỡ về

Phiên này **không thay đổi gì trên production**. Tài liệu: `git revert <SHA của V11149>`.

---

## 9 · Theo dõi tiếp — Wave 1 còn lại

| # | việc | mục lệnh |
|---|---|---|
| 1 | `UNIFIED_CANDIDATE_CONTRACT` | `IV` |
| 2 | Full emitter (thấy đủ `SYSTEM_PROMPT`) + `LLM_CONTEXT_ONLY_V2` | `V` |
| 3 | `ML_PURE_MATH_V2` | `VI` |
| 4 | `ALL_MODEL_ARENA` | `VII` (Wave 2) |
| 5 | `TOTAL_V2` · `COMBO_V2` · `FINAL_V2` · gỡ hidden override | `VIII`–`X` (Wave 3) |
| 6 | Replay + canary | `XII`, `XIII` (Wave 4) |
| 7 | **Một** Cutover Packet | `XIII` (Wave 5) |

**Không hỏi owner giữa các Wave** (lệnh `XIII`), trừ bốn ca: destructive schema/data · SSH/
credential · không có rollback · cần kích hoạt official.

---

## 10 · Nguồn ba lớp (§62) + `NOT_VERIFIED`

### `OWNER_SAID`
`PROMPT 43 R1 · GRAND OVERHAUL AFTER V11148` (01/09), 15 mục `I`–`XV`. Nguyên văn trích ở mục 2
và `docs/SO_TUONG_TAC_OWNER.md`.

### `CODE_DID`
Bản chụp 7 hash tệp lõi · `final_bundles` hash bất biến · quét `voters` trong `ranked_numbers`
của 270 bundle · `predictions.run_source` cho nhóm shadow · trọng số chuẩn hoá tính lại trên
18 voter — tất cả `sqlite3 -readonly` trên **DB VPS**.

### `DOC_SAID`
`CHANGELOG.md §V11149` · `docs/CURRENT_TRUTH_SSOT.md §V11149` ·
`docs/FOLLOW_UP_TRACKER.md → FU-449` (cập nhật Phase 0).

### `NOT_VERIFIED`

| mục | vì sao chưa |
|---|---|
| `combo-super`/`combo-no-token`/`smart-*` có double-count thật không | **đã thấy chúng nằm trong `voters`**, nhưng **chưa** truy parent lineage để chứng minh dùng lại inputs — Wave 3 |
| `TOTAL_V2` cho kết quả bao nhiêu | **chưa xây, chưa replay** |
| Vì sao pool `RUNTIME_ACTIVE` là 27 mà chỉ 18 vào `voters` | **chưa truy** cơ chế loại 9 nguồn còn lại — có thể là `output_eligible`, có thể là gate khác |
| Nguyên nhân nhân quả của «FINAL ≈ TB pool» | **diagnostic**, chưa phải causal proof — đúng như owner mục `II.1` |

---

TanPhatAI cần làm: ghi **Grand Overhaul Phase 0 xong**. Ghi **pool bỏ phiếu THẬT là 18, không phải 27** (57 từng chạy → 27 runtime-active → **18 trong `voters`**), đo trên **270 bundle**. Ghi **KHÔNG có `SHADOW_LINEAGE_LEAK`** — agent tự báo động 16 nguồn rồi **tự bác** bằng phép đo đúng chỗ; tên shadow chỉ nằm ở khoá **chẩn đoán**, `0` trong `voters`. Ghi **SỬA hai con số `V11148`**: «27 model» → **18 bỏ phiếu**; «3,87×» → **MN 1,63× · MB 2,08× · MT 5,70×**. Ghi **kết luận lõi sống sót và nặng hơn** — weight đỉnh **0,0705–0,0726**, chia đều là 0,0556, đỉnh chỉ hơn mức đều **1,28×**. Ghi **`FINAL` cũ đã khoá bằng hash `a82c508d3569abda…`**. Ghi **`combo-super`/`smart-*` nằm trong `voters`** ⇒ nghi `DOUBLE_COUNT`, **chưa chứng minh**, thuộc Wave 3. **Không mở FU mới** — dùng umbrella `FU-449`/`FU-450`.
