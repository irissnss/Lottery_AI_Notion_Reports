# V10843 — BÁO CÁO CUỐI NGÀY 24/07/2026: TỔNG LỰC 3 MIỀN × 4 LUỒNG HÔM NAY + 15 NGÀY

- Phiên: 24/07/2026 22:49 → 23:3x (giờ VN), sau khi hết chu kỳ live trong ngày.
- Nguồn dữ liệu: sync paired DB + prediction_trace `artifacts/live_sync/20260724_225123` (khớp VPS tại 22:51, sau M2s 20:50 + rule-cond 21:00).
- Phạm vi: kết quả hôm nay 3 miền × 4 luồng; 15 ngày 10→24/07; deep-dive AE theo nguồn, catalog điều kiện, đề/GĐB; an toàn hạ tầng; 1 fix tool cùng phiên; đề xuất an toàn.

## 1. HÔM NAY 24/07 — 4 LUỒNG × 3 MIỀN

### 1.1 Kết quả tổng quan theo miền

| Miền | Official /du-doan | /choi (money board) | M2s + lanes (V2/V3) | Rule-cond 📐 + V67 AE |
|---|---|---|---|---|
| MN | BT **08✓** · lo2 [08,54] **2/2✓** (WIN) | [08] ✓ (BT1_OFFICIAL) | m1/m2 = 08✓ · m4 3/4 · laneV2 [08,17]✓ · laneV3 [08,17]✓ | B=08✓ · (AE không chạy MN by design) |
| MT | BT 60✗ · lo2 [60,96] 0/2 (LOSE) | [54,60] ✗ | m2 [60,54] any=0 · m4 1/4✓ · laneV2 ✗ · laneV3 [60]✗ | B=60✗ · V67: 91✓ (rank-2/4) |
| MB | BT **17✓** · lo2 [17,75] 1/2 (PARTIAL) | [60] ✗ (AE) | m1/m2 = 17✓ · m4 1/4 · laneV2 [17,75]✓ · laneV3 [17,60]✓ | B=17✓ · V67: 74✓ (rank-6/7) |

### 1.2 Ba câu chuyện của ngày

1. **MN quét sạch 4 luồng** — official + /choi + M2s/lanes + rule-cond đều trúng 08 (bundle chốt 04:17, /choi khoá 11:59). Per-model **15/15 any-hit** — ngày đầu tiên trong cửa sổ 15d đạt tuyệt đối. Đáng chú ý: laneV3 MN chạy nhánh `fallback_m1_a_empty` (rules tier không nổ: n_rules_tier_ok=0) nhưng fallback M1-sạch-herd vẫn cho [08,17] ✓ — thiết kế fallback sau fix V10840 hoạt động đúng và có ích.
2. **MB đúng hướng, trừ /choi** — 4/5 surface trúng 17. Riêng /choi dùng lane AE khoá [60] → trượt. Chi tiết mục 3.1.
3. **MT trắng theo cụm** — toàn bộ surface (official, /choi, M2s, laneV2/V3, rule-cond) cùng hội tụ cụm 60/54 và cùng trượt; kết quả về 58/35 mà chỉ 5/15 model chạm (combo-no-token, gpt-5-mini, meta-learning, random-forest, smart-ml). Đây là rủi ro cấu trúc "đồng thuận sai": khi tầng tổng hợp đồng thuận cao nhưng sai, mọi luồng chết cùng nhau. Hướng xử lý đã chốt từ V10829: catalog điều kiện (không vá ad-hoc giữa cửa sổ đo).

### 1.3 V67 AE trace hôm nay

- MB 7 ứng viên (23:40 hôm trước + intraday): 32(2.18) 28(2.16) 22(1.11) 92(1.10) 60(1.07) 74(1.06) 46(1.05) — chỉ **74✓** (rank-6). Số được /choi khoá là 60 (rank-5) vì 60 qua vote-gate (có phiếu canon hôm nay), nguồn `cross_region_sameday` (60 = BT chính MT cùng ngày).
- MT 4 ứng viên: 96(1.09) 91(1.06) 75(1.06) 07(1.05) — **91✓** (rank-2).

## 2. 15 NGÀY 10→24/07 — THEO LUỒNG

### 2.1 Official /du-doan (bundle cuối/ngày, BT về-lô + any)

| Miền | BT | any (BT∪lo2) | Chuỗi ngày (B=BT✓, a=chỉ any✓, .=trắng) |
|---|---|---|---|
| MN | 6/15 | 8/15 | 10B 11a 12. 13. 14a 15. 16B 17. 18. 19B 20. 21B 22B 23. 24B |
| MT | 5/15 | 8/15 | 10a 11B 12B 13. 14. 15. 16. 17. 18a 19a 20B 21. 22B 23B 24. |
| MB | **2/15** | 7/15 | 10a 11. 12a 13B 14. 15a 16. 17. 18. 19. 20. 21a 22a 23. 24B |

### 2.2 /choi money board

| Miền | Kết quả | Ghi chú |
|---|---|---|
| MN | 6/13 | Nghỉ 11+18/07 = **Thứ 7, đúng lock tuần owner V10781 E5** (không phải lỗi). Mai 25/07 (T7) cũng sẽ nghỉ. |
| MT | **10/15** | Mạnh nhất hệ. Method xoay: AE (10–12) → HYBRID+STRENGTH (13–19) → PRIOR_REGION+STRENGTH (20–24). |
| MB | 4/13 · **0/4 gần nhất** (19,20,21,24) | Thiếu 22–23/07 vì AE gate không có pick đủ điều kiện (đúng thiết kế V10828, owner đã chấp nhận tạm). |

### 2.3 Tầng tổng hợp TOTAL-V2 (M2s shadow, 19→24/07, 6 ngày)

| Miền | m2_bt | m2_any | m4 dàn-4 any | official_bt cùng kỳ |
|---|---|---|---|---|
| MN | 4/6 | **6/6** | **6/6** | 4/6 |
| MT | 4/6 | 5/6 | **6/6** | 3/6 |
| MB | 3/6 | 5/6 | 4/6 | **1/6** |

**M2 (tầng tổng hợp có điều kiện) thắng official BT ở cả 3 miền trong 6 ngày forward.** Lane thật ghi bảng test: laneV2 BT MN 4/6 · MB 3/6 · MT 2/6; laneV3 (từ 22/07) MN 2/3 · MB 2/3 · MT 1/2.

### 2.4 Rule-cond V10829 (từ 21/07 forward, trước đó backfill)

- Forward 4 ngày (21→24/07): B_bt 6/12 = M0 official 6/12 — chưa tách bạch, mẫu quá nhỏ; giữ ngưỡng quyết định 04–11/08 như FU-V10829.
- Backfill 60 ngày: B_bt 26/60 (43.3%) — tham khảo, không dùng để promote.
- **Phát hiện mới: selector thoái hoá** — 72/72 ngày (60 backfill + 12 forward) đều chọn đúng một tổ hợp H-A4a∧H-B2a. Catalog hiện không phân hoá điều kiện theo ngày/miền → cần mở rộng chiều điều kiện hoặc rút cửa sổ trailing (đề xuất mục 4).

### 2.5 Per-model 15 ngày (any-hit, official rows)

| Hạng | Model | any 15d |
|---|---|---|
| 1= | claude-opus-4-6 · meta-learning · xgboost | 62.2% (28/45) |
| 4= | claude-sonnet-4-6 · gpt-5.4 | 60.0% |
| 6= | deepseek-reasoner · gemini-2.5-pro · smart-ensemble | 57.8% |
| 9 | gemini-2.5-flash | 55.6% |
| 10= | combo-super · gpt-5-mini · smart-ml | 51.1% |
| 13= | combo-no-token · lstm · random-forest | 48.9% |

Theo miền × nhóm: MN ML 75% > LLM 70% · MT ML 56% ≈ LLM 54% · **MB LLM 49% >> ML 31%** — ML yếu hẳn tại MB, khớp quan sát owner "MB rules có mà model mốc ố"; LLM tại MB cũng chỉ 49%.

### 2.6 Đề (GĐB) — kiểm chứng doctrine

- Đề nằm trong rules_union: MN 3/15 · MT 3/15 · MB 0/15. Đề-hit của bundle official: 1/45. Model đề-hit tốt nhất: lstm 3/45.
- Kết luận: hệ đang đúng doctrine "BT = về lô"; đề không phải target và không có tín hiệu đề nào bị bỏ sót đáng kể.

### 2.7 Sức khoẻ roster (empty output 15d, tất cả shadow-side)

- gemma-4-31b 11/45 (Google quota 429; hôm nay lại 429 ở MT+MB shadow) · qwen3-max-thinking 7/45 (toàn pre-revert; post-revert 1/21=4.8% PASS đã đóng sáng nay) · kimi-k2.5, grok-4.20, gpt-5.5, glm-5.2, gemini-3.5-flash mỗi model 1/45.
- Official 15 model: 0 empty hôm nay. Toàn bộ nhóm trên đưa vào lean/shadow agenda 28/07.

## 3. DEEP-DIVE MỚI TRONG PHIÊN

### 3.1 AE V67 theo NGUỒN ứng viên (30 ngày, per-candidate về-lô)

| Miền | Nguồn | Hit | % |
|---|---|---|---|
| MT | same_region_lag1_final_bundle | 12/22 | **54.5%** |
| MT | per_model_lag1 | 61/136 | 44.9% |
| MT | lo2_lag1_final_bundle | 6/14 | 42.9% |
| MT | cross_region_nextday | 5/12 | 41.7% |
| MT | cross_region_sameday | 2/8 | 25.0% |
| MB | per_model_lag1 | 43/164 | 26.2% |
| MB | cross_region_sameday | 7/30 | 23.3% |
| MB | cross_region_nextday | 0/2 | 0.0% |

- Baseline ngẫu nhiên ~25% (MB 25 tails/100 số; MT ~27-30%). **MT có edge thật** (same_region_lag1 +27pp so baseline). **MB không nguồn nào vượt baseline** → /choi MB đang tựa lên luồng không có lợi thế → giải thích 4/13 và 0/4 gần nhất.
- Case hôm nay: AE-MB khoá 60 từ nguồn cross_region_sameday (60 = MT-BT cùng ngày, qua được vote-gate vì có model MB cũng đoán 60) → trượt cả MT lẫn MB. Lịch sử reuse MT-BT→MB /choi 15d: 3/4 hit (16✓ 64✓ 31✓ 60✗) — mẫu nhỏ, ghi nhận trung thực 2 chiều, không kết luận vội.

### 3.2 V10841 live-verify (one-shot, read-only) — cache contract ĐÃ CHỨNG MINH LIVE

- PRE 20:49: v10821_rows hôm nay = 0, cache chỉ `base`, dispersion đọc DB đã thấy đủ 3 miền.
- POST 20:55: v10821_rows = **3** (M2s 20:50 vừa ghi), dispersion_has_today 3/3 miền, `_DISP_CACHE` vẫn chỉ `base`, **PID không đổi** (không restart) → panel nhặt dữ liệu mới ≤5 phút không cần restart. Đây chính là hành vi mà fix cache V10841 cam kết.
- Còn phase BOUNDARY 04:30 sáng 25/07 (cửa UTC≠VN) → đọc xong sẽ gỡ 3 cron one-shot.

### 3.3 Fix tool cùng phiên (diagnostic-only, zero official)

- **Triệu chứng:** probe cuối ngày import `_v10841_contract_check` → `ValueError: I/O operation on closed file` ngay tại print.
- **Root cause:** file này còn wrap `sys.stdout` ở **module-level**; khi được import bởi script đã wrap stdout, wrapper cũ mất tham chiếu → GC đóng buffer chung. Đúng lớp lỗi V10831 đã fix ở rule-cond (V10841) — lần này chính công cụ kiểm tra contract vi phạm contract của mình.
- **Fix:** chỉ wrap khi chạy CLI (`__main__` + `sys.stdout is sys.__stdout__`). Verify: chạy CLI PASS + import-từ-probe PASS (probe chạy trọn). Deploy VPS (file đã có từ sáng): compile OK, chạy PASS `pool {MN:15,MT:15,MB:15} canon 15/15/15`.
- **An toàn:** hash 4 bảng official pre=post **IDENTICAL** (`predictions 10847/5adf2f7c · final_bundles 441/74b1705d · lottery_results 15140/95bf835b · model_daily_eval 10711/c2f1589e`); health 200, admin anon 401, service active, không restart.

## 4. ĐỀ XUẤT AN TOÀN (chưa đổi gì — chờ owner)

1. **MB /choi:** cho phép đo shadow 7 ngày "what-if /choi MB dùng picks laneV2/V3 thay AE" (AE không edge theo nguồn; laneV2 MB BT 3/6 vs /choi MB 0/4 cùng kỳ). Ngưỡng viết sẵn: what-if − AE ≥ +15pp bền ≥7 ngày mới trình promote 1 quyết định. (FU-V10843-AE-MB-SOURCE-EDGE)
2. **Catalog V10829:** mở rộng chiều điều kiện (weekday-bucket, vote-depth) hoặc rút cửa sổ trailing của selector để hết thoái hoá 1-tổ-hợp; vẫn shadow-only, không đụng ngưỡng 04–11/08 đã chốt.
3. **Panel AE:** thêm readout per-source (dữ liệu đã có sẵn trong `contributions_json` — chỉ hiển thị, không đổi gate) để theo dõi hằng ngày nguồn nào cấp số.
4. **MT cụm 60/54:** không vá phản xạ; case này là đúng loại dữ liệu mà catalog điều kiện V10829 cần học (khi nào tin đồng thuận, khi nào né).

## 5. NHẮC LỊCH

- **CP-S3** (đóng addendum per-số): owner không phản đối trước **25/07** → CP-S4 gỡ 4 cron V10809 ngày 26/07.
- Sáng 25/07: đọc boundary 04:30 → gỡ 3 cron one-shot V10842; MN /choi nghỉ Thứ 7 theo lock (không phải lỗi).
- 28/07: lean/shadow agenda (gemma quota, glm/gemini-3.5 watch) + skim rule-cond forward + đọc FU-V10843.

## 6. GOVERNANCE

- CHANGELOG V10843 · SSOT block V10843 · FU-tracker: FU-V10843-AE-MB-SOURCE-EDGE (mới) + FU-V10842 (2/3 PASS) + FU-V10829 (ghi chú degeneracy) · AUTOMATION_STATE seq 304 + HISTORY appended.
- Backup pre-edit: `backups/v10843_pre/_v10841_contract_check.py.pre`.
- Files phiên: `_v10843_eod_probe.py` · `_v10843_followup_sniff.py` · `_v10843_deep_analysis.py` · `_v10843_schema_sniff.py` · `_v10843_vps_evening.py` · `_v10843_deploy.py` · `_v10843_state_update.py` + fix `_v10841_contract_check.py`.
