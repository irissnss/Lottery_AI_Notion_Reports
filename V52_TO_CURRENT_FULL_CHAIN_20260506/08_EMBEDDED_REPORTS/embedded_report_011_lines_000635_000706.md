| Tier-aware misnamed | LOW | dùng tên cẩn thận khi báo cáo; refactor future |
| Specialist roster placeholder | LOW | chấp nhận null cho ngày không đủ specialist; UI hiển thị "no_specialist_vote" |
| Daily runner thiếu hash guard | MEDIUM | trước khi auto-wire phải bổ sung |
| AI prompt designed-only | LOW | rõ ràng documented, không claim đang chạy |
| Persisted scoreboard chỉ 1 ngày | HIGH | không base decision trên 1 ngày; gate yêu cầu 14+ ngày |

---

## 30. Rollback plan

Nếu có sự cố:
1. Xóa các route `/du-doan-test`, `/api/du-doan-test/mb` trong main.py.
2. `DROP TABLE du_doan_test_*` (tất cả 6 bảng).
3. Xóa `mb_experimental_preview_shadow` (1 bảng).
4. Xóa file engine/runner/materializer trong `web/backend/`.
5. Frontend: xóa `du-doan-test.html` và link `duDoanTestLink` trong `du-doan.html`.
6. Restart `lottery.service`.
7. Verify `/du-doan` 200, source hashes identical.

`final_bundles`, `predictions`, `lottery_results`, `model_daily_eval`, scoring, voting, lane weights, prompt, model roster đều **không bị tác động** → rollback chỉ cần 5 phút.

---

## 31. Docs / tracker / changelog sync

Sẽ cập nhật ngay phần tiếp theo của session:
- `CHANGELOG.md` → V20.3.37.48.2 (TOTAL-FORCE START-OF-LIVE pass)
- `docs/CURRENT_TRUTH_SSOT.md` → row mới
- `docs/FOLLOW_UP_TRACKER.md` → 9 FU mới
- `docs/CHANGELOG_GOVERNANCE_LEDGER.md` → governance entry
- `docs/ACTIVE_ROADMAP_CROSS_REGION_LEAKAGE.md` → reference link

---

## 32. Technical no-drop audit

| Item | Drop? |
|---|---|
| VPS sync done | ✓ NO |
| Pre-hash captured (5+6+6 tables) | ✓ NO |
| Post-hash captured | ✓ NO |
| 12/12 hash IDENTICAL verified | ✓ NO |
| 7 experiment evaluated | ✓ NO |
| 91 independence explained | ✓ NO |
| 25-model corrected (14 voter) | ✓ NO |
| AI prompt status corrected (DESIGNED_ONLY) | ✓ NO |
| Live parallel classified MANUAL | ✓ NO |
| Schema gap audit | ✓ NO |
| Lane separation 13-row matrix | ✓ NO |
| UI matrix 20-item | ✓ NO |
| Today timeline | ✓ NO |
| Risk register | ✓ NO |
| Rollback plan | ✓ NO |

---

## 33. Governance no-overclaim audit

| Statement | OK? |
|---|---|
| "Đã có route + UI + schema" | ✓ |
| "Đã chạy auto live song song" | **❌** không claim — pass classified MANUAL |
| "Đã 25 model thực sự realtime test" | **❌** không claim — corrected 14/25 |
| "Đã chạy AI test prompt" | **❌** không claim — DESIGNED_ONLY |
| "Composite challenger 8/30 BT wins là live evidence" | **❌** không claim — clarified hardcoded backtest |
| "7 experiment fully independent pipelines" | **❌** không claim — SHARED_SOURCE_VARIANT |
| "Tier-aware tính tier thật" | **❌** không claim — misnamed transform |
| "Source hash 4/4 unchanged" | ✓ verified for 4 tables that should not change; predictions/final_bundles changed naturally and correctly attributed to live activity not test code |
| "Output mutation = false" | ✓ verified |
| "/du-doan unaffected" | ✓ verified |

→ Pass đạt yêu cầu **VERIFY-BEFORE-CLAIM** + **NO PASS-WASH**.
