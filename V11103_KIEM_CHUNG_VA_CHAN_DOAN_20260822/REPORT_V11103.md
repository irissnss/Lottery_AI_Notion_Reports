# REPORT V11103 — KIỂM CHỨNG LƯỢT 05:00 · CHẨN ĐOÁN `glm-5.1` · ĐO `FU-421`

**Ngày:** 2026-08-22 (sáng) · **Mã đọc:** `KS2208` · **Quyết định:** `QD-071` (thi hành tiếp)
**Production KHÔNG đổi** — phiên kiểm chứng + chẩn đoán, **không deploy, không restart, không sửa mã**
**Verdict:** `REPORT_PUBLISHED` · **V11102 GIỮ NGUYÊN, KHÔNG nâng lên `RUNTIME_PROVEN`** — lý do §3.1

---

## 1. Tóm tắt

Ba việc, và **cả ba đều cho kết quả ngược với điều đang được tin**:

| việc | điều đang được tin | điều đo được |
|---|---|---|
| kiểm chứng V11102 | *«sáng nay là kiểm được, nâng verdict»* | **hai xanh, một CHƯA kiểm được** ⇒ **không nâng** |
| `glm-5.1` rỗng | *«lỗi của MN»* · *«model này kém»* | **cả ba miền đều có** · tỉ lệ **ngang `deepseek-reasoner`** |
| `FU-421` ba chỗ hoà | *«thứ tự ngẫu nhiên có thể đổi số»* | **0/111 — không đổi**; nhưng lộ ra **một đường lùi câm** nguy hiểm hơn |

**Hai con số phải rút lại**, cả hai là của chính báo cáo hôm qua: **§4.1** và **§5.1**.

---

## 2. Owner yêu cầu gì (nguyên văn)

> *«V11102 đã deploy thước đo model + bộ chấm T-B. Verdict còn thiếu `RUNTIME_PROVEN` vì lượt
> production đầu tiên của ngày 22/08 chưa chạy lúc đóng báo cáo. Phiên này là phiên KIỂM CHỨNG +
> CHẨN ĐOÁN — CẤM sửa production.»*

> *«`glm-5.1` … 2/7 lượt tuần này trả RỖNG ở MN (MB/MT gần như không). Đo trước: rỗng vì API lỗi,
> vì bộ lọc nội dung, vì prompt miền Nam, hay vì timeout? Phân tích payload/log của đúng 2 lượt
> rỗng. CẤM hạ `MIN_MAU_DU_TUYEN` cho hết đỏ.»*

> *«`FU-421` — chạy `/du-doan` nhiều lần cùng một ngày trên môi trường thử, xem bộ số cuối có đổi
> không (tiền lệ cách đo của `FU-416`). Ba chỗ: `main.py:7894 :8101 :8354`. Chỉ trình — vá là
> phiên 24/08.»*

---

## 3. Đào bới / phát hiện — GĐ-1: kiểm chứng lượt 05:00 ngày 22/08

### 3.1 · Ba điều kiện, hai xanh, một chưa kiểm được

**① `CTX-18.4` — XANH.** Đo theo **giờ tạo từng bản ghi** (`RM-16`), không theo ngày:

```
TOÀN BỘ trace:
   CTX-18.3 : 821 lượt · mới nhất 2026-08-21 17:48:32
   CTX-18.4 :  19 lượt · mới nhất 2026-08-22 05:34:53

CHỈ các bản ghi tạo TỪ 2026-08-22 (tức SAU deploy):
   CTX-18.4 : 19 lượt        ← và KHÔNG bản ghi nào mang phiên bản cũ
```

**② Job đo sinh cả hai họ — CHƯA KIỂM ĐƯỢC.** Không phải đỏ, mà là **chưa tới lúc**:

```
lottery_results ngày 2026-08-22  →  RỖNG, chưa miền nào có kết quả  (lúc đo: 09:31 VN)
log SHADOW-PROMOTION-SCORECARD hôm nay  →  chưa chạy lần nào
```

Job `measurement_materialize` kích hoạt **khi kết quả xổ về đủ** từng miền
(`scheduler.py:1671/1740/1812`, sau `_cov_flag == "COMPLETE"`), **không phải lúc 05:00**.
MN về ~16:35 · MT ~17:35 · MB ~18:31. ⇒ **cửa kiểm là chiều tối nay.**

**③ Bảng khoá + lỗi — XANH:**

| bảng | trước | nay | đọc ra |
|---|---:|---:|---|
| `lottery_results` | 15.324 | **15.324** | không đổi |
| `model_daily_eval` | 12.953 | **12.953** | không đổi |
| `predictions` | 13.089 | 13.129 | **+40** = đúng số lượt hôm nay |
| `final_bundles` | 525 | 526 | **+1** = bundle hôm nay |

`Traceback` **0** · `CRITICAL` **0** kể từ restart · `health = 200`.

### 3.2 · Vì sao KHÔNG nâng verdict

`RM-12` cấm tự nâng tầng. Ba điều kiện thì **một chưa kiểm được**, nên `V11102` **giữ nguyên**
`CODE_PUSHED` + `DEPLOYED` + `REPORT_PUBLISHED`. Nâng lúc này là đổi lấy một dòng đẹp trong sổ
bằng một câu chưa có bằng chứng.

### 3.3 · Một đính chính về giờ restart

`REPORT_V11102` và prompt owner đều ghi *«restart 01:0x»*. **Sai.**
`systemctl show -p ActiveEnterTimestamp` ⇒ **`Sat 2026-08-22 00:00:35 +07`**.
`01:0x` là giờ chạy **nghiệm thu cuối**, không phải giờ restart. Chi tiết này quan trọng vì mọi
phép so «trước/sau deploy» đều lấy mốc đó.

---

## 4. Hướng xử lý và vì sao chọn — GĐ-2: `glm-5.1` rỗng, hai nguyên nhân khác hẳn nhau

### 4.1 · RÚT LẠI (theo `PRJ-RETRACTION-001` — đủ bốn phần)

| phần | nội dung |
|---|---|
| **chỗ gốc** | `REPORT_V11102` §6.2 và mục `FU-423`, công bố rạng sáng 22/08 |
| **nguyên văn câu sai** | *«rỗng CHỈ xảy ra ở MN»* |
| **điều đúng** | Đo 60 ngày: **MN 2/59 · MT 1/58 · MB 1/60** — **cả ba miền đều có**. Câu cũ dựng trên cửa sổ 30 ngày, nơi MB tình cờ bằng 0. Tái lập: `SELECT region, COUNT(*), SUM(pick_count=0) FROM model_daily_eval WHERE ai_model='glm-5.1' AND date>=date('now','-60 day') GROUP BY 1` |
| **đã dựa vào đâu** | Nó dẫn thẳng tới giả thuyết *«tại prompt miền Nam»* — một hướng điều tra **sai hẳn**. Không đo lại 60 ngày thì phiên 25/08 đã đi mổ prompt MN, mất một phiên cho một nguyên nhân không tồn tại |

### 4.2 · Hai lượt rỗng — trả lời đúng bốn câu owner hỏi

| ngày | trạng thái | độ trễ | nguyên nhân thật |
|---|---|---:|---|
| **15/08** | `ERROR` | **134.064 ms** | chờ **134 giây** rồi nhận **thân rỗng** (`Expecting value: line 1 column 1`) |
| **18/08** | `EMPTY_PROVIDER_OUTPUT` | **9 ms** | **cầu dao ngắt mạch OpenRouter đang mở** — lượt gọi **chưa bao giờ ra khỏi máy** |

| giả thuyết owner nêu | phán quyết |
|---|---|
| **API lỗi** | ✅ **đúng cho 15/08** — nhưng **không riêng `glm-5.1`**: cùng ngày, cùng miền, `deepseek-reasoner` (**nhà cung cấp KHÁC HẲN**) hỏng y hệt ⇒ sự kiện diện rộng |
| **bộ lọc nội dung** | ✗ không dấu vết nào |
| **prompt miền Nam** | ✗ **bác bỏ** — rỗng có ở cả ba miền, và gói ngữ cảnh MN **không phải** lớn nhất (MB mới lớn nhất) |
| **timeout** | ◐ một phần cho 15/08 — 134 s vượt ngưỡng «đi tiếp mềm» 90 s |
| *(không có trong danh sách owner)* | ✅ **cầu dao ngắt mạch** — nguyên nhân thật của 18/08 |

### 4.3 · Nhãn chẩn đoán GHI SAI SỰ THẬT — mục đáng vá riêng

`gpt_analyzer.py:3560 _openrouter_circuit_check()` khi cầu dao mở trả về:

```python
{"error": "⚠️ Model …: đang trong thời gian chờ (…s còn lại)", "ok": False}
```

Dict này **không có khoá `prediction`** ⇒ `scheduler.py:4370` lấy ra `numbers = []` ⇒ ghi thành
`EMPTY_PROVIDER_OUTPUT` với thông điệp:

> *«provider response parsed but no prediction numbers were found»*

**Câu này sai sự thật.** Provider **chưa hề trả lời gì** — lượt gọi bị chặn ngay tại máy. Ai đọc
bảng chẩn đoán sẽ đi tìm nguyên nhân ở **prompt** hoặc **bộ lọc nội dung** — đúng hướng mà chính
agent này suýt đi mất một phiên.

### 4.4 · So với các model output khác — và đây là chỗ đổi kết luận

| model | lượt (60 ngày) | rỗng | tỉ lệ |
|---|---:|---:|---:|
| **`glm-5.1`** | 177 | 4 | **2,26%** |
| **`deepseek-reasoner`** | 180 | 4 | **2,22%** |
| `gpt-oss-120b` | 180 | 2 | 1,11% |
| `gpt-5.4` | 180 | 1 | 0,56% |
| `claude-opus-4-6` · `claude-sonnet-4-6` · `combo-super` · `gemini-2.5-flash` · `gemini-2.5-pro` | 180 | 0 | **0%** |

`glm-5.1` **ngang bằng `deepseek-reasoner`** — model đã ở trong danh sách output từ lâu, **chưa ai
kêu**. Cảnh báo nổ cho `glm-5.1` **vì nó vừa vào danh sách hôm 21/08**, không phải vì nó tệ hơn.

**Vì sao chạm sàn:** hai lượt rỗng **rơi trúng cùng một cửa sổ 7 ngày của MN**, kéo mẫu xuống dưới
`MIN_MAU_DU_TUYEN = 5`. Với tỉ lệ 2,3% thì hai lượt rơi gần nhau là **chuyện bình thường của số
nhỏ** (`RM-04`), không phải dấu hiệu hỏng.

### 4.5 · ĐỀ XUẤT — lời thường, kèm được/mất (`QD-069`)

**Chuyện đang xảy ra, nói gọn:** `glm-5.1` thỉnh thoảng không trả lời — khoảng **2 lần trong 90
lượt**. Chuyện này **không mới** và **không riêng nó**; model `deepseek-reasoner` đang dùng lâu nay
cũng đúng tỉ lệ đó. Cái mới là `glm-5.1` **vừa được đưa vào danh sách chốt số hôm qua**, nên lần
đầu tiên có một cái cổng soi tới nó.

| lối | **được** | **mất** |
|---|---|---|
| **(a) GIỮ ở MN — đề xuất** | không cắt nhầm một model có tỉ lệ rỗng **ngang model đang dùng lâu nay**; tránh quyết định dựa trên cảnh báo do **cửa sổ 7 ngày** tạo ra | vẫn còn ~2,3% số ngày bundle thiếu một người đóng góp |
| (b) rút khỏi output MN | cổng hết đỏ ngay | **cắt mù** — `deepseek-reasoner` cùng tỉ lệ vẫn ở lại, tức xử một model **vì nó mới**, không vì nó kém |
| (c) hạ `MIN_MAU_DU_TUYEN` | hết đỏ ngay | **CẤM** — owner đã ký. Hạ sàn là **xoá đèn báo**, không sửa cái hỏng |

**Hai việc nên làm thay vì cắt:**
① **vá nhãn sai** của đường cầu dao — tách một trạng thái riêng cho *«chưa gọi vì cầu dao mở»*,
để lần sau không ai đi tìm nguyên nhân ở prompt;
② **đếm và báo số ngày bundle thiếu người** — hôm nay **không ai đang đếm** việc đó, nên không ai
biết 2,3% kia có làm hỏng gì không.

---

## 5. Đã làm gì — GĐ-3: đo `FU-421`, ba chỗ thiếu khoá phá hoà

Ba chỗ `main.py:7894` (Smart Ensemble) · `:8101` (Smart ML) · `:8354` (Combo No Token), cùng khuôn:

```python
sorted_nums = sorted(number_scores.items(), key=lambda x: -x[1])   # không khoá phá hoà
```

Cả ba nằm trong `_make_prediction()` và **đang chạy production** — `predictions` có dòng của
`smart-ensemble` · `smart-ml` · `combo-no-token` tới tận **22/08**.

### 5.1 · Ba phép đo, trên 111 cặp ngày-miền (60 ngày)

| phép | kết quả |
|---|---|
| **A. thử đối chứng** — dụng cụ đo có tác dụng không | một `set` thật cho **3 thứ tự khác nhau** qua `PYTHONHASHSEED` 1/2/987 ⇒ **CÓ tác dụng** |
| **B. thứ tự đổi theo seed?** | **0/111**, cả hai nhóm |
| **C. hoà với TỈ LỆ THẮNG THẬT?** | **0/111** — không một cặp hoà nào |

**Vì sao B ra 0 — lý do cấu trúc, không phải may mắn:** `number_scores` nạp từ `results.items()`,
mà `results` được đổ từ **danh sách/dict viết cứng** (`ml_models = [...]` ở `:7804`,
`all_ml_models = {...}` ở `:8245`). Dict Python giữ **thứ tự chèn** — **không `set` nào** lọt vào
chuỗi này.

**Vì sao C ra 0:** tỉ lệ thắng thật (`combo_super._get_dynamic_win_rates`, trộn 7 ngày ×2 + 30
ngày) là **số lẻ và khác nhau** — MN: `meta-learning` **54,2** · `lstm` **33,5** ·
`random-forest` **48,3** · `xgboost` **43,6** — nên `weight × position_bonus` gần như không thể trùng.

> **RÚT LẠI một con số của chính phép đo này.** Bản chạy đầu dùng giả định *«mọi model cùng
> win_rate»* vì đọc nhầm `model_rates = {}` ở `:7839` là giá trị cuối — **sai**, đó chỉ là khởi
> tạo, nó được nạp thật ở `:7843`. Con số **«107/111 hoà đúng biên hạng 0/1»** của bản đầu là
> **trường hợp xấu nhất giả định**, **không phải** số production. Số production là **0/111**.

⇒ **KHÔNG CHỨNG cả ba chỗ. Chúng KHÔNG đổi số công bố hôm nay.**

### 5.2 · Nhưng phép đo lộ ra thứ đáng giá hơn — một ĐƯỜNG LÙI CÂM

```python
model_rates = {}                                    # :7839  khởi tạo
try:    model_rates = {...dynamic_wr...}            # :7843  đường thường
except Exception:
    try:    model_rates = get_model_win_rates(...)  # :7848  lùi 1
    except Exception:  model_rates = {}             # :7850  lùi 2 — KHÔNG KÊU MỘT TIẾNG
```

Nếu **cả hai** phép lấy tỉ lệ thắng hỏng ⇒ `model_rates` rỗng ⇒ `wr` **luôn = 50** ⇒ **mọi model
trọng số bằng nhau**. Đo đúng tình huống đó:

| nhóm | có hoà ở đâu đó | hoà **đúng biên hạng 0/1** | biên hạng 2/3 |
|---|---:|---:|---:|
| **Smart Ensemble (2 model)** | 108/111 | **107/111 = 96%** | 107/111 |
| Smart ML · Combo (4 model) | 104/111 | 12/111 | 60/111 |

**Đọc ra:** ở tình huống lùi, **96% số ngày** con số hạng nhất của Smart Ensemble được quyết bởi
**thứ tự viết trong danh sách nguồn** — `meta-learning` luôn thắng `lstm` khi hoà — chứ **không**
bởi một luật nào. Và `except Exception: model_rates = {}` **không để lại một dấu vết nào**: đúng họ
lỗi mà `V11101` vừa dựng cổng để chặn (*che tiếng kêu rồi đọc số 0 thành sạch*).

Nói cách khác: **thứ đang phá hoà hôm nay không phải một luật, mà là một sự chênh lệch số học tình
cờ giữa các tỉ lệ thắng.** Nó đúng, nhưng không ai viết ra rằng nó phải đúng.

### 5.3 · Đề xuất cho phiên 24/08 — vá CẢ BA CÙNG LÚC, và thêm việc thứ tư

| # | việc | vì sao |
|---|---|---|
| ① | thêm `key=lambda x: (-x[1], x[0])` cho **cả ba** chỗ | owner ký 21/08: **cấm vá lẻ** |
| ② | **làm đường lùi KÊU LÊN** — ghi cảnh báo + một bản ghi đo được khi `model_rates` rỗng | đây mới là thứ biến một nợ ngủ yên thành một sự cố im lặng |
| ③ | đo lại đúng ba phép trên sau khi vá, phải ra **0 thay đổi** trên dữ liệu thật | chứng minh vá không đổi hành vi |

**Cấm:** chỉ vá khoá phá hoà rồi bỏ qua đường lùi câm — làm thế là **vá cái không đau và để nguyên
cái đau**.

---

## 6. Cổng kiểm

| cổng | kết quả |
|---|---|
| nguồn đo là production thật (`RM-13`) | ✅ mọi số của GĐ-1 và GĐ-2 đọc **thẳng trên VPS** |
| mốc theo giờ tạo từng bản ghi (`RM-16`) | ✅ CTX đo theo `ts` từng dòng trace, không theo ngày |
| thử đối chứng trước khi kết luận «không đổi» | ✅ phép A — `set` thật cho 3 thứ tự khác nhau |
| không đọc lane T-B trước 24/08 | ✅ **không chạm** |
| không hạ sàn dự tuyển | ✅ **không chạm**, và ghi rõ lý do cấm |
| không sửa production | ✅ **0 tệp mã thay đổi**, không deploy, không restart |

**Vắng log KHÔNG phải bằng chứng vắng chạy** (`RM-20`): journal không có dòng *«Dynamic WR loaded»*
nào từ 16/08, nhưng đó là vì `print()` trong worker của scheduler bị bọc chống stdout đóng. Bằng
chứng đúng là **dấu vết dữ liệu** — `predictions` có dòng của cả ba model tới 22/08.

---

## 7. Vướng vấp

1. **Suýt kết luận `model_rates` luôn rỗng.** Đọc `model_rates = {}` ở `:7839` rồi kết luận trọng
   số win-rate «không làm gì cả» — **sai**, đó là khởi tạo. Bắt được vì đi `grep` toàn bộ chỗ dùng
   thay vì đọc một đoạn. Nếu công bố thì đã là một cáo buộc rất nặng và **sai**.

2. **Suýt kết luận ba đường không chạy production** vì journal không có log. Đúng bẫy `RM-20`.

3. **Journal chỉ còn từ 16/08** nên không có log gốc của lượt rỗng 15/08 — phải dựng lại nguyên
   nhân từ `runtime_reliability_model_daily` và từ mã. Ghi thẳng là **không có log gốc**, không
   đoán thêm.

---

## 8. Gỡ về

**Không có gì để gỡ** — phiên này **không sửa một dòng mã nào**, không deploy, không đụng DB.
Thay đổi duy nhất là **hai mục sổ theo dõi** (`FU-421`, `FU-423` được cập nhật kết quả đo) và
tài liệu. Gỡ bằng `git revert <sha>`.

---

## 9. Theo dõi tiếp

| mã | việc | hạn |
|---|---|---|
| `FU-404` | **chiều tối nay**: job đo phải sinh **cả hai họ** cho 22/08 ⇒ đủ ba điều kiện thì mới nâng `V11102` lên `RUNTIME_PROVEN` | **22/08 tối** |
| `FU-421` | vá **cả ba** chỗ + **làm đường lùi kêu lên** + đo lại | 24/08 |
| `FU-423` | owner chọn lối (a)/(b)/(c) cho `glm-5.1`; **đề xuất (a) GIỮ** | 25/08 |
| *(mới, chưa cấp số)* | vá **nhãn sai** `EMPTY_PROVIDER_OUTPUT` cho đường cầu dao | chờ owner |
| *(mới, chưa cấp số)* | **đếm số ngày bundle thiếu người** — hôm nay không ai đếm | chờ owner |
| — | 24/08 đủ 14 ngày ⇒ **được phép đọc** lane T-B | 24/08 |
| — | 27/08 quyết **DỪNG** cho `gpt-5.5` và `qwen3-max-thinking` | 27/08 |

---

## §62 (A60) — BA LỚP NGUỒN

### `OWNER_SAID`

| nội dung | nguyên văn |
|---|---|
| phạm vi phiên | *«Phiên này là phiên KIỂM CHỨNG + CHẨN ĐOÁN — CẤM sửa production.»* |
| `glm-5.1` | *«Đo trước: rỗng vì API lỗi, vì bộ lọc nội dung, vì prompt miền Nam, hay vì timeout? Phân tích payload/log của đúng 2 lượt rỗng.»* |
| sàn | *«CẤM hạ `MIN_MAU_DU_TUYEN` cho hết đỏ (đã ghi trong sổ).»* |
| `FU-421` | *«Chỉ trình — vá là phiên 24/08.»* · *«đề xuất vá CẢ BA CÙNG LÚC (theo lệnh owner 21/08: cấm vá lẻ)»* |
| lane T-B | *«CẤM đọc kết quả lane T-B trước 24/08.»* |

### `CODE_DID`

| việc | bằng chứng |
|---|---|
| lượt 05:00 đã chạy | `predictions` 22/08: MN 15 official + 11 shadow · MT 7 · MB 7, sớm nhất `05:00:05` |
| prompt đúng phiên bản | **19/19** bản ghi trace tạo 22/08 mang `CTX-18.4`, mới nhất `05:34:53`; **0** bản ghi cũ |
| job đo chưa chạy | `lottery_results` 22/08 **rỗng**; log `SHADOW-PROMOTION-SCORECARD` hôm nay **không có dòng nào** |
| production yên | `lottery_results` và `model_daily_eval` **không đổi**; 0 `Traceback`, 0 `CRITICAL`; `health 200`; PID `2128063` |
| `glm-5.1` hai lượt rỗng | 15/08 `ERROR` 134.064 ms · 18/08 `EMPTY_PROVIDER_OUTPUT` **9 ms** |
| cầu dao ngắt mạch | `gpt_analyzer.py:3560` trả dict không có khoá `prediction` ⇒ `scheduler.py:4370` ghi `EMPTY_PROVIDER_OUTPUT` |
| `FU-421` ba chỗ | phép A 3 thứ tự khác nhau · phép B **0/111** · phép C với WR thật **0/111** · phép C ở đường lùi **107/111** |

### `DOC_SAID` — và chỗ tài liệu **lệch** với mã

| lệch | chi tiết |
|---|---|
| `REPORT_V11102` ≠ dữ liệu | *«rỗng CHỈ xảy ra ở MN»* — thật: **cả ba miền**. Đã rút lại §4.1 |
| `REPORT_V11102` ≠ hệ thống | ghi *«restart 01:0x»* — thật: **`00:00:35`** (`ActiveEnterTimestamp`) |
| nhãn trong DB ≠ điều đã xảy ra | `EMPTY_PROVIDER_OUTPUT` = *«provider response parsed»* trong khi **lượt gọi chưa ra khỏi máy** |
| `docs/FOLLOW_UP_TRACKER.md` ≠ sổ quyết định | vẫn ghi `FU-216` hạn 09/08, `FU-231`/`FU-226` hạn 10/08 — chưa theo `QD-045` |

---

**TanPhatAI cần làm:** cập nhật `docs/FOLLOW_UP_TRACKER.md` — `FU-421` chuyển sang **đã đo, KHÔNG CHỨNG cả ba chỗ** (vá 24/08 kèm việc thứ tư: làm đường lùi `model_rates = {}` kêu lên), và `FU-423` chuyển sang **đã chẩn đoán, đề xuất GIỮ `glm-5.1`** (rỗng có ở cả ba miền, tỉ lệ 2,26% ngang `deepseek-reasoner` 2,22%); theo dõi ba việc: ① **chiều tối nay** job đo phải sinh cả hai họ cho 22/08 — đủ thì mới nâng `V11102` lên `RUNTIME_PROVEN`, chưa đủ thì **cấm nâng**, ② owner chọn lối cho `FU-423` trước 25/08 (đề xuất **giữ**, **cấm hạ sàn**), ③ hai việc mới chưa cấp số cần owner duyệt: vá nhãn sai của đường cầu dao, và đếm số ngày bundle thiếu người — hôm nay **không ai đang đếm**.
