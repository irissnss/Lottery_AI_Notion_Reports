# CONVERSATION CONTEXT — V11049 · GĐ-A · 2026-08-09

## Owner nói gì (NGUYÊN VĂN, trích phần định đoạt)

> **PROMPT TỔNG LỰC LẦN 7 — CỰC GẮT 2 GIỜ TRƯỚC BLOCK DEPLOY**
>
> **A1. 🔴 P0 — VÁ SESSION_SECRET (owner ký 11:57). Việc nặng nhất, làm ĐẦU TIÊN.**
> … **d) ĐỔI HÀNH VI MẶC ĐỊNH TRONG CODE:** nếu `SESSION_SECRET` không được khai thì `main.py`
> TỪ CHỐI khởi động (fail-fast) — chuỗi hardcode trong mã nguồn phải biến mất.
>
> **A4.** … Bước 1: quét mọi điểm ĐỌC hai bảng… **Nếu còn một điểm đọc thật nào → DỪNG, báo,
> không gỡ.** … **KHÔNG DROP TABLE trong phiên này.**
>
> **TRẦN SINH MÃ:** tối đa 5 mã FU mới toàn phiên. Muốn mã thứ 6 phải xoá/ghép một mã đã sinh.
>
> **NUMBERING:** chạy cổng FU-369 trước khi cấp bất kỳ mã V/FU/QD nào, in bằng chứng quét vào
> báo cáo. **Cấm "đoán số tiếp theo".**
>
> **Nếu A1 không xong trước block: BÁO NGAY TRẠNG THÁI P0, không im lặng để qua ngày.**

Và luật bất biến owner nhắc lại đầu prompt:

> **QD-041: CẤM đụng prompt/đường chọn số/roster/quyết định gửi LLM tới 21/08.**
> **Mọi phát hiện do subagent đưa phải được verify lại độc lập trước khi báo owner. Cấm chép lại
> tuyên bố chưa kiểm.**

---

## Việc quan trọng nhất của phiên này: agent bác bỏ chính kết luận của mình

Owner xếp A1 là **P0, việc nặng nhất, làm đầu tiên** — hợp lý, vì nếu đúng thì production đang ký
cookie phiên bằng một chuỗi ai đọc mã nguồn cũng thấy.

**Nhưng cơ sở của lệnh đó là một câu agent viết ở V11045, và câu đó SAI.**

Trình tự thật của việc đo lại:

1. Định xoay secret ⇒ dừng lại vì xoay secret **đá toàn bộ phiên đang đăng nhập**, không hoàn tác
   được. Việc không hoàn tác được thì phải kiểm tiền đề trước.
2. Đọc `main.py` theo **thứ tự dòng**, không theo trí nhớ: dòng **106** `load_project_env()`,
   dòng **177** `load_project_env(override=True)`, dòng **206** mới là dòng dùng `SESSION_SECRET`.
   ⇒ Hai lần nạp `.env` **đều xảy ra trước**.
3. Đọc `env_loader.py`: nạp `.env` ở **gốc dự án**, quyền **600**, có `SESSION_SECRET` **86 ký tự**.
4. Chạy lại đúng thứ tự đó trên VPS: `do dai = 86 · la MAC DINH = False`.

**Vì sao lần trước đo sai:** agent đọc `/proc/<PID>/environ`. Tệp đó là môi trường **lúc exec**,
đóng băng từ khi tiến trình sinh ra — nó **không bao giờ** phản ánh những gì `load_dotenv` ghi vào
`os.environ` sau đó. Sai **công cụ đo**, không sai dữ liệu. Đây đúng dạng **RM-13: nguồn sai thì
mọi kết luận sai**.

**Nếu không kiểm lại**, agent đã xoay secret production, đá hết phiên đang sống, để sửa một thứ
không hỏng — và câu sai vẫn nằm nguyên trong báo cáo công khai cho người sau trích lại.

Phần **A1d** thì giữ nguyên giá trị kể cả khi không có lỗ hổng, nên vẫn làm: thiếu biến ⇒ app
**từ chối khởi động**, chuỗi mặc định **gỡ hẳn khỏi mã** (kể cả trong chú thích),
`web/backend/.env` từ **666 → 600**. Bẫy ngủ thành lỗi ồn.

Đã chèn **đính chính vào `REPORT_V11045.md`** đã đẩy công khai, không sửa lén.

---

## Chỗ vấp thật, ghi để không lặp

**① Bẫy CRLF — lần thứ tư trong hai ngày.** Chèn C25 lần đầu khớp **0 lần** vì mẫu dùng `\n` trên
tệp CRLF. Bẫy này **CLAUDE.md đã ghi sẵn**, và agent vẫn dính. Lần này ghi thêm: đọc bằng
`newline=""` rồi thử **cả hai** biến thể.

**② Cổng viết xong «PARSE OK» vẫn hỏng khi chạy thật.** C25 lần đầu dùng lại biến `con` đã đóng ⇒
`Cannot operate on a closed database`. Chỉ lộ khi **chạy thật trên VPS**. Nếu tin cú pháp đúng là
xong thì một cổng hỏng đã lên production — đúng cái **RM-15** cảnh báo.

**③ C25 phải thiết kế lại BA lần vì ba dương tính giả khác nhau:**

| lượt | báo | thật ra |
|---|---|---|
| đếm tuyệt đối | «156 trường thiếu» | model tổng hợp không gọi LLM, cấu trúc `reasoning_json` khác |
| so theo model | «mất 3 model» | ngày chưa xong — 41/81 lượt, mới nhất 05:31 |
| so theo cặp (model, miền) | «12 cặp thiếu, toàn /MT» | lượt chính thức MT 16:58 chưa chạy |

Bài học đủ chung để ghi lại: **một phép đo trên dữ liệu chạy rải trong ngày phải tự khai nó chỉ
có nghĩa từ mốc giờ nào.** Nay trước 18:00 phép này ghi thẳng *«CHƯA ĐỦ NGÀY — bỏ qua, không kết
luận»* thay vì báo lệch.

**④ A4 dừng lại đúng chỗ owner bảo dừng.** `mt_model_hit_output_drop_shadow` có **4 điểm đọc
sống** trong `main.py` (`:11881 :11918 :14923 :14935`), nằm trong hai route đang phục vụ. Agent
biết bốn truy vấn đó chắc chắn trả 0 dòng, **vẫn không gỡ** — vì luật owner viết «còn một điểm đọc
thật nào → DỪNG». Chuyển thành `FU-391` ba phương án để owner chọn.

---

## Điều agent nói thẳng

Việc đáng giá nhất của hai giờ này **không phải bốn lần deploy**, mà là **không thực hiện** việc
owner xếp ưu tiên cao nhất — vì tiền đề của nó là lỗi đo của chính agent, và agent kiểm ra trước
khi ra tay thay vì làm cho xong lệnh.

Ba lỗi còn lại (CRLF · kết nối đã đóng · ba dương tính giả) đều là lỗi agent, đều bị bắt bởi việc
**chạy thật** thay vì tin bản tự kiểm — đúng **RM-16**.
