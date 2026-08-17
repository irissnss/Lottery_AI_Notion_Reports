# REPORT V11079 — BỘ ĐO `_v11057` TỰ KHAI **READ-ONLY** NHƯNG **GHI ĐÈ** CHÍNH CHỨNG CŨ CỦA NÓ

> ### ⚠ BÁO CÁO BÙ — hai ngày khác nhau, đừng đọc nhầm
>
> | | |
> |---|---|
> | **việc xảy ra** | **16/08/2026 19:21** — commit `4a7ee6d` |
> | **báo cáo này viết** | **17/08/2026** (`V11083` / `GĐ-5`) |
>
> **Nguồn viết bù:** bản ghi của **chính phiên gốc** — phiên viết bản này là phiên đã làm bản vá.
> Owner khoá **phương án (a)** lúc 12:57 ngày 17/08: *«CHỈ phiên gốc viết bù từ bản ghi của chính
> nó (RM-17)… CẤM tự chuyển sang soạn từ commit message hay nguồn khác»*.

---

## 1. Tóm tắt

`_v11057_do_thuoc_chinh.py` **tự khai READ-ONLY ở dòng 51** nhưng **ghi đè** ở **dòng 203** —
và tệp bị đè chính là artifact đang giữ con số **`+0,34pp`** mà `QD-057` viện dẫn.

**Đính chính ngay trong phần này:** phát hiện gốc chỉ **đúng một nửa**. Vế *«đã ghi đè MẤT số
+0,34pp»* là **SAI** — `git status` sạch, nội dung vẫn `n=492 · +0,34pp`, **không mất gì**. Nhưng
**nguy cơ là thật**: lần chạy sau sẽ đè lên bản trước và **không ai biết bản nào đã mất**.

---

## 2. Owner yêu cầu gì (nguyên văn)

> *«Em phải biết rõ là cái nào nên làm trước và làm sau, cái nào đạp cái nào, cái nào chưa rõ phải
> đi tìm hiểu thêm, em phải sắp xếp đúng tuần tự lần lượt từ đơn giản đến phức tạp chứ em»*

Đây là mục **DỄ nhất và RÕ nhất** trong 47 phát hiện, và thuộc đúng loại **«cái này đạp cái kia»**
— nên nó được làm **trước**.

---

## 3. Đào bới / phát hiện

```
_v11057_do_thuoc_chinh.py:51    docstring khai «READ-ONLY, không ghi gì»
_v11057_do_thuoc_chinh.py:203   .write_text(...) GHI ĐÈ artifacts/v11057/thuoc_do_chinh.json
```

| vế của phát hiện gốc | phán quyết |
|---|---|
| *«tự khai READ-ONLY nhưng có ghi»* | **ĐÚNG** — dòng 51 vs dòng 203 |
| *«đã ghi đè MẤT số +0,34pp»* | **SAI** — `git status` sạch, nội dung vẫn `n=492 · +0,34pp` |

Vì sao đáng xử ngay dù chưa mất gì: bộ đo **tự khai sai bản chất của mình** thì người sau đọc
docstring sẽ tin là chạy bao nhiêu lần cũng an toàn — rồi mất bản đối chiếu mà **không có triệu
chứng nào**.

---

## 4. Hướng xử lý và vì sao chọn

Không đổi hành vi đo, chỉ đổi **cách ghi**: bản **MỐC** giữ nguyên, lần chạy sau ghi thêm bản
**có dấu thời gian**.

```python
_moc = _tm / "thuoc_do_chinh.json"
_ten = (f"thuoc_do_chinh_{dt.datetime.now():%Y%m%d_%H%M%S}.json"
        if _moc.exists() else "thuoc_do_chinh.json")
```

**Không chạm `QD-041`** — đây là **bộ đo**, không phải prompt / chọn số / roster.

---

## 5. Đã làm gì

| # | việc | vì sao |
|---|---|---|
| 1 | bản mốc giữ nguyên; lần sau ghi bản có dấu thời gian | giữ được đối chiếu |
| 2 | sửa docstring — khai **ĐÚNG** là **CÓ** ghi artifact | tự khai sai là gốc bệnh |
| 3 | sửa dòng log cuối — in **đúng tên tệp vừa ghi** | dòng cũ in cứng tên mốc ⇒ **báo sai** |

**TRƯỚC:** `— READ-ONLY, không ghi gì.`
**SAU:** `— chỉ ĐỌC DB, nhưng CÓ ghi một artifact kết quả vào artifacts/v11057/. Từ V11079:
không đè bản mốc — lần chạy sau ghi thêm tệp có dấu thời gian.`

---

## 6. Cổng kiểm

Chạy lại **2 lần**:

| phép | kết quả |
|---|---|
| bản mốc có bị động không | **KHÔNG** — `git status` sạch |
| mỗi lần chạy có sinh bản dấu thời gian không | **CÓ** |
| log cuối in đúng tên tệp vừa ghi | **ĐÚNG** |

---

## 6bis. §62 (A60) — NGUỒN BA LỚP

**`OWNER_SAID`** · 16/08: *«cái nào đạp cái nào, cái nào chưa rõ phải đi tìm hiểu thêm… từ đơn
giản đến phức tạp»* · 17/08 12:57: *«CHỈ phiên gốc viết bù từ bản ghi của chính nó (RM-17)»*

**`CODE_DID`** · `_v11057:51` khai READ-ONLY · `_v11057:203` `.write_text()` ghi đè ·
sau vá: bản mốc bất động qua **2** lần chạy · commit `4a7ee6d`

**`DOC_SAID`** · docstring cũ *«READ-ONLY, không ghi gì»* — **LỆCH thẳng với `CODE_DID`**, và đó
chính là khuyết tật. Đã sửa docstring trong cùng phiên.

**Lệch thứ hai, phải báo:** bản đào ghi *«đã ghi đè mất số +0,34pp»* — **sai**. Số vẫn còn.
Ghi lại đúng, **không im lặng sửa**.

---

## 7. Vướng vấp — **hai vấp của chính agent**, cả hai đều ghi lại

**Vấp 1 — `>/dev/null` che mất lỗi.** Chạy thử với `>/dev/null` nên **không thấy** bản vá ném
`NameError: name 'datetime' is not defined` — tệp dùng `import datetime as dt`, bản vá lại gọi
`datetime.now()`.

Đây **đúng lớp lỗi mà agent ĐÃ TỰ GHI hai lần trước đó**: *«chặn stderr biến lỗi ồn ào thành số 0
im lặng»*. Ghi ra rồi vẫn tái phạm ⇒ theo `§61`, nhắc suông đã thất bại.
**Bắt được vì chạy lại CÓ NHÌN OUTPUT**, không phải vì tin dòng «✓ đã sửa».

**Vấp 2 — vá xong log vẫn in tên tệp cũ** ⇒ báo sai. Đúng loại lỗi đang đi bắt.

---

## 8. Gỡ về

```bash
git revert 4a7ee6d
```

Không kéo theo gì — thay đổi khu trú trong một tệp bộ đo.

---

## 9. Theo dõi tiếp

| việc | trạng thái |
|---|---|
| `_v11057` không còn đè bản mốc | **XONG** |
| quét các bộ đo **khác** cũng tự khai READ-ONLY mà có ghi | **CHƯA** — `RM-07`: vá một lỗi không phải vá cả họ lỗi |
| lớp lỗi `>/dev/null` che stderr | tái phạm lần **3** — cần **cổng máy**, không nhắc suông |

**Verdict:** `CODE_PUSHED` = `4a7ee6d` (16/08) · `REPORT_PUBLISHED` = bản này (**bù 17/08**)

---

TanPhatAI cần làm: ghi **ĐÍNH CHÍNH** — vế *«đã ghi đè mất số +0,34pp»* là **SAI**, số vẫn còn
(`n=492 · +0,34pp`), chỉ **nguy cơ** là thật; ghi bản này là **BÙ** (việc 16/08, viết 17/08,
phương án (a)); và mở theo dõi **hai việc còn lại**: ① quét các bộ đo khác cùng loại tự-khai-sai
(`RM-07`), ② lớp lỗi `>/dev/null` che stderr đã **tái phạm lần 3** ⇒ đến ngưỡng phải dựng **cổng
máy**.
