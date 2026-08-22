# -*- coding: utf-8 -*-
"""FU-421/GĐ-3 — ĐO ba chỗ `sorted(number_scores.items(), key=lambda x: -x[1])`.

main.py:7894 (Smart Ensemble) · :8101 (Smart ML) · :8354 (Combo No Token)

CÁCH ĐO theo đúng tiền lệ FU-416:
  A. THỬ ĐỐI CHỨNG — chứng minh DỤNG CỤ ĐO có tác dụng: một `set` thật phải cho thứ tự KHÁC
     nhau qua các `PYTHONHASHSEED`. Không có bước này thì «mọi seed giống nhau» có thể chỉ là
     dụng cụ hỏng, không phải mã an toàn (RM-15 tinh thần: phải chứng minh phép đo biết ĐỎ).
  B. Dựng lại ĐÚNG cách `number_scores` được xây trong mã production, rồi so thứ tự qua nhiều
     seed.
  C. TRƯỜNG HỢP XẤU NHẤT: cho MỌI model cùng win_rate ⇒ tối đa hoá số cặp hoà, rồi đếm xem hoà
     có rơi vào BIÊN QUYẾT ĐỊNH không (rank 0/1 và biên top-N).

CHỈ ĐO — không sửa gì.
"""
import hashlib
import json
import os
import sqlite3
import subprocess
import sys

sys.stdout.reconfigure(encoding="utf-8")

DB = "data/lottery_ai.db"
# Đúng thứ tự viết cứng trong main.py — chép nguyên, không sắp lại
ML_ENSEMBLE = ["meta-learning", "lstm"]                       # :7804-7807
ML_COMBO = ["meta-learning", "lstm", "xgboost", "random-forest"]  # :8245-8250


def dung_diem(nums_theo_model: dict, wr: dict) -> dict:
    """Chép ĐÚNG phép tính ở main.py:7860-7863."""
    diem = {}
    for model_name, nums in nums_theo_model.items():
        weight = wr.get(model_name, 50) / 100.0
        for rank, num in enumerate(nums):
            diem[num] = diem.get(num, 0) + weight * (1.0 / (1 + rank * 0.15))
    return diem


def _lay_du_lieu(n_ngay: int = 60) -> list:
    con = sqlite3.connect(f"file:{DB}?mode=ro", uri=True)
    con.row_factory = sqlite3.Row
    try:
        rows = con.execute("""
            SELECT date, target_region, ai_model, main_numbers
            FROM predictions
            WHERE date >= date('now', ?) AND run_source='auto_daily'
              AND ai_model IN ('meta-learning','lstm','xgboost','random-forest')
            ORDER BY date, target_region
        """, (f"-{n_ngay} day",)).fetchall()
    finally:
        con.close()
    theo_ngay = {}
    for r in rows:
        try:
            nums = json.loads(r["main_numbers"] or "[]")
        except Exception:
            nums = []
        if nums:
            theo_ngay.setdefault((r["date"], r["target_region"]), {})[r["ai_model"]] = nums
    return sorted(theo_ngay.items())


def phepA_doi_chung() -> bool:
    """Dụng cụ đo có tác dụng không — một `set` thật phải đổi thứ tự theo seed."""
    ma = ("import os,sys\n"
          "s={'12','34','56','78','90','11','22','33'}\n"
          "sys.stdout.write(','.join(sorted(s, key=lambda x: 0)))\n")
    ra = set()
    for seed in ("1", "2", "987"):
        env = dict(os.environ, PYTHONHASHSEED=seed)
        p = subprocess.run([sys.executable, "-c", ma], capture_output=True, env=env)
        ra.add(p.stdout.decode().strip())
    print(f"  A. THỬ ĐỐI CHỨNG — `set` thật qua 3 seed cho {len(ra)} thứ tự khác nhau "
          f"⇒ dụng cụ đo {'CÓ tác dụng' if len(ra) > 1 else 'HỎNG'}")
    return len(ra) > 1


def phepB_ba_cho(du_lieu: list) -> None:
    """Thứ tự có đổi theo seed không, trên dữ liệu THẬT."""
    ma_tpl = (
        "import sys, json\n"
        "d = json.loads(sys.argv[1])\n"
        "wr = json.loads(sys.argv[2])\n"
        "diem = {}\n"
        "for m, nums in d.items():\n"
        "    w = wr.get(m, 50)/100.0\n"
        "    for r, n in enumerate(nums):\n"
        "        diem[n] = diem.get(n, 0) + w*(1.0/(1+r*0.15))\n"
        "s = sorted(diem.items(), key=lambda x: -x[1])\n"
        "sys.stdout.write(','.join(n for n, _ in s))\n"
    )
    for ten, ds_model in (("Smart Ensemble (:7894)", ML_ENSEMBLE),
                          ("Smart ML / Combo (:8101, :8354)", ML_COMBO)):
        khac = 0
        xet = 0
        for (ngay, mien), theo_model in du_lieu:
            d = {m: theo_model[m] for m in ds_model if m in theo_model}
            if len(d) < 2:
                continue
            xet += 1
            ra = set()
            for seed in ("1", "2", "987"):
                env = dict(os.environ, PYTHONHASHSEED=seed)
                p = subprocess.run([sys.executable, "-c", ma_tpl,
                                    json.dumps(d), json.dumps({})],
                                   capture_output=True, env=env)
                ra.add(p.stdout.decode().strip())
            if len(ra) > 1:
                khac += 1
        print(f"  B. {ten}: xét {xet} ngày-miền · số ngày thứ tự ĐỔI theo seed: {khac}")


def phepC_xau_nhat(du_lieu: list) -> None:
    """Trường hợp XẤU NHẤT: mọi model cùng win_rate ⇒ tối đa hoá hoà. Hoà có chạm BIÊN không."""
    for ten, ds_model in (("Smart Ensemble (:7894)", ML_ENSEMBLE),
                          ("Smart ML / Combo (:8101, :8354)", ML_COMBO)):
        xet = hoa_bat_ky = hoa_bien_01 = hoa_top3 = hoa_top10 = 0
        for (ngay, mien), theo_model in du_lieu:
            d = {m: theo_model[m] for m in ds_model if m in theo_model}
            if len(d) < 2:
                continue
            xet += 1
            diem = dung_diem(d, {})                     # rỗng ⇒ mọi model wr=50
            s = sorted(diem.items(), key=lambda x: -x[1])
            v = [x[1] for x in s]
            if len(set(v)) != len(v):
                hoa_bat_ky += 1
            if len(v) > 1 and v[0] == v[1]:
                hoa_bien_01 += 1
            if len(v) > 3 and v[2] == v[3]:
                hoa_top3 += 1
            if len(v) > 10 and v[9] == v[10]:
                hoa_top10 += 1
        print(f"  C. {ten}: {xet} ngày-miền · có hoà ở đâu đó {hoa_bat_ky} "
              f"· hoà ĐÚNG BIÊN hạng 0/1 {hoa_bien_01} · biên top-3 {hoa_top3} "
              f"· biên top-10 {hoa_top10}")


def main() -> int:
    print("=" * 92)
    print("  FU-421/GĐ-3 — ĐO ba chỗ thiếu khoá phá hoà (CHỈ ĐO, KHÔNG VÁ)")
    print("=" * 92)
    du_lieu = _lay_du_lieu(60)
    print(f"  dữ liệu: {len(du_lieu)} cặp ngày-miền có đủ số của model ML (60 ngày)\n")
    if not du_lieu:
        print("  ✗ không có dữ liệu — KHÔNG kết luận được")
        return 1
    if not phepA_doi_chung():
        print("  ✗ dụng cụ đo hỏng ⇒ mọi kết quả sau đây VÔ NGHĨA")
        return 1
    phepB_ba_cho(du_lieu)
    phepC_xau_nhat(du_lieu)
    print("=" * 92)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
