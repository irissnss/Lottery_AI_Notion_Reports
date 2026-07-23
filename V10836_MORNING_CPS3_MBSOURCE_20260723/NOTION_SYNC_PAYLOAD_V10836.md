# V10836 — Đầu ngày 23/07 + CP-S3 đóng addendum + trả lời "rules MN/MT lấy nguồn MB G1/GĐB"

**GitHub:** https://github.com/irissnss/Lottery_AI_Notion_Reports/tree/main/V10836_MORNING_CPS3_MBSOURCE_20260723

## Đầu ngày (sync 20260723_111630)
- MN sáng 15+12 (0 rỗng) · bundle 07 [07,12] · /choi MN [07]. Journal sạch.
- **Verify V10833 SỐNG:** V67 đêm qua ghi trace target 23/07 (MB [97,02] · MT [51,60,96,97]) — hết `[None,None]`.
- Panel 📐 ngày 2: **MN B [21,45] BT✓ 2 ngày liên tiếp**; MT trống trung thực; MB 33✗. M2s 22/07: 2/3.
- Guard-rail trial 5 ngày: LLM any **66.7% vs nền 55.4% (+11.3pp)** — trial đang thắng.

## CP-S3 (đến hạn hôm nay) — ĐÓNG addendum per-số
105/105 cặp: **B 48.6% vs A 59.0% (−10.4pp)**; đoạn cùng nền PB-18.1 (18–22/07): **B −16pp**; cặp phân định A thắng 22 · B 11 (khớp scorer nội bộ 51-62). → Không promote; cron tự no-op từ hôm nay, gỡ hẳn 26/07.

## Câu owner: "rules đích MN/MT thường lấy nguồn MB G1 + GĐB, 30 ngày liên tục?"
**ĐÚNG tuyệt đối:** đích MN **25/35 rules** nguồn MB (15 GĐB/G1), đích MT **27/39** (16 GĐB/G1); emit **30/30 ngày**, chiếm **~65–67% union** mỗi ngày.

**Hiệu quả 30 ngày:** MB-GĐB/G1 → MN precision 44.2% (**+1.1pp** vs nền), → MT 36.6% (**+1.5pp**) = dương nhẹ, sát nền (lộ thô ≠ edge). MB-G6/G7 → MT **−5.3pp**. Ngược lại nhóm hiếm fire lift cao: MN←MN +19.8pp · MN←MT +26.2pp · MT←MN +14.9pp (n nhỏ 9–14 ngày). Tier không giải thích chênh lệch.

**Insight (không vá giữa cửa sổ):** miner nghiêng nguồn MB (KQ D−1 luôn sẵn, 1 đài/ngày) → chiếm 2/3 union nhưng lift mỏng, có thể crowd-out nguồn nội/chéo tốt. Backlog đã ghi: khi đọc ngưỡng điều kiện 04–11/08, thêm nhát cắt `source_region` (khung H-A2d có sẵn) trước khi trình wire.
