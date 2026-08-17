# REPORT V11084 — KIỂM HẾT LIVE 17/08: **3/3 BẠCH THỦ**, VÀ HAI GIẢ THUYẾT BỊ CHÍNH PHÉP ĐO BÁC

**Ngày:** 2026-08-17 · **Mã đọc:** `KS1708-3` · **Read-only** — không sửa mã, không DB, không deploy.
Dữ liệu: đồng bộ sống lúc **19:46** (`artifacts/live_sync/20260817_194620`), sau khi MB về `18:31`.

---

## 1. Tóm tắt

**Hôm nay 3/3 bạch thủ** — kiểm thẳng từ bảng giải, **không** tin cột `bach_thu_status`.

**Nhưng đó không phải câu trả lời cho «hệ có lợi thế chưa».** Dấu của lợi thế **đổi theo cửa sổ**:
30 ngày **+4,07pp** · 90 ngày **−3,18pp** · 180 ngày **+0,91pp** với `CI95 [−3,2 · +5,0]`.
Con số đứng vững vẫn là **chưa có lợi thế nào được chứng minh**.

Và hai giả thuyết nêu trong phiên **đều bị bác bằng số**:

| giả thuyết | kết quả |
|---|---|
| ba miền **tụ** với nhau (14 ngày không có ngày 2/3 nào) | **BÁC** — 90 ngày `VIF = 1,002` |
| MN chốt `05:20` nên **lỡ** bộ học | **BÁC** — bộ eval chạy `20:20` tối trước |

---

## 2. Owner yêu cầu gì (nguyên văn)

> *«Còn gì tồn đọng — luật · kiểm soát hệ thống, các vấn đề đã và đang xử lý, về kết quả dự đoán
> hôm nay.»*

> *«em đã push báo cáo hết chưa em?»*

Câu thứ hai là lý do bản này tồn tại: mã đã push đủ, nhưng **phân tích live hôm nay chỉ nằm
trong chat**. `§57.2` — *«sau MỌI việc code, fix, audit cần đẩy báo cáo report lên github report
public»*.

---

## 3. Đào bới / phát hiện

### 3.1 · Kết quả hôm nay — kiểm từ **bảng giải**, không từ cột trạng thái

Cả ba bundle đều ghi `bach_thu_status = WIN`. Không dùng con số đó; mở `prizes_json` đếm lại:

| miền | bạch thủ | trúng ở đài | đuôi khác nhau trong ngày | **nền đúng** | lô2 thứ hai |
|---|---|---|---|---|---|
| **MN** | `89` | TP. HCM | 45 | **45%** | `96` ✗ |
| **MT** | `64` | Thừa Thiên Huế | 31 | **31%** | `96` ✗ |
| **MB** | `55` | Hà Nội | 25 | **25%** | `92` ✗ |

Kết quả xổ: MB `39`/`89` · MN Cà Mau `53`, TP.HCM `90`, Đồng Tháp `08` · MT Phú Yên `71`,
TT Huế `55`.

**Nền đúng theo `RM-18`** = `|đuôi khác nhau của miền đó trong ngày| / 100`, **không** phải
`1/100`. Xác suất 3/3 hoàn toàn ngẫu nhiên: `0,45 × 0,31 × 0,25` = **3,5%**.

**Số thứ hai của lô2 trật cả ba miền.** Đáng chú ý: MN và MT **cùng chọn `96`**, cả hai đều trật.

### 3.2 · Dấu của lợi thế ĐỔI theo cửa sổ — đây mới là phát hiện

| cửa sổ | n | tỉ lệ | nền đúng | chênh | z | CI95 |
|---|---|---|---|---|---|---|
| 14 ngày | 42 | 38,1% | 33,7% | **+4,4pp** | +0,61 | — |
| 30 ngày | 90 | 37,8% | 33,7% | **+4,07pp** | +0,82 | [−5,7 · +13,8] |
| **90 ngày** | 270 | 30,7% | 33,9% | **−3,18pp** | −1,10 | [−8,8 · +2,5] |
| **180 ngày** | **513** | 34,9% | 34,0% | **+0,91pp** | +0,43 | **[−3,2 · +5,0]** |

**Cả bốn đều `|z| < 2` ⇒ chưa được phép kết luận** (`RM-04`). Nhưng chuyện quan trọng hơn là
**dấu đổi**: nếu chỉ báo cửa sổ 30 ngày thì đó là **chọn cửa sổ cho khớp kết quả** — đúng thứ
`PRJ-SELECTION-WINDOW-001` (ban hành **sáng nay**) cấm.

Tách theo miền, 90 ngày: MN **−0,6pp** · MT **−4,2pp** · MB **−4,7pp** — **cả ba** chưa được phép
kết luận, và **cả ba đều âm**.

Con số **+0,91pp / n=513** khớp với **+0,34pp / n=492** đã công bố trước đó — cùng một kết luận:
**khoảng tin cậy trùm số 0**.

### 3.3 · Giả thuyết ① «ba miền tụ» — BÁC

14 ngày gần nhất **không có ngày nào 2/3**: toàn `3/3`, `0/3` hoặc `1/3`. Nếu ba miền độc lập với
`p ≈ 0,34` thì `2/3` phải xuất hiện **~3 lần**. Trông rất giống có cụm — và nếu có cụm thật thì
mọi khoảng tin cậy đang tính đều **hẹp giả**.

Đo phân bố số miền trúng trong ngày, so với kỳ vọng **độc lập dùng nền riêng từng miền-ngày**:

| cửa sổ | χ² (3 bậc tự do) | VIF thực nghiệm | phán quyết |
|---|---|---|---|
| 30 ngày | **9,38** *(> ngưỡng 5% = 7,81)* | 1,416 | trông có tụ |
| 60 ngày | 7,02 | 1,086 | không |
| **90 ngày** | **2,91** | **1,002** | **độc lập gần như hoàn hảo** |

**BÁC.** Mẫu «không có ngày 2/3» là **nhiễu của n = 14**. Và đây là `RM-04` đúng nguyên văn:
*n nhỏ không chỉ yếu mà KHÔNG ỔN ĐỊNH*.

`VIF = 1,002` cho thước **bạch thủ** cũng **khớp** con số `0,889` đo trước đó cho cùng thước, và
**tiếp tục khác hẳn** `VIF = 2,92` của thước *16 model cùng đoán một ngày* — đúng `RM-21`:
**hằng số chỉ đúng cho thước đã đo nó**.

### 3.4 · Giả thuyết ② «MN chốt sớm nên lỡ bộ học» — BÁC

Giờ chốt bundle 10 ngày liền, **rất ổn định**:

| miền | giờ chốt thực tế | hạn (`§55`) | sớm hơn hạn |
|---|---|---|---|
| **MN** | `05:19` – `05:31` | `15:45` | **hơn 10 giờ** |
| MT | `16:42` – `16:57` | `16:58` | 1 – 16 phút |
| MB | `17:34` – `17:42` | `17:58` | 16 – 24 phút |

Nghi vấn: MN chốt trước khi bộ học cập nhật? **Đo:** `model_daily_eval` ghi lúc **`20:20`** tối
hôm trước, đều đặn 7/7 ngày. `20:20` hôm trước **<** `05:20` hôm sau ⇒ MN **có** bản eval mới
nhất. **BÁC.**

**Còn lại một quan sát CHƯA giải thích, và cố ý KHÔNG gọi là phát hiện:** MN chốt sớm hơn hạn
**10h25m** trong khi hai miền kia chốt sát hạn. Chưa đo được nó **mất gì** — nêu ra để có mục
theo dõi, không nêu ra như một kết luận.

---

## 4. Hướng xử lý và vì sao chọn

**Vì sao không dùng cột `bach_thu_status`.** Nó là **kết quả chấm của hệ**, mà chính hệ đó là thứ
đang được đo. `RM-13`: nguồn sai thì mọi kết luận sai. Mở `prizes_json` đếm lại là **nguồn độc
lập với bộ chấm**.

**Vì sao báo cả bốn cửa sổ chứ không chọn một.** `PRJ-SELECTION-WINDOW-001` mục 3 buộc **báo cả
hai vế**. Ở đây vế bất lợi là 90 ngày `−3,18pp` — bỏ nó đi thì bản báo cáo này trở thành đúng thứ
luật vừa ban hành cấm.

**Vì sao ghi cả hai giả thuyết bị bác.** Nếu chỉ ghi kết luận, phiên sau sẽ **nhìn thấy đúng mẫu
hình đó** và đi đo lại từ đầu. Ghi rõ *«đã đo, đã bác, đây là số»* là cách duy nhất để nó không
quay lại.

---

## 5. Đã làm gì

| # | việc | ghi chú |
|---|---|---|
| 1 | đồng bộ dữ liệu sống `19:46` | `RM-01` — bản local đang cũ ~24 giờ, mọi bộ đo sẽ **từ chối chạy** |
| 2 | kiểm 3/3 từ `prizes_json` | không dùng cột trạng thái |
| 3 | tính nền đúng từng miền-ngày | `RM-18` |
| 4 | đo 4 cửa sổ + tách theo miền | dấu đổi theo cửa sổ |
| 5 | đo phân bố cụm + VIF thực nghiệm | giả thuyết ① bị bác |
| 6 | đối chiếu giờ chốt vs giờ eval | giả thuyết ② bị bác |

**Không sửa dòng mã nào.** `QD-041` nguyên vẹn.

---

## 6. Cổng kiểm

| cổng | kết quả |
|---|---|
| `RM-01` tuổi dữ liệu | **✓** đồng bộ `19:46`, sau khi MB về `18:31` |
| ghi tệp an toàn · đoán tên · mất mục · đóng băng · chéo quyết định · sáu mặt | **✓ 6/6 xanh** |
| `_v11062 --kiem` | **✗** — `V11080b`, **chờ owner** |
| `_v10981_kiem_lich` K8 | **✗** — `QD-021` vs `QD-066`, **chờ owner** |
| `_v10920_decision_ledger` | **✗ 4 phép trôi** |

> **Không ghi «mọi cổng xanh».** Hai cổng đỏ **đúng**, và cả hai đang chờ chữ ký owner chứ không
> chờ agent làm thêm việc.

**Lọc theo `PRJ-SELECTION-WINDOW-001`:** phép đo này đọc `final_bundles` — **bản đã chốt**, tạo
trước mốc `§55` (đo được: MN `05:20`/hạn `15:45` · MT `16:45`/`16:58` · MB `17:36`/`17:58`) ⇒
**không có rò dữ liệu sau mốc chốt**. Không dùng `predictions` nên không có dòng `shadow_auto_eval`
lọt vào.

---

## 6bis. §62 (A60) — NGUỒN BA LỚP

### `OWNER_SAID`

| nội dung | nguyên văn |
|---|---|
| yêu cầu rà tồn đọng | *«Còn gì tồn đọng — luật · kiểm soát hệ thống, các vấn đề đã và đang xử lý, về kết quả dự đoán hôm nay»* |
| hỏi về báo cáo | *«em đã push báo cáo hết chưa em?»* |
| nguyên tắc ưu tiên (`QD-066`, 12/08) | *«vấn đề ảnh hưởng dự án theo chiều hướng tốt lên là xử ngay»* |

### `CODE_DID`

| mã làm gì | evidence |
|---|---|
| 3/3 bạch thủ | `prizes_json` — MN `89`@TP.HCM · MT `64`@TT Huế · MB `55`@Hà Nội |
| nền đúng từng miền | 45 / 31 / 25 đuôi khác nhau |
| 180 ngày `+0,91pp` · `CI95 [−3,2 · +5,0]` | `final_bundles` × `lottery_results`, n = 513 |
| 90 ngày **âm** `−3,18pp` | n = 270 |
| `VIF = 1,002` (90 ngày) | phân bố số miền trúng vs kỳ vọng độc lập |
| MN chốt `05:19`–`05:31`, eval `20:20` hôm trước | `final_bundles.created_at` · `model_daily_eval.created_at` |

### `DOC_SAID`

| tài liệu ghi gì | lệch? |
|---|---|
| `final_bundles.bach_thu_status = WIN` ×3 | **khớp** — nhưng đã kiểm độc lập, không dùng làm nguồn |
| báo cáo trước: `+0,34pp` / n=492 | **khớp** — nay `+0,91pp` / n=513, cùng kết luận: CI trùm 0 |
| `RM-21`: `VIF 2,92` là của thước *16 model cùng ngày* | **khớp** — thước bạch thủ đo lại ra `1,002`, **không mượn** |

### Ba lớp lệch nhau ⇒ FINDING

**Không có lệch nào phải báo trong bản này.** Ba lớp khớp nhau. Ghi rõ điều đó thay vì bỏ trống
mục — `§62` cấm im lặng chọn một lớp.

---

## 7. Vướng vấp

**Hai giả thuyết của agent bị bác, cả hai đều do agent tự nêu rồi tự đo.**

Điểm chung: cả hai **nghe rất thuyết phục trước khi đo**. «14 ngày không có ngày 2/3» là một mẫu
hình sạch sẽ; «MN chốt sớm 10 tiếng» nghe hiển nhiên là bất lợi. Nếu báo lên trước khi đo thì
owner đã mất công đi kiểm hộ **hai lần** — đúng chuyện owner đã than mệt.

Đây là **lần thứ hai trong tuần** cùng một cơ chế cứu: `FU-316` (neo pool D-1) cũng có agent và
bản đào **cùng nghiêng về «có neo»**, đo ra `−0,79pp, z = −1,01` ⇒ **không neo**.

**Không có vấp kỹ thuật** trong bản này.

---

## 8. Gỡ về

Không có gì để gỡ — **read-only**, không sửa dòng mã nào, không ghi DB.

---

## 9. Theo dõi tiếp

### Chờ owner — bốn việc, xếp theo mức gấp

| | việc | hạn |
|---|---|---|
| **1** | **`FU-348`** hạ `MO_COI_TRAN` **15 → 2** | **HÔM NAY** · mồ côi đang **đúng bằng 2** ⇒ hạ xong vẫn ĐẠT |
| **2** | **K8** chọn lối **A / B / C** | **≤18/08** · khuyến nghị **lối A** |
| **3** | **`V11080b`** — không có bản ghi gốc | cổng đỏ tới khi có hướng |
| **4** | hook `SessionStart` · **48 bản vá** cũ | không gấp |

### Sổ theo dõi

**279 mã · 162 CÒN TREO** — quá hạn **81** · đến hạn hôm nay **4** (`FU-348` · `FU-306` ·
`FU-301` · `FU-292`) · hạn 18–21/08 **32** (trong đó **14 mục thuộc gói 21/08**) · không hạn **32**.

### Việc mới sinh từ bản này

| mã | việc | vì sao |
|---|---|---|
| **`FU-405`** | MN chốt sớm hơn hạn **10h25m** — đo xem có mất gì không | quan sát chưa giải thích; **không** kết luận vội |

### Luật — còn nợ gì

Ba luật `PRJ-*` ban hành sáng nay hiện là **luật thành văn, CHƯA có cổng máy**. Theo `§61`
(*«một RM tái phạm hai lần ⇒ phải dựng cổng máy, không được chỉ hứa»*),
**`PRJ-RETRACTION-001` đã tái phạm ba lần** ⇒ **đến ngưỡng phải có cổng**. Chưa dựng vì phiên
trước owner giới hạn phạm vi.

**Verdict:**
- **`CODE_PUSHED`** = không áp dụng — bản này **không sửa mã**
- **`REPORT_PUBLISHED`** = bản này

---

TanPhatAI cần làm: ① ghi **17/08 = 3/3 bạch thủ**, kiểm từ `prizes_json` **không** từ cột trạng
thái, nền đúng **45% / 31% / 25%**, xác suất ngẫu nhiên **3,5%**; ② ghi **dấu lợi thế ĐỔI theo
cửa sổ** — 30 ngày `+4,07pp`, **90 ngày `−3,18pp`**, 180 ngày `+0,91pp` `CI95 [−3,2 · +5,0]` ⇒
**vẫn chưa có lợi thế được chứng minh**, và **cấm trích riêng cửa sổ 30 ngày**;
③ ghi **hai giả thuyết ĐÃ BỊ BÁC** — «ba miền tụ» (90 ngày `VIF = 1,002`) và «MN lỡ bộ học»
(eval chạy `20:20` hôm trước) — **đừng đo lại**; ④ mở **`FU-405`** cho quan sát MN chốt sớm
10h25m; ⑤ ghi **ba luật `PRJ-*` chưa có cổng máy**, `PRJ-RETRACTION-001` đã tái phạm **ba lần**
⇒ tới ngưỡng `§61` phải dựng cổng; ⑥ ghi **hai cổng đang ĐỎ ĐÚNG**, cả hai **chờ chữ ký owner**
chứ không chờ agent.
