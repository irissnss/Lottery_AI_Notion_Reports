# V10819 — "Rules bị bỏ rơi": bốc-đại-từ-rules thắng model, sandbox RULES-FIRST (17/07/2026, 22:38→23:1x)

## 0. Owner flag (22:38)
"Rules thực sự có giá trị mà bị cái số đảo pha hay ±1 làm rơi rớt mất. Số 43 không nằm trong rules mà được đề xuất phi lý, trong khi 50/27/95/85/58/02 đều nằm rules — bốc đại cũng có khả năng trúng. Model AI đỉnh tư duy suy luận mà bốc toàn số trật phi lý (ví dụ MB với rules nguồn MN/MT). Tương tự đích MT và MN — đặc biệt MN 3 đài ~54 bộ số mà dự đoán sai hoài. Nếu cần tiếp tục chạy sandbox nữa đi."

## 1. Forensic 17/07 MB — anh đúng, có số liệu
- 5 rule READY_STRONG (bucket MB_T6, chốt as-of 13:15 trước giờ quay) phát **16 số**: 02 13 17 29 34 37 46 49 61 63 66 74 78 79 80 81 → **4 số trúng: 02, 13, 29, 46**.
- **43 KHÔNG nằm trong bất kỳ surface rules nào** (mined rules / injection contract / v101 cross / rule context / digit transform) — mà **9 model/method chốt 43: cả 9 trượt** (gemini-2.5-pro, grok-4.3, qwen3-max, combo-no-token, meta-learning, smart-ml, smart-ensemble, random-forest, xgboost). Nguồn gốc 43: mirror của 34 (V10818) + hạng 8 top-10 thống kê nội miền — không có rule support. Đúng chữ "phi lý".
- 46 chính là `strongest_candidate` của tracker conversion-loss hôm đó — bundle lại chốt 34 (drop_stage BUNDLE_SKEW). Tín hiệu đúng ĐÃ CÓ trong hệ, bị lớp chọn số làm rơi.
- Đính chính nhẹ: 50/27/95/85/58 không nằm trong mined-rules — chúng nằm trong **lô MN chiều cùng ngày**. V10817 đã đo tập soi-cùng-ngày tổng quát = 23.8% = nền; tập MINED RULES hẹp (~10.8 số/ngày) mới là tập có lift. Ý anh vẫn đúng hướng: số trong-hệ bị bỏ, số ngoài-hệ được chốt.

## 2. Lịch sử 200+ ngày/miền (từ 20/12/2025, as-of, không nhìn tương lai)
| Miền | Bốc-ĐẠI-1-số từ rules | Model main-hit | Bốc-2-số any | Model any-hit | % pick trong rules | hit trong vs ngoài |
|---|---|---|---|---|---|---|
| **MB** | **30.2%** | 22.7% | **51.9%** | 40.5% | 29.6% | **30.2% vs 20.2%** |
| **MN** | **47.2%** | 42.8% | **72.2%** | 67.0% | 28.5% | 47.8% vs 41.0% |
| MT | 37.3% | 36.3% | 61.0% | 58.1% | 24.2% | 35.3% vs 35.9% (~bằng) |
- **Bốc đại từ rules THẮNG model thật cả 3 miền** — đúng câu "bốc đại cũng có khả năng trúng luôn". Set rules ~10.5-10.8 số/ngày, ≥1 số trúng 97.5-100% số ngày.
- Model chỉ đặt **24-30% số pick nằm trong rule-set**. Nhóm ML bỏ rules nặng nhất: meta-learning 93.8% main ngoài rules (khi vào rules trúng 52.9% vs ngoài 30.1%), random-forest 93.0%, xgboost 93.0%, combo-no-token 90.5%, smart-ml 90.5%.
- MT là ngoại lệ: hit trong ≈ ngoài → rules MT yếu hơn (nhất quán với mirror-MT hơi dương ở V10818) → không áp RULES-FIRST cho MT vòng đầu.

## 3. Sandbox arm C "RULES-FIRST" (anh cho phép — 20 call as-of, 5 model × 4 case)
Addendum: inject **danh sách số rules tường minh** + main BẮT BUỘC chọn từ danh sách + phụ ưu tiên danh sách + cấm biến thể ±1/đảo.
- **MB@17/07: any-hit 4/5, main-hit 3/5 — gemini/qwen/deepseek đều TỰ hội tụ về 46✓ (claude phụ 46✓), cặp 34-43 biến mất** (replay prompt gốc cùng case: any 1/5).
- MN@17/07: 2/4 (29✓ ×2) · MT@17/07: 1/4 (61✓ — ngày MT cả bầy trượt) · MB@13/07 (đối chứng ngày bầy-thắng): 2/5, vẫn giữ được 89✓ của bầy vì 89 NẰM trong rules — RULES-FIRST không phá ngày bầy đúng khi số bầy có rule support.
- Cộng: **C any 9/18 (50%) vs A cùng case ~4/17 (23.5%)**; addendum được tuân 18/18 call. So với B (phase-off V10818): C tương đương về any nhưng main cao hơn và có CƠ CHẾ chọn (rules) thay vì chỉ CẤM (biến thể).

## 4. Đã deploy (§52, 23:0x)
- View `rules_drop` RECURRING (full/90d/forward từ 18/07 per miền + top model bỏ-rules + set hôm nay + model chốt ngoài set; cache 4.82s→0.52s) + khối **🎯 RULES BỊ BỎ RƠI** trong panel 🏃 CHASE-BIAS `/monitoring` (refresh 60s).
- Verify: health 200 · admin 401 · hash 4 bảng PRE=POST IDENTICAL · journal sạch · các khối V10816/17/18 vẫn sống. Không đụng official/prompt production.
- **Ngưỡng: CP-S3 23/07** — nếu forward giữ pattern (rand1 > model-main VÀ in-hit > out-hit ≥5pp ở MB/MN) → trình anh MỘT addendum duy nhất (RULES-FIRST MB/MN + cấm phụ-biến-thể V10818); ML models đề xuất riêng ép feature rule-set (đổi pipeline, cần anh OK).

## 5. Artifacts
`_v10819_rules_forensic.py`, `_v10819_rules_probe2.py`, `_v10819_rules_first_sandbox.py`, `_v10819_poll_c.py`, `_v10819_deploy.py`; kết quả arm C: VPS `/tmp/v10819_c_results.json`; FU: `FU-V10819-RULES-DROP` (WAIT_LIVE).
