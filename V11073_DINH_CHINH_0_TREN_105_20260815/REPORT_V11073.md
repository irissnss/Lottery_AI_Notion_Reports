# REPORT V11073 — V11073: DINH CHINH "0/105 luat qua cong" + do TRONG vs NGOAI MAU

> ## ⚠️ BÁO CÁO BÙ — ghi ngày **2026-08-16**, việc xảy ra ngày **2026-08-15**
>
> Bản này **KHÔNG** được viết tại thời điểm làm việc. Nó được bù ngày 16/08 sau khi đợt đào 49
> tác nhân phát hiện **12 nhãn version trôi 4 ngày không có báo cáo công khai nào** —
> vi phạm `§57.2`, và là **tái phạm** đúng ngày đến hạn xử `FU-375`.
>
> **Nguồn nội dung: chính commit message `4553838`** — bản ghi THẬT, viết tại thời điểm làm việc.
> Không bịa thêm. Phần nào không có dữ liệu thì ghi thẳng «không áp dụng vì …».
>
> Ranh giới với chế sử (`RM-17`): ngày việc xảy ra và ngày viết báo cáo **được ghi tách bạch**.

**Version:** `V11073` · **ngày việc:** 2026-08-15 · **commit:** `4553838` · **báo cáo bù:** 2026-08-16

---

## 1. Tóm tắt

V11073: DINH CHINH "0/105 luat qua cong" + do TRONG vs NGOAI MAU

---

## 2. Owner yêu cầu gì (nguyên văn)

Xem `CONVERSATION_CONTEXT_V11073_20260815.md` cùng thư mục. Với các bản thuộc chuỗi
kiểm tra hằng ngày, yêu cầu gốc của owner là *«kiểm tra toàn diện/tổng lực dùm anh»* — lặp lại
mỗi ngày trong giai đoạn 13–16/08.

---

## 3. Đào bới / phát hiện · 4. Hướng xử lý · 5. Đã làm gì

Nguyên văn bản ghi tại thời điểm làm việc (commit `4553838`):

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
git revert 4553838
```

---

## 9. Theo dõi tiếp

- `FU-375` — tái phạm «commit không có báo cáo công khai», nay đã có cổng chặn (`V11076`)
- Gói **21/08** — 14 mục, xem `docs/FOLLOW_UP_TRACKER.md`

---

TanPhatAI cần làm: ghi nhận `V11073` (2026-08-15) đã có báo cáo công khai **bù ngày 16/08**; lưu ý bản
này **không** viết đương thời, nguồn là commit `4553838`.
