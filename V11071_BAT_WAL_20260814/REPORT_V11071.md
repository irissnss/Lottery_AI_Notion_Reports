# REPORT V11071 — V11071: BAT WAL cho DB production — go nen cua moi vu "database is locked"

> ## ⚠️ BÁO CÁO BÙ — ghi ngày **2026-08-16**, việc xảy ra ngày **2026-08-14**
>
> Bản này **KHÔNG** được viết tại thời điểm làm việc. Nó được bù ngày 16/08 sau khi đợt đào 49
> tác nhân phát hiện **12 nhãn version trôi 4 ngày không có báo cáo công khai nào** —
> vi phạm `§57.2`, và là **tái phạm** đúng ngày đến hạn xử `FU-375`.
>
> **Nguồn nội dung: chính commit message `9d6c4fd`** — bản ghi THẬT, viết tại thời điểm làm việc.
> Không bịa thêm. Phần nào không có dữ liệu thì ghi thẳng «không áp dụng vì …».
>
> Ranh giới với chế sử (`RM-17`): ngày việc xảy ra và ngày viết báo cáo **được ghi tách bạch**.

**Version:** `V11071` · **ngày việc:** 2026-08-14 · **commit:** `9d6c4fd` · **báo cáo bù:** 2026-08-16

---

## 1. Tóm tắt

V11071: BAT WAL cho DB production — go nen cua moi vu "database is locked"

---

## 2. Owner yêu cầu gì (nguyên văn)

Xem `CONVERSATION_CONTEXT_V11071_20260814.md` cùng thư mục. Với các bản thuộc chuỗi
kiểm tra hằng ngày, yêu cầu gốc của owner là *«kiểm tra toàn diện/tổng lực dùm anh»* — lặp lại
mỗi ngày trong giai đoạn 13–16/08.

---

## 3. Đào bới / phát hiện · 4. Hướng xử lý · 5. Đã làm gì

Nguyên văn bản ghi tại thời điểm làm việc (commit `9d6c4fd`):

```
Owner duyet: "ok tot la lam thoi em. khong co rui ro thi lam thoi em".

AGENT DINH CHINH TRUOC KHI LAM: KHONG PHAI khong co rui ro.
Voi WAL, du lieu moi nam trong tep -wal CHUA NHAP vao .db. Cho nao sao chep MOI tep .db se lay
duoc ban THIEU du lieu moi nhat — ma khong co trieu chung gi.
=> Da quet truoc khi bat:
   _sync_live_forensic_inputs.py  freeze bang `sqlite3 .backup`  => AN TOAN (backup hieu WAL)
   _sync_db.py                    dung sftp.get() tho            => KHONG an toan, nhung 0 CRON
   cron tren VPS                  khong cron nao copy tep .db    => an toan
=> Rui ro that CO ton tai nhung nam o mot script CHAY TAY. Da them canh bao dau tep do.

DA LAM:
  [1] sao luu nhat quan truoc: sqlite3 .backup -> /root/lottery_ai.db.pre_wal_20260814 (707 MB)
  [2] PRAGMA journal_mode=WAL  (delete -> wal)
  [3] quick_check: ok · wal_autocheckpoint: 1000 trang (mac dinh)
  [4] restart lottery: PID 1438110 -> 1633166 (doi that) · NRestarts=0 · health 200
  [5] 4 bang khoa TRUOC va SAU deu 12522/504/15278/12305 — y het

CHUNG MINH LOI ICH THAT (khong chi kiem "co la co lat chua"):
  mot ben GIU giao dich ghi chua commit, roi:
    ben DOC   -> THANH CONG sau 0,007s, doc duoc 12.522 dong predictions
    ben GHI 2 -> BI CHAN dung nhu mong doi ("database is locked")
  => doc KHONG con bi chan boi ghi, con ghi-ghi van loai tru dung. Dung thu WAL phai lam.

VI SAO CAN: probe V11067 do duoc 21/1077 mau (2%) thay DB bi khoa ghi, va che do cu la
journal_mode=DELETE — moi lenh ghi khoa EXCLUSIVE TOAN BO TEP, nguoi doc cung bi chan.
Do la NEN cua vu 13/08 lam mat ket qua gemini-3.5-flash va gemini-3.6-flash o MB.

GO VE: sqlite3 data/lottery_ai.db "PRAGMA journal_mode=DELETE;" + restart lottery.
Ban sao luu truoc khi doi: /root/lottery_ai.db.pre_wal_20260814
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
git revert 9d6c4fd
```

---

## 9. Theo dõi tiếp

- `FU-375` — tái phạm «commit không có báo cáo công khai», nay đã có cổng chặn (`V11076`)
- Gói **21/08** — 14 mục, xem `docs/FOLLOW_UP_TRACKER.md`

---

TanPhatAI cần làm: ghi nhận `V11071` (2026-08-14) đã có báo cáo công khai **bù ngày 16/08**; lưu ý bản
này **không** viết đương thời, nguồn là commit `9d6c4fd`.
