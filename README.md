# Digital DM

Genre-agnostic **skills + campaign filesystem** for a Cursor agent acting as a long-term RPG / D&D Dungeon Master.

Chat is ephemeral. **Files are canon.**

## What’s in this repo

| Path | Purpose |
|------|---------|
| `skills/digital-dm/` | Run sessions: track world state, narrate, update files |
| `skills/digital-dm-setup/` | Scaffold a new campaign tree from templates |
| `templates/` | Starter markdown for NPCs, quests, inventory, etc. |
| `scaffold/` | Empty campaign folder layout to copy |

Genre (fantasy, Trek-like sci-fi, horror, …) lives in the **campaign** tree, not in these skills.

Tone palette inspirations (optional, not mandates): Dungeons and Daddies, Critical Role, Not Another D&D Podcast — see `skills/digital-dm/references/tone-inspirations.md`.

## Install skills for Cursor

```bash
"/home/rhys/Coding Projects/Tools/digital-dm/install.sh"
```

Symlinks into `~/.cursor/skills/`. Re-run after pulls.

## Typical campaign root

Point the agent at a campaign directory (example):

`/home/rhys/DnD-Campaigns/<campaign-slug>/`

See `skills/digital-dm/references/filesystem.md` for the full map.

## Quick start

1. Install skills (`install.sh`)
2. Ask the agent to use **digital-dm-setup** and create/copy a campaign under your campaigns folder
3. In play, invoke **digital-dm** (or mention Dungeon Master / campaign tracking) so it reads `state/campaign.md` and writes lasting changes to disk
