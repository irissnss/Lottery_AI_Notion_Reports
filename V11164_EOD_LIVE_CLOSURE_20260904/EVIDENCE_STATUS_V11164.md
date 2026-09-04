# EVIDENCE_STATUS_V11164 — CHỈNH LỚP BẰNG CHỨNG CỦA V11164

> **Sinh bởi:** V11165 · GATE 1 · làn sóng 1 · `2026-09-04` · `CURRENT_ACTOR = CLAUDE_CODE`
> **Việc của tệp này:** dán nhãn và đối chiếu lớp bằng chứng V11164. **KHÔNG sửa một ký tự nào**
> trong các raw artifact — giá trị của chúng nằm đúng ở chỗ chúng **chưa** được sửa.
> **Không nâng tầng** cho bất kỳ kết luận nào của V11164.
>
> **Nguồn đo lại:** clone bất biến `/root/Lottery_AI_Test/artifacts/v11165_immutable.db`
> `sha256 = c3c2f5688f0abbfc34b6fcdf9a0ef689cc509b0d4f9839b19e00ceb6efebb6e2` (mở `mode=ro`).
> 6/6 hash mã đang serve **khớp GATE 0** ⇒ không có drift giữa lúc chụp và lúc đo lại.

---

## 1 · Vì sao phải có tệp này

Bộ bằng chứng V11164 có **ba lớp chồng lên nhau**, và ba lớp đó **không nói giống nhau**:

| lớp | tệp | nói gì |
|---|---|---|
| **raw, TRƯỚC phản biện** | `evidence/GATE_g*.md` (8 tệp) | kết luận đầu tiên của từng cổng |
| **lớp sửa** | `evidence/PHAN_BIEN_32_SUA_LAI.md` | 32 phản biện: 7 `DUNG` · 25 `DUNG_MOT_PHAN` · 0 `SAI` |
| **canonical** | `REPORT_V11164.md` | đã áp mọi hiệu chỉnh của lớp sửa |

Ai mở thẳng một tệp `GATE_g*.md` sẽ đọc được **những con số đã bị thay** và **những mệnh đề đã bị
rút lại** — mà trong tệp đó **không có dấu hiệu nào báo điều đó**. Đây không phải giả định: bên
dưới có **ba mâu thuẫn còn sống** giữa chính các tệp evidence với nhau.

---

## 2 · Dán nhãn raw artifact

Tám tệp dưới đây mang nhãn:

```
RAW_PRE_REVIEW_ARTIFACT · NOT_CANONICAL_IN_ISOLATION
SUPERSEDED_BY = REPORT_V11164.md + evidence/PHAN_BIEN_32_SUA_LAI.md
```

**Cách đọc đúng:** dùng raw artifact **chỉ** để truy vết *một kết luận đã hình thành thế nào*.
Mọi con số đưa ra ngoài phải lấy từ `REPORT_V11164.md` sau khi đối chiếu bảng ở mục 3.

| tệp | sha256 (hiện tại) | bytes | tự khai tầng | tự khai tên | cảnh báo |
|---|---|---|---|---|---|
| `evidence/GATE_g1-region-ledger.md` | `651813d3669ba773d3a3c37e49a5cf5f730e55a409b1c6f65ccbaeed536275f9` | 8.701 | `EVIDENCE_COMPLETE` | `g1-region-ledger` | so sánh MT chọn lọc → **CC-12** |
| `evidence/GATE_g2-prompt-routing.md` | `d6ccccd5f3e63614ad9d1072c3247a2bcd95c90e4de842a12e2e8a5917fe4efc` | 10.943 | `PARTIAL` | `gate2` | — |
| `evidence/GATE_g3-model-universe.md` | `81fae9dc4f7bc2902556e98136083660bd860818345520f27d5e0488dd736eeb` | 9.362 | `EVIDENCE_COMPLETE` | **`gate4`** | số hiệu tự khai lệch → **CC-13** |
| `evidence/GATE_g4-total-final.md` | `920f471ec07d24654e2f9bb0685d9b9ee8ca05bc617d9c0812b246e90886a12d` | 11.957 | `EVIDENCE_COMPLETE` | **`gate6`** | 🔴 đọc lướt sẽ ngược hẳn mục 11 → **CC-13** |
| `evidence/GATE_g5-anomaly.md` | `5ee2e4c278e889ce8c06cd9e23a27adf3e6ace3a49450e709ad15a25dca4531f` | 8.749 | `EVIDENCE_COMPLETE` | `g5-anomaly` | 🔴 giữ **88/88 · 50.670** đã bị thay → **CC-05** |
| `evidence/GATE_g6-debt.md` | `c60315a4bf7886e67840d91e29260430be8780ad8cc8cae3e8e10a729d916790` | 12.461 | `PARTIAL` | `g6-debt` | 🔴 dòng 35 mang mệnh đề **đã rút lại** (RL-010) → **CC-07** |
| `evidence/GATE_g7-stdio.md` | `da81cb5168d62ce78ca6edce88802af8b479bef3e5acefd24b9296f48908477b` | 7.685 | `EVIDENCE_COMPLETE` | `g7-stdio` | 🔴 dòng 5 nói **quá phạm vi** socket (RL-013) → **CC-06** |
| `evidence/GATE_g8-abc.md` | `201ffdcb1cae4855c6a6481f1c99ff4c41ecd96b58fabed19f613889d9aef85f` | 11.972 | `EVIDENCE_COMPLETE` | `gate8` | ghi «**ba** nghĩa» trong khi REPORT ghi «**bốn** lớp» → **CC-10** |

**Không phải raw** — hai nguồn canonical và hai tệp bất biến:

| tệp | sha256 | nhãn |
|---|---|---|
| `REPORT_V11164.md` | `d0a279328e8f24c1aaa70141026f483be4b73f5215813388a655766000a02816` | `CANONICAL` |
| `CONVERSATION_CONTEXT_V11164_20260904.md` | `4fbc0dd919b0896965eefae85c6e71adfdd0fb7539288a903e7a0ceba8a531f4` | `CANONICAL` |
| `evidence/PHAN_BIEN_32_SUA_LAI.md` | `e37813a3bff4e92fe2520167c83bfc7a2821e416b9fe26578855a86f74355f1a` | `REVIEW_CORRECTION_LAYER` |
| `evidence/v11164_index.json` | `7a0dc6e0719319df3edcf3d023b7567a3e2c07406bab6d3e652dd9e2a65b50c8` | `IMMUTABLE_INDEX` |
| `evidence/v11164_gate0_manifest.json` | `e11069274a7d9da8249d746274a4f375fa410b6460f99414e6fa0024e8f4636f` | `IMMUTABLE_MANIFEST` |

---

## 3 · Bảng claim correction — 13 mục

### CC-01 · «8 cổng» ≠ «8/8 đạt»

- **Chỗ gốc:** `REPORT_V11164.md` dòng 5 · `CONVERSATION_CONTEXT` dòng 12, 14, 33, 94
- **Nguyên văn:** *«8 cổng · 40 agent · 32 phản biện độc lập · 84 phát hiện · 196 artifact»*
- **Đọc ĐÚNG:** 8/8 cổng **đã chạy** đến cùng, 40/40 agent hoàn tất.
- **Đọc SAI:** 8/8 cổng **đều PASS**.
- **Thực:** **6 `EVIDENCE_COMPLETE`** (`g1` `g3` `g4` `g5` `g7` `g8`) + **2 `PARTIAL`** (`g2`
  prompt-routing · `g6` debt). `GRAND_OVERHAUL_CHAIN = PARTIAL`.
- **Bằng chứng:** `grep -n 'tang=' evidence/GATE_g*.md` → 6 + 2; đối chiếu `REPORT_V11164.md` mục 11.
- **Phân loại:** `EXPECTED_BEHAVIOR` — báo cáo gốc **đã đúng ở mục 11**; rủi ro nằm ở cách đọc
  băng-rôn đầu bài.

### CC-02 · Năm tầng: tầng 5 KHÔNG ĐO ĐƯỢC

- **Chỗ gốc:** `REPORT_V11164.md` mục 1, hàng bảng *«Năm tầng raw → UI»*
- **Nguyên văn:** *«Năm tầng raw → UI | 🟢 tầng 1 = 2 = 3 = 4, không có điểm lệch»*
- **Đọc ĐÚNG:** **bốn** tầng (raw tái lập = persisted TOTAL = published FINAL = override-adjusted)
  không lệch.
- **Đọc SAI:** *«năm tầng đều không lệch»*.
- **Thực:** **tầng 5 (UI) KHÔNG ĐO ĐƯỢC** — bề mặt công khai bị viewer-freeze kẹp ở `2026-06-07`,
  `/api/final-bundle` sau FU-438 là admin-only fail-closed. Đây là **thiết kế owner đã khoá**,
  nhưng phải ghi *«không đo được»*, **cấm** ghi *«không lệch»*.
- **Bằng chứng:** `REPORT_V11164.md` mục 3.6 · `GATE_g4-total-final.md` mục TÓM TẮT.
- **Phân loại:** `PROVEN_DEFECT` — **nhãn hàng bảng** nói năm, **nội dung** chứng minh bốn.
- **Sửa nhãn thành:** *«Bốn tầng raw → override (tầng 5 UI: KHÔNG ĐO ĐƯỢC)»*.

### CC-03 · «TOTAL trung thực tuyệt đối» → FIDELITY, ba bundle, một ngày

- **Chỗ gốc:** `REPORT_V11164.md` mục 1, *«Ba điều đáng đọc nhất»* ①
- **Nguyên văn:** *«Bộ chọn TOTAL trung thực tuyệt đối.»*
- **Đọc ĐÚNG:** **FIDELITY** — sự trung thực số học giữa raw model output và số công bố — được
  chứng minh cho **đúng ba bundle ngày 04/09** (MN 825 · MT 827 · MB 829): 30/30 hàng top-10,
  81/81 hàng trọng số BT, lô-3 3/3.
- **KHÔNG chứng minh:** ① **predictive validity** — 60 ngày: không model nào vượt nền có ý nghĩa;
  V11086 đo bộ k số trên nền đúng `1−(1−b)^k`: 30 ngày −3,96pp · 90 ngày −5,15pp · 180 ngày
  −0,35pp, **cả ba đều âm**. ② **toàn lịch sử** — con số *«45/45 bundle»* là phép **tất định** trên
  đầu vào đã lưu, **khác hẳn** phép tái lập từ raw model output vốn chỉ làm cho 3 bundle.
- **Phân loại:** `PROVEN_DEFECT` (cụm từ nói quá phạm vi).

### CC-04 · Prompt: regime PASS, payload NOT PROVEN — đã tự đo lại trên mã đang serve

- **Nguyên văn:** *«`PROMPT_LANE_REGIME_FIXED` nhưng `PROMPT_CLEAN_NOT_PROVEN`»*
- **Đọc ĐÚNG:** **REGIME ROUTING = PASS** (60/60 lượt: 27/27 official → `LEGACY_PROMPT`,
  33/33 shadow → `CONTEXT_ONLY_V2`). **FULL PAYLOAD CLEAN = NOT PROVEN.**
- **Tôi đọc thẳng `gpt_analyzer.py` đang serve (sha `758c29c13185763f`, khớp GATE 0) — RM-14, RM-10:**

| dòng | mã | vai trò |
|---|---|---|
| `:6683` | `_ctx_only_lane = regime_prompt_cho_luot(lane_test_shadow_pack, selected_model)` | bản vá V11160 — **theo LƯỢT**, **đúng** |
| `:6698` | `create_analysis_prompt(..., context_only=_ctx_only_lane)` | cờ regime đi vào prompt |
| `:6680` | `_la_shadow = bool(lane_test_shadow_pack) or (selected_model in SHADOW_GATE_MODELS)` | theo MODEL **nhưng chỉ dùng cho dòng `print` chẩn đoán `:6686-6690`** — **KHÔNG** phải đường rò |
| **`:6738`** | `_shadow_mode = lane_test_shadow_pack or (selected_model in SHADOW_GATE_MODELS)` | 🔴 **đường rò còn lại** — theo MODEL |
| `:6740` | `build_context_pack(target_region, date_str, shadow_mode=_shadow_mode)` | dựng gói ngữ cảnh **biến thể shadow** |
| `:6755` | `prompt += _ctx_pack` | gói đó nối vào prompt |

- **Cơ chế chính xác — hai thứ khác nhau, cùng đúng một lúc:** **cờ** regime đúng, nhưng **nội
  dung** `ctx_pack` được dựng ở biến thể `shadow_mode=True` rồi nối vào một prompt `LEGACY`.
- **Vân tay:** `:6723` băm `(system_prompt) + "\n<<<USER>>>\n" + (prompt)` — **trước** khi nối
  `ctx_pack` (`:6755`) và `REASONING_RULEBOOK` (`:6760`) ⇒ vân tay chỉ phủ phần tiền-ctx.
- **Kết luận:** **đúng MỘT** chỗ rò — báo cáo gốc nói đúng. Tôi tái lập độc lập, không chép.
- **Phân loại:** `PROVEN_DEFECT`.

### CC-05 · Ba con số prompt đã bị thay — cấm trích lại số cũ

- **Chỗ gốc:** `evidence/GATE_g5-anomaly.md` dòng 5 (raw, **trước** phản biện)
- **Nguyên văn (SAI):** *«lệch **88/88** (ngày,miền) trong 30 ngày … `runtime_prompt_chars=24.435`
  trong khi chuỗi thật **≥50.670** ký tự»*
- **ĐÚNG:** **86/86** cặp (ngày, miền) **đo được** đều lệch; 3 cặp không đủ dữ liệu đối chiếu;
  mở sang 31 ngày: **89/89**; bảy model official khác **0/86**. Chuỗi thật = **50.658** ký tự;
  thiếu **26.223** ký tự = 51,8%.
- **Vì sao lệch 12 ký tự:** `len("\n<<<USER>>>\n")` = 12 — nằm trong `runtime_prompt_chars` nhưng
  **không** thuộc chuỗi gửi đi; bản raw đếm nó hai lần. Cơ chế này xác nhận được bằng đọc
  `gpt_analyzer.py:6723`.
- **Bằng chứng:** `PHAN_BIEN_32_SUA_LAI.md` mục 9 và mục 10.
- **`REPORT_V11164.md` đã dùng số mới** (dòng 191, 194–195). **Raw `g5` giữ số cũ** — đây chính là
  lý do `g5` phải mang nhãn `NOT_CANONICAL_IN_ISOLATION`.

### CC-06 · stdio — phạm vi probe mù hẹp hơn câu đã nói

- **Chỗ gốc:** `evidence/GATE_g7-stdio.md` dòng 5, **và** lời nói trực tiếp với owner trong IDE ~21:5x
- **Nguyên văn (SAI):** *«probe `stream.write("")+flush()` … KHÔNG phát hiện được hỏng ở tầng fd
  (EPIPE / EBADF / AF_UNIX peer chết) — **đúng hình dạng `fd1=fd2=socket:[76184038]` của service**»*
- **ĐÚNG:** probe mù với **PIPE MẤT ĐẦU ĐỌC** (kernel `pipe_write` thoát sớm ở đường
  *«Null write succeeds»* **trước** cả khi kiểm `pipe->readers`). Bản phản biện **KHÔNG** chứng
  minh được probe mù với **socket journald** — tức đúng hình dạng fd thật của service.
- **Mức nghiêm trọng THẤP HƠN** câu raw. Đã vào sổ rút lại **RL-013** (đủ bốn phần).
- **`REPORT_V11164.md` mục 3.12 đã thu hẹp đúng.** Raw `g7` dòng 5 giữ câu rộng.

### CC-07 · Gate 6 — mệnh đề đã bị rút lại vẫn nằm nguyên trong raw

- **Chỗ gốc:** `evidence/GATE_g6-debt.md` **dòng 35**
- **Nguyên văn (SAI):** *«Latent `_safe_stdio_ctx` concern — 28 vị trí trong `scheduler.py`,
  **0 dòng lỗi I/O đo được nên nhánh nguy hiểm chưa từng chạy**. Giữ nguyên quyết định chủ động
  không sửa của V11163, xếp P3.»*
- **ĐÚNG:** nhánh **đã chạy thật, 270 lần**. `scheduler_logs` có **270 dòng**
  `ValueError: I/O operation on closed file.` từ **2026-05-10 12:01:21** đến **2026-07-19 17:30:00**
  (`log_time` naive = **UTC** — §55), traceback trỏ thẳng `scheduler.py:1851 print(...)`.
- **Nhánh im từ 2026-08-01** là nhờ **V10800 (15/07) và V10826** tách job sang **subprocess** có
  stdout riêng — tức được vá bằng **cách ly tiến trình**, **hoàn toàn không** nhờ `_safe_stdio_ctx`.
- **Lỗi đo lường gốc:** quét **journal** (chỉ còn lưu từ 29/08) rồi kết luận cho **cả đời** nhánh mã
  — *cửa sổ bằng chứng hẹp hơn cửa sổ kết luận*.
- **Quyết định *«chủ động không sửa»* GIỮ NGUYÊN**, nhưng **lý do đổi hẳn**.
- **Bằng chứng:** `SELECT COUNT(*) FROM scheduler_logs WHERE message LIKE '%closed file%'` → 270;
  `docs/SO_RUT_LAI.json` **RL-010**.
- 🔴 **MÂU THUẪN CÒN SỐNG:** `g6` dòng 35 và `g7` dòng 22 nói **ngược nhau** về cùng một sự việc,
  trong cùng một thư mục evidence. Đây là lý do bắt buộc phải dán nhãn raw.

### CC-08 · combo-super: gọi lại là THIẾT KẾ, lỗi nằm chỗ khác

- **Nguyên văn:** *«combo-super **GỌI LẠI** chính model đã bỏ phiếu (trace bắt được 3 lượt gọi lại
  đúng giây tạo bundle)»*
- **ĐÚNG:** cơ chế gọi lại là **`EXPECTED_BEHAVIOR`** — thiết kế đã thành văn
  (`combo_super.py:1374 → :1134`, docstring `:1238`, `CLAUDE.md §59` UNIFIED TOP-3 V6.0).
- **Đọc SAI:** coi việc gọi lại là lỗi. Đó là `A57_VIOLATION` đọc sai thiết kế.
- **Defect THẬT nằm chỗ khác:** số đếm voter **thô** (không de-dup huyết thống) đi thẳng vào
  `consensus_level` (`main.py:10339-10345`, ≥4 → `strong`) ⇒ nhãn đồng thuận **bị thổi** từ
  `moderate` lên `strong`. Ngày 04/09 việc này **không** đổi bạch thủ.
  MT bạch thủ `28`: **4 voter nhưng chỉ 3 danh tính**; MN số `73`: **3 phiếu nhưng chỉ 2 nguồn**.
- **Phân loại:** `PROVEN_DEFECT` (ở `consensus_level`, **không** ở combo-super).

### CC-09 · 🔴 MT «71 ngày liên tiếp» — TÔI ĐÃ TỰ ĐO LẠI TRÊN CLONE

- **Chỗ gốc:** `REPORT_V11164.md` dòng 47 (mục 1) và dòng 581 (mục 9) · `PHAN_BIEN_32_SUA_LAI.md`
  mục 3 (đề xuất SỬA TIÊU ĐỀ)
- **Nguyên văn:** *«MT bị loại khỏi đo lường chính **71 ngày liên tiếp** vì một lỗi **KẾ TOÁN**,
  không phải lỗi chạy.»*

**Kết quả đo lại — con số 71 TÁI LẬP ĐƯỢC, nhưng chỉ với đúng MỘT định nghĩa:**

| định nghĩa | MT | MN | MB |
|---|---|---|---|
| **A** — `evaluation_policy != 'INCLUDE'`, đếm ngược từ 04/09 | **71 ngày** (`2026-06-26` → `2026-09-04`), phá ở `2026-06-25` (`INCLUDE · VALID_LIVE_DAY`) | **0** | **0** |
| **B** — `EXCLUDE_PRIMARY` liên tiếp | **7 ngày** (`2026-08-29` → `2026-09-04`), phá ở `2026-08-28` (`EXCLUDE_ALL`) | — | — |

⇒ **CẤM viết *«MT bị `EXCLUDE_PRIMARY` 71 ngày liên tiếp»***. Con số đó là **7**.
Câu đúng: *«MT không được `INCLUDE` vào đo lường chính 71 ngày liên tiếp — 70 `EXCLUDE_PRIMARY`
+ 1 `EXCLUDE_ALL`»*.

**Bao nhiêu quy cho cấp, bao nhiêu do nguyên nhân khác:**

| | trong chuỗi 71 | trong cửa sổ 90 dòng |
|---|---|---|
| mang dấu hiệu cấp `Thiếu 2 model (13/15)` | **65** | **65 / 72** |
| **KHÔNG** phải cấp | **6** | **7** |
| `EXCLUDE_PRIMARY` tổng | 70 | **72/90 = 80,0%** ✅ khớp báo cáo |

**Sáu ngày KHÔNG phải cấp trong chuỗi 71:**

| ngày | policy | lý do |
|---|---|---|
| `2026-07-25` | `EXCLUDE_PRIMARY` | Thiếu 4 model (11/15) |
| `2026-08-07` · `2026-08-08` · `2026-08-15` · `2026-09-02` | `EXCLUDE_PRIMARY` | Thiếu 3 model (12/15) |
| **`2026-08-28`** | **`EXCLUDE_ALL`** | *«Nghiêm trọng: chỉ 6/15 model (40%)»* — **hỏng CHẠY thật**: MT hôm đó **0 dòng `ai_chain`**, chỉ 7 dòng `auto_daily` |

⇒ Câu *«vì một lỗi KẾ TOÁN»* **không đúng cho cả 71 ngày**. Ít nhất `2026-08-28` là hỏng chạy thật.

**⚠️ RM-10 — cảnh báo về chính phép quy nguyên nhân của tôi:** dấu hiệu `Thiếu 2 model (13/15)`
**tự nó không phải bằng chứng** đó là trần V10752. Dấu hiệu này đã xuất hiện **7 lần TRƯỚC
`2026-06`** (tháng 3: 5 · tháng 4: 1 · tháng 5: 1) — tức **trước ngày owner duyệt trần (25/06)**.
Suy *«13/15 ⇒ trần V10752»* là kết luận theo **hình dạng**; muốn thành nhân quả phải thêm bằng
chứng `gate_diagnostics`.

**🔴 «46/72» KHÔNG TÁI LẬP ĐƯỢC — `RM-11`.** `GATE_g1` dòng 49 nêu kết quả *«46/72 ngày MT bị loại
là do cap chứ không do hỏng»* **mà không kèm truy vấn nào**, và không tệp evidence nào khác ghi
dẫn xuất. Đếm theo `degradation_reason` cho **65/72**.
**Thử nghiệm thất bại của tôi, ghi lại để không ai lặp:** tôi thử định nghĩa chặt hơn (cấp 13/15
**và** ≥15 model chạy thật trong ngày) và ra **0/65** — nhưng **bộ lọc `run_source` của tôi SAI**:
tôi chỉ lấy `('ai_chain','free_predict')` trong khi lượt official của MT thực tế là
`ai_chain + auto_daily` (04/09: 9+7=16 dòng) hoặc `ai_chain + rerun_post_mn` (01/07: 8+7=15).
**Kết quả 0/65 VÔ GIÁ TRỊ — ghi `INDETERMINATE`, không được dùng.**

- **Bằng chứng:** clone `c3c2f568…` ·
  `SELECT date, evaluation_policy, degradation_reason FROM day_governance WHERE region='MT' ORDER BY date`
  · artifact `v11165_h1_mt_streak.json` · `v11165_h1_mt_streak2.json` · `v11165_h1_mt_attr.json`
- **Phân loại:** `PROVEN_DEFECT` (nhãn `EXCLUDE_PRIMARY` sai) + `INDETERMINATE` (con số 46).

### CC-10 · NULL — `STATE_SPACE = 4`, bắt buộc nói TRƯỚC hay SAU migration

- **Chỗ gốc:** `REPORT_V11164.md` mục 4.1 và 4.3 R2 · `evidence/GATE_g8-abc.md` · `RL-009`
- **Nguyên văn (REPORT):** *«**Bốn lớp `NULL`** đo được (không phải hai như đã công bố):
  `COMPUTED_IN_TOP10` 2.094 · `COMPUTED_OUTSIDE_TOP10` 444 · `NOT_COMPUTABLE_NO_NUMBER` 135 ·
  `NOT_COMPUTED_OUT_OF_WINDOW` 14.448»*
- **Nguyên văn (`g8`):** *«NULL **sau migration** mang **ÍT NHẤT BA** nghĩa chứ không phải hai như
  đã công bố (thiếu lớp 135 dòng `parse_ok=0`)»*

**Hai câu này không mâu thuẫn — chúng đếm ở HAI MỐC THỜI GIAN khác nhau, và không tệp nào nói ra mốc:**

| mốc | cột `output_counterfactual_rank` | NULL mang mấy nghĩa |
|---|---|---|
| **TRƯỚC migration** *(= hiện tại)* | **rỗng cho CẢ BỐN state**: `17.121/17.121` NULL, `0` giá trị phân biệt | **BỐN** |
| **SAU phương án A** | chỉ `COMPUTED_IN_TOP10` (**2.094**) có rank | **BA** — phần NULL còn lại `444 + 135 + 14.448` = **15.027** |

- **CẤM** viết *«NULL hai lớp»* hoặc *«NULL bốn lớp»* mà không nói TRƯỚC/SAU migration — trộn hai
  cách đếm là `A60_VIOLATION_LAYER_CONFLATED`.
- **Owner đã khoá Option B (QD-073)** ⇒ **không có migration** ⇒ cột giữ nguyên `17.121/17.121`
  NULL, gộp **đủ bốn** state.
- **Bằng chứng:** clone —
  `SELECT COUNT(*), SUM(output_counterfactual_rank IS NULL), COUNT(DISTINCT output_counterfactual_rank) FROM shadow_model_promotion_scorecard_daily`
  → `17121 · 17121 · 0`. Kiểm số: `2.094 + 444 + 135 + 14.448 = 17.121` = đúng tổng bảng.
  Artifact `v11165_h1_null.json`.
- **Phân loại:** `PROVEN_DEFECT` (thiếu nhãn mốc thời gian ở cả hai tệp).

### CC-11 · Đếm số ca rút lại: 5 + 1 = 6

- **Chỗ gốc:** `REPORT_V11164.md` dòng 11 (*«RÚT LẠI **năm** kết luận đã công bố»*) và mục 4.3
  (*«Hai trong **năm** ca»*) — đứng cạnh mục 5 (*«rút lại | 0 | **6 ca**»*) và dòng TanPhatAI
  (*«**SÁU CA** RÚT LẠI»*)
- **Cách đếm — hai thước, không được trừ nhau (`RM-21`):**

| thước | đếm gì | số |
|---|---|---|
| **CÔNG BỐ** | mệnh đề sai có mặt trong tài liệu/báo cáo **đang lưu hành** | **5** (R1–R5 = `RL-008`…`RL-012`) |
| **SỔ RÚT LẠI** | mọi phát ngôn sai **đã đến tai owner hoặc người đọc** | **6** (thêm R6 = `RL-013`, câu nói trực tiếp trong IDE ~21:5x) |

- **Kiểm:** `docs/SO_RUT_LAI.json` có **13 mục** `RL-001`…`RL-013`; V11164 thêm **6**
  (`RL-008`…`RL-013`). Cả 6 đều đủ **bốn phần** bắt buộc của `PRJ-RETRACTION-001`:
  `cho_goc` · `nguyen_van_cau_sai` · `dieu_dung` (+ `phep_do_tai_lap`) · `quyet_dinh_da_dua_tren`.
- **Phân loại:** `EXPECTED_BEHAVIOR` — không sai, nhưng hai con số đứng cạnh nhau mà không nói rõ
  thước ⇒ phải ghi cách đếm.

### CC-12 · 🔴 PHÁT HIỆN MỚI — so sánh MT chọn lọc, bỏ quên MB

*(chưa có trong V11164 và chưa có trong 32 phản biện)*

- **Chỗ gốc:** `evidence/GATE_g1-region-ledger.md` dòng 5 · `REPORT_V11164.md` mục 1 và 4.2
- **Nguyên văn:** *«90 ngày qua MT bị loại **72/90 lượt (80,0%)** so với **MN 10/91 (11,0%)**»*
- **Thực đo trên clone (90 dòng gần nhất mỗi miền):**

| miền | `INCLUDE` | `EXCLUDE_PRIMARY` | `EXCLUDE_ALL` | tỉ lệ bị loại |
|---|---|---|---|---|
| MN | 80 | 10 | 0 | **11,1%** |
| MT | 17 | 72 | 1 | **80,0%** |
| **MB** | **17** | **73** | 0 | **81,1%** *(trên 91 dòng: 74/91 = **81,3%**)* |

⇒ **MB bị loại NHIỀU HƠN MT.** Báo cáo chỉ so MT với MN và **không nhắc MB ở bất kỳ chỗ nào**
trong so sánh này. Chọn vế so sánh như vậy làm vấn đề **trông như đặc thù của MT**.

- **Khác biệt THẬT giữa MT và MB — vẫn có, nhưng không phải khác biệt đã được kể:**
  - **MT**: bị loại **liên tục** (71 ngày liên tiếp), **65/71** mang dấu hiệu cấp `13/15`
    ⇒ đúng là lỗi **kế toán hệ thống**.
  - **MB**: bị loại **ngắt quãng**, ngày 04/09 là `INCLUDE` nên chuỗi liên tiếp = **0**; lý do là
    **43× `Thiếu 1 model (14/15)`** + 21× `13/15` + 10× `12/15` ⇒ **rớt model lặt vặt**,
    **KHÔNG** phải trần MT-13.
- **Hệ quả cho `MT_PREREGISTRATION`:** **củng cố** kết luận `NOT_READY_FOR_OWNER_LOCK`, nhưng lý do
  phải rộng hơn: không chỉ thước của MT hỏng — **HAI TRONG BA miền** đang bị loại ~80% số ngày.
  Mọi nền so sánh liên-miền dùng rolling WR/TOP1 hiện tại đang so **MN mẫu 80/90** với
  **MT 17/90** và **MB 17/90**.
- **Bằng chứng:** artifact `v11165_h1_mt_streak2.json` khối `policy_90`.
- **Phân loại:** `PROVEN_DEFECT`.

### CC-13 · 🔴 PHÁT HIỆN MỚI — tệp evidence tự khai SỐ HIỆU CỔNG lệch với tên tệp

- **Chỗ gốc:** `evidence/GATE_g3-model-universe.md` dòng 1 · `evidence/GATE_g4-total-final.md`
  dòng 1 · `REPORT_V11164.md` mục 11
- **Nguyên văn (`GATE_g4-total-final.md` dòng 1):** *«# **gate6** · tang=EVIDENCE_COMPLETE ·
  16 phat hien»*
- **Nguyên văn (`REPORT_V11164.md` mục 11):** *«GATE 2 prompt routing · **GATE 6 debt** | `PARTIAL` (2)»*
- **Thực:** `GATE_g3-model-universe.md` tự khai `gate4`; `GATE_g4-total-final.md` tự khai `gate6`.
  Mục 11 của REPORT ánh xạ theo **TÊN TỆP** (`g1 g3 g4 g5 g7 g8` = `EVIDENCE_COMPLETE`;
  `g2 g6` = `PARTIAL`) và ánh xạ đó **đúng**.
- **Vì sao nguy hiểm:** người mở `GATE_g4-total-final.md` đọc ngay dòng đầu
  *«gate6 · EVIDENCE_COMPLETE»*, trong khi mục 11 ghi *«GATE 6 = PARTIAL»* ⇒ **hai câu ngược nhau
  trên bề mặt**, chỉ vì `gate6` trong tệp là **số hiệu tự khai sai**. Đây là **lớp bằng chứng** —
  một agent đọc sau (TanPhatAI) đối chiếu *«GATE 6»* sẽ lấy nhầm tệp và kết luận ngược.
- **Xử:** **không sửa tệp raw**; dùng bảng ánh xạ ở **mục 2** của chính tệp này.
- **Phân loại:** `OPERATIONAL_IMPROVEMENT`.

---

## 4 · Mutation ledger của gate này

| loại | số | ghi chú |
|---|---|---|
| production DB row mutation | **0** | mọi kết nối mở `mode=ro` trên **clone bất biến**, không chạm DB production |
| thay đổi mã production | **0** | 6/6 hash tệp đang serve khớp GATE 0 |
| deploy · restart | **0 · 0** | |
| git commit / push | **0** | agent chính sẽ commit |
| ghi Notion | **0** | §57.1 |
| tệp ghi trên VPS | 7 JSON + script `_run__h1*.py` | tất cả trong `/root/Lottery_AI_Test/artifacts/` |
| tệp ghi local | 2 | `EVIDENCE_STATUS_V11164.md` · `.json` |
| **tệp raw bị sửa** | **KHÔNG** | 8 tệp `evidence/GATE_g*.md` giữ nguyên sha256 như mục 2 |

---

## 5 · Đầu vào cho làn sóng 2

1. **CC-09 + CC-12** — trước khi bất kỳ ai dùng rolling WR/TOP1 làm nền so sánh liên-miền, phải
   biết mẫu thật là **MN 80/90 · MT 17/90 · MB 17/90**. Đây là điều kiện chặn cho
   `MT_PREREGISTRATION` và cho mọi phép đo *«model nào tốt hơn»*.
2. **CC-09** — con số **«46/72» không tái lập được** từ artifact đã công bố (`RM-11`). Làn sóng 2
   hoặc **ghi rõ dẫn xuất**, hoặc **rút lại** con số.
3. **CC-10** — owner đã khoá **Option B** ⇒ **không có migration** ⇒ cột giữ nguyên
   `17.121/17.121` NULL, gộp **đủ bốn** state. Mọi tài liệu sau phải nói *«bốn state, chưa
   migration»*, **không** được mượn cách đếm *«ba nghĩa sau migration»* của `g8`.
4. **CC-04** — đường rò còn lại là **duy nhất một chỗ**: `gpt_analyzer.py:6738`, và nó chạm **NỘI
   DUNG** `ctx_pack` chứ **không** chạm **CỜ** regime. Mọi đề xuất vá phải nói rõ nó sửa nội dung
   hay sửa cờ.
5. **CC-13** — khi trích *«GATE 6»* phải nói rõ là **tên tệp** hay **số hiệu tự khai** — hai hệ
   đang lệch.

---

**TanPhatAI cần làm:** ghi nhận `EVIDENCE_STATUS_V11164.md` + `.json` là **lớp chỉnh bằng chứng**
của V11164 (sinh bởi V11165 GATE 1, **chưa commit** — agent chính commit). Ghi **8 tệp
`evidence/GATE_g*.md` nay mang nhãn `RAW_PRE_REVIEW_ARTIFACT · NOT_CANONICAL_IN_ISOLATION`,
`SUPERSEDED_BY = REPORT_V11164.md + PHAN_BIEN_32_SUA_LAI.md`** — sha256 từng tệp ở mục 2, **nội
dung KHÔNG bị sửa**. Ghi **13 mục claim correction `CC-01`…`CC-13`**, trong đó **hai mục MỚI chưa
có trong V11164**: **`CC-12`** — *MB bị loại `74/91 = 81,3%`, **cao hơn** MT `80,0%`, mà báo cáo chỉ
so MT với MN* ⇒ vấn đề **không** đặc thù MT, **hai trong ba miền** đang bị loại ~80% số ngày; và
**`CC-13`** — *`GATE_g4-total-final.md` tự khai «gate6 · EVIDENCE_COMPLETE» trong khi mục 11 ghi
«GATE 6 = PARTIAL»*, hai câu ngược nhau trên bề mặt lớp bằng chứng. Ghi **«71 ngày liên tiếp» TÁI
LẬP ĐƯỢC nhưng CHỈ với định nghĩa `policy != INCLUDE` (`2026-06-26`→`2026-09-04`, 70
`EXCLUDE_PRIMARY` + 1 `EXCLUDE_ALL`); chuỗi `EXCLUDE_PRIMARY` liên tiếp thật chỉ là **7 NGÀY** —
cấm viết «`EXCLUDE_PRIMARY` 71 ngày liên tiếp»**; và **`2026-08-28` là hỏng CHẠY thật (0 dòng
`ai_chain`), không phải lỗi kế toán** ⇒ cấm quy cả 71 ngày cho kế toán. Ghi **«46/72» KHÔNG TÁI LẬP
ĐƯỢC (`RM-11`) — đếm theo dấu hiệu cho 65/72**, và **dấu hiệu `13/15` đã xuất hiện 7 lần TRƯỚC
25/06 nên tự nó không chứng minh trần V10752 (`RM-10`)**. Ghi **`STATE_SPACE = 4`: TRƯỚC migration
NULL gộp **bốn** state (`17.121/17.121`), SAU phương án A còn **ba** (`15.027`) — owner khoá Option
B nên **giữ bốn**; cấm viết «NULL hai lớp»/«NULL bốn lớp» mà không nói mốc**. Ghi **rút lại = 5
claim đã công bố + 1 câu nói trong phiên = 6 ca, `RL-008`…`RL-013`, cả 6 đủ bốn phần**. Ghi
**`8 cổng` nghĩa là 8/8 ĐÃ CHẠY, KHÔNG phải 8/8 PASS — thực là 6 `EVIDENCE_COMPLETE` + 2
`PARTIAL`**; **«năm tầng» thực là BỐN — tầng 5 UI KHÔNG ĐO ĐƯỢC**; **«TOTAL trung thực tuyệt đối»
đổi thành FIDELITY chứng minh cho BA bundle 04/09, KHÔNG chứng minh predictive validity**. Ghi
**mutation ledger gate này: 0 ghi production · 0 deploy · 0 restart · 0 commit · 0 ghi Notion · 0
tệp raw bị sửa**. **Không mở Prompt 44. Không mở FU mới. Không mở Plan mới.** `MATERIALIZATION_OPTION`
giữ **B (`OWNER_LOCKED`, QD-073)** · `MT_PREREGISTRATION` giữ **`NOT_READY_FOR_OWNER_LOCK`** ·
`POOL_VERDICT` giữ **`HOLD`** · `MODEL_ACTION` giữ **`BLOCKED`**.
