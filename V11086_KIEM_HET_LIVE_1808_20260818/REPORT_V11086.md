# REPORT V11086 — KIỂM HẾT LIVE 18/08: **1/3 ĐÚNG BẰNG NỀN**, VÀ SỐ THỨ HAI CỦA LÔ2 CŨNG KHÔNG THÊM GÌ

**Ngày:** 2026-08-18 · **Mã đọc:** `KS1808-4` · **Read-only** — không sửa mã, không DB, không deploy.
Dữ liệu: đồng bộ sống **18:34**, sau khi MB về `18:32`.

---

## 1. Tóm tắt

**Hôm nay 1/3 bạch thủ** — MN `67` trúng, MT `71` và MB `91` trật. Kỳ vọng theo nền là **0,97**
⇒ **đúng bằng nền**, không hơn không kém.

**Phép đo MỚI của phiên này:** số **thứ hai** của lô2 có mang thông tin gì không?
Kết quả — **bộ 2 số phủ 55,2% so với nền đúng của bộ 2 số là 55,6%** ⇒ **−0,35pp**,
`CI95 [−4,5 · +3,8]` trên **n = 516** miền-ngày. Số thứ hai **thêm đúng bằng phần một lựa chọn
ngẫu nhiên thêm được**.

Bốn cửa sổ của bạch thủ **gần như không đổi** so với hôm qua, và **dấu vẫn đổi theo cửa sổ**.

---

## 2. Owner yêu cầu gì (nguyên văn)

> *«Còn gì để xử lý, phân tích đánh giá kết quả dự đoán hôm nay dùm anh.»*

---

## 3. Đào bới / phát hiện

### 3.1 · Kết quả 18/08 — kiểm từ `prizes_json`, không từ cột trạng thái

| miền | chốt | bạch thủ | nền ngày đó | kết quả | lô2 số thứ hai |
|---|---|---|---|---|---|
| **MN** | 05:18 | `67` | **42%** | **✓ TRÚNG** | `54` ✗ |
| **MT** | 16:50 | `71` | **29%** | ✗ trật | `25` ✗ |
| **MB** | 17:37 | `91` | **26%** | ✗ trật | `77` **✓ trúng** |

Kết quả xổ: MB Quảng Ninh `83`/`51` · MN Bạc Liêu `92`/`02`, Bến Tre `22`/`82`, Vũng Tàu
`16`/`13` · MT Quảng Nam `77`/`23`, Đắk Lắk `80`/`02`.

**Kỳ vọng theo nền:** `0,42 + 0,29 + 0,26` = **0,97**. Thực tế **1**. Hôm nay **không có tín hiệu
gì** — không tốt hơn, không tệ hơn.

Cột `bach_thu_status` ghi `WIN`/`LOSE`/`LOSE` — **khớp**, nhưng vẫn không dùng làm nguồn
(`RM-13`: đó là kết quả chấm của chính hệ đang được đo).

### 3.2 · Bốn cửa sổ — dấu VẪN đổi

| cửa sổ | n | tỉ lệ | nền | chênh | z | CI95 |
|---|---|---|---|---|---|---|
| 14 ngày | 42 | 38,1% | 33,7% | +4,43pp | +0,61 | [−9,9 · +18,7] |
| 30 ngày | 90 | 37,8% | 33,5% | +4,23pp | +0,85 | [−5,5 · +14,0] |
| **90 ngày** | 270 | 30,7% | 33,9% | **−3,17pp** | −1,10 | [−8,8 · +2,5] |
| **180 ngày** | **516** | 34,9% | 34,0% | **+0,91pp** | +0,44 | **[−3,2 · +5,0]** |

Theo miền, 90 ngày: MN **+0,51pp** (z=+0,10) · MT **−5,28pp** (z=−1,05) · MB **−4,76pp**
(z=−1,06). **Cả ba chưa được phép kết luận** (`RM-04`).

**Cấm trích riêng cửa sổ 30 ngày** — `PRJ-SELECTION-WINDOW-001` mục 3.

### 3.3 · PHÉP ĐO MỚI — số thứ hai của lô2 có mang thông tin không?

Suốt bảng 10 ngày, số thứ hai gần như luôn trật. Câu hỏi: nó **vô dụng**, hay chỉ **trông** vô
dụng vì bạch thủ hút hết chú ý?

**Đo riêng từng số** (nền 1 số = `b`):

| cửa sổ | n | số THỨ NHẤT | số THỨ HAI | trúng CẢ HAI | CHỈ số thứ hai cứu |
|---|---|---|---|---|---|
| 30 ngày | 90 | 37,8% (+4,23pp) | **22,2% (−11,32pp · z=−2,27)** | 8,9% | 13,3% |
| 90 ngày | 270 | 30,7% (−3,17pp) | 30,0% (−3,91pp · z=−1,36) | 10,4% | 19,6% |
| 180 ngày | 516 | 34,9% (+0,91pp) | 32,6% (−1,42pp · z=−0,68) | 12,2% | **20,3%** |

> ⚠️ Cửa sổ 30 ngày cho `z = −2,27` (**|z| > 2**) cho số thứ hai. **KHÔNG dùng con số này** làm
> kết luận: nó **không đứng** ở 90 và 180 ngày, và đây là **ba cửa sổ được thử** nên phải tính
> tới so sánh bội. Báo ra vì `PRJ-SELECTION-WINDOW-001` buộc **báo cả hai vế**, không phải vì nó
> có nghĩa.

**Đo cả BỘ** — và đây mới là phép trả lời đúng câu hỏi. Nền đúng cho bộ 2 số là
**`1 − (1−b)²`**, **không phải** nền của 1 số (`RM-18` cấm chính chỗ này):

| cửa sổ | n | bộ 2 số phủ được | nền bộ 2 số | chênh | z | CI95 |
|---|---|---|---|---|---|---|
| 30 ngày | 90 | 51,1% | 55,1% | −3,96pp | −0,78 | [−13,9 · +6,0] |
| 90 ngày | 270 | 50,4% | 55,5% | −5,15pp | −1,75 | [−10,9 · +0,6] |
| **180 ngày** | **516** | **55,2%** | **55,6%** | **−0,35pp** | −0,17 | **[−4,5 · +3,8]** |

**Kết luận:** số thứ hai **có** thêm phủ sóng — nó cứu **20,3%** số miền-ngày mà bạch thủ trật.
Nhưng đó **đúng bằng** phần một lựa chọn thứ hai **bất kỳ** thêm được. Bộ 2 số nằm **ngay trên
nền của bộ 2 số**.

Nói cách khác: **bó số rộng ra không tạo lợi thế, nó chỉ đổi hình dạng của nền.**

---

## 4. Hướng xử lý và vì sao chọn

**Vì sao phải đo cả bộ, không chỉ đo từng số.** Nhìn riêng thì số thứ hai trúng 32,6% so với nền
34,0% ⇒ trông như **kém nền**, dễ đọc thành *«bỏ số thứ hai đi»*. Nhưng câu hỏi thật là *«bộ 2 số
có hơn nền của bộ 2 số không»* — và câu trả lời là **ngang nền**. Hai câu khác hẳn nhau, và
`RM-18` sinh ra đúng để chặn việc lẫn chúng.

**Vì sao không kết luận từ `z = −2,27` của cửa sổ 30 ngày.** Ba lý do, mỗi lý do đủ để dừng:
① không đứng ở 90 và 180 ngày; ② ba cửa sổ được thử ⇒ so sánh bội; ③ `RM-04` — n nhỏ **không ổn
định**, không chỉ yếu.

**Vì sao báo cáo này tồn tại.** Hôm qua owner hỏi *«em đã push báo cáo hết chưa em?»* và câu trả
lời là **chưa** — phân tích live chỉ nằm trong chat. Phép đo lô2 hôm nay là **phép chưa từng có**,
để trong chat thì mai không ai tìm lại được.

---

## 5. Đã làm gì

| # | việc | ghi chú |
|---|---|---|
| 1 | đồng bộ sống `18:34` | `RM-01` — bản local cũ ~23 giờ |
| 2 | chấm 1/3 từ `prizes_json` | không dùng cột trạng thái |
| 3 | cập nhật 4 cửa sổ + tách theo miền | dấu vẫn đổi |
| 4 | **phép đo mới**: số thứ hai lô2, riêng và theo bộ | nền `1 − (1−b)²` |
| 5 | chạy toàn bộ cổng | 8 xanh · 1 đỏ đúng |

**Không sửa dòng mã nào.** `QD-041` nguyên vẹn.

---

## 6. Cổng kiểm

| cổng | |
|---|---|
| ghi tệp an toàn · đoán tên · mất mục · đóng băng · chéo quyết định · sáu mặt · **rút lại** | **✓ 7/7 xanh** |
| `_v10981_kiem_lich` **K8** | **✓ ĐẠT 8/8** · in `ⓘ 2 mục được miễn theo QD-066, hết hạn 21/08` |
| `_v11062 --kiem` | **✗ ĐỎ ĐÚNG** — `V11080b`, **chờ owner** |

> **Không ghi «mọi cổng xanh».** `_v11062` đỏ vì `V11080b` — bản của **phiên khác**, agent **bị
> cấm tự bù** theo phương án (a). Cổng chỉ vào một việc **thật sự đang thiếu**.

**Miễn trừ `QD-066` chạy đúng ngày thứ nhất:** cổng K8 in dòng miễn trừ như thiết kế, và hai mục
`FU-360`/`FU-389` **vẫn bị đếm 2/2 và vẫn bị in tên** — không mục nào bị đóng lén.

**Lọc theo `PRJ-SELECTION-WINDOW-001`:** mọi phép đo đọc `final_bundles` — bản **đã chốt** tại mốc
`§55` (MN 05:18/hạn 15:45 · MT 16:50/16:58 · MB 17:37/17:58) ⇒ **không rò dữ liệu sau chốt**;
không dùng `predictions` nên không có dòng `shadow_auto_eval` lọt vào.

---

## 6bis. §62 (A60) — NGUỒN BA LỚP

### `OWNER_SAID`

| nội dung | nguyên văn |
|---|---|
| yêu cầu phiên này | *«Còn gì để xử lý, phân tích đánh giá kết quả dự đoán hôm nay dùm anh»* |
| nguyên tắc ưu tiên (`QD-066`, 12/08) | *«vấn đề ảnh hưởng dự án theo chiều hướng tốt lên là xử ngay»* |
| lối A (17/08 21:16) | *«miễn trừ CÓ THỜI HẠN… TỰ HẾT 21/08»* |

### `CODE_DID`

| mã làm gì | evidence |
|---|---|
| 1/3 bạch thủ | MN `67` ✓ · MT `71` ✗ · MB `91` ✗ — từ `prizes_json` |
| nền ngày đó | 42% · 29% · 26% ⇒ kỳ vọng **0,97**, thực tế **1** |
| bộ 2 số 180 ngày | **55,2% vs nền 55,6%** ⇒ −0,35pp · n=516 |
| miễn trừ K8 hoạt động | `ⓘ 2 mục được miễn theo QD-066, hết hạn 21/08` · K8 `ĐẠT 8/8` |
| `_v11062` còn đỏ | `K1: V11080b` |

### `DOC_SAID`

| tài liệu ghi gì | lệch? |
|---|---|
| `V11084`: 180 ngày `+0,91pp`, `CI95 [−3,2 · +5,0]` | **khớp** — nay n=516, cùng con số |
| `SO_RUT_LAI.json` 6 mục | **khớp** — cổng chạy sạch trên báo cáo mới |
| `FOLLOW_UP_TRACKER`: miễn trừ tự hết 21/08 | **khớp** — cổng in đúng ngày hết hạn |

### Ba lớp lệch nhau ⇒ FINDING

**Không có lệch nào phải báo.** Ba lớp khớp. Ghi rõ thay vì bỏ trống mục.

---

## 7. Vướng vấp

**Không có vấp kỹ thuật trong phép đo.**

**Một vấp thao tác, ghi lại vì đúng lớp lỗi đã ghi:** viết báo cáo này lần đầu bằng heredoc trong
shell — vỡ vì nội dung có dấu nháy. Cùng họ với ca ngày 16/08 (*bash ăn mất đoạn trong backtick,
tệp ghi ra rỗng ở các khối mã mà lệnh vẫn báo thành công*). Lần này **kiểm trước khi tin**: thư
mục chưa hề được tạo ⇒ chuyển sang ghi thẳng bằng công cụ ghi tệp.

**Một cái bẫy đã tránh được:** nhìn bảng số thứ hai riêng lẻ (32,6% vs nền 34,0%) rất dễ kết luận
*«số thứ hai kém nền, bỏ đi»*. Đo đúng theo bộ thì nó **ngang nền** — bỏ đi sẽ **giảm phủ sóng
20,3%** mà **không được lợi gì**. `RM-18` chặn đúng chỗ này.

---

## 8. Gỡ về

Không có gì để gỡ — **read-only**, không sửa dòng mã nào, không ghi DB.

---

## 9. Theo dõi tiếp

### Chờ owner — không đổi từ V11085

| việc | ghi chú |
|---|---|
| **`V11080b`** chưa có dòng `HISTORY` | của phiên khác; agent bị cấm tự bù ⇒ `_v11062` **đỏ đúng** |
| hook `SessionStart` · **48 bản vá** cũ | treo từ V11083 |

### Lịch tự động

| mốc | chuyện gì |
|---|---|
| **22/08** | miễn trừ `QD-066` **tự hết** ⇒ **K8 đỏ lại là CỐ Ý**, nhắc xử `FU-360`/`FU-389` trong gói 21/08 |

### Sổ theo dõi — 18/08

**281 mã · 163 CÒN TREO** — quá hạn **84** · đến hạn hôm nay **6** · hạn 19–21/08 **26**
(phần lớn là gói 21/08) · **21 mục CHỜ OWNER KÝ**.

Sáu mục đến hạn hôm nay: `FU-221` (`OWNER_LOCK`) · `FU-327` · `FU-366` (`READY_NOT_DEPLOYED`) ·
`FU-335` · `FU-373` · `FU-360` (đang **được miễn trừ** tới 21/08).

### Việc mới sinh từ bản này

| mã | việc | ghi chú |
|---|---|---|
| **`FU-407`** | Bó số rộng ra **không tạo lợi thế** — kiểm xem các bó khác (`lo3`, `xien2`, `xien3`) có cùng tính chất không | nếu đúng thì **điểm nghẽn nằm ở SINH SỐ**, không ở việc chọn bao nhiêu số |

**Verdict:**
- **`CODE_PUSHED`** = không áp dụng — bản này **không sửa mã**
- **`REPORT_PUBLISHED`** = bản này

---

TanPhatAI cần làm: ① ghi **18/08 = 1/3 bạch thủ**, nền 42/29/26% ⇒ kỳ vọng **0,97** vs thực tế
**1** — **đúng bằng nền, không có tín hiệu gì**; ② ghi **phép đo mới**: bộ 2 số lô2 phủ **55,2%**
vs nền đúng của bộ 2 số **55,6%** (n=516) ⇒ **−0,35pp** — số thứ hai thêm phủ sóng **20,3%**
nhưng **đúng bằng phần một lựa chọn ngẫu nhiên thêm được**; ③ **CẤM** trích `z = −2,27` của cửa
sổ 30 ngày làm kết luận — không đứng ở 90/180 ngày, ba cửa sổ được thử, `RM-04`; ④ ghi **cấm bỏ
số thứ hai** — bỏ đi giảm phủ sóng 20,3% mà không được lợi gì; ⑤ mở **`FU-407`** kiểm `lo3`/`xien`
có cùng tính chất không — nếu đúng thì **điểm nghẽn nằm ở SINH SỐ**; ⑥ ghi **`_v11062` vẫn ĐỎ
ĐÚNG vì `V11080b`** và **miễn trừ K8 tự hết 22/08** — cấm ghi «mọi cổng xanh».
