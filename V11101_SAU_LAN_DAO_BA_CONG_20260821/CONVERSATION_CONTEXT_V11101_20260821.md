# CONVERSATION CONTEXT — V11101 · 21/08/2026 (tối → đêm)

## Owner nói gì (NGUYÊN VĂN)

> *«Đã push báo cáo hết chưa? Đề xuất tiếp theo là vấn đề nào còn tồn đọng, vấn đề nào chưa tìm
> hiểu đào sâu, kế hoạch cắt giảm model ai tới đâu rồi chỉ phí gánh ngày càng nặng mà chả hiệu
> quả gì.»*

> *«Chi phí ở đây không phải là model đắt tiền đong đếm bằng tiền. Chị phí chạy quá nhiều model ai
> lãng phí mà trong khi đó không đo được sức mạnh của model, model nào đáng dùng không đáng dùng,
> đắt cũng được nhưng phải chất lượng, phù hợp với dự án, phù hợp với ngữ cảnh, prompt phải tối ưu
> thuần ngữ cảnh nhồi toàn số đã lọc sẵn vào thì model ai đâu hoạt động đúng nghĩa của nó em. Đắt
> phải chất, ít nhưng hiệu quả đông loãng, nhiều thì không nên. Showdow là thử nghiệm để so sánh
> và tìm ra model phù hợp để thay thế các model hiện tại giá trị nó chỗ đó nó chưa tham gia output
> là đúng mà em, em phải làm việc này so sánh tìm ra ứng viên sáng giá chứ em..»*

> *«Em làm việc có vẻ cẩu thả và dư thừa, em có biết là anh đã yêu cầu em lên kế hoạch chuyển đổi
> các thông số đang tiêm vào prompt thành ngữ cảnh kèm các điều kiện phù hợp tương thích miền thứ
> biết bao nhiêu lần không hả? ML là ML là một model cơ chết số học hoàn toàn, LLM là LLM nó hoạt
> động với các ngủ cảnh điều kiện để truy vết, sàn lọc, chọn lọc, khoanh vùng để xác định được số
> tốt nhất đưa ra output tốt nhất… EM nghỉ anh rảnh lắm đưa vào 1 đống model AI không tham gia
> total output để làm cảnh ah để đốt tiền ah em? em quá kém cỏi đó.»*

---

## Owner đúng ở đâu, và em sai ở đâu

**Em sai ba chỗ, không phải một.**

**Sai 1 — gọi shadow là hàng thừa.** Em từng viết shadow *«không tham gia output»* theo giọng chê.
Owner sửa: *«nó chưa tham gia output là đúng mà em»*. Và cấu trúc hệ thống chứng minh owner đúng:
bảng `shadow_model_promotion_scorecard_daily` là **thứ duy nhất trong toàn kho** đã có sẵn hai cột
`b`/`c` — tức **đúng cái thước** cần để trả lời *«có nên đổi người không»*. Shadow là phòng thí
nghiệm; cái hỏng là **chưa ai mang thước từ phòng thí nghiệm ra đo người đang thi đấu**.

**Sai 2 — đọc «chi phí» thành tiền.** Owner nói rõ không phải tiền. Chi phí là **loãng**: chạy
6 tháng, 27 model, mà **8/15 model đang góp số công bố có 0 dòng chấm điểm**, và model đương nhiệm
`claude-sonnet-4-6` có **n = 0**. Tức không ai trả lời được câu *«nó mạnh hay yếu»*.

**Sai 3 — em trình lại việc owner đã yêu cầu từ 16/08 như thể là ý mới.** Cổng đối chiếu nhãn QD
dựng tối nay bắt được: quyết định **`QD-067`** ngày 16/08 có trong báo cáo, có trong
`AUTOMATION_HISTORY`, **nhưng không có trong sổ quyết định**. Nội dung của nó:

> *«chuyển hoá thuần ngữ cảnh cho model để model AI tự phân tích theo năng lực thay vì nhồi nhét
> vào»*

Đúng điều owner mắng tối nay. **Nó rơi khỏi sổ nên không ai theo.** Đó là câu trả lời thật cho
*«biết bao nhiêu lần không hả?»* — và nó không phải lời bào chữa, nó là **một lỗi sổ sách có mã**.

---

## Ba lần cổng bắt được chính agent trong phiên này

**① Bài thử chặn bắt cổng vừa vá là cổng MÙ.** `_v11044` bản đầu lấy tập «đã khai» từ hàm quét
**sáu nơi** (CHANGELOG · sổ theo dõi · SSOT…). Gỡ `QD-069` khỏi **sổ** thì nó **vẫn thấy** ở
CHANGELOG ⇒ không bao giờ đỏ được. Bước [2] của bài thử TRƯỢT ⇒ mới lộ ra.

> Nếu chỉ chạy xuôi rồi thấy màu xanh thì hôm nay đã giao owner một cái cổng **không chặn được gì**.
> Đây đúng là lý do `RM-15` tồn tại: **cổng không qua thử coi như không tồn tại**.

**② Cổng ghi tệp an toàn chặn chính bài thử chặn.** Bài thử của `_v11044` phải sửa rồi khôi phục
**sổ quyết định thật**, và em viết nó bằng `open(...,'w').write(...)` — **đúng khuôn** đã cắt cụt
hai tệp 900 KB ngày 31/07. Tiến trình chết giữa bài thử thì sổ nằm lại **cụt** — mà bài thử vốn
sinh ra để **bảo vệ** sổ. Đã đổi sang `tmp → flush → fsync → replace → đọc lại so`.

**③ Cổng che stderr tự làm mình mù HAI LẦN trong lúc dựng.**
Lần đầu: coi mọi khối ba nháy là chú thích, trong khi kho này dùng đầy khuôn `SH = r"""…shell…"""`
— **`CHÚ_THÍCH` nhảy 5 → 194**, tức nuốt mất **189 chỗ**. Lần hai: dùng một biến nên bỏ sót
**docstring lồng trong tải trọng** (`_v10978` bọc cả thân chương trình trong `REMOTE_SRC = r'''…'''`).
Cả hai lần đều bị bắt vì **soi lại con số bất thường**, không phải vì cổng tự báo.

---

## Một vấp về git đáng ghi

Commit đầu của GĐ-5b **nuốt mất 5 tệp**. Lần bị cổng `§63` chặn ngay trước đó đã **xoá sạch phần
đã `git add`**, nên commit landed với **đúng 4 tệp nâng version** trong khi thông điệp mô tả cả
phần vá cổng — **thông điệp mô tả thứ không có trong commit**. Đã `--amend` (chưa push).

**Bài học: sau mỗi lần cổng chặn, phải `git add` lại. Đừng cho rằng index còn nguyên.**

---

## Con số em phải rút lại — của chính hôm nay

Chiều nay em công bố *«MN 15% / MT 13% / MB 32% ký tự prompt là thống kê hiệu suất model»*.
**Đo trên gói THÔ.** Trên gói **model thật sự đọc** — sau khi `_V10768_DEHERD_PROMPT_ENABLED`
cắt ba khối đầu — chỉ còn **5,8% / 4,6% / 26,5%**.

Nếu để nguyên con số cũ thì việc dọn prompt sẽ **nhắm sai cả ba miền**. Sự thật là vấn đề
**gần như trọn ở MB**, và khối tệ nhất là `MB MODEL RANKING`: **11/35 model trong đó đã rời danh
bạ**, mà prompt vẫn dạy *«MB Thứ Bảy TRUST: `deepseek-v4-flash`»* — model **ngừng dự đoán MB từ
04/07, 48 ngày trước**.

---

## Điều owner nói mà em chưa làm xong

Owner: *«Anh tin chắc trong các audit báo cáo trong root có rất nhiều điều cần em phải kiểm tra,
rà soát lại rồi đó»* — **đúng**, và đào ra được:

- **11 lần khen model trong lịch sử, 0 lần thực tế xác nhận.**
- Con số `z = 2,81` của `V10947` **không tái lập được** (dùng nền 16,49% cho MT trong khi nền thật
  35,12%) và **chưa bao giờ được rút lại ở chỗ đã công bố**.
- Luật GĐB-đảo đã ký sẵn ngưỡng *«≤28% ⇒ đóng, đọc 16/08»*; đo lại **16,7% vs nền 23,3%** ⇒
  **phải đóng từ 16/08, quá hạn 5 ngày** — **lần rữa thứ BẢY**, và không ai đọc cái ngưỡng đã ký.

**Chưa làm xong:** lớp `create_analysis_prompt` (~**18.200 ký tự**) chưa dump được nên **chưa có
số ký tự từng khối**. Ghi thẳng **«không kiểm được»**, không đoán.
