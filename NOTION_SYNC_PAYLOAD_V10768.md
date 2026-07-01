# V10768 — De-herding prompt: bỏ bảng WR/BT ranking khỏi context pack official

**Ngày:** 2026-07-02 (UTC+7) · **Loại:** OFFICIAL PROMPT (mọi model AI, chỉ ảnh hưởng batch tương lai) · **Rollback:** flag 1-dòng

## Bối cảnh (owner)
Owner nhắc lại giả thuyết: prompt nhồi "BẢNG XẾP HẠNG WR/BT" ép model AI hội tụ (herding) → total trượt dù có model bắt đúng số. Yêu cầu thử sandbox trên ngày LOSE + model bắt sai. Sau khi có kết quả, owner chọn **PHƯƠNG ÁN C** (deploy ngay + backup/ghi chép đầy đủ nhất).

## Sandbox (read-only, VPS)
8 ngày LOSE official (MN+MT) × 3 model (claude-sonnet-4-6, gemini-2.5-flash, deepseek-reasoner) × 2 biến thể:
- **herded** = base context (KQ D-1 + mined_rules + số nóng) + khối WR/BT ranking causal (date < D).
- **de-herded** = base, BỎ khối WR/BT.

| Chỉ số | herded | de-herded |
|---|---|---|
| Union-hit (bắt ≥1 số) | 6/8 | **8/8** |
| Consensus-miss (cả 3 xúm 1 BT & trượt) | 2 | **1** |
| claude hit/ngày | 4/8 | **7/8 (+3)** |
| deepseek hit/ngày | 5/8 | **7/8 (+2)** |
| gemini hit/ngày | 6/8 | 5/8 (−1) |
| Bắt số herded-union bỏ lỡ | — | **2/8 ngày** |

Herding hiện rõ: 26/06 MT cả 3 model xúm về `25` → trượt (de-herded deepseek tách `11` → về); 29/06 MT cả 3 xúm `19` → trượt (de-herded claude tách `46` → về).

## Thay đổi kỹ thuật (V10768)
- `gpt_analyzer.py`: `_deherd_strip_ranking()` + gate `_V10768_DEHERD_PROMPT_ENABLED=True`.
- Áp trong luồng predict official NGAY sau `build_context_pack`: strip 3 mục gây herding ("Model Performance 14 ngày" WR, "BT MODEL RANKING 30d", "Riêng {thứ}").
- GIỮ NGUYÊN: mined_rules, KQ D-1, evidence table, 3-layer mandate, phase gate, anti-trap.
- Verify strip: MN 8690→7585, MT 9087→7908, MB 14207→13071 (đều bỏ đúng 3 mục ranking).

## An toàn / verify VPS
- compile OK; flag+apply present; strip verified 3 miền; health=200; `/du-doan`=200.
- **hash-guard 4 official IDENTICAL** (deploy không regen; áp dụng từ batch dự đoán 02/07 04:00 + chains).
- Backup nhiều lớp: `backups/v10768_remote_pre/gpt_analyzer.py` + VPS `backups/gpt_analyzer.py.v10768_pre.bak` + git history + flag.

## Rủi ro (owner chấp nhận)
Mẫu sandbox 8 ngày (nhỏ); prompt sandbox đơn giản hoá (không phải full official); gemini −1/8. → CHECKPOINT 2026-07-08 theo dõi official forward; tụt bất thường → rollback `_V10768_DEHERD_PROMPT_ENABLED=False`.

## Cải chính
gpt-5.4 bị loại khỏi sandbox do key env 401; official gpt VẪN chạy bình thường (dùng key DB) — không phải sự cố.
