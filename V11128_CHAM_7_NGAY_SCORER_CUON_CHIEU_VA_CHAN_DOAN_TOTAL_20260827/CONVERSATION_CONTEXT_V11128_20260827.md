# CONVERSATION CONTEXT — V11128 · 27/08/2026

> Nguyên văn lời owner · agent làm gì · vấp ở đâu (§57.2). Giờ **Việt Nam (UTC+07:00)**.
> `ACTOR_RUNTIME = CLAUDE_CODE`.

---

## 1 · Owner nói gì — nguyên văn

Prompt tổng lực lần 41, hiệu lực **27/08/2026 18:48 ICT**:

> *« Đây là phiên THỰC THI MỘT LƯỢT, không phải phiên viết thêm kế hoạch. »*
>
> *« Kết luận: Ưu tiên sửa ranking/TOTAL, không thêm model. Giữ M0_CURRENT official. »*
>
> *« Trước khi đọc kết quả phải đăng ký: Effect cần phát hiện. Power/cỡ mẫu. Cửa sổ. Stop rule.
> Promotion gate. Multiple-comparison correction. Ngày đọc lại. »*
>
> *« Phép đo phải có negative control và kiểm tập rỗng. »*
>
> *« Thiếu lực thì ghi `INSUFFICIENT_POWER`. Không được đổi thành "model vô dụng". »*
>
> *« lstm giữ riêng; không hard-collapse; chấm theo unique-save và tính độc lập nguồn. »*
>
> *« Không hỏi Owner việc Agent tự tra được. Không dừng ở plan-only nếu hành động an toàn đã đủ
> gate. »*
>
> *« Thiếu evidence phải ghi `NOT_VERIFIED` hoặc `NOT_SCORABLE`. Cấm lấp bằng Notion hoặc report
> cũ. »*

Bằng chứng Owner đưa vào: nền ngẫu nhiên 33,6 % · trung bình model 32,3 % · FINAL BT 30 ngày
33,0 % · 365 ngày 34,2 % · top-10 chứa số đúng 98,1 % · rank-1 thật 33,1 % ·
**random pick trong chính pool 34,55 %**.

---

## 2 · Agent làm gì

| chặng | việc | kết quả |
|---|---|---|
| 1 | preflight | 19:08 · ngoài block · runtime hash **khớp V11127** ⇒ `FU-438` không regression |
| 2 | chấm 21–27/08 | BT 6/21 · X2 1/21 · X3 0/20 · **3-càng `NOT_SCORABLE`** |
| 3 | **phép đo quyết định** | n=273 · FINAL 30,77 % vs pool-random 33,72 % · đối chứng đạt |
| 4 | chẩn đoán scorer | settlement **đã** cuốn chiếu; chỉ bước đồng bộ bị dồn 20:20 |
| 5 | deploy scorer | +23 dòng · PID → 2671007 · 3 job đăng ký |
| 6 | roster verdict | 16 `KEEP_OFFICIAL` · 14 `SHADOW_MEASURE` · 0 trên/dưới nền |
| 7 | phát hành | báo cáo này |

---

## 3 · Vấp ở đâu — kể cả vấp do chính agent gây ra

### V1 · 🔴 Agent dựng một nhãn chẩn đoán rồi **tự bác nó ngay**

Bảng phân loại đầu cho `RANKING_MISS = 14/21` — nghe như bằng chứng đanh thép rằng ranking hỏng.

**Nhưng nhãn đó vô giá trị.** Với nền ~33 % và 16 model, xác suất *«có ít nhất một model top-1
đúng»* là `1 − 0,67^16 ≈ 99,8 %` — **xảy ra gần như chắc chắn kể cả khi ranking hoàn hảo**.

Nếu công bố `14/21` như một phát hiện, Owner sẽ đầu tư sửa ranking dựa trên một con số **không
phân biệt được** giữa hệ thống tốt và hệ thống ngẫu nhiên.

Câu hỏi đúng phải là: *FINAL có tốt hơn **bốc bừa từ chính pool** không?* — và đó là mục 4 của
báo cáo.

### V2 · 🔴 Script deploy của agent in `RUNTIME_PROVEN` **sai**

Bộ đếm lỗi không tính hai phép: `model_daily_eval` vẫn 0, và không tìm thấy dòng log đăng ký.
Script vẫn kết luận `RUNTIME_PROVEN`.

Trạng thái **đúng** là `RUNTIME_LOADED`: tệp đã nạp, 3 job đã đăng ký (APScheduler ghi rõ), nhưng
**ba mốc chưa nổ lần nào** vì 16:50/17:45/18:45 đã trôi qua trước khi deploy lúc 19:15. Bằng
chứng hành vi sẽ có **16:50 ngày mai**.

Đã sửa nhãn trong báo cáo mục 5.4.

### V3 · 🔴 `grep` trả `0` và suýt thành *«job không đăng ký»*

Phép kiểm log tìm chuỗi tiếng Việt có dấu qua `journalctl | grep` trả **0**, trong khi APScheduler
**thực sự** đã ghi ba dòng `Added job "Per-Model Eval cuốn chiếu sau MN (16:50)"`.

Đó là **hiện vật mã hoá của `grep` với dấu tiếng Việt**, không phải vắng mặt. Đúng họ với `RM-15`:
phép kiểm không có đối chứng thì con số `0` là **vô nghĩa**, không phải bằng chứng.

### V4 · 🔴 Giả định về scorer **sai chỗ**

Vào phiên, tiền đề là *«scorer không chấm cuốn chiếu»*. Đo thật thì **settlement ĐÃ cuốn chiếu
đúng từng miền** — `verified_at` trùng **đúng giây** kết quả về ở cả ba miền. Chỉ bước đồng bộ
bảng chấm bị dồn 20:20.

Nếu không đo mà đi refactor hàm chấm theo giả định, agent sẽ sửa nhầm chỗ trên một tệp 470 KB
nằm trong đường sinh dự đoán — rủi ro cao mà không giải quyết đúng vấn đề.

Chẩn đoán đúng làm bản vá **teo từ "viết lại hàm" xuống "thêm 3 dòng lịch"**.

### V5 · Truy vấn nhiều dòng qua SSH bị hỏng

Lặp lại lỗi của phiên trước. Xử bằng truy vấn một dòng.

---

## 4 · Điều agent **không** làm, và vì sao

| không làm | vì sao |
|---|---|
| dựng TOTAL-N1/N2/N3 | phép đo cho thấy **pool không mang tín hiệu để xếp** — xây ba bộ xếp hạng cho pool ngẫu nhiên là **tối ưu hoá nhiễu**. Đã đăng ký **trước** rằng kỳ vọng tiên nghiệm là thấp, và trình bày lại thứ tự ưu tiên (mục 4.5) |
| promote hay retire model nào | **0 model** có KTC trên nền, **0 model** dưới nền ⇒ cắt là cắt mù |
| dừng `gpt-5.5` / `qwen3-max-thinking` | đo ra chúng **đã ở ngoài đường official** — 0 mẫu chính. Không có gì để dừng |
| hard-collapse `lstm` | Owner khoá giữ riêng |
| GĐ-5 prompt thuần ngữ cảnh | `§60.1` — 32 khối, làm nửa vời còn tệ hơn không làm; và cần đo bằng chính thước ở mục 4.1 mới có nghĩa |
| sửa `main.py` | không cần — `FU-438` đã xong ở V11127, chỉ smoke xác nhận |
| ghi vào production DB | mọi truy vấn `-readonly` + chặn từ khoá ghi phía client |
| lấp 3-càng bằng nguồn khác | không có writer ⇒ **`NOT_SCORABLE`**, ghi thẳng |
| CLASS C (SSH · rotation) | chặn ở `RECOVERY_PATH = NOT_VERIFIED` |

---

## 5 · Trạng thái cuối

| | |
|---|---|
| `main.py` runtime | `ec2540331be1…` — **khớp V11127**, `FU-438` nguyên vẹn |
| `scheduler.py` runtime | `a6c8bfff60b6…` — bản mới, 3 job đăng ký |
| MainPID | **2671007** · health **200** |
| production DB | **không ghi một dòng nào** |
| prediction / FINAL | **không drift** |
| credential · SSH · hook · Notion | **KHÔNG ĐỔI** |
| scorer cuốn chiếu | **`RUNTIME_LOADED`** — hành vi chứng minh **16:50 ngày 28/08** |

---

TanPhatAI cần làm: ghi **phép đo quyết định** vào sổ — FINAL **30,77 %** vs bốc ngẫu nhiên từ chính pool **33,72 %** vs nền **33,87 %**, n=273, đối chứng **0 %/100 %**; và ghi rằng **coverage 99,6 % không phải thành tích** mà khớp đúng kỳ vọng ngẫu nhiên. Mở mục theo dõi **scorer cuốn chiếu** với mốc kiểm **16:50 ngày 28/08** — **đừng** ghi `RUNTIME_PROVEN` trước lúc đó. Ghi **3-càng `NOT_SCORABLE`**. **Đừng** đọc *«`RANKING_MISS` 14/21»* thành *«ranking hỏng»* — agent đã tự bác nhãn đó ngay trong phiên. **GĐ-5 cố ý chưa làm**, cần phiên riêng. Không model nào bị đổi.
