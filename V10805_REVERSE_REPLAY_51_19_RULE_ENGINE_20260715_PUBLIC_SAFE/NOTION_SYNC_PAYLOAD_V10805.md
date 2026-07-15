# V10805 — Replay ngược vụ 51/19: rule engine là nguồn phát, 5/6 replay ra lại đúng số (2026-07-15)

**Kết quả chính**
- Model ra 51 (MB 14/07): 16 con đích danh — claude-opus/sonnet-4-6, combo-super, deepseek-reasoner, deepseek-v4-pro-real, gemini-2.5-flash/pro, gemini-3.5-flash, glm-5.1/5.2, gpt-5-mini/5.4/5.5, grok-4.20, kimi-k2.5, qwen3.7-max. Model ra 19: MT 12 con (16:36-52), MN 4 con (04:16-32).
- Pure-ML (lstm/xgb/rf/meta/smart/combo-no-token) KHÔNG dính cả 2 vụ, nhiều con còn trúng → mốc D của ML không sai trong 2 vụ này (MB re-run 17:30 same-day đúng V10801; MT/MN 04:00 D-1). combo-super = AI-echo (top1 trùng AI 65-77% ngày), không phải ML độc lập.
- Nguồn phát trong prompt: rule engine emit đuôi giải D-1 miền khác — Đồng Tháp G5+G7 → [32,51] + G2+G5 → [97,51] (51 = CONV×2 boost cao nhất, nhãn "12W=92%"); Vũng Tàu GĐB+G1 → [19,61] (nhãn "75%"); 19 còn nằm khối định lượng chung (freq 3-4).
- REPLAY THẬT (code production, VPS, không ghi DB): 5/6 RA LẠI — gemini-flash [51,32]+[19,32], gpt-5-mini [51,97]+[19,98], deepseek [19,68]; chỉ deepseek@MB thoát → output DETERMINISTIC theo prompt.
- Lỗ hổng semantic: "12W=92%" = hit_ANY bao-lô cụm 2 đuôi (baseline any-of-2 42% MB / 51% MT, n=12 weekly) — model đọc như per-số. Per-tail thật: 33.3% (+9.6pp) / 44.1% (+14.3pp) — có tín hiệu nhưng thổi phồng 2-3×.
- Adoption 120d: MB theo-rule 30.0% (+6.2pp), CONV×2 50.6%, NGOÀI rule 17.7% (hố chính −6.1pp); MT rule không cộng (BT theo-rule 28.6% < ngoài 40.0% → mandate §10A sai chỗ tại MT = vụ 19); MN CONV×2 38.8% dưới baseline (bẫy hội tụ).
- Deploy: bảng "📜 RULE ADOPTION" live trong panel chase-bias /monitoring (view `rule_adoption`, không bảng mới, không cron mới); hash 4 bảng official pre=post IDENTICAL; rollback backups/v10805_pre.

**Quyết định chờ owner (CP-L6, 6 mục):** (a) nhãn rule → per-tail %+n; (b) miền-hoá mandate §10A (hạ MT); (c) guard ngoài-rule MB; (d) khối định lượng per-miền; (e) combo-super đánh dấu AI-echo; (f) thay API gemini-2.5-flash + gpt-5-mini.

**Verify:** 16/07 bảng 📜 render; ~14/08 đọc ngưỡng cùng chase-bias.

**Chi tiết đầy đủ:** GitHub `Lottery_AI_Notion_Reports/V10805_REVERSE_REPLAY_51_19_RULE_ENGINE_20260715_PUBLIC_SAFE/`
