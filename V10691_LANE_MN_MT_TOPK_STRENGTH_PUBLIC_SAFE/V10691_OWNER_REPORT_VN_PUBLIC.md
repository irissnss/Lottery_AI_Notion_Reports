# V10691 — Lane-test MN + MT: full-pool vs per-region strength-filtered (số phụ + lọc model yếu)

Public-safe report. Không endpoint riêng, không IP, không đường dẫn nội bộ, không khóa nhà cung cấp.

> **Ghi chú đánh số (quan trọng)**: Báo cáo này gói 2 bước code chạy trong phiên ngày 2026-06-03 trên luồng **lane-test cho MN + MT**. Hai bước đó dùng tên file nội bộ `_v10679_full_pool_d_w06_lane.py` và `_v10680_topk_strength_lane.py`. Do có một phiên làm việc song song khác xử lý **MB** đã dùng nhãn V10679–V10690 cho việc MB, nên báo cáo công khai này dùng nhãn **V10691** để tránh trùng. Tên file code giữ nguyên (`_v10679_`, `_v10680_`) vì cron đang chạy ổn định — đổi tên file đã deploy là rủi ro vô ích. Việc MB và việc MN/MT là **độc lập hoàn toàn**, không đụng nhau.

---

## 1. Vì sao làm việc này

Owner quan sát: luồng lane-test có **rất nhiều model** (25-28 model dự đoán mỗi miền mỗi ngày) nhưng các experiment cũ chỉ gom trung bình **18-20 model** để ra số tổng. Như vậy **lãng phí tín hiệu**, đặc biệt bỏ phí **số phụ** (mỗi model cho 2 số: 1 số chính + 1 số phụ).

Đồng thời owner nhấn mạnh 2 nguyên tắc:
1. Không phải cứ lấy hết model — **trong pool có model tệ**, cần cân nhắc lọc bỏ.
2. **MN và MT độc lập tuyệt đối** — total output mỗi miền phải khác nhau, không miền nào giống miền nào.

Tất cả thay đổi chỉ nằm ở **luồng lane-test (thử nghiệm)** — KHÔNG đụng luồng official, KHÔNG đụng MB.

---

## 2. Phát hiện cốt lõi: cùng 1 model nhưng MN và MT đảo ngược nhau

Đo per-model 30 ngày, điểm tổng hợp = (tỉ lệ trúng số chính ×1.0) + (tỉ lệ trúng số phụ ×0.6):

| Model | Điểm ở MN | Điểm ở MT | Nhận xét |
|---|---|---|---|
| random-forest | 49.3 (đáy MN) | **78.7 (TOP 1 MT)** | MT cực mạnh, MN yếu |
| qwen3.6-plus | **74.7 (top 3 MN)** | 28.0 (đáy MT) | MN mạnh, MT yếu nhất |
| gemini-3.1-pro | **72.4 (top 4 MN)** | 35.9 (MT yếu) | đảo ngược |
| xgboost | 45.3 (đáy MN) | **68.0 (top 7 MT)** | MT mạnh, MN yếu |
| gpt-5.5 | **79.3 (top 1 MN)** | 48.0 (MT trung bình) | MN cực mạnh |

→ Kết luận rõ: **không thể dùng chung một danh sách model cho cả hai miền.** Mỗi miền phải có danh sách model mạnh riêng. Đây chính là điều owner nói "mỗi miền độc lập, không miền nào giống miền nào".

---

## 3. Bước 1 (file `_v10679_`): Full-pool D_w06 — dùng toàn bộ 25-28 model

Tạo 2 experiment lane-test mới: gom **toàn bộ** model có dự đoán, dùng công thức D_w06 = (số chính ×1.0) + (số phụ ×0.6), chọn đuôi điểm cao nhất làm Bạch Thủ.

Kết quả backtest 30 ngày:

| Miền | Bạch Thủ | Lô 2 (≥1 trúng) | Số model trung bình |
|---|---|---|---|
| MN | 47% | 57% | 27 |
| MT | 30% | 57% | 27 |

MN tốt (ngang top cũ, dùng nhiều model nhất → chứng minh full-pool hữu ích cho MN). Nhưng MT chỉ 30% Bạch Thủ — kém vì pool MT có nhiều model rác kéo xuống.

---

## 4. Bước 2 (file `_v10680_`): Top-K lọc theo sức mạnh — KHÁC NHAU theo miền

Vì MT bị nhiễu bởi model yếu, nên thay vì gom hết, ta **xếp hạng model theo sức mạnh trong quá khứ rồi chỉ lấy top-K mạnh nhất**, K khác nhau theo miền.

**Phương pháp kiểm chứng nghiêm ngặt (walk-forward, không rò rỉ tương lai):**
- Cửa sổ HUẤN LUYỆN: 60 ngày trước → 30 ngày trước (xếp hạng model từ dữ liệu quá khứ).
- Cửa sổ KIỂM TRA: 30 ngày trước → hôm nay (áp danh sách đó, đo ex-ante).
- Hai cửa sổ KHÔNG chồng lấn → không có chuyện "biết trước kết quả".

Kết quả:

| Miền | Cấu hình | Bạch Thủ | Lô 2 | So với tốt nhất cũ |
|---|---|---|---|---|
| MN | Top-22, trọng số phụ 0.4 | 43% | 57% | Kém full-pool 4 điểm — MN model đều nhau, lọc ít giá trị |
| **MT** | **Top-10, trọng số phụ 0.4** | **53%** | **70%** | **+8 điểm Bạch Thủ, +17 điểm Lô 2 so với tốt nhất cũ (45%)** |

**MT Top-10 đạt 53% Bạch Thủ / 70% Lô 2 — cao nhất trong toàn bộ lịch sử lane-test MT.** Lý do: MT có chênh lệch model rất lớn (top 79 vs đáy 28), nên loại 18 model yếu giúp giảm nhiễu mạnh, Bạch Thủ bay từ 30% → 53%.

MN ngược lại: model khá đều (top 79 vs đáy 45), lọc ít tác dụng → MN cần hướng khác (đang tìm tiếp).

---

## 5. So sánh tổng thể (backtest 30 ngày, tất cả experiment)

**MT — Top 5:**

| Experiment | Bạch Thủ | Lô 2 |
|---|---|---|
| **MT Top-10 strength-filtered (mới)** | **53%** | **70%** |
| PRIOR_REGION (tốt nhất cũ) | 45% | 53% |
| STRENGTH_WEIGHTED | 38% | 57% |
| NO_TOKEN_HERD_REDUCTION | 34% | 60% |
| AI_CHAIN_PRESERVATION | 37% | 45% |

**MN — Top 5:**

| Experiment | Bạch Thủ | Lô 2 |
|---|---|---|
| HYBRID / ADAPTIVE_EXPLOIT (cũ) | 49% | 49-61% |
| ADAPTIVE_BUDGET_SELECTOR | 48% | 52% |
| Full-pool D_w06 (mới) | 47% | 57% |
| Top-22 strength-filtered (mới) | 43% | 57% |

---

## 6. An toàn — cô lập tuyệt đối

Cả hai file mới đều có "hợp đồng cứng":
- `shadow_only=1`, không đủ điều kiện xuất ra số chính, chưa owner duyệt — chỉ là dữ liệu thử nghiệm.
- KHÔNG ghi vào 4 bảng official (predictions / final_bundles / model_daily_eval / lottery_results).
- KHÔNG đụng MB (đang xử lý ở phiên khác).
- Chỉ ghi vào các bảng lane-test.
- Phòng thủ: gặp lỗi thì bỏ qua, không bao giờ làm sập.

**Kiểm chứng:** Hash 4 bảng official GIỐNG HỆT trước/sau deploy + backfill (kiểm tra 5 lần trong phiên). Dịch vụ chạy, đăng nhập + health trả 200. Bộ theo dõi sức khỏe hệ thống 16/16 OK.

---

## 7. Lịch chạy tự động

- Bước 1 (full-pool): chạy 17:00 mỗi ngày.
- Bước 2 (top-K strength): chạy 17:05 mỗi ngày.
- Cả hai sau giờ dự đoán MT (16:40), nên pool đầy đủ.
- Cả hai chạy SONG SONG với 9 experiment cũ để so sánh công bằng.

---

## 8. Trạng thái hôm nay (2026-06-03, chưa xổ lúc deploy)

- MN bản full-pool + top-22: Bạch Thủ 47 (trùng số official MN hôm nay) — chờ xổ 16:30.
- MT bản top-10: deploy lúc 13:46 còn thiếu pool (5/10 model vì MT chưa predict đủ); cron 17:05 sẽ chạy lại đầy đủ sau 16:40.

---

## 9. Đề xuất tiếp theo

1. **Theo dõi MT Top-10 live 7-14 ngày.** Nếu giữ ≥45% Bạch Thủ live → đề xuất owner cho lên làm "ứng viên chính" cho MT ở lane-test.
2. **Tìm hướng riêng cho MN** (lọc top-K không hiệu quả vì model MN đều): thử combo D_w06 + trọng số theo độ mới (recency), hoặc giữ HYBRID/ADAPTIVE_EXPLOIT làm ứng viên MN.
3. Giữ cả full-pool và top-K chạy shadow để tích lũy dữ liệu so sánh dài hơn (không gây hại).

---

## 10. Trạng thái

`PUBLIC_SAFE` — không IP, không đường dẫn nội bộ, không khóa nhà cung cấp, không lộ cấu trúc DB riêng, không tham chiếu repo riêng. Mọi thay đổi chỉ ở luồng lane-test; luồng official và MB không bị đụng.
