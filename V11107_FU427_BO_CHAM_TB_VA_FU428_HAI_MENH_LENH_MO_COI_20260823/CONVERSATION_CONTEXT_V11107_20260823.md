# CONVERSATION CONTEXT — V11107 · bù ngày 26/08/2026

> ⚠️ **BẢN BÙ.** Việc làm ngày **23/08/2026**; tệp này viết ngày **26/08/2026**.

## 1 · Vì sao có tệp này

`V11107` **không có** thư mục báo cáo công khai — vi phạm `§57.2` tồn tại
**3 ngày** mà không cổng nào thấy, vì cổng A55 chỉ soi **8 bản gần nhất**
(lỗ hổng ②, vá ở `V11122`/`FU-442`).

## 2 · Nguồn dùng để dựng

| nguồn | quy mô | tính chất |
|---|---|---|
| khối `## V11107` trong `CHANGELOG.md` | 12,091 ký tự / 214 dòng | **đương thời** — viết lúc làm việc |
| commit git | 1 commit, ngày 2026-08-23 | **đương thời** |
| lượt owner trong vết phiên `.jsonl` | có | **đương thời** |

## 3 · Nguyên văn lời owner

> *«PROMPT TỔNG LỰC LẦN 28 — 23/08: TRUY 9 ms + TRUY KHÂU RÚT SỐ + VÁ FU-419 LỐI (a) ═══ OWNER ĐÃ KÝ (03:44 + 03:50 23/08) — KHÔNG HỎI LẠI ═══ ① Duyệt truy tiếp CẢ HAI: con số 9 ms chưa giải thích + khâu rút số (33.685 token không cho ra số nào). ② FU-419 lối (a): dòng «D-1 cross-region tail pool» chuyển thành GHI SỐ ĐẾM, bỏ danh sách. Ghi nhận điều kiện đi kèm: CẤM hứa nó làm tăng độ trúng (FU-316 đã đo: 20,2% vs nền 21…»*
> — owner, **23/08/2026 03:53** (giờ VN)

> *«push báo cáo chưa em?»*
> — owner, **23/08/2026 04:37** (giờ VN)

> *«Phiên prompt lần 28 đã xong việc nhưng báo cáo CHƯA lên kho GitHub công khai. Đóng phiên đúng kỷ luật: nâng bốn mặt version (_v11062) → lấy số hiệu từ _v11044 → đẩy báo cáo + tài liệu lên kho công khai → chạy cổng cuối phiên → xác nhận commit đã thấy trên remote. Xong báo lại mã commit.»*
> — owner, **23/08/2026 04:46** (giờ VN)

> *«PROMPT TỔNG LỰC LẦN 29 — TỐI 23/08: ĐÁNH GIÁ DỰ ĐOÁN + XỬ LÝ TOÀN BỘ TỒN ĐỌNG LỖI + ĐỌC LANE T-B + CHUYỂN HOÁ NGỮ CẢNH ĐỢT 1 ═══ BỐI CẢNH ═══ Live 23/08 đã kết thúc. Owner yêu cầu TỔNG LỰC: đánh giá dự đoán hôm nay, xử lý toàn bộ các lỗi đã được ký duyệt (FU-421, 425, 426, dòng chị em FU-419), đọc lane T-B (đã đủ 14 ngày), và bắt đầu CHUYỂN HOÁ NGỮ CẢNH NGAY LẬP TỨC (đợt 1). Không dậm chân tại chỗ. ═══ GĐ-0 · ĐÁNH GI…»*
> — owner, **23/08/2026 19:47** (giờ VN)

> *«PROMPT TỔNG LỰC LẦN 30 — 24/08: AUDIT CỰC GẮT — KIỂM CHỨNG DỮ LIỆU + ĐO MODEL AI NGAY + RỖNG→NGUYÊN NHÂN→THAY + ML GỐC→NGỌN + CHẤM DỨT "ĐO HOÀI KHÔNG RA" ═══ BỐI CẢNH ═══ Owner chất vấn 6 điểm: ① nghi ngờ dữ liệu kết quả bị ghi đè/trôi (MN không có bạch thủ 10) ② đòi ĐO MODEL AI TỚI ĐÂU NGAY, không chờ chuyển đổi ngữ cảnh ③ so sánh shadow vs official chéo regime là SAI (1 thằng nhồi số bốc thăm, 1 thằng tự kiếm số th…»*
> — owner, **23/08/2026 20:45** (giờ VN)

> *«PROMPT TỔNG LỰC LẦN 30 — 23/08 TỐI (CHẠY NGAY): AUDIT CỰC GẮT — KIỂM CHỨNG DỮ LIỆU + ĐO MODEL AI NGAY + RỖNG→NGUYÊN NHÂN→THAY + ML GỐC→NGỌN + CHẤM DỨT "ĐO HOÀI KHÔNG RA" ═══ BỐI CẢNH ═══ Owner chất vấn 6 điểm (20:42) + đòi tổng hợp toàn bộ yêu cầu (20:32) + yêu cầu CHẠY NGAY (20:51), không chờ 05:00. PHẦN AUDIT READ-ONLY LÀM NGAY. Chỉ 2 việc gắn mốc sau (ghi rõ trong báo cáo, không chặn phần còn lại): xác minh CTX-18…»*
> — owner, **23/08/2026 22:20** (giờ VN)


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
