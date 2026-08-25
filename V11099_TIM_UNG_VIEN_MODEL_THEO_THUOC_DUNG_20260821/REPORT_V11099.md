# V11099 — TÌM ỨNG VIÊN MODEL THEO THƯỚC ĐÚNG · và một lỗi thật trong prompt

**Ngày làm việc:** 21/08/2026 ·
**Ngày viết báo cáo này:** 26/08/2026 · **Commit riêng:** `38ab002`, `51e769e` ·
**Trạng thái:** `BÙ TỪ NGUỒN GỐC`

---

> ## ⚠️ ĐÂY LÀ BÁO CÁO **BÙ**, KHÔNG PHẢI BẢN VIẾT LÚC LÀM VIỆC
>
> Bản `V11099` làm ngày **21/08** nhưng **không có** thư mục báo cáo công khai —
> vi phạm `§57.2` đã tồn tại **5 ngày**.
> Cổng A55 cũ **không thấy** vì nó chỉ soi **8 bản gần nhất** (đã vá ở `V11122`, `FU-442`).
>
> **Ba nguồn dựng nên bản này — cả ba đều là bản ghi ĐƯƠNG THỜI:**
>
> | nguồn | quy mô |
> |---|---|
> | khối `## V11099` trong `CHANGELOG.md` — viết **ngay lúc làm việc** | **4,459 ký tự / 92 dòng** |
> | commit git mang nhãn `V11099` | **2** commit |
> | lượt owner trong vết phiên `.jsonl` cùng ngày | **có** |
> | khối phụ (`V11099b`/`c`/…) | — |
>
> 🔴 **PHẦN KHÔNG KHÔI PHỤC ĐƯỢC** — ghi thẳng, không suy:
> · **giờ chính xác** từng thao tác trong phiên · **vướng vấp giữa chừng** không được ghi lại lúc đó
> · **hash 4 bảng khoá trước/sau** (nếu phiên có chạm DB) · **PID trước/sau** (nếu có restart).
> Những chỗ đó dưới đây đều ghi `KHÔNG KHÔI PHỤC ĐƯỢC`, **không** điền số ước.

---

## 1. Tóm tắt

**21/08/2026 tối muộn** · **Read-only** — không cắt model nào, không đổi mã, không dừng cron.
### Owner chỉnh khung — và agent nghĩ sai hai chỗ
> *«Chi phí ở đây không phải là model đắt tiền đong đếm bằng tiền… Đắt phải chất, ít nhưng hiệu
> quả đông loãng nhiều thì không nên. Shadow là thử nghiệm để so sánh và tìm ra model phù hợp để
> thay thế… **nó chưa tham gia output là đúng mà em**, em phải làm việc này so sánh tìm ra ứng
> viên sáng giá chứ em.»*
| agent đã viết | thật ra |
|---|---|
| *«33 lượt/ngày chảy vào chỗ không dùng được»* | **shadow không tham gia output là ĐÚNG THIẾT KẾ** — việc phải làm là **dùng nó**, không phải cắt |
| đo *«chi phí»* bằng **tiền** | chi phí là **sự LOÃNG** — nhiều model mà không đo được sức mạnh từng cái thì đông cũng vô nghĩa |
### Đo SỰ LOÃNG — 90 ngày, 273 lượt
| nhóm | model/lượt | số khác nhau TB | **đa dạng / mỗi model** |
|---|---|---|---|
| **AI** *(đọc prompt)* | **19** | 6,7 | **0,35** |
| **ML** *(KHÔNG đọc prompt)* | 8 | 4,8 | **0,60** |
**42,1% model cùng chọn MỘT số. 19 model AI chỉ cho ra 6,7 ý kiến.**
ML — nhóm không đọc prompt — cho **đa dạng trên mỗi model cao gần gấp đôi**.
### Thước ĐÚNG để tìm ứng viên

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

## V11099 — TÌM ỨNG VIÊN MODEL THEO THƯỚC ĐÚNG · và một lỗi thật trong prompt

**21/08/2026 tối muộn** · **Read-only** — không cắt model nào, không đổi mã, không dừng cron.

### Owner chỉnh khung — và agent nghĩ sai hai chỗ

> *«Chi phí ở đây không phải là model đắt tiền đong đếm bằng tiền… Đắt phải chất, ít nhưng hiệu
> quả đông loãng nhiều thì không nên. Shadow là thử nghiệm để so sánh và tìm ra model phù hợp để
> thay thế… **nó chưa tham gia output là đúng mà em**, em phải làm việc này so sánh tìm ra ứng
> viên sáng giá chứ em.»*

| agent đã viết | thật ra |
|---|---|
| *«33 lượt/ngày chảy vào chỗ không dùng được»* | **shadow không tham gia output là ĐÚNG THIẾT KẾ** — việc phải làm là **dùng nó**, không phải cắt |
| đo *«chi phí»* bằng **tiền** | chi phí là **sự LOÃNG** — nhiều model mà không đo được sức mạnh từng cái thì đông cũng vô nghĩa |

### Đo SỰ LOÃNG — 90 ngày, 273 lượt

| nhóm | model/lượt | số khác nhau TB | **đa dạng / mỗi model** |
|---|---|---|---|
| **AI** *(đọc prompt)* | **19** | 6,7 | **0,35** |
| **ML** *(KHÔNG đọc prompt)* | 8 | 4,8 | **0,60** |

**42,1% model cùng chọn MỘT số. 19 model AI chỉ cho ra 6,7 ý kiến.**
ML — nhóm không đọc prompt — cho **đa dạng trên mỗi model cao gần gấp đôi**.

### Thước ĐÚNG để tìm ứng viên

Không phải tỉ lệ trúng thô: model trúng cao **nhưng luôn chọn giống model khác** thì **thêm nó
không được gì**. Thước đúng:

> **GIÁ TRỊ THÊM = tỉ lệ trúng TRONG NHỮNG LƯỢT NÓ ĐI RIÊNG.**

| # | model | nhóm | lượt đi riêng | giá trị thêm | CI95 |
|---|---|---|---|---|---|
| 1 | `glm-5.1` | OUTPUT | 133 | **43,6%** | [35,2 … 52,0] |
| **2** | **`gemini-3.5-flash`** | **shadow** | 63 | **42,9%** | [30,6 … 55,1] |
| 5 | `qwen3.7-max` | shadow | 80 | 41,2% | [30,5 … 52,0] |
| **13** | **`claude-sonnet-4-6`** | **OUTPUT** | 159 | **32,7%** | [25,4 … 40,0] |
| 15 | `gpt-5-mini` | shadow | 172 | **26,7%** | [20,1 … 33,4] |

**`gemini-3.5-flash` vs `claude-sonnet-4-6`: +10,2pp · CI95 [−4,1 … +24,4] · z=+1,40**
⇒ **CHƯA ĐƯỢC PHÉP KẾT LUẬN.** Không đề xuất thay ngay — `n=63` quá ít, và dự án đã ngã
**sáu lần** vì bật rồi rữa.

> **Cần 3,0 tháng nữa** để chứng minh chênh 10pp. **Và đây là chỗ hai ý của owner nối vào nhau:**
> phép so **chỉ đo được trên lượt model ĐI RIÊNG**, mà model chỉ đi riêng ~48% vì chúng hội tụ.
> ⇒ **model càng giống nhau ⇒ càng ít dữ liệu để so ⇒ càng lâu mới tìm ra ứng viên.**
> Cái làm model *«không hoạt động đúng nghĩa»* **cũng chính là** cái làm mình không tìm được
> model tốt hơn.

### Chất lượng prompt — agent đếm SAI HAI LẦN, rồi tìm ra lỗi thật

| lần | kết quả | sai ở đâu |
|---|---|---|
| 1 | *«40–45/100 số»* | tính cả **%** và **số đếm** (`54.8`, `17/31`) |
| 2 | *«3–10/100 số»* | loại **nhầm cả rổ số thật** — dòng rổ cũng chứa `0/2` |
| 3 | **đúng** — mẫu riêng từng khối | |

**Đếm đúng:** MN sự-kiện 25 · **rổ chọn 5** · MT 20 · **4** · MB 16 · **4**.

**TIN TỐT: prompt ĐÃ ĐƯỢC DỌN.** Khối `BỐI CẢNH SOI CẦU` ghi thẳng *«kể lại sự kiện — KHÔNG có
danh sách số chốt sẵn»* … *«Bạn tự rút số»*, và `MINED RULES` ghi *«không lặp lại danh sách ở
đây»*. Việc owner nêu **đã được làm một phần** (V11016). Rổ còn lại chỉ **4–5 số**.

### 🔴 `FU-419` — khối `D-1 tail pool` chỉ hiện SỐ NHỎ, mọi ngày

`gpt_analyzer.py:6020` — `', '.join(sorted(d1_union)[:12])`: **sắp tăng dần rồi cắt 12**.

| | |
|---|---|
| đuôi thật sự ra mỗi ngày | **~71/100** |
| khối hiển thị | **12** ⇒ cắt **83%**, luôn về phía **nhỏ nhất** |
| **31 ngày liên tiếp** | chỉ từng hiện **`00`–`21`** — **22 đuôi** |
| **đuôi CHƯA BAO GIỜ xuất hiện** | **78/100** |
| ba miền | nhận **y hệt** `01, 02, 03, …, 13` |

Khối **tự giới thiệu là ngữ cảnh chéo miền** nhưng ① gần như **không mang tin** · ② **thiên vị
có hệ thống về số nhỏ** cho mọi model mọi ngày · ③ **chiếm chỗ** của ngữ cảnh thật.

**Khác với «rổ số chốt sẵn» — và tệ hơn:** rổ chốt sẵn còn có nội dung; khối này là **một cửa sổ
CỐ ĐỊNH ở đầu dãy số**.

### Bốn đề xuất

**①** bỏ hoặc đổi `D-1 tail pool` thành **«đuôi KHÔNG ra»** *(ít hơn và mang tin hơn)* ·
**②** dựng **bảng ứng viên thường trực** + **ngưỡng cất nhắc đăng ký trước** ⇒ biến lane shadow
từ *«chạy cho có»* thành *«đang tuyển người»* · **③** dừng `gpt-5-mini` (26,7% — thấp nhất bảng)
· `qwen3-max-thinking` · `gpt-5.5` — **theo tiêu chí không đóng góp ý kiến khác biệt, không theo
tiền** · **④** `claude-sonnet-4-6` đang ở **đáy bảng OUTPUT**, thấp hơn **7 model shadow** —
chưa thay, nhưng có thể **đo cặp trực tiếp** để rút ngắn 3 tháng chờ.

## 4. Hướng xử lý và vì sao chọn

Lý do chọn nằm trong chính khối `CHANGELOG` ở mục 3 — đó là bản ghi viết **lúc làm việc**,
không phải suy lại. Phần **cân nhắc phương án bị loại** thì 🔴 **KHÔNG KHÔI PHỤC ĐƯỢC**: nó chỉ
tồn tại trong vết phiên và không được ghi vào tài liệu nào lúc đó.

## 5. Đã làm gì

| commit | ngày (giờ VN) | tệp | tổng |
|---|---|---|---|
| `38ab002` | 2026-08-21 21:33:33 | CHANGELOG.md, docs/AUTOMATION_HISTORY.jsonl, docs/AUTOMATION_STATE.json, docs/CURRENT_TRUTH_SSOT.md, docs/FOLLOW_UP_TRACKER.md, ...UNG_VIEN_MODEL_VA_C | 7 files changed, 354 insertions(+), 4 deletions(-) |
| `51e769e` | 2026-08-21 21:17:30 | docs/CAT_GIAM_MODEL_VA_TON_DONG_20260821.md, docs/FOLLOW_UP_TRACKER.md | 2 files changed, 263 insertions(+), 1 deletion(-) |

## 6. Cổng kiểm

🔴 **KHÔNG KHÔI PHỤC ĐƯỢC output cổng của phiên gốc** — cổng in ra `stdout`, không ghi tệp
(đúng khuyết tật `RM-15` mà `V11121` đã vá cho `cong_git_commit.py` bằng sổ điểm danh).

Điều **kiểm được hôm nay**, `26/08/2026`:

| phép | kết quả |
|---|---|
| commit của bản này còn trong `git log` | ✅ **2/2** còn nguyên, đều là tổ tiên của `origin/master` |
| khối `CHANGELOG` còn nguyên | ✅ 4,459 ký tự |
| bản này đã có báo cáo công khai chưa | ✅ **có, từ bản bù này** — trước đó `A55_VIOLATION_REPORT_MISSING` |

## 7. Vướng vấp

🔴 **KHÔNG KHÔI PHỤC ĐƯỢC** vướng vấp trong phiên gốc — không tài liệu nào ghi lại lúc đó.

Vướng vấp **của chính việc bù này**, ghi trung thực: bản bù dựng từ ba nguồn đương thời nhưng
**không thay được** một báo cáo viết lúc làm việc. Cụ thể mất: giờ từng thao tác · các phương án
đã cân nhắc rồi loại · lỗi gặp giữa chừng · trạng thái trước/sau của DB nếu phiên có chạm.

## 8. Gỡ về

Bản bù này **chỉ thêm tài liệu**, không đụng mã và không đụng dữ liệu ⇒ gỡ về =
`git rm -r V11099_TIM_UNG_VIEN_MODEL_THEO_THUOC_DUNG_20260821/` rồi commit lại. Trạng thái quay về đúng như trước khi bù.

Việc gỡ về của **bản gốc `V11099`** nằm trong chính khối `CHANGELOG` ở mục 3 (nếu bản đó có ghi).

## 9. Theo dõi tiếp

| mã | việc | trạng thái |
|---|---|---|
| `FU-442` | vá cổng A55 — chính lỗ hổng làm bản này vô hình | ✅ **ĐÃ VÁ** ở `V11122`, thử chặn **11/11** |
| — | bù nốt các bản còn thiếu | trên **toàn dải từ mốc thi hành `V10921`** còn **32** bản thiếu báo cáo; 10 bản của đợt này là nhóm ưu tiên |
| — | ngưỡng đóng bằng số | `_v10921_report_gate.py` chạy **không tham số** ⇒ `V11099` không còn trong danh sách `THIẾU BÁO CÁO` |

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
| 2 commit mang nhãn `V11099` | `38ab002`, `51e769e` — còn nguyên trong `git log`, đều là tổ tiên `origin/master` |
| tệp bị đụng | xem bảng mục 5 |
| bản này **chưa từng** có báo cáo công khai cho tới hôm nay | `_v10921_report_gate.py` liệt `V11099` trong `THIẾU BÁO CÁO` trước khi bù |

### `DOC_SAID`
| tài liệu | nói gì | khớp code chưa |
|---|---|---|
| `CHANGELOG.md` khối `## V11099` | 4,459 ký tự, viết đương thời | 🟢 **khớp** — commit tồn tại đúng ngày ghi |
| kho báo cáo công khai | **không có** thư mục `V11099_*` | 🔴 **LỆCH** — đã đóng bằng bản bù này |

### 🔴 BA LỚP LỆCH NHAU
`DOC_SAID` ≠ `CODE_DID`: mã đã chạy và đã commit, `CHANGELOG` đã ghi, nhưng **kho công khai không
có gì** suốt 5 ngày. Đó là `A55_VIOLATION_REPORT_MISSING`, và nó **vô hình** vì cổng chỉ soi 8
bản gần nhất — nay đã vá (`FU-442` · `V11122`).

---

**TanPhatAI cần làm:** ghi nhận đây là **báo cáo BÙ** viết ngày 26/08/2026 cho việc làm ngày
21/08, dựng từ **ba nguồn đương thời** (CHANGELOG 4,459 ký tự ·
2 commit · vết phiên), **không** phải bản viết lúc làm việc — mọi chỗ không khôi phục
được đã ghi thẳng là `KHÔNG KHÔI PHỤC ĐƯỢC`, **không** điền số ước.
