# V10880 — Hai model mới 404 vì lỗi định tuyến; bỏ mốc cứng 21 ngày

**Ngày:** 30/07/2026 · **Trạng thái:** đã sửa, đã deploy, đã gọi thật xác minh

---

## 1. Owner hỏi gì

> *"nếu như em đề xuất ban đầu tốn 21 ngày rồi lại live giờ chạy song song mà vẫn báo chưa đủ mẫu, đề xuất của anh còn trung thực còn rút ngắn thời gian live hơn mà chưa ổn nữa ah em. Vậy em đã làm hết chưa đó, total MN có vẻ tại thời điểm giờ là đã chốt rồi, còn MT và MB thì phải đợi đúng quy trình mốc giờ để có đủ nhé em. Đầu ngày kiểm tra toàn diện tổng lực dùm anh nhé, các model new mới add hoạt động ổn đúng chưa sao anh chưa thấy báo cáo em?"* — 30/07 10:07

---

## 2. Hai model cao cấp mới KHÔNG hoạt động

Hôm nay 30/07 là `first_run_date` của hai lane thêm ở V10872. Cả hai chạy lúc 04:22 và **trả rỗng**:

| Model | Lỗi trả về |
|---|---|
| `claude-opus-5-fast` | `404 not_found_error: model: claude-opus-5-fast` — từ **API Anthropic gốc** |
| `gpt-5.6-sol-pro` | `404 model_not_found` — từ **API OpenAI gốc** |

### Slug không sai — định tuyến mới sai

Dò `/models` của OpenRouter xác nhận cả hai đều tồn tại thật:

```
anthropic/claude-opus-5-fast   ctx 1.000.000   $10/M in   $50/M out
openai/gpt-5.6-sol-pro         ctx 1.050.000   $5/M in    $30/M out
```

Lỗi nằm ở chỗ khác. V10872 có khai slug trong `OPENROUTER_MODEL_MAP`, nhưng dict đó nằm **bên trong** hàm `_call_openrouter` — nó chỉ dịch tên *sau khi* đã quyết định đi đường OpenRouter. Cái quyết định đi đường nào là `OPENROUTER_MODELS_SET`, và em **quên ghi hai tên vào đó**.

Thiếu tên trong set nên bộ điều phối rơi về nhánh phán đoán theo tiền tố:

```python
is_claude = selected_model.startswith("claude")          # → Anthropic gốc
is_openai = not is_openrouter and selected_model.startswith("gpt")   # → OpenAI gốc
```

Cả hai bị gọi tới nhà cung cấp gốc bằng slug trần, nơi không có tên đó.

### Lỗi thứ hai cùng chỗ

`is_claude` **không nhường** OpenRouter, trong khi `is_openai` và `is_deepseek` đều đã có `not is_openrouter`. Nghĩa là kể cả sau khi thêm tên vào set, mọi model `claude-*` vẫn bị bắt về Anthropic. Đã vá cả hai, và thêm guard cho `is_gemini` để nhất quán.

### Gọi thật sau khi sửa

```
PASS claude-opus-5-fast   2,2s   122 token    {"main_numbers":["07","31"],"ok":true}
PASS gpt-5.6-sol-pro      3,8s   1854 token   {"main_numbers":["07","31"],"ok":true}
```

### Không chạy bù MN — cố ý

Hai lane thuộc slot `completion_triggered_shadow`, nên các mốc MT (~17:00) và MB (~18:00) hôm nay sẽ tự chạy bằng code đã sửa. Riêng MN 30/07 mất, và em chấp nhận mất: chạy bù lúc 10:20 sẽ cho hai model này thêm sáu giờ thông tin so với các model chạy lúc 04:22, làm hỏng phép so cùng ngày trong bảng chất lượng.

### Lưu ý khi đọc bảng chất lượng

Hai model sẽ hiện **tỷ lệ hỏng 100%** cho tới khi có dòng tốt đầu tiên. Đó là hậu quả của lỗi định tuyến, không phải chất lượng model.

---

## 3. `gemini-3.5-flash` cũng rỗng — nhưng lỗi phía Google

```
503 UNAVAILABLE: This model is currently experiencing high demand.
```

Không phải lỗi hệ thống. Tần suất 10 ngày gần nhất: hỏng ngày 30/07, 28/07, 24/07 — **3/11 ngày, khoảng 27%**. Ghi nhận theo dõi, chưa xử lý vì đây là lane shadow.

---

## 4. Official 30/07 không bị ảnh hưởng

| Miền | Trạng thái lúc 10:10 |
|---|---|
| MN | **Đã chốt** `BT=86`, `lo2=["86","31"]`, `model_count=15`, `weighted_voting_wr`, consensus **strong**, lúc 04:17:36. 23 model có số. |
| MT | Chưa chốt — **đúng lịch**, mốc ~17:00 |
| MB | Chưa chốt — **đúng lịch**, mốc ~18:00 |

Cả ba model rỗng đều là shadow, nằm ngoài bundle. Nhận định của owner về MN đã chốt còn MT/MB phải đợi mốc giờ là chính xác.

---

## 5. Bỏ mốc cứng 21 ngày — owner nói đúng

Em lấy ý owner về việc chạy song song nhưng vẫn giữ nguyên đồng hồ 21 ngày. Vậy thì không rút ngắn được gì. Con số 21 là em tự đặt, không tính từ dữ liệu nào.

### Chỗ nghĩ sai

Em coi giai đoạn forward như một phép đo **làm lại từ đầu**. Không phải. Đã có 135 miền-ngày backfill nhân quả sạch trên đúng cấu hình này, và riêng bộ chọn số de-herd còn có 267 ngày ở V10872. Việc của forward chỉ là **bác bỏ**: bắt lỗi cài đặt giữa backtest và chạy thật, bắt đổi chế độ thị trường. Câu hỏi bác bỏ cần ít mẫu hơn hẳn câu hỏi đo mới.

### Bootstrap 20.000 lần trên chính backfill

| Sau | P(hơn official) | P(lãi tuyệt đối > 0) |
|---|---|---|
| 3 ngày | 83% | 49% |
| **7 ngày** | **93%** | 53% |
| 15 ngày | 98% | 55% |
| 30 ngày | 100% | 59% |

Tiêu chí "lãi tuyệt đối dương" **không bao giờ chốt nổi**: biến động ±2,437tr mỗi miền-ngày so với trung bình chỉ +0,066tr. Hơn 31 ngày vẫn chỉ 59%. So theo **cặp với official** mới là phép đo có sức mạnh.

### Luật đăng ký trước 30/07

- Tối thiểu **7 ngày** forward.
- Hơn official theo tiền 1/1 ⇒ **ĐẠT**, đủ điều kiện trình owner duyệt lên official.
- Kém quá 16 triệu (phân vị 5% của dải bootstrap) ⇒ **TRƯỢT**, phải soi lại cài đặt.
- Hạn chót 19/08 giữ nguyên làm chặn cuối.

**Sớm nhất chốt được: 05/08/2026** — sớm hơn 14 ngày so với mốc cũ.

---

## 6. Tách nguồn lợi thế — kết quả lật ngược cách đọc cũ

Bảng 2×2 trên 135 miền-ngày, chuẩn 1/1:

| Nhánh | Ngày trúng | Chi | Lãi | ROI |
|---|---|---|---|---|
| nền official (số official, hết đài) | 34/135 | 284,9tr | −98,7tr | −34,6% |
| chỉ cắt đài (số official) | 20/135 | 182,2tr | −74,5tr | −40,9% |
| **chỉ đổi số (hết đài)** | **49/135** | 284,9tr | −0,7tr | −0,2% |
| cả hai = NGHIỆM THU | 36/135 | 182,2tr | +8,8tr | **+4,9%** |

**Động cơ là chọn số, không phải cắt đài.** Cùng bộ đài, số de-herd trúng **49 ngày** so với **34 ngày** của official. Đóng góp +98,0tr với `t≈+3,20`.

Cắt đài chỉ đóng góp +24,2tr, `t≈+1,36` — chưa đủ mạnh, và **tự nó còn làm xấu đi** (−40,9% so với nền −34,6%). Nó chỉ có ích khi đi cùng số de-herd, vì bộ chọn đài học trên chính chuỗi trúng của de-herd.

Điều này sửa lại một cách đọc sai trước đó của em: ở V10876 em quy công cho việc chọn đài. Con số nói ngược lại.

---

## 7. An toàn

Hash 4 bảng official trước/sau **giống hệt** qua cả hai lần deploy:

```
predictions       11287  f3b649b6bb472f63
final_bundles       457  1e54985da004e902
lottery_results   15173  ba42b58e9fc148fa
model_daily_eval  11111  5f034cce2676713e
```

`V10841_CONTRACT_PASS` · `/api/health=200` · `/du-doan=200` · `/api/admin/nghiemthu-1908=401`. Backup tại `.local_backup_v10880` và `.local_backup_v10880b`. Không đụng `final_bundles`, `/choi`, hay selector official.

---

## 8. Cần theo dõi

| Việc | Khi nào |
|---|---|
| Kiểm 2 model có dòng MT và MB không rỗng | Tối 30/07 |
| Đọc phán quyết luồng Nghiệm Thu | 05/08 |
| `gemini-3.5-flash` hỏng 27% do Google | Theo dõi liên tục |
| Chốt lên official | 19/08 (chặn cuối), có thể sớm từ 05/08 |
