# V10971 — Bàn giao máy mới + tổng hợp ~20 ngày (13/07→02/08) + live 02/08 may vs edge

**Ngày:** 02/08/2026 · **Giờ VN:** ~21:26+ · **Commit riêng:** 6aca275 · **Commit công khai:** ee75f2c · **Trạng thái:** CHỈ ĐỌC + báo cáo + gói handoff (không sửa production path chọn số; tôn trọng QD-014)

**Nền:** kế thừa V10970 / V10969 — **không** copy nguyên; cửa sổ rộng hơn (~20 ngày) + checklist máy mới.

---

## 1. Tóm tắt một đoạn

Gói **V10971** là bàn giao sang máy local khác: tổng hợp **không bỏ sót** các quyết định / đào bới / fix / chờ hạn từ arc gần đây (đặc biệt 01–02/08) và timeline **~13/07/2026 → 02/08/2026**, đẩy đủ báo cáo lên GitHub công khai kèm checklist handoff. Live **02/08** BT **3/3 WIN** (MN 43 · MT 69 · MB 52), chốt đúng hạn, hệ sạch — nhưng cổng lợi thế 90 ngày **vẫn ĐÓNG**; trong 90 ngày chỉ **1/91** ngày 3/3; kỳ vọng độc lập ~**2,21%**. Kết luận giữ nguyên V10970: **nhiễu ngày / may**, không claim hệ đã tốt lên có hệ thống. QD-014 đóng băng đường ra số tới hết **08/08**. Máy mới: pull 2 repo → đọc CLAUDE/ledger/SSOT/FU → session_start → làm FU-225 / docs trong freeze; không đụng roster/combo/override.

---

## 2. Owner yêu cầu gì (nguyên văn)

### 2.1 Kích hoạt V10971 (02/08 ~21:26 VN) — ý nguyên văn

1. Tổng hợp đầy đủ hơn nữa mọi vấn đề đã đề cập / đào bới / xử lý / chờ hạn trong trò chuyện + **không bỏ sót**.
2. Đồng thời: trong **~20 ngày** gần đây có nhiều yêu cầu / đào bới / code fix — tổng hợp thật kỹ.
3. Đẩy báo cáo thật đầy đủ lên GitHub công khai.
4. Trả lời: live 02/08 thành công nhờ đâu / có thay đổi gì làm tốt lên?
5. Mục đích: **chuyển máy local khác** — không thiếu soát, tiếp tục code/fix liền mạch.

### 2.2 Câu kích hoạt V10970 vẫn là gốc (02/08 ~21:14)

> *"Quá nhiều vấn đề anh và em đã đề cập đến và đào bới trong suốt trò chuyện này em có thể tổng hợp lại đầy đủ , chiêt hơn nữa được không em? … Đồng thời em đánh live hôm nay thành công nhờ đâu? Có thay đổi gì khiến 'tốt lên' hay chỉ may?"*

### 2.3 Các chốt then chốt còn hiệu lực (rút)

| Mốc | Nội dung |
|---|---|
| QD-013 | Dừng đặt tiền thật tới khi chứng minh lợi thế |
| QD-014 | Đóng băng đường ra số tới hết 08/08 |
| §57/A55 | Báo cáo public; Notion chỉ đọc |
| §56/A54 | Tra cứu trước khi hỏi |
| §58/A56 / QD-019 | Mã đọc + hạn (phương án B) |
| QD-018 | Sau 08/08 làm đúng 3 bước tuần tự |

---

## 3. Đào bới / phát hiện

### 3.1 Live 02/08 — may vs thật (tái khẳng định số V10969/V10970)

| Chỉ số | Giá trị |
|---|---|
| BT | MN **43 WIN** · MT **69 WIN** · MB **52 WIN** |
| Giờ chốt | MN 05:18:43 · MT 16:41:36 · MB 17:37:53 (đúng hạn) |
| model_count bundle | MN 15 · MT **13** · MB **14** |
| Edge 90d ~18:48 | MN −0,38pp · MT −2,02pp · MB −7,21pp · **ĐÓNG** |
| 3/3 trong 90 ngày | **1/91** (1,10%) — chính hôm nay |
| 3/3 trong 120 ngày | **2/121** (23/04 + 02/08) |
| P(3/3) kỳ vọng độc lập theo tỉ lệ WIN hệ 90d | ≈ **2,21%** |
| Health / PID (V10969) | 200 · `lottery` active · PID **645169** |
| Consistency | 16/16 · training AUC 12/12 · journal traceback **0** |

**Kết luận:** 3/3 = biến thiên ngày. Không mở tiền. Không claim edge.

Voters thắng (anecdote 1 ngày, V10970): có `gpt-5.4` / `glm-5.1` / `gpt-oss-120b` — ghi nhận theo dõi, không đủ z-score.

### 3.2 Thay đổi runtime 7–14 ngày trước 02/08

| Thay đổi | Ảnh hưởng path số? | Với 3/3 |
|---|---|---|
| V10917 tắt 5 override | Có | Có thể đổi số một số ngày; không có z 90d |
| V10931 glm-5.1 + gpt-oss-120b + FINAL 16:58/17:58 | Có | Vote thắng hôm nay = anecdote |
| V10939 gpt-5.4 vào / combo-no-token ra + filter combo | Có | Cùng anecdote; edge vẫn âm |
| V10945 edge gate | Không (đo/UI) | Không làm BT thắng |
| V10952–53 journal AUC | Không đổi công thức publish cùng ngày | Không giải thích 3/3 |
| UI V10960/64/64b | Không | Không |
| QD-014 freeze từ 02/08 | Chặn thêm đổi path | Path ổn định sau 01/08 |

### 3.3 Tiền / edge (V10945 — vẫn đúng hướng)

| Cửa sổ | Vốn | Thu | Lãi/lỗ |
|---|---:|---:|---:|
| 90 ngày | 579,2 tr | 445,9 tr | **−133,3 tr (−23%)** |

Hòa vốn MN/MT ~18,37% · MB ~27,55%. Ngưỡng mở cổng: ≥+3pp & z≥2.

### 3.4 MT tín hiệu rơi (V10955)

RF tự chọn 19,91% (+3,42pp) → công bố 12,32% (−4,16pp) · rơi **−7,59pp**. Tháng 2–5 từng +9,57pp; tháng 6–7 tắt. → QD-015 shadow RF đơn sau 08/08.

### 3.5 RULES-FIRST herding (V10959)

Số thật trong list ~12,4% ≈ ngẫu nhiên; model chọn từ list ~35,8%. → QD-016/017 + xếp sau B1/B2 (QD-018).

### 3.6 Retrain / AUC (V10952–53)

7 CN chết I/O (đã sửa 15/07); journal AUC mất từ 19/07 → sửa V10952; 02/08 **12/12 AUC**. FU-211 đóng. FU-213 còn lệch cửa sổ so sánh.

### 3.7 Timeline ~20 ngày (13/07 → 02/08) — theo ngày VN

| Ngày | Chủ đề chính (rút) | Version / báo cáo |
|---|---|---|
| **13–14/07** | Cycle review /choi combo · cold day · forensic total | V10794–V10796 |
| **15/07** | Improve pack · T-chốt · consistency · **full timetable** · ML mark A/B · chase bias · rules engine | V10797–V10805 |
| **16/07** | Rule routing nhầm miền · sandbox A/B · station merge · BT phụ JS · API key rotation | V10806–V10812 |
| **17/07** | Morning audit · Qwen/Grok · GĐB đảo · prompt pha · **RULES-FIRST live** | V10813–V10820 |
| **18–19/07** | TOTAL V2/V3 · day1 forward · GĐB xuôi cross | V10821–V10825 |
| **20–21/07** | Miner · cond A/B · day forensic · TOTAL_V3_COND live | V10826–V10832 |
| **22–23/07** | Timing causality · Bugbot hardening · herd bypass | V10833–V10841 |
| **24–25/07** | Morning/EOD · what-if MB · /choi realtime · UI teal · drift audit | V10842–V10848 |
| **26–27/07** | UI polish · output contract §54 · accuracy responsive · closeout 0/3 | V10855–V10868 |
| **28–29/07** | CP-L6 deep control · MN empty · quality roster · deherd · total bakeoff | V10869–V10874 |
| **30/07** | MN economics · /choi history · nghiệm thu lane · routing · official new lane | V10876–V10883 |
| **31/07** | Acceptance · FINAL means done · region mechanics · **tz VN + biên 2 phút** · consistency guard | V10884–V10906 |
| **01/08** | Override off · A54/A55 rules · model swap FINAL 16:58 · gemini rescue · combo filter · hai thước · **deploy total** · edge gate dừng tiền · MT edge tắt | V10917–V10947 |
| **02/08** | Retrain AUC · tổng hợp · tín hiệu rơi · **freeze QD-014** · RULES-FIRST · UI · §58 · deploy guard · hết live 3/3 · V10970 tổng hợp · **V10971 handoff** | V10952–V10971 |

Chi tiết từng folder: `evidence/public_report_index_20d.json` (**116** folder public trong cửa sổ ngày-trong-tên 13/07–02/08).

### 3.8 Bảng version trọng yếu cửa sổ (không liệt kê hết 100+; đủ để không rơi quyết định)

| Version | Làm gì | Kết quả | Treo? |
|---|---|---|---|
| V10800 | Full timetable audit | Nền playbook; sửa retrain process | — |
| V10820 | RULES-FIRST live | Herding đo sau (V10959) | QD-016… |
| V10861–66 | /choi contract + UI hệ | §54; UI live | polish FU |
| V10872 | Deherd lane | Shadow thắng backtest — **không** tự promote vào freeze | cẩn thận backtest rữa |
| V10893–V10905 | FINAL + tz VN | FINAL rồi dời 16:58/17:58 | OD-20260731-* |
| V10917 | Tắt 5 override | Deploy | FU-186 cửa sổ |
| V10919 | 6 lane nghỉ | Cron 83→71 | FU-185/189 |
| V10931 | glm-5.1 + gpt-oss-120b | Deploy; FINAL mới | — |
| V10933–39 | gemini / combo / BT metric / gpt-5.4 | Total mới live ~17:45 | — |
| V10940 | Deploy chạm T-chốt | BT không đổi; mc 15→14 | FU-207 → V10968 |
| V10945 | Edge gate | QD-013; lỗ 133tr/90d | cổng ĐÓNG |
| V10947 | Luồng chơi? | Không luồng $; MT từng edge | FU-210 |
| V10952–53 | Retrain/AUC | 12/12; đóng FU-211 | FU-213 |
| V10954–55b | Tổng hợp + tín hiệu rơi | −7,59pp | QD-015 |
| V10956 | Freeze | QD-014 | FU-215 |
| V10957–59 | LSTM + RULES-FIRST | Kế hoạch shadow | QD-015…017 |
| V10960–64b | UI filter + neo ngày | Deploy UI | **FU-225** |
| V10965–68 | Học + §58 + deploy guard | QD-018/019 | FU-233…237 |
| V10969 | Hết live | 3/3; edge ĐÓNG | — |
| V10970 | Tổng hợp arc + may | Báo cáo | — |
| **V10971** | Handoff 20 ngày | Gói này | FU mới TK |

### 3.9 Production hiện tại (từ V10969 + registry local)

| Mục | Giá trị |
|---|---|
| Service | `lottery` active |
| PID (18:48) | 645169 (sau deploy V10964b 18:13) |
| Pool | **15** có gpt-5.4; không combo-no-token |
| Deadlines | 15:45 / 16:58 / 17:58 |
| Edge | **CLOSED** cả 3 |
| Official path chọn số | **Đóng băng** tới hết 08/08 |

### 3.10 Transcript phiên này vs V10970

Ask còn lại sau V10970 = **gói bàn giao máy mới + mở cửa sổ 20 ngày** (chính V10971). Các ask trước (hết live, tổng hợp may/thật, §58, freeze…) đã nằm trong V10969/70 và ledger.

---

## 4. Hướng xử lý và vì sao chọn

| Hướng | Chọn? | Vì sao |
|---|---|---|
| Claim hệ tốt lên vì 3/3 | **Không** | Edge ĐÓNG; 1/91; kỳ vọng ~2% |
| Đổi roster/combo trong phiên | **Không** | QD-014 |
| Gói handoff + index 20 ngày + push A55 | **Có** | Owner chuyển máy — không rơi thông tin |
| Copy nguyên V10970 | **Không** | Phải rộng hơn + checklist máy mới |
| Ghi Notion | **Không** | §57 |
| Đo lại VPS 3/3 trong phiên này | Kế thừa V10970 | Số đã có; không đụng production |

Phương án loại: “tỉa model vì hôm nay đẹp” — loại (FU-209 / không z).

---

## 5. Đã làm gì

| File / việc | Thay đổi |
|---|---|
| `Lottery_AI_Notion_Reports/V10971_BAN_GIAO_MAY_MOI_20_NGAY_20260802/` | REPORT · CONTEXT · HANDOFF_CHECKLIST · INDEX_QD_FU · evidence |
| `docs/BAN_GIAO_MAY_MOI_V10971.md` | Mirror ngắn private |
| CHANGELOG / SSOT / FOLLOW_UP | Prepend V10971 (TK bàn giao) |
| `artifacts/v10971_handoff/` | index public 20d |
| Deploy / restart / hash 4 bảng | **Không đụng** |

Backup runtime: không áp dụng (không sửa production).

### Việc ĐƯỢC / CẤM tới 08/08

**CẤM:** đổi 15 model · combo-super constants · override toggles · mở tiền · promote shadow.

**ĐƯỢC:** tech fix rõ · đo shadow/chỉ-đọc · docs · UI verify FU-225 · báo cáo A55 · deploy guard ngoài khung nóng.

### Kế hoạch SAU 08/08

1. QD-015 RF shadow MT (cắt nếu &lt;95% khớp 7 ngày)  
2. QD-018 B1 tắt optimizer → B2 đo 105 luật → B3 gỡ RULES-FIRST (QD-016)  
3. QD-017 A/B prompt cùng model ≥14 ngày (không chồng B1–B3 nếu owner chưa xếp lại)

---

## 6. Cổng kiểm

| Kiểm | Kết quả |
|---|---|
| Session start 02/08 | 0 CP quá hạn; 82 FU treo / 0 quá hạn briefing |
| Kế thừa số live/edge V10969–70 | Khớp — không claim edge |
| Index public 20d | **116** folder trong evidence JSON |
| HANDOFF + INDEX có trong folder | Đạt |
| 9 phần A55 đủ tiêu đề | Đạt (báo cáo này) |
| Notion ghi | **Không** |
| Secrets | Không nhúng key; index chỉ path/URL |
| `_v10921_report_gate.py V10971` | Chạy sau push — phải PASS |

---

## 7. Vướng vấp

1. **Briefing file `_BRIEFING_DAU_PHIEN.txt` có thể cũ ngày** trong khi script session_start in ra ngày mới — luôn tin stdout lệnh vừa chạy. Hậu quả nếu bỏ qua: nêu CP quá hạn đã đóng.
2. **116 folder public / 100+ version CHANGELOG** — không thể nhét full prose từng bản vào 1 file; dùng index JSON + bảng trọng yếu. Hậu quả nếu bỏ: tưởng thiếu sót khi thực ra đã index.
3. **Một ngày 3/3 dễ diễn giải thành “áo mới hiệu quả”** — nếu bỏ cửa sổ 90d → mở tiền sớm → lặp lỗ 133tr.
4. **Sync forensic size-mismatch** (V10970) — máy mới dễ tin DB local. Phải sync hoặc VPS.
5. **Push public từng dính secret base64** — quét evidence trước push.
6. **Roadmap ACTIVE còn file cũ** — không hỏi lại CP di sản đã đóng (A54).

---

## 8. Gỡ về

Không đổi runtime.

```text
# Public
rmdir /s /q E:\Lottery_AI_Notion_Reports\V10971_BAN_GIAO_MAY_MOI_20_NGAY_20260802

# Private docs (sau commit): checkout file prepend
git checkout HEAD~1 -- CHANGELOG.md docs/CURRENT_TRUTH_SSOT.md docs/FOLLOW_UP_TRACKER.md docs/BAN_GIAO_MAY_MOI_V10971.md docs/AUTOMATION_STATE.json
```

Thời gian: &lt; 5 phút.

---

## 9. Theo dõi tiếp

Xem đầy đủ: [INDEX_QUYET_DINH_FU_V10971.md](./INDEX_QUYET_DINH_FU_V10971.md) · [HANDOFF_CHECKLIST_V10971.md](./HANDOFF_CHECKLIST_V10971.md)

**Top ưu tiên máy mới:**

1. **FU-225 · UI0803 · hạn 03/08** — owner verify UI  
2. Tôn trọng **FU-215 / QD-014** tới hết 08/08  
3. **FU-208 / QD-013** — không đặt tiền khi cổng ĐÓNG  
4. Sau 08/08: **FU-216 / QD-015** rồi chuỗi **FU-233→234→235**  
5. **FU-189 / FU-184** — bundle MT 13 / MB 14 vs kỳ vọng phiếu  

Ngưỡng tiền: không đặt thật tới edge ≥+3pp & z≥2 (90d).

---

## Phụ lục H1 — Checklist 5 bước đầu máy mới

1. Pull `Lottery_AI_Test` + `Lottery_AI_Notion_Reports`  
2. Đọc CLAUDE → ledger → SSOT → FOLLOW_UP → V10970/V10971  
3. `python web/backend/_v10920_session_start.py`  
4. Xác nhận QD-014 freeze + edge ĐÓNG  
5. Làm FU-225 / docs — **không** đụng roster  

## Phụ lục H2 — Index REPORT public (mẫu; full trong evidence)

Base: `https://github.com/irissnss/Lottery_AI_Notion_Reports/tree/main/`

Ưu tiên đọc gần nhất: V10971 · V10970 · V10969 · V10968 · V10967 · V10965b · V10964b · V10959 · V10956 · V10955 · V10945 · V10939/31 · V10917 · V10905 · V10872 · V10861 · V10820 · V10800.

Full 116 mục: `evidence/public_report_index_20d.json`.

## Phụ lục H3 — Live 02/08 một đoạn trả lời owner

Hôm nay 3/3 thắng **chủ yếu nhờ biến thiên ngày (may/nhiễu)**. Hệ vận hành sạch và đúng hạn; model mới có góp phiếu thắng — nhưng cửa sổ 90 ngày vẫn dưới ngưỡng cổng lợi thế, và tần suất 3/3 lịch sử không ủng hộ claim “đã tốt lên có hệ thống”. Trong freeze QD-014 không được diễn giải ngày đẹp thành lý do đổi path chọn số hay mở tiền.
