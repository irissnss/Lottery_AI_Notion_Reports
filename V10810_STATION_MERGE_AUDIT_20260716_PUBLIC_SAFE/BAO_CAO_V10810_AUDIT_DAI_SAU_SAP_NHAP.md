# V10810 — AUDIT ĐÀI SAU SÁP NHẬP TỈNH 1/7: ĐÀI, TÊN ĐÀI, THỨ + REPAIR THIẾU SÓT TÌM THẤY

- Ngày: 2026-07-16 11:49 → 12:4x
- Yêu cầu owner (11:49): "Sau 1/7 VN sáp nhập tỉnh, 1 số đài cũ được gộp về tỉnh mới nên 1 tuần khả năng đài sổ 2 lần khá nhiều. Xem thật kỹ hệ thống đang ghi nhận như nào có đúng với hiện tại không? Tự kiểm tra đài chính xác hiện hành trên các nền tảng so sánh đối chiếu — đài, tên đài, thứ, tất cả kiểm tra lại luôn, anh sợ đâu đó còn thiếu sót."
- Phạm vi: READ-ONLY audit (DB live VPS + web ngoài) → phát hiện thiếu sót thật → repair có backup + backfill + chống tái diễn. KHÔNG động /du-doan, final_bundles, model selector, prompt production.

---

## PHẦN 1 — TRẢ LỜI CÂU HỎI CHÍNH: LỊCH ĐÀI × THỨ CÓ ĐỔI SAU 1/7 KHÔNG?

### 1.1. KHÔNG ĐỔI — đối chiếu DB 2 cửa sổ (18/05-30/06 vs 01-15/07)

- **MN 21 đài, MT 14 đài, MB 6 đài — giữ nguyên thứ 100%.** Không đài nào biến mất, không đài mới xuất hiện (ngoại lệ duy nhất = 6 dòng mã tắt, xem Phần 2).
- Số đài mỗi ngày sau 01/07 vẫn chuẩn: MN 3 (T7=4), MT 2-3, MB 1.

### 1.2. Các đài "xổ 2 lần/tuần" hiện tại — ĐÃ NHƯ VẬY TỪ 2020, không phải hiện tượng mới

| Đài | Thứ | Tổng số kỳ trong DB (từ 2020) |
|---|---|---|
| TP. HCM (MN) | T2 + T7 | 644 |
| Khánh Hòa (MT) | T4 + CN | 672 |
| Thừa Thiên Huế (MT) | T2 + CN | 375* |
| Đà Nẵng (MT) | T4 + T7 | 670 |
| Hà Nội (MB) | T2 + T5 | 667 |

(Đài tuần-1-lần chỉ có ~322-337 kỳ → đài 2 lần/tuần có gần gấp đôi, nhất quán từ 2020. *Huế lịch sử có giai đoạn ghi tách.)

### 1.3. Đối chiếu web ngoài: phương án "gộp đài, xổ nhiều lần/tuần" LÀ DỰ THẢO, CHƯA ÁP DỤNG

- **Bộ Tài chính (công văn 16/6, đưa tin Tuổi Trẻ):** "Lịch quay số mở thưởng xổ số **vẫn duy trì như hiện nay** cho đến thời điểm công ty xổ số chính thức hoạt động theo mô hình mới."
- Phương án dự thảo XSMN (từng dự kiến 1/1/2026, đã lùi, Cần Thơ còn kiến nghị chỉnh): 21 công ty → 9 công ty; TP.HCM 4 lần/tuần (gộp BR-VT + Bình Dương); Vĩnh Long/Cần Thơ/Lâm Đồng 3 lần/tuần; Đồng Tháp/Cà Mau/Đồng Nai/Tây Ninh/An Giang 2 lần/tuần.
- **XSMT: chưa có phương án chính thức** — "vẫn giữ nguyên, chờ thông tin mới".
- **Thực chứng 15/07/2026 (T4):** web xổ Đồng Nai–Cần Thơ–Sóc Trăng (đúng lịch CŨ; lịch dự thảo mới là ĐN–CT–VL–LĐ). Số ĐB khớp DB hệ thống 100%: Đồng Nai 008402, Cần Thơ 867898, Sóc Trăng 282199.

**→ Kết luận 1: hệ thống đang ghi ĐÚNG với hiện tại. Khi phương án mới có hiệu lực THẬT, lịch MN sẽ đổi lớn (Bình Dương/Vũng Tàu/Trà Vinh/Bến Tre/Long An/Bình Phước/Hậu Giang... biến mất, gộp về đài mới) — hệ thống đã có 2 chuông báo tự động (mục 3.4) sẽ la ngay ngày đầu.**

---

## PHẦN 2 — THIẾU SÓT THẬT TÌM THẤY (đúng nỗi sợ "đâu đó còn thiếu sót")

### 2.1. 6 dòng kết quả ghi MÃ TẮT thay vì tên đài đầy đủ

| Ngày | Miền | Ghi trong DB | Đài thật | ĐB trong DB | ĐB web ngoài (verify) |
|---|---|---|---|---|---|
| 25/06 | MT | `QB` | Quảng Bình | 318032 | 318032 ✔ |
| 25/06 | MT | `QT` | Quảng Trị | 787705 | 787705 ✔ |
| 03/07 | MT | `GL` | Gia Lai | 072277 | 072277 ✔ |
| 03/07 | MT | `NT` | Ninh Thuận | 364600 | 364600 ✔ |
| 07/07 | MT | `DLK` | Đắk Lắk | 620584 | 620584 ✔ |
| 07/07 | MT | `QNA` | Quảng Nam | 353672 | 353672 ✔ |

- Cả 6 dòng **đầy đủ 9 giải / 18 số** — số liệu ĐÚNG, chỉ sai nhãn tên đài.
- Nguồn gốc: 3 ngày đó parser dự phòng xskt.com.vn thắng cuộc đua scrape (3 nguồn chạy song song), header trang render mã tắt; bảng alias cũ (V10804) chỉ biết QB/QT và chỉ vá ở tầng ĐỌC.

### 2.2. Hậu quả dây chuyền: 8 dòng đánh giá rule bị CÂM lặng lẽ

Tầng chấm rule (`mined_rule_eval`) tra kết quả nguồn bằng **tên đầy đủ chính xác** (`station = 'Ninh Thuận'`) → ngày đài bị ghi `NT` thì rule "không thấy dữ liệu nguồn" → bỏ qua không chấm, không báo lỗi:

| Ngày ảnh hưởng | Rule | Nguồn → Đích | Đáng lẽ nhả gì (sau repair) | Có hit không |
|---|---|---|---|---|
| 25/06 | #2084 G5+GĐB | Quảng Bình → MB | [32, 17] | **17 HIT ✔ (bị bỏ lỡ)** |
| 03/07 | #2090 G5+GĐB | Ninh Thuận → MB | [00, 01] | không |
| 04/07 | #2021 GĐB+G7 | Ninh Thuận → MN | [00, 54] | không |
| 04/07 | #2091 G1+G7 | Ninh Thuận → MB | [31, 54] | **54 HIT ✔ (bị bỏ lỡ)** |
| 04/07 | #2093 GĐB+G1 | Ninh Thuận → MB | [00, 31] | không |
| 04/07 | #2094 G1+G8 | Ninh Thuận → MB | [31, 61] | không |
| 07/07 | #2074 GĐB+G8 | Đắk Lắk → MB | [84, 36] | không |
| 08/07 | #2007 GĐB+G7 | Đắk Lắk → MN | [84, 72] | **84 HIT ✔ (bị bỏ lỡ)** |

- Đau nhất: **Ninh Thuận chính là đài best-spot số 1** (V10808: G1+G7→MB +23.9pp z=3.83) — ngày 03-04/07 toàn bộ 5 rule nguồn Ninh Thuận câm, prompt MB ngày 04/07 THIẾU dòng rule mạnh nhất.
- Backfill hàng tuần cũng KHÔNG tự vá được (chạy sau re-mine 15/07 vẫn thiếu đúng 8 dòng này) vì dữ liệu nguồn vẫn mang tên sai.

---

## PHẦN 3 — ĐÃ SỬA GÌ (4 tầng, deploy 12:2x)

### 3.1. Repair dữ liệu (có backup + guard 3 lớp)
- Backup 6 dòng nguyên trạng vào bảng `v10810_station_repair_backup` + file JSON.
- UPDATE theo rowid khóa cứng, guard: đúng mã + đúng ngày + đúng ĐB đã web-verify — sai bất kỳ điều nào là ABORT.
- Kết quả: 6/6 OK; toàn DB còn **0 dòng** tên đài ≤4 ký tự.

### 3.2. Backfill 8 dòng rule-eval
- Chạy lại đánh giá rule cho 6 ngày (25-26/06, 03-04/07, 07-08/07) — idempotent (INSERT OR REPLACE theo UNIQUE(rule_id, date)).
- 8/8 dòng thiếu đã xuất hiện, trong đó 3 hit thật được trả lại lịch sử (17, 54, 84). Panel ⛏ BEST SPOTS tự cập nhật (Ninh Thuận G1+G7 n 45→46, z 3.73→3.83).

### 3.3. Chống tái diễn tầng GHI (fix gốc)
- `save_lottery_result` (choke point mọi luồng ghi kết quả: 3 parser scrape, scheduler, API, script sync) giờ **tự chuẩn hóa tên đài** trước khi ghi.
- Bảng alias thêm 13 mã tắt MT không nhập nhằng (4 mã đã quan sát + 9 mã cùng họ). Cố ý KHÔNG thêm mã 2 chữ miền Nam (BT = Bến Tre hay Bình Thuận? BD = Bình Dương hay Bình Định? — nhập nhằng, thà để lọt rồi chuông báo la còn hơn map sai).
- Chuẩn hóa biến thể "Bà Rịa - Vũng Tàu" → "Vũng Tàu" (quy ước DB, tránh tách đôi identity).

### 3.4. Chống tái diễn tầng PHÁT HIỆN (2 chuông báo)
- **Check 11 mới** trong self-check định kỳ V10800 (cron T2 08:10): "14 ngày qua không có dòng tên đài mã tắt" — chạy ngay sau deploy: **PASS rows=0**.
- Chuông có sẵn `[STATION_INCOMPLETE]` (so đài thực tế vs danh sách kỳ vọng theo thứ) — sẽ la ngay ngày đầu nếu lịch mới có hiệu lực thật (đài cũ biến mất).

---

## PHẦN 4 — AN TOÀN & BẰNG CHỨNG

- Hash 4 bảng official: `predictions` 2ffa27cc, `final_bundles` c6119479, `model_daily_eval` aaa91dc6 **PRE = POST GIỐNG HỆT**; `lottery_results` 1a1820b1 → a87cc07a = **delta chủ đích đúng 6 dòng repair** (từng dòng đã backup + đối chiếu ĐB web ngoài).
- Selfcheck sau deploy: 10/11 PASS (FAIL duy nhất = check 3 retrain-OK-hàng-tuần: bệnh CŨ đã fix V10800 bằng subprocess, model files thực tế đã retrain 13/07 06:32 qua guard; hàng OK đầu tiên sẽ ghi CN 19/07 — không phải lỗi mới).
- Shadow A/B V10809 đang chạy KHÔNG bị ảnh hưởng (arm B tính emission bằng tên đầy đủ — sau repair, những ngày tới nếu xskt lại render mã tắt thì write path đã tự chuẩn hóa).
- Sync live → local sau repair: `artifacts/live_sync/20260716_123117/manifest.json`.
- Ghi chú tồn đọng KHÔNG sửa (chủ đích): ~40 dòng 2020-2021 dán nhãn miền lẫn (đài MT nằm region MN, lần cuối 10/2021) — nằm ngoài mọi cửa sổ 4-16W đang dùng để xếp hạng; sửa lịch sử 5 năm không đổi output hiện tại, rủi ro > lợi ích.

## PHẦN 5 — VIỆC CẦN NHỚ TIẾP

1. **T2 21/07 08:10** — selfcheck cron đầu tiên có check-11, kỳ vọng PASS.
2. **Khi có tin Bộ TC áp dụng lịch mới THẬT** (theo dõi tin XSKT miền Nam): cần 1 phiên riêng cập nhật danh sách đài kỳ vọng + rule nguồn các đài cũ (Bình Dương, Vũng Tàu, Trà Vinh... sẽ ngừng xổ). 2 chuông báo sẽ tự la ngày đầu tiên.
