# -*- coding: utf-8 -*-
"""FU-421/GĐ-3 — phép C ĐO LẠI bằng TỈ LỆ THẮNG THẬT.

Bản đầu dùng giả định «mọi model cùng win_rate» vì đọc nhầm `model_rates = {}` ở main.py:7839
là giá trị cuối. SAI — đó chỉ là khởi tạo; nó được nạp thật ở `:7843` từ
`combo_super._get_dynamic_win_rates(region)` (trộn 7 ngày ×2 + 30 ngày).

Con số «107/111 hoà đúng biên hạng 0/1» của bản đầu là TRƯỜNG HỢP XẤU NHẤT giả định, KHÔNG phải
số production. Bản này đo số thật.
"""
import json
import os
import sqlite3
import sys

sys.stdout.reconfigure(encoding="utf-8")
sys.path.insert(0, os.path.join("web", "backend"))

ML_ENSEMBLE = ["meta-learning", "lstm"]
ML_COMBO = ["meta-learning", "lstm", "xgboost", "random-forest"]


def wr_that(mien: str) -> dict:
    from combo_super import _get_dynamic_win_rates
    try:
        return {k: float(v) for k, v in _get_dynamic_win_rates(mien).items()}
    except Exception as e:
        print(f"  ⚠ không lấy được WR cho {mien}: {e}")
        return {}


def dung_diem(nums_theo_model: dict, wr: dict) -> dict:
    diem = {}
    for m, nums in nums_theo_model.items():
        w = wr.get(m, 50) / 100.0
        for r, n in enumerate(nums):
            diem[n] = diem.get(n, 0) + w * (1.0 / (1 + r * 0.15))
    return diem


con = sqlite3.connect("file:data/lottery_ai.db?mode=ro", uri=True)
con.row_factory = sqlite3.Row
rows = con.execute("""
    SELECT date, target_region, ai_model, main_numbers FROM predictions
    WHERE date >= date('now','-60 day') AND run_source='auto_daily'
      AND ai_model IN ('meta-learning','lstm','xgboost','random-forest')
""").fetchall()
con.close()

theo = {}
for r in rows:
    try:
        nums = json.loads(r["main_numbers"] or "[]")
    except Exception:
        nums = []
    if nums:
        theo.setdefault((r["date"], r["target_region"]), {})[r["ai_model"]] = nums

WR = {m: wr_that(m) for m in ("MN", "MT", "MB")}
print("  TỈ LỆ THẮNG THẬT đang dùng (từ `_get_dynamic_win_rates`):")
for m, d in WR.items():
    x = {k: round(v, 2) for k, v in d.items() if k in ML_COMBO}
    print(f"    {m}: {x if x else '(rỗng ⇒ mọi model rơi về mặc định 50)'}")
print()

print("=" * 92)
for ten, ds in (("Smart Ensemble (:7894)  2 model", ML_ENSEMBLE),
                ("Smart ML / Combo (:8101, :8354)  4 model", ML_COMBO)):
    xet = hoa = b01 = b23 = 0
    for (ngay, mien), tm in sorted(theo.items()):
        d = {m: tm[m] for m in ds if m in tm}
        if len(d) < 2:
            continue
        xet += 1
        s = sorted(dung_diem(d, WR.get(mien, {})).items(), key=lambda x: -x[1])
        v = [x[1] for x in s]
        if len(set(v)) != len(v):
            hoa += 1
        if len(v) > 1 and v[0] == v[1]:
            b01 += 1
        if len(v) > 3 and v[2] == v[3]:
            b23 += 1
    print(f"  {ten}")
    print(f"     xét {xet} ngày-miền · có hoà ở đâu đó {hoa} ({100*hoa//max(xet,1)}%) "
          f"· hoà ĐÚNG BIÊN hạng 0/1: {b01} · biên hạng 2/3: {b23}")
print("=" * 92)
