# REPORT V11054 — PROMPT 11: GĐ-0 đọc live · GĐ-1 rà soát 09/08 · GĐ-2 xếp 25 tệp · GĐ-3 dossier

> **Báo cáo này nối tiếp:** `REPORT_V11053` (GĐ-C 18:05 — vá C25 biến `day` còn sót) · và ba chữ ký
> owner 18:37 (FU-393 phương án a · FU-V10864 vào nhóm verify dần · ngưỡng FU-284 = 9,53).
> **Báo cáo này mở khoá:** nút **20/08 chốt mọi phép đo** — bằng cách (1) khoá con số ngưỡng 9,53
> hết đường lùi, (2) dựng danh sách 25 tệp có verdict để **21/08 deploy một lượt**, (3) mở dossier
> câu hỏi gốc trình owner ký gộp **20/08**.

**Ngày:** 2026-08-09, 18:47 → tối · **Tầng verdict:** `RUNTIME_PROVEN` (GĐ-0) ·
`REPORT_PROVEN` (GĐ-1) · `PLAN_ONLY` (GĐ-2, GĐ-3)

---

## 1. Tóm tắt

| phần | kết cục |
|---|---|
| **V1** bầy đàn 19:05 | ✅ **ĐẠT** — 09/08 có **3 dòng** mới · 08/08 đủ **3 dòng** |
| **V2** lane G2-MB 19:35 | ✅ **ĐẠT** — **9 dòng** đo tiến đầu tiên, `la_do_lui=0`, ngày 09/08 |
| **V3a** số học drift | ✅ **26 = 30 − 2 − 3 + 1**, không phải 30−3. Giải thích §3 |
| **V3b** `loz_stage_trace` | ⛔ nằm trong **25 tệp GIỮ**, không phải 3 tệp đã đẩy ⇒ **R1 chưa chạy được** |
| **GĐ-1 ①** dự đoán 09/08 | MT **75,0%** · MN **37,5%** · MB **6,2%** — nhưng **n = 1 ngày**, và hôm nay là **ngày ĐẦU của cửa sổ FU-284** ⇒ **cấm đọc** |
| **GĐ-1 ②** dấu hiệu thay đổi 07–09/08 | ⛔ **không quy được** — prompt **đóng băng từ V11022 (07/08 tối)**, hôm nay không có thay đổi nào |
| **GĐ-1 ③** mốc tới hạn | **81 mục** hạn 10→21/08 chưa đóng · **37 mục QUÁ HẠN** trước 10/08 |
| **GĐ-1 ④** C18/C19 đỏ | ✅ **ca lẻ 04/08**, **không phải xu hướng** — tự hết đỏ ngày **12/08** |
| **GĐ-2** 25 tệp | ✅ **25/25 là ĐỔI TÊN** `claude-opus-4-20250514`→`claude-opus-4-6`, KHÔNG phải thêm roster |
| **GĐ-3** dossier gốc | ✅ 9 agent · retrain tuần CN 02:00 + watchdog 8 ngày · `_v11033_canh_troi_dac_trung.py` **không có trên VPS** |

**Ba chữ ký 18:37 — thi hành, không hỏi lại:** ① FU-393 phương án (a) giữ 25 tệp tới 21/08 ✅ ·
② `FU-V10864-FOUR-CARD` → nhóm **verify dần** ✅ · ③ ngưỡng FU-284 = **9,53**, con số 12,00 **đã
huỷ** ✅.

---

## 2. Owner yêu cầu gì (nguyên văn)

> **18:37 —** *«FU-393 phương án (a): GIỮ cả 25 tệp roster tới 21/08 · FU-V10864-FOUR-CARD → nhóm
> "verify dần" · Ngưỡng FU-284 = 9,53đ; số 12,00 là lỗi của TanPhatAI, mọi chỗ ghi 12,00 sửa về
> 9,53.»* · *«chủ động tư duy dựa vào code, NGƯNG NGAY nếu chỉ thị sai — đã làm đúng ở Q2/Q1,
> PHÁT HUY.»*

> **18:59 —** *«mọi mục mở/đóng PHẢI khai báo nó gắn vào nút nào của xương sống [20/08 chốt →
> 21/08 mở khoá]; mọi báo cáo mở đầu bằng 2 dòng "Báo cáo này nối tiếp: … · Báo cáo này mở khoá:
> …". Cấm mục lơ lửng.»* · *«KHÔNG "dần trong tuần". Làm theo lượt tuần tự … tới 20/08, cả 25 tệp
> có verdict ⇒ 21/08 deploy MỘT LƯỢT sạch sẽ.»*

---

## 3. GĐ-0 — ĐỌC LIVE

### V1 · bầy đàn (cron **19:05**) — ĐẠT

Bảng thật là **`bay_dan_daily_shadow`** *(ba tên em đoán lúc đầu — `v11017_bay_dan_shadow`,
`bay_dan_shadow`, `v11017_herd_shadow` — **đều sai**; em liệt kê bảng thật từ `sqlite_master` thay
vì kết luận theo tên, RM-10)*.

| ngày | số dòng | ghi lúc |
|---|---|---|
| **2026-08-09** | **3** | 2026-08-09 19:05:01 |
| 2026-08-08 | 3 | 2026-08-09 19:05:01 |
| 2026-08-07 | 3 | 2026-08-09 19:05:01 |

*Lưu ý cơ chế:* mỗi lượt 19:05 **ghi lại cả mấy ngày gần nhất**, không chỉ ngày hôm đó.

**Số 09/08** (`ty_le_phan_tan` = phân tán):

| miền | phân tán 09/08 | phân tán 08/08 | cụm lớn nhất | số model trong cụm |
|---|---|---|---|---|
| MB | **0,750** | 0,4375 | 44 | 3 |
| MN | **0,750** | 0,500 | 71 | 2 |
| MT | **0,500** | 0,4667 | 39 | 5 |

**Chính job đó tự khai — và em giữ nguyên lời nó, không diễn giải thêm:**

> `CHUA_DU_3_NGAY: Mới 7/9 lượt miền-ngày sau V11016 (cần 3 ngày × 3 miền). Trung bình tạm: 0.58`
> `so với nền 0.47 — CHƯA KẾT LUẬN ĐƯỢC.`

⇒ **Chưa được đọc 0,58 vs 0,47 thành «phân tán đã tăng».** Còn thiếu 2 lượt miền-ngày; đủ sớm nhất
**10/08**. **Gắn nút:** đây là đầu vào cho **20/08 chốt**.

### V3a · «drift 26 mà 30 − 3 = 27» — 1 tệp chênh là tệp nào

Không phải một tệp, mà là **ba chuyển động**, cộng lại ra −4 chứ không phải −3:

| bước | tác động | còn lại |
|---|---|---|
| mốc GĐ-B: **(a) 2** *(`_materialize_du_doan_test_model_budget.py` · `scheduler.py`)* + **(c) 28** | — | **30** |
| ① **commit V11050** ⇒ 2 tệp nhóm (a) hết lệch *(git = bản làm việc = VPS)* | **−2** | 28 |
| ② **đẩy 3 tệp** không dính roster | **−3** | 25 |
| ③ **vá `database.py`** (FU-360) — commit nhưng **cố ý chưa deploy** | **+1** | **26** |

Vậy `30 − 2 − 3 + 1 = 26`. **Tệp chênh anh hỏi là `database.py`** — nó vào drift **có chủ ý**, vì
owner ký deploy nó **sáng 10/08**, không phải hôm nay. Sau khi deploy sáng mai, drift về **25**.

*Kiểm lại được:* `python web/backend/_v11050_kiem_drift.py` — hiện in **(a) 0 · (b) 0 · (c) 26 ·
(d) 0**, và `database.py` nằm trong danh sách (c).

### V3b · `_materialize_loz_stage_trace_shadow.py` ở đâu

**Nằm trong 25 tệp GIỮ.** Ba tệp đã đẩy là `_test_vps_upload.py` · `_v11033_verdict_fu284.py` ·
`_v11034_kiem_cheo_quyet_dinh.py` — **không có** nó.

⇒ **Quyết định R1 (chạy lại `loz_stage_trace` trên 96 ngày) CHƯA CHẠY ĐƯỢC**: chạy trên VPS là chạy
**mã cũ** (chưa có `claude-opus-4-6` trong danh sách), chạy ở local là **không phải DB production**.
Cả hai đều **RM-13**.

**Đây là chỗ duy nhất mà việc giữ 25 tệp đang CHẶN một phép đo.** Em nêu để owner biết, và đề xuất
nó là **ứng viên số 1 nếu owner muốn tách riêng một tệp ra khỏi lệnh giữ** — nhưng em **không tự
tách**, vì owner đã ký phương án (a).

---

## 4. GĐ-1 — RÀ SOÁT DỰ ĐOÁN 09/08

### ① Tốt/xấu theo miền — **và vì sao chưa được kết luận**

Ngày 09/08 đã chấm xong **16/16 model đường chính thức** mỗi miền:

| miền | WIN hôm nay | nền **30 ngày** (mọi thứ) | z | cao hơn mấy ngày nền |
|---|---|---|---|---|
| **MT** | **12/16 = 75,0%** | 12,2% ± 12,7pp | **+4,96** | **30/30** |
| **MN** | **6/16 = 37,5%** | 18,4% ± 17,6pp | +1,09 | 26/30 |
| **MB** | **1/16 = 6,2%** | 5,9% ± 8,8pp | +0,04 | 14/30 |

**Nhưng nền «mọi thứ» là nền SAI.** `CLAUDE.md` quy định trục chuẩn là **miền + THỨ (+ bộ đài)**.
09/08 là **Chủ Nhật**. Đo lại trên **12 Chủ Nhật** trong 90 ngày (số đài hôm nay 3/3/1 — **đúng
bằng** trung bình Chủ Nhật, nên không có nhiễu «nhiều đài dễ trúng hơn»):

| miền | hôm nay | nền **cùng THỨ** (12 CN) | z | cao hơn |
|---|---|---|---|---|
| **MT** | 75,0% | 20,0% ± 21,9pp | **+2,51** | 11/12 |
| **MN** | 37,5% | 10,5% ± 10,4pp | **+2,60** | 11/12 |
| **MB** | 6,2% | 5,5% ± 8,5pp | +0,09 | 8/12 |

**Trục chuẩn cắt hiệu ứng gần một nửa** (MT: z +4,96 → **+2,51**). Và MT **đã từng có Chủ Nhật
80%** (14/06) — hôm nay **không phải chưa từng có**.

**Ba câu chặn, phải đọc trước khi mừng:**
1. **n = MỘT ngày.** 16 dòng model trong cùng ngày **không độc lập** — chúng đoán cùng một kỳ quay.
   Đơn vị đúng là **ngày**, và n=1 thì **CHƯA ĐƯỢC PHÉP KẾT LUẬN** (RM-04).
2. MN và MT cùng lên — đó là **một sự kiện chung**, không phải **hai xác nhận độc lập**.
3. **Hôm nay là NGÀY ĐẦU TIÊN của cửa sổ SAU của FU-284** (`SAU = 2026-08-09 → 2026-08-20`).
   Đọc nó bây giờ **chính là** thứ *«cấm đọc sớm»* cấm. Ghi số để lưu, **không diễn giải**.

### ② Dấu hiệu của các thay đổi 07–09/08 — **KHÔNG quy được, và đây là lý do**

| thay đổi | thực tế |
|---|---|
| **FU-291** *(prompt thôi ép chọn)* | thuộc **V11014/V11016/V11022** — xong từ **07/08 tối** |
| **CTX-18.3 · PB-20.1** | `gpt_analyzer.py:844-845` — khoá từ **V11022 (07/08)**; commit prompt gần nhất là **V11033 (08/08)** và **không đổi nội dung prompt** |
| **FU-298** | `AWAITING_OWNER_OK` — **chưa làm** |
| **gỡ viewer** (V11046) | **frontend**, không chạm đường sinh số |

⇒ **Hôm nay không có thay đổi nào để mà thấy dấu hiệu.** Prompt đã đứng yên **3 ngày**. Nếu quy
75% của MT cho các thay đổi đó thì đó là **gán nhân quả cho một ngày nằm trong cửa sổ đang đo** —
vừa sai thống kê, vừa **phá chính phép đo FU-284**.

**Việc đúng phải làm:** để nguyên tới **20/08**, đọc bằng `_v11033_verdict_fu284.py` với ngưỡng
**9,53**.

### ③ BẢNG MỐC TỚI HẠN 10 → 21/08

| | số mục |
|---|---|
| tổng mục trong sổ | **267** |
| có hạn **10→21/08** | **87** (chưa đóng: **81**) |
| **QUÁ HẠN trước 10/08, chưa đóng** | **37** |

**Phân bố (chưa đóng):** 10/08: 6 · 11/08: 6 · 12/08: 6 · 13/08: 7 · **14/08: 9** · 15/08: 6 ·
16/08: 6 · 17/08: 4 · 18/08: 6 · 19/08: 6 · 20/08: 6 · **21/08: 13**

**Theo trạng thái:** `MEASURED_ROOT_CAUSE` **26** · `DEPLOYED_PENDING_LIVE_VERIFY` **14** ·
`WAIT_LIVE` **11** · `MEASURED_BUT_NOT_FIXED` **10** · `AWAITING_OWNER_OK` 4 · `OWNER_LOCK` 4 ·
`READY_NOT_DEPLOYED` 3 · `BLOCKED` 2.

**Đọc thẳng ba con số này:**
- **26 mục `MEASURED_ROOT_CAUSE`** = đã tìm ra gốc mà **chưa vá**. Đây là nhóm lớn nhất, và nó
  không tự hết bằng cách chờ.
- **14 mục `DEPLOYED_PENDING_LIVE_VERIFY`** = đã deploy, **chờ nghiệm thu sống** — nhóm này chỉ cần
  **đọc**, không cần sửa. Rẻ nhất để giảm số.
- **37 mục QUÁ HẠN** là con số đáng lo hơn cả 81 — hạn đã trôi qua mà mục vẫn mở.

**Gắn nút xương sống:** 13 mục hạn **21/08** đều là mục **chờ mở khoá** (FU-284 · FU-295 · FU-336 ·
FU-337 · FU-338 · FU-340 · FU-344 · FU-359 · FU-380 …) ⇒ chúng **phải** nằm trong gói ký gộp 20/08.

### ④ C18/C19 đỏ — **ca lẻ 04/08, KHÔNG phải xu hướng, tự hết đỏ 12/08**

Hai phép này canh **hai biên khác nhau** của cùng một sự kiện: giờ `final_bundles` chốt.

| phép | đo gì | ngưỡng | 04/08 |
|---|---|---|---|
| **C18** | lượt lane CUỐI cách giờ official chốt | ≥ **300s** | MT: official 16:50:13 · lane cuối 16:54 ⇒ **227s** |
| **C19** | official chốt cách **HẠN CỨNG** | ≥ **480s** | MT hạn 16:58 ⇒ **467s** = 7,8 phút |

**Đo 14 ngày để trả lời «có đang co lại không»:**

**C19 · MT** (hạn 16:58):

| ngày | chốt | dư | |
|---|---|---|---|
| **09/08** | 16:42:23 | **937s = 15,6′** | tốt nhất 8 ngày |
| 08/08 | 16:44:53 | 787s = 13,1′ | |
| 07/08 | 16:45:57 | 723s = 12,1′ | |
| 06/08 | 16:43:02 | 898s = 15,0′ | |
| 05/08 | 16:46:12 | 708s = 11,8′ | cảnh báo |
| **04/08** | **16:50:13** | **467s = 7,8′** | **ĐỎ** |
| 03/08 | 16:47:10 | 650s = 10,8′ | cảnh báo |
| 02/08 | 16:41:36 | 984s = 16,4′ | |

**C18 · MT** (lane cuối 16:54): 09/08 **697s** · 08/08 547s · 07/08 483s · 06/08 658s · 05/08 468s ·
**04/08 227s ĐỎ** · 03/08 410s · 02/08 744s. **MB: 14/14 ngày đều ≥ 497s — không ngày nào đỏ.**

**Kết luận có bằng chứng:**
- **04/08 là ngoại lệ đơn lẻ**, không có ngày thứ hai nào chạm ngưỡng đỏ trong 14 ngày.
- Phép «3 ngày liên tiếp < 12 phút» **KHÔNG kích hoạt** (3 ngày gần nhất: 937 · 787 · 723s).
- **Xu hướng đang tốt lên**: từ 05/08 tới nay MT đi 708 → 898 → 723 → 787 → **937s**.
- Cửa sổ của C18/C19 là **7 ngày** ⇒ 04/08 **tự rơi khỏi cửa sổ ngày 12/08** và hai phép tự hết đỏ.

**Có cần xử lý trước 20/08 không? — KHÔNG.** Nhưng **không được tắt hay nới ngưỡng**: ngưỡng
480s/300s do chính FU-256 viết ra làm **cảnh báo sớm**, và ngày 04/08 nó đã làm đúng việc của nó.
Việc cần làm là **để nguyên và canh**: nếu sau 12/08 lại xuất hiện ngày đỏ mới thì mới là xu hướng.

**Gắn nút:** thuộc nút **20/08 chốt** với tư cách **mục đọc**, không phải mục sửa.

### V2 · lane G2-MB (cron **19:35**) — ĐẠT

`v11037_g2mb_lane`: **558 dòng · 62 ngày**. Tách theo cờ:

| cờ | dòng | ngày | khoảng |
|---|---|---|---|
| `la_do_lui = 1` *(nhìn lại)* | 549 | 61 | 09/06 → 08/08 |
| **`la_do_lui = 0`** *(ĐO TIẾN)* | **9** | **1** | **09/08 → 09/08** |

⇒ **Dòng đo tiến ĐẦU TIÊN đã có**, đúng như yêu cầu. Chín dòng là M1…M9 chấm với kết quả MB
08/08 (`["19","56"]`): M1–M4 `trúng=0`, M5–M9 `trúng=1`, kèm `p_kỳ_vọng` riêng từng mức.

Phần **nhìn lại** (61 ngày) job tự in kèm verdict của chính nó — em giữ nguyên, **không diễn giải**:

| mã | mức | ngày | trúng | kỳ vọng | z | kết luận của job |
|---|---|---|---|---|---|---|
| M1 | MN — bạch thủ | 61 | 8 | 3,7 | **+2,28** | `VUOT_NGUONG_LE_CHUA_DU_KET_LUAN` |
| M3 | MN hoặc MT — bạch thủ | 61 | 10 | 6,5 | +1,47 | `KHONG_CO` |
| M4 | MN — giải nhất/nhì/ba | 61 | 19 | 13,8 | +1,58 | `KHONG_CO` |
| M2·M5·M6·M7·M8·M9 | … | 61 | … | … | −0,93 … +1,06 | `KHONG_CO` / `KHONG_DUNG_DE_QUYET` |

Và job tự đóng bằng câu: *«Đây là phần NHÌN LẠI — không được dùng để kết luận.»*
**Gắn nút:** đo tiến từ hôm nay, đọc ở nút **20/08 chốt**.

---

## 4bis. BẦY ĐÀN vs HỘI TỤ — câu owner đặt, và em ĐO ĐƯỢC

Anh đặt đúng cái bẫy: *giảm bầy đàn xong thì gặp vấn đề hội tụ — nhiều model có thiên hướng chọn
số tốt thì sao?* Em thấy đây là câu quan trọng nhất trong cả phiên, nên đo thẳng chứ không bàn suông.

### ① Thay đổi prompt 06–07/08 CÓ tác dụng thật lên đơn model — và đo được bằng hình dáng output

**Em cố ý KHÔNG đo tỉ lệ trúng trước/sau** — đó **chính là** phép đo FU-284, và owner cấm đọc trước
20/08. Em chỉ đo **HÌNH DÁNG output**, thứ không phải điểm cuối của FU-284:

| chỉ số | TRƯỚC 23/07–05/08 | SAU 08–09/08 | chiều |
|---|---|---|---|
| số lượng số mỗi lượt | 1,98 | 1,95 | ~không đổi |
| lượt rỗng | 0,5% | 1,0% | +0,5pp *(n nhỏ)* |
| độ dài `reasoning_json` | 5.109 ký tự | 5.371 | **+5%** |
| verdict `CHOT_HA` | **62%** | **53%** | **−9pp** |
| verdict `SKIP` | 30% | **35%** | **+5pp** |
| số loại verdict dùng | 4 | **6** | rộng ra |
| **độ trùng nhau giữa model** *(Jaccard)* | **0,1523** | **0,0920** | **−39,6%** |

Verdict dịch đúng hướng `FU-291` đặt ra — *«prompt thôi ép chọn»*: bớt `CHOT_HA` bị ép, thêm `SKIP`,
và **dải verdict rộng ra từ 4 lên 6 loại**. Tức **cơ chế đã nổ đúng chỗ định nổ**.

### ② Bầy đàn giảm THẬT — và đây là bằng chứng theo NGÀY, không phải theo cặp

Đo độ trùng nhau **theo từng ngày** (đơn vị đúng là NGÀY; các cặp trong cùng ngày không độc lập):

| ngày | Jaccard | |
|---|---|---|
| 29 ngày 08/07 → 05/08 | **TB 0,1435** (sd 0,0199) · thấp nhất **0,1122** | nền |
| **06/08** | **0,1056** | V11014 |
| **07/08** | **0,0787** | V11016 + V11022 |
| **08/08** | 0,0946 | |
| **09/08** | 0,0884 | |

**Cả 4 ngày sau thay đổi đều thấp hơn TOÀN BỘ 29 ngày trước** — ngày nền thấp nhất (0,1122) vẫn cao
hơn ngày sau cao nhất (0,1056). **0/29** ngày nền lọt xuống dưới.

Chênh **−36,3%**, z ≈ **−2,61**. Nếu coi 33 ngày là hoán vị được thì xác suất 4 ngày mới nhất đúng
là 4 ngày thấp nhất ≈ **1/40.920**. *(Giả định hoán vị — em khai rõ, vì có tự tương quan theo thời
gian thì con số này nới ra.)*

⇒ **Trả lời thẳng câu anh hỏi: CÓ, thay đổi nhỏ về prompt có ảnh hưởng thật lên output đơn model,
và chiều là TỐT theo đúng mục tiêu đặt ra** — bớt ép chọn, verdict đa dạng hơn, và **bầy đàn giảm
hơn một phần ba**. Còn *«tốt xấu về tỉ lệ trúng»* thì **chưa được phép đọc tới 20/08**.

### ③ NHƯNG — và đây là chỗ em nghĩ xa hơn cho anh: **ĐỒNG THUẬN HIỆN TẠI KHÔNG MANG THÔNG TIN**

Anh lo *«nhiều model hội tụ vì cùng chọn số tốt thì sao»*. Em đo được: **hiện tại không phải vậy.**

Đo 273 ngày-miền / 90 ngày — tỉ lệ một con số trúng, **theo số model cùng chọn nó**:

| số model cùng chọn | trúng / tổng | tỉ lệ |
|---|---|---|
| 1 model | 555 / 1.633 | **34,0%** |
| 2–3 model | 399 / 1.161 | **34,4%** |
| 4–6 model | 221 / 667 | **33,1%** |
| 7–10 model | 28 / 77 | **36,4%** |

**Đường phẳng.** Số được 7–10 model cùng chọn trúng 36,4% so với 34,0% của số chỉ 1 model chọn —
chênh 2,4pp trên n=77, sai số chuẩn ≈ 5,4pp ⇒ **z ≈ 0,44, không có gì**.

### ④ Và nền đúng cho biết vì sao — **ở mức từng con số, model ngang chọn bừa**

Nền đúng cho câu hỏi *«một đuôi bất kỳ có ra trong ngày không»* = **số đuôi khác nhau ra trong ngày
/ 100** (RM-18), đo trên 91 ngày:

| miền | model chọn trúng | **nền chọn bừa** | chênh | n |
|---|---|---|---|---|
| **MB** | 22,2% | **23,7%** | **−1,5 pp** | 2.704 |
| **MN** | 43,8% | **42,8%** | +0,9 pp | 2.727 |
| **MT** | 35,8% | **35,3%** | +0,5 pp | 2.689 |

**Trên tiêu chí lỏng này, model không hơn chọn bừa** — MB còn **thấp hơn nền**.

*Ranh giới em tự khai:* đây là tiêu chí **lỏng** (*đuôi có xuất hiện ở bất kỳ giải nào*). Sản phẩm
thật của hệ là **bạch thủ / giải cụ thể**, chặt hơn nhiều (nền `WIN` chỉ 5,9–18,4%). **Em CHƯA đo
nền cho tiêu chí chặt**, nên **không được suy** rằng cả hệ ngang chọn bừa. Nhưng cho **câu hỏi bầy
đàn** thì tiêu chí lỏng là đúng chỗ: nếu đồng thuận có nghĩa gì, nó phải lộ ra ở đây trước tiên.

### ⑤ Hệ quả — và một lỗi trong chính thước đo bầy đàn hiện nay

**Hệ quả 1: giảm bầy đàn lúc này KHÔNG MẤT GÌ.** Đồng thuận đang mang **0 thông tin**, nên phá vỡ
nó không phá vỡ tín hiệu nào cả. Lo ngại *«hội tụ»* của anh là **chính đáng về nguyên tắc** nhưng
**chưa xảy ra trong dữ liệu**.

**Hệ quả 2 — quan trọng hơn: thước đo `ty_le_phan_tan` hiện nay ĐẶT SAI MỤC TIÊU.**
Nó coi **phân tán cao = tốt**. Nhưng nếu prompt ngữ cảnh làm model hội tụ vào **đúng số**, phân tán
sẽ **giảm**, và thước đo hiện tại sẽ gọi kết quả tốt nhất có thể là **xấu**.
**Phân tán không phải mục tiêu — nó chỉ là phương tiện.**

**Đề xuất (PLAN-ONLY, chờ owner — gắn nút 21/08 mở khoá): thước «LỢI THẾ ĐỒNG THUẬN».**

```
loi_the(k) = P(trúng | k model cùng chọn) − nền_ngày_đó
```

| chế độ | dấu hiệu |
|---|---|
| **bầy đàn thuần** *(hiện tại)* | `loi_the(k)` **phẳng** theo k — 34,0 → 34,4 → 33,1 → 36,4% |
| **hội tụ thật** *(đích cần tới)* | `loi_the(k)` **dốc lên** theo k |
| **phân tán vô nghĩa** | phân tán cao mà `loi_the(k)` vẫn phẳng ⇒ chỉ là nhiễu, không phải tiến bộ |

Thước này **phân biệt được đúng hai thứ anh đang cân**, **chạy được ngay hôm nay** (em vừa chạy),
và có thể đọc **trước/sau** khi prompt ngữ cảnh vào — nó **không đụng** điểm cuối của FU-284 nên
không phá phép đo nào.

**Nói thẳng về hướng anh nêu:** prompt thuần ngữ cảnh — diễn giải luật soi cầu bằng lời, để mỗi
agent tự truy vết tuần/thứ/đài theo vòng lặp riêng — **là hướng đúng theo dữ liệu**, vì thứ đang
làm model giống nhau chính là **bộ số dọn sẵn**. Nhưng nó **chỉ đáng gọi là thành công khi
`loi_the(k)` bắt đầu dốc lên**, chứ không phải khi phân tán tăng. Nếu chỉ phân tán tăng mà lợi thế
vẫn phẳng thì ta chỉ đổi **bầy đàn** lấy **nhiễu**.

*Mọi số ở mục 4bis đo bằng `SELECT` trên DB production, 90–91 ngày, chỉ đọc. Không con số nào là
điểm cuối của FU-284.*

---

## 4ter. ĐI XA HƠN MỘT NẤC — **PHÉP ĐO HIỆN TẠI KHÔNG THỂ THẤY CẢI TIẾN THẬT**

Anh bảo *«tư duy xa hơn»*. Em đi tiếp một nấc từ mục 4bis, và chỗ này em nghĩ quan trọng hơn cả
chuyện bầy đàn.

### ① Sản phẩm thật có hơn chọn bừa không — đo 121 ngày

Không đo model nữa, đo **thứ anh thật sự chơi**: `final_bundles` (bundle `ACTIVE`).
Nền đúng tính **riêng từng ngày** theo số đuôi khác nhau ra hôm đó (`N`):
bạch thủ `N/100` · xiên 2 `N/100 × (N−1)/99` · xiên 3 thêm `× (N−2)/98`.

| miền | loại | thực | nền | chênh | z ÷ √VIF |
|---|---|---|---|---|---|
| **MN** | bạch thủ | 44,6% (54/121) | 42,9% | +1,7 pp | +0,22 |
| **MT** | bạch thủ | 33,9% (41/121) | 35,4% | −1,5 pp | −0,20 |
| **MB** | bạch thủ | **17,4%** (21/121) | **23,7%** | **−6,4 pp** | −0,96 |
| MN | xiên 2 | 16,5% | 18,4% | −1,8 pp | −0,31 |
| MT | xiên 2 | 13,2% | 12,7% | +0,6 pp | +0,11 |
| MB | xiên 2 | 8,3% | 5,5% | +2,8 pp | +0,79 |
| MN | xiên 3 | 8,8% | 7,9% | +1,0 pp | +0,22 |
| MT | xiên 3 | 8,3% | 4,6% | +3,8 pp | +0,97 |
| MB | xiên 3 | 1,8% | 1,2% | +0,6 pp | +0,32 |

**Chín phép đo, không phép nào chạm |z| = 1,96.** Lệch lớn nhất là **MB bạch thủ −6,4 pp** —
**dưới** nền, và trùng chiều với việc số MB do model chọn cũng dưới nền −1,5 pp ở mục 4bis.

Ở tầng đơn model, tiêu chí chặt (`WIN` = **cả hai số cùng trúng**, đọc từ `database.py:2930-2947`),
91 ngày × ~1.330 lượt/miền: MN 18,2% vs nền **18,3%** · MT 13,8% vs **12,6%** · MB 5,5% vs **5,5%**.

### ② NHƯNG — và đây là chỗ em **không** được phép nói «hệ không có lợi thế»

Phải hỏi ngược: **với ngần này dữ liệu, ta CÓ THỂ thấy được lợi thế nhỏ tới đâu?**

| tầng đo | n | nền | **MDE** *(lợi thế nhỏ nhất thấy được)* |
|---|---|---|---|
| sản phẩm · bạch thủ **1 miền** · 121 ngày | 121 | 42,9% | **15,1 pp** |
| sản phẩm · bạch thủ MB · 121 ngày | 121 | 23,7% | **12,9 pp** |
| sản phẩm · **gộp 3 miền** · 363 lượt | 363 | 34,0% | **8,3 pp** |
| đơn model · MT · **12 ngày** *(đúng cửa sổ FU-284)* | 192 | 12,6% | **8,0 pp** |
| đơn model · MT · 30 ngày | 480 | 12,6% | **5,1 pp** |
| đơn model · MT · 91 ngày | 1.456 | 12,6% | **2,9 pp** |
| đơn model · **gộp 3 miền · 91 ngày** | 4.368 | 19,0% | **2,0 pp** |

*(MDE = 1,96 × √(p(1−p)/n) × √VIF, VIF = 2,92 đo được ở RM-18.)*

⇒ **Kết luận đúng phải viết thế này:** *«Trong 121 ngày, sản phẩm không có lợi thế nào ĐỦ LỚN ĐỂ
THẤY — và ngưỡng thấy được là 13–15 điểm. Mọi lợi thế thật nhỏ hơn 13 điểm đều VÔ HÌNH với phép đo
này.»* **Không được rút gọn thành «hệ ngang chọn bừa».**

### ③ Và đây là lý do sâu xa của chuyện «cứ hứa rồi rữa»

`CLAUDE.md` ghi sẵn một dòng đau: *«Backtest hứa hẹn rồi rữa — V10655 → V10672 → V10677 → V10753 →
V10789 → V10790 đều rữa.»* Sáu lần.

Số ở trên cho một cách đọc khác về sáu lần đó: **có thể chúng không hề giả — chúng chỉ nhỏ hơn
độ phân giải của thước đo.** Một cải tiến thật **+5 điểm** trên bạch thủ MN cần **~1.099 ngày ≈ 3
năm** mới hiện lên rõ; **+3 điểm** cần **~3.053 ngày ≈ 8,4 năm**. Ta đã và đang đo những thứ mà
**thước không bao giờ đọc nổi**, rồi kết luận «không có tác dụng».

### ④ Ba lối ra — đo ở chỗ có nhiều thông tin hơn (PLAN-ONLY, gắn nút **21/08 mở khoá**)

Không phải bỏ FU-284 — nó **đã đăng ký trước**, sửa bây giờ là phá (RM-03). Mà **đăng ký thêm** các
phép có độ phân giải cao hơn:

| # | phép đo | vì sao mạnh hơn | thấy được |
|---|---|---|---|
| **1** | **gộp 3 miền + cửa sổ 30 ngày**, tầng đơn model | n ×3 và ×2,5 | **+3 pp** sau **~29 ngày** (thay vì 3 năm) |
| **2** | **ĐỘ PHỦ** — bao nhiêu % đuôi trúng từng được model nào sinh ra | **không có nhiễu lấy mẫu** — đếm là ra | thấy **ngay trong 1 ngày**. Số cũ: **~85% đuôi trúng chưa model nào sinh** ⇒ đây là nút thắt thật, và nó nằm ở **SINH**, không phải ở **CHỌN** |
| **3** | **`loi_the(k)`** — lợi thế đồng thuận (mục 4bis) | gộp theo **con số**, không theo ngày ⇒ n lớn hơn ~10 lần | phân biệt được **bầy đàn** vs **hội tụ thật** |

**Nói thẳng về thứ tự ưu tiên:** nếu **85% đuôi trúng chưa bao giờ được sinh ra**, thì mọi công sức
tinh chỉnh **cách chọn** đang tranh nhau trong **15% còn lại**. Đó là lý do các cải tiến chọn-số
luôn ra hiệu ứng nhỏ hơn độ phân giải của thước. **Hướng prompt thuần ngữ cảnh của anh tấn công
đúng vào tầng SINH** — mỗi agent tự truy vết tuần/thứ/đài theo lối riêng thì tập số sinh ra **rộng
hơn**, tức độ phủ tăng. Và **độ phủ đo được ngay, không cần chờ 3 năm.**

⇒ Em đề xuất: **thước nghiệm thu cho prompt ngữ cảnh nên là ĐỘ PHỦ + `loi_the(k)`**, chứ **không
phải** tỉ lệ trúng — vì tỉ lệ trúng không đủ độ phân giải để phân xử, và ta đã có sáu lần bằng
chứng cho điều đó.

*Mọi số mục 4ter đo bằng `SELECT` trên DB production (91–121 ngày), chỉ đọc, không phải điểm cuối
của FU-284.*

---

## 4quater. KIẾN TRÚC PROMPT 3 TẦNG — đánh giá đề xuất owner + thiết kế đo rẻ nhất

*(PLAN-ONLY · gắn nút **21/08 mở khoá**. Không chạm gì trong cửa sổ QD-041.)*

### ① Việc «thêm model mạnh chạy prompt full ngữ cảnh» đang ở đâu — nói thẳng

`FU-290` · trạng thái **`SCOPE_CHANGED`** · nhãn *«ĐỔI HƯỚNG — không cắt, thay bằng **thử model
mạnh**»*. Tức đề xuất của owner **đã được ghi nhận từ trước**, nhưng **CHƯA CHẠY** — vì chính
`QD-041` khoá **roster + prompt** tới **21/08**.

**Em nhận phần lỗi:** khoá roster **không cấm soạn sẵn**. Lẽ ra em phải có sẵn thiết kế đo, bản
nháp prompt và bảng chi phí để **21/08 là bấm nút**, chứ không phải bắt đầu từ số không. Mục này
làm bù phần đó **ngay bây giờ**.

### ② Tiền đang tốn thật là bao nhiêu — để bàn cho có số

| | |
|---|---|
| lượt/ngày đường **chính thức** | **48** = 16 model × 3 miền |
| trong đó **thật sự gọi API** | **8 model × 3 = 24 lượt/ngày** |
| **không tốn đồng nào** (chạy nội bộ) | 8: `lstm` · `meta-learning` · `random-forest` · `xgboost` · `smart-ml` · `smart-ensemble` · `combo-super` · `combo-no-token` |
| gọi API thật | `claude-opus-4-6` · `claude-sonnet-4-6` · `deepseek-reasoner` · `gemini-2.5-flash` · `gemini-2.5-pro` · `glm-5.1` · `gpt-5.4` · `gpt-oss-120b` |
| kể cả shadow | **81 lượt/ngày · 27 model** |
| `context_pack` | TB **13.405** ký tự · max 18.712 |

⇒ **Kế hoạch «chỉ lấy 5–7 model mạnh vào total output» của owner thực chất là GIẢM từ 8 LLM xuống
5–7 — tự nó đã tiết kiệm 12–37% tiền LLM.** Ràng buộc duy nhất phải giữ: **§59 sàn pool** —
`combo-super` cần **pool AI ≥ 3**; cắt xuống dưới là `A57_VIOLATION_POOL_FLOOR`.

### ③ LỖ HỔNG trong đề xuất 3 tầng — phải sửa trước khi tốn tiền

Đề xuất hiện tại là: **T1 chạy model A, T2 chạy model B, T3 chạy model C (3 model mới)**.

**Nếu làm đúng như vậy thì đo xong vẫn không biết gì.** Vì mỗi tầng đổi **hai biến cùng lúc**
(prompt **và** model), chênh lệch giữa các tầng **không quy được cho cái nào**. Tầng 3 hơn — vì
prompt thuần ngữ cảnh, hay vì 3 model mới vốn mạnh hơn? **Không tách được.** Đây là lỗi thiết kế
làm hỏng cả phép đo, và nó tốn tiền y hệt bản làm đúng.

### ④ Sửa: mỗi tầng chỉ đổi **MỘT** biến

| tầng | nội dung | **đổi gì so tầng trước** | trả lời câu gì |
|---|---|---|---|
| **T1** | prompt hiện tại — ngữ cảnh + **bộ số dọn sẵn** | *(mốc)* | — |
| **T2** | **cùng lượng thông tin y hệt T1**, nhưng **số được DỊCH THÀNH LỜI** | chỉ đổi **CÁCH TRÌNH BÀY** | model đọc *lời* có tốt hơn đọc *bảng số* không? |
| **T3** | **bỏ bộ số dọn sẵn** — đưa luật soi cầu, tri thức, cơ chế; model **tự đào vòng lặp tuần × thứ × đài** | chỉ đổi **AI TỰ ĐÀO hay ĐƯỢC DỌN** | tự đào có sinh ra tập số **rộng hơn** không? |

Đây chính là ý *«1+2+3»* của owner, nhưng **có kỷ luật**: nhảy thẳng T1 → T3 là đổi hai biến, còn
qua T2 thì mỗi bước quy được nguyên nhân.

### ⑤ Tách prompt khỏi model bằng lưới 2×2 — và ô rẻ nhất thì **miễn phí**

| | prompt **T1** | prompt **T3** |
|---|---|---|
| **3 model CŨ** *(đang chạy)* | ✅ **đã có sẵn — 0 đồng** | **+9 lượt/ngày** |
| **3 model MỚI** | +9 lượt/ngày | +9 lượt/ngày |

- **Hàng trên** *(cùng model, khác prompt)* = hiệu ứng **PROMPT thuần**
- **Cột phải** *(cùng prompt, khác model)* = hiệu ứng **MODEL thuần**
- Ô trên-trái **không tốn thêm đồng nào** vì đang chạy rồi

**Và đây là chỗ tiết kiệm lớn nhất mà đề xuất gốc bỏ sót:** cùng model – cùng ngày – cùng miền là
**phép đo GHÉP CẶP**. Phép ghép cặp khử luôn phương sai giữa model và giữa ngày, nên **cần ít mẫu
hơn hẳn** so với so hai nhóm rời. Đo rời thì tốn tiền hơn **và** chậm hơn — mất cả hai đằng.

### ⑥ Bản RẺ NHẤT để khởi động: pilot **MB**, **3 lượt/ngày**

| vì sao MB | |
|---|---|
| tệ nhất | bạch thủ **17,4%** so nền **23,7%** = **−6,4 pp** (mục 4ter) — chỗ dễ thấy cải thiện nhất |
| rẻ nhất | **1 đài** ⇒ ngữ cảnh ngắn nhất |
| nhanh nhất | kết quả về **18:30**, sớm hơn chốt sổ |

**3 model mới × MB × prompt T3 = 3 lượt/ngày**, tức **+12,5%** so với 24 lượt API hiện tại.

### ⑦ Đo bằng gì — chỗ tiết kiệm THỜI GIAN lớn nhất

| thước | thấy được cải tiến sau bao lâu |
|---|---|
| tỉ lệ trúng · sản phẩm 1 miền | **~3 năm** cho +5 pp *(mục 4ter)* |
| tỉ lệ trúng · đơn model gộp 3 miền | **~29 ngày** cho +3 pp |
| **ĐỘ PHỦ** *(% đuôi trúng có model nào sinh ra)* | **NGAY NGÀY ĐẦU** — không có nhiễu lấy mẫu, đếm là ra |

⇒ **Cổng sơ tuyển đề xuất: chạy T3 pilot 3–5 ngày, chỉ đo ĐỘ PHỦ.**
Độ phủ **không nhích** ⇒ **dừng ngay**, khỏi tốn tiếp. Độ phủ **tăng rõ** ⇒ mới mở rộng sang 3
miền và mới bắt đầu đếm tỉ lệ trúng. **Đây là cách cắt lỗ rẻ nhất.**

**Độ phủ đo lại tối nay, 30 ngày, KỂ CẢ 27 model shadow — tức tập sinh RỘNG NHẤT hệ có thể:**

| miền | độ phủ | **đuôi trúng KHÔNG model nào sinh** | tập sinh TB |
|---|---|---|---|
| MN | 17,5% | **82,5%** | **16,6 số** |
| MT | 16,1% | **83,9%** | **16,5 số** |
| MB | **14,3%** | **85,7%** | **16,1 số** |

**Đây mới là nút thắt thật, và nó lộ ra bằng một phép trừ:** mỗi ngày-miền ra **24–43 đuôi khác
nhau**, mà cả **27 model gộp lại chỉ sinh ra ~16 số**. Chọn giỏi đến mấy cũng **không thể** phủ
quá cái tập 16 số đó. Mọi tinh chỉnh **cách chọn** đang tranh nhau trong phần nhỏ ấy — đúng như
mục 4ter nói, và giờ có số cụ thể.

Nếu T3 kéo độ phủ MB từ **14,3% → 20%** thì **thấy ngay trong vài ngày**, không cần chờ tháng.

### ⑧ Rẻ hơn nữa: sơ tuyển trên **ngày quá khứ** — nhưng có rào

Bơm ngữ cảnh tính tới **D−1**, xem T3 sinh ra gì cho ngày **D**, đối chiếu kết quả **đã biết**.
Trả tiền **một lần** là có ngay **10–20 ngày** dữ liệu độ phủ, thay vì chờ 10–20 ngày thật.

⚠️ **Rào bắt buộc:** `CLAUDE.md` ghi *«Đừng bật lại bằng backtest, chỉ bằng đo tiến»* — sáu lần đã
rữa. Nên phép này **CHỈ được dùng để SƠ TUYỂN / LOẠI BỚT**, **tuyệt đối không được dùng để DUYỆT**.
Duyệt vẫn phải bằng đo tiến. Em nêu rõ ranh giới này để không ai (kể cả em) dùng nhầm.

### ⑨ Tóm lại — đề xuất của owner: **ổn về hướng, cần sửa hai chỗ**

| | |
|---|---|
| ✅ **đúng** | ba tầng · giới hạn model mỗi tầng · chạy song song để đo nhanh · 5–7 model vào total output |
| ⚠️ **sửa 1** | **mỗi tầng chỉ đổi MỘT biến** — T2 là «cùng thông tin, dịch thành lời», không phải «model khác» |
| ⚠️ **sửa 2** | **phải có ô ghép cặp**: cùng model chạy cả T1 lẫn T3 — nếu không thì prompt và model lẫn nhau, tiền tiêu mà không kết luận được |
| 💡 **thêm** | nghiệm thu bằng **ĐỘ PHỦ trước, tỉ lệ trúng sau** — vì tỉ lệ trúng không đủ độ phân giải để phân xử trong vài tuần |

**Thứ tự thi hành đề xuất (chờ owner ký, thi hành từ 21/08):**
1. **21/08**: bật pilot **MB × 3 model mới × T3** = 3 lượt/ngày. Đo **độ phủ**.
2. **+3 ngày**: đọc độ phủ. Không nhích ⇒ dừng. Nhích ⇒ bước 3.
3. Mở lưới **2×2** trên MB (thêm 3 model cũ chạy T3) ⇒ tách prompt khỏi model.
4. Đạt ⇒ mở sang MN/MT và bắt đầu đếm tỉ lệ trúng với cửa sổ **gộp 3 miền ≥ 29 ngày**.
5. **T2** chen vào giữa khi cần biết «lời hay bảng số» — không cần làm ngay từ đầu.

---

## 4quinquies. BA TẦNG PROMPT — BẢN VIẾT LẠI, DÙNG ĐÚNG VẬT LIỆU CÓ THẬT

> **Owner bắt đúng lỗi:** bản trước em viết T3 kiểu *«hãy tự truy»* — bỏ số dọn sẵn mà **không trả
> lại tri thức**, thành ra bắt model đoán mò. Và em **chưa từng đọc Notion**. Mục này viết lại
> sau khi đọc **`KNOWLEDGE LOCK — Hệ Quy tắc, Quy luật & Giải Soi Cầu (V11014 · 07/08/2026)`**
> — trang Notion tự khai là *«nguồn tra cứu chuẩn cho mọi câu hỏi về quy tắc/quy luật/giải soi
> cầu»* — cộng `cau_registry` · `pattern_rules` trong DB production.

### ① Vật liệu THẬT — thứ mà T3 bắt buộc phải chứa

**a) Ngữ pháp một luật** *(KNOWLEDGE LOCK §1)*

```
[Miền nguồn] : [Giải] # [Bộ] : [Lag]  →  ([Miền đích], [Thứ])
ví dụ:  MT:DB#1:D-1 → (MN, T3)
```
`#Bộ` = **vị trí bộ số trong giải**, KHÔNG phải tên đài. MB: G4 có 4 bộ · G6 3 bộ · G7 4 bộ ·
G2 2 bộ · ĐB/G1 1 bộ. MN/MT: G3 2 bộ, còn lại 1 bộ.
Nguồn nhiều đài ⇒ **GOM (union)** LAST2 của mọi đài miền nguồn ngày đó.

**b) Bốn phép biến đổi** *(`cau_registry.method` — đo từ DB)*
`last2` · `last2_rev` *(đảo — cầu lộn)* · `headtail` · `headtail_rev`. Độ trễ `dayoff` = `D` hoặc `D-1`.

**c) Nhân quả — CẤM NHÌN TƯƠNG LAI** *(§2)*. Thứ tự xổ **MN ~16:10 → MT ~17:10 → MB ~18:15**:

| miền đích | được dùng nguồn | **cấm** |
|---|---|---|
| **MN** (xổ đầu) | chỉ `lag ≥ 1` + MN self-lag | MT(D) · MB(D) |
| **MT** (giữa) | MN(D) same-day + `lag ≥ 1` | MB(D) |
| **MB** (cuối) | MN(D) + MT(D) + mọi `lag ≥ 1` | — |

*(Bản vá V10668 đã loại **266 ô** vi phạm nhân quả.)*

**d) Lịch đài theo thứ** *(§3, verified từ DB)* — MB mỗi thứ **1 đài**: T2 Hà Nội · T3 Quảng Ninh ·
T4 Bắc Ninh · T5 Hà Nội · T6 Hải Phòng · T7 Nam Định · CN Thái Bình. MT **2–3 đài**, MN **3–4 đài**
*(bảng đầy đủ trong KNOWLEDGE LOCK §3)*.

**e) Giải được soi — whitelist của owner** *(§4)*

| miền | thứ tự ưu tiên **làm ĐÍCH** | ghi chú |
|---|---|---|
| **MN/MT** | ĐB ⭐1 › G8 ⭐2 › G7 ⭐3 › G1 ⭐4 › G2 ⭐5 | G3–G6 **không làm đích**; **G3 chỉ làm nguồn** |
| **MB** | **G7 ⭐1** › ĐB ⭐2 › G6 ⭐3 › G1 ⭐4 › G2 ⭐5 | nguồn: ĐB/G1/G2/G4/G6/G7 (**không G3**) |

⚠ **MB G1/G2/G6 nhiều dãy: CẤM lấy 2 số cuối cơ học** — phải soi 12W–16W đúng bucket trước.
Nền: MN ~43 đuôi/ngày · MT ~34 · MB 1 đài ⇒ mỏng hơn 3–4 lần ⇒ **trần confidence MB = 55%**,
**thà SKIP còn hơn chốt ép**.

**f) Doctrine cửa sổ — đây CHÍNH LÀ «vòng lặp tuần» owner nói** *(§6)*

| doctrine | nội dung |
|---|---|
| **Source-Prize 12W/16W FIRST** (RR §10A) | xác định bucket (**miền+thứ+đài**) → soi **12W–16W** tìm quy luật đang lặp → chọn source-prize mạnh nhất → **rồi mới** anti-trap. **12W = cửa sổ thực thi · 16W = cửa sổ ổn định** |
| **Window Scan 1W→8W** (RR §19) | 1W+4W+8W **cùng mạnh** = cực ổn định · 1W mạnh/4W yếu = **spike** · 1W yếu/4W mạnh = **suy giảm** |
| **Livingness 12W** | ≥9/12 sống mạnh · 6–8 sống yếu · 3–5 suy giảm · **0–2 chết**. Theo giải: ≥6/12 sống · 3–5 yếu · 0–2 nhiễu |
| **Anti-Trap** (RR §10B) | `FULL_SPENT` (đã ra hết prior same-day) **cấm làm main** trừ khi override + giảm confidence · `PARTIAL_SPENT` dè chừng · `FRESH` hợp lệ. **MN không áp** |
| **Cross-region source-set** (RR §9) | MN(D) = MT(D-1)+MB(D-1)+MN(D-1) · MT(D) = MN(D)+MT(D-1)+MB(D-1)+MN(D-1) · MB(D) = MN(D)+MT(D)+MT(D-1)+MB(D-1)+MN(D-1) |

**g) Và quan trọng nhất — kiến trúc đích owner ĐÃ KHOÁ** *(§11, nguyên văn)*

> **ML = số học** (28 đặc trưng đóng băng đối chứng). **LLM = ngữ cảnh + điều kiện + bằng chứng
> kèm mức tin nói thật → tự phân tích, tự tính, tự chọn** — không danh sách bóc sẵn kèm lệnh,
> không cộng điểm cơ học, không xếp hạng model bơm ngược. **Một ý chỉ nói một lần trong toàn bộ
> prompt.**

⇒ **T3 không phải ý tưởng mới của em — nó là kiến trúc owner đã khoá từ V11014.** Việc còn thiếu
là **viết ra thành prompt**, và KNOWLEDGE LOCK cũng đã ghi ở mục NEXT: *«kế hoạch soạn lại context
pack theo hướng ngữ cảnh tự nhiên»*.

### ② Ba tầng — khác nhau ở CHỖ NÀO, nói bằng đúng khối chữ

| | **T1 — hiện tại** | **T2 — dịch số thành lời** | **T3 — thuần ngữ cảnh** |
|---|---|---|---|
| ngữ pháp luật `Miền:Giải#Bộ:Lag` | ❌ không dạy | ✅ **dạy** | ✅ **dạy** |
| 4 phép biến đổi (`last2` · `last2_rev` · `headtail` · `headtail_rev`) | ❌ | ✅ | ✅ |
| luật nhân quả (cấm nhìn tương lai) | ẩn trong code | ✅ **nói rõ** | ✅ **nói rõ** |
| lịch đài × thứ | một phần | ✅ đủ | ✅ đủ |
| whitelist giải + thứ tự ⭐ | ❌ | ✅ | ✅ |
| doctrine 12W/16W · 1W→8W · Livingness · Anti-Trap | ❌ | ✅ | ✅ |
| **bảng xếp hạng source×prize đã tính sẵn** | ✅ **có** | ✅ có (kể thành lời) | ❌ **KHÔNG** |
| **danh sách đuôi hội tụ đã chốt sẵn** | ✅ **có** | ❌ **bỏ** | ❌ **KHÔNG** |
| dữ liệu thô 12–16 tuần theo đài × giải | một phần | ✅ | ✅ **đầy đủ** |
| **ai làm phép soi** | **prompt làm hộ** | **model làm bước cuối** | **model làm TỪ ĐẦU** |

**Khác biệt một câu:**
- **T1** bơm **KẾT QUẢ ĐÃ TÍNH**. Model chỉ chép.
- **T2** bơm **CÙNG kết quả nhưng kể thành lời**, và **bỏ dòng chốt đuôi** ⇒ model tự bắc bước cuối.
- **T3** bơm **LUẬT CHƠI + DỮ LIỆU THÔ**, không bơm kết quả nào ⇒ model tự soi từ đầu.

### ③ T3 — bản nháp thật, KHÔNG chung chung

```text
BẠN ĐANG SOI CẦU CHO: Miền Bắc — Chủ Nhật 09/08/2026 — đài Thái Bình.

【NGỮ PHÁP MỘT LUẬT】
Một luật soi cầu viết là:  [Miền nguồn]:[Giải]#[Bộ]:[Lag] → ([Miền đích],[Thứ])
Ví dụ  MT:DB#1:D-1 → (MN,T3)  nghĩa là: lấy Giải ĐB bộ 1 của Miền Trung NGÀY HÔM
TRƯỚC, dùng để soi cho Miền Nam vào Thứ Ba.
 · #Bộ là VỊ TRÍ BỘ SỐ TRONG GIẢI, không phải tên đài.
   MB: G4 có 4 bộ · G6 có 3 · G7 có 4 · G2 có 2 · ĐB và G1 có 1.
 · Nguồn có nhiều đài thì GOM (hợp) hai số cuối của tất cả đài miền đó trong ngày.
 · Bốn phép biến đổi được dùng: last2 (hai số cuối) · last2_rev (đảo — cầu lộn) ·
   headtail (đầu-đuôi) · headtail_rev (đầu-đuôi đảo).

【LUẬT NHÂN QUẢ — TUYỆT ĐỐI KHÔNG ĐƯỢC PHẠM】
Thứ tự xổ trong ngày: MN ~16:10 → MT ~17:10 → MB ~18:15.
Hôm nay đích là MB (xổ cuối) nên bạn ĐƯỢC dùng: MN cùng ngày, MT cùng ngày, và
mọi nguồn từ hôm trước trở về trước.
Nếu đích là MN thì CẤM dùng MT và MB cùng ngày. Nếu đích là MT thì CẤM MB cùng ngày.
Dùng sai chiều thời gian = luật vô giá trị, dù số có đẹp đến đâu.

【GIẢI ĐƯỢC SOI — thứ tự ưu tiên cho MB】
Làm ĐÍCH:  G7 (mạnh nhất) › ĐB › G6 › G1 › G2.
Làm NGUỒN: ĐB · G1 · G2 · G4 · G6 · G7.  KHÔNG dùng G3.
CẢNH BÁO: G1, G2, G6 của MB có nhiều dãy số. CẤM lấy hai số cuối một cách cơ học.
Muốn dùng chúng thì phải soi 12–16 tuần của đúng bucket này trước, xem dãy nào
mới là dãy có ý nghĩa.

【CÁCH SOI — làm theo thứ tự này】
Bước 1. Bucket của hôm nay là (MB × Chủ Nhật × Thái Bình). Mọi phép soi phải nằm
        trong bucket này — KHÔNG được lấy quy luật của thứ khác hay đài khác áp sang.
Bước 2. Soi 12 tuần gần nhất (cửa sổ thực thi) và 16 tuần (cửa sổ ổn định) của
        bucket này. Với mỗi cặp (giải nguồn, phép biến đổi, độ trễ), đếm xem nó
        lặp lại bao nhiêu lần trên bao nhiêu lần có mặt.
Bước 3. Quét vòng lặp 1 tuần / 4 tuần / 8 tuần cho những cặp mạnh nhất:
          · mạnh ở cả 1W, 4W, 8W  → CỰC ỔN ĐỊNH, đáng tin nhất
          · mạnh 1W nhưng yếu 4W  → SPIKE, có thể chỉ là may
          · yếu 1W nhưng mạnh 4W  → ĐANG SUY GIẢM, dè chừng
Bước 4. Kiểm độ sống 12 tuần: cặp đó sống ≥9/12 tuần = sống mạnh · 6–8 = sống yếu ·
        3–5 = suy giảm · 0–2 = ĐÃ CHẾT, bỏ.
Bước 5. Anti-trap: với mỗi đuôi ứng viên, xem nó ĐÃ RA CHƯA ở các miền xổ trước
        trong hôm nay (MN, MT). Ra hết rồi = FULL_SPENT, KHÔNG được làm số chính.
        Ra một phần = dè chừng. Chưa ra = FRESH, hợp lệ.
Bước 6. Chốt tối đa 2 số. Với MB, trần tin cậy là 55% — nếu bạn không đạt mức đó,
        hãy SKIP. Thà bỏ một ngày còn hơn chốt ép.

【DỮ LIỆU】
(kết quả thô 16 tuần của MB/MN/MT theo từng đài từng giải — không tóm tắt,
 không xếp hạng sẵn, không tính hộ)

【BẠN PHẢI TRẢ LỜI THEO KHUÔN NÀY】
 · Luật bạn chọn, viết đúng ngữ pháp: [Miền]:[Giải]#[Bộ]:[Lag] → (MB, CN)
 · Vòng lặp bạn dùng và VÌ SAO chọn vòng lặp đó
 · Với MỖI số bạn đưa ra: liệt kê NGÀY – ĐÀI – GIẢI cụ thể làm căn cứ
 · Trạng thái anti-trap của từng số: FRESH / PARTIAL_SPENT / FULL_SPENT
 · Mức tin cậy, và nếu dưới 55% thì ghi SKIP

【CẤM】
 · CẤM đưa số mà không dẫn được ngày–đài–giải. Máy sẽ đối chiếu, dẫn sai thì
   toàn bộ lượt của bạn bị loại.
 · CẤM dùng nguồn xổ sau đích trong cùng ngày.
 · CẤM suy diễn kiểu "số này đẹp", "số này lâu chưa về nên sắp về".
   Mọi khẳng định phải quy được về một luật viết đúng ngữ pháp trên.
```

**Điểm mấu chốt em đã làm sai lần trước và nay sửa:** T3 **KHÔNG phải là bỏ tri thức**. T3 là
**giữ TOÀN BỘ tri thức** — ngữ pháp, nhân quả, whitelist giải, lịch đài, doctrine cửa sổ, anti-trap
— và **chỉ bỏ đúng một thứ: KẾT QUẢ ĐÃ TÍNH SẴN**. Đó là khác biệt giữa *«bắt model làm việc»* và
*«bắt model đoán mò»*.

### ④ Chốt chặn suy diễn — máy kiểm được, không phải lời hứa

Khối `【CẤM】` ở trên **kiểm được bằng máy**: mỗi số phải kèm `(ngày, đài, giải)`; script đối chiếu
thẳng `lottery_results`. Dẫn sai ⇒ **loại lượt**. Đây là thứ biến *«cấm suy diễn»* từ câu khẩu hiệu
thành **cổng**, và nó phải nằm trong T3 **ngay từ bản đầu**, không vá sau.

Thêm một chốt nữa lấy từ KNOWLEDGE LOCK §8 — **6/12 khối cơ chế cũ mắc cùng một bệnh**: *«chấm điểm
bằng nhìn ngược quá khứ rồi bảo model tin»*. T3 **không được** lặp lại: mọi con số bằng chứng đưa
vào T3 phải **kèm mức bằng chứng thật** (đo tiến hay chấm ngược), đúng tinh thần
*«bằng chứng kèm mức tin nói thật»* ở §11.

---

## 5. GĐ-2 — 25 TỆP ROSTER, XẾP DỄ → KHÓ

*(điền từ bộ soi từng tệp — mỗi tệp một verdict, chia lượt tuần tự)*

---

## 6. GĐ-3 — DOSSIER CÂU HỎI GỐC (PLAN-ONLY, trình owner 20/08)

*(điền từ bộ điều tra Q-A … Q-E)*

---

## 5bis. SAU KHI ĐỌC HẾT — BẢN ĐỒ NỀN VÀ ĐỀ XUẤT

> Owner ký: *«đợi đọc cho đủ nắm cho kỹ trước rồi hãy làm»*. Mục này viết **sau khi** đã đọc xong
> toàn bộ. Tổng cộng **~120 agent · ~23 triệu token** qua 6 bộ chạy nền.

### ① ĐÃ ĐỌC NHỮNG GÌ — và chỗ nào vẫn thiếu

| nguồn | quy mô | kết quả |
|---|---|---|
| GĐ-3 dossier 5 câu hỏi gốc | 9 agent | ✅ |
| GĐ-2 soi 25 tệp roster | 51 agent | ✅ **13 chỗ phản biện bác lượt đầu** |
| Đào lại nền prompt (5 kho) | 11 agent | ✅ |
| **Notion 14 hub** | 29 agent | ✅ — 6 hub bị báo thiếu, **đã vét lại** |
| Vét nốt Claude + 6 hub | 15 agent | ✅ |
| **Session Cursor** | 275 phiên · 213.115 tin nhắn | ✅ |
| `KE_HOACH_THAY_MODEL_20260801.md` · **79 dòng A/B** | — | ✅ |

**Chỗ vẫn thiếu, nói thẳng:** bản ghi Claude **KHÔNG chứa lời owner gốc** — sáu tệp 36,6 MB hoá ra
là **một bản duy nhất nhân bản sáu lần** (`md5` sau khi bỏ dòng 1 giống hệt:
`4bf972f744c050770946a1288801f783`), và 11 khối tưởng là lời owner thật ra là **6 bản tóm tắt tự
động + 1 caveat + 4 dòng lệnh `/model`**. Mọi câu owner trong đó là **trích lại trong bản tóm tắt
do chính agent viết** — nguồn hạng hai (RM-13). Tệp còn **bị cắt cụt giữa câu ở dòng 1457**.

### ② SÁU LẦN EM KẾT LUẬN SAI TRONG PHIÊN NÀY

| # | em nói | sự thật | nguồn |
|---|---|---|---|
| 1 | «25 tệp thêm roster, đẩy = đổi đường chọn số» | commit `217a6ed` **`fix Opus model ID`** — **25/25 là ĐỔI TÊN**, trọng số `0.75` y hệt. Và bản VPS mới là bản **hỏng**: `.get()` trật khoá ⇒ đang dùng `DEFAULT_DISCOUNT=0.70` | `git show 217a6ed` · `strength_calibrator.py:90` |
| 2 | trình lưới 2×2 ghép cặp như thiết kế mới | **owner đã viết 01/08** — `KE_HOACH_THAY_MODEL` GĐ4, kèm cỡ mẫu «~13 ngày thấy 5pp @95%», trạng thái **NEVER_RAN** | `docs/KE_HOACH_THAY_MODEL_20260801.md:144-153` |
| 3 | «T3 cần thêm tri thức soi cầu» | **RR-16.5 đã có đủ** §9 · §10 · §10A · §10B · §19 | `gpt_analyzer.py:482+` |
| 4 | T3 có **6 bước bắt buộc theo thứ tự** | đó là `PHASE_FIRST_CONTRACT` — **đo 70 ngày: 34,0% vs 34,2% = 0**, gỡ 25/06, owner **ký lại 00:33 ngày 09/08** không bật lại | Notion V10750 · V10871 · Active Plan Ledger |
| 5 | «gan bằng 0 thông tin» | **đo sai nền** — dùng 43% (mọi giải) thay vì **6,09%** (G8+ĐB) | đã đo lại |
| 6 | «nút thắt ở SINH, chọn chỉ tranh trong 15%» | **sai** — trong 360 ngày pool ĐÃ có số trúng, bạch thủ chỉ đúng **32,2%**, mất **244 ngày** ở khâu chọn | khớp Notion `CI-05` |

Gốc chung của cả sáu: **đề xuất trước khi đọc**, và **lẫn hai lớp Notion** — lớp SPEC/ý đồ (tự dán
nhãn *«implementation target»* = đích phải đến) với lớp AS-BUILT (cái đang chạy).

### ③ BỨC TRANH THẬT — hai nút thắt nối tiếp, không phải một

| tầng | mất bao nhiêu | n | nguồn |
|---|---|---|---|
| **SINH** | **82,5–85,7%** đuôi trúng không model nào sinh · cả 27 model gộp chỉ ra **~16 số/ngày** trong khi ngày ra **24–43 đuôi** | 30 ngày | em đo |
| **CHỌN** | trong **360** ngày-miền pool **đã có** số trúng, bạch thủ chỉ đúng **116 (32,2%)** ⇒ mất **244 ngày** | 120 ngày | em đo · khớp `CI-05` |

MB nặng nhất: pool có số trúng **119/120 ngày**, bạch thủ đúng **17,6%** — **thấp hơn cả nền 23,7%**,
tức **chọn tệ hơn bốc ngẫu nhiên từ chính pool của nó**.

**Và nguyên nhân tầng SINH nằm ngay trong prompt:** `RR §4` cảnh báo *«đồng thuận giả»*, nhưng
`§11` + `§18` ra lệnh *«KHÔNG tự tạo số mới nếu Rule Tails đã có gợi ý mạnh»*. Rule Tails giống hệt
cho 16 model ⇒ **trần độ phủ được viết thẳng vào prompt dưới dạng mệnh lệnh**, mâu thuẫn với §4
ngay trong cùng bộ luật.

### ④ CÔNG TẮC KHÔNG AI NHẮC — `MINED_RULES_MODE`

`main.py:124`, **giống hệt trên VPS**:

```python
#   off | shadow (chỉ log, KHÔNG bơm điểm) | soft (boost ~0,15) | active (boost ~0,35)
MINED_RULES_MODE = 'soft'      # V6.4: shadow → soft pilot
MINED_RULES_APPLY_TO = 'all'
```

Ghép ba mảnh lại:

| | |
|---|---|
| `KNOWLEDGE LOCK §8` | **0/105 luật qua cổng** · chấm ngược **+9,77σ** nhưng đo tiến **−0,33σ/+0,26σ** |
| Notion `CI-14` **P0 BLOCKER** | `rules_union` hậu-xổ **phồng backtest ~+12pp** ⇒ mọi claim bị hạ cấp |
| `main.py:124` | **vẫn đang cộng +0,15 cho `all`** |

⇒ Hệ **đang cộng điểm bằng bộ luật mà chính tài liệu ghi là 0/105 qua cổng**, trên một nền đã bị
phồng +12pp. Đây đúng loại «+điểm» owner đã bực với gan, nhưng **quy mô lớn hơn và chưa ai tắt**.

### ⑤ GAN — đo lại đúng phạm vi giải owner khai

Owner đính chính: gan soi **G8+ĐB** (MN/MT) và **ĐB** (MB) — *các giải ÍT BỘ SỐ*, không phải mọi
giải. Nền đúng: **6,09% / 4,68% / 1,00%**, không phải 43/35/24%.

**Gan bao lâu thì nổ** (400 ngày, từ `tail_g8`/`tail_db`):

| miền | trung vị | p75 | p90 | ngưỡng đang dùng | còn chưa ra ở ngưỡng đó |
|---|---|---|---|---|---|
| MN | **11** | 22 | 35 | 7 | **63,4%** |
| MT | **14** | 28 | 45 | 7 | **70,3%** |
| MB | **59** | 104 | 150 | 15 | **83,3%** |

⇒ **Cả ba ngưỡng nằm dưới trung vị rất xa ⇒ cờ gan bật gần như thường trực.** Khi trước gan lại
**+điểm**, nó cộng cho gần như mọi số. **Lỗi ngưỡng, không phải lỗi ý tưởng.**

**Đúng thiết kế owner** (gan chỉ lọc, không đề xuất):

| miền | gốc (model đề xuất) | tốt nhất | chênh | z÷√VIF |
|---|---|---|---|---|
| MN | 5,88% (n=2.415) | gan>30 → **7,25%** | **+1,37 pp** | +0,67 |
| MT | 5,27% (n=2.484) | gan>30 → 5,85% | +0,58 pp | +0,35 |
| MB | 0,91% (n=2.418) | gan>45 → 0,99% | +0,08 pp | +0,20 |

26 ô, **không ô nào chạm 1,96** ⇒ **chưa được phép kết luận**, nhưng **chiều dương ở ngưỡng dài**.

### ⑥ BÁO CÁO 14/07 KHÔNG AI VIẾT — `PROMPT_V2_AB_V1`, 79 cặp

Ghép cặp sạch: cùng `deepseek-reasoner`, cùng ngày, cùng miền. `test_bt` = prompt V2 ·
`official_bt` = prompt V1.

| | bạch thủ | lo2 |
|---|---|---|
| prompt **V2** | **36,7%** | 60,8% |
| prompt **V1** | 31,6% | 58,2% |
| chênh | **+5,1 pp** | +2,5 pp |
| McNemar | 32 cặp lệch · **z = +0,71** | 38 cặp · z = +0,32 |

| miền | V2 | V1 | chỉ V2 trúng | chỉ V1 trúng |
|---|---|---|---|---|
| **MT** | **58%** | 38% | **8** | 3 |
| MN | 31% | 23% | 6 | 4 |
| MB | 22% | **33%** | 4 | 7 |

**Chưa đủ để kết luận** — cần **~246 cặp** (≈82 ngày × 3 miền); cron bị tắt **01/08** khi mới **26
ngày**. Nhưng nó chứng minh **thiết kế ghép cặp chạy được và rẻ** (`~$0,134/ngày`).

### ⑦ ĐỘ PHÂN GIẢI — vì sao «hứa rồi rữa» sáu lần

| tầng đo | n | **thấy được lợi thế nhỏ nhất** |
|---|---|---|
| sản phẩm · bạch thủ 1 miền · 121 ngày | 121 | **15,1 pp** |
| đơn model · 12 ngày (cửa sổ FU-284) | 192 | **8,0 pp** |
| đơn model · **gộp 3 miền · 91 ngày** | 4.368 | **2,0 pp** |

Cải tiến thật **+5pp** trên bạch thủ MN cần **~3 năm** mới hiện; **+3pp** cần **~8,4 năm**.
⇒ Sáu lần «rữa» trong `CLAUDE.md` **có thể không giả — chỉ nhỏ hơn độ phân giải của thước**.

---

## 6bis. ĐỀ XUẤT — xếp theo AN TOÀN × LỢI ÍCH

> Tất cả **PLAN-ONLY**, chờ owner ký. Không mục nào đụng production trước khi có chữ ký.
> Mỗi mục ghi rõ **gắn nút nào** của xương sống [20/08 chốt → 21/08 mở khoá].

### Nhóm A — SỬA LỖI, rủi ro gần bằng 0

| # | việc | vì sao an toàn | lợi ích | nút |
|---|---|---|---|---|
| **A1** | **Đẩy 25 tệp đổi tên Opus** | không thêm model — chỉ khớp lại khoá đã chết từ 15/06; trọng số y hệt | hết áp nhầm 0,70 thay vì 0,75 · drift K3 **26 → 1** | 21/08 |
| **A2** | **Thêm vế `D-2` cho MN vào `RR §9`** | đúng công thức owner **đã khoá** ở `V105.19 §7`; mã đang thiếu đúng vế owner nói MN cần nhất | MN là miền owner nêu cần rescue | 21/08 |
| **A3** | **Bật lại writer gan** (shadow, `output_eligible=0`) | **0 đồng** — gan tính nội bộ, không gọi API | có dữ liệu đo phép hội tụ **tiến** | ngay |
| **A4** | **Sửa ngưỡng gan** MN>15 · MT>15 · MB>60 | chỉ đổi ngưỡng bảng shadow | cờ gan hết bật thường trực | ngay |

### Nhóm B — CẢI TIẾN THẬT, có đo, không tốn thêm tiền

| # | việc | thiết kế | thấy kết quả |
|---|---|---|---|
| **B1** ⭐ | **Sửa khâu CHỌN cho MB** | pool có số trúng **119/120 ngày** mà bạch thủ đúng **17,6% < nền 23,7%**. Không cần thêm model, không cần thêm token | dư địa lớn nhất toàn hệ |
| **B2** | **Phân tích tiếp 79 dòng A/B** + bật lại cron `PROMPT_V2_AB_V1` | dữ liệu đã có, thiết kế đã đúng, chỉ thiếu mẫu | ~82 ngày để đủ z |
| **B3** | **Gỡ `RR §11` + `§18`** | **không thêm gì**, chỉ gỡ hai câu cấm model sinh số ngoài Rule Tails — hai câu này mâu thuẫn với `§4` cùng bộ luật | đo bằng **độ phủ**, thấy **ngay ngày đầu** |
| **B4** | **Đổi `MINED_RULES_MODE` `soft` → `shadow`** | một dòng, có đường lui ngay. Biến bộ luật 0/105-qua-cổng từ «cộng điểm» thành «chỉ quan sát» — đúng nguyên tắc owner đã áp cho gan | gỡ nguồn nhiễu lớn nhất khỏi đường chọn số |
| **B5** | **Chạy lưới A/B owner ký 01/08** (GĐ4) | `shadow_mode=False/True`, cùng model cùng ngày cùng miền | ~13 ngày |

### Nhóm C — KHÔNG LÀM, đã có bằng chứng bác bỏ

| | vì sao |
|---|---|
| bật lại **phase-first / 6 bước cứng** | đo **70 ngày = 0**; owner ký bỏ **3 lần**, gần nhất 00:33 ngày 09/08 |
| dùng `proposed_weight_30d` của v93 đổi trọng số | công thức `clip(0.5+any_hit/100)`; chú thích gốc ghi *«for now»*; chênh do **trọng số cũ**, không do hiệu năng |
| **gan +điểm** | chính thứ owner bực; ngưỡng cũ làm nó bật thường trực |
| đổi roster / thêm model để cứu chất lượng | Notion: *«roster bão hoà, **selector là nút thắt**»* · `D-04`: *«giá không xếp hạng chất lượng»* |

### Thứ tự em đề nghị

1. **A3 + A4** — 0 đồng, không đụng đường ra số, bật ngay được
2. **B3** — gỡ hai câu lệnh, đo bằng độ phủ, thấy ngay
3. **B4** — một dòng, đường lui ngay
4. **A1 + A2** — gộp vào lượt deploy 21/08
5. **B1** — việc lớn nhất, cần thiết kế riêng
6. **B5** — sau khi 21/08 mở khoá

---

## 7. Cổng kiểm

**Cổng cấp số hiệu FU-369 (chạy trước khi cấp mã):**

```
V  : 401 số · cao nhất V11054 · trống tiếp: V11055
FU : 262 số · cao nhất FU-393 · trống tiếp: FU-394
QD : 42 số  · cao nhất QD-054 · trống tiếp: QD-055
```

*Ghi chú cổng:* V11054 hiện **đã có chủ** vì cổng quét **tên thư mục báo cáo** — tức việc tạo thư
mục `V11054_…` **chính là hành vi cấp mã**. Đúng thiết kế, và đúng bài học đã ghi ở V11050d: **đặt
tên mã vào tiêu đề/thư mục LÀ cấp mã**.

**Trần sinh mã: 3/5** — `FU-391` · `FU-392` · `FU-393`. **Phiên này chưa sinh mã FU mới.**

---

## 8. Gỡ về

Phiên này tới thời điểm viết **chưa đụng production** ngoài V11053 (đã ghi ở báo cáo đó).
GĐ-1/GĐ-2/GĐ-3 đều **read-only**. Không có gì để gỡ.

---

## 9. Theo dõi tiếp

| việc | khi nào | nút xương sống |
|---|---|---|
| **FU-360 deploy** + thử chặn thật + canh 24h | **sáng 10/08**, trước 15:30 | 21/08 mở khoá |
| bầy đàn đủ **9/9** lượt miền-ngày | **10/08** | 20/08 chốt |
| C18/C19 tự hết đỏ khi 04/08 rơi khỏi cửa sổ 7 ngày | **12/08** | 20/08 chốt |
| 25 tệp roster có verdict đủ | **trước 20/08** | 21/08 deploy một lượt |
| dossier câu hỏi gốc trình owner ký gộp | **20/08** | 20/08 chốt |
| FU-284 đọc bằng ngưỡng **9,53** | **20/08** | 20/08 chốt |

*Đẩy cùng commit (A55 · §57.2).*
