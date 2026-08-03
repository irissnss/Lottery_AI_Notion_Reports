# V10976 — Sửa 5 lỗi "xanh giả" ở tầng cổng tự kiểm (03/08/2026)

> **Loại phiên:** sửa cổng kiểm soát · **không** deploy · **không** đụng đường ra số
> **Freeze:** QD-014 còn hiệu lực tới hết 08/08 — phiên này không chạm 15 model official,
> combo-super filter, override toggle, `/du-doan` writer, `final_bundles` writer, bộ chọn model.
> **Backup:** `backups/v10976_pre/` (6 file `.pre`)

---

## 1. Tóm tắt một đoạn

Bugbot rà ra 5 lỗi nằm trong **chính các cổng tự kiểm** của dự án — tức là hệ có thể báo
**xanh giả**, và nhiều phiên qua đã báo owner *"gate PASS / ledger 0 TRÔI"* dựa trên các cổng
đó. Em đã sửa đủ 5 lỗi, kèm sửa thêm 2 điểm cùng loại phát hiện trong lúc làm, rồi **chạy lại
thật** bốn lệnh để lấy số thật. Kết quả: **số không xấu đi, nhưng độ tin của số thì tăng hẳn**.
Sổ quyết định trước 19 mục — 17 🟢 / 2 ⚪ / 0 TRÔI; sau 20 mục — 19 🟢 / 1 ⚪ / 0 TRÔI. Riêng
`OD-20260801-H` trước và sau đều hiện 🟢 5/5, **nhưng trước là xanh giả**: em chứng minh bằng
phép đo trực tiếp — bẻ `AGENTS.md` cho lệch thật rồi chạy cả hai bản trên cùng hoàn cảnh, **bản
cũ vẫn 🟢 5/5 và thoát 0**, bản mới **🔴 TRÔI 1/5 và thoát 2**. Cổng báo cáo công khai sau khi
sửa **thoát 1** và bắt ngay một vi phạm A55 đang tồn tại thật: **V10975 chưa có báo cáo công
khai** (cổng cũ in ✗ ra màn hình nhưng vẫn thoát 0 nên máy không chặn được). **Không deploy
VPS** vì cả bốn script không tồn tại trên VPS và không cron nào gọi chúng.

---

## 2. Owner yêu cầu gì (nguyên văn)

> *"sửa hết 5 lỗi ở tầng cổng tự kiểm, rồi chạy lại ledger/gate để xem SỐ THẬT."*

> *"Nếu số thật xấu hơn số cũ → BÁO THẬT, không che. Đây là điểm quan trọng nhất owner muốn
> biết."*

Ràng buộc owner đặt kèm:

- QD-014 đóng băng tới hết 08/08 — cấm đụng 15 model official, combo-super filter constants,
  override toggles, `/du-doan` writer, `final_bundles` writer, bộ chọn model production.
- Backup trước khi sửa từng file · Notion chỉ đọc · giờ Việt Nam · service tên `lottery`.
- Không ghi docs kiểu `open(p,"w")` — dùng `_doc_prepend.prepend()`.
- Có agent khác chạy song song (V10975) → không `git add -A`, chỉ stage đúng file của mình.

---

## 3. Đào bới / phát hiện

### 3.1 Xác nhận từng lỗi bằng dòng code thật (trước khi sửa)

| Mã | File · dòng | Dòng code thật | Hậu quả đo được |
|---|---|---|---|
| **L1** (HIGH) | `_v10920_decision_ledger.py` ~218 | `co = Path(k["file_ton_tai"]).exists()` — phép của `OD-20260801-H` khai là kiểm *"sáu mặt đồng bộ + file chết + .mdc tự nạp"* nhưng chỉ hỏi **file script có tồn tại không** | Ledger 🟢 5/5 kể cả khi quy tắc lệch thật — **đo trực tiếp, xem §3.2** |
| **L2** | `_v10920_decision_ledger.py` ~75 | `elif "trung_voi" in k: r["dat"] = None` | `OD-20260801-D` (trỏ tới `OD-20260801-A`) mãi ⚪ *"không kiểm máy"* dù A đã 🟢 6/6 |
| **L3** | `_v10920_session_start.py` ~189 | `print(f"\n[6] BA MẶT QUY TẮC")` + pathspec git chỉ gồm `.Antigravityrules.md .AGENT.md .cursorrules` | Sửa `CLAUDE.md` hay `AGENTS.md` **không cảnh báo gì**; `AGENTS.md` là bản **sinh từ** `CLAUDE.md` nên sửa tay nó thì trôi hoàn toàn im lặng |
| **L4** | `_v10921_report_gate.py` ~82 và cuối `main()` | `print(f"✗ không thấy repo…"); return` · `main()` không trả mã | In ✗ mà **luôn thoát 0** → hook/CI không chặn được vi phạm A55 |
| **L5** | `_v10920_decision_ledger.py` ~201 | `if "JSON_START" not in raw: print(raw[-2500:]); … return` | Probe hỏng thì giữ nguyên `OWNER_DECISION_LEDGER.md` cũ và thoát 0 → **owner mở file ra tưởng vừa kiểm tươi** |

### 3.2 Phép đo quyết định — chứng minh "xanh giả" bằng một lần chạy thật

Cách đo: làm cho `AGENTS.md` **lệch thật** khỏi bản sinh từ `CLAUDE.md` (thêm một dòng sửa tay),
rồi chạy **cả hai bản** sổ quyết định trên **đúng cùng một hoàn cảnh** (bản cũ đi kèm sổ JSON
cũ, bản mới đi kèm sổ JSON mới).

| | `OD-20260801-H` | mã thoát | kết luận |
|---|---|---|---|
| **Bản CŨ** (`backups/v10976_pre/*.pre`) | **🟢 khớp 5/5** | **0** | quy tắc đã lệch thật mà cổng vẫn báo xanh — **xanh giả** |
| **Bản MỚI** | **🔴 TRÔI 1/5** | **2** | bắt đúng, chỉ rõ `AGENTS.md lệch bản sinh từ CLAUDE.md` |

Bằng chứng: `evidence/KIEMAM_ledger_BAN_CU.txt` · `evidence/KIEMAM_ledger_BAN_MOI.txt`.

### 3.3 Hai lỗi cùng loại phát hiện thêm trong lúc làm

- `_v10925_rule_sync_check.py` gom file quy tắc **0 byte** vào danh sách `chet` rồi **chỉ in ra**,
  không tính là trượt — dòng kết luận vẫn ghi *"KHÔNG CÒN FILE CHẾT"*. Đã sửa: 0 byte = trượt.
- Chính bộ kiểm đó **tự ghi đè `AGENTS.md`** mỗi lần chạy. Nếu để sổ quyết định gọi nó ở chế độ
  mặc định thì **cổng tự sửa cái nó đang kiểm** → kiểm xong lúc nào cũng "đạt". Đã thêm chế độ
  `--check` chỉ đọc và bắt sổ quyết định gọi đúng chế độ đó.

### 3.4 Ai đang gọi ba script này (soi trước khi đổi mã thoát)

| Nơi gọi | Gọi script nào | Có đọc mã thoát không |
|---|---|---|
| `.cursor/hooks.json` → `sessionStart` | `session_start_briefing.py` | Hook đó chạy `_v10920_session_start.py`, **hứng stdout rồi luôn `return 0`** — không đọc mã thoát |
| `beforeShellExecution` / `afterShellExecution` | `governance_guard.py` / `deploy_automation_ledger.py` | Không gọi ba script này |
| cron VPS | — | **Không dòng nào** |
| script khác trong repo | chỉ **nhắc tên trong tài liệu/báo cáo** (`_v10921_governance.py`, `_v10973_build_report.py`, …) | Không `subprocess` |

→ Đổi mã thoát **không làm vỡ luồng nào**. Vẫn thêm cờ `--soft` cho chỗ chỉ muốn xem.

### 3.5 Bốn script có chạy trên VPS không

```
ls -la /root/Lottery_AI_Test/web/backend/_v10920_session_start.py … 
→ No such file or directory  (cả 4 file)
crontab -l | grep -E '10920|10921|10925|session_start|decision_ledger|report_gate|rule_sync'
→ không dòng nào
```

→ Đây là bộ kiểm **chạy ở máy local**. **Không deploy.**

---

## 4. Hướng xử lý và vì sao chọn

| Lỗi | Phương án đã cân nhắc | Chọn gì · vì sao |
|---|---|---|
| **L1** | (a) giữ `file_ton_tai`, thêm `file_chua` soi vài chuỗi trong file quy tắc — (b) **chạy thật script kiểm** | Chọn **(b)**. (a) vẫn là kiểm gián tiếp: chuỗi có mặt không có nghĩa là sáu mặt đồng bộ. Thêm kiểu kiểm `chay_lenh` chạy `_v10925_rule_sync_check.py --check`, bắt **mã thoát** và soi **dấu hiệu bắt buộc** `SÁU MẶT ĐỒNG BỘ` trong output. Script hỏng → `dat=False` (**TRÔI**), không phải `None`: hỏng cổng cũng là mất kiểm soát |
| **L1 phụ** | gọi script ở chế độ mặc định | Từ chối — chế độ mặc định **ghi đè `AGENTS.md`**. Thêm `--check` chỉ đọc |
| **L2** | (a) hai lượt phẳng — (b) **giải đệ quy có chống vòng lặp** | Chọn **(b)** vì chuỗi tham chiếu có thể dài hơn một bậc (A→B→C). Có `frozenset` chặn vòng lặp, mục trỏ tới ID không tồn tại thì báo **TRÔI** chứ không im lặng |
| **L3** | (a) chỉ đổi nhãn + thêm 2 file vào pathspec — (b) **thêm phép so nội dung `AGENTS.md` vs bản sinh từ `CLAUDE.md`** | Chọn **(b)**. (a) chỉ bắt được "có sửa hay chưa" theo git; `AGENTS.md` là bản sinh nên sửa tay xong commit luôn thì git sạch mà nội dung vẫn lệch |
| **L4** | (a) luôn exit 1 khi trượt — (b) **exit 1 khi trượt + exit 2 khi mất repo + cờ `--soft`** | Chọn **(b)**: phân biệt "đo được và trượt" với "không đo được", giống tinh thần L5 |
| **L5** | (a) chỉ exit khác 0 — (b) **exit khác 0 + đóng dấu lên bản `.md` + ghi mốc lần đo tươi cuối** | Chọn **(b)** theo đúng yêu cầu owner: không để số cũ giả danh số mới. Mốc lưu ở `docs/_LEDGER_TRANG_THAI.json`, dấu cảnh báo nằm ngay đầu `OWNER_DECISION_LEDGER.md` giữa hai mốc `<!-- LEDGER_TRANG_THAI_START/END -->` nên lần chạy sau tự thay, không chồng đống |

---

## 5. Đã làm gì

### 5.1 Bảng file × thay đổi

| File | Thay đổi | Backup |
|---|---|---|
| `web/backend/_v10920_decision_ledger.py` | **L1** thêm kiểu kiểm `chay_lenh` + hàm `chay_bo_kiem()` · **L2** thêm `giai_thua_huong()` (đệ quy, chống vòng lặp) · **L5** thêm `khong_do_duoc()`, `ghi_trang_thai()`, `danh_dau_khong_do_duoc()`, bọc `try` quanh SSH · mã thoát **0/1/2** · bản `.md` ghi qua file tạm rồi `os.replace` | `backups/v10976_pre/_v10920_decision_ledger.py.pre` |
| `web/backend/_v10920_session_start.py` | **L3** hằng `NAM_MAT` (5 mặt) · nhãn "BA MẶT" → **"NĂM MẶT QUY TẮC"** · liệt kê mặt nào chưa đụng · thêm phép `agents_lech()` | `…/_v10920_session_start.py.pre` |
| `web/backend/_v10921_report_gate.py` | **L4** `main()` trả mã · `raise SystemExit(main())` · exit **1** vi phạm / **2** mất repo · cờ `--soft` · in mã vi phạm A55 | `…/_v10921_report_gate.py.pre` |
| `web/backend/_v10925_rule_sync_check.py` | thêm `--check` (chỉ đọc) · tách `ban_sinh()` / `agents_lech()` để bộ khác gọi được · file quy tắc 0 byte tính là trượt · mã thoát **0/1** | `…/_v10925_rule_sync_check.py.pre` |
| `docs/OWNER_DECISION_LEDGER.json` | phép đầu của `OD-20260801-H`: `file_ton_tai` → `chay_lenh` + `phai_co` · thêm quyết định **OD-20260803-A** (SC0803) | `…/OWNER_DECISION_LEDGER.json.pre` |
| `CHANGELOG.md` · `docs/CURRENT_TRUTH_SSOT.md` · `docs/FOLLOW_UP_TRACKER.md` | prepend khối V10976 bằng `_doc_prepend.prepend()` | git |
| `docs/_LEDGER_TRANG_THAI.json` | **mới** — mốc lần đo tươi gần nhất | — |

Script phụ trợ của phiên: `_v10976_docs.py` (ghi hồ sơ), `_v10976_bang_chung.py` (thu bằng
chứng trước/sau + kiểm âm), `_v10976_baseline_ledger.py` (số nền), `_v10976_doi_chieu.py`
(đếm bằng máy), `_v10976_kiem_fu.py` (kiểm hai FU mới có được bộ đọc nhận không).

### 5.2 Deploy

**Không deploy.** Lý do đo được ở §3.5: bốn script không có trên VPS, không cron nào gọi.
Không chạm khung giờ cấm (05:00–06:30 và 15:30–18:15 VN) vì không có thao tác deploy nào.

### 5.3 Hash 4 bảng khoá

Không đụng. Phiên chỉ sửa script kiểm ở máy local + tài liệu; không script nào của phiên ghi
vào `predictions`, `final_bundles`, `lottery_results`, `model_daily_eval`. Sổ quyết định chỉ
**đọc** trên VPS (probe `importlib` + `crontab -l`).

---

## 6. Cổng kiểm

### 6.1 SỐ THẬT — chạy lại cả bốn lệnh, trước và sau

| Lệnh | TRƯỚC (bản cũ) | SAU (bản mới) | Đọc thế nào |
|---|---|---|---|
| `_v10925_rule_sync_check.py` | exit **0** · sáu mặt đủ dấu hiệu | exit **0** · sáu mặt đồng bộ **thật** | Trước không thể sai vì luôn thoát 0. Sau: kiểm âm bẻ `AGENTS.md` → exit **1** |
| `_v10920_decision_ledger.py` | exit **0** · **19** quyết định · **17 🟢 · 2 ⚪ · 0 TRÔI** | exit **0** · **20** quyết định · **19 🟢 · 1 ⚪ · 0 TRÔI** | +1 mục là `OD-20260803-A` ghi trong phiên (🟢 5/5). `OD-20260801-D` **⚪ → 🟢** (L2). ⚪ còn lại: `OD-20260801-C` — quyết định về cách làm việc, không có mệnh đề máy kiểm |
| `_v10920_session_start.py` | exit 0 · `[6] BA MẶT QUY TẮC` · 80 mục treo · 0 quá hạn | exit 0 · `[6] NĂM MẶT QUY TẮC` + `AGENTS.md khớp đúng bản sinh từ CLAUDE.md` · 80 mục treo · 0 quá hạn | Mục [6] nay soi thêm `CLAUDE.md` và `AGENTS.md` |
| `_v10921_report_gate.py` | exit **0** | exit **1** | **Cùng một trạng thái repo**: cả hai đều in `V10975 ✗ KHÔNG CÓ BÁO CÁO`, nhưng chỉ bản mới báo cho máy biết |

Bằng chứng: `evidence/TRUOC_*.txt` · `evidence/SAU_*.txt` · `evidence/DOI_CHIEU_truoc_sau.txt`.

### 6.2 Kiểm âm từng lỗi — cổng có thật sự bắt được không

| Lỗi | Cách bẻ | Kết quả bản mới | Kết quả bản cũ (đối chứng) |
|---|---|---|---|
| L1 | sửa tay `AGENTS.md` cho lệch bản sinh | ledger **🔴 TRÔI 1/5**, exit **2** | **🟢 khớp 5/5**, exit **0** |
| L2 | — (đo trực tiếp) | `OD-20260801-D` 🟢 1/1 · `thừa hưởng từ OD-20260801-A · OD-20260801-A khớp` | ⚪ không kiểm máy |
| L3 | sửa tay `AGENTS.md` | briefing: `⚠ CẦN NÊU VỚI OWNER NGAY…: 1/5 mặt quy tắc đang sửa dở · AGENTS.md lệch CLAUDE.md` | im lặng hoàn toàn |
| L4 | trạng thái repo thật (V10975 thiếu báo cáo) | exit **1** + in `A55_VIOLATION_REPORT_MISSING` | exit **0** |
| L5 | gọi thẳng nhánh probe hỏng | exit **1** · in `⛔ KHÔNG ĐO ĐƯỢC` · đóng dấu lên đầu `.md`: *"Mọi con số bên dưới là số CŨ, của lần đo tươi gần nhất 2026-08-03 09:03:54"* | chỉ in log rồi thoát 0, `.md` không có dấu gì |

Bằng chứng kiểm âm: `evidence/KIEMAM_ledger_BAN_CU.txt` · `evidence/KIEMAM_ledger_BAN_MOI.txt` ·
`evidence/TEST_am_L5_probe_hong.txt`.

### 6.3 Cổng phụ

- `python -m py_compile` cả 4 file: **đạt**.
- Hai mục FU mới có được `_v10958_fu_reader` nhận không: **có** — `FU-250` `KS0806`
  `MEASURED_BUT_NOT_FIXED` hạn 2026-08-06 · `FU-251` `BC0803` `WAIT_LIVE` hạn 2026-08-03. Ghi FU
  mà bộ đọc không thấy thì lại đúng loại lỗi im lặng phiên này đang sửa, nên phải kiểm.
- Sau khi prepend, ba tài liệu quản trị vẫn còn đủ khối **V10976 · V10975 · V10974** — không
  đè lên phần của agent chạy song song.
- `_v10921_report_gate.py V10976` sau khi push: xem §9.

---

## 7. Vướng vấp

| Vấp | Hậu quả nếu bỏ qua | Đã xử |
|---|---|---|
| **Bằng chứng đầu tiên không đọc được.** Hứng output bằng `*>` của PowerShell → file ra UTF-16 và chữ tiếng Việt **đã bị console bóp méo trước khi ghi** (`khớp` → `khß╗¢p`). Bộ đếm đọc ra **0** ở mọi ô | Báo cáo dẫn "bằng chứng" mà owner mở ra không đọc được — coi như không có bằng chứng | Viết `_v10976_bang_chung.py` hứng qua `subprocess` của Python (`encoding="utf-8"`), thu lại toàn bộ |
| **Tự dẫm vào bẫy đã ghi trong quy tắc:** dùng `python -c` in tiếng Việt → `UnicodeEncodeError: cp1252`. Đúng dòng đã có trong bảng "mẹo vận hành đã học được" | Mất thời gian, và là dấu hiệu đọc quy tắc mà không áp dụng | Chuyển sang script có `sys.stdout.reconfigure` |
| **`artifacts/` nằm trong `.cursorignore`** nên công cụ của em không đọc được file bằng chứng vừa ghi | Không tự kiểm được bằng chứng mình vừa tạo | Chép bằng chứng sang thẳng `evidence/` của repo báo cáo công khai rồi mới soi |
| **Suýt để cổng tự sửa thứ nó đang kiểm.** Bản đầu của L1 định gọi `_v10925_rule_sync_check.py` ở chế độ mặc định — mà chế độ đó **ghi đè `AGENTS.md`** | Sẽ tạo ra một lỗi xanh giả **mới**, tinh vi hơn lỗi đang sửa: cổng chạy xong thì hệ luôn "đồng bộ" | Thêm chế độ `--check` chỉ đọc, bắt sổ quyết định gọi đúng chế độ đó |
| **Thông báo lỗi vô nghĩa.** `chay_bo_kiem()` lấy "dòng cuối cùng khác rỗng" làm lý do → in ra một dãy `====` | Cổng bắt đúng lỗi nhưng owner không biết lỗi gì | Lọc bỏ dòng chỉ toàn `=`/`-`; nay in `AGENTS.md … lệch bản sinh…` |
| **Số nền đầu tiên không so được.** Bản chụp `TRƯỚC` của cổng báo cáo chạy lúc agent song song **chưa** thêm V10975 vào CHANGELOG, nên chênh lệch 0→1 có thể bị hiểu nhầm là do V10975 xuất hiện chứ không do sửa code | Owner có thể nghĩ em thổi phồng tác dụng bản sửa | Chạy lại **bản cũ** trên **đúng trạng thái repo hiện tại**: bản cũ exit **0**, bản mới exit **1**, cùng một hoàn cảnh |

**Không có vấp nào ảnh hưởng tới runtime, dữ liệu sống hay đường ra số.**

---

## 8. Gỡ về

```bash
cd E:\Lottery_AI_Test
copy backups\v10976_pre\_v10920_decision_ledger.py.pre  web\backend\_v10920_decision_ledger.py
copy backups\v10976_pre\_v10920_session_start.py.pre    web\backend\_v10920_session_start.py
copy backups\v10976_pre\_v10921_report_gate.py.pre      web\backend\_v10921_report_gate.py
copy backups\v10976_pre\_v10925_rule_sync_check.py.pre  web\backend\_v10925_rule_sync_check.py
copy backups\v10976_pre\OWNER_DECISION_LEDGER.json.pre  docs\OWNER_DECISION_LEDGER.json
copy backups\v10976_pre\OWNER_DECISION_LEDGER.md.pre    docs\OWNER_DECISION_LEDGER.md
del docs\_LEDGER_TRANG_THAI.json
python web\backend\_v10920_decision_ledger.py
```

Hoặc `git revert <commit V10976 riêng>`. **Mất khoảng 2 phút · không cần restart service · không
ảnh hưởng VPS** (không deploy gì). Tài liệu quản trị đã prepend thì gỡ bằng `git revert`; nếu
gỡ tay thì chỉ xoá khối `## V10976` ở đầu ba file, **đừng** ghi đè cả file.

---

## 9. Theo dõi tiếp

| Mã máy | Mã đọc | Nhãn | Hạn | Trạng thái | Ngưỡng hành động bằng số |
|---|---|---|---|---|---|
| **FU-250** | `KS0806` | Soát nốt cổng còn thoát 0 khi trượt | **06/08** | `MEASURED_BUT_NOT_FIXED` | `_v10861_runtime_contract_audit.py`, `_v10921_rule_a55.py`, `_v10958_fu_reader.py` **không có** `sys.exit`/`SystemExit`. Tới 06/08: script nào **có** hook/cron/script khác đọc mã thoát thì sửa ngay; không ai đọc thì ghi rõ trong docstring "chỉ để đọc bằng mắt" rồi đóng mục |
| **FU-251** | `BC0803` | V10975 chưa có báo cáo công khai | **03/08** | `WAIT_LIVE` | Hết ngày 03/08 mà `_v10921_report_gate.py V10975` vẫn exit 1 → ghi `A55_VIOLATION_REPORT_MISSING` cho phiên V10975 và nêu ngay đầu phiên 04/08 |

Quyết định owner đã ghi vào sổ: **OD-20260803-A** · `SC0803` · *"Sửa 5 lỗi xanh giả ở tầng cổng
tự kiểm; cổng phải thoát khác 0 khi có vi phạm; báo số thật kể cả khi xấu hơn số cũ"* — 5 mệnh
đề máy kiểm được, hiện **🟢 khớp 5/5**.

**Hạn rà soát:** không đặt hạn cố định cho OD-20260803-A vì đây là quyết định về chất lượng cổng
kiểm, có hiệu lực thường trực; mệnh đề `kiem_code` chạy lại mỗi phiên nên code trôi khỏi nó sẽ
tự hiện thành TRÔI.

---

## Phụ lục — bảng 5 lỗi gọn

| Lỗi | Mức | Sửa thế nào | Ảnh hưởng thật đo được |
|---|---|---|---|
| L1 | HIGH | `chay_lenh` chạy thật `_v10925_rule_sync_check.py --check`, bắt mã thoát + dấu hiệu `SÁU MẶT ĐỒNG BỘ`; script hỏng = TRÔI | Bẻ `AGENTS.md`: cũ 🟢 5/5 exit 0 → mới 🔴 TRÔI 1/5 exit 2 |
| L2 | MEDIUM | `giai_thua_huong()` giải đệ quy, chống vòng lặp, trỏ tới ID lạ = TRÔI | `OD-20260801-D` ⚪ → 🟢 1/1 (thừa hưởng từ `OD-20260801-A`); ⚪ toàn sổ 2 → 1 |
| L3 | MEDIUM | soi **NĂM** mặt + so `AGENTS.md` với bản sinh từ `CLAUDE.md` | Bẻ `AGENTS.md`: cũ im lặng → mới cảnh báo ngay đầu briefing |
| L4 | MEDIUM | exit 1 vi phạm · exit 2 mất repo · cờ `--soft`; đã soi không luồng nào phụ thuộc mã thoát cũ | Cùng trạng thái repo: cũ exit 0 → mới exit 1, bắt **V10975 thiếu báo cáo** |
| L5 | MEDIUM | in `⛔ KHÔNG ĐO ĐƯỢC`, đóng dấu lên đầu `.md`, ghi `docs/_LEDGER_TRANG_THAI.json`, exit 1 | Giả lập probe hỏng: cũ thoát 0 + `.md` sạch trơn → mới thoát 1 + dấu "số bên dưới là số CŨ, lần đo tươi gần nhất 09:03:54" |
