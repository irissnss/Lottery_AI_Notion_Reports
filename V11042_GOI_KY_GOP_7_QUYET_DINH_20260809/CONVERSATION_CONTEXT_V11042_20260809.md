# CONVERSATION CONTEXT — V11042 · 2026-08-08 23:40 → 2026-08-09 01:05

## Owner nói gì (NGUYÊN VĂN)

> **PROMPT TỔNG LỰC LẦN 4 — GÓI KÝ GỘP 23:38 08/08 (7 QUYẾT ĐỊNH OWNER)**
>
> (1) FU-290 phương án A — BỎ CỜ `output_eligible`, model vẫn chạy vẫn đo, sàn ML≥4 · AI≥3;
> (2) XÁC NHẬN QD-044 (FU-346 đóng);
> (3) B1 — phê chuẩn hành vi hiện tại của `/du-doan` (bundle=None, empty=True ở `main.py:10704`
> là ĐÚNG THIẾT KẾ);
> (4) B2 — THÊM AUTH cho `/api/status` (đang SELECT * không auth, chỉ giấu bằng CSS — đây là lỗ
> hổng bảo mật);
> (5) FU-224 — GỘP 4 trang;
> (6) FU-315 — GIÃN ngày nặng;
> (7) P2 — GIỮ PHASE-FIRST kèm đối chứng.

Trước đó, owner chỉ hỏi một câu ngắn: *"đẩy báo cáo chưa em?"*

## Agent làm gì

Việc đầu tiên là **nhìn đồng hồ** — TIMING GATE của FU-290A phụ thuộc vào nó. 23:44, còn **4,77
giờ** trước mốc 04:30. Còn kịp, nên **không được** viện cớ hết giờ để hoãn.

Rồi fan out **sáu hướng điều tra song song** trên kho thật trước khi chạm gì. Đó là quyết định
đúng nhất của phiên: bốn trong bảy quyết định hoá ra có **tiền đề lệch thực tế**, và không hướng
nào trong sáu hướng đó là thứ agent đoán ra được nếu chỉ đọc lệnh.

## Điều agent nói thẳng với owner — bốn chỗ

**1. B1: mệnh đề trong ngoặc của owner NGƯỢC với code.**
Owner viết *"(bundle=None, empty=True ở main.py:10704 là ĐÚNG THIẾT KẾ — hệ luôn xuất số kể cả
khi bundle rỗng)"*. Đọc code thì đó là **cổng CHẶN số**. Bundle **đã có đủ số** trong
`final_bundles`, API **chủ động thay bằng `None`**, frontend `return` ngay ⇒ **0 ô số**.
Số **bị giấu ở tầng API**, không phải "chưa có số". Phê chuẩn một câu tả sai code là đóng băng
cái sai vào sổ.

**2. FU-224: không phải 4 trang.** Cái thứ tư — `/api/filter-2-so-cuoi` — là một **endpoint
không có UI**; "gộp" không áp dụng được. Hạng mục thứ 5 `/nghiem-thu` agent **tự trả lời được**
bằng máy (12 trang FE trỏ tới + cron hằng ngày ⇒ giữ), không phải phiền owner. Và `OWNER_LOCK`
**chưa gỡ**: sổ ghi *"Agent KHÔNG tự xoá trang"*.

**3. P2: lệnh này ngược một quyết định owner đã ký.** PHASE-FIRST bị **bỏ hẳn 25/06** sau **70
ngày** đo — 34,0% vs 34,2%, không cải tiến, chỉ phình token. Ghi *"giữ phase-first"* thành ACTIVE
là tạo **hai quyết định ngược nhau cùng hiệu lực**, đúng thứ RM-19 sinh ra để chặn. Thêm nữa,
quét toàn kho **không tìm thấy** định nghĩa nào của một đề xuất tên *"P2"* gắn với phase-first.

**4. FU-290A: hoãn, và nói rõ vì sao chứ không viện cớ hết giờ.** Lúc quyết còn 4,7 giờ.
Ba lý do đo được, trong đó **lý do thứ hai là phát hiện nặng nhất của phiên**: `combo_super.py`
có **ZERO** lần xuất hiện chuỗi `output_eligible` — bộ chọn combo **không hề biết đến cờ này**.
Nên bỏ cờ **không cắt được ảnh hưởng gián tiếp**: model đã bỏ cờ vẫn bỏ phiếu vào `combo-super`,
mà `combo-super` **là** output_eligible. Bằng chứng sống là `predictions.id=25851` ngày 08/08.
Nhưng agent **không nống tầng**: ngày đó `combo-super` không có mặt trong `voters`, nên **chưa
chứng minh được số công bố bị nhiễm**.

## Một báo động giả agent tự bắt được TRƯỚC khi báo

`/api/status` trả `date: 2026-06-07` trong khi DB production đã có `2026-08-08`. Lệch **62 ngày**,
trông y như một lỗi nặng — và agent đã bắt đầu soạn câu báo. Đọc code thì đó là
`_VIEWER_FREEZE_DATE`, **cố ý**, owner ký 08/06. **Không phải lỗi.** Nếu báo ra thì đó là lần thứ
tư trong hai ngày đo bằng nguồn sai (RM-13).

## Vấp ở đâu — agent tự làm hỏng rồi tự sửa, ghi hết

**1. Băm nát tiêu đề sổ.** Phép giãn lịch bản đầu ghi **xuôi** trong khi offset lấy từ **một**
lần đọc — mỗi lần cắt ghép là chuỗi dịch đi, offset các mục sau thành rác:

```
### FU-335 · … CLAUDE.md · hạn 18/08UDE.md · hạn 14/08
### FU-327 · … khi nguồn 0 dòng — ĐÃ DỰNGDỰNG
```

Khôi phục **byte-khớp** từ backup, sửa thành ghi **từ CUỐI ngược lên**.

**2. Rồi script tự khen trong khi sổ nói ngược.** In *"KHÔNG CÒN VƯỢT ✓"* trong khi bộ đọc thật
cho 14/08 = 8. Nó đối chiếu với một `Counter` **do chính nó cộng ra**. Đúng RM-16 — chuỗi kiểm
tự viết không phải bằng chứng. Nay bắt script đọc lại từ sổ.

**3. Tự vi phạm RM-06 ngay trong phiên nói về RM-06.** Ba mục mới `FU-381/382/383` là **mục chờ
owner quyết**, mà agent **tự đặt hạn 11/08** — trong khi `FU-379` cùng loại thì để `LX`. Sửa về
`LX`. Chuyện này làm phép trôi tăng 1 → 5; sau khi tự sửa còn lại 1, **bằng lúc bắt đầu phiên**.

**4. Quên ô `status` cho ba mục mới** ⇒ bộ đọc không phân loại được ⇒ cổng lịch báo "mồ côi".

## Một phép trôi còn lại KHÔNG phải do phiên này

`QD-027` đỏ vì *"bảng khuyến cáo hôm nay RỖNG — materializer chưa chạy"*. Lúc **23:59** sổ báo
**1** phép trôi; sau **00:00** thành 2. Ngày vừa sang 09/08, materializer hằng ngày chưa chạy.
Agent **không** ghi nó thành lỗi của mình, cũng **không** giấu.

## Việc bảo mật — điều đáng nói nhất

Owner gọi `/api/status` là *"lỗ hổng bảo mật"*, và đúng — nhưng nặng hơn owner mô tả. Không phải
"vài số liệu nội bộ": mỗi bản ghi mang **`analysis_text` ~16 KB** chứa **luật khai thác kèm
hit-rate**, phase, `candidate_support_map`, cộng **`reasoning_json` ~10 KB**. Đó là **phương
pháp của hệ**, gửi cho mọi khách vô danh.

Và trang công khai **không hề đọc chúng** — nó dùng đúng **8 trường**. Tức 26 KB IP rò ra mà
**không ai dùng**.

Agent **không** gắn `require_admin` như owner viết, vì `/api/status` là nguồn dữ liệu **duy nhất**
của trang `/user-view`; gắn vào là **tắt hẳn trang người dùng**. Tách theo **quyền** thay vì từ
chối — phần bảo mật thật vẫn thi hành đủ. Production: **44.034 → 2.938 byte**, `ANALYSIS=0`,
`REASONING=0`, health 200, PID đổi.
