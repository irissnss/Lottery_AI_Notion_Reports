# CONVERSATION CONTEXT — V11011 · 2026-08-07

## Owner nói gì (NGUYÊN VĂN)

> "chạy đi và đo lại đi em sau đó báo cáo chi tiết đầy đủ dùm anh nha em, push báo cáo lên
> github và cập nhật https://claude.ai/code/artifact/916ca12a-33a3-49ad-8464-3ba26960f9f5
> lên V7 dùm a đi em"

Owner duyệt đề nghị ở cuối V11010: chạy `web/_sync_live_forensic_inputs.py` rồi đo lại toàn bộ.

## Agent làm gì

1. **Bấm hash 4 bảng TRƯỚC đồng bộ** để có mốc so.
2. **Chạy đồng bộ** — `sync_completed_at = 2026-08-07T00:31:55`. Mọi bảng lên 06/08.
3. **Chạy lại M4** vì đồng bộ ghi đè cột `giai_doan` và bảng `mined_rule_doi_chung` — đã cảnh
   báo trước ở REPORT_V11010 §8, nên không bất ngờ.
4. **Cài cổng tuổi dữ liệu ngay vào script đo mới** — `do_lai_tuoi.py` mở đầu bằng đọc
   `latest_manifest.json`, thoát nếu cũ hơn 6 giờ. Đây là mẫu cho FU-303.
5. **Đo lại toàn bộ** con số đầu bài trên dữ liệu tươi.
6. **Làm nốt PL19c phần C/D/E** chưa kịp làm ở gói trước.
7. **Commit cả script lẫn output** theo E4 — thư mục `scripts/` kèm báo cáo.

## Kết quả — cái gì đổi, cái gì không

**GIỮ NGUYÊN (4 con số lái quyết định):**

- model hơn nền sau Bonferroni: **0/34** → FU-290 không bị ảnh hưởng
- hội tụ "3 nguồn": z = −2,51 → **−2,54**, vững hơn
- bảng chi phí rỗng 0/4033 · bundle làm bù 90 · bầy đàn 21,7 → 9,2

**ĐỔI RÕ:**

- **đo tiến M4: −1,34σ → −0,33σ** (đổi đài) và **−0,82σ → +0,26σ** (dịch ngày).
  Cách đọc phải sửa: từ *"kém hơn đối chứng"* thành **"ngang bằng, không phân biệt được"**.

**BỐN PHÁT HIỆN MỚI:**

1. **"57/90 bundle thiếu phiếu" KHÔNG tái lập** — thực đo 30 ngày: **1/93 (1%)**.
2. **MB chạy theo V10895** (luôn rerun) 14/14 ngày ⇒ **V10770 phải đánh dấu SUPERSEDED**.
3. **D2 — §23 không giảm bầy đàn.** Tập khoá 7 model chung: 1,66× → 1,84×. Vẫn còn nhiễu
   (model/ngày 4,8 → 6,6) nên **giữ lệnh CẤM viết §24**.
4. **Hơn 40 bảng cũ hơn 14 ngày**, 3 bảng RỖNG. `model_latency_cost_audit_daily` dừng ghi
   **93 ngày** — trước nay chỉ nói "cột chi phí rỗng", thực ra cả bảng đã chết.

## Vấp ở đâu

### Bài học nặng nhất — n nhỏ không chỉ yếu, mà KHÔNG ỔN ĐỊNH

`DO_TIEN` từ **1 ngày** lên **3 ngày** làm z đi từ `−1,34` sang `−0,33`/`+0,26` — **đổi dấu**.
Nghĩa là kết luận trên mẫu nhỏ có thể **lật** chỉ vì thêm chút dữ liệu. Trước nay agent hay
viết "n nhỏ nên yếu"; đúng hơn phải là **"n nhỏ nên chưa được phép kết luận gì"**.

### Kho báo cáo cũ có con số không tái lập được

"57/90 bundle thiếu phiếu" (V10978) đo lại ra **1/93**. Hoặc định nghĩa khác, hoặc đã vá, hoặc
sai từ đầu — chưa biết. Đã mở FU-307 để tìm định nghĩa gốc trước khi kết luận.

### Bằng chứng gián tiếp cho V11010

`QD-027` trôi ở phiên trước với lý do *"bảng khuyến cáo hôm nay rỗng"*. Sau khi đồng bộ, nó
**tự hết trôi** — xác nhận đúng luận điểm V11010: đó là **triệu chứng của bản local cũ**, không
phải lỗi code.

## Điều agent NÓI THẲNG với owner

**Tin tốt lớn nhất:** con số owner sắp ký ngày 08/08 — **0/34 model hơn nền** — **không đổi** sau
khi đo lại trên dữ liệu tươi. FU-290 đứng vững.

**Nhưng một kết luận của agent phải sửa cách đọc.** M4 đo tiến không phải "kém hơn đối chứng" mà
là "ngang bằng". Sự khác biệt quan trọng: *kém hơn* nghĩa là luật có hại; *ngang bằng* nghĩa là
**chưa có bằng chứng nào cả, theo cả hai chiều**.

**Và kho báo cáo cũ cần rà lại.** Nếu "57/90" không tái lập được thì có thể còn con số khác cùng
loại. Đây là việc lớn hơn phạm vi phiên này.
