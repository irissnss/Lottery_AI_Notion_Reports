# CONVERSATION CONTEXT — V11079 · việc xảy ra 16/08/2026, viết bù 17/08/2026

> **BÙ.** Việc chạy lúc **16/08 19:21** (`4a7ee6d`); bản này viết **17/08** trong `V11083`/`GĐ-5`.
> Nguồn: **bản ghi của chính phiên gốc**. Owner khoá **phương án (a)** lúc **12:57 ngày 17/08**:
> *«CHỈ phiên gốc viết bù từ bản ghi của chính nó (RM-17). Nếu không còn truy cập bản ghi gốc →
> DỪNG mục này, báo owner; CẤM tự chuyển sang soạn từ commit message hay nguồn khác.»*

---

## Owner nói gì (NGUYÊN VĂN)

> *«Em phải biết rõ là cái nào nên làm trước và làm sau, cái nào đạp cái nào, cái nào chưa rõ phải
> đi tìm hiểu thêm, em phải sắp xếp đúng tuần tự lần lượt từ đơn giản đến phức tạp chứ em»*

Bản đào để lại **47 phát hiện**. Câu trên là lệnh **xếp thứ tự**, không phải lệnh làm nhiều hơn.
Mục này được chọn làm **trước** vì nó vừa **dễ nhất**, vừa **rõ nhất**, vừa thuộc loại **«cái này
đạp cái kia»**: nó đang **ăn mòn chứng cứ** của các mục khác.

---

## Khuyết tật, gọn trong hai dòng

```
_v11057_do_thuoc_chinh.py:51    docstring: «READ-ONLY, không ghi gì»
_v11057_do_thuoc_chinh.py:203   .write_text(...)  ← ghi đè artifacts/v11057/thuoc_do_chinh.json
```

Tệp bị đè chính là artifact giữ **`+0,34pp`** — con số `QD-057` viện dẫn.

---

## Nhưng phát hiện gốc chỉ ĐÚNG MỘT NỬA — và phải nói ra

| vế | phán quyết |
|---|---|
| *«tự khai READ-ONLY nhưng có ghi»* | **ĐÚNG** |
| *«đã ghi đè MẤT số +0,34pp»* | **SAI** — `git status` sạch, nội dung vẫn `n=492 · +0,34pp` |

**Không mất gì cả.** Nếu bưng nguyên vế thứ hai lên báo cáo thì owner lại phải đi kiểm hộ agent —
đúng chuyện owner đã than mệt.

Nhưng **nguy cơ là thật**, và loại nguy cơ này khó thấy nhất: lần chạy sau đè lên bản trước,
**không có triệu chứng nào**, và người sau đọc docstring sẽ tin là chạy bao nhiêu lần cũng an
toàn.

---

## Vá — nhỏ, khu trú, không chạm vùng khoá

Bản **MỐC** giữ nguyên; lần chạy sau ghi thêm bản **có dấu thời gian**. Kèm sửa docstring cho khai
**đúng**, và sửa dòng log cuối cho in **đúng tên tệp vừa ghi**.

Không chạm `QD-041`: đây là **bộ đo**, không phải prompt / chọn số / roster.

---

## Hai vấp của chính agent trong đúng bước này

**Vấp 1 — `>/dev/null` che mất lỗi.** Chạy thử có `>/dev/null` nên **không thấy** bản vá ném
`NameError: name 'datetime' is not defined` (tệp dùng `import datetime as dt`, bản vá gọi
`datetime.now()`). Lệnh vẫn «chạy xong», và nếu dừng ở đó thì báo cáo đã ghi *«đã vá»* cho một
bản vá **không chạy nổi**.

Đây **đúng lớp lỗi agent ĐÃ TỰ GHI hai lần trước đó**. Ghi ra rồi vẫn tái phạm — theo `§61`, đó
là dấu hiệu **nhắc suông đã thất bại, phải thành cổng máy**. Đã **tái phạm lần 3**.

**Bắt được vì chạy lại CÓ NHÌN OUTPUT.** Cùng bài học 13/08 và 16/08: **«lệnh chạy xong» không
bằng «việc đã xảy ra»**.

**Vấp 2 — vá xong, dòng log cuối vẫn in tên tệp cũ** ⇒ báo sai tên bản vừa ghi. Đúng loại lỗi
đang đi bắt, xảy ra ngay trong lúc đi bắt nó.

---

## Kiểm chứng

Chạy lại **2 lần**: bản mốc **không bị động** (`git status` sạch) · mỗi lần sinh **một** bản có
dấu thời gian · log in **đúng** tên tệp vừa ghi.

---

## Còn nợ — nói rõ, không lờ

`RM-07`: **vá một lỗi không phải vá cả họ lỗi.** Chưa quét các bộ đo **khác** xem còn tệp nào
cũng tự khai READ-ONLY mà có ghi. Việc này **còn nguyên**.

TanPhatAI cần làm: ghi **ĐÍNH CHÍNH** vế *«mất số +0,34pp»* là **SAI** (số vẫn còn, chỉ nguy cơ
là thật); ghi bản này là **BÙ**; mở theo dõi ② quét họ lỗi tự-khai-READ-ONLY (`RM-07`) và
③ lớp lỗi `>/dev/null` che stderr **tái phạm lần 3** ⇒ đã tới ngưỡng phải dựng **cổng máy**.
