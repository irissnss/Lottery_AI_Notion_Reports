# BÁO CÁO TỔNG V10787 — AUDIT LIVE 07-08/07 + ĐỐI CHỨNG 3 MẶT (OFFICIAL / LANE / CHOI)

Ngày: 2026-07-08 (chiều) · Phiên: V10787 · FU: `FU-V10787-THREE-SURFACE` · governance seq: 242

Câu hỏi owner (08/07, nguyên văn): *"Điều lại lùng là office 1 đường , lane test 1 nẻo , và /choi 1 kiểu . Mỗi cái trúng mỗi kiểu. Em không tìm ra được điểm mạnh để có output hoàn hảo nhất ah em"*

---

## PHẦN 1 — TRẢ LỜI THẲNG CÂU HỎI

### 1.1 Vì sao 3 mặt "mỗi cái một kiểu" — đó là THIẾT KẾ, không phải lỗi

| Mặt | Số lấy từ đâu | Vai trò |
|---|---|---|
| **OFFICIAL /du-doan** | Weighted voting 26 model (+ MB doctrine đầu tháng) | Số publish chính thức |
| **LANE test** | 20+ method thử nghiệm chạy shadow mỗi ngày | Phòng thí nghiệm — CHƯA vào official |
| **/choi** | Method ĐÃ KHÓA theo tuần (owner ký): MN=BT1-official · MT=AE · MB=AE | Tiền thật — chơi 1 method, bám cả tuần |

Số đo (từ 10/05, cùng thước /choi: song thủ × 50 điểm × tất cả đài, 1 ăn 98k, cost 18k/27k):
**3 mặt gần như KHÔNG BAO GIỜ chọn trùng số** — same-pick: MN **0/57 ngày** · MT **3/58** · MB **0/34**.
Selector khác nhau → số khác nhau → "mỗi cái trúng mỗi kiểu" là hệ quả toán học, không phải hệ thống loạn.

### 1.2 Bù trừ có thật — nhưng "trộn thành 1 output hoàn hảo" thì THUA TIỀN

Đối chứng BT official vs BT lane-AE (method /choi đang chơi), từ 10/05:

| Miền | n ngày | Official hit | Lane hit | Cả 2 trúng | Chỉ OFF | Chỉ LANE | Cùng trượt | Trần chọn-đúng-mặt |
|---|---|---|---|---|---|---|---|---|
| MN | 57 | 45.6% | 50.9% | 12 | 14 | 17 | 14 | **75.4%** |
| MT | 58 | 31.0% | 39.7% | 8 | 10 | 15 | 25 | **56.9%** |
| MB | 34 | 20.6% | 32.4% | 2 | 5 | 9 | 18 | **47.1%** |

Trần 75/57/47% nghe hấp dẫn — nhưng đó là **hindsight** (biết trước mặt nào trúng mới chọn được). Cách khả thi duy nhất để "ăn cả 2 mặt" là đánh CẢ 2 số mỗi ngày — và em đo luôn P&L cặp gộp [off-BT, lane-BT]:

| Miền | Cặp OFFICIAL | Cặp LANE | Cặp GỘP off+lane | Verdict |
|---|---|---|---|---|
| MN | -14.5M | **+47.2M** | +30.6M | Gộp THUA lane đơn |
| MT | **+31.7M** | +20.6M | +8.2M | Gộp THUA official đơn |
| MB | -2.5M | **+25.8M** | +1.3M | Gộp THUA lane đơn |

**Cả 3 miền: gộp đều thua mặt tốt nhất** — vì tiền cược x2 (2 số × tất cả đài) nuốt sạch lợi ích bù trừ. Cửa sổ gần (17/06→nay) cũng cùng kết luận (MN -5.1 · MT +8.9 · MB -12.6 khi gộp).

### 1.3 Vậy "điểm mạnh" thật nằm ở đâu?

**Không có output hoàn hảo bằng cách trộn. Điểm mạnh = CHỌN ĐÚNG MẶT THEO MIỀN, rồi bám — chính là cơ chế weekly-lock /choi đang làm.** Và lock tuần 06/07 anh đã ký KHỚP với data 21 ngày gần:

| Miền | Lock tuần 06/07 (anh ký) | Data 21d gần nói gì | Khớp? |
|---|---|---|---|
| MN | `MN_BT1_OFFICIAL_V1` | Official +8.6M/21d · lane AE **-6.1M/21d** (nguội rõ sau khi +35.9M nửa đầu) | ✅ ĐÚNG mặt |
| MT | `MT_ADAPTIVE_EXPLOIT_V1` | Official +30.7 vs lane +30.7 — HOÀ 21d | ✅ chấp nhận |
| MB | `MB_ADAPTIVE_EXPLOIT_V1` | Lane **+36.4M/21d** vs official **-7.7M/21d** — lệch nặng | ✅ ĐÚNG mặt |

Ý nghĩa thực dụng: mặt YẾU nhất hiện nay là **MB official** (doctrine đầu tháng đang 1W-1L, scorecard theo dõi riêng) — nhưng /choi KHÔNG chơi MB official nên tiền thật không dính. MN lane AE nguội là lý do data ủng hộ việc anh chuyển MN sang BT1-official tuần này.

### 1.4 Công cụ mới để anh nhìn thấy điều này mỗi tuần (deploy live 14:01 hôm nay)

Panel **SO GĂNG 3 TẦNG** tại `/monitoring` giờ có thêm khối **⚔ ĐỐI CHỨNG official vs lane-AE** cho từng miền: hit % 2 mặt · bù trừ (cả2/chỉOFF/chỉLANE/cùng trượt) · trần chọn-đúng-mặt · P&L 3 cặp (off/lane/gộp) · verdict `GỘP THẮNG / gộp KHÔNG hơn — đừng trộn`. Quy trình đề xuất: **mỗi thứ 2 trước khi khóa tuần, nhìn khối này + hàng BỀN để chọn mặt cho từng miền.** Nếu tương lai `merge_wins=True` xuất hiện 2 tuần liên tiếp ở miền nào, em sẽ trình phương án cặp gộp cho miền đó — hiện tại cả 3 = False.

---

## PHẦN 2 — AUDIT LIVE 07-08/07 (cùng phiên, hỏi trước đó)

- **Kết quả 07/07:** BT 3 miền đều LOSE (MN 30 · MT 63 · MB 87). MT lạnh sâu: 0/26 model WIN. MB: doctrine ML-plurality chọn 87 trong khi plain-vote top1=62 TRÚNG (12 model WIN với 62) → **scorecard doctrine 06-07/07: 1W-1L**, backtest owner-ký +30.8M, 1 ngày thua chưa đủ revert — theo dõi hết dom≤10.
- **Coverage 07/07:** 78/78 rows (26 model × 3 miền) · 1 empty duy nhất = gemma MB 429 (K8 CHỜ KÝ) · **late-fill cứu ca thứ 2**: gemma MT timeout 439s → kết quả về ghi late=1 lúc 10:00 (model khác qwen — cơ chế generalize đúng).
- **Vật theo dõi cũ:** kimi rt=1 KHÔNG tái diễn · glm-5.1 sạch 2 ngày · gpt-5.5 sạch tiếp.
- **Hạ tầng:** T-10 đúng giây 2 ngày · watchdog 96+ tick 0 alert · MDE 78 rows · verify 0 pending · cron gate 07:30 log ra file từ 08/07 (`all_pass=true`) · 0 restart · 0 ERROR.
- **/choi tuần 06/07 sau 3 ngày:** MN BT1 +1.7M · MT AE -2.8M · MB AE -3.2M (đều 1W-2L — mẫu nhỏ, đầu tuần).

---

## PHẦN 3 — THAY ĐỔI KỸ THUẬT + AN TOÀN

| Mục | Chi tiết |
|---|---|
| Code | `_v10773_three_layer_scoreboard.py`: thêm `_vs_lane()` + khối `vs_lane_ae` per region (READ-ONLY SELECT, không bảng mới) · `monitoring.html`: render khối đối chứng trong panel sẵn (auto-refresh 60s sẵn, API `require_admin` + `no-store` sẵn) |
| Sandbox-first | Test module mới trên DB thật READ-ONLY tại `/root/sandbox_v10785/v10787_mod/` PASS (3 miền đủ keys, số khớp probe) TRƯỚC khi deploy |
| Deploy | 14:01 08/07 — ngoài cửa sổ live (MN sáng xong 04:xx; T-10 MN 15:45 chưa tới) · restart `lottery.service` · smoke health=200 · admin unauth=401 · monitoring=401 |
| Hash 4 bảng | pre = post IDENTICAL: predictions 9538 `0e39714e` · final_bundles 391 `cde8625c` · lottery_results 15029 `d0564050` · model_daily_eval 9362 `59b55081` |
| Rollback | `/root/backups/v10787_pre_20260708_140006/` (2 file) |
| Nguyên tắc | DIAGNOSTIC-ONLY — /du-doan, bundle writer, selector official KHÔNG đổi; đề xuất đổi method lock luôn qua chữ ký anh |
| Probes (local, READ-ONLY) | `_v10787_2day_audit.py` · `_v10787_three_surface_gap.py` · `_v10787_cross_pair_pnl.py` · `_v10787_lock_probe.py` · `_v10787_selector_probe.py` · `_v10787_mb_selector.py` |

## PHẦN 4 — CHỜ KÝ (không mới trong phiên này)

- **K8 gemma MB 429** (từ V10785): K8a slim-context riêng gemma MB (đề xuất) / K8b nâng tier Google / K8c chấp nhận không phủ.
- K1–K7: bảng trong `BAO_CAO_TONG_V10785.md`.
- Nhắc lịch: **CP-L5 (LEAN_HARVEST) hard deadline 2026-07-09 — ngày mai.**
