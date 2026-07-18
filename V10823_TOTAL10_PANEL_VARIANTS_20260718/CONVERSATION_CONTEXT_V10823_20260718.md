# CONVERSATION CONTEXT — V10823 (2026-07-18, phiên 22:00)

## Owner message (verbatim, 22:00)

> Đã backtesst verify kỹ chưa em? Sao số outra 93 là lose ah là trung thực đó hả ? có cách nào làm nổi bật hơn để dễ nhìn hơn không em? Có tìm ra phương pháp nào tối ưu tốt hơn không , đã thử hết các phương pháp các cách chưa ? đặt tên cho Chỗ này là total 10 ngày thay đổi lớn đi . chứ nằm lọt giữ khó xem quá .

## Bối cảnh liền trước

- V10821 (19:39): Total-V2 shadow live — backtest 165d M2s thắng bundle +5.7→+11.6pp BT.
- V10822 (21:00): lane `TOTAL_V2_RULES_V1` live (ghi số trước giờ xổ) + vá cron shadow 19:14→20:50.
- V10822b (21:44): backup hoàn chỉnh + rollback script + ngày-0 18/07 ghi vào lane: MN [31,38]✗ · MT [41,46] 46✓phụ · MB [93,86] 86✓phụ.
- Owner nhìn thấy panel hiển thị 93 ✗ (lose) và hỏi 4 ý: verify kỹ chưa / trung thực không / làm nổi bật / thử hết phương pháp chưa + lệnh đặt tên panel.

## Việc đã làm trong phiên

1. Verify trung thực bằng DB live: MB tails 18/07 (24 số) không chứa 93 → BT trượt thật, 86 về phụ; cả 3 miền khớp 100% những gì panel hiển thị. Nhắc kỳ vọng đúng: BT 30-48%/miền, giá trị ở chênh cộng dồn so bundle cũ.
2. Quét thêm 7 biến thể tổng hợp (`_v10823_variant_backtest.py`) cùng khung leak-safe 165 ngày: VA main-weight 1.0/0.6, VC phiếu×form-30d+rules, VD bonus đa-rule, VE dual-gate cov≥2, VF main-gate, VH hedge BT-rules/partner-thường, W3 bộ-3. Kết quả: không biến thể nào thắng M2s bền cả 2 cửa sổ vượt nhiễu (VC/VE ≤ +1.7pp); VH sập any MB; W3 tăng any nhưng 1.5× vốn. → GIỮ M2s; VC re-check sau 28/07.
3. Panel theo lệnh owner: đổi tên "🧮 TOTAL 10 NGÀY THAY ĐỔI LỚN", dời từ giữa trang lên vị trí #2 sau 🎯 BẢNG NÊN CHƠI (khối cũ xóa, id duy nhất, node --check pass), viền vàng 3px + glow; khối đầu SỐ CHƠI HÔM NAY chip to màu trung thực (xanh=VỀ đỏ=TRƯỢT xám=chờ, nhãn BT/phụ); lịch sử lane chip ✓/✗ từng số; backend `_lane_view` thêm field `marks`.
4. Deploy `_v10823_deploy.py`: backup 2 đầu → sha khớp → compile → restart 22:1x (ngoài giờ job học) → health 200/admin 401/journal sạch → view marks đúng → hash 4 bảng IDENTICAL.
5. Governance: CHANGELOG V10823, SSOT, FU-V10823-TOTAL10-PANEL, STATE seq 284, HISTORY, PLAYBOOK (28/07 + VC re-check), SO_TAY 1.2/1.3, Notion + 2 push.

## Trạng thái sau phiên

- Panel "TOTAL 10 NGÀY THAY ĐỔI LỚN" ở vị trí #2, chip số chơi rõ ràng; phương pháp M2s không đổi.
- 19/07: 3 rows lane forward đầu tiên (MN 15:47 · MT 16:56 · MB 17:56) hiện thẳng vào khối SỐ CHƠI HÔM NAY.
- 28/07: chốt M2s vs M0 + re-check biến thể VC bằng dữ liệu forward.
