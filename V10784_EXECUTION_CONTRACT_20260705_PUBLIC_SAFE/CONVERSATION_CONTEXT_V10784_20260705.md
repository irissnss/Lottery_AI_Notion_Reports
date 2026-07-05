# CONVERSATION CONTEXT — V10784 (phiên 05/07/2026, chiều → đêm)

Ghi verbatim các message của owner trong phiên (thứ tự thời gian). Phục vụ §52F.5 — public repo giữ cùng context với Notion.

## Message 1 (~16:0x) — sau phiên V10782

> Cập nhật báo cáo trước đi đã em

## Message 2 (~16:2x) — PROMPT TỔNG LỰC V10783

> V10783 — PROMPT TỔNG LỰC: ỔN ĐỊNH LIVE MT/MB HÔM NAY + VÁ LOGGING + ĐỘC LẬP MIỀN×THỨ×TUẦN + CYCLE SCAN + TRẢ NỢ P2-UI/P3/P4/P5
> Ngày 05/07/2026, 16:2x. Thứ tự BẮT BUỘC: PHẦN 0 xong trước 16:45. Phạm vi can thiệp: CHỈ official + /choi; lane test/shadow GIỮ NGUYÊN hành vi (chỉ tách hiển thị). Báo cáo theo §52G GitHub-first.
> (PHẦN 0 — KHẨN: MT 16:55 / MB 17:55 HÔM NAY … PHẦN 1 — VÁ LOGGING … PHẦN 2 — METHOD LOCK HOÀN TẤT … PHẦN 3 — ĐĂNG KÝ GEMINI SHADOW LANE … PHẦN 4 — VIỆC DÀI TRONG ĐÊM … PHẦN 5 — VERIFY + BÁO CÁO — toàn văn lưu tại BAO_CAO_PARTIAL_V10783 folder V10783_LIVE_STABILITY_PARTIAL_20260705_PUBLIC_SAFE)

## Message 3 (16:44) — owner flag chậm trễ

> đẩy báo cáo dùm anh đi nào prompt dài thế mà thực hiện cái gì vắng tắc quá lý do là gì chờ gì tại sao

## Message 4 (16:5x) — PROMPT TỔNG LỰC V10784 (hợp đồng thực thi — toàn văn)

> V10784 — PROMPT TỔNG LỰC: HỢP ĐỒNG THỰC THI ĐẾN HẾT + CỨU EVAL ĐƠN MODEL + VERIFY FREEZE MT/MB + TRẢ TOÀN BỘ NỢ P1–P6 TRONG ĐÊM NAY
> Ngày 05/07/2026, 16:5x. Báo cáo §52G GitHub-first.
>
> ■ HỢP ĐỒNG THỰC THI (ràng buộc cứng, đặt trên mọi phần)
> - CHẠY ĐẾN HẾT danh sách. CẤM dừng phiên để hỏi owner khi việc không cần chữ ký. Chỉ 2 lý do được dừng: (a) đụng mục cần chữ ký owner theo danh sách LOCKED; (b) lỗi nguy hại hệ thống — khi đó ghi BLOCKED + lý do, NHẢY SANG PHẦN KẾ, cuối phiên gom lại.
> - Deliverable theo mốc: 18:15 báo partial #1 (P0) · 21:00 partial #2 (P1+P2) · trước 00:00 báo cáo tổng V10784. Không phụ thuộc câu trả lời nào của owner.
> - Việc quan sát (watch) chạy nền — không được lấy watch làm lý do ngồi chờ.
>
> PHẦN 0 — KHẨN NGAY (trước 17:45)
> 0.1. CỨU EVAL ĐƠN MODEL (nghi tác dụng phụ freeze — ưu tiên số 1):
> - Kiểm tra: model_daily_eval + luồng eval đơn model (kể cả shadow_auto_eval) hôm nay 05/07 có rows sau kết quả MN ~16:35 không? So với nhịp các ngày trước.
> - Nếu thiếu: trace đường ghi eval qua hook freeze trong database.py — freeze CHỈ được chặn predictions/final_bundles official surface của ngày đã chốt; PHẢI whitelist tường minh: lottery_results, model_daily_eval, mọi bảng eval/đo lường, mọi lane shadow/test.
> - Hotfix whitelist + smoke (giả lập 1 write eval sau freeze → PHẢI đi qua) + backfill eval MN hôm nay theo đúng cơ chế chuẩn (từ predictions + lottery_results, không sửa tay).
> - Deploy hotfix TRƯỚC 17:45 để MB không dính lỗi tương tự (kết quả MB ~18:30 > freeze 17:55 — nếu không vá, eval MB tối nay cũng đứng im). Tránh cửa sổ cấm 16:45–17:00 nếu còn trong đó thì làm ngay sau 17:00.
> 0.2. VERIFY FREEZE MT HẬU KIỂM (watch script đã fail): query trực tiếp DB + log: T-10 16:45 có chạy không, freeze 16:55 có fire không, sau 16:55 có write official nào bị chặn/late=1 không, card + total MT có đứng yên không. Xuất bảng bằng chứng.
> 0.3. SỬA WATCH SCRIPT (timeline trống): fix nguyên nhân, chạy lại cho MB — phải thấy events ghi vào watch_timeline.jsonl trước 17:40.
> 0.4. MB LIVE: xác nhận T-10 17:45 + freeze 17:55 fire đúng, quan sát 17:45–18:00 (không deploy trong cửa sổ này), verify eval MB chạy bình thường sau kết quả ~18:30 (nhờ hotfix 0.1).
> 0.5. Sau 18:00: upload frontend user-view.js (surface=official) — hoàn tất tách hiển thị lane test khỏi card official.
>
> PHẦN 1 — LOGGING (xong trước 23:00)
> 1.1. Parse reasoning vào DB: cả `reasoning` (OpenRouter) lẫn `reasoning_content` (DeepSeek native) → reasoning_json + reasoning_tokens gắn từng prediction row. Gap đã xác định: OpenRouter trả về nhưng chưa parse.
> 1.2. Lưu đủ custom_prompt trace.
> 1.3. Smoke NGAY bằng 1 call nhỏ mỗi route: qwen3-max-thinking / grok-4.20-multi-agent / gpt-5.5 → reasoning_tokens > 0 ghi thật vào DB. Không đợi run 06/07.
> 1.4. Dựng checklist verify tự động sáng 06/07: reasoning>0 (3 model E3 + qwen3.7-max + glm-5.2 + Gemini lane mới) · first-run 2 model mới · /choi MN = MN_BT1_OFFICIAL_V1 đúng lock · prompt 3 miền đúng đài THỨ HAI · freeze fire đúng 3 mốc · eval đơn model chạy đủ 3 miền.
>
> PHẦN 2 — METHOD LOCK HOÀN TẤT (xong trước 23:00)
> 2.1. UI /choi in method lock tuần 06/07 đủ 3 miền (MN=MN_BT1_OFFICIAL_V1 BT 1-số nghỉ T7 · MT=MT_ADAPTIVE_EXPLOIT_V1 · MB=MB_ADAPTIVE_EXPLOIT_V1) + ngày ký + tham chiếu quyết định.
> 2.2. Chạy audit hồi tố _v10782_p2_seed_audit.py toàn lịch sử — báo trung thực mọi trường hợp đổi method trong tuần/sau giờ kết quả.
> 2.3. Commit private governance còn treo (CHANGELOG + AUTOMATION_STATE seq 238) — không để governance lệch code.
>
> PHẦN 3 — ĐĂNG KÝ GEMINI SHADOW LANE (deadline cứng 23:30, làm trước phần dài)
> Audit config Gemini hiện tại (bản, route, thinking budget, log reasoning) + đăng ký lane shadow Gemini flash mới nhất, thinking bật đúng chuẩn, shadow_only=1, output_eligible=0, first_run 06/07, không backfill, thinking_enabled_date riêng. Không đụng 2 lane Gemini official.
>
> PHẦN 4 — VIỆC DÀI TRONG ĐÊM (làm tuần tự tới đâu báo tới đó, không bỏ)
> 4.1. P3 cũ: bộ lọc lịch sử dự đoán trên bảng hiện có (miền/model/lane/method/khoảng ngày, mặc định 7 ngày, phân trang server-side, không đẻ bảng mới).
> 4.2. Ma trận ĐỘC LẬP MIỀN×THỨ×TUẦN: mọi tham số chuỗi prompt→model→total→UI→/choi gắn nhãn GLOBAL / per-MIỀN / per-MIỀN×THỨ / per-TUẦN; mục GLOBAL nào nên tách thì đề xuất kèm evidence (không tách máy móc, có default kế thừa).
> 4.3. CYCLE SCAN (measurement-only): lưới lag {D-1,D-2,D-3,D-7 cùng-thứ,D-14,D-28} × miền × thứ × đài × vị trí (BT/G2/lô2) trên DB từ 10/05 (kết quả xổ dùng lịch sử dài, chú ý sáp nhập tỉnh 01/07/2025), so baseline + out-of-sample 70/30 + ổn định 2 nửa cửa sổ; sanity check phải nhìn thấy lại MN D-1 ~73% và MB G2 lag V106.04A; output vào shadow rules schema chuẩn; CẤM áp official trước 14/07.
> 4.4. Ma trận trùng lặp mục đích → bảng/endpoint/card/script → GIỮ / HỢP NHẤT / ĐỀ XUẤT BỎ (chờ ký, không xóa).
>
> PHẦN 5 — VERIFY + BÁO CÁO (trước 00:00)
> 5.1. Hash 4 bảng: chỉ natural growth (kết quả xổ MT/MB + eval backfill MN theo cơ chế chuẩn — ghi rõ diff eval do hotfix 0.1); khác biệt khác = dừng + điều tra.
> 5.2. Kiểm tra 23:50: money_board_lock tuần 06/07 nguyên vẹn (MN_BT1_OFFICIAL_V1/MT/MB) để compute_board() sau 00:00 tạo lock đúng.
> 5.3. Báo cáo V10784: GitHub public-safe + Notion ≤30 dòng + cập nhật 26_RUNTIME_AS-BUILT (mục 1 thêm freeze + whitelist eval; Sổ CLOSED thêm các mục đã đóng) + AUTOMATION_STATE.
> 5.4. Blocking: cấm deploy 17:45–18:00 ngoài quan sát; sau 00:00 cấm mọi thay đổi ảnh hưởng lock tuần; mọi mục cần chữ ký → gom 1 bảng cuối báo cáo, không tự quyết.

## Message 5 (~18:4x) — chỉ đạo bổ sung UI

> Good. Now update `user-view.js` to server-side pagination with a 7-day default.
