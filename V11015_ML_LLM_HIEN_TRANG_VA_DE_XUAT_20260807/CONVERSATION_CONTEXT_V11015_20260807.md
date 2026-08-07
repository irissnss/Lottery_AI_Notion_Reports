# CONVERSATION CONTEXT — V11015 · 2026-08-07

## Owner nói gì (NGUYÊN VĂN)

> ML và LLM đã làm được gì rồi? hiện tại và tương lại đề xuất là gì .
> - Với ML ngoài xác xuất thống kê thuần , anh quan tâm đến đối chứng với rules , bộ lọc để so
> sánh đối chiếu để output số chính và yêu hơn là số phụ, với ML cắt retrrain tuần thì retrain
> sẽ học lại ở thời điểm nào? làm sao kiểm soát nếu sau 1 tháng hoặc 3 tháng mới retrain thì làm
> sao biết nó có hoạt động.
> - Với LLM ngoài ngũ cảnh có sẵn, các số học được nhồi nhét cần biến thành ngữ cảnh thực sự để
> model đọc hiểu tự phân tích, tự tư duy tự tra soát trong ngưỡng tự quyết định output số tốt
> nhất ở số chính và nhẹ hơn là số phụ, tất cả tự nhiên có quy luật có điều kiện, đừng output
> theo số gò như thế dẫn đến bầy đàn là đúng rồi, lùa vào 1 bộ số định sẳn trong ngày để model
> quyết định xong thấy bầy đàn.
> ==> Em làm được gì và cần gì phải rõ ràng

## Agent làm gì

1. **Không trả lời từ trí nhớ.** Viết script đọc thẳng `FEATURE_COLUMNS` của
   `meta_data_collector.py`, đếm tham chiếu rules trong 7 tệp ML, truy `training_history`.
2. Phân nhóm 39 đặc trưng ML theo họ để thấy cái nào là gì.
3. Đối chiếu tầng ML với tầng LLM — và ra chỗ mâu thuẫn.
4. Trả lời theo đúng ba câu owner hỏi, kèm phần **"làm được gì / cần gì"** tách bạch.

## Bốn sự thật về ML

| | |
|---|---|
| **39 đặc trưng**, tất cả dẫn xuất từ số đã ra | tần suất · gan · xu hướng · hội tụ · lag · rolling · thứ · chéo miền |
| **0/34 model hơn nền** | AUC 0,48–0,56 qua **228 lượt** học lại |
| **KHÔNG đối chứng rules, KHÔNG qua bộ lọc** | 7/7 tệp ML: `mined_rule = 0` · `bộ_lọc = 0` |
| **KHÔNG tự phân biệt chính/phụ** | `secondary`/`top1`/`top2` = 0 lần trong `ml_predict.py` |

## Phát hiện mới — hai tầng chạy theo hai niềm tin trái ngược

| tầng | gan / nóng / lạnh |
|---|---|
| LLM prompt | **đã gỡ hết** (V11001 + V11007) |
| ML đặc trưng | **vẫn còn 6** — `gan_score_w` · `gan_days` · `gan_vs_avg` · `zone_encoded` · `freq_x_gan` · `trend_x_zone` |

Owner nói *"gan, cold, hot chả tích sự gì"*, agent gỡ khỏi prompt rất kỹ — quét ngược, phân
loại, cổng kiểm — **nhưng chưa hề soi tầng ML**.

## Vấp ở đâu

### Lỗi §60.2 câu 1 lặp lại

*"Ai còn trỏ tới thứ này?"* — agent soi rất kỹ **trong một tầng** rồi coi như xong. Lần trước là
quên tầng gọi bao ngoài của `include_same_day`; lần này là quên **cả một tầng ML**.

### Agent mới làm nửa việc LLM

V11014 bỏ mệnh lệnh ép chọn — cần, nhưng **chưa đủ**. Prompt vẫn đưa **rổ 10 số dọn sẵn**:

```
Các luật của bucket MB/Thứ Sáu hôm nay trỏ tới 10 đuôi: 13 31 32 35 60 69 84 88 89 95
```

Chừng nào còn rổ số đó thì model vẫn bị neo. Owner nói đúng bản chất: *"lùa vào 1 bộ số định sẵn
trong ngày để model quyết định xong thấy bầy đàn"*.

## Điều agent NÓI THẲNG với owner

**Owner hỏi ba câu, agent trả lời được cả ba — nhưng hai câu đầu ra kết quả không đẹp:**

1. *ML có đối chứng rules/bộ lọc không?* — **KHÔNG**, 0/7 tệp.
2. *ML có phân biệt chính/phụ không?* — **KHÔNG**, nó trả về danh sách xếp hạng.
3. *Cắt retrain tuần thì kiểm soát thế nào?* — hiện **chỉ có lịch + chốt chặn tuổi model**;
   agent đề xuất **canh trôi hằng ngày** để kích hoạt học lại theo trôi thay vì theo lịch, cộng
   bản đóng băng chấm **hằng tháng**. Khi đó không bao giờ phải chờ một tháng mới biết.

**Ba việc agent làm được ngay, không cần owner duyệt:** tầng đối chứng ML×rules×bộ lọc (đo
shadow) · canh trôi đặc trưng hằng ngày · đo cơ chế V11014 tối nay.

**Một câu agent cần owner trả lời:** **L-A (đổi số thành lời kể) làm ngay hay chờ 21/08?**
Làm ngay thì FU-284 thành đo gộp **ba** biến, hết tách nhân quả. Chờ thì giữ phép đo sạch nhưng
đợi thêm 2 tuần. Agent nghiêng về **làm ngay** và nói rõ đánh đổi thay vì tự quyết.
