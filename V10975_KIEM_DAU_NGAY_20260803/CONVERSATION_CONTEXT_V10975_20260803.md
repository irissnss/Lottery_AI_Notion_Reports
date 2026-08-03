# CONVERSATION CONTEXT — V10975 (03/08/2026)

Ghi nguyên văn lời owner trong phiên, agent làm gì, và vấp ở đâu. Không diễn giải lại lời owner.

---

## 1. Owner nói gì — nguyên văn

> **"Kiểm tra đầu ngày dùm anh"**

*(sáng 03/08/2026, giờ Việt Nam)*

Đó là toàn bộ lời owner trong phiên. Phần còn lại của yêu cầu do phiên điều phối triển khai thành khung việc 6 bước: briefing đầu phiên → sổ quyết định → trạng thái sống 03/08 → việc tới hạn hôm nay → đối chiếu việc đóng hôm qua → ghi nhận + báo cáo.

## 2. Ràng buộc owner đã ký từ trước, còn hiệu lực trong phiên

> **QD-014** *(owner ký 01/08)* — *"Đóng băng đường ra số công bố tới hết 2026-08-08"*
> Cấm đổi 15 model official · hằng số lọc combo-super · các cờ ghi đè · writer `/du-doan` · writer `final_bundles`.

> **§57 / A55** *(owner ký 01/08 11:04)* — *"thống nhất quy tắc Mô hình code, fix, audit của dự án anh là sau khi thực hiện code, fix, audit cần đẩy báo cáo report lên github report public dùm anh, cập nhận, ghi nhận quá trình, yêu cầu thật cụ thể chi tiết để kiểm soát tốt nhất nha em, Notion MCP dùng để tham khảo tài liệu khi cần không được cập nhật vào Notion nha em."*

> **§56 / A54** *(owner ký 01/08 10:41)* — *"Anh không muốn nhắc tới nhắc lui hoài những vấn đề mà em có thể tra ra, có thể kiểm soát được đâu? ... em phải tư duy để có mối liên hệ chặt chẽ giữa báo cáo, giữa tài liệu, giữa code để kiểm soát chứ em."*

> **QD-013** *(owner ký 01/08 19:30)* — dừng đặt tiền thật cho tới khi chứng minh được lợi thế; ngưỡng hơn bừa **≥3pp** và **z ≥2**.

Phiên này **không phát sinh quyết định mới nào của owner**, nên không thêm mục vào `docs/OWNER_DECISION_LEDGER.json`.

---

## 3. Agent làm gì, theo thứ tự

| # | Việc | Kết quả |
|---|---|---|
| 1 | `python web/backend/_v10920_session_start.py` | 0 checkpoint quá hạn · 0 roadmap chờ archive · 79 FU treo (quá hạn 0) · 0 quyết định tới hạn rà soát · ba mặt quy tắc không lệch |
| 2 | `python web/backend/_v10920_decision_ledger.py` | **19/19 khớp · 0 TRÔI** |
| 3 | Probe VPS vòng 1 (`_v10975_dau_ngay_probe.py`) | health 200 · PID 645169 · journal 0 traceback · **4 query sai cột** |
| 4 | Lấy schema thật (`_v10975_dau_ngay_probe2.py`) | `target_region`, `source_predictions_json`, `computed_at_vn`, `log_level` |
| 5 | Probe vòng 3 (`_v10975_dau_ngay_probe3.py`) | MN chốt 05:20:15 đủ 15/15 · kết quả 02/08 đủ · MDE 27×3 · tự kiểm 16/16 · **edge_gate_daily đứng ở 01/08** |
| 6 | So file frontend (`_v10975_fe_diff.py`) | **0 dòng khác / 4002 dòng** — lệch byte chỉ do CRLF vs LF |
| 7 | Tính tươi cổng lợi thế (`_v10975_edge_lane_final2.py`) | ĐÓNG cả 6 ô (30d + 90d) · xác nhận **không ghi thêm dòng nào** |
| 8 | Quét lane hết hạn lần 1 | **ra 0 — SAI**, thiếu cột `run_date` |
| 9 | Quét lại (`_v10975_lane_rescan.py`) | 97 dòng từ 31/07 · xu hướng 68 → 19 → 10 → 0 |
| 10 | Truy thủ phạm (`_v10975_who_fires.py`) | **`_mb_advanced_lane_daily.sh` gọi thẳng `_v10679` + `_v10680`** |
| 11 | Đối chiếu kết quả 02/08 (`_v10975_result_sanity.py`) | 3/3/1 đài khớp 6 Chủ Nhật gần nhất · BT **3/3 WIN** |
| 12 | Chạy tay hook đầu phiên | file briefing tươi lại từ 01/08 23:05 → 03/08 09:00 |
| 13 | Ghi 3 tài liệu quản trị (`_v10975_docs_update.py`) | +3.098 / +1.162 / +7.068 ký tự, dùng `prepend()` |
| 14 | Viết báo cáo công khai V10975 | file này + `REPORT_V10975.md` + `evidence/` |

**Không deploy. Không restart. Không sửa file nào trên VPS. Không ghi dòng nào vào DB. Không gọi hàm ghi Notion nào.**

---

## 4. Vấp ở đâu — kể cả vấp do chính agent gây ra

### 4.1 Suýt báo cáo sai theo hướng trấn an *(nghiêm trọng nhất)*

Script quét lane hết hạn của em nhận diện cột ngày theo danh sách `("date", "date_str", "target_date", "day")` — **thiếu `run_date`**, đúng là cột mà các bảng `du_doan_test_*` dùng. Kết quả trả về **0 dòng**.

Nếu tin con số đó, em đã báo với owner rằng *"lane hết hạn đã sạch, FU-189 tự khỏi"* — trong khi thực tế có **97 dòng** từ 31/07 và hai lane MB vẫn chạy đều mỗi ngày. Sai theo hướng làm owner yên tâm là loại sai tệ nhất.

Bắt được là nhờ đối chiếu ngược với `fu189_retired_detail.json` của V10974 hôm qua — báo cáo cũ ghi rõ hai lane đó ghi lúc 02/08 17:43, mâu thuẫn với kết quả 0 của em. Quét lại với `run_date` thì ra đúng.

**Bài học:** khi kết quả quét ra 0 mà báo cáo trước đó nói khác, phải nghi công cụ trước khi nghi dữ liệu.

### 4.2 Đoán tên cột thay vì đọc schema

Vòng query đầu dùng `predictions.region`, `final_bundles.bundle_json`, `v10900_consistency_guard.created_at`, `scheduler_logs.status` — cả bốn đều sai, trả `Error: no such column`. Mất một vòng. Lẽ ra đọc `pragma_table_info` trước.

### 4.3 Bốn hash giả giống hệt nhau mà không nghi ngay

Lệnh băm 4 bảng khoá vòng đầu trả `e3b0c44298fc1c14` cho **cả bốn** bảng. Đó là SHA256 của **chuỗi rỗng** — heredoc `.mode csv` trong `sqlite3` không nuốt được lệnh nên `sha256sum` băm rỗng. Bốn bảng khác nhau hoàn toàn mà ra cùng một hash thì phải nghi ngay lập tức, nhưng em chỉ phát hiện khi rà lại. Đã sửa sang `sqlite3 -csv`.

### 4.4 Nhồi script vào `python -c` — đúng cái bẫy đã ghi trong CLAUDE.md

Hai lần chạy `python -c` với chuỗi truyền qua `json.dumps` bị `SyntaxError: unexpected character after line continuation character` — ký tự `\n` vào tới shell thành hai ký tự literal. Bảng "mẹo vận hành đã học được" trong `CLAUDE.md` đã ghi rõ *"viết ra file script"*, em vẫn vấp. Đã chuyển sang upload script tạm vào `/tmp` qua SFTP, chạy xong `rm -f` ngay.

### 4.5 Tưởng ghi hỏng file tiếng Việt

Sau khi chạy hook, `Get-Content` hiển thị `KI��,M �?���U PHIASN` làm em tưởng đã ghi hỏng `_BRIEFING_DAU_PHIEN.txt`. Thực ra file hoàn toàn đúng UTF-8 — PowerShell 5.1 đọc theo bảng mã ANSI. Đọc lại bằng công cụ đọc file thì bình thường.

### 4.6 Dùng `&&` trong PowerShell

Hai lệnh đầu tiên của phiên dùng `cd ... && python ...`, PowerShell từ chối: *"The token '&&' is not a valid statement separator in this version."* Nhỏ, nhưng mất một lượt.

### 4.7 Chưa giải được — vì sao hook `sessionStart` không chạy

Đã kiểm: `.cursor/hooks.json` khai báo đúng (`python .cursor/hooks/session_start_briefing.py`, timeout 100), script chạy tay ra kết quả đúng, file ghi ra đúng chỗ. Nhưng dấu thời gian trong file cho thấy nó **không chạy suốt 02/08 và 03/08**. Nguyên nhân nằm ở phía Cursor có kích hoạt hook hay không — ngoài tầm soi trong phiên.

Em **không sửa mò** `.cursor/hooks.json`, vì chưa biết nguyên nhân thì sửa chỉ thêm biến. Đã ghi **FU-245** với phép thử cụ thể cho sáng mai: mở file, xem dấu thời gian có phải ngày hôm đó không.

---

## 5. Ba chỗ hở mới tìm ra và vì sao không sửa ngay

| Chỗ hở | Vì sao không sửa trong phiên |
|---|---|
| **Cổng lợi thế không ghi ngày** (`edge_gate_daily` đứng ở 01/08) | Thêm cron = đụng crontab production trong cửa sổ đóng băng QD-014. Mà thiệt hại thực tế **bằng không**: panel vẫn tính tươi nên màn hình không sai, bảng này là bảng chẩn đoán không có đường ra số công bố → **FU-244** hạn 10/08 |
| **Lane hết hạn còn ghi** (`_mb_advanced_lane_daily.sh` gọi `_v10679`/`_v10680`) | Sửa `.sh` + crontab = đụng production trong cửa sổ đóng băng. Mức hại đo được là **thấp** (`official_tables_touched: 0`, `output_impact: False`), xu hướng đang tự giảm 68 → 19 → 10 → **FU-185** dời hạn 10/08 |
| **Hook đầu phiên im 2 ngày** | Không thuộc production, nhưng **chưa biết nguyên nhân**. Đã làm việc làm được ngay: chạy tay cho file tươi lại → **FU-245** hạn 04/08 |

---

## 6. Điều đáng mừng trong phiên

- Bạch thủ ngày 02/08 **thắng cả ba miền**: MN `43` · MT `69` · MB `52`.
- Hệ chạy **14 giờ 37 phút liên tục không lỗi**, 0 traceback, 0 dòng ERROR.
- MN chốt **đúng giờ, đủ 15/15 model**, không phải bản dự phòng.
- Bốn mục FU-184 / FU-189 / FU-242 / FU-243 mà V10974 đóng hôm qua đều đã ghi **đúng** trong tracker — đối chiếu không lệch chỗ nào.

Cần nói thẳng một điều để khỏi hiểu nhầm: **thắng 3/3 hôm qua không phải bằng chứng hệ có lợi thế.** Cổng lợi thế đo trên 90 ngày vẫn **âm cả ba miền** (MN −0,21pp · MT −2,81pp · MB −7,04pp), không ô nào tới ngưỡng owner đặt. Một ngày đẹp là may, đúng như kết luận V10970 đã ghi.

---

*Ghi 03/08/2026 · mọi mốc giờ là giờ Việt Nam (`Asia/Ho_Chi_Minh`, UTC+7).*
