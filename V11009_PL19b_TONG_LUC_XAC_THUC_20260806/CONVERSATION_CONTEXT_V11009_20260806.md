# CONVERSATION CONTEXT — V11009 / PL19b · 2026-08-06

## Owner nói gì (NGUYÊN VĂN — brief PL19b, trích phần khung)

> ╔══════════════════════════════════════════════════════════════════════════╗
> ║  GÓI PL19b — TỔNG LỰC LÀM RÕ & XÁC THỰC (READ-ONLY TUYỆT ĐỐI)           ║
> ║  Phạm vi đã rà: GitHub commits V10977→V11008 (03/08→06/08) · trang V6   ║
> ║  "Soi lõi hệ dự đoán" (06/08 22:1x) · V10766/V10776/V10801/V10895/      ║
> ║  V10917/V10990/V10991 · báo cáo dừng PL17 · Current Control             ║
> ╚══════════════════════════════════════════════════════════════════════════╝

> NGUYÊN TẮC TOÀN GÓI:
> - READ-ONLY tuyệt đối: không mutation, không deploy, không đổi số. Hash 4 bảng
>   official pre=post. Mọi kết luận kèm evidence (bảng/dòng code/mốc đo/commit).
> - Mỗi câu trả lời theo khuôn: KẾT LUẬN (1 câu) → EVIDENCE → HÀM Ý (ảnh hưởng
>   quyết định hiện hành) → VIỆC TIẾP THEO (nếu có).
> - Thiếu dữ liệu → ghi rõ thiếu gì, cần bao nhiêu ngày/mẫu nữa. CẤM suy diễn.
> - Sửa con số/tài liệu đã công bố → kèm TRƯỚC/SAU/PHIÊN BẢN/KIỂM theo §60.

Mười lăm câu Q1–Q15 chia sáu phần: SAMDAY · THƯỚC ĐO · PROMPT · VẬN HÀNH · HẠN GẤP ·
KIẾN TRÚC MINED RULES.

Thiết kế đích owner đã chốt (Q15), nguyên văn:

> "Đối với ML: mined rules là cơ chế CƠ HỌC/SỐ HỌC để model ML có thêm tầng chọn lọc. Đối với
> prompt LLM: phải nhét NGỮ CẢNH THÔ thật tốt để agent tự chủ động khai thác, soi xét, tính toán
> toàn bộ và output tự nhiên — KHÔNG bị gò bởi rules đã tổng hợp số sẵn."

Sau khi trả lời xong, owner hỏi:

> "đẩy báo cáo lên github chưa em?"

→ Chưa. Báo cáo này là câu trả lời.

## Agent làm gì

1. **Bấm hash 4 bảng khoá TRƯỚC** để có bằng chứng READ-ONLY.
2. Q1 — không đọc báo cáo cũ, lần thẳng cờ `include_same_day` trong code. Phát hiện **có hai cờ
   khác nhau** và báo cáo V11001 nhầm chúng.
3. Khi so 04:00 với 17:30 ra "0 cặp" — **không kết luận "không khác"** mà đi tìm nguyên nhân,
   ra `INSERT OR REPLACE` (4.808/4.808 khoá chỉ 1 dòng).
4. Trước khi kết luận MB thiếu MN(D), **kiểm kênh thứ hai** `fresh_cross_tails` — cũng không bù.
5. Q6 — nhìn kỹ cột `date` thay vì chỉ đếm dòng, phát hiện `DO_TIEN` chỉ có **1 ngày**.
6. Q8/Q9 — dựng phép đo riêng, tính nền theo từng ngày, hiệu chỉnh Bonferroni.
7. Q15 — đếm tham chiếu `mined_rule` theo từng tầng, ra kết quả 0 / 31 / 8.
8. **Bấm hash 4 bảng khoá SAU** — y hệt. Kiểm `git status` xác nhận 3 tệp `M` có mtime
   17/07 và 02/08, không phải phiên này.

## Vấp ở đâu

### Vấp 1 — lỗi §60.2 câu 1: soi thiếu một tầng gọi

Báo cáo V11001 đọc `include_same_day` (mặc định `False` ở `meta_data_collector.py:206`) rồi kết
luận cho **cả hệ**, mà không lần theo cờ bao ngoài `include_same_day_cross`. Đúng lỗi §60.2
câu 1 — *"ai còn trỏ tới thứ này"* — soi thiếu một tầng.

Hệ quả: báo cáo công khai V11002 mang câu sai suốt hai ngày, và owner phải đối chiếu với V10895
mới phát hiện mâu thuẫn.

### Vấp 2 — trình "n=15" gây hiểu nhầm

V11003 ghi *"đo tiến 15 dòng"* mà không nói **15 dòng đó nằm trên 1 ngày duy nhất**. Người đọc
tự hiểu là 15 mẫu độc lập, đủ để nói "luật không có tác dụng khi đo tiến". Thực tế **không bác
bỏ được gì**.

Hệ quả nặng: FU-286 lên lịch 13/08 chuyển xếp hạng sang đo tiến — **bất khả thi**, thiếu ~139
ngày mẫu.

### Vấp 3 — brief mang tiền đề đã cũ

Q12 nêu FU-274 còn `OWNER_LOCK` với n≥4. Kiểm thì đã `CLOSED_PASS` và cổng n≥12+Bonferroni đã
nối. Agent nêu rõ thay vì trả lời theo tiền đề sai.

## Điều agent NÓI THẲNG với owner

**Ba báo cáo của chính agent phải đính chính.** Hai trong ba đã lên GitHub công khai, nên đính
chính cũng phải công khai — đó là lý do có báo cáo này.

**Phát hiện mới đáng lo nhất — §5g đang thưởng cho tín hiệu ngược.** Ô "3 nguồn" cho z=**−2,51**
(vượt Bonferroni 3 phép), tức là **tệ hơn nền có ý nghĩa thống kê**. Mà V11001 vừa **hạ ngưỡng
từ ≥4 xuống ≥3**, tức siết mạnh hơn vào đúng ô đó. Căn cứ cho việc hạ ngưỡng: `convergence_score`
0 chỗ, `conv_count` 0 chỗ trong code — **đổi bằng suy luận, không bằng đo**.

**Kiến trúc mined_rules ngược 100% so với ý owner.** `mined_rule` xuất hiện **0 lần** trong bốn
tệp ML, **31 lần** trong `gpt_analyzer.py`. Owner muốn rules nuôi ML và để LLM tự do; thực tế
rules **ép** LLM và **không chạm** ML.

**Ba chỗ thiếu dữ liệu, không suy diễn:** Q3 thiếu 7 ngày forward và bảng đứt 2 ngày · Q6 thiếu
~139 ngày · Q8 thiếu phép so khoá cùng tập model. Cả ba đều ghi rõ cần bao nhiêu.
