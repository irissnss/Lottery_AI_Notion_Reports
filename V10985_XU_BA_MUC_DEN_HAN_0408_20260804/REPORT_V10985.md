# V10985 — Xử ba mục đến hạn 04/08: nghiệm thu hook · khoá §59 luật cắt model · đóng phần đo MT

| | |
|---|---|
| **Phiên bản** | V10985 |
| **Ngày** | 2026-08-04 (giờ Việt Nam) |
| **Loại việc** | tài liệu + quản trị + vá một phép cổng · **KHÔNG deploy, KHÔNG restart `lottery`** |
| **Quyết định owner** | `QD-025` (mới) · trong khuôn `QD-021` lịch cuốn chiếu |
| **Mục xử** | `FU-187` · `FU-191` · `FU-212` (toàn bộ tải ngày 04/08 của nhóm 14) |
| **Mục mở mới** | `FU-265` · `DO1208` · hạn 12/08 |
| **Đóng băng** | `QD-014` còn hiệu lực hết 08/08 — **không cắt model nào**, không đổi hằng số combo-super |

---

## 1. Tóm tắt một đoạn

Ba mục đến hạn hôm nay **đóng hết, đúng hạn, không mục nào phải đổi hạn**: `FU-187` nghiệm thu
hook đầu phiên → `CLOSED_PASS` (sổ điểm danh **6 dòng** chia đều ba pha `VAO_HOOK`/
`DA_GHI_BRIEFING`/`XONG` = **2/2/2**, nghĩa là hook đi hết hàm cả hai lượt và **0 lượt treo ở
`sys.stdin.read()`**; briefing mốc **13,1 giờ** trước, **6/6** mục in ra số; bộ kiểm exit **0**).
`FU-191` khoá luật cắt model an toàn thành **§59 (A57)** ở **5/5** mặt quy tắc → `CLOSED_PASS`,
**không cắt model nào** — pool vẫn **4 ML + 9 AI = 13**. `FU-212` đóng phần **ĐO** →
`CLOSED_REPORT` (artifact **11.309** ký tự đủ **5/5** khoá `gt1`…`gt5`, **5/5** kết luận trong
sổ, chênh RF→công bố **7,59pp**), phần hành động ở `FU-216` hạn 09/08. Hai việc phát sinh phải
làm luôn: **vá phép `K8`** vì nó chặn oan mục làm xong (càng đúng lịch cổng càng đỏ), và **sửa
hai con số SAI trong chính mô tả cũ của FU-191** trước khi khoá — nếu khoá y nguyên là khoá cả
cái sai vào năm mặt quy tắc. Năm cổng kiểm đều đạt; **mục mồ côi 18 → 18, không tăng**.

---

## 2. Owner yêu cầu gì — nguyên văn

> **04/08 ~22:4x** (giờ VN): *"xử luôn tối nay"* — ba mục đến hạn hôm nay 04/08, để không trễ hạn.

Nhắc gốc của `FU-191`, owner nói **lần thứ hai**:

> *"cắt model ảnh hưởng đến combo super mới quan trọng cận thận chỗ này"*

Nền của lịch, owner ký **04/08 10:29**:

> *"Giãn ra cuốn chiếu tới hết ngày 10/08 phải hoàn thành, làm lần lượt những vấn đề nào xác
> thực rõ ràng , đơn giản làm trước tới cuối cùng 10/08 phải xong"*

Và **04/08 21:35**:

> *"anh cần một kế hoạch triển khai sơm hơn dự kiến em xem thử dùm anh có triển khai được gì
> trước không em ?"*

---

## 3. Đào bới / phát hiện

### 3.1 Đo bằng cách nào

Viết một bộ thu bằng chứng chỉ-đọc `web/backend/_v10985_bang_chung.py`. Lý do phải viết riêng:
`artifacts/` và `*.log` nằm trong `.cursorignore` nên công cụ đọc tệp **không mở được**
`docs/_HOOK_DIEM_DANH.log` lẫn `artifacts/v10955_tin_hieu_roi_rung.json` — hai thứ chính là bằng
chứng của FU-187 và FU-212. Kết quả ghi ra `evidence/v10985_bang_chung_ba_muc.json`.

### 3.2 FU-187 — hook có chạy thật không

| Tiêu chí đã ký (V10981b) | Đo được | Kết |
|---|---|---|
| `_v10920_session_start.py` exit 0 | exit **0** | ĐẠT |
| `docs/_BRIEFING_DAU_PHIEN.txt` có mốc trong 24 giờ | mốc **2026-08-04 10:06:01** = **13,1 giờ** trước | ĐẠT |
| 6/6 mục briefing in ra số | **6/6** (`[1]`…`[6]`, kèm cả `[3b]`) | ĐẠT |

Thêm một phép **không có trong tiêu chí nhưng là câu hỏi thật**: hook *chạy thật* hay chỉ là
agent gọi tay? Đây đúng chỗ V10980 dựng **sổ điểm danh** để phân biệt *"Cursor không gọi hook"*
với *"hook bị gọi nhưng treo"*.

`docs/_HOOK_DIEM_DANH.log` — **6 dòng**: `VAO_HOOK` **2** · `DA_GHI_BRIEFING` **2** · `XONG` **2**.
Ba pha **bằng nhau** nghĩa là hook đi hết `main()` cả hai lượt, **0 lượt treo ở
`sys.stdin.read()`** — đúng cái bẫy làm hook im 02/08→04/08 (`FU-245`). `.cursor/hooks.json` vẫn
khai `sessionStart` → `python .cursor/hooks/session_start_briefing.py`, timeout 100s.

### 3.3 FU-191 — đọc code thì thấy mô tả cũ đã SAI

Mục này chỉ là *"viết luật vào 5 mặt quy tắc"*, nhưng đọc `combo_super.py` để viết cho đúng thì
phát hiện **ba chỗ trong chính mô tả cũ của FU-191 không còn đúng**:

| Mô tả cũ (ghi 01/08) | Đọc từ code 04/08 |
|---|---|
| *"top-3 từ pool 4 ML **và** top-2 từ pool 7 AI"* | Đó là **DUAL POOL V5.9.6 đã bị bỏ** — code ghi thẳng `Replaces V5.9.6 DUAL POOL`. Cơ chế thật là **UNIFIED TOP-3 (V6.0)** |
| *"cắt an toàn `gpt-5.4` + `gpt-5-mini`, pool AI còn 5"* | Hai model đó **đã rời pool từ 01/08** (V10931). Pool AI hiện là **9** |
| *"pool ML ≥ 4 **vì chọn 3**"* | Dưới UNIFIED TOP-3 cơ chế chỉ cần **≥1 ML**. Ngưỡng 4 vẫn giữ nhưng **lý do phải sửa** |

Cơ chế thật, đọc từ `run_combo_super()`:

| | |
|---|---|
| Ứng viên | **4 ML + 9 AI = 13**, gộp làm MỘT bảng xếp hạng |
| Thước chấm | tỉ lệ **bạch thủ** từ `model_daily_eval`, trộn hai cửa sổ `(2×7ngày + 30ngày)/3` |
| Sàn mẫu | `MIN_MAU_DU_TUYEN = 5` lượt thật trong 7 ngày mới được dự tuyển |
| Chọn | **top-3 toàn bảng** rồi **bảo đảm ≥1 ML và ≥1 AI** → thực tế 1–2 ML + 1–2 AI |
| Nhịp | tính lại **mỗi ngày, riêng từng miền** |
| Chi phí | **cả 4 ML luôn chạy** ở Phase 1 để theo dõi shadow; **chỉ model được chọn mới bị gọi API** |

Danh sách thật: ML = `meta-learning` `lstm` `xgboost` `random-forest`. AI =
`claude-sonnet-4-6` `gemini-2.5-flash` `claude-opus-4-6` `gemini-2.5-pro` `deepseek-reasoner`
`glm-5.1` `gpt-oss-120b` `gemini-3.5-flash` `gemini-3.6-flash`.

### 3.4 Phát hiện phụ — sàn 5 lượt thật không áp ở nhánh chọn thật (mở `FU-265`)

`MIN_MAU_DU_TUYEN = 5` **chỉ có hiệu lực trong `_chon_top()`** — hàm đó xếp nhóm `chua_du` xuống
cuối. Nhưng nhánh **thật sự chọn** của `run_combo_super()` là `UNIFIED TOP-3`: nó lấy `wr_dict`
(giá trị thứ 4 của `compute_adaptive_top_n`) rồi `sorted(...)[:3]`, mà `wr_dict` **gộp cả
`du_mau` LẪN `chua_du`**. Nghĩa là model chỉ có **1–4 lượt thật** vẫn có thể chiếm suất top-3
nếu điểm bạch thủ cao — đúng cái bẫy **điểm ảo** mà V10936 dựng sàn để chặn (đo 01/08 từng cho
thấy thả `gemini-3.6-flash` 0 lượt vào là nó cướp suất #1 ở MB).

**CHƯA đo tác động** — chưa biết đã thật sự xảy ra lần nào chưa. Không kết luận sớm.

### 3.5 FU-212 — kiểm lại bằng chứng, không tin báo cáo cũ

| Phép | Số |
|---|---|
| `artifacts/v10955_tin_hieu_roi_rung.json` | **11.309** ký tự, đủ **5/5** khoá `gt1`…`gt5`, **khoá nào cũng có dữ liệu** |
| Kết luận từng giả thuyết ghi thành chữ trong sổ | **5/5** |
| Chênh RF → số công bố | **7,59pp** (nửa sau từ 06/05: RF **19,91%** +3,42pp z 1,34 → phiếu **15,17%** −1,32 → công bố **12,32%** −4,16) |
| Báo cáo công khai V10955 | tồn tại, **4 file** |

Năm kết luận: `gt1` **một phần** (RF/XGB top-1 kém đánh bừa; LSTM holdout top-1 21,4% +4,94pp
z 2,08) · `gt2` **bác bỏ** (bt = `main[0]` **368/368**) · `gt3` **xác nhận** (gộp phiếu loãng) ·
`gt4` xác nhận phụ (ghi đè mất thêm **~2,8pp**) · `gt5` AUC **0,55** lý thuyết đủ hoà vốn nhưng
thực tế chỉ LSTM holdout chuyển được.

### 3.6 Phát hiện phải sửa ngay — phép `K8` chặn oan mục LÀM XONG

Phép `K8` của `_v10981_kiem_lich.py` chỉ soi `TREO_STATUSES`, nên mục đóng bằng nhãn **hợp lệ**
(`CLOSED_PASS` / `CLOSED_REPORT`) bị đếm là **MỒ CÔI** và cổng TRƯỢT. Nghĩa là **càng làm đúng
lịch thì cổng càng đỏ** — đóng ba mục hôm nay là cổng đỏ ngay.

Trái với chính chú thích ngay trên nó (*"ngoài `TREO_STATUSES` **và ngoài `DONG_STATUSES`**"*) và
trái định nghĩa gốc trong `trang_thai_mo_coi()` (loại cả nhãn treo LẪN nhãn đóng). Đây là **cùng
một lỗi** mà `J8` của `_v10982_kiem_lich9.py` đã vá ở **V10984** (vấp thật: `FU-244`); bản `K8`
bị bỏ sót.

---

## 4. Hướng xử lý và vì sao chọn

### 4.1 FU-191 — ba phương án, chọn phương án 3

| Phương án | Nội dung | Vì sao chọn / loại |
|---|---|---|
| 1 | Khoá **y nguyên** mô tả cũ vào 5 mặt quy tắc | **LOẠI.** Là khoá cả ba con số sai vào năm mặt quy tắc — đúng thứ khó gỡ nhất về sau, vì mọi công cụ đều tự nạp năm mặt này |
| 2 | Hoãn tới khi đo lại được cơ chế trên dữ liệu sống | **LOẠI.** Mục đến hạn hôm nay; cơ chế đọc được thẳng trong code, không cần đo. Hoãn là trễ hạn không có lý do thật |
| 3 | **Khoá luật với nội dung đã sửa theo code, ghi rõ con số nào cũ** | **CHỌN.** Vẫn xong trong hạn, và luật khoá vào là luật ĐÚNG. Ghi thêm mục *"số đã cũ, đừng trích lại"* để lần sau không ai lôi lại pool 7 AI |

Sàn **ML ≥ 4 · AI ≥ 3** **giữ đúng con số owner đã ký** — không tự nới, không tự siết. Nhưng
**lý do được sửa**: không phải *"vì chọn 3"* (cơ chế chỉ cần ≥1 ML), mà vì **cả 4 ML đều chạy và
được đo mỗi ngày**, và ML là nguồn **duy nhất không tốn token**.

### 4.2 FU-265 — vì sao KHÔNG sửa luôn tối nay

Hai lý do thật, không phải né việc:

1. Sửa nhánh chọn của `combo_super` **chính là đổi bộ lọc combo-super** — `QD-014` cấm đích danh
   tới **hết 08/08**.
2. Bằng chứng là **đọc code**, chưa có ô nào chứng minh đã xảy ra. Luật playbook: bằng chứng chưa
   đủ thì **dựng phép đo kèm ngưỡng số**, không đụng production.

**Ngưỡng viết sẵn (không được nới):** đếm trên `model_daily_eval` 30 ngày, mỗi ô (miền × ngày)
xem có model vào top-3 unified với `n < 5` không. **≥3 ô** → sửa để nhánh unified dùng chung sàn
với `_chon_top`. **0–2 ô** → đóng mục kèm con số, ghi rõ chỉ là rủi ro lý thuyết.

**Vì sao hạn 12/08 mà không phải trong cửa sổ cuốn chiếu:** cố ý xếp **NGOÀI** 04→10/08. Ngày
chốt 10/08 đang **đúng trần 3 mục** mà owner yêu cầu giữ nhẹ — thêm một mục là phá trần và làm
phép `J5` trượt. Xếp 09/08 thì đẩy ngày nặng nhất từ 8 lên 9, xoá đúng cái cải thiện V10982b vừa
làm được.

### 4.3 `K8` — vá, không nới

Chọn **đúng cách `J8` đã vá ở V10984** để hai cổng không lệch nhau: nhận cả `DONG_STATUSES`, vẫn
chặn nhãn **không thuộc bộ nào** (nhãn tự chế kiểu `SCHEDULED` vẫn TRƯỢT). Không phải nới cổng —
là sửa cổng nói sai.

---

## 5. Đã làm gì

### 5.1 Bảng file × thay đổi

| File | Thay đổi | Loại |
|---|---|---|
| `CLAUDE.md` | thêm mục **§59 (A57)** — luật cắt model an toàn | quy tắc (nguồn) |
| `AGENTS.md` | **sinh lại** từ `CLAUDE.md`, 13.412 → 15.948 ký tự | quy tắc (máy sinh) |
| `.Antigravityrules.md` | thêm §59 | quy tắc |
| `.AGENT.md` | thêm §59 | quy tắc |
| `.cursorrules` | thêm §59 | quy tắc |
| `.antigravityrules` | bảng đánh số: thêm **§58** (ký 02/08, chưa ai ghi) và **§59** | quy tắc (trỏ đường) |
| `web/backend/_v10981_kiem_lich.py` | **vá `K8`** — nhận `DONG_STATUSES`, in thêm `đã đóng n/14` | cổng kiểm |
| `web/backend/_v10981_lich.py` | thêm khoá `xong` cho `FU-187` `FU-191` `FU-212` (hạn **giữ nguyên**) | nguồn lịch |
| `web/backend/_v10981_trang_lich.py` | §8.6 gộp cả nhóm 14 lẫn nhóm 9; thêm cột *Đúng hạn?* và *Nhãn mới* | máy sinh trang |
| `docs/LICH_CUON_CHIEU_DEN_10082026.md` | **sinh lại** (38.138 byte, 247 dòng) | tài liệu (máy sinh) |
| `docs/FOLLOW_UP_TRACKER.md` | prepend khối V10985: đóng 3 mục + mở `FU-265` (+11.158 ký tự) | sổ theo dõi |
| `CHANGELOG.md` | prepend khối V10985 (+4.616 ký tự) | changelog |
| `docs/CURRENT_TRUTH_SSOT.md` | prepend khối V10985 (+3.263 ký tự) | SSOT |
| `docs/OWNER_DECISION_LEDGER.json` | thêm **`QD-025`**, 26 → **27** quyết định (93.571 → 99.584 byte) | sổ quyết định |
| `docs/OWNER_DECISION_LEDGER.md` | máy sinh lại từ JSON | sổ quyết định (đọc) |
| `web/backend/_v10985_bang_chung.py` | **mới** — bộ thu bằng chứng chỉ-đọc | công cụ |
| `web/backend/_v10985_ghi_so.py` | **mới** — ghi sổ/CHANGELOG/SSOT qua `_doc_prepend` | công cụ |
| `web/backend/_v10985_ghi_quyet_dinh.py` | **mới** — ghi `QD-025` | công cụ |

### 5.2 Ba mục — nhãn trước → sau

| Mã máy | Mã đọc | Hạn | Nhãn trước | Nhãn sau |
|---|---|---|---|---|
| `FU-187` | `KS0804-1` | 04/08 | `DEPLOYED_PENDING_LIVE_VERIFY` | **`CLOSED_PASS`** |
| `FU-191` | `XH0804` | 04/08 | `MEASURED_BUT_NOT_FIXED` | **`CLOSED_PASS`** |
| `FU-212` | `DO0804` | 04/08 | `MEASURED_ROOT_CAUSE_FOUND` | **`CLOSED_REPORT`** |
| `FU-265` | `DO1208` | 12/08 | — (mới) | `MEASURED_ROOT_CAUSE_FOUND` |

**Hạn KHÔNG đổi mục nào** — cả ba đóng đúng ngày đã xếp, nên bảng mốc tải và sổ theo dõi không
lệch nhau (phép `K4` · `J5`).

### 5.3 Deploy · backup · hash

- **KHÔNG deploy. KHÔNG restart `lottery`. KHÔNG sửa cron. KHÔNG đụng DB.** Phiên này không có
  lượt ghi nào vào `predictions` · `final_bundles` · `lottery_results` · `model_daily_eval`, nên
  **không có bước so hash trước/sau** — không phải bỏ bước, mà là không có gì để so.
- **Backup:** không cần bản sao tay — mọi file đã sửa đều nằm trong git và mục *Gỡ về* dưới đây
  là một lệnh `git checkout`. Ba tài liệu quản trị ghi bằng `_doc_prepend.prepend()` (đọc xong
  mới ghi, **từ chối nếu file ngắn đi**, ghi tạm rồi đổi tên).
- `QD-014` **còn hiệu lực hết 08/08** và phiên này không phạm: **không cắt model nào**, roster
  official vẫn **15**, hằng số combo-super không đổi, `MIN_MAU_DU_TUYEN` vẫn **5**.

---

## 6. Cổng kiểm

Chạy **tách riêng từng lệnh** (gộp nhiều cổng vào một lệnh thì phiên trước bị cắt mất kết quả):

| Cổng | Lệnh | Kết quả |
|---|---|---|
| Sổ quyết định | `_v10920_decision_ledger.py` | **0 TRÔI** · 27/27 quyết định khớp · **`QD-025` khớp 11/11** |
| Lịch nhóm 14 | `_v10981_kiem_lich.py` | **ĐẠT 8/8** · `K8`: *14/14 nhãn hợp lệ · **đã đóng 3/14** (FU-187, FU-191, FU-212)* |
| Lịch nhóm 9 | `_v10982_kiem_lich9.py` | **ĐẠT 8/8** · `J5`: 10/08 = **3 mục** · **mốc tải khớp sổ thật 7/7 ngày** |
| Năm mặt quy tắc | `_v10925_rule_sync_check.py --check` | **ĐẠT** · sáu mặt đủ dấu hiệu · `AGENTS.md` khớp bản sinh · 4/4 `.mdc` tự nạp · 0 file chết |
| Briefing đầu phiên | `_v10920_session_start.py` | **ĐẾN HẠN HÔM NAY 3 → 0** · treo **99 → 97** · **mồ côi 18 → 18, KHÔNG tăng** |

Bằng chứng ba mục: `_v10985_bang_chung.py` → `FU-187` ĐẠT · `FU-191` ĐẠT · `FU-212` ĐẠT
(`evidence/v10985_bang_chung_ba_muc.json`).

Trong `QD-025`, phép chạy **trên VPS thật** đều khớp: `ML_MODELS.__len__() >= 4 and
AI_MODELS.__len__() >= 3` → **True** · `MIN_MAU_DU_TUYEN == 5` → **True**.

---

## 7. Vướng vấp

### 7.1 Cổng `K8` chặn oan mục làm xong — hậu quả nếu bỏ qua

Nếu không vá: đóng ba mục hôm nay làm cổng `_v10981_kiem_lich.py` **TRƯỢT**, và phản xạ tự nhiên
của phiên sau là **mở lại nhãn cho cổng xanh** — tức đảo ngược việc đã làm đúng để làm vừa lòng
một cổng sai. Đây đúng loại lỗi *"càng làm đúng thì cổng càng đỏ"*, tệ hơn cả không có cổng. Cùng
lỗi này `J8` đã vá ở **V10984** mà `K8` bị bỏ sót — **nghĩa là vá một cổng thì phải soi cổng
song sinh trong cùng phiên.**

### 7.2 Vấp do chính agent gây ra — so ký tự với byte

Bộ ghi `QD-025` tự chặn mình: guard so `len(chuỗi)` (ký tự) với `st_size` (byte). Tiếng Việt là
nhiều byte một ký tự nên bản mới **dài hơn thật** vẫn bị báo *"không dài hơn bản cũ"* và **từ
chối ghi**. Đã sửa thành so **byte với byte**. Guard chặn oan còn hơn guard không chặn, nhưng nếu
không đọc kỹ thì rất dễ kết luận sai là *"file không cần sửa"*.

### 7.3 Mô tả cũ của FU-191 sai — hậu quả nếu bỏ qua

Nếu khoá y nguyên: năm mặt quy tắc sẽ dạy mọi phiên sau rằng combo-super chọn *"top-3 từ 4 ML và
top-2 từ 7 AI"* và rằng *"cắt `gpt-5.4` + `gpt-5-mini` là an toàn"* — trong khi hai model đó **đã
rời pool từ 01/08**. Một đề xuất cắt dựa trên bảng đó sẽ nhắm vào model không còn tồn tại trong
pool, hoặc bỏ sót model đang thật sự bỏ phiếu. Đúng loại sai mà owner đã **suýt** duyệt một lần.

### 7.4 Chỗ chưa hoàn hảo của FU-187 — nói thẳng

Sổ điểm danh chỉ có **2 lượt** vì nó mới sinh sáng 04/08 cùng V10980, và Cursor bắn `sessionStart`
**một lần mỗi phiên** chứ không mỗi tin nhắn — các phiên V10981→V10985 nối nhau trong cùng một
phiên Cursor nên chỉ có một lượt hook. Đây là **hành vi đúng của công cụ**, không phải hook chết:
cả 2 lượt đều đi hết hàm. Muốn thêm mẫu thì phải **mở phiên Cursor mới**, không phải sửa code.
Vì vậy tiêu chí riêng của `FU-245` (*"xác nhận bằng sổ điểm danh sau 2 phiên"*) **chưa** coi là
đạt — để đúng phiên 06/08 của nó xác nhận, không đóng hộ.

### 7.5 Lệch nhãn cũ còn sót ở `FU-245` — ghi nhận, không tự sửa

Tiêu đề và mã đọc của `FU-245` còn ghi `hạn 04/08` / `SC0804`, nhưng ô dữ liệu mới nhất là
`hạn mới = 06/08`. Bộ đếm đọc **đúng 06/08** nên mục **không quá hạn** — lệch chỉ ở dòng hiển
thị. Không sửa trong phiên này vì `FU-245` có hạn riêng 06/08 và sửa tiêu đề của mục khác là lấn
phạm vi; đã ghi lại để phiên 06/08 dọn cùng lúc.

### 7.6 `git fetch` chết âm thầm — và nó làm **chính cổng báo cáo** xanh giả

Lúc push báo cáo, `git fetch` trong `E:\Lottery_AI_Notion_Reports` chết:

```
fatal: bad object refs/desktop.ini
error: ... did not send all necessary objects
```

Nguyên nhân: **5 tệp `desktop.ini`** của **Google Drive** (ẩn + hệ thống, 106 byte, nội dung
`[.ShellClassInfo] IconResource=…\GoogleDriveFS.exe,27`) nằm rải trong `.git/refs/`,
`.git/refs/heads/`, `.git/refs/remotes/`, `.git/refs/remotes/origin/`, `.git/refs/tags/`. Git đọc
**mọi tệp** trong `refs/` như một con trỏ commit, nên gặp tệp ini là gãy.

**Hậu quả nếu bỏ qua — đây mới là phần đáng sợ:** `fetch` chết thì `origin/main` **đứng đông**.
Cổng `_v10921_report_gate.py` kiểm *"đã push chưa"* bằng `git log origin/main..HEAD` — đọc một con
trỏ cũ thì cổng có thể báo **«commit chưa push: KHÔNG»** trong khi báo cáo **chưa hề lên remote**.
Tức cổng dựng ra để cưỡng chế A55 lại có thể **tự báo xanh cho một phiên chưa xong**.

Đo thật trong phiên: con trỏ cũ chỉ `c20b53d` còn remote đã ở `255b718`; lệnh đếm ra *"remote 0
ahead"* nhưng `git push` **bị từ chối non-fast-forward**. Đã xoá 5 tệp ini (còn đúng 3 ref thật:
`heads/main` · `remotes/origin/HEAD` · `remotes/origin/main`) → fetch sống lại, `pull --rebase`
xong, push được `77d337a`. **Không đụng ref thật, không rewrite lịch sử.**

Google Drive **sẽ đẻ lại** mấy tệp đó, nên đã mở **`FU-266`** thay vì coi là xong.

### 7.7 Việc KHÔNG làm, nêu rõ

- **Không cắt model nào** — `FU-191` là mục tài liệu, và `QD-014` cấm tới hết 08/08.
- **Không sửa nhánh `UNIFIED TOP-3`** dù đã thấy chỗ sàn 5 lượt không được áp → mở `FU-265`.
- **Không đóng hộ `FU-245`**, không đóng hộ 4 checkpoint roadmap cũ quá hạn (CP-X.1 · CP-2.2 ·
  CP-4.0 · CP-R4) — chúng không thuộc tiêu chí của ba mục hôm nay.

---

## 8. Gỡ về

Phiên này **thuần tài liệu + một phép cổng**, không có gì trên VPS phải gỡ. Mất khoảng **2 phút**:

```bash
cd E:/Lottery_AI_Test

# 1. Năm mặt quy tắc + file trỏ đường (bỏ §59)
git checkout HEAD -- CLAUDE.md AGENTS.md .cursorrules .AGENT.md \
                     .Antigravityrules.md .antigravityrules

# 2. Cổng kiểm + nguồn lịch + trang lịch máy sinh
git checkout HEAD -- web/backend/_v10981_kiem_lich.py \
                     web/backend/_v10981_lich.py \
                     web/backend/_v10981_trang_lich.py \
                     docs/LICH_CUON_CHIEU_DEN_10082026.md

# 3. Ba tài liệu quản trị (xoá khối V10985 ở đầu file)
git checkout HEAD -- docs/FOLLOW_UP_TRACKER.md CHANGELOG.md docs/CURRENT_TRUTH_SSOT.md

# 4. Sổ quyết định: bỏ QD-025 (hoặc đổi trang_thai -> SUPERSEDED)
git checkout HEAD -- docs/OWNER_DECISION_LEDGER.json docs/OWNER_DECISION_LEDGER.md

# 5. Kiểm lại
python web/backend/_v10925_rule_sync_check.py --check
python web/backend/_v10920_decision_ledger.py
```

Gỡ riêng từng phần cũng được — bốn nhóm trên độc lập nhau. Nếu chỉ muốn bỏ §59 mà giữ phần đóng
mục thì làm bước 1 rồi chạy lại `_v10925_rule_sync_check.py` để sinh lại `AGENTS.md`.

Ba mục muốn mở lại: đổi ô `status` trong khối V10985 của `docs/FOLLOW_UP_TRACKER.md` về nhãn cũ
(`DEPLOYED_PENDING_LIVE_VERIFY` · `MEASURED_BUT_NOT_FIXED` · `MEASURED_ROOT_CAUSE_FOUND`).

---

## 9. Theo dõi tiếp

| Mã máy | Mã đọc | Nhãn | Hạn | Ngưỡng hành động bằng số |
|---|---|---|---|---|
| **`FU-265`** | `DO1208` | Sàn 5 lượt thật không áp ở nhánh chọn thật | **12/08** | Đếm trên `model_daily_eval` 30 ngày, ô (miền × ngày) có model vào top-3 unified với `n < 5`: **≥3 ô** → sửa cho nhánh unified dùng chung sàn với `_chon_top`; **0–2 ô** → đóng kèm con số |
| **`FU-266`** | `DD1208` | `git fetch` chết vì `desktop.ini` trong `.git/refs` | **12/08** | Dựng lại tình huống fetch chết (đặt một tệp `desktop.ini` vào `.git/refs`) thì `_v10921_report_gate.py` phải **thoát ≠ 0** và in *"không fetch được"*; hiện thoát **0** ⇒ TRƯỢT. Và `desktop.ini` trong `.git/refs` phải đếm **0**. Trong lúc chờ: **mỗi phiên tự chạy `git fetch` và đọc kỹ output** trước khi tin cổng |
| `FU-245` | `SC0804` | Hook đầu phiên im 2 ngày | 06/08 | Sổ điểm danh có **≥2 lượt ở 2 PHIÊN CURSOR KHÁC NHAU**, mỗi lượt đủ ba pha. Hiện có 2 lượt nhưng **cùng một phiên** → chưa đạt. Dọn luôn tiêu đề/mã đọc còn ghi `04/08` |
| `FU-216` | `XH0809-1` | Shadow MT bạch thủ = random-forest đơn | 09/08 | Mang **phần hành động** của `FU-212` vừa đóng. Kết luận sớm nhất **15/08** (ngưỡng owner: 7 ngày, khớp live↔tái suy luận ≥95%) |
| `FU-215` | `DB0808` | Đóng băng `QD-014` hết hạn | 08/08 | 7/7 phép `kiem_code` của `QD-014` còn khớp, rồi owner chốt MỞ hay GIA HẠN. **`FU-265` phụ thuộc mốc này** |
| `QD-025` | `XH0804` | Luật §59 — hạn rà soát | **12/08** | 11/11 phép `kiem_code` phải còn khớp. Trượt phép nào = ai đó sửa quy tắc hoặc hạ sàn pool mà không ghi sổ |

**Không mục nào của phiên này bị đẩy hạn.** Tải ngày chốt **10/08 vẫn 3 mục**, ngày nặng nhất
**09/08 vẫn 8 mục** — `FU-265` cố ý xếp 12/08 để không phá hai con số đó.

**Việc còn treo chung, không thuộc phiên này:** `FU-225` quá hạn 03/08 (`DEPLOYED_PENDING_OWNER_VERIFY`,
chờ owner xác minh UI) · **18 mục mồ côi** nhãn chưa phân loại (không tăng trong phiên này, đã có
kiểm toán V10980 theo dõi).
