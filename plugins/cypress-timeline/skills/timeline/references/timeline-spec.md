# Timeline specification

Use a UTF-8 JSON object. Asset paths resolve from the spec's directory and must
remain inside it, including through symlinks. PNG/JPEG/WebP only; the renderer
never follows remote image URLs or accepts HTML/SVG as image assets.

```json
{
  "title": "从空地到家",
  "subtitle": "单层住宅 · 预计现场施工约 10 个月",
  "disclosure": "AI 概念推演，非实际记录；不含设计审批及开工前准备。",
  "image_fit": "contain",
  "stages": [
    {"title":"空地现状","label":"开工前","week":0,"seconds":7.5,"description":"测量与场地准备。","image":"assets/start.jpg"},
    {"title":"验收交付","label":"第 44 周（假设）","week":44,"seconds":7.5,"description":"验收、整改、清洁与移交。","image":"assets/finish.jpg"}
  ]
}
```

`title`, `subtitle`, `disclosure` are required nonblank text. Each of 2–30 stages
requires `title`, `label`, `description`, `image`, and a finite nonnegative `week`.
Weeks must be nondecreasing; they are labels and do not imply actual completion.
`seconds` defaults to 7.5 and must be 1–120; total running time is at most 30 minutes.
`image_fit` is `contain` (default, preserve full image) or `cover` (crop to fill).

The progress track indicates presentation position, not a physical percent complete.
Text is escaped for HTML and passed as text files with FFmpeg expansion disabled.
No user text becomes a shell command or HTML markup. Keep title/subtitle under
45 Chinese characters and descriptions under 60 for the fixed 1080p composition;
adapt the template or line wrapping when longer material is necessary. Inspect
glyph coverage using the actual supplied font.

The renderer writes `timeline.html` and/or `timeline.mp4` into the explicit output
directory and can replace those generated filenames; use a fresh/versioned output
directory unless replacing the previous output was requested. Temporary rendering
files are removed on exit. The caller owns persistent output storage.

For this conversation's illustrative construction sequence, a reusable starting
schedule is foundations 1–6, frame 7–10, enclosure 11–20, interior 21–30, fit-off
31–36, landscape 37–40, inspection/handover 41–44 weeks. Re-estimate for each real
project; do not copy this schedule as a verified local industry average.
