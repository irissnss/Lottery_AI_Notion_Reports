# V10693 — MB TOTAL FORCE: BÁO CÁO VERIFY (CHỜ DUYỆT)

> **Pha:** VERIFY + BÁO CÁO (chưa sửa code production/official).
> **Ngày báo cáo:** 2026-06-03 tối · **Data as-of:** 2026-06-03 (live sync `20260603_223215`).
> **Official zero-drift:** PASS (4 bảng official hash IDENTICAL trước & sau verify — xem `evidence/EVIDENCE_QUERIES.md` §0).
> **Phạm vi:** chỉ MB; MN/MT chỉ đo để đối chiếu, không đụng. Mọi thử nghiệm (nếu được duyệt) chỉ ở lane `/du-doan-test`.

---

## A. KẾT LUẬN 1 DÒNG

**MB không thiếu budget và không thiếu nguồn — MB thiếu CÁCH CHỐT SỐ.** Tín hiệu số trúng gần như luôn tồn tại trong vote model, nhưng cơ chế đồng thuận (`d_w06`) của MB **khuếch đại đám đông chốt SAI** (đồng thuận MB phản tác dụng: 10% < ngẫu nhiên 23.7%), khiến bạch thủ MB chỉ **6.7%/30 ngày** (dưới ngẫu nhiên 3.5 lần, 7 ngày gần nhất trượt 0/7).

---

## B. MỤC TIÊU CHẤT LƯỢNG XIÊN (định nghĩa "đủ tốt")

Xiên tốt = **bạch thủ (top1) + số phụ 1 (top2) + số phụ 2 (top3)** mỗi vị trí đủ mạnh.
Report đo tách bạch (HIT = số nằm trong tập đuôi mọi giải trong ngày; cross-check 30/30 khớp `bach_thu_status`):

| Miền | top1 (30d) | top2 | top3 | xiên2 | xiên3 | random 1-số |
|---|---|---|---|---|---|---|
| **MB** | **6.7%** | 20.0% | 20.0% | 3.3% | 0.0% | 23.7% |
| MN | 36.7% | 26.7% | 31.0% | 6.7% | 3.3% | 42.4% |
| MT | 40.0% | 43.3% | 50.0% | 13.3% | 6.7% | 34.8% |

→ MB **dưới ngẫu nhiên ở top1**, quanh ngẫu nhiên ở top2/top3. Muốn xiên 2/3/4 tốt thì **bắt buộc** vực top1 trước, rồi tới top2/top3. (`xiên4` official hiện = N/A vì official chỉ xuất tới top3.)

---

## C. VERIFY V1–V7 (trạng thái thực tế → gap → đề xuất fix)

### V1. BUDGET MB LANE — ✅ ĐÃ ĐỦ 20/20, nhưng chất lượng kém
- **Thực tế (DB hiện tại):** MB lane `SELECTED = 20/20` mọi ngày 7 ngày qua (`total=29, measured=23-24, selected=20`). Báo cũ "5/20 PREVIEW_BELOW_BUDGET" **đã lỗi thời** — adaptive budget selector `c16_adaptive_model_budget_v1` đã lấp đủ.
- **Gap thực:** 20 voter MB bị gắn cờ phạt: `MB_AI_STRUCTURAL_PENALTY`×168, `HERD_PENALTY`×128, `HURT_GT_HELP`×112 (7d). Tức budget đầy nhưng **lấp bằng model "hại nhiều hơn lợi"**.
- **Đề xuất fix:** không cần "kéo lên 20" (đã đủ). Cần (i) wire `MAIN_TEST_EQUALS_OFFICIAL`/đếm voter ra UI để hết hiểu nhầm "dưới budget"; (ii) chuyển trọng tâm từ "đếm model" sang "chọn cách tổng hợp tốt hơn" (xem V3/V4).

### V2. SOURCE_POOL_MISS — ✅ NGUỒN CÓ, ❌ KHÔNG ÉP VÀO PROMPT + BUNDLE CHỐT LỆCH (gốc rễ)
- **Thực tế:** nguồn ĐÃ gom đầy đủ ở tầng shadow (v101: MT(D-1)=99, MN(D)=98, MN(D-1)=98, MT(D)=97, MB(D-1)=95 đuôi riêng biệt; `SOURCE_READY`×2572). **Nhưng** `v104 REQUIRED_IN_PROMPT = 0` (toàn bộ 126 candidate là `OPTIONAL_REVIEW`/`REVIEW`). Và `candidate_drop_stage_daily`: **BUNDLE_SKEW = 17/28 ngày** (số trúng có trong vote nhưng bundle chốt số khác; có ngày 18 model trúng top1 mà bundle vẫn LOSE).
- **Gap:** (a) không có cơ chế **ép** tín hiệu nguồn mạnh (MN(D)/MT(D) same-day) vào prompt như "bắt buộc xem xét"; (b) khâu tổng hợp cuối **vứt bỏ** số trúng đã hiện trong vote.
- **Đề xuất fix:** (a) bật một số candidate nguồn-mạnh thành `REQUIRED_IN_PROMPT` cho MB (chỉ lane test); (b) sửa khâu chốt số (V3/V4) để không bỏ rơi số đã được nhiều model trúng.

### V3. PER-NUMBER METHOD — ❌ KHÔNG TỒN TẠI
- **Thực tế:** official **không** có cơ chế "mỗi số một phương pháp". Toàn bộ top1/top2/top3 lấy từ **một** danh sách `number_scores → ranked` (vote-sum). Lớp override `_v10640` **chỉ thay bạch thủ (top1)**; top2/top3/xiên vẫn theo ranked gốc. Có `_v10692_mn_mt_multidir_lane` gắn nhãn `BT/so_phu_1/so_phu_2` nhưng vẫn 1 ranked list và **shadow-only**, không vào official.
- **Gap:** không thể "mỗi vị trí đủ mạnh" khi cả 3 vị trí dùng chung 1 phép tổng hợp (và phép đó đang sai cho MB).
- **Đề xuất fix:** thiết kế **per-position method cho MB** (lane test): top1 = phương pháp A (vd anti-herd/structural-source), top2 = phương pháp B (vd co-occurrence với top1), top3 = phương pháp C (vd diversity/đuôi same-day MN-MT). Xem mục D.

### V4. CHOOSER HIỆN HÀNH — ✅ XÁC NHẬN cấu hình, ❌ MB sai phương pháp
- **Thực tế (OVERRIDE_CONFIG):** `MN={enabled, d_w06}`, `MT={enabled, nt_consensus}`, `MB={enabled, d_w06}` (cả 3 enabled; comment "MB OFF/hot30" trong header là **stale**, dict mới là đúng).
- **Hiệu năng per-position (30d):** `d_w06` MB = top1 6.7% (vs plurality 10%, vs random 23.7%). `d_w06` khuếch đại đồng thuận, mà **đồng thuận MB phản tác dụng** → kết quả tệ hơn cả random.
- **Gap:** `d_w06` hợp với MN (đồng thuận giúp ích 50%>42%) nhưng **không hợp MB**.
- **Đề xuất fix:** thay chooser MB bằng phương pháp **chống đồng thuận** (anti-herd) hoặc dựa nguồn cấu trúc, kiểm trên lane test trước; KHÔNG đổi MN/MT.

### V5. OBSERVABILITY / ISOLATION — ⚠️ marker chưa wire UI; isolation OK
- **Thực tế:** `MAIN_TEST_EQUALS_OFFICIAL` tính trong `main.py` (`_v10519_lane_contract_for_region`) và lộ qua **admin API** (`/api/admin/test-lane-readiness`, `/api/admin/test-lane-diff-vs-official`). Trang `/du-doan-test` đã có **UI render marker** nhưng `loadPreview()` gọi `/api/du-doan-test/{region}` — endpoint này **không set `clone_warning`** → marker không hiện. Isolation **được enforce** (hard-contract 3 engine + `source_hash_snapshot`/`official_tables_changed`; lane chỉ ghi `du_doan_test_*` + `*_experimental_preview_shadow`).
- **Gap:** owner không thấy "lane = official" hay "official bất biến" ngay trên UI lane test.
- **Đề xuất fix:** thêm `clone_warning` + chỉ báo "official unchanged (hash)" vào response `/api/du-doan-test/*` (chỉ thêm field đọc, không đổi official logic).

### V6. TRACEABILITY — ⚠️ runtime VPS đi TRƯỚC git
- **Thực tế:** VPS head `94242fb` (2026-06-03 13:44, branch `master`); private head `c187370` (2026-06-03 21:40). VPS có **thay đổi chưa commit**: `main.py` (mtime 06-03 15:49 > commit 05-31 20:20), `du-doan-test.html`, `_v10679/_v10680/_v10692_*`. Service active từ 06-03 21:39.
- **Gap:** "file đang chạy đi trước git" = **ĐÚNG** (có drift). Báo cũ "VPS=V17.19.4" đã lỗi thời.
- **Đề xuất fix:** commit/đồng bộ runtime VPS ↔ git để bảo toàn truy vết **trước** khi deploy đợt MB (tránh deploy đè mất thay đổi runtime).

### V7. METRIC GAP — ❌ chỉ đo BT 1 số; đã bổ sung bộ metric xiên trong report này
- **Thực tế:** backtest/PASS-FAIL hiện đo **BT hit (1 số)**. Report này đã bổ sung & đo: per-position (top1/2/3), xiên2/3, coverage top-N, ceiling, baseline (mục B + evidence).
- **Đề xuất fix:** đưa bộ metric per-position + xiên2/3/4 + coverage top-N vào **scoreboard lane test** (`du_doan_test_*_scoreboard`) làm tiêu chí PASS/FAIL chính thức cho MB.

---

## D. ĐỀ XUẤT HƯỚNG XIÊN CHO MB (a–f) — CHỜ DUYỆT, CHƯA CODE

| # | Đề xuất | Dựa trên bằng chứng | Phạm vi |
|---|---|---|---|
| **a** | **Per-position method**: top1 dùng anti-herd/structural; top2 dùng co-occurrence với top1; top3 dùng diversity. Mỗi vị trí 1 phương pháp riêng. | V3 (không có per-position) + V4 (d_w06 sai) + ceiling (consensus MB phản tác dụng) | lane `/du-doan-test` |
| **b** | **Co-occurrence miner**: cặp/bộ-ba đuôi hay trúng CÙNG NGÀY cho MB theo từng thứ → phục vụ xiên 2/3 (top2/top3 chọn số "đi kèm" top1). | xiên2 MB chỉ 3.3%, xiên3 0% → cần số phụ tương quan với top1 | lane |
| **c** | **Expected set coverage**: xếp hạng bổ trợ theo kỳ vọng phủ tập (không thay BT) để tăng coverage top-N. | cover top-N MB 43.3% vs MT 80% | lane |
| **d** | **Anti-herding / diversity**: top-N không trùng "họ" số; phạt đồng thuận khi đồng thuận lịch sử phản tác dụng. | **plurality MB 10% < random 23.7%** (đồng thuận hại) | lane |
| **e** | **Bơm đầy MN(D)+MT(D) same-day** vào tập đuôi MB (MB xổ cuối → hợp lệ nhân quả) + ép `REQUIRED_IN_PROMPT`. | V2 (`REQUIRED=0`; nguồn same-day có 97-98 đuôi nhưng không ép vào prompt) | lane |
| **f** | **77 rule MANUAL (MB-MANUAL-SOI)** dùng MỞ RỘNG/CỦNG CỐ tập top-N (confirm-only), KHÔNG drive BT. | V10689/V10690 đã chuẩn bị; confirm-only an toàn | lane |

---

## E. DANH SÁCH FIX DỰ KIẾN ĐỂ THỰC HIỆN 1 LƯỢT (sau khi duyệt)

> Tất cả chỉ trên lane `/du-doan-test`, ghi `du_doan_test_*` / `mb_experimental_preview_shadow`; official 4 bảng hash bất biến; MN/MT không đụng.

1. **[V4+V3+a+d] MB per-position chooser mới (lane):** top1 = anti-herd/structural (thay `d_w06` cho MB trong nhánh shadow); đo lại top1 vs baseline.
2. **[b] Co-occurrence miner MB** theo từng thứ → sinh top2/top3 "đi kèm" top1 cho xiên2/3.
3. **[e] Source injection MB:** bơm đầy MN(D)+MT(D) same-day + bật một số candidate nguồn-mạnh thành `REQUIRED_IN_PROMPT` (chỉ lane test).
4. **[c] Expected-set-coverage ranker** bổ trợ (không thay BT) để tăng coverage top-N.
5. **[f] 77 MANUAL confirm-only** mở rộng/củng cố tập top-N (đã có hạ tầng V10689/V10690).
6. **[V7] Scoreboard xiên:** thêm metric per-position + xiên2/3/4 + coverage top-N làm PASS/FAIL MB.
7. **[V5] Wire `clone_warning` + "official unchanged"** vào `/api/du-doan-test/*` (chỉ field đọc).
8. **[V6] Đồng bộ/commit runtime VPS ↔ git** trước khi deploy (bảo toàn truy vết, tránh đè).

**Tiêu chí xong (sáng mai so sánh):** MB lane-test-sau-fix chạy đủ tải, ghi `du_doan_test_*`, official hash IDENTICAL; có số liệu per-position + xiên2/3/4 để so trực tiếp với OFFICIAL.

---

## F. BẰNG CHỨNG

- `evidence/EVIDENCE_QUERIES.md` — toàn bộ số liệu thô (zero-drift, baseline, per-position, ceiling, budget, drop-stage, injection, traceability).
- `evidence/V7_PER_POSITION_METRICS.json` — machine-readable per-position + xiên (MB/MN/MT + 7 nhánh lane).
- `evidence/OFFICIAL_HASH_BASELINE.json` — hash 4 bảng official (baseline để kiểm bất biến).

---

## ⏳ CHỜ DUYỆT — danh sách fix dự kiến (V1–V7 + xiên a–f) để thực hiện 1 LƯỢT.

Anh duyệt giúp em: (1) đồng ý toàn bộ danh sách mục E, hay (2) chọn lọc mục nào làm trước. Sau khi anh OK, em sẽ code 1 lượt trên lane `/du-doan-test` và in lại hash official (phải y nguyên) để sáng mai so sánh lane-test-sau-fix vs OFFICIAL theo per-position + xiên2/3/4.
