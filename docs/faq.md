# FAQ

## Does this include an adventure?

No. Toolkit only. Use the Setup Wizard (**B** original, **A** your docs, **C** hybrid, **D** reskin).

## Fantasy or sci-fi?

Either. Genre lives in the **campaign** folder. Skills stay genre-agnostic.

## Where do campaigns go?

Anywhere you like. Common pattern: `~/DnD-Campaigns/<slug>/`. Not inside this git repo unless you choose that (usually better separate).

## The agent isn’t writing files

Remind it: files are canon; cite `state/campaign.md`. Check the agent has write access to the campaign path.

## Skills don’t show up in Cursor

Run `./install.sh` again. Confirm symlinks exist under `~/.cursor/skills/digital-dm` and `digital-dm-setup`. Restart Cursor if needed.

## Can I use this outside Cursor?

The markdown filesystem works with any DM process. The `SKILL.md` packages are aimed at Cursor Agent Skills; other tools can read the same docs/templates.

## How do I back up a campaign?

Version the **campaign folder** (its own git repo, Nextcloud, etc.). Pulling `digital-dm` does not back up your story.

## Comedy / D&Dads energy?

Allowed when you say so in the wizard — in-universe, not a quota, not mid-seriousness if you forbade that. See [narration-and-tone.md](narration-and-tone.md).

## Is magic required?

No. Your Session 0 rules win (including “Clarke’s law only, no magic”).
