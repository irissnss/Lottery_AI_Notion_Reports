# REPORT V11013 — Xếp lại mốc thời gian: 24/12 → 27/08, và rải 16 mục dồn một ngày

> **Ngày:** 2026-08-07 · **Owner:** *"cái gì mà đợi tới 24/12 hết năm kiểu này"*
> **Dữ liệu:** đồng bộ `07/08 00:31` · cổng FU-303 ĐẠT

---

## 1. Tóm tắt

Owner đúng ở cả hai chỗ. Mốc **24/12** không phải vì việc khó — mà vì **agent hỏi sai câu**.
Và ngày **13/08 dồn 16 mục**, trong đó **15 mục do chính agent đặt** vì mặc định "13/08" cho
mọi việc.

| | trước | **sau** |
|---|---|---|
| FU-286 (đo tiến bộ đào luật) | 24/12/2026 | **27/08/2026** |
| FU-285 (bản đóng băng) | 06/11 một phát | **07/09 · 07/10 · 07/11**, dừng sớm được |
| Ngày 13/08 | **16 mục** | **1 mục** |
| Ngày xa nhất | 24/12 (139 ngày) | **19/09 (43 ngày)** |

Ngoài ra tìm ra một lỗi **làm cổng trần tải đếm sai**: sổ đang dùng **hai định dạng ngày**.

## 2. Owner yêu cầu gì (nguyên văn)

> *"cái gì mà đợi tới 24/12 hết năm kiểu này thôi chứ làm gì với dự án bé tẹo này, làm tiếp đi
> nhưng cân đối thời gian hạn mốc tương đối ổn hơn đẹp hơn đi"*

## 3. Đào bới / phát hiện

### 3.1 Vì sao ra 24/12 — agent hỏi sai câu · `VERIFIED_TEST`

Cổng M4 của agent đặt **`MAU_TOI_THIEU_DO_TIEN = 20` CHO MỖI LUẬT**. Mỗi luật chỉ được chấm vào
**đúng THỨ của nó** ⇒ **1 lượt/tuần/luật** ⇒ 20 tuần = **140 ngày**.

Nhưng đó là câu hỏi **TỈA TỪNG LUẬT** (*"giữ luật A, bỏ luật B"*). Câu hỏi **đang chặn quyết
định** (FU-291) là câu hỏi **LỚP**: *"cơ chế `mined_rules` có lợi thế đo tiến không?"* — câu đó
**gộp được 105 luật**.

| | nhịp | dùng để |
|---|---|---|
| hỏi TỪNG LUẬT | 1 lượt/tuần/luật | tỉa từng luật — **chưa cần tới** |
| **hỏi CẢ LỚP** | **15 dòng/ngày** (nhanh hơn 15 lần) | **giữ hay bỏ cả cơ chế** — đúng cái FU-291 cần |

**Tính lại mẫu cần** (McNemar theo cặp, nền hiện tại 64,4%, sức mạnh 80%, α=0,05):

| chênh muốn phát hiện | cặp cần | còn thiếu | **ngày đạt** |
|---|---|---|---|
| +15 điểm | 140 | 95 | 14/08 |
| **+10 điểm** | **332** | **287** | **27/08** |
| +7,5 điểm | 605 | 560 | 14/09 |
| +5 điểm | 1.390 | 1.345 | 05/11 |

**Chọn +10 điểm ⇒ 27/08.** Nếu tới đó lớp **không** có lợi thế thì **bỏ cả cơ chế**, khỏi phải
tỉa từng luật — câu hỏi 24/12 **tự tan**. Chỉ khi lớp **có** lợi thế mới cần mốc dài.

### 3.2 FU-285 — một mốc 3 tháng đổi thành ba mốc hằng tháng

Trước: chấm **một phát 06/11** (91 ngày). Nay: **07/09 · 07/10 · 07/11**.

Cùng tổng công sức nhưng thấy **xu hướng** và **dừng sớm được**: `|z| ≥ 2` ở bất kỳ mốc nào ⇒
kết luận ngay, không chờ 07/11. Thông tin về sớm hơn **2 tháng**.

### 3.3 PHÁT HIỆN MỚI — sổ dùng HAI định dạng ngày, cổng trần tải đếm sai · `VERIFIED_TEST`

| định dạng | số mục |
|---|---|
| `2026-08-13` (ISO) | **51** |
| `13/08` (DD/MM) | **32** |

Cổng J5 (trần tải mỗi ngày) đếm theo **chuỗi hạn**, không quy chuẩn ngày ⇒ `13/08` và
`2026-08-13` bị coi là **hai ngày khác nhau** ⇒ **ngày nặng thật sự bị giấu đi**.

Sau khi gộp về cùng ngày, tải thật trước khi xếp lại:

| ngày | mục |
|---|---|
| 06/08 | 8 (**quá hạn**) |
| 08/08 | 11 |
| 09/08 | 9 |
| **13/08** | **16** |
| 15/08 | 12 |

### 3.4 15/16 mục dồn 13/08 là do agent

`FU-277 · FU-288 · FU-289 · FU-292 · FU-294 · FU-295 · FU-296 · FU-301 · FU-302 · FU-305 ·
FU-306 · FU-307 · FU-308 · FU-309 · FU-310 · FU-313` — agent mặc định gán "13/08" cho mọi việc
mới thay vì cân theo mức ưu tiên.

## 4. Hướng xử lý và vì sao chọn

**Rải theo mức ưu tiên thật**, không rải đều:

| ngày | tiêu chí | mục |
|---|---|---|
| **08/08** | chặn quyết định hoặc ngăn tái phạm | FU-290 · FU-303 · FU-311 · FU-312 |
| **11/08** | sửa thước đo | FU-294 · FU-304 · FU-310 |
| **12/08** | làm rõ số cũ | FU-307 · FU-308 |
| **14/08** | cổng và dọn dẹp | FU-288 · FU-289 · FU-296 |
| **17/08** | hạ tầng đo | FU-292 · FU-301 · FU-306 |
| **19/08** | rà diện rộng | FU-277 · FU-302 · FU-309 |
| **21/08** | chờ owner + cổng dài hạn | FU-295 · FU-313 |
| **27/08** | đo dài — theo mốc đo thật | FU-286 |

**Chỉ đổi hạn các mục agent tự mở.** Ba ngày còn nặng (08/08=10 · 09/08=9 · 15/08=12) là mục của
**phiên khác** — agent **không tự dời**.

**Ban đầu xếp vào 10/08 nhưng cổng `QD-022` chặn** — owner đã ký 04/08 rằng **10/08 là ngày chốt,
trần 3 mục**. Đã dời sang 11/08. Cổng làm đúng việc.

## 5. Đã làm gì

Đổi hạn **21 mục** trong `docs/FOLLOW_UP_TRACKER.md` (kèm mã đọc mới theo §58) ·
FU-285 đổi thiết kế từ một mốc thành ba mốc · cập nhật bảng mốc tải `_v10982_lich9.py`.

**Không đụng code production, không deploy.** Backup tracker trước khi sửa.

## 6. Cổng kiểm

| | |
|---|---|
| Bảng mốc tải J5 | **không lệch** |
| `QD-022` (trần 10/08 = 3) | **ĐẠT** sau khi dời sang 11/08 |
| `QD-027` | trượt — **dương tính giả đã biết** (FU-310: chạy lúc 01:0x, materializer chưa chạy) |
| Ngày xa nhất | **19/09** (43 ngày), trước là 24/12 (139 ngày) |
| Ngày 13/08 | **16 → 1** mục |

## 7. Vướng vấp

**Mốc 24/12 không đến từ việc khó mà từ câu hỏi sai.** Agent đặt cổng *"n≥20 cho mỗi luật"* mà
không hỏi lại: **câu hỏi nào đang thật sự chặn quyết định?** Hoá ra là câu hỏi lớp — gộp được,
nhanh hơn 15 lần.

Đây cùng họ với lỗi §60 đã ký: **làm đúng kỹ thuật nhưng sai phạm vi**.

**Và thói quen đặt hạn cho có.** 15 mục cùng gán "13/08" nghĩa là agent **không cân nhắc mức ưu
tiên** khi mở việc — chỉ chọn một ngày trông xa xa cho đủ trường.

## 8. Gỡ về

Backup `docs/FOLLOW_UP_TRACKER.md` trước khi sửa lưu tại scratchpad phiên. Đổi hạn không ảnh
hưởng runtime — chỉ ảnh hưởng thứ tự làm việc.

## 9. Theo dõi tiếp

| Mã | Nội dung | Hạn |
|---|---|---|
| **FU-286** | **24/12 → 27/08.** Đổi thiết kế: hỏi **cả lớp** (332 cặp, nhịp 15/ngày) thay vì từng luật. Lớp không có lợi thế ⇒ bỏ cả cơ chế, khỏi tỉa | 27/08 |
| **FU-285** | **06/11 → 07/09 · 07/10 · 07/11.** Chấm hằng tháng, `\|z\|≥2` ở bất kỳ mốc nào ⇒ kết luận sớm | 07/09 |
| **FU-314** | **Sổ dùng hai định dạng ngày** (ISO 51 mục · DD/MM 32 mục) ⇒ cổng trần tải J5 đếm sai, ngày nặng bị giấu. Quy chuẩn về MỘT định dạng + sửa bộ đọc quy chuẩn trước khi đếm | 12/08 |
| **FU-315** | **Ba ngày còn nặng của phiên khác** — 08/08 (10) · 09/08 (9) · 15/08 (12). Agent không tự dời; trình owner xem có giãn không | 08/08 |

**Ba con số cần nhớ:** 24/12 → **27/08** (hỏi đúng câu, nhanh hơn 15 lần) · 13/08 **16 → 1** mục ·
ngày xa nhất **139 → 43** ngày.
