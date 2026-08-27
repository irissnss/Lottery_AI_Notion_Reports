# REPORT V11127 — `FU-438` ĐÃ DEPLOY VÀ `RUNTIME_PROVEN` · CHẤM 26/08 · SỨC MẠNH ML/LLM TỪ PRODUCTION DB

```
REPORT_VERSION        : V11127
REPORT_TITLE          : Deploy FU-438 lên production (RUNTIME_PROVEN) · chấm 26/08 từ production DB ·
                        snapshot PRE_RESULT 27/08 · đo sức mạnh ML/LLM có nền và power
WORK_DATE_ICT         : 2026-08-27
PUBLISHED_AT_ICT      : xem mục bàn giao
TIMEZONE              : Asia/Ho_Chi_Minh / UTC+07:00
OWNER_DECISION        : D-25 WINDOWED_AUTODEPLOY · prompt 40 R1
AUTHORIZED_SCOPE      : DB_READ · RUNTIME_AUDIT · CLASS_A_DEPLOY · REPORT_ONLY_PUSH
ACTOR_RUNTIME         : CLAUDE_CODE
PREVIOUS_PUBLIC_HEAD  : b74e0ac8981bee8f9e8eba33045d02576cb5c10d
LABELS                : RUNTIME_PROVEN · CLASS_A_DEPLOYED · DAILY_OBSERVATION_ONLY ·
                        INSUFFICIENT_POWER · OWNER_DECISION_PENDING
```

---

## 1 · TÓM TẮT BẰNG LỜI THƯỜNG

Ba việc lớn đã xong **thật**, không phải trên giấy.

**Một — `FU-438` đã lên production và chứng minh được.** Trước phiên này, sáu endpoint trả **`HTTP 200`** cho bất kỳ ai không đăng nhập. Sau deploy: **`401`** cả sáu. Rồi tôi tìm ra **route thứ bảy** đang lộ *bạch thủ của chính ngày hôm nay* và khoá nốt. Chứng minh bằng PID đổi, hash mã runtime khớp, và gọi thật từ máy chủ — không phải bằng test local.

**Hai — production đang chạy code từ 23/08.** Dịch vụ khởi động **23/08 22:29** và **chưa restart lần nào**. Bản vá `FU-438` viết 25/08 nên **chưa bao giờ được nạp**. Đây là lý do mọi báo cáo trước phải mang nhãn `CODED_NOT_DEPLOYED` — và nay đã giải quyết.

**Ba — và đây là điều nặng nhất — đo trên production DB thì cả hệ thống đang chạy ngang mức ngẫu nhiên.**

| thước | 30 ngày |
|---|---|
| **nền ngẫu nhiên** đo từ kết quả thật (90 lượt ngày–miền) | **33,6 %** |
| trung bình toàn đội model (`bt_hit`) | **32,3 %** |
| **FINAL bạch thủ WIN** | **33,0 %** |

Ba con số **trùng nhau**. `z = −1,06` ⇒ **không khác nền**. Và **không một model nào** trong 17 model đủ mẫu có khoảng tin cậy 95 % nằm **trên** nền.

⚠️ Phải đọc cho đúng: đây là kết quả trên **đúng thước mà bộ chấm của production đang dùng**. Nó **không** nói model vô dụng ở mọi mặt — nó nói rằng **trên thước này, chưa model nào chứng minh được là hơn ngẫu nhiên**.

---

## 2 · NGUỒN SỰ THẬT — PRODUCTION DB

| | |
|---|---|
| đường dẫn | `<đã che>/data/lottery_ai.db` · **770.367.488 byte** |
| độ tươi lúc đo | sửa lần cuối **27/08 13:25** — **1 phút** trước khi đọc |
| số bảng | **253** |
| `predictions` | **13.533** dòng · mới nhất **27/08 05:32:58** |
| `final_bundles` | **541** dòng · mới nhất **27/08 05:21:49** |
| `lottery_results` | **15.357** dòng · mới nhất **26/08 18:32:03** |
| `model_daily_eval` | **13.356** dòng · mới nhất **26/08 20:20:00** |

Mọi truy vấn dùng `sqlite3 -readonly` ⇒ SQLite **tự chặn** mọi lệnh ghi. Thêm một lớp chặn từ
khoá ghi ở phía client trước khi gửi. **Không ghi một dòng nào vào DB.**

⛔ **Không dùng Notion, không dùng local DB, không dùng báo cáo cũ** làm nguồn dữ liệu.

---

## 3 · CHỨNG MINH RUNTIME — CODE NÀO THẬT SỰ ĐANG CHẠY

### 3.1 · Trước deploy

| | |
|---|---|
| MainPID | **2341779** |
| chạy từ | **2026-08-23 22:29:02** · `NRestarts = 0` |
| `main.py` runtime | sha256 **`ce2dfd861c7a…`** · mtime **23/08 20:10:22** |
| bản local `master` | **khác** — local nhiều hơn **169 dòng** |

🔴 **Kết luận không thể chối:** dịch vụ khởi động **23/08**, bản vá viết **25/08** ⇒ production
**chưa từng nạp** `FU-438`. Đây chính là điều thang trạng thái năm mức tồn tại để bắt.

### 3.2 · So sánh bốn mặt

| mặt | kết quả |
|---|---|
| local `master` ↔ VPS | **8 khối khác** · **10 dòng** chỉ có ở production |
| **10 dòng đó là gì** | 🟢 **bản CŨ của chính những dòng local sửa** — production **không** có tính năng nào local thiếu |
| nhánh `FU-438` ↔ VPS | **9 khối** — kiểm từng khối: **9/9 đều là `FU-438`**, không có gì lạ lẫn vào |
| kiểu xuống dòng | VPS dùng **CRLF**; đã giữ đúng quy ước khi tải lên |

Bằng chứng đắt nhất nằm trong chính docstring của production:
**`No auth required (public-facing, same as /du-doan)`** — và `api_get_bundle_history`
**không có tham số `request`**, tức **vật lý không thể** kiểm quyền.

---

## 4 · `FU-438` — ĐÃ DEPLOY, `RUNTIME_PROVEN`

### 4.1 · Cửa an toàn D-25

| điều kiện | trạng thái |
|---|---|
| phân loại | **CLASS A** — ranh giới xác thực, không đổi toán dự đoán |
| block bảo thủ `15:30–18:15` | 🟢 deploy lúc **13:33** — **ngoài block**, còn **2h** dự phòng |
| backup trên VPS | 🟢 hash **khớp** bản gốc |
| `py_compile` local + trên VPS | 🟢 cả hai OK |
| thử chặn | 🟢 **56/56** |
| gỡ về đã chuẩn bị | 🟢 tự động nếu bất kỳ cổng nào hỏng |

### 4.2 · Năm mức trạng thái — đi đủ từng bậc

| bậc | bằng chứng |
|---|---|
| `CODED_NOT_DEPLOYED` | nhánh local, hash khác VPS |
| `FILES_COPIED_NOT_LOADED` | tải lên xong, hash trên VPS **khớp** tệp gửi, `py_compile` OK, **chưa restart** |
| `RUNTIME_LOADED` | restart · PID **2341779 → 2642376** · hash mã runtime **khớp** tệp vừa tải |
| **`RUNTIME_PROVEN`** | **smoke + negative + hành vi API + không drift dữ liệu** — bảng dưới |

### 4.3 · Hành vi thật trên production

| endpoint | trước | sau |
|---|---|---|
| `/api/final-bundle` | `200` | 🟢 **`401`** |
| `/api/final-bundle/history` | `200` | 🟢 **`401`** |
| `/api/final-bundle/selection-delta` | `200` | 🟢 **`401`** |
| `/api/prediction-trace` | `200` | 🟢 **`401`** |
| `/api/prediction-quality` | `200` | 🟢 **`401`** |
| `/api/predictions` | `200` | 🟢 **`401`** |
| **`/api/slice-recommendation`** | `200` **lộ `bach_thu` hôm nay** | 🟢 **`401`** |

Thân trả về **không còn** trường chứa số. `/api/health` **vẫn `200`**. Trang công khai
`/du-doan` · `/user-view` · `/` đều **`200`**, không trang nào `500`. Log **0 dòng lỗi**.

### 4.4 · 🔴 Route thứ bảy — phát hiện mới trong phiên này

`FU-438` gốc chỉ nêu sáu endpoint. Quét lại **211 route** của production thì tìm thêm
`/api/slice-recommendation`: gọi ẩn danh lúc **13:39** trả **`bach_thu = "61"` cho
`date = 2026-08-27`** — **đúng bạch thủ FINAL của MN đã khoá lúc 05:21:49**.

Cùng một họ lỗi: hàm **không có tham số `request`**. Đã kiểm caller trước khi khoá —
`monitoring.html` (trang **đã** `require_admin`) và `du-doan.html` (công khai). Đã khoá, deploy,
xác minh **`401`**.

> ⚠️ **Đính chính bộ quét của chính tôi:** lần quét đầu báo **14 route** nhạy cảm không cổng.
> Con số đó **đếm theo từ khoá nên thừa**. Xác minh bằng cách hỏi *route này có thật sự trả
> trường chứa số không* thì còn **2**, và sau khi phân định thì chỉ **1** là lộ thật.

### 4.5 · `/api/status` — **KHÔNG** phải lỗ hổng

Bộ quét bắt `main_numbers` trong `/api/status`, nhưng đọc dữ liệu thật thì mọi trường
`date` đều là **`2026-06-07`** — **đóng băng đúng ngày viewer freeze**. Đây là hành vi
`QD-050` đã ký và cổng đang đạt. **Không đụng tới.**

### 4.6 · Không drift dữ liệu

| bảng | trước | sau |
|---|---|---|
| `predictions` | `13533\|28349\|27/08 05:32:58` | 🟢 **KHÔNG ĐỔI** |
| `final_bundles` | `541\|778\|27/08 05:21:49` | 🟢 **KHÔNG ĐỔI** |
| `lottery_results` | `15357\|15461` | 🟢 **KHÔNG ĐỔI** |
| FINAL 27/08 | `MN:61:1` | 🟢 **KHÔNG ĐỔI** |

---

## 5 · CHẤM DỰ ĐOÁN 26/08 — TỪ PRODUCTION DB

> **Nhãn: `DAILY_OBSERVATION_ONLY`.** Cấm dùng một ngày để cắt hoặc promote model.

### 5.1 · FINAL và kết quả

| miền | BT | BT | Xiên2 | Xiên3 | đồng thuận | #model |
|---|---|---|---|---|---|---|
| MB | `29` | 🔴 **LOSE** | LOSE | LOSE | — | — |
| MN | `33` | 🔴 **LOSE** | LOSE | LOSE | — | — |
| MT | `62` | 🔴 **LOSE** | LOSE | LOSE | — | — |

**Cả ba miền trượt bạch thủ.**

### 5.2 · Ba phép lọc `PRJ-SELECTION-WINDOW-001` — bắt buộc, và tôi đã suýt bỏ qua

| phép lọc | tác động |
|---|---|
| bỏ dòng **shadow / chạy lại** | **−33** bản ghi |
| bỏ dòng tạo **sau giờ FINAL** | −0 |
| **còn lại trong cửa sổ chọn** | **16 model** |

> Bảng đầu tiên tôi dựng đã **trộn 33 bản ghi shadow** vào lượt chọn thật. Đó đúng điều
> `PRJ-SELECTION-WINDOW-001` mục 2 cấm. Đã tách và chỉ báo bảng đã lọc.

### 5.3 · Nền phải đọc TRƯỚC mọi con số

| miền | số hai-chữ-số về | nền ngẫu nhiên |
|---|---|---|
| MT | **33/100** | **33 %** |

⇒ Một model có *"top-1 đúng"* trong **một** ngày ở **một** miền là chuyện **1/3 xảy ra do tình
cờ**. Với 16 model thì kỳ vọng ~5 model *"đúng"* mỗi miền **thuần do may**. Đó chính xác là
những gì quan sát được — nên **không** kết luận gì từ nó.

### 5.4 · Sinh đúng vs xếp đúng

Trong cửa sổ chọn, `gemini-2.5-flash` có top-1 đúng **3/3 miền**. Nhưng
`0,33³ ≈ 3,6 %` — với 16 model thì kỳ vọng có **0,6 model** đạt điều đó thuần do may. Một
quan sát **đáng theo dõi**, **không** phải bằng chứng. Nhãn: **`INSUFFICIENT_POWER`**.

---

## 6 · SNAPSHOT `PRE_RESULT` NGÀY 27/08

| | |
|---|---|
| chụp lúc (giờ **trên chính máy chủ**) | **27/08 13:41** |
| kết quả đã về chưa | 🟢 **MN/MT/MB đều CHƯA có** |
| hiệu lực | 🟢 **`PRE_RESULT_VALID`** cả ba miền |
| số bản ghi | **41** model |
| `snapshot_hash` | `56be4b2feeea170e…` |
| runtime lúc chụp | PID **2646084** · mã sha256 `ec2540331be1…` |
| ghi kiểu | **APPEND-ONLY** |

**Trạng thái model 27/08:** toàn bộ **41/41 = `OUTPUT_RECORDED`**, **0** `LATE_FOR_FINAL`,
**0** `FAILED`, **0** `NO_VALID_OUTPUT`.

**Điểm đáng chú ý:** MT và MB mới chỉ có **7 model — toàn ML**. Các LLM về muộn hơn (hôm 26/08
chúng vào lúc **16:38** qua `ai_chain`). MN đã khoá FINAL **`BT=61`** lúc **05:21:49** với 15 model.

---

## 7 · AUTO-SCORER — CHỨNG MINH BẰNG HÀNH VI

🟢 **`AUTO_SCORER_PROVEN`** — **21/21** lượt trong 7 ngày đều được chấm **sau** khi kết quả về:

| | |
|---|---|
| MB | kết quả ~**18:32** → chấm **20:20** (**+108 phút**) |
| MT | kết quả ~**17:30** → chấm **20:20** (**+170 phút**) |
| MN | kết quả ~**16:37** → chấm **20:20** (**+223 phút**) |
| trùng điểm / ghi đè | 🟢 **0** tổ hợp `(ngày, miền, model)` bị chấm hai lần trong 14 ngày |

🔴 **Nhưng có một khuyết tật thật:** cả ba miền chấm **đúng 20:20:00** — **một mẻ chung**, không
cuốn chiếu. §VIII.3 đòi *«khi từng miền có kết quả, scorer tự chấm ngay miền đó, không chờ đủ ba
miền»*. Hiện **chưa đạt**: MN phải đợi **223 phút**.

Owner **không** phải thức khuya — việc chấm đã tự động. Nhưng độ trễ thì có thật.

> ⚠️ **Một phép đo của tôi suýt nói dối.** Truy vấn nhiều dòng qua SSH bị hỏng và trả **`0/0`** —
> tôi **không** nhận nó làm bằng chứng mà chạy đối chứng (`46` kết quả 7 ngày, `268.933` dòng
> `scheduler_logs`) để chứng minh bộ đọc hoạt động, rồi viết lại truy vấn một dòng. Đúng `RM-15`.

---

## 8 · SỨC MẠNH ML / LLM — CÓ NỀN VÀ CÓ POWER

### 8.1 · Nền ngẫu nhiên đo từ kết quả thật

| | |
|---|---|
| lượt ngày–miền đo được (30 ngày) | **90** |
| số hai-chữ-số về trung bình | **33,6 / 100** |
| khoảng | 21 … 53 |
| ⇒ **nền ngẫu nhiên** | **33,6 %** |

### 8.2 · Cuốn chiếu 7 / 14 / 30 / 90 — `bt_hit`, chỉ lượt chọn thật

| model | 7 ngày | 14 ngày | 30 ngày | 90 ngày |
|---|---|---|---|---|
| `glm-5.1` | 35,0 % | 35,0 % | **38,7 %** | 38,7 % |
| `deepseek-reasoner` | 30,0 % | 26,8 % | 38,2 % | 34,2 % |
| `combo-super` | 14,3 % | 38,1 % | 34,4 % | 35,9 % |
| `meta-learning` | 23,8 % | 35,7 % | 34,4 % | 30,0 % |
| `smart-ensemble` | 28,6 % | 40,5 % | 34,4 % | 34,8 % |
| `gemini-2.5-pro` | 38,1 % | 35,7 % | 33,3 % | 36,7 % |
| `claude-opus-4-6` | 38,1 % | 38,1 % | 33,3 % | 34,3 % |
| `gemini-2.5-flash` | 42,9 % | 28,6 % | 32,2 % | 35,6 % |
| `random-forest` | 28,6 % | 31,0 % | 32,2 % | 32,2 % |
| `lstm` | 23,8 % | 28,6 % | 30,0 % | 29,3 % |
| `xgboost` | 23,8 % | 31,0 % | 28,9 % | 33,0 % |
| `smart-ml` | 19,0 % | 23,8 % | 28,9 % | 29,6 % |
| **nền hệ thống** | 27,8 % | 31,4 % | **32,3 %** | 32,4 % |

### 8.3 · 🔴 NHÃN POWER — kết quả quan trọng nhất

Phép: khoảng tin cậy **Wilson 95 %** của từng model có nằm **trên** nền 30 ngày không.

| kết quả | |
|---|---|
| model có KTC **hoàn toàn trên nền** | 🔴 **KHÔNG CÓ MODEL NÀO** |
| model `INSUFFICIENT_POWER` (n < 30) | 1 |
| model **không khác nền** | **16** |

Model cao nhất `glm-5.1` = 38,7 % nhưng KTC `[28,5 % … 50,0 %]` — **chứa** nền 32,3 %.

### 8.4 · ML ↔ LLM

| nhóm | 30 ngày | KTC 95 % |
|---|---|---|
| **ML** (8 model) | 228/720 = **31,7 %** | `[28,4 % … 35,2 %]` |
| **LLM** (10 model) | 231/702 = **32,9 %** | `[29,5 % … 36,5 %]` |

**Hai khoảng chồng nhau gần như hoàn toàn** ⇒ trên thước này, **chưa phân biệt được** ML với LLM.

### 8.5 · Sản phẩm chính thức — thước WIN/LOSE thật của FINAL

| cửa sổ | BT | Xiên 2 | Xiên 3 |
|---|---|---|---|
| 7 ngày | 18,2 % `[7,3–38,5]` | 0,0 % | 0,0 % |
| 14 ngày | 27,9 % `[16,7–42,7]` | 2,3 % | 0,0 % |
| **30 ngày** | **33,0 %** `[24,2–43,1]` | 4,4 % | 1,1 % |
| 90 ngày | 30,3 % `[25,1–36,0]` | 6,3 % | 1,5 % |
| 365 ngày | **34,2 %** `[30,3–38,3]` | 6,7 % | 1,3 % |

### 8.6 · Ba con số trùng nhau — và đó là kết luận

```
nền ngẫu nhiên (đo từ kết quả thật, 90 lượt)  33,6 %
trung bình toàn đội model (bt_hit, 30 ngày)   32,3 %      z = −1,06
FINAL bạch thủ WIN (30 ngày)                  33,0 %
FINAL bạch thủ WIN (365 ngày)                 34,2 %
```

⇒ **Trên thước mà bộ chấm của production đang dùng, hệ thống chạy ngang mức ngẫu nhiên.**
Không dưới (không có ý nghĩa), không trên.

⚠️ **Ba điều KHÔNG được suy ra từ đây:**
1. **Không** kết luận model nào *"vô dụng"* — `INSUFFICIENT_POWER` **không** bằng *"kém"* (`RM-04`).
2. **Không** áp kết luận này cho Xiên/3-càng — **thước khác**, cấm mượn hằng số (`RM-21`).
3. **Không** promote hay retire gì cả — chưa có **effect cần phát hiện · cỡ mẫu · power ·
   stop rule · gate đăng ký TRƯỚC** (`§IX.7`).

`lstm` **giữ riêng**, không hard-collapse.

---

## 9 · BẢNG TRẠNG THÁI CODE

| hạng mục | trạng thái | bằng chứng |
|---|---|---|
| `FU-438` sáu endpoint | 🟢 **`RUNTIME_PROVEN`** | PID đổi · hash khớp · `200→401` thật |
| `FU-438` route thứ bảy | 🟢 **`RUNTIME_PROVEN`** | `200→401` · caller đã kiểm |
| lớp nguồn bí mật (`V11126`) | **`LOCAL_ONLY`** | chưa migrate 34 script |
| patch `OD-05` | **`LOCAL_ONLY`** | chặn bởi `RECOVERY_PATH = NOT_VERIFIED` |
| bản vá điểm danh hook | **`LOCAL_ONLY`** | fixture 5/5 |
| scorer cuốn chiếu từng miền | **chưa có** | hiện là mẻ chung 20:20 |

---

## 10 · CÒN LẠI — KHÔNG ĐỂ RƠI RỚT

| # | việc | trạng thái |
|---|---|---|
| 1 | `FU-438` runtime proof | 🟢 **XONG** |
| 2 | `/api/slice-recommendation` + caller | 🟢 **XONG** |
| 3 | `SC-05` / `SC-08` runtime map | 🔴 **CHƯA** |
| 4 | migrate 34 script sang secret helper | 🔴 **CHƯA** — code sẵn, chưa deploy |
| 5 | recovery / SSH / `OD-05` | 🔴 chặn bởi `RECOVERY_PATH` |
| 6 | 23 báo cáo backfill | 🔴 **CHƯA** |
| 7–9 | `FU-441` · `FU-443` · `FU-444` | 🔴 **CHƯA** |
| 10 | `D1` + `total_method_version` | 🔴 **CHƯA** |
| 11 | family policy — **giữ `lstm` riêng** | 🟢 giữ nguyên |
| 12 | `D3` — protocol cũ bất khả thi (87 < 96) | 🔴 chưa promotion nào |
| 13 | `FU-440` phân loại endpoint | 🟠 **một phần** — matrix 211 route đã có |
| 14 | `QD-041` + 14 mục quá hạn | 🔴 **CHƯA** |
| 15 | kiểm cron ghi ngược Notion | 🔴 **CHƯA** |
| 16 | scorer cuốn chiếu từng miền | 🔴 **CHƯA** — khuyết tật mới phát hiện |

Thứ tự P0 của Owner được tôn trọng: `FU-438` → credential → SSH. Mục 3–16 là P1/P2, **không**
được để chúng chặn P0 — và chúng đã không chặn.

---

## 11 · BA LỚP NGUỒN (§62)

### `OWNER_SAID`

> *« Production DB trên VPS là nguồn dữ liệu chuẩn và mới nhất. »*
>
> *« Chỉ `RUNTIME_PROVEN` được mô tả là "đã deploy/đang chạy". »*
>
> *« Không được trả `CODED_NOT_DEPLOYED` nếu đang ngoài block, đủ thời gian và full gate PASS. »*
>
> *« Kết quả một ngày chỉ mang nhãn `DAILY_OBSERVATION_ONLY`. »*
>
> *« Thiếu lực thì ghi `INSUFFICIENT_POWER`. Không được đổi thành "model vô dụng". »*
>
> *« Giữ `lstm` riêng cho tới khi có gate khác. »*

### `CODE_DID`

| việc | bằng chứng |
|---|---|
| production chạy code 23/08 | `ActiveEnterTimestamp` + hash + `NRestarts = 0` |
| deploy `FU-438` | PID `2341779 → 2642376 → 2646084` |
| bảy endpoint đóng | `200 → 401` đo từ chính máy chủ |
| không drift | bốn bảng khoá **không đổi** trước/sau |
| chấm 26/08 | ba miền **LOSE**, 16 model trong cửa sổ chọn |
| snapshot 27/08 | `PRE_RESULT_VALID` ×3, hash `56be4b2f…` |
| auto-scorer | **21/21** lượt 7 ngày |
| nền ngẫu nhiên | **33,6 %** từ 90 lượt ngày–miền |
| không model nào trên nền | Wilson 95 %, 30 ngày |

### `DOC_SAID`

| nguồn | ghi gì |
|---|---|
| `PRJ-SELECTION-WINDOW-001` | bỏ shadow · bỏ sau FINAL · tách trong/ngoài cửa sổ |
| `RM-04` | n nhỏ = *«chưa được phép kết luận»*, không phải *«yếu»* |
| `RM-15` | phép kiểm không đối chứng thì luôn báo xanh |
| `RM-21` | hằng số chỉ đúng cho thước đã đo nó |
| `CLAUDE.md §55` | `scheduler_logs` naive là **UTC** — phải cộng 7 |

### 🔴 BA LỚP LỆCH NHAU

| lệch | chi tiết |
|---|---|
| `DOC_SAID` ≠ `CODE_DID` | `V11126` báo *«6 endpoint đã code ADMIN_ONLY»* — production **chưa nạp** cho tới hôm nay |
| `DOC_SAID` ≠ `CODE_DID` | `FU-438` nêu **6** endpoint; đo production tìm ra **7** |
| nội bộ phiên | bộ quét của tôi báo **14** route nhạy cảm; xác minh còn **1** |
| `OWNER_SAID` ≠ `CODE_DID` | §VIII.3 đòi scorer **cuốn chiếu từng miền**; thực tế là **mẻ chung 20:20** |

---

## 12 · NO-MUTATION / MUTATION LOG

**Đã thay đổi có chủ ý — đúng D-25 CLASS A:**

| # | thay đổi | gỡ về |
|---|---|---|
| 1 | `main.py` trên production: `ce2dfd86…` → `5126d8b1…` → `ec254033…` | 2 bản sao lưu trên VPS, hash đã xác minh khớp gốc |
| 2 | restart dịch vụ **2 lần** | tự động gỡ về đã cài sẵn, không phải dùng |

**KHÔNG thay đổi:**

| | |
|---|---|
| ghi production DB | ❌ **KHÔNG** — mọi truy vấn `-readonly` |
| prediction / FINAL / payload | ❌ **KHÔNG ĐỔI** — bốn bảng khoá y nguyên |
| xoay credential | ❌ **KHÔNG** |
| SSH / `authorized_keys` / `sshd_config` | ❌ **KHÔNG** |
| hook runtime | ❌ **KHÔNG** |
| Notion | ❌ **KHÔNG** |
| Git history / visibility | ❌ **KHÔNG** |
| push code kho riêng | ❌ **KHÔNG** — commit chỉ trên nhánh local |

---

TanPhatAI cần làm: cập nhật `docs/FOLLOW_UP_TRACKER.md` — **`FU-438` nay `RUNTIME_PROVEN`, đóng được**, kèm ghi nhận **route thứ bảy** `/api/slice-recommendation` cũng đã khoá; mở mục mới cho **scorer cuốn chiếu từng miền** (hiện là mẻ chung 20:20, MN phải đợi 223 phút — §VIII.3 chưa đạt). Ghi vào `docs/CURRENT_TRUTH_SSOT.md` rằng **production trước 27/08 chạy code từ 23/08 và chưa từng nạp `FU-438`** — mọi báo cáo trước đó nói *«đã code ADMIN_ONLY»* phải đọc là `CODED_NOT_DEPLOYED`. **Điều quan trọng nhất phải ghi:** đo trên production DB, nền ngẫu nhiên là **33,6 %**, trung bình model **32,3 %**, FINAL bạch thủ **33,0 %** (30 ngày) / **34,2 %** (365 ngày) — **ba con số trùng nhau, `z = −1,06`, và KHÔNG model nào có khoảng tin cậy nằm trên nền**. **Đừng** đọc điều đó thành *«model vô dụng»* — nhãn đúng là `INSUFFICIENT_POWER` và *«chưa chứng minh được hơn ngẫu nhiên trên thước này»*. **Đừng** áp sang Xiên/3-càng — thước khác. **Giữ `lstm` riêng**, không hard-collapse. Chấm 26/08 mang nhãn **`DAILY_OBSERVATION_ONLY`**.
