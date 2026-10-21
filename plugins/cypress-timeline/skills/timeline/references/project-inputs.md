# Project input classification

Read this before choosing images, estimating dates or generating media for a
house-and-land package. A complete set of photographs and drawings is not an
entry requirement. Classify supplied evidence separately from intended work;
never infer permission to demolish from a photograph of an existing house.

- [Record the brief](#record-the-brief)
- [Route the available combinations](#route-the-available-combinations)
- [Build the applicable sequence](#build-the-applicable-sequence)
- [Presentation and acceptance](#presentation-and-acceptance)

## Record the brief

Keep a private project brief beside the working assets. Reuse known answers;
ask only for a decision that blocks the requested result. Unknown information
remains unknown. This is an agent intake contract, not a new renderer CLI or an
automatically parsed upload format. The renderer consumes prepared stage images
through [timeline.json](timeline-spec.md).

| Dimension | Values and meaning |
| --- | --- |
| Site state | `existing_building`, `vacant_land`, `under_construction`, `unknown`; record photo date and confidence where known |
| Intended work | `new_build`, `demolition_rebuild`, `renovation`, `undecided`; use the user's scope, independently of site state |
| Site evidence | List available photos, aerial/site survey, dimensions and user descriptions; absence of a survey is not proof of a boundary |
| Design availability | `none`, `partial`, `provided`, `unknown`; inventory individual documents rather than claiming that all drawings exist |
| Schedule basis | Forecast, actual record or mixed; intended start date if known, included preconstruction activities and the construction-week origin |
| Deliverable | `web`, `mp4`, `both`; language, audience and illustrative keyframes versus requested generated motion |

Inventory each asset with a project-local ID, role, source/reference, date or
revision if supplied, and known limitations. Roles include site photo, floor
plan, elevation, site plan, exterior render, interior render and style reference.
Keep design approval status separate: `unknown`, `concept`, `submitted` or
`approved`, with the supporting source and its scope. A supplied drawing or
sales render does not establish approval. Do not turn an unknown status into
"approved" or treat a style reference as the proposed building.

For assets prepared for the presentation, also record:

- Origin: supplied photograph, supplied drawing/render, generated concept or
  derived crop/composite; derived assets retain their parent reference IDs.
- Depicted time: observed date, forecast stage or illustrative state. A generated
  image of the initial site is illustrative, even if based on a real photograph.
- Target status: user-selected presentation target or still a proposal. Selection
  of a concept for this presentation is distinct from statutory approval.
- Coverage: which stage or design decision it can support and which it cannot.

## Route the available combinations

| Site and design evidence | Starting state | Required preparation | Final target |
| --- | --- | --- | --- |
| Existing house; no design | Supplied existing-house photo, if available | Resolve rebuild versus renovation; propose a labelled concept when design is in scope | Selected concept; never described as an existing approved design |
| Existing house; design supplied | Actual existing-house photo, if available | Reconcile supplied design with site evidence; add demolition/clearance only for a rebuild | Supplied matching exterior render, or a derived view tied to the available drawings |
| Vacant land; no design | Actual vacant-land photo, if available | Propose a concept within stated dimensions/preferences; disclose unknown site constraints | Selected concept with assumptions |
| Vacant land; design supplied | Actual vacant-land photo, if available | Preserve supplied design identity; create only missing views/stages | Supplied matching render or a clearly identified derived view |

`partial` designs follow the supplied-design route for the information they
actually contain, and the concept route only for missing decisions. In particular:

- A floor plan alone does not establish facade, roof form, finishes, levels or
  site placement. Preserve documented information; record inferred features.
- An elevation alone does not establish the entire floor plan. A marketing render
  alone does not establish dimensions, boundaries, approval or buildability.
- Conflicting revisions or a render inconsistent with drawings require resolving
  the controlling reference before generating dependent images. Keep useful
  independent work moving; do not silently combine incompatible versions.
- If there is no site photo, continue from permitted plans, aerials or a user
  description when adequate for the brief. Label any reconstructed initial view
  "illustrative starting state"; never claim it is an actual site photograph.
  Request a real photograph only when a faithful photographic start is required.
- If neither site evidence nor a design brief supports a property-specific
  result, produce a clearly generic proposal or request the minimum missing
  information. Do not invent an address, dimensions or a completed design.
- For an active site, start from the latest documented construction state. Earlier
  stages may appear as supplied history or labelled reconstructions, never as
  newly observed progress. Unknown state requires clarification before claiming
  demolition is complete or foundation work has begun.

If no finished image exists, its creation is a preparation step, not an input
rejection. Use the relevant image-generation workflow when in scope. Retain a
supplied target unchanged unless the user requests a redesign; a changed camera
view or missing facade requires a derived asset with declared assumptions. When
a design choice materially changes the output, establish the presentation target
before generating its intermediate construction stages. A request for a concept
authorizes concept proposals; it does not require repeated approval of routine
visual choices.

## Build the applicable sequence

For demolition/rebuild, begin with the existing house, then demolition and site
clearance, then the new-build sequence. Do not skip directly from the old house
to foundations while labelling the first image as vacant land. A vacant-land
project starts from its actual cleared state and omits a fictional demolition.
Renovation keeps the retained building and uses its actual work packages instead
of automatically applying a full rebuild sequence.

For a new build, use applicable milestones: foundations, frame, enclosure,
interior finishes, fit-off/installations, landscape and handover. Site conditions
and contract sequencing may overlap stages; missing photographs do not remove
real work from the schedule. Generate a conceptual stage, use an honest text/
diagram representation or mark the view unavailable rather than inventing an
observed record. The current renderer needs an image per displayed stage, so
prepare that representation before export.

Separate design, approvals, demolition/clearance and site construction in both
the estimate and its explanation. Record what "week 0" means. If demolition is
included in the displayed timeline, weeks cannot simultaneously mean only weeks
since foundation work without explaining the origin. Re-estimate total elapsed
time and conditional stages; do not add assumed durations to a supposedly
verified total. Missing design introduces design/approval uncertainty rather
than a promise that construction can start immediately. Use current relevant
sources for a real estimate and mark project-specific assumptions.

## Presentation and acceptance

Keep the actual supplied initial state and selected final target wherever they
exist. Mark forecast/concept stages and actual dated photos in their own stage
labels or descriptions, so a mixed presentation cannot imply all stages are
real. Include a concise overall disclosure about generated/derived imagery,
missing design information and the estimate's included periods. These annotations
go into the shared timeline JSON and remain visible in both Web and MP4.

Before export, confirm the site/work/design classification, reference inventory,
controlling design revision, target, conditional demolition and schedule origin.
Check that no concept is presented as an approved design, no simulated progress
is presented as observed, and no missing image caused a silent change of scope.
Only export/publicize assets authorized for that audience; private source paths,
full intake notes and unnecessary personal data stay out of the presentation.
