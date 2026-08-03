# Bối cảnh hội thoại — V10976 (03/08/2026)

Phiên: sửa 5 lỗi Bugbot tìm được ở **tầng cổng tự kiểm**, rồi chạy lại để xem **số thật**.

---

## 1. Owner nói gì — nguyên văn

> *"sửa hết 5 lỗi ở tầng cổng tự kiểm, rồi chạy lại ledger/gate để xem SỐ THẬT."*

> *"Bugbot vừa rà code và tìm 5 lỗi — tất cả nằm trong chính các cổng tự kiểm, nghĩa là hệ có
> thể báo xanh giả. Đây là vấn đề nghiêm trọng về niềm tin: nhiều phiên qua đã báo owner 'gate
> PASS / ledger 0 TRÔI' dựa trên những cổng này."*

> *"Nếu số thật xấu hơn số cũ → BÁO THẬT, không che. Đây là điểm quan trọng nhất owner muốn
> biết."*

> *"Nếu phát sinh TRÔI / lệch quy tắc thật: sửa được trong freeze thì sửa (docs/quy tắc), không
> thì mở FU kèm mã đọc §58 + hạn."*

> *"Deploy VPS chỉ nếu ba script này có chạy trên VPS (cron). Nếu chỉ dùng local thì không
> deploy — ghi rõ trong báo cáo."*

Ràng buộc owner nhắc lại trong phiên:

> *"QD-014 đóng băng tới hết 08/08: CẤM đụng 15 model official, combo-super filter constants,
> override toggles, `/du-doan` writer, `final_bundles` writer, bộ chọn model production. Năm lỗi
> trên chỉ ở tầng kiểm soát → sửa được trong freeze."*

> *"Có một agent khác đang chạy song song làm 'kiểm đầu ngày 03/08' và sẽ đẩy báo cáo V10975 +
> prepend CHANGELOG/SSOT/FOLLOW_UP. Để tránh đạp nhau: bạn dùng version V10976. KHÔNG `git add
> -A` / `git add .` — chỉ stage đúng file của mình."*

---

## 2. Năm lỗi Bugbot nêu (nguyên văn rút gọn từ đề bài)

| Mã | Mức | Nội dung |
|---|---|---|
| L1 | HIGH | `_v10920_decision_ledger.py` ~218 — phép `kiem_code` đầu của `OD-20260801-H` khai là kiểm "sáu mặt quy tắc đồng bộ + file chết + `.mdc` tự nạp" nhưng handler local **chỉ kiểm file script có tồn tại**. *"Không chạy script, không đọc kết quả → ledger vẫn hiện 🟢 KHỚP (5/5) dù quy tắc thật đã lệch."* |
| L2 | MEDIUM | ~75 — mục có `trung_voi` luôn `dat=None`, không thừa hưởng kết quả. *"`OD-20260801-D` trỏ tới `OD-20260801-A` mãi ⚪ 'không kiểm được' dù A đã 🟢."* |
| L3 | MEDIUM | `_v10920_session_start.py` ~189 — mục [6] còn soi **3 mặt** và gọi là "BA MẮT QUY TẮC", trong khi luật đã lên **năm mặt**. *"Sửa hai file đó không hề cảnh báo."* |
| L4 | MEDIUM | `_v10921_report_gate.py` ~82 — in lỗi nhưng **luôn exit 0**. *"CẨN THẬN: soi xem có ai gọi script này rồi dựa vào exit code không."* |
| L5 | MEDIUM | `_v10920_decision_ledger.py` ~201 — probe thiếu `JSON_START` thì log rồi **return exit 0**, giữ nguyên `.md` cũ. *"Owner tưởng đã kiểm tươi."* |

---

## 3. Agent đã làm gì, theo thứ tự

1. **Đọc ba file + bộ kiểm quy tắc, xác nhận từng lỗi bằng dòng code thật** trước khi động vào
   (bảng §3.1 của báo cáo).
2. **Soi ai đang gọi bốn script** — `.cursor/hooks.json`, hook `session_start_briefing.py`,
   cron VPS, toàn bộ repo. Kết luận: **không luồng nào đọc mã thoát cũ**, nên đổi mã thoát an
   toàn. Vẫn thêm cờ `--soft`.
3. **Kiểm bốn script có trên VPS không** — `ls` báo *No such file or directory* cả bốn, `crontab -l`
   không dòng nào. → **không deploy**.
4. **Backup 6 file** vào `backups/v10976_pre/*.pre`.
5. **Sửa L1→L5**, cộng hai điểm cùng loại phát hiện trong lúc làm (file quy tắc 0 byte không
   tính là trượt; bộ kiểm tự ghi đè `AGENTS.md`).
6. **Kiểm âm từng lỗi** — bẻ `AGENTS.md` cho lệch thật, chạy **cả bản cũ lẫn bản mới** trên cùng
   hoàn cảnh; giả lập probe VPS hỏng. Khôi phục nguyên trạng sau mỗi phép đo.
7. **Chạy lại thật bốn lệnh**, chụp bằng chứng UTF-8, đếm bằng máy.
8. Ghi hồ sơ quản trị (prepend CHANGELOG/SSOT/FOLLOW_UP bằng `_doc_prepend.prepend()`), ghi
   quyết định owner **OD-20260803-A**, mở **FU-250** và **FU-251**.
9. Đẩy báo cáo công khai + chạy cổng kiểm báo cáo.

---

## 4. Vấp ở đâu — ghi đủ, kể cả vấp do agent tự gây

### 4.1 Bằng chứng đầu tiên không đọc được (tự gây)

Hứng output bằng `*>` của PowerShell. File ra **UTF-16** và chữ tiếng Việt **đã bị console bóp
méo trước khi ghi**: `khớp` thành `khß╗¢p`. Bộ đếm đọc ra **0** ở mọi ô — bảng trước/sau toàn số 0.

Đã xử: viết `_v10976_bang_chung.py` hứng qua `subprocess` của Python với `encoding="utf-8"`,
thu lại toàn bộ. **Hậu quả nếu bỏ qua:** báo cáo dẫn "bằng chứng" mà owner mở ra không đọc được.

### 4.2 Tự dẫm vào bẫy đã ghi sẵn trong quy tắc (tự gây)

Dùng `python -c` in tiếng Việt → `UnicodeEncodeError: 'charmap' codec … cp1252`. Đúng dòng đã có
trong bảng *"Mẹo vận hành đã học được"* của `CLAUDE.md`: *"`python -c` in tiếng Việt lỗi mã hoá
console → viết ra file script có `sys.stdout.reconfigure(encoding='utf-8')`."*

### 4.3 Suýt tạo ra một lỗi xanh giả MỚI (tự gây, nguy hiểm nhất)

Bản đầu của L1 định gọi `_v10925_rule_sync_check.py` ở **chế độ mặc định** — mà chế độ đó **ghi
đè `AGENTS.md`** từ `CLAUDE.md`. Nếu để vậy thì mỗi lần sổ quyết định chạy, nó tự sửa đúng thứ
nó đang kiểm, và hệ **luôn luôn** báo "đồng bộ". Tinh vi hơn cả lỗi L1 đang sửa.

Đã xử: thêm chế độ `--check` chỉ đọc, bắt sổ quyết định gọi đúng chế độ đó.

### 4.4 Thông báo lỗi vô nghĩa (tự gây)

`chay_bo_kiem()` lấy "dòng cuối khác rỗng" làm lý do trượt → in ra một dãy `====`. Cổng bắt đúng
lỗi nhưng owner không biết lỗi gì. Đã lọc bỏ dòng chỉ toàn `=`/`-`.

### 4.5 Số nền đầu tiên không so được (do chạy song song)

Bản chụp `TRƯỚC` của cổng báo cáo chạy lúc agent V10975 **chưa** thêm khối V10975 vào CHANGELOG.
Nếu để nguyên thì chênh lệch exit 0 → 1 có thể bị hiểu là *do V10975 xuất hiện*, chứ không phải
*do sửa code*. Đã chạy lại **bản cũ** trên **đúng trạng thái repo hiện tại** để so đúng một hoàn
cảnh: bản cũ exit **0**, bản mới exit **1**.

### 4.6 `artifacts/` nằm trong `.cursorignore`

Công cụ đọc file của agent không mở được thư mục bằng chứng vừa ghi. Đã chép bằng chứng sang
thẳng `evidence/` của repo báo cáo công khai rồi mới soi lại.

### 4.7 Va chạm với agent chạy song song — không xảy ra

Prepend ba tài liệu quản trị bằng `_doc_prepend.prepend()` (đọc xong mới ghi, từ chối nếu file
ngắn đi), rồi kiểm ngay sau khi ghi: cả ba file còn đủ khối **V10976 · V10975 · V10974**. Không
dùng `git add -A`.

---

## 5. Kết quả cuối — số thật

| | TRƯỚC | SAU |
|---|---|---|
| Sổ quyết định | 19 mục · **17 🟢 · 2 ⚪ · 0 TRÔI** · exit 0 | 20 mục · **19 🟢 · 1 ⚪ · 0 TRÔI** · exit 0 |
| `OD-20260801-H` | 🟢 5/5 — **nhưng là xanh giả** | 🟢 5/5 — **có chạy thật** |
| `OD-20260801-D` | ⚪ không kiểm máy | 🟢 khớp 1/1 (thừa hưởng từ `OD-20260801-A`) |
| Năm mặt quy tắc | không ai canh `CLAUDE.md` / `AGENTS.md` | đồng bộ **thật** · kiểm âm bẻ `AGENTS.md` → bắt được |
| Cổng báo cáo | exit **0** dù in ✗ | exit **1** — bắt **V10975 chưa có báo cáo công khai** |
| Deploy VPS | — | **Không** (bốn script không có trên VPS, không cron) |

**Số không xấu đi.** Điều xấu nằm ở chỗ khác: **trước đây một phần các số đó không được đo thật**.
