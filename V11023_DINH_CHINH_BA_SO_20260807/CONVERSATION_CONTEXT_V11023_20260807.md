# CONVERSATION CONTEXT — V11023 · 2026-08-07 đêm

## Owner nói gì (NGUYÊN VĂN)

> FU312 là gì sao để sai vậy anh đã nói output tối đa của MB là 17h58 rồi mà em, **Đủ thời gian
> cho các model Ai chạy song song 5 model 1 lượt mà em.**
> C4-C5 **xử lý dứt điểm** dùm đi
> FU215 em phải **kiểm tra xác thực rõ ràng từ số liệu** chứ sao anh chốt được.
> FU 290 thì trước mắt **vẫn chưa cắt** anh sau khi điều chỉnh prompt cần model Ai hiểu ngữ cảnh,
> và thông minh để chạy shadow đo là chọn lựa **thay thế** các model tệ nha em. **Các model cao
> cấp nhất ah em có thinking nha em.**
> FU328 đơn giản em canh và **tự xử lý** nha
> Phần bên dưới em thử sao anh **chỉ có xử lý MB thôi** ah em và em **chưa tổng hợp lại hoàn hảo
> và nhất quán** anh thấy cảnh báo độ trùng như thế thì có vẻ đang nhấn mạnh hơn những đoạn khác.
> […] rồi các vấn đề em để trạng thái hỏng đề xuất như thế nào? anh cũng **chưa thấy chi tiết
> diễn giải cụ thể** để cùng em xử lý ah em

## Owner nghi ba chỗ — CẢ BA đều là agent sai

### 1. FU-312 — owner đúng

Agent báo *"lane MB chạy 17:38 nên chấm thiếu model, sai 4/7 ngày"*.

Sự thật, đọc từ crontab VPS:

```
_v10879_nghiemthu_lane --predraw --region MB
  17:38 · 17:42 · 17:46 · 17:50 · 17:54       hạn official 17:58
```

**Năm lượt**, lượt cuối cách hạn cứng **4 phút**. Lane chỉ mở khi official đã chốt, nên official
xong 17:45 thì lượt 17:46 bắt được. **Agent đọc MỘT dòng cron rồi kết luận cả cơ chế.**

FU-312 → `CLOSED_NO_DEFECT`.

### 2. C4 · C5 — cổng MÙ, không phải hệ hỏng

`_crontab()` chạy `crontab -l` trên **máy đang chạy**; cron nằm ở **VPS**. Chạy local ⇒ rỗng ⇒
C4·C5·C6 báo LỆCH. Agent đã báo owner *"khoá /choi rỗng"* và *"trang web đang hiển thị sai giờ"*
— **cả hai bịa ra từ một cổng mù**.

Chạy đúng trên VPS: **20 đạt / 2 lệch**, C4 và C5 **sạch**. Bằng chứng: `_v10834_lock_freeze` có
đủ `15:43 · 16:56 · 17:56`; `LANE_SCHEDULE` khớp crontab từng phút.

**Sửa dứt điểm:** cổng không đọc được crontab thì **không đo và không báo lệch**, in rõ *"chạy
trên VPS mới đo đủ"*.

### 3. «10 → 4» không tái lập

Đo trên DB **trước** lượt đồng bộ 18:50. Đo lại 4 bản × 3 miền trên cùng nền dữ liệu mới:
MB **14→10** · MT **9→3** · **MN 1→2 — tệ hơn**.

Thứ giảm chắc chắn nhất là **mệnh lệnh 6–7 → 1** ở cả ba miền.

## «Sao chỉ xử lý MB» — owner đúng, agent chỉ đưa số MB

Bảng trong trang chỉ có MB. Nay có đủ **4 bản × 3 miền**, cùng một thước, cùng một nền dữ liệu.
Và số MN cho thấy **MN không cải thiện** — chỗ đó agent đã im lặng bỏ qua.

## FU-215 — số liệu owner cần

QD-014 nguyên văn: *"cần **một tuần yên** để biết chúng có tác dụng gì không"*.

⇒ Câu hỏi thật là **«tuần yên đó có xảy ra không»**. Đếm: **6 lần đổi `gpt_analyzer.py` trong 7
ngày đóng băng** (V11001 · V11007 · V11008 · V11014 · V11016 · V11022).

**Tuần yên chưa từng xảy ra.** Agent trình hai lựa chọn kèm số, không tự quyết.

## FU-290 — owner đổi hướng

Từ «cắt model yếu» sang «**thử model mạnh có thinking ở shadow để THAY model yếu**». Theo §59
đây là **thêm ứng viên vào shadow**, không phải «bỏ cờ» cũng không phải «dừng hẳn».

## Vấp ở đâu — một kiểu lỗi, ba lần

| # | agent đo bằng | lẽ ra phải đo bằng |
|---|---|---|
| 1 | một dòng cron `17:38` | **liệt kê hết** các lượt |
| 2 | `crontab -l` trên **local** | crontab trên **VPS** |
| 3 | DB **trước** đồng bộ | DB **sau** đồng bộ |

Và tệ hơn cả ba: agent **đưa cả ba vào báo cáo như sự thật đã kiểm chứng**, kèm đề xuất đi sửa
thứ không hỏng. Nếu owner không nghi thì agent đã dời lane MB — một cơ chế đang chạy đúng.

## Điều agent NÓI THẲNG với owner

**1. Owner đang phải làm việc kiểm chứng thay agent.** Ba lần trong một báo cáo. Đây không phải
lỗi kỹ thuật lẻ mà là **thói quen kết luận trước khi đủ dữ liệu**.

**2. MN không cải thiện** — trùng lặp 1→2, tệ hơn một chút. Agent đã không nói ra ở báo cáo
trước vì chỉ trình số MB.

**3. FU-215 agent không tự quyết** đúng như owner yêu cầu — chỉ đưa số và hai lựa chọn.

**4. FU-328 đã tự xử lý** như owner giao: cổng đã dựng, thử hai chiều đạt. Còn gắn cron và panel.
