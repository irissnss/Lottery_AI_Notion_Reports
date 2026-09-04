# CONVERSATION CONTEXT — V11165 · 04–05/09/2026

> Nguyên văn lời owner · agent làm gì · vấp ở đâu (§57.2). Giờ **Việt Nam (UTC+07:00)**.
> `CURRENT_ACTOR = CLAUDE_CODE` · **Prompt 43 R1 giữ `PARTIAL` — không mở Prompt 44.**

---

## 1 · Owner nói gì — NGUYÊN VĂN

| giờ (VN) | NGUYÊN VĂN | loại | agent đã làm gì | trạng thái |
|---|---|---|---|---|
| 04/09 **23:14** | *«Ok đồng ý khuyến nghị đề xuất, chứ ý ghi nhận đầy đủ thông tin kẻo quên.»* | `XÁC_NHẬN` | Chạy bộ cấp số canonical `_v11044` → **`QD-073`** (QD-072 là cao nhất, QD-073 trống). Ghi **nguyên văn** vào sổ quyết định + SSOT + tracker + CHANGELOG + STATE/HISTORY + sổ tương tác — **sáu chỗ** | `ĐÃ_LÀM` |
| 04/09 23:1x | **PROMPT 43 R1 · CONTINUATION AFTER V11164 · OWNER-LOCK MATERIALIZATION B · PURE-CONTEXT END-TO-END RECONCILIATION** (I–XXI) | `YÊU_CẦU` | GATE 0 + 14 cổng chia hai làn sóng, 70 agent, 56 phản biện | `ĐÃ_LÀM` |
| 05/09 ~00:0x | *«tới đâu rồi em»* | `HỎI` | Đọc `journal.jsonl` thật rồi báo **0/7 cổng xong, 6 agent đang chạy**; kèm bằng chứng ~30 artifact đã sinh trên VPS và xác nhận production còn nguyên | `ĐÃ_LÀM` |

**Ngữ cảnh trực tiếp ngay trước câu 23:14** — khuyến nghị agent trình ở V11164: chọn **B** · loại
**A** · hoãn **C** tới khi có câu hỏi SQL thật và grain do owner xác định · **chưa khoá ngưỡng MT**
· ưu tiên **sửa prompt hoàn chỉnh và kế toán MT** · **không đụng model**.

**Ràng buộc owner khoá, nguyên văn:**
*«Không tự đặt mã quyết định bằng phỏng đoán.»* · *«CONDITION ≠ RECOMMENDATION. Nêu một điều kiện
không đồng nghĩa "hãy chọn", "ưu tiên", "boost", "tránh" hoặc "chốt".»* ·
*«Không được diễn giải "Agent nghiêng về B" thành OWNER_LOCKED.»* ·
*«Không được tự nâng thành DEPLOYED / RUNTIME_PROVEN / OFFICIAL_CLEAN /
PREDICTIVE_IMPROVEMENT_PROVEN.»* · *«Nếu một claim không có raw evidence: ghi NOT PROVEN hoặc
INDETERMINATE; không suy luận lấp chỗ trống.»*

---

## 2 · Agent làm gì

| việc | kết quả |
|---|---|
| GATE 0 + chứng minh read-only | 🟢 **7/7** sau khi **bắt được lỗi của chính mình** (xem mục 3) |
| Owner-lock B | 🟢 **`QD-073`** vào **sáu chỗ** |
| Làn sóng 1 — 7 cổng nền tảng | 🟢 35 agent · 0 lỗi · 81 phút |
| Làn sóng 2 — 7 cổng xây dựng | 🟢 35 agent · 0 lỗi · 98 phút |
| phản biện độc lập | 🟢 **56 phép**: 10 `DUNG` · 46 `DUNG_MOT_PHAN` · **0 `SAI`** |
| artifact | 🟢 **283 tệp · 837,5 MB** · `INDEX_SHA256 = 12a115d9…8d6f75` |
| deliverable owner yêu cầu | 🟢 **23/24 xong**, 1 `INDETERMINATE` (`UCC` không có định nghĩa) |
| production | 🟢 **0 ghi · 0 deploy · 0 restart** — `neo558` khớp từng ký tự, 6 hash tệp serve không đổi |

---

## 3 · Điều đáng nói nhất — GATE 0 bắt được lỗi của chính agent

Phép thử chặn hai chiều **TRƯỢT 1/5** ở lần chạy đầu: `chmod 444` **không chặn được root** (root bỏ
qua bit quyền), nên `CREATE TABLE` lọt qua — và **chính phép thử đã tạo một bảng lạ trong bản clone
"bất biến"**.

Nếu không chạy phép thử hai chiều mà chỉ tin `chmod`, **cả phiên này sẽ dựng trên một bản bất biến
giả**. Dựng lại sạch + `chattr +i` (root cũng không ghi được), thử lại **7/7 ĐẠT**, trong đó có ba
phép mới thêm: `UPDATE` dưới root · ghi byte thô dưới root · `CREATE` dưới root.

Đây đúng tinh thần **RM-15**: *cổng không qua thử coi như không tồn tại*.

---

## 4 · Điều đáng nói thứ hai — câu trả lời cho «thuần ngữ cảnh» là CHƯA, và xa hơn ta tưởng

| đo được | con số |
|---|---|
| cờ `context_only` gác | **6/171 = 3,51%** điểm bơm chuỗi |
| `build_context_pack` (141 điểm) | gác **0** |
| cổng `CONTEXT_ONLY_V2` | gác **1,5/14** nhóm khối |
| payload thật trượt `CONTAMINATION_GATE_V2` | **57/57**, trung bình **220 điểm ô nhiễm** |
| producer có nền tường minh | **1/35** |
| sửa đủ 14 nhóm gỡ được | **~15%** độ dài |

Con số cuối là điều bất ngờ nhất: **«thuần ngữ cảnh» không phải chuyện cắt ngắn prompt**, mà là
chuyện **thay rổ số bằng điều kiện có nền**. Lane «thuần ngữ cảnh» hiện tại thậm chí **DÀI HƠN**
official ~3.400 ký tự — nó gỡ 3 khối và **thêm 4 khối**.

---

## 5 · Điều đáng nói thứ ba — phép đo owner cần đã chạy xong từ lâu, không ai đọc

Lane `T-B` (V11059): n=346 · b=51 · c=50 · **101 cặp bất đồng** · z = **−0,0995** ⇒
`NO_ANOMALY_FOUND` theo đúng ngưỡng đã khoá 11/08.

**Bốn điều chưa ai đọc, cả bốn đổi cách hiểu:**

1. **Ngưỡng `n=96` chỉ là 50% sức mạnh** — công thức `(1,96/(2ψ−1))²` **thiếu `z_β`**. Đúng phải
   **194 cặp**. Sức mạnh thực tế tại m=101 chỉ **52%**.
2. **Cả hai nhánh đều không khác mức chọn ngẫu nhiên** ở cả ba miền (|z| max 1,42).
3. **«Đổi 70,2% số chọn» phải đọc cạnh sàn nhiễu 61,3%** — gọi lại cùng model cho top-1 khác
   61,3% số lượt.
4. **Sáu ổ ô nhiễm còn nguyên trong mã đang serve, ở cả hai nhánh.**

⇒ Nó nói *«xếp lại ba tầng mà vẫn giữ rổ số thì không khác»*, **không** nói *«pure context vô dụng»*.

---

## 6 · Vấp ở đâu — mười lỗi tự gây, tất cả đều tự bắt

| # | vấp | gỡ |
|---|---|---|
| 1 | 🔴 `chmod 444` không chặn root — clone «bất biến» là giả | `chattr +i`, thử lại 7/7 |
| 2 | **Patch B bản nháp gọi hai ký hiệu KHÔNG TỒN TẠI** — deploy sẽ **mất sạch vân tay**, tệ hơn hiện trạng | suy route từ 5 cờ boolean có thật |
| 3 | **MT artifact bản r1 lặp lại đúng bẫy NULL-hai-nghĩa mà nó tuyên bố sửa** | bắt và vá ở r2 |
| 4 | **`CONTAMINATION_GATE_V2` bản đầu có ba lớp dương tính giả** — cùng họ lỗi với bộ 5 dấu mù, **chỉ ngược chiều** | phân loại từng lần khớp thay vì đếm chuỗi |
| 5 | Renderer lấy **nhầm bucket luật** do kho có **hai quy ước thứ ngược nhau** ⇒ tầng điều kiện ra rỗng **mà không báo lỗi** | bộ thử bắt được; production **không** dính |
| 6 | Gate 5 và Gate 6 **suýt dựng hai khuôn `CONDITION` khác nhau** | Gate 6 tự rút, trỏ sang Gate 5 (tránh `§60` chồng tầng) |
| 7 | Bộ đo lập luận **bản V1 đếm chuỗi thô** → 59 mâu thuẫn giả | tự rút, viết lại theo phân loại |
| 8 | Phép đo `SC-08` đầu tiên **sai vì regex bỏ sót `2W(14d)`** | kiểm bằng 8 cách viết; kết luận đứng nhưng **lý do khác hẳn** |
| 9 | **Hai con số tự suy ra SAI** (`P(≥6/8)=0,98` → đúng 0,8845; nền k=4 trộn nhầm cột) | buộc mọi giá trị lấy thẳng từ JSON đo được |
| 10 | **Backtick trong template literal JS làm hỏng workflow — lần thứ HAI** | thay bằng nháy đơn; cần nhớ dài hạn |

---

## 7 · Ba ca rút lại mới

**R14** — *«ít nhất 46/72 quy trực tiếp cho kế toán cap»* (V11164, commit công khai `af4597a`):
**KHÔNG TÁI LẬP ĐƯỢC** — dẫn xuất không được ghi ở đâu ⇒ **RM-11**. Số đúng: **45 ngày**.

**R15** — *«MT bị loại 71 ngày liên tiếp»*: tái lập được **nhưng chỉ với định nghĩa
`evaluation_policy != INCLUDE`**. Chuỗi `EXCLUDE_PRIMARY` liên tiếp thật chỉ **7 ngày**. Và trong
71 ngày đó **6 ngày KHÔNG phải cap** — riêng 28/08 là **hỏng chạy thật**.

**R16** — *«z = −0,10 · p = 1,00»* trong báo cáo tiến độ giữa phiên: **trộn hai phép McNemar khác
nhau**. Số tái lập được là **z = −0,0995** với chuẩn xấp xỉ hai phía. Verdict không đổi.

---

## 8 · Trạng thái cuối

| | |
|---|---|
| `MATERIALIZATION_OPTION` | **B** · `OWNER_LOCKED` (`QD-073`) |
| `PURE_CONTEXT_CANDIDATE` | 🔴 **`BLOCKED_WITH_EXACT_REASONS`** — 6 blocker + 1 indeterminate |
| `MT_PREREGISTRATION` | 🔴 **`NOT_READY_FOR_OWNER_LOCK`** |
| `POOL_VERDICT` · `MODEL_ACTION` | **`HOLD`** · **`BLOCKED`** |
| `PROMPT_43_R1` · `GRAND_OVERHAUL_CHAIN` | **`PARTIAL`** · **`PARTIAL`** |
| production | 🟢 `neo558` khớp · 6 hash serve không đổi · PID `3370750` · `NRestarts 0` |

---

## 9 · Cho TanPhatAI đọc tiếp

**Ba việc chặn ở owner:**

1. **Ký deploy ba vá NHÓM A** — `VA-A` (bịt rò gói ngữ cảnh, `gpt_analyzer.py:6738`) ·
   `VA-B` (vân tay 43,59% → 100%) · `VA-h12` (kế toán MT). Cả ba **đã code, đã test, có gỡ về**.
   Cho tới khi vá `VA-A`, **mọi phép so official-vs-shadow đều có một model official ăn prompt thí
   nghiệm** ⇒ nhánh official **không phải đối chứng sạch**.
2. **Chỉ rõ `UCC` là gì** — quét toàn kho, **không có định nghĩa nào**; 12 tệp khớp chỉ vì là chuỗi
   con của `SUCCESS`. Không có nó thì không đánh giá được tương thích output contract.
3. **Khoá ngưỡng đo tiến** — bản nháp đã hoà giải **5 bộ ngưỡng cũ**, nhãn
   `PROVISIONAL_AGENT_PROPOSED_DRAFT`.

**Bốn con số dễ bị trích sai, ghi rõ để khỏi lặp:**
- **«46/72»** đã bị **rút lại** — dùng **45**.
- **«71 ngày liên tiếp»** phải kèm định nghĩa `policy != INCLUDE`; `EXCLUDE_PRIMARY` liên tiếp là **7**.
- **«n=96 đủ mẫu»** — **sai**, đó là mốc 50% sức mạnh; đủ mẫu 80% là **194 cặp**.
- **«đổi 70,2% số chọn»** phải luôn đi kèm **sàn nhiễu 61,3%**.

---

TanPhatAI cần làm: ghi **`V11165`** — `governance_seq 481`, công khai bản này cùng `REPORT_V11165.md` và bảy tài liệu deliverable. Ghi **`QD-073` Owner khoá PHƯƠNG ÁN B**, nguyên văn *«Ok đồng ý khuyến nghị đề xuất, chứ ý ghi nhận đầy đủ thông tin kẻo quên.»*, và ghi rõ quyết định đã vào **SÁU chỗ** đúng theo yêu cầu «kẻo quên». Ghi **`PURE_CONTEXT_CANDIDATE = BLOCKED_WITH_EXACT_REASONS`** với 6 blocker + 1 indeterminate. Ghi **GATE 0 bắt được lỗi của chính agent** — `chmod 444` không chặn root nên bản clone «bất biến» đầu tiên là GIẢ, phải `chattr +i` mới thật; đây là RM-15 đúng nghĩa. Ghi **câu trả lời cho «thuần ngữ cảnh»: CHƯA ĐẠT** — `context_only` gác 3,51%, `CONTEXT_ONLY_V2` gác 1,5/14 nhóm, 57/57 payload thật trượt cổng ô nhiễm mới, và **sửa đủ 14 nhóm chỉ gỡ ~15% độ dài** nên đây **không phải chuyện cắt ngắn prompt**. Ghi **phép đo T-B đã tồn tại và chưa ai đọc verdict**, kèm **bốn điều chưa ai đọc**, đặc biệt **ngưỡng n=96 chỉ là 50% sức mạnh vì công thức thiếu `z_β`**. Ghi **hệ KHÔNG lưu prompt đã gửi** (vân tay khớp 0/60). Ghi **ba ca rút lại R14/R15/R16**. **Code KHÔNG đi trước tài liệu** — 0 ghi production, 0 deploy, 0 restart; bốn mặt ghi cùng phiên. **Không mở Prompt 44. Không mở FU mới. Không mở Plan mới.**
