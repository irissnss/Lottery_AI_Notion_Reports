# CONVERSATION CONTEXT — V11064 (QD-064) · 11/08/2026 khuya

## Owner nói gì (NGUYÊN VĂN)

Owner ký gộp **4 quyết định** lúc **22:36**, kèm ba lưu ý. Trích những câu quyết định nhất:

> **QĐ-1:** *«D-2 cho MN: BỎ TRONG CODE… LƯU Ý QUAN TRỌNG CỦA OWNER: TÀI LIỆU VẪN GIỮ — đánh dấu
> rõ "THAM KHẢO — KHÔNG TRIỂN KHAI (đo = 0, V11056)" ngay tại mục D-2 trong tài liệu. Tài liệu
> KHÔNG bị xoá theo code; nó là bằng chứng một ý tưởng đã được đo và loại bằng số — giá trị tham
> khảo cho sau.»*

> **QĐ-2:** *«ĐỢI LUÔN TỚI 21/08 — kể cả glm-5.1, KHÔNG chỉnh timeout sớm.»* — *«cắt cũng đã cắt
> rồi thì đợi luôn»*

> **QĐ-3:** *«ĐỒNG Ý không bù 286 bản ghi cũ (RM-17: bù = chế sử). NHƯNG phải GHI NHẬN RÕ Ở MỘT
> CHỖ HỢP LÝ để tra soát khi cần… Cổng §63 K2 phải hiểu marker này, không báo đỏ oan.»*

> **QĐ-4:** *«đóng gói một lần, không nhỏ giọt… không thêm, không bớt. Mọi ý tưởng mới sinh từ nay
> tới 21/08 đi vào HÀNG ĐỢI SAU GÓI.»*

Và cuối phiên:

> *«Anh nghỉ ngủ sớm đây em xem canh xử lý tỉ mỉ cẩn thận các vấn đề đã thống nhất, đã rõ ràng dùm
> anh để sẵn sàng live ngày mai nhé.»*

---

## Việc đầu tiên là bác lại chính owner — về một con số

Owner ghi *«mã dự kiến QD-060 cho gói này»*. Nhưng `QD-060` đã dùng **sáng nay** cho bản kiểm toàn
diện, và `QD-061`, `QD-062`, `QD-063` cũng đã dùng hết **trong cùng ngày**.

Nếu agent cứ ghi theo mã owner đưa, gói 4 quyết định này sẽ **ghi đè lên bản kiểm toán sáng nay**
trong sổ.

Chạy cổng `_v11044_cong_so_hieu.py` (quét **sáu** nơi: CHANGELOG · sổ theo dõi · thư mục báo cáo ·
tên tệp `_v*.py` · sổ quyết định · `git log`) → **`QD-064`**.

Đây đúng việc cổng sinh ra để làm. Nó được dựng sau khi số hiệu va chạm **5 lần trong 2 ngày**.

---

## QĐ-1 — vì sao phải đánh dấu TẠI CHỖ, không chỉ ghi ở SSOT

Owner nói rõ *«ngay tại mục D-2 trong tài liệu»*. Đọc tài liệu thì hiểu vì sao:

```
| MN cross-region D-1/D-2 rule | _v101_shadow_pilot.py | ... | DEPLOYED |
| MN prompt V2 | ... | Adds MN D-1/D-2 rule + gan + V99 semantic guard | DEPLOYED |
```

Chữ **`DEPLOYED`** nằm ngay đó. Người đọc lướt sẽ tưởng `D-2` **đang chạy trên đường ra số
official**. Ghi ở SSOT không cứu được — vì người đọc tài liệu V101 không nhất thiết mở SSOT.

Nên khung cảnh báo đặt **ngay đầu tài liệu** + **đánh dấu từng dòng có `D-2`**. **Nội dung giữ
nguyên**, không cắt chữ nào — đúng ý owner: tài liệu là **bằng chứng một ý tưởng đã bị loại bằng
số**, không phải rác cần dọn.

Số giữ lại: **+0,031pp, CI95 trùm 0** trên 2.337 ngày mô phỏng; bản thi hành thật 133 ngày cho vế
D-2 đóng góp **riêng 1,9%** ứng viên ≈ **0,012 lượt trúng thêm/ngày**.

**Vế `D-1` không bị ảnh hưởng** — phải nói rõ, kẻo phiên sau gỡ nhầm cả hai.

---

## QĐ-3 — cái bẫy suýt biến marker thành tấm bịt mắt

Owner đòi hai thứ cùng lúc, và chúng **kéo ngược nhau**:

1. *«phải GHI NHẬN RÕ… để tra soát khi cần»* — tức marker phải làm cổng **thôi báo đỏ**;
2. *«không báo đỏ oan»* — nhưng **oan** thôi, không phải **thôi báo hẳn**.

Cách làm cẩu thả là: cho marker tính như một mục mới ⇒ `K2` thấy tệp **luôn tươi** ⇒ **xanh vĩnh
viễn**. Cổng chết mà trông như đang sống.

> Đúng lỗi `RM-15` đã ghi trong sổ: cổng đóng băng `QD-041` từng **mù hoàn toàn** vì
> `git log --since=<ngày trần>` trả rỗng, nên nó **luôn báo xanh kể từ lúc dựng**.

Thiết kế đúng: **marker giải thích quá khứ, không che tương lai.**

- `K2` **đo tuổi trên MỤC THẬT** — marker bị **loại** khỏi phép đo;
- thêm `K5` — phải **có** marker và marker phải **đủ trường** tra soát.

**Thử chặn hai chiều:**

```
giữ marker + bỏ mục thật mới   →  ĐỎ ✓  (marker KHÔNG làm mù)
dữ liệu đủ + xoá marker        →  ĐỎ ✓  (K5 đòi phải có marker)
khôi phục                      →  XANH ✓  · tệp về 344.449 byte
```

Marker ghi đủ: hai khoảng trống (sự kiện từ `2026-07-31T18:20`, commit `7eb0571`; version từ
`2026-08-04`, mục cuối `V10984`, commit `a2a7e61`), chỗ nối lại (`420cc46`), **vì sao chết**,
**quyết định không bù**, và **cách tra bù bằng `git log`**.

---

## QĐ-4 — và một cái bẫy tên gọi phải chặn trước

Danh sách 13 mục có **`D2`** (`MINED_RULES_MODE` soft→shadow). Vừa nãy QĐ-1 loại **`D-2`** (luật
chéo miền MN).

Hai ký hiệu khác nhau **đúng một dấu gạch**.

Phiên sau đọc gói sẽ hỏi *«D-2 đã loại sao còn trong gói?»* và có thể **gỡ nhầm mục #2**. Nên
cảnh báo được ghi thẳng vào mục gói trong sổ theo dõi, dạng bảng hai dòng, không giấu trong văn
xuôi.

---

## Hai lỗi của agent trong phiên — cả hai đều do đi tắt

### 1 · Sai một dấu câu, cổng bắt được

Agent viết *«THAM KHẢO**,** KHÔNG TRIỂN KHAI»* trong khi owner ký *«THAM KHẢO **—** KHÔNG TRIỂN
KHAI (đo = 0, V11056)»*.

Cổng sổ quyết định báo `→ KHÔNG THẤY trong file`. Đã sửa dùng **đúng nguyên văn**.

`§62` đòi **trích nguyên văn** — và sai một dấu câu là đủ để cổng trượt. Đó là **tính năng**.

### 2 · Một lệnh tưởng là ĐỌC hoá ra là GHI

Agent cần **đọc hai hằng số** (`TREO_STATUSES`, `DONG_STATUSES`) nên gõ
`import _v10987_governance`.

Module đó **chạy mã cấp module** và **prepend một bản `V10987` TRÙNG**:

```
CHANGELOG.md               2.302.911 → 2.308.331   (+5.420)
docs/CURRENT_TRUTH_SSOT.md 1.079.202 → 1.081.694   (+2.492)
```

Đã xác minh là bản trùng (`## V10987` xuất hiện **2 lần**), cắt **đúng khối ở đầu**, giữ nguyên
`V11064` nằm dưới. Cả hai tệp về **1 lần**.

> **Ghi nhớ cứng: `_v10987_governance.py` GHI TÀI LIỆU NGAY KHI IMPORT.** Cấm import. Đọc hằng số
> bằng cách khác.

Và đó là lý do agent **không** dùng cách "gọn" cho vấn đề tiếp theo.

---

## Chỗ agent chọn KHÔNG sửa, dù nó đang gây trôi

Cổng lịch báo `FU-283` là **mồ côi đến hạn**. Truy ra nhãn `DEPLOYED_LIVE_VERIFIED` **không nằm
trong `DONG_STATUSES` lẫn `TREO_STATUSES`** ⇒ **6 mục** mang nhãn đó **rơi khỏi mọi bộ đếm** —
đúng họ lỗi `V10980` từng làm **14 mục biến mất**.

Cách sửa gọn: thêm nhãn vào `DONG_STATUSES`. **Không làm**, vì đó là **hằng số dùng chung ảnh
hưởng 6 mục**, còn phiên này owner khoá *«CHỈ GHI NHẬN + CẬP NHẬT TÀI LIỆU»*. Làm đúng kỹ thuật
nhưng **sai phạm vi** là `RM-05`.

Thay vào đó: `FU-283` ghi nhãn **đã đăng ký** kèm **ghi rõ tầng thật**, và phát hiện hệ thống đi
vào **HÀNG ĐỢI SAU GÓI** cho owner ký.

---

## Sẵn sàng live sáng mai — điều owner dặn trước khi ngủ

| | |
|---|---|
| dịch vụ | `active` · PID `1438110` · `NRestarts=0` · health **200** |
| P4 gan (cron 21:40) | ✓ 3 dòng hôm nay |
| B1 anti-trap (21:45) | ✓ 3 dòng hôm nay |
| **độ trễ model (21:50)** — cron **mới thêm chiều nay** | ✓ **57 dòng**, chạy đúng **ngay đêm đầu tiên** |
| 4 bảng khoá | **12280 / 495 / 15259 / 12144** — nguyên vẹn |
| sổ quyết định | **0 trôi** |

Phiên này **không deploy, không restart** — bản đang chạy là bản deploy lúc chiều (V11063), đã
verify và chạy sạch cả tối.

---

## Trạng thái cuối phiên

`QD-064` vào sổ với 4 quyết định. **Gói 21/08 đã khoá phạm vi 13 mục.** `D-2` đánh dấu tham khảo,
tài liệu nguyên vẹn. `GAP_MARKER` có, cổng `K5` canh, `K2` không bị làm mù. **Không sinh mã FU
mới.**

TanPhatAI cần làm: xem mục cuối `REPORT_V11064.md` — năm việc, quan trọng nhất là ② **gói 21/08
không thêm không bớt**, ③ **`D-2` ≠ `D2`, đừng gỡ nhầm**, và ⑤ **cấm `import _v10987_governance`**.
