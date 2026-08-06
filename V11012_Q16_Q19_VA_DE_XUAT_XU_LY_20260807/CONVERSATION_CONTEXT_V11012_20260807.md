# CONVERSATION CONTEXT — V11012 · 2026-08-07

## Owner nói gì (NGUYÊN VĂN)

> "Làm tiếp đi chứ chờ đợi gì nữa rồi tổng hợp báo cáo lên github đề xuất xử lý tiếp dùm anh
> luôn em"

Ở cuối V11011 agent tự khai còn thiếu Q16 và Q19 của gói PL19c. Owner bảo làm nốt và kèm đề
xuất xử lý.

## Agent làm gì

1. **Q16** — tra `CHANGELOG` tìm nguyên văn V10857, xác định đúng hai cửa sổ nó dùng
   (08–17/07 vs 18–25/07), rồi **đo lại bằng thước mới**: kèm nền theo ngày · kèm đối chứng bốc
   bừa · và **mở rộng cửa sổ sau tới hôm nay**.
2. **Q19** — đối chiếu `du_doan_test_bundles.test_bt` với `du_doan_test_results.test_bt` theo
   `run_id` để xem còn ca "công bố một đằng chấm một nẻo" không; rồi kiểm **giờ lane chạy** so
   với **giờ official chốt**.
3. Cả hai script đều **mở đầu bằng cổng tuổi dữ liệu** — bài học từ V11010.
4. Viết đề xuất xử lý theo thứ tự, mỗi đề xuất kèm rủi ro và cách gỡ về.

## Kết quả

### Q16 — kết luận thắng của RULES-FIRST sụp đổ

Số học của V10857 **tái lập chính xác** (6/30 = 20,0% · 10/24 = 41,7%). Nhưng:

- Cửa sổ **"trước" nằm DƯỚI nền 14 điểm** (20,0% vs nền 34,1%, z=−1,63)
- Cửa sổ "sau" chỉ trên nền 7 điểm, **z=+0,74** — không có ý nghĩa
- **Mở rộng cửa sổ sau tới 06/08: 33,3% vs nền 33,8%, z=−0,08** — đúng nền, hiệu ứng biến mất
- So hai cửa sổ trực tiếp: **z=+1,73**, không đạt cả ngưỡng lỏng 1,96
- Sức mạnh: cần **n≈82** mỗi cửa sổ; V10857 có **30 và 24**

⇒ "Gấp đôi" là **bật lên từ một hố xui**, không phải tiến bộ.

### Q19 — vá gốc giữ được, nhưng lỗi thứ hai vẫn sống

- **Lỗi 3 (công bố ≠ chấm): HẾT** — 2.112 cặp/30 ngày, **lệch 0**
- **Lỗi 2 (kho model chưa đủ): CÒN, riêng MB** — lane chạy **17:38**, official còn về tới
  **17:58**, lane chỉ thấy **18–21/27 model**, **6 ngày liên tiếp**
- MN (05:21) và MT (16:44) đều khớp 27/27

## Vấp ở đâu

### Mẫu lỗi có hệ thống trong cách đo "trước vs sau"

Q16 phơi ra công thức tạo kết quả đẹp mà không cần gian lận: cửa sổ ngắn + không có nền +
không đăng ký trước + cửa sổ sau kết thúc đúng ngày báo cáo. Bốn thứ cộng lại thì gần như
chắc chắn ra số đẹp — vì cửa sổ trước (dù vô tình) rơi vào lúc đang xui.

Đây là **lần thứ bảy** trong chuỗi `V10655 → V10672 → V10677 → V10753 → V10789 → V10790`.
Sáu lần trước dự án đã kết luận *"đừng bật lại bằng backtest, chỉ bằng đo tiến"* — nhưng
V10857 vẫn dùng backtest cửa sổ ngắn để **GIỮ** một cơ chế đang chạy.

### Vá một lỗi không có nghĩa là vá cả họ

V10884 nêu ba lỗi. Lỗi 3 vá xong và giữ được suốt 30 ngày. Nhưng lỗi 2 vẫn sống ở MB **6 ngày
liên tiếp** mà không cổng nào kêu — vì cổng chỉ kiểm "có chạy không", không kiểm "chạy với đủ
nguyên liệu chưa".

## Điều agent NÓI THẲNG với owner

**Q16 là bằng chứng mạnh nhất từ trước tới nay cho FU-291.** Ba nguồn nay chụm vào một chỗ:
căn cứ giữ RULES-FIRST sụp (Q16) · đo tiến ≈ đối chứng (M4) · §5g thưởng ô tệ nhất (Q9).

**Đề xuất gộp FU-291 và FU-298 làm MỘT biến** — chúng cùng một họ *"prompt tự cộng điểm cho tín
hiệu chưa chứng minh"*. Tách ra hai lần deploy tốn thêm 14 ngày đo mà không tách được nhân quả.

**MB lane sớm 20 phút là việc sửa được ngay** — chỉ đổi giờ cron của lane test, không đụng
`/du-doan` official, rủi ro rất thấp.

**Và cần một cổng mới (FU-313):** mọi kết luận "trước vs sau" phải kèm nền cho **cả hai** cửa sổ,
tính sức mạnh, và đăng ký trước ngày chốt. Thiếu một thứ ⇒ không được ghi là "thắng". Nếu có
cổng này từ 26/07 thì V10857 đã không qua được.
