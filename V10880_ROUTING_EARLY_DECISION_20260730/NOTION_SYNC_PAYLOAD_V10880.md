# V10880 — 2 model mới 404 vì lỗi định tuyến; bỏ mốc cứng 21 ngày

**30/07/2026 · đã sửa, đã deploy, đã gọi thật xác minh**

## Trả lời câu hỏi của owner về 2 model mới: CHƯA ỔN

Cả `claude-opus-5-fast` và `gpt-5.6-sol-pro` đều **404 suốt ngày chạy đầu tiên**.

Slug em khai ĐÚNG — `anthropic/claude-opus-5-fast` và `openai/gpt-5.6-sol-pro` đều tồn tại thật trên OpenRouter. Lỗi ở **định tuyến**: V10872 khai slug trong `_call_openrouter` nhưng quên ghi tên vào `OPENROUTER_MODELS_SET` — cái quyết định model đi đường nào. Thiếu tên nên bộ điều phối rơi về nhánh tiền tố, gọi thẳng API Anthropic và OpenAI gốc bằng slug trần. Lỗi thứ hai cùng chỗ: `is_claude` không có guard `not is_openrouter` như `is_openai` đã có.

**Sau khi sửa, gọi thật:** `claude-opus-5-fast` PASS 2,2s · `gpt-5.6-sol-pro` PASS 3,8s, cả hai trả JSON hợp lệ.

Không chạy bù MN — hai lane sẽ tự chạy ở mốc MT (~17:00) và MB (~18:00) hôm nay. Chạy bù lúc 10:20 cho chúng thêm 6 giờ thông tin so với model khác, hỏng phép so cùng ngày.

`gemini-3.5-flash` cũng rỗng nhưng do Google `503 UNAVAILABLE` — hỏng 3/11 ngày gần nhất (27%), phía nhà cung cấp.

## Official 30/07 không bị ảnh hưởng

MN đã chốt `BT=86`, 15 model, consensus strong lúc 04:17:36; 23 model có số. MT và MB chưa chốt lúc 10:10 — **đúng lịch** như owner nhận định.

## Bỏ mốc 21 ngày — owner nói đúng

21 là con số em tự đặt, không tính từ dữ liệu. Chỗ nghĩ sai: coi forward là phép đo làm lại từ đầu, trong khi đã có 135 miền-ngày backfill sạch. Việc của forward chỉ là bác bỏ.

Bootstrap 20.000 lần: sau **7 ngày** P(hơn official) = 93%. Tiêu chí "lãi tuyệt đối dương" bị loại vì 31 ngày vẫn chỉ 59%.

**Luật mới:** ≥7 ngày · hơn official theo tiền 1/1 ⇒ ĐẠT · kém quá 16tr ⇒ TRƯỢT · chặn cuối 19/08.
**Sớm nhất chốt được: 05/08** — sớm hơn 14 ngày.

## Tiền đến từ đâu — lật ngược cách đọc cũ

| Nhánh | Ngày trúng | ROI 1/1 |
|---|---|---|
| nền official | 34/135 | −34,6% |
| chỉ cắt đài | 20/135 | −40,9% |
| **chỉ đổi số** | **49/135** | −0,2% |
| cả hai | 36/135 | **+4,9%** |

Động cơ là **chọn số** (+98,0tr, `t=3,20`), không phải cắt đài (+24,2tr, `t=1,36`). Cắt đài tự nó còn làm xấu đi. Sửa lại cách đọc ở V10876 vốn quy công cho chọn đài.

## An toàn

Hash 4 bảng official pre/post IDENTICAL qua 2 lần deploy. V10841 PASS. Không đụng `final_bundles`, `/choi`, selector official.

Báo cáo đầy đủ: `V10880_ROUTING_EARLY_DECISION_20260730/REPORT_V10880.md`
