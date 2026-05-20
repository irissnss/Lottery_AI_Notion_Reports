# V105.84 Owner Report Public

## Finding

Rules with source station `TP. TP. HCM` can fail to produce candidate tails because result rows use `TP. HCM`.

## Known affected examples

- R1339, target date 2026-05-19, source `TP. TP. HCM`, keys `G7+G8`: before no tails; read-time alias would produce `42,80`.
- R1339, target date 2026-05-12: would produce `27,80`.
- R1356, target date 2026-05-16: would produce `41,72`.
- R1356, target date 2026-05-09: would produce `59,74`.

## Decision

Recommended safe path is read-time alias normalization only, no historical DB mutation, no Rule105 weight change, no selector change, no lane promotion.
