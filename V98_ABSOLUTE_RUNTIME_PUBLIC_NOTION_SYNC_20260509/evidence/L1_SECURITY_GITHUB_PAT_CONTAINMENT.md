# V99.2 L1 — GitHub PAT Containment + Secret Inventory (REDACTED)

**Generated**: 2026-05-09 12:35 VN  
**Owner directive**: V99.2 LANE 1 — NO full token printed.

## 1. GitHub PAT containment

| Item | Status |
|---|---|
| Working tree contains full PAT | ❌ NO (scan: 0 `ghp_*` in 14,353 files) |
| Local CHANGELOG/docs/artifacts | ✅ REDACTED (only `ghp_cvoSP***` prefix) |
| Public reports | ✅ REDACTED |
| Private git history commit `fb2ae98` | ⚠ CONTAINS_FULL_PAT (already pushed pre-redact) |
| VPS git remote URL | ⚠ CONTAINS_FULL_PAT |
| Owner REVOKED? | ⚠ UNKNOWN — OWNER_ACTION_REQUIRED |
| Post-revoke effective | ✅ INERT (token value useless once revoked) |

## 2. Secret inventory summary (NO full values printed)

| Secret | Location | In git history? | Status | Rotate? |
|---|---|---|---|---|
| GitHub PAT | VPS git config + commit fb2ae98 | YES | EXPOSED_CONFIRMED | **MUST_ROTATE_NOW** |
| OpenAI/Anthropic/Google/DeepSeek/Qwen/Kimi/GLM/xAI keys | `.env` (gitignored) | NO | NOT_EXPOSED_ENV_ONLY | KEEP_WITH_MONITORING |
| Admin JWT/DB | `.env` | NO | NOT_EXPOSED_ENV_ONLY | KEEP_WITH_MONITORING |

### False positives
- `_test_output_utf8.txt` 84 GLM-pattern matches = lottery digit sequences (NOT real tokens)

## 3. Owner action checklist

- [ ] **REVOKE GitHub PAT** at https://github.com/settings/tokens (P0)
- [ ] Fix VPS git remote (no inline PAT)
- [ ] (OPTIONAL) BFG/git-filter-repo to scrub history

## 4. Verdict

- ✅ Code scan clean (V99.1 redaction worked)
- ✅ All other secrets env-only (no exposure proof)
- ⚠ GitHub PAT still in private git history + VPS config — owner action required

**STATUS**: PARTIAL containment, OWNER_ACTION_REQUIRED to fully close.
