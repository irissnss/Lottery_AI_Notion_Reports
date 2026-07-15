# V10803 — MỔ SÂU MB SAU CHU KỲ LIVE 15/07 + TRUY VẾT "SỐ 51" + SHADOW CHASE-BIAS 3 MIỀN

- Ngày: 2026-07-15 tối (sau chu kỳ live: MB xổ 18:15, scrape 18:30, sync local 18:39)
- Trigger: owner 18:38 — "đào sâu MB thật sâu sắc… số 51 của dự đoán ngày hôm qua nổ rồi còn đề xuất cho MB nữa thiệt rối quá rối"
- Trạng thái: DEPLOYED (shadow-only, ZERO đụng official) — hash 4 bảng official pre=post IDENTICAL
- Sync evidence: `artifacts/live_sync/20260715_183916/manifest.json`

## 1. Chu kỳ live 15/07 — kết quả 3 miền vs official

| Miền | ĐB | Official BT | Lô2 | Kết quả | Chuỗi giờ |
|---|---|---|---|---|---|
| MN | 02 | 63 | 63, 19 | BT trượt, lô2 trượt cả 2 | bundle 04:17 → chốt 15:45 → settle 16:34 ✓ |
| MT | 30 | 19 | 19, 39 | BT trượt, lô2 trượt cả 2 | bundle 16:39 → settle 17:30 ✓ |
| MB | 19 | 64 | 64, 92 | BT trượt, **lô2 92 NỔ** | rerun ML 17:30-32 → ai_chain 17:32-34 → bundle 17:34 → settle 18:33 ✓ |

Vận hành đúng thiết kế V10798/V10799 (lane → T-chốt :54 → freeze :55), không có lỗi giờ giấc. Vấn đề nằm ở CHẤT LƯỢNG PICK — mổ ở phần 2-3.

## 2. TRUY VẾT SỐ 51 — trả lời thẳng cái "rối"

Chuỗi sự kiện thật (từ DB + trace):

1. **13/07**: 51 nổ ở MN.
2. **14/07**: 16 model (claude×2, gemini×3, gpt×3, deepseek×2, glm×2, grok, kimi, qwen, combo-super) **đuổi theo 51** → herd top-vote 51×16 phiếu → official MB BT=51 → **TRƯỢT** (ĐB 47, 51 không ra MB).
3. **15/07**: 51 nổ ở **MN và MT** (đây là cái "nổ rồi" anh thấy). Nhưng **KHÔNG model nào đề xuất 51 cho MB ngày 15/07** — vote map 15/07: 64×14, 43×6, 16×5, 92×5, không có 51. Đề xuất "51 cho MB" anh nhớ là của NGÀY 14/07.

**Kiểm định "di cư" (số đoán MB trượt → hôm sau nổ MN/MT):** trong 90 ngày có 75 ngày BT MB trượt; 48/75 = 64% số đó nổ MN/MT hôm sau. Null-test 2000 mô phỏng (thay BT bằng số ngẫu nhiên): cũng 64%, p~0.516. **→ Di cư là ẢO GIÁC TẦN SUẤT, không phải pattern**: MN ra trung bình ~43 đuôi khác nhau/ngày, MT ~35, gộp MN∪MT ~63/100 số — nghĩa là 2/3 số BẤT KỲ sẽ "nổ đâu đó" vào hôm sau. Não người thấy "số của mình lại ra chỗ khác" và cảm giác bị trêu — nhưng xác suất là như nhau với mọi số.

## 3. Bias THẬT phát hiện: pool ĐUỔI SỐ VỪA NỔ HÔM TRƯỚC (chase)

Đúng trực giác "tương tự giống mấy khi quá" của owner — nhưng bản chất khác cái anh nghĩ:

- 14/07 pool đuổi 51 (vừa nổ MN 13/07) → trượt. **15/07 pool lại đuổi 64** (vừa nổ MN+MB 14/07, 14 phiếu) → trượt tiếp. Cùng MỘT thói quen lặp lại.
- Đo 90 ngày MB: BT official là số-vừa-nổ-hôm-trước trong **67/90 ngày (74%)**; nhóm này nổ **10/67 = 15%**, trong khi BT KHÔNG-đuổi nổ **5/23 = 22%** (baseline bao-lô MB ~24%). Lô2: đuổi 20% vs không-đuổi **31%**. 30 ngày gần: đuổi 9.5% vs không-đuổi 20%.
- MT cùng chiều âm: BT-đuổi 31% vs không-đuổi 38% (nền 35%). MN NGƯỢC LẠI (đuổi 46% vs 22%) — MN ra 43 đuôi/ngày nên đuổi ở MN vô hại.
- Herd top-vote MB là số-đuổi 26/30 ngày (~87%, nền ngẫu nhiên ~72%) — pool có tilt đuổi nhẹ nhưng có hệ thống.

**Chưa đủ ý nghĩa thống kê** (nhánh không-đuổi chỉ n=23) → theo hardlock §53: KHÔNG đổi selector/prompt, dựng forward-proof.

## 4. Hạ tầng shadow V10803 (deployed 18:52)

- Bảng `v10803_chase_bias_daily` (UNIQUE date+region; shadow_only=1, output_eligible=0, diagnostic_only=1, owner_approved=0) — backfill 90 ngày xong lúc deploy; row forward từ 16/07.
- Materializer `_v10803_chase_bias_shadow.py`, cron **19:10 hằng ngày** (`--catchup 3`), sau settle 19:00 và V10801 19:05.
- API admin `GET /api/admin/chase-bias` (require_admin, Cache-Control no-store).
- Panel 🏃 CHASE-BIAS tại `/monitoring` (đăng ký loadAllSections + setInterval 60s): 3 miền × 3 lớp (BT/lô2/herd) × 3 cửa sổ (toàn kỳ/30d/FORWARD).
- **Ngưỡng hành động ghi sẵn:** ≥30 ngày forward + mỗi nhánh n≥30 — nếu (đuổi − không-đuổi) ≤ **−10pp** bền 2 nửa → trình owner anti-chase tie-break (demote ứng viên đuổi khi hoà điểm, 1 quyết định); nếu ≥ 0pp → đóng, kết luận đuổi vô hại (chỉ là ảo giác người xem). Review ~16/08.

## 5. Bối cảnh BT official 30 ngày vs baseline bao-lô

| Miền | BT nổ 30d | Baseline (số bất kỳ) |
|---|---|---|
| MN | 11/30 = 37% | ~43% |
| MT | 6/30 = 20% | ~35% |
| MB | 4/30 = 13% | ~24% |

Cả 3 miền BT đang chạy DƯỚI nền — chase-bias là nghi phạm số 1 đang được đo. Thước kinh tế /choi (money board V10759, BT1 MN + combo MB) là hệ đo riêng, không đổi trong phiên này.

## 6. Deploy + an toàn

- Backup: local `backups/v10803_pre/` + remote `/root/backups/v10803_pre/`.
- Upload 3 file → py_compile OK → cron 19:10 → restart `active` → smoke: health=200, /choi=401(login), `/api/admin/chase-bias`=401 no-auth ✓.
- **Hash 4 bảng official pre=post IDENTICAL**: predictions 10122/3a18c24b…, final_bundles 414/0e68ae9c…, lottery_results 15081/1a1820b1…, model_daily_eval 9908/97c981c1….
- Post-verify: diff main.py vs backup CHỈ chứa block V10803; journal NO_ERRORS; cron 19:00/19:05/19:10 xếp hàng đúng.
- Rollback: xoá dòng cron v10803 + copy 2 file backup về + restart.

## 7. Governance

- `CHANGELOG.md` V10803 + `docs/CURRENT_TRUTH_SSOT.md` block V10803 + `docs/FOLLOW_UP_TRACKER.md` FU-V10803-CHASE-BIAS (DEPLOYED_PENDING_LIVE_VERIFY) + `docs/AUTOMATION_STATE.json` seq 264 + `docs/AUTOMATION_HISTORY.jsonl` + playbook §1/§5 cập nhật cùng phiên.
