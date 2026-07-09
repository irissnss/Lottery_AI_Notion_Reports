# V10788 — Audit toàn bộ mốc tổng hợp (09/07/2026)

**Câu hỏi owner:** ML có tổng hợp sớm/muộn với các mốc không hợp thời điểm không? Kiểm tra toàn bộ mốc — mốc nào ổn định, hoạt động đúng thiết kế?

**Kết quả chính (7 probe READ-ONLY):**
- Mốc GIỜ chạy đúng thiết kế 100%: ML 04:00 (data D-1) · chain MT 16:35-41 · chain MB 17:30-42 · T-10 chốt · freeze :55 · retrain CN 02:00 · dedupe OK. Model về sau T-10 = shadow, không có phiếu → không có race bug.
- Mốc hỏng THẬT = cấu trúc phiếu: official MT 08/07 BT=59 thắng bằng 6 phiếu ML `auto_daily` 04:00 chụm (0.194 đè AI tươi 0.142); 09/07 khối lại chụm 59 = số vừa thua.
- Rerun MB 17:30 (tổng hợp muộn) VÔ DỤNG: 139 đổi → +21/−21 hoà tuyệt đối. AUC retrain MB 0.497 = tung xu.
- Echo theo miền (60d): lag1 MN +12pp · MT +6pp · **MB −6pp (ngược)** · MT→MB +7pp · MN→MT ≈0. Bảng V66 BOOST khớp audit độc lập — AE đúng thiết kế.
- Chasing 30d: MB AI đuổi số hôm trước 47% ngày, hit 17% vs 31% không đuổi = tự sát tại MB; MN đuổi có lợi.

**Deploy 10:07:** panel ⏱ MỐC & NHỊP mỗi miền `/monitoring` (lag1/cross vs nền + chase + rerun± + nhịp runtime). Sandbox PASS, health 200/admin 401, hash 4 bảng IDENTICAL. DIAGNOSTIC-ONLY.

**Quyết định chờ owner:**
- K13 (MỚI): shadow `RECENCY_WEIGHT_V1` — vote 7d×60%+30d×40% (phản chứng: 43% vs actual 29%).
- K10: shadow `ML_BLOC_DEDUP_V1` (khối sibling = 1.5 phiếu). K9: shadow `HERD_FADE_V1`. K11a: promote `MB_OUTPUT_V1` sau 10/07.
- 3 shadow chạy song song được; sau 14 ngày so 4 selector cùng thước rồi mới bàn official.

**Commit private:** `8064514` · Báo cáo đầy đủ: GitHub `Lottery_AI_Notion_Reports/V10788_MILESTONE_AUDIT_20260709_PUBLIC_SAFE/BAO_CAO_TONG_V10788.md`
