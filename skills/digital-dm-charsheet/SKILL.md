---
name: digital-dm-charsheet
description: >-
  Display and maintain RPG character sheets as Markdown files with YAML
  frontmatter and as boxed ASCII art in the terminal. Use when the user asks
  for a character sheet, charsheet, ASCII sheet, print sheet, show stats, or
  to create/update a party/*.md sheet for Digital DM.
---

# Digital DM — Character Sheet

Show sheets in **two forms**:

1. **Markdown file** (canon on disk) with YAML frontmatter  
2. **ASCII graphic** in the terminal via the renderer script  

## File format

Sheets live under the campaign, usually `party/<slug>.md`.

Required: YAML frontmatter between `---` lines. Human-readable Markdown body below is optional but recommended.

See [references/format.md](references/format.md) and [examples/sample-vanguard.md](examples/sample-vanguard.md).

## Agent workflow

### Show an existing sheet
1. Read the `.md` file (confirm frontmatter exists).  
2. Run the renderer and show the user the terminal output:

```bash
python3 "<REPO>/skills/digital-dm-charsheet/scripts/charsheet.py" render "<PATH_TO_SHEET.md>"
```

Resolve `<REPO>` as the digital-dm git root (parent of `skills/`). If the skill is symlinked from `~/.cursor/skills/digital-dm-charsheet`, use that path’s `scripts/charsheet.py`.

3. Optionally paste the same ASCII into chat if the user isn’t watching the terminal.

### Create / update a sheet
1. Write or edit the Markdown file (keep frontmatter fields in sync with play: HP, inventory, level).  
2. Run `render` (or `init` for a brand-new stub):

```bash
python3 "<REPO>/skills/digital-dm-charsheet/scripts/charsheet.py" init "<PATH>" --name "Name" --class Vanguard --level 1 --ancestry Human
```

3. After combat/loot, update the file **and** re-render.

### Digital DM integration
When skill **digital-dm** changes HP, inventory, or level on a PC, update that PC’s sheet frontmatter the same beat, then re-render if the user is looking at the sheet.

## Do not
- Invent a second sheet path; use the campaign `party/` file  
- Put ability scores only in chat  
- Skip the ASCII render when the user asked to “show” or “display” the sheet  
