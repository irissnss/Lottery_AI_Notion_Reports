# V10756.1 / .2 — BẢNG CẦU LIÊN MIỀN + P&L TIMELINE FORENSIC (2026-06-28)

> SHADOW thuần, ZERO official impact. Hash-guard 4 bảng official IDENTICAL.

## A. HOTFIX (V10756.1) — panel chỉ hiện 1 số → đủ top 1-2-3
Bug: `today_view()` lặp trên cùng cursor SQLite mà hàm con query lồng → "đè" vòng lặp → chỉ trả rank #1. Fix `.fetchall()`. Verify: MN 03-76-86, MT chờ-16-chờ, MB 74-66-76.

## B. V10756.2 — Đặt tên + QUY LUẬT TỔNG HỢP + Top 1→5 + trọng số nên/không nên

### Tên bảng: "BẢNG CẦU LIÊN MIỀN (MN dẫn cầu)"

### QUY LUẬT TỔNG HỢP (rút từ 105 cầu registry)
1. **MN là "nguồn cái"**: MN D-1 (và MN D same-day) dẫn cầu cho cả 3 miền.
2. **Giải Tư (G4) là vị trí nguồn nóng nhất** (41/105 cầu); kế G6.
3. D-1 (hôm qua) chiếm đa số; cầu same-day (D) chỉ áp cho MT/MB SAU khi MN/MT xổ.
4. **⚠️ Recurrence=0**: không cầu nào lặp qua ≥2 thứ → dấu hiệu OVERFIT, chỉ forward mới xác nhận.

### Top 1→5
TOP_K 3→5, registry 105 cầu (3 miền × 7 thứ × 5). Rank 4-5 lift in-sample thấp hơn (rank1 +22pp → rank5 ~+17pp), cùng mức overfit — chỉ để xem rõ hơn.

### Trọng số nên/không nên
🟢 NÊN (forward≥8 mẫu & vượt nền ≥8pp) · 🟡 CÂN NHẮC · 🔴 KHÔNG NÊN · ⏳ ĐANG ĐO. Hiện **100% ⏳ ĐANG ĐO** — trung thực: chưa cầu nào đủ tin để chơi thật; tier tự nâng khi forward về.

## C. P&L TIMELINE FORENSIC (2026-02-28 → 2026-06-27)

### Đường tiền (BT 1-số official, bao lô 50 điểm)
- 28/02→30/04: **+71.2M** (đỉnh cộng dồn +74.7M tuần 27/04)
- 10/05→31/05: **−37.5M** (win-rate 40%→27%)
- Tháng 6: BT **−34.2M** / song-thủ **+24.6M** (chập chờn)
- Cộng dồn cuối ≈ **−0.6M** (sụt ~75M từ đỉnh)

### Sự cố
- final_bundles + lottery_results: 0 ngày thiếu; scrape không trễ.
- **model_daily_eval thiếu đúng 1 ngày 09/05** (verify gap) — khớp "lỗi không cập nhật ~10/05".
- "20 ngày" = giai đoạn LỖ 10/05–31/05, không phải mất dữ liệu.
- Mid-May (12-15/05): deploy + restart + verify pending → xáo trộn vận hành.

### Theo miền (BT 1-số)
| | Th2-4 | Th5 (10-31) | Th6 |
|---|---|---|---|
| MN | +10.7M (47%) | +1.6M (45%) | −12.8M (44%) |
| MT | +35.6M (47%) | −19.2M (27%) | −14.4M (33%) |
| MB | +19.2M (31%) | −19.9M (**9%**) | −7.0M (22%) |

### Giả thuyết "thêm model = bẫy" + phục hồi
- Roster official KHÔNG tăng (~14.5/ngày suốt). Model mới vào official chỉ Opus đổi tên.
- **Nguyên nhân = đổi REGIME**: model mạnh sụp đồng loạt (smart-ensemble 41→29, sonnet 40→27, opus 39→28) = đúng "bẫy số trùng lặp".
- **Backtest phục hồi 10/05→27/06**: quay về roster cũ TOP8 = −81.5M (TỆ HƠN official −71.8M); smart-ensemble đơn −86.5M; adaptive 21d cả rổ −37.5M (giảm nửa, vẫn lỗ); đuổi model nóng −81.5M. **Không cấu hình forward-valid nào làm BT 1-số có lãi lại.**
- **Đường phục hồi thật = song-thủ + chuyên biệt miền** (MN giữ BT ổn; MT/MB → song-thủ: MT +20.2M, MB +25.1M tháng 6). KHÔNG kỳ vọng quay-về-cũ.
