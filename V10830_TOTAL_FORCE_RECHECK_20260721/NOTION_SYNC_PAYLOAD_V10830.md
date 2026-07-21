# V10830 — Tổng lực toàn diện lần 2 (owner re-reminder 11:25 21/07)

**Loại:** Audit read-only trên DB synced (`artifacts/live_sync/20260721_112853`) + chú giải điều kiện lên panel 📐.  
**GitHub đầy đủ:** https://github.com/irissnss/Lottery_AI_Notion_Reports/tree/main/V10830_TOTAL_FORCE_RECHECK_20260721

## Số liệu chính
- /choi 13–20/07: MN BT 2/7 · MT BT 5/8 · **MB BT 0/8** (any 2/8) — thất bại dồn MB.
- 4 luồng trial 18–20/07: M0 2/9 · lane 1/9 · M2s 3/9 · A/B-B any 16/45; ngày 20/07 cả 4 tầng đeo 26 (herd 3 miền D−1).
- Từng model: tệ nhất gpt-5.4/random-forest −25pp, combo-no-token −20, deepseek −16; tốt gemini-flash +24, lstm/xgb +12. **LLM gộp = thước đo any-hit 7 LLM cộng dồn**: 52.4% vs nền 55.4% (−3pp, chưa chạm rollback −10pp). MB là điểm gãy (LLM −8pp, ML −10pp).
- Rules vs model: union có số về mọi ngày trừ **MB 20/07 = 0/10** (ngày chết); 19/07 MB số 63 có 2 phiếu ML nhưng bị 7 phiếu 46 đè.
- Nguồn gốc: 26 = 10 rule đọc MB/Thái Bình G7 D−1 (tier thấp, 0 STRONG); 63 = rule #2202 MT/Khánh Hòa; 46 trong rules, **69 ngoài rules** (chase); 46/69 vào /choi qua AE lag-1 trước fix V10828.
- Học tập sạch: retrain ✓ miner W30 ✓ MRE ✓ re-rank ✓ MDE 27 ✓ self-check 11/11.

## Điều kiện đã đào (trả lời "mơ hồ")
RAW 38.18% → **H-A1a** 50.1% · **H-A4b** 49.6% (loại G7-đơn-độc kiểu 26) · **H-A4a** 42.1% (chống herd) · **B: H-A4a∧H-B2a** BT 46.9% vs M0 31.6% (+15.2pp). Minh họa 18–20/07: B-best BT✓ 5/9 vs official 2/9 (in-sample; forward thật từ 21/07, đọc 04–11/08). Panel 📐 thêm khối "📖 Nghĩa tiếng thường".

## An toàn
ZERO đổi production; hash 4 bảng pre=post IDENTICAL (`556073f8`/`44bf969e`/`7ce7a13f`/`07b4fbc5`). Watch tối nay: lock MB 17:5x không được chứa số 0-vote; V10829 forward row đầu 21:00.
