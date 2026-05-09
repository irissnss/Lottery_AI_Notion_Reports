# V105 Security PAT Deploy Key Report

## Scope

Owner pasted a new GitHub PAT in chat/report context. Treat both old and newly pasted PATs as exposed. Full tokens are never printed here.

## Findings

- 2026-05-10 01:45 VN redacted scans found no full `ghp_` PAT pattern in private/public report trees.
- Tracked placeholder/API-key patterns in private docs/tests were scrubbed so tracked files no longer match full `sk-` patterns.
- Tracked binary backup `backups/lottery-ai-repo-2026-04-07.bundle` contained a `sk-`-like pattern and was removed from the current private tree. Treat any token embedded in historical git objects as exposed/rotated.
- Remaining `sk-`/`AIza` pattern hits are untracked legacy scratch/backup files, not committed source.
- Existing V104.1 state: the newly pasted PAT was used only for VPS git remote authentication, not tracked files.
- Old token `ghp_cvoSP***`: owner must revoke explicitly in GitHub UI if not already deleted.
- Newly pasted token should also be revoked and replaced because it appeared in chat/report context.

## Recommendation

Replace PAT-based VPS remote authentication with an SSH deploy key:

1. Generate a dedicated deploy SSH key on VPS.
2. Add the public key to GitHub as deploy key or machine-user key.
3. Change VPS remote to SSH form.
4. Remove PAT from VPS git config.
5. Verify `git ls-remote origin HEAD` works without exposing credentials.

## Temporary Guard

If PAT remains temporarily, keep it only in VPS git config, root-only, never in `.env`, docs, Notion, GitHub public/private files, commit messages, logs, or artifacts.
