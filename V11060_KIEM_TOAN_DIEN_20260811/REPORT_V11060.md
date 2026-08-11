# REPORT V11060 — KIỂM TOÀN DIỆN ĐẦU NGÀY: BÁO CÁO CÓ MỘT LỖ TREO 2 NGÀY · ĐÓNG FU-360

**Ngày:** 2026-08-11 sáng · **Quyết định owner:** `QD-060` · **Mã đọc:** `KT1108`
**Production KHÔNG đổi** — hash 4 bảng khoá PRE = POST y hệt · PID `1353489` · health 200

---

## 1. Tóm tắt

Owner hỏi: *«Đầu ngày rồi em, em tiến hành kiểm tra toàn diện dùm anh, hôm qua giờ em đã cập nhật
báo cáo đầy đủ chưa em?»*

**Trả lời trung thực: GẦN đầy đủ — và chính câu hỏi đã lộ ra một lỗ thật.**

| # | lỗ | mức |
|---|---|---|
| **1** | Đính chính **do owner ký** treo **2 ngày** trên GitHub công khai — cổng báo cáo **không thể thấy** | **CAO** |
| **2** | Lane A/B dùng **nhầm khoá** Gemini ⇒ một cặp **mất tính một-biến**; và agent đã **phân loại sai** nguyên nhân 429 | **CAO** |
| **3** | Lane **không parse** được kết quả — 3/5 model gọi API **thành công** vẫn báo lỗi | **CAO** |
| **4** | Timeout bóp theo **miền hẹp nhất** ⇒ `deepseek-reasoner` timeout ở MN dù MN có cửa sổ 10 tiếng | TRUNG |

**FU-360 đã ĐÓNG** ở tầng `DEPLOYED_LIVE_VERIFIED` — **không** nâng lên `RUNTIME_PROVEN`.

Phương pháp: **8 tác nhân** (4 kiểm + 4 phản biện đối kháng). Phản biện **bác được thật** — trong
đó lật ngược chính chẩn đoán của agent về nguyên nhân 429.

---

## 2. Owner yêu cầu gì (nguyên văn)

> *«Đầu ngày rồi em em tiến hành kiểm tra toàn diện dùm anh hôm qua giờ em đã cập nhật báo cáo
> đầy đủ chưa em?»* — 11/08

---

## 3. Đào bới / phát hiện

### 3.1 · LỖ 1 — đính chính do OWNER KÝ treo 2 ngày, và cổng mù trước nó

Ba tệp `REPORT_V11050` · `REPORT_V11051` · `REPORT_V11052` mang **đính chính ngưỡng
`FU-284 = 9,53`** — owner ký **18:37 ngày 09/08**, huỷ con số `12,00` do TanPhatAI ghi nhầm.

| | |
|---|---|
| sửa lúc | **09/08 19:12:33** |
| commit | **CHƯA BAO GIỜ** |
| trôi qua | **2 ngày · 5 commit** (V11054 → V11059) |
| hậu quả | GitHub công khai vẫn hiển thị *«9,53 vs 12,00 — chốt trước 20/08»* trong khi owner **đã chốt** |

**Và cổng báo cáo KHÔNG THỂ thấy.** Nó chỉ hỏi tệp có nằm trong `git ls-files` không — mà cả ba
**đều nằm trong đó**. Nó in ra *«file chưa commit: 7»* rồi vẫn kết luận *«MỌI PHIÊN BẢN ĐỀU CÓ
BÁO CÁO ĐẦY ĐỦ VÀ ĐÃ PUSH»* và **thoát 0**.

> **«Có trong git» KHÔNG bằng «bản trong git là bản mới nhất».** Đúng họ `RM-02`: hash bằng nhau
> chỉ chứng minh *không ghi bậy*, không chứng minh *dữ liệu đúng thời điểm*.

### 3.2 · LỖ 2 — lane dùng nhầm khoá, và agent phân loại sai nguyên nhân

Đường official giải khoá **DB TRƯỚC, env SAU** (`main.py:8468-8521`):

```python
required_key = get_api_key('gemini_api_key')    or GEMINI_API_KEY
required_key = get_api_key('anthropic_api_key') or ANTHROPIC_API_KEY
```

Lane chỉ đọc hằng số cấp module. Đo ngày 11/08:

| nhà cung cấp | env | DB | |
|---|---|---|---|
| ANTHROPIC | `0735dcf3` | `0735dcf3` | trùng — không lộ |
| DEEPSEEK | `2fb83d77` | `2fb83d77` | trùng — không lộ |
| **GEMINI** | **`08614b1c`** | **`da3deef6`** | **LỆCH** |

**Hai hậu quả, và cái thứ hai nặng hơn:**

| | agent nói hôm qua | sự thật |
|---|---|---|
| `gemini-2.5-pro` 429 «limit: 0» | *«HẠN MỨC THẬT của nhà cung cấp, không phải lỗi mã»* | **lỗi CẤU HÌNH của lane** — sửa khoá xong model chạy được ngay |
| `gemini-2.5-flash` | cặp hợp lệ | gọi bằng **DỰ ÁN KHÁC CONTROL** ⇒ khác nhau **cả prompt lẫn khoá** ⇒ **mất tính một-biến** ⇒ **ĐÃ HUỶ** |

**Và cổng của chính agent đã nói dối.** `--soi-dinh-tuyen` bản đầu chỉ hỏi *«có khoá không»* và
trả lời **«CÓ»** — cho một khoá **SAI**.

> **Cổng xác nhận SỰ TỒN TẠI mà không xác nhận ĐÚNG NGUỒN thì không phải cổng.**

Nay nó **so băm khoá lane vs official**: **5/5 KHỚP**.

### 3.3 · LỖ 3 — lane không parse được, 3/5 model gọi API THÀNH CÔNG vẫn báo lỗi

`_call_*` trả về `{"content": "<chuỗi JSON thô>", "tokens_used": …}` — **không phải** dict đã
parse. Lane đọc thẳng `api["prediction"]["numbers"]` — **thứ chưa bao giờ tồn tại**.

Đường official làm **hai bước**:

```python
result_text = api_response["content"]
result      = _parse_ai_json_payload(result_text)   # gpt_analyzer.py:1151
nums        = result["prediction"]["numbers"]
```

Nay dùng **đúng hàm đó**, không tự viết bản parse thứ hai (RM-10).

### 3.4 · LỖ 4 — timeout bóp theo miền hẹp nhất

Đặt 120s cho cả ba miền vì cửa sổ MT/MB hẹp (~35 phút). Nhưng **MN có cửa sổ 10 tiếng**
(official 05:15 → kết quả 16:35 giờ VN), và `deepseek-reasoner` trễ thật **190–197s**.

Nay `TIMEOUT_THEO_MIEN = {MN: 300, MT: 120, MB: 120}`.

### 3.5 · PHÁT HIỆN KÈM — tái cấu trúc ĐÃ ĐỔI HÀNH VI MODEL

**4/4 model chuyển sang dạng `§25`** (`prediction.main_number` + `secondary_number`) thay vì
`OUTPUT FORMAT` (`prediction.numbers`).

Nguyên nhân là thứ tự khối:

| | thứ tự user message |
|---|---|
| CONTROL | thân *(YÊU CẦU cuối thân)* → pack → **rulebook (kết bằng §25/§26)** |
| T-B | pack → rulebook §1–21 → **§22–§26 → YÊU CẦU** |

T-B đẩy `§22–§26` xuống T3 nên `§25` nằm **sát cuối** ⇒ model tuân nó **chặt hơn** và bỏ luôn
khoá `numbers`.

**Xử lý: chấp nhận CẢ HAI dạng, KHÔNG bẻ lại thứ tự prompt** — bẻ là thêm một biến nữa vào phép
so vốn đang cố giữ **một biến**. Và dạng `§25` vẫn là **hợp đồng chính thức** của prompt, không
phải model bịa ra.

---

## 4. Hướng xử lý và vì sao

### 4.1 · Đóng FU-360 — và vì sao KHÔNG nâng tầng

| điều kiện owner ký (Q3 · 09/08 13:58) | kết quả |
|---|---|
| canh 24h | **10:06 10/08 → 10:06 11/08 · 0 dòng · 0 chặn NHẦM** |
| thử chặn thật | **5/5 ĐẠT** + **đối chứng bản chưa vá LỌT** ⇒ cổng phân biệt được hai bản |
| bản vá còn sống | `grep -c "CHAN CHEO LANE" database.py` = **1** trên production |
| cả ba miền dưới cổng | **11/08 05:00 giờ VN**: MN 27 dòng · MT 7 · MB 7 |

Cảnh báo hôm 10/08 (*«MN chạy trước restart nên chỉ MT/MB dưới cổng»*) **đã được giải quyết** —
hôm nay cả ba miền đều chạy sau khi cổng bật.

⇒ **`DEPLOYED_LIVE_VERIFIED`**.

**KHÔNG nâng lên `RUNTIME_PROVEN`** vì cổng **chưa từng chặn thật lần nào**. Ngày nổ ghi sẵn
trong FU-360 là **21/08**, khi `QD-015/016/017` chạy và một model chạy **cả hai đường**.

> **«0 dòng» là ĐÚNG DỰ KIẾN, không phải bằng chứng cổng sống** (RM-20). Bằng chứng cổng sống là
> **bài thử + đối chứng**, không phải số dòng journal. `RM-12` cấm tự nâng cấp tầng.

### 4.2 · Vì sao vá cổng thay vì chỉ push 3 tệp

Push 3 tệp là xử **triệu chứng**. Lỗ thật là cổng **không thể phát hiện** loại vi phạm này — nếu
chỉ push mà không vá, lần sau lặp lại y hệt và vẫn không ai thấy.

Vá xong **thử chặn (RM-15)**: sửa một REPORT rồi không commit ⇒ cổng **ĐỎ**; khôi phục ⇒ **XANH**;
tệp về **nguyên trạng**.

---

## 5. Đã làm gì

| # | việc | bằng chứng |
|---|---|---|
| 1 | Push 3 tệp đính chính `FU-284 = 9,53` | commit **`a778047`** trên repo công khai |
| 2 | Vá cổng báo cáo — bắt tệp **đã theo dõi mà bị SỬA** | thử chặn ĐẠT (đỏ ⇄ xanh, tệp nguyên trạng) |
| 3 | Vá lane: khoá **DB trước env sau** như official | `--soi-dinh-tuyen` **5/5 KHỚP băm** |
| 4 | Vá lane: parse bằng **chính** `_parse_ai_json_payload` | 5/5 model ra số |
| 5 | Vá lane: `TIMEOUT_THEO_MIEN` | `deepseek-reasoner` MN không còn timeout |
| 6 | **HUỶ** cặp `gemini-2.5-flash` nhiễm + chạy lại bằng khoá đúng | bảng còn 3 → nay **5 cặp sạch** |
| 7 | Bật lại `gemini-2.5-pro` | chạy được ngay ⇒ xác nhận 429 là lỗi cấu hình |
| 8 | **ĐÓNG FU-360** ở tầng `DEPLOYED_LIVE_VERIFIED` | commit `717a3da` |

**Hash 4 bảng khoá PRE = POST y hệt** ở mọi lượt chạy lane.

---

## 6. Cổng kiểm — xác minh

| cổng | kết quả |
|---|---|
| `_v10921_report_gate.py V11054…V11059` | **6/6 đủ 9 phần, đã commit** · V11056–V11059 đủ §62 ba lớp |
| cổng báo cáo **thử chặn** | sửa REPORT chưa commit ⇒ **✗ ĐỎ**; khôi phục ⇒ **✓** |
| `--soi-dinh-tuyen` | **5/5 KHỚP** băm khoá lane vs official |
| `_v11052_thu_chan_cheo_lane.py --doi-chung` | **5/5 ĐẠT** + đối chứng **LỌT** |
| `_v11055_canh_chan_cheo_lane.py` | **0 dòng · 0 chặn NHẦM** (đủ 24h) |
| `_v10925_rule_sync_check.py` | **SÁU MẶT ĐỒNG BỘ** |
| `_v10920_decision_ledger.py` | còn **1 phép trôi** — `FU-283` hạn **13/08**, việc thật đang treo |

---

## 6bis. §62 (A60) — NGUỒN BA LỚP

### `OWNER_SAID`

| giờ | nguyên văn |
|---|---|
| **11/08** | *«Đầu ngày rồi em em tiến hành kiểm tra toàn diện dùm anh hôm qua giờ em đã cập nhật báo cáo đầy đủ chưa em?»* |
| **09/08 18:37** | ngưỡng `FU-284` = **9,53** — con số `12,00` là lỗi TanPhatAI, **đã huỷ** |
| **09/08 13:58** | *«canh 24h · sáng 11/08 mới đóng · rollback ngay nếu thử chặn không đạt»* |

### `CODE_DID`

| mã làm gì | evidence |
|---|---|
| cổng báo cáo in *«file chưa commit: 7»* rồi vẫn **thoát 0** | `_v10921_report_gate.py:124` in số, `:206` thoát không dùng số đó |
| official giải khoá **DB trước env sau** | `main.py:8468` · `:8471` · `:8518` · `:8521` |
| khoá Gemini **lệch** giữa env và DB | env `08614b1c` vs DB `da3deef6` (chỉ in băm, không in giá trị) |
| `_call_*` trả `{"content": …}` **không phải dict đã parse** | `gpt_analyzer.py:3480-3488` |
| cả ba miền chạy official **05:00 giờ VN** ngày 11/08 | `predictions` — MN 27 dòng · MT 7 · MB 7 |
| bản vá chéo lane **còn sống** | `grep -c "CHAN CHEO LANE" database.py` = 1 |

### `DOC_SAID`

| tài liệu ghi gì | file:mục | lệch? |
|---|---|---|
| `REPORT_V11050/51/52` (bản trên GitHub tới sáng nay) | *«9,53 vs 12,00 — chốt trước 20/08»* | ✗ **CŨ 2 ngày** — owner đã chốt 09/08 |
| `REPORT_V11059` | *«gemini-2.5-pro 429 là hạn mức thật của nhà cung cấp»* | ✗ **SAI** — lỗi cấu hình của lane |
| `RM-02` | *«hash bằng nhau chỉ chứng minh không ghi bậy»* | **khớp** — và cổng báo cáo sập đúng họ lỗi này |
| `RM-12` | *«cấm tự nâng cấp tầng»* | **khớp** — FU-360 đóng ở `DEPLOYED_LIVE_VERIFIED` |

### Ba lớp lệch nhau ⇒ FINDING

1. **`OWNER_SAID` ≠ `DOC_SAID` công khai** — owner ký `9,53` từ 09/08, bản công khai vẫn ghi
   *«chưa chốt»* suốt 2 ngày. **Đây là lệch nghiêm trọng nhất** vì nó là thứ owner đọc.
2. **`DOC_SAID` của chính agent ≠ `CODE_DID`** — `REPORT_V11059` ghi 429 là hạn mức nhà cung cấp;
   thực tế là lane dùng nhầm khoá. Đã đính chính trong báo cáo này.
3. **`CODE_DID` tự mâu thuẫn** — cổng báo cáo **tính** được số tệp chưa commit nhưng **không dùng**
   nó khi kết luận.

---

## 7. Vướng vấp

| # | vấp | quy tắc |
|---|---|---|
| 1 | Cổng báo cáo **in ra bằng chứng vi phạm rồi bỏ qua chính nó** | **RM-02** |
| 2 | `--soi-dinh-tuyen` trả lời **«CÓ khoá»** cho một khoá **SAI** — xác nhận tồn tại, không xác nhận đúng nguồn | **RM-15** |
| 3 | Phân loại **sai** nguyên nhân 429: gọi là *«hạn mức nhà cung cấp»* trong khi là **lỗi cấu hình của mình** | **RM-13** |
| 4 | Giả định `_call_*` trả dict đã parse — **chưa bao giờ đúng** | **RM-10** |
| 5 | Bóp timeout cả ba miền theo miền hẹp nhất ⇒ tự bỏ mất MN | — |
| 6 | Ba phép thay nhiều dòng **trượt** vì dấu nối dòng — phải kiểm lại từng nhánh mới phát hiện | bẫy CRLF/format, lần thứ **chín** |

**Vấp 3 là nặng nhất về mặt phương pháp:** agent đọc log 429, thấy chữ *«free_tier limit: 0»*, và
**dừng ở đó** — không hỏi *«official gọi cùng model đó lúc 05:17 thành công, vậy nó dùng khoá
nào?»*. Đúng lỗ `§60.2`: **«ai còn trỏ tới thứ này?»** — phải soi cả **người gọi**, không chỉ
thư viện được gọi.

---

## 8. Gỡ về

```bash
git revert <sha V11060>          # kho riêng — chỉ vá cổng + vá lane shadow
git revert a778047               # kho công khai — nếu muốn bỏ đính chính (KHÔNG nên)
```

FU-360 nếu cần gỡ:
```bash
cp backups/database.py.pre_v11052 web/backend/database.py && systemctl restart lottery
```

Phiên này **không đổi hành vi production** — hash 4 bảng khoá PRE = POST y hệt.

---

## 9. Theo dõi tiếp

| mã | việc | ngưỡng hành động | mốc |
|---|---|---|---|
| ~~**FU-360**~~ | ~~chặn chéo lane~~ | **ĐÓNG 11/08** — `DEPLOYED_LIVE_VERIFIED` | ✅ |
| **FU-283** · `DO1308` | **đang trôi** — đổ `latency_seconds` từ trace vào bảng + panel §52 | model TB > 180s ⇒ xét cắt ở FU-290 | **13/08** |
| **FU-398** · `PB1108` | lane A/B ba tầng — **5 cặp sạch** đầu tiên hôm nay | `≥96 cặp bất đồng` **VÀ** `\|z\| ≥ 1,96` · **cấm đọc sớm** | ~**27/08** |
| **FU-397** · `AT1008` | B1 anti-trap | `n(FULL_SPENT) ≥ 90` · đang **51/90** | ~giữa 12/2026 |
| **FU-397b** · `CG2108` | nhánh CHỐT GẤP `+0,40` | chạm đường sinh số ⇒ **PLAN** | **21/08** |
| **FU-395** · `HT2108` | gói 21/08 từ C1–C6 | owner ký từng mục | **21/08** |
| FU-284 | cửa sổ đang chạy | **9,53** điểm *(đã chốt)* · z ≥ 1,96 · n ≥ 150 | **20/08** — cấm đọc sớm |

**Chưa dùng mã FU mới nào trong phiên này.**

---

TanPhatAI cần làm: ① ghi `QD-060` và **đóng `FU-360`** ở tầng `DEPLOYED_LIVE_VERIFIED` — **không**
ghi thành `RUNTIME_PROVEN`; ② **đính chính `REPORT_V11059`**: câu *«gemini-2.5-pro 429 là hạn mức
thật của nhà cung cấp»* là **SAI**, thực tế là lane dùng nhầm khoá env thay vì khoá DB; ③ ghi nhận
**cặp `gemini-2.5-flash` ngày 11/08 đã bị HUỶ và chạy lại** — đừng đếm cặp cũ; ④ **`FU-283` hạn
13/08 đang trôi** (đổ `latency_seconds` vào bảng + panel) — cần xếp lịch; ⑤ ghi vào sổ bài học
*«cổng xác nhận SỰ TỒN TẠI mà không xác nhận ĐÚNG NGUỒN thì không phải cổng»* — đã xảy ra thật
với `--soi-dinh-tuyen`.
