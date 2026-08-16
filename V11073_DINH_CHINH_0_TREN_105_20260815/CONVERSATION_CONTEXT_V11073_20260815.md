# CONVERSATION CONTEXT — V11073 · 2026-08-15

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

Nguồn: commit `4553838` — bản ghi viết **tại thời điểm làm việc**.

```
Owner hoi: "105 luat khai mo: 0/105 qua cong la sao em?"

AGENT DA NOI SAI CHU. Do lai tren du lieu that ngay 15/08:
   tong luat mined_rules      105
   READY_STRONG (qua cong)      8   <== KHONG phai 0
   READY_WITH_CAUTION          31
   LIMITED_WEIGHT              66

Y DUNG ma agent muon noi: 0/105 tung duoc kiem tren du lieu CHUNG CHUA THAY.
Toan bo 105 luat khai mo CUNG MOT LUC: 2026-08-10T00:30. Cac cot hr_4w/hr_8w/hr_12w la "ti le
trung 4/8/12 tuan qua" nhung TINH TAI THOI DIEM KHAI MO — tuc nhin nguoc vao chinh du lieu da
dung de chon ra luat. Mot luat duoc chon VI no khop 4 tuan qua thi duong nhien hr_4w = 1.0.
Do la DINH NGHIA, khong phai BANG CHUNG.

PHEP DO TRONG vs NGOAI MAU (dung mined_rule_effectiveness, 3737 dong, DA CO SAN — khong dung
bang moi). Nen dung = so duoi ra ngay do/100 x tails_count (RM-18):
   8 luat READY_STRONG : trong mau +37,7% (n=174 o) · NGOAI MAU -66,4% (n=5 o)
   toan bo 105 luat    : trong mau  +9,9% (n=3658)  · NGOAI MAU  -1,6% (n=75)
=> Loi the +9,9% BIEN MAT HOAN TOAN khi luat gap du lieu chua tung thay.

GIOI HAN PHAI NOI KEM — cam doc qua con so:
 - ngoai mau moi co n=75 o / 5 ngay => QUA NHO DE KET LUAN (RM-04). Rieng 8 luat READY_STRONG
   chi co n=5 o, tuc gan nhu khong co du lieu.
 - huong thi ro va khop khuon kinh dien: khop manh trong mau, ve 0 ngoai mau.
 - KHONG duoc dung con so nay de noi "luat khai mo co hai" — no chi du de noi "chua co bang
   chung nao cho thay chung co loi ngoai mau".

NOI VAO GOI 21/08: day la BANG CHUNG cho muc D2 (MINED_RULES_MODE soft -> shadow) DA CO SAN
trong goi, KHONG phai muc moi (QD-4). Viec nen lam sau 21/08: de bo luat chay shadow them ~4
tuan roi doc lai cot ngoai mau khi n du.

Bai hoc cho chinh agent: "0/105" la cach noi an tuong nhung SAI. Con so cong bo phai TAI LAP
DUOC va phai dung chu (RM-11, RM-17).
```

## Trạng thái

Bù tài liệu, **không** dựng lại hội thoại đã mất. Những gì không ghi lại được thì **để trống**,
không suy đoán — đúng ranh giới `RM-17`.

TanPhatAI cần làm: xem `REPORT_V11073.md` cùng thư mục.
