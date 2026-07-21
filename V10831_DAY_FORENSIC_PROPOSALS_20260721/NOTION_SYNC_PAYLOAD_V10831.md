# V10831 — Forensic trọn ngày 21/07 + gói đề xuất cải tiến (owner 19:37)

**Loại:** Read-only forensic (sync `artifacts/live_sync/20260721_193910`) + đề xuất chờ owner ký.  
**GitHub:** https://github.com/irissnss/Lottery_AI_Notion_Reports/tree/main/V10831_DAY_FORENSIC_PROPOSALS_20260721

## Ngày 21/07 thực tế không "tệ như cũ" đều 3 miền
- **MN THẮNG cả 3 luồng**: BT 04✓ (official + lane + /choi), model any 14/15.
- **MT**: official [42,89]✗ (42 ngoài rules, cụm ML); /choi 36✓; lane phụ 57✓.
- **MB**: official BT **50✗ = số herd** (về 3 miền hôm trước; writer official KHÔNG có anti-herd — 2 ngày liên tiếp đeo herd 26✗→50✗). **Lane 09✓ nhờ cắt herd.** /choi AE [48,57]✗ nhưng cả 2 có vote → **gate V10828 sống, hết khóa số 0-vote**.

## "Tín hiệu ngợp trời MB lọt lưới" = số VỀ nhưng 0-vote
Union 12 → VỀ 4: 09(6 vote)✓ lane bắt · 44/63 **0-vote** · 89(1v). AE cands VỀ (26/51) đều 0-vote → bị gate cắt đúng thiết kế. Đây là bài toán tầng B (điều kiện vote) đang đo forward — không phải bug mới.

## ML "tệ" — bệnh cụm-herd
MB: 7/8 model ML chạm 66 (66 trượt), any 1/8. MT dồn 42/24. LLM ngược lại hồi mạnh any 17/21 (81%). Guard-rail trial 4 ngày ~43% vs nền 35% = khỏe.

## Điều kiện V10829 — forward ngày 1
B-pick áp tay (union − herd, ưu tiên vote, tránh chase): **MN 04✓ · MT 57✓ · MB 09✓ = 3/3 BT** (1 ngày = nhiễu, KHÔNG promote; bản chính thức materialize 21:00, panel 📐).

## Đề xuất (chờ anh ký — không tự làm)
1. **P1 (mạnh nhất, an toàn): lane mới `TOTAL_V3_COND_V1`** — chơi B-best điều kiện, ghi số TRƯỚC giờ xổ, experiment riêng, tự chấm. Zero đụng official//choi/lane cũ.
2. **P2**: 28/07 quyết writer official → M2s (exhibit: official MB đeo herd 2 ngày liên tiếp).
3. **P3**: ML cụm-herd → agenda CP-L6 28/07 (ép feature rule-set cho ML).
4. **P4**: /choi MB tuần này = AE solo đang lạnh — đổi giữa tuần là owner-override, em trình số không tự đổi.
