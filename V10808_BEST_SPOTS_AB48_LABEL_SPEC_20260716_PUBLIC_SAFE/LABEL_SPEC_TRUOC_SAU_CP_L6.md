# V10808 — ĐẶC TẢ NHÃN PROMPT TRƯỚC/SAU (bản cụ thể cho owner ký CP-L6 19/07)

Nguyên tắc theo đúng chỉ đạo owner: **GIỮ NGUYÊN nhãn cũ** (không phá cách rules học/xếp hạng), **THÊM điều kiện** để model hiểu đúng nghĩa con số % và trỏ đúng miền. Toàn bộ đã qua sandbox 78 call thật (V10807: 30 call 3 ngày bẫy; V10808: 48 call 4 ngày thường).

---

## 1. KHỐI "MINED RULES" — ví dụ THẬT (MT, thứ Tư 15/07)

### ❌ TRƯỚC (đang chạy production — thứ đã gây vụ 19/39/61)

```
### 📜 MINED RULES MT/Thứ Tư (READY_STRONG | 3-LAYER V20.2):
  📋 Format: source | rank(12W/16W) | legacy | HR12W(L1) | HR16W(L2) | HR4W(L3) | composite | verdict
  ✔ Quảng Ninh G6+G7: rank=0.83 | legacy=0.79 | 12W=75.0%(L1) | 16W=68.8%(L2) | 4W=50.0%(L3) | comp=0.79 | 🟢HIGH_CONF_CURRENT
  ✔ Vũng Tàu GĐB+G1: rank=0.78 | legacy=0.75 | 12W=75.0%(L1) | 16W=62.5%(L2) | 4W=75.0%(L3) | comp=0.75 | 🟢HIGH_CONF_CURRENT
  ...
    ← Quảng Ninh G6+G7 → [05, 12, 39, 68, 74, 75, 99]
    ← Vũng Tàu GĐB+G1 → [19, 61]
```

Vấn đề đã chứng minh (V10805/V10806): model đọc "75%" như xác suất TỪNG SỐ → 12-16 model dồn vào 19/39; thực tế 75% là tỷ lệ "TRÚNG-ÍT-NHẤT-1-SỐ-TRONG-CỤM" (baseline cụm 2 số đã ~51% ở MT); per-số thật của Quảng Ninh G6+G7→MT chỉ 26.9% — DƯỚI baseline 35.2%.

### ✅ SAU (đề xuất — giữ dòng cũ, THÊM 1 dòng phụ mỗi rule + header + footer)

```
### 📜 MINED RULES MT/Thứ Tư (READY_STRONG | 3-LAYER V20.2):
  📋 Format: source | rank(12W/16W) | legacy | HR12W(L1) | HR16W(L2) | HR4W(L3) | composite | verdict
  ⚠ LƯU Ý NGHĨA SỐ %: 12W/16W% = tỷ lệ CỤM-TRÚNG-BAO-LÔ (ít nhất 1 trong k số của cụm về),
    KHÔNG phải xác suất từng số. Kỳ vọng TỪNG SỐ nằm ở dòng ↳ bên dưới mỗi rule.
  ✔ Quảng Ninh G6+G7: rank=0.83 | legacy=0.79 | 12W=75.0%(L1) | 16W=68.8%(L2) | 4W=50.0%(L3) | comp=0.79 | 🟢HIGH_CONF_CURRENT
     ↳ per-số ~26.9% (n=186) | ô nguồn-MB→MT −8.4pp ⛔ CHỈ THAM KHẢO — muốn dùng làm BT chính
       phải nêu ≥2 bằng chứng nội-miền MT độc lập | tối đa 1 vị trí từ rule này
  ✔ Vũng Tàu GĐB+G1: rank=0.78 | legacy=0.75 | 12W=75.0%(L1) | 16W=62.5%(L2) | 4W=75.0%(L3) | comp=0.75 | 🟢HIGH_CONF_CURRENT
     ↳ per-số ~44.1% (n=102) | ô nguồn-MN→MT +3.5pp ✔ GIỮ GIÁ TRỊ | tối đa 1 vị trí từ rule này
  📌 RÀNG BUỘC CHỐT SỐ (bắt buộc):
     • Mỗi rule chỉ được dùng cho TỐI ĐA 1 vị trí (BT hoặc phụ — không dồn cả 2 vào 1 rule).
     • Ít nhất 1 trong 2 vị trí phải đến từ tín hiệu NỘI-MIỀN độc lập (thống kê/phase/gan/cụm),
       KHÔNG lấy từ danh sách rule ở trên.
```

## 2. QUY TẮC GÁN ✔/⛔ CHO DÒNG ↳ (máy tự tính, model chỉ đọc)

| Điều kiện | Nhãn | Ví dụ thật |
|---|---|---|
| Rule per-số z≥2 DƯƠNG (bất kể ô) | ✔ GIỮ GIÁ TRỊ | Hải Phòng G6→MT +14.8pp z=2.18 (dương thật dù nằm Ô MB→MT âm) |
| Ô dương + rule không âm | ✔ | Đồng Tháp G5+G7→MB (ô MN→MB +5.5pp) |
| Ô âm + rule per-số không cứu được (z<2) | ⛔ CHỈ THAM KHẢO | Quảng Ninh G6+G7→MT (−8.4pp z=−2.39, n=186) |
| Ô trung tính | · (chỉ in per-số, không phán) | nguồn-MB→MN (+1.1pp z=1.3) |

Điểm mới so với V10806/V10807 (nhờ đào bới best-spots): **gate theo Ô làm NỀN + NGOẠI LỆ per-rule** — không chặn mù cả ô, vì trong cùng ô MB→MT âm vẫn có Hải Phòng G6 dương thật.

## 3. TRAP ALERT THEO MIỀN (đề xuất (h) — giữ từ V10806)

- MN: hạ ngưỡng cảnh báo hội tụ xuống **CONV×2** (data: MN CONV×2 chỉ 38.8% < baseline 42.9%).
- MB: GIỮ ngưỡng CONV×3 (MB CONV×2 = 50.6%, đang ăn — không đụng).
- MT: cảnh báo đã nằm trong dòng ⛔ per-rule ở trên (không cần alert riêng).

## 4. CĂN CỨ SANDBOX (78 call thật, không ghi DB)

| Phép đo | Prompt gốc | Prompt vá | Ghi chú |
|---|---|---|---|
| 3 ngày bẫy × 5 model (V10807) | 5/15 trúng, 11/15 dính bẫy | 6/15 trúng, 9/15 dính bẫy | MT dùng ô-âm 3/5→1/5; phụ-là-trap 5/15→1/15; model yếu 1/6→4/6 |
| 4 ngày thường × 2 model rẻ (V10808) | 16/24 (67%) | **18/24 (75%)**, trúng-đôi 2→5 | không miền nào bị phá |
| GỘP 7 ngày, 2 model rẻ (30 cặp) | 57% | **73% (+16pp)** | thắng-mới 8 / mất 3; sign-test p≈0.11 — hướng tốt, CHƯA đạt ý nghĩa → cần shadow live |

## 5. LỘ TRÌNH NẾU OWNER KÝ (CP-L6 19/07)

1. Implement dòng ↳ + header + footer trong `build_context_pack` (máy tự tính per-số/ô từ `mined_rule_effectiveness` mỗi ngày — không hard-code).
2. (i) Align tier miner theo per-số: promote 12 ô dương z≥2, demote/loại Quảng Ninh G6+G7→MT.
3. Chạy **shadow 7 ngày** (lane test/shadow eval đọc prompt mới, official giữ prompt cũ) → so any-hit + trap-rate → owner quyết bật official.
4. Hoãn thay API gemini-2.5-flash / gpt-5-mini đến sau shadow (2 con này hưởng lợi nhất từ gate: gpt-5-mini 8/12→10/12).
