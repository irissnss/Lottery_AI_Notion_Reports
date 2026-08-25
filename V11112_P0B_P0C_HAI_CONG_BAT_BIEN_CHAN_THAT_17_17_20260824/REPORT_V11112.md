# V11112 — 2026-08-24 (trưa) — HAI CỔNG BẤT BIẾN FINAL **CHỨNG MINH ĐƯỢC LÀ CHẶN THẬT** (17/17) · RÚT LẠI HAI CÂU SAI VỀ MÁY TRẠNG THÁI

**Ngày làm việc:** 24/08/2026 ·
**Ngày viết báo cáo này:** 26/08/2026 · **Commit riêng:** `0f4e162` ·
**Trạng thái:** `BÙ TỪ NGUỒN GỐC`

---

> ## ⚠️ ĐÂY LÀ BÁO CÁO **BÙ**, KHÔNG PHẢI BẢN VIẾT LÚC LÀM VIỆC
>
> Bản `V11112` làm ngày **24/08** nhưng **không có** thư mục báo cáo công khai —
> vi phạm `§57.2` đã tồn tại **2 ngày**.
> Cổng A55 cũ **không thấy** vì nó chỉ soi **8 bản gần nhất** (đã vá ở `V11122`, `FU-442`).
>
> **Ba nguồn dựng nên bản này — cả ba đều là bản ghi ĐƯƠNG THỜI:**
>
> | nguồn | quy mô |
> |---|---|
> | khối `## V11112` trong `CHANGELOG.md` — viết **ngay lúc làm việc** | **3,439 ký tự / 66 dòng** |
> | commit git mang nhãn `V11112` | **1** commit |
> | lượt owner trong vết phiên `.jsonl` cùng ngày | **có** |
> | khối phụ (`V11112b`/`c`/…) | — |
>
> 🔴 **PHẦN KHÔNG KHÔI PHỤC ĐƯỢC** — ghi thẳng, không suy:
> · **giờ chính xác** từng thao tác trong phiên · **vướng vấp giữa chừng** không được ghi lại lúc đó
> · **hash 4 bảng khoá trước/sau** (nếu phiên có chạm DB) · **PID trước/sau** (nếu có restart).
> Những chỗ đó dưới đây đều ghi `KHÔNG KHÔI PHỤC ĐƯỢC`, **không** điền số ước.

---

## 1. Tóm tắt

**`P0-B` + `P0-C` của prompt 34.**
### `RM-15` — cổng không qua thử coi như KHÔNG TỒN TẠI
Đo 24/08: **không một sự kiện chặn nào** trong journald (giữ từ 18/08) lẫn `scheduler_logs`.
Sáu ngày đó chắc chắn có bundle lên `v=2` ⇒ hoặc cổng cho qua đúng, hoặc **cổng chưa từng chạy**.
Không phân biệt được — đúng khuôn cổng `QD-041` từng **mù hoàn toàn** mà **luôn báo xanh**.
`_v11112_thu_chan_bat_bien.py` — **17/17**, hai chiều, chạy trên **DB tạm** dựng từ đúng lược đồ
production (đọc `sqlite_master`), **không chạm DB thật** (kiểm `mtime` + kích thước trước/sau).
**Hai cổng in ra thông điệp chặn thật:**
```
[FREEZE-GUARD] 🔒 Bundle MT/2026-08-27 đã verified lúc … → KHÔNG overwrite
[FREEZE-55]    🔒 Bundle MB/2026-08-21 đã qua mốc freeze → KHÔNG overwrite (single-flight total)
```
⇒ **cổng TỐT**, chỉ là chưa lần nào phải nổ. `n=0` trong log **không phải cổng mù**.
Biên đúng cả ba miền: MN `15:44` chưa khoá / `15:45` đã khoá · MT `16:57/16:58` · MB `17:57/17:58`.
Ngày quá khứ **luôn** khoá (chống sửa hồi tố). `T_CHOT_MARKS` đều **trước** `FREEZE_MARKS`.
**Ghi nhận cửa hậu:** `force=True` đi xuyên **cả hai** cổng. Grep toàn kho: **0 nơi truyền**.
### `P0-B` — writer/reader `final_bundles`: **đúng HAI câu lệnh ghi** toàn kho sống
| | câu lệnh | hàm | người gọi |

## 2. Owner yêu cầu gì (nguyên văn)

> *«em đã push báo cáo githubs chưa em?»*
> — owner, **24/08/2026 08:38** (giờ VN)

> *«PROMPT TỔNG LỰC LẦN 33 FINAL BẤT BIẾN · OFFICIAL FALLBACK · SỐ PHỤ · XIÊN 2/3 · 3 CÀNG · ADMIN-ONLY · BỘ ĐỐI CHỨNG VPS Đây là prompt thi hành sau V11110, hợp nhất toàn bộ quyết định Owner ngày 24/08 lúc 09:35, 09:49, 09:59 và 10:09. Không được sử dụng lại phương án viewer, P&L, timeout, sản phẩm output hoặc cách tính thành tích cũ đã bị Owner thay thế. ================================================== 0. VAI TRÒ, MỤ…»*
> — owner, **24/08/2026 10:25** (giờ VN)

> *«PROMPT TỔNG LỰC LẦN 34 TIẾP NỐI PROMPT 33 — DỰNG FINAL BẤT BIẾN DÁN PROMPT NÀY VÀO ĐÚNG PHIÊN AGENT IDE ĐANG THỰC HIỆN PROMPT 33. Đây là lệnh TIẾP NỐI và sắp lại mức ưu tiên sau bằng chứng runtime ngày 24/08. KHÔNG mở phiên cạnh tranh, KHÔNG làm lại việc GĐ-0/GĐ-1 đã hoàn thành, KHÔNG dừng bốn Algorithm Card đang chạy. Nơi nào trình tự cũ xung đột, ưu tiên P0 FINAL trong prompt này. ==================================…»*
> — owner, **24/08/2026 12:11** (giờ VN)


*(Trích từ corpus lượt owner đã khử trùng của vết phiên `.jsonl`; giờ đã quy về giờ Việt Nam.)*

## 3. Đào bới / phát hiện

Toàn văn khối `CHANGELOG` đương thời — **nguồn chính** của bản này:

## V11112 — 2026-08-24 (trưa) — HAI CỔNG BẤT BIẾN FINAL **CHỨNG MINH ĐƯỢC LÀ CHẶN THẬT** (17/17) · RÚT LẠI HAI CÂU SAI VỀ MÁY TRẠNG THÁI

**`P0-B` + `P0-C` của prompt 34.**

### `RM-15` — cổng không qua thử coi như KHÔNG TỒN TẠI

Đo 24/08: **không một sự kiện chặn nào** trong journald (giữ từ 18/08) lẫn `scheduler_logs`.
Sáu ngày đó chắc chắn có bundle lên `v=2` ⇒ hoặc cổng cho qua đúng, hoặc **cổng chưa từng chạy**.
Không phân biệt được — đúng khuôn cổng `QD-041` từng **mù hoàn toàn** mà **luôn báo xanh**.

`_v11112_thu_chan_bat_bien.py` — **17/17**, hai chiều, chạy trên **DB tạm** dựng từ đúng lược đồ
production (đọc `sqlite_master`), **không chạm DB thật** (kiểm `mtime` + kích thước trước/sau).

**Hai cổng in ra thông điệp chặn thật:**

```
[FREEZE-GUARD] 🔒 Bundle MT/2026-08-27 đã verified lúc … → KHÔNG overwrite
[FREEZE-55]    🔒 Bundle MB/2026-08-21 đã qua mốc freeze → KHÔNG overwrite (single-flight total)
```

⇒ **cổng TỐT**, chỉ là chưa lần nào phải nổ. `n=0` trong log **không phải cổng mù**.
Biên đúng cả ba miền: MN `15:44` chưa khoá / `15:45` đã khoá · MT `16:57/16:58` · MB `17:57/17:58`.
Ngày quá khứ **luôn** khoá (chống sửa hồi tố). `T_CHOT_MARKS` đều **trước** `FREEZE_MARKS`.

**Ghi nhận cửa hậu:** `force=True` đi xuyên **cả hai** cổng. Grep toàn kho: **0 nơi truyền**.

### `P0-B` — writer/reader `final_bundles`: **đúng HAI câu lệnh ghi** toàn kho sống

| | câu lệnh | hàm | người gọi |
|---|---|---|---|
| **W1** | `INSERT` `database.py:4648` | `save_final_bundle:4581` | **2** — `main.py:10391` (production) · `_backfill_bundles.py:177` |
| **W2** | `UPDATE` `database.py:4933` | `verify_final_bundle:4812` | **10** |

**Hai chỗ trông như writer mà KHÔNG phải** (phân loại, không đếm thô — `RM-09`):
`_v10889_no_copy.py:51` chạy `DELETE` trên **bản sao `:memory:`** (phép thử BỊT MẮT) ·
`_v10821_probe3.py:72` là **chuỗi grep**.

### `P0-A` — FINAL có bất biến không

`verify_final_bundle` ghi **đúng 7 cột**, **không một cột NHÓM A nào** ⇒ writer chấm kết quả
**không thể** đổi số dự đoán. `ON CONFLICT DO UPDATE` ghi đè **11/12** cột NHÓM A — rủi ro thật,
chỉ hai cổng chặn.

🔴 **Lỗ hổng quan sát chưa bịt được:** `updated_at` **bằng đúng** `verified_at` ở mọi dòng `v=2`
cả ba miền ⇒ lần ghi cuối là settlement, mà settlement **không chạm `bundle_version`** ⇒ **dấu
thời gian của lần bump `v` đã bị ghi đè mất**. `created_at` không nằm trong `DO UPDATE SET` nên
giữ giờ insert **đầu**. ⇒ **không thể biết lần ghi thứ hai xảy ra lúc nào từ dữ liệu đang có**.

### 🔴 RÚT LẠI HAI CÂU SAI — `PRJ-RETRACTION-001`

**Chỗ gốc:** `docs/CURRENT_TRUTH_MATRIX_20260824.md` §6, đã commit sáng 24/08.

**R1 nguyên văn:** *«**Không có bước «chụp snapshot và finalize đúng một lần lúc 15:45»** như hợp
đồng `GĐ-2` mô tả. Trên thực tế FINAL đã cố định từ `05:19`.»*
**Điều đúng:** **CÓ**, tên là **T-chốt**, đăng ký đủ ba miền `scheduler.py:8189-8198`,
`T_CHOT_MARKS = {MN 15:40, MT 16:55, MB 17:55}`. Em kết luận từ **`created_at` một dòng** — mà
`created_at` **không nằm trong `DO UPDATE SET`** nên nó **không thể** cho biết có lần ghi thứ hai.

**R2 nguyên văn:** *«state machine `ROSTER_FROZEN → … → RESULT_SCORED` **chưa tồn tại**.»*
**Điều đúng:** bộ khung **đã tồn tại**, thiếu **hai chặng đầu** — `FINAL_LOCKED` 🟢 (hai cổng
freeze) · `RESULT_SCORED` 🟢 · `ROSTER_FROZEN` 🔴 · `ELIGIBILITY_CLOSED` 🔴.

**Quyết định nào đã dựa vào:** chưa cái nào.

Bản đồ AS-IS đầy đủ: `docs/FINAL_OUTPUT_CONTRACT_20260824.md`.

## 4. Hướng xử lý và vì sao chọn

Lý do chọn nằm trong chính khối `CHANGELOG` ở mục 3 — đó là bản ghi viết **lúc làm việc**,
không phải suy lại. Phần **cân nhắc phương án bị loại** thì 🔴 **KHÔNG KHÔI PHỤC ĐƯỢC**: nó chỉ
tồn tại trong vết phiên và không được ghi vào tài liệu nào lúc đó.

## 5. Đã làm gì

| commit | ngày (giờ VN) | tệp | tổng |
|---|---|---|---|
| `0f4e162` | 2026-08-24 12:37:04 | CHANGELOG.md, docs/AUTOMATION_HISTORY.jsonl, docs/AUTOMATION_STATE.json, docs/CURRENT_TRUTH_MATRIX_20260824.md, docs/CURRENT_TRUTH_SSOT.md, docs/FINAL | 7 files changed, 778 insertions(+), 9 deletions(-) |

## 6. Cổng kiểm

🔴 **KHÔNG KHÔI PHỤC ĐƯỢC output cổng của phiên gốc** — cổng in ra `stdout`, không ghi tệp
(đúng khuyết tật `RM-15` mà `V11121` đã vá cho `cong_git_commit.py` bằng sổ điểm danh).

Điều **kiểm được hôm nay**, `26/08/2026`:

| phép | kết quả |
|---|---|
| commit của bản này còn trong `git log` | ✅ **1/1** còn nguyên, đều là tổ tiên của `origin/master` |
| khối `CHANGELOG` còn nguyên | ✅ 3,439 ký tự |
| bản này đã có báo cáo công khai chưa | ✅ **có, từ bản bù này** — trước đó `A55_VIOLATION_REPORT_MISSING` |

## 7. Vướng vấp

🔴 **KHÔNG KHÔI PHỤC ĐƯỢC** vướng vấp trong phiên gốc — không tài liệu nào ghi lại lúc đó.

Vướng vấp **của chính việc bù này**, ghi trung thực: bản bù dựng từ ba nguồn đương thời nhưng
**không thay được** một báo cáo viết lúc làm việc. Cụ thể mất: giờ từng thao tác · các phương án
đã cân nhắc rồi loại · lỗi gặp giữa chừng · trạng thái trước/sau của DB nếu phiên có chạm.

## 8. Gỡ về

Bản bù này **chỉ thêm tài liệu**, không đụng mã và không đụng dữ liệu ⇒ gỡ về =
`git rm -r V11112_P0B_P0C_HAI_CONG_BAT_BIEN_CHAN_THAT_17_17_20260824/` rồi commit lại. Trạng thái quay về đúng như trước khi bù.

Việc gỡ về của **bản gốc `V11112`** nằm trong chính khối `CHANGELOG` ở mục 3 (nếu bản đó có ghi).

## 9. Theo dõi tiếp

| mã | việc | trạng thái |
|---|---|---|
| `FU-442` | vá cổng A55 — chính lỗ hổng làm bản này vô hình | ✅ **ĐÃ VÁ** ở `V11122`, thử chặn **11/11** |
| — | bù nốt các bản còn thiếu | trên **toàn dải từ mốc thi hành `V10921`** còn **32** bản thiếu báo cáo; 10 bản của đợt này là nhóm ưu tiên |
| — | ngưỡng đóng bằng số | `_v10921_report_gate.py` chạy **không tham số** ⇒ `V11112` không còn trong danh sách `THIẾU BÁO CÁO` |

---

## 10. BA LỚP NGUỒN (§62 · A60)

### `OWNER_SAID`
> *«em đã push báo cáo githubs chưa em?»*
> — owner, **24/08/2026 08:38** (giờ VN)

> *«PROMPT TỔNG LỰC LẦN 33 FINAL BẤT BIẾN · OFFICIAL FALLBACK · SỐ PHỤ · XIÊN 2/3 · 3 CÀNG · ADMIN-ONLY · BỘ ĐỐI CHỨNG VPS Đây là prompt thi hành sau V11110, hợp nhất toàn bộ quyết định Owner ngày 24/08 lúc 09:35, 09:49, 09:59 và 10:09. Không được sử dụng lại phương án viewer, P&L, timeout, sản phẩm output hoặc cách tính thành tích cũ đã bị Owner thay thế. ================================================== 0. VAI TRÒ, MỤ…»*
> — owner, **24/08/2026 10:25** (giờ VN)

> *«PROMPT TỔNG LỰC LẦN 34 TIẾP NỐI PROMPT 33 — DỰNG FINAL BẤT BIẾN DÁN PROMPT NÀY VÀO ĐÚNG PHIÊN AGENT IDE ĐANG THỰC HIỆN PROMPT 33. Đây là lệnh TIẾP NỐI và sắp lại mức ưu tiên sau bằng chứng runtime ngày 24/08. KHÔNG mở phiên cạnh tranh, KHÔNG làm lại việc GĐ-0/GĐ-1 đã hoàn thành, KHÔNG dừng bốn Algorithm Card đang chạy. Nơi nào trình tự cũ xung đột, ưu tiên P0 FINAL trong prompt này. ==================================…»*
> — owner, **24/08/2026 12:11** (giờ VN)


### `CODE_DID`
| điều mã **thực sự** làm | bằng chứng |
|---|---|
| 1 commit mang nhãn `V11112` | `0f4e162` — còn nguyên trong `git log`, đều là tổ tiên `origin/master` |
| tệp bị đụng | xem bảng mục 5 |
| bản này **chưa từng** có báo cáo công khai cho tới hôm nay | `_v10921_report_gate.py` liệt `V11112` trong `THIẾU BÁO CÁO` trước khi bù |

### `DOC_SAID`
| tài liệu | nói gì | khớp code chưa |
|---|---|---|
| `CHANGELOG.md` khối `## V11112` | 3,439 ký tự, viết đương thời | 🟢 **khớp** — commit tồn tại đúng ngày ghi |
| kho báo cáo công khai | **không có** thư mục `V11112_*` | 🔴 **LỆCH** — đã đóng bằng bản bù này |

### 🔴 BA LỚP LỆCH NHAU
`DOC_SAID` ≠ `CODE_DID`: mã đã chạy và đã commit, `CHANGELOG` đã ghi, nhưng **kho công khai không
có gì** suốt 2 ngày. Đó là `A55_VIOLATION_REPORT_MISSING`, và nó **vô hình** vì cổng chỉ soi 8
bản gần nhất — nay đã vá (`FU-442` · `V11122`).

---

**TanPhatAI cần làm:** ghi nhận đây là **báo cáo BÙ** viết ngày 26/08/2026 cho việc làm ngày
24/08, dựng từ **ba nguồn đương thời** (CHANGELOG 3,439 ký tự ·
1 commit · vết phiên), **không** phải bản viết lúc làm việc — mọi chỗ không khôi phục
được đã ghi thẳng là `KHÔNG KHÔI PHỤC ĐƯỢC`, **không** điền số ước.
