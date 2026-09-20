# Campaign filesystem

Genre-agnostic layout. Keep **folder roles** stable so any Digital DM agent knows where to look. Rename flavour *inside* files freely.

Agent copy: `skills/digital-dm/references/filesystem.md`.

## Tree

```
<campaign-root>/
  README.md                 # how to use this campaign + tone pointer
  AGENT-HANDOFF.md          # paste into new chats
  DM-PROTOCOL.md            # optional short operator card
  world/                    # stable lore (calendar, map, cosmology)
  module/
    OVERVIEW.md             # premise, arcs / seasons
    secrets.md              # DM-only — never narrate raw
    arcs/   or  seasons/
    episodes/               # digressions that still change the world
    sidequests/             # seeds
  party/                    # PC sheets, shared inventory, currency
  npcs/                     # dossiers + index.md
  locations/                # places + index.md
  factions/
  traders/                  # stock, prices, restock
  quests/
    active.md
    dormant.md
    completed.md
    Q001-example.md
  state/
    campaign.md             # living snapshot (session, location, flags)
    clocks.md               # progress pressures
    session-log.md
    plot-points.md          # optional
    timeline.md             # optional
    player-canon.md         # accepted improv facts
    session-0-brief.md      # wizard answers
  encounters/               # random tables / engines
  rules/                    # house rules, tone.md, local improv notes
  handouts/                 # player-facing letters, map notes
```

The empty starter tree lives in `scaffold/`. File bodies are seeded from `templates/`.

## Source of truth (priority)

1. `state/campaign.md` + the relevant entity file  
2. `state/player-canon.md` (once written, equal to other canon)  
3. `module/` planned arc — does **not** override lived state  
4. Chat — never

## Naming

- Files: `kebab-case.md`
- Quests: `Q001-short-slug.md`
- Keep indexes updated: `npcs/index.md`, `locations/index.md`, `traders/index.md`, `factions/index.md`

## Toolkit vs campaign

| This repo (`digital-dm`) | Your campaign folder |
|--------------------------|----------------------|
| Skills, templates, docs | Story, secrets, PC sheets, session state |
| Safe to `git pull` | Yours alone — back it up separately |

Do **not** put Cursor skills inside the campaign tree.
