# WARP.md

## Recent Changes

### Auto-Deploy Webhook (2026-03-16)
- Added `/api/webhook/deploy` endpoint to app.py — receives GitHub webhook POSTs, verifies HMAC-SHA256 signature, runs `git pull --ff-only`
- New env var: `GITHUB_WEBHOOK_SECRET` — must match the secret configured in the GitHub webhook
- Both docs and tech instances share the same repo checkout, so either can receive the webhook

### User Guide Fixes (2026-03-16)
- Removed all TWEEE/GPT references from user-facing docs
- Made all site URLs clickable markdown links (classes.tiffanywoodyoga.com, clips.tiffanywoodyoga.com)
- Validated UI elements against actual templates and corrected inaccuracies:
  - Fixed "Publish Thumbnail (amber button)" → "Publish" (amber) — only available after Trim & Publish
  - Corrected workflow order: thumbnail must be selected BEFORE Trim & Publish (code enforces this)
  - Fixed "click the date → New Plan" → use "Add Class" toolbar button for dates without recordings
- Rewrote newsletters.md to remove TWEEE/ChatGPT dependency, now describes generic newsletter workflow with Mailchimp
