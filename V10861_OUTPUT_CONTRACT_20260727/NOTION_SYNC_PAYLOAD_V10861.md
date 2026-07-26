# V10861 — Output contract `/choi` + deadline/Top-K + P&L mobile

- Owner lock: output `/choi` luôn giữ đúng method để hiển thị/đo; gate chỉ quyết vốn.
- Deadline immutable: MN 15:55, MT 16:55, MB 17:55.
- Root bug: ranking lịch sử cắt K trước khi lọc model có output hôm nay.
- 26/07 MT K10 chỉ 6 voter; 4 model stale chiếm slot.
- Available-first tại 16:53 đủ 10 voter và chọn 58✓ thay 03✗.
- 60d BT: MN +3.3pp, MT +1.7pp, MB +1.7pp; any không giảm.
- Output từng bị readiness trigger refresh MT tới 17:10 sau deadline.
- Fix: row có trước deadline immutable; thiếu thì không sinh output muộn.
- `/choi` double-gate làm V10844 ghi NULL dù raw method có số.
- Tách `display_numbers` và `capital_numbers`.
- Backfill MB: 25/07 `[58,52]`; 26/07 `[52,65]`; capital không khóa.
- Rollover: hiện output gần nhất có ngày + “không phải số hôm nay”.
- P&L dynamic 14 cột/model dài đã có scroll nội bộ; Chromium+WebKit 320–430 pass.
- Measurement: 2 bảng shadow, API admin no-store, panel monitoring 60s, cron 20:45.
- Deploy: 8/8 MD5, health 200, admin 401, journal 0, self-check 11/11.
- Hash 4 bảng official IDENTICAL; không đổi prompt/writer/official selector.
- Live verify 27/07: MT K10 16:53, MB K8 17:52, freeze sau deadline.
- Báo cáo gốc: https://github.com/irissnss/Lottery_AI_Notion_Reports/tree/main/V10861_OUTPUT_CONTRACT_20260727
