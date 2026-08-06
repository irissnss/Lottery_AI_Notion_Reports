# -*- coding: utf-8 -*-
"""PL19c B4 — QUÉT LẠI TOÀN BỘ: mined_rules có đi vào đường TRAIN không?

PL19b kết luận "rules vào ML = 0" nhưng evidence ghi ml_train.py / meta_train.py
"không đọc được". Nay xác định: hai tệp đó KHÔNG TỒN TẠI. Phải tìm đường train thật.

Truy vấn VIẾT MỚI, không chạy lại script PL19b.
"""
import glob
import io
import os
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")

TU = re.compile(r"mined_rule|MINED_RULE|MinedRule|rule_engine|rule_id|BOOST_TABLE", re.I)

print("=" * 96)
print("B4-a — HAI TỆP PL19b BÁO 'KHÔNG ĐỌC ĐƯỢC': tồn tại không?")
print("=" * 96)
for f in ("web/backend/ml_train.py", "web/backend/meta_train.py"):
    print(f"  {f:<34} {'CÓ' if os.path.exists(f) else '❌ KHÔNG TỒN TẠI'}")
print("\n  ⇒ 'không đọc được' = KHÔNG CÓ TỆP, không phải thiếu quyền.")
print("     PL19b dùng danh sách tệp ĐOÁN, không phải danh sách tệp THẬT.")

print()
print("=" * 96)
print("B4-b — ĐƯỜNG TRAIN THẬT: tệp nào chứa hàm huấn luyện?")
print("=" * 96)
train = []
for p in sorted(glob.glob("web/backend/*.py")):
    try:
        s = io.open(p, encoding="utf-8", errors="replace").read()
    except Exception:
        continue
    if re.search(r"def .*train|\.fit\(|XGBClassifier|RandomForestClassifier|Sequential\(|"
                 r"model\.fit|joblib\.dump", s):
        n = len(TU.findall(s))
        train.append((os.path.basename(p), len(s), n))
for f, sz, n in sorted(train, key=lambda x: -x[2]):
    dau = "  ← CÓ RULES" if n else ""
    print(f"  {f:<40} {sz:>8,} byte   rules={n:>3}{dau}")

print()
print("=" * 96)
print("B4-c — QUÉT TOÀN web/backend: tệp nào chạm mined_rules, phân theo VAI TRÒ")
print("=" * 96)
VAI = {
    "PRODUCTION — sinh số": ["gpt_analyzer.py", "ml_predict.py", "meta_predict.py",
                              "lstm_predict.py", "scheduler.py", "main.py",
                              "meta_data_collector.py", "rule_engine.py",
                              "combo_super.py", "cross_region.py"],
    "PRODUCTION — huấn luyện": ["_retrain_all.py", "run_full_training.py",
                                 "run_backfill_training.py", "_v10646_retrain_guard.py",
                                 "weekly_rule_miner.py", "_seed_rules.py",
                                 "mined_rule_eval.py"],
}
da = set()
for ten, tep in VAI.items():
    print(f"\n  ── {ten} ──")
    for f in tep:
        p = "web/backend/" + f
        da.add(f)
        if not os.path.exists(p):
            print(f"    {f:<32} ❌ không tồn tại")
            continue
        s = io.open(p, encoding="utf-8", errors="replace").read()
        n = len(TU.findall(s))
        print(f"    {f:<32} {n:>4} lần" + ("   ← CÓ" if n else "   ← KHÔNG"))

print()
print("=" * 96)
print("B4-d — CÓ TỆP PRODUCTION NÀO KHÁC chạm rules mà PL19b bỏ sót?")
print("=" * 96)
bo_sot = []
for p in sorted(glob.glob("web/backend/*.py")):
    f = os.path.basename(p)
    if f in da or f.startswith("_v10") or f.startswith("_v11") or f.startswith("_test")\
            or f.startswith("_materialize"):
        continue
    try:
        s = io.open(p, encoding="utf-8", errors="replace").read()
    except Exception:
        continue
    n = len(TU.findall(s))
    if n:
        bo_sot.append((f, n))
for f, n in sorted(bo_sot, key=lambda x: -x[1])[:18]:
    print(f"    {f:<40} {n:>4} lần")
print(f"\n    tổng {len(bo_sot)} tệp production khác có chạm rules")

print()
print("=" * 96)
print("B4-e — PHÁN XỬ: đường TRAIN có đọc mined_rules không?")
print("=" * 96)
co = [f for f, _, n in train if n]
if co:
    print(f"  ⚠ CÓ {len(co)} tệp train chạm rules: {', '.join(co)}")
    print("  ⇒ PHẢI đính chính Q15 theo §60.")
else:
    print("  ✓ KHÔNG tệp train nào chạm mined_rules.")
    print("  ⇒ Kết luận Q15 GIỮ NGUYÊN, nhưng LÝ DO trong evidence phải sửa:")
    print("     'ml_train.py không đọc được' → 'ml_train.py KHÔNG TỒN TẠI;")
    print("      đường train thật là các tệp liệt kê ở B4-b'")
