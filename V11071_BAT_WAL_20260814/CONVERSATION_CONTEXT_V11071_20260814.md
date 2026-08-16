# CONVERSATION CONTEXT — V11071 · 2026-08-14

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

Nguồn: commit `9d6c4fd` — bản ghi viết **tại thời điểm làm việc**.

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

## Trạng thái

Bù tài liệu, **không** dựng lại hội thoại đã mất. Những gì không ghi lại được thì **để trống**,
không suy đoán — đúng ranh giới `RM-17`.

TanPhatAI cần làm: xem `REPORT_V11071.md` cùng thư mục.
