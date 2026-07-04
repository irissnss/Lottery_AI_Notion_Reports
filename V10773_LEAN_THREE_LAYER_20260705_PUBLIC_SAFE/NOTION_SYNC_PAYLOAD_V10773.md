# V10773 — TINH GỌN HỆ THỐNG + SO GĂNG 3 TẦNG từ 10/5 (2026-07-05)

## 1. Owner yêu cầu (04/07/2026, tối)

Hệ thống có nhiều thay đổi lớn, phình to → dọn dẹp sạch sẽ gọn gàng nhất quán. Audit toàn bộ TRƯỚC, xử lý vấn đề đã rõ, giữ vấn đề chờ live, cập nhật nhất quán, xác định đo lường nào còn hoạt động. UI nhét quá nhiều thứ, trùng lặp lộn xộn — cái nào đo, cái nào chơi, cái nào theo dõi, cái nào thử nghiệm? **Đơn model, total output, method — tới giờ cái nào MẠNH, CHÍNH XÁC, ỔN ĐỊNH?** Đặc biệt sau 10/5 dữ liệu ổn định, đầy đủ, xác thực hơn.

## 2. AUDIT TRẢ LỜI DỨT ĐIỂM (56 ngày 10/05→04/07)

Thước đo thống nhất: song-thủ 2 số × 50 điểm × tất cả đài của miền, 1 ăn 98k, cost MN/MT 18k MB 27k (khớp /choi). Chấm lô bằng FULL bảng giải (extractor validate 1707/1707 khớp hệ thống). Sync dữ liệu live trước audit (manifest 20260704_232253).

### TOTAL OUTPUT (official /du-doan)
| Miền | P&L 56d | 2 nửa | Hạng/52 | Kết luận |
|---|---|---|---|---|
| MN | **−37.5M** | −26.1/−11.4 (ÂM CẢ 2) | 34/52 | **Mắt xích yếu nhất hệ thống** |
| MT | **+29.6M** | +0.1/+29.5 (BỀN) | 7/52 | **Total output làm ĐÚNG việc** |
| MB | +0.7M | −2.1/+2.8 (hòa) | 17/52 | Chờ giả thuyết RF (V10772) |

### MODEL ĐƠN mạnh-ổn định (BỀN = lời cả 2 nửa kỳ)
- **deepseek-reasoner: model DUY NHẤT dương cả 3 miền (+94M tổng)** — MN +40.1M BỀN, MT +41.8M BỀN, MB +12.3M.
- **random-forest: BỀN ở MT (+68.8M, mạnh nhất MT) và MB (+39.9M)** — tái xác nhận giả thuyết V10772 trên cửa sổ 56 ngày độc lập; nhưng MN −32.6M (âm 2 nửa) → RF chỉ hợp MT/MB.
- gpt-5.4 MB +44.8M nhưng nửa sau chỉ +2.8M (kém bền hơn RF).
- **combo-super chỉ mạnh MT (+39.4M BỀN); MB −53.2M** (khẳng định lại: tổng hợp nhiều model đang HẠI MB).

### METHOD lane-test (20 method)
- MN ADAPTIVE_EXPLOIT +47.7M BỀN **nhưng 21 ngày gần −11M (đang nguội)** — CP-66.9 chờ owner quyết đã ~26 ngày.
- MB các method OUTPUT/DIR2/DIR3/XIEN +29M BỀN (n=31).
- **Không method nào thắng official MT** → MT không cần đổi gì.

## 3. PHÌNH TO ĐO ĐƯỢC + ĐÃ DỌN (đợt 1)

**Đo được:** 212 bảng DB (41 bảng CHẾT >30 ngày không ghi); /monitoring 56 panel, 53 loader, **39 loader tự refresh 60s** (nguồn "treo lag"); 6 panel đọc bảng đã chết từ 09-30/05 (chuỗi V102→V105 đã retire nhưng UI chưa gỡ).

**Đã dọn (an toàn, đảo ngược được):**
1. Panel MỚI "🥇 SO GĂNG 3 TẦNG từ 10/5" trên /monitoring — trả lời cố định câu "model đơn / total / method cái nào mạnh-ổn định" (READ-ONLY 100%, không ghi bảng nào).
2. Gỡ 6 panel + 6 loader + 6 endpoint ZOMBIE (V103 / V104 / V105-lane / V105.6 / V105.22 / EQ-MB-R11).
3. Auto-refresh 60s: **39 → 17 loader** (chỉ nhóm Trọng tâm; nhóm đo lường/cũ nạp 1 lần) — giảm ~2/3 call nền.
4. Bộ lọc panel đổi nhãn theo đúng câu owner hỏi: 🎯 CHƠI & Official · 🧪 THỬ NGHIỆM forward · 📏 ĐO LƯỜNG/audit · 🗄️ CŨ/đã kết luận.
5. 41 bảng chết → liệt kê file drop-candidates, **CHỜ OWNER OK mới drop** (không tự xóa dữ liệu).

## 4. AN TOÀN & VERIFY

- KHÔNG đụng /du-doan, final_bundles writer, scheduler materializer nào. Không drop bảng.
- Hash-guard 4 bảng official PRE = POST **IDENTICAL** (predictions 9268, final_bundles 381, lottery_results 15010, model_daily_eval 9132).
- Smoke sau deploy: health=200, /du-doan=200, /monitoring=401, endpoint mới 401 (admin-lock), 6 endpoint zombie = 404 đúng kỳ vọng.
- Guard V10772B chạy đúng lúc restart: `skip: no_bundle_yet_normal_chain_will_handle` (00:01, chưa có bundle 05/07 — chuẩn).
- Scoreboard chạy trên VPS khớp local: MN official 34/52, MT 7/52 BỀN, MB 17/52.

## 5. CHỜ OWNER QUYẾT (không tự làm)

1. **CP-66.9 (quá hạn ~26 ngày):** adaptive-exploit MN — lane +47.7M/56d nhưng 21d gần −11M. Đề xuất: ĐÓNG hoặc gia hạn theo dõi, KHÔNG promote lúc tín hiệu nguội.
2. **Drop 41 bảng chết** (danh sách đã lập, backup trước khi drop).
3. **MN official đang âm bền** — ứng viên bền: deepseek-reasoner (+40.1M) / gpt-oss-120b (+25M). Đề xuất xử lý SAU checkpoint RF-MB 14/07 (không đổi 2 miền cùng lúc).

## 6. Truy vết

- Private commit: `00c960b` (Lottery_AI_Test).
- Backup: `backups/v10773_cleanup_20260704/`.
- FU tracker: `FU-V10773-LEAN-3TIER` (checkpoint cùng nhịp RF-MB 14/07).
- Governance seq: 228.
