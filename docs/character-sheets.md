# Character sheets (Markdown + ASCII)

Skill: **digital-dm-charsheet**

## What it does
- Stores PC sheets as `party/<slug>.md` with **YAML frontmatter** + Markdown body  
- Renders a **boxed ASCII** sheet in the terminal  

## Install
From the digital-dm repo root: `./install.sh` (includes this skill).

## Commands

```bash
# Print ASCII from an existing sheet
python3 skills/digital-dm-charsheet/scripts/charsheet.py render path/to/sheet.md

# Create a stub sheet and print ASCII
python3 skills/digital-dm-charsheet/scripts/charsheet.py init party/ada-voss.md \
  --name "Ada Voss" --class Vanguard --level 1 --ancestry Human
```

Format details: `skills/digital-dm-charsheet/references/format.md`  
Example: `skills/digital-dm-charsheet/examples/sample-vanguard.md`
