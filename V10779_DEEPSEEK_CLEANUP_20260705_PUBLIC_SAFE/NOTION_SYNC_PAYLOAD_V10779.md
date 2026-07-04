# V10779 — PHASE B: R1 NAMEFIX + DEEPSEEK-CLEANUP + OPENROUTER-ADD (plan-only A2)

- Ngày: 2026-07-05 (04:00–05:30 VN)
- Loại: PHASE B RUNTIME (triển khai sau V10778 Phase A)
- Plan ID: PLAN-20260705-V10777-R1SWAP-NAMEFIX-RETIRE
- Backup: `backups/v10779_pre/` (DB + 24 file .pre)
- Hash guard VPS (PRE=POST): predictions 9289 bc7f0260… | final_bundles 381 0f70d14a… | lottery_results 15010 2076e8f7… | model_daily_eval 9132 cbd1f568…

## 1. QUYẾT ĐỊNH OWNER (Phase B prompt)

| Gate | Quyết định |
|---|---|
| R2 | **R2-D**: thay slot v4-flash bằng **DeepSeek V4 Pro THẬT** (`deepseek-v4-pro-real`, API id `deepseek-v4-pro`, 1.6T, thinking ON, max output 393216) |
| PL-1 | **Duyệt migrate ngay**: alias `deepseek-reasoner` → explicit `deepseek-v4-flash` + thinking; giữ model_id nội bộ |
| PL-2 | Retire lane shadow `deepseek-v4-pro` cũ (P&L trùng official V4-Flash-thinking); id mới không nối P&L cũ |
| CP-66.9 | **Option A**: giữ lock tuần 29/06 hết 05/07; pool MN = MN_HYBRID_V1 từ 06/07; V66/V67 giữ MT/MB |
| R4 | Retire 4 shadow âm (qwen3-coder, gemini-3-flash, gemini-3.1-pro, qwen3.6-plus) |
| A2 | OpenRouter plan-only — **CHƯA đăng ký model**, chờ owner chốt |

## 2. BẢNG NGHIỆM THU B1–B7

| ID | Nội dung | Trạng thái | Bằng chứng |
|---|---|---|---|
| B1 | Backup + hash PRE | ✅ | `backups/v10779_pre/` + hash VPS 04:05 |
| B2 | R1 namefix 12 vị trí | ✅ | grep live "DeepSeek R1" = 0 |
| B3 | PL-1 alias migrate | ✅ | 3 call: alias + explicit cùng fp `fp_8b330d02d0`, response_model=deepseek-v4-flash |
| B4 | R2-D swap + smoke | ✅ | V4 Pro fp `fp_9954b31ca7` KHÁC Flash; max_tokens range [1,393216] |
| B5 | CP-66.9 Option A | ✅ | main.py pool MN_HYBRID_V1; scheduler skip MN từ 06/07; roadmap CLOSED |
| B6 | Retire 6 shadow | ✅ | registry self-test: SHADOW_AUTO=8, RETIRED=6 |
| B7 | UI RETIRED pill | ✅ | monitoring.html pill cam + note nhóm ĐÃ NGHỈ |

## 3. MA TRẬN TƯƠNG THÍCH M1–M8

| ID | Kiểm tra | Kết quả |
|---|---|---|
| M1 | /du-doan 15/15 output-eligible | PASS (15/15) |
| M2 | /choi lock tuần 29/06 | PASS (không đổi hết tuần 05/07) |
| M3 | Hash 4 bảng official | PASS IDENTICAL |
| M4 | Lane test C-16 pool loại RETIRED | PASS (_materialize_du_doan_test_model_budget fix) |
| M5 | V10752 MT cap | PASS (không đụng) |
| M6 | V10766/V10767/V10770 mốc | PASS (không đụng) |
| M7 | Shadow lanes checkpoint 14/07 | PASS (RF-MB, wplur_rf2_ml, ai_plurality2, MN BT chạy tiếp) |
| M8 | MODEL_LINEAGE api_route_change | PASS (database.py annotation) |

## 4. A2 OPENROUTER (PLAN-ONLY — CHỜ OWNER)

**A2-1 Key:** OPENROUTER_API_KEY + 20 per-model key có trên VPS `/root/Lottery_AI_Test/.env`

**A2-2 Smoke kimi-k2-thinking (1 call):**
- status=OK latency=2.1s
- model=moonshotai/kimi-k2-thinking-20251106
- reasoning 309 chars, JSON parse OK
- giá $0.60/$2.50 per 1M, ctx 262K, max_out 100,352

**A2-3 Ứng viên Qwen thinking (live OpenRouter /models 05/07):**

| Model | $in/$out per 1M | Context | Max out | Ghi chú |
|---|---|---|---|---|
| qwen/qwen3.7-max | $1.25 / $3.75 | 1M | 65K | flagship 05/2026 |
| qwen/qwen3.7-plus | $0.32 / $1.28 | 1M | 65K | mới nhất 06/2026 |
| qwen/qwen3-max-thinking | $0.78 / $3.90 | 262K | 32K | đã có trong hệ (+7.1M MN) |

**A2-4:** CHƯA đăng ký — chờ owner chốt 0–2 model.

## 5. SỐ MODEL SAU V10779

- SHADOW_AUTO: 13 → **8** (glm-5.1, grok-4.20, kimi-k2.5, qwen3-max-thinking, gpt-oss-120b, gpt-5.5, **deepseek-v4-pro-real**, gemma-4-31b)
- OUTPUT_ELIGIBLE: **15/15** (không đổi)
- RETIRED mới: 6 (reversible, giữ 100% history)

## 6. ROLLBACK

Copy file `.pre` từ `backups/v10779_pre/` đè lại + `systemctl restart lottery`. Retire reversible = flip status trong model_registry.py.

## 7. CHECKPOINT TIẾP THEO

- **06/07**: verify first_run row `deepseek-v4-pro-real` (3 miền × shadow lane)
- **OWNER**: chốt A2 OpenRouter register
- **14/07**: checkpoint shadow lanes (RF-MB, wplur_rf2_ml, ai_plurality2, MN BT) — không bị ảnh hưởng bởi V10779
