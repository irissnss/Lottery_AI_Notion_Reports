# V10970 — Tổng hợp toàn phiên đào bới (arc V10933→V10969) + phân tích live 02/08 3/3

**Ngày:** 02/08/2026 · **Giờ VN thu thập bằng chứng:** ~21:16–21:20 · **Trạng thái:** CHỈ ĐỌC + báo cáo (không sửa production; tôn trọng QD-014)

---

## 1. Tóm tắt một đoạn

Đây là báo cáo **bao quát toàn arc** từ cứu `gemini-3.5` / đổi total (V10933–V10939) tới cổng lợi thế + dừng tiền (V10945/QD-013), đóng băng đường ra số (QD-014), đào tín hiệu MT (V10955), retrain/AUC (V10952–53), prompt RULES-FIRST (V10959), UI filter/du-doan-test (V10960/64), cơ chế học + mã công việc §58 (V10965–68), và kiểm hết live 02/08 (V10969). Live **02/08** ba miền **BT 3/3 WIN** (MN 43 · MT 69 · MB 52), chốt đúng hạn, hệ sạch — nhưng cổng lợi thế 90 ngày **vẫn ĐÓNG cả 3 miền**. Đo VPS: trong **90 ngày** chỉ **1** ngày 3/3 (chính hôm nay, 1,10%); trong **120 ngày** chỉ **2** ngày (23/04 và 02/08). Kỳ vọng độc lập theo tỉ lệ ngày WIN hệ ~**2,21%**. Kết luận trung thực: **3/3 hôm nay là biến thiên ngày / may**, không phải bằng chứng hệ đã có edge; QD-014 đóng băng nên gần như không có thay đổi path chọn số sau cửa sổ 01/08. Các model mới (`gpt-5.4`, `glm-5.1`, `gpt-oss-120b`) **có góp phiếu** vào số thắng hôm nay — đó là quan sát một ngày, **không** đủ để claim “đã tốt lên có hệ thống”.

---

## 2. Owner yêu cầu gì (nguyên văn)

### 2.1 Câu hỏi kích hoạt V10970 (02/08 ~21:14 VN)

> *"Quá nhiều vấn đề anh và em đã đề cập đến và đào bới trong suốt trò chuyện này em có thể tổng hợp lại đầy đủ , chiêt hơn nữa được không em? Đẩy thêm 1 báo cáo thật đầy đủ hơn nữa bao gồm tất cả các vấn đề anh đã đề cập, em đã xử lý , em đã tổng hợp, em đã đào bới, em đã ghi nhận chờ tới hạn , tất cả mọi thứ không bỏ sót bất kỳ nội dung nào trong trò chuyện này ? Đồng thời em đánh live hôm nay thành công nhờ đâu? Có thay đổi gì khiến 'tốt lên' hay chỉ may?"*

### 2.2 Các yêu cầu then chốt trong arc (rút nguyên văn / gần nguyên văn)

| Thời điểm (arc) | Nguyên văn rút |
|---|---|
| V10945 | Dừng đặt tiền thật khi hệ không hơn đánh bừa 90 ngày |
| V10954 | Tổng hợp chi tiết mọi vấn đề / tiến trình chờ quyết định / total mới đã áp chưa / xem ở đâu / nguyên nhân giảm sút |
| V10955 | Tín hiệu MT rơi ở đâu — CHỈ ĐỌC; nói thẳng nếu không cứu được |
| V10956 | Đóng băng đường ra số tới 08/08; đóng checkpoint di sản |
| V10959 | Prompt có ép model hội tụ? Hai prompt cùng model? |
| §56/A54 | Không muốn nhắc đi nhắc lại việc agent tra được |
| §57/A55 | Báo cáo public GitHub; Notion chỉ đọc |
| §58/A56 / QD-019 | Mã đọc + hạn ngày (phương án B) |
| V10969 | Hết live — kiểm tổng lực + đẩy báo cáo đầy đủ |
| QD-018 | Sau 08/08 làm đúng 3 bước tuần tự, không song song |

Chi tiết nguyên văn dài: `CONVERSATION_CONTEXT_V10970_20260802.md` + `evidence/owner_message_index.json` (199 mục index).

---

## 3. Đào bới / phát hiện — theo chủ đề

### 3.1 Tiền / edge / P&L / break-even / QD-013 cổng

| Chỉ số | Giá trị | Nguồn |
|---|---|---|
| Vốn 90 ngày | 579,2 triệu | V10945 |
| Thu 90 ngày | 445,9 triệu | V10945 |
| Lỗ | **−133,3 triệu (−23%)** | V10945 |
| Hòa vốn MN/MT | ~18,37% (1 điểm = 18k, ăn 98k) | V10945 / TONG_HOP |
| Hòa vốn MB | ~27,55% (1 điểm = 27k) | V10945 |
| Đánh bừa ước | MN/MT ~16,5% · MB ~23,8% | V10945 |
| Cổng mở khi | lợi thế ≥ **+3,0pp** và **z ≥ 2,0** (90 ngày) | QD-013 / `_v10945_edge_gate` |
| Cổng 02/08 18:48 | MN −0,38pp z−0,17 · MT −2,02pp z−0,81 · MB −7,21pp z−1,62 · **ĐÓNG** | V10969 |
| `cong_mo_tong` 21:16 | **false** | evidence_33_vps.json |

**QD-013:** dừng đặt tiền thật tới khi chứng minh lợi thế. Không mở lại vì một ngày đẹp.

### 3.2 MT mất tín hiệu sau May (RF → vote → published)

Chuỗi đo V10955 (MT, nửa sau từ 06/05, đếm đài):

| Tầng | Hit rate | vs bừa |
|---|---:|---|
| RF tự chọn | **19,91%** | **+3,42pp** (z 1,34) |
| Số thắng phiếu | 15,17% | −1,32pp |
| Số công bố | **12,32%** | **−4,16pp** |
| Rơi RF→công bố | | **−7,59pp** |

- Lợi thế MT tháng 2–5 từng **+9,57pp** (z 3,74); tháng 6 −1,14 · tháng 7 −1,83 (V10947 / FU-210).
- Ứng viên RF/XGB chỉ ~40 số/ngày → chỉ ~41% số trúng nằm trong bộ — bó trước cả xếp hạng.
- V10955b: RF live +3,42pp ≠ CSV holdout −2pp — hai thước khác nhau; đề xuất shadow RF đơn (QD-015).
- LSTM live lệch suy luận (FU-217) — đo riêng V10957.

### 3.3 Prompt herding / RULES-FIRST (V10959)

- Danh sách RULES-FIRST ~11 số; số thật trong list ~**12,4%** ≈ ngẫu nhiên.
- Model **chọn từ list** ~**35,8%** — bị ép hội tụ.
- Owner: QD-016 (sau 08/08, shadow bỏ ép chọn từ list); QD-017 (A/B hai prompt **cùng model** ≥14 ngày); QD-018 xếp thứ tự B1→B2→B3.

### 3.4 Retrain bugs & journal AUC (V10952–53)

- 7 chủ nhật 17/05→12/07: lỗi `I/O operation on closed file` — 12/12 model chết trong ~1 giây (đã sửa từ 15/07 V10800).
- Từ 19/07: câu ghi bảng rút cột → **0/12 dòng có AUC** dù status “OK”.
- V10952 sửa journal; V10952b chạy thật; V10953 xác minh job 02:00 — **12/12 có AUC** ngày 02/08. Đóng FU-211.
- FU-213: so AUC cũ↔mới đang lệch cửa sổ — chưa dùng để tự cắt model.

### 3.5 Ranking hypocrisy (WR vs BT)

- Bộ lọc từng chấm win rate trong khi owner đánh bạch thủ; `meta-learning` lệch −10,9pp giữa hai thước (V10938).
- Điểm ảo 50% để model 0 lượt cướp suất (V10936) — đã bỏ, yêu cầu ≥5 lượt thật.
- Cắt `gpt-5.4` vội rồi gọi về thay `combo-no-token` (V10937/39).
- FU-230 / FU-232: đồng bộ thước WR vs BT; nửa V10938 còn treo.

### 3.6 UI / filter / du-doan-test / deploy time guard

- `/filter` trùng/khó xem (V10960); sticky + gom card + `Cache-Control: no-store` (V10964/64b).
- `/du-doan-test` neo ngày lệch múi giờ / fallback ngày cũ (V10964/64b) — MN/MT/MB cùng `requested_date`.
- Deploy 01/08 17:45 chạm T-chốt 17:55: model_count 15→14, BT may không đổi (V10940) → FU-207 / V10968 chốt cửa sổ cấm deploy.
- FU-225 · UI0803 · hạn 03/08: chờ owner verify tay.

### 3.7 Cơ chế học & xếp hạng map (V10965/65b/68)

- Bản chính: `docs/CO_CHE_HOC_VA_XEP_HANG.md` (~18 cơ chế sống).
- Optimizer chủ nhật 03:00: kết quả tốt nhất vẫn **âm cả 3 miền**.
- 105 luật sống nhồi prompt: **chưa đo** có giúp số công bố không (FU-234).
- QD-018: B1 tắt optimizer → B2 đo 105 luật → B3 gỡ ép RULES-FIRST — mỗi bước ≥7–14 ngày.

### 3.8 Live 02/08 — vận hành (V10969 + đo bổ sung V10970)

| Miền | Hạn | Giờ chốt | BT | Status | model_count |
|---|---|---|---|---|---|
| MN | 15:45 | 05:18:43 | 43 | **WIN** | 15 |
| MT | 16:58 | 16:41:36 | 69 | **WIN** | 13 |
| MB | 17:58 | 17:37:53 | 52 | **WIN** | 14 |

Health 200 · PID 645169 · journal 0 traceback · consistency 16/16 · training AUC 12/12 · pool 15 có gpt-5.4 không combo-no-token.

### 3.9 Voters / model góp số thắng 02/08 (VPS `source_predictions_json`)

| Miền | BT công bố | Voters top-1 (ranked_numbers[0]) |
|---|---|---|
| MN | 43 | glm-5.1, **gpt-5.4**, gemini-2.5-pro, deepseek-reasoner, claude-opus-4-6, claude-sonnet-4-6 |
| MT | 69 | glm-5.1, **gpt-5.4**, deepseek-reasoner, claude-opus-4-6 |
| MB | 52 | deepseek-reasoner, **gpt-oss-120b**, glm-5.1, gemini-2.5-pro, gemini-2.5-flash |

Nhận xét: `glm-5.1` / `gpt-5.4` / `gpt-oss-120b` (đưa vào official 01/08) xuất hiện trong voters thắng — **một ngày**, không suy ra edge 90 ngày.

### 3.10 Mọi cỡ mẫu đã đo (index nhanh)

| Đo | Cỡ / cửa sổ | Version |
|---|---|---|
| P&L thật | 7/30/90 ngày | V10945 |
| Edge gate | 90 ngày × 3 miền | V10945/69 |
| MT RF→publish drop | nửa sau từ 06/05 | V10955 |
| AUC 4 họ MT | holdout / metrics 02/08 | V10952/55 |
| RULES-FIRST coverage | ~11 số/list | V10959 |
| 3/3 BT WIN ngày | 120/90/30 ngày VPS | **V10970** |
| Override lệch phiếu | 67/180 lượt | V10917 |

---

## 4. Hướng xử lý và vì sao chọn

| Hướng | Chọn? | Vì sao |
|---|---|---|
| Mở tiền / claim edge vì 3/3 | **Không** | Cổng 90d ĐÓNG; 3/3 = 1/91; kỳ vọng ~2% |
| Đổi roster / combo / override ngay | **Không** | QD-014 đóng băng tới hết 08/08 |
| Shadow RF MT (QD-015) sau 08/08 | **Có (đã ký)** | Thu hồi ~3pp ước; cổng khớp live↔re ≥95% 7 ngày đầu |
| Gỡ RULES-FIRST official ngay | **Không** | Chỉ shadow sau 08/08; xếp sau B1/B2 (QD-018) |
| Báo cáo tổng hợp V10970 | **Có** | Owner yêu cầu không bỏ sót + phân tích may vs thật |
| Bịa V10963/66 | **Không** | Không có CHANGELOG giao hàng |

Phương án loại: “tỉa thêm model vì hôm nay đẹp” — loại vì FU-209 / QD-013 / không có z-score.

---

## 5. Đã làm gì

### 5.1 Phiên V10970 (báo cáo này)

| File / việc | Thay đổi |
|---|---|
| `Lottery_AI_Notion_Reports/V10970_…/` | REPORT + CONTEXT + evidence |
| `docs/TONG_HOP_TOAN_PHIEN_V10970.md` | Bản rút owner-facing |
| CHANGELOG / SSOT / FOLLOW_UP | Prepend V10970 (TK báo cáo) |
| `artifacts/v10970/` | evidence_33_vps · model_attr · owner index |
| Deploy / restart / hash 4 bảng | **Không đụng** |

### 5.2 Bảng version × kết quả (arc — không bịa commit nếu chưa ghi)

| Version | Chủ đề | Kết quả chính | Runtime? |
|---|---|---|---|
| V10933 | Cứu gemini-3.5 503 | Khai OpenRouter; shadow | Có |
| V10934 | Tính lại total | Code; deploy sau | Có (qua V10939) |
| V10936 | Bộ lọc combo | Bỏ điểm ảo 50%; pool 7→9 | Có (V10939) |
| V10937/38 | Hai thước đo | Gọi về gpt-5.4; chấm BT | Có (V10939) |
| V10939 | Deploy gói | Total mới live | **Có** |
| V10940 | Deploy chạm T-chốt | BT không đổi; mc 15→14 | Quan sát |
| V10945 | Edge gate + dừng tiền | QD-013 | Đo + UI |
| V10947 | Luồng nào để chơi? | Không luồng $; MT từng có edge | Chỉ đọc |
| V10952–53 | Retrain/AUC | 12/12 AUC; đóng FU-211 | Sửa journal |
| V10954 | Tổng hợp tình hình | docs/TONG_HOP… | Tài liệu |
| V10955/55b | Tín hiệu rơi | −7,59pp RF→publish | Chỉ đọc |
| V10956 | Đóng CP + QD-014 | Freeze tới 08/08 | Tài liệu |
| V10957 | LSTM + QD-015 | Shadow RF kế hoạch | Chỉ đọc |
| V10958 | Đọc nhầm FU | Reader đầu file | Tooling |
| V10959 | RULES-FIRST | Herding đo được | Chỉ đọc |
| V10960/64/64b | UI filter + neo ngày | Deploy UI | UI only |
| V10961 | Rà sót Notion/nội bộ | Notion = lịch sử | Chỉ đọc |
| V10962 | QD-016/017 + FINAL 16:58 | Ledger khớp code | Tài liệu |
| V10965/65b/67/68 | Học + mã §58 + deploy guard | QD-018/019 | Tài liệu + guard |
| V10969 | Hết live 3/3 | Hệ sạch; edge ĐÓNG | Chỉ đọc |
| **V10970** | Tổng hợp toàn phiên + may vs edge | Báo cáo này | Chỉ đọc |

Backup: không sửa runtime → không backup file production. Evidence VPS trong `evidence/`.

---

## 6. Cổng kiểm

| Kiểm | Kết quả |
|---|---|
| Session start | 0 checkpoint quá hạn (lúc chạy V10970) |
| Nguồn V10969 bundles 3/3 | Khớp VPS 21:16 |
| 3/3 lịch sử 90/120 ngày | 1/91 và 2/121 |
| Edge gate vẫn ĐÓNG | Đạt |
| Model voters BT hôm nay | Có trong evidence |
| Không sửa `/du-doan` writer | Đạt |
| Notion ghi | **Không** |
| Secrets trong evidence | Quét — chỉ JSON đo; không key |
| `_v10921_report_gate.py V10970` | Chạy sau push — phải đạt |

---

## 7. Vướng vấp

1. **Sync forensic local size-mismatch** (`remote=646074368 local=646078464`) — không dùng DB local làm SSOT cho hôm nay; chuyển sang query VPS. Hậu quả nếu bỏ qua: kết luận sai vì thiếu ngày 02/08 trên local.
2. **Gán model lần 1 thất bại** vì `source_predictions_json` là dict `ranked_numbers` không phải list model — đã sửa cách đọc. Hậu quả nếu bỏ qua: báo “không truy được model”.
3. **Một ngày 3/3 dễ bị diễn giải thành “hệ đã tốt”** — nếu bỏ qua cửa sổ 90 ngày + cổng z: mở tiền sớm → lặp lỗ 133 triệu.
4. **model_count MT 13 / MB 14 < 15** — pool eligible đủ nhưng bundle thiếu phiếu; dễ báo sai “đủ 15”.
5. **Push public từng bị chặn secret** (V10969 `anthropic_api_key` base64) — V10970 không nhúng probe có key.

---

## 8. Gỡ về

Không đổi runtime. Gỡ báo cáo/tài liệu:

```text
# Public
rmdir /s /q E:\Lottery_AI_Notion_Reports\V10970_TONG_HOP_TOAN_PHIEN_DAO_BOI_20260802

# Private docs (nếu đã commit)
git checkout HEAD~1 -- CHANGELOG.md docs/CURRENT_TRUTH_SSOT.md docs/FOLLOW_UP_TRACKER.md docs/TONG_HOP_TOAN_PHIEN_V10970.md docs/AUTOMATION_STATE.json
```

Thời gian: < 5 phút.

---

## 9. Theo dõi tiếp — FU/QD/CP còn treo (mã đọc §58)

### Canh sát 08/08

| Mã | Mã đọc | Việc | Hạn | Status |
|---|---|---|---|---|
| QD-014 / FU-215 | DB0808 | Đóng băng đường ra số | 08/08 | OWNER_LOCK |
| QD-013 / FU-208 | KSLX / KS0808 | Cổng lợi thế — chỉ đặt tiền khi mở | LX / 08/08 | ACTIVE |
| QD-015 / FU-216 | XH0808-1 | Shadow MT RF đơn | 08/08 | OWNER_LOCK |
| QD-016 / FU-231 | HT0808-1 | Bỏ ép RULES-FIRST (shadow) | 08/08 | OWNER_LOCK |
| QD-017 / FU-226 | HT0808-2 | A/B hai prompt cùng model | 08/08 | OWNER_LOCK |
| FU-210 | DO0808-1 | Tháng 6 mất lợi thế MT | 08/08 | MEASURED |
| FU-217 | SC0808-1 | LSTM live lệch | 08/08 | MEASURED |
| FU-203 | DO0808-2 | gemini-3.5 hồi phong độ | 08/08 | WAIT_LIVE |
| FU-207 | DP0808 | Mốc an toàn deploy | 08/08 | MEASURED |
| FU-209 | XHLX-209 | Dừng thêm/cắt model tới cổng mở | LX | ACTIVE |

### Sau 08/08 (QD-018 tuần tự)

| Bước | FU | Mã đọc | Việc | Hạn |
|---|---|---|---|---|
| B1 | FU-233 | HT0822-1 | Tắt tối ưu trọng số | 22/08 |
| B2 | FU-234 | DO0905 | Đo 105 luật có giúp công bố | 05/09 |
| B3 | FU-235 | HT0919 | Gỡ ép chọn từ list | 19/09 |

### Gần hạn khác

| FU | Mã đọc | Hạn | Ghi chú |
|---|---|---|---|
| FU-225 | UI0803 | 03/08 | Verify UI du-doan-test + filter |
| FU-185 | DD0803 | 03/08 | Lane hết hạn vẫn chạy |
| FU-189 | KS0802-1 | 02/08 | Lane nghỉ — đối chiếu bundle thiếu phiếu |
| FU-184 | KS0802-2 | 02/08 | MT/MB công bố đúng phiếu |
| FU-237 | DP0815 | 15/08 | Canh chốt giờ cấm deploy |
| FU-213 | HT0815 | 15/08 | Phép so AUC lệch cửa sổ |
| FU-228 | DO0815-4 | 15/08 | Đo hiệu quả cơ chế học |
| FU-229 | SC0815-2 | 15/08 | Champion selector cron |
| FU-230 | DO0815-3 | 15/08 | Đồng bộ WR vs BT |
| FU-232 | SC0815-3 | 15/08 | V10938 nửa còn |
| FU-204 | KS0815-1 | 15/08 | gpt-5.4 gọi về đúng |
| FU-224 | UI0809 | 09/08 | Dọn frontend trùng |
| FU-238 | KS0802-3 | 02/08 | Kiểm tổng lực — đóng bởi V10969 |

Ngưỡng hành động tiền: **không** đặt tiền thật tới khi edge gate mở (QD-013).

---

## Phụ lục A — Timeline phiên (giờ VN, rút)

| Mốc | Việc |
|---|---|
| 31/07 | Múi giờ VN + biên chốt 2 phút; FINAL MN 15:45 / MT 16:53 / MB 17:53 (sau V10931 → 16:58/17:58) |
| 01/08 sáng | V10931 promote glm-5.1 + gpt-oss-120b; dời FINAL |
| 01/08 | V10933–38: gemini-3.5, combo filter, hai thước, gọi về gpt-5.4 |
| 01/08 ~17:45 | V10939 deploy total mới; V10940 chạm T-chốt |
| 01/08 | V10945 edge gate + QD-013 dừng tiền; lỗ 133tr/90d |
| 01/08 tối | V10947: MT từng +9,57pp rồi tắt từ tháng 6 |
| 02/08 ~02:00 | Retrain CN — AUC 12/12 sau V10952/53 |
| 02/08 | QD-014 freeze; V10954–68 đào + UI + mã §58 + QD-015…019 |
| 02/08 05:18 | MN chốt BT 43 |
| 02/08 16:41 | MT chốt BT 69 |
| 02/08 17:37 | MB chốt BT 52 |
| 02/08 ~18:48 | V10969 kiểm hết live: 3/3 WIN, edge ĐÓNG |
| 02/08 ~21:14+ | Owner yêu cầu tổng hợp siêu đầy đủ + “may hay thật” → **V10970** |

Transcript gốc: `eeb49d3c-16d5-440b-9e2e-df1485c7bdf9`.

---

## Phụ lục B — QD-013…QD-019 (ngắn + trạng thái)

| QD | Nội dung ngắn | Trạng thái |
|---|---|---|
| **QD-013** | Dừng tiền thật tới khi chứng minh lợi thế (≥3pp, z≥2, 90d) | Đang hiệu lực — cổng ĐÓNG |
| **QD-014** | Đóng băng roster/combo/override tới hết 08/08 | Đang hiệu lực |
| **QD-015** | Sau 08/08: shadow MT RF đơn; cắt nếu live↔re <95% 7 ngày | Chờ hết freeze |
| **QD-016** | Sau 08/08: shadow bỏ ép chọn từ RULES-FIRST | Chờ hết freeze |
| **QD-017** | Sau 08/08: A/B hai prompt cùng model ≥14 ngày | Chờ hết freeze |
| **QD-018** | Sau freeze: B1→B2→B3 tuần tự 7–14 ngày/bước | Kế hoạch |
| **QD-019** | Quy ước mã công việc phương án B (§58) | Đã áp dụng |

---

## Phụ lục C — FU còn mở (ưu tiên)

Xem mục 9. Nhóm nóng: FU-215/208/216/231/226/210/217/225/207/209 + chuỗi QD-018 (233/234/235).

---

## Phụ lục D — Việc đã đóng / roadmap archive

| Mục | Ghi chú |
|---|---|
| FU-211 | Job huấn luyện 02:00 ghi AUC — ĐÓNG V10953 |
| FU-212 | Đo xong tín hiệu rơi — chuyển QD-015/FU-216 |
| FU-219 | FINAL 16:58 khớp — ĐÓNG V10962 |
| FU-220 | Bù báo cáo A55 — ĐÓNG V10962 |
| CP-X.1, CP-2.2, CP-4.0, CP-R4 | Owner đóng (di sản) — thay bằng edge gate |
| V10917 | Tắt 5 lớp ghi đè — đã deploy; theo dõi FU-186 |
| V10919 | 6 lane hết hạn nghỉ |
| V10969 / FU-238 | Kiểm hết live 02/08 |

---

## Phụ lục E — Phân tích 02/08 3/3: may hay thật?

### E.1 Số liệu VPS (2026-08-02 21:16 VN)

| Cửa sổ | Ngày đủ 3 miền WIN/LOSE | Số ngày 3/3 WIN | Tỉ lệ |
|---|---:|---:|---:|
| 30 ngày | 31 | **1** (02/08) | **3,23%** |
| 90 ngày | 91 | **1** (02/08) | **1,10%** |
| 120 ngày | 121 | **2** (23/04, 02/08) | **1,65%** |

Tỉ lệ ngày WIN hệ 90d (bach_thu_status theo ngày): MN **40,66%** · MT **32,97%** · MB **16,48%**.

Nếu độc lập: P(3/3) ≈ 0,4066×0,3297×0,1648 ≈ **2,21%**. Quan sát 1/91 ≈ 1,10% — **thấp hơn hoặc quanh kỳ vọng**, không phải outlier dương mạnh.

So với đánh bừa union đuôi ngày 02/08 (V10969): MN 46% · MT 43% · MB 26% → P(3/3|bừa độc lập) ≈ **5,14%** (thước khác — union tails/100). Hệ thắng cả 3 trong một ngày vẫn nằm trong nhiễu ngắn hạn.

### E.2 Thay đổi runtime 7–14 ngày trước 02/08 — có thể ảnh hưởng số official?

| Thay đổi | Ảnh hưởng path chọn số? | Kết luận với 3/3 |
|---|---|---|
| V10917 tắt 5 override | Có (ít ghi đè hơn) | Có thể đổi số một số ngày; **không** có z 90d chứng minh tốt lên |
| V10931 glm-5.1 + gpt-oss-120b vào | Có | Hôm nay chúng **có vote** số thắng — anecdote 1 ngày |
| V10939 gpt-5.4 vào / combo-no-token ra + filter combo | Có | Cùng anecdote; edge 90d vẫn âm |
| V10945 edge gate | Không (chỉ đo/UI) | Không làm BT thắng |
| V10952–53 journal AUC | Không đổi công thức publish cùng ngày | Không giải thích 3/3 |
| UI V10960/64 | Không | Không |
| **QD-014 freeze** từ 02/08 | Chặn thêm đổi path | Path ổn định sau 01/08 deploy |

### E.3 Kết luận một câu

**Hôm nay tốt chủ yếu nhờ biến thiên ngày (may / nhiễu), không phải bằng chứng hệ đã có lợi thế ổn định.** Có dấu vết model mới góp phiếu thắng — ghi nhận để theo dõi sau 08/08, **không** mở tiền, **không** claim “đã tốt lên có hệ thống” khi chưa có z-score cửa sổ dài.

Bằng chứng: `evidence/evidence_33_vps.json`, `evidence/model_attr_raw.json`, V10969 `het_live_evidence.json`.

---

## Phụ lục F — Index REPORT_V109xx trong arc

| Folder public | Ghi chú |
|---|---|
| [V10933_GEMINI35_RESCUE_20260801](https://github.com/irissnss/Lottery_AI_Notion_Reports/tree/main/V10933_GEMINI35_RESCUE_20260801) | Cứu gemini-3.5 |
| [V10934_TINH_LAI_TOTAL_20260801](https://github.com/irissnss/Lottery_AI_Notion_Reports/tree/main/V10934_TINH_LAI_TOTAL_20260801) | Tính lại total |
| [V10936_BO_LOC_COMBO_SUPER_20260801](https://github.com/irissnss/Lottery_AI_Notion_Reports/tree/main/V10936_BO_LOC_COMBO_SUPER_20260801) | Bộ lọc combo |
| [V10937_SOI_LAI_HAI_THUOC_DO_20260801](https://github.com/irissnss/Lottery_AI_Notion_Reports/tree/main/V10937_SOI_LAI_HAI_THUOC_DO_20260801) | Hai thước WR/BT |
| [V10945_DUNG_DAT_TIEN_20260801](https://github.com/irissnss/Lottery_AI_Notion_Reports/tree/main/V10945_DUNG_DAT_TIEN_20260801) | Dừng tiền + edge |
| [V10947_LUONG_NAO_DE_CHOI_20260801](https://github.com/irissnss/Lottery_AI_Notion_Reports/tree/main/V10947_LUONG_NAO_DE_CHOI_20260801) | Không luồng $ |
| [V10952_SUA_LOI_HUAN_LUYEN_ML_20260802](https://github.com/irissnss/Lottery_AI_Notion_Reports/tree/main/V10952_SUA_LOI_HUAN_LUYEN_ML_20260802) | Retrain bug |
| [V10952b_CHAY_THAT_RETRAIN_20260802](https://github.com/irissnss/Lottery_AI_Notion_Reports/tree/main/V10952b_CHAY_THAT_RETRAIN_20260802) | Chạy thật |
| [V10953_XAC_MINH_JOB_HUAN_LUYEN_20260802](https://github.com/irissnss/Lottery_AI_Notion_Reports/tree/main/V10953_XAC_MINH_JOB_HUAN_LUYEN_20260802) | Job 02:00 ĐẠT |
| [V10954_TONG_HOP_TINH_HINH_20260802](https://github.com/irissnss/Lottery_AI_Notion_Reports/tree/main/V10954_TONG_HOP_TINH_HINH_20260802) | Tổng hợp sớm |
| [V10955_TIN_HIEU_ROI_RUNG_O_DAU_20260802](https://github.com/irissnss/Lottery_AI_Notion_Reports/tree/main/V10955_TIN_HIEU_ROI_RUNG_O_DAU_20260802) | MT drop chain |
| [V10955b_LAM_RO_HAI_CON_SO_RF_20260802](https://github.com/irissnss/Lottery_AI_Notion_Reports/tree/main/V10955b_LAM_RO_HAI_CON_SO_RF_20260802) | RF +3,42 vs −2 |
| [V10956_DON_ROADMAP_VA_DONG_BANG_20260802](https://github.com/irissnss/Lottery_AI_Notion_Reports/tree/main/V10956_DON_ROADMAP_VA_DONG_BANG_20260802) | QD-014 |
| [V10957_LOI_LSTM_CHAY_LIVE_20260802](https://github.com/irissnss/Lottery_AI_Notion_Reports/tree/main/V10957_LOI_LSTM_CHAY_LIVE_20260802) | LSTM + QD-015 |
| [V10958_SUA_DOC_NHAM_TRANG_THAI_FU_20260802](https://github.com/irissnss/Lottery_AI_Notion_Reports/tree/main/V10958_SUA_DOC_NHAM_TRANG_THAI_FU_20260802) | FU reader |
| [V10959_PROMPT_EP_MODEL_HOI_TU_20260802](https://github.com/irissnss/Lottery_AI_Notion_Reports/tree/main/V10959_PROMPT_EP_MODEL_HOI_TU_20260802) | RULES-FIRST |
| [V10960_RA_SOAT_TRANG_FILTER_20260802](https://github.com/irissnss/Lottery_AI_Notion_Reports/tree/main/V10960_RA_SOAT_TRANG_FILTER_20260802) | /filter |
| [V10961_RA_SOAT_CHEO_TIM_BO_SOT_20260802](https://github.com/irissnss/Lottery_AI_Notion_Reports/tree/main/V10961_RA_SOAT_CHEO_TIM_BO_SOT_20260802) | Rà sót |
| [V10962_GHI_QUYET_DINH_VA_DON_LECH_20260802](https://github.com/irissnss/Lottery_AI_Notion_Reports/tree/main/V10962_GHI_QUYET_DINH_VA_DON_LECH_20260802) | QD-016/017 |
| [V10964_SUA_NEO_NGAY_DU_DOAN_TEST_20260802](https://github.com/irissnss/Lottery_AI_Notion_Reports/tree/main/V10964_SUA_NEO_NGAY_DU_DOAN_TEST_20260802) | Neo ngày |
| [V10964b_HOAN_TAT_NEO_NGAY_FILTER_20260802](https://github.com/irissnss/Lottery_AI_Notion_Reports/tree/main/V10964b_HOAN_TAT_NEO_NGAY_FILTER_20260802) | Addendum UI |
| [V10965_CO_CHE_HOC_VA_QUY_UOC_MA_20260802](https://github.com/irissnss/Lottery_AI_Notion_Reports/tree/main/V10965_CO_CHE_HOC_VA_QUY_UOC_MA_20260802) | Cơ chế + mã |
| [V10965b_CO_CHE_HOC_DAY_DU_20260802](https://github.com/irissnss/Lottery_AI_Notion_Reports/tree/main/V10965b_CO_CHE_HOC_DAY_DU_20260802) | Bản đầy đủ |
| [V10967_QUY_UOC_MA_VA_KE_HOACH_SAU_0808_20260802](https://github.com/irissnss/Lottery_AI_Notion_Reports/tree/main/V10967_QUY_UOC_MA_VA_KE_HOACH_SAU_0808_20260802) | §58 + QD-018 |
| [V10968_GOP_TAI_LIEU_VA_CHOT_GIO_DEPLOY_20260802](https://github.com/irissnss/Lottery_AI_Notion_Reports/tree/main/V10968_GOP_TAI_LIEU_VA_CHOT_GIO_DEPLOY_20260802) | Gộp docs + deploy guard |
| [V10969_KIEM_TONG_LUC_HET_LIVE_20260802](https://github.com/irissnss/Lottery_AI_Notion_Reports/tree/main/V10969_KIEM_TONG_LUC_HET_LIVE_20260802) | Hết live 3/3 |
| **V10970_TONG_HOP_TOAN_PHIEN_DAO_BOI_20260802** | Báo cáo này |

(Các folder trùng tên V10964/V10965 giữ nguyên lịch sử; ưu tiên bản `b` khi có.)
