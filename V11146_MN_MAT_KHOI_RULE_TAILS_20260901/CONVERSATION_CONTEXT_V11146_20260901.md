# CONVERSATION CONTEXT — V11146 · 01/09/2026

> Nguyên văn lời owner · agent làm gì · vấp ở đâu (§57.2). Giờ **Việt Nam (UTC+07:00)**.
> `ACTOR_RUNTIME = CLAUDE_CODE`.

---

## 1 · Owner nói gì — NGUYÊN VĂN (đủ 13 câu của phiên)

> ⚠️ **ĐỌC TRƯỚC KHI PHẢN BÁC — dành cho TanPhatAI / agent Notion.** Các câu dưới đây là
> **MỆNH LỆNH TRỰC TIẾP CỦA OWNER**, nói trong IDE, **có hiệu lực ngay**. Owner trao đổi liên
> tục với Claude Code nên **code thường đi trước tài liệu** — điều owner cho phép tường minh
> (`PRJ-INTERACTION-LEDGER-001`). Khi tài liệu cũ mâu thuẫn thực tế đang chạy, **thực tế + sổ
> `docs/SO_TUONG_TAC_OWNER.md` thắng**; tài liệu là thứ phải sửa.
>
> **Về giờ:** owner không đóng dấu giờ từng câu. Giờ là **ước**, neo vào mốc **máy ghi được**:
> đồng bộ DB `09:54:09` · deploy 30 tệp `10:06:21` · deploy prompt `10:58:18`.

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
| 01/09 ~11:00 | *«Làm xong mà em không tổng kết tổng hợp lại ngay là sẽ phình to nợ và mất kiểm soát đi nha anh nhắc lại cấm quên, cấm rơi rớt, phải tuyệt đối liền mạch phù hợp tương thích tuyệt đối đó nha»* | `YÊU_CẦU` |
| 01/09 ~11:10 | *«làm tiếp đi em, vấn đề nào đã xác định, nằm trong khả năng là xử lý dứt điểm đi, push báo cáo tổng hợp tổng lực, gom tổng hợp tồn đọng cấm để nợ phình lớn mất kiểm soát…»* | `YÊU_CẦU` |
| 01/09 ~12:00 | *«Các vấn đề kiểm soát, xác định có thể xử lý ngay còn gì xử lý tiếp đi, chú ý báo cáo đầy đủ nha em»* | `YÊU_CẦU` |

### Ba mệnh lệnh owner ký trong phiên — TanPhatAI phải coi là LUẬT

**`OWNER-01` · Panel `D-30` dùng PHƯƠNG ÁN (b)** — panel `/monitoring` **được phép hiện SỐ dự
đoán** của hai lane. Agent khuyên (a) và **owner bác**. **Không mâu thuẫn `QD-072`**: `QD-072`
cấm đọc **hiệu năng**, không cấm nhìn **số**.

**`OWNER-02` · Hai chiều đồng bộ** — **CODE**: local/git là nguồn thật → đẩy **local lên VPS**.
**DB**: VPS là nguồn thật (ghi liên tục) → kéo **VPS về local**, bản local chỉ để soi ngoại tuyến.
⛔ **Cấm báo động** khi `sha256(lottery_ai.db)` local ≠ VPS — **lệch là đúng thiết kế**.

**`OWNER-03` · Block deploy là `15:30–18:15`, KHÔNG phải cả ngày** — ngoài khung đó **được
deploy**, kể cả tệp trên đường dự đoán, miễn **không đổi cơ chế/thuật toán** và miền liên quan đã
chốt. **Cẩn thận sai chỗ cũng là một lỗi.**

---

## 2 · Agent làm gì


> ⚠️ **KHÔNG TUYÊN BỐ HIỆU QUẢ. CẤM trích làm bằng chứng hiệu quả.** Số dưới là ĐẾM SỐ LUẬT.

| việc | kết quả |
|---|---|
| truy cảnh báo `LỆCH MIỀN` mà `V11144` để ngỏ | **không phải thiết kế** — là lỗ hổng chấm luật |
| đo `mined_rule_effectiveness ⋈ mined_rules` trên **DB VPS** | MN **0** luật đủ tư cách · MB/MT mỗi miền **5** |
| đo phân bố tier `mined_rules is_active` | MN có **nhiều `READY_STRONG` nhất** (6) |
| khai `FU-448` kèm ba hướng | agent **không tự chọn** — cả ba cần owner ký |
| thử tự động hoá `FU-447` | ánh xạ **vô nghĩa** ⇒ **TỪ CHỐI ghi** |

---

## 3 · Vấp trong phiên

**🟡 Suýt tin cảnh báo của cổng mà không truy.** `_v11107` ghi *«có thể ĐÚNG thiết kế — BÁO,
không chặn»*. Dừng ở đó thì đã bỏ qua một chênh lệch **không ai cố ý** giữa ba miền. Cảnh báo
«có thể đúng» **không phải** kết luận «đúng».

**🟡 Bộ gán tự động cho kết quả vô nghĩa** — `V11135 «gỡ về» → DECISION PACKET`,
`V11128 «đào bới» → BA LỚP NGUỒN`. Đã từ chối. Ghi lại để phiên sau **không làm lại cách sai đó**.

**🟡 Một lệnh `git commit` nối bằng `&&` im lặng không chạy** — tưởng đã commit, thực ra chưa.
Phát hiện nhờ `git log` không có bản mới. Bài học: **luôn xác minh bằng `git log`**, đừng tin
lệnh đã chạy chỉ vì không thấy lỗi.

---

## 4 · Trạng thái cuối

| | |
|---|---|
| production | 🟢 **không bị đụng** — bản này chỉ đo và ghi tài liệu |
| `FU-448` | 🔴 mới khai — chờ owner chọn 1 trong 3 hướng |
| `FU-447` | ⚪ giữ treo — **không tự động hoá được**, phải đọc từng bản |
| chờ owner | 🔴 `FU-444` · `FU-445` · `FU-446` · `FU-448` · `CAP5` · quyền thư mục |

---

TanPhatAI cần làm: ghi **`FU-448`** — MN **không bao giờ** nhận khối `🎯 RULE TAILS`, **KHÔNG phải thiết kế**; MN có nhiều `READY_STRONG` nhất (6) nhưng **0** luật được chấm hiệu quả trong 2 ngày ⇒ **ba miền chạy hai bộ hướng dẫn khác nhau, không ai cố ý**. Ghi **chưa kết luận MN mất gì** (`RM-04`). Ghi **`FU-447` không tự động hoá được**. Đọc bảng **13 câu nguyên văn của owner** ở mục 1 trước khi đối chiếu tài liệu với thực tế.
