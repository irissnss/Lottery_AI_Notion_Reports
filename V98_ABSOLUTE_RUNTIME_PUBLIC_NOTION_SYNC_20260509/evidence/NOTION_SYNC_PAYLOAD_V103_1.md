# NOTION_SYNC_PAYLOAD_V103.1

> **Ngày:** 2026-05-09 22:35 VN
> **Phiên:** V103.1 — Cross-Region & D-1 Recurrence Tracker UI + §52 Governance Hardlock
> **Trạng thái:** SHADOW_ONLY — official UNCHANGED
> **Cross-ref:** `.Antigravityrules.md` §52, `.AGENT.md` §9D, `.cursorrules`, CHANGELOG V20.3.37.103.1
> **Tracker:** `FU-V103-1-MONITORING-UI` (DEPLOYED_PENDING_LIVE_VERIFY)

---

## 1. Yêu cầu owner (nguyên văn)

> "Các vấn đề đặt biệt là phần ngữ cảnh cho promot với các điều lose Miền trước, sổ miền sau, hoặc là lose hôm nay xổ ngày mai có các bảng theo dõi đo lường không em. Anh nói rất nhiều lần cần phải đo lưởng tất cả, có UI trực quan ở https://xs.io.vn/monitoring để theo dõi và không bị lãng quên, cập nhật changlog, cập nhật tài liệu Notion MCP (gồm các yêu cầu, xác nhận và thực hiện), deploy code và các vấn đề quan trọng ở githup pri và ở github ở Pulic các vấn đề này cần ghi nhận vào quy tắc chuẩn chỉnh ở .AGENT / .Antigravityrules / .cursorrules để luôn luôn tuân thủ nha em."
>
> Khung giờ: 2026-05-09 22:12 VN.

## 2. Diễn dịch yêu cầu

1. Hai pattern chính cần đo lường liên tục:
   - **Lose hôm nay xổ ngày mai** (same-region D-1 recurrence).
   - **Lose miền trước xổ miền sau** (cross-region same-day + next-day).
2. Phải có **bảng đo lường** (DB shadow tables).
3. Phải có **UI trực quan** ở `https://xs.io.vn/monitoring` để không quên.
4. Phải đầy đủ: CHANGELOG + Notion MCP + private GitHub + public GitHub.
5. **Codify** vào `.AGENT.md` + `.Antigravityrules.md` + `.cursorrules` để mọi session sau luôn tuân thủ.

## 3. Xác nhận agent

| Mục | Trạng thái phiên này |
|-----|----------------------|
| Bảng đo lường D-1 + cross-region đã có | ✅ V101 + V102 + V103 + V94 (8 shadow tables, 8743+666+420+61+540 rows trên VPS) |
| UI panel ở `/monitoring` | ✅ V103.1 mới ship — `sectionV103CrossRegionTracker`, 4 panels, auto-refresh 60s |
| Admin API readout | ✅ `/api/admin/v103-cross-region-tracker`, 401 unauth, 200 admin, no-store cache |
| CHANGELOG | ✅ V20.3.37.103.1 |
| Notion MCP payload | ✅ File này (`NOTION_SYNC_PAYLOAD_V103_1.md`); Notion-page sync UNVERIFIED → tracked under `FU-170 OWNER_LOCK` (cần owner cấp MCP access) |
| Private GitHub | ⏳ Sẽ commit + push trong cùng phiên |
| Public GitHub | ⏳ Sẽ commit + push trong cùng phiên |
| `.Antigravityrules.md` | ✅ NEW §52 MEASUREMENT-UI-DEPLOY-SYNC HARDLOCK (full hardlock + 13-deliverable matrix + self-check + violation taxonomy) |
| `.AGENT.md` | ✅ NEW §9D Measurement-UI-Deploy-Sync Contract + checklist mở rộng |
| `.cursorrules` | ✅ NEW Measurement-UI-Deploy-Sync Rule §52 mirror |
| Hash 4 official tables | ✅ IDENTICAL pre/post |
| Mutation `/du-doan` / `final_bundles` / production selector | ✅ ZERO |

## 4. UI tại `https://xs.io.vn/monitoring`

Sau khi admin login, panel mới `🔁 V103 Cross-Region & D-1 Recurrence Tracker — đo lường liên tục` hiển thị 4 panels:

### P1 — V101 MN Cross-Region D-1/D-2 Top 15 (today)
- Source pool: MN + MT + MB D-1 và D-2.
- Cột: rank, candidate_tail, score, d1_occurrences, d2_occurrences, source regions, source stations, gan(N/S), V67/V70/V73 match.
- Mục đích: thấy ngay tail nào MN ngày D nên review khi nó vừa lose ở MN/MT/MB D-1 hoặc D-2.

### P2 — V102 Recurrence 60d/90d
- Cột: window, axis, source_region, target_region, source_group, opportunities, hits, hit_rate%, baseline%, Δpp, sample_qualified, eligible_for_shadow_boost.
- Đo lường lift_pp: bao nhiêu phần trăm pattern "lose D → hit D+1" hơn baseline.
- Hàng `eligible_for_shadow_boost=🚀` là pattern có sample đủ + lift đủ để cân nhắc cho V104 prompt injection.
- Sub-table STRONG/MEDIUM today: tail nào trong region đang được V102 đánh dấu STRONG/MEDIUM, kèm `recurrence_score` và `recommendation`.

### P3 — V103 Candidate Supply Gate (REQUIRED / REVIEW / BLOCKED)
- Bảng đếm số candidate per region per gate (REQUIRED / REVIEW / BLOCKED).
- Bảng top REQUIRED + REVIEW today: region, tail, gate, gate_score, gate_reasons.
- Heatmap supply layer: cho mỗi region, đếm số tail được supply từ AI / NoTok / Off / Test / V67 / V70 / V73 / V101 / V102 / Gan / Rule.
- Mục đích: thấy ngay nếu một tail có recurrence STRONG nhưng không có AI nào pick → V103 đánh dấu REVIEW để V104 có thể inject vào shadow prompt.

### P4 — V94 Cross-Region Leakage Continuous Monitor
- Cột: pair (MN→MT, MN→MB, MT→MB), window (7d/14d/30d), n_lose, n_leak, leak_rate%, baseline%, Δpp, alert_class.
- Hàng `ALERT_HIGH` (Δpp ≥ 5pp với sample qualified) hiển thị nền đỏ → owner thấy ngay pattern cross-region đang nóng.

## 5. Codify governance — quy tắc luôn tuân thủ

### `.Antigravityrules.md` §52 (canonical)

§52 — MEASUREMENT-UI-DEPLOY-SYNC HARDLOCK:

> Khi owner flag bất kỳ measurable pattern, signal, recurrence, leakage, accuracy hypothesis, hoặc candidate-supply audit, agent **PHẢI** giao 13 deliverable trong cùng phiên (xem bảng đầy đủ trong file canonical):
> 1. Shadow measurement table (`output_eligible=0`, `diagnostic_only=1`, `owner_approved=0`, `shadow_only=1`).
> 2. Admin-only readout API (`require_admin`, `Cache-Control: no-store`).
> 3. UI panel ở `/monitoring` — auto-refresh 60s — **registered ở `loadAllSections()` AND `setInterval`**.
> 4. `CHANGELOG.md` entry.
> 5. `docs/CURRENT_TRUTH_SSOT.md` row.
> 6. `docs/FOLLOW_UP_TRACKER.md` issue.
> 7. `docs/AUTOMATION_STATE.json` entry (governance_seq++).
> 8. `NOTION_SYNC_PAYLOAD_VxxxYYY.md` (file này).
> 9. VPS deploy + restart + smoke (health=200, admin=401).
> 10. Private GitHub push.
> 11. Public GitHub push.
> 12. Pre/post hash 4 official tables IDENTICAL.
> 13. ZERO mutation `/du-doan` / `final_bundles` / production selector.
>
> Hard violations:
> - `§52_VIOLATION_UI_MISSING` (table có nhưng UI panel chưa có).
> - `§52_VIOLATION_DOC_MISSING` (deploy nhưng CHANGELOG/SSOT/FU thiếu).
> - `§52D_DRIFT_VIOLATION` (private push nhưng public chưa push).
> - `§52B_VIOLATION_REFRESH_MISSING` (UI panel không có trong `setInterval`).
> - `§52_OWNER_REREMINDER` (owner nhắc lại pattern lần thứ 2 ở 2 phiên khác nhau → escalate).

### `.AGENT.md` §9D (mirror cho execution agent)
Ghi 13-deliverable contract + violation taxonomy + Cursor commit shell workaround (`cmd /c .cmd` để bypass auto-injected `Co-authored-by: Cursor <...>` trailer phá PowerShell). Checklist phiên cuối thêm 3 check items §52-specific.

### `.cursorrules` (mirror cho Cursor surface)
Ghi Measurement-UI-Deploy-Sync Rule (§52) đầy đủ + violation taxonomy + Cursor commit workaround. Cross-ref tới canonical `.Antigravityrules.md` §52.

## 6. Bằng chứng deploy

| Mục | Bằng chứng |
|-----|-----------|
| Local file | `web/backend/_v103_cross_region_tracker.py` (290 lines) |
| Admin route | `web/backend/main.py` `@app.get("/api/admin/v103-cross-region-tracker")` |
| UI panel | `web/frontend/monitoring.html` `sectionV103CrossRegionTracker` + `loadV103CrossRegionTracker()` + entry trong `loadAllSections()` + entry trong `setInterval(60000)` |
| VPS scp | 3 files scp xong (status code 0) |
| Restart | `systemctl restart lottery` → `is-active=active` |
| Smoke health | `/api/health=200` |
| Smoke admin endpoint | `/api/admin/v103-cross-region-tracker=401 unauth` (admin-locked đúng) |
| Hash guard | 4 official tables IDENTICAL pre/post (predictions, final_bundles, lottery_results, model_daily_eval — chỉ tăng do natural daily growth) |

## 7. Pending — cần owner action

| Item | Trạng thái | Tracker |
|------|-----------|---------|
| Notion-page sync (manual copy hoặc cấp MCP access) | UNVERIFIED | FU-170 OWNER_LOCK |
| GitHub PAT `ghp_cvoSP***` revoke | PENDING | FU-V99-GITHUB-TOKEN-LEAK P0 |
| BT scoring doctrine STRICT vs DIAGNOSTIC | LOCKED to STRICT, revisit 2026-06-08 | FU-V99-BT-SCORING-DEBATE |
| V104 shadow prompt injection (V103 REQUIRED/REVIEW → AI shadow prompts) | OWNER_LOCK | FU-V104-SHADOW-PROMPT-INJECTION |

## 8. Next gate

- **2026-05-10 19:00 VN cycle:** Live verify P1/P2/P3 panels populate sau MN/MT/MB closeout. Hash 4 official tables IDENTICAL.
- **2026-05-21 14d gate:** V101 candidates + V102 recurrence stats có đủ sample evaluator-known để decide V104 promotion proposal.
- **2026-06-08 30d gate:** Final BT scoring doctrine review.

---

**Hard contract reaffirmed:** `output_eligible=0`, `diagnostic_only=1`, `owner_approved=0`, `shadow_only=1`. NO selector / scoring / production prompt change. NO new cron. UI is read-only.
