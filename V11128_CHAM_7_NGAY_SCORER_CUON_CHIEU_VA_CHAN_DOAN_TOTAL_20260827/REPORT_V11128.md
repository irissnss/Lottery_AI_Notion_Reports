# REPORT V11128 — CHẤM ĐỦ 21–27/08 · SCORER CUỐN CHIẾU ĐÃ DEPLOY · CHẨN ĐOÁN GỐC TOTAL/RANKING

```
REPORT_VERSION        : V11128
REPORT_TITLE          : Chấm 7 ngày từ production DB · deploy scorer cuốn chiếu ·
                        phép đo quyết định về TOTAL/ranking · verdict roster model
WORK_DATE_ICT         : 2026-08-27
PUBLISHED_AT_ICT      : xem mục bàn giao
TIMEZONE              : Asia/Ho_Chi_Minh / UTC+07:00
OWNER_DECISION        : D-25 WINDOWED_AUTODEPLOY · prompt 41
AUTHORIZED_SCOPE      : DB_READ · RUNTIME_AUDIT · CLASS_A_DEPLOY · REPORT_ONLY_PUSH
ACTOR_RUNTIME         : CLAUDE_CODE
PREVIOUS_PUBLIC_HEAD  : 57bb564b79406da72c1875cb137b9d225e3bdd16
LABELS                : DAILY_OBSERVATION_ONLY · INSUFFICIENT_POWER · CLASS_A_DEPLOYED ·
                        RUNTIME_LOADED · OWNER_DECISION_PENDING
```

---

## 1 · TÓM TẮT BẰNG LỜI THƯỜNG

**Phát hiện lớn nhất của phiên này là một phép đo đơn giản mà trước nay chưa ai làm:**
*FINAL có chọn tốt hơn **bốc ngẫu nhiên từ chính pool ứng viên của nó** không?*

Câu trả lời, trên **273 lượt ngày–miền** trong 90 ngày, với đối chứng âm/dương đều đạt:

| cách chọn | tỉ lệ trúng |
|---|---|
| **FINAL — M0 hiện hành** | **30,77 %** |
| **bốc ngẫu nhiên từ chính pool** | **33,72 %** |
| equal vote | 33,70 % |
| bốc ngẫu nhiên một model | 32,63 % |
| vote vị trí đầu | 31,50 % |
| **nền toàn cục** | **33,87 %** |

⇒ **Tầng xếp hạng không thêm gì cả** — nó còn **thấp hơn 2,95 điểm** so với bốc bừa từ chính
danh sách nó đang xếp *(z = −1,03, tức chênh này chưa có ý nghĩa thống kê — nhưng chắc chắn
**không** có lợi thế nào)*.

**Và sâu hơn nữa:** pool chứa đáp án **99,6 %** lượt, nghe rất ấn tượng — nhưng pool trung bình
**13,5 số** và mỗi ngày có ~33,9/100 số về, nên `1 − (1−0,339)^13,5 ≈ 99,6 %`. **Con số coverage
đó được giải thích TRỌN VẸN bằng tình cờ.** Bốc ngẫu nhiên từ pool ra **33,72 %**, đúng bằng nền
toàn cục **33,87 %** — tức **bản thân pool cũng không giàu hơn ngẫu nhiên**.

**Nói gọn: không phải ranking hỏng còn generation tốt. Cả hai tầng đều chưa vượt ngẫu nhiên.**

Việc thứ hai đã làm xong: **scorer cuốn chiếu đã deploy**. Và hoá ra chẩn đoán ban đầu chưa đúng
chỗ — settlement **đã** chạy cuốn chiếu từng miền rồi; chỉ có bước đồng bộ bảng chấm bị dồn vào
20:20. Nên bản vá là **thêm ba mốc lịch, không sửa một dòng logic nào**.

---

## 2 · NGUỒN VÀ RUNTIME

| | |
|---|---|
| production DB | `<đã che>/data/lottery_ai.db` · mtime **27/08 19:08** |
| `predictions` | **13.573** · mới nhất **27/08 17:48:58** |
| `final_bundles` | **543** · mới nhất **27/08 17:36:00** |
| `lottery_results` | **15.364** · mới nhất **27/08 18:31:33** |
| MainPID | **2671007** |
| `main.py` runtime | `ec2540331be1…` — **khớp bản V11127** ⇒ `FU-438` **không regression** |
| `scheduler.py` runtime | `a6c8bfff60b6…` — **bản mới deploy phiên này** |

Mọi truy vấn `sqlite3 -readonly` + chặn từ khoá ghi phía client. **Không ghi một dòng nào vào DB.**

---

## 3 · GĐ-1 · SCORECARD 21–27/08

### 3.1 · Sản phẩm chính thức

| cửa sổ | BT | Xiên 2 | Xiên 3 | 3-càng |
|---|---|---|---|---|
| **7 ngày (21–27/08)** | **6/21 = 28,6 %** | **1/21 = 4,8 %** | **0/20 = 0 %** | **`NOT_SCORABLE`** |

🔴 **3-càng = `NOT_SCORABLE`** — tra schema `final_bundles` (26 cột) và toàn bộ 253 bảng:
**không có cột nào, không có bảng nào** chứa sản phẩm 3-càng. Không có writer ⇒ không có gì để
chấm. **Không lấp bằng nguồn khác.**

### 3.2 · Từng ngày × miền

| ngày | MB | MN | MT |
|---|---|---|---|
| 21/08 | `22` LOSE | `74` LOSE | `69` LOSE |
| 22/08 | `28` LOSE | `10` 🟢 **WIN** | `41` LOSE |
| 23/08 | `54` LOSE | `73` LOSE | `15` 🟢 **WIN** |
| 24/08 | `59` LOSE | `45` LOSE | `82` LOSE |
| 25/08 | `94` 🟢 **WIN** | `84` 🟢 **WIN** | `65` LOSE |
| 26/08 | `29` LOSE | `33` LOSE | `62` LOSE |
| 27/08 | `61` 🟢 **WIN** | `61` LOSE | `68` 🟢 **WIN** |

### 3.3 · Phân loại sự cố — và vì sao nhãn đầu tiên của tôi **sai**

| phân loại | số lượt |
|---|---|
| `GENERATION_MISS` | **0** |
| `RANKING_MISS` | 14 |
| `RANKING_MISS` (không model nào xếp đầu) | 1 |
| `FINAL_WIN` | 6 |

> ⚠️ **Tôi phải tự bác nhãn này ngay khi vừa dựng nó.** *«Có model nào top-1 đúng không»* là câu
> hỏi **SAI**: với nền ~33 % và 16 model, xác suất *«có ít nhất một model top-1 đúng»* là
> **≈ 99,8 % kể cả khi ranking hoàn hảo**. Nên `RANKING_MISS = 14/21` **không** chứng minh
> ranking hỏng — nó gần như chắc chắn xảy ra dù thế nào.
>
> Câu hỏi **đúng** là mục 4.

---

## 4 · GĐ-3 · PHÉP ĐO QUYẾT ĐỊNH

### 4.1 · Thiết kế

**Câu hỏi:** FINAL có tốt hơn **bốc ngẫu nhiên từ chính pool của nó** không?
**Mẫu:** 273 lượt ngày–miền có đủ FINAL + kết quả + pool, 90 ngày.
**Lọc:** bỏ shadow/replay · bỏ dòng tạo sau giờ FINAL từng miền.

### 4.2 · Đối chứng — bắt buộc trước khi đọc kết quả

| đối chứng | kỳ vọng | đo được |
|---|---|---|
| cố tình chọn số **KHÔNG** về | ~0 % | 🟢 **0,0 %** (0/273) |
| cố tình chọn số **ĐÃ** về | 100 % | 🟢 **100,0 %** (273/273) |

⇒ **phép đo phân biệt được.** Không phải một thước mù.

### 4.3 · Kết quả

```
FINAL (M0)                30,77 %
bốc ngẫu nhiên từ pool    33,72 %      chênh −2,95 điểm · z = −1,03
equal vote                33,70 %
bốc ngẫu nhiên 1 model    32,63 %
vote vị trí đầu           31,50 %
nền toàn cục              33,87 %
```

| | |
|---|---|
| pool chứa đáp án | **272/273 = 99,6 %** |
| kích thước pool trung bình | **13,5 số** |
| coverage kỳ vọng nếu pool **hoàn toàn ngẫu nhiên** | `1 − (1−0,339)^13,5 = ` **99,6 %** |

### 4.4 · Đọc kết quả cho đúng

1. **Ranking không có lợi thế.** FINAL thấp hơn bốc bừa từ chính pool 2,95 điểm. Chênh này
   `z = −1,03` nên **chưa có ý nghĩa thống kê** — nhưng chắc chắn **không có bằng chứng nào**
   cho thấy tầng xếp hạng đang thêm giá trị.
2. **Coverage 99,6 % không phải thành tích.** Nó khớp **chính xác** con số kỳ vọng của một pool
   ngẫu nhiên cùng kích thước.
3. **Pool cũng không giàu hơn nền.** 33,72 % vs 33,87 % — hai con số như một.

⇒ **Kết luận:** vấn đề **không** nằm ở chỗ *«ML sinh đúng nhưng TOTAL xếp sai»*. Đo được thì
**cả hai tầng đều đang ở mức ngẫu nhiên**.

### 4.5 · Hệ quả cho TOTAL-N1/N2/N3

Ba challenger được yêu cầu (chuẩn hoá · shrinkage · dedupe family) đều là **cách xếp lại một
danh sách**. Nhưng đo được rằng **danh sách đó không mang tín hiệu nào để xếp** — bốc bừa từ nó
cho kết quả **bằng nền**.

**Do đó tôi ĐĂNG KÝ TRƯỚC (chưa đọc kết quả) rằng kỳ vọng tiên nghiệm cho N1/N2/N3 là THẤP**, và
đề nghị **đổi thứ tự ưu tiên**: trước khi tinh chỉnh cách xếp, phải trả lời được câu
*«có tín hiệu nào để xếp không?»*. Xây ba bộ xếp hạng cho một pool ngẫu nhiên là **tối ưu hoá
nhiễu** — và nếu một trong ba tình cờ trội lên, đó gần như chắc chắn là may rủi chứ không phải
tiến bộ. **Đây chính là chỗ `multiple-comparison correction` tồn tại để chặn.**

⛔ **Chưa promote gì. M0 giữ official.**

---

## 5 · GĐ-2 · SCORER CUỐN CHIẾU — ĐÃ DEPLOY

### 5.1 · Chẩn đoán — và nó khác giả định ban đầu

Đo lúc **19:1x ngày 27/08**:

| | |
|---|---|
| settlement | 🟢 **ĐÃ cuốn chiếu từng miền rồi** — MN `verified_at 16:37:42`, MT `17:30:01`, MB `18:31:33` — **cùng giây** kết quả về |
| `predictions` đã settle | **81 dòng** sẵn sàng chấm |
| `model_daily_eval` 27/08 | 🔴 **0 dòng** — vì job đồng bộ chỉ chạy **20:20** |

⇒ Khuyết tật **chỉ là độ trễ ở bước đồng bộ**, không phải settlement.

### 5.2 · Bản vá — **+23 dòng, không đổi một dòng logic nào**

Hàm chấm **đã** có sẵn hai tính chất cần thiết:

| tính chất | bằng chứng |
|---|---|
| **tự guard** | chỉ đọc `predictions` có `status IN ('WIN','PARTIAL','LOSE')` ⇒ miền chưa có kết quả **không** bị chấm sớm |
| **idempotent** | `INSERT OR REPLACE` trên `UNIQUE(date, region, ai_model)` ⇒ chạy lại **không** tạo điểm thứ hai |

Nên bản vá **chỉ thêm ba mốc lịch**: `16:50` (sau MN) · `17:45` (sau MT) · `18:45` (sau MB),
giữ nguyên `20:20` làm **lượt đối soát cuối ngày**.

### 5.3 · Deploy và bằng chứng

| bậc | bằng chứng |
|---|---|
| gate | CLASS A · **19:15, ngoài block** · backup hash **khớp gốc** · `py_compile` OK cả local lẫn VPS |
| `FILES_COPIED_NOT_LOADED` | sha256 trên VPS `a6c8bfff60b6…` **khớp** tệp gửi |
| `RUNTIME_LOADED` | PID **2646084 → 2671007** · hash runtime **khớp** |
| **đăng ký job** | 🟢 **APScheduler ghi rõ 3 dòng**: `Added job "Per-Model Eval cuốn chiếu sau MN (16:50)"` · `MT (17:45)` · `MB (18:45)` |
| không regression | `/api/health` **200** · `FU-438`: cả ba endpoint kiểm vẫn **401** |
| không drift | `predictions` · `final_bundles` · FINAL 27/08 — **không đổi** |
| trùng điểm | **0** |

### 5.4 · 🔴 Trạng thái đúng là `RUNTIME_LOADED`, **chưa** phải `RUNTIME_PROVEN`

Script deploy của tôi **in nhầm `RUNTIME_PROVEN`** — bộ đếm lỗi không tính hai phép quan trọng.
Sự thật:

- ✅ tệp đã nạp, hash khớp, **3 job đã đăng ký** — chứng minh được
- ❌ **ba mốc chưa nổ lần nào**: 16:50/17:45/18:45 **đã trôi qua** trước khi deploy (19:15)
- ❌ `model_daily_eval` 27/08 vẫn **0** — lượt `20:20` hôm nay sẽ là lượt chấm đầu tiên

⇒ **Bằng chứng hành vi cuốn chiếu sẽ có vào 16:50 ngày mai (28/08).** Không được ghi
`RUNTIME_PROVEN` trước lúc đó.

---

## 6 · GĐ-4 · VERDICT ROSTER

Roster **sống** lấy từ production DB, **không** dùng số tồn kho trong tài liệu.

| verdict | số model |
|---|---|
| **`KEEP_OFFICIAL`** | **16** |
| **`SHADOW_MEASURE`** | **14** |
| `PAUSE_FROM_OUTPUT` | 0 |
| `RETIRE_PENDING_GATE` | **0** |

**Nền 30 ngày = 33,6 %.**
🔴 **Model có KTC 95 % nằm TRÊN nền: KHÔNG CÓ.**
🔴 **Model có KTC 95 % nằm DƯỚI nền: KHÔNG CÓ.**

⇒ **Không ai đủ điều kiện promote, và cũng không ai đủ điều kiện retire.** Cắt bất kỳ model nào
lúc này là **cắt mù**.

### Nhóm Owner yêu cầu soi kỹ

| model | mẫu | tỉ lệ | KTC 95 % | verdict |
|---|---|---|---|---|
| **`gpt-5.5`** | **0** | — | — | **`SHADOW_MEASURE`** — 🟢 **đã ở ngoài đường official**, không có gì để dừng |
| **`qwen3-max-thinking`** | **0** | — | — | **`SHADOW_MEASURE`** — 🟢 như trên |
| `smart-ml` | 90 | 28,9 % | `[20,5–39,0]` | `KEEP_OFFICIAL` — chứa nền |
| `xgboost` | 90 | 28,9 % | `[20,5–39,0]` | `KEEP_OFFICIAL` |
| `random-forest` | 90 | 32,2 % | `[23,5–42,4]` | `KEEP_OFFICIAL` |
| `combo-super` | 90 | 34,4 % | `[25,4–44,7]` | `KEEP_OFFICIAL` |
| `glm-5.1` | 75 | **38,7 %** | `[28,5–50,0]` | `KEEP_OFFICIAL` — cao nhất nhưng KTC **vẫn chứa nền** |
| `deepseek-reasoner` | 89 | 38,2 % | `[28,8–48,6]` | `KEEP_OFFICIAL` |
| `gemini-2.5-flash` | 90 | 32,2 % | `[23,5–42,4]` | `KEEP_OFFICIAL` |
| **`lstm`** | 90 | 30,0 % | `[21,5–40,1]` | `KEEP_OFFICIAL` — **giữ riêng**, không hard-collapse |

⛔ **Verdict là NHÃN ĐO, không phải lệnh thi hành.** Không model nào bị đổi trong phiên này.

---

## 7 · CÒN LẠI — TRUNG THỰC VỀ NHỮNG GÌ CHƯA LÀM

| GĐ | việc | trạng thái |
|---|---|---|
| **GĐ-1** | chấm 21–27/08 | 🟢 **XONG** (3-càng `NOT_SCORABLE` — không có writer) |
| **GĐ-2** | scorer cuốn chiếu | 🟢 **DEPLOY XONG** · `RUNTIME_LOADED` · hành vi chứng minh **16:50 mai** |
| **GĐ-3** | chẩn đoán TOTAL | 🟢 **XONG — phép đo quyết định** · N1/N2/N3 **chưa dựng**, kèm lý do ở mục 4.5 |
| **GĐ-4** | roster verdict | 🟢 **XONG** — 30 model |
| **GĐ-5** | prompt thuần ngữ cảnh | 🔴 **CHƯA** — xem dưới |
| **GĐ-6** | output / UI / bất biến | 🟠 **một phần** — `FU-438` + không-drift đã chứng minh; chuỗi UI đầy đủ chưa |
| **GĐ-7** | tồn đọng (SC-05/08, 34 script, FU-440/441/443/444, 23 report, QD-041…) | 🔴 **CHƯA** |

### Vì sao GĐ-5 **cố ý** chưa làm

Đây là thay đổi CLASS B trên prompt **~18.200 ký tự / 32 khối**, đụng thẳng đường sinh dự đoán.
`§60.1` ghi rõ: **bỏ nửa chừng còn tệ hơn không làm** — chính `V11001` đã gỡ 8 khối rồi để lại
10 chỗ dạy model dùng đúng thứ vừa gỡ, khiến phép đo 14 ngày sau đó **vô giá trị**.

Làm đúng nó cần: dump prompt từ hàm đang serve · lập bản đồ 32 khối · gỡ · **quét ngược có phân
loại** · cấp regime mới · deploy sau FINAL · không trộn cohort. Đó là một phiên riêng, không phải
phần đuôi của phiên này.

**Và có một lý do thứ hai, mạnh hơn:** mục 4 cho thấy pool hiện tại **không giàu hơn ngẫu nhiên**.
Sửa prompt để LLM tự sinh candidate là hướng **đúng** — nhưng phải đo nó bằng chính thước ở mục
4.1 *(pool mới có giàu hơn nền không)*, nếu không sẽ lại được một phép đo không nói lên gì.

---

## 8 · BA LỚP NGUỒN (§62)

### `OWNER_SAID`

> *« Ưu tiên sửa ranking/TOTAL, không thêm model. »*
>
> *« Trước khi đọc kết quả phải đăng ký: effect cần phát hiện, power, cửa sổ, stop rule,
> promotion gate, multiple-comparison correction. »*
>
> *« Phép đo phải có negative control và kiểm tập rỗng. »*
>
> *« Thiếu lực thì ghi `INSUFFICIENT_POWER`. »* · *« `lstm` giữ riêng. »*
>
> *« Không dừng ở plan-only nếu hành động an toàn đã đủ gate. »*

### `CODE_DID`

| việc | bằng chứng |
|---|---|
| chấm 7 ngày | BT 6/21 · X2 1/21 · X3 0/20 · 3-càng `NOT_SCORABLE` |
| phép đo quyết định | n=273 · FINAL 30,77 % vs pool-random 33,72 % · đối chứng 0 %/100 % |
| coverage giải thích được | 99,6 % đo được vs 99,6 % kỳ vọng ngẫu nhiên |
| settlement đã cuốn chiếu | `verified_at` = **cùng giây** kết quả về, cả ba miền |
| deploy scorer | PID `2646084 → 2671007` · 3 job đăng ký trong log APScheduler |
| không regression | `FU-438` 3/3 endpoint vẫn 401 · health 200 |
| không drift | `predictions` · `final_bundles` · FINAL 27/08 không đổi |
| roster | 16 `KEEP_OFFICIAL` · 14 `SHADOW_MEASURE` · **0 trên nền, 0 dưới nền** |

### `DOC_SAID`

| nguồn | ghi gì |
|---|---|
| `PRJ-SELECTION-WINDOW-001` | bỏ shadow · bỏ sau FINAL · tách trong/ngoài cửa sổ |
| `RM-04` | n nhỏ = *«chưa được phép kết luận»* |
| `RM-15` | phép kiểm không đối chứng thì luôn báo xanh |
| `§60.1` | bỏ nửa chừng còn tệ hơn không làm |

### 🔴 BA LỚP LỆCH NHAU

| lệch | chi tiết |
|---|---|
| giả định ≠ đo được | tiền đề *«ML sinh đúng, TOTAL xếp sai»* — đo được **pool cũng chỉ bằng nền**, nên không phải chỉ lỗi xếp |
| nội bộ phiên | nhãn `RANKING_MISS = 14/21` của chính tôi **không có giá trị chẩn đoán** — ~99,8 % xảy ra do tình cờ |
| nội bộ phiên | script deploy in `RUNTIME_PROVEN`; sự thật là **`RUNTIME_LOADED`** — đã sửa trong mục 5.4 |
| `DOC_SAID` ≠ `CODE_DID` | giả định *«scorer không cuốn chiếu»* — thật ra **settlement đã cuốn chiếu**, chỉ bước đồng bộ bị dồn |

---

## 9 · MUTATION / ROLLBACK LOG

| # | thay đổi | gỡ về |
|---|---|---|
| 1 | `scheduler.py`: `6ba74fa8…` → `a6c8bfff…` (**+23 dòng**, chỉ thêm 3 mốc lịch) | bản sao lưu trên VPS, hash **khớp gốc** |
| 2 | restart dịch vụ ×1 | tự động gỡ về đã cài sẵn — không phải dùng |

**KHÔNG thay đổi:** ghi DB · prediction/FINAL · `main.py` · credential · SSH · hook · Notion ·
Git history · visibility · push code kho riêng.

---

## 10 · KHÔNG CÓ CÂU HỎI CHO OWNER LƯỢT NÀY

Mọi việc CLASS A đủ gate đã tự làm. CLASS C (SSH · `OD-05` · rotation) vẫn chặn ở
`RECOVERY_PATH = NOT_VERIFIED` — **không đổi so với V11126**, và **không** phải việc mới.

Điều duy nhất đáng để Owner cân nhắc **không phải một câu hỏi kỹ thuật** mà là một đề nghị đổi
thứ tự ưu tiên, đã trình bày ở **mục 4.5**: trước khi dựng ba bộ xếp hạng mới, nên trả lời câu
*«có tín hiệu nào để xếp không?»* — vì phép đo hiện tại nói là **chưa có**.

---

TanPhatAI cần làm: ghi vào `docs/FOLLOW_UP_TRACKER.md` **kết quả đo quyết định**: FINAL **30,77 %** vs bốc ngẫu nhiên từ chính pool **33,72 %** vs nền **33,87 %** trên **n = 273** lượt, đối chứng âm/dương **0 %/100 %** — tức **tầng xếp hạng chưa chứng minh được lợi thế nào, và pool cũng không giàu hơn nền**. Ghi rõ rằng coverage **99,6 %** **không phải thành tích** — nó khớp đúng kỳ vọng của pool ngẫu nhiên cùng kích thước. Mở mục cho **scorer cuốn chiếu**: đã deploy, **`RUNTIME_LOADED`**, bằng chứng hành vi sẽ có lúc **16:50 ngày 28/08** — **đừng** ghi `RUNTIME_PROVEN` trước lúc đó. Ghi **3-càng = `NOT_SCORABLE`** (không có cột/bảng writer nào trong 253 bảng). Roster: **16 `KEEP_OFFICIAL` · 14 `SHADOW_MEASURE` · 0 trên nền · 0 dưới nền** ⇒ **không cắt, không promote ai**; `gpt-5.5` và `qwen3-max-thinking` **đã ở ngoài official sẵn**; `lstm` giữ riêng. **Đừng** đọc *«`RANKING_MISS` 14/21»* thành *«ranking hỏng»* — với 16 model và nền 33 %, con số đó xảy ra ~99,8 % **dù ranking hoàn hảo**. **GĐ-5 (prompt thuần ngữ cảnh) CỐ Ý chưa làm** — lý do ở mục 7, và nó cần một phiên riêng.
