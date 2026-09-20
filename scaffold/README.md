# Campaign scaffold

Empty folder tree copied into a new campaign root by **digital-dm-setup**.

```bash
cp -a scaffold/. /path/to/your-campaign/
```

Then seed file bodies from `../templates/` (the setup skill does this for you).

## Included stubs

- `npcs/index.md`, `locations/index.md`, `traders/index.md`, `factions/index.md`
- `quests/active.md`, `dormant.md`, `completed.md`

Create `README.md`, `module/`, `party/`, and `state/` files from templates + wizard answers. See [docs/campaign-filesystem.md](../docs/campaign-filesystem.md).
