import sys
sys.path.insert(0, "/root/Lottery_AI_Test/web/backend")
from model_registry import SHADOW_AUTO_EVAL_MODELS
import scheduler

for region in ("MN", "MT", "MB"):
    ordered = scheduler._order_shadow_models_for_region(SHADOW_AUTO_EVAL_MODELS, region, "2026-05-05")
    print(region, "registry=", SHADOW_AUTO_EVAL_MODELS)
    print(region, "ordered =", ordered)
