# V86 — TOTAL FORENSIC REGISTRY + /v82-monitor merged into /monitoring

Ngày: 2026-05-08 00:10 VN
Trạng thái: SHADOW ONLY + UI MERGE — Không touch official.

## 0. TL;DR cho anh

Anh nói đúng — V85 vẫn thiếu. V86 đào sâu thêm:

1. **/monitoring** đã có sẵn `Parallel Shadow Proof` board (V20.3.37.19) — em đã bỏ qua trong V84/V85.
2. **132 API endpoints** trong `main.py` (22 PAGE + 86 PUBLIC_API + 24 ADMIN_API; 90 admin-only).
3. **12 frontend pages** chứ không phải 11 (em đếm sót `viewer.html`).
4. **142 FU items** đã đăng (FU-066 → FU-152 mới).
5. **224 CHANGELOG versions** từ V6.8 → V20.3.37.85 (~9 tháng).
6. **116 phase_checkpoints** trong `artifacts/phase_checkpoints/` qua 14 distinct dates (2026-04-13 → 2026-05-07).
7. **26 AUTOMATION_HISTORY entries** seq=0 → seq=25.

**Em đã làm trong V86**:
- Tạo **`TOTAL_PUBLIC_REGISTRY.md`** (1 bảng duy nhất Notion AI tra cứu, 26 KB).
- **Gộp V82 monitor vào `/monitoring`** thành `sectionV82MasterControl` mới (sau `sectionParallelShadowProof`). Anh không cần nhớ `/v82-monitor` nữa — vào `/monitoring` xem hết.
- `/v82-monitor` standalone vẫn giữ cho ai cần link riêng.
- 6 sub-section embed vào `/monitoring`:
  1. 7-day per-region OFFICIAL/AI herd/NO_TOKEN herd
  2. V82 60d cached summary (PROMOTION_CANDIDATE/DESTRUCTIVE/BASELINE pill)
  3. V79 cluster-weighted (rank=1)
  4. V81 provider pilot per-call (3 model × 3 region)
  5. V67/V70/V73 traces
  6. V80 MB regime + MN V67 save + V77 fast incident

## 1. Inventory tổng V86 (deeper than V85)

| Category | Count | Source |
|---|---|---|
| API endpoints | 132 | parsed from `main.py` |
| Admin-only endpoints | 90 | `require_admin()` proximity |
| ADMIN_API routes | 24 | `/api/admin/...` |
| PUBLIC_API routes | 86 | `/api/...` non-admin |
| PAGE routes | 22 | HTML serving |
| Frontend pages | 12 | `web/frontend/*.html` |
| FU items | 142 | `docs/FOLLOW_UP_TRACKER.md` |
| CHANGELOG versions | 224 | V6.8 → V20.3.37.85 |
| Phase checkpoints | 116 | `artifacts/phase_checkpoints/` |
| AUTOMATION_HISTORY | 26 entries | seq=0 → seq=25 |

## 2. Frontend pages (12) → URLs

| File | URL | Size | Note |
|---|---|---|---|
| index.html | `/` | 21 KB | Home |
| login.html | `/login` | 8 KB | Login |
| du-doan.html | `/du-doan` | 44 KB | **Production prediction (15 model output)** |
| du-doan-test.html | `/du-doan-test` | 63 KB | Admin experimental lane (V52.5+) |
| monitoring.html | `/monitoring` | **162 KB** (V86 +20 KB merge) | **Admin runtime monitoring center** (Parallel Shadow Proof + V82 master control merged) |
| v82-monitor.html | `/v82-monitor` | 18 KB | V83 standalone (V86 also embedded in /monitoring) |
| accuracy.html | `/accuracy` | 19 KB | Accuracy review |
| review-dashboard.html | `/review-dashboard` | 86 KB | Review dashboard |
| search.html | `/search` | 34 KB | Search |
| settings.html | `/settings` | 93 KB | Admin settings |
| user-view.html | `/user-view` | 19 KB | Compact user view |
| viewer.html | `/viewer` | 21 KB | Generic viewer |

## 3. Em đã add 1 section vào `/monitoring`

```html
<div class="section" id="sectionV82MasterControl">
  <div class="section-title">🎛️ V82 Master Control Board — AI vs NO_TOKEN vs V67/V70/V73 vs V79 cluster vs V81 pilot</div>
  ...
  <div id="v82MasterControlContent">...</div>
</div>
```

Đặt **ngay sau `sectionParallelShadowProof`**. Auto-refresh 60s cùng các section khác. Backed by `/api/admin/v82-monitor` (V83 endpoint).

## 4. Hash guard PASS

PRE = POST cho 4 official tables:
- predictions=25d1a3db67d6e406 (4461)
- final_bundles=999d42cbaabea95a (207)
- lottery_results=937407feeb8d8f90 (14628)
- model_daily_eval=07a53a97d1521933 (4412)

## 5. TOTAL_PUBLIC_REGISTRY (cho Notion AI)

1 file `TOTAL_PUBLIC_REGISTRY.md` (26 KB) gồm 10 sections:
1. Statistics tổng
2. 12 frontend pages + URLs
3. 24 ADMIN API endpoints
4. 86 PUBLIC API endpoints
5. 22 PAGE routes
6. 30 FU items mới nhất (top 30 / 142)
7. 30 CHANGELOG versions mới nhất (top 30 / 224)
8. Phase checkpoint files theo date
9. Cross-reference V63 → V86
10. Index links cho Notion AI tra cứu

## 6. Em thấy gì còn thiếu (cho V87+ nếu owner OK)

1. **Settings DB** chưa kê (config keys / values).
2. **Migration history** chưa tracked.
3. **Backup VPS timeline** chưa kê.
4. **Notion docs full inventory** — em chưa kê 20+ pages doctrine.
5. **Per-FU current state full audit** (FU-001 → FU-100 cũ chưa được verify lại).
6. **Per-version regression check** — không phải mọi V đều có hash guard data.
7. **Decision log entries** (`docs/DECISION_LOG.md`) chưa kê.
8. **Governance ledger** (`docs/CHANGELOG_GOVERNANCE_LEDGER.md`) chưa kê.

## 7. Phương án

V86 đã đủ cho mục đích "1 bảng Notion AI tra cứu" và "gộp /v82-monitor vào /monitoring". Anh có thể:
1. Vào `/monitoring` (đăng nhập admin) → cuộn xuống section `V82 Master Control Board` để xem mọi thứ.
2. Tra `TOTAL_PUBLIC_REGISTRY.md` trên Notion để biết file/route nào ở đâu.
3. Nếu cần V87 = settings/migration/notion full → owner OK em làm.

## 8. Official UNTOUCHED ✅

- 4 official tables hash UNCHANGED.
- monitoring.html chỉ thêm 1 section + 1 load function + 2 line vào init/setInterval. KHÔNG đổi scoring/selector/output path.
- /v82-monitor route vẫn còn, không xóa.

## 9. Links sẽ update sau push
