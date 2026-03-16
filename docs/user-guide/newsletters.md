# Newsletters

TWEEE is a custom GPT that generates Tiffany Wood Yoga newsletters. It pulls class plan data via API and produces content in Tiffany's voice, ready for Mailchimp distribution.

## How It Works

1. TWEEE GPT is configured as a ChatGPT Custom GPT at [chatgpt.com/g/g-thtGYCFAR-tweee](https://chatgpt.com/g/g-thtGYCFAR-tweee)
2. It has GPT Actions that call the class-plans API:
   - `GET /api/plans` — list upcoming class plans
   - `GET /api/plans/<date>` — get a specific plan
   - `GET /api/overview` — full-year monthly overview
   - `GET /api/overview/<month>` — single month overview
3. It uses a knowledge base of 15 curated newsletters, philosophy books, and voice training materials to write in Tiffany's style
4. Output is formatted for Mailchimp campaigns

## Using TWEEE

1. Open [TWEEE on ChatGPT](https://chatgpt.com/g/g-thtGYCFAR-tweee)
2. Ask it to write a newsletter for the upcoming week
3. TWEEE will pull the class plans via API and generate content
4. Review, edit, and paste into Mailchimp

## How Do I...

### Update the GPT's knowledge base

The knowledge files live in `twy-tweee-gpt/knowledge/`:

- `NEWSLETTER_VOICE_TRAINING.pdf` — 15 curated newsletters (113MB)
- `TIFFS_EVOLUTION.md` — Voice timeline
- `COMBINED_TRAINING_GUIDE.md` — Complete voice/philosophy guide
- Philosophy books and teaching materials

To update: edit the files locally, then upload to the ChatGPT GPT editor under "Knowledge".

### Update the GPT system prompt

The condensed system prompt is at:
`twy-tweee-gpt/docs/guides/TWEEE-GPT-INSTRUCTIONS-CONDENSED.md`

Copy this content into the "Instructions" field in the ChatGPT GPT editor.

### Check the API endpoints

The class-plans API serves TWEEE. Test from the server:

```bash
# List plans
curl -s https://classes.tiffanywood.yoga/api/plans | python3 -m json.tool

# Get a specific plan
curl -s https://classes.tiffanywood.yoga/api/plans/2026-03-15 | python3 -m json.tool

# Monthly overview
curl -s https://classes.tiffanywood.yoga/api/overview/3 | python3 -m json.tool
```

### Send the newsletter via Mailchimp

The `send_to_mailchimp.py` script in twy-tweee-gpt handles Mailchimp campaign creation. Configuration is in `.mailchimp.env`.

## GPT Configuration Reference

Full setup guides in the twy-tweee-gpt repo:

- `docs/guides/GPT_SETUP_GUIDE.md` — OpenAI configuration
- `docs/guides/GPT_ACTION_SETUP.md` — Mailchimp GPT Actions
- `docs/guides/MAILCHIMP_INTEGRATION.md` — Distribution system
