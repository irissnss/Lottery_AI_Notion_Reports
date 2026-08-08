# CONVERSATION_CONTEXT V11037 — 08/08/2026

Ghi lại **nguyên văn** lời owner, agent làm gì, và vấp ở đâu. Theo §57.2.

---

## Lượt 1 — owner nêu mẫu hình bộ 3 số

> *"Em hãy dựa vào DB mới nhất xem dùm anh mỗi ngày có hiện tượng này không nhé em:*
> *- Ví dụ : Thứ 6 07/08 MN có bộ số đuôi 869 - MT có cũng Bộ Số 869 --> MB có bộ số 689*
> *- Ví dụ : Thứ 5 06/08 MN có bộ số đuôi 617 - MT có cũng Bộ Số 617 --> MB có bộ số 167*
> *==> hãy xem dùm anh trong hôm nay có bộ số nào tương tự không em?*
> *Trong tuần này có hiện tượng này liên tục không em?"*

**Agent làm:** suy định nghĩa từ chính hai ví dụ (3 chữ số cuối của bất kỳ số trúng nào), kiểm
lại — khớp 100%. Trả lời: hôm nay 08/08 **không có**; tuần này **2/6 ngày** (T5, T6). Chạy phép
thử ngẫu nhiên một trục (dời MB) → 20,0% thật vs 17–21% giả ⇒ kết luận trùng hợp.

**Agent chỉ ra thêm:** ngày 07/08 còn một cụ nữa owner chưa thấy — MN Trà Vinh `25223`, MT Gia
Lai `94223`, MB Hải Phòng `5322`.

## Lượt 2 — owner bắt đúng chỗ agent làm ẩu

> *"ngày trước 3 hôm ổn hơn ah em? hoặc là MN trước 3 hôm só với MT hôm nay và MB hôm nay chẳng
> hạn em thử hết các phép thử chưa em?"*

**Agent thừa nhận:** chưa. Phép thử trước chỉ **7 phép, một trục**. Chạy lại **lưới đầy đủ 225
tổ hợp × 2 tập = 450 phép**.

**Kết quả:** ý owner nêu (MN trước 3 hôm) = **19,41%, hạng 180/225** — dưới trung bình. Con số
21,1% hôm trước chỉ là **0,5 sigma**, nhiễu thuần.

**VẤP LỚN NHẤT PHIÊN:** lưới trên toàn lịch sử lộ "tín hiệu" **+5,59 sigma**. Agent suýt báo
owner là có quy luật thật. Đào tiếp mới ra: **toàn bộ nằm ở năm 2021**, do 229 bản ghi sai nhãn
miền. Đây là lý do Việc 2 tồn tại.

## Lượt 3 — owner nêu mẫu hình thứ hai + hỏi ảnh hưởng dữ liệu sai

> *"Rồi còn 1 chỗ nữa mà anh cũng vừa thấy đó là đuôi giải 2 của MB ngày hôm trước hay về lại MN
> và MT ngày hôm sau với tỷ lệ khá cao và vị trúng khá ổn như là bạch thủ hoặc nhiều hit ah em.
> Ví dụ 94-43 MB ngày 07/08 --> hay sảy ra ở MN ah em… em xem thửu anh nói có đúng không?
> đồng thời kiểm tra dữ liệu sai có ai đang dùng không có ảnh hưởng gì không nha em? phương án
> xử lý thế nào em"*

**Agent xác nhận owner đúng cho đoạn gần đây:** 08/08 MN Bình Phước ĐB `828343` trúng bạch thủ
43; 14 ngày cuối 6 lần bạch thủ; 60 ngày cuối 8 lần vs kỳ vọng 3,7 — **kỷ lục 6,5 năm**.

**Nhưng:** hiệu chỉnh tìm-ở-đâu-cũng-thấy cho thấy đợt nóng cỡ đó có **67,8%** khả năng xuất
hiện đâu đó trong 6,5 năm. 5/6 năm trước đều **dưới** kỳ vọng. Lag 1 là lag **thấp nhất**.

**Về dữ liệu sai:** agent tra sổ trước khi báo (§56) và phát hiện việc này **đã biết từ
05/07/2026** — con số 229 đã nằm sẵn trong `gpt_analyzer.py:1059`. Không nơi production nào chạm
tới (cửa sổ sâu nhất 500 ngày → 27/03/2025). Trình 3 phương án.

## Lượt 4 — owner duyệt

> *"ok đồng ý các đề xuất cho việc 1 và 2 nha em"*

Qua bảng hỏi, owner chọn: deploy **gộp một lần sau Việc 1** · đo **đủ 9 mức**.

**Agent phản biện có kiểm soát:** 9 mức ⇒ 37% ăn may ⇒ thêm **ngưỡng họ** z ≥ 2,539. Vẫn làm
đúng ý owner, nhưng gắn hiệu chỉnh để lane không đẻ kết luận sai.

## Lượt 5 — owner giao quyền kỹ thuật

> *"Cách nào an toàn nhất , nhanh nhất , hợp lý nhất thì làm nha em về kỹ thuật em nắm tốt hơn
> anh . Tiến hành kiểm tra , dự đoán trước các tình huống nha em. Báo cáo chi tiết đầy đủ nha em"*

**Agent phát hiện có phiên khác chạy song song** trên cùng kho, cùng VPS (V11035/V11036,
NO_ANSWER, QD-046). Kiểm trước khi đụng VPS:

- Họ đẩy `combo_super.py`/`scheduler.py` — **không chồng** bộ tệp của phiên này
- Backfill của họ **đã chạy xong** trên VPS (đếm được `NO_ANSWER = 138`)
- Kéo bản VPS về **so từng dòng** với local ⇒ phát hiện `_v10900_consistency_guard.py` local có
  **khối V11023 chưa deploy** ⇒ dựng **bản ghép** để không deploy hộ việc của người khác

Deploy đạt: PID 1089328 → 1092764, health 200, endpoint admin 401, 24 phép, C23/C24 xanh.

## Lượt 6 — owner yêu cầu ghi nhận và cập nhật

> *"ghi nhận và cập nhật báo cáo đây đủ chi tiết nha em"*

**Agent phát hiện ngay đầu lượt:** `_v11037_deploy.py` của phiên này **đã bị phiên song song
ghi đè** bằng script deploy cho việc khác. Soi tiếp thì thấy **cả bốn mã FU** (355–358) cũng
trùng.

**Xử:** khôi phục script từ commit `207404c` thành `_v11037_deploy_g2mb.py` · đổi bốn mã FU
sang 365–368 (nhận diện khối của mình bằng **mã đọc**, không bằng số FU — vì số FU chính là
thứ đang trùng) · kiểm lại từng mã chỉ còn trỏ tới một việc · cập nhật CHANGELOG · SSOT ·
FOLLOW_UP · báo cáo công khai.

**Agent đề nghị thành quy tắc (FU-369):** cấp số hiệu và mã FU phải quét **ba nơi** —
`CHANGELOG` + `web/backend/_v*.py` + kho báo cáo công khai — chứ không chỉ CHANGELOG.

---

## Những chỗ agent làm SAI trong phiên và đã sửa

| # | Sai | Sửa |
|---|---|---|
| 1 | Phép thử chỉ một trục, 7 phép — owner phải hỏi lại | Chạy 450 phép, lưới đầy đủ |
| 2 | Suýt báo "tín hiệu +5,59σ" là thật | Đào ra vùng dữ liệu bẩn 2021 |
| 3 | Quét ngược dò bằng chuỗi thô → trượt `date>=?` | Dùng regex |
| 4 | Dò docstring bằng ký tự đầu dòng → bắt nhầm chính file mình | Dùng AST |
| 5 | Câu văn có chữ `from` bị tính là truy vấn | Yêu cầu có động từ SQL |
| 6 | Dựng cổng C23/C24 rồi báo "đạt" mà **chưa thử** (RM-15) | Bổ sung `_v11037_thu_cong.py` |
| 7 | Ghi nhãn `DEPLOYED_LOCAL` khi code mới ở local (RM-12) | Sửa thành `LOCAL_CHUA_COMMIT` |
| 8 | Lấy số hiệu V11035 rồi V11036 — cả hai đã có chủ (§58) | Đổi sang V11037 |
| 9 | Báo "hash 4 bảng giữ nguyên" khi `model_daily_eval` đã đổi | Truy bằng bản chụp VPS, xác định là việc của phiên song song |
| 10 | Bốn mã FU và một tệp deploy bị phiên song song chiếm mất | Đổi sang FU-365..368, tách tên `_v11037_deploy_g2mb.py`, đề nghị FU-369 |
