# V10784 — Cứu eval + Freeze whitelist + Reasoning capture + Method lock UI (05/07/2026)

> Notion page: `3941d385-9bf8-81b6-8cd3-e9d6c42504c9` — tạo 21:09 05/07 (phiên V10785) dưới trang canonical Lottery_AI_Test.

**Kết quả chính (10 dòng):**
1. CỨU EVAL: MT shadow mất do restart 16:38 giết trigger (KHÔNG phải freeze) — backfill chuẩn 10 rows late=0; whitelist freeze deploy 17:06: freeze CHỈ chặn official surface, shadow/test/eval đi qua tự do (smoke 3/3 PASS).
2. XÁC NHẬN SỐNG ngày đầu: model_daily_eval 20:20 tối nay ghi 74 rows đủ 3 miền (MB 24 · MN 25 · MT 25).
3. FREEZE LIVE: T-10 MT fired 16:45:03 (BT=49 v2) + MB 17:45:00; bundle đứng yên sau mốc :55; 0 official write late.
4. REASONING CAPTURE 3 route (OpenRouter/DeepSeek/Gemini) + cột predictions.reasoning_tokens; smoke 3/3 PASS; live: grok 78,346 · reasoner 8,988 · gpt-5.5 8,804.
5. METHOD LOCK UI /choi + audit hồi tố (0 đổi method trong ngày; 2 phát hiện 04/07 = artifact ngày sinh bảng — trung thực).
6. GEMINI-3.5-FLASH lane shadow đăng ký (first_run 06/07) + FIRST-RUN GATE toàn hệ (active 05/07=8, 06/07=11).
7. P4: pagination server-side + 2 ma trận chờ ký (P42 độc lập miền/thứ · P44 trùng lặp) + cycle scan 1,614 cells shadow.

**Chờ anh ký (K1–K6):** loại 3 rows qwen3.7-max/glm-5.2 chạy sớm 05/07 khỏi so găng · ĐX-1/2/3 per-miền · S1–S5 dọn trùng lặp · cycle scan sau 14/07.

**Đính chính từ forensic V10785:** P2.1 "lock UI hoàn tất hiển thị" sớm 1 ngày — lockLine + decision ref đầy đủ chỉ hiện từ 00:00 06/07 (board hôm nay còn tuần 29/06). Code đã live đúng.

**Bằng chứng đầy đủ (GitHub-first §52G):**
https://github.com/irissnss/Lottery_AI_Notion_Reports/tree/main/V10784_EXECUTION_CONTRACT_20260705_PUBLIC_SAFE
(BAO_CAO_TONG + 2 partial + P42 + P44 + conversation context)

Private code: Lottery_AI_Test commits 58eb3fc · bd574f7 · d31b683. Rollback: /root/backups/v10784_pre + v10784_p1_pre.
