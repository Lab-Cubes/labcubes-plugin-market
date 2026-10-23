# Address-to-rebuild workflow

Accept an Australian street address or property/listing URL without requiring
uploaded photographs or a design. Research the correct site, prepare a sourced
brief, then use the existing input classification and Web/MP4 production flow.
This is an agent-operated research workflow using available tools, not a bundled
geocoder, scraper, cadastral API or guaranteed source of property photographs.

- [Resolve the target](#resolve-the-target)
- [Acquire available evidence](#acquire-available-evidence)
- [Choose the starting image](#choose-the-starting-image)
- [Prepare the site brief](#prepare-the-site-brief)
- [Create the simulation](#create-the-simulation)
- [Handle failures and verify](#handle-failures-and-verify)

## Resolve the target

1. Normalize the address while preserving street-number suffix, unit, suburb,
   state and postcode. Do not infer location from unrelated user profile data.
2. Discover currently available address/map/property tools. Prefer a suitable
   connected capability over browser access; use native Web search and source
   pages when the available connector cannot research this property type/status.
   Read tool restrictions before use. A for-sale search is not a universal
   address/land-record lookup and a sold-price workflow need not be run merely
   to locate a site. Last Sold, if installed, can supply address location and map
   capture; inspect its current tools rather than inventing API names or keys.
3. Match street number, unit, street and locality against source records. Retain
   candidate matches when incomplete. A geocoder result, rooftop point or common
   street address does not establish an independently owned parcel.
4. Classify `single_property`, `complex_or_shared_site` or `unresolved`. A base
   address can identify several lots or units; never assume the entire site or
   a neighbour is available for demolition. Ask for the smallest identifier
   needed when alternative targets materially change the simulation. Keep
   research/planning moving without depicting a selected property prematurely.

## Acquire available evidence

Use one permitted source or a combination. Prefer suitable REA plugin capabilities
for finding the starting photograph, but do not require REA and a map service
both to succeed. Open the source record behind a search result where accessible;
mark a snippet-only observation provisional. Keep URL, access date and record/
imagery date separately. Do not infer capture date from when a page was fetched.

| Source | Useful evidence | Boundary |
| --- | --- | --- |
| REA listing/property page or another permitted property source | Reported land area, site dimensions, existing dwelling, listing photographs or plans | Agent/marketing claims remain attributed claims; sale date and listing state do not prove current site condition |
| Connected map, aerial or street-view source | Address context, street relationship, visible buildings, access and trees | A pin, viewport, roof or fence is not a cadastral boundary; old/undated imagery cannot prove present demolition status |
| Official state/council parcel and planning sources | Parcel identifiers, recorded geometry/area and applicable planning information where retrievable | Map records are not a survey or development consent; unavailable layers remain unknown |
| User plans/photos/survey | Additional site evidence and intended design | Preserve supplied revision, date, scope and limitations |

For SA, use [SAPPA](https://sappa.plan.sa.gov.au/) and
[PlanSA's atlas guidance](https://plan.sa.gov.au/our_planning_system/plan_sa/south_australian_property_and_planning_atlas)
where accessible. For another jurisdiction, discover its actual official source.
Do not copy SA controls to another state. Official data may still be dated or
imprecise; [SAPPA's FAQ](https://plan.sa.gov.au/__data/assets/pdf_file/0007/799234/FAQ_-_South_Australian_Property_and_Planning_Atlas_SAPPA.pdf)
explains that parcel boundaries and aerial imagery may not align.

Retrieve a bounded amount of relevant evidence. Respect provider permissions,
attribution, permitted storage/export and media use. Do not bypass access blocks,
buy reports, register accounts or scrape at scale as part of ordinary research.
Use a permitted summary instead of exporting a restricted connector's raw data.
Do not download, alter, publish or send third-party photography/maps to a model
unless the available rights and provider workflow permit that use. Preserve
required attribution. When reuse is unavailable, retain source links and create
an independent, labelled schematic/concept from permitted factual information.

## Choose the starting image

1. Preserve an applicable user-supplied real site photo. Otherwise discover the
   installed REA plugin's actual lookup/image capabilities first and use them when
   they support the property and task. Prefer a street-facing exterior image of
   the matched site, not an interior, aerial, proposed development render or
   neighbouring property's photo. A for-sale-only tool cannot be treated as an
   arbitrary-address or sold/off-market photo endpoint; do not call it outside
   its scope, export restricted raw results or invent a photo-download tool.
2. If the connector cannot supply the image, inspect the correct listing/property
   page or another permitted property source using the host's supported research
   route. Check the address, unit/lot and visible frontage before using the image.
   A historical or undated listing photo can be a labelled historical/undated
   starting reference; it does not establish the site's current condition.
3. If no suitable reusable property photo is available, use Google Street View or another
   real street-level source only when its actual host integration is connected
   and authorized for this use. Record the panorama/image date where available,
   viewpoint and attribution. A Google satellite map or address pin is not a
   street-level image. A user's possible future API connection is not a current
   integration: report it as unavailable and do not invent endpoints, acquire
   keys, enable billing or add API infrastructure in the public skill package.
4. Verify permitted download, transformation, model input and output display for
   the chosen source. Viewing an image or receiving its URL does not establish
   these permissions. Retain required credits. If reuse is not permitted, keep
   the source link and explain that limitation rather than uploading the image.
5. Use the real image directly or render faithfully from it through the preferred
   media workflow. Keep the observed old house/site state, camera, road, driveway,
   neighbours and visible trees; do not beautify the starting state into a
   different building. Record the original reference and any visible uncertainty.
   Label the result as an original site photo, a photo-derived illustrative
   render, or an independent illustrative reconstruction, as appropriate.
6. Lock the initial real view before deriving the new-house concept and exterior
   stages. Preserve a supplied target's design decisions when adapting its view;
   resolve material conflicts with the source scene rather than replacing the
   source. Do not invent an old house by reversing the completed-house concept.
   If no reusable real image can be obtained, state what was checked and why it
   failed, then use the existing labelled-concept fallback when in scope. Ask
   for a photo or connected street-view source only when a faithful real-site
   starting view is required. Do not imply that a generic concept is street view.

Keep the source page/image reference, access date, capture date (or unknown),
matched property scope, selected camera, reuse/attribution conditions and reason
for choosing or rejecting each candidate in the private asset inventory. A derived
render retains its parent photo ID. Avoid putting keys or unrestricted connector
payloads in that inventory or in exported files.

## Prepare the site brief

Keep the brief in the private project working area, outside the plugin repo.
Record the supplied address, normalized candidate/resolved target, entity scope,
source inventory, research date, unknowns and conflicts. Do not collect owner,
occupant or contact information that the simulation does not need.

For each useful fact, record value/unit, evidence status, source, record date if
known and the scope it applies to. Status is `source_reported`, `corroborated`,
`assumed`, `conflicting` or `unknown`; these are evidence descriptions, not a
legal verification or numeric confidence score.

| Fact | Rule |
| --- | --- |
| Coordinates/address identity | Retain resolution accuracy and unit/lot ambiguity; geocoding bounds describe a display/result extent, not ownership |
| Land area | Distinguish land from floor/building area and unit entitlement from whole-site area; preserve conflicting values instead of averaging |
| Frontage, depth and shape | Use explicit dimensions or sourced geometry; area alone cannot determine them. Any rectangle or inferred dimension is a declared modelling assumption |
| Parcel identity/boundary | Include only when sourced at the correct property scope; otherwise unknown. A conceptual outline is not a cadastral polygon |
| Road orientation, access, slope and visible trees/buildings | Distinguish directly sourced observations from interpretation; unknown slope/services cannot be invented from a street pin |
| Site condition | Keep historical/undated observations separate from current evidence; a user-requested hypothetical demolition can proceed without claiming the old house still exists |
| Planning constraints | Record only what was actually retrieved for this site, with source/date; unknown setbacks, heritage/tree controls, easements and demolition permissions remain unresolved |

Display a concise sourced site summary before or with the proposed design:
matched address/scope, available area/dimensions, scene basis, important unknowns
and selected assumptions. Provide source links in the accompanying report/chat.
A claimed redevelopment opportunity or "subject to consent" does not establish
that the simulated design is allowable. Never turn missing controls into an
approval, assured dwelling count, buildable envelope or permitted demolition.

## Create the simulation

An explicit request to "simulate demolishing and rebuilding at this address"
establishes `demolition_rebuild` as a hypothetical scope; it does not authorize
physical demolition, applications or any other external write. An address by
itself does not specify renovation versus rebuilding; use the conversation's
scope or clarify only when necessary.

Feed the brief into [project input classification](project-inputs.md). Follow
[starting-image selection](#choose-the-starting-image) before generating the
target and dependent stages. Prefer the authorized real site image or a faithful
photo-derived render; use an independent illustrative view only after recording
the source-search outcome and fallback reason. Label source date/uncertainty and every
reconstruction. If the observed site is already vacant, omit pending demolition;
offer a labelled earlier hypothetical state only if useful to the requested story.

Reuse a supplied design. With none, propose a replacement house using known
site information and explicitly assumed size, form, placement and materials.
Do not imply a generated plan fits verified setbacks or preserves exact geometry
without evidence. Fix the presentation viewpoint and target before preparing
demolition/cleared-site, foundations, frame, enclosure, interiors, installation,
landscape and handover stages as applicable.

Use an explicitly assumed forecast with design/approval/demolition periods
separate from site construction. Include visible brief disclosures in the shared
timeline labels/descriptions: illustrative reconstruction or sourced historical
view, hypothetical replacement, unresolved boundaries/controls, and timing basis.
Keep exact typography and outer-frame transitions deterministic in both formats.
Source links and required media attribution must accompany delivered outputs;
keep necessary source names/credits in the image or stage text when required.
The renderer's JSON still contains prepared images and public annotations only;
no raw provider response or private brief is embedded automatically.

## Handle failures and verify

- No exact address/lot match: continue candidate research; do not generate a
  falsely site-specific proposal. Request a unit, postcode, listing or map pin
  only when the missing identifier blocks target selection.
- No REA page, unavailable connector or blocked page: try permitted alternative
  property/official sources and native Web search; do not invent a listing.
- No area or usable dimensions: proceed with a visibly schematic massing concept
  if useful and in scope, or request the minimum measurement for a fitted design.
- No reusable real site photo: record the REA/source-page search outcome and
  whether an authorized street-view integration exists. Explain any access,
  scope or reuse limitation; use a labelled independent reconstruction when in
  scope. Request a real photo or connection only when a faithful start is required.
- Conflicting data: retain source values and dates; select an expressly assumed
  scenario or resolve the conflict before asserting a fitted result.

Verify address and entity scope, evidence-to-fact traceability, observed versus
hypothetical state, source/media permissions, and that unknown boundaries and
controls remain visible. Verify starting-image provenance and the photo-derived
render's visible geometry against its parent; retain dates and credits in the
shared output. Check the prepared timeline through the usual Web/MP4
checks. Report address research, media generation, rendering, hosting and actual
planning verification separately; success in one does not establish the others.
