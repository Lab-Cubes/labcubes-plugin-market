# Start here

1. Read [README.md](README.md) for the purpose and registration commands.
2. Inspect [the catalog](.agents/plugins/marketplace.json), the authoritative list
   of plugins and their display order.
3. Follow [the review guide](docs/REVIEW-GUIDE.md) for plugin additions and moves.
4. Read [SECURITY.md](SECURITY.md) before publishing files.

## Repository map

| Path | Purpose |
| --- | --- |
| `.agents/plugins/marketplace.json` | Marketplace identity and ordered entries |
| `plugins/<plugin-name>/` | Plugin files, created when a plugin is added |
| `docs/REVIEW-GUIDE.md` | Review path and verification |
| `SECURITY.md` | Distribution and data boundaries |
| `LICENSE` | Existing repository license |

## Names and boundaries

The marketplace identifier is `labcubes-plugin-market`. A plugin identifier is
the name of its own directory and manifest; installation references use
`<plugin-name>@labcubes-plugin-market`.

The repository is a Git catalog. Codex retrieves listed plugin files and uses
the plugin's declared components. External integrations and credentials belong
to the user's host environment. Plugin behavior and dependencies must be
documented with each plugin.
