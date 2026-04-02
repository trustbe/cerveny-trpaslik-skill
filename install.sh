#!/bin/bash
# Cerveny Trpaslik — Claude Code skill installer
# Smoke me a kipper, I'll be back for breakfast!

set -e

SKILL_DIR="$HOME/.claude/skills/cerveny-trpaslik"
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"

echo "=== Cerveny Trpaslik — instalace skillu ==="
echo ""

# Check if Claude Code skills directory exists
if [ ! -d "$HOME/.claude" ]; then
    echo "Slozka ~/.claude neexistuje. Mas nainstalovanej Claude Code?"
    echo "https://claude.ai/claude-code"
    exit 1
fi

# Create skill directory
mkdir -p "$SKILL_DIR/references"

# Copy skill files
cp "$SCRIPT_DIR/SKILL.md" "$SKILL_DIR/"
cp "$SCRIPT_DIR/references/"*.md "$SKILL_DIR/references/"

echo "Nainstalováno do: $SKILL_DIR"
echo ""
echo "Soubory:"
echo "  SKILL.md ($(wc -c < "$SKILL_DIR/SKILL.md" | tr -d ' ') B)"
echo "  references/ ($(ls "$SKILL_DIR/references/" | wc -l | tr -d ' ') souborů)"
echo ""
echo "Skill se aktivuje automaticky kdyz zminis:"
echo "  Cerveny trpaslik, Red Dwarf, Lister, Rimmer, Cat, Kryten, Holly..."
echo ""
echo "Hotovo! Staci restartovat Claude Code."
echo ""
echo "  \"Vsichni jsou mrtvi, Dave.\""
