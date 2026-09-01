# REPORT V11140 — PANEL `D-30` TRÊN `/monitoring` — **OWNER CHỌN PHƯƠNG ÁN (b)**, hiện cả số hai lane

> **Ngày:** 01/09/2026 · `ACTOR_RUNTIME = CLAUDE_CODE` · **Commit riêng:** `2897999`
> **Phiên:** 31/08 – 01/09/2026, owner tương tác liên tục trong IDE.

---

## 1 · Tóm tắt

Owner hỏi *«link D-30 ngày là link nào»*. Sự thật lúc đó: **không có link nào** — route
chứa `d30` trả `[]`, `main.py` nhắc `d30` **0 dòng**, frontend 0 trang. Agent trình ba phương án
và **khuyên (a)** (panel vận hành, giấu hiệu năng); **owner chọn (b)** — hiện cả số dự đoán.
Đã nêu lo ngại một lần, owner quyết, thi hành đúng yêu cầu.

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

### Ranh giới đã giữ — và vì sao

Panel hiện **SỐ**: `bach_thu` · `score_breakdown` · `contribution_trace` · nhãn ·
`degraded_reason`. Nó **cố ý KHÔNG** tính hit rate · **KHÔNG** xếp hạng · **KHÔNG** p-value ·
**KHÔNG** so với `lottery_results` — đó **đúng danh sách `QD-072` gọi tên** khi khoá «cấm đọc
giữa kỳ tới 30/09». Owner xem số; **máy không chấm hộ**. Ghi thẳng vào docstring hàm để phiên
sau không tự tiện thêm.

**Không mâu thuẫn `QD-072`:** `QD-072` cấm đọc **hiệu năng**, không cấm nhìn **số**.

### §52 — đăng ký ở CẢ HAI chỗ

`monitoring.html:8517` lần nạp đầu (`Promise.all`) **và** `:8526` `setInterval` 60s.
Thiếu vế thứ hai là `§52B_VIOLATION_REFRESH_MISSING`.

### 🔴 Một lỗi bộ smoke của tôi suýt cho qua

Vòng deploy đầu **ĐẠT HẾT CỔNG**: route đăng ký, ẩn danh `401`, no-drift, 0 traceback. Nhưng gọi
**thẳng hàm** thì `NameError: name 'io' is not defined` — `main.py` **không** import `io` ở
module-level. Với người dùng admin thật, endpoint sẽ ném **500**. Cổng smoke **không lộ** vì
`401` chặn **trước** khi thân hàm chạy.

**Bài học:** với endpoint `ADMIN_ONLY`, `401` chứng minh **route + cổng**, **không** chứng minh
**thân hàm**. Phải kiểm tầng dữ liệu riêng.

### Trạng thái `D-30`

`2026-08-30.jsonl` `WARMUP_NOT_SCORED` · `2026-08-31.jsonl` = **ngày chấm số 1** (cron 19:15 chạy
thật: `ghi_moi 6 · bỏ qua trùng 0`, nhãn **không còn** `WARMUP`).

`CAP5` **vẫn chưa chấm được**: cổng trong lane là *bất kỳ model nào thiếu top-5 ⇒ cả lane rỗng*,
mà 8 model LLM chỉ trả **2 số** theo hợp đồng prompt. Đo trên dữ liệu thật cả ba miền:
`lstm` 10 ứng viên · `meta-learning`/`random-forest`/`xgboost` 5 · **8 LLM = `predictions` NULL**.

---

## 4 · Hướng xử lý và vì sao chọn

Nêu trong mục 3 — mỗi phát hiện đi kèm lý do chọn hướng. Nguyên tắc chung của phiên: **không suy
từ một dấu hiệu**; mọi kết luận về «chết / thừa / lệch» đều phải có **hai neo độc lập** và phải
**đọc ngữ cảnh** chứ không đếm chuỗi thô (`RM-09`), và không kết luận theo **tên đoán** (`RM-10`).

---

## 5 · Đã làm gì — `TRƯỚC / SAU / PHIÊN BẢN / KIỂM` (§60.4)

```
TRƯỚC:  không route nào phục vụ D-30; owner không có link
SAU:    GET /api/admin/d30-lane (require_admin · no-store · ?days=1..400)
        panel #sectionD30Lane trên /monitoring
PHIÊN BẢN: main.py 2c81c579dd2b -> b618f0ed84ee (+104 dòng)
        monitoring.html 01e729b9ce62 -> 2c43ba6afcfe (+92 dòng, GIỮ CRLF)
        PID 2980020 -> 3110970 -> 3114967 · backup .bak_v11140
KIỂM:   AST — handler mới gắn ĐÚNG decorator · hàm phụ trợ decorator_list == []
        · handler CŨ ở neo giữ nguyên decorator  ⇒ KHÔNG lặp lại P0 hôm 30/08
        bảng route tiến trình sống: ['api_admin_d30_lane']
        tầng dữ liệu trên VPS với artifact THẬT: 2 ngày × 6 bản ghi · 0 cảnh báo
```

---

## 6 · Cổng kiểm

| cổng | kết quả |
|---|---|
| `CHEN_API_D30` (AST 3 phép) | ✅ ĐẠT |
| `CHEN_PANEL_D30` (6 phép, giữ CRLF) | ✅ ĐẠT |
| `DEPLOY_V11140b` (8 phép) | ✅ ĐẠT |
| ẩn danh `401` · `/du-doan` `200` · 0 traceback | ✅ ĐẠT |

---

## 7 · Vướng vấp — **kể cả vấp do chính agent gây ra**

Xem mục *«lỗi bộ smoke»* ở trên — `401` che mất `NameError` trong thân hàm. Ngoài ra một phép
kiểm *«panel có trong HTML đã serve»* của tôi **sai**: `/monitoring` trả `401` nên `curl` bắt
được thân 401 chứ không phải trang. Đã kiểm lại đúng chỗ (tệp trên đĩa).

---

## 8 · Gỡ về

```bash
sudo cp <BACKEND>/main.py.bak_v11140 <BACKEND>/main.py
sudo cp <FRONTEND>/monitoring.html.bak_v11140 <FRONTEND>/monitoring.html
sudo systemctl restart lottery
```

---

## 9 · Theo dõi tiếp

| # | việc | chặn ở đâu |
|---|---|---|
| 1 | `CAP5` — 8 LLM chỉ trả 2 số | **chặn ở owner**: cần ký đổi hợp đồng prompt |
| 2 | `FU-445` `DEGRADED_BODY_OVER_HTTP` | **chặn ở owner**: cần phiên admin thật |
| 3 | Cấm đọc hiệu năng `D-30` tới `30/09` | đang tuân |

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

TanPhatAI cần làm: ghi **`OWNER-01`: owner chọn phương án (b)** — panel `D-30` được phép hiện SỐ dự đoán, agent đã khuyên (a) và owner bác. **Không mâu thuẫn `QD-072`** (cấm đọc hiệu năng, không cấm nhìn số). Ghi **`31/08` là ngày chấm số 1** của `D-30`. Ghi **`CAP5` bế tắc cấu trúc** — 8 LLM chỉ trả 2 số, cần owner ký đổi prompt.
