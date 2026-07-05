# V10781 — GĐ2 THỰC THI THEO CHỮ KÝ OWNER + UI AUTO-DISPLAY + §52G GITHUB-FIRST + DỌN ROOT/VPS + PROMPT CONTEXT V2 (SHADOW)

- **Ngày:** 2026-07-05 (Asia/Ho_Chi_Minh) · **Kế thừa:** V10780 GĐ1 (PASS 7/7, zero runtime change)
- **Phạm vi:** thực thi ĐÚNG các dòng owner đã ký trong PHẦN 0 (E1→E6b) + PHẦN 2/3/4/5/6
- **Backup:** `backups/v10781_pre/` (15 file) · **Deploy:** VPS qua `web/backend/_v10781_deploy.py` (10 bước có bằng chứng)
- **Chính sách báo cáo:** đây là BẢN GỐC chi tiết theo §52G (GitHub-first); Notion chỉ 1 trang tóm tắt ≤30 dòng

---

## 0. TÓM TẮT 10 DÒNG

1. **E6b FIX-2 áp official:** 3 query đọc đài giới hạn 84 ngày → prompt MN Chủ Nhật từ **5 đài SAI → đúng 3 đài** (Tiền Giang, Kiên Giang, Đà Lạt); diff PRE/POST 3 miền đính kèm.
2. **E6a FIX-1+FIX-3 áp official:** nhãn nguồn MN chuẩn `MB(D-1)/MT(D-1)/MN(D-1)` + câu ràng buộc miền trong YÊU CẦU.
3. **E5 KỊP DEADLINE — KHÔNG fallback:** /choi MN tuần 06/07 = BT 1-SỐ nguồn official bạch-thủ, NGHỈ T7 code tường minh + lý do trên UI, vốn theo lịch đài THẬT (2.7M/ngày 3 đài).
4. **E2+E4a:** đăng ký `qwen3.7-max` + `glm-5.2` SHADOW_AUTO (first_run 06/07, smoke thật OK) → SHADOW_AUTO 8→**10**, output-eligible **15/15 KHÔNG đổi**.
5. **E3a/b/c:** bật `reasoning effort=high` cho qwen3-max-thinking (+max_tokens 32,768), grok-4.20 (**sửa slug đúng bản multi-agent**), gpt-5.5; mốc `thinking_enabled_date=2026-07-05` ghi vào registry.
6. **PHẦN 2:** display_name 1 nguồn duy nhất (registry) + endpoint `/api/model-display-names` + `model-names.js`; 7 trang UI bỏ hardcode.
7. **PHẦN 3:** chính sách §52G GITHUB-FIRST ghi vào 3 rule files (áp dụng từ báo cáo này).
8. **PHẦN 4:** archive 10 script one-off + 4 file .bak VPS rời cây serve (manifest sha256) — **KHÔNG XÓA GÌ**; danh sách đề-xuất-xóa trình riêng.
9. **PHẦN 5:** Context Pack V2 + lane A/B `PROMPT_V2_AB_V1` (deepseek-reasoner, 1 biến duy nhất) chạy cron 3 miền, **$0.134/ngày**, run thật đầu tiên OK.
10. **Hash 4 bảng official PRE = POST IDENTICAL 4/4** — zero đụng dữ liệu official.

---

## 1. PHẦN 1 — THỰC THI THEO CHỮ KÝ (thứ tự E6b → E6a → E5 → E2/E3/E4a)

### 1.1 Hash PRE tươi (trước thay đổi đầu tiên) và POST (sau toàn bộ)

| Bảng | Rows | SHA256 | PRE 11:23:58 | POST 14:30:11 |
|---|---|---|---|---|
| predictions | 9,304 | `5e92c59ef7ab274facde6f9c8025a9b360e433dbfb3710d2976d9447fe24131e` | ✔ | ✔ IDENTICAL |
| final_bundles | 382 | `1bef9c34635ba9510514b61d7606dab27a1c854a431537566b447631d4e9b9a3` | ✔ | ✔ IDENTICAL |
| lottery_results | 15,010 | `2076e8f7675ef90f2d00717304c8dec84d323bfa65e48d04f5bbe467f2e44d51` | ✔ | ✔ IDENTICAL |
| model_daily_eval | 9,132 | `cbd1f56854cf0356999da4c6e8e87f081d6721446094c8f0bb8fb0bb0e7422b7` | ✔ | ✔ IDENTICAL |

### 1.2 E6b FIX-2 — query đài giới hạn 84 ngày (CHỈ QUERY ĐỌC)

**3 điểm sửa:**
- `web/backend/gpt_analyzer.py` — header prompt (`create_analysis_prompt`): `SELECT DISTINCT station … AND date >= date(?, '-84 day') AND date <= ?` anchor theo ngày dự đoán.
- `web/backend/gpt_analyzer.py` — trace bucket context (`_build_trace_bucket_context`): cùng cửa sổ 84 ngày.
- `web/backend/main.py` — `_get_region_weekday_station_set(anchor_date)`: bucket label API dùng cùng cửa sổ (fix `target_station_set_label`).

**Kết quả prompt MN Chủ Nhật (bằng chứng diff `artifacts/v10781_prompt_audit/`):**
- TRƯỚC: 5 đài — Tiền Giang, Kiên Giang, Đà Lạt, **Khánh Hòa (SAI - của MT), Kon Tum (SAI - của MT)** (nhiễm từ 229 rows 2020–21 gán region='MN' sai).
- SAU: **3 đài — Tiền Giang, Kiên Giang, Đà Lạt** ✔ khớp thực tế sau sáp nhập tỉnh.

**Lịch đài 7 ngày × 3 miền sau FIX-2 (script `_v10781_station_calendar.py`, cửa sổ 84d đến 05/07):**

| Thứ | MN | MT | MB |
|---|---|---|---|
| T2 | TP.HCM, Đồng Tháp, Cà Mau | Phú Yên, Thừa T. Huế | Hà Nội |
| T3 | Bến Tre, Vũng Tàu, Bạc Liêu | Đắk Lắk, Quảng Nam | Quảng Ninh |
| T4 | Đồng Nai, Cần Thơ, Sóc Trăng | Đà Nẵng, Khánh Hòa | Bắc Ninh |
| T5 | Tây Ninh, An Giang, Bình Thuận | Bình Định, Quảng Trị, Quảng Bình | Hà Nội |
| T6 | Vĩnh Long, Bình Dương, Trà Vinh | Gia Lai, Ninh Thuận | Hải Phòng |
| T7 | TP.HCM, Long An, Bình Phước, Hậu Giang (4 đài) | Đà Nẵng, Quảng Ngãi, Đắk Nông | Nam Định |
| CN | Tiền Giang, Kiên Giang, Đà Lạt | Kon Tum, Khánh Hòa, Thừa T. Huế | Thái Bình |

**229 rows 2020–21 gán nhầm miền:** theo chữ ký — KHÔNG sửa bảng official; ghi data-annotation note; FU xử lý riêng có giám sát (nằm trong checkpoint 14/07).

### 1.3 E6a FIX-1 + FIX-3 — nhãn nguồn MN + câu ràng buộc miền

- **FIX-1:** `scheduler.py` specs miền MN dùng key thô `MB/MT/MN` với nhãn `MB(D-1) <ngày>` / `MT(D-1) <ngày>` / `MN(D-1) <ngày>` (trước đây nhãn "ƯU TIÊN ?" không rõ nguồn-ngày); `gpt_analyzer.py` header nguồn thêm "(HÔM QUA)" khi target=MN — hết mơ hồ D-1.
- **FIX-3:** khối `## YÊU CẦU:` thêm câu ràng buộc: dự đoán CHỈ cho miền target, dữ liệu miền khác chỉ để tham khảo pattern — chặn model "lai" kết quả giữa miền.
- Cả hai áp official (đã ký E6a), có mặt trong prompt POST cả 3 miền (diff đính kèm).

### 1.4 E5 — /choi MN tuần 06/07 = BT 1-SỐ OFFICIAL (KỊP deadline 00:00)

**Code:** `web/backend/_v10759_money_board.py` — method mới `MN_BT1_OFFICIAL_V1`, hằng số tường minh:
- `MN_BT1_METHOD = "MN_BT1_OFFICIAL_V1"`, `MN_BT1_START_WEEK = "2026-07-06"`, `MN_BT1_SKIP_WEEKDAY = 5` (T7), `MN_BT1_SKIP_REASON` hiển thị trên UI.
- Tuần ≥ 06/07: lock tuần MN tự tạo với method này; số chơi = **bạch thủ official** (`final_bundles.bach_thu`); T7 = `verdict "NGHỈ"` + số None + vốn 0; vốn ngày thường = 1 số × số đài THẬT (lịch FIX-2) × 50đ×18k = **2.7M/ngày (3 đài)**.
- **Method guard daily-lock:** chỉ tái dùng số đã khóa trong ngày nếu `method_label` khớp — bug bắt được ở test scenario C (số cũ của method khác rò vào), đã fix.
- UI `/choi` (choi.html): hiện playStyle "BT 1 SỐ (official bạch-thủ)", số đài, và lý do NGHỈ T7.

**Test 3 kịch bản (DB copy, không đụng production):**
| Scenario | Kỳ vọng | Kết quả |
|---|---|---|
| A. Thứ Hai 06/07 | 1 số = official bạch-thủ, 3 đài, vốn 2.7M | PASS |
| B. Thứ Bảy 11/07 | NGHỈ + reason + vốn 0 | PASS |
| C. Chủ Nhật backdate có daily-lock method khác | KHÔNG tái dùng số method cũ | PASS (sau fix guard) |

**MT/MB giữ nguyên** — không đụng. Kết luận: KHÔNG kích hoạt fallback MN_HYBRID_V1.

### 1.5 E2 + E4a — đăng ký 2 model SHADOW_AUTO

| Model | Provider route | Slug | first_run | max_tokens | Giá blended (USD/1k) | Smoke |
|---|---|---|---|---|---|---|
| `qwen3.7-max` | OpenRouter (key riêng DB) | `qwen/qwen3.7-max` | 2026-07-06 | 32,768 | 0.0025 | OK — JSON parse, reasoning tokens > 0 |
| `glm-5.2` | OpenRouter (key riêng DB) | `z-ai/glm-5.2` | 2026-07-06 | 24,576 | 0.0015 | OK — JSON parse |

- Cả 2: `SHADOW_AUTO`, `shadow_only=1`, `output_eligible=0`, KHÔNG backfill, id tường minh, `display_name` chuẩn.
- glm-5.2 chạy **song song** glm-5.1 — xét retire 5.1 tại 14/07 khi 5.2 đủ dữ liệu (điều kiện owner).
- E4b: KHÔNG nâng version nào khác. E1: KHÔNG đăng ký thêm Kimi.

### 1.6 E3a/b/c — bật thinking effort high (shadow-only)

**Refactor:** `_MODELS_REASONING_LOW` (cũ) → 2 set mới `_MODELS_REASONING_HIGH` + `_MODELS_REASONING_EXCLUDE`; call OpenRouter gửi `reasoning={"effort":"high"}` cho nhóm HIGH.

| Model | Thay đổi | Ghi chú |
|---|---|---|
| `qwen3-max-thinking` | exclude → effort high + max_tokens 32,768 | giá cập nhật 0.00234 USD/1k |
| `grok-4.20-multi-agent` | exclude → effort high + **slug sửa `x-ai/grok-4.20` → `x-ai/grok-4.20-multi-agent`** | registry khai multi-agent nhưng slug cũ gọi bản thường — nay id/display/slug nhất quán |
| `gpt-5.5` | thêm effort high | shadow-only |
| `qwen3.7-max` (mới) | effort high từ đầu | theo config chuẩn E2 |

- **Mốc đo:** registry notes cả 3 model gắn `thinking_enabled_date=2026-07-05` — mọi bảng so găng sau này TÁCH trước/sau mốc, không trộn.
- **Cost guard:** nhóm effort-high dùng ngưỡng cảnh báo riêng **$0.15/call** (nhóm thường giữ $0.05) — tránh false positive khi reasoning tokens tăng.
- E3d: official `gpt-5.4`, `sonnet`, `opus` KHÔNG đổi config — xem lại 14/07.

### 1.7 Ma trận tương thích (1.3)

| Hạng mục | Kết quả |
|---|---|
| SHADOW_AUTO_EVAL_MODELS | 10 model đúng danh sách (8 cũ + qwen3.7-max + glm-5.2) — tự tính từ status, không hardcode |
| Scheduler route | openrouter (qwen/glm/grok/kimi/oss/gpt-5.5) · deepseek (reasoner, v4-pro-real) · đúng key per-model từ DB |
| RETIRED lọt pool? | KHÔNG — guard registry + `_registry_pool()` loại RETIRED |
| /choi MN mới rò /du-doan? | KHÔNG — money board là module riêng, không đụng final_bundles writer/model selector |
| Watch panel + money board + bảng MN BT 1 SỐ (V10777) | Tiếp tục cập nhật đủ 8 nguồn (API agg-signal không đổi schema) |
| Lineage | 0 đứt — 2 model mới là id mới tinh (không nối P&L); 3 model thinking giữ nguyên id + mốc thời gian tách giai đoạn |
| Chi phí token/ngày sau thay đổi | ~$5.1/ngày shadow (trace-based; +2 lane mới ~$0.3/ngày + reasoning high tăng output tokens có guard 0.15) |

---

## 2. PHẦN 2 — UI DISPLAY NAME: 1 NGUỒN SỰ THẬT

- **Registry:** 38 model có `display_name` chính thức; helpers `get_display_name(id)`, `get_display_name_map()`, `auto_display_name(id)` (Title Case + brand rules: DeepSeek/GPT/GLM/Grok/Qwen/Kimi/Gemma → vd `deepseek-v4-pro-real` → "DeepSeek V4 Pro Real").
- **API:** `GET /api/model-display-names` (public, cache 5 phút phía FE).
- **FE:** `web/frontend/model-names.js` — `ModelNames.get/decorated/autoCase/applyToSelects`; các trang đánh dấu `data-model-names` trên `<select>`, suffix qua `data-name-suffix`.
- **7 file bỏ hardcode:** index.html, user-view.html, accuracy.html, settings.html, viewer.html, app.js, user-view.js (+ combo_super.py backend lấy label từ registry).
- **Verify:** grep 0 hardcode map tên model còn sót trong UI; 5 trang render đúng qua smoke HTTP; label reasoner vẫn **"DeepSeek Reasoner (V4-Flash Thinking)"**; endpoint + model-names.js đều HTTP 200 trên VPS.

## 3. PHẦN 3 — CHÍNH SÁCH §52G GITHUB-FIRST (áp dụng từ V10781)

- Ghi vào **3 rule files sync** (`.Antigravityrules.md`, `.AGENT.md`, `.cursorrules`): báo cáo chi tiết đầy đủ = GitHub public-safe repo (bản gốc); Notion = 1 trang/version ≤30 dòng (kết quả chính + quyết định owner + link GitHub) + trang knowledge cho bài học/kiến trúc.
- Báo cáo V10781 này là báo cáo ĐẦU TIÊN theo chính sách mới.

## 4. PHẦN 4 — DỌN ROOT + VPS (KHÔNG XÓA GÌ)

**4.1 Quét an toàn trước khi di chuyển (2 lớp):**
- `_v10781_archive_scan.py`: quét import tĩnh mọi `_v107xx/_v108xx` → phân loại KEEP (imported) / ARCHIVE-CANDIDATE.
- `_v10781_archive_scan2.py`: quét reference động (string trong shell script, cron, systemd) → loại tiếp khỏi candidate nếu được gọi runtime.

**4.2 Đã di chuyển (manifest đầy đủ path cũ → mới + sha256 + lý do):**
- Local: **10 script one-off** đã chạy xong → `archive/2026/v10781_oneoff_scripts/` + `MANIFEST_v10781.json` (_v10705_output_total_station, _v10779_* ×6, _v10780_phase1_verify, _commit_v10776 ×2).
- VPS: **4 file `*.bak`** rời cây serve `web/backend/` → `/root/backups/v10781_bak_relocate/` + MANIFEST.txt sha256 (database.py.v15.bak, gpt_analyzer.py.v15.bak, mined_rule_eval.py.v15.bak, rule_engine.py.v18.bak).
- Smoke sau di chuyển: `/api/health` 200, các trang chính OK.

**4.4 VPS inventory:**
| Mục | Số liệu |
|---|---|
| Disk | 25G/39G (63%), còn 15G |
| Top thư mục | project 5.0G (venv 2.0G · backups nội bộ 1.7G · data 889M · artifacts 142M · web 119M), /www 2.5G |
| Log rotation | `logrotate.timer` ACTIVE (chạy 00:00 hằng đêm; nginx/rsyslog có config) |
| DB chính | lottery_ai.db 481M |

**ĐỀ-XUẤT-XÓA (chờ owner ký riêng — đợt này CHƯA xóa):**
1. `data/lottery_ai_BACKUP_pre_canon_views_20260530_100748.db` (316M — dup backup DB trong cây data, đã quá 5 tuần).
2. `/root/backups/lottery_ai_stale.db` (14M — bản 27/03/2026, đã có backup mới hơn nhiều lớp).
3. `web/backend/logs/*.log` cũ hơn 30 ngày (một phần của 43M) — hoặc đưa vào logrotate config riêng.
4. Local: các thư mục `_deploy_backup_f1safetynet_20260604`, `_cursor_backup_20260418`, `_headsync_preserve_20260605`, `_bk_235950_main_m3.py` (~4M tổng) — bản cứu hộ cũ đã có git history.

**4.5 Code hygiene (đề xuất đợt sau, KHÔNG sửa logic đợt này):** dead flags kiểu `_V10766_SKIP_MT_REPREDICT` sau khi hết hiệu lực; comment mồ côi tham chiếu version đã archive; map alias DeepSeek cũ (safety net) có thể gỡ sau 24/07 khi alias upstream chết hẳn.

## 5. PHẦN 5 — PROMPT CONTEXT V2 (SHADOW-ONLY, KHÔNG áp official)

**5.1 Thiết kế `_v10781_context_pack_v2.py`** — tự tổng hợp mỗi ngày per miền × thứ từ DB:
- **(i) V2-HEADER:** miền/thứ/ngày + đài hiện hành theo lịch 84 ngày (sau FIX-2).
- **(ii) V2-MILESTONE:** đúng doctrine miền — MN(16:35 xổ đầu ngày): nguồn D-1 duy nhất; MT: D-1 + MN(D) cùng ngày; MB(18:15 cuối ngày): D-1 + MN(D) + MT(D) mốc-điều-kiện V10770.
- **(iii) V2-STATS:** 12 tuần same-weekday anchor ≤ D-1 — đuôi về nhiều/ít (số kỳ có mặt), gan dài nhất đang chạy, tỉ lệ lặp D-1→D, chẵn/lẻ + cao/thấp đặc biệt.
- **(iv) V2-RULES:** rules từ `mined_rules_mn/mt_daily` snapshot mới nhất ≤ D (lifecycle MANH/TANG_TRUONG, top-5 theo rank) — trình bày dạng **dữ kiện trung tính** (nguồn đài/offset/giải/HR12W/n), không khuyến nghị.
- **(v) V2-DAY-TRAITS:** đầu/giữa/cuối tháng, tuần thứ mấy trong tháng, ISO week, lễ VN.
- **Ràng buộc cứng đã tôn trọng:** V10768 — ZERO WR/BT ranking model trong pack; mọi thống kê anchor ≤ D-1 (zero leak tương lai); footer pack tự khai ràng buộc.

**5.2 Lane A/B `_v10781_prompt_v2_lane.py` — thiết kế 1-biến sạch:**
- TREATMENT = 1 call `deepseek-reasoner` với prompt = **BODY V1 y hệt official** (create_analysis_prompt + rules + learned_intelligence như scheduler) + **PACK V2** + REASONING_RULEBOOK.
- CONTROL = pick official cùng model cùng ngày từ `predictions` (KHÔNG gọi API thêm) → biến duy nhất khác nhau là context pack v1 ↔ v2.
- Ghi `du_doan_test_runs` + `du_doan_test_bundles`, EXP `PROMPT_V2_AB_V1`, đủ cờ shadow (`test_only=1, admin_only=1, official_output='false', output_impact='false', owner_approved=0, output_eligible=0, diagnostic_only=0`).
- Guards: control-official-tồn-tại; causal chưa-xổ; hash-guard official quanh khối INSERT; re-run cùng ngày chỉ replace khi CHƯA settle.

**Run thật đầu tiên (VPS, 05/07):** `run_id 6815` — treatment BT **73** vs control BT **85** (bt_changed=true), 25,450 tokens, 57.6s, `official_tables_touched=0`.

**Cron VPS (3 dòng mới):** MN 05:10 (sau official 04:22, trước xổ 16:35) · MT 16:56 · MB 17:58 — log `logs/v10781_pv2_lane.log`.

**5.3 Chi phí (đo từ 43 call thật deepseek-reasoner 28/06→05/07):** avg 31,964 tokens/call × $0.0014/1k = **$0.0447/call → $0.134/ngày 3 miền (~$4/tháng)** — dưới ngân sách shadow hiện tại, không cần trình thêm. Đo 7–14 ngày, trình kết quả A/B tại checkpoint **14/07**.

## 6. PHẦN 6 — VERIFY + KẾ HOẠCH BÁO CÁO BỔ SUNG

- **6.1:** hash POST=PRE 4/4 IDENTICAL (bảng §1.1); smoke `/api/health` 200 + `/du-doan` + `/choi` + `/monitoring` + `/api/model-display-names` 200; registry text-proof TRƯỚC/SAU trong backup pre; diff prompt 3 miền `artifacts/v10781_prompt_audit/`.
- **6.2 evidence E5:** logic lock tuần 06/07 tự tạo ở `compute_board()` đầu tiên sau 00:00 với method `MN_BT1_OFFICIAL_V1` (test PASS 3 scenario; verify live sáng 06/07).
- **6.3 NGÀY MAI 06/07 báo cáo bổ sung:** first-run rows qwen3.7-max + glm-5.2; reasoning tokens > 0 của 3 model thinking trong run thật; /choi MN ngày đầu đúng lock; prompt MN đúng đài thứ Hai (TP.HCM, Đồng Tháp, Cà Mau).
- **6.4 checkpoint 14/07 (FU-V10781-GD2-EXECUTION):** MB RF@COND · MT wplur_rf2_ml · MN ai_plurality2 · MN BT nguồn số · lane 2 model mới · 3 model thinking tách trước/sau mốc · kimi-k2.5 form 14d + **thiết kế late-fill shadow row (plan-only)** · gemma-4-31b · gate nhà Google (official −77.1M/−90.5M) · glm-5.1 vs 5.2 · prompt v2 vs v1 · duyệt đề-xuất-xóa · 229 rows annotation.

## 7. THIẾT KẾ LATE-FILL SHADOW ROW (E1 — plan-only, trình 14/07, CHƯA deploy)

**Vấn đề:** kimi-k2.5 call thành công nhưng latency > soft-continue 90s → scheduler bỏ ghi row → mất dữ liệu so găng dù đã trả tiền call.

**Thiết kế đề xuất:**
1. Scheduler khi soft-continue vẫn GIỮ future/thread đang chạy, đăng ký callback thay vì hủy.
2. Callback khi call về: nếu (a) row model đó chưa tồn tại cho (date, region), (b) chưa tới closeout (MN 16:20 / MT 17:20 / MB 18:00), (c) kết quả parse hợp lệ → INSERT row `predictions` với flag `late_fill=1` trong `run_source` (vd `auto_daily_latefill`).
3. Sau closeout: hủy callback — call về muộn chỉ ghi trace, không ghi row (giữ causal).
4. Bảng so găng đánh dấu row late-fill riêng để owner biết row nào từng trễ.
5. KHÔNG áp cho official 15/15 — chỉ shadow lanes.

**Rủi ro cần owner cân nhắc:** row late-fill sinh sau thời điểm các model khác đã chốt (không đồng thời điểm nhưng vẫn causal vì trước giờ xổ); cần index unique (date, region, model) tránh double-insert.

## 8. FILE THAY ĐỔI + ARTIFACTS

**Runtime (VPS đã deploy):** `web/backend/gpt_analyzer.py` (E6b/E6a/E2/E3/E4a) · `main.py` (E6b + API display-names + route model-names.js) · `scheduler.py` (FIX-1) · `model_registry.py` (display_name + 2 model mới + thinking dates) · `combo_super.py` (label từ registry) · `_v10759_money_board.py` (E5) · `_provider_pricing_table.py` (giá 3 model) · FE: choi/index/user-view/accuracy/settings/viewer html + app.js + user-view.js + **model-names.js (mới)**.

**Shadow/ops (không ảnh hưởng official):** `_v10781_context_pack_v2.py` · `_v10781_prompt_v2_lane.py` · `_v10781_station_calendar.py` · `_v10781_deploy.py` · `_v10781_deploy_p5.py` · `_v10781_archive_scan.py/scan2.py/move.py` · `_v10781_vps_bak_move.py`.

**Artifacts:** `artifacts/v10781_prompt_audit/prompt_{MN,MT,MB}_2026-07-0{5,6}.txt` (PRE/POST) · `backups/v10781_pre/` (15 file) · `archive/2026/v10781_oneoff_scripts/MANIFEST_v10781.json` · VPS `/root/backups/v10781_bak_relocate/MANIFEST.txt`.

**Cron mới (VPS):** 3 dòng `_v10781_prompt_v2_lane` (05:10/16:56/17:58).

## 9. NGOÀI PHẠM VI (không làm đợt này)

- Không sửa 229 rows 2020–21 trong `lottery_results` (chỉ annotation + FU giám sát).
- Không xóa bất kỳ file nào (chỉ archive/relocate + đề-xuất-xóa).
- Không đổi config official gpt-5.4/sonnet/opus (E3d).
- Không đăng ký Kimi mới (E1); không nâng version model khác (E4b).
- Không sửa dead code/flag (chỉ liệt kê 4.5).
