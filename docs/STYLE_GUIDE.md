# TWY Style Guide

Rules for the TWY documentation and for the dashboard pages. Every human and every minion reads this file before writing a doc or building a page.

## Audience

### User Guide (`docs/user-guide/`)
- Written for a non-technical yoga studio owner
- No CLI commands, file paths, script names, environment variables, or developer jargon
- Task-oriented: what the user does in the browser, not how the system works

### Technical Docs (`docs/technical/`)
- Written for developers maintaining the TWY systems
- Full technical detail is appropriate here

## Editorial Rules (DO NOT VIOLATE)

### No TWEEE or GPT references in user docs
Never mention TWEEE, ChatGPT, GPT, or any AI writing tool in user-facing docs. The `newsletters.md` page describes a generic Mailchimp workflow — keep it that way. TWEEE details belong only in technical docs.

### No emojis for UI icons
When referring to UI icons (e.g. the video camera icon on the calendar), describe them in plain text. Do not use emoji characters — no emoji matches the actual SVG icons used in the apps.

### Button names must match the UI exactly
Always verify button text against the actual template HTML before writing it in docs. Known examples:
- The thumbnail publish button text is **"Publish"** (not "Publish Thumbnail")
- The plan creation button is **"Add Class"** (in the top-right toolbar)
- Trim buttons are **"✂ Trim"** and **"✂ Trim & Publish"**

### Thumbnail → Trim & Publish ordering
The workflow order in the user guide is: select thumbnail → Trim & Publish → publish thumbnail. The code enforces this (`startTrim` requires `thumbSelectedFilename`). Do not reorder these steps.

### All site URLs must be clickable markdown links
Always use `[classes.tiffanywoodyoga.com](https://classes.tiffanywoodyoga.com)`, never bare text like `classes.tiffanywoodyoga.com`.

### Preview features stay out of user docs
Features gated behind the cookie-based `{% if preview %}` pattern belong only in technical docs, clearly marked as preview. Do not add them to the user guide.

## General Rules

### Be surgical
Only update docs that are actually affected by code changes. Do not rewrite entire documents.

### Preserve style
Match the existing tone, structure, and formatting of each doc file.

### Cross-references
If changes affect architecture (new services, changed ports, new dependencies), update `architecture.md`. If new env vars are added, update `environment-variables.md`.

### No fluff
Do not add speculative documentation. Only document what the code actually does.

## Dashboard UI (read before building or changing a page)

Added 2026-09-22 after a new page shipped with its create form at the bottom
of the list instead of a New button in the toolbar. Nothing here is new
policy: every rule below is read off the templates that were already live.
The guide had covered documentation only, so a page could be built without
ever meeting these, which is what happened.

The macOS HIG is the tiebreaker for anything this section does not settle
(`.claude/rules/twy.md`): the confirming button sits at the far right of an
action row, segmented controls stay compact, card headers are nouns.

### Which theme a page wears

- **Tiff-facing** (classes.tiffanywoodyoga.com): the warm gradient in
  `base_layout.html`, `linear-gradient(135deg, #f6d365 0%, #fda085 50%, #d4a574 100%)`.
- **JP-facing operational** (tech.tiffanywoodyoga.com): the blue gradient in
  `overview/static/style.css`,
  `linear-gradient(160deg, #a8d8f0 0%, #1a85c2 40%, #0d5a8a 70%, #062540 100%)`.
- A page in the classes app that is JP's overrides `body { background: ... }`
  in its own `page_styles` block. Classify a mixed-use page by its primary
  user, not by which app happens to host it.

### Page skeleton

Every page extends `base_layout.html` and fills its blocks:

| Block | Holds |
| --- | --- |
| `title` | `<Page> \| TWY Class Plans` |
| `site_title` | the page name, plus `labs_badge('<feature>')` when gated |
| `back_link` | one `<a class="back-link">` to the parent page |
| `header_right` | the page's primary action, top right |
| `page_styles` | page-scoped CSS only |
| `content` | the page body, inside `.card` |

### The primary action is a button in the top-right toolbar

`header_right` carries it, as `btn btn-primary`: **Add Class** on the calendar,
**New** on Emails and Blog. Secondary actions beside it are `btn btn-outline`.

A form for creating something is **its own page**, reached by that button, never
a form at the foot of the list and never a modal. Live examples: `/blog/new`,
`/journeys/new`, `/journeys/newsletters/new`, `/features/new`. The form page
carries its own `back_link` to the list.

### Forms

- The form lives in a `.card`.
- Labels: `display: block; font-size: 12px; text-transform: uppercase;
  letter-spacing: 0.04em; color: #777; margin: 0 0 6px`.
- Inputs and textareas: full width, `border: 1px solid #d5d5d5`, `border-radius: 8px`,
  `padding: 10px 12px`, `margin-bottom: 14px`, `font: inherit`.
- Side-by-side fields use a grid that collapses to one column under 760px.
- The action row is last: `.actions { display: flex; gap: 12px;
  align-items: center; justify-content: flex-end; margin-top: 8px; }`, with an
  optional `.hint` to the left of the button and the confirming button last.
- **No placeholder text in an input.** A label says what the field is; a
  placeholder that looks like a value reads as one (JP 2026-09-22).

### Buttons

`btn-primary` blue `#007aff` confirming, `btn-outline` white with a `#ccc`
border, `btn-ghost` translucent on a coloured header, `btn-success` `#34c759`,
`btn-danger` `#ff3b30`. All are defined in `base_layout.html`; never restyle
one in a page.

### Cards

`.card` is white, `border-radius: 12px`, `box-shadow: 0 4px 18px rgba(0,0,0,0.12)`,
`padding: 20px`. Page content goes inside one. A page-local class must not be
called `card`: it shadows the layout's and the page loses its panel.

### Gated surfaces

A page behind a contribution gate wears `labs_badge('<feature>')` in its
`site_title`, and its entry in the Labs column on the calendar uses
`labs_host('<feature>')` with `labs_disabled('<feature>')`. An off surface
stays visible, dimmed and inert (JP 2026-09-19); it does not vanish.
