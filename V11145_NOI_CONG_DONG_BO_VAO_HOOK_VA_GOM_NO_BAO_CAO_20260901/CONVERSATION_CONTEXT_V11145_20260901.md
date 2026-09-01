# CONVERSATION CONTEXT — V11145 · 01/09/2026

> Nguyên văn lời owner · agent làm gì · vấp ở đâu (§57.2). Giờ **Việt Nam (UTC+07:00)**.
> `ACTOR_RUNTIME = CLAUDE_CODE`.

---

## 1 · Owner nói gì — NGUYÊN VĂN (đủ 12 câu của phiên)

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
| 01/09 ~10:25 | *«Xử lý xong cần cập nhật nhất quán, push báo cáo chi tiết đầy đủ lên GitHub report cả các yêu cầu, xác nhận của anh trong phiên làm việc trò chuyện để agent Notion nhận biết đâu là mệnh lệnh của anh và không phản bác khi có mâu thuẫn xảy ra giữa tài liệu và thực tế, vì thực tế anh đang tương tác liên tục với em và agent Notion không nắm và sẽ lỗi thời nên cần ghi nhận lại nha em.»* | `YÊU_CẦU` |
| 01/09 ~10:40 | *«Các việc tồn đọng, dang dở cần làm cho xong trước khi đẩy báo cáo tổng lực nha em»* | `YÊU_CẦU` |
| 01/09 ~11:00 | *«Làm xong mà em không tổng kết tổng hợp lại ngay là sẽ phình to nợ và mất kiểm soát đi nha anh nhắc lại cấm quên, cấm rơi rớt, phải tuyệt đối liền mạch phù hợp tương thích tuyệt đối đó nha»* | `YÊU_CẦU` |
| 01/09 ~11:10 | *«làm tiếp đi em, vấn đề nào đã xác định, nằm trong khả năng là xử lý dứt điểm đi, push báo cáo tổng hợp tổng lực, gom tổng hợp tồn đọng cấm để nợ phình lớn mất kiểm soát, các yêu cầu của anh cần ghi nhận để agent notion biết phân biệt các thay đổi điều chỉnh mà tài liệu notion không thể theo kịp tránh phản bác vô lý rồi lại lòng vòng làm rõ nha em»* | `YÊU_CẦU` |

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

| giờ | việc | kết quả |
|---|---|---|
| 11:15 | thêm `--nhanh` cho `_v11143` | **1,3 giây** cho 5 tệp trọng yếu |
| 11:20 | cắm vào `governance_guard.py` (`beforeShellExecution`) | bản đầu **sai tên biến** |
| 11:25 | thử chặn `RM-15` | **1/4** — phát hiện `except` nuốt `NameError` |
| 11:28 | sửa `REPO` → `REPO_ROOT` **và** sửa `except` | **3/3 ĐẠT** |
| 11:35 | bù §62 cho 14 báo cáo | không bịa lời owner |
| 11:40 | cổng commit **chặn** | bắt vi phạm **có sẵn** `REPORT_V11070.md:20` |
| 11:45 | đính chính `V11070` | `PRJ_WINDOW = SACH` |
| 11:50 | khai `FU-447` + cập nhật `FU-444` | nợ 50 → 38, **có danh sách chính xác** |

---

## 3 · Vấp trong phiên

**🔴 Cổng của chính tôi vô dụng ở bản đầu.** Sai tên biến (`REPO` vs `REPO_ROOT`) → `NameError`
→ `except Exception: pass` **nuốt im lặng** → cổng **cho qua**. Bắt được **chỉ vì** có bộ thử.
Sửa **hai** thứ: tên biến **và** cái `except` — nay chính cổng hỏng thì cũng chặn.

**🟡 Hook chặn CẢ lệnh Bash chứa `git commit`** nên **hai lần chỉnh sửa của tôi không hề chạy** —
tôi tưởng đã sửa mà thực ra chưa, và cứ thế commit lại rồi lại bị chặn. Bài học: khi hook chặn,
**toàn bộ** lệnh bị chặn, kể cả phần sửa tệp đứng trước. Phải tách lệnh sửa khỏi lệnh commit.

**🟡 `\n` trong heredoc thành xuống dòng thật — lần thứ ba trong phiên**, hỏng cú pháp hai tệp.

---

## 4 · Code đi trước tài liệu ở đâu — cả phiên

| việc | code chạy từ | tài liệu bù |
|---|---|---|
| `V11136` vá `scheduler.py` | VPS **29/08 00:40** | repo **31/08** (`V11139`) |
| `P43` vá `combo_super.py` | VPS **27/08 22:52** | repo **31/08** (`V11139`) |
| 17 module `C1–C6` | local, 108 phép thử ĐẠT | git **01/09** (`V11142`) |
| Panel `D-30` | VPS **01/09 09:03** | `V11140` |
| Dọn UI + nginx `.bak` | VPS **01/09 09:30–10:00** | `V11141` |
| Deploy 30 tệp | VPS **01/09 10:06** | `V11142` |
| Gỡ 2 mệnh lệnh mồ côi | VPS **01/09 10:58** | `V11144` |
| Cắm cổng vào hook deploy | local **01/09 11:20** | `V11145` (bản này) |

---

## 5 · Trạng thái cuối phiên

| | |
|---|---|
| production | 🟢 `PID 3156545` · health 200 · 0 traceback · FINAL bất biến |
| đồng bộ code | 🟢 0 tệp VPS mới hơn · cổng nay **chặn được deploy** (`RM-15` 3/3) |
| đồng bộ DB | 🟢 theo cặp · `integrity_check=ok` · **lệch hash là đúng thiết kế** |
| prompt | 🟢 `PROMPT_MO_COI = ĐẠT` (trước: CHẶN 9 ngày) |
| UI | 🟢 **84%** rác đã dọn · nginx cảnh báo 4 → 0 |
| `D-30` | 🟢 ngày chấm **số 1 = 31/08** · panel `/monitoring` đã có |
| nợ báo cáo | 🟡 **50 → 38** · tách `FU-447` (16) và `FU-444` (22) |
| chờ owner | 🔴 `FU-444` · `FU-446` · `FU-445` · `CAP5` prompt · quyền thư mục |

---

TanPhatAI cần làm: đọc **bảng 12 câu nguyên văn của owner** ở mục 1 **trước** khi đối chiếu tài liệu Notion với thực tế — owner tương tác liên tục trong IDE, **code được phép đi trước tài liệu**, và bảng ở mục 4 nói rõ **chỗ nào đi trước**. Ghi ba mệnh lệnh **`OWNER-01/02/03`** là LUẬT. Ghi **nợ báo cáo 50 → 38**, tách `FU-447` (16 bản tiêu đề lệch) và `FU-444` (22 bản thiếu hẳn, **đề xuất KHÔNG BÙ**, chờ owner ký). Ghi **`V11066`–`V11075` có `OWNER_SAID` KHÔNG TÁI LẬP ĐƯỢC** — sổ tương tác chỉ có từ **25/08**, đừng coi khoảng trống đó là mâu thuẫn.
