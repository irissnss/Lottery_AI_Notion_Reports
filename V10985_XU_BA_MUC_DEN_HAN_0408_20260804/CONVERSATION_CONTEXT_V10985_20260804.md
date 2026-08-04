# Ngữ cảnh phiên V10985 — 2026-08-04 (giờ Việt Nam)

Ghi **nguyên văn** lời owner, agent làm gì theo thứ tự, và vấp ở đâu. Không diễn giải lại lời
owner.

---

## 1. Owner nói gì — nguyên văn

**04/08 ~22:4x** — quyết định của phiên này:

> *"xử luôn tối nay"*

(ba mục đến hạn hôm nay 04/08, để không trễ hạn: `FU-187` · `FU-191` · `FU-212`)

**Nhắc gốc của `FU-191`** — owner nói **lần thứ hai** về chỗ này:

> *"cắt model ảnh hưởng đến combo super mới quan trọng cận thận chỗ này"*

**04/08 10:29** — nền của lịch cuốn chiếu (`QD-021`):

> *"Giãn ra cuốn chiếu tới hết ngày 10/08 phải hoàn thành, làm lần lượt những vấn đề nào xác thực
> rõ ràng , đơn giản làm trước tới cuối cùng 10/08 phải xong"*

**04/08 11:0x** — `QD-022`:

> *"Giãn luôn 9 mục cũ đó ra 05-09/08 cho ngày chốt nhẹ"*

**04/08 12:4x** — `QD-022` bổ sung:

> *"Chuyển xuống 06/08 - 09/08 còn 8 mục"*

**04/08 21:35** — bối cảnh "làm sớm hơn dự kiến":

> *"Thực sự quán chán ngán kết quả dự đoán quá tệ anh cần một kế hoạch triển khai sơm hơn dự kiến
> em xem thử dùm anh có triển khai được gì trước không em ? Theo như anh quan sat thấy offical
> cũng khá tiềm năng chứ em, cần 1 sự kết hợp hoàn hảo ở /nghiem-thu và offical nha . Kết quả dự
> đoán ngày hôm nay thế nào em thử tổng lực dùm anh."*

---

## 2. Agent làm gì — theo thứ tự

| # | Việc | Kết quả |
|---|---|---|
| 1 | Chạy `_v10920_session_start.py` **trước khi làm gì khác** | 3 mục đến hạn hôm nay · 1 quá hạn (`FU-225`) · **18 mồ côi** (ghi lại làm mốc so sánh cuối phiên) |
| 2 | Đọc `docs/FOLLOW_UP_TRACKER.md` lấy nội dung đầy đủ 3 mục | Mỗi mục có **4 bản** trong sổ (ghi chồng). Bản gần đầu file = sự thật hiện tại (V10981b), bản dưới là lịch sử |
| 3 | Đọc `_v10958_fu_reader.py` | Xác nhận: reader lấy **bản đầu tiên**; `TREO_STATUSES` 9 nhãn · `DONG_STATUSES` 7 nhãn |
| 4 | Đọc **cả hai** cổng lịch trước khi sửa gì | **Phát hiện `K8` sẽ chặn oan** khi đóng mục — xem §3.1 |
| 5 | Chạy cả hai cổng lấy **mốc nền** | `_v10981_kiem_lich.py` 8/8 · `_v10982_kiem_lich9.py` 8/8 |
| 6 | Viết `_v10985_bang_chung.py` (chỉ đọc) | Vì `artifacts/` và `*.log` nằm trong `.cursorignore`, công cụ đọc tệp không mở được hai bằng chứng chính |
| 7 | Đọc `combo_super.py` để viết luật cho đúng | **Phát hiện mô tả cũ của FU-191 sai 3 chỗ** — xem §3.2 |
| 8 | Kiểm `MIN_MAU_DU_TUYEN` và `_cham_diem_du_tuyen` | **Phát hiện sàn 5 lượt không áp ở nhánh chọn thật** → mở `FU-265` |
| 9 | Viết **§59 (A57)** vào `CLAUDE.md` rồi 3 mặt còn lại; thêm §58+§59 vào bảng đánh số | `.antigravityrules` trước đó **thiếu cả §58** (ký 02/08) |
| 10 | `_v10925_rule_sync_check.py` (không `--check`) | Sinh lại `AGENTS.md` 13.412 → **15.948** ký tự · sáu mặt đồng bộ |
| 11 | Vá `K8` giống cách `J8` đã vá ở V10984 | Cổng vẫn 8/8, in thêm `đã đóng n/14` |
| 12 | Thêm khoá `xong` cho 3 mục vào `_v10981_lich.py`; mở rộng `_v10981_trang_lich.py` | §8.6 trước chỉ đọc `LICH9` nên 3 mục nhóm 14 **không hiện ở đâu** trong trang lịch |
| 13 | Sinh lại trang lịch | 38.138 byte · 247 dòng |
| 14 | Viết `_v10985_ghi_so.py`, chạy **chế độ xem trước** rồi mới `--that` | Guard chặn nhãn lạ trước khi ghi (bài học V10981b) |
| 15 | Ghi `QD-025` vào sổ quyết định | **Vấp** — guard tự chặn, xem §3.3 |
| 16 | Chạy **5 cổng, mỗi cổng một lệnh riêng** | Tất cả đạt — xem §4 |
| 17 | Viết báo cáo công khai + đẩy hai repo | — |

---

## 3. Vấp ở đâu

### 3.1 `K8` chặn oan mục LÀM XONG — bắt được TRƯỚC khi ghi sổ

Đọc `_v10981_kiem_lich.py` trước khi sửa sổ thì thấy `K8` chỉ soi `TREO_STATUSES`. Nghĩa là đóng
ba mục bằng nhãn **hợp lệ** (`CLOSED_PASS`/`CLOSED_REPORT`) sẽ làm chúng bị đếm là **MỒ CÔI** và
cổng TRƯỢT — **càng làm đúng lịch thì cổng càng đỏ**.

Trái với chính chú thích ngay trên phép đó (*"ngoài `TREO_STATUSES` **và ngoài `DONG_STATUSES`**"*)
và trái `trang_thai_mo_coi()`. Và đây là **cùng một lỗi** mà `J8` đã vá ở **V10984** (vấp thật:
`FU-244` làm xong sớm) — bản `K8` bị bỏ sót.

**Hậu quả nếu bỏ qua:** phiên sau thấy cổng đỏ sẽ có phản xạ **mở lại nhãn cho cổng xanh**, tức
đảo ngược việc đã làm đúng để làm vừa lòng một cổng sai.

**Bài học ghi lại:** *vá một cổng thì phải soi cổng song sinh trong cùng phiên.*

### 3.2 Mô tả cũ của `FU-191` sai 3 chỗ — nếu khoá y nguyên là khoá cả cái sai

`FU-191` chỉ yêu cầu *"viết luật vào 5 mặt quy tắc"*. Nhưng đọc `combo_super.py` thì:

| Mô tả cũ (01/08) | Code 04/08 |
|---|---|
| *"top-3 từ pool 4 ML **và** top-2 từ pool 7 AI"* | **DUAL POOL V5.9.6 đã bị bỏ** — code ghi thẳng `Replaces V5.9.6 DUAL POOL`. Thật là **UNIFIED TOP-3 (V6.0)**: 13 ứng viên gộp MỘT bảng, top-3 toàn bảng + bảo đảm ≥1 ML và ≥1 AI |
| *"cắt an toàn `gpt-5.4` + `gpt-5-mini`, pool AI còn 5"* | Hai model đó **đã rời pool từ 01/08** (V10931). Pool AI hiện **9** |
| *"pool ML ≥ 4 **vì chọn 3**"* | Cơ chế chỉ cần **≥1 ML**. Ngưỡng 4 giữ nguyên nhưng **lý do phải sửa** |

Đã chọn: khoá luật với nội dung **đã sửa theo code**, thêm mục *"số đã cũ, đừng trích lại"*, và
giữ đúng con số sàn owner đã ký (ML ≥ 4 · AI ≥ 3) nhưng ghi lại lý do thật.

### 3.3 Vấp do chính agent gây ra — so ký tự với byte

Bộ ghi `QD-025` có guard *"từ chối nếu file ngắn đi"*. Guard đó so `len(chuỗi)` (**ký tự**) với
`st_size` (**byte**). Tiếng Việt là nhiều byte một ký tự, nên bản mới **dài hơn thật** vẫn bị báo:

```
✗ kết quả không dài hơn bản cũ — TỪ CHỐI GHI
```

Đã sửa thành so **byte với byte** (`len(moi.encode("utf-8"))`), rồi ghi được: 93.571 → **99.584**
byte, 26 → **27** quyết định. Guard chặn oan còn hơn guard không chặn, nhưng nếu không đọc kỹ thì
rất dễ kết luận sai là *"file không cần sửa"*.

### 3.4 Regex bắt giả thuyết của `FU-212` sai lần đầu

Bộ thu bằng chứng đầu tiên tìm `GT-1`…`GT-5` trong artifact → **không thấy gì**, suýt kết luận
*"thiếu bằng chứng"*. Thực tế artifact đặt khoá **`gt1`…`gt5`** (chữ thường, không gạch ngang).
Sửa lại thành đọc **khoá JSON** thay vì dò chuỗi, và kiểm thêm rằng **kết luận từng giả thuyết có
mặt trong sổ theo dõi** chứ không chỉ trong JSON. **Bài học:** dò chuỗi trong JSON là đoán; đọc
khoá là biết.

### 3.5 Trang lịch là **máy sinh**, suýt sửa tay

`docs/LICH_CUON_CHIEU_DEN_10082026.md` có dòng đầu ghi *"Trang này do máy sinh … **đừng sửa
tay**"*. Đã dừng lại, đi sửa **nguồn** (`_v10981_lich.py` + `_v10981_trang_lich.py`) rồi sinh
lại. Nếu sửa tay thì lần sinh sau sẽ **xoá sạch** phần vừa viết.

### 3.6 `git fetch` của repo công khai chết — và nó làm **chính cổng báo cáo** xanh giả

Lúc push báo cáo:

```
fatal: bad object refs/desktop.ini
error: github.com:irissnss/Lottery_AI_Notion_Reports.git did not send all necessary objects
```

**5 tệp `desktop.ini`** của **Google Drive** (ẩn+hệ thống, 106 byte, nội dung
`[.ShellClassInfo] IconResource=…\GoogleDriveFS.exe,27`) nằm trong `.git/refs/`,
`.git/refs/heads/`, `.git/refs/remotes/`, `.git/refs/remotes/origin/`, `.git/refs/tags/`. Git đọc
**mọi tệp** trong `refs/` như con trỏ commit → gãy.

**Chỗ đáng sợ:** `fetch` chết thì `origin/main` đứng đông, mà `_v10921_report_gate.py` kiểm *"đã
push chưa"* bằng `git log origin/main..HEAD`. Con trỏ cũ ⇒ cổng có thể báo *"commit chưa push:
KHÔNG"* trong khi báo cáo **chưa lên remote**. Thấy tận mắt: đếm ra *"remote 0 ahead"* nhưng
`git push` bị **từ chối non-fast-forward**; con trỏ cũ ở `c20b53d` còn remote đã ở `255b718`.

Xử: xoá 5 tệp ini (kiểm nội dung từng tệp trước khi xoá, còn đúng 3 ref thật) → fetch sống lại →
`stash` 4 tệp `desktop.ini` đang sửa dở **của phiên khác** → `pull --rebase` → push `77d337a` →
`stash pop` trả lại nguyên trạng. **Không đụng ref thật, không rewrite lịch sử, không commit hộ
việc của người khác.** Đã mở **`FU-266`** vì Google Drive sẽ đẻ lại.

### 3.7 Chỗ chưa hoàn hảo — nói thẳng, không che

Sổ điểm danh của hook chỉ có **2 lượt** vì nó mới sinh sáng 04/08, và Cursor bắn `sessionStart`
**một lần mỗi phiên** chứ không mỗi tin nhắn — V10981→V10985 nối nhau trong cùng một phiên Cursor
nên chỉ một lượt hook. Cả 2 lượt **đều đi hết hàm**, nên tiêu chí của `FU-187` đạt. Nhưng tiêu chí
riêng của `FU-245` (*"xác nhận bằng sổ điểm danh sau 2 phiên"*) **chưa** coi là đạt vì hai lượt
nằm **cùng một phiên** — để đúng phiên 06/08 của nó xác nhận, **không đóng hộ**.

---

## 4. Cổng kiểm — chạy tách riêng từng lệnh

Chạy gộp nhiều cổng vào một lệnh thì phiên trước bị cắt mất kết quả, nên phiên này mỗi cổng một
lệnh:

| Lệnh | Kết quả |
|---|---|
| `python web/backend/_v10920_decision_ledger.py` | **0 TRÔI** · 27 quyết định · `QD-025` **11/11** |
| `python web/backend/_v10981_kiem_lich.py` | **ĐẠT 8/8** · `K8` in *đã đóng 3/14 (FU-187, FU-191, FU-212)* |
| `python web/backend/_v10982_kiem_lich9.py` | **ĐẠT 8/8** · `J5` mốc tải khớp sổ thật **7/7 ngày** |
| `python web/backend/_v10925_rule_sync_check.py --check` | **ĐẠT** · sáu mặt đồng bộ · `AGENTS.md` khớp bản sinh |
| `python web/backend/_v10920_session_start.py` | đến hạn hôm nay **3 → 0** · treo **99 → 97** · mồ côi **18 → 18** |

---

## 5. Việc KHÔNG làm — và vì sao

| Không làm | Vì sao |
|---|---|
| Cắt / dừng bất kỳ model nào | `FU-191` là mục **tài liệu**; `QD-014` cấm tới hết 08/08. Pool giữ đúng **4 ML + 9 AI = 13** |
| Sửa nhánh `UNIFIED TOP-3` dù đã thấy sàn 5 lượt không được áp | Là **đổi bộ lọc combo-super** — `QD-014` cấm. Và bằng chứng là **đọc code**, chưa đo tác động → mở `FU-265` kèm ngưỡng ≥3 ô |
| Xếp `FU-265` vào cửa sổ 04→10/08 | Ngày chốt 10/08 đang **đúng trần 3 mục**; thêm một mục là phá trần và làm `J5` trượt. Xếp **12/08** |
| Deploy · restart `lottery` · sửa cron · đụng DB | Không cần — phiên thuần tài liệu. Vì vậy **không có bước so hash 4 bảng khoá**: không có lượt ghi nào để so |
| Đóng hộ `FU-245` | Tiêu chí của nó cần 2 **phiên khác nhau**; hiện 2 lượt cùng một phiên |
| Sửa tiêu đề / mã đọc lệch của `FU-245` | Mục đó có hạn riêng 06/08; sửa tiêu đề mục khác là lấn phạm vi. Đã ghi lại để 06/08 dọn |
| Đóng 4 checkpoint roadmap cũ quá hạn (CP-X.1 · CP-2.2 · CP-4.0 · CP-R4) | Không thuộc tiêu chí ba mục hôm nay |
| Ghi bất cứ gì vào Notion | **§57 cấm mọi thao tác ghi** — Notion chỉ đọc |

---

## 6. Kết cục ba mục

| Mã máy | Nhãn mới | Số chốt |
|---|---|---|
| `FU-187` | **`CLOSED_PASS`** | điểm danh **2/2/2** ba pha · **0** lượt treo `stdin` · briefing **13,1 giờ** · **6/6** mục có số · exit **0** |
| `FU-191` | **`CLOSED_PASS`** | **§59 (A57)** ở **5/5** mặt · sync exit **0** · pool vẫn **4 ML + 9 AI = 13** |
| `FU-212` | **`CLOSED_REPORT`** | **5/5** khoá `gt1`…`gt5` · **5/5** kết luận trong sổ · **7,59pp** · báo cáo V10955 **4 file** |
| `FU-265` | `MEASURED_ROOT_CAUSE_FOUND` (mới) | hạn **12/08** · ngưỡng **≥3 ô** thì sửa, **0–2 ô** thì đóng kèm số |
| `FU-266` | `MEASURED_ROOT_CAUSE_FOUND` (mới) | hạn **12/08** · đã xoá 5 tệp `desktop.ini` khỏi `.git/refs`, fetch sống lại, push `77d337a`. Còn lại: cho cổng báo cáo **TRƯỢT khi fetch thất bại** |

> **Suýt vấp lần nữa ngay ở bước này:** thoạt đầu định gán `FU-266` nhãn
> `FIXED_PENDING_LIVE_VERIFY`. Nhãn đó **KHÔNG nằm trong** `TREO_STATUSES` — dùng là mục rơi khỏi
> mọi bộ đếm và **tổng mồ côi 18 → 19**, đúng cái bẫy V10981b đã làm mất 11/14 mục. Tra danh sách
> nhãn hợp lệ **trước khi ghi** nên bắt được. Đã đổi sang `MEASURED_ROOT_CAUSE_FOUND` (hợp lệ, và
> đúng bản chất: căn nguyên đã rõ, vá bền chưa làm).
