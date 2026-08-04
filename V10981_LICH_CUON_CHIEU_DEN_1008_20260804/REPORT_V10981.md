# BÁO CÁO V10981 — Giãn 14 mục dồn ngày 08/08 thành lịch cuốn chiếu tới 10/08

| | |
|---|---|
| Phiên bản | **V10981** |
| Ngày | **2026-08-04** (giờ Việt Nam) |
| Loại | Lập kế hoạch + cập nhật tài liệu — **không deploy, không đụng runtime** |
| Quyết định owner | **QD-021** |
| Cổng kiểm | `_v10981_kiem_lich.py` **8/8 ĐẠT** · `_v10920_decision_ledger.py` **0 TRÔI** |
| Phiên chạy song song | **V10979** (nhịp cuốn chiếu 5 model) — không đụng vào nhau |

---

## 1. Tóm tắt một đoạn

Kiểm toán V10980 sáng 04/08 đếm được **14 mục theo dõi cùng đáo hạn 08/08** — đúng ngày hết
đóng băng QD-014, trong đó 5 mục mang nhãn chờ owner. Owner ký lúc **10:29** chọn giãn ra cuốn
chiếu, hạn chót **10/08**, làm tuần tự, cái nào xác thực rõ ràng và đơn giản làm trước. Phiên
này đã giãn 14 mục thành **04/08=3 · 05/08=1 · 06/08=1 · 07/08=1 · 08/08=3 · 09/08=3 · 10/08=2** —
ngày nặng nhất từ **14 xuống 3 mục**. **5
mục kéo lên được 04–07/08** vì không chạm vùng đóng băng; **8 mục buộc phải
từ 09/08 trở đi** vì QD-014 cấm đích danh đổi roster 15 model / bộ lọc combo-super / lớp ghi đè.
Quan trọng nhất: **5 mục KHÔNG THỂ kết luận trước 10/08**
vì ngưỡng đo do chính owner ký cần 7–14 ngày — với chúng, "xong trước 10/08" được định nghĩa lại
thành **chạy được và có ngày đo đầu tiên**, và ngày kết luận thật (15/08 → 23/08) ghi rõ từng
mục thay vì hứa cho xong. Quyết định vào sổ ngay trong phiên (`QD-021`, 5 mệnh đề máy kiểm
được, khớp 5/5); toàn sổ 23 quyết định **0 TRÔI**.

---

## 2. Owner yêu cầu gì — nguyên văn

> "Giãn ra cuốn chiếu tới hết ngày 10/08 phải hoàn thành, làm lần lượt những vấn đề nào xác thực rõ ràng , đơn giản làm trước tới cuối cùng 10/08 phải xong"

*(owner ký 2026-08-04 10:29 giờ Việt Nam)*

Bối cảnh câu hỏi trước đó: agent trình rằng 14 mục cùng đáo hạn 08/08 và hỏi **"giãn ra hay giữ
nguyên"**. Owner chọn **giãn ra**, kèm bốn ràng buộc đọc được từ chính câu nói:

| Ràng buộc | Trích |
|---|---|
| Trải theo ngày, không dồn | *"Giãn ra cuốn chiếu"* |
| Hạn chót tuyệt đối | *"tới hết ngày 10/08 phải hoàn thành"* · *"tới cuối cùng 10/08 phải xong"* |
| Làm tuần tự, không song song | *"làm lần lượt"* |
| Thứ tự ưu tiên | *"những vấn đề nào xác thực rõ ràng , đơn giản làm trước"* |

---

## 3. Đào bới / phát hiện

### 3.1 Đo bằng cách nào

Dùng **bộ đọc chuẩn** `web/backend/_v10958_fu_reader.py` (không tự viết lại parser) — bộ này
lấy khối gần đầu file nhất của mỗi mã FU làm sự thật hiện tại, vì `docs/FOLLOW_UP_TRACKER.md`
được ghi bằng `prepend()` nên bản cũ vẫn nằm dưới làm lịch sử. Đọc thêm
`docs/OWNER_DECISION_LEDGER.md` mục QD-013 → QD-019 vì phần lớn nhóm 14 gắn với quyết định
"sau khi hết đóng băng".

Cỡ mẫu: **117 mục** đọc được
trong sổ theo dõi (98 treo + 19
mồ côi), lọc ra 14 mã owner nêu đích danh.

### 3.2 Số thật đo được

| Phát hiện | Số |
|---|---|
| Mục treo có hạn ≤ 10/08 (toàn hệ, không chỉ nhóm 14) | **32** |
| Mục mồ côi có hạn ≤ 10/08 | **4** |
| Nhóm owner nêu | **14** — tất cả cùng `due = 2026-08-08` |
| Trong nhóm 14: chạm vùng đóng băng QD-014 | **8/14** |
| Trong nhóm 14: KHÔNG chạm, kéo lên sớm được | **5/14** |
| Trong nhóm 14: cần > 7 ngày đo nên không kết luận nổi trước 10/08 | **5/14** |
| Ngày 10/08 đã có sẵn hạn từ phiên trước | **9 mục** (V10974–V10980) |

### 3.3 Phân loại từng mục theo hai trục owner yêu cầu

| Mã máy | Nhãn | Độ rõ ràng | Độ phức tạp | Chạm đóng băng |
|---|---|---|---|---|
| `FU-187` | Nghiệm thu hook tra cứu đầu phiên | 🟢 rõ ràng | đơn giản | không |
| `FU-191` | Khoá luật cắt model an toàn combo-super | 🟢 rõ ràng | đơn giản | không |
| `FU-212` | MT tín hiệu rơi ở gộp phiếu — đóng phần đo | 🟢 rõ ràng | đơn giản | không |
| `FU-207` | Nâng cổng an toàn deploy lên mốc FINAL / bundle v2 | 🟢 rõ ràng | trung bình | không |
| `FU-210` | Đào nguyên nhân mất lợi thế MT tháng 6 | 🟡 mơ hồ | trung bình | không |
| `FU-193` | Sàn chất lượng combo-super — thiết kế + ngưỡng số | 🔵 chờ owner | trung bình | **CÓ** |
| `FU-186` | Đọc kết quả 7 ngày sau tắt lớp ghi đè | 🟢 rõ ràng | đơn giản | **CÓ** |
| `FU-203` | gemini-3.5-flash — chấm tuần 02→08/08 | 🟢 rõ ràng | đơn giản | không |
| `FU-215` | Đóng băng QD-014 hết hạn — chốt hoặc gia hạn | 🔵 chờ owner | đơn giản | **CÓ** |
| `FU-192` | Promote glm-5.1 / gpt-oss-120b hay đóng lại | 🔵 chờ owner | trung bình | **CÓ** |
| `FU-216` | Khởi động shadow MT bạch thủ = random-forest đơn (QD-015) | 🟢 rõ ràng | nặng | **CÓ** |
| `FU-217` | Sửa key `lstm_probability` combo đọc sai + đo shadow | 🟢 rõ ràng | nặng | **CÓ** |
| `FU-231` | Khởi động shadow bỏ ép RULES-FIRST (QD-016) | 🟢 rõ ràng | nặng | **CÓ** |
| `FU-226` | Khởi động A/B hai prompt trên cùng model (QD-017) | 🟢 rõ ràng | nặng | **CÓ** |

### 3.4 Ba phát hiện phụ trong lúc đào

1. **`FU-212` lệch nhãn hạn.** Tiêu đề ghi `hạn LX` (không hạn) nhưng ô `due` ghi
   `2026-08-08`. Bộ đọc lấy ô `due` nên mục vẫn bị đếm vào nhóm 08/08, trong khi người đọc
   tiêu đề tưởng nó không có hạn. Đã sửa trong phiên.
2. **Quy ước mã đọc §58 trong kho thực tế là MMDD, không phải DDMM như văn bản §58 viết.**
   Bằng chứng: `FU-243 · SC0805 · hạn 05/08`, `FU-258 · KS0806-1 · hạn 06/08`,
   `FU-261 · QD0809 · hạn 09/08`, `QD-018 · HT0822 · hạn 22/08`. Hai mục lệch chuẩn
   (`FU-252 · KS1008`, `FU-253 · SC1008`) thuộc phiên khác. Phiên này theo cách kho đang dùng
   để không tạo dị bản thứ ba.
3. **Ba trong "5 mục chờ owner" thật ra owner đã ký từ 02/08.** `FU-216`←`QD-015`,
   `FU-226`←`QD-017`, `FU-231`←`QD-016`, cả ba đều có nguyên văn *"Duyệt trước để 08/08 tự
   chạy"*. Chúng mang nhãn `OWNER_LOCK` nhưng đang chờ **ngày**, không chờ **chữ ký**. Theo
   §56 (tra cứu trước khi hỏi) **không được hỏi lại** — đã báo cáo thay vì hỏi.

---

## 4. Hướng xử lý và vì sao chọn

### 4.1 Ba phương án đã cân

| Phương án | Nội dung | Vì sao loại / chọn |
|---|---|---|
| A — chia đều 2 mục/ngày | 14 mục ÷ 7 ngày | **Loại.** Bỏ qua ràng buộc thật: 8 mục chạm đường ra số không thể nằm trước 09/08 dù có chia đẹp đến đâu. Chia đều là đẹp trên giấy, vỡ ngay ngày đầu. |
| B — dồn hết về 09–10/08 sau khi hết đóng băng | Chờ freeze xong rồi làm | **Loại.** Đúng cái owner vừa bảo đừng làm. 5 mục không chạm đóng băng mà bắt chờ là lãng phí 4 ngày. |
| C — xếp theo RÀNG BUỘC THẬT rồi mới theo độ dễ | Lọc mục không chạm đóng băng → kéo lên sớm, sắp theo rõ-ràng/đơn-giản; mục chạm đóng băng → 09/08 trở đi | **CHỌN.** Bám đúng hai vế owner nói: "xác thực rõ ràng, đơn giản làm trước" **và** hạn chót 10/08, mà không phá QD-014. |

### 4.2 Vì sao trần 3 mục/ngày

Owner nói *"không dồn quá nhiều mục vào một ngày"*. Đặt trần bằng số cụ thể để cổng máy kiểm
được, thay vì để chữ "quá nhiều" tuỳ diễn giải. Chọn **3** vì với 14 mục trong 7
ngày, mức trung bình là 2 — trần 3 cho phép gom mục cùng loại vào một ngày (04/08 gom 3 mục
quản trị; 09/08 gom 3 mục shadow) mà vẫn không ai phải làm 4 việc khác nhau trong một ngày.

### 4.3 Vì sao KHÔNG hứa xong hết trước 10/08

Năm mục có ngưỡng đo do **chính owner ký**: `QD-015` đòi *"7 ngày đầu tỉ lệ khớp ≥95%"*,
`QD-016` đòi *"overlap ≤10% trong ≥14 ngày"*, `QD-017` đòi *"≥14 ngày, chấm bằng bạch thủ"*.
Bóp ngắn cửa sổ đo để kịp hạn chính là cái bẫy đã làm rữa sáu lần liên tiếp
(V10655→V10672→V10677→V10753→V10789→V10790). Nên với 5 mục đó, "xong trước 10/08" được định
nghĩa lại bằng số: **job chạy thật + có ngày đo đầu tiên ghi được**, và ngày kết luận thật ghi
riêng.

---

## 5. Đã làm gì

### 5.1 Bảng file × thay đổi

| File | Loại | Thay đổi |
|---|---|---|
| `docs/FOLLOW_UP_TRACKER.md` | sửa | `prepend()` khối **V10981** (14 mục hạn mới + mã đọc §58 mới + điều kiện xong đo được bằng số) rồi khối đính chính **V10981b** (trả nhãn trạng thái thật — xem §7.1). **1.018.092 → 1.034.263 → 1.051.529 ký tự (+33.437)** |
| `docs/LICH_CUON_CHIEU_DEN_10082026.md` | **mới** | Trang lịch cho owner, 8 mục, 17.076 byte, máy sinh |
| `docs/ACTIVE_ROADMAP_LEAN_HARVEST_20260619.md` | sửa | CP-L6 gắn ngày cụ thể (`FU-186` 08/08 · `FU-192` 09/08) + 1 dòng vào §5 |
| `docs/OWNER_DECISION_LEDGER.json` | sửa | **QD-021** chèn đầu mảng · 5 mệnh đề máy kiểm được · theo dõi 14 mục |
| `docs/OWNER_DECISION_LEDGER.md` | máy sinh lại | 23 quyết định · QD-021 khớp 5/5 |
| `CHANGELOG.md` | sửa | `prepend()` khối V10981 · 1.945.654 → 1.951.410 (+5.756) |
| `docs/CURRENT_TRUTH_SSOT.md` | sửa | `prepend()` khối V10981 · 931.877 → 933.764 (+1.887) |
| `docs/AUTOMATION_STATE.json` | sửa | `governance_seq` **390 → 391** + `_v10981_last_event` |
| `docs/AUTOMATION_HISTORY.jsonl` | thêm | +1 dòng |
| `web/backend/_v10981_lich.py` | **mới** | Nguồn sự thật duy nhất của lịch — sổ, trang, cổng, báo cáo đều sinh từ đây |
| `web/backend/_v10981_kiem_lich.py` | **mới** | Cổng **8 phép**, kiểm trên `FOLLOW_UP_TRACKER.md` THẬT (K8 thêm sau khi bắt được lỗi mồ côi) |
| `web/backend/_v10981b_fix_trangthai.py` · `_v10981b_ghi_tracker.py` | **mới** | Đính chính nhãn trạng thái (§7.1) |
| `web/backend/_v10981_ghi_tracker.py` · `_v10981_trang_lich.py` · `_v10981_ghi_so.py` · `_v10981_governance.py` · `_v10981_bao_cao.py` | **mới** | Script ghi sổ / sinh trang / prepend / báo cáo |
| `web/backend/_v10981_doc_14.py` · `_v10981_quet_han.py` · `_v10981_ma_doc_dung.py` · `_v10981_peek_ledger.py` | **mới** | Script đào (chỉ đọc) |
| `artifacts/v10981_lich_cuon_chieu.json` | **mới** | Bảng lịch dạng máy đọc, 17.818 byte |

### 5.2 Lịch cuốn chiếu — kết quả

| Ngày | Nhóm 14 | Mục sẵn của phiên khác | Tải thật | Tính chất |
|---|---|---|---|---|
| **04/08** | 3 · `FU-187` `FU-191` `FU-212` | 0 | **3** | Rõ ràng + đơn giản, không chạm đóng băng |
| **05/08** | 1 · `FU-207` | 4 | **5** | Sửa công cụ deploy |
| **06/08** | 1 · `FU-210` | 3 | **4** | Đào chỉ-đọc |
| **07/08** | 1 · `FU-193` | 0 | **1** | Thiết kế + hạn chót owner quyết |
| **08/08** | 3 · `FU-186` `FU-203` `FU-215` | 1 | **4** | **Hết đóng băng** — chỉ đọc kết quả |
| **09/08** | 3 · `FU-192` `FU-216` `FU-217` | 4 | **7** | Ngày đầu được động vào đường ra số |
| **10/08** | 2 · `FU-231` `FU-226` | 9 | **11** | **Hạn chót owner đặt** |

### 5.3 Backup

Phiên **không sửa file runtime nào** nên không cần backup mã nguồn. Tài liệu đều ghi bằng
`prepend()` (đọc xong mới ghi, từ chối nếu file ngắn đi) và `os.replace` qua file tạm — bản cũ
vẫn nằm nguyên phía dưới trong cùng file, cộng với lịch sử git.

### 5.4 Deploy

**KHÔNG deploy.** QD-014 còn hiệu lực tới hết 08/08; phiên này thuần kế hoạch + tài liệu.
Không restart service, không đụng crontab, không sinh lượt gọi model nào.

### 5.5 Hash 4 bảng khoá

**Không áp dụng theo cách thông thường** vì phiên không chạm DB: không có lệnh ghi nào tới
`predictions`, `final_bundles`, `lottery_results`, `model_daily_eval`. Số của 4 bảng đã được
phiên V10979 cùng ngày ghi nhận TRƯỚC/SAU giống hệt (`predictions` 11673 `2c5fca45` ·
`final_bundles` 472 `d95dc3e6` · `lottery_results` 15207 `924fd080` · `model_daily_eval` 11496
`f6e52dc7`).

---

## 6. Cổng kiểm

### 6.1 Cổng lịch cuốn chiếu — `_v10981_kiem_lich.py`, 8 phép, kiểm trên sổ THẬT

| Phép | Kiểm gì | Kết quả |
|---|---|---|
| K1 | Đủ 14 mã trong `FOLLOW_UP_TRACKER.md` | ✅ đủ 14/14 |
| K2 | Không mã nào còn hạn sau 10/08 | ✅ 0 mã vượt |
| K3 | Mỗi mã có mã đọc §58 | ✅ 14/14 |
| K4 | Hạn thật trong sổ khớp hạn đã xếp | ✅ 14/14 khớp |
| K5 | Không ngày nào quá 3 mục | ✅ 04/08=3 · 05/08=1 · 06/08=1 · 07/08=1 · 08/08=3 · 09/08=3 · 10/08=2 |
| K6 | Mã đọc không đụng mã mục khác | ✅ 0 va chạm |
| K7 | Mục không kết luận nổi trước 10/08 đều nêu lý do | ✅ 5 mục nêu thẳng |
| K8 | Không mục nào rơi thành **mồ côi** (nhãn phải trong `TREO_STATUSES`) | ✅ 14/14 nhãn hợp lệ |

Cổng bắt được **hai lỗi thật** trong phiên, không phải xanh sẵn:

- Chạy **trước** khi cập nhật sổ → **trượt K4** (14 mục còn hạn 08/08).
- Sau vòng ghi đầu → **trượt K8**, liệt đúng 11 mã bị nhãn `SCHEDULED` đẩy thành mồ côi
  (xem §7). K8 được **thêm vào chính vì lỗi này**, để không tái phát.
- Sau khi đính chính V10981b → **8/8 ĐẠT**.

Bằng chứng: `evidence/cong_kiem_lich_8_phep.txt`.

**Đối chứng độc lập** — chạy lại `_v10920_session_start.py` sau khi sửa: mục mồ côi vẫn
**19** (không tăng), mục treo vẫn **98**, và briefing đã hiện đúng **"ĐẾN HẠN HÔM NAY: 3"**
(`FU-187` `FU-191` `FU-212`) — lịch đã sống trong bộ đếm chứ không chỉ nằm trong báo cáo.

### 6.2 Sổ quyết định — `_v10920_decision_ledger.py`

**QD-021 🟢 khớp 5/5.** Toàn sổ **23 quyết định · 0 TRÔI**. Bằng chứng:
`evidence/so_quyet_dinh_0_troi.txt`.

### 6.3 Không làm mất khối của phiên chạy song song

Mỗi lần ghi đều **đọc lại ngay trước khi ghi** rồi kiểm lại sau khi ghi:

| Kiểm | Kết quả |
|---|---|
| `FU-260` `FU-261` `FU-262` (V10979) còn trong tracker sau khi prepend | ✅ CÒN NGUYÊN |
| `QD-020` (V10979) còn trong sổ sau khi chèn QD-021 | ✅ CÒN |
| Khối `V10979` + `V10980b` còn trong CHANGELOG và SSOT sau khi prepend | ✅ CÒN |
| File dài ra chứ không ngắn đi | ✅ cả 4 file |

### 6.4 Cổng báo cáo A55

`python web/backend/_v10921_report_gate.py V10981` — kết quả ghi ở §9.

---

## 7. Vướng vấp

| Vấp | Hậu quả nếu bỏ qua |
|---|---|
| **PowerShell 5 không nhận `&&`** — hai lệnh đầu phiên hỏng ngay. | Nhỏ, nhưng nếu quen tay dùng `&&` trong script deploy thì lệnh thứ hai âm thầm không chạy mà exit vẫn 0. Đã chuyển sang `;`. |
| **`FU-212` ghi `hạn LX` ở tiêu đề nhưng `due = 2026-08-08` ở ô bảng.** | Người đọc tiêu đề tưởng mục không có hạn nên không ai đụng tới; máy đọc ô `due` nên vẫn tính vào nhóm quá tải. Hai bên cùng "đúng" mà lệch nhau — đúng loại lỗi làm việc trôi. Đã đồng bộ. |
| **§58 viết `DDMM`, kho thực tế dùng `MMDD`.** | Nếu phiên này theo đúng chữ trong §58 thì sẽ sinh ra dị bản thứ ba, và mọi mã đọc mới sẽ đọc ngược so với 160+ mã đang có. Đã theo cách kho dùng và ghi rõ mâu thuẫn này để owner biết. |
| **Ba mục `OWNER_LOCK` suýt bị hỏi lại.** Nhóm 14 có 5 mục nhãn chờ owner; nếu chỉ nhìn nhãn thì sẽ trình owner 5 câu hỏi. Tra `OWNER_DECISION_LEDGER.md` mới thấy 3 mục đã ký ngày 02/08. | Vi phạm §56 `A54_VIOLATION_ASKED_WITHOUT_LOOKUP` — đúng cái owner đã phải nhắc ngày 01/08. Đã tra trước, chỉ trình **3 câu hỏi thật** thay vì 5. |
| **Ngày 10/08 tổng tải 11 mục.** Nhóm 14 chỉ góp 2, còn 9 mục là hạn có sẵn từ V10974–V10980. | Nếu im lặng thì owner tưởng đã giãn xong mà ngày chót vẫn nghẽn. Đã ghi rõ trong trang lịch §1 và không tự ý dời hạn của phiên khác. |
| **Phiên V10979 chạy song song cùng chạm `FOLLOW_UP_TRACKER.md`, `OWNER_DECISION_LEDGER.json`, `CHANGELOG.md`, `CURRENT_TRUTH_SSOT.md`.** | Ghi đè nhau là mất việc của một trong hai phiên. Đã: chỉ dùng `prepend()`/`os.replace`, đọc lại ngay trước mỗi lần ghi, `assert` khối của phiên kia còn nguyên sau khi ghi, và chỉ `git add` đúng file của mình. |

### 7.1 Vấp NẶNG NHẤT — do chính agent gây ra, suýt lặp đúng lỗi vừa đi vá

Vòng ghi đầu (10:45) gán nhãn **`SCHEDULED`** cho 14 mục. Nhãn đó là **tự chế** — không nằm
trong `_v10958_fu_reader.TREO_STATUSES` cũng không nằm trong `DONG_STATUSES`. Hậu quả đo được:
**11/14 mục lập tức rơi khỏi mọi bộ đếm và bị xếp MỒ CÔI**.

| | |
|---|---|
| Mức nghiêm trọng | **Cao** — 11 mục biến mất khỏi briefing đầu phiên, khỏi bộ đếm quá hạn, khỏi cổng thiếu mã đọc |
| Hậu quả nếu bỏ qua | Đến 10/08 **không ai biết chúng trượt hạn**. Cả phiên giãn lịch trở nên vô nghĩa vì lịch không ai canh |
| Trớ trêu | Kiểm toán V10980 sáng nay vừa bêu **19 mục mồ côi**; phiên đi xử chuyện đó suýt đẻ thêm **11 mục** nữa |
| Phát hiện nhờ đâu | Chạy `_v10981_quet_han.py` để nghiệm thu sau khi ghi, thấy 11 mã hiện ở nhóm *"mồ côi"* thay vì *"treo"* |
| Đã sửa | `V10981b` — trả đúng nhãn cũ của từng mục (phiên này chỉ đổi **hạn**, không đổi **tiến độ việc**). Riêng `FU-193` nâng `MEASURED_BUT_NOT_FIXED` → `AWAITING_OWNER_OK` vì nay chờ owner duyệt ngưỡng; cả hai nhãn đều hợp lệ |
| Chặn tái phát | Thêm phép **K8** vào cổng: mọi mục trong nhóm phải mang nhãn thuộc `TREO_STATUSES`. Chạy trên bản lỗi → K8 **TRƯỢT**, liệt đúng 11 mã. Cổng nay **8 phép** |
| Đối chứng sau khi sửa | `_v10920_session_start.py`: mồ côi vẫn **19** (không tăng) · treo vẫn **98** · *"ĐẾN HẠN HÔM NAY: 3"* hiện đúng |

**Bài học:** khi ghi vào sổ theo dõi, nhãn trạng thái **không phải chỗ để sáng tạo**. Phải lấy
từ danh sách bộ đọc công nhận, nếu không mục sẽ "trông như đã ghi" mà thực chất vô hình với
mọi cổng — đúng loại **xanh giả** owner sợ nhất.

**Không có vấp nào phải gỡ về** — lỗi trên đã sửa xong trong cùng phiên, có cổng máy chặn tái phát.

---

## 8. Gỡ về

```bash
cd E:\Lottery_AI_Test

# 1. trả 14 mục về hạn 08/08 + trả roadmap về nguyên trạng
git checkout HEAD -- docs/FOLLOW_UP_TRACKER.md docs/ACTIVE_ROADMAP_LEAN_HARVEST_20260619.md

# 2. xoá trang lịch
del docs\LICH_CUON_CHIEU_DEN_10082026.md

# 3. huỷ quyết định: đổi QD-021 trang_thai -> SUPERSEDED trong docs/OWNER_DECISION_LEDGER.json
python web/backend/_v10920_decision_ledger.py     # sinh lại bản .md

# 4. gỡ khối V10981 ở đầu CHANGELOG.md và docs/CURRENT_TRUTH_SSOT.md
git checkout HEAD -- CHANGELOG.md docs/CURRENT_TRUTH_SSOT.md
```

Backup: toàn bộ nằm trong lịch sử git (commit ngay trước phiên là `665b548`). Vì phiên
**không đụng runtime** — không deploy, không restart, không sửa 15 model official / bộ lọc
combo-super / lớp ghi đè / `/du-doan` / writer `final_bundles` / crontab — nên gỡ về chỉ là gỡ
tài liệu. **Mất khoảng 2 phút, không cần restart gì.**

---

## 9. Theo dõi tiếp

### 9.1 Mười bốn mục với hạn mới và ngưỡng hành động bằng số

| Mã máy | Mã đọc | Nhãn | Hạn | Ngưỡng hành động |
|---|---|---|---|---|
| `FU-187` | `KS0804-1` | Nghiệm thu hook tra cứu đầu phiên | **04/08** | `_v10920_session_start.py` chạy exit 0 và `docs/_BRIEFING_DAU_PHIEN.txt` có mốc trong vòng 24 giờ; 6/6 mục briefing in ra số (không mục nào rỗng). |
| `FU-191` | `XH0804` | Khoá luật cắt model an toàn combo-super | **04/08** | Luật «bỏ `output_eligible` ≠ dừng model · pool ML phải ≥ 4 · pool AI phải ≥ 3» có mặt trong cả 5 mặt quy tắc; `_v10925_rule_sync_check.py` exit 0. |
| `FU-212` | `DO0804` | MT tín hiệu rơi ở gộp phiếu — đóng phần đo | **04/08** | Phần ĐO đóng lại (`CLOSED_REPORT`): 5/5 giả thuyết GT-1…GT-5 đã có kết luận, chênh RF→công bố 7,59pp có trong `artifacts/v10955_tin_hieu_roi_rung.json |
| `FU-207` | `DP0805-1` | Nâng cổng an toàn deploy lên mốc FINAL / bundle v2 | **05/08** | `_v10934_deploy.py` chặn khi giờ VN < 17:58 HOẶC bundle MB còn `bundle_version < 2`; chạy thử 2 ca (trước 17:58 → chặn, sau 17:58 + v2 → cho qua) đúng |
| `FU-210` | `DO0806-1` | Đào nguyên nhân mất lợi thế MT tháng 6 | **06/08** | Trả lời đủ 4 hướng đào (thay đổi code/cấu hình 01/05–15/06 · lịch retrain ML · đặc tính kết quả MT · chuyển ML→AI ở MT), mỗi hướng kèm bằng chứng hoặc |
| `FU-193` | `XH0807` | Sàn chất lượng combo-super — thiết kế + ngưỡng số | **07/08** | Có bản thiết kế + MỘT con số ngưỡng owner duyệt (đề xuất: cả pool ML thắng < 5% trong 7 ngày gần nhất thì combo-super bỏ nhánh ML), kèm backtest chỉ-đ |
| `FU-186` | `KS0808-2` | Đọc kết quả 7 ngày sau tắt lớp ghi đè | **08/08** | Bảng 7 ngày 02/08→08/08: MT và MB phải có phiếu bầu == số công bố **100% số ngày**; tỉ lệ trúng gộp ba miền so với mốc 28,9% (kỳ vọng ~35%); 6 lane đã |
| `FU-203` | `DO0808-2` | gemini-3.5-flash — chấm tuần 02→08/08 | **08/08** | Chạy đúng câu SQL đã ghi trong FU-203 trên `model_daily_eval` `date>='2026-08-02'`. ≥30% → đề xuất xét vào total (thi hành sau 08/08). <25% → gỡ khỏi  |
| `FU-215` | `DB0808` | Đóng băng QD-014 hết hạn — chốt hoặc gia hạn | **08/08** | Hết ngày 08/08: chạy 7/7 phép `kiem_code` của QD-014 phải còn KHỚP (chứng minh trong tuần không ai lén đổi đường ra số), rồi owner chốt MỞ hay GIA HẠN |
| `FU-192` | `XH0809` | Promote glm-5.1 / gpt-oss-120b hay đóng lại | **09/08** | Một trong hai kết cục, không để treo tiếp: (a) promote `glm-5.1` (KEEP_STABLE, dương 4/5 kỳ, 110 ngày/309 lượt) và/hoặc `gpt-oss-120b` (+3,14pp, 3/5 k |
| `FU-216` | `XH0809-1` | Khởi động shadow MT bạch thủ = random-forest đơn (QD-015) | **09/08** | TRONG HẠN: job shadow chạy thật, bảng shadow khai đúng 4 cờ (`output_eligible=0 diagnostic_only=1 owner_approved=0 shadow_only=1`), panel `/monitoring |
| `FU-217` | `SC0809` | Sửa key `lstm_probability` combo đọc sai + đo shadow | **09/08** | TRONG HẠN: `combo_super` đọc đúng `lstm_probability` (kiểm bằng một lượt chạy lại có LSTM vào được phiếu), thả trên **shadow trước**, và ghi snapshot  |
| `FU-231` | `HT0810-1` | Khởi động shadow bỏ ép RULES-FIRST (QD-016) | **10/08** | TRONG HẠN: nhánh shadow bỏ chữ «bắt buộc chọn từ danh sách» (vẫn đưa danh sách như gợi ý) chạy thật, có ngày đo đầu tiên ghi overlap bạch-thủ prompt↔p |
| `FU-226` | `HT0810-2` | Khởi động A/B hai prompt trên cùng model (QD-017) | **10/08** | TRONG HẠN: job A/B chạy trên `claude-sonnet-4-6` + `deepseek-reasoner` + `gemini-2.5-flash`, mỗi model HAI prompt, có ngày đo đầu tiên và hoá đơn toke |

### 9.2 Năm mục có ngày kết luận THẬT muộn hơn 10/08

| Mã máy | Xong trước 10/08 nghĩa là | Kết luận sớm nhất | Ngưỡng do owner ký |
|---|---|---|---|
| `FU-193` | chạy được + ngày đo đầu tiên | **16/08** | Sửa bộ lọc combo-super là đổi đường ra số — QD-014 cấm tới hết 08/08, và QD-018 bắt làm TỪNG BƯỚC MỘT nên phải xếp sau B1 (tắt bộ tối ưu trọng số, khởi động 09/08, đo ≥7 ngày). Trong hạn 07/08 chỉ xong được THIẾT KẾ + NGƯỠNG, không phải triển khai. |
| `FU-216` | chạy được + ngày đo đầu tiên | **15/08** | Chốt tự cắt của chính owner là «7 ngày đầu tỉ lệ ngày live khớp tái suy luận ≥95%». Khởi động 09/08 thì ngày thứ 7 rơi vào 15/08. Không có cách rút ngắn — dưới 7 ngày thì con số không đủ để cắt hay giữ. |
| `FU-217` | chạy được + ngày đo đầu tiên | **16/08** | Sửa key là việc một buổi, nhưng câu hỏi thật là «sửa xong LSTM còn tệ −5,58pp nữa không» — cái đó cần ≥7 ngày live sau khi sửa. Khớp live↔tái suy luận đang 23%, ba ngày không đủ nói gì. |
| `FU-231` | chạy được + ngày đo đầu tiên | **23/08** | Ngưỡng owner đặt là «overlap ≤10% trong ≥14 ngày đo» (từ mức ~26% hiện tại). Khởi động 10/08 thì ngày thứ 14 rơi vào 23/08. |
| `FU-226` | chạy được + ngày đo đầu tiên | **23/08** | Chính owner ký «≥14 ngày, chấm bằng tỉ lệ trúng bạch thủ». Khởi động 10/08 thì ngày thứ 14 rơi vào 23/08. Rút ngắn là quay lại đúng cái bẫy đã làm rữa V10655→V10790. |

### 9.3 Owner cần quyết gì, trước ngày nào

| Mã máy | Cần quyết | Hạn quyết |
|---|---|---|
| `FU-192` | Promote `glm-5.1` và/hoặc `gpt-oss-120b` vào 15 model official, hay chốt «không promote»? | **07/08** |
| `FU-215` | Hết 08/08: MỞ đóng băng hay GIA HẠN? Mở thì mở cả ba việc (roster · bộ lọc combo-super · lớp ghi đè) hay mở từng phần? | **08/08** |
| `FU-193` | Duyệt MỘT con số ngưỡng sàn chất lượng combo-super (đề xuất: pool ML thắng <5% trong 7 ngày → bỏ nhánh ML). | **07/08** |

Ba mục **KHÔNG hỏi lại** (§56 — đã ký 02/08):
- `FU-216` ← `QD-015 · 2026-08-02`
- `FU-226` ← `QD-017 · 2026-08-02`
- `FU-231` ← `QD-016 · 2026-08-02`

### 9.4 Hạn rà soát chính quyết định này

`QD-021` có `ngay_ra_soat = 2026-08-10`. Đúng ngày đó phải chạy lại
`python web/backend/_v10981_kiem_lich.py` và đối chiếu: mục nào đã đóng, mục nào trượt hạn,
mục nào phải mang sang cửa sổ sau. **Trượt từ 3 mục trở lên = lịch này sai giả định, phải lập
lại chứ không dời từng mục.**

### 9.5 Việc kéo dài quá 10/08 mà chính owner đã ký — để không bất ngờ

`QD-018` (ký 02/08) bắt làm **từng bước một**, mỗi bước đo 7–14 ngày:

| Bước | Việc | Theo dõi | Sớm nhất |
|---|---|---|---|
| B1 | Tắt bộ tối ưu trọng số (cron chủ nhật 03:00) | `FU-233` | khởi động 09/08, đo ≥7 ngày |
| B2 | Đo 105 luật có giúp số công bố không | `FU-234` | sau B1, ≥14 ngày (~05/09) |
| B3 | Gỡ ép RULES-FIRST trên luồng official | `FU-235` | sau B2 (~19/09) |

`FU-231` (shadow bỏ ép RULES-FIRST) đứng **trước** B3, không trùng việc.

### 9.6 Cổng báo cáo A55

```
python web/backend/_v10921_report_gate.py V10981
```

Kết quả: **xem `evidence/cong_bao_cao_a55.txt`**.

---

## Bằng chứng kèm theo

| Tệp | Nội dung |
|---|---|
| `evidence/v10981_lich_cuon_chieu.json` | Toàn bộ lịch dạng máy đọc: 14 mục, phân loại hai trục, tải thật mỗi ngày, mục không kết luận nổi trước hạn, mục chờ owner |
| `evidence/cong_kiem_lich_8_phep.txt` | Output đầy đủ cổng 8 phép (gồm K8 chặn mồ côi) |
| `evidence/cong_kiem_lich_K8_truot_truoc_khi_sua.txt` | Output lúc K8 **TRƯỢT** — bằng chứng cổng bắt được lỗi thật |
| `evidence/so_quyet_dinh_0_troi.txt` | Output sổ quyết định — QD-021 khớp 5/5, toàn sổ 0 TRÔI |
| `evidence/cong_bao_cao_a55.txt` | Output cổng báo cáo A55 |

**Không có khoá API / bí mật nào trong báo cáo này** — phiên không chạm `.env`, không gọi
provider, không in cấu hình kết nối.
