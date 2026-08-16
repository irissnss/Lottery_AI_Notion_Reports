# CONVERSATION CONTEXT — V11066 · 2026-08-13

> **BẢN BÙ.** Viết ngày **2026-08-16**, việc xảy ra ngày **2026-08-13**.

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

## Nội dung phiên 2026-08-13

Nguồn: commit `b023eca` — bản ghi viết **tại thời điểm làm việc**.

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

## Trạng thái

Bù tài liệu, **không** dựng lại hội thoại đã mất. Những gì không ghi lại được thì **để trống**,
không suy đoán — đúng ranh giới `RM-17`.

TanPhatAI cần làm: xem `REPORT_V11066.md` cùng thư mục.
