# CONVERSATION CONTEXT — V11068 · 2026-08-13

> **BẢN BÙ.** Viết ngày **2026-08-16**, việc xảy ra ngày **2026-08-13**.

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

## Nội dung phiên 2026-08-13

Nguồn: commit `4410e86` — bản ghi viết **tại thời điểm làm việc**.

```
Owner duyet: "ok lam luon di em".

PHAT HIEN LON HON CA RETENTION:
/var/log/journal KHONG TON TAI => journal nam trong /run (RAM, VOLATILE).
Hai hau qua:
  (1) MAT SACH moi lan reboot
  (2) /run gioi han theo RAM (max 100M) nen xoay vong rat gat
      => ngay 12/08 CHI CON 1 DONG, trong khi 13/08 co 18.295 dong
      => MOI SU CO QUA 24 GIO LA KHONG THE DIEU TRA
Day chinh la ly do probe FU-402 phai ghi ra tep rieng thay vi dua vao journal.

DA LAM (drop-in, go lai = xoa dung mot tep):
  /etc/systemd/journald.conf.d/99-lottery-retention.conf
     Storage=persistent · SystemMaxUse=500M · SystemKeepFree=1G
     MaxRetentionSec=7day · RuntimeMaxUse=100M
  mkdir -p /var/log/journal + systemd-tmpfiles --create (dat quyen chuan)
  systemctl restart systemd-journald
  systemctl RESTART systemd-journal-flush   <-- BUOC BI SOT LAN DAU

VAP: hai lan dau restart xong van thay File path = /run/... Agent KHONG restart lan ba ma di
truy: drop-in CO duoc doc (Storage=persistent hien trong cau hinh hop nhat), thu muc CO va dung
quyen, nhung journald van ghi vao /run. Goc: systemd-journal-flush la ONESHOT DA CHAY TU 18/04 va
dang active(exited) => lenh `systemctl start` KHONG LAM GI CA. Phai `restart` moi kich lai.
Bai hoc: "lenh chay xong" khong bang "viec da xay ra" — phai kiem DAU VET (File path), dung tin
chu 'restart thanh cong'.

KIEM CHUNG THAT (khong chi doc cau hinh):
  File path: /var/log/journal/c4c19408.../system.journal   <- da la luu ben
  /var/log/journal/<machine-id>/ ton tai, 25M
  ghi mot dong bang logger roi doc lai duoc
  System Journal max 500.0M, con trong 475.9M
  lottery: active · PID 1438110 KHONG DOI · health 200

Dia: 39G tong, con 12G. Tran 500M = 4% cho trong. An toan.
Tu ngay mai truy vet duoc 7 NGAY thay vi 1 ngay.
```

## Trạng thái

Bù tài liệu, **không** dựng lại hội thoại đã mất. Những gì không ghi lại được thì **để trống**,
không suy đoán — đúng ranh giới `RM-17`.

TanPhatAI cần làm: xem `REPORT_V11068.md` cùng thư mục.
