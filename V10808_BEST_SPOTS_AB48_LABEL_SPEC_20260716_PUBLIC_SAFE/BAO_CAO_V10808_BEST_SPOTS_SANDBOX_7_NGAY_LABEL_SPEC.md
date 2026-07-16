# V10808 — TRẢ LỜI 3 CÂU HỎI OWNER: ĐỀ XUẤT TỐT NHẤT / SANDBOX BAO NHIÊU NGÀY / NHÃN ĐỔI CỤ THỂ RA SAO

**Thời gian:** 2026-07-16 08:44 → 09:5x (giờ VN)
**Trigger (owner 08:44):** "Vậy đề xuất tốt nhất hiện tại là gì? nhớ là các chỗ đang khai thác cần ghi nhận và có thể đào bới thêm để tìm ra được chỗ tốt nhất. Hiện sandbox em chạy bao nhiêu ngày với 3 miền và 5 model? Có nên thay thế nhãn nội dung prompt như thế nào — cần cụ thể rõ ràng hơn chứ anh thật sự khó hiểu quá."

---

## 1. SANDBOX CHẠY BAO NHIÊU NGÀY? (trả lời thật)

| Đợt | Ngày-case | Model | Call | Mục đích |
|---|---|---|---|---|
| V10807 (đêm 16/07) | 3 ngày BẪY: MB@14/07, MT@15/07, MN@15/07 | 5 (2 kém + 2 mạnh + 1 trung) | 30 | Gate có gỡ được bẫy 51/19/39 không |
| V10808 (sáng 16/07) | 4 ngày THƯỜNG: 10-13/07 × 3 miền | 2 rẻ (gemini-flash, gpt-5-mini) | 48 | Gate có PHÁ ngày tốt không + fix leakage (per-số chỉ dùng data trước ngày case) |
| **Tổng** | **7 ngày-case × 3 miền = 21 case** | | **78 call, 0 lỗi, không ghi DB** | |

Ghi chú trung thực: opus/qwen (model mạnh, đắt) mới chạy 1 ngày/miền; 2 model rẻ đủ 7 ngày. Kết quả +16pp bên dưới là của 2 model rẻ trên 7 ngày — **chưa đạt ý nghĩa thống kê (p≈0.11)**, nên bước tiếp theo bắt buộc là shadow live 7 ngày chứ không bật thẳng official.

## 2. KẾT QUẢ A/B MỞ RỘNG (4 ngày thường — câu hỏi "gate có phá ngày tốt?")

| Phép đo | A (prompt gốc) | B (prompt vá) |
|---|---|---|
| any-hit 24 case | 16 (67%) | **18 (75%)** |
| trúng cả 2 số | 2 | **5** |
| theo miền | MN 5/8, MT 7/8, MB 4/8 | MN 6/8, MT 7/8, MB 5/8 — không miền nào tụt |
| theo model | gemini 8/12, gpt-5-mini 8/12 | gemini 8/12, gpt-5-mini **10/12** |
| đổi pick | — | 22/24 cặp; B thắng-mới 5, mất 3 |

**GỘP 7 ngày (2 model rẻ, 30 cặp A/B): 57% → 73% (+16pp); thắng-mới 8 / mất 3.** Main-hit giữ nguyên 37% — gate chủ yếu sửa VỊ TRÍ PHỤ, đúng nơi bẫy tập trung (V10807: phụ-là-trap 5/15→1/15).

## 3. ĐÀO BỚI "CHỖ ĐANG KHAI THÁC" → TÌM CHỖ TỐT NHẤT (per-số đài×giải×đích×offset, n≥40, full history)

Baseline per-số 120d: MN 43.0% / MT 35.2% / MB 23.8%.

### ⛏ 12 Ô DƯƠNG z≥2 (chỗ tốt nhất — TẤT CẢ đang được khai thác bởi rule active)

| Đài giải | Tuyến | Per-số | Lift | z | 120d | Thứ | Tier hiện tại |
|---|---|---|---|---|---|---|---|
| Ninh Thuận G1+G7 | MT→MB/D-1 | 47.7% (n=44) | **+23.9pp** | 3.73 | 53.1% | T7 | READY_STRONG |
| Phú Yên G5+G7 | MT→MN/D-1 | 66.7% (n=54) | +23.7pp | 3.51 | 70.6% | T3 | READY_WITH_CAUTION ← lệch |
| Bình Dương GĐB+G1 | MN→MT/D-1 | 57.5% (n=40) | +22.2pp | 2.95 | 58.8% | T7 | READY_STRONG |
| Trà Vinh G5+G7 | MN→MN/D-1 | 62.5% (n=40) | +19.5pp | 2.49 | 62.5% | T7 | READY_STRONG |
| Khánh Hòa G2+G5 | MT→MB/D-1 | 41.2% (n=51) | +17.4pp | 2.92 | 45.5% | T5 | READY_STRONG |
| Sóc Trăng GĐB+G7 | MN→MB/D-1 | 38.6% (n=44) | +14.9pp | 2.31 | 41.2% | T5 | READY_WITH_CAUTION ← lệch |
| Bình Dương G2+G7 | MN→MB/D-1 | 38.6% (n=44) | +14.9pp | 2.31 | 44.1% | T7 | READY_WITH_CAUTION ← lệch |
| Hải Phòng G6 | MB→MT/D-1 | 50.0% (n=50) | +14.8pp | 2.18 | 50.0% | T7 | READY_WITH_CAUTION ← lệch |
| Ninh Thuận G1+G8 | MT→MB/D-1 | 37.5% (n=40) | +13.7pp | 2.04 | 40.0% | T7 | READY_WITH_CAUTION ← lệch |
| Vũng Tàu G5+G7 | MN→MB/D-1 | 36.7% (n=49) | +13.0pp | 2.13 | 35.3% | T4 | LIMITED_WEIGHT ← lệch nặng |
| Khánh Hòa G1+G8 | MT→MN/D-1 | 56.0% (n=75) | +13.0pp | 2.28 | 60.0% | T2/T5 | LIMITED_WEIGHT ← lệch nặng |
| Hà Nội G1+G2 | MB→MB/D-1 | 35.2% (n=71) | +11.4pp | 2.26 | 34.0% | T6 | READY_STRONG |

### ⛔ Ô ÂM z≤−2 (hố phải tránh)

| Đài giải | Tuyến | Per-số | Lift | z | Tier |
|---|---|---|---|---|---|
| Quảng Ninh G6+G7 | MB→MT/D-1 | 26.9% (n=186) | **−8.4pp** | −2.39 | **VẪN ACTIVE (LIMITED_WEIGHT)** ← thủ phạm 39/61 ngày 15/07 |

### 2 phát hiện quan trọng làm SỬA LẠI đề xuất

1. **Cùng ô MB→MT có cả ÂM (Quảng Ninh) lẫn DƯƠNG thật (Hải Phòng G6 +14.8pp z=2.18)** → gate không được chặn mù cả ô; bản cuối = **Ô làm nền + NGOẠI LỆ per-rule** (rule per-số z≥2 giữ ✔ dù nằm ô âm).
2. **Tier miner đang lệch với giá trị thật:** 6/12 ô dương mạnh bị đè LIMITED_WEIGHT/CAUTION, trong khi ô âm QN vẫn active → đề xuất mới (i): **align tier theo per-số**.

Việc "ghi nhận cố định": bảng **⛏ BEST SPOTS** đã lên panel 🏃 /monitoring (cùng endpoint `/api/admin/chase-bias`, auto-refresh 60s) — tự tính lại mỗi lần xem, không phụ thuộc trí nhớ phiên chat.

## 4. NHÃN PROMPT ĐỔI THẾ NÀO — XEM `LABEL_SPEC_TRUOC_SAU_CP_L6.md` (cùng thư mục)

Tóm tắt 1 câu: **GIỮ nguyên dòng nhãn 12W/16W cũ, THÊM 1 dòng phụ `↳ per-số ~X% (n=Y) | ô ✔/⛔ | tối đa 1 vị trí` dưới mỗi rule + 1 câu header giải thích nghĩa % + 2 ràng buộc footer (mỗi rule 1 vị trí; ≥1 vị trí nội-miền).** File spec có ví dụ THẬT nguyên văn prompt MT 15/07 trước/sau để owner nhìn thấy đúng cái model sẽ đọc.

## 5. ĐỀ XUẤT TỐT NHẤT HIỆN TẠI (gói CP-L6 19/07 — xếp theo độ chắc chắn của bằng chứng)

| # | Việc | Bằng chứng | Rủi ro |
|---|---|---|---|
| 1 | Nhãn ↳ per-số + điều kiện ô + 2 ràng buộc (spec §4) | 78 call sandbox: +16pp (p≈0.11), không phá ngày tốt, gỡ trap phụ 5→1 | Thấp (thêm chữ, không xoá gì) — vẫn shadow 7 ngày trước |
| 2 | Loại/demote Quảng Ninh G6+G7→MT | n=186, −8.4pp z=−2.39, thủ phạm 39/61 | Rất thấp |
| 3 | (i) Align tier 12 ô dương (promote per-số cao) | bảng ⛏ full-history z≥2 | Thấp — chỉ đổi trọng số miner |
| 4 | MN trap alert CONV×2 | MN CONV×2 38.8% < base 42.9% | Thấp |
| 5 | Hoãn thay API gemini-flash/gpt-5-mini đến sau shadow | gpt-5-mini 8/12→10/12 với gate | Không tốn gì |

## 6. AN TOÀN & ARTIFACTS

- Prompt production CHƯA đổi một chữ nào; mọi thứ chờ owner ký CP-L6.
- Deploy phiên này chỉ là bảng đo ⛏ (read-only view): smoke 200/401/401, journal sạch, hash 4 bảng pre=post IDENTICAL (predictions 10162 — tăng tự nhiên do MN sáng 16/07 chạy lúc 04:16, trước phiên).
- Code private: `_v10808_ab_extended.py`, `_v10808_best_spots.py`, `_v10808_analyze.py`, `_v10808_deploy.py`…; dữ liệu `artifacts/v10807_ab/v10808_*.json`; evidence đầy đủ trong `EVIDENCE_AB48_BEST_SPOTS.md`.
