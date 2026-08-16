# CONVERSATION CONTEXT — V11069 · 2026-08-14

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

Nguồn: commit `3045196` — bản ghi viết **tại thời điểm làm việc**.

```
Kiem dau ngay 14/08. Moi thu sach: dich vu active, PID 1438110 khong doi, 0 loi moi loai,
0 dong "database is locked" (ban va FU-403 co tac dung), 3 cron toi qua ghi du,
MN chot BT=41 luc 05:19 voi 0 model rong.

VA BAN VA LUU BEN CUNG CO TAC DUNG NGAY: journal VAN GIU DUOC 13/08 voi 539 dong.
Hom qua gio nay chi con 1 dong.

TRUC TRAC TIM DUOC: lane MN sang nay chi 4 model, hom qua 5. deepseek-reasoner FAIL_TIMEOUT.
Do lai bang bang FU-283: do tre THAT cua deepseek-reasoner la 87-239s, chua bao gio vuot 300s
o duong official. Nhung lane chi ghi duoc 3/42 cap co deepseek, VA CA BA DEU LA MN.
Goc: TIMEOUT_THEO_MIEN = {MN:300, MT:120, MB:120}. MT/MB dat 120s la BAO DAM TRUOT.

VI SAO TRUOC DAY DAT 120s: luc do lane chay TRONG cua so official (cron 16:52 / 17:45) nen phai
nhuong. Toi 13/08 (FU-403) da doi lane ra 17:15 / 18:05 — SAU khi official chot => rang buoc do
KHONG CON: MT con ~15 phut toi gio xo, MB con ~25 phut.
Giu 120s bay gio chi la TU VUT DU LIEU.

DA SUA: TIMEOUT_THEO_MIEN = {MN:420, MT:300, MB:300}. Deploy + compile OK tren VPS.
Cong nhan qua van chan neu mien da xo, nen noi timeout KHONG THE lam hong tinh hop le.

Loi ich do duoc: lane dang 42 cap / 32 bat dong tren nguong 96. Neu deepseek ghi duoc o ca ba
mien thay vi chi MN, nhip tang them ~2 cap/ngay => ve dich som hon.
```

## Trạng thái

Bù tài liệu, **không** dựng lại hội thoại đã mất. Những gì không ghi lại được thì **để trống**,
không suy đoán — đúng ranh giới `RM-17`.

TanPhatAI cần làm: xem `REPORT_V11069.md` cùng thư mục.
