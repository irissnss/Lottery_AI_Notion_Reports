# CONVERSATION CONTEXT — V11067 · 2026-08-13

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

Nguồn: commit `2e913e1` — bản ghi viết **tại thời điểm làm việc**.

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

## Trạng thái

Bù tài liệu, **không** dựng lại hội thoại đã mất. Những gì không ghi lại được thì **để trống**,
không suy đoán — đúng ranh giới `RM-17`.

TanPhatAI cần làm: xem `REPORT_V11067.md` cùng thư mục.
