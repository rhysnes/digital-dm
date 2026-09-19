---
name: digital-dm-setup
description: >-
  Scaffolds a genre-agnostic Digital DM campaign filesystem (state, party, NPCs,
  locations, quests, traders, factions, module, templates). Use when the user
  asks to create a new campaign, initialize Digital DM files, or set up RPG
  tracking folders for a long-term D&D or similar game.
---

# Digital DM — Campaign Setup

Create a campaign tree the **digital-dm** skill can run against.

## Steps

1. **Confirm** parent folder (default suggestion: `~/DnD-Campaigns/`) and **slug** (e.g. `ember-concord`, `idsx-galapagos`).
2. **Copy scaffold** from this repo:

```bash
REPO="/home/rhys/Coding Projects/Tools/digital-dm"
DEST="${CAMPAIGNS_PARENT}/${SLUG}"  # set these
cp -a "$REPO/scaffold/." "$DEST/"
# seed key stubs from templates
cp "$REPO/templates/campaign-state.md" "$DEST/state/campaign.md"
cp "$REPO/templates/session-log.md" "$DEST/state/session-log.md"
cp "$REPO/templates/clocks.md" "$DEST/state/clocks.md"
cp "$REPO/templates/player-canon.md" "$DEST/state/player-canon.md"
cp "$REPO/templates/character.md" "$DEST/party/roster.md"  # replace with real roster after
```

Prefer writing real starter files over leaving empties. Use templates in `templates/` for NPCs, quests, etc.

3. **Write** at minimum:
   - `README.md` — tone, genre, how to use the tree
   - `AGENT-HANDOFF.md` — paste block for future chats
   - `module/OVERVIEW.md` — premise + season/arc map
   - `module/secrets.md` — DM-only framework (locked antagonist rules)
   - `party/` — PC sheet(s)
   - `state/campaign.md` — session 0 flags

4. **Genre** goes in campaign content (names, tech/magic, voice). Do not fork the skill for genre.

5. Tell the user the path and that play uses skill **digital-dm**.

## Layout reference

See [../digital-dm/references/filesystem.md](../digital-dm/references/filesystem.md).

## Do not

- Overwrite an existing campaign without explicit confirmation
- Copy a finished adventure’s secrets into a new slug by accident
- Put Cursor skills inside the campaign tree (skills live in this repo / `~/.cursor/skills`)
