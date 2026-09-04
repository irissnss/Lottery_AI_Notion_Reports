# k14-deploy · tang=CODED_AND_TESTED_NOT_RUNTIME_PROVEN

## TOM TAT

GATE 14 xong cả ba việc. VIỆC 1: gói deploy/rollback cho 8 hạng mục (6 vá + cổng + module), mỗi hạng mục có tệp/dòng/trước-sau/test/rủi ro/thứ tự/cách kiểm/cách gỡ/điều kiện dừng, và ghi rõ cái nào độc lập cái nào phụ thuộc. VIỆC 2: viết mã sinh artifact đo lường MT đúng phương án B, chạy thật trên 90 ngày MT — 2.635 dòng, 2,45 MB, chmod 0444, 13/13 kiểm độc lập + 15/15 tự kiểm ĐẠT. VIỆC 3: PURE_CONTEXT_CANDIDATE = BLOCKED_WITH_EXACT_REASONS, 6 blocker + 1 indeterminate.

Ba việc đáng chú ý nhất, đều là chỗ suýt sai: (1) bản nháp patch B của làn sóng 1 gọi hai ký hiệu KHÔNG TỒN TẠI trong mã đang serve — nếu deploy sẽ làm mất sạch vân tay, tệ hơn hiện trạng; đã sửa để suy route từ năm cờ boolean có thật. (2) Bản r1 artifact của chính tôi lặp lại đúng bẫy NULL-hai-nghĩa mà nó tuyên bố sửa (prompt_version rỗng 50,4% không kèm lý do) — đã bắt và vá ở r2. (3) Phép đo SC-08 đầu tiên của tôi kết luận "7/8 cửa sổ không có dữ liệu" là SAI do một mẫu regex bỏ sót cách viết `2W(14d)`; kiểm lại bằng 8 cách viết mới ra kết luận đúng (7W/8W trống, sáu cửa sổ còn lại chỉ có một dòng tổng hợp) — kết luận CHẶN vẫn đứng nhưng lý do khác hẳn.

Mutation ledger: 0 ghi DB · 0 deploy · 0 restart · 0 sửa tệp đang serve. neo558 = NGUYÊN, 4 bảng khoá không đổi, PID 3370750 / NRestarts 0 không đổi, output_counterfactual_rank vẫn 0/17121.

## BLOCKER

PURE_CONTEXT_CANDIDATE = BLOCKED_WITH_EXACT_REASONS — 6 blocker:

(1) SC-02 hash coverage < 100% — vân tay hiện phủ 39,81-48,07% (tb 43,59%), thiếu 26.478-35.315 ký tự/lượt, bắt 2/11 phép đột biến. Vá VA-B đã code+test, CHƯA deploy.
(2) SC-07 routing vẫn phụ thuộc selected_model — gpt_analyzer.py:6738 còn `or (selected_model in SHADOW_GATE_MODELS)`; gpt-oss-120b (OFFICIAL) nhận gói ngữ cảnh shadow. Vá VA-A đã code+test+thử chặn hai chiều, CHƯA deploy.
(3) SC-12 MT cấp vẫn bị tính là gate failure — main.py:9840 gộp một tập cho hai việc; artifact đo được 122 dòng cấp có ý vs 38 dòng trượt cổng. Vá VA-h12 đã 30/30 test + replay 45 dòng, CHƯA deploy.
(4) SC-04 candidate vẫn có preselected basket — lane CONTEXT_ONLY_V2 đang chạy vẫn còn 5 dấu rổ-chọn-sẵn mỗi miền (official 6). Không vá nào trong gói này gỡ được; cần renderer.
(5) SC-05 condition không truy được về raw source/cutoff — 35 producer: 27 bơm AGGREGATED_NUMBER_SET, 2 RAW_NUMBER_FACT, chỉ 1/35 có nền tường minh. CONDITION_CONTRACT v1.0 đã có nhưng production chưa áp.
(6) SC-08 model bị yêu cầu làm việc không có phương tiện để làm — mệnh lệnh quét 8 cửa sổ, nhưng 7W/8W có 0 dòng số liệu ở cả 6 dump, sáu cửa sổ còn lại chỉ có một dòng tổng hợp không theo ứng viên, và không có tool-calling ở bất kỳ model nào.

Cộng 1 INDETERMINATE: SC-10 — 'UCC' không có định nghĩa nào trong kho (12 tệp khớp chỉ vì là chuỗi con của 'SUCCESS'), không đánh giá được, cần owner chỉ rõ.

Chặn nền tảng đứng trên tất cả: MT_PREREGISTRATION = NOT_READY_FOR_OWNER_LOCK và POOL_VERDICT = HOLD. Kể cả gỡ hết 6 blocker kỹ thuật, phép đo vẫn chưa được phép kết luận. Và chưa ai từng đo một prompt thoả đủ chín điều kiện owner đặt ra — lane ba tầng T-B so 'prompt production' với 'prompt production đã xếp lại ba tầng', không phải so với pure context.

## TRA LOI

CÂU HỎI: PURE_CONTEXT_CANDIDATE = READY_FOR_OWNER_SHADOW_DEPLOY hay BLOCKED_WITH_EXACT_REASONS?

TRẢ LỜI: BLOCKED_WITH_EXACT_REASONS. 6 blocker, 1 indeterminate, 6 không chặn.

Chia làm hai nhóm rất khác nhau về cách gỡ:

NHÓM A — ba blocker ĐÃ CÓ VÁ, chỉ chờ owner ký deploy:
· SC-02 → VA-B (vân tay 43,59% → 100%)
· SC-07 → VA-A (bịt rò gói ngữ cảnh)
· SC-12 → VA-h12 (kế toán MT)
Cả ba đã code, đã test, đã có gỡ về chính xác, đã có thử chặn RM-15.

NHÓM B — ba blocker là BẢN CHẤT của prompt production, không vá nào trong gói này gỡ được:
· SC-04 rổ số chọn sẵn (lane 'thuần ngữ cảnh' vẫn còn 5 dấu/miền)
· SC-05 điều kiện không truy được về nguồn (1/35 producer có nền tường minh)
· SC-08 mệnh lệnh trỏ vào dữ liệu không có (7W/8W trống ở cả 6 dump)
Ba cái này cần PURE_CONTEXT_RENDERER + preregistration được owner khoá, tức là một work package riêng.

Và trên tất cả: MT_PREREGISTRATION = NOT_READY_FOR_OWNER_LOCK. Kể cả khi gỡ hết 6 blocker kỹ thuật thì phép đo vẫn chưa được phép kết luận, vì chưa có ngưỡng nào được đăng ký trước.

Ba việc suýt sai mà tôi tự bắt được, xin nêu thẳng vì chúng đổi kết luận:
1. Bản nháp patch B của làn sóng 1 nếu deploy nguyên trạng sẽ làm MẤT SẠCH vân tay (gọi hai ký hiệu không tồn tại, NameError bị except nuốt) — tệ hơn hiện trạng chứ không phải cải thiện.
2. Bản r1 artifact của chính tôi lặp lại đúng bẫy NULL-hai-nghĩa mà nó tuyên bố sửa; đã vá ở r2.
3. Phép đo SC-08 đầu tiên của tôi sai vì đếm chuỗi bằng một mẫu duy nhất (RM-09); kết luận CHẶN vẫn đứng nhưng lý do khác hẳn — đã ghi phần rút lại vào cả artifact lẫn báo cáo.

## PHAT HIEN
  - [PROVEN_DEFECT] Bản nháp patch B của làn sóng 1 KHÔNG deploy được — gọi hai ký hiệu không tồn tại
  - [PROVEN_DEFECT] `hang_cua_no_trong_A` NULL 973/973 là BẤT KHẢ THI VỀ CẤU TRÚC, không phải thiếu dữ liệu
  - [PROVEN_DEFECT] Bản artifact phương án B đang có cắt cụt top-10, mất dữ liệu ở 71/90 ô MT
  - [PROVEN_DEFECT] SC-08 — prompt ra lệnh quét 8 cửa sổ nhưng 7W/8W không có một dòng số liệu nào
  - [PROVEN_DEFECT] TỰ RÚT LẠI trong chính phiên: phép đo SC-08 đầu tiên của tôi sai vì đếm chuỗi bằng một mẫu duy nhất
  - [PROVEN_DEFECT] Bản r1 artifact MT của chính tôi lặp lại đúng bẫy NULL-hai-nghĩa mà nó tuyên bố sửa
  - [PROVEN_DEFECT] Rò gói ngữ cảnh shadow vào lượt official VẪN SỐNG; ba điểm mù khác của cổng cũng vậy
  - [OPERATIONAL_IMPROVEMENT] Cổng V11160 mù đúng nửa ctx_pack — đo được, không phải suy đoán
  - [OPERATIONAL_IMPROVEMENT] Artifact MT tách được CẤP CÓ Ý khỏi TRƯỢT GATE mà không cần đụng production
  - [INDETERMINATE] SC-10 — 'UCC' không có định nghĩa nào trong kho, không đánh giá được
  - [SUSPICIOUS_NEEDS_MORE_EVIDENCE] SC-09 — truncation hiện rất hiếm nhưng prompt thuần-ngữ-cảnh dài hơn nên rủi ro tăng
  - [EXPECTED_BEHAVIOR] Bốn điều kiện dừng KHÔNG chặn — có bằng chứng, không phải mặc định qua
  - [EXPECTED_BEHAVIOR] Kết quả gate 9 thay đổi giữa phiên — con số 5 TRƯỢT tôi đọc lúc đầu đã bị thay thế

## CHUA TRA LOI

1. SC-10 / UCC — không đánh giá được. 'UCC' không tồn tại như một định nghĩa trong kho: quét toàn bộ web/backend + artifacts ra 12 tệp, tất cả chỉ khớp vì UCC là chuỗi con của 'SUCCESS'. RM-10 cấm kết luận theo tên đoán. CẦN OWNER chỉ rõ UCC là gì, hoặc tên thật của hợp đồng đầu ra cần kiểm tương thích.

2. Truncation trên prompt thuần-ngữ-cảnh ở quy mô — INDETERMINATE. Đo được 3/6.533 = 0,046% trên prompt HIỆN TẠI, nhưng prompt thuần-ngữ-cảnh dài hơn 3.000-3.400 ký tự ở cả ba miền và chưa từng chạy ở quy mô. Không có cách nào biết trước tỉ lệ truncation của bản mới mà không chạy thật (mà chạy thật thì cần owner ký).

3. Đối chiếu với nhánh CONTROL của lane A/B — không làm được. Bảng prompt_3tang_ab_shadow_v11059 chỉ lưu SỐ KÝ TỰ (control_prompt_ky_tu), không lưu văn bản control. Nên không thể dump lại và so từng khối với nhánh đối chứng. Đây là giới hạn dữ liệu, không phải giới hạn phương pháp.

4. Hành vi model thật với prompt thuần ngữ cảnh — chưa đo được, và trong phiên này KHÔNG ĐƯỢC PHÉP đo (luật cứng cấm gọi provider). Nhóm G của bộ thử k9 chỉ kiểm VALIDATOR, không kiểm hành vi model. Mọi kết luận về 'prompt thuần ngữ cảnh cho output tốt hơn' đều chưa có một dòng bằng chứng nào.

5. Hiệu ứng thật của từng vá lên chất lượng dự đoán — chưa đo được vì chưa deploy. Tất cả những gì phiên này chứng minh là: vá làm ĐÚNG điều nó nói (bản vá 7/7 cổng, replay đổi đúng 45 dòng, dump ctx còn 1 bản thay vì 2). Không có gì chứng minh output tốt lên. RM-12: đây là tầng CODED_AND_TESTED, không phải RUNTIME_PROVEN, càng không phải PREDICTIVE_IMPROVEMENT_PROVEN.

6. Con số '46/72 quy cho cấp' của làn sóng trước — KHÔNG TÁI LẬP ĐƯỢC, phải rút lại. Số tái lập được là 45 ngày cấp giải thích trọn vẹn, hoặc 70 ngày có cấp tham gia. Tôi chưa truy được vì sao ra 46, nên chỉ ghi là không tái lập được chứ không đoán.

7. Bộ CONTAM-V2 có bắt đúng hơn bộ 5 dấu cũ trên MỌI payload hay không — chưa đủ bằng chứng để khuyến nghị deploy. Nó đúng hơn trên các mẫu đã thử, nhưng nó ĐỔI NGHĨA một cột đang ghi hằng ngày (runtime_prompt_contam_hits), nên rủi ro nằm ở ngữ nghĩa chứ không ở kỹ thuật. Tôi đề nghị ghi ra cột MỚI, giữ cột cũ để so — nhưng chưa làm việc đó trong phiên này.