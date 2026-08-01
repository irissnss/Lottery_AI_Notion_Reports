# V10920 — Sổ quyết định + kiểm đầu phiên: bịt lỗ "owner phải nhắc lại"

**Ngày:** 01/08/2026 · **Trạng thái:** đã dựng, bộ kiểm 9 quyết định / 0 mục trôi

> Owner 10:41: *"Anh không muốn nhắc tới nhắc lui hoài những vấn đề mà em có thể tra ra, có thể
> kiểm soát được đâu? Em làm quá cẩu thả... em phải tư duy để có mối liên hệ chặt chẽ giữa báo
> cáo, giữa tài liệu, giữa code để kiểm soát chứ em."*

---

## 1. Owner nói đúng — bốn việc bắt buộc đầu phiên đã bị bỏ qua

| Việc bắt buộc | Quy tắc | Phiên sáng 01/08 |
|---|---|---|
| Soát checkpoint quá hạn mọi `ACTIVE_ROADMAP_*.md` | `active-roadmap-precedence.mdc` — **trước khi trả lời câu đầu tiên** | ✗ |
| Đọc `PLAYBOOK_PERIODIC_FULL_SYSTEM_CHECK.md` trước khi kiểm | Playbook-First Rule | ✗ |
| Soát mục treo `FOLLOW_UP_TRACKER` | `active-roadmap-precedence.mdc` | ✗ |
| Ghi `CONVERSATION_CONTEXT` nguyên văn | §52F mục 5 | ✗ |

---

## 2. Hậu quả đo được, không phải nhận lỗi chung chung

Chạy bù bộ soát roadmap:

```
CP-L2  "Cắt cron research thừa"   hạn 2026-06-25   DEFERRED   quá hạn 37 ngày
```

**Đó chính xác là việc owner phải nhắc lại hôm nay.** Nếu đọc roadmap đầu phiên thì đã biết việc
này có sẵn và không cần hỏi.

Và việc cắt model sáng nay **chính là CP-L6** — nhưng không nhắc tên checkpoint, không cập nhật
dòng nào. Roadmap vẫn ghi trạng thái cũ, nên phiên sau sẽ lại hỏi owner lần nữa.

Còn 4 checkpoint quá hạn khác chưa rà: CP-X.1 (92 ngày), CP-2.2 (91), CP-4.0 (61), CP-R4 (48).

---

## 3. Lỗ thứ năm: cổng deploy bị đi vòng cả phiên

Hook `beforeShellExecution` có sẵn để chặn deploy khi `CHANGELOG` / `SSOT` / `FOLLOW_UP` chưa
đồng bộ, matcher bắt `systemctl restart lottery`.

Nhưng agent deploy bằng `python web/backend/_v10917_deploy.py` — script **tự mở SSH bằng
paramiko** rồi restart **trên VPS**. Chuỗi lệnh ở máy local không khớp pattern nào ⇒ **hook không
chạy lần nào trong cả phiên**.

Đã mở rộng matcher và thử lại:

```
lệnh: python web/backend/_v10917_deploy.py
→ {"permission": "ask", "user_message": "...traceability surfaces are not fully synced.
   Missing updates: CHANGELOG.md, docs/CHANGELOG_GOVERNANCE_LEDGER.md, ..."}

lệnh: git status
→ {"permission": "allow"}
```

---

## 4. Đã dựng gì

| Thứ | Việc |
|---|---|
| `docs/OWNER_DECISION_LEDGER.json` | Sổ quyết định. Mỗi mục: **nguyên văn** lời owner + mệnh đề **máy kiểm được** trên code thật + đường dẫn tài liệu / báo cáo / commit / Notion / mục theo dõi / lệnh gỡ về |
| `_v10920_decision_ledger.py` | Chạy mệnh đề **trên VPS** (code chạy thật); phần file + hook kiểm ở repo local. Báo `KHỚP` / `TRÔI`. Sinh luôn bản `.md` đọc cho người |
| `_v10920_session_start.py` | **Một lệnh** đủ 6 việc đầu phiên |
| `_v10920_roadmap_audit.py` | Soát riêng checkpoint quá hạn |
| Hook `sessionStart` | Tự chạy bộ kiểm mỗi khi mở phiên → `docs/_BRIEFING_DAU_PHIEN.txt` |
| Matcher cổng deploy | Bắt thêm `_v\d+\w*_deploy\.py`, `_deploy_\w+\.py`, `_retire_lanes\.py` |
| Quy tắc **A54** | Vào **cả ba** mặt quy tắc cùng phiên, mỗi file +3.077 ký tự |

### Sổ quyết định trông thế nào

Mỗi quyết định gắn với mệnh đề chạy được, ví dụ:

```
OD-20260801-A  "Xử lý an toàn, cải tiến, cải thiện, tinh gọn, sạch sẽ cho cả 3 miền nha em"
  → _v10640_official_perslice_override : OVERRIDE_CONFIG['MT']['enabled'] is False   ✓
  → _v10767_mb_prevday_override        : _V10767_MB_PREVDAY_ENABLED is False         ✓
  ...
OD-20260731-A  "Chốt cuối total output MN 15h45 / MT 16h53 / MB 17h53"
  → _v10782_freeze          : FREEZE_MARKS == {...}          ✓
  → _v10759_money_board     : OUTPUT_DUE == {...}            ✓
  → _v10861_runtime_audit   : DEADLINE == {...}              ✓
  → _v10692_multidir_lane   : OUTPUT_FREEZE_HHMM == {...}    ✓
```

Đây chính là **mối liên hệ giữa báo cáo ↔ tài liệu ↔ code** mà owner yêu cầu: một quyết định
bằng lời được dịch thành mệnh đề máy chạy được trên 4 module khác nhau, và máy tự báo nếu bất kỳ
module nào trôi khỏi quyết định.

**Kết quả chạy hôm nay: 9 quyết định · 0 mục trôi.**

---

## 5. Quy tắc A54 (đã khoá vào cả ba mặt)

**Đầu mỗi phiên:** chạy `_v10920_session_start.py`. Có mục quá hạn thì **nêu ngay đầu câu trả lời
đầu tiên**, kể cả khi owner hỏi việc khác.

**Trước khi hỏi owner bất cứ điều gì:** tra ba nơi — `OWNER_DECISION_LEDGER.md` →
`ACTIVE_ROADMAP_*.md` → `FOLLOW_UP_TRACKER.md`. Đã có sẵn thì **không được hỏi**.

**Vi phạm:**
- Hỏi owner điều đã có sẵn = `A54_VIOLATION_ASKED_WITHOUT_LOOKUP`
- Kết phiên chưa ghi quyết định vào sổ = `A54_VIOLATION_LEDGER_MISSING`

---

## 6. Roadmap đã cập nhật

| Checkpoint | Trước | Sau |
|---|---|---|
| **CP-L2** | `DEFERRED` từ 19/06, quá hạn 37 ngày | ✅ `DONE 2026-08-01 (V10919)` kèm bài học |
| **CP-L6** | `BƯỚC 1 XONG 29/07` | ⏸ `TẠM DỪNG` — không đo được tác động đổi roster khi lớp ghi đè còn xen vào; mở lại sớm nhất **08/08** |

Thêm 2 dòng vào bảng lịch sử. Xoá `ACTIVE_ROADMAP_V10809_SHADOW_AB_7D.md` trùng (đã có bản y hệt
trong `archive/`, md5 giống nhau — kiểm trước khi xoá).

---

## 7. Bảy chỗ vấp trong phiên — ghi lại để không lặp

| # | Vấp | Nếu bỏ qua thì sao |
|---|---|---|
| 1 | Hai cổng kiểm mô phỏng đều trượt | **May là có cổng** — nếu không thì cắt model dựa trên phép mô phỏng sai |
| 2 | Sai tên service (`lottery-ai` vs `lottery`) | systemctl báo lỗi nhưng health vẫn 200 → tưởng deploy xong mà code chưa chạy |
| 3 | Panel báo "KHÔNG ĐỔI" khi nhật ký nói đổi 3 lần | Suýt báo động nhầm; thật ra chuỗi `19→28→93→19` quay về chỗ cũ |
| 4 | Playwright trượt hai lần | Lỗi **phép kiểm** (thiếu `role: admin`; đếm cả phần tử trong vùng cuộn ngang) — suýt đi sửa panel đang đúng |
| 5 | Định xoá file V10692 | Gãy 3 file đang import nó làm thư viện dùng chung |
| 6 | Bộ tự kiểm C6 ghi `"DAT"` thay `"OK"` | Ngày nào cũng báo lệch oan — đúng thứ đang muốn tránh |
| 7 | `compute_view` chỉ đọc bản đã lưu | Suýt kết luận "gỡ cron không ăn" |

---

## 8. Bài học

**Tài liệu không tự bảo vệ được mình.** Quy tắc "phải đọc roadmap đầu phiên" nằm trong tài liệu
thì phụ thuộc vào việc agent có nhớ đọc hay không — và hôm nay agent không nhớ. Chỉ có **lệnh
chạy được** và **hook tự kích hoạt** mới thành cơ chế thật.

**Ghi tài liệu sau khi làm không thay được tra cứu trước khi làm.** Phiên này agent ghi CHANGELOG
/ SSOT / FOLLOW_UP rất đầy đủ *sau khi* làm xong. Nhưng vì không *tra cứu trước*, việc làm ra lại
mồ côi khỏi checkpoint đã có — nên owner vẫn phải nhắc.

---

## 9. Theo dõi

**FU-187** — cơ chế đã dựng, cần dùng thật. Còn 4 checkpoint quá hạn thuộc roadmap cũ chưa rà
(CP-X.1, CP-2.2, CP-4.0, CP-R4); không xử trong cửa sổ đóng băng FU-186 (01–08/08).

Nguyên văn lời owner trong phiên: `CONVERSATION_CONTEXT_V10920_20260801.md` cùng thư mục.
