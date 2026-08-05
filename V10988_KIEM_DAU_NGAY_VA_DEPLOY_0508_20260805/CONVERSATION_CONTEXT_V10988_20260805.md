# Ngữ cảnh phiên V10988 — 2026-08-05

Ghi **nguyên văn** lời owner, agent đã làm gì theo thứ tự, và **vấp ở đâu**. Không diễn giải lại
lời owner.

---

## 1. Owner nói gì — nguyên văn

> **08:59 ngày 05/08/2026 (giờ Việt Nam):**
>
> *"Đầu ngày rồi đó em, kiểm tra tổng lực và deploy nếu cần đi chứ chờ đợi gì nữa?"*

**Đọc ra hai vế:**

1. **Kiểm tổng lực đầu ngày** — chạy đủ cổng tự kiểm, soi sức khoẻ hệ thống, soi trạng thái sống.
2. **Deploy những gì đang chờ** — *"chờ đợi gì nữa"* là câu then chốt. Phiên **V10987** hôm qua
   đã dựng xong phần lý thuyết của `C22` nhưng **không deploy được** vì được giao phạm vi
   *"phiên công cụ chạy ở máy local + tài liệu, KHÔNG deploy, KHÔNG restart `lottery`"*. Mục
   `FU-262` đến hạn **đúng hôm nay 05/08**. Owner nói *"chờ đợi gì nữa"* = đừng hoãn tiếp.

**Giờ chạy 09:0x** nằm **ngoài cả hai khung cấm deploy** (05:00–06:30 và 15:30–18:15) → được
phép deploy.

---

## 2. Agent đã làm gì — theo thứ tự

| # | Việc | Kết quả |
|---|---|---|
| 1 | Chạy **6 cổng tự kiểm TÁCH RIÊNG từng lệnh** (gộp lại từng bị cắt mất kết quả) | tất cả **thoát 0** |
| 2 | Kiểm `FU-266` — cổng báo cáo có xanh giả không | `HEAD` = `origin/main` = `628734e…`; V10987 **có thật** trên remote |
| 3 | Soi sức khoẻ VPS | health 200 · PID **801640 đúng như đã biết** · `NRestarts=0` · đĩa 69% · 0 traceback |
| 4 | Soi `monitoring.html` trên VPS | **577.617 byte** — nguyên vẹn |
| 5 | Dò trạng thái sống 05/08 bằng script `scp` lên VPS | MN chốt 05:19:51 · bt **25** · **15/15** |
| 6 | Đo **độ trễ `DA_XONG_BLOCK`** của MN | **12 giây** (hôm qua 17.754s) — **ĐẠT** |
| 7 | Đọc `_v10900_consistency_guard.py`, thiết kế `C22` | 3 điều kiện, mốc **cao nhất** |
| 8 | **Backup** vào `backups/v10988_pre/` | 5 tệp |
| 9 | Viết `C22` + bảng mốc `v10988_ui_moc` | 30.847 → 36.053 byte |
| 10 | **THỬ NGƯỢC** bằng tệp cụt thật 262.144 byte | **7/7 ĐẠT** |
| 11 | Deploy lên VPS, chạy `run_checks()` ngay | **22 phép**, `C22` = **OK** |
| 12 | Nghiệm thu cổng deploy `FU-207` | **2/2** ca bắt buộc, 6/6 toàn bộ |
| 13 | Chạy cổng lợi thế 3 miền × 3 cửa sổ | **9/9 ĐÓNG** |
| 14 | Ghi sổ theo dõi · CHANGELOG · SSOT · sổ quyết định `QD-026` | qua `prepend()` |
| 15 | Sinh lại lịch cuốn chiếu · cập nhật Playbook §1/§5 | 38.146 byte |
| 16 | **Restart `lottery`** + smoke + hash 4 bảng khoá | PID 801640 → **834969**, hash **y nguyên** |
| 17 | Chạy lại 6 cổng | *"đến hạn hôm nay"* **5 → 0** |

---

## 3. Vấp ở đâu — ghi đủ, kể cả lỗi do chính agent gây ra

### Vấp 1 — PowerShell băm nát lệnh nhồi qua SSH (**vấp HAI lần**)

Nhồi `python3 -c "..."` qua `ssh` từ PowerShell → nuốt dấu nháy, báo *"An expression was
expected after '('"*. Lần hai với vòng `for f in ...; do ... $(stat -c%s $p)` → *"$(subexpression)
is missing the closing ')'"*.

**Xử:** bỏ hẳn lối nhồi lệnh — viết tệp `.py` rồi `scp` lên VPS và chạy.

**Đáng nói:** đây **đúng là bẫy đã ghi sẵn** trong mục *"Mẹo vận hành đã học được"* của bộ quy
tắc (*"`python -c` in tiếng Việt lỗi mã hoá console → viết ra file script"*). **Biết mà vẫn
vấp**, nên ghi lại để lần sau đọc mục đó trước khi gõ.

### Vấp 2 — dò sai tên cột, suýt kết luận trên bản dò hỏng

Lượt dò đầu dùng ba tên cột **không tồn tại**: `final_bundles.numbers`,
`model_daily_eval.bach_thu_hit`, `predictions.region`. Tên thật lần lượt là `lo2`/`bach_thu`,
`bt_hit`, `target_region`.

**Hậu quả nếu bỏ qua:** ba mục lớn của phần kiểm (bạch thủ MN · chấm điểm 04/08 · số model chạy
hôm nay) sẽ **trống** trong báo cáo, hoặc tệ hơn là bị điền bằng phỏng đoán.

**Xử:** đọc `PRAGMA table_info` rồi dò lại bằng tên đúng. **Không con số nào trong báo cáo lấy
từ lượt dò hỏng.**

### Vấp 3 — bộ thử ngược cổng deploy đọc nhầm DB thật

Đưa `sqlite3`/`datetime` giả vào **globals của `exec`**, nhưng `MB_SCRIPT` tự
`import sqlite3, datetime` ở dòng đầu nên lượt import **ghi đè** bản giả → mở **DB thật** và
chết `unable to open database file`.

**Hậu quả nếu bỏ qua — đây là chỗ nguy hiểm nhất:** nếu máy local **có** DB thật thì bộ thử sẽ
**chạy được** nhưng đọc dữ liệu thật, cho kết quả **vô nghĩa mà trông như đạt**. Đúng loại xanh
giả đang đi diệt, chỉ khác là nằm trong chính bộ thử.

**Xử:** thay ở `sys.modules` trước khi `exec`, khôi phục trong `finally`.

### Vấp 4 — mệnh đề máy kiểm của `QD-026` báo TRÔI oan (tự gây)

Viết mệnh đề kiểm bảng mốc tải bằng `module: _v10982_lich9` + `bieu_thuc`. Chạy sổ quyết định →
**`QD-026` TRÔI 1/14**, `No module named '_v10982_lich9'`.

**Căn nguyên:** `_v10920_decision_ledger.py` chạy mệnh đề `module`/`bieu_thuc` **TRÊN VPS**, còn
`_v10982_lich9.py` là công cụ chạy ở **máy local**, không deploy. Mệnh đề đúng ý nhưng sai chỗ
chạy.

**Hậu quả nếu bỏ qua:** sổ quyết định đứng ở **TRÔI**, mà luật ghi rõ *"có mục TRÔI thì dừng, xử
trước khi làm việc mới"* → phiên sau bị chặn bởi một lỗi giả.

**Xử:** đổi sang `file_chua`. Chạy lại → **khớp 14/14**, 0 TRÔI.

**Bài học:** `module`/`bieu_thuc` chạy trên **VPS** — chỉ dùng cho module **có deploy**. Công cụ
chỉ chạy local phải kiểm bằng `file_chua` / `file_ton_tai`.

---

## 4. Chỗ agent CỐ Ý làm khác yêu cầu đã ghi — và nói rõ vì sao

`FU-262` viết nguyên văn: *"kích thước không tụt quá 10% **so với lần trước**"*.

**Agent làm khác:** so với **MỐC CAO NHẤT** (`v10988_ui_moc`, cập nhật bằng `MAX()`, chỉ đi lên).

**Vì sao:** làm đúng câu chữ thì một tệp bị cắt cụt chỉ báo đỏ **đúng một ngày** — hôm sau bản
cụt trở thành mốc mới và **cổng xanh trở lại** dù tệp vẫn hỏng. Đó **chính là loại xanh giả** mà
cả `FU-262` lẫn bảy mục cùng họ đang đi diệt. Nếu làm đúng câu chữ thì phép mới sẽ tái tạo đúng
cái bệnh nó sinh ra để chữa.

**Đã chứng minh, không nói suông:** bước 4 và bước 5 của bộ thử ngược tồn tại **chỉ để kiểm điều
này** — chạy lần thứ hai trên bản cụt **vẫn đỏ**, và mốc **vẫn giữ 577.617** chứ không tụt theo
bản cụt.

---

## 5. Chỗ agent KHÔNG làm, và vì sao — nói thẳng

### `FU-243` không đóng được đúng hạn

Ba thứ phải chạm để sửa — `bt_gate`, `MT_top13_V10752` (bộ lọc combo-super / bộ chọn model
production) và `expected_output_model_count` (con số công bố của đường ra số) — **đều nằm trong
5 thứ `QD-014` cấm đích danh** tới hết 08/08.

**Không có cách nào đóng đúng hạn 05/08 mà không phạm quy tắc owner đã ký.** Nên **dời sang
09/08** (ngày đầu tiên hết đóng băng) kèm lý do, thay vì nhắm mắt đóng cho đủ chỉ tiêu. Bảng mốc
tải đã cập nhật **cùng phiên** (nếu không thì cổng `J5` trượt ngay).

### `FU-256` chưa dời lượt vá dù `C19` đã LỆCH

`C19` LỆCH lần đầu ngày 04/08 (MT chốt cách hạn cứng **467 giây**, dưới ngưỡng đỏ 480s). Nhưng
`FU-256` **tự viết** là cần đọc `C19`+`C20` **đủ 2 ngày liên tiếp** (05/08 và 06/08) mới quyết.
Hôm nay mới có 1 ngày → **giữ mở đúng như mục đã ghi**, không tự ý hành động sớm.

### Không cắt model nào, không đụng vùng đóng băng

`QD-014` còn hiệu lực hết 08/08. Phiên này **không** chạm 15 model official, bộ lọc combo-super,
lớp ghi đè, `/du-doan` writer, `final_bundles` writer, bộ chọn model production. Hash 4 bảng khoá
**giống hệt trước/sau** là bằng chứng.

---

## 6. Phát hiện ngoài phạm vi yêu cầu — nhưng phải nói

**Hai cron mới của V10984 CHƯA TỪNG chạy thật.** Kiểm bằng máy: **không tồn tại**
`logs/v10945_edge_gate.log` lẫn `logs/v10984_ghep_lane.log`. Cron được đặt lúc ~22:0x ngày
04/08 — **sau** giờ chạy 19:00/19:10 của chính ngày đó. Nên các dòng ngày 04/08 trong
`edge_gate_daily` (`created_at` **22:36:44**) và `ghep_nt_official_daily` là **do chạy tay trong
phiên V10984**, không phải cron.

`FU-244` vẫn đóng **đúng** vì ngưỡng nó tự viết chỉ đòi *"có dòng cron"* + *"có dòng mới"* — cả
hai đều đạt. Nhưng **tối nay 05/08 mới là lượt cron đầu tiên**, phải xác nhận lại sau 19:10.
Nếu 06/08 vẫn không có tệp log thì **mở mục mới**.
