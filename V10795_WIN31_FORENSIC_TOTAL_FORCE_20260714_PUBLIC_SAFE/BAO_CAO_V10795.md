# BÁO CÁO V10795 — "CON 31 TỪ ĐÂU RA" + TỔNG LỰC 3 MIỀN × 3 LUỒNG + BACKTEST COMBO "89-31"

- **Ngày:** 2026-07-14 sáng (giờ VN) — READ-ONLY, không code change.
- **Yêu cầu owner (09:26):** "Hôm qua anh mới vừa win 31 ở MB — số này từ đâu ra, xuyên suốt /choi thì đó là may mắn hay quy luật gì? Nếu ra 89-31 thì quá đẹp. Xem tổng lực 3 miền, 3 luồng lane/official//choi. Bài học đúc kết và đề xuất chỉnh sửa thật an toàn, cải tiến nâng cao tỷ lệ trúng."
- **Dữ liệu:** sync live `artifacts/live_sync/20260714_092825`; 5 probe `_v10795_*.py`.

## 1. Con 31 từ đâu ra — KHÔNG phải may mắn, là echo cầu chéo có cơ chế

Timeline causal ngày 13/07:

| Giờ | Sự kiện |
|---|---|
| 17:30 | MT xổ — BT official MT = **31 TRẬT tại MT** |
| 17:35 | AE MB sinh bundle: bắt lại 31 theo flow `cross_region_sameday` (trace: `src_region=MT`, lift +5.5pp trên 58 lần thua/90 ngày) + 41 theo flow `per_model_lag1` (meta-learning BT 41 hôm trước trật, lift +8.6pp) |
| 17:36 | /choi khóa cặp [41, 31] |
| 18:15 | MB xổ: **31 VỀ** (41 trượt; 89 của official cũng VỀ) |

Đây chính là tín hiệu **cầu chéo MT→MB +7pp** đã đo và công bố ở V10788 — AE được thiết kế để "đòi nợ" đúng những số vừa thua. Caption K12 trên /choi ("BT miền MT HÔM NAY vừa trật — AE bắt cầu chéo") hiển thị cơ chế này từng ngày, từng số.

## 2. Xuyên suốt /choi: quy luật tới mức nào? (90 ngày, hit lô)

| Miền | Flow | Trúng/đề cử | Tỷ lệ |
|---|---|---|---|
| MB | cross_region_sameday (cơ chế của con 31) | 19/70 | **27%** |
| MB | per_model_lag1 (cơ chế của con 41) | 86/308 | **28%** |
| MT | các flow echo | — | 34-45% |
| MN | các flow echo (AE MN đã retire by-design) | — | 51-81% |

Nền mù ~24.8%/số. Kết luận trung thực: từng-số lift **có thật nhưng khiêm tốn** (MB +2-3pp); /choi lãi bền là nhờ **tổng hợp nhiều flow + verdict guard (NGHỈ/CÂN NHẮC/CHƠI) + khóa tuần chống nhảy method** — một HỆ quy luật, không phải một quy luật đơn lẻ. Pick thực AE 90d: MB leg1 36%/leg2 26% · MT 42%/35% · MN 51%/47%.

## 3. "Nếu ra 89-31 thì quá đẹp" — backtest nghiêm 5 biến thể cặp

Hôm qua cặp 89-31 cho 2 nháy +7.1M thật. Nhưng backtest causal toàn kỳ chung (bundle trước cutoff):

**MB — MB_OUTPUT_V1 × AE (39 ngày, 05/06→13/07):**

| Biến thể | P&L | Ăn-ngày | Nửa đầu / nửa sau |
|---|---|---|---|
| **V0 top1+top1 (fix V10794 đã deploy)** | **+41.7M** | **24/39 = 62% cao nhất** | **+12.4M / +29.3M — 2 nửa đều dương** |
| V1 "89-31" (m1top1+m2top2) | +39.5M | 18/39 | **−9.4M** / +48.9M — nửa đầu ÂM |
| V2 AE-pair nguyên | +49.3M | 20/39 | +2.6M / +46.7M — dồn nửa sau |
| V3 lane-pair nguyên | +22.1M | 18/39 | +22.2M / −0.1M |

**MT — HYBRID × STRENGTH (64 ngày):** V0 **+75.6M** đè bẹp V1 +35.6M và V2 −8.2M.

Per-leg làm nền: leg1 ≥ leg2 ở hầu hết method (MT STRENGTH leg2 **−11.3M**; ngoại lệ duy nhất AE MB leg2 +22.2M nhờ echo chéo). Tuần 06-12/07 V0 cũng đã thắng V2 (+15.4 vs +13.2M).

**Kết luận: GIỮ V0 (top1+top1).** "89-31" là hindsight 1 ngày — đúng bài học V10792: cặp đẹp hôm qua ≠ quy luật; phải đo 39-64 ngày và bắt buộc 2 nửa cùng dương mới đổi. May mắn có hậu: fix race sáng nay (V10794) tình cờ chính là biến thể bền nhất.

## 4. Tổng lực 3 miền × 3 luồng (30 ngày, kinh tế cặp)

| Luồng | MN | MT | MB |
|---|---|---|---|
| OFFICIAL (/du-doan) | +2.3M (BT 40%) | **+30.3M** (18/30 ăn) | +2.3M (**BT 13% — mắt xích yếu**) |
| LANE tốt nhất | MN_OUTPUT −12.4M (cả dàn âm) | AE +35.2M · HYBRID +32.3M | **AE +57.5M mạnh nhất hệ** · OUTPUT_V1 +21.9M |
| /CHOI (stake-adj) | +8.4M | **+45.2M** | +14.5M |

- /choi tổng **+68.1M/30d** — mặt hái tiền chính, MT là động cơ.
- MB official BT 13% vẫn là chỗ yếu → K11a (`MB_OUTPUT_V1`) đang trị đúng bệnh, chốt 16/07.
- MN tuần lạnh 09-13/07 (BT official 1/5): guard E5 làm việc **đúng thiết kế** — NGHỈ 2 ngày né trọn, CÂN NHẮC nửa vốn 2 ngày → cả tuần chỉ −1.2M. Không sửa gì.

## 5. Bài học đúc kết + đề xuất

1. **Tách vai đang chạy đúng:** 13/07 MB cả 2 mặt cùng thắng — official (vote bắt bầy) ra 89✓, /choi (echo đòi nợ) ra 31✓. Seesaw union hoạt động như thiết kế.
2. **Không đuổi cặp-đẹp-hôm-qua:** chuẩn mới từ phiên này — mọi đề xuất đổi cặp /choi phải qua backtest ≥39 ngày, 2 nửa cùng dương.
3. **Không code change phiên này** — V0 giữ nguyên; nếu muốn tăng độ phủ echo (flow-weight AE), xét SAU checkpoint 16-17/07.
4. Nhắc lịch: 14/07 tối verify lock combo đủ 2 leg (FU-V10794) · 16/07 K11a d7 · 17/07 K15 d7 · 23/07 selector 14d · CP-L6 chờ anh quyết (đề xuất dời 19/07).

## 6. Governance

- CHANGELOG V10795 + SSOT + `FU-V10795-WIN31-FORENSIC` + AUTOMATION_STATE seq 256 + HISTORY.
- READ-ONLY: không deploy, không restart, hash 4 bảng không đổi.
