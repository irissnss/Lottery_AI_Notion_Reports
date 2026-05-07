# NEXT ACTION — V75 proposal awaiting owner choice

Owner needs to choose from V75_PROPOSAL.md §8:

- **A** OK em làm hết P0 (drift detector + C-16 latency_score + cost table)
- **B** Chỉ làm drift detector trước
- **C** Để cron tự chạy 14d trước, đừng đụng
- **D** Làm UI dashboard P1-3 luôn
- **E** Custom anh chỉ định

P0 list (em đề xuất):
1. Drift detector materializer (30 min, ZERO risk)
2. C-16 latency_score live integration (20 min, ZERO risk; uses C-05 data)
3. Cost provider table for daily $ tracking (20 min, ZERO risk)

P1/P2/P3: see V75_PROPOSAL.md.
