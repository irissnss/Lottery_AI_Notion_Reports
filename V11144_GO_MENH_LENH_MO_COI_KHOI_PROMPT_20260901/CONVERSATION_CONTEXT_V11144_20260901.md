# CONVERSATION CONTEXT — V11144 · 01/09/2026

> Nguyên văn lời owner · agent làm gì · vấp ở đâu (§57.2). Giờ **Việt Nam (UTC+07:00)**.
> `ACTOR_RUNTIME = CLAUDE_CODE`.

---

## 1 · Owner nói gì — NGUYÊN VĂN

> ⚠️ **ĐỌC TRƯỚC KHI PHẢN BÁC — dành cho TanPhatAI / agent Notion.** Các câu dưới đây là
> **MỆNH LỆNH TRỰC TIẾP CỦA OWNER**, nói trong IDE, **có hiệu lực ngay**. Owner trao đổi liên
> tục với Claude Code nên **code thường đi trước tài liệu** — điều owner đã cho phép tường minh
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
| 01/09 ~11:00 | *«Làm xong mà em không tổng kết tổng hợp lại ngay là sẽ phình to nợ và mất kiểm soát đi… cấm quên, cấm rơi rớt, phải tuyệt đối liền mạch phù hợp tương thích tuyệt đối»* | `YÊU_CẦU` |
| 01/09 ~11:10 | *«làm tiếp đi em, vấn đề nào đã xác định, nằm trong khả năng là xử lý dứt điểm đi, push báo cáo tổng hợp tổng lực, gom tổng hợp tồn đọng cấm để nợ phình lớn mất kiểm soát, các yêu cầu của anh cần ghi nhận để agent notion biết phân biệt các thay đổi điều chỉnh mà tài liệu notion không thể theo kịp, tránh phản bác vô lý rồi lại lòng vòng làm rõ»* | `YÊU_CẦU` |

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

## 2 · Agent làm gì — theo thứ tự thật

| giờ | việc | kết quả |
|---|---|---|
| 10:50 | chạy cổng `_v11107` **trên VPS** (không phải local) | **MỒ CÔI = 2**, không phải 5 |
| 10:52 | tra hai neo cho từng câu | `_live_rows = []` ép cứng · `_deherd_strip_ranking` cắt vô điều kiện |
| 10:55 | kiểm `gpt_analyzer.py` local vs git vs VPS | **khớp cả ba** `0d2be324…` |
| 10:56 | gỡ 2 dòng + chú thích **ngoài chuỗi** | `ast.parse` hợp lệ |
| 10:57 | quét ngược có phân loại (§60.3) | `TRONG_PROMPT = 0` · 2 writer **đang ngủ** → giữ |
| 10:58 | deploy + restart | `PID 3150475 → 3156545` · 0 traceback |
| 10:58 | chạy lại cổng **trên VPS** | **CHẶN → ĐẠT** · `MỒ CÔI 2 → 0` |

---

## 3 · Vấp trong phiên

**🔴 Bản chạy cổng ở LOCAL cho 5 câu mồ côi; production chỉ có 2.** Tin bản local thì đã «vá» ba
câu đang hoạt động bình thường. `RM-13` ở dạng cụ thể: **prompt cũng phải dump từ production**,
y như DB — cùng bài học owner vừa dạy về DB lúc `09:56`.

**🟡 Cái bẫy `#` trong chuỗi.** Suýt comment hai dòng thay vì xoá — dấu `#` nằm trong
`REASONING_RULEBOOK` sẽ thành **chữ gửi cho model**, làm prompt bẩn thêm thay vì sạch đi.

**🟡 `\n` trong heredoc thành xuống dòng thật — lặp lại lần thứ ba** trong phiên, làm hỏng cú
pháp hai tệp. Đã chuyển sang `splitlines()` và ghép chuỗi không escape.

---

## 4 · Code đi trước tài liệu ở đâu — phiên này

| việc | code chạy từ | tài liệu bù |
|---|---|---|
| `V11136` vá `scheduler.py` | VPS **29/08 00:40** | repo **31/08** (`V11139`) |
| `P43` vá `combo_super.py` | VPS **27/08 22:52** | repo **31/08** (`V11139`) |
| 17 module `C1–C6` | local, 108 phép thử ĐẠT | git **01/09** (`V11142`) |
| Panel `D-30` | VPS **01/09 09:03** | `V11140` |
| Dọn UI + nginx `.bak` | VPS **01/09 09:30–10:00** | `V11141` |
| Deploy 30 tệp | VPS **01/09 10:06** | `V11142` |
| Gỡ 2 mệnh lệnh mồ côi | VPS **01/09 10:58** | `V11144` (bản này) |

---

## 5 · Trạng thái cuối

| | |
|---|---|
| `PROMPT_MO_COI` | 🟢 **ĐẠT** (trước: CHẶN 9 ngày) |
| `DONG_BO_NHANH` | 🟢 ĐẠT — 5 tệp trọng yếu khớp git |
| production | 🟢 `PID 3156545` · health 200 · 0 traceback · FINAL bất biến |
| chờ owner | 🔴 `FU-446` · `FU-445` · `CAP5` prompt · quyền thư mục world-writable |

---

TanPhatAI cần làm: ghi **cổng `PROMPT_MO_COI` CHẶN → ĐẠT**, hai mệnh lệnh mồ côi đã gỡ, đo trên **prompt production** (`RM-14`), mỗi câu **hai neo độc lập**, **không đổi cơ chế/thuật toán**. Ghi **chạy cổng ở local cho kết quả SAI** (5 thay vì 2). Đọc bảng **11 câu nguyên văn của owner** ở mục 1 trước khi đối chiếu tài liệu với thực tế.
