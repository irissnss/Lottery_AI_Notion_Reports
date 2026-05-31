# V10643 — Forensic "Prompt shadow-first" + Kế hoạch THIẾT KẾ LẠI

**Ngày:** 2026-05-31. **Loại:** read-only forensic (không đụng code/official) + plan. **Chain:** … → V10642B → **V10643**.

## Câu hỏi của owner: "Prompt shadow-first có cứu hay phá?"

### Nó là gì
**V81 provider shadow pilot**: 3 model (claude-sonnet-4-6, deepseek-chat, gemini-3-flash) × 3 miền, gọi AI THẬT với prompt chuyên-gia-miền bản shadow (V104), chạy tự động **19:14 mỗi ngày**, ghi bảng shadow (không ảnh hưởng official).

### Nhìn bề mặt thì như "cứu" lớn (216 lệnh gọi OK, 06→30/05)
| Miền | shadow BT | official BT | chênh |
|---|:---:|:---:|:---:|
| MN | 64.4% | 41.1% | **+23.3pp** |
| MT | 45.2% | 38.4% | +6.8pp |
| MB | 15.1% | 4.1% | +11pp |

### 🔴 NHƯNG đây là ẢO do NHÌN TRƯỚC KẾT QUẢ (lookahead)
- Gọi lúc **19:14** — SAU khi cả 3 miền đã xổ + lưu kết quả (MN 16:38, MT 17:32, MB 18:32).
- Dữ liệu đầu vào (context) **lộ thẳng**: `actual_known: true`, `official_status: WIN`, và số trúng nằm sẵn trong tín hiệu (vd 30/05 số về **76**, context có v67/v73 = 76).
- **3 model luôn ra CÙNG 1 số mỗi ngày** → bị lái bởi "ứng viên" tính sau khi đã biết kết quả.
- Lịch chạy ghi rõ: "19:14 chạy sau V80 để tận dụng post-cascade data" = CỐ Ý sau kết quả.

### Verdict
**+23pp là ẢO, không phải edge thật khi chơi trước giờ xổ.** Vì nó cô lập (không tính vào official) nên KHÔNG phá số official trực tiếp — NHƯNG đang **đốt ~20.000 token/ngày** + tạo **ảo tưởng "cứu tinh" nguy hiểm**. → Nói thẳng: là **"phá"** theo nghĩa gây hiểu lầm + tốn chi phí, **KHÔNG dùng được như "cứu"**. Cùng họ ảo tưởng với "oracle headroom" đã bị bác ở V10641.

## Kế hoạch THIẾT KẾ LẠI

Nguyên nhân gốc lặp lại = **ảo do nhìn trước / in-sample**. Nên gốc sửa: **no-lookahead BẮT BUỘC theo thiết kế** (mọi dự đoán phải có dấu thời gian TRƯỚC giờ xổ; cái nào không chứng minh được → gắn cờ "HINDSIGHT").

| CP | Hạng mục | Hành động |
|---|---|---|
| **R1** (chờ owner, 03/06) | V81 shadow-prompt | **RETIRE** (tắt, lưu token ngay) **HOẶC** re-architect **EX-ANTE** (gọi TRƯỚC xổ, context sạch) |
| R2 | Harness no-lookahead | ghi `predicted_at` + cutoff giờ-xổ per miền; cờ HINDSIGHT cho bảng vi phạm (nền chống ảo) |
| R4 | P3 reduce-cadence | gọi THƯA model bị giảm = tiết kiệm token thật + vẫn đo recovery; reversible |
| R3 | (nếu chọn ex-ante) pilot | 1 model (gemini-3-flash) MN, gọi ~15:30 trước xổ, đo 3-4 tuần xem có edge thật |
| R5 | Selector per-slice | chọn theo (miền×thứ×đài) dùng model_progress, validate ex-ante qua harness |

Nền đã vững (V10642/B): nhãn per-ĐÀI, model_progress (RECOVERING), slice_policy REDUCE, UI per-đài.

*Public-safe: không chứa code private / DB rows / IP / path nội bộ. Tên model công khai.*
