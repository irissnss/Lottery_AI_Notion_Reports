# NEXT ACTION (V105.41 — 2026-05-14 09:25 VN, morning comprehensive audit)

Trạng thái: `V105_41_MORNING_COMPREHENSIVE_AUDIT` + `NATURAL_VERIFY_PARTIAL_PASS_NOT_FULL_PASS`. Service uptime 26 ngày 8 giờ, chưa restart kể từ V105.35 deploy ngày 12/5 19:38 VN. V105.40 expansion patch vẫn chờ owner gate.

## Việc cần làm theo thứ tự ưu tiên

1. **Owner OK V105.40 expansion patch + service restart sau MB 17:35 cycle close (~19:00 VN hôm nay).** Patch nhỏ, không đổi scoring/prompt/selector/voting/roster/publish-gate/timeout/trigger. Backup + py_compile + smoke + journal scan + rollback path đã sẵn sàng.
2. **Mở rộng V105.40 scope thêm 5 path:** Excel writer, verify-final-bundle, Pattern Tracker, Shadow Daily Comparison, Shadow Rule D1 measurement materializer. Tất cả cùng class lỗi closed-file; cùng một helper `_safe_print(traceback.format_exc())` fix được hết.
3. **Giữ Day-control hard lock đến sau MT 16:30 + MB 17:35 cycles.** Không deploy/restart giữa ngày live, không gọi provider/manual, không đổi trigger/cron.
4. **MT 5-model watch active cho cycle 16:30 hôm nay.** Sau 13/5 đã recovered đầy đủ; nếu hôm nay tái phát closed-file thì label `CLOSED_FILE_REGRESSION_P0`, không force publish.
5. **MB cycle 17:35 verify gate semantic V105.35:** `publish_ready = output_eligible_row_count == 15`; `scoreable_model_count < 15` chỉ là quality warning. Lane-test 7 experiments shadow-only, không promote.
6. **Direct-API vs OpenRouter shadow A/B** tiếp tục đo lường. Closed-file regression xuất hiện trên cả hai route, nên route migration không phải fix; phải fix stdio handling trên long-running process.
7. **MB lo2 weight A/B (0.95 / 0.75 / 0.55) shadow-only** tiếp tục accumulate. Không promote.
8. **GLM-5.1 compact JSON profile** vẫn owner-gated. Không gọi provider để test nếu chưa OK.
9. **Source-pool / prompt / top-2 tuning** chờ V105.40 ship + 24h cycle sạch.
10. **Public mirror** đã được clean trong release này. V105.36 closeout wrapper + V105.41 morning audit + 3 deep-dive evidence files đã publish cùng commit.
11. **Notion** vẫn là secondary SSOT; FINAL TRUTH page đã được cập nhật V105.41 morning.

## Owner decision queue

| # | Decision | Recommendation |
|---|---|---|
| 1 | Authorize V105.40 expansion deploy + restart sau MB 17:35 close (~19:00 VN) | YES |
| 2 | Confirm extended scope (gpt_analyzer.py + main.py 16 sites + Excel + verify + Pattern Tracker + Shadow Daily Comparison + Shadow Rule D1) | YES |
| 3 | Maintain day-control hard lock through MT 16:30 + MB 17:35 | YES |
| 4 | Timeout 90 / 300 preserved; V105.38 500 s remains proposal only | YES |
| 5 | Lane-test reserve-fill remains test-only; official reserve-fill HOLD | YES |
| 6 | MB lo2 A/B shadow continue accumulating; no promote | YES |
| 7 | Direct-API vs OpenRouter shadow A/B continue accumulating; no migration | YES |
| 8 | Source-pool / prompt / top-2 tuning held until V105.40 deploys + 24h cycle clean | YES |
| 9 | Model health scoreboard continue accumulating; no roster change | YES |
| 10 | Public mirror: V105.41 release cleanup pushed; remaining V105.37/V105.38/V105.39/V105.40 evidence stays private + Notion mirrored | YES |

## Stop-loss

Dừng ngay và báo owner nếu:

- Official endpoint nào trả HTTP 500 ngoài path đã biết (`/api/review-hub/filter`).
- Service bị restart loop hoặc inactive.
- Live DB sync hash mismatch lặp lại.
- Closed-file xuất hiện trên path `auto_daily` (không chỉ shadow).
- Trigger / cron timing đổi bất ngờ.
- Provider key environment bất thường.
- Patch yêu cầu rewrite rộng.
- Public mirror dirty và push có thể overwrite remote.
- Yêu cầu gọi provider thủ công.
- Yêu cầu force publish MT khi output rows < 15.

Default action: `NO_UNSAFE_RECOVERY` · `PENDING_PRESERVED` · `NO_SYSTEM_DAMAGE`.

Evidence chính: `V105_41_MORNING_COMPREHENSIVE_AUDIT_20260514/evidence/V105_41_MORNING_COMPREHENSIVE_REPORT.md`, `V105_41_MODEL_HEALTH_AND_METHODOLOGY_DEEP_DIVE.md`, `V105_41_RUNTIME_STABILITY_AND_GOVERNANCE.md`.
