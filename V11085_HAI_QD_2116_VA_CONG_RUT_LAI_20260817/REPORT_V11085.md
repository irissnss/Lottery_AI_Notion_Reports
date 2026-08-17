# REPORT V11085 — THI HÀNH 2 QUYẾT ĐỊNH OWNER 21:16 + CỔNG MÁY `PRJ-RETRACTION-001`

**Ngày:** 2026-08-17 · **Mã đọc:** `LU1708-3` · **Quyết định:** `QD-068`
**Production KHÔNG đổi** — không DB · không deploy · không Notion · `QD-041` nguyên vẹn.
**Bốn việc, bốn commit riêng, revert được độc lập.**

---

## 1. Tóm tắt

| # | việc | kết quả |
|---|---|---|
| **①** | `FU-348` hạ `MO_COI_TRAN` **15 → 2** | **XONG** — trần nay **bằng đúng** ngưỡng `FU-258` tự khai |
| **②** | K8 **lối A** — miễn trừ có thời hạn, tự hết 21/08 | **XONG** — K8 `ĐẠT 8/8`, thử chặn **6/6** |
| **③** | Cổng máy `PRJ-RETRACTION-001` | **XONG** — thử chặn **9/9**, **0 báo động giả**, đã cắm hook |
| **④** | Khai `FU-405` + `FU-406` | **XONG** — bù một lời hứa `V11084` chưa thực hiện |

**Vấp lớn nhất, và nó nằm ở việc ③:** bản đầu của cổng **báo động giả 20 chỗ** trên chính các báo
cáo viết **đúng**. Nếu đẩy nguyên như vậy thì cổng mới **đỏ ngay từ ngày dựng** — đúng thứ owner
đã cấm ở `CHECKSUMS`.

---

## 2. Owner yêu cầu gì (nguyên văn)

> **21:16 · 17/08** — *«① `FU-348`: HẠ `MO_COI_TRAN` 15 → 2 NGAY HÔM NAY. Căn cứ đo sẵn: mồ côi
> hiện đúng bằng 2 ⇒ hạ xong K8 vẫn ĐẠT, không vỡ gì.»*

> **21:16 · 17/08** — *«② K8 — LỐI A: miễn trừ CÓ THỜI HẠN cho hai mục `FU-360`/`FU-389`, gắn mã
> `QD-066`, TỰ HẾT 21/08… KHÔNG đóng lén mục nào · KHÔNG sửa `QD-066` · KHÔNG thêm nhãn vào
> `DONG_STATUSES` · Miễn trừ phải tự rơi ra sau 21/08 (không cần ai nhớ gỡ)… Mỗi lần cổng K8
> chạy phải in rõ… Thử chặn hai chiều.»*

> **17/08** — *«Luật đã tái phạm 3 lần ⇒ tới ngưỡng "phải dựng cổng, không được chỉ hứa"…
> Danh sách "đã rút" đọc từ MỘT sổ rút-lại duy nhất — CẤM hardcode trong cổng.»*

---

## 3. Đào bới / phát hiện

### 3.1 · `FU-348` — cổng rộng hơn **chính lời nó tự nói**

`FU-258` **tự viết** ngưỡng là *«tổng mồ côi ≤ 2»*, code để `MO_COI_TRAN = 15`. Chênh **gấp 7,5
lần** ⇒ K8 in `[ĐẠT]`, thoát 0, trong khi thực tế còn **5** mồ côi.

Đúng tầng theo `RM-12`: **`CỔNG_XANH_NHƯNG_NGƯỠNG_CHƯA_ĐẠT`**, **không phải** «cổng trượt».

**Vì sao tới nay mới hạ được:** lúc `FU-348` được viết, mồ côi là **5** ⇒ hạ ngay sẽ làm cổng
**đỏ thêm**, nên nó nằm lại. Đo 17/08: còn **đúng 2** ⇒ hạ về 2 là **ĐẠT ngay**.

### 3.2 · K8 — hai quyết định owner **ngược nhau, cùng ACTIVE**

```
QD-066 (12/08) → FU-360/FU-389 GIỮ nhãn, KHÔNG đóng, KHÔNG vào DONG_STATUSES
                          ↓ hệ quả BẮT BUỘC
                 hai mục VĨNH VIỄN là mồ côi
                          ↓ va thẳng vào
QD-021 (04/08) → K8 đòi 0 mồ côi đến hạn trong 2 ngày tới
```

`RM-19`. Sổ theo dõi đã viết sẵn *«đó là chủ ý, không phải lỗi»* — nhưng **không cổng nào đọc
được câu đó**. Đo được: **ĐẠT 15/08 → TRƯỢT 16/08**, và **21/08 · 22/08 vẫn TRƯỢT** ⇒ **không tự
hết**.

### 3.3 · Cổng `PRJ-RETRACTION-001` — canh **hậu quả**, không canh thủ tục

Cổng **không** canh *«có rút lại chưa»* — cái đó phải người đọc. Nó canh **hậu quả nguy hiểm
nhất**: một kết luận **đã bị bác** được trích lại **như tín hiệu dương**.

Ví dụ thật **suýt xảy ra**: nếu một báo cáo sau viết *«vì pool D-1 neo model nên cần sửa
`gpt_analyzer.py:5958`»* thì đó là đề xuất sửa **vùng `QD-041` đang khoá**, dựa trên một kết luận
**đã chết** (đo ra `−0,79pp, z = −1,01`).

---

## 4. Hướng xử lý và vì sao chọn

**Vì sao miễn trừ chỉ tha phần (b).** Owner cấm đóng mục và cấm thêm nhãn. Miễn trừ **không đóng
gì cả** — hai mục **vẫn nằm trong `toan_so`**, **vẫn bị đếm ở phần (c)** (`2/2`), **vẫn bị in
tên**. Chỉ **không kích hoạt phần (b)** cho tới ngày hết hạn.

**Vì sao hạn phải là hằng số ngày, không phải cờ bật/tắt.** Miễn trừ không có ngày hết hạn là
**cửa sau vĩnh viễn**. Ở đây hạn được so với `HOM_NAY` **mỗi lần chạy**, không lưu trạng thái ⇒
sau 21/08 nó **tự rơi**, **không cần ai nhớ gỡ**.

**Vì sao danh sách rút-lại phải nằm ngoài cổng.** Không phải chuyện gọn gàng. Cổng nào **tự giữ**
danh sách thì sửa danh sách phải sửa cổng, sửa cổng phải **thử lại** cổng ⇒ trên thực tế **không
ai thêm mục mới nữa**, và cổng chết dần đúng kiểu `RM-20`. Thêm một mục = **sửa một tệp JSON**,
không đụng một dòng mã. `T4`/`T5` chứng minh điều đó **bằng máy**.

**Vì sao hai luật `PRJ` còn lại KHÔNG dựng cổng phiên này.** `§61` đặt ngưỡng là **tái phạm hai
lần**. `SELECTION-WINDOW` có **2 ca** (đã chạm — dựng phiên tới), `PROMPT-COHERENCE` có **1 ca**
(chưa tới). **Cổng thừa cũng gây hại như cổng thiếu** — nó chiếm chỗ chú ý mà chưa có bằng chứng
cần thiết.

---

## 5. Đã làm gì

### ① `FU-348` — commit `aa7bb27`

| | |
|---|---|
| **TRƯỚC** | `_v10981_kiem_lich.py:152` `MO_COI_TRAN = 15` |
| **SAU** | `MO_COI_TRAN = 2` |
| **PHIÊN BẢN** | V11085 · 17/08/2026 |
| **KIỂM** | `tổng toàn sổ 2 (trần 15)` → `tổng toàn sổ 2 (trần 2)` — phần (c) **ĐẠT** |

Tài liệu: phân biệt **sổ sống** (sửa) với **bản ghi lịch sử** (không viết lại). Thêm khối
`FU-348` mới `CLOSED_PASS` đủ TRƯỚC/SAU/PHIÊN BẢN/KIỂM (`§60.4`); thêm banner *«OWNER ĐÃ KÝ»* vào
bản trình K8 nhưng **giữ nguyên phần trình gốc** — đó là căn cứ owner đã đọc để quyết.

### ② K8 lối A — commit `825bfd7`

```
ⓘ 2 mục được miễn theo QD-066, hết hạn 21/08: FU-360, FU-389
[ĐẠT ] K8 · … · toàn sổ mồ côi 2/2 · MIỄN TRỪ: … · còn treo phân loại: FU-360(18/08) FU-389(—)
```

**TRƯỚC** `[TRƯỢT] K8 · exit=1` → **SAU** `ĐẠT 8/8 phép · LICH_CUON_CHIEU_DAT · exit=0`.

### ③ Cổng rút-lại — commit `d120e6f`

`docs/SO_RUT_LAI.json` — **6 mục**, mỗi mục đủ bốn phần bắt buộc của `PRJ-RETRACTION-001`.
`web/backend/_v11085_cong_rut_lai.py` — ba điều kiện tha: ⓪ trong khối ``` · ① trong dấu trích
dẫn · ② vùng lân cận **6 dòng** có từ khoá rút.

Cửa sổ lân cận chứ **không phải cả tệp**: một báo cáo có thể rút `RL-002` ở đầu rồi vẫn trích lậu
`RL-004` ở cuối — soi cả tệp sẽ cho qua, đúng lỗi `RM-09`.

**Đã cắm vào `.claude/hooks/cong_git_commit.py`** ngay trong phiên dựng. Hook nay chạy **7** cổng.

### ④ Khai mã — commit `1047578`

`FU-405` (`DO2308`) · `FU-406` (`HT2508`). **Hai mã mới**, trong giới hạn ≤5/phiên.

---

## 6. Cổng kiểm

| cổng | kết quả |
|---|---|
| `_v10981_kiem_lich` K8 | **✓ ĐẠT 8/8** + in dòng miễn trừ |
| thử chặn miễn trừ (`_v11085_thu_chan_mien_tru`) | **✓ 6/6** |
| thử chặn cổng rút-lại (`--thu-chan`) | **✓ 9/9** |
| cổng rút-lại trên **8 báo cáo thật** | **✓ 0 báo động giả** |
| ghi tệp an toàn · đoán tên · mất mục · đóng băng · chéo quyết định · sáu mặt | **✓ 6/6** |
| `_v11062 --kiem` | **✗ ĐỎ ĐÚNG — `V11080b`** |

> **KHÔNG ghi «mọi cổng xanh».** `_v11062` **vẫn đỏ vì `V11080b`** — bản của **phiên khác**, agent
> này **không giữ bản ghi gốc** nên **bị cấm tự bù** theo phương án (a) owner khoá 12:57. Cổng
> đang chỉ vào một việc **thật sự đang thiếu**, và nó **chờ chữ ký owner** chứ không chờ agent.

### Thử chặn miễn trừ — 6 phép

```
T1 hôm nay 17/08          → K8 XANH + in dòng miễn trừ      exit=0
T2 biên 21/08 (hết hạn)   → VẪN miễn                        exit=0
T3 ngày 22/08             → miễn trừ TỰ RƠI, K8 ĐỎ LẠI      exit=1   ← quan trọng nhất
T4 ngày 22/08             → in rõ «ĐÃ HẾT HẠN», không im
T5 đang miễn              → VẪN đếm 2/2, VẪN in tên          (không đóng lén)
T6 DONG_STATUSES          → KHÔNG có DEPLOYED_LIVE_VERIFIED  (QD-066 cấm)
```

Không có `T3` thì đây chỉ là **một dòng tắt cổng vĩnh viễn có gắn nhãn cho đẹp**.
`T6` canh một đường khác hẳn: có thể làm K8 xanh bằng cách **lén thêm nhãn** vào `DONG_STATUSES`
— cách đó `QD-066` cấm thẳng, và nó sẽ **đóng luôn 6 mục khác** đang mang cùng nhãn.

### Thử chặn cổng rút-lại — 9 phép

```
T1 trích lậu ⇒ CHẶN                     T2 có nhãn ĐÍNH CHÍNH ⇒ CHO QUA
T3 báo cáo sạch ⇒ CHO QUA               T4 sổ RỖNG ⇒ không bắt gì   ← đọc SỔ, không hardcode
T5 thêm mục MỚI vào sổ ⇒ bắt ngay       T6 rút A ở đầu KHÔNG tha lậu B ở cuối
T7 trích nguyên văn + chữ BÁC ⇒ CHO QUA ← chống báo động giả
T8 dùng làm mệnh đề sống ⇒ VẪN CHẶN     ← ngoặc không phải lá bùa
T9 trong khối ``` ⇒ CHO QUA
```

---

## 6bis. §62 (A60) — NGUỒN BA LỚP

### `OWNER_SAID`

| giờ | nguyên văn |
|---|---|
| **21:16 17/08** | *«`FU-348`: HẠ `MO_COI_TRAN` 15 → 2 NGAY HÔM NAY»* |
| **21:16 17/08** | *«K8 — LỐI A: miễn trừ CÓ THỜI HẠN… TỰ HẾT 21/08… KHÔNG đóng lén mục nào»* |
| 17/08 | *«Danh sách "đã rút" đọc từ MỘT sổ rút-lại duy nhất — CẤM hardcode trong cổng»* |
| 12/08 (`QD-066`) | *«Tạm thời để nguyên tới 21/08 luôn em… để càng lâu càng rõ ràng chứ em»* |

### `CODE_DID`

| mã làm gì | evidence |
|---|---|
| trần hạ 15 → 2 | `_v10981_kiem_lich.py` · `tổng toàn sổ 2 (trần 2)` |
| miễn trừ tha **chỉ** phần (b) | hai mục vẫn `2/2`, vẫn in tên |
| miễn trừ **tự rơi** 22/08 | `T3`: `exit=1`, `[TRƯỢT] K8` |
| `DEPLOYED_LIVE_VERIFIED` **không** vào `DONG_STATUSES` | `T6` sạch |
| cổng đọc **sổ**, không hardcode | `T4` sổ rỗng ⇒ 0 bắt · `T5` thêm mục ⇒ bắt ngay |
| cổng chạy trong hook | hook báo **7** cổng, chỉ `_v11062` trượt |

### `DOC_SAID`

| tài liệu ghi gì | lệch? |
|---|---|
| `FU-258` *«tổng mồ côi ≤ 2»* | **ĐÃ HẾT LỆCH** — code nay đúng bằng 2 |
| `FU-348` *«K8 đang xanh giả vì trần chưa hạ»* | **ĐÃ CŨ** — đã đóng `CLOSED_PASS`, ghi TRƯỚC/SAU |
| `FOLLOW_UP_TRACKER:239` *«mồ côi… là chủ ý»* | **khớp** owner — nay **cổng đọc được** qua miễn trừ |
| `docs/K8_TRINH_OWNER_20260817.md` | **đã gắn banner** *«OWNER ĐÃ KÝ 21:16»*, giữ nguyên phần trình gốc |

### Ba lớp lệch nhau ⇒ FINDING

**`DOC_SAID` ≠ `CODE_DID` đã được xoá trong phiên này, không phải bỏ qua:** hai chỗ tài liệu mô
tả trạng thái cũ (`FU-258` ngưỡng ≤2 vs code 15; `FU-348` «xanh giả») nay **đã khớp**. Ghi rõ
thay vì để người đọc tự đoán.

---

## 7. Vướng vấp

### VẤP LỚN — cổng mới **báo động giả 20 chỗ** trên báo cáo viết ĐÚNG

Bản đầu chỉ dò **từ khoá**. Câu `### 3.3 · Giả thuyết ① «ba miền tụ» — BÁC` bị bắt vì danh sách
thiếu chữ `BÁC`. Nghịch lý: **viết đúng thì càng bị bắt** — vì viết đúng nghĩa là **trích nguyên
văn câu sai rồi bác nó ngay bên cạnh**.

Nếu đẩy nguyên như vậy: cổng mới **đỏ ngay từ ngày dựng** ⇒ người đọc quen mắt ⇒ **mất sạch giá
trị cảnh báo**. Đúng thứ owner đã cấm ở `CHECKSUMS`: *«đỏ 100% thì tệ hơn là không có»*.

**Sửa hai chỗ, và một trong hai là sửa SỔ chứ không sửa cổng:**

| chỗ | sửa gì |
|---|---|
| **cổng** | thêm phép phân loại **trích dẫn** + **khối mã**. Dấu trích dẫn là tín hiệu mạnh nhất phân biệt *nhắc tới* với *khẳng định*, và nó **không phụ thuộc** danh sách từ khoá có đủ hay không (`RM-09`) |
| **sổ** | dấu hiệu `«CÓ NEO»` **quá rộng** — hai chữ đó nằm trong **chính câu định nghĩa ngưỡng**. Dấu hiệu phải là **mệnh đề bị rút**, không phải mảnh chữ xuất hiện trong nó |

**Trước sửa: 20 báo động giả / 8 báo cáo thật. Sau sửa: 0.**

### Vấp nhỏ — `V11084` hứa `FU-405` mà chưa khai

Báo cáo `V11084` viết *«mở `FU-405`»* nhưng phiên đó **chưa khai vào sổ** — `_v11044` vẫn báo
`FU-405` còn trống. Tức báo cáo hứa một mục theo dõi **không tồn tại**. Bù ở việc ④.

---

## 8. Gỡ về

```bash
git revert 1047578   # ④ khai FU-405 + FU-406
git revert d120e6f   # ③ cổng PRJ-RETRACTION (gỡ luôn khỏi hook)
git revert 825bfd7   # ② K8 lối A — miễn trừ
git revert aa7bb27   # ① hạ MO_COI_TRAN
```

Bốn commit **độc lập**. Gỡ ② mà giữ ① thì K8 đỏ lại vì phần (b) — đúng trạng thái trước phiên.

---

## 9. Theo dõi tiếp

### Chờ owner

| việc | ghi chú |
|---|---|
| **`V11080b`** chưa có dòng `HISTORY` | của **phiên khác**; agent bị cấm tự bù ⇒ `_v11062` **đỏ đúng** tới khi có hướng |
| hook `SessionStart` · **48 bản vá** cũ | vẫn treo từ V11083 |

### Lịch tự động

| mốc | chuyện gì xảy ra |
|---|---|
| **22/08** | miễn trừ `QD-066` **tự hết**. `FU-360`/`FU-389` quay lại tính mồ côi ⇒ **K8 đỏ lại là CỐ Ý** — lời nhắc xử hai mục trong gói 21/08, **không phải lỗi mới** |

### Mã mới

| mã | việc | hạn |
|---|---|---|
| **`FU-405`** `DO2308` | MN chốt sớm hơn hạn 10h25m — **chưa rõ mất gì**. Giả thuyết «lỡ bộ học» **đã bị bác** (`RL-006`) | 23/08 |
| **`FU-406`** `HT2508` | cổng cho 2 luật `PRJ` còn lại — `DEFER`: `SELECTION-WINDOW` **2 ca** (dựng phiên tới) · `PROMPT-COHERENCE` **1 ca** (chưa tới ngưỡng `§61`) | 25/08 |

**Verdict tách hai dòng:**
- **`CODE_PUSHED`** = `aa7bb27` · `825bfd7` · `d120e6f` · `1047578`
- **`REPORT_PUBLISHED`** = bản này

---

TanPhatAI cần làm: ① ghi **`FU-348` ĐÓNG `CLOSED_PASS`** — `MO_COI_TRAN` **15 → 2**, trần nay
bằng đúng ngưỡng `FU-258` tự khai; ② ghi **K8 lối A** — miễn trừ `FU-360`/`FU-389` gắn `QD-066`,
**TỰ HẾT 21/08**, hai mục **vẫn đếm 2/2 và vẫn in tên** (không đóng lén), thử chặn **6/6** với
`T3` chứng minh tự rơi; ③ ghi **cổng `PRJ-RETRACTION-001` đã dựng và đã cắm vào hook** — nguồn là
**`docs/SO_RUT_LAI.json`**, thêm mục rút lại **chỉ sửa JSON, cấm sửa cổng**; ④ ghi **vấp 20 báo
động giả đã sửa** (nay 0) — bài học: cổng đỏ trên việc đúng thì mất sạch giá trị; ⑤ mở
**`FU-405`** (MN chốt sớm 10h25m, giả thuyết «lỡ bộ học» **đã bị bác**) và **`FU-406`** (cổng 2
luật PRJ còn lại, `DEFER` có lý do); ⑥ **đánh dấu lịch 22/08** — miễn trừ tự hết, **K8 đỏ lại là
CỐ Ý**, không phải lỗi mới; ⑦ ghi **`_v11062` vẫn ĐỎ ĐÚNG vì `V11080b`** — chờ owner,
**cấm ghi «mọi cổng xanh»**.
