# k6-threelayer · tang=EVIDENCE_COMPLETE

## TOM TAT

GATE 6 xong hai deliverable, khong viet ma nao, khong dung production.

DAC TA BA TANG — gan tang cho ca 35 producer, suy TU disposition da do o Gate 4 (khong gan tay):
TANG_1_FACTS 6 (P01 P09 P14 P16 P17 P29) · TANG_2_CONDITIONS 10 (P04 P15 P21 P23 P24 P25 P26 P28
P30 P34) · LOAI 18 · NGOAI_HOP_DONG 1 (P33, chi lane shadow).

TU DINH CHINH TRONG PHIEN: ban nhap dau cua toi tu dung mot khuon CONDITION 12 truong. SAI —
Gate 5 cung lan song da chot CONDITION_CONTRACT 24 truong + 17 dieu kien. Dung khuon thu hai la
tao chong tang moi (§60). Da RUT khuon 12 truong, dac ta nay nay TRO sang Gate 5 va chi them DUNG
HAI rang buoc dung lai tu vung cua Gate 5.

HE QUA NANG NHAT khi ghep luat Tang 3 voi kiem ke Gate 5: 0/17 dieu kien dat PROSPECTIVE_SUPPORTED
=> duoi hop dong de xuat, model CHI duoc rut so tu 5/17 dieu kien (RAW_FACT 2 +
MECHANICALLY_DERIVED 3). 12 dieu kien con lai duoc phep xuat hien nhu du kien nhung CAM lam can cu
uu tien so.

SO XUNG DOT — lap NAM xung dot, khong phai ba: ba cai gate neu, cong hai cai do ra trong luc lap
so (XD-04 verdict mo vs bo hien thi nhi phan · XD-05 secondary ba luat ba ten). Da de xuat MOT
contract duy nhat (PURE-CONTEXT-OUTPUT-1.0.0-DRAFT) kem ba phuong an va cai gia tung cai; chon PA-3
"tach KIENG NHUONG khoi CHAN SO".

PHAT HIEN LON NHAT — CAP5_INPUT_NOT_READY la AM TINH GIA cua bo doc, khong phai thieu du lieu:
near_miss_shortlist co that trong reasoning_json (1.371 dong, 3.774 phan tu); hop nhat voi
main_numbers dat DUNG 5 so o 610 dong. Bo doc CAP5 tra nham COT (analysis_text) va danh sach 9 ten
khoa KHONG co near_miss_shortlist.

## BLOCKER

CHƯA thể lên READY_FOR_OWNER_SHADOW_DEPLOY, và cũng CHƯA đạt CODED_AND_TESTED_NOT_RUNTIME_PROVEN — vì Gate 6 chỉ sinh ĐẶC TẢ và SỔ XUNG ĐỘT, KHÔNG viết dòng mã nào. Đó là đúng phạm vi gate yêu cầu, không phải thiếu sót.

BỐN THỨ CHẶN, theo thứ tự phải gỡ:

1. GRAIN `near_miss_shortlist` CHƯA ĐỊNH NGHĨA — chặn thi hành XD-03. Prompt định nghĩa nó là TẬP BỊ LOẠI (gpt_analyzer.py:786), không phải HẠNG 3–5; 33,8% dòng trùng với main_numbers. Không định nghĩa grain + dedupe + quy tắc gán rank thì sửa bộ đọc CAP5 sẽ đẻ ra lỗi đếm hai lần (đúng họ consensus_level ở L10).

2. THƯỚC ĐO CÒN HỎNG (L5) — phải vá TRƯỚC khi đo bất cứ gì: vân tay runtime_prompt_sha256 chỉ phủ 43,59% trung bình; bộ 5 dấu ô nhiễm `_dau_o_nhiem` (gpt_analyzer.py:6712) mù cấu trúc, báo 0/5 «sạch» trong khi payload thật còn `weight=` ở 33/33 lượt; cổng _v11160_test_lane.py mù với nửa ctx_pack. Đo bằng dụng cụ hỏng thì mọi kết luận vô hiệu.

3. RÒ SHADOW VÀO OFFICIAL VẪN SỐNG (L4) — gpt_analyzer.py:6738 còn `_shadow_mode = lane_test_shadow_pack or (selected_model in SHADOW_GATE_MODELS)`, khiến gpt-oss-120b (OFFICIAL) nhận gói ngữ cảnh SHADOW ở 88/88 lượt official trong 30 ngày. Không vá thì không lấy official làm control được.

4. OWNER CHƯA KHOÁ CONTRACT ĐỀ XUẤT. `PURE-CONTEXT-OUTPUT-1.0.0-DRAFT` mới là ĐỀ XUẤT. Theo OWNER LOCK 23:14 04/09 thì MODEL_ACTION = BLOCKED và MT_PREREGISTRATION = NOT_READY_FOR_OWNER_LOCK, nên gate này KHÔNG được tự nâng tầng. Việc thi hành PA-3 đòi sửa 4 điểm bơm độc lập + bộ hiển thị TRONG CÙNG MỘT PHIÊN (§60.2) — sửa lẻ là A58_VIOLATION_HALF_DONE.

## TRA LOI

CÂU HỎI TRỌNG TÂM CỦA GATE: ba thứ (quyền SKIP · owner-lock V11150 N≥1 · UCC ranked top-K adapter) mâu thuẫn nhau thế nào, và contract duy nhất nào hoà giải được?

TRẢ LỜI: chúng KHÔNG mâu thuẫn theo kiểu «phải chọn một, bỏ hai». Đo xong thì thấy mỗi cái hỏng theo một kiểu KHÁC nhau, và khi sửa đúng chỗ hỏng thì cả ba cùng đứng được:

1. QUYỀN SKIP — không phải một quyền đang cạnh tranh với owner-lock, mà là một NHÃN KHÔNG CÓ HIỆU LỰC. 283 lượt LLM tự khai SKIP thì 272 (96,1%) vẫn ra số; hạ nguồn chỉ hạ trọng số 0,4–0,7 và hai bộ tính WR bỏ qua hẳn verdict. Nên «bỏ SKIP» không mất gì đang chạy — nó chỉ gỡ một mệnh lệnh trỏ vào khả năng không tồn tại (đúng họ với L6 tool calling).

2. OWNER-LOCK V11150 — không mâu thuẫn với SKIP, mà mâu thuẫn với CHÍNH UCC: luật nói ở tầng NGÀY×MIỀN, phép tự suy NO_OUTPUT chạy ở tầng MỘT NGUỒN, và văn bản hợp đồng không tách hai tầng.

3. RANKED TOP-K — không mâu thuẫn với trần 2 số. Trần 2 số là chuyện CÔNG BỐ; ranked top-K là chuyện GHI VẾT. Dữ liệu hạng 3–5 đã tồn tại suốt trong near_miss_shortlist; chỉ bộ đọc CAP5 tra nhầm cột.

CONTRACT DUY NHẤT ĐỀ XUẤT — `PURE-CONTEXT-OUTPUT-1.0.0-DRAFT`, nguyên tắc trung tâm là TÁCH KIÊNG NHƯỢNG KHỎI CHẶN SỐ:
- `main_number` VẪN bắt buộc, cấm rỗng (giữ nguyên owner-lock V11016/V11022).
- Thêm `evidence_sufficiency` {SUFFICIENT|THIN|INSUFFICIENT} làm kênh kiêng nhượng THẬT, KHÔNG chặn số ⇒ XD-01 hết.
- `output_status=NO_OUTPUT` CHỈ dành cho lỗi truyền tải/parse, cấm dùng như lựa chọn biên tập; luật N≥1 giữ ở tầng NGÀY do validate_batch ⇒ XD-02 hết.
- `ranked_candidates` rank 1–2 = main/secondary (CÔNG BỐ, giữ trần 2), rank 3–5 = near_miss_shortlist (chỉ ghi vết) ⇒ XD-03 hết mà không đổi gì ở đầu ra người dùng.
- Đóng từ vựng verdict + sửa bộ hiển thị cùng phiên ⇒ XD-04 hết.
- MỘT luật duy nhất cho secondary (condition_refs không giao với main ở mức nhóm_độc_lập), XOÁ §5d ⇒ XD-05 hết.

BA PHƯƠNG ÁN VÀ CÁI GIÁ đã lập đủ: PA-1 (giữ SKIP như quyền thật) TỪ CHỐI — trái thẳng owner-lock, và đo 07/08 cho thấy nhóm bỏ số phụ trúng 0/4 vs nhóm giữ 5/12, tức đóng một cửa trúng THẬT. PA-2 (gỡ hẳn SKIP, không thay gì) KHÔNG ĐỦ — mất kênh cho model nói ra bằng chứng mỏng, và vẫn còn XD-04/XD-05. PA-3 CHỌN, giá phải trả: phải sửa 4 điểm bơm độc lập trong CÙNG một phiên, phải sửa bộ hiển thị cùng lúc, và phải RÚT LẠI ở chỗ gốc (PRJ-RETRACTION-001) mọi báo cáo từng dùng verdict làm bộ lọc.

## PHAT HIEN
  - [PROVEN_DEFECT] XD-01 — «Quyền SKIP» là mệnh lệnh trỏ vào một khả năng KHÔNG TỒN TẠI (cùng họ với L6 tool calling)
  - [PROVEN_DEFECT] XD-03 — «CAP5_INPUT_NOT_READY» là ÂM TÍNH GIẢ của bộ đọc: dữ liệu hạng 3–5 đã tồn tại suốt
  - [PROVEN_DEFECT] XD-04 — verdict.decision là từ vựng MỞ (37 giá trị) nhưng bộ hiển thị coi mọi thứ ≠ CHOT_HA là SKIP
  - [PROVEN_DEFECT] XD-05 — secondary_number bị BA luật và BA TÊN khác nhau điều khiển trong cùng một prompt
  - [PROVEN_DEFECT] XD-02 — owner-lock V11150 «N≥1 không được thành NO_OUTPUT» và việc UCC TỰ SUY NO_OUTPUT ở tầng NGUỒN là hai TẦNG bị gọi cùng tên
  - [PROVEN_DEFECT] `strength` được dùng làm trọng số tuyến tính ở tầng bundle nhưng KHÔNG đơn điệu theo kết quả
  - [OPERATIONAL_IMPROVEMENT] Gate 5 và Gate 6 suýt dựng HAI khuôn CONDITION khác nhau — đã tự bắt và tự rút trong phiên

## CHUA TRA LOI

1. GIAO DIỆN CÓ RENDER `display_text` KHÔNG — INDETERMINATE. Đã chứng minh đến tận thân trả lời API (main.py:7544 và :8898 đều đưa display_text vào payload), nhưng chưa kiểm tầng frontend. Điều này giới hạn PHẠM VI của XD-04: chắc chắn sai ở tầng API, chưa biết người dùng cuối có nhìn thấy dòng «SKIP – BỎ QUA HÔM NAY» hay không.

2. GRAIN CỦA `near_miss_shortlist` CHƯA ĐỊNH NGHĨA — và đây là thứ đang CHẶN thi hành XD-03. Chính prompt (gpt_analyzer.py:786) định nghĩa nó là «1–3 số khác có evidence mạnh nhưng KHÔNG được chọn làm main», tức MỘT TẬP BỊ LOẠI, KHÔNG phải HẠNG 3–5. Đo khớp với định nghĩa đó: 33,8% dòng có phần tử trùng với main_numbers. Phải định nghĩa grain + phép dedupe + quy tắc gán rank TRƯỚC khi dùng làm input CAP5, nếu không sẽ đếm một số hai lần — đúng lỗi consensus_level ở L10 (268/567 bundle mang nhãn cao hơn sự thật).

3. HIỆU ỨNG DỰ ĐOÁN CỦA CONTRACT ĐỀ XUẤT — CHƯA ĐO, và theo mục tiêu owner #9 thì CẤM hứa hit rate từ thiết kế prompt. Chỉ được nói contract này sửa NGHĨA, không được nói nó cải thiện kết quả.

4. CHƯA SO BẢNG HIỆU CHUẨN STRENGTH VỚI NỀN TÁCH MIỀN. Gate 5 đã đo nền T1 thật (MN 0,4298 · MT 0,3509 · MB 0,2374) nhưng bảng của tôi gộp ba miền và dùng cột `status` (WIN|PARTIAL) — chưa chắc đồng nghĩa «đuôi có mặt» của thước T1. Phải khớp định nghĩa và tách miền trước; hiện CẤM đọc bảng đó như bằng chứng hiệu năng.

5. ĐẶC TẢ NÀY CHƯA CÓ MÃ. Không có patch nào được viết, không có cổng nào được dựng, 8 phép thử chặn RM-15 mới chỉ là danh sách yêu cầu. Verdict trần CODED_AND_TESTED_NOT_RUNTIME_PROVEN CHƯA ĐẠT.

6. UCC VÀ RANKED ADAPTER CHỈ ĐỌC ĐƯỢC BẢN LOCAL. Hai tệp không có trên VPS (grep 'ranked_candidates' trên web/backend VPS = 0 dòng), nên XD-02 và một nửa XD-03 là xung đột TIỀM ẨN ở trạng thái CODED, chưa runtime — không được ghi như lỗi đang gây hại.