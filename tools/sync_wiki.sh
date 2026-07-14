#!/usr/bin/env bash
#
# Mirror the canonical wiki source (wiki/) to a local clone of the GitHub wiki.
#
# This regenerates the parameter quick-reference from src/canfix.json, then
# copies the wiki pages into a sibling ../canfix-spec.wiki working copy. It does
# NOT push -- review the result and push it yourself (publishing is outward-facing).
#
# Usage:
#   tools/sync_wiki.sh [wiki-remote-url] [wiki-clone-dir]
#
# Defaults:
#   wiki-remote-url = https://github.com/billmallard/canfix-spec.wiki.git
#   wiki-clone-dir  = ../canfix-spec.wiki   (relative to repo root)
#
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
SRC="$REPO_ROOT/wiki"
WIKI_URL="${1:-https://github.com/billmallard/canfix-spec.wiki.git}"
WIKI_DIR="${2:-$REPO_ROOT/../canfix-spec.wiki}"

# 1. Regenerate the parameter quick-reference from the spec data.
echo "Regenerating Parameter-Reference.md from src/canfix.json"
python "$REPO_ROOT/tools/gen_param_reference.py"

if [ ! -d "$SRC" ]; then
  echo "error: $SRC not found" >&2
  exit 1
fi

# 2. Clone or update the wiki working copy.
if [ -d "$WIKI_DIR/.git" ]; then
  echo "Updating existing wiki clone at $WIKI_DIR"
  git -C "$WIKI_DIR" pull --ff-only
else
  echo "Cloning wiki from $WIKI_URL into $WIKI_DIR"
  echo "  (the wiki must exist: open the repo's Wiki tab and create one page first,"
  echo "   or push an initial commit to $WIKI_URL)"
  git clone "$WIKI_URL" "$WIKI_DIR"
fi

# 3. Copy each page. Inter-page links already use the extension-less GitHub wiki
#    form ([text](Page-Name)); the sed is a harmless safety net for any that use
#    a .md suffix.
shopt -s nullglob
for f in "$SRC"/*.md; do
  base="$(basename "$f")"
  sed -e 's#\](\([A-Za-z0-9_-]*\)\.md\([)#]\)#](\1\2#g' \
      "$f" > "$WIKI_DIR/$base"
  echo "  page: $base"
done

echo
echo "Mirror staged in $WIKI_DIR (NOT pushed)."
echo "Review and publish:"
echo "  cd \"$WIKI_DIR\" && git add -A && git commit -m 'Sync wiki from wiki/' && git push"
