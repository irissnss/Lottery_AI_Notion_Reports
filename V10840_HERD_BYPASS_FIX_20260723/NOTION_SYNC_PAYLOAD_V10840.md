# V10840 — Bịt herd-bypass M2s shadow/lane (Bugbot R2 High + Low) — 23/07

**GitHub:** https://github.com/irissnss/Lottery_AI_Notion_Reports/tree/main/V10840_HERD_BYPASS_FIX_20260723

## Bối cảnh
Owner 21:49: "vẫn còn lỗi đó em... xử lý được không em?" — 3 finding Bugbot vòng 2 (ghi ở FU-V10838B). Xử lý: **(a)+(b) fix ngay, (c) hẹn 28/07.**

## Đo trước khi sửa (quyết định an toàn)
Probe 15 ô forward 19–23/07: **bypass 0 · label-lie 0 · pad-leak 0** → lỗi High là **latent, chưa từng kích hoạt** (pick dính herd 19–20/07 là rows trước khi gate V10828 tồn tại). Fix **không đổi bất kỳ số liệu nào của kỳ đọc 28/07** — thuần bịt lỗ trước khi nó nổ đúng "ngày bầy mạnh nhất".

## Fix (2 module `_v10821_total_v2_shadow.py` + `_v10822_total_v2_lane.py`, nhãn 1:1)
1. Không model nào vote số sạch (r2 rỗng) → hết rơi thầm về M1 thô dưới nhãn `rules_minus_herd3` sai; nhãn mới `fallback_m1_herd_cleared_no_clean_votes`.
2. Phần đệm sau r2 = **M1 đã loại herd** (trước đây số phụ/fallback vẫn lọt herd); ca cực hiếm toàn-herd → đánh dấu `_raw_all_herd` minh bạch.
3. Nhãn lane = shadow y hệt (finding Low) — 2 surface đối chiếu được.

## Verify
Local: 21–22/07 khớp 6/6 rows lưu + lane 23/07 khớp 3/3. **VPS: sanity PASS 9/9 ô trên DB live.** Restart 22:0x · health 200 / admin 401 · journal sạch · **hash 4 bảng pre=post IDENTICAL** (`fce6bae9`/`60e876fa`/`066d773b`/`bfb0670f`). Backup 2 đầu.

## Còn lại
**(c)** wire bộ canon động (`get_output_eligible_ids()` + fallback tĩnh) cho gate money board — làm ở buổi **28/07** cùng lúc board chọn method tuần mới (chuỗi §52 đầy đủ).
