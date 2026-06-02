# V10679 — Cơ chế Rules CHUYÊN cho Miền Bắc (SUPERSEDED by V10680)

> **SUPERSEDED / ĐỌC V10680 TRƯỚC**: Báo cáo này chứa phần R3 từng đề xuất `MB XIÊN candidate aggregator`. Sau phản biện của owner, phần aggregator đã bị rollback vì UI official đã có xiên 2/3 trong `generate_final_bundle`.  
> **Bản đúng mới nhất**: [V10680_MB_RULE_STACK_CLARIFICATION_AND_NEXT_STEPS_VN.md](./V10680_MB_RULE_STACK_CLARIFICATION_AND_NEXT_STEPS_VN.md).  
> **Giữ lại từ V10679**: 3 tầng MB rule-stack, T2 cap 8, T2 mở rộng V10636-DIG/LAGS, lifecycle rule.  
> **Bỏ / không dùng**: aggregator xiên riêng.

# Nội dung lịch sử V10679 (để audit lineage)

> **Generated**: 2026-06-03 00:30 VN — bản R3 (xiên-friendly) | **Trạng thái**: code + verify xong tại local, CHỜ owner OK deploy VPS

## R3 highlights (mới so với R2)

- **Bỏ cap display 4 → cap 8** (Tier 2 trong context pack); thêm cảnh báo coverage `<3 rule/weekday`.
- **Mở rộng Tier 2** đọc thêm V10636-DIG (MB self-lag D-1) + V10636-LAGS (MB lag D-2/D-3): 73 → **77** rule sau dedup. Mỗi rule gắn `source_artifact` để truy.
- **Phát hiện**: 19 pre-register **KHÔNG hoàn toàn ⊂ 73** thủ công (chỉ 5/19 axis overlap) → giữ 3 tầng độc lập.
- **MB XIÊN candidate aggregator** mới (`mb_xien_aggregator.py`): hợp nhất tail Tier 1 → score = boost × lifecycle_weight + T2-confirm bonus → top-K đuôi cho xiên 2/3/4 + cảnh báo coverage.
- **Owner ưu tiên xiên**: prompt MB hiện hiển thị "MB XIÊN CANDIDATE SET" với top 6 đuôi unique kèm support count, T2-confirm count, lifecycle dominant.

## Coverage XIÊN MB theo từng thứ (verify thực tế)

| Ngày | Thứ | Đuôi unique | Xiên 2 | Xiên 3 | Xiên 4 |
|---|---|---:|:---:|:---:|:---:|
| 2026-06-01 | wd0 (T2) | 3 | OK | OK | ⚠️ (G6+G7 compact) |
| 2026-06-02 | wd1 (T3) | 9 | OK | OK | OK |
| 2026-06-03 | wd2 (T4) | 5 | OK | OK | OK |

(Ngày tương lai cho 0 tail = đúng production: nguồn MN/MT(D) chưa xổ; tại 17:42 lúc predict thật, KQ đã có → tail sinh đủ.)


> **Phạm vi**: CHỈ rules **đích = MB**. MN/MT đóng băng tuyệt đối, đã chứng minh 108/108 chữ ký IDENTICAL bằng before/after swap test.
> **Tài liệu nền**: [V10676 Grand Master](V10676_GRAND_MASTER_ALL_RULES_VN.md), [Index](V10667_RULES_INDEX.md), [MB target rules](V10667_RULES_MB_TARGET.md)

---

## 0. Đếm chính xác MB-target trong từng nhóm (đã verify trên DB live)

| Nhóm gốc | Tổng | **Lọc MB-target** | Ghi chú |
|---|---:|---:|---|
| 105 production (`mined_rules`) | 105 | **35** | đã có sẵn trong DB |
| "183 thủ công" (V10675 labeled) | 183 | **1** | 183 là pool cross-region, target chủ yếu MT=134 / MN=48 / MB=1 |
| **Soi cầu thủ công đích=MB** (V10667 per-target MB) | 73 | **73** | đây mới là bộ MB-target thật sự (5 BH-pass, 17 p<.05) |
| 63 pre-register (V10626 panel + FU4) | 63 | **19** | 15 panel MB + 4 FU4 MB |

→ Em dùng **35 + 73 + 19** làm 3 tầng MB-target. (Không dùng "183" vì lọc MB chỉ còn 1, sai khái niệm.)

---

## 1. Ba cơ chế daily — đặt tên chính xác

| ID cơ chế | Tên đầy đủ | Nguồn | Drive số? | Bảng |
|---|---|---|---|---|
| **MB-T1-DYN8W** | MB Tier-1 Dynamic Cumulative Re-rank (8W) | 35 MB production | ✅ CÓ (qua score) | `mined_rules_mb_daily` |
| **MB-T2-SOI** | MB Tier-2 Manual Soi-Cau Daily Re-rank | 73 MB manual (V10667) | ❌ confirm-only | `mb_t2_manual_daily` |
| **MB-T3-WATCH** | MB Tier-3 Pre-Register Watch Tracker | 19 MB pre-register | ❌ watch-only | `mb_t3_prereg_daily` |

Cả 3 đều **xếp hạng lại mỗi ngày** (cron 20:30 sau MRE + guard 17:00 trước AI MB 17:42).

---

## 2. Đa yếu tố trong cơ chế học tích lũy

Mỗi rule được chấm điểm bằng tổ hợp **nhiều yếu tố** (không chỉ một con số):

| Yếu tố | Tier 1 | Tier 2 | Tier 3 |
|---|:---:|:---:|:---:|
| Window hit-rate 4W/8W/12W/16W (nhấn 8W) | ✓ tính lại từ MRE | — | — |
| Lift / hit-rate vs baseline (sức mạnh) | ✓ | ✓ | ✓ |
| Significance (p-value / BH-pass) | ✓ qua lift-ratio + strong-hit | ✓ trực tiếp | — |
| Half-split stability (ổn định) | ✓ split-half MRE | — | ✓ `half_stable` |
| Recency 4W + decay guard | ✓ | — | — |
| Confidence (sample size) | ✓ | ✓ days_evaluated | — |
| Temporal validity (MN/MT(D) ✓ vào MB) | ✓ | ✓ | ✓ |

**Công thức composite (rút gọn):**
- `MB-T1-DYN8W`: `0.40·hr8 + 0.30·hr12 + 0.20·hr16 + 0.10·hr4` (×100) × confidence × **weight-mult vòng đời** + bonus significance.
- `MB-T2-SOI`: `0.45·strength + 0.35·significance + 0.20·confidence` (×100).
- `MB-T3-WATCH`: `0.5·strength + 0.5·half_stable` (×100).

---

## 3. Vòng đời rule + kế hoạch xử lý (mạnh / yếu / tăng / giảm)

Mọi rule trong cả 3 tầng đều được gán **một** trong 5 nhãn + kế hoạch xử lý cụ thể:

| Nhãn | Điều kiện | Kế hoạch xử lý | weight-mult Tier1 |
|---|---|---|:---:|
| **MANH** | composite ≥ 75 + significant | FULL_WEIGHT (giữ nguyên) | ×1.00 |
| **TANG_TRUONG** | trend Δ ≥ +8pp (nửa mới − nửa cũ) | PROMOTE_CANDIDATE (ưu tiên) | ×1.05 |
| **ON_DINH** | còn lại, không decay | KEEP | ×1.00 |
| **XUONG_CAP** | trend Δ ≤ −8pp HOẶC hr_4w ≤ hr_16w − 15pp | REDUCE_FLAG_DEMOTE (hạ + cảnh báo) | ×0.85 |
| **YEU** | composite < 50 hoặc không significant | SUPPRESS (nén) | ×0.70 |

**Phân bố Tier 1 hôm nay (35 rule MB):** TĂNG_TRƯỞNG **17** · MẠNH **3** · ỔN_ĐỊNH **1** · XUỐNG_CẤP **13** · YẾU **1**.

Context pack prompt MB hiển thị nhãn vòng đời cho **cả 3 tầng** (vd `[tăng↑]`, `[giảm↓]`, `[mạnh]`) → AI biết rule nào nên tin, nên giảm tin, nên theo dõi.

---

## 4. Mốc thời gian (đã kiểm hợp lý)

| Giờ VN | Việc | Lý do |
|---|---|---|
| 18:15 hôm trước | KQ MB D-1 xổ | dữ liệu mới |
| 20:15 | MRE chấm hit | có dữ liệu hiệu quả mới |
| **20:30** | **MB re-rank (cả 3 tầng)** | làm tươi điểm cho lần predict 17:42 hôm sau |
| **17:00** | **MB guard** | rebuild nếu snapshot stale (cron lỡ) |
| 17:42 | AI MB predict | đọc snapshot đã tươi |

Guard 17:00 chống tái diễn gap như `mining_log` từng mất 3 thứ Hai (05-11/18/25).

---

## 5. Bằng chứng MN/MT bất biến (chứng minh đa lần)

| Lần check | Kết quả |
|---|---|
| Sau Phase 1 (ranker mới) | 108/108 IDENTICAL |
| Sau Phase 2 (consumption) | 108/108 IDENTICAL |
| Sau Phase 3 (prompt) | 108/108 IDENTICAL |
| Sau R2 (3 cơ chế + vòng đời) | 108/108 IDENTICAL |
| **Before/after swap test** (đổi file hiện tại ↔ `.pre` trên cùng frozen DB) | 108/108 IDENTICAL |

Harness `_mn_mt_invariance_harness.py` dùng frozen DB + `PYTHONHASHSEED=0` cho tính tất định tuyệt đối.

---

## 6. Backup dự phòng

`backups/v10679_mb_rule_stack_20260602_234240/`:
- 5 file code: `rule_engine.py.v10679.pre`, `gpt_analyzer.py.v10679.pre`, `prompt_registry.py.v10679.pre`, `scheduler.py.v10679.pre`, `mb_rule_ranker.py.v10679.pre`.
- 4 bảng DB: `_bak_v10679_mined_rules` (105 rows) + `_bak_v10679_mined_rules_mb_daily` + `_bak_v10679_mb_rule_context` + `_bak_v10679_mb_rerank_log`.
- `MANIFEST.txt` ghi cách restore.

**Rollback nhanh**: copy file `.pre` về (bỏ đuôi) + tắt `MB_DAILY_RANK_ENABLE` + gỡ 2 cron mới.

---

## 7. Trung thực về dữ liệu (ranh giới chưa làm)

- **Tier 1 trend** = **LIVE** từ `mined_rule_effectiveness` → trend chính xác.
- **Tier 2 trend** = **STATIC** (V10667 không có time-split). Bước kế tiếp: live rolling re-measure 73 rule manual theo thời gian (đo lại lift hàng tuần) để có trend động cho T2.
- **Tier 3** dùng `half_stable` (đã ghi sẵn) làm proxy ổn định, chưa rolling.

---

## 8. Phạm vi & nút tắt

- **CHƯA đụng** đường NO_TOKEN của MB (theo dặn dò: token-path trước).
- Tier 2/3 luôn `live_eligible=False` cho tới khi owner OK nâng tầng.
- Rollback một dòng: tắt cờ + gỡ cron.

---

**STATUS**: V10679-R2 = MB-target rule stack mechanism + 3 cơ chế daily đặt tên + đa yếu tố + vòng đời rule. Code + verify local PASS, có backup, chờ owner OK deploy VPS. Đây là TẦNG RULES nền cho bước nâng prompt/AI MB tiếp theo.
