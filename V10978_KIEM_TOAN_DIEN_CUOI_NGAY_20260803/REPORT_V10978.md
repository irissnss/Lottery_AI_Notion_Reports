# V10978 — Kiểm toàn diện cuối ngày 03/08/2026

> Owner hỏi lúc **19:03 ngày 03/08/2026 (giờ VN)**. Phiên **đọc thuần**: 0 file runtime bị sửa,
> 0 deploy, 0 restart. `QD-014` (đóng băng đường ra số tới hết 08/08) **không bị đụng**.
>
> Sự cố *"MB /nghiệm-thu hôm nay không output"* đang được xử ở phiên **V10977** — báo cáo này
> **không đào chồng**, chỉ ghi nhận và trỏ tham chiếu.

---

## 1. Tóm tắt một đoạn

Đo toàn hệ lúc 19:08–19:15 ngày 03/08. **Chỗ nguy hiểm nhất thì vẫn nắm chắc:** 4/4 cổng tự
kiểm thoát 0 thật, 20 quyết định owner khớp 63/63 mệnh đề máy kiểm, bộ tự kiểm nhất quán
**16/16** bốn ngày liên tiếp, chuỗi output 30 ngày **90/90 ô có bundle — 0 thiếu, 0 trễ hạn, 0
rỗng**, và **không một đồng tiền thật nào đang mở** (111/111 dòng `money_board_log` đều cờ
shadow, `stake = 0`, từ 28/06 tới nay). Cổng lợi thế đo tươi: **6/6 ô ĐÓNG**, không miền nào
chạm ngưỡng QD-013. **Nhưng tầng canh gác thì đang tuột:** hook đầu phiên **không kích hoạt
phiên thứ 3 liên tiếp**; `edge_gate_daily` chỉ ghi **1 lượt duy nhất** (01/08) vì **không cron
nào gọi**; ba bảng P&L **chết 75 ngày**; `system_alerts` **chết 84 ngày** và **0 lần** được
nhắc trong tracker lẫn SSOT; **4 bảng chưa bao giờ có dòng nào**; biên giờ chốt MT còn **11
phút**, MB còn **14 phút** — sát nhất trong 30 ngày. **Kết luận: hệ chưa mất kiểm soát ở tiền
và đường ra số, nhưng nhiều chốt kiểm chỉ còn được giữ bằng việc agent nhớ chạy tay, không
phải bằng máy.**

---

## 2. Owner yêu cầu gì (nguyên văn)

> *"Kiểm tra toàn diện tất cả các vấn đề của dự án anh tới thời điểm hiện tại dùm anh. ... Riết
> em mất kiểm soát dần thì phải"*

Ý chính đọc được: owner **mất niềm tin**, muốn biết hệ có còn được kiểm soát chặt không hay
đang tuột dần — và muốn trả lời **bằng số**, không đường mật, không biện hộ.

---

## 3. Đào bới / phát hiện

### 3.1 Bốn cổng tự kiểm — mã thoát THẬT

V10976 (sáng cùng ngày) vừa sửa 5 lỗi "xanh giả" trong chính các cổng này, nên mã thoát bây giờ
mới có ý nghĩa. Chạy lại đủ bốn:

| lệnh | exit | kết quả |
|---|---|---|
| `_v10920_session_start.py` | **0** | 0 checkpoint quá hạn · 0 roadmap cần archive · 79 mục treo (0 quá hạn) · 20 quyết định · 6 mặt quy tắc khớp |
| `_v10920_decision_ledger.py` | **0** | 20 quyết định · **63/63 mệnh đề khớp** · 1 mục "không kiểm máy" (OD-20260801-C, có nêu lý do) · **0 TRÔI** |
| `_v10921_report_gate.py` | **0** | 8/8 phiên gần nhất đủ 9 phần **và đã push** · 0 commit chờ push |
| `_v10925_rule_sync_check.py --check` | **0** | 6 mặt quy tắc đồng bộ · `AGENTS.md` khớp bản sinh · **4/4 `.mdc` đều `alwaysApply=true`** · 0 file quy tắc chết |

**Không cổng nào trượt.** Đây là điểm sáng thật, đo được bằng máy.

### 3.2 Sức khoẻ hệ thống (VPS 14.225.224.89)

| mục | số đo 03/08 19:10 |
|---|---|
| `systemctl is-active lottery` | `active` |
| MainPID | **645169** — **không đổi** so với sáng nay |
| `NRestarts` | **0** |
| Lên từ | Sun 2026-08-02 18:13:33 +07 (≈ 25 giờ) |
| `/api/health` | **200**, `version V20.3.36`, timezone `Asia/Ho_Chi_Minh (UTC+7)` |
| Đĩa `/` | 27G / 39G = **69%** (còn 13G) |
| DB | **650.698.752 B** (≈ 620 MB) |
| Đồng hồ | DB localtime `19:10:29` = shell VN `19:10:29`, UTC `12:10:29` → lệch đúng 7 tiếng, **không sai giờ** |

**Bốn bảng khoá:** `predictions` 11.632 · `final_bundles` 471 · `lottery_results` 15.207 ·
`model_daily_eval` 11.415. SHA256 từng bảng lưu trong `evidence/vps_audit_raw.json`.

**Bộ tự kiểm nhất quán:** lượt 03/08 = **16/16 OK**. Lịch sử đủ 4 lượt kể từ khi dựng:
03/08 · 02/08 · 01/08 · 31/07 — **tất cả 16/16**.

**Journal hôm nay:** 341 dòng · **0 Traceback** · 14 dòng ERROR/WARNING · `429` ×1 · `503` ×1 ·
`timeout` 0 · `RateLimit` 0. Toàn bộ 14 dòng là `SCRAPE_FAIL` MN trong khoảng 16:30–16:36 —
sau đó lấy được (kết quả MN có 3 dòng, ghi cuối 16:39:41). MB cũng `SCRAPE_FAIL` lúc 18:30:00
rồi lấy được lúc 18:31:02. **Không có lỗi tồn đọng.**

### 3.3 Chuỗi output 30 ngày — phần owner sợ nhất

Đo trên `final_bundles`, cửa sổ **05/07 → 03/08** (30 ngày lịch liên tục, không đứt ngày nào),
90 ô = 30 ngày × 3 miền. Hạn: MN 15:45 · MT 16:58 · MB 17:58 (giờ VN, `created_at` của
`final_bundles` khai `stored_tz = VN` trong `tz_registry` → đọc thẳng, không cộng bù).

| phép đo | kết quả |
|---|---|
| Tổng ô (ngày × miền) | **90** |
| **THIẾU output hoàn toàn** | **0** |
| **Chốt SAU hạn** | **0** |
| **display/bạch-thủ + lô rỗng** | **0** |
| **Thiếu phiếu (`model_count` < 15)** | **57** |

**Không có lỗ hổng lịch sử nào bị giấu.** 90/90 ô đều có bundle, đều chốt trước hạn, đều có số.
Đây là câu trả lời thẳng cho lo lắng lớn nhất của owner.

**Nhưng 57/90 ô (63%) chốt với ít hơn 15 phiếu.** Bóc ra:

- **MT ở `model_count = 13` đúng 30/30 ngày** (riêng 25/07 xuống 11).
- **MB dưới 15 ở 26/30 ngày** (12–14); chỉ 14–18/07 đủ 15.
- **MN đủ 15 ở 28/30 ngày** (28/07 = 14, 01/08 = 13).
- Phân bố: `15`→33 ô · `14`→19 · `13`→34 · `12`→3 · `11`→1.

**Đây không phải lỗi mới và có lý do có tên.** V10974 đã ghi: MT thiếu `meta-learning` (cổng
`bt_gate`) + `gemini-2.5-pro` (`MT_top13_V10752`); MB thiếu `random-forest` (`bt_gate`). Tức là
**cổng lọc chủ ý**, không phải model chết — `predictions` hôm nay vẫn đủ **27 model mỗi miền**.

**Điều chưa ai thấy:** ngưỡng do chính `FU-243` viết ra là *"≥3 ngày/tuần incomplete cùng
pattern → escalate"*. Với MT ở 13/15 **suốt 30/30 ngày**, ngưỡng đó bị vượt **mọi tuần trong
một tháng** mà không ai escalate — vì phép canh chỉ nhìn **một ngày một lần**, chưa lần nào
nhìn rộng ra tháng. Ngoài ra `/api/health` vẫn khai `expected_output_model_count: 15` trong khi
thực trạng ổn định của MT là **13** — con số công bố không khớp con số thật.

### 3.4 Biên giờ chốt đang co lại (phát hiện mới)

Tuy 0/90 ô trễ hạn, **khoảng đệm trước hạn đang mỏng đi đều**:

| miền | đầu tháng 7 (điển hình) | 01/08 | 02/08 | **03/08** |
|---|---|---|---|---|
| MT (hạn 16:58) | 16:38–16:43 → dư **15–20 phút** | 16:46 (dư 12) | 16:41 (dư 17) | **16:47 → dư 11 phút** |
| MB (hạn 17:58) | 17:33–17:36 → dư **22–25 phút** | 17:39 (dư 19) | 17:37 (dư 21) | **17:44 → dư 14 phút** |

Cả hai đều là **mức sát hạn nhất trong 30 ngày**. MN không có vấn đề (chốt 04:17–05:20, dư hơn
10 tiếng). `FU-207` có ghi rủi ro **deploy** chạm đầu ra, nhưng **không cổng máy nào canh chính
cái biên này co lại** → mở `FU-256`.

### 3.5 Cổng lợi thế và tiền

Gọi thẳng `_v10945_edge_gate.tinh()` (**chỉ tính, không ghi bảng**), 3 miền × 2 cửa sổ.
Ngưỡng owner QD-013: hơn đánh bừa **≥ 3pp** VÀ **z ≥ 2**.

| cửa sổ | MN | MT | MB |
|---|---|---|---|
| **30 ngày** | −1,00pp · z −0,27 · **ĐÓNG** | −4,78pp · z −1,12 · **ĐÓNG** | −0,87pp · z −0,11 · **ĐÓNG** |
| **90 ngày** | −0,37pp · z −0,17 · **ĐÓNG** | −2,94pp · z −1,18 · **ĐÓNG** | −7,22pp · z −1,62 · **ĐÓNG** |

**6/6 ô ĐÓNG.** Không miền nào phân biệt được với đánh bừa; cả sáu đều **âm**. Hoà vốn cần
18,37% (MN/MT) và 27,55% (MB) — hệ đạt 15,31% · 11,84% · 22,58% ở cửa sổ 30 ngày.

**Tiền thật: khoá 100%.** Toàn bộ **111/111** dòng `money_board_log` từ 28/06 đến 03/08 đều mang
`diagnostic_only=1, shadow_only=1, output_eligible=0, owner_approved=0` và `stake = 0.0` —
**không có ngoại lệ nào trong toàn bộ lịch sử bảng**. QD-013 giữ nguyên hiệu lực.

**P&L 30 ngày (mô phỏng):** nếu đánh bạch thủ 1 số mỗi ngày mỗi đài theo giá owner chốt 26/07
(MN/MT 18k/đài · MB 27k/đài · trúng thu 98k):

| miền | ngày | lượt đài | trúng | tỷ lệ | vốn | thu | **lãi/lỗ** |
|---|---|---|---|---|---|---|---|
| MN | 31 | 98 | 15 | 15,31% | 1.764.000đ | 1.470.000đ | **−294.000đ** |
| MT | 31 | 76 | 9 | 11,84% | 1.368.000đ | 882.000đ | **−486.000đ** |
| MB | 31 | 31 | 7 | 22,58% | 837.000đ | 686.000đ | **−151.000đ** |
| **Tổng** | | **205** | **31** | | **3.969.000đ** | **3.038.000đ** | **−931.000đ (−23,5%)** |

Con số này **xác nhận quyết định dừng tiền của owner là đúng** — và cho thấy thiệt hại đã tránh được.

### 3.6 Bảng đo đã chết — phần "chỉ có trên giấy"

Soát cả **241 bảng** trong DB, **102 bảng có cột `date`**, đối chiếu ngày ghi cuối với hôm nay:

| bảng | ghi cuối | đứng | có cron? | có trong tracker/SSOT? |
|---|---|---|---|---|
| `pnl_daily_summary` / `_bets` / `_settlements` | 2026-05-20 | **75 ngày** | **0** | rải rác, **không mục riêng** |
| `system_alerts` (9 dòng) | 2026-05-11 | **84 ngày** | **0** | **0 lần trong cả hai** |
| `cohere_rerank_log` / `cohere_effectiveness_daily` | 2026-07-09 | **25 ngày** | 0 | có nhắc Cohere |
| `model_latency_cost_audit_daily` | 2026-05-06 | **89 ngày** | 0 | có nhắc |
| `signal_governance_ledger` (10.317 dòng) | 2026-05-22 | **73 ngày** | 0 | — |
| `v10809_shadow_ab_daily` | 2026-07-22 | **12 ngày** | 0 | có nhắc |
| `edge_gate_daily` | 2026-08-01 | **2 ngày**, 1 lượt ghi duy nhất | **0** | FU-244 |
| `sync_parity_audit_daily` | **chưa bao giờ** | — | 0 | có nhắc |
| `data_preservation_manifest_daily` | **chưa bao giờ** | — | 0 | có nhắc |
| `bundle_replay_compare_daily` | **chưa bao giờ** | — | 0 | có nhắc |
| `v10883_connector_apply_log` | **chưa bao giờ** | — | 0 | có nhắc |

Ba bảng `*_daily` đầu trong nhóm "chưa bao giờ" được **khai trong `database.py` nhưng không
module nào ghi**. `v10883_connector_apply_log` **có** writer (`_v10883_official_connector.py`)
nhưng writer chưa bao giờ chạy.

**P&L đã chuyển nhà mà không ai retire bảng cũ:** cron duy nhất có chữ `pnl` là
`30 22 * * * _v10730_pnl_forward_track.py`, và nó ghi bảng **khác** —
`pnl_forward_track_shadow` (còn sống, ghi cuối 02/08). Ba bảng `pnl_daily_*` bị bỏ lại nguyên
trạng, ai mở thẳng sẽ đọc số của tháng 5.

**Cohere:** `/api/health` vẫn khai `active_rerank_measurement_model_count: 1` với chú thích
*"plus 1 shadow rerank measurement component (Cohere)"*, trong khi hai bảng log của nó đứng
25 ngày.

**Điểm sáng ngược lại:** `crontab -l` có **76 dòng đang bật**, và **không dòng nào trỏ tới file
không tồn tại**. 44/61 file log được ghi trong 2 ngày qua.

### 3.7 Hook đầu phiên vẫn im — ngưỡng FU-245 đã chạm

`FU-245` (hạn 04/08) viết: *"đầu phiên 04/08 nếu dấu thời gian trong file vẫn không phải ngày
hôm đó → coi như hook hỏng thật."*

**Bằng chứng lúc 19:03 hôm nay:** `docs/_BRIEFING_DAU_PHIEN.txt` mang dấu
`# Sinh tự động lúc 2026-08-03 09:00:00` — của lần **chạy tay** phiên sáng, không phải của phiên
này. Nội dung còn ghi `FU-185 … hạn 03/08` đứng đầu, trong khi bộ kiểm chạy tươi lúc 19:08 cho
`FU-250` đứng đầu và 79 mục. **Hook không kích hoạt phiên thứ 3 liên tiếp** (02/08 · 03/08 sáng
· 03/08 tối). Bản chụp giữ ở `evidence/evidence_briefing_stale_1903.txt`.

**Đã loại trừ được lỗi phía repo:**

- Script hook **không hỏng**: `"" | python .cursor/hooks/session_start_briefing.py` → in `{}`,
  exit **0**, chạy hết **0,49 giây**.
- `.cursor/hooks.json` khai đúng: `sessionStart` → `python .cursor/hooks/session_start_briefing.py`,
  timeout 100.
- `git diff .cursor/hooks.json` chỉ khác **đầu dòng LF/CRLF**, không đổi nội dung.

→ lỗi nằm ở phía **Cursor không gọi hook**, không phải ở repo. Nghi vấn còn lại chưa chứng minh
được: `main()` gọi `sys.stdin.read()`; nếu Cursor mở stdin mà không đóng thì lời gọi chờ tới hết
timeout 100s rồi bị giết, file không bao giờ được ghi.

**Đây là phát hiện nặng nhất của phiên:** lưới an toàn dựng ra để chặn đúng lỗi "mất kiểm soát"
đang im lặng; chỗ này hiện **chỉ còn kỷ luật agent chạy tay** giữ.

### 3.8 Đối chiếu việc treo

| phép đếm | số |
|---|---|
| FU khác nhau có trong tracker | **240** |
| Mục **còn treo** | **111** |
| **Quá hạn** | **1** — `FU-236`, hạn 02/08 |
| Đến hạn trong 5 ngày | **13** (FU-185 hạn hôm nay · FU-250 06/08 · 10 mục hạn 08/08) |
| **Thiếu mã đọc §58** | **54 / 111** |

Bộ `_v10920_session_start.py` đếm **79** mục treo (nó chỉ tính mục có khối `###` chuẩn); phép
đếm rộng hơn của phiên này ra **111**. Chênh lệch là các mục cũ ghi không đúng khuôn — chính là
phần lớn trong 54 mục thiếu mã đọc.

**Roadmap còn ACTIVE:** 4 file. `ACTIVE_ROADMAP_CROSS_REGION_LEAKAGE.md` **không có dòng
`STATUS:`** (nên bộ kiểm không phân loại được). `ACTIVE_ROADMAP_OUTPUT_TOTAL_ADVANCED.md` có
**CP-OT3 mốc 2026-06-21 chưa đánh dấu xong** (đã đo âm, ghi rõ "KHÔNG đụng official") — không
phải việc bỏ quên, nhưng dòng checkpoint chưa được đóng.

**Sổ quyết định:** 20 quyết định hiệu lực · **0 mục TRÔI** · **0 mục tới hạn rà soát**.

### 3.9 Trạng thái từng FU owner hỏi đích danh

| FU | mã đọc · hạn | trạng thái | đứng ở đâu hôm nay |
|---|---|---|---|
| FU-208 | (thiếu mã đọc) | liên quan FU-215/225/QD-014 | không có khối `###` riêng — chỉ xuất hiện dạng tham chiếu |
| FU-209 | (thiếu mã đọc) | MEASURED_BUT_NOT_FIXED / OWNER_LOCK | bằng chứng duy nhất từng có lợi thế thật; chưa có hạn |
| FU-210 | DO0808-1 · 08/08 | MEASURED_BUT_NOT_FIXED | tháng 6 mất lợi thế MT — còn đúng hạn |
| FU-213 | (thiếu mã đọc) · 08/08 | DEPLOYED_PENDING_LIVE_VERIFY / OWNER_LOCK | còn đúng hạn |
| FU-215 | DB0808 · 08/08 | OWNER_LOCK | đóng băng đường ra số (QD-014) — **còn hiệu lực, đã xác nhận** |
| FU-216 | XH0808-1 · 08/08 | OWNER_LOCK | shadow MT RF đơn (QD-015), chờ hết freeze |
| FU-217 | SC0808-1 · 08/08 | MEASURED_BUT_NOT_FIXED | LSTM live lệch suy luận — còn đúng hạn |
| **FU-225** | UI0803 · **hạn hôm nay** | **CLOSED** | xác minh UI du-doan-test + filter — **đã đóng ở V10975**, không còn treo |
| FU-232 | SC0815-3 · 15/08 | MEASURED_BUT_NOT_FIXED / OWNER_LOCK | còn xa hạn |
| FU-233 | HT0822-1 · 22/08 | OWNER_LOCK | chờ sau 08/08 |
| FU-243 | SC0805 · 05/08 | MEASURED_ROOT_CAUSE | **bổ sung đo 30 ngày trong phiên này** (mục 3.3) |
| FU-244 | KS0810 · 10/08 | MEASURED_ROOT_CAUSE | **xác nhận vẫn nguyên trạng** (mục 3.5) |
| FU-245 | SC0804 · 04/08 | MEASURED_ROOT_CAUSE | **ngưỡng ĐÃ CHẠM** (mục 3.7) |
| FU-250 | KS0806 · 06/08 | MEASURED_BUT_NOT_FIXED | **có bằng chứng quyết** (mục 4.3) |

---

## 4. Hướng xử lý và vì sao chọn

### 4.1 Vì sao KHÔNG sửa gì trong phiên này

Ba lý do, theo đúng thứ tự ưu tiên của luật:

1. **QD-014 đóng băng đường ra số tới hết 08/08.** Mọi thứ chạm `model_count`, cổng lọc
   `bt_gate` / `MT_top13_V10752`, hay giờ chốt bundle đều nằm trong vùng cấm.
2. **Có agent khác (V10977) đang sửa trên cùng VPS.** Đụng crontab hay file chung lúc này là
   rủi ro giẫm chân, mất khả năng quy kết khi có sự cố.
3. **Playbook-first:** bằng chứng rõ thì sửa ngay, bằng chứng mơ hồ thì dựng đo có ngưỡng số.
   Toàn bộ phát hiện của phiên này thuộc nhóm **"đã đo rõ nhưng cách xử phải chờ hết freeze"**
   → đúng bài là ghi mục theo dõi kèm ngưỡng hành động bằng số, không phải sửa vội.

### 4.2 Vì sao KHÔNG tự thêm cron cho cổng lợi thế (FU-244)

Đây là cám dỗ lớn nhất của phiên: `edge_gate_daily` chỉ có 1 lượt ghi, docstring của module tự
nhận *"tự chấm mỗi ngày… không phụ thuộc trí nhớ ai"* — nghe rất đáng sửa ngay.

**Không sửa, vì phiên V10975 đã cân nhắc đúng việc này và ký lý do:** *"thêm cron là đụng
crontab production, mà QD-014 đang đóng băng tới 08/08. Bảng này là bảng chẩn đoán
(`diagnostic_only=1`, `shadow_only=1`, `output_eligible=0`) nên không có rủi ro số ra ngoài —
hoãn được."* Hạn đã đặt là **10/08**, chưa tới. Tự ý làm lại là **re-litigate một quyết định đã
ký** — đúng thứ §56 cấm.

Việc phiên này làm thay thế: **đo tươi để chứng minh khoảng trống đó chưa gây hại** — 6/6 ô vẫn
ĐÓNG, rủi ro tiền = 0.

### 4.3 Vì sao FU-250 nên đi nhánh "ghi docstring rồi đóng"

`FU-250` tự viết ngưỡng: *"nếu có hook/cron/script khác gọi nó và đọc mã thoát thì sửa ngay;
nếu không ai đọc mã thoát thì chỉ ghi rõ trong docstring và đóng mục."*

Đã soát `_v10861_runtime_contract_audit` · `_v10921_rule_a55` · `_v10958_fu_reader` trong
`.cursor/hooks.json`, `.cursor/hooks/*.py`, `web/backend/*.py` và `crontab -l` → **0 nơi gọi cả
ba**. Vậy điều kiện đã rõ: đi nhánh thứ hai. Để lại cho phiên 06/08 thực hiện, không làm chồng
trong phiên kiểm.

### 4.4 Phương án đã loại

| phương án | vì sao loại |
|---|---|
| Sửa `expected_output_model_count` trong `/api/health` cho khớp thực tế MT=13 | Chạm bề mặt công bố của đường ra số → QD-014 cấm tới 08/08 |
| Bật lại cron ghi `pnl_daily_*` | Chưa biết bảng nào mới là nguồn P&L chính thức; nối bừa sẽ tạo hai nguồn sự thật. Phải chốt trước (FU-254) |
| Xoá luôn 4 bảng rỗng | Xoá schema là thao tác một chiều; phải xác nhận không module nào định dùng lại (FU-255) |
| Sửa `.cursor/hooks.json` để chữa hook im | Chưa chứng minh được nguyên nhân; sửa mò dễ che mất triệu chứng thật |

---

## 5. Đã làm gì

### 5.1 Bảng file × thay đổi

| file | loại | thay đổi |
|---|---|---|
| `web/backend/_v10978_audit_probe.py` | **mới** | Probe VPS đọc thuần: dịch vụ, đĩa, 4 bảng khoá + sha256, `tz_registry`, consistency guard, chuỗi output 30 ngày, cổng lợi thế, journal, crontab |
| `web/backend/_v10978_probe2.py` | **mới** | Probe 2: cron cổng lợi thế, phủ model 30 ngày, biên giờ chốt, scheduler_logs, 102 bảng có cột `date` |
| `web/backend/_v10978_probe3.py` | **mới** | Probe 3: cờ tiền thật, P&L 30 ngày tự tính, bảng rỗng ai ghi, cron trỏ file không tồn tại |
| `web/backend/_v10978_analyze.py` / `_analyze2.py` / `_analyze3.py` | **mới** | Ba bộ tóm tắt ra bản đọc được |
| `web/backend/_v10978_fu_check.py` / `_fu_read.py` | **mới** | Soi trạng thái FU + đếm treo/quá hạn/thiếu mã đọc |
| `web/backend/_v10978_governance.py` | **mới** | Ghi 3 tài liệu quản trị bằng `_doc_prepend.prepend()` |
| `web/backend/_v10978_evidence.py` | **mới** | Dựng bộ bằng chứng công khai + che khoá API |
| `CHANGELOG.md` | prepend | +1.726 ký tự |
| `docs/CURRENT_TRUTH_SSOT.md` | prepend | +3.117 ký tự |
| `docs/FOLLOW_UP_TRACKER.md` | prepend | +9.818 ký tự (4 mục mới + 4 mục cập nhật) |

**KHÔNG file runtime nào bị sửa.** Mọi script mới đều mở DB ở chế độ `file:…?mode=ro`.

### 5.2 Backup

Không cần backup file nào vì **không sửa file có sẵn** — chỉ thêm file mới và **prepend** (chỉ
nối thêm, không ghi đè) vào 3 tài liệu. `_doc_prepend.prepend()` từ chối ghi nếu kết quả ngắn
hơn bản cũ; cả 3 lần đều dài ra đúng như bảng trên.

### 5.3 Deploy

**Không deploy.** Không restart. PID 645169 giữ nguyên từ đầu tới cuối phiên.

### 5.4 Hash 4 bảng khoá

Đo **một lần** (phiên đọc thuần, không có thao tác ghi nào giữa chừng nên không có cặp
trước/sau): `predictions` 11.632 · `final_bundles` 471 · `lottery_results` 15.207 ·
`model_daily_eval` 11.415, kèm SHA256 đầy đủ trong `evidence/vps_audit_raw.json`. Số dòng khớp
đúng nhịp tăng tự nhiên trong ngày.

---

## 6. Cổng kiểm

| cổng | kết quả | đạt? |
|---|---|---|
| `_v10920_session_start.py` | exit **0** · 0 quá hạn | ✅ |
| `_v10920_decision_ledger.py` | exit **0** · 63/63 mệnh đề · 0 TRÔI | ✅ |
| `_v10921_report_gate.py` (toàn bộ) | exit **0** · 8/8 phiên đủ 9 phần và đã push | ✅ |
| `_v10925_rule_sync_check.py --check` | exit **0** · 6 mặt đồng bộ · 4/4 `.mdc` tự nạp | ✅ |
| `/api/health` | **200** | ✅ |
| `v10900_consistency_guard` 03/08 | **16/16 OK** | ✅ |
| Chuỗi output 30 ngày | 0 thiếu · 0 trễ · 0 rỗng | ✅ |
| Tiền thật đang mở | **0 đồng** · 111/111 dòng shadow | ✅ |
| Cổng lợi thế | 6/6 **ĐÓNG** | ✅ (đúng ý QD-013) |
| Ba tài liệu quản trị dài ra, không mất lịch sử | +1.726 / +3.117 / +9.818 ký tự | ✅ |
| Che khoá API trong `evidence/` | quét 5 mẫu khoá trên 10 tệp → **SẠCH**, 0 lượt phải che | ✅ |
| `_v10921_report_gate.py V10978` | (chạy sau khi push — xem mục 9) | — |

---

## 7. Vướng vấp

**Vấp do chính agent gây ra trong phiên:**

1. **Dùng cú pháp `cmd` trong PowerShell** — lệnh đầu tiên `cd /d … && …` hỏng ngay. Hậu quả
   nếu bỏ qua: mất thời gian, và nguy hiểm hơn là dễ tưởng cổng "chạy rồi" trong khi nó chưa
   chạy. Đã chuyển sang cú pháp PowerShell và **in `$LASTEXITCODE` sau mỗi cổng** để không bao
   giờ đoán mã thoát.
2. **Đoán sai tên cột 2 lần** — `predictions.region` (thật là `target_region`),
   `lottery_results.prizes` (thật là `prizes_json`), `scheduler_logs.status` (thật là
   `log_level`). Probe chết giữa chừng. Hậu quả nếu bỏ qua: mục "scheduler_logs" trong bản
   tóm tắt đầu tiên hiện `ERR no such column` mà vẫn in ra như một kết quả — đúng loại "xanh
   giả" ở quy mô nhỏ. Đã đọc `PRAGMA table_info` trước rồi mới viết lại truy vấn.
3. **`python -c` in tiếng Việt hỏng mã hoá**, và **PowerShell nuốt f-string nhiều dấu ngoặc** —
   đúng hai bẫy đã ghi trong `CLAUDE.md`. Đã chuyển hẳn sang viết script ra file có
   `sys.stdout.reconfigure(encoding="utf-8")`.
4. **Suýt tự ý thêm cron cho `_v10945_edge_gate.py`.** Đã dừng lại khi đọc kỹ FU-244 và thấy
   phiên V10975 **đã cân nhắc và ký lý do hoãn tới sau 08/08**. Hậu quả nếu bỏ qua: vi phạm
   §56 (làm lại việc đã quyết), đụng crontab production trong lúc QD-014 đóng băng, và giẫm
   chân agent V10977 đang thao tác trên cùng máy.

**Vấp của hệ thống, không phải của phiên:**

5. `Read` tool không đọc được file trong `artifacts/` (permission denied) — phải in qua Python.
   Không ảnh hưởng kết quả.
6. `_v10920_session_start.py` đếm **79** mục treo còn phép đếm rộng ra **111**. Hai con số đều
   đúng theo định nghĩa riêng, nhưng **chênh 32 mục** là dấu hiệu tracker có nhiều mục cũ ghi
   sai khuôn. Ghi lại trong SSOT để không ai hoảng khi thấy hai số khác nhau.

---

## 8. Gỡ về

Phiên **không sửa code chạy, không deploy**, nên không có gì phải gỡ ở phía runtime.

Nếu cần bỏ phần tài liệu đã ghi:

```bash
cd E:\Lottery_AI_Test
git log --oneline -3                       # tìm commit V10978
git revert <commit_V10978>                 # bỏ 3 tài liệu + 9 script mới
```

Ba tài liệu chỉ bị **prepend** (nối lên đầu), nội dung cũ nguyên vẹn — có thể xoá tay khối
`## V10978 …` ở đầu mỗi file thay vì revert. Mất khoảng **2 phút**.

Chín script `_v10978_*.py` đều là công cụ đọc thuần, xoá đi không ảnh hưởng gì:

```bash
del web\backend\_v10978_*.py
```

Bộ bằng chứng thô giữ ở `artifacts/v10978/` (không vào Git) và bản đã che khoá ở
`Lottery_AI_Notion_Reports/V10978_.../evidence/`.

---

## 9. Theo dõi tiếp

**Bốn mục mới mở trong phiên này:**

| mã máy | mã đọc | nhãn | hạn | ngưỡng hành động bằng số |
|---|---|---|---|---|
| **FU-254** | KS0810-2 | Ba bảng P&L chết 75 ngày | **10/08** | Tới 10/08: hoặc nối cron ghi lại, hoặc đánh dấu RETIRED trong SSOT và ghi rõ nguồn P&L chính thức là `money_board_log`. Không để mập mờ |
| **FU-255** | KS0810-3 | `system_alerts` + 4 bảng rỗng không ai canh | **10/08** | Tới 10/08: mỗi bảng chọn một — nối writer + cron thật, hoặc xoá khỏi `database.py` và ghi RETIRED |
| **FU-256** | DO0806 | Biên giờ chốt MT/MB co lại | **06/08** | Dựng phép đếm trong `_v10900_consistency_guard`: MT hoặc MB còn **< 8 phút** trước hạn, **hoặc 3 ngày liên tiếp < 12 phút** → báo đỏ. Chưa dựng được tới 06/08 → escalate OWNER_LOCK |
| **FU-257** | KS0810-4 | Cohere chết 25 ngày mà health khai đang chạy | **10/08** | Tới 10/08: bật lại ghi log, hoặc hạ `active_rerank_measurement_model_count` về 0 và ghi rõ trong SSOT |

**Bốn mục cập nhật bằng chứng mới:**

- **FU-245** (hạn **04/08 — ngày mai**): ngưỡng **đã chạm**, hook im phiên thứ 3. Đã loại trừ
  lỗi phía repo. Việc phải làm 04/08: chuyển sang gọi bộ kiểm thẳng trong quy trình và ghi
  `A54_VIOLATION` nếu bỏ sót.
- **FU-243** (hạn 05/08): bổ sung bức tranh 30 ngày — 57/90 ô thiếu phiếu, MT 13/15 suốt 30/30
  ngày. Ngưỡng bổ sung: **sau 08/08** sửa `expected_output_model_count` theo miền hoặc xem lại
  `bt_gate`/`MT_top13_V10752`. **Trước 08/08 không đụng.**
- **FU-244** (hạn 10/08): xác nhận nguyên trạng, 6/6 ô vẫn ĐÓNG nên rủi ro tiền = 0. Giữ nguyên
  quyết định hoãn của V10975.
- **FU-250** (hạn 06/08): đã có bằng chứng quyết — 0 nơi gọi 3 script → đi nhánh "ghi docstring
  rồi đóng mục".

**Mục cần chú ý ngay:**

- **FU-236** — mục treo **duy nhất đã quá hạn** (hạn 02/08).
- **13 mục đến hạn trong 5 ngày**, trong đó **10 mục dồn vào 08/08** — đúng ngày hết đóng băng
  QD-014. Ngày 08/08 sẽ rất nặng, nên chia bớt việc từ bây giờ.
- **54/111 mục treo thiếu mã đọc §58** — quy ước owner ký 02/08 mới chỉ áp cho mục mới.
- `ACTIVE_ROADMAP_CROSS_REGION_LEAKAGE.md` **thiếu dòng `STATUS:`** nên bộ kiểm không phân loại
  được; `CP-OT3` trong `ACTIVE_ROADMAP_OUTPUT_TOTAL_ADVANCED.md` có mốc 21/06 chưa đóng dòng.

**Việc của phiên khác:** sự cố *"MB /nghiệm-thu hôm nay không output"* → **V10977**.

---

## 10. Kết luận — hệ đang được kiểm soát tới mức nào

**Một câu:** hệ **chưa mất kiểm soát ở chỗ nguy hiểm nhất** — tiền và đường ra số vẫn nắm chắc,
có số chứng minh — **nhưng tầng canh gác thì đang tuột**: nhiều chốt kiểm giờ chỉ còn được giữ
bằng việc agent nhớ chạy tay, không phải bằng máy.

### Cái gì đã kiểm soát THẬT (có cổng máy kiểm được, có số, có ngưỡng)

| | bằng chứng |
|---|---|
| 4 cổng tự kiểm | exit **0** thật cả bốn (V10976 vừa sửa xanh giả sáng nay) |
| Quyết định owner không trôi | **63/63** mệnh đề máy kiểm khớp trên code thật · 0 TRÔI |
| Nhất quán hệ thống | **16/16 OK**, 4/4 ngày kể từ khi dựng |
| Chuỗi output | **90/90 ô** có bundle · **0 thiếu · 0 trễ hạn · 0 rỗng** trong 30 ngày |
| Tiền | **0 đồng** đang mở · **111/111** dòng shadow từ 28/06 · QD-013 giữ 100% |
| Cổng lợi thế | **6/6 ĐÓNG**, đo tươi hôm nay, cả 6 đều âm |
| Báo cáo công khai | **8/8** phiên gần nhất đủ 9 phần **và đã push** |
| Quy tắc | 6 mặt đồng bộ · **4/4 `.mdc` đều tự nạp** |
| Dịch vụ | health 200 · PID không đổi · **0 restart · 0 Traceback** hôm nay |

### Cái gì CHỈ CÓ TRÊN GIẤY (có FU hoặc có bảng, nhưng không máy nào canh)

| | tình trạng | có mục theo dõi chưa |
|---|---|---|
| **Hook đầu phiên** | im **3 phiên liên tiếp**; chỉ còn kỷ luật agent giữ | FU-245, hạn **04/08**, ngưỡng **đã chạm** |
| **`edge_gate_daily`** | 1 lượt ghi duy nhất, **0 cron** — cổng tiền của QD-013 không tự chấm ngày nào | FU-244, hạn 10/08, **có lý do hoãn đã ký** |
| **3 bảng P&L** | chết **75 ngày**, 0 cron, P&L đã chuyển nhà mà không ai retire bảng cũ | **chưa có — mở FU-254 hôm nay** |
| **`system_alerts`** | chết **84 ngày**, **0 lần** nhắc trong tracker lẫn SSOT | **chưa có — mở FU-255 hôm nay** |
| **4 bảng rỗng** | **chưa bao giờ có dòng nào**; 3 bảng không module nào ghi | **chưa có — mở FU-255 hôm nay** |
| **Cohere** | log chết **25 ngày** mà `/api/health` vẫn khai đang chạy | **chưa có — mở FU-257 hôm nay** |
| **3 script cổng** | vẫn thoát 0 khi trượt | FU-250, hạn 06/08, **đã có bằng chứng quyết** |
| **54/111 mục treo** | thiếu mã đọc §58 owner ký 02/08 | ghi nhận trong SSOT phiên này |

### Cái gì ĐANG TUỘT (có bằng chứng bằng số)

1. **Biên giờ chốt co lại.** MT còn **11 phút**, MB còn **14 phút** trước hạn — **sát nhất trong
   30 ngày**, trong khi đầu tháng 7 còn 15–25 phút. Chưa ô nào trễ, nhưng xu hướng rõ và
   **không cổng máy nào canh**.
2. **63% bundle chốt với ít hơn 15 phiếu.** MT ở 13/15 **cả 30/30 ngày**. Có lý do đã ghi, nhưng
   ngưỡng "≥3 ngày/tuần" của chính FU-243 bị vượt **mọi tuần suốt một tháng** mà không ai
   escalate — vì phép canh chỉ nhìn một ngày, chưa lần nào nhìn rộng ra tháng.
3. **`/api/health` khai `expected_output_model_count: 15`** trong khi thực trạng ổn định của MT
   là **13** — số công bố không khớp số thật.
4. **Hiệu quả tiền âm và ổn định:** P&L 30 ngày mô phỏng **−931.000đ / −23,5%**, không miền nào
   tới hoà vốn. (Đây là lý do quyết định dừng tiền của owner đang đúng, không phải lỗi vận hành.)
5. **Lưới an toàn tự động im lặng** (hook đầu phiên) — nghiêm trọng nhất, vì nó là thứ dựng ra
   để chặn đúng cái owner đang lo.

### Trả lời thẳng câu "riết em mất kiểm soát dần"

**Owner đúng một nửa, và đúng ở phần quan trọng.**

**Không đúng ở chỗ:** không có ngày nào mất output, không có ô nào chốt trễ, không đồng tiền
nào lọt ra, không quyết định nào bị trôi khỏi code, không lỗi runtime nào tồn đọng. Những con
số đó có thật và kiểm được bằng máy.

**Đúng ở chỗ:** số lượng thứ **được canh bằng máy** đang tụt lại so với số lượng thứ **được ghi
trên giấy**. Có ít nhất **11 bảng đo đã chết hoặc chưa bao giờ sống**, trong đó `system_alerts`
chết 84 ngày mà **không một dòng nào** trong tracker hay SSOT nhắc tới — tức là nó chết mà
không ai biết, và cũng không có cơ chế nào để biết. Cộng thêm hook đầu phiên im 3 phiên liên
tiếp, thì **cảm giác "tuột dần" của owner là có cơ sở vật chất**, không phải cảm tính.

Chỗ cần vá không phải đường ra số — chỗ đó đang tốt. Chỗ cần vá là **cơ chế phát hiện khi một
phép đo ngừng chạy**. Hiện tại không có cái đó, nên mỗi lần một bảng chết là phải đợi tới khi
có người ngồi soát tay như phiên này mới lộ ra.

---

## 11. Bổ sung sau khi push — sổ quyết định chuyển từ 0 TRÔI sang 1 TRÔI lúc 19:30

Chạy lại `_v10920_decision_ledger.py` **sau khi** đã push, để xác nhận phiên không làm hỏng gì.
Kết quả **khác lúc 19:08**:

| lúc | số quyết định | kết quả | exit |
|---|---|---|---|
| 19:08 (đầu phiên) | **20** | 0 TRÔI | **0** |
| 19:30 (cuối phiên) | **21** | **1 TRÔI** | **2** |

**Không phải do phiên này.** Mục mới là **`OD-20260803-B`**, nguyên văn owner ghi trong đó là:

> *"MB /nghiem-thu này không output là sao em? ly do gi sao ma tao lao the em? Riet em mat kiem
> soat dan thi phai"*

Đây là **việc của phiên V10977** đang chạy song song. Bằng chứng: `git status` cho
`docs/OWNER_DECISION_LEDGER.json` là **`M` (sửa, chưa commit)** — commit gần nhất chạm file này
vẫn là `cd95b8f` của V10976 lúc 09:18 sáng. Tức mục đó đang **dở dang trong phiên khác**, chưa
được commit.

**Phép bị trôi** là mệnh đề số 2 trong 5 mệnh đề của `OD-20260803-B`:

```
Lane khai lượt chạy CUỐI cho cả ba miền
LANE_SCHEDULE['MN']['last_run'] == '06:15' and LANE_SCHEDULE['MT']['last_run'] == '16:54'
  and LANE_SCHEDULE['MB']['last_run'] == '17:54'
→ LỖI: name 'all' is not defined
```

Mệnh đề **không chạy được** (môi trường `eval` của bộ kiểm không có sẵn hàm dựng sẵn `all`), và
bộ kiểm tính "chạy lỗi" = **TRÔI**. Bốn mệnh đề còn lại của mục đó khớp.

**V10978 cố ý KHÔNG sửa:** đây là file đang được phiên V10977 thao tác; sửa vào lúc này là giẫm
chân và làm mất khả năng quy kết. Ghi nhận lại đúng hiện trạng để phiên V10977 xử trong phiên
của họ.

**Điều đáng rút ra cho owner:** đây lại đúng một ca *"mệnh đề máy kiểm nhưng không chạy được"* —
họ hàng gần với loại "xanh giả" mà V10976 vừa dọn sáng nay. Nó **đã bị bắt đúng** (bộ kiểm báo
đỏ và thoát mã 2 thay vì im lặng), nên lần này cơ chế **hoạt động như thiết kế**.

**Bốn cổng còn lại vẫn nguyên trạng lúc 19:30:** `_v10925_rule_sync_check --check` exit **0** ·
`_v10921_report_gate.py V10978` exit **0** (đủ 9 phần, đã push). Kết luận ở mục 10 **không đổi**.

### 11.1 Đính chính mục 3.2 — PID đã đổi lúc 19:23 (do V10977, không phải V10978)

Mục 3.2 ghi *"MainPID 645169 — không đổi"*, đúng tại thời điểm đo 19:10. Đo lại lúc **19:33**:

| | 19:10 | **19:33** |
|---|---|---|
| MainPID | 645169 | **738032** |
| Lên từ | 02/08 18:13:33 | **03/08 19:23:58** |
| Dòng cron đang bật | 76 | **81** |
| `/api/health` | 200 | **200** |

**Nguyên nhân là phiên V10977 deploy, không phải V10978.** Bằng chứng trên máy: hai file backend
được sửa trong 2 giờ qua là `_v10900_consistency_guard.py` (19:21) và `_v10879_nghiemthu_lane.py`
(19:23); **5 dòng cron mới** đều mang chú thích nguyên văn của họ:

```
# V10977 lượt vá: official chốt trôi tới 17:44:54 ngày 03/08
```

V10978 **không deploy, không restart, không đụng crontab** — toàn bộ probe của phiên này mở DB ở
chế độ `file:…?mode=ro`.

### 11.2 Hai phiên độc lập gặp nhau ở cùng một con số

Đáng chú ý: lượt vá của V10977 ghi lý do là *"official chốt trôi tới **17:44:54** ngày 03/08"* —
**đúng con số mà mục 3.4 của báo cáo này đo được độc lập** (MB chốt 17:44, chỉ còn 14 phút trước
hạn 17:58, sát nhất trong 30 ngày).

Hai phiên đi từ hai hướng khác nhau — một bên điều tra sự cố `/nghiệm-thu` không ra output, một
bên soát chuỗi 30 ngày — và **gặp nhau ở cùng một nguyên nhân gốc: biên giờ chốt của MB đang co
lại**. Đây là bằng chứng chéo mạnh cho `FU-256`, và cho thấy vấn đề không phải chuyện một ngày:
nó đã âm ỉ suốt tháng, chỉ tới hôm nay mới đủ sát để làm hỏng một lane.

`FU-256` giữ nguyên ngưỡng đã đặt (MT hoặc MB còn **< 8 phút**, hoặc **3 ngày liên tiếp < 12
phút** → báo đỏ), và nay có thêm một ca hỏng thật để chứng minh ngưỡng đó là cần thiết.
