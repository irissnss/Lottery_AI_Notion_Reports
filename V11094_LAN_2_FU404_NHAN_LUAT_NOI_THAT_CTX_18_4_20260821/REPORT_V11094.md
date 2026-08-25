# V11094 — LÀN 2 mục 1: `FU-404` nhãn luật NÓI THẬT · `CTX-18.3` → `CTX-18.4`

**Ngày làm việc:** 21/08/2026 ·
**Ngày viết báo cáo này:** 26/08/2026 · **Commit riêng:** `676e34b`, `709efaf`, `fd19d95`, `d0b20f6`, `74f3c37`, `b5d9367` ·
**Trạng thái:** `BÙ TỪ NGUỒN GỐC`

---

> ## ⚠️ ĐÂY LÀ BÁO CÁO **BÙ**, KHÔNG PHẢI BẢN VIẾT LÚC LÀM VIỆC
>
> Bản `V11094` làm ngày **21/08** nhưng **không có** thư mục báo cáo công khai —
> vi phạm `§57.2` đã tồn tại **5 ngày**.
> Cổng A55 cũ **không thấy** vì nó chỉ soi **8 bản gần nhất** (đã vá ở `V11122`, `FU-442`).
>
> **Ba nguồn dựng nên bản này — cả ba đều là bản ghi ĐƯƠNG THỜI:**
>
> | nguồn | quy mô |
> |---|---|
> | khối `## V11094` trong `CHANGELOG.md` — viết **ngay lúc làm việc** | **3,577 ký tự / 65 dòng** |
> | commit git mang nhãn `V11094` | **6** commit |
> | lượt owner trong vết phiên `.jsonl` cùng ngày | **có** |
> | khối phụ (`V11094b`/`c`/…) | — |
>
> 🔴 **PHẦN KHÔNG KHÔI PHỤC ĐƯỢC** — ghi thẳng, không suy:
> · **giờ chính xác** từng thao tác trong phiên · **vướng vấp giữa chừng** không được ghi lại lúc đó
> · **hash 4 bảng khoá trước/sau** (nếu phiên có chạm DB) · **PID trước/sau** (nếu có restart).
> Những chỗ đó dưới đây đều ghi `KHÔNG KHÔI PHỤC ĐƯỢC`, **không** điền số ước.

---

## 1. Tóm tắt

**21/08/2026** · `QD-041` hết hạn · `QD-068` · **chưa deploy** — mã đã sửa, prompt đã dump kiểm.
### Cổng đóng băng `QD-041` lệch MỘT NGÀY — sửa trước khi làm gì khác
`_v11028_cong_dong_bang.py` so `hôm_nay > KẾT_THÚC` với `KẾT_THÚC = 21/08` ⇒ **ngày 21/08 vẫn
bị khoá**. Nhưng `QD-064` ghi *«gói mở khoá 21/08»*, `FU-380` ghi ngưỡng *«21/08 ⇒ vá»*, và
bảng kiểm là bảng kiểm **của chính ngày 21/08**. Cổng khoá đúng cái ngày mọi văn bản khác coi
là ngày làm việc — **lệch một ngày**, không phải chủ ý (chủ ý thì `KẾT_THÚC` đã là 22/08).
Đổi thành `>=`: cửa sổ phủ **08/08 → 20/08**. **Không nới `KẾT_THÚC`** — muốn đóng băng tiếp
phải có chữ ký MỚI và `BẢN_KHOÁ` mới.
### `FU-404` — và hai chỗ mục ấy ghi SAI ĐƯỜNG
**① Chuỗi mục trích dẫn không thuộc production.** Mục ghi *«`CTX-18.3` CÓ khối `[V2-RULES]`»*
và trích *«`HR12W 1.0` (n=20)»*. Nhưng `[V2-RULES]` ở `_v10781_context_pack_v2.py`, mà **chính
tệp đó tự khai dòng 26**: *«Chỉ `_v10781_prompt_v2_lane.py` (cron riêng) dùng nó»* — **lane A/B**.
`CTX-18.3` thật ở `gpt_analyzer.py:844`. **Dump production: chuỗi `HR12W` xuất hiện 0 lần** ở
cả ba miền (`RM-13` · `RM-14`).
**② Vế «trạng thái ngoài mẫu» ĐÃ CÓ SẴN** từ trước tại `gpt_analyzer.py:4805`.
⇒ phần còn thiếu **không phải** trạng thái ngoài mẫu, mà là **lợi thế trên nền**.
### Lõi vấn đề — nhãn không chỉ nói quá, nó nói NGƯỢC
| luật (đo 21/08) | prompt hiển thị | sự thật cùng dòng |

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

## V11094 — LÀN 2 mục 1: `FU-404` nhãn luật NÓI THẬT · `CTX-18.3` → `CTX-18.4`

**21/08/2026** · `QD-041` hết hạn · `QD-068` · **chưa deploy** — mã đã sửa, prompt đã dump kiểm.

### Cổng đóng băng `QD-041` lệch MỘT NGÀY — sửa trước khi làm gì khác

`_v11028_cong_dong_bang.py` so `hôm_nay > KẾT_THÚC` với `KẾT_THÚC = 21/08` ⇒ **ngày 21/08 vẫn
bị khoá**. Nhưng `QD-064` ghi *«gói mở khoá 21/08»*, `FU-380` ghi ngưỡng *«21/08 ⇒ vá»*, và
bảng kiểm là bảng kiểm **của chính ngày 21/08**. Cổng khoá đúng cái ngày mọi văn bản khác coi
là ngày làm việc — **lệch một ngày**, không phải chủ ý (chủ ý thì `KẾT_THÚC` đã là 22/08).
Đổi thành `>=`: cửa sổ phủ **08/08 → 20/08**. **Không nới `KẾT_THÚC`** — muốn đóng băng tiếp
phải có chữ ký MỚI và `BẢN_KHOÁ` mới.

### `FU-404` — và hai chỗ mục ấy ghi SAI ĐƯỜNG

**① Chuỗi mục trích dẫn không thuộc production.** Mục ghi *«`CTX-18.3` CÓ khối `[V2-RULES]`»*
và trích *«`HR12W 1.0` (n=20)»*. Nhưng `[V2-RULES]` ở `_v10781_context_pack_v2.py`, mà **chính
tệp đó tự khai dòng 26**: *«Chỉ `_v10781_prompt_v2_lane.py` (cron riêng) dùng nó»* — **lane A/B**.
`CTX-18.3` thật ở `gpt_analyzer.py:844`. **Dump production: chuỗi `HR12W` xuất hiện 0 lần** ở
cả ba miền (`RM-13` · `RM-14`).

**② Vế «trạng thái ngoài mẫu» ĐÃ CÓ SẴN** từ trước tại `gpt_analyzer.py:4805`.
⇒ phần còn thiếu **không phải** trạng thái ngoài mẫu, mà là **lợi thế trên nền**.

### Lõi vấn đề — nhãn không chỉ nói quá, nó nói NGƯỢC

| luật (đo 21/08) | prompt hiển thị | sự thật cùng dòng |
|---|---|---|
| `MN/Hà Nội G6+G7` | `HR12W = 1.0` | `lift_365 = 0,9612` ⇒ **−3,88%, KÉM NỀN** |
| `MN/Nam Định G1+G7` | `HR12W = 1.0` | ⇒ **−1,62%, KÉM NỀN** |

**13/105 luật có `lift ≤ 1,0`.** Và `1.0` gần **mức sàn** chứ không phải đỉnh: `HR12W` đếm
*«tuần đó có ÍT NHẤT MỘT trong 3–4 số trúng»* ⇒ **105/105 luật đạt ≥ 40%**, trung bình `0,8675`.

### Đã sửa

Thêm `lift_365` vào **cả hai** truy vấn (`READY_STRONG` · `FALLBACK`) — hai truy vấn đó **vốn đã
lấy `hit_rate_365, n_365` rồi vứt đi**. Mỗi dòng luật nay kết bằng `| lợi thế +X%/nền (n=…)`,
kèm `⚠mẫu mỏng` khi `n<30` và **`⛔KÉM NỀN`** khi `lift ≤ 1`. Thêm câu **CÁCH ĐỌC HR**.

**KHÔNG bỏ `HR12W/16W/4W`** — mệnh lệnh `ORDER OF OPERATIONS: first determine the current
12W-16W source-prize law` còn trỏ vào chúng. Bỏ số mà giữ mệnh lệnh = `PRJ_PROMPT_DANGLING`.

**Kiểm (dump từ `build_context_pack`, `PYTHONHASHSEED=0` để khử nhiễu):** diff sạch
**MN 3 · MT 3 · MB 7 dòng** — đúng bằng dòng luật × 2 + câu ghi chú, **không một dòng thừa**.
Quét bốn thứ: mệnh lệnh mồ côi **0** · few-shot **0** · nhãn mồ côi **không gỡ gì** · mâu thuẫn
**không có câu nào bảo model TIN `HR`**.

### `FU-416` — phát hiện lớn nhất phiên, sinh ra từ MỘT DÒNG DIFF KHÔNG GIẢI THÍCH ĐƯỢC

So TRƯỚC/SAU thấy một dòng đổi mà bản vá **không đụng tới**. Kiểm thay vì cho qua:

| phép | MN | MT | MB |
|---|---|---|---|
| hai lần chạy **cùng mã** | **6 dòng khác** | **6 dòng khác** | **2 dòng khác** |
| đặt `PYTHONHASHSEED=0` | **0** | **0** | **0** |

⇒ **prompt production đổi nội dung theo hạt băm chuỗi của từng tiến trình Python.**
Đích danh `gpt_analyzer.py:5941`: `sorted(candidate_tails.items(), key=lambda x: -x[1])[:10]` —
**không phá hoà bằng khoá**, rồi `[:10]` và `[:6]` **cắt**.
Đo 21/08: **MT** 2/3 đuôi hoà tại `0,1207` **đúng hai vị trí đầu** · **MB** 5/6 đuôi trong nhóm
hoà gồm cả top-2 ⇒ **số model nhìn thấy TRƯỚC TIÊN là do hạt băm quyết**.
Mọi phép đo prompt A/B trong dự án đang có nhiễu này **chồng lên tín hiệu mà chưa ai trừ ra**.
Vá đề nghị **một dòng**: `key=lambda x: (-x[1], x[0])`. **Không làm hôm nay** — `QD-018`.

## 4. Hướng xử lý và vì sao chọn

Lý do chọn nằm trong chính khối `CHANGELOG` ở mục 3 — đó là bản ghi viết **lúc làm việc**,
không phải suy lại. Phần **cân nhắc phương án bị loại** thì 🔴 **KHÔNG KHÔI PHỤC ĐƯỢC**: nó chỉ
tồn tại trong vết phiên và không được ghi vào tài liệu nào lúc đó.

## 5. Đã làm gì

| commit | ngày (giờ VN) | tệp | tổng |
|---|---|---|---|
| `676e34b` | 2026-08-21 19:23:38 | CHANGELOG.md, docs/AUTOMATION_HISTORY.jsonl, docs/AUTOMATION_STATE.json, docs/CURRENT_TRUTH_SSOT.md, docs/_I2_DA_CHAY.json, web/backend/_v11096_kiem_m | 7 files changed, 262 insertions(+), 7 deletions(-) |
| `709efaf` | 2026-08-21 10:01:26 | docs/FOLLOW_UP_TRACKER.md, docs/FU290A_THIET_KE_CAT_MODEL.md, web/backend/_v10958_fu_reader.py | 3 files changed, 225 insertions(+), 3 deletions(-) |
| `fd19d95` | 2026-08-21 09:53:17 | docs/FOLLOW_UP_TRACKER.md | 1 file changed, 56 insertions(+), 1 deletion(-) |
| `d0b20f6` | 2026-08-21 09:47:36 | docs/FOLLOW_UP_TRACKER.md, web/backend/rule_engine.py | 2 files changed, 56 insertions(+), 8 deletions(-) |
| `74f3c37` | 2026-08-21 09:42:01 | CHANGELOG.md, docs/AUTOMATION_HISTORY.jsonl, docs/AUTOMATION_STATE.json, docs/CURRENT_TRUTH_SSOT.md, docs/FOLLOW_UP_TRACKER.md, docs/_I2_DA_CHAY.json | 7 files changed, 178 insertions(+), 15 deletions(-) |
| `b5d9367` | 2026-08-21 09:40:47 | web/backend/_v11028_cong_dong_bang.py | 1 file changed, 22 insertions(+), 2 deletions(-) |

## 6. Cổng kiểm

🔴 **KHÔNG KHÔI PHỤC ĐƯỢC output cổng của phiên gốc** — cổng in ra `stdout`, không ghi tệp
(đúng khuyết tật `RM-15` mà `V11121` đã vá cho `cong_git_commit.py` bằng sổ điểm danh).

Điều **kiểm được hôm nay**, `26/08/2026`:

| phép | kết quả |
|---|---|
| commit của bản này còn trong `git log` | ✅ **6/6** còn nguyên, đều là tổ tiên của `origin/master` |
| khối `CHANGELOG` còn nguyên | ✅ 3,577 ký tự |
| bản này đã có báo cáo công khai chưa | ✅ **có, từ bản bù này** — trước đó `A55_VIOLATION_REPORT_MISSING` |

## 7. Vướng vấp

🔴 **KHÔNG KHÔI PHỤC ĐƯỢC** vướng vấp trong phiên gốc — không tài liệu nào ghi lại lúc đó.

Vướng vấp **của chính việc bù này**, ghi trung thực: bản bù dựng từ ba nguồn đương thời nhưng
**không thay được** một báo cáo viết lúc làm việc. Cụ thể mất: giờ từng thao tác · các phương án
đã cân nhắc rồi loại · lỗi gặp giữa chừng · trạng thái trước/sau của DB nếu phiên có chạm.

## 8. Gỡ về

Bản bù này **chỉ thêm tài liệu**, không đụng mã và không đụng dữ liệu ⇒ gỡ về =
`git rm -r V11094_LAN_2_FU404_NHAN_LUAT_NOI_THAT_CTX_18_4_20260821/` rồi commit lại. Trạng thái quay về đúng như trước khi bù.

Việc gỡ về của **bản gốc `V11094`** nằm trong chính khối `CHANGELOG` ở mục 3 (nếu bản đó có ghi).

## 9. Theo dõi tiếp

| mã | việc | trạng thái |
|---|---|---|
| `FU-442` | vá cổng A55 — chính lỗ hổng làm bản này vô hình | ✅ **ĐÃ VÁ** ở `V11122`, thử chặn **11/11** |
| — | bù nốt các bản còn thiếu | trên **toàn dải từ mốc thi hành `V10921`** còn **32** bản thiếu báo cáo; 10 bản của đợt này là nhóm ưu tiên |
| — | ngưỡng đóng bằng số | `_v10921_report_gate.py` chạy **không tham số** ⇒ `V11094` không còn trong danh sách `THIẾU BÁO CÁO` |

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
| 6 commit mang nhãn `V11094` | `676e34b`, `709efaf`, `fd19d95`, `d0b20f6`, `74f3c37`, `b5d9367` — còn nguyên trong `git log`, đều là tổ tiên `origin/master` |
| tệp bị đụng | xem bảng mục 5 |
| bản này **chưa từng** có báo cáo công khai cho tới hôm nay | `_v10921_report_gate.py` liệt `V11094` trong `THIẾU BÁO CÁO` trước khi bù |

### `DOC_SAID`
| tài liệu | nói gì | khớp code chưa |
|---|---|---|
| `CHANGELOG.md` khối `## V11094` | 3,577 ký tự, viết đương thời | 🟢 **khớp** — commit tồn tại đúng ngày ghi |
| kho báo cáo công khai | **không có** thư mục `V11094_*` | 🔴 **LỆCH** — đã đóng bằng bản bù này |

### 🔴 BA LỚP LỆCH NHAU
`DOC_SAID` ≠ `CODE_DID`: mã đã chạy và đã commit, `CHANGELOG` đã ghi, nhưng **kho công khai không
có gì** suốt 5 ngày. Đó là `A55_VIOLATION_REPORT_MISSING`, và nó **vô hình** vì cổng chỉ soi 8
bản gần nhất — nay đã vá (`FU-442` · `V11122`).

---

**TanPhatAI cần làm:** ghi nhận đây là **báo cáo BÙ** viết ngày 26/08/2026 cho việc làm ngày
21/08, dựng từ **ba nguồn đương thời** (CHANGELOG 3,577 ký tự ·
6 commit · vết phiên), **không** phải bản viết lúc làm việc — mọi chỗ không khôi phục
được đã ghi thẳng là `KHÔNG KHÔI PHỤC ĐƯỢC`, **không** điền số ước.
