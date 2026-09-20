# Getting started

## Prerequisites

- [Cursor](https://cursor.com) (desktop) with Agent / skills support
- Git
- A place to store campaigns (example: `~/DnD-Campaigns/`)

## 1. Clone and install skills

```bash
git clone https://github.com/rhysnes/digital-dm.git
cd digital-dm
./install.sh
```

This symlinks:

- `~/.cursor/skills/digital-dm` → this repo’s `skills/digital-dm`
- `~/.cursor/skills/digital-dm-setup` → `skills/digital-dm-setup`

Re-run `./install.sh` after `git pull` if links break.

**Manual install:** copy or symlink those two skill folders into `~/.cursor/skills/` yourself.

## 2. Run the Setup Wizard

In a Cursor chat:

> Use **digital-dm-setup**. Start the Setup Wizard for a new campaign.

The agent asks about tone, setting, comedy rules, and whether to:

- **A** use existing docs  
- **B** invent an original storyline  
- **C** hybrid  
- **D** reskin  

Details: [setup-wizard.md](setup-wizard.md).

It will confirm a summary card, then create a campaign folder (default pattern: `~/DnD-Campaigns/<slug>/`) with scaffold + filled stubs.

## 3. Play

> Act as Digital DM for `<campaign-path>` using **digital-dm**. Read `state/campaign.md` first. Do not start the adventure until I say go.

Or paste your campaign’s `AGENT-HANDOFF.md` into a new chat. See [agent-handoff.md](agent-handoff.md).

## 4. What success looks like

After a session beat you should see real file updates under the campaign root, for example:

- `state/campaign.md` — location, session #, flags  
- `state/session-log.md` — keypoints  
- `party/` — HP, inventory, currency  
- `npcs/`, `quests/` — as things appear  

If the agent only “remembers” in chat and never writes files, remind it: **files are canon**.

## Updating the toolkit

```bash
cd digital-dm
git pull
./install.sh
```

Campaign folders are separate; pulling the toolkit does not overwrite your adventures.
