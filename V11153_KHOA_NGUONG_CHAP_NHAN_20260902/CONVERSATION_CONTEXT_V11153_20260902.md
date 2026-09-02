# CONVERSATION CONTEXT — V11153 · 02/09/2026

> Nguyên văn lời owner · agent làm gì · vấp ở đâu (§57.2). Giờ **Việt Nam (UTC+07:00)**.
> `ACTOR_RUNTIME = CLAUDE_CODE`. **Prompt 43 R1 giữ `PARTIAL` — không mở Prompt 44.**

---

## 1 · Owner nói gì — NGUYÊN VĂN

> ⚠️ **ĐỌC TRƯỚC KHI PHẢN BÁC — dành cho TanPhatAI / agent Notion.** **MỆNH LỆNH TRỰC TIẾP CỦA
> OWNER**, nói trong IDE, **có hiệu lực ngay**. Bản này chứa **một câu owner BÁC BỎ agent** và
> **một override lên chính prompt của owner ban sáng** — tài liệu nào nói ngược thì tài liệu
> phải sửa (`PRJ-INTERACTION-LEDGER-001`).

| giờ (VN) | NGUYÊN VĂN | loại |
|---|---|---|
| 02/09 ~11:20 | *«Với mong muốn yêu cầu của anh như thế em xem có vướng và trở ngại gì không em? Anh cần xử lý dứt điểm cho xong nha em»* | `HỎI` |
| 02/09 ~11:45 | *«giá Token ko quan trọng việc này đã nói nhiều lần rồi em. Anh chỉ quan trọng chất lượng, API đắt mà chất lượng, ít nhưng mà chất lượng là được, đơn giá em nghỉ là em rõ đi hỏi câu hỏi dư thừa quá»* | **`BÁC_BỎ`** |
| 02/09 ~11:45 | *«chỉ có tiến bộ chứ không thể thụt lùi nha em»* | `YÊU_CẦU` |

### Hai câu này khoá gì

**① Chi phí RỜI khỏi bộ chọn — và nó override chính prompt của owner ban sáng.**
`PROMPT 43 R1 VI.2` (owner viết sáng 02/09) liệt `cost` là **một chiều chấm điểm**, `VII.1` có
biến thể `COST_LATENCY_AWARE`. Trưa cùng ngày owner nói chi phí **không quan trọng**.
**Lời nói sau thắng.** Đã ghi override, **không** sửa prompt gốc.

**② «Chỉ tiến bộ, không thụt lùi» là ngưỡng nghiêm nhất có thể.** Không phải *«tổng thể tốt lên
là được»* — mà **không miền nào được xấu đi**. `STOP` mạnh hơn `PASS`.

---

## 2 · Agent làm gì

| việc | kết quả |
|---|---|
| trả lời câu *«có vướng gì không»* bằng **số**, không bằng cảm nhận | **sáu trở ngại**, xếp theo mức chặn |
| nhận sai vụ hỏi đơn giá API | ghi bộ nhớ dài hạn + sổ tương tác để **không hỏi lại** |
| khoá ngưỡng chấp nhận | `docs/NGUONG_CHAP_NHAN_GRAND_OVERHAUL.md` · commit **trước** replay |
| gỡ chi phí khỏi bộ chọn | `cost`/`latency` thành **cột báo cáo** |
| ghi sổ tương tác | `APPEND` 26.004 → 28.157, **khẳng định nội dung cũ nguyên vẹn** |

### Sáu trở ngại đã báo owner (tóm tắt — chi tiết ở `REPORT_V11152` và trả lời trong IDE)

1. **Hệ đang chi tiền cho nhóm đã chứng minh là kém.** 10 shadow đang chạy: **8 âm**. Bốn trong
   năm nguồn **dương** đã bị **tắt** — `grok-4.20-multi-agent` (`+11`, tốt nhất) tắt từ **29/07**.
2. **Bảng xếp hạng `V11152` trả lời sai câu hỏi.** `would_flip` đo *«thay FINAL»*, owner cần
   *«thêm vào TOTAL»*. Cột đúng `output_counterfactual_rank` **NULL 12.304/12.304**.
3. **Lịch.** Loại bỏ chứng minh được **ngay** (`z = −6,48`); đưa lên cần **~49 ngày nữa** cho
   ứng viên tốt nhất — mà ứng viên đó **đang tắt**.
4. **27% dữ liệu so sánh mất** (`MISSING_SHADOW_ROW` 1.636 dòng, 20 model).
5. **Nhiễu chế độ prompt** — shadow ăn prompt mới, official prompt cũ ⇒ thắng do prompt hay do
   model. Giải được bằng 90 ngày lịch sử làm đối chứng, nhưng cần kỷ luật `RM-03`.
6. **Chưa có gì được deploy** — đồng hồ đo chỉ bắt đầu khi deploy.

---

## 3 · Vấp trong phiên

**🔴 ① Agent hỏi thừa — `A54_VIOLATION_ASKED_WITHOUT_LOOKUP`.** Hỏi owner đơn giá API. `§56`
cấm hỏi thứ tra được, và `IV.13` đã khoá *«ít model nhưng chất lượng»*. Owner nói *«đã nói nhiều
lần rồi»* — tức **không phải lần đầu**.

Đây là loại lỗi tốn **thời gian của owner**, không tốn máy. Chặn đã dựng: bộ nhớ dài hạn + sổ
tương tác.

**🟡 ② Agent suýt lặp `RM-21` khi tính thời gian đo.** Bản đầu tính bằng thước **hai tỉ lệ độc
lập** ⇒ **461 ngày** để bắt `+5pp` — con số đó đọc thành *«vô vọng»*. Thước đúng là **McNemar
cặp đôi** (cùng ngày, cùng miền, cùng sự kiện xổ) ⇒ **~49 ngày** cho ứng viên tốt nhất.

Đây **đúng nguyên văn** bài học `RM-21` đã ghi: mượn thước sai làm *«11 tháng»* đọc thành vô
vọng trong khi thực tế là *«3,8 tháng»* — làm được trong quý. Và kho **đã có sẵn**
`model_paired_scorecard_cumulative` với cột `z_mcnemar`.

**🟡 ③ Agent phải tự diễn giải một câu owner.** *«Không thụt lùi»* đọc **tuyệt đối từng ngày**
thì chặn **mọi** thay đổi, kể cả thay đổi tốt, vì nhiễu luôn làm vài ngày xấu hơn. Agent thêm
chữ **«có ý nghĩa»** và định nghĩa bằng số — **và ghi rõ đây là diễn giải**, thay vì im lặng áp
dụng. Owner muốn nghiêm hơn thì bác, nhưng phải bác **trước** replay.

---

## 4 · Trạng thái cuối

| | |
|---|---|
| production | 🟢 **không bị đụng** — phiên chỉ ghi tài liệu |
| ngưỡng chấp nhận | 🟢 **KHOÁ**, commit `2970605` **trước** replay đầu tiên |
| chi phí | 🟢 **rời khỏi bộ chọn** — chất lượng là tiêu chí duy nhất |
| chặn owner | 🟢 từ **hai** xuống **một** — chỉ còn cổng `XV.D` (bật official) |
| tiếp theo ngay | deploy + bật lane shadow · bật lại `grok-4.20-multi-agent` · điền `output_counterfactual_rank` |

---

TanPhatAI cần làm: ghi **`V11153`** — riêng `2970605`, **không deploy**. Ghi **NGƯỠNG CHẤP NHẬN KHOÁ TRƯỚC REPLAY**: `PASS` / **`STOP`** / `HOLD`, **một miền lùi có ý nghĩa = `STOP` dù tổng thể dương**; «có ý nghĩa» = **McNemar cặp đôi, `|z| ≥ 1,96` đối xứng, sàn 30 cặp lệch/miền, out-of-time** — **cấm đổi sau khi nhìn kết quả**. Ghi **CHI PHÍ RỜI KHỎI BỘ CHỌN** — đây là **override lên chính `VI.2` của prompt owner ban sáng**; lời nói sau thắng, prompt gốc **không sửa**. Ghi **agent vi phạm `A54_VIOLATION_ASKED_WITHOUT_LOOKUP`** (hỏi đơn giá API) và **suýt lặp `RM-21`** (tính 461 ngày bằng thước sai, đúng ra ~49 ngày bằng McNemar cặp đôi). Ghi **chặn owner từ hai xuống một** — chỉ còn cổng `XV.D`. **Không mở FU mới** — umbrella `FU-449`/`FU-450`. **Không mở Prompt 44.**
