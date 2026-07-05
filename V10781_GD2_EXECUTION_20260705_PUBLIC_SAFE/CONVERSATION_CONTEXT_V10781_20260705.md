# CONVERSATION CONTEXT — V10781 (2026-07-05)

Nguyên văn prompt owner cấp cho phiên GĐ2 (V10781). Các quyết định ký trong PHẦN 0 là căn cứ thực thi duy nhất.

---

## Owner message (nguyên văn)

```
PROMPT TỔNG LỰC — GĐ2 THỰC THI V10780 (OWNER KÝ TẠI ĐÂY) + UI AUTO-DISPLAY + DỌN ROOT/VPS/CODE +
PROMPT CONTEXT V2 (SHADOW) + CHÍNH SÁCH BÁO CÁO GITHUB-FIRST
Kế thừa: V10780 GĐ1 (PASS 7/7, zero runtime change). Delivery = version kế tiếp còn trống (~V10781).
Backup backups/<version>_pre/. Timezone: Asia/Ho_Chi_Minh. Ngày: 05/07/2026.
DEADLINE CỨNG: E5 phải deploy + verify TRƯỚC 00:00 đêm nay (lock tuần 06/07 tạo ở compute_board()
đầu tiên sau 00:00). Ưu tiên: PHẦN 1 (E5 + E6) → PHẦN 2 → PHẦN 3-4 → PHẦN 5 (được phép trả sau).

======== PHẦN 0 — CHỮ KÝ OWNER (đóng bảng E của V10780) ========
E1 = KHÔNG đăng ký thêm Kimi. Ghi FU: nếu kimi-k2.5 rớt row thêm ≥2 lần trước 14/07 → trình lại
     phương án k2-thinking (5-17s). Đồng thời THIẾT KẾ (plan-only, chưa deploy) cơ chế "late-fill
     shadow row" từ trace call thành công sau soft-continue 90s nhưng trước closeout — trình 14/07.
E2 = OK: đăng ký qwen3.7-max — SHADOW_AUTO, shadow_only=1, output_eligible=0, không backfill,
     first_run 06/07, config chuẩn reasoning effort high, giá thật, id tường minh.
E3a = OK: qwen3-max-thinking bỏ exclude → effort high + max_tokens 32,768 (shadow-only).
E3b = OK: grok-4.20 bỏ exclude → effort high; kiểm tra + sửa luôn slug đúng bản multi-agent nếu
      registry khai multi-agent (nếu slug thường là chủ đích thì đổi display/id cho trung thực).
E3c = OK: gpt-5.5 thêm effort high (shadow-only).
E3d = KHÔNG: official (gpt-5.4, sonnet, opus) GIỮ NGUYÊN config — xem lại 14/07.
QUY TẮC ĐO SAU E3: 3 model vừa bật thinking phải gắn mốc "thinking_enabled_date=2026-07-05" trong
registry note; mọi bảng so găng sau này tách rõ trước/sau mốc, KHÔNG trộn 2 giai đoạn.
E4a = OK: đăng ký glm-5.2 chạy song song glm-5.1; xét retire 5.1 tại 14/07 khi 5.2 đủ dữ liệu.
E4b = KHÔNG nâng version khác đợt này.
E5 = A: /choi MN tuần 06/07 = BT 1-SỐ, nguồn OFFICIAL BẠCH-THỦ, NGHỈ T7 (số đài/vốn tính theo lịch
     đài THẬT sau FIX-2, không dùng danh sách đài cũ). MT/MB giữ nguyên. Logic NGHỈ T7 phải là code
     rõ ràng + hiển thị lý do trên /choi. KHÔNG KỊP test đầy đủ trước 00:00 → fallback MN_HYBRID_V1,
     báo rõ — không khóa ẩu.
E6a = OK: FIX-1 + FIX-3 (nhãn nguồn MN + câu ràng buộc miền) áp official.
E6b = OK: FIX-2 áp official — query đài giới hạn 84 ngày (chỉ sửa QUERY ĐỌC, không ghi bảng official)
      + sửa target_station_set_label. Sau fix: dựng lại prompt 3 miền, xác nhận MN đúng 3 đài CN
      (Tiền Giang, Kiên Giang, Đà Lạt) + lịch đài 7 ngày × 3 miền khớp thực tế sau sáp nhập tỉnh;
      diff prompt TRƯỚC/SAU đính kèm. 229 rows 2020-2021 gán nhầm miền: KHÔNG sửa bảng official —
      ghi thành data-annotation note + FU xử lý riêng có giám sát.

======== PHẦN 1 — THỰC THI THEO CHỮ KÝ (thứ tự: E6b → E6a → E5 → E2/E3/E4a) ========
1.1 Chụp hash PRE tươi 4 bảng official ngay trước thay đổi đầu tiên (mốc 11:23:58 chỉ để đối chiếu).
1.2 Thực thi từng dòng đã ký, mỗi dòng: backup → sửa → test → bằng chứng.
1.3 MA TRẬN TƯƠNG THÍCH sau khi xong: SHADOW_AUTO_EVAL_MODELS đúng danh sách mới (8+2=10);
    scheduler route đúng (openrouter/zhipu/deepseek); aggregation-signal + mn_bt + plurality/
    top1-strength/combo-super + MN cap + trọng số total output: model mới + model vừa bật thinking
    chỉ vào pool theo rule dữ liệu tối thiểu, RETIRED không lọt; /choi MN mới không rò sang /du-doan;
    watch panel + money board + bảng MN BT 1 SỐ (V10777) tiếp tục cập nhật đủ 8 nguồn; lineage 0 đứt;
    chi phí token/ngày ước tính sau thay đổi.

======== PHẦN 2 — UI DISPLAY NAME: AUTO TỪ 1 NGUỒN (hết hardcode 12 chỗ) ========
2.1 Thêm display_name chính thức vào model_registry cho TỪNG model (một nguồn sự thật duy nhất).
2.2 API/UI (monitoring, du-doan, choi, accuracy, viewer, settings, index, user-view, app.js…) lấy
    display_name qua 1 helper/endpoint chung; XÓA mọi mapping tên hardcode rải rác.
2.3 Auto-case fallback: id chưa có display_name → tự sinh Title Case chuẩn (vd "deepseek-v4-pro-real"
    → "DeepSeek V4 Pro Real"), quy tắc viết hoa brand (DeepSeek, GPT, GLM, Grok, Qwen, Kimi, Gemma).
2.4 Verify: grep 0 hardcode tên model còn sót trong UI; chụp 5 trang UI sau đổi; label reasoner
    vẫn "DeepSeek Reasoner (V4-Flash Thinking)".

======== PHẦN 3 — CHÍNH SÁCH BÁO CÁO GITHUB-FIRST (áp dụng từ báo cáo version này) ========
3.1 BÁO CÁO CHI TIẾT ĐẦY ĐỦ (evidence, bảng số, trace, toàn văn) → GitHub public-safe repo
    (Lottery_AI_Notion_Reports/<version>_.../) như hiện nay — đây là bản gốc.
3.2 Notion mỗi version CHỈ 1 trang tóm tắt ngắn (≤30 dòng): kết quả chính + quyết định owner +
    link GitHub — không đổ toàn văn evidence vào Notion nữa.
3.3 BÀI HỌC / KIẾN THỨC / KIẾN TRÚC (vd: 3 tầng tên DeepSeek, bài học alias, công thức P&L chuẩn,
    insight per-region MB kéo âm, chuẩn OpenRouter reasoning{}) → bổ sung vào trang knowledge Notion
    (Knowledge Locks / SSOT) — Notion là nơi tài liệu chuẩn.
3.4 Ghi chính sách này vào quy tắc vận hành (AGENTS/working rules) để mọi phiên sau tuân theo.

======== PHẦN 4 — DỌN ROOT + VPS + CODE (an toàn, có manifest, DELETE chỉ đề xuất) ========
4.1 Inventory root local + VPS: kích thước, ngày sửa cuối, phân loại: CORE-RUNTIME / OPS-MỚI-NHẤT /
    BACKUP-LỚN-GIỮ / ARCHIVE (cũ, không import/serve) / ĐỀ-XUẤT-XÓA.
4.2 Kiểm chứng TRƯỚC khi di chuyển: grep import/reference + access log — file nào đang được
    import/serve thì tuyệt đối không đụng. Scripts _v107xx/_v108xx một lần đã chạy xong → archive/.
4.3 Di chuyển ARCHIVE vào archive/<năm>/ kèm MANIFEST (path cũ → mới, lý do, hash); *.bak trong
    web/ chuyển khỏi cây serve. KHÔNG XÓA gì trong đợt này — danh sách ĐỀ-XUẤT-XÓA trình owner ký riêng.
4.4 VPS: disk usage tổng + top thư mục; log rotation đang bật chưa; backup cũ quá hạn liệt kê
    (giữ backup lớn theo ý owner — chỉ đề xuất dọn bản trùng lặp).
4.5 Code hygiene (không đổi hành vi): liệt kê dead code path/flag hết hiệu lực/comment mồ côi —
    ĐỀ XUẤT dọn đợt sau, đợt này không sửa logic. Smoke đầy đủ sau khi di chuyển file.

======== PHẦN 5 — PROMPT CONTEXT V2 (THIẾT KẾ + SHADOW, KHÔNG áp official) ========
Mục tiêu owner: prompt ngữ cảnh sâu sắc chứa yếu tố cốt lõi, linh hoạt theo TUẦN/THỨ/MIỀN,
tự tổng hợp tự động hằng ngày từ DB.
5.1 Thiết kế CONTEXT PACK V2 tự tổng hợp mỗi ngày, per miền × thứ: (i) header chuẩn miền/thứ/ngày/
    đài hiện hành (sau FIX-2); (ii) mốc dữ liệu đúng doctrine miền (MN D-1, MB mốc-điều-kiện V10770,
    MT theo lock); (iii) pattern thống kê per miền × thứ từ soi-cầu v2 + rules V10667 (dạng dữ kiện
    trung tính); (iv) đặc trưng ngày (đầu tháng, sau ngày nghỉ…). RÀNG BUỘC: tôn trọng V10768 —
    TUYỆT ĐỐI không WR/BT ranking model vào context; không leak kết quả tương lai.
5.2 Chạy SHADOW: 1 lane prompt-v2 dùng chính deepseek-reasoner (id lane riêng, shadow_only=1) so
    đối đầu prompt v1 official cùng model — đo 7-14 ngày, trình 14/07. KHÔNG đổi prompt official
    ngoài FIX-1/2/3 đã ký.
5.3 Ước chi phí lane v2/ngày trước khi bật; vượt ngân sách shadow hiện tại → trình trước.

======== PHẦN 6 — VERIFY + BÁO CÁO ========
6.1 Hash POST = PRE 4 bảng official (lệch tự nhiên giải trình từng row); smoke /api/health, /du-doan,
    /choi, /monitoring; registry text-proof TRƯỚC/SAU; diff prompt TRƯỚC/SAU 3 miền.
6.2 Evidence E5: money board lock 06/07 = MN BT 1-số official bạch-thủ + NGHỈ T7 + vốn đúng lịch đài mới.
6.3 NGÀY MAI 06/07 báo cáo bổ sung: first-run qwen3.7-max + glm-5.2; 3 model bật thinking có
    reasoning tokens > 0 trong run thật; /choi MN ngày đầu đúng lock; prompt MN đúng đài thứ Hai.
6.4 Báo cáo THEO CHÍNH SÁCH MỚI: GitHub full + Notion 1 trang ngắn + bài học vào trang knowledge.
    FU checkpoint 14/07 đủ hạng mục: MB RF@COND, MT wplur_rf2_ml, MN ai_plurality2, MN BT nguồn số,
    lane model mới + 3 model sau mốc thinking, kimi-k2.5 form 14d + late-fill design, gemma-4-31b,
    gate nhà Google (official −77.1M/−90.5M), glm-5.1 vs 5.2, prompt v2 vs v1, đề-xuất-xóa root.

======== BLOCKING RULES ========
- E5 không kịp test đầy đủ trước 00:00 → fallback MN_HYBRID_V1 + báo rõ, không khóa ẩu.
- Hash official lệch không giải trình → rollback backups/<version>_pre/ + báo ngay.
- File đang import/serve → cấm di chuyển. Không xóa gì đợt này.
- Model smoke fail → không đăng ký con đó, phần khác chạy tiếp.
- Phần 5 chỉ shadow; mọi thay đổi prompt official ngoài FIX-1/2/3 = CẤM.
- Ngoài phạm vi → không làm, ghi "ngoài phạm vi".
```

---

Trước đó trong cùng phiên (sau khi báo cáo GĐ1 V10780), owner có 2 tin nhắn ngắn:
- "cái gì vậy chưa xong mà em tiếp đi em"
- "Em không tổng hợp đầy đủ chi tiết lên github và Notion MCP ah em? làm điể tool Ai của anh hỗ trợ phân tích thêm"
