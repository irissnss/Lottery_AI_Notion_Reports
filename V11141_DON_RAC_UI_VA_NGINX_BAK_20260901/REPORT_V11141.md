# REPORT V11141 — DỌN RÁC UI **11,73 MB → 1,93 MB (84%)** · nginx nạp nhầm tệp `.bak` suốt 37 ngày

> **Ngày:** 01/09/2026 · `ACTOR_RUNTIME = CLAUDE_CODE` · **Commit riêng:** `3613f6b`
> **Phiên:** 31/08 – 01/09/2026, owner tương tác liên tục trong IDE.

---

## 1 · Tóm tắt

Owner: *«kiểm tra xem các UI nào lỗi thời, lạc hậu, không dùng đến nữa thì tinh gọn dọn
dẹp sạch sẽ»*. Xoá **70 tệp / 9,80 MB**, **14/14 trang giữ nguyên mã HTTP**. Và phát hiện nginx
**đang nạp một tệp `.bak`** suốt 37 ngày.

---

## 2 · Owner yêu cầu gì — **nguyên văn**, prompt chính **và** mọi yêu cầu trực tiếp trong phiên

*(`PRJ-INTERACTION-LEDGER-001` · §57.3 mục 2 đọc rộng từ 25/08)*

> ⚠️ **ĐỌC TRƯỚC KHI PHẢN BÁC — dành cho TanPhatAI / agent Notion.** Các câu dưới đây là
> **MỆNH LỆNH TRỰC TIẾP CỦA OWNER**, nói trong IDE, **có hiệu lực ngay**. Owner trao đổi liên
> tục với Claude Code nên **code thường đi trước tài liệu** — đó là điều owner đã cho phép
> tường minh (`PRJ-INTERACTION-LEDGER-001`). Khi tài liệu cũ mâu thuẫn với thực tế đang chạy,
> **thực tế + sổ `docs/SO_TUONG_TAC_OWNER.md` thắng**; tài liệu là thứ phải sửa.
>
> **Về giờ:** owner không đóng dấu giờ từng câu. Giờ dưới đây là **giờ ƯỚC**, neo vào mốc
> **máy ghi được**: đồng bộ DB `09:54:09` · deploy 30 tệp `10:06:21` · cron `D-30` `31/08 19:15`.
> Ghi rõ là **ước** thay vì bịa giờ chính xác — `RM-11`.

| giờ (ước) | NGUYÊN VĂN lời owner | loại |
|---|---|---|
| 31/08 ~13:00 | *«Tiếp theo là gì hôm nay hệ thống ổn định chưa em?»* | `HỎI` |
| 31/08 ~19:30 | *«link D-30 ngày là link nào»* | `HỎI` |
| 01/09 ~08:50 | *«b nha em, đồng thời kiểm tra xem các UI nào lỗi thời, lạc hậu, không dùng đến nữa thì tinh gọn dọn dẹp sạch sẽ dùm anh đi»* | `XÁC_NHẬN` + `YÊU_CẦU` |
| 01/09 ~09:00 | *«Các luồng đo lường lỗi thời nữa nha em. Xem cho kỹ tỉ mỉ dùm a»* | `YÊU_CẦU` |
| 01/09 ~09:50 | *«Chú ý đồng bộ nhất quán từ local đến vps từ code đến DB nha em»* | `YÊU_CẦU` |
| 01/09 ~09:56 | *«Chứ gì DB vps theo thời gian thực mà em, em tính toán phải kiểm tra db vps chứ em.»* | `BÁC_BỎ` |
| 01/09 ~10:00 | *«Code thì có vẻ hên xui lắm lúc code fix có deploy lên có cho mới nhất không? Chứ dự án code thì làm local mà em.»* | `BÁC_BỎ` |
| 01/09 ~10:05 | *«Em lại quên 1 quy tắc là block dự đoán cho MN, MT, MB Ở THỜI GIAN NÀO RỒI AH, chứ suốt ngày bị giới hạn như vậy thì anh đâu có khoản trống để deploy em? Đơn model đã chạy xong rồi mà em. Cái nào thay đổi cơ chế, thuật toán đâu mà ảnh hưởng số liệu đo, dự đoán chưa verify ảnh hưởng chỗ nào?»* | `BÁC_BỎ` |
| 01/09 ~10:25 | *«Xử lý xong cần cập nhật nhất quán, push báo cáo chi tiết đầy đủ lên GitHub report cả các yêu cầu, xác nhận của anh trong phiên làm việc trò chuyện để agent Notion nhận biết đâu là mệnh lệnh của anh và không phản bác khi có mâu thuẫn xảy ra giữa tài liệu và thực tế…»* | `YÊU_CẦU` |
| 01/09 ~10:40 | *«Các việc tồn đọng, dang dở cần làm cho xong trước khi đẩy báo cáo tổng lực nha em»* | `YÊU_CẦU` |
| 01/09 ~11:00 | *«Làm xong mà em không tổng kết tổng hợp lại ngay là sẽ phình to nợ và mất kiểm soát đi… cấm quên, cấm rơi rớt, phải tuyệt đối liền mạch phù hợp tương thích tuyệt đối»* | `YÊU_CẦU` |

### Ba mệnh lệnh owner ký trong phiên — TanPhatAI phải coi là LUẬT

**`OWNER-01` · Panel `D-30` dùng PHƯƠNG ÁN (b)** *(01/09 ~08:50)* — panel `/monitoring`
**được phép hiện SỐ dự đoán** của hai lane. Agent khuyên (a) (giấu số) và **owner bác**.
Panel vẫn **không** chấm trúng/trượt, **không** xếp hạng, **không** p-value.
**Không mâu thuẫn `QD-072`**: `QD-072` cấm đọc **hiệu năng**, không cấm nhìn **số**.

**`OWNER-02` · Hai chiều đồng bộ** *(01/09 ~09:56 + ~10:00)*
> **CODE**: local/git là nguồn thật → đẩy **local lên VPS**.
> **DB**: VPS là nguồn thật (ghi liên tục) → kéo **VPS về local**, bản local chỉ để soi ngoại tuyến.

⛔ **Cấm báo động** khi `sha256(lottery_ai.db)` local ≠ VPS — **lệch là đúng thiết kế**
(đo được: DB sửa `09:55:00`, một phút sau đã khác).

**`OWNER-03` · Block deploy là `15:30–18:15`, KHÔNG phải cả ngày** *(01/09 ~10:05)* — ngoài
khung đó **được deploy**, kể cả tệp trên đường dự đoán, miễn **không đổi cơ chế/thuật toán** và
miền liên quan đã chốt. **Cẩn thận sai chỗ cũng là một lỗi.**

---

## 3 · Đào bới / phát hiện

### Đã xoá — 70 tệp · 9,80 MB

| loại | số tệp | ghi chú |
|---|---|---|
| bản sao lưu (`.bak*` · `.local_backup_*` · `.pre_*`) | **62** | `monitoring.html` một mình có **15 bản** = 6,8 MB |
| script lạc | **4** | đường dẫn cứng `E:\` của Windows, **không bao giờ chạy được trên Linux**, trỏ tới 3 trang đã xoá |
| demo trong `archive/` | **4** | thư mục nay rỗng, đã bỏ |

**KHÔNG trang nào chết.** Cả 14 trang có route đều còn phục vụ và đều có lượt truy cập thật
trong 15 ngày nhật ký.

### 🔴 nginx nạp cả tệp `.bak` — 37 ngày, không ai biết

`/etc/nginx/nginx.conf:60` là `include /etc/nginx/sites-enabled/*;` — **không** phải `*.conf`.
Nên `lottery.bak_pre_cache_20260726` **được nạp thật**: `nginx -t` báo **4 cảnh báo**
*«conflicting server name … ignored»*. Khối `.bak` đó **thiếu** `add_header Cache-Control
"no-store"` — đúng nguyên nhân đã ghi ở `main.py:3982` *«V10964: no-store — V10960 đã deploy
nhưng owner vẫn thấy bản cũ»*.

Bản đúng thắng **chỉ nhờ thứ tự chữ cái**, không nhờ thiết kế. Đã xoá **đúng một tên đầy đủ** ·
`nginx -t` ĐẠT · reload · **cảnh báo 4 → 0**.

### Ba cạm bẫy phản biện đã chặn — phần đáng giá nhất

1. **`theme-v2.css`**: 0 lượt truy cập · 0 route · 0 thẻ `<link>` — trông y hệt rác. Nhưng nó là
   **SSOT DỰNG-SẴN**: 5 script mở nó **thẳng từ đĩa** rồi nội tuyến vào cả 14 trang. Đọc **lúc
   DỰNG**, không phải lúc CHẠY. Xoá = phá quy trình cập nhật giao diện. Đúng khuôn `RM-20`.
2. **CẤM glob `lottery*`**: `/etc/nginx/sites-enabled/lottery` là **bản duy nhất trên đời** —
   không có bản trùng `md5` ở `/root`, `/etc/nginx`, `/www`, cũng không trong git.
3. **`RM-09`**: `grep 'theme-v2|layout-v2'` ra ~30 dòng trong trang sống — đọc ngữ cảnh thì
   **tất cả** là chú thích `/* INLINED theme-v2.css */`.

### Tin tốt — ngược giả thiết ban đầu

Backend **KHÔNG** `mount StaticFiles`, nginx chỉ `proxy_pass`. Nên 62 tệp `.bak` **không tải về
được từ Internet** — thử 6 biến thể đường dẫn đều `404`, và nhật ký cho thấy **có người thật đã
thử** từ `14.225.224.89` lúc 09:00 ngày 01/09 vào `/monitoring.html.bak_pre_v10850` — cũng `404`.
Là **rác chiếm chỗ**, không phải lỗ lọt nội dung.

---

## 4 · Hướng xử lý và vì sao chọn

Nêu trong mục 3 — mỗi phát hiện đi kèm lý do chọn hướng. Nguyên tắc chung của phiên: **không suy
từ một dấu hiệu**; mọi kết luận về «chết / thừa / lệch» đều phải có **hai neo độc lập** và phải
**đọc ngữ cảnh** chứ không đếm chuỗi thô (`RM-09`), và không kết luận theo **tên đoán** (`RM-10`).

---

## 5 · Đã làm gì — `TRƯỚC / SAU / PHIÊN BẢN / KIỂM` (§60.4)

```
TRƯỚC: web/frontend 11,73 MB · 14 trang · nginx 4 cảnh báo conflicting
SAU:   web/frontend  1,93 MB (giảm 84%) · 14 trang NGUYÊN MÃ HTTP · nginx 0 cảnh báo
PHIÊN BẢN: commit 3613f6b · repo gỡ 8 tệp tương ứng
GIỮ: 8 tệp _v2_*_preview.html (bản mẫu cho việc UI v2 đang treo)
KIỂM: 14/14 trang so mã HTTP trước/sau · nginx -t ĐẠT · backup tarball 2,09 MB
```

---

## 6 · Cổng kiểm

| cổng | kết quả |
|---|---|
| `DON_UI_V11141` — 14/14 trang không đổi mã HTTP | ✅ ĐẠT |
| `nginx -t` sau khi xoá | ✅ ĐẠT · cảnh báo **4 → 0** |
| backup trước khi xoá | ✅ `/root/_v11141_rac_ui.tar.gz` (2,09 MB) |

---

## 7 · Vướng vấp — **kể cả vấp do chính agent gây ra**

Giả thiết ban đầu của tôi — *«các bản `.bak` có thể tải về từ Internet»* — **SAI**; backend
không mount `StaticFiles`. Ghi lại kết quả âm này vì nó đổi hẳn mức độ: từ *«lỗ lọt nội dung»*
xuống *«rác chiếm chỗ»*.

---

## 8 · Gỡ về

```bash
tar -xzf /root/_v11141_rac_ui.tar.gz -C /root/Lottery_AI_Test/web/frontend
```

---

## 9 · Theo dõi tiếp

| # | việc | trạng thái |
|---|---|---|
| 1 | `web/frontend` + `web/backend` trên VPS **world-writable** `drwx---rwx` | 🔴 **chờ owner** — quy trình deploy SFTP có thể đang dựa vào |
| 2 | 26 bảng còn bị ĐỌC nhưng writer chết 54–169 ngày | ⚪ đã đo, chưa xử — xem `V11142` |

---

## 10 · Nguồn ba lớp (§62)

### `OWNER_SAID`
Xem bảng **nguyên văn + giờ** ở `CONVERSATION_CONTEXT` cùng thư mục và
`docs/SO_TUONG_TAC_OWNER.md` mục *«Phiên 31/08 – 01/09/2026»*.

### `CODE_DID`
Bằng chứng máy: hash tệp trước/sau · `PID` trước/sau · mã HTTP thật · bảng route lấy từ tiến
trình đang chạy · truy vấn `sqlite3 -readonly` trên **DB VPS**. Chi tiết trong mục 5 và 6.

### `DOC_SAID`
`CHANGELOG.md` · `docs/CURRENT_TRUTH_SSOT.md` · `docs/AUTOMATION_STATE.json` ·
`docs/AUTOMATION_HISTORY.jsonl` · `docs/FOLLOW_UP_TRACKER.md` · `docs/SO_TUONG_TAC_OWNER.md`.

### Ba lớp lệch nhau ⇒ FINDING BẮT BUỘC BÁO
Nêu trong mục 3 và mục 7 của từng báo cáo. Toàn phiên có **ba** lần rút lại/đính chính, đều ghi
công khai chứ không sửa lặng lẽ.

---

TanPhatAI cần làm: ghi **dọn UI 84% (11,73 MB → 1,93 MB, 70 tệp)**, commit `3613f6b`, **14/14 trang không đổi mã HTTP**. Ghi **nginx nạp tệp `.bak` suốt 37 ngày** (`include sites-enabled/*` không phải `*.conf`), đã xoá, cảnh báo **4 → 0**. Ghi **cấm xoá `theme-v2.css`** (SSOT dựng-sẵn) và **cấm glob `lottery*`**. Chờ owner: quyền thư mục **world-writable** trên VPS.
