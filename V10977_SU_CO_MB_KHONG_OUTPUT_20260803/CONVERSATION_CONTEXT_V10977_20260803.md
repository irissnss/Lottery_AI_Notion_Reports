# CONVERSATION CONTEXT — V10977 · 03/08/2026

Ghi lại **nguyên văn** lời owner, agent đã làm gì theo thứ tự, và vấp ở đâu. Không diễn giải lại
lời owner, không làm đẹp phần vấp.

---

## 1. Lời owner — nguyên văn

**03/08/2026, 19:03 (giờ VN)**, giọng rất khó chịu:

> *"MB /nghiem-thu này không output là sao em? ly do gi sao ma tao lao the em? Riet em mat kiem
> soat dan thi phai"*

Bối cảnh lúc owner nhắn: hạn output MB là **17:58**, lúc đó đã **19:03** — quá hạn hơn một tiếng
mà owner mở trang vẫn không thấy số MB.

Owner **không ra quyết định** và **không chọn phương án nào**. Owner báo sự cố, và nêu mối lo lớn
hơn bản thân sự cố: *"riết em mất kiểm soát dần thì phải"* — tức hệ đang trôi tới chỗ owner phải
là người phát hiện lỗi thay vì máy. Toàn bộ hướng xử lý bên dưới do agent đề xuất và tự chịu
trách nhiệm.

---

## 2. Agent đã làm gì, theo thứ tự

| # | Việc | Kết quả |
|---|---|---|
| 1 | Chạy `_v10920_session_start.py` (bắt buộc đầu phiên) | 0 checkpoint quá hạn · 79 mục treo, 0 quá hạn → được vào việc |
| 2 | Tìm `/nghiem-thu` là gì | trang `web/frontend/nghiem-thu.html` ← API `/api/nghiem-thu` (`require_admin`) ← `_v10879_nghiemthu_lane.compute_view()` ← bảng `du_doan_test_bundles` (`{REGION}_NGHIEMTHU_1908_V1`) + `v10879_nghiemthu_scoreboard` |
| 3 | Đọc `LANE_SCHEDULE` | thấy ngay `final` MT 16:53 / MB 17:53 — **stale**, V10931 đã dời sang 16:58/17:58 |
| 4 | Probe VPS lần 1 (chỉ đọc) | official MB **CÓ** (id 641, BT 59, chốt **17:44:54**) · lane MB **KHÔNG CÓ** · cron MB chạy 17:38 và 17:42 |
| 5 | Probe lần 2 | chết vì đoán sai tên cột `predictions` (`region` → thật ra `target_region`) |
| 6 | Probe lần 3 | log lane dòng 2118 + 2187: `CHƯA ĐỦ ĐIỀU KIỆN · official chưa chốt miền này`. Bảng biên 34 ngày: **02/08 chỉ 9 GIÂY** |
| 7 | Tra `tz_registry` trước khi đọc dấu thời gian | `final_bundles` / `predictions` / `du_doan_test_bundles` = **VN** (đọc thẳng) · `scheduler_logs` = **UTC** |
| 8 | Loại trừ | không restart (PID 645169 liên tục) · không deploy trong khung cấm · có `no-store` · MN/MT bình thường |
| 9 | Backup + hash trước | `backups/v10977_pre/` 4 file + crontab 121 dòng; hash 4 bảng khoá |
| 10 | Sửa 4 file | lane (mốc FINAL + `last_run` + `_pending_reason`) · tự kiểm (C17 + C18) · 2 trang |
| 11 | Cập nhật docs bằng `_doc_prepend.prepend()` | CHANGELOG +3.763 · SSOT +2.134 · FU +2.318 — cả ba **dài ra** |
| 12 | Ghi sổ quyết định | **OD-20260803-B**, 5 mệnh đề máy kiểm được |
| 13 | Deploy lượt 1 (19:2x, ngoài khung cấm) | 4 file + 5 lượt cron vá · PID 645169 → 737795 · health 200 · 0 traceback |
| 14 | Kiểm sau deploy | C17 kêu đúng · C18 xanh · **không sinh số bù** (0 dòng) · hash 4 bảng **giữ nguyên** |
| 15 | Phát hiện câu chữ mình vừa viết bị sai (mục 3.1) | sửa + deploy lượt 2 · PID 737795 → 738032 |
| 16 | Gom bằng chứng, viết báo cáo, push riêng + công khai | — |

---

## 3. Vấp ở đâu

### 3.1 Vấp nặng nhất — agent tự viết một câu chẩn đoán SAI rồi suýt để nguyên

Trong `_pending_reason()` bản đầu, nhánh "official chốt trước lượt cuối mà lane vẫn trống" viết
thẳng:

> *"Đây là lỗi khác (không phải trôi giờ), phải soi logs/v10879_nghiemthu.log."*

Kiểm sau deploy lượt 1 thì MB 03/08 rơi đúng vào nhánh đó — vì `last_run` lúc ấy đã là **17:54**
(lịch MỚI vừa thêm trong chính phiên này), còn lượt cuối THẬT của hôm nay là **17:42** (lịch CŨ).
Câu chữ thành ra chỉ sai hướng: nói "không phải trôi giờ" trong khi nguyên nhân **đúng là** trôi
giờ.

Trớ trêu: đây chính là loại lỗi "trang nói dối người xem" mà cả phiên đang đi sửa, và agent tự tay
tạo thêm một cái. Đã sửa để câu chữ chỉ nói phần chắc chắn (official chốt lúc nào · lane trống ·
hôm nay không có số) rồi trỏ vào log, **không tự chẩn đoán**.

**Bài học:** đổi hằng số lịch trong cùng phiên thì mọi câu chữ suy ra từ hằng số đó chỉ đúng cho
NGÀY MAI. Nó không mô tả được hôm nay.

### 3.2 Suýt gộp hai lỗi khác nhau làm một

`MB_DEHERD_V1` ngày 03/08 cũng trống. Rất dễ kết luận "cùng một nguyên nhân, sửa cron là xong".
Đo kỹ mới thấy lane de-herd chết vì `sqlite3.OperationalError: database is locked` lúc 17:42:01
(5 cron đè nhau khung 17:40–17:43), hoàn toàn khác cổng `_official_gate`. Đã tách thành **FU-253**
thay vì tuyên bố xong.

### 3.3 Đoán tên cột thay vì đọc schema

Probe chết hai lần: `predictions` không có cột `region` (thật ra là `target_region`) và không có
`model_name` (thật ra là `ai_model`). Mất hai vòng probe. Lần sau đọc `PRAGMA table_info` trước.

### 3.4 Chuông đã có sẵn mà agent suýt không thấy

`_v10891_deadline_guard` **đã đếm đúng** từ đầu: `V10891_GUARD 2026-08-03: 55 mục · trễ 0 · chưa
có 1`. Nghĩa là máy **biết** có một mục thiếu. Nhưng nó chỉ in con số, không nêu tên mục, và chỉ
ghi vào file log. Suýt nữa kết luận "hệ hoàn toàn mù" và đi dựng bộ đo mới từ đầu — trong khi bộ
cũ đo đúng, chỉ thiếu đường phát tín hiệu. Đã ghi vào FU-252 để cân nhắc cho nó nêu tên mục.

### 3.5 PowerShell

Lệnh đầu tiên dùng `&&` — PowerShell không nhận. Chuyển sang cú pháp PowerShell. Commit vẫn bọc
trong file `.cmd` theo quy tắc đã ghi.

---

## 4. Những chỗ agent CHỦ ĐỘNG KHÔNG làm, và vì sao

| Không làm | Vì sao |
|---|---|
| **Không sinh số bù cho MB 03/08** | 19:2x đã quá mốc FINAL 17:58 và đã xổ ~18:31. Sinh số lúc này là số *sau khi biết kết quả* — phá quy tắc đóng băng và đầu độc chính phép đo tới mốc 19/08 |
| Không nới cổng `_official_gate` | Đó chính là bài học 30/07: lane từng chốt bừa `43` từ 7 model rồi tối tính lại thành `86`. Cổng đúng, chỉ thiếu chuông |
| Không đụng vùng đóng băng QD-014 | 15 model official · combo-super filter · override · `/du-doan` · writer `final_bundles` · bộ chọn production — không sửa gì, không deploy `main.py` |
| Không sửa `_v10891_deadline_guard` ngay | C17 đã phủ được việc cần kíp; sửa thêm trong cùng phiên là mở rộng phạm vi không cần thiết. Ghi FU-252 |
| Không dời giờ hàng loạt để chữa DB lock | Dời bừa có thể đẩy job khác qua biên lane 17:56. Cần đo tần suất trước → FU-253 |
| Không `git add -A` | Có agent khác chạy song song V10978. Chỉ stage đúng file của V10977 |

---

## 5. Trả lời thẳng câu owner hỏi

**"MB /nghiem-thu này không output là sao em?"**
→ Đúng, MB **không có số** ở luồng Nghiệm Thu ngày 03/08. Official MB thì có bình thường (BT **59**,
chốt 17:44:54) — chỉ luồng thứ 5 mất.

**"lý do gì sao mà tào lao thế em?"**
→ Lane chỉ chạy hai lượt 17:38 và 17:42, mà cổng chỉ mở khi official đã chốt. Hôm nay official chốt
**17:44:54** — muộn hơn lượt cuối **2 phút 53 giây**. Hết lượt trước khi cổng mở.

**"Riết em mất kiểm soát dần thì phải"**
→ Owner nói đúng, và đây là phần nghiêm trọng hơn cả sự cố. Bộ tự kiểm báo **16/16 OK** đúng cái
ngày MB trắng, vì nó chỉ kiểm *cấu hình giờ* chứ không kiểm *có output thật*. Biên an toàn đã mỏng
tới **9 giây** hôm 02/08 mà không phép kiểm nào kêu. Đã thêm C17 (miền trống sau mốc FINAL) và C18
(biên mỏng dưới 300 giây) để lần sau máy kêu trước owner.
