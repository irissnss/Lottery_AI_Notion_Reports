# REPORT V11070 — V11070: kiem tong luc 14/08 — 3/3 bach thu, hai su co hom qua KHONG tai dien, probe da tra loi

> ## ⚠️ BÁO CÁO BÙ — ghi ngày **2026-08-16**, việc xảy ra ngày **2026-08-14**
>
> Bản này **KHÔNG** được viết tại thời điểm làm việc. Nó được bù ngày 16/08 sau khi đợt đào 49
> tác nhân phát hiện **12 nhãn version trôi 4 ngày không có báo cáo công khai nào** —
> vi phạm `§57.2`, và là **tái phạm** đúng ngày đến hạn xử `FU-375`.
>
> **Nguồn nội dung: chính commit message `fef2c35`** — bản ghi THẬT, viết tại thời điểm làm việc.
> Không bịa thêm. Phần nào không có dữ liệu thì ghi thẳng «không áp dụng vì …».
>
> Ranh giới với chế sử (`RM-17`): ngày việc xảy ra và ngày viết báo cáo **được ghi tách bạch**.

**Version:** `V11070` · **ngày việc:** 2026-08-14 · **commit:** `fef2c35` · **báo cáo bù:** 2026-08-16

---

## 1. Tóm tắt

V11070: kiem tong luc 14/08 — 3/3 bach thu, hai su co hom qua KHONG tai dien, probe da tra loi

> **ĐÍNH CHÍNH 01/09/2026 (`V11145`) — `PRJ-SELECTION-WINDOW-001`.**
> Câu «3/3 bạch thủ» ở trên là kết cục của **đúng một ngày** (14/08), so với nền của **chính
> ngày đó** — **KHÔNG** phải tuyên bố hiệu quả theo cửa sổ trên thước `TW-001`. Đây là chỗ nói
> rõ: **cố ý chỉ trích một ngày**, không phải đủ bộ cửa sổ.
>
> Theo `RM-04`, `n = 3` là **«chưa được phép kết luận»**, không phải «hiệu quả cao».
>
> **Đủ bộ cửa sổ của thước này nằm ở `V11084` và `V11086`** — và chúng đo được **dấu đổi theo
> cửa sổ**: `30 ngày +4,07pp` · `90 ngày −3,18pp` · `180 ngày +0,91pp`, `CI95 [−3,2 → +5,0]`.
> **CẤM trích** riêng cửa sổ 30 ngày làm căn cứ — đó là chọn cửa sổ cho khớp kết quả.


---

## 2. Owner yêu cầu gì (nguyên văn)

Xem `CONVERSATION_CONTEXT_V11070_20260814.md` cùng thư mục. Với các bản thuộc chuỗi
kiểm tra hằng ngày, yêu cầu gốc của owner là *«kiểm tra toàn diện/tổng lực dùm anh»* — lặp lại
mỗi ngày trong giai đoạn 13–16/08.

---

## 3. Đào bới / phát hiện · 4. Hướng xử lý · 5. Đã làm gì

Nguyên văn bản ghi tại thời điểm làm việc (commit `fef2c35`):

```
KET QUA 14/08: 3/3 (MN 41 · MT 69 · MB 36). Nen dung 0,95/3; xac suat ca ba trung do ngau nhien
0,41x0,29x0,25 = 2,97% = 1 ngay trong 34. RM-04: n=3 CAM KET LUAN.

HAI SU CO HOM QUA KHONG TAI DIEN:
  MT bien han: 1 PHUT (13/08) -> 12 PHUT (14/08)
  model rong : 2 model (13/08) -> 0 model ca ba mien
  database is locked trong journal: 0 dong
=> ban va FU-403 (commit tung dong + doi cron) co tac dung.

PROBE FU-402 DA TRA LOI (1.077 mau, 16:35-18:05):
  21 mau thay DB BI KHOA = 2%
  cac dot khoa NGAN: 5-15 giay moi dot (16:37:42-57 · 16:41:43-53 · 16:48 · 16:50 · 17:30:36-46)
  => KHOA CO THAT NHUNG NGAN, KHONG giai thich duoc khoang lang 11 phut hom qua
  => hom nay KHONG co khoang lang nao => probe CHUA GAP LAI dieu kien hom qua
  => VAN CHUA KET LUAN duoc nguyen nhan FU-402. Probe chay tiep.

PHAT HIEN KEM, DANG GIA: wal=0 o MOI mau. Kiem ra:
  journal_mode = DELETE (khong phai WAL) · synchronous = 2 (FULL) · DB 707 MB
Trong che do DELETE, MOI LENH GHI KHOA EXCLUSIVE TOAN BO TEP — nguoi doc cung bi chan.
Day la NEN cua moi vu "database is locked". WAL cho phep doc song song voi ghi.
=> DE XUAT OWNER (chua tu lam vi cham DB production).

LANE: noi timeout an ngay. deepseek-reasoner GHI DUOC o MT (240s) va MB (140s) — truoc day
timeout 120s bao dam truot. MT/MB nay 5 cap thay vi 4. deepseek tu 3 cap len 5.
Cong don 52 cap / 38 bat dong / 96 => du nguong ~20-21/08.

FU-400 CAP NHAT (them 3 ngay, n 437 -> 443):
  A-B: -2,75pp -> -2,26pp · CI95 [-6,28..+0,79] -> [-5,80..+1,28] · z -1,456 -> -1,082
  Ngay 14/08 di NGUOC xu huong: trong so CUU 2/3 (MN hang #3, MB hang #2).
  Cua so 30 ngay DA DOI DAU: +5,56pp (z=+0,97), nhung 60/90/120/toan bo VAN AM.
  DOC DUNG: CI nay trum 0 RONG HON => BANG CHUNG YEU DI, khong manh len.
  Tran "trong so giup" noi tu +0,79pp len +1,28pp. VAN CHUA DUOC PHEP KET LUAN.
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
git revert fef2c35
```

---

## 9. Theo dõi tiếp

- `FU-375` — tái phạm «commit không có báo cáo công khai», nay đã có cổng chặn (`V11076`)
- Gói **21/08** — 14 mục, xem `docs/FOLLOW_UP_TRACKER.md`

---

TanPhatAI cần làm: ghi nhận `V11070` (2026-08-14) đã có báo cáo công khai **bù ngày 16/08**; lưu ý bản
này **không** viết đương thời, nguồn là commit `fef2c35`.

---

## Nguồn ba lớp (§62 · A60) — **bù ngày 01/09/2026** *(`V11145`)*

> Mục này **thiếu từ lúc phát hành** và cổng `_v10921_report_gate.py` bắt được. Bù bằng nguồn
> **tái lập được**, và **nói thẳng lớp nào không tái lập được** thay vì viết cho đủ chỗ.

### `OWNER_SAID`

**KHÔNG TÁI LẬP ĐƯỢC — và đây là lý do, không phải chỗ bỏ trống.**

Bản này ra ngày **13–16/08/2026**. Sổ `docs/SO_TUONG_TAC_OWNER.md` chỉ ra đời **25/08** cùng
`PRJ-INTERACTION-LEDGER-001`. Lời owner trong phiên đó **không được ghi lại ở đâu**, nên nay
không có nguồn nào tái lập.

**Cố tình KHÔNG bịa.** Viết ra một câu «owner yêu cầu…» nghe hợp lý để cổng xanh là **chế dữ
liệu** — đúng thứ `RM-17` cấm, và đúng lý do §63 đã **từ chối** bù 286 dòng `HISTORY` suy từ tiêu
đề. Ghi thẳng là thiếu, kèm lý do, thì người đọc sau biết **đừng đi tìm**.

### `CODE_DID`

Tái lập được bằng máy, không cần trí nhớ:

```bash
git log --all --grep=V11070 --format='%h %cI %s'      # commit thuộc bản này
git show <hash> --stat                              # tệp đã đổi + số dòng
```

Kho riêng: `github.com/irissnss/Lottery_AI_Test`. Bằng chứng runtime (PID, hash, mã HTTP) nằm
trong thân báo cáo phía trên nếu phiên đó có đo.

### `DOC_SAID`

- `CHANGELOG.md` — mục `## V11070`
- `docs/CURRENT_TRUTH_SSOT.md` — mục `### V11070`
- `docs/AUTOMATION_HISTORY.jsonl` — dòng `version=V11070` *(từ `V11062` trở đi)*

### Ba lớp lệch nhau

Không đối chiếu được vì lớp `OWNER_SAID` khuyết — **đó chính là finding**, và nó đã được ghi: sổ tương tác ra đời muộn hơn bản này 9–12 ngày.

---

TanPhatAI cần làm: đọc mục ba lớp bù ở trên. Lớp `OWNER_SAID` của bản này **không tái lập được** — sổ tương tác owner chỉ có từ **25/08**; **đừng đi tìm** và **đừng coi khoảng trống đó là mâu thuẫn**.
