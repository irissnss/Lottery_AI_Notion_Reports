# Ngữ cảnh phiên V10990 — 2026-08-05 (giờ Việt Nam)

## 1. Nguyên văn lời owner

### 1.1 Mở đầu chuỗi việc (10:07)

Owner gửi ảnh chụp màn hình trang `/du-doan-test` tab MN và viết đúng bốn chữ:

> **"em tự nhìn đi"**

Trang lúc đó hiện: *"Chưa có dự đoán HÔM NAY (05/08/2026) — MN cập nhật lúc ~04:30"*, lùi về *"THAM KHẢO ngày 01/08/2026 (đã có kết quả)"* với bạch thủ 38, ngay dưới lại ghi *"Chưa xổ — kết quả win/lose cập nhật sau 19:00"*, và khuyến cáo *"nên chơi OFFICIAL — Official 38%"* đặt cạnh *"ADAPTIVE EXPLOIT V1 62% (hứa hẹn nhưng CHƯA đủ cỡ số)"*.

Việc này dẫn tới V10989 và V10989b. Phiên V10990 là phần owner quyết sau khi đọc hai báo cáo đó.

### 1.2 Hai quyết định (≈12:05)

Owner được hỏi hai câu và chọn:

**Câu 1 — khối "Output Lane Test" đọc từ lane đã bị gỡ cron ngày 01/08, anh muốn xử sao?**

> **"Bỏ hẳn khối đó khỏi trang — nguồn đã nghỉ thì đừng hiển thị nữa"**

**Câu 2 — cổng khuyến cáo hiện chỉ cần n≥8 lượt, quá mỏng để khuyên đặt tiền. Nâng lên không?**

> **"Nâng hẳn lên n≥40 — nghiêm như chú thích cũ vẫn ghi"**

### 1.3 Hai lần gián đoạn

> **"Hết API gián đoạn , em tiếp tục chạy dùm anh với nha"** (11:38)

Và sau đó phiên bị cắt thêm hai lần nữa vì hết hạn mức API (≈12:40 và ≈13:13), không có lời owner kèm theo — hệ thống tự báo lỗi `resource_exhausted`.

---

## 2. Agent đã làm gì

1. Soi nguồn của khối "Output Lane Test": tìm ra `_v10692_mn_mt_multidir_lane.py` là **nguồn duy nhất** ghi `{MIỀN}_OUTPUT_V1`, cả 4 dòng cron bị gỡ 01/08 theo V10919. Chạy `--dry-run` xác nhận lane vẫn chạy tốt — thuần là cron tắt.
2. Soi **cả ai đọc BẢNG** chứ không chỉ ai import module (bẫy đã ghi sẵn trong quy tắc, và chính là nguyên nhân gốc của sự cố này).
3. Sửa `du-doan-test.html`: bỏ khối số, thay bằng dòng nói thật trạng thái nguồn; lane nghỉ không còn là lựa chọn mặc định.
4. Sửa `_v10725_champion_selector.py`: `REC_WD_MIN_N` từ `8` thành `REC_MIN_LONG_N` (= 40), cập nhật docstring.
5. Deploy 12:52:07 (ngoài khung cấm), restart `lottery`, PID 842736 → 846146.
6. Nghiệm thu bằng cách **bóc hàm dựng khối ra khỏi tệp đang phục vụ, đổ dữ liệu thật vào, bỏ thẻ HTML rồi đọc chữ** — cả ba miền, trước và sau.
7. Ghi `QD-027` vào sổ quyết định (khớp 14/14), prepend ba mặt tài liệu quản trị.

---

## 3. Vấp ở đâu

### 3.1 Hết hạn mức API hai lần

Phiên bị cắt lúc ≈12:40 và ≈13:13. Sau mỗi lần, trạng thái được **kiểm độc lập** chứ không tin trí nhớ:

- **12:42** — VPS hoàn toàn chưa bị động tới: `du-doan-test.html` trên máy chủ vẫn 225.695 byte (đúng bản backup), `REC_WD_MIN_N` vẫn là 8, PID vẫn 842736 từ 11:49. Local đã sửa xong hai file, backup đã có.
- **13:14** — deploy đã chạy lúc 12:52:07 giữa hai lần cắt. Local và VPS khớp nhau.

Nếu không kiểm lại lần hai thì đã tưởng chưa deploy và deploy đè thêm lần nữa — thêm một restart vô ích sát giờ MN.

### 3.2 Nâng cổng chưa trọn — phát hiện khi đọc chữ thật

Sau khi deploy, đọc chữ thật tab MB vẫn thấy:

> 🎯 Bạch Thủ: **45** ← MB_SCREEN_WEIGHTED_V1 (62% BT hit/T3, **n=8**)

Tức là **lời khuyên** nay cần 40 lượt, nhưng **con số được chọn để hiển thị** vẫn chỉ cần 4–8 lượt — `pick_champion()` trong cùng file dùng `min_n=4` (theo thứ) và `min_n=8` (nền miền).

Tệ hơn: chú thích mới viết ở dòng 224 tuyên bố *"một sàn duy nhất, không còn chỗ nghiêm chỗ lỏng"* — câu đó **hiện đang nói quá**. Đây là một mẫu "xanh giả" ở tầng chữ nghĩa, cùng họ với chuỗi đã phát hiện suốt hai ngày qua.

Agent **không tự sửa** vì đổi ngưỡng này đổi con số hiển thị, mà owner vừa ra quyết định ngưỡng ở chỗ khác — mở rộng sang đây phải hỏi. Mở `FU-274 · QD0808-1`, hạn 08/08, `OWNER_LOCK`.

### 3.3 Kết quả tốt hơn owner được cảnh báo

Owner đã chấp nhận trước rằng khối khuyến cáo sẽ nhàm đi, gần như luôn ra OFFICIAL. Thực tế cả ba miền chỉ rời khỏi lát cắt theo-thứ mỏng và rơi xuống nền miền rộng hơn nhiều — MN n=29→120, MT n=35→169, MB n=8→62. **MB vẫn khuyến cáo LANE**, chỉ là nay dựa trên 62 lượt thay vì 8.

---

## 4. Điều đáng ghi cho phiên sau

- Cách nghiệm thu đúng là **đọc chữ thật từ tệp đang phục vụ**, không phải so kích thước file hay xem header. Chính cách này bắt được lỗi ở V10989b và lại bắt được `FU-274` hôm nay.
- Khi nâng một ngưỡng, phải soi **mọi nơi khác trên cùng đường đi** dùng ngưỡng nào — nếu không sẽ tạo ra "chỗ nghiêm chỗ lỏng" mới, và tệ hơn là một chú thích tuyên bố sai.
- Sau mỗi lần gián đoạn, **kiểm trạng thái thật** trên cả local và VPS trước khi làm tiếp. Hai lần cắt trong phiên này rơi vào hai trạng thái khác hẳn nhau.
