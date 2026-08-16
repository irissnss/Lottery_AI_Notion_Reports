# REPORT V11071b — V11071b: xac minh duong GHI cua production chay duoc duoi WAL

> ## ⚠️ BÁO CÁO BÙ — ghi ngày **2026-08-16**, việc xảy ra ngày **2026-08-14**
>
> Bản này **KHÔNG** được viết tại thời điểm làm việc. Nó được bù ngày 16/08 sau khi đợt đào 49
> tác nhân phát hiện **12 nhãn version trôi 4 ngày không có báo cáo công khai nào** —
> vi phạm `§57.2`, và là **tái phạm** đúng ngày đến hạn xử `FU-375`.
>
> **Nguồn nội dung: chính commit message `9a6873c`** — bản ghi THẬT, viết tại thời điểm làm việc.
> Không bịa thêm. Phần nào không có dữ liệu thì ghi thẳng «không áp dụng vì …».
>
> Ranh giới với chế sử (`RM-17`): ngày việc xảy ra và ngày viết báo cáo **được ghi tách bạch**.

**Version:** `V11071b` · **ngày việc:** 2026-08-14 · **commit:** `9a6873c` · **báo cáo bù:** 2026-08-16

---

## 1. Tóm tắt

V11071b: xac minh duong GHI cua production chay duoc duoi WAL

---

## 2. Owner yêu cầu gì (nguyên văn)

Xem `CONVERSATION_CONTEXT_V11071b_20260814.md` cùng thư mục. Với các bản thuộc chuỗi
kiểm tra hằng ngày, yêu cầu gốc của owner là *«kiểm tra toàn diện/tổng lực dùm anh»* — lặp lại
mỗi ngày trong giai đoạn 13–16/08.

---

## 3. Đào bới / phát hiện · 4. Hướng xử lý · 5. Đã làm gì

Nguyên văn bản ghi tại thời điểm làm việc (commit `9a6873c`):

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

---

## 6. Cổng kiểm

Xem phần cuối khối trên. Các bản chạm production đều ghi PID trước/sau, `/api/health`, và số dòng
4 bảng khoá.

---

## 7. Vướng vấp

Ghi ngay trong khối trên khi có. **Vướng vấp lớn nhất của cả cụm 12 bản này là chính việc thiếu
báo cáo** — nguyên nhân: `.claude/settings.json` không tồn tại nên **không cổng nào chạy** trong
các phiên Claude Code (xem `V11076`).

---

## 8. Gỡ về

```bash
git revert 9a6873c
```

---

## 9. Theo dõi tiếp

- `FU-375` — tái phạm «commit không có báo cáo công khai», nay đã có cổng chặn (`V11076`)
- Gói **21/08** — 14 mục, xem `docs/FOLLOW_UP_TRACKER.md`

---

TanPhatAI cần làm: ghi nhận `V11071b` (2026-08-14) đã có báo cáo công khai **bù ngày 16/08**; lưu ý bản
này **không** viết đương thời, nguồn là commit `9a6873c`.
