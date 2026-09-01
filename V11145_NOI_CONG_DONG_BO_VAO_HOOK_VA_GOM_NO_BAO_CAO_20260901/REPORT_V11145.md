# REPORT V11145 — NỐI CỔNG ĐỒNG BỘ VÀO HOOK CHẶN DEPLOY · bù §62 cho 14 báo cáo · nợ báo cáo **50 → 38**

> **Ngày:** 01/09/2026 · `ACTOR_RUNTIME = CLAUDE_CODE` · **Commit riêng:** `260f373` ·
> **Công khai:** `f9e5376` · **Theo dõi:** `FU-444` · `FU-447`

---

## 1 · Tóm tắt

Owner yêu cầu xử dứt điểm những gì đã xác định và **gom tồn đọng, cấm để nợ phình lớn**. Bản này:
nối cổng đồng bộ vào **hook chặn deploy** (đúng chỗ nguy hiểm), bù mục §62 cho **14** báo cáo mà
**không bịa lời owner**, và **tách bạch** nợ báo cáo còn lại thành hai mục có **danh sách chính
xác** thay vì một con số mơ hồ.

---

## 2 · Owner yêu cầu gì — nguyên văn

> **01/09 ~11:10** — *«làm tiếp đi em, vấn đề nào đã xác định, nằm trong khả năng là xử lý dứt
> điểm đi, push báo cáo tổng hợp tổng lực, gom tổng hợp tồn đọng cấm để nợ phình lớn mất kiểm
> soát, các yêu cầu của anh cần ghi nhận để agent notion biết phân biệt các thay đổi điều chỉnh
> mà tài liệu notion không thể theo kịp, tránh phản bác vô lý rồi lại lòng vòng làm rõ nha em»*
>
> **01/09 ~11:00** — *«Làm xong mà em không tổng kết tổng hợp lại ngay là sẽ phình to nợ và mất
> kiểm soát đi… cấm quên, cấm rơi rớt, phải tuyệt đối liền mạch phù hợp tương thích tuyệt đối»*
>
> **01/09 ~10:40** — *«Các việc tồn đọng, dang dở cần làm cho xong trước khi đẩy báo cáo tổng
> lực nha em»*

Bảng **12 câu nguyên văn** của owner trong phiên và ba mệnh lệnh `OWNER-01/02/03` nằm ở
`CONVERSATION_CONTEXT` cùng thư mục và `docs/SO_TUONG_TAC_OWNER.md`.

⚠️ **TanPhatAI:** owner trao đổi liên tục trong IDE nên **code thường đi trước tài liệu** — điều
owner cho phép tường minh (`PRJ-INTERACTION-LEDGER-001`). Tài liệu cũ mâu thuẫn thực tế đang
chạy thì **thực tế + sổ tương tác thắng**.

---

## 3 · Đào bới / phát hiện

### 3.1 Cổng đồng bộ mới chỉ chạy tay — chưa chặn được gì

`_v11143_cong_dong_bo.py` dựng ở `V11143` phân loại **có chiều**, nhưng **không ai gọi nó tự
động**. Một cổng không được cắm vào đường đi thì không chặn được gì.

**Đúng chỗ cắm là `beforeShellExecution`, không phải `git commit`** — vì bản vá bị xoá ở lúc
**DEPLOY**, không phải lúc commit.

### 3.2 Ngân sách hook 20 giây — quét đầy đủ không kịp

`.cursor/hooks.json` cho `governance_guard.py` **timeout 20**. Quét 581 tệp mất hàng chục giây.
⇒ thêm chế độ `--nhanh`: so **5 tệp production trọng yếu** trong **một lượt `sha256sum`**.
Đo được **1,3 giây**.

**Đánh đổi nói thẳng:** `--nhanh` **KHÔNG thay** lượt quét đầy đủ. Nó chặn **đúng ca đã xảy ra**
(`scheduler.py` · `combo_super.py`), không phủ hết mọi tệp.

### 3.3 🔴 Bộ thử bắt được lỗi trong chính khối vừa chèn

Bản đầu dùng **sai tên biến** — `REPO` thay vì `REPO_ROOT` → `NameError` → bị
`except Exception: pass` **nuốt im lặng** → cổng **cho qua như không có gì**.

Nếu không thử thì đã có một cổng **hoàn toàn vô dụng** nằm đó và **không ai biết** — đúng điều
`RM-15` cảnh báo: *«cổng không qua thử coi như KHÔNG TỒN TẠI»*.

### 3.4 🔴 Cổng commit chặn đúng — bắt một vi phạm CÓ SẴN

Khi chạm vào 16 tệp báo cáo, `_v11088_cong_cua_so_chon.py` (`PRJ-SELECTION-WINDOW-001`) quét lại
và bắt `REPORT_V11070.md:20`: câu *«3/3 bạch thủ»* đọc thành **tuyên bố hiệu quả** trên thước
`TW-001` mà **chỉ có 0/3 cửa sổ**.

### 3.5 Nợ báo cáo tách thành hai loại khác hẳn nhau

| loại | số | bản chất |
|---|---|---|
| **`FU-447`** — có nội dung, **tiêu đề ngoài khung** | **16** | lỗi **cách viết** của agent |
| **`FU-444`** — **không có báo cáo** | **22** | lỗ hổng **lịch sử** |

**Khẳng định đáng giá: `FU-444` ĐÃ ĐÓNG BIÊN** — không bản nào sau `V11087B` thiếu báo cáo. Lỗ
hổng **không còn rò theo thời gian thực**; `V11088` → `V11144` đều có.

---

## 4 · Hướng xử lý và vì sao chọn

### Bù §62 — cách bù KHÁC NHAU theo thời kỳ, và vì sao

| nhóm | vì sao khác | cách bù |
|---|---|---|
| `V11066`–`V11075` (13–16/08) | sổ `SO_TUONG_TAC_OWNER.md` **chưa tồn tại** (ký 25/08) | ghi thẳng `OWNER_SAID` **KHÔNG TÁI LẬP ĐƯỢC** + lý do |
| `V11131` · `V11132` (25–28/08) | sổ đã có, prompt owner còn trong `CONVERSATION_CONTEXT` | trỏ tới nguồn thật, **không chép lại** |

**Cố tình KHÔNG bịa lời owner để cổng xanh.** Viết một câu *«owner yêu cầu…»* nghe hợp lý là
**chế dữ liệu** — `RM-17` cấm, và đúng lý do §63 đã **từ chối** bù 286 dòng `HISTORY`:

> *«bù 286 dòng suy từ tiêu đề rồi đóng dấu như thể ghi lúc xảy ra là chế dữ liệu — `RM-17` cấm.
> **Ghi thẳng là thiếu, kèm lý do.**»*

Hai lớp `CODE_DID` + `DOC_SAID` **tái lập được cho cả hai thời kỳ** bằng `git log` và `CHANGELOG`
⇒ vẫn ghi đủ, kèm **lệnh chạy lại được**.

### `FU-444` — đề xuất KHÔNG BÙ, và vì sao không tự quyết

Đây là **nhượng bộ một luật quản trị** (`A55_VIOLATION_REPORT_MISSING`) nên agent **không tự
quyết**. Việc agent tự làm được là dựng cơ chế **khai khoảng trống** (giống `GAP_MARKER` của
`_v11062`) — mục đích **không phải** làm cổng xanh cho dễ, mà để **tách bạch** «22 khoảng trống
lịch sử đã khai» với «vi phạm MỚI», kẻo một bản thiếu hôm nay bị chôn trong đống 22 bản cũ.

---

## 5 · Đã làm gì — `TRƯỚC / SAU / PHIÊN BẢN / KIỂM` (§60.4)

```
TRƯỚC:  _v11143 chỉ chạy tay · 14 báo cáo thiếu §62 · V11144 chưa có báo cáo
        nợ báo cáo 50/220 · REPORT_V11070.md:20 trích một cửa sổ
SAU:    _v11143 --nhanh cắm vào beforeShellExecution (governance_guard.py)
        14 báo cáo đã bù §62 · V11144 đã phát hành · V11070 đã đính chính
        nợ báo cáo 38/221 · tách thành FU-447 (16) và FU-444 (22)
PHIÊN BẢN: commit riêng 260f373 · công khai f9e5376 · KHÔNG deploy · KHÔNG restart
KIỂM:   THU_CHAN_HOOK_V11145 = 3/3 · PRJ_WINDOW = SACH · DONG_BO_NHANH = ĐẠT (1,3 giây)
```

Sửa **hai** thứ trong khối hook, không phải một: tên biến, **và** cái `except` quá im — nay khi
chính cổng hỏng thì nó **cũng chặn** (`ask`) kèm lý do, thay vì lặng lẽ `allow`.

Đính chính `REPORT_V11070.md`: *«3/3 bạch thủ»* là kết cục của **đúng một ngày** (14/08), so với
nền của **chính ngày đó**; `RM-04` → `n = 3` là **«chưa được phép kết luận»**; đủ bộ cửa sổ ở
`V11084`/`V11086` đo được **dấu đổi**: `30 ngày +4,07pp` · `90 ngày −3,18pp` · `180 ngày +0,91pp`
· `CI95 [−3,2 → +5,0]`; **CẤM trích** riêng cửa sổ 30 ngày.

---

## 6 · Cổng kiểm

| cổng | kết quả |
|---|---|
| `THU_CHAN_HOOK_V11145` (`RM-15`, 3 chiều) | ✅ **3/3 ĐẠT** — lệch→`ask` · khớp→`allow` · **cổng hỏng→`ask`** |
| `DONG_BO_NHANH` | ✅ ĐẠT · **1,3 giây** (ngân sách 20s) |
| `PRJ_WINDOW` sau đính chính | ✅ **SACH** |
| `NANG_VERSION_V11062` `K1..K4` | ✅ ĐẠT |
| nợ báo cáo công khai | ✅ **50 → 38** |

---

## 7 · Vướng vấp

**🔴 Cổng của chính tôi vô dụng ở bản đầu** — sai tên biến, bị `except` nuốt. Bắt được **chỉ vì**
có bộ thử. Nếu chỉ «viết xong rồi cắm» thì đã có một cổng luôn xanh nằm đó.

**🟡 Hook chặn cả lệnh Bash chứa `git commit`** nên **hai lần chỉnh sửa của tôi không hề chạy** —
tôi tưởng đã sửa mà thực ra chưa. Bài học: khi hook chặn, **toàn bộ** lệnh bị chặn, kể cả phần
sửa tệp đứng trước. Phải tách lệnh sửa ra khỏi lệnh commit.

**🟡 `\n` trong heredoc thành xuống dòng thật — lần thứ ba trong phiên**, làm hỏng cú pháp hai
tệp. Đã chuyển sang `splitlines()` và ghép chuỗi không escape.

---

## 8 · Gỡ về

```bash
git revert 260f373                      # kho riêng — repo-only, production không bị đụng
git -C <kho công khai> revert f9e5376   # kho báo cáo
cp backups/governance_guard.py.pre_v11145 .cursor/hooks/governance_guard.py
```

---

## 9 · Theo dõi tiếp

| # | việc | chặn ở đâu |
|---|---|---|
| 1 | **`FU-444`** — 22 bản không có báo cáo, đề xuất **KHÔNG BÙ** | 🔴 **chờ owner ký** (nhượng bộ luật quản trị) |
| 2 | **`FU-447`** — 16 bản tiêu đề ngoài khung | ⚪ agent tự làm, cần **đọc từng bản** |
| 3 | **`FU-446`** — bảng hiệu chỉnh 15 khoá/24 model | 🔴 chờ owner ký (**có** đổi `strength`) |
| 4 | **`FU-445`** — `DEGRADED_BODY_OVER_HTTP` | 🔴 chờ owner mở `/du-doan` chọn MT 28/08 |
| 5 | **`FU-430`** mốc 2 `06/09` · mốc 3 `13/09` | ⚪ để chạy tiếp, cấm kết luận sớm |
| 6 | `CAP5` hợp đồng prompt 8 LLM | 🔴 chờ owner ký |
| 7 | quyền thư mục `drwx---rwx` trên VPS | 🔴 chờ owner |
| 8 | 26 bảng còn bị đọc / 38 lane nghỉ (332.471 dòng) | ⚪ đã đo, chưa xử |
| 9 | `🎯 RULE TAILS` chỉ có ở MT/MB | ⚪ chưa xác minh là thiết kế hay lỗi |

---

## 10 · Nguồn ba lớp (§62)

### `OWNER_SAID`
*«gom tổng hợp tồn đọng cấm để nợ phình lớn mất kiểm soát»* (01/09 ~11:10). Đủ 12 câu nguyên văn
ở `CONVERSATION_CONTEXT` cùng thư mục và `docs/SO_TUONG_TAC_OWNER.md`.

### `CODE_DID`
`.cursor/hooks/governance_guard.py` +34 dòng · `_v11143_cong_dong_bo.py` thêm `--nhanh` ·
14 `REPORT_*.md` bù §62 · `REPORT_V11070.md` đính chính · commit `260f373` / `f9e5376` ·
`THU_CHAN_HOOK_V11145 = 3/3` · `PRJ_WINDOW = SACH`.

### `DOC_SAID`
`CHANGELOG.md §V11145` · `docs/CURRENT_TRUTH_SSOT.md §V11145` ·
`docs/FOLLOW_UP_TRACKER.md → FU-447` và `FU-444` (cập nhật) · `docs/SO_TUONG_TAC_OWNER.md`.

### Ba lớp lệch nhau
`DOC_SAID` ≠ `CODE_DID`: §57.3 ghi *«cổng kiểm dò theo tiêu đề»* nhưng **16 báo cáo do chính
agent viết** lại đặt tiêu đề theo chủ đề — tài liệu có luật, agent không theo. Đã khai `FU-447`
kèm danh sách chính xác.

---

TanPhatAI cần làm: ghi **cổng đồng bộ nay CHẶN được deploy** (`_v11143 --nhanh` cắm vào `beforeShellExecution`, `RM-15` **3/3**, kể cả ca **chính cổng hỏng cũng chặn**). Ghi **bù §62 cho 14 báo cáo** — với `V11066`–`V11075` thì `OWNER_SAID` **KHÔNG TÁI LẬP ĐƯỢC** vì sổ tương tác chỉ có từ **25/08**; **đừng đi tìm, đừng coi là mâu thuẫn**. Ghi **nợ báo cáo 50 → 38**, tách thành **`FU-447`** (16 bản tiêu đề lệch, agent tự làm) và **`FU-444`** (22 bản thiếu hẳn, **đề xuất KHÔNG BÙ**, chờ owner ký). Ghi **`FU-444` đã đóng biên**: không bản nào sau `V11087B` thiếu báo cáo.
