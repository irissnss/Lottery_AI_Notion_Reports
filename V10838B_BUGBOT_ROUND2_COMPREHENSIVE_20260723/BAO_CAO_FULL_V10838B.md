# V10838B — VÒNG BUGBOT TOÀN DIỆN SAU FIX + BÁO CÁO TỔNG HỢP TOÀN PHIÊN REVIEW 23/07

**GitHub folder:** https://github.com/irissnss/Lottery_AI_Notion_Reports/tree/main/V10838B_BUGBOT_ROUND2_COMPREHENSIVE_20260723
**Phiên:** 23/07/2026 20:46 → 21:5x · **Loại:** REVIEW + REPORT (READ-ONLY runtime — phiên này KHÔNG đổi code production)
**Liên quan:** V10838 (fix High + deploy 21:1x, commit private `cb6f72f`, public `e443248`, Notion `3a61d385-9bf8-81e6-b2d9-de896bf32374`)

---

## 1. DÒNG THỜI GIAN — 5 LẦN CHẠY BUGBOT TRONG NGÀY

| # | Giờ | Chế độ | Phạm vi | Kết quả |
|---|-----|--------|---------|---------|
| R1 | 20:46 | branch changes | so với base branch | **diff rỗng** — repo đứng trên `master` (chính là default branch) nên không có branch-delta |
| R2 | 20:5x | uncommitted changes | working tree | **diff rỗng** — Bugbot không tính được diff local repo này (nghi CRLF/Windows); dù `git diff` thật có 4 file |
| R3 | 20:5x | natural language (mô tả 4 file đổi) | gate V10828 money board + 2 file herd-chase + AUTOMATION_STATE | **2 finding: High + Medium** (mục 2) |
| R4 | 21:17 | natural language | commit V10838 (fix) + 2 file herd-chase | **SẠCH — 0 finding** (fix High được xác nhận đúng) |
| R5 | 21:2x | natural language + custom instructions soi sâu edge case (owner: "toàn diện") | như R4, yêu cầu soi None/empty, SQL, date, đồng bộ 2 module, drift canon, 2 script one-off | **3 finding MỚI: High + Medium + Low** (mục 4) |

Lưu ý trung thực về chữ "toàn diện": phạm vi Bugbot là **bộ thay đổi gần đây** (gate V10828/V10838 + herd-chase V10828 + 2 script V10838), soi sâu edge case — KHÔNG phải audit toàn bộ codebase hàng trăm file.

---

## 2. VÒNG 1 (R3) — 2 FINDING VÀ SỐ PHẬN CỦA CHÚNG

### 2.1 High — gate vote thiếu lọc canon → "phiếu lậu" (ĐÃ FIX trong V10838)
- `_v10759_money_board.py`: gate V10828 build `_voted` từ MỌI row `predictions` non-shadow, không giới hạn bộ 15 model canon → số 0-vote (theo nghĩa canon) vẫn có thể được "phiếu lậu" từ model ngoài canon giữ sống — đúng ca gate sinh ra để chặn.
- **Verify dữ liệu (phiên fix):** 20–23/07 zero phiếu lậu (4 ngày gần chỉ canon có row non-shadow), outcome gate 21–23/07 MB giống hệt canon-only → CHƯA gây hại thật; nhưng tiền lệ lịch sử CÓ: `claude-opus-4-20250514` 160 rows non-shadow đến 16/06 (thời chưa rename) → rủi ro tiềm ẩn thật, fix chặn trước.
- **Fix V10838:** thêm `_V10828_CANON` (đúng bộ 15, khớp AE materializer) + filter `ai_model not in canon → bỏ phiếu`.

### 2.2 Medium — frozen (khóa ngày) thắng gate (CHẤP NHẬN THEO THIẾT KẾ)
- Row `money_board_daily_lock` tồn tại → `frozen` thay `songthu` vô điều kiện, gate không được chạy lại trên giá trị đã khóa.
- Đây là bất biến "sáng = tối" owner tin dùng (V10794): gate áp tại **thời điểm TẠO lock**; row tạo bởi logic cũ chỉ tồn tại đúng ngày deploy 20/07 (`[46,69]` — đã qua). Ghi comment giải thích vào code, KHÔNG sửa hồi tố số đã freeze.

### 2.3 An toàn deploy V10838 (bằng chứng phiên fix)
Backup 2 đầu (`backups/v10838_pre/` + `/root/backups_v10838/`) · sha khớp · py_compile · sanity `compute_board()` OK (lock hôm nay nguyên: MN `[07]`, MT `[68,54]`) · restart 21:1x active · health 200 / admin 401 · journal sạch · **hash 4 bảng official pre=post IDENTICAL** (`fce6bae9`/`60e876fa`/`066d773b`/`bfb0670f`).

---

## 3. LIVE-CHECK ĐỘC LẬP SAU FIX (phiên này, 21:4x, script read-only `_v10838b_live_check.py`)

| Hạng mục | Kết quả |
|---|---|
| SHA256 file money board local (HEAD `cb6f72f`) vs VPS | `e5a3f062e1380586` = `e5a3f062e1380586` → **KHỚP** |
| Marker fix `_V10828_CANON` trên VPS | 2 dòng (kỳ vọng ≥2) ✓ |
| Service / health / admin | `active` · health **200** · `/api/admin/rule-cond` **401** (đúng chuẩn không auth) |
| Lock /choi hôm nay 23/07 | MN `["07"]` @08:53 · MT `["68","54"]` @16:47 · **MB trống** (AE `[97,02]` không trùng vote → gate chặn; cả 2 số này thực tế TRƯỢT — gate cứu tiền ngày 2, đúng option (a) owner ký) |
| Journal 30 phút (err trở lên) | 0 entries ✓ |

Kết luận: **fix V10838 đang chạy thật trên VPS, hệ sạch.**

---

## 4. VÒNG TOÀN DIỆN (R5) — 3 FINDING MỚI (TRẠNG THÁI: GHI NHẬN, CHƯA FIX)

### 4.1 HIGH — M2s "lọc herd" bị vòng qua khi coverage-rank rỗng, và nhãn nói dối
- **Vị trí:** `web/backend/_v10821_total_v2_shadow.py:247-256` (compute_picks), lặp y hệt tại `web/backend/_v10822_total_v2_lane.py` (run_for_region).
- **Cơ chế:** khi rules active và `allow = union − herd` còn ≥2 số, code gọi `_coverage_rank(preds, allow=allow)` và đặt `m2_mode="rules_minus_herd3"`. Nhưng nếu **không model canon nào vote số nào trong allow** → `_coverage_rank` trả **rỗng** → `r2f = [] + M1-nguyên-bản` → picks M2s lấy từ ranking M1 **chưa lọc herd** (số herd có thể lên làm BT), trong khi `m2_mode` vẫn ghi `rules_minus_herd3` (nhãn khẳng định đã lọc).
- **Điểm đau nhất:** kịch bản "không ai vote số sạch" thường xảy ra đúng **ngày bầy đàn dồn phiếu vào số herd** — tức bypass kích hoạt đúng ngày cần lọc nhất.
- **Phạm vi tác động:** surface đo shadow (`v10821_total_v2_daily`) + lane test (`du_doan_test_bundles`) — **KHÔNG đụng official `/du-doan`**. Tác hại chính: chuỗi số liệu A/B bị dán nhãn chế độ sai → ngày như vậy lọt vào nhóm "đã lọc herd" làm bẩn phép đo ngưỡng 04–11/08.

### 4.2 MEDIUM — `_V10828_CANON` tĩnh có nguy cơ lệch registry động
- **Vị trí:** `web/backend/_v10759_money_board.py:515-529`.
- **Cơ chế:** `generate_final_bundle` (main.py) lọc phiếu theo `get_output_eligible_ids()` **động** từ `model_registry`; gate money board dùng bộ **tĩnh** 15 model. Nếu owner thêm model output-eligible mới vào registry: model đó vote trong bundle official nhưng gate /choi **bỏ phiếu của nó** → cặp AE hợp lệ có thể bị strip về `None` (mất lock ngày đó) **âm thầm, không báo lỗi**.
- **Hiện trạng:** registry đang đúng bộ 15 → **CHƯA có tác hại**; đây là rủi ro cấu trúc tương lai. Ghi chú thêm: hệ hiện có ≥3 bản sao bộ canon (registry/main.py · `CANON` trong `_v10821` · `_V10828_CANON`) — drift risk nhân lên theo số bản sao.

### 4.3 LOW — nhãn `m2_mode` lệch nhau giữa 2 surface cùng một nhánh
- **Vị trí:** `web/backend/_v10822_total_v2_lane.py:150-155` vs `_v10821_total_v2_shadow.py`.
- Cùng nhánh "herd dọn allow còn <2 số": lane ghi `fallback_m1`, shadow ghi `fallback_m1_herd_cleared` → consumer monitoring/`risk_flags_json` không phân biệt được fallback-do-herd với fallback thường ở lane; đối chiếu chéo 2 surface theo `m2_mode` sẽ lệch.

---

## 5. VÌ SAO PHIÊN NÀY KHÔNG FIX 3 FINDING MỚI (QUYẾT ĐỊNH + CĂN CỨ)

1. **Lệnh đứng của owner (00:22 21/07, FU-V10828):** "không coi đây là tư duy điều kiện — giữ như hygiene tạm, **đo catalog V10829 thay vì vá tiếp**"; FU-V10829 next_action ghi rõ: "**CẤM vá phản xạ / mở rộng anti-herd ad-hoc giữa cửa sổ đo**" (cửa sổ forward đến 04–11/08). Finding High + Low nằm CHÍNH XÁC trong vùng cấm vá này (shadow/lane đo lường đang chạy forward).
2. Finding Medium chưa có tác hại hiện tại (registry khớp 15) và cách sửa đúng chạm runtime `/choi` (đọc registry động + fallback tĩnh) → cần owner ký riêng, không tự ý.
3. Yêu cầu phiên này của owner = review toàn diện + báo cáo + push GitHub (không yêu cầu fix).

**3 option trình owner (chọn theo mức):**
- **(a) Sửa nhãn thuần telemetry** (High phần-nhãn + Low): khi coverage rỗng đặt `m2_mode="fallback_m1_no_coverage"` (2 surface dùng CÙNG chuỗi) — không đổi hành vi pick; nếu làm giữa cửa sổ đo phải chú thích mốc đổi nhãn để chuỗi số liệu đọc đúng.
- **(b) Sửa hành vi herd-bypass** (strip herd khỏi cả fallback M1 của M2s, hoặc trả rỗng trung thực kiểu NO_QUALIFIED_PICK như lane V3): đổi hành vi lane/shadow giữa cửa sổ đo → khuyến nghị GHI NHẬN bây giờ, quyết CÙNG mốc đọc ngưỡng 04–11/08 (trừ khi owner muốn sớm).
- **(c) Fix canon drift:** wire `get_output_eligible_ids()` động + fallback bộ tĩnh khi registry lỗi — làm vào lần chạm money board kế tiếp, kèm chuỗi §52 đầy đủ.

Khuyến nghị của em: **(a) làm sớm được** (rẻ, không đổi hành vi, cứu độ sạch của phép đo), **(b)+(c) gộp vào buổi quyết 28/07 hoặc mốc 04–11/08**.

---

## 6. GOVERNANCE PHIÊN NÀY

- **FU mới:** `FU-V10838B-BUGBOT-ROUND2` — status `MEASURED_BUT_NOT_FIXED (PENDING_OWNER options a/b/c)`.
- **Docs cùng phiên:** CHANGELOG V10838b · SSOT block V10838B · FU tracker (item mới + cross-ref FU-V10828) · AUTOMATION_STATE seq 300 (seq 299 thuộc V10839 markdownlint — phiên song song cùng tối) · AUTOMATION_HISTORY +1 dòng.
- **Runtime:** ZERO thay đổi (chỉ thêm script read-only `_v10838b_live_check.py` vào repo private).
- **Roadmap check (rule phiên):** 6 roadmap ACTIVE, **không checkpoint nào quá hạn** tại 23/07; mốc gần: 26/07 (CP-R4 auto-action re-trình + CP-S4 gỡ cron addendum) · 28/07 (CP-L6 RE-VERIFY quyết một buổi: K11a/K15/lean-roster/CP-R4/glm-5.1 + chốt trial V10820 + lane V2/V3) · 04–11/08 (đọc ngưỡng catalog V10829 + nhát cắt source_region FU-V10836).
- **Commit:** public repo (folder này) + private repo (docs + script) — ID ghi trong AUTOMATION_STATE và message commit.

---

## 7. TÓM MỘT ĐOẠN CHO NGƯỜI ĐỌC NHANH

Fix V10838 (lọc canon cho gate chống số-0-vote ở /choi) đã được vòng re-review xác nhận đúng và live-check xác nhận đang chạy trên VPS, hệ sạch. Vòng soi sâu theo lệnh "toàn diện" tìm thêm 3 điểm mới — nặng nhất là M2s shadow/lane có thể vòng qua bộ lọc herd đúng ngày bầy đàn mạnh nhất và dán nhãn sai chế độ; cả 3 đều KHÔNG đụng official /du-doan và đều được ghi nhận chờ owner quyết (option a/b/c), đúng lệnh đứng "không vá ad-hoc giữa cửa sổ đo".
