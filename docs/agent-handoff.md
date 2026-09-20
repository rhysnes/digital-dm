# Agent handoff

Long campaigns span many chats. Use a paste block so a fresh agent reloads canon from disk.

## Template

After setup, each campaign should have `AGENT-HANDOFF.md`. Starter text: `templates/AGENT-HANDOFF.md`.

Example:

```markdown
Act as Digital DM for **[CAMPAIGN TITLE]**.

Canon on disk — read before narrating:
- `[CAMPAIGN_ROOT]/README.md`
- `[CAMPAIGN_ROOT]/state/campaign.md`
- `[CAMPAIGN_ROOT]/module/OVERVIEW.md`
- Skill: **digital-dm**

Rules:
1. Files are source of truth; write lasting changes there.
2. Do not restart chargen if sheets exist.
3. Do not replace the locked deep plot framework in `module/secrets.md`.
4. Sensible options only; plain narration; yes-and improv → `state/player-canon.md`.
5. Resume from `state/campaign.md`.
```

## Tips

- Attach or `@` the campaign folder if your Cursor build supports it
- If the agent invents a parallel tree, stop it and point at the real path
- After big OOC rules changes, update `rules/` **and** the handoff so the next chat inherits them
