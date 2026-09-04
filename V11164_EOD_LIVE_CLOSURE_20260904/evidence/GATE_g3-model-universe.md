# gate4 · tang=EVIDENCE_COMPLETE · 13 phat hien

## TOM TAT

Vũ trụ model thật là 63 danh tính (57 trong `predictions` ∪ 6 chỉ có trong registry) — con số «57 nguồn lịch sử» ĐÚNG cho `predictions.ai_model` nhưng THIẾU 6 mục registry, và 3 chuỗi `<NULL>` / `NO_TOKEN_DIAGNOSTIC` / `all` không phải model. Ngày 04/09 roster khớp tuyệt đối: hàm của chính hệ `get_expected_models()` mong đợi 27 model, thực tế đúng 27 model × 3 miền = 81 dòng, 0 dòng rỗng, 0 timeout, 0 model shadow rò vào bundle. Phát hiện nặng nhất là CẤU TRÚC chứ không phải vận hành: 7/15 voter của bundle là dẫn xuất hoặc cha mẹ của nhau (smart-ensemble ⊂ 4 ML · smart-ml = xgboost+random-forest · combo-super = top-3 của chính pool đó), nên số voter công bố LỚN HƠN số nguồn độc lập — ngày 04/09 số 73 ở MN có 3 phiếu nhưng chỉ 2 nguồn. Kèm theo là một lỗi ghi nhãn đã chứng minh: `smart-ensemble` chọn top-2 ML ĐỘNG nhưng `verdict_reason` và nhật ký luôn viết cứng «Meta / LSTM», nên ngày 04/09 MN cha mẹ thật là `xgboost + meta-learning` mà sổ ghi là Meta+LSTM. Đo 60 ngày trên nền ĐÚNG cho từng miền (phủ sóng đuôi 2 số / 100, bootstrap cụm theo ngày): KHÔNG model nào vượt nền có ý nghĩa, ba dòng dưới nền (`gemma-4-31b` đã nghỉ · `glm-5.2` · `smart-ml`) trong đó hai dòng sau sát biên và chưa hiệu chỉnh đa biến. `combo-super` — model cờ đầu — chỉ đổi top1 6/158 bundle và đóng 6,0% điểm top1, 0 cứu / 0 phá.

## TRA LOI CAU HOI

**1. «57 nguồn lịch sử» — kiểm chưa?** Rồi. `SELECT COUNT(DISTINCT ai_model) FROM predictions` = **57**, đúng. Nhưng đó KHÔNG phải vũ trụ model: hợp với `MODEL_REGISTRY` (49) cho **63 danh tính**, và có 3 chuỗi trong các bảng khác không phải model (`<NULL>` · `NO_TOKEN_DIAGNOSTIC` · `all`) phải loại chứ không đếm.

**2. Reconciliation các tập.** 63 vũ trụ · 30 `ALL_RUNTIME_MODELS` (gồm 2 RERANK + 1 model video ⇒ 27 model sinh dự đoán) · 27 roster mong đợi 04/09 = **27 roster thực tế** (khớp tuyệt đối, hiệu hai chiều rỗng) · 15 `OUTPUT_ELIGIBLE` = **15 voter-at-time 04/09** (0 rò shadow) · 11 `SHADOW_MODELS` = đúng 11 model chạy lane `shadow_auto_eval` với regime `CONTEXT_ONLY_V2` · 21 danh tính từng ảnh hưởng TRỰC TIẾP tới TOTAL trên 456 bundle lịch sử.

**3. Nguồn ảnh hưởng GIÁN TIẾP tới TOTAL — phần gate hỏi mà số liệu bề mặt không trả lời được.** Ngoài 15 voter trực tiếp còn hai đường gián tiếp đã truy được: (a) 4 ML gốc chảy vào TOTAL **hai lần** — một lần trực tiếp, một lần qua smart-ensemble/smart-ml; (b) combo-super **gọi lại bằng API mới** những model AI mà nó chọn (04/09: gemini-2.5-pro + claude-opus-4-6 ở MN, gemini-2.5-flash ở MT), rồi bỏ phiếu như một voter thứ 15 độc lập.

**4. Từng identity có đủ trường chưa?** Có — 63/63 danh tính trong `v11164_g3_model_universe.json` mang đủ: canonical identity · aliases · route thật · loại · parent/lineage · lane · official/shadow/both · first/last seen · khả dụng · expected vs output THỰC TẾ 04/09 · parse/timeout/empty · vote eligibility · effective weight · TOTAL influence (04/09 + lịch sử) · duplicate-parent risk · chất lượng vs nền · marginal save/break · khuyến nghị vòng đời · mức bằng chứng.

**5. Các điều CẤM — đã giữ.** Không ép model đơn xuất 3 càng (3 càng chỉ khoá ở PREFIX + BT official của đúng lane, không đưa vào trường của model đơn). Không coi model thiếu dòng TRƯỚC ngày nó tồn tại là thừa — mọi `first_seen` đều đọc từ `date` thật, và `gpt-oss-120b` (từ 01/08) hay `claude-opus-4-6` (từ 17/06) được chấm đúng từ mốc ra đời. Không gộp *unavailable / not invoked / parse fail / genuine no-output*: 04/09 cả bốn loại đều bằng 0, và `wan-2.7`/`pplx-embed-v1` được ghi là **kỳ vọng 0 theo thiết kế** chứ không phải «không có output». Không gọi hai nguồn là độc lập chỉ vì top-1 không đổi sau dedupe — ngược lại, mục 3 chứng minh chúng KHÔNG độc lập bằng lineage code + nhật ký, không bằng phép so top-1.

**6. Điều cần nói thẳng.** Ngày 04/09 vận hành **sạch**: đúng roster, đúng số lượt, không rỗng, không timeout, không rò shadow. Vấn đề nằm ở tầng dưới: cách **đếm phiếu** và cách **ghi cha mẹ**, cộng với việc suốt 60 ngày **không model nào chứng minh được là hơn nền**. Đây là ngày thứ nhất, không phải xu hướng — cấm đọc thành «model tốt lên» hay «model hỏng».


## PHAT HIEN (tieu de)
  - [PROVEN_DEFECT] smart-ensemble ghi SAI cha mẹ: chọn top-2 ML ĐỘNG nhưng nhãn viết cứng «Meta / LSTM»
  - [PROVEN_DEFECT] Số voter công bố LỚN HƠN số nguồn độc lập — 7/15 voter là dẫn xuất hoặc cha mẹ của nhau
  - [PROVEN_DEFECT] combo-super GỌI LẠI thành viên AI bằng lượt API MỚI thay vì dùng dòng đã lưu — trả tiền hai lần và đẻ ra phiếu trùng nguồn
  - [SUSPICIOUS_NEEDS_MORE_EVIDENCE] Đo 60 ngày trên nền ĐÚNG cho từng miền: KHÔNG model nào vượt nền có ý nghĩa
  - [OPERATIONAL_IMPROVEMENT] combo-super gần như không ảnh hưởng tới TOTAL: 6/158 bundle đổi top1, 6,0% điểm top1, 0 cứu / 0 phá
  - [NO_ANOMALY_FOUND] Roster 04/09 khớp tuyệt đối 27/27 — không thiếu, không thừa, không rỗng, không timeout
  - [EXPECTED_BEHAVIOR] contam_hits=4 trên lane official là ĐÚNG THIẾT KẾ; 33/33 lượt shadow sạch — V11160 nay có bằng chứng NỘI DUNG
  - [SUSPICIOUS_NEEDS_MORE_EVIDENCE] Ngày 13/04/2026: ba model shadow/retired bỏ phiếu vào bundle OFFICIAL qua run_source='manual'
  - [PROVEN_DEFECT] Con số «57 nguồn lịch sử» ĐÚNG nhưng KHÔNG PHẢI là vũ trụ model — vũ trụ thật là 63
  - [PROVEN_DEFECT] Alias và trùng route: deepseek-v4-pro (shadow cũ) từng TRÙNG KHÍT cấu hình deepseek-reasoner (official)
  - [EXPECTED_BEHAVIOR] wan-2.7 / pplx-embed-v1 / cohere-rerank-4-pro KHÔNG phải model thừa — kiểm điểm ĐỌC trước khi gọi là mồ côi (RM-20)
  - [EXPLORATORY_PREDICTIVE_SIGNAL] MT ngày 04/09: bạch thủ 28 lọt anti-trap FULL_SPENT và số voter khai 4 nhưng nguồn phân biệt ≤3
  - [INDETERMINATE] Bằng chứng cứu/phá của từng model quá nhỏ để xếp hạng vòng đời

## CHUA TRA LOI DUOC

**1. Thành viên combo-super ở MB ngày 04/09 — INDETERMINATE.** Nhật ký 04/09 in dòng `UNIFIED` cho MN (dòng 3242) và MT (dòng 8721) nhưng KHÔNG in cho MB, và MB cũng không có lượt trace gọi lại nào. Vì thế tôi không xác định được combo-super MB gồm những model nào, nên không đo được trùng cha mẹ cho bundle 829. Không suy đoán để lấp chỗ trống.

**2. Ảnh hưởng của việc đếm phiếu trùng nguồn lên CON SỐ ĐƯỢC CHỌN — chưa đo.** Cơ chế đã chứng minh, nhưng để biết nó có đổi bạch thủ hay không thì phải chạy lại bộ chọn với phiếu đã gộp theo nguồn, trên nhiều tháng. Ba miền một ngày là n=3 — RM-04: chưa được phép kết luận.

**3. Phép bỏ-một-model chỉ là bậc MỘT.** Tôi trừ điểm của model khỏi `score_breakdown` đã lưu, KHÔNG mô phỏng lại `pp1_convergence_dampener`, cổng bt/wr, `max_voters_cap` (MT chỉ giữ top-13), hay việc bỏ một model có thể kéo model khác lọt vào. Nên các con số cứu/phá là ước lượng thô, không phải phản thực tế đầy đủ.

**4. Hai dòng dưới nền chưa đủ để gọi là đã chứng minh.** `glm-5.2` [−13,1; −0,5] và `smart-ml` [−13,2; −1,0] có CI hoàn toàn âm, nhưng tôi chạy 34 phép so nên kỳ vọng ~1,7 dương tính giả ở mức 95%; chưa hiệu chỉnh đa biến. Chỉ `gemma-4-31b` [−21,9; −6,1] là vững — và model đó đã nghỉ. Không đề xuất hành động nào lên `glm-5.2` hay `smart-ml` từ số này.

**5. Sự kiện 13/04 — chưa dựng lại được cổng đương thời.** Ba model shadow/retired bỏ phiếu vào bundle official qua `run_source='manual'` là SỰ THẬT đo được, nhưng tôi không truy được code ngày 13/04 để biết lúc đó `manual` có được phép vào bundle hay không. Không gọi là vi phạm khi chưa chứng minh được chính sách đương thời (RM-13).

**6. Lineage của ba tổ hợp cũ.** `ensemble-2models` (4 dòng), `ensemble-3models` (13 dòng), `combo-ai-3models` (9 dòng) — đều từ 29/01–13/02/2026. Không quét ra được hàm nào còn định nghĩa chúng, nên trường parent/lineage ghi `KHONG_CHUNG_MINH_DUOC` chứ không đoán theo tên (RM-10).

**7. Bằng chứng chi phí của việc combo-super gọi lại.** Trace 04/09 có `cost_es