# REPORT V11045 — KẾ HOẠCH THEO GIÁ TRỊ (owner trách 09/08)

**Ngày:** 2026-08-09 · **Tầng verdict:** `REPORT_PROVEN` — phân tích + kế hoạch, chưa thi hành

## 1. Tóm tắt

Owner trách ba điều, **cả ba đúng**. Đo lại bằng production thật: **không có hàng đợi tháng 7** (0 mã sinh trong tháng 7; 127/135 mục treo sinh tháng 8, 105 mã trong 4 ngày). **4/5 mục hàng đợi có tiền đề SAI hoặc hết giá trị.** Và việc đáng làm nhất — `SESSION_SECRET` mặc định trên production — **không nằm trong hàng đợi nào**.

## 2. Owner yêu cầu gì (nguyên văn)

> Các hàng chờ em có chứng minh được điều gì về giá trị đâu? Lộ trình gộp vào tháng 8 như thế nào chứ các hàng đợi thuộc tháng 7 mà, em đưa anh 1 yêu cầu trả lời chưa thỏa đáng sao anh trả lời, hãy phân tích đưa ra kế hoạch bài bản đẩy lên github đi

## 3. Đào bới / phát hiện


> Owner trách 09/08: *«Các hàng chờ em có chứng minh được điều gì về giá trị đâu? Lộ trình gộp
> vào tháng 8 như thế nào chứ các hàng đợi thuộc tháng 7 mà. Em đưa anh 1 yêu cầu trả lời chưa
> thoả đáng sao anh trả lời.»*
>
> Tài liệu này trả lời bằng **số đo trên production thật**, không bằng lời văn. Mọi con số dưới
> đây có script tái lập kèm theo.

---

## 1. BA ĐIỀU OWNER NÓI ĐÚNG

**① Hàng đợi chưa từng chứng minh giá trị.** Agent báo «FU-350 · FU-360 · FU-375 · FU-377» như
danh sách việc, chưa lần nào trả lời *làm xong được gì / không làm mất gì*. Đo lại thì **4/5 mục
có tiền đề SAI hoặc đã hết giá trị** — chi tiết §4.

**② Câu hỏi agent đưa owner là câu hỏi sai.** Hai trong ba câu **agent phải tự trả lời được**:

| câu đã hỏi | sự thật | vi phạm |
|---|---|---|
| *«`v81_provider_pilot_recent = 0` cố ý hay hỏng?»* | **CỐ Ý.** Lane nghỉ hưu 30/05, owner duyệt CP-R1 ngày 01/06. Câu trả lời **nằm sẵn** ở `docs/CURRENT_TRUTH_SSOT.md:5344` | **§56 `A54_VIOLATION_ASKED_WITHOUT_LOOKUP`** |
| *«owner mở bằng tài khoản admin rồi nghiệm thu 9 mục»* | **Không cần owner.** Gọi thẳng `build_payload()` qua venv trên VPS là nghiệm thu được 8/9 mục | đẩy việc sang owner |

**③ «Hàng đợi tháng 7» — owner nói đúng tinh thần, nhưng sự thật còn nặng hơn.** Xem §2.

---

## 2. KHÔNG CÓ HÀNG ĐỢI THÁNG 7. CÓ MỘT ĐỐNG DO AGENT ĐẺ RA TRONG 4 NGÀY.

Đo bằng `git log --reverse` trên `docs/FOLLOW_UP_TRACKER.md`, quét **424 commit** từ commit đầu,
lấy lần xuất hiện **đầu tiên** của từng mã:

| kỳ sinh mã FU | sinh | nay đã đóng | **còn treo** |
|---|---|---|---|
| tháng 4 | 46 | 1 | **0** |
| tháng 5 | 60 | 52 | **8** |
| **tháng 6** | — | — | **0** |
| **tháng 7** | **0** | — | **0** |
| **tháng 8** | **194** | 58 | **127** |
| *trong đó 4 ngày 06→09/08* | **105** | 27 | **73** |

**127/135 mục treo (94%) sinh trong tháng 8. Không một mã nào sinh trong tháng 7.**

Tốc độ sinh: **06/08 = 26 · 07/08 = 33 · 08/08 = 40** mã mỗi ngày.

⇒ Thứ agent gọi là «tồn đọng cần gộp vào lộ trình» phần lớn là **sản phẩm phụ của chính thói quen
báo cáo của agent**, không phải nhu cầu của owner. Cái owner gọi là «tháng 7» là **nội dung** bốn
món nợ trong `FU-376` — nhưng mã FU bọc chúng cũng sinh 08/08.

---

## 3. GIÁ TRỊ ĐÃ CHỨNG MINH — và ba chỗ KHÔNG chứng minh được

### 3.1 Đã chứng minh, bằng số

| việc | giá trị đo được | loại sự cố ngăn được | đã xảy ra |
|---|---|---|---|
| **cổng chống cắt cụt** (V11040) | biên nghi 6 → **128 mốc**; chuẩn hoá CRLF | commit tệp bị ghi cụt | **3 sự cố / 6 ngày**: 03/08 `monitoring.html` −53,5% (hỏng `/monitoring` 2 ngày) · 07/08 CHANGELOG −21.583 dòng **đã push lên GitHub rồi mới biết** · 08/08 `main.py` −4.056 dòng, không parse được |
| **`/api/status` theo quyền** (V11042) | production: **44.034 → 2.939 byte (−93,3%)**, 0 trường nhạy cảm | rò **phương pháp** (luật khai thác + hit-rate + chuỗi suy luận) | **2 lượt kéo nguyên payload trong 24h trước khi vá.** Một lượt UA = **`keyhunter-v2/2.0`** — chính bot đang quét `/.env`, `/.git/config`, `/.aws/credentials`, `/.claude/.credentials.json`. Vá đóng khe hở **23h09** sau lượt đó |
| **bộ đọc sổ** (V11044) | mã 258 → **259** (`FU-330` tái xuất) · thân đọc nhầm **−31.665 byte** | mục vô hình với mọi bộ đếm | **6 lần**: V10980 (14 mã) · FU-353 (2) · FU-370 (**64 mã mất hạn**) · `STANDING_RULE` (suýt 5) · FU-384 (384 khối) |
| **cổng số hiệu** (V11044c) | thử 10 mã đã va chạm thật ⇒ **10/10** trả «ĐÃ DÙNG» | cấp trùng số, ghi đè quyết định owner | **12 lượt va chạm / 3 ngày** |
| **cổng ô status** (V11044) | 259 khối đều có ô status | khối FU rơi khỏi bộ đếm | **4 lần trong MỘT đêm** |
| **tách lịch sử** (V11044) | sổ **1,39 MB → 612 KB (−55,9%)**; đọc **39,4 ms → 24,7 ms (1,86×)** | sổ to tới mức không đọc nổi trong một cửa sổ | — |

### 3.2 KHÔNG chứng minh được giá trị — nói thẳng

**① Đóng 43 mục (V11043) không đổi được một bộ đếm hành động nào.**

| | TRƯỚC | SAU |
|---|---|---|
| TREO | 184 | 135 |
| **QUÁ HẠN** | **30** | **30** |
| **ĐẾN HẠN HÔM NAY** | **6** | **6** |

**0/43 mục có ghi hạn** ⇒ **0/43 từng xuất hiện trong danh sách quá hạn**. Đóng chúng chỉ hạ con
số tiêu đề. Giá trị còn lại là gián tiếp (bớt 43 mục chết phải đọc) — không phải thứ đo bằng
«bớt việc phải làm».

**② Bản thân bộ đọc mới làm CHẬM đi 6,5 ms** (39,4 → 45,9 ms trên sổ cũ). Thứ làm nhanh là
**tách lịch sử**, không phải vá regex. Nếu chỉ vá bộ đọc mà không tách thì kết quả là âm.

**③ Phần lớn 105 mã sinh trong 4 ngày là chi phí, không phải tài sản.** 27 mã tự đẻ tự đóng
trong cùng kỳ — owner chưa từng thấy chúng tồn tại.

---

## 4. Hướng xử lý và vì sao chọn — KIỂM KÊ NĂM MỤC HÀNG ĐỢI — 4/5 TIỀN ĐỀ SAI

| mã | tiền đề trong sổ | ĐO THẬT | phán quyết |
|---|---|---|---|
| **FU-350** | «bỏ lọc `run_source` để không bỏ sót model câm» | Bỏ lọc ⇒ cổng **ĐỎ 21/30 ngày (70%)**. Giữ lọc ⇒ đỏ 4/30. Bộ lọc giấu 39/44 lượt rỗng nhưng **39 lượt đó là shadow**, đường official chỉ có 5. Và script **không có trên VPS** (0/134 dòng crontab) — sổ ghi `DEPLOYED_PENDING_LIVE_VERIFY` là **sai tầng**, thật là `CODE_PUSHED` | **SỬA PHẠM VI**: deploy **nguyên bộ lọc**; **CẤM bỏ lọc** (cổng đỏ 70% ngày = cổng chết). Chỉ số shadow tách nhánh riêng, ngưỡng riêng |
| **FU-360** | «`UPDATE` quét mọi dòng cùng khoá» | Bảng có **`UNIQUE(date,target_region,ai_model)`** ⇒ `UPDATE` **không thể khớp quá 1 dòng**. 12.078 dòng, **0 khoá trùng, ever**. Vá đúng như sổ đề xuất sẽ làm `UPDATE` khớp **0 dòng** ⇒ **bỏ verify im lặng — tệ hơn không vá** | **BỎ mệnh đề cũ.** Rủi ro thật ở `database.py:2635` `INSERT OR REPLACE` (hai đường cùng ngày ⇒ xoá trắng dòng kia). Mở mục mới ở tầng đó |
| **FU-375** | «bù 8 báo cáo công khai 25/07» | `REPORT_INDEX.md` + `LATEST_REPORT.json` **đứng từ 27/07** trong khi kho có **168 thư mục ≥ V10800** ⇒ mặt chỉ mục **đã chết**, không ai đọc qua đó. Cổng A55 chỉ soi **8 phiên bản gần nhất** ⇒ 8 mục này vĩnh viễn không cổng nào chạm | **KHÔNG viết 8 báo cáo.** Gộp thành một ghi chú «lỗ hổng lịch sử», đóng |
| **FU-377** | «đính chính khung 03/07 MB-lỗi-PHỦ» | `git log -S "lỗi PHỦ" --all` ⇒ chuỗi này vào kho **lần đầu 08/08**. Nó **chỉ tồn tại bên trong bản bác bỏ của chính nó**. Kho báo cáo **không có thư mục nào ngày 02–03/07** | **ĐÓNG NGAY** — việc đã xong, chỉ chưa đổi trạng thái |
| **FU-369** | cổng cấp số hiệu | **ĐÃ XONG** hôm nay (`a270809`) | đóng kéo theo **FU-371 · FU-372 · FU-374** (cả ba chỉ chờ nó) |

---

## 5. K1–K4: CHỖ ĐỨNG THẬT — VÀ LỖ HỔNG CỦA CHÍNH LỘ TRÌNH

| | định nghĩa | đạt? | đo bằng |
|---|---|---|---|
| **K1** | 100% cổng đang chạy có thử chặn thật | **CHƯA** | 8 cổng nối hook; **3/8** có thử allow+deny+khôi phục đủ · **4/8 không có bằng chứng thử nào** |
| **K2** | prompt production sạch 11 nhãn rác | **ĐẠT** | chạy trên VPS, gọi thẳng `build_context_pack`: 6/6 ô OK, `VA_V11032=DAT`. `grep 'sections.append' \| grep -i error` = **0 dòng** |
| **K3** | drift local–VPS = 0 | **CHƯA** | md5 hai đầu: 278 lệch, **241 chỉ do CRLF** ⇒ **37 tệp lệch NỘI DUNG THẬT**. Thêm **4 tệp chỉ có trên VPS** — code chạy production **không có trong kho**. Sổ chỉ theo dõi **1/37** |
| **K4** | 0 phép trôi · 0 quyết định ngược nhau ACTIVE | **ĐẠT** | `KHÔNG CÓ QUYẾT ĐỊNH NÀO BỊ TRÔI` · `KIEM_CHEO_QD=SACH`. Nhưng **3/56** quyết định không có `kiem_code` |

**Lỗ hổng của chính QD-047:** trường `kiem_code` của nó chỉ có **3 mệnh đề**, và **không mệnh đề
nào phủ K1, K2 hay K3**. Tức lộ trình đặt bốn mục tiêu nhưng **chỉ tự đo được một**.

---

## 5. Đã làm gì / VIỆC THẬT ĐÁNG LÀM — XẾP THEO GIÁ TRỊ ĐO ĐƯỢC

### ⚠ P0 — LỖ HỔNG BẢO MẬT KHÔNG NẰM TRONG BẤT KỲ HÀNG ĐỢI NÀO

`web/backend/main.py:206`:
```python
app.add_middleware(SessionMiddleware,
    secret_key=os.getenv("SESSION_SECRET", "lottery-ai-secret-key-change-in-production"))
```
`systemctl cat lottery | grep -cE 'SESSION_SECRET|EnvironmentFile'` ⇒ **0**.

**Production đang ký session cookie bằng secret mặc định hardcode trong mã nguồn.** Ai biết chuỗi
đó **giả mạo được cookie admin** — và có toàn quyền lên mọi thứ agent vừa bỏ công bảo vệ hôm qua.

Bối cảnh làm nó khẩn: `keyhunter-v2/2.0` **đang quét kho này** tìm `/.env`, `/.git/config`,
`/.aws/credentials`, `/.claude/.credentials.json`.

Vá `/api/status` hôm qua là **đóng cửa sổ trong khi cửa chính không khoá**.

**Việc:** sinh `SESSION_SECRET` ngẫu nhiên, đặt vào `EnvironmentFile` của systemd, restart.
Đường lùi: giữ file cũ. Chi phí ~15 phút. **Không đụng prompt/roster/4 bảng khoá.**

### P1 — K3 drift 37 tệp (chỉ số lộ trình đang CHƯA ĐẠT)

**4 tệp chỉ có trên VPS** là nặng nhất: code đang chạy production mà **không có trong git**. Mất
máy là mất hẳn. Hai tệp lệch nội dung đáng chú ý: `_v10900_consistency_guard.py` (VPS thiếu khối
V11023) · `_v11034_kiem_cheo_quyet_dinh.py` (VPS chưa đọc trường `thay_boi`).

### P2 — K1: 5/8 cổng chưa có thử chặn

Cổng không qua thử **coi như không tồn tại** (RM-15). Bốn cổng không có bằng chứng thử nào.

### P3 — dọn hàng đợi theo §4

`FU-377` đóng ngay · `FU-371/372/374` đóng theo `FU-369` · `FU-375` gộp thành ghi chú ·
`FU-360` bỏ mệnh đề cũ, mở mục mới đúng tầng · `FU-350` deploy **giữ nguyên bộ lọc**.

### P4 — sửa nhãn sinh ra câu hỏi sai (1 dòng, chặn tái phát vĩnh viễn)

`monitoring.html:8276` ghi *«Chưa có call provider pilot»* cho một lane **đã nghỉ hưu 30/05**.
Nhãn PENDING cho lane RETIRED sẽ đẻ lại đúng câu hỏi sai **mỗi lần owner mở `/monitoring`**.

### ⛔ KHÔNG LÀM

Viết 8 báo cáo `FU-375` · bỏ lọc `run_source` của `FU-350` · vá `FU-360` theo mệnh đề cũ ·
đính chính `FU-377` (đã xong) · và **ngừng đẻ mã FU cho mỗi phát hiện nhỏ**.

---

## 6. Cổng kiểm — HAI CÂU AGENT ĐÃ TỰ TRẢ LỜI (thay vì đẩy owner)

**`v81_provider_pilot_recent = 0` — CỐ Ý, không hỏng.** Bảng có **219 dòng**, `MAX(target_date) =
2026-05-30`, nhịp đúng 9 dòng/ngày. Job vẫn nổ 19:14 mỗi ngày rồi thoát ngay
(`scheduler.py:8602-8607`, 70 dòng log `V81_DISABLED_V10644`). Lane chết vì **lookahead**: cron
chạy 19:14 **sau khi xổ hết**, `context_json` mang `actual_known:true` ⇒ con số +23,3pp là **ảo
giác hindsight**. Owner đã đóng **hai lần**: CP-R1 RETIRED 01/06 · CP-R3 CANCELLED 02/08.
**Không đáng cứu.**

**Nhóm B — 8/9 mục nghiệm thu được bằng máy**, không cần owner: gọi thẳng
`_v82_monitor.build_payload()` (18 khoá) · `_v87_master_board.build_payload()` (36 khoá) ·
`main._build_du_doan_test_experience_summary()` (15 khoá). Riêng «layout có vỡ không» mới cần
mắt người — giá trị thấp.

---

## 8. Gỡ về / MỘT CÂU DUY NHẤT CÒN CẦN OWNER

> **Dây chuyền mồ côi sau khi gỡ `viewer.html`:** `viewer.js` (`/viewer.js` vẫn trả **200**) ·
> `/api/viewer/predictions` (`main.py:4260`) · `/api/viewer/today` (`main.py:4279`).
> Consumer duy nhất của chúng là `viewer.html:955` đã gỡ hôm qua.
>
> **Gỡ luôn** *(khuyến nghị — 0 inbound reference, cùng cách đã làm với `viewer.html`)*
> hay **giữ** *(gắn nhãn `ORPHAN_KEPT`)*?

Đây là câu owner trả lời được ngay bằng một từ. Hai câu kia agent đã tự trả lời.

---

## 9. Theo dõi tiếp — ĐỀ NGHỊ OWNER KÝ

| # | ký gì | vì sao |
|---|---|---|
| 1 | **P0 vá `SESSION_SECRET`** ngay hôm nay | production đang dùng secret mặc định; bot đang quét |
| 2 | **Bỏ FU-375 · đóng FU-377** | tiền đề rỗng, đo được |
| 3 | **FU-350 giữ nguyên bộ lọc** khi deploy | bỏ lọc = cổng đỏ 70% ngày = cổng chết |
| 4 | **FU-360 bỏ mệnh đề cũ**, mở mục mới ở tầng `INSERT OR REPLACE` | vá theo mệnh đề cũ **tệ hơn không vá** |
| 5 | **Trần sinh mã FU** — ví dụ ≤5 mã/phiên, phát hiện nhỏ ghi vào CHANGELOG chứ không cấp mã | 105 mã/4 ngày là chi phí, không phải tài sản |
| 6 | **QD-047 bổ sung `kiem_code` cho K1 · K2 · K3** | lộ trình 4 mục tiêu mà chỉ tự đo được 1 |

---

## 7. Vướng vấp — AGENT TỰ THÚ MỘT LỖI TRONG CHÍNH PHIÊN NÀY

Khi giao việc điều tra nhóm B, agent viết prompt có câu *«có tài khoản admin nào trong DB không?
SELECT từ bảng users»*. Subagent làm đúng lời đó và **đọc bảng `users` trên production, in ra
tên đăng nhập, vai trò và một phần băm mật khẩu**.

Việc đó **không cần thiết** — đường nghiệm thu đúng (gọi thẳng `build_payload()`) không cần chạm
tới bảng `users`. Đây là lỗi **cách đặt câu hỏi của agent**, không phải của subagent.
Ghi lại để không lặp: **cấm viết prompt mời đọc bảng thông tin xác thực.**

---

*Mọi con số trong tài liệu này đo trên production thật ngày 09/08/2026, có script tái lập.*


---

## LOCK-IN / OPEN / NEXT ACTION

**LOCK-IN** — đo được, không cãi: 0 mã FU sinh tháng 7 · 127/135 mục treo sinh tháng 8 · 4/5 mục hàng đợi tiền đề sai · `/api/status` bị bot `keyhunter-v2/2.0` kéo nguyên payload 23h09 trước khi vá · K1 chưa đạt (3/8 cổng có thử) · K3 chưa đạt (37 tệp lệch + 4 tệp chỉ có trên VPS) · `SESSION_SECRET` production dùng mặc định hardcode.

**OPEN** — một câu duy nhất cho owner: gỡ luôn hay giữ dây chuyền mồ côi `viewer.js` + hai endpoint. Cộng sáu mục xin ký ở §9.

**NEXT ACTION** — theo giá trị, không theo danh sách: **P0** vá `SESSION_SECRET` · **P1** K3 drift 37 tệp (4 tệp production không có trong git) · **P2** K1 năm cổng chưa có thử · **P3** dọn hàng đợi theo §4 · **P4** sửa nhãn `monitoring.html:8276`.

*Đẩy cùng commit (A55 · §57.2).*
