# V10790 — K15 MT LANE PROMOTE + METRIC LẶP-SỐ-VỪA-THUA + FORWARD DAY-1 (09/07/2026 tối)

## 0. Lời owner (verbatim, rút gọn)

- 17:32: *"Tiếp tục MT tơi bời với 59 nữa. việc số ngày hôm qua có khả năng ra lại hôm sau là bình thường chỉ là **yếu tố + điểm** đừng quá ưu tiên như thế chứ em. xem kỹ dùm anh coi khổ quá vậy em"*
- 17:50: *"đợi MB xổ xong rồi phân tích đánh giá **xử lý luôn** em"* (duyệt K15 đã đề xuất cùng phiên)

## 1. Forensic MT 09/07 — 59 lặp 2 ngày là gì

- Official MT: BT=59 lo2=[59,40] (16:40) — 59 KHÔNG về → **thua ngày 2 liên tiếp cùng một số**.
- Phiếu 59 hôm nay = **5 model khối ML y hệt danh sách hôm qua** (combo-no-token, meta-learning, random-forest, smart-ensemble, smart-ml). Mốc 04:00 dùng data D-1 gần như không đổi → khối nhả lại nguyên số, và vì khối chiếm 5-6 ghế nên 59 lại thắng vote. **Không phải "echo được cộng điểm" — là khối chiếm ghế.**
- /choi MT (lock tuần AE) cũng chết cùng kiểu: AE echo đúng "số official vừa thua" = [59, 86] ✗.
- **Ngày lãng phí thật sự: 12/26 model cầm số trúng ngay top-1** (cụm 73 ×4 phiếu, 41 ×2, 84 ×2, 37 ×2) mà official vẫn 59.
- **Lặp-sau-thua 90d MT: 6 lần, chỉ trúng 2** — nếu thay bằng á quân hôm đó: trúng 4/6. Trực giác owner có số chống lưng.
- AE echo 30d: echo 20/44 (45%) vs không-echo 21/48 (44%) — dài hạn hoà, không phải gốc bệnh chính.
- **MT_OUTPUT_V1 (top-10 strength) hôm nay chọn 84 TRÚNG; 60 ngày 23/61 = 38% vs official 30%.**

## 2. Forward day-1 (09/07) — số chốt TRƯỚC giờ quay

| Miền | Official | SEL_BASE | SEL_DEDUP | SEL_RECENCY | *_OUTPUT_V1 |
|---|---|---|---|---|---|
| MN | 13✗ (echo hôm qua, 6 phiếu AI) | 02✗ | 02✗ | 02✗ | 02✗ |
| MT | 59✗ (lặp ngày 2) | 40✗ (né được 59) | 40✗ | 40✗ | **84✓** |
| MB | 16✗ (K11a áp, applied=1) | 16✗ | 16✗ | 16✗ | 16✗ |

- MN: bể 26 model chụm 02/13 sai cả loạt (chỉ 5/26 trúng lẻ tẻ, cụm trúng lớn nhất 73 nằm ở khối shadow phiếu-2) — ngày không cứu được bằng bầu phiếu.
- MB: **K11a nổ phát đầu đúng thiết kế** (log applied=1, inline 17:33 khớp 100% lane bundle 17:55 = 16) — 16 trật NHƯNG champion doctrine 86 cũng trật → hoà, không thiệt. Cả bể chỉ 1/26 trúng (ngày không tín hiệu).
- MT: **chỉ một mình MT_OUTPUT_V1 bắt được 84** — đúng lớp K15 vừa promote.

## 3. Xử lý (deploy 18:50, guard SAFE sau khi MB có KQ, hash 4 bảng IDENTICAL)

1. **K15 — MT lane promote** (`_v10790_mt_lane_promote.py` + hook `main.py`): từ **10/07**, BT+lô-2 official MT = thuật toán `MT_OUTPUT_V1` (V10692 nguyên bản K=10 w2=0.6; ưu tiên lane bundle 16:50, fallback inline tại 16:40; min 3 voter). Sandbox 4 case PASS (start-gate / lane-bundle 84-41 / inline 84-41 / not_mt). Kill-switch 1 dòng + log audit `v10790_mt_lane_promote_log`.
2. **Metric "lặp-số-vừa-thua"** vào panel ⏱ MỐC & NHỊP (`/monitoring`): official BT = BT vừa TRẬT hôm trước — 60d: MT 1/5, MB 0/3, MN 0; **cảnh đỏ khi HÔM NAY đang lặp** → không bao giờ lặp âm thầm nữa.
3. Smoke: health 200, admin 401, journal sạch. Hash pre/post IDENTICAL (66a48f26/9a372c39/95c3004a/4fc6e4a0).

## 4. Trạng thái tổng sau 09/07

- **MB**: official = MB_OUTPUT_V1 (K11a, live từ 09/07) ✅
- **MT**: official = MT_OUTPUT_V1 (K15, live từ 10/07) ✅
- **MN**: giữ nguyên vote thường (miền khỏe nhất 45%/30d) — K13 recency đo shadow 14 ngày rồi mới xét
- Selector shadow (K10/K13) forward tiếp tục; Cohere đã tháo; /choi có caption nguồn số.
- Chờ ký: K9 herd-fade, K14 MB same-day-train, K8 gemma 429.

*Verify tiếp theo: 10/07 ~16:41 log `[V10790-K15]` bundle MT. Commit private + public trong cùng phiên.*
