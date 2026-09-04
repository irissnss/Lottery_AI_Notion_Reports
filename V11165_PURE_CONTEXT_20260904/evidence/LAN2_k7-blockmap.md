# k7-blockmap · tang=EVIDENCE_COMPLETE

## TOM TAT

GATE 7 xong — đã mapping ĐỦ 12 nhóm khối lịch sử + P07 + RULEBOOK §11 (14 nhóm), mỗi nhóm đọc mã THẬT đang serve rồi đo trên DUMP THẬT 57 tổ hợp ngày 04/09 (RM-14), nền đo lại trên clone bất biến read-only (RM-13/RM-21). Kết quả nặng nhất: cổng «ngữ cảnh thuần» CONTEXT_ONLY_V2 chỉ gác được 1,5/14 nhóm — 12 nhóm còn nguyên ở CẢ 33/33 lượt của làn ngữ cảnh, trong đó có BLOCK_ORACLE P07 («ĐỀ XUẤT PYTHON: 02 (score=13), 28 (score=13)» + «SỐ NÊN TRÁNH 11 số» + «AI KHÔNG NÊN chọn») 57/57 lượt. Phase 19 «TRÍ TUỆ TỰ HỌC» KHÔNG có cổng nào và là chỗ chuỗi «weight=» sống sót 933 lần / câu «→ Ưu tiên yếu tố có WR cao nhất» 57/57 — tức V11150 gỡ Phase 14A rồi để mở cửa bên cạnh (A58_VIOLATION_HALF_DONE). Ba phép đo mới đổi kết luận: (a) EVIDENCE TABLE xếp hạng 988/988 dòng có n<10 và số dòng «100%» quan sát được KHÔNG vượt kỳ vọng do nền ở cả ba miền (nền 92,01/84,66/65,10%; kỳ vọng 31,0/19,9/5,6 bucket vs bảng in 10/10/4) — xếp hạng không mang thông tin; (b) 76/76 dòng khai «3 rules» đều là MỘT miền nguồn và có MỘT GIẢI CHUNG ở cả ba luật ⇒ hội tụ là đếm một tiếng nói ba lần; (c) nhãn COLD/OVER_HOT của P07 được ngẫu nhiên thuần sinh ra ở quy mô 22,4 và 18,8 đuôi/ngày. Sửa đủ 14 nhóm gỡ 7.757–8.289 ký tự/lượt official (14,8–15,5%) và 6.491–7.068 ký tự/lượt shadow (11,8–12,3%) — tức «ngữ cảnh thuần» KHÔNG chủ yếu là chuyện cắt độ dài. Hai nhóm KHÔNG phải lỗi: nhóm 1 (sorted[:12]) ĐÃ được vá từ V11105/V11106 — 114/114 dòng nay là số đếm, tiền đề của Gate 7 mục 1 đã cũ; nhóm 12 (lịch sử đài) là khối gần RAW_NUMBER_FACT nhất, có cutoff `date &lt; ?` thật.

## BLOCKER

Chưa đạt READY_FOR_OWNER_SHADOW_DEPLOY vì Gate 7 mới là MAPPING + ĐO: chưa viết một dòng mã vá nào, chưa có candidate patch trong artifacts/, chưa chạy phép kiểm nào trên bản đã sửa. Mỗi nhóm đã có sẵn phép kiểm máy chạy được (trường `phep_kiem`) nhưng tất cả đang ở trạng thái CHƯA CHẠY vì chưa có mã để kiểm. Ba việc phải làm trước khi lên được tầng kế tiếp: (1) viết candidate patch dạng TỆP MỚI trong artifacts/ cho ít nhất P07 + nhóm 7 + nhóm 5 (ba việc nặng nhất, và nhóm 5 phải đụng ĐỦ ba module ngoài trong cùng một lần theo §60.2); (2) dump lại prompt từ ba hàm đang serve với patch nạp trong sandbox rồi chạy đủ 14 phép kiểm, kèm thử chặn RM-15 cho cổng de-herding mới; (3) OWNER LOCK hiện tại vẫn ghi MODEL_ACTION = BLOCKED · PROMPT_43_R1 = PARTIAL, và mọi thay đổi prompt official cần owner ký — cấm tự nâng tầng.

## TRA LOI

Gate 7 hỏi: với MỖI nhóm trong 12 nhóm khối lịch sử — đọc mã thật, đo trên dump thật, rồi ghi disposition + cách chuyển đổi cụ thể; kèm P07 và RULEBOOK §11; mỗi nhóm có trước/sau, số ký tự đổi, và phép kiểm máy chạy được. Đã làm đủ 14/14, ghi vào artifacts/v11165_k7_block_mapping.json.

DISPOSITION theo nhóm (kèm số ký tự gỡ trung bình mỗi lượt, đo bằng cách cắt đúng dòng/khối khỏi payload thật):
1. D-1 tail pool → DROP hai dòng số đếm + CHUYỂN `fresh_carry[:6]` thành condition · 266 ký tự · EXPECTED_BEHAVIOR (phần `sorted[:12]` ĐÃ vá từ V11105/V11106, 114/114 dòng nay là số đếm)
2. EVIDENCE TABLE → DROP xếp hạng, thay bằng MỘT dòng condition có nền + n + KTC · 910 ký tự · PROVEN_DEFECT (988/988 dòng n<10; số dòng 100% không vượt kỳ vọng do nền ở cả ba miền)
3. OWNER ANTI-TRAP → GIỮ raw prior-region, DROP thang FRESH>PARTIAL>FULL + 5 dòng quyết định · 994 ký tự · PROVEN_DEFECT
4. CONVERGENCE → TRANSFORM: khử trùng theo đài/giải, báo SỐ NGUỒN ĐỘC LẬP, bỏ `conv_bonus` · 1.017 ký tự · PROVEN_DEFECT (76/76 dòng '3 rules' là một nguồn)
5. GAN/HOT/COLD → DROP ở ĐỦ BA MODULE ngoài (statistical_analyzer + feature_engineering + metrics_calculator) · 1.012 ký tự · PROVEN_DEFECT
6. Phase 11 → DROP luôn ở official (đã DROP sẵn ở làn ngữ cảnh) · 39 ký tự · PROVEN_DEFECT
7. Phase 14A + Phase 19 → DROP CẢ HAI, không chỉ 14A · 990 ký tự (official 1.639–1.701 · shadow 483–545) · PROVEN_DEFECT
8. MB HARD MODE → GIỮ phần độ khó/nền (MB 1 đài/ngày, trần 55%), DROP 3 dòng tên model + WR · 42 ký tự (126 ở MB) · PROVEN_DEFECT
9. Python Top-5 / FE / KB → DROP KB + DROP TOP 5 GỢI Ý + DROP TOP POSITIONS; FE giữ được phần đối xứng toàn vũ trụ nếu kèm n và cutoff · 973 ký tự · PROVEN_DEFECT
10. Ký hiệu thủ công → DROP (0/19 lượt có định nghĩa; tool calling không bật nên model không tra được) · 243 ký tự (728 ở MB) · PROVEN_DEFECT
11. Lịch sử chính model → TRANSFORM: thêm `date < ?`, bỏ dòng WR n=7 và mệnh lệnh 'hãy thay đổi chiến lược' · 275 ký tự · PROVEN_DEFECT
12. Lịch sử đài → KEEP (có cutoff thật, đúng miền/đài); sửa hai chỗ nhỏ · 324 ký tự · EXPECTED_BEHAVIOR
P07 → DROP toàn bộ, ƯU TIÊN SỐ 1 · 628 ký tự · PROVEN_DEFECT
RB11 → DROP câu 'KHÔNG tự tạo số mới…' + 'nên có trong top-2' + sửa §13 · 213 ký tự · PROVEN_DEFECT

TỔNG nếu làm hết: official gỡ 7.757–8.289 ký tự/lượt (14,8–15,5%, 153–161 dòng) · shadow gỡ 6.491–7.068 ký tự/lượt (11,8–12,3%, 122–130 dòng).

MỖI NHÓM ĐỀU CÓ PHÉP KIỂM MÁY trong artifact, dạng assert trên DUMP (không grep mã), ví dụ P07: assert 'ĐỀ XUẤT PYTHON' not in payload and 'SỐ NÊN TRÁNH' not in payload and 'AI nên ưu tiên' not in payload and 'ưu tiên Python metrics' not in (system+user) trên CẢ 57 payload; nhóm 8 kèm THỬ CHẶN RM-15: chèn khối giả '### X — claude-opus-4-6: 99% WR' vào ctx_pack ⇒ de-herding phải gỡ nó, rồi khôi phục nguyên trạng.

ĐỐI CHIẾU CHÍN MỤC TIÊU OWNER: nhóm P07 + 5 + 9 vi phạm mục tiêu 1 và 3 (đưa rổ số đã lọc/xếp hạng rồi bảo model 'tự chọn'); RB11 + nhóm 10 vi phạm mục tiêu 2 (cấm model tự khoanh vùng / đưa ký hiệu model không giải nghĩa được); nhóm 7 + 8 vi phạm mục tiêu 5 (dùng tên model, win rate, trọng số để đẩy LLM bắt chước nhau); nhóm 10 vi phạm mục tiêu 6 (đưa ký hiệu cần tra trong khi tool calling không bật ở bất kỳ model nào); nhóm 2 + 9 + 11 vi phạm mục tiêu 7 (phép tính không có schema nguồn / không có nền / không có cutoff); nhóm 2 + 3 + 4 vi phạm mục tiêu 8 (ĐIỀU KIỆN bị viết thành KHUYẾN NGHỊ SỐ). Chỉ nhóm 12 thoả gần đủ định nghĩa PURE CONTEXT.

## PHAT HIEN
  - [PROVEN_DEFECT] P07 BLOCK_ORACLE — prompt đưa thẳng ĐÁP ÁN, có mặt cả ở làn «ngữ cảnh thuần»
  - [PROVEN_DEFECT] Phase 19 «TRÍ TUỆ TỰ HỌC» KHÔNG có cổng — chỗ «weight=» sống sót qua làn ngữ cảnh thuần
  - [PROVEN_DEFECT] EVIDENCE TABLE — xếp hạng «100%» không vượt nền, và mâu thuẫn với chính câu ngưỡng trong cùng prompt
  - [PROVEN_DEFECT] GAN/HOT/COLD — V11001/V11007 chỉ gỡ phía gpt_analyzer, BA MODULE NGOÀI vẫn bơm mọi lượt
  - [PROVEN_DEFECT] Hội tụ đếm THÔ: 76/76 dòng khai «3 rules» thật ra là MỘT nguồn nhìn từ ba lát cắt chồng nhau
  - [PROVEN_DEFECT] RULEBOOK §11 — một câu đóng cửa mục tiêu owner số 2, có mặt 57/57
  - [PROVEN_DEFECT] KNOWLEDGE BASE đóng băng 130 ngày, không ghi mốc, và MÂU THUẪN với khối sống trong CÙNG một prompt
  - [PROVEN_DEFECT] Ký hiệu thủ công G4#3 / FIRST2 / HEAD_TAIL / TAIL_HEAD / LAST2 / D-3 — 0/19 lượt có định nghĩa
  - [PROVEN_DEFECT] Phase 15 (lịch sử của chính model) KHÔNG có mốc cutoff trong SQL — 57/57 dump có dòng ĐÚNG ngày dự đoán
  - [PROVEN_DEFECT] De-herding mù lần THỨ HAI: MB HARD MODE + MB Ceiling lọt, và các khối ở user payload thì về nguyên tắc không bao giờ với tới
  - [PROVEN_DEFECT] OWNER ANTI-TRAP — thang FRESH > PARTIAL_SPENT > FULL_SPENT là KHUYẾN NGHỊ, không phải điều kiện
  - [EXPECTED_BEHAVIOR] Nhóm 1 (D-1 tail pool) — tiền đề của Gate 7 mục 1 ĐÃ CŨ: `sorted(...)[:12]` không còn trong mã đang serve
  - [EXPECTED_BEHAVIOR] Nhóm 12 (lịch sử đài) là khối SẠCH NHẤT — giữ, chỉ sửa hai chỗ nhỏ
  - [OPERATIONAL_IMPROVEMENT] Cổng CONTEXT_ONLY_V2 chỉ gác 1,5/14 nhóm — và sửa ĐỦ 14 nhóm chỉ gỡ ~15% payload

## CHUA TRA LOI

1. PHASE 15 CÓ RÒ Ở PRODUCTION LÚC CHỐT KHÔNG — INDETERMINATE. Đã chứng minh được: SQL không có mệnh đề `date < date_str`, và 57/57 dump chứa một dòng mang đúng ngày dự đoán. CHƯA chứng minh được: lúc job t10_chot chạy (MN 15:40 · MT 16:55 · MB 17:55) thì bản ghi cùng ngày của CHÍNH miền đó đã có `status` chưa — cần một cột thời điểm chấm (đã liệt kê cột bảng predictions nhưng chưa dựng phép đo thời điểm ghi status vs mốc chốt). Dump là REPLAY sau khi kết quả đã về nên KHÔNG dùng làm bằng chứng cho production.
2. GỠ 14 NHÓM CÓ LÀM TĂNG ĐỘ TRÚNG KHÔNG — KHÔNG ĐO, VÀ CẤM HỨA (mục tiêu owner số 9 + RM-03). Gate 7 chỉ chứng minh các khối này không thoả định nghĩa PURE CONTEXT của owner và một số khối không mang thông tin trên nền. Không có bất kỳ phép đo tiến nào ở đây.
3. NHÓM 10 CHỈ ĐO ĐƯỢC PHÍA MB. Neo '### 🔵 MN RULE STACK' và '### 🔵 MT RULE STACK' trả về 0 kết quả trên dump 04/09 ⇒ khối MANUAL của MN/MT không có mặt ngày đó. Chưa biết chúng bật ở điều kiện nào — cần quét thêm ngày khác trước khi kết luận cho MN/MT.
4. CHỈ MỘT NGÀY (2026-09-04). Mọi con số theo lượt (57 tổ hợp) đều của một ngày. Các đại lượng phụ thuộc dữ liệu — số dòng EVIDENCE TABLE, số đuôi CONV, n mỗi bucket — sẽ đổi theo ngày. Riêng phần cấu trúc (khối nào có cổng, khối nào không, câu lệnh nào có mặt) không phụ thuộc ngày.
5. TRUY VẤN THEO THỨ KHÔNG CÓ `HAVING evals>=3`: quét 30 ngày × 3 miền chưa gặp ca n<3 lọt top-8 ⇒ đây là RỦI RO CẤU TRÚC đã chứng minh trong mã, chưa phải ca thật đã xảy ra. Ghi đúng như vậy, không nâng thành PROVEN.
6. DÒNG '## CHỈ SỐ ĐỊNH LƯỢNG' trong bảng độ phủ de-herding là HIỆN VẬT CỦA CÁCH CẮT KHỐI (khối chạy tới tiêu đề ##/### kế tiếp nên nuốt cả Phase 15/19/14A/station history). Đã ghi chú thẳng vào artifact để người đọc sau không đọc nhầm; hai dòng còn lại (MB HARD MODE, MB Ceiling) là tiêu đề '### ' thật.
7. CHƯA KIỂM: sau khi gỡ 14 nhóm thì còn câu lệnh nào trong prompt trỏ vào các khối đã gỡ không (PRJ_PROMPT_DANGLING). Phải quét ngược có PHÂN LOẠI (RM-09) SAU khi có patch, không phải bây giờ.