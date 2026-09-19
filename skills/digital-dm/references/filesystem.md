# Campaign filesystem

Genre-agnostic. Rename flavour inside files; keep folder roles stable so agents always know where to look.

```
<campaign-root>/
  README.md                 # bible pointer + tone
  AGENT-HANDOFF.md          # paste for new chats
  DM-PROTOCOL.md            # optional short operator card
  world/                    # stable setting lore (calendar, map, cosmology)
  module/
    OVERVIEW.md             # premise, arcs/seasons map
    secrets.md              # DM-only; never narrate raw
    arcs/                   # or seasons/
    episodes/               # digressions that still change the world
    sidequests/             # seeds
  party/                    # PC sheets, shared inventory, currency
  npcs/                     # dossiers + index
  locations/                # places + index
  factions/                 # goals, pressure on PCs
  traders/                  # stock, prices, restock
  quests/                   # active.md, dormant.md, completed.md, Q-###-*.md
  state/
    campaign.md             # living snapshot (session, location, flags)
    clocks.md               # progress clocks
    session-log.md          # keypoints per session
    plot-points.md          # optional
    timeline.md             # optional
    player-canon.md         # accepted improv facts
  encounters/               # tables / random engines
  rules/                    # house rules, narration, improv (campaign-local)
  handouts/                 # player-facing texts
```

## Source of truth priority

1. `state/campaign.md` + relevant entity file  
2. `state/player-canon.md` (once written, equal to other canon)  
3. `module/` for planned arc — does not override lived state  
4. Chat — never

## Naming

- Files: `kebab-case.md`
- Quests: `Q001-short-slug.md`
- Indexes in `npcs/index.md`, `locations/index.md`, `traders/index.md`
