# REPORT V11069b — V11069b: dong bo du lieu song — hai phep troi QD-046/QD-056 la do DU LIEU LOCAL CU

> ## ⚠️ BÁO CÁO BÙ — ghi ngày **2026-08-16**, việc xảy ra ngày **2026-08-14**
>
> Bản này **KHÔNG** được viết tại thời điểm làm việc. Nó được bù ngày 16/08 sau khi đợt đào 49
> tác nhân phát hiện **12 nhãn version trôi 4 ngày không có báo cáo công khai nào** —
> vi phạm `§57.2`, và là **tái phạm** đúng ngày đến hạn xử `FU-375`.
>
> **Nguồn nội dung: chính commit message `e9edf54`** — bản ghi THẬT, viết tại thời điểm làm việc.
> Không bịa thêm. Phần nào không có dữ liệu thì ghi thẳng «không áp dụng vì …».
>
> Ranh giới với chế sử (`RM-17`): ngày việc xảy ra và ngày viết báo cáo **được ghi tách bạch**.

**Version:** `V11069b` · **ngày việc:** 2026-08-14 · **commit:** `e9edf54` · **báo cáo bù:** 2026-08-16

---

## 1. Tóm tắt

V11069b: dong bo du lieu song — hai phep troi QD-046/QD-056 la do DU LIEU LOCAL CU

---

## 2. Owner yêu cầu gì (nguyên văn)

Xem `CONVERSATION_CONTEXT_V11069b_20260814.md` cùng thư mục. Với các bản thuộc chuỗi
kiểm tra hằng ngày, yêu cầu gốc của owner là *«kiểm tra toàn diện/tổng lực dùm anh»* — lặp lại
mỗi ngày trong giai đoạn 13–16/08.

---

## 3. Đào bới / phát hiện · 4. Hướng xử lý · 5. Đã làm gì

Nguyên văn bản ghi tại thời điểm làm việc (commit `e9edf54`):

```
Kiem san sang truoc live 14/08. So quyet dinh bao 2 phep troi:
  QD-046 'Khong con dong RONG nao mang nhan LOSE' -> exit 1: '1 model rot san — MAT UNG VIEN'
  QD-056 'Bo do D-2 chay duoc'                    -> exit 1: 'RM-01: du lieu cu hon 6 gio'

CA HAI LA MOT GOC: du lieu local cu hon 6 gio nen cong RM-01 TU CHOI CHAY — tuc cong lam DUNG
viec, khong phai he hong. Sau khi chay web/_sync_live_forensic_inputs.py:
  NO_ANSWER_V11036=DAT · dong RONG mang nhan LOSE: 0 (tong rong 145, da gan NO_ANSWER 145)
  model rot san vi loai luot rong: 0
=> KHONG co ung vien nao bi mat, pool combo-super nguyen ven.

Bai hoc ghi lai: 'phep troi' trong so quyet dinh co the la TRIEU CHUNG CUA DU LIEU CU chu khong
phai code troi. Truoc khi di sua code, dong bo du lieu roi chay lai — dung thu tu nay de khong
duoi theo mot loi khong ton tai.

Xac minh ban tren VPS dung ban vua sua: TIMEOUT_THEO_MIEN {MN:420, MT:300, MB:300} va commit
trong vong lap o dong 565 — ban va FU-403 CO tren VPS.
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
git revert e9edf54
```

---

## 9. Theo dõi tiếp

- `FU-375` — tái phạm «commit không có báo cáo công khai», nay đã có cổng chặn (`V11076`)
- Gói **21/08** — 14 mục, xem `docs/FOLLOW_UP_TRACKER.md`

---

TanPhatAI cần làm: ghi nhận `V11069b` (2026-08-14) đã có báo cáo công khai **bù ngày 16/08**; lưu ý bản
này **không** viết đương thời, nguồn là commit `e9edf54`.

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
git log --all --grep=V11069B --format='%h %cI %s'      # commit thuộc bản này
git show <hash> --stat                              # tệp đã đổi + số dòng
```

Kho riêng: `github.com/irissnss/Lottery_AI_Test`. Bằng chứng runtime (PID, hash, mã HTTP) nằm
trong thân báo cáo phía trên nếu phiên đó có đo.

### `DOC_SAID`

- `CHANGELOG.md` — mục `## V11069B`
- `docs/CURRENT_TRUTH_SSOT.md` — mục `### V11069B`
- `docs/AUTOMATION_HISTORY.jsonl` — dòng `version=V11069B` *(từ `V11062` trở đi)*

### Ba lớp lệch nhau

Không đối chiếu được vì lớp `OWNER_SAID` khuyết — **đó chính là finding**, và nó đã được ghi: sổ tương tác ra đời muộn hơn bản này 9–12 ngày.

---

TanPhatAI cần làm: đọc mục ba lớp bù ở trên. Lớp `OWNER_SAID` của bản này **không tái lập được** — sổ tương tác owner chỉ có từ **25/08**; **đừng đi tìm** và **đừng coi khoảng trống đó là mâu thuẫn**.
