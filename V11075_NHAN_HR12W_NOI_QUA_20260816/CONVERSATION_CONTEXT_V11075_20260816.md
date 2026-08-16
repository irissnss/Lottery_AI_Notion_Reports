# CONVERSATION CONTEXT — V11075 · 2026-08-16

> **BẢN BÙ.** Viết ngày **2026-08-16**, việc xảy ra ngày **2026-08-16**.

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

## Nội dung phiên 2026-08-16

Nguồn: commit `61ee931` — bản ghi viết **tại thời điểm làm việc**.

```
Owner chat van 16/08: "cac yeu cau ve tong hop cac co che, quy tac soi cau, rules thanh ngu canh
de bom vao model AI thi sao em? Anh thay truoc do anh co gui nhieu yeu cau ve viec nay roi ma em?
Sao gio nay em van lan quan miet vay em?"

AGENT DA SAI VA OWNER BAT DUNG.
Luot truoc agent noi "rules chi CONG DIEM cho so model da neu, khong sinh so" — THIEU.
Context Pack CTX-18.3 CO khoi [V2-RULES] bom soi-cau vao prompt => luat CO tac dong vao khau SINH.
YEU CAU CUA OWNER DA DUOC LAM VA DANG CHAY. Vi du that, MN/Chu Nhat 16/08:
   "Nguon MB/Nam Dinh offset-D-1 giai GDB+G6 -> MN: HR12W 1.0 (n=20, TANG_TRUONG)"
Dung dang soi cau cheo mien owner mo ta: nguon dai + giai -> mien dich.

NHUNG PHAT HIEN MOT LOI THAT TRONG DO:
   moi luat de xuat 3,5 so (1-7)
   HR12W = 1.0 nghia la "12/12 tuan deu trung IT NHAT 1 trong 3,5 so"
   KHONG phai "dung 100%"
   prompt hien thi "HR12W 1.0" => model doc thanh CHAC CHAN TUYET DOI
Loi the THAT cua 41 luat mang nhan 1.0:
   trong mau +1,0% (n=1069 o) · ngoai mau +1,5% (n=24 o)  => DUNG BANG NEN
41/105 = 39% bo luat dang duoc gioi thieu voi model bang mot con so noi qua.

DAY LA LOI CUA TA, KHONG PHAI CUA MODEL. Model tin 1.0 la hop ly — no khong co cach nao biet
HR12W do "co it nhat mot so trung" chu khong phai "so de xuat trung". Dung ho RM-18: so ti le
cua BO k SO voi chuan cua 1 SO.

HUONG SUA (CHUA LAM): thay "HR12W 1.0" bang loi the tren nen kem n va trang thai ngoai mau,
vi du "+1,0% tren nen, n=20, CHUA co bang chung ngoai mau". Model se tu ha trong so dung muc.
VI SAO CHUA SUA: sua noi dung Context Pack = CHAM PROMPT => QD-041 khoa toi 21/08, va QD-4 khoa
pham vi goi => OWNER QUYET co dua vao goi hay de HANG DOI.
```

## Trạng thái

Bù tài liệu, **không** dựng lại hội thoại đã mất. Những gì không ghi lại được thì **để trống**,
không suy đoán — đúng ranh giới `RM-17`.

TanPhatAI cần làm: xem `REPORT_V11075.md` cùng thư mục.
