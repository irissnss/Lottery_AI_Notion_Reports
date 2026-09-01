# REPORT V11131 — ROOT CAUSE `gpt-5-mini` · XÁC MINH BỘ LỌC SHADOW · GIỚI HẠN ĐÚNG CỦA KẾT LUẬN

```
REPORT_VERSION        : V11131
REPORT_TITLE          : PHA A — PRE snapshot · root cause gpt-5-mini · xác minh bộ lọc shadow ·
                        phân định chính xác shadow trong FINAL blob
WORK_DATE_ICT         : 2026-08-27
PUBLISHED_AT_ICT      : xem mục bàn giao
TIMEZONE              : Asia/Ho_Chi_Minh / UTC+07:00
OWNER_DECISION        : prompt 43 R1 · D-25
ACTOR_RUNTIME         : CLAUDE_CODE
PREVIOUS_PUBLIC_HEAD  : b7c39008375ce04f1a07df2dd3d6234b24d095de
PRE_SNAPSHOT_HASH     : 085d4979a28d8187d607995c02786123790e1f414ea46ca9
LABELS                : WAIT_LIVE · RUNTIME_LOADED · SELF_CORRECTION · NOT_VERIFIED_PRESENT
```

---

## 1 · TÓM TẮT BẰNG LỜI THƯỜNG

Phiên này làm xong **PHA A** và mang về **hai đính chính cho chính báo cáo trước của tôi** — cả
hai đều quan trọng.

**Thứ nhất — `gpt-5-mini` KHÔNG phải model official.** Nó **đã rời official từ `2026-08-01`**,
26 ngày trước, và từ đó tới nay **100 % là `shadow_auto_eval`**. Nghĩa là:

> 🔴 **Con số «17 official» tôi công bố ở `V11130` là SAI.** Đúng phải là **16 official**
> + `gpt-5-mini` **đã ở shadow**. Trớ trêu: con số **16** của `V11128` **tình cờ đúng** — dù
> tôi đã bác nó ở `V11130` bằng một lập luận sai.

**Thứ hai — không có bằng chứng nào cho thấy model shadow đã đổi FINAL.** 11 model shadow **có**
tên trong `source_predictions_json` của cả ba bundle 27/08, nhưng đọc kỹ thì chúng chỉ nằm trong
**bảng thống kê 30 model** (`model_wr` / `model_bt`), **không** nằm trong tập bỏ phiếu (13–15
model) và **không** nằm trong `score_breakdown` — nơi ghi đóng góp điểm thật.

⇒ Nhãn đúng vẫn là **`SHADOW_ENTERED_COMBO_PATH`**. ⛔ **Không** được ghi `SHADOW_CHANGED_FINAL`.

**Và bản vá lọc shadow của `V11130` đã được xác minh hoạt động đúng** — sau khi tôi tự phát báo
động sai rồi tự bác nó.

---

## 2 · PHA A1 · PRE SNAPSHOT

| | |
|---|---|
| chụp lúc (**giờ máy chủ**) | **2026-08-27 23:27:23 +0700** |
| `snapshot_hash` | `085d4979a28d8187d607995c02786123790e1f414ea46ca9` |
| MainPID | **2694667** · chạy từ 22:53:01 · health **200** |
| `main.py` | `ec2540331be1…` |
| `scheduler.py` | `a6c8bfff60b6…` |
| `combo_super.py` | `47047b1dc0b7…` ← bản vá `V11130` |
| `gpt_analyzer.py` | `0d2be3247abf…` |
| `predictions` | `13573 \| 28423` |
| `final_bundles` | `543 \| 782` |
| `lottery_results` | `15364 \| 15468` |
| `model_daily_eval` | `13437 \| 13437` |
| **FINAL 27/08** | `MB:61:WIN · MN:61:LOSE · MT:68:WIN` |

⛔ **Từ lúc chụp tới 05:00 ngày 28/08: không deploy, không restart, không đổi official path.**

---

## 3 · 🔴 TỰ BÁC MỘT BÁO ĐỘNG CỦA CHÍNH MÌNH

Script snapshot của tôi báo `_ti_le_bach_thu` trả về **0 model ở cả ba miền** — nghe như bản vá
`V11130` đã làm rỗng bảng dự tuyển và sẽ **làm hỏng Combo lúc 05:00**.

**Sai. Lỗi ở script đo, không ở bản vá.** Chạy lại không cắt output:

```
TYPE dict · LEN 16
KEYS: claude-opus-4-6 · claude-sonnet-4-6 · combo-no-token · combo-super ·
      deepseek-reasoner · gemini-2.5-flash · gemini-2.5-pro · glm-5.1 · gpt-5.4 ·
      gpt-oss-120b · lstm · meta-learning · random-forest · smart-ensemble ·
      smart-ml · xgboost
```

Regex của tôi không khớp vì dòng `[INIT]` chen vào stdout. Truy vấn SQL chạy trực tiếp cũng trả
**16 dòng**.

### 🔴 Và điều nghiêm trọng hơn: **cổng deploy của `V11130` đã cho qua một cách RỖNG**

Ở `V11130` tôi kiểm bằng `"SHADOW_CON_LAI []" in output`. Điều kiện đó **đúng một cách vô nghĩa**
nếu toàn bộ dict rỗng — nó **không** phân biệt được *«đã loại shadow»* với *«mất sạch mọi model»*.

Đúng bài học `RM-15`: **một phép kiểm không có đối chứng dương thì luôn báo xanh.** Lần này bản vá
tình cờ đúng, nhưng **cổng thì đã hỏng**. Từ nay mọi cổng loại-trừ phải kèm **đối chứng dương**
(*«cái đáng giữ có còn không»*), không chỉ đối chứng âm.

**Kết quả xác minh lại — bản vá ĐÚNG:**

| | |
|---|---|
| model dự tuyển | **16** ở cả ba miền |
| model shadow còn lại | 🟢 **0** |
| `gpt-5-mini` còn dự tuyển | 🟢 **False** |

---

## 4 · PHA A2 · ROOT CAUSE `gpt-5-mini`

### 4.1 · Bằng chứng từ DB

| bảng | 7 ngày | 14 ngày | 30 ngày |
|---|---|---|---|
| `predictions` | 24 | 45 | 93 |
| `model_daily_eval` | 24 | 45 | 93 |

**`run_source` theo thời gian — đây là câu trả lời:**

| `run_source` | số dòng | khoảng ngày |
|---|---|---|
| `ai_chain` | 8 | **28/07 → 31/07** |
| `auto_daily` | 5 | **28/07 → 01/08** |
| 🔴 **`shadow_auto_eval`** | **80** | **01/08 → 27/08** |

### 4.2 · Đối chiếu với một LLM official bình thường

| model | `predictions` (7 ngày) | `model_daily_eval` (7 ngày) |
|---|---|---|
| `gpt-5.4` | `ai_chain, auto_daily` | `ai_chain, auto_daily` |
| **`gpt-5-mini`** | 🔴 **`shadow_auto_eval`** | 🔴 **`shadow_auto_eval`** |

### 4.3 · Chất lượng output — **không phải model hỏng**

**93 dòng · 0 rỗng · 0 late.** Không có alias trùng.

### 4.4 · Kết luận root cause

> **`gpt-5-mini` đã được chuyển sang shadow từ `2026-08-01`.** Nó có **0 lượt eval sạch** trong
> 7 ngày **không phải vì lỗi**, mà vì **nó vốn không còn ở đường official** từ 26 ngày trước.

**Vì sao tôi đếm nhầm nó thành official ở `V11130`:** phép đếm dùng cửa sổ **30 ngày** với
`run_source IN (auto_daily, ai_chain)`. Các dòng đó nằm ở **28/07–01/08** — tức **rìa cửa sổ**.
Cửa sổ 30 ngày quét ngược từ 27/08 chạm đúng vào đuôi giai đoạn official cũ của nó.

### 4.5 · VERDICT

## **`ALREADY_SHADOW_NO_ACTION`**

⛔ **Không** phải `MOVE_TO_SHADOW` — nó đã ở shadow 26 ngày rồi.
⛔ **Không** được gọi việc nó mất tư cách dự tuyển Combo là *«đã cắt model»*.
🟢 Nó vẫn chạy, vẫn được chấm, vẫn có đường quay lại — đúng nguyên tắc shadow.

### 4.6 · Roster official — con số đúng

| | |
|---|---|
| ~~17 official~~ (`V11130`) | 🔴 **SAI** |
| **16 official** | 🟢 **ĐÚNG** — 8 LLM_BASE + 4 ML_BASE + 2 ENSEMBLE + 2 HYBRID_COMBO |
| `gpt-5-mini` | **SHADOW từ 01/08** |

> `V11128` ghi **16** — **tình cờ đúng**, nhưng bằng lập luận sai (nhãn `n < 30`). `V11130` bác
> nó và ghi **17** — **sai**. Nay con số đúng là **16**, và lý do đúng là:
> **`gpt-5-mini` đã rời official từ 01/08.**

---

## 5 · SHADOW TRONG FINAL BLOB — PHÂN ĐỊNH CHÍNH XÁC

**11 model shadow** đều có tên trong `source_predictions_json` của cả ba bundle 27/08:
`gpt-5-mini` `gpt-5.5` `qwen3-max-thinking` `gemini-3.5-flash` `gemini-3.6-flash` `glm-5.2`
`grok-4.3` `deepseek-v4-pro-real` `claude-opus-5-fast` `qwen3.7-max` `gpt-5.6-sol-pro`

**Nhưng chúng nằm ở ĐÂU mới là câu hỏi đúng:**

| mục trong blob | MN | MT | MB | có shadow không |
|---|---|---|---|---|
| **`total_models`** — tập bỏ phiếu thật | **15** | **13** | **13** | — |
| `output_eligible_row_count` | 15 | 15 | 15 | — |
| `scoreable_model_count` | 15 | 13 | 13 | — |
| `quality_filtered_models` | 0 | 2 | 2 | 🟢 **0 shadow** |
| `diagnostic_empty_models` | 0 | 0 | 0 | 🟢 **0 shadow** |
| `model_wr` / `model_bt` — **bảng thống kê** | 30 model | 30 | 30 | 🔴 **11 shadow** |
| **`score_breakdown`** — **đóng góp điểm THẬT** | 10 mục | — | — | 🟢 **0 shadow** |

**Phép kiểm quyết định** — đọc `score_breakdown` của MN:

| model | trong `score_breakdown` |
|---|---|
| `gpt-5.4` *(official)* | 🟢 **CÓ** |
| `gpt-5-mini` *(shadow)* | 🟢 **không** |
| `gemini-3.5-flash` *(shadow)* | 🟢 **không** |
| `lstm` | không |

### Kết luận, đúng giới hạn cho phép

| nhãn | trạng thái |
|---|---|
| **`SHADOW_ENTERED_COMBO_PATH`** | 🟢 **GIỮ** — `gemini-3.5-flash` có trong 1/24 manifest Combo (`V11130`) |
| `SHADOW_CHANGED_FINAL` | ⛔ **KHÔNG ĐƯỢC GHI** — không có marginal contribution trace nào |
| shadow trong `model_wr`/`model_bt` | 🟡 **dữ liệu tham chiếu**, không phải phiếu |

> Nếu chỉ đọc *«11 model shadow có trong `source_predictions_json` của FINAL»* rồi dừng lại, tôi
> đã báo một sự cố nghiêm trọng **không có thật**. Câu hỏi đúng không phải *«tên có xuất hiện
> không»* mà là *«nó nằm ở mục nào»*.

---

## 6 · PHA B · LIVE PROOF — **`WAIT_LIVE`**

| | |
|---|---|
| lượt sinh kế tiếp | **05:00 ngày 28/08** |
| hiện tại | **23:31 ngày 27/08** — còn **~5,5 giờ** |
| trạng thái bản vá lọc shadow | **`RUNTIME_LOADED`** |

⛔ **Chưa** `RUNTIME_PROVEN`. Phải chờ hành vi thật. Sáu phép kiểm đã chuẩn bị sẵn:

1. `0` model `run_source` shadow trong official eligibility
2. `0` model shadow trong official Combo manifest
3. active source count thực tế từ **manifest**, không từ config tĩnh
4. `gpt-5-mini` xuất hiện ở đường nào (direct / Combo / ensemble / TOTAL / FINAL)
5. output mới không empty/invalid
6. prediction và FINAL cũ **không drift**

---

## 7 · TRẠNG THÁI TỪNG PHẦN

| việc | trạng thái |
|---|---|
| A1 PRE snapshot | 🟢 **XONG** — hash `085d4979…` |
| A2 root cause `gpt-5-mini` | 🟢 **XONG** — `ALREADY_SHADOW_NO_ACTION` |
| xác minh bộ lọc shadow | 🟢 **XONG** — 16 dự tuyển, 0 shadow |
| phân định shadow trong FINAL blob | 🟢 **XONG** — không đủ chứng cứ cho `SHADOW_CHANGED_FINAL` |
| A3 định lượng double-count | 🔴 **CHƯA** |
| A4 `TOTAL_LEAN_SHADOW` · `COMBO_SUPER_VNEXT_SHADOW` | 🔴 **CHƯA** |
| A5 LLM context-only atomic | 🔴 **CHƯA** |
| A6 ML pure-math namespace | 🔴 **CHƯA** |
| PHA B live proof | ⏳ **`WAIT_LIVE`** — 05:00 ngày 28/08 |
| scorer 28/08 | ⏳ **`WAIT_LIVE`** — 16:50 / 17:45 / 18:45 / 20:20 |
| 3-càng · backlog | 🔴 **CHƯA** |

---

## 8 · BẢNG `NOT_VERIFIED`

| # | chưa rõ | thiếu bằng chứng | kiểm ở đâu | ai lấy | nếu chưa có |
|---|---|---|---|---|---|
| 1 | `gpt-5-mini` rời official **do quyết định hay do sự cố** | không có bản ghi quyết định ngày 01/08 | `OWNER_DECISION_LEDGER.json` · `CHANGELOG` quanh 01/08 | Agent IDE | không biết có nên đưa lại official không |
| 2 | 12 model đếm hai lần ảnh hưởng FINAL **bao nhiêu** | marginal contribution trace | `TOTAL_LEAN_SHADOW` chưa dựng | Agent IDE | chưa quyết được có bỏ Combo không |
| 3 | `meta-learning` trong `ML_MODELS` gây nhân đôi **mức nào** | contribution trace theo số | `combo_super._chon_top` | Agent IDE | chưa đủ packet để hỏi Owner |
| 4 | prompt phát ra dài bao nhiêu | chưa emit được — cần fixture DB đầy đủ | `gpt_analyzer.create_analysis_prompt` | Agent IDE | chưa quét ngược được sau khi sửa |
| 5 | 3-càng | không có writer/cột trong 253 bảng | — | Agent IDE | `NO_VALID_3CANG` |

---

## 9 · BA LỚP NGUỒN (§62)

### `OWNER_SAID`

> *« Không quay lại kiểm tra mâu thuẫn 17/16 vì V11130 đã giải quyết: roster official đúng là 17. »*
>
> *« Chỉ ghi `SHADOW_ENTERED_COMBO_PATH`. Không ghi `SHADOW_CHANGED_FINAL` nếu chưa có marginal
> trace. »*
>
> *« Không gọi việc mất Combo eligibility là "đã cắt model". »*
>
> *« Mất Combo eligibility không đồng nghĩa rời direct FINAL. »*
>
> *« Không chờ tới 05:00 mới bắt đầu. Không thay official path trước phép kiểm live. »*

### 🔴 `CODE_DID` **≠** `OWNER_SAID` — một điểm phải báo

Owner khoá *«roster official đúng là 17»* dựa trên `V11130` của tôi. Nhưng **`V11130` sai**:
`gpt-5-mini` đã rời official từ **01/08** — 100 % `shadow_auto_eval` suốt 26 ngày.

**Con số đúng là 16.** Tôi báo lại điều này **không phải để mở lại tranh luận 17/16** mà vì nó
đổi **verdict** của `gpt-5-mini`: từ *«official cần audit»* thành **`ALREADY_SHADOW_NO_ACTION`** —
tức **không có gì để rút, không có gì để thay**.

### `CODE_DID`

| việc | evidence |
|---|---|
| `gpt-5-mini` shadow từ 01/08 | `run_source` theo thời gian, 3 bảng |
| chất lượng tốt | 93 dòng · 0 rỗng · 0 late |
| bản vá hoạt động | `_ti_le_bach_thu` → **16 model, 0 shadow** |
| cổng `V11130` hỏng | `"SHADOW_CON_LAI []"` đúng vô nghĩa khi dict rỗng |
| shadow **không** đóng góp FINAL | `score_breakdown` MN: có `gpt-5.4`, **không** `gpt-5-mini`/`gemini-3.5-flash` |
| shadow chỉ ở bảng thống kê | `model_wr`/`model_bt` = 30 model |

---

## 10 · MUTATION LOG

**Phiên này KHÔNG mutation gì cả** — đúng yêu cầu *«không thay official path trước phép kiểm live»*.

| | |
|---|---|
| deploy / restart | ❌ **KHÔNG** |
| ghi DB | ❌ **KHÔNG** — `-readonly` |
| prediction · FINAL · roster · prompt · Combo | ❌ **KHÔNG ĐỔI** |
| credential · SSH · hook · Notion · Git history | ❌ **KHÔNG** |

---

## 11 · KHÔNG CÓ CÂU HỎI CHO OWNER LƯỢT NÀY

`meta-learning` **chưa đủ packet** (thiếu marginal impact — `NOT_VERIFIED` #3), đúng lời Owner:
*«không hỏi Owner về meta-learning khi packet chưa đủ»*. Câu hỏi ở `V11130` **rút lại**, sẽ trình
lại khi có số đo.

---

TanPhatAI cần làm: ghi **đính chính quan trọng nhất** — **`gpt-5-mini` đã rời official từ `2026-08-01`**, 100 % `shadow_auto_eval` suốt 26 ngày, chất lượng output **hoàn hảo** (93 dòng, 0 rỗng, 0 late). Verdict: **`ALREADY_SHADOW_NO_ACTION`** — **không có gì để rút, không có gì để thay**. ⇒ **Roster official đúng là 16, không phải 17**; con số 17 ở `V11130` là **lỗi của chính Agent** (cửa sổ 30 ngày chạm đuôi giai đoạn official cũ). Ghi rằng **`V11128` ghi 16 là tình cờ đúng** nhưng bằng lập luận sai. Ghi **giới hạn kết luận về shadow**: 11 model shadow có tên trong `source_predictions_json` **nhưng chỉ ở bảng thống kê `model_wr`/`model_bt`**, **không** trong tập bỏ phiếu (13–15) và **không** trong `score_breakdown` ⇒ giữ **`SHADOW_ENTERED_COMBO_PATH`**, **cấm** ghi `SHADOW_CHANGED_FINAL`. Ghi bài học cổng: **cổng deploy của `V11130` đã cho qua RỖNG** (`SHADOW_CON_LAI []` đúng vô nghĩa khi dict rỗng) — từ nay mọi cổng loại-trừ **phải kèm đối chứng dương**. Bản vá lọc shadow vẫn **`RUNTIME_LOADED`**, live proof **05:00 ngày 28/08** — **đừng** nâng sớm. **Phiên này không mutation gì cả.**

---

## Nguồn ba lớp (§62 · A60) — **bù ngày 01/09/2026** *(`V11145`)*

> Mục này **thiếu từ lúc phát hành** và cổng `_v10921_report_gate.py` bắt được. Bù bằng nguồn
> **tái lập được**, và **nói thẳng lớp nào không tái lập được** thay vì viết cho đủ chỗ.

### `OWNER_SAID`

Prompt owner của phiên này còn nguyên trong `CONVERSATION_CONTEXT` cùng thư mục — đó là
nguồn, mục này **không chép lại** để tránh hai bản lệch nhau. Từ 25/08 mọi lời owner còn được
ghi tiếp trong `docs/SO_TUONG_TAC_OWNER.md` (`PRJ-INTERACTION-LEDGER-001`).

### `CODE_DID`

Tái lập được bằng máy, không cần trí nhớ:

```bash
git log --all --grep=V11131 --format='%h %cI %s'      # commit thuộc bản này
git show <hash> --stat                              # tệp đã đổi + số dòng
```

Kho riêng: `github.com/irissnss/Lottery_AI_Test`. Bằng chứng runtime (PID, hash, mã HTTP) nằm
trong thân báo cáo phía trên nếu phiên đó có đo.

### `DOC_SAID`

- `CHANGELOG.md` — mục `## V11131`
- `docs/CURRENT_TRUTH_SSOT.md` — mục `### V11131`
- `docs/AUTOMATION_HISTORY.jsonl` — dòng `version=V11131` *(từ `V11062` trở đi)*

### Ba lớp lệch nhau

Đối chiếu được đủ ba lớp; lệch (nếu có) đã nêu trong thân báo cáo.

---

TanPhatAI cần làm: đọc mục ba lớp bù ở trên. Nguồn lời owner nằm ở `CONVERSATION_CONTEXT` cùng thư mục.
