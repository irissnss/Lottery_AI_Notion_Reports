# V10818 — Prompt gốc + "lệch ±1" + "đảo pha 34-43": mổ prompt, đo lịch sử, sandbox PHASE-OFF (17/07/2026, 20:59→22:2x)

## 0. Câu hỏi owner (20:59)
- Prompt gốc trong dự án là gì để các model AI đọc và suy luận?
- "Có vẻ model suy luận luôn lệch ±1 so với số trúng từng miền (MB hôm nay dự đoán 34 → trúng 35, dự đoán 75 → trúng 85). Nếu bỏ ±1 thì lịch sử live có khả quan hơn không?"
- "Các yếu tố đảo pha lược bỏ, chỉ để model tập trung soi rules thì khả quan hơn không? MB hôm nay toàn dự đoán 34-43, nếu không có đảo pha thì số phụ không phải 43 mà là số tín hiệu tốt hơn thì sao? Nếu cần chạy thử sandbox."

## 1. Prompt gốc là gì — trả lời thẳng
- Model đọc: `SYSTEM_PROMPT` (~160 dòng, PB-18.0, trong `gpt_analyzer.py`) + context pack động mỗi ngày (MINED RULES per-số + CHỈ SỐ ĐỊNH LƯỢNG Python + Knowledge Base + thống kê 56 ngày + self-learning + CONVERGENCE TRAP ALERT). Không đọc file nào khác.
- **CÓ dạy pha thật, đúng nghi ngờ của anh:**
  - §3 Nhận diện PHA: "ĐẢO GƯƠNG (Mirror): nhiều cặp XY ↔ YX (VD 46 ↔ 64)" + "GIAO TRỤC (Cross): cụm dịch +1/-1".
  - Thang điểm strength: "Ảnh đối XY/YX đều có dấu: 0-2đ".
  - Few-shot Example dạy nguyên văn: "chốt 64 chính, 46 phụ (mirror + KB)".
  - ANTI-HERDING khi trap: "tìm SỐ THAY THẾ gần (±1, cùng family)".
  - JSON schema ép trường `phase` + `mirror_support` → model bị buộc "diễn" pha.
- Hệ quả nhìn thấy 17/07: gemini-2.5-pro, grok-4.3, qwen3-max-thinking **cùng ghép 34-43** cho MB — là DO PROMPT DẠY, không phải model tự bịa. Có sẵn công tắc `rule_mirror` / `rule_cross` để tắt.

## 2. "Lệch ±1" — đo 6.680 lần main trượt: ẢO GIÁC TẦN SUẤT
| Miền | main trượt, có hàng-xóm ±1 về | null (số bất kỳ trượt) | z |
|---|---|---|---|
| MN | 86.5% | 89.2% | **−3.78** |
| MT | 78.7% | 80.5% | −2.16 |
| MB | 65.7% | 67.1% | −1.50 |
- Lô 22-46 số phủ dày → hầu như số nào trượt cũng có "hàng xóm" về. Pick của model KHÔNG gần số trúng hơn số ngẫu nhiên (z âm cả 3 miền).
- Mirror-khi-main-trượt: chỉ MT hơi dương thật (38.1% vs null 34.4%, z=+3.55); MN âm; MB = null.
- **Kết luận: không tồn tại "model luôn lệch 1"; bỏ ±1 không cứu được các ngày đã trượt.** (17/07: 35✓ 85✓ nhưng 34✗ 75✗ 43✗ — đúng kiểu ngày tạo cảm giác đó.)

## 3. Nhưng CẶP PHỤ-BIẾN-THỂ là bias thật ở MB (90 ngày, phụ = mirror hoặc ±1-một-chữ-số của main)
| Miền | tỷ lệ ghép biến-thể | any-hit: biến-thể vs độc-lập | phụ-hit: biến-thể vs độc-lập |
|---|---|---|---|
| **MB** | 152/2253 = 6.7% | **33.6% vs 40.3% (−6.7pp)** | **17.8% vs 23.7% (−5.9pp)** |
| MN | 225/2360 = 9.5% | 69.3% vs 67.6% | 41.8% vs 44.0% (âm nhẹ) |
| MT | 189/2330 = 8.1% | 60.3% vs 56.8% | 38.1% vs 35.3% (NHỈNH hơn) |
- Model hay ghép: qwen3-coder 17.4%, gemini-2.5-pro 15.4%, qwen3-max-thinking 14.6%, claude-opus-cũ 14.5% (claude-opus-4-6 ~1%).
- Ý nghĩa: ghép 43 "cho có đôi" với 34 = vứt 1 slot tín hiệu thật — đúng miền MB anh phàn nàn.

## 4. Sandbox PHASE-OFF (owner cho phép) — 60 call as-of replay, 5 model tốt+tệ × 2 arm
- Arm B: tắt Đảo Gương + Giao Trục (`rule_mirror/rule_cross=0`) + addendum cấm số-phụ-biến-thể, bắt phụ có evidence độc lập.
- **Batch 1 — 17/07 (ngày bầy-trượt 34/63):** A any-hit 3/13, B **8/13**; B thoát herd rõ (MT: 78✓/80✓/77✓ thay vì cả bầy 63✗); cặp 34-43 biến mất.
- **Batch 2 — đối chứng 3 ngày bầy-THẮNG (MN@16/07 96✓, MT@12/07 64✓, MB@13/07 89✓):** A any 11/14 (main 5), B any 11/14 (main 3) — B không hại any nhưng **rời số bầy cả khi bầy đúng** (gemini/qwen bỏ 96 ở MN).
- **Cộng 2 batch: B any-hit 19/27 vs A 14/27 (+18pp) · main-hit 4 vs 6 (−7pp) · dính-herd 13 vs 19.**
- Đọc trung thực: tắt-pha giúp SỐ PHỤ đa dạng → any-hit tăng rõ, nhưng tắt hẳn làm main mất neo. **Đúng liều = chỉ CẤM PHỤ-BIẾN-THỂ (nhất là khi trap) + sửa gợi ý "±1 cùng family" → "số thay thế từ rule/thống kê độc lập". KHÔNG tắt hẳn PHA. MT giữ nguyên.**

## 5. Đã deploy (§52 chain, 22:1x)
- View `variant_pairs` RECURRING trong `_v10803_chase_bias_shadow.py` (90d/miền + top model + cặp hôm nay, cache 4.32s→0.50s) + khối **🪞 CẶP BIẾN THỂ ±1/ĐẢO** trong panel 🏃 CHASE-BIAS `/monitoring` (refresh 60s).
- Verify: health 200 · admin 401 · hash 4 bảng PRE=POST IDENTICAL (10280/420/15094/10144) · journal sạch · gdb_swap V10816-17 vẫn sống.
- Không đụng official/prompt production. Backup: `backups/v10818_pre/` + VPS `backups/v10818_vps/`.
- **Ngưỡng: CP-S3 23/07** (cùng phiên shadow A/B V10809): MB phụ-biến-thể vẫn kém ≥5pp → trình owner addendum 2 dòng; owner OK → sandbox lại 1 vòng rồi mới vào production.

## 6. Artifacts
`_v10818_mirror_probe.py`, `_v10818_phase_off_sandbox.py`, `_v10818_phase_off_batch2.py`, `_v10818_fetch_ab2.py`, `_v10818_deploy.py`; kết quả sandbox: VPS `/tmp/v10818_ab_results.json`, `/tmp/v10818_ab2_results.json`; FU: `FU-V10818-VARIANT-PAIR` (WAIT_LIVE).
