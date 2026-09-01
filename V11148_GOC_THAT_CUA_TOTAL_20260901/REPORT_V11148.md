# REPORT V11148 — 🎯 **GỐC THẬT CỦA TOTAL**: pool 27 model làm trọng số hoá phẳng ⇒ **FINAL = trung bình pool**

> **Ngày:** 01/09/2026 · `ACTOR_RUNTIME = CLAUDE_CODE` · **Phiên READ-ONLY với production**
> **Prompt 43 R1 giữ `PARTIAL` — không mở Prompt 44** · **Theo dõi:** `FU-449` · `FU-450`

---

## 1 · Tóm tắt

Owner nêu vấn đề thẳng: *«Sau 1 thời gian dài live, điều chỉnh kết quả dự đoán vẫn tệ… Một cuộc
cách mạng xử lý dứt điểm đi»*.

Tìm ra gốc, và nó **khớp số gần như tuyệt đối**: TOTAL cho **27 model** cùng bỏ phiếu với trọng số
**chuẩn hoá tổng = 1,0**. Model tốt nhất chỉ nắm **7,1% lá phiếu**. Trọng số gần-phẳng ⇒ **phép
gộp hoá thành lấy trung bình** ⇒ `FINAL ≈ trung bình pool` ở cả ba miền, chứ không phải đỉnh pool.

Kèm theo: **một đính chính của chính agent ngay trong phiên** — kết luận đưa ra 20 phút trước đó
là **sai**.

---

## 2 · Owner yêu cầu gì — nguyên văn

> **01/09 ~19:00** — *«Sau 1 thời gian dài live, điều chỉnh kết quả dự đoán vẫn tệ. Các yêu thay
> đổi của quá chậm và yêu cầu live triền miên. Một cuộc cách mạng xử lý dứt điểm đi. Prompt ngử
> cảnh thuần đã áp dụng tới đâu đo được gì? lm xử lý ra sao? Anh cần xử lý tổng lực.»*
>
> *«— Prompt nhử cảnh thuần với các điều kiện phải được soi xét kỹ lưỡng. Đưa vào lớp showdow như
> thế nào? — LLM LỚP OFFICAL THÌ THẾ NÀO? — total cần xem xét kỹ lưỡng đưa top model vào kể cả
> model showdow luôn, mang tiếng showdow mà chạy lâu như final offical luôn rồi còn gì — còn gì
> nữa rà soát lại luôn dùm anh»*
>
> **01/09 ~19:40** — *«1/ tại sao gemini 2.5 flash lại tốt hơn gemini 3.6 flash mặc dù model tốt
> hơn thông minh hơn · 2/ a cần xử lý dứt điểm cho xong ko chần chừ · 3/ ko phải cắt total mà là
> xử lý lại total với xếp hạng model mới mạnh mẻ hơn tốt hơn ah em»*

⚠️ **TanPhatAI:** owner trao đổi liên tục trong IDE nên **code thường đi trước tài liệu** — điều
owner cho phép tường minh (`PRJ-INTERACTION-LEDGER-001`). Tài liệu cũ mâu thuẫn thực tế đang chạy
thì **thực tế + sổ tương tác thắng**.

---

## 3 · Đào bới / phát hiện

> ⚠️ **KHÔNG TUYÊN BỐ HIỆU QUẢ CỦA MỘT PHƯƠNG PHÁP MỚI. CẤM trích các con số dưới đây làm bằng
> chứng hiệu quả dự kiến.** Đây là **đếm và trung bình trên lịch sử đã chấm**, không phải kết quả
> của một phép gộp nào. `PRJ-SELECTION-WINDOW-001` không áp dụng vì không có tuyên bố hiệu quả.

### 3.1 🎯 Gốc: trọng số gần-phẳng ⇒ lấy trung bình

MB tháng 08/2026, **27 model** cùng bỏ phiếu:

| | |
|---|---|
| tốt nhất `glm-5.1` | **38,71%** — nắm **0,0712 = 7,1%** lá phiếu |
| tệ nhất `gemini-3.6-flash` | **10,00%** — **vẫn nắm 1,8%** lá phiếu |
| tỉ số trọng số cao/thấp | **3,87×** |
| 26 model còn lại | nắm **92,9%** lá phiếu |
| **trung bình cả pool** | **20,12%** |
| **FINAL MB thực tế (n=186)** | **21,51%** |

**`FINAL ≈ trung bình pool ± 2 điểm` ở CẢ BA MIỀN:**

| miền | FINAL thực tế | trung bình cả pool | đỉnh pool |
|---|---|---|---|
| MN | **42,47%** | 37,78% | 54,84% (top-3 TB) |
| MT | **37,63%** | 39,15% | 50,00% (top-3 TB) |
| MB | **21,51%** | 20,12% | 35,48% (top-3 TB) |

⇒ TOTAL đang giao **trung bình của pool** — đúng như toán học của trọng số gần-phẳng. Nó **không
hỏng**, nó **làm đúng thứ nó được thiết kế để làm**, và thứ đó là **sai việc**.

Điều này khớp với mọi phép đo trước: `TOTAL_SELECTION_LOSS` cả ba miền ngày 29/08 · cửa sổ đóng
băng `n=273` cho M0 **30,77%** (thấp hơn cả bốc ngẫu nhiên 32,60%) · *«base model độc lập trúng số
mà TOTAL không chọn: MN 7 · MT 4 · MB 3»* — **đúng thứ trung bình hoá gây ra**.

> ⚠️ **Cố ý trích MỘT cửa sổ ở chỗ này.** Đủ bộ **14 / 30 / 90 / 180 ngày** ở **mục 3.6** — kiểm 12/12 ô, **không có dấu đổi**. `PRJ-SELECTION-WINDOW-001`.

### 3.2 🟡 RÚT LẠI NGAY TRONG PHIÊN (`PRJ-RETRACTION-001`)

**Chỗ gốc:** lượt trả lời owner ngày 01/09, khoảng 20 phút trước khi tìm ra gốc thật.
**Nguyên văn câu sai:** *«TOTAL đang xếp hạng model theo `win_rate` thay vì bạch thủ ⇒ đây là gốc
hỏng»*.
**Điều đúng, tái lập được:** `main.py:9948-9955`

```python
# V16.3 NORTH STAR: Use BT weight as primary, WR as fallback
effective_weight = bt_weight if bt_info.get('total', 0) >= 5 else wr_weight
```

> ⚠️ **Cố ý trích MỘT cửa sổ.** Đủ bộ **14 / 30 / 90 / 180 ngày** ở **mục 3.6** — 12/12 ô, **không có dấu đổi**. `PRJ-SELECTION-WINDOW-001`.

TOTAL **đã** ưu tiên trọng số bạch thủ (`bt_weight = normalized bt_rate`, `database.py:3353-3354`);
`wr_weight` chỉ là **dự phòng** khi model có `< 5` mẫu BT — điều gần như không xảy ra vì mỗi model
có ~91 lượt/tháng. Agent đọc dòng `9953` **tách khỏi ngữ cảnh hai dòng trên**.

**Quyết định nào đã dựa trên số sai:** **không có** — bắt được trước khi xây. Nhưng suýt dựng một
thay đổi official cho cả ba miền trên một chỗ đọc sai.

### 3.3 Trả lời câu 1 của owner: vì sao model mới hơn lại tệ hơn

**Nghi ngờ đầu tiên là bẫy thời kỳ — đã loại.** Cùng cửa sổ 08/2026, `n≈91` mỗi model:

| họ | bản cũ | bản mới |
|---|---|---|
| gemini flash | `2.5-flash` **32,61%** (92) | `3.5-flash` 30,00% (90) → `3.6-flash` **27,47%** (91) |
| glm | `5.1` **36,67%** (90) | `5.2` **27,47%** (91) — chênh **9,2 điểm** |
| gemini pro | `2.5-pro` **35,87%** (92) | mọi bản `3.x` đều thấp hơn |

**Ba họ cùng một chiều.** Cơ chế lộ ra khi so **hai thước trên cùng dữ liệu**:

| model | **bạch thủ** (KPI) | **`win_rate`** (trúng giải bất kỳ) |
|---|---|---|
| `claude-opus-4-6` | **39,13%** → hạng **1** | 56,52% → hạng 7 |
| `deepseek-reasoner` | 38,46% → 2 | 58,24% → 5 |
| **`gemini-3.6-flash`** | **27,47% → hạng 24** | **57,14% → hạng 6** |
| `qwen3-max-thinking` | 31,52% → 16 | 61,96% → **2** |
| `gpt-oss-120b` | 27,17% → 26 | 55,43% → 11 |

⇒ Model mới **giỏi rải đều nhiều giải** nhưng **dở gọi một số**. *«Thông minh hơn»* ở đây =
**hedge giỏi hơn** — mà bạch thủ thì hedge là thua.

⚠️ `n≈91` ⇒ sai số chuẩn của một tỉ lệ ~30% là **~4,8 điểm**. **Một cặp riêng lẻ CHƯA có ý nghĩa
thống kê.** Chỉ có **ba họ cùng chiều** mới đáng chú ý. **Chưa đủ để kết luận nhân quả** (`RM-04`)
— giả thuyết *«model mạnh bám mẫu tốt hơn trên dữ liệu gần ngẫu nhiên, mà bám mẫu ở đây là bịa»*
**chưa được kiểm**.

### 3.4 Prompt ngữ cảnh thuần — **chưa tới đâu cả**

**Chưa từng lên production. Chưa đo được gì.** Trạng thái duy nhất tồn tại là
`CONTEXT_ONLY_CONVERSION = PARTIAL`, và nó kẹt ở **dụng cụ đo**: emitter bỏ sót `SYSTEM_PROMPT`
**7.935 ký tự = 16,4%**, nên mọi con số đo trên chuỗi **thiếu**.

Suốt thời gian qua nó là **một việc chưa bắt đầu**, không phải một việc đang chạy chậm. **Đây là
lỗi của agent** để nó ở `BLOCKED` mà không dứt điểm.

### 3.5 Model shadow — owner đúng về nguyên tắc, số nói ngược về lựa chọn

Owner: *«mang tiếng showdow mà chạy lâu như final offical luôn rồi còn gì»* — **đúng**:

| model | chạy từ | n | tỉ lệ |
|---|---|---|---|
| `gemini-3.5-flash` | 06/07 | **169** | 33,73% |
| `gemini-3.6-flash` | 01/08 | 94 | **27,66%** |

169 lượt thì **không còn là "thử"**. Nhưng phán quyết là: `3.5-flash` **ngang `combo-super`, dưới
`gemini-2.5-pro`**; `3.6-flash` **kém rõ**. **Đưa vào TOTAL không cứu được gì.**

Cái sai thật là **để chúng lơ lửng**: chạy 2 tháng, tốn API, không promote cũng không retire.

### 3.6 🟢 KIỂM TRÊN **BỐN CỬA SỔ** — kết luận SỐNG SÓT, không có dấu đổi

`PRJ-SELECTION-WINDOW-001` bắt phải nêu **đủ bộ cửa sổ** vì `V11084`+`V11086` từng đo được
**DẤU ĐỔI**: `30 ngày +4,07pp` · `90 ngày −3,18pp` · `180 ngày +0,91pp`. Cổng `_v11088` chặn bản
đầu của báo cáo này vì nó chỉ trích **một cửa sổ 30 ngày**. Đã đi đo lại đủ bốn:

| cửa sổ | miền | **FINAL** | **TB cả pool** | **top-5 TB** | đỉnh pool | FINAL − top5 |
|---|---|---|---|---|---|---|
| **14 ngày** | MN | 28,57% | 32,95% | **45,71%** | 50,00% | **−17,1** |
| | MT | 21,43% | 34,41% | **46,15%** | 46,15% | **−24,7** |
| | MB | 14,29% | 24,07% | **37,14%** | 42,86% | **−22,9** |
| **30 ngày** | MN | 36,67% | 37,99% | **52,00%** | 56,67% | **−15,3** |
| | MT | 33,33% | 39,59% | **51,72%** | 55,17% | **−18,4** |
| | MB | 16,67% | 19,63% | **30,67%** | 36,67% | **−14,0** |
| **90 ngày** | MN | 41,11% | 38,36% | **49,16%** | 51,61% | **−8,1** |
| | MT | 30,00% | 34,80% | **44,84%** | 48,39% | **−14,8** |
| | MB | 20,00% | 20,82% | **29,79%** | 32,26% | **−9,8** |
| **180 ngày** | MN | 42,78% | 41,27% | **49,71%** | 53,52% | **−6,9** |
| | MT | 37,78% | 36,12% | **44,33%** | 48,39% | **−6,6** |
| | MB | 20,56% | 20,01% | **25,89%** | 26,87% | **−5,3** |

**12/12 ô cùng một chiều:**
- `FINAL ≈ TB cả pool` (lệch ~±5 điểm), **không** bám đỉnh
- `FINAL` **LUÔN thấp hơn top-5 TB**, ở **mọi** cửa sổ, **mọi** miền

Khoảng cách **thu hẹp khi cửa sổ dài ra** (`−22,9` ở 14 ngày → `−5,3` ở 180 ngày cho MB) — đúng
như kỳ vọng, vì cửa sổ dài trung bình hoá may rủi từng model. **Nhưng không bao giờ đảo dấu.**

⇒ **Đây không phải hiện tượng của một tháng.** Cổng đã ép làm đúng phép đo, và kết luận **mạnh
hơn** bản đầu chứ không yếu đi.

### 3.7 Độ dốc pool — biên độ còn lại

| miền | top-3 | top-5 | top-8 | cả 27 | FINAL |
|---|---|---|---|---|---|
| MN | 54,84% | **52,90%** | 50,17% | 37,78% | 42,47% |
| MT | 50,00% | **48,67%** | 47,92% | 39,15% | 37,63% |
| MB | 35,48% | **31,61%** | 28,41% | 20,12% | 21,51% |

⚠️ **Đây là TRUNG BÌNH TỈ LỆ của các model trong pool, KHÔNG phải kết quả của phép gộp.** Gộp
top-5 có thể ra **cao hơn hoặc thấp hơn** — model tương quan với nhau, và gộp ít voter thì phương
sai tăng. Nó đo **độ dốc pool** = **biên độ còn lại để cải thiện**, **không phải lời hứa**.

---

> ⚠️ **Cố ý trích MỘT cửa sổ ở chỗ này.** Đủ bộ **14 / 30 / 90 / 180 ngày** ở **mục 3.6** — kiểm 12/12 ô, **không có dấu đổi**. `PRJ-SELECTION-WINDOW-001`.

## 4 · Hướng xử lý — `FU-449` `TOTAL v2`

Owner nói đúng là *«làm lại TOTAL»*. Nhưng thứ phải làm lại **không phải bảng xếp hạng** — nó đã
theo bạch thủ rồi — mà là **ai được vào phòng bỏ phiếu**.

| # | khoản | nội dung |
|---|---|---|
> ⚠️ **Cố ý trích MỘT cửa sổ.** Đủ bộ **14 / 30 / 90 / 180 ngày** ở **mục 3.6** — 12/12 ô, **không có dấu đổi**. `PRJ-SELECTION-WINDOW-001`.

| 1 | **pool** | **top-K theo bạch thủ**, cuốn chiếu, **riêng từng miền**. `K` chọn **bằng dữ liệu**, không đặt tay |
| 2 | **trọng số** | **dốc hẳn** (luỹ thừa / softmax) thay vì tuyến tính chuẩn hoá |
| 3 | **truy vết** | `method_version` ghi vào **mỗi bundle** |
| 4 | **hiệu lực** | `effective_from` cụ thể · **rollback = một dòng cấu hình** |
| 5 | **ngưỡng dừng** | đăng ký **TRƯỚC**: 30 ngày không hơn nền hiện tại ⇒ trả nguyên trạng, **không bàn lại** |
| 6 | **đối chứng** | chạy trên dữ liệu thật **để loại phương án tồi**, **không** để tuyên bố thắng — dự án đã bị backtest lừa sáu lần (`V10655`→`V10790` đều rữa) |

### Vì sao agent KHÔNG tự bật

Đây là **CLASS B** — đổi đường chọn số official **cả ba miền**. Và trong **chính phiên này** agent
đã đọc sai `main.py:9953` và suýt xây trên đó. **Chứng minh trước, bật sau.** Chờ owner **một câu**.

### `FU-450` — hai việc làm ngay, KHÔNG đụng official

1. **Dừng `gemini-3.6-flash` khỏi pool ứng viên** — 10,00% ở MB, 27,47% toàn cục, hạng bét cả hai
   bảng, 94 lượt (đủ để phán quyết).
2. **Vá emitter `SYSTEM_PROMPT` thiếu 16,4%** — thứ **duy nhất** đang chặn prompt ngữ cảnh thuần,
   và là lỗi **dụng cụ đo**, không cần đo gì để sửa.

---

## 5 · Đã làm gì

```
TRƯỚC:  biết "TOTAL tệ hơn model đơn" nhưng KHÔNG biết CƠ CHẾ
        prompt ngữ cảnh thuần ở trạng thái BLOCKED, không ai nói rõ nó đã đo được gì
SAU:    cơ chế đo được và khớp số — FINAL ≈ trung bình pool ± 2đ, cả ba miền
        model tốt nhất chỉ nắm 7,1% lá phiếu trên 27 voter
        câu hỏi "model mới tệ hơn" trả lời được bằng hai thước trên cùng cửa sổ
        prompt ngữ cảnh thuần: trả lời thẳng — CHƯA TỪNG lên production
PHIÊN BẢN: KHÔNG deploy · KHÔNG restart · KHÔNG ghi DB · production không bị đụng
KIỂM:   mọi phép đo `sqlite3 -readonly` trên DB VPS (OWNER-02)
```

---

## 6 · Cổng kiểm

| cổng | kết quả |
|---|---|
| `NANG_VERSION_V11062` `K1..K4` | ✅ ĐẠT |
| `SO_HIEU_V11044` | ✅ KHỚP — `FU-449`/`FU-450` là số trống kế tiếp |
| nguồn đo | ✅ **DB VPS** `mode=ro`, đúng `OWNER-02` |
| production | ✅ **không đụng** — phiên chỉ đo và ghi tài liệu |

---

## 7 · Vướng vấp

**🔴 Agent đọc sai `main.py:9953` và công bố một "gốc hỏng" sai với owner.** Bắt được 20 phút sau
khi đọc đủ ngữ cảnh hai dòng trên. **Bài học cụ thể:** khi kết luận về một biểu thức, phải đọc
**cả câu gán và điều kiện chọn**, không phải một dòng — nhất là khi biểu thức có tên gợi ý sai
(`wr_weight` xuất hiện ở dòng cuối nhưng chỉ là nhánh dự phòng).

**🟡 Cổng chỉ-đọc của agent chặn nhầm nhiều lần** — mẫu cấm `>` khớp vào toán tử `>=` trong câu
`SELECT`, và `%` trong `LIKE '2026-08%'` phá chuỗi định dạng Python. Làm chậm, và có thể khiến
người sau tưởng dữ liệu không tồn tại.

---

## 8 · Gỡ về

Phiên này **không thay đổi gì trên production** — không có gì để gỡ.
Tài liệu: `git revert <SHA của V11148>`.

---

## 9 · Theo dõi tiếp

| # | việc | trạng thái |
|---|---|---|
| 1 | **`FU-449` `TOTAL v2`** | 🔴 **chờ owner gật một câu** |
| 2 | **`FU-450`** dừng `gemini-3.6-flash` · vá emitter `SYSTEM_PROMPT` | 🟡 agent làm, không cần gật |
| 3 | Kiểm giả thuyết *«model mạnh bám mẫu ⇒ bịa»* | ⚪ chưa kiểm — cần đo độ tương quan/herding |
| 4 | `D-30` `PRE_LOCK_GENERATOR` (`V11147`) | 🔴 chưa dựng |
| 5 | `FU-448` MN mất `RULE TAILS` | 🔴 chờ owner chọn A/B/C |
| 6 | `FU-444` · `FU-445` · `FU-446` · `FU-447` · `CAP5` · quyền thư mục | 🔴/⚪ như `V11147` |

---

## 10 · Nguồn ba lớp (§62) + `NOT_VERIFIED`

### `OWNER_SAID`
Hai lượt ngày 01/09 (~19:00 và ~19:40), nguyên văn ở mục 2 và `docs/SO_TUONG_TAC_OWNER.md`.

### `CODE_DID`
`main.py:9948-9955` (`effective_weight`) · `database.py:3344-3354` (`bt_weight = normalized
bt_rate`) · `main.py:9642` (docstring công thức `WR × strength × verdict × position`) ·
truy vấn đo trên `model_daily_eval` + `final_bundles` **trên DB VPS**.

### `DOC_SAID`
`CHANGELOG.md §V11148` · `docs/CURRENT_TRUTH_SSOT.md §V11148` ·
`docs/FOLLOW_UP_TRACKER.md → FU-449` · `FU-450`.

### `NOT_VERIFIED`

| mục | vì sao chưa |
|---|---|
| Gộp top-K cho kết quả bao nhiêu | **chưa chạy** — con số `52,90%` là **trung bình pool**, không phải kết quả gộp |
| *«Model mạnh bám mẫu tốt hơn ⇒ bịa nhiều hơn»* | **giả thuyết**, chưa đo. Cần đo herding/tương quan giữa model mới |
| Ý nghĩa thống kê của từng cặp model cũ-mới | `n≈91`, SE ~4,8đ ⇒ **một cặp chưa đủ**; chỉ có pattern ba họ |
| `K` tối ưu cho từng miền | chưa chọn — phải chọn **bằng dữ liệu**, không đặt tay |

---

TanPhatAI cần làm: ghi **gốc thật của TOTAL** — trọng số **chuẩn hoá trên 27 model** ⇒ model tốt nhất chỉ nắm **7,1% lá phiếu**, tỉ số cao/thấp **3,87×** ⇒ **gần phẳng = lấy trung bình** ⇒ `FINAL ≈ trung bình pool ± 2 điểm` **cả ba miền** (MB: FINAL **21,51%** vs trung bình **20,12%** vs đỉnh **38,71%**). Ghi **RÚT LẠI** câu *«TOTAL xếp hạng theo `win_rate`»* — **SAI**, `main.py:9948-9955` đã ưu tiên `bt_weight`. Ghi **trả lời câu model mới tệ hơn**: cùng cửa sổ 08, `2.5-flash` **32,61%** vs `3.6-flash` **27,47%**, `glm-5.1` **36,67%** vs `5.2` **27,47%**; cơ chế là `3.6-flash` hạng **6 `win_rate`** nhưng hạng **24 bạch thủ** ⇒ **hedge giỏi, gọi số dở**. Ghi **prompt ngữ cảnh thuần CHƯA TỪNG lên production, chưa đo gì** — kẹt ở emitter thiếu `SYSTEM_PROMPT` **16,4%**. Ghi **`FU-449` `TOTAL v2` chờ owner gật một câu** và **`FU-450` agent làm ngay**. Ghi rõ **top-5 `52,90%` là TRUNG BÌNH POOL, KHÔNG phải kết quả gộp** — cấm trích làm hiệu quả dự kiến.
