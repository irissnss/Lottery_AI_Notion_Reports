# REPORT V10980 — KIỂM TOÀN DIỆN ĐẦU NGÀY 04/08/2026

- **Phiên:** V10980 · **Ngày:** 04/08/2026 (giờ Việt Nam, `Asia/Ho_Chi_Minh`)
- **Khung giờ làm:** 09:49 → 10:25
- **Loại việc:** kiểm toàn diện đầu ngày + vá cổng đếm việc (không đụng đường ra số)
- **Đụng production:** **KHÔNG** — 0 file runtime bị sửa · 0 deploy · 0 restart · QD-014 nguyên vẹn
- **Chạy song song:** phiên **V10979** đang thiết kế lại nhịp chạy cuốn chiếu 5 model AI. Phiên
  này **không chạm** việc đó, chỉ ghi nhận để owner biết hai luồng khác nhau.

---

## 1. Tóm tắt một đoạn

Hệ **vẫn đang được kiểm soát thật** ở mặt hạ tầng: dịch vụ `lottery` sống nguyên PID **738032**
từ lần deploy 19:23:58 tối qua, `NRestarts=0`, `/api/health` **200**, nhật ký **0 Traceback ·
0 ERROR** cả hôm nay lẫn từ lúc deploy, đĩa 69%, và **hash 4 bảng khoá giống hệt** trước/sau
phiên. Bốn cổng tự kiểm đều **exit 0 thật**. Mọi việc deploy tối qua đều đứng vững: cron nghiệm
thu mới đã vào crontab (MT 16:44/16:48/16:52/16:54 · MB 17:38/17:42/17:46/17:50/17:54), mốc
FINAL MT 16:58 / MB 17:58 khớp ở cả 4 module. **Nhưng có hai chỗ "chỉ có trên giấy".** Thứ
nhất: hai phép tự kiểm mới **C17/C18 chưa từng chạy thật một lần nào** — cron chạy 18:05 còn
deploy lúc 19:23, nên lượt ghi 03/08 vẫn là **16 phép chứ không phải 18**; gọi tươi `run_checks()`
cho 18/18 OK nên code đúng, lượt ghi thật đầu tiên là **18:05 tối nay**. Thứ hai, và nặng hơn:
**chính cổng đếm việc đầu phiên đang báo xanh giả** — nó in *"treo 81 · quá hạn 0 · đến hạn hôm
nay 0"* trong khi **FU-245 tới hạn đúng hôm nay** và **FU-225 đã quá hạn từ 03/08**. Nguyên nhân
đo được: bộ đọc chỉ tìm hạn ở ô `| **due** |` (kho chỉ có 51 ô đó, trong khi **68 tiêu đề** ghi
`hạn DD/MM`) nên **24 mã mất hạn**, và `TREO_STATUSES` thiếu ba nhãn đồng nghĩa nên **14 mã** rơi
khỏi mọi bộ đếm. Đã vá cả hai; con số thật là **treo 97 · quá hạn 1 · mồ côi 17**. Nhân đó cũng
**tìm ra và chứng minh được căn nguyên FU-245 đúng ngày tới hạn**: hook treo ở `sys.stdin.read()`
— thử đối chứng cho thấy bản cũ giữ stdin mở thì **không bao giờ ghi được briefing**, bản mới ghi
sau **0,62 giây**. Về tiền: **cổng lợi thế ĐÓNG cả 6 ô**, không ô nào dương, và **tiền thật = 0
đồng** (111/111 dòng đều shadow). Bạch thủ official 03/08 **trượt cả ba miền** (MN 64 · MT 64 ·
MB 59).

---

## 2. Owner yêu cầu gì (nguyên văn)

> "Kiểm tra toàn diện hệ thống đầu ngày dùm anh luôn em"

*(owner nhắn 09:47 ngày 04/08/2026, giờ Việt Nam)*

Bối cảnh kèm theo: tối qua 03/08 owner **tự phát hiện trước cả máy** rằng trang MB `/nghiem-thu`
trắng — không có lấy một con số — trong khi cả 16 phép tự kiểm vẫn xanh và `/monitoring` vẫn
sạch. Owner đang mất dần niềm tin, nên yêu cầu **trả lời bằng số, không đường mật**.

---

## 3. Đào bới / phát hiện

### 3.1 Bốn cổng tự kiểm — mã thoát thật

| cổng | mã thoát | nội dung |
|---|---|---|
| `_v10920_session_start.py` | **0** | 0 checkpoint quá hạn · 0 roadmap chưa lưu trữ |
| `_v10920_decision_ledger.py` | **0** | **21 quyết định đang hiệu lực · 0 TRÔI** (63/63 mệnh đề máy kiểm khớp) |
| `_v10921_report_gate.py` | **0** | V10971→V10978 đều đủ 9 phần và đã push |
| `_v10925_rule_sync_check.py --check` | **0** | 6 mặt quy tắc đồng bộ · 4 `.mdc` đều tự nạp |

Sáng 03/08 (V10976) đã sửa 5 lỗi "xanh giả" nên các cổng này giờ thoát khác 0 khi trượt — cả bốn
ra 0 là tín hiệu thật, không phải mặc định.

### 3.2 Sức khoẻ hệ thống

| mục | đo được | ghi chú |
|---|---|---|
| `systemctl is-active lottery` | **active** | |
| PID | **738032** | **y nguyên** PID sau deploy lần 2 tối qua — không có restart ngoài ý muốn |
| `NRestarts` | **0** | |
| uptime tiến trình | **14 giờ 28 phút** | khớp mốc `ActiveEnterTimestamp` 03/08 19:23:58 |
| `/api/health` | **200** | `V20.3.36`, timezone `Asia/Ho_Chi_Minh (UTC+7)` |
| đĩa `/` | **69%** — 27G/39G, còn **13G** | chưa tới ngưỡng lo |
| DB | **652.627.968 B ≈ 652 MB** | |
| RAM | còn **2,5 GB** khả dụng / 3,9 GB | |
| Traceback hôm nay | **0** | |
| ERROR hôm nay | **0** | |
| Traceback / ERROR từ 03/08 19:00 (lúc deploy) | **0 / 0** | deploy tối qua không để lại lỗi |
| 429 / 503 / timeout / RateLimit / Overloaded | **0 / 0 / 0 / 0 / 0** | |

Một chi tiết cần nói rõ để khỏi hiểu nhầm: phép đếm thô bắt **1 lần chuỗi "500"**, nhưng soi ra
đó là **dấu mili-giây trong dòng log thành công** (`05:22:58,500 - INFO - HTTP Request: POST
openrouter … "HTTP/1.1 200 OK"`), không phải mã lỗi 500.

`scheduler_logs` hôm nay: **341 INFO · 7 WARNING · 0 ERROR**. Bảy WARNING đều là
`[SOFT_CONTINUE_90S]` — model chưa trả lời sau 90 giây nên chạy model kế tiếp và chờ tiếp tối đa
300 giây; đây là **cơ chế thiết kế sẵn**, không phải hỏng. Có **1 WARNING đáng để mắt**:
`[RULE_QUALITY_ALERT] MN (2026-08-04 wd=1): 0 READY_STRONG rules (total=5)` — không luật nào đạt
mức mạnh, dự đoán phải dựa nhiều hơn vào thống kê. Cùng cảnh báo này cũng xuất hiện cho MB hôm
qua.

### 3.3 Đối chiếu việc đã deploy tối qua 03/08

| việc deploy 03/08 | trạng thái sáng nay | bằng chứng |
|---|---|---|
| Cron nghiệm thu MB 17:46 / 17:50 / 17:54 | **ĐÃ VÀO** | `crontab -l` → MB có `17:38 / 17:42 / 17:46 / 17:50 / 17:54` |
| Cron nghiệm thu MT 16:52 / 16:54 | **ĐÃ VÀO** | MT có `16:44 / 16:48 / 16:52 / 16:54` |
| Mốc FINAL MT 16:53→16:58, MB 17:53→17:58 | **ĐÃ TRẢ NỢ V10931 XONG** | khớp cả 4 module: `FREEZE_MARKS` · `OUTPUT_DUE` · `DEADLINE` · `OUTPUT_FREEZE_HHMM` **và** `LANE_SCHEDULE` |
| Nhãn "LỠ HẠN" thay "chưa tới giờ" | **CÓ** | có trong `_v10879_nghiemthu_lane.py` và `web/frontend/nghiem-thu.html` |
| Bộ tự kiểm 16 → 18 phép | **CHƯA CHẠY THẬT LẦN NÀO** | xem 3.4 |
| Dịch vụ còn sống sau deploy | **CÓ** | PID 738032, `NRestarts=0`, uptime 14h29 |

Tổng cộng **76 dòng cron** đang bật.

### 3.4 C17 / C18 — đúng trên giấy, chưa có lượt ghi thật

Đây là phát hiện đầu tiên thuộc loại "chỉ có trên giấy".

- Cron bộ tự kiểm chạy **18:05 mỗi ngày**. Deploy hai phép mới xong lúc **19:23:57** ngày 03/08.
  → lượt 18:05 ngày 03/08 chạy **bản 16 phép**, trước khi có C17/C18 **1 giờ 18 phút**.
- Bảng `v10900_consistency_guard` ngày 03/08: **16 dòng**, không có `C17_nghiemthu_co_output`
  cũng không có `C18_bien_lane_du_rong`. Lịch sử 4 ngày gần nhất đều **16/16 OK**.
- **Kiểm bù ngay trong phiên:** gọi thẳng `run_checks()` trên VPS — cố ý **không** dùng
  `compute_view()` vì hàm đó chỉ đọc bản đã lưu, không tính lại (bẫy đã ghi trong sổ tay vận
  hành). Kết quả: **18 phép · OK 18 · LỆCH 0 · LỖI 0.**
  - `C17_nghiemthu_co_output` = `[]` — đúng, vì lúc 09:52 chưa miền nào qua mốc FINAL.
  - `C18_bien_lane_du_rong` = `[]` — biên MB nay là **546 giây** (official chốt 17:44:54, lượt
    lane cuối 17:54), trên ngưỡng **300 giây**. Chính bản vá cron tối qua tạo ra khoảng biên này.
- File `_v10900_consistency_guard.py` trên VPS sửa lúc **03/08 19:21:57**, có chứa cả hai chuỗi
  `C17_nghiemthu_co_output` và `C18_bien_lane_du_rong`.

**Kết luận:** code đúng, chưa có bằng chứng chạy thật. **Lượt ghi thật đầu tiên là 18:05 tối nay.**
Mở `FU-259` để canh.

### 3.5 Cổng đếm việc đang báo xanh giả — phát hiện nặng nhất phiên này

Briefing đầu phiên sáng nay in:

```
[3] MỤC THEO DÕI CÒN TREO: 81 · trong đó QUÁ HẠN 0
```

Không có dòng "đến hạn hôm nay". Nhưng đọc tay sổ theo dõi thì
**`FU-245 · SC0804 · Hook đầu phiên im 2 ngày · hạn 04/08`** — tới hạn **đúng hôm nay**, và
**`FU-225 · UI0803` hạn 03/08** — **đã quá hạn**. Cổng không thấy cả hai.

Đào ra **hai lỗ riêng biệt**:

**Lỗ 1 — hạn viết ở tiêu đề thì bộ đọc không thấy.**
`_v10958_fu_reader` chỉ dò hạn trong ô bảng `| **due** | … |`. Nhưng khối cập nhật (kiểu V10975,
V10978) thường **bỏ ô đó** và chỉ ghi hạn ở **tiêu đề** (`### FU-245 · SC0804 · … · hạn 04/08`)
hoặc ở ô `**hạn mới**`. Đếm trong kho:

| cách ghi hạn | số lần |
|---|---|
| ô `\| **due** \|` | **51** |
| ô `\| **hạn mới** \|` | 1 |
| tiêu đề mang `hạn DD/MM` | **68** |

→ **24 mã** ra `due_date = None`, tức **không bao giờ** bị tính là quá hạn hay đến hạn. Trong 24
mã đó có FU-225 (quá hạn thật) và FU-245 (đến hạn hôm nay). Riêng FU-225 còn nghiệt hơn: bản
**cũ** của nó *có* ô `| **due** | 2026-08-03 |`, nhưng bản **mới nhất** (cập nhật V10975) bỏ ô
đó — mà bộ đọc thì đúng quy tắc chỉ lấy bản mới nhất, nên hạn biến mất.

**Lỗ 2 — nhãn trạng thái mồ côi.**
`TREO_STATUSES` khai **6 nhãn**, nhưng sổ đang thực dùng **28 nhãn khác nhau**. Ba trong số đó
chỉ là cách viết khác của nhãn đã có:

| nhãn không được đếm | tương đương nhãn đã khai |
|---|---|
| `MEASURED_ROOT_CAUSE` (6 mã) | `MEASURED_BUT_NOT_FIXED` |
| `MEASURED_ROOT_CAUSE_FOUND` (1 mã) | `MEASURED_BUT_NOT_FIXED` |
| `DEPLOYED_PENDING_OWNER_VERIFY` (7 mã) | `DEPLOYED_PENDING_LIVE_VERIFY` |

→ **14 mã** rơi khỏi bộ đếm treo, bộ đếm quá hạn, **và** cả phép soát thiếu mã đọc §58. Ngoài ra
còn **17 mã** mang nhãn chưa ai phân loại (`DEFER`, `FALSE_NEGATIVE`, `READY_NOT_DEPLOYED`,
`WAIT_CLOSEOUT`, `DELIVERED_*_DOCS_ONLY`, …) — không tính là treo, cũng chưa ai đóng.

**Hậu quả cộng dồn:** con số "81 mục treo · 0 quá hạn" mà agent báo cho owner suốt mấy phiên gần
đây **không dùng được**.

### 3.6 FU-245 — tìm ra căn nguyên và chứng minh được, đúng ngày tới hạn

V10978 mới **nghi** hook treo ở `sys.stdin.read()` nhưng ghi rõ *"chưa chứng minh"*. Phiên này
chứng minh xong.

- **Bằng chứng hiện trường:** lúc phiên bắt đầu, `docs/_BRIEFING_DAU_PHIEN.txt` mang mốc sửa
  **03/08 19:19** — không phải sáng nay. Hook **không kích hoạt phiên thứ 4 liên tiếp**
  (02/08 · 03/08 sáng · 03/08 tối · 04/08 sáng).
- **Thử đối chứng** (`_v10980_hook_test.py`): chạy **cả bản cũ lẫn bản mới**, stdin **để mở** —
  đúng tình huống nghi ngờ là Cursor mở stdin rồi không đóng. Chờ tối đa 8 giây:

| bản | briefing có được ghi không |
|---|---|
| **cũ** (`stdin.read()` ở dòng đầu `main()`) | **KHÔNG — treo hết 8 giây** |
| **mới V10980** (làm việc trước, đọc stdin sau) | **CÓ, sau 0,62 giây** |

Cơ chế hỏng đã rõ: `sys.stdin.read()` nằm ở **dòng đầu tiên** của `main()`. Nếu phía gọi giữ
stdin mở, lời gọi này chặn tới hết timeout 100 giây rồi bị giết — **bộ kiểm không bao giờ được
chạy, file không bao giờ được ghi**. Đó là lý do briefing đứng im mà chạy tay thì vẫn tốt
(`"" | python …` đóng stdin ngay nên không tái hiện được).

### 3.7 Trạng thái sống hôm nay 04/08

| mục | kết quả |
|---|---|
| MN official | **đã chốt 05:19:56** · bạch thủ **22** · `lo2` 12 ký tự · `status=ACTIVE` · `is_fallback=0` |
| MN `model_count` | **15/15 — đủ**, không bị lọc phiếu |
| MT / MB official | **chưa tới giờ** (hạn 16:58 / 17:58) |
| Lane nghiệm thu MN | **ĐÃ RA SỐ** — `MN_NGHIEMTHU_1908_V1`, `test_bt=22`, khớp official |
| Lane nghiệm thu MT / MB | chưa tới giờ |

**FU-252 (ngưỡng 21/21 ô miền-ngày trong 7 ngày): đo được 13/21.** Bóc chi tiết:

| ngày | MN | MT | MB |
|---|---|---|---|
| 04/08 | ✅ | chưa tới giờ | chưa tới giờ |
| 03/08 | ✅ | ✅ | ❌ **mất trắng** (đúng sự cố owner bắt tối qua) |
| 02/08 | ✅ | ✅ | ✅ |
| 01/08 | ✅ | ✅ | ✅ |
| 31/07 | ✅ | ✅ | ✅ |
| 30/07 | ✅ | ❌ | ❌ |
| 29/07 | ❌ | ❌ | ❌ |

`MB_NGHIEMTHU_1908_V1` lần ghi cuối cùng là **02/08**. Cron vá mới chỉ có hiệu lực từ tối qua,
nên **tối nay 04/08 mới là lượt thử thật đầu tiên cho MB**.

### 3.8 Kết quả và chấm điểm 03/08

- `lottery_results` ngày 03/08: **đủ 3 miền** — MN 3 đài · MT 2 đài · MB 1 đài. Chuỗi 9 ngày gần
  nhất đều đủ 3 miền, không đứt.
- `model_daily_eval` ngày 03/08: **81 dòng = 27 dòng/miền × 3 miền** — đã chấm xong.

**Bạch thủ official 03/08 — trượt cả ba miền:**

| miền | bạch thủ | số đài | trúng | kết quả |
|---|---|---|---|---|
| MN | **64** | 3 | 0 | **TRƯỢT** |
| MT | **64** | 2 | 0 | **TRƯỢT** |
| MB | **59** | 1 | 0 | **TRƯỢT** |

Owner nhờ kiểm lại MN 64 và MB 59 — xác nhận đúng hai con số đó, và **cả hai đều trượt**.

### 3.9 Cổng lợi thế và tiền

Gọi thẳng `_v10945_edge_gate.tinh()` (đọc thuần, không ghi bảng), ngưỡng QD-013 là **lợi thế ≥
+3,0pp VÀ z ≥ 2,0**:

| cửa sổ | miền | kỳ | hệ trúng | đánh bừa | lợi thế | z | cổng |
|---|---|---|---|---|---|---|---|
| 90 ngày | MN | 90 | 16,25% | 16,45% | **−0,19pp** | −0,09 | **ĐÓNG** |
| 90 ngày | MT | 90 | 13,24% | 16,50% | **−3,26pp** | −1,30 | **ĐÓNG** |
| 90 ngày | MB | 90 | 16,67% | 23,72% | **−7,06pp** | −1,57 | **ĐÓNG** |
| 30 ngày | MN | 30 | 15,96% | 16,30% | **−0,34pp** | −0,09 | **ĐÓNG** |
| 30 ngày | MT | 30 | 10,96% | 16,62% | **−5,66pp** | −1,30 | **ĐÓNG** |
| 30 ngày | MB | 30 | 23,33% | 23,50% | **−0,17pp** | −0,02 | **ĐÓNG** |

**Cả 6 ô đều ĐÓNG, và không ô nào dương.** Ô gần hoà nhất là MB 30 ngày (−0,17pp); ô tệ nhất là
MB 90 ngày (−7,06pp). Khoảng cách tới ngưỡng +3pp còn rất xa.

**Tiền thật = 0 đồng.** `money_board_log` có **111 dòng**, và **cả 111/111** đều mang đúng bộ cờ
shadow: `diagnostic_only=1 · shadow_only=1 · output_eligible=0 · owner_approved=0`. Cột `stake`
là **nhãn chữ** để đọc (`"Full (50 điểm/số/đài)"`, `"Nửa (25 điểm)"`, `"Nghỉ hôm nay"`), **không
phải số tiền đã đặt** — không có dòng nào thoát khỏi trạng thái shadow. Các bảng liên quan:
`money_board_lock` 18 dòng · `money_board_daily_lock` 84 · `pnl_daily_bets` 28 — đều là sổ đo.

### 3.10 FU-243 — lọc phiếu vẫn nguyên hình

Phân bố `model_count` 14 ngày gần nhất:

| miền | phân bố |
|---|---|
| MT | **13 ở 12/13 ngày**, một ngày xuống 11 |
| MB | **14 ở 10 ngày**, 13 ở 3 ngày |
| MN | **15 ở 12/14 ngày**, còn lại 14 và 13 |

Hôm nay MN chốt **15/15** — đủ. Vẫn còn chỗ lệch tài liệu đã ghi từ V10978: `/api/health` khai
`expected_output_model_count: 15` trong khi mức ổn định thật của MT là **13**. **Không đụng trước
08/08** theo QD-014.

---

## 4. Hướng xử lý và vì sao chọn

**Việc phát hiện:** hai chỗ "chỉ có trên giấy" (C17/C18 chưa chạy thật; cổng đếm việc báo xanh
giả) và một căn nguyên đã chứng minh được (FU-245).

**Với C17/C18 — chọn: chỉ canh, không đụng.**
Phương án loại bỏ: (a) chạy tay bộ tự kiểm ngay bây giờ để có lượt ghi 18 dòng — **loại**, vì sẽ
ghi một dòng ngày 04/08 lúc 10 giờ sáng, sai ngữ cảnh (bộ này thiết kế để chạy 18:05 sau khi cả
ba miền đã chốt), và C17 chắc chắn trả rỗng vì chưa miền nào qua mốc FINAL — tức tạo ra đúng một
"xanh giả" nữa. (b) dời cron sớm hơn — **loại**, đụng crontab production trong lúc QD-014 đang
đóng băng. **Chọn:** mở `FU-259` với ngưỡng bằng số — 18:05 tối nay bảng phải có **đúng 18 dòng**
ngày 04/08 và phải thấy tên cả hai phép; không đạt thì soi lại đường dẫn trong crontab.

**Với cổng đếm việc — chọn: sửa ngay trong phiên.**
Đây là **lỗi rõ ràng, có bằng chứng, đo được**, đúng loại mà playbook bắt "sửa ngay trong phiên,
không hỏi lại". Nó cũng **cùng họ với 5 lỗi xanh giả V10976 đã sửa**, chỉ khác tầng. Và nó là
thứ trực tiếp gây ra chuyện owner sợ nhất: máy báo sạch trong khi việc đang trôi.

Nhưng có một chỗ **cố ý không tự quyết**: trong 31 mã mang nhãn ngoài danh sách, chỉ **3 nhãn**
là đồng nghĩa hiển nhiên với nhãn đã có (`MEASURED_ROOT_CAUSE` ↔ `MEASURED_BUT_NOT_FIXED`, …) —
ba nhãn này thì thêm thẳng. Còn **17 mã** mang nhãn như `DELIVERED_DOCS_ONLY`, `DEFER`,
`FALSE_NEGATIVE` thì **ranh giới đóng/treo là quyết định nghiệp vụ, không phải kỹ thuật** —
tự gán bừa là lại chế ra một loại sai khác. Nên chọn cách **bêu tên chúng ra** (`[3b] MỤC MỒ
CÔI` trong briefing) và mở `FU-258` hạn 06/08 để phân loại dứt điểm. Thà briefing kêu to còn hơn
im lặng bỏ rơi.

**Với FU-245 — chọn: vá + dựng sổ điểm danh.**
Chỉ vá thứ tự thực thi thì vẫn còn một câu chưa trả lời được: Cursor **có gọi** hook hay không?
Hai phiên trước phải đoán. Nên ngoài việc chuyển phần làm việc lên trước, thêm
`docs/_HOOK_DIEM_DANH.log` ghi mốc `VAO_HOOK` **ngay dòng đầu**, trước mọi thứ có thể chặn. Từ
phiên sau, nhìn sổ là biết chắc: có dòng `VAO_HOOK` mà không có `DA_GHI_BRIEFING` nghĩa là gọi
rồi nhưng treo; không có dòng nào nghĩa là Cursor không gọi. **Hết đoán.**

**Không đụng đường ra số.** QD-014 đóng băng tới hết 08/08. Ba file đã sửa đều là **công cụ chạy
ở máy local**; đã kiểm `crontab -l` trên VPS: không có `_v10920`, `_v10958`, `_v10921`, `_v10945`
— nên **không cần deploy**, và cũng không có gì để deploy.

---

## 5. Đã làm gì

### 5.1 Bảng file × thay đổi

| file | thay đổi | vì sao |
|---|---|---|
| `web/backend/_v10958_fu_reader.py` | thêm `_han_cua_khoi()` — chuỗi dò hạn `**due**` → `**hạn mới**` → `**deadline**` → tiêu đề; thêm `_ddmm_thanh_ngay()` suy năm theo khoảng cách gần nhất; thêm 3 nhãn vào `TREO_STATUSES`; thêm `DONG_STATUSES` và `trang_thai_mo_coi()` | vá lỗ 1 + lỗ 2 |
| `web/backend/_v10920_session_start.py` | in thêm **"ĐẾN HẠN HÔM NAY"** và **"không ghi hạn"**; thêm mục `[3b] MỤC MỒ CÔI`; đưa cả hai vào danh sách cảnh báo đầu câu trả lời | để hai lỗ trên không tái diễn trong im lặng |
| `.cursor/hooks/session_start_briefing.py` | chuyển `sys.stdin.read()` xuống **sau** khi đã chạy bộ kiểm, ghi file và in `{}`; thêm sổ điểm danh `_diem_danh()` | vá FU-245 |
| `CHANGELOG.md` | prepend khối V10980 | §52 |
| `docs/CURRENT_TRUTH_SSOT.md` | prepend bảng trạng thái V10980 | §52 |
| `docs/FOLLOW_UP_TRACKER.md` | prepend: cập nhật FU-245 · FU-252 · FU-243; **mở mới FU-258, FU-259** | §52 |

**Không sửa** bất kỳ file runtime nào, **không** đụng `/du-doan`, **không** đụng writer
`final_bundles`, **không** đụng bộ chọn model.

### 5.2 Backup

`backups/v10980_pre/` — `_v10958_fu_reader.py.pre` · `_v10920_session_start.py.pre` ·
`session_start_briefing.py.pre`. Hash trước khi sửa:
`_v10958_fu_reader.py` = `149FBC99…`, `_v10920_session_start.py` = `9D2F8233…`,
`session_start_briefing.py` = `BD076059…`.

### 5.3 Deploy

**Không có.** Ba file đã sửa không tồn tại trong `crontab -l` trên VPS và không thuộc đường chạy
runtime. Dịch vụ **không restart** — PID vẫn **738032** trước và sau phiên.

### 5.4 Hash 4 bảng khoá trước/sau

| bảng | dòng | trước → sau |
|---|---|---|
| `predictions` | 11.673 | **GIỐNG HỆT** |
| `final_bundles` | 472 | **GIỐNG HỆT** |
| `lottery_results` | 15.207 | **GIỐNG HỆT** |
| `model_daily_eval` | 11.496 | **GIỐNG HỆT** |

Đo lúc 09:52 và 10:12. Dịch vụ sau phiên: `active` · PID `738032` · `NRestarts=0` · health `200`.

---

## 6. Cổng kiểm

| kiểm | kết quả |
|---|---|
| `_v10920_session_start.py` (đầu phiên) | **exit 0** |
| `_v10920_decision_ledger.py` | **exit 0** — 21 quyết định, 0 TRÔI |
| `_v10921_report_gate.py` (toàn bộ) | **exit 0** |
| `_v10925_rule_sync_check.py --check` | **exit 0** — 6 mặt đồng bộ |
| `_v10920_session_start.py` **sau khi sửa** | **exit 0** |
| `_v10925_rule_sync_check.py` **sau khi sửa** | **exit 0** |
| `_v10967_list_treo.py` (bên thứ ba dùng bộ đọc) | chạy được, ra 97 mục |
| `_v10976_kiem_fu.py` (bên thứ ba dùng bộ đọc) | **exit 0** |
| Hash 4 bảng khoá trước/sau | **giống hệt cả 4** |
| `/api/health` | **200** |
| `/api/nghiem-thu` không kèm khoá | **401** — đúng, endpoint admin |
| PID trước/sau | **738032 = 738032** — không restart |
| Thử đối chứng hook (stdin để mở) | bản cũ **treo** · bản mới **ghi sau 0,62s** |
| Soát khoá API trong thư mục bằng chứng | **0 chỗ phải che** — đã quét `sk-`, `AIza`, `gsk_`, `ghp_`, `api_key`, `Bearer`, `PRIVATE KEY` |
| `_v10921_report_gate.py V10980` | xem mục 9 (chạy sau khi push) |

**Cổng đếm việc trước và sau khi vá:**

| | trước | sau |
|---|---|---|
| mục treo | 81 | **97** |
| quá hạn | 0 | **1** (FU-225) |
| đến hạn hôm nay | *không có dòng này* | **1** (FU-245, trước khi dời hạn) |
| mục mồ côi | *không đếm* | **17** |
| thiếu mã đọc §58 | 0 | **0** |

---

## 7. Vướng vấp

**7.1 — Tự mình tạo ra 2 mục mồ côi khi ghi sổ, và bị chính bộ dò mới bắt được.**
Khi prepend khối cập nhật cho FU-243 và FU-252, ban đầu viết dạng kể chuyện **không kèm bảng
`| **status** |`**. Vì bộ đọc chỉ lấy bản mới nhất, hai mã đó lập tức mất trạng thái và rơi vào
danh sách mồ côi — số mồ côi nhảy từ 17 lên 19. Đã thêm bảng trạng thái đầy đủ cho cả hai và
kiểm lại về đúng 17. *Hậu quả nếu bỏ qua:* FU-252 (đang canh lane MB) và FU-243 (đang canh lọc
phiếu) sẽ **biến mất khỏi mọi bộ đếm** — đúng loại lỗi vừa mất công sửa. Bài học: **mỗi khối
cập nhật FU bắt buộc phải có bảng trạng thái**, không được viết kể chuyện suông.

**7.2 — Suýt báo nhầm FU-185 là quá hạn.**
Bản dò hạn đầu tiên đòi ô hạn khớp **trọn chuỗi** `DD/MM`. Ô của FU-185 ghi
`10/08 (sau freeze QD-014)` nên không khớp, bộ đọc rơi xuống lấy hạn ở tiêu đề là `03/08` và
báo **quá hạn**. Thực tế owner **đã gia hạn tới 10/08**. Đã sửa sang dò trong chuỗi kèm chặn
ngày/tháng hợp lệ. *Hậu quả nếu bỏ qua:* báo cho owner một mục quá hạn **không có thật** —
đúng thứ đang cố diệt, và tệ hơn xanh giả vì làm owner mất niềm tin vào cả những cảnh báo đúng.

**7.3 — Câu lệnh đầu phiên viết sai kiểu shell.**
Gõ `cd /d … && …` theo lối `cmd` trong khi phiên chạy PowerShell, lỗi ngay. Mất một lượt. Không
ảnh hưởng dữ liệu.

**7.4 — Truy vấn `scheduler_logs` sai tên cột.**
Dùng `status` trong khi bảng chỉ có `log_level`, nên lần probe đầu trả `ERR no such column`. Đã
đọc `PRAGMA table_info` rồi truy vấn lại đúng. *Hậu quả nếu bỏ qua:* sẽ kết luận "0 lỗi
scheduler" từ một câu truy vấn hỏng — tức lại một xanh giả nữa, lần này do chính agent tạo ra.

**7.5 — `compute_view()` của lane cần tham số `con`, gọi thiếu nên probe 2 báo lỗi.**
Đã gọi lại đúng ở probe 3. Không ảnh hưởng kết luận.

**7.6 — `/api/du-doan` trả 404.**
Đường dẫn thử là phỏng đoán, không phải endpoint thật; `/api/health` và `/api/nghiem-thu` đều
đúng. Không kết luận gì từ con số 404 này. Việc kiểm 15/15 lấy thẳng từ `final_bundles`
(`model_count=15`) nên không phụ thuộc endpoint.

**7.7 — Không kiểm được trang `/nghiem-thu` bằng mắt.**
Endpoint trả **401** khi gọi không kèm khoá — đúng thiết kế admin, nhưng nghĩa là phiên này
**chỉ xác nhận được dữ liệu trong DB**, không xác nhận được trang hiển thị ra sao. Owner tối qua
bắt lỗi **bằng mắt trên trang**, nên khoảng trống này vẫn còn. Đã ghi vào FU-252.

**7.8 — Kho sổ theo dõi có nhiều file đang sửa dở của phiên V10979 chạy song song.**
`git status` cho thấy hàng loạt file `web/backend/_v107xx…` bị sửa mà phiên này không đụng. Đã
**chỉ stage đúng file của mình**, không dùng `git add -A`.

---

## 8. Gỡ về

Không có gì chạm production nên **không cần gỡ gì trên VPS**. Nếu muốn trả ba file công cụ về
bản cũ:

```bat
cd /d E:\Lottery_AI_Test
copy backups\v10980_pre\_v10958_fu_reader.py.pre         web\backend\_v10958_fu_reader.py
copy backups\v10980_pre\_v10920_session_start.py.pre     web\backend\_v10920_session_start.py
copy backups\v10980_pre\session_start_briefing.py.pre    .cursor\hooks\session_start_briefing.py
python web\backend\_v10920_session_start.py
```

Thời gian: **dưới 1 phút**. Sau khi gỡ, briefing sẽ quay lại báo *"treo 81 · quá hạn 0"* — tức
**quay lại trạng thái xanh giả**, nên chỉ gỡ nếu bản vá gây lỗi thật.

Ba khối đã prepend vào `CHANGELOG.md` · `docs/CURRENT_TRUTH_SSOT.md` ·
`docs/FOLLOW_UP_TRACKER.md` nằm ở **đầu file**, xoá tay được, không cần công cụ.

---

## 9. Theo dõi tiếp

| mã | mã đọc | việc | ngưỡng bằng số | hạn |
|---|---|---|---|---|
| **FU-259** | KS0805 | C17/C18 phải có lượt ghi thật | **18:05 hôm nay 04/08**: `v10900_consistency_guard` ngày 04/08 phải có **đúng 18 dòng**, có mặt `C17_nghiemthu_co_output` + `C18_bien_lane_du_rong`. Vẫn 16 dòng → soi đường dẫn crontab ngay | **05/08** |
| **FU-258** | KS0806-1 | Phân loại dứt điểm 17 mục mồ côi | mỗi mục: hoặc đóng, hoặc gán một nhãn nằm trong `TREO_STATUSES`. Đích: **mồ côi = 0** | **06/08** |
| **FU-245** | SC0804 | Xác nhận bản vá hook ăn thật | mở **2 phiên mới**; `docs/_HOOK_DIEM_DANH.log` phải có dòng `VAO_HOOK` + `DA_GHI_BRIEFING` đúng giờ mở phiên. Không có dòng nào → Cursor thật sự không gọi hook, chuyển sang bắt buộc gọi tay | **06/08** |
| **FU-252** | KS1008 | Lane nghiệm thu đủ 3 miền | **21/21** ô miền-ngày / 7 ngày. Đang **13/21**. Mốc gần nhất: **tối nay 04/08 MB phải ra số** — lượt thử thật đầu tiên của cron vá | **10/08** |
| **FU-225** | UI0803 | **ĐANG QUÁ HẠN từ 03/08** — chờ owner tự mở `/du-doan-test` xác nhận UI | owner hard-refresh MN/MT/MB + `/filter?tab=overview` | **quá hạn** |
| **FU-243** | SC0805 | Lọc phiếu MT 13 / MB 14 | sau 08/08: hoặc sửa `expected_output_model_count` theo miền, hoặc xem lại `bt_gate` / `MT_top13_V10752` | **05/08** |
| **FU-256** | DO0806 | Biên giờ chốt MT/MB co lại | C18 canh sẵn, ngưỡng 300 giây | **06/08** |

**Việc dồn vào 08/08 — ngày hết đóng băng QD-014: 14 mục.**
FU-186 (KS0808-2) · FU-187 (KS0808) · FU-191 (XH0808-2) · FU-192 (XH0808-3) · FU-193 (XH0808-4) ·
FU-203 (DO0808-2) · FU-207 (DP0808) · FU-210 (DO0808-1) · FU-212 (TDLX-212) · FU-215 (DB0808) ·
FU-216 (XH0808-1) · FU-217 (SC0808-1) · FU-226 (HT0808-2) · FU-231 (HT0808-1).

Trong 14 mục đó có **6 mục `OWNER_LOCK`** — tức chờ owner quyết chứ agent không tự làm được:
FU-215 (đóng băng đường ra số) · FU-216 (shadow MT RF đơn) · FU-226 (A/B hai prompt) ·
FU-231 (bỏ ép RULES-FIRST) · và FU-192 đang `AWAITING_OWNER_OK`.

**Cần owner quyết:**
1. **FU-225 đang quá hạn** và chỉ owner mới đóng được — cần owner mở `/du-doan-test` ba miền,
   hard-refresh, xác nhận nhìn đúng.
2. **14 việc dồn vào 08/08** là quá nhiều cho một ngày. Nên chọn trước vài mục để giãn sang
   09–10/08, hay giữ nguyên?

---

*Báo cáo lập bởi agent vận hành, phiên V10980, 04/08/2026. Toàn bộ số liệu đo trực tiếp trên VPS
`14.225.224.89` trong khung 09:49–10:25 giờ Việt Nam. Tệp bằng chứng thô nằm trong `evidence/`.*
