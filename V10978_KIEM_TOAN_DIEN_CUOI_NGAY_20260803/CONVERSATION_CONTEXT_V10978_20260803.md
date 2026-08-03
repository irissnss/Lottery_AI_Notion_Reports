# Ngữ cảnh phiên V10978 — 03/08/2026

Ghi lại **nguyên văn** lời owner, agent đã làm gì, và vấp ở đâu. Không diễn giải lại.

---

## 1. Owner nói gì (nguyên văn)

**19:03 ngày 03/08/2026, giờ Việt Nam:**

> *"Kiểm tra toàn diện tất cả các vấn đề của dự án anh tới thời điểm hiện tại dùm anh. ... Riết
> em mất kiểm soát dần thì phải"*

Ghi chú kèm theo khi giao việc:

> *"Owner đang MẤT NIỀM TIN. Ý chính: hệ thống có còn được kiểm soát chặt không, hay đang tuột
> dần. Phải trả lời bằng số, không đường mật, không biện hộ."*

Và về phần owner cần nhất:

> *"Owner nói 'riết em mất kiểm soát dần' — phải trả lời thẳng: đúng ở chỗ nào, không đúng ở
> chỗ nào."*

Ràng buộc được nêu rõ khi giao việc:

- `QD-014` đóng băng đường ra số tới hết **08/08**: cấm đổi 15 model official, combo-super
  filter constants, override toggles, `/du-doan` writer, `final_bundles` writer.
- `QD-013`: cổng lợi thế phải **≥ +3pp và z ≥ 2** mới đặt tiền thật.
- Notion **chỉ đọc** (§57).
- Có **agent khác chạy song song** (V10977) điều tra sự cố *"MB /nghiệm-thu hôm nay không
  output"* → **không được đào chồng**, chỉ ghi nhận và trỏ tham chiếu.
- Không `git add -A`; đọc lại docs ngay trước khi prepend; `git pull --rebase` trước khi push.
- **Không sửa production path chọn số.** Lỗi hạ tầng / docs / canh đo thì sửa được.

---

## 2. Agent đã làm gì, theo thứ tự

1. **Chạy 4 cổng tự kiểm, in mã thoát thật** — cả bốn exit **0**.
2. **Probe VPS lần 1** (`_v10978_audit_probe.py`, DB mở `mode=ro`): dịch vụ, đĩa, 4 bảng khoá +
   sha256, `tz_registry`, consistency guard, chuỗi output 30 ngày, cổng lợi thế, journal, crontab.
3. **Probe lần 2** (`_v10978_probe2.py`): đào 3 nghi vấn — cron cổng lợi thế, nguyên nhân
   `model_count < 15`, biên giờ chốt trôi. Quét luôn **102 bảng có cột `date`** xem bảng nào đứng.
4. **Probe lần 3** (`_v10978_probe3.py`): cờ tiền thật, P&L 30 ngày tự tính từ
   `final_bundles` × `lottery_results`, bảng rỗng ai định ghi, cron trỏ file không tồn tại.
5. **Đối chiếu giấy tờ:** `FOLLOW_UP_TRACKER.md` (240 FU, 111 treo), 4 file
   `ACTIVE_ROADMAP_*.md`, `OWNER_DECISION_LEDGER.md` (20 quyết định, 0 TRÔI), và trạng thái
   từng FU owner hỏi đích danh.
6. **Kiểm hai ngưỡng FU nghi đã chạm:** FU-245 (hook đầu phiên) và FU-250 (script thoát 0).
7. **Ghi 3 tài liệu quản trị** bằng `_doc_prepend.prepend()` — 4 mục FU mới + 4 mục cập nhật.
8. **Dựng bộ bằng chứng đã che khoá** rồi push riêng + công khai.

---

## 3. Vấp ở đâu

### 3.1 Vấp do agent gây ra

| # | vấp | hậu quả nếu bỏ qua | đã xử |
|---|---|---|---|
| 1 | Lệnh đầu tiên dùng cú pháp `cmd` (`cd /d … && …`) trong **PowerShell** → lỗi cú pháp ngay | Mất thời gian; nguy hiểm hơn là dễ tưởng cổng "đã chạy" trong khi chưa chạy | Chuyển cú pháp PowerShell, **in `$LASTEXITCODE` sau mỗi cổng** |
| 2 | Đoán sai tên cột **3 lần**: `predictions.region` (thật: `target_region`), `lottery_results.prizes` (thật: `prizes_json`), `scheduler_logs.status` (thật: `log_level`) | Probe chết giữa chừng. Mục `scheduler_logs` ở bản tóm tắt đầu in `ERR no such column` **mà vẫn hiện như một kết quả** — đúng loại "xanh giả" thu nhỏ | Đọc `PRAGMA table_info` trước rồi mới viết lại truy vấn |
| 3 | `python -c` in tiếng Việt hỏng mã hoá; PowerShell nuốt f-string nhiều dấu ngoặc | Đúng hai bẫy đã ghi sẵn trong `CLAUDE.md` mà vẫn giẫm phải | Viết hẳn script ra file có `sys.stdout.reconfigure(encoding="utf-8")` |
| 4 | **Suýt tự ý thêm cron cho `_v10945_edge_gate.py`** khi thấy `edge_gate_daily` chỉ có 1 dòng | Vi phạm §56 (làm lại việc đã ký), đụng crontab production trong lúc QD-014 đóng băng, và **giẫm chân agent V10977** đang thao tác cùng máy | Đọc kỹ FU-244, thấy V10975 **đã cân nhắc và ký lý do hoãn tới sau 08/08** → dừng lại, chỉ đo tươi để chứng minh khoảng trống chưa gây hại |

Vấp số 4 là vấp đáng ghi nhất: nếu không đọc lại FU-244 thì đã "sửa giúp" một thứ mà phiên
trước **cố ý không sửa**, và làm mất dấu vết quyết định.

### 3.2 Vấp của hệ thống, không phải của phiên

| # | vấp | ghi nhận |
|---|---|---|
| 5 | Tool `Read` không mở được file trong `artifacts/` (permission denied) | Phải in qua Python; không ảnh hưởng kết quả |
| 6 | `_v10920_session_start.py` đếm **79** mục treo, phép đếm rộng ra **111** | Chênh **32 mục** — dấu hiệu tracker có nhiều mục cũ ghi sai khuôn. Đã ghi vào SSOT để không ai hoảng khi thấy hai số khác nhau |

---

## 4. Những gì agent quyết định KHÔNG làm, và vì sao

| không làm | vì sao |
|---|---|
| Thêm cron cho `_v10945_edge_gate.py` | FU-244 đã ký lý do hoãn tới sau 08/08 (QD-014). Hạn 10/08 chưa tới. Đo tươi cho thấy 6/6 ô vẫn ĐÓNG → rủi ro tiền = 0 |
| Sửa `expected_output_model_count` trong `/api/health` | Chạm bề mặt công bố của đường ra số → QD-014 cấm tới 08/08 |
| Nối lại cron ghi `pnl_daily_*` | Chưa chốt bảng nào là nguồn P&L chính thức; nối bừa tạo hai nguồn sự thật → mở FU-254 để chốt trước |
| Xoá 4 bảng rỗng | Xoá schema là thao tác một chiều, phải xác nhận không module nào định dùng lại → mở FU-255 |
| Sửa `.cursor/hooks.json` | Chưa chứng minh được nguyên nhân hook im; sửa mò dễ che mất triệu chứng thật |
| Đào sự cố MB `/nghiệm-thu` | **V10977 đang xử** — tránh trùng lặp và tránh sửa đụng cùng file |
| Đóng FU-250 luôn | Bằng chứng đã đủ (0 nơi gọi 3 script), nhưng hạn là 06/08 và việc thuộc phiên đó; ghi bằng chứng lại để phiên sau quyết nhanh |

---

## 5. Kết quả cuối, gọn

- **Verdict:** hệ chưa mất kiểm soát ở tiền và đường ra số; **tầng canh gác thì đang tuột**.
- **4 cổng tự kiểm:** exit 0 cả bốn.
- **Chuỗi output 30 ngày:** 90/90 ô — 0 thiếu, 0 trễ, 0 rỗng; **57 ô thiếu phiếu**.
- **Cổng lợi thế:** 6/6 ĐÓNG. **Tiền thật đang mở: 0 đồng.**
- **P&L 30 ngày mô phỏng:** −931.000đ (−23,5%).
- **Mở mới:** FU-254 · FU-255 · FU-256 · FU-257. **Cập nhật:** FU-243 · FU-244 · FU-245 · FU-250.
- **Không sửa file runtime nào, không deploy, không restart.**
