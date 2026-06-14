# V10709 — KIỂM TOÁN: MN/MT vs MB ở lane test (cơ chế model AI) + tình trạng áp dụng phương pháp RULES của MB cho MN/MT

> **Loại:** READ-ONLY audit (chỉ kiểm tra + đo, KHÔNG sửa code, KHÔNG đụng official).
> **Data as-of:** 2026-06-13 (đo trực tiếp trên DB live VPS). **Official 4 bảng không bị ghi.**
> **Câu hỏi owner (14/06):** MN/MT ở lane test có cơ chế giống MB (về model AI) không? Đợt áp dụng phương pháp rules MB cho MN/MT đã làm chưa, có cải tiến không?

---

## A. TRẢ LỜI NGẮN

1. **MN/MT KHÔNG dùng cơ chế giống MB** — ngược nhau có chủ ý:
   - **MN/MT = model-AI-driven** (gộp phiếu model qua D_w06 + lọc TOP-K theo miền). DÙNG đồng thuận model.
   - **MB = rule-driven / anti-herd** (V10693/V2): KHÔNG dùng phiếu model (vì đồng thuận model HẠI MB: plurality 10% < ngẫu nhiên 23.7%).
2. **Phương pháp RULES của MB ĐÃ được áp dụng cho MN/MT** (từ 10/06) — dạng **HYBRID** (model + doctrine rules trong prompt), KHÔNG thay hẳn bằng rule như MB. Gồm **V10707 doctrine A/B** + **V10708 rule-ranker**.
3. **Cải tiến: CHƯA kết luận được** — mẫu quá nhỏ (~4-5 ngày): MN doctrine chưa đổi pick nào (=control); MT đổi 1 ngày và thua. Cần đủ ~2 tuần (≈24/06).

---

## B. SO SÁNH CƠ CHẾ (lane test)

| | **MN lane** | **MT lane** | **MB lane (V10693/V2)** |
|---|---|---|---|
| Cơ chế | D_w06 gộp phiếu model + TOP-K | D_w06 + TOP-K (K gắt hơn) | Rule soi-cầu (drive_weight) + bơm board MN/MT same-day |
| Nguồn | bảng `predictions` (**phiếu model AI**) | `predictions` (**phiếu model AI**) | `mb_t2_manual_daily` (rule) + `lottery_results` |
| Dùng model AI? | **CÓ** | **CÓ** | **KHÔNG (anti-herd)** |
| TOP-K | K=25/22 | **K=10** | n/a (rule theo thứ) |
| Lý do thiết kế | đồng thuận model **giúp** MN/MT | (như MN) | đồng thuận model **hại** MB |

→ Bộ model registry dùng chung cho cả 3 miền (~27 model); chỉ **CÁCH dùng** khác: MN/MT tin model, MB bỏ model dùng rule.

---

## C. HIỆU NĂNG LIVE (đo thật trên VPS — per-position + xiên)

### LIVE kể từ 04/06 (10 ngày — out-of-sample thật)
| Miền | Cơ chế | top1 | top2 | top3 | xiên2 | xiên3 | official top1 |
|---|---|---|---|---|---|---|---|
| MB | V2 rule | 30.0% | 20.0% | **0.0%** | **0.0%** | 0.0% | 40.0% |
| MN | model | 30.0% | 30.0% | 50.0% | **20.0%** | **20.0%** | 50.0% |
| MT | model | 40.0% | 10.0% | 30.0% | 0.0% | 0.0% | 40.0% |

### 30 ngày
| Miền | Cơ chế | top1 | top2 | top3 | xiên2 | xiên3 | official top1 |
|---|---|---|---|---|---|---|---|
| MB | V2 rule | 23.3% | 16.7% | 20.0% | 6.7% | 3.3% | 16.7% |
| MN | model | 43.3% | 30.0% | 53.3% | 16.7% | 13.3% | 46.7% |
| MT | model | 36.7% | 33.3% | 30.0% | 6.7% | 3.3% | 30.0% |

**Đọc trung thực:**
- **MN** lane mạnh nhất, xiên 2/3 tốt (16.7%/13.3% trong 30d; 20%/20% trong 10d live).
- **MT** lane 30d nhỉnh official (36.7% vs 30%) nhưng xiên live yếu.
- **MB V2**: 30d vượt official MB yếu (23.3% vs 16.7%) — đúng kỳ vọng; **NHƯNG 10 ngày live: top1 30% < official 40% và xiên 2/3 = 0%** → out-of-sample mới ngang/dưới official, **xiên MB chưa ăn** (điểm cần xử lý). Khớp cảnh báo cũ (90d V2 ≈ official).

---

## D. ÁP DỤNG PHƯƠNG PHÁP RULES MB CHO MN/MT (từ 10/06)

| Thành phần | Vai trò | Trạng thái live |
|---|---|---|
| **V10708 rule-ranker** (`_v10708_mnmt_rule_ranker.py`) | Học tích luỹ + vòng đời + xếp hạng rule MN/MT (mirror `mb_rule_ranker`); cửa sổ **nhấn 12W/16W** (khác MB 8W); ghi `mined_rules_mn_daily`/`mt_daily` | ✅ cron 04:40, **5 snapshot** tới 14/06 |
| **V10707 doctrine A/B** (`_v10707_mnmt_doctrine_shadow.py`) | TREATMENT = gọi lại 7 LLM với prompt **CÓ doctrine rules** (kiểu MB); CONTROL = pick official không doctrine | ✅ cron MN 05:00 / MT 16:50; `mn/mt_rule_context` nạp rule (10/8 dòng) |

**Khác biệt thiết kế quan trọng:** MN/MT áp dụng **HYBRID** = model AI **+ doctrine rules trong prompt** (giữ model vì model giúp MN/MT). KHÁC MB (thuần rule, bỏ model). Mỗi model nhận doctrine rules trong prompt rồi gộp phiếu — đúng kiểu "đơn model + phương pháp rules".

### Kết quả A/B doctrine (treatment vs control) — mẫu còn nhỏ
| Miền | ngày có KQ | treat (CÓ doctrine) | ctrl (KHÔNG doctrine) | doctrine đổi BT | Nhận xét |
|---|---|---|---|---|---|
| **MN** | 4 | 75% (3/4) | 75% (3/4) | **0 ngày** | doctrine ra y hệt control → **chưa tác động** |
| **MT** | 3 | 33% (1/3) | 67% (2/3) | 1 ngày | 06-11 doctrine chốt 16 trượt vs control 54 trúng → **thua ngày đó** |

→ **Quá sớm để kết luận** (mới ~4-5 ngày; owner đã chấp nhận tốn API ~2 tuần). Cần đủ ≥10-14 ngày có KQ (≈24/06).

---

## E. KẾT LUẬN

1. MN/MT **không** giống MB về model AI (model-driven vs rule-driven anti-herd) — đúng thiết kế.
2. Phương pháp rules MB **đã áp dụng** cho MN/MT (V10707 doctrine hybrid + V10708 ranker, từ 10/06), độc lập theo miền, cửa sổ 12W/16W.
3. **Cải tiến chưa chứng minh được**: MN doctrine chưa đổi gì; MT đổi 1 ngày và thua. Mẫu quá nhỏ.
4. MN lane đang tốt nhất; MB V2 ngang official + xiên MB live còn yếu.

## F. ĐỀ XUẤT (chờ owner, chưa làm)
- Đợi đủ 2 tuần (~24/06) → đo lại đầy đủ A/B doctrine MN/MT + so các nhánh model (V10680/V10692) để chốt doctrine có đáng giữ không.
- Đào sâu **vì sao xiên MB live = 0** (top2/top3 chọn lệch chỗ nào).

---

**READ-ONLY — official 4 bảng không bị ghi, không sửa code phiên này. Số liệu đo trực tiếp DB live as-of 2026-06-13.**
Machine-readable: `machine_readable/V10709_MEASUREMENTS.json`.
