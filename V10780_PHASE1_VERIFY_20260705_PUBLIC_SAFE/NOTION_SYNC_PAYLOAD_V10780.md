# V10780 — GIAI ĐOẠN 1 VERIFY TOÀN HỆ: RE-VERIFY V10779 + REASONING-FIRST POOL + OPENROUTER CHUẨN + AUDIT PROMPT MIỀN/THỨ (DỪNG CHỜ OWNER KÝ PHẦN E)

- Ngày: 2026-07-05 (11:11–12:30 VN)
- Loại: **GIAI ĐOẠN 1 — VERIFY ONLY, ZERO THAY ĐỔI RUNTIME** (GIAI ĐOẠN 2 = PHẦN F chỉ chạy sau khi owner ký PHẦN E)
- Kế thừa: V10778 Phase A + V10779 Phase B (deploy 05/07 04:07)
- Evidence scripts (read-only, CHƯA deploy): `web/backend/_v10780_phase1_verify.py` (25 block chạy trên VPS qua SSH), `web/backend/_v10780_prompt_audit.py` (dựng prompt production từ đúng code path + DB thật trên VPS)
- Evidence pack local: `artifacts/v10780_prompt_audit/` (3 prompt nguyên văn MN/MT/MB + báo cáo)
- Hash 4 bảng official chụp 11:23:58 (mốc PRE cho GIAI ĐOẠN 2): predictions 9,304 `5e92c59e…` · final_bundles 382 `1bef9c34…` · lottery_results 15,010 `2076e8f7…` · model_daily_eval 9,132 `cbd1f568…` — **không ghi gì vào 4 bảng trong suốt phiên**

## 0. YÊU CẦU OWNER (tóm tắt prompt tổng lực)

Cấu trúc 2 giai đoạn: GĐ1 (PHẦN A–D) chỉ kiểm chứng + test + báo cáo, CẤM sửa runtime; GĐ2 (PHẦN E–F) chỉ thực thi dòng đã ký. Nguyên tắc bất biến: /du-doan không đổi hành vi khi chưa ký; 4 bảng official chỉ đọc hash-guard PRE=POST; model mới SHADOW_AUTO shadow_only=1 output_eligible=0 không backfill; retire theo RETIRED+reason+date; không nối P&L id cũ–mới; không xác minh được → ghi "KHÔNG XÁC MINH ĐƯỢC"; tôn trọng lock V10768 de-herding (không đưa WR/BT ranking vào context pack). Toàn văn prompt lưu ở CONVERSATION_CONTEXT cùng thư mục.

## 1. NĂM PHÁT HIỆN QUAN TRỌNG

1. **Prompt MN ghi SAI danh sách đài** — header production hôm nay ghi `ĐÀI XỔ HÔM NAY (MN): Khánh Hòa, Kiên Giang, Kon Tum, Tiền Giang, Đà Lạt` (5 đài) trong khi MN Chủ Nhật thật = **Tiền Giang, Kiên Giang, Đà Lạt (3 đài)**. Nguyên nhân: 229 rows `lottery_results` năm 2020–2021 bị gán nhầm region='MN' cho 14 đài MT (Khánh Hòa 27 rows, Kon Tum 14 rows… max date 2021-10-21), và query lấy đài quét DISTINCT toàn lịch sử. Trace production hôm nay xác nhận label 5 đài này đi vào prompt thật. KHÔNG phải lỗi V10779 (tồn tại từ lâu). Fix đề xuất ở mục 5 (D4).
2. **2 model thinking bị TẮT ngầm trong production**: `grok-4.20-multi-agent` và `qwen3-max-thinking` đang gửi `reasoning: {"exclude": true}` → đo thật **0 reasoning tokens**. Grok còn gọi slug `x-ai/grok-4.20` (bản thường, không phải multi-agent).
3. **Số +7.1M của qwen3-max-thinking: ĐÃ TÁI LẬP ĐƯỢC (per-region)** — +7.1M là P&L 56d RIÊNG MIỀN MN. Tính per-region bằng công thức chuẩn hệ: **MN +7.1M · MT +2.9M · MB −69.6M → TỔNG 3 miền −59.6M**. Kết luận: qwen3-max-thinking dương nhẹ MN/MT, bị MB kéo âm nặng. (Lúc báo cáo 12:01 chưa tách miền nên ghi "KHÔNG XÁC MINH ĐƯỢC"; block `perregion` chạy 12:15 đã giải trình xong.)
4. **kimi-k2.5 hôm nay mất row**: call thành công (trace 04:29:16, JSON OK) nhưng latency **470.7s** vượt soft-continue 90s của scheduler → không có row predictions hôm nay (7/8 shadow có row). Rủi ro latency vốn có của k2.5 — liên quan trực tiếp quyết định E1.
5. **A6 lệch 1 id, giải trình được**: `claude-opus-4-20250514` còn trong cửa sổ 30d (rows cuối 16/06 — ngày đổi id V10729 sang `claude-opus-4-6`, lineage có ghi). Tự thoát cửa sổ từ 17/07. Không phải vi phạm.

## 2. PHẦN A — RE-VERIFY V10779 TRÊN VPS: 7/7 PASS

| Mục | Kết quả | Bằng chứng |
|---|---|---|
| A1 Namefix | PASS | grep cây live `web/` = 0 match "DeepSeek R1" ở file runtime (chỉ còn trong `*.bak` không serve/import). 5 trang UI + `app.js` đều là "DeepSeek Reasoner (V4-Flash Thinking)" |
| A2 PL-1 | PASS | Route table 5/5 id → explicit id (0 alias đi upstream); journal 05/07 04:15:08: `DeepSeek explicit route: deepseek-reasoner -> deepseek-v4-flash (thinking=True)`; call test id tường minh trả fingerprint `fp_8b330d02d0` (khớp); pilot V81 (id deepseek-chat) DISABLED từ V10644 + có safety-net route |
| A3 Registry | PASS | SHADOW_AUTO=8 đúng danh sách, output_eligible=15, RETIRED=6 đủ reason+date (dump chạy trên VPS) |
| A4 pro-real | PASS | Có trong lịch (SHADOW_ORDER_C16 8/8); first-run row id 21335: 2026-07-05 MN [73,87] strength 9.0 CHOT_HA, run_source=shadow_auto_eval, 04:26:24; registry first_run_date=2026-07-05; parser/usage OK |
| A5 Hash PRE | Chụp 11:23:58 | 4 hash ở header; GĐ2 sẽ chụp lại PRE tươi ngay trước F1 |
| A6 DISTINCT 30d | PASS* | 30 id predictions / 29 id eval — khớp registry 100% trừ 1 ngoại lệ giải trình được (phát hiện 5) |
| A7 CP-66.9 | PASS | Pool MN = `("MN_HYBRID_V1",)` duy nhất; V67 + intraday skip MN từ 06/07; money-board chặn `MN_ADAPTIVE_EXPLOIT_V1` khỏi khóa tuần mới ≥06/07; roadmap CLOSED_BY_OWNER_ABANDON; lock tuần 29/06 (MN=ADAPTIVE) hết hạn hôm nay |

## 3. PHẦN B — REASONING-FIRST POOL (B2 = đo thật 1 call/model, config + key production)

### 3a. Official 7 AI (output-eligible)

| Model | Route đang gọi | Thinking đo được | Max tokens | P&L 56d (2-số) | Version cao nhất của nhà | Đề xuất |
|---|---|---|---|---|---|---|
| deepseek-reasoner | explicit v4-flash+thinking | ON (fp khớp) | 16,384 | **+94.2M** (tốt nhất hệ) | V4 (pro đã có lane riêng) | GIỮ NGUYÊN — anchor |
| gpt-5.4 | gpt-5.4 | 0 reasoning toks (không set effort) | 16,384 | **+27.1M** | GPT-5.6 (preview gov-gated, GA ~giữa 07) | GIỮ — đang lời, không đổi |
| claude-opus-4-6 | opus-4-6 stream | OFF | 16,384 | +2.6M (18d id mới) | Opus 4.8 | GIỮ; option bật adaptive thinking (E3d) |
| claude-sonnet-4-6 | sonnet-4-6 | OFF | 16,384 | −15.3M (14d +15.2M) | Sonnet 5 (30/06: adaptive thinking mặc định, $2/$10 intro, cấm temperature, tokenizer +30%) | Theo dõi; nâng = id mới + lịch sử mới (E4) |
| gpt-5-mini | gpt-5-mini | ON (320 toks) | 16,384 | −29.6M (28d +3.2M) | GPT-5.6 Luna (gated) | GIỮ |
| gemini-2.5-flash | 2.5-flash | ON dynamic (34) | 65,536 | **−77.1M** | Gemini 3.x — shadow 3-flash đã đo −52.1M → retired | Cờ đỏ hiệu suất; 3.x KHÔNG phải giải pháp — review 14/07 |
| gemini-2.5-pro | 2.5-pro | ON dynamic (471) | 65,536 | **−90.5M** | 3.1-pro shadow đã đo −41.5M → retired | Cờ đỏ như trên |

### 3b. Shadow 8 (SHADOW_AUTO)

| Model | Thinking đo được | P&L 56d / 14d | Đề xuất |
|---|---|---|---|
| deepseek-v4-pro-real | ON (fp_9954b31ca7, max 393,216) | first-run hôm nay | GIỮ — mới chạy |
| glm-5.1 | ON (641 toks) | −21.2M / +2.8M | NÂNG glm-5.2 (E4a): 1M ctx, 128k out, RẺ hơn ($0.728/$2.288 vs $0.966/$3.036) |
| kimi-k2.5 | ON (897) nhưng latency 470s hôm nay → mất row | −68.2M / **+22.3M** | GIỮ, quyết thêm ở E1 |
| gpt-5.5 | ON nông (29) | −30.1M / 28d +6.0M | Bật effort high (E3c) |
| gpt-oss-120b | ON (110) | −60.8M / −40.9M | Review 14/07 |
| qwen3-max-thinking | **EXCLUDE → 0 toks** | −59.6M tổng (MN +7.1M) | Bật thinking thật (E3a) hoặc để qwen3.7 thay dần (E2) |
| grok-4.20-multi-agent | **EXCLUDE → 0 toks** | −29.7M / −37.0M | Bật effort high (E3b); nhà có grok-4.3 ($1.25/$2.5) |
| gemma-4-31b | thoughts nhẹ (141) — non-thinking | +9.1M/56d NHƯNG −9.1M/14d, −35.2M/28d | Trade-off FREE vs form xấu gần đây → đề xuất GIỮ vì free, chấm lại 14/07 |

### 3c. P&L 56d THEO TỪNG MIỀN (block `perregion`, chạy VPS 12:15 — công thức chuẩn hệ PTS=50, PAY=98k, COST 18k/18k/27k; công thức này khớp CHÍNH XÁC 5 con số retire trong registry: −118.2M/−72.6M/−33.9M/−41.5M/−52.1M)

| Model | MN | MT | MB | TỔNG |
|---|---|---|---|---|
| deepseek-reasoner | +40.1M | +41.8M | +12.3M | **+94.2M** |
| gemma-4-31b | +3.7M | +4.8M | +0.6M | +9.1M |
| glm-5.1 | +12.1M | +16.4M | −49.7M | −21.2M |
| gpt-5.5 | −17.4M | −17.4M | +4.8M | −30.1M |
| gpt-oss-120b | **+25.0M** | −25.1M | −60.6M | −60.8M |
| grok-4.20-multi-agent | **+23.7M** | −26.5M | −26.9M | −29.7M |
| kimi-k2.5 | −32.0M | −17.0M | −19.1M | −68.2M |
| qwen3-max-thinking | **+7.1M** | +2.9M | −69.6M | −59.6M |

Insight cho tool AI phân tích: nhiều shadow DƯƠNG ở MN (gpt-oss +25.0M, grok +23.7M, glm +12.1M, qwen +7.1M) nhưng bị MB kéo âm; duy nhất deepseek-reasoner dương cả 3 miền. kimi-k2.5 âm cả 3 miền trên 56d (nhưng 14d +22.3M — form mới cải thiện).

### 3d. B3 — Version mới các nhà (chỉ đề xuất; nâng version = id mới + lịch sử P&L mới từ 0)

- OpenAI: GPT-5.6 Sol/Terra/Luna (preview 26/06, ~20 org được duyệt, GA "vài tuần tới" — chưa đăng ký được)
- Anthropic: Sonnet 5 (30/06) + Opus 4.8
- Google: Gemini 3.1 Pro / 3 Flash preview — hệ ĐÃ đo shadow → âm → retired (bằng chứng thật, không đoán)
- xAI: grok-4.3 (30/04, $1.25/$2.5)
- Qwen: qwen3.7-max / qwen3.7-plus
- Moonshot: k2.7-code (chỉ code) / k2.5 = general reasoning mới nhất (đã có trong hệ)
- DeepSeek: V4 là thế hệ hiện hành (flash official + pro-real shadow từ hôm nay)
- Zhipu: glm-5.2 (rẻ hơn glm-5.1)

## 4. PHẦN C — OPENROUTER CONFIG CHUẨN + KIMI/QWEN

**C1 Config chuẩn (thiết kế, áp khi ký):** `reasoning: {"effort": "high"}` (hoặc `{"max_tokens": N}` với nhà tính budget); key từ env/DB settings — hiện KHÔNG hardcode (PASS); code hiện KHÔNG dùng `include_reasoning` deprecated, KHÔNG dùng hậu tố `:thinking` (PASS — `qwen3-max-thinking` là slug chính thức của Qwen, không phải suffix).

**C2 Chống bẫy token:** PASS — toàn bộ ~20 call test đều `finish_reason=stop`; max_tokens 16,000 ≥ 2× reasoning đo được (1.1k–3.4k); xác nhận OpenRouter tính reasoning vào completion_tokens.

**C3 Parser:** PASS 6/6 — test đúng combo production (json_object + temp=0 + reasoning effort high) trên kimi-k2.5 / qwen3.7-max / glm-5.1: reasoning không bị drop, JSON parse OK cả 2 combo. Production đang đọc `content` (OpenRouter) + `reasoning_content` (DeepSeek native, có log). Gap nhẹ: `_call_openrouter` chưa log reasoning_tokens/call — bổ sung khi thực thi F nếu ký.

**C4 KIMI đối đầu (3 call/model, config chuẩn):**

| | kimi-k2-thinking (11/2025) | kimi-k2.5 (01/2026 — thế hệ mới hơn) |
|---|---|---|
| Reasoning toks thật | 1,290 / 2,012 / 1,070 (avg 1,457) | 2,865 / 2,354 / 2,120 (avg **2,446**) |
| Latency | **5–17s** | 31–85s (production hôm nay 470s với prompt ~15k toks) |
| JSON parser | 3/3 OK | 3/3 OK |
| Chi phí thật/call | $0.0046 | $0.0071 (giá /M rẻ hơn: $0.375/$2.025 vs $0.6/$2.5) |
| Max output | 100,352 | không công bố (OpenRouter max_out=None) |

→ Khuyến nghị: theo tiêu chí owner (thế hệ cao nhất + thinking THẬT), hệ ĐÃ CÓ kimi-k2.5 đạt chuẩn → KHÔNG cần đăng ký thêm Kimi. Chỉ cân nhắc k2-thinking (nhanh 3–5×) làm ứng viên THAY k2.5 sau này nếu k2.5 tiếp tục rớt row vì latency.

**C5 QWEN:**

| | qwen3.7-max (0520) | qwen3.7-plus (0602) |
|---|---|---|
| Reasoning thật | **3,381 toks** (sâu nhất nhóm test) | 1,103 toks |
| Benchmark | AA Intelligence 56.6, reasoning 58.8, GPQA 92.3 (cao hơn kimi-k2.5 51.8) | thấp hơn max |
| Giá | $1.25/$3.75, 1M ctx, 65k out | $0.32/$1.28, 1M ctx, 65k out |
| Chi phí ước prompt production | ~$0.10/ngày 3 miền (~$3/tháng) | ~$0.03/ngày |

→ Khuyến nghị: **qwen3.7-max** — flagship + thinking thật sâu nhất, chi phí không đáng kể. Vai trò: shadow BỔ SUNG (id mới, lịch sử mới từ 0, không backfill); `qwen3-max-thinking` giữ chạy để so — thành ứng viên retire sau nếu tiếp tục âm.

## 5. PHẦN D — AUDIT PROMPT MIỀN/THỨ

**D1** Prompt nguyên văn 3 miền dựng từ ĐÚNG code path production + DB thật trên VPS (khớp cấu trúc trace PB-18.0 hôm nay): `artifacts/v10780_prompt_audit/vps/prompt_{MN,MT,MB}_2026-07-05.txt` (37.3 / 36.6 / 41.3 KB, gồm system prompt).

**D2 Chấm điểm:**

| Tiêu chí | MN | MT | MB |
|---|---|---|---|
| (i) Ghi rõ MIỀN dự đoán | ĐẠT — `## DỰ ĐOÁN CHO: MIỀN NAM` + nhắc lại đậm trong YÊU CẦU | ĐẠT | ĐẠT |
| (ii) THỨ + ngày dương | ĐẠT — `## NGÀY: 2026-07-05 (Chủ Nhật)` | ĐẠT | ĐẠT |
| (iii) Danh sách đài + số đài | **SAI: 5 đài (lẫn 2 đài MT)** | ĐẠT 3 đài đúng | ĐẠT Thái Bình |
| (iv) Nhãn miền trên dữ liệu lịch sử | THIẾU nhãn thời gian ("MIỀN BẮC — ƯU TIÊN ?" không có "HÔM QUA"/ngày) | ĐẠT đầy đủ `MIỀN NAM (HÔM QUA) — ƯU TIÊN 1 (MN(D-1) 2026-07-04, 4 đài)` | ĐẠT |
| (v) Output ràng buộc miền | CÓ nêu MIỀN đậm trong YÊU CẦU; JSON schema không field miền (chấp nhận được — mỗi call 1 miền) | như MN | như MN |

**D3 Cross-region scan:** 3 điểm assemble source_data (job 04:00, MB re-predict, shadow eval) đều đúng SSOT soi chéo (MN←D-1 MB/MT/MN; MT←D-1×3+MN(D); MB←D-1×3+MN(D)+MT(D)) — mọi nguồn cross-region CÓ nhãn miền. `_V10766_SKIP_MT_REPREDICT=True` xác nhận còn hiệu lực (MN về chỉ re-predict MB). Context pack / mined rules / KB / lịch sử đài bucket đúng miền+thứ target. KHÔNG tìm thấy đường rò không nhãn — trừ lỗi (iii) MN (dữ liệu đài nhiễm 2020–21).

**D4 Đề xuất (thiết kế — CHƯA deploy, tôn trọng V10768 không WR/BT ranking):**
- FIX-1 (SỬA CLARITY): MN dùng key nguồn D-1 chuẩn như MT/MB → nhãn thành `MIỀN BẮC (HÔM QUA) — ƯU TIÊN 1 (MB(D-1) <ngày>, 1 đài)` thay vì "ƯU TIÊN ?". Chỉ đổi text nhãn, data giữ nguyên.
- FIX-2 (SỬA LOGIC nhẹ): query đài-hôm-nay giới hạn cửa sổ 84 ngày (`AND date >= date(?, '-84 day')`) → MN Chủ Nhật ra đúng 3 đài. Sửa QUERY ĐỌC, KHÔNG ghi/sửa bảng lottery_results. Bonus: sửa luôn `target_station_set_label` trong trace/bucket đang bị nhiễm.
- FIX-3 (SỬA CLARITY): thêm 1 câu ràng buộc trong YÊU CẦU: "Chỉ chốt số cho MIỀN X; dữ liệu miền khác chỉ dùng làm tín hiệu soi chéo."

## 6. PHẦN E — BẢNG XÁC NHẬN OWNER (DỪNG CHỜ KÝ TỪNG DÒNG)

**GIỜ KHÓA TUẦN /choi (E5):** lock tuần 06/07 được tạo ở lần compute_board() ĐẦU TIÊN sau 00:00 06/07 (+07) — lượt mở /choi đầu tiên sau nửa đêm hoặc job scheduler sáng mai; đã tạo là KHÓA cả tuần (UNIQUE region+week). → Muốn đổi hành vi tuần 06/07 phải ký + deploy TRƯỚC 00:00 đêm nay; đề nghị ký E5 trước ~22:00. Không kịp → tự động fallback an toàn MN_HYBRID_V1 đúng blocking rule.

| # | Quyết định | Số liệu chốt | Khuyến nghị | Ký |
|---|---|---|---|---|
| E1 | Đăng ký thêm Kimi? | k2.5 đã có: reasoning 2,446 toks thật, 14d +22.3M, nhưng latency 470s làm mất row hôm nay; k2-thinking nhanh 5–17s, $0.0046/call | KHÔNG đăng ký thêm (k2.5 đã cover Moonshot); option B: k2-thinking nếu ưu tiên latency | ☐ |
| E2 | Đăng ký Qwen? | qwen3.7-max: thinking thật 3,381 toks, AA 56.6, ~$3/tháng | OK — qwen3.7-max SHADOW_AUTO, shadow_only=1, output_eligible=0, first_run 06/07, không backfill | ☐ |
| E3a | qwen3-max-thinking: bỏ `exclude` → `effort high` + max_tokens 32,768 | Đang 0 reasoning toks; tổng −59.6M/56d (MN +7.1M) | OK (shadow-only, đo lại đúng bản chất thinking) | ☐ |
| E3b | grok-4.20-multi-agent: bỏ `exclude` → `effort high` | Đang 0 reasoning toks; −29.7M/56d (MN +23.7M) | OK (shadow-only) | ☐ |
| E3c | gpt-5.5: thêm `reasoning effort high` | Reasoning nông 29 toks; 28d +6.0M | OK (shadow-only) | ☐ |
| E3d | Official: bật adaptive thinking sonnet/opus + reasoning_effort gpt-5.4 | gpt-5.4 đang +27.1M KHÔNG thinking; sonnet 14d +15.2M | KHÔNG đợt này — đổi hành vi official rủi ro; xem lại 14/07 | ☐ |
| E4a | glm-5.1 → glm-5.2 (id mới, lịch sử mới) | glm-5.2: 1M ctx, 128k out, RẺ hơn; glm-5.1: −21.2M/56d, 14d +2.8M | Trung lập — nếu ký: chạy song song rồi retire glm-5.1 sau khi 5.2 đủ dữ liệu; rủi ro thêm 1 lane token | ☐ |
| E4b | Nâng version khác (grok-4.3 / Sonnet 5 / Gemini 3.x) | Gemini 3.x đã có bằng chứng shadow ÂM; GPT-5.6 chưa GA | KHÔNG đợt này — chờ 14/07 + GPT-5.6 GA | ☐ |
| E5 | /choi MN tuần 06/07: (A) BT 1-SỐ nguồn official bạch-thủ + NGHỈ T7 (V10777: +7.6M bền bỏ-T7, forward 14d +6.8M) hay (B) giữ fallback MN_HYBRID_V1? | Deadline ký trước ~22:00 tối nay; qua 00:00 là khóa tự động | Nếu owner tin số V10777 → A; không kịp test đầy đủ trước giờ khóa → giữ B theo blocking rule | ☐ A / ☐ B |
| E6a | Áp FIX-1 + FIX-3 (SỬA CLARITY nhãn nguồn MN + câu ràng buộc miền) cho official? | Chỉ đổi text nhãn/1 câu, data không đổi | OK | ☐ |
| E6b | Áp FIX-2 (query đài 84 ngày — sửa lỗi 5 đài MN) cho official, hay shadow test 1 ngày trước? | Sửa lỗi factual đang nhiễm prompt + bucket label MỖI NGÀY | OK áp official (sửa query đọc, không ghi bảng official); nếu muốn chắc → shadow 1 ngày | ☐ |

## 7. TRẠNG THÁI TỪNG MỤC (PASS/FAIL/BLOCKED/CHỜ)

| Mục | Trạng thái |
|---|---|
| PHẦN A (A1–A7) | PASS 7/7 (A6 có 1 ngoại lệ giải trình được) |
| PHẦN B (B1–B3) | DONE — 2 model thinking tắt ngầm (finding 2); +7.1M đã giải trình per-region |
| PHẦN C (C1–C5) | DONE — khuyến nghị: không thêm Kimi; thêm qwen3.7-max |
| PHẦN D (D1–D4) | DONE — 1 lỗi factual đài MN (finding 1) + 2 fix clarity |
| PHẦN E | **CHỜ OWNER KÝ TỪNG DÒNG** |
| PHẦN F (thực thi + verify + docs) | BLOCKED chờ chữ ký E |
| Runtime thay đổi trong phiên | **ZERO** (chỉ 2 script audit read-only, chưa deploy) |

## 8. GHI CHÚ CHO TOOL AI PHÂN TÍCH THÊM

- Công thức P&L chuẩn hệ (2-số/miền/ngày): profit = nhảy×50×98,000 − số_đài×2×50×COST, COST = 18k (MN/MT), 27k (MB). Công thức đã đối chiếu khớp chính xác 5 con số retire registry V10779.
- Cửa sổ đo: 56d (10/05→04/07). Multi-window qwen3-max-thinking: −59.6M/56d, −53.5M/28d, −44.5M/14d; BT (1-số) −89.1M/56d.
- Câu hỏi mở đáng phân tích: (1) pattern "shadow dương MN, âm MB" (gpt-oss/grok/glm/qwen) — do MB 27k cost + 1 đài, hay do bản chất model? (2) kimi-k2.5 đảo chiều 14d +22.3M sau 56d −68.2M — form thật hay nhiễu? (3) gemma-4-31b +9.1M/56d nhưng âm dần (−35.2M/28d, −9.1M/14d) — giữ vì free đến bao giờ? (4) gemini-2.5 official âm nặng nhất hệ (−77.1M/−90.5M) mà Gemini 3.x shadow cũng âm → có nên đề xuất owner cắt hẳn nhà Google khỏi official (cần gate riêng vì đổi output 15/15)?
- Lock V10768 de-herding vẫn hiệu lực: context pack KHÔNG chứa WR/BT ranking; audit D không đề xuất đưa lại.
