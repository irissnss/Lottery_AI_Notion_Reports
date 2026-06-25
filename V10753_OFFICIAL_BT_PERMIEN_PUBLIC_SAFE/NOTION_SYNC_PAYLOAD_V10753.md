# V10753 — OFFICIAL: BT theo phương pháp tốt nhất per-miền + Lô3 3-càng nới lỏng

**Thời điểm:** 2026-06-26T00:45:00+07:00
**Loại:** THAY ĐỔI OUTPUT OFFICIAL (MN + MB bạch thủ; lô3 cả 3 miền). MT giữ nguyên.
**Trạng thái:** ĐÃ DEPLOY + VERIFY — theo dõi live 5–7 ngày.

---

## 1. Yêu cầu của owner (nguyên văn)

> "TẤT CẢ ĐÃ ĐO LƯỜNG, KIỂM TRA, TÍNH TOÁN RÕ RÀNG RỒI THÌ XỬ LÝ TẤT CẢ LUÔN ĐI EM, HÔM NAY XỬ LÝ TẤT CẢ Ở LUỒNG OFFICIAL ĐI QUÁ MỆT MỎI RỒI, KHÔNG ĐO ĐO HOÀI NỮA ĐÂU. CHÚ Ý BT LÀ SỐ CHÍNH KHẢ NĂNG TRÚNG CAO NHẤT, SỐ NHIỀU HÍT NHẤT, SỐ PHỤ LÀ SỐ ĐỨNG THỨ 2 DỰ PHÒNG HOẶC CHƠI SONG THỦ, XIÊN LÀ CẶP SỐ HIT Ở TRONG CÙNG 1 ĐÀI CAO NHẤT NHA E, 3 CÀNG LÀ SỐ CÓ PHƯƠNG PHÁP ĐÃ VÀ ĐANG LÀM CẦN TÌM HIỂU THÊM CÓ CÁCH NÀO PHƯƠNG PHÁP NÀO GHÉP THÊM 1 SỐ VÀO SỐ BT ĐỂ KHẢ NĂNG 3 CÀNG DỄ HIT NHẤT NHA EM, 3 CÀNG ĐANG NƠI LỎNG LÀ 3 CHỮ SỐ XUẤT HIỆN Ở BẤT KỲ GIẢI NÀO CỦA ĐÀI MIỀN NHA EM"

**Định nghĩa chốt:** BT = số nhiều hit nhất (plurality) · SP = số thứ 2 (song-thủ/dự phòng) · Xiên = cặp cùng 1 đài · Lô3 = 3 chữ số ở bất kỳ giải nào + cần ghép 1 số vào BT.

---

## 2. Đo lường (113 ngày LIVE, có sẵn — KHÔNG đo lại)

So sánh **BT lô-hit** của từng method với **official THỰC TẾ** (final_bundles, đã gồm override cũ) trên cùng ngày, cùng định nghĩa hit (số xuất hiện trong tails các giải).

| Miền | Official LIVE | Method tốt nhất (full-window) | Δ | Ổn định 30/60/90/full |
|---|---|---|---|---|
| **MN** | 44.9% | **specialist 52.7%** | **+7.8pp** | +9.7 / +8.2 / +5.5 / +7.1 |
| **MB** | 23.7% | **prior_region 31.2%** | **+7.5pp** | +19.4 / +11.5 / +12.1 / +8.0 |
| MT | 42.4% | strength_weighted 45.0% | +2.6pp | +13.3 / +8.3 / +5.6 / +3.6 |

**Phát hiện:** override cũ `d_w06` đã **suy thoái về mức baseline** (MN 44.9%≈45.5%; MB 23.7%≈23.2%) → không còn tác dụng. Ứng viên mới thắng official ở **mọi cửa sổ** → không phải overfit.

---

## 3. Thay đổi OFFICIAL (reversible — tái dùng cơ chế override sẵn có, KHÔNG viết lại selector)

- **MN: `d_w06` → `specialist`** — bạch thủ = số được nhiều model có BT-rate ≥ 35% (trailing-60 ngày, chặt `date < hôm nay`, không nhìn trước) bình chọn.
- **MB: `d_w06` → `prior_region`** (chooser mới, copy 1:1 từ lane test) — bạch thủ = số có điểm cao nhất **mà đã xuất hiện trong kết quả MN + MT cùng ngày**.
  - **HỢP LỆ NHÂN-QUẢ:** official MB chạy **17:42**, SAU khi MN (16:30) và MT (17:30) đã xổ → tails MN+MT là dữ liệu **có trước** thời điểm dự MB (đây chính là chữ "SAFE"). Nếu thiếu dữ liệu → tự giữ top1 official.
- **MT: GIỮ `nt_consensus`** — **bảo vệ cỗ máy song-thủ đang lời (+105.7M)**: đổi BT sẽ kéo theo lo2/song-thủ; +3.6pp BT không đáng đánh đổi lợi nhuận đã chứng minh.

- **Lô3 (3-càng) nới lỏng:** trước đây chỉ đếm chữ số đứng trước khi BT là **2 số cuối** của giải → nay đếm **mọi vị trí** BT xuất hiện như chuỗi con trong **mọi giải** (90 ngày), rồi ghép chữ số đứng-trước phổ biến nhất. Khớp đúng định nghĩa "3 chữ số xuất hiện ở bất kỳ giải nào".

- **SP + Xiên (xác nhận, không đổi code):** SP = số mạnh thứ 2 sau BT (song-thủ) ✓ ; Xiên2 = cặp top-2 mạnh nhất.

---

## 4. Kiểm thử + Verify

- **Test local trước deploy:** MB top1 ngoài-tails (`01`) → được nâng lên số trong tails MN+MT (`00`); MN specialist trả bạch thủ (`12`); lô3 trả 3 số hợp lệ (MN bt=11: nới lỏng `111` vs cũ `311`).
- **Deploy:** diff local-vs-server **SẠCH** (chỉ đúng thay đổi V10753); compile OK; restart service OK; `/api/health = 200` (nội bộ + `https://xs.io.vn`); endpoint admin = 401.
- **Khoá an toàn — 4 bảng official IDENTICAL trước/sau** (không regen quá khứ):
  - `predictions 1b0ad34ad7e7cad6`
  - `final_bundles f60a97d89581164c`
  - `lottery_results 7fe6f7fddcf0b8fc`
  - `model_daily_eval 74571578c8fe0848`
- Áp dụng từ chu kỳ tới: **MN 04:15, MT 16:42, MB 17:42**.

---

## 5. Theo dõi & Rollback

- **Theo dõi 5–7 ngày:** MN BT vs 44.9% (kỳ vọng ~52%); MB BT vs 23.7% (kỳ vọng ~31%); lô3 3-càng hit-rate; MT song-thủ P&L (không đổi).
- **Rollback (tức thì):** đổi chooser MN/MB về `"d_w06"` (đường cũ còn nguyên) hoặc `enabled=False`; lô3 phục hồi từ backup.

---

*Public-safe: không chứa secret/API key/IP/đường dẫn deploy. Chi tiết code + backup nằm ở repo private Lottery_AI_Test (commit V10753).*
