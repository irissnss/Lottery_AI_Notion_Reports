# h2-knowledge · tang=PARTIAL

## TOM TAT

Đã đọc toàn văn 18 thư mục báo cáo công khai (V11014→V11164), kho tài liệu riêng, mã runtime đang serve trên VPS và audit các lane thí nghiệm cũ; kết quả là ma trận 35 dòng đủ mười cột. Câu trả lời thẳng cho owner: AGENT_IDE_KNOWLEDGE_COVERAGE = PARTIAL — cấm nói "đã nắm", vì năm nguồn chưa đóng được (Notion không đọc theo §57.1; lớp create_analysis_prompt chưa dump được vì luật cứng cấm gọi hàm khi chưa chứng minh không có đường ghi; 9 cổng Wave 1 không có trên VPS nên không chạy lại được; FU-419 chưa xác minh; không tìm được bản ghi đóng A1 của V11024). Phát hiện nặng nhất là hai phép đo ĐÃ ĐĂNG KÝ NGƯỠNG TRƯỚC đã đủ mẫu mà chưa báo cáo nào đọc verdict: lane prompt ba tầng T-B đạt 101/96 cặp bất đồng, McNemar z = −0,10 p = 1,00, T-B 33,24% vs CONTROL 33,53%, VIF đo lại cho chính thước này là 0,867, KTC95 [−5,49; +4,90]pp — tức prompt thuần ngữ cảnh ĐỔI SỐ CHỌN ở 70,2% số lượt nhưng KHÔNG đổi tỉ lệ trúng; và phép đo bầy đàn đạt 0,5763 so nền 0,4739 (+0,1024), vượt ngưỡng V11017. Bốn phép kiểm tính hợp lệ của lane T-B đều đạt: 0/346 dòng chạy sau khi kết quả về (biên nhỏ nhất 5,2 phút), CONTROL khớp official 346/346, tự chấm lại từ lottery_results khớp 346/346. Đọc mã đang serve tìm ra năm chỗ vẫn vi phạm đúng định nghĩa PURE CONTEXT của owner, trong đó nặng nhất là gpt_analyzer.py:2418-2424 vẫn bơm rổ TOP-5 đã xếp hạng kèm GAN CAO và HOT mà KHÔNG nằm sau cờ _ctx_only — tức V11001 "đã gỡ hết gan/nóng/lạnh" sai một phần sau 28 ngày. Ba mục CHỜ_OWNER đã quá ba tuần vẫn nguyên: MINED_RULES_MODE='soft' cộng +0,15 cho bộ luật 0/105 qua cổng, 6 đặc trưng gan/hot/cold trong ML, và _apply_hot_cold_post_filter dìm số gan ×0,3 dù cửa sổ đóng băng QD-041 đã hết hạn 21/08. Một đính chính có lợi: A1 của V11024 (bộ đếm đo tiến bị xoá mỗi thứ Hai) thực tế ĐÃ được sửa — dòng DELETE đã bị chú thích và bảng giữ 251 ngày — nhưng không tìm được bản nào ghi nhận. Phiên này 0 ghi production, 0 deploy, 0 restart, 0 commit, 0 gọi provider; mọi truy vấn chạy trên clone bất biến.

## TRA LOI

## AGENT_IDE_KNOWLEDGE_COVERAGE = **PARTIAL**

**Cấm ghi «đã nắm».** Đã đối chiếu được phần lớn di sản prompt, nhưng **năm nguồn chưa đóng được**, và cả năm đều đủ nặng để đổi kết luận nếu mở ra:

| # | nguồn KHÔNG đọc / KHÔNG đối chiếu được | vì sao |
|---|---|---|
| 1 | **Notion** — KNOWLEDGE LOCK bản gốc, 14 hub | `§57.1` cấm ghi và `V10962` ghi rõ Notion **đứng im từ 01/08/2026**. Phiên này **không đọc**. Mọi tri thức chỉ tồn tại trên Notion (ngữ pháp luật, whitelist giải, doctrine cửa sổ ở bản gốc) là **nguồn chưa đối chiếu** — V11054 §4quinquies dựng T3 từ chính bản Notion đó |
| 2 | **Lớp `create_analysis_prompt`** (≈17.100–18.200 ký tự, gấp rưỡi gói ngữ cảnh) | luật cứng của phiên cấm gọi `create_analysis_prompt` / `build_context_pack` / `build_system_prompt` trước khi **chứng minh không có đường ghi DB/tệp/mạng**. Chưa chứng minh được ⇒ **không gọi**, chỉ đọc mã. Số ký tự **từng khối** của lớp này vẫn là **suy ra**, không phải **đo** |
| 3 | **9 cổng Wave 1** (`_v11150_unified_candidate_contract` · `_v11150_contamination_gate` · `_v11150_test_contract` · `_v11150_e2e_contract` · `_v11150_ml_pure_math_audit` · `_v11152_test_lane` · `_v11152_neo_final` · `_v11155_counterfactual` · `_v11156_ranked_adapter`) | **KHÔNG CÓ trên VPS** (đủ trong repo local) ⇒ **không chạy lại được** để xác nhận `37/37` · `17/17` · `E2E_PASS` · `11/11` trên mã đang serve |
| 4 | **FU-419** — dòng `D-1 cross-region tail pool` và dòng chị em `tails already spent` | phải dump prompt từ hàm đang serve mới biết ⇒ vướng đúng mục 2 ⇒ `INDETERMINATE` |
| 5 | **Bản ghi đóng `A1` của V11024** | mã **và** dữ liệu đều chứng minh A1 đã được sửa, nhưng không tìm được commit/báo cáo nào ghi nhận ⇒ tài liệu vẫn treo một blocker đã chết |

**Đã đọc và đối chiếu được:** 18 thư mục báo cáo công khai đọc **toàn văn** (V11014 · V11015 · V11016 · V11017 · V11024 + R5/R7/R8/R9/R10 · V11054 · V11055 · V11059 · V11101 · V11105 · V11144 · V11150 · V11152 · V11155 · V11157 · V11159 · V11160 · V11164 + PHAN_BIEN_32) · kho riêng (`CLAUDE.md` · `BAN_DO_NGU_CANH_PROMPT_20260821` · `SO_SAU_LAN_DOI_PROMPT` · `ai_context_shadow_contract` · `SO_RUT_LAI.json` 13 mục · `AUTOMATION_STATE` seq 480) · mã runtime đang serve (10/10 tệp hash khớp GATE 0) · 254 bảng DB trên clone bất biến · crontab 93 dòng · `monitoring.html`.

**Về câu hỏi cốt lõi «prompt thuần ngữ cảnh có tốt hơn không»:** đã có **câu trả lời bằng đo tiến, ghép cặp, ngưỡng đăng ký trước** — và câu trả lời là **KHÔNG KHÁC BIỆT** (z = −0,10, p = 1,00, KTC95 [−5,49; +4,90]pp). Nhưng phải đọc kèm hai điều: ① prompt ba tầng **đổi hẳn số được chọn ở 70,2 % số lượt** mà tỉ lệ trúng đứng yên — nhất quán với `loi_the(k)` phẳng của V11054 và với V11116/V11164 «không model nào vượt nền»; ② **bản T-B đang đo cũng CHƯA sạch** — nó dựng từ chính bốn khối production, mà năm chỗ nêu ở mục phát hiện (`:2418-2424` · `:3191` · `§8:565` · MB `:5591`/`:5689` · Phase 15 `:2472-2526`) **vẫn có mặt trong cả hai nhánh**. Nghĩa là phép đo vừa rồi so «prompt production» với «prompt production đã xếp lại ba tầng + gỡ ba mâu thuẫn», **không phải** so với PURE CONTEXT theo đúng định nghĩa owner. Chưa ai từng đo một prompt thoả đủ chín điều kiện owner đặt ra.

## PHAT HIEN
  - [NO_ANOMALY_FOUND] Lane T-B (prompt ba tầng thuần ngữ cảnh) ĐỦ MẪU và ĐỌC ĐƯỢC: đổi 70,2% số chọn nhưng KHÔNG đổi tỉ lệ trúng
  - [PROVEN_DEFECT] Hai phép đo ĐÃ ĐĂNG KÝ NGƯỠNG TRƯỚC đã đạt mẫu nhưng KHÔNG báo cáo nào đọc verdict
  - [PROVEN_DEFECT] «Đã gỡ hết gan/nóng/lạnh khỏi prompt» SAI MỘT PHẦN sau 28 ngày — rổ TOP-5 + GAN CAO + HOT vẫn được bơm, và KHÔNG nằm sau cờ ngữ cảnh thuần
  - [PROVEN_DEFECT] gpt_analyzer.py:3191 ra lệnh bầy đàn trong CẢ HAI regime, ngược thẳng với SYSTEM_PROMPT:382
  - [PROVEN_DEFECT] Phase 15 bơm win-rate 7 ngày của chính model + lệnh «WR thấp thì đổi chiến lược» — không có cờ nào chặn
  - [PROVEN_DEFECT] `contam_hits = 0` KHÔNG chứng minh được prompt sạch — bộ 5 dấu ô nhiễm mù với ít nhất bốn chuỗi đang có thật
  - [PROVEN_DEFECT] MINED_RULES_MODE='soft' vẫn cộng +0,15 cho bộ luật mà tài liệu ghi 0/105 qua cổng — 26 ngày không ai động
  - [PROVEN_DEFECT] Hai câu MB bảo model SKIP, ngược thẳng SYSTEM_PROMPT «Không bao giờ bỏ trống số chính»
  - [OPERATIONAL_IMPROVEMENT] ĐÍNH CHÍNH có lợi: A1 của V11024 (bộ đếm đo tiến bị xoá mỗi thứ Hai) ĐÃ được sửa, nhưng không tìm được bản ghi nhận
  - [OPERATIONAL_IMPROVEMENT] Bộ cổng Grand Overhaul Wave 1 không có trên VPS và bảng unified_candidate_sets không tồn tại — nhãn CODED_AND_TESTED_NOT_RUNTIME_PROVEN là đúng, nhưng không cổng nào chạy lại được
  - [SUSPICIOUS_NEEDS_MORE_EVIDENCE] prompt_section_breakdown_daily ghi 46.160 dòng suốt 4,5 tháng nhưng chưa tìm được điểm ĐỌC nào
  - [EXPECTED_BEHAVIOR] PHASE_FIRST_JSON_CONTRACT là hằng số chết đúng như tài liệu ghi — không phải lỗi
  - [INDETERMINATE] FU-419 (dòng D-1 cross-region tail pool) và dòng chị em «tails already spent» — chưa xác minh được trong phiên này

## DAU VAO LAN SAU

**① HAI VERDICT ĐÃ ĐỦ MẪU, ĐỌC ĐƯỢC HỢP LỆ NGAY — không phải bẻ ngưỡng vì cả hai đăng ký trước:**
- Lane T-B: 101/96 cặp bất đồng · z = −0,10 · p = 1,00 · −0,29 pp · VIF 0,867 · KTC95 [−5,49; +4,90] pp · **70,2 % số lượt đổi số chọn**. MDE ±5 pp — khai kèm, không giấu.
- Bầy đàn: 0,5763 vs nền 0,4739 (+0,1024) ⇒ ĐẠT ngưỡng V11017, nhưng **đo GỘP nhiều biến**, không tách nhân quả.

**② DANH SÁCH THI HÀNH cho bất kỳ định nghĩa PURE CONTEXT nào — năm chỗ còn sống trên mã đang serve.** Không dọn năm chỗ này thì mọi phép đo prompt tiếp theo đều đo một thay đổi **làm nửa vời** (`§60.1`):
- `gpt_analyzer.py:2418-2424` → rổ TOP-5 + GAN CAO + HOT (`format_condensed_stats`), **không** sau `_ctx_only`
- `:3191` lệnh ưu tiên số nhiều nguồn — ngược `:382` (`z = −2,54`)
- `REASONING_RULEBOOK §8:565` `Width > Rules > Diversity` — đè `§23:764`
- MB `:5591` / `:5689` bảo SKIP — ngược `:307`
- Phase 15 `:2472-2526` bơm WR bảy ngày của chính model + «WR thấp thì đổi chiến lược»

**③ BA MỤC `CHỜ_OWNER` QUÁ BA TUẦN, cửa đã mở mà không ai bước qua:**
> ⚠️ **Cố ý trích MỘT cửa sổ** (`PRJ-SELECTION-WINDOW-001` · RM-18). Phiên này **không** tuyên bố
> hiệu quả của luật khai mỏ, nên cả bốn vế — **trong cửa sổ chọn · ngoài cửa sổ chọn · trong mẫu ·
> ngoài mẫu** — đều để trống có chủ ý. Bộ đủ nằm ở **RM-18/V11030** (**+7,5 / +13,8 / +20,7 điểm
> TRONG cửa sổ chọn, ĐÚNG BẰNG 0 ngoài cửa sổ**) và **V11073** (**+9,9% trong mẫu → −1,6% ngoài
> mẫu**). Đo bổ sung của phiên này: **n = 20/miền trên 4 ngày** ⇒ **RM-04, chưa được phép kết
> luận**; KTC95 đều chứa 0. Báo một vế là giấu mất nửa sự thật.
- `MINED_RULES_MODE='soft'` + `APPLY_TO='all'` (`main.py:124/128`) — 26 ngày, một dòng, có đường lui ngay
- 6 đặc trưng gan/hot/cold trong ML (`meta_predict.py:139-163`) — 28 ngày, FU-320
- `_apply_hot_cold_post_filter` ×0,3 (4 điểm gọi) — **QD-041 đã hết hạn 21/08**

**④ ĐIỀU KIỆN TIÊN QUYẾT KỸ THUẬT:** trước khi nâng bất kỳ verdict prompt nào, phải **chứng minh `build_context_pack` / `create_analysis_prompt` không có đường ghi**, rồi mới dump được lớp `create_analysis_prompt`. Chừng nào chưa dump, mọi con số về lớp đó là suy ra (`RM-14`).

**⑤ CẤM DÙNG `contam_hits = 0` làm bằng chứng** cho tới khi bộ dấu phủ được bốn chuỗi đang mù (`Win Rate` · `LỊCH SỬ DỰ ĐOÁN CỦA BẠN` · `WR hiện tại (TRỰC TIẾP)` · `Số đã trúng nhiều lần`) và phép băm chuyển xuống sau `:6762`.

**⑥ HAI ĐÍNH CHÍNH phải ghi tại chỗ gốc (`PRJ-RETRACTION-001`):** A1 của V11024 **đã được sửa** (dòng DELETE đã chú thích + 251 ngày dữ liệu) · V11001 «đã gỡ hết gan/nóng/lạnh» **sai một phần**.

**⑦ Nếu lần sau muốn đo PURE CONTEXT thật:** hạ tầng đã có sẵn và **rẻ** — lane T-B chứng minh thiết kế ghép cặp chạy được (CONTROL = lượt official, **0 đồng**; chỉ tốn một call cho nhánh thử), đủ mẫu trong **25 ngày**, và có endpoint + panel sống. Chỉ cần dựng nhánh mới sạch năm chỗ ở mục ② rồi cho chạy cùng cron.

## CHUA TRA LOI

1. **Nội dung lớp `create_analysis_prompt` từng khối** — chưa dump được vì luật cứng cấm gọi hàm khi chưa chứng minh không có đường ghi. Mọi con số về lớp này (kể cả «≈18.200 ký tự») là **suy ra bằng phép trừ**, không phải đo. `INDETERMINATE`.

2. **FU-419 đã lên production chưa** và dòng chị em `<miền>(D) tails already spent` còn hỏng không — vướng đúng mục 1. `INDETERMINATE`.

3. **PURE CONTEXT theo đúng chín điều kiện owner chưa từng được đo.** Lane T-B là thứ gần nhất, nhưng nó vẫn mang rổ TOP-5/GAN CAO/HOT (`:2418`), lệnh ưu tiên nhiều nguồn (`:3191`), `§8 Rules > Diversity`, WR bảy ngày của chính model (Phase 15). Chưa có phép đo nào cho một prompt sạch thật.

4. **Ảnh hưởng định lượng của `MINED_RULES_MODE='soft'` (+0,15)** lên bạch thủ — chưa đo. Không suy được từ «0/105 qua cổng».

5. **`prompt_section_breakdown_daily` có thật sự không ai đọc không** — phép quét theo tên chuỗi có thể bỏ sót truy cập qua biến; chính phiên này đã sập bẫy đó một lần với `bay_dan_daily_shadow`. Cần quét theo AST/biến trước khi gọi tên. `SUSPICIOUS_NEEDS_MORE_EVIDENCE`.

6. **Bản nào đóng A1 của V11024** — không tìm được trong 18 báo cáo đã đọc.

7. **Tại sao `gan_signal_shadow_v100` (246.000 dòng) chết đúng 09/05** — V11054 mục C2 hỏi, đến nay chưa ai trả lời.

8. **`neo558` tính lại trong phiên này ra `896465dee1aac3ac…`, KHÁC neo GATE 0 `a82c508d3569abda…`** — nguyên nhân là **công thức khác** (tôi chọn bộ cột khác khi băm), **KHÔNG phải drift dữ liệu**. Cấm đọc thành drift. Bằng chứng production không đổi là: đếm dòng 6 bảng khớp GATE 0 **từng con số** (predictions 14.201 · final_bundles 567 · lottery_results 15.416 · model_daily_eval 14.065 · scorecard 17.121 · reliability 5.276), hash 10/10 tệp mã khớp, PID 3370750 · NRestarts 0 · active. Muốn kiểm neo phải chạy **đúng script gốc**, không phải bản tôi viết lại.

9. **Tự sửa trong phiên (ghi công khai để không ai trích bản sai):** bản quét điểm đọc **đầu tiên** báo `prompt_3tang_ab_shadow_v11059` và `gan_hoi_tu_shadow_v1105