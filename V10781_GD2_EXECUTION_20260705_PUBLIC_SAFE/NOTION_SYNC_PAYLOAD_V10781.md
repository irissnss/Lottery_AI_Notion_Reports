# V10781 — GĐ2 thực thi chữ ký owner + UI auto-display + §52G + dọn + Context V2 shadow (2026-07-05)

**Trang tóm tắt theo chính sách §52G GITHUB-FIRST (≤30 dòng). Bản gốc chi tiết: GitHub.**

## Kết quả chính
1. **E6b:** query đài giới hạn 84 ngày → prompt MN Chủ Nhật từ 5 đài SAI → đúng **3 đài** (Tiền Giang, Kiên Giang, Đà Lạt); lịch 7 ngày × 3 miền khớp thực tế; diff PRE/POST đính kèm GitHub.
2. **E6a:** nhãn nguồn MN chuẩn `MB(D-1)/MT(D-1)/MN(D-1)` + câu ràng buộc miền trong YÊU CẦU — áp official.
3. **E5 KỊP DEADLINE:** /choi MN tuần 06/07 = **BT 1-SỐ official bạch-thủ, NGHỈ T7** (code tường minh + lý do trên UI), vốn theo lịch đài thật (2.7M/ngày 3 đài) — KHÔNG cần fallback.
4. **E2+E4a:** đăng ký `qwen3.7-max` + `glm-5.2` SHADOW_AUTO (first_run 06/07) → shadow 8→10; output official **15/15 KHÔNG đổi**.
5. **E3a/b/c:** bật reasoning effort high cho qwen3-max-thinking / grok-4.20 (sửa slug đúng bản **multi-agent**) / gpt-5.5; mốc `thinking_enabled_date=2026-07-05` — so găng sau tách trước/sau mốc.
6. **UI display name 1 nguồn:** registry + `/api/model-display-names` + `model-names.js`; 7 trang bỏ hardcode; label reasoner giữ nguyên.
7. **Dọn (không xóa):** 10 script one-off → archive + manifest; 4 file .bak VPS rời cây serve; đề-xuất-xóa trình riêng (dup DB 316M…).
8. **Context Pack V2 (shadow):** lane A/B 1-biến `PROMPT_V2_AB_V1` cùng deepseek-reasoner, cron 3 miền, **$0.134/ngày**; run đầu MN: v2=73 vs v1=85; tôn trọng V10768 (zero WR/BT ranking).
9. **Hash 4 bảng official PRE=POST IDENTICAL 4/4** (predictions 9,304 `5e92c59e…` · final_bundles 382 `1bef9c34…` · lottery_results 15,010 `2076e8f7…` · model_daily_eval 9,132 `cbd1f568…`).

## Quyết định owner đã thực thi
E1 KHÔNG Kimi (late-fill design 14/07) · E2 OK · E3a/b/c OK · E3d KHÔNG (official giữ nguyên) · E4a OK · E4b KHÔNG · E5=A (BT 1-số + nghỉ T7) · E6a OK · E6b OK (229 rows = annotation-only).

## Theo dõi
- **06/07:** first-run 2 model mới; reasoning tokens > 0 của 3 model thinking; /choi MN ngày đầu; prompt MN đài thứ Hai.
- **14/07 checkpoint gộp:** MB RF@COND · MT wplur_rf2_ml · MN ai_plurality2 · MN BT nguồn số · lane model mới · thinking trước/sau mốc · kimi form 14d + late-fill design · gemma-4-31b · gate Google · glm-5.1 vs 5.2 · prompt v2 vs v1 · đề-xuất-xóa.

**GitHub bản gốc:** `Lottery_AI_Notion_Reports/V10781_GD2_EXECUTION_20260705_PUBLIC_SAFE/BAO_CAO_CHI_TIET_V10781.md`
