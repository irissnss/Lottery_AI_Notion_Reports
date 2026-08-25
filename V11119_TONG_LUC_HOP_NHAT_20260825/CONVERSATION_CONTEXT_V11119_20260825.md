# CONVERSATION CONTEXT — V11119 · 25/08/2026

> Nguyên văn lời owner · agent làm gì · vấp ở đâu. Theo **§57.2 (A55.2)**.
> Giờ trong tệp này là **giờ Việt Nam (UTC+7)**. Timestamp gốc trong vết phiên là **UTC**.

---

## 1 · Owner nói gì — nguyên văn, có giờ

### `~18:57` — prompt chính (kèm tệp đính kèm «Tổng Kết Lottery Ai.txt»)

> *« Em hãy tiến hành đọc toàn bộ các phiên làm việc của claude code và cursor kết hợp báo cáo
> tổng hợp đính kèm và các thông tin audit báo cáo tất cả mọi thể chạy tổng lực tổng hợp lại một
> phiên tổng lực với đầy đủ tất cả các vấn đề không làm rơi rụng bất kỳ vấn đề nào, các vấn đề đã
> xử lý , có thể xử lý , tự xử lý rõ ràng , các yêu cầu của anh v.... không bỏ sớt bất kỳ điểm nào
> nha em. Em tiến hành xem toàn bộ các phiên làm việc khác của Claude Code dùm anh, đồng thời anh
> có đinh kèm các tổng kết báo cáo cuối cùng , Sau đó phân tích lên kế hoạch xử lý cho liền mạch
> nhất quán nha em . Gom lại tổng hợp lại thành một báo cáo cáo tổng chi tiết đầy đủ tổng lực hợp
> nhất và đề xuất 1 plan tổng lực dùm anh. »*

**Đọc yêu cầu này thành bốn việc rời:**
① đọc **toàn bộ** vết phiên Claude Code **và Cursor**
② hợp với tài liệu tổng kết owner gửi
③ gom thành **một** báo cáo, **không rơi rụng vấn đề nào**, phân rõ *đã xử lý / có thể xử lý / tự xử lý*
④ đề xuất **một** plan liền mạch nhất quán.

### Bối cảnh: đây là lần thứ **24** owner nêu cùng một điều

Quét toàn corpus 711 lượt, tìm các câu phàn nàn về rơi rớt / cẩu thả ⇒ **24 lượt trực tiếp**.
Chuỗi này bắt đầu từ **02/08** và chưa đứt. Trích ba mốc nặng nhất:

| giờ VN | nguyên văn |
|---|---|
| 06/08 20:20 | *«Cần 1 cơ chế chống quên lãng , rơi rớt các vấn đề anh phân tích đề xuất cũng như căn dặn nha em.»* |
| 09/08 20:38 | *«Anh thực sự rất không hài lòng về em, em đã xem nhẹ tài liệu mặc dù anh nhắc rất nhiều lần…»* |
| 16/08 14:19 | *«…em làm việc vẫn chểnh mãng lắm rơi rớt tùm lum , anh phải nhắc đi nhắc lại, nhân mạnh nhiều lần mệt mỏi quá em.»* |

**Đó là lý do bản này đổi cách làm**: sổ yêu cầu owner dựng **bằng phép cơ học**, trích thẳng
nguyên văn, không qua mô hình diễn giải — vì cách cũ (đọc rồi tóm tắt) đã thất bại 24 lần.

---

## 2 · Agent làm gì — theo trình tự

| # | việc | kết quả |
|---|---|---|
| 1 | Chạy cổng đầu phiên bắt buộc `_v10920_session_start.py` | 189 treo · 125 quá hạn · 6 đến hạn · 15 QĐ tới hạn · 3 thiếu mã đọc |
| 2 | Quét thư mục phiên Claude Code | **12 tệp `.jsonl`** ≈350 MB |
| 3 | Bóc lượt owner, khử trùng theo **băm nội dung** | **234 lượt duy nhất**, 810.865 ký tự, 03/07→25/08 |
| 4 | Xác định quan hệ 5 tệp nghi trùng | **bản rẽ nhánh `--resume`** — cùng `promptId`/nội dung, khác `sessionId`+`uuid` |
| 5 | Mở kho Cursor `state.vscdb` **10,9 GB** | `cursorDiskKV` 310.889 dòng · `composerData` 286 · `bubbleId` 213.115 |
| 6 | Bóc tin owner Cursor (`type == 1`) | **890 tin** trên **125 phiên**, 04/07→05/08 |
| 7 | Dựng **sổ yêu cầu owner cơ học** | **711 lượt duy nhất** (227 CC + 484 Cursor) |
| 8 | Dựng bản đồ **35 prompt tổng lực** | đủ chuỗi; phát hiện prompt **14 không có dấu vết** |
| 9 | Đếm chủ đề toàn corpus | «phàn nàn cẩu thả/rơi rớt» **160 lần** xuất hiện |
| 10 | Đối chiếu **version × báo cáo công khai** | **10 bản thiếu** + **1 đặt sai thư mục** + **26 bản chỉ có ở git** |
| 11 | Kiểm `V11077`/`V11079` | **CÓ đủ báo cáo từ 16/08** ⇒ câu đã công bố **SAI** |
| 12 | Chạy `_v10920_decision_ledger.py` | **0 TRÔI**, 1 không kết luận được ⇒ câu «3 phép TRÔI» **không còn đúng** |
| 13 | Chạy `_v11044_cong_so_hieu.py` | cấp **`V11119`** · `FU-439` · `QD-072` |
| 14 | Chạy `_v11062_nang_version.py --kiem` | **ĐẠT** |
| 15 | Xác minh `FU-438` trên **production** (`RM-13`) | `/history` **39.682 B ẩn danh** có `ranked_numbers`+`voters` ⇒ **`RUNTIME_PROVEN`** |
| 16 | Kiểm kê `FOLLOW_UP_TRACKER` | 313 khối `FU` · 207 không đóng · **37 chặn ở owner** |
| 17 | Kiểm kê sổ quyết định | 73 QĐ · 68 `ACTIVE` · **15 quá hạn rà soát** · chỉ **8/73** khai quan hệ thay thế |
| 18 | Truy thiết kế `GĐ-7` | **không có trong tài liệu nào** — chỉ trong vết phiên |
| 19 | Kiểm deliverable prompt 35 | Algorithm Card **đã có 175.765 B / 2.169 dòng**, ba thẻ phủ bốn sản phẩm |
| 20 | Ghi sổ tương tác owner | append **1 dòng**, +1.086 ký tự, **không sửa dòng cũ** |
| 21 | Chạy **22 làn đọc/phản biện** song song `READ-ONLY` | đang chạy nền — kết quả nạp bổ sung |

---

## 3 · Vấp ở đâu — kể cả vấp do chính agent gây ra

### V1 · Cursor không đọc được bằng đường thông thường

`conversation-search.db` có **164 hàng** nhưng **tiêu đề rỗng gần hết**, và bảng nội dung chỉ
**6/164** hàng có chữ. Nếu dừng ở đó thì kết luận *«Cursor không có dữ liệu»* — **sai**, mất 890
tin owner. Phải mở thẳng `state.vscdb` **10,9 GB** và lọc `bubbleId:*` lấy `type == 1`.

### V2 · Băm tệp **không** khử được trùng

Năm tệp phiên có **cùng 8.687 dòng và cùng 38.409.630 byte** nhưng **băm khác nhau** — vì mỗi
dòng nhúng `sessionId` và `uuid` riêng. Nếu khử theo băm tệp thì giữ cả 5 ⇒ đếm ra ~1.168 lượt
owner thay vì 234, **phóng đại gấp 5**. Phải khử theo **băm nội dung từng lượt**.

### V3 · 🔴 Agent tự đặt một giả thuyết sai và phải tự bác — ghi lại đầy đủ

Sau khi thấy owner nhắn ngày 09/08 *«em có xem được seccsion của chính cursos không»*, agent định
viết: *«phiên hôm nay là phiên đầu tiên thực sự đọc Cursor»*.

**Tra vết phiên trước khi trình** (`RM-13` — chứng minh nguồn trước khi kết luận):
phiên `d2a0e7e5` đã mở `state.vscdb` lúc **13:50:40** ngày 09/08 — tức **40 giây** sau câu hỏi —
và tới **14:03** báo lại *«CÓ, em đọc được session Cursor»*, liệt kê 275 phiên / 213.115 tin.

⇒ Giả thuyết **bị bác trước khi trình owner**. Điều đúng: lần đó đọc **7 phiên liên quan prompt**;
đây là lần đầu bóc **toàn bộ 890 tin owner trên 125 phiên**.

**Hậu quả nếu bỏ qua:** một câu tự khen sai sự thật, và làm owner tưởng yêu cầu 09/08 đã bị bỏ rơi.

### V4 · Mã `GĐ-n` bị dùng lại giữa các prompt

`GĐ-7` là «retire P&L» ở prompt 32 · «lượt rỗng» ở prompt 33/34 · «10 bản vá» ở prompt 35.
Tra theo mã ra nhầm việc — đã suýt xảy ra trong chính phiên này.

### V5 · Thiết kế `GĐ-7` chỉ tồn tại trong vết phiên

10 bản vá (54 kết luận) **không có trong tài liệu nào** của kho. Phiên đóng hoặc bị nén là **mất
hẳn**. Đã khai thành `FU-439`.

### V6 · Các làn đọc sinh kết quả rất chậm

Mỗi làn trả 76–113 mục có nguyên văn. Nên sổ yêu cầu owner được dựng **bằng phép cơ học song
song**, không chờ mô hình — đó là lý do bản này bảo đảm được *«không rơi lượt»* dù các làn chưa
xong hết.

---

## 4 · Bốn con số bị rút lại — và chúng đã dựa vào đâu

| # | câu sai | nguồn | điều đúng | đã dùng để làm gì |
|---|---|---|---|---|
| R1 | *«V11077 · V11079 thiếu báo cáo»* | tệp owner đính kèm | có **đủ** báo cáo từ 16/08; thiếu **mục CHANGELOG** | căn cứ xếp «6 bản chưa có báo cáo» ⇒ dẫn sai hướng xử lý |
| R2 | *«còn 4 (hoặc 6) bản thiếu báo cáo»* | cùng tệp | **10 bản** + 1 đặt sai thư mục | quyết định «bù báo cáo một lượt» ⇒ nếu bù 4 thì sót 6 |
| R3 | *«cổng quyết định báo 3 phép TRÔI»* | cùng tệp | **0 TRÔI**, 1 không kết luận được | liệt vào «còn treo» ⇒ tốn công xử việc đã xong |
| R4 | *«Algorithm Card chưa viết»* | báo cáo phiên trước | đã có **175.765 B / 2.169 dòng** | làm khối lượng còn lại của prompt 35 trông lớn hơn thực tế |

---

## 5 · Điều agent **không** làm, và vì sao

| không làm | vì sao |
|---|---|
| Sửa bất kỳ dòng mã production nào | 25/08 là ngày `GĐ-0` khoá *«cấm đổi production TOTAL giữa ngày»* |
| Vá `FU-438` | đổi hành vi cổng ⇒ vùng owner khoá *«cấm tự quyết»* |
| Thi hành 10 bản vá `GĐ-7` | cả mười đều đổi hành vi cổng hoặc lược đồ |
| Đóng bất kỳ mục `FU` nào | owner đã cấm đóng hàng loạt (`FU-390`, `QD-066`) |
| Cắt model nào | `CORE = 0`, gate chưa đạt; và **chưa ai đo tiền** |
| Bù báo cáo cho `V11077`/`V11079` | vì chúng **không thiếu** — thiếu là mục CHANGELOG |
| Rewrite lịch sử git để scrub rò rỉ | owner khoá *«cấm rewrite lịch sử Git»*, và đó là thao tác phá huỷ |

---

## 6 · Trạng thái cuối phiên

| | |
|---|---|
| tệp bị sửa trong kho riêng | `docs/SO_TUONG_TAC_OWNER.md` (**append 1 dòng**) · `docs/OWNER_DECISION_LEDGER.md` + `docs/_LEDGER_TRANG_THAI.json` + `docs/_I2_DA_CHAY.json` (máy sinh, chỉ dấu thời gian) |
| tệp thêm ở kho công khai | `V11119_TONG_LUC_HOP_NHAT_20260825/` — báo cáo + tệp này |
| deploy | **không** |
| restart service | **không** |
| ghi DB | **không** |
| chạm `/du-doan` | **không** |
| chỗ code đi trước tài liệu | **không có** — phiên không sửa mã nào |

**TanPhatAI cần làm:** đọc `REPORT_V11119.md` §10 (ba lớp nguồn) và §1 (bốn con số rút lại) trước
khi phản biện bất kỳ con số nào của phiên 25/08; đặc biệt **đừng đi bù báo cáo cho `V11077`/`V11079`**
— chúng đã có đủ từ 16/08.
