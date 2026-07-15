# V10803 — Truy vết "số 51" + Chase-bias shadow 3 miền (15/07/2026 tối)

**Owner hỏi:** số 51 dự đoán hôm qua nổ rồi mà còn đề xuất cho MB — rối quá.

**Truy vết 51:** 13/07 nổ MN → 14/07 16 model đuổi 51 cho MB (BT official=51, TRƯỢT) → 15/07 51 nổ MN+MT. KHÔNG ai đề xuất 51 cho MB ngày 15/07 — đề xuất owner nhớ là của 14/07.

**Kết luận 1 — di cư là ẢO GIÁC:** "BT MB trượt → hôm sau nổ MN/MT" = 64% thật vs 64% null 2000 sim (p~0.52). MN∪MT ra ~63 đuôi/ngày nên 2/3 số bất kỳ sẽ "nổ đâu đó" hôm sau. Không có bug.

**Kết luận 2 — bias THẬT cần đo:** pool đuổi số vừa nổ hôm trước. MB 90d: BT-đuổi nổ 15% (10/67) vs không-đuổi 22% (5/23, nền 24%); lô2 20% vs 31%; 15/07 sống: đuổi 64×14 phiếu → trượt tiếp. MT cùng chiều âm; MN vô hại. Chưa đủ ý nghĩa → shadow forward.

**Triển khai (ZERO đụng official, hash 4 bảng IDENTICAL):** bảng `v10803_chase_bias_daily` (backfill 90d) + cron 19:10 + API `/api/admin/chase-bias` + panel 🏃 /monitoring 60s.

**Ngưỡng:** ≥30d forward + n≥30/nhánh: đuổi − không-đuổi ≤ −10pp bền 2 nửa → trình anti-chase tie-break; ≥0pp → đóng. Review ~16/08.

**Bối cảnh 30d:** BT official dưới nền bao-lô cả 3 miền (MN 37%/43%, MT 20%/35%, MB 13%/24%).

**Chi tiết đầy đủ:** GitHub `Lottery_AI_Notion_Reports/V10803_CHASE_BIAS_SHADOW_20260715_PUBLIC_SAFE/`
