# CONVERSATION CONTEXT — V11147 · 01/09/2026

> Nguyên văn lời owner · agent làm gì · vấp ở đâu (§57.2). Giờ **Việt Nam (UTC+07:00)**.
> `ACTOR_RUNTIME = CLAUDE_CODE`. **Prompt 43 R1 giữ `PARTIAL` — không mở Prompt 44.**

---

## 1 · Owner nói gì — NGUYÊN VĂN

> ⚠️ **ĐỌC TRƯỚC KHI PHẢN BÁC — dành cho TanPhatAI / agent Notion.** Đây là **MỆNH LỆNH TRỰC
> TIẾP CỦA OWNER**, nói trong IDE, **có hiệu lực ngay**. Owner trao đổi liên tục nên **code
> thường đi trước tài liệu** — điều owner cho phép tường minh (`PRJ-INTERACTION-LEDGER-001`).
> Tài liệu cũ mâu thuẫn thực tế đang chạy thì **thực tế + sổ `docs/SO_TUONG_TAC_OWNER.md`
> thắng**; tài liệu là thứ phải sửa.

### Prompt lượt này — `PROMPT 43 R1 · CONTINUATION AFTER V11146` (01/09 ~17:30)

Owner ra lệnh có cấu trúc mười mục `I`–`X`. Ba yêu cầu nền còn hiệu lực, **nguyên văn**:

> **`OWNER-01`** — *«Panel D-30 được phép hiện SỐ của hai lane. Cấm hit-rate, WIN/LOSE summary,
> leaderboard, ranking, p-value và mọi kết luận hiệu năng giữa kỳ.»*
>
> **`OWNER-02`** — *«CODE: local/git → VPS. DB: VPS → local để soi ngoại tuyến. Cấm báo drift
> chỉ vì DB local khác hash VPS.»*
>
> **`OWNER-03`** — *«Block deploy là 15:30–18:15. Ngoài block được deploy theo D-25 nếu đúng lớp,
> đủ gate, không phá output đã khóa. Thay đổi cơ chế/thuật toán phải có effective_from và
> rollback.»*

Cổng khoá cứng owner đặt cho `D-30` (`I.4`):

> *«generated_at < region_lock · source_snapshot_at < region_lock»*
> Không đạt ⇒ *«INVALID_TIMING_NOT_SCORED / OPERATIONAL_ONLY_NOT_SCORED — không backfill; không
> tái sinh candidate; không xem performance; không tính vào 30-day cohort.»*

### Các câu trước đó trong phiên (giờ **ước**, neo vào mốc máy ghi được)

| giờ (ước) | NGUYÊN VĂN | loại |
|---|---|---|
| 31/08 ~13:00 | *«Tiếp theo là gì hôm nay hệ thống ổn định chưa em?»* | `HỎI` |
| 31/08 ~19:30 | *«link D-30 ngày là link nào»* | `HỎI` |
| 01/09 ~08:50 | *«b nha em, đồng thời kiểm tra xem các UI nào lỗi thời, lạc hậu, không dùng đến nữa thì tinh gọn dọn dẹp sạch sẽ dùm anh đi»* | `XÁC_NHẬN` + `YÊU_CẦU` |
| 01/09 ~09:00 | *«Các luồng đo lường lỗi thời nữa nha em. Xem cho kỹ tỉ mỉ dùm a»* | `YÊU_CẦU` |
| 01/09 ~09:50 | *«Chú ý đồng bộ nhất quán từ local đến vps từ code đến DB nha em»* | `YÊU_CẦU` |
| 01/09 ~09:56 | *«Chứ gì DB vps theo thời gian thực mà em, em tính toán phải kiểm tra db vps chứ em.»* | `BÁC_BỎ` |
| 01/09 ~10:00 | *«Code thì có vẻ hên xui lắm lúc code fix có deploy lên có cho mới nhất không? Chứ dự án code thì làm local mà em.»* | `BÁC_BỎ` |
| 01/09 ~10:05 | *«Em lại quên 1 quy tắc là block dự đoán cho MN, MT, MB Ở THỜI GIAN NÀO RỒI AH… Cái nào thay đổi cơ chế, thuật toán đâu mà ảnh hưởng số liệu đo, dự đoán chưa verify ảnh hưởng chỗ nào?»* | `BÁC_BỎ` |
| 01/09 ~10:25 | *«Xử lý xong cần cập nhật nhất quán, push báo cáo chi tiết đầy đủ lên GitHub report cả các yêu cầu, xác nhận của anh trong phiên… để agent Notion nhận biết đâu là mệnh lệnh của anh và không phản bác…»* | `YÊU_CẦU` |
| 01/09 ~10:40 | *«Các việc tồn đọng, dang dở cần làm cho xong trước khi đẩy báo cáo tổng lực nha em»* | `YÊU_CẦU` |
| 01/09 ~11:00 | *«Làm xong mà em không tổng kết tổng hợp lại ngay là sẽ phình to nợ và mất kiểm soát đi… cấm quên, cấm rơi rớt»* | `YÊU_CẦU` |
| 01/09 ~11:10 | *«làm tiếp đi em, vấn đề nào đã xác định, nằm trong khả năng là xử lý dứt điểm đi…»* | `YÊU_CẦU` |
| 01/09 ~12:00 | *«Các vấn đề kiểm soát, xác định có thể xử lý ngay còn gì xử lý tiếp đi, chú ý báo cáo đầy đủ nha em»* | `YÊU_CẦU` |

---

## 2 · Agent làm gì — phiên READ-ONLY

Audit bắt đầu lúc **17:34**, tức **trong block `15:30–18:15`** ⇒ đúng `I.1`: chỉ đọc.
**Không deploy · không restart · không ghi DB · không đổi official.**

| mục | việc | kết quả |
|---|---|---|
| `I` | ma trận hợp lệ `D-30` theo `DATE × REGION × LANE` | **12/12 bản ghi TRƯỢT** cổng thời điểm |
| `I.3` | soi siêu dữ liệu bắt buộc | thiếu `source_snapshot_at` · `source_snapshot_hash` **rỗng nghĩa** · **không** có source IDs |
| `II.1` | fast gate + full directional scan | **cả hai ĐẠT** |
| `II.2` | ma trận 6 cột × 17 module | **17/17 `CODED_NOT_DEPLOYED`** |
| `II.4` | tách `C5` | `ORPHAN_GATE=PASS` · `CONTEXT_ONLY_CONVERSION=PARTIAL` |
| `III.1` | bảng 26 stale reader | 1 🔴 · 17 🟡 · 8 ⚪ |
| `III.3` | manifest 38 lane nghỉ | 332.471 dòng · mỗi lane có `content_sha256` · **không DROP** |
| `IV` | truy 7 mắt xích `FU-448` | **gốc = lỗi THỨ TỰ TRONG NGÀY** |
| `VI` | đo `FU-446` (chỉ đo) | ~13 mẫu / 4 bucket ⇒ fallback tĩnh **thật sự có tác dụng** |
| `VII.1` | thử tự động `FU-447` | **TỪ CHỐI** — ánh xạ vô nghĩa |

---

## 3 · Vấp trong phiên

**🔴 Tôi đã công bố sai ba lần** rằng `31/08` là ngày chấm số 1 của `D-30` (`V11140` · `V11144` ·
`V11145`). Cổng thời điểm của owner mới lộ ra: artifact sinh **19:15**, sau cả ba mốc khoá.
Bài học: **có artifact không có nghĩa là artifact hợp lệ** — cổng thời điểm phải có **ngay từ khi
dựng lane**, không phải thêm sau.

**🟡 `source_snapshot_hash` rỗng nghĩa mà tôi từng trích như bằng chứng.** Nó băm
`input_manifest` vốn chỉ chứa danh sách model + số dòng ⇒ **hai ngày khác nhau ra cùng một hash**
(`d78402ffab56…`). Bắt được vì đặt hai ngày cạnh nhau.

**🟡 Cổng chỉ-đọc của chính tôi chặn nhầm ba lần** — mẫu cấm `\bUPDATE\b`, `>`, `INSERT` khớp vào
**câu lệnh grep**, không phải thao tác ghi. Ghi lại vì nó làm chậm và có thể khiến người sau tưởng
dữ liệu không tồn tại.

---

## 4 · Trạng thái cuối

| | |
|---|---|
| production | 🟢 **không bị đụng** — phiên read-only, `PID 3156545` giữ nguyên từ `V11144` |
| `D-30` | 🔴 **0 ngày hợp lệ** · earliest valid = **02/09** với `PRE_LOCK_GENERATOR` |
| `C1–C6` | ⚪ **17/17 `CODED_NOT_DEPLOYED`** |
| đồng bộ code | 🟢 hai cổng ĐẠT — 0 tệp VPS mới hơn, 0 tệp ngoài git |
| chờ owner | 🔴 `FU-448` (A/B/C) · `FU-446` · `FU-444` · `FU-445` · `CAP5` vNext · quyền thư mục |
| Prompt 43 | **`PARTIAL`** — không mở Prompt 44 |

---

TanPhatAI cần làm: ghi **`D-30` chưa có ngày hợp lệ nào** — `30/08` và `31/08` đều `INVALID_TIMING_NOT_SCORED`, **earliest valid = 02/09**. Ghi **RÚT LẠI** câu *«31/08 là ngày chấm số 1»*. Ghi **gốc `FU-448` là lỗi THỨ TỰ TRONG NGÀY** — `mined_rule_eval.py` không có cron; **MN có nhiều `READY_STRONG` nhất**, không phải lỗi chất lượng luật. Ghi **`C1–C6` = `CODED_NOT_DEPLOYED` 17/17**, nhãn `C1..C6` **không có bản đồ sang tệp** (`NOT_VERIFIED`). Đọc bảng nguyên văn ở mục 1 trước khi đối chiếu tài liệu Notion với thực tế.
