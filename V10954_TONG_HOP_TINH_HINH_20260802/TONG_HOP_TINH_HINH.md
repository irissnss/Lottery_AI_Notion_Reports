# TỔNG HỢP TÌNH HÌNH — 02/08/2026

> Viết cho chủ dự án đọc một lần là nắm được. Số liệu lấy từ tài liệu quản trị và từ máy đang chạy thật lúc khoảng 15:57 giờ VN ngày 02/08. Không đoán.

---

## 1. Trả lời ngay bốn câu anh hỏi

### Total / official mới đã áp dụng chưa?

**Đã áp dụng.** Bấm nút tối 01/08 khoảng 17:45 (phiên bản V10939), sau khi nghiệm thu đêm đầu với hạn mới.

Thay đổi cụ thể so với trước sáng 01/08:
- Vào danh sách 15 model công bố: `glm-5.1`, `gpt-oss-120b` (sáng 01/08, V10931), rồi `gpt-5.4` (chiều 01/08, V10937 — gọi về vì cắt vội).
- Ra khỏi quyền góp phiếu công bố: `gpt-5-mini`, rồi `combo-no-token` (vẫn chạy để đo, chỉ mất quyền góp phiếu).
- `gemini-3.5-flash` **chưa** vào total — anh đã hoãn vì đang tụt phong độ; đang chạy shadow.
- Bộ lọc combo-super: bỏ điểm ảo 50%, mở pool 7→9 AI, chấm bằng bạch thủ thay win rate.

Máy đang chạy xác nhận đúng 15 model official, có `gpt-5.4`, không có `combo-no-token` trong total.

### Người dùng nên xem ở đâu?

Trang web thật: **https://xs.io.vn** (cũng có `www.xs.io.vn`).

| Việc cần xem | Đường dẫn |
|---|---|
| Số dự đoán công bố (official) | https://xs.io.vn/du-doan |
| Bảng chơi / vốn / chốt số | https://xs.io.vn/choi |
| Góc nhìn người dùng | https://xs.io.vn/user-view |
| Theo dõi kỹ thuật (cổng lợi thế, lớp ghi đè, tự kiểm…) | https://xs.io.vn/monitoring — cần đăng nhập admin |

Lưu ý: anh đã chốt **dừng đặt tiền thật** (QD-013). Hệ vẫn chạy và vẫn ra số để đo, nhưng chưa nên dùng số để đặt tiền.

### Nguyên nhân giảm sút là gì?

Không phải “hệ chưa bao giờ đoán được”. Ở miền Trung, từ tháng 2 tới tháng 5 hệ **từng hơn đánh bừa rõ ràng** (+9,57 điểm phần trăm, độ tin cậy thống kê rất mạnh). Từ tháng 6 lợi thế đó **tắt hẳn**.

Đồng thời, việc huấn luyện máy học chết 7 chủ nhật (tháng 5–7) vì lỗi ống ghi, rồi sau khi sửa (15/07) thì bảng ghi chất lượng lại bị rút gọn nên mọi chữ “OK” thành vô nghĩa. Nhưng điểm mấu chốt: tới hôm nay tín hiệu ở tầng model miền Trung **vẫn còn** (AUC khoảng 0,52–0,55). Phần mất nằm ở khâu biến tín hiệu thành số công bố — chưa tìm ra đúng chỗ gãy.

### Hiện đang chờ anh quyết những gì?

Gọn nhất:
1. **Giữ nguyên dừng đặt tiền** cho tới khi cổng lợi thế mở (đã chốt QD-013 — chỉ cần nhớ, không cần quyết lại).
2. **Cửa sổ đóng băng đường ra số tới 08/08** (OD-20260801-D) — tới hạn thì xem có mở khóa tỉa tót không.
3. **Bốn checkpoint roadmap quá hạn rất lâu** (CP-X.1, CP-2.2, CP-4.0, CP-R4) — đóng / hủy / làm tiếp?
4. **Sau 08/08**: có đào tiếp chỗ “MT còn tín hiệu nhưng không ra số trúng” không (FU-212 / FU-210)?
5. Các mục `OWNER_LOCK` cũ (cắt model an toàn, shadow promote, báo cáo tồn đọng…) — liệt kê ở mục 6.

---

## 2. Toàn bộ vấn đề đã phát hiện — xếp theo mức nghiêm trọng

### Nghiêm trọng — ảnh hưởng tiền / lòng tin

| # | Vấn đề | Phát hiện | Bằng chứng bằng số | Đã sửa? | Version |
|---|---|---|---|---|---|
| 1 | Hệ 90 ngày không hơn đánh bừa; lỗ thật lớn | 01/08 | Vốn 579,2 tr · thu 445,9 tr · **lỗ 133,3 tr (−23%)**. Ba miền đều không phân biệt được với ngẫu nhiên | Đã biến thành **cổng lợi thế** trong code; owner chốt dừng đặt tiền | V10945 · QD-013 |
| 2 | Họ ML từng có lợi thế thật ở MT rồi tắt | 01/08 tối | Nửa đầu +9,57pp (z 3,74); nửa sau +0,58pp (z 0,23). Tháng 6 −1,14 · tháng 7 −1,83 | Chưa sửa nguyên nhân gốc — đang đo | V10947 · FU-210 |
| 3 | Tín hiệu MT còn nhưng không thành số trúng | 01–02/08 | AUC MT vẫn 0,52–0,55 (cả 4 họ); MB đúng bằng ngẫu nhiên | Chưa — đây là hướng đào tiếp | V10952 · FU-212 |
| 4 | Huấn luyện ML chết 7 chủ nhật | 01/08 khuya | 17/05→12/07: lỗi `I/O operation on closed file`, 12/12 model chết trong 1 giây | **Đã sửa từ 15/07** (chạy tiến trình riêng). 19/07 và 26/07 OK | V10800 (sửa cũ) · V10952 (đào ra) |
| 5 | Bảng huấn luyện ngừng ghi chất lượng từ 19/07 | 01/08 khuya | Từ 19/07: 0/12 dòng có AUC; trước đó 9/12. Mọi dòng vẫn ghi “OK” | **Đã sửa 01–02/08**. Lượt thật 02/08: 12/12 có AUC | V10952 · V10953 |

### Nghiêm trọng — lỗi kỹ thuật làm chọn sai model / sai số

| # | Vấn đề | Phát hiện | Bằng chứng | Đã sửa? | Version |
|---|---|---|---|---|---|
| 6 | Điểm ảo 50% trong bộ lọc combo-super | 01/08 chiều | Model chưa chạy ngày nào ở MB tự lên #1 (thử `gemini-3.6-flash` 0 lượt cướp suất) | **Đã sửa + đã deploy**: đủ 5 lượt thật mới được dự tuyển | V10936 · V10939 |
| 7 | Bộ lọc chấm win rate trong khi anh đánh bạch thủ | 01/08 | `meta-learning` lệch −10,9pp giữa hai thước; đổi thước thì đổi lựa chọn cả ba miền | **Đã sửa + đã deploy** | V10938 · V10939 |
| 8 | Cắt `gpt-5.4` vội bằng một thước đo | 01/08 | Bạch thủ dưới mặt bằng nhưng win rate **trên** mặt bằng và đang đi lên | **Đã gọi về** thay `combo-no-token` | V10937 · V10939 |
| 9 | Bỏ sót khai `gemini-3.5-flash` vào đường thoát 503 | 01/08 | Đường thoát OpenRouter đã có từ 31/07 nhưng chỉ khai bản 3.6; bản 3.5 rớt 6,58% | **Đã khai + đã deploy**; đang chạy shadow | V10933 |
| 10 | Deploy 17:45 chạm lượt T-chốt 17:55 | 01/08 tối | `model_count` 15→14; **bạch thủ may không đổi** (vẫn 90) | Rút quy tắc mới: chỉ deploy sau MB 17:58. Cổng tự động chưa nâng xong | V10940 · FU-207 |

### Trung bình — vận hành / quản trị

| # | Vấn đề | Ghi chú | Trạng thái |
|---|---|---|---|
| 11 | 5 lớp ghi đè bạch thủ làm tệ đi | 67/180 lượt số công bố ≠ phiếu bầu; tắt 5 lớp, giữ MN | Đã deploy V10917; đang theo dõi tới 08/08 (FU-186) |
| 12 | 6 lane đo hết hạn vẫn chạy | Owner: luồng rối | Đã cho nghỉ V10919 (comment cron, có thể bật lại) |
| 13 | Shadow 110 ngày 0 lần promote | Sau đó đã promote `glm-5.1` + `gpt-oss-120b` sáng 01/08 | Một phần đã xử; FU-192 còn chữ “chờ owner” — **lệch tài liệu** (xem cảnh báo) |
| 14 | So AUC cũ↔mới đang so hai cửa sổ khác nhau | Không thể kết luận “model tụt” chắc chắn | FU-213; **không** bật lại cổng tự gỡ model |
| 15 | Agent hỏi lại việc đã có trong roadmap | CP-L2 quá hạn 37 ngày mà vẫn hỏi | Đã dựng sổ quyết định + kiểm đầu phiên (V10920) |

---

## 3. Nguyên nhân giảm sút — câu chuyện theo thời gian

**Tháng 2–5/2026.** Ở miền Trung, họ model không tốn token (`combo-no-token` và các anh em ML) **thật sự hơn đánh bừa**. Nửa đầu cửa sổ đo: +9,57 điểm phần trăm, z = 3,74 — đây không phải nhiễu. Tháng 2 từng +18,92pp. Có lợi thế thật.

**Tháng 5–7.** Việc huấn luyện lại hàng tuần bắt đầu chết: đúng 7 chủ nhật (17/05, 24/05, 31/05, 14/06, 21/06, 28/06, 12/07) cả 12 model nổ cùng một lỗi ống ghi đã đóng. Cùng lúc, lợi thế tiền thật ở MT tắt: tháng 6 −1,14pp, tháng 7 −1,83pp.

**15/07.** Lỗi ống ghi được sửa (chạy tiến trình riêng). Huấn luyện chạy lại được — nhưng câu lệnh ghi bảng bị rút còn 4 cột, nên từ 19/07 trở đi **không còn số AUC**. Mọi dòng “OK” trở thành lời tự khen không kiểm chứng.

**Cuối tháng 7 – 01/08.** Hệ tiếp tục tỉa model, đổi bộ lọc, sửa prompt. Đo lại 90 ngày thì **không miền nào hơn đánh bừa có ý nghĩa**. Ngày đẹp 01/08 (+1,2 triệu) không cứu được bức tranh dài: lỗ 133 triệu / 90 ngày.

**Điểm mấu chốt (01–02/08).** Đo lại AUC trên model hiện tại: miền Trung vẫn 0,52–0,55 ở cả bốn họ (random-forest, xgboost, meta-learning, lstm). Miền Bắc đúng bằng ngẫu nhiên. Nghĩa là:

> Tín hiệu ở tầng model **còn**. Phần mất nằm ở khâu biến tín hiệu thành số công bố (bộ lọc, trọng số, lớp ghi đè, cách gộp phiếu…).

Đó là lý do không nên vội “thêm model / cắt model” nữa — phải tìm chỗ gãy giữa điểm model và số đưa ra ngoài.

---

## 4. Tiền — con số thật

Số liệu từ báo cáo V10945 (01/08), đếm theo **đài trúng** (anh đặt 3 đài), không đếm theo kỳ:

| Cửa sổ | Vốn | Thu | Lãi / lỗ |
|---|---|---|---|
| 7 ngày | 52,2 triệu | 39,2 triệu | **−13,0 triệu** |
| 30 ngày | 198,5 triệu | 147,0 triệu | **−51,5 triệu** |
| 90 ngày | 579,2 triệu | 445,9 triệu | **−133,3 triệu (−23% vốn)** |

### Vì sao ngay cả đánh bừa cũng lỗ?

Luật trả thưởng hiện dùng:
- MN / MT: bỏ 18.000 được trả 98.000 khi trúng → **cần trúng 18,37% mới hòa vốn**. Đánh bừa chỉ khoảng **16,5%**.
- MB: bỏ 27.000 → **cần 27,55%**. Đánh bừa khoảng **23,8%**.

Phần thiệt đã cài sẵn khoảng **10%** ở MN/MT và **14%** ở MB. Hệ phải hơn ngẫu nhiên ít nhất khoảng **1,9 điểm phần trăm** ở MN/MT chỉ để hòa — chưa nói lãi.

### Cổng lợi thế lúc này (máy chạy thật 02/08 ~15:57)

Ngưỡng mở cổng (anh đã chốt): hơn đánh bừa **≥ 3pp** và **z ≥ 2**.

| Miền | Hệ 90 ngày | Đánh bừa | Chênh | z | Cổng |
|---|---|---|---|---|---|
| MN | 15,90% | 16,46% | −0,56pp | −0,25 | ĐÓNG |
| MT | 13,76% | 16,49% | −2,72pp | −1,08 | ĐÓNG |
| MB | 15,56% | 23,67% | −8,11pp | −1,81 | ĐÓNG |

Kết luận máy ghi: *“CHƯA miền nào đủ điều kiện — owner đã chốt 01/08 dừng đặt tiền thật”*.

(Số 90 ngày hôm nay hơi lệch vài phần mười so với báo cáo 01/08 vì cửa sổ trượt thêm một ngày — hướng kết luận không đổi.)

---

## 5. Đã thay đổi gì trong hệ ngày 01–02/08

| Thay đổi | Lúc nào | Đã deploy? | Xác minh |
|---|---|---|---|
| Tắt 5 lớp ghi đè bạch thủ (giữ MN) | 01/08 sáng | Có (V10917) | Hash 4 bảng giữ nguyên; panel canh trên `/monitoring` |
| Cho 6 lane hết hạn nghỉ (comment cron) | 01/08 sáng | Có (V10919) | Cron 83→71; tự kiểm lệch 0 |
| Hoán `glm-5.1` + `gpt-oss-120b` vào total; dời hạn MT/MB → 16:58 / 17:58 | 01/08 sáng | Có (V10931) | Đêm đầu: MT/MB đúng hạn, 0 lỗi |
| Cứu `gemini-3.5-flash` (khai đường thoát 503) | 01/08 chiều | Có (V10933) | Thử trọn đường có nhóm đối chứng |
| Sửa bộ lọc: bỏ điểm ảo 50%, mở pool 9, chấm bạch thủ | 01/08 chiều–tối | Có (V10936+38, deploy V10939 ~17:45) | PID đổi; tự kiểm 10/10; hash giữ nguyên |
| Gọi `gpt-5.4` về, `combo-no-token` ra total | 01/08 tối | Có (V10937, cùng chuyến V10939) | Total đúng 15; `gpt-5.4` có trong danh sách live |
| Cổng lợi thế (≥3pp, z≥2) + panel | 01/08 tối | Có (V10945) | Cổng ĐÓNG cả ba miền |
| Sửa ghi bảng huấn luyện (AUC thật) | 01/08 khuya | Có (V10952) | 02/08 00:02: 12/12 có AUC |
| Xác minh job CN 02:00 | 02/08 02:18 | Chỉ đọc (V10953) | 12/12 có AUC; không lỗi ống ghi |

### 15 model official đang chạy thật (02/08)

1. `claude-sonnet-4-6`
2. `gemini-2.5-flash`
3. `claude-opus-4-6`
4. `deepseek-reasoner`
5. `gemini-2.5-pro`
6. `gpt-5.4` ← gọi về chiều 01/08
7. `glm-5.1` ← lên sáng 01/08
8. `gpt-oss-120b` ← lên sáng 01/08
9. `meta-learning`
10. `lstm`
11. `xgboost`
12. `random-forest`
13. `smart-ensemble`
14. `smart-ml`
15. `combo-super`

**Không còn trong total:** `combo-no-token` (vẫn chạy đo), `gpt-5-mini` (shadow).

**Pool AI combo-super (9):** sonnet, flash 2.5, opus, pro 2.5, deepseek, glm-5.1, gpt-oss-120b, gemini-3.5-flash, gemini-3.6-flash. Bộ lọc tự chọn top-2 mỗi miền mỗi ngày.

**Pool ML combo-super (4):** meta-learning, lstm, xgboost, random-forest — chọn top-3.

### Bundle hôm qua và hôm nay (máy thật)

| Ngày | Miền | Giờ tạo | Model | Bạch thủ | Đã chấm? |
|---|---|---|---|---|---|
| 01/08 | MN | 05:20 | 13 | 16 | WIN |
| 01/08 | MT | 16:46 | 13 | 55 | LOSE |
| 01/08 | MB | 17:39 (v2 sau T-chốt) | **14** | 90 | WIN |
| 02/08 | MN | 05:18 · T-chốt 15:40 | **15** | 43 | PENDING (chưa xổ / chưa chấm) |
| 02/08 | MT / MB | — | — | — | **Chưa có** lúc tra (~15:57) — đúng vì chưa tới giờ chạy |

Dịch vụ: `/api/health` = **200**, đang chạy, khai đúng 15 model output.

---

## 6. Đang chờ owner quyết — phần quan trọng nhất

| Mã | Việc gì | Vì sao cần anh quyết | Các lựa chọn | Khuyến nghị của em | Hậu quả nếu để trôi |
|---|---|---|---|---|---|
| **QD-013 / FU-208** | Dừng đặt tiền thật tới khi cổng mở | Đã chốt 01/08 — cần **nhớ và giữ**, không lỏng tay khi có tuần đẹp | (a) Giữ dừng (b) Hạ ngưỡng (c) Đặt lại sớm | **Giữ dừng.** Ngưỡng ≥3pp và z≥2 nằm trong code. Không hạ ngưỡng khi sốt ruột | Đặt lại khi cổng còn đóng = tiếp tục lỗ theo phần thiệt cài sẵn |
| **FU-209** | Dừng thêm/cắt model vặt | Khác biệt nhỏ hơn mức đo được → tỉa mãi không biết việc nào có ích | (a) Giữ dừng (b) Chỉ sửa lỗi rõ (c) Tiếp tục tỉa | **Giữ dừng tỉa.** Chỉ động khi giả thuyết ≥5pp hoặc lỗi kỹ thuật rõ (như lối thoát 503) | Lặp vòng “cứ lẩn quẩn mãi” |
| **OD-D / FU-186** | Đóng băng đường ra số tới **08/08** | Cần 7 ngày sạch để biết tắt lớp ghi đè có đúng không | (a) Giữ đóng băng tới 08/08 (b) Mở sớm | **Giữ tới 08/08.** Có phát hiện mới thì ghi nhận, không sửa chồng | Sửa chồng = mất khả năng quy kết kết quả |
| **CP-X.1** | Hook theo dõi PP1 sau khi chấm điểm | Quá hạn **93 ngày** (hạn 01/05). Roadmap cũ còn ACTIVE | (a) Đóng vì đã lỗi thời (b) Xác minh còn chạy không rồi đóng (c) Làm tiếp | **Cho đóng / hủy** sau một lần xác minh nhanh — đừng để treo đầu phiên mãi | Mỗi phiên agent lại nhắc; nhiễu việc thật |
| **CP-2.2** | Tinh chỉnh chính sách cứu số (đã đo kém) | Quá hạn **92 ngày**. Trạng thái: framework đã dựng, cổng chưa đạt | (a) Hủy vì dưới chuẩn (b) Tiếp tục tích lũy dữ liệu (c) Gấp rút promote | **Hủy hoặc xếp “không làm”** — đang dưới chuẩn và trùng với QD-013 dừng tỉa | Roadmap giả ACTIVE, agent tưởng còn việc |
| **CP-4.0** | Kiểm độ chín mẫu TIER 4 | Quá hạn **62 ngày**. Tài liệu ghi đã gộp vào CP-L6 | (a) Đóng chính thức (b) Mở lại | **Đóng chính thức** (đã gộp chỗ khác) | Cùng nhiễu như trên |
| **CP-R4** | Gọi thưa model REDUCED (tiết kiệm token) | Quá hạn **49 ngày**. Anh từng bảo chờ thêm | (a) Làm sau 08/08 (b) Hủy vì QD-013 (c) Làm ngay | **Hoãn sau 08/08**, hoặc hủy nếu anh muốn tiết kiệm quyết định. Không tự wire | Treo OWNER_DECIDED_WAIT mãi |
| **FU-206** | Quy tắc cắt model: đủ 2 thước + xu hướng tuần | Tránh lặp lỗi cắt `gpt-5.4` / phóng đại `gemini-3.5` | (a) Khóa thành quy tắc cứng (b) Chỉ ghi nhớ | **Khóa cứng** vào sổ + tài liệu vận hành | Agent phiên sau cắt vội lại |
| **FU-192** | Shadow 110 ngày / promote | Ứng viên cũ đã được promote một phần sáng 01/08 | (a) Đóng FU vì đã promote glm + oss (b) Giữ mở cho đợt sau | **Đóng hoặc sửa chữ** cho khớp việc đã làm; đừng để chữ “chờ owner” lệch sự thật | Tài liệu nói chờ trong khi việc đã làm |
| **FU-210 / FU-212** | Đào vì sao MT mất lợi thế / tín hiệu không thành số | Đây là hướng duy nhất còn “từng có lợi thế thật” | (a) Cho phép đào sau 08/08 (b) Dừng hẳn (c) Đào ngay trong cửa sổ đóng băng | **Đào sau 08/08**, chỉ đo / shadow, **không** đổi đường ra số cho tới khi có ngưỡng bằng số | Bỏ qua = mất cơ hội duy nhất đã từng thắng ngẫu nhiên |
| **FU-213** | Phép so AUC cũ↔mới sai cửa sổ | Chặn việc bật lại cổng tự gỡ model | (a) Sửa phép so rồi mới xét cổng (b) Bỏ cổng luôn | **Sửa phép so trước.** Không bật cổng tự gỡ khi còn so hai cửa sổ khác nhau | Gỡ oan model tốt / giữ model tệ |
| Các FU `OWNER_LOCK` cũ (V105.*) | Gói lane-test / anti-clone / PAT deploy key… từ tháng 5 | Lâu, chồng lên quyết định mới hơn | (a) Rà một lần rồi đóng hàng loạt (b) Giữ | **Sau 08/08**: một phiên dọn hàng loạt, đóng cái lỗi thời | Sổ theo dõi phình, khó đọc |

---

## 7. Đang tự chạy, không cần anh làm gì

| Việc | Đang làm gì | Hạn rà |
|---|---|---|
| Cổng lợi thế | Tự chấm mỗi ngày; hiện ĐÓNG cả 3 miền | Liên tục (FU-208) |
| Theo dõi 7 ngày sau tắt lớp ghi đè | Panel `/monitoring` đối chiếu phiếu bầu vs số công bố | **08/08** (FU-186) |
| `gemini-3.5-flash` hồi phong độ? | Chạy shadow + trong pool combo (chưa được chọn) | **08/08** (FU-203) |
| `gpt-5.4` gọi về có đúng không | Đo 14 ngày bạch thủ + win rate | **15/08** (FU-204) |
| Bộ lọc bạch thủ có tốt hơn win rate? | So `combo-super` trước/sau 02/08 | **15/08** (FU-205) |
| Đường thoát 503 của gemini-3.5 | Canh tỉ lệ hỏng < 1,5% | **15/08** (FU-197) |
| So găng gemini 3.5 vs 3.6 | Cả hai chạy đủ 3 miền từ 02/08 | **01/09** (FU-198) |
| `glm-5.1` ngưỡng gỡ nếu lỗi >6% hoặc làm MT lỡ hạn ≥2 ngày | Tự theo dõi | **15/08** (FU-195) |
| Lớp ghi đè MN còn bật | Âm tiền tới 31/08 thì tắt (đã duyệt ngưỡng) | **31/08** (FU-183) |
| Job huấn luyện CN 02:00 | Đã xác minh ĐẠT 02/08; bảng ghi AUC thật | Đã đóng FU-211 |
| Bộ tự kiểm nhất quán | Cron 18:05, 16 phép | Hàng ngày |
| Dịch vụ `lottery` | Health 200 lúc tra | — |

---

## 8. Việc nên làm tiếp — đề xuất xếp ưu tiên

1. **Giữ dừng đặt tiền và giữ đóng băng đường ra số tới 08/08.** Đây không phải thụ động — đây là điều kiện để số liệu 7 ngày có nghĩa.
2. **Ngày 08/08: một phiên đọc kết quả FU-186 / FU-184 / FU-203**, rồi mới quyết mở khóa gì. Không quyết sớm.
3. **Sau 08/08: đào FU-210 + FU-212** (MT từng thắng rồi mất; tín hiệu còn nhưng không thành số). Đây là hướng duy nhất có bằng chứng lợi thế thật trong quá khứ.
4. **Dọn 4 checkpoint roadmap quá hạn** (đóng/hủy) để đầu mỗi phiên không còn báo nhiễu.
5. **Sửa phép so AUC (FU-213)** trước mọi ý định bật lại cổng tự gỡ model.
6. **Không** thêm/cắt model chỉ vì một tuần đẹp hoặc một bảng xếp hạng ngắn — đúng QD-013 / FU-209.
7. Tồn đọng báo cáo công khai cũ (FU-188) — làm khi rảnh sau 08/08, không chen việc đo.

---

## Cảnh báo: chỗ tài liệu cũ lệch với máy đang chạy

1. **SSOT / FU còn dòng “CHƯA DEPLOY” cho V10936–V10938** (bản ghi lúc chiều 01/08), trong khi **V10939 phía trên đã ghi ĐÃ DEPLOY tối 01/08**. Máy live khớp bản đã deploy. Đọc file dài phải lấy khối **trên cùng**.
2. **FU-201 / FU-205** vẫn ghi `READY_NOT_DEPLOYED` ở một số chỗ — lệch; bộ lọc đã lên máy tối 01/08.
3. **FU-192** vẫn `AWAITING_OWNER_OK` promote `glm-5.1` / `gpt-oss-120b`, nhưng hai model này **đã vào total sáng 01/08 (V10931)**.
4. **Mốc FINAL**: từ V10931, hạn output MT/MB là **16:58 / 17:58** (không còn 16:53 / 17:53 của V10905). Tài liệu cũ hơn vẫn có thể ghi mốc cũ.
5. **Số tiền / lợi thế 90 ngày** trong báo cáo 01/08 và số live 02/08 lệch nhẹ (cửa sổ trượt) — hướng kết luận giống nhau: cổng ĐÓNG, lỗ lớn.

---

## Nguồn đã dùng (để kiểm lại)

- `CHANGELOG.md` (V10933 → V10953)
- `docs/CURRENT_TRUTH_SSOT.md`, `docs/FOLLOW_UP_TRACKER.md`, `docs/OWNER_DECISION_LEDGER.json` (QD-013)
- Roadmap ACTIVE: CROSS_REGION_LEAKAGE, REDESIGN_20260531 (+ các file ACTIVE khác)
- Máy VPS 02/08 ~15:57: `OUTPUT_ELIGIBLE_MODELS`, `combo_super` pools, `_v10945_edge_gate.compute_view()`, `final_bundles` 01–02/08, `/api/health`, nginx `xs.io.vn`

---

*Bản này là tài liệu chỉ đọc. Không sửa code, không deploy trong phiên viết.*
