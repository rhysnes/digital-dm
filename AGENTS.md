# Notes for AI agents

You are helping with the **Digital DM toolkit** repository, or using it to run a campaign.

## If the user wants to *play*

1. Prefer skills **digital-dm-setup** (new campaign / wizard) or **digital-dm** (session play).
2. Campaign canon lives in the **campaign folder**, not in this repo.
3. Read `state/campaign.md` before narrating. Write lasting changes to disk.
4. Human docs: `docs/`. Skill refs: `skills/*/references/`.

## If the user wants to *change this toolkit*

- Keep skills genre-agnostic
- Update `docs/` when behaviour changes
- Do not commit personal campaign secrets into this repository

## Install check

Skills should be symlinked via `./install.sh` to `~/.cursor/skills/digital-dm` and `digital-dm-setup`.
