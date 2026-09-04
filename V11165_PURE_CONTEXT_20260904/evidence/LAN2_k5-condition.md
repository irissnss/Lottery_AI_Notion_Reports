# k5-condition · tang=EVIDENCE_COMPLETE

## TOM TAT

GATE 5 — CONDITION_CONTRACT hoàn tất. Đọc lại 35 producer từ kiểm kê lần sóng 1 (KHÔNG đo lại), dựng hợp đồng 24 trường, áp 12 nguyên tắc chuyển đổi cho từng producer, ra bảng đối chiếu đủ 35 dòng: 17 producer sinh ra 17 điều kiện, 18 producer bị DROP/BLOCK.

Đóng góp mới của lần sóng 2 là ĐO NỀN — vì không có nền thì không điều kiện nào hợp lệ (nguyên tắc 6), và lần sóng 1 đã đo được chỉ 1/35 producer có nền tường minh. Đo trên clone bất biến (sha256 khớp neo, chattr +i còn nguyên), mode=ro:

• Nền T1 (bạch thủ) W180: MN 0,4298 · MT 0,3509 · MB 0,2374 — lệch gần gấp đôi giữa MN và MB. Nền T2 (bộ k đuôi) cho k=2..20, đối chiếu cả nền đo thật lẫn 1−(1−b)^k (|lệch| ≤ 0,9pp, nên RM-18 dùng công thức được, miễn dùng b đúng miền).
• k thật của luật: MN 3,96 · MT 3,70 · MB 2,52.
• Nền khớp từng dòng cho họ điều kiện LUẬT, tách TRONG/NGOÀI cửa sổ chọn, design effect đo riêng cho chính thước này (KHÔNG mượn 2,92 hay 0,867).

Ba con số quyết định: dòng prompt MN in "6W(42d):265/288=92%" có nền khớp 84,4%; MB in "65%" có nền 47,3%. Mười hai dòng "6/6=100.0%" mà prompt in như bằng chứng mạnh nhất — MN quan sát 32 ô đạt 100%, kỳ vọng dưới nền 25,0; MB quan sát 4, kỳ vọng 3,55. Câu "12 tuần trúng 12/12" lặp 4 lần trong một khối: kỳ vọng 12,6/105 luật đạt được hoàn toàn do may rủi ở MN.

Tự sửa trong phiên: hai con số tôi tự suy ra ban đầu SAI — "P(≥6/8) = 0,98" (đúng: 0,8845) và nền k=4 của C-RULE-04 (tôi trộn nhầm cột xấp xỉ với cột đo thật). Đã tính lại, sửa, và buộc mọi giá trị lấy thẳng từ JSON đo được để không trôi lại.

KHÔNG sửa một dòng mã nào đang serve, không deploy, không ghi DB production.

## BLOCKER

Verdict là EVIDENCE_COMPLETE chứ KHÔNG phải READY_FOR_OWNER_SHADOW_DEPLOY vì bốn chặn, theo thứ tự phải gỡ:

CHẶN 1 — KHÔNG CÓ MÃ. Gate 5 sinh ra HỢP ĐỒNG + BẢNG ĐỐI CHIẾU + BẢNG NỀN, không sinh candidate patch nào. Không có gì để shadow-deploy. Ghi CODED_AND_TESTED_NOT_RUNTIME_PROVEN sẽ là tự nâng tầng (RM-12) vì không có dòng mã nào được viết hay thử.

CHẶN 2 — THƯỚC ĐANG DÙNG LÀ THƯỚC HỎNG, PHẢI SỬA TRƯỚC. Lần sóng 1 đo được: vân tay runtime_prompt_sha256 chỉ phủ 39,81–48,07% payload (tb 43,59%), bắt 2/11 phép đột biến; bộ 5 dấu ô nhiễm (_dau_o_nhiem, gpt_analyzer.py:6712) báo 0/5 «sạch» trong khi payload thật còn weight= (33/33 lượt) và Best MB model (11/33); _V10768_HERD_SECTION_KEYS (gpt_analyzer.py:4598) chỉ 4 chuỗi khớp header '### ' nên bỏ sót '### 🔴 MB HARD MODE' — LẦN THỨ HAI cùng họ lỗi (V11106 đã vá ca MB MODEL RANKING). Deploy bản mới rồi đo bằng cổng mù thì mọi kết luận sau đó vô nghĩa.

CHẶN 3 — GỠ NỬA CHỪNG SẼ TÁI PHẠM ĐÚNG LỖI V11001 (§60.1). 13/35 producer đi kèm mệnh lệnh (NT-07), và ít nhất ba mệnh lệnh được LẶP ở hai chỗ: 'SỐNG MẠNH → ưu tiên tuyệt đối' có ở cả khối dữ liệu (L652) lẫn RULEBOOK §19 (L980); 'CONV×3 win rate thấp hơn average' có ở cả L600 lẫn RULEBOOK §23 mục 8. Gỡ số mà giữ mệnh lệnh trỏ vào nó là A58_VIOLATION_HALF_DONE.

CHẶN 4 — HỢP ĐỒNG CHƯA CÓ CỔNG MÁY. Không có script nào kiểm một điều kiện có đủ 24 trường trước khi vào prompt, và chưa có thử chặn (giả lập vi phạm ⇒ thoát ≠ 0; trạng thái sạch ⇒ thoát 0). Theo RM-15, cổng chưa qua thử coi như KHÔNG TỒN TẠI — ở đây thậm chí chưa dựng.

NGOÀI RA, quyết định owner QD-073 đang khoá: OUTPUT_COUNTERFACTUAL_RANK_PRODUCTION_WRITE = FORBIDDEN · MODEL_ACTION = BLOCKED · MT_PREREGISTRATION = NOT_READY_FOR_OWNER_LOCK. Gate này không đụng vào các khoá đó và không đề nghị mở khoá nào.

## TRA LOI

CÂU HỎI GATE 5: dựng quy tắc chuyển BỘ SỐ thành ĐIỀU KIỆN, áp cho 35 producer, ra bảng đối chiếu 35 dòng.

TRẢ LỜI — 35 producer chia thành 10 disposition (dùng nguyên từ vựng động lần sóng 1):
TRANSLATE_TO_NEUTRAL_CONDITION 10 · DROP_MODEL_META 6 · DROP_UNSUPPORTED 5 · DROP_DUPLICATE 4 · RENDER_FULL_UNIVERSE_SYMMETRICALLY 3 · KEEP_RAW_FACT 2 · BLOCK_AMBIGUOUS 2 · BLOCK_ORACLE 1 · EXPOSE_VIA_REAL_QUERY_TOOL 1 · SHADOW_HYPOTHESIS_ONLY 1. Tổng 35.
⇒ 17 producer sinh ra điều kiện · 18 bị DROP/BLOCK · 17 điều kiện được định nghĩa đủ 24 trường.

17 ĐIỀU KIỆN:
C-RAW-01 kết quả ngày trước, đầy đủ đài/giải (bỏ cắt [:3]) · C-RAW-02 lịch sử đài raw (bỏ phần 'top=' vì đó là top-k trá hình)
C-UNIV-01 bảng đuôi 00-99 tần suất/khoảng vắng/theo thứ, thứ tự cố định — THAY THẾ P01+P04+P05 · C-UNIV-02 cờ đảo gương toàn universe · C-UNIV-03 đuôi×giải đối xứng — nuốt cả P20
C-STAT-01 độ dốc xu hướng (HYPOTHESIS_ONLY) · C-STAT-02 đồng xuất hiện cặp, BẮT BUỘC kèm số phép so 4.950 và ngưỡng sau hiệu chỉnh
C-RULE-01 mệnh đề luật kèm nền khớp + tách cửa sổ chọn · C-RULE-02 hit_any theo cửa sổ, cấm in trần · C-RULE-03 nguồn×giải kèm hiệu chỉnh bội — nuốt P27 · C-RULE-04 bối cảnh sự kiện, PHẢI đổi thứ tự sang trung tính — nuốt P22 · C-RULE-05 hội tụ = rủi ro bầy đàn · C-RULE-06 độ sống nguồn, BỎ mệnh lệnh 4 bậc · C-RULE-07 kho luật MB
C-SPEND-01 miền ra trước — giữ SỰ KIỆN, bỏ nhãn FRESH/SPENT và bỏ xếp hạng · C-TOOL-01 truy vấn pool D-1 (UNAVAILABLE — chưa có tool) · C-SHADOW-01 lag-1 spillover, CHỈ lane shadow

BỐN CHỖ CẤM TÁI SINH DƯỚI BẤT KỲ DẠNG ĐIỀU KIỆN NÀO:
• P07_ĐỀ XUẤT PYTHON (BLOCK_ORACLE) — prompt đưa sẵn ĐÁP ÁN đúng dạng hợp đồng đầu ra (main+secondary kèm score) rồi HAI mệnh lệnh ép model ưu tiên nó (SYSTEM_PROMPT §5b gpt_analyzer.py:337-341 và metrics_calculator.py:635). Đây là RECOMMENDATION, không phải CONDITION — vi phạm trực tiếp nhất mục tiêu owner #3 và #8.
• P18/P19 KNOWLEDGE BASE (BLOCK_AMBIGUOUS) — nguồn đóng băng từ 2026-04-26 00:45:54 nhưng VẪN ĐƯỢC ĐỌC MỖI LƯỢT, và mâu thuẫn trực tiếp với P17 trong CÙNG MỘT prompt. RM-20 ngược lại: đây không phải bảng chết, đây là NGUỒN CHẾT MÀ VẪN ĐƯỢC ĐỌC — nguy hiểm hơn bảng chết.
• 6 producer DROP_MODEL_META (P06/P10/P13/P31/P32/P35) — NT-10 bỏ tuyệt đối. P10 và P35 hiện CÓ MẶT ở cả lane 'ngữ cảnh thuần'.

BA KHUÔN MẪU ĐÃ ĐÚNG SẴN TRONG KHO — không cần dựng lại từ đầu:
① Đoạn tự phủ định dump MN L554–L555 (đúng nguyên tắc 6, nhưng PHẠM VI sai — không phủ 12 dòng 100.0% nằm bên dưới)
② Câu hội tụ = rủi ro bầy đàn dump MN L685 (đúng nguyên tắc 9)
③ V11105/FU-419 bỏ sorted(d1_union)[:12] chỉ giữ số đếm (đúng nguyên tắc 2)

## PHAT HIEN
  - [PROVEN_DEFECT] 31/35 producer bơm số vào prompt mà KHÔNG kèm nền — nguyên tắc 6 bị vi phạm nhiều nhất
  - [PROVEN_DEFECT] Con số prompt in ra bị đọc sai theo CẢ HAI CHIỀU vì thiếu nền khớp
  - [PROVEN_DEFECT] Mười hai dòng '6/6=100.0%' là điều may rủi gần như chắc chắn sinh ra — không phải bằng chứng
  - [PROVEN_DEFECT] Đoạn tự phủ định ĐÚNG đã tồn tại — nhưng phạm vi của nó loại trừ đúng chỗ cần nó nhất
  - [PROVEN_DEFECT] Nhãn 'SỐNG MẠNH' gần như là trạng thái MẶC ĐỊNH ở MN nhưng hiếm ở MB — cùng một ngưỡng 6/8 cho cả ba miền
  - [PROVEN_DEFECT] Tách TRONG/NGOÀI cửa sổ chọn tái hiện đúng hình của RM-18 — trên một thước KHÁC
  - [INDETERMINATE] Luật có hiệu quả ngoài cửa sổ chọn hay không — CHƯA ĐƯỢC PHÉP KẾT LUẬN
  - [PROVEN_DEFECT] Nhãn nói ngược với nội dung ngay dòng kế tiếp — hai chỗ, đều nguyên văn
  - [PROVEN_DEFECT] Hội tụ 'CONV×4' đếm bốn LUẬT, không phải bốn NGUỒN — chứng minh trực tiếp trên dump
  - [OPERATIONAL_IMPROVEMENT] Nền lệch gần gấp đôi giữa các miền — hợp đồng nay buộc nền gắn chết vào miền + thước
  - [PROVEN_DEFECT] C-TOOL-01 phải mang evidence_status = UNAVAILABLE: không model nào bật tool calling
  - [OPERATIONAL_IMPROVEMENT] Ngân sách token cho render đối xứng 00-99 — đo được, và rẻ hơn cái nó thay thế

## CHUA TRA LOI

1. BỎ BỚT BỘ SỐ CÓ LÀM TĂNG ĐỘ TRÚNG KHÔNG — CHƯA ĐO. Đây là mục tiêu owner #9 và là câu quan trọng nhất. Gate này chỉ dựng hợp đồng và đo NỀN; không có một phép đo tiến nào. 17 điều kiện mới là thiết kế trên giấy, chưa có bản chạy. Không được đọc bất kỳ con số nào trong gate này thành «bản mới tốt hơn».

2. LUẬT CÓ HIỆU QUẢ NGOÀI CỬA SỔ CHỌN KHÔNG — CHƯA ĐƯỢC PHÉP KẾT LUẬN. n=20/miền trên 4 ngày (RM-04). Điểm ước lượng âm cả ba miền nhưng KTC95 đều chứa 0. Cấm viết theo cả hai hướng.

3. KHÔNG ĐIỀU KIỆN NÀO TRONG 17 ĐẠT PROSPECTIVE_SUPPORTED. Phân bố: RAW_FACT 2 · MECHANICALLY_DERIVED 3 · RETROSPECTIVE_ONLY 6 · HYPOTHESIS_ONLY 5 · UNAVAILABLE 1. Đây là kết quả, không phải thiếu sót của bản kiểm kê.

4. DANH SÁCH 35 PRODUCER CÓ ĐỦ KHÔNG — KHÔNG CHẮC. Lần sóng 1 đã ghi DC-03 «phạm vi chưa phủ». Bằng chứng cụ thể rằng danh sách có thể còn thiếu: P34_MB_RULE_STACK đã BỊ BỎ SÓT một vòng vì gate của nó đọc biến môi trường nằm trong .env chứ không trong /proc/<PID>/environ — chỉ phát hiện được vì đã DUMP THẬT. Có thể còn producer khác cùng dạng.

5. 3-CÀNG (NT-12) CHƯA KIỂM trong gate này — số 0 là do không có dữ liệu trong tập 35 producer, KHÔNG phải do đã đạt.

6. 2.421/5.035 LƯỢT ĐÁNH GIÁ KHÔNG TÁCH ĐƯỢC trong/ngoài cửa sổ chọn vì rule_id không còn trong mined_rules. Đã tách riêng nhãn KHONG_RO_mined_at, không gộp vào kết luận — nhưng nghĩa là gần một nửa dữ liệu lịch sử nằm ngoài phép tách.

7. NỀN CHO TRỤC «TIÊU HAO» (FRESH/PARTIAL_SPENT/FULL_SPENT của C-SPEND-01) CHƯA ĐO RIÊNG. Phép đo liên quan gần nhất là FU-316 (V11076): model chọn đuôi thấp 20,2% vs nền 21,0%, z=−1,01 ⇒ không neo. Nhưng đó là thước khác, và RM-21 cấm mượn.

8. HỢP ĐỒNG CHƯA CÓ CỔNG MÁY. Không có script nào kiểm được rằng một điều kiện mới có đủ 24 trường trước khi vào prompt. Theo RM-15, cổng chưa thử chặn được coi như không tồn tại — ở đây thậm chí chưa có cổng.