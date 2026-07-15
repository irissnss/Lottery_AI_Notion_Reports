# BÁO CÁO V10805 — REPLAY NGƯỢC VỤ 51/19: MODEL NÀO RA SỐ, PROMPT NÀO ĐẨY SỐ, SAI CHỖ NÀO, ĐÚNG CHỖ NÀO

- Ngày: 2026-07-15 (~21:53 → 23:0x, sau V10804 cùng ngày)
- Trigger owner 21:53: "51/19 anh muốn biết MODEL NÀO dự ra số đó… thử nghiệm ngược với mốc, với model, với điều kiện tại thời điểm đó — dùng lại có ra số đó không — để xác định mình sai chỗ nào, đúng chỗ nào, lỗ hổng là gì. ML thì mốc dữ liệu có chọn sai mốc D không, model AI thì prompt nào ảnh hưởng đến output. Tra ngược để tìm chỗ sai và xử lý đúng lại."
- Forensic input: sync 21:56 (`artifacts/live_sync/20260715_215628/manifest.json`), DB + prediction_trace.jsonl (cặp đôi).

## 1. DANH SÁCH MODEL CHÍNH XÁC (không phải "khoảng 16 model" — đích danh)

**51 @ MB 14/07 (BT official = 51, TRƯỢT) — 16 model, 17:31-17:48:**

| Model | vị trí 51 | giờ | nguồn |
|---|---|---|---|
| claude-opus-4-6 | pos1 [51,36] | 17:31 | ai_chain |
| claude-sonnet-4-6 | pos1 [51,32] | 17:31 | ai_chain |
| gemini-2.5-flash | pos1 [51,54] | 17:31 | ai_chain |
| gpt-5-mini | pos2 [36,51] | 17:31 | ai_chain |
| gemini-2.5-pro | pos1 [51,36] | 17:32 | ai_chain |
| deepseek-reasoner | pos2 [36,51] | 17:32 | ai_chain |
| gpt-5.4 | pos2 [32,51] | 17:32 | ai_chain |
| combo-super | pos1 [51,36] | 17:34 | ai_chain (ML-echo) |
| grok-4.20-multi-agent | pos1 [51,36] | 17:35 | shadow_auto_eval |
| deepseek-v4-pro-real | pos1 [51,32] | 17:47 | shadow_auto_eval |
| gemini-3.5-flash · glm-5.1 · gpt-5.5 · qwen3.7-max | pos1 [51,36] | 17:48 | shadow_auto_eval |
| glm-5.2 | pos1 [51,32] | 17:48 | shadow_auto_eval |
| kimi-k2.5 | pos2 [36,51] | 17:48 | shadow_auto_eval |

**19 @ MT 15/07 (BT official = 19, TRƯỢT) — 12 model 16:36-16:52:** claude-sonnet-4-6, combo-super, deepseek-reasoner, deepseek-v4-pro-real, gemini-2.5-flash, gemini-2.5-pro, glm-5.1, glm-5.2, gpt-5-mini, gpt-5.4, gpt-5.5, grok-4.20 (11 pos1 + gemini-flash pos2).
**19 @ MN 15/07 — 4 model 04:16-04:32:** gemini-2.5-flash, gpt-5-mini, gpt-5.4, gpt-oss-120b.
**19 @ MB 15/07: KHÔNG model nào** — mà ĐB MB = 19 (pattern H3/H5 của V10804).

**PURE-ML KHÔNG DÍNH cả 2 vụ:** lstm, xgboost, random-forest, meta-learning, smart-ensemble, smart-ml, combo-no-token KHÔNG ra 51 lẫn 19 — nhiều con còn trúng (MB 14/07: combo-no-token 57✓, lstm 90✓, meta 57✓, rf 57✓; MT 15/07: combo-no-token 21✓, rf 21✓, xgb 21✓, smart 42✓). **combo-super là ngoại lệ vì nó KHÔNG phải ML độc lập**: input của nó chứa picks AI (trace: `ai_models: {claude-sonnet: [51,36], claude-opus: [51,36]}`), top1 của nó trùng top2 của ≥1 AI **65-77% số ngày** (MN 77%, MT 65%, MB 77%) = bộ khuếch đại herd đội lốt "đơn model".

## 2. PROMPT NÀO ĐẨY RA SỐ ĐÓ — RULE ENGINE LÀ NGUỒN PHÁT (root cause)

Khối MINED RULES trong prompt lấy từ `mined_rules` + `extract_rule_candidates_v2`, cơ chế: **emit ĐUÔI CỦA GIẢI D-1 ĐÀI MIỀN KHÁC làm candidate hôm nay** (thiết kế, không phải bug):

- **14/07 MB:** rule "Đồng Tháp G5+G7 (MN D-1)" emit **[32, 51]** + rule "Đồng Tháp G2+G5" emit **[97, 51]** → 51 = **CONV×2, boost CAO NHẤT trong prompt**, kèm nhãn "12W=92% + FRESH + CONV×2". (51 nằm G5 Đồng Tháp ngày 13/07 — chính là lần "51 nổ MN" owner thấy.)
- **15/07 MT:** rule "Vũng Tàu GĐB+G1 (MN D-1)" emit **[19, 61]** kèm nhãn "12W=75%, boost 0.121"; 19 đồng thời nằm trong khối định lượng dùng chung (freq 3-4 lần vì 19 nổ MN 14/07 ở 2 giải) → "hội tụ nhiều nguồn" giả.
- Reasoning lưu trong trace của từng model đều viện dẫn đúng các nhãn này (claude-sonnet: "51: Rule Tails CONV×2 boost=0.361 cao nhất, Đồng Tháp G5+G7 ACTIVE 92% 12W"; deepseek-v4: "19: Rule MN Vũng Tàu GĐB+G1 12W 75% + cross-region support 3/4 doctrine").

## 3. REPLAY THẬT — "dùng lại có ra số đó không?" → **CÓ: 5/6**

Chạy `analyze_and_predict` (đúng code production, prompt + context pack + provider), trên VPS bằng key production, **không ghi DB, trace no-op**:

| Model | MB @ 14/07 (đích 51) | MT @ 15/07 (đích 19) |
|---|---|---|
| gemini-2.5-flash | lịch sử [51,54] → replay **[51,32] ◄ RA LẠI** | lịch sử [61,19] → replay **[19,32] ◄ RA LẠI** |
| gpt-5-mini | lịch sử [36,51] → replay **[51,97] ◄ RA LẠI** (kb: "Đồng Tháp G5+G7 hỗ trợ 51 — boost cao nhất") | lịch sử [19,61] → replay **[19,98] ◄ RA LẠI** |
| deepseek-reasoner | lịch sử [36,51] → replay [66,62] (thoát — reasoning dài tự phản biện) | lịch sử [19,39] → replay **[19,68] ◄ RA LẠI** (kb: "rule Vũng Tàu GĐB+G1") |

→ **Output là DETERMINISTIC theo prompt** — không phải model "tự nhiên thích" 51/19. Đổi model không đổi prompt thì số vẫn vậy. Caveat: bảng rule đã trôi vài ngày so thời điểm gốc (boost 51: 0.265 nay vs 0.361 lúc đó — vẫn rank 1 CONV×2), coi là replay tương-đương-điều-kiện.

## 4. LỖ HỔNG TÌM RA (sai chỗ nào)

**(i) Nhãn % gây hiểu nhầm hệ thống — lỗ hổng chính:** "12W=92%" là **hit_ANY BAO-LÔ của cụm k đuôi** — rule 2 đuôi có baseline any-of-2 ≈ **42% (MB) / 51% (MT)**, và 92% chỉ là 11/12 trên **12 mẫu weekly**. Model đọc nhãn như xác suất per-số → 12-16 model dồn BT vào 1 số. Per-tail THẬT toàn lịch sử: Đồng Tháp G5+G7→MB **33.3%** (14/42, baseline 23.7%, +9.6pp); Vũng Tàu GĐB+G1→MT **44.1%** (45/102, baseline 29.8%, +14.3pp) → rule CÓ tín hiệu nhẹ nhưng nhãn thổi phồng 2-3 lần. Ngày 14/07 cả 2 rule ĐT trượt trắng (emit [32,51],[97,51] — hit 0).

**(ii) Rule adoption 120d — sai/đúng theo miền (bảng giờ LIVE trong /monitoring):**

| Miền | model top1 ∈ rule | ∈ CONV×2 | model NGOÀI rule | baseline | BT official ∈ rule | BT ngoài |
|---|---|---|---|---|---|---|
| MN | 47.7% (n=940) | **38.8% — DƯỚI baseline** | 41.8% | 42.9% | 44.4% | 44.7% |
| MT | 35.7% (n=840) | 31.1% | 36.0% | 35.2% | **28.6%** | **40.0%** |
| MB | 30.0% (n=978) | **50.6% (n=249)** | **17.7% — hố chính** | 23.8% | 27.6% | 15.2% |

- **MB sai ở phần TỰ-NGHĨ:** ngoài-rule 17.7% dưới baseline −6.1pp (lý do kiểu "KB Quảng Ninh top tails/cụm/gương") — rule MB thật ra TỐT (CONV×2 50.6%).
- **MT sai ở chỗ ƯU TIÊN RULE:** rule không cộng gì (BT theo-rule 28.6% < ngoài-rule 40.0%) mà mandate §10A vẫn ép "source-prize first" → vụ 19 chính là hệ quả.
- **MN: CONV×2 là bẫy** (38.8% < baseline 42.9%) — hội tụ nhiều rule tại MN không có nghĩa.
- Day-level "ngày nào rule cũng trúng gì đó" (62-95%) = ảo giác k-đuôi; per-tail chỉ 39-43%.

**(iii) combo-super:** AI-echo (copy 65-77%) được đếm như "đơn model" trong phiếu → khuếch đại herd.

**(iv) Mốc D của ML — KHÔNG sai trong 2 vụ:** MB ML re-run 17:30:45 same-day (đúng kết luận A/B V10801 — hoà, giữ); MT/MN 04:00-04:16 D-1 (MT meta+xgb same-day đang đo shadow V10801, chưa đổi). Pure-ML không ra 51/19 nên 2 vụ này không dính lỗi mốc.

## 5. XỬ LÝ

**Trong phiên (zero regime change):** view `/api/admin/chase-bias` thêm khối `rule_adoption` + bảng **"📜 RULE ADOPTION"** trong panel chase-bias /monitoring (đọc live `mined_rule_effectiveness`+`predictions`+`final_bundles`, không bảng mới, không cron mới). Deploy 2 file, restart `lottery.service`, smoke 200/401, journal sạch, **hash 4 bảng official pre=post IDENTICAL** (predictions 10122/3a18c24b · final_bundles 414/0e68ae9c · lottery_results 15081/1a1820b1 · model_daily_eval 9986/aaa91dc6). Backup `backups/v10805_pre/` + `/root/backups/v10805_pre/`.

**Đề xuất CP-L6 (cần chữ ký owner — regime change prompt/selector):**
1. Nhãn rule trong prompt → per-tail % + n (hết thổi phồng).
2. Miền-hoá mandate §10A: hạ ưu tiên rule tại MT (không có edge tại MT).
3. Guard nhánh ngoài-rule MB (17.7% là hố nặng nhất hệ thống).
4. Khối CHỈ SỐ ĐỊNH LƯỢNG per-miền (V10804, FU-V10804-QUANT-BLOCK-SHARED).
5. combo-super đánh dấu AI-echo khi đếm phiếu total.
6. Thay API đợt cắt: gemini-2.5-flash + gpt-5-mini (replay ra lại số chase 100% cả 2 vụ, đáy bảng MT 29%/36%).

## 6. LỊCH VERIFY

| Mốc | Việc |
|---|---|
| 16/07 | Bảng 📜 RULE ADOPTION render /monitoring; cùng đợt V10804 (budget_catchup MB ~17:40, header MT 3 đài) |
| ~14/08 | Đọc ngưỡng rule-adoption (nhánh lệch ≥10pp bền 2 nửa → chốt CP-L6 mục b/c) |
| CP-L6 | Trình 6 đề xuất trên + danh sách thay API |

Probe read-only: `_v10805_reverse_trace.py`, `_v10805_rule_forensic.py`, `_v10805_adoption_outcome.py`, `_v10805_pertail_rules.py`, `_v10805_ml_and_groups.py`, `_v10805_ai_replay.py`, `_v10805_run_replay_vps.py`.
