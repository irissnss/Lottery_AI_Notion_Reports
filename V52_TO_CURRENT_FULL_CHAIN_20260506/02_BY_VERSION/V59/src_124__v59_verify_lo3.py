import sys
import json
sys.path.insert(0, "/root/Lottery_AI_Test/web/backend")
import main

for region in ("MN", "MT", "MB"):
    axes = main._du_doan_test_actual_axis_sets(region, "2026-05-05")
    print("===", region, "actual ===")
    print("2d_n=", len(axes["tails_2d"]), "3d_n=", len(axes["tails_3d"]), "stations=", list(axes["per_station_2d"].keys()))
    # Load API-style bundle via helper pieces by calling region endpoint internals is hard,
    # so print known expected test lo3 from direct helper by reconstructing selected primary.
    # We validate status helper directly on official/test values seen in DB.
    for lo3 in ("015", "052", "152", "044", "083", "141"):
        print(lo3, main._du_doan_test_lo3_status(lo3, axes))
    for vals in (["52", "15"], ["52", "41"], ["41", "83"], ["91", "14"], ["44", "31"]):
        print(vals, "x2=", main._du_doan_test_xien_status(vals, axes, 2), "x3=", main._du_doan_test_xien_status(vals + ["98"], axes, 3))
