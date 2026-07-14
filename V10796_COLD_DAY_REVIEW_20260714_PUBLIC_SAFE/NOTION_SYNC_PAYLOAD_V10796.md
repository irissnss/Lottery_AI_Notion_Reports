# V10796 — Mổ ngày lạnh 14/07 + verify fix combo-lock PASS + lệch pool-giờ MT (14/07 tối, READ-ONLY)

Owner 18:48: "MB nay tín hiệu tệ thật sự, MN full tín hiệu mà output không khá được, MT trung bình trật luôn — có gì cần xử lý không em?"

**Kết quả chính:**
- Ngày 14/07 KHÔNG bất thường: cả-3-miền-trượt-BT = 24% ngày lịch sử (kỳ vọng độc lập ~35%); journal sạch, health 200.
- MN: bể nóng 10/15, vote gốc 04✓ bị override V10640 đổi → 12✗ — NHƯNG forward từ 26/06 override vẫn +2 ngày net → 1 ngày đau, không gãy cấu trúc, KHÔNG sửa.
- MT: PHÁT HIỆN CẤU TRÚC — official sinh 16:38 với 13-15 model, lane 17:10 đủ 26 model → K15-era lệch 3/5 ngày = CHẠM ngưỡng báo; 60d lane 36% vs official 28% (+8pp official chưa hưởng trọn).
- MB: bầy-chụm 51×12 phiếu trượt cả cụm; đo 120d: modal-share cao KHÔNG tăng hit (22/20/18%) → không chế guard bầy. AE mặt kia vẫn ăn (46✓ MB, 62✓ MT) — seesaw đúng thiết kế.
- Verify fix combo-lock V10794 (hạn tối nay): PASS — lock MB 17:58:21 đủ 2 leg V0. FU-V10794 ĐÓNG.
- Nhịp: K11a chốt 16/07 (chênh chỉ 1 ngày đúp); K15 chốt 17/07 (challenger ≥ champion); selector 23/07; /choi tuần −2.4M/2 ngày.

**Chờ owner quyết:**
1. P1: dời giờ bundle official MT → ~17:05, MB → ~17:56 (pool-đầy, hết lệch) — đổi lại official ra muộn hơn.
2. CP-L6 QUÁ HẠN 14/07: (a) dời 19/07 (khuyến nghị) / (b) làm ngay / (c) huỷ.
3. Key rotation: chờ cấp 13 key mới theo inventory.

**Chi tiết đầy đủ:** GitHub `Lottery_AI_Notion_Reports/V10796_COLD_DAY_REVIEW_20260714_PUBLIC_SAFE/BAO_CAO_V10796.md`
