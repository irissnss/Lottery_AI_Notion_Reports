# V10693 — PHÂN TÍCH CHI TIẾT CHO AI REVIEW (trước khi deploy)

> Mục đích: cung cấp đầy đủ số liệu + thiết kế để các tool AI phân tích/critique **trước khi** deploy lên VPS lane.
> **Trung thực tuyệt đối — KHÔNG tô hồng.** Mọi số đo trên DB hiện tại (as-of 2026-06-03), official 4-table ZERO-DRIFT PASS.
> Code (private, không public): `web/backend/_v10693_mb_perpos_predictor.py`. Full per-date: `evidence/V10693_WALKFORWARD_DETAIL.json`.

---

## 0. TÓM TẮT TRUNG THỰC (đọc kỹ trước khi kết luận)

- Method per-position rule-driven **vực BT MB từ "dưới ngẫu nhiên" lên "ngang/trên ngẫu nhiên"**, nhưng **mức lợi phụ thuộc cửa sổ đo**:
  - **60 ngày:** top1 **25.0%** vs official **13.3%** (+11.7pp, ~1.9×).
  - **90 ngày:** top1 **22.2%** vs official **21.1%** (+1.1pp — **gần như HÒA**).
- Nghĩa là: cửa sổ 60d official rơi vào giai đoạn đặc biệt tệ (13.3%); mở rộng 90d thì official hồi về 21.1% và method chỉ ngang. **Không phải thắng áp đảo.**
- Giá trị thật của method: (1) tín hiệu **độc lập, rule-based, anti-herd** (không dính đồng thuận model vốn phản tác dụng cho MB); (2) **top2 độc lập tốt (25.6% @90d)** dùng cho xiên; (3) ổn định trên/ngang ngẫu nhiên ở hầu hết các thứ.
- **Đây là lý do cần 2 tuần live shadow + AI review** trước khi quyết định thay official.

---

## 1. VẤN ĐỀ GỐC (từ verify V1–V7)

- MB BT official **dưới ngẫu nhiên**: 6.7%/30d, 13.3%/60d, 21.1%/90d vs random 23.7%.
- Nguyên nhân: chooser `d_w06` khuếch đại **đồng thuận model**, mà đồng thuận MB **phản tác dụng** (plurality 10% < random 23.7%); `BUNDLE_SKEW` 17/28 ngày (số trúng có trong vote nhưng bundle chốt sai); `v104 REQUIRED_IN_PROMPT=0`.
- Không có per-number method (1 ranked list + override chỉ thay BT).

---

## 2. THIẾT KẾ METHOD (đầy đủ để critique)

**Cơ chế học tập tích luỹ xếp hạng (mb_rule_ranker + _v10689):**
1. Mỗi ngày re-rank PRODUCTION 35 + MANUAL 77, **gắn theo từng THỨ** (target_weekday), composite nhấn 8 tuần + lifecycle.
2. `_v10689` rolling re-measure 90 ngày → `drive_weight ∈ [0,1]` mỗi rule (loại mining gap 2026-05-04..05-31).
3. Ngày dự đoán → lấy **top rules của THỨ hiện tại**, `drive_weight>0`, bỏ forward-audit confirm-only.

**Sinh số từng vị trí (pseudo-code):**
```
score = {}
for rule in top_rules_of_weekday(date):           # MANUAL soi-cầu, drive_weight>0
    sset = apply_transform(rule, source_draw(date - rule.lag))   # tập đuôi rule bắn (union đa đài)
    w    = rule.drive_weight / sqrt(|sset|)        # đặc hiệu: rule bắn ít đuôi → mạnh hơn
    for tail in sset: score[tail] += w
for region in (MN, MT):                            # MB xổ cuối → same-day hợp nhân quả
    score[ DB_tail(region, date) ] += 0.50         # bonus cấu trúc đuôi ĐB cùng ngày
ranked = sort_desc(score)
top1, top2, top3 = ranked[0], ranked[1], ranked[2]   # mỗi vị trí 1 số khác nhau
```
- **Anti-herd theo cấu trúc:** KHÔNG dùng phiếu AI/model (vốn phản tác dụng cho MB).
- BT/số phụ 1/số phụ 2 = top1/top2/top3.

---

## 3. WALK-FORWARD TRUNG THỰC (không look-ahead, recompute weight mỗi ngày)

| Cửa sổ | n | top1 (BT) | top2 | top3 | xiên2 | xiên3 | coverTop4 | **official top1** |
|---|---|---|---|---|---|---|---|---|
| 60 ngày | 60 | **25.0%** | 26.7% | 15.0% | 11.7% | 1.7% | 63.3% | **13.3%** |
| 90 ngày | 90 | **22.2%** | 25.6% | 18.9% | 8.9% | 1.1% | 66.7% | **21.1%** |

- random 1-số = 23.7%. → 90d: method ≈ ngẫu nhiên (22.2%) và ≈ official (21.1%).
- top2 ổn định 25.6–26.7% (trên ngẫu nhiên) — hữu ích cho xiên.
- top3 yếu (15–18.9%) — **điểm yếu cần cải thiện**.

---

## 4. PER-WEEKDAY (90 ngày) — method vs official

| Thứ | n | method top1 | method top2 | method top3 | official top1 | Nhận xét |
|---|---|---|---|---|---|---|
| T2 | 13 | 23.1% | 30.8% | 15.4% | 23.1% | hòa top1, top2 tốt |
| T3 | 13 | 23.1% | 30.8% | 7.7% | 23.1% | hòa top1, top3 kém |
| T4 | 13 | 15.4% | 38.5% | 23.1% | 15.4% | top1 thấp (ít rule), top2 rất tốt |
| T5 | 12 | 25.0% | 8.3% | 16.7% | 16.7% | top1 hơn official, top2 kém |
| T6 | 13 | 23.1% | 15.4% | 15.4% | 23.1% | hòa (T6 không có BH-pass) |
| T7 | 13 | 15.4% | 38.5% | 30.8% | 23.1% | top1 thua official, top2/3 tốt |
| CN | 13 | 30.8% | 15.4% | 23.1% | 23.1% | top1 hơn official |

→ Bức tranh **lẫn lộn theo thứ**: method mạnh top2 ở T2/T3/T4/T7; top1 hơn ở T5/CN; thua ở T7; T4 ít rule (5) nên top1 thấp.

---

## 5. TUNING CONFIG (lưu ý: as-of weights = có look-ahead, chỉ để so SÁNH TƯƠNG ĐỐI khi chọn config)

| Config | 60d top1 | top2 | top3 | xiên2 |
|---|---|---|---|---|
| base (Σ drive_weight) | 41.7 | 28.3 | 28.3 | 13.3 |
| inv_size | 38.3 | 30.0 | 35.0 | 16.7 |
| **invsqrt + struct0.5 (CHỌN)** | 40.0 | 31.7 | 33.3 | 20.0 |
| invsqrt+struct+antiherd | 38.3 | 30.0 | 28.3 | 16.7 |

→ Chọn `invsqrt + struct0.5` (cân bằng 3 vị trí + xiên2 cao nhất). **Cảnh báo:** các số mục 5 dùng weight as-of → cao hơn thực tế; số CHUẨN là walk-forward mục 3.

---

## 6. GIỚI HẠN & RỦI RO (phải cân nhắc khi review)

1. **Phụ thuộc cửa sổ:** lợi thế top1 lớn ở 60d nhưng gần như biến mất ở 90d (official hồi phục). Không chắc thắng bền.
2. **Mẫu nhỏ + nhiễu:** mỗi thứ chỉ ~12-13 ngày/90d; số hit 2-5 → sai số lớn.
3. **top3 yếu (15-19%):** chưa đạt "mỗi vị trí đủ mạnh" cho xiên3.
4. **T4 ít rule (5 drive>0):** ngày mỏng rule → top1 thấp (15.4%).
5. **Bonus struct same-day MN/MT = giả định** đuôi ĐB cùng ngày liên quan MB — cần kiểm thêm độ bền.
6. **Backfill shadow dùng weight as-of** (top1 hiển thị 40% trong bảng lane) — KHÁC walk-forward 25%; khi đọc UI lane cần hiểu đây là preview, không phải kỳ vọng live.
7. Chưa có dữ liệu **out-of-sample LIVE** — đó là mục đích 2 tuần shadow.

---

## 7. CÂU HỎI MỞ CHO AI REVIEW

1. Với top1 90d chỉ ngang official (22.2% vs 21.1%), có nên deploy thay BT không, hay chỉ dùng method làm **nguồn top2/xiên bổ trợ** (top2 ổn định hơn)?
2. Cách cải thiện **top3**? (co-occurrence với top1? rule riêng cho vị trí 3? diversity theo họ số?)
3. `struct_bonus=0.5` cho same-day MN/MT — nên tăng/giảm, hay thêm các giải khác ngoài ĐB?
4. Có nên **blend** method (rule-driven) với official (model) thay vì thay hẳn — vì 2 nguồn độc lập?
5. T4/T6/T7 (ít/không BH-pass rule) xử lý sao — fallback structural mạnh hơn?
6. Tiêu chí PASS/FAIL sau 2 tuần live nên là gì (top1 ≥ official? xiên2 ≥ 2× official? per-weekday)?

---

## 8. TRẠNG THÁI

- **Local:** method + register + backfill 60 ngày + walk-forward 60/90d xong. Official ZERO-DRIFT PASS; MN/MT bất biến.
- **VPS:** CHƯA deploy (owner chọn xem report trước). Deploy lane-only sẵn sàng khi owner OK.
- **Evidence:** `evidence/V10693_WALKFORWARD_DETAIL.json` (full per-date 60+90d + per-weekday), `evidence/V10693_WALKFORWARD_PERPOS.json`, `evidence/EVIDENCE_QUERIES.md`.
