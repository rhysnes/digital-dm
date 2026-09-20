#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")" && pwd)"
DEST="${HOME}/.cursor/skills"
mkdir -p "$DEST"
for skill in digital-dm digital-dm-setup digital-dm-charsheet; do
  src="$ROOT/skills/$skill"
  dst="$DEST/$skill"
  if [[ -e "$dst" || -L "$dst" ]]; then
    rm -rf "$dst"
  fi
  ln -s "$src" "$dst"
  echo "linked $dst -> $src"
done
echo "Done. Skills available: digital-dm, digital-dm-setup, digital-dm-charsheet"
