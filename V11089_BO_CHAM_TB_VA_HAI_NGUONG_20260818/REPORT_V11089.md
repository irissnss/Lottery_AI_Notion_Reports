# REPORT V11089 — BỘ CHẤM LANE T-B + HAI NGƯỠNG CHO NGÀY KHOÁ 20/08

**Ngày:** 2026-08-18 · **Mã đọc:** `DO1808` · **Quyết định:** `QD-068`
**Production KHÔNG đổi** — không deploy · không Notion · `QD-041` nguyên vẹn ·
**không đọc sớm** `FU-284` (`RM-03`).

---

## 1. Tóm tắt

| chặng | kết quả |
|---|---|
| **GĐ-1** bộ chấm lane T-B | **110/110 chấm được · 0 từ chối · 0 còn NULL** |
| **GĐ-2** hai ngưỡng | **1 KHÔI PHỤC · 1 ĐỀ XUẤT MỚI** — cả hai **chờ owner ký** |

**Hai kết quả đáng chú ý:**

**①** Lane T-B **sống lại**: từ **0 cặp đọc được** thành **110 cặp đã chấm**, trong đó **79 cặp
bất đồng** (ngưỡng `QD-059` cần **≥96**) ⇒ dự kiến đủ **~20/08**.

**②** Ngưỡng bầy đàn **không cần nghĩ mới** — đã có **bảng bốn dòng chốt trước**, tìm lại được
nguyên văn. Owner chỉ cần **xác nhận khôi phục**.

---

## 2. Owner yêu cầu gì (nguyên văn)

> **22:27 · 18/08** — *«① Lane T-B — LỐI A: dựng bộ chấm + CHẤM NGƯỢC 110 dòng hiện có.»*

> **22:27 · 18/08** — *«② Ngưỡng DEHERD + bầy đàn: agent ĐỀ XUẤT kèm DẪN XUẤT (tiền lệ 9,53đ của
> FU-284), trình owner ký trước 20/08. CHƯA CÓ CHỮ KÝ thì CẤM ĐỌC hai phép đo đó (RM-03).»*

> *«CHẤM ĐỂ LẤP DỮ LIỆU — CẤM tổng hợp thành verdict/kết luận trước 20/08. Chỉ in số lượng (đếm),
> KHÔNG in tỉ lệ thắng so sánh.»*

> *«Bầy đàn: RÀ TRƯỚC xem ngưỡng 0,50/0,35 từng xuất hiện ở đâu — nếu có nguồn thật thì khôi phục
> + ghi vào kho; nếu không, đề xuất mới kèm dẫn xuất.»*

---

## 3. Đào bới / phát hiện

### 3.1 · Vì sao lane T-B chưa bao giờ chấm được

`trung_control`/`trung_tb` **chỉ tồn tại ở câu `CREATE TABLE`** (`_v11059:176-177`). Quét toàn
kho: **không một câu `UPDATE` nào**. Cron `06:00/16:52/17:45` chỉ **thu**, không **chấm**.

Cột `bat_dong` **có** ghi (79 khác / 31 giống): lane biết A và B **có khác nhau không**, nhưng
**không biết bên nào thắng**. Đúng nửa việc.

### 3.2 · Ngưỡng bầy đàn — **CÓ nguồn thật**, và đầy đủ hơn hai con số owner nhớ

`CHANGELOG.md:5128-5131` — bảng **bốn dòng**, đăng ký trước:

| kết luận | điều kiện |
|---|---|
| **CÓ TÁC DỤNG** | trung bình **≥ 0,50** *và* hơn nền **≥ 0,05** |
| **KHÔNG TÁC DỤNG** | trung bình **≤ 0,35** |
| **CHƯA RÕ** | nằm giữa hai ngưỡng |
| **CHƯA ĐỦ** | dưới **9 lượt** (3 ngày × 3 miền) |

`docs/archive/FOLLOW_UP_TRACKER_LICH_SU.md:298` (`FU-325`) nhắc lại cùng ngưỡng.

**Nền = `0,47`** ⇒ vế *«hơn nền ≥ 0,05»* thực chất là **≥ 0,52**, **chặt hơn** vế `≥ 0,50`.
Hai vế **không thừa nhau** — vế nền mới là vế ràng buộc thật.

### 3.3 · `PL13` — không có gì để khôi phục

Quét toàn bộ `.md`/`.py`/`.json`: **0 kết quả**. Không có ngưỡng DEHERD đăng ký trước nào còn
hiệu lực. ⇒ phải **đề xuất mới**.

---

## 4. Hướng xử lý và vì sao chọn

**Vì sao bộ chấm phải có hai chốt chống lookahead.** Chấm ngược là chỗ **dễ rò kết quả tương lai
nhất**, và `PRJ-SELECTION-WINDOW-001` cấm đúng chuyện đó. Nếu một dòng lane được sinh **sau** giờ
xổ thì nó đã «biết đáp án» — chấm nó là **tự bơm điểm**. Nên chốt là **máy**, không phải lời hứa.

**Vì sao chỉ in ĐẾM.** Owner ký thẳng *«CẤM tổng hợp thành verdict trước 20/08»*. Bộ chấm in
**đếm** và **chỉ đếm** — không tỉ lệ, không z, không so sánh.

**Vì sao bầy đàn là KHÔI PHỤC chứ không phải đề xuất.** Owner dặn *«rà trước»*, và rà ra
**nguồn thật, đầy đủ hơn**. Đề xuất một con số mới khi đã có ngưỡng chốt trước là **sửa ngưỡng
sau khi có dữ liệu** — đúng thứ `RM-03` cấm.

---

## 5. Đã làm gì

### GĐ-1 — bộ chấm lane T-B · commit `<GĐ-1>`

**Hai chốt chống lookahead:**
1. chỉ chấm bằng kết quả của **chính ngày-miền đó**;
2. dòng lane phải tạo **TRƯỚC** khi kết quả về (`created_at` dòng `<` `created_at` sớm nhất của
   `lottery_results` cùng ngày-miền). Không thoả ⇒ **TỪ CHỐI**, ghi lý do.

**Kết quả — CHỈ ĐẾM:**

| | |
|---|---|
| dòng đầu vào | **110** |
| chấm được | **110** |
| **TỪ CHỐI** chấm | **0** |
| **đọc lại TỪ DB** (xác minh độc lập) | **110** ✓ khớp |
| còn `NULL` | **0** |
| **trong đó bất đồng (A≠B)** | **79** · ngưỡng `QD-059` cần **≥96** |

Nhịp ~**11** cặp bất đồng/ngày ⇒ đủ 96 dự kiến **~20/08**. *(Đếm mẫu, **không** phải verdict.)*

**Xác minh dấu vết:** đọc lại thẳng từ DB bằng truy vấn **độc lập**, **không tin exit code** —
đúng lời owner dặn.

**Commit theo lô 50 dòng** — bài học `V11066`/`FU-403`: giữ khoá ghi SQLite suốt một giao dịch
dài đã làm **mất 2 kết quả model**.

### GĐ-2 — hai ngưỡng · commit `e34e7a5` · `docs/NGUONG_DEHERD_VA_BAYDAN_20260818.md`

**Dẫn xuất DEHERD, cùng khuôn `9,53`:**

| đại lượng | giá trị | nguồn |
|---|---|---|
| `n` | **63** miền-ngày | 21 ngày × 3 miền |
| phương sai/quan sát | **0,2174** | nền riêng: MB `0,235` · MN `0,427` · MT `0,350` |
| `VIF` | **1,002** | ⚠️ **mượn** từ thước bạch thủ (`RM-21`) |
| `z` | **1,96** | như `FU-284` |

```
SE  = √(2 × 0,2174 / 63) × √1,002 = 0,08316
MDE = 1,96 × 0,08316              = 0,16299 = 16,3pp
```

⇒ **`|chênh| ≥ 16,3pp` VÀ `|z| ≥ 1,96` VÀ `n ≥ 63`.** Không có ô «gần đạt».

---

## 6. Cổng kiểm

| cổng | |
|---|---|
| `_v11089 --thu-chan` | **✓ 6/6** — `T3`+`T6` chống lookahead |
| đọc lại DB xác minh | **✓ 110/110**, 0 `NULL` |
| `_v11062 --kiem` K1–K4 | **✓ ĐẠT** |
| `_v11085_cong_rut_lai` | **✓ SẠCH** |
| `_v11088_cong_cua_so_chon` | **✓ SẠCH** |
| `_v10981_kiem_lich` K8 | **✓ ĐẠT 8/8** |

---

## 6bis. §62 (A60) — NGUỒN BA LỚP

### `OWNER_SAID`

| giờ | nguyên văn |
|---|---|
| **22:27 18/08** | *«Lane T-B — LỐI A: dựng bộ chấm + CHẤM NGƯỢC 110 dòng hiện có»* |
| **22:27 18/08** | *«CHƯA CÓ CHỮ KÝ thì CẤM ĐỌC hai phép đo đó (RM-03)»* |
| **22:27 18/08** | *«CHẤM ĐỂ LẤP DỮ LIỆU — CẤM tổng hợp thành verdict… Chỉ in số lượng (đếm)»* |

### `CODE_DID`

| mã làm gì | evidence |
|---|---|
| `trung_control` chưa từng có writer | chỉ ở `_v11059:176-177`, 0 câu `UPDATE` |
| chấm 110/110, 0 từ chối | đọc lại DB độc lập: 110, `NULL` = 0 |
| 79 cặp bất đồng | `WHERE trung_control IS NOT NULL AND bat_dong=1` |
| chống lookahead hoạt động | `T3`/`T6` từ chối dòng tạo ≥ giờ kết quả |
| ngưỡng bầy đàn có nguồn | `CHANGELOG.md:5128-5131` · `archive/…:298` |
| `PL13` không tồn tại | quét `.md`/`.py`/`.json` ⇒ 0 |
| MDE DEHERD = 16,3pp | `n=63` · `var=0,2174` · `VIF=1,002` · `z=1,96` |

### `DOC_SAID`

| tài liệu ghi gì | lệch? |
|---|---|
| `FU-398`: *«đọc khi đủ ≥96 cặp bất đồng»* | **hết lệch** — nay có 79/96, đếm được |
| owner nhớ ngưỡng bầy đàn *«0,50/0,35»* | **khớp**, và tài liệu còn **đầy đủ hơn**: 4 dòng + nền `0,47` + sàn 9 lượt |
| `V11088`: *«lane T-B không đọc được»* | **đã xử** — không phải rút lại, mà là **đã sửa** |

### Ba lớp lệch nhau ⇒ FINDING

**`OWNER_SAID` vs kho:** owner nhớ *«0,50/0,35»* — kho có **đủ bốn dòng** cộng nền `0,47` và sàn
`9 lượt`. Trí nhớ owner **đúng nhưng thiếu**, và phần thiếu (**vế nền ≥0,52**) là vế **ràng buộc
thật**. Báo lại thay vì im.

---

## 7. Vướng vấp

**Không có vấp kỹ thuật trong phiên này.**

**Một chỗ suýt làm sai và đã dừng đúng lúc:** dẫn xuất DEHERD cần `VIF`. Có sẵn `VIF = 2,92` từ
`FU-284`. Dùng nó thì ngưỡng phồng lên **~27,8pp** — nhưng `2,92` đo cho thước *16 model cùng
đoán một ngày*, **khác hẳn hình dạng**. Đúng ca `RM-21` đã ghi. Dùng `1,002` (thước bạch thủ,
cùng hình dạng) và **ghi rõ đó là hằng số MƯỢN**.

---

## 8. Gỡ về

```bash
git revert e34e7a5   # GĐ-2 (chỉ là giấy tờ)
git revert <GĐ-1>    # GĐ-1 bộ chấm
```

Gỡ `GĐ-1` **không** xoá điểm đã chấm trong DB local — chạy lại
`_sync_live_forensic_inputs.py` là DB trở về nguyên trạng VPS (`NULL`).

---

## 9. Theo dõi tiếp

### ⛔ HAI NGƯỠNG — **CHỜ OWNER KÝ, CHƯA KÍCH HOẠT**

| ngưỡng | trạng thái | owner cần làm |
|---|---|---|
| **Bầy đàn** ≥0,50 & hơn nền ≥0,05 · ≤0,35 · <9 lượt | **có sẵn, chờ xác nhận khôi phục** | xác nhận, **không đổi số** |
| **DEHERD** \|chênh\|≥16,3pp & \|z\|≥1,96 & n≥63 | **chờ ký** | chọn **A/B/C** ở §2 tài liệu |

**Chưa có chữ ký ⇒ CẤM ĐỌC hai phép đo đó ngày 20/08.**

### ⚠️ Điều owner cần biết trước khi ký DEHERD — **phép đo này YẾU**

`n = 63` chỉ thấy được hiệu ứng **≥ 16,3pp**:

| hiệu ứng | n cần | = ngày | ≈ tháng |
|---|---|---|---|
| 20 pp | 42 | 14 | 0,5 |
| **16,3 pp** | **63** | **21** | **0,7** ← hiện có |
| 10 pp | 167 | 56 | 1,9 |
| **5 pp** | **669** | **223** | **7,4** |

Nếu DEHERD có lợi thế thật cỡ **+5pp** — mức rất đáng làm — phép đo 21 ngày **không thể thấy**.
Kết quả *«chưa kết luận»* ngày 20/08 sẽ là **bằng chứng cửa sổ quá ngắn**, **không phải** bằng
chứng DEHERD vô dụng.

### ⚠️ Bộ chấm CHƯA lên VPS

DB local bị **ghi đè** mỗi lần đồng bộ ⇒ điểm chấm **sẽ mất**. Bộ chấm thiết kế **chạy lại sau
mỗi lần đồng bộ** và **idempotent**, kèm kết xuất bền `artifacts/v11089/`. Nhưng **chưa deploy
lên VPS** — vùng cấm phiên này.

⇒ **Ngày 20/08 phải chạy `_v11089_cham_lane_tb.py` SAU khi đồng bộ, TRƯỚC khi đọc.** Đã ghi vào
bản đồ 21/08.

### Khi đọc bầy đàn 20/08 — **kiểm `giai_doan` TRƯỚC**

Bẫy đã sập một lần: ba lượt 07/08 bị gắn `SAU_V11016` với phân tán `0,56/0,57/0,57`, *«nhìn như
thắng lớn so với nền 0,47»* — nhưng chúng tạo lúc **05:00–05:20** còn `V11016` lên máy chủ
**13:35:48**, tức chạy **prompt CŨ**.

**Không mở FU mới** — mọi phát hiện gắn vào `FU-398` · `FU-325`.

**Verdict tách hai dòng:**
- **`CODE_PUSHED`** = `<GĐ-1>` (bộ chấm) · `e34e7a5` (hai ngưỡng)
- **`REPORT_PUBLISHED`** = bản này

---

TanPhatAI cần làm: ① ghi **lane T-B ĐÃ SỐNG LẠI** — `110/110` chấm được, `0` từ chối, `0` còn
`NULL`, xác minh bằng truy vấn **độc lập** đọc lại DB; **79 cặp bất đồng**, ngưỡng `QD-059` cần
**≥96**, dự kiến đủ **~20/08**; ② ghi **bộ chấm có HAI chốt chống lookahead** (`T3`+`T6`) — dòng
tạo **≥** giờ kết quả về là **TỪ CHỐI**, vì nó đã biết đáp án; ③ ghi **ngưỡng bầy đàn KHÔNG cần
nghĩ mới** — bảng **bốn dòng** chốt trước ở `CHANGELOG:5128`, nền **`0,47`** ⇒ vế nền thực chất
**≥0,52** và đó là vế **ràng buộc thật**; owner chỉ cần **xác nhận khôi phục**; ④ ghi **ngưỡng
DEHERD đề xuất `16,3pp`** với dẫn xuất `n=63 · var=0,2174 · VIF=1,002 · z=1,96`, và **cảnh báo
phép đo YẾU**: muốn thấy `+5pp` cần **223 ngày**; ⑤ ghi **`VIF=1,002` là hằng số MƯỢN** (`RM-21`)
— dùng `2,92` sẽ phồng ngưỡng lên `~27,8pp` **vô cớ**; ⑥ ghi **CẢ HAI NGƯỠNG CHƯA KÍCH HOẠT** —
chưa có chữ ký owner thì **cấm đọc** hai phép đo ngày 20/08; ⑦ ghi **bộ chấm chưa lên VPS** ⇒
ngày 20/08 phải **chạy lại sau đồng bộ, trước khi đọc**.
