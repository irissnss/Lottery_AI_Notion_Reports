# REPORT_V10974 — Đào hết đỏ/vàng + sót transcript (2026-08-02)

**Giờ VN:** 02/08/2026 ~22:50+ · **Phạm vi:** forensic / đo / evidence / FU · **Không đổi path chọn số** · **QD-014 freeze** · **Không ghi Notion**

## 1. Tóm tắt một đoạn

**Hai mục đỏ đã đào xong bằng số; không còn đỏ “chưa đào”.** Bundle MT=13/MB=14 **không** phải timeout/empty/provider — là cổng chất lượng có chủ đích: MT loại `meta-learning` (bt_gate) + `gemini-2.5-pro` (cap Top-13 V10752); MB loại `random-forest` (bt_gate). FU-184 **CLOSED_PASS** (phiếu=công bố 100% MT/MB 01–02/08). FU-189 **CLOSED_FAIL** một phần: doctrine/prompt/DIR nghỉ sạch ở official, nhưng `MB_FULL_POOL_D_W06_V1` + `MB_TOPK10_W04_V2` vẫn ghi 1 dòng test mỗi cái (oe=0). Mọi 🟡 đã có baseline số hôm nay; hành động production vẫn chờ 08/08 theo freeze. Thêm sót transcript: **gemini-3.5-flash** (FU-203) — shadow chạy 3/3 miền hôm nay, BT hit MT+MB.

## 2. Owner yêu cầu gì (nguyên văn)

> *"đỏ vàng gì đào hết, còn thiếu thông tin nào anh đã từng chia sẻ , từng nhắc từng đóng góp trong trò chuyện thì xem lại đào luôn"*

## 3. Đào bới / phát hiện

### 3.1 Hai mục 🔴

| ID | Kết quả đào | Trạng thái mới |
|---|---|---|
| **T18 Bundle MT13/MB14** | Predictions pool 15/15 non-empty cả 3 miền. Thiếu phiếu = quality filter, **không** timeout. MT: `meta-learning` reason=`bt_gate` detail=`bt<14`; `gemini-2.5-pro` reason=`max_voters_cap` detail=`MT_top13_only_V10752_weakest_dropped`. MB: `random-forest` reason=`bt_gate` detail=`bt<12`. day_governance: MT/MB `INCOMPLETE` / `DEGRADED_LIVE_DAY`. | **ĐÃ ĐÀO** · FU-242 cập nhật root-cause · không sửa gate (QD-014) |
| **T26 FU-184/189** | FU-184: ranked[0]==bach_thu **True** cả MT/MB ngày 01/08 và 02/08. FU-189: run_source official chỉ `ai_chain/auto_daily/rerun_post_mt/shadow_auto_eval`; doctrine/prompt/DIR **không** xuất hiện; nhưng FULL_POOL+TOPK MB vẫn ghi test 17:43. | FU-184 **CLOSED_PASS** · FU-189 **CLOSED_FAIL** (dư FULL_POOL/TOPK → FU-185) |

### 3.2 Mọi mục 🟡 — baseline hôm nay

| ID | Kết quả đào 1 dòng | Trạng thái mới |
|---|---|---|
| T03 Freeze QD-014 | Ledger/FREEZE_MARKS khớp; cửa sổ tới 08/08 | OWNER_LOCK (chờ hành động 08/08) · **đã đào** |
| T04 FU-210 MT mất edge | BT tháng: 04=40%→05=38,7%→**06=33,3%**→07=25,8%; chuỗi V10955: RF→vote→công bố −7,59pp | MEASURED · gap: chưa sửa vote/ghi đè (freeze) |
| T05 RF shadow | Baseline V10955b giữ; chưa bật runtime | OWNER_LOCK chờ 08/08 · **đã đào** |
| T06 RULES-FIRST | V10959 list≈12,4% / model≈35,8% — baseline sẵn | OWNER_LOCK shadow sau 08/08 · **đã đào** |
| T07 Prompt A/B | Kế hoạch+chi phí 15–25 USD sẵn; chưa chạy | OWNER_LOCK · **đã đào** |
| T09 WR vs BT | Combo BT; trọng số số còn WR (FU-232) | PARTIAL · hạn 15/08 · **đã đào** |
| T11 FU-225 UI | VPS có `du-doan-test.html`+`app.js`; `/filter`=review-dashboard; no-store đã deploy | **DEPLOYED_PENDING_OWNER_VERIFY** (hard-refresh) |
| T12 FU-207 deploy | `governance_guard.py` có cửa sổ **05:00–06:30** và **15:30–18:15** | Guard **CÓ** · FU-207 nâng v2 vẫn chờ · **đã đào** |
| T16 A55 backlog | Gate sống; FU-188 tồn đọng cũ hạn 10/08 | MEASURED backlog · **đã đào** |
| T19 FU-217 LSTM | VPS `combo_super.py` vẫn đọc `ml_probability`, **không** `lstm_probability` | Bug **còn** · plan sửa sau 08/08 · **đã đào** |
| T20 Optimizer | Job qua `scheduler.py` CN 03:00 (`weight_optimizer_enabled` seed=1); cron shell không có dòng riêng | Còn sống trong scheduler · chờ tắt 22/08 · **đã đào** |
| T21 105 rules | Cần đo causal sau B1; count rules để bàn giao | OWNER_LOCK · **đã đào** |
| T23 FU treo | Session: 83 treo · 0 quá hạn cứng | INTENTIONAL_QUEUE · **đã đào** |
| T25 FU-185 | FULL_POOL/TOPK còn ghi → đúng việc tinh gọn | MEASURED · hạn 03/08 |
| T30 QD-018 B1→B2→B3 | Thứ tự khóa; chưa tới cửa sổ | OWNER_LOCK · **đã đào** |
| Edge gate (T01 liên quan) | 90d: MN −0,38 · MT −2,02 · MB −7,21 pp — **ĐÓNG 3 miền** | Giữ ĐÓNG · **đo lại OK** |

### 3.3 Sót từ transcript (chưa có hàng riêng trong V10973)

| ID mới | Chủ đề owner | Đào hôm nay | Ghi nhận |
|---|---|---|---|
| **T31** | Cứu/giữ `gemini-3.5-flash`, giữ 3.6 | Shadow 02/08 chạy 3 miền non-empty; MDE BT hit MT=1 MB=1 MN=0 | FU-203 · FU-198 |
| **T32** | Live 3/3 nhờ đâu / tốt lên? | V10970: 3/3 = 1/91 ngày 90d ≈ may; voters có gpt-5.4/glm-5.1 | Đã đào V10970 — **không claim edge** |
| **T33** | Cơ chế combo filter auto top | V10936/39 + T09/T10 | Đã ghi nhận |
| **T34** | Repo 240G / máy mới | V10972 đo 254GB; clone nhẹ | FU-241 CLOSED · kế hoạch only |

### 3.4 Root cause bundle (chi tiết)

```
MT 02/08 model_count=13 / scoreable=13 / eligible_rows=15 / incomplete=true
  - meta-learning     bt_gate          bt<14
  - gemini-2.5-pro    max_voters_cap   MT_top13_only_V10752_weakest_dropped

MB 02/08 model_count=14 / scoreable=14 / eligible_rows=15 / incomplete=true
  - random-forest     bt_gate          bt<12

MN 02/08 model_count=15 / incomplete=false / hard_timeout=[] / empty=[]
```

**Không phải** timeout, empty prediction, hay lỗi provider. Predictions đủ 15 model non-empty trước khi cổng lọc.

Evidence: `evidence/exclusion_reasons.json` · `evidence/bundle_model_level.json` · sync `artifacts/live_sync/20260802_224532/manifest.json`.

## 4. Hướng xử lý và vì sao chọn

Chỉ forensic + đóng FU bằng checklist + cập nhật tài liệu. **Không** tắt bt_gate / MT_top13 / LSTM key trước 08/08 (QD-014). Phương án loại: “sửa gate ngay để model_count=15” — phá freeze và làm mất khả năng quy kết tuần yên. FULL_POOL/TOPK còn chạy → ghi vào FU-185 (tinh gọn), không đụng official.

## 5. Đã làm gì

| File / nơi | Thay đổi |
|---|---|
| `web/_sync_live_forensic_inputs.py` | Chạy — local khớp VPS |
| `web/backend/_v10974_*.py` | Script đọc forensic (shadow-only) |
| `Lottery_AI_Notion_Reports/V10974_.../` | REPORT + CONTEXT + evidence/ |
| `docs/FOLLOW_UP_TRACKER.md` | Đóng FU-184/189; cập nhật FU-242/225/217/207 |
| `CHANGELOG.md` / `docs/CURRENT_TRUTH_SSOT.md` | Prepend V10974 |
| Production / VPS runtime | **Không đụng** path chọn số · **không restart** |
| Notion | **Không ghi** |

## 6. Cổng kiểm

| Mục | Kết quả |
|---|---|
| Session start | 0 CP quá hạn |
| Forensic sync | Đạt (`20260802_224532`) |
| Báo cáo 9 phần | Đạt (file này) |
| Report gate V10974 | Chạy sau push |
| Hash 4 bảng | Không áp dụng (không deploy) |
| Notion write | Không gọi |

## 7. Vướng vấp

| # | Vấp | Hậu quả nếu bỏ qua |
|---|---|---|
| 1 | `final_bundles` không có `analysis_json` — phải dùng `source_predictions_json` | Đào sai cột → kết luận timeout ảo |
| 2 | model_count<15 bị tưởng “thiếu prediction” | Sửa nhầm khi thật ra là gate |
| 3 | Query settings `LIKE %optim%` suýt lộ API key vào evidence | Đã REDACT; chỉ ghi metadata |
| 4 | FU-189 expect gồm “model_count không tụt” trong khi MT_top13 **cố ý** 13 | Phải tách: lane nghỉ vs quality gate |

## 8. Gỡ về

Chỉ tài liệu/báo cáo: xóa folder public V10974; revert prepend CHANGELOG/SSOT/FU; không rollback runtime. ~2 phút.

## 9. Theo dõi tiếp

| Mã | Việc | Ngưỡng / hạn |
|---|---|---|
| **FU-242 · KS0805** | Canh incomplete lặp lại im lặng; sau 08/08 xem lại bt_gate/MT_top13 có khớp intent không | Rà 05/08 |
| **FU-185 · DD0803** | Gỡ/xác minh FULL_POOL+TOPK còn ghi | 03/08 |
| **FU-225 · UI0803** | Owner hard-refresh xác minh | 03/08 |
| **FU-215 / QD-014** | Freeze path | hết 08/08 |
| **FU-217** | Sửa key `lstm_probability` sau freeze | 08/08+ |
| **FU-216/226/231 + QD-015/016/017** | Shadow RF / A/B / bỏ ép list | từ 08/08 |
| **FU-233** | Tắt weight optimizer | 22/08 |
| **FU-203** | Canh gemini-3.5 shadow | 08/08 |
