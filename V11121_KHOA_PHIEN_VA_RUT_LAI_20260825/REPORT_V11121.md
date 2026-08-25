# V11121 — KHOÁ PHIÊN GHI · CỨU `GĐ-7` · BA CANDIDATE CARD · `§55` QUY ƯỚC THỨ TƯ — VÀ **RÚT LẠI HAI CÂU CỦA CHÍNH `V11119`**

**Ngày:** 25/08/2026 · **Commit riêng:** `2d973c7` · **Commit công khai:** *(bản này)* ·
**Trạng thái:** `READ-ONLY` với production — không deploy, không restart, không ghi DB

---

## 1. Tóm tắt

Prompt 36 mục `P0`/`P2`/`P3`/`P4`. Tám làn đọc song song `READ-ONLY` (**1,07 triệu token · 336 lượt
gọi công cụ · 0 lỗi**), Coordinator giữ quyền ghi.

**Bốn kết quả nặng nhất:**

1. 🔴 **Hai câu của chính `V11119` phải rút lại** — `R6` *«26 nhãn git-only»* **không tái lập được**;
   `R7` *«chỗ làm cổng `_v11062 K1` mù»* **sai từ `V11082`**. Đã rút lại **đúng chỗ đã công bố**.
2. 🔴 **`R5` xác nhận — và có BA lỗ hổng, không phải hai.** Lỗ thứ ba chưa ai nêu: cổng sắp theo
   **số hiệu**, không theo **thời gian commit** ⇒ `V11037c` commit **hôm nay** rơi ngoài cửa sổ
   **ngay trong ngày tạo**.
3. 🟢 **Dựng xong khoá phiên ghi**, thử chặn hai chiều **8/8 ĐẠT** — và **tái lập 100%** vụ lẫn nhãn
   commit chiều 25/08 bằng `git`.
4. 🟢 **`T1` (sàn `b+c ≥ 96`) là BẤT KHẢ THI** trong cửa sổ `26/08 → 23/09` — chứng minh bằng **trần
   số học**, không phụ thuộc ước lượng. ⇒ `NO_PROMOTION_INSUFFICIENT_POWER` tại `D3` là **biết trước
   từ hôm nay**.

## 2. Owner yêu cầu gì (nguyên văn)

> *« **IV. P0 — PREFLIGHT VÀ SINGLE WRITER** … 3. Dựng session lease: owner/session/PID/start/TTL.
> … 5. Thử chặn hai writer và thử đường sạch. »*
>
> *« **VIII. P3 — HARD STOP** … 26/08→23/09 tối đa khoảng 87 region-days < sàn 96. Phải ghi rõ bất
> khả thi nếu dùng prospective-only. … Không hạ ngưỡng. Không tự kéo dài. »*
>
> *« **IX. P4 — GOVERNANCE** … 3. Xác nhận hoặc bác R5 bằng output thật. 4. Cứu "GĐ-7 mười bản vá"
> thành tài liệu có đủ 10 mục, code anchor, được/mất, test, rollback. … 6. **Không bù report cho
> V11077/V11079.** … 10. Bổ sung `scheduler_logs.log_time=UTC` đúng sáu mặt. »*
> — prompt 36, `25/08/2026`

## 3. Đào bới / phát hiện

### 3.1 · 🔴 RÚT LẠI `R6` — *«26 nhãn version chỉ có ở `git log`»*

| phần | nội dung |
|---|---|
| **chỗ gốc** | `REPORT_V11119.md §3.3` · `CHANGELOG` khối `V11119` · `CURRENT_TRUTH_SSOT` |
| **nguyên văn câu sai** | *«Và chiều ngược lại — **26 nhãn version chỉ có ở `git log`**, không có mục CHANGELOG»* |
| **điều đúng** | Không phạm vi theo **số hiệu** nào ra `26`: cổng **12** · thô `≥V11062` **21** · gộp hậu tố toàn lịch sử **54** · thô toàn lịch sử **135**. Chỉ ra `26` khi cắt theo **NGÀY COMMIT `≥ 2026-08-10`** — mốc **không được khai** ở đâu cả. Vi phạm `RM-11` |
| **tái lập** | `_v11062_nang_version.muc_git_log()` ∖ `muc_changelog()` → **12** |
| **đã dựa vào đâu** | Mục `P0-4` của plan *«bù mục CHANGELOG cho 26 bản»* — khối lượng sai. Và **12/12** nhãn git-only **ĐỀU CÓ** báo cáo công khai ⇒ **không có việc bù nào** |

### 3.2 · 🔴 RÚT LẠI `R7` — *«chỗ làm cổng `_v11062 K1` mù»*

| phần | nội dung |
|---|---|
| **nguyên văn câu sai** | *«Đây chính là chỗ làm cổng `_v11062 K1` mù: nó lấy worklist từ `muc_changelog()`»* |
| **điều đúng** | Worklist **đã là** `CHANGELOG ∪ git log` **từ `V11082`** (`_v11062_nang_version.py:207-212`); mã ghi rõ `chi_git` là **GHI CHÚ**, không phải lỗi (`:249-258`) |
| **tái lập** | `--kiem` → `chỉ-có-ở-git 12 (THIẾU HISTORY: 0)` · `✓ ĐẠT` |
| **đã dựa vào đâu** | Mục `P3-2` *«vá `_v11062 K1`»* — **việc đó không tồn tại**, đã vá 8 ngày trước |

### 3.3 · 🔴 `R5` XÁC NHẬN — **BA** lỗ hổng

Cùng một phiên, cùng một phút, cùng trạng thái kho:

```
_v10921_report_gate.py V11119   → soi 1 bản · "MỌI PHIÊN BẢN ĐỀU CÓ BÁO CÁO" · thoát 0
_v10921_report_gate.py          → soi 8 bản · V11117 V11115 V11112 THIẾU  · thoát 1
```

| # | lỗ hổng | neo mã | thiệt hại **đo được** |
|---|---|---|---|
| ① | băng-rôn **toàn cục** in khi worklist chỉ có **một** phần tử | `:229` · `:355-356` | `CLAUDE.md §0` **đang dạy đúng chế độ mù** (`<VERSION>`) |
| ② | cửa sổ cắt cứng `[:8]` | `:84` · `:144` | CHANGELOG **460** mục ⇒ **452** bản không bao giờ soi lại. Trong **40** bản gần nhất có **11** thiếu, cổng báo **3**. Tám bản vô hình: `V11111` `V11107` `V11100` `V11099` `V11096` `V11094` `V11093` `V11087B` |
| ③ | **MỚI** — sắp theo **SỐ HIỆU**, không theo **thời gian commit** | `:141-144` | `V11037c` commit **HÔM NAY** nhưng số `11037` ⇒ rơi ngoài cửa sổ (bắt đầu `11112`) **ngay trong ngày tạo**; kho công khai **không có** `REPORT_V11037C.md` |

Thêm: cổng **không được nối vào hook nào** — `grep _v10921` trong `.cursor/` và `.claude/` ra **0 dòng**.

### 3.4 · 🟢 Vụ lẫn nhãn commit 25/08 — **tái lập 100% bằng `git`**

```
6487e6d  18:42:46  nhãn «V11037c» → khối CHANGELOG V11118 (diff dòng 28) + V11037c (dòng 54)
76c391b  18:42:49  nhãn «V11118»  → 6 tệp, 0 dòng CHANGELOG
```

Writer **A** `prepend()` khối A · writer **B** `prepend()` khối B **đè lên trên** · **A**
`git add CHANGELOG.md` quét **cả hai** rồi commit dưới nhãn A. Ba giây sau **B** commit thì
CHANGELOG **không còn gì để stage**.

**Chỗ nghẽn KHÔNG phải `git commit`** mà là `_doc_prepend.prepend()` — `:80` đọc `old` → `:95` ghép
→ `:105` `os.replace`. Hai tiến trình đọc cùng `old` thì **bản rename sau nuốt bản trước**, và phép
chắn duy nhất (`len(merged) < len(old)`, `:97`) **không bao giờ nổ** vì hai khối cộng dồn luôn dài ra.

### 3.5 · 🔴 BA lỗ hổng cổng khác, đo được trong chính phiên này

1. **Hook gọi bằng ĐƯỜNG DẪN TƯƠNG ĐỐI.** Chạy với cwd của **shell**; chỉ cần một lệnh `cd` vào thư
   mục con là Python báo `can't open file` và **thoát 2** — với `PreToolUse`, **thoát 2 = CHẶN**.
   Hỏng **cả hai chiều**: chín cổng con **không chạy lần nào**, mà agent lại thấy **mọi lệnh Bash bị
   từ chối**. **Đã vấp thật** — nửa phiên phải chuyển sang công cụ khác. → **ĐÃ VÁ**.
2. **Hook không có sổ điểm danh** — chỉ `print(..., file=sys.stderr)`, **0** lời gọi ghi tệp ⇒
   **không ai truy ngược được** nó có chạy lúc `18:42:46` hay không (`RM-15`). → **ĐÃ VÁ**.
3. 🔴 **Bốn hook Cursor đã CHẾT 9 NGÀY** với phiên Claude Code — `.cursor/hooks.json` khai 4 hook
   nhưng dùng **tên sự kiện của Cursor**. Sổ điểm danh dừng ở **16/08** ⇒ toàn bộ phiên 25/08 chạy
   **không có** `truncation_guard` và `code_quality_guard`. **CHƯA VÁ** — chờ owner.

### 3.6 · 🟢 `P3` — `T1` **BẤT KHẢ THI**

`26/08 → 23/09` = **29 ngày × 3 miền = 87** region-day (owner ghi `87`: **đúng chính xác**).

| trần | phép tính | kết quả |
|---|---|---|
| **số học** | `b+c` đếm region-day **bất đồng kết quả**, mỗi region-day góp **tối đa 1** | `b+c ≤ 87 < 96` — **không phụ thuộc ước lượng nào** |
| **thực tế** | nền bạch thủ `0,3388` ⇒ `P ≤ 2p(1−p) = 0,4480` ngay cả khi đổi số **mỗi ngày** | `≈ 39,0` |
| **đo được** | `M3`: `46/423 = 10,875%` | `E[b+c] = 9,46` = **9,9%** sàn |

`P(b+c ≥ 96 | Poisson λ=9,46) = 4,26 × 10⁻⁶¹`. Cần **295 ngày** ⇒ **16/06/2027**, tức **266 ngày
SAU `D3`**. Kịch bản trần lý thuyết (bất đồng 100% mỗi ngày) cũng cần **32 ngày** ⇒ `26/09` — **vẫn
muộn hơn `D3` ba ngày**. `D2` `09/09` chỉ có **45** region-day ⇒ `E[b+c] = 4,89`.

### 3.7 · 🔴 Trùng nguồn **sâu hơn** tầng ensemble — chưa ai nêu

`ml_predict.py:23-24` import `run_full_analysis` (`statistical_analyzer`) **và**
`extract_prediction_features` (`meta_predict`); dòng `62`/`68` gọi đúng hai hàm đó, **chú thích tại
chỗ** ghi *«same pipeline as Meta-Learning»*. ⇒ `xgboost` / `random-forest` / `meta-learning` dùng
**cùng bộ ứng viên và cùng bộ đặc trưng**, chỉ khác **bộ phân loại** — **không phải bốn nguồn độc
lập kể cả khi bỏ hết ensemble**. Ba tầng đếm trùng trong 15 suất official.
**Đo được: 15 model rút còn 6–7 họ.**

🔴 DB **không có** trường dòng dõi nào. ⛔ `provider` **không thay được** family: `openrouter` gộp
9 model của **≥5 hãng**; `local` gộp 4 ML gốc với 3 ensemble dẫn xuất từ chúng. Bản đồ family thật
duy nhất (`_v10872_deherd_selector.py:68`) là **`shadow_only`** và **thiếu 6/27** model.

### 3.8 · 🔴 Nhãn *«nhiễm `run_source` 21,8%»* — số ĐÚNG, **nhãn SAI LỚP**

Tử số tái lập **chính xác** (`1.630`/`111` ngày–miền). Nhưng **`shadow_auto_eval` góp ĐÚNG `0/1.630`**:
`111` ngày–miền nằm trọn `28/02 → 05/04`, còn `shadow_auto_eval` **chỉ bắt đầu ghi từ `14/04`** ⇒
hai khoảng **không giao nhau**, bằng 0 theo **cấu trúc**. Nhiễm thật là **`auto_daily` 83,7%**.
Không phải lookahead (`13/1.630` = `0,8%`). Nhánh **«sạch» còn nhiễm NẶNG HƠN: `26,1%`**.
🔴 `RM-11`: công cụ sinh ra `21,8%` **không có trong kho**; thư mục `V11116_*` **không có `evidence/`**.

### 3.9 · 🟢 `§55` — quy ước giờ **thứ tư**, ba neo độc lập

Job `t10_chot` có giờ VN **khoá cứng** `MN 15:40 · MT 16:55 · MB 17:55`; trong `scheduler_logs` hiện
ở **`08:40` · `09:55` · `10:55`** — lệch **đúng 7 giờ ở cả ba**. ⚠️ **Hai bảng naive, hai nghĩa ngược
nhau**: `final_bundles` naive **đã là giờ VN** (cấm cộng 7), `scheduler_logs` naive **là UTC** (bắt
buộc cộng 7) — nhìn chuỗi chữ **không phân biệt được**.

### 3.10 · Ma trận khuyết Algorithm Card

`docs/AS_IS_OUTPUT_ALGORITHMS_20260824.md` có **đúng 4 Algorithm Card** phủ đủ 4 sản phẩm. Ma trận
`4 sản phẩm × 14 bước`: **43 ô ĐỦ · 4 MỘT PHẦN · 6 THIẾU · 3 KHÔNG ÁP DỤNG**. Hai bước thiếu
(`parser` và `combo-super`) **dùng chung cho cả ba sản phẩm có model** ⇒ chỉ tốn **2 bài viết**.

## 4. Hướng xử lý và vì sao chọn

| lối | vì sao |
|---|---|
| khoá ở `git commit` | ❌ **không đủ** — vụ 25/08 xảy ra ở **lúc `prepend()`**, không phải lúc commit |
| khoá ở `prepend()` | ✅ **đúng chỗ** — nhưng đụng đường ghi của mọi tài liệu ⇒ để **nhóm B**, cần owner ký |
| **cổng con thứ 0 ở `git commit` + thiết kế tầng `prepend()`** ✅ | chắn cuối **dựng ngay được**, thử được, gỡ được; tầng sớm trình owner |

Lease đặt ở `.git/lottery_writer.lease`: Git **không bao giờ** theo dõi `.git/`, riêng cho từng
clone. `docs/` và `backups/` **sẽ vào Git** ⇒ cấm. `artifacts/` đã gitignore nhưng **bị đồng bộ lại**
⇒ dễ mất lease giữa chừng.

## 5. Đã làm gì

| tệp | thay đổi |
|---|---|
| `web/backend/_v11120_session_lease.py` | **mới** — 11 trường, `TTL 900s`, nhịp tim `60s`, danh tính từ `CLAUDE_CODE_SESSION_ID` + `CLAUDE_PID` |
| `web/backend/_v11120_thu_chan_lease.py` | **mới** — thử chặn hai chiều 5 ca + khôi phục nguyên trạng |
| `.claude/hooks/cong_git_commit.py` | thêm **cổng con thứ 0** (lease, đặt đầu để thoát nhanh) + **sổ điểm danh** |
| `.claude/settings.json` | 🔴 **sửa đường dẫn tương đối → tuyệt đối** |
| `docs/GD7_MUOI_BAN_VA_20260825.md` | **mới** — cứu 10 bản vá khỏi vết phiên |
| `docs/TOTAL_V2_CANDIDATE_CARDS_20260825.md` | **mới** — 3 card + 1 ablation |
| `CLAUDE.md` `§55` + `AGENTS.md` + `GEMINI.md` | quy ước giờ **thứ tư** |

## 6. Cổng kiểm

| cổng | kết quả |
|---|---|
| `_v11120_thu_chan_lease.py` | ✅ **8/8 ĐẠT** — `D1` chặn · `D2` **vẫn chặn** khi nhịp tim tắt mà PID sống · `D3` thu hồi + ghi sổ · `D4` cùng phiên qua · `S1`/`S2` đường sạch qua |
| hook từ **cwd khác gốc kho** | ✅ `EXIT=0` *(trước bản vá: `EXIT=2` — chặn mù)* |
| sổ điểm danh | ✅ có `CHAY` + `DAT · 9/9 cổng con qua` cho **chính commit này** |
| `_v11062_nang_version.py --kiem` | ✅ **ĐẠT** · `seq=451` · `last_version=V11121` |
| `_v10925_rule_sync_check.py` | ✅ **SÁU MẶT ĐỒNG BỘ** |
| `_v11044_cong_so_hieu.py` | ✅ **KHỚP** — cấp `V11121` |
| `_v10920_decision_ledger.py` | ✅ **0 TRÔI** · 1 không kết luận được (`QD-056`, `RM-01`) |

## 7. Vướng vấp

1. **Bash kẹt thư mục làm việc gần nửa phiên.** Một lệnh `cd web/backend` làm hook (đường dẫn tương
   đối) **thoát 2** ⇒ **mọi lệnh Bash sau đó bị chặn**, kể cả lệnh `cd` để quay lại. Phải chuyển sang
   PowerShell + công cụ đọc/grep chuyên dụng cho tới khi shell tự đặt lại.
   *Hậu quả nếu bỏ qua:* đây chính là **lỗ hổng cổng số 1** — nếu không vấp thì không phát hiện.
2. **Commit đầu lỡ đưa backup 1 MB / 22.184 dòng vào Git.** Git đã có bản trước-vá ở `de35b10` ⇒
   dư thừa vĩnh viễn. Đã gỡ (chưa push) + thêm mẫu vào `.gitignore`.
3. **Cổng commit chặn đúng lần amend** — `V11120` đã vào `git log` mà chưa có dòng `HISTORY` (`§63 K1`).
   Đây là **cổng làm đúng việc**, ghi lại để không ai đọc nhầm thành lỗi.
4. **Workflow 22 làn của phiên trước bị DỪNG** khi tiến trình thoát — chỉ **2/22** có kết quả, 6 làn
   dở dang **mất**, 14 làn chưa chạy. Đã kiểm bằng `journal.jsonl`, không suy đoán.

## 8. Gỡ về

| việc | lệnh |
|---|---|
| toàn bộ `V11121` | `git revert 2d973c7` |
| chỉ khoá phiên | xoá cổng con thứ 0 khỏi `SOI` (1 dòng) · `rm .git/lottery_writer.lease` |
| chỉ `settings.json` | đổi lại đường dẫn tương đối *(không khuyến nghị — đó là lỗi gốc)* |

Lease nằm trong `.git/` ⇒ **không vào Git**, xoá là hết. Không có migration DB.

## 9. Theo dõi tiếp

| mã | việc | ngưỡng đóng bằng số | ai chặn |
|---|---|---|---|
| `FU-438` | deploy bản vá bề mặt công khai | xem `REPORT_V11120 §9` | 🔴 **OWNER** |
| `FU-439` | cứu `GĐ-7` | ✅ **ĐÓNG** — `docs/GD7_MUOI_BAN_VA_20260825.md`, đủ 10 mục | — |
| `FU-441` *(mới)* | **4 hook Cursor chết 9 ngày** — chuyển sang `.claude/settings.json` hay bỏ | sổ điểm danh có dòng của cả 4 hook trong 1 phiên Claude Code | 🔴 **OWNER** |
| `FU-442` *(mới)* | vá cổng A55 ba lỗ hổng: worklist ba nguồn · sắp theo **thời gian** · băng-rôn nói **đúng phạm vi** | thử hai chiều: giả lập bản thiếu **ngoài** cửa sổ cũ ⇒ thoát ≠ 0; sạch ⇒ 0 | tự làm được |
| `FU-443` *(mới)* | khoá tầng **`prepend()`** (tầng sớm, bắt đúng ca 25/08) | thử hai chiều trên chính `_doc_prepend` | 🔴 **OWNER** — đụng đường ghi mọi tài liệu |
| — | **`D3` 23/09** | 🔴 **`NO_PROMOTION_INSUFFICIENT_POWER` — biết trước từ hôm nay.** Muốn đi tiếp phải **mở preregistration mới** trên thước có power đạt được | 🔴 **OWNER** |

---

## 10. BA LỚP NGUỒN (§62 · A60)

### `OWNER_SAID`
> *«Thử chặn hai writer và thử đường sạch.»* · *«Phải ghi rõ bất khả thi nếu dùng prospective-only.»*
> · *«Không hạ ngưỡng. Không tự kéo dài.»* · *«Không bù report cho V11077/V11079.»*
> — prompt 36, `25/08/2026`

### `CODE_DID`
| điều mã **thực sự** làm | bằng chứng |
|---|---|
| hai writer ghi đè nhau ở `prepend()` | `6487e6d` mang **2** khối CHANGELOG · `76c391b` mang **0** · cách nhau **3 giây** |
| hook **không chạy** khi cwd sai | từ cwd khác: `can't open file` · `EXIT=2` = chặn mù |
| hook **không có** sổ điểm danh | đọc hết 147 dòng: chỉ `print(...)`, **0** lời gọi ghi tệp |
| 4 hook Cursor **im 9 ngày** | sổ điểm danh dòng cuối `2026-08-16 23:16:36` |
| `K1` **không mù** | `--kiem` → `THIẾU HISTORY: 0` · `ĐẠT` |
| 4 ML **không độc lập** | `ml_predict.py:62,68` — *«same pipeline as Meta-Learning»* |
| `t10_chot` lệch **đúng 7h** | VN `15:40/16:55/17:55` ↔ log `08:40/09:55/10:55` |

### `DOC_SAID`
| tài liệu | nói gì | khớp code chưa |
|---|---|---|
| `REPORT_V11119 §3.3` | *«26 nhãn git-only»* · *«chỗ làm K1 mù»* | 🔴 **CẢ HAI SAI** — đã rút lại |
| `CLAUDE.md §0` | `_v10921_report_gate.py <VERSION>` | 🔴 **dạy đúng chế độ mù** |
| `CLAUDE.md §55` (trước bản này) | *«BA quy ước»* | 🔴 **THIẾU** quy ước thứ tư — đã bù |
| prompt 36 `§III` | *«Reliability history nhiễm `run_source` 21,8%»* | 🟡 **số đúng, nhãn sai lớp** — `shadow_auto_eval` góp `0/1.630` |

### 🔴 BA LỚP LỆCH NHAU
`DOC_SAID` ≠ `CODE_DID` ở **bốn** chỗ trên — hai chỗ là lỗi của chính báo cáo trước (`R6`/`R7`), một
chỗ là tài liệu vận hành dạy sai chế độ cổng, một chỗ là nhãn sai lớp trong current-truth.
`OWNER_SAID` ≠ `CODE_DID`: owner khoá *«không để hai writer cùng ghi repo»* nhưng **không có cơ chế
khoá nào tồn tại** cho tới bản này — `grep` `lock|lease|flock|pidfile` trong `.claude` + `.cursor/hooks`
ra **0 dòng**.

---

**TanPhatAI cần làm:** ghi nhận (a) **`R6` và `R7` của `REPORT_V11119` đã bị rút lại** — **đừng thi
hành** hai việc *«bù mục CHANGELOG cho 26 bản»* và *«vá `_v11062 K1`»*, cả hai **không tồn tại**;
(b) `R5` **xác nhận** với **ba** lỗ hổng, và `CLAUDE.md §0` đang dạy đúng chế độ mù của cổng A55 —
đây là việc sửa tài liệu, không chỉ sửa mã; (c) **`D3` 23/09 sẽ là `NO_PROMOTION_INSUFFICIENT_POWER`
— biết trước từ hôm nay** bằng trần số học `87 < 96`, nên đừng chờ tin vui ở mốc đó; (d) nhãn
*«nhiễm `run_source` 21,8%»* trong current-truth **sai lớp** — số đúng nhưng `shadow_auto_eval` góp
`0/1.630`, nhiễm thật là `auto_daily` `83,7%`; (e) mở `FU-441` `FU-442` `FU-443`, đóng `FU-439`.
