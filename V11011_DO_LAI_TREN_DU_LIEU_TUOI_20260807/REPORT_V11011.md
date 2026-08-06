# REPORT V11011 — Đồng bộ dữ liệu sống, đo lại toàn bộ, hoàn tất PL19c

> **Ngày:** 2026-08-07 · **Owner duyệt:** *"chạy đi và đo lại đi em"*
> **Đồng bộ:** `2026-08-07T00:31:55` — mọi bảng lên **06/08**
> **Script đo commit kèm** (theo E4) tại `scripts/`

---

## 1. Tóm tắt

Đồng bộ xong, đo lại toàn bộ trên dữ liệu tươi. **Bốn con số quyết định giữ nguyên**, **một con
số đổi rõ**, và **bốn phát hiện mới** từ phần C/D/E của PL19c chưa từng làm.

Đáng chú ý nhất: **đo tiến của bộ đào luật đổi từ `−1,34σ` thành `−0,33σ`** — tức từ *"kém hơn
đối chứng"* thành *"ngang bằng đối chứng"*. Ba ngày dữ liệu thay vì một ngày đã đủ để đảo cách
đọc.

Và **hai con số lịch sử KHÔNG tái lập được**: "57/90 bundle thiếu phiếu" thực tế chỉ **1/93**.

## 2. Owner yêu cầu gì (nguyên văn)

> *"chạy đi và đo lại đi em sau đó báo cáo chi tiết đầy đủ dùm anh nha em, push báo cáo lên
> github và cập nhật [trang phân tích] lên V7 dùm a đi em"*

## 3. Đào bới / phát hiện

### 3.1 Đồng bộ — hash 4 bảng khoá đổi đúng như dự kiến · `VERIFIED_TEST`

| bảng | TRƯỚC (05/08 12:11) | **SAU (07/08 00:31)** |
|---|---|---|
| `predictions` | 11.754 `96bf3180…` | **11.875** `220e9bce…` |
| `final_bundles` | 475 `f8d7eb8f…` | **480** `45a762e0…` |
| `lottery_results` | 15.213 `3c334771…` | **15.226** `20c3f6e1…` |
| `model_daily_eval` | 11.577 `75fffeac…` | **11.739** `f6063f89…` |

Cột `giai_doan` và bảng `mined_rule_doi_chung` do V11003 ghi vào local **đã bị ghi đè** — đúng
như đã cảnh báo trong REPORT_V11010 §8. Đã chạy lại `_v11003_m4_doi_chung_luat.py --dung`.

### 3.2 M4 trên dữ liệu tươi — kết luận đổi cách đọc · `VERIFIED_TEST`

| giai đoạn | đối chứng | cặp | THẬT | GIẢ | **z cũ** | **z mới** |
|---|---|---|---|---|---|---|
| `CHAM_NGUOC` | đổi đài | 692 | 73,7% | 47,3% | +9,77 | **+9,77** |
| `CHAM_NGUOC` | dịch 28 ngày | 1.695 | 85,0% | 74,2% | +8,47 | **+8,47** |
| `DO_TIEN` | đổi đài | **23** | 43,5% | 47,8% | −1,34 | **−0,33** |
| `DO_TIEN` | dịch 28 ngày | **45** | 66,7% | 64,4% | −0,82 | **+0,26** |

**Cách đọc phải sửa:** trước nói *"đo tiến kém hơn đối chứng"*; đúng ra là **"ngang bằng đối
chứng, không phân biệt được"**. Vẫn **0/105 luật** qua cổng (cần n≥20/luật, hiện tối đa ~3).

### 3.3 Bốn con số quyết định — GIỮ NGUYÊN trên dữ liệu tươi · `VERIFIED_TEST`

| con số | cũ (dữ liệu 05/08) | **mới (06/08)** | |
|---|---|---|---|
| model hơn nền sau Bonferroni | 0/34 | **0/34** | ✅ FU-290 không đổi |
| hội tụ "3 nguồn" | n=294, z=−2,51 | n=**302**, z=**−2,54** | ✅ FU-298 vững hơn |
| bảng chi phí rỗng | 0/4033 | **0/4033** | ✅ |
| bundle làm bù | 90 | **90** | ✅ |
| bầy đàn MN | 21,6 → 9,2 số | 21,7 → 9,2 (2,36×) | ✅ |

Bảng xếp hạng model trên dữ liệu tươi: `gemini-2.5-pro` **+1,61** · `smart-ensemble` +1,01 ·
`gemini-3.5-flash` +0,97 · … · `qwen3-coder` **−2,08**. **Không con nào chạm ngưỡng ±3,01.**

### 3.4 FU-297 — mốc chốt samday MT 12/08 **KHẢ THI** · `VERIFIED_TEST`

`v10801_ml_mark_ab_daily`: **23/28 ngày forward** từ 15/07, liên tục 15/07 → 06/08, 184 dòng.
Còn thiếu **5 ngày** ⇒ đủ vào **~11/08** ⇒ **mốc 12/08 kịp**.

### 3.5 PHÁT HIỆN MỚI 1 — "57/90 bundle thiếu phiếu" KHÔNG tái lập · `VERIFIED_TEST`

Đo 30 ngày trên dữ liệu tươi: **93 bundle** · số chốt **CÓ** trong phiếu model **92 (99%)** ·
**KHÔNG có phiếu nào: 1 (1%)**.

Con số V10978 *"57/90 = 63% thiếu phiếu"* **không tái lập được**. Hoặc định nghĩa "thiếu phiếu"
khác (ví dụ đếm phiếu **top-1** thay vì mọi phiếu), hoặc đã được vá. **Chưa kết luận là sai —
phải đối chiếu đúng định nghĩa gốc.**

### 3.6 PHÁT HIỆN MỚI 2 — MB chạy theo V10895, V10770 đã bị thay thế · `VERIFIED_TEST`

14/14 ngày gần nhất, MB **luôn** có `rerun_post_mt×7`:

| ngày | run_source |
|---|---|
| 06/08 → 02/08 | `shadow_auto_eval×11` · `ai_chain×9` · **`rerun_post_mt×7`** |
| 01/08 | `ai_chain×8` · **`rerun_post_mt×7`** · `shadow_auto_eval×3` |
| 31/07 → 24/07 | `shadow_auto_eval×10-12` · `ai_chain×8` · **`rerun_post_mt×7`** |

**⇒ V10895 (luôn rerun 17:30) là cơ chế đang chạy. V10770 (đầu tháng samday / cuối tháng D-1)
phải đánh dấu `SUPERSEDED`.**

### 3.7 PHÁT HIỆN MỚI 3 — D2 herd có kiểm soát: §23 KHÔNG giảm bầy đàn · `VERIFIED_TEST`

Khoá tập model AI chạy **cả trước lẫn sau** 29/03 — **7 model chung**:
`claude-opus-4-20250514` · `claude-sonnet-4-6` · `deepseek-reasoner` · `gemini-2.5-flash` ·
`gemini-2.5-pro` · `gpt-5-mini` · `gpt-5.4`.

| giai đoạn | ngày | model/ngày | số khác nhau | **hệ số** |
|---|---|---|---|---|
| TRƯỚC 29/03 | 107 | 4,8 | 2,9 | **1,66×** |
| SAU 29/03 | 392 | 6,6 | 3,6 | **1,84×** |

Trên tập khoá, hệ số **vẫn tăng nhẹ** (1,66→1,84). Nhưng model/ngày trong tập chung cũng tăng
4,8→6,6 (vài model không chạy đủ ngày ở giai đoạn đầu) nên **vẫn còn nhiễu**.

**Kết luận trung thực:** **không có bằng chứng §22/§23 làm giảm bầy đàn**. Cũng chưa đủ sạch để
nói nó làm tăng. **Giữ lệnh CẤM viết §24** cho tới khi có phép so cân bằng số ngày/model.

### 3.8 PHÁT HIỆN MỚI 4 — Q17: hơn 40 bảng cũ hơn 14 ngày · `VERIFIED_TEST`

| bảng | dòng | mới nhất | cũ (ngày) |
|---|---|---|---|
| `mb_t3_prereg_daily` · `sync_parity_audit_daily` · `v10883_connector_apply_log` | 0 | **RỖNG** | — |
| `pattern_rules` | 160 | 26/02 | **162** |
| `prediction_policies` | 6 | 30/03 | **130** |
| `cross_region_spillover_shadow` | 11.283 | 02/05 | **97** |
| `loz_selector_shadow` | 4.033 | 06/05 | **93** |
| **`model_latency_cost_audit_daily`** | 4.033 | 06/05 | **93** |
| `v105_context_completeness_audit` | 7.219 | 10/05 | **89** |

**Hơn 40 bảng** cũ hơn 14 ngày. Đặc biệt `model_latency_cost_audit_daily` — trước nay chỉ nói
*"cột chi phí rỗng"*, thực ra **cả bảng đã dừng ghi 93 ngày**.

### 3.9 E5 — `pnl_daily_summary` · `VERIFIED_TEST`

Cột: `date · mn_cost · mn_payout · mt_cost · mt_payout · total_cost · total_payout · net ·
wallet_balance_after · settled_at`. **Không có cột cờ nào.** 14 dòng, **07/05 → 20/05** — cũ
**79 ngày**. Ghi bởi `pnl_settlement.py:744`.

## 4. Hướng xử lý và vì sao chọn

**Cổng FU-303 đã cài sẵn vào script đo** — `do_lai_tuoi.py` mở đầu bằng việc đọc
`latest_manifest.json`, tính tuổi dữ liệu, **thoát ngay nếu cũ hơn 6 giờ**. Đây là mẫu để nhân
ra mọi script đo.

**Commit cả script lẫn output** (theo E4) — thư mục `scripts/` kèm báo cáo, để bất kỳ ai tái lập
được mà không phải viết lại truy vấn.

**Không sửa vội hai con số lịch sử không tái lập được** (57/90 bundle thiếu phiếu). Phải tìm
định nghĩa gốc trước — sửa vội dễ tạo dị bản.

## 5. Đã làm gì

Chạy `web/_sync_live_forensic_inputs.py` (owner duyệt) · chạy lại
`_v11003_m4_doi_chung_luat.py --dung` · viết và chạy 2 script đo mới (`do_lai_tuoi.py` ·
`pl19c_cde.py`) · cập nhật `CHANGELOG` · `SSOT` · `FOLLOW_UP` · bảng mốc tải.

**Không đụng code production, không deploy.**

## 6. Cổng kiểm

| | |
|---|---|
| Đồng bộ | `sync_completed_at = 2026-08-07T00:31:55` · tuổi dữ liệu **0,0 giờ** |
| Cổng tuổi dữ liệu | `[cong] DU_LIEU_TUOI` — **ĐẠT** |
| M4 | `[cong] M4_DOI_CHUNG=DAT DONG_GIA=2455 LUAT_DAT=0/105 Z_DAI=−0.33 Z_NGAY=+0.26` |
| Bảng mốc tải J5 | **không lệch** |
| Sổ quyết định | `QD-027` hết trôi sau khi đồng bộ — **đúng như dự đoán ở V11010** |

**QD-027 tự hết trôi** là bằng chứng trực tiếp cho luận điểm V11010: cổng đó báo *"bảng khuyến
cáo hôm nay rỗng"* **chính vì bản local cũ**, không phải lỗi code.

## 7. Vướng vấp

**Ba ngày dữ liệu đổi cách đọc một kết luận.** `DO_TIEN` từ 1 ngày lên 3 ngày làm z đi từ
`−1,34` lên `−0,33`/`+0,26`. Bài học: **kết luận trên n nhỏ không chỉ yếu — nó còn KHÔNG ỔN
ĐỊNH**, đổi dấu khi thêm chút mẫu.

**Hai con số lịch sử không tái lập được** (57/90 bundle thiếu phiếu → thực đo 1/93). Nghĩa là
kho báo cáo cũ có ít nhất một con số **không còn đúng hoặc không còn cùng định nghĩa**, mà chưa
ai phát hiện.

## 8. Gỡ về

Bản trước đồng bộ lưu tại `artifacts/live_sync/20260807_003101/`. Muốn quay lại chỉ cần chép
ngược — nhưng **không nên**, vì bản cũ chính là nguồn gây sai.

## 9. Theo dõi tiếp

| Mã | Nội dung | Hạn |
|---|---|---|
| **FU-303** | Nhân cổng tuổi dữ liệu (đã cài mẫu trong `do_lai_tuoi.py`) ra **mọi** script đo + nối vào sổ diễn tập DT-06 | 08/08 |
| **FU-304** | Đính chính `DO_TIEN` trong REPORT_V11003 và trang: 15/1 → **45/3**, và z **−1,34 → −0,33** | 08/08 |
| **FU-305** | **ĐÓNG** — 512 vs 8.890 là khác cửa sổ đếm (30 ngày = 2.856 · 60 ngày = 5.724 · từ 08/05 = 7.887). V10994 đếm cửa sổ hẹp hơn | 07/08 |
| **FU-307** | **"57/90 bundle thiếu phiếu" không tái lập** — thực đo 30 ngày: **1/93**. Tìm định nghĩa gốc của V10978 rồi mới kết luận | 13/08 |
| **FU-308** | **V10770 đánh dấu `SUPERSEDED`** — MB chạy theo V10895 (luôn rerun) 14/14 ngày. Hợp nhất MỘT tài liệu cơ chế 3 miền | 13/08 |
| **FU-309** | **Hơn 40 bảng cũ hơn 14 ngày**, 3 bảng RỖNG hoàn toàn. Mỗi bảng: nối lại · đánh dấu `RETIRED` · hoặc xoá. `model_latency_cost_audit_daily` dừng ghi **93 ngày** — không chỉ rỗng cột | 13/08 |
| **D2** | **CẤM viết §24** giữ nguyên. Tập khoá 7 model cho 1,66×→1,84× nhưng model/ngày cũng tăng 4,8→6,6 ⇒ **chưa đủ sạch** | — |

**Ba con số cần nhớ:** đo tiến **−1,34 → −0,33** (3 ngày thay 1 ngày) · bundle thiếu phiếu
**57/90 → 1/93** · **hơn 40 bảng** cũ hơn 14 ngày.
