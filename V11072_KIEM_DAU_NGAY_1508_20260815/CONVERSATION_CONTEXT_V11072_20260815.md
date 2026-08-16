# CONVERSATION CONTEXT — V11072 · 2026-08-15

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

Nguồn: commit `aefadf5` — bản ghi viết **tại thời điểm làm việc**.

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

## Trạng thái

Bù tài liệu, **không** dựng lại hội thoại đã mất. Những gì không ghi lại được thì **để trống**,
không suy đoán — đúng ranh giới `RM-17`.

TanPhatAI cần làm: xem `REPORT_V11072.md` cùng thư mục.
