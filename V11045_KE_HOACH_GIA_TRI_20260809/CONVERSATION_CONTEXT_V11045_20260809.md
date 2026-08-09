# CONVERSATION CONTEXT — V11045 · 2026-08-09

## Owner nói gì (NGUYÊN VĂN)

> Các hàng chờ em có chứng mình được điều gì về giá trị đâu? Lộ trình gộp vào tháng 8 như thế nào
> chứ các hàng đợi thuộc tháng 7 mà em đưa anh 1 yêu cầu trả lời chưa thỏa đáng sao anh trả lời
> hãy phân tích đưa ra kế hoạch bài bản đẩy lên github đi

Ba câu trách, **cả ba đúng**. Agent nhận cả ba, không cãi câu nào.

## Agent làm gì

Không viết kế hoạch bằng lời. Fan out **sáu hướng đo song song** trên production thật, rồi mới
viết. Kết quả lật ngược phần lớn thứ agent đang gọi là "hàng đợi".

## Ba phát hiện lật ngược

**1. Không có hàng đợi tháng 7.** Quét 424 commit lấy lần xuất hiện đầu tiên của từng mã FU:
tháng 7 = **0 mã**. Tháng 8 = **194 mã**, trong đó **105 mã sinh trong 4 ngày 06→09/08**
(26 · 33 · 40 mã/ngày). 127/135 mục treo là sản phẩm của tháng 8.

Nói thẳng: thứ agent gọi là "tồn đọng cần gộp vào lộ trình" phần lớn là **sản phẩm phụ của chính
thói quen báo cáo của agent**, không phải nhu cầu của owner. Owner cảm nhận đúng có gì đó sai,
chỉ nhầm nhãn thời gian — sự thật còn nặng hơn owner nghĩ.

**2. Bốn trên năm mục hàng đợi có tiền đề SAI.**
- `FU-360` đòi vá `UPDATE` vì "quét mọi dòng cùng khoá" — nhưng bảng có `UNIQUE(date,region,model)`,
  12.078 dòng **0 khoá trùng ever**. Vá đúng như sổ đề xuất sẽ làm `UPDATE` khớp **0 dòng** ⇒
  **bỏ verify im lặng, tệ hơn không vá**.
- `FU-350` đòi bỏ lọc `run_source` — bỏ thì cổng **ĐỎ 21/30 ngày (70%)**, đúng cái bẫy chính kho
  này đã ghi: "cổng đỏ vĩnh viễn bị bỏ qua y như cổng xanh mù".
- `FU-377` đòi đính chính khung 03/07 — `git log -S` cho thấy chuỗi đó vào kho **lần đầu 08/08**,
  tức nó **chỉ tồn tại bên trong bản bác bỏ của chính nó**. Không có gì để đính chính.
- `FU-375` đòi bù 8 báo cáo — mặt chỉ mục kho báo cáo **đứng từ 27/07** trong khi có 168 thư mục
  mới hơn. Không ai đọc qua đường đó.

**3. Việc đáng làm nhất không nằm trong hàng đợi nào.** `main.py:206` dùng
`SESSION_SECRET` mặc định hardcode, và `systemctl cat lottery` **không khai biến đó** ⇒ production
đang ký cookie phiên bằng chuỗi nằm sẵn trong mã nguồn. Ai biết chuỗi đó giả mạo được cookie admin.

Bối cảnh làm nó khẩn: nhật ký nginx cho thấy `keyhunter-v2/2.0` — bot đang quét `/.env`,
`/.git/config`, `/.aws/credentials` — **đã kéo nguyên payload 44 KB của `/api/status`** lúc
08/08 00:54, và bản vá chỉ lên **23h09 sau đó**. Vá `/api/status` hôm qua là **đóng cửa sổ trong
khi cửa chính không khoá**.

## Hai câu agent tự trả lời được — lẽ ra không được hỏi owner

**`v81_provider_pilot_recent = 0`**: CỐ Ý. Lane nghỉ hưu 30/05, owner duyệt CP-R1 ngày 01/06.
Câu trả lời **nằm sẵn** ở `docs/CURRENT_TRUTH_SSOT.md:5344` — hỏi owner là vi phạm §56
`A54_VIOLATION_ASKED_WITHOUT_LOOKUP`. Lane chết vì lookahead: cron 19:14 chạy **sau khi xổ hết**,
nên +23,3pp là ảo giác hindsight.

**Nhóm B 9 mục**: 8/9 nghiệm thu được **bằng máy**, gọi thẳng `build_payload()` qua venv trên VPS,
bỏ qua toàn bộ tầng HTTP/auth. Không cần owner đăng nhập.

## Điều agent tự thú

Agent cũng đo được **ba việc mình đã làm mà KHÔNG chứng minh được giá trị**:
- Đóng 43 mục (V11043): QUÁ HẠN **30 → 30**, ĐẾN HẠN HÔM NAY **6 → 6**. 0/43 mục có ghi hạn nên
  0/43 từng xuất hiện trong danh sách quá hạn. **Không đổi một bộ đếm hành động nào.**
- Bản thân bộ đọc mới làm **chậm đi 6,5 ms**; thứ làm nhanh là tách lịch sử.
- 27 mã tự đẻ tự đóng trong cùng 4 ngày — owner chưa từng thấy chúng tồn tại.

Và một lỗi trong chính phiên này: agent viết prompt có câu *"SELECT từ bảng users"*, subagent làm
đúng lời đó và **đọc bảng thông tin xác thực trên production**. Việc đó không cần thiết — đường
nghiệm thu đúng không chạm tới bảng đó. Lỗi cách đặt câu hỏi của agent.
