# CONVERSATION CONTEXT — V10805 (2026-07-15, ~21:53)

Nguyên văn tin nhắn owner (giữ đúng chính tả gốc):

> 51 là số của ngày hôm trước thật nhưng anh muốn biết model nào dự đoán ra số đó
> 19 là số trượt của miền trước thật nhưng anh muốn biết model  nào dự đoán ra số đó
> ==> anh muốn em thử nghiệm ngược với mốc với model , với điều kiện của các model dự đoán ra số đó tại thời điểm của miền trước hoặc của ngày hôm trước thì có nhưng gì dùng lại có ra số đó không để xác định mình đang làm sai chỗ nào , đúng chỗ nào lỗ hỏng là gì v.v... ML thì mốc dữ liệu như nào có chọn sai mốc D không , model Ai thì prompt nào ảnh hưởng đến output số đó v.v.. ý anh là tra ngược lại để tìm ra chỗ sai hiện tại và xử lý đúng lại ah em

(23:09, sau gián đoạn phiên): "tiếp đi em gián đoạn nữa rồi em"

Bối cảnh: cùng ngày đã có V10803 (truy vết 51, chase-bias shadow) và V10804 (truy nguồn 4 số, sandbox di cư H1/H3, fix C16 budget MB, audit prompt). Owner muốn đi sâu hơn 1 lớp: từ "số nào, pattern nào" xuống "MODEL nào + PROMPT/ĐIỀU KIỆN nào sinh ra số, replay có tái hiện không, sai đúng nằm đâu, xử lý lại cho đúng".

Phản hồi tóm tắt của agent (V10805):
- Liệt kê ĐÍCH DANH: 16 model ra 51 cho MB 14/07 (15 AI + combo-super); 12 model ra 19 cho MT + 4 cho MN 15/07. Pure-ML không dính cả 2 vụ (nhiều con còn trúng) → mốc D của ML không phải chỗ sai trong 2 vụ này.
- Tìm ra nguồn phát trong prompt: rule engine emit đuôi giải D-1 của đài miền khác (Đồng Tháp G5+G7 → [32,51] CONV×2 nhãn "12W=92%"; Vũng Tàu GĐB+G1 → [19,61] nhãn "75%").
- REPLAY THẬT 6 call trên VPS bằng đúng code production: 5/6 RA LẠI đúng số (gemini-2.5-flash và gpt-5-mini ra lại ở CẢ 2 vụ) → output deterministic theo prompt.
- Lỗ hổng semantic: nhãn % là hit_any bao-lô cụm k đuôi (baseline any-of-2 42-51%) nhưng model đọc như xác suất per-số; per-tail thật 33-44%.
- Đo adoption 120d: MB ngoài-rule 17.7% (hố chính), MT rule không cộng gì (BT theo-rule 28.6% < ngoài 40%), MN CONV×2 dưới baseline (bẫy).
- Deploy bảng RULE ADOPTION live vào panel /monitoring (zero regime change), hash 4 bảng IDENTICAL.
- 6 đề xuất CP-L6 chờ owner ký (nhãn per-tail, miền-hoá mandate §10A, guard ngoài-rule MB, khối định lượng per-miền, combo-super=AI-echo, thay API gemini-2.5-flash+gpt-5-mini).
