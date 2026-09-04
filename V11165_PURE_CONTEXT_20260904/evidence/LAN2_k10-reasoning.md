# k10-reasoning · tang=CODED_AND_TESTED_NOT_RUNTIME_PROVEN

## TOM TAT

GATE 10 đã CÓ BỘ ĐO và SÁU PHÉP METAMORPHIC chạy được trên dữ liệu thật, tự kiểm 31/31 đạt (15 phép cho bộ đo + 16 phép cho metamorphic, mỗi phép đều có ca SẠCH và ca GÀI VI PHẠM theo RM-15). Đã áp lên đủ 60 lượt ngày 04/09 (27 official + 33 shadow).

PHÁT HIỆN LỚN NHẤT KHÔNG NẰM Ở BỘ ĐO MÀ Ở CHUẨN ĐỂ ĐO: prompt đã phục vụ ngày 04/09 KHÔNG TÁI DỰNG ĐƯỢC. Vân tay runtime khớp 0/60 lượt. Quét độ sâu thống kê 7..180 ngày không bản render nào tái lập được khối TOP-5 mà model trích dẫn — ví dụ ba model của BA NHÀ CUNG CẤP KHÁC NHAU (glm-5.2, gemini-3.5-flash, gemini-3.6-flash) cùng ghi "39: 77.7pt, WARM, UP, #2" cho MT, mà chuỗi "77.7" không tồn tại trong bất kỳ bản render nào. Ba model độc lập không thể bịa ra cùng một bộ bốn (số + giá trị + hạng + zone) ⇒ chuỗi đó CÓ THẬT trong prompt đã gửi, và hệ thống KHÔNG lưu bản prompt đó (chỉ lưu sha256 phủ ~43,6%). Mọi thước cần đối chiếu prompt (M01/M03/M06) vì thế có sẵn một lỗi không khử được.

Phát hiện phụ nhưng nặng: hai làn đang được đem so với nhau KHÔNG cùng cửa sổ thống kê — official (scheduler.py:4245-4255) bị find_optimal_window ghi đè xuống 15/30/30 ngày, shadow (scheduler.py:7356) dùng thẳng setting 60 ngày không ghi đè. Cộng thêm roster model khác hẳn (8 token-model vs 11 shadow-model), phép so "CONTEXT_ONLY_V2 vs LEGACY_PROMPT" đang đổi ít nhất BA biến cùng lúc.

Kết quả metamorphic đáng chú ý nhất: MR5 cho thấy 117 tỉ lệ trong prompt chỉ có 14 (11,97%) kèm nền tường minh — tức "đổi nền" không làm payload đổi gì, model KHÔNG THỂ đánh giá lại sức mạnh bằng chứng; MR3 cho thấy đổi TOÀN BỘ số trong source_data bằng một song ánh thì chỉ 3/27 khối mang số biến đổi theo.

Tôi cũng phải tự rút lại: bản V1 của chính bộ đo này đếm 59 mâu thuẫn và 15 lỗi số học — đọc tay thì hầu hết là dương tính giả (chuỗi "reason_not_main" chứa chữ "main"; "21/08" là NGÀY; "56/39" là CẶP SỐ ỨNG VIÊN). Sau khi siết còn 4 và 0.

## BLOCKER

Ba blocker, xếp theo thứ tự phải gỡ. Không cái nào gỡ được trong phiên này.

BLOCKER 1 — KHÔNG CÓ BẢN LƯU PROMPT ĐÃ PHỤC VỤ (chặn cứng, phải gỡ đầu tiên)
Hệ thống chỉ lưu runtime_prompt_sha256 phủ ~43,6% payload; không lưu nguyên văn. Re-render từ hàm đang serve trên clone bất biến khớp 0/60 lượt, và không độ sâu nào từ 7 đến 180 ngày tái lập được giá trị mà ba model độc lập cùng trích dẫn. Chừng nào chưa lưu, mọi con số M01/M03/M06 đều có lỗi nền không khử được và không được dùng làm căn cứ quyết định (RM-17).
Việc phải làm: ghi nguyên văn payload cuối (system+user) cho từng lượt, hoặc tối thiểu sha256 phủ 100%; ghi kèm statistical_depth thực tế của từng lượt vào trace. Cần owner duyệt vì đụng vào đường ghi của tiến trình đang serve.

BLOCKER 2 — HAI LÀN KHÔNG CÙNG CỬA SỔ THỐNG KÊ (chặn mọi kết luận nhân quả)
scheduler.py:4245-4255 (official) bị find_optimal_window ghi đè xuống 15/30/30; scheduler.py:7356 (shadow) dùng thẳng setting 60, không ghi đè. Cộng roster model khác hẳn (8 token-model vs 11 shadow-model), phép so pure-context đang đổi ba biến cùng lúc. Phải chốt một biến một lần (QD-018) trước khi bất kỳ con số so sánh nào được ghi là kết quả.

BLOCKER 3 — CẤM GỌI LLM THẬT (chặn vế model của cả sáu phép metamorphic)
MR1..MR6 mới kiểm được payload có biến đổi đúng không. Vế "model có phản ứng đúng không" — tức phần trả lời được mục tiêu owner số 1, 3, 5 — chỉ chạy được khi owner duyệt shadow deploy. Mã đã chừa sẵn, không phải viết lại.

Ngoài ra, hai điều kiện tiên quyết về nội dung prompt phải sửa trước khi đo model, nếu không phép đo sẽ không phân biệt được suy luận với bám neo:
- 88% tỉ lệ trong prompt không có nền (MR5) ⇒ không có gì để model đánh giá lại sức mạnh bằng chứng.
- 24/27 khối mang số không biến đổi theo source_data (MR3), trong đó có khối lặp lại chính những sự kiện đã có trong source_data qua một đường đọc DB riêng ⇒ nếu Gate 11 lọc source_data để làm pure-context thì các khối này sẽ âm thầm bơm lại dữ liệu chưa lọc, đúng lỗi làm nửa vời của V11001.

## TRA LOI

VIỆC 1 — bộ đo không cần outcome: XONG. 13 thuộc tính theo đúng danh sách yêu cầu, cộng M00 (độ tin cậy của chính phép đối chiếu) mà tôi phải thêm vì nếu không có nó thì mọi con số M01/M03/M06 đều vô nghĩa. Mỗi thuộc tính có định nghĩa chính xác viết trong docstring, cách tính deterministic trên văn bản, và một phép kiểm trên dữ liệu thật chứng minh chạy được. Không thuốc nào nhìn kết quả xổ số; không thuốc nào chấm bằng "lời văn trôi chảy" (M01 đòi NEO NGUỒN có thật trong prompt, không đòi văn hay; M03 đòi con số khớp nguồn; M04 đòi nhất quán nội tại).

VIỆC 2 — sáu phép metamorphic: XONG ở vế renderer, KHÔNG làm được ở vế model.
1. Đổi thứ tự raw facts → HỎNG: đúng một đại lượng ('Cross shift') là sản phẩm của thứ tự liệt kê.
2. Đổi nhãn giả → ĐẠT: không đuôi nào chỉ sống nhờ nhãn (89 = 89).
3. Hoán vị số nguồn → HỎNG: chỉ 3/27 khối mang số biến đổi theo; 16 khối DỮ LIỆU và 8 khối CHÍNH SÁCH đứng yên. Đây là câu trả lời quan trọng nhất của VIỆC 2: đổi dữ liệu nguồn thì rổ số model nhìn thấy hầu như không nhúc nhích.
4. Xoá một condition → HỎNG nhẹ: 1 mệnh lệnh thật sẽ mồ côi (KNOWLEDGE BASE), 4 tham chiếu còn lại vô hại.
5. Đổi nền giữ hit rate → HỎNG: 88% tỉ lệ không có nền, nên phép biến đổi vô nghĩa ngay từ prompt.
6. Cùng condition khác miền → INDETERMINATE: 9 khối dùng chung hằng số nhưng đều là văn bản chính sách; câu hỏi thật đã bị (5) chặn trước.

Giới hạn đã nói rõ trong docstring của module và trong ketqua.json: không gọi LLM nên chỉ kiểm được payload có đổi đúng không, KHÔNG kiểm được model có phản ứng đúng không. Thiết kế đã chừa sẵn để khi owner duyệt shadow deploy thì bộ đo chạy thẳng trên output thật.

VIỆC 3 — áp lên 60 lượt 04/09: XONG. Đo được 12/13 thuộc tính; M10 đo được 35/60 (25 lượt thiếu candidate_support_map); M02 KHÔNG ÁP DỤNG ĐƯỢC 60/60 vì prompt hiện tại không đánh số điều kiện nào — đúng như yêu cầu đã lường trước, và bản thân nó là một phát hiện.

TRẢ LỜI THẲNG CHO GATE 10 ("lập luận có tốt hơn không"): CHƯA TRẢ LỜI ĐƯỢC, và lý do không nằm ở bộ đo mà ở chuẩn để đo. Ba rào theo đúng thứ tự phải gỡ:
(1) Prompt đã phục vụ không tái dựng được → mọi thước cần prompt có lỗi nền không khử được.
(2) Hai làn đang so với nhau khác nhau ở ít nhất ba biến (chế độ prompt / cửa sổ 15 vs 60 / roster model) → không quy được nhân quả cho chế độ prompt.
(3) Prompt hiện tại không cho model điều kiện có định danh và 88% mệnh đề không có nền → ngay cả khi gọi model thật, phép đo cũng không phân biệt được model suy luận hay model bám neo.
Nói cách khác: SỬA PROMPT LÀ ĐIỀU KIỆN CẦN TRƯỚC KHI ĐO MODEL, chứ không phải đo model rồi mới biết prompt có vấn đề.

## PHAT HIEN
  - [PROVEN_DEFECT] Prompt đã phục vụ 04/09 KHÔNG tái dựng được — bộ đo không có chuẩn để bám vào
  - [PROVEN_DEFECT] Hai làn official/shadow dùng CỬA SỔ THỐNG KÊ KHÁC NHAU — confound của chính phép so pure-context
  - [PROVEN_DEFECT] MR5 — 88% tỉ lệ trong prompt KHÔNG có nền, nên 'đổi nền' là phép biến đổi vô nghĩa
  - [OPERATIONAL_IMPROVEMENT] MR3 — đổi TOÀN BỘ số nguồn bằng một song ánh, chỉ 3/27 khối mang số biến đổi theo
  - [PROVEN_DEFECT] M02 — prompt không đánh số điều kiện nào, nên đường suy luận của model không kiểm được
  - [PROVEN_DEFECT] MR1 — một đại lượng thống kê trong prompt là sản phẩm của THỨ TỰ LIỆT KÊ đài, không phải của dữ liệu
  - [PROVEN_DEFECT] MR4 — một mệnh lệnh phụ thuộc khối sẽ mồ côi nếu gỡ KNOWLEDGE BASE
  - [EXPLORATORY_PREDICTIVE_SIGNAL] Làn CONTEXT_ONLY_V2 trên MN tụ hơn làn LEGACY cùng ngày — tín hiệu, CHƯA ĐƯỢC PHÉP KẾT LUẬN
  - [SUSPICIOUS_NEEDS_MORE_EVIDENCE] 65 ca CHÉP SAI SỐ trong trích dẫn của model — có thật nhưng bị nhiễu bởi lỗi nền M00
  - [NO_ANOMALY_FOUND] MR2, M05, M06, M13 — bốn kết quả ÂM thật, không có bất thường
  - [PROVEN_DEFECT] TỰ RÚT LẠI — bản V1 của chính bộ đo này đếm chuỗi thô và cho 59 mâu thuẫn + 15 lỗi số học giả

## CHUA TRA LOI

1. PHẢN ỨNG CỦA MODEL — nửa quan trọng của cả sáu phép metamorphic. Phiên cấm gọi provider LLM thật, nên MR1..MR6 chỉ kiểm được VẾ RENDERER (payload có biến đổi đúng không), KHÔNG kiểm được VẾ MODEL (model có bám thứ tự / nhãn / số cũ / điều kiện đã xoá / nền / miền hay không). Mỗi phép đều trả về trường `gioi_han` ghi rõ điều này. Chế độ `model` đã chừa sẵn: khi owner duyệt shadow deploy, chỉ cần gọi cùng hàm với renderer thật rồi so output hai nhánh bằng chính bộ thước VIỆC 1, không phải viết lại gì.

2. NGUYÊN NHÂN của việc prompt 04/09 không tái dựng được. Đã loại trừ được: sai độ sâu thống kê (quét 7..180 ngày), sai source_data (tái lập đúng logic scheduler), thiếu as-of cutoff trên lottery_results (statistical_analyzer.py:71 có `date < target_date` và dữ liệu ≤03/09 không đổi), sai learned_intelligence (code hai làn giống hệt). CHƯA xác định được biến nào còn lại đã đổi. Hai giả thuyết: (a) một producer khác đọc trạng thái thay đổi theo thời gian, (b) ba model của ba nhà cung cấp cùng bịa ra một bộ bốn giống hệt. (b) rất khó tin nhưng tôi KHÔNG có bằng chứng loại trừ nó, nên ghi INDETERMINATE cho nguyên nhân — bản thân hiện tượng thì đã chứng minh.

3. Khoảng lệch ~1.400 ký tự có hệ thống giữa bản re-render làn shadow và runtime_prompt_chars trong trace (official chỉ lệch 16–124). Đã kiểm và loại trừ: độ sâu, source_data, learned_intelligence. Chưa quy được về đâu.

4. MR6 — câu hỏi thật ("mỗi mệnh đề có dùng nền của MIỀN nó không") KHÔNG trả lời được, vì MR5 đã cho thấy 88% mệnh đề không có nền nào cả nên không còn gì để so theo miền. 9 khối bị MR6 gắn cờ đều là văn bản chính sách tĩnh, không phải nền. Ghi INDETERMINATE, không ghi "phát hiện nền dùng chung".

5. Trong 65 ca CHÉP SAI SỐ, không tách được phần do model chép sai với phần do bản đối chiếu lệch (hệ quả trực tiếp của M00=0/60). Chỉ nói được: các ca lệch 0,1–0,3 trên cùng một cấu trúc là dấu hiệu chép sai thật.

6. Nguyên nhân của việc làn CONTEXT_ONLY_V2 tụ hơn trên MN. Ba biến đổi cùng lúc (chế độ prompt / cửa sổ 15 vs 60 / roster 8 vs 11 model) và n = một ngày một miền. Không quy được nhân quả, và cũng chưa tính được cỡ mẫu cần.

7. M10 chỉ đo được 35/60 lượt; 25 lượt không có trường candidate