# V10804 — Truy nguồn 51/19/92/17 + sandbox di cư + fix C16 budget MB (2026-07-15)

**Kết quả chính**
- Số 19: 12 model MT đuổi (19 vừa nổ MN 14/07) → trượt; KHÔNG ai dự cho MB mà ĐB MB = 19 → đúng pattern "MN/MT trượt → MB tối" (H3/H5).
- Số 92 (MB lô2 trúng): 5-6 model dùng tín hiệu D-1 thật (g8_tails ×2) — KHÔNG phải đuổi. Card phụ1 92 của lane DIR2 trúng nhưng method chỉ 26% lịch sử — chưa tin cậy.
- Số 17 (/choi MT trúng): MT_HYBRID_V1 đánh LẠI số vừa trượt hôm qua — khớp H1 (45.9% vs null 34.8%, p≈0.027), không phải may mắn thuần.
- Số 51: lane HYBRID/AE vẫn đuổi cho MB hôm nay (trượt). Sandbox H2 xác nhận lại: MB-trượt→MN/MT KHÔNG có edge (ảo giác tần suất).
- Sandbox di cư 8 giả thuyết, null hoán vị 4000 sim: mạnh nhất H3b "mọi pick MN+MT trượt → MB tối" 30.7% vs 24.3-24.9% (p≈0.013, 423 legs) — chưa vượt đa-so-sánh → chỉ SHADOW, panel "🔁 DI CƯ SỐ TRƯỢT" trong /monitoring, ngưỡng promote ≥+5pp & p<0.01 sau 30d.
- **BUG THẬT ĐÃ FIX**: C16 budget MB chết đói từ 04/06 (lane khác ghi bundle trước tick → nhánh budget không bao giờ chạy) = nguyên nhân TEST CHALLENGER "Chưa có dữ liệu". Fix budget_catchup trong scheduler; verify 16/07 ~17:40.
- Audit prompt 3 miền: fix header MT (5 nhãn → 3 đài, alias QB/QT); PHÁT HIỆN khối "CHỈ SỐ ĐỊNH LƯỢNG" dùng chung 129 đuôi 9 đài cả 3 miền → "ĐỀ XUẤT PYTHON: 96, 57" y hệt trong 3 prompt = nguồn herding xuyên miền → chờ owner ký CP-L6.
- Prompt V10768 pre/post: MT pool KHÔNG giảm (55.8→56.2%); official MT 13→29%, MB 7→14%, MN 40→29%; herd share tăng MT/MB. Ứng viên thay API đợt cắt: gemini-2.5-flash (29%), gpt-5-mini (36%); giữ opus-4-6 (86%), qwen3-max (73%), deepseek-pro-real (64%).

**An toàn**: hash 4 bảng official pre=post IDENTICAL; /du-doan, selector, T-chốt không đụng; rollback backups/v10804_pre.

**Quyết định chờ owner**: (1) CP-L6 — khối định lượng per-miền + danh sách cắt/thay API; (2) sau 30d — promote/huỷ H3b.

**Chi tiết đầy đủ**: GitHub `Lottery_AI_Notion_Reports/V10804_TRACE4_MIGRATION_C16FIX_20260715_PUBLIC_SAFE/`
