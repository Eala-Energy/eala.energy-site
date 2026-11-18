---
name: eala energy
description: Institutional briefing on warm paper: set type, sourced figures, plain structure. Built on branch redesign (18 Nov 2026): home, blog, privacy and 404 restyled; home sections keep their old structure and copy for now.
colors:
  paper: "#E8EDF1"
  sheet: "#F5F7F9"
  ink: "#17191C"
  ink-2: "#4F545A"
  rule: "#C2CCD5"
  slate: "#35546F"
  slate-deep: "#27425A"
  amber: "#B5650A"
  amber-tint: "#F3E2C8"
  error: "#A3261B"
typography:
  display:
    fontFamily: "Source Serif 4, Georgia, 'Times New Roman', serif"
    fontSize: "clamp(2.5rem, 4.6vw, 3.75rem)"
    fontWeight: 600
    lineHeight: 1.04
    letterSpacing: "-0.015em"
  h2:
    fontFamily: "Source Serif 4, Georgia, serif"
    fontSize: "clamp(1.75rem, 3vw, 2.5rem)"
    fontWeight: 600
    lineHeight: 1.12
    letterSpacing: "-0.01em"
  h3:
    fontFamily: "Public Sans, system-ui, sans-serif"
    fontSize: "1.125rem"
    fontWeight: 600
    lineHeight: 1.35
  lead:
    fontFamily: "Public Sans, system-ui, sans-serif"
    fontSize: "1.25rem"
    fontWeight: 400
    lineHeight: 1.55
  body:
    fontFamily: "Public Sans, system-ui, sans-serif"
    fontSize: "1.0625rem"
    fontWeight: 400
    lineHeight: 1.65
  figure:
    fontFamily: "Source Serif 4, Georgia, serif"
    fontSize: "clamp(2.25rem, 4vw, 3.25rem)"
    fontWeight: 600
    lineHeight: 1
  label:
    fontFamily: "Red Hat Mono, ui-monospace, Menlo, monospace"
    fontSize: "0.8125rem"
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: "0"
rounded:
  none: "0px"
  sm: "2px"
spacing:
  xs: "8px"
  sm: "16px"
  md: "24px"
  lg: "48px"
  xl: "96px"
  section: "clamp(72px, 10vw, 136px)"
components:
  button-primary:
    backgroundColor: "{colors.slate}"
    textColor: "{colors.sheet}"
    rounded: "{rounded.sm}"
    padding: "14px 22px"
  button-primary-hover:
    backgroundColor: "{colors.slate-deep}"
  button-secondary:
    backgroundColor: "{colors.paper}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    padding: "13px 21px"
  input:
    backgroundColor: "{colors.sheet}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    padding: "12px 14px"
    height: "48px"
---

# Design System: eala energy

> **Status: planned, not built.** Written on 17 Nov 2026 from `/impeccable shape` on branch `redesign`, from a direction the founder pinned (AUDIT.md directions A + C). The live site still runs the dark navy identity. When the build lands, `/impeccable document` re-records this file from the shipped code, and that version wins over this one.

## Overview

The site reads like the front page of a serious infrastructure briefing: the kind of paper a grid engineer, a fund analyst and a civil servant would each forward. The argument is carried by set type, sourced figures and plain structure. There is no hero drawing: a single-line diagram was built and dropped because it did not match how eala's sites actually connect (see Components).

- **Register:** neutral-institutional, engineering-led, calm. Authority comes from precision (sourced numbers, honest stage), never from effects.
- **Physical scene:** read on a laptop in an office or on a phone between meetings, in daylight. That is why the ground is light: a printed briefing on warm paper, not a control room.
- **Refuses:** the "AI infrastructure" category look (dark navy, cyan glow, wireframe globes, glass dashboards, particle fields), and also the softest version of this brief (cream paper, italic serif, tracked caps labels everywhere).
- **Motion:** a quiet ambient layer the founder asked to keep from the old site (18 Nov 2026): a slowly drifting grid and a particle field joined by thin lines, drawn on a fixed canvas behind the home page in slate at low opacity, no glow. Section blocks fade up once on scroll. Buttons change fill on hover and press 1px. On top of that (18 Nov 2026, founder asked for more of the old site's life): a slate wireframe sphere with two orbits and a particle shell in the hero's right columns (three.js 0.187, ESM + SRI, follows the pointer softly; abstract, it depicts no site or grid); line icons in small sheet tiles on the three platform columns, with a slate rule that draws across the column top, a sheet panel behind the column and a tilt towards the pointer of up to 6° on hover (fine pointers only); and a strip of abstract compute racks under Why it wins (slate outlines, load bars that sweep, one scan line). All of it stops under reduced motion and when the tab is hidden; blog, privacy and 404 stay still.

## Colors

Restrained strategy: tinted neutrals, one accent, one semantic signal.

### Primary
- **Slate** `#35546F` (deep `#27425A`): the only accent. Links, the primary button, figure numbers, chart bars. A Scottish slate-blue that also sits next to the logo's blues. 6.7:1 on paper.

### Signal (charts only)
- **Amber** `#B5650A`, tint `#F3E2C8`: means **curtailed energy** and nothing else. Used for the curtailment series in a chart (section 1). Not used anywhere yet. Never for text (3.7:1 on paper), buttons, links, highlights or decoration.

### Neutral
- **Paper** `#E8EDF1`: page ground. The slate accent diluted to a pale blue-grey, so ground, accent and drawings read as one family, like a drawing sheet (chosen 18 Nov 2026 over warm #EEECE6, which read as the saturated cream template, and over neutral #EDEFF0).
- **Sheet** `#F5F7F9`: raised surfaces (form fields, secondary-button hover, chart plates).
- **Ink** `#17191C`: text and drawing lines. 14.9:1 on paper.
- **Ink-2** `#4F545A`: secondary text, captions, source lines. 6.5:1 on paper.
- **Rule** `#C2CCD5`: hairlines and borders. Decorative only.
- **Error** `#A3261B`: form error text only.

### Named rules
- **One accent, one signal.** If something is coloured and it is not slate or curtailment amber, it is a bug.
- **Amber is a measurement.** It appears only where curtailed energy is plotted.
- **No gradients, glows, blur or transparency effects.** Flat fills and lines only.

## Typography

All faces are SIL OFL and self-hosted as latin-subset woff2 in `/fonts/`, with `font-display: swap` and real fallback stacks. No third-party font requests.

- **Source Serif 4** (600, optical size on): H1, H2, and large figures. The voice of a published paper: institutional, not bookish.
- **Public Sans** (400, 600): body, lead, H3, UI, form. A government-grade neutral grotesque, built for public-sector reading.
- **Red Hat Mono** (500): figure numbers, units, source markers, dates in lists, chart labels. Sentence case, no letter-spacing.

### Hierarchy
- H1 display, H2 for each numbered section, H3 in Public Sans for sub-points. One scale, as in the frontmatter, and nothing outside it.
- Body measure is 60–72 characters. Lead at 1.25rem for the first paragraph of the hero and of each section.
- Figures (3–10 MW, 6–8 hr, £1.9bn) are set in the serif at `figure` size, each with a mono unit line and a source marker.
- Headings take `text-wrap: balance`, body takes `text-wrap: pretty`.

### Named rules
- **No kickers.** No small uppercase label above a heading. If a section needs a number, the number belongs to the heading ("2. Where the wind goes"), because the sections really are a sequence.
- **Mono is for annotation, not decoration.** If a mono line is not a label, unit, figure number, date or source, it is set in Public Sans.

## Layout

- **Grid:** 12 columns, max content width 1200px, gutter 24px, side margins `max(16px, 4vw)`. Text columns span at most 7 columns, so reading width holds even on wide screens.
- **Rhythm:** sections separated by `spacing.section`, each opened by a full-width 1px rule in `rule` with the section number and title on the left margin. This is the briefing-paper structure.
- **Hero:** copy in the left 9 columns (H1 in 2 lines at 1440), the right side left as open paper. The facts line spans all 12 columns under a hairline. Below 960px everything is one column.
- **Footnotes:** every number on the home page carries a bracketed marker `[1]` linked to a numbered Sources list at the end of its section, the same pattern as the Insights posts.
- **Responsive:** one column at 390px. No horizontal scroll at 320px. Tap targets at least 44px.

## Elevation & Depth

Flat. Depth comes from paper versus sheet and from hairline rules, as on a printed page. No shadows except a 1px ink focus ring offset 3px. No sticky blur bars: the header is static and opaque.

## Shapes

Drawing-office geometry: square corners (`rounded.none`) for plates, figures and sections; `rounded.sm` (2px) only on buttons and inputs. No pills, no circles.

## Components

### Buttons
- **Primary:** slate fill, sheet text, 2px corners, Public Sans 600. Hover: slate-deep. Press: 1px down. Focus: 1px ink ring, 3px offset.
- **Secondary:** paper fill, 1px ink border, ink text.
- Labels are a verb plus an object: "Talk to eala", "Read the Insights".

### Hero diagram (removed)
- A single-line diagram with an "Export available / Curtailment event" toggle was built for the hero and removed on 18 Nov 2026: the drawn topology (wind farm, export limit, surplus routed into the node) did not match how eala's sites actually connect.
- Do not bring back a drawing of grid topology or power flows unless the founder supplies or approves the actual configuration.

### Figures and charts
- Large serif figure, a unit line in mono, a source marker.
- Charts are flat SVG with ink axes and slate bars. Amber is used only for curtailment series. Projected values are hatched, not faded, and labelled "projection".

### Inputs and fields
- Visible Public Sans labels above every field, 48px height, sheet fill, 1px rule border, ink focus ring. Errors in error colour under the field. The form keeps the Formspree endpoint and the privacy line.

### Navigation
- Static header: logo (it is transparent and was drawn for light grounds), wordmark "eala energy", then text links: Problem, Platform, Status, Insights, Contact.
- Below 720px the header shows the logo, Insights and Contact. No hamburger is needed for five anchors.

### Insights list
- The three latest posts: date (mono), title (serif, H3 size), one-line description, and a link to all Insights. Rows separated by rules, no cards.

## Do's and Don'ts

### Do
- Source every number on the home page, the way the Insights posts do.
- Keep amber for curtailed energy only, so it means the same thing everywhere.
- Say plainly what stage eala is at.
- Explain the mechanism in words and sourced figures. Do not decorate around it.
- Self-host every font, keep the consent-first analytics, and keep the Formspree form.

### Don't
- No three.js, WebGL, glows, gradients, glassmorphism, noise overlays, tilt or parallax beyond the exceptions below. The exceptions are the home-page background canvas, hero sphere, platform icons and rack strip described in Overview (founder decision, 18 Nov 2026); keep them slate, without glow, and still under reduced motion.
- Scroll reveal only as a single fade-up per block; without JS, content is visible at rest.
- No status lights, "live" badges, fake telemetry, or values that look like readings from an operating site.
- No kicker labels, pill eyebrows, icon tiles over headings, or rows of three identical cards.
- No photographs or renders that could be read as an eala site.
- Never lead with battery, BESS or storage. No financial jargon, and none of the dropped claims: "Low-cost input", "Lower structural energy cost…", "A stackable revenue model…".
- Do not use "AI + Grid" as a stat tile. It is a phrase, not a figure.

## Home page brief

From `/impeccable shape`, 17 Nov 2026. Direction pinned by the founder, so there was no concept roll: `seed: none (pinned)`, from "институциональный брифинг с инженерной однолинейной схемой в hero. Светлый тёплый фон, почти чёрный текст, один сланцево-синий акцент, янтарный только для curtailed-энергии на схеме".

**Job and audience.** All audiences on the messaging matrix at once (see PRODUCT.md): investors, energy and data-centre partners, public sector. Mode: **Persuade**, in the register of a briefing. The visitor should leave understanding the mechanism, believing eala is precise and honest about its stage, and knowing how to start a conversation.

**Sequence**

| # | Section | Content | Proof |
|---|---|---|---|
| — | Hero | H1 and lead. Primary "Talk to eala", secondary "Read the Insights". No drawing. Facts line below: **3–10 MW** modular site design · **6–8 hr** on-site energy continuity. | Approved figures only |
| 1 | The curtailment problem | Why Scottish wind is switched off: transmission south is full. Constraint costs £1.9bn in 2025-26 against £0.6bn in 2018-19, projected at £6.6–7.8bn a year by 2030 [NAO, Sep 2026]. 2026 costs passed £1bn two months earlier than in 2025 [Wasted Wind tracker, via SmartestEnergy, Aug 2026]. A small flat chart: 2018-19 → 2025-26 → 2030 range, hatched as a projection. | Sources already cited in the Insights post "Is storage arguing over the wrong purse?" |
| 2 | Mechanism and stack | Demand placed on the spot, behind the constraint. The three layers set as one stack (a typeset list, not a drawing of the site and not three cards): energy-resilience layer (sized for long curtailment events, 6–8 hr), containerised AI compute (inference-led, hardware-optional), orchestration that decides between compute, energy resilience and grid services ("AI + Grid" lives here as a phrase). Why it does not need the firm connection conventional data centres wait years for. | Existing approved copy |
| 3 | Where we are now | A dated register: incorporated 23 Mar 2026 (Companies House 17110070), plus **general progress lines whose exact wording the founder supplies**. No sites, partners, team or deployment status. | Companies House |
| 4 | Insights | The three latest posts, plus a link to all. | Generated from `blog/posts` |
| 5 | Contact | Who eala is speaking with. Email, LinkedIn, the form (labels, privacy line), registered office labelled as such. | — |
| — | Footer | Legal line (company number, registered office), Privacy, Insights. | Required in the UK |

**First viewport (1440×900).** Header. H1 across the 9 left columns, 3.75rem serif, 2 lines, then the lead and both buttons. The facts line closes the hero at about 700px, so the next section starts inside the first screen. At 390px: header, H1 (3 lines), lead, buttons and both facts in the first screen. Built on `redesign`, 18 Nov 2026.

**Signature interaction.** The hero sphere turning towards the pointer. The hero diagram and its toggle were removed (see Components).

**Scope.** Home page first. The blog template (`tools/build_blog.py`), `privacy.html` and `404.html` move to the same system in the same release, so the site never runs two identities. Fidelity: production page.

**Implementation consequences**
- New self-hosted fonts: Source Serif 4, Public Sans, Red Hat Mono, latin subsets, with OFL licences in `fonts/`. Inter can go once nothing uses it.
- Remove the three.js import map, both canvases and all keyframes.
- `tools/build_blog.py` gains a marker that writes the latest 3 posts into the home page, like the existing `blog:nav` and `blog:footer` markers.
- Keep untouched: GA4 Consent Mode with the `cookie_consent` key, the Formspree endpoint, JSON-LD, `llms.txt`, sitemap and IndexNow, the approved figures, the legal footer.

**Open decisions (the builder must not invent these)**
1. The exact "general progress" lines for section 3. The founder supplies the wording.
2. Final copy for the H1 and section intros. The builder drafts it from existing approved copy and the founder approves it before launch. The current H1 may stay.
3. Wordmark case: the logo bitmap reads "Eala Energy", while PRODUCT.md writes "eala energy" in lower case. Keep the bitmap as it is, or get a lower-case version?
4. Whether the 2030 projection appears in the chart or only in the text.
