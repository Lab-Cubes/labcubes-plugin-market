# Timeline specification

First classify the available material using [the project input contract](project-inputs.md).
The private intake brief may contain incomplete or non-image design documents;
this renderer spec contains the prepared presentation stages, not raw uploads.
Missing site or completion photographs can be replaced by explicitly labelled
illustrative views when appropriate. Record actual/forecast/concept status in
each stage's label or description and relevant assumptions in `disclosure`;
both outputs use these annotations. Keep source inventory and private intake
notes outside this exported JSON. No intake parser or automatic design/approval
verification is implemented by the renderer.

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
    {"title":"空地现状","label":"开工前","week":0,"description":"测量与场地准备。","image":"assets/start.jpg"},
    {"title":"验收交付","label":"第 44 周（假设）","week":44,"description":"验收、整改、清洁与移交。","image":"assets/finish.jpg"}
  ]
}
```

`title`, `subtitle`, `disclosure` are required nonblank text. Each of 2–30 stages
requires `title`, `label`, `description`, `image`, and a finite nonnegative `week`.
Weeks must be nondecreasing; they are labels and do not imply actual completion.
Each omitted `seconds` defaults to 30 divided by the number of stages, producing
a 30-second report when all stages omit it (nine stages: 3⅓ seconds each).
Explicit stage durations are preserved and must be 1–120; mixing explicit and
omitted values can produce a total other than 30 seconds. For a requested total,
assign explicit durations that sum to that total. Maximum runtime is 30 minutes.
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

Inspect source images and actual encoded presentation crops. `cover` uses the
wide 1800×640 picture area and can clip a tall two-storey frame or roof; preserve
the locked camera while repairing the asset, or use `contain` when full-image
visibility is needed. Web's picture-only drift may tighten the crop further.
Check the roof throughout its displayed stage, not only the unscaled source.
Keep generation resolution separate from the 1920×1080 output canvas.

After replacing an image, rebuild both requested formats from the same selected
assets. Check final embedded Web image bytes against those files and inspect the
new encoded stage. Reuse still-applicable control tests when player code is
unchanged, but record which revision was tested and any final preview limitation.
An unsupported fullscreen API or blocked preview must not be labelled as passed.

For this conversation's illustrative construction sequence, a reusable starting
schedule is foundations 1–6, frame 7–10, enclosure 11–20, interior 21–30, fit-off
31–36, landscape 37–40, inspection/handover 41–44 weeks. Re-estimate for each real
project; do not copy this schedule as a verified local industry average.
