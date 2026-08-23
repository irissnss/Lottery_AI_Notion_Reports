# REPORT V11107 + V11108 — AUDIT CỰC GẮT · 23/08/2026 (tối)

> **Phạm vi:** hai version trong một phiên. `V11107` = vá `FU-427`/`FU-428` + dựng cổng prompt
> mồ côi. `V11108` = audit bảy tác nhân, tìm ra lớp ghi đè, và **rút lại** chính bản vá `FU-427`.
>
> **Commit:** `8ca990d` (V11107) · `0cb5e78` (V11108) — cả hai **đã xác nhận trên remote**.
> **VPS (CẬP NHẬT 22:28):** đã **GỠ VỀ** `RR-16.5` · `CTX-18.6` theo lệnh owner — PID `2341779`.
> Bản `RR-16.6` từng serve 21:1x–22:28, **không lượt dự đoán nào chạy trên nó**.
>
> 🔴 **ĐỌC §1b TRƯỚC KHI ĐỌC §3.7** — bản này có một câu bị rút lại.

---

## 1 · TÓM TẮT

| # | việc | kết quả |
|---|---|---|
| 1 | **Tìm ra lớp ghi đè số công bố** — treo từ `FU-429` | `main.py:10059–10072` → `_v10640…` · **MN BẬT**, MT/MB TẮT · **owner đã ký duyệt** |
| 2 | **Gốc bệnh bản ghi nói ngược** | `main.py:10189` lấy `ranked[0]` — số **TRƯỚC** ghi đè · **51/183 = 27,9%** bundle |
| 3 | **RÚT LẠI `FU-427`** | bản vá đầu **tự đổi ngưỡng sau khi thấy số** — đúng thứ owner cấm |
| 4 | **ML miền MB dưới mức ngẫu nhiên** | `AUC < 0,50` suốt **13/13** lần học lại |
| 5 | **«4 model ML» = ~2 phép thử độc lập** | trùng số đầu **24–31%** vs kỳ vọng **1,5%** |
| 6 | **`FU-428` — hai mệnh lệnh mồ côi**, không phải một | dòng thứ hai mồ côi **16 ngày**, lộ ra **tình cờ** |
| 7 | **Cổng máy cho `PRJ-PROMPT-COHERENCE-001`** | họ lỗi này đã cắn **ba lần** ⇒ phải là cổng |
| 8 | **Sổ yêu cầu owner** | **302 mã FU** · 19 thiếu hạn · 50 thiếu ngưỡng |
| 9 | Nghi ngờ «ghi đè/trôi» của owner | 🔴 **RÚT LẠI câu «bác bỏ»** — đúng ở tầng DB nhưng **SAI TẦNG**. Bề mặt trả `bundle: null` cho MN 22/08 (cổng publish đòi đúng 15, có 14). **Bạch thủ 10 thắng nhưng chưa bao giờ lên trang — owner ĐÚNG.** Xem §1b |

**Không kết luận được:** `V11106`/`V11107` **chưa** `RUNTIME_PROVEN` — giờ VN trên VPS là
`23/08 21:xx`, lượt 05:00 ngày 24/08 **chưa xảy ra** (`RM-12`).

---

## 1b · 🔴 RÚT LẠI TRONG CHÍNH BẢN NÀY — trả lời **SAI TẦNG** cho nghi ngờ của owner

**Chỗ gốc:** chính mục `V11108` này · `docs/CURRENT_TRUTH_SSOT.md` mục `V11108` ·
`Lottery_AI_Notion_Reports/V11108_AUDIT_CUC_GAT_20260823/REPORT_V11108.md` §1 và §3.7 ·
commit riêng `0cb5e78`, công khai `90ec8dd` — **cả hai đã lên remote**.

**Nguyên văn câu sai:**

> *«**MN 22/08 bạch thủ = `10`, WIN, OFFICIAL** … `V11104` **xác minh đúng**.»*
> *«Nghi ngờ «ghi đè/trôi» của owner: **bác bỏ ở tầng DB**.»*

**Điều đúng.** Mọi câu trên **đúng ở tầng DB** và vẫn giữ nguyên. Nhưng owner **không hỏi về
DB** — owner nói về **thứ owner NHÌN THẤY**. Đo đúng bề mặt đó:

```
GET /api/final-bundle?region=MN&date=2026-08-22
  → "bundle": null · "empty": true
  → "message": "Official chưa đủ điều kiện publish: cần đúng 15 model
                 output-eligible, hiện có 14."
  → "publication_status": "WAIT_MODEL_COUNT"
```

**Bạch thủ `10` thắng thật, nhưng CHƯA BAO GIỜ lên trang `/du-doan`.** Owner nói *«MN không có
bạch thủ 10»* — **owner ĐÚNG**. Em đã trả lời một câu hỏi **khác** với câu owner hỏi.

**Phép đo tái lập được** (`RM-11`) — **ĐỦ BỐN CỬA SỔ** (`PRJ-SELECTION-WINDOW-001`):

| cửa sổ | cặp ngày-miền | qua cổng | **bị chặn** | tỉ lệ chặn | **bundle THẮNG bị chặn** |
|---|---:|---:|---:|---:|---:|
| 14 ngày | 45 | 43 | 2 | 4,4% | 1 |
| 30 ngày | 93 | 90 | 3 | **3,2%** | 1 |
| **90 ngày** | 273 | 196 | 77 | **28,2%** | **27** |
| **180 ngày** | 543 | 196 | **347** | **63,9%** | **126** |

> 🔴 **CỔNG `PRJ_WINDOW_NOT_SPLIT` BẮT ĐƯỢC EM.** Bản đầu của mục rút lại này chỉ trích **30
> ngày** (`3,2%`) — và cổng `_v11088_cong_cua_so_chon.py` **chặn commit**. Nó đúng: `3,2%` là
> **hiện vật của cửa sổ chọn**. Nhìn đủ bộ thì cổng publish từng chặn **đa số ngày**, và
> **126 bundle THẮNG chưa bao giờ lên trang** trong 180 ngày.
>
> Đây là **đúng cái lỗi em phê người khác suốt phiên** (hai làn phản biện bác làn đo vì
> «không tách cửa sổ»). Em mắc lại nó **ngay trong mục rút lại một lỗi khác**.

**Đọc đúng dải thời gian:** mọi lượt **qua cổng** đều nằm trong **90 ngày gần nhất** (196 ở cả
hai cửa sổ 90 và 180) ⇒ trước cuối tháng 5 **gần như không ngày nào publish được**. Lần chặn
gần nhất **trước** 22/08 là **16/06** ⇒ **~66 ngày sạch liên tục**, rồi 22/08 tái phát. Nên
`22/08` là **một ca lẻ sau hai tháng sạch**, KHÔNG phải triệu chứng thường trực — nhưng cũng
**không phải chuyện mới**.

| ngày | miền | có | thiếu | BT | kết cục |
|---|---|---|---|---|---|
| 26/07 | MT | 14/15 | `glm-5.1` | 03 | LOSE |
| 13/08 | MT | 14/15 | `glm-5.1` | 40 | LOSE |
| **22/08** | **MN** | **14/15** | **`deepseek-reasoner`** | **10** | 🔴 **WIN** |

**Quyết định nào đã dựa trên số sai:** không có quyết định, **nhưng có hậu quả thật** — câu
*«bác bỏ ở tầng DB»* **đóng lại đúng hướng điều tra** dẫn tới `FU-434` · `FU-435` · `FU-436`.
Nếu owner không hỏi lại, ba mục đó **không được mở**.

**Bài học:** *«dữ liệu đúng»* **không phải** câu trả lời cho *«tôi không thấy nó»*. Phải hỏi
**owner nhìn ở đâu** rồi đo **đúng bề mặt đó**. Cùng họ `RM-13` — chỉ khác là lần này nguồn
**đúng**, còn **tầng** thì sai.

**Đính chính kèm theo — bề mặt viewer bị đóng băng là CÓ CHỦ Ý, không phải lỗi:**
`main.py:6311` `_VIEWER_FREEZE_DATE = "2026-06-07"`, owner ký 08/06 —
**admin/dev KHÔNG BAO GIỜ bị treo**, chỉ viewer/public treo. `curl` không đăng nhập rơi vào
nhánh viewer, nên `requested_date` trả về `2026-06-07`. **Đó là thiết kế, không phải trôi.**

---

## 2 · OWNER YÊU CẦU GÌ (NGUYÊN VĂN)

> *«PROMPT TỔNG LỰC LẦN 30 — 24/08: AUDIT CỰC GẮT»*

Sáu chất vấn:
① nghi dữ liệu kết quả **bị ghi đè/trôi** *(«MN không có bạch thủ 10»)* ·
② đòi **đo model AI NGAY**, không chờ chuyển hoá ngữ cảnh ·
③ **so chéo regime shadow vs official là SAI** — một bên được nhồi số, một bên phải tự tìm ·
④ lượt AI rỗng phải **truy tới nơi** ⇒ sửa hoặc thay ·
⑤ **ML phải fix TỪ GỐC TỚI NGỌN** ·
⑥ *«đo hoài không ra»* — mọi phép đo phải có **NGÀY QUYẾT ĐỊNH** và **verdict**.

Vùng cấm: *«CẤM so sánh chéo regime shadow vs official · CẤM kết luận khi chưa đủ mẫu/ngưỡng ·
CẤM hạ sàn cho hết đỏ · CẤM heredoc khi sửa mã · ≤5 FU mới · số hiệu từ `_v11044` · báo tiến độ
TỪNG CHẶNG · CẤM cờ bỏ-qua-cổng · §62 ba lớp + «TanPhatAI cần làm:» · QD-069.»*

> **Ghi chú thước — đọc trước khi đi tiếp.** Câu ① ở trên là **trích nguyên văn câu hỏi của
> owner**, KHÔNG phải một tuyên bố hiệu quả. Mọi phép đo liên quan **bạch thủ** trong bản này
> báo **đủ bốn cửa sổ** theo `PRJ-SELECTION-WINDOW-001` — xem **§1b**
> (14 / 30 / 90 / 180 ngày). Và bảng *«chênh tiền»* ở **§3.1** thuộc **một thước KHÁC**
> (lớp ghi đè `V10640`, thước tiền của `FU-183`), **không** phải thước bạch thủ vs nền —
> `RM-21`: hai thước không đọc chung được.

**Một chỗ trong lệnh phải nói lại:** prompt đề *«24/08»* nhưng **giờ VN trên VPS là
`2026-08-23 20:46`** lúc bắt đầu phiên. Ngày 24/08 **chưa tới**.

---

## 3 · ĐÀO BỚI / PHÁT HIỆN

### 3.1 · Lớp ghi đè — có tên, có cờ, có bảng theo dõi, và **owner đã duyệt nó**

`FU-429` (21/08) ghi *«lớp ghi đè **không được ghi lại ở đâu**»* và để ngỏ **lớp nào**.

| | |
|---|---|
| **điểm gọi** | `web/backend/main.py:10059–10072` |
| **mã** | `from _v10640_official_perslice_override import get_override_bt` … `if _ovr_bt … : bach_thu = _ovr_bt` |
| **cấu hình** | `_v10640_official_perslice_override.py:28` → `OVERRIDE_CONFIG` |
| **cờ hiện tại** | **MN `enabled=True`** (`chooser="specialist"`) · MT `False` · MB `False` |
| **lô 2 số** | `main.py:10076` — tính **SAU** ghi đè ⇒ bị kéo theo |
| **lịch sử** | `V10917` (01/08, owner ký): TẮT MT + MB, GIỮ MN. Đo tiến 60 ngày: MT `−24,5tr` · MB `−29,4tr` · MN `+14,7tr` |

**Giải thích trọn vẹn** phát hiện cũ *«13/93 bundle có `bach_thu ≠ ranked[0]`, TẤT CẢ đều MN»*.

**Đo lại tới 23/08** — tự chạy `_v10918_override_watch`, không lấy số của tác nhân:

| cửa sổ | ghi đè | cứu | phá | hoà | `p` thử dấu | chênh tiền |
|---|---:|---:|---:|---:|---:|---:|
| **từ 01/08** | **8** | **4** | **1** | 3 | **0,375** | **+14,7tr** |
| 60 ngày MN | 20 | 8 | 2 | 10 | 0,109 | +39,2tr |
| 120 ngày MN | 29 | 10 | 5 | 14 | 0,302 | +29,4tr |

Tám ca kể từ 01/08, đối chiếu **đuôi ra thật**:

```
06/08  phiếu 60 trượt → công bố 95 TRÚNG   ghi đè CỨU
07/08  phiếu 60 trượt → công bố 13 TRÚNG   ghi đè CỨU
09/08  phiếu 22 trượt → công bố 54 trượt   hoà
14/08  phiếu 14 trượt → công bố 41 TRÚNG   ghi đè CỨU
16/08  phiếu 32 trượt → công bố 71 trượt   hoà
17/08  phiếu 96 trượt → công bố 89 TRÚNG   ghi đè CỨU
19/08  phiếu 02 trượt → công bố 56 trượt   hoà
23/08  phiếu 46 TRÚNG → công bố 73 trượt   ghi đè PHÁ   ← ca PHÁ duy nhất, và là HÔM NAY
```

> **CẤM đọc thành «lớp ghi đè đang thắng»** — `n=5`, `p=0,375`. Chính chú thích trong mã đã ghi
> từ đầu: *«nhánh MN dương nhưng **CHƯA đạt chuẩn chắc chắn** (`p=0,754`) — giữ vì là phương án
> đo được tốt nhất, **không phải vì đã chứng minh**»*.

**Ngưỡng + ngày quyết định ĐÃ CÓ SẴN** (`_v10640…:62-64`): *«nếu MN **âm tiền** trong 30 ngày
tới (**rà 2026-08-31**) thì tắt nốt, xem `FU-183`»*.
⚠️ **`RM-21`:** ngưỡng viết bằng **TIỀN**; bảng cứu/phá là **TRÚNG/TRẬT** — **không thay thế nhau**.

### 3.2 · Gốc bệnh của bản ghi nói ngược — nay có tệp:dòng

| | |
|---|---|
| `main.py:10068` | lớp ghi đè đổi `bach_thu`, **và cập nhật `top_score`** |
| `main.py:10189` | `top1_row = ranked[0]` ← **số TRƯỚC ghi đè** |
| `main.py:10199` | `top1_reason = f"selected {top1_row[0]} …"` ← **tả số KHÔNG được công bố** |

Cách nhau **120 dòng**, không ai nối. Đo được **51/183 = 27,9%** bundle nói ngược.
`generation_method` ghi `'weighted_voting_wr'` cho **183/183** kể cả 51 ca đổi số ⇒ **đọc DB
không có cách nào biết lớp nào đã đổi**. Bốn lớp ghi đè đều **nuốt lỗi** bằng `try/except` chỉ
`print` (`:10071 · 10092 · 10112 · 10132`).

### 3.3 · ML — gốc tới ngọn

**GỐC · MB dưới mức ngẫu nhiên.** `AUC` toàn lịch sử (`training_history`):

| miền | random-forest | xgboost | meta-learning | lstm |
|---|---|---|---|---|
| **MB** | **0,4844** 🔴 | **0,4881** 🔴 | **0,4925** 🔴 | 0,5031 |
| MN | 0,5165 | 0,5076 | 0,5118 | 0,5114 |
| MT | 0,5425 | 0,5410 | 0,5395 | 0,5491 |

`AUC < 0,50` **không phải «yếu»** — tín hiệu yếu là `≈ 0,50`. Dưới 0,50 là **xếp hạng ngược**.
**Hai thước độc lập cùng chiều** (AUC trên tập kiểm nội bộ · tỉ lệ trúng trên kết quả xổ thật).

**GỐC · «4 model ML» ≈ 2 phép thử độc lập.** Trùng số đầu vs kỳ vọng (hoán vị ngày ≥2.000 lần):
`xgb+rf 31,1%` · `meta+xgb 29,0%` · `meta+rf 24,0%` — kỳ vọng **~1,5%**. `lstm` **0–1,6%** =
đúng mức ngẫu nhiên ⇒ **ML độc lập duy nhất**. `xgb`/`rf` dùng chung **28 đặc trưng**.

**THÂN.** `smart-ml` **không hơn** chính đầu vào tốt nhất của nó: vs `random-forest`
`b=19 c=26` điểm `−3,8%` `z=−1,04`. Chưa đủ mẫu ⇒ **chưa kết luận**, nhưng đủ để dựng shadow.

**CADENCE.** **Không có bằng chứng** học lại hằng tuần giúp: `66/129 = 51%` lần AUC tốt lên,
`ΔAUC +0,00045`, `z=+0,37`. **Không đề xuất đổi nhịp** — phép đo đúng **đã tồn tại** (hẹn
**06/11**, `FU-285`). ⚠️ Nhưng bản đối chứng **chỉ có 6/12 tệp**, thiếu `lstm` + `meta_learner`
⇒ **hạn cứng 30/08 trước 02:00**.

### 3.4 · Vì sao **KHÔNG** công bố bảng xếp hạng 15 model

Hai làn phản biện độc lập bác bảng của làn đo ở **ba** chỗ:

| chỗ bị bác | bản đo nói | phản biện đo lại |
|---|---|---|
| hệ số cụm | `DEFF = 1,045` (cụm model×ngày) | dòng **GỘP 15 model** phải dùng cụm **NGÀY** ⇒ `DEFF = 6,88` (sandwich) / `7,09` (bootstrap 4.000 lần). **`z: 1,72 → 0,65`** — phồng **2,6×** |
| `n` cần | dùng `z = 1,96` | tự mâu thuẫn với ngưỡng chính nó đăng ký (Bonferroni 15 model ⇒ `z=2,938`); thêm sức mạnh 80% ⇒ phồng **3,72×**. *«sớm nhất THĂNG 11/12/2026»* → thực tế **2027–2028** |
| không tách cửa sổ | một con số gộp | tách **ngày theo phiếu bầu** vs **ngày bị ghi đè**: `+0,0055 (p=0,866)` vs `+0,1879 (p=0,00076)` |

**Cơ chế:** **0/384** ô ngày-miền có đồng thời `b>0` và `c>0` ⇒ **15 model trong một ngày-miền
LUÔN CÙNG DẤU**. Cụm gần như hoàn hảo — đó là lý do `DEFF` thật gần **7**.

### 3.5 · `FU-433` — mọi phép đo thước cặp **gộp qua một biên chế độ NỀN**

`01/08` (`V10917`) tắt 5 lớp ghi đè ⇒ **nền của thước đổi chất**:

| miền | ngày bị ghi đè TRƯỚC 01/08 | TỪ 01/08 | thước TRƯỚC | thước TỪ |
|---|---|---|---|---|
| MB | 23,8% | **0%** | **+0,2242** (z=+4,07) | **−0,0870** (z=−0,83) |
| MT | 21,0% | **0%** | **+0,1218** (z=+2,54) | **−0,1311** (z=−1,45) |
| MN | 20,0% | **34,8%** | −0,0588 | −0,0429 |

Năm lần trước đều soi regime ở vế **MODEL** (shadow vs official). **Chưa lần nào soi vế NỀN.**

### 3.6 · Một điều luật của chính dự án **ghi công thức sai**

`RM-18` viết nền cho bộ `k` đuôi là `1 − (1−b)^k` — công thức **CÓ HOÀN LẠI**. `k` số dự đoán là
**phân biệt** ⇒ đúng phải là `1 − C(100−D,k)/C(100,k)`. Lệch nhỏ (0,18–0,25 điểm ở `k=2`) nhưng
**SAI CHIỀU**: luật **ước lượng THẤP** nền ⇒ luôn làm model trông **tốt hơn** thực tế. Không làn
nào bắt được **vì chính điều luật ghi sai**.

### 3.7 · `GĐ-0` — nghi ngờ của owner

- **MN 22/08 bạch thủ = `10`, WIN, OFFICIAL** — đuôi `10` có thật (Hậu Giang, giải tám). Bundle
  **duy nhất** có `bach_thu='10'` trong 30 ngày. `V11104` **xác minh đúng**.
- Tự kiểm **9/9** ca: `bach_thu_status` + `lo2_status` khớp **100%** với tính lại từ
  `prizes_json`, **0 lệch**.
- `lottery_results` **KHÔNG HỀ bị ghi đè**: 0 trùng lặp, **0 id bị đốt**, `sqlite_sequence == max(id)`.
- `final_bundles` ghi đè **tại chỗ 88 lần**/30 ngày nhưng **KHÔNG đổi số** (87/87 log khớp,
  **0 lần ghi sau mốc chốt**). Đối soát `88 == 87+1` khớp tuyệt đối.
- `predictions` dùng `INSERT OR REPLACE` ⇒ **ghi lại `created_at`** (1.556 id bị đốt). Phân loại
  đúng: **1.863** dòng `pre=[]` (**chưa chụp**, KHÔNG phải đổi số) · 157 giữ nguyên · **173 thật
  sự đổi số**, trong đó **144** thuộc model OUTPUT — **100% MB, 100% `rerun_post_mt`**.

> **Lời giải thích thứ ba, đo được:** số công bố cho MN **khác** số các model bầu ra ở
> **8/23 ngày = 34,8%** kể từ 01/08 — **đúng thiết kế**, do lớp `V10640`. Nếu owner đang so
> *«số model chọn»* với *«số hiện trên `/du-doan`»* thì **hai số đó lệch nhau thật, một phần ba
> số ngày**.

---

## 4 · HƯỚNG XỬ LÝ VÀ VÌ SAO CHỌN

**Không đụng đường chọn số.** Lớp `V10640` **owner đã ký duyệt**; ép `bach_thu = ranked[0]` là
**đổi đường chọn số**, không phải sửa bản ghi. Chỉ **GHI THÊM** (`override_layer` ·
`override_basis` · `pre_override_top1`) và **tính lại ba trường mô tả SAU ghi đè** — giữ `QD-018`
một-biến-một-lần.

**Đẩy prompt tối nay thay vì sáng mai.** Để tới sau 05:00 thì 24/08 chạy bản **vẫn còn** mệnh
lệnh mồ côi, 25/08 mới đổi ⇒ **hai biên regime liền nhau, cả hai `n` bé**, cắt đôi phép đo model
MB mà owner vừa ký *«đếm lại từ mốc hôm nay»*.

**Không công bố bảng xếp hạng.** Ba lỗi thước (cụm · ngưỡng · cửa sổ) đều **đổi kết luận**.
Owner cấm *«kết luận khi chưa đủ mẫu/ngưỡng»*.

---

## 5 · ĐÃ LÀM GÌ

| # | việc | bằng chứng |
|---|---|---|
| 1 | `FU-427` — bộ chấm T-B in **cả ba** điều kiện đăng ký | thử chặn **13/13** |
| 2 | `FU-428` — gỡ **hai** mệnh lệnh mồ côi · `RR-16.5 → RR-16.6` | dump production: cả hai `= 0` ở ba miền |
| 3 | Dựng cổng `PRJ_PROMPT_DANGLING` | `MỒ CÔI=0` · thử chặn **4/4** · khôi phục sạch |
| 4 | Vá `_v11062.ghi()` — bộ ghi và bộ kiểm dùng **cùng hợp đồng** | thử chặn **7/7** |
| 5 | Sổ yêu cầu owner | `docs/SO_YEU_CAU_OWNER_20260824.md` — **302** mã FU |
| 6 | Kế hoạch ML gốc→ngọn | `docs/KE_HOACH_ML_GOC_NGON_20260824.md` |
| 7 | `FU-430/431/432/433` mới — **tất cả có hạn + ngưỡng** | `FOLLOW_UP_TRACKER` |
| 8 | Deploy | PID `2299279 → 2317479 → 2320523` · `/api/health=200` · 4 bảng khoá `+0` |

---

## 6 · CỔNG KIỂM

| cổng | kết quả |
|---|---|
| `_v11062_nang_version.py --kiem` | ✓ **ĐẠT** — bốn mặt đi cùng nhau (V11107 · V11108) |
| `_v11044_cong_so_hieu.py` | ✓ `SO_HIEU_V11044=KHOP` · mọi nhãn QD trong 179 báo cáo đều có trong sổ |
| `_v11107_thu_chan_fu427.py` | ✓ **13/13** |
| `_v11107_cong_prompt_mo_coi.py --thu-chan` | ✓ **4/4**, khôi phục nguyên trạng |
| thử chặn heading `_v11062` | ✓ **7/7** |
| 4 bảng khoá PRE→POST | ✓ `+0` cả hai lượt đẩy |
| dump từ hàm đang serve | ✓ `RR= RR-16.6` |

---

## 7 · VƯỚNG VẤP

### 7.1 · 🔴 **RÚT LẠI — `FU-427` bản đầu TỰ ĐỔI NGƯỠNG SAU KHI THẤY SỐ**

**Chỗ gốc:** `CHANGELOG.md` mục `V11107` · `docs/CURRENT_TRUTH_SSOT.md` · `FOLLOW_UP_TRACKER`
khối `FU-427` · commit `8ca990d`, **đã đẩy lên remote**.

**Nguyên văn câu sai:** *«`122` là số dòng hai DỰ ĐOÁN khác nhau; ngưỡng `96` đăng ký cho **cặp
lệch KẾT CỤC** (`b+c`). Con số đó là **46**»* · *«còn thiếu **50 cặp lệch kết cục**»*.

**Điều đúng.** Ngưỡng đăng ký **11/08** ở **ba nơi độc lập** đều nói **«≥96 cặp BẤT ĐỒNG» VÀ
`|z| ≥ 1,96`** (`SSOT:818` · `BAN_DO_THUC_THI_2108.md:19` · `DUYET_GOP_2208.md:411`). Và **20/08**
chính dự án đọc đúng thế: *«Sàn mẫu ĐẠT (100 ≥ 96) nhưng `|z| = 0,480`»*.

**Phép đo tái lập được** (`_v11089_cham_lane_tb.py --chi-dem`, DB production 23/08):

```
✓ số cặp BẤT ĐỒNG : 122   [QD-059 cần ≥96]
✗ số NGÀY         : 13    [QD-017 cần ≥14]
✗ |z| McNemar     : 0.5898 [QD-059 cần ≥1.96]   z = (21−25)/√46
⛔ CHƯA ĐƯỢC PHÉP KẾT LUẬN
```

**Quyết định nào đã dựa trên số sai:** **không có** — bản sai sống ~30 phút, và lane **không
được đọc** ở cả hai bản. **Phán quyết trùng nhau, lý do khác hẳn.**

**Vì sao vẫn là lỗi NẶNG:** bản sai **nâng sàn** từ 96-trên-bất-đồng (đã đạt từ ~20/08) lên
96-trên-`b+c` (46) — **sau khi đã nhìn thấy số**. Owner khoá đúng câu này: *«CẤM tự ý đổi ngưỡng
sau khi thấy số»*. Nếu số nghiêng chiều khác, cùng thao tác đó là **dời cột gôn**.

**Và bài thử chặn KHÔNG bắt được — phần đáng sợ nhất.** Bản đầu **ĐẠT 9/9** trên chính cái
ngưỡng bịa ra. Bài thử chỉ chứng minh hàm làm **đúng điều nó được viết ra để làm**; nó **không**
kiểm được điều đó có phải điều **ĐÃ ĐĂNG KÝ**. Nay có **phép [10]** đối chiếu ngưỡng trong mã
với bản đăng ký `(96 · 1,96 · 14)` ⇒ **13/13**.

**Sức mạnh (`RM-03`):** giữ chênh lệch `−4/46 = −0,087` ⇒ cần `n ≈ 508` cặp; tốc độ `≈3,5/ngày`
⇒ **≈131 ngày nữa**. **`RM-21`:** `−0,087` đo trên `n=46`, **rất không ổn định**, có thể đổi dấu.

### 7.2 · Nâng nhầm lớp prompt, và **đã đẩy lên VPS**

Dòng gỡ nằm trong `REASONING_RULEBOOK`; em nâng `context_pack → CTX-18.7` và **đẩy lúc 21:02**,
sửa lại lúc 21:1x. Giữa hai mốc **không lượt dự đoán nào chạy** (4 bảng khoá `+0`) ⇒ **không bản
ghi nào đóng dấu `CTX-18.7`**. Lớp đúng: **`RR-16.6`**.

### 7.3 · *«Đúng một dòng, không có họ lỗi phía sau»* — **sai, có hai**

Dòng thứ hai (`WEEKLY LIVINGNESS`) mồ côi từ **07/08 — 16 ngày**, và lộ ra **hoàn toàn tình cờ**
vì bộ đếm trong script đẩy nới rộng hơn dự định. Đúng ca `RM-07`.

### 7.4 · Bản nháp cổng báo **«10 mệnh lệnh mồ côi»** — thật ra **1**

Hai lỗi, đúng hai kiểu luật đã cảnh báo: **đo thiếu nguồn** (`RM-13` — chỉ dump context pack, bỏ
thân do `create_analysis_prompt` dựng ⇒ **4 báo giả**) và **đếm chuỗi thô** (`RM-09` — nuốt cả
giá trị mẫu trong khung JSON đầu ra: `"CHOT_HA"`, `"CAO / TRUNG BÌNH / THẤP"`).

### 7.5 · Đếm khối thay vì gộp theo số hiệu

Đếm khối `FOLLOW_UP_TRACKER` ra **327**; gộp theo số hiệu ra **302** (`FU-423` một mình có **ba**
khối). Và *«hạn giữ»* bị đọc thành **thiếu hạn** ⇒ báo **27** thay vì **19**.

---

## 8 · GỠ VỀ

| việc | lệnh gỡ |
|---|---|
| `RR-16.6` | `cp /root/Lottery_AI_Test/web/backend/gpt_analyzer.py.pre_v11107 …/gpt_analyzer.py && systemctl restart lottery` |
| bộ chấm T-B | `git checkout 6a646d0 -- web/backend/_v11089_cham_lane_tb.py` |
| lớp ghi đè MN | `OVERRIDE_CONFIG["MN"]["enabled"] = False` — **một dòng, gỡ tức thì** |
| cổng prompt mồ côi | công cụ đo, **không nối vào hook** ⇒ xoá tệp là xong |

---

## 9 · THEO DÕI TIẾP

| ngày | việc | verdict nếu ngưỡng đạt |
|---|---|---|
| **24/08** | luật chống model ML giả-đa-dạng (`FU-431`) | **áp dụng ngay** |
| **24/08** | kiểm lượt 05:00 có đóng dấu `RR-16.6` ⇒ nâng verdict | `RUNTIME_PROVEN` |
| **24/08** | đo **bề mặt hiển thị** `/du-doan` MN 22/08 | khoảng trống cuối của `GĐ-0` |
| **26/08** | vá sổ gốc tự mâu thuẫn (`FU-429`) | `0/N` bundle mới vi phạm |
| **30/08** | vá bản đóng băng đối chứng (`FU-432`) — **trước 02:00** | đủ 12/12 tệp |
| **31/08** | rà lớp ghi đè MN (`FU-183`) — **thước TIỀN** | MN âm tiền ⇒ `enabled=False` |
| **31/08** | dựng cổng chặn bundle đổi số không khai lớp | thử chặn hai chiều đạt |
| **13/09** | ML MB `AUC < 0,50` **ba lần liên tiếp** (`FU-430`) | **BỎ CỜ** ML MB |
| **30/09** | `smart-ml` vs `random-forest` | điểm `≤ 0` ⇒ **BỎ CỜ** |
| **06/11** | cadence: đóng băng vs học tuần (`FU-285`) | ngang nhau ⇒ **cắt học lại hằng tuần** |

**Chưa kiểm được:** P&L (tiền) cho mọi phép trên · `combo-super` chọn model nào mỗi ngày ·
`chooser="specialist"` chọn số theo luật nào · `PP1`/`PP5` đổi thứ hạng bao nhiêu lần ·
nguyên nhân gốc 3 model ML trùng nhau.

---

## §62 (A60) — BA LỚP NGUỒN

### `OWNER_SAID`

> *«PROMPT TỔNG LỰC LẦN 30 — 24/08: AUDIT CỰC GẮT»* — sáu chất vấn, nguyên văn ở §2.
> *«đo hoài không ra»* · *«ML phải fix TỪ GỐC (model đơn sinh số trúng) TỚI NGỌN (cơ chế lấy
> total)»* · *«CẤM tự ý đổi ngưỡng sau khi thấy số»* *(lệnh `GĐ-3` lần 29, còn hiệu lực)*.

### `CODE_DID`

| điều | bằng chứng |
|---|---|
| lớp ghi đè MN **đang BẬT** | `_v10640_official_perslice_override.py:28` · `main.py:10059–10072` |
| `top1_reason` dựng từ số **trước** ghi đè | `main.py:10189` · `main.py:10199` |
| ML MB `AUC < 0,50` | `training_history`, 13 lần học × 3 model |
| lane T-B: bất đồng 122 ✓ · 13 ngày ✗ · `\|z\|` 0,59 ✗ | `_v11089_cham_lane_tb.py --chi-dem` |
| prompt: **0** mệnh lệnh mồ côi | `_v11107_cong_prompt_mo_coi.py` |
| deploy | PID `2299279 → 2317479 → 2320523` · 4 bảng khoá `+0` |
| commit | `8ca990d` · `0cb5e78` — **xác nhận trên remote** |

### `DOC_SAID`

| nguồn | ghi gì | lệch không |
|---|---|---|
| `SSOT:818` · `BAN_DO_THUC_THI_2108.md:19` · `DUYET_GOP_2208.md:411` | *«≥96 cặp bất đồng VÀ `\|z\| ≥ 1,96`»* | **KHỚP** — và chính chỗ này lật bản vá `FU-427` đầu |
| `_v10640…:62-64` | *«MN âm tiền 30 ngày (rà 31/08) thì tắt nốt»* | **KHỚP** — ngày quyết định đã có sẵn |
| `RM-18` (`CLAUDE.md`) | nền `1 − (1−b)^k` | 🔴 **LỆCH** — công thức **có hoàn lại**, đúng phải là siêu bội |
| `CHANGELOG` `V11107` bản đầu | *«`b+c` mới là số so với ngưỡng»* | 🔴 **LỆCH** — đã rút lại §7.1 |

**Ba lớp lệch nhau ⇒ hai finding, đã báo, không giấu:** `RM-18` ghi công thức sai (§3.6) ·
`V11107` bản đầu đổi ngưỡng (§7.1).

---

**TanPhatAI cần làm:** cập nhật `docs/FOLLOW_UP_TRACKER.md` cho `FU-429` (đã có gốc bệnh
`main.py:10189`) và bốn mục mới `FU-430/431/432/433`; ghi vào sổ **năm mốc quyết định gần nhất**
— **24/08** luật ML giả-đa-dạng + kiểm `RR-16.6` + đo bề mặt `/du-doan`, **26/08** vá `FU-429`,
**30/08 trước 02:00** vá bản đóng băng `FU-432`, **31/08** rà lớp ghi đè MN bằng **thước TIỀN**
(`FU-183`), **13/09** ML MB; theo dõi `docs/SO_YEU_CAU_OWNER_20260824.md` — **19 mục thiếu hạn**
và **50 mục thiếu ngưỡng số** cần owner đặt; và **sửa `RM-18` trong cả sáu mặt quản trị** vì
công thức nền hiện đang ghi sai.
