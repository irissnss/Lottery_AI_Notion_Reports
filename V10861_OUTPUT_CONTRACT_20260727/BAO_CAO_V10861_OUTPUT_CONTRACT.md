# V10861 — `/choi` output contract + Top-K/deadline + P&L mobile

## Owner lock

- `/choi` output phải đúng phương pháp để hiển thị và đo lường.
- Gate chỉ quyết định vốn/chơi; không được xoá output.
- Deadline tối đa: MN 15:55, MT 16:55, MB 17:55.

## Root cause đã xác nhận

### 1. Top-K thiếu model thực

Code cũ lấy top-K từ ranking lịch sử trước, sau đó mới đọc prediction hôm nay.
Model stale/không chạy vẫn chiếm slot:

- MT 26/07: K=10 nhưng chỉ 6 voter.
- Bốn slot rỗng: qwen3.6-plus, deepseek-v4-flash, glm-5.1, qwen3-coder.
- Output cũ 03 trượt.
- Lọc model có output tại 16:53 trước rồi mới lấy K10: 58 trúng.

Backtest causal 60 ngày:

| Miền | BT cũ | BT available-first | Any |
|---|---:|---:|---:|
| MN | 41.7% | 45.0% | 63.3% giữ nguyên |
| MT | 35.0% | 36.7% | 53.3% giữ nguyên |
| MB | 25.0% | 26.7% | 40.0→41.7% |

Số ngày pool-hole: MN 56/60, MT 35/60, MB 21/60.

### 2. Output còn thay sau deadline

Readiness trigger chạy mỗi 5 phút từng refresh MT_OUTPUT tới 17:10, dù K15 đã áp row
16:53 lúc 16:54. Vì vậy UI/history có thể khác số official đã dùng.

Fix:

- Có output trước deadline: giữ immutable.
- Trigger sau deadline trả `FROZEN_OWNER_DEADLINE_KEEP`.
- Không có output trước deadline: `MISSED_OWNER_DEADLINE_NO_WRITE`, không sinh số muộn.

### 3. `/choi` double-gate làm mất output

AE raw output bị xoá khỏi lane khi không qua vote gate; V10844 lại chỉ đọc daily capital lock.
Kết quả là UI fallback tạm nhưng measurement ghi NULL.

Fix tách:

- `display_numbers`: raw method output, luôn giữ để UI/đo.
- `capital_numbers`: chỉ có khi gate vốn pass.

Backfill MB:

- 25/07 display `[58,52]`, capital không khóa.
- 26/07 display `[52,65]`, capital không khóa.
- 27/07 trước 17:52: current output vẫn pending đúng method; UI hiện output 26 với nhãn
  “không phải số hôm nay”, không gán AE sai.

### 4. P&L model mobile

Static audit trước không có dynamic rows nên bỏ sót. Bảng verify-preview có 14 cột và
model/profile dài, nhưng không có scroll wrapper; body overflow bị ẩn nên nhìn như tràn/cắt.

Fix:

- scroll nội bộ cho capital/preview/settle/history;
- constrain pnl-wrap/section/details;
- model cell `break-word`;
- payload 8 model dài trên Chromium + WebKit, 320/390/430px:
  body overflow = false, table scroll nội bộ đúng.

## Measurement/deploy

- Bảng `v10861_output_deadline_audit`: 180 rows.
- Bảng `v10861_choi_display_output`: 87 rows sau live persist.
- API admin `/api/admin/output-contract`.
- Monitoring panel auto-refresh 60s.
- Cron 20:45.
- 8/8 file MD5 local=VPS.
- Health 200, guest admin 401, journal error-level 0, self-check 11/11.
- Bốn official table hashes IDENTICAL.

## Live gate kế tiếp

Ngày 27/07:

- MT 16:53 phải đủ K10; K15 16:54 dùng đúng frozen row.
- MB 17:52 phải đủ K8; K11a 17:54 dùng đúng frozen row.
- Sau 16:55/17:55 không được thay output.
- `/choi` display phải có số sau deadline dù capital gate block.

Không promote/rollback K15, K11a, M2s hay PB-18.1 ngoài các gate đã khóa cho 28/07.
