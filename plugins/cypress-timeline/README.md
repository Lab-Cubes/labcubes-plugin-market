# Cypress-timeline 0.1.0

Turn start/end reference images and project milestones into an interactive Web
timeline, an MP4 progress report, or both. The outer presentation frame stays
visible while the main image changes. Chinese and English annotations are supported.

```bash
codex plugin add cypress-timeline@labcubes-plugin-market
```

Example requests:

- “用这张空地照片和完成图，估算节点，生成 Web 和 MP4 施工汇报。”
- “只做离线 HTML，外框固定，主图交叉渐变，可以暂停和拖动。”
- “保留已有时间线，只修复 MP4 转场时外框变黑的问题。”

Start with [the timeline Skill](skills/timeline/SKILL.md), then the
[input contract](skills/timeline/references/timeline-spec.md) and
[dependency contract](skills/timeline/references/dependencies.md).

PixVerse supplies new generated media and advanced video/audio editing. Sites
supplies hosted Web delivery. Dependencies are checked by the workflow; this
skills-only package does not automatically install other plugins. Existing local
images can produce offline HTML without either connection. The bundled MP4 path
requires Python 3.10+, FFmpeg/ffprobe and a language-capable font; it exports a
silent 1920×1080 keyframe report. Continuous generated motion is a separate,
explicit PixVerse route and may require account entitlement and credits.

One timeline JSON drives both formats. Web playback supports pause, scrub,
milestone selection, speed and fullscreen. HTML embeds assets for offline use.
The package contains no MCP server, backend, credentials or customer imagery.
Only user-authorized assets go to media providers or a published Site.

Run the repository checks with `python3 scripts/check_cypress.py` and
`python3 -m unittest discover -s tests -p 'test_cypress*.py' -v`.
Generated provider motion, Sites deployment and clean-host plugin installation
must be verified separately when used; local tests do not establish those results.
