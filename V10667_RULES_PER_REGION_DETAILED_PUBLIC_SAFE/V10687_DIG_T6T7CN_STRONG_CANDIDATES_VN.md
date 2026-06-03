# V10687 — Đào sâu T6/T7/CN (MB target) tìm rule gold + tổng hợp trạng thái

> **Generated**: 2026-06-03 12:40 VN
> **Trigger**: Owner: "xử lý T6/T7/CN thiếu BH-pass — đào thêm rule gold cho 3 thứ này" + "T3 đã hủy".
> **Trạng thái**: REPORT-ONLY (forensic). Không deploy code, không đụng official.
> **Live sync**: `artifacts/live_sync/20260603_122600/manifest.json` (DB tới 2026-06-02).

---

## 0. Kết luận thẳng (trung thực)

> **KHÔNG có rule gold (BH-pass FDR) cho T6/T7/CN — kể cả sau khi đào sâu mở rộng nguồn/lag/transform.**
> Tín hiệu CÓ thật nhưng ở mức **STRONG (p<.01)**, chưa đủ ngưỡng gold. Đây là **đặc tính của dữ liệu**, không phải thiếu nỗ lực.

Đề xuất: nạp các ứng viên STRONG vào **forward-audit 90 ngày** (`live_eligible=False`), KHÔNG gắn nhãn gold. Sau audit mới xét.

---

## 1. Phương pháp đào (cùng family V10636-CROSS, có guard)

| Tham số | Giá trị |
|---|---|
| Target | MB, weekday T6 (Thứ Sáu, Hải Phòng) / T7 (Thứ Bảy, Nam Định) / CN (Thái Bình) |
| Source region | MN, MT (D same-day hợp lệ — MB xổ cuối), MB (self-lag) |
| Lag | D, D-1 … D-7 |
| Prize (owner whitelist) | MB: DB/G1/G2/G4/G6/G7 ; MN/MT: DB/G1/G2/G5/G7/G8 (NO G3) |
| Transform | LAST2 (chính, đúng production) + FIRST2/HEAD_TAIL (exploratory) |
| Mẫu mỗi cell (n_eval) | **~322-328** (≈6 năm dữ liệu × 52 thứ/năm) — ĐỦ lớn |
| Baseline | `1-(1-p_MB)^avg_src_size`, p_MB≈0.238 |
| p-value | binomial normal-approx |
| FDR | BH trong family tập trung T6/T7/CN |
| Temporal guard | same-day source chỉ MN/MT; không MB(D)→MB(D) |

**Vì sao n không nhỏ?** MB có ~6 năm dữ liệu → mỗi thứ ~322 lần xuất hiện. Nên BH-pass fail KHÔNG do thiếu mẫu mà do **lift vừa phải (5-11pp)** so với ngưỡng FDR.

---

## 2. Kết quả — LAST2 (chính, conservative)

| Thứ | Tổng cells | BH-focused pass | p<.001 | p<.01 | p<.05 | lift≥5pp |
|---|---:|---:|---:|---:|---:|---:|
| T6 | 201 | **0** | 0 | 1 | 8 | 5 |
| T7 | 201 | **0** | 0 | 2 | 7 | 5 |
| CN | 201 | **0** | 0 | 2 | 9 | 3 |

**Top mỗi thứ (LAST2):**
- **T6**: `MN:G7#1:LAST2:D-4` — hit 63.38% vs base 54.83%, **lift +8.55pp**, p=0.0012
- **T7**: `MB:G6#3:LAST2:D-7` — hit 31.06% vs 23.79%, **lift +7.27pp**, p=0.0014
- **CN**: `MB:G7#2:LAST2:D-7` — hit 30.43% vs 23.79%, **lift +6.65pp**, p=0.0031

---

## 3. Kết quả — mở rộng transform (exploratory, 1809 cells)

| Thứ | BH-focused pass | p<.001 | p<.01 | lift≥5pp |
|---|---:|---:|---:|---:|
| T6 | **0** | 2 | 6 | 16 |
| T7 | **0** | 0 | 5 | 12 |
| CN | **0** | 1 | 7 | 15 |

**Top mỗi thứ (mở rộng):**
- **T6**: `MN:G1#1:FIRST2:D-4` — lift **+10.9pp**, **p=4.9e-5** (mạnh nhất toàn dig)
- **T7**: `MB:G6#3:LAST2:D-7` — lift +7.27pp, p=0.0014
- **CN**: `MN:G2#1:HEAD_TAIL:D-2` — lift +9.45pp, p=0.00036

Ngay cả ứng viên mạnh nhất (T6, p=4.9e-5) vẫn **suýt trượt** focused-BH (ngưỡng rank-1 trong family 1809 cells = 0.05/1809 = **2.76e-5**). p=4.9e-5 > 2.76e-5 → KHÔNG pass.

---

## 4. Vì sao KHÔNG có gold? (toán FDR + selection bias)

1. **FDR threshold rất khắt khe**: với family 603-1809 cells, rank-1 cần p < 8e-5 đến 2.76e-5. Lift +8-11pp với n~325 cho p≈1e-3 đến 5e-5 → chưa đủ.
2. **Selection bias**: ứng viên mạnh nhất nổi lên từ search rộng (1809 tổ hợp) → kỳ vọng có vài cái "đẹp do ngẫu nhiên". `bh_focused_pass=False` chính là guard trung thực chống điều này.
3. **Global FDR còn khó hơn**: nếu tính FDR trên TOÀN grid (như V10636 gốc) thì family lớn hơn → càng không pass. Focused đã fail nên global chắc chắn fail.

→ **Honest**: ép gold cho T6/T7/CN sẽ là p-hacking. Tốt nhất là gắn STRONG + forward-audit.

---

## 5. Ứng viên STRONG đề xuất cho forward-audit (per weekday)

Tất cả temporal hợp lệ (lag ≥ 2), `live_eligible=False`, `status=PRE_REGISTER_FORWARD_AUDIT`, cờ `SELECTION_BIAS_RISK`.

### T6 (Thứ Sáu — Hải Phòng)
| Lineage | Lift | Hit% | p-value | n | Tier | Nguồn dig |
|---|---:|---:|---:|---:|---|---|
| `MN:G1#1:FIRST2:D-4` | +10.9pp | 65.85% | 4.9e-5 | 325 | STRONG | wide |
| `MT:DB#1:FIRST2:D-6` | +8.73pp | 64.2% | 9.5e-4 | 324 | STRONG | wide |
| `MN:G7#1:LAST2:D-4` | +8.55pp | 63.38% | 1.2e-3 | 325 | STRONG | LAST2 |
| `MB:DB#1:LAST2:D-4` | +5.5pp | 29.28% | 1.2e-2 | 321 | MODERATE | LAST2 |

### T7 (Thứ Bảy — Nam Định)
| Lineage | Lift | Hit% | p-value | n | Tier | Nguồn dig |
|---|---:|---:|---:|---:|---|---|
| `MB:G6#3:LAST2:D-7` | +7.27pp | 31.06% | 1.4e-3 | 322 | STRONG | LAST2 |
| `MT:G5#1:HEAD_TAIL:D-4` | +7.2pp | 48.77% | 4.9e-3 | 326 | STRONG | wide |
| `MN:G2#1:LAST2:D-5` | +6.63pp | 61.54% | 9.5e-3 | 325 | STRONG | LAST2 |

### CN (Chủ Nhật — Thái Bình)
| Lineage | Lift | Hit% | p-value | n | Tier | Nguồn dig |
|---|---:|---:|---:|---:|---|---|
| `MN:G2#1:HEAD_TAIL:D-2` | +9.45pp | 64.33% | 3.6e-4 | 328 | STRONG | wide |
| `MT:G7#1:HEAD_TAIL:D-7` | +8.64pp | 51.85% | 1.0e-3 | 324 | STRONG | wide |
| `MB:G7#2:LAST2:D-7` | +6.65pp | 30.43% | 3.1e-3 | 322 | STRONG | LAST2 |
| `MB:G2#1:LAST2:D-4` | +5.84pp | 29.63% | 8.1e-3 | 324 | MODERATE | LAST2 |

Machine-readable: `machine_readable/V10687_T6T7CN_STRONG_CANDIDATES.json`.

---

## 6. Đề xuất rõ ràng cho owner

| Phương án | Mô tả | Em đánh giá |
|---|---|---|
| **A. Forward-audit STRONG** | Nạp 3-4 ứng viên STRONG/thứ vào forward-audit 90d (live_eligible=False). Sau closeout (≈2026-09-01) mới xét promote MANUAL pool. | ⭐ KHUYẾN NGHỊ — đúng doctrine, trung thực |
| **B. Đưa thẳng vào MANUAL pool (CONFIRM-only)** | Thêm ngay vào tầng MANUAL như rule CONFIRM (không drive), AI thấy để đối chiếu. | OK nếu owner muốn coverage T6/T7/CN ngay; vẫn không drive số |
| **C. Bỏ qua** | T6/T7/CN dựa hoàn toàn PRODUCTION (đang có 5 rule/thứ). | An toàn nhưng bỏ phí tín hiệu STRONG |

**Em nghiêng A** (audit trước) hoặc **B** (CONFIRM-only ngay, an toàn vì không drive). KHÔNG có phương án "gắn gold" vì dữ liệu không cho phép.

---

## 7. Trạng thái tổng hợp MB (cập nhật)

| Hạng mục | Trạng thái |
|---|---|
| PRODUCTION 35 rule | LIVE drive (17 tăng / 3 mạnh / 1 ổn / 13 giảm / 1 yếu) |
| MANUAL 77 rule | CONFIRM-only; BH-pass tập trung T2-T5; **T6/T7/CN = 0 gold** (xác nhận lại hôm nay) |
| PRE-REGISTER (T3) | **ĐÃ HỦY** — purge sạch `TIER3_WATCH` khỏi `mb_rule_context` hôm nay (V10686.1) |
| T6/T7/CN dig | KHÔNG có gold; có STRONG candidates (báo cáo này) |
| MN/MT cô lập 2 luồng | 18/18 PASS |
| MN/MT bất biến | 108/108 IDENTICAL |
| Full verify | 55/55 PASS |
| Code deploy VPS | CHƯA |
| Official mutation | KHÔNG |

---

## 8. Cần owner quyết

1. **T6/T7/CN**: chọn A (forward-audit) / B (MANUAL CONFIRM-only ngay) / C (bỏ qua)?
2. Sau đó quay lại lộ trình V10686: code V10684 (rolling re-measure) → V10683 (3 shadow experiments).

---

**Bottom line**: Đã đào hết sức cho T6/T7/CN. Sự thật: **không có gold**, nhưng có tín hiệu STRONG (lift +6 đến +11pp, p<.01) cho cả 3 thứ. Trung thực gắn STRONG + forward-audit thay vì ép gold. Anh chọn A/B/C để em xử lý tiếp (vẫn report-only tới khi anh OK code/deploy).
