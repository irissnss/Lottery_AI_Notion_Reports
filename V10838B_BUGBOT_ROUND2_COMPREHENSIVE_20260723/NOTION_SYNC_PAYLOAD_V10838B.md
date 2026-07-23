# V10838B — Bugbot vòng 2 toàn diện sau fix: re-review SẠCH; vòng sâu ra 3 finding mới (chưa fix — đúng lệnh không vá ad-hoc) (23/07)

**GitHub:** https://github.com/irissnss/Lottery_AI_Notion_Reports/tree/main/V10838B_BUGBOT_ROUND2_COMPREHENSIVE_20260723

## Kết quả 5 lần chạy Bugbot 23/07
- R1/R2 (branch + uncommitted): diff rỗng (repo trên master; Bugbot không tính được diff local) → dùng chế độ mô tả.
- R3: 2 finding (High phiếu-lậu canon → **ĐÃ FIX V10838**; Medium frozen thắng gate → **thiết kế, ghi comment**).
- R4 (sau fix): **SẠCH 0 finding**.
- R5 (owner: "toàn diện"): **3 finding MỚI** — chỉ chạm shadow/lane + rủi ro tương lai, KHÔNG đụng official /du-doan.

## 3 finding mới (GHI NHẬN — CHƯA FIX)
1. **High:** M2s shadow/lane vòng qua bộ lọc herd khi `_coverage_rank` rỗng (không model nào vote số sạch) → picks rơi về M1 chưa lọc, `m2_mode` vẫn ghi `rules_minus_herd3` (nhãn sai) — kích hoạt đúng ngày bầy đàn mạnh nhất, làm bẩn phép đo A/B.
2. **Medium:** `_V10828_CANON` tĩnh ở money board vs `get_output_eligible_ids()` động ở main.py — thêm model registry mới là gate bỏ phiếu âm thầm → AE pair hợp lệ có thể mất lock. Hiện registry khớp 15 → chưa hại.
3. **Low:** nhãn `m2_mode` cùng nhánh nhưng lane ghi `fallback_m1`, shadow ghi `fallback_m1_herd_cleared` → 2 surface không đối chiếu được.

## Vì sao chưa fix + option chờ owner
- Lệnh đứng owner 00:22 21/07 (FU-V10828/FU-V10829): "đo catalog V10829 thay vì vá tiếp; CẤM vá ad-hoc giữa cửa sổ đo (đến 04–11/08)".
- **(a)** sửa nhãn thuần telemetry (làm sớm được) · **(b)** sửa hành vi herd-bypass (quyết cùng 04–11/08) · **(c)** wire canon động + fallback (lần chạm money board kế tiếp). Khuyến nghị: a sớm, b+c gộp mốc 28/07 / 04–11/08.

## Live-check fix V10838 (read-only, 21:4x)
sha VPS = HEAD `e5a3f062e1380586` khớp · marker `_V10828_CANON` ×2 · service active · health 200 / admin 401 · journal sạch · lock 23/07 nguyên: MN [07] · MT [68,54] · MB trống (gate chặn AE [97,02] — cả 2 số trượt thật = gate cứu tiền ngày 2).

## Governance
FU mới `FU-V10838B-BUGBOT-ROUND2` (MEASURED_BUT_NOT_FIXED, PENDING_OWNER) · CHANGELOG V10838b · SSOT · AUTOMATION_STATE seq 299 · ZERO đổi runtime · roadmap không mốc quá hạn (gần nhất 26/07 · 28/07 · 04–11/08).
