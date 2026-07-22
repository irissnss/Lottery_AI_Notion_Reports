# V10834 — Audit nhân-quả mốc giờ + fix freeze-at-cutoff /choi (22/07)

**GitHub:** https://github.com/irissnss/Lottery_AI_Notion_Reports/tree/main/V10834_TIMING_CAUSALITY_AUDIT_20260722

## Owner 13:01
"Đúng các mốc thời gian cũng quan trọng không kém — nó ảnh hưởng dữ liệu, rules v.v. — cần kiểm tra và tư duy logic thật tương quan."

## Đã làm
- **Audit 22 mắt xích producer→consumer bằng GIỜ THẬT 7 ngày** (created_at/locked_at/computed_at + crontab + scheduler_logs): votes→lane (MT +14p, MB +22p) · same-day chéo miền KQ MN→lane MT +16p, KQ MT→lane MB +23p · KQ MB→job học tối +32p · MRE→M2s→📐 +10p · giờ xổ→ingest +15..19p (không lookahead). **Chuỗi sống OK hết.**
- 2 cờ đỏ = false positive: rows retro ngày-0 18/07 (by design) và **`mined_rule_effectiveness.created_at` là UTC** (13:15 = 20:15 VN) — pitfall mới ghi vào playbook cùng bẫy scheduler_logs.
- **1 lỗ hổng thật:** freeze /choi daily lock phụ thuộc "lần compute_board gần nhất" → **19/07 MB freeze 18:31, SAU cutoff 18:00 và SAU giờ xổ 18:15** (số vẫn causal từ lane pre-draw, nhưng kỷ luật freeze hở; 13/14 ngày còn lại đúng).
- **Fix:** cron **freeze-tick 16:00/17:00/18:00** chạy `_v10834_lock_freeze.py` → `compute_board()` — logic khóa V10794/V10828 nguyên vẹn, chỉ bảo đảm thời điểm. Test tick: MN giữ lock cũ, MT/MB không ghi sớm. Hash 4 bảng IDENTICAL.

## Verify tối nay
Log 3 tick + `locked_at` 3 miền ≤ cutoff; kèm verify V10832 (lane V3 rows đầu) + V10833 (lock MB đọc trace mới).
