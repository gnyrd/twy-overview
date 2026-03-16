# Documentation Style Guide

Rules for maintaining TWY documentation. The automated doc agent MUST read and follow this file before making any changes.

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
