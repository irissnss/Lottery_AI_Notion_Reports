# CONVERSATION CONTEXT — V11010 · 2026-08-07

## Owner nói gì (NGUYÊN VĂN)

Sau khi agent báo phát hiện bản local cũ trong gói PL19c:

> "thế trước đo PL 19a và PL19b thì sao em? có đo trên nền dữ liệu củ không và các vấn đề trước
> đó nữa có đo trên dữ liệu của không em? em làm việc kiểu gì mà chả tư duy gì cả vây nhỉ? hãy
> xem lại dùm a toàn bộ đi nào. Sua đó cập nhật báo cáo chi tiết đầy đủ len github dùm a nha"

## Agent làm gì

1. **Soi lịch sử đồng bộ** `artifacts/live_sync/` — 553 lần từ 20/04, nhưng tháng 8 chỉ có 7 lần,
   **lần cuối 05/08 12:11**, và **06/08 không lần nào**.
2. **Đối chiếu mốc commit với mốc đồng bộ** → xác định **17 bản** V10991→V11009 đo trên dữ liệu
   cũ 9–35 giờ.
3. **Không đoán xem con số nào sai** — viết script chạy **thẳng trên VPS** (read-only) đo lại
   từng con số đầu bài.
4. Phân loại kết quả: **6 giữ nguyên · 2 sai · 1 cần làm rõ phạm vi**.
5. Chạy lại kiểm chứng độc lập B1·B2·B3·B4 → **11/11 khớp**, chứng minh sai lệch đến từ **độ cũ
   dữ liệu**, không từ thuật toán.

## Vấp ở đâu

### Vấp gốc — bỏ một bước có ghi rõ trong CLAUDE.md, 17 lần liên tiếp

CLAUDE.md, mục "Toàn vẹn dữ liệu sống", có đúng hai câu:

> *"Trước mọi việc accuracy / audit / forensic dùng bản local: chạy
> `python web/_sync_live_forensic_inputs.py`."*
> *"Trích dẫn `artifacts/live_sync/latest_manifest.json` khi dùng bản local làm bằng chứng."*

Agent **không làm cả hai**, từ V10991 (05/08 21:36) tới V11009 (06/08 23:30).

### Vì sao lỗi này sống lâu đến thế

Dữ liệu cũ **không gây lỗi**. Script chạy trơn, số ra đẹp, mọi cổng kiểm đều đạt. Không có
triệu chứng nào để nghi ngờ. Chỉ khi owner đối chiếu một con số cụ thể (bảng A/B "đứt") thì
mới lộ.

### Bài học nặng nhất — hiểu sai phép kiểm của chính mình

Agent tự hào suốt hai gói về `hash 4 bảng khoá PRE=POST`. Nhưng phép đó **chỉ chứng minh không
ghi bậy vào dữ liệu**, **không** chứng minh **dữ liệu đúng thời điểm**. Hai chuyện hoàn toàn
khác nhau. Agent đã lấy phép kiểm A để yên tâm về chuyện B.

### Vấp phụ — B4 dùng danh sách tệp ĐOÁN

PL19b kết luận "rules vào ML = 0" dựa trên 4 tệp, và evidence ghi `ml_train.py`,
`meta_train.py` "không đọc được". Kiểm lại: **hai tệp đó không tồn tại**. Agent đoán tên tệp
train thay vì tìm tệp train thật.

Kết luận vẫn đúng (8/8 module train thật đều = 0), nhưng **cách đi tới kết luận thì sai**.

## Con số đã soi lại — cái nào đổi

| con số | local (đã công bố) | VPS (thật) | |
|---|---|---|---|
| model hơn nền sau Bonferroni | 0/34 | **0/34** | GIỮ |
| bầy đàn MN | 21,6 → 9,2 | 21,7 → 9,2 | GIỮ |
| số đài đang sống | 41 | **41**, 0 đài lạ | GIỮ |
| bundle làm bù | 90 | **90** | GIỮ |
| bảng chi phí rỗng | 0/4033 | **0/4033** | GIỮ |
| hội tụ "3 nguồn" | z=−2,51 | z=**−2,54** | GIỮ, vững hơn |
| **`DO_TIEN`** | 15 dòng/1 ngày | **45 dòng/3 ngày** | **SAI, gấp 3** |
| **bảng A/B** | *"ĐỨT 05–06/08"* | **KHÔNG đứt**, 23/28 ngày | **SAI HẲN** |
| shadow `output_eligible=0` | 512 | 8.890 (toàn thời gian) | khác phạm vi đếm |

## Điều agent NÓI THẲNG với owner

**Owner hỏi đúng chỗ agent đáng lẽ phải tự hỏi.** Khi phát hiện bản local cũ trong PL19c, phản
xạ đúng phải là *"vậy còn những gì tôi đã đo trước đó?"* — agent không tự đặt câu hỏi đó, owner
phải hỏi.

**Tin tốt là phần lớn kết luận đứng vững:** 6/9 con số đầu bài không đổi, kể cả con số quan
trọng nhất đang chờ owner ký ngày 08/08 — **0/34 model hơn nền**, VPS xác nhận y hệt. **FU-290
không bị ảnh hưởng.**

**Hai chỗ phải sửa:** FU-297 dựng trên tiền đề sai (bảng A/B chưa bao giờ đứt) ⇒ **giữ mốc chốt
samday MT 12/08**, không dời 17/08. Và `DO_TIEN` gấp 3 con số đã báo — nhưng hạn FU-286 (24/12)
**không đổi** vì ước tính dựa trên nhịp 1 lượt/tuần/luật, không dựa trên số dòng.

**Đề xuất cổng chặn thay vì nhắc nhở.** Lỗi lặp 17 lần nghĩa là nhắc không đủ. FU-303: script
đo phải tự đọc `latest_manifest.json`, thấy dữ liệu cũ hơn 6 giờ thì **từ chối chạy**.
