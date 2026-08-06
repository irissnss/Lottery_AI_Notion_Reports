# CONVERSATION CONTEXT — V10993–V10996 — 2026-08-06

> Nguyên văn lời owner · agent làm gì · vấp ở đâu. Không diễn giải lại.

---

## 1. Owner nói gì (nguyên văn, theo thứ tự)

**(1) Sau khi agent trình phát hiện điểm mù của cổng no-lookahead:**

> *"ok duyệt làm đi canh số thật không canh canh số nháp làm gì"*

**(2) Khi agent nói phải chờ khung giờ 18:15 mới đẩy được:**

> *"Đẩy thì có làm sao? Không có sửa số mà lo gì em. Làm đi"*

**(3) Sau khi agent báo phát hiện 90 bundle làm bù:**

> *"ok em làm đi em đồng ý nếu lẫn thì phải làm cho rõ ra để có xác nhận và quyết định chính
> xác || Đồng thời xem thêm dùm anh: Đo tiếp A2/A3. Kiểm tra thêm bảng shadow có ảnh hưởng số
> chính thức không. Bổ sung kiểm tra cho 3 bảng chính thức. Không sửa số, không sửa prompt."*

**(4) Chọn một trong ba hướng xử 90 bundle làm bù:**

> *"ok vậy b nha em. làm đi nhưng nó sẽ đúng và có tính lại vẫn không bị sợ sơ xuất nha em"*

**(5) Sau khi xem bảng trước/sau của 6 chỗ tính thành tích:**

> *"OK LÀM ĐI EM"*

**(6) Về việc chờ khung giờ và về báo cáo:**

> *"Nói chung hôm nay anh sẽ bỏ không tham gia vào dự đoán, anh cần điều chỉnh để hệ thống tốt
> trước đã nên việc 18h15 cũng ko cần thiết, cái anh cần là điều chỉnh, đẩy báo cáo lên github
> để tool ai giám sát lại lần nữa dùm anh, cái nào chư commit, lý do nói rõ luôn"*

---

## 2. Bối cảnh trước đó — owner phàn nàn agent trình bày khó hiểu

Trước phiên này owner đã nói:

> *"Có cách nào dân giả hơn không em? em trình bày anh khó hiểu quá em? anh chưa hiểu anh chưa
> quyết định được gì luôn đó em. Làm sao để anh dễ hiểu theo cách hiểu của anh nhất ah em"*

Từ đó agent đổi cách trình bày: bỏ thuật ngữ, dùng ví von *"ghi số trước giờ xổ"* thay cho
`HINDSIGHT`, *"sổ thật / sổ nháp"* thay cho tên bảng. Owner sau đó quyết được ngay.

**Ghi lại vì đây là bài học vận hành, không phải chuyện kỹ thuật:** báo cáo đúng mà người đọc
không hiểu thì owner không quyết được, và việc đứng lại.

---

## 3. Agent làm gì, theo thứ tự

1. Chạy `_v10920_session_start.py` (bắt buộc §0). Cảnh báo **8 mục đến hạn hôm nay** — đã nêu
   ngay đầu câu trả lời cho owner.
2. Nhận brief PL17, vào phần A1 (chuỗi gọi runtime) → thấy sẵn `_v10801_ml_mark_ab_shadow.py`
   (A/B samday) và `_v10660_no_lookahead_harness.py` (leakage). **Playbook-first: kiểm cái có
   trước, không dựng lại.**
3. Đọc `no_lookahead_audit` → **750 dòng HINDSIGHT** → **chạm điều kiện dừng của brief** →
   dừng, báo owner.
4. Owner duyệt mở rộng cổng → V10993.
5. Quét 400 ngày → phát hiện **90 bundle làm bù** → **đính chính hai kết luận đã báo owner**.
6. Owner yêu cầu làm rõ + đo A2/A3 + kiểm shadow → V10994.
7. Owner chọn hướng (b) → V10995.
8. Trình bảng trước/sau 6 chỗ → owner duyệt → V10996.
9. Owner miễn trừ khung giờ → agent thêm cờ có ghi lý do → **bị lớp kiểm duyệt chặn** → dừng,
   không lách, báo owner.

---

## 4. Vấp ở đâu — kể hết, kể cả lỗi của chính agent

### 4.1 Đếm thiếu, rồi báo sai cho owner

Sáng 06/08 agent báo *"final_bundles: MN 0 · MT 2 · MB 0 ghi sau giờ xổ"* và kết luận
*"sổ thật gần như sạch"*.

**Sai.** Phép đó chỉ soi bản ghi muộn **trong cùng ngày** (`time(created_at) >= giờ_xổ`), bỏ
sót loại ghi **sang ngày khác** (`date(created_at) > date`). Đếm đủ là **92 bản**.

Cổng vừa mở rộng bắt được ngay — tức **cổng bắt lỗi của chính người mở nó**.

### 4.2 Kết luận sai về tháng 3 — lỗi nặng hơn

Tuần trước agent trình owner bảng xu hướng theo tháng, lấy tháng 3 làm mốc rồi kết luận
*"tháng 3 gặp may, từ đó hồi quy về nền"*.

**Sai.** Tháng 3 có **29/31 ngày là số làm bù**, không phải dự đoán thật. Tháng 3 không gặp
may — tháng 3 gần như không có dự đoán thật nào.

Số đúng sau khi tách: MB dự đoán thật **18,0%** so với nền 23,7% — **thấp hơn nền**, không
phải 38,7% như đã báo.

### 4.3 Lỗi lặp lại HAI LẦN — cùng một cái

Hai lần liên tiếp đặt `chay_lenh` trong sổ quyết định có kèm tham số:
`"..._v10660_no_lookahead_harness.py --days 14"` rồi `"..._v10995_loc_lam_bu.py --kiem"`.
Sổ truyền cả chuỗi làm đường dẫn → Python không mở được tệp → exit 2.

**Bài học:** `chay_lenh` chỉ được là đường dẫn tệp, không kèm tham số. Muốn đổi hành vi thì đổi
mặc định của chính script.

### 4.4 Sổ quyết định suýt chạy lệnh deploy thật

Ban đầu để `kiem_code` của QD-034 gọi thẳng `_v10996_deploy.py`. Sổ quyết định chạy **mỗi
phiên** — tức mỗi phiên sẽ **thử đẩy thật lên VPS**. Đã tách ra `_v10996_kiem.py` chỉ đọc.

Đây là loại lỗi nguy hiểm: cổng kiểm mà lại có tác dụng phụ.

### 4.5 Thông báo lỗi nói sai nguyên nhân

Cổng in *"1 bản ghi sau giờ xổ / số bị sửa"* trong khi thật ra là **bộ lọc làm bù bị lệch** (do
DB local chưa dựng view). Người đọc sẽ đi tìm nhầm chỗ. Đã sửa thành liệt kê đúng từng lý do.

### 4.6 Chệch khỏi chữ owner nói — có nêu trước, không làm lén

Owner nói *"đánh cờ `is_backfill` vào bảng"*. Agent **không** ghi cột vào bảng, vì:
`final_bundles` là bảng khoá (ghi cột = đổi mã băm = phá cổng đang canh số), và cờ ghi cứng có
thể lệch lặng lẽ.

Agent **nêu rõ chỗ chệch và lý do ngay trong câu trả lời**, trước khi làm. Owner không phản đối.

### 4.7 Bị lớp kiểm duyệt chặn — không lách

Owner miễn trừ khung giờ deploy. Agent thêm cờ `--owner-mien-tru` **có ghi lý do vào artifact**,
giữ nguyên cổng chặn mặc định (đã thử: không có cờ thì vẫn chặn đúng).

Nhưng lệnh chạy bị **lớp kiểm duyệt của Claude Code chặn** — cờ miễn trừ trông giống hành vi đi
vòng cổng an toàn.

**Agent KHÔNG tìm cách lách** (không đổi tên cờ, không tự scp + restart bằng tay để né). Dừng
và trình owner quyết.

---

## 5. Điều đáng nói nhất

Cổng canh no-lookahead tồn tại từ lâu, chạy đều mỗi ngày 14:45, và **suốt thời gian đó chỉ soi
2 bảng shadow**. Ba trên bốn bảng khoá — `predictions`, `final_bundles`, `model_daily_eval` —
**chưa bao giờ được soi**.

Không ai biết là mình không biết. Cổng vẫn xanh mỗi ngày.

Ngày đầu tiên mở rộng nó, nó bắt được ngay: 90 bundle làm bù nằm lẫn trong sổ thật, thổi phồng
thành tích MB tới gần gấp đôi, và **hai kết luận sai mà chính agent đã báo owner**.

---

## 6. Còn treo, cần owner biết

- **V10996 chưa đẩy.** Chờ owner quyết: cấp quyền cho lệnh có cờ miễn trừ, hay chờ sau 18:15
  thì cổng tự mở và không cần cờ nào.
- **`backups/` (156 tệp) và `share_exports.rar` (7,4 MB) chưa nằm trong `.gitignore`** — nên
  đưa vào, nhưng đó là quyết định của owner về cấu trúc kho.
- **51 tệp hiện `M`** chỉ khác ký tự xuống dòng, không phải sửa thật. Không commit để tránh
  nhiễu lịch sử.
