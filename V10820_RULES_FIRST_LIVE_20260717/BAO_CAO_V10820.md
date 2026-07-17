# V10820 — ĐIỀU CHỈNH LỚN THEO LỆNH OWNER: RULES-FIRST VÀO PROMPT PRODUCTION (PB-18.1), CHẠY THẬT TỪ LIVE 18/07, ĐO 7-10 NGÀY

- Thời điểm: 2026-07-17 23:33 → 2026-07-18 00:1x (đêm trước live 18/07)
- Trigger: owner 23:33 bác phương án chờ-CP-S3: "backup tại thời điểm này và tiến hành điều chỉnh lớn luôn, chạy thật luôn trong 7-10 ngày để đo cái cải tiến… đảm bảo sau xử lý là chạy ổn định đáp ứng tốt cho live ngày mai luôn."
- Kết quả: prompt production đổi **PB-18.0 → PB-18.1** (lần đầu đổi prompt runtime kể từ PB-18.0), deploy xong 00:0x, verify sạch, hash 4 bảng IDENTICAL, rollback 2 phút luôn sẵn.

## 1. LÝ DO OWNER RA LỆNH (nguyên văn ý)

- Phương pháp/prompt đã chạy rất lâu; **đơn-model tín hiệu không ổn định** (bữa có bữa không, bữa dày bữa mỏng) — total tốt mấy mà đơn model lèo tèo thì output không đúng nổi.
- K11a chưa ổn định cũng vì đơn-model tín hiệu kém.
- Cái hiện tại đã đo quá lâu → làm lớn luôn, chạy thật 7-10 ngày, kết hợp lịch sử cũ (PB-18.0 đã live cả trăm ngày) là đủ so sánh.

## 2. NỘI DUNG THAY ĐỔI (gộp bằng chứng V10818 + V10819 thành MỘT thay đổi)

1. **`_rules_first_live_block()` mới trong `gpt_analyzer.py`**: cuối MỌI context pack, tính as-of **DANH SÁCH SỐ tường minh** từ TẤT CẢ `mined_rules` active của bucket (region, weekday) — đúng tập `mined_rule_effectiveness` mà V10819 đo "bốc-đại-1-số-từ-rules thắng model main cả 3 miền" (MB 30.2% vs 22.7%). Mỗi rule in kèm nguồn + tails, ví dụ: `Tây Ninh GĐB+G7 (D-1): 43 64 81`. Rule nguồn-D chưa quay tại giờ prompt → tự bỏ qua (không nhìn tương lai).
2. **Kỷ luật main theo miền**: MB/MN — main **BẮT BUỘC** chọn từ danh sách khi danh sách ≥4 số (xếp hạng TRONG danh sách bằng evidence độc lập, cấm xếp bằng mirror/±1); MT — **ƯU TIÊN MẠNH** (rules MT yếu, in≈out; mirror MT z=+3.55 hơi thật). Bucket nghèo (<4 số) → fallback kỷ luật chuẩn, không ép.
3. **Cấm số-phụ-biến-thể MỌI MIỀN** (V10818: cặp biến-thể MB any 33.6% vs 40.3% độc lập): phụ phải từ danh sách hoặc có evidence độc lập; cấm đảo (34→43) và ±1 (34→35/33/44/24) của main; không có evidence → chỉ chốt 1 số. Đưa thẳng vào khối "⛔ OUTPUT KHÔNG HỢP LỆ" của REASONING MANDATE.
4. **Anti-herding sửa 1 dòng**: "Tìm SỐ THAY THẾ gần (±1, cùng family)" → "từ DANH SÁCH MINED RULES / thống kê độc lập, KHÔNG biến thể ±1/đảo của số trap" (dòng cũ chính là thủ phạm dạy cả bầy 34-43 ngày 17/07).
5. **KHÔNG tắt PHA** (Đảo Gương/Giao Trục giữ cho main — sandbox batch 2 V10818: tắt hẳn làm main −7pp); `mirror_support` chỉ được tính điểm khi số đó nằm trong danh sách rules.
6. Versions: `CTX-16.4 → CTX-16.5`, `PB-18.0 → PB-18.1` — trace `prompt_version` tự tách trước/sau, là thước đo chính của trial.

## 3. KIỂM CHỨNG TRƯỚC DEPLOY (smoke as-of trong sandbox /tmp trên VPS, không đè production)

- Đối chiếu 17/07: block khớp **EXACT** MRE cả 3 miền — MB 16 số, MT 10, MN 9. (Bản đầu dùng LIMIT 5 READY_STRONG bị lệch tập MRE → sửa thành all-active rồi mới deploy — đây chính là tập đã backtest +7.5pp.)
- 18/07 as-of tối nay: MN 14 số (BẮT BUỘC) · MT 11 số (ƯU TIÊN MẠNH) · MB 6 số (BẮT BUỘC): 43 64 80 81 86 94.
- Call thật `gpt-5-mini` MB@18/07 (không ghi DB): main **64 — TRONG danh sách** ✓, phụ 46 evidence độc lập (không phải biến thể của 64 — hợp lệ).
- Build time +0.1-0.2s/pack — không ảnh hưởng lịch chốt.

## 4. DEPLOY + VERIFY (00:0x 18/07 — `_v10820_deploy.py`)

- Backup 2 đầu TRƯỚC khi sửa: `backups/v10820_pre/` (bản git HEAD 3 file) + VPS `backups/v10820_vps/` (3 file đang chạy). **Rollback = copy lại + restart ≈ 2 phút.**
- 3 file lên VPS (gpt_analyzer.py + `_v10803_chase_bias_shadow.py` banner live-trial + monitoring.html) — sha local=VPS khớp cả 3; compile OK; service active.
- Health 200 · admin 401 · sau restart: PB-18.1, block 3 miền đúng policy (MN BẮT BUỘC 14 / MT ƯU TIÊN 11 / MB BẮT BUỘC 6), grep "±1 cùng family" = 0 hit trên VPS, journal sạch.
- **Hash 4 bảng PRE=POST IDENTICAL** (predictions 10280 · final_bundles 420 · lottery_results 15094 · model_daily_eval 10144) — zero đụng dữ liệu official.

## 5. THƯỚC ĐO 7-10 NGÀY (đã ghi vào panel 🎯 + playbook §5)

| Mốc | Điều kiện | Hành động |
|---|---|---|
| 18/07 tối | %pick-in-rules panel 🎯 phải nhảy >50% (baseline 24-30%); đủ 15/15 chốt + pool 27 | xác nhận ngày-1 |
| 21/07 | model-any 3 ngày < baseline −10pp hoặc output lỗi tăng | **ROLLBACK NGAY** không cần hỏi |
| 23/07 CP-S3 | đọc giữa kỳ cùng V10809 A/B (2 arm cùng nền V10820 từ 18/07) | báo cáo owner |
| 25/07 | %in-rules >50% bền; main MB/MN không giảm | tiếp tục |
| 28/07 | main MB/MN ≥ baseline +3pp = **GIỮ VĨNH VIỄN** · ±3pp = thêm 7 ngày · <−3pp = **rollback** | quyết cùng owner |

Baseline so sánh: main-hit 90d MB 22.7% / MN 42.8% / MT 36.3% + toàn bộ lịch sử PB-18.0 trong trace. ML models (meta/rf/xgb 90-94% ngoài rules) KHÔNG đổi đợt này — tránh 2 biến số cùng lúc; đề xuất riêng sau khi trial chốt.

## 6. ẢNH HƯỞNG LÊN CÁC TRACK ĐANG CHẠY

- V10809 shadow A/B: từ 18/07 cả 2 arm tự nằm trên nền V10820 → A/B vẫn đo đúng delta addendum per-số; so sánh xuyên 16-17/07 phải tách đoạn (PB-18.0 vs PB-18.1). CP-S3 đổi vai = đọc giữa kỳ.
- Panel 🎯 RULES BỊ BỎ RƠI (V10819): banner đỏ LIVE TRIAL — cột FORWARD (từ 18/07) = sau-thay-đổi; full/90d = baseline.
- Panel 🪞 CẶP BIẾN THỂ (V10818): kỳ vọng tỷ lệ ghép biến-thể giảm mạnh từ 18/07.
- FU-V10819-RULES-DROP + FU-V10818-VARIANT-PAIR → `SUPERSEDED_BY_V10820`; FU mới `FU-V10820-RULES-FIRST-LIVE` (LIVE_TRIAL_RUNNING).
- K11a: theo owner, bất ổn là do đơn-model tín hiệu kém → không flip đợt này; đánh giá lại sau trial.

## 7. ARTIFACTS

- Code: `web/backend/gpt_analyzer.py` (PB-18.1), `_v10803_chase_bias_shadow.py`, `web/frontend/monitoring.html`
- Probe/deploy: `_v10820_smoke.py`, `_v10820_smoke2.py`, `_v10820_deploy.py`, `_v10820_grepcheck.py`
- Backup: `backups/v10820_pre/` (local) + `/root/Lottery_AI_Test/backups/v10820_vps/` (VPS)
- Governance: CHANGELOG V10820 · SSOT V10820 · FU-V10820 · AUTOMATION_STATE seq 281 · HISTORY · Playbook §1+§5 · ACTIVE_ROADMAP V10809 §2-4
