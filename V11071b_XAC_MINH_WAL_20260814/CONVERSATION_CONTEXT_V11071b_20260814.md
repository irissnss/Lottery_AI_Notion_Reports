# CONVERSATION CONTEXT — V11071b · 2026-08-14

> **BẢN BÙ.** Viết ngày **2026-08-16**, việc xảy ra ngày **2026-08-14**.

## Vì sao bản này tồn tại

Ngày 16/08, owner yêu cầu *«đưa ra khối lượng agent lớn đi làm việc khắp nơi trong dự án để đào
cho ra chỗ thiếu sót»*. Đợt đào **49 tác nhân** tìm ra:

> **12 nhãn version trôi 4 ngày (13/08→16/08) mà CHANGELOG · SSOT · STATE · HISTORY đều đứng ở
> V11065, và kho báo cáo công khai không có thư mục `V1107*` nào.**

Gốc bệnh: `.claude/settings.json` **không tồn tại**, `.git/hooks/` **trống**, `.cursor/hooks.json`
dùng tên sự kiện **Cursor** mà Claude Code không đọc ⇒ **toàn bộ hàng rào cổng chưa bao giờ chạy**
trong các phiên đã tạo ra 12 bản này.

Owner đã nói thẳng: *«em làm việc vẫn chểnh mảng lắm rơi rớt tùm lum, anh phải nhắc đi nhắc lại,
nhấn mạnh nhiều lần mệt mỏi quá em»*. Bản bù này là một phần của việc dọn lại.

## Nội dung phiên 2026-08-14

Nguồn: commit `9a6873c` — bản ghi viết **tại thời điểm làm việc**.

```
Sau khi bat WAL va restart, agent nhan ra CHUA XAC MINH XONG: chua thay tep -wal, tuc ung dung
CHUA GHI lan nao ke tu restart. Bai thu truoc do dung KET NOI RIENG cua agent, KHONG phai module
ghi cua production. De toi 21:40 moi biet thi muon.

DA THU BANG CHINH database.get_connection() — dung duong ma production dung:
   ghi qua database.get_connection(): THANH CONG
   journal_mode ma production doc duoc: wal
   da don sach bang thu
4 bang khoa: model_daily_eval 12305 -> 12386 (tang tu nhien do cham diem toi, dung du kien);
ba bang con lai y het.

Bai hoc: 'da bat WAL' + 'ket noi rieng ghi duoc' KHONG bang 'duong GHI CUA PRODUCTION chay duoc'.
Phai thu dung module ma production dung — cung ho voi bai hoc 'lenh chay xong khong bang viec da
xay ra'.
```

## Trạng thái

Bù tài liệu, **không** dựng lại hội thoại đã mất. Những gì không ghi lại được thì **để trống**,
không suy đoán — đúng ranh giới `RM-17`.

TanPhatAI cần làm: xem `REPORT_V11071b.md` cùng thư mục.
