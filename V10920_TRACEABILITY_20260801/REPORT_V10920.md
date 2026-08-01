# V10920 — Sổ quyết định + kiểm đầu phiên: bịt lỗ "owner phải nhắc lại"

**Ngày:** 01/08/2026 · **Trạng thái:** đã dựng, bộ kiểm 9 quyết định / 0 mục trôi

> Owner 10:41: *"Anh không muốn nhắc tới nhắc lui hoài những vấn đề mà em có thể tra ra, có thể
> kiểm soát được đâu? Em làm quá cẩu thả... em phải tư duy để có mối liên hệ chặt chẽ giữa báo
> cáo, giữa tài liệu, giữa code để kiểm soát chứ em."*

---

## 1. Tóm tắt

Owner phê bình agent không tra cứu trước khi hỏi. **Owner nói đúng, và có bằng chứng đo được:**
phiên sáng 01/08 bỏ qua 4 việc bắt buộc đầu phiên, hậu quả là **CP-L2 đã nằm trong roadmap từ
25/06** (quá hạn 37 ngày) mà agent vẫn đi hỏi owner lại từ đầu. Phát hiện thêm lỗ thứ năm: cổng
deploy **bị đi vòng cả phiên**.

Đã dựng: sổ quyết định gắn **mệnh đề máy kiểm được** trên code thật (9 quyết định, 0 mục trôi) ·
một lệnh kiểm đầu phiên + hook `sessionStart` tự chạy · mở rộng matcher cổng deploy · quy tắc
**A54** vào cả ba mặt quy tắc.

---

## 2. Owner yêu cầu gì (nguyên văn)

**01/08 10:41:**

> *"Các vấn đề xử lý ghi nhận đào, bới, anh xác nhận, anh chia sẻ, anh chốt và hướng xử lý cũng
> như vướng vấp, nói chung tất cả cần cập nhật, ghi nhận lại đầy đủ chi tiết rõ ràng tránh quên
> lãng nha em. Anh không muốn nhắc tới nhắc lui hoài những vấn đề mà em có thể tra ra, có thể
> kiểm soát được đâu? Em làm quá cẩu thả, em đã tham chiếu với lịch sử, changelog, tài liệu,
> v.v. để nắm rõ và kiểm tra lại, em phải tư duy để có mối liên hệ chặt chẽ giữa báo cáo, giữa
> tài liệu, giữa code để kiểm soát chứ em."*

---

## 3. Đào bới / phát hiện — bốn việc bắt buộc đầu phiên đã bị bỏ qua

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

## 3c. Hướng xử lý và vì sao chọn

| Phương án | Vì sao chọn / loại |
|---|---|
| **Lệnh chạy được + hook tự kích hoạt** | **ĐÃ CHỌN.** Bài học ngay trong phiên: quy tắc nằm trong tài liệu thì phụ thuộc agent có nhớ đọc hay không — hôm nay agent không nhớ |
| Chỉ viết thêm quy tắc vào tài liệu | Loại: quy tắc *"soát roadmap đầu phiên"* đã có sẵn và vẫn bị bỏ qua. Thêm chữ không giải quyết |
| Sổ quyết định chỉ dạng văn bản | Loại: không phát hiện được khi **code trôi khỏi quyết định** — đúng lỗi từng xảy ra (`OUTPUT_DUE` giữ 15:55 nhiều ngày sau khi owner chốt 15:45) |
| Sổ quyết định gắn **mệnh đề máy kiểm được** | **ĐÃ CHỌN.** Một câu owner nói → nhiều mệnh đề chạy trên nhiều module; module nào trôi là máy báo |
| Kiểm mọi mệnh đề trên VPS | Chỉnh lại: mệnh đề về **code chạy** kiểm trên VPS, mệnh đề về **file/hook** kiểm ở repo local — kiểm sai chỗ là báo nhầm |

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

## 6b. Cổng kiểm

| Kiểm | Kết quả |
|---|---|
| Sổ quyết định chạy trên hệ thống thật | **9 quyết định · 0 mục trôi** |
| Hạn FINAL khớp ở bao nhiêu module | **4/4** (`_v10782_freeze`, `_v10759_money_board`, `_v10861_runtime_audit`, `_v10692_multidir_lane`) |
| Cổng deploy chặn đúng lệnh paramiko | ✓ trả `permission: ask` kèm danh sách tài liệu thiếu |
| Cổng deploy vẫn cho qua lệnh vô hại | ✓ `git status` → `allow` |
| Hook `sessionStart` ghi file | ✓ `docs/_BRIEFING_DAU_PHIEN.txt`, 3.572 byte |
| Ba mặt quy tắc có A54 | ✓ cả ba, mỗi file +3.077 ký tự |
| Chạy lại bộ kiểm đầu phiên sau khi sửa | CP-L2 **biến khỏi danh sách quá hạn** · roadmap chưa lưu trữ **0** |

---

## 7. Vướng vấp — bảy chỗ vấp trong phiên, ghi lại để không lặp

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

## 8b. Gỡ về

Phiên này **chỉ thêm** cơ chế kiểm tra, **không đổi đường ra số** và **không đụng database**.
Muốn gỡ:

```
git revert 1d36b0c        # bỏ sổ quyết định + kiểm đầu phiên + A54
```

Hoặc gỡ lẻ: xoá mục `sessionStart` trong `.cursor/hooks.json` (tắt hook đầu phiên) · khôi phục
`DEPLOY_REGEXES` cũ trong `governance_guard.py` (thu hẹp lại matcher). Gỡ về không ảnh hưởng
production — Cursor tự nạp lại `hooks.json` khi lưu.

---

## 9. Theo dõi tiếp

**FU-187** — cơ chế đã dựng, cần dùng thật. Ngưỡng: mỗi phiên phải chạy `_v10920_session_start.py`
và `_v10920_decision_ledger.py`; có mục `TRÔI` là dừng, xử trước khi làm việc mới.

Còn **4 checkpoint quá hạn** thuộc roadmap cũ chưa rà (CP-X.1 92 ngày, CP-2.2 91, CP-4.0 61,
CP-R4 48); **không xử** trong cửa sổ đóng băng FU-186 (01–08/08), rà sau 08/08.

Nguyên văn lời owner trong phiên: `CONVERSATION_CONTEXT_V10920_20260801.md` cùng thư mục.
