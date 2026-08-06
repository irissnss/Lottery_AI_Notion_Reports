# REPORT V11006 — Tên đài sau khi gộp tỉnh: vá lỗ hổng IM LẶNG

> **Ngày:** 2026-08-06 · **Mã việc:** FU-292 · FU-293
> **Deploy:** ĐẠT — PID `930315` → `936322`, 4 bảng khoá **y hệt**

---

## 1. Tóm tắt

Owner báo các tỉnh đã gộp nên tên đài và lịch xổ có thể đổi. **Đo trước, sửa sau.**

**Tin tốt:** việc gộp tỉnh **chưa đụng gì tới dữ liệu**. Lịch xổ 21/21 ô khớp, mỗi đài đủ 17/17
ngày, 105 luật trỏ trúng hết. Các công ty xổ số giữ nguyên tên thương hiệu.

**Nhưng tìm ra một lỗ hổng im lặng đã từng sập một lần** — và nguyên nhân gốc là chữ `Đ` tiếng
Việt không tách dấu được theo NFKD.

## 2. Owner yêu cầu gì (nguyên văn)

> *"Ah còn 1 việc là hiện các tỉnh thành đã gộp nên 1 số đài tên đài lịch sổ đều bị thay đổi em
> xem kỹ dùm anh nha em. Mỗi nơi đặt mỗi tên gọi khách nhau như khánh hòa có chỗ là KH hay TP
> HCM, chỗ thì tp hồ chí minh."*

> *"tất cả xử lý xong cần deploy đầy đủ đừng để hỏng hệ thống nha em."*

## 3. Đào bới / phát hiện

### 3.1 Việc gộp tỉnh CHƯA đụng gì tới dữ liệu · `VERIFIED_TEST`

| kiểm | kết quả |
|---|---|
| Lịch xổ khai trong `scheduler.EXPECTED_STATION_COUNT` vs thực tế 120 ngày | **21/21 ô KHỚP** |
| Đài nào xổ thứ nào | mỗi đài đủ **17/17 ngày**, không lệch một ngày |
| 105 luật đang bật trỏ vào đài có thật | **0 luật hỏng** |
| Tên đài mới xuất hiện từ 2025 | **không có** |
| Biến thể chính tả trong DB | **không có** (trừ 1 dòng `Đắc Nông` từ 2021) |

41 đài vẫn xổ đều tới 04/08/2026.

### 3.2 Nhưng có lỗ hổng IM LẶNG — đã sập một lần rồi · `VERIFIED_CODE`

`canonical_station()` trả về **nguyên văn** khi không nhận ra tên (đúng theo docstring:
*"Unknown names are returned stripped, preserving the source spelling"*). Mọi chỗ tra cứu theo
tên chính xác sau đó **im lặng trả rỗng** — không nổ, không log, không cảnh báo.

**Đã xảy ra thật:** ngày **03–07/07/2026** nguồn `xskt.com.vn` đổi sang mã ngắn
`GL`/`NT`/`DLK`/`QNA`; `mined_rule_eval` và shadow AB âm thầm không ra gì. V10810 mới vá bằng
cách thêm từng mã một.

Thử **116 cách viết tên**: nhận đúng **66**, KHÔNG nhận ra **50**, nhận nhầm **0**.

### 3.3 Lỗi gốc: chữ `Đ` không tách dấu được · `VERIFIED_TEST`

`_identity_key()` dùng `unicodedata.normalize("NFKD", …)` rồi bỏ ký tự tổ hợp. Cách này xử lý
được `à`, `ạ`, `ă`… nhưng **`Đ`/`đ` (U+0110/U+0111) là chữ CÓ GẠCH NGANG, không phải chữ + dấu**
— NFKD không tách được.

```
_identity_key("Đà Lạt")  →  "đalat"
_identity_key("Da Lat")  →  "dalat"     ← hai khoá KHÁC NHAU
```

Đó chính là lý do bảng bí danh cũ phải liệt kê tay từng bản bỏ dấu: `Da Nang`, `Dak Lak`,
`Dak Nong`, `Binh Dinh`, `Quang Nam`… — **vá từng cái thay vì vá gốc**.

Hệ quả: **cả họ chữ Đ** (Đà Nẵng · Đắk Lắk · Đắk Nông · Đà Lạt · Đồng Nai · Đồng Tháp) đều
không khớp được bản bỏ dấu nào chưa liệt kê sẵn.

### 3.4 Bảng bí danh thiếu chính tên đài · `VERIFIED_CODE`

`STATION_ALIASES` có mã ngắn `"KH": "Khánh Hòa"` nhưng **KHÔNG có** chính `"Khánh Hòa"`. Nên
`Khanh Hoa` (bỏ dấu) rơi thẳng xuống nhánh trả-về-nguyên-văn. Đúng ví dụ owner nêu.

## 4. Hướng xử lý và vì sao chọn

**Vá gốc chứ không vá từng cái.** Đổi `Đ→D` trước NFKD thì cả họ chữ Đ tự khớp — thay vì tiếp
tục thêm từng biến thể mỗi lần nguồn đổi cách viết.

**Thêm danh sách 41 đài chuẩn** thay vì liệt kê từng biến thể. Có danh sách này thì mọi cách
viết bỏ dấu tự khớp.

**TỪ CHỐI đoán tên mơ hồ.** `Lâm Đồng` sau gộp có thể là **Đà Lạt hay Bình Thuận hay Đắk Nông**
— ba đài khác nhau. Mã `BD` `ĐN` `QN` cũng mơ hồ. **Đoán sai nguy hiểm hơn trả rỗng**: trả rỗng
thì mất số và cảnh gác bắt được; đoán sai thì **lấy số từ đài khác** mà không ai biết.

## 5. Đã làm gì

| | |
|---|---|
| `_identity_key()` | đổi `Đ→D`, `đ→d` **trước** NFKD |
| `CANONICAL_STATIONS` | 41 đài đang sống, đọc từ `lottery_results` |
| tên tỉnh MỚI không mơ hồ | `Hưng Yên`→Thái Bình · `Ninh Bình`→Nam Định · `Thành phố Huế`→Thừa Thiên Huế · `Bắc Giang`→Bắc Ninh · `Hải Dương`→Hải Phòng |
| mã ngắn không mơ hồ | 27 mã (CM, VL, TG, AG, KG, BL, LA, TN, BP, CT, HG, ST, TV…) |
| dạng `Tỉnh mới (Đài cũ)` | lấy vế **trong ngoặc** vì đó mới là đài thật |
| `AMBIGUOUS_MERGED_NAMES` | `Lâm Đồng` — cấm ánh xạ |
| `AMBIGUOUS_SHORT_CODES` | `BT` `BD` `ĐN` `DN` `QN` — cấm ánh xạ |
| `_v11006_ten_dai.py --canh-gac` | cảnh gác hằng ngày, tên lạ là báo ngay |

**Kết quả: nhận đúng 66 → 111/116.** Năm cái còn lại là **cố ý từ chối đoán**.

## 6. Cổng kiểm

**An toàn trước khi đẩy:**

| kiểm | kết quả |
|---|---|
| bí danh cũ bị đổi nghĩa | **0/39** |
| va chạm khoá sau khi đổi `Đ→D` | **0** |
| tên đài đang có trong DB bị đổi cách gom | **0** |

Riêng `Đắc Nông`→`Đắk Nông` là **hành vi đã có sẵn** từ trước V11006 (dòng
`"Đắc Nông": "Đắk Nông"` có trong bảng cũ), không phải hành vi mới.

**Deploy — thử TRÊN VPS trước khi restart:**

```
'Khanh Hoa' → 'Khánh Hòa'          'Da Lat' → 'Đà Lạt'
'KH' → 'Khánh Hòa'                 'Dak Lak' → 'Đắk Lắk'
'TP HCM' → 'TP. HCM'               'Hưng Yên' → 'Thái Bình'
'Thành phố Hồ Chí Minh' → 'TP. HCM'  'Cần Thơ (Hậu Giang)' → 'Hậu Giang'
'Lâm Đồng' → 'Lâm Đồng'   ← từ chối đoán, ĐÚNG
'BD' → 'BD'  ·  'QN' → 'QN'         ← từ chối đoán, ĐÚNG
```

**Sau restart:**

| | |
|---|---|
| PID | `930315` → `936322` **KHÁC** (tiến trình cũ đã chết) |
| `predictions` | `0dffcdf61c1ce69ae8a2…` 11.875 dòng — **y hệt** |
| `final_bundles` | `3edfafe6465b0612bfc5…` 480 dòng — **y hệt** |
| `lottery_results` | `1543b2e7de4592e01306…` 15.226 dòng — **y hệt** |
| `model_daily_eval` | `6175b0e1e91c515bb8a6…` 11.739 dòng — **y hệt** |
| luật trỏ hỏng | 0 → **0** |
| `/api/health` | **200** sau ~10s |
| cảnh gác trên VPS | `TEN_DAI=DAT DAI_SONG=41 BI_DANH=360 TEN_LA=0` |

`[cong] V11006_DEPLOY=DAT HASH_DOI=0 PID_KHAC=True LUAT_HONG=0`

## 7. Vướng vấp

**Script deploy có một cổng chặn đúng chỗ.** Trước khi restart, nó chạy bản mới **ngay trên
VPS** và so cách gom tên đài trước/sau. Chỉ chấp nhận đúng **một** thay đổi đã biết
(`Đắc Nông`→`Đắk Nông`); bất kỳ tên nào khác đổi cách gom là **DỪNG, không restart** — vì đổi
cách gom là đổi số.

**Smoke test của agent gõ nhầm tên endpoint.** Kiểm `/api/admin/rule-drift` mong 401 nhưng ra
404 — endpoint đó không tồn tại. Lỗi ở câu kiểm, không phải ở hệ; `/api/health` = 200 đúng.

**Vòng đầu chỉ nâng được 66 → 92.** Còn `Da Lat`, `Dak Lak` vẫn trượt. Phải đào tiếp mới ra
nguyên nhân `Đ` không tách dấu — nếu dừng ở 92 thì đã bỏ sót cả họ chữ Đ.

## 8. Gỡ về

```bash
# trên VPS
cp /root/Lottery_AI_Test/backups/v11006_pre_vps/station_identity.py.pre \
   /root/Lottery_AI_Test/web/backend/station_identity.py
systemctl restart lottery
```

Bản local: `backups/v11006_pre/station_identity.py.pre` md5 `e172e73a4ed8488f382743c02daf9d4c`.
Bốn script kiểm đẩy kèm không ai import — xoá đi cũng không ảnh hưởng runtime.

## 9. Theo dõi tiếp

| Mã | Nội dung | Hạn |
|---|---|---|
| **FU-292** | Nối `_v11006_ten_dai.py --canh-gac` vào cron hằng ngày + thêm vào sổ diễn tập. Ngưỡng: `TEN_LA` > 0 ⇒ báo đầu phiên | 13/08 |
| **FU-293** | Owner quyết cách xử tên MƠ HỒ. Nếu nguồn đổi sang `Lâm Đồng` thì đó là đài nào? Hoặc phân biệt bằng **THỨ** (mỗi đài xổ thứ khác nhau) | 13/08 |

**Con số cần nhớ:** nhận đúng **66 → 111/116** cách viết · **0** nhận nhầm · **5** cái còn lại
là cố ý từ chối đoán.
