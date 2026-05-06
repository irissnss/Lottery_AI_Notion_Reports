import sys
import json

sys.path.insert(0, "/root/Lottery_AI_Test/web/backend")
import main

for region in ("MN", "MT", "MB"):
    data = main._build_du_doan_test_model_budget_summary(region, "2026-05-05")
    print("===", region, "===")
    print(json.dumps({
        "status": data.get("status"),
        "budget": {
            "total_pool_count": (data.get("budget") or {}).get("total_pool_count"),
            "measured_pool_count": (data.get("budget") or {}).get("measured_pool_count"),
            "selected_count": (data.get("budget") or {}).get("selected_count"),
            "watch_count": (data.get("budget") or {}).get("watch_count"),
            "skipped_count": (data.get("budget") or {}).get("skipped_count"),
            "weekday_name": (data.get("budget") or {}).get("weekday_name"),
            "station_set": (data.get("budget") or {}).get("station_set"),
        },
        "selected_top": [
            {
                "rank": r.get("model_rank"),
                "model": r.get("model_name"),
                "role": r.get("selector_role"),
                "score": r.get("final_budget_score"),
                "strength": r.get("strength_score"),
                "grain": r.get("strength_grain"),
                "sample": r.get("strength_sample"),
                "pick": (r.get("pick_for_date") or {}).get("numbers"),
                "status": (r.get("pick_for_date") or {}).get("status"),
            }
            for r in data.get("selected_voters", [])[:12]
        ],
        "watch_top": [
            {"model": r.get("model_name"), "score": r.get("final_budget_score"), "role": r.get("selector_role")}
            for r in data.get("watch_only", [])[:5]
        ],
    }, ensure_ascii=False, indent=2))
