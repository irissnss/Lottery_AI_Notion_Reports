# V10807 — SANDBOX A/B ĐỀ XUẤT ROUTING-GATE TRÊN 5 MODEL THẬT × 3 MIỀN × 2 ARM (30 CALL THẬT)

**Thời gian:** 2026-07-16 00:39 → 01:4x (giờ VN)
**Trigger (owner 00:39):** "Em đã test thử nghiệm trong sandbox chưa — nó ảnh hưởng đến output của đơn model AI. Cần thử nghiệm trong sandbox 3-5 model trên 3 miền, với model đang kém và đang mạnh."
**Phạm vi:** SANDBOX-ONLY — zero thay đổi runtime/prompt production. Hash 4 bảng official IDENTICAL trước/sau.

---

## 1. THIẾT KẾ THÍ NGHIỆM

| Thành phần | Chi tiết |
|---|---|
| Case (as-of lịch sử, đã biết KQ để chấm) | **MB@14/07** (bẫy 51), **MT@15/07** (bẫy 19/39/61), **MN@15/07** (bẫy 19) |
| Model KÉM | gemini-2.5-flash (−18pp V10804), gpt-5-mini (−11pp) — đúng 2 con trong danh sách thay API |
| Model MẠNH | claude-opus-4-6 (+32pp), qwen3.7-max (+33pp) |
| Model TRUNG | deepseek-reasoner |
| Arm A (gốc) | Prompt production nguyên bản, replay đúng đường code production (như V10805) |
| Arm B (vá) | Y hệt A + khối **"🧭 ĐIỀU KIỆN TRỎ MIỀN & NHÃN PER-SỐ"** (~1.1-1.3k chars/miền): (g) routing gate ô-âm/ô-dương theo ma trận V10806 + (a′) per-số %+n thật của từng rule + (h) trap CONV×2 MN / ghi chú CONV MB |
| An toàn | Chạy trên VPS bằng key production (DB-first), KHÔNG ghi DB, trace no-op; 30/30 call OK, 0 lỗi, ~42 phút |

Khối addendum mẫu (MT — rút gọn):

```
### 🧭 ĐIỀU KIỆN TRỎ MIỀN & NHÃN PER-SỐ (V10806 — ĐỌC BẮT BUỘC TRƯỚC KHI CHỐT SỐ)
Nhãn 12W/16W% ở MINED RULES là tỷ lệ CỤM-TRÚNG-BAO-LÔ, KHÔNG phải xác suất per-số...
⛔ Quảng Ninh G6+G7 (nguồn MB, D-1) → [05,12,39,68,74,75,99]: per-số ~26.9% (n=186) — ô nguồn-MB→MT ÂM −2.0pp (z=−3): CHỈ THAM KHẢO...
✔ Vũng Tàu GĐB+G1 (nguồn MN, D-1) → [19,61]: per-số ~44.1% (n=102) — ô nguồn-MN→MT +3.5pp: giữ nhưng KHÔNG dồn cả 2 vị trí vào cùng 1 rule
KẾT LUẬN BẮT BUỘC: nếu định chọn số thuộc dòng ⛔/⚠/🚨 phải nêu ≥2 bằng chứng nội-miền độc lập...
```

---

## 2. KẾT QUẢ ĐẦY ĐỦ 30 CALL

### MB @ 14/07 (bẫy 51 — KQ thật có 66, 32/36 trượt)

| Model | Arm A (gốc) | Arm B (vá) | Ghi chú |
|---|---|---|---|
| gemini-2.5-flash | [51,36] trap, trượt | [51,32] trap, trượt | đổi phụ 36→32 |
| gpt-5-mini | [97,51] trap, trượt | [97,00] **BỎ trap 51**, trượt | nghe lời gate |
| deepseek-reasoner | [97,66] **✅66** | [97,32] trượt | SE2: bỏ 66 (stat nội-miền) sang 32 (rule ✔) |
| qwen3.7-max | [51,36] trap, trượt | [51,32] trap, trượt | lì — giữ 51 cả 2 arm |
| claude-opus-4-6 | [51,66] trap, **✅66** | [51,36] trap, trượt | SE2: bỏ 66 sang 36 (rule ✔) |

### MT @ 15/07 (bẫy 19/39/61 — KQ thật có 32, 54)

| Model | Arm A (gốc) | Arm B (vá) | Ghi chú |
|---|---|---|---|
| gemini-2.5-flash | [68,19] trap, trượt | [19,32] **✅32** | bỏ 68 (ô-âm QN), phụ 32 trúng |
| gpt-5-mini | [19,61] trap×2, trượt | [19,54] **BỎ 61, ✅54** | nghe lời gate |
| deepseek-reasoner | [19,54] ✅54 | [19,93] trượt | đổi phụ 54→93 (rule ✔ Bạc Liêu) |
| qwen3.7-max | [68,61] trap, trượt | [61,68] trap, trượt | lì — vẫn ôm 61+68 |
| claude-opus-4-6 | [68,19] trap, trượt | [19,61] trap×2, trượt | **SE1: dồn cả 2 vị trí vào 1 rule ✔ VT** |

### MN @ 15/07 (bẫy 19 — KQ thật có 74, 98, 48, 17, 67)

| Model | Arm A (gốc) | Arm B (vá) | Ghi chú |
|---|---|---|---|
| gemini-2.5-flash | [19,61] trap, trượt | [74,18] **BỎ 19, ✅74** | cải thiện rõ nhất |
| gpt-5-mini | [19,98] trap, ✅98 | [19,48] trap, ✅48 | giữ 19 nhưng vẫn trúng phụ |
| deepseek-reasoner | [68,18] trượt | [74,18] **✅74** | chuyển sang tail per-số cao |
| qwen3.7-max | [61,63] trượt | [54,18] trượt | đổi nhưng chưa trúng |
| claude-opus-4-6 | [17,67] **✅17,67** | [17,67] **✅17,67** | duy nhất giữ nguyên — trúng đôi cả 2 arm |

### Tổng hợp

| Chỉ số | Arm A (gốc) | Arm B (vá) | Δ |
|---|---|---|---|
| Đổi pick A→B | — | **14/15 cặp** | addendum tác động thật |
| any-hit | 5/15 | 6/15 | +1 (nhiễu, mẫu nhỏ) |
| main-hit (vị trí BT) | 1/15 | 3/15 | +2 |
| Dính trap | 11/15 | 9/15 | −2 |
| MT dùng tail ô-âm QN | 3/5 | 1/5 | **−2 (đúng thiết kế)** |
| Vị trí phụ là trap | 5/15 | 1/15 | **−4 (đúng thiết kế)** |
| Model KÉM trúng | 1/6 | **4/6** | **+3 — hưởng lợi nhất** |
| Model MẠNH trúng | 2/6 | 1/6 | −1 (trơ với addendum) |
| deepseek trúng | 2/3 | 1/3 | −1 (SE2) |

---

## 3. TRẢ LỜI CÂU HỎI OWNER

**"Nó ảnh hưởng đến output của đơn model AI?"** — CÓ, rất mạnh: 14/15 model đổi pick khi thêm khối điều kiện; 7/15 record arm B trích dẫn trực tiếp "per-số / ô nguồn / chỉ tham khảo" trong reasoning.

**"Model đang kém và đang mạnh phản ứng khác nhau?"** — KHÁC RÕ:
- **Model KÉM nghe lời và hưởng lợi nhất** (1/6 → 4/6 trúng; trap 6/6 → 4/6): gemini-flash bỏ 19@MN → trúng 74; gpt-5-mini bỏ 61@MT → trúng 54, bỏ 51@MB. Đây chính là 2 con đang nằm danh sách thay API — gate có thể cứu được chúng trước khi phải thay.
- **Model MẠNH trơ:** qwen lì 51@MB + 61@MT cả 2 arm; opus tự tin hướng riêng ([17,67]@MN trúng đôi cả 2 arm — không cần gate). Chữ nghĩa mềm không lay chuyển được model mạnh.
- **Nhãn per-số làm việc đúng:** cho model thấy trật tự giá trị thật — rule MN per-số 45-48% (đáng theo) vs MB 20-33% (đừng dồn); trước đây mọi rule đều khoe "83-92%" nhìn như nhau.

**Hành vi đổi đúng hướng thiết kế:** MT bớt dùng tail ô-âm Quảng Ninh (3/5 → 1/5); vị trí phụ bớt trap (5/15 → 1/15); MN sạch hơn (any-hit 2 → 4).

---

## 4. HAI TÁC DỤNG PHỤ PHÁT HIỆN ĐƯỢC (giá trị nhất của sandbox)

- **SE1 — dòng ✔ thành nam châm herd mới:** opus@MT arm B dồn CẢ 2 vị trí vào đúng 1 rule ✔ Vũng Tàu [19,61], vi phạm ngay câu cấm mềm trong addendum (thêm trap 61 so với arm A). → bản (g′) phải nâng thành **ràng buộc cứng "mỗi rule tối đa 1 vị trí"** (validate bằng JSON contract nếu owner muốn cứng tuyệt đối).
- **SE2 — hút model khỏi tín hiệu nội-miền:** MB arm A deepseek [97,66]✅ + opus [51,66]✅ nhờ 66 = top-10 thống kê nội-miền; arm B cả hai bỏ 66 chạy sang tail rule ✔ (32/36) → 0 hit. → (g′) thêm **mandate đa dạng: "ít nhất 1 trong 2 vị trí phải từ tín hiệu NỘI-MIỀN độc lập (thống kê/phase/gan), không lấy từ rule block"**.

Lưu ý đúng thiết kế (không phải lỗi): 51@MB arm B vẫn được phép pick (ô nguồn-MN→MB DƯƠNG +5.5pp — gate chỉ hạ kỳ vọng per-số ~33%, không cấm); 19/61@MT vẫn được phép (rule VT dương thật +13-15pp, trượt 15/07 là variance ~32% như V10806 đã tính).

**Giới hạn trung thực:** mỗi case chỉ 1 ngày → any-hit 5 vs 6 KHÔNG đủ kết luận accuracy tổng thể. Kết luận chắc chắn của sandbox nằm ở HÀNH VI (đổi pick, né ô-âm, né trap phụ) — đúng câu owner hỏi ("ảnh hưởng đến output").

---

## 5. ĐỀ XUẤT CHO CP-L6 19/07 (chờ owner ký — chưa đổi gì)

1. **(g′)** = (g) routing gate + vá SE1 ("mỗi rule tối đa 1 vị trí" — cứng) + vá SE2 ("≥1 vị trí từ tín hiệu nội-miền độc lập").
2. **(h)** trap alert theo miền giữ nguyên đề xuất (MN CONV×2, MB giữ ×3, MT cảnh báo tail nguồn-MB).
3. **(a′)** nhãn per-số %+n GIỮ — sandbox cho thấy nó là thứ giúp model yếu tự xếp lại trật tự.
4. Nếu ký: implement trong `build_context_pack` (render production, không cần file ngoài) + **shadow 7 ngày** trước khi bật official.
5. Gợi ý cân nhắc thêm: gate cứu được gemini-flash/gpt-5-mini trong sandbox — owner có thể hoãn thay API 2 con này đến sau 7 ngày shadow để so.

## 6. AN TOÀN & ARTIFACTS

- ZERO đổi runtime; không ghi DB (log_prediction_trace no-op); hash 4 bảng sau phiên IDENTICAL với post-V10806: predictions 10122/3a18c24b, final_bundles 414/0e68ae9c, lottery_results 15081/1a1820b1, model_daily_eval 9986/aaa91dc6.
- Code: `web/backend/_v10807_ab_sandbox.py` (engine), `_v10807_run_ab_vps.py`, `_v10807_analyze.py`, `_v10807_fetch_results.py`, `_v10807_hash_check.py` (private repo).
- Dữ liệu: `artifacts/v10807_ab/v10807_ab_results.json` + 3 file addendum (private); bản addendum đầy đủ 3 miền trong `EVIDENCE_ADDENDUM_3_MIEN.md` (folder này).
