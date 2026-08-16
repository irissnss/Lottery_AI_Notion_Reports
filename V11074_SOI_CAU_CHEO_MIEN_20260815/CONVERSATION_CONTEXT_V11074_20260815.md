# CONVERSATION CONTEXT — V11074 · 2026-08-15

> **BẢN BÙ.** Viết ngày **2026-08-16**, việc xảy ra ngày **2026-08-15**.

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

## Nội dung phiên 2026-08-15

Nguồn: commit `8db3a83` — bản ghi viết **tại thời điểm làm việc**.

```
Owner neu 15/08: 'dich MB hom nay thi nguon MT co 58, MN co 66,83... lam sao khai thac day em'.

QUAN SAT CUA OWNER DUNG — kiem tung so:
  58 : MT Dak Nong Giai Dac Biet -> MB Nam Dinh Giai sau
  66 : MN Long An Giai bay       -> MB Nam Dinh Giai bay
  83 : MN Hau Giang G7/Long An G4/TPHCM G4 -> MB Nam Dinh Giai nam

NHUNG DO LA SO HOC, KHONG PHAI TIN HIEU:
  15/08: MN 50 duoi + MT 40 duoi = hop lai 67/100 duoi cua bang so
         MB ra 22 duoi, 15 (68%) co trong MN/MT
         ky vong neu BA MIEN HOAN TOAN DOC LAP: 22 x 0,67 = 14,7 => chenh +0,3
  31 ngay: thuc te 460 · ngau nhien 454 => chenh +6 = +1,2%
MN+MT phu 2/3 bang so nen gan nhu MOI so cua MB deu tim thay duoc o MN/MT ke ca khi ba mien doc
lap hoan toan. Nhin thay 58/66/83 khop la vi NHIN SAU KHI BIET KET QUA.

BAN HEP — do dung cau truc owner chi ra (VI TRI GIAI), 60 ngay, 18 to hop nguon-giai:
  cao nhat MT Giai nhi z=+1,44 · MT Giai sau z=+1,16
  MT Giai Dac Biet (nguon cua so 58) z=-0,11 — DUNG BANG NEN
  0/18 to hop dat |z|>=1,96
Va thu 18 thu thi ky vong ~1 cai vuot nguong do may rui — KHONG CAI NAO VUOT. Nen day la bang
chung UNG HO gia thuyet KHONG co tin hieu, khong phai 'chua tim thay'.

VI SAO KHO KHAI THAC: van de khong phai 'co mau hinh hay khong' ma la 'mau hinh co HEP HON SO
HOC khong'. Nguon rong (67 so) thi trung la duong nhien; nguon hep (mot giai) thi ve dung nen.
Muon khai thac phai hep toi muc du doan duoc SO NAO trong 67 so se ve — do chinh la viec
mined_rules dang lam: +9,9% trong mau, -1,6% ngoai mau.

NOI VAO 21/08: ung ho muc D2 (MINED_RULES_MODE soft -> shadow) DA CO trong goi, khong phai muc moi.
CO THE dang thu sau 21/08 (chi neu owner muon, va phai DO TIEN): HAI NGUON CUNG DONG Y — so xuat
hien o CA MN VA MT cung ngay. Ban hep hon chua do, co co che hop ly, do duoc trong ~3 tuan.
Uoc tinh nhanh: ~23 so/ngay (giao cua 50 va 40) — van con rong nen KY VONG THAP.
```

## Trạng thái

Bù tài liệu, **không** dựng lại hội thoại đã mất. Những gì không ghi lại được thì **để trống**,
không suy đoán — đúng ranh giới `RM-17`.

TanPhatAI cần làm: xem `REPORT_V11074.md` cùng thư mục.
