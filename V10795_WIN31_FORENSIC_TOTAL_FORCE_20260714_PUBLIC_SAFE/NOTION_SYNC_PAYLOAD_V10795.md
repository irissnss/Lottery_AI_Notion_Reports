# V10795 — "Con 31 từ đâu ra" + tổng lực 3 miền × 3 luồng + backtest combo 89-31 (14/07, READ-ONLY)

**Con 31 (owner win 13/07 MB): KHÔNG phải may mắn.** Echo cầu chéo cùng ngày: 17:30 MT xổ BT official MT 31 TRẬT → 17:35 AE MB bắt lại (flow `cross_region_sameday`, +5.5pp/90d, trace đầy đủ) → 18:15 MB: 31 VỀ. Con 41 cùng họ (`per_model_lag1`, meta-learning trật hôm trước) — trượt. Đúng tín hiệu cross MT→MB +7pp của V10788; caption K12 /choi hiển thị cơ chế từng ngày.

**Quy luật tới mức nào (90d):** MB cross_sameday 27% · per_model_lag1 28% (nền 24.8%) — lift thật nhưng khiêm tốn; MT 34-45%. /choi lãi bền nhờ TỔNG HỢP flow + verdict guard + khóa tuần, không phải 1 quy luật đơn.

**"89-31 thì quá đẹp":** backtest 5 biến thể (39d MB, 64d MT, causal): V0 top1+top1 (= fix V10794 đã deploy sáng nay) ăn-ngày cao nhất 24/39, 2 nửa đều dương; V1 "89-31" nửa đầu −9.4M = hindsight 1 ngày; MT V0 +75.6M đè V1/V2. **GIỮ V0 — không đổi code.**

**Tổng lực 30d:** /choi +68.1M (MT +45.2 · MB +14.5 · MN +8.4) · lane MB AE +57.5M mạnh nhất hệ · official MT +30.3M, MB BT 13% mắt xích yếu (K11a đang trị, chốt 16/07). MN tuần lạnh: guard E5 né đúng, chỉ −1.2M.

**Bài học:** tách vai chạy đúng (13/07 MB cả official 89✓ lẫn /choi 31✓); chuẩn mới: đổi cặp /choi phải backtest ≥39 ngày 2-nửa-dương.

**Nhắc:** 14/07 tối verify combo lock · 16/07 K11a d7 · 17/07 K15 d7 · 23/07 selector 14d · CP-L6 chờ anh quyết (đề xuất dời 19/07).

**Chi tiết:** GitHub `Lottery_AI_Notion_Reports/V10795_WIN31_FORENSIC_TOTAL_FORCE_20260714_PUBLIC_SAFE/BAO_CAO_V10795.md`
