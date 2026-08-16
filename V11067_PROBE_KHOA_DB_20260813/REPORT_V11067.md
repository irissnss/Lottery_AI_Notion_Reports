# REPORT V11067 — V11067 (FU-402): bo lay mau khoa DB — bat thu pham cua khoang lang 11 phut

> ## ⚠️ BÁO CÁO BÙ — ghi ngày **2026-08-16**, việc xảy ra ngày **2026-08-13**
>
> Bản này **KHÔNG** được viết tại thời điểm làm việc. Nó được bù ngày 16/08 sau khi đợt đào 49
> tác nhân phát hiện **12 nhãn version trôi 4 ngày không có báo cáo công khai nào** —
> vi phạm `§57.2`, và là **tái phạm** đúng ngày đến hạn xử `FU-375`.
>
> **Nguồn nội dung: chính commit message `2e913e1`** — bản ghi THẬT, viết tại thời điểm làm việc.
> Không bịa thêm. Phần nào không có dữ liệu thì ghi thẳng «không áp dụng vì …».
>
> Ranh giới với chế sử (`RM-17`): ngày việc xảy ra và ngày viết báo cáo **được ghi tách bạch**.

**Version:** `V11067` · **ngày việc:** 2026-08-13 · **commit:** `2e913e1` · **báo cáo bù:** 2026-08-16

---

## 1. Tóm tắt

V11067 (FU-402): bo lay mau khoa DB — bat thu pham cua khoang lang 11 phut

---

## 2. Owner yêu cầu gì (nguyên văn)

Xem `CONVERSATION_CONTEXT_V11067_20260813.md` cùng thư mục. Với các bản thuộc chuỗi
kiểm tra hằng ngày, yêu cầu gốc của owner là *«kiểm tra toàn diện/tổng lực dùm anh»* — lặp lại
mỗi ngày trong giai đoạn 13–16/08.

---

## 3. Đào bới / phát hiện · 4. Hướng xử lý · 5. Đã làm gì

Nguyên văn bản ghi tại thời điểm làm việc (commit `2e913e1`):

```
Owner: "ok lam di dung chan chu ngay nao cung te te te riet nan qua luon".

VAN DE: MT 13/08 chot cach han 1 PHUT. Khoang lang 11 phut 1 giay giua "moi model xong"
(16:42:47) va "combo-super ghi" (16:57:31). Tien trinh KHONG treo (nhip scheduler 16:45/16:50
van chay xong trong 100ms). CHUA GIAI THICH DUOC.

VI SAO KHONG SUA combo_super.py DE THEM LOG:
 (1) QD-041 khoa duong chon so toi 21/08 — combo_super.py CHINH LA duong do
 (2) them ma vao ham dang phuc vu, du chi la print, van co xac suat khac 0 lam hong luot that
 (3) JOURNAL KHONG GIU DUOC: journal ngay 12/08 chi con 1 DONG. Moi moc in ra stdout se boc hoi
     sau mot ngay => probe dua vao journal la probe VO DUNG
=> Lay mau TU BEN NGOAI, ghi ra tep rieng, CHAM 0 DONG MA PRODUCTION.

DO GI: moi nhip
   BEGIN IMMEDIATE voi timeout=0  -> DB co dang bi GIU khoa ghi khong (cau chinh)
   kich thuoc -wal                -> co giao dich lon dang mo khong
   so dong predictions hom nay    -> chuoi co DANG TIEN hay dung im
   fuser tren tep DB              -> AI giu khoa (chi goi khi CO khoa, do ton)

KET LUAN DUOC CA HAI CHIEU: neu suot khoang lang ma BEGIN IMMEDIATE luon truot => dung la tranh
chap khoa, va fuser chi ra thu pham. Neu luon thanh cong => KHONG phai khoa DB, phai tim huong
khac — LOAI DUOC MOT GIA THUYET CUNG LA KET QUA.

HOP DONG AN TOAN — khong lap lai chinh loi vua va o FU-403:
 - timeout=0 de KHONG BAO GIO xep hang cho khoa; tha bao "dang khoa" con hon tu minh cho va
   thanh mot ke giu khoa nua
 - BEGIN IMMEDIATE roi ROLLBACK NGAY, giu vai mili-giay, va chi khi DB dang ranh
 - ghi ra logs/v11067_khoa_db.jsonl, KHONG ghi vao DB
 - loi => ghi roi chay tiep, khong raise (cron-safe)

DA THU: 6 mau/1 phut, chay dung, doc lai dung. Da xoa file mau thu de mai chay sach.
CRON: 16:35 chay 90 phut, nhip 5s — phu ca cua so MT (16:35-16:58) va MB (17:25-17:58).
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
git revert 2e913e1
```

---

## 9. Theo dõi tiếp

- `FU-375` — tái phạm «commit không có báo cáo công khai», nay đã có cổng chặn (`V11076`)
- Gói **21/08** — 14 mục, xem `docs/FOLLOW_UP_TRACKER.md`

---

TanPhatAI cần làm: ghi nhận `V11067` (2026-08-13) đã có báo cáo công khai **bù ngày 16/08**; lưu ý bản
này **không** viết đương thời, nguồn là commit `2e913e1`.
