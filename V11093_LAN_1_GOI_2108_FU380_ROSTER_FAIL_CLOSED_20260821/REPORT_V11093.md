# V11093 — LÀN 1 GÓI 21/08: `FU-380` vá roster fail-closed · mục #12 gỡ `latency_score`

**Ngày làm việc:** 21/08/2026 ·
**Ngày viết báo cáo này:** 26/08/2026 · **Commit riêng:** `143a95e`, `e3ebc19`, `3cea289` ·
**Trạng thái:** `BÙ TỪ NGUỒN GỐC`

---

> ## ⚠️ ĐÂY LÀ BÁO CÁO **BÙ**, KHÔNG PHẢI BẢN VIẾT LÚC LÀM VIỆC
>
> Bản `V11093` làm ngày **21/08** nhưng **không có** thư mục báo cáo công khai —
> vi phạm `§57.2` đã tồn tại **5 ngày**.
> Cổng A55 cũ **không thấy** vì nó chỉ soi **8 bản gần nhất** (đã vá ở `V11122`, `FU-442`).
>
> **Ba nguồn dựng nên bản này — cả ba đều là bản ghi ĐƯƠNG THỜI:**
>
> | nguồn | quy mô |
> |---|---|
> | khối `## V11093` trong `CHANGELOG.md` — viết **ngay lúc làm việc** | **3,290 ký tự / 52 dòng** |
> | commit git mang nhãn `V11093` | **3** commit |
> | lượt owner trong vết phiên `.jsonl` cùng ngày | **có** |
> | khối phụ (`V11093b`/`c`/…) | — |
>
> 🔴 **PHẦN KHÔNG KHÔI PHỤC ĐƯỢC** — ghi thẳng, không suy:
> · **giờ chính xác** từng thao tác trong phiên · **vướng vấp giữa chừng** không được ghi lại lúc đó
> · **hash 4 bảng khoá trước/sau** (nếu phiên có chạm DB) · **PID trước/sau** (nếu có restart).
> Những chỗ đó dưới đây đều ghi `KHÔNG KHÔI PHỤC ĐƯỢC`, **không** điền số ước.

---

## 1. Tóm tắt

**21/08/2026 sáng** · `QD-041` **hết hạn**, gói mở khoá · `QD-068` · **production chưa đổi**
(chưa deploy, không ghi DB) — LÀN 1 theo định nghĩa **không chạm đường sinh số**.
### `#11 FU-380` — hai danh sách cứng **fail-closed** trôi khỏi registry
Ngưỡng đăng ký trước (owner ký 00:33 09/08): *«so hai danh sách cứng với
`get_output_eligible_ids()`, chênh > 0 phần tử ⇒ vá»*. `FU-284` đã đóng 20/08 nên rào đã hết.
**Đo được: chênh 4 phần tử trên CẢ BA miền.** `main.py:466` và `main.py:9462` — bỏ `gpt-5-mini`
(nay `SHADOW_AUTO`) + `combo-no-token` (nay `output_eligible=False`), thêm `glm-5.1` +
`gpt-oss-120b`. **Chênh 4 → 0.**
> **Số dòng trong sổ đã TRÔI.** Mục `FU-380` ghi `main.py:446-451` và `:9412-9417` từ 09/08 —
> ngày 21/08 **cả hai đều sai** (446 là `_parse_optional_datetime`, 9412 là docstring). Tìm lại
> **bằng nội dung** (`RM-10`). Ai đọc mục cũ rồi nhảy thẳng tới dòng sẽ **sửa nhầm chỗ**.
**Cổng mới `_v11093_kiem_fu380.py`** — dựng vì đây là nhánh **fail-closed**: nó sai **âm thầm**,
không lỗi không cảnh báo, chỉ lộ đúng lúc registry hỏng và không ai nhìn. Lần trôi trước mất
**12 ngày** mới thấy. Thử chặn `RM-15` **ĐẠT hai chiều**, `main.py` khôi phục **khớp từng byte**.
### `#12` — gỡ `latency_score`, và vì sao nó **không** phải việc dọn rác đơn giản
Mục này trong sổ có **đúng một dòng**, ô ghi chú **trống** — không một lý do nào trong toàn kho.
Phải tự đo lấy căn cứ:
`latency_score` = **0,5 ở CẢ 7.981 dòng** `du_doan_test_selected_voters`, đúng **một** giá trị

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

## V11093 — LÀN 1 GÓI 21/08: `FU-380` vá roster fail-closed · mục #12 gỡ `latency_score`

**21/08/2026 sáng** · `QD-041` **hết hạn**, gói mở khoá · `QD-068` · **production chưa đổi**
(chưa deploy, không ghi DB) — LÀN 1 theo định nghĩa **không chạm đường sinh số**.

### `#11 FU-380` — hai danh sách cứng **fail-closed** trôi khỏi registry

Ngưỡng đăng ký trước (owner ký 00:33 09/08): *«so hai danh sách cứng với
`get_output_eligible_ids()`, chênh > 0 phần tử ⇒ vá»*. `FU-284` đã đóng 20/08 nên rào đã hết.

**Đo được: chênh 4 phần tử trên CẢ BA miền.** `main.py:466` và `main.py:9462` — bỏ `gpt-5-mini`
(nay `SHADOW_AUTO`) + `combo-no-token` (nay `output_eligible=False`), thêm `glm-5.1` +
`gpt-oss-120b`. **Chênh 4 → 0.**

> **Số dòng trong sổ đã TRÔI.** Mục `FU-380` ghi `main.py:446-451` và `:9412-9417` từ 09/08 —
> ngày 21/08 **cả hai đều sai** (446 là `_parse_optional_datetime`, 9412 là docstring). Tìm lại
> **bằng nội dung** (`RM-10`). Ai đọc mục cũ rồi nhảy thẳng tới dòng sẽ **sửa nhầm chỗ**.

**Cổng mới `_v11093_kiem_fu380.py`** — dựng vì đây là nhánh **fail-closed**: nó sai **âm thầm**,
không lỗi không cảnh báo, chỉ lộ đúng lúc registry hỏng và không ai nhìn. Lần trôi trước mất
**12 ngày** mới thấy. Thử chặn `RM-15` **ĐẠT hai chiều**, `main.py` khôi phục **khớp từng byte**.

### `#12` — gỡ `latency_score`, và vì sao nó **không** phải việc dọn rác đơn giản

Mục này trong sổ có **đúng một dòng**, ô ghi chú **trống** — không một lý do nào trong toàn kho.
Phải tự đo lấy căn cứ:

`latency_score` = **0,5 ở CẢ 7.981 dòng** `du_doan_test_selected_voters`, đúng **một** giá trị
duy nhất suốt đời bảng (05/05 → 21/08). Gốc: nguồn `model_latency_cost_audit_daily` **chết từ
06/05** (107 ngày) và `latency_available=1` đếm được **0/4.033** — **chưa bao giờ** có một dòng
dùng được.

> **Cái bẫy:** gỡ thẳng số hạng chết **vẫn không trung tính**. Điểm đi qua `final *= 0.55` khi
> model chưa đo được ⇒ bỏ hằng số thì nhóm **đo được** mất `0,05` còn nhóm **chưa đo** chỉ mất
> `0,0275` ⇒ hình phạt `0,55` bị **chỉnh lại NGẦM**. Đo được: **1.115/109.426 cặp đảo chiều**,
> **100%** là cặp *(đo được × chưa đo)*, và **930 cặp CHẠM `SELECTED_VOTER`**.
> Tức gỡ thẳng là **đổi hành vi lane test ở 930 chỗ** trong khi báo cáo ghi *«gỡ một chỉ số chết»*.

**Lối đã chọn — giữ nguyên số học:** bỏ hàm (75 dòng) + nguồn chết + cột, **giữ** hằng số dưới
tên `DI_SAN_LATENCY = 0.05` **hiện nguyên hình kèm lý do**. Kiểm: công thức mới tái lập điểm cũ
**7.981/7.981, lệch 0** ⇒ **0 cặp đảo, 0 model đổi vai**. Việc chỉnh hình phạt tách thành
`FU-412` **trình owner** — `QD-018` *«một biến một lần»*.

### Bốn mục theo dõi mới — đều là **phát hiện**, không tự vá (`QD-064`)

| | |
|---|---|
| `FU-412` | hình phạt `×0,55` **nhạy với điểm gốc tuỳ ý** của thang chấm — ba lối cho owner chọn |
| `FU-413` | hai bản sao roster ngoài phạm vi; nặng nhất là `_v10759_money_board.py:35` mang chú thích **tự khai** *«registry 15/15 khớp fallback»* — **câu đó nay SAI** |
| `FU-414` | `model_latency_cost_audit_daily` chết **107 ngày** nhưng còn **hai điểm đọc SỐNG** trong `main.py` (`:11917 :14916`) — **vế ngược** của `RM-20` |
| `FU-415` | hook cổng `git commit` dùng **đường dẫn tương đối** ⇒ sau một lệnh `cd` vào thư mục con thì **mọi** lệnh Bash bị chặn cứng, kể cả chính lệnh `cd` quay về |

## 4. Hướng xử lý và vì sao chọn

Lý do chọn nằm trong chính khối `CHANGELOG` ở mục 3 — đó là bản ghi viết **lúc làm việc**,
không phải suy lại. Phần **cân nhắc phương án bị loại** thì 🔴 **KHÔNG KHÔI PHỤC ĐƯỢC**: nó chỉ
tồn tại trong vết phiên và không được ghi vào tài liệu nào lúc đó.

## 5. Đã làm gì

| commit | ngày (giờ VN) | tệp | tổng |
|---|---|---|---|
| `143a95e` | 2026-08-21 09:25:07 | CHANGELOG.md, docs/AUTOMATION_HISTORY.jsonl, docs/AUTOMATION_STATE.json, docs/BAN_DO_THUC_THI_2108.md, docs/CURRENT_TRUTH_SSOT.md, docs/_I2_DA_CHAY.js | 6 files changed, 119 insertions(+), 11 deletions(-) |
| `e3ebc19` | 2026-08-21 09:23:16 | docs/FOLLOW_UP_TRACKER.md, .../_materialize_du_doan_test_model_budget.py | 2 files changed, 79 insertions(+), 84 deletions(-) |
| `3cea289` | 2026-08-21 09:08:51 | docs/FOLLOW_UP_TRACKER.md, web/backend/_v11093_kiem_fu380.py, web/backend/main.py | 3 files changed, 154 insertions(+), 8 deletions(-) |

## 6. Cổng kiểm

🔴 **KHÔNG KHÔI PHỤC ĐƯỢC output cổng của phiên gốc** — cổng in ra `stdout`, không ghi tệp
(đúng khuyết tật `RM-15` mà `V11121` đã vá cho `cong_git_commit.py` bằng sổ điểm danh).

Điều **kiểm được hôm nay**, `26/08/2026`:

| phép | kết quả |
|---|---|
| commit của bản này còn trong `git log` | ✅ **3/3** còn nguyên, đều là tổ tiên của `origin/master` |
| khối `CHANGELOG` còn nguyên | ✅ 3,290 ký tự |
| bản này đã có báo cáo công khai chưa | ✅ **có, từ bản bù này** — trước đó `A55_VIOLATION_REPORT_MISSING` |

## 7. Vướng vấp

🔴 **KHÔNG KHÔI PHỤC ĐƯỢC** vướng vấp trong phiên gốc — không tài liệu nào ghi lại lúc đó.

Vướng vấp **của chính việc bù này**, ghi trung thực: bản bù dựng từ ba nguồn đương thời nhưng
**không thay được** một báo cáo viết lúc làm việc. Cụ thể mất: giờ từng thao tác · các phương án
đã cân nhắc rồi loại · lỗi gặp giữa chừng · trạng thái trước/sau của DB nếu phiên có chạm.

## 8. Gỡ về

Bản bù này **chỉ thêm tài liệu**, không đụng mã và không đụng dữ liệu ⇒ gỡ về =
`git rm -r V11093_LAN_1_GOI_2108_FU380_ROSTER_FAIL_CLOSED_20260821/` rồi commit lại. Trạng thái quay về đúng như trước khi bù.

Việc gỡ về của **bản gốc `V11093`** nằm trong chính khối `CHANGELOG` ở mục 3 (nếu bản đó có ghi).

## 9. Theo dõi tiếp

| mã | việc | trạng thái |
|---|---|---|
| `FU-442` | vá cổng A55 — chính lỗ hổng làm bản này vô hình | ✅ **ĐÃ VÁ** ở `V11122`, thử chặn **11/11** |
| — | bù nốt các bản còn thiếu | trên **toàn dải từ mốc thi hành `V10921`** còn **32** bản thiếu báo cáo; 10 bản của đợt này là nhóm ưu tiên |
| — | ngưỡng đóng bằng số | `_v10921_report_gate.py` chạy **không tham số** ⇒ `V11093` không còn trong danh sách `THIẾU BÁO CÁO` |

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
| 3 commit mang nhãn `V11093` | `143a95e`, `e3ebc19`, `3cea289` — còn nguyên trong `git log`, đều là tổ tiên `origin/master` |
| tệp bị đụng | xem bảng mục 5 |
| bản này **chưa từng** có báo cáo công khai cho tới hôm nay | `_v10921_report_gate.py` liệt `V11093` trong `THIẾU BÁO CÁO` trước khi bù |

### `DOC_SAID`
| tài liệu | nói gì | khớp code chưa |
|---|---|---|
| `CHANGELOG.md` khối `## V11093` | 3,290 ký tự, viết đương thời | 🟢 **khớp** — commit tồn tại đúng ngày ghi |
| kho báo cáo công khai | **không có** thư mục `V11093_*` | 🔴 **LỆCH** — đã đóng bằng bản bù này |

### 🔴 BA LỚP LỆCH NHAU
`DOC_SAID` ≠ `CODE_DID`: mã đã chạy và đã commit, `CHANGELOG` đã ghi, nhưng **kho công khai không
có gì** suốt 5 ngày. Đó là `A55_VIOLATION_REPORT_MISSING`, và nó **vô hình** vì cổng chỉ soi 8
bản gần nhất — nay đã vá (`FU-442` · `V11122`).

---

**TanPhatAI cần làm:** ghi nhận đây là **báo cáo BÙ** viết ngày 26/08/2026 cho việc làm ngày
21/08, dựng từ **ba nguồn đương thời** (CHANGELOG 3,290 ký tự ·
3 commit · vết phiên), **không** phải bản viết lúc làm việc — mọi chỗ không khôi phục
được đã ghi thẳng là `KHÔNG KHÔI PHỤC ĐƯỢC`, **không** điền số ước.
