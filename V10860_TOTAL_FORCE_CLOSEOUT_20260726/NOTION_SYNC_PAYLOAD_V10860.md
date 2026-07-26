# V10860 — Tổng lực closeout 26/07

- Owner yêu cầu đào sâu mọi model/phương pháp/cơ chế/mốc/UI trên 3 miền × 4 luồng và hỏi ngày xấu có phải do áo mới.
- Kết luận: KHÔNG do áo. V10859 chỉ HTML/CSS, backend không restart/không đổi; 72/72 trace PB-18.1 + rules, official đủ 15 rows/miền.
- 26/07 official BT 0/3 nhưng dữ liệu/station/scheduler sạch.
- Per-model: MN BT 1/15 any 5/15; MT BT 8/15 any 14/15; MB BT 3/15 any 5/15.
- Rule union vẫn có 4 tail trúng mỗi miền; lỗi ngày nằm ở selection/ranking top.
- K15 MT: champion 58 trúng bị challenger 03 trượt thay; in-trial challenger 4/9 vs champion 5/9, net −1, chưa gate −2.
- K11a MB: challenger 2/9 vs champion 1/9, hiện giữ.
- M2s: 12/24 vs M0 10/24 = +8.3pp; any +29.2pp, chưa đủ n=30.
- PB-18.1 equal-window: LLM any 46.6→65.8%; official BT 18.5→37.0%; không rollback vì một ngày.
- Rule-cond 8/18 = M0; what-if MB mới 2 ngày.
- Fix 1: pattern-reasoning JSON null crash trên ngày MB gate/no-lock.
- Fix 2: timing-audit báo giả do hard-code, retro row và UTC/VN.
- Fix 3: settings/user-view mobile overflow + loại `overflow-wrap:anywhere`.
- UI Chromium: 14 trang × 6 viewport = 84 case, 0 FAIL sau fix.
- Deploy: 7/7 MD5, health 200, admin guest 401, journal sạch, hash 4 bảng official IDENTICAL.
- Miner W31 27/07 00:30 LIVE_PROVEN: SUCCESS 105 rules / 9 STRONG / 11.45s; weekly lock 3/3; self-check 11/11.
- Mốc kế: gói quyết định lớn 28/07; what-if MB khoảng 01/08.
- Báo cáo gốc: https://github.com/irissnss/Lottery_AI_Notion_Reports/tree/main/V10860_TOTAL_FORCE_CLOSEOUT_20260726
