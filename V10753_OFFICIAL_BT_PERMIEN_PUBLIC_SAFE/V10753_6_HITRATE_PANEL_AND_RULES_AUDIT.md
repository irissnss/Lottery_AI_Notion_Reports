# V10753.6 — Panel % trúng lịch sử + AUDIT hệ thống RULES

**Thời điểm:** 2026-06-26T21:50:00+07:00 · **Owner:** duyệt thêm % kỳ vọng + hỏi audit rules (tích lũy/xếp hạng/đẩy prompt).

## A) Panel hit-rate (kỳ vọng thật)
Panel /du-doan giờ kèm "Lịch sử nhóm này trúng lô ~X% (KHÔNG thắng chắc mỗi ngày)":
- MN: NÊN CHƠI ~70% · CÂN NHẮC ~47%
- MT: NÊN CHƠI ~48% · SKIP ~12%
- MB: NÊN CHƠI ~31% · SKIP ~14%

**Backtest "theo gate" 119d:** chơi tất +139.3M → theo gate **+166.5M (+27.2M)**. Nhưng ngày NÊN CHƠI vẫn: MN 70% / MT 48% / MB 31% trúng → MT thua ~52% ngày, MB ~69% ngày kể cả "NÊN CHƠI" (hôm nay MT/MB trật = bình thường). Gate = né ngày tệ + gom lời dài hạn, KHÔNG thắng mỗi ngày.

## B) AUDIT hệ thống RULES
- **Xếp hạng / re-rank: CHẠY HẰNG NGÀY** ✅ — MB rule re-rank 20:30 + 04:45 + guard 17:00 (hôm nay "SUCCESS: 0 rules, T2=86"); bảng hiệu quả rule + sức mạnh theo thứ + phase-evidence đều cập nhật hôm nay. Rule yếu <45% bị loại khỏi prompt; theo tier T2/T3.
- **Đẩy vào prompt: CÓ** ✅ — mỗi prompt AI được inject rule đã mined + "RULE TAILS" + rulebook 13 mục dạy cách dùng (STRONG/MED/LIGHT, suppress<45%, prize-source, anti-trap, hội tụ).
- **Tích lũy rule MỚI: BÃO HÒA** ⚠️ — miner tuần có đăng ký (T2 00:30) nhưng rule mới latest 17/06 (9 ngày), re-rank "0 new rules" → kho rule ổn định, không đẻ thêm. Không phải lỗi nhưng đáng theo dõi nếu muốn rule tươi hơn.

**Kết luận:** cơ chế xếp-hạng + đẩy-prompt ĐANG CHẠY ĐÚNG hằng ngày, model AI được inject rule + dạy cách dùng. Chỉ khâu khai-thác rule MỚI là bão hòa.

Verify: diff main +26/-10, compile OK, health 200, /du-doan 200, 4 bảng official IDENTICAL.
