# V10707/V10708 — MN/MT DOCTRINE SHADOW A/B (áp phương pháp MB cho MN/MT) — 2026-06-10

**Trạng thái:** DEPLOYED — đo forward từ 2026-06-11. Shadow-only, zero official drift.

## 1. Mục tiêu
Trả lời bằng phép đo có kiểm soát: "Rules đưa vào prompt AI (doctrine — phương pháp đang dùng cho MB) có giúp MN/MT không?" — đo song song với A/B doctrine MB (mốc 19/06), độc lập tuyệt đối theo miền × thứ.

## 2. Thiết kế A/B (chỉ khác DUY NHẤT 1 biến)
- **TREATMENT** = gọi lại CHÍNH 7 LLM official với prompt CÓ doctrine (rule stack weekday-bound + doctrine text riêng miền).
- **CONTROL** = picks của đúng 7 model đó từ luồng official cùng ngày (prompt KHÔNG doctrine — không gọi thêm).
- Context (nguồn dữ liệu, settings, learned intelligence, post-filter) mirror Y HỆT luồng official.
- Vote đối xứng (top1=1.0, top2=0.5) trên đúng tập model thành công của cả 2 phía.
- Causal: chạy TRƯỚC giờ xổ miền target; rule context từ dữ liệu ≤ D-1; guard chặn chạy sau xổ.

## 3. Doctrine riêng từng miền (KHÔNG copy mù MB)
- **MN**: xổ ĐẦU ngày → nguồn DUY NHẤT = D-1 (không miền nào same-day); 3 đài/ngày (T7: 4) → ưu tiên tail hội tụ ≥2 tín hiệu; cửa sổ 12W/16W.
- **MT**: xổ SAU MN → được dùng MN(D) same-day làm tín hiệu nóng + D-1; cấm tuyệt đối MB(D); 2-3 đài/ngày.
- RULE STACK weekday-bound của CHÍNH miền: PRODUCTION 5 rule/thứ (cross-verify) + MANUAL (soi-cầu target-miền, CONFIRM-only).

## 4. V10708 — tầng học tập tích lũy + phân loại + xếp hạng (hoàn thiện phương pháp MB)
- Daily ranker cho MN/MT (mirror cơ chế MB): recompute hit-rate 4/8/12/16 tuần từ bảng hiệu quả rule (chấm hằng ngày), composite cửa sổ RIÊNG MN/MT (nhấn 12W/16W — khác MB nhấn 8W), **vòng đời** MẠNH / TĂNG_TRƯỞNG / ỔN_ĐỊNH / XUỐNG_CẤP / YẾU, xếp hạng lại mỗi sáng per (miền × thứ).
- Snapshot ngày đầu (10/06): MN 35 rule = 15 MẠNH / 13 TĂNG / 7 GIẢM; MT 35 = 9 MẠNH / 15 TĂNG / 11 GIẢM.
- Doctrine prompt hiển thị vòng đời từng rule (như MB).

## 5. Vận hành & an toàn
- Lịch: ranker 04:40 → MN A/B 05:00 → MT A/B 16:50 (đều SAU official, TRƯỚC giờ xổ → không ảnh hưởng giờ cung cấp số người dùng).
- Shadow tuyệt đối: chỉ ghi bảng lane-test + bảng context mới; 4 bảng official hash-check mỗi run (`official_tables_touched=0`); cờ test_only/output_eligible=0.
- Gate prompt chỉ tồn tại trong process runner (không vào cấu hình service) → prompt official MN/MT không đổi.
- Smoke test thật (1 model): doctrine làm model đổi pick top1 — đúng hiệu ứng cần đo; zero drift xác nhận.

## 6. Theo dõi & mốc quyết
- UI: panel "🧭 A/B Doctrine (rules → prompt)" trên trang lane-test admin — hôm nay treatment vs control + tích lũy + số model đổi pick.
- CLI: `--report` per miền + per thứ.
- **Mốc quyết per-miền ~24/06**: GO official nếu treatment > control ≥ +5pp BT bền (n≥10-14 ngày); DROP nếu ≤. Đối chiếu cùng kết quả A/B doctrine MB 19/06.
- Chi phí: ~14 lượt LLM/ngày (owner chấp nhận, ~2 tuần).

## 7. Bối cảnh nghiên cứu liên quan (V10705, 09-10/06)
- Backtest công bằng 90-120d: bộ chọn official đã gần TRẦN dữ liệu (tách đài/thứ/bỏ-ML đều không vượt OOS) → doctrine-vào-prompt là đòn bẩy còn lại chưa đo cho MN/MT; phép đo này khép lại câu hỏi đó bằng số liệu thật.
