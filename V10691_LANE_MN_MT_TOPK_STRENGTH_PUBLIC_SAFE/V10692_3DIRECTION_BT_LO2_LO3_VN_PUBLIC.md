# V10692 — Lane-test 3 hướng song song: Bạch Thủ / Lô 2 / Lô 3 (MN + MT)

Public-safe. Tiếp nối V10691. Không endpoint riêng, không IP, không đường dẫn nội bộ.

> **Đánh số**: phiên MB song song dùng V10679–V10690; phiên lane MN+MT này dùng file `_v10679_/_v10680_` + public V10691. Bước này = **V10692**, nối tiếp, tránh trùng. Hai việc độc lập hoàn toàn.

## 1. Yêu cầu của owner

Thay vì chỉ 1 cách total, chạy **3 hướng output SONG SONG** dạng shadow để có dữ liệu so sánh, mỗi hướng nhắm một loại số:
- **Hướng 1 — Bạch Thủ (1 số)**: cho người chơi đánh 1 con.
- **Hướng 2 — Lô 2 (2 số, "số phụ 2")**: tận dụng số phụ nhiều hơn.
- **Hướng 3 — Lô 3 (3 số, "số phụ 3")**: mạng lưới rộng nhất.

Thuật toán **độc lập theo miền**: MN giữ rộng 25 model (model MN đều nhau), MT lọc gắt 10 model mạnh nhất (MT chênh lệch model lớn).

## 2. Cô lập tuyệt đối (theo chỉ đạo owner)

- **Miền Bắc (MB)**: không đụng cả hai luồng (official + lane).
- **MN + MT luồng official**: không đụng.
- **Chỉ chạy trên lane test**, shadow-only, không đủ điều kiện xuất số chính, chưa duyệt.
- Không đụng 2 thử nghiệm trước (full-pool, top-K) — chạy song song.
- Chỉ ghi vào bảng lane-test.

## 3. Kết quả (backtest ex-ante 30 ngày + đối chiếu thực tế 30 ngày đã xổ)

| Miền | Hướng | Bạch Thủ trúng | Trúng ≥1 (theo độ rộng) |
|---|---|---|---|
| MN | H1 Bạch Thủ (1 số) | **47%** | 47% |
| MN | H2 Lô 2 (2 số) | 43% | 53% |
| MN | H3 Lô 3 (3 số) | 40% | **70%** |
| MT | H1 Bạch Thủ (1 số) | **53%** | 53% |
| MT | H2 Lô 2 (2 số) | 47% | **70%** |
| MT | H3 Lô 3 (3 số) | 43% | **77%** |

Đọc bảng:
- Người chơi thích **1 con chắc** → dùng Hướng 1 (MT 53%, MN 47%).
- Người chơi đánh **2 con** → Hướng 2 (MT trúng ≥1 trong 2 là 70%).
- Người chơi đánh **3 con** → Hướng 3 (MT 77%, MN 70%).
- Càng nhiều số thì xác suất trúng ≥1 càng cao, nhưng Bạch Thủ đơn lẻ giảm — đúng quy luật, để owner cân nhắc khẩu vị rủi ro.

## 4. Phương pháp kiểm chứng

- Walk-forward, không rò rỉ tương lai: xếp hạng model từ cửa sổ quá khứ (60→30 ngày trước), áp lên cửa sổ kiểm tra (30 ngày gần nhất).
- Đối chiếu thêm với 30 ngày đã xổ thật (settle 180 dòng, 0 lỗi).

## 5. An toàn

- 4 bảng official hash GIỐNG HỆT trước/sau (kiểm tra nhiều lần).
- Dịch vụ chạy, đăng nhập 200, theo dõi sức khỏe 16/16 OK.
- 0 đụng MB, 0 đụng official, các thử nghiệm cũ vẫn chạy.
- Lịch tự động 17:10 mỗi ngày (sau giờ dự đoán MT).

## 6. Đề xuất tiếp

- Theo dõi live 7–14 ngày, báo cáo hàng tuần.
- Owner chọn sau: mỗi miền nên lấy hướng nào làm ứng viên chính (tùy khẩu vị: 1 số chắc vs 2-3 số phủ rộng).

## 7. Trạng thái

`PUBLIC_SAFE` — chỉ luồng lane-test; official và MB không bị đụng.
