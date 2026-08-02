# REPORT_V10973 — Kiểm soát đối chiếu owner (2026-08-02)

**Giờ VN:** 02/08/2026 ~21:55+ · **Phạm vi:** chỉ đọc + báo cáo · **Không sửa production** · **Không ghi Notion**

## 1. Tóm tắt một đoạn

**CHƯA hết chặt: đã kiểm soát cứng phần quyết định/cổng/ghi nhận (✅11); còn hở hàng đợi freeze/08/08 (🟡15) và 2 mục đỏ thiếu đào/đóng.**

Đối chiếu transcript owner + sổ quyết định + FU treo + SSOT/CHANGELOG + báo cáo V10945–V10972 + briefing đầu phiên. Ledger **0 TRÔI**. Briefing: **0 checkpoint quá hạn**, **82 FU treo**, **0 quá hạn cứng**. Máy mới: **chỉ kế hoạch**, chưa chuyển. Đếm bảng bắt buộc: **✅ 11 · 🟡 15 · 🔴 2 · ⚪ 2**.

## 2. Owner yêu cầu gì (nguyên văn)

> Owner làm rõ: CHƯA chuyển máy mới (chỉ là kế hoạch). Câu hỏi thật:
> **Toàn bộ hệ thống hiện đã được kiểm soát chặt chẽ hết chưa? Các vấn đề anh đã nêu / nhắc / góp ý / đề cập đã được ghi nhận, đào bới, kiểm tra hết chưa?**
> Trả lời trung thực, có bằng chứng — phân loại ✅ / 🟡 / 🔴 / ⚪.
> Deliverable V10973… Push public… Gate PASS. Không sửa production. Không Notion write.

## 3. Đào bới / phát hiện

### 3.0 Máy kiểm đầu phiên + sổ

| Kiểm | Kết quả |
|---|---|
| `_v10920_session_start.py` | 0 CP quá hạn · 82 FU treo · 0 quá hạn cứng |
| `_v10920_decision_ledger.py` | **0 TRÔI** · 19 quyết định ACTIVE · QD-013…019 khớp |
| Consistency (V10969) | 16/16 OK |
| Edge gate (V10969/70) | ĐÓNG 3 miền |

### 3.1 Bảng đối chiếu đầy đủ

| ID | Class | Chủ đề | Owner nêu gì | Ghi nhận (QD/FU/doc) | Đã đào? | Đã xử lý? | Còn hở gì | Hạn |
|---|---|---|---|---|---|---|---|---|
| T01 | ✅ | Edge / P&L / cổng lợi thế | Hệ 90 ngày lỗ lớn, không hơn đánh bừa; cần cổng thống kê trước khi đặt | QD-013 · FU-208 · V10945 · _v10945_edge_gate | V10945: vốn 579,2tr / thu 445,9tr / lỗ −133,3tr (−23%); hòa vốn MN/MT  | YES_GATE_DEPLOYED | Cổng vẫn ĐÓNG 3 miền (02/08); không mở vì 1 ngày đẹp | LX (giữ đến khi ≥3pp và z≥2) |
| T02 | ✅ | Dừng đặt tiền thật | Dừng đặt tiền thật tới khi chứng minh lợi thế | QD-013 · FU-208 OWNER_LOCK | V10945 + V10969/70: edge 90d ĐÓNG | YES_DECISION_LOCKED | Chỉ cần giữ kỷ luật khi có tuần đẹp | LX |
| T03 | 🟡 | Freeze đường ra số tới 08/08 | Có. Hôm qua đổi ba thứ cùng lúc, cần một tuần yên… | QD-014 · OD-20260801-D · FU-215 DB0808 | V10956 khóa quyết định; ledger khớp 7/7 | YES_LOCKED_WAIT_WINDOW | Không tỉa roster/combo/cách tính số tới hết 08/08 | 08/08 |
| T04 | 🟡 | MT mất tín hiệu / lợi thế tắt tháng 6 | MT từng hơn bừa rồi tắt; tín hiệu còn nhưng không ra số trúng | FU-210 DO0808-1 · FU-212 TDLX-212 | V10947/55/55b: RF→vote→công bố rơi −7,59pp; AUC MT còn 0,52–0,55 | NO_ROOT_FIX (đóng băng + chờ shadow RF) | Chỗ gãy vote/ghi đè chưa sửa production; chờ QD-015 sau 08/0 | 08/08 |
| T05 | 🟡 | RF shadow đơn (sau freeze) | Duyệt trước để 08/08 tự chạy shadow RF, tự cắt nếu khớp <95%/7d | QD-015 · FU-216 XH0808-1 | V10955b/57: live RF +3,42pp ≠ CSV holdout −2pp — hai thước khác nhau | NO_RUNTIME_YET (chờ hết freeze) | Chưa bật shadow RF trên VPS | 08/08 |
| T06 | 🟡 | RULES-FIRST herding / ép chọn từ list | Prompt có ép model hội tụ? Bỏ bắt buộc chọn từ danh sách trên shadow | QD-016 · FU-231 · FU-222 · V10959 | V10959: list ~12,4%≈bừa; model chọn từ list ~35,8% | NO_RUNTIME_YET (sau 08/08, shadow) | Production vẫn RULES-FIRST; chỉ shadow sau freeze | 08/08 → 22/08 (FU-222) |
| T07 | 🟡 | Prompt A/B cùng model | Hai prompt song song trên CÙNG model ≥14 ngày, chấm BT | QD-017 · FU-226 HT0808-2 · FU-223 | V10959 đề xuất; chi phí ước 15–25 USD | NO_RUNTIME_YET | Chưa chạy A/B | 08/08 |
| T08 | ✅ | Retrain / AUC journal | Vì sao huấn luyện hỏng nhiều / không ai biết model tốt hay tệ | FU-211 CLOSED · V10952 · V10953 | 7 CN chết I/O closed file; từ 19/07 AUC=0 dù OK; sửa ghi AUC | YES_FIXED | AUC MN/MB ~0,50 vẫn yếu — tín hiệu, không còn bug journal | — |
| T09 | 🟡 | Ranking WR vs bạch thủ | Bộ lọc/chấm WR trong khi anh đánh bạch thủ | V10938 · FU-230 · FU-232 SC0815-3 | meta-learning lệch −10,9pp; V10965 WR vs BT lệch tới +47pp (sonnet MN) | PARTIAL — combo-super đổi BT; trọng số số còn WR ( | Nửa V10938 còn WR; đồng bộ thước toàn hệ chưa xong | 15/08 |
| T10 | ✅ | gpt-5.4 gọi về / combo-no-token ra total | Cắt gpt-5.4 vội bằng một thước; cần gọi về | V10937 · V10939 · FU-204 | BT dưới mặt bằng nhưng WR trên + xu hướng lên | YES_DEPLOYED — pool 15 có gpt-5.4, không combo-no- | Canh tới 15/08 gpt-5.4 có giữ chất lượng không | 15/08 |
| T11 | 🟡 | UI /du-doan-test + /filter | Neo ngày sai / filter khó xem / lệch múi giờ | FU-225 UI0803 · V10960 · V10964 · V10964b | Owner nhầm MN là hôm qua vì thiếu nhãn; getVNDateISO nhảy ngày | YES_DEPLOYED — Cache-Control no-store; neo request | Owner hard-refresh xác minh UI tới hạn 03/08 | 03/08 |
| T12 | 🟡 | Deploy giờ cấm / chạm T-chốt | Deploy 17:45 đụng T-chốt 17:55; model_count 15→14 | FU-207 DP0808 · FU-237 DP0815 · V10940 · V10968 | V10968 chốt cửa sổ cấm 05:00–06:30 và 15:30–18:15 trong governance_gua | PARTIAL — cổng giờ đã ghi; nâng đủ MB qua 17:58/v2 | FU-207 chưa nâng đủ điều kiện v2; FU-237 canh live | 08/08 / 15/08 |
| T13 | ✅ | Múi giờ VN / FINAL marks | MN 15:45 · MT/MB 16:58/17:58; biên 2 phút; giờ VN nhất quán | OD-20260731-A/B/C · V10931 · V10962 · §55 | V10961 từng TRÔI 16:53; V10962 sửa → hiện khớp 4/4 | YES — FREEZE_MARKS + ledger + consistency C10–C13 | Không | — |
| T14 | ✅ | Mã công việc §58 phương án B | Số hiệu viết tắt + hạn ngày; chọn B | QD-019 · §58 · V10967 · DE_XUAT_QUY_UOC_MA_CONG_VIEC.md | Áp ma_doc trên QD/FU treo; cổng thieu_ma_doc trong briefing | YES_GOVERNANCE | Một số FU lịch sử LX vẫn generic | — |
| T15 | ✅ | Notion chỉ đọc | Notion MCP chỉ tham khảo, không cập nhật Notion | OD-20260801-F · §57 · FU-221 | V10961: Notion đứng đông 01/08 16:43 — lỗi thời so SSOT | YES_RULE_LOCKED — agent không ghi Notion | Owner tự cập nhật tay Notion nếu cần; truth = SSOT+VPS | LX |
| T16 | 🟡 | Báo cáo GitHub A55 | Sau mọi code/fix/audit phải đẩy report public đủ 9 phần | §57 · FU-188b · _v10921_report_gate | V10961 thiếu vài bản → V10962/69 bù; V10970/71/72 có | YES_RECENT — backlog cũ FU-188 còn | FU-188 tồn đọng báo cáo cũ hạn 10/08 | 10/08 |
| T17 | ✅ | Consistency guard | Tự kiểm mốc giờ / tz / FINAL phải khớp | _v10900_consistency_guard · cron 18:05 | V10969: 16/16 OK trên VPS | YES_LIVE_OK | Chạy hằng ngày | hằng ngày |
| T18 | 🔴 | Bundle thiếu model MT13/MB14 (02/08) | Kiểm tổng lực / đủ phiếu / nhất quán 15 model | V10969 REPORT+evidence; nhắc FU-184/189 — CHƯA có FU riêng root-cause | PARTIAL — biết MT=13 MB=14 MN=15; CHƯA liệt kê model nào timeout/empty | NO | Thiếu đào model-level + thiếu mã FU riêng; dễ lặp thiếu phiế | đề xuất 05/08 |
| T19 | 🟡 | LSTM live lệch suy luận | LSTM chạy live có khớp suy luận không | FU-217 SC0808-1 · V10957 | V10957 đo lệch live vs suy luận | NO (QD-014 đóng băng) | Chờ hết freeze mới sửa | 08/08 |
| T20 | 🟡 | Weight optimizer làm tệ | Tắt bộ tối ưu trọng số (đang làm tệ đi) — sau 08/08 | QD-018 B1 · FU-233 HT0822-1 · V10965 | V10965: lift tốt nhất âm cả 3 miền; cron CN 03:00 còn sống | NO_YET (tuần tự sau freeze) | Chưa tắt optimizer | 22/08 |
| T21 | 🟡 | 105 rules có giúp công bố? | Đo xem 105 luật có giúp gì không (sau B1) | QD-018 B2 · FU-234 DO0905 · V10965 | 105 active v2026W31; chưa đo giúp số công bố | NO_YET | Chưa đo causal | 05/09 |
| T22 | ✅ | QD-013…QD-019 toàn bộ | Mọi quyết định phải ghi sổ + kiểm code | OWNER_DECISION_LEDGER.json — 19 quyết định ACTIVE | _v10920_decision_ledger.py 02/08: 0 TRÔI; QD-013..019 khớp | YES_LEDGER | Không TRÔI | — |
| T23 | 🟡 | FU còn mở (treo) | Các vấn đề ghi nhận chờ hạn / OWNER_LOCK | FOLLOW_UP_TRACKER + _v10958_fu_reader → 82 treo | Session start 02/08: 82 treo · 0 quá hạn cứng | INTENTIONAL_QUEUE | Nhiều DEPLOYED_PENDING lịch sử (FU-118..) chưa đóng; nhiễu k | theo từng FU |
| T24 | ✅ | Owner frustration — hỏi lại việc đã ký | Anh không muốn nhắc tới nhắc lui… em phải tra được | §56 A54 · OD-20260801-E · FU-187 · _v10920_session_start | Vi phạm thật CP-L2 01/08; đã dựng briefing + ledger | YES_PROCESS | Cần chứng minh agent không hỏi lại trong cửa sổ 7 ngày | 08/08 |
| T25 | 🟡 | Lane cleanup CP-L2 | Luồng rối — cắt cron research thừa | CP-L2 DONE V10919 · OD-20260801-B · FU-185 còn tinh gọn thêm | 12 cron nghỉ 83→71; CP-L2 từng quá hạn 37 ngày | YES_CORE; FU-185 còn MEASURED_BUT_NOT_FIXED | FU-185 hạn 03/08 — dọn lane đo chồng thêm | 03/08 (FU-185) |
| T26 | 🔴 | FU-184/189 xác minh 02/08 | MT/MB công bố đúng phiếu; lane nghỉ phải vắng | FU-184 KS0802-2 · FU-189 KS0802-1 WAIT_LIVE hạn 02/08 | V10969 có bundle counts; CHƯA đóng FU bằng checklist xác minh đầy đủ | NO_CLOSE | Hạn hôm nay — thiếu bước đóng có bằng chứng; liên quan T18 | 02/08 |
| T27 | ⚪ | CP di sản CROSS_REGION quá hạn | Đóng hết. Chúng là di sản… đã có cổng thống kê thay thế | V10956 CANCELLED CP-X.1/2.2/2.3/4.0/R4 | Session start hiện 0 checkpoint quá hạn | YES_CANCELLED | File roadmap vẫn STATUS:ACTIVE vì còn CP phụ chưa đóng hết | — |
| T28 | ⚪ | Thay API key toàn bộ | Kế hoạch thay API key — sau rảnh xử lý | Owner hoãn nguyên văn trong transcript | Không đào trong arc 01–02/08 (đúng lệnh hoãn) | DEFERRED_BY_OWNER | Chờ owner mở lại | LX |
| T29 | ✅ | Sáp nhập tỉnh 1/7 — lịch đài | Sau 1/7 đài có sổ 2 lần/tuần? Hệ ghi đúng không? | FU-V10810-STATION-IDENTITY · V10810 | Lịch KHÔNG đổi; sửa 6 dòng mã tắt + backfill MRE | YES_FIXED | Không | — |
| T30 | 🟡 | QD-018 ba bước sau 08/08 | Tắt optimizer → đo 105 luật → gỡ ép list; làm tuần tự | QD-018 · FU-233/234/235 | V10967 khóa thứ tự B1→B2→B3 | YES_PLAN_LOCKED | Chưa tới cửa sổ thực thi | 22/08 → 05/09 → 19/09 |

Chi tiết máy đọc: `evidence/bang_doi_chieu.json` · `evidence/bang_doi_chieu.md`.

### 3.2 Mục 🔴 (anh cần nghe)

- **T18 · Bundle thiếu model MT13/MB14 (02/08)** — Thiếu đào model-level + thiếu mã FU riêng; dễ lặp thiếu phiếu im lặng (ghi nhận: V10969 REPORT+evidence; nhắc FU-184/189 — CHƯA có FU riêng root-cause; đào: PARTIAL — biết MT=13 MB=14 MN=15; CHƯA liệt kê model nào timeout/empty)
- **T26 · FU-184/189 xác minh 02/08** — Hạn hôm nay — thiếu bước đóng có bằng chứng; liên quan T18 (ghi nhận: FU-184 KS0802-2 · FU-189 KS0802-1 WAIT_LIVE hạn 02/08; đào: V10969 có bundle counts; CHƯA đóng FU bằng checklist xác minh đầy đủ)

### 3.3 Top 🟡 chờ 08/08 (hoặc sát hạn)

- **T03 · Freeze đường ra số tới 08/08** — hạn 08/08 · QD-014 · OD-20260801-D · FU-215 DB0808
- **T04 · MT mất tín hiệu / lợi thế tắt tháng 6** — hạn 08/08 · FU-210 DO0808-1 · FU-212 TDLX-212
- **T05 · RF shadow đơn (sau freeze)** — hạn 08/08 · QD-015 · FU-216 XH0808-1
- **T06 · RULES-FIRST herding / ép chọn từ list** — hạn 08/08 → 22/08 (FU-222) · QD-016 · FU-231 · FU-222 · V10959
- **T07 · Prompt A/B cùng model** — hạn 08/08 · QD-017 · FU-226 HT0808-2 · FU-223
- **T12 · Deploy giờ cấm / chạm T-chốt** — hạn 08/08 / 15/08 · FU-207 DP0808 · FU-237 DP0815 · V10940 · V10968
- **T19 · LSTM live lệch suy luận** — hạn 08/08 · FU-217 SC0808-1 · V10957

Sát hạn gần: **FU-225 UI0803** (03/08), **FU-185 DD0803** (03/08), **FU-184/189** (02/08 — đang 🔴 vì chưa đóng).

## 4. Hướng xử lý và vì sao chọn

Chỉ **đối chiếu + ghi nhận gap**, không sửa runtime (QD-014). Phương án loại: tự đóng FU-184/189 hoặc đào model_count trong phiên này — đúng việc nhưng vượt phạm vi “không sửa production / báo cáo đối chiếu”; để FU-242 theo dõi gap đỏ. Không đường mật: hệ **chưa** “hết chặt”.

## 5. Đã làm gì

| File / nơi | Thay đổi |
|---|---|
| `Lottery_AI_Notion_Reports/V10973_.../` | REPORT + CONTEXT + evidence |
| `CHANGELOG.md` / `CURRENT_TRUTH_SSOT.md` / `FOLLOW_UP_TRACKER.md` | Prepend V10973 + FU-242 |
| Production / VPS | **Không đụng** |
| Commit public | `ccecf1b` (và commit evidence sau) |
| Commit riêng | `76968ae` |
| Notion | **Không ghi** |

Backup runtime: không áp dụng. Deploy: không.

## 6. Cổng kiểm

| Mục | Kết quả |
|---|---|
| Session start | Đạt (0 CP quá hạn) |
| Decision ledger | Đạt (0 TRÔI) |
| Báo cáo đủ 9 phần | Đạt (file này) |
| Report gate V10973 | Chạy sau push |
| Hash 4 bảng | Không áp dụng (không deploy) |
| Notion write | Không gọi — đạt A55.1 |

## 7. Vướng vấp

| # | Vấp | Hậu quả nếu bỏ qua |
|---|---|---|
| 1 | V10969 thấy MT13/MB14 nhưng không mở FU root-cause | Thiếu phiếu lặp lại im lặng |
| 2 | FU-184/189 hạn 02/08 vẫn WAIT_LIVE | Briefing tưởng “ổn” trong khi xác minh chưa đóng |
| 3 | 82 FU treo (nhiều DEPLOYED_PENDING lịch sử) | Nhiễu kiểm soát; khó nhìn việc thật |
| 4 | PowerShell phá `python -c` nhiều `{ }` | Phải ghi script file (đã học) |

## 8. Gỡ về

Chỉ tài liệu/báo cáo: xóa thư mục public V10973; revert prepend CHANGELOG/SSOT/FU; không có rollback runtime. Mất ~2 phút.

## 9. Theo dõi tiếp

| Mã | Việc | Ngưỡng / hạn |
|---|---|---|
| **FU-242 · KS0805 · Gap bundle thiếu phiếu + đóng FU-184/189 · hạn 05/08** | Đào model nào thiếu ở MT/MB 02/08; đóng hoặc escalate FU-184/189 | Xong checklist model-level trước 05/08 |
| FU-215 / QD-014 | Giữ freeze | hết 08/08 |
| FU-216/226/231 + QD-015/016/017 | Shadow RF + A/B + bỏ ép list | từ 08/08 |
| FU-225 | Owner verify UI | 03/08 |
| FU-185 | Tinh gọn lane thêm | 03/08 |
