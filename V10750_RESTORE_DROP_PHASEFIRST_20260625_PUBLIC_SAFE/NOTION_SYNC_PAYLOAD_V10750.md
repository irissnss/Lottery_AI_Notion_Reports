# V10750 — Khôi phục 6 model (cắt vội) + Bỏ phase-first + Top-5 shadow per-miền

**Thời gian:** 2026-06-25T22:25:00+07:00
**Owner:** "cắt model hơi vội vàng thiếu bước" → yêu cầu bảng top-5 shadow TỪNG MIỀN trước, rồi mới vạch kế hoạch cắt + gộp official. Duyệt bỏ hẳn phase-first.

## A) Khôi phục 6 model (undo cắt vội V10748)
- Per-miền 90d cho thấy aggregate che mất giá trị per-miền: gpt-5.5 = shadow MẠNH NHẤT cả 3 miền (MT #1 38.6%, MB #1 32.8% vượt official tốt nhất 28.9%); deepseek-v4-flash MB #3; grok/deepseek-v4-pro/qwen-max/kimi đều top-8 + giá trị cứu thua per-miền.
- model_registry.py: 6 model REMOVED→SHADOW_AUTO. SHADOW 7→13. OUTPUT_ELIGIBLE 15 không đổi.

## B) Bỏ phase-first contract (owner-approved)
- gpt_analyzer.py: PHASE_FIRST_CONTRACT_MODELS=set() → không model nào còn bị append PHASE-FIRST JSON CONTRACT.
- Lý do (70 ngày): PHASE_FIRST 34.0% ≈ OFFICIAL 34.2% BT lô-hit (0 cải tiến) + phình input token + chậm request. Rollback: =set(SHADOW_GATE_MODELS).

## Bảng top-5 shadow per-miền (BT lô-hit 90d)
- MN: qwen3.6-plus 53.2 | gpt-oss-120b 52.3 | glm-5.1 50.0 | gpt-5.5 50.0 | opus-4-0514 48.1 (official tốt nhất combo-super 53.3)
- MT: gpt-5.5 38.6 | gpt-oss-120b 37.1 | glm-5.1 33.8 | opus-0514 33.8 | grok 33.3 (official tốt nhất combo-no-token 47.8)
- MB: gpt-5.5 32.8 (>official 28.9) | gemini-3.1-pro 26.0 | deepseek-v4-flash 25.9 | gpt-oss-120b 25.8 | grok 23.3 (official tốt nhất smart-ml 28.9)

## Verify deploy
- compile PASS, restart OK, health=200, shadow=13 live, phase-first rỗng live, 4 bảng official IDENTICAL pre/post (predictions 6cd53e1dedbe1a02, final_bundles 9779d624c5a52964, lottery_results 3812f94588de6d0f, model_daily_eval f7dd3711b9f5191c). 0 official impact. Backup backups/v10750_remote_pre/.

## Kế hoạch tiếp (chờ owner duyệt từng bước)
1. Gộp official (upside): đo unique-contribution gpt-oss-120b (FREE, mạnh cả 3 miền) → thêm vào 15 official voting nếu bổ sung tín hiệu. Cân nhắc gpt-5.5 cho MB.
2. Cắt deliberate: chỉ model bottom mọi miền + 0 cứu thua, sau đo kỹ. Tiết kiệm chính = bỏ phase-first (token), không cắt thô.
