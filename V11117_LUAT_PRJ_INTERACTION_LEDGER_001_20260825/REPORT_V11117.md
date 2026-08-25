# V11117 — 2026-08-25 (chiều) — LUẬT MỚI `PRJ-INTERACTION-LEDGER-001`: CODE ĐƯỢC ĐI TRƯỚC, GHI NHẬN THÌ KHÔNG

**Ngày làm việc:** 25/08/2026 ·
**Ngày viết báo cáo này:** 26/08/2026 · **Commit riêng:** `7097d16`, `110b05b` ·
**Trạng thái:** `BÙ TỪ NGUỒN GỐC`

---

> ## ⚠️ ĐÂY LÀ BÁO CÁO **BÙ**, KHÔNG PHẢI BẢN VIẾT LÚC LÀM VIỆC
>
> Bản `V11117` làm ngày **25/08** nhưng **không có** thư mục báo cáo công khai —
> vi phạm `§57.2` đã tồn tại **1 ngày**.
> Cổng A55 cũ **không thấy** vì nó chỉ soi **8 bản gần nhất** (đã vá ở `V11122`, `FU-442`).
>
> **Ba nguồn dựng nên bản này — cả ba đều là bản ghi ĐƯƠNG THỜI:**
>
> | nguồn | quy mô |
> |---|---|
> | khối `## V11117` trong `CHANGELOG.md` — viết **ngay lúc làm việc** | **2,612 ký tự / 52 dòng** |
> | commit git mang nhãn `V11117` | **2** commit |
> | lượt owner trong vết phiên `.jsonl` cùng ngày | **có** |
> | khối phụ (`V11117b`/`c`/…) | — |
>
> 🔴 **PHẦN KHÔNG KHÔI PHỤC ĐƯỢC** — ghi thẳng, không suy:
> · **giờ chính xác** từng thao tác trong phiên · **vướng vấp giữa chừng** không được ghi lại lúc đó
> · **hash 4 bảng khoá trước/sau** (nếu phiên có chạm DB) · **PID trước/sau** (nếu có restart).
> Những chỗ đó dưới đây đều ghi `KHÔNG KHÔI PHỤC ĐƯỢC`, **không** điền số ước.

---

## 1. Tóm tắt

Owner nêu 25/08 chiều. Luật **MỚI** ⇒ vào **đủ SÁU MẶT** trong cùng phiên.
### Chỗ hổng có thật, không phải lo xa
Owner làm việc với Claude Code **theo dòng liên tục trong IDE** — hỏi, chốt, đổi hướng, xác nhận,
tất cả bằng lời ngay trong phiên. Tốc độ đó **cố ý và được phép**. Nhưng nó khiến **code đi trước
tài liệu**, và:
| có sẵn | KHÔNG có |
|---|---|
| `OWNER_DECISION_LEDGER.json` — **quyết định trang trọng** (`QD-xxx`) | lời owner **chưa thành quyết định**: xác nhận · chia sẻ · đổi ưu tiên |
| `SO_YEU_CAU_OWNER_*.md` — **sinh tự động** từ `FOLLOW_UP_TRACKER`, chỉ là bảng mã `FU` | — |
| §62 lớp `OWNER_SAID` — chỉ trong **báo cáo của chính phiên đó** | **sổ chạy dài xuyên phiên** |
⇒ TanPhatAI/Notion mở kho, thấy code đi trước tài liệu, **không tìm được chỗ ghi «owner đã bảo
làm thế»** ⇒ **bỡ ngỡ và phản bác** ⇒ owner mất công giải thích lại việc đã nói rồi.
### Bốn câu
1. **Code ĐƯỢC đi trước tài liệu** — không phải vi phạm, owner cho phép tường minh.
2. **GHI NHẬN không được đi sau quá một phiên** — mọi lời owner nói trực tiếp vào
   `docs/SO_TUONG_TAC_OWNER.md` **trong cùng phiên**, **nguyên văn + giờ**.
3. **Sổ APPEND-ONLY** — cấm sửa dòng cũ (cùng luật với `HISTORY` ở §63).
4. **Báo cáo công khai phải có mục `OWNER YÊU CẦU` đầy đủ** — prompt chính **VÀ** mọi yêu cầu trực

## 2. Owner yêu cầu gì (nguyên văn)

> *«PROMPT TỔNG LỰC LẦN 35 KIỂM TOÁN VÀ THAY PHƯƠNG PHÁP TOTAL/OUTPUT THỰC THI TRONG NGÀY 25/08/2026 Dùng multi-agent song song nhưng chỉ MỘT Coordinator hợp nhất. Không mở Plan/sổ cạnh tranh. Không mặc định 15 model tốt hơn 8 model. Không mặc định nhiều model tốt hơn ít model. Số lượng model chỉ là tồn kho. Chất lượng TOTAL phải được chứng minh bằng: - khả năng sinh số; - độ phủ; - xếp hạng; - đóng góp biên; - tính độc …»*
> — owner, **25/08/2026 12:52** (giờ VN)

> *«đang đo lường ah em? đợi kết quả hay sao?»*
> — owner, **25/08/2026 13:03** (giờ VN)

> *«còn đang chạy không em ? xong chưa push báo cáo tổng lực chưa em?»*
> — owner, **25/08/2026 14:26** (giờ VN)

> *«Đã push báo cáo hết chưa em? - Kiểm tra lại toàn bộ 1 lần nữa xem còn gì không để push báo cáo 1 lần luôn - Các vấn đề anh tương tác trực tiếp đã push thành 1 bảng ghi nhận yêu cầu của owner chưa ? Có cần cập nhật quy tắc trong claude.md để chuẩn hóa không vì đôi lúc code đi trước tài liệu do tương tác trực tiếp với em liên tục cho liền mạch ah em. Nên em claude code có thể đi trước tài liệu và việc ghi nhận các yêu …»*
> — owner, **25/08/2026 18:29** (giờ VN)

> *«Em hãy tiến hành đọc toàn bộ các phiên làm việc của claude code và cursor kết hợp báo cáo tổng hợp đính kèm và các thông tin audit báo cáo tất cả mọi thể chạy tổng lực tổng hợp lại một phiên tổng lực với đầy đủ tất cả các vấn đề không làm rơi rụng bất kỳ vấn đề nào, các vấn đề đã xử lý , có thể xử lý , tự xử lý rõ ràng , các yêu cầu của anh v.... không bỏ sớt bất kỳ điểm nào nha em. Em tiến hành xem toàn bộ các phiên…»*
> — owner, **25/08/2026 18:56** (giờ VN)


*(Trích từ corpus lượt owner đã khử trùng của vết phiên `.jsonl`; giờ đã quy về giờ Việt Nam.)*

## 3. Đào bới / phát hiện

Toàn văn khối `CHANGELOG` đương thời — **nguồn chính** của bản này:

## V11117 — 2026-08-25 (chiều) — LUẬT MỚI `PRJ-INTERACTION-LEDGER-001`: CODE ĐƯỢC ĐI TRƯỚC, GHI NHẬN THÌ KHÔNG

Owner nêu 25/08 chiều. Luật **MỚI** ⇒ vào **đủ SÁU MẶT** trong cùng phiên.

### Chỗ hổng có thật, không phải lo xa

Owner làm việc với Claude Code **theo dòng liên tục trong IDE** — hỏi, chốt, đổi hướng, xác nhận,
tất cả bằng lời ngay trong phiên. Tốc độ đó **cố ý và được phép**. Nhưng nó khiến **code đi trước
tài liệu**, và:

| có sẵn | KHÔNG có |
|---|---|
| `OWNER_DECISION_LEDGER.json` — **quyết định trang trọng** (`QD-xxx`) | lời owner **chưa thành quyết định**: xác nhận · chia sẻ · đổi ưu tiên |
| `SO_YEU_CAU_OWNER_*.md` — **sinh tự động** từ `FOLLOW_UP_TRACKER`, chỉ là bảng mã `FU` | — |
| §62 lớp `OWNER_SAID` — chỉ trong **báo cáo của chính phiên đó** | **sổ chạy dài xuyên phiên** |

⇒ TanPhatAI/Notion mở kho, thấy code đi trước tài liệu, **không tìm được chỗ ghi «owner đã bảo
làm thế»** ⇒ **bỡ ngỡ và phản bác** ⇒ owner mất công giải thích lại việc đã nói rồi.

### Bốn câu

1. **Code ĐƯỢC đi trước tài liệu** — không phải vi phạm, owner cho phép tường minh.
2. **GHI NHẬN không được đi sau quá một phiên** — mọi lời owner nói trực tiếp vào
   `docs/SO_TUONG_TAC_OWNER.md` **trong cùng phiên**, **nguyên văn + giờ**.
3. **Sổ APPEND-ONLY** — cấm sửa dòng cũ (cùng luật với `HISTORY` ở §63).
4. **Báo cáo công khai phải có mục `OWNER YÊU CẦU` đầy đủ** — prompt chính **VÀ** mọi yêu cầu trực
   tiếp trong phiên.

### §57.3 đọc rộng ra

Mục **2** nay là *«prompt chính VÀ mọi yêu cầu trực tiếp trong phiên, nguyên văn + giờ»*.
Mục **3** (đào bới/tra soát) và mục **9** (theo dõi) phải **LIỆT KÊ ĐỦ**, không tóm lược — rút gọn
làm người đọc sau tưởng phiên làm ít hơn thực tế và **mất dấu những phép đo đã tốn công nhưng chưa
ra kết luận**.

### Sổ mới: `docs/SO_TUONG_TAC_OWNER.md`

Năm trường bắt buộc: `giờ (VN)` · `NGUYÊN VĂN` · `loại` · `agent đã làm gì` · `trạng thái`.
Có mục **«CHỖ CODE ĐI TRƯỚC TÀI LIỆU»** để TanPhatAI đọc trước.
Phần trước 25/08 dựng lại từ prompt đã lưu; chỗ không có nguyên văn ghi rõ
`[DỰNG LẠI — không có nguyên văn]`, **không bịa lời owner vào ngoặc kép**.

### Cổng sáu mặt bắt đúng — và bắt em

Chèn lần đầu dùng `###` và tiêu đề tiếng Anh cho `.AGENT.md` ⇒ cổng `_v11027` báo
*«1 điều mới chưa đủ sáu mặt»*. Nguyên nhân: `_muc()` chỉ nhận `^##` (H2), và `_khoa()` khớp
**chữ tiêu đề đã chuẩn hoá** khi luật **không có số `§`**. Đã chuẩn hoá cả sáu mặt về **cùng một
tiêu đề H2**. Hai cổng nay **ĐẠT**.

**Vi phạm:** `PRJ_INTERACTION_UNLOGGED` · `PRJ_INTERACTION_PARAPHRASED` ·
`PRJ_INTERACTION_REPORT_MISSING` · `PRJ_INTERACTION_LEDGER_REWRITTEN`.

## 4. Hướng xử lý và vì sao chọn

Lý do chọn nằm trong chính khối `CHANGELOG` ở mục 3 — đó là bản ghi viết **lúc làm việc**,
không phải suy lại. Phần **cân nhắc phương án bị loại** thì 🔴 **KHÔNG KHÔI PHỤC ĐƯỢC**: nó chỉ
tồn tại trong vết phiên và không được ghi vào tài liệu nào lúc đó.

## 5. Đã làm gì

| commit | ngày (giờ VN) | tệp | tổng |
|---|---|---|---|
| `7097d16` | 2026-08-25 18:39:18 | docs/_I2_DA_CHAY.json, web/backend/_v11027_so_muc_quan_tri.py | 2 files changed, 10 insertions(+), 1 deletion(-) |
| `110b05b` | 2026-08-25 18:37:44 | .AGENT.md, .Antigravityrules.md, .cursorrules, AGENTS.md, CHANGELOG.md, CLAUDE.md | 14 files changed, 511 insertions(+), 13 deletions(-) |

## 6. Cổng kiểm

🔴 **KHÔNG KHÔI PHỤC ĐƯỢC output cổng của phiên gốc** — cổng in ra `stdout`, không ghi tệp
(đúng khuyết tật `RM-15` mà `V11121` đã vá cho `cong_git_commit.py` bằng sổ điểm danh).

Điều **kiểm được hôm nay**, `26/08/2026`:

| phép | kết quả |
|---|---|
| commit của bản này còn trong `git log` | ✅ **2/2** còn nguyên, đều là tổ tiên của `origin/master` |
| khối `CHANGELOG` còn nguyên | ✅ 2,612 ký tự |
| bản này đã có báo cáo công khai chưa | ✅ **có, từ bản bù này** — trước đó `A55_VIOLATION_REPORT_MISSING` |

## 7. Vướng vấp

🔴 **KHÔNG KHÔI PHỤC ĐƯỢC** vướng vấp trong phiên gốc — không tài liệu nào ghi lại lúc đó.

Vướng vấp **của chính việc bù này**, ghi trung thực: bản bù dựng từ ba nguồn đương thời nhưng
**không thay được** một báo cáo viết lúc làm việc. Cụ thể mất: giờ từng thao tác · các phương án
đã cân nhắc rồi loại · lỗi gặp giữa chừng · trạng thái trước/sau của DB nếu phiên có chạm.

## 8. Gỡ về

Bản bù này **chỉ thêm tài liệu**, không đụng mã và không đụng dữ liệu ⇒ gỡ về =
`git rm -r V11117_LUAT_PRJ_INTERACTION_LEDGER_001_20260825/` rồi commit lại. Trạng thái quay về đúng như trước khi bù.

Việc gỡ về của **bản gốc `V11117`** nằm trong chính khối `CHANGELOG` ở mục 3 (nếu bản đó có ghi).

## 9. Theo dõi tiếp

| mã | việc | trạng thái |
|---|---|---|
| `FU-442` | vá cổng A55 — chính lỗ hổng làm bản này vô hình | ✅ **ĐÃ VÁ** ở `V11122`, thử chặn **11/11** |
| — | bù nốt các bản còn thiếu | trên **toàn dải từ mốc thi hành `V10921`** còn **32** bản thiếu báo cáo; 10 bản của đợt này là nhóm ưu tiên |
| — | ngưỡng đóng bằng số | `_v10921_report_gate.py` chạy **không tham số** ⇒ `V11117` không còn trong danh sách `THIẾU BÁO CÁO` |

---

## 10. BA LỚP NGUỒN (§62 · A60)

### `OWNER_SAID`
> *«PROMPT TỔNG LỰC LẦN 35 KIỂM TOÁN VÀ THAY PHƯƠNG PHÁP TOTAL/OUTPUT THỰC THI TRONG NGÀY 25/08/2026 Dùng multi-agent song song nhưng chỉ MỘT Coordinator hợp nhất. Không mở Plan/sổ cạnh tranh. Không mặc định 15 model tốt hơn 8 model. Không mặc định nhiều model tốt hơn ít model. Số lượng model chỉ là tồn kho. Chất lượng TOTAL phải được chứng minh bằng: - khả năng sinh số; - độ phủ; - xếp hạng; - đóng góp biên; - tính độc …»*
> — owner, **25/08/2026 12:52** (giờ VN)

> *«đang đo lường ah em? đợi kết quả hay sao?»*
> — owner, **25/08/2026 13:03** (giờ VN)

> *«còn đang chạy không em ? xong chưa push báo cáo tổng lực chưa em?»*
> — owner, **25/08/2026 14:26** (giờ VN)

> *«Đã push báo cáo hết chưa em? - Kiểm tra lại toàn bộ 1 lần nữa xem còn gì không để push báo cáo 1 lần luôn - Các vấn đề anh tương tác trực tiếp đã push thành 1 bảng ghi nhận yêu cầu của owner chưa ? Có cần cập nhật quy tắc trong claude.md để chuẩn hóa không vì đôi lúc code đi trước tài liệu do tương tác trực tiếp với em liên tục cho liền mạch ah em. Nên em claude code có thể đi trước tài liệu và việc ghi nhận các yêu …»*
> — owner, **25/08/2026 18:29** (giờ VN)

> *«Em hãy tiến hành đọc toàn bộ các phiên làm việc của claude code và cursor kết hợp báo cáo tổng hợp đính kèm và các thông tin audit báo cáo tất cả mọi thể chạy tổng lực tổng hợp lại một phiên tổng lực với đầy đủ tất cả các vấn đề không làm rơi rụng bất kỳ vấn đề nào, các vấn đề đã xử lý , có thể xử lý , tự xử lý rõ ràng , các yêu cầu của anh v.... không bỏ sớt bất kỳ điểm nào nha em. Em tiến hành xem toàn bộ các phiên…»*
> — owner, **25/08/2026 18:56** (giờ VN)


### `CODE_DID`
| điều mã **thực sự** làm | bằng chứng |
|---|---|
| 2 commit mang nhãn `V11117` | `7097d16`, `110b05b` — còn nguyên trong `git log`, đều là tổ tiên `origin/master` |
| tệp bị đụng | xem bảng mục 5 |
| bản này **chưa từng** có báo cáo công khai cho tới hôm nay | `_v10921_report_gate.py` liệt `V11117` trong `THIẾU BÁO CÁO` trước khi bù |

### `DOC_SAID`
| tài liệu | nói gì | khớp code chưa |
|---|---|---|
| `CHANGELOG.md` khối `## V11117` | 2,612 ký tự, viết đương thời | 🟢 **khớp** — commit tồn tại đúng ngày ghi |
| kho báo cáo công khai | **không có** thư mục `V11117_*` | 🔴 **LỆCH** — đã đóng bằng bản bù này |

### 🔴 BA LỚP LỆCH NHAU
`DOC_SAID` ≠ `CODE_DID`: mã đã chạy và đã commit, `CHANGELOG` đã ghi, nhưng **kho công khai không
có gì** suốt 1 ngày. Đó là `A55_VIOLATION_REPORT_MISSING`, và nó **vô hình** vì cổng chỉ soi 8
bản gần nhất — nay đã vá (`FU-442` · `V11122`).

---

**TanPhatAI cần làm:** ghi nhận đây là **báo cáo BÙ** viết ngày 26/08/2026 cho việc làm ngày
25/08, dựng từ **ba nguồn đương thời** (CHANGELOG 2,612 ký tự ·
2 commit · vết phiên), **không** phải bản viết lúc làm việc — mọi chỗ không khôi phục
được đã ghi thẳng là `KHÔNG KHÔI PHỤC ĐƯỢC`, **không** điền số ước.
