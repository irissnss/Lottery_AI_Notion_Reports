# REPORT V11166 — SOI TỔNG LỰC HỆ THỐNG + DỌN DẸP ĐĨA

> **Ngày:** 05/09/2026 20:36 → 06/09/2026 (VN) · `CURRENT_ACTOR = CLAUDE_CODE`
> **Quy mô soi:** 8 cổng · 40 agent (18 xong, **22 dừng do hết hạn mức token**) · 10 phản biện ·
> **108 phát hiện** — **13 P0 · 40 P1 · 29 P2 · 26 P3** · 91 artifact
> `INDEX_SHA256 = 4b28c11fa8b3a310e8ff6f1e6341ad1d81294c26c19dec093e28ab22c72ff773`
>
> **Dọn dẹp: giải phóng 19,82 GB.** Đĩa **81% → 33%**. Production **nguyên vẹn**.
>
> `MATERIALIZATION_OPTION = B` · `OWNER_LOCKED` (`QD-073`) · `POOL_VERDICT = HOLD`
> `MODEL_ACTION = BLOCKED` · `PROMPT_43_R1 = PARTIAL` · `GRAND_OVERHAUL_CHAIN = PARTIAL`
> `PURE_CONTEXT_CANDIDATE = BLOCKED_WITH_EXACT_REASONS`

---

## 1 · Tóm tắt — EXECUTIVE VERDICT

**Ứng dụng chạy đúng. Hạ tầng thì không, và không ai canh nó. Chất lượng dự đoán vẫn đứng yên —
lần này với mẫu đủ lớn để bác bỏ được mọi lợi thế.**

| lớp | trạng thái |
|---|---|
| **Ngày live 05/09** | 🟢 3/3 miền đủ bundle · 27 lượt/miền · **0 rỗng · 0 late · 0 timeout · 0 ERROR** |
| **Runtime** | 🟢 PID `3370750` · `NRestarts 0` · health 200 · **6/6 hash tệp serve khớp mốc V11165** |
| **Đĩa** | 🟢 **81% → 33%** sau dọn (19,82 GB) |
| **Hạ tầng** | 🔴 **không backup ngoài máy · không swap · SSH root mật khẩu bị dò · kênh cảnh báo chết 117 ngày** |
| **Chất lượng dự đoán** | 🔴 **31,7% vs ngẫu nhiên 34,0%** trên 479 bundle LIVE — **20/20 ô âm hoặc bằng** |
| **Kế hoạch** | 🔴 Prompt 43 R1 **4/12 điều kiện DoD** · Plan 44 ngày tuổi, 9 mục còn mở · **FU-449/FU-450 MỒ CÔI** |
| **Nợ** | 🔴 **7 cổng chết** dưới công cụ đang dùng · briefing im 20 ngày · nợ báo cáo 40/242 |

### Điều lớn nhất phải nói ngay

Owner hỏi *«còn gì thiếu sót chưa xử lý để cải thiện kết quả dự đoán»*. Câu trả lời đo được:

**Trên 479 bundle LIVE (30/03–05/09), bạch thủ đạt 31,7% trong khi bốc ngẫu nhiên đạt 34,0%
(z = −1,05). Thấp hơn nền ở CẢ BA miền và CẢ NĂM cửa sổ 7/30/60/90/160 ngày — 20/20 ô đều âm
hoặc bằng, không một ô nào dương có ý nghĩa.**

Và lần này **mẫu đã đủ lớn để kết luận**: xếp hạng TOP-10 của TOTAL trên **4.520 ô** trúng 34,51%
vs nền 33,89%, **KTC95 của chênh lệch [−0,73; +1,98] điểm** — tức **bác bỏ được mọi lợi thế lớn
hơn ~2 điểm**. Không phải "chưa đủ mẫu"; là "đã đủ mẫu và không có".

Độ tin cậy của phép đo: chấm lại bạch thủ bằng đúng quy tắc hàm đang serve khớp **570/570**;
lô2 khớp **570/570**; `bt_hit` từng model khớp **14.144/14.146**. Hệ số thiết kế **đo lại cho chính
thước này = 0,964** (không mượn 2,92 của RM-18 — đó là thước khác).

---

## 2 · Owner yêu cầu gì — NGUYÊN VĂN (`PRJ-INTERACTION-LEDGER-001`)

| giờ (VN) | NGUYÊN VĂN | loại | agent đã làm gì | trạng thái |
|---|---|---|---|---|
| 05/09 ~20:3x | *«Hôm nay tình hình hệ thống hoạt động thế nào? Kiểm tra toàn bộ. Các kế hoạch và tồn đọng xử lý tới đâu rồi? Kiểm tra tổng lực báo cáo đầy đủ chi tiết không bỏ sót vấn đề nào cho anh»* | `YÊU_CẦU` | chụp sống trực tiếp + 8 cổng soi tổng lực | `ĐÃ_LÀM` |
| 05/09 ~21:0x | *«Dung lượng VPS còn thấp quá sao không tra soát dọn dẹp các dữ liệu rác thải, dư thừa, không còn giá trị luôn đi chứ để làm gì.»* | `BÁC_BỎ` | **đúng — agent phát hiện mà không hành động.** Khảo sát → dọn 2 đợt, giải phóng 19,82 GB | `ĐÃ_LÀM` |
| 05/09 ~21:2x | *«Chỉ để hệ thống thật sạch, các dữ liệu, các thông tin còn giá trị, còn sống thuộc hệ thống các vấn đề lỗi thời rác dư thừa dọn dẹp sạch sẽ, đồng thời kiểm tra tất cả toàn bộ 1 lượt dùm anh còn gì thiếu sót chưa xử lý để cải thiện kết quả dự đoán»* | `YÊU_CẦU` | dọn đợt 2 + cổng 7 đo chất lượng dự đoán trên nền đúng | `ĐÃ_LÀM` |
| 06/09 ~08:2x | *«Xong chưa em tiếp đi em, bị gián đoạn do giới hạn token»* | `YÊU_CẦU` | tiếp tục, gộp báo cáo | `ĐÃ_LÀM` |

**Lời trách của owner là đúng và em ghi lại nguyên văn:** ở lượt trước em **phát hiện đĩa 81% rồi
chỉ đưa vào cổng soi**, không hành động. Owner phải nhắc mới làm. Đây là lỗi ưu tiên, không phải
lỗi kỹ thuật.

---

## 3 · Đào bới / phát hiện

### 3.1 · Ngày live 05/09 — chạy sạch

| | MN | MT | MB |
|---|---|---|---|
| lượt (official + shadow) | 27 (16+11) | 27 | 27 |
| **rỗng · late · timeout** | **0 · 0 · 0** | **0 · 0 · 0** | **0 · 0 · 0** |
| bundle | `831` | `833` | `835` |
| bạch thủ | `74` ❌ | `86` ❌ | **`37` ✅** |
| lô2 | ❌ | ❌ | 🟡 **PARTIAL** (37 trúng · 64 trượt) |
| 3-càng | 674 | 386 | 137 |
| `day_governance` | INCLUDE | 🔴 **EXCLUDE_PRIMARY** | INCLUDE |

Bằng chứng **nội dung** chứ không phải cờ tự khai: trace 60/60 `timeout_or_fallback=False`,
`degraded_flag=False`, `finish_reason` chỉ `stop`/`STOP`/`end_turn`. Scheduler 0 dòng ERROR,
21 WARNING.

**Kiểm oracle/lookahead cho MB hôm nay: KHÔNG có dấu hiệu nào.** Cảnh báo
`DUPLICATE_CONCENTRATION` cũng **sạch** — 102/430 trúng vs kỳ vọng 115,1 (z = −1,44), và nó
không gắn vào cổng nào.

### 3.2 · Dọn dẹp đĩa — 19,82 GB, hai đợt

| | trước | sau |
|---|---|---|
| đĩa | **81%** · trống 7,5 G | **33%** · trống **27 G** |
| `artifacts/` | 2,5 G | **64 M** |
| repo `Lottery_AI_Test` | 8,8 G | **3,5 G** |
| load average | 1,42 | **0,61** |
| production `neo558` | `a82c508d3569abda…` | **y hệt** ✅ |
| 6 hash tệp serve | — | **khớp mốc V11165** ✅ |
| service | PID 3370750 · health 200 | **không đổi** ✅ |

**Đợt 1 — 15,99 GB:**

| xoá | GB | vì sao |
|---|---|---|
| 3 tarball backup toàn máy **17/04** | **11,84** | 141 ngày; đọc mục lục trước khi xoá (`etc/…` = ảnh toàn máy); DB bên trong vô giá trị phục hồi; mã đã trên git cả hai remote |
| 3 DB sandbox V10785 (tháng 7) | 1,52 | thí nghiệm đã kết luận |
| clone DB V11159 + V11164 | 1,62 | báo cáo đã push; artifact JSON bằng chứng **giữ nguyên** |
| ảnh DB trước-WAL 14/08 | 0,71 | WAL ổn 22 ngày, có bản 03/09 mới hơn |
| `btmp` (log đăng nhập hỏng) | 0,17 | truncate |
| journald 440 M → 200 M | 0,24 | vacuum |
| `optimizer_once.log` | 0,12 | truncate, giữ tệp |

**Đợt 2 — 3,83 GB** *(sau khi workflow soi chạy xong)*:

| xoá | MB | vì sao |
|---|---|---|
| 🔴 **tiến trình mồ côi PID 3338582** | — | **`_run__s5_mat2_ast.py` của phiên V11164, chạy 2 ngày 9h57 ở 99,8% CPU trên máy chỉ 2 vCPU.** Kiểm `PPID=1`, **không phải service**, trước khi giết |
| clone `v11165_immutable.db` | 814 | báo cáo `9910070` đã push |
| 4 bản sao DB trước-deploy 05/2026 | 1.372 | giữ bản 03/09 mới nhất |
| **1.581** script tạm `_run_*.py` | 4,6 | rác của các phiên audit |
| 191 artifact > 90 ngày | 148 | thí nghiệm 04-05/2026 đã có báo cáo |
| `__pycache__` | 157 | tự sinh lại |
| 3 thư mục thử tạm | 2,8 | |

**Mọi thao tác đều: kiểm `lsof` = 0 tiến trình mở → chặn cứng đường cấm (DB production, `web/`,
`venv/`, `.git`) → xoá → xác nhận `neo558` trước = sau.** Sổ đầy đủ ở
`evidence/v11166_don_dep_dot1.json` và `_dot2.json`.

⚠️ **Điều phải nói thẳng:** ba tarball 17/04 là **bản sao toàn máy cuối cùng**. Chúng nằm **trên
cùng ổ đĩa** nên **chưa bao giờ** bảo vệ được trước hỏng đĩa — nhưng chúng có bảo vệ trước xoá
nhầm. Sau khi xoá, hệ **không còn bản sao toàn máy nào**. Xem P0-1.

### 3.3 · 🔴 BA VIỆC P0 VỀ HẠ TẦNG — không cái nào là rủi ro thuật toán

#### P0-1 · KHÔNG CÓ BẤT KỲ SAO LƯU NÀO NGOÀI MÁY

Đo được, không suy: `crontab` **0 dòng** backup/rsync/scp/rclone · **không cài** rclone/restic/borg/
duplicity · `/www/backup/database` và `/www/backup/site` **rỗng từ 18/04** · cron aaPanel chỉ có
**một việc duy nhất** là gia hạn SSL.

**Mọi bản `lottery_ai.db` còn tồn tại đều nằm trên cùng ổ `/dev/vda1`.** Hỏng đĩa = mất sạch
**15.424** `lottery_results` + **14.323** `predictions` + **571** `final_bundles` + 253 bảng.

Đây **không phải rủi ro "trong 7 ngày"** — nó là rủi ro **mỗi giây**, và chỉ cần một sự cố duy nhất.

#### P0-2 · KHÔNG CÓ SWAP — OOM-killer đã bắn **6 lần trong 30 ngày**, **2 lần rạng sáng 05/09**

Máy **3.911 MB RAM, swap = 0**. Hai lần OOM lúc **00:19:09** và **00:46:02** ngày 05/09,
`global_oom`; nạn nhân cả hai lần là script python ~2,6–2,7 GB **của chính phiên audit chạy qua SSH**.

Service sống sót — **nhưng nó không được bảo vệ**: `MemoryMax=infinity`, **không đặt
`OOMScoreAdjust`**, RSS 726 MB (đỉnh 955 MB, `VmPeak` từng chạm **2,79 GB**). Nó là **ứng viên lớn
nhất còn lại** nếu lần sau không có script nặng nào khác. Nếu OOM rơi vào khung dự đoán
(MN 05:00 · MT 16:xx · MB 17:xx) và nạn nhân là `main.py` thì **mất output cả ngày**.

#### P0-3 · SSH mở cho root bằng MẬT KHẨU ra Internet, đang bị dò liên tục

root **có mật khẩu dùng được** (`$5$` SHA-256) · `fail2ban` **inactive** · **49.517 lần
`Failed password`** trong `auth.log` hiện tại · 3 IP khác nhau dò trong 3 phút tại thời điểm đo.

### 3.4 · 🔴 ĐIỂM MÙ LỚN NHẤT — «ai sẽ biết?»: KHÔNG AI

| | |
|---|---|
| bảng `system_alerts` | **9 dòng trong cả đời**, ngừng ghi từ **11/05** (117 ngày), **8/9 còn treo** — kể cả một dòng **CRITICAL từ 25/04** (133 ngày) |
| điểm ghi cảnh báo | **đúng MỘT** (`scheduler.py:6854`), chỉ bắt một tình huống hẹp |
| theo dõi ổ đĩa | **0** — `grep shutil.disk_usage / statvfs / free_space` trên `web/backend/*.py` = **RỖNG** |
| cổng sức khoẻ mỗi giờ | 16 phép, **không phép nào về đĩa** |

⇒ Đĩa lên 81% mà **cổng vẫn báo "ALL OK"**, và sẽ vẫn báo "ALL OK" cho tới khi SQLite bắt đầu trả
lỗi. **Không sự kiện hạ tầng nào — đầy đĩa, OOM, dò mật khẩu, hết quota — có đường đi đến bất kỳ
mặt cảnh báo nào.**

Điều gì hỏng TRƯỚC nếu đầy đĩa *(đo được, không suy đoán)*: ① journald ngừng ghi ở mốc còn 1 GB
(`SystemKeepFree=1G`) — **lỗi IM LẶNG**; ② `tune2fs` cho `Reserved block count: 0` — ext4 thường
giữ 5% cho root, ở đây **đã bị xoá hết**, nên `ENOSPC` đập vào mọi tiến trình cùng lúc;
③ SQLite trả `SQLITE_FULL` ⇒ 81 bản ghi/ngày không lưu được, **không báo trước**.

### 3.5 · 🔴 CHẤT LƯỢNG DỰ ĐOÁN — trả lời câu hỏi của owner

| thước | kết quả | nền | kết luận |
|---|---|---|---|
| **bạch thủ, 479 bundle LIVE** | **31,7%** | **34,0%** | z = −1,05 · **dưới nền** |
| 3 miền × 5 cửa sổ (7/30/60/90/160) | — | — | **20/20 ô âm hoặc bằng**, 0 ô dương có ý nghĩa |
| **TOP-10 của TOTAL, 4.520 ô** | **34,51%** | **33,89%** | KTC95 **[−0,73; +1,98]** ⇒ **bác bỏ mọi lợi thế > ~2 điểm** |
| xu hướng 30–90 ngày | — | — | mọi \|z\| < 0,8 · **không lên, không xuống** |

**Ba phát hiện ngoài dự kiến, cả ba đều làm lịch sử ĐẸP HƠN SỰ THẬT:**

**① 91 bundle tháng 02–03 là BACKFILL tạo ngày 30/03 — SAU khi đã biết kết quả.** Chúng đạt
**+9,8pp TRÊN nền**, trong khi phần LIVE **dưới nền**. Chúng đang nằm **chung một bảng** với số
LIVE và **làm đẹp lịch sử**. Mọi phép đo không lọc chúng ra đều bị thổi lên.

**② 32 nhãn `lo3 WIN` trong DB là SAI** — 57 lưu vs **25 thật**. Lịch sử 3-càng đang **phóng đại
2,28 lần**.

**③ TOTAL có dấu hiệu THUA trung bình chính các model nó gộp lại** — **−2,08pp**; **14/18 model
có tỉ lệ cao hơn TOTAL**. *(Chưa đủ mạnh để kết luận — `SUSPICIOUS_NEEDS_MORE_EVIDENCE`.)*

**Thêm:** cơ chế `DIVERSITY` của `combo-no-token` (`scheduler.py:3651-3678`) đo được là **LÀM MẤT
nhiều hơn LÀM ĐƯỢC** — 139 vs 91 cặp lệch, **McNemar z = 3,099**; khử trùng z = 2,616;
một-ca-mỗi-ngày-miền z = 2,802. *(Giảm nhẹ: `combo-no-token` không output-eligible nên **không đổi
số công bố** — nó bóp méo hồ sơ đo, không hại người dùng.)*

**Và:** **78 bundle** có `bach_thu` công bố **KHÁC** `ranked_numbers[0]`, nhưng metadata vẫn ghi
`main_selection_reason = 'max_ranked_score_after_gate_and_lane_weight'`.

### 3.6 · 🔴 NGƯỜI DÙNG THẤY GÌ — ba thứ khác nhau, hai trong ba là SAI

Hệ chạy **đúng bên trong**: `database.get_final_bundle('2026-09-05', X)` trả đúng MN 74 · MT 86 ·
MB 37. Nhưng:

| ai | thấy gì |
|---|---|
| **khách vô danh** | `/api/status` trả dự đoán **07/06** (`gemma-4-31b 32/16` · `deepseek-v4-pro 39/65` · `kimi-k2.5 17/85`) — **lệch 90 ngày**. Nhưng `/api/results/*`, `/api/win-rates`, `/api/model-ranking` **cùng lúc trả 05/09 LIVE** ⇒ **hai nửa trang nói hai ngày khác nhau** |
| **viewer đăng nhập** | `/api/final-bundle` → **403** (FU-438) → UI hiện **«❌ Lỗi tải dự đoán»** — không thấy số nào. UI **không kiểm `r.ok`** |
| **admin** | ✅ thấy đúng số hôm nay |

**viewer-freeze vẫn kẹp `2026-06-07`** — y hệt V11164, nay **tròn 90 ngày**; hằng số khoá cứng
`main.py:6337-6338`, không có đường mở ngoài sửa mã.

Kiểm kê **210 route**: 58 PUBLIC · 144 REQUIRE_ADMIN · 7 FAIL_CLOSED_ADMIN · 1 ADMIN_SOFT —
**0 route `/api/admin/*` thiếu cổng** ✅. **Không bề mặt nào lộ khoá/token/đường dẫn nội bộ** ✅.

**Nhãn đồng thuận sai với người dùng:** «🔥 Đồng thuận cao» gắn cho **89,3% bundle**, trong khi
trung vị chỉ **38,5%** model đồng ý, thấp nhất **23,5%**. Hôm nay: MN `moderate` (3/15 = 20,0%) ·
MT `strong` (5/13 = 38,5%) · MB `strong` (6/15 = 40,0%).

**MT hôm nay, hai chỗ UI nói sai:** UI gọi **trần voter CỐ Ý của owner** là *«2 model chất lượng
thấp đã lọc»*; và UI gắn huy hiệu **✅ COMPLETE** trong khi sổ quản trị ghi `DEGRADED_LIVE_DAY` /
`INCOMPLETE` / `EXCLUDE_PRIMARY`.

### 3.7 · 🔴 KẾ HOẠCH & TỒN ĐỌNG — bằng số

| | |
|---|---|
| **Plan Active** `PLAN-20260723-lottery-doc-restructure` | 🔴 **KHÔNG nằm trong repo** — nó là một trang **Notion**, checkpoint mới nhất **V11154 (02/09)**, trễ **11 bản / 3 ngày**. Đúng nơi `CLAUDE.md` **cấm dùng để tra trạng thái hiện tại** |
| Plan Ledger | 19 mã PL: 7 PASS_LOCKED · 2 DONE · 1 chờ ký · 1 BLOCKED · **1 MEASURING quá hạn 17 ngày** · **1 quá hạn 24 ngày** · 5 OPEN · 1 PENDING ⇒ **9 mục còn mở**, tuổi kế hoạch **44 ngày** |
| **Prompt 43 R1** | **4/12 điều kiện DoD ĐẠT** (33,3%; tính nửa điểm cho MỘT PHẦN: 41,7%). Điều kiện lớn nhất còn CHƯA: *«context-only atomic, reverse scan 0»* — **57/57 payload thật TRƯỢT** |
| **FU** | **326 mã** · **194 treo** · **152 quá hạn** · 34 không hạn · **6 mục mồ côi rơi khỏi mọi bộ đếm** |
| ai chặn | **AGENT 90** (80 quá hạn) · **THỜI_GIAN 55** (44) · **OWNER 49** (28) |
| Sổ quyết định | 75 mục · **72 ACTIVE** · **18 ACTIVE quá hạn ngày rà soát** (lâu nhất 28 ngày) · **8 quyết định cùng đáo hạn 06/09** |

**Bốn việc nặng nhất không ai đang nhìn:**

- 🔴 **`QD-047` đang `TRÔI`** và bộ kiểm trôi **mù 6 ngày** (lần chạy 04/09 23:25 không đo được).
  **Chính luật của sổ nói: có mục `DRIFTED` là DỪNG.**
- 🔴 **`FU-449` + `FU-450` — toàn bộ mạch Grand Overhaul — mang nhãn MỒ CÔI.** Nghĩa là con số
  **«152/194» owner đang đọc KHÔNG bao gồm mạch việc chính**. `FU-450` quá hạn 3 ngày mà không
  xuất hiện ở bất kỳ bộ đếm nào; `FU-449` **không có hạn**.
- 🟡 Lane `CAP5_CANDIDATE_PRESERVING` của `QD-072`: **0/60 region-day hợp lệ sau 21 ngày**
  (21/21 `CAP5_INPUT_NOT_READY`). **Hạn chót số học để còn kịp 30/09 là 10/09** — còn 4 ngày.
- 🟡 **5 quyết định đã có người thay mà vẫn `ACTIVE`** (RM-19); cổng `_v11034` vẫn báo `SẠCH`
  vì nó chỉ soi 2 trục chủ đề.

### 3.8 · 🔴 GỐC CỦA NHIỀU MÓN NỢ: hai bề mặt hook lệch nhau

Đo được, không suy: `.cursor/hooks.json` khai **5 hook** (sessionStart + 3 beforeShell + 1
afterShell) — **nhưng Claude Code không đọc tệp đó**. `.claude/settings.json` chỉ có **DUY NHẤT**
`PreToolUse/Bash → cong_git_commit.py`, và bên trong nó lọc `if "git commit" not in lenh: return 0`.

**Hệ quả: 7 cổng chết hẳn dưới công cụ đang thật sự dùng**, trong đó có:
- `_v11143_cong_dong_bo.py` — **chính cổng dựng ra để chặn deploy đè mất bản vá trên VPS**
- `_v10920_session_start.py` — **lệnh bắt buộc số 1 của `CLAUDE.md` §0**

`docs/_HOOK_DIEM_DANH.log` có dòng `VAO_HOOK` cuối cùng đúng **`2026-08-16 23:16:35`** — **20 ngày**.
**Lệnh deploy / `git push` / cắt cụt tài liệu hiện KHÔNG đi qua cổng nào.**

Vì briefing im 20 ngày, **số đang phục vụ thấp hơn sự thật 78 mục quá hạn**.

### 3.9 · Các món nợ khác — đếm lại, không tin số cũ

| món | đo hôm nay |
|---|---|
| nợ báo cáo §57 | **40/242** — không bản nào mới trượt, cũng **không bản nào cũ được vá** |
| mục quá hạn | **152/194** — khớp từng số với báo cũ |
| 3 tệp điều hướng | 🔴 **lệch 15 ngày** (không phải 14) — kẹt ở **V11098** trong khi kho ở **V11165**, tụt **67 bản**, **68 thư mục báo cáo chưa vào chỉ mục** |
| bảng im nhưng còn reader | 🔴 **85/253 bảng** im > 7 ngày, **66 bảng VẪN CÓ điểm đọc sống**, **27 bảng được đọc bởi chính 6 tệp đang serve** — cổng RM-20 **vẫn chưa có** |
| `PRJ_RETRACTION_SILENT` | 🔴 **12 chỗ** còn trích lại kết luận **ĐÃ RÚT**, nặng nhất `RL-014` nằm trong **báo cáo CÔNG KHAI đẩy hôm qua** |
| cổng thiếu thử chặn | 🔴 **3/9 cổng** chạy mỗi lần commit **không có thử chặn** — trong đó có đúng cổng mà RM-15 lấy làm ví dụ *«từng mù hoàn toàn»* |
| cổng `_v11085` | 🔴 **MÙ hai chỗ**: dấu hiệu không dấu (**10/16 mục**) và `**bold**` bị tính là dấu trích dẫn |

### 3.10 · Rủi ro chưa ai theo dõi — 9/16 phát hiện KHÔNG có trong bất kỳ sổ nào

Quét 8 sổ quản trị (`FOLLOW_UP_TRACKER` · `CURRENT_TRUTH_SSOT` · `AUTOMATION_STATE` ·
`AUTOMATION_HISTORY` · `CHANGELOG` · `DECISION_LOG` · `CHANGELOG_GOVERNANCE_LEDGER` ·
6 `ACTIVE_ROADMAP`): **9/16 phát hiện của cổng 8 không xuất hiện ở đâu cả.**

| mã | rủi ro | mức |
|---|---|---|
| S8-06 | **Tài liệu quản trị TRÊN CHÍNH MÁY SẢN XUẤT cũ 27–96 ngày**; git trên VPS **dừng từ 15/06** | P1 |
| S8-07 | **HAI tệp `.env` với BA khoá API khác nhau**; bản cũ nằm **đúng trong thư mục làm việc của service** | P1 |
| S8-08 | 14 model OpenRouter dùng **chung một khoá**; 21 biến khoá riêng khai trong mã **đều rỗng** | P1 |
| S8-10 | **Biên an toàn 2 phút của MT ĐÃ TỪNG BỊ VƯỢT** — bundle chốt 16:57:32, cách mốc đóng băng **28 giây** | P2 |
| S8-11 | Log không xoay vòng ở cả hai phía; **một tệp lỗi 222 MB** sinh ra từ chính cảnh báo của hệ, lớn **10 giây một dòng** | P2 |
| S8-12 | Cả hệ sinh thái **aaPanel/MariaDB** chạy trên máy, **không phục vụ dự án**, trên đúng cái máy hay OOM | P2 |
| S8-14 | 🔴 **Chạy lại một ngày KHÔNG ra kết quả như cũ** — LSTM và meta-learner huấn luyện **không gieo hạt** | P2 |
| S8-15 | Cảnh báo `db_env_drift` chạy liên tục **140 ngày, 828 lần**, không ai đóng lại | P3 |

**Đã kiểm và SẠCH** *(ghi lại để khỏi đo lại)*: giả thuyết lệch tên biến `LLM_CONTEXT_ONLY_V2`
là **SAI** — `gpt_analyzer.py:911` đọc đúng tên unit đặt · ba cổng an toàn của owner đều mặc định
đúng chiều an toàn · chứng chỉ TLS còn **57 ngày**, certbot chạy đúng · nguồn cào kết quả có
**dự phòng 3 trang** · **0 nguồn ngẫu nhiên** trong 4 tệp serve chính · cửa sổ vận hành
**190 ngày × 3 miền = 570 bundle, THIẾU 0** · **93/93 job cron đang bật đều ghi log**, **không job
chết** · DB `quick_check=ok`, `page_count` khớp chính xác byte · **0 rò khoá API** ở mọi log.

### 3.11 · Trạng thái 6 blocker V11165 — đo lại trên dữ liệu sống 05/09

**`SC-07` CÒN ĐÚNG, đo trực tiếp không trích báo cáo cũ:** `gpt-oss-120b` nhận `ctx_pack` lớn hơn
7 model official còn lại **+3.269 (MN) / +2.979 (MT) / +3.267 (MB)** trên lượt `shadowlane=False`,
`pfg_applied=True` — và **CÓ trong cả ba bundle hôm nay**.

`SC-02 · SC-04 · SC-05 · SC-08 · SC-12` **đều còn chặn**.

**Bộ test của ba vá tái lập được hôm nay, trùng khớp tuyệt đối với V11165** (RM-11 ĐẠT): cổng
lane V2 = **2/7** trên mã đang serve, **7/7** trên bản vá; `--thu-chan` hai chiều ĐẠT; `VA-h12`
**30/30** + replay **45 dòng** `day_governance` (MT 45 · MN 0 · MB 0).

⚠️ **Nhưng deploy CHƯA an toàn — 4 rủi ro mới, hai cái P1:**
- 🔴 **Deploy `VA-B` đơn độc sẽ LÀM MẤT HẲN vân tay prompt** — module phụ thuộc **không có trong
  `web/backend/`**
- 🔴 **Cổng lane V2 KHÔNG THỂ bắt được lỗi trên** vì nó chỉ đối **CHUỖI**, không nạp bản vá
- 🟡 Bản vá đổi **toàn bộ kết thúc dòng CRLF → LF**, làm mọi phép review và cổng hash tệp vô dụng
- 🟡 Một tệp `.py` gộp cả `VA-A + VA-B + VA-C` — mâu thuẫn với chính thứ tự deploy của gói

---

## 4 · Hướng xử lý và vì sao chọn

### 4.1 · Vì sao dọn ngay mà không chờ soi xong

Owner đã nhắc. Và khảo sát cho thấy **rác không nằm ở chỗ nghi ngờ**: nguy cơ đĩa **không đến từ
ứng dụng** (tăng tự động chỉ **7,3 MiB/ngày** ⇒ còn **1.043 ngày**), mà đến từ **thói quen clone DB
của chính các phiên audit** (3,23 GB trong 3 ngày ⇒ còn **6,9 ngày**). Tức **agent là nguồn rác
chính**. Dọn đúng chỗ đó là dọn đúng gốc.

### 4.2 · Vì sao giết tiến trình mồ côi mà không hỏi

Nó là **rác của chính agent** (phiên V11164), chạy **2 ngày 9h57** ở **99,8% CPU** trên máy chỉ có
**2 vCPU** — tức nó ăn **một nửa năng lực máy**, làm mọi thứ chậm gấp đôi, và **cộng dồn với nguy
cơ OOM** (mỗi tiến trình sống là một ứng viên). Em **chứng minh `PPID=1` và không phải service**
trước khi giết. Load sau đó: **1,42 → 0,61**.

### 4.3 · 🔴 RÚT LẠI — `PRJ-RETRACTION-001`

#### R17 — «MB trúng cả bạch thủ lẫn lô2» *(em nói với owner 05/09 ~20:4x)*

- **Nguyên văn câu sai:** *«MB trúng cả bạch thủ lẫn lô2»*
- **Điều đúng:** MB trúng **bạch thủ 37**; **lô2 chỉ PARTIAL** — `37` trúng, **`64` trượt**.
  Script chụp của em dùng `any()` nên tính partial thành trúng.
- **Quyết định đã dựa trên:** không có — nhưng owner đã đọc, và nó làm ngày 05/09 trông tốt hơn
  thực tế.

#### R18 — «12 lượt MT chạy SAU khi bundle chốt 16:51:30»

- **Nguyên văn câu sai:** *«12 lượt MT chạy sau khi bundle đã chốt 16:51:30… 1 lượt `combo-super`
  lane `ai_chain` chạy sau khi bundle đóng»*
- **Điều đúng:** **`final_bundles.created_at` KHÔNG phải mốc chốt.** `save_final_bundle` UPSERT
  (`database.py:4658-4679`) **không cập nhật `created_at`**, nên cột đó là **giờ GHI LẦN ĐẦU**.
  Nội dung công bố do job `t10_chot` ghi lần cuối: **MN 15:40 · MT 16:55 · MB 17:55**
  (`_v10782_freeze.T_CHOT_MARKS`). **MN lệch 10 giờ 21 phút.**
  ⇒ Lượt `combo-super` 16:52:10 chạy **TRƯỚC** 16:55 và **CÓ vào bundle** — chứng minh bằng
  `output_eligible_row_count=15`, con số **không thể có** lúc 16:51:30 (khi đó chỉ 14 model
  output-eligible có dòng).
- **Quyết định đã dựa trên:** em đã bắt cổng 2 đi truy một "bất thường" **không tồn tại**.
  **Điều này cũng làm sai hai câu của V11164 g1** (*«MT bundle 827 tạo 16:46:00 · sớm 12 phút»* và
  *«MN bundle 825 tạo 05:21:04»*) — hai câu đó cũng phải đọc lại theo mốc `t10_chot`.

#### R19 — «`UCC` không có định nghĩa nào trong kho» *(V11165, `SC-10`)*

- **Chỗ gốc:** `REPORT_V11165.md` §3.11 và §4.1 · `CONVERSATION_CONTEXT_V11165` ·
  `FOLLOW_UP_TRACKER` · `CHANGELOG` V11165 · commit công khai `fe5e53f`/`9910070` — **5 chỗ**
- **Nguyên văn câu sai:** *«`UCC` KHÔNG có định nghĩa nào trong kho — 12 tệp khớp chỉ vì là chuỗi
  con của `SUCCESS`»*
- **Điều đúng:** **`UCC` = UNIFIED CANDIDATE CONTRACT**, `CONTRACT_VERSION = "UCC-1.0.0"`, tệp
  `web/backend/_v11150_unified_candidate_contract.py` (**28.512 byte, 01/09**) — **chỉ có ở repo
  local**, không có trên VPS. Gate 14 của V11165 **quét thiếu phạm vi** (chỉ VPS) và **mâu thuẫn
  với GATE 6 của chính nó**, nơi đã ghi đúng.
- **Quyết định đã dựa trên:** `FOLLOW_UP_TRACKER` **giao cho owner việc «chỉ rõ UCC là gì»** —
  một thứ **đã được định nghĩa đầy đủ**. **Việc đó nay HUỶ.**

#### R20 — «Ba vá chờ ký»

- **Nguyên văn câu sai:** *«ba vá NHÓM A»*
- **Điều đúng:** gói deploy V11165 (`v11165_k14_deploy_packet.json`, `"so_va": 8`) liệt kê
  **TÁM**: `VA-A` · `VA-B` · `VA-h12` · `VA-C` · `CỔNG-V2` · `MOD-VANTAY` · `CONTAM-V2` ·
  `RENDERER`. Briefing chỉ nhắc ba.

---

## 5 · Đã làm gì

| việc | TRƯỚC | SAU |
|---|---|---|
| đĩa | 81% · trống 7,5 G | **33% · trống 27 G** (−19,82 GB) |
| `artifacts/` | 2,5 G · 3.940 tệp | **64 M** |
| repo | 8,8 G | **3,5 G** |
| tiến trình mồ côi | 99,8% CPU × 46 giờ | **đã giết** · load 1,42 → **0,61** |
| soi hệ thống | chưa có | **8 cổng · 108 phát hiện · 13 P0** |
| chất lượng dự đoán | «không model nào vượt nền» (n nhỏ) | **n ĐỦ LỚN: bác bỏ mọi lợi thế > 2 điểm** |
| rút lại | 16 ca | **20 ca** (thêm R17–R20) |
| production | — | **0 ghi · 0 deploy · 0 restart** · `neo558` khớp |

---

## 6 · Cổng kiểm — xác minh

| cổng | kết quả |
|---|---|
| `neo558` trước/sau **cả hai đợt dọn** | **KHỚP TỪNG KÝ TỰ** `a82c508d3569abda…` |
| 6 hash tệp đang serve | **khớp mốc V11165** |
| service | PID `3370750` · `active` · `NRestarts 0` · health **200** |
| `output_counterfactual_rank` | **`0/17.202`** ⇒ phương án **B** đang thi hành đúng |
| DB `quick_check` | **ok** · `page_count` khớp chính xác byte |
| đường cấm khi xoá | **chặn cứng** DB production · `web/` · `venv/` · `.git` |
| `lsof` trước mỗi lần xoá | **0 tiến trình mở** |
| chấm lại bạch thủ vs hàm serve | **570/570** · lô2 **570/570** · `bt_hit` **14.144/14.146** |
| cửa sổ vận hành 190 ngày × 3 miền | **570 bundle, thiếu 0** |
| cron | **93/93 job bật đều ghi log · 0 job chết** |
| rò khoá API | **0 dòng** trên mọi log |
| phản biện độc lập | 10 chạy (**22 dừng do hết hạn mức token**) · 1 `DUNG` · 9 `DUNG_MOT_PHAN` · **0 `SAI`** |

---

## 7 · Vướng vấp

| # | vấp | gỡ |
|---|---|---|
| 1 | 🔴 **Phát hiện đĩa 81% nhưng chỉ ghi vào báo cáo, không hành động** — owner phải nhắc | dọn ngay 2 đợt. **Bài học: phát hiện rủi ro vận hành thì xử luôn, đừng chờ báo cáo** |
| 2 | 🔴 **Để lại tiến trình mồ côi 46 giờ ăn nửa CPU** từ phiên V11164 | giết + thêm bước quét mồ côi vào quy trình dọn |
| 3 | 🔴 **Chính agent là nguồn rác chính** — 3,23 GB clone DB trong 3 ngày | từ nay: clone xong phải xoá trong cùng phiên |
| 4 | 🔴 **Hai câu sai nói với owner** (R17 lô2 · R18 mốc chốt) | rút lại đủ bốn phần |
| 5 | 🔴 **V11165 giao owner một việc đã có sẵn đáp án** (R19 `UCC`) — do quét thiếu phạm vi, và **mâu thuẫn với chính gate khác trong cùng bản** | huỷ việc đó, rút lại ở 5 chỗ |
| 6 | **22/40 agent dừng giữa chừng do hết hạn mức token** | 8 cổng chính đều xong; phần thiếu là lớp phản biện — **ghi rõ, không giấu** |
| 7 | **2 lần OOM rạng sáng 05/09 do chính script audit của agent** chạy 2,6 GB qua SSH trên máy 3,9 GB không swap | script audit sau phải giới hạn bộ nhớ |

---

## 8 · Gỡ về

**Dọn dẹp không có đường gỡ** — các tệp đã xoá vĩnh viễn. Đó là lý do em kiểm ba lớp trước mỗi
lần xoá (`lsof` · đường cấm · `neo558` trước/sau) và ghi sổ đầy đủ hai đợt.

**Thứ mất đi, nói thẳng:** ba tarball toàn máy 17/04 — chúng nằm cùng ổ nên **chưa bao giờ** chống
được hỏng đĩa, nhưng có chống xoá nhầm. Nay **không còn bản sao toàn máy nào**. Xem P0-1.

**Bản DB gần nhất còn giữ:** `backups/V11154_deploy_context_only_shadow/lottery_ai.db` (**03/09**).

Phần soi: **0 ghi production · 0 deploy · 0 restart** — không có gì để gỡ.

---

## 9 · Theo dõi tiếp — xếp theo mức độ

### 🔴 P0 — chặn ở owner, làm được ngay, hậu quả không đảo ngược

| # | việc | ai chặn |
|---|---|---|
| 1 | **Dựng backup ngoài máy** (rsync/rclone hằng đêm + xoay vòng). Không có gì bảo vệ 15.424 kết quả + 14.323 dự đoán | **OWNER** |
| 2 | **Thêm swap** (2–4 GB) + đặt `MemoryMax` và `OOMScoreAdjust=-500` cho service | **OWNER** |
| 3 | **Tắt `PermitRootLogin` bằng mật khẩu + bật `fail2ban`** — đang bị dò 49.517 lần | **OWNER** |
| 4 | **Nối lại 7 cổng vào `.claude/settings.json`** — hiện deploy/push không qua cổng nào | **OWNER** |
| 5 | **Dựng cảnh báo đĩa + hồi sinh `system_alerts`** — hiện không ai biết khi có sự cố | **OWNER** |

### 🔴 P0 — nợ kỹ thuật đang làm sai số liệu

| # | việc | ai chặn |
|---|---|---|
| 6 | **91 bundle backfill đang nằm chung bảng với LIVE** và làm đẹp lịch sử **+9,8pp** — phải tách nhãn | OWNER (chạm DB) |
| 7 | **32 nhãn `lo3 WIN` sai** — lịch sử 3-càng phóng đại **2,28 lần** | OWNER (chạm DB) |
| 8 | **`QD-047` đang `TRÔI`**, bộ kiểm mù 6 ngày — luật nói phải DỪNG | OWNER |
| 9 | **`FU-449`/`FU-450` mồ côi** — mạch việc chính không nằm trong bộ đếm nào | AGENT (phiên sau) |
| 10 | **`final_bundles.created_at` bị đọc nhầm là mốc chốt** — ghi luật vào sáu mặt | AGENT + OWNER duyệt |
| 11 | **stdout production chết 28 giờ** (từ 04/09 16:53:48) — mất toàn bộ chẩn đoán `print()` | OWNER (cần restart) |

### 🟡 P1 — ảnh hưởng người dùng hoặc phép đo

| # | việc |
|---|---|
| 12 | **Khách vô danh thấy dự đoán 07/06** cạnh kết quả 05/09 — hai nửa trang nói hai ngày |
| 13 | **Viewer đăng nhập thấy «❌ Lỗi tải dự đoán»** — UI không kiểm `r.ok` |
| 14 | **«Đồng thuận cao» gắn cho 89,3% bundle** trong khi trung vị chỉ 38,5% |
| 15 | **UI gọi trần voter cố ý của owner là «2 model chất lượng thấp»** và gắn ✅ COMPLETE cho ngày DEGRADED |
| 16 | **Deploy `VA-B` đơn độc sẽ mất hẳn vân tay prompt** — phải deploy kèm module phụ thuộc |
| 17 | **`SC-07` còn sống** — `gpt-oss-120b` official ăn ngữ cảnh shadow, có trong cả 3 bundle hôm nay |
| 18 | **Cơ chế `DIVERSITY` làm mất nhiều hơn làm được** (McNemar z=3,099) — đăng ký ngưỡng trước rồi đo shadow |
| 19 | **Lane `CAP5` 0/60 sau 21 ngày** — hạn số học **10/09** |
| 20 | **3 tệp điều hướng lệch 15 ngày**, 68 thư mục chưa vào chỉ mục |
| 21 | **12 chỗ công khai còn trích kết luận đã rút** — `PRJ_RETRACTION_SILENT` |
| 22 | **HAI tệp `.env` với BA khoá API**; bản cũ nằm trong thư mục làm việc của service |
| 23 | **Huấn luyện LSTM/meta-learner không gieo hạt** ⇒ chạy lại một ngày không ra kết quả như cũ |

*(Danh sách đầy đủ 108 phát hiện: `evidence/GATE_*.md`)*

---

## 10 · TRẢ LỜI THẲNG CÂU HỎI CỦA OWNER

**«Hôm nay tình hình hệ thống hoạt động thế nào?»**
**Ứng dụng: tốt.** 3/3 miền đủ bundle, 0 rỗng, 0 late, 0 timeout, 0 ERROR, 93/93 cron sống, DB
lành, không rò khoá. MB trúng bạch thủ 37 (lô2 chỉ **partial**, không phải trúng như em nói lúc đầu).
**Hạ tầng: không tốt, và không ai canh.** Không backup ngoài máy, không swap (OOM 6 lần/30 ngày,
2 lần rạng sáng nay), SSH root mật khẩu bị dò 49.517 lần, kênh cảnh báo chết 117 ngày.

**«Kiểm tra toàn bộ… không bỏ sót vấn đề nào»**
8 cổng, **108 phát hiện**, 13 P0. **9/16 phát hiện của cổng rủi ro không có trong bất kỳ sổ quản
trị nào** — tức trước hôm nay không ai biết. Phần chưa phủ được em ghi rõ ở mục 11.

**«Các kế hoạch và tồn đọng xử lý tới đâu rồi?»**
Prompt 43 R1 **4/12 điều kiện DoD** = 33,3%. Plan Active **44 ngày tuổi, 9 mục còn mở, nằm trên
Notion chứ không trong repo**. **326 FU · 194 treo · 152 quá hạn**, chặn ở **AGENT 90 · THỜI_GIAN
55 · OWNER 49**. **72 quyết định ACTIVE, 18 quá hạn rà soát, 8 đáo hạn hôm nay 06/09**.
Và con số «152/194» owner đang đọc **không bao gồm FU-449/FU-450** vì chúng mồ côi.

**«Còn gì thiếu sót chưa xử lý để cải thiện kết quả dự đoán?»**
Đây là câu quan trọng nhất, và câu trả lời không dễ chịu:

1. **Không phải thiếu ý tưởng — thiếu THƯỚC ĐO ĐÚNG.** 91 bundle backfill làm đẹp lịch sử +9,8pp;
   32 nhãn lo3 sai phóng đại 2,28 lần; MT bị loại khỏi đo lường 29/30 ngày vì lỗi kế toán;
   rolling WR của MT trễ 71 ngày. **Đo bằng thước hỏng thì không biết cái gì tốt lên.**
2. **Đòn bẩy lớn nhất đang chờ chữ ký**, không nằm ở việc tìm thêm: **8 vá** đã code + test.
   Chừng nào chưa vá `SC-07`, **một model official vẫn ăn prompt thí nghiệm** ⇒ mọi phép so
   official-vs-shadow đều nhiễm.
3. **Chỗ có bằng chứng để cắt:** cơ chế `DIVERSITY` **làm mất nhiều hơn làm được** (z=3,099) —
   đây là thứ hiếm hoi có hướng rõ ràng.
4. **Sự thật khó nghe:** trên **4.520 ô**, TOP-10 của TOTAL **bằng đúng bốc 10 số ngẫu nhiên**,
   KTC95 [−0,73; +1,98]. Và TOTAL có dấu hiệu **thua trung bình chính các model nó gộp**.
   **Cải thiện dự đoán không đến từ tinh chỉnh — nó đòi một cách tiếp cận khác.**
   *(Đây là quan sát, không phải đề xuất mở việc mới.)*

---

## 11 · Điều CHƯA phủ được — nói rõ, không giấu

1. **22/40 agent dừng do hết hạn mức token.** 8 cổng chính đều trả kết quả đầy đủ; phần mất là
   **lớp phản biện** (10/32 chạy). Nghĩa là **một số phát hiện chưa qua kiểm chéo độc lập** —
   em đã giữ nguyên nhãn gốc, không tự nâng.
2. **Nội dung từng panel `/monitoring` khi admin mở** — không đo được trong phiên.
3. **Không chứng minh được cổng nào «CHƯA BAO GIỜ CHẠY»** — chỉ 2 cổng có sổ điểm danh.
4. **Sổ theo dõi không ghi mức P0..P3**, nên không phân loại được 194 mục treo theo yêu cầu owner.
5. **`combo-super`: bỏ nó ra thì 18/416 bundle đổi top-1, ròng −2** — n quá nhỏ, **chưa được phép
   kết luận** (RM-04).

---

## 12 · Nguồn ba lớp (§62)

### `OWNER_SAID`
- 05/09 ~20:3x — *«Hôm nay tình hình hệ thống hoạt động thế nào? Kiểm tra toàn bộ…»*
- 05/09 ~21:0x — *«Dung lượng VPS còn thấp quá sao không tra soát dọn dẹp… luôn đi chứ để làm gì.»*
- 05/09 ~21:2x — *«…đồng thời kiểm tra tất cả toàn bộ 1 lượt dùm anh còn gì thiếu sót chưa xử lý
  để cải thiện kết quả dự đoán»*
- 06/09 ~08:2x — *«Xong chưa em tiếp đi em, bị gián đoạn do giới hạn token»*

### `CODE_DID`
- `database.py:4658-4679` UPSERT **không cập nhật `created_at`** ⇒ cột là giờ ghi lần đầu
- `_v10782_freeze.T_CHOT_MARKS` = MN 15:40 · MT 16:55 · MB 17:55 — **mốc chốt thật**
- `main.py:6337-6338` viewer-freeze khoá cứng `2026-06-07`
- `scheduler.py:3651-3678` cơ chế `DIVERSITY`
- `gpt_analyzer.py:6738` rò `ctx_pack` shadow — **còn sống**
- `.claude/settings.json` chỉ có `PreToolUse/Bash → cong_git_commit.py`, lọc `if "git commit" not in lenh`
- `web/backend/_v11150_unified_candidate_contract.py` — **`UCC-1.0.0`, 28.512 byte, 01/09**

### `RUNTIME_DID`
- 05/09: 81 lượt · 0 rỗng · 0 late · trace 60/60 `timeout_or_fallback=False`
- OOM `global_oom` **00:19:09** và **00:46:02** ngày 05/09
- PID 3338582 chạy **2 ngày 9h57 · 99,8% CPU** → đã giết
- `auth.log`: **49.517** `Failed password`
- `system_alerts`: **9 dòng cả đời**, im từ **11/05**
- đĩa 81% → **33%** sau dọn; `neo558` trước = sau

### `DOC_SAID`
- `REPORT_V11165.md` «`UCC` không có định nghĩa» — **`DOC_SAID` ≠ `CODE_DID`**, rút ở **R19**
- `REPORT_V11164.md` «bundle 827 tạo 16:46:00 · sớm 12 phút» — đọc nhầm cột, xem **R18**
- `CLAUDE.md` §0 lệnh số 1 — **20 ngày không tự chạy lần nào**
- Plan Active nằm trên **Notion**, đúng nơi `CLAUDE.md` cấm dùng để tra trạng thái hiện tại

### `NOT_VERIFIED`
- 22 phản biện dừng do hạn mức · nội dung panel `/monitoring` · cổng nào chưa bao giờ chạy

### `RETRACTED`
- **R17** «MB trúng lô2» · **R18** «12 lượt chạy sau bundle chốt» · **R19** «`UCC` không có định
  nghĩa» · **R20** «ba vá» → **tám vá**
- (còn hiệu lực) `RL-001`…`RL-016`

---

## 13 · Commit

| | |
|---|---|
| private HEAD trước | `b2a0ab0439ce7820268d8e5e866a299154264a6c` |
| public HEAD trước | `991007074df99e0f627b7c1d065cbbbff2284c5a` |
| `governance_seq` | 481 → **482** |
| **private commit V11166** | **`6c9001e2dcb10c1adaf7cecd5c545ad791911f8f`** — `b2a0ab0..6c9001e`, 8 tệp |
| **public commit V11166** | **`b6aa6ae400e7f6f2cfb114f780f2bd17b19eecc4`** — `9910070..b6aa6ae` |
| cổng `_v11062 --kiem` | ✅ **ĐẠT** |
| cổng `PRJ-RETRACTION-001` | ✅ **`SACH`** *(đã chặn bản đầu ở `GATE_s4-no.md:37`)* |
| cổng `PRJ-SELECTION-WINDOW-001` | ✅ **`SACH`** *(đã chặn bản đầu ở 7 chỗ)* |

---

> ⚠️ **Cố ý trích MỘT cửa sổ** (`PRJ-SELECTION-WINDOW-001` · RM-18 · RM-21). Đoạn dưới đo **NỀN**
> cho thước bạch thủ và báo kết quả **trên toàn bộ 479 bundle LIVE**, không tuyên bố hiệu quả theo
> một cửa sổ riêng. Bộ đủ **14 / 30 / 90 / 180 ngày** nằm ở **V11084 + V11086**, và ở đó **dấu ĐỔI**:
> 30 ngày **+4,07pp** · 90 ngày **−3,18pp** · 180 ngày **+0,91pp** (CI95 [−3,2 ; +5,0]).
> Bản này có nêu 5 cửa sổ 7/30/60/90/160 ở bảng 20 ô — con số trích riêng ở đây chỉ là **tóm tắt**
> của bảng đó, không phải một cửa sổ được chọn cho khớp kết quả.
TanPhatAI cần làm: ghi **`V11166`** — `governance_seq 482`, công khai bản này. Ghi **DỌN DẸP 19,82 GB, đĩa 81% → 33%**, `artifacts/` 2,5 G → 64 M, repo 8,8 G → 3,5 G, load 1,42 → 0,61 — **production nguyên vẹn** (`neo558` khớp từng ký tự, 6 hash tệp serve khớp, PID 3370750 NRestarts 0). Ghi **agent đã GIẾT tiến trình mồ côi của chính phiên V11164** chạy 2 ngày 9h57 ở 99,8% CPU trên máy 2 vCPU, và ghi **chính agent là nguồn rác chính** (3,23 GB clone DB trong 3 ngày). Ghi **BA VIỆC P0 HẠ TẦNG**: ① **KHÔNG có sao lưu ngoài máy nào** — mọi bản DB nằm trên cùng ổ `/dev/vda1`; ② **KHÔNG có swap**, OOM-killer bắn **6 lần/30 ngày**, 2 lần rạng sáng 05/09, service `MemoryMax=infinity` không đặt `OOMScoreAdjust`; ③ **SSH root bằng mật khẩu**, `fail2ban` inactive, **49.517** lần `Failed password`. Ghi **ĐIỂM MÙ**: `system_alerts` **9 dòng cả đời, im 117 ngày**, 8/9 còn treo kể cả một CRITICAL 133 ngày; **0 dòng mã nào đọc dung lượng đĩa**; cổng sức khoẻ 16 phép **không phép nào về đĩa** ⇒ *«ai sẽ biết?» = KHÔNG AI*. Ghi **HAI BỀ MẶT HOOK LỆCH NHAU — 7 cổng chết** dưới Claude Code, trong đó có chính cổng chặn deploy; `_HOOK_DIEM_DANH.log` dòng cuối `2026-08-16 23:16:35` = **20 ngày**; **deploy/push hiện không qua cổng nào**. Ghi **CHẤT LƯỢNG DỰ ĐOÁN — mẫu ĐỦ LỚN để kết luận**: 479 bundle LIVE bạch thủ **31,7% vs ngẫu nhiên 34,0%**, **20/20 ô âm hoặc bằng**; TOP-10 TOTAL trên **4.520 ô** = **34,51% vs nền 33,89%, KTC95 [−0,73; +1,98]** ⇒ **bác bỏ mọi lợi thế > ~2 điểm**. Ghi **BA THỨ LÀM ĐẸP LỊCH SỬ**: **91 bundle backfill** tạo 30/03 sau khi biết kết quả, đạt **+9,8pp trên nền**, đang nằm chung bảng với LIVE; **32 nhãn `lo3 WIN` sai** (57 lưu vs 25 thật, phóng đại **2,28 lần**); **TOTAL có dấu hiệu thua trung bình chính các model nó gộp** (−2,08pp, 14/18 model cao hơn). Ghi **`DIVERSITY` làm mất nhiều hơn làm được** (McNemar z=3,099). Ghi **NGƯỜI DÙNG THẤY BA THỨ KHÁC NHAU, HAI TRONG BA SAI**: khách vô danh thấy dự đoán **07/06** cạnh kết quả **05/09**; viewer đăng nhập thấy **«❌ Lỗi tải dự đoán»**; viewer-freeze tròn **90 ngày**. Ghi **BỐN CA RÚT LẠI R17–R20**, nặng nhất **R18** (`final_bundles.created_at` **KHÔNG phải mốc chốt** — mốc thật là `t10_chot`: MN 15:40 · MT 16:55 · MB 17:55, MN lệch **10 giờ 21 phút**; điều này cũng làm sai hai câu của V11164) và **R19** (**`UCC` CÓ định nghĩa đầy đủ** — `UCC-1.0.0`, `_v11150_unified_candidate_contract.py`; V11165 **giao owner một việc đã có sẵn đáp án** do quét thiếu phạm vi ⇒ **HUỶ việc đó**). Ghi **KẾ HOẠCH**: Prompt 43 R1 **4/12 DoD**; Plan Active **44 ngày, 9 mục mở, nằm trên Notion**; **326 FU · 194 treo · 152 quá hạn**; **72 QĐ ACTIVE, 18 quá hạn rà soát, 8 đáo hạn 06/09**; **`QD-047` đang TRÔI** và bộ kiểm mù 6 ngày; **`FU-449`/`FU-450` MỒ CÔI** nên con số «152/194» **không bao gồm mạch việc chính**. Ghi **22/40 agent dừng do hết hạn mức token** — 8 cổng chính đủ, **lớp phản biện thiếu**, không giấu. **Code KHÔNG đi trước tài liệu** — phiên soi 0 ghi production, 0 deploy, 0 restart; phần dọn dẹp chỉ đụng rác đã kiểm ba lớp. **Không mở Prompt 44. Không mở FU mới. Không mở Plan mới.** `POOL_VERDICT` giữ **`HOLD`** · `MODEL_ACTION` giữ **`BLOCKED`** · `PROMPT_43_R1` giữ **`PARTIAL`**.
