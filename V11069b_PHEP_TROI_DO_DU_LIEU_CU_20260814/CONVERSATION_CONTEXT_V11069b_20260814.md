# CONVERSATION CONTEXT — V11069b · 2026-08-14

> **BẢN BÙ.** Viết ngày **2026-08-16**, việc xảy ra ngày **2026-08-14**.

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

## Nội dung phiên 2026-08-14

Nguồn: commit `e9edf54` — bản ghi viết **tại thời điểm làm việc**.

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

## Trạng thái

Bù tài liệu, **không** dựng lại hội thoại đã mất. Những gì không ghi lại được thì **để trống**,
không suy đoán — đúng ranh giới `RM-17`.

TanPhatAI cần làm: xem `REPORT_V11069b.md` cùng thư mục.
