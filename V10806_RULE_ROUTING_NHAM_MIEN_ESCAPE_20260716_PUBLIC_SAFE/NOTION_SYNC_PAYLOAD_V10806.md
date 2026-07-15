# V10806 — Ma trận routing + escape audit: "ngược ngạo" chỉ 1 chiều thật, ô sai chỗ = nguồn-MB→MT, không model nào thoát block

- Owner hỏi (23:35): tại sao 19 trúng MB / 51 trúng MN+MT ngược ngạo; 12W=92% có nhầm miền không; sao model khác "vượt qua được"; giữ nhãn + thêm điều kiện trỏ đúng miền được không.
- "Ngược ngạo" tách 2 chiều: THẬT = nguồn MN/MT → MB CÙNG TỐI (+5.5pp z=3.1; nguồn MT same-day +11.8pp z=3.6) — vụ 19 rơi đúng chiều này. ẢO = D+1 (vụ 51): mọi ô z<1.6, base-rate nổ MN∪MT ngày kế ≈63%.
- Nhãn 92%/75% tính ĐÚNG miền trong code (verify per-row). Rule Vũng Tàu→MT 2 chân đều dương — 15/07 chỉ là ngày xui (~32%).
- Thử re-route VT→MN: +25.6pp z=5.26 nhưng là MIRAGE VÒNG TRÒN (Vũng Tàu là đài MN, chân same-day trùng cơ học 100%) — ma trận gắn cờ circular, cấm promote nhầm.
- Ô SAI CHỖ THẬT: nguồn-MB → đích-MT lift ÂM (−2pp, raw z=−3) nhưng chiếm 23 rule active / 206 emissions 60d trong prompt MT → nguồn herd 39/61 ngày 15/07, kéo tín hiệu MT xuống. MB tự-lặp cũng âm (−2.5pp).
- Escape audit: AI 0/18 trúng 2 ngày, 17/17 pick TRONG block (kể cả claude-opus/kimi [39,61] — ghế khác cùng block); thoát thật = ML thuần không đọc prompt (4/7 + 5/7 trúng).
- Guard hoạt động khi được kích: 39@MN = CONV×4 → trap alert nổ → 0/26 model MN pick 39 (trượt thật). 51 CONV×2 / 19 CONV×1 dưới ngưỡng ≥3 → không cảnh báo.
- Deploy: view `/api/admin/chase-bias` + panel "🧭 RULE ROUTING" /monitoring; smoke 200/401; hash 4 bảng pre=post IDENTICAL.
- Đề xuất CP-L6 19/07 (đúng hướng owner): (g) ROUTING GATE — giữ nhãn, in điều kiện ô-âm cho rule nguồn-MB→MT; (h) trap alert theo miền (MN hạ ngưỡng CONV×2, MB giữ ×3, MT cảnh báo tail nguồn-MB); (a′) nhãn per-tail giữ nguyên đề xuất.
- Chi tiết đầy đủ: GitHub `Lottery_AI_Notion_Reports/V10806_RULE_ROUTING_NHAM_MIEN_ESCAPE_20260716_PUBLIC_SAFE/BAO_CAO_V10806_MA_TRAN_ROUTING_NHAM_MIEN_ESCAPE_AUDIT.md`
