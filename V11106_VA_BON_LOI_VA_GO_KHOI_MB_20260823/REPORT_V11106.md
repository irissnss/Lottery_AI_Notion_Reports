# REPORT V11106 — DEPLOY `FU-419` · VÁ BỐN LỖI HỆ THỐNG · GỠ KHỐI BẦY ĐÀN MB · LANE T-B CHƯA ĐỦ MẪU

**Ngày:** 2026-08-23 (tối) · **Mã đọc:** `SC2308-2` · **Quyết định:** owner ký 05:10 + tối 23/08
**Production:** deploy **3 tệp** · restart `lottery` · PID `2293117 → 2299279`
**Verdict:** `CODE_PUSHED` + `DEPLOYED` + `REPORT_PUBLISHED` — **CHƯA `RUNTIME_PROVEN`**, xem §6

---

## 1. Tóm tắt

Năm việc. **Ba trong năm cho kết quả khác điều đang được tin**, và một trong đó **chặn đúng lúc**
một phán quyết sắp công bố trên nửa số mẫu.

| việc | trạng thái |
|---|---|
| **GĐ-0** đánh giá 23/08 | 1 trúng / 3 miền — **đúng bằng nền**, `n=3` chưa được kết luận. **ĐÍNH CHÍNH §3.1b: MN là LỖI KHÂU CHỌN** — engine xếp `46` (TRÚNG) hạng #1, công bố `73` |
| **GĐ-1** deploy `FU-419` | ✅ 9 bước · `CTX-18.5` |
| **GĐ-2** vá 4 lỗi | ✅ 3 commit riêng · thử chặn **6/6 + 6/6** |
| **GĐ-3** đọc lane T-B | ⛔ **DỪNG Ở BƯỚC 2** — `b+c = 46` so với ngưỡng **96** |
| **GĐ-4** gỡ khối MB | ✅ MB **−10,0%**, MN/MT **không đổi một byte** |

---

## 2. Owner yêu cầu gì (nguyên văn)

> *«Phân tích kết quả dự đoán của 3 miền hôm nay… Trình bày ngắn gọn, minh bạch, có số liệu,
> KHÔNG tô hồng.»*

> *«① `FU-421` (3 chỗ phá hoà)… CÙNG LÚC + làm đường lùi `model_rates={}` KÊU LÊN. Đo lại phải ra
> 0 thay đổi trên dữ liệu thật. ② `FU-425`… ③ `FU-426`… ④ Dòng chị em `tails[:12]`… Mỗi việc 1
> commit riêng. Thử chặn hai chiều bắt buộc.»*

> *«Đọc lane T-B… KỶ LUẬT: CẤM tự ý đổi ngưỡng sau khi thấy số. CẤM kết luận ngoài ngưỡng.»*

> *«BỎ hoàn toàn khối MB MODEL RANKING (chiếm 26,5% prompt MB)… (1) Model MẤT gì… (2) Model ĐƯỢC
> gì… LUẬT BIÊN REGIME: Mọi quyết định THĂNG cho model MB sẽ đếm lại từ mốc hôm nay.»*

---

## 3. Đào bới / phát hiện

### 3.1 · GĐ-0 — kết quả 23/08, đọc thẳng, không tô hồng

| miền | số đuôi ra | **nền THẬT hôm đó** | bạch thủ | kết quả | model output có mặt | số-đầu-trúng |
|---|---:|---:|---|---|---|---|
| MN | 41 | **41%** | `73` | ❌ | **15/15** | 5/15 = **33%** — **dưới nền** |
| **MT** | 42 | 42% | **`15`** | ✅ **TRÚNG** | **15/15** | 7/15 = 47% — trên nền |
| MB | 24 | 24% | `54` | ❌ | **15/15** | 2/15 = **13%** — **bằng nửa nền** |

Kỳ vọng theo nền `0,41 + 0,42 + 0,24 = **1,07**`. Thực tế **1**. **Đúng bằng nền.**
`n = 3` ⇒ **`RM-04`: chưa được phép kết luận** — nêu con số, cấm đọc thành xu hướng.

**Khâu sinh số vs khâu chọn — kết luận từng miền:**

- **Cả ba miền đủ 15/15 model output**, không dòng nào rỗng. Khác hôm qua (22/08 thiếu
  `deepseek-reasoner` ở MN). ⇒ **hôm nay không thiếu ai.**
- **MB là chỗ yếu thật**: chỉ **2/15** model có số đầu trúng, trong khi nền là 24% — tức **bằng
  nửa nền**. Không cách chọn nào cứu được từ một tập ứng viên như thế ⇒ **lỗi khâu SINH SỐ**.
- **MN cũng dưới nền** (33% vs 41%) nhưng nhẹ hơn.
- **MT trên nền** (47% vs 42%) và bundle chọn trúng.

### 3.1b · ĐÍNH CHÍNH NGAY TRONG BẢN NÀY — MN là **LỖI KHÂU CHỌN**, không phải khâu sinh số

> Phần §3.1 phía trên viết MN *«5/15 = 33% — dưới nền»* và xếp nó cùng nhóm với MB như một vấn đề
> **sinh số**. **SAI.** Sáu làn đào xong sau khi bản đầu đã đẩy lên kho công khai, và bằng chứng
> lấy từ **chính blob chẩn đoán của hệ thống** lật ngược kết luận đó. Em đã **tự kiểm chứng lại
> trên VPS** trước khi ghi vào đây.

**MN 23/08 — engine chọn ĐÚNG số trúng, số công bố lại là số khác:**

```
ranked_numbers[0]  =  46   score 0,1397   4 phiếu   ← 46 TRÚNG
top1_reason        =  "selected 46 because score=0.1397, voters=4, lane_votes={'auto_daily': 4}"
bach_thu CÔNG BỐ   =  73   score 0,1256   7 phiếu   ← 73 TRƯỢT
cột top_score      =  0,1256              ← khớp 73, KHÔNG khớp 46
```

Nghĩa là **nguyên liệu ĐỦ và engine đã xếp đúng** — số trúng nằm ở **hạng #1**. Thứ đổi số nằm ở
**sau khâu xếp hạng**.

**Không phải ca lẻ — đo 30 ngày trên VPS:**

```
93 bundle đối chiếu được · LỆCH (bach_thu ≠ ranked_numbers[0]): 13 = 14,0%
   06/08 MN: engine 60 → công bố 95 (WIN)     07/08 MN: engine 60 → công bố 13 (WIN)
   09/08 MN: engine 22 → công bố 54 (LOSE)    14/08 MN: engine 14 → công bố 41 (WIN)
   16/08 MN: engine 32 → công bố 71 (LOSE)    17/08 MN: engine 96 → công bố 89 (WIN)
   19/08 MN: engine 02 → công bố 56 (LOSE)    23/08 MN: engine 46 → công bố 73 (LOSE)
```

**Tám ca hiện ra đều là MN**, và kết cục **4 WIN / 4 LOSE** — nên **KHÔNG được đọc thành «lớp ghi
đè làm hỏng»**. Chưa đo được nó tốt hay xấu; `n` quá nhỏ và chưa có nền cho từng vế.

**Điều CHẮC CHẮN sai, và đó mới là mục phải vá:**

| | |
|---|---|
| `top1_reason` ghi *«selected 46»* | trong khi **46 không được công bố** — **câu này sai sự thật 14% số lần** |
| lớp ghi đè | **không được ghi lại ở đâu** trong blob — không trường nào nói «đã bị đổi bởi X» |
| blob MN 23/08 **tự mâu thuẫn** | `near_miss_anti_trap` liệt kê `73` là *«near miss»* trong khi `73` **chính là bạch thủ đã công bố** |

> Đây là **cùng một họ** với hai lỗi đã vá trong phiên này: `latency_ms = 9 ms` cho một lượt gọi
> 79 giây, và `EMPTY_PROVIDER_OUTPUT` nói *«provider response parsed»* khi lượt gọi chưa rời máy.
> **Ba lần trong một tuần, ba chỗ khác nhau, cùng một khuôn: bản ghi chẩn đoán mô tả một chuyện
> khác với chuyện đã xảy ra.**

→ **`FU-429`** (chờ owner ký).

**Sửa lại kết luận từng miền:**

| miền | bản đầu viết | ĐÚNG là |
|---|---|---|
| **MN** | *«dưới nền — khâu sinh số»* | **LỖI KHÂU CHỌN** — số trúng `46` ở **hạng #1**, công bố `73` |
| MT | cả hai khâu đạt | **giữ nguyên** — `ranked[0] = 15 = bạch thủ = TRÚNG` |
| MB | khâu sinh số hỏng | **giữ nguyên, và nặng hơn**: số trúng đầu tiên ở **hạng #4**, top-3 trượt sạch; và **1 trong 2** model có số đầu trúng (`claude-sonnet-4-6`, số `09`) **đã bị cổng `bt_gate` loại khỏi phiếu** |

**Thêm hai con số bản đầu chưa nêu:**

- `model_count` thật trong bundle: **MN 15 · MT 13 · MB 12** — thấp hơn 15 vì cổng chặn, không
  phải vì thiếu dòng. `incomplete_bundle`: MN **false** · MT **true** (2 model chạm
  `max_voters_cap`) · MB **true** (3 model bị `bt_gate`, ngưỡng `bt<12`).
- `diagnostic_empty_models = []` ở **cả 9 bundle** 21–23/08 ⇒ không lượt rỗng nào trong ba ngày này.

---

### 3.2 · GĐ-3 — lane T-B: **CHƯA ĐỦ MẪU**, và suýt đọc sớm bằng thước sai

```
181 dòng · 181 chấm được · 0 từ chối · mẫu 11/08 → 23/08 = 13 ngày
b = 21   (CONTROL đúng khi T-B sai)
c = 25   (T-B đúng khi CONTROL sai)
n = b + c = 46          ngưỡng đăng ký TRƯỚC: >= 96
```

**46 < 96 ⇒ DỪNG ở bước 2. Không tính z. Không phán quyết.** Và `QD-017` đăng ký **14 ngày**,
hiện mới **13**. ⇒ **chưa tới hạn ở CẢ HAI điều kiện.**

> **SUÝT ĐỌC SỚM BẰNG THƯỚC SAI.** Bộ chấm `_v11089_cham_lane_tb.py:175` tự in:
>
> ```
> trong đó bất đồng (A≠B) : 122   [ngưỡng QD-059: ≥96]
> ```
>
> Nó đem **122** — số dòng mà **HAI DỰ ĐOÁN khác nhau** — so với ngưỡng vốn đăng ký cho **CẶP
> LỆCH KẾT CỤC** (`b+c` = **46**). **Đọc lướt dòng đó là kết luận trên nửa số mẫu.**

**Vì sao hai con số lệch xa thế:** hai bên đoán số khác nhau **122** lần nhưng **phần lớn cùng
trượt** — mà cùng trượt thì **không phân biệt được ai hơn ai**, nên không vào mẫu. Đúng tinh thần
McNemar: ô «cùng đúng» và ô «cùng sai» **không mang thông tin**.

**Tự kiểm chứng lại, không nhận nguyên si kết quả tác nhân:**

```
sqlite3 "SELECT COUNT(*), SUM(bat_dong=1), SUM(trung_control<>trung_tb),
                SUM(trung_control=1 AND trung_tb=0), SUM(trung_control=0 AND trung_tb=1),
                MIN(run_date), MAX(run_date), COUNT(DISTINCT run_date) …"
→ 181 | 122 | 46 | 21 | 25 | 2026-08-11 | 2026-08-23 | 13
```

→ **`FU-427`**, hạn 25/08.

### 3.3 · Đính chính một con số trong chính lệnh của owner

Lệnh ghi khối `MB MODEL RANKING` *«chiếm 26,5% prompt MB»*. Con số **26,5%** lấy từ báo cáo cũ
của agent, nhưng đó là **TỔNG mọi nội dung thống kê model** trong gói MB, **không phải riêng khối
này**.

Đo lại đúng khối, 7 ngày trên VPS: **1.484–1.667 ký tự = 8,83–10,76%** gói ngữ cảnh MB
(≈2,5–2,8% prompt tổng). **Vẫn đáng gỡ** — nhưng em không để một con số sai đi vào báo cáo.

### 3.4 · Một mệnh lệnh mồ côi SẴN CÓ, không do lần gỡ này

`gpt_analyzer.py:736` bảo model:

> *«Khi Context Pack có "BT MODEL RANKING" → tham khảo model nào mạnh BT nhất»*

Trong khi `BT MODEL RANKING` **nằm trong danh sách bị de-herding CẮT** (`:4334`
`_V10768_HERD_SECTION_KEYS`). Prompt đang trỏ vào một khối **đã bị gỡ** ⇒ `PRJ_PROMPT_DANGLING`.
→ **`FU-428`** (chờ owner duyệt).

---

## 4. Hướng xử lý và vì sao chọn

### 4.1 · `FU-421` — điều kiện owner đặt: **ĐẠT, nhưng phải nói cho đúng**

Owner đặt: *«Đo lại phải ra 0 thay đổi trên dữ liệu thật»*. Đo 114 cặp ngày-miền, 60 ngày, VPS:

| lát cắt | Smart Ensemble | Smart ML/Combo |
|---|---:|---:|
| **TOP-2 — lát hệ thống THẬT SỰ đọc** (V8.0 «strict TOP1/TOP2») | **0/114** | **0/114** |
| TOP-3 trở đi | 0/114 | **11/114 ĐỔI** |

**Phần được dùng: 0 thay đổi ✓.** Phần đổi nằm ở **top-3 trở đi**, mà mã lấy **top-2** mỗi model
nên nó **không tới được đầu ra**.

> Em ghi tách ra thay vì gộp thành *«0 thay đổi»*. Gộp lại thì đúng chữ nhưng **giấu mất** một
> nửa sự thật — và nếu sau này ai đó đọc top-3 cho việc khác thì con số gộp sẽ nói dối họ.

### 4.2 · Vì sao việc CHÍNH của `FU-421` là đường lùi, không phải khoá phá hoà

Nếu **cả hai** phép lấy tỉ lệ thắng hỏng ⇒ `wr` về **50 cho mọi model** ⇒ phép cân theo tỉ lệ
thắng **thôi không còn tác dụng**, và khi đó Smart Ensemble hoà đúng biên hạng 0/1 ở **107/111 =
96% số ngày**.

> **Thứ đang phá hoà hôm nay KHÔNG PHẢI MỘT LUẬT, mà là một chênh lệch số học TÌNH CỜ giữa các
> tỉ lệ thắng.** Nó đúng — nhưng không ai viết ra rằng nó phải đúng, và **trước bản vá này không
> ai được báo khi nó thôi đúng.**

Nay đường lùi **in cảnh báo** và **ghi một bản ghi đo được** vào `wr_fallback_rong_v11106`.

### 4.3 · `FU-425` — vá mốc thôi CHƯA ĐỦ

Sửa mốc là sửa **lần này**. Cờ chéo `LECH_DONG_HO` là để bắt **lần sau**, khi lệch vì lý do khác.
Nó đọc từ **một nguồn khác** (`prediction_trace.jsonl`) — không phải kiểm lại chính con số vừa tính.

### 4.4 · `FU-426` — chỉ lưu cho lượt RỖNG, không lưu cho mọi lượt

| lối | được | mất |
|---|---|---|
| **lưu cho lượt rỗng — chọn** | lần rỗng sau **chẩn đoán được ngay trong ngày**; nội dung **đã có sẵn trong bộ nhớ** ⇒ **không thêm một lượt gọi nào** | ~3–5 KB × ~2 lượt/90 — không đáng kể |
| lưu cho mọi lượt | đầy đủ nhất | **đổi một vấn đề nhỏ lấy một vấn đề dung lượng lớn** |

---

## 5. Đã làm gì

### 5.1 · GĐ-1 — `FU-419` DEPLOYED

PID `2128063 → 2293117` · md5 khớp từng byte · `py_compile` **trước** restart · health 200 ·
admin 401 · 0 lỗi · **4 bảng khoá PRE=POST tuyệt đối** (13.250 · 531 · 15.339 · 13.033).
`CTX-18.5` sống, dòng D-1 = `77 distinct tails`.

### 5.2 · GĐ-2 — bốn bản vá, ba commit riêng

**① `FU-421`** — ba chỗ + đường lùi kêu lên. Bản vá **đếm trước khi thay**: kỳ vọng 3 chỗ, tìm
thấy 3; khác 3 thì **dừng lại, không vá bừa**.

**② `FU-425`** — một mốc duy nhất + cờ chéo. Thử chặn **6/6**, gồm **hai phép biên** (19% ⇒ im ·
21% ⇒ đỏ).

> **Bài thử bắt được HAI lỗi trong chính bản vá đầu**, cả hai họ «che tiếng kêu»: hàm dùng
> `__file__` nên `NameError` bị `except` nuốt ⇒ **cờ không bao giờ đỏ**; và
> `except Exception: return None` biến **mọi lỗi thành «không có gì bất thường»**. Nay lỗi trả
> cờ riêng `KHONG_DOI_CHIEU_DUOC`.

**③ `FU-426`** — đường rỗng ghi `reasoning_json` + `raw_response[:2000]`. Thử chặn **6/6**, gồm
phép *«payload hỏng ⇒ phải GHI LÝ DO, không nuốt im»* — đúng lỗi bản vá `FU-425` vừa mắc.

**④ dòng chị em `tails[:12]`** — đo thật trên VPS ngày 23/08:
`01, 04, 05, 18, 20, 21, 22, 23, 26, 27, 28, 29 ...` → **`41 distinct tails`**.

### 5.3 · GĐ-4 — gỡ trọn khối `MB MODEL RANKING`

Gỡ **3.680 ký tự · 57 dòng** tại `gpt_analyzer.py:5372–5428`. Hai mệnh lệnh bị gỡ:

```
💡 MB {thứ} TRUST: {model} historically mạnh nhất
   → Nếu output giống models này → TĂNG CONFIDENCE nhẹ
⚠️ MB {thứ} CAUTION: {model} historically yếu → GIẢM CONFIDENCE
```

**Bằng chứng dump TRƯỚC/SAU trên VPS (ngày 2026-08-24):**

| miền | TRƯỚC | SAU | đổi |
|---|---|---|---|
| MN | 12.194 kt · `d3d5ed93` | 12.194 kt · `d3d5ed93` | **không đổi một byte** |
| MT | 10.762 kt · `5c07bf99` | 10.762 kt · `5c07bf99` | **không đổi một byte** |
| **MB** | 15.372 kt · `045aa3e2` | **13.832** kt · `1433a381` | **−1.540 kt = −10,0%** |

Chuỗi `MB MODEL RANKING`: **1 → 0**. **MN/MT không suy suyển ⇒ đúng phạm vi.**

**MODEL MẤT GÌ:** một bảng tỉ lệ thắng all-time theo thứ trong tuần, và hai mệnh lệnh bảo nó
chỉnh confidence theo việc output có giống model khác hay không.

**MODEL ĐƯỢC GÌ:** hết bị bảo tin theo một bảng **có lẫn model đã ngừng dự đoán** (truy vấn lấy
`all-time`, **không có điều kiện thời gian nào**); ngữ cảnh MB sạch hơn **10,0%**; và nó phải
**tự phân tích theo năng lực** thay vì soi xem mình có giống số đông không.

**Vì sao khối lọt lưới de-herding:** tiêu đề thụt lề `  📊` chứ không phải `### `, nên
`_V10768_HERD_SECTION_KEYS` không bắt được. Đo 7 ngày: chuỗi đó **vẫn còn** trong gói **sau khi**
de-herd đã chạy.

> **KHÔNG HỨA TĂNG ĐỘ TRÚNG.** Chưa phép đo nào chứng minh khối này làm giảm độ trúng; lý do gỡ
> là **nó dạy sai** và **nó chứa số cũ**. Mọi kết luận về độ trúng phải chờ **đo tiến, có nền,
> có z**.

**LUẬT BIÊN REGIME (owner ký):** mọi quyết định **THĂNG cho model MB đếm lại từ 2026-08-24** —
ngày đầu tiên MB chạy trọn vẹn trên gói không còn khối này. Dữ liệu MB trước mốc thuộc regime
**khác**, **cấm trộn**.

### 5.4 · Deploy ba tệp — nghiệm thu đầy đủ

| phép | kết quả |
|---|---|
| md5 local = VPS | `main.py` `a5472268…` · `scheduler.py` `c855e092…` · `gpt_analyzer.py` `8123da61…` — **khớp cả ba** |
| `py_compile` **trước** restart | **OK cả ba tệp** |
| PID | `2293117 → 2299279` — **đã đổi** |
| smoke | `health = 200` · `admin = 401` |
| lỗi 3 phút sau restart | **0** |
| **4 bảng khoá PRE = POST** | `13.250` · `531` · `15.339` · `13.033` — **không đổi một dòng** |
| xác nhận prompt sống | `CTX-18.6` · MB `1433a381` = **đúng bản dump thử** · khối MB = **0** |

---

## 6. Cổng kiểm

| cổng | kết quả |
|---|---|
| `_v11106_thu_chan_fu425.py` | `THU_CHAN_FU425_V11106=ĐẠT` — **6/6** |
| `_v11106_thu_chan_fu426.py` | `THU_CHAN_FU426_V11106=ĐẠT` — **6/6** |
| `_v11062_nang_version.py --kiem` | `ĐẠT` — bốn mặt đi cùng nhau |
| `_v11050_kiem_cong.py` (K1) | **8/8** |
| `_v11044_cong_so_hieu.py` | `KHỚP` |
| `_v11034_kiem_cheo_quyet_dinh.py` | `SẠCH` |
| `_v11101_cong_che_stderr.py` | `SẠCH` |

**Vì sao CHƯA `RUNTIME_PROVEN`:** `CTX-18.6` và bốn bản vá mới lên máy lúc **20:1x**, sau khi cả
ba miền đã chốt số hôm nay. **Lượt production đầu tiên trên bản mới là 05:00 ngày 24/08.**
`RM-12` cấm tự nâng tầng ⇒ chờ đọc lại sau lượt đó.

---

## 7. Vướng vấp

1. **Bản vá `FU-425` đầu tiên làm hỏng cú pháp** — neo vào chuỗi **không có phần thụt lề**, mà
   `_persist_official_diagnostic_empty_row` là **hàm lồng thụt 4 dấu cách**, nên khối chèn vào
   giữa dòng. Khôi phục ngay từ backup; md5 sau khôi phục **khớp VPS từng byte**, xác nhận không
   để lại dấu vết.

2. **Hai lỗi trong `FU-425` do chính bài thử bắt** — §5.2. Nếu chỉ chạy xuôi thì đã giao một cái
   cờ **không bao giờ đỏ** mà trông như đang canh.

3. **Con số `26,5%` trong lệnh owner không đúng cho khối này** — §3.3. Nói ra thay vì im lặng
   dùng con số dễ nghe hơn.

4. **Bộ chấm lane T-B tự in phép so sai thước** — §3.2. Nếu đọc theo dòng nó in thì hôm nay đã
   công bố một phán quyết trên **46 mẫu trong khi ngưỡng cần 96**.

---

## 8. Gỡ về

| việc | lệnh |
|---|---|
| cả ba tệp | `backups/{main,scheduler,gpt_analyzer}.py.pre_v11106` (có **cả trên VPS**) → chép lại + `systemctl restart lottery` |
| theo commit | `git revert <sha>` — ba commit riêng, **gỡ độc lập được** |
| bảng mới | `wr_fallback_rong_v11106` — chỉ ghi khi đường lùi kích hoạt; xoá bảng là đủ |

---

## 9. Theo dõi tiếp

| mã | việc | hạn |
|---|---|---|
| — | **24/08 sáng**: lượt 05:00 phải đóng dấu `CTX-18.6`; MB phải **không còn** khối ranking ⇒ mới được ghi `RUNTIME_PROVEN` | **24/08** |
| **`FU-427`** · `SC2508-2` | bộ chấm T-B in `b+c` kèm nhãn đúng, **không** đặt con số «hai dự đoán khác nhau» cạnh ngưỡng | 25/08 |
| **`FU-428`** *(chờ owner)* | mệnh lệnh mồ côi `:736` trỏ vào `BT MODEL RANKING` đã bị de-herding cắt | chờ ký |
| — | lane T-B: cần thêm **50 cặp lệch kết cục** nữa (46/96) và **1 ngày** (13/14) | ~27/08 |
| — | **MB regime mới** đếm từ 24/08 — cấm trộn dữ liệu MB trước mốc | — |
| — | 27/08 quyết **DỪNG** cho `gpt-5.5` và `qwen3-max-thinking` | 27/08 |

---

## §62 (A60) — BA LỚP NGUỒN

### `OWNER_SAID`

| nội dung | nguyên văn |
|---|---|
| đánh giá | *«Trình bày ngắn gọn, minh bạch, có số liệu, KHÔNG tô hồng»* |
| `FU-421` | *«thêm `key=lambda x:(-x[1], x[0])` CÙNG LÚC + làm đường lùi `model_rates={}` KÊU LÊN. Đo lại phải ra 0 thay đổi trên dữ liệu thật»* |
| lane T-B | *«CẤM tự ý đổi ngưỡng sau khi thấy số. CẤM kết luận ngoài ngưỡng»* |
| khối MB | *«(1) Model MẤT gì… (2) Model ĐƯỢC gì… LUẬT BIÊN REGIME: Mọi quyết định THĂNG cho model MB sẽ đếm lại từ mốc hôm nay»* |

### `CODE_DID`

| việc | bằng chứng |
|---|---|
| kết quả 23/08 | nền MN 41% · MT 42% · MB 24%; kỳ vọng 1,07, thực tế 1; 15/15 model cả ba miền |
| `FU-419` deploy | PID `2128063→2293117`; `CTX-18.5`; D-1 = `77 distinct tails` |
| `FU-421` | 3 chỗ (đếm trước khi thay); top-2 **0/114** đổi; top-3 11/114 |
| `FU-425` | `_model_call_start = _pre["start_time"]`; cờ `LECH_DONG_HO`; thử chặn 6/6 |
| `FU-426` | `reasoning_json` + `raw_response[:2000]` cho lượt rỗng; thử chặn 6/6 |
| khối MB gỡ | MB 15.372→**13.832** kt (`045aa3e2`→`1433a381`); MN/MT **byte-identical**; khối 1→0 |
| lane T-B | `181 | 122 | 46 | b=21 | c=25 | 13 ngày` — tự kiểm chứng |
| deploy | md5 khớp cả 3 tệp · `py_compile` trước restart · PID đổi · 4 bảng khoá **PRE=POST** |

### `DOC_SAID` — chỗ tài liệu **lệch** với mã

| lệch | chi tiết |
|---|---|
| lệnh owner ≠ số đo | *«khối MB chiếm 26,5% prompt MB»* — thật là **8,83–10,76%** gói ngữ cảnh MB |
| bộ chấm T-B ≠ ngưỡng nó in | in `122` cạnh `≥96` trong khi ngưỡng dành cho `b+c` = **46** |
| prompt `:736` ≠ prompt thật | trỏ vào `BT MODEL RANKING` mà de-herding **đã cắt** |
| `docs/FOLLOW_UP_TRACKER.md` ≠ sổ quyết định | vẫn ghi `FU-216` hạn 09/08, `FU-231`/`FU-226` hạn 10/08 — chưa theo `QD-045` |

---

**TanPhatAI cần làm:** cập nhật `docs/FOLLOW_UP_TRACKER.md` — `FU-419` nay **`DEPLOYED`**, `FU-421`/`FU-425`/`FU-426` **đã vá + deploy** (thử chặn 6/6 mỗi cái), **`FU-427` mới** (bộ chấm T-B in phép so sai thước, hạn 25/08), và **`FU-428` chờ owner ký** (mệnh lệnh mồ côi `:736`); ghi vào sổ quyết định **LUẬT BIÊN REGIME: mọi quyết định THĂNG cho model MB đếm lại từ 24/08/2026** vì gói ngữ cảnh MB đã đổi (−10,0%); theo dõi ba việc: ① **sáng 24/08** kiểm lượt 05:00 có đóng dấu `CTX-18.6` và MB có còn khối ranking không — **chưa kiểm thì cấm ghi `RUNTIME_PROVEN`**, ② **lane T-B CHƯA ĐƯỢC ĐỌC**: còn thiếu **50 cặp lệch kết cục** (46/96) và **1 ngày** (13/14), **cấm đọc theo con số 122 mà bộ chấm in ra**, ③ MB là miền yếu nhất hôm nay (**2/15** model có số đầu trúng, bằng nửa nền) — đó là **khâu sinh số**, không phải khâu chọn, nên đừng tìm cách sửa bộ chọn.
