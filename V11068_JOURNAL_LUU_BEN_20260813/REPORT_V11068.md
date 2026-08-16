# REPORT V11068 — V11068 (FU-402): journal VOLATILE -> LUU BEN 7 ngay — go rao chan moi viec truy vet

> ## ⚠️ BÁO CÁO BÙ — ghi ngày **2026-08-16**, việc xảy ra ngày **2026-08-13**
>
> Bản này **KHÔNG** được viết tại thời điểm làm việc. Nó được bù ngày 16/08 sau khi đợt đào 49
> tác nhân phát hiện **12 nhãn version trôi 4 ngày không có báo cáo công khai nào** —
> vi phạm `§57.2`, và là **tái phạm** đúng ngày đến hạn xử `FU-375`.
>
> **Nguồn nội dung: chính commit message `4410e86`** — bản ghi THẬT, viết tại thời điểm làm việc.
> Không bịa thêm. Phần nào không có dữ liệu thì ghi thẳng «không áp dụng vì …».
>
> Ranh giới với chế sử (`RM-17`): ngày việc xảy ra và ngày viết báo cáo **được ghi tách bạch**.

**Version:** `V11068` · **ngày việc:** 2026-08-13 · **commit:** `4410e86` · **báo cáo bù:** 2026-08-16

---

## 1. Tóm tắt

V11068 (FU-402): journal VOLATILE -> LUU BEN 7 ngay — go rao chan moi viec truy vet

---

## 2. Owner yêu cầu gì (nguyên văn)

Xem `CONVERSATION_CONTEXT_V11068_20260813.md` cùng thư mục. Với các bản thuộc chuỗi
kiểm tra hằng ngày, yêu cầu gốc của owner là *«kiểm tra toàn diện/tổng lực dùm anh»* — lặp lại
mỗi ngày trong giai đoạn 13–16/08.

---

## 3. Đào bới / phát hiện · 4. Hướng xử lý · 5. Đã làm gì

Nguyên văn bản ghi tại thời điểm làm việc (commit `4410e86`):

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
git revert 4410e86
```

---

## 9. Theo dõi tiếp

- `FU-375` — tái phạm «commit không có báo cáo công khai», nay đã có cổng chặn (`V11076`)
- Gói **21/08** — 14 mục, xem `docs/FOLLOW_UP_TRACKER.md`

---

TanPhatAI cần làm: ghi nhận `V11068` (2026-08-13) đã có báo cáo công khai **bù ngày 16/08**; lưu ý bản
này **không** viết đương thời, nguồn là commit `4410e86`.
