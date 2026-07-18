# V10821 — TỔNG KẾT TRỌN NGÀY-1 LIVE RULES-FIRST (18/07) + TOTAL-V2: PHƯƠNG PHÁP TỔNG HỢP MỚI CHO TOTAL VÀ /CHOI (SHADOW)

- **Ngày:** 2026-07-18, phiên 19:39 → 20:4x (UTC+7)
- **Trigger (owner 19:39):** "đã hết chu kỳ live với những thay đổi lớn em hãy kiểm tra phân tích đánh giá toàn diện sau đợt thay đổi lớn này. Total và /choi cần có 1 phương pháp mới với tín hiệu dàn trải ở các model và ở bt và số phụ ah em? cần kiểm tra và có kế hoạch cụ thể dùm anh"
- **Phạm vi:** đọc trọn ngày-1 trial V10820 (3 miền) + root-cause tầng Total + backtest 165 ngày 4 phương pháp tổng hợp + deploy TOTAL-V2 shadow (§52 đầy đủ). ZERO đụng /du-doan, writer bundle, /choi, prompt.

---

## PHẦN 1 — NGÀY-1 LIVE RULES-FIRST (PB-18.1): ĐÁNH GIÁ TOÀN DIỆN

### 1.1 Kết quả xổ 18/07 (Thứ 7)
| Miền | Số lô unique | ĐB (đuôi) |
|---|---|---|
| MN (4 đài: Bình Phước, Hậu Giang, Long An, TP.HCM) | 50 | 11 / 07 / 70 / 82 |
| MT (3 đài: Quảng Ngãi, Đà Nẵng, Đắk Nông) | 42 | 75 / 42 / 50 |
| MB (Nam Định) | 24 | 90 (GĐB 26890) |

### 1.2 Tuân thủ RULES-FIRST: 21/21 (100%)
- Danh sách rules ngày 18/07: **MN 14 số** (10 13 26 27 31 38 39 43 46 59 64 69 77 81 — BẮT BUỘC) · **MT 11 số** (10 13 26 39 41 46 59 69 77 91 94 — ƯU-TIÊN-MẠNH) · **MB 8 số lúc 17:42** (27 43 64 80 81 86 93 94 — BẮT BUỘC; sáng chỉ 6 số, rule nguồn MT-ngày-D nở thêm 27+93 sau khi MT quay 17:15 — đúng thiết kế as-of).
- **21/21 main của 7 LLM official × 3 miền đều nằm trong danh sách** (baseline trước đó: 24-30%). Số phụ biến-thể (đảo/±1): **0/21** — hôm trước ngày nào cũng dính.
- Trace: 28 call prompt_version=PB-18.1; 0 output rỗng; journal 0 lỗi cả ngày.

### 1.3 Trúng/trượt từng tầng (any-hit = chạm ≥1 số lô)
| Cohort | MN | MT | MB | Cộng |
|---|---|---|---|---|
| 7 LLM official (nghe lời) | 6/7 | 5/7 (2 WIN: opus 46+59, gpt-5-mini 46) | 4/7 | **15/21 = 71.4%** |
| Shadow bám 67 ngoài rules (MN) | 2/5 — 67 KHÔNG VỀ | — | — | bầy cãi-lời sập |
| Toàn pool 27 row | 13/27 | 22/27 | 15/27 | — |
| Danh sách rules về lô | 9/14 (64% vs nền 50% ✓) | 4/11 (36% vs nền 42% ✗) | 1/8 (12.5% vs nền 24% ✗) | 1 ngày = nhiễu |

- GĐB-đảo (V10816): ứng viên **54 VỀ lô MB ngay ngày-1 forward** (từ GĐB 45739 hôm 17/07). Ứng viên mai: **62** (GĐB 26890). Panel 🔄 tự chấm.
- Money board /choi: MB song-thủ [80, 34] → 34 VỀ (1 chân); MT [63, 41] → 63 VỀ (1 chân); MN nghỉ T7 theo lock tuần.
- A/B V10809 (đo addendum per-số): scored 15/15; ngày-1 arm B hại MB (1/5 vs prod 3/5) → **addendum per-số KHÔNG phải hướng đúng**.

### 1.4 Điểm trừ lớn nhất: BUNDLE BT 0/3 — đúng chỗ owner chỉ
| Miền | Bundle chốt | Kết cục | Số VỀ bị bỏ | Nó nằm ở đâu trong tín hiệu |
|---|---|---|---|---|
| MN | BT=31, lo2=[31,67] | LOSE cả bộ | **13** | 2 main (gemini-flash, gemini-pro) + 2 phụ (deepseek, gpt-5-mini) = 4 model chạm |
| MT | BT=41, lo2=[41,46] | BT trượt, lo2 PARTIAL (46✓) | 46 | 3 main + 2 phụ = 5 model chạm — vẫn xếp sau 41 (5 phiếu main) |
| MB | BT=80, lo2=[80,93] | LOSE cả bộ | **86** | 1 main (gemini-flash) + 3 phụ (opus, sonnet, gpt-5-mini) = 4 model chạm |

Root cause (đọc code `generate_final_bundle`, main.py): điểm = WR × strength × verdict × position, **phiếu main nặng, số phụ trọng số thấp, không neo rules** → tín hiệu "dàn trải ở bt và số phụ" (chữ của owner) bị chìm. Prompt mới (V10820) đã đưa tín hiệu đúng LÊN tầng model; tầng tổng hợp cũ chưa biết đọc.

---

## PHẦN 2 — BACKTEST TẦNG TỔNG HỢP (165 NGÀY, 20/12/2025 → 17/07/2026)

### 2.1 Leak-check trước khi tin số
- `mined_rules` có 11 rule nguồn ngày-D nhưng toàn cặp hợp lệ (MT←MN, MB←MN, MB←MT — nguồn quay TRƯỚC freeze miền đích). Đo thực tế trên `mined_rule_effectiveness`: **0.0% tails từ nguồn leak, cả 3 miền** → backtest M2s dùng đúng dữ liệu as-of.

### 2.2 Bốn phương pháp
- **M0** = bundle official đã ghi (đối chứng).
- **M1 COVERAGE** = 1 model 1 phiếu cho MỖI số nó chạm (main + phụ), tiebreak theo vị trí.
- **M2s COVERAGE-RULES** = M1 nhưng ưu tiên tuyệt đối số thuộc union rules ngày đó (≥4 số mới kích hoạt, thiếu thì fallback M1) — CÙNG danh sách RULES-FIRST bơm vào prompt.
- **M4 DÀN-4** = top-4 theo M1 (phục vụ /choi kiểu dàn).
- (M3 WR-weighted đã thử: ≈ M1, bỏ để giữ đơn giản.)

### 2.3 Kết quả (BT-lô % / lo2-any %)
| Miền | M0 bundle | M1 | **M2s** | M4 dàn-4 (any / TB số trúng) |
|---|---|---|---|---|
| MN toàn kỳ (n=140) | 42.9 / 63.6 | 42.9 / 65.0 | **48.6 / 71.4** | 88.6% / 1.66 |
| MT toàn kỳ | 39.3 / 63.6 | 44.3 / 64.3 | 44.3 / 64.3 | 82.9% / 1.53 |
| MB toàn kỳ | 21.4 / 41.4 | 27.1 / 40.0 | **32.9 / 55.7** | 68.6% / 0.94 |
| MN 60d gần | 41.7 | 43.3 | **51.7 (+10.0pp)** | 93.3% |
| MT 60d gần | 26.7 | 35.0 | **35.0 (+8.3pp)** | 76.7% |
| MB 60d gần | 15.0 | 25.0 | **30.0 (+15.0pp)** | 63.3% |

### 2.4 Đối chiếu 18/07 (ngoài backtest, nền prompt MỚI)
- Dàn-4 any **3/3 miền** (MN vớt 13; MT 97+46; MB 86+42).
- M2s hôm nay KHÔNG cứu được BT MN (31 vẫn đứng đầu trong-danh-sách theo phiếu) → M2s là lợi thế trung bình dài hạn, không phải đũa thần từng ngày. Trung thực ghi rõ.

---

## PHẦN 3 — TOTAL-V2 SHADOW ĐÃ LIVE (§52 đầy đủ)

- **Bảng** `v10821_total_v2_daily` (shadow_only=1, output_eligible=0, diagnostic_only=1, UNIQUE date+region): picks + hit của M0/M1/M2s/M4 mỗi ngày; **backfill 471 rows** (20/12/2025→18/07/2026).
- **Cron 19:14** hằng ngày (--catchup 3) — chấm sau khi có KQ, chỉ đọc `predictions` (pick trước freeze — causal), `lottery_results`, `final_bundles`, `mined_rule_effectiveness`.
- **API** `/api/admin/total-v2` (require_admin, Cache-Control no-store) + **panel 🧮 TOTAL-V2** tại /monitoring (viền xanh #38bdf8, cạnh CHASE-BIAS; bảng M0/M1/M2s/M4 × toàn-kỳ/60d/FORWARD; 7 ngày gần; preview picks hôm-nay trước giờ chấm; đăng ký loadAllSections + setInterval 60s).
- **Deploy:** backup 2 đầu (`backups/v10821_pre/` local + `/root/backups_v10821/` VPS) → upload 3 file sha khớp → compile OK → **restart GATE: script tự đợi daily-eval 20:00-20:20 ghi xong (81 rows @20:20) mới restart** — không cắt ngang job học; gọi nhầm `lottery-backend.service` (không tồn tại — vô hại) rồi restart đúng `lottery.service`; health 200, admin 401 khi chưa auth, journal sạch.
- **Hash 4 bảng official:** predictions / final_bundles / lottery_results **IDENTICAL pre=post**; model_daily_eval khác do scorer 20:20 ghi 81 rows đúng lịch (natural growth — ghi rõ minh bạch).

## PHẦN 4 — KẾ HOẠCH CỤ THỂ CHO TOTAL + /CHOI (trả lời thẳng câu owner)

| Mốc | Việc | Ngưỡng |
|---|---|---|
| 19→24/07 | Forward tự chạy (cron 19:14), panel 🧮 tự cộng | — |
| 25/07 (giữa kỳ, CÙNG mốc V10820) | Đọc M2s−M0 BT forward | Giữ dấu + → soạn nháp writer mới |
| **28/07 (chốt, CÙNG trial V10820)** | Quyết promote | **≥ +5pp BT gộp 3 miền (n≥30, any không giảm) → trình owner ký promote scoring `generate_final_bundle` = coverage-rules** (backup + rollback 2'; /choi đọc bundle nên TỰ HƯỞNG, không sửa /choi) · ≤ +2pp → đóng, giữ M0 |
| Sau 28/07 (tùy chọn riêng) | Play-style "dàn-4" cho /choi (any 68-89%) | Kèo vốn — owner quyết riêng, không gộp vào quyết định writer |

**Vì sao KHÔNG đổi writer ngay hôm nay:** (1) 1 biến số/lần — trial V10820 đang chạy, đổi writer giữa chừng làm nhiễu phép đo prompt; (2) backtest 165d đo trên nền prompt CŨ, cần forward xác nhận trên nền PB-18.1; (3) writer là logic official /du-doan — cần chữ ký owner (§52).

---

## ARTIFACTS
- Module + cron: `web/backend/_v10821_total_v2_shadow.py`
- Probes: `_v10821_day1_full.py`, `_v10821_probe2.py`…`_v10821_probe5.py`, `_v10821_agg_backtest.py`, `_v10821_leak_probe.py`
- Deploy: `_v10821_deploy.py`, `_v10821_restart.py`; backup `backups/v10821_pre/` + VPS `/root/backups_v10821/`
- Governance: CHANGELOG V10821 · SSOT V10821 · FU-V10821-TOTAL-V2 · AUTOMATION_STATE seq 282 · HISTORY · Playbook §5 (19/25/28-07) · Sổ tay mục 1.2
