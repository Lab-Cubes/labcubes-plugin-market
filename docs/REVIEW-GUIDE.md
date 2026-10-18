# Marketplace review guide

Start with `.agents/plugins/marketplace.json`, then read each changed plugin's
manifest and README. Preserve the marketplace identifier and unrelated entries.

For a plugin addition or migration:

- Use `./plugins/<plugin-name>` relative to the repository root and verify the
  resolved path stays inside the repository.
- Match the directory and manifest identities; preserve the released version
  and package contents for a move. Check provenance hashes when supplied.
- Declare installation policy, authentication policy, and category in the
  catalog. Review declared dependencies, credentials, and external data flows.
- Verify referenced assets and Skills exist. Exclude private profiles,
  credentials, machine-specific paths, symlinks, and build artifacts.
- Explain purpose, impact, and verification in the pull request. Publish a
  destination before removing a previous distribution location.

For an empty catalog, check JSON syntax, the marketplace name, and that
`plugins` is an array:

```bash
python3 -m json.tool .agents/plugins/marketplace.json
git diff --check
```

Use the host's current plugin validator when available for real plugin entries.
If a referenced helper is unavailable, report that limitation and verify the
affected manifest, paths, assets, metadata, and provenance directly. This
catalog has no runtime build or dependency restore step.
