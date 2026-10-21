# Dependency contract

| Dependency | Role | Required for |
| --- | --- | --- |
| `pixverse@openai-curated-remote` | Reference-controlled media generation, motion, audio and editorial work | New generated media or advanced media editing |
| `sites@openai-curated-remote` | Web preview and hosted delivery | Publishing a Web version |
| Python 3.10+ standard library | Timeline validation, offline HTML and MP4 orchestration | Bundled renderer |
| FFmpeg + ffprobe | Picture normalization, main-picture crossfades, H.264 export and verification | Bundled MP4 |
| Language-capable local TTF/OTF font | Controlled annotation rendering | Bundled MP4 |

Reviewed integration baselines: PixVerse 1.3.3 and Sites 1.1.0. Load the installed
version's instructions rather than assuming its CLI contract stayed unchanged.

The `org.labcubes.timeline` manifest extension records workflow dependencies.
It is descriptive metadata consumed by this skill; Agent Plugins 1.0 does not
define native cross-plugin dependency installation. It does not silently install,
authenticate, purchase, expose a server, or grant Sites/PixVerse access.

If PixVerse is unavailable, find its actual installed/discoverable plugin before
offering connection. Keep independent timeline planning and existing-asset exports
moving. If generated motion was requested, disclose that blocker; a still-image
report is a different output and needs the user's acceptance.

Use Sites for requested hosting. For a request specifically for an offline HTML,
use the local output and do not publish merely to satisfy a dependency.
