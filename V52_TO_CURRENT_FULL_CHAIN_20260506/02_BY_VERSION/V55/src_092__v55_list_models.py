"""V20.3.37.55 — list available Google models on the new Tier-2 key (project sxkt)."""
import sys, os, re
sys.path.insert(0, '/root/Lottery_AI_Test/web/backend')
from env_loader import load_project_env
load_project_env()
from google import genai as google_genai

client = google_genai.Client(api_key=os.environ['GEMINI_KEY_SHADOW_NEW'])

print("=== Models containing 'gemini-3' or 'gemma-4' ===")
for m in client.models.list():
    name = m.name or ''
    short = name.replace('models/', '')
    if re.search(r'gemini-3|gemma-4', short, re.I):
        methods = getattr(m, 'supported_actions', None) or []
        disp = getattr(m, 'display_name', '')
        print(f"  api_id={short:40s}  display={disp}")
