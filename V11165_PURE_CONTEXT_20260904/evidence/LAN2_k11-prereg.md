# k11-prereg · tang=EVIDENCE_COMPLETE

## TOM TAT

GATE 11 (PROSPECTIVE_MEASUREMENT_PREREG_DRAFT) đã xong hai đầu ra: `artifacts/v11165_k11_prereg.json` (28.621 byte, sha256_16 `744c43f676474389`) trên VPS và `E:\Lottery_AI_Notion_Reports\V11165_PURE_CONTEXT_20260904\PROSPECTIVE_MEASUREMENT_PREREG_DRAFT.md` (37.235 byte, 559 dòng). Nhãn: `PROVISIONAL_AGENT_PROPOSED_DRAFT` — CẤM Owner-lock.

VIỆC ĐẦU TIÊN (đọc verdict T-B đã tồn tại) đã làm trọn, tái lập TỪ ĐẦU trên clone bất biến, không trích lại báo cáo. Tái lập ĐÚNG: n=346 · b=51 · c=50 · 101 cặp bất đồng · WR CONTROL 33,53% vs T-B 33,24% · z=-0,0995. PHÁN QUYẾT theo đúng ngưỡng V11059 khoá 11/08: T1 (≥96) ĐẠT · T3 (≥14 ngày) ĐẠT · T2 (|z|≥1,96) KHÔNG ĐẠT ⇒ `NO_ANOMALY_FOUND` — nhưng CHỈ trong phạm vi MDE ≈ 8,04 pp.

BỐN ĐIỀU CHƯA AI ĐỌC, cả bốn đổi cách hiểu phép đo:
① NỀN — cả hai nhánh đều KHÔNG khác nền ở cả ba miền (|z| max = 1,42). Con số gộp «33,24% vs 33,53%» là trung bình của BA nền khác nhau (MB 23,90% · MT 34,52% · MN 43,15%).
② SỨC MẠNH — n=96 sinh từ công thức `(1,96/(2ψ-1))²` THIẾU số hạng z_β ⇒ ~50% sức mạnh. Đúng phải 194 cặp cho power 80%. Sức mạnh thực tế đạt được tại m=101 chỉ 52%.
③ SÀN NHIỄU — «đổi 70,2% số chọn» phải đọc cạnh 61,3%: gọi LẠI cùng model AI đã cho top-1 khác 61,3% số lượt. Cùng bậc độ lớn.
④ Ô NHIỄM — sáu ổ còn nguyên trong mã ĐANG SERVE ở CẢ HAI nhánh; `gpt_analyzer.py:3191` («ưu tiên số xuất hiện trong NHIỀU nguồn») KHÔNG bị `CONTEXT_ONLY_V2` gỡ.

Đã hoà giải đủ 5 bộ ngưỡng cũ (QD-017 · V11059 · TOTAL_V2 25/08 · V11153 · V11161) thành bảng «ngưỡng nào của bản nào, đo trên thước nào, còn dùng không, vì sao». KHÔNG tái sử dụng mù một ngưỡng nào.

## BLOCKER

Chưa thể `READY_FOR_OWNER_SHADOW_DEPLOY` vì BA chặn, theo thứ tự phải xử:

① **CANDIDATE chưa tồn tại.** Bản nháp định nghĩa sáu cổng `K-C1…K-C6` (dump từ hàm đang serve · 0 chuỗi cấm · 0 mệnh lệnh ưu tiên số · mọi CONDITION có schema nguồn · 0 dangling · 0 tự mâu thuẫn) nhưng CHƯA có một prompt nào đạt cả sáu. Phiên này CẤM sửa tệp đang serve và CẤM gọi provider LLM thật, nên không thể dựng và thử CANDIDATE. Không có CANDIDATE thì không có gì để shadow-deploy.

② **`gpt_analyzer.py:6738` chưa vá.** `_shadow_mode = lane_test_shadow_pack or (selected_model in SHADOW_GATE_MODELS)` còn sống ⇒ gpt-oss-120b (OFFICIAL) nhận gói ngữ cảnh SHADOW. Nhánh CONTROL của phép đo mới vì thế KHÔNG đồng nhất giữa các model official. Đây là điều kiện huỷ số 3 và số 5 của chính bản nháp — phải xử TRƯỚC ngày bắt đầu.

③ **Vân tay payload chưa đủ phủ.** Cổng `O7` đòi coverage ≥ 99% mới được bắt đầu đếm ngày; vân tay `runtime_prompt_sha256` hiện hành chỉ phủ 43,59% (thiếu 26.478–35.315 ký tự/lượt). Bản vá ứng viên `_v11165_van_tay_payload.py` đã có nhưng ở trạng thái `CODED_AND_TESTED_NOT_RUNTIME_PROVEN`, chưa deploy.

Ngoài ba chặn kỹ thuật: bản này là `PROVISIONAL_AGENT_PROPOSED_DRAFT`, owner chưa ký một ngưỡng nào, và `QD-073` (owner lock 23:14 04/09) vẫn giữ `MODEL_ACTION = BLOCKED` · `POOL_VERDICT = HOLD` · `MT_PREREGISTRATION = NOT_READY_FOR_OWNER_LOCK`.

## TRA LOI

**Câu hỏi trung tâm của gate 11 — «phép đo T-B đã tồn tại nói lên điều gì?» — trả lời trọn vẹn:**

Nó nói: **theo đúng ngưỡng V11059 đã khoá ngày 11/08 trước khi có số, không có bằng chứng prompt ba tầng khác prompt official.** T1 (≥96 cặp bất đồng) đạt với 101 · T3 (≥14 ngày) đạt với 25 · T2 (|z|≥1,96) không đạt với 0,0995. Vì T1 đã đạt, đây là **kết luận NULL hợp lệ**, không phải RM-04 «chưa được phép kết luận».

Nhưng nó **chỉ nói được điều đó trong phạm vi MDE ≈ 8,04 pp** — và bốn điều sau, chưa báo cáo nào ghi, giới hạn phạm vi đó hẹp hơn nữa:

1. **Nền.** Cả hai nhánh đều không khác mức chọn ngẫu nhiên một đuôi, ở cả ba miền (|z| lớn nhất 1,42). Đây là phép so giữa hai nhánh **đều đang ở mức ngẫu nhiên**, không phải giữa hai nhánh «đang hoạt động».
2. **Sức mạnh.** Ngưỡng 96 sinh từ công thức thiếu z_β ⇒ ~50% sức mạnh. Sức mạnh thực đạt được 52%.
3. **Sàn nhiễu.** «Đổi 70,2% số chọn» phải đọc cạnh 61,3% — tỉ lệ đổi top-1 khi chỉ **gọi lại** cùng model. Cùng bậc độ lớn.
4. **Ô nhiễm.** Sáu ổ còn ở **cả hai** nhánh; T-B chỉ ngắn hơn CONTROL 13,0%.

**Vì vậy nó TUYỆT ĐỐI KHÔNG nói «pure context không có tác dụng».** Nó chỉ nói: *«xếp lại ba tầng mà vẫn giữ rõ số chọn sẵn thì không khác — trong phạm vi 8pp, trên một thiết kế 52% sức mạnh, giữa hai nhánh đều ở mức ngẫu nhiên».*

**Về phép đo mới:** thiết kế ghép cặp (model × miền × ngày) như V11059, nhưng **bốn nhánh** — thêm `CONTROL′` (gọi lại prompt official, nhánh A/A) làm nhánh **bắt buộc**, vì không có nó thì mọi con số «đổi X% số chọn» đều không đọc được. Ba nhóm chỉ số đăng ký trước: Operational (`O1…O7`, đọc sớm được) · Reasoning (`R1…R5`, đọc sớm được) · Predictive (`P2…P5`, **cấm đọc sớm**), McNemar chính xác hai phía, Holm phiên bản hoá `HOLM_V11165_R1`, nền hypergeometric riêng từng miền, ngày đọc cố định 30 và 65.

**Về sức mạnh — con số thẳng thắn nhất của bản này:** với 15 lượt/ngày, power 80%, α=0,05 hai phía, VIF=1,0 bảo thủ — **5 pp cần ~61 ngày · 3 pp cần ~169 ngày · 2 pp cần ~381 ngày**. Muốn kết luận trong một tháng thì hiệu ứng phải **≥ ~7 pp**. Đó là thực tế toán học, không phải một lựa chọn có thể thương lượng.

**Về hoà giải ngưỡng cũ:** đã lập đủ bảng 5 dòng (QD-017 · V11059 · TOTAL_V2 25/08 · V11153 · V11161) — ngưỡng nào của bản nào, đo trên thước nào, còn dùng không, vì sao. **Không tái sử dụng mù một ngưỡng nào.** Cấm mang sang: VIF 2,92 · VIF 0,889 · n=96 · ngưỡng V11161 (đo thước `TOTAL ranked[0]`, khác thước này).

## PHAT HIEN
  - [NO_ANOMALY_FOUND] VERDICT T-B: NO_ANOMALY_FOUND — nhưng chỉ trong phạm vi MDE ≈ 8,04 pp
  - [PROVEN_DEFECT] n = 96 của V11059 là con số 50% SỨC MẠNH — công thức thiếu số hạng z_beta
  - [PROVEN_DEFECT] NỀN chưa ai đọc: CẢ HAI nhánh đều KHÔNG khác mức chọn ngẫu nhiên, ở cả ba miền
  - [SUSPICIOUS_NEEDS_MORE_EVIDENCE] «Đổi 70,2% số chọn» phải đọc cạnh sàn nhiễu 61,3% — phần quy cho prompt là nhỏ
  - [PROVEN_DEFECT] Sáu ổ ô nhiễm còn nguyên trong mã ĐANG SERVE, ở CẢ HAI nhánh — và CONTEXT_ONLY_V2 không gỡ mâu thuẫn M1
  - [PROVEN_DEFECT] VIF phụ thuộc THƯỚC chứ không chỉ phụ thuộc LANE — cùng lane, cùng cụm, chênh gấp đôi
  - [PROVEN_DEFECT] «z = -0,10 · p = 1,00» của làn sóng 1 trộn HAI phép McNemar khác nhau
  - [EXPECTED_BEHAVIOR] Hoà giải «101/96»: số 96 là NGƯỠNG đăng ký trước, không phải một phép đo
  - [OPERATIONAL_IMPROVEMENT] Hai sàn cặp bất đồng đang mâu thuẫn: T1 = 96 gộp (QD-017) vs 30 mỗi miền (V11153)
  - [SUSPICIOUS_NEEDS_MORE_EVIDENCE] Chiều hiệu ứng T-B ĐẢO DẤU giữa các model — thêm một lý do cấm đọc số gộp
  - [PROVEN_DEFECT] gpt_analyzer.py:6738 còn sống ⇒ nhánh CONTROL của phép đo mới CHƯA phải official thuần

## CHUA TRA LOI

1. **KTC95 `[-5,49; +4,90]` của làn sóng 1 không tái lập chính xác.** Tái lập ra `[-5,68; +5,10]` (VIF 0,894) hoặc `[-5,99; +5,41]` (không VIF). Điểm ước lượng (-0,289 pp) và z tái lập ĐÚNG; chỉ khoảng tin cậy lệch. Không truy được làn sóng 1 dùng VIF/SE nào (0,867 cũng không tái lập). **Kết luận không đổi** — cả ba khoảng đều ôm 0 — nhưng con số phải rút lại theo `PRJ-RETRACTION-001`.

2. **VIF = 0,867 sinh từ đâu.** Đã thử 7 định nghĩa cụm × thước (ngày · ngày×miền · ngày×model · miền · model, trên thước ghép cặp và thước một nhánh), không định nghĩa nào cho 0,867. Gần nhất 0,894.

3. **Sàn nhiễu THẬT.** Con số 61,3% lấy từ combo-super gọi lại model cha; **chưa chứng minh được đầu vào lần gọi lại giống từng byte** với lần gọi gốc. Nên nó là xấp xỉ trần trên, không phải sàn nhiễu đo trực tiếp. Chỉ nhánh `CONTROL′` (A/A) mới trả lời được — và phiên này cấm gọi provider LLM thật.

4. **Tỉ lệ cặp bất đồng của CANDIDATE.** Bảng n cần dùng 29,19% đo trên T-B. CANDIDATE khác T-B nhiều hơn nên tỉ lệ này có thể cao hơn (⇒ n cần giảm). Không đoán được trước khi CANDIDATE tồn tại; bản nháp buộc đo lại sau 14 ngày đầu và báo cáo, nhưng **cấm sửa ngưỡng**.

5. **Số token.** VPS chưa cài tokenizer (`tiktoken`), nên mọi số về token là `INDETERMINATE` — chỉ báo được ký tự và byte. Kế thừa từ làn sóng 1, không xử được trong phiên này.

6. **Chín mục tiêu owner có ánh xạ đủ sang sáu cổng `K-C` không.** Đã ánh xạ 1→ML thuần toán (ngoài phạm vi prompt), 2/3/4→K-C2+K-C4, 5→K-C2, 6→K-C4, 7→K-C4, 8→K-C3, 9→mục V.3. Nhưng **chưa có owner xác nhận** ánh xạ này đúng ý — đây là diễn giải của agent, và theo `A60_VIOLATION_LAYER_CONFLATED` phải ghi rõ nó là `CODE_DID`/đề xuất chứ không phải `OWNER_SAID`.

7. **`SHAM` arm có đáng chạy không.** Bản nháp để nó là tuỳ chọn vì chưa tính được chi phí/lợi ích: nó là nhánh duy nhất tách được «bỏ rõ số» khỏi «xếp lại cấu trúc», nhưng thêm một nhánh làm bài toán đa so sánh nặng thêm. Chờ owner quyết.