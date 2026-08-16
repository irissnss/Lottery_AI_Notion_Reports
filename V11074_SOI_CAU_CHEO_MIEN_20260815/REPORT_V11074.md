# REPORT V11074 — V11074: do SOI CAU CHEO MIEN theo cau hoi owner — quan sat DUNG nhung la SO HOC

> ## ⚠️ BÁO CÁO BÙ — ghi ngày **2026-08-16**, việc xảy ra ngày **2026-08-15**
>
> Bản này **KHÔNG** được viết tại thời điểm làm việc. Nó được bù ngày 16/08 sau khi đợt đào 49
> tác nhân phát hiện **12 nhãn version trôi 4 ngày không có báo cáo công khai nào** —
> vi phạm `§57.2`, và là **tái phạm** đúng ngày đến hạn xử `FU-375`.
>
> **Nguồn nội dung: chính commit message `8db3a83`** — bản ghi THẬT, viết tại thời điểm làm việc.
> Không bịa thêm. Phần nào không có dữ liệu thì ghi thẳng «không áp dụng vì …».
>
> Ranh giới với chế sử (`RM-17`): ngày việc xảy ra và ngày viết báo cáo **được ghi tách bạch**.

**Version:** `V11074` · **ngày việc:** 2026-08-15 · **commit:** `8db3a83` · **báo cáo bù:** 2026-08-16

---

## 1. Tóm tắt

V11074: do SOI CAU CHEO MIEN theo cau hoi owner — quan sat DUNG nhung la SO HOC

---

## 2. Owner yêu cầu gì (nguyên văn)

Xem `CONVERSATION_CONTEXT_V11074_20260815.md` cùng thư mục. Với các bản thuộc chuỗi
kiểm tra hằng ngày, yêu cầu gốc của owner là *«kiểm tra toàn diện/tổng lực dùm anh»* — lặp lại
mỗi ngày trong giai đoạn 13–16/08.

---

## 3. Đào bới / phát hiện · 4. Hướng xử lý · 5. Đã làm gì

Nguyên văn bản ghi tại thời điểm làm việc (commit `8db3a83`):

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
git revert 8db3a83
```

---

## 9. Theo dõi tiếp

- `FU-375` — tái phạm «commit không có báo cáo công khai», nay đã có cổng chặn (`V11076`)
- Gói **21/08** — 14 mục, xem `docs/FOLLOW_UP_TRACKER.md`

---

TanPhatAI cần làm: ghi nhận `V11074` (2026-08-15) đã có báo cáo công khai **bù ngày 16/08**; lưu ý bản
này **không** viết đương thời, nguồn là commit `8db3a83`.
