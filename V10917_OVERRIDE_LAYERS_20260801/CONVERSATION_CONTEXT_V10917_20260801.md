# Nguyên văn phiên 01/08/2026 — phần V10917 / V10918 / V10919

> Giữ **nguyên văn** lời owner, không diễn giải lại. Phần bàn về truy vết và quy tắc nằm ở
> `V10920_TRACEABILITY_20260801/CONVERSATION_CONTEXT_V10920_20260801.md`.

---

## 1. Owner mở phiên (08:51)

> **"Rồi làm đi thật cản thận có kiểm soát nha em"**

**Hiểu là:** duyệt kế hoạch 5 giai đoạn cắt/thay model đã trình phiên trước, bắt đầu Giai đoạn 0
— mô phỏng trên dữ liệu cũ, không đụng production.

**Agent làm:** dựng phép mô phỏng, tự đặt **hai cổng kiểm bắt buộc** — phép mô phỏng phải tái
tạo đúng quá khứ thì mới được tin.

**Vấp 1 — cả hai cổng đều trượt.** Agent dừng đúng như đã hứa thay vì nới ngưỡng:

- Cổng 1: 76/1.776 số lệch điểm, tỉ lệ lệch đều đặn 1,176–1,186
- Cổng 2: **67/180 bundle** có số đầu bảng khác bạch thủ đã công bố

Truy nguyên: cổng 1 do bộ giảm điểm `pp1_convergence_dampener` (≥3 model "bầy đàn" cùng chọn một
số → nhân 0,85; kiểm `0.1154 × 0.85 = 0.0981` khớp chính xác, và `1/0.85 = 1,176` đúng bằng tỉ lệ
lệch quan sát). Cổng 2 do **5 lớp ghi đè** chạy sau khi cộng phiếu xong.

**→ Phát hiện chính: 37% số ngày, bạch thủ công bố KHÔNG phải số thắng phiếu bầu.**

---

## 2. Owner quyết hướng xử lý (~10:0x)

Agent trình bằng chứng đo tiến 60 ngày và hỏi hai câu. Owner trả lời:

> **"Đừng có D chạy song song nữa, số liệu có rõ ràng rồi mà đo hoài, Xử lý an toàn, cải tiến,
> cải thiện, tinh gọn, sạch sẽ cho cả 3 miền nha em. Còn luồng thì anh thấy cũng bắt đầu rối
> rồi đó, mất kiểm soát rồi đó. Nào là lane test, nào là choi, nào là nghiem thu, nao là
> offical v.v... cần xem xử lý luôn đi"**

Và chọn cách triển khai: **"Làm ngay hôm nay, kịp trước mốc chốt MN 15h45"**.

**Điểm quan trọng:** owner **từ chối phương án D** — dựng luồng chạy song song đo tiếp 2 tuần.
Owner không muốn thêm chu kỳ đo khi bằng chứng đã đủ.

**Agent làm:** tắt 5 lớp ghi đè giữ V10640·MN (V10917) · dựng panel `/monitoring` đối chiếu
phiếu bầu vs số công bố (V10918) · kiểm kê toàn bộ luồng.

---

## 3. Owner chốt phạm vi dọn luồng (~10:2x)

Agent trình danh sách 6 lane chết hoặc hết hạn đo. Owner chọn:

> **Dẹp cả 6** · và **"Chờ ít nhất 7 ngày xem số liệu thật đúng như dự tính rồi mới động tiếp"**

**Agent làm:** gỡ 12 dòng cron (83→71), giữ nguyên file (V10919).

---

## 4. Bảy chỗ vấp trong phiên

| # | Vấp | Hậu quả nếu bỏ qua |
|---|---|---|
| 1 | Hai cổng kiểm mô phỏng đều trượt | **May là có cổng.** Không có thì cắt model dựa trên phép mô phỏng sai |
| 2 | Sai tên service — dùng `lottery-ai` thay vì `lottery`. `systemctl` báo *"Unit not found"* nhưng `/api/health` vẫn trả **200** vì tiến trình cũ còn sống, và bước đọc cờ vẫn thấy đúng vì nó đọc từ đĩa chứ không từ tiến trình | **Tưởng deploy xong mà code mới chưa hề chạy.** Đã thêm so PID trước/sau làm cổng bắt buộc |
| 3 | Panel báo MB 31/07 *"phiếu 19 · công bố 19 · KHÔNG ĐỔI"* trong khi nhật ký ghi số bị đổi ba lần | Suýt báo động nhầm. Truy ra chuỗi là `19 → 28 → 93 → 19` — đổi qua đổi lại rồi quay về đúng số ban đầu, nên "không đổi" là **đúng** về kết quả cuối |
| 4 | Playwright báo trượt hai lần | Lỗi **phép kiểm** chứ không phải panel: (a) dữ liệu giả thiếu trường `role: "admin"` nên trang đá về `/login`; (b) đếm cả phần tử nằm trong vùng cuộn ngang là "tràn khung". **Suýt đi sửa panel đang đúng.** Đã sửa phép kiểm chứ không nới tay |
| 5 | Định xoá luôn file `_v10692_mn_mt_multidir_lane.py` | Soi tham chiếu chéo thấy **ba file khác** đang `import` nó làm thư viện dùng chung (`_v10861:233`, `_v10869:336,554`, `_v10900:110`). **Xoá là gãy ba chỗ.** Chỉ gỡ cron |
| 6 | Bản sửa bộ tự kiểm C6 đầu tiên ghi `status="DAT"` trong khi cả hệ dùng `"OK"`/`"LECH"` và `compute_view` đếm `status == "OK"` | Để nguyên là **C6 bị tính lệch mỗi ngày** — đúng thứ đang muốn tránh |
| 7 | `compute_view()` chỉ **đọc bản đã lưu** chứ không tính lại | Lần kiểm đầu thấy C6 vẫn trả giờ cũ, **suýt kết luận "gỡ cron không ăn"**. Phải gọi thẳng `run_checks()` mới biết |

---

## 5. Kết quả cuối phiên

Kiểm tổng thể **7/7 mục đạt**: 6 cờ ghi đè đúng trạng thái duyệt · 6 lane còn 0 dòng cron (tổng
71) · các job SỐNG còn nguyên · bộ tự kiểm 16 phép lệch 0 · **hash 4 bảng khoá GIỮ NGUYÊN** ·
health 200 · admin 401.
