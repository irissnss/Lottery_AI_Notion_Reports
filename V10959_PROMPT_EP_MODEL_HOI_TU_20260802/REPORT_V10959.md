# V10959 — Prompt có đang ép model hội tụ không?

**Ngày:** 02/08/2026 · **Commit riêng:** `6143995` · **Commit công khai:** `ce671fe` · **Trạng thái:** ĐẠT (chỉ đọc + đo)

> Khung A55.3. Phiên **chỉ đo** — không sửa code, không deploy. Owner đã đóng băng đường ra số tới hết 08/08 (QD-014).

---

## 1. Tóm tắt

Owner đúng phần lõi: các model dùng prompt **hội tụ mạnh** — bạch thủ trùng nhau khoảng **24–27%**, gấp khoảng **24–27 lần** mức ngẫu nhiên (1%). Model không dùng prompt (ML) gần như **không** trùng với model prompt (~**1,6%**, sát ngẫu nhiên). Đó là bằng chứng mạnh rằng prompt đang kéo AI về cùng một chỗ.

Owner hơi sai về hình dạng cụm: không phải hai cụm sạch “total giống nhau / eval giống nhau”. Trong prompt-TOTAL trùng **26,0%**, prompt-EVAL **26,9%**, giữa hai nhóm vẫn **22,3%** — chỉ hơn nhau khoảng 4 điểm phần trăm. Cấu trúc thật là **một đàn prompt lớn**, với một hiệu ứng nhẹ của nhánh shadow (PHASE-FIRST).

Việc chạy hai prompt song song trên cùng một model: đã làm nhỏ/lẻ (V10768 de-herd, V10781 PROMPT_V2 trên deepseek, sandbox V10807/08) nhưng **chưa bao giờ chạy đủ roster**; lane PROMPT_V2 đã tắt 01/08; thiết kế “chéo prompt” GĐ4 vẫn **chưa chạy**.

---

## 2. Owner yêu cầu gì (nguyên văn)

> *"Sao anh thấy các model eval có kết quả gần gần giống nhau, còn các model trong total ra kết quả gần gần giống nhau? Có khi nào do prompt không đúng không em? Giống như miền Trung hiện tại Opus 4.6 ra 69-86 còn GPT 5 mini ra 71-65, và nhóm eval thì giống giống nhau, còn nhóm total official thì giống giống nhau."*

Kèm nhiệm vụ: chỉ đọc và đo; đo trùng lặp bằng số; đọc prompt; tra việc A/B prompt; kết luận dứt khoát; đề xuất nhưng không tự làm (đóng băng tới 08/08).

---

## 3. Đào bới / phát hiện

### Cách đo

- VPS qua paramiko: `_v10959_do_trung_lap.py`, `_v10959b_kiem_cheo.py`, `_v10959c_ab_status.py`, `_v10959d_ab_counts.py`.
- Nguồn: `model_daily_eval` (bt_number + main_numbers), cửa sổ chính **01/05→31/07** (trước hoán đổi gpt-5-mini / gpt-oss-120b ngày 01/08) — 273 cặp ngày-miền.
- Kiểm chéo: `predictions` (run_source auto_daily/ai_chain) khớp MDE **100%** khi cùng có; BT trùng prompt↔prompt trên predictions = **27,06%**.
- Baseline ngẫu nhiên: BT độc lập đều = **1%**; Jaccard dàn ~2 số ≈ **0,01**.
- Phân cụm: gộp cặp nếu tỉ lệ trùng BT trung bình ≥ ngưỡng 0,15 / 0,20 / 0,25 / 0,30.

### Số liệu chính (prompt lõi, nhóm lịch sử đúng)

| So sánh | BT trùng | Jaccard dàn | Cỡ mẫu cặp-ngày |
|---|---:|---:|---:|
| Trong TOTAL prompt (8 model) | **26,0%** | 0,256 | 6434 |
| Trong EVAL prompt (11 model) | **26,9%** | 0,238 | 8380 |
| Giữa TOTAL ↔ EVAL prompt | **22,3%** | 0,203 | 16064 |
| Mọi cặp prompt↔prompt | **24,4%** | 0,226 | — |
| Cặp ML↔ML | **15,1%** | 0,170 | 6 cặp model |
| Cặp prompt↔ML | **1,57%** | 0,018 | — |
| Ngẫu nhiên | **1,0%** | ~0,01 | — |

### Cặp then chốt

| Cặp | BT trùng | n |
|---|---:|---:|
| claude-opus-4-6 × claude-sonnet-4-6 | **51,1%** | 135 |
| gpt-5-mini × gpt-5.4 | 36,9% | 271 |
| gemini-2.5-flash × gemini-2.5-pro | 30,5% | 272 |
| random-forest × xgboost | 26,4% | 273 |
| gpt-5-mini × claude-opus-4-6 (MT ví dụ owner) | **17,2%** | 134 |
| random-forest × claude-opus-4-6 | **2,2%** | 135 |
| lstm × claude-opus-4-6 | **0,7%** | 135 |

Ví dụ owner (Opus 69-86 vs GPT-5-mini 71-65): đó là **hai dàn khác nhau**, không phải trùng. Trên 45–134 ngày MT, hai model này chỉ cùng bạch thủ khoảng **17–22%** — không “gần giống” về đúng số; cảm giác “giống nhóm” đến từ việc cả đàn prompt đều lệch khỏi ML theo cùng một hướng.

### Cụm

- Ngưỡng 0,20: một cụm prompt **12 model** lẫn TOTAL và EVAL (sonnet, deepseek, gemini-2.5, gpt-5-mini, gpt-5.4, gpt-5.5, …) + một cụm ML/ensemble riêng.
- Ngưỡng 0,25: lõi TOTAL AI 4 model (sonnet, deepseek, gemini-2.5-flash/pro) tách ra; vẫn không thành đúng “2 cụm = total / eval”.

### RULES-FIRST ép danh sách số

Trên 120 ngày-miền mẫu, danh sách mined-rules trung bình **11 số**:

| Nhóm | % bạch thủ nằm trong danh sách rules |
|---|---:|
| Model prompt | **35,8%** |
| Model ML | **12,9%** |
| Đuôi số thật sự về | **12,4%** |
| Kỳ vọng nếu chọn đều trên 100 số với list 11 | ~**11%** |

Prompt model bị kéo vào list gấp ~3 lần so với ML và so với số thật.

### Nội dung prompt (đọc code + dựng pack mẫu VPS ngày 01/08 MT)

- Một bộ dựng chung (`gpt_analyzer`): SP-4.1 + body + CTX-16.5 + RR-16.4 + RULES-FIRST.
- Nhánh `shadow_mode`: thêm PHASE-FIRST (~+3000–4000 ký tự). Pack official mẫu 10363 ký tự; shadow 13342; sau de-herd còn 9271 / 12250.
- De-herd V10768 đang bật: đã cắt bảng xếp hạng WR/BT khỏi pack.
- Chỗ còn ép hội tụ:
  1. **RULES-FIRST** — danh sách số tường minh; MB/MN bắt buộc chọn main từ list.
  2. **Thống kê đã nhai** trong body (`TOP 5 GỢI Ý`, gan, trend — `statistical_analyzer.format_condensed_stats`).
  3. **Few-shot** trong SYSTEM_PROMPT với số cụ thể (64, 46, 47, 12…).
  4. **Cùng một body** cho mọi LLM official; shadow chỉ thêm gate kể chuyện.
- Ước lượng thô: khoảng **70–80%** nội dung là kết luận/xếp hạng/luật đã nhai; **20–30%** là đuôi thô theo giải.

### Ngày đồng thuận cao vs thấp → phiếu có hơn không?

276 ngày-miền, chia ba theo % model TOTAL-prompt cùng số mode:

| Tertile | Đồng thuận TB | Hit TB (theo đài) |
|---|---:|---:|
| Thấp | 28% | 15,9% |
| Trung | 43% | 13,6% |
| Cao | 65% | 16,9% |

Không có quan hệ sạch “bất đồng thì phiếu tốt hơn”. MN hơi nghiêng bất đồng tốt hơn; MT/MB nghiêng đồng thuận tốt hơn. Không được dùng lát cắt này để hứa phục hồi lớn.

### Việc A/B prompt đã tới đâu

| Việc | Same-model 2 prompt? | Trạng thái |
|---|---|---|
| V10768 de-herd sandbox → official | Có (3 model × 2 biến thể) | ĐÃ làm, đã đưa vào official 02/07 |
| V10781 `PROMPT_V2_AB_V1` | Có (chỉ deepseek-reasoner) | Chạy 05/07→01/08 (79 hàng); cron tắt 01/08; **chưa có báo cáo đối đầu** |
| V10807/08 sandbox | Có (one-shot) | Xong một lần, không lưu bảng |
| V104 / V81 shadow-prompt | Không (tiêm ứng viên / hậu kỳ) | RETIRED 31/05 (lookahead) |
| GĐ4 “chéo prompt” roster | Có (thiết kế đúng) | **CHƯA BAO GIỜ CHẠY** — chờ owner |

---

## 4. Hướng xử lý và vì sao chọn

Phiên này chỉ đo (QD-014). Không chọn phương án sửa.

Các hướng *đề xuất sau 08/08* (không tự làm):

1. **Bóc RULES-FIRST cứng** (đặc biệt lệnh “BẮT BUỘC chọn từ danh sách”) — nghi phạm số 1 vì coverage 35,8% vs ~11% nền.
2. **Chạy chéo prompt đúng nguyên tắc owner**: cùng model × prompt A (official) × prompt B (shadow/gầy) ≥14 ngày — đúng GĐ4 đã viết sẵn.
3. **Giảm trọng số đàn prompt trong phiếu** / tăng trọng số ML độc lập (khớp V10955: RF còn tín hiệu vì không đọc prompt).
4. Không nên chỉ so “nhóm total vs nhóm eval” — phép đo đó bị nhiễu; phải so prompt↔prompt vs prompt↔ML.

---

## 5. Đã làm gì

| File | Thay đổi |
|---|---|
| `web/backend/_v10959_do_trung_lap.py` | Script đo trùng lặp (chỉ đọc) |
| `web/backend/_v10959b_kiem_cheo.py` | Kiểm chéo nhóm lịch sử + RULES-FIRST |
| `web/backend/_v10959c_ab_status.py` | Trạng thái A/B + kích thước pack |
| `web/backend/_v10959d_ab_counts.py` | Đếm hàng PROMPT_V2 / V104 / V81 |
| `artifacts/v10959_prompt_hoi_tu/*.json` | Bằng chứng số |
| `CHANGELOG.md` / `docs/CURRENT_TRUTH_SSOT.md` / `docs/FOLLOW_UP_TRACKER.md` | Ghi nhận qua `prepend()` |
| Báo cáo công khai | thư mục này |

Backup: không sửa runtime. Deploy: không. Hash 4 bảng khoá: không đụng — không áp dụng.

---

## 6. Cổng kiểm

| Mục | Kết quả |
|---|---|
| Chỉ đọc / không deploy | Đạt |
| Cỡ mẫu ≥90 ngày | Đạt (01/05→31/07 ≈ 92 ngày lịch; 273 ngày-miền) |
| Ba miền | Đạt |
| Baseline ngẫu nhiên | Đạt (1%) |
| Kiểm chéo MDE ↔ predictions | Đạt (100% khi cùng có) |
| Phân nhóm lịch sử (trước 01/08) | Đạt (tránh nhiễu V10931) |
| Báo cáo 9 phần A55 | Đạt (file này) |
| Notion ghi | Không đụng (A55) |

---

## 7. Vướng vấp

1. Lần đo đầu dùng registry *hiện tại* → gpt-5-mini bị xếp EVAL dù gần như cả cửa sổ nó còn TOTAL. **Hậu quả nếu bỏ qua:** tưởng TOTAL ít hội tụ hơn sự thật. Đã đo lại với nhóm lịch sử.
2. Cột `lo2_numbers` không tồn tại trên VPS — đúng là `main_numbers`. **Hậu quả:** script gãy ngay nếu không dò schema.
3. `build_context_pack` in noise ra stdout → JSON hỏng. **Hậu quả:** mất bằng chứng kích thước prompt. Đã nuốt stdout / ghi file.
4. Lát cắt “ngày bất đồng → phiếu tốt hơn” không ủng hộ giả thuyết phục hồi sạch. **Hậu quả nếu báo cáo chiều lòng:** hứa phục hồi ảo.

---

## 8. Gỡ về

Không áp dụng vì không sửa code / không deploy. Xoá tài liệu phiên nếu cần: revert commit docs + xoá thư mục báo cáo công khai.

---

## 9. Theo dõi tiếp

| Mã | Việc | Ngưỡng / hạn |
|---|---|---|
| FU-222 | Sau 08/08: thử bóc/nới RULES-FIRST (shadow trước) | Đo BT trùng prompt↔prompt; mục tiêu giảm từ ~26% xuống gần ≤10% trong 14 ngày; hạn rà 2026-08-22 |
| FU-223 | Chạy GĐ4 chéo prompt cùng model (chờ owner OK) | ≥14 ngày × ≥4 model; báo cáo đối đầu; hạn thiết kế 2026-08-10 |

**Kết luận một câu cho owner:** Anh đúng là prompt đang ép model hội tụ (BT trùng ~26% vs ngẫu nhiên 1%, còn ML gần như không dính prompt); anh chưa đúng nếu nói có đúng hai cụm total/eval sạch — đó chỉ là một đàn prompt, với nhánh shadow hơi dính hơn một chút.
