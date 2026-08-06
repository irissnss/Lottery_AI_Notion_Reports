# REPORT V11000 — 38 model, không con nào hơn chọn bừa

> **Ngày:** 2026-08-06 · **Mã việc:** FU-283
> **Báo cáo chung:** [`REPORT_V10993_V10996.md`](./REPORT_V10993_V10996.md)

---

## 1. Tóm tắt

Owner nêu đúng cốt lõi. Đo thẳng vào đó: **0/38 model hơn chọn bừa**, kể cả `combo-super` —
thứ gộp tất cả lại — cho **z = −0,14**.

## 2. Owner yêu cầu gì (nguyên văn)

> *"Giờ còn sửa gì nữa em ML và prompt thì sao em? cốt lõi không ra số trúng thì không có
> phương pháp nào để ra output chuẩn nổi em nhé. tiếp tục soi ML và Prompt"*

## 3. Đào bới / phát hiện — `VERIFIED_TEST`

Nguồn `model_daily_eval.bt_hit` · 11.577 dòng · 57 model · 29/01→04/08. So với **nền của chính
ngày đó** (số đuôi riêng biệt về / 100). 38 model đủ mẫu (n≥30), Bonferroni α=0,10/38 →
ngưỡng **|z| ≥ 3,01**.

| | Model | n | Trúng | Nền | z |
|---|---|---|---|---|---|
| Tốt nhất | AI `gemini-2.5-pro` | 460 | 37,6% | 34,0% | **+1,68** |
| | ML `smart-ensemble` | 523 | 36,3% | 34,0% | +1,14 |
| | ML `xgboost` | 519 | 34,9% | 34,0% | +0,42 |
| | ML `meta-learning` | 523 | 34,2% | 34,0% | +0,10 |
| **Bộ gộp** | ML **`combo-super`** | **539** | **33,8%** | **34,1%** | **−0,14** |
| | ML `random-forest` | 519 | 32,6% | 34,0% | −0,72 |
| | ML `lstm` | 521 | 31,5% | 34,0% | −1,23 |
| Kém nhất | AI `gemma-4-31b` | 244 | 25,4% | 34,0% | −2,88 |

**0/38 vượt ngưỡng. 0/38 kém có ý nghĩa.** Dải −2,88 → +1,68 đúng bằng thứ 38 người tung đồng
xu tạo ra.

**Ngưỡng để tự chứng minh:** n≈500, nền 34% → cần **~40,4% bền vững**. Tốt nhất 37,6%.

### Hai phát hiện phụ

**Bảng chi phí RỖNG.** `model_latency_cost_audit_daily`: 4.033 dòng, `cost_estimate` **0/4033**,
`token_count` **0/4033**, `latency_seconds` **0/4033**. `missing_reason` ghi rõ
`NO_COST_ESTIMATE,NO_TOKEN_COUNT,NO_PER_MODEL_DURATION`.

**Bầy đàn nặng.** 30 ngày, 93 lượt có ≥5 model: **25,8 model → 9,8 số riêng biệt**. 33% model
chọn cùng một số; 14% số lượt có ≥50% trùng. Nếu chọn độc lập thì kỳ vọng ~22,8 số riêng biệt.
Prompt có hẳn §22/§23 chống bầy đàn mà vẫn vậy.

## 4. Hướng xử lý và vì sao chọn

Không đề xuất chỉnh model hay chỉnh bộ gộp — **đo đã nói rõ nguyên liệu là nhiễu**, chỉnh cách
trộn nhiễu không tạo ra tín hiệu.

Đề xuất duy nhất còn giá trị: **đo được chi phí trước đã**. Khi 0/38 model hơn chọn bừa thì
quyết định hợp lý duy nhất là cắt tiền — mà không có số tiền thì không quyết được cắt con nào.

## 5. Đã làm gì

Đo và ghi. **Không sửa model, không sửa prompt, không sửa bộ gộp.** Mở `FU-283`.

## 6. Cổng kiểm

Dùng chính `_v10991_sample_gate` (Bonferroni) đã dựng và đã khớp tay 4/4 giá trị nhị thức.
Nền tính theo **từng ngày** chứ không lấy trung bình — tránh đúng lỗi đơn vị đã mắc ngày 05/08.

## 7. Vướng vấp

Không có lỗi mới trong phiên đo này. Nhưng cần nói rõ **giới hạn của phép đo**: nó trả lời
*"model có hơn chọn bừa không"*, **không** trả lời *"model nào đáng giữ nếu buộc phải giữ vài
con"*. Câu sau cần dữ liệu chi phí — hiện chưa có.

## 8. Gỡ về

Không có gì để gỡ — phiên này chỉ đọc và ghi tài liệu.

## 9. Theo dõi tiếp

**FU-283 · DO1308 · hạn 13/08** — truy vì sao ba cột chi phí không được ghi; nối lại từ
`prediction_trace.jsonl` (trace **có** `cost_estimate`, `token_count`, `latency_seconds`).
Có số tiền rồi mới trình owner phương án cắt.

**Còn treo:** FU-282 (dời lịch MN, 07/08) · FU-277 · FU-278 (13/08).
