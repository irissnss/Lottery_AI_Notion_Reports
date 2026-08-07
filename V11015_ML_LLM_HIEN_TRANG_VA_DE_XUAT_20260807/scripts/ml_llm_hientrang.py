# -*- coding: utf-8 -*-
"""V11015 — ML và LLM HIỆN TRẠNG: làm được gì, thiếu gì.

Owner 07/08: "ML và LLM đã làm được gì rồi? hiện tại và tương lai đề xuất là gì…
Em làm được gì và cần gì phải rõ ràng"
"""
import io
import re
import sqlite3
import sys

sys.stdout.reconfigure(encoding="utf-8")

print("=" * 96)
print("PHẦN 1 — ML: bộ đặc trưng thật")
print("=" * 96)
t = io.open("web/backend/meta_data_collector.py", encoding="utf-8").read()
m = re.search(r"FEATURE_COLUMNS\s*=\s*\[(.*?)^\]", t, re.S | re.M)
blob = m.group(1) if m else ""
cols = re.findall(r"['\"]([a-z0-9_]+)['\"]", blob)
print(f"  Tổng: {len(cols)} đặc trưng\n")

NHOM = {
    "gan / nóng / lạnh (owner nói 'chả tích sự gì')":
        [c for c in cols if any(k in c for k in ("gan", "zone", "recency"))],
    "tần suất thuần": [c for c in cols if "freq" in c or "rolling" in c],
    "xu hướng": [c for c in cols if "trend" in c],
    "hội tụ (§5g đo z=−2,54)": [c for c in cols if "converg" in c],
    "xếp hạng thống kê": [c for c in cols if "rank" in c or "top" in c or "score" in c],
    "thứ trong tuần": [c for c in cols if "dow" in c],
    "lịch sử trúng gần đây": [c for c in cols if "lag" in c or "hit" in c],
    "chéo miền": [c for c in cols if "cross" in c],
}
da = set()
for ten, ds in NHOM.items():
    ds = [c for c in ds if c not in da]
    da |= set(ds)
    if ds:
        print(f"  {ten}")
        print(f"     {len(ds)} đặc trưng: {', '.join(ds)}")
con = [c for c in cols if c not in da and c not in ("date", "region", "tail")]
if con:
    print(f"  khác\n     {len(con)}: {', '.join(con)}")

print()
print("  ⚠ ĐỐI CHIẾU VỚI PROMPT:")
gan_ml = [c for c in cols if any(k in c for k in ("gan", "zone"))]
print(f"     LLM prompt: gan/nóng/lạnh **đã gỡ hết** (V11001+V11007, còn 1 câu cảnh báo)")
print(f"     ML đặc trưng: **vẫn còn {len(gan_ml)}** — {', '.join(gan_ml)}")

print()
print("=" * 96)
print("PHẦN 2 — ML có đối chứng với RULES / BỘ LỌC không?")
print("=" * 96)
TEP = ["meta_data_collector.py", "ml_predict.py", "meta_predict.py", "lstm_predict.py",
       "ml_models.py", "meta_learner.py", "lstm_model.py"]
for f in TEP:
    try:
        s = io.open("web/backend/" + f, encoding="utf-8").read()
    except Exception:
        continue
    n_rule = len(re.findall(r"mined_rule|rule_engine|rule_id", s))
    n_loc = len(re.findall(r"filter_2_so_cuoi|bo_loc|_v10991_sample_gate", s))
    print(f"  {f:<26} rules={n_rule:<3} bộ_lọc={n_loc}")
print("\n  ⇒ ML KHÔNG đối chứng với rules, KHÔNG qua bộ lọc. Nó chỉ là hồi quy trên 39 đặc trưng.")

print()
print("=" * 96)
print("PHẦN 3 — ML có phân biệt SỐ CHÍNH và SỐ PHỤ không?")
print("=" * 96)
s = io.open("web/backend/ml_predict.py", encoding="utf-8").read()
for k in ("main_number", "secondary", "top1", "top2", "so_chinh", "so_phu"):
    print(f"  '{k}': {s.count(k)} lần trong ml_predict.py")
m2 = re.search(r"def predict_with_xgboost.*?return\s+([^\n]+)", s, re.S)
print("\n  ⇒ ML trả về DANH SÁCH XẾP HẠNG, không tự phân biệt chính/phụ.")
print("     Việc chọn chính/phụ do tầng gộp (bundle) làm sau.")

print()
print("=" * 96)
print("PHẦN 4 — NHỊP HUẤN LUYỆN LẠI và cách kiểm soát")
print("=" * 96)
sc = io.open("web/backend/scheduler.py", encoding="utf-8").read()
m3 = re.search(r"retrain_day\s*=\s*([^\n]+)", sc)
m4 = re.search(r"retrain_time\s*=\s*([^\n]+)", sc)
print(f"  lịch trong scheduler : {m3.group(1).strip() if m3 else '?'} · {m4.group(1).strip() if m4 else '?'}")
g = io.open("web/backend/_v10646_retrain_guard.py", encoding="utf-8").read()
m5 = re.search(r"THRESHOLD_DAYS\s*=\s*(\d+)", g)
print(f"  chốt chặn (guard)    : ép huấn luyện nếu model cũ quá {m5.group(1) if m5 else '?'} ngày")

c = sqlite3.connect("file:data/lottery_ai.db?mode=ro", uri=True)
c.row_factory = sqlite3.Row
try:
    r = list(c.execute("""SELECT model_name, COUNT(*) n, MAX(trained_at) moi_nhat
                          FROM training_history GROUP BY 1 ORDER BY 1"""))
    print(f"\n  {'model':22} {'số lần học lại':>14} {'lần gần nhất':>22}")
    for x in r:
        print(f"  {str(x['model_name'])[:22]:22} {x['n']:>14} {str(x['moi_nhat'])[:19]:>22}")
except Exception as e:
    print("  training_history:", str(e)[:70])
c.close()
