# CONVERSATION CONTEXT — V11044 · 2026-08-09 09:20 → 10:45

## Owner nói gì (NGUYÊN VĂN)

> **GĐ-1 · 10/08 — FU-384: MỘT NỬA SỔ VÔ HÌNH** (việc nặng nhất — làm đầu ngày với đầu óc tỉnh,
> KHÔNG làm cuối phiên dài)
>
> 1. BACKUP sổ + chạy mọi thay đổi trên BẢN SAO trước (bài học FU-324).
> 2. Sửa regex/loader để thấy đủ 768 tiêu đề; FU-330 xuất hiện lại, FU-185 không còn nuốt thân.
> 3. Gộp 128 khối trùng, GHI TỪ CUỐI NGƯỢC LÊN, đọc lại bằng bộ đọc THẬT.
> 4. Cổng máy §61 cho lỗi "quên ô status": thiếu ⇒ CHẶN. Thử allow/deny.
> 5. ĐÍNH CHÍNH §60 các con số lịch sử.

## Việc đầu tiên là nhìn đồng hồ

GĐ-0 tối nay (18:05, 19:35) còn **8–10 giờ nữa** — chưa quan sát được. Nên làm thứ **kiểm được
ngay**: chứng minh bảng bầy đàn 08/08 đã có (không mất), trace 09/08 có `context_pack_chars=64 =
0` (prompt sạch), rồi chuyển sang FU-384 như owner dặn — việc nặng nhất, làm đầu ngày.

## FU-384 — làm đúng thứ tự, mỗi bước có chứng minh

**Sửa bộ đọc:** điểm cắt thân khối nay là **mọi `##`/`###`** (không riêng `### FU-<số>`), nên
FU-185 hết nuốt 573 KB (còn 1.679 ký tự); nhận FU có tiền tố ngắn (`A1 / FU-330`) nên FU-330 tái
xuất. Trước/sau: 258 → 259 mã, **0 mất, 0 đổi bất thường**.

**Tách lịch sử:** 357 LEGACY + 134 khối cũ → `docs/archive/`, bảo toàn từng byte. Chạy `--thu`
trên bản sao trước, chỉ `--ap-dung` khi bản sao đạt. Sổ chính **1,29 MB → 564 KB**.

## Ba chỗ agent vấp — ghi hết

**1. Suýt mất lịch sử một lần nữa — và đây là chỗ đáng sợ nhất.** File archive rơi vào
`.gitignore` (`archive/`). Commit V11044 xoá 8.736 dòng khỏi FOLLOW_UP, nhưng bản lưu chúng
**không vào git**. Cổng cắt cụt **cho qua** vì tệp ngắn đi không phải tiền tố — **đúng lỗ hổng
08/08 đã mất 4.056 dòng**. Chỉ bắt được vì agent kiểm `git ls-files` sau commit theo phản xạ.
Force-add ở V11044b. **Nếu không kiểm, ai clone kho sẽ mất toàn bộ 7.521 dòng lịch sử.** Đây là
bằng chứng: cổng cắt cụt vẫn **mù với xoá-giữa-tệp**, chỉ bắt được xoá-đuôi.

**2. Vật chất hoá mã đọc lần đầu làm sai.** Thêm ô `**ma_doc**` — nhưng bộ đọc lấy mã đọc từ
**tiêu đề**. Thử archive thấy 10 mã đổi, khôi phục, làm lại đúng (chèn vào tiêu đề). Bài học: khi
vật chất hoá, phải ghi vào **đúng chỗ bộ đọc đọc**, không phải chỗ trông hợp lý.

**3. Đưa nhầm script one-shot vào loạt cổng.** `_v11044_archive_so` là script thi hành một lần;
chạy lại nó trên tệp đã archive thấy FU-384 có 2 khối (bản V11043 + bản V11044 mới prepend) là
**bình thường qua prepend**, không phải hỏng. Đã tách bạch: đó không phải cổng.

## Điều agent nói thẳng với owner

**1. Con số «749 mục» sai từ gốc.** Nó đếm cả 357 khối di sản LEGACY và 134 khối trùng như mục
riêng. Sự thật: **259 mã FU thật**. Mọi con số về sổ theo dõi từ trước tới nay đều tính trên một
nửa tệp — không phải lỗi ai cố ý, mà là bộ đọc mù một nửa.

**2. Cổng cắt cụt vẫn có một lỗ.** Nó bắt được **xoá-đuôi** (tiền tố) nhưng **mù với xoá-giữa**
(archive rải rác). Sự cố 08/08 là xoá-đuôi nên V11040 vá được; nhưng archive hôm nay là xoá-giữa,
cổng cho qua. May là `_doc_prepend` kêu và `git ls-files` bắt. Nên xét bổ sung cổng: mọi commit
làm tệp quản trị ngắn >20% phải có file archive tương ứng trong git — nhưng đó là việc riêng, ghi
lại chứ chưa làm.

**3. GĐ-0 tối nay chưa chạy được** — đồng hồ 09:20, hai mốc cron còn 8–10 giờ. Không bịa kết quả.
