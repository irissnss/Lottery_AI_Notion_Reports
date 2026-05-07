# V82 — Phương án tối ưu (data-driven, không động official)

## Nguyên tắc

1. Official LOCKED. Không sửa `/du-doan`, `/api/final-bundle`, official prompt, official selector, model roster.
2. Mọi đề xuất mới = shadow-only / measurement-only / dossier-only.
3. Mỗi quyết định promotion phải có 60d hoặc đầy đủ 14d natural live + owner OK.
4. Region khác nhau cần policy khác nhau — không global no-token tăng/giảm.

## Layer 1 — Hôm nay → 24h

A. Giữ nguyên cron chain 19:00-19:14 VN. KHÔNG đổi tham số. Chờ closeout 2026-05-08 để có 1 ngày live thật cho V79/V80/V81.

B. Bật một panel UI admin-only `/du-doan-test/admin-monitor` đọc:
   - `ai_no_token_cross_verification_shadow` (V79)
   - `cluster_weighted_consensus_shadow` (V79)
   - `mn_ai_herd_vs_v67_save_daily` (V80)
   - `mb_regime_shift_shadow` (V80)
   - `ai_region_specialist_provider_shadow_results` (V81)

   Mục đích: anh nhìn được hàng ngày AI herd vs NO_TOKEN herd vs V67/V73 vs cluster vs V81 pilot
   trước/sau closeout. KHÔNG có nút promote. KHÔNG có scoring nào ăn vào output.

   Phân loại: DATA_READY_UI_PENDING.

## Layer 2 — 7d window (đến 2026-05-14)

A. Tích lũy V81 pilot 7 ngày liên tiếp natural cron. Đo:
   - parse_status==OK ratio
   - cost per call (phải ≤ ngân sách provider thực tế)
   - would_save vs would_break per region
   - confidence calibration (HIGH/MEDIUM/LOW vs hit)

B. Tích lũy V79 cluster-weighted + V79 cross-verify rolling 7d. So với OFFICIAL/V67/V70/V73 trên 7d.

C. Báo cáo MB regime-shift 7d. Nếu MB official ≥ 7d toàn cold → escalate P0 forensic + bật MB regime shadow alert.

## Layer 3 — 14d window (đến 2026-05-21)

A. Sau 14d natural live cho V79/V80/V81:
   - Nếu MN cluster-weighted hoặc V81 specialist prompt có would_save > would_break + Wilson hit > OFFICIAL Wilson upper → đề xuất `MN_TEST_LANE_VOTER_PROPOSAL` (test lane only, không official).
   - Nếu MT toàn 4/4 hoặc 4/3 → giữ consensus-first, KHÔNG tự promote V67/cluster cho MT.
   - Nếu MB tiếp tục cold → kích hoạt MB regime forensic chuyên sâu (lag/source-prize/station/rule reset).

B. C-16 latency_score đã rolling-7d sau 2026-05-13. Cập nhật cost provider table với hóa đơn thực tế (anh có thể edit `_provider_pricing_table.py`).

## Layer 4 — Promotion candidates 60d (chỉ test lane, không official)

Dựa 60d evidence hôm nay:

| Region | Method | 60d | Save/Break/Net | Verdict |
|---|---|---|---|---|
| MN | MN_SPECIALIST_ROSTER_V1 | 51.7% (n=60) | 4/0/+4 | PROMOTION_CANDIDATE — cần dossier + owner OK |
| MN | MN_AI_CHAIN_PRESERVATION_V1 | 52.5% (n=59) | 5/1/+4 | PROMOTION_CANDIDATE — cần dossier + owner OK |
| MN | NO_TOKEN_HERD floor +1 | 51.7% (n=60) | 14/10/+4 | REGION_SPECIFIC_FLOOR — cần shadow validation 14d |
| MT | giữ OFFICIAL/V70 consensus-first | 50% (n=60) | — | KEEP_BASELINE |
| MB | MB_SPECIALIST_ROSTER_V1 | 36.6% (n=41) | 5/0/+5 | WAIT_60D — chưa đủ 60d sample (chỉ 41) |

→ Kể cả candidates đủ 60d cũng không tự promote. Cần dossier riêng và owner OK.

## Layer 5 — KHÔNG được làm

- Không tăng NO_TOKEN floor toàn cục (delta-pp 60d MN +0pp/MT +8.3pp/MB -3.3pp khác nhau).
- Không cap AI cluster cho MN (MN AI_HERD đang +3.3pp vs OFFICIAL).
- Không promote V67/V73/V79/V81 vào official trước 14-30d.
- Không sửa official prompt.
- Không bỏ MT_AI_CHAIN/MT_PRIOR_REGION khỏi shadow đo lường (đo destructive cũng có giá trị).

## Owner gates pending

1. UI panel admin (Layer 1B) → cần OK để bật read-only frontend.
2. MN dossier draft (Layer 4) → sau 14d natural live (đã có 60d).
3. MB forensic deep dive (Layer 3C) → kích hoạt nếu cold streak ≥ 7d.
4. Provider invoice update vào `_provider_pricing_table.py` → cần OK trước khi commit.
