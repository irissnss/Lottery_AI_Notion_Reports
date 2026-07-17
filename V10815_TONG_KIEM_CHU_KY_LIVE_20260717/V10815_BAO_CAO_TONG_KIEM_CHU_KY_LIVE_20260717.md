# V10815 — TỔNG KIỂM CUỐI CHU KỲ LIVE 17/07/2026 (READ-ONLY)

**Thời gian phiên:** 17/07/2026 18:41 → 19:1x (UTC+7)
**Yêu cầu owner (18:41):** "hết chu kỳ live rồi em. kiểm tra toàn diện dùm anh dự đoán hôm nay và tất cả các ngày live vừa qua"
**Tính chất:** 100% READ-ONLY — 0 file code đổi, 0 restart, chỉ probe + cập nhật docs.

---

## 1. HÔM NAY 17/07 — KẾT QUẢ vs DỰ ĐOÁN

### 1.1 Kết quả về đúng nhịp, đủ đài
| Miền | Đài | Giờ về (UTC+7) | Coverage |
|---|---|---|---|
| MN | Vĩnh Long, Bình Dương, Trà Vinh (3/3 Thứ Sáu... đúng lịch T5→T6 giao ngày) | 16:38 | COMPLETE |
| MT | Gia Lai, Ninh Thuận (2/2 — Thứ Năm đúng 2 đài) | 17:31 | COMPLETE |
| MB | Hải Phòng (1/1) | 18:31 | COMPLETE |

0 chuông `[STATION_INCOMPLETE]`, PRIZE_CARD_COMPLETE cả 3 miền (27 slot/đài). Tên đài chuẩn (sau fix V10810).

### 1.2 Official TRẮNG cả 3 miền (cả BT lẫn lô-2)
| Miền | BT official | Lô2 official | Kết cục | Ghi chú |
|---|---|---|---|---|
| MN | 63 ✗ | [63, 34] 0/2 | LOSE | bundle chốt 04:18, 15 model, consensus strong |
| MT | 63 ✗ | [63, 84] 0/2 | LOSE | bundle 16:43 + K15 promote 16:54, 13 model |
| MB | 34 ✗ | [34, 86] 0/2 | LOSE | bundle 17:35 + K11a promote 17:54, 15 model |

- Ngày toàn-trượt cả 3 miền có tần suất nền **24%** trong lịch sử (đã đo V10796) — bản thân nó không phải bất thường hệ thống.
- Nét đáng chú ý: bầy hôm nay chụm **63** (xuất hiện BT ở cả MN + MT) và **34** (có mặt trong pick cả 3 miền, 12+ model MB) — đúng hình dạng trap hội tụ (CONV) đã mô tả ở V10806.

### 1.3 Tín hiệu thật CÓ nhưng bị vote bỏ (đơn model trúng lô hôm nay)
| Miền | Model trúng BT-vị-trí-1 vào lô | Model trúng số phụ |
|---|---|---|
| MN | grok-4.20 (95), lstm (66), smart-ensemble (66) | combo-no-token 66, deepseek-reasoner 64, gemini-2.5-flash 23, kimi 95, meta-learning 67, rf/smart-ml/xgb 95 |
| MT | gemini-3.5-flash (78) | grok-4.3 14, qwen3-max 43, qwen3.7-max 14, random-forest 36 |
| MB | **deepseek-reasoner (46), gpt-5.4 (46)** | meta-learning 02, smart-ml 02 |

- MB đau nhất: 2 model official cùng pick **46 ✓ lô** nhưng vote chọn 34 (herd) — thêm 1 case cho hồ sơ "bầy chụm không tăng hit" (V10796: modal-share cao không tăng tỷ lệ trúng).

### 1.4 K11a MB — champion ĐÚNG bị thay LẦN THỨ 4 (nóng nhất phiên)
| Ngày | Champion (cũ) | Challenger (applied) | Kết cục |
|---|---|---|---|
| 09/07 | 86 ✗ | 16 ✗ | hoà |
| 10/07 | 98 ✗ | 86 ✗ | hoà |
| 11/07 | **98 ✓** | 64 ✗ | champ đúng bị thay #1 |
| 12/07 | 35 ✗ | 72 ✗ | hoà |
| 13/07 | 35 ✗ | **89 ✓** | challenger thắng duy nhất |
| 14/07 | 67 ✗ | 51 ✗ | hoà |
| 15/07 | **57 ✓** | 64 ✗ | champ đúng bị thay #2 |
| 16/07 | **16 ✓** | 69 ✗ | champ đúng bị thay #3 |
| 17/07 | **02 ✓** | 34 ✗ | champ đúng bị thay #4 |

- **9 ngày: challenger BT 1/9 vs champion 4/9 = net −3 ngày do promote.** Chuỗi thua challenger 4 ngày (quy tắc kill = 5 liên tiếp, chưa chạm nhưng sát).
- → **Ưu tiên #1 agenda CP-L6 19/07: đề xuất flip kill-switch K11a về champion** (1 dòng, có sẵn từ thiết kế), trừ khi anh muốn chờ trio 23/07 cho đủ mẫu.

### 1.5 K15 MT — chạm ngưỡng báo (nhưng champion cũng thua y hệt)
| Ngày | Champion | Challenger (applied) |
|---|---|---|
| 10/07 | 16 ✗ | 16 ✗ |
| 11/07 | 94 ✗ | **61 ✓** |
| 12/07 | **43 ✓** | **64 ✓** |
| 13-17/07 | 31/45/22/94/84 đều ✗ | 31/17/19/40/63 đều ✗ |

- Challenger 2/8 vs champion 1/8 — vẫn nhỉnh hơn, **NHƯNG chuỗi thua challenger = 5 ngày liên tiếp (13-17/07) = ngưỡng "báo owner cân nhắc kill-switch"** theo quy tắc K15 gốc.
- Champion cũng thua đúng 5 ngày đó → lane KHÔNG tệ hơn baseline; 2 BT WIN duy nhất của MT trong 7 ngày (61, 64) đều là số challenger. **Khuyến nghị: GIỮ, quyết cùng CP-L6 19/07** (còn 2 ngày).

### 1.6 /choi hôm nay + freeze compliance
- /choi: MN **NGHỈ** (verdict engine đúng — 63 trượt); MT [94, 63] CÂN NHẮC trượt; MB [34, 75] CHƠI-Full trượt.
- Freeze: MN T-chốt 15:45:00 fired đúng giây · MT promote 16:54 < 16:55 ✓ · MB promote 17:54 < 17:55 ✓ · money board MB lock 17:55:17 ✓ (fix V10794 ngày 4 giữ nhịp).

---

## 2. V10814 (DEPLOY TRƯA NAY) — LIVE_VERIFIED CẢ 2 VIỆC

### 2.1 Grok 4.3 Thinking — 2 row shadow đầu tiên PASS
| Miền | Giờ | Picks | Kết cục | Bằng chứng call |
|---|---|---|---|---|
| MT | 16:53:13 | [58, 14] | **PARTIAL — 14 trúng lô MT ngay call đầu tiên** | 200, finish=stop, latency 42.6s, reasoning_tokens 5154 |
| MB | 17:50:36 | [34, 43] | LOSE | 200, finish=stop, latency 42.0s, reasoning_tokens 2378 |

- KEY_MODE journal: `grok-4.3: DB_GENERAL (openrouter_api_key from DB)` — đúng key OR chung, không key mới.
- ~24K token/call ≈ $0.05/call → ~$0.14/ngày 3 miền (đúng ước tính $0.15-0.25).
- Ngày đủ 3 miền đầu tiên: **18/07** (MN 04:2x + MT + MB).

### 2.2 Qwen3 Max Thinking — HẾT rỗng sau revert
| Row 17/07 | Giờ | Picks | Ghi chú |
|---|---|---|---|
| MN | 04:23 | **[] rỗng** | chạy TRƯỚC revert 12:40 — đúng bệnh cũ |
| MT | 16:44 | [63, 43] — **43 trúng lô phụ** | lần chạy ĐẦU sau revert: CÓ output |
| MB | 17:41 | [34, 43] | CÓ output |

- 2/2 lần chạy sau revert có output → FU-V10814-QWEN-EMPTY-REVERT chuyển **LIVE_VERIFIED_DAY1**; recheck empty-rate 7 ngày ~24/07 giữ nguyên.
- Shadow chiều nay đủ **12 MT + 12 MB rows, 0 rỗng**; MN 11 rows (grok-4.3 chưa vào chuỗi sáng — đúng thiết kế first_run).

---

## 3. CÁC NGÀY LIVE VỪA QUA (11-17/07)

### 3.1 Official 7 ngày
| Ngày | MN | MT | MB |
|---|---|---|---|
| 11/07 | 75✗ (lô2 1: 95) | **61✓** (lô2 1) | 64✗ |
| 12/07 | 64✗ | **64✓** (lô2 2: 64+10) | 72✗ (lô2 1: 17) |
| 13/07 | 94✗ | 31✗ | **89✓** (lô2 1) |
| 14/07 | 12✗ (lô2 1: 04) | 17✗ | 51✗ |
| 15/07 | 63✗ | 19✗ | 64✗ (lô2 1: 92) |
| 16/07 | **72✓ WIN ĐÔI** (lô2 2) | 40✗ | 69✗ |
| 17/07 | 63✗ | 63✗ | 34✗ |

- BT 7 ngày: MN 1/7 · MT 2/7 · MB 1/7. Điểm nhấn: **cả 3 BT WIN của MT+MB đều là số challenger lane** (61, 64 từ K15; 89 từ K11a) — lane có giá trị thật, vấn đề của K11a là nó THAY cả những ngày champion đúng.
- MT là miền hưởng K15 rõ nhất: lô2 có ăn 4/8 ngày kể từ K15.

### 3.2 Đơn model 7 ngày (BT vị-trí-1 trúng lô, n=21 lượt/model)
| Hạng | Model | BT% | any% |
|---|---|---|---|
| 1 | gemini-2.5-pro | **48%** | 48% |
| 2 | **gemini-3.5-flash (shadow)** | **43%** | 62% |
| 3-6 | claude-sonnet-4-6, deepseek-v4-pro-real, qwen3.7-max, smart-ensemble | 38% | 52-62% |
| … | gemini-2.5-flash (official) | 29% | 43% |
| … | gpt-5.5 (đắt nhất) | 29% | 38% |
| đáy | gemma-4-31b 14% · meta-learning 14% (any 67%!) · smart-ml 10% | | |

- **gemini-3.5-flash 43% > gemini-2.5-flash 29%** — bằng chứng swap (FU-V10812-GEMINI25-EOL) dày thêm cho CP-L6.
- meta-learning any 67% nhưng BT 14% = đúng "bệnh xếp vị trí" đã đo V10811 (tín hiệu có, chọn BT sai chỗ).
- gpt-5.5: 29% với giá đắt nhất — củng cố B1/B2 (đang chờ anh ký).

### 3.3 /choi 7 ngày (20 lượt lock)
- 6/20 lượt có hit: MT 4 (16+64 đôi 11/07 · 39 13/07 · 17 15/07 · 19 16/07), MB 2 (56+64 đôi 12/07 · 31 13/07), MN 1 (72 16/07).
- **Cảnh báo dải lạnh MB:** các lượt CHƠI-Full MB 14-17/07 trượt 4 ngày liên tục (sau khi 13/07 ăn 31); verdict engine vẫn CHƠI vì net_long 30.9M — đọc lại sau trio 23/07, chưa đổi gì.

### 3.4 Shadow A/B V10809 — day-2 đủ nhịp
- **15/15 row, err=0**, đúng 3 nhịp miền (MN 04:2x · MT 16:5x · MB 17:4x-17:50). Scorer 19:15 tối nay chấm chính thức.
- Tay-đếm sơ bộ: arm B main trắng BT như production (cùng chìm ngày herd); secondary B có ~4 hit lô (MN qwen 64✓ · MT opus 14✓ + gemini 61✓ · MB deepseek 13✓). SE3 ["00","00"] không tái diễn.

---

## 4. SỨC KHỎE HỆ + AN TOÀN PHIÊN

| Hạng mục | Kết quả |
|---|---|
| /api/health | 200 |
| /api/admin/chase-bias | 401 (đúng — require_admin) |
| Hash 4 bảng | Chỉ tăng trưởng tự nhiên trong ngày: predictions 10240→10280 · final_bundles 418→420 · lottery_results 15088→15094 · model_daily_eval 10064 (chấm tối 19:15/21:30 mới tăng — đúng lịch) |
| Journal chiều 16:00-18:40 | 0 lỗi thật; CASCADE MT 8/8 success; mọi call HTTP 200 (OR ×10/chuỗi = đủ cohort 9 + grok-4.3) |
| SCRAPE_FAIL 16:30 MN | Bình thường — vòng chờ kết quả trước khi đài công bố, tự hết lúc 16:38 khi 3 nguồn có data |
| Code/restart | 0 thay đổi — phiên read-only |

---

## 5. VIỆC CHỜ PHÍA TRƯỚC (xếp lịch)
1. **Tối nay 19:15**: scorer A/B day-2 + MDE chấm 17/07.
2. **18/07**: grok-4.3 ngày đủ 3 miền đầu tiên + CP-S1 A/B health.
3. **CP-L6 19/07 — agenda đã chốt đủ bằng chứng:**
   - **K11a flip về champion** (ưu tiên #1 — champ đúng bị thay 4 lần, net −3 ngày);
   - K15 giữ/kill (chạm mốc báo 5 ngày thua — khuyến nghị GIỮ vì champ cũng thua 5 và 2 win MT đều của challenger);
   - retire gpt-5.5 → grok-4.3 (B2) + B1 hạ effort nếu chưa ký;
   - retire glm-5.1;
   - gemini-3.5-flash swap 2.5-flash (43% vs 29% 7d);
   - CP-R4 housekeeping + CP-4.0 ack.
4. **CN 19/07 02:00**: retrain subprocess lần đầu (khép self-check check-3).
5. **23/07**: CP-S3 tổng kết A/B 105 cặp + trio selector (quyết K11a nếu 19/07 anh muốn chờ).
6. **~24/07**: recheck qwen empty-rate 7 ngày.

**Artifacts:** `web/backend/_v10815_live_review.py` → `_final_checks2.py` (6 probe); docs cập nhật: CHANGELOG V10815 · SSOT V10815 · FOLLOW_UP_TRACKER (2 FU V10814 → LIVE_VERIFIED_DAY1) · PLAYBOOK §5 · AUTOMATION_STATE seq 276.
