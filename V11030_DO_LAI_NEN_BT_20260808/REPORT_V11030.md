# REPORT V11030 — ĐO LẠI NỀN CHO ĐÚNG: BẠCH THỦ 1 SỐ vs LUẬT k ĐUÔI

**Ngày:** 2026-08-08 · **Loại:** audit / đo lường · **Chỉ đọc, không đụng production**

---

## 1. Tóm tắt

Owner chỉ ra một chỗ agent nói sai. Agent từng viết *"`hit_any` là thước gần như vô nghĩa"*.
**Owner đúng, agent sai.** Thước không vô nghĩa — **phép so** mới sai.

Đo lại bằng nền đúng, kết quả **lật một kết luận cũ và củng cố một kết luận khác**:

| | trước (V11024 R4) | nay (V11030) |
|---|---|---|
| **luật soi cầu** | *"20/21 ô NGANG NỀN"* | **HƠN NỀN** cả 3 miền: +7,3 / +13,3 / +20,0 điểm |
| **bạch thủ official** | chưa đo riêng bằng nền 1 số | **NGANG NỀN** cả 3 miền |
| **nhưng tách trong/ngoài cửa sổ chọn** | — | TRONG **+7,5/+13,8/+20,7** · NGOÀI **+2,2/−0,7/−1,5** |

Kết luận cuối **không đổi** (luật chưa chứng minh được kỹ năng đo tiến), nhưng **lý do phải nói
cho đúng**: không phải vì luật ngang nền, mà vì lợi thế **chỉ tồn tại trong chính cửa sổ dùng để
chọn luật**.

---

## 2. Owner yêu cầu gì (NGUYÊN VĂN)

> giờ đo lại hit any đúng không em? việc đang làm nhất đó hả. Đúng là số bạch dù gọi là bạch thủ
> nhưng số dự đoán trúng ở bất kỳ giải nào của đài thuộc thứ hôm đó đều được tính, miễn là số hit
> càng nhiều càng tốt không phải bạch thủ là phải nhất quyết nằm ở GB hay Giải Đặc Biệt nên độ dễ
> của dự đoán đã được nới lỏng rồi mà em. Xem kiểm tra lại dùm anh nhé

---

## 3. Đào bới / phát hiện

### 3.1 Agent sai ở đâu — nói thẳng

Agent lập luận: *"luật có `hit_any` 90–98% vì nền cao tới 86,8% — thước vô nghĩa"*.

**Lỗi logic:** nới lỏng *"trúng ở bất kỳ giải nào"* áp cho **CẢ HAI** bên — model official cũng
được tính y hệt. Một điều kiện áp cho cả hai bên thì **không giải thích được chênh lệch giữa hai
bên**. Agent lấy một đặc điểm chung đi giải thích một khác biệt riêng.

### 3.2 Thứ THẬT SỰ giải thích được: **k**

| | model official | luật soi cầu |
|---|---|---|
| ra bao nhiêu số | **1** (bạch thủ) | **k đuôi** |
| k thực đo | 1 | MN **4,45** · MT **4,10** · MB **2,82** |
| nền ĐÚNG để so | `b` | **`1 − (1−b)^k`** |

Agent đem tỉ lệ của **một bộ k đuôi** so với nền của **một số**. Sai từ gốc — và đó chính là lỗi
làm R4 (V11024) kết luận nhầm.

### 3.3 Nền thật (99 ngày, từ 01/05/2026)

`b` = số **đuôi khác nhau** ra trong ngày đó ở miền đó, chia 100.

| miền | ngày đo | đuôi khác nhau/ngày | nền 1 số |
|---|---|---|---|
| MN | 99 | 42,65 | **42,6%** |
| MT | 99 | 35,17 | **35,2%** |
| MB | 99 | 23,68 | **23,7%** |

---

## 4. Hướng xử lý và vì sao chọn

**Chọn:** viết một script **chỉ đọc** đo bốn phần tách bạch, không sửa gì.

**Vì sao không sửa `hit_any` trong code:** thước không hỏng. Sửa thước để chữa một phép so sai là
chữa nhầm chỗ — và sẽ làm mọi số lịch sử không so được với nhau nữa.

**Vì sao thêm hiệu chỉnh cụm ngày (VIF = 2,92):** 16 model cùng đoán MỘT ngày thì 16 lượt đó
**không độc lập** — chúng cùng ăn theo độ khó của ngày. R6 đo 2,91×, R9 đo độc lập ra 2,92×.
Bản chạy đầu **chưa có VIF** và ra `z = −2,39 / +1,25 / −2,30` ⇒ sẽ kết luận nhầm *"DƯỚI NỀN"*.
Bỏ VIF là thổi `z` lên **~1,7 lần**.

---

## 5. Đã làm gì

**TRƯỚC:** R4 (V11024) kết luận *"20/21 ô NGANG NỀN"*, so `hit_any` của luật với nền **1 số**.
**SAU:** `web/backend/_v11030_do_lai_nen_bt.py` — 4 phần, nền đúng theo từng loại.
**PHIÊN BẢN:** V11030 · 08/08/2026 · script mới, **không sửa file production nào**.
**KIỂM:** `python web/backend/_v11030_do_lai_nen_bt.py`

### PHẦN 2 — BẠCH THỦ OFFICIAL (1 số) vs nền 1 số

| miền | lượt | trúng | tỉ lệ | nền | chênh | z | kết luận |
|---|---|---|---|---|---|---|---|
| MN | 1.488 | 589 | 39,6% | 42,6% | −3,1 | −1,40 | **NGANG NỀN** |
| MT | 1.480 | 544 | 36,8% | 35,2% | +1,6 | +0,73 | **NGANG NỀN** |
| MB | 1.490 | 315 | 21,1% | 23,7% | −2,5 | −1,35 | **NGANG NỀN** |

Khớp với kết luận cũ *"0/34 model hơn nền"*, nay đo bằng **thước đúng của bạch thủ 1 số**.

### PHẦN 3 — LUẬT (k đuôi) vs nền `1−(1−b)^k`

| miền | lượt | k tb | hit_any | nền k đuôi | chênh | z | kết luận |
|---|---|---|---|---|---|---|---|
| MN | 490 | 4,45 | 94,7% | 87,4% | **+7,3** | **+2,86** | **HƠN NỀN** |
| MT | 490 | 4,10 | 89,8% | 76,5% | **+13,3** | **+4,07** | **HƠN NỀN** |
| MB | 490 | 2,82 | 70,0% | 50,0% | **+20,0** | **+5,19** | **HƠN NỀN** |

**ĐÍNH CHÍNH R4.** Với nền đúng, luật **hơn nền rõ rệt** — ngược hẳn kết luận cũ.

### PHẦN 4 — tách TRONG / NGOÀI cửa sổ chọn luật (mốc 03/08/2026)

`_seed_rules` chọn top-5 bằng cửa sổ **365 ngày kết thúc `mined_at` = 03/08/2026**. Mọi ngày
≤ 03/08 là dữ liệu **đã dùng để chọn chính các luật đó**.

| miền | đoạn | lượt | hit_any | nền k | chênh | z |
|---|---|---|---|---|---|---|
| MN | **TRONG** cửa sổ chọn | 475 | 94,9% | 87,4% | **+7,5** | **+2,89** |
| MN | **NGOÀI** cửa sổ chọn | 15 | 86,7% | 84,4% | +2,2 | **+0,14** |
| MT | **TRONG** | 475 | 90,5% | 76,8% | **+13,8** | **+4,16** |
| MT | **NGOÀI** | 15 | 66,7% | 67,4% | −0,7 | **−0,03** |
| MB | **TRONG** | 475 | 70,7% | 50,0% | **+20,7** | **+5,28** |
| MB | **NGOÀI** | 15 | 46,7% | 48,2% | −1,5 | **−0,07** |

**Trong cửa sổ chọn: +7,5 · +13,8 · +20,7. Ngoài cửa sổ: +2,2 · −0,7 · −1,5 — tức ĐÚNG BẰNG
KHÔNG.** Ba miền độc lập, cùng một hình dạng.

Đây là **dấu vân tay của thiên vị chọn**, nay đo được bằng **nền đúng** thay vì nền sai —
khớp độc lập với R2 (V11024) đo lift **1,084 trong cửa sổ** vs **1,000 ngoài cửa sổ**.

---

## 6. Cổng kiểm

| cổng | kết quả |
|---|---|
| Không sửa production code | **ĐẠT** — chỉ thêm 1 script mới `_v11030_*` |
| Không ghi bảng nào | **ĐẠT** — mở DB bằng `mode=ro` |
| Không đụng 4 bảng khoá | **ĐẠT** — không có câu `INSERT`/`UPDATE`/`DELETE` nào |
| Không đụng `gpt_analyzer.py` (QD-041) | **ĐẠT** |
| Chạy lại ra y hệt | **ĐẠT** — thuần đọc + số học, không có nguồn ngẫu nhiên |
| Sổ quyết định | 1 phép TRÔI (tồn từ trước, không phát sinh mới) |

---

## 7. Vướng vấp

**7.1 — Bản chạy đầu KẾT LUẬN NHẦM "DƯỚI NỀN".** Chưa hiệu chỉnh cụm ngày, `z` ra
−2,39 / +1,25 / −2,30 ⇒ MN và MB sẽ bị gán *"DƯỚI NỀN"*. Thêm `VIF = 2,92` mới ra đúng
**NGANG NỀN**. Bài học: **thêm VIF là bắt buộc ở MỌI phép đo trên `predictions`**, vì bảng này
luôn có 16 model chung một ngày.

**7.2 — Suýt dừng ở PHẦN 3 và báo tin vui.** PHẦN 3 cho `z = +2,86 / +4,07 / +5,19` — rất dễ báo
*"luật có tín hiệu thật"*. Chỉ PHẦN 4 mới lộ ra lợi thế đó **nằm trọn trong cửa sổ chọn**.
Đúng §60.2 câu 3: *"có phép nào máy chạy được để chứng minh không?"*

**7.3 — Mẫu ngoài cửa sổ chỉ 15 lượt/miền.** Chưa đủ để kết luận chắc. Và đây chính là lý do
**A1 (V11025) quan trọng**: trước A1 con số này bị `DELETE ... WHERE date >= -112 days` **xoá về
0 mỗi thứ Hai** nên **không bao giờ lớn lên được**.

---

## 8. Gỡ về

Không cần — phiên này **không sửa gì**. Muốn bỏ thì xoá 1 tệp:

```bash
git rm web/backend/_v11030_do_lai_nen_bt.py
```

---

## 9. Theo dõi tiếp

| mã | nhãn | hạn | trạng thái |
|---|---|---|---|
| **FU-339 · TK0808** | Đính chính R4 — "20/21 ô ngang nền" so với nền SAI | 08/08 | `CLOSED_PASS` |
| **FU-340 · DO2108** | Đo lại PHẦN 4 khi mẫu ngoài cửa sổ đủ lớn | 21/08 | `WAIT_LIVE` |

**Ngưỡng hành động FU-340:** cần **≥100 lượt/miền** ngoài cửa sổ chọn.
Nếu chênh vẫn quanh 0 với `|z| < 1,96` ⇒ **luật không mang tín hiệu đo tiến**, chốt vào SSOT.
Nếu `z ≥ +1,96` ⇒ luật CÓ tín hiệu thật, mở lại bàn đưa vào ML.
