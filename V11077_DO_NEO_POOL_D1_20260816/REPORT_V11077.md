# REPORT V11077 (FU-316) — POOL D-1 BỊ CẮT CÓ **NEO** MODEL VỀ ĐUÔI THẤP KHÔNG?

> ### ⚠ BÁO CÁO BÙ — hai ngày khác nhau, đừng đọc nhầm
>
> | | |
> |---|---|
> | **việc xảy ra** | **16/08/2026 18:56** — commit `a33b86a` |
> | **báo cáo này viết** | **17/08/2026** (`V11083` / `GĐ-5`) |
>
> Bản này **trôi mất** báo cáo công khai lúc đó — và trôi **34 phút sau** khi phiên vừa bù xong
> 12 bản khác, mà cổng vẫn **báo xanh**. Chỗ mù ấy đã vá ở `V11082`.
>
> **Nguồn viết bù:** bản ghi của **chính phiên gốc** (phiên viết bản này là phiên đã chạy phép
> đo). Owner khoá **phương án (a)** lúc 12:57 ngày 17/08 — *«CHỈ phiên gốc viết bù từ bản ghi
> của chính nó (RM-17)… CẤM tự chuyển sang soạn từ commit message hay nguồn khác»*.
> Mọi con số dưới đây **tái lập được** bằng `web/backend/_v11077_do_neo_pool_d1.py`.

---

## 1. Tóm tắt

Một dòng trong prompt cắt **83%** pool D-1 rồi mới bơm cho model. Nghi vấn: dòng cắt đó có
**neo** model về nhóm đuôi thấp không?

**Đăng ký ngưỡng TRƯỚC khi chạy** — `CÓ NEO ⇔ chênh ≥ +2,5pp VÀ |z| ≥ 2`.

**Kết quả NGƯỢC với dự đoán của cả agent lẫn bản đào:** model chọn đuôi `00–21` ở **20,2%**,
nền **21,0%** ⇒ **−0,79pp · z = −1,01** ⇒ **KHÔNG NEO**. `FU-316` đóng theo **nhánh 2**.

---

## 2. Owner yêu cầu gì (nguyên văn)

> *«làm hết đi giao nhiệm vụ thì làm đi, làm sao phải tổng lực không rơi rớt, phải tìm cho ra chỗ
> cải tiến nâng cao dự đoán, cấm đoán bừa, suy diễn»*

Câu **«cấm đoán bừa, suy diễn»** là lý do phép đo này tồn tại ở dạng **đăng ký ngưỡng trước**,
chứ không phải dạng đọc code rồi kết luận.

---

## 3. Đào bới / phát hiện

**Dòng bị nghi**, `gpt_analyzer.py:5958` — nằm trong vùng **QD-041 khoá tới 21/08**:

```python
f"- D-1 cross-region tail pool: {', '.join(sorted(d1_union)[:12])}"
```

Hai dấu hiệu làm cả agent lẫn bản đào nghiêng về **«có neo»**:

| dấu hiệu | số |
|---|---|
| phần pool bị cắt trước khi bơm | **83%** |
| số ngày mà 12 đuôi còn lại **không chứa** đuôi nào > 21 | **30/30** |

`sorted()` trên chuỗi hai chữ số ⇒ `[:12]` gần như luôn giữ nhóm **thấp nhất**. Nghe rất thuyết
phục — và đó chính là chỗ nguy hiểm.

---

## 4. Hướng xử lý và vì sao chọn

**Đăng ký ngưỡng TRƯỚC khi chạy, ghi vào script rồi mới đo:**

```
CÓ NEO  ⇔  chênh ≥ +2,5pp  VÀ  |z| ≥ 2
```

Vì sao phải đăng ký trước: khi **đã tin** vào một giả thuyết, mọi con số đều đọc được thành ủng
hộ nó. Ngưỡng đăng ký sau là ngưỡng **đặt vừa khít quanh kết quả**.

Nền đúng là **tỉ lệ đuôi `00–21` trong kết quả thật**, không phải `22/100` — `RM-18` cấm so tỉ lệ
của một bộ đuôi với nền của một số.

---

## 5. Đã làm gì

Dựng `web/backend/_v11077_do_neo_pool_d1.py` — đọc số model **thật sự chọn**, đối chiếu nền:

| | |
|---|---|
| model chọn đuôi `00–21` | **20,2%** |
| nền | **21,0%** |
| chênh | **−0,79pp** *(ngược dấu so với dự đoán)* |
| z | **−1,01** |
| ngưỡng đã đăng ký | ≥ +2,5pp **và** \|z\| ≥ 2 |
| **kết luận** | **KHÔNG NEO** — `FU-316` đóng theo **nhánh 2** |

**Không đụng** `gpt_analyzer.py`: `QD-041` khoá vùng này tới 21/08, và phép đo vừa nói **không có
gì để sửa**.

---

## 6. Cổng kiểm

| cổng | kết quả |
|---|---|
| `RM-01` tuổi dữ liệu (nằm sẵn trong script) | **✓** lúc chạy 16/08 |
| ngưỡng đăng ký trước | **✓** ghi trong script **trước** khi chạy |
| nền đúng theo `RM-18` | **✓** nền = tỉ lệ đuôi `00–21` thật |

> Chạy lại **hôm nay 17/08** thì script trả **`✗ RM-01: dữ liệu cũ 19,3 giờ ⇒ TỪ CHỐI CHẠY`** —
> đó là **cổng đang làm đúng việc**, không phải hỏng. Muốn tái lập thì đồng bộ dữ liệu sống trước.

---

## 6bis. §62 (A60) — NGUỒN BA LỚP

**`OWNER_SAID`** · 16/08: *«phải tìm cho ra chỗ cải tiến nâng cao dự đoán, cấm đoán bừa, suy
diễn»* · 17/08 12:57: *«CHỈ phiên gốc viết bù từ bản ghi của chính nó (RM-17)»*

**`CODE_DID`** · `gpt_analyzer.py:5958` cắt `[:12]` ⇒ giữ **83%** phần thấp · đo thật:
**20,2% vs 21,0% ⇒ −0,79pp, z = −1,01** · `_v11077_do_neo_pool_d1.py`, commit `a33b86a`

**`DOC_SAID`** · `FU-316` mô tả nghi vấn *«dòng cắt neo model về đuôi thấp»* — **LỆCH với
`CODE_DID`**: nghi vấn **không đứng vững**. Sổ đã cập nhật, `FU-316` đóng theo **nhánh 2**.

---

## 7. Vướng vấp

**Cái bẫy suýt sập:** agent **và** bản đào 49 tác nhân đều nghiêng về «có neo» **trước khi đo**.
Nếu không đăng ký ngưỡng trước, báo cáo này đã ghi *«tìm ra nguyên nhân»* cho một thứ **không tồn
tại** — và owner sẽ mất công đi kiểm hộ.

---

## 8. Gỡ về

Không có gì để gỡ — phép đo **read-only**, không sửa dòng nào trong đường dự đoán.

---

## 9. Theo dõi tiếp

**Giới hạn phải nói rõ:** đây là **một** ca, đo **một** cơ chế. **Cấm** suy rộng thành *«mọi việc
nhồi nhét vào prompt đều vô hại»* — `FU-404` (nhãn `HR12W 1.0` **nói quá** giá trị thật) vẫn còn
nguyên trong gói 21/08.

| mã | việc | trạng thái |
|---|---|---|
| `FU-316` | neo pool D-1 | **ĐÓNG — nhánh 2 (không neo)** |
| `FU-404` | nhãn `HR12W` nói quá | còn mở, gói 21/08 |

**Verdict:** `CODE_PUSHED` = `a33b86a` (16/08) · `REPORT_PUBLISHED` = bản này (**bù 17/08**)

---

TanPhatAI cần làm: ghi `FU-316` **ĐÓNG theo nhánh 2 — KHÔNG NEO** (`−0,79pp · z = −1,01`, ngược
dấu dự đoán); ghi rõ đây là **báo cáo BÙ** — việc xảy ra **16/08**, viết **17/08**, nguồn là bản
ghi của **chính phiên gốc** theo phương án (a) owner khoá 12:57; và **cấm** trích kết quả này để
kết luận chung về việc nhồi ngữ cảnh — `FU-404` vẫn mở.
