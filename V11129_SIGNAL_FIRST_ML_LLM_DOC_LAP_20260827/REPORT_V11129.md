# REPORT V11129 — SIGNAL TRƯỚC RANKING: ĐO ML VÀ LLM ĐỘC LẬP THEO HỢP ĐỒNG KHOÁ TRƯỚC

```
REPORT_VERSION        : V11129
REPORT_TITLE          : Đăng ký hợp đồng đo signal · tách pool ML/LLM tại K=10 ·
                        GO/NO-GO cho ranking · audit prompt từ hàm đang serve
WORK_DATE_ICT         : 2026-08-27
PUBLISHED_AT_ICT      : xem mục bàn giao
TIMEZONE              : Asia/Ho_Chi_Minh / UTC+07:00
OWNER_DECISION        : D-28 SIGNAL_FIRST_GENERATION (khoá 27/08 21:19)
AUTHORIZED_SCOPE      : DB_READ · RUNTIME_AUDIT · CLASS_A_DEPLOY · REPORT_ONLY_PUSH
ACTOR_RUNTIME         : CLAUDE_CODE
PREVIOUS_PUBLIC_HEAD  : ac8b74a37cf7258cac65ef50d878bdb5a6e88a44
PREREG_HASH           : 8a163adc3cf027f169b342060ee4ea81ed6b0bcb6d8956c7
LABELS                : NO_GO_RANKING · INSUFFICIENT_POWER · RETROSPECTIVE_DIAGNOSTIC ·
                        WAIT_LIVE · OWNER_DECISION_PENDING
```

---

## 1 · TÓM TẮT BẰNG LỜI THƯỜNG

Phiên này khoá thước đo **trước** khi nhìn kết quả, rồi tách pool ML và pool LLM ra đo riêng ở
cùng kích thước `K = 10`.

**Kết quả, và nó rất thẳng:**

| nguồn | hit rate | chênh nền |
|---|---|---|
| `ML_PURE_MATH` | **33,33 %** | **−0,54 điểm** |
| `LLM` | **34,77 %** | +0,90 điểm |
| kết hợp hai nguồn | 34,13 % | +0,26 điểm |
| 🎲 **pool SINH NGẪU NHIÊN** *(seed ghi trước khi đo)* | **34,25 %** | +0,38 điểm |
| **nền toàn cục** | 33,87 % | — |

**Một pool 10 số sinh ngẫu nhiên xếp trên pool ML.** Không nguồn nào qua gate. **`NO-GO`.**

**Nhưng — và đây là phần quan trọng hơn kết quả:** hợp đồng đăng ký trước đã tính rằng với
`n = 273`, hiệu ứng **nhỏ nhất phát hiện được** là **+9,3 điểm**. Nên kết quả trên **không**
chứng minh hệ thống vô dụng. Nó chứng minh **thước đo hiện tại không đủ nhạy**:

| lợi thế | cần bao nhiêu lượt | = bao lâu |
|---|---|---|
| **+3 điểm** *(rất đáng kể về kinh tế)* | 2.602 | **867 ngày ≈ 28,5 tháng** |
| +5 điểm | 937 | 312 ngày ≈ 10,3 tháng |
| **+9,3 điểm** | 270 | **90 ngày ← đúng dữ liệu hiện có** |

⇒ **Mọi cải tiến ranking dưới 9 điểm đều nằm trong vùng không phân biệt được với dữ liệu 91
ngày.** Đó là lý do **kỹ thuật** của `NO-GO` — không phải cảm tính, không phải bi quan.

---

## 2 · GĐ-0 · PREFLIGHT

| | |
|---|---|
| MainPID | **2671007** · health **200** |
| `main.py` runtime | `ec2540331be1…` — **khớp V11127** ⇒ `FU-438` không regression |
| `scheduler.py` runtime | `a6c8bfff60b6…` — **khớp V11128** |
| production DB | mtime **27/08 21:50** · **253** bảng |
| `predictions` | 13.573 · mới nhất 27/08 17:48:58 |
| `final_bundles` | 543 · mới nhất 27/08 17:36:00 |
| `lottery_results` | 15.364 · mới nhất 27/08 18:31:33 |
| `model_daily_eval` | **13.437** · mới nhất **27/08 20:20:00** |
| roster sống | **17** model đường chính · 30 model kể cả shadow |

Mọi truy vấn `sqlite3 -readonly` + chặn từ khoá ghi phía client. **Không ghi một dòng nào vào DB.**

---

## 3 · GĐ-1 · HỢP ĐỒNG ĐO — KHOÁ TRƯỚC KHI ĐỌC OUTCOME

| | |
|---|---|
| `prereg_hash` | **`8a163adc3cf027f169b342060ee4ea81ed6b0bcb6d8956c7`** |
| đăng ký lúc | **27/08 21:56:05** — **giờ lấy từ chính máy chủ**, không phải đồng hồ local |
| loại bằng chứng | **`RETROSPECTIVE_DIAGNOSTIC`** — ⛔ cấm dùng để promote |

### `K = 10` — chọn bằng ba lý do kỹ thuật, **trước** khi đo

1. Pool gộp hiện tại trung bình **13,5** số ⇒ `K = 10` là phép thử **chặt hơn**, không phải nới
   lỏng để làm đẹp coverage.
2. Cả hai nguồn đều đạt được: ML 8 model × 2 = 16 thô, LLM ~9 × 2 = 18 thô.
3. Coverage kỳ vọng của pool **ngẫu nhiên** tại `K=10` là **98,4 %** — **còn phân biệt được**
   với 100 %; tại `K=14` là 99,7 %, **quá sát trần** nên mất khả năng phân biệt.

⛔ **Cấm đổi `K` sau khi thấy kết quả.**

### Công suất — con số quan trọng nhất của hợp đồng

```
n dự kiến                                     270 lượt ngày–miền
sai số chuẩn                                  2,88 điểm
hiệu ứng NHỎ NHẤT phát hiện được (80% power)  +8,1 điểm
sau hiệu chỉnh Bonferroni (3 phép so)         +9,3 điểm
```

⇒ **Mọi chênh nhỏ hơn ngưỡng này BẮT BUỘC ghi `INSUFFICIENT_POWER`.** Cấm đọc thành
*«không có signal»* hay *«model kém»*.

### Endpoint

| | |
|---|---|
| **primary** | `POOL_RANDOM_HIT_RATE` — xác suất trúng khi chọn **đều** một candidate trong pool đã khoá trước kết quả |
| **primary contrast** | `POOL_RANDOM_HIT_RATE − GLOBAL_BASELINE` |
| **coverage** | **SECONDARY** — ⛔ mọi lần báo **phải** kèm `1−(1−p)^K` |
| hiệu chỉnh đa so sánh | Bonferroni, 3 phép ⇒ `α = 0,0167`, `z = 2,394` |
| stop rule | đọc **đúng một lần** khi `n ≥ 250` |
| seed pool ngẫu nhiên | **20260827** — ghi trước, không sinh lại |

---

## 4 · GĐ-2/4/5 · KẾT QUẢ ĐO

### 4.1 · Đối chứng — chạy **trước** khi đọc kết quả chính

| đối chứng | kỳ vọng | đo được |
|---|---|---|
| **âm** — cố tình chọn số KHÔNG về | ~0 % | 🟢 **0,0 %** |
| **dương** — cố tình chọn số ĐÃ về | 100 % | 🟢 **100,0 %** |
| tập rỗng | bị loại, không kéo trung bình | 🟢 đã loại |
| trùng lặp | tính một lần | 🟢 đã dedupe |
| dòng sau FINAL | bị loại | 🟢 **0** dòng |
| dòng shadow/replay | bị loại | 🟢 **3.203** dòng loại ra |

⇒ **phép đo phân biệt được.**

### 4.2 · Kết quả chính — `K = 10`, nền **33,87 %**

| nguồn | n | hit rate | CI95 (Bonferroni) | chênh nền | coverage (kỳ vọng) |
|---|---|---|---|---|---|
| `ML_PURE_MATH` | 273 | **33,33 %** | `[26,50 – 40,16]` | **−0,54 pt** | 95,2 % (98,4 %) |
| `LLM` | 273 | **34,77 %** | `[27,87 – 41,67]` | **+0,90 pt** | 91,9 % (98,4 %) |
| `POST_COMBINATION` | 273 | 34,13 % | `[27,26 – 41,00]` | +0,26 pt | 97,8 % (98,4 %) |
| 🎲 **pool ngẫu nhiên** | 273 | **34,25 %** | `[27,37 – 41,12]` | +0,38 pt | 97,4 % (98,4 %) |

**Kích thước pool thực tế:** ML **8,2** · LLM **6,8** · kết hợp **10,0** · ngẫu nhiên **10,0**.

### 4.3 · Ba điều đọc được, và một điều **không** được đọc

1. 🔴 **Pool sinh ngẫu nhiên (34,25 %) xếp TRÊN pool ML (33,33 %)** và ngang bản kết hợp.
2. **Không nguồn nào** có CI nằm trên nền — cả bốn khoảng đều chồng nhau gần hoàn toàn.
3. **ML và LLM không đạt nổi `K = 10`** — chỉ sinh được **8,2** và **6,8** ứng viên phân biệt.
   Đây là phát hiện riêng: **nguồn không đủ đa dạng để lấp một pool 10 số.**
4. ⛔ **KHÔNG được đọc thành «ML kém hơn LLM»** — chênh 1,44 điểm giữa hai nguồn nằm **sâu bên
   trong** vùng không phân biệt được (ngưỡng 9,3 điểm).

### 4.4 · Coverage — đọc kèm điều chỉnh theo `K`, đúng hợp đồng

| nguồn | K thực tế | coverage đo | coverage kỳ vọng nếu **ngẫu nhiên** |
|---|---|---|---|
| ML | 8,2 | 95,2 % | `1−(1−0,339)^8,2` = **96,2 %** |
| LLM | 6,8 | 91,9 % | `1−(1−0,339)^6,8` = **93,1 %** |

⇒ Cả hai coverage **thấp hơn** kỳ vọng ngẫu nhiên cho chính kích thước pool của chúng.
**Coverage không phải thành tích ở đây, và cũng không phải bằng chứng ngược lại** — chênh nằm
trong nhiễu.

### 4.5 · GO / NO-GO

```
ngưỡng hiệu ứng tối thiểu (Bonferroni, 80% power):  +9,3 điểm

ML_PURE_MATH        chênh −0,5 pt  →  INSUFFICIENT_POWER
LLM                 chênh +0,9 pt  →  INSUFFICIENT_POWER
POST_COMBINATION    chênh +0,3 pt  →  INSUFFICIENT_POWER
```

## 🔴 **`NO-GO` — KHÔNG dựng, KHÔNG tối ưu `TOTAL-N1/N2/N3` trong phiên này.**

⛔ **Và `NO-GO` này KHÔNG có nghĩa:** *«pool vô dụng»* · *«ML kém»* · *«LLM hơn ML»* ·
*«không có signal»*. Nó có nghĩa **duy nhất**: với 91 ngày dữ liệu, **không thể phân biệt** bất
kỳ nguồn nào với ngẫu nhiên.

---

## 5 · CẦN BAO NHIÊU MẪU — con số định hình cả chương trình

| lợi thế thật | cần n lượt | = ngày | = tháng |
|---|---|---|---|
| +1 điểm | 23.425 | 7.808 | 257 |
| +2 điểm | 5.856 | 1.952 | 64 |
| **+3 điểm** | **2.602** | **867** | **28,5** |
| +5 điểm | 937 | 312 | 10,3 |
| +8 điểm | 366 | 122 | 4,0 |
| **+9,3 điểm** | **270** | **90** | **3,0 ← hiện có** |

Một hệ thống có lợi thế **+3 điểm** so với ngẫu nhiên là **rất đáng kể**. Nhưng chứng minh nó cần
**hơn 2,5 năm đo liên tục**. 91 ngày hiện có chỉ bắt được lợi thế **≥ 9,3 điểm** — mức gần như
thần kỳ.

**Hệ quả cho hướng đi:** đầu tư vào tinh chỉnh ranking lúc này **không thể kiểm chứng được** bằng
dữ liệu hiện có. Ba hướng đo được nhanh hơn:

| hướng | vì sao đo nhanh hơn |
|---|---|
| **tăng số quan sát mỗi ngày** | đo trên **từng đài / từng giải** thay vì gộp ngày–miền ⇒ nhân số lượt lên nhiều lần với cùng thời gian |
| **chọn thước có nền thấp hơn** | nền BT là 33,9 % nên phương sai lớn. Xiên 2 nền ~4 % ⇒ cùng số ngày, một lợi thế **tương đối** dễ phát hiện hơn nhiều |
| **sửa nguyên nhân cấu trúc** | ML/LLM không sinh nổi 10 ứng viên phân biệt — đó là vấn đề **đo được ngay**, không cần chờ mẫu |

---

## 6 · GĐ-3 · AUDIT PROMPT TỪ HÀM ĐANG SERVE

Dump từ **mã trên VPS mà PID đang nạp** (`RM-14` cấm kết luận từ tệp local):

| | |
|---|---|
| tệp | `gpt_analyzer.py` · sha256 **`0d2be3247abf…`** |
| hàm | `create_analysis_prompt` — **50.741 ký tự mã nguồn · 939 dòng** |
| điểm bơm vào prompt | **30** × `prompt +=` · **8** × `kb_text +=` · 108 × f-string |

### 🔴 46 dấu vết **phải gỡ** khỏi input LLM

| loại | số lần |
|---|---|
| số / top-list **đã lọc sẵn** | **25** |
| **win-rate injection** | **14** |
| **TOTAL vote / FINAL** | **5** |
| **model ranking** | **2** |

### 🟢 Giữ hoặc chuyển thành ngữ cảnh có provenance

| loại | số lần |
|---|---|
| miền / thứ / đài / giải | **189** |
| gan / nóng-lạnh | 26 |
| tần suất / thống kê | 11 |

> ⚠️ **Một đính chính về con số:** đề bài nêu *«create_analysis_prompt khoảng 18.200 ký tự»*.
> Con số **50.741** ở trên là **độ dài MÃ NGUỒN của hàm**, không phải chuỗi prompt phát ra.
> Hai thứ khác nhau. Tôi **chưa emit được prompt thật** vì cần ngữ cảnh DB đầy đủ của một lượt
> sinh — nên phần *«prompt phát ra dài bao nhiêu»* vẫn là **`NOT_VERIFIED`**.

### Vì sao **chưa** thực hiện chuyển đổi atomic

Ba lý do, xếp theo sức nặng:

1. **`§60.1` — cấm làm nửa vời.** 46 dấu vết trên 939 dòng, có 38 điểm bơm. `V11001` đã gỡ 8 khối
   rồi để sót 10 chỗ, khiến phép đo 14 ngày sau đó **vô giá trị**.
2. **Chưa emit được prompt thật** ⇒ chưa có bản đồ đầy đủ để quét ngược sau khi sửa. Sửa mà không
   quét ngược được là `A58_VIOLATION_NO_REVERSE_SCAN`.
3. 🔴 **Và lý do mạnh nhất:** mục 5 cho thấy hiệu quả của thay đổi này **không thể kiểm chứng**
   với dữ liệu hiện có nếu nó dưới 9,3 điểm. Deploy một thay đổi lớn rồi **không đo được nó có
   tác dụng gì** là đúng loại việc `RM-03` cấm.

**Việc đúng phải làm trước:** giải quyết vấn đề **đo được ngay** ở mục 5 — mở rộng đơn vị quan sát
hoặc đổi sang thước có nền thấp hơn — rồi mới đổi prompt và đo bằng thước đủ nhạy.

⛔ **Không** vì thế mà bỏ. `LLM_CONTEXT_ONLY` vẫn đúng về **thiết kế** (LLM không được nhận
shortlist của ML) — đó là lý do độc lập với hiệu năng, và bản đồ 46 dấu vết ở trên đã sẵn sàng
cho phiên thực hiện.

---

## 7 · GĐ-7 · SCORER

### 7.1 · Lượt 20:20 ngày 27/08 — 🟢 **ĐẠT**

| | |
|---|---|
| `model_daily_eval` 27/08 | **0 → 81** bản ghi (lúc 19:27 còn 0) |
| theo miền | MB **27** · MN **27** · MT **27**, đều ghi lúc **20:20:00** |
| khớp `predictions` đã settle | **81 / 81** ✅ |
| **trùng điểm** | 🟢 **0** |
| `bt_hit` | 28/81 |

### 7.2 · Các mốc cuốn chiếu ngày 28/08 — **`WAIT_LIVE`**

| mốc | trạng thái |
|---|---|
| 16:50 (sau MN) · 17:45 (sau MT) · 18:45 (sau MB) · 20:20 (đối soát) | **`WAIT_LIVE`** — chưa tới |

⛔ **Giữ nhãn `RUNTIME_LOADED`.** Ba job **đã đăng ký** (APScheduler ghi rõ ở V11128) nhưng
**chưa nổ lần nào**. Cấm nâng lên `RUNTIME_PROVEN` trước bằng chứng ngày 28/08.

---

## 8 · GĐ-9 · FINAL BẤT BIẾN — 🟢 CHỨNG MINH

| phép kiểm | kết quả |
|---|---|
| số dòng `final_bundles` mỗi (ngày, miền) | 🟢 **1** — 7 ngày, **0** trùng |
| MN 27/08 | `id 778` **không đổi** · `created_at` = giờ khoá gốc **05:21:49** |
| `updated_at` | = **đúng giây** kết quả về (settlement ghi trạng thái) |
| **payload** | `BT = 61` lúc **13:33** và vẫn **61** lúc **22:00** — **không đổi** |
| `bundle_version` 1 → 2 | settlement ghi trạng thái, **không phải viết lại payload** |

> Tôi tự đính chính một mối nghi của chính mình trong phiên: ban đầu thấy `max(id)` của bảng đổi
> `778 → 782` và nghi MN bị ghi đè. **Đọc nhầm** — đó là max toàn bảng, còn id của MN vẫn là 778.

---

## 9 · TRẠNG THÁI TỪNG GIAI ĐOẠN — TRUNG THỰC

| GĐ | việc | trạng thái |
|---|---|---|
| **GĐ-0** | preflight runtime + DB | 🟢 **XONG** |
| **GĐ-1** | hợp đồng đo, khoá trước outcome | 🟢 **XONG** — hash + giờ máy chủ |
| **GĐ-2** | ML pure-math | 🟠 **một phần** — đã tách và đo; audit leakage/artifact **chưa** |
| **GĐ-3** | LLM context-only | 🟠 **audit XONG** (46 dấu vết) · **chuyển đổi CHƯA** — lý do mục 6 |
| **GĐ-4** | khoá độc lập ML/LLM | 🟠 **đo độc lập XONG** · persist hai namespace shadow **chưa** |
| **GĐ-5** | GO/NO-GO | 🟢 **XONG** — **`NO-GO`** |
| **GĐ-6** | deploy regime mới | ⚪ **không áp dụng** — `NO-GO` nên không có regime mới |
| **GĐ-7** | scorer | 🟢 20:20 27/08 **ĐẠT** · mốc 28/08 **`WAIT_LIVE`** |
| **GĐ-8** | 3-càng shadow | 🔴 **CHƯA** — vẫn `MISSING_PIPELINE / NOT_SCORABLE` |
| **GĐ-9** | FINAL bất biến | 🟢 **CHỨNG MINH** · backlog **chưa** |

---

## 10 · BA LỚP NGUỒN (§62)

### `OWNER_SAID`

> *« KHÔNG CÓ SIGNAL THÌ KHÔNG TỐI ƯU RANKING. »*
>
> *« Cấm thay K sau khi thấy kết quả để làm đẹp coverage. »*
>
> *« Cấm đọc coverage mà không điều chỉnh theo K. Coverage cao nhưng đúng bằng random
> expectation không phải signal. »*
>
> *« Nếu chưa đủ live sample: ghi `INSUFFICIENT_POWER` hoặc `WAIT_LIVE`. Không biến thành thất
> bại. Không biến thành thành công. »*
>
> *« Nếu evidence bác tiền đề, được dừng chỉ thị sai. Phải ghi rõ lý do và chọn hành động an toàn
> hơn. »*
>
> *« Không ghi `RUNTIME_PROVEN` khi mới chỉ `RUNTIME_LOADED`. »*

### `CODE_DID`

| việc | bằng chứng |
|---|---|
| hợp đồng khoá trước | hash `8a163adc…` · giờ **máy chủ** 21:56:05 |
| đối chứng | âm **0,0 %** · dương **100,0 %** |
| lọc | **3.203** dòng shadow · **0** dòng sau FINAL |
| kết quả | ML 33,33 % · LLM 34,77 % · kết hợp 34,13 % · **ngẫu nhiên 34,25 %** · nền 33,87 % |
| công suất | ngưỡng **+9,3 điểm**; +3 điểm cần **867 ngày** |
| prompt | `gpt_analyzer.py` sha256 `0d2be324…` · **46** dấu vết phải gỡ |
| scorer 20:20 | 81/81 · **0** trùng |
| FINAL bất biến | 1 dòng/(ngày,miền) · payload không đổi |

### `DOC_SAID`

| nguồn | ghi gì |
|---|---|
| `PRJ-SELECTION-WINDOW-001` | bỏ shadow · bỏ sau FINAL · tách trong/ngoài cửa sổ |
| `RM-03` | cấm kết luận «trước vs sau» thiếu nền và thiếu tính sức mạnh |
| `RM-04` | n nhỏ = *«chưa được phép kết luận»*, **không** phải *«yếu»* |
| `RM-14` | prompt thật ≠ prompt lý thuyết — phải dump từ hàm đang serve |
| `§60.1` | bỏ nửa chừng còn tệ hơn không làm |

### 🔴 BA LỚP LỆCH NHAU

| lệch | chi tiết |
|---|---|
| `DOC_SAID` ≠ `CODE_DID` | đề bài nêu prompt *«~18.200 ký tự»*; đo được **50.741** ký tự **mã nguồn hàm** — hai đại lượng khác nhau, prompt phát ra vẫn `NOT_VERIFIED` |
| tiền đề ≠ đo được | tiền đề *«tách ML/LLM sẽ lộ ra nguồn nào có signal»* — đo được **cả hai đều không phân biệt được với ngẫu nhiên** |
| nội bộ phiên | tôi nghi MN bị ghi đè FINAL; **đọc nhầm** `max(id)` toàn bảng — đã tự đính chính ở mục 8 |

---

## 11 · MUTATION LOG

**Phiên này KHÔNG mutation gì cả.**

| | |
|---|---|
| ghi production DB | ❌ **KHÔNG** — mọi truy vấn `-readonly` |
| deploy / restart | ❌ **KHÔNG** |
| prediction / FINAL / M0 / roster | ❌ **KHÔNG ĐỔI** |
| prompt / regime | ❌ **KHÔNG ĐỔI** — chỉ audit |
| credential · SSH · hook · Notion · Git history | ❌ **KHÔNG** |
| push code kho riêng | ❌ **KHÔNG** |

Mọi thao tác ghi nằm trong thư mục tạm cô lập, ngoài cả hai kho.

---

## 12 · KHÔNG CÓ CÂU HỎI KỸ THUẬT CHO OWNER

Mọi việc Agent tự tra được đã tự làm. CLASS C (SSH · `OD-05` · rotation) vẫn chặn ở
`RECOVERY_PATH = NOT_VERIFIED` — **không đổi**, không phải việc mới.

Điều duy nhất đáng đưa lên **không phải câu hỏi kỹ thuật** mà là hệ quả của mục 5: với thước hiện
tại, **mọi cải tiến dưới 9 điểm đều không kiểm chứng được**. Ba hướng làm thước nhạy hơn đã nêu ở
mục 5 — Agent có thể tự dựng và đo, không cần Owner ký.

---

TanPhatAI cần làm: ghi vào `docs/FOLLOW_UP_TRACKER.md` kết quả **`NO-GO` cho ranking**, kèm **`prereg_hash 8a163adc…`** và giờ khoá **21:56:05 lấy từ máy chủ**. Ghi bốn con số cạnh nhau để không ai đọc lệch: **ML 33,33 % · LLM 34,77 % · kết hợp 34,13 % · pool NGẪU NHIÊN 34,25 % · nền 33,87 %** — **pool sinh ngẫu nhiên xếp trên pool ML**. **Đừng** đọc thành *«model vô dụng»* hay *«LLM hơn ML»*: ngưỡng phát hiện là **+9,3 điểm**, mọi chênh trong bảng đều **nhỏ hơn 1,5 điểm** ⇒ nhãn đúng là **`INSUFFICIENT_POWER`**. Ghi **con số định hình chương trình**: muốn chứng minh một lợi thế **+3 điểm** cần **867 ngày ≈ 28,5 tháng**; 91 ngày hiện có chỉ bắt được lợi thế **≥ 9,3 điểm**. Ghi **scorer: lượt 20:20 ngày 27/08 ĐẠT (81/81, 0 trùng)**, còn ba mốc cuốn chiếu 28/08 là **`WAIT_LIVE`** — **đừng** nâng `RUNTIME_PROVEN`. Ghi **prompt audit: 46 dấu vết phải gỡ** (25 top-list · 14 win-rate · 5 TOTAL/FINAL · 2 ranking) trên `gpt_analyzer.py`, và **chuyển đổi CỐ Ý chưa làm** — lý do ở mục 6. **FINAL bất biến đã chứng minh.** Phiên này **không mutation gì cả**.
