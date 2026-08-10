# REPORT V11056 — CHỐT SÁU MỤC C1–C6 + ĐO KHẢ THI D-2 + LUẬT §62 NGUỒN BA LỚP

**Ngày:** 2026-08-10 chiều · **Quyết định owner:** `QD-056` · **Mã đọc:** `LR1008`
**Production KHÔNG đổi trong phiên này** — PID `1286954` · health 200 · hash 4 bảng khoá nguyên

---

## 1. Tóm tắt

Ba việc, và một đính chính nặng của chính agent.

| việc | kết quả |
|---|---|
| **C1–C6** | chốt đủ nhãn, **không mục nào treo trống**: 2 `ĐÃ RÕ` · 4 `PLAN 21/08` · 0 `CHỜ 7 NGÀY` |
| **D-2 cho MN** | **`KHÔNG_KHẢ_THI`** — đo trên **bản thi hành thật**, vế D-2 đóng góp riêng **75/3.991 = 1,9%** ứng viên |
| **§62 (A60)** | luật NGUỒN BA LỚP vào **đủ sáu mặt** + mặt trỏ đường, kèm **cổng máy đã chứng minh chặn được** |

**Đính chính của chính agent, phát hiện trong phiên:** mã trích `V105.19 §7` trong sổ V11054
là **SAI**. Công thức của owner nằm ở **`V105.5`** (`docs/CURRENT_TRUTH_SSOT.md:7252`, ghi
*«Owner formula clarification 2026-05-10 11:22 VN»*). Sáng nay agent còn **nhân mã trích sai
đó vào 5 tệp governance** khi viết §62 — đã sửa hết trong cùng phiên.

Phương pháp: **14 tác nhân** (7 điều tra + 7 phản biện đối kháng). Phản biện **bác được thật**
— trong đó có việc bác lại chính kết luận `ĐÃ RÕ` của C4 và C5.

---

## 2. Owner yêu cầu gì (nguyên văn)

> *«① ĐO khả thi D-2 cho MN (anh mới đề xuất trong tài liệu, CHƯA có chứng minh) · ② làm rõ
> LUÔN toàn bộ mục CHƯA RÕ (C1–C6) rồi chốt một lượt · ③ LUẬT MỚI: NGUỒN BA LỚP.»* — 12:52

> *«MỌI báo cáo phải có mục riêng ghi nhận các trao đổi trong phiên chat/IDE, phân tách ba lớp
> nguồn… anh trao đổi trực tiếp trong IDE nhanh hơn TanPhatAI theo kịp — báo cáo phải đủ để
> TanPhatAI đọc là biết phải đồng bộ/hỗ trợ gì.»* — 12:52

> *«"đúng theo tài liệu" ≠ "có giá trị đo được". PHẢI ĐO TRƯỚC.»* — 12:52

---

## 3. Đào bới / phát hiện — BẢNG CHỐT C1–C6

| mục | nhãn | phát hiện quyết định | evidence |
|---|---|---|---|
| **C1** | **PLAN 21/08** | combo-super **CÓ ghi** model được chọn (181/181 lượt, 60 ngày) nhưng **KHÔNG ghi điểm chọn** — điểm chỉ `print()` ra stdout, mà journald là **volatile trên RAM** | `combo_super.py:2646` ghi `dual_pool_v596`; `combo_super.py:1265` chỉ print; `journalctl --header` → `/run/log/journal` |
| **C2** | **ĐÃ RÕ** | **Câu hỏi sai tiền đề**: không ai tắt writer — **chưa bao giờ có writer định kỳ**. 246.000 dòng ghi trong **một cửa sổ 8 giây** | `computed_at` chỉ có `2026-05-10T13:31:49..13:31:56`; crontab và `scheduler.py` **không có** dòng nào |
| **C3** | **PLAN 21/08** | **CÓ** gộp ngày D vào chính gan của ngày D — `substr(date,1,10) <= ?` với chính `anchor_date` | `_v100_gan_calculator.py:165-168`, xác minh **cả trên VPS**; 3.857 dòng `gan=0` |
| **C4** | **ĐÃ RÕ (tách hai tầng)** | tầng **tệp** verified thật; tầng **owner-eye chưa từng xảy ra**; nhãn `FALSE_NEGATIVE` là **nói về sai mục tiêu** | md5 VPS `f37506cd…` == local; owner nguyên văn 27/07 nói về **nhóm card khác** |
| **C5** | **PLAN 21/08** | đúng **4 bước nhảy** SP-4.0→4.4; **SP-4.3 và SP-4.4 KHÔNG có mục nào trong sổ quyết định**; và **3+ chỗ khoá SP-4.1/4.0 trong MÃ SỐNG** | `git log -L 284,462`: `1cd2833`·`381d9da`·`38fe600`·`9510886`; `_v98_command_center.py:250`; `_v87_master_board.py:99` |
| **C6** | **PLAN 21/08** | **hai bộ 28 đặc trưng khác hẳn nhau**; FU-320 liệt kê 6 là **ĐẾM THIẾU**; **bỏ 6 đặc trưng KHÔNG gỡ được gan khỏi ML** | 12 artifact production đều `n_features_in_=28`; `recency_score` là hàm thuần của `gan_days` |

### C1 — điều đáng nói nhất: cơ chế chọn **tái lập được**, chỉ là **không lưu vết**

Mô phỏng chỉ-đọc bằng đúng SQL của `_ti_le_bach_thu` cho ra **đúng top-3 mà DB đã ghi** cho
ngày 10/08 MN (`claude-opus-4-6` · `deepseek-reasoner` · `lstm`). Nên hiểu biết về pool
**không còn phải suy từ hằng số** — đó là điều C1 đặt ra và nay đã trả lời.

Ba chỗ lệch tìm thêm được:

- ứng viên thật là **4 ML + 9 AI = 13**, dù biến tên `all_8_ids` và dòng in ghi *«4 ML + 4 AI»*
- `model_win_rates` lưu trong DB là **WIN RATE**, còn thước chọn là **BẠCH THỦ** — hai con số
  khác nhau, rất dễ đọc nhầm cái này thành cái kia
- sàn mẫu `MIN_MAU_DU_TUYEN=5` **không áp trên nhánh combo-super** — nhưng **đây KHÔNG phải
  phát hiện mới**: đã nằm trong `FU-265 · DO1208 · hạn 12/08`, status
  `MEASURED_ROOT_CAUSE_FOUND`, từ **04/08**. Phản biện bắt đúng chỗ agent suýt trình lại thứ
  đã có sẵn — **đúng lỗi khuôn mà owner đã phê bình ở V11054.**

**Vì sao PLAN 21/08:** thêm câu ghi điểm chọn phải sửa `combo_super.py` — module **sinh số
công bố**. `QD-041` khoá tới 21/08. Không lách bằng lý do «chỉ ghi log».

### C2 — «ai tắt» là câu hỏi sai; câu đúng là «lớp bằng chứng đang rỗng câm»

Bảng **không chết** (RM-20): còn **1 điểm đọc SỐNG** —
`_v10763_pattern_reasoning_shadow.py:325`, gọi từ `scheduler.py:551` và route
`/api/admin/pattern-reasoning` (`main.py:15949`), **chạy mỗi ngày**. Nhưng truy vấn đó trả
**0 dòng liên tục 93 ngày** ⇒ lớp bằng chứng «gan» trong pattern-reasoning **rỗng âm thầm,
không báo lỗi**. Đó mới là vấn đề, không phải «ai tắt».

### C3 — có nhìn trộm, nhưng nhãn phải ghi ĐÚNG TẦNG

Phản biện chỉnh lại một điểm quan trọng: DDL của chính writer ghi
`anchor_date -- date when gan computed (today's perspective)` (`_v100_gan_calculator.py:54`),
nên gộp ngày D **đúng theo hợp đồng của nó**. Lỗi nằm ở **bên TIÊU THỤ** đã dùng `anchor=D` để
chấm chính ngày D. Và phản biện tính được phép **EX-ANTE đúng chuẩn** (anchor D → ngày D+1)
ngay trên cùng bảng đó ⇒ **không được kết luận «gan vô dụng»**.

Phản biện cũng bắt agent gọi sai chữ **«nền»**: `16–24%` là **tỉ lệ trúng**, không phải nền
(RM-18). Nền thật là `|đuôi ra ngày đó| / 100`.

### C4 — chỉ mục này được chốt ngay, và phải tách hai tầng (RM-12)

| tầng | verdict | vì sao |
|---|---|---|
| **LIVE_FILE** | **ĐÃ RÕ — verified** | md5 tệp đang phục vụ trên VPS `f37506cd…` **trùng y hệt** local; backup PRE `75155b03…` trùng `backups/v10864_pre/`; mốc thời gian VPS 27/07 09:55 độc lập |
| **OWNER_EYE** | **chưa từng xảy ra** | cả ba mặt đều dừng ở `DEPLOYED_PENDING_LIVE_VERIFY`; owner nguyên văn 27/07 đang nói về **nhóm card khác** (`FU-V10865` station cards) |

**Và phải nói thẳng: «4/4 phép kiểm ĐẠT» KHÔNG dùng làm bằng chứng được.**
Hai trong bốn phép là **tautology** — `'.v50-kv {' in t and 'min-width: 0' in t` là **hai phép
`in` độc lập trên toàn tệp**, không hề ràng buộc thứ này nằm trong thứ kia. Và `journal 0` là
**hằng số viết cứng** `"journal_errors": 0,` (`_v10864_deploy.py:99`), không phải số đo được.

### C5 — hai thứ nặng hơn cả bản đồ delta

1. **`SP-4.3` và `SP-4.4` KHÔNG có mục nào trong `docs/OWNER_DECISION_LEDGER.json`** — trong
   khi `SP-4.1` có `DEC-019-PROMPT-2NUM` và `SP-4.2` có `QD-037`. Hai lần đổi prompt gần nhất
   **không có chữ ký**.
2. Chỗ thật sự còn **khoá SP-4.1** không nằm trong `docs/` mà là **MÃ SỐNG đang phục vụ**:
   `_v98_command_center.py:250` — và ít nhất còn `_v87_master_board.py:99` ghi **SP-4.0**.

Phản biện thêm một cảnh báo phương pháp: **chuỗi gửi cho model ≠ chuỗi trong tệp**. Đường phục
vụ thật là `gpt_analyzer.py:6195 analyze_and_predict` → `:6317` mới ráp. Mọi con số ký tự đo
trên lát cắt mã nguồn (dòng 284-462) **không phải** số của prompt thật (RM-14).

### C6 — «bỏ 6 đặc trưng» không gỡ được gan khỏi ML

- Có **HAI** bộ 28 đặc trưng khác hẳn nhau: bộ cây/meta (`FEATURE_COLS`, khai ở **bốn** nơi) và
  bộ meta của LSTM (28 chiều, danh sách hoàn toàn khác).
- **FU-320 liệt kê 6 là đếm thiếu:** `recency_score` là **hàm thuần của `gan_days`** (thứ 7), và
  `total_score` do gan quyết định **54,6–63,1%** ⇒ `stat_rank`/`in_top10`/`in_top20` đều nhiễm gan.
- **Lệch huấn luyện/phục vụ có thật:** `freq_x_gan` là **hằng số 0 khi suy luận** (cùng 4 đặc
  trưng khác), và `in_top20` **hằng số 1** khi phục vụ vs trung bình 0,478 khi huấn luyện.
- Phản biện sửa hai con số agent công bố: **60–70% → 54,6–63,1%** và **14,1–23,2% → 8,1–19,7%**
  (khi phục vụ), và bác cổng «30 ứng viên» — cổng thật là **20**, vì `all_scores` chỉ có 20 phần
  tử nên `[:30]` **không bao giờ ràng buộc**.

---

## 4. Hướng xử lý và vì sao — ĐO KHẢ THI D-2 (GĐ-2)

### 4.1 · Bẫy chính và cách tránh

Nguồn cross-region là một **TẬP ĐUÔI**. Tập càng to càng dễ «chứa» đuôi trúng — **kể cả khi vô
nghĩa**. Nên **cấm so độ phủ trần**; phải so với **nền đúng cho từng bên** (RM-18):

```
lợi thế  =  độ phủ thật  −  (cỡ tập / 100)
```

### 4.2 · Mô phỏng 2.337 ngày (Đ1–Đ2)

| | độ phủ | cỡ tập | nền (k/100) | **lợi thế** |
|---|---|---|---|---|
| chỉ D-1 (mã hiện tại) | 70,4% | 70,4 | 70,4% | **−0,003pp** · CI95 [−0,364 … +0,358] |
| D-1 + D-2 (owner khoá) | 91,1% | 91,1 | 91,1% | **+0,031pp** · CI95 [−0,202 … +0,265] |

Độ phủ tăng **+20,7pp** nhưng **toàn bộ** mức tăng là **nền dâng lên**. CI chỉ rộng **±0,23pp**
⇒ đây **không phải «chưa biết»** mà là **đã đo chính xác và bằng KHÔNG**.

**Bền vững ở phạm vi hẹp (G8+ĐB):** tập 11,9 → 22,4 đuôi, lợi thế `+0,056` và `+0,148pp`,
**CI vẫn trùm 0**. Kết luận **bền qua cả hai phạm vi**.

### 4.3 · Đ4 — đo trên CHÍNH BẢN THI HÀNH THẬT (mạnh hơn mọi mô phỏng)

Vế D-2 **đã từng được thi hành thật**: `_v101_shadow_pilot.materialize_mn_cross_region_rule`
(`method_version = v101_mn_cross_region_d1_d2_v1`) ghi bảng `v101_mn_cross_region_rule_shadow`
— **133 ngày, 3.991 ứng viên**, mỗi ứng viên tách riêng `d1_occurrences` và `d2_occurrences`.

| nhóm ứng viên | trúng | tỉ lệ | so nền **43,2%** | z |
|---|---|---|---|---|
| CHỈ D-1 tìm ra | 163/358 | 45,5% | +2,3pp | +0,52 |
| cả D-1 và D-2 cùng có | 1559/3558 | 43,8% | +0,6pp | +0,43 |
| **CHỈ D-2 tìm ra** | **34/75** | **45,3%** | **+2,1pp** | **+0,22** |

### 4.4 · VERDICT: **`KHÔNG_KHẢ_THI`**

Lý do là **lập luận KHỐI LƯỢNG, không phụ thuộc thống kê** — nên không bị `n=75` làm hỏng:

> Vế D-2 đóng góp **riêng** đúng **75/3.991 = 1,9%** ứng viên, tức **0,56 ứng viên/ngày**.
> Dù `+2,1pp` có thật đi nữa, áp lên 0,56 ứng viên/ngày chỉ ra **~0,012 lượt trúng thêm mỗi
> ngày**. Khớp với mô phỏng 2.337 ngày: lợi thế trên nền `+0,031pp`, CI95 `±0,233pp`.

**RM-04 cấm kết luận từ `n=75` về TỈ LỆ — nhưng không cấm kết luận từ TỈ TRỌNG.** Hai chuyện
khác nhau, và ở đây tỉ trọng mới là thứ quyết định.

### 4.5 · Giới hạn — khai trước, không giấu ở cuối

- Đo trên **quá khứ** ⇒ chỉ đủ tư cách **SƠ TUYỂN / LOẠI BỚT**, **tuyệt đối không dùng để
  DUYỆT**. Sáu lần backtest đã rữa (V10655→V10790).
- **Đ3 là CHẶN TRÊN**, không phải mức đạt được: đuôi nằm trong nguồn ≠ model sẽ sinh ra nó.
- Phép này đo **tư cách thành viên tập đuôi**. Nếu `§9` rút ra **luật cầu có cấu trúc**
  (giải→giải kèm lag) thì đó là đối tượng **mịn hơn** mà phép này **không kiểm**.

---

## 5. Đã làm gì

| # | việc | bằng chứng |
|---|---|---|
| 1 | `§62 (A60)` NGUỒN BA LỚP vào **đủ sáu mặt** + mặt trỏ đường | `_v10925_rule_sync_check.py` → **SÁU MẶT ĐỒNG BỘ** |
| 2 | Nối **cổng máy** cho §62 vào `_v10921_report_gate.py` | dò `OWNER_SAID`/`CODE_DID`/`DOC_SAID` + dòng `TanPhatAI cần làm:` |
| 3 | `_v11056_do_d2_mn.py` — 4 phép đo D-2, READ-ONLY | `artifacts/v11056/d2_mn.json` |
| 4 | 14 tác nhân điều tra + phản biện đối kháng C1–C6 | 1,6 triệu token · 562 lượt gọi công cụ |
| 5 | **Sửa mã trích sai** `V105.19 §7` → `V105.5` ở 4 tệp sống + 2 mặt sinh | `grep` còn 0 trong tệp sống |
| 6 | Ghi **đính chính có TRƯỚC/SAU** vào sổ V11054 | `artifacts/v11054/SO_DANG_KY_VAN_DE_V11054.md` |

**KHÔNG đụng production:** không deploy · không restart · không sửa prompt/đường chọn số/roster.

---

## 6. Cổng kiểm — xác minh

| cổng | kết quả |
|---|---|
| `_v11044_cong_so_hieu.py` (FU-369) | V11056 · FU-395 · QD-056 là số trống — **cấp đúng** |
| `_v10925_rule_sync_check.py` | **SÁU MẶT ĐỒNG BỘ** sau khi thêm §62 |
| `_v10921_report_gate.py` **thử chặn (RM-15)** | V11056 thiếu mục ba lớp ⇒ **✗ `A60_VIOLATION_NO_THREE_LAYER`**; V11055 (báo cáo cũ) ⇒ **✓ không bị bắt oan** |
| `_v10920_decision_ledger.py` | **KHÔNG CÓ QUYẾT ĐỊNH NÀO BỊ TRÔI** |
| RM-01 tuổi dữ liệu | manifest 10/08 10:09 — **3,0 giờ** ⇒ ĐẠT |
| RM-10 đối chiếu hàm thật | so với `database.get_all_tails` — **lệch 0** |

Cổng §62 chặn theo **mốc V11056 trở đi**: ép ngược lên báo cáo cũ sẽ làm cổng đỏ hàng loạt vì
một luật chưa tồn tại lúc chúng được viết — **cổng đỏ vì lý do sai thì người ta học cách bỏ qua
nó**, và cổng coi như chết.

---

## 6bis. §62 (A60) — NGUỒN BA LỚP

### `OWNER_SAID`

| giờ | nguyên văn |
|---|---|
| **10/08 12:52** | *«① ĐO khả thi D-2 cho MN (anh mới đề xuất trong tài liệu, CHƯA có chứng minh) · ② làm rõ LUÔN toàn bộ mục CHƯA RÕ (C1–C6) rồi chốt một lượt · ③ LUẬT MỚI: NGUỒN BA LỚP.»* |
| **10/08 12:52** | *«anh trao đổi trực tiếp trong IDE nhanh hơn TanPhatAI theo kịp — báo cáo phải đủ để TanPhatAI đọc là biết phải đồng bộ/hỗ trợ gì.»* |
| **10/08 sáng** | *«FU360, Và P4 luôn nha em cái này hiếm gặp ==> tiến hành»* |
| **10/05 11:22** | *«`MN_D=(MN+MT+MB) D-1 + (MN+MT+MB) D-2`, `MT_D=(MN+MT+MB) D-1 + MN D`, `MB_D=(MN+MT+MB) D-1 + MN D + MT D`»* — và nói rõ **MT/MB không được đổi ngoài các công thức đã duyệt** |

### `CODE_DID`

| mã làm gì | evidence |
|---|---|
| `RR §9` official cho MN **chỉ có D-1** | `gpt_analyzer.py:529-535`, xác minh **y hệt trên VPS** |
| vế **D-2 CÓ được thi hành** — nhưng **chỉ ở lane SHADOW** | `_v101_shadow_pilot.py:505` + `gpt_analyzer.py:6090`, cổng `lane_test_shadow_pack` chỉ bật từ `shadow_auto_eval` (`gpt_analyzer.py:6218`) |
| bảng thi hành D-2 **đóng băng từ 30/05** | `v101_mn_cross_region_rule_shadow` 3.991 dòng, `MAX(target_date)=2026-05-30` |
| combo-super **ghi model chọn nhưng không ghi điểm chọn** | `combo_super.py:2646` vs `combo_super.py:1265` (chỉ `print`) |
| gan writer **chưa bao giờ có cron** | `computed_at` chỉ một cửa sổ 8 giây `2026-05-10T13:31:49..56` |
| `SP-4.3`/`SP-4.4` deploy **không có chữ ký owner** | `docs/OWNER_DECISION_LEDGER.json` — 0 mục ngày 2026-08-07 |

### `DOC_SAID`

| tài liệu ghi gì | file:mục | lệch với thực tế? |
|---|---|---|
| công thức D-2 cho MN | `docs/CURRENT_TRUTH_SSOT.md:7252` (**V105.5**) | **khớp OWNER_SAID** |
| *«V105.19 §7 (owner khoá)»* | `artifacts/v11054/SO_DANG_KY_VAN_DE_V11054.md:32` | ✗ **SAI MÃ TRÍCH** — đã đính chính |
| *«RR §9 thiếu D-2 ⇒ mã thiếu»* | cùng file, mục M2 | ✗ **mô tả sai bản chất** — mã có, chỉ nằm ở lane shadow |
| khoá `SP-4.1` | `_v98_command_center.py:250` · `_v87_master_board.py:99` (**mã sống**) | ✗ **lạc hậu** — mã chạy `SP-4.4` |
| `FU-320` liệt kê **6** đặc trưng gan | `docs/FOLLOW_UP_TRACKER.md` | ✗ **đếm thiếu** — ít nhất 7, và `total_score` nhiễm gan 54,6–63,1% |
| `FU-265` sàn 5 lượt, hạn 12/08 | `docs/FOLLOW_UP_TRACKER.md:2740-2775` | **khớp** — agent suýt trình lại như phát hiện mới |

### Ba lớp lệch nhau ⇒ FINDING (đúng §62.2)

1. **`OWNER_SAID` ≠ `CODE_DID`** — owner khoá D-2 cho MN từ 10/05; official `RR §9` chưa bao giờ
   có. Nhưng **đo xong thì KHÔNG nên sửa cho khớp** — xem §4.4.
2. **`DOC_SAID` ≠ thực tế (hai lần)** — mã trích `V105.19 §7` sai, và mô tả *«mã thiếu»* sai bản
   chất. **Cả hai đều do agent viết**, và một trong hai đã bị nhân vào 5 tệp governance sáng nay.
3. **`DOC_SAID` ≠ `CODE_DID`** — tài liệu và mã sống khoá `SP-4.1`/`SP-4.0` trong khi production
   chạy `SP-4.4`.

---

## 7. Vướng vấp — lỗi tự gây

| # | vấp | quy tắc |
|---|---|---|
| 1 | Sổ V11054 ghi bảng **`prediction_reasoning`** — bảng đó **không tồn tại**; cột thật là `predictions.reasoning_json` | **RM-10** |
| 2 | Mã trích **`V105.19 §7`** sai (thật là `V105.5`), rồi **nhân vào 5 tệp governance** sáng nay khi viết §62 | **RM-10** + §62.2 |
| 3 | Mô tả M2 *«mã thiếu D-2»* — thật ra mã **có**, chỉ nằm ở lane shadow | **RM-13** |
| 4 | Điều tra viên C1 trình sàn `MIN_MAU_DU_TUYEN` như **phát hiện mới** — đã là `FU-265` từ 04/08 | §56 |
| 5 | Điều tra viên C4 dùng *«4/4 phép kiểm ĐẠT»* làm bằng chứng — 2 phép là **tautology**, `journal 0` là **hằng số viết cứng** | **RM-09** |
| 6 | Điều tra viên C3 gọi `16–24%` là **«nền»** — đó là **tỉ lệ trúng** | **RM-18** |
| 7 | Verdict D-2 bản đầu phân loại `CHƯA_ĐỦ_BẰNG_CHỨNG` trong khi CI chỉ rộng ±0,23pp — **«chưa biết» khác hẳn «đã đo và bằng 0»** | **RM-04** |

**Bảy vấp, năm cái do phản biện đối kháng bắt được, hai cái agent tự bắt.** Không có tầng phản
biện thì `C4` và `C5` đã được đóng nhãn `ĐÃ RÕ` sai.

---

## 8. Gỡ về

Phiên này **không đụng production** nên không có gì phải gỡ ở tầng runtime.

```bash
# gỡ §62 khỏi sáu mặt (nếu owner bác luật)
git revert <sha V11056>
python web/backend/_v10925_rule_sync_check.py      # sinh lại AGENTS.md + GEMINI.md

# gỡ cổng §62 riêng, giữ luật
#   xoá khối PHAN_62 trong web/backend/_v10921_report_gate.py
```

Bộ đo D-2 (`_v11056_do_d2_mn.py`) là **read-only**, xoá tệp là hết dấu vết.

---

## 9. Theo dõi tiếp

| mã | việc | ngưỡng hành động | mốc |
|---|---|---|---|
| **FU-360** · `CL1008` | canh 24h chặn chéo lane | **bất kỳ** lần chặn NHẦM ⇒ rollback ngay | **sáng 11/08** |
| **FU-395** · `HT2108` | gói 21/08: C1 ghi điểm chọn · C3 phép kiểm biên · C5 chữ ký SP-4.3/4.4 + gỡ khoá lạc hậu · C6 phương án gan trong ML | owner ký từng mục | **21/08** |
| **FU-265** · `DO1208` | sàn 5 lượt không áp ở nhánh combo-super | đã có sẵn, **không tạo mã mới** | **12/08** |
| **FU-320** | 6 đặc trưng gan trong ML — **đếm thiếu**, phải sửa thành ≥7 | — | cùng gói 21/08 |
| — | `D-2` cho MN: **KHÔNG_KHẢ_THI**, **không đưa vào gói 21/08** | — | đóng |
| FU-284 | cửa sổ đang chạy | **9,53** điểm · z ≥ 1,96 · n ≥ 150 | **20/08** — cấm đọc sớm |
| DEHERD_V1 | mới **1/21** ngày | ≥21 ngày · dẫn official · không thua miền nào | **19/08** |

**Đã dùng 1 mã FU mới (`FU-395`)** — đúng trần 5 FU/phiên (391·392·393·394·395).

---

TanPhatAI cần làm: ① cập nhật `docs/OWNER_DECISION_LEDGER.json` mục **`QD-056`** (owner ký 10/08 12:52 — luật §62 NGUỒN BA LỚP + lệnh đo D-2 trước khi sửa) và **`FU-395`** gói 21/08 gồm C1/C3/C5/C6; ② **đính chính** mọi nơi còn ghi mã trích *«V105.19 §7»* thành **`V105.5`** (`docs/CURRENT_TRUTH_SSOT.md:7252`, owner ký 10/05/2026 11:22) — sổ V11054 đã có banner đính chính, các bản sao khác cần rà; ③ ghi nhận verdict **D-2 = `KHÔNG_KHẢ_THI`** để **không đưa `D-2` vào gói mở khoá 21/08**; ④ theo dõi **`FU-360` chốt hay rollback sáng 11/08** và **`FU-265` hạn 12/08** (đã có sẵn, đừng cấp mã mới).
