#!/usr/bin/env python3
"""Validate Cypress package identity, dependency metadata and catalog containment."""
import json
from pathlib import Path


def main() -> None:
    """Check source files without installing plugins or contacting providers."""
    root = Path(__file__).resolve().parents[1]
    catalog = json.loads((root / ".agents/plugins/marketplace.json").read_text())
    assert catalog["name"] == "labcubes-plugin-market"
    entries = [item for item in catalog["plugins"] if item["name"] == "cypress-timeline"]
    assert len(entries) == 1
    source = entries[0]["source"]["path"]
    assert source == "./plugins/cypress-timeline"
    package = (root / source).resolve()
    assert package.is_relative_to(root)
    portable = json.loads((package / "plugin.json").read_text())
    legacy = json.loads((package / ".codex-plugin/plugin.json").read_text())
    assert portable["$schema"] == "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json"
    assert portable["name"] == legacy["name"] == "cypress-timeline"
    assert portable["version"] == legacy["version"] == "0.1.1"
    interface = portable["extensions"]["com.openai"]["interface"]
    assert interface == legacy["interface"]
    assert len(interface["shortDescription"]) <= 30
    assert entries[0]["category"] == interface["category"] == "Creativity"
    assert entries[0]["policy"] == {"installation": "AVAILABLE", "authentication": "ON_INSTALL"}
    deps = portable["extensions"]["org.labcubes.timeline"]["workflowDependencies"]
    assert {dep["plugin"] for dep in deps} == {"pixverse@openai-curated-remote", "sites@openai-curated-remote"}
    assert legacy["extensions"]["org.labcubes.timeline"] == portable["extensions"]["org.labcubes.timeline"]
    skill = package / "skills/timeline"
    text = (skill / "SKILL.md").read_text()
    assert text.startswith("---\nname: timeline\n")
    assert "TODO" not in text
    for path in package.rglob("*"):
        assert not path.is_symlink(), path
        assert path.resolve().is_relative_to(package), path
        if path.is_file():
            assert path.suffix not in (".mp4", ".jpg", ".png", ".pyc"), path
    for required in ("scripts/build_timeline.py", "assets/player.html", "references/dependencies.md", "references/timeline-spec.md", "references/project-inputs.md", "agents/openai.yaml"):
        assert (skill / required).is_file(), required
    print("Cypress manifests, catalog, dependencies and package boundaries verified")


if __name__ == "__main__":
    main()
