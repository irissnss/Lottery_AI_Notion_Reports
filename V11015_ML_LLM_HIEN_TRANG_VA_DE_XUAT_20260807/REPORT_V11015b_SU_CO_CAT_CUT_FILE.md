# REPORT V11015b — SỰ CỐ CẮT CỤT FILE: mất 23.551 dòng, đã gỡ về, đã dựng cổng

> **Ngày:** 2026-08-07 · **Mức:** nghiêm trọng, tự phát hiện · **Trạng thái:** ĐÃ GỠ VỀ ĐẦY ĐỦ
> **Runtime:** KHÔNG ảnh hưởng — VPS đã kiểm đọc-không-ghi

---

## 1. Tóm tắt

Ngay sau khi đẩy commit V11015, agent đọc dòng thống kê của **chính commit mình vừa push**:

```
4 files changed, 156 insertions(+), 23551 deletions(-)
```

Thêm 156 dòng mà **xoá 23.551**. Đào ra: **ba tệp bị cắt cụt âm thầm**, hai trong số đó **đã lên
GitHub**. Đã gỡ về đầy đủ, dựng cổng chặn, và kiểm VPS không dính.

**Không phải owner báo.** Nhưng cũng không có cổng nào báo — đó mới là chỗ phải sửa.

## 2. Owner yêu cầu gì (nguyên văn)

Owner **không** yêu cầu việc này. Sự cố sinh ra trong lúc thực hiện lệnh:

> *"cập nhật báo cáo github và nâng verison V10 cho aritifact đi em"*

Ghi lại theo §60.4 — việc đã làm phải có trước/sau/phiên bản/kiểm — và theo A55: mọi việc fix
phải có báo cáo công khai.

## 3. Đào bới / phát hiện

### 3.1 Mất gì

| tệp | trong git | trên đĩa | mất | đã commit chưa |
|---|---|---|---|---|
| `CHANGELOG.md` | 28.194 dòng | 6.664 | **21.583 dòng · 1,63 triệu ký tự** | **RỒI** — `54f3299`, đã push |
| `docs/CURRENT_TRUTH_SSOT.md` | 6.415 dòng | 4.480 | **1.968 dòng · 543 nghìn ký tự** | **RỒI** — `54f3299`, đã push |
| `web/backend/main.py` | 21.128 dòng | 6.043 | **15.085 dòng · 679 nghìn ký tự** | **CHƯA** — chỉ bản làm việc |

### 3.2 Vân tay — cả ba cắt tại ĐÚNG biên luỹ thừa 2

| tệp | cỡ sau khi cắt | = |
|---|---|---|
| `main.py` | 262.144 byte | **256 KiB chẵn** |
| `CHANGELOG.md` | 524.288 byte (đo trước khi ghép khối V11015) | **512 KiB chẵn** |
| `CURRENT_TRUTH_SSOT.md` | 524.288 byte (đo trước khi ghép khối V11015) | **512 KiB chẵn** |

Ba tệp khác nhau về loại, kích cỡ và thời điểm động vào, mà **đều dừng tại một biên đệm chẵn** —
không trùng hợp được. Một đường ghi file có **trần đệm** đã ghi cụt và **không báo lỗi**.

Phần còn lại là **TIỀN TỐ nguyên vẹn** của bản cũ, cắt **giữa chừng một dòng**:

```
… start_date = body.get('start_date')
   end_date = body.get('end_date')
   top_n = int(body.get('top_n', 5))
   ⟵ CẮT Ở ĐÂY (262.144 byte chẵn)
```

Vì thế `git diff` trông như *"xoá 21.583 dòng cuối"* — trong một commit nhiều tệp thì rất dễ lướt.

### 3.3 Vì sao BA cổng đang có đều không bắt được

| cổng | vì sao mù |
|---|---|
| `_doc_prepend.prepend()` | chỉ so bản mới với bản **TRÊN ĐĨA**. Đĩa đã cụt sẵn ⇒ ghép khối mới vào vẫn "dài hơn bản cũ" ⇒ **cho qua**. Nó không hề biết bản trong git dài gấp bốn |
| băm 4 bảng khoá | chỉ chứng minh **không ghi bậy vào DB** — không nói gì về tệp tài liệu hay mã nguồn |
| cổng báo cáo A55 | kiểm **đủ 9 tiêu đề**, không kiểm **độ dài** |

Cả ba đều đúng việc của mình. Chỗ trống là: **không cổng nào so bản làm việc với bản trong git.**

## 4. Hướng xử lý và vì sao chọn

**Gỡ về bằng `HEAD~1`, không bằng bản sao lưu tay** — vì đã chứng minh được bằng máy rằng phần
còn lại trên đĩa là **tiền tố nguyên vẹn** của `HEAD~1`, tức bản làm việc **không có gì mới để
mất**. Điều kiện kiểm trước khi ghi: `old.startswith(phần_còn_lại)`, sai là dừng ngay.

**KHÔNG viết lại lịch sử git.** `54f3299` đã push lên kho chung ⇒ sửa bằng **commit khôi phục
tiếp theo**. Ép ghi đè lịch sử nguy hiểm hơn cái sai nó vá.

**Cổng mới soi đúng chỗ ba cổng cũ mù** — so với **git HEAD**, không so với đĩa.

## 5. Đã làm gì

### 5.1 Gỡ về · `VERIFIED_TEST`

| tệp | TRƯỚC | SAU | kiểm |
|---|---|---|---|
| `CHANGELOG.md` | 6.664 dòng | **28.247 dòng** | phần cũ khớp `HEAD~1` từng ký tự |
| `docs/CURRENT_TRUTH_SSOT.md` | 4.480 dòng | **6.448 dòng** | như trên |
| `web/backend/main.py` | 6.043 dòng | **21.128 dòng** | `git checkout --` + `ast.parse` OK |

### 5.2 Cổng mới `web/backend/_v11015_cong_chan_cat_cut.py`

Chặn khi tệp ngắn đi **>5% và >50 dòng** **và** có ít nhất một trong hai dấu hiệu mạnh:

- phần còn lại là **tiền tố nguyên vẹn** của bản trong git (cắt cụt, không phải sửa nội dung)
- cỡ tệp rơi đúng **biên luỹ thừa 2** (64 KiB … 2 MiB)

### 5.3 Hook `.cursor/hooks/truncation_guard.py`

Matcher `git commit|git push` · `failClosed: true` · timeout 60s. Chặn thì trả `permission: deny`
kèm nguyên văn chi tiết và câu lệnh gỡ về.

## 6. Cổng kiểm

| phép | kết quả |
|---|---|
| Cổng chạy trên bản **lành** | mã thoát **0** — *"Không tệp nào ngắn đi bất thường"* |
| Cổng chạy trên bản **đã cắt** (thử ngược) | mã thoát **1** — bắt đúng `main.py 21.128 → 6.043 dòng (mất 15.085 · 72,3%)`, in đúng *"cắt tại ĐÚNG 256 KiB chẵn"* |
| `hooks.json` | JSON hợp lệ, hook trả `{"permission": "allow"}` trên bản lành |
| `main.py` biên dịch | `ast.parse` OK |
| **VPS `main.py`** | **21.128 dòng — KHỚP local** |
| **VPS `py_compile`** | **OK** |
| **VPS PID `lottery`** | **974549** (không restart) |
| **VPS `/api/health`** | **200** |
| J5 mốc tải | khớp sổ thật |

**Bản đã cắt CHƯA BAO GIỜ được deploy** — phiên này READ-ONLY, không có lượt deploy nào.

## 7. Vướng vấp

**Agent đẩy một commit xoá 23.551 dòng mà không đọc dòng thống kê trước khi push.** Con số nằm
ngay trong đầu ra của `git commit`, đọc là thấy — agent đọc **sau khi** đã push.

**Và cái sai gốc còn sâu hơn:** `_doc_prepend` được viết ra chính để chống ghi đè mất lịch sử, có
cả `DocShrinkError`. Nhưng nó so với **đĩa**. Khi đĩa đã hỏng thì nó **hợp thức hoá** cái hỏng —
một cổng an toàn quay ra bảo chứng cho dữ liệu đã mất. Đúng lỗi **§60.2 câu 1**: *"ai còn trỏ tới
thứ này?"* — ở đây là *"cổng này thật ra đang so với cái gì?"*

## 8. Gỡ về

Đã gỡ về xong (mục 5.1). Nếu cần lùi tiếp:

```bash
git checkout 9510886 -- CHANGELOG.md docs/CURRENT_TRUTH_SSOT.md   # bản đầy đủ trước sự cố
git checkout -- web/backend/main.py
```

Muốn tắt cổng mới: xoá khối `truncation_guard.py` khỏi `beforeShellExecution` trong
`.cursor/hooks.json`. Cổng chỉ **đọc**, không sửa tệp nào.

## 9. Theo dõi tiếp

| Mã | Nội dung | Trạng thái | Hạn |
|---|---|---|---|
| **FU-323** | Sự cố cắt cụt + cổng chặn | **`CLOSED_PASS`** — gỡ về xong, cổng thử hai chiều đạt | 07/08 |
| **FU-324** | **Rà nguồn** — cổng bắt được *hậu quả*, chưa bịt được *nguồn*. Chưa biết đường ghi nào có trần đệm 256/512 KiB | `MEASURED_ROOT_CAUSE` | 14/08 |

**Ngưỡng hành động FU-324:** mọi đường ghi tệp >64 KiB trong kho phải ghi ra `.tmp` → `flush` →
`os.replace` → **đọc lại so độ dài**. Chỗ nào thiếu thì sửa, hoặc ghi rõ vì sao được miễn.

**Bài học nên nhớ:** một cổng an toàn so với **nguồn đã hỏng** thì không phải cổng — nó là con
dấu đóng lên cái sai. `_doc_prepend` so với đĩa; đĩa hỏng thì nó ký cho cái hỏng.
