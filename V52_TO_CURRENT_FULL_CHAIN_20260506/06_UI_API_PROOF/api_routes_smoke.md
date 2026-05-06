# API route smoke

- `/api/health=200`
- `/du-doan=200`
- `/du-doan-test=401` unauth admin-only
- `/api/du-doan-test/{region}=401` unauth admin-only
- `/api/final-bundle?region=MN/MT/MB=200` in V55/V56/V57 smoke logs
