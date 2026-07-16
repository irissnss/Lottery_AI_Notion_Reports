# BÁO CÁO V10809 — AUDIT MỐC CỬA SỔ XẾP HẠNG RULES + KHỞI ĐỘNG SHADOW A/B 7 NGÀY LIVE (16-22/07)

Ngày: 2026-07-16 (10:35 → 11:2x). Trigger: owner xác nhận "đang đi đúng hướng" và yêu cầu:
(1) xem lại rules đang cập nhật tự động phân tích xếp hạng ở mốc 12W, hệ số từng miền (nam 8W? trung 6-8W?)
còn đúng không, có điều chỉnh gì không; (2) chạy test shadow 7 ngày × 3 miền × 5 model AI kết hợp tốt và
tệ nhất, tổng hợp những cải thiện vừa làm rõ; (3) sau đó đưa ra đề xuất hoàn hảo an toàn nhất;
(4) ghi nhận lại toàn bộ — "anh không nhớ nổi đâu".

---

## PHẦN 1 — MỐC CỬA SỔ THẬT TRONG CODE (trí nhớ anh gần đúng, nhưng bị đảo miền)

| Tầng | File | Công thức/trọng số | Phạm vi |
|---|---|---|---|
| Miner tuần (đẻ rule + nhãn 3-LAYER trong prompt) | `_seed_rules.py` / `weekly_rule_miner.py` | composite = **0.50×12W + 0.35×16W + 0.10×4W** (+0.05 confidence) | CHUNG cả 3 miền |
| MB re-rank hằng ngày | `mb_rule_ranker.py` (MB-PROD-DYN8W) | **8W 0.40** / 12W 0.30 / 16W 0.20 / 4W 0.10 | CHỈ MB |
| MN/MT re-rank hằng ngày | `_v10708_mnmt_rule_ranker.py` | **12W 0.35 / 16W 0.30** / 8W 0.25 / 4W 0.10 | CHỈ MN/MT |
| Rule engine V20 (chấm runtime) | `rule_engine.py` | 12W execution check + 16W stability (SPIKE_RISK ×0.80, stable ×1.05) | cả 3 miền |

Kết luận đối chiếu trí nhớ: mốc **12W là trục chính** — đúng như anh nhớ. Nhưng **8W là hệ số của MB**
(không phải miền Nam), MN/MT nhấn 12W/16W, và **không tồn tại mốc 6W nào trong code**.
Điểm quan trọng nhất: TẤT CẢ các mốc này chấm rule bằng `hit_any` CỤM (any-of-k đuôi trúng bao lô) —
cùng semantics với nhãn "12W=92%" đã chứng minh gây hiểu lầm ở V10805.

## PHẦN 2 — AUDIT THỰC NGHIỆM: MỐC NÀO DỰ BÁO TƯƠNG LAI TỐT NHẤT? (`_v10809_window_audit.py`)

Dữ liệu: 2921 dòng `mined_rule_effectiveness` (20/12/2025 → 15/07/2026), forward-only:
trailing HR cửa sổ W tính từ các lần eval TRƯỚC ngày D → so với kết quả thật tại D.
Ba phép đo: corr pooled, tercile spread (nhóm 1/3 trailing cao nhất vs thấp nhất), top-2/ngày lift.

### 2a. Thước CỤM-any (thước hệ thống ĐANG dùng để xếp hạng) — HỎNG

| Miền | Kết quả | Ý nghĩa |
|---|---|---|
| MN | bão hòa ~96%, spread ±0..−5pp mọi mốc | rule nào cũng "trúng cụm" gần mọi ngày → xếp hạng theo thước này ở MN gần như vô nghĩa |
| MT | dương yếu (+5.1..+7.6pp, W16 tốt nhất) | còn chút giá trị nhưng mỏng |
| MB | **ĐẢO CHIỀU −6.9..−12.9pp** (MB_8W_tuned −11.2pp) | rule vừa "nóng cụm" thì kỳ sau KÉM hơn (mean-reversion) — xếp MB theo cụm-any nóng = chọn ngược |

### 2b. Thước PER-SỐ (thước thật để chọn số) — MỐC 12W/16W SỐNG TỐT

| Miền | Mốc tốt nhất | Tercile spread | corr | top2-lift |
|---|---|---|---|---|
| MN | W16 (12W sát nút) | **+12.6pp** (54.0% vs 41.4%) | +0.192 | +4.5pp |
| MT | W16 (12W sát nút) | **+12.3pp** (47.2% vs 35.0%) | +0.231 | +3.9pp |
| MB | W12/W8 | **+3.7pp** (yếu hơn hẳn 2 miền kia) | +0.03 | +1.9..+2.3pp |
| MB (mốc ngắn) | W4 −2.5pp, W6 −0.9pp | ÂM — mốc ngắn ở MB là nhiễu | | |

Công thức 12W-tuned hiện tại của MN/MT đứng gần đầu bảng per-số ở CẢ 3 miền
(MB: 12W-tuned +3.9pp > chính công thức MB-8W-tuned +2.4pp).

### 2c. Thiên lệch cụm — bằng chứng số cho "rule rải thảm được thưởng nhầm"

| Miền | corr(nhả-nhiều-số, HR-any-12W) | corr(nhả-nhiều-số, per-số thật) |
|---|---|---|
| MN | +0.58 | **−0.62** |
| MT | +0.45 | **−0.72** |
| MB | +0.39 | **−0.83** |

Rule càng nhả nhiều số → điểm cụm-any càng cao (được xếp hạng cao) → nhưng giá trị per-số càng THẤP.
Đây là gốc rễ thống nhất với chuỗi V10805→V10808: nhãn ĐÃ sửa trong đề xuất; giờ chứng minh
BẢNG XẾP HẠNG cũng cần đổi thước.

### 2d. TRẢ LỜI 3 CÂU CỦA ANH

1. **"Mốc 12W còn đúng không?"** — CÒN ĐÚNG về độ dài cửa sổ: 12W/16W là mốc dự báo tốt nhất
   trên thước per-số ở cả 3 miền. Cái SAI không phải mốc mà là THƯỚC (đang chấm cụm-any).
2. **"Hệ số từng miền (nam 8W, trung 6-8W)?"** — Thực tế code: MB=8W, MN/MT=12W/16W, không có 6W.
   Audit cho thấy 8W-emphasis của MB không có lợi thế (per-số MB: 12W-tuned +3.9pp > 8W-tuned +2.4pp;
   cụm-any thì cả hai đều âm). Mốc ngắn 4W/6W ở MB còn ÂM → không nên thêm 6W.
3. **"Có điều chỉnh gì không?"** — Có, gói vào CP-L6 (CHƯA làm gì vào production trong phiên này):
   - Đổi thước chấm ranking: cụm-any → per-số (hoặc hybrid per-số-chính).
   - GIỮ mốc 12W/16W làm trục; 4W chỉ dùng làm livingness-check (không vào điểm chính).
   - MB bỏ 8W-emphasis, dùng chung 12W-tuned trên per-số.
   - Đồng bộ với đề xuất (i) V10808: align production_tier theo per-số z-score.

## PHẦN 3 — SHADOW A/B 7 NGÀY LIVE (16-22/07) — ĐÃ KHỞI ĐỘNG

- **5 model** (đúng yêu cầu tốt+tệ): KÉM = gemini-2.5-flash, gpt-5-mini | MẠNH = claude-opus-4-6,
  qwen3.7-max | TRUNG = deepseek-reasoner.
- **Arm B** (cron gọi mỗi ngày): prompt production + addendum "🧭 ĐIỀU KIỆN TRỎ MIỀN & NHÃN PER-SỐ" —
  đúng bản đã kiểm chứng sandbox V10807 (30 call ngày bẫy) + V10808 (48 call ngày thường):
  per-số per-rule causal (chỉ dữ liệu < ngày D), gate ô âm/dương theo ma trận routing,
  MN CONV×2 trap alert, kết luận bắt buộc ≥2 bằng chứng nội-miền khi vượt dòng ⛔/⚠/🚨.
  Emission rule tính LIVE từ `mined_rules` active + `lottery_results` (mirror `mined_rule_eval`) —
  không dùng bảng chấm điểm của ngày hôm nay (chưa tồn tại trước giờ xổ) → không leakage.
- **Arm A KHÔNG tốn call**: chính là output production hằng ngày của 5 model đó (bảng `predictions`),
  scorer tự đối chiếu cùng model cùng ngày → so găng công bằng "nếu hôm đó có addendum thì sao".
- **Cron (giờ VN)**: 04:20 MN · 16:48 MT · 17:42 MB · 19:15 chấm điểm. Idempotent, tự tắt sau 22/07.
- **Ghi DUY NHẤT** bảng `v10809_shadow_ab_daily` (shadow_only=1, output_eligible=0) — ZERO đụng official.
- **Theo dõi không cần nhớ**: khối 🧪 SHADOW A/B 7 NGÀY trong panel 🏃 `/monitoring` (auto-refresh 60s):
  so găng B vs PROD tổng / theo miền / theo model + bảng 30 dòng gần nhất.
- **Day-1 đã chạy lúc 11:04**: MN gemini-flash [96,17], gpt-5-mini [96,02] đã ghi bảng; opus/qwen/deepseek
  nối tiếp; MT/MB vào cron chiều nay. Chi phí ước tính cả 7 ngày ~105 call ≈ 3-6 USD.

## PHẦN 4 — GHI NHẬN CỐ ĐỊNH (trả lời "anh không nhớ nổi")

Roadmap mới `docs/ACTIVE_ROADMAP_V10809_SHADOW_AB_7D.md` — RULE bắt buộc surface đầu MỌI phiên:

| CP | Ngày | Việc |
|---|---|---|
| CP-S1 | 18/07 | Health shadow ngày 1-2 (đủ 15 row/ngày, lỗi=0, scorer chạy) |
| CP-S2 | 19-20/07 | Giữa kỳ; nếu B thua A ≥15pp bền 2 miền → dừng sớm. CP-L6 19/07 chỉ ký phần không phụ thuộc shadow |
| **CP-S3** | **23/07** | **Tổng kết 105 cặp → trình ĐỀ XUẤT HOÀN HẢO AN TOÀN NHẤT** |
| CP-S4 | 26/07 | Gỡ cron V10809 |

## PHẦN 5 — DEPLOY + AN TOÀN

Deploy `_v10809_deploy.py`: backup 2 chiều (`backups/v10809_pre/` local + `/root/backups/v10809_pre/` VPS)
→ upload 3 file (`_v10809_shadow_ab.py` mới, `_v10803_chase_bias_shadow.py` +`_shadow_ab7_stats`,
`monitoring.html` +khối 🧪) → compile OK → restart `lottery.service` active → smoke health=200,
chase-bias(anon)=401, monitoring(anon)=401 → view check `shadow_ab7` OK → cron 4 dòng installed
(verify `crontab -l`) → journal sạch → **hash 4 bảng official pre=post IDENTICAL**
(predictions 10162/2ffa27cc · final_bundles 415/c6119479 · lottery_results 15081/1a1820b1 ·
model_daily_eval 9986/aaa91dc6). Rollback: `cp /root/backups/v10809_pre/* + restart`;
gỡ cron: `crontab -l | grep -v V10809 | crontab -`.

## PHẦN 6 — ĐỀ XUẤT TỐT NHẤT HIỆN TẠI (chờ dữ liệu shadow để thành "hoàn hảo an toàn nhất" 23/07)

1. (Đang chạy) Shadow 7 ngày quyết định số phận addendum — nếu B ≥ A và không phá miền nào →
   bật addendum vào `build_context_pack` official (CP-S3 23/07 trình kèm rollback).
2. (CP-L6 19/07, không phụ thuộc shadow) Demote/loại Quảng Ninh G6+G7→MT (−8.4pp z=−2.39, n=186);
   align tier miner theo per-số.
3. (CP-L6, mới từ V10809) Đổi thước xếp hạng rules: cụm-any → per-số, giữ mốc 12W/16W, 4W=livingness,
   MB bỏ 8W-emphasis.
4. (Sau shadow) Quyết định thay API gemini-2.5-flash / gpt-5-mini bằng chứng cứ B-arm 7 ngày
   (V10807: 2 con này nghe gate tốt nhất — có thể giữ nếu B cải thiện rõ).
