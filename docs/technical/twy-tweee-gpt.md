# twy-tweee-gpt

Custom GPT system for newsletter generation and class planning. Not a server — it's a ChatGPT Custom GPT that calls the twy-class-plans API.

**Repo:** `gnyrd/twy-tweee-gpt` → `/root/twy/tweee-gpt/`
**GPT:** [chatgpt.com/g/g-thtGYCFAR-tweee](https://chatgpt.com/g/g-thtGYCFAR-tweee)

## Architecture

TWEEE is a ChatGPT Custom GPT configured with:

1. **System prompt** — condensed instructions at `docs/guides/TWEEE-GPT-INSTRUCTIONS-CONDENSED.md`
2. **Knowledge files** — uploaded to GPT's knowledge store (not served via API)
3. **GPT Actions** — HTTP calls to the class-plans API at `classes.tiffanywood.yoga`

### API Endpoints Used

| Action | Endpoint |
|--------|----------|
| List plans | `GET /api/plans?from=&to=` |
| Get plan | `GET /api/plans/<date>` |
| Upsert plan | `POST /api/plans/<date>` |
| Batch upsert | `POST /api/plans/batch` |
| Year overview | `GET /api/overview` |
| Month overview | `GET /api/overview/<month>` |

OpenAPI spec served at `GET /openapi.yaml` on the class-plans dashboard.

## Knowledge Base

Located in `knowledge/`:

- `NEWSLETTER_VOICE_TRAINING.pdf` — 15 curated newsletters (113MB)
- `TIFFS_EVOLUTION.md` — Voice evolution timeline (2024–2025)
- `COMBINED_TRAINING_GUIDE.md` — Complete voice and philosophy guide
- 6 philosophy books (960 pages)
- 5 newsletter system guides
- 3 Anusara teaching materials (RTF)

Source newsletters in `sources/TWY Newsletters/` (2024: 66, 2025: 48).

## Mailchimp Integration

`send_to_mailchimp.py` creates Mailchimp campaigns from generated content. Config in `.mailchimp.env`.

`config.json` stores GPT configuration metadata.

## File Structure

```
twy-tweee-gpt/
├── config.json                  # GPT config
├── gpt.yaml                     # GPT action schema (read by class-plans)
├── send_to_mailchimp.py         # Mailchimp campaign creation
├── .mailchimp.env               # Mailchimp credentials (gitignored)
├── docs/guides/
│   ├── TWEEE-GPT-INSTRUCTIONS-CONDENSED.md  # Active system prompt
│   ├── TWEEE-GPT-INSTRUCTIONS.md            # Full reference
│   ├── GPT_SETUP_GUIDE.md
│   ├── GPT_ACTION_SETUP.md
│   └── MAILCHIMP_INTEGRATION.md
├── knowledge/                   # Upload to ChatGPT
├── sources/                     # Raw newsletter archives
├── scripts/                     # Utility scripts
└── tests/
```
