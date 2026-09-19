# Digital DM

Genre-agnostic **skills + campaign filesystem** for a Cursor agent acting as a long-term RPG / D&D Dungeon Master.

Chat is ephemeral. **Files are canon.**

This repository is the **DM toolkit only** — it does not include a pre-written adventure. Each user runs the Setup Wizard and builds (or imports) their own campaign.

## What’s in this repo

| Path | Purpose |
|------|---------|
| `skills/digital-dm/` | Run sessions: track world state, narrate, update files |
| `skills/digital-dm-setup/` | Setup wizard + scaffold a new campaign tree |
| `templates/` | Starter markdown for NPCs, quests, inventory, etc. |
| `scaffold/` | Empty campaign folder layout to copy |

Genre (fantasy, Trek-like sci-fi, horror, …) lives in the **campaign** tree you create, not in these skills.

Tone palette inspirations (optional, not mandates): Dungeons and Daddies, Critical Role, Not Another D&D Podcast, DnD Is For Nerds — see `skills/digital-dm/references/tone-inspirations.md`.

## Install skills for Cursor

From the repo root:

```bash
./install.sh
```

Symlinks into `~/.cursor/skills/`. Re-run after pulls.

## Typical campaign root

Point the agent at a campaign directory you create, for example:

`~/DnD-Campaigns/<campaign-slug>/`

See `skills/digital-dm/references/filesystem.md` for the full map.

## Quick start

1. Clone this repo and run `./install.sh`
2. In Cursor, ask the agent to run **digital-dm-setup** — Setup Wizard (tone, theme, setting, existing docs vs original storyline)
3. After files exist, play with **digital-dm** (reads `state/campaign.md`, writes lasting changes)
