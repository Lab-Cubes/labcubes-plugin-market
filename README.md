# LabCubes Plugin Market

Public, repository-owned Codex plugin marketplace for LabCubes plugins.
The catalog distributes the plugins listed below.

Read [START-HERE.md](START-HERE.md) for the repository map and contribution path,
[the review guide](docs/REVIEW-GUIDE.md) before changing the catalog, and
[SECURITY.md](SECURITY.md) for the distribution trust boundary.

## Register the marketplace

```bash
codex plugin marketplace add Lab-Cubes/labcubes-plugin-market --ref main
```

For a local checkout, `codex plugin marketplace add .` registers that checkout.
Registration is optional when editing this repository and changes your local
Codex configuration.

## Available plugins

### Iris Console 0.1.2

Iris Console provides evidence-aware Australian property research, acquisition,
investment and development workflows through 18 coordinated Skills. See the
[plugin README](plugins/iris-console/README.md) for its contents and dependencies.

```bash
codex plugin add iris-console@labcubes-plugin-market
```

### Cypress-timeline 0.2.5

Create milestone progress presentations as interactive Web/HTML, MP4, or both.
Start from site/design references or an Australian address for a sourced,
hypothetical demolition-and-rebuild presentation.
Reports default to 30 seconds across milestones unless custom timing is supplied.
Starting images prefer actual site photos or faithful photo-derived renders,
using suitable REA capabilities and optional connected street-level sources.
The outer frame stays visible while the main picture crossfades. Prefer available
PixVerse workflows for generated media and use Sites for hosted delivery;
local existing-asset exports need neither connection.
An explicitly selected host image tool can also supply stage stills for local
HTML/MP4 composition; a working image tool does not imply a video endpoint.
See the [plugin README](plugins/cypress-timeline/README.md).

```bash
codex plugin add cypress-timeline@labcubes-plugin-market
```

## Structure and standards

The ordered catalog lives at `.agents/plugins/marketplace.json`. Add
`plugins/<plugin-name>/` only when a real plugin is ready to be listed. Catalog
source paths resolve from the repository root.

This repository distributes plugin files through Git; it has no hosted service,
database, or application build. Follow the applicable canonical
`InnoLotus.Standards` for engineering and security and `InnoLotus.Codebase` for
reusable implementation patterns. This initial scaffold follows
`innolotus-project-scaffolding`'s marketplace mode because the inspected Codebase
templates contain only .NET and Node.js templates.
