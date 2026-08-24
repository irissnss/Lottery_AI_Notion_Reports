# REPORT V11111 · V11112 · V11113 — FINAL BẤT BIẾN: `P0-A` → `P0-E`

**Ngày:** 24/08/2026 (trưa) · **Kho riêng:** `daf8cd8` → `0f4e162` → `2fca495`
**Trạng thái:** `REPORT_PROVEN` + `CODE_PUSHED` — **KHÔNG deploy**, **KHÔNG chạm production**

> ⚠️ **`RM-12`:** phiên này **không** có gì đạt `RUNTIME_PROVEN`. Toàn bộ là **đọc + đo + dựng
> cổng thử**. Không một dòng mã production nào bị sửa, không một lần restart nào.

---

## 1 · TÓM TẮT

Owner giao `P0-A` → `P0-E` của prompt 34: chứng minh FINAL có bất biến không, truy đủ
writer/reader, tách CANDIDATE/FINAL/RESULT, truy `300s` thật sự làm gì, và dựng fallback OFFICIAL.

**Kết quả lớn nhất: phần lớn kiến trúc owner yêu cầu ĐÃ TỒN TẠI** — em đã báo sai là *«chưa có»*.

| owner yêu cầu | thực tế |
|---|---|
| bước finalize một lần trước mốc khoá | 🟢 **có** — job **T-chốt** `MN 15:40 · MT 16:55 · MB 17:55` |
| FINAL khoá sau mốc | 🟢 **có** — **hai** cổng, nay **chứng minh được là chặn thật** (17/17) |
| chấm kết quả không được đổi số | 🟢 **có** — writer settlement ghi **đúng 7 cột**, **0 cột mang dự đoán** |
| model quá hạn vẫn chạy, output muộn vẫn lưu, không sửa FINAL | 🟢 **có** — late-fill, **68 dòng log** 06/07→23/08 |
| cutoff riêng từng model | 🟢 **có** — bảng trần riêng |
| fallback OFFICIAL | 🟢 **có** — hai lớp, lớp 2 **fail-CLOSED** |
| roster đóng băng theo ngày | 🔴 **chưa có** |
| trục «đủ tư cách vào FINAL» tách khỏi hard timeout | 🔴 **chưa có** |

**Ba câu em đã công bố mà sai, đã rút lại đủ bốn phần.**

---

## 2 · OWNER YÊU CẦU GÌ (NGUYÊN VĂN)

> *«`P0-A` ảnh chụp + diff `v1/v2` **trước MN 15:45**.»*

> *«`P0-D`: **CẤM đổi mù 300 thành 500**. Phải truy `AI_MODEL_HARD_TIMEOUT_SEC=300` hiện đang:
> hủy request/future; chỉ hết thời gian chờ; hay model vẫn chạy ngầm.»*

> *«Provider/runtime hard timeout là trục khác. **Không được dùng eligibility cutoff để hủy
> model**.»*

> *«Cấm thay thuật toán mù.» · «Cấm tự quyết.» · «Cấm gọi `CODE_PUSHED` hoặc `DEPLOYED` là
> `RUNTIME_PROVEN` trước lượt live thật.» · «Agent phân tích mặc định chỉ được READ-ONLY.»*

---

## 3 · ĐÀO BỚI / PHÁT HIỆN

### 3.1 · `P0-B` — **đúng HAI câu lệnh ghi** `final_bundles` trong toàn kho sống

| | câu lệnh | hàm | người gọi |
|---|---|---|---|
| **W1** | `INSERT` `database.py:4648` | `save_final_bundle:4581` | **2** — `main.py:10391` (production) · `_backfill_bundles.py:177` |
| **W2** | `UPDATE` `database.py:4933` | `verify_final_bundle:4812` | **10** — `main.py` ×7 · `scheduler.py:1264` · backfill · `force_rescrape` |

**Hai chỗ trông như writer mà KHÔNG phải** — phân loại, không đếm thô (`RM-09`):
`_v10889_no_copy.py:51` chạy `DELETE` trên **bản sao trong bộ nhớ** (phép thử «bịt mắt») ·
`_v10821_probe3.py:72` là **chuỗi grep** trong script dò.

### 3.2 · 🟢 Writer chấm kết quả **KHÔNG THỂ** đổi số dự đoán

`verify_final_bundle` ghi **đúng 7 cột**: năm cột `*_status` + `verified_at` + `updated_at`.
**Không một cột mang dự đoán nào.** Và nó **không chạm `bundle_version`**.

### 3.3 · 🟢 `RM-15` — hai cổng bất biến **chứng minh được là chặn thật**

Đo ban đầu: **0 sự kiện chặn** trong journald (giữ 6 ngày) lẫn bảng log. Sáu ngày đó chắc chắn có
bundle ghi lần hai ⇒ **không phân biệt được** «cổng cho qua đúng» với «cổng chưa từng chạy» —
đúng khuôn cổng đóng băng `QD-041` từng **mù hoàn toàn** mà **luôn báo xanh**.

⚠️ **Suýt kết luận bằng nguồn sai (`RM-13`):** hai cổng dùng `print()`, **không** ghi vào bảng log
— đo bảng log ra `0` **không chứng minh gì**. Phải đo journald.

Dựng `_v11112_thu_chan_bat_bien.py` — **17/17**, hai chiều, chạy trên **DB tạm** dựng từ đúng lược
đồ production, **không chạm DB thật** (kiểm dấu thời gian + kích thước trước/sau).

**Hai cổng in ra thông điệp chặn thật.** Biên đúng cả sáu điểm:
`MN 15:44 chưa khoá / 15:45 đã khoá` · `MT 16:57/16:58` · `MB 17:57/17:58`.
Ngày quá khứ **luôn** khoá. `T_CHOT_MARKS` đều **trước** `FREEZE_MARKS`.

⇒ **`0` trong log KHÔNG phải cổng mù — cổng tốt, chỉ là chưa lần nào phải nổ.**

**Ghi nhận cửa hậu:** `force=True` đi xuyên **cả hai** cổng. Quét toàn kho: **0 nơi truyền**.

### 3.4 · 🔴 Lỗ hổng quan sát — **không biết được lần ghi thứ hai xảy ra lúc nào**

`updated_at` **bằng đúng** `verified_at` ở **mọi** dòng `v=2`, cả ba miền, năm ngày gần nhất
⇒ lần ghi **cuối** là settlement. Mà settlement **không chạm `bundle_version`** ⇒ lần bump `v`
xảy ra **trước đó** và **dấu thời gian của nó đã bị ghi đè mất**. `created_at` **không nằm trong**
nhánh ghi-đè nên nó giữ giờ tạo **đầu tiên**.

Phân bố `bundle_version` toàn lịch sử: **MN** `127/49/2` · **MT** `90/87` · **MB** `89/88`.
`v>=2` tổng **226** dòng, trong đó `verified_at` rỗng: **0**.

⇒ **không cột nào ghi lại giờ của lần ghi thứ hai.** Đây chính là lỗ `P0-A` sinh ra để bịt.

### 3.5 · `P0-D` — `300s` thật sự làm gì

| câu owner hỏi | trả lời | bằng chứng |
|---|---|---|
| huỷ request/future? | **KHÔNG — model vẫn chạy ngầm** | `future.cancel()` chỉ có tác dụng khi tác vụ **chưa chạy**; **mã BIẾT điều này** — hàm đăng ký ghi thẳng *«future vẫn chạy nền, sẽ poll lại theo watchdog»* |
| late output có lưu? | **CÓ, đang chạy thật** | **68 dòng log** 06/07→23/08: một model về ở **869s · 1053s · 979s**, ghi lane đo `late=1`, **không vào bundle** |
| cutoff riêng từng model? | **CÓ** | `glm-5.1` **840s** · `gpt-oss-120b` **900s** · `kimi-k2.5` **620s** · `qwen3.7-max` **480s** · mặc định **300s** |

**Timeout thật 60 ngày:** chỉ `300s` nổ — 50 lần không gán được model + **2 lần** một model
không có trong bảng trần riêng.

🔴 **Khoảng trống thật:** đường `combo-super` **không truyền cutoff riêng** ⇒ luôn `300s`, trong
khi official và shadow đều truyền. **3 sự kiện** timeout `>300s` toàn lịch sử, cả ba vào **giờ
lẻ** không trùng cửa sổ dự đoán chính thức ⇒ **có thể** là lượt chạy tay, **chưa xác minh**.
Thật, nhưng **không khẩn**.

### 3.6 · `P0-E` — fallback đã có; roster thiếu **chiều ngày**

Fallback OFFICIAL **hai lớp**: registry động → **danh sách cứng 15 model** (**fail-CLOSED**).

🟡 **Cùng một khuôn `try/except ImportError`, HAI hành vi NGƯỢC NHAU:** ở fallback roster là
**fail-CLOSED** (vẫn lọc); ở cổng khoá thời gian `database.py:4646` là **fail-OPEN** (bỏ cổng
luôn). **Chỗ fail-open mới là chỗ phải bịt.**

🔴 Hàm lấy roster **không có tham số ngày** — lọc theo trạng thái + miền, **bỏ qua hoàn toàn**
`first_run_date`/`retired_date` ⇒ **roster HÔM NAY bị áp cho MỌI ngày lịch sử**.

🔴 **Dữ liệu để vá CHƯA CÓ:** cả **15/15** model output đều `first_run_date` **rỗng**. Trường tồn
tại trong lược đồ nhưng rỗng ở **đúng** những model cần nó ⇒ phải **bù bằng đo, không được bịa**
(`RM-17`).

---

## 4 · HƯỚNG XỬ LÝ VÀ VÌ SAO CHỌN

**Chọn: đo và dựng cổng thử, KHÔNG sửa gì.** Vì:

1. Owner khoá *«Cấm thay thuật toán mù»* + *«Cấm tự quyết»*. Bốn trong bảy việc còn treo đều
   **đổi hành vi cổng hoặc lược đồ** ⇒ phải trình, không được tự làm.
2. `P0-D` hoá ra **không cần sửa gì** — cơ chế owner mô tả đã chạy. Đổi `300`→`500` sẽ là **sửa
   nhầm trục**, đúng thứ owner cấm.
3. `RM-15` bắt buộc: cổng chưa qua thử **coi như không tồn tại**. Nên việc đầu tiên đáng làm là
   **chứng minh hai cổng có chặn**, chứ không phải thêm cổng thứ ba.

---

## 5 · ĐÃ LÀM GÌ

| # | việc | trạng thái |
|---|---|---|
| 1 | `_v11111_snapshot_final.py` — chụp FINAL, phân loại cột **ba nhóm**, cột lạ ⇒ nhóm mang-dự-đoán (fail-closed) | 🟢 thử chặn **9/9** |
| 2 | **Ảnh chụp #1** `24/08 12:15:04` — MN `v=1` `BT='45'`, có băm SHA-256 | 🟢 đã lưu vào kho |
| 3 | `_v11112_thu_chan_bat_bien.py` — thử chặn hai cổng bất biến | 🟢 **17/17** |
| 4 | `docs/FINAL_OUTPUT_CONTRACT_20260824.md` — bản đồ AS-IS đầy đủ `P0-A/B/C/D/E` | 🟢 |
| 5 | Rút lại **ba câu sai**, đủ bốn phần, **đúng chỗ đã công bố** | 🟢 |
| 6 | Bốn mặt version cho `V11111` · `V11112` · `V11113` | 🟢 cổng `§63` **ĐẠT** |

**Ảnh chụp #2** đặt lịch `15:50` — **sau** T-chốt `15:40`, **sau** freeze `15:45`, **TRƯỚC**
settlement `~16:36`. Cửa sổ này **cô lập đúng** lần ghi T-chốt, không lẫn settlement.

---

## 6 · CỔNG KIỂM

| cổng | kết quả |
|---|---|
| `_v11111` thử chặn | 🟢 **9/9** |
| `_v11112` thử chặn bất biến | 🟢 **17/17** |
| `§63` bốn mặt version | 🟢 **ĐẠT** — `THIẾU HISTORY: 0` |
| DB production nguyên vẹn | 🟢 **từng byte**, kiểm trước/sau |
| cổng an toàn báo cáo công khai | 🟢 chạy trước khi đẩy |

---

## 7 · VƯỚNG VẤP

**7.1 · Cổng `§63` chặn commit của chính em — và nó ĐÚNG.** Em gán nhãn `V11111` ở commit đầu mà
**quên ghi `HISTORY`** ⇒ `A61_VIOLATION_PARTIAL_BUMP`. **Không đi vòng** — sửa nguyên nhân bằng
`ghi()` đủ bốn mặt rồi commit lại.

**7.2 · Suýt kết luận bằng nguồn sai (`RM-13`)** — đo `FREEZE-GUARD` trong bảng log ra `0` và suýt
kết luận cổng mù. Hai cổng dùng `print()` ⇒ ra journald, **không** vào bảng. Đổi nguồn rồi mới đo.

**7.3 · Đoán tên bảng (`RM-10`)** — thử bốn tên bảng roster, **cả bốn không tồn tại**. Phải quét
mã tìm đường thật.

**7.4 · Suýt nói *«dữ liệu để vá đã có sẵn»*** — trường ngày **có trong lược đồ**, nhưng đo lại thì
**cả 15/15 model output đều rỗng**. Sửa ngay trong cùng lượt, trước khi câu đó kịp đứng.

---

## 8 · GỠ VỀ

**Không có gì để gỡ** — phiên này **không sửa mã production, không deploy, không restart**.
Ba tệp mới đều là **công cụ đo/thử độc lập**; xoá đi là xong, không ảnh hưởng runtime.

---

## 9 · THEO DÕI TIẾP

| # | việc | chặn ở đâu |
|---|---|---|
| 1 | **diff ảnh chụp #1 ↔ #2** | chờ `~15:50` hôm nay |
| 2 | đo `combo-super` — 3 timeout có phải lượt chạy tay không | chưa đo |
| 3 | bịt `except ImportError: pass` làm cổng khoá thời gian **fail-OPEN** | **cần owner ký** |
| 4 | cột trạng thái tường minh + dấu thời gian lần ghi thứ hai | **cần owner ký** — đổi lược đồ |
| 5 | trục `OUTPUT_ELIGIBILITY_CUTOFF_SEC` tách khỏi hard timeout | **cần owner ký** |
| 6 | roster theo ngày + bù `first_run_date` bằng đo | **cần owner ký** |
| 7 | truyền cutoff riêng cho đường `combo-super` | **cần owner ký** |

---

## 10 · BA LỚP NGUỒN (§62 · A60)

### `OWNER_SAID`

> *«**CẤM đổi mù 300 thành 500**. Phải truy `AI_MODEL_HARD_TIMEOUT_SEC=300` hiện đang: hủy
> request/future; chỉ hết thời gian chờ; hay model vẫn chạy ngầm.»* — prompt 34, mục VI

> *«Provider/runtime hard timeout là trục khác. **Không được dùng eligibility cutoff để hủy
> model**.»* — prompt 34, mục VI

> *«`P0-A` ảnh chụp + diff `v1/v2` **trước MN 15:45**.»* — prompt 34

### `CODE_DID`

| điều mã **thực sự** làm | bằng chứng |
|---|---|
| hard timeout **không giết** model | `scheduler.py:319-329`; hàm đăng ký late-fill ghi *«future vẫn chạy nền»* |
| late output **được lưu**, **không vào bundle** | **68 dòng log** 06/07→23/08 |
| settlement ghi **đúng 7 cột**, **0 cột mang dự đoán** | `database.py:4932-4943` |
| hai cổng bất biến **chặn thật** | `_v11112` **17/17**, thông điệp chặn in ra |
| roster **không có** chiều ngày | chữ ký hàm lấy roster: không có tham số `date` |
| `first_run_date` **rỗng ở cả 15** model output | đo trên nguồn đang chạy |

### `DOC_SAID`

| tài liệu | nói gì | có khớp mã không |
|---|---|---|
| `docs/CURRENT_TRUTH_MATRIX_20260824.md` §6 | *«không có bước finalize»* · *«state machine chưa tồn tại»* | 🔴 **KHÔNG** — đã rút lại tại chỗ |
| `docs/FOLLOW_UP_TRACKER.md` `FU-436` | *«`glm-5.1` bị trần 300s»* | 🔴 **KHÔNG** — đã rút lại đủ bốn phần |
| `docs/FOLLOW_UP_TRACKER.md` `FU-437` | *«model mới vào roster ⇒ mọi ngày `14/15`»* | 🟡 **CHƯA ĐỦ** — một miền vẫn đủ 15 suốt tháng 6; hai miền kia chỉ có 8 vì lý do khác |
| `CLAUDE.md` §55 | mốc khoá `15:45 / 16:58 / 17:58` | 🟢 **KHỚP** nguồn đang chạy |

### 🔴 BA LỚP LỆCH NHAU — finding bắt buộc báo

**`DOC_SAID` ≠ `CODE_DID`** ở ba chỗ, **cả ba do chính em viết trong 24 giờ qua**, và **cả ba đã
rút lại** theo `PRJ-RETRACTION-001` (đủ bốn phần, **đúng chỗ đã công bố**).

**`OWNER_SAID` ≠ `DOC_SAID`:** owner yêu cầu *«truy `300` thật sự làm gì»* vì mặc định nó **đang
cắt** model. Đo cho thấy **ngược lại** — nó **không giết** model, và cơ chế owner muốn xây
**đã chạy**. Sổ theo dõi từng ghi ngược ⇒ **đã sửa trong phiên**.

**Không lệch nào bị bỏ qua.**

---

TanPhatAI cần làm: cập nhật `docs/CURRENT_TRUTH_MATRIX_20260824.md` §6 (hai câu đã rút lại, đừng trích bản cũ) và `FU-436` (đã chuyển sang sai-âm-tính, không còn là việc cần sửa); theo dõi bảy mục ở §9, trong đó **năm mục cần owner ký** vì đổi hành vi cổng hoặc lược đồ; **không** dùng `FU-436` hay hai câu ở `CURRENT_TRUTH_MATRIX` §6 làm căn cứ cho bất kỳ quyết định nào; chờ kết quả diff ảnh chụp `15:50` trước khi kết luận FINAL có bất biến trong thực tế hay không.
