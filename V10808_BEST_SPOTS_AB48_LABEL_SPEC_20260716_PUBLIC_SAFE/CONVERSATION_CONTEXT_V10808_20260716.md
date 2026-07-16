# CONVERSATION CONTEXT — V10808 (16/07/2026, 08:44 → 09:5x)

## Verbatim owner (nguyên văn)

> Vậy đề xuất tốt nhất hiện tại là gì? nhớ là các chỗ đang khai thác cần ghi nhận và có thể đào bới thêm để tìm ra được chỗ tốt nhất nha em. Hiện sandbox em chạy bao nhiu ngày với 3 miền và 5 model em. Có nên thay thế nhãn nội dung prompt như thế nào em? cần cụ thể rõ ràng hơn chứ anh thật sự khó hiểu quá

> tiếp đi em gián đoạn nữa em (09:39 — sau khi phiên bị ngắt giữa chừng)

## Bối cảnh

- Nối tiếp V10807 (sandbox A/B 30 call trên 3 ngày bẫy — đã chứng minh addendum tác động thật, model yếu hưởng lợi nhất, 2 tác dụng phụ SE1/SE2).
- Owner hỏi 3 câu: đề xuất tốt nhất, sandbox bao nhiêu ngày (ngầm ý: chưa đủ dày), nhãn đổi cụ thể thế nào.

## Việc đã làm trong phiên

1. Trả lời thật: V10807 chỉ 1 ngày/miền → chạy thêm `_v10808_ab_extended.py`: 4 ngày thường 10-13/07 × 3 miền × 2 model rẻ × 2 arm = 48 call (fix leakage per-số dùng data < ngày case). Kết quả: A 67% → B 75%, không miền nào bị phá; gộp 7 ngày 2 model rẻ: 57% → 73% (+16pp, p≈0.11).
2. Đào bới `_v10808_best_spots.py`: per-số đài×giải×đích×offset full-history n≥40 → 12 ô dương z≥2 (đều đang khai thác, 6/12 tier lệch thấp) + 1 ô âm (Quảng Ninh G6+G7→MT −8.4pp vẫn active). Phát hiện Hải Phòng G6→MT dương thật trong ô âm → gate phải là Ô-nền + ngoại lệ per-rule.
3. Ghi nhận cố định: bảng ⛏ BEST SPOTS thêm vào view `/api/admin/chase-bias` + panel 🏃 /monitoring, deploy VPS (smoke 200/401/401, hash 4 bảng IDENTICAL, backup v10808_pre).
4. Viết `LABEL_SPEC_TRUOC_SAU_CP_L6.md`: nguyên văn prompt MT 15/07 TRƯỚC và SAU (giữ dòng 12W + thêm dòng ↳ per-số | ô ✔/⛔ | tối đa 1 vị trí + header nghĩa % + footer ≥1 vị trí nội-miền + quy tắc gán ✔/⛔ 4 dòng).
5. Governance V10808: CHANGELOG, SSOT, FU-V10808-BEST-SPOTS (mới) + cập nhật FU-V10807, PLAYBOOK lịch verify (17/07 bảng ⛏ + ~14/08 đọc lại), AUTOMATION_STATE seq 269, commits 2 repo, Notion.

## Trạng thái chờ

- CP-L6 19/07: owner ký gói 5 mục (nhãn ↳; demote QN G6+G7→MT; align tier; MN CONV×2; hoãn thay API 2 model rẻ) → shadow 7 ngày → owner quyết bật official.
