# CONVERSATION CONTEXT — V11031 · 2026-08-08

## Owner nói gì (NGUYÊN VĂN)

> Kiểm tra phân tích đánh giá nhân xét đầu ngày , đề xuất xử lý tiếp là gì

## Agent làm gì

1. Chạy `_v10920_session_start.py` — báo **18 mục quá hạn · 9 đến hạn hôm nay · 5 mồ côi ·
   5 quyết định tới hạn rà soát**.
2. **Cổng RM-01 chặn:** manifest local **cũ 13,6 giờ > 6 giờ** ⇒ **từ chối đo** ⇒ chạy
   `web/_sync_live_forensic_inputs.py` trước. Đây là lần đầu cổng này thật sự chặn một phiên.
3. Dựng 6 mũi soi song song + phản biện đối kháng cho mọi phát hiện nặng — **29 agent, 2,62
   triệu token, 712 lượt gọi công cụ, 0 lỗi**.
4. **Tự kiểm lại phát hiện nặng nhất**, không tin agent con.

## Phát hiện nặng nhất — và vì sao agent chính phải tự làm lại

Agent con báo: *"context pack vỡ ở chế độ bóng, 908 lượt, official 9/21"*. Đúng — nhưng **thiếu
hai chi tiết quan trọng nhất**, và chính hai chi tiết đó mới trả lời được câu *"vì sao 67 ngày
không ai thấy"*:

| chi tiết agent con bỏ sót | vì sao nó quan trọng |
|---|---|
| Chuỗi báo lỗi dài **đúng 64 ký tự**, cổng canh là `len(...) > 50` | **64 > 50 nên LỌT**. Cổng dựng ra để bắt "không có ngữ cảnh" bị đánh bại bởi chính chuỗi báo lỗi |
| Log in ra `[CONTEXT_PACK] Injected 64 chars` | **màu xanh cho một thất bại toàn phần** — không ai đi soi một dòng log báo thành công |

Agent chính đọc `gpt_analyzer.py:4681` vs `:4761` vs `:5575` vs `:6272` mới ra được.

## Bằng chứng tự dựng — ba tầng

**Tầng 1 — đọc code:** dòng `4681` mở **11 biến**, dòng `4761` mở **10 biến**, cùng một `rules`
từ câu SELECT **11 cột** (`4662–4676`).

**Tầng 2 — chạy hàm production thật, hôm nay:**

```
MN  shadow=False   9.935 ký tự  OK       MN  shadow=True    64 ký tự  *** VỠ ***
MT  shadow=False   9.948 ký tự  OK       MT  shadow=True  12.927     OK
MB  shadow=False   9.610 ký tự  OK       MB  shadow=True    64 ký tự  *** VỠ ***
'\n## CONTEXT PACK — Lỗi: too many values to unpack (expected 10)\n'
```

**MT không vỡ là bằng chứng CỦNG CỐ, không phải phản chứng:** thứ Bảy MT có **0 luật
`READY_STRONG`** ⇒ `rules` rỗng ⇒ vòng lặp không chạy. Đếm luật ra MN `T7=2` · MT `T7=0` ·
MB `T7=1` — khớp đúng ba kết quả.

**Tầng 3 — dấu vân tay lịch sử:** `prediction_trace.jsonl` có **908/4.897 lượt** với
`context_pack_chars` **đúng bằng 64**, và **không một giá trị nào khác dưới 200**. Từ **02/06**
tới **08/08 05:41 sáng nay**.

## Vấp ở đâu

| # | vấp | sửa |
|---|---|---|
| 1 | Đoán `predictions.model_name` — cột thật là **`ai_model`** | `PRAGMA table_info` (RM-10) |
| 2 | Đoán `final_bundles.target_region` — cột thật là **`region`** | như trên |
| 3 | Trace **không có `run_source`** ⇒ suýt đọc 908 thành 908 lượt official | join trace × `predictions` theo `(date, region, model)` ⇒ ra **9** |
| 4 | Một mũi soi báo *"cổng tuổi dữ liệu chưa có dòng code nào"* — sai, khuôn đã tồn tại dưới tên khác | phản biện bác được (RM-10) |
| 5 | `cd web/backend` rồi mở DB đường dẫn tương đối ⇒ `unable to open database file` | dùng `os.path.abspath` |

## Điều agent NÓI THẲNG với owner

**1. Agent KHÔNG tự vá, dù lỗi đã rõ mười mươi.** `gpt_analyzer.py` bị **QD-041** khoá md5 tới
21/08 — chính owner ký hôm qua vì prompt đã chồng **sáu lần** trong bảy ngày. Vá là phá cửa sổ
đo. Lỗi đã sống **67 ngày**, thêm 13 ngày không đổi bản chất; **mất 14 ngày đo thì không mua lại
được**. Đây là **chữ ký của owner, không phải việc agent tự chọn**.

**2. Cổng đóng băng đang KHÔNG bảo vệ gì cả.** `_v11028_cong_dong_bang.py` **không có trong
`.cursor/hooks.json`** — chỉ chạy khi gọi tay. Cổng chạy tay là cổng không tồn tại.

**3. Sổ quyết định tự mâu thuẫn mà bộ kiểm báo toàn 🟢.** Ba mục đóng băng ngược nhau cùng
`ACTIVE` (`QD-041` đóng · `QD-029` *"mở nha em"* · `OD-20260801-D` đóng). Bộ kiểm chỉ đối chiếu
**quyết định × code**, **chưa bao giờ quyết định × quyết định** — đúng lỗi `CLAUDE.md` đã ghi về
`_v10925_rule_sync_check`.

**4. Bảy ngày qua không có gì để khen.** MN 46,8% nghe hay nhưng **nền MN đã là 42,8%**.
MT 27,0% trên nền 35,4% — **đang thua nền**. Cả ba miền, cả ba cửa sổ đo: **NGANG NỀN**.

**5. Và đây là con số owner nên nhớ:** MN tuần 25→31/07 là **−16,2 điểm (z = −1,98)**, tuần
01→07/08 là **+4,1 điểm (z = +0,51)**. **Đảo 20 điểm giữa hai tuần liền kề**, n≈105 mỗi tuần.
Mọi kết luận rút từ một cửa sổ 7 ngày đều là **nhiễu** — đây là bằng chứng số cho **RM-04**.

**6. Máy thì khoẻ, đừng nhầm hai chuyện.** `lottery` active, PID 1004216, `NRestarts=0`,
health 200, 83 cron sống, **0 dòng trỏ vào file đã mất**, 0 lỗi journal 24h, `OD-20260801-B` đã
thực thi đủ **6/6 lane**, md5 ba tệp khớp tuyệt đối local = VPS. **Hạ tầng không phải vấn đề.
Thước đo mới là vấn đề.**
