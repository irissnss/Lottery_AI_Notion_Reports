# CONVERSATION_CONTEXT V10780 — 2026-07-05

## Owner messages (verbatim, session 05/07 11:11–12:30 +07)

### 1. PROMPT TỔNG LỰC (11:11) — toàn văn

```
PROMPT TỔNG LỰC — VERIFY TOÀN HỆ + REASONING-FIRST POOL + CHUẨN HÓA PROMPT MIỀN/THỨ + GATE KÝ + THỰC THI
Kế thừa: V10778 Phase A + V10779 Phase B (đã deploy 05/07 04:07). Delivery = version kế tiếp còn trống.
Backup backups/<version>_pre/ trước mọi thay đổi. Timezone: Asia/Ho_Chi_Minh. Ngày: 05/07/2026.
LƯU Ý THỜI GIAN: còn ~6h tới live + hôm nay là hạn chốt /choi tuần 06/07 — chạy GIAI ĐOẠN 1 (verify)
trước, trình bảng ký, owner ký tới đâu thực thi tới đó.

CẤU TRÚC 2 GIAI ĐOẠN:
- GIAI ĐOẠN 1 (PHẦN A-D): CHỈ kiểm chứng + test + báo cáo. CẤM sửa runtime.
- GIAI ĐOẠN 2 (PHẦN E-F): CHỈ thực thi các dòng owner đã ký OK trong bảng xác nhận.

NGUYÊN TẮC BẤT BIẾN:
- /du-doan official không đổi hành vi nếu chưa có dòng ký tương ứng. 4 bảng official chỉ đọc,
  hash-guard PRE=POST. Model mới: SHADOW_AUTO, shadow_only=1, output_eligible=0, không backfill,
  first_run_date rõ. Retire theo cơ chế RETIRED+reason+date. Không nối P&L id cũ-mới.
- Không xác minh được thông số → ghi "KHÔNG XÁC MINH ĐƯỢC" + lý do, cấm đoán.
- Tôn trọng lock V10768 (de-herding): KHÔNG đưa WR/BT ranking trở lại context pack.

================ PHẦN A — RE-VERIFY ĐỘC LẬP V10779 (bằng chứng mới trên VPS production) ================
A1. Namefix: grep "DeepSeek R1" = 0 gán cho reasoner; mở 5 trang UI chụp label thật.
A2. PL-1: xác nhận 0 call runtime còn dùng alias deepseek-reasoner/deepseek-chat; 1 call id tường minh
    so fingerprint fp_8b330d02d0; call log hôm nay của official đi route mới.
A3. Dump MODEL_REGISTRY thật: bảng id | provider | api_route | status | thinking | max_tokens |
    shadow_only | output_eligible | first_run_date | retire_reason. Đếm SHADOW_AUTO=8, output=15,
    6 RETIRED đủ reason.
A4. deepseek-v4-pro-real: có trong lịch hôm nay; first-run row nếu đã chạy (row + usage + parser OK).
A5. Hash + row count 4 bảng official — chụp mốc PRE cho các thay đổi tối nay.
A6. SELECT DISTINCT ai_model 30 ngày predictions/model_daily_eval — khớp 100% registry.
A7. CP-66.9 CLOSED; pool MN 06/07 fallback = MN_HYBRID_V1; V66/V67 nguyên cho MT/MB.

================ PHẦN B — AUDIT REASONING-FIRST POOL + THINKING/MAXTOKEN/VERSION ================
Định hướng owner: các lane shadow (không tham gia total output) phải ƯU TIÊN model có cấu trúc
suy luận tự kiểm chứng như "DeepSeek Reasoner (V4-Flash Thinking)".
B1. Bảng TỪNG model sống (official + 8 shadow + ứng viên mới): model | provider | version đang gọi |
    version CAO NHẤT của nhà đó | KIẾN TRÚC (reasoning/thinking thuần? hybrid? non-thinking?) |
    thinking đang BẬT/TẮT + param | max output tokens set/tối đa | P&L 56d | đề xuất:
    GIỮ / BẬT THINKING / TĂNG MAXTOKEN / NÂNG VERSION / ĐỀ XUẤT THAY (nếu non-thinking không lý do giữ).
B2. Test thật 1 call/model: reasoning tokens > 0 với model khai thinking; ghi model nào thinking TẮT
    hoặc set sai. Lưu ý gemma-4-31b (free, non-thinking +9.1M): nêu rõ trade-off giữ (free) vs thay.
B3. Quét version mới từng nhà (OpenAI, xAI, Google, Qwen, Moonshot, DeepSeek): bản cao hơn + có
    thinking + max token + giá. CHỈ đề xuất — nâng version = id mới + lịch sử mới (ghi rõ rủi ro).

================ PHẦN C — OPENROUTER CONFIG CHUẨN + TEST KIMI/QWEN ================
C1. Config chuẩn DUY NHẤT: tham số hợp nhất reasoning{} (effort hoặc max_tokens theo kiểu từng nhà).
    CẤM include_reasoning (deprecated), CẤM hậu tố :thinking. Key từ env/secrets, không hardcode.
C2. Chống bẫy token: reasoning tính vào completion tokens → max_tokens tổng ≥ 2x budget reasoning;
    test không dính finish_reason=length.
C3. Parser xử lý CẢ reasoning (OpenRouter) và reasoning_content (DeepSeek native); test đúng tổ hợp
    production (streaming/json) — có model âm thầm drop reasoning theo tổ hợp.
C4. TEST ĐỐI ĐẦU KIMI (3 call/model, config chuẩn): kimi-k2-thinking (chuyên thinking, 11/2025,
    ~$0.60/$2.50) vs kimi-k2.5 (thế hệ mới hơn, có reasoning, $0.40/$1.90, bật thinking qua reasoning{}):
    reasoning tokens thật? độ sâu suy luận? parser OK? chi phí thật/call? → khuyến nghị 1 con theo
    tiêu chí owner (thế hệ cao nhất + thinking THẬT + max token).
C5. QWEN: xác minh thật qwen3.7-max vs qwen3.7-plus (thinking? max token? benchmark reasoning? giá?)
    → khuyến nghị 1 bản. Ghi chú: hệ đang giữ qwen3-max-thinking (+7.1M) — nêu rõ model mới bổ sung
    hay ứng viên thay thế tương lai.

================ PHẦN D — AUDIT PROMPT DỰ ĐOÁN: NHẬN DIỆN MIỀN/THỨ (chống lẫn miền) ================
D1. Trích prompt production thật đang gửi model AI cho TỪNG miền (MN/MT/MB) — đính kèm nguyên văn
    (che phần nhạy cảm nếu có).
D2. Chấm điểm từng prompt theo checklist: có ghi rõ (i) MIỀN đang dự đoán? (ii) THỨ trong tuần +
    ngày dương lịch? (iii) danh sách ĐÀI quay hôm đó + số đài? (iv) dữ liệu lịch sử trong context
    có gắn nhãn miền rõ ràng không (nguy cơ trộn kết quả miền khác)? (v) yêu cầu format output có
    ràng buộc miền không?
D3. Quét code assemble context pack: xác nhận dữ liệu miền nào chỉ đút vào prompt miền đó; liệt kê
    mọi chỗ dữ liệu cross-region đi vào prompt (nếu có) + lý do tồn tại (V10766 đã bỏ re-predict
    MN→MT — xác nhận không còn đường rò khác).
D4. Đề xuất CONTEXT HEADER chuẩn (nếu D2/D3 có lỗ hổng): khối đầu prompt thống nhất
    [MIỀN | THỨ | NGÀY | ĐÀI | SỐ ĐÀI | phạm vi dữ liệu lịch sử = chỉ miền này] — thiết kế cụ thể,
    KHÔNG deploy; tôn trọng V10768 (không thêm WR/BT ranking). Phân loại đề xuất: SỬA CLARITY
    (rủi ro thấp, có thể áp official nếu owner ký) vs SỬA LOGIC (phải shadow test trước).

================ PHẦN E — BẢNG XÁC NHẬN OWNER (kết quả GIAI ĐOẠN 1) — DỪNG CHỜ KÝ ================
Mỗi dòng 1 quyết định, đủ số liệu để ký:
E1. Đăng ký Kimi: con nào (K2 Thinking / K2.5 theo C4)? OK/KHÔNG
E2. Đăng ký Qwen: bản nào (theo C5)? OK/KHÔNG
E3. Model đang sống cần BẬT thinking / TĂNG maxtoken (từng con, theo B1-B2)? OK/KHÔNG từng con
E4. Model đề xuất NÂNG VERSION hoặc THAY vì non-thinking (theo B1/B3, kèm rủi ro lịch sử mới)?
    OK/KHÔNG từng con
E5. /choi MN tuần 06/07: BT 1-SỐ nguồn official bạch-thủ + NGHỈ T7 (V10777: +7.6M BỀN bỏ-T7,
    forward 14d +6.8M) hay giữ fallback MN_HYBRID_V1? — KÈM GIỜ KHÓA TUẦN để owner quyết kịp.
E6. Context header miền/thứ (theo D4): áp bản SỬA CLARITY cho official? OK/KHÔNG;
    phần SỬA LOGIC (nếu có) → shadow test? OK/KHÔNG.
DỪNG TẠI ĐÂY CHỜ OWNER KÝ TỪNG DÒNG.

================ PHẦN F — THỰC THI THEO DÒNG ĐÃ KÝ + VERIFY TỔNG LỰC ================
F1. Backup + hash PRE (mốc A5). Thực thi đúng các dòng ký OK, đúng quy trình:
    đăng ký model (smoke → registry → pricing giá thật → scheduler), /choi MN lock, prompt header.
F2. MA TRẬN TƯƠNG THÍCH sau mọi thay đổi (cấm sót): SHADOW_AUTO_EVAL_MODELS đúng danh sách;
    scheduler route đúng (openrouter/deepseek); aggregation-signal + mn_bt + plurality/top1-strength/
    combo-super + MN cap + trọng số TOTAL OUTPUT: model mới chỉ vào pool khi đủ dữ liệu tối thiểu,
    model RETIRED không lọt forward; /choi MN mới không rò sang /du-doan; UI monitoring + choi + đã nghỉ
    đúng; token audit chi phí/ngày; lineage 0 đứt.
F3. VERIFY: hash POST=PRE IDENTICAL (lệch tự nhiên giải trình từng row); smoke /api/health,
    /du-doan, /choi, /monitoring 200 + render đúng; registry text-proof TRƯỚC/SAU; money board lock
    06/07 evidence; nếu sửa prompt: diff prompt TRƯỚC/SAU + 1 call test/miền xác nhận model nhận
    diện đúng miền/thứ trong output.
F4. NGÀY MAI (06/07): báo cáo bổ sung first-run proof mọi lane mới + /choi MN ngày đầu đúng lock
    + prompt mới (nếu áp) chạy đúng 3 miền không lẫn.
F5. DOCS: CHANGELOG; SSOT + HOME sync; FU-<version> (checkpoint 14/07 đủ hạng mục: MB RF@COND,
    MT wplur_rf2_ml, MN ai_plurality2, MN BT nguồn số, đánh giá sơ bộ lane model mới); AUTOMATION_STATE;
    trace pack; Notion report chi tiết: yêu cầu owner → việc làm → bằng chứng → trạng thái từng mục
    (PASS/FAIL/BLOCKED/CHỜ) → mục chờ owner.

BLOCKING RULES:
- GIAI ĐOẠN 1 zero thay đổi runtime. Lệch thực tế vs V10779 → CRITICAL đầu báo cáo + bằng chứng 2 phía.
- Dòng nào owner chưa ký → tuyệt đối không thực thi.
- Smoke/test model fail → không đăng ký con đó, phần khác chạy tiếp, báo rõ.
- /choi MN logic NGHỈ T7 không kịp test đầy đủ trước giờ khóa → giữ fallback MN_HYBRID_V1 tuần này,
  báo owner, không khóa ẩu.
- Lệch hash official không giải trình được → rollback + restart + báo ngay.
- Ngoài phạm vi → không làm, ghi mục "ngoài phạm vi".
```

### 2. (12:01) — nhắc hoàn thành

```
cái gì vậy chưa xong mà em tiếp đi em
```

### 3. (12:13) — yêu cầu tổng hợp lên GitHub + Notion MCP

```
Em không tổng hợp đầy đủ chi tiết lên github và Notion MCP ah em? làm điể tool Ai của anh hỗ trợ phân tích thêm
```

## Agent actions this session (GIAI ĐOẠN 1 — verify only)

- Viết 2 script audit read-only (KHÔNG deploy, không đụng runtime): `web/backend/_v10780_phase1_verify.py` (25 block: a1/a2log/a3reg/a4pro/a5hash/a6distinct/a7cp/ui/b2a/b2b/c3/c4/c5/station/pnl/pnl2/btpnl/multiwin/perregion/qwenmeta/aliasgrep/misc×4) chạy trên VPS qua SSH; `_v10780_prompt_audit.py` dựng prompt production 3 miền từ đúng code path + DB thật trên VPS.
- PHẦN A: 7/7 PASS (A6 có 1 ngoại lệ claude-opus-4-20250514 giải trình được — id cũ V10729, tự thoát cửa sổ 17/07).
- PHẦN B: đo thật thinking từng model (1 call/model, key production từ app_settings DB base64): phát hiện grok-4.20 + qwen3-max-thinking gửi `reasoning {"exclude": true}` → 0 reasoning tokens; gpt-5.4 official không set effort (0 toks) nhưng +27.1M.
- P&L per-region: giải trình được +7.1M qwen3-max-thinking = P&L 56d riêng miền MN (MT +2.9M, MB −69.6M, tổng −59.6M).
- PHẦN C: config chuẩn OpenRouter thiết kế xong; C2 PASS (finish_reason=stop toàn bộ); C3 parser PASS 6/6; C4 Kimi head-to-head (k2.5 reasoning sâu hơn 2,446 vs 1,457 toks, k2-thinking nhanh hơn 5–17s vs 31–85s); C5 khuyến nghị qwen3.7-max (3,381 reasoning toks).
- PHẦN D: dựng prompt nguyên văn 3 miền; phát hiện lỗi factual đài MN (5 đài thay vì 3 — nhiễm 229 rows 2020–21 region='MN' gán nhầm 14 đài MT); D3 không có đường rò cross-region không nhãn; D4 thiết kế FIX-1/2/3.
- kimi-k2.5 mất row hôm nay: call OK nhưng 470.7s > soft-continue 90s → scheduler bỏ ghi.
- PHẦN E: trình bảng ký 11 dòng (E1→E6b) + giờ khóa tuần /choi (trước 00:00 06/07, đề nghị ký trước 22:00). DỪNG chờ ký — PHẦN F chưa thực thi.
- Hash 4 bảng official: chỉ đọc, chụp PRE 11:23:58; zero runtime change toàn phiên.
- Tổng hợp report này lên GitHub public + Notion MCP (trang con dưới Lottery_AI_Test) theo §52F.
