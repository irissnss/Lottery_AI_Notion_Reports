# V10790-B — Báo cáo chi tiết: Bập bênh 2 mặt (model-pool vs /choi) — 09/07/2026 tối muộn

## 1. Câu hỏi owner (18:59, verbatim)

> "Miền Bắc nay lại về ? khó hiểu đúng thật sự khó hiểu , toàn bộ các đơn model đa số trật hết mà /choi lại trúng, hôm qua đa số đơn model dự đoán ok mà /choi lại trượt , rồi ngày 7/06 cung thế đa số đơn model trúng là output /choi trượt. . thật lạ có cách nào khống chế cần bằng ổn áp hơn không em? dựa vào dữ liệu live có tìm được cơ chế nào không em ? Các phân tích, xử lý sandbox của em như thế nào rồi có khả quan không em? đề xuất xử lý là gì em?"

## 2. Xác minh 3 ngày MB owner nêu (probe 1)

| Ngày | % model trúng top-1 | Bầy lớn nhất | /choi AE | Official |
|---|---|---|---|---|
| 07/07 | 76% (25 model) | 17 con | [16,59] ✗ | 87 ✗ |
| 08/07 | 60% (25 model) | 9 con | [59] ✗ | 44 ✗ |
| 09/07 | **4%** (26 model) | 9 con | **[13,64] ✓VỀ** | 16 ✗ |

Đúng như owner quan sát: bể model càng "nóng" thì /choi (AE) càng trượt, bể càng "trắng" thì AE càng về.

## 3. Thống kê 60 ngày — bập bênh là CÓ THẬT (probe 1+2)

Bucket ngày theo % model trúng top-1: TRẮNG <10% · VỪA 10-30% · NÓNG ≥30%.

### Hit-rate cặp 2 số theo bucket (AE = echo //choi; OUTPUT_V1 = vote top-K mạnh nhất 30d)

| Miền | Bucket TRẮNG | Bucket NÓNG | Union ≥1 mặt trúng |
|---|---|---|---|
| MN (n=57) | AE 100% (2) vs vote 0% | AE 72% vs vote 81% (36) | **88%** |
| MT (n=60) | AE 33% (6) vs vote 0% | AE 69% vs vote 81% (36) | **82%** |
| MB (n=36) | **AE 67% (12) vs vote 8%** | **vote 86% (14) vs AE 29%** | **78%** |

Cơ chế: AE chọn số echo/ngược bể (số vừa thua, cầu chéo) — khi kết quả "lệch kịch bản" mà cả bể mù thì AE bắt được; OUTPUT_V1 dồn theo model mạnh — khi kết quả "thuận bể" thì vote ăn đậm. Hai mặt gần như không trùng số (overlap 3/36 ngày ở MB).

## 4. Vì sao KHÔNG đề xuất switch theo ngày (kết quả trung thực)

1. **Regime không dự đoán được:** hôm qua TRẮNG → hôm nay TRẮNG chỉ 7/18; ma trận chuyển gần base-rate → không có "mùa" để bám.
2. **Mọi rule switch causal đều thua always-AE** (backtest 60d MB, chỉ dùng info biết trước giờ quay):
   - Switch theo share hôm qua: 49% · Follow-streak: 37% · Anti-streak: 33% · Anti-herd (bầy ≥10): 44% · Overlap-consensus: 42% — luôn-AE 47%, nên mọi rule đều trong sai số hoặc tệ hơn.
3. **Số "đồng thuận" 2 mặt cùng chọn không mạnh hơn:** 60d MT 3/11=27%, MB 0/3, MN 1/2 — trùng số không phải tín hiệu tin cậy.

Kết luận kỹ thuật: bập bênh là anti-correlation CÙNG NGÀY (biết sau giờ quay), không khai thác được bằng switch. Cách khai thác đúng là giữ CẢ HAI mặt chạy song song với vai trò tách bạch.

## 5. Cơ chế "ổn áp" — đã ở đúng cấu hình từ hôm nay

| Mặt | Vai | Trạng thái |
|---|---|---|
| Official /du-doan MB | VOTE (MB_OUTPUT_V1, K11a) | LIVE từ 09/07 |
| Official /du-doan MT | VOTE (MT_OUTPUT_V1, K15) | LIVE từ 10/07 |
| Official /du-doan MN | Vote thường (đang khoẻ, 45%) | Không đổi |
| /choi cả 3 miền | ECHO (AE, lock tuần) | Không đổi |

Union 2 mặt 78-88% ngày có ít nhất 1 mặt trúng — panel mới giám sát con số này.

## 6. Deploy V10790-B

- Khối `seesaw` (`_seesaw_view`) vào `_v10773_three_layer_scoreboard.py`: bucket + hit từng mặt + union + latest day, 60d, DIAGNOSTIC-ONLY.
- Panel **⚖ BẬP BÊNH 2 MẶT** vào `/monitoring` (cạnh ⏱ MỐC & NHỊP, auto-refresh 60s sẵn có).
- Sandbox PASS (số khớp probe từng miền); verify module production trực tiếp MN 88/MT 82/MB 78.
- Restart 19:0x guard SAFE; smoke health 200, admin no-auth 401; hash 4 bảng pre/post IDENTICAL (9654/396/15042/9440 rows).
- Không đổi bất kỳ số official/lane//choi nào.

## 7. Tình trạng sandbox/shadow đang chạy (trả lời "có khả quan không?")

| Lớp | Trạng thái | Kết quả tới nay |
|---|---|---|
| K11a MB_OUTPUT_V1 → official | LIVE ngày 1 (09/07) | 16✗ nhưng champion 86 cũng ✗ (hoà, ngày không tín hiệu — cả bể 1/26 trúng); 2 ngày trước đó lane bắt 62✓ 77✓ |
| K15 MT_OUTPUT_V1 → official | LIVE từ 10/07 | Hôm nay lane 84✓ trong khi official 59✗ — đúng hướng |
| K10/K13 selector shadow | Forward ngày 1/14 | Backfill 60d: dedup/recency thắng base cả 3 miền (MB 20-22% vs 18%; MT 37% vs 33%; MN 47% vs 45%) |
| Cohere | ĐÃ THÁO (09/07) | 247 mẫu helped=0 |
| K9 herd-fade, K14 MB same-day retrain | Chờ ký | — |

## 8. Probe files (private repo)

`web/backend/_v10790_seesaw_probe.py` · `_v10790_seesaw_probe2.py` · `_v10790_seesaw_probe3.py` (READ-ONLY, chạy qua sandbox VPS).
