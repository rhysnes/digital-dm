# Contributing

Thanks for improving **Digital DM** (the toolkit — not individual campaign stories).

## Scope

In scope:

- Skills (`skills/digital-dm`, `skills/digital-dm-setup`)
- Templates, scaffold, `docs/`, install script
- Clarity, portability, bug fixes

Out of scope for this repo:

- Full adventure modules / personal campaign state
- Genre forks of the skills (put genre in the campaign tree instead)

## Dev loop

1. Fork / branch from `main`
2. Edit skills or docs
3. Keep `SKILL.md` files concise; put detail in `references/` or `docs/`
4. Run `./install.sh` locally to test symlinks
5. Open a PR with a short “why”

## Skill authoring notes

- Follow [Cursor skill guidance](https://cursor.com): clear `description`, progressive disclosure
- Descriptions in third person; include WHAT and WHEN
- Do not hardcode one user’s home directory paths in docs users will copy

## Commit style

Short imperative subject; explain *why* in the body when needed.
