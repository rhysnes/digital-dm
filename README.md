# Digital DM

Genre-agnostic **skills + campaign filesystem** for a [Cursor](https://cursor.com) agent acting as a long-term RPG / D&D Dungeon Master.

**Chat is ephemeral. Files are canon.**

This repository is the **DM toolkit only**. It does **not** ship a pre-written adventure. You (and the Setup Wizard) create or import your own campaign.

| | |
|-|-|
| **Repo** | https://github.com/rhysnes/digital-dm |
| **Skills** | `digital-dm-setup` (wizard + scaffold) · `digital-dm` (run sessions) |
| **Requires** | [Cursor](https://cursor.com) with Agent Skills enabled |

## Documentation

| Doc | What it’s for |
|-----|----------------|
| [Getting started](docs/getting-started.md) | Clone, install, first campaign |
| [Setup Wizard](docs/setup-wizard.md) | Tone, theme, setting, storyline source (A–D) |
| [Campaign filesystem](docs/campaign-filesystem.md) | Folder map and what each path means |
| [Playing sessions](docs/playing-sessions.md) | How the DM skill runs a session |
| [Tracking guide](docs/tracking-guide.md) | NPCs, quests, inventory, clocks, currency |
| [Narration & tone](docs/narration-and-tone.md) | Plain speech, sensible options, comedy rules |
| [Improv & canon](docs/improv-and-canon.md) | Yes-and, player-canon pipeline |
| [Agent handoff](docs/agent-handoff.md) | Paste blocks for new chats |
| [FAQ](docs/faq.md) | Common questions |
| [Contributing](CONTRIBUTING.md) | Changes to the toolkit |
| [Agents](AGENTS.md) | Notes for AI agents using this repo |

## Quick start

```bash
git clone https://github.com/rhysnes/digital-dm.git
cd digital-dm
./install.sh
```

In Cursor, ask something like:

> Run the **digital-dm-setup** Setup Wizard and create a new campaign.

After the wizard scaffolds files, play with:

> Act as Digital DM for the campaign at `~/DnD-Campaigns/<your-slug>/` using the **digital-dm** skill.

## What’s in this repo

```
digital-dm/
├── README.md                 ← you are here
├── AGENTS.md
├── CONTRIBUTING.md
├── LICENSE
├── install.sh                ← symlink skills into ~/.cursor/skills/
├── docs/                     ← human documentation
├── skills/
│   ├── digital-dm/           ← session runner skill
│   └── digital-dm-setup/     ← wizard + scaffold skill
├── templates/                ← markdown starters copied into campaigns
└── scaffold/                 ← empty campaign folder tree
```

Genre (fantasy, sci-fi, horror, …) lives in **your campaign folder**, not in these skills.

Optional tone inspirations (palette, not mandates): Dungeons and Daddies, Critical Role, Not Another D&D Podcast, DnD Is For Nerds — see [Narration & tone](docs/narration-and-tone.md).

## License

MIT — see [LICENSE](LICENSE).
