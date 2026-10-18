# LabCubes Plugin Market

The official Git-based plugin marketplace for LabCubes.

## Add the marketplace

Run this command from the terminal available to Codex or the ChatGPT desktop app:

```bash
codex plugin marketplace add Lab-Cubes/labcubes-plugin-market --ref main
```

Restart the ChatGPT desktop app, open the Plugins Directory, and select
**LabCubes Plugin Market**. Git-backed marketplaces are supported by Codex and
the ChatGPT desktop app, not ChatGPT on the web or mobile apps.

## Repository layout

The marketplace catalog is stored at
`.agents/plugins/marketplace.json`. Plugin packages should live under
`plugins/<plugin-name>/` and provide a portable `plugin.json` manifest (or the
compatibility path `.codex-plugin/plugin.json`). Catalog sources must use
repository-relative paths such as `./plugins/example`.

The catalog is intentionally empty until the first LabCubes plugin is ready for
release.

See the [OpenAI plugin packaging documentation](https://developers.openai.com/plugins/build/plugins)
for the full manifest and marketplace schema.
