# REPORT V11143 — **CỔNG ĐỒNG BỘ BA ĐƯỜNG CÓ CHIỀU** · sổ tương tác owner · `FU-430` mốc 1 đã nổ · `FU-446`

> **Ngày:** 01/09/2026 · `ACTOR_RUNTIME = CLAUDE_CODE` · **Commit riêng:** `b0d7298`
> **Phiên:** 31/08 – 01/09/2026, owner tương tác liên tục trong IDE.

---

## 1 · Tóm tắt

Owner: *«Các việc tồn đọng, dang dở cần làm cho xong trước khi đẩy báo cáo tổng lực»*.
Bản này đóng **bốn việc treo** trước khi phát hành: cổng máy chống drift **có chiều**, sổ tương
tác owner, mốc `FU-430` đã nổ mà chưa ai ghi, và khai `FU-446`.

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

### 🟢 `_v11143_cong_dong_bo.py` — cổng máy cho lỗi đã tái phạm

`_v11050_kiem_drift.py` chỉ hỏi *«lệch hay không»* rồi mặc định **git đi trước**. Chiều ngược lại
**không có phép nào** — nên hai bản vá nằm trên VPS nhiều ngày mà cổng **vẫn in dấu tích xanh**
rồi **thoát 0**. Luật dự án: một lỗi tái phạm ⇒ phải thành **CỔNG MÁY**.

Cổng mới quyết định **CHIỀU** bằng cách so `mtime` VPS với **ngày commit cuối** chạm tệp:

| phân loại | nghĩa | |
|---|---|---|
| `BA_BAN_BA_DUONG` | local ≠ git ≠ VPS | 🔴 nặng nhất |
| `VPS_MOI_HON` | VPS mới hơn commit cuối ⇒ **có người vá thẳng lên VPS** | 🔴 deploy sẽ XOÁ bản vá |
| `CHI_CO_TREN_VPS` · `CHUA_VAO_GIT` | mã production ngoài version control | 🔴 |
| `VPS_CU_HON` | git đi trước ⇒ deploy sẽ cập nhật | ⚪ an toàn |

**Chỉ soi MÃ NGUỒN.** Cổng **không** so tệp DB — theo `OWNER-02`. **Ngoại lệ có chủ ý** khai
ngay trong mã, mỗi mục **bắt buộc kèm lý do**.

**Thử chặn `RM-15` — 4/4 ĐẠT.** Bản đầu của bộ thử **TRƯỢT 3/4** vì lấy **chính tệp cổng** làm
neo, mà lúc đó tệp chưa commit nên `git show HEAD:` rỗng ⇒ mọi ca rơi vào `CHUA_VAO_GIT`. Đúng
loại lỗi `RM-15` sinh ra để bắt, chỉ khác chiều: lần này **bộ thử** mới là thứ hỏng.

**Chạy thật: `DONG_BO_V11143=DAT`** — 0 tệp VPS mới hơn, 0 tệp ngoài git.

### 🟢 Sổ tương tác owner — ghi bù cả phiên

Owner nêu rõ lý do: *«để agent Notion nhận biết đâu là mệnh lệnh của anh và không phản bác khi có
mâu thuẫn xảy ra giữa tài liệu và thực tế»*. `docs/SO_TUONG_TAC_OWNER.md` **+5.537 ký tự**
(APPEND-ONLY): **11 mục nguyên văn** + ba mệnh lệnh `OWNER-01/02/03` + bảng **«code đi trước tài
liệu ở đâu»**.

### 🔴 `FU-430` — mốc 1/3 đã nổ 30/08, tới 01/09 chưa ai ghi

Đo trên **DB VPS**: AUC trung bình ML miền MB **suy giảm đơn điệu 4 tuần liền**:

| ngày | AUC TB | |
|---|---|---|
| 09/08 | 0,4974 | |
| 16/08 | 0,4914 | |
| 23/08 | 0,4838 | |
| **30/08** | **0,4764** | ← mốc 1 nổ |

Ba trên bốn model dưới `0,50` — **kém hơn đoán ngẫu nhiên** — và **cả ba đều tệ đi**:
`xgboost 0,4765→0,4649` · `random-forest 0,4736→0,469` · `meta-learning 0,4845→0,4703`.
Cùng ngày **MN `0,5151` · MT `0,5282`** ⇒ vấn đề **riêng của MB**.

Ngưỡng đăng ký trước nên mốc 2 (`06/09`) và mốc 3 (`13/09`) **phải để chạy tiếp**; cấm kết luận
sớm và cấm đổi ngưỡng giữa chừng (`RM-08`).

### 🔴 `FU-446` — bảng hiệu chỉnh 15 khoá / 24 model

Thiếu 12 model đang sống; giữ ngược lại khoá của model **đã rời pool** (`gpt-5-mini`, `gpt-5.4`).
**Phải hỏi owner trước** — khác hẳn ba việc ngày 01/09: đổi hệ số **CÓ** đổi `strength` ghi vào
`predictions`. Kèm cảnh báo phương pháp: `use_dynamic=True` **thử DB trước**, bảng tĩnh chỉ là
**nhánh dự phòng**.

---

## 4 · Hướng xử lý và vì sao chọn

Nêu trong mục 3 — mỗi phát hiện đi kèm lý do chọn hướng. Nguyên tắc chung của phiên: **không suy
từ một dấu hiệu**; mọi kết luận về «chết / thừa / lệch» đều phải có **hai neo độc lập** và phải
**đọc ngữ cảnh** chứ không đếm chuỗi thô (`RM-09`), và không kết luận theo **tên đoán** (`RM-10`).

---

## 5 · Đã làm gì — `TRƯỚC / SAU / PHIÊN BẢN / KIỂM` (§60.4)

```
TRƯỚC:  không có phép nào kiểm chiều VPS-mới-hơn
        sổ tương tác dừng ở 26/08 · FU-430 mốc 1 nổ 30/08 chưa ai ghi · FU-446 chưa khai
SAU:    _v11143_cong_dong_bo.py — 4 phân loại có chiều + ngoại lệ có lý do
        SO_TUONG_TAC_OWNER.md +5.537 ký tự · FU-430 cập nhật · FU-446 khai mới
PHIÊN BẢN: commit b0d7298 · KHÔNG deploy · KHÔNG restart
KIỂM:   THU_CHAN_V11143 = 4/4 · DONG_BO_V11143 = ĐẠT
```

---

## 6 · Cổng kiểm

| cổng | kết quả |
|---|---|
| `THU_CHAN_V11143` (`RM-15`, 4 phép hai chiều) | ✅ **4/4 ĐẠT** |
| `DONG_BO_V11143` chạy thật | ✅ **ĐẠT** — 0 tệp VPS mới hơn |
| `NANG_VERSION_V11062` `K1..K4` | ✅ ĐẠT |
| sổ tương tác APPEND-ONLY (không ngắn đi) | ✅ ĐẠT |

---

## 7 · Vướng vấp — **kể cả vấp do chính agent gây ra**

**Bộ thử của chính tôi TRƯỢT 3/4 ở bản đầu** — neo vào tệp chưa commit. Ghi lại vì nó minh hoạ
đúng điều `RM-15` cảnh báo: cổng không qua thử coi như không tồn tại, và **bộ thử cũng có thể là
thứ hỏng**.

---

## 8 · Gỡ về

```bash
git revert b0d7298     # repo-only, production không bị đụng
```

---

## 9 · Theo dõi tiếp

| # | việc | chặn ở đâu |
|---|---|---|
| 1 | **`FU-446`** đo lại bảng hiệu chỉnh | 🔴 **chờ owner ký** |
| 2 | **`FU-430`** mốc 2 (`06/09`) · mốc 3 (`13/09`) | ⚪ để chạy tiếp, cấm kết luận sớm |
| 3 | **`FU-445`** `DEGRADED_BODY_OVER_HTTP` | 🔴 chờ owner mở `/du-doan` chọn MT 28/08 |
| 4 | quyền thư mục world-writable trên VPS | 🔴 chờ owner |
| 5 | 26 bảng còn bị đọc / 38 lane nghỉ | ⚪ đã đo, chưa xử |
| 6 | `CAP5` hợp đồng prompt 8 LLM | 🔴 chờ owner ký |
| 7 | nối `_v11143` vào hook `git commit` | ⚪ chưa làm |

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

TanPhatAI cần làm: ghi **cổng `_v11143_cong_dong_bo.py`** — phân loại **CÓ CHIỀU**, `RM-15` **4/4**, chạy thật **ĐẠT**; nó thay chỗ mù của `_v11050`. Ghi **sổ tương tác owner +5.537 ký tự** với **11 mục nguyên văn** và ba mệnh lệnh **`OWNER-01/02/03`** — đây là nguồn để không phản bác khi tài liệu lệch thực tế. Ghi **`FU-430` mốc 1 đã nổ 30/08**: AUC ML MB `0,4764`, giảm đơn điệu 4 tuần, 3/4 model dưới `0,50`; mốc 2 `06/09`, mốc 3 `13/09`. Ghi **`FU-446` chờ owner ký**.
