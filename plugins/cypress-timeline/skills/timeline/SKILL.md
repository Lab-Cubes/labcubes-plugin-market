---
name: timeline
description: "Create or revise milestone progress reports from available site photos, partial or complete designs, project stages, or dated photos. Use Cypress-timeline for house-and-land packages with an existing house or vacant land, construction progress, renovation timelines, interactive Web/HTML timelines, MP4 reports, or both."
---

# Cypress-timeline

Deliver a milestone presentation with persistent framing and transitions confined
to the main picture. Use one timeline and one asset set for Web and MP4 outputs.

## Resolve scope and dependencies

1. Infer the requested output: `web`, `mp4`, or `both`. Follow an explicit choice;
   otherwise default to both. Reuse the current project and previous accepted
   assets on revisions. Ask only for missing information that blocks the result.
2. Read [the dependency contract](references/dependencies.md). Use the installed
   **PixVerse** workflow for new video/media generation and the installed **Sites**
   workflow for hosted Web delivery. Resolve current skills at runtime; never use
   another user's machine paths, copied credentials or invented tool IDs.
3. For supplied images and offline HTML/local MP4 composition, use the bundled
   renderer without a PixVerse login or Sites deployment. Missing optional
   generation/hosting must not block independent work. Do not silently substitute
   keyframe slides for requested continuous generated construction footage.
4. Treat the package's dependency declaration as a workflow contract, not a native
   cross-plugin auto-installer. Never claim a dependency was installed without
   observing installation. Follow provider authentication and spending gates.

## Classify inputs before planning

Read [the project input contract](references/project-inputs.md). Classify site
state, intended work and design availability independently; inventory the actual
assets and their revisions. Accept incomplete inputs: an existing house or vacant
land can each have no design, partial drawings or a supplied finished render.
Do not require both a vacant-land photograph and an approved completion image.

For a rebuild, include demolition/clearance when still required; for renovation,
retain the building. If no target image exists, propose a labelled concept or
derive the missing view from supplied drawings within the authorized scope.
Distinguish a presentation target selected by the user from statutory approval.
Resolve material design conflicts before generating dependent stages. Record
each asset's origin and each stage's observed/forecast/illustrative status.

## Plan the timeline

- Identify the initial state, exact final target, milestones, timing, audience,
  language and source assets. Distinguish forecast, actual and illustrative states.
- For construction, separate design/approvals/preconstruction from site work.
  Estimate a range from relevant current evidence when facts are unknown; label
  the selected display schedule as an assumption. The included example is not a
  universal building duration or approval promise.
- Preserve the site's footprint, camera, tree and neighbouring geometry across
  exterior stages. Use a different viewpoint only when it conveys meaningful
  progress, such as interior fit-off. Label invented interiors as conceptual.
- Keep the user's actual starting photo and selected finished reference where
  supplied. Otherwise prepare clearly labelled illustrative starting/target
  images under the input contract. Generate only missing required assets; do not
  replace supplied design decisions or claim generated views are actual photos.
- Explain whether the deliverable is a keyframe presentation or generated motion.
  Keep factual annotations and exact typography in deterministic composition.

## Prepare assets

For new generation, read PixVerse's relevant video/image workflow and use its
current capability checks, reference chains, preflight and confirmation policy.
Avoid giant prompts that attempt every building stage in one uncontrolled shot.
Reuse accepted assets and keep bounded repairs within the agreed result.

Prepare one clean PNG/JPEG/WebP per stage. Crop contact-sheet panels through the
media editing workflow before passing them to the renderer. Do not ship clients'
images, profiles or reports back into this public plugin repository.

## Build and deliver

Read [the spec and renderer contract](references/timeline-spec.md). Write
`timeline.json` beside its asset directory, then run the bundled implementation:

```bash
python3 <skill-root>/scripts/build_timeline.py /project/timeline.json \
  --format both --output /project/deliverables --font /available/cjk-font.ttf
```

- Select `web` to build a self-contained, offline HTML without FFmpeg or a font.
- Select `mp4` or `both` with FFmpeg, ffprobe and a supplied language-capable font.
  Never install packages or download a font merely because this command needs it;
  use existing authorized setup scope or request the missing dependency.
- Use the bundled stable-frame template; it supports pause/resume, scrubbing,
  milestone selection, speed, fullscreen and reduced motion. Preserve structure
  during transition edits. Animate pictures only; never fade the outer shell.
- For hosted Web output, follow Sites' current create/update, access, packaging
  and publication flow. An offline HTML file is not a deployed Site. Respect a
  user request for offline/local-only work.
- The bundled MP4 is a silent keyframe report. For music, narration, main-picture
  motion clips or other advanced edits, continue through PixVerse's editing
  workflow, keep this stable-shell rule and preserve the accepted references.
- Validate the encoded duration, first/final state, text legibility and several
  transitions. Validate Web node selection, pause/scrub, image loading and mobile
  layout where the preview runtime allows. Report unperformed checks honestly.
- Save artifacts through the host's persistent file workflow. Return only the
  requested formats and actual saved/deployed locations. Keep unsuccessful
  generation or a missing format visible; never claim both were completed when
  only one exists.

## Acceptance criteria

The requested formats exist and open; input classification and conditional stages
match the evidence and intended work; supplied initial/final references are retained;
annotations and timing share the same source; external shell pixels never fade;
Web controls work; the MP4 probes successfully; estimated progress is not
misrepresented as an actual site record or engineering certification; inferred
designs are labelled and the schedule's included periods and origin are explicit.
