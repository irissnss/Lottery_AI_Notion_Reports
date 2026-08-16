# CONVERSATION CONTEXT — V11070 · 2026-08-14

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

Nguồn: commit `fef2c35` — bản ghi viết **tại thời điểm làm việc**.

```
KET QUA 14/08: 3/3 (MN 41 · MT 69 · MB 36). Nen dung 0,95/3; xac suat ca ba trung do ngau nhien
0,41x0,29x0,25 = 2,97% = 1 ngay trong 34. RM-04: n=3 CAM KET LUAN.

HAI SU CO HOM QUA KHONG TAI DIEN:
  MT bien han: 1 PHUT (13/08) -> 12 PHUT (14/08)
  model rong : 2 model (13/08) -> 0 model ca ba mien
  database is locked trong journal: 0 dong
=> ban va FU-403 (commit tung dong + doi cron) co tac dung.

PROBE FU-402 DA TRA LOI (1.077 mau, 16:35-18:05):
  21 mau thay DB BI KHOA = 2%
  cac dot khoa NGAN: 5-15 giay moi dot (16:37:42-57 · 16:41:43-53 · 16:48 · 16:50 · 17:30:36-46)
  => KHOA CO THAT NHUNG NGAN, KHONG giai thich duoc khoang lang 11 phut hom qua
  => hom nay KHONG co khoang lang nao => probe CHUA GAP LAI dieu kien hom qua
  => VAN CHUA KET LUAN duoc nguyen nhan FU-402. Probe chay tiep.

PHAT HIEN KEM, DANG GIA: wal=0 o MOI mau. Kiem ra:
  journal_mode = DELETE (khong phai WAL) · synchronous = 2 (FULL) · DB 707 MB
Trong che do DELETE, MOI LENH GHI KHOA EXCLUSIVE TOAN BO TEP — nguoi doc cung bi chan.
Day la NEN cua moi vu "database is locked". WAL cho phep doc song song voi ghi.
=> DE XUAT OWNER (chua tu lam vi cham DB production).

LANE: noi timeout an ngay. deepseek-reasoner GHI DUOC o MT (240s) va MB (140s) — truoc day
timeout 120s bao dam truot. MT/MB nay 5 cap thay vi 4. deepseek tu 3 cap len 5.
Cong don 52 cap / 38 bat dong / 96 => du nguong ~20-21/08.

FU-400 CAP NHAT (them 3 ngay, n 437 -> 443):
  A-B: -2,75pp -> -2,26pp · CI95 [-6,28..+0,79] -> [-5,80..+1,28] · z -1,456 -> -1,082
  Ngay 14/08 di NGUOC xu huong: trong so CUU 2/3 (MN hang #3, MB hang #2).
  Cua so 30 ngay DA DOI DAU: +5,56pp (z=+0,97), nhung 60/90/120/toan bo VAN AM.
  DOC DUNG: CI nay trum 0 RONG HON => BANG CHUNG YEU DI, khong manh len.
  Tran "trong so giup" noi tu +0,79pp len +1,28pp. VAN CHUA DUOC PHEP KET LUAN.
```

## Trạng thái

Bù tài liệu, **không** dựng lại hội thoại đã mất. Những gì không ghi lại được thì **để trống**,
không suy đoán — đúng ranh giới `RM-17`.

TanPhatAI cần làm: xem `REPORT_V11070.md` cùng thư mục.
