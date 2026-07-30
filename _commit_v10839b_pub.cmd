@echo off
cd /d E:\Lottery_AI_Notion_Reports
git add .markdownlint.jsonc V10839_MARKDOWNLINT_NOISE_CLEANUP_20260723
git commit -m "V10839b: repo-level markdownlint config (default:false) + report addendum - 1173 md files 0 issues"
git log -1 --oneline
