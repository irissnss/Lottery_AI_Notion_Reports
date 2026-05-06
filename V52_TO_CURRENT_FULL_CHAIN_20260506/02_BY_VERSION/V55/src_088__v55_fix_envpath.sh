#!/bin/bash
# V20.3.37.55 — append GEMINI_KEY_SHADOW_NEW to PROJECT-ROOT .env (the one env_loader actually reads)
set -e

ROOT_ENV=/root/Lottery_AI_Test/.env
BACKEND_ENV=/root/Lottery_AI_Test/web/backend/.env
BK=/root/Lottery_AI_Test/backups/v55_shadow_add_20260505_0750

# Backup project-root .env
cp "$ROOT_ENV" "$BK/project_root_env.bak"

# Idempotent append
if grep -q '^GEMINI_KEY_SHADOW_NEW=' "$ROOT_ENV"; then
    echo "GEMINI_KEY_SHADOW_NEW already in project-root .env — skipping"
else
    echo "" >> "$ROOT_ENV"
    echo "# V20.3.37.55 (2026-05-05): Google AI Studio Tier-2 key for new shadow cohort" >> "$ROOT_ENV"
    echo "# Used by gemini-3.1-pro / gemini-3-flash / gemma-4-31b only." >> "$ROOT_ENV"
    echo "# Output models gemini-2.5-flash / gemini-2.5-pro keep using legacy GEMINI_API_KEY." >> "$ROOT_ENV"
    echo "GEMINI_KEY_SHADOW_NEW=<REDACTED_GOOGLE_API_KEY>" >> "$ROOT_ENV"
    echo "GEMINI_KEY_SHADOW_NEW appended to project-root .env"
fi

# Remove the wrongly appended key from backend/.env (keep only legacy keys)
if grep -q '^GEMINI_KEY_SHADOW_NEW=' "$BACKEND_ENV"; then
    sed -i '/^GEMINI_KEY_SHADOW_NEW=/d' "$BACKEND_ENV"
    echo "Cleaned wrongly-appended key from backend/.env"
fi

echo "=== project-root .env keys (names only) ==="
grep -E '^[A-Z_]+=' "$ROOT_ENV" | sed 's/=.*/=<set>/'

echo "=== backend/.env keys (names only) ==="
grep -E '^[A-Z_]+=' "$BACKEND_ENV" | sed 's/=.*/=<set>/'

echo "=== POST-FIX HASHES ==="
sha256sum "$ROOT_ENV" "$BACKEND_ENV"
