# REPORT V11075 — V11075 (FU-404): nhan "HR12W 1.0" bom vao prompt NOI QUA gia tri that — va agent da tra loi SAI

> ## ⚠️ BÁO CÁO BÙ — ghi ngày **2026-08-16**, việc xảy ra ngày **2026-08-16**
>
> Bản này **KHÔNG** được viết tại thời điểm làm việc. Nó được bù ngày 16/08 sau khi đợt đào 49
> tác nhân phát hiện **12 nhãn version trôi 4 ngày không có báo cáo công khai nào** —
> vi phạm `§57.2`, và là **tái phạm** đúng ngày đến hạn xử `FU-375`.
>
> **Nguồn nội dung: chính commit message `61ee931`** — bản ghi THẬT, viết tại thời điểm làm việc.
> Không bịa thêm. Phần nào không có dữ liệu thì ghi thẳng «không áp dụng vì …».
>
> Ranh giới với chế sử (`RM-17`): ngày việc xảy ra và ngày viết báo cáo **được ghi tách bạch**.

**Version:** `V11075` · **ngày việc:** 2026-08-16 · **commit:** `61ee931` · **báo cáo bù:** 2026-08-16

---

## 1. Tóm tắt

V11075 (FU-404): nhan "HR12W 1.0" bom vao prompt NOI QUA gia tri that — va agent da tra loi SAI

---

## 2. Owner yêu cầu gì (nguyên văn)

Xem `CONVERSATION_CONTEXT_V11075_20260816.md` cùng thư mục. Với các bản thuộc chuỗi
kiểm tra hằng ngày, yêu cầu gốc của owner là *«kiểm tra toàn diện/tổng lực dùm anh»* — lặp lại
mỗi ngày trong giai đoạn 13–16/08.

---

## 3. Đào bới / phát hiện · 4. Hướng xử lý · 5. Đã làm gì

Nguyên văn bản ghi tại thời điểm làm việc (commit `61ee931`):

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
git revert 61ee931
```

---

## 9. Theo dõi tiếp

- `FU-375` — tái phạm «commit không có báo cáo công khai», nay đã có cổng chặn (`V11076`)
- Gói **21/08** — 14 mục, xem `docs/FOLLOW_UP_TRACKER.md`

---

TanPhatAI cần làm: ghi nhận `V11075` (2026-08-16) đã có báo cáo công khai **bù ngày 16/08**; lưu ý bản
này **không** viết đương thời, nguồn là commit `61ee931`.

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
git log --all --grep=V11075 --format='%h %cI %s'      # commit thuộc bản này
git show <hash> --stat                              # tệp đã đổi + số dòng
```

Kho riêng: `github.com/irissnss/Lottery_AI_Test`. Bằng chứng runtime (PID, hash, mã HTTP) nằm
trong thân báo cáo phía trên nếu phiên đó có đo.

### `DOC_SAID`

- `CHANGELOG.md` — mục `## V11075`
- `docs/CURRENT_TRUTH_SSOT.md` — mục `### V11075`
- `docs/AUTOMATION_HISTORY.jsonl` — dòng `version=V11075` *(từ `V11062` trở đi)*

### Ba lớp lệch nhau

Không đối chiếu được vì lớp `OWNER_SAID` khuyết — **đó chính là finding**, và nó đã được ghi: sổ tương tác ra đời muộn hơn bản này 9–12 ngày.

---

TanPhatAI cần làm: đọc mục ba lớp bù ở trên. Lớp `OWNER_SAID` của bản này **không tái lập được** — sổ tương tác owner chỉ có từ **25/08**; **đừng đi tìm** và **đừng coi khoảng trống đó là mâu thuẫn**.
