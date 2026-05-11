# V105.22 Tomorrow Live Ready Checklist

Generated: 2026-05-11T08:59:39+07:00

Safety scope: lane-test / shadow / diagnostic only. No production scoring, selector, bundle voting, official prompt, official roster, `generate_final_bundle()`, `/du-doan`, or `/api/final-bundle` mutation.

Hash guard pre/post for the V105.22 live-prep deploy and access-log stability fix is identical for the four official evidence tables:

```json
{
  "predictions": {
    "rows": 4739,
    "sha256": "a3a6022eda6fadcf244f7b429091d5d6d0a1946d8816ce1266e6fc14584a1b2c"
  },
  "final_bundles": {
    "rows": 217,
    "sha256": "105ed85c01defb3c6407dff87f7ede426afd3f54f137981aeeb6d80ece2aadcf"
  },
  "lottery_results": {
    "rows": 14649,
    "sha256": "379b7b51587bf5c8e2d5fac206099bc2b7ee3fd4feb2fbd68f57a1e230911e87"
  },
  "model_daily_eval": {
    "rows": 4572,
    "sha256": "3f71c595ee87b620182e0f2f28949f33de9916c489dc635167ff066a3e0e6517"
  }
}
```


## Checklist

- Governance/private docs read and updated: yes.
- Official hash baseline recorded: yes, 4/4 unchanged.
- VPS runtime deployed: yes, service active.
- Endpoint smoke: health/status/du-doan/final-bundle MN/MT/MB = 200; admin/test surfaces require auth = 401 unauth expected.
- Region profiles saved: yes, 3 rows.
- Station identity audit: pass, `unexpected_count=0` for runtime checked tables.
- Lose-only gate: pass, recycled winner count=0 and source unknown used=0 for MN/MT/MB.
- Security scan: token-pattern matches exist in historical docs/artifacts; VPS remote still contains token pattern. Owner action remains revoke exposed PATs and migrate VPS deploy to SSH key.
- Live lane morning state: MN ready 20/20; MT/MB preview below budget until later regional cadence.
