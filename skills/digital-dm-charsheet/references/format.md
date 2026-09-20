# Character sheet format

## YAML frontmatter (required for ASCII render)

```yaml
---
name: Ada Voss
player: Rhys
ancestry: Human
class: Vanguard
level: 3
background: Frontier Scout
alignment: NG
hp: 28
hp_max: 28
ac: 16
speed: 30
proficiency: 2
initiative: 1
str: 16
dex: 12
con: 14
int: 10
wis: 13
cha: 8
armor: Chain mail
skills:
  - Athletics
  - Perception
  - Survival
weapons:
  - Longsword +5 (1d8+3)
  - Javelin +5 (1d6+3)
features:
  - Second Wind
  - Action Surge
inventory:
  - Explorer's pack
  - 15 gp
notes: |
  Prefers the front line.
---
```

Below the closing `---`, keep normal Markdown tables/lists for humans and for campaigns that don’t use the renderer.

## Field reference

| Key | Purpose |
|-----|---------|
| `name` | Character name |
| `player` | Player name |
| `ancestry` | Race / ancestry |
| `class` | Class / role |
| `level` | Level or rank number |
| `background` | Background |
| `alignment` | Alignment / ethos |
| `hp`, `hp_max` | Current / max HP |
| `ac`, `speed`, `proficiency`, `initiative` | Combat stats |
| `str`…`cha` | Ability scores (integers) |
| `armor` | Armor string |
| `skills`, `weapons`, `features`, `inventory` | YAML lists |
| `notes` | Block or string |

Aliases accepted by renderer: `species`→ancestry, `role`→class, `hp_current`→hp.
