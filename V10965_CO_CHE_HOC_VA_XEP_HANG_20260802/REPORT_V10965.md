# REPORT V10965 — Co che hoc va xep hang

## 1. Tom tat mot doan

Dao sau moi co che hoc / tich luy / xep hang / retrain dang chay trong he (chi doc). Viet `docs/CO_CHE_HOC_VA_XEP_HANG.md`. Ket luan: ~18 co che song, ~7 anh huong so cong bo, ~8 chay chi ghi so, ~6+ chet. RULES-FIRST dang hai (list 12,4% ≈ random, pick 35,8%). Optimizer lift am. Lech WR vs BT toi +47pp. Khong sua code (QD-014).

## 2. Owner yeu cau gi

> "Roi cac co che nhu hoc tap tich luy, xep hang, retrain cua cac model LLM va ML thi sao, em da dao sau het co chua? Viet chi tiet cu the tat ca moi thu hien dang code de kiem soat, tong hop that day du."

## 3. Dao boi / phat hien

- Crontab VPS that (26 dong lien quan hoc/shadow).
- DB: training_history 02/08 12/12 OK; mined_rules 105; edge_gate dong; champion bang dung 15/06.
- Lech WR−BT 30d (81 cap): sonnet MN +47.2; deepseek-reasoner MN +44.4; meta MN +40.8.
- Bang chung: `evidence/probe_live.json`, `evidence/probe5_lech.json`.

## 4. Huong xu ly va vi sao chon

Chi viet tai lieu + FU theo doi. Khong sua runtime vi QD-014. Sau 08/08: QD-016/017 + FU-228/229/230.

## 5. Da lam gi

| File | Thay doi |
|---|---|
| `docs/CO_CHE_HOC_VA_XEP_HANG.md` | Tai lieu day du moi |
| CHANGELOG / SSOT / FOLLOW_UP | prepend V10965b + FU-229/230 |
| AUTOMATION_STATE.json | governance_seq +1 |
| Public folder nay | Bao cao + evidence |
| Backup / deploy / hash | Khong ap dung (chi doc) |

## 6. Cong kiem

- Chi doc: khong deploy, khong retrain.
- Crontab + DB doi chieu trong probe.
- Report gate se chay sau push.

## 7. Vuong vap

- Agent song song da viet ban rut `CAC_CO_CHE_*` + stub V10965; ban nay bo sung day du dung ten owner yeu cau.
- Cot predictions la `ai_model` (khong phai `model`) — probe dau bi loi schema.
- Champion: cron song / bang dung — de to hong neu chi nhin log.

## 8. Go ve

Khong doi runtime. Xoa tai lieu: git revert file docs + folder public. Khong can restore VPS.

## 9. Theo doi tiep

- FU-222 / QD-016 RULES-FIRST (sau 08/08)
- FU-228 do tung co che
- FU-229 champion bang dung
- FU-230 dong bo thuoc WR vs BT
