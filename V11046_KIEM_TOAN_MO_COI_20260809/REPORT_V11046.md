# REPORT V11046 — KIỂM TOÁN MỒ CÔI: TRUY NGUỒN GỐC TRƯỚC KHI GỠ

**Ngày:** 2026-08-09 11:00–12:30 · **Tầng verdict:** `RUNTIME_PROVEN` cho phần đã gỡ + deploy ·
`REPORT_PROVEN` cho phần đề xuất

---

## 1. Tóm tắt

Owner hỏi đúng cách: *«em có nắm tại sao mồ côi và lý do mồ côi, trước đó dùng để làm gì hiện tại
cần ko? có cần đấu nối đo lại với time line khác không hay thực sự mồ côi»*.

Truy nguồn gốc từng thứ theo sáu câu bắt buộc. Kết quả **lật ngược ba kết luận trước đó của
agent**, trong đó **một là lỗi làm owner ký nhầm**.

| kết luận | số thứ |
|---|---|
| **MỒ CÔI THẬT** → đã gỡ / đề xuất gỡ | 5 |
| **KHÔNG mồ côi — đang được dùng SỐNG** (agent báo sai) | 3 |
| **KHÔNG mồ côi — «đồ tốt bỏ quên»**, phải đưa vào kho | 1 |
| **Phụ thuộc CHẾT đang được dùng SỐNG** — nguy hơn mồ côi | 1 |

---

## 2. Owner yêu cầu gì (nguyên văn)

> Anh và em cùng 1 suy nghĩ với các mồ côi, nhưng em có nắm tại sao mồ côi và lý do mồ côi, trước
> đó dùng để làm gì hiện tại cần ko? có cần đấu nối đo lại với time line khác không hay thực sự
> mồ côi. Mồ côi thực sự thì gỡ luôn cho tinh gọn và nhất quán nha em. Sau đó đẩy báo cáo chi tiết
> kèm đề xuất xử lý an toàn nhất quán đảm bảo cải tiến nâng cao dự đoán nha em

---

## 3. Đào bới / phát hiện

### 3.1 ❌ LỖI CỦA AGENT — owner đã ký đóng 3 mục bằng tiền đề SAI

09/08 lúc 00:33 agent trình bảng 57 mục; owner ký. Ba mục đóng với lý do **agent tự viết**:
*«chờ bảng đã ngừng nhận dòng: `v94_cross_region_spillover_aware_shadow` /
`verdict_weight_recalibration_shadow`»*.

**Đo lại production:**

| bảng | dòng | mới nhất | thật ra |
|---|---|---|---|
| `v93_verdict_weight_recalibration_shadow` | **3.775** | 2026-08-08 | **SỐNG**, ghi 19:16 mỗi ngày, 122 ngày liên tục |
| `v94_cross_region_spillover_aware_shadow` | **13.278** | 2026-08-08 | **SỐNG**, ghi 19:18 mỗi ngày |

Cả hai **đang được ba endpoint sống đọc** (`_v95_dashboard` · `_v98_command_center` ·
`_v96_master_tracker`).

**Nguyên nhân lỗi:** agent quét tên `verdict_weight_recalibration_shadow` **thiếu tiền tố `v93_`**
rồi kết luận «KHÔNG CÓ BẢNG» — đúng **RM-10**, quy tắc agent đã tự trích hai lần trong hai ngày.

⇒ `FU-160` `FU-162` `FU-164` **đã MỞ LẠI** (`AWAITING_OWNER_OK`, hạn `LX`).
**Chữ ký owner không sai — dữ kiện agent đưa mới sai.**

### 3.2 ⚠ `model_strength_by_region_weekday_station_daily` — PHỤ THUỘC CHẾT ĐANG DÙNG SỐNG

Không phải mồ côi. **Nguy hiểm hơn mồ côi.**

- **Sinh:** V52.5.1 — xếp sức mạnh model theo (miền, thứ, đài) để chọn voter.
- **Vì sao đứng im:** **chưa bao giờ có tự động hoá** — 0 dòng crontab, 0 import; chỉ chạy tay
  hai đợt forensic. 17.815 dòng **không phải 17.815 ngày**: chỉ **2 anchor_date**, cùng
  `computed_at` trong **2 giây** ngày 2026-05-10. Fan-out 4 window × 3 grain × 41 đài.
- **Đang được dùng SỐNG:** `_materialize_du_doan_test_model_budget.py:205/277` chạy **mỗi ngày**
  qua `scheduler.py:6928`. **374/616 dòng voter 7 ngày qua (61%)** nhận `strength_score` tính từ
  tensor **cũ 96 ngày**. Không triệu chứng, số vẫn ra đẹp — **RM-01**.
- **Lookahead: SẠCH.** `_date_iter()` cửa sổ **lùi hoàn toàn**; docstring: *«anchor defaults to
  "yesterday" … so the snapshot is live-available»*.
- ⚠ **BẪY phải vá TRƯỚC khi nối lại:** biên consumer là `WHERE anchor_date <= ?` — **cho phép
  `anchor == date`**. Hôm nay vô hại (anchor kẹt 05-05). Bật lại hằng ngày với anchor = hôm nay
  thì **kết quả ngày T rò vào việc chọn model cho ngày T**. Phải đổi `<= date(?, '-1 day')`.
- **Giá trị không nằm ở 17.815 dòng cũ** — nằm ở **7.785 dòng / 96 ngày bằng chứng chưa gộp**, và
  ở chỗ script **vẫn chạy được**.

### 3.3 🎯 PHÁT HIỆN LỚN NHẤT CHO «CẢI TIẾN NÂNG CAO DỰ ĐOÁN»

`loz_stage_trace_shadow` (6.356 dòng, 62 ngày) trả lời câu **không bảng nào khác trả lời được**:
đuôi trúng thật bị mất ở **khâu nào**?

| miền | chưa model nào sinh ra | lỗi chọn dòng lô | lỗi pool | trúng ra output |
|---|---|---|---|---|
| MN | **2.302 (85,4%)** | 226 | 107 | 60 (2,2%) |
| MT | **1.852 (84,6%)** | 188 | 93 | 55 (2,5%) |
| MB | **1.240 (84,2%)** | 125 | 77 | 31 (2,1%) |

> **~85% đuôi trúng CHƯA BAO GIỜ được model nào sinh ra.**
> Nút thắt **không phải khâu chọn** — là khâu **sinh / độ phủ**.
> Mọi công sức tỉa bộ chọn chỉ đang giành nhau trong **15%** còn lại.

Đây là câu trả lời **có bằng chứng** cho *«đảm bảo cải tiến nâng cao dự đoán»*: hướng đang đầu tư
(tỉa bộ chọn, xếp hạng model) chạm được **tối đa 15%** dư địa.

### 3.4 `model_latency_cost_audit_daily` — SỐ HẠNG CHẾT TRONG CÔNG THỨC SỐNG

4.033 dòng, **100% `latency_available = 0`**, `rows_with_real_latency = 0`. Hệ quả:
`_latency_score()` trả **hằng số 0,50** cho **2.855/2.855 dòng** từ 01/07. Một số hạng **chết**
trong công thức chấm điểm C-16 **đang chạy** — tạo ảo giác «có cân nhắc độ trễ».
Sửa được phải đụng `gpt_analyzer.py` — **QD-041 khoá tới 21/08**.

### 3.5 Dây chuyền `viewer` — MỒ CÔI THẬT, 94 ngày

**Thủ phạm:** commit **`d411670` · 07/05 · V83** cắt route trang thành redirect nhưng **để
nguyên** `viewer.html`, `viewer.js`, route `/viewer.js`, hai endpoint `/api/viewer/*`.
Đây là §60 «bỏ nửa chừng» ở quy mô lớn nhất kho.

**Bằng chứng chết:** nhật ký nginx **15 bản xoay · 56.465 dòng · 26/07 → 09/08**:
`/viewer.js` **0 hit** · `/api/viewer/*` **0 hit** · `/viewer` **2 hit** — và hai hit đó là
**công cụ tự kiểm của chính agent** (cùng IP, `curl` rồi `HeadlessChrome`, cách 46 giây, trùng
commit V10866). Đối chiếu: `/du-doan` **3.663 hit**, `/user-view` **245 hit**.

**Lãng phí đo được:** **15 commit** sửa `viewer.html` **sau khi nó đã chết**, gồm trọn đợt reskin
UI v2 «14 trang production live».

**Dữ liệu cứu được: KHÔNG CÓ GÌ ĐỂ CỨU** — dây chuyền **không sở hữu bảng nào**, chỉ là wrapper
mỏng gọi ba hàm dùng chung trên `predictions` (bảng sống, 12.078 dòng, ghi tới hôm nay).

### 3.6 `__trigger_reload__.py` — MỒ CÔI THẬT, phụ thuộc chết

133 byte, sinh **bởi API deploy** 16/04 để chạm tệp kích `uvicorn --reload`. Nhưng service chạy
`main.py:21270` `uvicorn.run(app, ...)` — **không có `reload=True`**. Watcher nó nhắm tới **không
tồn tại**. Chạm tệp này không gây ra bất cứ điều gì.

### 3.7 `_shadow_phase_audit.py` — KHÔNG mồ côi, «đồ tốt bỏ quên»

Chưa bao giờ ở trong git (`git log --all` = rỗng), tạo thẳng trên VPS 17/04. Nhưng cơ chế nó soi
**vẫn sống trong production**: `gpt_analyzer.py:1109-1125` vẫn **bắt buộc** ba trường nó kiểm.
**Vẫn chạy được, chỉ không ai gọi.** Phải **đưa vào kho**, không phải gỡ.

### 3.8 `v94_cross_region_spillover` — SỐNG, SẠCH, nhưng CHƯA có lợi thế

Lookahead **sạch** (chỉ dùng miền thượng nguồn đã xổ trước trong ngày, đúng thứ tự MN→MT→MB).
Nhưng đo 122 ngày với nền đúng từng miền (RM-18):

| | n | chênh vs nền | z | kết luận |
|---|---|---|---|---|
| MT rank-1 | 122 | +2,33pp | +0,54 | chưa được phép kết luận |
| MB rank-1 | 122 | **−4,02pp** | −1,04 | chưa được phép kết luận |
| MT is_hit | 5.235 | −0,22pp | −0,34 | **bằng 0** |

Cần **~3.300 ngày** để đủ sức mạnh, đang có 122. Thêm: `DEFAULT_LIFT_30D` là **hằng số ghi cứng**
tháng 5 nằm trong cột tên `empirical_lift_30d_pp`, và vì không đổi trong một miền nên **không ảnh
hưởng xếp hạng**. **Giữ chạy, KHÔNG promote.**

---

## 4. Hướng xử lý và vì sao chọn

Owner cho phép *«mồ côi thực sự thì gỡ luôn»*. Agent **chỉ gỡ thứ đã chứng minh đủ sáu câu**, và
**không đụng** thứ nào chạm `logic chọn số` — QD-041 khoá tới 21/08. Cụ thể **không gỡ**
`latency_score` dù nó là số hạng chết, vì nó nằm trong công thức chấm điểm C-16.

Nguyên tắc phân biệt rút ra từ phiên này:

| dấu hiệu | kết luận |
|---|---|
| không ai gọi **và** không sở hữu dữ liệu **và** phụ thuộc đã chết | **mồ côi thật** → gỡ |
| không ai gọi **nhưng** cơ chế nó soi còn sống | **đồ tốt bỏ quên** → đưa vào kho |
| có người gọi **nhưng** nguồn đứng im | **phụ thuộc chết đang dùng sống** → nguy nhất, phải vá |
| dữ liệu còn **nhưng** sinh sau khi biết kết quả | **nhiễm lookahead** → không cứu |

---

## 5. Đã làm gì

### Đã GỠ + DEPLOY

| gỡ | bằng chứng |
|---|---|
| `web/frontend/viewer.js` | 0 hit / 56.465 dòng nhật ký |
| route `/viewer.js` (`main.py`) | như trên |
| endpoint `/api/viewer/predictions` | 0 hit |
| endpoint `/api/viewer/today` | 0 hit |
| `__trigger_reload__.py` (VPS) | watcher không tồn tại |
| 3 chỗ trỏ `viewer.html` **V11043 bỏ sót** | `_full_audit.py:10` · `_cache_bust.ps1:7` · `_mega_fix.ps1:8` |

**GIỮ** route `/viewer` (redirect 307 → `/du-doan`) — đường lùi cho bookmark cũ.

**Deploy:** PID **1141956 → 1157897** · health **200** · `/du-doan` **200** · `/monitoring` **401**
· `/viewer.js` **404** · `/api/viewer/today` **404** · `/viewer` **307**.

### Đã MỞ LẠI

`FU-160` · `FU-162` · `FU-164` → `AWAITING_OWNER_OK`, hạn `LX` (RM-06, không tự đặt hạn).

---

## 6. Cổng kiểm

`_v11015_cong_chan_cat_cut` **0** · `main.py` **PARSE OK** local + `py_compile` trên VPS ·
quét ngược §60.2 sau khi gỡ: chỉ còn **chú thích** và **script một lần lịch sử** (`_v10848_*`,
không cron — giữ làm vết, đúng phân loại `CHU_THICH` §60.3).

---

## 7. Vướng vấp

**7.1 — Agent báo sai «KHÔNG CÓ BẢNG» và owner ký nhầm vì thế.** Xem §3.1. Đây là lỗi nặng nhất
phiên: một phép quét hỏng làm hỏng cả một quyết định đã ký.

**7.2 — Agent điều tra báo «lỗ hổng bảo mật đang mở» ở `/api/viewer/*`. SAI.** Agent chính kiểm
độc lập: cả hai trả **401 Not authenticated** (`main.py:4282` `get_current_user(request)`).
Nếu chép lại lời agent thì đã báo owner một lỗ hổng không tồn tại. Điểm còn lại chỉ là **thiếu
nhất quán** (đường này không kẹp freeze như `/user-view`) — nay đã hết vì endpoint bị gỡ.

**7.3 — V11043 khai «xử 5 chỗ» nhưng bỏ sót 3.** Nay đã dọn.

**7.4 — Agent từng gọi 17.815 dòng là «vàng».** Sai: chỉ **2 anchor**, tính trong 2 giây. Giá trị
thật nằm ở 96 ngày **chưa gộp**, không ở dòng cũ.

---

## 8. Gỡ về

```bash
cp backups/v11044_pre/main.py web/backend/main.py
cp backups/v11044_pre/viewer.js web/frontend/
ssh root@14.225.224.89 'cd /root/Lottery_AI_Test && mv backups/v11046_viewer/viewer.js web/frontend/ && systemctl restart lottery'
git revert <commit V11046>
```

---

## 9. Theo dõi tiếp — ĐỀ XUẤT XỬ LÝ AN TOÀN

### 🖊️ Xin owner ký

| # | việc | vì sao | khi nào |
|---|---|---|---|
| 1 | **Vá biên `<= date(?, '-1 day')`** rồi **bật lại tensor hằng ngày** | 61% dòng voter đang ăn số 96 ngày tuổi; và bật lại **mà không vá biên trước** sẽ **tạo lookahead mới** | vá biên **ngay** · bật lại **sau 21/08** |
| 2 | **Đưa `_shadow_phase_audit.py` vào git** | code chạy được, cơ chế nó soi vẫn sống, mất máy là mất hẳn | ngay |
| 3 | **Gỡ `model_latency_cost_audit_daily` + số hạng `latency_score`** | 100% dòng rỗng tín hiệu; `latency_score` là hằng 0,50 | **sau 21/08** (chạm logic chọn) |
| 4 | **Gỡ `weekday_blackspot_shadow`** (42 dòng, n = 4–5) | RM-04: n = 4–5 là «chưa được phép kết luận» | ngay |
| 5 | **Gỡ `mt_model_hit_output_drop_shadow` + panel** | panel **chắc chắn rỗng**: biên `-59 ngày` = 11/06 > dữ liệu cuối 06/05 | ngay |
| 6 | **Chạy lại `_materialize_loz_stage_trace_shadow` trên 96 ngày mới** | để có lại con số «85% chưa sinh ra» **trên roster hiện tại** | ngay (read-only, không chạm output) |

### 🎯 Đề xuất CẢI TIẾN DỰ ĐOÁN — có ngưỡng đo được, không hứa bằng lời

**Hướng 1 — ĐỘ PHỦ, không phải bộ chọn.** Bằng chứng: ~85% đuôi trúng chưa model nào sinh ra.
Trước khi tỉa thêm bộ chọn, phải đo lại con số đó trên roster hiện tại (mục 6).
*Ngưỡng:* nếu vẫn **≥80%** ⇒ **dừng mọi việc tỉa bộ chọn**, chuyển sang mở rộng độ phủ.

**Hướng 2 — chọn model theo (miền × thứ × đài) thay vì một số trung bình.** Hiện `combo_super`
dùng **đúng một** `unified_wr` 7 ngày/miền; chuỗi `model_strength` xuất hiện **0 lần** trong tệp
đó. Tensor giữ đúng chiều còn thiếu (5.788 dòng × 7 thứ · 10.972 dòng × 41 đài) và **sạch
lookahead**. C-16 **không thay thế được** chiều này — nó là bảng ngân sách, không phải bảng sức mạnh.
*Ngưỡng:* sau khi bật lại tensor + vá biên, đo A/B **≥30 ngày**; chọn-theo-thứ phải hơn nền
**≥3pp với z ≥ 1,96** mới nhận. **Chỉ được làm sau 21/08** (QD-041).

**Hướng 3 — KHÔNG promote `v94_spillover`.** Đo 122 ngày: MT +2,33pp `z = 0,54`, MB **−4,02pp**.
Cần ~3.300 ngày. Giữ chạy để tích dữ liệu, **cấm dùng làm căn cứ**.

---

## LOCK-IN / OPEN / NEXT ACTION

**LOCK-IN:** dây chuyền viewer gỡ sạch + deploy, health 200 · `__trigger_reload__` gỡ · 3 chỗ
V11043 bỏ sót đã dọn · `FU-160/162/164` mở lại · `/viewer` giữ redirect làm đường lùi ·
tensor xác định **sạch lookahead** nhưng biên consumer có **bẫy phải vá trước**.

**OPEN:** sáu mục xin owner ký ở §9 · và **con số 85%** cần đo lại trên roster hiện tại trước khi
quyết hướng đầu tư.

**NEXT ACTION:** vá biên `anchor_date` (ngay — chống lookahead) · đưa `_shadow_phase_audit.py` vào
git · chạy lại `loz_stage_trace` trên 96 ngày mới · tối nay đọc log 18:05 + 19:35 để đóng
`FU-373` và `FU-366`.

*Đẩy cùng commit (A55 · §57.2).*
