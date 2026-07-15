@echo off
cd /d E:\Lottery_AI_Notion_Reports
git add V10785_FORENSIC_GATE_20260705_PUBLIC_SAFE/BAO_CAO_TONG_V10785.md V10785_FORENSIC_GATE_20260705_PUBLIC_SAFE/NOTION_SYNC_PAYLOAD_V10785.md V10785_FORENSIC_GATE_20260705_PUBLIC_SAFE/CONVERSATION_CONTEXT_V10785_20260705.md
git commit --trailer "Co-authored-by: Cursor <cursoragent@cursor.com>" -m "V10785 final: bao cao tong (gate GO 9/9 + 23:50 PASS + lock 06/07 active + board ref fix 00:10 + hash IDENTICAL + K1-K7 cho ky) + Notion payload + conversation context"
git push origin main
echo EXIT_PUBLIC=%ERRORLEVEL%
