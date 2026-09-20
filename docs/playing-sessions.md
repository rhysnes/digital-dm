# Playing sessions

Skill: **digital-dm** (`skills/digital-dm/SKILL.md`).

## Session open

The agent should read:

1. `state/campaign.md`
2. `state/clocks.md` (if present)
3. `state/player-canon.md`
4. Active quests
5. Party sheets + inventory + currency
6. Current location (+ NPCs present)
7. Last `state/session-log.md` entry — **resume, don’t soft-reset**

## During play

- Ask for intent; roll when failure is interesting and stakes are real
- Offer only **sensible** actions (possible here, now, with current tools)
- Narrate plainly; match register to the campaign without purple mush
- **Yes, and…** player improv; write lasting facts to disk
- New recurring NPC/place/trader → create a file the same session
- Ignored pressures → tick clocks; world moves off-screen
- Digressions can become `module/episodes/`; main arc waits or evolves quietly
- OOC corrections (voice, logic) → fix immediately; update `rules/` if needed

## Session close (or end of a substantial beat)

1. Append keypoints to `state/session-log.md`
2. Update `state/campaign.md` (session #, location, flags, next hook)
3. Sync clocks, quests, inventories, currency, NPC attitudes
4. Flush improv into `state/player-canon.md` + entity files

## Non-negotiables

- Files win over memory
- Secrets in `module/secrets.md` / `[DM]` stay secret until earned
- Do not restart chargen or Chapter 1 if sheets/state already exist
- Do not replace the campaign’s locked deep antagonist framework
- Comedy permission ≠ comedy quota

## Starting play

Begin Chapter 1 / cold open only when the player says go (or `adventure_started` is already true and you’re resuming).
