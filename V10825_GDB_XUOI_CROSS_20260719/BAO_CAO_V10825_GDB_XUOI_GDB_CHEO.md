# V10825 — "26 = 2 SỐ ĐẦU KHÔNG ĐẢO CỦA GĐB MB + ĐIỀU KIỆN GĐB SOI CẦU 3 MIỀN" (owner phát hiện 23:07 19/07)

**Câu owner:** "số 26 nằm ở chỗ hàng chục nghìn và hàng nghìn không đảo của miền bắc nằm ở giải đặc biệt đó em. xem điều kiện là kèm là so sánh với các giải đặc biệt dùng để soi cầu của 3 miền trong đó miền nam có giải đặc biệt có 26 đó em ==> xem lại dùm anh tất cả toàn diện 1 lần nữa, đề xuất an toàn tổng lực là gì em?"

**Phiên:** 19/07 23:07 → 23:3x · probe read-only + deploy shadow-only (zero đụng official) · §52 đầy đủ

---

## 1. VERIFY INSTANCE — ANH ĐÚNG 100%

| Thành phần | Giá trị | Ghi chú |
|---|---|---|
| GĐB MB 18/07 | **26890** | 2 số đầu (chục nghìn + nghìn) KHÔNG đảo = **26** |
| GĐB MN 19/07 (3 đài) | 310228, **486026**, 087842 | đài thứ 2 **đuôi = 26** — quay 16:15, TRƯỚC MB 18:15 → điều kiện CAUSAL hợp lệ |
| GĐB MT 19/07 (3 đài) | 048363, 359736, 136472 | không chứa 26 |
| Kết quả | **26 VỀ lô MB 19/07** ✓ | đối xứng rule đảo V10816: đảo → 62 TRƯỢT hôm nay, xuôi → 26 VỀ |

## 2. BACKTEST TOÀN DIỆN 6.5 NĂM (2.333 cặp ngày D → D+1) — TRUNG THỰC: TRONG NHIỄU

| Phép đo | n | Hit | % | Nền | z |
|---|---|---|---|---|---|
| Xuôi KHÔNG điều kiện | 2.333 | 577 | 24.7% | 23.8% | +1.08 |
| — nửa đầu lịch sử | 1.166 | 316 | **27.1%** | 23.8% | +2.68 |
| — nửa sau lịch sử | 1.167 | 261 | **22.4%** | 23.8% | **−1.15** |
| X1: cand = ĐUÔI GĐB MN(D+1) 16:15 | 76 | 20 | 26.3% | 23.8% | +0.51 |
| X3: cand = ĐUÔI GĐB MN∪MT(D+1) | 123 | 33 | 26.8% | 23.9% | +0.77 |
| X4: cand ⊂ GĐB MN∪MT(D+1) chuỗi-con | 551 | 137 | 24.9% | 23.7% | +0.62 |

**Placebo bắt buộc (bài học V10817):** chạy CÙNG điều kiện GĐB-chéo trên cả **20 biến thể vị-trí** cặp chữ số GĐB → median z = −0.48, max z = +2.60 nhưng thuộc **pos24** (không phải biến thể owner), biến thể owner pos01 xếp hạng **5/20**, chỉ 1/20 đạt z≥2. → Mức 26-27% của X1/X3 **chưa vượt nhiễu chọn-lọc**. Phần dương của xuôi nằm trọn ở nửa đầu lịch sử (2019-2022), nửa sau DƯỚI nền.

Tần suất tín hiệu: X4 ~7.1 lần/tháng; X3 ~1.6 lần/tháng (30 ngày forward chỉ cho n≈5 → ngưỡng viết rõ n≥12).

## 3. ĐỀ XUẤT AN TOÀN TỔNG LỰC (đã deploy trong phiên)

Theo đúng nguyên tắc V10801 (bằng chứng mâu thuẫn/trong nhiễu → KHÔNG đổi production, ĐO shadow với ngưỡng viết sẵn):

1. **KHÔNG** đưa vào official/prompt/rule engine — đang giữa trial V10820 (ngày-2) + lane TOTAL_V2 (ngày-1), nguyên tắc 1-biến-số/lần; và backtest nói trong nhiễu.
2. **CÓ** đo forward công khai từ 19/07: khối **➡️ BẢN KHÔNG ĐẢO + GĐB CHÉO** gắn ngay dưới tracker GĐB-đảo trong panel 🔄 `/monitoring`:
   - Bảng xuôi + X1/X3/X4: full 6.5y / 2 nửa / 120 tín hiệu gần / **FORWARD từ 19/07**.
   - 10 ngày gần nhất có đánh dấu ˣ = ngày có tín hiệu GĐB chéo.
   - **WATCH LIVE:** ngày mai 20/07 cand xuôi = **46** (GĐB 19/07 = 46438) — X1/X3 panel TỰ chấm ngay sau MN 16:15 / MT 17:15, anh thấy tín hiệu TRƯỚC giờ MB quay 18:15. (Lưu ý thú vị: 46 cũng chính là số cả bầy AI vừa đuổi hôm nay — quan sát kép.)
3. **Ngưỡng hành động viết sẵn:** ~02/08 (14d): X3 ≥6/14 → báo anh sớm · ~18/08 (30d, cùng mốc rule-đảo 16/08): X3 ≥40% (n≥12) → trình anh cân nhắc side-bet; ≤~28% → đóng cùng rule gốc.
4. Khối GĐB-đảo V10816 + điều kiện V10817 giữ NGUYÊN — hai anh em xuôi/đảo đọc cùng một mốc.

## 4. XEM LẠI TOÀN DIỆN TRƯỚC 0H (câu 2 của anh)

- Service active · health 200 · admin 401 · journal sạch.
- Ngày forward-1 đã chốt ở V10824: lane 3 miền đúng giờ (MN trúng BT 90), shadow forward đủ, A/B đủ, trial ngày-2 any 27/42 = 64% chưa chạm guard-rail.
- Rules sẵn sàng: 105 active; miner weekly chạy 00:30 đêm nay (restart deploy đã né trước, 23:20).
- CP-L6 vẫn đang CHỜ ANH KÝ 3 mục (flip K11a về champion / K15 giữ đến 23/07 / lean-roster dời sau 28/07).

## 5. §52 CHAIN

Backup 2 đầu trước sửa (`backups/v10825_pre/` + VPS `/root/backups_v10825/`) · sha khớp 2 file · py_compile + node --check pass · **sandbox /tmp chạy bản mới TRƯỚC deploy** (số khớp probe) · restart 23:20 active · health 200 · chase-bias unauth 401 · view sống (watch cand 46) · **hash 4 bảng official IDENTICAL** (d8785a51/f23cbcc6/42a3d128/d93423b5).

Artifacts: `web/backend/_v10825_gdb_xuoi_probe.py` · `_v10825_sandbox.py` · `_v10825_deploy.py`

## 6. ADDENDUM 23:45 — OWNER QUYẾT CP-L6: CHỜ THÊM + RE-VERIFY TRƯỚC KHI XỬ LÝ

Nguyên văn owner: *"chờ thêm đi em? sau đó trước khi xử lý cầm verify lại để xác thực 1 lần nữa nha em, lỡ dầu prompt mới lại thay đổi kế hoạch, phương án đó em."*

- **KHÔNG flip K11a** — điểm owner bắt rất chuẩn về đo lường: 11 ngày challenger 1/11 vs champion 4/11 đo gần trọn dưới PROMPT CŨ; RULES-FIRST (live 18/07) đổi tín hiệu đơn-model = đổi đầu vào của chính lane → số cũ không còn là căn cứ hợp lệ.
- Hiện trạng giữ nguyên: lane `MB_OUTPUT_V1` tiếp tục chạy official MB; kill-switch 5-thua-liên-tiếp vẫn tự canh độc lập.
- Cả gói agenda CP-L6 (K11a · K15 · lean-roster opus/gpt-5.4 · retire glm-5.1 · CP-R4 · 10 món sổ tay mục 5) dời về **28/07**, quyết MỘT buổi cùng chốt trial V10820 + Total-V2 + lane 10 ngày.
- **Giao thức RE-VERIFY bắt buộc trước mọi xử lý** (ghi tại `ACTIVE_ROADMAP_LEAN_HARVEST_20260619.md` mục 2): chạy lại K-lanes TÁCH 2 ĐOẠN pre-trial (≤17/07) vs in-trial (18/07→27/07) — chỉ đoạn in-trial làm căn cứ; K11a cần ≥6 ngày phân-định; K15 trio 23/07 chỉ đọc-ghi-nhận; trial gia hạn +7 ngày → CP-L6 dời theo.
- Ghi nhận: `DECISION_LOG.md` 19/07 23:45 · CHANGELOG V10825 addendum 5 · playbook §5 · FU-V10824 · sổ tay mục 3/5/9 · AUTOMATION_STATE seq 287. **Doc-only — zero runtime, zero deploy, hash 4 bảng không đụng.**
