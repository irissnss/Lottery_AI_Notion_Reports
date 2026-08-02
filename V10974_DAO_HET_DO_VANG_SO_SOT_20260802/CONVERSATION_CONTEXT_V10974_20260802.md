# CONVERSATION_CONTEXT_V10974_20260802

## Owner (nguyên văn)

> *"đỏ vàng gì đào hết, còn thiếu thông tin nào anh đã từng chia sẻ , từng nhắc từng đóng góp trong trò chuyện thì xem lại đào luôn"*

Deliverable: V10974 folder public A55; đào hết 🔴🟡 V10973; rà transcript; push; gate PASS. QD-014 freeze — không đổi 15 model / combo filter / override / `/du-doan` / final_bundles writer.

## Agent làm gì

1. `_v10920_session_start.py` — 0 CP quá hạn · 83 FU treo.
2. Đọc V10973 bảng đối chiếu (T01–T30).
3. `python web/_sync_live_forensic_inputs.py` → `artifacts/live_sync/20260802_224532`.
4. Đào local DB + VPS read-only:
   - Parse `source_predictions_json` → exclusion reasons MT/MB.
   - FU-184 ballot checklist 01–02/08.
   - FU-189 experiment names + cron.
   - Edge gate remeasure; LSTM key trên VPS `combo_super.py`; deploy windows trong `governance_guard.py`; frontend hashes; gemini-3.5 hôm nay; MT monthly FU-210.
5. Search transcript Aug 1–2 user messages → sót T31–T34.
6. Cập nhật FU-184/189/242/225/… + CHANGELOG/SSOT + báo cáo public.

## Vấp

- Sai cột `analysis_json` trên VPS remote script lần 1 → chuyển `source_predictions_json`.
- Query settings quá rộng suýt ghi API key vào evidence → REDACT ngay.
- PowerShell phá `python -c` nhiều ngoặc → chuyển sang file `.py`.

## Kết luận nhanh gửi parent

- Còn đỏ “chưa đào”? **Không.**
- Còn vàng “chưa đào”? **Không** — còn vàng = chờ hành động/freeze, đã có baseline số.
- Root cause MT13/MB14: bt_gate + MT_top13 cap (không timeout).
- Sót transcript thêm: gemini-3.5 (FU-203), live-may (V10970), combo filter, 240G handoff.
