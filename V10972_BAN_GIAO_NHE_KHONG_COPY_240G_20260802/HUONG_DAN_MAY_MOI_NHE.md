# HƯỚNG DẪN MÁY MỚI NHẸ — V10972 (02/08/2026)

> Copy-paste cho owner. **Không** copy nguyên `E:\Lottery_AI_Test` (~254 GB).

## Vì sao không copy 240G?

Gần như toàn bộ dung lượng là **bản sao forensic cũ**, không phải source code:

| Chỗ | ~GB | Phân loại | Mang sang máy mới? |
|---|---:|---|---|
| `artifacts/live_sync/` (547 snapshot DB) | **241** | B runtime | **KHÔNG** — sync lại từ VPS khi cần |
| `backups/` (2 file tar.gz VPS 4/2026 + .pre) | **9.7** | C backup | **KHÔNG** trừ khi chủ động restore |
| `data/` (`lottery_ai.db` + .bak) | **1.7** | B runtime | **KHÔNG** — sync từ VPS |
| Code + docs git-tracked | **~0.09** | A source | **CÓ** qua `git clone` |
| `.git` pack private | **~0.1** | A | Đi kèm clone |
| Public reports | **~0.04** | D | Clone repo reports |
| `.env` | **<1 KB** | E secrets | Copy **thủ công** riêng |

**Máy mới ước tính:** ~150–250 MB (2 repo clone sạch) · thêm ~0.6–1 GB nếu chạy một lần sync forensic từ VPS.

---

## 7 bước trên máy mới

### 1) Cài Git + Python 3.11+ + Cursor

- Git for Windows, Python (PATH), Cursor.
- SSH key GitHub gắn quyền private repo `irissnss/Lottery_AI_Test`.

### 2) Clone repo riêng (code + docs)

```powershell
cd E:\
git clone git@github.com:irissnss/Lottery_AI_Test.git
cd E:\Lottery_AI_Test
```

(HTTPS cũng được nếu đã login `gh` / credential.)

### 3) Clone repo báo cáo công khai

```powershell
cd E:\
git clone git@github.com:irissnss/Lottery_AI_Notion_Reports.git
```

### 4) Secrets — copy thủ công (USB / 1Password)

Từ máy cũ, **chỉ** copy các file secrets (ví dụ):

- `E:\Lottery_AI_Test\.env` → cùng path trên máy mới
- Nếu có credential SSH VPS / key API ngoài `.env` — cũng thủ công

**CẤM:** commit `.env` · đẩy lên public reports · paste API key vào chat/report.

Tham chiếu cấu trúc (không phải secret): `.env.example` trong repo.

### 5) Đọc bàn giao nội dung (V10971) + quy tắc

```text
docs/BAN_GIAO_MAY_MOI_V10971.md
docs/BAN_GIAO_NHE_KHONG_COPY_240G_V10972.md   (mirror hướng dẫn này)
CLAUDE.md  /  docs/OWNER_DECISION_LEDGER.md  /  docs/CURRENT_TRUTH_SSOT.md
docs/FOLLOW_UP_TRACKER.md
Public: V10971_BAN_GIAO_MAY_MOI_20_NGAY_20260802/
Public: V10972_BAN_GIAO_NHE_KHONG_COPY_240G_20260802/
```

Cursor rules đã nằm trong repo (`.cursorrules`, `.cursor/rules/`, `CLAUDE.md`, `AGENTS.md`).

### 6) Kiểm đầu phiên

```powershell
cd E:\Lottery_AI_Test
python web/backend/_v10920_session_start.py
```

### 7) Khi cần audit / accuracy trên máy mới

```powershell
python web/_sync_live_forensic_inputs.py
```

- Kéo `lottery_ai.db` + `prediction_trace.jsonl` từ **VPS** (không mang 241 GB `live_sync` cũ).
- Khi trích dẫn bằng chứng local: cite `artifacts/live_sync/latest_manifest.json`.
- Deploy / fix vẫn SSH lên VPS từ máy mới — **không** cần `backups/` local.

---

## Danh sách KHÔNG copy

- `artifacts/` (đặc biệt `live_sync/`)
- `backups/` (tar.gz, `*_pre/`, `prod_frontend_*`)
- `data/*.db`, `data/*.bak`, `web/backend/prediction_trace.jsonl`, logs
- `venv` / `.venv` / `__pycache__` / `node_modules` (tạo lại khi cần)
- Copy nguyên cả folder `.git` từ máy cũ nếu nghi corrupt — **clone fresh tốt hơn**

## Cảnh báo cứng

1. **Đừng** copy `backups/` / `data/` trừ khi owner **chủ động** restore từ bản local.
2. Nguồn sự thật runtime = **VPS**, không phải DB local cũ.
3. Tới hết **08/08**: freeze QD-014 — không đổi roster / combo-super / override / mở tiền.
4. Ưu tiên máy mới: **FU-225 · UI0803 · hạn 03/08** (verify UI).

## Ước kích thước sau setup

| Thành phần | Ước lượng |
|---|---:|
| `Lottery_AI_Test` clone (pack ~95 MiB + tree ~87 MB) | ~150–200 MB |
| `Lottery_AI_Notion_Reports` clone | ~50 MB |
| `.env` | <1 KB |
| **Tổng không sync** | **~200–250 MB** |
| + 1 lần `_sync_live_forensic_inputs.py` (DB ~600 MB + jsonl ~20 MB) | **~0.9–1.1 GB** |

So với máy cũ ~**254 GB** → giảm **>99%**.
