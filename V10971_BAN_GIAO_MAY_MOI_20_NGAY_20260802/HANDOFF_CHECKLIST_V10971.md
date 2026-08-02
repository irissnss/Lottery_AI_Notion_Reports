# HANDOFF_CHECKLIST_V10971 — Máy local mới (02/08/2026)

> Mục đích: agent/owner mở máy mới, làm đúng thứ tự → code/fix liền mạch, không rơi quyết định / FU / freeze.

**Repo riêng:** `https://github.com/irissnss/Lottery_AI_Test`  
**Repo công khai:** `https://github.com/irissnss/Lottery_AI_Notion_Reports`  
**Báo cáo gốc gói này:** [REPORT_V10971.md](./REPORT_V10971.md) · [INDEX_QUYET_DINH_FU_V10971.md](./INDEX_QUYET_DINH_FU_V10971.md)

---

## 0. Trước khi làm gì khác

- [ ] Đồng hồ máy = **giờ Việt Nam** (`Asia/Ho_Chi_Minh`) khi đọc tài liệu / báo cáo.
- [ ] Không mở Notion để lấy trạng thái hiện tại (Notion đứng đông từ 01/08 — §57). SSOT = `docs/CURRENT_TRUTH_SSOT.md` + VPS.

---

## 1. Clone / pull hai repo

```text
git clone https://github.com/irissnss/Lottery_AI_Test.git
git clone https://github.com/irissnss/Lottery_AI_Notion_Reports.git
# hoặc trên máy đã có:
cd Lottery_AI_Test && git pull
cd Lottery_AI_Notion_Reports && git pull
```

- [ ] Workspace trỏ đúng thư mục code riêng.
- [ ] Public reports nằm cạnh (path quen: `E:/Lottery_AI_Notion_Reports` hoặc tương đương).

---

## 2. Đọc theo thứ tự (không nhảy)

1. [ ] `CLAUDE.md` (hoặc `.cursorrules`) — §56 tra cứu · §57 báo cáo public · §58 mã đọc
2. [ ] `docs/OWNER_DECISION_LEDGER.md` (+ `.json` nếu cần `kiem_code`)
3. [ ] `docs/CURRENT_TRUTH_SSOT.md` (đầu file = sự thật mới nhất)
4. [ ] `docs/FOLLOW_UP_TRACKER.md` (đầu file = FU mới; **đừng** đọc bản cũ dưới đáy)
5. [ ] `docs/TONG_HOP_TOAN_PHIEN_V10970.md` + `docs/BAN_GIAO_MAY_MOI_V10971.md`
6. [ ] Public: `V10970_…/REPORT_V10970.md` rồi `V10971_…/REPORT_V10971.md`
7. [ ] `docs/PLAYBOOK_PERIODIC_FULL_SYSTEM_CHECK.md` (§1 timetable · §5 calendar)
8. [ ] `docs/CO_CHE_HOC_VA_XEP_HANG.md`
9. [ ] `docs/DE_XUAT_QUY_UOC_MA_CONG_VIEC.md` (APPROVED_B)

---

## 3. Đầu mỗi phiên — bắt buộc

```bash
python web/backend/_v10920_session_start.py
# đọc docs/_BRIEFING_DAU_PHIEN.txt
python web/backend/_v10920_decision_ledger.py   # có TRÔI thì dừng
```

- [ ] Nêu checkpoint / FU quá hạn **đầu câu trả lời đầu tiên** nếu briefing báo.

---

## 4. Audit / accuracy dùng bản local

```bash
python web/_sync_live_forensic_inputs.py
```

- [ ] DB + `prediction_trace.jsonl` là **một cặp**.
- [ ] Cite `artifacts/live_sync/latest_manifest.json`.
- [ ] Size-mismatch → **không** lấy local làm SSOT; query VPS.

---

## 5. Secrets / `.env`

- [ ] Lấy từ máy cũ hoặc quy trình VPS đã có — **không** commit `.env` / key.
- [ ] **Không** in secret vào REPORT / evidence / conversation context.
- [ ] Push public từng bị chặn vì base64 key trong probe (V10969) — quét trước push.

---

## 6. VPS / deploy

| Mục | Giá trị |
|---|---|
| Service | **`lottery`** (không `lottery-ai`) |
| Health | `GET /api/health` → 200 |
| So PID | **bắt buộc** trước/sau restart |
| FINAL | MN **15:45** · MT **16:58** · MB **17:58** |
| Biên lane | MN 15:43 · MT 16:56 · MB 17:56 (+2 phút → FINAL) |
| Cấm deploy giờ nóng | khung ~05:00–06:30 và ~15:30–18:15 (V10968); thoát `DEPLOY_KHAN=1` + log |
| Matcher deploy | `_v\d+\w*_deploy\.py`, `_deploy_\w+\.py`, `_retire_lanes\.py` phải nằm trong hook |

- [ ] Không deploy runtime artifact (`*.db`, `*.jsonl`, `*.log`, `*.bak`).
- [ ] Hash 4 bảng khoá pre/post khi đụng runtime: `predictions` · `final_bundles` · `lottery_results` · `model_daily_eval`.

---

## 7. Notion

- [ ] **CHỈ ĐỌC** — cấm mọi API ghi (§57 / A55.1).
- [ ] Không ghi `notion_pages[]` mới vào `AUTOMATION_STATE`.

---

## 8. Kết phiên code/fix/audit

1. [ ] CHANGELOG + SSOT + FOLLOW_UP (qua `_doc_prepend.prepend()` — **cấm** `open(w)+read`)
2. [ ] Ledger nếu owner quyết gì mới
3. [ ] Push private `Lottery_AI_Test`
4. [ ] Folder public `<VERSION>_…/` đủ `REPORT_` + `CONVERSATION_CONTEXT_` (+ evidence)
5. [ ] Push public
6. [ ] `python web/backend/_v10921_report_gate.py <VERSION>` → PASS

---

## 9. Đừng đụng tới hết 08/08 (QD-014 / FU-215 · DB0808)

**CẤM đổi đường tạo số công bố:**

- [ ] Danh sách **15** model `OUTPUT_ELIGIBLE` (pool hiện tại gồm `gpt-5.4`, `glm-5.1`, `gpt-oss-120b`; **không** `combo-no-token` trong total)
- [ ] Hằng số / logic bộ lọc **combo-super**
- [ ] Bật/tắt thêm lớp ghi đè bạch thủ (override toggles)
- [ ] Đưa shadow vào official / cắt model vì một ngày đẹp
- [ ] Claim edge / mở tiền vì 3/3 ngày 02/08

**ĐƯỢC làm trong freeze:**

- [ ] Tech fix rõ ràng (journal, UI neo ngày, deploy guard, tooling FU reader…)
- [ ] Đo shadow / chỉ-đọc / docs / báo cáo A55
- [ ] Owner verify UI **FU-225 · UI0803 · hạn 03/08**

---

## 10. Ưu tiên ngày đầu trên máy mới

1. [ ] Chạy session_start + đọc briefing
2. [ ] Xác nhận freeze còn hiệu lực tới **08/08**
3. [ ] **FU-225** — owner verify `/du-doan-test` 3 miền + `/filter` (hạn 03/08)
4. [ ] Không mở tiền — edge gate ĐÓNG (QD-013)
5. [ ] Nếu audit: sync forensic hoặc VPS; không tin DB local lệch
6. [ ] Đọc kế hoạch sau 08/08: QD-015 → rồi QD-018 B1→B2→B3 (không song song)

---

## 11. Năm bước tối thiểu khi “chỉ cần chạy lại”

1. Pull 2 repo  
2. `python web/backend/_v10920_session_start.py`  
3. Đọc đầu SSOT + đầu FOLLOW_UP + ledger QD-013…019  
4. Xác nhận QD-014 freeze còn  
5. Làm đúng 1 việc ưu tiên (thường FU-225 hoặc docs/đo) — không đụng roster  

---

## 12. Link nhanh production (không secret)

| Việc | URL |
|---|---|
| Official | https://xs.io.vn/du-doan |
| Chơi / vốn | https://xs.io.vn/choi |
| Monitoring (admin) | https://xs.io.vn/monitoring |

**Tiền thật:** dừng tới khi cổng lợi thế mở (≥ **+3,0pp** và **z ≥ 2,0** trên 90 ngày) — QD-013.
