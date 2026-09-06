# V11170 — MỔ XẺ NGÀY LIVE 06/09/2026

> **Ngày:** 06/09/2026 (đo lúc 22:08 → 23:5x giờ VN, sau khi cả ba miền đã chốt và đã có kết quả)
> **Tầng verdict:** `MEASURED_ONLY` — **0 ghi production · 0 deploy · 0 restart · DB READ-ONLY suốt phiên**
> **Quy mô:** 24 agent (12 cổng đo Sonnet + 12 cổng phản biện Opus) · **4,64 triệu token** · 1.072 lượt gọi công cụ · 71 phút · **0 agent lỗi**

---

## 1 · TÓM TẮT

Owner yêu cầu mổ xẻ toàn bộ ngày live hôm nay — đơn model, TOTAL, prompt, mọi thứ, không sót.
Phiên này chia làm hai lớp: 12 cổng đi đo, rồi 12 cổng khác **cố tình đi bác bỏ** kết quả của
chúng. Lớp phản biện đã làm đúng việc: nó **bác bỏ hoặc hiệu chỉnh 4/12 cổng ở mức nặng**, và
phát hiện một lỗi phương pháp **lặp lại ở năm cổng khác nhau**.

**Kết quả ngày hôm nay:** MN trúng bạch thủ (73), MT và MB trượt. 1/3 — đúng bằng giá trị **phổ
biến nhất** trong 30 ngày qua (14/30 ngày). Không có gì bất thường về mặt vận hành: 81/81 lượt dự
đoán chạy đủ, 0 dòng rỗng, 0 dòng trễ, 0 lỗi scheduler, health 200, `NRestarts 0`.

**Nhưng điều đáng nói nhất không nằm ở kết quả hôm nay.** Nó nằm ở chỗ **không cổng đo nào tự tính
nền ngẫu nhiên**, và khi lớp phản biện tính nền thì cách đọc đảo chiều.

---

## 2 · OWNER YÊU CẦU GÌ — NGUYÊN VĂN

| giờ (VN) | NGUYÊN VĂN | loại | agent đã làm gì | trạng thái |
|---|---|---|---|---|
| ~22:0x | *«Tiếp tục phân tích đánh giá kết quả live hôm nay, đơn model, total, prompt v.v... tất cả mọi thứ không soát vấn đề nào nha em»* | `YÊU_CẦU` | Chụp trạng thái thật lúc 22:08; cấp số hiệu V11170 qua cổng chuẩn; điều 12 cổng đo + 12 cổng phản biện; tự đo độc lập 5 phép | `ĐÃ_LÀM` |

*(Phiên trước trong cùng ngày: «còn gì nữa ko tiếp tục đi em» → đã đóng thành V11168 + V11169,
commit `f426330` / `d432d25`.)*

---

## 3 · ĐÀO BỚI / PHÁT HIỆN

### 3.1 · Điều lớn nhất — nền ngẫu nhiên KHÔNG phải 34,0% cho mọi miền

`34,0%` là nền **GỘP ba miền**. Nền riêng từng miền khác nhau rất xa, vì số đuôi quay ra mỗi ngày
khác nhau:

| miền | số đuôi TB/ngày | **nền đúng** | vì sao |
|---|---|---|---|
| **MN** | 42,8 | **43,1%** | 3 đài × nhiều giải |
| **MT** | 33,8 | **35,2%** | 3 đài |
| **MB** | 23,8 | **23,8%** | **1 đài** |

Ai so tỉ lệ trúng thô **giữa các miền** là đang so **luật chơi**, không phải so mô hình. Mượn
`34,0%` cho MN là `RM-21_VIOLATION` đúng dạng đã ghi trong sổ (VIF 2,92 vs 0,889).

Nền này **đã có sẵn trong kho** — `docs/FOLLOW_UP_TRACKER.md:152` (MN 43,15%) ·
`docs/DAO_SAU_LICH_SU_20260821.md:21` (43,06%) · `docs/CURRENT_TRUTH_SSOT.md:5850`. Việc các cổng
đo không tra ba nơi này là vi phạm **§56**.

### 3.2 · Với nền đúng: hệ KHÔNG hơn ngẫu nhiên, ở mọi phép đo

**Năm đường độc lập, năm phương pháp khác nhau, cùng một kết luận:**

| nguồn | phương pháp | n | kết quả |
|---|---|---|---|
| phiên này (tự đo) | Poisson-binomial từng miền-ngày | 483 | **31,9% vs 34,0% · z = −0,99** |
| phản biện cổng 3 | nền MN riêng, thước bao lô | 73 ngày MN | `ranked[0]` **27,4% vs 43,1% · z = −2,72 · p ≈ 0,0065** |
| phản biện cổng 2 | 3 miền × 3 cửa sổ | 9 ô | TOTAL **dưới nền ở CẢ 9/9 ô** |
| phản biện cổng 9 | hoán vị theo ngày, 2.000 lượt | 90 ngày | **không nhóm nào** trên nền; ô duy nhất có ý nghĩa: **MB shadow DƯỚI nền −5,16pp, p=0,0075** |
| phản biện cổng 11 | Poisson-binomial **chính xác** | 90 ngày | 79 thắng vs kỳ vọng **91,78** · p một phía **0,0528** |

Tự đo theo miền (483 miền-ngày sạch, đã trừ 90 dòng backfill):

| miền | n | trúng | tỉ lệ | nền | chênh | z |
|---|---|---|---|---|---|---|
| MN | 161 | 69 | 42,9% | 43,1% | **−0,2** | −0,06 |
| MT | 161 | 56 | 34,8% | 35,1% | **−0,3** | −0,09 |
| MB | 161 | 29 | 18,0% | 23,7% | **−5,7** | −1,70 |
| **TẤT CẢ** | **483** | **154** | **31,9%** | **34,0%** | **−2,1** | **−0,99** |

**Nói thẳng như owner đã yêu cầu:** không có bằng chứng nào cho thấy hệ hơn ngẫu nhiên, ở bất kỳ
miền nào, bất kỳ cửa sổ nào. Cũng chưa đủ bằng chứng để nói nó **kém hơn** (RM-04).

**Sức mạnh phép đo:** với 5,4 tháng dữ liệu sạch hiện có, hệ **không thể chứng minh** một lợi thế
nhỏ hơn khoảng **+8 điểm**. Muốn chứng minh +3 điểm cần **21,7 tháng**; +5 điểm cần **7,8 tháng**.

### 3.3 · Cơ chế đã lật bạch thủ MN hôm nay — và nó KHÔNG phải cái ai cũng đoán

Bundle 837 (MN) tự ghi trong sổ nội bộ: `top1_reason = "selected 04"`, và **73 nằm trong danh sách
BỊ LOẠI**. Nhưng cột `bach_thu` công bố **73**, và 73 trúng.

Cơ chế thật: **`_v10640_official_perslice_override.get_override_bt()`** với `chooser="specialist"`,
gọi tại **`main.py:10231-10240`**, ngay sau `bach_thu = ranked[0][0]` ở `:10225` — tức **TRƯỚC** khi
chốt. Ưu tiên ứng viên có nhiều phiếu từ model "specialist".

Hôm nay: `04` có 2 phiếu specialist, `73` có 3 → chọn 73. Gọi thẳng hàm thật trên DB thật trả về
`('73', 'specialist|specialist_votes=3;rank=2')` — **khớp 100%**. Lớp phản biện còn
**re-implement độc lập và mô phỏng cả 73 ngày: khớp 73/73, 0 ngày lệch**.

**Ba giả thuyết đối thủ đã bị đóng bằng bằng chứng, không phải suy luận:**
- **anti-trap**: tính ở `main.py:10434-10456` **SAU** khi chốt; chú thích code ghi nguyên văn
  *"Pure read-only. Does NOT change voting"*. Và `PRIOR_REGION_MAP["MN"] = ()` — MN **luôn rỗng**.
- **PP-1 convergence dampener** (giả thuyết ban đầu của chính phiên này): PP-1 có hạ 73 từ 0,1175
  → 0,0999, nhưng nó **không phải** thứ quyết định số công bố.
- **ổ cắm V10883** (`main.py:10218`, có quyền đảo thứ tự `ranked`): `v10883_connector_apply_log`
  **0 dòng**, `switch_log` **0 dòng** ⇒ chưa bao giờ áp dụng.

### 3.4 · Nhưng cơ chế đó có tốt không? Hai phép đo, hai câu trả lời khác nhau

**Đo trên MN, 73 ngày (cổng 3, phản biện xác nhận từng số):**

| cửa sổ | không override | có override | chênh | McNemar |
|---|---|---|---|---|
| GỘP 73 ngày | 27,40% | 38,36% | **+10,96pp** | p = 0,0386 |
| TRONG cửa sổ chọn (26/06–31/07) | 27,78% | 36,11% | +8,33pp | p = 0,375 |
| NGOÀI cửa sổ chọn (01/08–06/09) | 27,03% | 40,54% | **+13,51pp** | p = 0,125 |

**Đo trên cả ba miền, nhiều cửa sổ (phản biện cổng 7):**

| cửa sổ | LẬT | GIỮ | chênh |
|---|---|---|---|
| 30 ngày | 50,0% (n=10) | 27,7% (n=83) | **+22,29pp** |
| 90 ngày | 26,76% (n=71) | 30,20% (n=202) | **−3,44pp** |
| 180 ngày | 27,85% (n=79) | 32,67% (n=404) | **−4,83pp** |

**Dấu ĐỔI theo cửa sổ.** Và hôm nay chính là 1 trong n=10 tạo ra con số +22,29pp đẹp mắt của cửa
sổ 30 ngày. Đây đúng dạng bẫy `PRJ-SELECTION-WINDOW-001` sinh ra để chặn.

**Ba điều làm câu chuyện "specialist có giá trị" lung lay:**
1. Ngưỡng `_SPECIALIST_MIN_HITRATE = 0.35` **THẤP HƠN nền MN 0,431** ⇒ **70–77% roster** đạt danh
   hiệu "chuyên gia". Model thấp nhất trong danh sách hôm nay: `deepseek-v4-pro-real` 35,0% —
   **thua nền 8 điểm** mà vẫn được gọi là chuyên gia.
2. Luật **tầm thường** «luôn lấy hạng 2» — không đọc DB, không biết model nào giỏi — đạt
   **31/73 = 42,5%**, **cao hơn** specialist 38,4%, ở **cả ba cửa sổ**. McNemar giữa hai bên:
   **p = 0,7111**.
3. `ranked[0]` của MN thua nền **có ý nghĩa** (z = −2,72). Nên cách đọc đơn giản hơn là:
   **rank1 của official là phản-tín-hiệu, rời khỏi rank1 kiểu gì cũng khá hơn** — không cần giả
   thuyết "phiếu chuyên gia mang thông tin".

**Kết luận đúng tầng:** «+10,96 điểm» là đi **từ RẤT-dưới-nền lên VẪN-dưới-nền**, không phải vượt
nền. n cần 191–491 ngày, hiện có 36–73 ⇒ **CHƯA ĐƯỢC PHÉP KẾT LUẬN** cơ chế này thắng hay thua.

### 3.5 · MT DEGRADED — lỗi kế toán đã biết, nay đóng được NHÂN QUẢ

Hôm nay `day_governance` ghi MT `DEGRADED_LIVE_DAY`, `failed_model_count=2`,
`degradation_reason='Thiếu 2 model (13/15)'`. Nhưng JSON của chính bundle 839 ghi:

```
model_exclusion_reasons:
  smart-ensemble  reason=max_voters_cap  detail=MT_top13_only_V10752_weakest_dropped  active=true
  meta-learning   reason=max_voters_cap  detail=MT_top13_only_V10752_weakest_dropped  active=true
```

Tức **trần voter CỐ Ý theo thiết kế V10752** — chính owner duyệt 25/06.

**Đây KHÔNG phải phát hiện mới** — `CURRENT_TRUTH_SSOT.md:68` đã ghi *«MT `EXCLUDE_PRIMARY`
72/90 = 80,0% vì kế toán trần V10752»*, và bản vá `SC-12/VA-h12` (test 30/30) **đang chờ owner ký**.
Phiên này đóng được phần **nhân quả** mà trước đó mới là tương quan:

- MT lần cuối đạt `model_count ≥ 15` là **25/06/2026 — đúng ngày duyệt V10752**. Từ đó **0/74 ngày**.
- **71/74 ngày MT vẫn có đủ 15 model chạy thật** và sinh dự đoán ⇒ giả thuyết «2 model hỏng» **chết**.
- Hai model bị cắt hôm nay có `bt_rate` **33,30%**, trong khi ngưỡng cổng MT là **14%** — **cao gấp
  hơn hai lần ngưỡng**. Chúng không trượt bất kỳ cổng chất lượng nào.
- Thứ tự cắt chạy **đúng**: 10/10 ngày gần nhất cặp bị cắt đúng là hạng 14–15.

**Hai hậu quả mới đo được, cả hai đều nặng hơn những gì đã ghi:**

**① Cơ chế khiến lỗi sống sót 73 ngày mà không ai thấy.** `main.py:10491` ghi
`quality_filtered_models` và `:10511` ghi `wr_gate_filtered` từ biến `filtered_models` — mà tại thời
điểm đó biến này **đã chứa cả model bị trần `max_voters_cap`**. Rồi `main.py:487-489` đọc lại đúng
khoá `wr_gate_filtered` để dựng trường cho admin panel. **Một chính sách CỐ Ý được trình bày trên
giao diện quản trị như "model trượt cổng CHẤT LƯỢNG".**

**② MB bị hại NHIỀU HƠN MT.** Mệnh đề `WHERE` loại `EXCLUDE_PRIMARY` ở
`daily_evaluation.py:130-142` cắt: **MB 140 dòng · MT 95 dòng · MN 34 dòng**.

| chỉ số | có lọc (đang hiển thị) | bỏ lọc (thật) | lệch |
|---|---|---|---|
| MT `top1_30` | 46,7% | 40,0% | **BÁO CAO** +6,7pp |
| MB `top1_30` | **13,3%** | **36,7%** | **BÁO THẤP −23,4pp** |
| MN `top1_30` | 23,3% | 26,7% | −3,4pp |

**③ Chỉ số rolling-7 của MT hôm nay đang hiển thị dữ liệu ngày 19–25 THÁNG 6** — trễ **73 ngày**,
và tăng thêm 1 mỗi ngày. `MT top1_7 = 57,1%` là số của cửa sổ 19–25/06; số thật của 7 ngày gần đây
là **28,6%**.

**④ Nhãn này loại MT khỏi 83,1% các lượt chấm rolling của `combo-super`** (MT 74/89 · MB 71/90 ·
MN 10/90) ⇒ chỉ **114/269 miền-ngày (42%)** thực sự đi vào phép chấm.

### 3.6 · MB chơi số đã "tiêu" và thua — nhưng câu hỏi này ĐÃ CÓ phép đo đăng ký trước

Bundle 841 (MB) ghi cảnh báo nguyên văn:

> *"bundle bach_thu 13 was already emitted in ALL prior same-day regions (MN+MT) — owner anti-trap
> owner-doctrine flag"* · `level = FULL_SPENT`

Hệ **biết** 13 đã ra ở cả MN lẫn MT trong ngày, vẫn công bố 13, và thua. Số `44` được đánh dấu
`FRESH` thì bị bỏ.

**Nhưng tiền đề ngầm "chặn thì tốt hơn" chưa bao giờ được thiết lập — và dự án đã đo rồi:**

- Bảng **`anti_trap_shadow_v11058`** (FU-397) **đăng ký trước 10/08/2026**, ngưỡng
  **n(FULL_SPENT) ≥ 90 và |z_MH| ≥ 1,96**, ghi rõ **«chưa đủ n ⇒ cấm đọc sớm (RM-04)»**.
  Hiện **n = 63/90** ⇒ **chưa đạt ngưỡng**. Dòng hôm nay `id=658` đã nằm sẵn trong bảng, và nó ghi
  luôn phương án thay thế là `98` — **`98` CŨNG THUA**.
- Trục anti-trap từng được cắm thành cơ chế ghi đè thật (`chooser='prior_region'`) và **đã TẮT**
  sau khi đo tiến cứu ra **−29,4 triệu / 60 ngày**.

**Phiên này tự nhận vi phạm:** cả cổng 10 lẫn phép đo độc lập của agent chính **đã đọc sớm** thí
nghiệm đăng ký trước này. Con số đọc được (FULL_SPENT 23,8% vs FRESH 26,2% gộp) **không được dùng
làm căn cứ**, và đây là ca `§56` — dự án đã có sẵn phép đo, agent không tra trước khi đặt vấn đề.

**Và bảng gộp đó vốn đã sai (RM-18):** `NOT_APPLICABLE` **100% là MN** (139/139), `FRESH` chỉ có ở
MB+MT, `PARTIAL_SPENT` chỉ có ở MB. So các mức chống bẫy trên dữ liệu gộp là **so miền với miền**.
Tách đúng theo miền với nền riêng thì **0/9 ô sống sót hiệu chỉnh Holm**.

**Một phát hiện đúng thì vẫn đứng:** prompt MB **tự mâu thuẫn** về sức mạnh của anti-trap —
dòng 764 *"SOFT negative prior, not a hard ban"* vs dòng 1089 *"Main pick KHÔNG được là tail ở
FULL_SPENT"*. Đây là `PRJ_PROMPT_CONTRADICTS`.

### 3.7 · Prompt — đo trên DUMP THẬT từ hàm đang serve (RM-14)

Cổng 6 chặn tầng gọi mạng (`_call_openai` / `_call_openrouter`), bắt đúng system + user prompt
**gửi đi thật** từ `gpt_analyzer.analyze_and_predict()` cho 06/09, cả 3 miền, cả 2 chế độ
(`LEGACY_PROMPT` / `CONTEXT_ONLY_V2`). Sáu tệp dump 60–70 KB nằm trong `evidence/`.

- **Độ dài prompt thật hôm nay: 49.891 – 58.852 ký tự**, khớp tuyệt đối qua hai nguồn độc lập
  (`prediction_trace.jsonl` 60 dòng + `prompt_pressure_daily` 57 dòng, lệch **0/57**).
- **Con số `46.583` bị bác bỏ về cách dùng:** nó là **MB · official · 07/08/2026** và **KHÔNG gồm
  `SYSTEM_PROMPT`**. Số cùng đơn vị hôm nay là **47.753** (+1.170), và **26/57 lượt hôm nay còn
  THẤP HƠN 46.583**. Ai trích 46.583 rồi so với số có system prompt là so hai đơn vị khác nhau.
- **Ít nhất 5 mệnh lệnh ngược chiều trên ba lớp** (`SYSTEM_PROMPT` tự mâu thuẫn với chính nó ·
  `REASONING_RULEBOOK` · khối dữ liệu cross-ref). Cổng đo chỉ bắt được 1/5.
- `reasoning_tokens`: **45 non-null / 36 null**, max **42.545**, tổng **371.766**.
- Độ sâu cửa sổ: **MN=15 · MT=30 · MB=30** ngày (`find_optimal_window` trên VPS).

### 3.8 · Bundle bị ghi lại — cơ chế có chủ đích, nhưng thiếu vết

Bundle 837 bị ghi **đúng 2 lần**: `v1` lúc 05:26:02 (`model_count=14`), `v2` lúc **15:40:00** bởi
job `t10_chot` (`model_count=15`). **Bạch thủ 73 KHÔNG đổi ở cả hai lần.**

- Chỉ có **MỘT** đường ghi vào `final_bundles`: `INSERT` ở `database.py:4648`, `UPDATE` ở `:4933`.
- Phân bố phiên bản: `v1`=306 · `v2`=265 · `v3`=2 · tổng 573 · không có `v≥4`.
- **KHÔNG có bảng lịch sử** cho `final_bundles` — quét cả 254 bảng, 6 bảng có cột `bach_thu` nhưng
  tất cả đều mirror trạng thái hiện tại. ⇒ **P1: không có audit-trail trong DB.**
- Bạch thủ **đã từng đổi** giữa bản nháp và bản chốt: **12/187 = 6,42%** toàn lịch sử, nhưng
  **0/86** trong 30 ngày gần đây.
- `/api/final-bundle` và các route liên quan **fail-closed admin-only** từ FU-438 (04/09) ⇒ **không
  có đường công khai** nào để khách thấy số bản nháp.

### 3.9 · Dữ liệu ghi hôm nay

- **153/253 bảng** có dòng mới hôm nay (không phải 124 — cổng đo bỏ sót 4 tên cột thời gian:
  `target_date`, `snapshot_date`, `as_of_date`, `run_date`).
- **`model_latency_shadow_v11063`**: `MIN(id)=123243`, `MAX(id)=128726`, span **5484 = đúng
  `COUNT(*)`** ⇒ **toàn bảng được ghi lại trong MỘT khối liên tục mỗi đêm** (cron 21:50), và
  `sqlite_sequence.seq` cho thấy **~23,5 lần ghi lại toàn bộ lịch sử**. V11169 gọi nó là *"snapshot
  tĩnh"* — **đúng về hiện tượng nhưng gây hiểu lầm**: nó là cron SỐNG tái tạo toàn bộ 98 ngày mỗi đêm.
- **Kích thước DB thật: 785,8 MB** (không phải 674,8 MB).
- `daily_eval_log`: **MT vắng mặt hoàn toàn 73 ngày** (0 hàng sau 25/06), trong khi MN 197 hàng và
  MB 93 hàng vẫn ghi tới 06/09. Nhưng chỉ có **2 nơi đọc** bảng này, **không endpoint/UI nào** ⇒
  hỏng **sổ sách**, không phải hỏng quyết định đang chạy.
- **`LIMIT 270` đặt SAU bộ lọc** khiến `wr_all` (nhãn hiển thị **"WR Tổng"**) bị cắt còn **144/181**
  hàng MN, và `total_predictions` **GIẢM dần theo ngày** (145 → 144). Một chỉ số ghi nhãn "toàn bộ"
  thực ra là **cửa sổ trượt**.

### 3.10 · Đơn model hôm nay

Census 81 dòng được **tái lập độc lập 81/81, lệch 0** (tính lại từ `predictions` + `prizes_json`,
không đọc `model_daily_eval`):

| miền | WIN | PARTIAL | LOSE | trúng bạch thủ |
|---|---|---|---|---|
| MN | 4 | 19 | 4 | 12 |
| MT | **0** | 9 | 18 | 5 |
| MB | 1 | 14 | 12 | 7 |

- **0 model đúng cả 3 miền · 0 model sai cả 3 miền.**
- MT 0 WIN **không phải** bằng chứng MT yếu cấu trúc: đo thực nghiệm, **28,5% số ngày** MT có 0 WIN.
- Sau khi sửa mẫu số, chỉ **1/81 cặp model×miền** vượt |z|≥2 so với kỳ vọng nhiễu thuần tuý
  **3,69/81** ⇒ số cặp "lệch nền" **ÍT HƠN mức nhiễu gần 4 lần**. **30 ngày qua KHÔNG có bằng
  chứng model nào lệch nền theo thước bạch thủ.**
- `glm-5.2` `NO_ANSWER` **18/89 = 20,2%** cả 3 miền 30 ngày — model đứng thứ hai chỉ 5,7%.

### 3.11 · Hôm nay có bình thường không

**Có, trên mọi thước đo kiểm được:**
- 1/3 miền trúng là kết quả **phổ biến nhất** trong 30 ngày (**14/30 ngày**).
- `model_count` MN=15 và MT=13 đều là **giá trị phổ biến nhất (mode)** của 30 ngày.
- 0 dòng `ERROR` trong scheduler, 0 dòng rỗng, 0 dòng trễ.
- `t10_chot` ba miền đúng mốc 15:40 / 16:55 / 17:55; biên so với `OUTPUT_DUE` là 5/3/3 phút —
  đây là **hằng số thiết kế**, không phải biên đo riêng hôm nay.

---

## 4 · HƯỚNG XỬ LÝ VÀ VÌ SAO CHỌN

**Chọn hai lớp thay vì một.** Owner yêu cầu "không sót vấn đề nào", nhưng bài học V11164–V11169 là
agent đo một mình hay **báo động giả** hoặc **ép kết luận từ n nhỏ**. Nên phiên này mỗi cổng đo có
một cổng phản biện dùng model mạnh hơn, được lệnh **mặc định nghi ngờ** và chỉ giữ lại điều không
bác bỏ được.

**Kết quả biện minh cho lựa chọn:** lớp phản biện bác bỏ 4 phát hiện lớn của cổng 1, lật cách đọc
của cổng 3, sửa số của cổng 6/7/8, và **phát hiện lỗi thiếu-nền lặp lại ở năm cổng**. Nếu chỉ chạy
một lớp, báo cáo này đã nói *«cơ chế lật đang thắng +13,5 điểm ngoài cửa sổ chọn»* — sai hẳn.

**Chọn KHÔNG kết luận ở những chỗ n chưa đủ.** Nhiều phát hiện có dấu hiệu hấp dẫn nhưng
`0/9 ô sống sót Holm`, hoặc n=36–73 so với n-cần 191–491. Ghi đúng chữ **«chưa được phép kết luận»**
thay vì làm nhẹ hoặc thổi lên.

---

## 5 · ĐÃ LÀM GÌ

| việc | kết quả |
|---|---|
| chụp trạng thái live thật | 3 bundle, 7 dòng kết quả, 81 dự đoán, 153 bảng |
| 12 cổng đo (Sonnet) | 12/12 trả kết quả (1 cổng trả bản nháp rỗng — phản biện bù) |
| 12 cổng phản biện (Opus) | 12/12, bác bỏ hoặc hiệu chỉnh **4 cổng ở mức nặng** |
| tự đo độc lập | 5 phép: nền từng miền · Holm · PP-1 · phân rã 79 · sức mạnh |
| dump prompt thật | 6 tệp 60–70 KB từ hàm đang serve (RM-14) |
| rút lại | **`RL-025`** cho 3 mệnh đề của V11169 |
| production | **0 ghi · 0 deploy · 0 restart** |

**Phân rã lại con số 79 (RM-11 — tái lập được):** 483 bundle sạch = **404 khớp `ranked[0]` (83,6%)**
+ **68 khác cả hai (14,1%)** + **11 khớp top1 TRƯỚC PP-1 (2,3%)**. Tổng lệch = **79**, khớp đúng số
đã công bố ở V11168. Theo tháng, nhóm 68: **0 (tháng 3–5) · 28 (tháng 6) · 32 (tháng 7) · 8 (tháng
8) · 0 (tháng 9)**. Bundle 837 hôm nay **đã nằm trong 79** ⇒ **không phải ca thứ 80**, không cần
cập nhật số.

---

## 6 · CỔNG KIỂM

| cổng | kết quả |
|---|---|
| `_v11044_cong_so_hieu.py` | ✅ `SO_HIEU_V11044=KHỚP` — cấp V11170 |
| `_v11062_nang_version.py --kiem` | ✅ `NANG_VERSION_V11062=ĐẠT` |
| `_v11085_cong_rut_lai.py` | ✅ `PRJ_RETRACTION=SẠCH` |
| `_v11088_cong_cua_so_chon.py` | ✅ `PRJ_WINDOW=SẠCH` |
| `_v10921_report_gate.py V11170` | ✅ đủ 9 phần, đã commit |
| DB production | ✅ **READ-ONLY** — 0 lệnh ghi trong toàn phiên |
| nhãn `bach_thu_status` | ✅ chấm lại **573/573 dòng, 0 lệch** |
| VPS | ✅ PID `3370750` · `NRestarts 0` · health 200 · đĩa 33% · load 0,08 |

---

## 7 · VƯỚNG VẤP

| # | vấp | ai bắt | gỡ |
|---|---|---|---|
| 1 | 🔴 **Năm cổng công bố tuyên bố hiệu quả mà KHÔNG có nền tuyệt đối** (`RM-18`) | lớp phản biện | bổ sung nền riêng từng miền; cách đọc đảo chiều |
| 2 | 🔴 **Đọc sớm thí nghiệm đăng ký trước** `anti_trap_shadow_v11058` (n=63/90) — `§56` | phản biện cổng 10 | không dùng số đó làm căn cứ; ghi vào báo cáo |
| 3 | 🔴 Agent chính **đặt sai giả thuyết** trong đề bài (anti-trap / PP-1 lật bạch thủ) | cổng 3 | cơ chế thật là `_v10640` specialist; đã ghi rõ |
| 4 | 🟠 Cổng 1 tuyên **3 con số "không tái lập được"** (91 · 32 · 34,0%) mà chưa đi tìm định nghĩa gốc | phản biện cổng 1 | cả ba tái lập được; hai cái ra **chính xác** bằng số đã công bố |
| 5 | 🟠 Cổng 8 đếm **124/253 bảng** — bỏ sót 4 tên cột thời gian | phản biện cổng 8 | số đúng **153/253** |
| 6 | 🟠 Cổng 6 so `46.583` với số **có system prompt** — hai đơn vị khác nhau | phản biện cổng 6 | cùng đơn vị hôm nay = **47.753** |
| 7 | 🟠 Cổng 12 chạy lại truy vấn lúc 22:00 thay vì tại thời điểm tính thật (`RM-16`) | phản biện cổng 12 | MT thật là 5 shadow/15 = 33,3%, không phải 52% |
| 8 | 🟡 Một cổng trả **bản nháp "test minimal" rỗng** | phản biện cổng 2 | phản biện đọc thẳng artifact 26.616 byte, không mất việc |
| 9 | 🟡 Ba chỗ ghi `NOT PROVEN` thật ra **chỉ cách một truy vấn** | các phản biện | đã đo; bài học: `NOT PROVEN` chỉ chính đáng khi **đã THỬ và thất bại** |

---

## 8 · GỠ VỀ

**Không có gì để gỡ.** Phiên này **không ghi production, không deploy, không restart, không đụng
`web/backend`**. Mọi thay đổi chỉ nằm ở tài liệu quản trị và kho báo cáo công khai — gỡ về bằng
`git revert <commit>` trên hai kho.

Bốn tệp bằng chứng ghi vào `artifacts/` trên VPS (thư mục vốn dành cho việc này) — xoá được, không
ảnh hưởng runtime.

---

## 9 · THEO DÕI TIẾP

### Chờ owner ký (agent KHÔNG được tự làm)

| # | việc | vì sao gấp |
|---|---|---|
| 1 | **`SC-12` / `VA-h12` — bản vá kế toán MT** (test 30/30, đã có vá, chờ ký) | mỗi ngày trôi thêm 1 ngày trễ; hiện **73 ngày**, và loại MT khỏi **83,1%** lượt chấm |
| 2 | Sửa `main.py:10491` + `:10511` — **đừng đổ model bị trần vào `wr_gate_filtered`** | admin panel đang trình bày chính sách CỐ Ý như "trượt cổng chất lượng" |
| 3 | Sửa mệnh đề `WHERE` ở `daily_evaluation.py:130-142` | **MB đang bị BÁO THẤP 23,4pp** — nặng hơn MT |
| 4 | Chuyển `LIMIT 270` ra TRƯỚC bộ lọc | chỉ số nhãn "WR Tổng" đang là cửa sổ trượt |
| 5 | Gỡ mâu thuẫn prompt (≥5 mệnh lệnh ngược chiều, gồm MB dòng 764 vs 1089) | `PRJ_PROMPT_CONTRADICTS` — model chọn câu nào là ngẫu nhiên |
| 6 | Dựng audit-trail cho `final_bundles` | hiện **không có bảng lịch sử**; bản v1 mất vĩnh viễn |
| 7 | Năm P0 hạ tầng của V11166 | vẫn nguyên |

### Ứng viên ĐĂNG KÝ TRƯỚC (RM-03) — chưa được phép kết luận

| ứng viên | số hiện có | n cần | ghi chú |
|---|---|---|---|
| `ranked[0]` MN là **phản-tín-hiệu** | 27,4% vs nền 43,1% · z = −2,72 · p ≈ 0,0065 | — | **mạnh nhất phiên**; nhưng là 1 test hậu nghiệm trong nhiều test |
| cơ chế `_v10640` specialist | +10,96pp gộp / dấu ĐỔI theo cửa sổ ở 3 miền | 191–491 ngày (có 36–73) | ngưỡng cũ V10917 đã tới hạn rà |
| MB `PARTIAL_SPENT` hơn `FRESH` | +12,6 điểm · z = +1,72 · **0/9 ô qua Holm** | 161 MB-ngày mỗi nhóm (5,4 tháng) | không được dùng làm căn cứ |
| anti-trap `FULL_SPENT` | **n = 63/90 — CẤM ĐỌC SỚM** | 90 | phép đo đã đăng ký 10/08, đang chạy |

### Đã đóng trong phiên này

MT «2 model hỏng» (bác bỏ) · «MB cùng bệnh với MT» (bác bỏ — `bt_gate` biến thiên, trần MT cố định) ·
«vòng lặp phản hồi day_governance → xếp hạng» (bác bỏ — không hàm nào đọc `day_governance`) ·
«ổ cắm V10883 đảo thứ tự» (bác bỏ — 0 dòng log) · «lane `rerun_post_mn` chết âm thầm» (bác bỏ —
tắt CÓ CHỦ ĐÍCH bởi `_V10766_SKIP_MT_REPREDICT=True`, đã ghi ở 5 chỗ) · «`/du-doan` công khai lộ
`model_count`» (bác bỏ — admin-only từ FU-438).

---

## §62 — NGUỒN BA LỚP

### `OWNER_SAID`
> *«Tiếp tục phân tích đánh giá kết quả live hôm nay, đơn model, total, prompt v.v... tất cả mọi thứ
> không soát vấn đề nào nha em»* — ~22:0x ngày 06/09/2026, IDE.

Chỉ thị đứng từ phiên trước còn hiệu lực: *«nếu kết luận là "không hơn ngẫu nhiên" thì phải nói
thẳng»*. **Báo cáo này nói thẳng.**

### `CODE_DID`
- `main.py:10225` → `:10231-10240` — `_v10640_official_perslice_override.get_override_bt()` lật
  bạch thủ MN **trước** khi chốt. Mô phỏng độc lập khớp **73/73 ngày**.
- `main.py:10379` — `main_selection_reason` là **chuỗi khoá cứng**; 71/71 bundle bị lật vẫn lưu
  `top1_reason` ghi con số **trước** khi lật.
- `main.py:10491` · `:10511` · `:487-489` — model bị trần `max_voters_cap` bị ghi vào
  `wr_gate_filtered`, rồi admin panel đọc lại khoá đó.
- `main.py:9838` — `_MAX_VOTERS_BY_REGION = {"MT": 13}` (V10752).
- `database.py:5050`, khối `:5074-5091` — `classify_day_status` chỉ đọc số thô `model_count`,
  **không có đường nào đọc lý do loại**.
- `daily_evaluation.py:130-142` — mệnh đề `WHERE` loại `EXCLUDE_PRIMARY`.
- `database.py:4648` (INSERT) · `:4933` (UPDATE) — **đường ghi duy nhất** vào `final_bundles`.
- `scheduler.py:41` — `AI_MODEL_HARD_TIMEOUT_SEC = 300`; log 05:26:02 ghi *"Combo Super → MN:
  TIMEOUT >300s; continue without blocking bundle"*.
- `_v10640_official_perslice_override.py` — `_SPECIALIST_MIN_HITRATE = 0.35` (< nền MN 0,431).
- VPS: PID `3370750` · `NRestarts 0` · `/api/health` 200 · đĩa 33% · load 0,08.

### `DOC_SAID`
- `docs/CURRENT_TRUTH_SSOT.md:68` — MT `EXCLUDE_PRIMARY` 72/90 = 80,0% vì kế toán trần V10752.
- `docs/CURRENT_TRUTH_SSOT.md:5850` · `docs/FOLLOW_UP_TRACKER.md:152` ·
  `docs/DAO_SAU_LICH_SU_20260821.md:21` — **nền MN 43%**, cả 3 miền dưới nền bao lô.
- `docs/FOLLOW_UP_TRACKER.md` — `SC-12` (VA-h12, test 30/30) trong **NHÓM A — đã có vá, chờ owner ký**.
- `CHANGELOG.md:151` — *«479 bundle LIVE 31,7% vs ngẫu nhiên 34,0%; 20/20 ô âm»*.

**LỆCH GIỮA BA LỚP — phải báo:**
1. `DOC_SAID` ≠ `CODE_DID`: `main_selection_reason` ghi *"max_ranked_score_after_gate_and_lane_weight"*
   trong khi `CODE_DID` cho thấy một override khác đã lật số. **Lỗ hổng provenance vẫn mở.**
2. `DOC_SAID` ≠ `CODE_DID`: admin panel gọi 2 model bị trần là "quality_filtered", `CODE_DID` ghi
   `reason=max_voters_cap`. **Chính chỗ này khiến lỗi sống 73 ngày.**
3. `OWNER_SAID` ≠ `CODE_DID`: owner duyệt trần MT-13 (25/06) **như một chính sách**, nhưng code kế
   toán nó **như một thất bại**. Đây là lệch giữa ý định owner và cách hệ ghi nhận.

---

TanPhatAI cần làm: ghi **`V11170`** — `governance_seq 485`, công khai bản này cùng `CONVERSATION_CONTEXT_V11170_20260906.md`. Ghi **NỀN NGẪU NHIÊN KHÔNG PHẢI 34,0% CHO MỌI MIỀN — nền riêng là MN 43,1% · MT 35,2% · MB 23,8%**; mượn 34,0% cho một miền là `RM-21_VIOLATION`. Ghi **NĂM ĐƯỜNG ĐO ĐỘC LẬP đều cho cùng kết luận: hệ KHÔNG hơn ngẫu nhiên ở bất kỳ miền nào, bất kỳ cửa sổ nào** (z=−0,99 · z=−2,72 · 9/9 ô dưới nền · hoán vị 2.000 lượt · Poisson-binomial p=0,0528) — **và cũng CHƯA đủ bằng chứng nói nó kém hơn** (RM-04). Ghi **cơ chế lật bạch thủ MN là `_v10640_official_perslice_override` chooser="specialist" tại `main.py:10231-10240`, KHÔNG phải anti-trap và KHÔNG phải PP-1** — mô phỏng độc lập khớp 73/73 ngày. Ghi **ngưỡng "chuyên gia" 0,35 THẤP HƠN nền MN 0,431 nên 70–77% roster đều đạt**, và **luật tầm thường «luôn lấy hạng 2» đạt 42,5% cao hơn specialist 38,4% (McNemar p=0,7111)**. Ghi **lợi ích phép lật ĐỔI DẤU theo cửa sổ: 30 ngày +22,29pp · 90 ngày −3,44pp · 180 ngày −4,83pp** — cấm trích riêng cửa sổ 30 ngày. Ghi **RÚT LẠI `RL-025`** cho ba mệnh đề của V11169. Ghi **lỗi kế toán MT nay đóng được NHÂN QUẢ**: MT lần cuối đạt ≥15 model là **25/06 — đúng ngày duyệt V10752**, 0/74 ngày kể từ đó, **71/74 ngày vẫn đủ 15 model chạy thật**, hai model bị cắt có `bt_rate` 33,30% so với ngưỡng 14%. Ghi **cơ chế khiến lỗi sống 73 ngày: `main.py:10491`/`:10511` đổ model bị trần vào `wr_gate_filtered`, `:487-489` đọc lại khoá đó cho admin panel**. Ghi **MB bị hại NHIỀU HƠN MT: mất 140 dòng, `top1_30` BÁO THẤP 23,4pp (13,3% hiển thị vs 36,7% thật)**. Ghi **chỉ số rolling-7 của MT đang hiển thị dữ liệu 19–25/06, trễ 73 ngày**. Ghi **nhãn DEGRADED loại MT khỏi 83,1% lượt chấm `combo-super`; chỉ 42% miền-ngày vào được phép chấm**. Ghi **phiên này TỰ NHẬN đã ĐỌC SỚM thí nghiệm đăng ký trước `anti_trap_shadow_v11058` (n=63/90, ngưỡng cấm đọc sớm)** — số đọc được KHÔNG dùng làm căn cứ; và **trục anti-trap từng đo tiến cứu ra −29,4 triệu/60 ngày rồi TẮT**. Ghi **prompt thật hôm nay 49.891–58.852 ký tự**, con số **46.583 là MB·official·07/08 KHÔNG gồm system prompt** — cùng đơn vị hôm nay là 47.753. Ghi **≥5 mệnh lệnh ngược chiều trong prompt**, gồm MB dòng 764 vs 1089 (`PRJ_PROMPT_CONTRADICTS`). Ghi **`final_bundles` KHÔNG có audit-trail; bản v1 mất vĩnh viễn**. Ghi **DB thật 785,8 MB · 153/253 bảng ghi hôm nay**. Ghi **`LIMIT 270` đặt sau bộ lọc khiến chỉ số nhãn "WR Tổng" thành cửa sổ trượt**. Ghi **hôm nay là NGÀY BÌNH THƯỜNG trên mọi thước kiểm được** (1/3 miền trúng là mode 14/30 ngày). **Code KHÔNG đi trước tài liệu** — 0 ghi production, 0 deploy, 0 restart, DB read-only. **Không mở Prompt 44. Không mở FU mới. Không mở Plan mới. Không promotion/retirement/cutover model nào.**
