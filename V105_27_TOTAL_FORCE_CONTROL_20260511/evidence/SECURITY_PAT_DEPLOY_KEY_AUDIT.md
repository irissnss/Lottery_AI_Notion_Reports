# SECURITY / PAT / DEPLOY KEY AUDIT — V105.27

## 1. Findings (synthesized from V105.6 / V105 security report and current state)

| Item | Evidence | Status | Required owner action |
|---|---|---|---|
| Tracked file scan for `ghp_` PAT pattern | V105 security report: "2026-05-10 01:45 VN redacted scans found no full `ghp_` PAT pattern in private/public trees" | `SECRET_SCAN_CLEAN` (current tracked tree) | None — keep redacted scan in CI/pre-commit |
| Tracked `sk-` API key patterns | `archive/tests/test_prediction.py`, `web/README.md` scrubbed; remaining `sk-`/`AIza` hits are untracked legacy backups | `SECRET_SCAN_CLEAN` for committed source | Sweep untracked legacy backup files before any new git push |
| Removed binary backup with embedded key | `backups/lottery-ai-repo-2026-04-07.bundle` removed (contained `sk-`-like pattern) | `REMOVED` | Treat token embedded in historical git objects as exposed/rotated |
| Old GitHub PAT `ghp_cvoSP***` | V105 security report | `PAT_REVOKE_PENDING` — owner must revoke in GitHub UI if not done | YES — owner click revoke + confirm |
| Newly pasted PAT (appeared in chat context earlier) | V105 security report | `PAT_REVOKE_PENDING` — best practice rotate after chat exposure | YES — owner rotate |
| SSH deploy key migration | V105 security report recommended migration; FU-V105-22-TOTAL-FORCE-LIVE-PREP carries this | `SSH_DEPLOY_KEY_PENDING` | YES — owner approve to: generate VPS SSH key, add as deploy key on GitHub, switch VPS remote to SSH form, remove PAT from VPS git config |
| `.env` not committed | No `.env` in tracked tree (verify via `git ls-files .env` returns empty) | `CLEAN` | None |
| Runtime manifest token redaction | Live-sync manifest uses path-only fingerprints, no embedded secrets | `CLEAN` | None |

## 2. Classification

- `SECURITY_P0_OPEN` — old PAT revocation not confirmed by owner.
- `PAT_REVOKE_PENDING` — both old and newly pasted PATs need explicit owner action.
- `SSH_DEPLOY_KEY_PENDING` — migration approved in concept, not yet executed.
- `SECRET_SCAN_CLEAN` — current tracked tree clean.
- `REDACTION_REQUIRED_BEFORE_PUBLIC_PUSH` — every public-push step must pass `rg "ghp_[A-Za-z0-9]{36}"`, `rg "sk-[A-Za-z0-9]{20,}"`, `rg "AIza[0-9A-Za-z\-_]{35}"` returns 0.

## 3. Recommended sequence (owner-gated)

1. Owner revokes old + newly-pasted PATs on GitHub.
2. Owner approves SSH deploy key generation on VPS (no provider/credential changes, pure SSH).
3. Agent generates `ed25519` key on VPS (read-only step, no chat output of private key).
4. Owner pastes public key into GitHub deploy keys; agent rewires `origin` to SSH.
5. Agent removes PAT from VPS `git config`; verifies `git ls-remote origin HEAD` works.
6. Run final redacted scan + commit governance update.

No secrets printed in this report.
