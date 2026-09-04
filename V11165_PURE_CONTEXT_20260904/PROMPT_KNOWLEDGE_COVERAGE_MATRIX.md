# PROMPT_KNOWLEDGE_COVERAGE_MATRIX — V11165 · GATE 2

> **Ngày:** 04/09/2026 · `CURRENT_ACTOR = CLAUDE_CODE` · **lượt sóng 1, GATE 2**
> **Phạm vi:** đọc toàn bộ di sản prompt (18 thư mục báo cáo công khai + kho tài liệu riêng + mã
> runtime đang serve + audit các lane thí nghiệm cũ), rồi đối chiếu từng mục theo mười cột.
> **Không deploy · không restart · không ghi production DB · không commit.** Mọi truy vấn DB chạy
> trên clone bất biến `artifacts/v11165_immutable.db` (`mode=ro`, `chattr +i`).
>
> **JSON máy đọc:** `/root/Lottery_AI_Test/artifacts/v11165_h2_knowledge_coverage.json`
> `sha256 = ea8b2fb9f585dc96a6617e4c470dc6ec6ed466eeddbf63bacbe06efc48672c9d` · 35 dòng ma trận.

---

## 0 · TRẢ LỜI THẲNG CÂU OWNER HỎI

> ## `AGENT_IDE_KNOWLEDGE_COVERAGE = PARTIAL`

**Không được nói «đã nắm».** Đã đối chiếu được phần lớn, nhưng **năm nguồn chưa đóng được**, và
chúng không phải chuyện nhỏ:

| # | nguồn KHÔNG đọc / KHÔNG đối chiếu được | vì sao |
|---|---|---|
| 1 | **Notion** (KNOWLEDGE LOCK bản gốc, 14 hub) | `§57.1` cấm ghi, và `V10962` ghi rõ Notion **đứng im từ 01/08/2026**. Phiên này **không đọc**. Mọi tri thức chỉ tồn tại trên Notion là **nguồn chưa đối chiếu** |
| 2 | **Lớp `create_analysis_prompt` (≈17.100–18.200 ký tự)** | luật cứng của phiên cấm gọi `create_analysis_prompt` / `build_context_pack` / `build_system_prompt` trước khi **chứng minh không có đường ghi**. Chưa chứng minh được ⇒ **không gọi**. Số ký tự từng khối của lớp này vẫn là **suy ra**, không phải **đo** |
| 3 | **Bộ cổng Wave 1** (`_v11150_unified_candidate_contract` · `_v11150_contamination_gate` · `_v11150_test_contract` · `_v11150_e2e_contract` · `_v11150_ml_pure_math_audit` · `_v11152_test_lane` · `_v11152_neo_final` · `_v11155_counterfactual` · `_v11156_ranked_adapter`) | **KHÔNG CÓ trên VPS** (có đủ trong repo local) ⇒ **không chạy lại được** để xác nhận `37/37` · `17/17` · `E2E_PASS` trên mã đang serve |
| 4 | **`FU-419`** — dòng `D-1 cross-region tail pool` và dòng chị em `tails already spent` | chưa dump lại prompt ngày 04/09 ⇒ `INDETERMINATE` |
| 5 | **Bản ghi đóng `A1` của `V11024`** | mã **và** dữ liệu đều cho thấy A1 đã được sửa, nhưng **không tìm được báo cáo nào ghi nhận việc đóng** |

---

## 1 · BỐN KẾT QUẢ NẶNG NHẤT CỦA GATE NÀY

### 1.1 🟢 Lane T-B (prompt ba tầng thuần ngữ cảnh) ĐÃ ĐỦ MẪU — và câu trả lời là **KHÔNG KHÁC BIỆT**

`V11059` khoá ngưỡng **trước** khi có dữ liệu (11/08/2026), nguyên văn: *«≥ 96 cặp bất đồng **VÀ**
|z| ≥ 1,96 · **CẤM đọc sớm** · đọc được ~27/08»*. Hôm nay là **04/09** — quá hạn đọc **8 ngày**,
lane đã chạy **25 ngày** và **chưa báo cáo nào đọc verdict**.

| | |
|---|---|
| cặp ghép | **346** (25 ngày × 5 model × 3 miền, 11/08 → 04/09) |
| **cặp bất đồng kết cục** | **101** ≥ 96 ⇒ **ĐỦ MẪU theo đúng ngưỡng đã đăng ký** |
| b (T-B cứu) / c (T-B phá) | **50 / 51** |
| **McNemar** | **z = −0,10 · p_exact = 1,000** |
| bạch thủ | T-B **33,24 %** vs CONTROL **33,53 %** ⇒ **−0,29 pp** |
| **VIF đo cho CHÍNH thước này** (RM-21) | **0,867** — bootstrap cụm theo ngày, 5.000 lần; ghép cặp đã khử hết hiệu ứng ngày, **không phồng** |
| KTC95 (bootstrap cụm ngày) | **[−5,49 ; +4,90] pp** · `z_cụm = −0,107` |
| theo miền | MB **−4,35 pp** (z −1,15) · MN **+3,42 pp** (z +0,62) · MT **0,00 pp** |
| **số chọn KHÁC NHAU** | **243 / 346 = 70,2 %** |

**Bốn phép kiểm tính hợp lệ, cả bốn ĐẠT** (làm trước khi tin con số):

| phép | kết quả |
|---|---|
| rò kết quả (`PRJ-SELECTION-WINDOW-001` mục 1) | **0 / 346** dòng chạy sau khi kết quả về · biên nhỏ nhất **5,2 phút** (MT 03/09) · trung vị **22,8 phút** |
| CONTROL có phải lượt official thật | **346 / 346 khớp** `predictions` đường official — CONTROL **đúng là prompt production** |
| tự chấm lại từ `lottery_results` (RM-11) | **346 / 346 khớp** `trung_control` và `trung_tb` |
| ba mệnh lệnh mâu thuẫn đã gỡ ở nhánh T-B | `m1_da_go = m2_da_go = m3_da_go = 1` ở **346/346** dòng |

> **Câu phải nói với owner, đúng mức bằng chứng:**
> *Prompt ba tầng thuần ngữ cảnh **đổi số được chọn ở 70,2 % số lượt**, nhưng **không đổi tỉ lệ
> trúng** — trên phép đo tiến, ghép cặp, đăng ký ngưỡng trước, đã đủ mẫu.*
>
> **Giới hạn khai trước, không giấu:** với 346 cặp, **MDE ≈ ±5 pp**. Lợi thế thật **nhỏ hơn 5 pp
> vẫn vô hình** với thước này. Và vì owner đã bỏ nhánh T-A (`V11059` §4.5), **không tách được**
> phần do *tái cấu trúc ba tầng* với phần do *gỡ ba mâu thuẫn*.

### 1.2 🟢 Phép đo bầy đàn ĐÃ ĐẠT NGƯỠNG đăng ký trước — cũng chưa ai đọc

`V11017` khoá ngưỡng **trước** khi có dữ liệu: *«CÓ TÁC DỤNG = trung bình ≥ 0,50 **và** hơn nền
≥ 0,05»*.

| nhãn | n | phân tán trung bình | cửa sổ |
|---|---|---|---|
| `NEN` | 64 | **0,4739** | 17/07 → 07/08 |
| `SAU_V11016` | **85** | **0,5763** | 07/08 → 04/09 |
| `HON_HOP` | 1 | (đã loại đúng thiết kế) | 07/08 |

⇒ `0,5763 ≥ 0,50` ✅ **và** `+0,1024 ≥ 0,05` ✅ ⇒ **verdict theo ngưỡng đã đăng ký là «CÓ TÁC DỤNG»**.

⚠️ **Nhưng đọc kèm hai điều, nếu không sẽ hiểu sai:**
① cửa sổ `SAU` gộp **nhiều biến** (V11022 · V11094 · V11106 · V11144 · V11160) ⇒ **không tách được
nhân quả**;
② `V11054` §4bis⑤ đã cảnh báo **phân tán không phải mục tiêu** — đồng thuận hiện tại mang **0 thông
tin** (34,0 → 34,4 → 33,1 → 36,4 % theo số model cùng chọn). Cộng với kết quả 1.1: **phân tán tăng,
số chọn đổi 70 %, tỉ lệ trúng không đổi.** Ba phép đo độc lập cùng chỉ một hướng.

### 1.3 🔴 «Đã gỡ hết gan/nóng/lạnh» — SAI MỘT PHẦN, sau **28 ngày**

`V11001` (06/08) báo đã gỡ; `V11024` (07/08, mục **B4/A3**) báo **chưa gỡ hết**. Đo lại hôm nay
trên mã đang serve (`gpt_analyzer.py` sha `758c29c13185763f` = GATE 0):

```
gpt_analyzer.py:2418   if prediction_mode == 'HYBRID' and STATS_AVAILABLE:
gpt_analyzer.py:2423       stat_text = format_condensed_stats(stat_analysis)
gpt_analyzer.py:2424       prompt += f"\n\n{stat_text}\n"

statistical_analyzer.py:869   lines.append("🎯 TOP 5 GỢI Ý (Score/Zone/Trend/Gan):")
statistical_analyzer.py:876   lines.append(f"⏳ GAN CAO: {gan_str}")
statistical_analyzer.py:881   lines.append(f"🔥 HOT: {', '.join(hot[:8])}")
```

**Khối này KHÔNG nằm sau `_ctx_only`.** `_ctx_only` chỉ xuất hiện ở `:2241 :2983 :3035 :3184 :3194
:6683 :6684 :6698 :6845` — **không có :2418**. Nghĩa là **cả lane official lẫn lane «ngữ cảnh
thuần» đều đang nhận một rổ TOP-5 đã xếp hạng sẵn kèm GAN CAO và HOT** — đúng thứ owner định nghĩa
là `AGGREGATED_NUMBER_SET` và cấm đưa vào prompt.

`prediction_mode == 'HYBRID'` **là nhánh production** — chứng minh bằng chính journal của
`V11159`: dòng `[Phase 11][CONTEXT_ONLY_V2] BỎ QUA…` chỉ in được từ nhánh `elif` của cùng điều
kiện đó.

### 1.4 🔴 Prompt vẫn tự nói ngược nhau — ba chỗ, cả ba trong **CẢ HAI** regime

| # | hai câu ngược nhau | dòng |
|---|---|---|
| **M1** | `SYSTEM_PROMPT`: *«đừng cộng điểm cho số chỉ vì nó xuất hiện ở nhiều nguồn»* (kèm `z = −2,54`) **vs** yêu cầu cuối: *«Đưa ra CHỐT HẠ rõ ràng — ưu tiên số xuất hiện trong NHIỀU nguồn»* | `:382` vs **`:3191`** — `:3191` nằm trong `_yc +=` **không điều kiện** |
| **M2** | `RULEBOOK §8`: *«Width > Rules > Diversity»* **vs** `§23`: *«2-3/7 AI models nên chọn SỐ KHÁC»* | `:565` vs `:764` |
| **MB** | `SYSTEM_PROMPT`: *«Không bao giờ bỏ trống số chính»* **vs** gói MB: *«accept 'SKIP' nếu evidence yếu»* / *«chỉ 1 rule match → giữ SKIP»* | `:307` vs `:5591` / `:5689` |

Cộng thêm **Phase 15** (`:2472–2526`) — **không guard** — bơm WR 7 ngày của chính model kèm câu
*«⚠️ LƯU Ý: Nếu WR thấp (<50%), hãy thay đổi chiến lược!»*. Đây đúng thứ owner cấm ở mục 5
(*không dùng win rate để đẩy LLM bắt chước nhau*), và nó **dạy đuổi nhiễu trên n = 7** (RM-04).

**Hệ quả cho bộ đo:** `_dau_o_nhiem` (`:6719-6720`) chỉ có **5 chuỗi** và **mù** với `Win Rate`
(`:2991`, viết hoa có dấu cách), `LỊCH SỬ DỰ ĐOÁN CỦA BẠN` (`:2472`), `WR hiện tại (TRỰC TIẾP)`
(`:2473`), `Số đã trúng nhiều lần trong kỳ qua` (`:2512`) và `:3191`.
⇒ **`contam_hits = 0` KHÔNG được dùng làm bằng chứng prompt sạch.**

---

## 2 · BẢNG CHỈ MỤC — 35 mục, xếp theo mức chặn

| # | source | claim (rút gọn) | current validity | conflict | action |
|---|---|---|---|---|---|
| 1 | V11001+V11007 · SO_SAU_LAN_DOI_PROMPT | «đã gỡ HẾT gan/nóng/lạnh khỏi prompt» | 🔴 **SAI MỘT PHẦN**, còn nguyên 28 ngày | `CODE_DID ≠ DOC_SAID` | `PROVEN_DEFECT` — đưa vào cờ |
| 2 | V11014 | mệnh lệnh 23→18, `ép_chọn=False` | 🟢 còn hiệu lực | — | giữ; nói rõ đo trên LỚP nào |
| 3 | V11015 · FU-320 | ML còn 6 đặc trưng gan/hot/cold | 🔴 **vẫn đúng** (`meta_predict.py:139-163`) | `OWNER_SAID ≠ CODE_DID` | `CHỜ_OWNER` (phải huấn luyện lại) |
| 4 | V11016 | L-A số thành lời kể | 🟢 còn · L-B đã gỡ (V11022) | — | giữ |
| 5 | **V11017 · bay_dan** | ngưỡng ≥0,50 & +0,05 | 🟢 **ĐẠT** 0,5763 vs 0,4739 | **chưa ai đọc verdict** | `OPERATIONAL_IMPROVEMENT` |
| 6 | V11024 L1 | 105 luật không thuộc lineage V10636 | 🟢 còn đúng (`_seed_rules.py:432`) | — | giữ LOCK |
| 7 | V11024 **A1** | bộ đếm đo tiến bị xoá mỗi thứ Hai | 🟢 **ĐÃ ĐƯỢC SỬA** (dòng đã chú thích + 251 ngày dữ liệu) | `DOC_SAID ≠ CODE_DID` | ghi ĐÍNH CHÍNH tại chỗ gốc |
| 8 | V11024 L4 / RM-14 | prompt thật 46.583 ký tự | 🟡 nguyên tắc đúng, **số đã cũ** (nay 54.000–60.500) | — | trích từ `prompt_pressure_daily` |
| 9 | V11024 R5 | RR-16.5 chỉ 7–10/28 mục có code | 🟢 còn đúng | — | đo lại trước khi cắt |
| 10 | V11054 | hai nút thắt SINH / CHỌN | 🔴 còn đúng — `§11:639` + `§18:675` vẫn khoá tầng SINH | `§4:542` vs `§11:639` | `CHỜ_OWNER` (B3/P1, treo từ 09/08) |
| 11 | V11054 | `MINED_RULES_MODE='soft'` cộng +0,15 | 🔴 **còn nguyên** (`main.py:124/128`) | `DOC_SAID ≠ CODE_DID` | `CHỜ_OWNER` — **mục lớn nhất chưa ai động** |
| 12 | V11054 | `loi_the(k)` phẳng · MDE 15,1 pp | 🟢 tái xác nhận bởi V11116 + V11164 | — | dùng ĐỘ PHỦ + `loi_the(k)` làm thước |
| 13 | V11055+V11057 | `_apply_hot_cold_post_filter` ×0,3 | 🔴 **còn 4 điểm gọi sống** | `OWNER_SAID ≠ CODE_DID` | `CHỜ_OWNER` (QD-041 hết hạn 21/08) |
| 14 | **V11059 M1** | prompt tự nói ngược về «nhiều nguồn» | 🔴 **còn nguyên** cả hai regime | `PRJ_PROMPT_CONTRADICTS` | `PROVEN_DEFECT` — ưu tiên nhất |
| 15 | **V11059 M2** | `§8` xếp `Rules > Diversity` | 🔴 còn nguyên | `PRJ_PROMPT_CONTRADICTS` | `PROVEN_DEFECT` |
| 16 | **V11059 M3** | de-herding làm nửa chừng | 🟡 Phase 14A đã vào cờ · **Phase 15 chưa** | owner mục 5 | `PROVEN_DEFECT` |
| 17 | **V11059 lane T-B** | ngưỡng ≥96 cặp & \|z\|≥1,96 | 🟢 **ĐỦ MẪU 101/96** | — | đọc verdict (mục 1.1) |
| 18 | **KẾT QUẢ T-B (phiên này)** | — | 🟢 **KHÔNG KHÁC BIỆT** z=−0,10 | — | trình owner |
| 19 | V11101 · BAN_DO | 32 khối: GIỮ 7 / DỊCH 7 / BỎ 15 | 🟢 cơ chế đúng | de-herding để lọt 4 khối cùng loại | đo lại trước khi dùng làm kế hoạch |
| 20 | V11101 | rút lại 2 ca (5,8/4,6/26,5 %; z=2,81) | 🟢 đã rút đúng chỗ | — | giữ làm mẫu |
| 21 | V11105 | FU-419 dòng D-1 tail pool | ⚪ **chưa xác minh** | — | `INDETERMINATE` |
| 22 | V11105 | dòng `tails already spent` | ⚪ **chưa xác minh** | — | `INDETERMINATE` |
| 23 | V11144 | cổng mồ côi CHẶN → ĐẠT | 🟢 còn đúng | — | chạy lại sau khi chứng minh side-effect |
| 24 | V11150 | Phase 14A là ổ contamination | 🟢 đã vào cờ đúng (`:3035`) | — | giữ |
| 25 | V11150 | UCC · emitter · cổng contamination | 🟡 `CODED_AND_TESTED_NOT_RUNTIME_PROVEN` | 9 tệp cổng **không có trên VPS**; `unified_candidate_sets` **không tồn tại**; grep `UCC` = **0/4.440** | ghi rõ cổng chạy ở LOCAL hay VPS |
| 26 | V11152 | cờ ngữ cảnh thuần theo lane | 🟢 còn đúng (`:910-932`) | mục 3.2 **đã bị rút lại** | giữ cờ; cấm trích bảng 3.2 |
| 27 | V11155 | biên non-inferiority · 17,4 năm | 🟢 còn đúng | — | lý do **cấm** hứa «prompt mới tốt hơn» |
| 28 | V11157 | 3-càng = prefix + BT | 🟢 `SUBSTANTIALLY_VALID` | rút lại `NO_VALID_3CANG` | giữ |
| 29 | V11159 | rò prompt thí nghiệm vào official | 🟢 đã vá phần **regime** | — | giữ |
| 30 | V11160 | vân tay prompt runtime | 🔴 **băm SAI vị trí** (`:6723` trước `:6755-6762`) | `DOC_SAID ≠ CODE_DID` ngay trong cùng khối mã | `CHỜ_OWNER` (FU-450) |
| 31 | V11160/V11164 | bộ 5 dấu ô nhiễm | 🔴 **KHÔNG ĐỦ** — mù ≥ 4 chuỗi có thật | — | `PROVEN_DEFECT` — cấm dùng `contam=0` |
| 32 | V11164 | `:6738` còn định tuyến theo MODEL | 🔴 **còn nguyên** | dễ đọc nhầm thành **một** công tắc | `CHỜ_OWNER` (FU-450) |
| 33 | BAN_DO 1.4 | hai câu MB ngược luật owner | 🔴 còn nguyên | `PRJ_PROMPT_CONTRADICTS` (chỉ MB) | `PROVEN_DEFECT` |
| 34 | ai_context_shadow_contract | 4 khối shadow đã DONE | 🟡 5 mục `OWNER_LOCK` treo **5 tháng** | BAN_DO đề xuất **BỎ** Block 1+2 | `CHỜ_OWNER` |
| 35 | `PHASE_FIRST_JSON_CONTRACT` | khối đã bỏ 25/06 | 🟢 đúng — `PHASE_FIRST_CONTRACT_MODELS = set()` ⇒ `:6762` **không bao giờ chạy** | — | `EXPECTED_BEHAVIOR` — ghi vào sổ |

---

## 3 · MA TRẬN ĐẦY ĐỦ MƯỜI CỘT

Bản đầy đủ (mọi dòng đủ **source · owner intent · claim · code implementation · runtime proof ·
current validity · superseded by · conflict · missing evidence · action**) nằm ở
`artifacts/v11165_h2_knowledge_coverage.json`, khoá `ma_tran`, **35 phần tử**.
Dưới đây trích **bảy dòng chặn nặng nhất**, đủ mười cột.

### 3.1 · `format_condensed_stats` vẫn bơm rổ số dọn sẵn

| cột | nội dung |
|---|---|
| **source** | `V11001` + `V11007` (06/08) · `docs/SO_SAU_LAN_DOI_PROMPT.md` |
| **owner intent** | 06/08: *«gan, cold, hot chả tích sự gì»* |
| **claim** | «đã gỡ HẾT gan/nóng/lạnh khỏi prompt (8 khối, rồi 10 chỗ sót)» |
| **code implementation** | `gpt_analyzer.py:2418-2424` → `statistical_analyzer.py:869 · :876 · :881`. **Không** nằm sau `_ctx_only` |
| **runtime proof** | sha `758c29c13185763f` = GATE 0; `prediction_mode=='HYBRID'` là nhánh production (journal V11159) |
| **current validity** | 🔴 **SAI MỘT PHẦN — còn nguyên sau 28 ngày** |
| **superseded by** | `V11024` B4/A3 (07/08) đã báo; **chưa bản nào đóng** |
| **conflict** | `CODE_DID ≠ DOC_SAID` — sổ ghi «giữ» cho V11001 |
| **missing evidence** | chưa đo được số ký tự khối condensed trong prompt thật |
| **action** | `PROVEN_DEFECT` — đưa vào cờ; `A58_VIOLATION_HALF_DONE` |

### 3.2 · `:3191` ra lệnh bầy đàn trong cả hai regime

| cột | nội dung |
|---|---|
| **source** | `V11059` (11/08) mục M1 |
| **owner intent** | *«prompt chuẩn đâu mà đòi AI tốt hơn ML»* |
| **claim** | `SYSTEM_PROMPT` cấm cộng điểm đa nguồn (`z = −2,54`) nhưng thân phân tích **ra lệnh** ưu tiên nhiều nguồn |
| **code implementation** | `:382` vs **`:3191`**; `:3191` trong `_yc +=` **không điều kiện** |
| **runtime proof** | `_ctx_only` chỉ ở `:2241 :2983 :3035 :3184 :3194 :6683 :6684 :6698 :6845` |
| **current validity** | 🔴 **còn nguyên sau 24 ngày**, kể cả lane «ngữ cảnh thuần» |
| **superseded by** | — |
| **conflict** | `PRJ_PROMPT_CONTRADICTS` |
| **missing evidence** | chưa đo model nghe câu nào |
| **action** | `PROVEN_DEFECT` — ưu tiên nhất của mọi việc dọn prompt |

### 3.3 · Phase 15 bơm WR của chính model

| cột | nội dung |
|---|---|
| **source** | `V11059` M3 · phát hiện mở rộng trong phiên này |
| **owner intent** | mục 5: *không dùng tên model · win rate · trọng số để đẩy LLM bắt chước nhau* |
| **claim** | de-herding chỉ cắt context pack, không chạm thân phân tích |
| **code implementation** | Phase 14A `:3040-3043` **đã** có `if not _ctx_only` `:3035`; **Phase 15 `:2472-2526` không có guard nào** |
| **runtime proof** | đọc tệp đang serve, sha khớp GATE 0 |
| **current validity** | 🟡 **SỬA MỘT PHẦN** |
| **superseded by** | `V11150` đặt Phase 11/14A sau cờ |
| **conflict** | `OWNER_SAID ≠ CODE_DID` |
| **missing evidence** | chưa đo số ký tự Phase 15 trong prompt thật |
| **action** | `PROVEN_DEFECT` — đưa Phase 15 vào cùng cờ `_ctx_only` |

### 3.4 · `MINED_RULES_MODE = 'soft'`

| cột | nội dung |
|---|---|
| **source** | `V11054` (09/08) §5bis④ · D2 · B4 · P2 |
| **owner intent** | *«gan +điểm làm anh bực»* — cùng nguyên tắc, quy mô lớn hơn |
| **claim** | hệ đang cộng **+0,15** cho bộ luật mà tài liệu ghi **0/105 qua cổng**, trên nền đã phồng **+12 pp** — ⚠️ **ĐÍNH CHÍNH · KẾT LUẬN ĐÃ RÚT LẠI (`RL-002`):** câu *«0/105 qua cổng»* là **SAI**. Sự thật: **8/105 luật đạt `READY_STRONG`**; câu đúng phải là *«0/105 kiểm NGOÀI MẪU»* — hai mệnh đề khác hẳn nhau (một cái nói luật không đạt tiêu chuẩn nào, cái kia nói chưa có kiểm ngoài mẫu). Trích ở đây **chỉ để ghi lại nguyên văn tài liệu gốc**, KHÔNG dùng làm căn cứ. Xem `docs/SO_RUT_LAI.json` mục `RL-002` |
| **code implementation** | `main.py:124 MINED_RULES_MODE='soft'` · `:128 MINED_RULES_APPLY_TO='all'` |
| **runtime proof** | đọc trực tiếp tệp đang serve, sha `4ed5fd7ebaee8d23` = GATE 0 |
| **current validity** | 🔴 **còn nguyên sau 26 ngày** |
| **superseded by** | — |
| **conflict** | `DOC_SAID ≠ CODE_DID` — `KNOWLEDGE LOCK §8` vs mã |
| **missing evidence** | chưa đo ảnh hưởng định lượng của boost 0,15 lên bạch thủ |
| **action** | `CHỜ_OWNER` — một dòng, có đường lui ngay; **mục lớn nhất chưa ai động** |

### 3.5 · Vân tay prompt băm sai vị trí

| cột | nội dung |
|---|---|
| **source** | `V11160` (04/09) · `V11164` §3.4 |
| **owner intent** | *«không suy luận lấp chỗ trống — không có raw evidence thì ghi NOT PROVEN»* |
| **claim** | ba trường vân tay «băm CHÍNH chuỗi sắp gửi đi» |
| **code implementation** | `:6723-6726` băm `system_prompt + '<<<USER>>>' + prompt`; nhưng `:6755 prompt += _ctx_pack` · `:6760 += REASONING_RULEBOOK` · `:6762 += PHASE_FIRST_JSON_CONTRACT` xảy ra **SAU** |
| **runtime proof** | đọc tệp đang serve |
| **current validity** | 🔴 **SAI MỘT PHẦN** — chú thích `:6716` tự khai ngược với hành vi |
| **superseded by** | `V11164` đo được: phủ **48,2 %** (24.435 / 50.658), thiếu **26.223** ký tự |
| **conflict** | `DOC_SAID ≠ CODE_DID` ngay trong cùng một khối mã |
| **missing evidence** | — |
| **action** | `CHỜ_OWNER` (FU-450) — chuyển phép băm xuống sau `:6762` |

### 3.6 · Bộ cổng Wave 1 không có trên production

| cột | nội dung |
|---|---|
| **source** | `V11150` (02/09) · `V11152` · `V11155` · `V11156` |
| **owner intent** | `V.2`: *«không chấp nhận emitter tiếp tục bỏ 7.935 ký tự SYSTEM_PROMPT»* |
| **claim** | `UNIFIED_CANDIDATE_CONTRACT` **37/37** · contamination gate **17/17** · `E2E_PASS` **trên dữ liệu production** |
| **code implementation** | trên VPS **có** `_v11150_full_emitter.py`, `_v11155_vai_tro_theo_thoi_diem.py`, `_v11160_test_lane.py`, `_v11161_rank_gen.py`, `_v11162_lo3_lineage.py`; **không có** 9 tệp cổng còn lại (đủ trong repo local) |
| **runtime proof** | bảng `unified_candidate_sets` **không tồn tại** trong 254 bảng DB production; grep `unified_candidate\|UCC` = **0 hit / 4.440 tệp** trên VPS |
| **current validity** | 🟡 `CODED_AND_TESTED_NOT_RUNTIME_PROVEN` — **đúng như V11150 tự khai** |
| **superseded by** | — |
| **conflict** | các cổng đó **không chạy lại được** trên production |
| **missing evidence** | chưa rõ `37/37` và `17/17` chạy ở LOCAL hay VPS |
| **action** | `OPERATIONAL_IMPROVEMENT` — mọi báo cáo sau **phải ghi rõ cổng chạy ở đâu** |

### 3.7 · `A1` của V11024 đã được sửa mà không ai ghi nhận

| cột | nội dung |
|---|---|
| **source** | `V11024` (07/08) OPEN ITEM **A1** — nút thắt được xếp hạng **cao nhất** toàn phiên đó |
| **owner intent** | — |
| **claim** | `weekly_rule_miner.py:170` xoá 112 ngày `mined_rule_effectiveness` ⇒ *«mọi kế hoạch đo thêm N ngày là bất khả thi về cấu trúc»* |
| **code implementation** | `weekly_rule_miner.py:171` nay là **dòng chú thích**: `#     c.execute("DELETE FROM mined_rule_effectiveness WHERE date >= date('now','-112 days')")` |
| **runtime proof** | `mined_rule_effectiveness` giữ **251 ngày phân biệt**, `2025-12-20 → 2026-09-04`, n = **5.035** |
| **current validity** | 🟢 **ĐÃ ĐƯỢC SỬA** — hai neo độc lập |
| **superseded by** | không xác định được bản nào đóng |
| **conflict** | `DOC_SAID ≠ CODE_DID` — `V11024` NEXT ACTION vẫn đứng «owner quyết A1» |
| **missing evidence** | không tìm được commit / báo cáo đóng A1 |
| **action** | `OPERATIONAL_IMPROVEMENT` — ghi ĐÍNH CHÍNH tại chỗ gốc |

---

## 4 · AUDIT CÁC LANE THÍ NGHIỆM CŨ

| lane / bảng | dòng | cửa sổ | writer / cron | reader sống | panel | trạng thái |
|---|---|---|---|---|---|---|
| **`prompt_3tang_ab_shadow_v11059`** | **346** | 11/08 → **04/09** | `_v11059_lane_ab_3tang.py` · cron **06:00 MN · 17:15 MT · 18:05 MB** | `main.py:18503` (`/api/admin/prompt-3tang-ab` `:18471`) | `monitoring.html:2599` `sectionPrompt3Tang`, có trong **cả** `loadAllSections` **lẫn** `setInterval` | 🟢 **SỐNG · ĐỦ MẪU · CHƯA AI ĐỌC VERDICT** |
| **`bay_dan_daily_shadow`** | **150** | 17/07 → **04/09** | `_v11017_bay_dan_shadow.py` · cron **19:05** | `main.py:22119` `from _v11017_bay_dan_shadow import view` (`/api/admin/bay-dan-shadow` `:22114`) | `monitoring.html:2198` `sectionBayDan` | 🟢 **SỐNG · ĐẠT NGƯỠNG · CHƯA AI ĐỌC** |
| **`gan_hoi_tu_shadow_v11055`** | **567** | 28/02 → **04/09** | `_materialize_gan_hoi_tu_shadow.py` · cron **21:40** | `main.py:18741` · `:18772` (`/api/admin/gan-hoi-tu-shadow` `:18700`) | `monitoring.html:2682` `sectionGanHoiTu` | 🟢 sống — FU-394 chưa đọc |
| **`PROMPT_V2_AB_V1`** | — | 05/07 → 01/08 (79 cặp) | `_v10781_prompt_v2_lane.py` (`EXP_NAME`) | — | — | 🔴 **KHÔNG có bảng mang tên đó** trong 254 bảng; cron đã tắt **01/08**. Là **tên thí nghiệm**, không phải tên bảng (`RM-10`) |
| **`unified_candidate_sets`** (UCC) | **0** | — | `_v11150_unified_candidate_contract.py` (**chỉ local**) | — | — | 🔴 **bảng không tồn tại trên production** |
| **`prompt_pressure_daily`** | **7.368** | 22/04 → **04/09** | `main.py:2499 INSERT OR REPLACE` | `_materialize_v95_data_integrity_audit.py:343` | — | 🟢 sống — **nguồn số ký tự prompt đáng tin nhất hiện có** |
| **`prompt_section_breakdown_daily`** | **46.160** | 22/04 → **04/09** | `_materialize_prompt_section_breakdown.py:153` | **0 điểm đọc tìm được** | — | 🟡 `SUSPICIOUS` — ghi đều 4,5 tháng, chưa tìm được ai đọc (`RM-20`) |
| **`mined_rule_effectiveness`** | **5.035** | 20/12/2025 → **04/09** | `weekly_rule_miner.py` | — | — | 🟢 **251 ngày** — A1 đã hết hiệu lực |
| **`gan_signal_shadow_v100`** | **246.000** | — | ngừng ghi **09/05** | — | — | 🔴 chết từ 09/05, chưa ai nêu lý do (`V11054` C2) |
| **`loz_stage_trace_shadow`** | **6.356** | 05/03 → **05/05** | — | — | — | 🔴 ngừng ghi 05/05 |

> ⚠️ **Tự sửa trong phiên:** bản quét điểm đọc **đầu tiên** báo `prompt_3tang_ab_shadow_v11059` và
> `gan_hoi_tu_shadow_v11055` **chỉ có điểm đọc trong `backups/` và `artifacts/`** — **SAI**, do giới
> hạn 25 dòng mỗi nhóm và thứ tự duyệt thư mục. Kiểm lại **trực tiếp trên `main.py` đang serve**:
> **có đủ** endpoint và **có đủ** panel đăng ký `setInterval`. Ghi lại để không ai trích bản quét đầu.

---

## 5 · ĐẦU VÀO CHO LÀN SÓNG 2

1. **Đọc hai verdict đã đủ mẫu** (mục 1.1 và 1.2) — cả hai **đã đăng ký ngưỡng trước**, nên đọc bây
   giờ là **hợp lệ**, không phải bẻ ngưỡng. Trình owner nguyên văn con số, kèm MDE ±5 pp.
2. **Bốn chỗ prompt tự mâu thuẫn còn sống** (`:3191` · `§8:565` · MB `:5591`/`:5689` · Phase 15
   `:2472-2526`) và **một rổ số dọn sẵn còn sống** (`:2418-2424`) — đây là **danh sách thi hành**
   cho bất kỳ định nghĩa «PURE CONTEXT» nào. Không dọn năm chỗ này thì mọi phép đo prompt tiếp theo
   đều đang đo một thay đổi **làm nửa vời** (`§60.1`).
> ⚠️ **Cố ý trích MỘT cửa sổ** (`PRJ-SELECTION-WINDOW-001` · RM-18). Phiên này **không** tuyên bố
> hiệu quả của luật khai mỏ, nên cả bốn vế — **trong cửa sổ chọn · ngoài cửa sổ chọn · trong mẫu ·
> ngoài mẫu** — đều để trống có chủ ý. Bộ đủ nằm ở **RM-18/V11030** (**+7,5 / +13,8 / +20,7 điểm
> TRONG cửa sổ chọn, ĐÚNG BẰNG 0 ngoài cửa sổ**) và **V11073** (**+9,9% trong mẫu → −1,6% ngoài
> mẫu**). Đo bổ sung của phiên này: **n = 20/miền trên 4 ngày** ⇒ **RM-04, chưa được phép kết
> luận**; KTC95 đều chứa 0. Báo một vế là giấu mất nửa sự thật.
3. **Ba mục `CHỜ_OWNER` cũ hơn 3 tuần**: `MINED_RULES_MODE` (26 ngày) · 6 đặc trưng ML gan/hot/cold
   (28 ngày) · `_apply_hot_cold_post_filter` (cửa sổ đóng băng QD-041 **đã hết hạn 21/08**).
4. **Trước khi nâng bất kỳ verdict prompt nào:** phải chứng minh `build_context_pack` /
   `create_analysis_prompt` **không có đường ghi**, rồi mới dump được lớp `create_analysis_prompt`.
   Chừng nào chưa dump, mọi con số về lớp đó là **suy ra**, không phải **đo** (`RM-14`).
5. **`contam_hits = 0` phải ngừng được dùng làm bằng chứng** cho tới khi bộ dấu phủ được ít nhất
   bốn chuỗi đang bị mù.

---

## 6 · CỔNG AN TOÀN CỦA CHÍNH GATE NÀY

| phép | kết quả |
|---|---|
| ghi production DB | **0** — mọi kết nối `sqlite3.connect(..., mode=ro, uri=True)` trên clone bất biến |
| deploy / restart / sửa tệp trong `web/backend` | **0** |
| git commit / push | **0** |
| ghi Notion | **0** |
| gọi provider LLM | **0** |
| gọi `build_context_pack` / `create_analysis_prompt` / `build_system_prompt` | **0** — chưa chứng minh được không có đường ghi ⇒ **không gọi**, chỉ đọc mã |
| tệp ghi trên VPS | chỉ trong `/root/Lottery_AI_Test/artifacts/` |
| hash mã đang serve so GATE 0 | **khớp 10/10** (`gpt_analyzer 758c29c13185763f` · `main 4ed5fd7ebaee8d23` · `combo_super 47047b1dc0b7e0b9` · `scheduler 2961987d8c3a6e27` · …) |

---

> ⚠️ **Cố ý trích MỘT cửa sổ** (`PRJ-SELECTION-WINDOW-001` · RM-18). Phiên này **không** tuyên bố
> hiệu quả của luật khai mỏ, nên cả bốn vế — **trong cửa sổ chọn · ngoài cửa sổ chọn · trong mẫu ·
> ngoài mẫu** — đều để trống có chủ ý. Bộ đủ nằm ở **RM-18/V11030** (**+7,5 / +13,8 / +20,7 điểm
> TRONG cửa sổ chọn, ĐÚNG BẰNG 0 ngoài cửa sổ**) và **V11073** (**+9,9% trong mẫu → −1,6% ngoài
> mẫu**). Đo bổ sung của phiên này: **n = 20/miền trên 4 ngày** ⇒ **RM-04, chưa được phép kết
> luận**; KTC95 đều chứa 0. Báo một vế là giấu mất nửa sự thật.
TanPhatAI cần làm: ghi **`AGENT_IDE_KNOWLEDGE_COVERAGE = PARTIAL`** — **cấm ghi «đã nắm»**; năm nguồn chưa đóng nêu ở mục 0 (Notion không đọc · lớp `create_analysis_prompt` chưa dump được · 9 cổng Wave 1 không có trên VPS · FU-419 chưa xác minh · không tìm được bản đóng A1). Ghi **hai verdict đã ĐỦ MẪU theo ngưỡng ĐĂNG KÝ TRƯỚC và chưa báo cáo nào đọc**: ① lane T-B `prompt_3tang_ab_shadow_v11059` — **101 ≥ 96 cặp bất đồng**, **z = −0,10 · p = 1,00**, T-B **33,24 %** vs CONTROL **33,53 %**, **VIF = 0,867 đo cho chính thước này**, KTC95 **[−5,49; +4,90] pp**, và **70,2 % số lượt ĐỔI SỐ CHỌN mà tỉ lệ trúng không đổi** — bốn phép kiểm hợp lệ đều đạt (0/346 rò kết quả, CONTROL khớp official 346/346, tự chấm lại khớp 346/346); ② `bay_dan_daily_shadow` — **0,5763 vs nền 0,4739 (+0,1024)** ⇒ **ĐẠT** ngưỡng V11017, nhưng là **đo GỘP nhiều biến**. Ghi **năm chỗ prompt còn vi phạm định nghĩa PURE CONTEXT trên mã đang serve**: `gpt_analyzer.py:2418-2424` (rổ TOP-5 + GAN CAO + HOT, **không** sau `_ctx_only`) · `:3191` (ra lệnh ưu tiên nhiều nguồn, ngược `:382`) · `§8:565` (`Rules > Diversity`) · MB `:5591`/`:5689` (SKIP ngược `:307`) · Phase 15 `:2472-2526` (WR 7 ngày + «WR thấp thì đổi chiến lược»). Ghi **`contam_hits = 0` KHÔNG còn là bằng chứng** — bộ 5 dấu mù với `Win Rate` · `LỊCH SỬ DỰ ĐOÁN CỦA BẠN` · `WR hiện tại (TRỰC TIẾP)` · `Số đã trúng nhiều lần` · `:3191`. Ghi **ba mục CHỜ_OWNER quá 3 tuần**: `MINED_RULES_MODE='soft'` (26 ngày) · 6 đặc trưng ML gan/hot/cold (28 ngày) · `_apply_hot_cold_post_filter` (QD-041 **đã hết hạn 21/08**). Ghi **ĐÍNH CHÍNH A1 của V11024**: `weekly_rule_miner.py:171` DELETE **đã bị chú thích** và `mined_rule_effectiveness` giữ **251 ngày** ⇒ A1 **đã được sửa**, nhưng **không tìm được bản ghi nhận**. Ghi **9 tệp cổng Wave 1 không có trên VPS** và **`unified_candidate_sets` không tồn tại trong DB production** (grep `UCC` = 0/4.440 tệp) ⇒ `V11150` giữ đúng nhãn `CODED_AND_TESTED_NOT_RUNTIME_PROVEN`. Ghi **tự sửa trong phiên**: bản quét điểm đọc đầu báo hai bảng «không ai đọc» là **SAI** — kiểm lại trên `main.py` đang serve thì **có đủ** endpoint và panel. **Phiên này: 0 ghi production · 0 deploy · 0 restart · 0 commit · 0 gọi provider.**
