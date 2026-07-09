# V10789 — OWNER KÝ "CẢ 3" + ESCALATE "XỬ LÝ NGAY HÔM NAY" + THÁO COHERE (09/07/2026 chiều)

## 0. Bối cảnh — lời owner (verbatim, rút gọn)

- 13:0x: **"OK cả 3: K12 + K10/K13 shadow + K11a từ 11/07 (Khuyến nghị)"**
- 14:00 escalate: *"2 ngày liên tiếp theo quan sát anh thấy ML trượt mà model AI là toàn win… ngày 7/6 - 62 1 bầy… ngày 8/6 cũng 1 đàn 81-77 mà không dám đụng ai dè lại ra thật 1 lần nữa — anh cần em xem thật kỹ **xử lý ngay trong hôm nay**. Phương pháp total đang gặp vấn đề trầm trọng: tín hiệu tốt khá ổn đa số ngày nào cũng có nhưng **bắt tệ quá**. Tín hiệu là thật không phải đoán mò… Nhưng total vẫn trượt, **cần 1 lớp gì đó có thể lấy được tín hiệu tốt**, model **cohere không giúp ích gì sao em? ko thì tháo luôn** model đó đi."*

## 1. Forensic bầy AI MB 07-08/07 — owner đúng 100%

Probe READ-ONLY `_v10789_mb_herd_cohere_probe.py` trên DB live:

| Ngày | Bầy AI | Official | Lane MB_OUTPUT_V1 (17:55) |
|---|---|---|---|
| 07/07 | **17/17 model AI có 62 trong top-2** (15 con để top-1; đa số QUA gate bt≥12) — 62 VỀ THẬT | 87 ✗ | **62 ✓ WIN** |
| 08/07 | **14/17 có 77/81** — CẢ HAI VỀ THẬT | 44 ✗ | **77 ✓ WIN** |

**Thủ phạm KHÔNG phải gate** (đa số AI pass) — là **doctrine đầu tháng dom≤10 (V10770)**: thay toàn bộ phiếu bầu bằng plurality của đúng 4 model ML (meta-learning/lstm/xgboost/random-forest) → phiếu của 15-17 model AI trúng **không có đường vào output** hai ngày liền.

ML vs AI theo ngày (BT-hit, MB 10 ngày): AI áp đảo 2 ngày gần nhất (17/17 rồi 14/17) vs ML 2/8 rồi 1/8. MN cùng mẫu ngày 07/07 (AI 12/18 win, official trượt). MT thì bầy mỏng (1/18) — mẫu "AI bầy win" mạnh ở MB+MN, không phải toàn hệ.

## 2. Lớp bắt tín hiệu — 4 việc deploy 14:30 (1 lần restart, guard SAFE)

### 2a. K11a — MB lane promote, ĐÔN START 11/07 → **09/07** (theo lệnh "xử lý ngay trong hôm nay")
- Từ bundle MB tối nay 17:34: **BT + lô-2 official MB = thuật toán `MB_OUTPUT_V1`** (V10692 nguyên bản: top-8 model mạnh nhất 30d **kể cả 10 model shadow**, trọng số top-2 = 0.6).
- Bundle official tạo 17:34 nhưng lane bundle 17:55 → module **tính inline cùng thuật toán** khi lane bundle chưa có. Giả lập pool đúng-thời-điểm-17:34 hai ngày lịch sử: inline chọn **62 (07/07) và 77 (08/07) — y hệt lane bundle**, n_voted=6.
- An toàn: lỗi bất kỳ/thiếu voter (<3) → giữ nguyên champion; log audit `v10789_mb_lane_promote_log` (champion vs challenger, applied, source); kill-switch 1 dòng `_V10789_MB_LANE_PROMOTE_ENABLED=False`; doctrine V10767 vẫn chạy + log shadow để so forward.

### 2b. K10+K13 — Selector shadow 3 bộ chọn (SHADOW_ONLY, 14 ngày forward)
- `SEL_BASE_V1` = replica vote official (thước trung thực) · `SEL_DEDUP_V1` (K10) = 8 model khối ML đếm như MỘT phiếu · `SEL_RECENCY_V1` (K13) = trọng số BT-rate 7d×60% + 30d×40%.
- Causal (rate as-of từng ngày, loại `late=1`), cron chốt TRƯỚC giờ quay 15:56/16:56/17:56 + settle 21:30.
- **Backfill 60 ngày = 531 rows settled:** MB 18% / 20% / **22%** (official thật 15%) · MT 33% / **37%** / **37%** (off 30%) · MN 45% / 45% / **47%** (recency P&L +2.3M — dương duy nhất). Sanity 08/07: SEL_DEDUP MB chọn **77✓** trong khi base 44✗ — đúng kỳ vọng chặn pile-on ML.
- Panel 🗳️ SELECTOR SHADOW tại `/monitoring` (60s) — cột FORWARD từ 09/07 là thước quyết; sau 14 ngày selector nào thắng base + official thật → trình owner đổi bộ chọn official.

### 2c. K12 — Caption "Số này ở đâu ra?" trên /choi
Mỗi số chơi có chú thích nguồn dịch từ method + trace AE: "BT official hôm qua TRẬT — AE echo lại (đòi nợ)" / "BT miền X HÔM NAY vừa trật — AE bắt cầu chéo" / "BT chính thức /du-doan hôm nay"… Display-only, không đổi số.

### 2d. THÁO COHERE (owner pre-approve "không giúp thì tháo luôn")
Bằng chứng quyết định từ `cohere_effectiveness_daily`: **247 mẫu / 83 ngày × 3 miền (17/04→09/07): helped=0 · hurt=0 · no_effect=247**; 16 lần đổi BT cũng không đổi được trúng/trượt; tốn ~1.8s/call. → Flag `_V10789_COHERE_REMOVED=True` trong scheduler (skip call + log 🔌). Bảng đo + registry giữ nguyên làm bằng chứng. Bật lại = flip flag.

## 3. Chuỗi an toàn V105.19

Sandbox test trên DB thật PASS (selector materialize+settle 9 rows đúng; promote 4 case start-gate/lane-bundle/inline/not_mb; source_notes MN render) → backup VPS `/root/backup_v10789_pre/` + local `backups/v10789_pre/` → upload 7 file → py_compile OK → restart 14:30 guard SAFE → smoke health 200 / admin 401 ×3 / journal sạch → cron 4 dòng → backfill 531 → **hash 4 bảng pre/post IDENTICAL** (efebca79 / 2e85228e / 76af5ec6 / 4fc6e4a0).

## 4. Trả lời thẳng câu hỏi owner

1. **"ML trượt mà AI toàn win?"** — Đúng, đo được: MB 2 ngày AI 17/17 và 14/17 BT-hit vs ML 2/8, 1/8. Official trượt vì doctrine chỉ nghe 4 model ML.
2. **"Cần 1 lớp lấy được tín hiệu tốt"** — Lớp đó là **K11a (MB, LIVE tối nay)** — đã chứng minh bắt đúng 62✓/77✓ hai ngày anh bực — và **K13 recency (MN/MT, shadow 14 ngày)**: backfill cho thấy nó là selector duy nhất dương tiền tại MN và +7pp tại MT.
3. **"Cohere không giúp thì tháo"** — Đã tháo. 247 mẫu 0 lần giúp.

## 5. Việc chờ + mốc verify

- Tối nay ~17:35: journal `[V10789-K11a]` + log applied=1; 21:30 settle forward ngày đầu.
- 14 ngày (23/07): tổng kết FORWARD 3 selector → đề xuất đổi bộ chọn official nếu thắng.
- Chờ ký riêng: K9 HERD_FADE · K14 MB same-day-from-train · K8 gemma 429.

*Commit private: e9c7503 · Probe/module files: `_v10789_selector_shadow.py`, `_v10789_mb_lane_promote.py`, `_v10789_mb_herd_cohere_probe.py`, `_v10789_tmp_timing*.py`, `_v10789_deploy.py`*
