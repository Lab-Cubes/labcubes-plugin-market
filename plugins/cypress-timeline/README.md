# Cypress-timeline 0.2.5

Turn available site/design references and project milestones into an interactive Web
timeline, an MP4 progress report, or both. The outer presentation frame stays
visible while the main image changes. Chinese and English annotations are supported.

```bash
codex plugin add cypress-timeline@labcubes-plugin-market
```

Example requests:

- “输入这个澳洲地址，查地图和 REA 可用的土地资料，模拟拆除重建，做 Web 和 MP4。”
- “用这张空地照片和完成图，估算节点，生成 Web 和 MP4 施工汇报。”
- “只做离线 HTML，外框固定，主图交叉渐变，可以暂停和拖动。”
- “保留已有时间线，只修复 MP4 转场时外框变黑的问题。”

Start with [the timeline Skill](skills/timeline/SKILL.md), then the
[project input classification](skills/timeline/references/project-inputs.md),
[address-to-rebuild workflow](skills/timeline/references/address-rebuild.md),
[renderer contract](skills/timeline/references/timeline-spec.md) and
[dependency contract](skills/timeline/references/dependencies.md).

House-and-land inputs need not be complete. Classify the existing site separately
from design availability: an old house or vacant land can each have no design,
partial drawings or a supplied render. Preserve known design decisions, identify
generated concepts and inferred views, and include demolition only for the
applicable work. Separate preconstruction from site construction estimates.
These are agent workflow instructions; the renderer still takes prepared stage
images, not raw drawing uploads or an automatically verified intake form.

An Australian address or listing URL can start the workflow without uploads.
The agent resolves the property/lot scope, retrieves available map/property and
official evidence, then creates a sourced brief and hypothetical rebuild stages.
Land dimensions, source dates, uncertain boundaries and generated views remain
explicit. A missing REA record or reusable photo can fall back to other permitted
sources and a labelled concept. This uses host research capabilities; it does not
provide a standalone address API or guarantee approval, exact site geometry or
third-party imagery reuse. Source links and required credits accompany outputs.

Prefer an actual site photograph or a faithful render based on it for the starting
image. Retain supplied photos; otherwise first discover applicable REA plugin
capabilities, then permitted source-page photos, then an optional connected street-
level source such as Google Street View. Check the property, imagery date and
allowed reuse before passing a photo to any media provider. Lock this camera before
deriving the completion concept and exterior stages. Record photo-derived renders
and independent concepts distinctly; report source gaps before using a generic
reconstruction. Google Street View API integration is not included in this release.

Prefer PixVerse whenever its plugin/workflow is available for new images,
construction-stage stills, videos, audio and advanced media editing. Read its
workflow before choosing a generator. A present plugin with a missing runtime,
login or entitlement follows PixVerse setup/preflight rather than a silent
provider switch. Explicit user provider choices and host requirements take
precedence; disclose an absent plugin or unsupported capability before using
another provider. Existing accepted assets remain reusable without generation.
Sites supplies hosted Web delivery. Dependencies are checked by the workflow; this
skills-only package does not automatically install other plugins. Existing local
images can produce offline HTML without either connection. The bundled MP4 path
requires Python 3.10+, FFmpeg/ffprobe and a language-capable font; it exports a
silent 1920×1080 keyframe report. Continuous generated motion is a separate,
explicit PixVerse route and may require account entitlement and credits.

When the user selects a supported built-in image tool, follow its current host
workflow to generate the initial scene, completed target and missing stage stills,
then compose the same offline HTML and silent MP4 locally. This does not require
a built-in video endpoint and must not be described as generated continuous
footage. Inspect actual returned dimensions and do not invent a model ID or price.
PixVerse remains the default preference; a runtime or budget blocker alone does
not authorize a silent provider switch. Check the complete planned batch against
available balance and relevant prior usage before spending on a partial batch.

Check cleared structures, garage foundations, two-storey frame/roof continuity,
actual encoded crops and final embedded images after repairs. Preserve honest
limitations when preview/fullscreen or mobile checks are unavailable. Keep client
imagery, prompts and source handovers private rather than adding them here.

The default whole report is 30 seconds, divided equally across milestones and
shared by Web at 1× and MP4. Explicitly supplied stage timing remains effective;
revisions do not silently shorten a user's custom timing.

One timeline JSON drives both formats. Web playback supports pause, scrub,
milestone selection, speed and fullscreen. HTML embeds assets for offline use.
The package contains no MCP server, backend, credentials or customer imagery.
Only user-authorized assets go to media providers or a published Site.

Run the repository checks with `python3 scripts/check_cypress.py` and
`python3 -m unittest discover -s tests -p 'test_cypress*.py' -v`.
Generated provider motion, Sites deployment and clean-host plugin installation
must be verified separately when used; local tests do not establish those results.
