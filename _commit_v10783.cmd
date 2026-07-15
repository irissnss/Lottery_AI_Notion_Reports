@echo off
cd /d E:\Lottery_AI_Notion_Reports
git add V10783_LIVE_STABILITY_PARTIAL_20260705_PUBLIC_SAFE
git commit -m "V10783 partial report: P0 only (~55%%) - commit freeze NO STATE LOSS, smoke freeze pass, surface=official backend; P1-P6 not started; honest delivery gap explanation"
git push origin main
git log --oneline -1
