# CONVERSATION CONTEXT — V11017 · 2026-08-07

## Owner nói gì (NGUYÊN VĂN)

> Giờ đề xuất tiếp theo là gì em

Rồi sau khi agent trình ba nhóm việc:

> ok tiếp đi em.

Agent đã trình: *"em dựng phép đo bầy đàn tối nay và bắt đầu M-A — cả hai không cần anh duyệt.
Anh chỉ cần trả lời FU-215 trước sáng mai."*

Việc gốc, owner nêu 07/08:

> *"đừng output theo số gò như thế dẫn đến bầy đàn là đúng rồi, lùa vào 1 bộ số định sẵn trong
> ngày để model quyết định xong thấy bầy đàn."*

Ràng buộc owner đặt từ 06/08 (`FU-287`):

> *"1 tháng mới biết rồi fix rồi đợi 1 tháng nữa thì quá tệ."*

## Agent làm gì

1. **Tra sổ thật trước khi đề xuất**, không nói theo trí nhớ — đọc `treo_items` ra 8 mục quá hạn,
   11 mục đáo hạn 08/08 trong đó 4 mục chờ owner.
2. Đo nền bầy đàn — và phát hiện phải **lọc đường official**, vì gộp shadow vào thì số model
   nhảy từ 16 lên 27 và tỉ lệ méo hẳn.
3. Dựng đủ chuỗi §52: bảng shadow · API admin · panel · cron · tài liệu · `governance_seq`.
4. Deploy, **rồi đọc lại dữ liệu thật** — và bắt được lỗi nhiễm bẩn.
5. Sửa mốc, deploy lại, kiểm lại.

## Nền đo được — 64 lượt miền-ngày

**Trung bình phân tán 0,474 ± 0,087** (17/07 → 07/08). Ca nặng nhất:

| ngày | miền | model | số khác nhau | phân tán | số đông nhất |
|---|---|---|---|---|---|
| 02/08 | MB | 16 | 5 | **0,31** | 73 × 6 |
| 30/07 | MN | 15 | 5 | **0,33** | 86 × **7 model** |
| 05/08 | MT | 16 | 7 | 0,44 | 93 × **8 model** |

**16 model ra 5 số**, có hôm **8/16 model chốt đúng một số**.

## Vấp ở đâu — suýt tạo ra một phép đo TỰ KHEN

Bản đầu lấy mốc theo **NGÀY**. Deploy xong đọc lại:

| ngày | miền | nhãn | phân tán |
|---|---|---|---|
| 07/08 | MB | `SAU_V11016` | **0,5714** |
| 07/08 | MN | `SAU_V11016` | **0,5625** |
| 07/08 | MT | `SAU_V11016` | **0,5714** |

So nền 0,474 thì đây là **thắng lớn, vượt cả ngưỡng 0,50**. Nhưng:

```
predictions 07/08 tạo lúc     : 05:00:05 → 05:20:44
gpt_analyzer.py đổi trên VPS  : 13:35:48
```

**Ba lượt đó chạy prompt CŨ.** Sáng mai đọc bảng là báo cáo nhầm *"lời kể có tác dụng"* — trên
chính dữ liệu của bản cũ.

**Sửa:** mốc thành **MỐC GIỜ** `13:36:00`, phân loại theo `created_at` từng bản ghi. Lượt có cả
trước lẫn sau ⇒ `HON_HOP`, **loại khỏi cả hai trung bình**. Không đọc được giờ ⇒ xếp về **NỀN** —
thà xếp nhầm về nền còn hơn tự khen.

Sau khi sửa: nền `n=63 → 64` · `sau n=1 → 0` · kết luận `CHUA_DU_3_NGAY → CHUA_DU_DU_LIEU`.

## Một lỗi thứ hai, lộ ra vì phải deploy hai lần

Script deploy dùng `cp` để sao lưu. Chạy lần hai là **ghi đè bản "pre" bằng bản đã deploy** —
mất luôn đường gỡ về. Đổi sang **`cp -n`**.

Lỗi này chỉ lộ vì phải deploy hai lần trong cùng phiên. Nếu deploy trót lọt ngay lần đầu thì nó
sẽ nằm im đến lần sau — và lần sau có thể là lúc cần gỡ về gấp.

## Điều agent NÓI THẲNG với owner

**1. Cái cứu không phải là cẩn thận.** Agent viết mốc theo NGÀY một cách rất tự nhiên và không
thấy gì sai. Cái bắt được lỗi là **đọc lại dữ liệu thật ngay sau khi deploy**, thay vì tin vào
thứ mình vừa viết.

**2. Đáng lo hơn cái lỗi:** một phép đo dựng ra để chống tự huyễn hoặc lại suýt trở thành công
cụ tự huyễn hoặc — và nó sẽ tự huyễn hoặc theo hướng **có lợi cho việc agent vừa làm**.

**3. Ngưỡng đã chốt TRƯỚC khi có dữ liệu** và viết thẳng vào mã nguồn lẫn panel, để sau này
không ai — kể cả agent — bẻ ngưỡng cho vừa kết quả.

**4. Lượt đo sạch đầu tiên là 08/08**, không phải 07/08. Nếu tối nay ba miền có thêm bản ghi thì
07/08 thành `HON_HOP` và **bị loại** — đúng thiết kế, không phải hỏng.

**5. FU-326 rộng hơn vẻ ngoài:** bất kỳ phép đo trước/sau nào của một thay đổi **deploy giữa
ngày** đều dính đúng lỗi này. Phải rà, và phép đo nào dính thì **kết luận của nó không dùng
được**.
