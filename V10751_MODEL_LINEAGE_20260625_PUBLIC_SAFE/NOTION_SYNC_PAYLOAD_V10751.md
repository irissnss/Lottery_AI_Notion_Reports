# V10751 — Model Lineage: nối lịch sử khi đổi model-id (vá Opus mis-weight)

**Thời gian:** 2026-06-25T23:05:00+07:00
**Owner:** duyệt 100% P1 + yêu cầu cơ chế thay model rõ ràng (opus 4.6 lỗi thời → giữ API set 4.7, chỉ số liền mạch có mốc).

## Vấn đề (đào từ câu hỏi "Opus sao ít chạy")
- Opus chạy MỖI NGÀY; nhưng đổi id 16/06 (V10729: claude-opus-4-20250514 EOL → claude-opus-4-6).
- Alias cũ chỉ route API, KHÔNG áp vào đọc WR/BT → lịch sử đứt → Opus (mạnh, MN 47.7%) bị tính trọng số/gate trên 9 mẫu thay vì track record đầy đủ → trọng số official lệch.

## Fix
- database.py: MODEL_LINEAGE (id cũ→mới, chain-safe) + canonical_model_id(); áp get_model_win_rates (gộp theo canonical) + get_model_bt_rates (map mỗi row).
- Verify: opus-4-6 total 9→31 (gộp đủ 30d), id cũ nối vào, BT MN 35.5/MT 32.3/MB 22.6. health200, 4 bảng official IDENTICAL pre/post. Backup backups/v10751_remote_pre/.

## Cơ chế swap model tương lai (owner ask)
opus 4.6→4.7: (1) registry đổi id ACTIVE; (2) gpt_analyzer route API; (3) MODEL_LINEAGE thêm 'claude-opus-4-6':'claude-opus-4-7' → chỉ số liền mạch, có mốc rõ ràng.

## Chờ owner duyệt thiết kế
- P2: bộ lọc per-miền ĐỘNG (BT + cứu, top-K, tự điều chỉnh, không blocklist tĩnh).
- P3: gộp gpt-oss-120b (free) vào official + thứ-tự-chạy AI ưu tiên theo miền để kịp giờ (no-token luôn chạy trước sau khi cào same-day).
