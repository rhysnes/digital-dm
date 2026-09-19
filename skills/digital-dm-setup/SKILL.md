---
name: digital-dm-setup
description: >-
  Setup wizard and scaffold for Digital DM campaigns. Asks leading questions on
  tone, theme, setting, system, and storyline source (existing docs vs original
  invention), then creates the campaign filesystem. Use when the user wants a
  new campaign, Session 0, Digital DM setup, or to initialize RPG tracking folders.
---

# Digital DM — Campaign Setup

Always start with the **Setup Wizard** unless the user says “skip wizard” and already provided full specs.

Full question script: [references/setup-wizard.md](references/setup-wizard.md)

## Phase A — Wizard (before writing files)

Ask in short batches (don’t dump 20 questions at once). Record answers; later write them into `state/session-0-brief.md` and the campaign bible.

### Batch 1 — Frame
1. Campaign working title (or “suggest one later”)
2. Rules system (e.g. D&D 5e, lightweight narrative, other)
3. Party size / solo PC?
4. Where to put files (default `~/DnD-Campaigns/<slug>/`)

### Batch 2 — Tone & table
5. Tone keywords (pick any): earnest, pulpy, horror, mystery, heroic, grounded, bit-friendly, dry…
6. Inspiration palette? (optional: D&Dads / CR / NADDPOD / DnDIFN / none / other)
7. Hard lines / soft lines / veils
8. How much comedy is welcome? (none / occasional in-universe / frequent) — remind: permission ≠ quota

### Batch 3 — Setting
9. Genre/setting: fantasy / sci-fi / modern / historical / other (user words)
10. Scope: single town, region, ship+ports, planar, sandbox…
11. Tech/magic level in one sentence
12. Anything that must appear or must never appear

### Batch 4 — Storyline source (critical fork)
Offer **exactly these options** (user may mix):

| Option | Meaning |
|--------|---------|
| **A. Existing documentation** | Use / adapt files or books the user points to (path, paste, or “campaign already on disk”) |
| **B. Completely original** | Invent a unique premise, arcs, and secrets with the user — no borrowed AP plot |
| **C. Hybrid** | Keep user’s setting docs / lore bible; invent a new main arc on top |
| **D. Reskin** | Take a known structure/seeds and remount into a new genre/skin (user must name source + target) |

For **A**: ask for paths or “wait, I’ll paste.” Do not invent over their canon.  
For **B**: brainstorm 2–3 premise pitches, let them pick/combine, then lock secrets in `module/secrets.md`.  
For **C/D**: clarify what is locked vs fair game to invent.

### Batch 5 — Play shape
13. Arc shape: seasonal TV, sandbox, mystery ladder, hexcrawl, ship campaign…
14. Session length preference / detail level
15. Start: chargen first vs ready-made PC vs “I have a sheet”

Confirm a one-paragraph **Session 0 summary** back to the user before scaffolding.

## Phase B — Scaffold

Only after confirmation:

1. Create `DEST` (confirm overwrite if exists).
2. Copy scaffold + seed templates (resolve `REPO` = this skill’s repo root, usually parent of `skills/`):

```bash
REPO="…"  # digital-dm repo root
DEST="…"  # campaign root
cp -a "$REPO/scaffold/." "$DEST/"
cp "$REPO/templates/campaign-state.md" "$DEST/state/campaign.md"
cp "$REPO/templates/session-log.md" "$DEST/state/session-log.md"
cp "$REPO/templates/clocks.md" "$DEST/state/clocks.md"
cp "$REPO/templates/player-canon.md" "$DEST/state/player-canon.md"
cp "$REPO/templates/session-0-brief.md" "$DEST/state/session-0-brief.md"
```

3. Fill from wizard answers (don’t leave empties when you know the content):
   - `state/session-0-brief.md` — wizard answers
   - `README.md` — tone, genre, how to use tree
   - `AGENT-HANDOFF.md` — from template
   - `module/OVERVIEW.md` — premise + arc map
   - `module/secrets.md` — DM-only framework (**B/C/D invent; A extract/adapt only**)
   - `rules/tone.md` — table tone + comedy permission from Batch 2
   - `party/` — sheet stubs or chargen notes
   - `state/campaign.md` — session 0 flags, `wizard_complete: true`

4. Tell the user the path; next skill for play = **digital-dm**. Begin adventure only when they say go.

## Do not

- Skip the storyline-source fork (A/B/C/D)
- Overwrite an existing campaign without explicit confirmation
- Steal a published AP plot under “original” without the user choosing **A** or **D** and naming it
- Put Cursor skills inside the campaign tree
