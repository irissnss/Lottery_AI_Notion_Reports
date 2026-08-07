# CONVERSATION CONTEXT — V11024 · 2026-08-07 đêm

## Owner nói gì (NGUYÊN VĂN)

> lần nào cũng báo cáo vở vẩn chả kiểm tra so sánh trên vps trước mà cứ báo cáo sai lệch xong rồi
> đi tìm hiểu rồi lại xin lỗi rồi lại đào bới khổ em quá nha.
> Vấn đề ngữ cảnh, lời kể của em diễn giải như thế nào? Trước đây để có cơ chế mined Rules anh
> cũng yêu cầu như sau, em xem thêm prompt bên dưới và tiến hành theo yêu cầu dùm anh, các vấn đề
> nào nghi vấn chưa rõ em có thể tham chiếu ngược lại từ báo cáo, từ changlog ở tất cả các kênh
> trong root, trong github **em phải làm việc ở cường độ cực cao để tìm cho ra giải pháp điều
> chỉnh thật hoàn mỹ cho anh**

Kèm đề bài đầy đủ: CURRENT_ACTOR / AUTHORIZED_LAYER / FORBIDDEN_ACTIONS / R1–R10 / cổng kiểm 8 gạch.

## Phê bình của owner ĐÚNG — và phiên này chứng minh bằng số

Suốt ngày 07/08 agent báo owner prompt MB dài **12.497 → 15.617 ký tự**. Dump thật trên VPS:
**46.583 ký tự**. Sai **gấp ba**.

Nguyên nhân: agent đo `build_context_pack`, nhưng prompt THẬT gửi model là
`create_analysis_prompt` — gói `context_pack` vào cùng system prompt, doctrine, và khối
«CHỈ SỐ ĐỊNH LƯỢNG (PYTHON TÍNH SẴN)» 10.066 ký tự mà **chưa ai từng soi**.

**Hai phát hiện nặng nhất phiên này KHÔNG THỂ thấy từ local:**
- bộ đếm đo tiến bị xoá mỗi thứ Hai → nằm trong `weekly_rule_miner.py` chạy bằng cron VPS
- khối gan/hot vẫn đang bơm → nhánh `prediction_mode=='HYBRID'` chỉ chạy khi có `numpy`;
  máy local **thiếu numpy** nên khối im lặng biến mất khỏi mọi phép đo local

⇒ *"Kiểm VPS trước"* không phải hình thức, là **điều kiện cần**.

## Agent làm gì

Chạy một bộ tra soát **16 agent · 3,13 triệu token · 851 lượt gọi công cụ · 83 phút**:
- 6 agent tra soát R1–R6
- **6 agent phản biện**, mỗi agent đo lại bằng **phương pháp khác** (SQL nếu gốc là Python và
  ngược lại), được lệnh *"mặc định nghi ngờ, tìm cách chứng minh con số đó SAI"*
- 3 agent kế hoạch R7–R10 (PLAN-ONLY)
- 1 agent phê bình độ đầy đủ, soi lại cả 9 agent trên

Kết quả: **83 script** + **101 tệp bằng chứng**.

## Bốn phát hiện lật đổ nền tảng

| | |
|---|---|
| **1** | **105 luật production không phải hậu duệ chuỗi V10636.** `_seed_rules.py:432` chạy `DELETE FROM mined_rules` rồi đào lại 21 bucket × top-5. 105 luật đều `mined_at` trong **10 giây** ngày 03/08, một `source_run_id` duy nhất |
| **2** | **Bộ đếm ĐO TIẾN bị xoá mỗi thứ Hai** — `weekly_rule_miner.py:170` xoá 112 ngày rồi backfill bằng chính bộ luật vừa đào ⇒ số lượt đo tiến **không bao giờ vượt 35/miền** |
| **3** | **Cổng thăng hạng 55% nằm DƯỚI mức ngẫu nhiên** của 71/105 luật, **toàn bộ 35 luật MN** |
| **4** | **Prompt thật gấp ~3 lần** con số agent vẫn báo. Kết quả xổ thô chỉ **7,3%**; 92,7% là bóc sẵn + mệnh lệnh (**233 lần** từ khoá ra lệnh ở MB) |

## Trả lời thẳng câu hỏi của owner về giải soi cầu

**KHÔNG giải nguồn nào mang tín hiệu đo tiến.** Quét vũ trụ **60.412 lượt** không qua bộ chọn:
20/21 ô `NGANG_NEN`, **0 ô sống sót** sau hiệu chỉnh đa so sánh.

Toàn bộ "sức mạnh" là hai thứ: **nền quá cao** (MB 51,1% · MT 77,1% · MN 86,8% — `hit_any` gần
như miễn phí) và **thiên lệch chọn mẫu** (`MB·G1`: +14,3pp z=3,79 khi chấm ngược → **+0,1pp
z=0,15** khi quét vũ trụ).

**R2 đo được dấu vân tay thiên vị chọn rõ nhất:** trong cửa sổ chọn lift **1,084** (z +8,84);
ra ngoài cửa sổ lift **1,000** — lệch **6,6 lượt** trên 29.205.

## Vấp ở đâu — bốn lỗi trong CHÍNH phiên này, do agent phê bình bắt

1. **R7 tóm tắt không khớp artifact của chính nó** — khai `GỠ 8 · VIẾT LẠI 8`, thật là
   `GO 9 · VIET_LAI 10`; và **đếm chồng** (`MB HARD MODE` đã bao gồm `MB MODEL RANKING` nhưng
   vẫn tính riêng).
2. **R7 còn 43% bảng chưa động** — hai dòng lớn nhất mang nhãn `VIET_LAI` nhưng **TRƯỚC = SAU**
   (`RR-16.5` 15.465→15.465). Phần khó nhất chưa soạn mà con số "giảm 33,8%" đã được trình như
   đã làm. **§60.4 + §60.1.**
3. **R8 đo trên prompt không phải bản chạy thật** — local 49.270 vs VPS 46.583; R8 còn cảnh báo
   ngược *"VPS còn dài hơn"*.
4. **R5 và R7 mâu thuẫn về §11 RULE TAILS** — "chết 100%" vs "rỗng đúng lúc dựng prompt". Hai
   chẩn đoán dẫn tới hai cách sửa khác nhau.

Cả bốn đều đã ghi vào báo cáo thay vì giấu.

## Điều agent NÓI THẲNG với owner

**1. Thứ tự ưu tiên phải đảo.** Owner giao soạn lại ngữ cảnh. Nhưng sửa prompt trước khi sửa
**bộ đếm đo tiến bị xoá mỗi thứ Hai** thì mọi phép đo sau đó vẫn vô nghĩa. Đúng thứ tự là:
sửa cơ chế **đo** → sửa cơ chế **chọn luật** → mới tới soạn **ngữ cảnh**.

**2. Hai con số đang bơm vào prompt cho model đọc thì không tái lập được:**
`z = −0,33σ/+0,26σ` tính từ **9 và 15 cặp lệch**, và bảng gốc đã bị lần đồng bộ 18:51 xoá.

**3. Căn cứ từ chối FU-300 bước 3 bị sai:** "84/84 khoảng tin cậy chứa 0,50" — đo lại ra
**80/84**, và **không tồn tại script gốc** nào sinh ra con số 84/84.

**4. V11001 chưa gỡ hết gan/hot.** `format_condensed_stats` vẫn sinh `TOP 5 GỢI Ý
(Score/Zone/Trend/Gan)` + `⏳ GAN CAO` + `🔥 HOT`, và `gpt_analyzer.py:2229` vẫn bơm khi
`prediction_mode=='HYBRID'`. Đây là §60.1 lần thứ hai với cùng một việc.

**5. Cửa sổ đo 14 ngày không đủ sức** cho ngưỡng "tụt ≥5 điểm" mà chính FU-284 khai — với
VIF 2,92× thì 14 ngày chỉ phát hiện được chênh **≥8,76 điểm**; muốn thấy 5 điểm cần **44,1 ngày**.

**6. Agent KHÔNG đề xuất sửa gì trong phiên này** — đề bài là READ-ONLY + PLAN-ONLY, và bốn phát
hiện nền tảng làm thay đổi hẳn thứ tự ưu tiên. Trình để owner quyết, không tự làm.
