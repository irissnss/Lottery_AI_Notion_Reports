# REPORT V11063 (FU-283) — ĐO ĐỘ TRỄ TỪNG MODEL: NGƯỠNG OWNER KÝ ĐANG CHỆCH

**Ngày:** 2026-08-11 · **Mã đọc:** `DO1108` · **Quyết định:** `QD-063` · **FU-283 hạn 13/08 —
làm xong trước hạn 2 ngày**
**Deploy:** PID `1353489` → `1438110` · `NRestarts=0` · health 200 · admin 401 · **4 bảng khoá số
dòng y hệt** · `QD-041` nguyên vẹn

---

## 1. Tóm tắt

Owner duyệt các đề xuất, `FU-283` là việc đầu. Làm xong **trước hạn 2 ngày**, đủ §52.

**Phát hiện chính: ngưỡng owner ký đang gắn cờ đúng model KHÔNG nguy hiểm.**

| model | TB mọi lượt | % trên đường tới hạn | max | đọc ra |
|---|---|---|---|---|
| `kimi-k2.5` | **231,4s** ⇒ **vượt ngưỡng** | **0/167 = 0%** · **ngừng chạy từ 29/07** | 1.087s | **cắt KHÔNG giảm** rủi ro hạn nào |
| **`glm-5.1`** | 185,5s ⇒ vượt ngưỡng | **32/207 = 15%** · TB-ĐTH **205s** | **1.027s** | **RỦI RO THẬT DUY NHẤT** |

**Agent KHÔNG tự đổi ngưỡng đã đăng ký** (RM-08) — ghi đúng cột owner ký, **thêm** cột đường tới
hạn để owner quyết ở `FU-290`.

**Ba lần agent phải tự sửa khung đo** trước khi ra được con số đúng (mục 7).

---

## 2. Owner yêu cầu gì (nguyên văn)

> *"Các đề xuất của em anh đồng ý em tiến hành 1 cách cẩn thận và tỉ mỉ dùm anh nhé."* — 11/08

Và mục đã ký từ trước:

> `FU-283` · `DO1308`: *"Bỏ phần đối soát tiền. Đổ `latency_seconds` từ trace vào bảng + panel
> `/monitoring` theo §52. Ngưỡng hành động: model nào TB > 180s ⇒ đưa vào danh sách xét cắt ở
> FU-290"* — hạn **13/08**

Và trước đó về cách làm việc:

> *"thà em cập nhật tình hình thì anh còn dễ biết, em âm thầm quá"* — 11/08

**Đã thi hành:** báo tiến độ **5 chặng**, và khi owner hỏi *"em đang làm việc đúng không"* thì trả
lời thẳng **"không, chưa gọi lệnh nào"** thay vì để owner chờ hụt.

---

## 3. Đào bới / phát hiện

### 3.1 · Dữ liệu có thật, đủ 100%

`prediction_trace.jsonl` — **5.120 dòng**, `latency_seconds` có ở **5.120/5.120**, khoảng
**01/06 → 11/08 (72 ngày)**. `duration_seconds` **trùng hoàn toàn** với `latency_seconds`
(0/5.120 dòng khác nhau) ⇒ một trong hai là thừa.

### 3.2 · Ba lần khung đo sai — và vì sao mỗi lần đều "có vẻ đúng"

**Lần 1 — "tổng độ trễ vs biên tới hạn":**

```
11/08 MT  tổng 2.564s   biên còn lại 660s   ⇒ TỔNG > BIÊN
14 lượt gần nhất: TỔNG vượt biên 9 lần
```

Nếu đúng thì MT phải vỡ hạn gần như mỗi ngày. **Nó không vỡ.** ⇒ khung sai.

**Lần 2 — "vậy chắc chạy song song":**

Nghe hợp lý (MAX chỉ vượt biên **1/14 lần**). Nhưng đọc mã:

```
scheduler.py:298   ThreadPoolExecutor(max_workers=1, thread_name_prefix="ai-timeout")
```

**`max_workers=1` KHÔNG phải song song** — đó là **vỏ bọc timeout** (chạy trong luồng riêng để bỏ
được khi quá giờ). Chỗ song song duy nhất là `scraper.py` (**cào kết quả xổ**), không phải gọi
model.

**Lần 3 — "tính cả chuỗi từ đầu tới cuối":**

```
11/08 MT   chuỗi AI 16:38 → 17:01     bundle CHỐT 16:47
```

**11/21 model chạy SAU khi đã chốt** — đó là `Shadow Auto-Eval Start` lúc `16:47:41` trong
journal. Chúng **không nằm trên đường tới hạn**, chậm mấy cũng vô hại.

**Khung đúng — chỉ tính `timestamp ≤ giờ chốt bundle`:**

| ngày | miền | n trước | n sau | tổng trước | **wall trước** | dư hạn |
|---|---|---|---|---|---|---|
| 11/08 | MT | 10 | 11 | 1.000s | **9 phút** | 11 phút |
| 11/08 | MB | 9 | 11 | 792s | 6 phút | 21 phút |
| 10/08 | MT | 10 | 11 | 676s | 5 phút | 11 phút |
| 09/08 | MB | 8 | 11 | 1.102s | 10 phút | 18 phút |

Tổng (1.000s ≈ 17 phút) **lớn hơn** wall (9 phút) ⇒ **có song song ~2× ở tầng khác**, dù
`scheduler.py` chỉ bọc timeout.

### 3.3 · Thủ phạm thật trên đường tới hạn

```
11/08 MT :  glm-5.1 410s · deepseek-reasoner 197s · gpt-oss-120b 105s
11/08 MB :  glm-5.1 253s · deepseek-reasoner 168s · gpt-oss-120b 125s
```

**`glm-5.1` một mình chiếm gần hết wall-clock 9 phút** của chuỗi MT.

30 ngày gần nhất, xếp theo TB **trên đường tới hạn**:

| model | TB-ĐTH | max | ô |
|---|---|---|---|
| **`glm-5.1`** | **205,0s** | **639,6s** | 32 |
| `deepseek-reasoner` | 111,4s | 256,9s | 91 |
| `gpt-oss-120b` | 105,8s | 256,3s | 32 |
| `claude-opus-4-6` | 54,6s | 80,8s | 93 |

### 3.4 · Vì sao ngưỡng owner ký đang chệch

Ngưỡng `TB > 180s` tính trên **mọi lượt**, gồm **11/21 model chạy sau khi bundle đã chốt**. Hệ quả:

- **Gắn cờ `kimi-k2.5`** (TB 231,4s) — model **0/167 = 0% đường tới hạn** và **ngừng chạy từ
  29/07**. Cắt nó **không giảm được rủi ro hạn nào**.
- **Không phản ánh** hành vi đuôi của `glm-5.1`: TB chỉ 185,5s (sát ngưỡng) nhưng
  **max 1.027s = 17 phút**, **vượt toàn bộ ngân sách MT**.

> **Agent KHÔNG tự đổi ngưỡng đã đăng ký** (RM-08 — *"owner tái khẳng định ⇒ THỰC THI, không viện
> nó để hoãn"*, và đăng ký trước là để chống chọn ngưỡng sau khi thấy số). Bảng ghi **đúng** cột
> `tb_giay` theo ngưỡng 180s, **và thêm** `tb_giay_toi_han` · `max_giay` ·
> `pct_tren_duong_toi_han`. **Owner quyết ở `FU-290`.**

### 3.5 · Rủi ro đặt cạnh nhau

| | |
|---|---|
| biên hạn MT | **~13 phút KINH NIÊN suốt 12 ngày**, thấp nhất **8 phút** (04/08) |
| wall-clock chuỗi MT | 5–9 phút |
| `glm-5.1` ngày 11/08 | **410 giây** |
| `glm-5.1` max từng đo | **1.027 giây = 17 phút** |

---

## 4. Hướng xử lý và vì sao

**Không cắt model nào trong phiên này.** Lý do:

1. Cắt model chạm **roster** — `QD-041` khoá tới **21/08**.
2. `FU-283` là mục **đo**, không phải mục **cắt**; mục cắt là `FU-290`.
3. Và số vừa đo cho thấy **danh sách cắt theo ngưỡng hiện tại sẽ cắt nhầm** — cắt `kimi-k2.5`
   (đã ngừng chạy) mà giữ `glm-5.1` (rủi ro thật).

**Việc đúng là dựng phép đo trước, đưa số cho owner, để owner quyết.** Đó chính là `FU-283`.

---

## 5. Đã làm gì — đủ §52

| # | §52 đòi | đã làm |
|---|---|---|
| 1 | bảng shadow đủ 4 cờ | **`model_latency_shadow_v11063`** — 4.046 ô, 72 ngày · `shadow_only=1 diagnostic_only=1 output_eligible=0 owner_approved=0` |
| 2 | API admin | **`/api/admin/do-tre-model`** — `require_admin`, `Cache-Control: no-store` |
| 3 | panel `/monitoring` + `setInterval` | **`loadDoTreModel()`** đăng ký ở **`loadAllSections()` (dòng 8489)** *và* **`setInterval` (dòng 8500)** |
| 4–7 | `CHANGELOG` · `SSOT` · `FOLLOW_UP` · `AUTOMATION_STATE` | ghi bằng **chính công cụ §63 dựng hôm nay** (`_v11062_nang_version.ghi`) — bốn mặt một lệnh, `governance_seq → 405` |
| 8 | báo cáo công khai | tệp này |
| 9 | deploy + restart + smoke | PID `1353489` → **`1438110`** · health **200** · admin **401** |
| 12 | 4 bảng khoá giữ nguyên | **12280 / 495 / 15259 / 12144** — y hệt trước deploy |
| 13 | không đụng `/du-doan`, writer bundle, bộ chọn model | **không đụng** |

Thêm: **cron 21:50** (sau P4 21:40 và anti-trap 21:45) · đăng ký vào **cổng §52 chung** —
`FU283_DO_TRE_V11063=ĐẠT 6/6`.

---

## 6. Cổng kiểm

| cổng | kết quả |
|---|---|
| `_v11055_kiem_p4.py` (§52 chung, 4 bộ đo) | **✓ 4/4 ĐẠT, mỗi bộ 6/6 phép** |
| `_v11062_nang_version.py --kiem` (§63) | **✓ ĐẠT** — bốn mặt đi cùng nhau |
| deploy smoke | health **200** · admin **401** · PID **đổi thật** |
| 4 bảng khoá | **✓ số dòng y hệt** trước/sau |
| cron | **7 dòng materialize**, dòng mới ở 21:50 |

---

## 6bis. §62 (A60) — NGUỒN BA LỚP

### `OWNER_SAID`

| giờ | nguyên văn |
|---|---|
| 11/08 | *"Các đề xuất của em anh đồng ý em tiến hành 1 cách cẩn thận và tỉ mỉ dùm anh nhé"* |
| 11/08 | *"em đang làm việc đúng không anh chờ báo cáo hay sao em?"* |
| ~04/08 (`FU-283`) | *"model nào TB > 180s ⇒ đưa vào danh sách xét cắt ở FU-290"* |

### `CODE_DID`

| mã làm gì | evidence |
|---|---|
| `latency_seconds` có ở **5.120/5.120** dòng trace, trùng hoàn toàn `duration_seconds` | đọc trực tiếp `prediction_trace.jsonl` |
| `scheduler.py:298` là `ThreadPoolExecutor(max_workers=1)` — **vỏ timeout**, không song song | `scheduler.py:298` |
| **11/21 model MT chạy SAU khi bundle chốt** | chuỗi 16:38→17:01 vs chốt 16:47 |
| `kimi-k2.5` **0/167 ô** trên đường tới hạn, mới nhất **29/07** | `model_latency_shadow_v11063` |
| `glm-5.1` **32/207 ô**, TB-ĐTH **205s**, max **1.027s**, còn chạy **11/08** | cùng bảng |
| deploy đổi PID thật `1353489` → `1438110` | `systemctl show lottery -p MainPID` |

### `DOC_SAID`

| tài liệu ghi gì | file:mục | lệch? |
|---|---|---|
| `FU-283` *"model TB > 180s ⇒ xét cắt ở FU-290"* | `docs/FOLLOW_UP_TRACKER.md` | **⚠ ngưỡng đúng hình thức nhưng chệch mục tiêu** — tính trên mọi lượt gồm cả model chạy sau khi chốt |
| `RM-08` *"owner tái khẳng định ⇒ THỰC THI"* | `CLAUDE.md` §61 | **khớp** — nên **không tự đổi** ngưỡng, chỉ thêm cột |
| §52 *"bảng shadow có mà không có panel = VI PHẠM"* | `CLAUDE.md` §52 | **khớp** — panel + `setInterval` đủ |

### Ba lớp lệch nhau ⇒ FINDING

**`DOC_SAID` (ngưỡng đã ký) ≠ `CODE_DID` (thứ thật sự doạ hạn).** Ngưỡng `TB > 180s` sẽ dẫn tới
**cắt nhầm**: bỏ `kimi-k2.5` (đã ngừng chạy, 0% đường tới hạn) mà **giữ** `glm-5.1` (rủi ro thật).
Agent **không tự sửa ngưỡng** — báo lên để owner quyết ở `FU-290`. Đây đúng vai trò của `§62`:
lệch là **dữ liệu**, không phải phiền toái.

---

## 7. Vướng vấp — ba lần tự sửa khung đo

| # | khung sai | phát hiện bằng |
|---|---|---|
| 1 | tổng độ trễ vs biên | **thực tế mâu thuẫn**: tổng vượt biên 9/14 lượt mà MT không vỡ hạn lần nào |
| 2 | "chắc chạy song song" | **đọc mã**: `max_workers=1` là vỏ timeout, không phải song song |
| 3 | tính cả chuỗi đầu–cuối | **đối chiếu giờ chốt**: 11/21 model chạy sau khi bundle đã chốt |

**Cả ba đều có thể ra một báo cáo nghe rất kêu và sai.** Khung 1 cho ra *"MT vượt ngân sách 4 lần
mỗi ngày"*; khung 3 cho ra *"chuỗi MT mất 43 phút"*. Cái cứu là **hỏi lại: nếu vậy thì MT phải vỡ
hạn — sao nó không vỡ?**

---

## 8. Gỡ về

```bash
git revert 30e4681 && systemctl restart lottery
```

Chỉ thêm **bảng đọc + panel + cron**. Không chạm `/du-doan`, writer `final_bundles`, hay bộ chọn
model.

---

## 9. Theo dõi tiếp

| mã | việc | mốc |
|---|---|---|
| ~~**FU-283**~~ | ~~đo độ trễ~~ | **XONG 11/08**, trước hạn 2 ngày |
| **FU-290** | **cần owner quyết:** cắt theo ngưỡng `TB>180s` sẽ **cắt nhầm**. Đề nghị xét thêm `pct_tren_duong_toi_han` | **sau 21/08** (chạm roster, `QD-041` khoá) |
| **FU-398** | lane A/B — 12 cặp, 9 bất đồng | ~**22/08** · cấm đọc sớm |
| **FU-399** | UI `/filter` — **chờ owner mô tả** | — |
| — | `glm-5.1` max **1.027s** vs biên MT **~13 phút** — theo dõi qua panel mới | mỗi ngày |
| — | `duration_seconds` **trùng hoàn toàn** `latency_seconds` (0/5.120 khác) ⇒ một cột thừa | chưa cấp bách |

---

TanPhatAI cần làm: ① ghi **`FU-283` ĐÃ XONG** (`DEPLOYED_LIVE_VERIFIED`, trước hạn 2 ngày) và
`QD-063`; ② **ghi rõ cho `FU-290`**: ngưỡng `TB > 180s` owner ký sẽ **cắt nhầm** — `kimi-k2.5`
vượt ngưỡng nhưng **0% đường tới hạn + ngừng chạy từ 29/07**, còn `glm-5.1` mới là **rủi ro thật**
(15% đường tới hạn, max **1.027s**); ③ ghi rằng agent **KHÔNG tự đổi ngưỡng** (RM-08), chỉ thêm
cột `pct_tren_duong_toi_han` — **đừng ai coi đó là ngưỡng mới**; ④ ghi ba lần sửa khung đo để
không ai đo lại bằng "tổng độ trễ vs biên"; ⑤ ghi **`glm-5.1` cần theo dõi hằng ngày** qua panel
`/monitoring` mới.
