# REPORT V11009 — PL19b: TỔNG LỰC LÀM RÕ & XÁC THỰC (READ-ONLY)

> **Ngày:** 2026-08-06 · **Loại:** audit READ-ONLY, 15 câu hỏi
> **Hash 4 bảng khoá:** PRE = POST · **không mutation · không deploy · không đổi số**
> **Ba đính chính báo cáo cũ theo §60:** V11001 (samday) · V11003 (n=15) · tiền đề Q12

---

## 1. Tóm tắt

Audit 15 câu theo brief PL19b. Kết quả nặng nhất là **ba đính chính vào chính báo cáo của
agent**, và **hai phát hiện mới** chưa từng được nêu:

| | |
|---|---|
| **Đính chính 1** | V11001 nói *"include_same_day=False cho TẤT CẢ trong production"* — **SAI**. Samday **đang chạy thật** |
| **Đính chính 2** | V11003 trình *"đo tiến n=15"* gây hiểu là 15 mẫu — thực ra là **15 luật × 1 NGÀY** |
| **Đính chính 3** | Tiền đề Q12 đã cũ — FU-274 đã `CLOSED_PASS`, cổng n≥12 đã nối |
| **Phát hiện mới 1** | **§5g đang thưởng +1đ cho đúng ô tệ nhất**: "3 nguồn" z=**−2,51** (vượt Bonferroni) |
| **Phát hiện mới 2** | `mined_rules` vào ML = **0 tham chiếu**, vào prompt LLM = **31** ⇒ kiến trúc **ngược 100%** so với thiết kế đích owner |

Hệ quả lịch: **FU-286 không thể thực hiện 13/08** (thiếu ~139 ngày mẫu) · **mốc chốt samday MT
dời từ 12/08 sang ~17/08** (mới có 21/28 ngày forward, và bảng đứt 2 ngày).

## 2. Owner yêu cầu gì (nguyên văn — trích brief PL19b)

> *"READ-ONLY tuyệt đối: không mutation, không deploy, không đổi số. Hash 4 bảng official
> pre=post. Mọi kết luận kèm evidence (bảng/dòng code/mốc đo/commit)."*

> *"Thiếu dữ liệu → ghi rõ thiếu gì, cần bao nhiêu ngày/mẫu nữa. CẤM suy diễn."*

> *"Sửa con số/tài liệu đã công bố → kèm TRƯỚC/SAU/PHIÊN BẢN/KIỂM theo §60."*

Thiết kế đích owner đã chốt (Q15):

> *"Đối với ML: mined rules là cơ chế CƠ HỌC/SỐ HỌC để model ML có thêm tầng chọn lọc. Đối với
> prompt LLM: phải nhét NGỮ CẢNH THÔ thật tốt để agent tự chủ động khai thác, soi xét, tính toán
> toàn bộ và output tự nhiên — KHÔNG bị gò bởi rules đã tổng hợp số sẵn."*

## 3. Đào bới / phát hiện

### 3.1 Q1 — SAMDAY: V10895 đúng, V11001 sai · `VERIFIED_CODE` + `VERIFIED_TEST`

Cờ **`include_same_day_cross=True`** đang chạy thật tại `scheduler.py` dòng **5969 · 5994 ·
6019 · 6054**, trong hàm `_rerun_free_models_after_scrape_inner` (dòng 5822). Đường xuống:
`meta_predict:92` → `_get_cross_region_momentum(include_same_day=True)` →
`meta_data_collector.py:244` `earlier_op = "<="`.

Cổng nhân quả **V10667 DRAW-ORDER GUARD** (`meta_data_collector.py:222-234`) chỉ cho miền **xổ
trước** dùng `date <= target`.

**Vì sao so 04:00 với 17:30 ra "0 cặp":** `force=True` dùng `INSERT OR REPLACE`
(`scheduler.py:2751`, `:3106`) — **4.808/4.808 khoá chỉ có 1 dòng**. Dòng 04:00 **bị ghi đè**,
đúng như V10895 mô tả.

**Nhân quả an toàn:** 413/413 dòng `rerun_post_mt` ghi lúc **17:50 (giữa)**, **0 dòng sau 18:15**.

**Ma trận 3 miền × 3 lớp:**

| miền | ML (đặc trưng) | AI (prompt) | Rules | khớp spec owner? |
|---|---|---|---|---|
| MN | KHÔNG | KHÔNG | KHÔNG | ✅ |
| MT | **CÓ MN(D)** | theo mốc gọi | **CÓ** 6 luật `MT←MN offset=D` | ✅ |
| MB | **CÓ MT(D) · THIẾU MN(D)** | theo mốc gọi | **CÓ** 6 `MB←MN D` + 8 `MB←MT D` | ⚠️ **LỆCH ở ML** |

`_ADJACENT_REGIONS[MB] = ['MT']` (`meta_data_collector.py:136`). Kênh phụ `fresh_cross_tails`
không bù được: chỉ lấy `trigger_region` (`scheduler.py:5909-5912`) và **chỉ tới LSTM**
(`lstm_predict.py:299`), không tới meta/xgb/rf.

### 3.2 Q6 — "n=15" thực ra là 1 NGÀY · `VERIFIED_TEST`

| nhãn | dòng | **ngày** | luật |
|---|---|---|---|
| `CHAM_NGUOC` | 1.695 | 113 | 105 |
| `DO_TIEN` | **15** | **1** (04/08) | 15 |
| `MO_COI` | 1.493 | 106 | 1.027 |

Luật có ≥1 dòng đo tiến: **15/105**. Có ≥5 dòng: **0/105**.
Mỗi luật chỉ được chấm vào đúng THỨ của nó ⇒ **1 lượt/tuần/luật** ⇒ để đạt 20 lượt/luật cần
**~140 ngày**.

### 3.3 Q9 — §5g thưởng đúng ô tệ nhất · `VERIFIED_TEST`

90 ngày, 3 miền, nền tính riêng từng ngày:

| mức hội tụ | lượt | trúng | tỉ lệ | nền | **z** |
|---|---|---|---|---|---|
| 1–2 nguồn | 1.925 | 639 | 33,2% | 33,8% | −0,55 |
| **3 nguồn** | 294 | 78 | **26,5%** | 33,4% | **−2,51** |
| ≥4 nguồn | 603 | 198 | 32,8% | 34,8% | −1,02 |

Bonferroni 3 phép ⇒ ngưỡng \|z\|≥2,39. **z=−2,51 vượt ngưỡng.**
Căn cứ đổi ≥4→≥3: `convergence_score` **0 chỗ**, `conv_count` **0 chỗ** trong `gpt_analyzer.py`
⇒ đổi bằng **suy luận hình thức**, không bằng đo.

### 3.4 Q8 — §22/§23: hệ số TĂNG, nhưng phép so bị nhiễu · `VERIFIED_TEST`

§23 vào code `e84494e` **29/03/2026**.

| giai đoạn | nhóm | ngày | model/ngày | số khác nhau | hệ số |
|---|---|---|---|---|---|
| TRƯỚC | tất cả | 154 | 12,8 | 7,2 | 1,77× |
| SAU | tất cả | 390 | **24,7** | 10,0 | **2,46×** |
| TRƯỚC | chỉ AI | 138 | 5,8 | 3,2 | 1,80× |
| SAU | chỉ AI | 388 | **16,8** | 6,1 | **2,74×** |
| TRƯỚC | chỉ ML | 146 | 7,8 | 4,8 | 1,63× |
| SAU | chỉ ML | 390 | 8,0 | 4,8 | 1,68× |

**Nhóm ML là phép so sạch duy nhất** (7,8→8,0 model): **1,63× → 1,68×** = không đổi — và ML
**không chịu §22/§23** vì đó là luật prompt. Nhóm AI tăng 5,8→16,8 model ⇒ **không kết luận được**.

### 3.5 Q15 — kiến trúc mined_rules NGƯỢC 100% · `VERIFIED_CODE`

| tầng | tệp | `mined_rule` xuất hiện | |
|---|---|---|---|
| **ML — đặc trưng** | `meta_data_collector.py` · `ml_predict.py` · `meta_predict.py` · `lstm_predict.py` | **0 · 0 · 0 · 0** | ❌ **KHÔNG CÓ** |
| **LLM — prompt** | `gpt_analyzer.py` | **31** | ✅ nhiều nhất |
| **Chấm điểm** | `rule_engine.py` | **8** | ✅ |

**Một luật ảnh hưởng tối thiểu 3 lần** lên cùng một con số: (1) `MINED RULES` §3 →
(2) `RULES-FIRST` ép chọn (`gpt_analyzer.py:4370`) → (3) `RULE TAILS` + `WEEKLY LIVINGNESS` +
`EVIDENCE TABLE` trình lại → (4) `rule_engine` BOOST cộng điểm lần nữa.

### 3.6 Q3 — mốc chốt samday MT không kịp 12/08 · `VERIFIED_TEST`

`v10801_ml_mark_ab_daily`: **504 dòng · 63 ngày** · 03/06 → **04/08** · ghi đều 8 dòng/ngày.
Ngày forward từ 15/07: **21/28**. **Thiếu 05/08 và 06/08** ⇒ bảng đã ngừng ghi 2 ngày.

Ba thước lệch nhau vì đo ba thứ khác nhau: V10766 **tiền, toàn wave** · V10801 **top2 hit,
per-model** · V10994 **McNemar per-day, 4 model gộp**. V10801 tách ra thấy **2 model lợi
(meta +14,3pp, xgb +11,9pp), 2 model hại (lstm −9,5, rf −4,8)** — gộp lại triệt tiêu thành
z=+1,86.

### 3.7 Q11 — P&L 100% mô phỏng · `VERIFIED_TEST`

| bảng | dòng | cờ |
|---|---|---|
| `money_board_log` | 114 | `shadow_only=1` **114/114** · `output_eligible=0` **114/114** |
| `pnl_forward_track_shadow` | 1.242 | `shadow_only=1` **1.242/1.242** |
| `pnl_daily_summary` | 14 | ⚠️ **không có cột cờ** |

### 3.8 Q5 — "65%" đúng số học, sai diễn giải · `VERIFIED_TEST`

`strongest_vs_final_shadow`: **188/288 = 65,3%** mang nhãn `BUNDLE_SKEW`. Nhưng đối chứng bốc
bừa cho MB **98,3%** so với thật **88,0%** ⇒ nhãn **không đo được** chất lượng bộ tổng hợp.

### 3.9 Q10 · Q12 · Q13 · Q14

- **Q10:** **536 chỗ** dùng `now`/`localtime` trong `web/backend/*.py`, chưa có chuẩn thống nhất.
- **Q12:** FU-274 **`CLOSED_PASS`**; `_v10991_sample_gate.chon` đã nối tại `main.py:13676`,
  `:13697`, `:13847`. Không còn `n >= 4` ở nhánh chọn số.
- **Q13:** FU-282 `MEASURED_ROOT_CAUSE` — **4 job chưa xếp lại** ⇒ MN giữ **04:00**;
  5 job 15:36–15:43 **không bị đụng**.
- **Q14:** V10996 mới đổi **1 truy vấn** (`FROM final_bundles` 39→38) — **còn 38 chỗ chưa soi**.

## 4. Hướng xử lý và vì sao chọn

**Không sửa số cũ hàng loạt (Q14)** — sửa tay hàng chục bảng tạo dị bản. Ghi chú chuẩn *"số
trước V10996 đọc theo `v_final_bundles_that`"* rẻ hơn và không sinh lỗi mới.

**Không backfill để tăng tốc đo tiến (Q6)** — đó chính là bệnh chấm ngược đang chữa.

**Tách FU-291 thành hai quyết định độc lập (Q7)** — *bỏ tính ép* làm được ngay vì chỉ cần bằng
chứng "không có lợi thế"; *tắt hẳn khối* phải chờ đủ mẫu tiến (~139 ngày).

**Gộp Q9 vào FU-291** — §5g cộng điểm theo số nguồn và RULES-FIRST ép chọn là **cùng một họ**
("prompt tự cộng điểm cho tín hiệu chưa chứng minh"), nên đi chung **một biến** theo QD-018.

**KHÔNG viết §24 chống bầy đàn (Q8)** — chưa có phép so có kiểm soát thì mọi kết luận về
§22/§23 đều vô căn cứ.

## 5. Đã làm gì

**Không sửa gì.** Chỉ chạy 4 script đo READ-ONLY (`q1.py` · `q367.py` · `q_batch.py` ·
`q89.py`), toàn bộ chỉ `SELECT` và đọc mã nguồn. Kết quả thô lưu trong `evidence/`.

Ba đính chính tài liệu ghi vào `CHANGELOG.md` · `docs/CURRENT_TRUTH_SSOT.md` theo khuôn §60
(TRƯỚC / SAU / PHIÊN BẢN / KIỂM). Bảy mục theo dõi mới/sửa ghi vào `docs/FOLLOW_UP_TRACKER.md`.

## 6. Cổng kiểm

| | |
|---|---|
| `predictions` | 11.754 dòng `96bf3180…` **PRE = POST** |
| `final_bundles` | 475 dòng `f8d7eb8f…` **PRE = POST** |
| `lottery_results` | 15.213 dòng `3c334771…` **PRE = POST** |
| `model_daily_eval` | 11.577 dòng `75fffeac…` **PRE = POST** |
| `git status web/backend/` | 3 tệp `M` — **mtime 17/07 và 02/08**, có từ trước phiên |

**STOP CONDITIONS — không kích hoạt cái nào:**

| điều kiện | trạng thái |
|---|---|
| Official nhiễm hindsight | **không** — 413/413 `rerun_post_mt` ghi trước 18:15 |
| Bundle ghi lại sau FINAL | **không** — V10993 `soi_so_bi_sua=0` |
| Cần mutation/deploy | **không thực hiện** — mọi đề xuất chờ owner ký |
| Thiếu dữ liệu | **3 chỗ**, đã ghi rõ số ngày/mẫu còn thiếu |

## 7. Vướng vấp

**Ba đính chính vào chính báo cáo của agent — khuôn §60:**

| | TRƯỚC | SAU | PHIÊN BẢN | KIỂM |
|---|---|---|---|---|
| **Samday** | *"include_same_day=False cho TẤT CẢ trong production"* | *"`include_same_day_cross=True` đang chạy thật ở `_rerun_free_models_after_scrape_inner`; MT nhận MN(D), MB nhận MT(D) nhưng **thiếu** MN(D) ở tầng ML"* | V11001 → **V11009** | `grep -n "include_same_day_cross=True" scheduler.py` → **4 dòng** |
| **Đo tiến** | *"đo tiến −1,34σ (n=15)"* | *"đo tiến mới có **1 ngày** (04/08), 15 luật × 1 lượt. **Không bác bỏ được gì** — chỉ nói chưa có bằng chứng tiến"* | V11003 → **V11009** | `SELECT COUNT(DISTINCT date) FROM mined_rule_effectiveness WHERE giai_doan='DO_TIEN'` → **1** |
| **FU-274** | brief PL19b nêu *"OWNER_LOCK, hạn 08/08, vẫn n≥4"* | *"đã `CLOSED_PASS`; cổng n≥12+Bonferroni nối tại `main.py:13676/13697/13847`"* | — → **V11009** | `_v10958_fu_reader.get_fu('FU-274')` → `CLOSED_PASS` |

**Nguyên nhân gốc của đính chính 1:** agent đọc `include_same_day` (mặc định `False` ở
`meta_data_collector.py:206`) rồi kết luận cho **cả hệ**, mà không lần theo cờ bao ngoài
`include_same_day_cross`. Đây là lỗi §60.2 câu 1 — *"ai còn trỏ tới thứ này"* — soi thiếu một
tầng gọi.

## 8. Gỡ về

**Không có gì để gỡ** — phiên này READ-ONLY, không đụng code, không đụng dữ liệu, không deploy.
Chỉ thêm tài liệu và mục theo dõi.

## 9. Theo dõi tiếp

| Mã | Nội dung | Hạn |
|---|---|---|
| **FU-286** | **DỜI** từ 13/08 → **~24/12/2026**. Đo tiến chỉ tích luỹ **1 lượt/tuần/luật**, cần ~140 ngày để mỗi luật đạt 20 lượt. Giữ song song hai bảng xếp hạng tới khi mỗi luật có ≥10 lượt | 24/12 |
| **FU-297** | **Mốc chốt samday MT DỜI 12/08 → ~17/08.** Trước đó phải tìm vì sao `v10801_ml_mark_ab_daily` đứt 05–06/08. Chốt theo **per-model (meta+xgb)**, KHÔNG gộp 4 model | 17/08 |
| **FU-298** | **§5g thưởng đúng ô tệ nhất** (3 nguồn z=−2,51, vượt Bonferroni). Gộp cùng FU-291 làm MỘT biến: bỏ cộng điểm theo số nguồn, chỉ trình số nguồn như dữ liệu | sau 20/08 |
| **FU-299** | **MB thiếu MN(D) ở tầng ML.** Thêm `'MN'` vào `_ADJACENT_REGIONS['MB']` ⇒ **phải huấn luyện lại bằng đúng cờ đó**, cấm train một kiểu serve một kiểu | sau 20/08 |
| **FU-300** | **Kiến trúc mined_rules 3 bước** theo thiết kế đích owner: (1) bỏ tính ép khỏi prompt · (2) gom 4 khối trùng còn 1 · (3) đưa rules thành đặc trưng ML — bước 3 theo M3 **bị từ chối mặc định** trừ khi kèm phép đo chứng minh khác lớp 28 đặc trưng hiện có | 3 mốc |
| **FU-294** | **ĐỔI THỂ THỨC** — quét theo **thực thể** chứ không theo từ khoá: mỗi mã (M\*, G\*, FU-\*, CP-\*) chỉ được có MỘT trạng thái trên toàn trang; ≥2 trạng thái ⇒ chặn | 13/08 |
| **FU-277** | **MỞ RỘNG 3 nhánh**: (i) 750 dòng shadow HINDSIGHT · (ii) 90 bundle làm bù · (iii) xếp hạng dùng dòng cũ 8 ngày. Thêm: **38 chỗ còn đọc thẳng `final_bundles`** | 13/08 |
| **FU-301** | Chuẩn hoá múi giờ: **536 chỗ** dùng `now`/`localtime`. Một hàm `gio_vn()` duy nhất + kiểm thử hồi quy 3 ca (UTC · +07:00 · naive) vào bộ tự kiểm 18:05 | 13/08 |
| **FU-302** | Ký hiệu **`P&L_mô_phỏng`** cho mọi con số hiện có. `pnl_daily_summary` **không có cột cờ** ⇒ thêm cờ hoặc `RETIRED` (gộp FU-254) | 13/08 |
| **Q8** | **CẤM viết §24 chống bầy đàn** trước khi có phép so khoá cùng một tập model AI cố định trước/sau 29/03 | — |

**Ba con số cần nhớ:** `mined_rules` vào ML = **0**, vào prompt = **31** · §5g thưởng ô
z=**−2,51** · đo tiến có **1 ngày**, không phải 15 mẫu.
