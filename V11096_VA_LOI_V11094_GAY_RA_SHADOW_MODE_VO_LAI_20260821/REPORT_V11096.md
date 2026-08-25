# V11096 — VÁ LỖI CHÍNH `V11094` GÂY RA: `shadow_mode=True` vỡ lại · dựng cổng chống tái phạm

**Ngày làm việc:** 21/08/2026 ·
**Ngày viết báo cáo này:** 26/08/2026 · **Commit riêng:** `ce37ba5`, `194fed1`, `2fb1919`, `676e34b` ·
**Trạng thái:** `BÙ TỪ NGUỒN GỐC`

---

> ## ⚠️ ĐÂY LÀ BÁO CÁO **BÙ**, KHÔNG PHẢI BẢN VIẾT LÚC LÀM VIỆC
>
> Bản `V11096` làm ngày **21/08** nhưng **không có** thư mục báo cáo công khai —
> vi phạm `§57.2` đã tồn tại **5 ngày**.
> Cổng A55 cũ **không thấy** vì nó chỉ soi **8 bản gần nhất** (đã vá ở `V11122`, `FU-442`).
>
> **Ba nguồn dựng nên bản này — cả ba đều là bản ghi ĐƯƠNG THỜI:**
>
> | nguồn | quy mô |
> |---|---|
> | khối `## V11096` trong `CHANGELOG.md` — viết **ngay lúc làm việc** | **2,273 ký tự / 44 dòng** |
> | commit git mang nhãn `V11096` | **4** commit |
> | lượt owner trong vết phiên `.jsonl` cùng ngày | **có** |
> | khối phụ (`V11096b`/`c`/…) | — |
>
> 🔴 **PHẦN KHÔNG KHÔI PHỤC ĐƯỢC** — ghi thẳng, không suy:
> · **giờ chính xác** từng thao tác trong phiên · **vướng vấp giữa chừng** không được ghi lại lúc đó
> · **hash 4 bảng khoá trước/sau** (nếu phiên có chạm DB) · **PID trước/sau** (nếu có restart).
> Những chỗ đó dưới đây đều ghi `KHÔNG KHÔI PHỤC ĐƯỢC`, **không** điền số ước.

---

## 1. Tóm tắt

**21/08/2026 tối** · phát hiện khi rà soát cuối chu kỳ · **chưa deploy**.
### Lỗi — và nó là bản sao đúng của một lỗi 13 ngày trước
`V11094` (`FU-404`) thêm `lift_365` vào câu `SELECT` của khối `MINED RULES` ⇒ **12 cột**. Sửa
chỗ mở gói ở nhánh thường, **bỏ quên chỗ thứ hai** trong nhánh `shadow_mode=True`
(`gpt_analyzer.py:4802`) ⇒ `ValueError: too many values to unpack (expected 11)`.
**Hậu quả đo được:** `build_context_pack(shadow_mode=True)` tụt còn **106 ký tự** thay vì
~11.000, ở **CẢ BA MIỀN**.
> **Đây đúng là `FU-341`/`QD-042` lặp lại.** Lần trước: `SELECT` 11 cột, chỗ mở gói còn 10 ⇒
> `shadow_mode=True` **vỡ 67 NGÀY** không ai biết. Lần này cùng cơ chế, chỉ khác con số
> `10→11` thành `11→12`. **Cách nhau 13 ngày.**
**Vì sao lỗi này độc:** nó **không làm sập tiến trình**. `build_context_pack` có `try/except`
nên khi vỡ, nó trả một chuỗi ngắn — model vẫn nhận prompt, vẫn trả lời, vẫn ra số. Không lỗi,
không cảnh báo, không triệu chứng. **Chỉ lộ ra khi ĐO ĐỘ DÀI.**
**Và chú thích cảnh báo đã có sẵn ngay trên dòng lỗi** — do chính `V11032` viết sau 67 ngày kia.
Nó **không cứu được**, vì người sửa xuất phát từ **câu `SELECT`**, không xuất phát từ chỗ mở gói.
### Cổng mới `_v11096_kiem_mo_goi_rules.py`
`§61` nói rõ: một lỗi **tái phạm hai lần ⇒ phải dựng CỔNG MÁY**, không được chỉ hứa.
Cổng đếm **tĩnh** số cột của từng câu `SELECT` trên `mined_rules` và so với số tên ở **mọi**

## 2. Owner yêu cầu gì (nguyên văn)

> *«PROMPT TỔNG LỰC LẦN 22 — GO 21/08: THỰC THI GÓI 12 MỤC + 1 THIẾT KẾ (sáng 21/08 · QD-041 HẾT HẠN · thực thi theo docs/BAN_DO_THUC_THI_2108.md ĐÃ CHỐT tối 20/08) ═══ BỐI CẢNH ĐÃ CHỐT — KHÔNG MỞ LẠI, KHÔNG HỎI LẠI ═══ • Gói = 12 mục thực thi + 1 việc thiết kế. D3 ĐÃ HOÃN (FU-411, lối C) — CẤM chen vào. • FU-284 ĐÃ ĐÓNG «không đủ sức» — cấm mở lại. • Bốn ô verdict đã điền: bầy đàn CÓ TÁC DỤNG (0,5815 vs nền 0,4739) · DE…»*
> — owner, **21/08/2026 08:52** (giờ VN)

> *«Tới hạn rồi xong chu kỳ theo dõi, chu kỳ xổ số hôm nay rồi. Em tiến hành kiểm tra , rà soát tất cả chuẩn chị cho việc xử lý đi nào»*
> — owner, **21/08/2026 19:00** (giờ VN)

> *«deploy chứ chờ gì nữa em? FU-290A (đề xuất: không cắt vì độ trễ ) ==> ko rõ model nào nhưng chưa cắt là đúng vì độ trễ do nhiều yếu tố bới quá nhiều model quá mà em FU-394 (đề xuất: gỡ hẳn nhánh gan, hành vi không đổi) ==> cắt đi FU-416 (vá một dòng) · FU-393 (ba lối a/b/c). ==> chi tiết cụ thể là gì diễn giải cụ thể toàn là mã ngắn gọn mà bắt duyệt làm sao mà duyệt được duyệt mù ah em.»*
> — owner, **21/08/2026 19:49** (giờ VN)

> *«PROMPT TỔNG LỰC LẦN 23 — TỐI 21/08: VÁ FU-416 + KIỂM KÊ DỌN DẸP + SOẠN TÀI LIỆU DUYỆT GỘP ═══ OWNER KÝ 20:15 21/08 — KHÔNG HỎI LẠI ═══ ① Vá FU-416 NGAY phiên này — một dòng: thêm key=lambda x: (-x[1], x[0]) tại gpt_analyzer.py:5941 (sorted không phá hoà rồi cắt [:10]/[:6] ⇒ số nào model nhìn thấy trước tiên đang do HẠT BĂM quyết). ② Dọn dẹp app theo kiểu: KIỂM KÊ CÓ BẰNG CHỨNG → owner duyệt một lượt → MỚI CẮT. Phiên …»*
> — owner, **21/08/2026 20:19** (giờ VN)

> *«Đã push báo cáo hết chưa? Đề xuất tiếp theo là vấn đề nào còn tồn đọng , vấn đề nào chưa tìm hiểu đào sâu, kế hoạch cắt giảm model ai tới đâu rồi chỉ phí gánh ngày càng nặng mà chả hiệu quả gì.»*
> — owner, **21/08/2026 21:06** (giờ VN)

> *«Chi phí ở đây không phải là model đắt tiền đong đếm bằng tiền. Chị phí chạy quá nhiều model ai lãng phí mà trong khi đó không đo được sức mạnh của model, model nào đáng dùng không đáng dùng, đắt cũng được nhưng phải chất lượng , phù hợp với dự án, phù hợp với ngữ cảnh, prompt phải tối ưu thuần ngữ cảnh nhồi toàn số đã lọc sẵn vào thì model ai đâu hoạt động đúng nghĩa của nó em. Đắt phải chất , ít nhưng hiệu quả đông …»*
> — owner, **21/08/2026 21:21** (giờ VN)


*(Trích từ corpus lượt owner đã khử trùng của vết phiên `.jsonl`; giờ đã quy về giờ Việt Nam.)*

## 3. Đào bới / phát hiện

Toàn văn khối `CHANGELOG` đương thời — **nguồn chính** của bản này:

## V11096 — VÁ LỖI CHÍNH `V11094` GÂY RA: `shadow_mode=True` vỡ lại · dựng cổng chống tái phạm

**21/08/2026 tối** · phát hiện khi rà soát cuối chu kỳ · **chưa deploy**.

### Lỗi — và nó là bản sao đúng của một lỗi 13 ngày trước

`V11094` (`FU-404`) thêm `lift_365` vào câu `SELECT` của khối `MINED RULES` ⇒ **12 cột**. Sửa
chỗ mở gói ở nhánh thường, **bỏ quên chỗ thứ hai** trong nhánh `shadow_mode=True`
(`gpt_analyzer.py:4802`) ⇒ `ValueError: too many values to unpack (expected 11)`.

**Hậu quả đo được:** `build_context_pack(shadow_mode=True)` tụt còn **106 ký tự** thay vì
~11.000, ở **CẢ BA MIỀN**.

> **Đây đúng là `FU-341`/`QD-042` lặp lại.** Lần trước: `SELECT` 11 cột, chỗ mở gói còn 10 ⇒
> `shadow_mode=True` **vỡ 67 NGÀY** không ai biết. Lần này cùng cơ chế, chỉ khác con số
> `10→11` thành `11→12`. **Cách nhau 13 ngày.**

**Vì sao lỗi này độc:** nó **không làm sập tiến trình**. `build_context_pack` có `try/except`
nên khi vỡ, nó trả một chuỗi ngắn — model vẫn nhận prompt, vẫn trả lời, vẫn ra số. Không lỗi,
không cảnh báo, không triệu chứng. **Chỉ lộ ra khi ĐO ĐỘ DÀI.**

**Và chú thích cảnh báo đã có sẵn ngay trên dòng lỗi** — do chính `V11032` viết sau 67 ngày kia.
Nó **không cứu được**, vì người sửa xuất phát từ **câu `SELECT`**, không xuất phát từ chỗ mở gói.

### Cổng mới `_v11096_kiem_mo_goi_rules.py`

`§61` nói rõ: một lỗi **tái phạm hai lần ⇒ phải dựng CỔNG MÁY**, không được chỉ hứa.

Cổng đếm **tĩnh** số cột của từng câu `SELECT` trên `mined_rules` và so với số tên ở **mọi**
vòng `for … in rules:` / `in rwc_rules:`. Không cần DB, không cần chạy prompt.
Đo hiện tại: **3 chỗ mở gói, cả 3 khớp 12 = 12**.
Thử chặn `RM-15`: `[1]` sạch → thoát 0 · `[2]` bỏ một tên → **thoát 1** · `[3]` khôi phục →
thoát 0 · `gpt_analyzer.py` **khớp từng byte**.

> **Bản đầu của cổng tự báo đỏ trên mã ĐÚNG** — nó vớ phải câu `SELECT` đầu tiên trong tệp
> (6 cột, thuộc hàm khác) thay vì câu ngay trước vòng lặp. Đã sửa thành đi **ngược từ vòng lặp**.
> Ghi lại vì đó là bài học riêng: **cổng báo đỏ thì câu hỏi đầu tiên là «đỏ vì mã, hay vì phép
> đo?»** — hôm nay là vì phép đo.

### Nghiệm thu bằng cổng THẬT

`_v11032_kiem_va.py`: **6/6 ô ĐẠT** — `shadow_mode=True` nay ra **14.226 · 13.669 · 17.123**
ký tự (MN · MT · MB), đều có `PHASE-STATE=True`.

## 4. Hướng xử lý và vì sao chọn

Lý do chọn nằm trong chính khối `CHANGELOG` ở mục 3 — đó là bản ghi viết **lúc làm việc**,
không phải suy lại. Phần **cân nhắc phương án bị loại** thì 🔴 **KHÔNG KHÔI PHỤC ĐƯỢC**: nó chỉ
tồn tại trong vết phiên và không được ghi vào tài liệu nào lúc đó.

## 5. Đã làm gì

| commit | ngày (giờ VN) | tệp | tổng |
|---|---|---|---|
| `ce37ba5` | 2026-08-21 19:44:30 | web/backend/_v11096_deploy.py | 1 file changed, 244 insertions(+) |
| `194fed1` | 2026-08-21 19:39:41 | web/backend/_v11036_kiem_no_answer.py | 1 file changed, 43 insertions(+), 1 deletion(-) |
| `2fb1919` | 2026-08-21 19:31:26 | docs/OWNER_DECISION_LEDGER.json, web/backend/_v11028_cong_dong_bang.py | 2 files changed, 76 insertions(+), 17 deletions(-) |
| `676e34b` | 2026-08-21 19:23:38 | CHANGELOG.md, docs/AUTOMATION_HISTORY.jsonl, docs/AUTOMATION_STATE.json, docs/CURRENT_TRUTH_SSOT.md, docs/_I2_DA_CHAY.json, web/backend/_v11096_kiem_m | 7 files changed, 262 insertions(+), 7 deletions(-) |

## 6. Cổng kiểm

🔴 **KHÔNG KHÔI PHỤC ĐƯỢC output cổng của phiên gốc** — cổng in ra `stdout`, không ghi tệp
(đúng khuyết tật `RM-15` mà `V11121` đã vá cho `cong_git_commit.py` bằng sổ điểm danh).

Điều **kiểm được hôm nay**, `26/08/2026`:

| phép | kết quả |
|---|---|
| commit của bản này còn trong `git log` | ✅ **4/4** còn nguyên, đều là tổ tiên của `origin/master` |
| khối `CHANGELOG` còn nguyên | ✅ 2,273 ký tự |
| bản này đã có báo cáo công khai chưa | ✅ **có, từ bản bù này** — trước đó `A55_VIOLATION_REPORT_MISSING` |

## 7. Vướng vấp

🔴 **KHÔNG KHÔI PHỤC ĐƯỢC** vướng vấp trong phiên gốc — không tài liệu nào ghi lại lúc đó.

Vướng vấp **của chính việc bù này**, ghi trung thực: bản bù dựng từ ba nguồn đương thời nhưng
**không thay được** một báo cáo viết lúc làm việc. Cụ thể mất: giờ từng thao tác · các phương án
đã cân nhắc rồi loại · lỗi gặp giữa chừng · trạng thái trước/sau của DB nếu phiên có chạm.

## 8. Gỡ về

Bản bù này **chỉ thêm tài liệu**, không đụng mã và không đụng dữ liệu ⇒ gỡ về =
`git rm -r V11096_VA_LOI_V11094_GAY_RA_SHADOW_MODE_VO_LAI_20260821/` rồi commit lại. Trạng thái quay về đúng như trước khi bù.

Việc gỡ về của **bản gốc `V11096`** nằm trong chính khối `CHANGELOG` ở mục 3 (nếu bản đó có ghi).

## 9. Theo dõi tiếp

| mã | việc | trạng thái |
|---|---|---|
| `FU-442` | vá cổng A55 — chính lỗ hổng làm bản này vô hình | ✅ **ĐÃ VÁ** ở `V11122`, thử chặn **11/11** |
| — | bù nốt các bản còn thiếu | trên **toàn dải từ mốc thi hành `V10921`** còn **32** bản thiếu báo cáo; 10 bản của đợt này là nhóm ưu tiên |
| — | ngưỡng đóng bằng số | `_v10921_report_gate.py` chạy **không tham số** ⇒ `V11096` không còn trong danh sách `THIẾU BÁO CÁO` |

---

## 10. BA LỚP NGUỒN (§62 · A60)

### `OWNER_SAID`
> *«PROMPT TỔNG LỰC LẦN 22 — GO 21/08: THỰC THI GÓI 12 MỤC + 1 THIẾT KẾ (sáng 21/08 · QD-041 HẾT HẠN · thực thi theo docs/BAN_DO_THUC_THI_2108.md ĐÃ CHỐT tối 20/08) ═══ BỐI CẢNH ĐÃ CHỐT — KHÔNG MỞ LẠI, KHÔNG HỎI LẠI ═══ • Gói = 12 mục thực thi + 1 việc thiết kế. D3 ĐÃ HOÃN (FU-411, lối C) — CẤM chen vào. • FU-284 ĐÃ ĐÓNG «không đủ sức» — cấm mở lại. • Bốn ô verdict đã điền: bầy đàn CÓ TÁC DỤNG (0,5815 vs nền 0,4739) · DE…»*
> — owner, **21/08/2026 08:52** (giờ VN)

> *«Tới hạn rồi xong chu kỳ theo dõi, chu kỳ xổ số hôm nay rồi. Em tiến hành kiểm tra , rà soát tất cả chuẩn chị cho việc xử lý đi nào»*
> — owner, **21/08/2026 19:00** (giờ VN)

> *«deploy chứ chờ gì nữa em? FU-290A (đề xuất: không cắt vì độ trễ ) ==> ko rõ model nào nhưng chưa cắt là đúng vì độ trễ do nhiều yếu tố bới quá nhiều model quá mà em FU-394 (đề xuất: gỡ hẳn nhánh gan, hành vi không đổi) ==> cắt đi FU-416 (vá một dòng) · FU-393 (ba lối a/b/c). ==> chi tiết cụ thể là gì diễn giải cụ thể toàn là mã ngắn gọn mà bắt duyệt làm sao mà duyệt được duyệt mù ah em.»*
> — owner, **21/08/2026 19:49** (giờ VN)

> *«PROMPT TỔNG LỰC LẦN 23 — TỐI 21/08: VÁ FU-416 + KIỂM KÊ DỌN DẸP + SOẠN TÀI LIỆU DUYỆT GỘP ═══ OWNER KÝ 20:15 21/08 — KHÔNG HỎI LẠI ═══ ① Vá FU-416 NGAY phiên này — một dòng: thêm key=lambda x: (-x[1], x[0]) tại gpt_analyzer.py:5941 (sorted không phá hoà rồi cắt [:10]/[:6] ⇒ số nào model nhìn thấy trước tiên đang do HẠT BĂM quyết). ② Dọn dẹp app theo kiểu: KIỂM KÊ CÓ BẰNG CHỨNG → owner duyệt một lượt → MỚI CẮT. Phiên …»*
> — owner, **21/08/2026 20:19** (giờ VN)

> *«Đã push báo cáo hết chưa? Đề xuất tiếp theo là vấn đề nào còn tồn đọng , vấn đề nào chưa tìm hiểu đào sâu, kế hoạch cắt giảm model ai tới đâu rồi chỉ phí gánh ngày càng nặng mà chả hiệu quả gì.»*
> — owner, **21/08/2026 21:06** (giờ VN)

> *«Chi phí ở đây không phải là model đắt tiền đong đếm bằng tiền. Chị phí chạy quá nhiều model ai lãng phí mà trong khi đó không đo được sức mạnh của model, model nào đáng dùng không đáng dùng, đắt cũng được nhưng phải chất lượng , phù hợp với dự án, phù hợp với ngữ cảnh, prompt phải tối ưu thuần ngữ cảnh nhồi toàn số đã lọc sẵn vào thì model ai đâu hoạt động đúng nghĩa của nó em. Đắt phải chất , ít nhưng hiệu quả đông …»*
> — owner, **21/08/2026 21:21** (giờ VN)


### `CODE_DID`
| điều mã **thực sự** làm | bằng chứng |
|---|---|
| 4 commit mang nhãn `V11096` | `ce37ba5`, `194fed1`, `2fb1919`, `676e34b` — còn nguyên trong `git log`, đều là tổ tiên `origin/master` |
| tệp bị đụng | xem bảng mục 5 |
| bản này **chưa từng** có báo cáo công khai cho tới hôm nay | `_v10921_report_gate.py` liệt `V11096` trong `THIẾU BÁO CÁO` trước khi bù |

### `DOC_SAID`
| tài liệu | nói gì | khớp code chưa |
|---|---|---|
| `CHANGELOG.md` khối `## V11096` | 2,273 ký tự, viết đương thời | 🟢 **khớp** — commit tồn tại đúng ngày ghi |
| kho báo cáo công khai | **không có** thư mục `V11096_*` | 🔴 **LỆCH** — đã đóng bằng bản bù này |

### 🔴 BA LỚP LỆCH NHAU
`DOC_SAID` ≠ `CODE_DID`: mã đã chạy và đã commit, `CHANGELOG` đã ghi, nhưng **kho công khai không
có gì** suốt 5 ngày. Đó là `A55_VIOLATION_REPORT_MISSING`, và nó **vô hình** vì cổng chỉ soi 8
bản gần nhất — nay đã vá (`FU-442` · `V11122`).

---

**TanPhatAI cần làm:** ghi nhận đây là **báo cáo BÙ** viết ngày 26/08/2026 cho việc làm ngày
21/08, dựng từ **ba nguồn đương thời** (CHANGELOG 2,273 ký tự ·
4 commit · vết phiên), **không** phải bản viết lúc làm việc — mọi chỗ không khôi phục
được đã ghi thẳng là `KHÔNG KHÔI PHỤC ĐƯỢC`, **không** điền số ước.
