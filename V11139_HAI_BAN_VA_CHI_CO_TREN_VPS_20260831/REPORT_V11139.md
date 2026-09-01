# REPORT V11139 — HAI BẢN VÁ PRODUCTION **CHỈ TỒN TẠI TRÊN VPS** — deploy từ local là xoá mất chúng

> **Ngày:** 31/08/2026 · `ACTOR_RUNTIME = CLAUDE_CODE` · **Commit riêng:** `bf993e8`
> **Phiên:** 31/08 – 01/09/2026, owner tương tác liên tục trong IDE.

---

## 1 · Tóm tắt

Phiên soi ổn định 31/08 (13 agent) lật ra một **quả mìn**: hai bản vá đang chạy trên
production **chưa bao giờ vào repo**. Một lệnh deploy từ local là xoá sạch cả hai — tức mở lại
đúng sự cố MT ngày 28/08 đã lấy mất một ngày của owner.

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

### Hai tệp chỉ tồn tại trên VPS

| tệp | VPS | local == git | chênh |
|---|---|---|---|
| `scheduler.py` | `2961987d8c3a` · 9881 dòng | `6ba74fa8c322` · 9757 dòng | **124 dòng = TOÀN BỘ `V11136`** |
| `combo_super.py` | `47047b1dc0b7` · 2763 dòng | `ed503dfe1a40` · 2738 dòng | **25 dòng = bản vá `P43` 27/08** |

Local **không có một từ khoá nào** của `V11136`: `_LEASE_GIAY` · `AI_TOKEN_STATE` ·
`FINAL_LOCK_PASSED` · `BLOCKED_PRECONDITION`.

`combo_super.py` bản VPS thêm `AND (run_source IS NULL OR run_source NOT LIKE '%shadow%')` vào
truy vấn **tư cách dự tuyển** Combo-Super — chính nó chặn `gemini-3.5-flash` (SHADOW) đi vòng
vào FINAL, cái owner gọi là *«rút giả»*.

### Cách xử ĐÚNG: kéo VPS về repo

**Không** viết lại bản vá trên tệp local cũ — làm thế mất 124 dòng thật và đẻ ra bản thứ ba khác
cả hai. Xác minh trước khi nhận: `sha256` khớp VPS **từng byte** · `ast.parse` hợp lệ · **đọc
nguyên văn** 25 dòng của `P43`.

### Vì sao không ai thấy — cổng drift báo XANH GIẢ

`_v11050_kiem_drift.py` xếp cả hai vào ô *«git đi trước, VPS chưa nhận»* rồi in *«không ai sửa
thẳng trên VPS»* và **thoát 0**. Nó suy **một chiều**. Lúc `13:57` ngày 31/08 cổng **vẫn** in dấu
tích xanh trong khi cả hai bản vá đang nằm đó. *(Đã dựng cổng thay thế ở `V11143`.)*

### `RM-07` — vá một lỗi không phải vá cả họ lỗi

Ngày 30/08 tôi tìm ra `main.py` có bản vá `V11136` chưa vào repo, đóng nó, **rồi dừng lại**.
Nhưng `V11136` sửa **HAI** tệp. Nay quét đủ họ: `main.py` (đóng 30/08) · `scheduler.py` ·
`combo_super.py` (bản vá khác, phát hiện thêm).

### 🟡 RÚT LẠI theo `PRJ-RETRACTION-001`

**Chỗ gốc:** `REPORT_V11138.md` mục 6 + `CHANGELOG V11138`, công bố 30/08.
**Nguyên văn câu sai:** *«`DRIFT_K3_V11050` ĐẠT — 31 → 30, «chỉ có trên VPS» 2 → 0»*.
**Điều đúng:** con số đó đọc từ một cổng **không kiểm được chiều VPS-mới-hơn**; lúc ấy đã có
**hai** bản vá chỉ tồn tại trên VPS. Phép đo tái lập được: so `sha256` từng tệp giữa
**VPS · local · git HEAD** (không chỉ VPS vs git) + đối chiếu `mtime` VPS với ngày commit cuối.
**Quyết định nào dựa trên số sai:** không quyết định nào — nhưng nó để **quả mìn mở suốt hai
ngày**, và `REPORT_V11138` đã tuyên bố *«drift đã đóng»*.

---

## 4 · Hướng xử lý và vì sao chọn

Nêu trong mục 3 — mỗi phát hiện đi kèm lý do chọn hướng. Nguyên tắc chung của phiên: **không suy
từ một dấu hiệu**; mọi kết luận về «chết / thừa / lệch» đều phải có **hai neo độc lập** và phải
**đọc ngữ cảnh** chứ không đếm chuỗi thô (`RM-09`), và không kết luận theo **tên đoán** (`RM-10`).

---

## 5 · Đã làm gì — `TRƯỚC / SAU / PHIÊN BẢN / KIỂM` (§60.4)

```
TRƯỚC:  scheduler.py    local==git 9757 dòng, KHÔNG có V11136
        combo_super.py  local==git 2738 dòng, KHÔNG có P43
SAU:    cả hai kéo từ VPS về repo, khớp VPS TỪNG BYTE
PHIÊN BẢN: commit bf993e8 · KHÔNG deploy · KHÔNG restart
KIỂM:   sha256 khớp · ast.parse hợp lệ · drift 30 → 28
        ba tệp main.py/scheduler.py/combo_super.py nay khớp cả VPS · local · git
```

---

## 6 · Cổng kiểm

| cổng | kết quả |
|---|---|
| `sha256` khớp VPS từng byte (2 tệp) | ✅ ĐẠT |
| `ast.parse` hợp lệ | ✅ ĐẠT |
| `DRIFT_K3_V11050` | ✅ 30 → **28** |
| production không bị đụng | ✅ không deploy, không restart |

---

## 7 · Vướng vấp — **kể cả vấp do chính agent gây ra**

**Vấp của chính agent:** ngày 30/08 tôi đóng `main.py` rồi **dừng lại**, dù `V11136` sửa hai
tệp — đúng lỗi `RM-07` mà tôi vừa đi bắt người khác. Và tôi đã **trích con số của một cổng
báo xanh giả** vào báo cáo `V11138` mà không kiểm cổng đó đo cái gì.

---

## 8 · Gỡ về

```bash
git revert bf993e8     # repo-only, production không bị đụng trong bản này
```

---

## 9 · Theo dõi tiếp

| # | việc | trạng thái |
|---|---|---|
| 1 | Vá cổng drift để kiểm được chiều VPS-mới-hơn | ✅ **xong** ở `V11143` |
| 2 | 25 tệp còn lệch (git mới hơn VPS) | ✅ **xong** ở `V11142` — deploy 30/30 |

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

TanPhatAI cần làm: ghi **hai bản vá production chỉ tồn tại trên VPS đã được kéo về repo** — `scheduler.py` (124 dòng `V11136`, máy trạng thái token AI) và `combo_super.py` (25 dòng `P43` 27/08, lọc shadow khỏi dự tuyển Combo), commit `bf993e8`, **không deploy, không restart**. Ghi **RÚT LẠI** câu *«drift đã đóng»* trong `REPORT_V11138`. Ghi **cổng `_v11050` chỉ kiểm một chiều** ⇒ đã thay bằng `_v11143` ở bản sau.
