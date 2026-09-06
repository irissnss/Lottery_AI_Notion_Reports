# -*- coding: utf-8 -*-
"""V11169 CONG3 -- kiem tra CHI DOC: cot notes cua 91 bundle backfill co con nguyen
'Phase 1.5 backfill' khong (neu con thi dung lam nhan san co, khong can ALTER TABLE)."""
import sqlite3, json, io, sys
sys.stdout.reconfigure(encoding="utf-8")
DB = "file:/root/Lottery_AI_Test/data/lottery_ai.db?mode=ro"
c = sqlite3.connect(DB, uri=True)
c.row_factory = sqlite3.Row

IDS = [4,2,3,7,5,6,10,8,9,13,11,12,16,14,15,19,17,18,22,20,21,25,23,24,28,26,27,31,29,30,
       34,32,33,37,35,36,40,38,39,43,41,42,46,44,45,49,47,48,52,50,51,55,53,54,58,56,57,
       61,59,60,64,62,63,67,65,66,70,68,69,73,71,72,76,74,75,79,77,78,82,80,81,85,83,84,
       88,86,87,91,89,90,93]
print("so id kiem tra:", len(IDS), "| unique:", len(set(IDS)))
q = "SELECT id,date,region,notes,generation_method,verified_at,bundle_version,status FROM final_bundles WHERE id IN (%s)" % ",".join("?" * len(IDS))
rows = c.execute(q, IDS).fetchall()
print("tim thay:", len(rows), "dong")
notes_count = {}
gm_count = {}
for r in rows:
    notes_count[r["notes"]] = notes_count.get(r["notes"], 0) + 1
    gm_count[r["generation_method"]] = gm_count.get(r["generation_method"], 0) + 1
print("PHAN BO notes:", json.dumps(notes_count, ensure_ascii=False))
print("PHAN BO generation_method:", json.dumps(gm_count, ensure_ascii=False))

# doi chieu nguoc: co bundle nao KHONG trong 91 id nhung notes = 'Phase 1.5 backfill' khong?
# (kiem tra marker co DAC THU rieng cho 91 dong, khong dinh nham dong khac)
all_notes = c.execute("SELECT id,notes FROM final_bundles").fetchall()
mang_nhan = [r["id"] for r in all_notes if r["notes"] and "backfill" in (r["notes"] or "").lower()]
print("TONG so id trong CA BANG co notes chua 'backfill' (khong phan biet hoa thuong):", len(mang_nhan))
print("co dung bang 91 khong:", set(mang_nhan) == set(IDS), "| thua:",
      sorted(set(mang_nhan) - set(IDS))[:20], "| thieu:", sorted(set(IDS) - set(mang_nhan))[:20])

# kiem verified_at + status cua toan bo 91 -- dam bao KHONG bi force-overwrite mat notes
vac = {}
for r in rows:
    vac[(r["status"], bool(r["verified_at"]))] = vac.get((r["status"], bool(r["verified_at"])), 0) + 1
print("PHAN BO (status, co_verified_at):", vac)
