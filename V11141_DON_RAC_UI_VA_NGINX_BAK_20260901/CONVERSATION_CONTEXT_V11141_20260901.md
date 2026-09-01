# CONVERSATION CONTEXT — V11141 · 01/09/2026

> Nguyên văn lời owner · agent làm gì · vấp ở đâu (§57.2). Giờ **Việt Nam (UTC+07:00)**.
> `ACTOR_RUNTIME = CLAUDE_CODE`.

---

## 1 · Owner nói gì — NGUYÊN VĂN

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

## 2 · Vì sao bảng trên quan trọng với TanPhatAI

Owner làm việc với Claude Code **theo dòng liên tục trong IDE**: hỏi, chốt, đổi hướng, xác nhận —
tất cả bằng lời, ngay trong phiên. Tốc độ đó là **cố ý và được owner cho phép**
(`PRJ-INTERACTION-LEDGER-001`). Hệ quả: **code thường đi trước tài liệu**.

Nếu agent đọc sau chỉ nhìn tài liệu cũ, sẽ thấy mâu thuẫn với thực tế đang chạy và **phản bác** —
và phản bác đó **tốn thời gian của owner để giải thích lại một việc đã nói rồi**. Bảng trên là
để **không phải đoán**: mọi câu đều là mệnh lệnh trực tiếp, có hiệu lực ngay.

---

## 3 · Code đã đi trước tài liệu ở đâu — phiên này

| việc | code chạy từ | tài liệu bù |
|---|---|---|
| `V11136` vá `scheduler.py` (máy trạng thái token) | VPS **29/08 00:40** | repo **31/08** (`V11139`, `bf993e8`) |
| `P43` vá `combo_super.py` (lọc shadow khỏi dự tuyển Combo) | VPS **27/08 22:52** | repo **31/08** (`V11139`) |
| 17 module `C1–C6` (108 phép thử ĐẠT) | local | git **01/09** (`V11142`, `aeacdf9`) |
| Panel `D-30` + API `/api/admin/d30-lane` | VPS **01/09 09:03** | `V11140` (`2897999`) |
| Dọn 70 tệp UI + nginx `.bak` | VPS **01/09 09:30–10:00** | `V11141` (`3613f6b`) |
| Deploy 30 tệp local → VPS | VPS **01/09 10:06** | `V11142` (`aeacdf9`) |

---

## 4 · Vấp trong phiên — kể cả vấp do chính agent gây ra

Giả thiết ban đầu của tôi — *«các bản `.bak` có thể tải về từ Internet»* — **SAI**; backend
không mount `StaticFiles`. Ghi lại kết quả âm này vì nó đổi hẳn mức độ: từ *«lỗ lọt nội dung»*
xuống *«rác chiếm chỗ»*.

---

## 5 · Trạng thái cuối phiên

| | |
|---|---|
| `D-30` | 🟢 ngày chấm **số 1 = 31/08** · cron 19:15 chạy thật · panel `/monitoring` đã có |
| đồng bộ code | 🟢 **0 tệp VPS mới hơn** · 30/30 đã deploy · cổng `_v11143` `RM-15` 4/4 |
| đồng bộ DB | 🟢 theo cặp · `integrity_check=ok` · **lệch hash là đúng thiết kế** |
| UI | 🟢 **84%** rác đã dọn · 14/14 trang nguyên mã HTTP · nginx cảnh báo 4 → 0 |
| chờ owner | 🔴 `FU-446` · `FU-445` · `CAP5` prompt · quyền thư mục world-writable |

---

TanPhatAI cần làm: ghi **dọn UI 84% (11,73 MB → 1,93 MB, 70 tệp)**, commit `3613f6b`, **14/14 trang không đổi mã HTTP**. Ghi **nginx nạp tệp `.bak` suốt 37 ngày** (`include sites-enabled/*` không phải `*.conf`), đã xoá, cảnh báo **4 → 0**. Ghi **cấm xoá `theme-v2.css`** (SSOT dựng-sẵn) và **cấm glob `lottery*`**. Chờ owner: quyền thư mục **world-writable** trên VPS.
