# V10641 — RECHECK BY CODE (read-only) — FULL EVIDENCE DETAIL

Session: 2026-05-30 (đêm). Mode: READ-ONLY (đo + báo cáo; KHÔNG deploy/push-code-private/đổi official/cron/AI-provider/ví).
Repo (private) · VPS (redacted) · DB (production sqlite, opened read-only).
Vai trò: kỹ sư kiểm chứng — đo lại sự thật theo code, KHÔNG khẳng định lại kết luận cũ. Per-slice, no-lookahead, ngưỡng nghiêm.

NOTE trung thực: prompt giả định "MT/MB OFF (chỉ MN override live)". Thực tế phiên trước agent đã BẬT thêm MT override (V10640D). Item C audit lại chính MT override này theo ngưỡng nghiêm — kể cả nếu RỚT chuẩn (khả năng rollback).

═══════════════════════════════════════════════════════════
## §1. KHUNG ĐO CHUẨN (framework)
═══════════════════════════════════════════════════════════
HÀM CHẤM HIT BẠCH THỦ (code):
- `web/backend/database.py:4611 verify_final_bundle()` → dòng 4648: `bach_thu_status = 'WIN' if bach_thu in tails_set else 'LOSE'`.
- `tails_set` = tập đuôi (2 chữ số cuối) của actual results. Hit = bach_thu ∈ tails_set (region, date, bất kỳ giải nào).

BASE-RATE per slice = E[# đuôi trúng phân biệt mỗi ngày]/100 (random pick trúng kỳ vọng), tính riêng region×weekday, 90d:
| region | base-rate per weekday |
|---|---|
| MN | T2 41.8 · T3 40.6 · T4 41.9 · T5 42.1 · T6 41.5 · **T7 52.2** · CN 41.5  (≈42%) |
| MT | T2 29.9 · T3 30.4 · T4 30.2 · **T5 42.8** · T6 30.2 · **T7 42.4** · **CN 41.0** (≈30% / 42%) |
| MB | T2 23.2 · T3 23.5 · T4 23.8 · T5 23.5 · T6 24.0 · T7 24.3 · CN 23.9  (≈24%) |

PHÁT HIỆN NỀN TẢNG (đảo cách đọc mọi con số):
- **MN official ~45% ⇒ chỉ +~3pp trên base ~42%** (MN có ~42 đuôi trúng/ngày → 1 số ngẫu nhiên đã trúng ~42%).
- **MB official ~24% ≈ base ~24% ⇒ lift ~0 = NGẪU NHIÊN** (MB không có tín hiệu BT đáng kể).
- Mọi "lift" phải tính vs base-rate slice, KHÔNG vs "official". p-value = one-sided binomial P(X≥hits | n, base).
- NGƯỠNG PROMOTE: n≥30 AND lift≥+5pp AND p<0.05 AND no-lookahead PASS. Thiếu → HOLD-LANE/UNVERIFIED/KILL.

Tái lập: query base-rate = đếm distinct 2-digit tails (prizes_json + tail_db + tail_g8) per (region,date), group theo weekday, /100.

═══════════════════════════════════════════════════════════
## §2. ITEM A — MB G2 D-2 → MN
═══════════════════════════════════════════════════════════
### ITEM A: MB G2 D-2 → MN
VERDICT: **KILL**
LÝ DO (số liệu): Đo BROAD (MB-all D-2 → MN-all D, n=115): observed overlap = **100.0%** nhưng BASE overlap (do may, vì cả 2 bên nhiều đuôi) = **100.0%** → **lift = +0.0pp, p = 1.000**. Per-weekday đều +0pp. "60%/76%" là **artifact phủ-sóng + slicing**, KHÔNG phải tín hiệu. Chênh "+14.1pp vs +0.3pp" trước đây = do (a) chọn baseline sai (so với official thay vì base-rate overlap) + (b) cả 2 tập nhiều đuôi → overlap luôn cao do may. KHÔNG phải lookahead leak (source = D-2, có trước D).
BẢNG PER-SLICE:
| region | weekday | n | base_rate | hit_rate | lift | p | no_lookahead |
|---|---|---|---|---|---|---|---|
| MN(from MB-all D-2) | T2..CN | 16-17 mỗi | 100% | 100% | +0.0pp | 1.000 | PASS |
| (narrow G2→G2) | — | — | overlap-base cao (MN-G2 nhiều đuôi) | ~base | ~+0pp (cùng cơ chế) | n/a | PASS |
ĐƯỜNG DẪN BẰNG CHỨNG: hit code `database.py:4648`; query overlap-base + binomial trên lottery_results (prizes_json "Giải nhì"); script đo broad/narrow chạy read-only trên VPS (kèm trong session log).
RỦI RO / CẢNH BÁO: Đây là gốc của lúng túng — mọi tài liệu cũ nói "60%/76%" phải bỏ. Không can thiệp official theo tín hiệu này.

═══════════════════════════════════════════════════════════
## §3. ITEM B — MN override V10640 (LIVE official)
═══════════════════════════════════════════════════════════
VERDICT: **HOLD-LANE** (live, reversible, no-lookahead-correct — NHƯNG chưa đạt ngưỡng promote).
LÝ DO (no-lookahead, 92 ngày MN settled):
- Claim "+5.4pp vs official" ĐÚNG: override 50.0% (46/92) vs official 44.6% (41/92) = **+5.43pp**; override khác official 13/92 ngày, net +5 (5W/0L).
- Nhưng vs BASE-RATE (anchor chặt): override 50.0% vs base 43.1% = **+6.9pp, p=0.111 (≥0.05 → KHÔNG significant)**.
- PER-SLICE region×weekday: mọi weekday n=13-14 (<30) → không slice nào promotable. Weak weekday lift vs base ÂM: **T7 35.7% vs base 51.8% = −16.1pp**, T6 −10.8pp, T4 −3.5pp.
- "0 losses" chỉ vì official đã trượt cả 13 ngày override khác → không phải bằng chứng an toàn thật.
- LIVE nhưng impact thật = 0 tới giờ (deploy 2026-05-30, stored bach_thu = official top1 trên 92/92 ngày). Reversible (cờ), defensive (lỗi→official), official_drift chỉ bach_thu/lo2/lo3 của MN.
BẢNG: region|weekday|n|base|official|override|lift_vs_base|p|no_lookahead
MN|CN|13|41.5%|61.5%|61.5%|+20.0|0.119|PASS · MN|T2|13|41.9%|61.5%|69.2%|+27.4|0.043|PASS · MN|T3|13|40.6%|61.5%|61.5%|+20.9|0.106|PASS · MN|T4|13|41.9%|23.1%|38.5%|**−3.5**|0.698|PASS · MN|T5|13|42.1%|46.2%|53.8%|+11.8|0.279|PASS · MN|T6|13|41.5%|30.8%|30.8%|**−10.8**|0.858|PASS · MN|T7|14|51.8%|28.6%|35.7%|**−16.1**|0.930|PASS · MN|ALL(merged)|92|43.1%|44.6%|50.0%|+6.9|**0.111**|PASS
BẰNG CHỨNG: `_v10640_official_perslice_override.py:26` (MN enabled), `:80,86` (no-lookahead date<today), `main.py:9529,9535-9545` (wiring); hit `database.py:4648`.
RỦI RO: per-slice n<30 + p=0.111 → không promotable; weak weekday âm; toàn bộ edge = 5 flip/13 ngày (mỏng, may rủi).

═══════════════════════════════════════════════════════════
## §4. ITEM C — MT lane→official (C1) + MT override V10640D em vừa bật (C2)
═══════════════════════════════════════════════════════════
### C1 (du_doan_test lane → official): VERDICT **HOLD-LANE**
- Lane sạch nhất (STRENGTH_WEIGHTED, n=57): vs official **+8.8pp** (full), +13.3pp (30d) → khớp claim "+8.5/+11.6pp". vs base +10.3pp. Promote-gate sim net +5 (8 save/3 break).
- RỚT chuẩn: region p=**0.070** (>0.05); per-weekday n=8 (<30); **no-lookahead PARTIAL** (199/596 dòng backfill 2026-05-03, không forward-log). Chỉ T5 significant (8/8, p=0.001).
### C2 (MT override V10640D — LIVE, em bật phiên trước): VERDICT **UNVERIFIED** → đề xuất **NARROW (tắt T7/CN), KHÔNG full-rollback**
- "+4.4pp" XÁC NHẬN là vs-OFFICIAL (+4.5pp@90d, +13.6pp@60d — khớp docstring). vs base: **+16.5pp region (p=0.0002, n=118)**.
- Nhưng per-weekday n=16-18 (<30) → không slice nào đạt n≥30. Edge tập trung GIỮA TUẦN T3/T4/T5 (p=0.027/0.042/0.030 PASS); **T6/T7/CN yếu + gần đây ÂM** (T7 −5→−17pp, CN −4→−17pp 30-60d gần).
- No-lookahead PASS (pick integrity 809==809, 0 disagree).
- ⚠ **BUG family-classifier (member set 1 phần ngẫu nhiên):** `random-forest` + `glm-5.1` bị LOẠI nhầm (keyword `random_forest`/`glms`); `nemotron-3-super` bị NHẬN nhầm là combo (khớp "super"). Edge đo được là cho roster vô tình này.
BẢNG C2: MT|T3|16|.303|.563|**+25.9**|0.027|PASS · MT|T4|17|.302|.529|+22.7|0.042|PASS · MT|T5|18|.418|.667|+24.8|0.030|PASS · MT|T6|18|.306|.389|+8.3|0.298|PASS · MT|T7|17|.421|.588|+16.8|0.125|PASS(âm gần đây) · MT|CN|16|.409|.438|+2.8|0.504|PASS(âm gần đây) · MT|ALL|118|.352|.517|+16.5|0.0002|PASS(region)
BẰNG CHỨNG: `main.py:9535-9545` (live wiring), `_v10640_official_perslice_override.py:54-76` (_choose_no_token_combo_main), `:43-51` (_family BUG). Comment "MN only" `main.py:9532` đã cũ (MT đang bật). Rollback lever: `OVERRIDE_CONFIG["MT"]["enabled"]=False` (tức thì).
RỦI RO: C2 chưa đạt per-slice; T6/T7/CN âm gần đây → NÊN narrow (tắt T7/CN, giữ T3/T4/T5); classifier bug nên sửa; full-kill sẽ mất ~+4-5 net BT/90d nên KHÔNG nên.

═══════════════════════════════════════════════════════════
## §5. ITEM D — MB freq_hot
═══════════════════════════════════════════════════════════
VERDICT: **HOLD-LANE** (claim +15.7pp là ARTIFACT; không edge cấu trúc; tín hiệu W60 gần đây có thật nhưng recent-only → forward-monitor, KHÔNG promote).
LÝ DO:
- Base 23.8% xác nhận → official MB ~24% ≈ NGẪU NHIÊN (lift ~0).
- "+15.7pp" = **artifact 2 lớp chọn**: freq_hot recent-HOT (34.3%) − official recent-COLD (18.6% = đúng trailing-70d, official −5.1pp DƯỚI base). ~1/3 khoảng cách là do official lạnh, không phải freq_hot mạnh.
- KHÔNG edge cấu trúc: full-history W30 +0.5pp (p=0.30), W60 +0.0pp (p=0.51).
- Significant CHỈ recent W60: last90 +15.1pp (p=0.001), last60 +18.1pp (p=0.0015) — nhưng recent-only, không bền, + **KHÔNG phải config W30 đã publish** (W30 không bao giờ đạt p<0.05).
- Dàn 2026-05-30 = W30 (BT=14): BT=14 TRÚNG; dàn 5/10 trúng (n=1 ngày, không significant). Token-free XÁC NHẬN (chỉ đọc lottery_results; grep freq_hot trên VPS = none → chưa wire runtime). MB_STRENGTH_CAP=6.0 (`database.py:2428`) verified live, orthogonal với freq_hot.
BẢNG (W30 published, full history): MB|ALL|2262|.238|.243|+0.5|0.302|PASS · per-weekday đều ~0, NS. Recent W60 last90: n=90|base.238|hit.389|+15.1|0.001 (recent-only, không bền).
RỦI RO: bẫy sai-baseline (so official lạnh); recency/overfit; config 34.3%(W45-55) ≠ dàn publish(W30); doc roadmap A1 còn ghi "+15.7pp most valuable" → cần re-anchor về base (đã flag, KHÔNG sửa vì read-only).

═══════════════════════════════════════════════════════════
## §6. ITEM E — Doctrine official
═══════════════════════════════════════════════════════════
VERDICT khung: **GIỮ "official read-only + override per-slice có kiểm soát" — NHƯNG siết lại định nghĩa "đã chứng minh".**
- Không 1 item nào (A-D) đạt ngưỡng PROMOTE nghiêm (n≥30/slice AND lift≥+5pp vs base AND p<0.05 AND no-lookahead PASS). Tất cả = KILL/HOLD-LANE/UNVERIFIED.
- 2 override LIVE của agent (MN, MT) đều CHƯA đạt per-slice bar (n=13-18/weekday, cần ~7 tháng/weekday để đạt n≥30). MN: p=0.111 vs base. MT: region-significant nhưng T7/CN âm gần đây + classifier bug.
- Để MAX BT-hit/miền thật: (i) giữ official làm nền; (ii) override chỉ ở slice có region-significance + theo dõi per-slice; (iii) chấp nhận bằng chứng promote-grade per-slice cần nhiều tháng; (iv) cảnh giác base-rate cao (MN ~42%) làm "win%" trông to nhưng lift nhỏ.
- ĐỀ XUẤT (không tự thực thi): NARROW MT override (tắt T7/CN); fix family-classifier bug; tiếp tục forward-log MN/MT/freq_hot tới khi đủ n≥30/slice.

═══════════════════════════════════════════════════════════
## §7. BẢNG TỔNG HỢP 5 VERDICT + ƯU TIÊN
═══════════════════════════════════════════════════════════
| Item | Verdict | Lift vs BASE (anchor chặt) | Ngưỡng promote? |
|---|---|---|---|
| [A] MB G2 D-2 → MN | **KILL** | +0.0pp (p=1.000) | FAIL (lift=0) — ảo phủ sóng |
| [B] MN override (live) | **HOLD-LANE** | +6.9pp nhưng p=0.111; weak-wd âm | FAIL (p, n<30/slice) |
| [C1] MT lane→official | **HOLD-LANE** | +10.3pp vs base nhưng p=0.070; no-lookahead PARTIAL | FAIL (p, n<30, lookahead) |
| [C2] MT override (live, em bật) | **UNVERIFIED→NARROW** | +16.5pp region p=0.0002 NHƯNG per-slice n<30, T7/CN âm gần đây, classifier bug | FAIL per-slice → narrow T3/T4/T5 |
| [D] MB freq_hot | **HOLD-LANE** | ~0 cấu trúc; W60 recent +15pp (không bền, ≠ config publish) | FAIL (structural ~0) |

ƯU TIÊN HÀNH ĐỘNG (đòn bẩy lớn nhất trước, KHÔNG tự thực thi — chờ chủ + TanPhatAI):
1. **MT override (C2):** NARROW — tắt T7/CN (đang âm), giữ T3/T4/T5; fix family-classifier bug. (Reversible: cờ MT.)
2. **MN override (B):** giữ lane, KHÔNG quảng bá "đã chứng minh"; theo dõi T4/T6/T7 (đang âm vs base).
3. **MB freq_hot (D):** re-anchor doc về base; lock 1 cửa sổ W; forward-monitor, không promote.
4. **MB G2→MN (A):** KILL — bỏ khỏi mọi tài liệu/quyết định.
5. CP-66.7 OVERDUE (2026-05-21, data-blocked) → recheck 2026-06-03.

SỰ THẬT CỐT LÕI: với base-rate đúng, **không tín hiệu nào đạt chuẩn promote nghiêm**; 2 override live là "lane bet" hợp lý NHƯNG chưa significant per-slice. Official MN ~45% chỉ +3pp trên ngẫu nhiên; MB ~ngẫu nhiên hoàn toàn.

