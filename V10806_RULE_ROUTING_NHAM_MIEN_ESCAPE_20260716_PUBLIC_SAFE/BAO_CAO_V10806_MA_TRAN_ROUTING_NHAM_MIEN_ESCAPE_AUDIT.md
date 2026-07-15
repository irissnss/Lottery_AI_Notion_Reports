# V10806 — MA TRẬN ROUTING + ESCAPE AUDIT: TRẢ LỜI 3 CÂU HỎI "NGƯỢC NGẠO / NHẦM MIỀN / MODEL NÀO VƯỢT QUA"

**Thời điểm:** 2026-07-15 23:35 → 2026-07-16 ~00h (giờ VN) · **Trạng thái:** DEPLOYED (panel đo) + AWAITING_OWNER (đề xuất prompt CP-L6 19/07)
**Input pháp lý:** DB + trace sync từ VPS trước khi đo — manifest `artifacts/live_sync/20260716_000004/manifest.json`

## 0. Câu hỏi owner (nguyên văn 23:35)

> "anh hiểu rồi vậy em có đặt câu hỏi lại tại sao ? với prompt đó mà 19 lại trung Miền Bắc và 51 lại trúng miền MT và MN mà lại output ngược ngạo vậy làm cho trật chồng chéo vậy không? rõ ràng còn số 12W=92% nó cũng có lý được rules phân tích học tập và xếp hạng nhưng có lẻ có nhầm lẫn miền thì sao em? rồi tại sao cũng prompt đó mà model Ai khác lại output ra số ổn hơn vượt qua được hoặc hiểu được con số đó nó không nằm trong đề xuất hôm nay ? em phải giải thích được các vấn đề đó đã rồi hãy đề xuất sửa nhãn, có khi giữ nguyên chỉ thêm điều kiện nào khác để nó trỏ đúng miền thì sao? Xem lại dùm anh 1 lần nữa nhé"

## 1. Câu 1 — "Ngược ngạo": tách 2 chiều, chỉ 1 chiều THẬT

Ma trận routing 120 ngày: mọi tail do rules emit, gom theo (miền nguồn, offset dữ liệu), chấm cả 3 miền cùng ngày (D) và hôm sau (D+1), khử trùng lặp theo (ngày, tail). Lift = hit% − baseline miền chấm; z = binomial.

| Nguồn/offset | chấm MN@D | chấm MT@D | chấm MB@D | MN@D+1 | MT@D+1 | MB@D+1 |
|---|---|---|---|---|---|---|
| MB/D-1 (n≈1150/ô) | +1.8pp z1.2 | **−2.0pp z−1.4 (raw z−3.0)** | −2.5pp z−2.0 (tự-lặp) | +2.5pp z... | −3.0pp | +0.3pp |
| MN/D (same-day) | VÒNG TRÒN | +9.7pp z3.0 | +5.6pp z1.7 | −4.7pp | +5.2pp z1.6 | +2.3pp |
| MN/D-1 (n≈580-750/ô) | −0.6pp (tự-lặp) | +3.5pp z1.8 | **+5.5pp z3.1** | +1.2pp | −1.0pp | +2.0pp |
| MT/D (same-day) | −9.9pp | VÒNG TRÒN | **+11.8pp z3.6** | +0.9pp | +2.0pp | −2.1pp |
| MT/D-1 | +5.3pp z2.3 | +3.2pp (tự-lặp) | +4.7pp z2.2 | +6.3pp z2.8 | +1.8pp | −1.0pp |

- **Chiều THẬT — nguồn MN/MT → MB CÙNG TỐI:** +5.5pp (z=3.1) và +11.8pp (z=3.6). Causal sạch: MN quay 16:1x-16:3x, MT 17:1x-17:3x, đều TRƯỚC MB 18:15. **Vụ 19 rơi đúng chiều này:** 19 = GĐB Vũng Tàu 14/07 → rule emit cho MT 15/07 → trượt MT → nổ ĐB MB cùng tối (khớp pattern H3b đã đo V10804, p≈0.013).
- **Chiều ẢO — MB trượt → MN/MT NGÀY SAU (vụ 51):** toàn bộ cột D+1 không ô nào z≥2. Số 51 emit cho MB 14/07 trượt cả 3 miền ngày 14, nổ MN+MT ngày 15 — nhưng 1 số bất kỳ nổ MN-hoặc-MT ngày kế ≈ 63% theo xác suất nền (union 43%+35%). Cảm giác "nó chạy qua bên kia" là ảo giác tần suất — thống nhất với null test V10803/V10804 (p=0.70).
- Cảm giác "MT tín hiệu giảm mạnh" có số đo: block rule MT 15/07 chỉ trúng 2/14 tails (kỳ vọng ngẫu nhiên 4.1). Block MB 14/07 trúng 4/11 (kỳ vọng 2.8) — block không tệ, nhưng cả 17 AI dồn vào 3 tail "nóng nhất nhãn" (51/32/36) và cả 3 đều trượt.

## 2. Câu 2 — "12W=92% có nhầm lẫn miền?": phép tính KHÔNG nhầm, nhưng CÓ Ô SAI CHỖ THẬT (ngược hướng nghi vấn)

1. **Verify per-row:** nhãn 92% (Đồng Tháp G5+G7→MB lúc 14/07) và 75% (Vũng Tàu GĐB+G1→MT) đều được chấm ĐÚNG miền đích, ĐÚNG ngày trong `mined_rule_effectiveness` (11/12, 9/12 hit_any). Miner cũng đã có sibling rule cho từng miền (Đồng Tháp G1+G2→MN 92%; Vũng Tàu 3 rule→MB, 3 rule GĐB+*→MT) — không thiếu biến thể miền, không nhầm trong code.
2. **Rule Vũng Tàu GĐB+G1→MT không "trỏ nhầm miền":** rule chạy 2 chân — thứ Ba emit số Vũng Tàu CÙNG NGÀY (VT quay 16:16, trước MT 17:15 → hợp lệ), thứ Tư emit số D-1. Cả 2 chân đều dương: per-tail 45.7% vs base 30.4% (T3) và 42.9% vs 30.0% (T4). Ngày 15/07 là chân T4; hai tail [19,61] cùng trượt MT có xác suất ~32% theo rate lịch sử — một ngày xui bình thường của một rule tốt.
3. **Thử re-route theo ý "trỏ sang MN": phát hiện MIRAGE VÒNG TRÒN.** Chấm rule VT vs MN cho 66.7% (+25.6pp, z=5.26) — nghe như "rule này thuộc về MN". Nhưng bóc từng emission: toàn bộ phần thắng nằm ở chân T3 same-day, mà **Vũng Tàu LÀ đài MN** — số của nó đương nhiên nằm trong kết quả MN cùng ngày (trùng cơ học 100%). Ma trận đã gắn cờ `circular` cho 2 ô này để không bao giờ promote nhầm.
4. **Ô SAI CHỖ THẬT: nguồn-MB → đích-MT.** Lift lịch sử ÂM (−2.0pp dedup; raw z=−3.0 trên n=5035; out-of-selection −2.7pp) nhưng đây là CỤM RULE ĐÔNG NHẤT của prompt MT: **23 rule active, 206 emissions/60 ngày** (Hà Nội/Quảng Ninh dump 4-7 tails mỗi rule). Ngày 15/07 chính cụm này bơm 39 vào block MT (Quảng Ninh G6+G7 + GĐB+G7) → herd [39,61]. MB tự-lặp (nguồn-MB→MB) cũng âm (−2.5pp, z=−2.0, 9 rule active). Đây mới là chỗ "nhầm miền" cần điều kiện — không phải rule Vũng Tàu.

## 3. Câu 3 — "Model khác vượt qua được?": KHÔNG ai vượt qua cả

| Ngày | AI trong block | AI ngoài block | AI trúng | ML thuần trúng |
|---|---|---|---|---|
| 14/07 MB (block 11 tails) | 17/17 | 0 (2 model "trắng" = FAIL không output) | **0/17** | **4/7** (57, 54, 02, 98...) |
| 15/07 MT (block 14 tails) | 17/18 | 1 (gpt-oss [98,48] — cũng trượt) | **0/18** | **5/7** (21, 22, 42) |

- Các model "trông ổn hơn" (claude-opus, kimi, gemini-3.5-flash, qwen [39,61]) thực ra chỉ **ngồi ghế khác trong cùng block** — 39 là tail Quảng Ninh (nguồn-MB, ô âm), 61 là tail Vũng Tàu. Không model nào "hiểu số đó không nằm trong đề xuất hôm nay".
- Kẻ thoát thật là **ML thuần — vì không đọc prompt** (mù block), không phải vì thông minh hơn.
- **Guard hiện có HOẠT ĐỘNG khi được kích:** 39 tại MN 15/07 là CONV×4 → prompt MN in cảnh báo "🚨 CONVERGENCE TRAP ALERT" (ngưỡng CONV≥3, `gpt_analyzer.py` L4726) → **0/26 model MN chọn 39**, và 39 trượt MN thật. Trong khi đó 51 chỉ CONV×2, 19 chỉ CONV×1 → DƯỚI ngưỡng → không ai được cảnh báo. Vấn đề không phải model kém — là **alert chưa phủ vùng CONV thấp** và chưa phân biệt miền.

## 4. Đã deploy phiên này (đo lường, zero regime change)

- View `/api/admin/chase-bias` thêm khối `rule_routing` (5 hàng nguồn/offset × 6 ô miền@D/D+1, dedup, lift+z, cờ circular) — file `web/backend/_v10803_chase_bias_shadow.py`.
- Panel /monitoring (chase-bias) thêm bảng **"🧭 RULE ROUTING"** — xanh z≥2, đỏ z≤−2, ô vòng tròn ghi rõ. Cùng endpoint + auto-refresh 60s sẵn có.
- Deploy `_v10806_deploy.py`: backup remote+local → upload 2 file → compile OK → restart `lottery.service` → smoke health=200 / admin=401 → view check 5 hàng → journal sạch → **hash 4 bảng official pre=post IDENTICAL** (predictions 10122/3a18c24b · final_bundles 414/0e68ae9c · lottery_results 15081/1a1820b1 · model_daily_eval 9986/aaa91dc6).

## 5. Đề xuất CP-L6 (19/07) — CẬP NHật theo hướng owner "giữ nguyên nhãn, thêm điều kiện trỏ đúng miền"

- **(g) ROUTING GATE per-ô [mới, ưu tiên cao nhất]:** rule nguồn-MB nhắm MT GIỮ NGUYÊN nhãn, nhưng in kèm 1 dòng điều kiện: "⚠ Ô nguồn-MB→MT lift lịch sử −2pp (z=−3): CHỈ THAM KHẢO, không dùng làm BT chính" — hoặc demote hẳn khỏi prompt MT (owner chọn mức). Tương tự ô MB tự-lặp. Chiều MN/MT→MB cùng-ngày (+5~12pp) đã có rule khai thác, không mở rộng khi chưa qua shadow.
- **(h) TRAP ALERT theo miền [mới]:** MN hạ ngưỡng alert xuống CONV×2 (data V10805: MN CONV×2 hit 38.8% < base 42.9% = bẫy thật); MB giữ ngưỡng ×3 (MB CONV×2 50.6% đang ăn); MT thêm cảnh báo khi tail đến từ rule nguồn-MB (ô âm).
- **(a′)** nhãn per-tail %+n vẫn giữ (semantic hit_ANY là gốc herd — V10805); (b)-(f) V10805 giữ nguyên.
- Tất cả là thay đổi prompt production → chờ owner ký tại CP-L6, không tự đổi trong phiên.

## 6. Bằng chứng / lineage

- Probes read-only: `_v10806_region_routing.py`, `_v10806_verify_and_escape.py`, `_v10806_clean_routing.py`, `_v10806_leak_and_block.py`, `_v10806_dedup_bias.py`, `_v10806_vt_check.py` (repo private `Lottery_AI_Test`).
- Governance: CHANGELOG V10806 · SSOT block V10806 · FU-V10806-RULE-ROUTING · AUTOMATION_STATE seq=267 · PLAYBOOK §5 (+2 mốc verify 16/07 & ~14/08).
- Rollback: `cp /root/backups/v10806_pre/*` + restart `lottery.service`.
