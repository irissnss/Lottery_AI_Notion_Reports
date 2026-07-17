# V10820 — RULES-FIRST vào prompt production (PB-18.1), chạy thật từ 18/07, đo 7-10 ngày

**Owner ký 23:33 17/07:** "backup tại thời điểm này và tiến hành điều chỉnh lớn luôn, chạy thật luôn trong 7-10 ngày để đo… đảm bảo mai live ổn định luôn."

**Đã làm trong đêm (23:33→00:1x):**
- Prompt production PB-18.0 → **PB-18.1** (lần đầu đổi kể từ PB-18.0): mọi context pack kết thúc bằng khối RULES-FIRST — danh sách số as-of từ mined_rules active (khớp EXACT tập MRE đã backtest +7.5pp MB).
- MB/MN: main BẮT BUỘC từ danh sách (khi ≥4 số) · MT: ưu-tiên-mạnh · cấm số-phụ-biến-thể (đảo/±1) mọi miền · anti-herding hết gợi ý "±1 cùng family" · PHA giữ cho main (tắt hẳn hại main −7pp).
- Smoke trước deploy: block khớp EXACT MRE 3 miền @17/07 (16/10/9 số); 18/07: MN 14 · MT 11 · MB 6 số; call thật gpt-5-mini main-trong-danh-sách ✓.
- Deploy 00:0x: sha khớp, health 200/admin 401, journal sạch, **hash 4 bảng IDENTICAL**. Backup 2 đầu `backups/v10820_pre/` + VPS `v10820_vps/` — rollback ~2 phút.

**Lịch đo (trace PB-18.1 vs PB-18.0 + panel 🎯):**
- 18/07 tối: %pick-in-rules phải >50% (baseline 24-30%), đủ 15/15 chốt.
- 21/07 guard-rail: any < baseline −10pp → rollback ngay.
- 25/07 giữa kỳ · **28/07 chốt: main MB/MN ≥ +3pp GIỮ / ±3pp thêm 7 ngày / <−3pp rollback.**

**Trạng thái FU:** FU-V10820-RULES-FIRST-LIVE (LIVE_TRIAL_RUNNING) · FU-V10818 + FU-V10819 → SUPERSEDED_BY_V10820 · ML models không đổi đợt này.

**Báo cáo đầy đủ:** GitHub `Lottery_AI_Notion_Reports/V10820_RULES_FIRST_LIVE_20260717/BAO_CAO_V10820.md`
