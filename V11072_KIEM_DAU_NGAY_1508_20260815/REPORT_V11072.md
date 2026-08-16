# REPORT V11072 — V11072: kiem dau ngay 15/08 — WAL song qua dem, va agent sua chinh loi minh vua tao

> ## ⚠️ BÁO CÁO BÙ — ghi ngày **2026-08-16**, việc xảy ra ngày **2026-08-15**
>
> Bản này **KHÔNG** được viết tại thời điểm làm việc. Nó được bù ngày 16/08 sau khi đợt đào 49
> tác nhân phát hiện **12 nhãn version trôi 4 ngày không có báo cáo công khai nào** —
> vi phạm `§57.2`, và là **tái phạm** đúng ngày đến hạn xử `FU-375`.
>
> **Nguồn nội dung: chính commit message `aefadf5`** — bản ghi THẬT, viết tại thời điểm làm việc.
> Không bịa thêm. Phần nào không có dữ liệu thì ghi thẳng «không áp dụng vì …».
>
> Ranh giới với chế sử (`RM-17`): ngày việc xảy ra và ngày viết báo cáo **được ghi tách bạch**.

**Version:** `V11072` · **ngày việc:** 2026-08-15 · **commit:** `aefadf5` · **báo cáo bù:** 2026-08-16

---

## 1. Tóm tắt

V11072: kiem dau ngay 15/08 — WAL song qua dem, va agent sua chinh loi minh vua tao

---

## 2. Owner yêu cầu gì (nguyên văn)

Xem `CONVERSATION_CONTEXT_V11072_20260815.md` cùng thư mục. Với các bản thuộc chuỗi
kiểm tra hằng ngày, yêu cầu gốc của owner là *«kiểm tra toàn diện/tổng lực dùm anh»* — lặp lại
mỗi ngày trong giai đoạn 13–16/08.

---

## 3. Đào bới / phát hiện · 4. Hướng xử lý · 5. Đã làm gì

Nguyên văn bản ghi tại thời điểm làm việc (commit `aefadf5`):

```
WAL SONG TOT QUA DEM (cau con no tu 14/08):
  journal_mode=wal · quick_check=ok · PID 1633166 KHONG DOI · NRestarts=0 · health 200
  journal hom nay: 0 Traceback / 0 ERROR / 0 CRITICAL / 0 "database is locked"
  3 cron toi qua ghi du (P4 3 dong, anti-trap 3 dong, do tre 57 dong)

HOM QUA 14/08: 3/3 BACH THU (MN 41 · MT 69 · MB 36). Bien MT ve 12 phut — binh thuong tro lai
sau vu 1 phut ngay 13/08.

HOM NAY MN co 2 model RONG — DA LOAI TRU WAL:
  deepseek-reasoner : "DeepSeek returned empty response" (nha cung cap tra rong)
  glm-5.1           : "Loi phan tich response JSON: Expecting value: line 1 column 1"
KHONG loi nao la "database is locked".
So dong rong 10 ngay: 0·1·2·0·0·1·1·3·0·2 => hom nay 2 NAM DUNG TRONG DAI BINH THUONG.
Ngay te nhat la 13/08 (3 dong) — chinh ngay khoa DB; sau khi va thi 14/08 ve 0.
Tan suat rieng: deepseek-reasoner 3/28 = 11% · glm-5.1 1/27 = 4% trong 10 ngay.

PROBE FU-402 (chay 16:35-18:04 hom qua, 1077 mau):
  21 mau (2%) thay DB BI KHOA. Cac dot: 16:37:42-16:37:57 (~20s) · 16:41:43-16:41:53 (~15s)
  + hai mau le. DOT DAI NHAT ~20 GIAY, KHONG dot nao toi 11 phut.
  => Khoang lang 13/08 KHONG giai thich duoc bang mot cu khoa dai.
  GIOI HAN PHAI NOI RO: hom qua MT chot som 12 phut, tuc SU CO KHONG TAI DIEN — probe chi quan
  sat duoc mot NGAY BINH THUONG. No cho DUONG NEN (2%, dot <=20s), chua bat duoc luc hong.
  Va wal=0 trong moi mau vi WAL moi bat 19:40 toi qua => probe hom nay la PHEP THU THAT: neu WAL
  co tac dung, so mau bi khoa phai giam manh hoac ve 0.

AGENT SUA CHINH LOI MINH VUA TAO:
2/4 muc mo coi la FU-401 va FU-402 — do chinh agent dat hai nhan MOI chua dang ky
(HANG_DOI_SAU_GOI, MEASURED_ROOT_CAUSE_NOT_FOUND) ngay sau khi vua va dung loai loi do hom 12/08.
Da doi sang nhan DA DANG KY thay vi de them nhan moi:
  FU-401 -> DEFER (nghia "hoan, khong phai xong")
  FU-402 -> MEASURED_BUT_NOT_FIXED
Mo coi 4 -> 2. Hai muc con lai la FU-360/FU-389 — owner ky QD-066 GIU NGUYEN toi 21/08.

CONG: so quyet dinh 0 TROI · §63 DAT · §52 4/4 bo do DAT 6/6.
LANE A/B: cong don 56 cap / 41 bat dong tren 96. Hom qua deepseek chay duoc CA BA MIEN
(MB 5 · MN 4 · MT 5) — noi timeout V11069 co tac dung.
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
git revert aefadf5
```

---

## 9. Theo dõi tiếp

- `FU-375` — tái phạm «commit không có báo cáo công khai», nay đã có cổng chặn (`V11076`)
- Gói **21/08** — 14 mục, xem `docs/FOLLOW_UP_TRACKER.md`

---

TanPhatAI cần làm: ghi nhận `V11072` (2026-08-15) đã có báo cáo công khai **bù ngày 16/08**; lưu ý bản
này **không** viết đương thời, nguồn là commit `aefadf5`.
