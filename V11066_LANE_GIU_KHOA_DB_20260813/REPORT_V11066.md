# REPORT V11066 — V11066 (FU-403): LANE CUA AGENT GIU KHOA DB LAM MAT 2 KET QUA MODEL — da va + deploy

> ## ⚠️ BÁO CÁO BÙ — ghi ngày **2026-08-16**, việc xảy ra ngày **2026-08-13**
>
> Bản này **KHÔNG** được viết tại thời điểm làm việc. Nó được bù ngày 16/08 sau khi đợt đào 49
> tác nhân phát hiện **12 nhãn version trôi 4 ngày không có báo cáo công khai nào** —
> vi phạm `§57.2`, và là **tái phạm** đúng ngày đến hạn xử `FU-375`.
>
> **Nguồn nội dung: chính commit message `b023eca`** — bản ghi THẬT, viết tại thời điểm làm việc.
> Không bịa thêm. Phần nào không có dữ liệu thì ghi thẳng «không áp dụng vì …».
>
> Ranh giới với chế sử (`RM-17`): ngày việc xảy ra và ngày viết báo cáo **được ghi tách bạch**.

**Version:** `V11066` · **ngày việc:** 2026-08-13 · **commit:** `b023eca` · **báo cáo bù:** 2026-08-16

---

## 1. Tóm tắt

V11066 (FU-403): LANE CUA AGENT GIU KHOA DB LAM MAT 2 KET QUA MODEL — da va + deploy

---

## 2. Owner yêu cầu gì (nguyên văn)

Xem `CONVERSATION_CONTEXT_V11066_20260813.md` cùng thư mục. Với các bản thuộc chuỗi
kiểm tra hằng ngày, yêu cầu gốc của owner là *«kiểm tra toàn diện/tổng lực dùm anh»* — lặp lại
mỗi ngày trong giai đoạn 13–16/08.

---

## 3. Đào bới / phát hiện · 4. Hướng xử lý · 5. Đã làm gì

Nguyên văn bản ghi tại thời điểm làm việc (commit `b023eca`):

```
Owner bao 13/08 toi: "cac model AI cua MB co 1 so model cung rong nua do em".

TRUY RA: gemini-3.5-flash va gemini-3.6-flash rong o MB. Va analysis_text chua bang chung THAT:
   SYSTEM_EXCEPTION · error_message: "database is locked"
   Traceback: scheduler.py:7490 -> :7350 -> database.py:2673 save_prediction

BANG CHUNG KHOP TOI GIAY:
   17:51:28  lane A/B cua agent ghi  claude-sonnet-4-6
   17:51:28  official ghi            gemini-3.6-flash  => database is locked
   17:51:29  official ghi            gemini-3.5-flash  => RONG theo

GOC LOI — CUA AGENT, khong phai cua he:
_v11059_lane_ab_3tang.py chi con.commit() MOT LAN sau ca hai vong lap. Lenh INSERT dau tien MO
GIAO DICH GHI, va giao dich do GIU KHOA SQLITE SUOT MOI LENH GOI API PHIA SAU — moi lenh 30-190
giay => lane giu khoa ca DB trong NHIEU PHUT.
PRAGMA busy_timeout=60000 KHONG CUU DUOC: no chi lam ben DOI kien nhan hon, khong rut ngan thoi
gian ben GIU khoa.

DA VA + DEPLOY:
 (1) con.commit() NGAY SAU MOI DONG => khoa giu mili-giay thay vi phut
 (2) doi cron ra ngoai cua so official: MT 16:52 -> 17:15 · MB 17:45 -> 18:05
     (van truoc gio co ket qua => cong nhan qua nguyen ven)

QUET NGUOC §60: 3 materializer khac cua agent goi 0 API => giao dich duoi 1 giay, khong rui ro.
_materialize_ai_region_specialist_provider_shadow_pilot.py co goi API nhung 0 DONG CRON => khong
chay dinh ky. CHI LANE MAC LOI NAY.

NOI SANG FU-402: khoang lang 11 phut cua MT co the CUNG HO (tranh chap khoa DB) — CHUA CHUNG
MINH: lane MT chay 16:52 con khoang lang bat dau 16:42:47, tuc TRUOC lane. Probe cua FU-402 nen
ghi kem trang thai khoa DB.

Ti le rong cua hai model gemini 3.x: 2/38 = 5% moi con trong 14 ngay. Hai model deu la
shadow_auto_eval => KHONG anh huong bach thu MB hom nay. Nhung mat du lieu do tien la that.

Xac minh live: luot 14/08 o khung gio moi.
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
git revert b023eca
```

---

## 9. Theo dõi tiếp

- `FU-375` — tái phạm «commit không có báo cáo công khai», nay đã có cổng chặn (`V11076`)
- Gói **21/08** — 14 mục, xem `docs/FOLLOW_UP_TRACKER.md`

---

TanPhatAI cần làm: ghi nhận `V11066` (2026-08-13) đã có báo cáo công khai **bù ngày 16/08**; lưu ý bản
này **không** viết đương thời, nguồn là commit `b023eca`.
