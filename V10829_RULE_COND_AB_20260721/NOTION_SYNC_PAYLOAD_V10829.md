# V10829 — Catalog điều kiện RULES (pipeline A→B)

**Ngày:** 2026-07-21 00:22→00:3x  
**Loại:** Shadow measurement (§52) — KHÔNG đụng official/prompt  
**GitHub đầy đủ:** https://github.com/irissnss/Lottery_AI_Notion_Reports/tree/main/V10829_RULE_COND_AB_20260721

## Kết quả chính
- Catalog H-A* / H-B* chạy backtest ~180 ngày + 2 nửa + placebo.
- RAW precision ≈ 38.2% (đối chứng bắt buộc).
- **A finalists:** H-A1a · H-A4b · H-A4a (placebo OK).
- **B finalists:** H-A4a+H-B2a · RAW+H-B2a · H-A4a+H-B1a.
- Materialize chính: **H-A4a ∧ H-B2a**.
- Panel 📐 + API `/api/admin/rule-cond` + bảng `v10829_rule_cond_daily` + cron 21:00.
- Forward từ **21/07**; **28/07 chỉ đọc sơ bộ**; wire sau ≥14–21 ngày nếu vượt ngưỡng (+5pp).

## Quyết định owner
- Không vá phản xạ thêm giữa cửa sổ đo.
- **V10828 hygiene tạm giữ nguyên** (herd≥3 + AE vote-gate) — không mở rộng; có thể thay/thu hẹp sau kết luận điều kiện thật.

## Hash 4 bảng official
IDENTICAL: `4b303e45` / `23843b5a` / `7ce7a13f` / `07b4fbc5`
