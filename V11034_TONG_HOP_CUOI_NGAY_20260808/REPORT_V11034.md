# REPORT V11034 — TỔNG HỢP CUỐI NGÀY 08/08

**Ngày:** 2026-08-08 tối · **Loại:** audit cuối chu kỳ live · **CHỈ ĐỌC**
19 agent soi + phản biện đối kháng · đo **thẳng trên VPS** (`mode=ro`, `timeout=30`)

---

## 1. Tóm tắt

**MT thắng · MN và MB trượt · hệ khoẻ không lỗi runtime · bản vá đã ăn vào đường chạy thật —
nhưng CHƯA ĐƯỢC PHÉP nói nó tốt hay xấu.**

Và **agent phải đính chính chính lời mình** nói lúc 18:40.

| | |
|---|---|
| **Đính chính** | *"MN chạy prompt HỎNG"* — **SAI**. 11/12 lượt 64 ký tự là **shadow**; MN official chạy prompt **chưa vá nhưng LÀNH** (8.797 ký tự, giữa dải bình thường) |
| **Phát hiện quý nhất** | MN **trượt đúng MỘT BẬC** — top-10 có **9/10 số trúng** (kỳ vọng 5,3). **Bộ sinh tốt, hỏng ở XẾP HẠNG** |
| **Lỗi thật hôm nay** | `deepseek-reasoner` MT lỗi JSON **hai ngày liên tiếp**; cổng canh đã viết nhưng **chưa deploy** |
| **Cạm bẫy thống kê** | `n=16` là **ảo** — n hiệu dụng **4,8–6,1**. MB ở cỡ này **dù 0/16 cũng không bao giờ đạt ý nghĩa** |
| **Sai đếm** | 3 model là **bản sao tất định** của 4 bộ sinh ⇒ mọi phép đếm "7 model NO_TOKEN" là **đếm trùng** |

---

## 2. Owner yêu cầu gì (NGUYÊN VĂN)

> Hết chu kỳ live rồi em kiểm tra phân tích đánh giá dự đoán hôm nay dùm anh nha em, sau đó
> tổng hợp đầy đủ và đề xuất xử lý tiếp dùm anh nhé em

---

## 3. Đào bới / phát hiện

### 3.1 ĐÍNH CHÍNH — MN official KHÔNG chạy prompt hỏng

Agent lúc 18:40 báo *"MN chạy prompt HỎNG được 68,8%, MB chạy prompt ĐÃ VÁ được 6,2%"*.
Bóc 12 lượt 64 ký tự ngày 08/08:

| | |
|---|---|
| **11/12 là SHADOW** | `run_source='shadow_auto_eval'`, 05:33–05:41 — **bị loại khỏi 16 lượt chấm** |
| **1 lượt official** | `gpt-oss-120b` MN **05:17:21** |
| **7/8 model TOKEN official MN** | gói **8.797 ký tự**. Nền MN 7 ngày trước: 9.009 · 8.847 · 8.552 · 8.919 · 8.979 · 8.929 · 8.307 ⇒ **nằm giữa dải bình thường** |

**Phơi nhiễm là biến theo MODEL, không theo MIỀN.** Quét 25/07–08/08: model official **duy
nhất** từng dính lỗi 64 ký tự là `gpt-oss-120b`, **8 ngày rải đều cả ba miền**.
Chia nhóm theo miền là **sai hai tầng**.

### 3.2 Kết quả ba miền

| miền | BT | kết quả | đồng thuận | đáng nói |
|---|---|---|---|---|
| **MT** | **42** | ✅ **WIN** | `moderate` (12) | số 42 chỉ **3 phiếu** mà trúng |
| MN | 69 | ❌ LOSE | `strong` (15) | **trượt đúng MỘT BẬC** |
| MB | 93 | ❌ LOSE | `strong` (15) | số trúng đầu tiên mãi **hạng 6** |

**Hai miền `strong` trượt cả hai; miền thắng lại là miền đồng thuận thấp nhất.**

### 3.3 MN — bộ SINH tốt, hỏng ở XẾP HẠNG

Top-10 MN có **9/10 số trúng**, kỳ vọng theo nền chỉ **5,3**.
BT hạng 1 số **69** — 4 phiếu · 0,1184 điểm — **TRƯỢT**.
Hạng 2 số **43** — **5 phiếu** · 0,1037 — **TRÚNG**.

**Số nhiều phiếu hơn lại xếp dưới.** Đây là chỗ đáng đào nhất, nhưng **n = 1 ngày**.

### 3.4 Tỉ lệ bạch thủ — luôn kèm nền và MDE

| miền | trúng | tỉ lệ | **nền** | chênh | z (÷√VIF 2,92) | **MDE** |
|---|---|---|---|---|---|---|
| MN | 11/16 | 68,8% | **53%** | +15,7 | +0,74 | **45,8 điểm** |
| MT | 8/15 | 53,3% | **43%** | +10,3 | +0,47 | **51,4 điểm** |
| MB | 1/16 | 6,2% | **25%** | −18,8 | −1,01 | **51,5 điểm** |

Chênh quan sát **thấp hơn ngưỡng đọc được 3–5 lần** ⇒ cả ba **NGANG NỀN** (RM-04).

**`n = 16` là ảo:** MN 16 model chỉ ra **8** số BT khác nhau · MT 15 ra **7** · MB 16 ra **7**.
**n hiệu dụng 4,8 – 6,1.**

> **Điểm mạnh nhất về MB:** ngưỡng bác bỏ chiều giảm ở n=16 là **p ≤ −11,3%** — **dù MB có 0/16
> cũng KHÔNG BAO GIỜ đạt ý nghĩa thống kê**. MB ở cỡ mẫu này **về cấu trúc không thể kiểm được**.

### 3.5 ⚠ BA MODEL LÀ BẢN SAO TẤT ĐỊNH

`combo-no-token` · `smart-ml` · `smart-ensemble` = hàm tất định của 4 bộ sinh.

| miền | đếm thô (7) | **đếm đúng (4)** | so nền |
|---|---|---|---|
| MN | 6/7 = 85,7% | **4/4** | +47,0 |
| MT | 1/7 = 14,3% | **1/4** | −18,0 |
| MB | 1/7 = 14,3% | **1/4 = 25,0%** | **+0,0 — ĐÚNG BẰNG NỀN** |

### 3.6 Lỗi thật: `deepseek-reasoner` MT

`Expecting value: line 7 column 18` · chạy **230,3 giây** · `main_numbers='[]'`.
**API CÓ trả lời** — không timeout, không API chết. **Lặp 07/08 và 08/08.**

30 ngày: `deepseek-reasoner` **3/90 = 3,3%** (MT **2/30 = 6,7%**) · `gpt-5.4` 1/88 ·
`gpt-5-mini` 1/67.

**Cổng `_v11023_canh_thieu_so.py` ĐÃ VIẾT nhưng CHƯA DEPLOY** — quét toàn ổ VPS **0 kết quả**,
không cron. Sổ ghi `DEPLOYED_PENDING_LIVE_VERIFY` là **SAI TẦNG** (RM-12) — thật là `CODE_PUSHED`.

### 3.7 Hệ khoẻ

PID **1053968** · uptime 4h50m · **`NRestarts=0`** · health **200** · journal 24h **1 ERROR** ·
`database is locked` **0 lần hôm nay** · đĩa 69% · DB 645M.
4 bảng khoá: `predictions` +40 · `final_bundles` +2 · `lottery_results` +8 ·
`model_daily_eval` **+0** (job 20:15 chưa chạy lúc đo).
Bộ tự kiểm 18:05: **2 LỆCH**, cả hai từ **cùng sự kiện `MT 2026-08-04`** — đúng FU-256.

### 3.8 Hai mục vô hình với máy

`FU-325` và `FU-317` có `due_date = None` ⇒ **rơi khỏi mọi bộ đếm hạn**.
Gốc: `_han_cua_khoi()` không đọc được dạng hạn của hai khối đó.
`FU-347` trích **sai số dòng** — «39 đặc trưng vs 33» ở dòng **664**, không phải 533.

---

## 4. Hướng xử lý và vì sao chọn

**Chọn: KHÔNG SỬA GÌ TỐI NAY.** Ba lý do:

1. Phát hiện quý nhất (**MN hỏng ở xếp hạng**) đứng trên **n = 1 ngày**. Sửa bộ xếp hạng bây
   giờ là đúng thứ **RM-04** cấm.
2. Bộ xếp hạng thuộc **bộ chọn số** ⇒ `QD-041` khoá tới 21/08.
3. Thêm bất kỳ biến nào tối nay là **biến thứ ba** chồng lên V11032/V11033 — `QD-018` cấm.

**Việc duy nhất đáng làm sớm** là deploy cổng canh model thiếu số (`_v11023`) — nó là **cổng
kiểm**, không đụng đường ra số, và bệnh nó bắt **vừa xảy ra hai ngày liên tiếp**.

---

## 5. Đã làm gì

**KHÔNG SỬA GÌ.** Đã làm:

| | |
|---|---|
| Cổng tuổi dữ liệu | local cũ **10,11 giờ** ⇒ **TỪ CHỐI** ⇒ đồng bộ lại. Lượt 18:34 hỏng («database is locked»), lượt **18:39:07 thành công** |
| Đo thẳng trên VPS | mọi con số từ `/root/Lottery_AI_Test/data/lottery_ai.db`, `mode=ro`, `timeout=30` |
| 4 mũi soi + 14 phản biện | chấm kết quả · hiệu lực bản vá · sức khoẻ hệ · tồn đọng |
| Ghi 3 mặt tài liệu | `CHANGELOG` · `SSOT` · `FOLLOW_UP` (FU-350 → FU-354) |

---

## 6. Cổng kiểm

| cổng | kết quả |
|---|---|
| **Tuổi dữ liệu (RM-01)** | **CHẶN đúng** lúc 10,11 giờ · sau đồng bộ **`DU_LIEU_TUOI` 0,00 giờ** |
| Không sửa production | **ĐẠT** |
| Không mutation DB | **ĐẠT** — mọi kết nối `mode=ro` |
| 4 bảng khoá | tăng tự nhiên trong ngày, không dòng nào bị ghi đè |
| `_v11028_cong_dong_bang` | **ĐẠT** — `DONG_BANG_QD041=CON_NGUYEN` |
| `_v11034_kiem_cheo_quyet_dinh` | **ĐẠT** — `KIEM_CHEO_QD=SACH` |
| Bộ tự kiểm 18:05 | 2 LỆCH, **cùng một sự kiện cũ** (FU-256) |

---

## 7. Vướng vấp

**7.1 — Agent nói SAI và phải tự đính chính.** Tiền đề *"MN chạy prompt hỏng"* sai vì **không
lọc `run_source`** — 11/12 lượt 64 ký tự là shadow. Đây đúng bẫy đã ghi trong sổ RM nhiều lần:
**quên lọc dòng shadow**.

**7.2 — Đồng bộ thất bại lúc 18:34** («database is locked»). Nhưng đo kỹ: `database is locked`
xuất hiện **0 lần hôm nay** trong cả hai log job. Lượt 18:34 chỉ **trùng khoảnh khắc**; 18:39
đã qua. **Không phải bệnh hệ thống như FU-253 mô tả.**

**7.3 — `n=16` từng bị chính agent dùng như mẫu độc lập.** Thật ra model **xúm chọn cùng số**,
n hiệu dụng chỉ **4,8–6,1**. Mọi phép đo theo ngày phải dùng n hiệu dụng.

**7.4 — Ba model bản sao làm lệch mọi phép đếm nhóm.** Đếm thô cho MB NO_TOKEN 14,3% (nghe như
hỏng); đếm đúng **25,0% = đúng bằng nền**.

**7.5 — Bộ canh trôi đặc trưng chạy local ra «CHƯA ĐỦ MẪU»** vì máy local **không có `numpy`**
và `pip` bị chặn SSL. Nó **chỉ chạy được trên venv VPS**. Phải ghi vào tài liệu, nếu không
phiên sau sẽ tưởng dữ liệu thiếu.

---

## 8. Gỡ về

Không cần — phiên này **không sửa gì**. Ba mặt tài liệu chỉ **thêm vào đầu tệp**.

---

## 9. Theo dõi tiếp

| mã | nhãn | hạn | trạng thái |
|---|---|---|---|
| **FU-350 · SC0908** | `deepseek-reasoner` MT lỗi JSON 2 ngày liên tiếp; cổng chưa deploy | 09/08 | `MEASURED_ROOT_CAUSE` |
| **FU-351 · DO0914** | MN trượt đúng một bậc — nghi bộ XẾP HẠNG | 14/09 | `MEASURED_BUT_NOT_FIXED` |
| **FU-352 · TK0808-4** | ba model là bản sao tất định — mọi phép đếm nhóm sai | 08/08 | `MEASURED_BUT_NOT_FIXED` |
| **FU-353 · SC0908-2** | FU-325 + FU-317 mất hạn với máy; FU-347 sai số dòng | 09/08 | `MEASURED_ROOT_CAUSE` |
| **FU-354 · QD0909** | 4 quyết định «SAU 08/08» va chạm QD-041 | 09/08 | `OWNER_DECISION_NEEDED` |

### LOCK-IN

- Bản vá **RUNTIME_PROVEN**: 0/39 lượt hỏng sau deploy 13:47:38, prompt +1.620 ký tự (trung vị)
- `gpt_analyzer.py` md5 `c60ab13ba9bb83e35e6366f07002db74` · `CTX-18.3` · khoá tới 21/08
- Cả ba miền hôm nay **NGANG NỀN** — không miền nào được ghi là tốt hay tệ

### NEXT ACTION — một bước

**Sáng 09/08: deploy cổng `_v11023_canh_thieu_so.py` + gắn cron sau mốc chốt từng miền
(16:05 / 17:05 / 18:05), cho nó GHI VÀO BẢNG thay vì chỉ in màn hình.**
Nghiệm thu: chạy với ngày **08/08** phải ra **ĐỎ** (bắt được `deepseek-reasoner` MT).

### Câu cần owner ký

**FU-354** — *"Ba quyết định QD-015/016/017 anh ký «sau 08/08» đều cần chạm prompt, mà QD-041
khoá tới 21/08. Anh cho dời cả ba sang 21/08 không?"*
