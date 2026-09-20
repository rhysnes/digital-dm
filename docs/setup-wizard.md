# Setup Wizard

Used by skill **digital-dm-setup**. Full agent script: `skills/digital-dm-setup/references/setup-wizard.md`.

The wizard runs **before** scaffolding files (unless you say “skip wizard” and already gave full specs).

## Batches

### 1 — Frame
- Working title (or invent later)
- Rules system (e.g. D&D 5e loose)
- Solo PC vs party
- Campaign path / slug

### 2 — Tone & table
- Tone keywords
- Optional show palette (D&Dads / CR / NADDPOD / DnDIFN / none)
- Lines & veils
- Comedy: none / occasional in-universe / frequent  
  **Allowed ≠ forced** — the DM must not steer every scene toward jokes

### 3 — Setting
- Genre in your words
- Scope (town, region, ship + ports, multi-system, …)
- Magic or tech one-liner
- Must-include / must-exclude

### 4 — Storyline source (required fork)

| Option | Meaning |
|--------|---------|
| **A. Existing documentation** | Adapt files/books/paths you provide; don’t overwrite sacred canon |
| **B. Completely original** | Invent premise + secrets with you (agent offers 2–3 pitches) |
| **C. Hybrid** | Your lore stays; new main arc |
| **D. Reskin** | Named structure remounted in a new genre/skin |

### 5 — Play shape
- Arc structure (seasons, sandbox, mystery, crawl, shipboard, …)
- Narration density: terse / medium / lush
- PC: chargen / import sheet / stub
- First session: chargen only / soft open / cold open

## Confirmation

The agent reads back a one-paragraph card. Scaffolding starts only when you confirm.

## What gets written

| File | Content |
|------|---------|
| `state/session-0-brief.md` | Wizard answers |
| `state/campaign.md` | Flags including `wizard_complete: true` |
| `README.md` | Campaign bible pointer |
| `AGENT-HANDOFF.md` | Paste for future chats |
| `module/OVERVIEW.md` | Premise + arc map |
| `module/secrets.md` | DM-only framework |
| `rules/tone.md` | Table tone / comedy permission |
| `party/` | Sheet stubs or chargen notes |

Adventure play begins only when you say go (skill **digital-dm**).
