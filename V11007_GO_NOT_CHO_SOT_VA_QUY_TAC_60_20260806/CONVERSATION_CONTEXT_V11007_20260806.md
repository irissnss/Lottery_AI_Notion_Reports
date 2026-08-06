# CONVERSATION CONTEXT — V11007 · 2026-08-06

## Owner nói gì (NGUYÊN VĂN)

> V5 sao anh thấy chưa có trạng thái trước và sau sửa ah , hoàn thành hay chưa ah em, nhìn hình
> gây hiểu nhầm liền sữa rồi thì hoàn thành ở lần ở version nào trong code luôn rõ ràng chứ em,
> anh biết em có tư duy suy nghĩ, phải đảm bảo logic tương quan , tương thích, phù hợp nha em,
> nghĩa là đụng tới chỗ nào các vấn đề nào liên quan là cần phải soi xét mới xử lý chứ đừng để
> xử lý chỗ này làm lỗi chỗ khác điều này cần ghi vào quy tắc làm việc claude.md đó nha cấm cẩu
> thả thiếu suy xét trước sau nha em

Kèm ảnh chụp mục 03 của trang phân tích, khoanh đỏ hai dòng G1 và G2.

## Agent làm gì, theo thứ tự

1. **Không ghi "xong" theo trí nhớ.** Đọc thẳng code kiểm từng mục G1–G5.
2. Vòng grep đầu **báo động giả** — thấy `GAN ĐÀI`, `SỐ SẮP ĐẾN CHU KỲ` vẫn còn nên suýt kết
   luận "G2/G5 chưa làm". Đọc ngữ cảnh mới thấy chúng nằm trong **dòng chú thích**.
3. Viết bộ quét **có phân loại** (`TRONG_PROMPT` / `GHI_VÀO_PROMPT` / `CODE` / `CHU_THICH`) rồi
   quét toàn tệp → ra **10 chỗ sót thật**.
4. Sửa 11 chỗ, nâng ba phiên bản prompt.
5. Ký **§60 (A58)** vào bốn mặt quy tắc, sinh lại `AGENTS.md`, kiểm sáu mặt đồng bộ.
6. Deploy có cổng quét ngược riêng — **lần đẩy đầu bị chặn**, sửa rồi đẩy lại.
7. Sửa mục 03 của trang: thêm **TRẠNG THÁI + TRƯỚC/SAU + LÀM Ở BẢN NÀO + LỆNH KIỂM**.

## Vấp ở đâu

### Vấp 1 — suýt báo nhầm vì đếm chuỗi thô

`grep 'GAN ĐÀI'` ra kết quả ⇒ tưởng chưa gỡ. Thật ra là dòng chú thích
`# C. (V11001 — GỠ) khối "⏳ GAN ĐÀI HÔM NAY"`. **Đếm chuỗi mà không đọc ngữ cảnh là sai** —
điều này thành `§60.3`.

### Vấp 2 — cổng của chính V11001 vỡ vì nâng phiên bản

`_v11001_kiem_prompt.py` so **CỨNG** chuỗi `'SP-4.2'`. Nâng lên `SP-4.3` làm cổng **TRƯỢT** dù
prompt sạch hơn hẳn. Đúng kiểu owner vừa cảnh báo: *"xử lý chỗ này làm lỗi chỗ khác"* —
**bắt được ngay trong phiên ký quy tắc cấm chuyện đó**.

Sửa: so **SÀN** thay vì so **BẰNG**.

### Vấp 3 — cổng deploy chặn vì tên biến

Cổng quét ngược trên VPS khớp trúng `hot_str` — **tên biến**, không phải chữ trong prompt.
Dương tính giả. Nhưng thay vì nới cổng, **đổi tên biến** thành `trung_nhieu_str`: giữ cổng chặt,
bỏ chỗ mập mờ.

## Điều agent NÓI THẲNG với owner

**Owner đúng cả hai điểm.** Trang viết ở thì đề xuất cho việc đã làm — gây hiểu nhầm thật. Và
khi đi kiểm thì lòi ra việc **thực sự làm nửa chừng**, nặng hơn lỗi trình bày.

**Chỗ nguy hiểm nhất là dòng 2966:** model được bảo *"Sử dụng dữ liệu Deep Focus (…, Gan đài)"*
trong khi khối `⏳ GAN ĐÀI HÔM NAY` **đã bị chính V11001 xoá**. Model được lệnh dùng một thứ
không tồn tại.

**FU-284 phải đếm lại.** Ngày đo đầu tiên chạy trên bản nửa vời nên kết luận vô giá trị. Đây
không phải biến thứ hai theo QD-018 mà là **làm nốt biến thứ nhất**.
