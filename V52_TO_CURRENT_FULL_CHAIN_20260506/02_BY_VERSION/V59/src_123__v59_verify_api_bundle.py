import sys
import asyncio
import json

sys.path.insert(0, "/root/Lottery_AI_Test/web/backend")
import main

class Req:
    pass

main.require_admin = lambda request: True

async def run():
    for region in ("MN", "MT", "MB"):
        if region == "MB":
            data = await main.api_du_doan_test_mb(Req(), date="2026-05-05")
        else:
            data = await main.api_du_doan_test_region(Req(), region=region, date="2026-05-05")
        tb = data.get("test_bundle") or {}
        print(region, json.dumps({
            "experiment": tb.get("experiment_name"),
            "bt": tb.get("bach_thu"),
            "bt_status": tb.get("bach_thu_status"),
            "lo3": tb.get("lo3"),
            "lo3_status": tb.get("lo3_status"),
            "xien2": tb.get("xien2"),
            "xien2_status": tb.get("xien2_status"),
            "xien3": tb.get("xien3"),
            "xien3_status": tb.get("xien3_status"),
            "is_post_closeout_diagnostic": tb.get("is_post_closeout_diagnostic"),
        }, ensure_ascii=False))

asyncio.run(run())
