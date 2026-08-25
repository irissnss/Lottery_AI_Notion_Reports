# V11100 — TỔNG LỰC: kế hoạch NGỮ CẢNH · ứng viên model · và BỐN chỗ agent sai

**Ngày làm việc:** 21/08/2026 ·
**Ngày viết báo cáo này:** 26/08/2026 · **Commit riêng:** `175293f`, `2345c4d` ·
**Trạng thái:** `BÙ TỪ NGUỒN GỐC`

---

> ## ⚠️ ĐÂY LÀ BÁO CÁO **BÙ**, KHÔNG PHẢI BẢN VIẾT LÚC LÀM VIỆC
>
> Bản `V11100` làm ngày **21/08** nhưng **không có** thư mục báo cáo công khai —
> vi phạm `§57.2` đã tồn tại **5 ngày**.
> Cổng A55 cũ **không thấy** vì nó chỉ soi **8 bản gần nhất** (đã vá ở `V11122`, `FU-442`).
>
> **Ba nguồn dựng nên bản này — cả ba đều là bản ghi ĐƯƠNG THỜI:**
>
> | nguồn | quy mô |
> |---|---|
> | khối `## V11100` trong `CHANGELOG.md` — viết **ngay lúc làm việc** | **5,059 ký tự / 103 dòng** |
> | commit git mang nhãn `V11100` | **2** commit |
> | lượt owner trong vết phiên `.jsonl` cùng ngày | **có** |
> | khối phụ (`V11100b`/`c`/…) | — |
>
> 🔴 **PHẦN KHÔNG KHÔI PHỤC ĐƯỢC** — ghi thẳng, không suy:
> · **giờ chính xác** từng thao tác trong phiên · **vướng vấp giữa chừng** không được ghi lại lúc đó
> · **hash 4 bảng khoá trước/sau** (nếu phiên có chạm DB) · **PID trước/sau** (nếu có restart).
> Những chỗ đó dưới đây đều ghi `KHÔNG KHÔI PHỤC ĐƯỢC`, **không** điền số ước.

---

## 1. Tóm tắt

**21/08/2026 đêm** · **Read-only** — không đổi mã, không deploy.
### Owner phê bình — và agent nhận đủ bốn chỗ
> *«anh đã yêu cầu em lên kế hoạch chuyển đổi các thông số đang tiêm vào prompt thành ngữ cảnh
> kèm các điều kiện phù hợp tương thích miền thứ biết bao nhiêu lần không hả?»* ·
> *«ML là ML là một model cơ chế số học hoàn toàn, LLM là LLM nó hoạt động với các ngữ cảnh điều
> kiện để truy vết, sàng lọc, chọn lọc, khoanh vùng»* · *«Shadow, lane test nhiệm vụ của nó là để
> thử nghiệm để so sánh… để áp dụng cho official, final mà giờ nói là không có giá trị sao»* ·
> *«trong các audit báo cáo trong root có rất nhiều điều cần em phải kiểm tra, rà soát lại»*
| # | agent nói | sự thật trong kho |
|---|---|---|
| 1 | trình *«chuyển số thành ngữ cảnh»* như **việc mới** | owner dặn **nguyên văn 07/08**; kế hoạch có mã từ hôm đó: `L-A`=`FU-321` · `L-B`=`FU-322` · `L-C`=`FU-316` |
| 2 | *«prompt đã được dọn — tin tốt»* như phát hiện | **`FU-321`+`FU-322` LÀM XONG 07/08**, owner chốt *«Làm ngay luôn đi em»*, deploy cùng ngày (V11016) |
| 3 | *«tìm ra lỗi khối `D-1 tail pool`»* | **`FU-316` đã ghi đúng khối đó từ 07/08**, hạn 14/08 — **quá hạn 7 ngày** |
| 4 | shadow *«chảy vào chỗ không dùng được»* | **sai hoàn toàn** — shadow tồn tại **để so sánh rồi áp cho official/final** |
**Và một con số agent báo sai vì không đọc `FU-352`:** ba model `smart-ensemble`/`smart-ml`/
`combo-no-token` là **hàm của 4 bộ sinh** ⇒ đếm 8 model ML là **đếm trùng**.
### 🔴 PHÁT HIỆN CHÍNH — prompt đang tiêm THÔNG SỐ VỀ MODEL
| miền | **thông số về model** | ngữ cảnh xổ số | mệnh lệnh |

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

## V11100 — TỔNG LỰC: kế hoạch NGỮ CẢNH · ứng viên model · và BỐN chỗ agent sai

**21/08/2026 đêm** · **Read-only** — không đổi mã, không deploy.

### Owner phê bình — và agent nhận đủ bốn chỗ

> *«anh đã yêu cầu em lên kế hoạch chuyển đổi các thông số đang tiêm vào prompt thành ngữ cảnh
> kèm các điều kiện phù hợp tương thích miền thứ biết bao nhiêu lần không hả?»* ·
> *«ML là ML là một model cơ chế số học hoàn toàn, LLM là LLM nó hoạt động với các ngữ cảnh điều
> kiện để truy vết, sàng lọc, chọn lọc, khoanh vùng»* · *«Shadow, lane test nhiệm vụ của nó là để
> thử nghiệm để so sánh… để áp dụng cho official, final mà giờ nói là không có giá trị sao»* ·
> *«trong các audit báo cáo trong root có rất nhiều điều cần em phải kiểm tra, rà soát lại»*

| # | agent nói | sự thật trong kho |
|---|---|---|
| 1 | trình *«chuyển số thành ngữ cảnh»* như **việc mới** | owner dặn **nguyên văn 07/08**; kế hoạch có mã từ hôm đó: `L-A`=`FU-321` · `L-B`=`FU-322` · `L-C`=`FU-316` |
| 2 | *«prompt đã được dọn — tin tốt»* như phát hiện | **`FU-321`+`FU-322` LÀM XONG 07/08**, owner chốt *«Làm ngay luôn đi em»*, deploy cùng ngày (V11016) |
| 3 | *«tìm ra lỗi khối `D-1 tail pool`»* | **`FU-316` đã ghi đúng khối đó từ 07/08**, hạn 14/08 — **quá hạn 7 ngày** |
| 4 | shadow *«chảy vào chỗ không dùng được»* | **sai hoàn toàn** — shadow tồn tại **để so sánh rồi áp cho official/final** |

**Và một con số agent báo sai vì không đọc `FU-352`:** ba model `smart-ensemble`/`smart-ml`/
`combo-no-token` là **hàm của 4 bộ sinh** ⇒ đếm 8 model ML là **đếm trùng**.

### 🔴 PHÁT HIỆN CHÍNH — prompt đang tiêm THÔNG SỐ VỀ MODEL

| miền | **thông số về model** | ngữ cảnh xổ số | mệnh lệnh |
|---|---|---|---|
| MN | **15%** | 78% | 6% |
| MT | **13%** | 80% | 6% |
| **MB** | **32%** | 63% | 5% |

Gồm `BT MODEL RANKING (30d)` *(«gpt-5.4: BT=54,8%»)* · `Model Performance 14 ngày` ·
`Riêng Thứ X (30d)` · `MB Ceiling` · **`MB HARD MODE`** *(2.554 ký tự = **18% prompt MB**, nội
dung: «AI TOKEN GẦN NHƯ BẤT LỰC CHO MB» + trần tự tin 60%)*.

> **Nói cho một LLM biết «model nào đang giỏi nhất» là bảo nó bắt chước model đó.** Và **mọi model
> đều nhận cùng một bảng xếp hạng** ⇒ đây là **lực bầy đàn mạnh nhất** trong prompt, mạnh hơn bất
> kỳ rổ số nào. Riêng MB: 18% prompt dùng để nói với model rằng **nó bất lực** — lời tiên tri tự
> ứng nghiệm.

**Bằng chứng nó gây hội tụ** *(đã sửa theo `FU-352`)*:

| nhóm | model | số khác nhau | **đa dạng/model** |
|---|---|---|---|
| AI *(đọc prompt)* | 18,6 | 6,7 | **0,36** |
| ML — **4 bộ sinh độc lập** *(không đọc prompt)* | 4,0 | 3,3 | **0,82** |

**ML cho đa dạng gấp 2,3 lần AI.** ⇒ vấn đề **không phải «AI kém»**, là **«AI đang bị làm cho
giống nhau»**.

### Kế hoạch owner yêu cầu — 6 mục `N1`…`N6`

`N1` **gỡ hẳn** ba khối xếp hạng model *(thuộc tầng gộp phiếu, không thuộc prompt)* ·
`N2` đổi `MB HARD MODE` thành **điều kiện theo miền+thứ+bộ đài**, bỏ trần tự tin ·
`N3` `WEEK-SLOT`/`DIRECT-HIT` thành quy luật có điều kiện · `N4` `EVIDENCE TABLE` kèm **cách đọc**
· `N5` `D-1 tail pool` **đảo chiều thành «đuôi KHÔNG ra»** · `N6` gỡ `Đa dạng model`.

**Thứ tự:** `N5` *(rủi ro thấp nhất)* → `N1` *(lực bầy đàn mạnh nhất)* → `N2` → còn lại.
Mỗi bước **một biến, một cửa sổ đo**.

### 🔴 THƯỚC ĐO PHẢI ĐỔI

**Không đo bằng «tỉ lệ trúng»** — đo trúng cần **3–16 tháng**. Thứ đang sửa là **sự loãng**, và
nó đo được **trong 2 tuần**:

> **`đa dạng / mỗi model`** — hiện **0,36**, mục tiêu **≥ 0,60** *(ngang ML khi không đọc prompt)*.
> **Không cần chờ kết quả xổ** — đo ngay trong ngày.

Và đa dạng tăng ⇒ model **đi riêng nhiều hơn** ⇒ bảng so ứng viên **nhiều dữ liệu hơn** ⇒
**tìm ra ứng viên nhanh hơn**. Sửa prompt vừa chữa bệnh vừa tăng tốc tuyển model.

### Ứng viên — shadow ĐANG làm đúng việc của nó

| model | nhóm | lượt đi riêng | giá trị thêm |
|---|---|---|---|
| `glm-5.1` | OUTPUT | 133 | 43,6% |
| **`gemini-3.5-flash`** | **shadow** | 63 | **42,9%** |
| `qwen3.7-max` | shadow | 80 | 41,2% |
| `gemini-3.1-pro` | shadow | 78 | 41,0% |
| **`claude-sonnet-4-6`** | **OUTPUT** | 159 | **32,7%** |

**Shadow đã chỉ ra 3 ứng viên nằm trên model OUTPUT yếu nhất.** Chênh `+10,2pp` nhưng
**CI95 [−4,1 … +24,4]** ⇒ chưa kết luận.

**Hai mục đã treo sẵn mà chưa ai xử:** `FU-192` *«promote `glm-5.1`/`gpt-oss-120b` hay đóng lại»*
**quá hạn 12 ngày** · `FU-203` *«chấm `gemini-3.5-flash`»* **quá hạn 13 ngày** — **chính ứng viên
mạnh nhất hôm nay**.

### Kho lịch sử: **102 mục quá hạn**

`MEASURED_ROOT_CAUSE` **43** *(tìm ra căn nguyên, chưa sửa)* · `DEPLOYED_PENDING_LIVE_VERIFY`
**27** *(đã đẩy, chưa ai xác minh sống)* · `MEASURED_BUT_NOT_FIXED` 19 · `WAIT_LIVE` 18 ·
**chờ owner 40**. Cụm lâu nhất **12–15 ngày**.

**`FU-270`:** bộ chấm lane test **không có cron** ⇒ `du_doan_test_results` dừng. **Lane để so sánh
mà không ai chấm thì không so được gì.**

### Luật đề nghị — chống chính lỗi agent vừa mắc

> Mọi báo cáo nêu một *«phát hiện»* phải kèm **một dòng đã tra sổ theo dõi và báo cáo cũ**:
> *«chưa từng có»* hoặc *«đã có tại `FU-xxx` ngày …»*. **Không có dòng đó thì không được gọi là
> phát hiện.**

## 4. Hướng xử lý và vì sao chọn

Lý do chọn nằm trong chính khối `CHANGELOG` ở mục 3 — đó là bản ghi viết **lúc làm việc**,
không phải suy lại. Phần **cân nhắc phương án bị loại** thì 🔴 **KHÔNG KHÔI PHỤC ĐƯỢC**: nó chỉ
tồn tại trong vết phiên và không được ghi vào tài liệu nào lúc đó.

## 5. Đã làm gì

| commit | ngày (giờ VN) | tệp | tổng |
|---|---|---|---|
| `175293f` | 2026-08-21 21:47:57 | CHANGELOG.md, docs/AUTOMATION_HISTORY.jsonl, docs/AUTOMATION_STATE.json, docs/CURRENT_TRUTH_SSOT.md, docs/_I2_DA_CHAY.json | 5 files changed, 122 insertions(+), 4 deletions(-) |
| `2345c4d` | 2026-08-21 21:45:50 | docs/TONG_LUC_NGU_CANH_VA_UNG_VIEN_20260821.md | 1 file changed, 246 insertions(+) |

## 6. Cổng kiểm

🔴 **KHÔNG KHÔI PHỤC ĐƯỢC output cổng của phiên gốc** — cổng in ra `stdout`, không ghi tệp
(đúng khuyết tật `RM-15` mà `V11121` đã vá cho `cong_git_commit.py` bằng sổ điểm danh).

Điều **kiểm được hôm nay**, `26/08/2026`:

| phép | kết quả |
|---|---|
| commit của bản này còn trong `git log` | ✅ **2/2** còn nguyên, đều là tổ tiên của `origin/master` |
| khối `CHANGELOG` còn nguyên | ✅ 5,059 ký tự |
| bản này đã có báo cáo công khai chưa | ✅ **có, từ bản bù này** — trước đó `A55_VIOLATION_REPORT_MISSING` |

## 7. Vướng vấp

🔴 **KHÔNG KHÔI PHỤC ĐƯỢC** vướng vấp trong phiên gốc — không tài liệu nào ghi lại lúc đó.

Vướng vấp **của chính việc bù này**, ghi trung thực: bản bù dựng từ ba nguồn đương thời nhưng
**không thay được** một báo cáo viết lúc làm việc. Cụ thể mất: giờ từng thao tác · các phương án
đã cân nhắc rồi loại · lỗi gặp giữa chừng · trạng thái trước/sau của DB nếu phiên có chạm.

## 8. Gỡ về

Bản bù này **chỉ thêm tài liệu**, không đụng mã và không đụng dữ liệu ⇒ gỡ về =
`git rm -r V11100_KE_HOACH_NGU_CANH_VA_BON_CHO_AGENT_SAI_20260821/` rồi commit lại. Trạng thái quay về đúng như trước khi bù.

Việc gỡ về của **bản gốc `V11100`** nằm trong chính khối `CHANGELOG` ở mục 3 (nếu bản đó có ghi).

## 9. Theo dõi tiếp

| mã | việc | trạng thái |
|---|---|---|
| `FU-442` | vá cổng A55 — chính lỗ hổng làm bản này vô hình | ✅ **ĐÃ VÁ** ở `V11122`, thử chặn **11/11** |
| — | bù nốt các bản còn thiếu | trên **toàn dải từ mốc thi hành `V10921`** còn **32** bản thiếu báo cáo; 10 bản của đợt này là nhóm ưu tiên |
| — | ngưỡng đóng bằng số | `_v10921_report_gate.py` chạy **không tham số** ⇒ `V11100` không còn trong danh sách `THIẾU BÁO CÁO` |

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
| 2 commit mang nhãn `V11100` | `175293f`, `2345c4d` — còn nguyên trong `git log`, đều là tổ tiên `origin/master` |
| tệp bị đụng | xem bảng mục 5 |
| bản này **chưa từng** có báo cáo công khai cho tới hôm nay | `_v10921_report_gate.py` liệt `V11100` trong `THIẾU BÁO CÁO` trước khi bù |

### `DOC_SAID`
| tài liệu | nói gì | khớp code chưa |
|---|---|---|
| `CHANGELOG.md` khối `## V11100` | 5,059 ký tự, viết đương thời | 🟢 **khớp** — commit tồn tại đúng ngày ghi |
| kho báo cáo công khai | **không có** thư mục `V11100_*` | 🔴 **LỆCH** — đã đóng bằng bản bù này |

### 🔴 BA LỚP LỆCH NHAU
`DOC_SAID` ≠ `CODE_DID`: mã đã chạy và đã commit, `CHANGELOG` đã ghi, nhưng **kho công khai không
có gì** suốt 5 ngày. Đó là `A55_VIOLATION_REPORT_MISSING`, và nó **vô hình** vì cổng chỉ soi 8
bản gần nhất — nay đã vá (`FU-442` · `V11122`).

---

**TanPhatAI cần làm:** ghi nhận đây là **báo cáo BÙ** viết ngày 26/08/2026 cho việc làm ngày
21/08, dựng từ **ba nguồn đương thời** (CHANGELOG 5,059 ký tự ·
2 commit · vết phiên), **không** phải bản viết lúc làm việc — mọi chỗ không khôi phục
được đã ghi thẳng là `KHÔNG KHÔI PHỤC ĐƯỢC`, **không** điền số ước.
