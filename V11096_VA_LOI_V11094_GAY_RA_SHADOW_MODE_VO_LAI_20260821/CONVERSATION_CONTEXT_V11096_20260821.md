# CONVERSATION CONTEXT — V11096 · bù ngày 26/08/2026

> ⚠️ **BẢN BÙ.** Việc làm ngày **21/08/2026**; tệp này viết ngày **26/08/2026**.

## 1 · Vì sao có tệp này

`V11096` **không có** thư mục báo cáo công khai — vi phạm `§57.2` tồn tại
**5 ngày** mà không cổng nào thấy, vì cổng A55 chỉ soi **8 bản gần nhất**
(lỗ hổng ②, vá ở `V11122`/`FU-442`).

## 2 · Nguồn dùng để dựng

| nguồn | quy mô | tính chất |
|---|---|---|
| khối `## V11096` trong `CHANGELOG.md` | 2,273 ký tự / 44 dòng | **đương thời** — viết lúc làm việc |
| commit git | 4 commit, ngày 2026-08-21 | **đương thời** |
| lượt owner trong vết phiên `.jsonl` | có | **đương thời** |

## 3 · Nguyên văn lời owner

> *«PROMPT TỔNG LỰC LẦN 22 — GO 21/08: THỰC THI GÓI 12 MỤC + 1 THIẾT KẾ (sáng 21/08 · QD-041 HẾT HẠN · thực thi theo docs/BAN_DO_THUC_THI_2108.md ĐÃ CHỐT tối 20/08) ═══ BỐI CẢNH ĐÃ CHỐT — KHÔNG MỞ LẠI, KHÔNG HỎI LẠI ═══ • Gói = 12 mục thực thi + 1 việc thiết kế. D3 ĐÃ HOÃN (FU-411, lối C) — CẤM chen vào. • FU-284 ĐÃ ĐÓNG «không đủ sức» — cấm mở lại. • Bốn ô verdict đã điền: bầy đàn CÓ TÁC DỤNG (0,5815 vs nền 0,4739) · DE…»*
> — owner, **21/08/2026 08:52** (giờ VN)

> *«Tới hạn rồi xong chu kỳ theo dõi, chu kỳ xổ số hôm nay rồi. Em tiến hành kiểm tra , rà soát tất cả chuẩn chị cho việc xử lý đi nào»*
> — owner, **21/08/2026 19:00** (giờ VN)

> *«deploy chứ chờ gì nữa em? FU-290A (đề xuất: không cắt vì độ trễ ) ==> ko rõ model nào nhưng chưa cắt là đúng vì độ trễ do nhiều yếu tố bới quá nhiều model quá mà em FU-394 (đề xuất: gỡ hẳn nhánh gan, hành vi không đổi) ==> cắt đi FU-416 (vá một dòng) · FU-393 (ba lối a/b/c). ==> chi tiết cụ thể là gì diễn giải cụ thể toàn là mã ngắn gọn mà bắt duyệt làm sao mà duyệt được duyệt mù ah em.»*
> — owner, **21/08/2026 19:49** (giờ VN)

> *«PROMPT TỔNG LỰC LẦN 23 — TỐI 21/08: VÁ FU-416 + KIỂM KÊ DỌN DẸP + SOẠN TÀI LIỆU DUYỆT GỘP ═══ OWNER KÝ 20:15 21/08 — KHÔNG HỎI LẠI ═══ ① Vá FU-416 NGAY phiên này — một dòng: thêm key=lambda x: (-x[1], x[0]) tại gpt_analyzer.py:5941 (sorted không phá hoà rồi cắt [:10]/[:6] ⇒ số nào model nhìn thấy trước tiên đang do HẠT BĂM quyết). ② Dọn dẹp app theo kiểu: KIỂM KÊ CÓ BẰNG CHỨNG → owner duyệt một lượt → MỚI CẮT. Phiên …»*
> — owner, **21/08/2026 20:19** (giờ VN)

> *«Đã push báo cáo hết chưa? Đề xuất tiếp theo là vấn đề nào còn tồn đọng , vấn đề nào chưa tìm hiểu đào sâu, kế hoạch cắt giảm model ai tới đâu rồi chỉ phí gánh ngày càng nặng mà chả hiệu quả gì.»*
> — owner, **21/08/2026 21:06** (giờ VN)

> *«Chi phí ở đây không phải là model đắt tiền đong đếm bằng tiền. Chị phí chạy quá nhiều model ai lãng phí mà trong khi đó không đo được sức mạnh của model, model nào đáng dùng không đáng dùng, đắt cũng được nhưng phải chất lượng , phù hợp với dự án, phù hợp với ngữ cảnh, prompt phải tối ưu thuần ngữ cảnh nhồi toàn số đã lọc sẵn vào thì model ai đâu hoạt động đúng nghĩa của nó em. Đắt phải chất , ít nhưng hiệu quả đông …»*
> — owner, **21/08/2026 21:21** (giờ VN)


## 4 · Điều KHÔNG khôi phục được — ghi thẳng, không suy

- **giờ chính xác** từng thao tác trong phiên gốc
- **vướng vấp giữa chừng** — không tài liệu nào ghi lúc đó
- **các phương án đã cân nhắc rồi loại**
- **hash 4 bảng khoá trước/sau** và **PID trước/sau** nếu phiên gốc có chạm DB hoặc restart
- **output cổng kiểm** của phiên gốc — cổng in `stdout`, không ghi tệp (khuyết tật `RM-15`, đã vá
  cho `cong_git_commit.py` ở `V11121` bằng sổ điểm danh)

## 5 · Điều bản bù này **không** làm

| không làm | vì sao |
|---|---|
| Chế lại lời owner | `§62` cấm — thà để trống còn hơn bịa |
| Điền số ước cho hash/PID | `RM-11` — số không tái lập được thì không dùng |
| Sửa khối `CHANGELOG` gốc | nó là bản ghi đương thời, **cấm viết lại lịch sử** |
| Gộp với bản khác | mỗi bản một thư mục riêng, đúng `§57.2` |

**TanPhatAI cần làm:** đọc mục 4 trước khi đối chiếu — bản bù **không** thay được báo cáo viết lúc
làm việc, và những chỗ trống là **cố ý trung thực**, không phải thiếu sót.
